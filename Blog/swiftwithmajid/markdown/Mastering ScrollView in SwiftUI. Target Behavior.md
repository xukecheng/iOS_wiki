##  Mastering ScrollView in SwiftUI. Target Behavior

20 Jun 2023

This year we have massive additions to the _ScrollView_ functionality in
SwiftUI. Apple has added a bunch of new APIs to work with the _ScrollView_ .
This week we will talk about snapping behavior in _ScrollView_ and how we can
customize the scroll target.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

The SwiftUI framework provides the brand-new _scrollTargetBehavior_ view
modifier allowing us to specify a particular snapping behavior. Let’s take a
look at a quick example.

    
    
    struct ContentView: View {
        var body: some View {
            ScrollView {
                ForEach(0..<100) { number in
                    Text(verbatim: String(number))
                        .font(.largeTitle)
                        .frame(minWidth: 0, maxWidth: .infinity, minHeight: 300)
                        .background(Rectangle().fill(Color.green))
                }
            }
            .scrollTargetBehavior(.paging)
        }
    }
    

Here we use the _scrollTargetBehavior_ view modifier with the _paging_ option
to enable scrolling by pages. In this case, the _ScrollView_ uses containing
size to calculate the next visible target.

The paging instance of the _PagingScrollTargetBehavior_ type conforms to the
_ScrollTargetBehavior_ protocol. Another type conforming to the
_ScrollTargetBehavior_ protocol is _ViewAlignedScrollTargetBehavior_ .

    
    
    struct ContentView: View {
        var body: some View {
            ScrollView {
                ForEach(0..<100) { number in
                    Text(verbatim: String(number))
                        .font(.largeTitle)
                        .frame(minWidth: 0, maxWidth: .infinity, minHeight: 300)
                        .background(Rectangle().fill(Color.green))
                        .scrollTarget()
                }
            }
            .scrollTargetBehavior(.viewAligned)
        }
    }
    

As you can see in the example above, we use the _scrollTargetBehavior_ view
modifier with the _viewAligned_ option to enable view snapping. _ScrollView_
automatically decelerates after scrolling to align with the first visible item
in its viewport. The _ScrollView_ looking for the views marked with the
_scrollTarget_ view modifier to align.

Usually, you define the _ScrollView_ with the layout container inside, like
_LazyVGrid_ or _LazyVStack_ . In this case, you should use the
_scrollTargetLayout_ view modifier on an instance of the _LazyVGrid_ or
_LazyVStack_ to allow the _ScrollView_ to target views inside the container.

    
    
    struct ExampleScrollView: View {
        var body: some View {
            ScrollView {
                LazyVStack {
                    ForEach(0..<100) { number in
                        Text(verbatim: String(number))
                            .font(.largeTitle)
                            .frame(minWidth: 0, maxWidth: .infinity, minHeight: 300)
                            .background(Rectangle().fill(Color.green))
                    }
                }
                .scrollTargetLayout()
            }
            .scrollTargetBehavior(.viewAligned)
        }
    }
    

You can also use the _scrollTarget_ and _scrollTargetLayout_ view modifiers in
a single _ScrollView_ to mark individual views as scroll targets in pair with
the items in the layout container.

    
    
    struct AnotherExampleScrollView: View {
        var body: some View {
            ScrollView {
                CustomHeaderView()
                    .scrollTarget()
                
                LazyVStack {
                    // some content here
                }
                .scrollTargetLayout()
                
                CustomFooterView()
                    .scrollTarget()
            }
            .scrollTargetBehavior(.viewAligned)
        }
    }
    

Remember that you can use the _scrollTargetBehavior_ view modifier to set the
horizontal and vertical scrolling target. It depends on how you allow axes on
the _ScrollView_ .

    
    
    struct ExampleScrollView: View {
        var body: some View {
            ScrollView(.horizontal) {
                LazyHStack {
                    ForEach(0..<100) { number in
                        Text(verbatim: String(number))
                            .font(.largeTitle)
                            .frame(minWidth: 0, maxWidth: .infinity, minHeight: 300)
                            .background(Rectangle().fill(Color.green))
                    }
                }
                .scrollTargetLayout()
            }
            .scrollTargetBehavior(.viewAligned)
        }
    }
    

The SwiftUI provides two options for scrolling target behavior: _viewAligned_
and _paging_ . But you can create your types by conforming to the
_ScrollTargetBehavior_ protocol.

    
    
    struct CustomScrollTargetBehavior: ScrollTargetBehavior {
        func updateTarget(_ target: inout ScrollTarget, context: TargetContext) {
            if context.velocity.dy > 0 {
                target.rect.origin.y = context.originalTarget.rect.maxY
            } else if context.velocity.dy < 0 {
                target.rect.origin.y = context.originalTarget.rect.minY
            }
        }
    }
    
    extension ScrollTargetBehavior where Self == CustomScrollTargetBehavior {
        static var custom: CustomScrollTargetBehavior { .init() }
    }
    
    struct ContentView: View {
        var body: some View {
            ScrollView {
                ForEach(0..<100) { number in
                    Text(verbatim: String(number))
                        .font(.largeTitle)
                        .frame(minWidth: 0, maxWidth: .infinity, minHeight: 300)
                        .background(Rectangle().fill(Color.green))
                }
            }
            .scrollTargetBehavior(.custom)
        }
    }
    

As you can see in the example above, we define the
_CustomScrollTargetBehavior_ type conforming to the _ScrollTargetBehavior_
protocol. It needs to implement the only required function called
_updateTarget_ . The _updateTarget_ function has two parameters _target_ and
_context_ .

The _target_ parameter is an inout instance of the _ScrollTarget_ type and
allows us to set the _rect_ and _anchor_ point for our target inside the
_ScrollView_ .

The _context_ parameter is an instance of the _ScrollTargetBehaviorContext_
type and provides information about the context in which the scroll target
updates. It provides access to enabled axes, velocity, container size, content
size, original target, etc.

> To learn more about additions to the _ScrollView_ , take a look at my [
> “Mastering ScrollView in SwiftUI. Transitions” ](/2023/06/13/mastering-
> scrollview-in-swiftui-transitions/) post.

With these additions, the _ScrollView_ type gains a lot of power and allows us
to build a super-custom experience for our users on all Apple platforms. I
hope you enjoy the post. Feel free to follow me on [ Twitter
](https://twitter.com/mecid) and ask your questions related to this post.
Thanks for reading, and see you next week!

