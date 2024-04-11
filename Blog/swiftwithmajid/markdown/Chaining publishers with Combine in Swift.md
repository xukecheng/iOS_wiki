##  Chaining publishers with Combine in Swift

04 May 2021

The Combine framework provides you a bunch of operators to map, filter, and
chain asynchronous operations. This week I want to focus on the chaining
asynchronous jobs using two main operators that the Combine framework provides
us. We will learn how to use _flatMap_ and _switchToLatest_ operators to chain
asynchronous tasks in a declarative way.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

####  Chaining basics with the flatMap operator

The _flatMap_ operator allows us to take the result of one publisher, pass it
to another and run the second publisher. We can use it to chain two different
publishers. Let’s take a look at how we can use it.

    
    
    final class GithubService {
        private let session: URLSession
        private let decoder: JSONDecoder
    
        init(session: URLSession = .shared, decoder: JSONDecoder = .init()) {
            self.session = session
            self.decoder = decoder
        }
    
        func searchPublisher(matching query: String) -> AnyPublisher<[Repo], Error> {
            // some code here
        }
    }
    
    final class SearchViewModel: ObservableObject {
        @Published var query: String = ""
        @Published private(set) var repos: [Repo] = []
    
        private let service = GithubService()
    
        init() {
            $query
                .flatMap { 
                    self.service.searchPublisher(matching: $0)
                        .replaceError(with: []) 
                }
                .receive(on: DispatchQueue.main)
                .assign(to: &$repos)
        }
    }
    

As you can see in the example above, we create the _SearchViewModel_ class
that conforms to _ObservableObject_ . Here we define two properties query and
repos. @ _Published_ property wrapper automatically provides a publisher for
property and allows us to access it via projected value using **$** sign.

> To learn more about designing API with Combine publishers, take a look at my
> [ “Designing API using Combine framework” ](/2021/04/07/designing-api-using-
> combine-framework/) post.

In the _SearchViewModel_ initializer, we use the _flatMap_ operator to pass
the value of query publisher and generate a new search publisher using the
provided query. Then we use the _assign_ operator to save the result of the
search operation in the repos property.

    
    
    struct ContentView: View {
        @StateObject var viewModel = SearchViewModel()
    
        var body: some View {
            NavigationView {
                List {
                    TextField("Query", text: $viewModel.query)
                    ForEach(viewModel.repos, id: \.id) { repo in
                        VStack(alignment: .leading) {
                            Text(repo.name)
                                .font(.headline)
                            if let description = repo.description {
                                Text(description)
                                    .foregroundColor(.secondary)
                            }
                        }
                    }
                }.navigationTitle("Search")
            }
        }
    }
    

Now we can use the _SearchViewModel_ in our SwiftUI app to implement a GitHub
repos search screen. Here we have a SwiftUI view that contains a text field
for query terms and a list of results.

_SearchViewModel_ will make a network request as soon as the user types
something in the query text field. Every new character in the text field
generates a new API request. Usually, we want to delay requests till user
typing. We can achieve this behavior by using _debounce_ operator on query
publisher in the _SearchViewModel_ .

    
    
    final class SearchViewModel: ObservableObject {
        @Published var query: String = ""
        @Published private(set) var repos: [Repo] = []
    
        private let service = GithubService()
    
        init() {
            $query
                .debounce(for: 0.5, scheduler: DispatchQueue.main)
                .flatMap { 
                    self.service.searchPublisher(matching: $0)
                        .replaceError(with: []) 
                }
                .receive(on: DispatchQueue.main)
                .assign(to: &$repos)
        }
    }
    

The _debounce_ operator blocks the chain for a time interval that you provide
and doesn’t emit any values in that period of time. It emits the latest value
after the timeout that you provide. We can significantly reduce the number of
network requests we make using _debounce_ operator.

> To learn more about the set of operators that the Combine framework provides
> us, take a look at my [ “Catching errors in Combine” ](/2020/04/22/catching-
> errors-in-combine/) post.

####  Advanced chaining with switchToLatest operator

Assume that you have a situation where a user types two queries in a sequence,
but the network delays the first one, and the second one finishes earlier. The
view represents the search result for the second request, but after a decent
amount of time, the first query finishes, and the data appears on the screen
by replacing the results of the second query.

Usually, we want to present the results of the latest query and ignore the
previous attempts. We can’t achieve that with the _flatMap_ operator, and
especially for this case, the Combine framework provides us the
_switchToLatest_ operator.

    
    
    final class SearchViewModel: ObservableObject {
        @Published var query: String = ""
        @Published private(set) var repos: [Repo] = []
    
        private let service = GithubService()
    
        init() {
            $query
                .debounce(for: 0.5, scheduler: DispatchQueue.main)
                .map { 
                    self.service.searchPublisher(matching: $0)
                        .replaceError(with: [])
                }
                .switchToLatest()
                .receive(on: DispatchQueue.main)
                .assign(to: &$repos)
        }
    }
    

In the example above, we refactored our _SearchViewModel_ to use the
_switchToLatest_ operator. The _switchToLatest_ operator is designed to work
with a publisher that emits other publishers. That’s why we use the _map_
operator to transform our publisher into the publisher that emits search
publishers. Then we attach the _switchToLatest_ operator flattening the stream
of publishers and delivering results only from the latest one.

####  Conclusion

This week we learned about two different ways of chaining asynchronous
operations with the Combine framework. Usually, the _flatMap_ operator is what
you need to chain multiple operations. When you should do some work as a
response to a user action, you should use the combination of _map_ and
_switchToLatest_ operators to deliver the latest results. I hope you enjoy the
post. Feel free to follow me on [ Twitter ](https://twitter.com/mecid) and ask
your questions related to this post. Thanks for reading, and see you next
week!

