Initializer

# init(product:)

Returns a new payment for the specified product.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    convenience init(product: SKProduct)

##  Parameters

`product`

    

The product the user wishes to purchase.

## Return Value

A new payment object.

## Discussion

This Object creation uses the `productIdentifier` property obtained from the
`product` parameter to create and return a new payment with that identifier.
The quantity property defaults to `1`.

To create a `SKPayment` object with a quantity greater than `1`, create a
`SKMutablePayment` object, adjust its `quantity` property and then add it to
the payment queue.

## See Also

### Related Documentation

In-App Purchase Programming Guide

Instance Property

# productIdentifier

A string used to identify a product that can be purchased from within your
app.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    var productIdentifier: String { get }

## Discussion

The product identifier is a string previously agreed on between your app and
the Apple App Store.

## See Also

### Getting Payment Details

`var quantity: Int`

The number of items the user wants to purchase.

`var requestData: Data?`

Reserved for future use.

`var applicationUsername: String?`

A string that associates the transaction with a user account on your service.

Instance Property

# quantity

The number of items the user wants to purchase.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    var quantity: Int { get }

## Discussion

The default value is 1, the minimum value is 1, and the maximum value is 10.

## See Also

### Getting Payment Details

`var productIdentifier: String`

A string used to identify a product that can be purchased from within your
app.

`var requestData: Data?`

Reserved for future use.

`var applicationUsername: String?`

A string that associates the transaction with a user account on your service.

Instance Property

# requestData

Reserved for future use.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    var requestData: Data? { get }

## Discussion

The default value is `nil`. If `requestData` is not `nil`, your payment
request will be rejected.

## See Also

### Getting Payment Details

`var productIdentifier: String`

A string used to identify a product that can be purchased from within your
app.

`var quantity: Int`

The number of items the user wants to purchase.

`var applicationUsername: String?`

A string that associates the transaction with a user account on your service.

Instance Property

# applicationUsername

A string that associates the transaction with a user account on your service.

iOS 7.0+  iPadOS 7.0+  macOS 10.9+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    var applicationUsername: String? { get }

## Discussion

For more information on how to set and use this property, see
`applicationUsername`.

## See Also

### Getting Payment Details

`var productIdentifier: String`

A string used to identify a product that can be purchased from within your
app.

`var quantity: Int`

The number of items the user wants to purchase.

`var requestData: Data?`

Reserved for future use.

Instance Property

# simulatesAskToBuyInSandbox

A Boolean value that produces an "ask to buy" flow for this payment in the
sandbox.

iOS 8.3+  iPadOS 8.3+  macOS 10.14+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    var simulatesAskToBuyInSandbox: Bool { get }

Instance Property

# paymentDiscount

The details of the discount offer to apply to the payment.

iOS 12.2+  iPadOS 12.2+  macOS 10.14.4+  Mac Catalyst 13.1+  tvOS 12.2+
watchOS 6.2+  visionOS 1.0+

    
    
    @NSCopying
    var paymentDiscount: SKPaymentDiscount? { get }

## See Also

### Getting Discount Details

`class SKPaymentDiscount`

The signed discount to apply to a payment.

