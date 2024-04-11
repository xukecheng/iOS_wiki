##  Introducing Container views in SwiftUI

31 Jul 2019

During app development using SwiftUI, you can see that your views are very
coupled with the data flow. Views fetch and render the data, handle user input
and actions, etc. By doing so many things views become very fat and we can’t
reuse them across the app. Let’s take a look at a different way of decomposing
views by using _Container Views_ .

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

In my first post about SwiftUI, we build a Github app.

    
    
    import SwiftUI
    import Combine
    
    struct FavoritesView : View {
        @EnvironmentObject var store: ReposStore
    
        var body: some View {
            NavigationView {
                List {
                    ForEach(store.repos) { repo in
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
                .navigationBarTitle(Text("Favorites"))
                .onAppear(perform: fetch)
            }
        }
    
        private func fetch() {
            store.fetchFavorites()
        }
    }
    

Here we have a simple view which fetches and renders my starred repositories.
It looks very straightforward, but there is a massive problem. _FavoritesView_
mixes data fetching plus rendering, and because of that, we can’t reuse this
view. For example, I want to use it to render a user’s repositories or repos
search result. To make it possible, let’s start our refactoring process.

####  Composition

As you can see, SwiftUI uses mainly value types instead of classes and built
on top _Composition over Inheritance_ principle. Let’s follow this way by
decomposing our _FavoritesView_ into a few small composable views.

    
    
    import SwiftUI
    
    struct ReposView : View {
        let repos: [Repo]
    
        var body: some View {
            List {
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
    }
    

Now we have a simple _ReposView_ , which accepts an array of repos and render
them. That’s it. We can use it anywhere across the app where we need to
display a repos list.

####  Introducing Container views

But now we have another question, where we can do data-flow stuff like data
fetching and user actions handling. Let’s introduce _Container View_ concept.
_Container View_ fetches data and passes it to a _Rendering View_ or another
_Container View_ . _Container View_ doesn’t present any User Interface itself.
It is just managing data-flow and passes the data to the _Rendering View_ .

    
    
    import SwiftUI
    
    struct FavoritesContainerView: View {
        @EnvironmentObject var store: ReposStore
    
        var body: some View {
            ReposView(repos: store.repos)
                .onAppear(perform: fetch)
        }
    
        private func fetch() {
            store.fetchFavorites()
        }
    }
    

In the example above, we have a _FavoritesContainerView_ which handles the
data fetching and passes repos array to _ReposView_ . By doing this, we have a
clear separation between our data-flow and data rendering. Let’s take a look
at a more complicated example.

    
    
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
    
    struct SearchView : View {
        @Binding var query: String
        
        let repos: [Repo]
        let onCommit: () -> Void
    
        var body: some View {
            List {
                TextField("Type something", text: $query, onCommit: onCommit)
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
    }
    

Here we have a more complex example, where _Container View_ provides an acton
handling closure and state binding to _Rendering View_ . Let’s summarize our
thoughts about _Container and Rendering views in SwiftUI_ .

**_Container Views_ should do things only related to data-flow: **

  1. Store the state of the _Rendering View_
  2. Fetch data using _ObservableObject_
  3. Handle life cycle ( _onAppear/onDisappear_ ) 
  4. Provide action handlers to the _Rendering View_

**_Rendering Views_ should do things only related to rendering: **

  1. Build User Interface using primitive components provided by SwiftUI. 
  2. Compose User Interface by using other _Rendering Views_ . 
  3. Use data as input to render User Interface and don’t store any state. 

####  Conclusion

Today we discussed a way of decomposing your complex view into small and
reusable pieces. I try to follow this approach as much as possible to make a
clean separation between data-flow and displaying data. Try to use this method
and share with me your thoughts about it. Feel free to follow me on [ Twitter
](https://twitter.com/mecid) and ask your questions related to this post.
Thanks for reading and see you next week!

