##  Drag and drop transferable data in SwiftUI

05 Apr 2023

Last week we discussed the new _ShareLink_ view and the _Transferable_
protocol powering it. The new _Transferable_ protocol is useful for sharing
your data from the app, but it also powers drag and drop in your app. This
week we will learn how we can drag and drop data conforming to the
_Transferable_ protocol in SwiftUI.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

####  Dragging

The new _Transferable_ protocol allows us to implement the drag-and-drop
experience in our apps much more easily. All you need to do is to attach the
_draggable_ view modifier to any view in the view hierarchy and pass the data
you want to drag. The data you pass have to conform to the new _Transferrable_
protocol.

    
    
    struct BookmarksList: View {
        @State private var links: [URL] = [
            URL(string: "https://twitter.com/mecid")!
        ]
        
        var body: some View {
            List {
                ForEach(links, id: \.self) { url in
                    Text(url.absoluteString)
                        .draggable(url) {
                            Text(verbatim: url.absoluteString)
                        }
                }
            }
            .navigationBarTitle("Bookmarks")
        }
    }
    

As you can see in the example above, we use the new _draggable_ view modifier
to enable dragging URLs from the list. The _URL_ type conforms to the new
_Transferable_ protocol out of the box, and you don’t need to do anything here
to implement the conversion of URL data to the transferable format. We also
provide a preview for the draggable content by creating a _Text_ view with the
URL string.

The example above shows how you can enable the drag and drop feature for the
URL item, but you can do it for any type conforming to the _Transferable_
protocol.

> To learn more about the basics of the _Transferable_ protocol, take a look
> at my [ “Sharing content in SwiftUI” ](/2023/03/28/sharing-content-in-
> swiftui/) post.

####  Dropping

The next step is allowing your app to accept transferable content via drops.
All you need to do is to attach the new _dropDestination_ view modifier to any
view you want to take drops.

    
    
    struct BookmarksList: View {
        @State private var links: [URL] = [
            URL(string: "https://twitter.com/mecid")!
        ]
        
        var body: some View {
            List {
                ForEach(links, id: \.self) { url in
                    Text(url.absoluteString)
                        .draggable(url) {
                            Text(verbatim: url.absoluteString)
                        }
                }
                .dropDestination(for: URL.self) { items, location in
                    links.append(contentsOf: items)
                }
            }
            .navigationBarTitle("Bookmarks")
        }
    }
    

As you can see in the example above, we use the _dropDestination_ view
modifier to register an area that takes drops of the _URL_ type. We also use
the _dropDestination_ view modifier to register closure handling drops. It
takes two parameters: _items_ and _location_ . The _items_ parameter defines
an array of transferable data, and the _location_ parameter indicates the drop
position on the screen.

####  Conclusion

As you can see, it is straightforward to support the drag and drop feature in
your apps with the new _draggable_ and _dropDestination_ view modifiers. Both
of them are powered by the brand new CoreTransferable framework. I hope you
enjoy the post. Feel free to follow me on [ Twitter
](https://twitter.com/mecid) and ask your questions related to this post.
Thanks for reading, and see you next week!

