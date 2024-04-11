##  Managing app in SwiftUI

19 Aug 2020

One of the most important things that Apple did release this year was the
native app and scene management for SwiftUI apps. This week we will understand
how to manage our apps using _App_ protocol without old _AppDelegate_ . We
will learn how to achieve the same set of features with _App_ protocol.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

####  Entry point

[ SE-0281 ](https://github.com/apple/swift-
evolution/blob/master/proposals/0281-main-attribute.md) introduced type-based
program entry points for Swift language. This proposal provides us _@main_
attribute that allows us to mark the app’s entry point. Swift compiler will
recognize this entry point and launch it by running the static main function.
Let’s take a look at the smallest “Hello World” app example.

    
    
    @main
    struct MyApp: App {
        var body: some Scene {
            WindowGroup {
                Text("Hello World!")
            }
        }
    }
    

As you can see in the example above, we create an app by conforming to _App_
protocol and implementing the single requirement, _body_ property. _Body_
property should return an instance of scene protocol, and we use the
_WindowGroup_ scene here. _WindowGroup_ is a standard scene type provided by
SwiftUI that handles multiple windows on macOS or various scenes on iPadOS. We
will deep dive into scene management in [ another post
](https://swiftwithmajid.com/2020/08/26/managing-scenes-in-swiftui/) .

You may notice that there is no static main function in the code example that
Swift compiler uses as the entry point. _App_ protocol has the extension that
defines the static main function; that’s why we don’t need to care about it.

####  didBecomeActive and didEnterBackground

We have learned the basics of _App_ protocol, and it is time to move forward
to understand how we can replace _AppDelegate_ callbacks like
_didBecomeActive_ or _didEnterBackground_ .

    
    
    import SwiftUI
    
    @main
    struct CardioBotApp: App {
        @Environment(\.scenePhase) var scenePhase
    
        @StateObject var store = Store(
            initialState: AppState(),
            reducer: appReducer,
            environment: AppEnvironment()
        )
    
        var body: some Scene {
            WindowGroup {
                RootView()
                    .environmentObject(store)
                    .onChange(of: scenePhase) { phase in
                        if phase == .active {
                            store.send(.fetch)
                        }
                    }
            }
        }
    }
    

SwiftUI uses the environment to store the phase of the current scene. You can
access it by using the scene phase environment value. The excellent addition
to the new app and scene management API is the _onChange_ modifier. It runs
the provided closure on every change of the value that you pass. In the
example above, we fetch data whenever the scene becomes active.

####  Deep linking

Another thing that we used to do in _AppDelegate_ is deep linking. SwiftUI
provides us a special _onOpenURL_ modifier that allows us to handle links.

    
    
    @main
    struct MyApp: App {
        var body: some Scene {
            WindowGroup {
                Text("Hello World!")
                    .onOpenURL { url in
                        if url.absoluteString.contains("today") {
                            // toggle state to navigate to today screen
                        }
                    }
            }
        }
    }
    

As you can see in the example above, we register a closure that handles URLs.
SwiftUI will run it whenever the app should open the URL. We can extract the
data from a URL and assign it to the state property that enables the
navigation link or switch tabs.

####  Handoff and user activity

Similarly to deep linking, SwiftUI provides us a modifier to handle Handoff
and user activity. We can use _onContinueUserActivity_ modifier in the very
same way as we use _onOpenURL_ modifier. Let’s take a look at another example.

    
    
    import SwiftUI
    
    @main
    struct MyApp: App {
        var body: some Scene {
            WindowGroup {
                Text("Hello World!")
                    .onContinueUserActivity("com.myapp.today") { userActivity in
                        // toggle state to navigate to today screen
                    }
            }
        }
    }
    

We use _onContinueUserActivity_ modifier to set a closure that will parse a
user activity. In the same way, as we did before, we can parse a user activity
and toggle state property that routes the navigation. SwiftUI will run this
closure as soon as the user continues activity.

####  UIApplicationDelegateAdaptor

As you can see, we can implement many _AppDelegate_ callbacks with _App_
protocol and the new set of modifiers that SwiftUI provides us. But there are
still some gaps.

For example, there is no way to register for remote notifications with _App_
protocol. That’s why SwiftUI gives us another type called
_UIApplicationDelegateAdaptor_ . We can merge the functionality of old
_AppDelegate_ with the new App protocol using _UIApplicationDelegateAdaptor_
property wrapper.

    
    
    final class AppDelegate: NSObject, UIApplicationDelegate {
        func applicationDidBecomeActive(_ application: UIApplication) {
            application.registerForRemoteNotifications()
        }
    }
    
    @main
    struct MyApp: App {
        @UIApplicationDelegateAdaptor(AppDelegate.self) var delegate
    
        var body: some Scene {
            WindowGroup {
                Text("Hello World!")
            }
        }
    }
    

####  Conclusion

_App_ protocol is another step towards the declarative approach that Apple
gives us to build our apps. It allows us to replace old _AppDelegate_ with a
simple struct that conforms to _App_ protocol. I hope you enjoy the post. Feel
free to follow me on [ Twitter ](https://twitter.com/mecid) and ask your
questions related to this article. Thanks for reading, and see you next week!

