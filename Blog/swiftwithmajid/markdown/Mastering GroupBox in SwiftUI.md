##  Mastering GroupBox in SwiftUI

15 Oct 2020

Styleable views is the thing I love in SwiftUI. You can separate your view
logic and its style. You can easily apply different styles in different
conditions whenever you need to change appearance depending on the platform or
other environmental requirements. This week we will talk about _GroupBox_ ,
another view container that SwiftUI provides, and allows us easily change its
look and feel using a style protocol.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

####  Basics

_GroupBox_ is a stylized view with an optional label that is associated with a
logical grouping of content. Default styling on iOS is a simple card with the
title and content. Let’s take a look at it.

    
    
    import SwiftUI
    
    struct ContentView: View {
        var body: some View {
            GroupBox(
                label: Label("Heart Rate", systemImage: "heart.fill")
                    .foregroundColor(.red)
            ) {
                Text("Your hear rate is 90 BPM.")
            }.padding()
        }
    }
    

![group-box](/public/groupbox1.png)

As you can see in the example above, the default styling of _GroupBox_ is a
card with the system grouped background and continuous corner radius. It looks
similar to cards that we used to see in the Apple Health app or Apple Fitness
app. I should mention that it can look differently on different Apple
platforms. It is available for macOS and iOS now, but I hope to see it on
watchOS and tvOS during the next iteration of SwiftUI.

Cards are great, and I use them a lot in my apps. You can use _GroupBox_ as
the root container for every item in your grid or stack, and you will gain a
modest card-based look and feel.

    
    
    import SwiftUI
    
    struct ContentView: View {
        var body: some View {
            ScrollView {
                LazyVGrid(columns: [.init(), .init()]) {
                    ForEach(0..<10) { _ in
                        GroupBox(
                            label: Label("Heart Rate", systemImage: "heart.fill")
                                .foregroundColor(.red)
                        ) {
                            Text("Your hear rate is 90 BPM.")
                        }.groupBoxStyle(PlainGroupBoxStyle())
                    }
                }.padding()
            }
        }
    }
    

![group-box](/public/groupbox2.png)

As you can see, SwiftUI provides nice card-based styling for _GroupBox_ view
by default. Sometimes it is not what we need. For example, when you place
_GroupBox_ inside a grouped _List_ , it looks like a card inside a card.
Fortunately, we can tune the look and feel using the _GroupBoxStyle_ protocol.

> To learn more about grids in SwiftUI, take a look at my [ “Mastering grids
> in SwiftUI” ](/2020/07/08/mastering-grids-in-swiftui/) post.

####  Styling

SwiftUI provides us the _GroupBoxStyle_ protocol that allows us to change the
look and feel of any _GroupBox_ instance completely. We can create different
styles for any use-cases we need. For example, I don’t need a background and
corner radius when I use _GroupBox_ inside a _List_ .

    
    
    struct PlainGroupBoxStyle: GroupBoxStyle {
        func makeBody(configuration: Configuration) -> some View {
            VStack(alignment: .leading) {
                configuration.label
                configuration.content
            }
        }
    }
    
    struct ContentView: View {
        var body: some View {
            GroupBox(
                label: Label("Heart Rate", systemImage: "heart.fill")
                    .foregroundColor(.red)
            ) {
                Text("Your hear rate is 90 BPM.")
            }.groupBoxStyle(PlainGroupBoxStyle())
        }
    }
    

All you need to do to create your own _GroupBox_ style is create a struct that
conforms to _GroupBoxStyle_ protocol. _GroupBoxStyle_ has the only
requirement. You have to create a _makeBody_ function that accepts an instance
of _GroupBoxStyleConfiguration_ type and returns a new view.

_GroupBoxStyleConfiguration_ provides us both the label and content of our
_GroupBox_ . You can use them inside the _makeBody_ function as you need. Our
_PlainGroupBoxStyle_ example put the label and content view inside a _VStack_
with leading alignment and returns the stack.

You can set the style by using the _groupBoxStyle_ modifier. SwiftUI will
share it using environment across all children of the view hierarchy.

![group-box](/public/groupbox3.png)

You can create super custom _GroupBox_ styles. To show more complex styling
options, let’s replicate the default card-based layout.

    
    
    struct CardGroupBoxStyle: GroupBoxStyle {
        func makeBody(configuration: Configuration) -> some View {
            VStack(alignment: .leading) {
                configuration.label
                configuration.content
            }
            .padding()
            .background(Color(.systemGroupedBackground))
            .clipShape(RoundedRectangle(cornerRadius: 8, style: .continuous))
        }
    }
    

As you can see, we are able to create any _GroupBox_ style we need. Another
option might be a style that hides the label or something else.

> To learn more about other styling protocols available in SwiftUI, take a
> look at [ “Mastering buttons in SwiftUI” ](/2020/02/19/mastering-buttons-in-
> swiftui/) post.

####  Conclusion

_GroupBox_ provides us a simple card-based look and feel that we used to see
in many apps on iOS. The great thing about _GroupBox_ that it allows us to
customize its appearance as we need. I hope you enjoy the post. Feel free to
follow me on [ Twitter ](https://twitter.com/mecid) and ask your questions
related to this article. Thanks for reading, and see you next week!

