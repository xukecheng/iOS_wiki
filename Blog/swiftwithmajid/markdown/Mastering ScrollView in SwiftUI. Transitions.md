##  Mastering ScrollView in SwiftUI. Transitions

13 Jun 2023

The fifth iteration of the SwiftUI framework brings a lot of new APIs related
to ScrollView, making it much more powerful than before. This week will begin
the series of posts about new abilities of the ScrollView in SwiftUI, and we
will start with scroll transitions.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

The brand new _scrollTransition_ view modifier allows us to observe the
transition of the view while the user scrolls content. It will enable us to
understand whenever a view is in the viewport of the _ScrollView_ and allows
us to apply visual effects like scaling, rotating, etc. Let’s take a look at a
quick example.

    
    
    struct ContentView: View {
        var body: some View {
            ScrollView {
                ForEach(0..<10, id: \.self) { _ in
                    Rectangle()
                        .fill(Color.random)
                        .frame(width: 300, height: 300)
                        .scrollTransition { view, transition in
                            view.opacity(transition.isIdentity ? 1 : 0.3)
                        }
                }
            }
        }
    }
    

As you can see in the example above, we use the new _scrollTransition_ view
modifier to accept a closure with two parameters. The first is the view
without any effects, and the second is an instance of the
_ScrollTransitionPhase_ type.

![scroll-transition-video](/public/scroll-transition.mp4)

The _ScrollTransitionPhase_ type defines a state of a view transition in the
viewport of an instance of the _ScrollView_ . The _ScrollTransitionPhase_ type
is an enum with three cases: _topLeading_ , _bottomTrailing_ , and _identity_
. The _ScrollTransitionPhase_ enum provides the _isIdentity_ property allowing
us to check whenever the view finished its transition.

Usually, you display the view in the identity phase without any effects. The
SwiftUI framework animates all the changes you apply during the transition. In
our example, I use the _opacity_ view modifier to change the view’s alpha
during the transition.

The _ScrollTransitionPhase_ enum provides another property called _value_ . It
ranges from -1 to 1 and defines the numeric phase of transition where -1 means
_topLeading_ and 1 means _bottomTrailing_ . We can use it to scale our visual
effects while a view transition from _topLeading_ to _bottomTrailing_ .

    
    
    struct ContentView: View {
        var body: some View {
            ScrollView {
                ForEach(0..<10, id: \.self) { _ in
                    Rectangle()
                        .fill(Color.random)
                        .frame(width: 300, height: 300)
                        .scrollTransition { view, transition in
                            view.scaleEffect(transition.isIdentity ? 1 : transition.value)
                        }
                }
            }
        }
    }
    

As you can see in the example above, we use the _value_ property on the
_ScrollTransitionPhase_ type to scale our view while transitioning from one
phase to another.

The _scrollTransition_ view modifier allows us to tune the animation we want
to use while interpolating the transition.

    
    
    struct ContentView: View {
        var body: some View {
            ScrollView {
                ForEach(0..<10, id: \.self) { _ in
                    Rectangle()
                        .fill(Color.random)
                        .frame(width: 300, height: 300)
                        .scrollTransition(.animated(.bouncy)) { view, transition in
                            view.scaleEffect(transition.isIdentity ? 1 : transition.value)
                        }
                }
            }
        }
    }
    

Here we use the bouncy animation to interpolate between transition phases. You
can use a few options to configure the transition: _interactive_ , _animated_
with the particular animation you provide, and _identity_ to disable
animation.

    
    
    struct ContentView: View {
        var body: some View {
            ScrollView {
                ForEach(0..<10, id: \.self) { _ in
                    Rectangle()
                        .fill(Color.random)
                        .frame(width: 300, height: 300)
                        .scrollTransition(
                            topLeading: .identity,
                            bottomTrailing: .interactive
                        ) { view, transition in
                            view.rotationEffect(.radians(transition.value))
                        }
                }
            }
        }
    }
    

We also can use different configurations for _topLeading_ and _bottomTrailing_
transitions. I use the _identity_ configuration to disable transition effects
in this direction.

Today we learned how to use the new _scrollTransition_ view modifier to
animate viewport transitions in the _ScrollView_ . I hope you enjoy the post.
Feel free to follow me on [ Twitter ](https://twitter.com/mecid) and ask your
questions related to this post. Thanks for reading, and see you next week!

