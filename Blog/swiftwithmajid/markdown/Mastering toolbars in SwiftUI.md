##  Mastering toolbars in SwiftUI

15 Jul 2020

Toolbar API is another excellent addition to SwiftUI this year. Usually, we
use toolbars to provide available actions. Did you remember the case where you
have a button outside of the navigation bar or bottom bar? This week we will
learn all about the new Toolbar API.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

In the previous version of SwiftUI, we could place buttons in the navigation
bar by using _navigationBarItems_ modifier. Let’s take a quick look at how it
works.

    
    
    import SwiftUI
    
    struct ContentView: View {
        let messages: [String]
    
        var body: some View {
            List(messages, id: \.self) { message in
                Text(message)
            }
            .navigationTitle("Messages")
            .navigationBarItems(trailing: EditButton())
        }
    }
    

The example above looks good, but there is one big issue. It works only with
the navigation bar. For instance, watchOS apps use _NavigationView_ to provide
a navigation stack, but there is no navigation bar to deliver actions. We have
to use 3D touch menus on the watchOS, but then we face another problem. SwitUI
doesn’t provide us API to use 3D touch menus.

Fortunately, Apple released the unified Toolbar API that works on all Apple
platforms. Toolbar API is another example of a declarative API that adapts to
the environment and looks different on different devices. For example, it uses
a navigation bar on iOS, but on watchOS, it inserts a button into the top of
the screen. Let’s take a look at how easily we can use it.

    
    
    import SwiftUI
    
    struct ContentView: View {
        let messages: [String]
    
        var body: some View {
            List(messages, id: \.self) { message in
                Text(message)
            }
            .navigationTitle("Messages")
            .toolbar {
                ToolbarItem(placement: .primaryAction) {
                    Button("New") {}
                }
    
                ToolbarItem(placement: .bottomBar) {
                    Button("Filter") {}
                }
            }
        }
    }
    

As you can see in the example above, SwiftUI provides us the _toolbar_
modifier that we can use to build toolbar items. The _toolbar_ modifier
accepts the _ToolbarContentBuilder_ closure, which is very similar to
_ViewBuilder_ function builder, but instead of views, it uses _ToolbarItems_ .

####  ToolbarItem

We use _ToolbarItem_ struct to declare an action. _ToolbarItem_ has two
required parameters. The first one is placement, which is the instance of
_ToolbarItemPlacement_ struct. The second one is _ViewBuilder_ closure that
SwiftUI uses to build the view representation of your action.

SwiftUI hides all the magic of toolbars behind _ToolbarItemPlacement_ struct.
SwiftUI can put your toolbar item in different places, depending on the value
of the placement parameter. There are multiple placement opportunities. Let’s
talk about the essential options.

  1. _automatic_ \- The item is placed in the default section that varies depending on the current platform. 
  2. _primaryAction_ \- The item represents a primary action. Usually, SwiftUI places this item in the navigation bar on iOS or on top of other views on watchOS. 

There are placement options that we can use only in toolbars presented by a
modal view.

  1. _confirmationAction_ \- The item represents a confirmation action for a modal interface. You can use it in your sheets to confirm saving action. 
  2. _cancellationAction_ \- The item represents a cancellation action for a modal interface. 
  3. _destructiveAction_ \- The item represents a destructive action for a modal interface. You can use it in your modal screens that delete some data. 

There are also a bunch of platform-specific placement options.

  1. _principal_ \- The item is placed in the main item section. For example, you can use it to customize the navigation bar’s title view on iOS. 
  2. _bottomBar_ \- The item is placed in the bottom toolbar. It is available only on iOS. 
  3. _keyboard_ \- The item is placed in the keyboard section. On iOS, keyboard items are above the software keyboard when present. On macOS, keyboard items will be placed inside the Touch Bar. 
  4. _navigationBarLeading_ \- The item is placed in the leading area of the navigation bar. It is available only on iOS and macOS. 
  5. _navigationBarTrailing_ \- The item is placed in the trailing area of the navigation bar. It is available only on iOS and macOS. 

![watchOS-toolbar](/public/watchOS.png)

####  ToolbarContent

We can also create a dedicated type defining our toolbar that we can reuse
across the app. SwiftUI provides us the _ToolbarContent_ protocol that allows
us to create a struct representing a reusable toolbar. Let’s take a look at
how we can use it.

    
    
    import SwiftUI
    
    struct ItemsToolbar: ToolbarContent {
        let add: () -> Void
        let sort: () -> Void
    
        var body: some ToolbarContent {
            ToolbarItem(placement: .primaryAction) {
                Button("Add", action: add)
            }
    
            ToolbarItem(placement: .bottomBar) {
                Button("Sort", action: sort)
            }
        }
    }
    

As you can see in the example above, we create _ItemsToolbar_ struct that
conforms to _ToolbarContent_ protocol. We customize it by providing closures
for adding new items and sorting. Now we can reuse it across the app whenever
we need to present a list of actions for an items list.

    
    
    @main
    struct MyApp: App {
        var body: some Scene {
            WindowGroup {
                NavigationView {
                    Text("Hello World!")
                        .toolbar {
                            ItemsToolbar {
                                // add new item here
                            } sort: {
                                // sort items
                            }
    
                        }
                }
            }
        }
    }
    

####  ToolbarItemGroup

Sometimes we might have several toolbar items in the same placement. Creating
a _ToolbarItem_ for every single button in the toolbar can be very repetitive.
That’s why SwiftUI provides us another type called _ToolbarItemGroup_ .
_ToolbarItemGroup_ allows us to fix toolbar items in the specific placement.
Let’s take a look at a very quick example.

    
    
    import SwiftUI
    
    struct ItemsToolbar: ToolbarContent {
        let add: () -> Void
        let sort: () -> Void
        let filter: () -> Void
    
        var body: some ToolbarContent {
            ToolbarItem(placement: .primaryAction) {
                Button("Add", action: add)
            }
    
            ToolbarItemGroup(placement: .bottomBar) {
                Button("Sort", action: sort)
                Button("Filter", action: filter)
            }
        }
    }
    

####  Conclusion

Today we learned how to use the new Toolbar API to present actions in our apps
in a unified way on different platforms. I hope you enjoy the post. Feel free
to follow me on [ Twitter ](https://twitter.com/mecid) and ask your questions
related to this post. Thanks for reading, and see you next week!

