##  Tabs and pages in SwiftUI

16 Sep 2020

This week we will talk about creating tabs and pager views in SwiftUI.
_TabView_ gained superpower during WWDC20. We can now use it across all the
Apple platforms to build tabbed and paged user experiences with SwiftUI out of
the box.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

####  Basics

_TabView_ is a container view that puts children views into separated tabs.
Let’s start with a quick example.

    
    
    import SwiftUI
    
    struct ContentView: View {
        var body: some View {
            TabView {
                Text("Hello")
                Text("World")
            }
        }
    }
    

As you can see, we just wrap our views with _TabView_ , and that’s it. SwiftUI
creates a tab-based user interface to switch our views. We can decorate our
tabs with text labels and images using the _tabItem_ modifier by adding it to
_TabView_ children.

    
    
    import SwiftUI
    
    struct ContentView: View {
        var body: some View {
            TabView {
                Text("Hello")
                    .tabItem {
                        Image(systemName: "heart.fill")
                        Text("Tab1")
                    }
                Text("World")
                    .tabItem {
                        Text("Tab2")
                    }
            }
        }
    }
    

Remember that we can only use _Image_ and _Text_ views inside _tabItem_
closure to decorate our tabs. Sometimes we need to control the selected tab of
our _TabView_ to switch it during deep linking or while opening a
notification. There is another _TabView_ initializer that we can use to make
programmatic tab switching possible.

    
    
    import SwiftUI
    
    struct ContentView: View {
        @State private var selection = 0
    
        var body: some View {
            TabView(selection: $selection) {
                Text("Hello")
                    .tabItem {
                        Image(systemName: "heart.fill")
                        Text("Tab1")
                    }.tag(0)
                Text("World")
                    .tabItem {
                        Text("Tab2")
                    }.tag(1)
            }
        }
    }
    

As you can see in the example above, we need to provide a selection binding to
a _TabView_ . We can change the value of our state property to switch tabs
programmatically. We also need to use a tag modifier to provide a value
associated with the view. SwiftUI switches tabs using tag value.

####  Pager view

We can easily replace our tabbed user interface with paged one by applying the
_tabViewStyle_ modifier on the view that contains _TabView_ or on _TabView_
itself. Let’s take a look at how we can do that.

    
    
    struct ContentView: View {
        var body: some View {
            TabView {
                Text("Hello")
                Text("World")
            }.tabViewStyle(PageTabViewStyle(indexDisplayMode: .always))
        }
    }
    

As you can see in the example above, we set an instance of _PageTabViewStyle_
struct as the style of our _TabView_ . We can also control whenever we want to
show the page indicator using the _indexDisplayMode_ parameter.

_TabView_ ’s selection binding fully supports animations. It means that you
can wrap the binding changes using the _withAnimation_ function and
programmatically animate page transition. You might need it when your designs
contain buttons for the next and previous pages.

    
    
    import SwiftUI
    
    struct ContentView: View {
        @State private var selection = 0
    
        var body: some View {
            ZStack(alignment: .bottom) {
                TabView(selection: $selection) {
                    Text("Hello").tag(0)
                    Text("World").tag(1)
                }.tabViewStyle(PageTabViewStyle(indexDisplayMode: .always))
    
                Button("next") {
                    withAnimation {
                        selection = 1
                    }
                }
            }
        }
    }
    

####  Conclusion

I’m happy to see that this year _TabView_ supports all the platforms. You can
use it on watchOS to build a paged user experience or macOS in the settings
scene that will apply the correct styling to match the settings screen that we
used to see on macOS. It also looks great and adapts to tvOS styling when you
use it in a TV app.

I hope you enjoy the post. Feel free to follow me on [ Twitter
](https://twitter.com/mecid) and ask your questions related to this article.
Thanks for reading, and see you next week!

