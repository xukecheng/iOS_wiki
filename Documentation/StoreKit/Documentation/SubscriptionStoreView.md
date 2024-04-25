Initializer

# init(groupID:visibleRelationships:)

Creates a view to load all subscriptions in a subscription group from the App
Store and merchandise them with automatic marketing content.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    init(
        groupID: String,
        visibleRelationships: Product.SubscriptionRelationship = .all
    ) where Content == AutomaticSubscriptionStoreMarketingContent

##  Parameters

`groupID`

    

The subscription group identifier to load from the App Store.

`visibleRelationships`

    

The kinds of subscription option relationships the view makes visible when
someone is already subscribed to the subscription.

## See Also

### Creating subscription store views with subscription group IDs

`init(groupID: String, visibleRelationships: Product.SubscriptionRelationship,
marketingContent: () -> (Content))`

Creates a view to load all the subscriptions in a subscription group from the
App Store and merchandise them with custom marketing content.

`struct AutomaticSubscriptionStoreMarketingContent`

A view that represents the default marketing content for a subscription store.

Initializer

# init(groupID:visibleRelationships:marketingContent:)

Creates a view to load all the subscriptions in a subscription group from the
App Store and merchandise them with custom marketing content.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    init(
        groupID: String,
        visibleRelationships: Product.SubscriptionRelationship = .all,
        @ViewBuilder marketingContent: () -> (Content)
    )

##  Parameters

`groupID`

    

The subscription group identifier to load from the App Store.

`visibleRelationships`

    

The kinds of subscription option relationships the view makes visible when
someone is already subscribed to the subscription.

`marketingContent`

    

The view that contains marketing content, to display above the store controls.

## See Also

### Creating subscription store views with subscription group IDs

`init(groupID: String, visibleRelationships:
Product.SubscriptionRelationship)`

Creates a view to load all subscriptions in a subscription group from the App
Store and merchandise them with automatic marketing content.

`struct AutomaticSubscriptionStoreMarketingContent`

A view that represents the default marketing content for a subscription store.

Initializer

# init(productIDs:)

Creates a view to load a collection of subscriptions and merchandise them with
automatic marketing content.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    init(productIDs: some Collection<String>) where Content == AutomaticSubscriptionStoreMarketingContent

##  Parameters

`productIDs`

    

The product identifiers to load from the App Store.

## See Also

### Creating subscription store views with product IDs

`init(productIDs: some Collection<String>, marketingContent: () -> (Content))`

Creates a view to load a collection of subscriptions from the App Store and
merchandise them with custom marketing content.

Initializer

# init(productIDs:marketingContent:)

Creates a view to load a collection of subscriptions from the App Store and
merchandise them with custom marketing content.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    init(
        productIDs: some Collection<String>,
        @ViewBuilder marketingContent: () -> (Content)
    )

##  Parameters

`productIDs`

    

The product identifiers to load from the App Store.

`marketingContent`

    

The view that contains marketing content, to display above the store controls.

## See Also

### Creating subscription store views with product IDs

`init(productIDs: some Collection<String>)`

Creates a view to load a collection of subscriptions and merchandise them with
automatic marketing content.

Initializer

# init(subscriptions:)

Creates a view to display a collection of subscription options and merchandise
them with automatic marketing content.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    init(subscriptions: some Collection<Product>) where Content == AutomaticSubscriptionStoreMarketingContent

##  Parameters

`subscriptions`

    

A collection of auto-renewable subscription `Product` instances to
merchandise. The auto-renewable subscriptions need to belong to the same
subscription group.

## See Also

### Creating subscription store views with preloaded subscriptions

`init(subscriptions: some Collection<Product>, marketingContent: () ->
(Content))`

Creates a view to display a collection of subscription options and merchandise
them with custom marketing content.

Initializer

# init(subscriptions:marketingContent:)

Creates a view to display a collection of subscription options and merchandise
them with custom marketing content.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    init(
        subscriptions: some Collection<Product>,
        @ViewBuilder marketingContent: () -> (Content)
    )

##  Parameters

`subscriptions`

    

A collection of auto-renewable subscription `Product` instances to
merchandise. The auto-renewable subscriptions need to belong to the same
subscription group.

`marketingContent`

    

A view that contains marketing content, to display above the store controls.

## See Also

### Creating subscription store views with preloaded subscriptions

`init(subscriptions: some Collection<Product>)`

Creates a view to display a collection of subscription options and merchandise
them with automatic marketing content.

Instance Method

# inAppPurchaseOptions(_:)

Adds a function the system calls before it processes a purchase from a store
view, which provides a set of purchase options.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    func inAppPurchaseOptions(_ options: ((Product) async -> Set<Product.PurchaseOption>)?) -> some View

## See Also

### Responding to store events

`func onInAppPurchaseStart(perform: ((Product) -> ())?) -> View`

Adds an action to perform when a person uses the purchase button for a product
within the view.

`func onInAppPurchaseCompletion(perform: ((Product,
Result<Product.PurchaseResult, any Error>) -> ())?) -> View`

Adds an action to perform when a purchase the person initiates from within a
product view completes.

`func subscriptionStoreSignInAction((() -> ())?) -> View`

Add an action to perform when a person uses the sign-in button on a
subscription store view within the view.

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

Adds a function the system calls before it processes a purchase from a store
view, which provides a set of purchase options.

`func onInAppPurchaseCompletion(perform: ((Product,
Result<Product.PurchaseResult, any Error>) -> ())?) -> View`

Adds an action to perform when a purchase the person initiates from within a
product view completes.

`func subscriptionStoreSignInAction((() -> ())?) -> View`

Add an action to perform when a person uses the sign-in button on a
subscription store view within the view.

`enum EntitlementTaskState`

The state of an entitlement task.

Instance Method

# onInAppPurchaseCompletion(perform:)

Adds an action to perform when a purchase the person initiates from within a
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

Adds an action to perform when a person uses the purchase button for a product
within the view.

`func subscriptionStoreSignInAction((() -> ())?) -> View`

Add an action to perform when a person uses the sign-in button on a
subscription store view within the view.

`enum EntitlementTaskState`

The state of an entitlement task.

Instance Method

# subscriptionStoreSignInAction(_:)

Add an action to perform when a person uses the sign-in button on a
subscription store view within the view.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    func subscriptionStoreSignInAction(_ action: (() -> ())?) -> some View

## See Also

### Responding to store events

`func inAppPurchaseOptions(((Product) -> Set<Product.PurchaseOption>)?) ->
View`

Adds a function the system calls before it processes a purchase from a store
view, which provides a set of purchase options.

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

# subscriptionStoreControlIcon(icon:)

Sets a view to use to decorate individual subscription options within a
subscription store view.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    func subscriptionStoreControlIcon(@ViewBuilder icon: @escaping (Product, Product.SubscriptionInfo) -> some View) -> some View

##  Parameters

`icon`

    

A closure that takes a `Product` and `Product.SubscriptionInfo` and returns a
view.

## Discussion

You can adjust this view to provide a different appearance for each
subscription option.

## See Also

### Configuring subscription store view controls

`func subscriptionStorePickerItemBackground(some ShapeStyle) -> View`

Sets the background style for picker items of the subscription store view
instances within a view.

`func subscriptionStoreButtonLabel(SubscriptionStoreButtonLabel) -> View`

Configures the subscription store views within a view to use a specified
button label.

`struct SubscriptionStoreButtonLabel`

The label of the subscribe button that a subscription store view uses.

`func subscriptionStoreControlStyle(some SubscriptionStoreControlStyle) ->
View`

Sets the control style for subscription store views within a view.

Instance Method

# subscriptionStorePickerItemBackground(_:)

Sets the background style for picker items of the subscription store view
instances within a view.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    func subscriptionStorePickerItemBackground(_ backgroundStyle: some ShapeStyle) -> some View

## See Also

### Configuring subscription store view controls

`func subscriptionStoreControlIcon(icon: (Product, Product.SubscriptionInfo)
-> some View) -> View`

Sets a view to use to decorate individual subscription options within a
subscription store view.

`func subscriptionStoreButtonLabel(SubscriptionStoreButtonLabel) -> View`

Configures the subscription store views within a view to use a specified
button label.

`struct SubscriptionStoreButtonLabel`

The label of the subscribe button that a subscription store view uses.

`func subscriptionStoreControlStyle(some SubscriptionStoreControlStyle) ->
View`

Sets the control style for subscription store views within a view.

Instance Method

# subscriptionStoreButtonLabel(_:)

Configures the subscription store views within a view to use a specified
button label.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    func subscriptionStoreButtonLabel(_ label: SubscriptionStoreButtonLabel) -> some View

## See Also

### Configuring subscription store view controls

`func subscriptionStoreControlIcon(icon: (Product, Product.SubscriptionInfo)
-> some View) -> View`

Sets a view to use to decorate individual subscription options within a
subscription store view.

`func subscriptionStorePickerItemBackground(some ShapeStyle) -> View`

Sets the background style for picker items of the subscription store view
instances within a view.

`struct SubscriptionStoreButtonLabel`

The label of the subscribe button that a subscription store view uses.

`func subscriptionStoreControlStyle(some SubscriptionStoreControlStyle) ->
View`

Sets the control style for subscription store views within a view.

Instance Method

# subscriptionStoreControlStyle(_:)

Sets the control style for subscription store views within a view.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    func subscriptionStoreControlStyle(_ style: some SubscriptionStoreControlStyle) -> some View

## Discussion

This view modifier set the style of controls for `SubscriptionStoreView`
instances within a view.

## See Also

### Configuring subscription store view controls

`func subscriptionStoreControlIcon(icon: (Product, Product.SubscriptionInfo)
-> some View) -> View`

Sets a view to use to decorate individual subscription options within a
subscription store view.

`func subscriptionStorePickerItemBackground(some ShapeStyle) -> View`

Sets the background style for picker items of the subscription store view
instances within a view.

`func subscriptionStoreButtonLabel(SubscriptionStoreButtonLabel) -> View`

Configures the subscription store views within a view to use a specified
button label.

`struct SubscriptionStoreButtonLabel`

The label of the subscribe button that a subscription store view uses.

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

### Adding accessory feature buttons

`struct StoreButtonKind`

A button to display in a store view or subscription store view.

Structure

# ContainerBackgroundPlacement

The placement of a container background.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct ContainerBackgroundPlacement

## Overview

This method controls where to place a background that you specify with the
`containerBackground(_:for:)` or `containerBackground(for:alignment:content:)`
modifier.

## Topics

### Getting placements

`static let navigation: ContainerBackgroundPlacement`

A background placement inside a `NavigationStack` or `NavigationSplitView`

`static let tabView: ContainerBackgroundPlacement`

A background placement inside a `TabView`.

`static let widget: ContainerBackgroundPlacement`

The container background placement for a widget.

### Getting StoreKit placements

`static var subscriptionStore: ContainerBackgroundPlacement`

A background placement inside a `SubscriptionStoreView`.

`static var subscriptionStoreFullHeight: ContainerBackgroundPlacement`

A background placement that spans the full height of a
`SubscriptionStoreView`.

`static var subscriptionStoreHeader: ContainerBackgroundPlacement`

A background placement inside the marketing content of a
`SubscriptionStoreView`

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Layering views

Adding a background to your view

Compose a background behind your view and extend it beyond the safe area
insets.

`struct ZStack`

A view that overlays its subviews, aligning them in both axes.

`func zIndex(Double) -> some View`

Controls the display order of overlapping views.

`func background<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify behind this view.

`func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to a style.

`func background(ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to the default background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with the default
background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with the default background
style.

`func overlay<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify in front of this view.

`func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Layers the specified style in front of this view.

`func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Layers a shape that you specify in front of this view.

`var backgroundMaterial: Material?`

The material underneath the current view.

`func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some
View`

Sets the container background of the enclosing container using a view.

`func containerBackground<V>(for: ContainerBackgroundPlacement, alignment:
Alignment, content: () -> V) -> some View`

Sets the container background of the enclosing container using a view.

Instance Method

# subscriptionStorePolicyDestination(for:destination:)

Configures a view as the destination for a policy button action in
subscription store views.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    func subscriptionStorePolicyDestination(
        for button: SubscriptionStorePolicyKind,
        @ViewBuilder destination: () -> some View
    ) -> some View

## See Also

### Configuring the subscription store policies

`func subscriptionStorePolicyDestination(url: URL, for:
SubscriptionStorePolicyKind) -> View`

Configures a URL as the destination for a policy button action in subscription
store views.

`func subscriptionStorePolicyForegroundStyle(some ShapeStyle) -> View`

Sets the style for the terms of service and privacy policy buttons within a
subscription store view.

`func subscriptionStorePolicyForegroundStyle(some ShapeStyle, some ShapeStyle)
-> View`

Sets the primary and secondary style for the terms of service and privacy
policy buttons within a subscription store view.

`struct SubscriptionStorePolicyKind`

The type of policy, such as the terms of service or privacy policies.

Instance Method

# subscriptionStorePolicyDestination(url:for:)

Configures a URL as the destination for a policy button action in subscription
store views.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    func subscriptionStorePolicyDestination(
        url: URL,
        for button: SubscriptionStorePolicyKind
    ) -> some View

## See Also

### Configuring the subscription store policies

`func subscriptionStorePolicyDestination(for: SubscriptionStorePolicyKind,
destination: () -> some View) -> View`

Configures a view as the destination for a policy button action in
subscription store views.

`func subscriptionStorePolicyForegroundStyle(some ShapeStyle) -> View`

Sets the style for the terms of service and privacy policy buttons within a
subscription store view.

`func subscriptionStorePolicyForegroundStyle(some ShapeStyle, some ShapeStyle)
-> View`

Sets the primary and secondary style for the terms of service and privacy
policy buttons within a subscription store view.

`struct SubscriptionStorePolicyKind`

The type of policy, such as the terms of service or privacy policies.

Instance Method

# subscriptionStorePolicyForegroundStyle(_:)

Sets the style for the terms of service and privacy policy buttons within a
subscription store view.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    func subscriptionStorePolicyForegroundStyle(_ style: some ShapeStyle) -> some View

## See Also

### Configuring the subscription store policies

`func subscriptionStorePolicyDestination(for: SubscriptionStorePolicyKind,
destination: () -> some View) -> View`

Configures a view as the destination for a policy button action in
subscription store views.

`func subscriptionStorePolicyDestination(url: URL, for:
SubscriptionStorePolicyKind) -> View`

Configures a URL as the destination for a policy button action in subscription
store views.

`func subscriptionStorePolicyForegroundStyle(some ShapeStyle, some ShapeStyle)
-> View`

Sets the primary and secondary style for the terms of service and privacy
policy buttons within a subscription store view.

`struct SubscriptionStorePolicyKind`

The type of policy, such as the terms of service or privacy policies.

Instance Method

# subscriptionStorePolicyForegroundStyle(_:_:)

Sets the primary and secondary style for the terms of service and privacy
policy buttons within a subscription store view.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    func subscriptionStorePolicyForegroundStyle(
        _ primary: some ShapeStyle,
        _ secondary: some ShapeStyle
    ) -> some View

## See Also

### Configuring the subscription store policies

`func subscriptionStorePolicyDestination(for: SubscriptionStorePolicyKind,
destination: () -> some View) -> View`

Configures a view as the destination for a policy button action in
subscription store views.

`func subscriptionStorePolicyDestination(url: URL, for:
SubscriptionStorePolicyKind) -> View`

Configures a URL as the destination for a policy button action in subscription
store views.

`func subscriptionStorePolicyForegroundStyle(some ShapeStyle) -> View`

Sets the style for the terms of service and privacy policy buttons within a
subscription store view.

`struct SubscriptionStorePolicyKind`

The type of policy, such as the terms of service or privacy policies.

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

### Implementing a subscription store view

`typealias SubscriptionStoreView.Body`

The type of view that represents the body of the subscription store view.

Type Alias

# SubscriptionStoreView.Body

The type of view that represents the body of the subscription store view.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    typealias SubscriptionStoreView<Content>.Body = some View

## Relationships

### From Protocol

  * `View`

## See Also

### Implementing a subscription store view

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

