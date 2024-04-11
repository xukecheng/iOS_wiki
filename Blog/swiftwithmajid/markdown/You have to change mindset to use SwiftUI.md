##  You have to change mindset to use SwiftUI

19 Nov 2019

Last week I saw that the community tries to move _UIKit_ development patterns
to SwiftUI. But I’m sure that the best way to write efficient SwiftUI is to
forget everything about _UIKit_ and entirely change your mindset in terms of
User Interface development. This week we will learn the main differences
between _UIKit_ and SwiftUI development.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

####  Diffing

_UIKit_ is an imperative event-driven framework for building User Interfaces
for iOS platform. It means you have to handle all the state changes during
events like view loaded, button pressed, etc. The big downside of this
approach is the complexity of keeping in sync User Interface with its state.
As soon as state changes, you need to manually add/remove/show/hide the views
and keep it in sync with the current state.

SwiftUI is a declarative framework for building User Interfaces on Apple
platforms. The keyword here is declarative. Declarative means that you need to
declare what you want to achieve, and the framework takes care of it.
Framework knows the best way to render the User Interface.

> ` UI = f(state) `

The User Interface in SwiftUI is a function of its state. It means whenever
the view’s state changes, it recomputes its **body property** and generates a
new view. Let’s take a look at a quick sample.

    
    
    struct ContentView: View {
        @ObservedObject var store: Store
    
        var body: some View {
            Group {
                if store.isLoading {
                    Text("Loading...")
                        .font(.subheadline)
                } else {
                    Image("photo")
                        .font(.largeTitle)
                }
            }
        }
    }
    

As you can see in the example above, we have a view that shows loading text
and image when the loading finishes. _ObserverObject_ here is a state of this
view, and as soon as it changes, SwiftUI recomputes the body property and
assigns a new view. In typical _UIKit_ development, we need manually to
hide/show the elements of the view hierarchy, but in SwiftUI, we don’t need to
add/remove the loading indicator.

> We have a few ways of describing a state of the view in SwiftUI, to learn
> more about them take a look at [ “Understanding Property Wrappers in
> SwiftUI” ](/2019/06/12/understanding-property-wrappers-in-swiftui/) .

Let’s take a more in-depth look at what happens when the view’s state changes.
SwiftUI has a snapshot of the current view hierarchy, and as soon as state
changes, it computes a new view. Finally, SwiftUI applies diffing algorithms
to understand differences and automatically add/remove/update needed views. By
default, SwiftUI uses standard fade in/out transition to show/hide views, but
you can manually change the transition to any animation you want.

> To learn more about transitions and animations in SwiftUI, take a look at my
> [ “Animations in SwiftUI” ](/2019/06/26/animations-in-swiftui/) post.

####  View hierarchy

Let’s talk about view hierarchy now, and how actually SwiftUI renders your
view struct. The very first thing which I want to mention that SwiftUI doesn’t
render your view struct by doing the one-to-one mapping. You can use as many
view containers as you want, but in the end, SwiftUI renders only views that
make sense. It means that you can extract you view logic into small views and
then compose and reuse them across the app. Don’t worry, performance, in this
case, won’t be affected.

The best way to understand the complex view hierarchies in SwiftUI is by
printing its type. SwiftUI uses the static type system of Swift to make
diffing so fast. First of all, it checks the type of the view, and then checks
its values of the view components. I’m not a fan of using reflections in
production code, but it is very helpful during the learning process.

    
    
    print(Mirror(reflecting: ContentView(store: .init()).body))
    // Group<_ConditionalContent<Text, ModifiedContent<Image, _EnvironmentKeyWritingModifier<Optional<Font>>>>>
    

By using _Mirror_ struct, we can print the real type of the _ContentView_ ’s
body and learn how SwiftUI works under the hood.

> To learn more how SwiftUI uses __ConditionalContent_ take a look at my [
> “Structural identity in SwiftUI” ](/2021/12/09/structural-identity-in-
> swiftui/) post.

####  Conclusion

This week we learned the main difference between _UIKit_ and SwiftUI and took
an in-depth look at the diffing algorithm in SwiftUI. I hope you enjoy the
post. Feel free to follow me on [ Twitter ](https://twitter.com/mecid) and ask
your questions related to this post. Thanks for reading, and see you next
week!

