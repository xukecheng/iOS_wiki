##  SF Symbols in SwiftUI

21 Dec 2021

Apple provides us with a set of different icons available across all the
platforms called SF Symbols. SF Symbols package contains more than 3200 icons
that we can use to visualize different states and actions in our apps. This
week we will learn how to utilize the power of SF Symbols in SwiftUI views.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

####  Basics

You can easily display an SF Symbols in SwiftUI by using a particular
initializer of the _Image_ struct. Let’s take a look at a few quick examples.

    
    
    Image(systemName: "doc.on.doc")
    

![sf-symbol](/public/sf1.png)

As you can see in the example above, we define an image with a system name.
SwiftUI uses the _systemName_ parameter for SF Symbol lookup. Keep in mind
that you can use string interpolation to show an SF Symbol as the part of any
text.

    
    
    Text("Super star \(Image(systemName: "star"))")
    

![sf-symbol](/public/sf2.png)

Another SwiftUI view that plays well with SF Symbols is _Label_ . The _Label_
view contains both text and an image and shows them according to the current
context. For example, it hides the text and shows only the image in a toolbar.

    
    
    Button(role: .destructive, action: {}) {
        Label("Remove", systemImage: "trash")
    }
    

![sf-symbol](/public/sf3.png)

> To learn more about the power of the _Label_ view, take a look at my
> dedicated [ “Labels in SwiftUI” ](/2020/12/23/labels-in-swiftui/) post.

####  Styling options

You can easily change the color of an SF Symbol using the _foregroundStyle_ or
_foregroundColor_ view modifiers.

    
    
    VStack(spacing: 8) {
        Image(systemName: "doc.on.doc")
            .foregroundColor(.green)
    
        Text("Super star \(Image(systemName: "star"))")
            .foregroundStyle(.secondary)
    }
    

There are two ways of changing the size of an SF Symbol in SwiftUI view.
First, you can apply the _font_ view modifier to keep the text and the image
size in sync with the selected Dynamic Type category.

    
    
    Button(role: .destructive, action: {}) {
        Label("Remove", systemImage: "trash")
    }
    .font(.title3)
    

Another option is the _imageScale_ view modifier that doesn’t affect the size
of the text and only changes the size of the SF Symbol relatively.

    
    
    Button(role: .destructive, action: {}) {
        Label("Remove", systemImage: "trash")
    }
    .imageScale(.large)
    

####  Variants

SF Symbols package provides us with icons in many different variants. For
example, the trash icon comes with filled, circled, squared, and slashed
versions. You can define the variant you need by providing the dedicated
symbol name.

    
    
    Image(systemName: "doc.on.doc.fill")
    

SwiftUI views are smart enough to display the variant they need without the
concrete name. For example, tab bars use the filled version of SF Symbols, and
you don’t need to specify it manually. SwiftUI picks up the correct version of
the SF Symbol automatically.

    
    
    struct ContentView: View {
        var body: some View {
            TabView {
                Text("Hello")
                    .tabItem {
                        Image(systemName: "trash")
                    }
            }
        }
    }
    

SwiftUI also provides the _symbolVariant_ view modifier that sets the
particular variant in the environment and forces it to use in the view
hierarchy.

    
    
    VStack(spacing: 8) {
        Image(systemName: "doc.on.doc")
            .foregroundColor(.green)
    
        Text("Super star \(Image(systemName: "star"))")
            .foregroundStyle(.secondary)
    
        Button(role: .destructive, action: {}) {
            Label("Remove", systemImage: "trash")
        }
        .imageScale(.large)
    }
    .symbolVariant(.fill)
    

> To learn more about environment in SwiftUI, take a look at my [ “The power
> of Environment in SwiftUI” ](/2019/08/21/the-power-of-environment-in-
> swiftui/) post.

####  Rendering mode

SF Symbols support four rendering modes that allow you to customize the way
SwiftUI colors them. Let’s take a look at them.

  1. _Monochrome_ : A mode that renders symbols as a single layer filled with color. 
  2. _Multicolor_ : This method generates symbols as multiple layers with their inherited styles. 
  3. _Hierarchical_ : A mode renders symbols as various layers, with different opacities applied to the foreground style. 
  4. _Palette_ : A way that renders symbols as numerous layers, with different styles used as the layers. 

You can use the _symbolRenderingMode_ view modifier to set a particular
rendering mode in the environment and apply it across the view hierarchy.

    
    
    struct ContentView: View {
        var body: some View {
            VStack(spacing: 8) {
                Image(systemName: "doc.on.doc.fill")
                    .foregroundColor(.green)
    
                Text("Super star \(Image(systemName: "star"))")
                    .foregroundStyle(.secondary)
    
                Button(role: .destructive, action: {}) {
                    Label("Remove", systemImage: "trash")
                }
                .imageScale(.large)
            }
            .symbolVariant(.fill)
            .symbolRenderingMode(.hierarchical)
        }
    }
    

SwiftUI allows us to set the foreground styles for different layers inside the
SF Symbol in _palette_ mode by using the _foregroundStyle_ view modifier with
multiple levels.

    
    
    struct ContentView: View {
        var body: some View {
           Image(systemName: "doc.on.doc")
                .symbolRenderingMode(.palette)
                .foregroundStyle(.red, .green, .blue)
        }
    }
    

####  Conclusion

It became straightforward to build friendly apps with a well-crafted set of
icons using SF Symbols. Moreover, SwiftUI provides a few ways of customizing
these icons by using dedicated view modifiers that we have learned today. I
hope you enjoy the post. Feel free to follow me on [ Twitter
](https://twitter.com/mecid) and ask your questions related to this post.
Thanks for reading, and see you next week!

