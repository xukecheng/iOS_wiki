##  The many faces of button in SwiftUI

30 Jun 2021

Button is one of the crucial components of any app. We use buttons to provide
actions in the user interface of the app. SwiftUI 3 released a bunch of new
view modifiers that allow us to style buttons in different ways. New
_bordered_ and _borderedProminent_ button styles in conjunction with
_controlSize_ and _buttonBorderShape_ view modifiers can change button
presentation drastically.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

####  Button role

New in SwiftUI Release 3, you can provide an optional button role. By default,
it is _nil_ and uses a standard one, but you can set the predefined role
provided by _ButtonRole_ enum. The role can be _destructive_ or _cancel_ . In
this case, SwiftUI will set a specified button appearance. For example,
SwiftUI changes the button tint to red for destructive buttons.

    
    
    Button("Delete", role: .destructive) {
        viewModel.delete()
    }
    

![button-destructive](/public/buttons-destructive.png)

Button roles change the appearance in many places across the app, like context
menus, toolbar menus, etc.

    
    
    struct ContentView: View {
        var body: some View {
            NavigationView {
                Text("Hello, World!")
                    .toolbar {
                        Menu("Actions") {
                            Button("New action") {}
                            Button("Delete", role: .destructive) {}
                    }
                }.navigationTitle("Buttons")
            }
        }
    }
    

![button-toolbar](/public/buttons-toolbar.png)

####  Bordered button style

There is a new _BorderedButtonStyle_ type that allows us to display buttons
with rounded corners. You can set the button style for a particular button or
the full view hierarchy using the _buttonStyle_ view modifier.

    
    
    Button("New action") {}
        .buttonStyle(.bordered)
    

![button-bordered](/public/buttons-bordered.png)

_BorderedButtonStyle_ provides you a bordered button appearance with rounded
corners that you can see in many places across the iOS system.

> To learn more about buttons and how to create custom button style, take a
> look at my [ “Mastering buttons in SwiftUI” ](/2020/02/19/mastering-buttons-
> in-swiftui/) post.

####  Button tint

There is a new _tint_ view modifier that we should use to override the default
accent color. Unlike an app’s accent color, which can be overridden by user
preference, the tint color is always respected.

    
    
    Button("New action") {}
        .buttonStyle(.bordered)
        .tint(.green)
    

![button-tint](/public/buttons-bordered-tint.png)

####  Control size

We can’t directly control the corner radius of the bordered button, but we can
affect it using the _controlSize_ view modifier. The _controlSize_ view
modifier allows us to set the size of controls within the view. There is a
_ControlSize_ enum with four cases: _mini, small, regular, and large_ . We can
use one of them and pass it via the _controlSize_ modifier.

    
    
     Button("New action") {}
        .tint(.green)
        .buttonStyle(.bordered)
        .controlSize(.large)
    

![button-bordered-large](/public/buttons-bordered-large.png)

In the example above, we set the large size for controls in our view
hierarchy. As you can see, it affects the size of our button and changes its
corner radius.

####  Bordered button shape

There is a new _buttonBorderShape_ view modifier that allows us to change the
shape of bordered button in the view. _buttonBorderShape_ view modifier
accepts an instance of _ButtonBorderShape_ struct that defines the shape.
There are a few predefined options like _capsule, roundedRectangle, and
automatic_ .

    
    
    Button("New action") {}
        .tint(.green)
        .buttonStyle(.bordered)
        .buttonBorderShape(.capsule)
        .controlSize(.large)
    

![button-bordered-capsule](/public/buttons-bordered-capsule.png)

####  Button prominence

Button prominence defines the dominance of a button in the user interface. You
can increase the importance using the new _borderedProminent_ style.

    
    
    Button("New action") {}
        .tint(.green)
        .controlSize(.large)
        .buttonStyle(.borderedProminent)
    

![button-bordered-tint-important](/public/buttons-tint-fill.png)

As you can see in the example above, SwiftUI changes button appearance
whenever we set the increased prominence. SwiftUI displays buttons with
increased prominence by filling them with tint color.

####  Conclusion

There are a lot of new opportunities for customizing buttons both in SwiftUI
and UIKit. New control size and prominence APIs will play a crucial role in
styling SwiftUI buttons without implementing custom button styles. I hope you
enjoy the post. Feel free to follow me on [ Twitter
](https://twitter.com/mecid) and ask your questions related to this post.
Thanks for reading, and see you next week!

