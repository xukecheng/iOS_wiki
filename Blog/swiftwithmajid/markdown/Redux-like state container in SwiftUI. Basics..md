##  Redux-like state container in SwiftUI. Basics.

18 Sep 2019

This week we will talk about building a state container similar to _Redux_ and
_The Elm Architecture_ that provides a single source of truth for your app. A
single state for the whole app makes it easier to debug and inspect. Single
source of truth eliminates tons of bugs produced by creating multiple states
across the app.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

####  Single source of truth

The main idea here is describing the whole app state by using a single struct
or composition of structs. Assume that we are working on a Github repos search
app where the state is the repos array that we fetch matching some query using
Github API.

    
    
    struct AppState {
        var searchResult: [Repo] = []
    }
    

Next step is passing the read-only app state to every view inside the app. The
best way for doing that is _SwiftUI’s Environment_ feature. We can put an
object holding the whole app state in the _Environment_ of the root view. Root
view will share its _Environment_ with all child views.

> SwiftUI uses environment to pass system-wide and application-related
> information. You can also populate environment with your custom objects. To
> learn more about environment, take a look at my [ “The power of Environment
> in SwiftUI” ](/2019/08/21/the-power-of-environment-in-swiftui/) post.
    
    
    final class Store: ObservableObject {
        @Published private(set) var state: AppState
    }
    

In the example above, we create a store object that stores the app state and
provides read-only access to it. State property uses _@Published_ property
wrapper that notifies SwiftUI during any changes. It allows us to keep up to
date the whole app by deriving it from a single source of truth.

> To learn more you can check [ “Modeling app state using Store objects in
> SwiftUI” ](/2019/09/04/modeling-app-state-using-store-objects-in-swiftui/)
> post.

####  Reducer and Actions

It’s time to talk about user actions which lead to state mutations. _Action_
is a simple enum or composition of enums describing a change of the state. For
example, set loading value during data fetch, assign fetched repositories to
the state property. Let’s take a look at the example code for _Action_ enum.

    
    
    enum AppAction {
        case search(query: String)
        case setSearchResult(repos: [Repo])
    }
    

_Reducer_ is a function that takes current state, applies _Action_ to the
state, and generates a new state. Generally, _reducer_ or _composition of
reducers_ is the single place where your app should mutate the state. The fact
that the only one function can modify the whole app state is super simple,
debuggable, and testable. Here is an example of reduce function.

    
    
    typealias Reducer<State, Action> = (inout State, Action) -> Void
    
    func appReducer(state: inout AppState, action: AppAction) {
        switch action {
        case let .setSearchResults(repos):
            state.searchResult = repos
        case let .search(query):
            break
        }
    }
    

####  Unidirectional flow

Let’s talk about data flow now. Every view has a read-only access to the state
via store object. Views can send _actions_ to the store object. _Reducer_
modifies the state, and then SwiftUI notifies all the views about state
changes. SwiftUI has a super-efficient diffing algorithm that’s why diffing of
the whole app state and updating changed views works so fast. Let’s modify our
store object to support sending _actions_ .

    
    
    final class Store<State, Action>: ObservableObject {
        @Published private(set) var state: State
    
        private let reducer: Reducer<State, Action>
    
        init(initialState: State, reducer: @escaping Reducer<State, Action>) {
            self.state = initialState
            self.reducer = reducer
        }
    
        func send(_ action: Action) {
            reducer(&state, action)
        }
    }
    

_State - > View -> Action -> State -> View _

This architecture revolves around a strict **unidirectional** data flow. It
means that all the data in the application follows the same pattern, making
the logic of your app more predictable and easier to understand.

####  Side effects

We already implemented a _unidirectional_ flow that accepts user actions and
modifies the state, but what about _async actions_ which we usually call _side
effects_ . How to bake a support for async tasks into our store type? I think
it is a good time to introduce the usage of _Combine framework_ that perfectly
fits async task processing.

    
    
    typealias Reducer<State, Action, Environment> =
        (inout State, Action, Environment) -> AnyPublisher<Action, Never>?
    

We add support for _async tasks_ by changing _Reducer_ typealias, it has the
additional parameter called _Environment_ . _Environment_ might be a plain
struct that holds all needed dependencies like service and manager classes.

    
    
    func appReducer(
        state: inout AppState,
        action: AppAction,
        environment: Environment
    ) -> AnyPublisher<AppAction, Never>? {
        switch action {
        case let .setSearchResults(repos):
            state.searchResult = repos
        case let .search(query):
            return environment.service
                .searchPublisher(matching: query)
                .replaceError(with: [])
                .map { AppAction.setSearchResults(repos: $0) }
                .eraseToAnyPublisher()
        }
        return nil
    }
    

Side Effect is a sequence of _Actions_ which we can publish using _Combine_
framework’s _Publisher_ type. It allows us to handle async job and then
publish an _action_ that will be used by _reducer_ to change the current
state.

    
    
    final class Store<State, Action, Environment>: ObservableObject {
        @Published private(set) var state: State
    
        private let environment: Environment
        private let reducer: Reducer<State, Action, Environment>
        private var cancellables: Set<AnyCancellable> = []
    
        init(
            initialState: State,
            reducer: @escaping Reducer<State, Action, Environment>,
            environment: Environment
        ) {
            self.state = initialState
            self.reducer = reducer
            self.environment = environment
        }
    
        func send(_ action: Action) {
            guard let effect = reducer(&state, action, environment) else {
                return
            }
    
            effect
                .receive(on: DispatchQueue.main)
                .sink(receiveValue: send)
                .store(in: &cancellables)
        }
    }
    

As you can see in the example above, we build a _Store_ type that supports
async tasks. Usually, reducer resolves an action by applying it on top of the
state. In case of an async action, reducer returns it as _Combine Publisher_ ,
then _Store_ run it and send result back to the reducer as a plain action.

####  Real usage example

Finally, we can finish our repos search app that calls Github API
asynchronously and fetches repositories matching a query. The full source code
available on [ Github ](https://github.com/mecid/redux-like-state-container-
in-swiftui) .

    
    
    typealias AppStore = Store<AppState, AppAction, AppEnvironment>
    
    struct SearchContainerView: View {
        @EnvironmentObject var store: AppStore
        @State private var query: String = "Swift"
    
        var body: some View {
            SearchView(
                query: $query,
                repos: store.state.searchResult,
                onCommit: fetch
            ).onAppear(perform: fetch)
        }
    
        private func fetch() {
            store.send(.search(query: query))
        }
    }
    
    struct SearchView : View {
        @Binding var query: String
        let repos: [Repo]
        let onCommit: () -> Void
    
        var body: some View {
            NavigationView {
                List {
                    TextField("Type something", text: $query, onCommit: onCommit)
    
                    if repos.isEmpty {
                        Text("Loading...")
                    } else {
                        ForEach(repos) { repo in
                            RepoRow(repo: repo)
                        }
                    }
                }.navigationBarTitle(Text("Search"))
            }
        }
    }
    

We divide our screen into two views: _Container View_ and _Rendering View_ .
_Container View_ handles the actions and retrieves the needed piece of state
from the global state. _Rendering View_ accepts the data and renders it.

> We already talked about _Container Views_ in my previous posts, to learn
> more take a look at [ “Introducing Container views in SwiftUI”
> ](/2019/07/31/introducing-container-views-in-swiftui/) post.

####  Conclusion

Today we learned how to build _Redux-like_ state container with _side-effects_
in mind. To achieve that we used _Combine_ framework. I hope you enjoy the
post. Feel free to follow me on [ Twitter ](https://twitter.com/mecid) and ask
your questions related to this post. Thanks for reading and see you next week!

  1. Redux-like state container in SwiftUI. Basics 
  2. [ Redux-like state container in SwiftUI. Best practices ](/2019/09/25/redux-like-state-container-in-swiftui-part2/)
  3. [ Redux-like state container in SwiftUI. Container Views. ](/2019/10/02/redux-like-state-container-in-swiftui-part3/)
  4. [ Redux-like state container in SwiftUI. Connectors. ](/2021/02/03/redux-like-state-container-in-swiftui-part4/)
  5. [ Redux-like state container in SwiftUI. Swift concurrency model. ](/2022/02/17/redux-like-state-container-in-swiftui-part5/)

####  References

The series of posts have built on a foundation of ideas started by other
libraries, particularly Redux, Elm, and TCA.

  1. [ WWDC20 - Data Essentials in SwiftUI ](https://developer.apple.com/videos/play/wwdc2020/10040/)
  2. [ Redux ](https://redux.js.org) \- The JavaScript library that popularized unidirectional data flow. 
  3. [ The Elm Architecture ](https://guide.elm-lang.org/architecture/) \- A purely functional language and runtime that inspired the creation of Redux. 
  4. [ The Composable Architecture ](https://github.com/pointfreeco/swift-composable-architecture) \- A library that bridges concepts from the Elm Architecture and Redux to Swift. It introduced the “environment” and “effect” patterns that this series covers. 

