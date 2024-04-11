##  Building custom layout in SwiftUI. LayoutValueKey.

14 Dec 2022

During the last weeks, we covered many aspects of building custom layouts
using the new _Layout_ protocol in SwiftUI. But we still have a lot to cover.
This week we will learn how to use the _LayoutValueKey_ protocol to pass
custom layout parameters while composing views in the custom layout.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

In the previous posts, we built the flow layout type using the new _Layout_
protocol in SwiftUI. Let’s continue the work on the _FlowLayout_ type by
adding another feature. Assume that we want to tune the anchor point while
placing views in the layout. The first view might use the top point and the
second one use the bottom.

> To learn more about the basics of the _Layout_ protocol, take a look at my
> dedicated [ “Building custom layout in SwiftUI. Basics”
> ](/2022/11/16/building-custom-layout-in-swiftui-basics/) post.

SwiftUI provides us with the _LayoutValueKey_ protocol allowing us to register
a custom layout parameter. We can use this type to attach any value we need to
a view inside the layout and extract this value later in the layout cycle.

First, we should define a type conforming to the _LayoutValueKey_ protocol.

    
    
    struct UnitPointKey: LayoutValueKey {
        static var defaultValue: UnitPoint = .center
    }
    

Creating a custom layout parameter is pretty straightforward. The only thing
we have to do is to provide a default value for the parameter. Second, we
should create an extension on the _View_ type to simplify passing the custom
layout parameters.

    
    
    extension View {
        func anchor(_ anchor: UnitPoint) -> some View {
            layoutValue(key: UnitPointKey.self, value: anchor)
        }
    }
    

As you can see in the example above, we use the _layoutValue_ view modifier to
attach the particular value to the specific type conforming to the
_LayoutValueKey_ protocol. We can use the _layoutValue_ view modifier without
creating an extension on the _View_ type, but the extension provides a much
nicer and cleaner API.

    
    
    Text("!!!")
        .font(.title3)
        .layoutValue(key: UnitPointKey.self, value: .top)
        
    Text("!!!")
        .font(.title3)
        .anchor(.top)
    

Now, we can define a flow layout with the set of views and pass the custom
anchor point for each view inside the layout. Whenever we don’t set the value
for the custom layout parameter, SwiftUI uses the default value we provide.

    
    
    struct ContentView: View {
        var body: some View {
            FlowLayout {
                Text("Hello")
                    .font(.largeTitle)
                    .anchor(.bottom)
                Text("World")
                    .font(.title)
                    .anchor(.top)
                Text("!!!")
                    .font(.title3)
            }
        }
    }
    

The last step is to use the custom layout parameter while placing or sizing
the layout. We can access custom layout parameters by using the subscript on
the _Subview_ proxy type.

    
    
    struct FlowLayout: Layout {
    //  ....
        func placeSubviews(
            in bounds: CGRect,
            proposal: ProposedViewSize,
            subviews: Subviews,
            cache: inout Cache
        ) {
            var lineX = bounds.minX
            var lineY = bounds.minY
            var lineHeight: CGFloat = 0
            
            for index in subviews.indices {
                if lineX + cache.sizes[index].width > (proposal.width ?? 0) {
                    lineY += lineHeight
                    lineHeight = 0
                    lineX = bounds.minX
                }
                
                let anchor = subviews[index][UnitPointKey.self]
                let position = CGPoint(
                    x: lineX + cache.sizes[index].width / 2,
                    y: lineY + cache.sizes[index].height / 2
                )
                
                lineHeight = max(lineHeight, cache.sizes[index].height)
                lineX += cache.sizes[index].width
                
                subviews[index].place(
                    at: position,
                    anchor: anchor,
                    proposal: ProposedViewSize(cache.sizes[index])
                )
            }
        }
    }
    

As you can see in the example above, we use the subscript on the _Subview_
proxy type to extract the value of the _UnitPointKey_ type. Finally, we use
this value to provide an anchor point while placing the views in the layout.

Custom layout parameters allow us to build super customizable and reusable
layouts in SwiftUI very easily. I hope you enjoy the post. Feel free to follow
me on [ Twitter ](https://twitter.com/mecid) and ask your questions related to
this post. Thanks for reading, and see you next week!

