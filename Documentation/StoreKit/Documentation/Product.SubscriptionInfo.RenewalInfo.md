Instance Property

# environment

The server environment that signs the renewal information for an auto-
renewable subscription.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    let environment: AppStore.Environment

## See Also

### Getting the environment

`@backDeployed(before: iOS 16.0, macOS 13.0, tvOS 16.0, watchOS 9.0,
macCatalyst 16.0) var environmentStringRepresentation: String`

The string representation of the server environment that signs the renewal
information for an auto-renewable subscription.

Deprecated

Instance Property

# environmentStringRepresentation

The string representation of the server environment that signs the renewal
information for an auto-renewable subscription.

iOS 15.0–16.0  Deprecated  iPadOS 15.0–16.0  Deprecated  macOS 12.0–13.0
Deprecated  Mac Catalyst 16.0–16.0  Deprecated  tvOS 15.0–16.0  Deprecated
watchOS 8.0–9.0  Deprecated  Xcode 13.0–14.0  Deprecated

    
    
    @backDeployed(before: iOS 16.0, macOS 13.0, tvOS 16.0, watchOS 9.0, macCatalyst 16.0)
    var environmentStringRepresentation: String { get }

## See Also

### Getting the environment

`let environment: AppStore.Environment`

The server environment that signs the renewal information for an auto-
renewable subscription.

Instance Property

# originalTransactionID

The transaction identifier of the original purchase.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let originalTransactionID: UInt64

Instance Property

# currentProductID

The subscription product ID that the customer is subscribed to.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let currentProductID: String

Instance Property

# offerID

A string that identifies an offer applied to the next subscription period.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let offerID: String?

## Discussion

This value is `nil` if there isn’t an offer, or if the offer type is
`introductory`.

If the offer type is `promotional`, this value contains the promotional offer
identifier you set up in App Store Connect. For more information about
promotional offers, see Set up promotional offers for auto-renewable
subscriptions.

If the offer type is `code`, this value contains the reference name of the
offer code you set up in App Store Connect. For more information about offer
codes, see Set up offer codes.

## See Also

### Getting subscription offers

`let offerType: Transaction.OfferType?`

The subscription offer type for the next subscription period.

Instance Property

# offerType

The subscription offer type for the next subscription period.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let offerType: Transaction.OfferType?

## Discussion

If this value is `nil`, there’s no offer applied.

## See Also

### Getting subscription offers

`let offerID: String?`

A string that identifies an offer applied to the next subscription period.

Instance Property

# recentSubscriptionStartDate

The earliest start date of a subscription in a series of auto-renewable
subscription purchases that ignores all lapses of paid service shorter than 60
days.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 16.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 14.0+

    
    
    @backDeployed(before: iOS 16.0, macOS 13.0, tvOS 16.0, watchOS 9.0, macCatalyst 16.0)
    var recentSubscriptionStartDate: Date { get }

## Discussion

Important

Don’t use the `recentSubscriptionStartDate` date to calculate days of paid
service. For more information about paid days of service, see Net revenue
after a year.

Instance Property

# state

The renewal state of the auto-renewable subscription.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let state: Product.SubscriptionInfo.RenewalState

## See Also

### Getting subscription status information

`let renewalInfo: VerificationResult<Product.SubscriptionInfo.RenewalInfo>`

The signed renewal information for the auto-renewable subscription.

`let transaction: VerificationResult<Transaction>`

The latest transaction for the subscription group.

`struct Product.SubscriptionInfo.RenewalInfo`

The renewal information for an auto-renewable subscription.

`struct Product.SubscriptionInfo.RenewalState`

The renewal states of auto-renewable subscriptions.

Instance Property

# autoRenewPreference

The product ID of the auto-renewable subscription that will automatically
renew.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let autoRenewPreference: String?

## Discussion

This value is the product ID of the auto-renewable subscription that will
renew after the current period expires. The value may be:

  * The same as `currentProductID` if the subscription will renew with the same product.

  * Another product ID value if the subscription will renew to a different product.

  * `nil` if the subscription won’t renew in the next period. This may occur for several reasons, including when the person disables auto-renew for the subscription, the subscription lapses due to a billing issue, or you increase the subscription price and the person doesn't accept the increase.

## See Also

### Getting the renewal or expiration state

`let state: Product.SubscriptionInfo.RenewalState`

The renewal state of the auto-renewable subscription.

`let willAutoRenew: Bool`

A Boolean value that indicates whether the subscription will automatically
renew in the next period.

`let expirationReason: Product.SubscriptionInfo.RenewalInfo.ExpirationReason?`

The reason the auto-renewable subscription expired.

`struct Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The reasons for auto-renewable subscription expirations.

`@backDeployed(before: iOS 17.0, macOS 14.0, tvOS 17.0, watchOS 10.0,
macCatalyst 17.0) var renewalDate: Date?`

The UNIX time, in milliseconds, that the most recent auto-renewable
subscription purchase expires.

Instance Property

# willAutoRenew

A Boolean value that indicates whether the subscription will automatically
renew in the next period.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let willAutoRenew: Bool

## See Also

### Getting the renewal or expiration state

`let state: Product.SubscriptionInfo.RenewalState`

The renewal state of the auto-renewable subscription.

`let autoRenewPreference: String?`

The product ID of the auto-renewable subscription that will automatically
renew.

`let expirationReason: Product.SubscriptionInfo.RenewalInfo.ExpirationReason?`

The reason the auto-renewable subscription expired.

`struct Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The reasons for auto-renewable subscription expirations.

`@backDeployed(before: iOS 17.0, macOS 14.0, tvOS 17.0, watchOS 10.0,
macCatalyst 17.0) var renewalDate: Date?`

The UNIX time, in milliseconds, that the most recent auto-renewable
subscription purchase expires.

Instance Property

# expirationReason

The reason the auto-renewable subscription expired.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let expirationReason: Product.SubscriptionInfo.RenewalInfo.ExpirationReason?

## Discussion

This optional value is `nil` if the auto-renewable subscription is active and
hasn’t expired.

## See Also

### Getting the renewal or expiration state

`let state: Product.SubscriptionInfo.RenewalState`

The renewal state of the auto-renewable subscription.

`let autoRenewPreference: String?`

The product ID of the auto-renewable subscription that will automatically
renew.

`let willAutoRenew: Bool`

A Boolean value that indicates whether the subscription will automatically
renew in the next period.

`struct Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The reasons for auto-renewable subscription expirations.

`@backDeployed(before: iOS 17.0, macOS 14.0, tvOS 17.0, watchOS 10.0,
macCatalyst 17.0) var renewalDate: Date?`

The UNIX time, in milliseconds, that the most recent auto-renewable
subscription purchase expires.

Instance Property

# renewalDate

The UNIX time, in milliseconds, that the most recent auto-renewable
subscription purchase expires.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 17.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    @backDeployed(before: iOS 17.0, macOS 14.0, tvOS 17.0, watchOS 10.0, macCatalyst 17.0)
    var renewalDate: Date? { get }

## Discussion

The `renewalDate` is a value that’s always present for auto-renewable
subscriptions, even for expired subscriptions. This date indicates the
expiration date of the most recent auto-renewable subscription purchase,
including renewals, and may be in the past. For subscriptions that renew
successfully, the `renewalDate` is the date when the subscription renews.

## See Also

### Getting the renewal or expiration state

`let state: Product.SubscriptionInfo.RenewalState`

The renewal state of the auto-renewable subscription.

`let autoRenewPreference: String?`

The product ID of the auto-renewable subscription that will automatically
renew.

`let willAutoRenew: Bool`

A Boolean value that indicates whether the subscription will automatically
renew in the next period.

`let expirationReason: Product.SubscriptionInfo.RenewalInfo.ExpirationReason?`

The reason the auto-renewable subscription expired.

`struct Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The reasons for auto-renewable subscription expirations.

Instance Property

# isInBillingRetry

A Boolean value that indicates whether an auto-renewable subscription is in
the billing retry period.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let isInBillingRetry: Bool

## Discussion

This field indicates whether Apple is attempting to automatically renew an
expired subscription. If a subscription expires due to a billing issue, a
value of `true` indicates that Apple is still trying to renew the
subscription. If the subscription is in a billing grace period, the optional
`gracePeriodExpirationDate` contains a date.

Use the `isInBillingRetry` value along with `expirationReason` for more
insight, as the following table shows:

Values| Description  
---|---  
`isInBillingRetry` is `false,` `expirationReason` is `nil`| The auto-renewable
subscription is active and not in a billing retry period. The subscription is
entitled to service.  
`isInBillingRetry` is `true,``expirationReason` is
`billingError`,`gracePeriodExpirationDate` has a date| The auto-renewable
subscription is in a billing grace period. The subscription is entitled to
service until the date in `gracePeriodExpirationDate`.  
`isInBillingRetry` is `true,``expirationReason` is
`billingError`,`gracePeriodExpirationDate` is `nil`| The auto-renewable
subscription is in a billing retry period. The subscription is not entitled to
service.  
`isInBillingRetry` is `false,` `expirationReason` is `billingError`| The auto-
renewable subscription expired and billing retry wasn’t able to recover the
subscription.The subscription is not entitled to service.  
  
## See Also

### Getting billing status

`let gracePeriodExpirationDate: Date?`

The date the billing grace period expires for the auto-renewable subscription.

Instance Property

# gracePeriodExpirationDate

The date the billing grace period expires for the auto-renewable subscription.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let gracePeriodExpirationDate: Date?

## Discussion

This value is `nil` if the subscription is not in a billing grace period.

This date is present if you enable Billing Grace Period for your app and the
subscription is in the billing grace period. Ensure that your app provides
full service for the subscription throughout the grace period, which ends on
the `gracePeriodExpirationDate`.

A billing grace period occurs at the start of a billing retry state.
Throughout the billing grace period, the value of `isInBillingRetry` is
`true`, which indicates that Apple is attempting to automatically renew the
subscription.

For information about supporting Billing Grace Period, see Enable Billing
Grace Period for auto-renewable subscriptions and Reducing Involuntary
Subscriber Churn.

## See Also

### Getting billing status

`let isInBillingRetry: Bool`

A Boolean value that indicates whether an auto-renewable subscription is in
the billing retry period.

Article

# Managing Price Increases for Auto-Renewable Subscriptions

Identify the price increase status for auto-renewable subscriptions, in your
app and on your server.

## Overview

If you increase the price of an auto-renewable subscription in App Store
Connect, the `priceIncreaseStatus` in the `renewalInfo` object indicates if
the subscription is subject to the price increase. Auto-renewable
subscriptions have two types of price increases: those that require customer
consent, and those that don’t require customer consent.

For price increases that require customer consent, look for the following
status values in your app:

`Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus.noIncreasePending`|
Indicates there’s no price increase for this auto-renewable subscription.  
---|---  
`Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus.pending`| Indicates
there’s a pending price increase for the auto-renewable subscription that
requires customer consent, and the customer hasn’t yet consented. If the
customer doesn’t consent, the auto-renewable subscription expires at the end
of the billing cycle. When it expires, your app gets a status update in
`updates` with an `expirationReason` of `didNotConsentToPriceIncrease`.  
`Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus.agreed`| Indicates
that the customer consented to a price increase for the auto-renewable
subscription.  
  
For price increases that don’t require customer consent, look for the
following status values in your app:

`Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus.noIncreasePending`|
Doesn’t apply.  
---|---  
`Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus.pending`| Doesn’t
apply.  
`Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus.agreed`| Indicates
that the App Store informed the customer of the price increase for the auto-
renewable subscription, and the subscription is subject to the price
increase.If the customer cancels the auto-renewable subscription, your app
gets a status update in `updates` with an `expirationReason` of
`autoRenewDisabled`.  
  
For more information about managing subscription prices in App Store Connect,
see Managing Prices.

### Receive Notifications for Price Increase Status Events

If you’ve enabled App Store Server Notifications V2, your server receives
notifications for events related to auto-renewable subscription price
increases.

For auto-renewable subscription price increases that require customer consent,
look for the following notifications:

Notification type| Subtype| Description  
---|---|---  
`PRICE_INCREASE` | `PENDING`| Indicates that the App Store informed the customer of the price increase for the auto-renewable subscription, and the customer hasn’t yet responded.  
`PRICE_INCREASE`| `ACCEPTED`| Indicates that the customer consented to the
price increase for the auto-renewable subscription.  
`EXPIRED`| `PRICE_INCREASE`| Indicates that the auto-renewable subscription
expired because the customer didn’t consent to the price increase, and allowed
the subscription to expire.  
`EXPIRED`| `VOLUNTARY`| Indicates that the customer voluntarily canceled the
auto-renewable subscription. (Note: This notification type and subtype isn’t
specific to price increases.)  
  
For auto-renewable subscription price increases that don’t require customer
consent, look for the following notifications:

Notification type| Subtype| Description  
---|---|---  
`PRICE_INCREASE`| `ACCEPTED`| Indicates that the App Store informed the
customer of the auto-renewable subscription price increase, and the
subscription is subject to the price increase.  
`EXPIRED` | `VOLUNTARY`| Indicates that the customer voluntarily canceled the auto-renewable subscription. (Note: This notification type and subtype isn't specific to price increases.)  
  
For more information about App Store Server Notifications, see Enabling App
Store Server Notifications. For more information about notification types and
subtypes, see `notificationType` and `subtype`.

## See Also

### Getting the price increase status

`let priceIncreaseStatus:
Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus`

The status that indicates whether the auto-renewable subscription is subject
to a price increase.

`enum Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus`

Status values that indicate whether an auto-renewable subscription is subject
to a price increase.

Instance Property

# priceIncreaseStatus

The status that indicates whether the auto-renewable subscription is subject
to a price increase.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let priceIncreaseStatus: Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus

## Discussion

For more information about price increase status, see Managing Price Increases
for Auto-Renewable Subscriptions.

## See Also

### Getting the price increase status

Managing Price Increases for Auto-Renewable Subscriptions

Identify the price increase status for auto-renewable subscriptions, in your
app and on your server.

`enum Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus`

Status values that indicate whether an auto-renewable subscription is subject
to a price increase.

Instance Property

# deviceVerification

The device verification value to use to verify whether the renewal information
belongs to the device.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let deviceVerification: Data

## Discussion

For more information, see `deviceVerificationID`.

## See Also

### Verifying subscription renewal information

`let deviceVerificationNonce: UUID`

The UUID to use to compute the device verification value.

`let signedDate: Date`

The date that the App Store signed the JWS renewal information.

Instance Property

# deviceVerificationNonce

The UUID to use to compute the device verification value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let deviceVerificationNonce: UUID

## Discussion

For more information, see `deviceVerificationID`.

## See Also

### Verifying subscription renewal information

`let deviceVerification: Data`

The device verification value to use to verify whether the renewal information
belongs to the device.

`let signedDate: Date`

The date that the App Store signed the JWS renewal information.

Instance Property

# signedDate

The date that the App Store signed the JWS renewal information.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let signedDate: Date

## Discussion

Use the `signedDate` to verify whether the certificate used to sign the
transaction was valid when the App Store signed the transaction.

## See Also

### Verifying subscription renewal information

`let deviceVerification: Data`

The device verification value to use to verify whether the renewal information
belongs to the device.

`let deviceVerificationNonce: UUID`

The UUID to use to compute the device verification value.

Instance Property

# jsonRepresentation

The raw JSON representation of the subscription renewal information.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var jsonRepresentation: Data { get }

## Discussion

The information in `jsonRepresentation` is the same information that’s in the
properties of the same instance of `Product.SubscriptionInfo.RenewalInfo`.

Instance Property

# debugDescription

A string representation of the renewal info, suitable for debugging.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var debugDescription: String { get }

## Relationships

### From Protocol

  * `CustomDebugStringConvertible`

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func != (lhs: Product.SubscriptionInfo.RenewalInfo, rhs: Product.SubscriptionInfo.RenewalInfo) -> Bool

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

### Comparing and hashing renewal information

`static func == (Product.SubscriptionInfo.RenewalInfo,
Product.SubscriptionInfo.RenewalInfo) -> Bool`

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

    
    
    static func == (lhs: Product.SubscriptionInfo.RenewalInfo, rhs: Product.SubscriptionInfo.RenewalInfo) -> Bool

## See Also

### Comparing and hashing renewal information

`static func != (Product.SubscriptionInfo.RenewalInfo,
Product.SubscriptionInfo.RenewalInfo) -> Bool`

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

### Comparing and hashing renewal information

`static func != (Product.SubscriptionInfo.RenewalInfo,
Product.SubscriptionInfo.RenewalInfo) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (Product.SubscriptionInfo.RenewalInfo,
Product.SubscriptionInfo.RenewalInfo) -> Bool`

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

### Comparing and hashing renewal information

`static func != (Product.SubscriptionInfo.RenewalInfo,
Product.SubscriptionInfo.RenewalInfo) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (Product.SubscriptionInfo.RenewalInfo,
Product.SubscriptionInfo.RenewalInfo) -> Bool`

Returns a Boolean value that indicates whether two values are equal.

`func hash(into: inout Hasher)`

Hashes the essential components of the value by feeding them into the given
hasher.

Instance Property

# environment

The server environment that signs the renewal information for an auto-
renewable subscription.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    let environment: AppStore.Environment

## See Also

### Getting the environment

`@backDeployed(before: iOS 16.0, macOS 13.0, tvOS 16.0, watchOS 9.0,
macCatalyst 16.0) var environmentStringRepresentation: String`

The string representation of the server environment that signs the renewal
information for an auto-renewable subscription.

Deprecated

Instance Property

# environmentStringRepresentation

The string representation of the server environment that signs the renewal
information for an auto-renewable subscription.

iOS 15.0–16.0  Deprecated  iPadOS 15.0–16.0  Deprecated  macOS 12.0–13.0
Deprecated  Mac Catalyst 16.0–16.0  Deprecated  tvOS 15.0–16.0  Deprecated
watchOS 8.0–9.0  Deprecated  Xcode 13.0–14.0  Deprecated

    
    
    @backDeployed(before: iOS 16.0, macOS 13.0, tvOS 16.0, watchOS 9.0, macCatalyst 16.0)
    var environmentStringRepresentation: String { get }

## See Also

### Getting the environment

`let environment: AppStore.Environment`

The server environment that signs the renewal information for an auto-
renewable subscription.

Instance Property

# originalTransactionID

The transaction identifier of the original purchase.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let originalTransactionID: UInt64

Instance Property

# currentProductID

The subscription product ID that the customer is subscribed to.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let currentProductID: String

Instance Property

# offerID

A string that identifies an offer applied to the next subscription period.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let offerID: String?

## Discussion

This value is `nil` if there isn’t an offer, or if the offer type is
`introductory`.

If the offer type is `promotional`, this value contains the promotional offer
identifier you set up in App Store Connect. For more information about
promotional offers, see Set up promotional offers for auto-renewable
subscriptions.

If the offer type is `code`, this value contains the reference name of the
offer code you set up in App Store Connect. For more information about offer
codes, see Set up offer codes.

## See Also

### Getting subscription offers

`let offerType: Transaction.OfferType?`

The subscription offer type for the next subscription period.

Instance Property

# offerType

The subscription offer type for the next subscription period.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let offerType: Transaction.OfferType?

## Discussion

If this value is `nil`, there’s no offer applied.

## See Also

### Getting subscription offers

`let offerID: String?`

A string that identifies an offer applied to the next subscription period.

Instance Property

# recentSubscriptionStartDate

The earliest start date of a subscription in a series of auto-renewable
subscription purchases that ignores all lapses of paid service shorter than 60
days.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 16.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 14.0+

    
    
    @backDeployed(before: iOS 16.0, macOS 13.0, tvOS 16.0, watchOS 9.0, macCatalyst 16.0)
    var recentSubscriptionStartDate: Date { get }

## Discussion

Important

Don’t use the `recentSubscriptionStartDate` date to calculate days of paid
service. For more information about paid days of service, see Net revenue
after a year.

Instance Property

# state

The renewal state of the auto-renewable subscription.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let state: Product.SubscriptionInfo.RenewalState

## See Also

### Getting subscription status information

`let renewalInfo: VerificationResult<Product.SubscriptionInfo.RenewalInfo>`

The signed renewal information for the auto-renewable subscription.

`let transaction: VerificationResult<Transaction>`

The latest transaction for the subscription group.

`struct Product.SubscriptionInfo.RenewalInfo`

The renewal information for an auto-renewable subscription.

`struct Product.SubscriptionInfo.RenewalState`

The renewal states of auto-renewable subscriptions.

Instance Property

# autoRenewPreference

The product ID of the auto-renewable subscription that will automatically
renew.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let autoRenewPreference: String?

## Discussion

This value is the product ID of the auto-renewable subscription that will
renew after the current period expires. The value may be:

  * The same as `currentProductID` if the subscription will renew with the same product.

  * Another product ID value if the subscription will renew to a different product.

  * `nil` if the subscription won’t renew in the next period. This may occur for several reasons, including when the person disables auto-renew for the subscription, the subscription lapses due to a billing issue, or you increase the subscription price and the person doesn't accept the increase.

## See Also

### Getting the renewal or expiration state

`let state: Product.SubscriptionInfo.RenewalState`

The renewal state of the auto-renewable subscription.

`let willAutoRenew: Bool`

A Boolean value that indicates whether the subscription will automatically
renew in the next period.

`let expirationReason: Product.SubscriptionInfo.RenewalInfo.ExpirationReason?`

The reason the auto-renewable subscription expired.

`struct Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The reasons for auto-renewable subscription expirations.

`@backDeployed(before: iOS 17.0, macOS 14.0, tvOS 17.0, watchOS 10.0,
macCatalyst 17.0) var renewalDate: Date?`

The UNIX time, in milliseconds, that the most recent auto-renewable
subscription purchase expires.

Instance Property

# willAutoRenew

A Boolean value that indicates whether the subscription will automatically
renew in the next period.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let willAutoRenew: Bool

## See Also

### Getting the renewal or expiration state

`let state: Product.SubscriptionInfo.RenewalState`

The renewal state of the auto-renewable subscription.

`let autoRenewPreference: String?`

The product ID of the auto-renewable subscription that will automatically
renew.

`let expirationReason: Product.SubscriptionInfo.RenewalInfo.ExpirationReason?`

The reason the auto-renewable subscription expired.

`struct Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The reasons for auto-renewable subscription expirations.

`@backDeployed(before: iOS 17.0, macOS 14.0, tvOS 17.0, watchOS 10.0,
macCatalyst 17.0) var renewalDate: Date?`

The UNIX time, in milliseconds, that the most recent auto-renewable
subscription purchase expires.

Instance Property

# expirationReason

The reason the auto-renewable subscription expired.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let expirationReason: Product.SubscriptionInfo.RenewalInfo.ExpirationReason?

## Discussion

This optional value is `nil` if the auto-renewable subscription is active and
hasn’t expired.

## See Also

### Getting the renewal or expiration state

`let state: Product.SubscriptionInfo.RenewalState`

The renewal state of the auto-renewable subscription.

`let autoRenewPreference: String?`

The product ID of the auto-renewable subscription that will automatically
renew.

`let willAutoRenew: Bool`

A Boolean value that indicates whether the subscription will automatically
renew in the next period.

`struct Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The reasons for auto-renewable subscription expirations.

`@backDeployed(before: iOS 17.0, macOS 14.0, tvOS 17.0, watchOS 10.0,
macCatalyst 17.0) var renewalDate: Date?`

The UNIX time, in milliseconds, that the most recent auto-renewable
subscription purchase expires.

Instance Property

# renewalDate

The UNIX time, in milliseconds, that the most recent auto-renewable
subscription purchase expires.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 17.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    @backDeployed(before: iOS 17.0, macOS 14.0, tvOS 17.0, watchOS 10.0, macCatalyst 17.0)
    var renewalDate: Date? { get }

## Discussion

The `renewalDate` is a value that’s always present for auto-renewable
subscriptions, even for expired subscriptions. This date indicates the
expiration date of the most recent auto-renewable subscription purchase,
including renewals, and may be in the past. For subscriptions that renew
successfully, the `renewalDate` is the date when the subscription renews.

## See Also

### Getting the renewal or expiration state

`let state: Product.SubscriptionInfo.RenewalState`

The renewal state of the auto-renewable subscription.

`let autoRenewPreference: String?`

The product ID of the auto-renewable subscription that will automatically
renew.

`let willAutoRenew: Bool`

A Boolean value that indicates whether the subscription will automatically
renew in the next period.

`let expirationReason: Product.SubscriptionInfo.RenewalInfo.ExpirationReason?`

The reason the auto-renewable subscription expired.

`struct Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The reasons for auto-renewable subscription expirations.

Instance Property

# isInBillingRetry

A Boolean value that indicates whether an auto-renewable subscription is in
the billing retry period.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let isInBillingRetry: Bool

## Discussion

This field indicates whether Apple is attempting to automatically renew an
expired subscription. If a subscription expires due to a billing issue, a
value of `true` indicates that Apple is still trying to renew the
subscription. If the subscription is in a billing grace period, the optional
`gracePeriodExpirationDate` contains a date.

Use the `isInBillingRetry` value along with `expirationReason` for more
insight, as the following table shows:

Values| Description  
---|---  
`isInBillingRetry` is `false,` `expirationReason` is `nil`| The auto-renewable
subscription is active and not in a billing retry period. The subscription is
entitled to service.  
`isInBillingRetry` is `true,``expirationReason` is
`billingError`,`gracePeriodExpirationDate` has a date| The auto-renewable
subscription is in a billing grace period. The subscription is entitled to
service until the date in `gracePeriodExpirationDate`.  
`isInBillingRetry` is `true,``expirationReason` is
`billingError`,`gracePeriodExpirationDate` is `nil`| The auto-renewable
subscription is in a billing retry period. The subscription is not entitled to
service.  
`isInBillingRetry` is `false,` `expirationReason` is `billingError`| The auto-
renewable subscription expired and billing retry wasn’t able to recover the
subscription.The subscription is not entitled to service.  
  
## See Also

### Getting billing status

`let gracePeriodExpirationDate: Date?`

The date the billing grace period expires for the auto-renewable subscription.

Instance Property

# gracePeriodExpirationDate

The date the billing grace period expires for the auto-renewable subscription.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let gracePeriodExpirationDate: Date?

## Discussion

This value is `nil` if the subscription is not in a billing grace period.

This date is present if you enable Billing Grace Period for your app and the
subscription is in the billing grace period. Ensure that your app provides
full service for the subscription throughout the grace period, which ends on
the `gracePeriodExpirationDate`.

A billing grace period occurs at the start of a billing retry state.
Throughout the billing grace period, the value of `isInBillingRetry` is
`true`, which indicates that Apple is attempting to automatically renew the
subscription.

For information about supporting Billing Grace Period, see Enable Billing
Grace Period for auto-renewable subscriptions and Reducing Involuntary
Subscriber Churn.

## See Also

### Getting billing status

`let isInBillingRetry: Bool`

A Boolean value that indicates whether an auto-renewable subscription is in
the billing retry period.

Article

# Managing Price Increases for Auto-Renewable Subscriptions

Identify the price increase status for auto-renewable subscriptions, in your
app and on your server.

## Overview

If you increase the price of an auto-renewable subscription in App Store
Connect, the `priceIncreaseStatus` in the `renewalInfo` object indicates if
the subscription is subject to the price increase. Auto-renewable
subscriptions have two types of price increases: those that require customer
consent, and those that don’t require customer consent.

For price increases that require customer consent, look for the following
status values in your app:

`Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus.noIncreasePending`|
Indicates there’s no price increase for this auto-renewable subscription.  
---|---  
`Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus.pending`| Indicates
there’s a pending price increase for the auto-renewable subscription that
requires customer consent, and the customer hasn’t yet consented. If the
customer doesn’t consent, the auto-renewable subscription expires at the end
of the billing cycle. When it expires, your app gets a status update in
`updates` with an `expirationReason` of `didNotConsentToPriceIncrease`.  
`Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus.agreed`| Indicates
that the customer consented to a price increase for the auto-renewable
subscription.  
  
For price increases that don’t require customer consent, look for the
following status values in your app:

`Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus.noIncreasePending`|
Doesn’t apply.  
---|---  
`Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus.pending`| Doesn’t
apply.  
`Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus.agreed`| Indicates
that the App Store informed the customer of the price increase for the auto-
renewable subscription, and the subscription is subject to the price
increase.If the customer cancels the auto-renewable subscription, your app
gets a status update in `updates` with an `expirationReason` of
`autoRenewDisabled`.  
  
For more information about managing subscription prices in App Store Connect,
see Managing Prices.

### Receive Notifications for Price Increase Status Events

If you’ve enabled App Store Server Notifications V2, your server receives
notifications for events related to auto-renewable subscription price
increases.

For auto-renewable subscription price increases that require customer consent,
look for the following notifications:

Notification type| Subtype| Description  
---|---|---  
`PRICE_INCREASE` | `PENDING`| Indicates that the App Store informed the customer of the price increase for the auto-renewable subscription, and the customer hasn’t yet responded.  
`PRICE_INCREASE`| `ACCEPTED`| Indicates that the customer consented to the
price increase for the auto-renewable subscription.  
`EXPIRED`| `PRICE_INCREASE`| Indicates that the auto-renewable subscription
expired because the customer didn’t consent to the price increase, and allowed
the subscription to expire.  
`EXPIRED`| `VOLUNTARY`| Indicates that the customer voluntarily canceled the
auto-renewable subscription. (Note: This notification type and subtype isn’t
specific to price increases.)  
  
For auto-renewable subscription price increases that don’t require customer
consent, look for the following notifications:

Notification type| Subtype| Description  
---|---|---  
`PRICE_INCREASE`| `ACCEPTED`| Indicates that the App Store informed the
customer of the auto-renewable subscription price increase, and the
subscription is subject to the price increase.  
`EXPIRED` | `VOLUNTARY`| Indicates that the customer voluntarily canceled the auto-renewable subscription. (Note: This notification type and subtype isn't specific to price increases.)  
  
For more information about App Store Server Notifications, see Enabling App
Store Server Notifications. For more information about notification types and
subtypes, see `notificationType` and `subtype`.

## See Also

### Getting the price increase status

`let priceIncreaseStatus:
Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus`

The status that indicates whether the auto-renewable subscription is subject
to a price increase.

`enum Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus`

Status values that indicate whether an auto-renewable subscription is subject
to a price increase.

Instance Property

# priceIncreaseStatus

The status that indicates whether the auto-renewable subscription is subject
to a price increase.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let priceIncreaseStatus: Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus

## Discussion

For more information about price increase status, see Managing Price Increases
for Auto-Renewable Subscriptions.

## See Also

### Getting the price increase status

Managing Price Increases for Auto-Renewable Subscriptions

Identify the price increase status for auto-renewable subscriptions, in your
app and on your server.

`enum Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus`

Status values that indicate whether an auto-renewable subscription is subject
to a price increase.

Instance Property

# deviceVerification

The device verification value to use to verify whether the renewal information
belongs to the device.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let deviceVerification: Data

## Discussion

For more information, see `deviceVerificationID`.

## See Also

### Verifying subscription renewal information

`let deviceVerificationNonce: UUID`

The UUID to use to compute the device verification value.

`let signedDate: Date`

The date that the App Store signed the JWS renewal information.

Instance Property

# deviceVerificationNonce

The UUID to use to compute the device verification value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let deviceVerificationNonce: UUID

## Discussion

For more information, see `deviceVerificationID`.

## See Also

### Verifying subscription renewal information

`let deviceVerification: Data`

The device verification value to use to verify whether the renewal information
belongs to the device.

`let signedDate: Date`

The date that the App Store signed the JWS renewal information.

Instance Property

# signedDate

The date that the App Store signed the JWS renewal information.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let signedDate: Date

## Discussion

Use the `signedDate` to verify whether the certificate used to sign the
transaction was valid when the App Store signed the transaction.

## See Also

### Verifying subscription renewal information

`let deviceVerification: Data`

The device verification value to use to verify whether the renewal information
belongs to the device.

`let deviceVerificationNonce: UUID`

The UUID to use to compute the device verification value.

Instance Property

# jsonRepresentation

The raw JSON representation of the subscription renewal information.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var jsonRepresentation: Data { get }

## Discussion

The information in `jsonRepresentation` is the same information that’s in the
properties of the same instance of `Product.SubscriptionInfo.RenewalInfo`.

Instance Property

# debugDescription

A string representation of the renewal info, suitable for debugging.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var debugDescription: String { get }

## Relationships

### From Protocol

  * `CustomDebugStringConvertible`

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func != (lhs: Product.SubscriptionInfo.RenewalInfo, rhs: Product.SubscriptionInfo.RenewalInfo) -> Bool

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

### Comparing and hashing renewal information

`static func == (Product.SubscriptionInfo.RenewalInfo,
Product.SubscriptionInfo.RenewalInfo) -> Bool`

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

    
    
    static func == (lhs: Product.SubscriptionInfo.RenewalInfo, rhs: Product.SubscriptionInfo.RenewalInfo) -> Bool

## See Also

### Comparing and hashing renewal information

`static func != (Product.SubscriptionInfo.RenewalInfo,
Product.SubscriptionInfo.RenewalInfo) -> Bool`

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

### Comparing and hashing renewal information

`static func != (Product.SubscriptionInfo.RenewalInfo,
Product.SubscriptionInfo.RenewalInfo) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (Product.SubscriptionInfo.RenewalInfo,
Product.SubscriptionInfo.RenewalInfo) -> Bool`

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

### Comparing and hashing renewal information

`static func != (Product.SubscriptionInfo.RenewalInfo,
Product.SubscriptionInfo.RenewalInfo) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (Product.SubscriptionInfo.RenewalInfo,
Product.SubscriptionInfo.RenewalInfo) -> Bool`

Returns a Boolean value that indicates whether two values are equal.

`func hash(into: inout Hasher)`

Hashes the essential components of the value by feeding them into the given
hasher.

Instance Property

# environment

The server environment that signs the renewal information for an auto-
renewable subscription.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    let environment: AppStore.Environment

## See Also

### Getting the environment

`@backDeployed(before: iOS 16.0, macOS 13.0, tvOS 16.0, watchOS 9.0,
macCatalyst 16.0) var environmentStringRepresentation: String`

The string representation of the server environment that signs the renewal
information for an auto-renewable subscription.

Deprecated

Instance Property

# environmentStringRepresentation

The string representation of the server environment that signs the renewal
information for an auto-renewable subscription.

iOS 15.0–16.0  Deprecated  iPadOS 15.0–16.0  Deprecated  macOS 12.0–13.0
Deprecated  Mac Catalyst 16.0–16.0  Deprecated  tvOS 15.0–16.0  Deprecated
watchOS 8.0–9.0  Deprecated  Xcode 13.0–14.0  Deprecated

    
    
    @backDeployed(before: iOS 16.0, macOS 13.0, tvOS 16.0, watchOS 9.0, macCatalyst 16.0)
    var environmentStringRepresentation: String { get }

## See Also

### Getting the environment

`let environment: AppStore.Environment`

The server environment that signs the renewal information for an auto-
renewable subscription.

Instance Property

# originalTransactionID

The transaction identifier of the original purchase.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let originalTransactionID: UInt64

Instance Property

# currentProductID

The subscription product ID that the customer is subscribed to.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let currentProductID: String

Instance Property

# offerID

A string that identifies an offer applied to the next subscription period.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let offerID: String?

## Discussion

This value is `nil` if there isn’t an offer, or if the offer type is
`introductory`.

If the offer type is `promotional`, this value contains the promotional offer
identifier you set up in App Store Connect. For more information about
promotional offers, see Set up promotional offers for auto-renewable
subscriptions.

If the offer type is `code`, this value contains the reference name of the
offer code you set up in App Store Connect. For more information about offer
codes, see Set up offer codes.

## See Also

### Getting subscription offers

`let offerType: Transaction.OfferType?`

The subscription offer type for the next subscription period.

Instance Property

# offerType

The subscription offer type for the next subscription period.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let offerType: Transaction.OfferType?

## Discussion

If this value is `nil`, there’s no offer applied.

## See Also

### Getting subscription offers

`let offerID: String?`

A string that identifies an offer applied to the next subscription period.

Instance Property

# recentSubscriptionStartDate

The earliest start date of a subscription in a series of auto-renewable
subscription purchases that ignores all lapses of paid service shorter than 60
days.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 16.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 14.0+

    
    
    @backDeployed(before: iOS 16.0, macOS 13.0, tvOS 16.0, watchOS 9.0, macCatalyst 16.0)
    var recentSubscriptionStartDate: Date { get }

## Discussion

Important

Don’t use the `recentSubscriptionStartDate` date to calculate days of paid
service. For more information about paid days of service, see Net revenue
after a year.

Instance Property

# state

The renewal state of the auto-renewable subscription.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let state: Product.SubscriptionInfo.RenewalState

## See Also

### Getting subscription status information

`let renewalInfo: VerificationResult<Product.SubscriptionInfo.RenewalInfo>`

The signed renewal information for the auto-renewable subscription.

`let transaction: VerificationResult<Transaction>`

The latest transaction for the subscription group.

`struct Product.SubscriptionInfo.RenewalInfo`

The renewal information for an auto-renewable subscription.

`struct Product.SubscriptionInfo.RenewalState`

The renewal states of auto-renewable subscriptions.

Instance Property

# autoRenewPreference

The product ID of the auto-renewable subscription that will automatically
renew.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let autoRenewPreference: String?

## Discussion

This value is the product ID of the auto-renewable subscription that will
renew after the current period expires. The value may be:

  * The same as `currentProductID` if the subscription will renew with the same product.

  * Another product ID value if the subscription will renew to a different product.

  * `nil` if the subscription won’t renew in the next period. This may occur for several reasons, including when the person disables auto-renew for the subscription, the subscription lapses due to a billing issue, or you increase the subscription price and the person doesn't accept the increase.

## See Also

### Getting the renewal or expiration state

`let state: Product.SubscriptionInfo.RenewalState`

The renewal state of the auto-renewable subscription.

`let willAutoRenew: Bool`

A Boolean value that indicates whether the subscription will automatically
renew in the next period.

`let expirationReason: Product.SubscriptionInfo.RenewalInfo.ExpirationReason?`

The reason the auto-renewable subscription expired.

`struct Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The reasons for auto-renewable subscription expirations.

`@backDeployed(before: iOS 17.0, macOS 14.0, tvOS 17.0, watchOS 10.0,
macCatalyst 17.0) var renewalDate: Date?`

The UNIX time, in milliseconds, that the most recent auto-renewable
subscription purchase expires.

Instance Property

# willAutoRenew

A Boolean value that indicates whether the subscription will automatically
renew in the next period.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let willAutoRenew: Bool

## See Also

### Getting the renewal or expiration state

`let state: Product.SubscriptionInfo.RenewalState`

The renewal state of the auto-renewable subscription.

`let autoRenewPreference: String?`

The product ID of the auto-renewable subscription that will automatically
renew.

`let expirationReason: Product.SubscriptionInfo.RenewalInfo.ExpirationReason?`

The reason the auto-renewable subscription expired.

`struct Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The reasons for auto-renewable subscription expirations.

`@backDeployed(before: iOS 17.0, macOS 14.0, tvOS 17.0, watchOS 10.0,
macCatalyst 17.0) var renewalDate: Date?`

The UNIX time, in milliseconds, that the most recent auto-renewable
subscription purchase expires.

Instance Property

# expirationReason

The reason the auto-renewable subscription expired.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let expirationReason: Product.SubscriptionInfo.RenewalInfo.ExpirationReason?

## Discussion

This optional value is `nil` if the auto-renewable subscription is active and
hasn’t expired.

## See Also

### Getting the renewal or expiration state

`let state: Product.SubscriptionInfo.RenewalState`

The renewal state of the auto-renewable subscription.

`let autoRenewPreference: String?`

The product ID of the auto-renewable subscription that will automatically
renew.

`let willAutoRenew: Bool`

A Boolean value that indicates whether the subscription will automatically
renew in the next period.

`struct Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The reasons for auto-renewable subscription expirations.

`@backDeployed(before: iOS 17.0, macOS 14.0, tvOS 17.0, watchOS 10.0,
macCatalyst 17.0) var renewalDate: Date?`

The UNIX time, in milliseconds, that the most recent auto-renewable
subscription purchase expires.

Instance Property

# renewalDate

The UNIX time, in milliseconds, that the most recent auto-renewable
subscription purchase expires.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 17.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    @backDeployed(before: iOS 17.0, macOS 14.0, tvOS 17.0, watchOS 10.0, macCatalyst 17.0)
    var renewalDate: Date? { get }

## Discussion

The `renewalDate` is a value that’s always present for auto-renewable
subscriptions, even for expired subscriptions. This date indicates the
expiration date of the most recent auto-renewable subscription purchase,
including renewals, and may be in the past. For subscriptions that renew
successfully, the `renewalDate` is the date when the subscription renews.

## See Also

### Getting the renewal or expiration state

`let state: Product.SubscriptionInfo.RenewalState`

The renewal state of the auto-renewable subscription.

`let autoRenewPreference: String?`

The product ID of the auto-renewable subscription that will automatically
renew.

`let willAutoRenew: Bool`

A Boolean value that indicates whether the subscription will automatically
renew in the next period.

`let expirationReason: Product.SubscriptionInfo.RenewalInfo.ExpirationReason?`

The reason the auto-renewable subscription expired.

`struct Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The reasons for auto-renewable subscription expirations.

Instance Property

# isInBillingRetry

A Boolean value that indicates whether an auto-renewable subscription is in
the billing retry period.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let isInBillingRetry: Bool

## Discussion

This field indicates whether Apple is attempting to automatically renew an
expired subscription. If a subscription expires due to a billing issue, a
value of `true` indicates that Apple is still trying to renew the
subscription. If the subscription is in a billing grace period, the optional
`gracePeriodExpirationDate` contains a date.

Use the `isInBillingRetry` value along with `expirationReason` for more
insight, as the following table shows:

Values| Description  
---|---  
`isInBillingRetry` is `false,` `expirationReason` is `nil`| The auto-renewable
subscription is active and not in a billing retry period. The subscription is
entitled to service.  
`isInBillingRetry` is `true,``expirationReason` is
`billingError`,`gracePeriodExpirationDate` has a date| The auto-renewable
subscription is in a billing grace period. The subscription is entitled to
service until the date in `gracePeriodExpirationDate`.  
`isInBillingRetry` is `true,``expirationReason` is
`billingError`,`gracePeriodExpirationDate` is `nil`| The auto-renewable
subscription is in a billing retry period. The subscription is not entitled to
service.  
`isInBillingRetry` is `false,` `expirationReason` is `billingError`| The auto-
renewable subscription expired and billing retry wasn’t able to recover the
subscription.The subscription is not entitled to service.  
  
## See Also

### Getting billing status

`let gracePeriodExpirationDate: Date?`

The date the billing grace period expires for the auto-renewable subscription.

Instance Property

# gracePeriodExpirationDate

The date the billing grace period expires for the auto-renewable subscription.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let gracePeriodExpirationDate: Date?

## Discussion

This value is `nil` if the subscription is not in a billing grace period.

This date is present if you enable Billing Grace Period for your app and the
subscription is in the billing grace period. Ensure that your app provides
full service for the subscription throughout the grace period, which ends on
the `gracePeriodExpirationDate`.

A billing grace period occurs at the start of a billing retry state.
Throughout the billing grace period, the value of `isInBillingRetry` is
`true`, which indicates that Apple is attempting to automatically renew the
subscription.

For information about supporting Billing Grace Period, see Enable Billing
Grace Period for auto-renewable subscriptions and Reducing Involuntary
Subscriber Churn.

## See Also

### Getting billing status

`let isInBillingRetry: Bool`

A Boolean value that indicates whether an auto-renewable subscription is in
the billing retry period.

Article

# Managing Price Increases for Auto-Renewable Subscriptions

Identify the price increase status for auto-renewable subscriptions, in your
app and on your server.

## Overview

If you increase the price of an auto-renewable subscription in App Store
Connect, the `priceIncreaseStatus` in the `renewalInfo` object indicates if
the subscription is subject to the price increase. Auto-renewable
subscriptions have two types of price increases: those that require customer
consent, and those that don’t require customer consent.

For price increases that require customer consent, look for the following
status values in your app:

`Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus.noIncreasePending`|
Indicates there’s no price increase for this auto-renewable subscription.  
---|---  
`Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus.pending`| Indicates
there’s a pending price increase for the auto-renewable subscription that
requires customer consent, and the customer hasn’t yet consented. If the
customer doesn’t consent, the auto-renewable subscription expires at the end
of the billing cycle. When it expires, your app gets a status update in
`updates` with an `expirationReason` of `didNotConsentToPriceIncrease`.  
`Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus.agreed`| Indicates
that the customer consented to a price increase for the auto-renewable
subscription.  
  
For price increases that don’t require customer consent, look for the
following status values in your app:

`Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus.noIncreasePending`|
Doesn’t apply.  
---|---  
`Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus.pending`| Doesn’t
apply.  
`Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus.agreed`| Indicates
that the App Store informed the customer of the price increase for the auto-
renewable subscription, and the subscription is subject to the price
increase.If the customer cancels the auto-renewable subscription, your app
gets a status update in `updates` with an `expirationReason` of
`autoRenewDisabled`.  
  
For more information about managing subscription prices in App Store Connect,
see Managing Prices.

### Receive Notifications for Price Increase Status Events

If you’ve enabled App Store Server Notifications V2, your server receives
notifications for events related to auto-renewable subscription price
increases.

For auto-renewable subscription price increases that require customer consent,
look for the following notifications:

Notification type| Subtype| Description  
---|---|---  
`PRICE_INCREASE` | `PENDING`| Indicates that the App Store informed the customer of the price increase for the auto-renewable subscription, and the customer hasn’t yet responded.  
`PRICE_INCREASE`| `ACCEPTED`| Indicates that the customer consented to the
price increase for the auto-renewable subscription.  
`EXPIRED`| `PRICE_INCREASE`| Indicates that the auto-renewable subscription
expired because the customer didn’t consent to the price increase, and allowed
the subscription to expire.  
`EXPIRED`| `VOLUNTARY`| Indicates that the customer voluntarily canceled the
auto-renewable subscription. (Note: This notification type and subtype isn’t
specific to price increases.)  
  
For auto-renewable subscription price increases that don’t require customer
consent, look for the following notifications:

Notification type| Subtype| Description  
---|---|---  
`PRICE_INCREASE`| `ACCEPTED`| Indicates that the App Store informed the
customer of the auto-renewable subscription price increase, and the
subscription is subject to the price increase.  
`EXPIRED` | `VOLUNTARY`| Indicates that the customer voluntarily canceled the auto-renewable subscription. (Note: This notification type and subtype isn't specific to price increases.)  
  
For more information about App Store Server Notifications, see Enabling App
Store Server Notifications. For more information about notification types and
subtypes, see `notificationType` and `subtype`.

## See Also

### Getting the price increase status

`let priceIncreaseStatus:
Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus`

The status that indicates whether the auto-renewable subscription is subject
to a price increase.

`enum Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus`

Status values that indicate whether an auto-renewable subscription is subject
to a price increase.

Instance Property

# priceIncreaseStatus

The status that indicates whether the auto-renewable subscription is subject
to a price increase.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let priceIncreaseStatus: Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus

## Discussion

For more information about price increase status, see Managing Price Increases
for Auto-Renewable Subscriptions.

## See Also

### Getting the price increase status

Managing Price Increases for Auto-Renewable Subscriptions

Identify the price increase status for auto-renewable subscriptions, in your
app and on your server.

`enum Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus`

Status values that indicate whether an auto-renewable subscription is subject
to a price increase.

Instance Property

# deviceVerification

The device verification value to use to verify whether the renewal information
belongs to the device.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let deviceVerification: Data

## Discussion

For more information, see `deviceVerificationID`.

## See Also

### Verifying subscription renewal information

`let deviceVerificationNonce: UUID`

The UUID to use to compute the device verification value.

`let signedDate: Date`

The date that the App Store signed the JWS renewal information.

Instance Property

# deviceVerificationNonce

The UUID to use to compute the device verification value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let deviceVerificationNonce: UUID

## Discussion

For more information, see `deviceVerificationID`.

## See Also

### Verifying subscription renewal information

`let deviceVerification: Data`

The device verification value to use to verify whether the renewal information
belongs to the device.

`let signedDate: Date`

The date that the App Store signed the JWS renewal information.

Instance Property

# signedDate

The date that the App Store signed the JWS renewal information.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let signedDate: Date

## Discussion

Use the `signedDate` to verify whether the certificate used to sign the
transaction was valid when the App Store signed the transaction.

## See Also

### Verifying subscription renewal information

`let deviceVerification: Data`

The device verification value to use to verify whether the renewal information
belongs to the device.

`let deviceVerificationNonce: UUID`

The UUID to use to compute the device verification value.

Instance Property

# jsonRepresentation

The raw JSON representation of the subscription renewal information.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var jsonRepresentation: Data { get }

## Discussion

The information in `jsonRepresentation` is the same information that’s in the
properties of the same instance of `Product.SubscriptionInfo.RenewalInfo`.

Instance Property

# debugDescription

A string representation of the renewal info, suitable for debugging.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var debugDescription: String { get }

## Relationships

### From Protocol

  * `CustomDebugStringConvertible`

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func != (lhs: Product.SubscriptionInfo.RenewalInfo, rhs: Product.SubscriptionInfo.RenewalInfo) -> Bool

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

### Comparing and hashing renewal information

`static func == (Product.SubscriptionInfo.RenewalInfo,
Product.SubscriptionInfo.RenewalInfo) -> Bool`

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

    
    
    static func == (lhs: Product.SubscriptionInfo.RenewalInfo, rhs: Product.SubscriptionInfo.RenewalInfo) -> Bool

## See Also

### Comparing and hashing renewal information

`static func != (Product.SubscriptionInfo.RenewalInfo,
Product.SubscriptionInfo.RenewalInfo) -> Bool`

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

### Comparing and hashing renewal information

`static func != (Product.SubscriptionInfo.RenewalInfo,
Product.SubscriptionInfo.RenewalInfo) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (Product.SubscriptionInfo.RenewalInfo,
Product.SubscriptionInfo.RenewalInfo) -> Bool`

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

### Comparing and hashing renewal information

`static func != (Product.SubscriptionInfo.RenewalInfo,
Product.SubscriptionInfo.RenewalInfo) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (Product.SubscriptionInfo.RenewalInfo,
Product.SubscriptionInfo.RenewalInfo) -> Bool`

Returns a Boolean value that indicates whether two values are equal.

`func hash(into: inout Hasher)`

Hashes the essential components of the value by feeding them into the given
hasher.

Instance Property

# environment

The server environment that signs the renewal information for an auto-
renewable subscription.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    let environment: AppStore.Environment

## See Also

### Getting the environment

`@backDeployed(before: iOS 16.0, macOS 13.0, tvOS 16.0, watchOS 9.0,
macCatalyst 16.0) var environmentStringRepresentation: String`

The string representation of the server environment that signs the renewal
information for an auto-renewable subscription.

Deprecated

Instance Property

# environmentStringRepresentation

The string representation of the server environment that signs the renewal
information for an auto-renewable subscription.

iOS 15.0–16.0  Deprecated  iPadOS 15.0–16.0  Deprecated  macOS 12.0–13.0
Deprecated  Mac Catalyst 16.0–16.0  Deprecated  tvOS 15.0–16.0  Deprecated
watchOS 8.0–9.0  Deprecated  Xcode 13.0–14.0  Deprecated

    
    
    @backDeployed(before: iOS 16.0, macOS 13.0, tvOS 16.0, watchOS 9.0, macCatalyst 16.0)
    var environmentStringRepresentation: String { get }

## See Also

### Getting the environment

`let environment: AppStore.Environment`

The server environment that signs the renewal information for an auto-
renewable subscription.

Instance Property

# originalTransactionID

The transaction identifier of the original purchase.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let originalTransactionID: UInt64

Instance Property

# currentProductID

The subscription product ID that the customer is subscribed to.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let currentProductID: String

Instance Property

# offerID

A string that identifies an offer applied to the next subscription period.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let offerID: String?

## Discussion

This value is `nil` if there isn’t an offer, or if the offer type is
`introductory`.

If the offer type is `promotional`, this value contains the promotional offer
identifier you set up in App Store Connect. For more information about
promotional offers, see Set up promotional offers for auto-renewable
subscriptions.

If the offer type is `code`, this value contains the reference name of the
offer code you set up in App Store Connect. For more information about offer
codes, see Set up offer codes.

## See Also

### Getting subscription offers

`let offerType: Transaction.OfferType?`

The subscription offer type for the next subscription period.

Instance Property

# offerType

The subscription offer type for the next subscription period.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let offerType: Transaction.OfferType?

## Discussion

If this value is `nil`, there’s no offer applied.

## See Also

### Getting subscription offers

`let offerID: String?`

A string that identifies an offer applied to the next subscription period.

Instance Property

# recentSubscriptionStartDate

The earliest start date of a subscription in a series of auto-renewable
subscription purchases that ignores all lapses of paid service shorter than 60
days.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 16.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 14.0+

    
    
    @backDeployed(before: iOS 16.0, macOS 13.0, tvOS 16.0, watchOS 9.0, macCatalyst 16.0)
    var recentSubscriptionStartDate: Date { get }

## Discussion

Important

Don’t use the `recentSubscriptionStartDate` date to calculate days of paid
service. For more information about paid days of service, see Net revenue
after a year.

Instance Property

# state

The renewal state of the auto-renewable subscription.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let state: Product.SubscriptionInfo.RenewalState

## See Also

### Getting subscription status information

`let renewalInfo: VerificationResult<Product.SubscriptionInfo.RenewalInfo>`

The signed renewal information for the auto-renewable subscription.

`let transaction: VerificationResult<Transaction>`

The latest transaction for the subscription group.

`struct Product.SubscriptionInfo.RenewalInfo`

The renewal information for an auto-renewable subscription.

`struct Product.SubscriptionInfo.RenewalState`

The renewal states of auto-renewable subscriptions.

Instance Property

# autoRenewPreference

The product ID of the auto-renewable subscription that will automatically
renew.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let autoRenewPreference: String?

## Discussion

This value is the product ID of the auto-renewable subscription that will
renew after the current period expires. The value may be:

  * The same as `currentProductID` if the subscription will renew with the same product.

  * Another product ID value if the subscription will renew to a different product.

  * `nil` if the subscription won’t renew in the next period. This may occur for several reasons, including when the person disables auto-renew for the subscription, the subscription lapses due to a billing issue, or you increase the subscription price and the person doesn't accept the increase.

## See Also

### Getting the renewal or expiration state

`let state: Product.SubscriptionInfo.RenewalState`

The renewal state of the auto-renewable subscription.

`let willAutoRenew: Bool`

A Boolean value that indicates whether the subscription will automatically
renew in the next period.

`let expirationReason: Product.SubscriptionInfo.RenewalInfo.ExpirationReason?`

The reason the auto-renewable subscription expired.

`struct Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The reasons for auto-renewable subscription expirations.

`@backDeployed(before: iOS 17.0, macOS 14.0, tvOS 17.0, watchOS 10.0,
macCatalyst 17.0) var renewalDate: Date?`

The UNIX time, in milliseconds, that the most recent auto-renewable
subscription purchase expires.

Instance Property

# willAutoRenew

A Boolean value that indicates whether the subscription will automatically
renew in the next period.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let willAutoRenew: Bool

## See Also

### Getting the renewal or expiration state

`let state: Product.SubscriptionInfo.RenewalState`

The renewal state of the auto-renewable subscription.

`let autoRenewPreference: String?`

The product ID of the auto-renewable subscription that will automatically
renew.

`let expirationReason: Product.SubscriptionInfo.RenewalInfo.ExpirationReason?`

The reason the auto-renewable subscription expired.

`struct Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The reasons for auto-renewable subscription expirations.

`@backDeployed(before: iOS 17.0, macOS 14.0, tvOS 17.0, watchOS 10.0,
macCatalyst 17.0) var renewalDate: Date?`

The UNIX time, in milliseconds, that the most recent auto-renewable
subscription purchase expires.

Instance Property

# expirationReason

The reason the auto-renewable subscription expired.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let expirationReason: Product.SubscriptionInfo.RenewalInfo.ExpirationReason?

## Discussion

This optional value is `nil` if the auto-renewable subscription is active and
hasn’t expired.

## See Also

### Getting the renewal or expiration state

`let state: Product.SubscriptionInfo.RenewalState`

The renewal state of the auto-renewable subscription.

`let autoRenewPreference: String?`

The product ID of the auto-renewable subscription that will automatically
renew.

`let willAutoRenew: Bool`

A Boolean value that indicates whether the subscription will automatically
renew in the next period.

`struct Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The reasons for auto-renewable subscription expirations.

`@backDeployed(before: iOS 17.0, macOS 14.0, tvOS 17.0, watchOS 10.0,
macCatalyst 17.0) var renewalDate: Date?`

The UNIX time, in milliseconds, that the most recent auto-renewable
subscription purchase expires.

Instance Property

# renewalDate

The UNIX time, in milliseconds, that the most recent auto-renewable
subscription purchase expires.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 17.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    @backDeployed(before: iOS 17.0, macOS 14.0, tvOS 17.0, watchOS 10.0, macCatalyst 17.0)
    var renewalDate: Date? { get }

## Discussion

The `renewalDate` is a value that’s always present for auto-renewable
subscriptions, even for expired subscriptions. This date indicates the
expiration date of the most recent auto-renewable subscription purchase,
including renewals, and may be in the past. For subscriptions that renew
successfully, the `renewalDate` is the date when the subscription renews.

## See Also

### Getting the renewal or expiration state

`let state: Product.SubscriptionInfo.RenewalState`

The renewal state of the auto-renewable subscription.

`let autoRenewPreference: String?`

The product ID of the auto-renewable subscription that will automatically
renew.

`let willAutoRenew: Bool`

A Boolean value that indicates whether the subscription will automatically
renew in the next period.

`let expirationReason: Product.SubscriptionInfo.RenewalInfo.ExpirationReason?`

The reason the auto-renewable subscription expired.

`struct Product.SubscriptionInfo.RenewalInfo.ExpirationReason`

The reasons for auto-renewable subscription expirations.

Instance Property

# isInBillingRetry

A Boolean value that indicates whether an auto-renewable subscription is in
the billing retry period.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let isInBillingRetry: Bool

## Discussion

This field indicates whether Apple is attempting to automatically renew an
expired subscription. If a subscription expires due to a billing issue, a
value of `true` indicates that Apple is still trying to renew the
subscription. If the subscription is in a billing grace period, the optional
`gracePeriodExpirationDate` contains a date.

Use the `isInBillingRetry` value along with `expirationReason` for more
insight, as the following table shows:

Values| Description  
---|---  
`isInBillingRetry` is `false,` `expirationReason` is `nil`| The auto-renewable
subscription is active and not in a billing retry period. The subscription is
entitled to service.  
`isInBillingRetry` is `true,``expirationReason` is
`billingError`,`gracePeriodExpirationDate` has a date| The auto-renewable
subscription is in a billing grace period. The subscription is entitled to
service until the date in `gracePeriodExpirationDate`.  
`isInBillingRetry` is `true,``expirationReason` is
`billingError`,`gracePeriodExpirationDate` is `nil`| The auto-renewable
subscription is in a billing retry period. The subscription is not entitled to
service.  
`isInBillingRetry` is `false,` `expirationReason` is `billingError`| The auto-
renewable subscription expired and billing retry wasn’t able to recover the
subscription.The subscription is not entitled to service.  
  
## See Also

### Getting billing status

`let gracePeriodExpirationDate: Date?`

The date the billing grace period expires for the auto-renewable subscription.

Instance Property

# gracePeriodExpirationDate

The date the billing grace period expires for the auto-renewable subscription.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let gracePeriodExpirationDate: Date?

## Discussion

This value is `nil` if the subscription is not in a billing grace period.

This date is present if you enable Billing Grace Period for your app and the
subscription is in the billing grace period. Ensure that your app provides
full service for the subscription throughout the grace period, which ends on
the `gracePeriodExpirationDate`.

A billing grace period occurs at the start of a billing retry state.
Throughout the billing grace period, the value of `isInBillingRetry` is
`true`, which indicates that Apple is attempting to automatically renew the
subscription.

For information about supporting Billing Grace Period, see Enable Billing
Grace Period for auto-renewable subscriptions and Reducing Involuntary
Subscriber Churn.

## See Also

### Getting billing status

`let isInBillingRetry: Bool`

A Boolean value that indicates whether an auto-renewable subscription is in
the billing retry period.

Article

# Managing Price Increases for Auto-Renewable Subscriptions

Identify the price increase status for auto-renewable subscriptions, in your
app and on your server.

## Overview

If you increase the price of an auto-renewable subscription in App Store
Connect, the `priceIncreaseStatus` in the `renewalInfo` object indicates if
the subscription is subject to the price increase. Auto-renewable
subscriptions have two types of price increases: those that require customer
consent, and those that don’t require customer consent.

For price increases that require customer consent, look for the following
status values in your app:

`Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus.noIncreasePending`|
Indicates there’s no price increase for this auto-renewable subscription.  
---|---  
`Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus.pending`| Indicates
there’s a pending price increase for the auto-renewable subscription that
requires customer consent, and the customer hasn’t yet consented. If the
customer doesn’t consent, the auto-renewable subscription expires at the end
of the billing cycle. When it expires, your app gets a status update in
`updates` with an `expirationReason` of `didNotConsentToPriceIncrease`.  
`Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus.agreed`| Indicates
that the customer consented to a price increase for the auto-renewable
subscription.  
  
For price increases that don’t require customer consent, look for the
following status values in your app:

`Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus.noIncreasePending`|
Doesn’t apply.  
---|---  
`Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus.pending`| Doesn’t
apply.  
`Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus.agreed`| Indicates
that the App Store informed the customer of the price increase for the auto-
renewable subscription, and the subscription is subject to the price
increase.If the customer cancels the auto-renewable subscription, your app
gets a status update in `updates` with an `expirationReason` of
`autoRenewDisabled`.  
  
For more information about managing subscription prices in App Store Connect,
see Managing Prices.

### Receive Notifications for Price Increase Status Events

If you’ve enabled App Store Server Notifications V2, your server receives
notifications for events related to auto-renewable subscription price
increases.

For auto-renewable subscription price increases that require customer consent,
look for the following notifications:

Notification type| Subtype| Description  
---|---|---  
`PRICE_INCREASE` | `PENDING`| Indicates that the App Store informed the customer of the price increase for the auto-renewable subscription, and the customer hasn’t yet responded.  
`PRICE_INCREASE`| `ACCEPTED`| Indicates that the customer consented to the
price increase for the auto-renewable subscription.  
`EXPIRED`| `PRICE_INCREASE`| Indicates that the auto-renewable subscription
expired because the customer didn’t consent to the price increase, and allowed
the subscription to expire.  
`EXPIRED`| `VOLUNTARY`| Indicates that the customer voluntarily canceled the
auto-renewable subscription. (Note: This notification type and subtype isn’t
specific to price increases.)  
  
For auto-renewable subscription price increases that don’t require customer
consent, look for the following notifications:

Notification type| Subtype| Description  
---|---|---  
`PRICE_INCREASE`| `ACCEPTED`| Indicates that the App Store informed the
customer of the auto-renewable subscription price increase, and the
subscription is subject to the price increase.  
`EXPIRED` | `VOLUNTARY`| Indicates that the customer voluntarily canceled the auto-renewable subscription. (Note: This notification type and subtype isn't specific to price increases.)  
  
For more information about App Store Server Notifications, see Enabling App
Store Server Notifications. For more information about notification types and
subtypes, see `notificationType` and `subtype`.

## See Also

### Getting the price increase status

`let priceIncreaseStatus:
Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus`

The status that indicates whether the auto-renewable subscription is subject
to a price increase.

`enum Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus`

Status values that indicate whether an auto-renewable subscription is subject
to a price increase.

Instance Property

# priceIncreaseStatus

The status that indicates whether the auto-renewable subscription is subject
to a price increase.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let priceIncreaseStatus: Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus

## Discussion

For more information about price increase status, see Managing Price Increases
for Auto-Renewable Subscriptions.

## See Also

### Getting the price increase status

Managing Price Increases for Auto-Renewable Subscriptions

Identify the price increase status for auto-renewable subscriptions, in your
app and on your server.

`enum Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus`

Status values that indicate whether an auto-renewable subscription is subject
to a price increase.

Instance Property

# deviceVerification

The device verification value to use to verify whether the renewal information
belongs to the device.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let deviceVerification: Data

## Discussion

For more information, see `deviceVerificationID`.

## See Also

### Verifying subscription renewal information

`let deviceVerificationNonce: UUID`

The UUID to use to compute the device verification value.

`let signedDate: Date`

The date that the App Store signed the JWS renewal information.

Instance Property

# deviceVerificationNonce

The UUID to use to compute the device verification value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let deviceVerificationNonce: UUID

## Discussion

For more information, see `deviceVerificationID`.

## See Also

### Verifying subscription renewal information

`let deviceVerification: Data`

The device verification value to use to verify whether the renewal information
belongs to the device.

`let signedDate: Date`

The date that the App Store signed the JWS renewal information.

Instance Property

# signedDate

The date that the App Store signed the JWS renewal information.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let signedDate: Date

## Discussion

Use the `signedDate` to verify whether the certificate used to sign the
transaction was valid when the App Store signed the transaction.

## See Also

### Verifying subscription renewal information

`let deviceVerification: Data`

The device verification value to use to verify whether the renewal information
belongs to the device.

`let deviceVerificationNonce: UUID`

The UUID to use to compute the device verification value.

Instance Property

# jsonRepresentation

The raw JSON representation of the subscription renewal information.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var jsonRepresentation: Data { get }

## Discussion

The information in `jsonRepresentation` is the same information that’s in the
properties of the same instance of `Product.SubscriptionInfo.RenewalInfo`.

Instance Property

# debugDescription

A string representation of the renewal info, suitable for debugging.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var debugDescription: String { get }

## Relationships

### From Protocol

  * `CustomDebugStringConvertible`

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func != (lhs: Product.SubscriptionInfo.RenewalInfo, rhs: Product.SubscriptionInfo.RenewalInfo) -> Bool

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

### Comparing and hashing renewal information

`static func == (Product.SubscriptionInfo.RenewalInfo,
Product.SubscriptionInfo.RenewalInfo) -> Bool`

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

    
    
    static func == (lhs: Product.SubscriptionInfo.RenewalInfo, rhs: Product.SubscriptionInfo.RenewalInfo) -> Bool

## See Also

### Comparing and hashing renewal information

`static func != (Product.SubscriptionInfo.RenewalInfo,
Product.SubscriptionInfo.RenewalInfo) -> Bool`

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

### Comparing and hashing renewal information

`static func != (Product.SubscriptionInfo.RenewalInfo,
Product.SubscriptionInfo.RenewalInfo) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (Product.SubscriptionInfo.RenewalInfo,
Product.SubscriptionInfo.RenewalInfo) -> Bool`

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

### Comparing and hashing renewal information

`static func != (Product.SubscriptionInfo.RenewalInfo,
Product.SubscriptionInfo.RenewalInfo) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (Product.SubscriptionInfo.RenewalInfo,
Product.SubscriptionInfo.RenewalInfo) -> Bool`

Returns a Boolean value that indicates whether two values are equal.

`func hash(into: inout Hasher)`

Hashes the essential components of the value by feeding them into the given
hasher.

