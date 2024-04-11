##  Drag and drop in SwiftUI

01 Apr 2020

Another _iPadOS_ feature released in SwiftUI with Xcode 11.4 was the drag and
drop. Finally, we can use drag and drop API not only with _UIKit_ but also
with SwiftUI. This week we will learn all about drag and drop interactions in
SwiftUI.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

####  Basics

Drag and drop interactions allow users to send data between two apps or two
scenes of the same app. For example, you can run Safari and Notes apps side-
by-side and drag the links from Safari to Notes app. As part of the post, we
will build a bookmarking app that uses drag and drop to save or open links
stored in the app.

####  Drag

SwiftUI provides _onDrag_ modifier that allows us to register a closure that
will create and return _NSItemProvider_ . _NSItemProvider_ is the class that
describes the content and the type of draggable item. Let’s take a look at how
we can use _onDrag_ modifier.

    
    
    struct BookmarksList: View {
        @State private var links: [URL] = [
            URL(string: "https://twitter.com/mecid")!
        ]
    
        var body: some View {
            List {
                ForEach(links, id: \.self) { url in
                    Text(url.absoluteString)
                        .onDrag { NSItemProvider(object: url as NSURL) }
                }
            }
            .navigationBarTitle("Bookmarks")
        }
    }
    

As you can see in the example above, all we need to do is to use _onDrag_
modifier that returns an instance of _NSItemProvider_ . Now you can run the
app on the iPad simulator side-by-side with Safari and try to drag and drop
the link from our app to Safari.

####  Drag preview

Another version of the _onDrag_ view modifier allows you to provide a preview
of the dragging content.

    
    
    struct BookmarksList: View {
        @State private var links: [URL] = [
            URL(string: "https://twitter.com/mecid")!
        ]
    
        var body: some View {
            List {
                ForEach(links, id: \.self) { url in
                    Text(url.absoluteString)
                        .onDrag {
                            NSItemProvider(object: url as NSURL)
                        } preview: {
                            Text(verbatim: url.absoluteString)
                        }
                }
            }
            .navigationBarTitle("Bookmarks")
        }
    }
    

####  Drop

Unlike drag operation, drop interaction is a little bit complicated. SwiftUI
gave us three overloads of _onDrop_ modifier.

    
    
    struct BookmarksList: View {
        @State private var links: [URL] = [
            URL(string: "https://twitter.com/mecid")!
        ]
        
        var body: some View {
            List {
                ForEach(links, id: \.self) { url in
                    Text(url.absoluteString)
                        .onDrag { NSItemProvider(object: url as NSURL) }
                }
                .onDrop(of: ["public.url"], isTargeted: nil) { providers in
                    providers.forEach { provider in
                        _ = provider.loadObject(ofClass: URL.self) { url, _ in
                            if let url {
                                links.append(url)
                            }
                        }
                    }
                    return true
                }
            }
            .navigationBarTitle("Bookmarks")
        }
    }
    

The most interesting one is the overload that accepts _DropDelegate_ .
_DropDelegate_ is the protocol that we can implement to control drop
interaction. Let’s take a look at the quick example.

    
    
    struct BookmarksDropDelegate: DropDelegate {
        @Binding var bookmarks: [URL]
    
        func performDrop(info: DropInfo) -> Bool {
            guard info.hasItemsConforming(to: ["public.url"]) else {
                return false
            }
    
            let items = info.itemProviders(for: ["public.url"])
            for item in items {
                _ = item.loadObject(ofClass: URL.self) { url, _ in
                    if let url = url {
                        DispatchQueue.main.async {
                            self.bookmarks.insert(url, at: 0)
                        }
                    }
                }
            }
    
            return true
        }
    }
    

Here we have a _BookmarksDropDelegate_ struct that conforms to _DropDelegate_
protocol. _DropDelegate_ protocol requires us to implement _performDrop_
function. This function should return _true_ whenever the drop succeeded or
_false_ if it failed. _performDrop_ function has _DropInfo_ parameter, which
provides us the information about items that should be dropped.

Using _DropInfo_ , we can filter items and accept only links. Apple uses
_Uniform Type Identifiers_ to identify the type of data. We want to receive
only URLs that’s why we use **public.link** identifier. _DropInfo_ also
provides us the location of drop using _CGPoint_ instance.

> To learn more about _Uniform Type Identifiers_ , take a look at [ Apple’s
> documentation
> ](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/understanding_utis/understand_utis_intro/understand_utis_intro.html)
> .

_DropDelegate_ also has a few not required functions that we can use to
understand when dropping started and ended. Finally, we are ready to register
our _BookmarksDropDelegate_ on the _List_ or _ForEach_ to enable drop
interaction.

    
    
    struct BookmarksList: View {
        @State private var links: [URL] = [
            URL(string: "https://twitter.com/mecid")!
        ]
    
        var body: some View {
            List {
                ForEach(links, id: \.self) { url in
                    Text(url.absoluteString)
                        .onDrag { NSItemProvider(object: url as NSURL) }
                }
                .onDrop(
                    of: ["public.url"],
                    delegate: BookmarksDropDelegate(bookmarks: $links)
                )
            }
            .navigationBarTitle("Bookmarks")
        }
    

Unfortunately, _onDrop_ modifier doesn’t affect the _List_ or any view that
inside a _List_ . It works well with _VStack_ , _ScrollView_ , and other
views. But it doesn’t work with the _List_ .

I hope it is a bug, and Apple will fix it soon. We can replace the _List_ with
_ScrollView_ to make _onDrop_ modifier working. But in this case, we will lose
all the features of the _List_ component.

####  Insert

Gladly, SwiftUI provides us another modifier that we can use on _ForEach_
view. _onInsert_ modifier looks like a simplified version of _onDrop_
modifier, and it works inside _List_ component. Let’s take a look at the quick
usage example of _onInsert_ modifier.

    
    
    struct BookmarksList: View {
        @State private var links: [URL] = [
            URL(string: "https://twitter.com/mecid")!
        ]
    
        var body: some View {
            List {
                ForEach(links, id: \.self) { url in
                    Text(url.absoluteString)
                        .onDrag { NSItemProvider(object: url as NSURL) }
                }
                .onInsert(of: ["public.url"], perform: drop)
            }
            .navigationBarTitle("Bookmarks")
        }
    
        private func drop(at index: Int, _ items: [NSItemProvider]) {
            for item in items {
                _ = item.loadObject(ofClass: URL.self) { url, _ in
                    DispatchQueue.main.async {
                        url.map { self.links.insert($0, at: index) }
                    }
                }
            }
        }
    }
    

As you can see, we use _onInsert_ modifier to accept the insertion of links.
We also pass the drop function that handles the process of loading the URL
object and insertion.

####  Conclusion

Today we learned another new feature that released with Xcode 11.4. Please
note that all drag and drop related modifiers are available as part of iOS
13.4. I hope you enjoy the post. Feel free to follow me on [ Twitter
](https://twitter.com/mecid) and ask your questions related to this post.
Thanks for reading, and see you next week!

