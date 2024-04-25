Instance Property

# id

The product identifier of the promoted in-app purchase that the user selects
to purchase on the App Store.

iOS 16.4+  iPadOS 16.4+  macOS 14.4+  Mac Catalyst 16.4+  Xcode 14.3+

    
    
    var id: Product.ID { get }

## See Also

### Identifying the product

`let product: Product`

The product information of the promoted in-app purchase the user selects to
purchase on the App Store.

Instance Property

# product

The product information of the promoted in-app purchase the user selects to
purchase on the App Store.

iOS 16.4+  iPadOS 16.4+  macOS 14.4+  Mac Catalyst 16.4+  Xcode 14.3+

    
    
    let product: Product

## Discussion

To enable users to complete the purchase they start on the App Store, call
`purchase(options:)` on this product instance.

## See Also

### Identifying the product

`var id: Product.ID`

The product identifier of the promoted in-app purchase that the user selects
to purchase on the App Store.

Type Property

# intents

The asynchronous sequence that emits a purchase intent when the user selects a
promoted in-app purchase on the App Store.

iOS 16.4+  iPadOS 16.4+  macOS 14.4+  Mac Catalyst 16.4+  Xcode 14.3+

    
    
    static var intents: PurchaseIntent.PurchaseIntents { get }

## Discussion

When a user selects to purchase a promoted product on the App Store, your app
receives a purchase intent. Use the `product` object to complete your app’s
purchase workflow, including finishing the purchase, unlocking the product,
and any other workflow specific to your app.

The following example code receives the purchase intent, and calls a method to
complete the purchase workflow:

## See Also

### Getting purchase intents

`struct PurchaseIntent.PurchaseIntents`

An asynchronous sequence of purchase intents for in-app purchases that users
initiate on the App Store.

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 16.4+  iPadOS 16.4+  macOS 14.4+  Mac Catalyst 16.4+  Xcode 14.3+

    
    
    static func != (lhs: PurchaseIntent, rhs: PurchaseIntent) -> Bool

##  Parameters

`lhs`

    

A value to compare.

`rhs`

    

Another value to compare.

## Discussion

Inequality is the inverse of equality. For any values `a` and `b`, `a != b`
implies that `a == b` is `false`.

This is the default implementation of the not-equal-to operator (`!=`) for any
type that conforms to `Equatable`.

## See Also

### Comparing purchase intents

`static func == (PurchaseIntent, PurchaseIntent) -> Bool`

Returns a Boolean value that indicates whether two values are equal.

Operator

# ==(_:_:)

Returns a Boolean value that indicates whether two values are equal.

iOS 16.4+  iPadOS 16.4+  macOS 14.4+  Mac Catalyst 16.4+  Xcode 14.3+

    
    
    static func == (a: PurchaseIntent, b: PurchaseIntent) -> Bool

## See Also

### Comparing purchase intents

`static func != (PurchaseIntent, PurchaseIntent) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

