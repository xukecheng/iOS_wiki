##  Catching errors in Combine

22 Apr 2020

The Combine framework provides a declarative _Swift API_ for processing values
over time. It is another excellent framework that released side-by-side with
SwiftUI. I already covered it multiple times on my blog, but today I want to
talk about one of the key aspects of data processing. Today we will learn how
to handle errors during data processing using the Combine framework.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

####  The lifecycle of publisher

We use publishers to emit values over time. In the end, the publisher can
finish its work by sending the completion event or fail with an error. Neither
after completion nor after failure, the publisher can not emit new values.
Let’s take a look at the typical use-case that we might have in our apps.

    
    
    import SwiftUI
    
    struct SearchView: View {
        @ObservedObject var store: SearchStore
    
        var body: some View {
            NavigationView {
                List {
                    TextField("type something...", text: $store.query)
                    ForEach(store.repos, id: \.id) { repo in
                        Text(repo.name)
                    }
                }.navigationBarTitle("Search")
            }
        }
    }
    

In the example above, we have a view that allows users to enter a keyword and
the list that renders search results. We use a store object to bind a query
and repos array that holds search results. The main goal of the store object
is fetching repos matching the query using Github API.

    
    
    final class SearchStore: ObservableObject {
        @Published var query: String = ""
        @Published private(set) var repos: [Repo] = []
        private var cancellable: AnyCancellable?
    
        init(service: GithubService) {
            cancellable = $query
                .debounce(for: .seconds(0.5), scheduler: DispatchQueue.main)
                .flatMap { service.searchPublisher(matching: $0) }
                .subscribe(on: DispatchQueue.global())
                .receive(on: DispatchQueue.main)
                .sink(
                    receiveCompletion: { completion in
                        switch completion {
                        case .failure(let error): print("Error \(error)")
                        case .finished: print("Publisher is finished")
                        }
                },
                    receiveValue: { [weak self] in self?.repos = $0 }
            )
        }
    }
    

I don’t want to produce too many requests as user types a query. That’s why I
debounce it for 500ms. It means the publisher will wait at least 500ms
whenever the user stops typing and then publish a value. Then I can use a
_flatMap_ operator to run a search request using a query. In the end, I use
the _sink_ subscriber to assign search results to a store variable. As soon as
published variables change, SwiftUI will update the view to respect new data.

> To learn more about store concept, take a look at my [ “Modeling app state
> using Store objects in SwiftUI” ](/2019/09/04/modeling-app-state-using-
> store-objects-in-swiftui/) post.

We have one problem here, whenever the publisher fails with an error, nothing
will happen in the view. _Sink_ subscriber will just print the message in the
console.

####  Replace error with the value

Publishers provide us a few ways to handle errors in the chain. Let’s start
with the easiest one. Every publisher that can fail allows us to replace the
error with some default value using _replaceError_ operator. Let’s take a look
at how we can use it.

    
    
    init(service: GithubService) {
        $query
            .debounce(for: .seconds(0.5), scheduler: DispatchQueue.main)
            .flatMap { service.searchPublisher(matching: $0) }
            .replaceError(with: [])
            .subscribe(on: DispatchQueue.global())
            .receive(on: DispatchQueue.main)
            .assign(to: &$repos)
    }
    

As you can see, I have inserted _replaceError_ operator with an empty array.
Publisher will replace any error that might occur with an empty array and then
terminate. The downside here is that the publisher completes its work after an
error. It means our binding will not process new values. The user will type
further queries, but nothing will happen. Let’s see how we can fix that.

    
    
    init(service: GithubService) {
        $query
            .debounce(for: .seconds(0.5), scheduler: DispatchQueue.main)
            .flatMap { 
                service
                    .searchPublisher(matching: $0)
                    .replaceError(with: []) 
            }
            .subscribe(on: DispatchQueue.global())
            .receive(on: DispatchQueue.main)
            .assign(to: &$repos)
    }
    

To keep your publisher alive, you have to handle all errors outside of the
main chain. We can fix it by moving _replaceError_ operator inside the
_flatMap_ . As you can see, the publisher inside the _flatMap_ replaces an
error with a value and then terminate its work. The main chain is still alive
and emits new values.

####  Retry operator

Another useful operator that can help to solve an issue during value
processing is _retry_ . _Retry_ operator tries to process the value again and
again as many times as you specify.

    
    
    init(service: GithubService) {
        $query
            .debounce(for: .seconds(0.5), scheduler: DispatchQueue.main)
            .flatMap {
                service
                    .searchPublisher(matching: $0)
                    .retry(3)
                    .replaceError(with: [])
            }
            .subscribe(on: DispatchQueue.global())
            .receive(on: DispatchQueue.main)
            .assign(to: &$repos)
    }
    

As you can see in the example above, I ask the publisher to retry three times
before replacing an error with an empty array.

####  Catch operator

Both retry and replace error operators are built on top of the _catch_
operator. The _catch_ operator allows us to replace a failed publisher with a
new one. After that, the chain will use the new publisher to emit values.

    
    
    init(service: GithubService) {
        $query
            .debounce(for: .seconds(0.5), scheduler: DispatchQueue.main)
            .flatMap {
                service
                    .searchPublisher(matching: $0)
                    .catch { error -> AnyPublisher<[Repo], Never> in
                        if error is URLError {
                            return Just([])
                                .eraseToAnyPublisher()
                        } else {
                            return Empty(completeImmediately: true)
                                .eraseToAnyPublisher()
                        }
                }
            }
            .subscribe(on: DispatchQueue.global())
            .receive(on: DispatchQueue.main)
            .assign(to: &$repos)
    }
    

Another great thing about the _catch_ operator is the opportunity to access
the error and return a new publisher after inspecting the error.

####  Conclusion

The Combine is the framework that I use in all of my apps. It has a high
performance and friendly _Swift API_ . Sometimes it is hard to debug errors in
the Combine publisher chains. I hope this post gave you more information on
the publisher’s lifecycle and explained to you how to catch the errors. Feel
free to follow me on [ Twitter ](https://twitter.com/mecid) and ask your
questions related to this post. Thanks for reading, and see you next week!

