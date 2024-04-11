##  The many faces of ShapeStyle in SwiftUI

17 Nov 2021

_ShapeStyle_ is the protocol that we have from the very first release of the
SwiftUI framework. _ShapeStyle_ defines a color or pattern to use when
rendering a shape. This week we will learn the many faces of _ShapeStyle_
protocol and different implementations provided by the SwiftUI framework.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

####  Colors

Usually, we don’t use the _ShapeStyle_ protocol itself. We use the many
implementations of the protocol that SwiftUI provides us. One of them is the
_Color_ struct. We can use an instance of the _Color_ struct to fill or stroke
a shape in SwiftUI. Let’s take a look at the quick example.

    
    
    struct ContentView: View {
        var body: some View {
            ZStack {
                Circle()
                    .fill(Color.yellow)
                Circle()
                    .stroke(Color.green, lineWidth: 16)
            }
            .padding(32)
        }
    }
    

![color-shape-style](/public/shapestyle.png)

We can also use a _ShapeStyle_ as a background or overlay for any view.

    
    
    struct ContentView: View {
        var body: some View {
            ZStack {
                Text("Hello, World!")
                    .background(Color.red)
            }
            .padding(32)
        }
    }
    

####  Gradients

Another implementation of the _ShapeStyle_ protocol is gradients. You can use
gradients anywhere in SwiftUI to provide an instance of the _ShapeStyle_
protocol.

    
    
    struct ContentView: View {
        var body: some View {
            ZStack {
                Circle()
                    .fill(
                        LinearGradient(
                            colors: [.green, .yellow],
                            startPoint: .top,
                            endPoint: .bottom
                        )
                    )
            }
            .padding(32)
        }
    }
    

![color-shape-style](/public/shapestyle1.png)

> To learn more about gradients, take a look at my dedicated [ “Gradient in
> SwiftUI” ](/2019/11/13/gradient-in-swiftui/) post.

####  Hierarchical

SwiftUI provides us a shape style that maps to one of the numbered content
styles. It has a few static instances: _primary, secondary, tertiary,
quaternary_ . You can use one of them whenever you need to use the
hierarchical styling of the content.

    
    
    struct ContentView: View {
        var body: some View {
            ZStack {
                Circle()
                    .fill(.quaternary)
            }
            .padding(32)
        }
    }
    

####  Selection

There is a special implementation of the _ShapeStyle_ protocol called
_SelectionShapeStyle_ that defines the platform-oriented selection styling.
You can use it whenever you need to highlight the selected state of the view.

    
    
    struct ContentView: View {
        var body: some View {
            ZStack {
                Circle()
                    .fill(SelectionShapeStyle())
            }
            .padding(32)
        }
    }
    

####  Tint

_TintShapeStyle_ is another implementation of the _ShapeStyle_ protocol that
uses the tint color. SwiftUI uses the app’s accent color by default, but you
can override it using the _tint_ view modifier.

    
    
    struct ContentView: View {
        var body: some View {
            ZStack {
                Circle()
                    .fill(TintShapeStyle())
            }
            .tint(Color.yellow)
            .padding(32)
        }
    }
    

####  Background

_BackgroundStyle_ type is the implementation of the _ShapeStyle_ protocol that
defines the background style in the current context. You can use it to adapt
both dark and light themes.

    
    
    struct ContentView: View {
        var body: some View {
            ZStack {
                Circle()
                    .fill(BackgroundStyle())
            }
            .padding(32)
        }
    }
    

####  Foreground

_ForegroundStyle_ type is similar to the _BackgroundStyle_ type but instead
defines the foreground style of the current context. This one also works both
in dark and light themes.

    
    
    struct ContentView: View {
        var body: some View {
            ZStack {
                Circle()
                    .fill(ForegroundStyle())
            }
            .padding(32)
        }
    }
    

####  Material

Materials in SwiftUI conform to the _ShapeStyle_ protocol also. It means you
can use provided materials as the instance of _ShapeStyle_ protocol anywhere
in SwiftUI.

    
    
    struct ContentView: View {
        var body: some View {
            ZStack {
                Circle()
                    .fill(Material.ultraThin)
            }
            .padding(32)
        }
    }
    

> To learn more about materials, take a look at my dedicated [ “Blur effect
> and materials in SwiftUI” ](/2021/10/28/blur-effect-and-materials-in-
> swiftui/) post.

####  ImagePaint

_ImagePaint_ type implements the _ShapeStyle_ protocol and fills a shape by
repeating a region of an image.

    
    
    struct ContentView: View {
        var body: some View {
            ZStack {
                Circle()
                    .fill(ImagePaint(image: Image(systemName: "star")))
            }
            .padding(32)
        }
    }
    

> To learn more about images in SwiftUI, take a look at my dedicated [
> “Mastering images in SwiftUI” ](/2021/11/17/the-many-faces-of-shapestyle-in-
> swiftui/) post.

####  AnyShapeStyle

The last but not least type that conforms to the _ShapeStyle_ protocol is the
_AnyShapeStyle_ type. _AnyShapeStyle_ is the type-erased implementation of the
_ShapeStyle_ protocol that allows us to pass styles without using generics.

    
    
    struct AvatarView: View {
        let style: AnyShapeStyle
    
        var body: some View {
            Circle()
                .fill(style)
        }
    }
    
    let style = AnyShapeStyle(TintShapeStyle())
    let avatarView = AvatarView(style: style)
    

####  Conclusion

Today we learned how to use the _ShapeStyle_ protocol and the many
implementations that SwiftUI provides us. I hope you enjoy the post. Feel free
to follow me on [ Twitter ](https://twitter.com/mecid) and ask your questions
related to this post. Thanks for reading, and see you next week!

