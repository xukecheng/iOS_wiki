Instance Property

# status

An array that contains status information for a subscription group, including
renewal and transaction information.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var status: [Product.SubscriptionInfo.Status] { get async throws }

## Discussion

This array is empty if the customer was never subscribed to a product in this
subscription group.

The array can have more than one subscription status if your subscription
supports Family Sharing. Provide the customer with service for the
subscription based on the highest level of service where the state is
`subscribed`.

## See Also

### Determining the subscription status

`static func status(for: String) -> [Product.SubscriptionInfo.Status]`

Gets the subscription status for a subscription group identifier.

`struct Product.SubscriptionInfo.Status`

The renewal status information for an auto-renewable subscription.

Type Method

# status(for:)

Gets the subscription status for a subscription group identifier.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func status(for groupID: String) async throws -> [Product.SubscriptionInfo.Status]

##  Parameters

`groupID`

    

The subscription group identifier of the subscription to get status for.

## Return Value

An array of `Product.SubscriptionInfo.Status`. This array is empty if the
customer has never subscribed to a product in this subscription group.

## Discussion

To get the subscription group identifier of a subscription, see
`subscriptionGroupID` in `Product.SubscriptionInfo`, or `subscriptionGroupID`
in `Transaction`. You originally create subscription group identifiers when
you set up in-app purchases in App Store Connect. For more information, see
Offer auto-renewable subscriptions.

Users can only buy one auto-renewable subscription within a group at a time.
However, the returned array may contain multiple status values if your
subscription supports Family Sharing, and the person has access to other
subscriptions in the group through Family Sharing. For more information about
Family Sharing, see Enable Family Sharing for your subscriptions.

## See Also

### Determining the subscription status

`var status: [Product.SubscriptionInfo.Status]`

An array that contains status information for a subscription group, including
renewal and transaction information.

`struct Product.SubscriptionInfo.Status`

The renewal status information for an auto-renewable subscription.

Instance Property

# subscriptionGroupID

The subscription group identifier for this subscription.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let subscriptionGroupID: String

## Discussion

Auto-renewable subscriptions always belong to a subscription group. You create
the subscription group identifiers in App Store Connect before you create and
add an auto-renewable subscription. For more information about subscription
groups, see Offer auto-renewable subscriptions.

## See Also

### Identifying the subscription group

`@backDeployed(before: iOS 17.0, macOS 14.0, tvOS 17.0, watchOS 10.0) var
groupDisplayName: String`

The localized name of the subscription group, suitable for display.

`@backDeployed(before: iOS 17.0, macOS 14.0, tvOS 17.0, watchOS 10.0) var
groupLevel: Int`

The rank of the subscription relative to other subscriptions in the same
subscription group.

Instance Property

# groupDisplayName

The localized name of the subscription group, suitable for display.

iOS 16.4+  iPadOS 16.4+  macOS 13.3+  Mac Catalyst 17.0+  tvOS 16.4+  watchOS
9.4+  visionOS 1.0+  Xcode 14.3+

    
    
    @backDeployed(before: iOS 17.0, macOS 14.0, tvOS 17.0, watchOS 10.0)
    var groupDisplayName: String { get }

## Discussion

You provide a group display name in App Store Connect when you set up a
subscription group. For more information, see Offer auto-renewable
subscriptions.

The `SubscriptionStoreView` uses this value as part of the automatic marketing
content if you don’t provide a marketing content view.

Note

When you create a new product in App Store Connect or in a StoreKit
configuration file, you can test it before you add a product localization. The
`groupDisplayName` value is an empty string until you add a localization. For
more information on localizations, see Add localizations.

## See Also

### Identifying the subscription group

`let subscriptionGroupID: String`

The subscription group identifier for this subscription.

`@backDeployed(before: iOS 17.0, macOS 14.0, tvOS 17.0, watchOS 10.0) var
groupLevel: Int`

The rank of the subscription relative to other subscriptions in the same
subscription group.

Instance Property

# groupLevel

The rank of the subscription relative to other subscriptions in the same
subscription group.

iOS 16.4+  iPadOS 16.4+  macOS 13.3+  Mac Catalyst 17.0+  tvOS 16.4+  watchOS
9.4+  visionOS 1.0+  Xcode 14.3+

    
    
    @backDeployed(before: iOS 17.0, macOS 14.0, tvOS 17.0, watchOS 10.0)
    var groupLevel: Int { get }

## Discussion

If you offer multiple auto-renewable subscriptions with different price tiers,
you can assign each to a level in App Store Connect. Ranking your
subscriptions determines the upgrade, downgrade, and crossgrade paths
available.

Subscriptions with the highest level of service within a subscription group
have a `groupLevel` value of `1`. Subscriptions with lower levels of service
or content have `groupLevel` values of `2` or greater. For example, when
comparing two subscriptions, moving from a subscription with a `groupLevel` of
`2` to a subscription with a `groupLevel` of `1` represents an upgrade.

For more information on ranking, see Ranking subscriptions within the group.
For information on assigning subscription levels in App Store Connect, see
Assign subscription levels.

Note

On systems earlier than iOS 17, macOS 14, tvOS 17, and watchOS 10, this
property returns a sentinel value of `0` when you test your app using StoreKit
Testing in Xcode or if there’s an unexpected server error.

## See Also

### Identifying the subscription group

`let subscriptionGroupID: String`

The subscription group identifier for this subscription.

`@backDeployed(before: iOS 17.0, macOS 14.0, tvOS 17.0, watchOS 10.0) var
groupDisplayName: String`

The localized name of the subscription group, suitable for display.

Instance Property

# subscriptionPeriod

The duration of time between subscription renewals.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let subscriptionPeriod: Product.SubscriptionPeriod

## See Also

### Getting the subscription period

`struct Product.SubscriptionPeriod`

Values that represent the duration of time between subscription renewals.

Instance Property

# isEligibleForIntroOffer

A Boolean value that indicates whether the customer is eligible for an
introductory offer.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var isEligibleForIntroOffer: Bool { get async }

## Discussion

This value is `true` if the customer is eligible for an introductory offer on
this auto-renewable subscription, or any auto-renewable subscription in the
same subscription group; this value is `false` otherwise. This value may be
`true` even if you haven’t set up an introductory offer in App Store Connect.
The following example illustrates checking the `subscription` property of a
product to determine whether the user is eligible for an introductory offer.

## See Also

### Getting subscription offer details

`static func isEligibleForIntroOffer(for: String) -> Bool`

Returns a Boolean value that determines the customer's eligibility for an
introductory offer within the provided subscription group.

`let introductoryOffer: Product.SubscriptionOffer?`

Information about the introductory offer available for the auto-renewable
subscription.

`let promotionalOffers: [Product.SubscriptionOffer]`

An array of promotional offers available for the auto-renewable subscription.

`struct Product.SubscriptionOffer`

Information about a subscription offer that you configure in App Store
Connect.

Type Method

# isEligibleForIntroOffer(for:)

Returns a Boolean value that determines the customer's eligibility for an
introductory offer within the provided subscription group.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func isEligibleForIntroOffer(for groupID: String) async -> Bool

##  Parameters

`groupID`

    

The subscription group identifier to check eligibility for an introductory
offer.

## Return Value

`true` if the customer is eligible for an introductory offer on any auto-
renewable subscription within the subscription group; `false `otherwise.

## Discussion

This value may be `true` even if you haven’t set up an introductory offer in
App Store Connect.

## See Also

### Getting subscription offer details

`var isEligibleForIntroOffer: Bool`

A Boolean value that indicates whether the customer is eligible for an
introductory offer.

`let introductoryOffer: Product.SubscriptionOffer?`

Information about the introductory offer available for the auto-renewable
subscription.

`let promotionalOffers: [Product.SubscriptionOffer]`

An array of promotional offers available for the auto-renewable subscription.

`struct Product.SubscriptionOffer`

Information about a subscription offer that you configure in App Store
Connect.

Instance Property

# introductoryOffer

Information about the introductory offer available for the auto-renewable
subscription.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let introductoryOffer: Product.SubscriptionOffer?

## Discussion

This value is `nil` if you don't set up an introductory offer in App Store
Connect. Use `isEligibleForIntroOffer` to determine whether the customer is
eligible for an introductory offer.

## See Also

### Getting subscription offer details

`var isEligibleForIntroOffer: Bool`

A Boolean value that indicates whether the customer is eligible for an
introductory offer.

`static func isEligibleForIntroOffer(for: String) -> Bool`

Returns a Boolean value that determines the customer's eligibility for an
introductory offer within the provided subscription group.

`let promotionalOffers: [Product.SubscriptionOffer]`

An array of promotional offers available for the auto-renewable subscription.

`struct Product.SubscriptionOffer`

Information about a subscription offer that you configure in App Store
Connect.

Instance Property

# promotionalOffers

An array of promotional offers available for the auto-renewable subscription.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let promotionalOffers: [Product.SubscriptionOffer]

## Discussion

This array is empty if you haven't set up promotional offers in App Store
Connect.

For more information about promotional offers, see Set up promotional offers
for auto-renewable subscriptions.

## See Also

### Getting subscription offer details

`var isEligibleForIntroOffer: Bool`

A Boolean value that indicates whether the customer is eligible for an
introductory offer.

`static func isEligibleForIntroOffer(for: String) -> Bool`

Returns a Boolean value that determines the customer's eligibility for an
introductory offer within the provided subscription group.

`let introductoryOffer: Product.SubscriptionOffer?`

Information about the introductory offer available for the auto-renewable
subscription.

`struct Product.SubscriptionOffer`

Information about a subscription offer that you configure in App Store
Connect.

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func != (lhs: Product.SubscriptionInfo, rhs: Product.SubscriptionInfo) -> Bool

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

### Comparing and hashing subscription information

`static func == (Product.SubscriptionInfo, Product.SubscriptionInfo) -> Bool`

Returns a Boolean value indicating whether two values are equal.

`func hash(into: inout Hasher)`

Hashes the essential components of this value by feeding them into the given
hasher.

`var hashValue: Int`

The hash value.

Operator

# ==(_:_:)

Returns a Boolean value indicating whether two values are equal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func == (a: Product.SubscriptionInfo, b: Product.SubscriptionInfo) -> Bool

## See Also

### Comparing and hashing subscription information

`static func != (Product.SubscriptionInfo, Product.SubscriptionInfo) -> Bool`

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

### Comparing and hashing subscription information

`static func != (Product.SubscriptionInfo, Product.SubscriptionInfo) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (Product.SubscriptionInfo, Product.SubscriptionInfo) -> Bool`

Returns a Boolean value indicating whether two values are equal.

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

### Comparing and hashing subscription information

`static func != (Product.SubscriptionInfo, Product.SubscriptionInfo) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (Product.SubscriptionInfo, Product.SubscriptionInfo) -> Bool`

Returns a Boolean value indicating whether two values are equal.

`func hash(into: inout Hasher)`

Hashes the essential components of this value by feeding them into the given
hasher.

Instance Property

# status

An array that contains status information for a subscription group, including
renewal and transaction information.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var status: [Product.SubscriptionInfo.Status] { get async throws }

## Discussion

This array is empty if the customer was never subscribed to a product in this
subscription group.

The array can have more than one subscription status if your subscription
supports Family Sharing. Provide the customer with service for the
subscription based on the highest level of service where the state is
`subscribed`.

## See Also

### Determining the subscription status

`static func status(for: String) -> [Product.SubscriptionInfo.Status]`

Gets the subscription status for a subscription group identifier.

`struct Product.SubscriptionInfo.Status`

The renewal status information for an auto-renewable subscription.

Type Method

# status(for:)

Gets the subscription status for a subscription group identifier.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func status(for groupID: String) async throws -> [Product.SubscriptionInfo.Status]

##  Parameters

`groupID`

    

The subscription group identifier of the subscription to get status for.

## Return Value

An array of `Product.SubscriptionInfo.Status`. This array is empty if the
customer has never subscribed to a product in this subscription group.

## Discussion

To get the subscription group identifier of a subscription, see
`subscriptionGroupID` in `Product.SubscriptionInfo`, or `subscriptionGroupID`
in `Transaction`. You originally create subscription group identifiers when
you set up in-app purchases in App Store Connect. For more information, see
Offer auto-renewable subscriptions.

Users can only buy one auto-renewable subscription within a group at a time.
However, the returned array may contain multiple status values if your
subscription supports Family Sharing, and the person has access to other
subscriptions in the group through Family Sharing. For more information about
Family Sharing, see Enable Family Sharing for your subscriptions.

## See Also

### Determining the subscription status

`var status: [Product.SubscriptionInfo.Status]`

An array that contains status information for a subscription group, including
renewal and transaction information.

`struct Product.SubscriptionInfo.Status`

The renewal status information for an auto-renewable subscription.

Instance Property

# subscriptionGroupID

The subscription group identifier for this subscription.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let subscriptionGroupID: String

## Discussion

Auto-renewable subscriptions always belong to a subscription group. You create
the subscription group identifiers in App Store Connect before you create and
add an auto-renewable subscription. For more information about subscription
groups, see Offer auto-renewable subscriptions.

## See Also

### Identifying the subscription group

`@backDeployed(before: iOS 17.0, macOS 14.0, tvOS 17.0, watchOS 10.0) var
groupDisplayName: String`

The localized name of the subscription group, suitable for display.

`@backDeployed(before: iOS 17.0, macOS 14.0, tvOS 17.0, watchOS 10.0) var
groupLevel: Int`

The rank of the subscription relative to other subscriptions in the same
subscription group.

Instance Property

# groupDisplayName

The localized name of the subscription group, suitable for display.

iOS 16.4+  iPadOS 16.4+  macOS 13.3+  Mac Catalyst 17.0+  tvOS 16.4+  watchOS
9.4+  visionOS 1.0+  Xcode 14.3+

    
    
    @backDeployed(before: iOS 17.0, macOS 14.0, tvOS 17.0, watchOS 10.0)
    var groupDisplayName: String { get }

## Discussion

You provide a group display name in App Store Connect when you set up a
subscription group. For more information, see Offer auto-renewable
subscriptions.

The `SubscriptionStoreView` uses this value as part of the automatic marketing
content if you don’t provide a marketing content view.

Note

When you create a new product in App Store Connect or in a StoreKit
configuration file, you can test it before you add a product localization. The
`groupDisplayName` value is an empty string until you add a localization. For
more information on localizations, see Add localizations.

## See Also

### Identifying the subscription group

`let subscriptionGroupID: String`

The subscription group identifier for this subscription.

`@backDeployed(before: iOS 17.0, macOS 14.0, tvOS 17.0, watchOS 10.0) var
groupLevel: Int`

The rank of the subscription relative to other subscriptions in the same
subscription group.

Instance Property

# groupLevel

The rank of the subscription relative to other subscriptions in the same
subscription group.

iOS 16.4+  iPadOS 16.4+  macOS 13.3+  Mac Catalyst 17.0+  tvOS 16.4+  watchOS
9.4+  visionOS 1.0+  Xcode 14.3+

    
    
    @backDeployed(before: iOS 17.0, macOS 14.0, tvOS 17.0, watchOS 10.0)
    var groupLevel: Int { get }

## Discussion

If you offer multiple auto-renewable subscriptions with different price tiers,
you can assign each to a level in App Store Connect. Ranking your
subscriptions determines the upgrade, downgrade, and crossgrade paths
available.

Subscriptions with the highest level of service within a subscription group
have a `groupLevel` value of `1`. Subscriptions with lower levels of service
or content have `groupLevel` values of `2` or greater. For example, when
comparing two subscriptions, moving from a subscription with a `groupLevel` of
`2` to a subscription with a `groupLevel` of `1` represents an upgrade.

For more information on ranking, see Ranking subscriptions within the group.
For information on assigning subscription levels in App Store Connect, see
Assign subscription levels.

Note

On systems earlier than iOS 17, macOS 14, tvOS 17, and watchOS 10, this
property returns a sentinel value of `0` when you test your app using StoreKit
Testing in Xcode or if there’s an unexpected server error.

## See Also

### Identifying the subscription group

`let subscriptionGroupID: String`

The subscription group identifier for this subscription.

`@backDeployed(before: iOS 17.0, macOS 14.0, tvOS 17.0, watchOS 10.0) var
groupDisplayName: String`

The localized name of the subscription group, suitable for display.

Instance Property

# subscriptionPeriod

The duration of time between subscription renewals.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let subscriptionPeriod: Product.SubscriptionPeriod

## See Also

### Getting the subscription period

`struct Product.SubscriptionPeriod`

Values that represent the duration of time between subscription renewals.

Instance Property

# isEligibleForIntroOffer

A Boolean value that indicates whether the customer is eligible for an
introductory offer.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var isEligibleForIntroOffer: Bool { get async }

## Discussion

This value is `true` if the customer is eligible for an introductory offer on
this auto-renewable subscription, or any auto-renewable subscription in the
same subscription group; this value is `false` otherwise. This value may be
`true` even if you haven’t set up an introductory offer in App Store Connect.
The following example illustrates checking the `subscription` property of a
product to determine whether the user is eligible for an introductory offer.

    
    
    func eligibleForIntro(product: Product) async throws -> Bool {
        guard let renewableSubscription = product.subscription else {
            // No renewable subscription is available for this product.
            return false
        }
        if await renewableSubscription.isEligibleForIntroOffer {
            // The product is eligible for an introductory offer.
            return true
        }
        return false
    }
    

## See Also

### Getting subscription offer details

`static func isEligibleForIntroOffer(for: String) -> Bool`

Returns a Boolean value that determines the customer's eligibility for an
introductory offer within the provided subscription group.

`let introductoryOffer: Product.SubscriptionOffer?`

Information about the introductory offer available for the auto-renewable
subscription.

`let promotionalOffers: [Product.SubscriptionOffer]`

An array of promotional offers available for the auto-renewable subscription.

`struct Product.SubscriptionOffer`

Information about a subscription offer that you configure in App Store
Connect.

Type Method

# isEligibleForIntroOffer(for:)

Returns a Boolean value that determines the customer's eligibility for an
introductory offer within the provided subscription group.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func isEligibleForIntroOffer(for groupID: String) async -> Bool

##  Parameters

`groupID`

    

The subscription group identifier to check eligibility for an introductory
offer.

## Return Value

`true` if the customer is eligible for an introductory offer on any auto-
renewable subscription within the subscription group; `false `otherwise.

## Discussion

This value may be `true` even if you haven’t set up an introductory offer in
App Store Connect.

## See Also

### Getting subscription offer details

`var isEligibleForIntroOffer: Bool`

A Boolean value that indicates whether the customer is eligible for an
introductory offer.

`let introductoryOffer: Product.SubscriptionOffer?`

Information about the introductory offer available for the auto-renewable
subscription.

`let promotionalOffers: [Product.SubscriptionOffer]`

An array of promotional offers available for the auto-renewable subscription.

`struct Product.SubscriptionOffer`

Information about a subscription offer that you configure in App Store
Connect.

Instance Property

# introductoryOffer

Information about the introductory offer available for the auto-renewable
subscription.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let introductoryOffer: Product.SubscriptionOffer?

## Discussion

This value is `nil` if you don't set up an introductory offer in App Store
Connect. Use `isEligibleForIntroOffer` to determine whether the customer is
eligible for an introductory offer.

## See Also

### Getting subscription offer details

`var isEligibleForIntroOffer: Bool`

A Boolean value that indicates whether the customer is eligible for an
introductory offer.

`static func isEligibleForIntroOffer(for: String) -> Bool`

Returns a Boolean value that determines the customer's eligibility for an
introductory offer within the provided subscription group.

`let promotionalOffers: [Product.SubscriptionOffer]`

An array of promotional offers available for the auto-renewable subscription.

`struct Product.SubscriptionOffer`

Information about a subscription offer that you configure in App Store
Connect.

Instance Property

# promotionalOffers

An array of promotional offers available for the auto-renewable subscription.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let promotionalOffers: [Product.SubscriptionOffer]

## Discussion

This array is empty if you haven't set up promotional offers in App Store
Connect.

For more information about promotional offers, see Set up promotional offers
for auto-renewable subscriptions.

## See Also

### Getting subscription offer details

`var isEligibleForIntroOffer: Bool`

A Boolean value that indicates whether the customer is eligible for an
introductory offer.

`static func isEligibleForIntroOffer(for: String) -> Bool`

Returns a Boolean value that determines the customer's eligibility for an
introductory offer within the provided subscription group.

`let introductoryOffer: Product.SubscriptionOffer?`

Information about the introductory offer available for the auto-renewable
subscription.

`struct Product.SubscriptionOffer`

Information about a subscription offer that you configure in App Store
Connect.

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func != (lhs: Product.SubscriptionInfo, rhs: Product.SubscriptionInfo) -> Bool

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

### Comparing and hashing subscription information

`static func == (Product.SubscriptionInfo, Product.SubscriptionInfo) -> Bool`

Returns a Boolean value indicating whether two values are equal.

`func hash(into: inout Hasher)`

Hashes the essential components of this value by feeding them into the given
hasher.

`var hashValue: Int`

The hash value.

Operator

# ==(_:_:)

Returns a Boolean value indicating whether two values are equal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func == (a: Product.SubscriptionInfo, b: Product.SubscriptionInfo) -> Bool

## See Also

### Comparing and hashing subscription information

`static func != (Product.SubscriptionInfo, Product.SubscriptionInfo) -> Bool`

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

### Comparing and hashing subscription information

`static func != (Product.SubscriptionInfo, Product.SubscriptionInfo) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (Product.SubscriptionInfo, Product.SubscriptionInfo) -> Bool`

Returns a Boolean value indicating whether two values are equal.

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

### Comparing and hashing subscription information

`static func != (Product.SubscriptionInfo, Product.SubscriptionInfo) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (Product.SubscriptionInfo, Product.SubscriptionInfo) -> Bool`

Returns a Boolean value indicating whether two values are equal.

`func hash(into: inout Hasher)`

Hashes the essential components of this value by feeding them into the given
hasher.

