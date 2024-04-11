##  Microapps architecture in Swift. Dependency Injection.

02 Feb 2022

We covered a lot of things related to microapps architecture in Swift during
the last month. I would love to finalize the series of posts by touching
another essential edge of the approach: Dependency Injection. This week we
will learn how to inject the dependencies into feature modules to improve
testability and facilitate Xcode previews.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

As we told before, we should build our feature modules as completely isolated
apps. That’s why we call them microapps. Every microapp can have its
architecture or state management approach depending on the feature complexity.
You can use MVVM in one module or unidirectional flow in another module.

> To learn more about unidirectional flow, take a look at my [ “Redux-like
> state container in SwiftUI” ](/2019/09/18/redux-like-state-container-in-
> swiftui/) post.

Feature modules shouldn’t implement low-level functionality like networking or
caching. Feature modules should define the dependencies needed, and the app
coordinator or container fulfills them. Let’s take a look at some examples.

Assume that we are working on a search feature module. We need to make an API
request to search for the items matching our query. We also need to fetch
recent queries to show query history. Let’s start with defining the view model
for our search view.

    
    
    @MainActor public final class SearchViewModel: ObservableObject {
        public struct Dependencies {
            var search: (String) async throws -> [String]
            var fetchRecent: () async throws -> [String]
        }
    
        let dependencies: Dependencies
        public init(dependencies: Dependencies) {
            self.dependencies = dependencies
        }
    }
    

As you can see in the example above, we create the _SearchViewModel_ that
defines the _Dependencies_ type. The _Dependencies_ struct list all the low-
level pieces that we need to implement the functionality of our view model.
Now we can move on to fulfill the logic we need in our _SearchView_ .

    
    
    @MainActor public final class SearchViewModel: ObservableObject {
        public struct Dependencies {
            var search: (String) async throws -> [String]
            var fetchRecent: () async throws -> [String]
        }
    
        let dependencies: Dependencies
        public init(dependencies: Dependencies) {
            self.dependencies = dependencies
        }
    
        @Published private(set) var items: [String] = []
        @Published private(set) var recent: [String] = []
    
        func fetchRecent() async {
            do {
                recent = try await dependencies.fetchRecent()
            } catch {
                recent = []
            }
        }
    
        func search(matching query: String) async {
            do {
                items = try await dependencies.search(query)
            } catch {
                items = []
            }
        }
    }
    

This approach allows us to expose only necessary low-level logic to our view
model. The _SearchViewModel_ type defines its own set of dependencies and
requires them to compile.

In another case, the _SearchService_ type might implement different search
endpoint functions, and we can pass the instance inside the _SearchViewModel_
. The downside of this approach is that the _SearchViewModel_ type will have
access to all the parts of the _SearchService_ type, even if it doesn’t need
them.

    
    
    public struct SearchView: View {
        @ObservedObject var viewModel: SearchViewModel
        @State private var query: String = ""
    
        public init(viewModel: SearchViewModel) {
            self.viewModel = viewModel
        }
    
        public var body: some View {
            List(viewModel.items, id: \.self) { item in
                Text(item)
            }
            .navigationTitle("Search")
            .searchable(text: $query) {
                ForEach(viewModel.recent, id: \.self) { query in
                    Text(query)
                        .searchCompletion(query)
                }
            }
            .onSubmit(of: .search) {
                Task {
                    await viewModel.search(matching: query)
                }
            }
            .task { await viewModel.fetchRecent() }
        }
    }
    

> To learn more about the _searchable_ view modifier, take a look at my [
> “Mastering search in SwiftUI” ](/2021/06/23/mastering-search-in-swiftui/)
> post.

Another benefit of the approach we describe in this post is the opportunity to
easily mock dependencies to write unit tests and run previews in Xcode.

    
    
    extension SearchViewModel.Dependencies {
        static let mock: Self = .init(
            search: { _ in ["Search Item 1", "Search Item 2"] },
            fetchRecent: { ["query1", "query2"] }
        )
    }
    
    struct SearchView_Previews: PreviewProvider {
        static var previews: some View {
            NavigationView {
                SearchView(
                    viewModel: .init(
                        dependencies: .mock
                    )
                )
            }
        }
    }
    

Now let’s talk about where to store the whole app dependencies. Usually, we
have a container that initializes and keeps all the app’s services. We can
store it in the _AppDelegate_ or inside the root view of a SwiftUI app.

    
    
    struct SearchService {
        func search(matching query: String) async throws -> [String] {
            // ...
        }
    
        func fetchRecent() async throws -> [String] {
            // ...
        }
    
        func save(query: String) async throws {
            // ...
        }
    
        func delete(query: String) async throws {
            // ...
        }
    }
    
    struct AppDependencies {
        let searchService: SearchService
        let storage: Storage
    }
    
    extension AppDependencies {
        var search: SearchViewModel.Dependencies {
            .init(
                search: searchService.search,
                fetchRecent: searchService.fetchRecent
            )
        }
    }
    
    struct RootView: View {
        let dependencies = AppDependencies()
    
        var body: some View {
            SearchView(
                viewModel: .init(
                    dependencies: dependencies.search
                )
            )
        }
    }
    

As you can see, I also added the extension with calculated property to easily
extract dependencies only needed for the search feature module. You can have
this kind of property as many as you need to fulfill the requirements of all
the app’s feature modules.

Today we learned how to inject the low-level functionality inside feature
modules without exposing information about the concrete implementation. I hope
you enjoy the post. Feel free to follow me on [ Twitter
](https://twitter.com/mecid) and ask your questions related to this post.
Thanks for reading, and see you next week!

####  References

  1. [ Meet the microapps architecture ](https://increment.com/mobile/microapps-architecture/)
  2. [ Introduction to App Modularisation with Swift Package Manager ](https://holyswift.app/introduction-to-app-modularisation-with-swift-package-manager-a-tale-to-be-told)
  3. [ How to Control the World ](https://www.pointfree.co/blog/posts/21-how-to-control-the-world)

