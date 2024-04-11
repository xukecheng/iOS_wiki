##  Redux-like state container in SwiftUI. Container Views.

02 Oct 2019

This week I want to continue the topic of using a _Redux-like state container
in SwiftUI_ . I’m delighted with the new approach and already finished the
refactoring of the [ NapBot app ](https://napbot.swiftwithmajid.com) in this
way. That’s why today I want to share with you how I use _Container Views_
with a state container similar to _Redux_ .

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

In previous weeks we already discussed the basics and some good practices
while using _Redux-like state containers_ . If you are not familiar with
_Redux_ , please take a look at those posts to understand how to build it in
SwiftUI and which benefits you get by using it.

  1. [ Redux-like state container in SwiftUI. Basics ](/2019/09/18/redux-like-state-container-in-swiftui/)
  2. [ Redux-like state container in SwiftUI. Best practices ](/2019/09/25/redux-like-state-container-in-swiftui-part2/)

The container which holds the whole app’s state as a single source of truth
simplifies my codebase and eliminates a bunch of bugs that I had during manual
sync between multiple states across the app screens.

> To learn more about modeling app state using multiple store objects, take a
> look at my dedicated [ “Modeling app state using Store objects in SwiftUI”
> ](/2019/09/04/modeling-app-state-using-store-objects-in-swiftui/) post.

####  Container Views

Today, I want to touch another subject from my previous posts which plays very
nice in conjunction with a _Redux-like state container_ , and this is
_Container Views_ . _Container Views_ help us to keep our SwiftUI views simple
and responsible for only one job.

The main idea is dividing your views into two types: _Container Views and
Rendering Views_ . The _Rendering View_ is responsible for drawing the
content, and that’s all. So basically it should not store the state or handle
any lifecycle event. It usually renders the data which you pass via the init
method.

_Container View_ , on another hand, is responsible for handling data-flow and
lifecycle events by providing the functions/closures to a _Rendering View_ .
Let’s take a look at a simple example.

    
    
    import SwiftUI
    
    struct SearchContainerView: View {
        @EnvironmentObject var store: ReposStore
        @State private var query: String = "Swift"
    
        var body: some View {
            SearchView(query: $query, repos: store.repos, onCommit: fetch)
                .onAppear(perform: fetch)
        }
    
        private func fetch() {
            store.fetch(matching: query)
        }
    }
    
    struct SearchView: View {
        @Binding var query: String
    
        let repos: [Repo]
        let onCommit: () -> Void
    
        var body: some View {
            List {
                TextField("Type something", text: $query, onCommit: onCommit)
                ReposView(repos: repos)
            }
        }
    }
    
    struct ReposView: View {
        let repos: [Repo]
    
        var body: some View {
            ForEach(repos) { repo in
                HStack(alignment: .top) {
                    VStack(alignment: .leading) {
                        Text(repo.name)
                            .font(.headline)
                        Text(repo.description ?? "")
                            .font(.subheadline)
                    }
                }
            }
        }
    }
    

In the example above, you can see how we build a connection between _Container
and Rendering views_ . _Container View_ provides the data to _Rendering Views_
. By doing this, we can easily reuse our _ReposView_ anywhere across the app.
_ReposView_ doesn’t have any dependency on some state or datastore and gets
all the needed data via the init method.

> To learn more about _Container Views_ , take a look at [ “Introducing
> Container views in SwiftUI” post ](/2019/07/31/introducing-container-views-
> in-swiftui/) .

####  Using Container Views with Redux-like state container

During my transition from multiple stores to a single source of truth, I
realize that _Container Views_ play a significant role in this approach. I
mainly use them for sending actions to the store and mapping the global app
state to _Rendering View_ properties. _Container Views_ perfectly fit into my
current app architecture. Let’s take a look at the example.

    
    
    import SwiftUI
    
    struct SearchContainerView: View {
        @EnvironmentObject var store: AppStore
        @State private var query: String = "Swift"
    
        var body: some View {
            SearchView(
                query: $query,
                repos: store.state.search.result,
                onCommit: fetch
            ).onAppear(perform: fetch)
        }
    
        private func fetch() {
            store.send(SideEffect.search(query))
        }
    }
    
    struct SearchView: View {
        @Binding var query: String
    
        let repos: [Repo]
        let onCommit: () -> Void
    
        var body: some View {
            List {
                TextField("Type something", text: $query, onCommit: onCommit)
                ReposView(repos: repos)
            }
        }
    }
    

As you can see in the example above, _Container View_ helps us to keep
_Rendering Views_ small and independent.

####  Conclusion

Today we talked about the benefits of using _Container Views with Redux-like
state containers_ . I love this approach and use it as my main way to go with
SwiftUI. I hope you enjoy the post. Feel free to follow me on [ Twitter
](https://twitter.com/mecid) and ask your questions related to this post.
Thanks for reading and see you next week!

  1. [ Redux-like state container in SwiftUI. Basics ](/2019/09/18/redux-like-state-container-in-swiftui/)
  2. [ Redux-like state container in SwiftUI. Best practices ](/2019/09/25/redux-like-state-container-in-swiftui-part2/)
  3. Redux-like state container in SwiftUI. Container Views. 
  4. [ Redux-like state container in SwiftUI. Connectors. ](/2021/02/03/redux-like-state-container-in-swiftui-part4/)
  5. [ Redux-like state container in SwiftUI. Swift concurrency model. ](/2022/02/17/redux-like-state-container-in-swiftui-part5/)

####  References

The series of posts have built on a foundation of ideas started by other
libraries, particularly Redux, Elm, and TCA.

  1. [ WWDC20 - Data Essentials in SwiftUI ](https://developer.apple.com/videos/play/wwdc2020/10040/)
  2. [ Redux ](https://redux.js.org) \- The JavaScript library that popularized unidirectional data flow. 
  3. [ The Elm Architecture ](https://guide.elm-lang.org/architecture/) \- A purely functional language and runtime that inspired the creation of Redux. 
  4. [ The Composable Architecture ](https://github.com/pointfreeco/swift-composable-architecture) \- A library that bridges concepts from the Elm Architecture and Redux to Swift. It introduced the “environment” and “effect” patterns that this series covers. 

