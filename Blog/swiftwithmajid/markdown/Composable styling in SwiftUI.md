##  Composable styling in SwiftUI

28 Aug 2019

This week I want to talk about the styling of views in SwiftUI. SwiftUI
provides a pretty composable architecture for building your apps. Every screen
in terms of SwiftUI is a function on some data which returns a view. So let’s
talk today about composable and highly reusable styling options which we have
in SwiftUI.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

####  Branding

Whenever I begin a project, I start with defining my brand color for my User
Interface. I use brand color as a tint for my buttons, switches, slider, etc.
We can easily set the tint color on every view in the app by using
_accentColor_ modifier on the root view. Here is a quick example.

    
    
    func scene(_ scene: UIScene, willConnectTo session: UISceneSession, options connectionOptions: UIScene.ConnectionOptions) {
            window = UIWindow(windowScene: scene as! UIWindowScene)
            window?.rootViewController = UIHostingController(
                rootView: RootView()
                    .accentColor(.purple)
            )
    
            window?.makeKeyAndVisible()
        }
    

SwiftUI uses _Environment_ feature to pass the values implicitly inside any
child view. This is how we can give an accent color to every view across the
app. To learn more about _Environment_ feature of SwiftUI, check my dedicated
post [ “The power of Environment in SwiftUI” ](/2019/08/21/the-power-of-
environment-in-swiftui/) .

Another must-have option which I want to enable on every view in my app is
line limit. I want to make every text in my app multi-lined in the case when
it is too long. I also need it when a user enables extra large font size for
Dynamic Type. It is also straightforward to achieve by adding _lineLimit_
modifier to my root view.

    
    
        func scene(_ scene: UIScene, willConnectTo session: UISceneSession, options connectionOptions: UIScene.ConnectionOptions) {
            window = UIWindow(windowScene: scene as! UIWindowScene)
            window?.rootViewController = UIHostingController(
                rootView: RootView()
                    .accentColor(.purple)
                    .lineLimit(nil)
            )
    
            window?.makeKeyAndVisible()
        }
    

####  Button styles

I often have a few button types which I reuse across the app. Before SwiftUI,
I was using inheritance to apply my styling to _UIButtons_ in _UIKit_ . But
SwiftUI relies on composition instead of inheritance, that’s why it provides
us _ButtonStyle_ protocol which we can implement to reuse our button styles
across the app.

    
    
    import SwiftUI
    
    struct OutlineStyle: ButtonStyle {
        func makeBody(configuration: Configuration) -> some View {
            configuration.label
                .frame(minWidth: 44, minHeight: 44)
                .padding(.horizontal)
                .foregroundColor(Color.accentColor)
                .background(RoundedRectangle(cornerRadius: 8).stroke(Color.accentColor))
        }
    }
    
    struct FillStyle: ButtonStyle {
        func makeBody(configuration: Configuration) -> some View {
            configuration.label
                .frame(minWidth: 44, minHeight: 44)
                .padding(.horizontal)
                .foregroundColor(configuration.isPressed ? .gray : .white)
                .background(Color.accentColor)
                .cornerRadius(8)
        }
    }
    

As you can see in the example above, we implement two button styles:
_OutlinedButton_ and _FilledButton_ . To apply them to a button in SwiftUI, we
have to use button style modifier. Let’s see how we can use them.

    
    
    HStack {
        store.monthly.map { product in
            Button("\(product.localizedPrice) / \(product.localizedPeriod)") {
                self.store.buyProduct(product)
                self.presentation.wrappedValue.dismiss()
            }.buttonStyle(OutlineStyle())
        }
    
        store.annually.map { product in
            Button("\(product.localizedPrice) / \(product.localizedPeriod)") {
                self.store.buyProduct(product)
                self.presentation.wrappedValue.dismiss()
            }.buttonStyle(FillStyle())
        }
    }.padding()
    

**I want to note that you can use _buttonStyle_ modifier on any view in
SwiftUI and it utilizes _Environment_ feature to share the style with any
button inside it. **

####  Text styles

Similar to buttons, I have a few different styling options for my text
representation. Unfortunately, SwiftUI doesn’t provide something like
_TextStyle_ protocol. But instead, it gives us a much more powerful
composition concept, and it is _ViewModifier_ . Let’s take a look at how we
can use _ViewModifiers_ to style our Text views.

    
    
    struct TitleStyle: ViewModifier {
        func body(content: Content) -> some View {
            content
                .font(.title)
                .lineSpacing(8)
                .foregroundColor(.primary)
        }
    }
    
    struct ContentStyle: ViewModifier {
        func body(content: Content) -> some View {
            content
                .font(.body)
                .lineSpacing(4)
                .foregroundColor(.secondary)
        }
    }
    
    extension Text {
        func textStyle<Style: ViewModifier>(_ style: Style) -> some View {
            ModifiedContent(content: self, modifier: style)
        }
    }
    

In the example above, we implement two style modifiers. We also provide an
extension for _Text_ component, which allows us easily apply any modifier to a
_Text_ . Now we can use our styles by adding _textStyle_ modifier to any
_Text_ component.

    
    
    VStack {
        Text("title")
            .textStyle(TitleStyle())
        Text("content")
            .textStyle(ContentStyle())
    }
    

_ViewModifiers_ allow us to encapsulate and reuse any logic across the _Views_
. To learn more about _ViewModifiers_ , take a look at my dedicated post [
“ViewModifiers in SwiftUI” ](/2019/08/07/viewmodifiers-in-swiftui/) .

####  Conclusion

Today we learned how to create highly reusable styling components for SwiftUI
by using features like _ViewModifiers_ and _Environment_ . I hope you enjoy
the post. Feel free to follow me on [ Twitter ](https://twitter.com/mecid) and
ask your questions related to this post. Thanks for reading and see you next
week!

