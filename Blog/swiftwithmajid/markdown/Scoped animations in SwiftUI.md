##  Scoped animations in SwiftUI

21 Nov 2023

Animations were the most powerful feature of SwiftUI from day one. You can
quickly build fluid animations in SwiftUI. The only downside was how we
control animations whenever we need to run multi-step animation or scope the
animation to a particular part of the view hierarchy.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

Let’s start with a simple example showing a few downsides of our old
approaches to drive animations in SwiftUI.

    
    
    struct ContentView: View {
        @State private var isHidden = false
        
        var body: some View {
            VStack {
                Button("Animate") {
                    isHidden.toggle()
                }
                
                HugeView()
                    .opacity(isHidden ? 0.0 : 1.0)
                    
                AnotherHugeView()
            }
            .animation(.default)
        }
    }
    

As you can see in the example above, we have a view hierarchy with a button
and two views placed in the vertical stack. We attach the _animation_ view
modifier to the whole stack to animate any change inside.

When we press the button, the stack animates any changes inside. Still, the
_animation_ view modifier doesn’t connect to the _isHidden_ property, which
means it will animate any change that can happen. Some of these changes can be
unexpected, like environmental value change.

We can eliminate unexpected animations by using another version of the
_animation_ view modifier where we can bind to a particular value and animate
only when the value changes.

    
    
    struct ContentView: View {
        @State private var isHidden = false
        
        var body: some View {
            VStack {
                Button("Animate") {
                    isHidden.toggle()
                }
                
                HugeView()
                    .opacity(isHidden ? 0.0 : 1.0)
                
                AnotherHugeView()
            }
            .animation(.default, value: isHidden)
        }
    }
    

In the example above, we use the _animation_ view modifier with the _value_
parameter. It allows us to scope the animation to a single value and animate
changes only correlated with the particular value. In this case, we don’t have
any unexpected animations.

What if we have more than one animatable property? We must attach an
_animation_ modifier for every animatable property in this case. This solution
works very well but has a downside on the ergonomic side.

    
    
    struct ContentView: View {
        @State private var firstStep = false
        @State private var secondStep = false
        
        var body: some View {
            VStack {
                Button("Animate") {
                    Task {
                        firstStep.toggle()
                        try? await Task.sleep(nanoseconds: 3_000_000_000)
                        secondStep.toggle()
                    }
                }
                
                // other views here
                
                SomeView()
                    .opacity(firstStep ? 1.0 : 0.0)
                    .blur(radius: secondStep ? 0 : 20.0)
            }
            .animation(.default, value: firstStep)
            .animation(.default, value: secondStep)
        }
    }
    

Fortunately, SwiftUI introduced a new variant of the _animation_ view
modifier, allowing us to scope animations using a _ViewBuilder_ closure.

    
    
    struct ContentView: View {
        @State private var firstStep = false
        @State private var secondStep = false
        
        var body: some View {
            VStack {
                Button("Animate") {
                    Task {
                        firstStep.toggle()
                        try? await Task.sleep(nanoseconds: 1_000_000_000)
                        secondStep.toggle()
                    }
                }
                
                // other views here
                
                SomeView()
                    .animation(.default) { content in
                        content
                            .opacity(firstStep ? 1.0 : 0.0)
                            .blur(radius: secondStep ? 0 : 20.0)
                    }
            }
        }
    }
    

As you can see in the example above, we use the _animation_ view modifier by
providing a type of animation we need and a _ViewBuilder_ closure where this
animation applies. The animation works only in the context of the provided
_ViewBuilder_ closure and doesn’t spread anywhere else.

As a starting point, the _ViewBuilder_ closure provides a single parameter,
the placeholder for the view where you have applied the _animation_ view
modifier. It is safe to apply any view modifiers to your view inside the
_ViewBuilder_ closure and expect animation only for this code block.

    
    
    struct ContentView: View {
        @State private var firstStep = false
        @State private var secondStep = false
        
        var body: some View {
            VStack {
                Button("Animate") {
                    Task {
                        firstStep.toggle()
                        try? await Task.sleep(nanoseconds: 1_000_000_000)
                        secondStep.toggle()
                    }
                }
                
                // other views here
                
                SomeView()
                    .transaction { t in
                        t.animation = t.animation?.speed(2)
                    } body: { content in
                        content
                            .opacity(firstStep ? 1.0 : 0.0)
                            .blur(radius: secondStep ? 0 : 20.0)
                    }
            }
        }
    }
    

As you can see, SwiftUI provides a similar way to maintain scoped transactions
in the view hierarchy.

> To learn more about transactions in SwiftUI, take a look at my dedicated [
> “Transactions in SwiftUI” ](/2020/10/07/transactions-in-swiftui/) post.

This week, we have learned about a new approach for building precise and
scoped animations in SwiftUI. Remember that it is available only on the latest
platforms and is not backward compatible. I hope you enjoy the post. Feel free
to follow me on [ Twitter ](https://twitter.com/mecid) and ask your questions
related to this post. Thanks for reading, and see you next week!

