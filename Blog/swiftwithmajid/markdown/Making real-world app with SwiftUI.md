##  Making real-world app with SwiftUI

05 Jun 2019

That is WWDC week: everybody is so excited about so many new things like
SwiftUI, Dark Mode, updateable Core ML models, etc. I will try to cover all
the new stuff during the upcoming weeks. Let’s start with SwiftUI. SwiftUI is
an entirely new approach to building apps for the Apple ecosystem.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

SwiftUI is a declarative Component-Oriented framework. You have to forget
about MVC where you have controllers mediating between view and model. All we
have in SwiftUI is a state and view derived from the state. As soon as your
state changes SwiftUI rebuild UI for that state changes. Apple team did an
excellent job by providing so beautiful [ tutorial page
](https://developer.apple.com/tutorials/swiftui/) for SwiftUI. It covers a lot
of stuff like Layout, Interfacing with UIKit, etc.

I will try to show you real-world app example written entirely in SwiftUI.
Let’s build an app searching for Github repos. We need a screen with a text
field for typing a query and a list of repos which comes from the search
query. I assume that you have already read the SwiftUI documentation because
I’m not going to describe basics, I will try to show something that
documentation didn’t covers.

Let’s start by building the _GithubService_ class, which creates a search
request and Repo struct, which represents a Github repository.

    
    
    struct Repo: Decodable, Identifiable {
        var id: Int
        let name: String
        let description: String
    }
    
    struct SearchResponse: Decodable {
        let items: [Repo]
    }
    
    class GithubService {
        private let session: URLSession
        private let decoder: JSONDecoder
    
        init(session: URLSession = .shared, decoder: JSONDecoder = .init()) {
            self.session = session
            self.decoder = decoder
        }
    
        func search(matching query: String, handler: @escaping (Result<[Repo], Error>) -> Void) {
            guard
                var urlComponents = URLComponents(string: "https://api.github.com/search/repositories")
                else { preconditionFailure("Can't create url components...") }
    
            urlComponents.queryItems = [
                URLQueryItem(name: "q", value: query)
            ]
    
            guard
                let url = urlComponents.url
                else { preconditionFailure("Can't create url from url components...") }
    
            session.dataTask(with: url) { [weak self] data, _, error in
                if let error = error {
                    handler(.failure(error))
                } else {
                    do {
                        let data = data ?? Data()
                        let response = try self?.decoder.decode(SearchResponse.self, from: data)
                        handler(.success(response?.items ?? []))
                    } catch {
                        handler(.failure(error))
                    }
                }
            }.resume()
        }
    }
    

Our _Repo_ struct has only a few fields, but it is enough for our sample. If
we want to use our _Repo_ struct as the model which should be used by SwiftUI
to build a View it has to conform to _Identifiable_ protocol. The only
requirement of _Identifiable_ protocol is id property, which has to be a
_Hashable_ value.

Now we can start implementing view which represents _Repo_ row in our list of
repos. We will use a vertical stack with two text labels.

    
    
    struct RepoRow: View {
        let repo: Repo
    
        var body: some View {
            VStack(alignment: .leading) {
                Text(repo.name)
                    .font(.headline)
                Text(repo.description)
                    .font(.subheadline)
            }
        }
    }
    

Let’s move to our SearchView which describes entire the screen.

    
    
    struct SearchView : View {
        @State private var query: String = "Swift"
        @EnvironmentObject var repoStore: ReposStore
    
        var body: some View {
            NavigationView {
                List {
                    TextField("Type something...", text: $query, onCommit: fetch)
                    ForEach(repoStore.repos) { repo in
                        RepoRow(repo: repo)
                    }
                }.navigationBarTitle(Text("Search"))
            }.onAppear(perform: fetch)
        }
    
        private func fetch() {
            repoStore.fetch(matching: query)
        }
    }
    

Here we have a query field which is marked as _@State_ . It means that this
view is derived from this state, and as soon as state changes, SwiftUI
rebuilds the view. SwiftUI uses diffing algorithm to understand changes and
update only corresponding views. SwiftUI stores all the fields marked as
_@State_ in special separated memory, where only corresponded view can access
and update them. _@State_ is a new Swift feature called Property Wrapper, more
about this feature you can read in [ the proposal
](https://github.com/apple/swift-
evolution/blob/master/proposals/0258-property-delegates.md) . The exciting
aspect is the usage of _$query_ , It means to get a reference for property
wrapper, not value itself. We use it to connect _TextField_ and _query_
variable in two way binding.

Another interesting fact here is _@EnvironmentObject_ . It is a part of
feature called _Environment_ . You can populate your _Environment_ with all
needed service classes and then access them from any view inside that
_Environment_ . The _Environment_ is the right way of Dependency Injection
with SwiftUI.

    
    
    import Foundation
    import Combine
    
    final class ReposStore: ObservableObject {
        @Published private(set) var repos: [Repo] = []
    
        private let service: GithubService
        init(service: GithubService) {
            self.service = service
        }
    
        func fetch(matching query: String) {
            service.search(matching: query) { [weak self] result in
                DispatchQueue.main.async {
                    switch result {
                    case .success(let repos): self?.repos = repos
                    case .failure: self?.repos = []
                    }
                }
            }
        }
    }
    

_ReposStore_ class should conform _ObservableObject_ protocol. It makes
possible to use it inside _Environment_ and rebuild view as soon as any
property marked as _@Published_ changes.

The main difference between _@State_ and _@EnvironmentObject_ is that _@State_
is accessible only to a particular view, in opposite _@EnvironmentObject_
available for every view inside the _Environment_ . But both of them used by
SwiftUI to track changes and rebuild views as soon as changes appear.

    
    
    class SceneDelegate: UIResponder, UIWindowSceneDelegate {
    
        var window: UIWindow?
    
        func scene(_ scene: UIScene, willConnectTo session: UISceneSession, options connectionOptions: UIScene.ConnectionOptions) {
            let window = UIWindow(frame: UIScreen.main.bounds)
            let store = ReposStore(service: .init())
            window.rootViewController = UIHostingController(
                rootView: SearchView().environmentObject(store)
            )
            self.window = window
            window.makeKeyAndVisible()
        }
    }
    

And this is how we can start our SwiftUI app with defined _Environment_ .

####  Conclusion

This week we talked about an entirely new approach in the iOS development
world. I will try to cover more WWDC topics in the upcoming weeks. Feel free
to follow me on [ Twitter ](https://twitter.com/mecid) and ask your questions
related to this post. Thanks for reading and see you next week!

