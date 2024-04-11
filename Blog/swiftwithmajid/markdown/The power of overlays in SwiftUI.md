##  The power of overlays in SwiftUI

03 May 2023

An overlay is a view drawing on top of another view. And today, we will talk
about two interesting use cases of using overlays in SwiftUI. One of them
allows us to keep the structural identity of the view, and another one becomes
very handy whenever you build custom navigation transitions.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

####  Keeping structural identity with overlays

Structural identity is the type of identity that SwiftUI uses to understand
your views without an explicit identifier by using your layout description. It
is essential to keep your view hierarchy without unnecessary branches that you
may create using **if** statements in the body of a _ViewBuilder_ closure
because it may hurt the performance of your views and produce state losses.

    
    
    struct ContentView: View {
        @State private var isDownloading = false
        
        var body: some View {
            if isDownloading {
                ProgressView()
            } else {
                DownloadButton("Download") {
                    isDownloading = true
                    // start download here
                    isDownloading = false
                }
            }
        }
    }
    

In the example above, whenever the _isDownloading_ property changes, the
framework creates a new button or new progress view. In the case of our custom
button, it completely loses its state because SwiftUI makes a new one. This
behavior can be unexpected in different scenarios, so avoid branching using
**if** statements in _ViewBuilder_ closures as much as possible.

> To learn more about structural identity in SwiftUI, take a look at my
> dedicated [ “Structural identity in SwiftUI” ](/2021/12/09/structural-
> identity-in-swiftui/) post.

Instead of branching via **if** statements, we can use overlays to keep the
structural identity of the view.

    
    
    struct ContentView: View {
        @State private var isDownloading = false
        
        var body: some View {
            DownloadButton() {
                isDownloading = true
                // start download here
                isDownloading = false
            }
            .disabled(isDownloading)
            .overlay {
                if isDownloading {
                    ProgressView()
                }
            }
        }
    }
    

As you can see in the example above, we use the _overlay_ view modifier to
display the progress view on the top button and disable it by using one of the
inert view modifiers. SwiftUI will never create a new button in this case.

####  Custom transitions with overlays

From the very first day, the SwiftUI framework shows us how easily we can
animate changes in the view hierarchy. Working with SwiftUI to build fluid
animations is super easy. The only downside I can find is the custom
navigation transitions. Unfortunately, there is no way to customize navigation
transitions inside the _NavigationView_ or _NavigationStack_ .

One of the powerful animation tools of the SwiftUI framework, the
_matchedGeomerty_ view modifier, doesn’t support _NavigationView_ and
_NavigationStack_ at the very moment. Fortunately, we can use overlay view
modifiers to build custom navigation transitions without using
_NavigationView_ or _NavigationStack_ .

    
    
    struct ContentView: View {
        @State private var selectedImage: String?
        @Namespace private var hero
    
        let images: [String] = [
            "pencil",
            "trash",
            "lock.doc",
            "person",
            "figure.run"
        ]
    
        var body: some View {
            NavigationStack {
                LazyVGrid(columns: Array(repeating: .init(.flexible()), count: 3)) {
                    ForEach(images, id: \.self) { image in
                        Image(systemName: selectedImage == image ? "" : image)
                            .resizable()
                            .scaledToFit()
                            .background(Material.regular)
                            .matchedGeometryEffect(id: image, in: hero)
                            .onTapGesture {
                                selectedImage = image
                            }
                    }
                }
                .overlay {
                    if let image = selectedImage {
                        Image(systemName: image)
                            .resizable()
                            .scaledToFill()
                            .background(Material.thin)
                            .matchedGeometryEffect(id: image, in: hero)
                            .animation(.easeInOut, value: selectedImage)
                            .onTapGesture {
                                selectedImage = nil
                            }
                    }
                }
            }
            .animation(.default, value: selectedImage)
        }
    }
    

Here is another example where the overlay trick shines. Instead of
_NavigationLink_ , we pair the overlay view modifier with the
_matchedGeomerty_ view modifier. We show the overlay with the matched geometry
animation only when the user makes a selection.

This pair allows us to build super custom navigation transitions like hero
animation. Yes, it adds some work to maintain the navigation state, but it
will enable us to provide an excellent user experience in our apps.

> To learn more about the matchedGeometry view modifier, take a look at my [
> “Hero animations in SwiftUI” ](/2020/12/17/hero-animations-in-swiftui/)
> post.

Today we learned how valuable is the _overlay_ view modifier in SwiftUI, and
with the latest addition allowing us to build overlays by using the
_ViewBuilder_ closure, it became effortless. I hope you enjoy the post. Feel
free to follow me on [ Twitter ](https://twitter.com/mecid) and ask your
questions related to this post. Thanks for reading, and see you next week!

