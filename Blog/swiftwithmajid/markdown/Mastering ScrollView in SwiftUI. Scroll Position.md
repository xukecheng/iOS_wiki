##  Mastering ScrollView in SwiftUI. Scroll Position

27 Jun 2023

This week we will continue the series of posts dedicated to mastering
_ScrollView_ . Today we will talk about a set of new options for controlling
the scroll content position of a _ScrollView_ in SwiftUI.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

####  Initial position

The SwiftUI framework provides us the brand new _scrollPosition_ view modifier
allowing us to set the initial anchor for the content in the _ScrollView_ .
Let’s take a look at a very quick example.

    
    
    struct ContentView: View {
        var body: some View {
            ScrollView {
                LazyVStack {
                    ForEach(0..<100) { index in
                        Rectangle()
                            .fill(Color.green.gradient)
                            .frame(height: 300)
                            .id(index)
                    }
                }
            }
            .scrollPosition(initialAnchor: .center)
        }
    }
    

As you can see in the example above, we use the new _scrollPosition_ view
modifier to set the initial anchor to the center of the content. The center
option here is the instance of the _UnitPoint_ type, which has a bunch of
predefined values like _bottom_ , _top_ , _trailing_ , _leading_ , etc. You
can also create your own _UnitPoint_ by providing x and y values which take
normalized values from 0 to 1.

    
    
    struct ContentView: View {
        var body: some View {
            ScrollView {
                LazyVStack {
                    ForEach(0..<100) { index in
                        Rectangle()
                            .fill(Color.green.gradient)
                            .frame(height: 300)
                            .id(index)
                    }
                }
            }
            .scrollPosition(initialAnchor: .init(x: 0, y: 0.9)
        }
    }
    

####  Scroll position

Another variant of the new _scrollPosition_ view modifier takes a binding to
the hashable value allowing us to read and write the scroll content offset.

    
    
    struct ContentView: View {
        @State private var position: Int?
        
        var body: some View {
            ScrollView {
                LazyVStack {
                    ForEach(0..<100) { index in
                        Rectangle()
                            .fill(Color.green.gradient)
                            .frame(height: 300)
                            .id(index)
                    }
                }
                .scrollTargetLayout()
            }
            .scrollPosition(id: $position)
        }
    }
    

As you can see in the example above, we use the _scrollPosition_ view modifier
with the binding to the integer value. We also use the _id_ view modifier to
explicitly set the identifier to the view inside the scroll. You don’t need to
set id manually if you are using _ForEach_ with identifiable types or provide
the _KeyPath_ to _id_ .

Remember that you should always use the _scrollTargetLayout_ or _scrollTarget_
view modifiers to allow the _ScrollView_ to understand where to find the
identifiers for the binding.

> To learn more about the _scrollTargetLayout_ and _scrollTarget_ view
> modifiers, take a look at my [ “Mastering ScrollView in SwiftUI. Target
> Behavior” ](/2023/06/20/mastering-scrollview-in-swiftui-target-behavior/)
> post.

As I said before, you can use the _scrollPosition_ view modifier not only for
reading but also to change the scroll content offset. In the following
example, we will add the button changing the value of the binding, and the
scroll view updates content offset accordingly.

    
    
    struct ContentView: View {
        @State private var position: Int?
        
        var body: some View {
            ScrollView {
                LazyVStack {
                    Button("Jump...") {
                        position = 99
                    }
                    
                    ForEach(0..<100) { index in
                        Rectangle()
                            .fill(Color.green.gradient)
                            .frame(height: 300)
                            .id(index)
                    }
                }
                .scrollTargetLayout()
            }
            .scrollPosition(id: $position)
        }
    }
    

####  Indicator flash

Another brand new view modifier related to the scrolling content is the
_scrollIndicatorsFlash_ view modifier. It allows us to show a scroll indicator
whenever needed. For example, you might need to fade in the scroll indicator
while appending the content in the _ScrollView_ .

    
    
    struct ContentView: View {
        @State private var trigger = false
        
        var body: some View {
            ScrollView {
                LazyVStack {
                    Button("Indicator flash") {
                        trigger.toggle()
                    }
                    
                    ForEach(0..<100) { index in
                        Rectangle()
                            .fill(Color.green.gradient)
                            .frame(height: 300)
                            .id(index)
                    }
                }
            }
            .scrollIndicatorsFlash(trigger: trigger)
        }
    }
    

As you can see, we use the _scrollIndicatorsFlash_ view modifier and pass some
equatable value. The _ScrollView_ blinks the indicator as soon as the passed
value changes. I hope you enjoy the post. Feel free to follow me on [ Twitter
](https://twitter.com/mecid) and ask your questions related to this post.
Thanks for reading, and see you next week!

