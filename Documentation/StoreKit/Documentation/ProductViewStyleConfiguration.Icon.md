Instance Property

# body

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    @MainActor
    var body: some View { get }

## Relationships

### From Protocol

  * `View`

## See Also

### Implementing product view style configurations

`typealias ProductViewStyleConfiguration.Icon.Body`

Type Alias

# ProductViewStyleConfiguration.Icon.Body

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    typealias ProductViewStyleConfiguration.Icon.Body = some View

## Relationships

### From Protocol

  * `View`

## See Also

### Implementing product view style configurations

`var body: View`

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

