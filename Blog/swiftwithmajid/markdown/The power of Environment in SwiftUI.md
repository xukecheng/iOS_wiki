##  The power of Environment in SwiftUI

21 Aug 2019

_Environment_ is one of the unique features of SwiftUI which we didn’t have
before in _UIKit_ . Today I would like to show you all the benefits of using
_Environment_ in your apps.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

####  Environment

Let’s start with describing the idea of _Environment_ . We already discussed
it previously in [ “Understanding Property Wrappers in SwiftUI”
](/2019/06/12/understanding-property-wrappers-in-swiftui/) , but I want to
start with basics. When you create and start your very first _View_ in
SwiftUI, the framework generates _Environment_ for it. SwiftUI creates it
automatically, and we don’t need to do something.

SwiftUI uses _Environment_ to pass system-wide settings like
_ContentSizeCategory, LayoutDirection, ColorScheme, etc_ . _Environment_ also
contains app-specific stuff like _UndoManager_ and _NSManagedObjectContext_ .
Full list of the passed values you can find in [ _EnvironmentValues_ struct
documentation
](https://developer.apple.com/documentation/swiftui/environmentvalues) . Let’s
take a look at an example where we access _Environment_ values.

    
    
    struct ButtonsView: View {
        @Environment(\.sizeCategory) var sizeCategory
    
        var body: some View {
            Group {
                if sizeCategory == .accessibilityExtraExtraExtraLarge {
                    VStack {
                        buttons
                    }
                } else {
                    HStack {
                        buttons
                    }
                }
            }
        }
    }
    

By using @ _Environment property wrapper_ , we can read and subscribe on
changes for the selected value. Here we have _ButtonsView_ that reads Dynamic
Type value from _Environment_ and put buttons in _VStack_ or _HStack_
depending on the size category value. User can change Dynamic Type value in
the system settings, and as soon as it happens, SwiftUI will recreate
_ButtonsView_ to respect the changes.

Now let’s see how we can modify _Environment_ values. In SwiftUI we don’t have
separation like _Controllers_ or _Views_ . Everything is a _View_ , and
because of that, we can easily modify _Environment_ for an entire view
hierarchy of the app by adding _environment modifier_ to the root view.

    
    
    func scene(_ scene: UIScene, willConnectTo session: UISceneSession, options connectionOptions: UIScene.ConnectionOptions) {
            window = UIWindow(windowScene: scene as! UIWindowScene)
            window?.rootViewController = UIHostingController(
                rootView: RootView()
                    .environment(\.multilineTextAlignment, .center)
                    .environment(\.lineLimit, nil)
                    .environment(\.lineSpacing, 8)
            )
    
            window?.makeKeyAndVisible()
        }
    

In the example above, we made all the text in the app center-aligned with line
spacing 8pt without any line limit.

####  Environment inheritance

Every view inside SwiftUI inherits _Environment_ from its parent view by
default. But remember that you can override any values you want while creating
the child view by attaching _Environment_ modifier.

    
    
    struct RootView {
        var body: some View {
            PlayerView()
                .environment(\.layoutDirection, .leftToRight)
        }
    }
    
    struct PlayerView: View {
        var body: some View {
            HStack {
                Button("previous") {
    
                }
                Button("play") {
    
                }
                Button("next") {
    
                }
            }
        }
    }
    

We don’t need to change the order of the buttons on right-to-left locales like
Arabic. That’s why _RootView_ set layout direction to _leftToRight_ on
_PlayerView_ . It’s important to understand that this modification will apply
only to _PlayerView_ and all its child views.

####  View specific Environment values

We already covered how SwiftUI pass system-wide settings via _Environment_ ,
but this is not the end. SwiftUI uses _Environment_ to inject visible view
specific values like _isEnabled, editMode, presentationMode,
horizontalSizeClass, verticalSizeClass, etc._

    
    
    struct ModalView: View {
        @Environment(\.presentationMode) var presentation
    
        var body: some View {
            Button("dismiss") {
                self.presentation.value.dismiss()
            }
        }
    }
    

Here we use view-specific environment values to dismiss presented modal view.

####  Custom Environment keys

Now we know that SwiftUI provides us plenty of system-wide and view-specific
values via the environment. However, I have to mention that we can create a
custom environment key and push any value we want into the environment. Let’s
take a look at how we can insert custom values into the environment.

    
    
    import SwiftUI
    
    struct ItemsPerPageKey: EnvironmentKey {
        static var defaultValue: Int = 10
    }
    
    extension EnvironmentValues {
        var itemsPerPage: Int {
            get { self[ItemsPerPageKey.self] }
            set { self[ItemsPerPageKey.self] = newValue }
        }
    }
    
    struct RelatedProductsView: View {
        @Environment(\.itemsPerPage) var count
    
        let products: [Product]
    
        var body: some View {
            ForEach(products[..<count], id: \.id) { product in
                Text(product.title)
            }
        }
    }
    

In the example above, we create a custom key that represents a count of items
that can be presented on a screen. We also implement a view that uses that
environment value. You can easily pass that value to any view you want by
using the _environment modifier_ .

####  Dependency Injection via Environment

Another great use-case for _Environment_ is Dependency Injection. Every view
has its copy of the parent’s _Environment_ , and we can use it to add all
_ObservableObjects_ related to the current view.

    
    
    struct CalendarView : View {
        @EnvironmentObject var store: CalendarStore
    
        var body: some View {
            NavigationView {
                List {
                    ForEach(self.store.sleeps) { sleep in
                        NavigationLink(
                            destination: SleepDetailsView()
                                .environmentObject(SleepStore(sleep: sleep))
                        ) {
                            CalendarRow(sleep: sleep)
                        }
                    }
                }
            }.navigationBarTitle("calendar")
        }
    }
    

In the example above, we use _environmentObject_ modifier to pass an instance
of _SleepStore_ object. _SleepStore_ should conform to _ObservableObject_
protocol, which is used by SwiftUI to recreate the view during data changes.

> To learn more about _ObservableObject_ check another post [ “Making real-
> world app with SwiftUI” ](/2019/06/05/swiftui-making-real-world-app/) .

The significant benefit of using _Environment_ and not passing
_ObservableObject_ via the _init_ method of the view is the internal SwiftUI
storage. SwiftUI stores _Environment_ in the special framework memory outside
the view. It gives an implicit access to view-specific _Environment_ for all
child views.

####  Conclusion

As much as I use SwiftUI, I enjoy the concept of _Environment_ . As you can
see, it allows us to configure our app’s view hierarchy and make nice
Dependency Injection out of the box. I hope you will love _Environment_
feature of SwiftUI. Feel free to follow me on [ Twitter
](https://twitter.com/mecid) and ask your questions related to this post.
Thanks for reading and see you next week!

