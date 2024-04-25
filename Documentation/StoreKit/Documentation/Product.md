Generic Type Method

# products(for:)

Requests product data from the App Store.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func products<Identifiers>(for identifiers: Identifiers) async throws -> [Product] where Identifiers : Collection, Identifiers.Element == String

##  Parameters

`identifiers`

    

A collection of unique in-app purchase product identifiers that you previously
configured in App Store Connect. StoreKit ignores any duplicate identifiers in
the collection.

## Return Value

An array of products, returned from the App Store.

## Discussion

Use this method to get an instance of `Product`. Your app must have its
product identifiers available to provide them to this function. The following
example illustrates requesting two products using hard-coded identifiers.

You initially create product identifiers when you configure in-app purchases
in App Store Connect; for more information, see Create an in-app purchase.
Your app can store or retrieve product identifiers in several ways, such as
embedding the identifiers in the app bundle, or fetching them from your
server.

If any identifiers are invalid or the App Store can’t find them, the App Store
excludes them from the return value. The `products(for:)` function can throw a
`StoreKitError` for system-related errors.

Instance Property

# displayName

The localized display name of the product, if it exists.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let displayName: String

## Discussion

The storefront of the device determines the language of the display name, not
the preferred language set on the device. For more information, see
`Storefront`.

Note

When you create a new product in App Store Connect or in a StoreKit
configuration file, you can test it before you add a product localization. The
`displayName` value is an empty string until you add a localization. For more
information on localizations, see Add and remove localizations.

## See Also

### Displaying a product description and price

`let description: String`

The localized description of the product.

`let displayPrice: String`

The localized string representation of the product price, suitable for
display.

`let price: Decimal`

The decimal representation of the cost of the product, in local currency.

`@backDeployed(before: iOS 16.0, macOS 13.0, tvOS 16.0, watchOS 9.0,
macCatalyst 16.0) var priceFormatStyle: Decimal.FormatStyle.Currency`

The format style for the numbers in the price of the product.

`@backDeployed(before: iOS 16.0, macOS 13.0, tvOS 16.0, watchOS 9.0,
macCatalyst 16.0) var subscriptionPeriodFormatStyle:
Date.ComponentsFormatStyle`

The format style for the date components related to a subscription’s duration.

`var subscriptionPeriodUnitFormatStyle:
Product.SubscriptionPeriod.Unit.FormatStyle`

The format style for subscription period units, such as week, month, or year.

Instance Property

# description

The localized description of the product.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let description: String

## Discussion

The storefront of the device determines the language of the `description`, not
the preferred language set on the device. For more information, see
`Storefront`.

Note

When you create a new product in App Store Connect or in a StoreKit
configuration file, you can test it before you add a product localization. The
`description` value is an empty string until you add a localization. For more
information on localizations, see Add and remove localizations.

## See Also

### Displaying a product description and price

`let displayName: String`

The localized display name of the product, if it exists.

`let displayPrice: String`

The localized string representation of the product price, suitable for
display.

`let price: Decimal`

The decimal representation of the cost of the product, in local currency.

`@backDeployed(before: iOS 16.0, macOS 13.0, tvOS 16.0, watchOS 9.0,
macCatalyst 16.0) var priceFormatStyle: Decimal.FormatStyle.Currency`

The format style for the numbers in the price of the product.

`@backDeployed(before: iOS 16.0, macOS 13.0, tvOS 16.0, watchOS 9.0,
macCatalyst 16.0) var subscriptionPeriodFormatStyle:
Date.ComponentsFormatStyle`

The format style for the date components related to a subscription’s duration.

`var subscriptionPeriodUnitFormatStyle:
Product.SubscriptionPeriod.Unit.FormatStyle`

The format style for subscription period units, such as week, month, or year.

Instance Property

# displayPrice

The localized string representation of the product price, suitable for
display.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let displayPrice: String

## Discussion

Use this string to display the price, formatted for the locale. The storefront
that the user’s device is connected to determines the locale. For more
information, see `Storefront`.

To perform arithmetic calculations with the price, use the `price` property
instead.

## See Also

### Displaying a product description and price

`let displayName: String`

The localized display name of the product, if it exists.

`let description: String`

The localized description of the product.

`let price: Decimal`

The decimal representation of the cost of the product, in local currency.

`@backDeployed(before: iOS 16.0, macOS 13.0, tvOS 16.0, watchOS 9.0,
macCatalyst 16.0) var priceFormatStyle: Decimal.FormatStyle.Currency`

The format style for the numbers in the price of the product.

`@backDeployed(before: iOS 16.0, macOS 13.0, tvOS 16.0, watchOS 9.0,
macCatalyst 16.0) var subscriptionPeriodFormatStyle:
Date.ComponentsFormatStyle`

The format style for the date components related to a subscription’s duration.

`var subscriptionPeriodUnitFormatStyle:
Product.SubscriptionPeriod.Unit.FormatStyle`

The format style for subscription period units, such as week, month, or year.

Instance Property

# price

The decimal representation of the cost of the product, in local currency.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let price: Decimal

## Discussion

Use this property to perform arithmetic calculations with the price of the
product. For a localized string representation of the price to display to
customers, use the `displayPrice` property instead.

## See Also

### Displaying a product description and price

`let displayName: String`

The localized display name of the product, if it exists.

`let description: String`

The localized description of the product.

`let displayPrice: String`

The localized string representation of the product price, suitable for
display.

`@backDeployed(before: iOS 16.0, macOS 13.0, tvOS 16.0, watchOS 9.0,
macCatalyst 16.0) var priceFormatStyle: Decimal.FormatStyle.Currency`

The format style for the numbers in the price of the product.

`@backDeployed(before: iOS 16.0, macOS 13.0, tvOS 16.0, watchOS 9.0,
macCatalyst 16.0) var subscriptionPeriodFormatStyle:
Date.ComponentsFormatStyle`

The format style for the date components related to a subscription’s duration.

`var subscriptionPeriodUnitFormatStyle:
Product.SubscriptionPeriod.Unit.FormatStyle`

The format style for subscription period units, such as week, month, or year.

Instance Property

# priceFormatStyle

The format style for the numbers in the price of the product.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 16.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    @backDeployed(before: iOS 16.0, macOS 13.0, tvOS 16.0, watchOS 9.0, macCatalyst 16.0)
    var priceFormatStyle: Decimal.FormatStyle.Currency { get }

## Discussion

The `priceFormatStyle` value is a localized number suitable for display.

To display the `price` directly, rather than making calculations, use the
`displayPrice` string instead.

## See Also

### Displaying a product description and price

`let displayName: String`

The localized display name of the product, if it exists.

`let description: String`

The localized description of the product.

`let displayPrice: String`

The localized string representation of the product price, suitable for
display.

`let price: Decimal`

The decimal representation of the cost of the product, in local currency.

`@backDeployed(before: iOS 16.0, macOS 13.0, tvOS 16.0, watchOS 9.0,
macCatalyst 16.0) var subscriptionPeriodFormatStyle:
Date.ComponentsFormatStyle`

The format style for the date components related to a subscription’s duration.

`var subscriptionPeriodUnitFormatStyle:
Product.SubscriptionPeriod.Unit.FormatStyle`

The format style for subscription period units, such as week, month, or year.

Instance Property

# subscriptionPeriodFormatStyle

The format style for the date components related to a subscription’s duration.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 16.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    @backDeployed(before: iOS 16.0, macOS 13.0, tvOS 16.0, watchOS 9.0, macCatalyst 16.0)
    var subscriptionPeriodFormatStyle: Date.ComponentsFormatStyle { get }

## Discussion

Use this format style to format text that describes a subscription period,
including its length and unit, such as “1 week”, “2 months”, and so on.

## See Also

### Displaying a product description and price

`let displayName: String`

The localized display name of the product, if it exists.

`let description: String`

The localized description of the product.

`let displayPrice: String`

The localized string representation of the product price, suitable for
display.

`let price: Decimal`

The decimal representation of the cost of the product, in local currency.

`@backDeployed(before: iOS 16.0, macOS 13.0, tvOS 16.0, watchOS 9.0,
macCatalyst 16.0) var priceFormatStyle: Decimal.FormatStyle.Currency`

The format style for the numbers in the price of the product.

`var subscriptionPeriodUnitFormatStyle:
Product.SubscriptionPeriod.Unit.FormatStyle`

The format style for subscription period units, such as week, month, or year.

Instance Property

# subscriptionPeriodUnitFormatStyle

The format style for subscription period units, such as week, month, or year.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    var subscriptionPeriodUnitFormatStyle: Product.SubscriptionPeriod.Unit.FormatStyle { get }

## See Also

### Displaying a product description and price

`let displayName: String`

The localized display name of the product, if it exists.

`let description: String`

The localized description of the product.

`let displayPrice: String`

The localized string representation of the product price, suitable for
display.

`let price: Decimal`

The decimal representation of the cost of the product, in local currency.

`@backDeployed(before: iOS 16.0, macOS 13.0, tvOS 16.0, watchOS 9.0,
macCatalyst 16.0) var priceFormatStyle: Decimal.FormatStyle.Currency`

The format style for the numbers in the price of the product.

`@backDeployed(before: iOS 16.0, macOS 13.0, tvOS 16.0, watchOS 9.0,
macCatalyst 16.0) var subscriptionPeriodFormatStyle:
Date.ComponentsFormatStyle`

The format style for the date components related to a subscription’s duration.

Instance Method

# purchase(options:)

Initiates a purchase for the product with the App Store and displays the
confirmation sheet.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  Xcode 13.0+

    
    
    func purchase(options: Set<Product.PurchaseOption> = []) async throws -> Product.PurchaseResult

##  Parameters

`options`

    

A set of options you can associate with the purchase.

## Return Value

Returns a `Product.PurchaseResult`.

## Discussion

StoreKit provides several APIs you can use to enable customers to initiate a
purchase. Before using `purchase(options:)` consider the following APIs and
choose the one that best suits your app’s implementation:

  * Use `PurchaseAction` for apps that use SwiftUI, including multi-scene apps for visionOS.

  * Use `purchase(confirmIn:options:)` for apps that use UIKit.

  * Use `purchase(options:)` if your app runs on watchOS or macOS.

Important

If you use StoreKit views such as `ProductView`, `StoreView`, or
`SubscriptionStoreView` you don’t need to call any other API to initiate a
purchase. StoreKit manages the purchase action automatically, including
presenting the purchase confirmation UI. For more information, see StoreKit
views.

### Use the purchase API

Call the `purchase(options:)` method when a customer initiates a purchase,
either within your app or after selecting a promoted in-app purchase on the
App Store. This method brings up the system-confirmation sheet. The user can
confirm to complete the transaction or cancel it.

Include the purchase options to provide additional information about the
purchase, such as:

  * `appAccountToken(_:)` to associate the purchase with the resulting transaction

  * `promotionalOffer(offerID:keyID:nonce:signature:timestamp:)`, if the customer is redeeming a promotional offer for an auto-renewable subscription

  * `quantity(_:)`, if the customer is purchasing more than one of the product

The following example illustrates calling `purchase(options:)` using the
`options` parameter to provide an app account token:

If you’re testing your app in the sandbox environment, test an Ask to Buy
scenario by setting the `simulatesAskToBuyInSandbox(_:)` purchase option to
`true`. For more information about Ask to Buy, see Approve what kids buy with
Ask to Buy.

This method may throw a `Product.PurchaseError` or `StoreKitError`.

For more information about purchases that users initiate on the App Store, see
Promoting in-app purchases.

## See Also

### Purchasing a product

`func purchase(confirmIn: some UIScene, options: Set<Product.PurchaseOption>)
-> Product.PurchaseResult`

Initiates a purchase for the product with the App Store and displays the
confirmation sheet.

`struct Product.PurchaseOption`

Optional settings for a product purchase.

`enum Product.PurchaseResult`

The result of a purchase.

`enum Product.PurchaseError`

Error information for product purchase errors.

Instance Method

# purchase(confirmIn:options:)

Initiates a purchase for the product with the App Store and displays the
confirmation sheet.

iOS 17.0+  iPadOS 17.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS 1.0+  Xcode
15.0+

    
    
    func purchase(
        confirmIn scene: some UIScene,
        options: Set<Product.PurchaseOption> = []
    ) async throws -> Product.PurchaseResult

##  Parameters

`scene`

    

The `UIScene` the system uses to show the purchase confirmation UI.

`options`

    

A set of options (`Product.PurchaseOption`) you can associate with the
purchase.

## Return Value

The result of the purchase, `Product.PurchaseResult`.

## Discussion

StoreKit provides several APIs you can use to enable customers to initiate a
purchase. Before using `purchase(confirmIn:options:)`, consider the following
APIs and choose the one that best suits your app’s implementation:

  * Use `PurchaseAction` for apps that use SwiftUI, including multi-scene apps for visionOS.

  * Use `purchase(confirmIn:options:)` for apps that use UIKit.

  * Use `purchase(options:)` if your app runs on watchOS or macOS.

Important

If you use StoreKit views such as `ProductView`, `StoreView`, or
`SubscriptionStoreView` you don’t need to call any other API to initiate a
purchase. StoreKit manages the purchase action automatically, including
presenting the purchase confirmation UI. For more information, see StoreKit
views.

The `purchase(confirmIn:options:)` method may throw a `Product.PurchaseError`
or `StoreKitError`.

## See Also

### Purchasing a product

`func purchase(options: Set<Product.PurchaseOption>) ->
Product.PurchaseResult`

Initiates a purchase for the product with the App Store and displays the
confirmation sheet.

`struct Product.PurchaseOption`

Optional settings for a product purchase.

`enum Product.PurchaseResult`

The result of a purchase.

`enum Product.PurchaseError`

Error information for product purchase errors.

Instance Property

# currentEntitlement

The transaction that entitles the user to the product.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var currentEntitlement: VerificationResult<Transaction>? { get async }

## Discussion

This value is `nil` if the user isn’t currently entitled to this product.
Current entitlement information applies only to non-consumables, non-renewing
subscriptions, and auto-renewable subscriptions. The following example checks
the current entitlement for a product.

Instance Property

# latestTransaction

The most recent transaction for the product.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var latestTransaction: VerificationResult<Transaction>? { get async }

## Discussion

This value is `nil` if the user has never purchased this product. The
following example illustrates requesting the latest transaction for a product
to determine whether the user has purchased the product.

Instance Property

# subscription

The subscription information for an auto-renewable subscripton.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let subscription: Product.SubscriptionInfo?

## Discussion

A `nil` value indicates that this product isn’t an auto-renewable
subscription.

For more information about subscriptions, see Auto-renewable Subscriptions.

## See Also

### Getting subscription information

`struct Product.SubscriptionInfo`

Information about an auto-renewable subscription, such as its status, period,
subscription group, and subscription offer details.

`struct Product.SubscriptionPeriod`

Values that represent the duration of time between subscription renewals.

`struct Product.SubscriptionOffer`

Information about a subscription offer that you configure in App Store
Connect.

`struct Product.SubscriptionInfo.Status`

The renewal status information for an auto-renewable subscription.

Instance Property

# id

The unique product identifier.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let id: String

## Relationships

### From Protocol

  * `Identifiable`

## See Also

### Getting product identifiers and type

`typealias Product.ID`

A type representing a unique product identifier.

`let type: Product.ProductType`

The in-app purchase product type.

`struct Product.ProductType`

The types of in-app purchases.

`var id: ObjectIdentifier`

The stable identity of the entity associated with this instance.

Available when `Product` conforms to `AnyObject`.

Type Alias

# Product.ID

A type representing a unique product identifier.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    typealias Product.ID = String

## See Also

### Getting product identifiers and type

`let id: String`

The unique product identifier.

`let type: Product.ProductType`

The in-app purchase product type.

`struct Product.ProductType`

The types of in-app purchases.

`var id: ObjectIdentifier`

The stable identity of the entity associated with this instance.

Available when `Product` conforms to `AnyObject`.

Instance Property

# type

The in-app purchase product type.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let type: Product.ProductType

## See Also

### Getting product identifiers and type

`let id: String`

The unique product identifier.

`typealias Product.ID`

A type representing a unique product identifier.

`struct Product.ProductType`

The types of in-app purchases.

`var id: ObjectIdentifier`

The stable identity of the entity associated with this instance.

Available when `Product` conforms to `AnyObject`.

Instance Property

# id

The stable identity of the entity associated with this instance.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 15.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+  Xcode 11.0+

    
    
    var id: ObjectIdentifier { get }

Available when `Product` conforms to `AnyObject`.

## Discussion

Note

This documentation comment was inherited from `Identifiable`.

## See Also

### Getting product identifiers and type

`let id: String`

The unique product identifier.

`typealias Product.ID`

A type representing a unique product identifier.

`let type: Product.ProductType`

The in-app purchase product type.

`struct Product.ProductType`

The types of in-app purchases.

Instance Property

# isFamilyShareable

A Boolean value that indicates whether the product is available for Family
Sharing in App Store Connect.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let isFamilyShareable: Bool

## Discussion

Check the value of `isFamilyShareable` to learn whether an in-app purchase is
sharable with the family group.

When displaying in-app purchases in your app, indicate whether the product
includes Family Sharing to help customers make a selection that best fits
their needs.

Configure your in-app purchases to allow Family Sharing in App Store Connect.
For more information about setting up Family Sharing, see Turn-on Family
Sharing for in-app purchases.

Instance Property

# jsonRepresentation

The raw JSON representation of the product information.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var jsonRepresentation: Data { get }

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func != (lhs: Product, rhs: Product) -> Bool

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

### Comparing and hashing products

`static func == (Product, Product) -> Bool`

Returns a Boolean value that indicates whether two values are equal.

`func hash(into: inout Hasher)`

Hashes the essential components of the value by feeding them into the given
hasher.

`var hashValue: Int`

The hash value.

Operator

# ==(_:_:)

Returns a Boolean value that indicates whether two values are equal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func == (lhs: Product, rhs: Product) -> Bool

## See Also

### Comparing and hashing products

`static func != (Product, Product) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`func hash(into: inout Hasher)`

Hashes the essential components of the value by feeding them into the given
hasher.

`var hashValue: Int`

The hash value.

Instance Method

# hash(into:)

Hashes the essential components of the value by feeding them into the given
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

### Comparing and hashing products

`static func != (Product, Product) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (Product, Product) -> Bool`

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

### Comparing and hashing products

`static func != (Product, Product) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (Product, Product) -> Bool`

Returns a Boolean value that indicates whether two values are equal.

`func hash(into: inout Hasher)`

Hashes the essential components of the value by feeding them into the given
hasher.

Instance Property

# debugDescription

A string representation of the product structure, suitable for debugging.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var debugDescription: String { get }

## Relationships

### From Protocol

  * `CustomDebugStringConvertible`

