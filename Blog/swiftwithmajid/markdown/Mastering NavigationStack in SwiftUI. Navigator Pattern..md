##  Mastering NavigationStack in SwiftUI. Navigator Pattern.

15 Jun 2022

SwiftUI is the declarative data-driven framework allowing us to build complex
user interfaces by defining the data rendering on the screen. Navigation was
the main pain point of the framework from the very first day. Fortunately,
things have changed since WWDC 22, and SwiftUI provides the new data-driven
Navigation API. This week we will learn how to use the new Navigation API to
build complex user flows.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

####  Basics

First, I must mention that the old _NavigationView_ is deprecated, and we
should use the new _NavigationStack_ instead. Let’s take a look at a quick
example.

    
    
    struct MasterView: View {
        let products: [Product]
        
        var body: some View {
            NavigationStack {
                List(products) { product in
                    NavigationLink(product.title) {
                        ProductDetailView(product: product)
                    }
                }
                .navigationTitle("Products")
            }
        }
    }
    
    struct ProductDetailView: View {
        let product: Product
        
        var body: some View {
            Text(product.title)
                .font(.title)
                .navigationTitle(product.title)
        }
    }
    

In the example above, we define a simple master-detail flow. We place
_NavigationStack_ at the root of our view hierarchy. Next, we define a list of
messages where every message provides a link to the details screen of the
particular message. As you can see, we still use the old _NavigationLink_ type
here, and it works great for this use case.

> To learn more about other new features of SwiftUI, take a look at my [ “What
> is new in SwiftUI after WWDC22” ](/2022/06/07/what-is-new-in-swiftui-after-
> wwdc22/) post.

The _NavigationLink_ type adds new data-driven capabilities. A brand new
initializer allows us to create a link bound to some value. Here is the
previous example refactored using the new data-driven Navigation API.

    
    
    struct MasterView1: View {
        let products: [Product]
        
        var body: some View {
            NavigationStack {
                List(products) { product in
                    NavigationLink(product.title, value: product)
                }
                .navigationTitle("Products")
                .navigationDestination(for: Product.self) { product in
                    ProductDetailView(product: product)
                }
            }
        }
    }
    

We use the new value-based navigation links to route the user through the app.
Look at how we associate every item on the list with a particular value. Keep
in mind, **value** must conform to the **Hashable** protocol. Next, we define
a destination view for a specific value using the _navigationDestination_ view
modifier. In the current example, we have only one type of destination, but
you can have as many as you need by applying multiple _navigationDestination_
view modifiers.

    
    
    struct MasterView2: View {
        let categories: [Category]
        let recentProducts: [Product]
        
        var body: some View {
            NavigationStack {
                List {
                    Section("Categories") {
                        ForEach(categories) { category in
                            NavigationLink(value: category) {
                                Text(category.query)
                                    .font(.headline)
                            }
                        }
                    }
                    
                    Section("Recent") {
                        ForEach(recentProducts) { product in
                            NavigationLink(product.title, value: product)
                        }
                    }
                }
                .navigationTitle("Home")
                .navigationDestination(for: Category.self) { category in
                    CategoryView(category: category)
                }
                .navigationDestination(for: Product.self) { product in
                    ProductDetailView(product: product)
                }
            }
        }
    }
    

Remember that we also have another version of the value-based _NavigationLink_
initializer, allowing us to provide a custom label for the link. We use this
version of the initializer to give the headline font for category links.

####  Placing rules

You should be careful about placing the _navigationDestination_ view modifier
in the view hierarchy. There are three rules for placing the
_navigationDestination_ view modifier:

  1. The _navigationDestination_ view modifier should be inside the _NavigationStack_ . 
  2. Don’t place _navigationDestination_ view modifier on the child of lazy container like _List_ , _ScrollView_ , _LazyVStack_ , etc. 
  3. The top-level _navigationDestination_ view modifier will always override the lowest one for the same type. 

####  Navigator pattern

I love to keep my feature’s navigation flow in a single place. That’s why I
usually implement the Navigator pattern allowing me to handle my navigation in
a type-safe way. It is effortless to implement the Navigator pattern with the
new data-driven Navigation API in SwiftUI. First, we should create an enum
type defining all our app/feature/module routes.

    
    
    enum Route: Hashable {
        case product(Product)
        case category(Category)
    }
    

Next, we should use Route enum with the new value-based navigation links.

    
    
    struct MasterView3: View {
        let categories: [Category]
        let recentProducts: [Product]
        
        var body: some View {
            List {
                Section("Categories") {
                    ForEach(categories) { category in
                        NavigationLink(value: Route.category(category)) {
                            Text(category.query)
                        }
                    }
                }
                
                Section("Recent") {
                    ForEach(recentProducts) { product in
                        NavigationLink(value: Route.product(product)) {
                            Text(product.title)
                        }
                    }
                }
            }
            .navigationTitle("Home")
        }
    }
    

Finally, we can place the single _navigationDestination_ view modifier and
handle all the cases of our _Route_ type.

    
    
    struct AppContainerView: View {
        @StateObject private var store = Store()
        
        var body: some View {
            NavigationStack {
                MasterView3(
                    categories: store.categories,
                    recentProducts: store.products
                )
                .navigationDestination(for: Route.self) { route in
                    switch route {
                    case let .category(category):
                        CategoryView(category: category)
                    case let .product(product):
                        ProductDetailView(product: product)
                    }
                }
            }
        }
    }
    

####  Conclusion

I’m thrilled to use the new data-driven Navigation API in SwiftUI. If you
follow my blog, you might know that I have been waiting for it since the first
day. I will continue to cover the new data-driven Navigation API in detail,
and next week we will talk about deep linking. I hope you enjoy the post. Feel
free to follow me on [ Twitter ](https://twitter.com/mecid) and ask your
questions related to this post. Thanks for reading, and see you next week!

