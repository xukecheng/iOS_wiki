##  Building custom layout in SwiftUI. Spacing.

06 Dec 2022

Multiple layouts allow us to compose views in different ways. One crucial
thing is the spacing between children of the concrete layout. This week we
will learn how to build a custom layout allowing us to specify a particular
spacing between views and how to respect the platform-oriented predefined
spacing rules in SwiftUI.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

As many types we create in Swift, the type conforming to the _Layout_ protocol
can define its properties and initialize it via the _init_ function. Our
_FlowLayout_ type is not an exception here. Let’s add the _spacing_ property
to the _FlowLayout_ type.

    
    
    struct FlowLayout: Layout {
        var spacing: CGFloat = 0
        
        struct Cache {
            var sizes: [CGSize] = []
        }
        
        func makeCache(subviews: Subviews) -> Cache {
            let sizes = subviews.map { $0.sizeThatFits(.unspecified) }
            return Cache(sizes: sizes)
        }
    }
    

> To learn more about the basics of the _Layout_ protocol, take a look at my
> dedicated [ “Building custom layout in SwiftUI. Basics”
> ](/2022/11/16/building-custom-layout-in-swiftui-basics/) post.
    
    
    struct ContentView: View {
        var body: some View {
            FlowLayout(spacing: 8) {
                Text("Hello")
                    .font(.largeTitle)
                Text("World")
                    .font(.title)
                Text("!!!")
                    .font(.title3)
            }
            .border(Color.red)
        }
    }
    

As you can see in the example above, now we can place an instance of the
_FlowLayout_ type with the particular spacing between views. But first, we
should tune the _sizeThatFits_ function to respect the spacing between views
while calculating the final size of the layout.

    
    
    struct FlowLayout: Layout {
    //  ....
        func sizeThatFits(
            proposal: ProposedViewSize,
            subviews: Subviews,
            cache: inout Cache
        ) -> CGSize {
            var totalHeight = 0.0
            var totalWidth = 0.0
            
            var lineWidth = 0.0
            var lineHeight = 0.0
            
            for index in subviews.indices {
                if lineWidth + cache.sizes[index].width > proposal.width ?? 0 {
                    totalHeight += lineHeight
                    lineWidth = cache.sizes[index].width
                    lineHeight = cache.sizes[index].height
                } else {
                    lineWidth += cache.sizes[index].width + spacing
                    lineHeight = max(lineHeight, cache.sizes[index].height)
                }
                
                totalWidth = max(totalWidth, lineWidth)
            }
            
            totalHeight += lineHeight
            
            return .init(width: totalWidth, height: totalHeight)
        }
    }
    

Second, we must add spacing between views while placing them in the
_placeSubviews_ function.

    
    
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
                
                let position = CGPoint(
                    x: lineX + cache.sizes[index].width / 2,
                    y: lineY + cache.sizes[index].height / 2
                )
                
                lineHeight = max(lineHeight, cache.sizes[index].height)
                lineX += cache.sizes[index].width + spacing
                
                subviews[index].place(
                    at: position,
                    anchor: .center,
                    proposal: ProposedViewSize(cache.sizes[index])
                )
            }
        }
    }
    

Finally, we have a fully working _FlowLayout_ that allows us to set the custom
spacing between views.

####  Preferred spacing

As you can see, most of the layouts in SwiftUI allow us to set the spacing to
_nil_ , where the layout uses the preferred spacing instead of zero. SwiftUI
has spacing preferences between views. For example, it has preferred spacing
between _Image_ and _Text_ views, but this value might differ from _Text_ to
_Text_ views. And these spacing preferences might be different for iOS, macOS,
watchOS, and tvOS.

Fortunately, SwiftUI provides an API to calculate spacing between views by
respecting platform-oriented spacing preferences. This API is a part of the
_Layout_ protocol and lives in the _Subview_ proxy type.

    
    
    struct FlowLayout: Layout {
        var spacing: CGFloat? = nil
        
        struct Cache {
            var sizes: [CGSize] = []
            var spacing: [CGFloat] = []
        }
        
        func makeCache(subviews: Subviews) -> Cache {
            let sizes = subviews.map { $0.sizeThatFits(.unspecified) }
            let spacing: [CGFloat] = subviews.indices.map { index in
                guard index != subviews.count - 1 else {
                    return 0
                }
                
                return subviews[index].spacing.distance(
                    to: subviews[index+1].spacing,
                    along: .horizontal
                )
            }
            
            return Cache(sizes: sizes, spacing: spacing)
        }
    }
    

Let’s start by adding the _spacing_ property to our cache. It is a perfect
candidate to live in the cache because we want to calculate it once when the
list of the subviews changes.

Next, we iterate over the subviews and use the _spacing_ property on the
_Subview_ type to call the _distance_ function with the following view as a
parameter to calculate the preferred spacing between two views in the
horizontal axis. We also can measure vertical spacing between views if needed
by using the same function with vertical parameter for axis.

> To learn more about implementing a layout cache, take a look at my dedicated
> [ “Building custom layout in SwiftUI. Caching.” ](/2022/11/29/building-
> custom-layout-in-swiftui-caching/) post.

Let’s tune the _sizeThatFits_ function to respect the spacing between views
while calculating the final size of the layout.

    
    
    struct FlowLayout: Layout {
        func sizeThatFits(
            proposal: ProposedViewSize,
            subviews: Subviews,
            cache: inout Cache
        ) -> CGSize {
            var totalHeight = 0.0
            var totalWidth = 0.0
            
            var lineWidth = 0.0
            var lineHeight = 0.0
            
            for index in subviews.indices {
                if lineWidth + cache.sizes[index].width > proposal.width ?? 0 {
                    totalHeight += lineHeight
                    lineWidth = cache.sizes[index].width
                    lineHeight = cache.sizes[index].height
                } else {
                    lineWidth += cache.sizes[index].width + (spacing ?? cache.spacing[index])
                    lineHeight = max(lineHeight, cache.sizes[index].height)
                }
                
                totalWidth = max(totalWidth, lineWidth)
            }
            
            totalHeight += lineHeight
            
            return .init(width: totalWidth, height: totalHeight)
        }
    }
    

The next step is to add spacing between views while placing them. We can apply
similar changes to the _placeSubviews_ function to respect the preferred
spacing between different views.

    
    
    struct FlowLayout: Layout {
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
                
                let position = CGPoint(
                    x: lineX + cache.sizes[index].width / 2,
                    y: lineY + cache.sizes[index].height / 2
                )
                
                lineHeight = max(lineHeight, cache.sizes[index].height)
                lineX += cache.sizes[index].width + (spacing ?? cache.spacing[index])
                
                subviews[index].place(
                    at: position,
                    anchor: .center,
                    proposal: ProposedViewSize(cache.sizes[index])
                )
            }
        }
    }
    

Finally, we have a flow layout that respects the preferred view spacing by
default. The _Layout_ protocol provides us with the reach API to build
reusable layouts across all the platforms. We should carefully learn the API
SwiftUI provides to create layouts respecting the platform-oriented rules.

    
    
    struct ContentView: View {
        var body: some View {
            FlowLayout {
                Text("Hello")
                    .font(.largeTitle)
                Text("World")
                    .font(.title)
                Text("!!!")
                    .font(.title3)
            }
            .border(Color.red)
        }
    }
    

I hope you enjoy the post. Feel free to follow me on [ Twitter
](https://twitter.com/mecid) and ask your questions related to this post.
Thanks for reading, and see you next week!

