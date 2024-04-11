##  PhotosPicker in SwiftUI

25 Apr 2023

Nowadays, many frameworks Xcode provides us contain SwiftUI views, including
the PhotosUI framework. The PhotosUI framework provides the _PhotosPicker_
button, allowing us to offer photo-picking functionality in our apps quickly.
This week we will learn how to use the _PhotosPicker_ view in SwiftUI.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

The _PhotosPicker_ view is a simple SwiftUI button handling the photo-picking
experience for us for free. It is straightforward to use and provides a nice
API. Let’s take a look at a simple example.

    
    
    struct ContentView: View {
        @State private var selectedPhoto: PhotosPickerItem?
        @State private var image: Image?
        
        var body: some View {
            NavigationStack {
                ZStack {
                    image?
                        .resizable()
                        .scaledToFit()
                }
                .toolbar {
                    PhotosPicker(selection: $selectedPhoto) {
                        Image(systemName: "pencil")
                    }
                }
            }
        }
    }
    

First, we must import the PhotosUI framework to use the _PhotosPicker_ view.
As you can see in the example above, we use an instance of the _PhotosPicker_
view in the toolbar. The _PhotosPicker_ button has only one required
parameter: the selection binding. It should be binding to the
_PhotosPickerItem_ type.

    
    
    struct ContentView: View {
        @State private var selectedPhoto: PhotosPickerItem?
        @State private var image: Image?
        
        var body: some View {
            NavigationStack {
                ZStack {
                    image?
                        .resizable()
                        .scaledToFit()
                }
                .toolbar {
                    PhotosPicker(
                        selection: $selectedPhoto,
                        matching: .images
                    ) {
                        Image(systemName: "pencil")
                    }
                }
            }
        }
    }
    

We can also limit the type of the photos user allowed to pick by using the
_matching_ parameter, an instance of the _PHPickerFilter_ type. The
_PHPickerFilter_ provides predefined filters like images, screenshots, live
photos, etc. You can also combine filters by using _any_ , _all_ , and _not_
functions.

    
    
    struct ContentView: View {
        @State private var selectedPhoto: PhotosPickerItem?
        @State private var image: Image?
        
        var body: some View {
            NavigationStack {
                ZStack {
                    image?
                        .resizable()
                        .scaledToFit()
                }
                .toolbar {
                    PhotosPicker(
                        selection: $selectedPhoto,
                        matching: .all(of: [.screenshots, .panoramas])
                    ) {
                        Image(systemName: "pencil")
                    }
                }
            }
        }
    }
    

Remember, you can pick not only images but also video content by using the
_PhotosPicker_ view.

    
    
    struct ContentView: View {
        @State private var selectedPhoto: PhotosPickerItem?
        @State private var image: Image?
        
        var body: some View {
            NavigationStack {
                ZStack {
                    image?
                        .resizable()
                        .scaledToFit()
                }
                .toolbar {
                    PhotosPicker(
                        selection: $selectedPhoto,
                        matching: .videos
                    ) {
                        Image(systemName: "pencil")
                    }
                }
            }
        }
    }
    

You can also provide a binding to an array of the _PhotosPickerItem_ type to
enable multiple selections. In this case, you can use the _maxSelectionCount_
parameter to control the maximal number of allowed items.

    
    
    struct ContentView: View {
        @State private var selectedPhotos: [PhotosPickerItem] = []
        @State private var image: Image?
        
        var body: some View {
            NavigationStack {
                ZStack {
                    image?
                        .resizable()
                        .scaledToFit()
                }
                .toolbar {
                    PhotosPicker(selection: $selectedPhoto, maxSelectionCount: 3) {
                        Image(systemName: "pencil")
                    }
                }
            }
        }
    }
    

OK, we know how to provide a photo-picking experience, but what next? How can
we load the selected images? The _PhotosPickerItem_ type contains the whole
image and video loading logic. It provides the _loadTransferable_ function
allowing us to load any type conforming to the _Transferable_ protocol.

> To learn more about the basics of the _Transferable_ protocol, take a look
> at my [ “Sharing content in SwiftUI” ](/2023/03/28/sharing-content-in-
> swiftui/) post.
    
    
    struct ContentView: View {
        @State private var selectedPhoto: PhotosPickerItem?
        @State private var image: Image?
        
        var body: some View {
            NavigationStack {
                ZStack {
                    image?
                        .resizable()
                        .scaledToFit()
                }
                .toolbar {
                    PhotosPicker(
                        selection: $selectedPhoto,
                        matching: .all(of: [.screenshots, .panoramas])
                    ) {
                        Image(systemName: "pencil")
                    }
                }
                .task(id: selectedPhoto) {
                    image = try? await selectedPhoto?.loadTransferable(type: Image.self)
                }
            }
        }
    }
    

As you can see in the example above, we use the _loadTransferable_ function to
decode the image by using the new Swift Concurrency feature. The
_PhotosPickerItem_ type also provides a callback-based alternative if you
don’t use Swift Concurrency feature.

    
    
    struct ContentView: View {
        @State private var selectedPhoto: PhotosPickerItem?
        @State private var image: Image?
        
        var body: some View {
            NavigationStack {
                ZStack {
                    image?
                        .resizable()
                        .scaledToFit()
                }
                .toolbar {
                    PhotosPicker(
                        selection: $selectedPhoto,
                        matching: .all(of: [.screenshots, .panoramas])
                    ) {
                        Image(systemName: "pencil")
                    }
                }
                .task(id: selectedPhoto) {
                    if selectedPhoto?.supportedContentTypes.first == .image {
                        image = try? await selectedPhoto?.loadTransferable(type: Image.self)
                    }
                }
            }
        }
    }
    

The _PhotosPickerItem_ type also has the _supportedContentTypes_ property
defining the supported content type of the selected image or video item,
allowing us to understand how to decode the item.

Today we learned how to use the _PhotosPicker_ view in SwiftUI to implement
the image-picking functionality in our app. I enjoy the API it provides and
believe it is an excellent example of SwiftUI and Swift Concurrency feature
usage. I hope you enjoy the post. Feel free to follow me on [ Twitter
](https://twitter.com/mecid) and ask your questions related to this post.
Thanks for reading, and see you next week!

