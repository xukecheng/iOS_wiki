##  Mastering ControlGroup in SwiftUI

21 Oct 2021

One of the new container views delivered in SwiftUI Release 3 was the
_ControlGroup_ view. The _ControlGroup_ view displays semantically-related
controls in a visually appropriate manner for the context. This week we will
learn how to use and customize the appearance of the _ControlGroup_ view in
SwiftUI.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

####  Basics

The _ControlGroup_ view is the simple container view that accepts
_ViewBuilder_ closure and displays it depending on the current environment.
Let’s see how we can use it.

> To learn more about _ViewBuilder_ , take a look at my dedicated [ “The power
> of @ViewBuilder in SwiftUI” ](/2019/12/18/the-power-of-viewbuilder-in-
> swiftui/) post.
    
    
    struct ContentView: View {
        var body: some View {
            ControlGroup {
                Button(action: {}) {
                    Label("Decrease", systemImage: "minus")
                }
    
                Button(action: {}) {
                    Label("Increase", systemImage: "plus")
                }
            }
        }
    }
    

![controlgroup](/public/controlgroup1.png)

As you can see in the example above, we simply put two buttons inside the
_ControlGroup_ view as we do with _VStack_ or _HStack_ . But instead of laying
out views using vertical or horizontal axes, the _ControlGroup_ adds the
semantic look and feel depending on the view’s placement.

####  Styling

The _ControlGroup_ view has a few styling options out of the box. SwiftUI
provides _automatic_ and _navigation_ styles. The _automatic_ style is used by
default, but you can set another style directly using the _controlGroupStyle_
view modifier. SwiftUI uses the _navigation_ style when you place the
_ControlGroup_ view in the toolbar of the _NavigationView_ .

    
    
    struct ContentView: View {
        var body: some View {
            ControlGroup {
                Button(action: {}) {
                    Label("Decrease", systemImage: "minus")
                }
    
                Button(action: {}) {
                    Label("Increase", systemImage: "plus")
                }
            }
            .controlGroupStyle(.navigation)
        }
    }
    

![navigation-styled-controlgroup](/public/controlgroup2.png)

As you can see in the example, we use the _controlGroupStyle_ view modifier to
set the style manually. SwiftUI uses the same approach for many different
views and allows us to create our own style types by conforming to a protocol.
In the case of the _ControlGroup_ view, we should create a type that conforms
to the _ControlGroupStyle_ protocol and implement the single required function
called _makeBody_ .

> To learn more about other styling protocols available in SwiftUI, take a
> look at [ “Mastering buttons in SwiftUI” ](/2020/02/19/mastering-buttons-in-
> swiftui/) post.
    
    
    struct VerticalControlGroupStyle: ControlGroupStyle {
        func makeBody(configuration: Configuration) -> some View {
            VStack {
                configuration.content
            }.foregroundColor(.red)
        }
    }
    
    struct ContentView: View {
        var body: some View {
            ControlGroup {
                Button("Action 1") {}
                Button("Action 2") {}
            }
            .controlGroupStyle(VerticalControlGroupStyle())
        }
    }
    

![custom-styled-controlgroup](/public/controlgroup3.png)

The _makeBody_ function has the single parameter of _Configuration_ type that
you can use to access the content of the _ControlGroup_ passed via
_ViewBuilder_ closure. It allows you to modify the look and feel of the
content in the way you need by applying any view modifiers you want. In the
current example, we place the content in the vertical stack and set the
foreground color to red.

    
    
    struct ControlGroupWithTitle: ControlGroupStyle {
        let title: LocalizedStringKey
    
        func makeBody(configuration: Configuration) -> some View {
            VStack {
                Text(title)
                    .font(.title)
                HStack {
                    configuration.content
                }
            }
        }
    }
    
    struct ContentView: View {
        var body: some View {
            ControlGroup {
                Button("Action 1") {}
                Button("Action 2") {}
            }
            .controlGroupStyle(ControlGroupWithTitle(title: "Actions"))
        }
    }
    

![custom-styled-controlgroup](/public/controlgroup4.png)

We also can change the look and feel by adding new views and wrapping the
content with another container view.

    
    
    extension ControlGroupStyle where Self == ControlGroupWithTitle {
        static func with(title: LocalizedStringKey) -> ControlGroupWithTitle {
            ControlGroupWithTitle(title: title)
        }
    }
    
    struct ContentView: View {
        var body: some View {
            ControlGroup {
                Button("Action 1") {}
                Button("Action 2") {}
            }.controlGroupStyle(.with(title: "Actions"))
        }
    }
    

Swift 5.5 allows us to write extensions for protocols with associated types
and improve the usage of our custom styles provided to the _controlGroupStyle_
view modifier.

####  Conclusion

The _ControlGroup_ view is a new way to group buttons and other controls in a
semantic way. I really love SwiftUI because it uses the same approach across
the many views to provide custom styling options. I hope you enjoy the post.
Feel free to follow me on [ Twitter ](https://twitter.com/mecid) and ask your
questions related to this post. Thanks for reading, and see you next week!

