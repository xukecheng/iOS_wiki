##  Mastering Preview macro in Swift

17 Oct 2023

Xcode Preview Canvas is a crucial part of my development experience. Previews
have significant changes this year by introducing the new **#Preview** macro.
This week, we will learn about using the new **#Preview** macro and the
benefits of this approach.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

The new **#Preview** macro is super easy to use. Let’s take a look at the
first example.

    
    
    #Preview {
        ContentView()
            .preferredColorScheme(.dark)
    }
    

As you can see in the example above, all you need to do is embed your SwiftUI
view into the _#Preview_ macro. That’s it. And let me tell you that it works
not only with SwiftUI views. You can embed any instance of _UIViewController_
or _UIView_ .

    
    
    #Preview {
        SearchViewController()
    }
    

> To learn more about Xcode Preview Canvas, take a look at my [ “Mastering
> SwiftUI previews” ](/2021/03/10/mastering-swiftui-previews/) post.

You may want to have a set of previews displaying different states of your
view. In this case, you can put as many _#Preview_ macros as you want to
display more than one preview.

    
    
    #Preview {
        ItemsView(data: .empty)
    }
    
    #Preview {
        ItemsView(data: .error)
    }
    

Whenever you have more than one preview, you should give them different titles
to differentiate them in the preview canvas. You can easily do that by passing
a title as a parameter of the _#Preview_ macro.

    
    
    #Preview("Empty state") {
        ItemsView(data: .empty)
    }
    
    #Preview("Error state") {
        ItemsView(data: .error)
    }
    

The _#Preview_ macro has the _traits_ parameter, allowing us to display your
preview in landscape or a particular size. This version of the _#Preview_
macro is not working on previous versions and requires an availability
attribute.

    
    
    @available(iOS 17, *)
    #Preview(traits: .landscapeLeft) {
        ContentView()
    }
    
    @available(iOS 17, *)
    #Preview(traits: .fixedLayout(width: 300, height: 300)) {
        ContentView()
    }
    

Another option is to use the _#Preview_ macro with widgets to provide a
timeline provider and display an interactive widget timeline.

    
    
    #Preview(as: .accessoryRectangular) {
        SugarBotWidget()
    } timeline: {
        RawValuesProvider()
    }
    

Today, we learned how to use the new _#Preview_ macro to improve our
development experience. Remember that you can create a Swift file containing
only previews for your design system package or an example case displaying how
to use your custom view.

I hope you enjoy the post. Feel free to follow me on [ Twitter
](https://twitter.com/mecid) and ask your questions related to this post.
Thanks for reading, and see you next week!

