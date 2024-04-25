Initializer

# init(id:prefersPromotionalIcon:)

Creates a view to load and merchandise an individual product from the App
Store.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    init(
        id productID: Product.ID,
        prefersPromotionalIcon: Bool = false
    ) where Icon == EmptyView, PlaceholderIcon == EmptyView

##  Parameters

`productID`

    

The product identifier to load from the App Store.

`prefersPromotionalIcon`

    

A Boolean value that indicates whether to use the promotional image from the
App Store, if it’s available. If this parameter is `false`, the system ignores
any promotional images.

## Discussion

By default, the view doesn’t show an icon. If you set the
`prefersPromotionalIcon` parameter to `true`, the view displays a placeholder
icon while loading, and replaces the placeholder with the promotional image
for the product.

Tip

To gain more control over the image that decorates this view, use the
`init(id:icon:placeholderIcon:)` initializer. It receives a
`ProductIconPhase`, which enables you to supply an image for each phase of the
image-loading process.

## See Also

### Creating product views that load products

`init(id: Product.ID, prefersPromotionalIcon: Bool, icon: () -> Icon)`

Creates a view to load an individual product from the App Store and
merchandise it using a custom icon.

`init(id: Product.ID, prefersPromotionalIcon: Bool, icon: () -> Icon,
placeholderIcon: () -> PlaceholderIcon)`

Creates a view to load an individual product from the App Store and
merchandise it using an image and a custom placeholder icon.

`init(id: Product.ID, icon: (ProductIconPhase) -> Icon, placeholderIcon: () ->
PlaceholderIcon)`

Creates a view to load an individual product from the App Store, and
merchandise it using its promotional image and a custom placeholder icon.

Initializer

# init(id:prefersPromotionalIcon:icon:)

Creates a view to load an individual product from the App Store and
merchandise it using a custom icon.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    init(
        id productID: Product.ID,
        prefersPromotionalIcon: Bool = false,
        @ViewBuilder icon: () -> Icon
    ) where PlaceholderIcon == AutomaticProductPlaceholderIcon

##  Parameters

`productID`

    

The product identifier to load from the App Store.

`prefersPromotionalIcon`

    

A Boolean value that indicates whether to use the promotional image from the
App Store, if it’s available. If this value is `true` and a promotional image
for the product is available, the view displays it instead of the view you
provide in the `icon` parameter.

`icon`

    

A closure that returns the image the view displays when the system finishes
loading the product from the App Store.

## Discussion

The product view displays a placeholder icon until the system finishes loading
the product. After the product loads, the system uses the view you provide in
the `icon` parameter, by default. If `prefersPromotionalIcon` is `true` and
the product has a promotional image, the view displays the promotional image
as its icon instead of the provided view.

Tip

To gain more control over the image that decorates this view, use the
`init(id:icon:placeholderIcon:)` initializer. It receives a
`ProductIconPhase`, which enables you to supply an image for each phase of the
image-loading process.

## See Also

### Creating product views that load products

`init(id: Product.ID, prefersPromotionalIcon: Bool)`

Creates a view to load and merchandise an individual product from the App
Store.

`init(id: Product.ID, prefersPromotionalIcon: Bool, icon: () -> Icon,
placeholderIcon: () -> PlaceholderIcon)`

Creates a view to load an individual product from the App Store and
merchandise it using an image and a custom placeholder icon.

`init(id: Product.ID, icon: (ProductIconPhase) -> Icon, placeholderIcon: () ->
PlaceholderIcon)`

Creates a view to load an individual product from the App Store, and
merchandise it using its promotional image and a custom placeholder icon.

Initializer

# init(id:prefersPromotionalIcon:icon:placeholderIcon:)

Creates a view to load an individual product from the App Store and
merchandise it using an image and a custom placeholder icon.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    init(
        id productID: Product.ID,
        prefersPromotionalIcon: Bool = false,
        @ViewBuilder icon: () -> Icon,
        @ViewBuilder placeholderIcon: () -> PlaceholderIcon
    )

##  Parameters

`productID`

    

The product identifier to load from the App Store.

`prefersPromotionalIcon`

    

A Boolean value that indicates whether to use the promotional image from the
App Store, if it’s available. If this value is `true` and a promotional image
for the product is available, the view displays it instead of the view you
provide in the `icon` parameter.

`icon`

    

A closure that returns the image the view displays when the system
successfully finishes loading the product from the App Store.

`placeholderIcon`

    

A closure that returns the image that the view uses while the system loads the
product from the App Store.

## Discussion

The product view displays the custom `placeholderIcon` until the system
finishes loading the product. After the product loads, the system uses the
view you provide in the `icon` parameter by default. If
`prefersPromotionalIcon` is `true` and the product has a promotional image,
the view displays the promotional image as its image instead of the view that
`icon` provides.

The following code example shows how to create a product view using the `icon`
and a custom `placeholderIcon`:

Tip

To gain more control over the image that decorates this view, use the
`init(id:icon:placeholderIcon:)` initializer. It receives a
`ProductIconPhase`, which enables you to supply an image for each phase of the
image-loading process.

## See Also

### Creating product views that load products

`init(id: Product.ID, prefersPromotionalIcon: Bool)`

Creates a view to load and merchandise an individual product from the App
Store.

`init(id: Product.ID, prefersPromotionalIcon: Bool, icon: () -> Icon)`

Creates a view to load an individual product from the App Store and
merchandise it using a custom icon.

`init(id: Product.ID, icon: (ProductIconPhase) -> Icon, placeholderIcon: () ->
PlaceholderIcon)`

Creates a view to load an individual product from the App Store, and
merchandise it using its promotional image and a custom placeholder icon.

Initializer

# init(id:icon:placeholderIcon:)

Creates a view to load an individual product from the App Store, and
merchandise it using its promotional image and a custom placeholder icon.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    init(
        id productID: Product.ID,
        @ViewBuilder icon: @escaping (ProductIconPhase) -> Icon,
        @ViewBuilder placeholderIcon: () -> PlaceholderIcon
    )

##  Parameters

`productID`

    

The product identifier to load from the App Store.

`icon`

    

A closure that receives a `ProductIconPhase` as an input, which indicates the
state of the loading operation of the product’s promotional image, and returns
the view to display for the specified phase.

`placeholderIcon`

    

A closure that returns an icon to display until the system finishes loading
the product from the App Store.

## Discussion

The product view shows the `placeholderIcon` until the system finishes loading
the product. After the product finishes loading, the view asynchronously loads
and displays the product’s promotional image. Use the `ProductIconPhase` to
monitor the current loading state of the product’s promotional image.

If the product is unavailable, the view displays the `placeholderIcon` as a
fallback.

The `ProductIconPhase` value indicates whether the promotional image is
loading, unavailable, or whether it succeeded or failed to load. Use the phase
to decide what to draw. While the image’s loading operation is in the
`ProductIconPhase.loading` phase, consider displaying the same view that you
provide in the `placeholderIcon` closure. For more information, see
`ProductIconPhase`.

## See Also

### Creating product views that load products

`init(id: Product.ID, prefersPromotionalIcon: Bool)`

Creates a view to load and merchandise an individual product from the App
Store.

`init(id: Product.ID, prefersPromotionalIcon: Bool, icon: () -> Icon)`

Creates a view to load an individual product from the App Store and
merchandise it using a custom icon.

`init(id: Product.ID, prefersPromotionalIcon: Bool, icon: () -> Icon,
placeholderIcon: () -> PlaceholderIcon)`

Creates a view to load an individual product from the App Store and
merchandise it using an image and a custom placeholder icon.

Initializer

# init(_:prefersPromotionalIcon:icon:)

Creates a view to merchandise an individual product using a custom icon.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    init(
        _ product: Product,
        prefersPromotionalIcon: Bool = false,
        @ViewBuilder icon: () -> Icon
    ) where PlaceholderIcon == EmptyView

##  Parameters

`product`

    

The product to merchandise.

`prefersPromotionalIcon`

    

A Boolean value that indicates whether to use the promotional image from the
App Store, if it’s available. If this value is `true` and a promotional image
for the product is available, the view displays it instead of the view you
provide in the `icon` parameter.

`icon`

    

A closure that returns the image to use for decorating the in-app purchase
product.

## Discussion

If `prefersPromotionalIcon` is `true` and the product has a promotional image,
the view displays the promotional image instead of the view you provide in
`icon`.

The following example shows how to create a product view using a custom icon:

Tip

To gain more control over the image that decorates this view, use the
`init(_:icon:)` initializer. It receives a `ProductIconPhase`, which enables
you to supply an image for each phase of the image-loading process.

## See Also

### Creating product views with preloaded products

`init(Product, prefersPromotionalIcon: Bool)`

Creates a view to merchandise an individual product.

`init(Product, icon: (ProductIconPhase) -> Icon)`

Creates a view to display a product that the system already loaded from the
App Store, and merchandise it using its promotional image.

Initializer

# init(_:prefersPromotionalIcon:)

Creates a view to merchandise an individual product.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    init(
        _ product: Product,
        prefersPromotionalIcon: Bool = true
    ) where Icon == EmptyView, PlaceholderIcon == EmptyView

##  Parameters

`product`

    

The product to merchandise.

`prefersPromotionalIcon`

    

A Boolean value that indicates whether to use the promotional image from the
App Store, if it’s available. If this value is `true` and a promotional image
for the product is available, the view displays it.

## Discussion

If the product has a promotional image available, the view displays it.
Otherwise, the view doesn’t show an image.

If you set the `prefersPromotionalIcon` parameter to `false`, the view doesn’t
show an image even if the product has a promotional image available.

Tip

To gain more control over the image that decorates this view, use the
`init(_:icon:)` initializer. It receives a `ProductIconPhase`, which enables
you to supply an image for each phase of the image-loading process.

## See Also

### Creating product views with preloaded products

`init(Product, prefersPromotionalIcon: Bool, icon: () -> Icon)`

Creates a view to merchandise an individual product using a custom icon.

`init(Product, icon: (ProductIconPhase) -> Icon)`

Creates a view to display a product that the system already loaded from the
App Store, and merchandise it using its promotional image.

Initializer

# init(_:icon:)

Creates a view to display a product that the system already loaded from the
App Store, and merchandise it using its promotional image.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    init(
        _ product: Product,
        @ViewBuilder icon: @escaping (ProductIconPhase) -> Icon
    ) where PlaceholderIcon == EmptyView

##  Parameters

`product`

    

The product to merchandise.

`icon`

    

A closure that receives a `ProductIconPhase` as an input, which indicates the
state of the loading operation of the product’s promoted image, and returns
the view to display for the specified phase.

## Discussion

The product view asynchronously loads and displays the product’s promotional
image.

The `ProductIconPhase` value indicates whether the promotional image is
loading, unavailable, or whether it succeeded or failed to load. Use the
`ProductIconPhase` to monitor current loading phase, and to decide the image
to return in the `icon` closure.

## See Also

### Creating product views with preloaded products

`init(Product, prefersPromotionalIcon: Bool, icon: () -> Icon)`

Creates a view to merchandise an individual product using a custom icon.

`init(Product, prefersPromotionalIcon: Bool)`

Creates a view to merchandise an individual product.

Initializer

# init(_:)

Creates a view to merchandise an individual product using a configuration for
product view style.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    init(_ configuration: ProductViewStyleConfiguration) where Icon == ProductViewStyleConfiguration.Icon, PlaceholderIcon == ProductViewStyleConfiguration.Icon

##  Parameters

`configuration`

    

A configuration for a product view style.

## Discussion

Use this initializer within the `makeBody(configuration:)` method of a
`ProductViewStyle` to create an instance of the product view you want to
style. This is useful for custom product view styles that modify the current
style, rather than implementing a new style.

The following code example shows how to create and use custom styles by
composing standard styles:

## See Also

### Creating product views with a configuration

`struct AutomaticProductPlaceholderIcon`

A view that represents the default placeholder icon for an in-app store
product.

Instance Method

# inAppPurchaseOptions(_:)

Adds a function the system calls before it processes a purchase from a product
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

## Discussion

When you provide purchase options ( `Product.PurchaseOption` ), the view adds
default purchase options to your options. These default purchase options may,
in some cases, override your purchase options. For example, the default
options sets the quantity to 1, because the product view always displays
prices based on a single item.

The product view uses the purchase options to configure the purchase.

If you want an in-app purchase to begin without adding purchase options, add
an action using `onInAppPurchaseStart(perform:)` instead.

You can remove any options that ancestor views may add by providing `nil` for
the `option` parameter, which results in the purchase having the default set
of purchase options.

## See Also

### Responding to store events

`func onInAppPurchaseStart(perform: ((Product) -> ())?) -> View`

Adds an action to perform when a person uses the purchase button for a product
within the view.

`func onInAppPurchaseCompletion(perform: ((Product,
Result<Product.PurchaseResult, any Error>) -> ())?) -> View`

Adds an action to perform when a purchase the person initiates from within a
product view completes.

`enum EntitlementTaskState`

The state of an entitlement task.

Instance Method

# onInAppPurchaseStart(perform:)

Adds an action to perform when a person uses the purchase button for a product
within the view.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    func onInAppPurchaseStart(perform action: ((Product) async -> ())?) -> some View

##  Parameters

`action`

    

A closure that defines an action to perform, including the product the person
intends to purchase as a parameter.

## Discussion

Set the `action` parameter to `nil` to remove any actions that ancestor views
may add.

## See Also

### Responding to store events

`func inAppPurchaseOptions(((Product) -> Set<Product.PurchaseOption>)?) ->
View`

Adds a function the system calls before it processes a purchase from a product
view, which provides a set of purchase options.

`func onInAppPurchaseCompletion(perform: ((Product,
Result<Product.PurchaseResult, any Error>) -> ())?) -> View`

Adds an action to perform when a purchase the person initiates from within a
product view completes.

`enum EntitlementTaskState`

The state of an entitlement task.

Instance Method

# onInAppPurchaseCompletion(perform:)

Adds an action to perform when a purchase the person initiates from within a
product view completes.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    func onInAppPurchaseCompletion(perform action: ((Product, Result<Product.PurchaseResult, any Error>) async -> ())?) -> some View

##  Parameters

`action`

    

A closure that defines action to perform, including the product value and the
purchase result as parameters.

## Discussion

By default, `updates` in `Transaction` emits transactions from successful in-
app store view purchases. If the purchase fails with an error, the system
displays an alert. You can revert a view to this behavior by setting the
`action` parameter to `nil`.

Each purchase performs only one action. Descendant views can override the
action by using another `onInAppPurchaseCompletion(perform:)` modifier.

## See Also

### Responding to store events

`func inAppPurchaseOptions(((Product) -> Set<Product.PurchaseOption>)?) ->
View`

Adds a function the system calls before it processes a purchase from a product
view, which provides a set of purchase options.

`func onInAppPurchaseStart(perform: ((Product) -> ())?) -> View`

Adds an action to perform when a person uses the purchase button for a product
within the view.

`enum EntitlementTaskState`

The state of an entitlement task.

Instance Method

# productViewStyle(_:)

Sets the style for in-app purchase product views within a view.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    func productViewStyle(_ style: some ProductViewStyle) -> some View

##  Parameters

`style`

    

The style to apply to the in-app purchase product views within the view.

## Discussion

This modifier styles any `ProductView` or `StoreView` instances within a view.

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

### Implementing a product view

`typealias ProductView.Body`

The type of view that represents the body of the product view.

Type Alias

# ProductView.Body

The type of view that represents the body of the product view.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    typealias ProductView<Icon, PlaceholderIcon>.Body = some View

## Relationships

### From Protocol

  * `View`

## See Also

### Implementing a product view

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

