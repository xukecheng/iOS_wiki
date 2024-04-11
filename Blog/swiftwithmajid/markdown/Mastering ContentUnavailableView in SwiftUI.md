##  Mastering ContentUnavailableView in SwiftUI

31 Oct 2023

SwiftUI introduces the new _ContentUnavailableView_ type, allowing us to
display empty, error states or any other state where content is unavailable in
our apps. This week, we will learn how to use the _ContentUnavailableView_ to
guide users through empty states of your app.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

Let’s start with the very first example showing the basic usage of the
_ContentUnavailableView_ view.

    
    
    struct ContentView: View {
        let store: Store
        
        var body: some View {
            NavigationStack {
                List(store.products, id: \.self) { product in
                    Text(verbatim: product)
                }
                .navigationTitle("Products")
                .overlay {
                    if store.products.isEmpty {
                        ContentUnavailableView(
                            "Connection issue",
                            systemImage: "circle"
                        )
                    }
                }
            }
        }
    }
    

![empty-state](/public/ContentUnavailableView1.png)

As you can see in the example above, we define the _ContentUnavailableView_ as
overlay for the list of products. Whenever the product list is empty we
display the _ContentUnavailableView_ with title and image. Another variant of
the _ContentUnavailableView_ view allows us also define the description text
of the current state.

    
    
    struct ContentView: View {
        let store: Store
        
        var body: some View {
            NavigationStack {
                List(store.products, id: \.self) { product in
                    Text(verbatim: product)
                }
                .navigationTitle("Products")
                .overlay {
                    if store.products.isEmpty {
                        ContentUnavailableView(
                            "Connection issue",
                            systemImage: "wifi.slash",
                            description: Text("Check your internet connection")
                        )
                    }
                }
            }
        }
    }
    

![empty-state](/public/ContentUnavailableView2.png)

The _ContentUnavailableView_ allows us also display action buttons below the
description. That’s why there is another variant of the
_ContentUnavailableView_ initializer allowing us to define every piece of the
view using _ViewBuilder_ closures.

    
    
    struct ContentView: View {
        let store: Store
        
        var body: some View {
            NavigationStack {
                List(store.products, id: \.self) { product in
                    Text(verbatim: product)
                }
                .navigationTitle("Products")
                .overlay {
                    if store.products.isEmpty {
                        ContentUnavailableView {
                            Label("Connection issue", systemImage: "wifi.slash")
                        } description: {
                            Text("Check your internet connection")
                        } actions: {
                            Button("Refresh") {
                                store.fetch()
                            }
                        }
                    }
                }
            }
        }
    }
    

As you can see in the example above, we use a set of closures to define label,
description and actions. This initializer allows us to fully customize the
look and feel of an instance of the _ContentUnavailableView_ type.

![empty-state](/public/ContentUnavailableView3.png)

SwiftUI provides us a ready-to-use predefined instance of the
_ContentUnavailableView_ type that we can use in search screens.

    
    
    struct ContentView: View {
        @Bindable var store: Store
        
        var body: some View {
            NavigationStack {
                List(store.products, id: \.self) { product in
                    Text(verbatim: product)
                }
                .navigationTitle("Products")
                .overlay {
                    if store.products.isEmpty {
                        ContentUnavailableView.search
                    }
                }
                .searchable(text: $store.query)
            }
        }
    }
    

Whenever you have a search screen displaying search results, you can use the
_search_ function of the _ContentUnavailableView_ type. It is localized by the
framework and traverse the view hierarchy to find a search bar and extract its
text to display inside the view.

![empty-state](/public/ContentUnavailableView4.png)

Remember that you should place the _searchable_ view modifier below the
overlay if you want to extract the text from the search bar otherwise it
doesn’t personalize the message.

    
    
    struct ContentView: View {
        @Bindable var store: Store
        
        var body: some View {
            NavigationStack {
                List(store.products, id: \.self) { product in
                    Text(verbatim: product)
                }
                .navigationTitle("Products")
                .overlay {
                    if store.products.isEmpty {
                        ContentUnavailableView.search(text: store.query)
                    }
                }
                .searchable(text: $store.query)
            }
        }
    }
    

You can also provide query into the description manually by using the _search_
function of the _ContentUnavailableView_ type with a single parameter.

Today, we learned how to use the _ContentUnavailableView_ type in SwiftUI to
display empty states in a user-friendly manner. I hope you enjoy the post.
Feel free to follow me on [ Twitter ](https://twitter.com/mecid) and ask your
questions related to this post. Thanks for reading, and see you next week!

