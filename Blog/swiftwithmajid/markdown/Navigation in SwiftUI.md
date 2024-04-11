##  Navigation in SwiftUI

17 Jul 2019

This week I want to talk about _Navigation in SwiftUI_ . SwiftUI provides both
declarative and imperative ways of implementing navigation in your apps. Today
we will cover two ways of _Master-Detail_ navigation available in SwiftUI. We
will learn how use _NavigationLink_ , and how to do programmatic navigation in
SwiftUI.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

> _NavigationView_ is deprecated. Use _NavigationStack_ instead. To learn
> more, take a look at my [ “Mastering NavigationStack in SwiftUI. Navigator
> Pattern” ](/2022/06/15/mastering-navigationstack-in-swiftui-navigator-
> pattern/) post.

####  Master-Detail flow

Assume that you are working on app which shows a list of some items and you
want to move to details screen as soon as the user selects any item. For this
type of navigation, SwiftUI provides _NavigationView_ and _NavigationLink_
components. Let’s check how we can use them.

    
    
    struct MasterView: View {
        private let messages = [
            "Hello", "How are you?"
        ]
    
        var body: some View {
            NavigationView {
                List(messages, id: \.self) { message in
                    NavigationLink(destination: DetailsView(message: message)) {
                        Text(message)
                    }
                }.navigationBarTitle("Messages")
            }
        }
    }
    
    struct DetailsView: View {
        let message: String
    
        var body: some View {
            VStack {
                Text(message)
                    .font(.largeTitle)
            }
        }
    }
    

Here we have a list of messages, to make navigation possible we embed our
_List_ into a _NavigationView_ , it adds standard _NavigationBar_ on top of
our _List_ . We can also set text as a title of _NavigationBar_ by adding
_navigationBarTitle_ modifier to a _List_ . Please make sure that you add the
_navigationBarTitle_ modifier to a _List_ component, and not to a
_NavigationView_ because multiple views can share same _NavigationView_ and
every view can have a different title.

**Hidden gem: You can embed two views into NavigationView to achieve Split on
iPadOS and MacOS**

Next, we embed List rows into _NavigationLink_ , while creating
_NavigationLink_ , we have to provide a destination view. SwiftUI presents a
destination view when the user presses the _List row_ . By wrapping _List row_
into a _NavigationLink_ , SwiftUI adds trailing arrow to the view which
indicates that there is a details screen next to the view. And this is where
the real power of declarative programming comes. _List row_ starts appearing
in another way only by embedding it into _NavigationLink_ . To learn more
about environment-based appearance in SwiftUI, you can check out [ “Building
forms with SwiftUI” post ](/2019/06/19/building-forms-with-swiftui/) .

####  Programmatic navigation

Sometimes we need to check multiple conditions and after that push some view.
For this kind of situations, _NavigationLink_ provides a different way of
initialization, which binds it to some value, and as soon as you set the
tagged value to the binding, it pushes the view. Let’s take a look at the code
sample.

    
    
    import SwiftUI
    
    struct Master: View {
        @State var selection: Int? = nil
        
        var body: some View {
            NavigationView {
                VStack {
                    NavigationLink(destination: Details(), tag: 1, selection: $selection) {
                        Button("Press me") {
                            self.selection = 1
                        }
                    }
                }
            }
        }
    }
    
    struct Details: View {
        @Environment(\.presentationMode) var presentation
    
        var body: some View {
            Group {
                Text("Details")
                Button("pop back") {
                    self.presentation.wrappedValue.dismiss()
                }
            }
        }
    }
    

As you can see in the example above, we create _NavigationLink_ by passing
destination view and two additional parameters _Hashable_ tag and binding to
the _Hashable_ . As soon as the value of binding is equal to tag,
_NavigationView_ pushes _NavigationLink_ . You can programmatically pop back
by using _dismiss_ method on _EnvironmentValue_ called _presentationMode_ .

####  Conclusion

As you can see, SwiftUI provides both imperative and declarative ways of
pushing views into navigation stack by using _NavigationLink_ . Feel free to
use a way of navigation which fits best to your app requirements. Follow me on
[ Twitter ](https://twitter.com/mecid) and ask your questions related to this
post. Thanks for reading and see you next week!

