##  Combining multiple Combine publishers in Swift

12 May 2021

I’ve already covered a few essential topics from the Combine framework story.
We talked about handling errors and chaining operations, but today I want to
talk about running multiple operations in parallel and handing results in a
single place. This week we will learn how to use zip, merge and combine
operators.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

####  Zip

_Zip_ operator is handy when you have a couple of publishers and need to wait
for values from both of them. For example, assume that you are working on some
kind of store app. You have a product screen where you show product details
and the list of related products. In this case, you might want to display
details and associated products at the same time. You can achieve this
behavior using the _Zip_ operator.

    
    
    final class ProductViewModel: ObservableObject {
        @Published private(set) var product: Product?
        @Published private(set) var related: [Product] = []
    
        let service = ProductsService()
        private var cancellable: AnyCancellable?
    
        func fetch(_ product: UUID) {
            cancellable = Publishers.Zip(
                service.fetch(product),
                service.fetchRelatedProducts(for: product)
            )
            .sink(
                receiveCompletion: { print($0) },
                receiveValue: { [weak self] product, related in
                    self?.product = product
                    self?.related = related
                }
            )
        }
    }
    

> To learn more about designing API with Combine publishers, take a look at my
> [ “Designing API using Combine framework” ](/2021/04/07/designing-api-using-
> combine-framework/) post.

As you can see in the example above, we use _Zip_ to fetch product details and
related products. As soon as both publishers emit the value _sink_ subscriber
will assign them to the stored properties.

####  CombineLatest

The main downside of the _Zip_ operator is that it delivers values only when
all the publishers emit. Sometimes we want to obtain all the values even when
some of them change more often than others. For example, assume that you are
working on a signup screen where you have text fields for email, password, and
repeated password. You also have a signup button that should be enabled when
all the text fields contain valid data.

    
    
    final class SignUpViewModel: ObservableObject {
        @Published var email: String = ""
        @Published var password1: String = ""
        @Published var password2: String = ""
    
        var isValid: AnyPublisher<Bool, Never> {
            Publishers
                .CombineLatest3($email, $password1, $password2)
                .allSatisfy { email, password1, password2 in
                    email.contains("@") &&
                        password1.count > 7 &&
                        password1 == password2
                }.eraseToAnyPublisher()
        }
    }
    

Here we have the signup screen’s view model. It contains a few stored
properties which we are going to use in our view. It also has _isValid_
computed property that creates a validation publisher.

As you can see, we use the _CombineLatest_ operator to obtain the latest
values from all the publishers. _CombineLatest_ publisher collects the first
value from all three publishers and emits them as a single tuple.
_CombineLatest_ continues sending new values even when only one publisher
emits a new value.

On the other hand, the _Zip_ operator sends a new value only when all the
publishers emit new values.

####  MergeMany

_Merge_ is another helpful operator provided by the Combine framework that you
can use to join a few different publishers with the same output type. I often
use the _Merge_ operator while fetching locally cached data and fetching new
data from the webserver.

    
    
    final class FavoritesViewModel: ObservableObject {
        @Published private(set) var products: [Product] = []
        let service = ProductsService()
    
        func fetch() {
            Publishers.MergeMany(
                service.fetchCachedFavorites(),
                service.fetchFavorites()
            )
            .replaceError(with: [])
            .assign(to: &$products)
        }
    }
    

As you can see, the _MergeMany_ operator allows me to create a single pipe for
cached and fresh data where the cached information usually appears first and
then replaced by new data.

> To learn about building custom Combine operators, take a look at my [
> “Building custom Combine operators in Swift” ](/2021/04/28/building-custom-
> combine-operators-in-swift/) post.

####  Conclusion

This week we learned about operators of the Combine framework, which allows us
to build complex data pipelines by zipping and merging multiple publishers. I
hope you enjoy the post. Feel free to follow me on [ Twitter
](https://twitter.com/mecid) and ask your questions related to this post.
Thanks for reading, and see you next week!

