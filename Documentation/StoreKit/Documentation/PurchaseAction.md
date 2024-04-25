Instance Method

# callAsFunction(_:options:)

Starts an in-app purchase for the indicated product and purchase options.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    func callAsFunction(
        _ product: Product,
        options: Set<Product.PurchaseOption> = []
    ) async throws -> Product.PurchaseResult

##  Parameters

`product`

    

The in-app purchase `Product` the customer is purchasing.

`options`

    

A set of options you may associate with the purchase
(`Product.PurchaseOption`).

## Return Value

The result of the purchase, `Product.PurchaseResult`.

## Discussion

Don’t call this method directly. SwiftUI calls it when you call the
`PurchaseAction` structure with the `product` and `options` as arguments.

This method may throw a `Product.PurchaseError` or `StoreKitError`.

For information about how Swift uses the `callAsFunction(_:options:)` method
to simplify call site syntax, see Methods with Special Names in _The Swift
Programming Language_.
