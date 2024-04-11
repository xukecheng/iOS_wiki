##  Keyboard shortcuts in SwiftUI

17 Nov 2020

This year Apple released the new App Lifecycle API for SwiftUI, which brings
tons of new modifiers to replace _AppDelegate_ callbacks. I have already
covered most of them in previous posts. This week, we will discuss the new
_keyboardShortcut_ modifier, which allows us to assign a shortcut to any
interacting view.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

SwiftUI provides us the _keyboardShortcut_ modifier that we can attach to any
view in the view hierarchy and define a keyboard shortcut. Pressing the
defined keyboard shortcut is the equivalent to direct interaction with the
view to perform its primary action. Let’s take a look at the example.

> To learn more about new App Lifecycle API, take a look at [ “Managing app in
> SwiftUI” ](/2020/08/19/managing-app-in-swiftui/) post.
    
    
    import SwiftUI
    
    struct ContentView: View {
        var body: some View {
            Button("Print message") {
                print("Hello World!")
            }.keyboardShortcut("p", modifiers: [.command, .shift])
        }
    }
    

As you can see in the example above, we assign a keyboard shortcut to the
button. We define it by using _keyboardShortcut_ modifier and passing the “p”
key equivalent and a list of modifier keys. A modifier key is an instance of
_EventModifiers_ struct that conforms to _OptionSet_ protocol and defines keys
like shift, command, control, option, etc. You can ignore the key modifier
parameter, and in this case, SwiftUI will use the command modifier by default.

> To learn more about _OptionSet_ in Swift, look at my [ “Inclusive enums with
> OptionSet” ](/2019/04/10/inclusive-enums-with-optionset/) post.

This first parameter of _keyboardShortcut_ modifier should be an instance of
_KeyEquivalent_ struct. _KeyEquivalent_ struct conforms to
_ExpressibleByExtendedGraphemeClusterLiteral_ protocol, which allows us to
create an instance of the _KeyEquivalent_ using a string literal containing
only one character. _KeyEquivalent_ also defines a few key symbols like
arrows, escape, delete, home, etc.

Remember that you have to press the “Capture Keyboard” button in the simulator
chrome to test keyboard shortcuts on a simulator.

    
    
    import SwiftUI
    
    struct ContentView: View {
        @State private var isEnabled = false
    
        var body: some View {
            Toggle(isOn: $isEnabled) {
                Text(String(isEnabled))
            }.keyboardShortcut("t")
        }
    }
    

I have to mention that _keyboardShortcut_ is a view modifier, and you can
apply it to any SwiftUI view. In the example above, we define a keyboard
shortcut on the toggle view. By pressing this shortcut, we interact with the
toggle and switch its value.

> To learn more about view modifiers, take a look at my [ “ViewModifiers in
> SwiftUI” ](/2019/08/07/viewmodifiers-in-swiftui/) post.

You can also attach the _keyboardShortcut_ modifier to any container view like
_VStack_ or _HStack_ . In this case, the shortcut will apply to the first
interactive child in the container hierarchy.

    
    
    import SwiftUI
    
    struct ContentView: View {
        @State private var isEnabled = false
    
        var body: some View {
            VStack {
                Button("Print message") {
                    print("Hello World!")
                }
                
                Button("Delete message") {
                    print("Message deleted.")
                }
            }.keyboardShortcut("p")
        }
    }
    

####  Conclusion

This week we learned about implementing keyboard shortcuts in your SwiftUI
apps. Keyboard shortcuts can improve your app user experience in a great way.
It is effortless to implement in SwiftUI, and I believe you will not waste
your time and add it as soon as possible. I hope you enjoy the post. Feel free
to follow me on [ Twitter ](https://twitter.com/mecid) and ask your questions
related to this article. Thanks for reading, and see you next week!

