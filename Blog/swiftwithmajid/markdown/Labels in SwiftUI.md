##  Labels in SwiftUI

23 Dec 2020

We often underestimate the power of simple things. The same feelings I had
during the first usage of _Label_ view in SwiftUI. It looks straightforward,
but it hides many use cases where it works great. Today we will talk about the
_Label_ view and its customization capabilities.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

####  Basics

_Label_ is a standard component for user interface items, consisting of an
icon with a title. One of the most common and recognizable user interface
components is the combination of an icon and a label. Let’s take a look at how
easily we can use it in code.

    
    
    struct ContentView: View {
        var body: some View {
            // SF Symbol
            Label("Heart Rate", systemImage: "heart.fill")
            
            // Image from app bundle
            Label("ECG", image: "ecg")
        }
    }
    

![label](/public/label.png)

As you can see, we create a label by passing two parameters to the
initializer. The first one is a title that we can pass as a plain string or
_LocalizedStringKey_ . The second one is an image, a system image from the SF
Symbols collection, or your custom image from the app bundle.

> To learn more about _LocalizedStringKey_ , take a look at [ “Localization in
> SwiftUI” ](/2019/10/16/localization-in-swiftui/) post.

Another initializer overload allows you to define a label using two
_@ViewBuilder_ closures to build the _Label_ view.

    
    
    struct ContentView: View {
        var body: some View {
            Label {
                Text("Hello")
            } icon: {
                Image(systemName: "heart")
            }
        }
    }
    

The main thing that I love about the _Label_ view is how it deals with
accessibility. It combines both image and title in a single accessibility
element and uses the title as an accessibility label for the whole view. This
is usually what we want to achieve while using a stack with an image and text
describing that image.

> To learn more about accessibility labels and VoiceOver, take a look at my [
> “Accessibility in SwiftUI” ](/2019/09/10/accessibility-in-swiftui/) post.

####  Styling

SwiftUI provides us _LabelStyle_ protocol to implement different styling
options for our labels. There are already three style options coming with
SwiftUI out of the box. You might be already familiar with style protocols in
SwiftUI, as I already covered it on my blog a few times.

SwiftUI gives us _DefaultLabelStyle_ , _IconOnlyLabelStyle_ and
_TitleOnlyLabelStyle_ style options to use out of the box. The default one is
_DefaultLabelStyle_ that shows both title and image. _IconOnlyLabelStyle_
shows only the image, and _TitleOnlyLabelStyle_ shows the title only.

    
    
    struct ContentView: View {
        var body: some View {
            Label("Heart Rate", systemImage: "heart.fill")
                .labelStyle(IconOnlyLabelStyle())
            Label("ECG", image: "ecg")
                .labelStyle(TitleOnlyLabelStyle())
        }
    }
    

The great thing about style protocols is that you can create your own
implementation and place the items the way you need. Let’s try to build
another style that will place the icon and title in a horizontal or vertical
stack depending on the current accessibility category.

    
    
    struct AccessibleLabelStyle: LabelStyle {
        @Environment(\.sizeCategory) var sizeCategory
    
        @ViewBuilder
        func makeBody(configuration: Configuration) -> some View {
            if sizeCategory.isAccessibilityCategory {
                VStack {
                    configuration.icon
                    configuration.title
                }
            } else {
                HStack {
                    configuration.icon
                    configuration.title
                }
            }
        }
    }
    
    struct ContentView: View {
        var body: some View {
            Button(action: {}) {
                Label("Heart Rate", systemImage: "heart.fill")
            }.labelStyle(AccessibleLabelStyle())
        }
    }
    

As you can see in the example above, we create a custom label style called
_AccessibleLabelStyle_ . It uses the environment to read the size category and
layout items appropriately. We use _labelStyle_ modifier to set and share the
style for labels using the environment.

> To learn more about sharing styles using the environment, take a look at my
> [ “Styling custom SwiftUI views using environment” ](/2020/12/09/styling-
> custom-swiftui-views-using-environment/) post.

####  Conclusion

Today we learned about another great SwiftUI view that provides us a lot of
ways for customization and styling. I hope you enjoy the post. Feel free to
follow me on [ Twitter ](https://twitter.com/mecid) and ask your questions
related to this article. Thanks for reading, and see you next week!

