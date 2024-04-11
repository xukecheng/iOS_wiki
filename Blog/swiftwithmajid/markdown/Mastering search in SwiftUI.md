##  Mastering search in SwiftUI

23 Jun 2021

SwiftUI Release 3.0 brought tons of expected features that we missed in
previous iterations. One of them is the ability to provide the search feature
in our apps. Fortunately, we have a new _searchable_ view modifier. This week,
we will learn about the new _searchable_ modifier and how to build a great
search experience using it.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

####  Basics

We can mark the content of our view as searchable using the new view modifier.
SwiftUI understands the structure of your app and displays the search bar in
the appropriate place. Let’s take a look at the quick example.

    
    
    struct RootView: View {
        @State private var query: String = ""
    
        var body: some View {
            NavigationView {
                Master()
                Details()
            }
            .searchable(text: $query, prompt: Text("Search"))
        }
    }
    

![search](/public/search.png)

We attach the _searchable_ view modifier to the _NavigationView_ at the root
of our app. SwiftUI can put the search bar in different places depending on
the environment. For example, it will put a search bar in the _Master_ view on
iOS and iPadOS. On macOS, SwiftUI places the search bar in the toolbar of the
trailing column of the _NavigationView_ .

    
    
    struct RootView: View {
        @State private var query: String = ""
    
        var body: some View {
            NavigationView {
                Master()
                Details()
            }
            .searchable(
                text: $query,
                placement: .toolbar,
                prompt: "Type something..."
            )
        }
    }
    

You can also suggest placement for the search bar using the _placement_
parameter, but keep in mind that SwiftUI can ignore it. A few possible
placements for the search bar are _automatic_ , which is the default one,
_sidebar, toolbar, and navigationBarDrawer._

    
    
    struct ContentView: View {
        @StateObject private var viewModel = SearchViewModel()
        @State private var query = ""
    
        var body: some View {
            NavigationView {
                List(viewModel.repos) { repo in
                    VStack(alignment: .leading) {
                        Text(repo.name)
                            .font(.headline)
                        Text(repo.description ?? "")
                            .foregroundColor(.secondary)
                    }
                }
                .navigationTitle("Search")
                .searchable(text: $query)
                .onChange(of: query) { newQuery in
                    Task { await viewModel.search(matching: query) }
                }
            }
        }
    }
    

Whenever we use the _searchable_ modifier, we should provide a binding to a
string value. We can observe changes and filter our content depending on the
query term using that binding.

    
    
    struct ContentView: View {
        @StateObject private var viewModel = SearchViewModel()
        @State private var searchShown = false
        @State private var query = ""
    
        var body: some View {
            NavigationView {
                List(viewModel.repos) { repo in
                    VStack(alignment: .leading) {
                        Text(repo.name)
                            .font(.headline)
                        Text(repo.description ?? "")
                            .foregroundColor(.secondary)
                    }
                }
                .navigationTitle("Search")
                .searchable(text: $query, isPresented: $searchShown)
                .onChange(of: query) { newQuery in
                    Task { await viewModel.search(matching: query) }
                }
                .onAppear {
                    searchShown = true
                }
            }
        }
    }
    

We can also control the search visibility programmatically by using the
_isPresented_ parameter of the _searchable_ view modifier accepting a boolean
binding defining the current visibility of the search.

####  Environment

SwiftUI provides us _isSearching_ environment value that indicated whether the
user is currently interacting with the search bar that has been placed by a
surrounding _searchable_ modifier. We can use this value to understand whether
to show quick search results.

    
    
    struct StarredReposList: View {
        @StateObject var viewModel = SearchViewModel()
        @Environment(\.dismissSearch) var dismissSearch
        @Environment(\.isSearching) var isSearching
    
        let query: String
    
        var body: some View {
            List(viewModel.repos) { repo in
                RepoView(repo: repo)
            }
            .overlay {
                if isSearching && !query.isEmpty {
                    VStack {
                        Button("Dismiss search") {
                            dismissSearch()
                        }
                        SearchResultView(query: query)
                            .environmentObject(viewModel)
                    }
                }
            }
        }
    }
    

Another search-related environment value we have is _dismissSearch_ .
_dismissSearch_ asks the system to dismiss the current search interaction.
Remember that both environment values work only in the views surrounded by the
_searchable_ modifier.

> To learn more about environment in SwiftUI, take a look at my [ “The power
> of Environment in SwiftUI” ](/2019/08/21/the-power-of-environment-in-
> swiftui/) post.

####  Suggestions

Suggestions are a vital part of the excellent search experience, and SwiftUI
gives us a very nice API that we can use to provide search suggestions to our
users. The _searchSuggestions_ view modifier allows us to pass a
_@ViewBuilder_ closure displaying search suggestions. Let’s see how we can use
it.

    
    
    struct ContentView: View {
        @StateObject private var viewModel = SearchViewModel()
        @State private var query = ""
    
        let suggestions: [String] = [
            "Swift", "SwiftUI", "Obj-C"
        ]
    
        var body: some View {
            NavigationView {
                List(viewModel.repos) { repo in
                    VStack(alignment: .leading) {
                        Text(repo.name)
                            .font(.headline)
                        Text(repo.description ?? "")
                            .foregroundColor(.secondary)
                    }
                }
                .navigationTitle("Search")
                .searchable(text: $query)
                .searchSuggestions {
                    ForEach(suggestions, id: \.self) { suggestion in
                        Text(suggestion)
                            .searchCompletion(suggestion)
                    }
                }
                .onChange(of: query) { newQuery in
                    Task { await viewModel.search(matching: query) }
                }
            }
        }
    }
    

![search-suggestions](/public/search1.png)

As you can see in the example above, we use the _searchSuggestions_ view
modifier and provide a _@ViewBuilder_ closure with _ForEach_ view that
iterates over an array of suggestions. We also use the _searchCompletion_ view
modifier to wrap every text view in a button that assigns its value to the
search query binding.

Keep in mind that _searchCompletion_ modifier wraps its content in a _Button_
. It means you should apply it to the view that doesn’t have user interaction
like _Text_ or _Label_ .

####  Scopes

The SwiftUI framework provides us another view modifier allowing us to improve
search experience. We can use the _searchScopes_ view modifier to provide
search scopes displayed in the segmented control under the search bar.

    
    
    struct ContentView: View {
        @State private var query = ""
        @State private var scope: Scope = .local
        
        var body: some View {
            NavigationStack {
                List {
                    // ...
                }
                .searchable(text: $query)
                .searchScopes($scope) {
                    ForEach(Scope.allCases, id: \.self) { scope in
                        Text(scope.rawValue)
                    }
                }
            }
        }
    }
    

####  Tokens

Another version of the _searchable_ view modifier allows us to display tokens
in the search bar.

    
    
    struct Token: Identifiable {
        let id = UUID()
        let value: String
    }
        
    struct ContentView: View {
        @State private var query = ""
        @State private var tokens: [Token] = []
        @State private var suggestedTokens: [Token] = [
            .init(value: "Token1"),
            .init(value: "Token2"),
            .init(value: "Token3"),
            .init(value: "Token4")
        ]
        
        var body: some View {
            NavigationStack {
                List {
                    // ...
                }
                .searchable(
                    text: $query,
                    tokens: $tokens,
                    suggestedTokens: $suggestedTokens
                ) { token in
                    Text(verbatim: token.value)
                }
                .navigationTitle("Search")
            }
        }
    }
    

In the example above, we use the _searchable_ view modifier and pass two
bindings for suggested tokens and selected tokens. The SwiftUI displays
suggested tokens and move them into the search bar as soon as user taps one of
them. It also moves the token from the suggested collection to the selected
collection of tokens.

    
    
    struct ContentView: View {
        @State private var query = ""
        @State private var tokens: [Token] = []
        
        var body: some View {
            NavigationStack {
                List {
                    // ...
                }
                .searchable(
                    text: $query,
                    tokens: $tokens
                ) { token in
                    Text(verbatim: token.value)
                }
                .navigationTitle("Search")
                .onChange(of: query) { newValue in
                    if newValue.contains("new") {
                        tokens.append(.init(value: "NEW"))
                    }
                }
            }
        }
    }
    

Another variation of the _searchable_ view modifier allows us to manually
filter the query and populate tokens.

####  Conclusion

Today we learned how to build a great search experience using the brand new
_searchable_ view modifier. It is incredible how easy you can make things like
suggestions, the platform adopted placement using the only _searchable_ view
modifier. I hope you enjoy the post. Feel free to follow me on [ Twitter
](https://twitter.com/mecid) and ask your questions related to this post.
Thanks for reading, and see you next week!

