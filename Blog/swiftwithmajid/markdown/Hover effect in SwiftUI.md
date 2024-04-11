##  Hover effect in SwiftUI

25 Mar 2020

Apple introduced the hover effect a few years ago to improve the interaction
of the trackpads on iPadOS. Later, it became available on tvOS, producing the
same effect while the user navigated through the app using Apple TV Remote.
Nowadays, we can use the hover effect in response to eye focus on visionOS.
This week, we will learn all about hover effect interaction in SwiftUI.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

####  hoverEffect view modifier

SwiftUI provides us the _hoverEffect_ modifier that we can attach to any view.
This modifier enables the transformation of eye focus or mouse pointer into
the covering view shape. It is tough to explain this transformation and better
to see. Let’s run the example on an iPad or Vision Pro simulator.

    
    
    import SwiftUI
    
    struct RootView: View {    
        var body: some View {
            Text("Hello World!")
                .hoverEffect()
        }
    }
    

Fortunately, iPad simulator supports trackpad simulation. You have to enable
it by using _I/O - > Input -> Send cursor to Device _ menu. Now we can see the
pointer on the screen. Let’s cover the text view with the pointer.

SwiftUI provides us the _HoverEffect_ struct that describes three types of
transformation of the pointer into a view shape. By default, _hoverEffect_
modifier uses the first one, which is called _automatic_ . Besides that, we
have _highlight_ and _lift_ transformations. You can use them by only passing
it as a parameter of the _hoverEffect_ modifier.

    
    
    struct RootView: View {    
        var body: some View {
            VStack {
                Text("Hello")
                    .hoverEffect(.lift)
                Text("World")
                    .hoverEffect(.highlight)
            }
        }
    }
    

Highlight transformation describes an effect that morphs the pointer into a
platter behind the view and shows a light source indicating position. On the
other hand, lift transformation defines an effect that slides the pointer
under the view and disappears as the view scales up and gains a shadow.
Usually, we need the _automatic_ transformation that attempts to determine the
effect automatically.

    
    
    struct ContentView: View {
        @State private var isEnabled = false
        
        var body: some View {
            VStack {
                Toggle(isOn: $isEnabled) {
                    Text(isEnabled ? "Disable" : "Enable")
                }
                
                Text("Hello World!")
                    .hoverEffect(.lift, isEnabled: isEnabled)
            }
        }
    }
    

As you can see in the example above, the _hoverEffect_ view modifier also
allows us to control whenever to turn the effect on or off by using the
_isEnabled_ parameter.

The only downside of the _hoverEffect_ view modifier is that you must apply it
to every view you want to enable the hover effect. You can easily forget to
add it to a particular view. Fortunately, SwiftUI provides the
_defaultHoverEffect_ view modifier, allowing us to enable selected hover
effects on every view in the hierarchy with a single line of code.

    
    
    struct ContentView: View {
        var body: some View {
            VStack {
                Text("Hello")
                Text("World")
            }
            .defaultHoverEffect(.lift)
        }
    }
    

Whenever you use the _defaultHoverEffect_ on the whole hierarchy, you can use
the _hoverEffectDisabled_ view modifier to turn off the hover effect on the
particular view.

    
    
    struct ContentView: View {
        var body: some View {
            VStack {
                Text("Hello")
                Text("World")
                    .hoverEffectDisabled(true)
            }
            .defaultHoverEffect(.lift)
        }
    }
    

####  onHover view modifier

Now we are familiar with the standard types of hover effect that SwiftUI
provides us. But what about custom effects? Happily, SwiftUI enables us to
create super custom hover effects by using _onHover_ modifier. This modifier
allows us to register a closure that will be called whenever the pointer
intersects the view. _onHover_ modifier enables all the power of animations in
SwiftUI that we can use to highlight interaction.

    
    
    struct CustomView: View {
        @State private var hovered = false
        
        var body: some View {
            Text("Hello World!")
                .scaleEffect(hovered ? 2.0 : 1.0)
                .animation(.default, value: hovered)
                .onHover { isHovered in
                    self.hovered = isHovered
                }
        }
    }
    

As you can see in the example above, we use _onHover_ modifier to register a
closure that delivers us a _Boolean_ value. This _Boolean_ value is _true_
whenever the pointer covers the view. We save the value into a state variable
and scale our view using default animation.

> To learn more about the power of animation modifier in SwiftUI, take a look
> at my [ “Animations in SwiftUI” ](/2019/06/26/animations-in-swiftui/) post.

When you build the custom view, you can use the _isHoverEffectEnabled_
environment value to understand whether to apply a custom hover effect.

    
    
    struct CustomView: View {
        @Environment(\.isHoverEffectEnabled) var isEnabled
        @State private var hovered = false
        
        var body: some View {
            Text("Hello World!")
                .scaleEffect(hovered && isEnabled ? 2.0 : 1.0)
                .animation(.default, value: hovered)
                .onHover { isHovered in
                    self.hovered = isHovered
                }
        }
    }
    

####  onContinuousHover view modifier

SwiftUI also provides the _onContinuousHover_ view modifier, allowing us to
track the hover phases. For example, you can read the hover’s location and
react whenever it changes.

    
    
    struct CustomView: View {
        @State private var scale = 1.0
        
        var body: some View {
            Text("Hello World!")
                .scaleEffect(scale)
                .animation(.default, value: scale)
                .onContinuousHover { phase in
                    switch phase {
                    case .active(let location):
                        scale = location.y / location.x
                    case .ended:
                        scale = 1
                    }
                }
        }
    }
    

####  Conclusion

I am pleased to see that hover effect expands from iPadOS and tvOS to
visionOS. Feel free to follow me on [ Twitter ](https://twitter.com/mecid) and
ask your questions related to this post. Thanks for reading, and see you next
week!

