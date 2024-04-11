##  What's new in SwiftUI

23 Jun 2020

I have been waiting for this day for the last nine months, and it has finally
arrived. We saw the next iteration of the SwiftUI framework. Apple did a great
job during the last year by improving SwiftUI and moving it towards by making
it a standalone way for building apps for the Apple ecosystem. Today we will
take a peek at all-new SwiftUI features.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

####  App structure

Apple provides a brand new way of defining the app’s entry point by using the
_App_ protocol. _App_ protocol allows us to easily replace the _AppDelegate_
and _SceneDelegate_ with a single struct that will manage our scenes and app
lifecycle. Let’s take a look at a very quick example.

    
    
    @main
    struct CardioBotApp: App {
        @SceneBuilder var body: some Scene {
            WindowGroup {
                ContentView()
            }
        }
    }
    

In the example above, we have a struct that conforms to the _App_ protocol.
The only requirement is the _body_ property that should return any _Scene_ .
The _Scene_ is another new protocol introduced by SwiftUI that allows us to
declare an app scene. SwiftUI comes with a few ready to use implementations,
and one of them is _WindowGroup_ . _WindowGroup_ is a scene type that we will
mostly use for the main interface of our app that isn’t document-based.

    
    
    @main
    struct MyApp: App {
        @SceneBuilder var body: some Scene {
            DocumentGroup(newDocument: TextFile()) { textFile in
                TextEditor(textFile.$document.text)
            }
    
            #if os(macOS)
            Settings {
                SettingsView()
            }
            #endif
        }
    }
    

For document-based apps, SwiftUI provides a _DocumentGroup_ scene that
automatically handles the navigation through files.

####  Lazy stacks

One thing that I don’t like about SwiftUI stacks is the eager initialization.
Whenever you have ten or thousand views in a stack, SwiftUI tries to create
them immediately. Fortunately, it is changed today. The new version of the
SwiftUI framework provides us _LazyHStack_ and _LazyVStack_ which create its
children only when needed.

    
    
    import SwiftUI
    
    struct ContentView: View {
        var body: some View {
            ScrollView {
                LazyVStack {
                    ForEach(0...1000, id: \.self) { index in
                        Text(String(index))
                            .onAppear { print(index) }
                    }
                }
            }
        }
    }
    

####  Grids

It was so tough to create a photo gallery or calendar layout in SwiftUI
without _UICollectionView_ . Nowadays, most of the apps have a screen with a
grid layout. It was nearly impossible to create a grid layout efficiently
using SwiftUI. Fortunately, now we can do it using the new _LazyVGrid_ and
_LazyHGrid_ views. Let’s take a look at a quick example.

    
    
    import SwiftUI
    
    struct ContentView: View {
        var body: some View {
            ScrollView {
                LazyVGrid(
                    columns: Array(
                        repeating: GridItem(.flexible()),
                        count: 3
                    )
                ) {
                    ForEach(0...1000, id: \.self) { _ in
                        Color.red
                    }
                }
            }
        }
    }
    

####  ScrollView

If you read my post about [ SwiftUI wishes ](/2020/06/10/swiftui-wishlist-for-
wwdc20/) , you might know that I have been waiting for an ability to scroll to
a particular offset using a _ScrollView_ . That part of functionally stopped
me from using SwiftUI’s _ScrollView_ . It is also changed today when Apple
released the _ScrollViewReader_ . _ScrollViewReader_ works very similarly to
_GeometryReader_ and provides a way to scroll to a specific view using its
_ID_ .

    
    
    import SwiftUI
    
    struct ContentView: View {
        var body: some View {
            ScrollView {
                ScrollViewReader { scrollView in
                    LazyVStack {
                        ForEach(0...1000, id: \.self) { index in
                            Text(String(index))
                                .id(index)
                        }
                        Button("Scroll to the middle") {
                            scrollView.scrollTo(500)
                        }
                    }
                }
            }
        }
    }
    

####  TextEditor

One of the most missing components in SwiftUI was _TextView_ . There was no
way to edit or type multiline text. We end up with wrapping _TextView_ with
_UIViewRepresentable_ , but it doesn’t work well in different circumstances.
Finally, this year SwiftUI provides us a _TextEditor_ view that allows us to
edit multiline text. Let’s take a look at how we can use it.

    
    
    import SwiftUI
    
    struct ContentView: View {
        @State private var text = "Hello World!"
    
        var body: some View {
            TextEditor(text: $text)
        }
    }
    

The usage is pretty similar to _TextField_ , but in this case, we allowed to
type very long text examples. There is still no way to use attributed text,
but I hope it will arrive during the next betas.

####  New data flow property wrappers

Besides all the new views that Apple released today, we also have brand new
ways to handle data flow in SwiftUI. SwiftUI now includes the _AppStorage_
property wrapper that accesses _UserDefauls_ and invalidates view as soon as
corresponding key changes. Let’s take a look at the example.

    
    
    import SwiftUI
    
    struct ContentView: View {
        @AppStorage("isNotificationsEnabled") var enabled = false
    
        var body: some View {
            Toggle("Notifications", isOn: $enabled)
        }
    }
    

There is also _SceneStorage_ property wrapper that we can use for the
automatic state restoration of the value. It works similarly to _AppStorage_ ,
but instead of _UserDefaults_ , it uses per-scene storage managed by the
system.

Another new property wrapper is _StateObject_ . _StateObject_ works similarly
to _State_ property wrapper. It allocates memory inside the SwiftUI framework
and stores your _ObservableObject_ there. It allows to _ObservableObject_ to
survive during view updates.

    
    
    @main
    struct CardioBotApp: App {
        @StateObject var store = Store()
    
        var body: some Scene {
            WindowGroup {
                ContentView()
                    .environmentObject(store)
            }
        }
    }
    

####  New styling opportunities

One of the best things about SwiftUI is the way that the framework uses to
apply styling. Most of the views in SwiftUI provides protocols that we can
conform to share the styling across the app. This year the list of styling
protocols increased. SwiftUI allows us to transform _TabView_ into a paging
view by applying _PageTabViewStyle_ . There is also a new collection of list
styles like _SidebarListStyle_ , _InsetGroupedListStyle_ , and
_InsetListStyle_ .

####  New views

This year SwiftUI integrates more deeply with all the frameworks across the
Apple ecosystem. For example, MapKit provides _Map_ and _MapAnnotations_
SwiftUI views. ClockKit provides us a _Gauge_ view that we can use to show
value within a range. AVKit provides the _VideoPlayer_ view that we can use to
integrate with _AVPlayer_ .

There is also a bunch of new views that SwiftUI provides us today. We finally
have a system-wide color picker, native _SignInWithAppleButton_ ,
_ProgressView_ that supports both linear and circular progress indicators,
_OutlineGroup_ that allows us to display tree-structured collections of data,
and much more.

####  Conclusion

I’m delighted to see that the next iteration of SwiftUI is so strong. Of
course, I will share with you detailed posts about all new features of SwiftUI
as soon as I play with them enough to share something. Feel free to follow me
on [ Twitter ](https://twitter.com/mecid) and ask your questions related to
this post. Thanks for reading, and have a nice week!

