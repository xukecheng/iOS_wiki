##  Understanding Property Wrappers in SwiftUI

12 Jun 2019

Last week we started a new series of [ posts ](/2019/06/05/swiftui-making-
real-world-app) about SwiftUI framework. Today I want to continue this topic
by covering _Property Wrappers_ provided by SwiftUI. SwiftUI gives us _@State_
, _@Binding_ , _@ObservedObject_ , _@EnvironmentObject_ , and _@Environment_
_Property Wrappers_ . So let’s try to understand the differences between them
and when and why which one we have to use.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

####  Property Wrappers

_Property Wrappers_ feature described in [ SE-0258
](https://github.com/DougGregor/swift-evolution/blob/property-
wrappers/proposals/0258-property-wrappers.md) proposal. The main goal here is
wrapping properties with logic which can be extracted into the separated
struct to reuse it across the codebase.

####  @State

_@State_ is a _Property Wrapper_ which we can use to describe _View_ ’s state.
SwiftUI will store it in special internal memory outside of _View_ struct.
Only the related _View_ can access it. As soon as the value of @ _State_
property changes SwiftUI rebuilds _View_ to respect state changes. Here is a
simple example.

    
    
    struct ProductsView: View {
        let products: [Product]
    
        @State private var showFavorited: Bool = false
    
        var body: some View {
            List {
                Button(
                    action: { self.showFavorited.toggle() },
                    label: { Text("Change filter") }
                )
    
                ForEach(products) { product in
                    if !self.showFavorited || product.isFavorited {
                        Text(product.title)
                    }
                }
            }
        }
    }
    

In the example above we have a straightforward screen with _Button_ and _List_
of products. As soon as we press the button, it changes the value of the state
property, and SwiftUI recreates _View_ .

####  @Binding

@ _Binding_ provides _reference_ like access for a **value** type. Sometimes
we need to make the state of our _View_ accessible for its children. But we
can’t simply pass that value because it is a value type and Swift will pass
the copy of that value. And this is where we can use _@Binding Property
Wrapper_ .

    
    
    struct FilterView: View {
        @Binding var showFavorited: Bool
    
        var body: some View {
            Toggle(isOn: $showFavorited) {
                Text("Change filter")
            }
        }
    }
    
    struct ProductsView: View {
        let products: [Product]
    
        @State private var showFavorited: Bool = false
    
        var body: some View {
            List {
                FilterView(showFavorited: $showFavorited)
    
                ForEach(products) { product in
                    if !self.showFavorited || product.isFavorited {
                        Text(product.title)
                    }
                }
            }
        }
    }
    

We use @ _Binding_ to mark _showFavorited_ property inside the _FilterView_ .
We also use _$_ to pass a binding reference, because without _$_ Swift will
pass a copy of the value instead of passing bindable reference. _FilterView_
can read and write the value of _ProductsView_ ’s _showFavorited_ property. As
soon as _FilterView_ changes value of _showFavorited_ property, SwiftUI will
recreate the _ProductsView_ and _FilterView_ as its child.

> @ _Binding_ provides a _reference_ like access for a ` value ` type. That’s
> why it should be used only with value types. If ` Value ` of Binding is not
> value semantic, the updating behavior for any views that make use of the
> resulting ` Binding ` is unspecified.

####  @ObservedObject

We should use @ _ObservedObject_ to handle data that lives outside of SwiftUI,
like your business logic. We can share it between multiple independent _Views_
which can subscribe and observe changes on that object, and as soon as changes
appear SwiftUI rebuilds all _Views_ bound to this object. Let’s take a look at
an example.

    
    
    import Combine
    
    final class PodcastPlayer: ObservableObject {
        @Published private(set) var isPlaying: Bool = false
    
        func play() {
            isPlaying = true
        }
    
        func pause() {
            isPlaying = false
        }
    }
    

Here we have _PodcastPlayer_ class which we share between the screens of our
app. Every screen has to show floating pause button in the case when the app
is playing a podcast episode. SwiftUI tracks the changes on _ObservableObject_
with the help of _@Published_ property wrapper, and as soon as a property
marked as _@Published_ changes SwiftUI rebuild all _Views_ bound to that
_PodcastPlayer_ object. Here we use _@ObservedObject Property Wrapper_ to bind
our _EpisodesView_ to _PodcastPlayer_ class

    
    
    struct EpisodesView: View {
        @ObservedObject var player: PodcastPlayer
        let episodes: [Episode]
    
        var body: some View {
            List {
                Button(
                    action: {
                        if self.player.isPlaying {
                            self.player.pause()
                        } else {
                            self.player.play()
                        }
                }, label: {
                        Text(player.isPlaying ? "Pause": "Play")
                    }
                )
                ForEach(episodes) { episode in
                    Text(episode.title)
                }
            }
        }
    }
    

> Remember, we can share ` ObservableObject ` between multiple views, that’s
> why it must be a ` reference type/class ` .

####  @EnvironmentObject

Instead of passing _ObservableObject_ via init method of our View we can
implicitly inject it into _Environment_ of our _View_ hierarchy. By doing
this, we create the opportunity for all child _Views_ of current _Environment_
access this _ObservableObject_ .

    
    
    class SceneDelegate: UIResponder, UIWindowSceneDelegate {
    
        var window: UIWindow?
    
        func scene(_ scene: UIScene, willConnectTo session: UISceneSession, options connectionOptions: UIScene.ConnectionOptions) {
            let window = UIWindow(frame: UIScreen.main.bounds)
            let episodes = [
                Episode(id: 1, title: "First episode"),
                Episode(id: 2, title: "Second episode")
            ]
    
            let player = PodcastPlayer()
            window.rootViewController = UIHostingController(
                rootView: EpisodesView(episodes: episodes)
                    .environmentObject(player)
            )
            self.window = window
            window.makeKeyAndVisible()
        }
    }
    
    struct EpisodesView: View {
        @EnvironmentObject var player: PodcastPlayer
        let episodes: [Episode]
    
        var body: some View {
            List {
                Button(
                    action: {
                        if self.player.isPlaying {
                            self.player.pause()
                        } else {
                            self.player.play()
                        }
                }, label: {
                        Text(player.isPlaying ? "Pause": "Play")
                    }
                )
                ForEach(episodes) { episode in
                    Text(episode.title)
                }
            }
        }
    }
    

As you can see, we can pass _PodcastPlayer_ object via _environmentObject_
modifier of our _View_ . By doing this, we can easily access _PodcastPlayer_
by defining it with _@EnvironmentObject Property Wrapper_ . @
_EnvironmentObject_ uses dynamic member lookup feature to find _PodcastPlayer_
class instance in the _Environment_ , that’s why you don’t need to pass it via
init method of _EpisodesView_ . It works like magic.

####  @Environment

As we discussed in the previous chapter, we can pass custom objects into the
_Environment_ of a _View_ hierarchy inside SwiftUI. But SwiftUI already has an
_Environment_ populated with system-wide settings. We can easily access them
with _@Environment Property Wrapper_ .

    
    
    struct CalendarView: View {
        @Environment(\.calendar) var calendar: Calendar
        @Environment(\.locale) var locale: Locale
        @Environment(\.colorScheme) var colorScheme: ColorScheme
    
        var body: some View {
            return Text(locale.identifier)
        }
    }
    

By marking our properties with _@Environment Property Wrapper_ , we access and
subscribe to changes of system-wide settings. As soon as _Locale_ , _Calendar_
or _ColorScheme_ of the system change, SwiftUI recreates our _CalendarView_ .

> To learn about new property wrappers released during WWDC20, take a look at
> my [ “New property wrappers in SwiftUI”
> ](https://swiftwithmajid.com/2020/06/29/new-property-wrappers-in-swiftui/)
> post.

####  Conclusion

Today we talked about _Property Wrappers_ provided by SwiftUI. _@State,
@Binding, @EnvironmentObject, @Environment and @ObservedObject_ play huge role
in SwiftUI development. Feel free to follow me on [ Twitter
](https://twitter.com/mecid) and ask your questions related to this post.
Thanks for reading and see you next week!

