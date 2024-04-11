##  Animations in SwiftUI

26 Jun 2019

SwiftUI brings declarative and straightforward approach in building User
Interfaces. We have _List_ and _Form_ components and _Bindings_ . All of these
things make SwiftUI so easy to use and very powerful. But today we are going
to talk about another feature of SwiftUI, and it is animations.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

####  Animation

You can smoothly animate any change in SwiftUI by wrapping it into
_withAnimation_ block. By default, SwiftUI uses fade in and fade out for
animating changes. Let’s take a look at a small example.

    
    
    struct ContentView : View {
        @State private var isButtonVisible = true
    
        var body: some View {
            VStack {
                Button(action: {
                    withAnimation {
                        self.isButtonVisible.toggle()
                    }
                }) {
                    Text("Press me")
                }
    
                if isButtonVisible {
                    Button(action: {}) {
                        Text("Hidden Button")
                    }
                }
            }
        }
    }
    

In the current example, we wrap the _State_ change with _withAnimation_ block,
and it produces nice fade in animation. You can modify animation by passing
timing and spring values. Another option can be attaching animation modifier
to the animating view.

    
    
    struct ContentView : View {
        @State private var isButtonVisible = true
    
        var body: some View {
            VStack {
                Button(action: {
                    self.isButtonVisible.toggle()
                }) {
                    Text("Press me")
                }
    
                if isButtonVisible {
                    Button(action: {}) {
                        Text("Hidden Button")
                    }.animation(.easeInOut, value: isButtonVisible)
                }
            }
        }
    }
    

In the code sample above, we achieve the same animation by simply adding
animation modifier. We use _easeInOut_ animation, but you can pass custom
animation properties. The second parameter is the equatable value that SwiftUI
observes to understand changes and animate them.

Sometimes we have a situation where multiple views depend on some state, and
we want to animate all depending view changes together. For this case, we have
animatable bindings.

    
    
    struct ContentView : View {
        @State private var isButtonVisible = true
    
        var body: some View {
            VStack {
                Toggle(isOn: $isButtonVisible.animation()) {
                    Text("Show/Hide button")
                }
    
                if isButtonVisible {
                    Button(action: {}) {
                        Text("Hidden Button")
                    }
                }
            }
        }
    }
    

As you can see, we can easily convert our binding into animatable binding by
calling animation method on it. This method wraps every change of binding
value into an animation block. You can pass animation settings as parameters
to this method. More about bindings you can read in my [ previous post
](/2019/06/12/understanding-property-wrappers-in-swiftui) .

####  Transitions

As I said before, SwiftUI uses fade in and fade out transition by default, but
we can apply any other transition we want. Let’s replace fading with moving.

    
    
    struct ContentView : View {
        @State private var isButtonVisible = true
    
        var body: some View {
            VStack {
                Toggle(isOn: $isButtonVisible.animation()) {
                    Text("Show/Hide button")
                }
    
                if isButtonVisible {
                    Button(action: {}) {
                        Text("Hidden Button")
                    }.transition(.move(edge: .trailing))
                }
            }
        }
    }
    

In the example above, we attach transition modifier to the view. SwiftUI has a
bunch of ready to use transitions like _move_ , _slide_ , _scale_ , _offset_ ,
_opacity_ , etc. We can combine them into a single transition. Let’s take a
look at the example.

    
    
    extension AnyTransition {
        static func moveAndScale(edge: Edge) -> AnyTransition {
            AnyTransition.move(edge: edge).combined(with: .scale())
        }
    }
    
    struct ContentView : View {
        @State private var isButtonVisible = true
    
        var body: some View {
            VStack {
                Toggle(isOn: $isButtonVisible.animation()) {
                    Text("Show/Hide button")
                }
    
                if isButtonVisible {
                    Button(action: {}) {
                        Text("Hidden Button")
                    }.transition(.moveAndScale(edge: .trailing))
                }
            }
        }
    }
    

We created a _moveAndScale_ transition, which is basically a combination of
move and scale transitions. SwiftUI applies the current transition
symmetrically according to timing or spring values which you pass into the
animation method.

SwiftUI provides a way of building asymmetric transitions also. Assume that
you need a move transition on insertion and a fade transition on removal. For
those cases, we have an _asymmetric_ method on _AnyTransition_ struct, which
we can use to build asymmetric transitions.

    
    
    extension AnyTransition {
        static func moveOrFade(edge: Edge) -> AnyTransition {
            AnyTransition.asymmetric(
                insertion: .move(edge: edge),
                removal: .opacity
            )
        }
    }
    
    struct ContentView : View {
        @State private var isButtonVisible = true
    
        var body: some View {
            VStack {
                Toggle(isOn: $isButtonVisible.animation()) {
                    Text("Show/Hide button")
                }
    
                if isButtonVisible {
                    Button(action: {}) {
                        Text("Hidden Button")
                    }.transition(.moveOrFade(edge: .trailing))
                }
            }
        }
    }
    

As you can see, we use _asymmetric_ method to pass two transitions, the first
one for insertion and another one for removal. We can pass here combined
transition which we created.

####  Conclusion

Today we discussed multiple ways of animating changes in SwiftUI. It totally
depends on you and on use-case which way you have to choose. By spending more
and more time with SwiftUI, I understand that it is already a compelling
framework. Feel free to follow me on [ Twitter ](https://twitter.com/mecid)
and ask your questions related to this post. Thanks for reading and see you
next week!

