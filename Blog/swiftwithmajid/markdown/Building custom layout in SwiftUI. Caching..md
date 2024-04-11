##  Building custom layout in SwiftUI. Caching.

29 Nov 2022

In the previous post, we talked about the basics of the new _Layout_ protocol.
Today I’m going to continue the series of posts about the new opportunity to
build super-custom reusable layouts by covering the idea of caching layout
information and tuning its performance.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

SwiftUI calls functions of your custom layout many times across the lifecycle
to measure different sizing options during the layout process. It caches a few
things automatically, but you can also implement your own caching mechanics if
you need to improve your layout performance.

> To learn more about the basics of the _Layout_ protocol, take a look at my
> dedicated [ “Building custom layout in SwiftUI. Basics”
> ](/2022/11/16/building-custom-layout-in-swiftui-basics/) post.

The _Layout_ protocol has an associated type called _Cache_ , which is _Void_
by default. But you can define any type you need instead and implement your
custom caching behavior. The easiest way is to define a nested type with the
name _Cache_ inside your custom layout type.

    
    
    struct FlowLayout: Layout {
        struct Cache {
            var sizes: [CGSize] = []
        }
    }
    

The _Layout_ protocol has the _makeCache_ function, which we can implement to
provide a cache instance and make some initial calculations to store during
layout changes.

    
    
    struct FlowLayout: Layout {
        struct Cache {
            var sizes: [CGSize] = []
        }
        
        func makeCache(subviews: Subviews) -> Cache {
            let sizes = subviews.map { $0.sizeThatFits(.unspecified) }
            return Cache(sizes: sizes)
        }
    }
    

The _Layout_ protocol also provides the _updateCache_ function, which we can
use to update our cache. The SwiftUI framework calls this function as soon as
children of the layout change. You can ignore the updateCache function. In
this case, SwiftUI calls the _makeCache_ function and builds the cache from
scratch.

    
    
    struct FlowLayout: Layout {
        struct Cache {
            var sizes: [CGSize] = []
        }
        
        func makeCache(subviews: Subviews) -> Cache {
            let sizes = subviews.map { $0.sizeThatFits(.unspecified) }
            return Cache(sizes: sizes)
        }
        
        func updateCache(_ cache: inout Cache, subviews: Subviews) {
            cache.sizes = subviews.map { $0.sizeThatFits(.unspecified) }
        }
    }
    

As you can see in the example above, the _updateCache_ function provides cache
instance as the _inout_ parameter allowing us to mutate it during the call.

Keep in mind that both _makeCache_ and _updateCache_ functions provide you
only the instance of the _Subviews_ type, a proxy on the list of children. It
doesn’t provide you with the proposed size and bounds rectangle, which means
we can’t calculate the exact position of the views.

Instead, the _Layout_ protocol allows us to mutate our cache in _sizeThatFits_
and _placeSubviews_ functions where we have the proposed size.

    
    
    struct FlowLayout: Layout {
        // ....
    
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
                
                // you can populate cache
                // with additional information here
                
                lineHeight = max(lineHeight, cache.sizes[index].height)
                lineX += cache.sizes[index].width
                
                subviews[index].place(
                    at: position,
                    anchor: .center,
                    proposal: ProposedViewSize(cache.sizes[index])
                )
            }
        }
    }
    

As you can see in the example above, we populate our cache with the exact
position values during the _placeSubviews_ function. Whenever SwiftUI calls
this function, we can check our cache and place subviews in the cached
position. In the case where our cache is empty, we can populate it with the
correct values.

The _Layout_ protocol provides us with all the necessary APIs for building
performant custom layouts. We will continue learning the massive set of APIs
SwiftUI gives us to create reusable and flexible layouts. Feel free to follow
me on [ Twitter ](https://twitter.com/mecid) and ask your questions related to
this post. Thanks for reading, and see you next week!

