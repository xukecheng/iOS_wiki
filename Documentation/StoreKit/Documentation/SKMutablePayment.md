Instance Property

# productIdentifier

A string that identifies a product that can be purchased from within your app.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    var productIdentifier: String { get set }

## Discussion

The product identifier is a string previously agreed on between your app and
the Apple App Store.

## See Also

### Getting and Setting Attributes

`var quantity: Int`

The number of items the user wants to purchase.

`var requestData: Data?`

Reserved for future use.

`var applicationUsername: String?`

A string that associates the transaction with a user account on your service.

### Related Documentation

In-App Purchase Programming Guide

Instance Property

# quantity

The number of items the user wants to purchase.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    var quantity: Int { get set }

## Discussion

The quantity property must be greater than `0`.

## See Also

### Getting and Setting Attributes

`var productIdentifier: String`

A string that identifies a product that can be purchased from within your app.

`var requestData: Data?`

Reserved for future use.

`var applicationUsername: String?`

A string that associates the transaction with a user account on your service.

Instance Property

# requestData

Reserved for future use.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    var requestData: Data? { get set }

## Discussion

The default value is `nil`. If `requestData` is not `nil`, your payment will
be rejected by the Apple App Store.

## See Also

### Getting and Setting Attributes

`var productIdentifier: String`

A string that identifies a product that can be purchased from within your app.

`var quantity: Int`

The number of items the user wants to purchase.

`var applicationUsername: String?`

A string that associates the transaction with a user account on your service.

Instance Property

# applicationUsername

A string that associates the transaction with a user account on your service.

iOS 7.0+  iPadOS 7.0+  macOS 10.9+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    var applicationUsername: String? { get set }

## Discussion

Consider assigning a UUID to the `applicationUsername` property. When this
value is a UUID, the App Store server stores it as an `appAccountToken`. In
this scenario, the following happens:

  * In the App Store Server API, the `JWSTransactionDecodedPayload` object returns the `applicationUsername` value in the `appAccountToken` field.

  * In App Store Server Notifications, the `JWSTransactionDecodedPayload` object returns the `applicationUsername` value in the `appAccountToken` field. 

  * When you call the verifyReceipt endpoint to verify an App Store receipt, the App Store server returns the `applicationUsername` value in the `app_account_token` field of the `responseBody.Latest_receipt_info`.

The sample code below shows how to assign a UUID value to
`applicationUsername`. You may choose to generate the UUID on your server.
Assign the value before adding the payment to the payment queue.

If you don’t assign a UUID string value to `applicationUsername`, the App
Store server doesn’t persist the value. The value won’t appear in the
`app_account_token` fields in notifications or receipts.

Important

An `applicationUsername` property that isn’t a UUID isn’t guaranteed to
persist between the time when you add the payment transaction to the queue and
when the queue updates the transaction.

## See Also

### Getting and Setting Attributes

`var productIdentifier: String`

A string that identifies a product that can be purchased from within your app.

`var quantity: Int`

The number of items the user wants to purchase.

`var requestData: Data?`

Reserved for future use.

Instance Property

# simulatesAskToBuyInSandbox

A Boolean value that produces an “ask to buy” flow for this payment in the
sandbox.

iOS 8.3+  iPadOS 8.3+  macOS 10.14+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    var simulatesAskToBuyInSandbox: Bool { get set }

Instance Property

# paymentDiscount

The details of the discount offer to apply to the payment.

iOS 12.2+  iPadOS 12.2+  macOS 10.14.4+  Mac Catalyst 13.1+  tvOS 12.2+
watchOS 6.2+  visionOS 1.0+

    
    
    @NSCopying
    var paymentDiscount: SKPaymentDiscount? { get set }

