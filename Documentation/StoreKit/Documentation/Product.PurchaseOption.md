Type Method

# appAccountToken(_:)

Sets a UUID to associate the purchase with an account in your system.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func appAccountToken(_ token: UUID) -> Product.PurchaseOption

##  Parameters

`token`

    

A UUID you provide to associate with the purchase.

## Return Value

An instance of `Product.PurchaseOption` to use in `purchase(options:)`.

## Discussion

When you set the app account token in the purchase options, the App Store
returns the same app account token value in the resulting transaction, in
`appAccountToken`.

## See Also

### Setting the purchase options

`static func onStorefrontChange(shouldContinuePurchase: (Storefront) -> Bool)
-> Product.PurchaseOption`

Indicates whether a transaction needs to continue if the App Store storefront
changes on the device during the transaction.

`static func promotionalOffer(offerID: String, keyID: String, nonce: UUID,
signature: Data, timestamp: Int) -> Product.PurchaseOption`

Applies a promotional offer for an auto-renewable subscription.

`static func quantity(Int) -> Product.PurchaseOption`

Indicates the quantity of items the customer is purchasing.

Type Method

# onStorefrontChange(shouldContinuePurchase:)

Indicates whether a transaction needs to continue if the App Store storefront
changes on the device during the transaction.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    @preconcurrency
    static func onStorefrontChange(shouldContinuePurchase: @escaping @Sendable (Storefront) -> Bool) -> Product.PurchaseOption

##  Parameters

`shouldContinuePurchase`

    

A closure that returns a Boolean value to indicate whether the purchase needs
to continue when the App Store storefront changes to the `storefront` value
during a transaction.

## Return Value

`Product.PurchaseOption`

## Discussion

The default value is `true` if this option isn’t added to the purchase.

## See Also

### Setting the purchase options

`static func appAccountToken(UUID) -> Product.PurchaseOption`

Sets a UUID to associate the purchase with an account in your system.

`static func promotionalOffer(offerID: String, keyID: String, nonce: UUID,
signature: Data, timestamp: Int) -> Product.PurchaseOption`

Applies a promotional offer for an auto-renewable subscription.

`static func quantity(Int) -> Product.PurchaseOption`

Indicates the quantity of items the customer is purchasing.

Type Method

# promotionalOffer(offerID:keyID:nonce:signature:timestamp:)

Applies a promotional offer for an auto-renewable subscription.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func promotionalOffer(
        offerID: String,
        keyID: String,
        nonce: UUID,
        signature: Data,
        timestamp: Int
    ) -> Product.PurchaseOption

##  Parameters

`offerID`

    

The subscription-offer identifier, `id`.

`keyID`

    

The key ID of the subscription key.

`nonce`

    

The anti-replay value used in the signature. Use lowercase.

`signature`

    

The cryptographic signature of the offer parameters, which you generate on
your server.

`timestamp`

    

The UNIX time, in milliseconds, when you generate the signature.

## Return Value

An instance of `Product.PurchaseOption` to use in `purchase(options:)`.

## Discussion

For information about `keyID`, `nonce`, `signature`, and `timestamp`, see
Generating a signature for promotional offers. If you’re providing an
`appAccountToken(_:)` in the purchase options, you must include that value
when you generate the `signature`. Use lowercase for the UUID string
representations of the app account token and the `nonce` in the signature.

You can offer a discounted or free period of service for auto-renewable
subscriptions on iOS, iPadOS, macOS, and tvOS using promotional offers. Before
you can provide promotional offers in your app, you must set up the offers in
your App Store Connect account. To configure your offer, see Set up
promotional offers for auto-renewable subscriptions.

## See Also

### Setting the purchase options

`static func appAccountToken(UUID) -> Product.PurchaseOption`

Sets a UUID to associate the purchase with an account in your system.

`static func onStorefrontChange(shouldContinuePurchase: (Storefront) -> Bool)
-> Product.PurchaseOption`

Indicates whether a transaction needs to continue if the App Store storefront
changes on the device during the transaction.

`static func quantity(Int) -> Product.PurchaseOption`

Indicates the quantity of items the customer is purchasing.

Type Method

# quantity(_:)

Indicates the quantity of items the customer is purchasing.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func quantity(_ quantity: Int) -> Product.PurchaseOption

##  Parameters

`quantity`

    

The number of items the customer is purchasing.

The default value is 1. The maximum value is 10.

## Return Value

An instance of `Product.PurchaseOption` to use in `purchase(options:)`.

## Discussion

The quantity applies to consumable in-app purchases and non-renewing
subscriptions.

## See Also

### Setting the purchase options

`static func appAccountToken(UUID) -> Product.PurchaseOption`

Sets a UUID to associate the purchase with an account in your system.

`static func onStorefrontChange(shouldContinuePurchase: (Storefront) -> Bool)
-> Product.PurchaseOption`

Indicates whether a transaction needs to continue if the App Store storefront
changes on the device during the transaction.

`static func promotionalOffer(offerID: String, keyID: String, nonce: UUID,
signature: Data, timestamp: Int) -> Product.PurchaseOption`

Applies a promotional offer for an auto-renewable subscription.

Type Method

# purchaseDate(_:renewalBehavior:)

Sets the purchase date for the transaction in the testing environment, and
indicates the renewal behavior for an auto-renewable subscription.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS 10.0+  visionOS 1.0+
Xcode 15.0+

    
    
    static func purchaseDate(
        _ date: Date,
        renewalBehavior: Product.PurchaseOption.SubscriptionRenewalBehavior = .renewUntilNow
    ) -> Product.PurchaseOption

##  Parameters

`date`

    

The purchase date for the transaction. Specify a date in the past or the
current moment. Dates in the future aren’t valid.

`renewalBehavior`

    

The renewal behavior for the auto-renewable subscription in this transaction,
whether it renews continuously from the purchase date, or it cancels after the
first period. By default, the subscription renews.

## Discussion

Use this purchase option when you test your app in Xcode using StoreKit Test
and call `buyProduct(identifier:options:)`.

Use this purchase option to create useful transactions for your test cases.
For example, use a date in the past with the default `renewalBehavior` to
generate a full history of subscription renewals to test. Or, use a date in
the past with the
`Product.PurchaseOption.SubscriptionRenewalBehavior.cancelImmediately`
behavior to simulate an account of a customer who canceled their subscription.

## See Also

### Setting options for StoreKit Testing in Xcode

`enum Product.PurchaseOption.SubscriptionRenewalBehavior`

Renewal options for auto-renewable subscriptions that you purchase in the
testing environment.

`static func codeOffer(referenceName: String) -> Product.PurchaseOption`

Sets an offer code for the transaction in the testing environment.

`static func promotionalOffer(id: String) -> Product.PurchaseOption`

Sets a promotional offer for the transaction in the testing environment.

Type Method

# codeOffer(referenceName:)

Sets an offer code for the transaction in the testing environment.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS 10.0+  visionOS 1.0+
Xcode 15.0+

    
    
    static func codeOffer(referenceName: String) -> Product.PurchaseOption

##  Parameters

`referenceName`

    

The reference name of the offer code to apply to the transaction. You need to
set up offer codes in your StoreKit configuration file.

## Discussion

Use this purchase option when you test your app in Xcode using StoreKit Test
and call `buyProduct(identifier:options:)`.

Set up the offer codes to use in this call in your StoreKit configuration
file. For more information, see Setting up StoreKit Testing in Xcode.

When you apply this option, the purchase transaction simulates a customer
redeeming an offer code and includes the offer code you specify.

## See Also

### Setting options for StoreKit Testing in Xcode

`static func purchaseDate(Date, renewalBehavior:
Product.PurchaseOption.SubscriptionRenewalBehavior) -> Product.PurchaseOption`

Sets the purchase date for the transaction in the testing environment, and
indicates the renewal behavior for an auto-renewable subscription.

`enum Product.PurchaseOption.SubscriptionRenewalBehavior`

Renewal options for auto-renewable subscriptions that you purchase in the
testing environment.

`static func promotionalOffer(id: String) -> Product.PurchaseOption`

Sets a promotional offer for the transaction in the testing environment.

Type Method

# promotionalOffer(id:)

Sets a promotional offer for the transaction in the testing environment.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS 10.0+  visionOS 1.0+
Xcode 15.0+

    
    
    static func promotionalOffer(id identifier: String) -> Product.PurchaseOption

##  Parameters

`identifier`

    

The identifier of the promotional offer to apply to the transaction. You need
to set up identifiers in your StoreKit configuration file.

## Discussion

Use this purchase option when you test your app in Xcode using StoreKit Test
and call `buyProduct(identifier:options:)`.

Set up the promotional offer identifiers you use in this call in your StoreKit
configuration file. For more information, see Setting up StoreKit Testing in
Xcode.

When you apply this option, the purchase transaction simulates a customer
redeeming a promotional offer and includes the promotional offer you specify.

## See Also

### Setting options for StoreKit Testing in Xcode

`static func purchaseDate(Date, renewalBehavior:
Product.PurchaseOption.SubscriptionRenewalBehavior) -> Product.PurchaseOption`

Sets the purchase date for the transaction in the testing environment, and
indicates the renewal behavior for an auto-renewable subscription.

`enum Product.PurchaseOption.SubscriptionRenewalBehavior`

Renewal options for auto-renewable subscriptions that you purchase in the
testing environment.

`static func codeOffer(referenceName: String) -> Product.PurchaseOption`

Sets an offer code for the transaction in the testing environment.

Type Method

# simulatesAskToBuyInSandbox(_:)

Simulates an Ask to Buy scenario when testing your app in the sandbox
environment.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func simulatesAskToBuyInSandbox(_ simulateAskToBuy: Bool) -> Product.PurchaseOption

##  Parameters

`simulateAskToBuy`

    

Set to `true` to simulate a child’s account asking permission to make a
purchase.

## Return Value

An instance of `Product.PurchaseOption` to use in `purchase(options:)`.

## Discussion

For information about testing Ask to Buy scenarios, see Testing at all stages
of development with Xcode and the sandbox.

For information about purchases made using Ask to Buy, see Approve what kids
buy with Ask to Buy.

Type Method

# custom(key:value:)

Adds data for a custom key to a purchase.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func custom(
        key: String,
        value: Data
    ) -> Product.PurchaseOption

##  Parameters

`key`

    

The key for this custom option.

`value`

    

The data value you assign to this custom option.

## Discussion

Custom purchase options don’t have any effect and are reserved for future use.

## See Also

### Setting custom purchase options

`static func custom(key: String, value: String) -> Product.PurchaseOption`

Adds a string for a custom key to a purchase.

`static func custom(key: String, value: Bool) -> Product.PurchaseOption`

Adds a Boolean value for a custom key to a purchase.

`static func custom(key: String, value: Double) -> Product.PurchaseOption`

Adds a number for a custom key to a purchase.

Type Method

# custom(key:value:)

Adds a string for a custom key to a purchase.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func custom(
        key: String,
        value: String
    ) -> Product.PurchaseOption

##  Parameters

`key`

    

The key for this custom option.

`value`

    

The string value you assign to this custom option.

## Discussion

Custom purchase options don’t have any effect and are reserved for future use.

## See Also

### Setting custom purchase options

`static func custom(key: String, value: Data) -> Product.PurchaseOption`

Adds data for a custom key to a purchase.

`static func custom(key: String, value: Bool) -> Product.PurchaseOption`

Adds a Boolean value for a custom key to a purchase.

`static func custom(key: String, value: Double) -> Product.PurchaseOption`

Adds a number for a custom key to a purchase.

Type Method

# custom(key:value:)

Adds a Boolean value for a custom key to a purchase.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func custom(
        key: String,
        value: Bool
    ) -> Product.PurchaseOption

##  Parameters

`key`

    

The key for this custom option.

`value`

    

The Boolean value you assign to this custom option.

## Discussion

Custom purchase options don’t have any effect and are reserved for future use.

## See Also

### Setting custom purchase options

`static func custom(key: String, value: Data) -> Product.PurchaseOption`

Adds data for a custom key to a purchase.

`static func custom(key: String, value: String) -> Product.PurchaseOption`

Adds a string for a custom key to a purchase.

`static func custom(key: String, value: Double) -> Product.PurchaseOption`

Adds a number for a custom key to a purchase.

Type Method

# custom(key:value:)

Adds a number for a custom key to a purchase.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func custom(
        key: String,
        value: Double
    ) -> Product.PurchaseOption

##  Parameters

`key`

    

The key for this custom option.

`value`

    

The numerical value you assign to this custom option.

## Discussion

Custom purchase options don’t have any effect and are reserved for future use.

## See Also

### Setting custom purchase options

`static func custom(key: String, value: Data) -> Product.PurchaseOption`

Adds data for a custom key to a purchase.

`static func custom(key: String, value: String) -> Product.PurchaseOption`

Adds a string for a custom key to a purchase.

`static func custom(key: String, value: Bool) -> Product.PurchaseOption`

Adds a Boolean value for a custom key to a purchase.

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func != (lhs: Product.PurchaseOption, rhs: Product.PurchaseOption) -> Bool

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

### Comparing and hashing purchase options

`static func == (Product.PurchaseOption, Product.PurchaseOption) -> Bool`

Returns a Boolean value that indicates whether two values are equal.

`func hash(into: inout Hasher)`

Hashes the essential components of this value by feeding them into the given
hasher.

`var hashValue: Int`

The hash value.

Operator

# ==(_:_:)

Returns a Boolean value that indicates whether two values are equal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func == (a: Product.PurchaseOption, b: Product.PurchaseOption) -> Bool

## See Also

### Comparing and hashing purchase options

`static func != (Product.PurchaseOption, Product.PurchaseOption) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`func hash(into: inout Hasher)`

Hashes the essential components of this value by feeding them into the given
hasher.

`var hashValue: Int`

The hash value.

Instance Method

# hash(into:)

Hashes the essential components of this value by feeding them into the given
hasher.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    func hash(into hasher: inout Hasher)

##  Parameters

`hasher`

    

The hasher to use when combining the components of this instance.

## Relationships

### From Protocol

  * `Hashable`

## See Also

### Comparing and hashing purchase options

`static func != (Product.PurchaseOption, Product.PurchaseOption) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (Product.PurchaseOption, Product.PurchaseOption) -> Bool`

Returns a Boolean value that indicates whether two values are equal.

`var hashValue: Int`

The hash value.

Instance Property

# hashValue

The hash value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var hashValue: Int { get }

## Relationships

### From Protocol

  * `Hashable`

## See Also

### Comparing and hashing purchase options

`static func != (Product.PurchaseOption, Product.PurchaseOption) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (Product.PurchaseOption, Product.PurchaseOption) -> Bool`

Returns a Boolean value that indicates whether two values are equal.

`func hash(into: inout Hasher)`

Hashes the essential components of this value by feeding them into the given
hasher.

Instance Property

# debugDescription

A debug description of the purchase option.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var debugDescription: String { get }

## Relationships

### From Protocol

  * `CustomDebugStringConvertible`

Type Method

# promotionalOffer(offerID:signature:)

iOS 17.4+  iPadOS 17.4+  macOS 14.4+  Mac Catalyst 17.4+  tvOS 17.4+  watchOS
10.4+  visionOS 1.1+  Xcode 15.3+

    
    
    static func promotionalOffer(
        offerID: String,
        signature: Product.SubscriptionOffer.Signature
    ) -> Product.PurchaseOption

