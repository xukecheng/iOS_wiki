##  Accessibility focus in SwiftUI

23 Sep 2021

One of the new features of SwiftUI Release 3 is accessibility focus
management. SwiftUI allows us easily handle the focus state for assistive
technologies like VoiceOver and Switch Control. This week we will learn how to
use the _AccessibilityFocusState_ property wrapper to move the accessibility
focus in SwiftUI.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

SwiftUI Release 3 provides us a particular set of tools for managing
accessibility focus. It includes the _AccessibilityFocusState_ property
wrapper and the _accessibilityFocused_ view modifier. We can handle
accessibility focus in a similar way that we manage it without assistive
technologies.

> To learn more about focus management in SwiftUI, take a look at my [
> “Mastering FocusState property wrapper in SwiftUI” ](/2021/08/24/mastering-
> focusstate-property-wrapper-in-swiftui/) post.
    
    
    import SwiftUI
    
    struct SignInView: View {
        @AccessibilityFocusState
        private var isEmailFocused: Bool
    
        @State private var email = ""
    
        var body: some View {
            NavigationView {
                Form {
                    TextField("email", text: $email, prompt: Text("email"))
                        .accessibilityFocused($isEmailFocused)
                }
                .navigationTitle("Sign in")
                .onChange(of: isEmailFocused) { newValue in
                    print(newValue)
                }
            }
        }
    }
    

As you can see in the example above, we use the _AccessibilityFocusState_
property wrapper to define a variable that represents whenever the email field
is focused. SwiftUI initializes the variable with the false value by default
because the user can focus on any other area of the screen. We also use the
_accessibilityFocused_ view modifier to bind the focus state of a particular
view to a variable holding its value.

Remember that you can declare as many variables as you need to cover your
accessibility focus logic with the _AccessibilityFocusState_ property wrapper.

    
    
    import SwiftUI
    
    struct SignInView: View {
        @AccessibilityFocusState
        private var isEmailFocused: Bool
        
        @AccessibilityFocusState
        private var isPasswordFocused: Bool
    
        @State private var email = ""
        @State private var password = ""
    
        var body: some View {
            NavigationView {
                Form {
                    TextField("email", text: $email, prompt: Text("email"))
                        .accessibilityFocused($isEmailFocused)
                    SecureField("password", text: $password, prompt: Text("password"))
                        .accessibilityFocused($isPasswordFocused)
                }
                .navigationTitle("Sign in")
            }
        }
    }
    

The nice thing about the _AccessibilityFocusState_ property wrapper is that
you can limit its behavior to a dedicated assistive technology. For example,
you can activate the _AccessibilityFocusState_ property wrapper only for
VoiceOver or Switch Control. By default, SwiftUI aggregates the value for all
assistive technologies available on the device.

    
    
    import SwiftUI
    
    struct SignInView: View {
        @AccessibilityFocusState(for: .switchControl)
        private var isEmailFocused: Bool
    
        @State private var email = ""
    
        var body: some View {
            NavigationView {
                Form {
                    TextField("email", text: $email, prompt: Text("email"))
                        .accessibilityFocused($isEmailFocused)
                }
                .navigationTitle("Sign in")
                .onChange(of: isEmailFocused) { newValue in
                    print(newValue)
                }
            }
        }
    }
    

Usually, you have more than one element on the screen, and you might want to
move the focus between them. For this particular case, SwiftUI provides us a
way to define our focusable fields via enum and switch between them.

    
    
    enum FocusableField: Hashable {
        case email
        case password
    }
    
    struct ContentView: View {
        @State private var email = ""
        @State private var password = ""
        
        @AccessibilityFocusState
        private var focus: FocusableField?
    
        var body: some View {
            NavigationView {
                Form {
                    TextField("email", text: $email, prompt: Text("email"))
                        .accessibilityFocused($focus, equals: .email)
                    SecureField("password", text: $password, prompt: Text("password"))
                        .accessibilityFocused($focus, equals: .password)
                    Button("login", action: login)
                }
                .toolbar {
                    ToolbarItem(placement: .keyboard) {
                        Button("next") {
                            if email.isEmpty {
                                focus = .email
                            } else if password.isEmpty {
                                focus = .password
                            } else {
                                focus = nil
                            }
                        }
                    }
                }
                .navigationTitle("Sign in")
                .onAppear {
                    DispatchQueue.main.asyncAfter(deadline: .now() + 0.1) {
                        focus = .email
                    }
                }
            }
        }
    
        private func login() {
            // your logic here
        }
    }
    

In the example above, we use the _AccessibilityFocusState_ view modifier with
our new _FocusableField_ enum that defines all the focusable views on the
screen. Keep in mind that you should make the _FocusableField_ enum hashable
and define an optional variable with the help of the _AccessibilityFocusState_
view modifier to allow the framework to set the value to **nil** whenever the
user moves the focus from the views you define.

We should also use another version of the _accessibilityFocused_ view modifier
to bind a view to a particular case of the hashable enum. Remember that you
can programmatically move the focus of VoiceOver or Switch Control by changing
the value of the variable wrapped with _AccessibilityFocusState_ .

> To learn about the basics of accessibility in SwiftUI, take a look at my [
> “Accessibility in SwiftUI” ](/2019/09/10/accessibility-in-swiftui/) post.

I love SwiftUI because the different APIs use the same style and they are
consistent across various features. You can learn it once and apply it in
multiple places. This week we learned how to manage the accessibility focus
which is very similar to the first responder management. I hope you enjoy the
post. Feel free to follow me on [ Twitter ](https://twitter.com/mecid) and ask
your questions related to this post. Thanks for reading, and see you next
week!

