##  Window management in SwiftUI

02 Nov 2022

One of the significant additions to the current iteration of the SwiftUI
framework was window management APIs. We can open a separate window using the
new environment APIs and create a menu bar app using the new scene APIs. This
week we will learn how to use new window management APIs in SwiftUI.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

####  Multiple windows support

You can always check whenever the platform you are running supports multiple
window environments using the _supportsMultipleWindows_ environment value.

    
    
    struct ContentView: View {
        @Environment(\.supportsMultipleWindows)
        private var supportsMultipleWindows
        
        var body: some View {
            if supportsMultipleWindows {
                Text("Supports multiple windows")
            } else {
                Text("Doesn't support multiple windows")
            }
        }
    }
    

####  Single window

SwiftUI provides a new scene type to define a single window on macOS.

    
    
    @main struct MyApp: App {
        var body: some Scene {
            #if os(macOS)
            Window("Statistics", id: "stats") {
                StatisticsView()
            }
            #endif
            
            WindowGroup {
                ContentView()
            }
        }
    }
    
    

As you can see in the example above, we use the new Window scene type to
define a single window assigned to a particular identifier. Now we can use the
_openWindow_ environment value to open a window with the dedicated identifier.

    
    
    struct ContentView: View {
        @Environment(\.openWindow) private var openWindow
        
        var body: some View {        
            Button("Open statistics") {
                openWindow(id: "stats")
            }
        }
    }
    

> To learn more about scenes in SwiftUI, take a look at my dedicated [
> “Managing scenes in SwiftUI” ](/2020/08/26/managing-scenes-in-swiftui/)
> post.

####  Window group

Another addition to the scene API is the new overload of the _WindowGroup_
scene type allowing us to register a window group displaying items by
identifier.

    
    
    @main struct MyApp: App {
        var body: some Scene {
            #if os(macOS)
            WindowGroup(for: Item.ID.self) { $itemId in
                ItemView(itemId: itemId ?? UUID())
            }
            #endif
            
            WindowGroup {
                ContentView()
            }
        }
    }
    

In the example above, we register a window group for a particular identifier
type. Now we can use the same environment value to open a window by providing
an item identifier.

    
    
    struct ContentView: View {
        @Environment(\.openWindow) private var openWindow
        
        let items: [Item]
        
        var body: some View {
            List(items) { item in
                Button("open \(item.title)") {
                    openWindow(id: "item", value: item.id)
                }
            }
        }
    }
    

####  Window styling

The SwiftUI framework provides a few ways of styling windows using view
modifiers. First, we can display or hide the title of the window by applying
the _windowStyle_ view modifier. It accepts _hiddenTitleBar_ or _titleBar_
values. This view modifier should be used on the window itself.

Another option is to use the _presentedWindowStyle_ view modifier on the view
hierarchy, which will set the particular style for windows created by this
view hierarchy.

####  Menubar window

Menu bar apps are very popular on macOS, and now we have a native way to build
them in SwiftUI. There is a new scene type called _MenuBarExtra_ . It appears
in the system menu bar and presents its content in a pull-down menu.

    
    
    @main struct MyApp: App {
        var body: some Scene {
            #if os(macOS)
            MenuBarExtra {
                MenuBarView()
            } label: {
                Label("MyApp", systemImage: "star")
            }
            #endif
            
            WindowGroup {
                ContentView()
            }
        }
    }
    

You can control the visibility of the menu bar icon via another overload
accepting a boolean binding.

    
    
    @main struct MyApp: App {
        @State private var menuBarExtraShown = true
        
        var body: some Scene {
            #if os(macOS)
            MenuBarExtra(isInserted: $menuBarExtraShown) {
                MenuBarView()
            } label: {
                Label("MyApp", systemImage: "star")
            }
            #endif
            
            WindowGroup {
                ContentView()
            }
        }
    }
    
    

Menu bar apps can render their content as a menu or inside a dedicated window.
You can control this behavior using the _menuBarExtraStyle_ view modifier.

    
    
    @main struct MyApp: App {
        @State private var menuBarExtraShown = true
        
        var body: some Scene {
            #if os(macOS)
            MenuBarExtra(isInserted: $menuBarExtraShown) {
                MenuBarView()
            } label: {
                Label("MyApp", systemImage: "star")
            }
            .menuBarExtraStyle(.window)
            #endif
            
            WindowGroup {
                ContentView()
            }
        }
    }
    

####  Conclusion

Today we learned how to use new APIs to manage windows in SwiftUI. The
declarative approach we used to see for views is working for high-level
concepts like windows now. Feel free to use it to build iOS, iPadOS, and macOS
apps in a single codebase. Feel free to follow me on [ Twitter
](https://twitter.com/mecid) and ask your questions related to this post.
Thanks for reading, and see you next week!

