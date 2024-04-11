##  Focus management in SwiftUI

02 Dec 2020

WWDC 20 brings us tons of new SwiftUI APIs, which we can use to improve our
apps user experience without using UIKit. One of these new APIs was the focus
management API that we can use on iOS, macOS, tvOS, and watchOS. This week we
will talk about SwiftUI functionality that allows us to manage the focus in
our apps.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

####  Basics

Focus indicates the act of selecting an element of a graphical user interface.
On Apple TV, people use the remote to interact indirectly with onscreen
elements. This interaction is based on a focus model. By pressing buttons and
using gestures on the remote, people move the focus from element to element,
stop on a specific one, and click to access content or initiate action.

You can easily make any view focusable by using the _focusable_ modifier.
Remember that you don’t need to use it with already focusable views like
_List_ and _Button_ . Let’s take a look at how we can use this modifier in
code.

    
    
    struct ContentView: View {
        var body: some View {
            ScrollView(.horizontal) {
                LazyHStack {
                    ForEach(0..<100) { index in
                        PosterView()
                            .focusable(true, interactions: .automatic)
                    }
                }
            }
        }
    }
    

As you can see in the example above, we use the _focusable_ modifier to enable
focusing abilities on _PosterView_ . _Focusable_ modifier accepts two
parameters. The first one is the bool value that indicates whenever the view
is focusable or not. The second one is an instance of the _FocusInteractions_
type indicating the focus interaction type, like _activate_ , _edit_ or
_automatic_ . This modifier is available on all Apple platforms.

Another thing that SwiftUI provides us to handle the focused state in our
views is environment value, which allows us to recognize if the view’s nearest
focusable ancestor has focus.

    
    
    struct PosterView: View {
        @Environment(\.isFocused) var isFocused
    
        var body: some View {
            RoundedRectangle(cornerRadius: 8)
                .frame(width: 100, height: 150)
                .scaleEffect(isFocused ? 1.2 : 1)
                .animation(.easeInOut, value: isFocused)
        }
    }
    
    struct ContentView: View {
        var body: some View {
            ScrollView(.horizontal) {
                LazyHStack {
                    ForEach(0..<100) { index in
                        ZStack {
                            PosterView()
                        }
                        .focusable()
                    }
                }
            }
        }
    }
    

In this example, we use the _isFocused_ environment value to understand
whenever our parent _ZStack_ is focused. The view itself doesn’t have to be
focusable because this environment value checks if the view is within the
focused view.

    
    
    struct MyCustomButton: View {
        @Environment(\.isFocused) private var isFocused
        
        var body: some View {
            Button("Some title") {
                // action
            }
            .focusEffectDisabled()
            .border(isFocused ? .red: .clear)
        }
    }
    

You can also disable the default focus effect by using the
_focusEffectDisabled_ view modifier and apply your own customizations by
tracking _isFocused_ environment value.

> SwiftUI uses environment to pass system-wide and application-related
> information. To learn more about environment, take a look at my [ “The power
> of Environment in SwiftUI” ](/2019/08/21/the-power-of-environment-in-
> swiftui/) post.

####  Focus on watchOS and tvOS

We already talked about the APIs available on most Apple platforms, but there
is much more new stuff. There is a bunch of new APIs that we can use only on
watchOS and tvOS. For example, we can define focus entry points for our views
on watchOS and tvOS. Assume that you are working on the login screen. You want
to focus on text fields as soon as the view appears. Let’s take a look at how
we can achieve this behavior with SwiftUI.

    
    
    struct LoginView: View {
        @State private var email = ""
        @State private var password = ""
    
        @State private var hasFilledCredentials = false
        @Namespace private var namespace
    
        @Environment(\.resetFocus) var resetFocus
    
        var body: some View {
            VStack {
                TextField("email", text: $email)
                    .prefersDefaultFocus(!hasFilledCredentials, in: namespace)
    
                SecureField("password", text: $password)
    
                Button("login") {}
                    .prefersDefaultFocus(hasFilledCredentials, in: namespace)
    
                Button("reset credentials") {
                    hasFilledCredentials = false
                    resetFocus(in: namespace)
                }
            }
            .focusScope(namespace)
        }
    }
    

As you can see, SwiftUI provides us a special _prefersDefaultFocus_ modifier
that allows us to define a preferred focus area in our view. Let’s take a
deeper look at how this modifier works. It accepts two parameters. The first
one is bool value describing whenever this view should be preferred as the
default focus area. The second one is the _namespace_ , defined by its
ancestor view and indicates the focus scope. Default focus preference is
limited to its _namespace_ . It allows you to define multiple scopes and
define different focus entry points in a single view hierarchy.

> To learn more about new property wrappers, take a look at my [ “New property
> wrappers in SwiftUI” ](/2020/06/29/new-property-wrappers-in-swiftui/) post.

There is also the _resetFocus_ environment action, which we can use to reset a
focus to its preferred default position when needed.

####  Conclusion

I really like how Apple transforms imperative UIKit APIs into the declarative
world of SwiftUI. I am still not sure why Apple doesn’t make all of these new
APIs available for all platforms, but I believe we will see them on iOS also.
I hope you enjoy the post. Feel free to follow me on [ Twitter
](https://twitter.com/mecid) and ask your questions related to this article.
Thanks for reading, and see you next week!
