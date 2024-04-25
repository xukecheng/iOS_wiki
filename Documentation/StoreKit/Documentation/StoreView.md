Initializer

# init(ids:prefersPromotionalIcon:)

Creates a view to load and merchandise a collection of products from the App
Store using product identifiers.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    init(
        ids productIDs: some Collection<String>,
        prefersPromotionalIcon: Bool = false
    ) where Icon == EmptyView, PlaceholderIcon == EmptyView

##  Parameters

`productIDs`

    

The product identifiers to load from the App Store.

`prefersPromotionalIcon`

    

A Boolean value that indicates whether to use promotional images from the App
Store, if they’re available. If this parameter is `false`, the system ignores
promotional images.

## See Also

### Creating store views that load products

`init(ids: some Collection<String>, prefersPromotionalIcon: Bool, icon:
(Product) -> Icon)`

Creates a view to load a collection of products from the App Store using
product identifiers, and merchandise them using a custom image.

`init(ids: some Collection<String>, prefersPromotionalIcon: Bool, icon:
(Product) -> Icon, placeholderIcon: () -> PlaceholderIcon)`

Creates a view to load a collection of products from the App Store using
product identifiers, and merchandise them using an image and a custom
placeholder icon.

`init(ids: some Collection<String>, icon: (Product, ProductIconPhase) -> Icon,
placeholderIcon: () -> PlaceholderIcon)`

Creates a view to load a collection of products from the App Store using
product identifiers, and merchandise them using their promotional images and a
custom placeholder icon.

Initializer

# init(ids:prefersPromotionalIcon:icon:)

Creates a view to load a collection of products from the App Store using
product identifiers, and merchandise them using a custom image.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    init(
        ids productIDs: some Collection<String>,
        prefersPromotionalIcon: Bool = false,
        @ViewBuilder icon: @escaping (Product) -> Icon
    ) where PlaceholderIcon == AutomaticProductPlaceholderIcon

##  Parameters

`productIDs`

    

The product identifiers to load from the App Store.

`prefersPromotionalIcon`

    

A Boolean value that indicates whether to use promotional images from the App
Store, if they’re available. If this parameter is `false`, the system ignores
promotional images.

`icon`

    

A closure that returns the image the view displays when the products finish
loading from the App Store.

## Discussion

The store view shows a placeholder icon until all products finish loading.
Then, the view uses the image that you provide in `icon`, by default. If you
set `prefersPromotionalIcon` to `true`, the view uses the promotional image
instead of the `icon` for any products that have promotional images available.

## See Also

### Creating store views that load products

`init(ids: some Collection<String>, prefersPromotionalIcon: Bool)`

Creates a view to load and merchandise a collection of products from the App
Store using product identifiers.

`init(ids: some Collection<String>, prefersPromotionalIcon: Bool, icon:
(Product) -> Icon, placeholderIcon: () -> PlaceholderIcon)`

Creates a view to load a collection of products from the App Store using
product identifiers, and merchandise them using an image and a custom
placeholder icon.

`init(ids: some Collection<String>, icon: (Product, ProductIconPhase) -> Icon,
placeholderIcon: () -> PlaceholderIcon)`

Creates a view to load a collection of products from the App Store using
product identifiers, and merchandise them using their promotional images and a
custom placeholder icon.

Initializer

# init(ids:prefersPromotionalIcon:icon:placeholderIcon:)

Creates a view to load a collection of products from the App Store using
product identifiers, and merchandise them using an image and a custom
placeholder icon.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    init(
        ids productIDs: some Collection<String>,
        prefersPromotionalIcon: Bool = false,
        @ViewBuilder icon: @escaping (Product) -> Icon,
        @ViewBuilder placeholderIcon: () -> PlaceholderIcon
    )

##  Parameters

`productIDs`

    

The product identifiers to load from the App Store.

`prefersPromotionalIcon`

    

A Boolean value that indicates whether to use a promotional image from the App
Store, if it’s available. If this parameter is `false`, the system ignores
promotional images.

`icon`

    

A closure that returns the image the view displays when the products finish
loading from the App Store.

`placeholderIcon`

    

A closure that returns the image that the view uses while the products are
loading. The view uses the same placeholder image for all the products.

## Discussion

The store view shows the custom placeholder icon until all products finish
loading. After the view finishes loading the products, it uses the image you
provide, by default. If you set `prefersPromotionalIcon `to `true`, any
products that have an available promotional image use the promotional image
instead.

The following example shows how to create a store view using an icon and a
custom placeholder icon:

## See Also

### Creating store views that load products

`init(ids: some Collection<String>, prefersPromotionalIcon: Bool)`

Creates a view to load and merchandise a collection of products from the App
Store using product identifiers.

`init(ids: some Collection<String>, prefersPromotionalIcon: Bool, icon:
(Product) -> Icon)`

Creates a view to load a collection of products from the App Store using
product identifiers, and merchandise them using a custom image.

`init(ids: some Collection<String>, icon: (Product, ProductIconPhase) -> Icon,
placeholderIcon: () -> PlaceholderIcon)`

Creates a view to load a collection of products from the App Store using
product identifiers, and merchandise them using their promotional images and a
custom placeholder icon.

Initializer

# init(ids:icon:placeholderIcon:)

Creates a view to load a collection of products from the App Store using
product identifiers, and merchandise them using their promotional images and a
custom placeholder icon.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    init(
        ids productIDs: some Collection<String>,
        @ViewBuilder icon: @escaping (Product, ProductIconPhase) -> Icon,
        @ViewBuilder placeholderIcon: () -> PlaceholderIcon
    )

##  Parameters

`productIDs`

    

The product identifiers to load from the App Store.

`icon`

    

A closure that receives a `Product` and a `ProductIconPhase` as input. The
`ProductIconPhase` indicates the state of the loading operation of the
product’s promotional image. The closure returns the view to display for the
given product and phase value.

`placeholderIcon`

    

A closure that returns the view that the store view uses while the products
are loading. The store view uses the same placeholder image for all the
products.

## Discussion

The store view shows the custom `placeholderIcon` until all products finish
loading. After the products finish loading, the view asynchronously loads and
displays each product’s promotional image.

Use the `ProductIconPhase` to monitor the current loading state of a product’s
promotional image, and provide a view for each phase. Consider returning the
view provided in the `placeholderIcon `closure for during the
`ProductIconPhase.loading` phase. For more information, see
`ProductIconPhase`.

If a product is unavailable, the store view uses the view that the
`placeholderIcon` closure provides as a fallback.

## See Also

### Creating store views that load products

`init(ids: some Collection<String>, prefersPromotionalIcon: Bool)`

Creates a view to load and merchandise a collection of products from the App
Store using product identifiers.

`init(ids: some Collection<String>, prefersPromotionalIcon: Bool, icon:
(Product) -> Icon)`

Creates a view to load a collection of products from the App Store using
product identifiers, and merchandise them using a custom image.

`init(ids: some Collection<String>, prefersPromotionalIcon: Bool, icon:
(Product) -> Icon, placeholderIcon: () -> PlaceholderIcon)`

Creates a view to load a collection of products from the App Store using
product identifiers, and merchandise them using an image and a custom
placeholder icon.

Initializer

# init(products:prefersPromotionalIcon:)

Creates a view to load and merchandise a collection of products from the App
Store.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    init(
        products: some Collection<Product>,
        prefersPromotionalIcon: Bool = false
    ) where Icon == EmptyView, PlaceholderIcon == EmptyView

##  Parameters

`products`

    

The products to merchandise.

`prefersPromotionalIcon`

    

A Boolean value that indicates whether to use promotional images from the App
Store, if they’re available. If this parameter is `false`, the system ignores
promotional images.

## Discussion

By default, the store view doesn’t show promotional images. If you set
`prefersPromotionalIcon` to `true`, the store view uses each product’s
promotional image as its icon.

## See Also

### Creating store views with preloaded products

`init(products: some Collection<Product>, prefersPromotionalIcon: Bool, icon:
(Product) -> Icon)`

Creates a view to merchandise a collection of products using a custom icon.

`init(products: some Collection<Product>, icon: (Product, ProductIconPhase) ->
Icon)`

Creates a view to merchandise a collection of products with promotional
images.

Initializer

# init(products:prefersPromotionalIcon:icon:)

Creates a view to merchandise a collection of products using a custom icon.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    init(
        products: some Collection<Product>,
        prefersPromotionalIcon: Bool = false,
        @ViewBuilder icon: @escaping (Product) -> Icon
    ) where PlaceholderIcon == EmptyView

##  Parameters

`products`

    

The products to merchandise.

`prefersPromotionalIcon`

    

A Boolean value that indicates whether to use promotional images from the App
Store, if they’re available. If this parameter is `false`, the system ignores
promotional images.

`icon`

    

A closure that returns the image the view displays when the products finish
loading from the App Store.

## Discussion

If you set `prefersPromotionalIcon` to `true`, the view uses promotional
images for products that have a promotional image available.

The following code example shows how to create a store view using a custom
icon:

## See Also

### Creating store views with preloaded products

`init(products: some Collection<Product>, prefersPromotionalIcon: Bool)`

Creates a view to load and merchandise a collection of products from the App
Store.

`init(products: some Collection<Product>, icon: (Product, ProductIconPhase) ->
Icon)`

Creates a view to merchandise a collection of products with promotional
images.

Initializer

# init(products:icon:)

Creates a view to merchandise a collection of products with promotional
images.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    init(
        products: some Collection<Product>,
        @ViewBuilder icon: @escaping (Product, ProductIconPhase) -> Icon
    ) where PlaceholderIcon == EmptyView

##  Parameters

`products`

    

The products to merchandise.

`icon`

    

A closure that receives a `Product` and a `ProductIconPhase` as input. The
`ProductIconPhase` indicates the state of the loading operation of the
product’s promotional image. The closure returns the view to display for the
given product and phase value.

## Discussion

The store view asynchronously loads and displays each product’s promotional
image. Use the `ProductIconPhase` to monitor the current loading phase of the
product’s promotional image, and provide an image for each phase. For more
information about the loading phases, see `ProductIconPhase`.

## See Also

### Creating store views with preloaded products

`init(products: some Collection<Product>, prefersPromotionalIcon: Bool)`

Creates a view to load and merchandise a collection of products from the App
Store.

`init(products: some Collection<Product>, prefersPromotionalIcon: Bool, icon:
(Product) -> Icon)`

Creates a view to merchandise a collection of products using a custom icon.

Instance Method

# inAppPurchaseOptions(_:)

Adds a function the system calls before it processes a purchase from a store
view, which provides a set of purchase options.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    func inAppPurchaseOptions(_ options: ((Product) async -> Set<Product.PurchaseOption>)?) -> some View

##  Parameters

`options`

    

A closure you provide for the system to call before it processes a purchase.
The system sends the product the person intends to purchase as a parameter.
Return a set of purchase options (`Product.PurchaseOption`) to add to the
purchase.

## See Also

### Responding to store events

`func onInAppPurchaseCompletion(perform: ((Product,
Result<Product.PurchaseResult, any Error>) -> ())?) -> View`

Adds an action to perform when a purchase the person initiated from within a
product view completes.

`func onInAppPurchaseStart(perform: ((Product) -> ())?) -> View`

Adds an action to perform when a user triggers the purchase button on a
product within this view.

`enum EntitlementTaskState`

The state of an entitlement task.

Instance Method

# onInAppPurchaseCompletion(perform:)

Adds an action to perform when a purchase the person initiated from within a
product view completes.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    func onInAppPurchaseCompletion(perform action: ((Product, Result<Product.PurchaseResult, any Error>) async -> ())?) -> some View

## See Also

### Responding to store events

`func inAppPurchaseOptions(((Product) -> Set<Product.PurchaseOption>)?) ->
View`

Adds a function the system calls before it processes a purchase from a store
view, which provides a set of purchase options.

`func onInAppPurchaseStart(perform: ((Product) -> ())?) -> View`

Adds an action to perform when a user triggers the purchase button on a
product within this view.

`enum EntitlementTaskState`

The state of an entitlement task.

Instance Method

# onInAppPurchaseStart(perform:)

Adds an action to perform when a user triggers the purchase button on a
product within this view.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    func onInAppPurchaseStart(perform action: ((Product) async -> ())?) -> some View

## See Also

### Responding to store events

`func inAppPurchaseOptions(((Product) -> Set<Product.PurchaseOption>)?) ->
View`

Adds a function the system calls before it processes a purchase from a store
view, which provides a set of purchase options.

`func onInAppPurchaseCompletion(perform: ((Product,
Result<Product.PurchaseResult, any Error>) -> ())?) -> View`

Adds an action to perform when a purchase the person initiated from within a
product view completes.

`enum EntitlementTaskState`

The state of an entitlement task.

Instance Method

# productViewStyle(_:)

Sets the style for in-app purchase product views within a view.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    func productViewStyle(_ style: some ProductViewStyle) -> some View

Instance Method

# storeButton(_:for:)

Specifies the visibility of auxilliary buttons that store view and
subscription store view instances may use.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    func storeButton(
        _ visibility: Visibility,
        for buttonKinds: StoreButtonKind...
    ) -> some View

##  Parameters

`visibility`

    

The preferred visibility (`Visibility`) of the button.

`buttonKinds`

    

The type of store button (`StoreButtonKind`).

## See Also

### Configuring and styling products

`struct StoreButtonKind`

A button to display in a store view or subscription store view.

Instance Property

# body

The content and behavior of the view.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    @MainActor
    var body: some View { get }

## Relationships

### From Protocol

  * `View`

## See Also

### Implementing store views

`typealias StoreView.Body`

The type of view that represents the body of the store view.

Type Alias

# StoreView.Body

The type of view that represents the body of the store view.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    typealias StoreView<Icon, PlaceholderIcon>.Body = some View

## Relationships

### From Protocol

  * `View`

## See Also

### Implementing store views

`var body: View`

The content and behavior of the view.

Instance Method

# productDescription(_:)

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.4+
tvOS 17.0+  watchOS 10.0+  visionOS 1.1+  Xcode 15.0+

    
    
    func productDescription(_ visibility: Visibility) -> some View

Instance Method

# searchPresentationToolbarBehavior(_:)

StoreKit  SwiftUI  iOS 17.1+  iPadOS 17.1+  macOS 14.1+  Mac Catalyst 17.2+
tvOS 17.1+  watchOS 10.1+  visionOS 1.0+  Xcode 14.4+

    
    
    func searchPresentationToolbarBehavior(_ behavior: SearchPresentationToolbarBehavior) -> some View

Instance Method

# subscriptionPromotionalOffer(offer:signature:)

StoreKit  SwiftUI  iOS 17.4+  iPadOS 17.4+  macOS 14.4+  Mac Catalyst 17.4+
tvOS 17.4+  watchOS 10.4+  visionOS 1.1+  Xcode 15.3+

    
    
    func subscriptionPromotionalOffer(
        offer: @escaping (Product, Product.SubscriptionInfo) -> Product.SubscriptionOffer?,
        signature: @escaping (Product, Product.SubscriptionInfo, Product.SubscriptionOffer) async throws -> Product.SubscriptionOffer.Signature
    ) -> some View

