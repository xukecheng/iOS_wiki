Instance Method

# callAsFunction()

Tells StoreKit to ask the user to rate or review your app, if appropriate.

StoreKit  SwiftUI  iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+
visionOS 1.0+  Xcode 14.0+

    
    
    @MainActor
    func callAsFunction()

## Discussion

Don’t call this method directly. SwiftUI calls it when you call the
`RequestReviewAction` instance that you get from the `requestReview`
environment value.

For information about how Swift uses the `callAsFunction()`method to simplify
call site syntax, see Methods with Special Names in _The Swift Programming
Language_.

Instance Property

# requestReview

StoreKit  SwiftUI  iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+
visionOS 1.0+

    
    
    @MainActor
    var requestReview: RequestReviewAction { get }

## See Also

### StoreKit configuration

`var displayStoreKitMessage: DisplayMessageAction`

Instance Method

# callAsFunction()

Tells StoreKit to ask the user to rate or review your app, if appropriate.

StoreKit  SwiftUI  iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+
visionOS 1.0+  Xcode 14.0+

    
    
    @MainActor
    func callAsFunction()

## Discussion

Don’t call this method directly. SwiftUI calls it when you call the
`RequestReviewAction` instance that you get from the `requestReview`
environment value.

For information about how Swift uses the `callAsFunction()`method to simplify
call site syntax, see Methods with Special Names in _The Swift Programming
Language_.

Instance Property

# requestReview

StoreKit  SwiftUI  iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+
visionOS 1.0+

    
    
    @MainActor
    var requestReview: RequestReviewAction { get }

## See Also

### StoreKit configuration

`var displayStoreKitMessage: DisplayMessageAction`

