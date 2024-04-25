Instance Property

# productIdentifier

The string that identifies the product to the Apple App Store.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    var productIdentifier: String { get }

Instance Property

# localizedDescription

A description of the product.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    var localizedDescription: String { get }

## Discussion

The description's language is determined by the storefront that the user's
device is connected to, not the preferred language set on the device.

## See Also

### Getting Product Attributes

`var localizedTitle: String`

The name of the product.

`var contentVersion: String`

A string that identifies the version of the content.

`var isFamilyShareable: Bool`

A Boolean value that indicates whether the product is available for Family
Sharing in App Store Connect.

`var contentLengths: [NSNumber]`

The total size of the content, in bytes.

Deprecated

### Related Documentation

`class SKStorefront`

An object containing the location and unique identifier of an Apple App Store
storefront.

Instance Property

# localizedTitle

The name of the product.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    var localizedTitle: String { get }

## Discussion

The title's language is determined by the storefront that the user's device is
connected to, not the preferred language set on the device.

## See Also

### Getting Product Attributes

`var localizedDescription: String`

A description of the product.

`var contentVersion: String`

A string that identifies the version of the content.

`var isFamilyShareable: Bool`

A Boolean value that indicates whether the product is available for Family
Sharing in App Store Connect.

`var contentLengths: [NSNumber]`

The total size of the content, in bytes.

Deprecated

### Related Documentation

`class SKStorefront`

An object containing the location and unique identifier of an Apple App Store
storefront.

Instance Property

# contentVersion

A string that identifies the version of the content.

iOS 13.0+  iPadOS 13.0+  macOS 10.8–10.14  Deprecated  Mac Catalyst 13.1–13.1
Deprecated  tvOS 13.0+  watchOS 6.2+

    
    
    var contentVersion: String { get }

## See Also

### Getting Product Attributes

`var localizedDescription: String`

A description of the product.

`var localizedTitle: String`

The name of the product.

`var isFamilyShareable: Bool`

A Boolean value that indicates whether the product is available for Family
Sharing in App Store Connect.

`var contentLengths: [NSNumber]`

The total size of the content, in bytes.

Deprecated

Instance Property

# isFamilyShareable

A Boolean value that indicates whether the product is available for Family
Sharing in App Store Connect.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    var isFamilyShareable: Bool { get }

## Discussion

Check the value of `isFamilyShareable` to learn whether an in-app purchase is
sharable with the family group.

    
    
    // Determine whether an in-app purchase supports Family Sharing.
    let myProduct: SKProduct = getProductWithId(id: "com.example.product_identifier")
    if myProduct.isFamilyShareable {
        print("Product can be shared with family group.")
    }
    

When displaying in-app purchases in your app, indicate whether the product
includes Family Sharing to help customers make a selection that best fits
their needs.

Configure your in-app purchases to allow Family Sharing in App Store Connect.
For more information about setting up Family Sharing, see Turn-on Family
Sharing for in-app purchases.

## See Also

### Getting Product Attributes

`var localizedDescription: String`

A description of the product.

`var localizedTitle: String`

The name of the product.

`var contentVersion: String`

A string that identifies the version of the content.

`var contentLengths: [NSNumber]`

The total size of the content, in bytes.

Deprecated

Instance Property

# contentLengths

The total size of the content, in bytes.

macOS 10.8–10.14  Deprecated

    
    
    var contentLengths: [NSNumber] { get }

## See Also

### Getting Product Attributes

`var localizedDescription: String`

A description of the product.

`var localizedTitle: String`

The name of the product.

`var contentVersion: String`

A string that identifies the version of the content.

`var isFamilyShareable: Bool`

A Boolean value that indicates whether the product is available for Family
Sharing in App Store Connect.

Instance Property

# price

The cost of the product in the local currency.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    var price: NSDecimalNumber { get }

## Discussion

Your app can format the price using a number formatter, as shown in the
following sample code:

## See Also

### Getting Pricing Information

`var priceLocale: Locale`

The locale used to format the price of the product.

`var introductoryPrice: SKProductDiscount?`

The object containing introductory price information for the product.

`var discounts: [SKProductDiscount]`

An array of subscription offers available for the auto-renewable subscription.

`class SKProductDiscount`

The details of an introductory offer or a promotional offer for an auto-
renewable subscription.

Instance Property

# priceLocale

The locale used to format the price of the product.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    var priceLocale: Locale { get }

## Discussion

Use the locale to format the `price`.

## See Also

### Getting Pricing Information

`var price: NSDecimalNumber`

The cost of the product in the local currency.

`var introductoryPrice: SKProductDiscount?`

The object containing introductory price information for the product.

`var discounts: [SKProductDiscount]`

An array of subscription offers available for the auto-renewable subscription.

`class SKProductDiscount`

The details of an introductory offer or a promotional offer for an auto-
renewable subscription.

Instance Property

# introductoryPrice

The object containing introductory price information for the product.

iOS 11.2+  iPadOS 11.2+  macOS 10.13.2+  Mac Catalyst 13.1+  tvOS 11.2+
watchOS 6.2+  visionOS 1.0+

    
    
    var introductoryPrice: SKProductDiscount? { get }

## Discussion

If you've set up introductory prices in App Store Connect, the introductory
price property will be populated. This property is `nil` if the product has no
introductory price.

Before displaying UI that offers the introductory price, you must first
determine if the user is eligible to receive it. See Implementing introductory
offers in your app for information on determining eligibility and displaying
introductory prices.

## See Also

### Getting Pricing Information

`var price: NSDecimalNumber`

The cost of the product in the local currency.

`var priceLocale: Locale`

The locale used to format the price of the product.

`var discounts: [SKProductDiscount]`

An array of subscription offers available for the auto-renewable subscription.

`class SKProductDiscount`

The details of an introductory offer or a promotional offer for an auto-
renewable subscription.

Instance Property

# discounts

An array of subscription offers available for the auto-renewable subscription.

iOS 12.2+  iPadOS 12.2+  macOS 10.14.4+  Mac Catalyst 13.1+  tvOS 12.2+
watchOS 6.2+  visionOS 1.0+

    
    
    var discounts: [SKProductDiscount] { get }

## Discussion

The `discounts` array contains all of the introductory offers and promotional
offers that you set up in App Store Connect for this subscription
(`productIdentifier`). It's up to the logic in your app to decide which offer
to present to the user.

For more information about offers, see Implementing promotional offers in your
app, and Implementing introductory offers in your app.

## See Also

### Getting Pricing Information

`var price: NSDecimalNumber`

The cost of the product in the local currency.

`var priceLocale: Locale`

The locale used to format the price of the product.

`var introductoryPrice: SKProductDiscount?`

The object containing introductory price information for the product.

`class SKProductDiscount`

The details of an introductory offer or a promotional offer for an auto-
renewable subscription.

Instance Property

# subscriptionGroupIdentifier

The identifier of the subscription group to which the subscription belongs.

iOS 12.0+  iPadOS 12.0+  macOS 10.14+  Mac Catalyst 13.1+  tvOS 12.0+  watchOS
6.2+  visionOS 1.0+

    
    
    var subscriptionGroupIdentifier: String? { get }

## Discussion

Auto-renewable subscriptions always belong to a subscription group. You create
the subscription group identifiers in App Store Connect before you create and
add an auto-renewable subscription. For more information about subscription
groups, see Offer auto-renewable subscriptions.

This property is `nil` if the `SKProduct` isn’t an auto-renewable
subscription.

## See Also

### Getting Subscription Information

`var subscriptionPeriod: SKProductSubscriptionPeriod?`

The period details for products that are subscriptions.

`class SKProductSubscriptionPeriod`

An object containing the subscription period duration information.

`enum SKProduct.PeriodUnit`

Values representing the duration of an interval, from a day up to a year.

Instance Property

# subscriptionPeriod

The period details for products that are subscriptions.

iOS 11.2+  iPadOS 11.2+  macOS 10.13.2+  Mac Catalyst 13.1+  tvOS 11.2+
watchOS 6.2+  visionOS 1.0+

    
    
    var subscriptionPeriod: SKProductSubscriptionPeriod? { get }

## Discussion

This read-only property is `nil` if the product is not a subscription.

A subscription period is described in terms of a unit and the number of units
that make up a single period.

## See Also

### Getting Subscription Information

`var subscriptionGroupIdentifier: String?`

The identifier of the subscription group to which the subscription belongs.

`class SKProductSubscriptionPeriod`

An object containing the subscription period duration information.

`enum SKProduct.PeriodUnit`

Values representing the duration of an interval, from a day up to a year.

Instance Property

# isDownloadable

A Boolean value that indicates whether the App Store has downloadable content
for this product.

iOS 6.0+  iPadOS 6.0+  macOS 10.15+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    var isDownloadable: Bool { get }

## Discussion

You can associate a set of data files with the App Store Connect record you
created for a product. The value of this property is `true` if at least one
file has been associated with the product.

## See Also

### Getting Downloadable Content Information

`var downloadContentLengths: [NSNumber]`

The lengths of the downloadable files available for this product.

`var downloadContentVersion: String`

A string that identifies which version of the content is available for
download.

`var downloadable: Bool`

A Boolean value that indicates whether the App Store has downloadable content
for this product.

Deprecated

Instance Property

# downloadContentLengths

The lengths of the downloadable files available for this product.

iOS 6.0+  iPadOS 6.0+  macOS 10.14+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    var downloadContentLengths: [NSNumber] { get }

## Discussion

The array holds `NSNumber` objects, each of which holds a `long long` value
that is the size of one of the downloadable files (in bytes).

## See Also

### Getting Downloadable Content Information

`var isDownloadable: Bool`

A Boolean value that indicates whether the App Store has downloadable content
for this product.

`var downloadContentVersion: String`

A string that identifies which version of the content is available for
download.

`var downloadable: Bool`

A Boolean value that indicates whether the App Store has downloadable content
for this product.

Deprecated

Instance Property

# downloadContentVersion

A string that identifies which version of the content is available for
download.

iOS 6.0+  iPadOS 6.0+  macOS 10.14+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    var downloadContentVersion: String { get }

## Discussion

The version string is formatted as a series of integers separated by periods.

## See Also

### Getting Downloadable Content Information

`var isDownloadable: Bool`

A Boolean value that indicates whether the App Store has downloadable content
for this product.

`var downloadContentLengths: [NSNumber]`

The lengths of the downloadable files available for this product.

`var downloadable: Bool`

A Boolean value that indicates whether the App Store has downloadable content
for this product.

Deprecated

Instance Property

# downloadable

A Boolean value that indicates whether the App Store has downloadable content
for this product.

macOS 10.8–10.15  Deprecated

    
    
    var downloadable: Bool { get }

Deprecated

Use `isDownloadable` instead.

## Discussion

You can associate a set of data files with the App Store Connect record you
created for a product. The value of this property is `true` if at least one
file has been associated with the product.

## See Also

### Getting Downloadable Content Information

`var isDownloadable: Bool`

A Boolean value that indicates whether the App Store has downloadable content
for this product.

`var downloadContentLengths: [NSNumber]`

The lengths of the downloadable files available for this product.

`var downloadContentVersion: String`

A string that identifies which version of the content is available for
download.

