##  Mastering AsyncImage in SwiftUI

07 Jul 2021

During our careers, we primarily build apps that work with web services to
retrieve and upload data. Remote image is one type of that data that we need
to download and display. SwiftUI provides us the _AsyncImage_ type, which is a
view that downloads and shows an image via URL. This week we learn how to use
and customize _AsyncImage_ in SwiftUI.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

####  Basics

Let’s start with a quick example that shows how to use _AsyncImage_ .

    
    
    struct AvatarView: View {
        let url: URL
    
        var body: some View {
            AsyncImage(url: url)
        }
    }
    

As you can see in the example above, _AsyncImage_ is a SwiftUI view that takes
a URL for an image, downloads it, and displays it. There is no need for
additional configuration of the network layer. _AsyncImage_ uses the shared
_URLSession_ to download and cache images. Unfortunately, we can’t provide a
custom _URLCache_ or somehow customize a _URLRequest_ that downloads the
image.

_AsyncImage_ is another SwiftUI view which means you can attach any set of
view modifiers to have the desired look and feel. For example, we can clip the
shape of our image and set the size.

    
    
    struct AvatarView: View {
        let url: URL
    
        var body: some View {
            AsyncImage(url: url)
                .frame(width: 44, height: 44)
                .background(Color.gray)
                .clipShape(Circle())
        }
    }
    

####  Customization

Usually, we need to customize the size of the downloaded image, scaling
options, rendering mode, etc. We can access the instance of underlining image
using another overload of _AsyncImage_ initializer.

    
    
        AsyncImage(url: url) { image in
            image
                .resizable()
                .scaledToFill()
        } placeholder: {
            ProgressView()
        }
        .frame(width: 44, height: 44)
        .background(Color.gray)
        .clipShape(Circle())
    

Here we use another _AsyncImage_ initializer to access the downloaded image,
make it resizable and apply the filling content mode. This initializer also
allows us to provide a placeholder view that SwiftUI displays while
downloading the image.

> To learn more about image rendering options in SwiftUI, take a look at my [
> “Mastering images in SwiftUI” ](/2020/05/27/mastering-images-in-swiftui/)
> post.

Keep in mind that this initializer uses a _ViewBuilder_ closure which means
you can take advantage of any SwiftUI view modifier you need and build a super
custom presentation.

    
    
        AsyncImage(url: url) { image in
            image
                .resizable()
                .scaledToFill()
                .overlay(Material.ultraThin)
        } placeholder: {
            ProgressView()
        }
        .frame(width: 44, height: 44)
        .background(Color.gray)
        .clipShape(Circle())
    

In the example above, we use the _overlay_ view modifier to cover our image
with the ultra-thin material that creates a light blur effect.

> To learn more about the logic behind the ViewBuilder type, take a look at my
> [ “The power of @ViewBuilder in SwiftUI” ](/2019/12/18/the-power-of-
> viewbuilder-in-swiftui/) post.

_AsyncImage_ allows us to take complete control of all the steps of image
presentation using another initializer.

    
    
    struct AvatarView: View {
        let url: URL
    
        var body: some View {
            AsyncImage(
                url: url,
                transaction: Transaction(animation: .easeInOut)
            ) { phase in
                switch phase {
                case .empty:
                    ProgressView()
                case .success(let image):
                    image
                        .resizable()
                        .transition(.scale(scale: 0.1, anchor: .center))
                case .failure:
                    Image(systemName: "wifi.slash")
                @unknown default:
                    EmptyView()
                }
            }
            .frame(width: 44, height: 44)
            .background(Color.gray)
            .clipShape(Circle())
        }
    }
    

As you can see, we use another initializer that accepts a _ViewBuilder_
closure. This closure has only one parameter that is an instance of
_AsyncImagePhase_ enum. _AsyncImagePhase_ enum defines a bunch of image
loading states like _empty, success, and failed_ . You can handle all these
cases to provide super-custom image presentations.

Another parameter of the currently used initializer is the SwiftUI
transaction. By default, _AsyncImage_ creates a new transaction with the
default configuration. In our example, I create a custom transaction with a
particular animation that _AsyncImage_ will use whenever phase changes.

> To learn more about the power of transactions in SwiftUI, take a look at my
> [ “Transactions in SwiftUI” ](/2020/10/07/transactions-in-swiftui/) post.

####  Conclusion

Today we learned how to download and display remote images using _AsyncImage_
view. I’m happy to see that SwiftUI provides us this feature because it is
fundamental for most of the apps we build. I hope you enjoy the post. Feel
free to follow me on [ Twitter ](https://twitter.com/mecid) and ask your
questions related to this post. Thanks for reading, and see you next week!

