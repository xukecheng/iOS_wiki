Instance Property

# environment

The server environment that generates and signs the transaction.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    let environment: AppStore.Environment

## See Also

### Getting the environment and storefront

`let storefront: Storefront`

The App Store storefront associated with the transaction.

Instance Property

# storefront

The App Store storefront associated with the transaction.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    let storefront: Storefront

## See Also

### Getting the environment and storefront

`let environment: AppStore.Environment`

The server environment that generates and signs the transaction.

Instance Property

# originalID

The original transaction identifier of a purchase.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let originalID: UInt64

## Discussion

The original transaction identifier, `originalID`, is identical to `id` except
when the user restores a purchase or renews a transaction. You can use this
value to:

  * Identify one or more renewals for the same subscription.

  * Differentiate a purchase transaction from a restore or a renewal transaction. For restore and renewal transactions, the original transaction identifier, `originalID`, and transaction identifier, `id`, differ.

  * Match a transaction in the app with a transaction you receive on your server in an App Store Server Notifications event.

## See Also

### Getting the original transaction identifier

`let originalPurchaseDate: Date`

The date of purchase for the original transaction.

Instance Property

# originalPurchaseDate

The date of purchase for the original transaction.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let originalPurchaseDate: Date

## See Also

### Getting the original transaction identifier

`let originalID: UInt64`

The original transaction identifier of a purchase.

Instance Property

# id

The unique identifier for the transaction.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let id: UInt64

## Discussion

Every transaction such as an in-app purchase, restore, or subscription renewal
has a unique transaction identifier.

## Relationships

### From Protocol

  * `Identifiable`

## See Also

### Identifying a transaction

`typealias Transaction.ID`

A type representing the transaction identifier.

`let webOrderLineItemID: String?`

A unique ID that identifies subscription purchase events across devices,
including subscription renewals.

`var id: ObjectIdentifier`

The stable identity of the entity associated with this instance.

Available when `Transaction` conforms to `AnyObject`.

Type Alias

# Transaction.ID

A type representing the transaction identifier.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    typealias Transaction.ID = UInt64

## See Also

### Identifying a transaction

`let id: UInt64`

The unique identifier for the transaction.

`let webOrderLineItemID: String?`

A unique ID that identifies subscription purchase events across devices,
including subscription renewals.

`var id: ObjectIdentifier`

The stable identity of the entity associated with this instance.

Available when `Transaction` conforms to `AnyObject`.

Instance Property

# webOrderLineItemID

A unique ID that identifies subscription purchase events across devices,
including subscription renewals.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let webOrderLineItemID: String?

## See Also

### Identifying a transaction

`let id: UInt64`

The unique identifier for the transaction.

`typealias Transaction.ID`

A type representing the transaction identifier.

`var id: ObjectIdentifier`

The stable identity of the entity associated with this instance.

Available when `Transaction` conforms to `AnyObject`.

Instance Property

# id

The stable identity of the entity associated with this instance.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 15.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+  Xcode 11.0+

    
    
    var id: ObjectIdentifier { get }

Available when `Transaction` conforms to `AnyObject`.

## Discussion

Note

This documentation comment was inherited from `Identifiable`.

## See Also

### Identifying a transaction

`let id: UInt64`

The unique identifier for the transaction.

`typealias Transaction.ID`

A type representing the transaction identifier.

`let webOrderLineItemID: String?`

A unique ID that identifies subscription purchase events across devices,
including subscription renewals.

Instance Property

# appBundleID

The bundle identifier for the app.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let appBundleID: String

## See Also

### Identifying the app and product

`let productID: String`

The product identifier of the in-app purchase.

`let productType: Product.ProductType`

The type of the in-app purchase.

`let subscriptionGroupID: String?`

The identifier of the subscription group that the subscription belongs to.

Instance Property

# productID

The product identifier of the in-app purchase.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let productID: String

## Discussion

You create product identifiers for in-app purchases in App Store Connect.

## See Also

### Identifying the app and product

`let appBundleID: String`

The bundle identifier for the app.

`let productType: Product.ProductType`

The type of the in-app purchase.

`let subscriptionGroupID: String?`

The identifier of the subscription group that the subscription belongs to.

Instance Property

# productType

The type of the in-app purchase.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let productType: Product.ProductType

## See Also

### Identifying the app and product

`let appBundleID: String`

The bundle identifier for the app.

`let productID: String`

The product identifier of the in-app purchase.

`let subscriptionGroupID: String?`

The identifier of the subscription group that the subscription belongs to.

Instance Property

# subscriptionGroupID

The identifier of the subscription group that the subscription belongs to.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let subscriptionGroupID: String?

## See Also

### Identifying the app and product

`let appBundleID: String`

The bundle identifier for the app.

`let productID: String`

The product identifier of the in-app purchase.

`let productType: Product.ProductType`

The type of the in-app purchase.

Instance Property

# purchaseDate

The date that the App Store charged the user’s account for a purchased or
restored product, or for a subscription purchase or renewal after a lapse.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let purchaseDate: Date

## See Also

### Getting purchase and expiration dates

`let expirationDate: Date?`

The date the subscription expires or renews.

Instance Property

# expirationDate

The date the subscription expires or renews.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let expirationDate: Date?

## See Also

### Getting purchase and expiration dates

`let purchaseDate: Date`

The date that the App Store charged the user’s account for a purchased or
restored product, or for a subscription purchase or renewal after a lapse.

Instance Property

# isUpgraded

A Boolean that indicates whether the user upgraded to another subscription.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let isUpgraded: Bool

## Discussion

If `isUpgraded` is `true`, the user has upgraded the subscription represented
by this transaction to another subscription. This value appears in the
transaction only when the value is `true`. To determine the service that the
customer is entitled to, look for another transaction that has a subscription
with a higher level of service.

## See Also

### Getting purchase details

`let ownershipType: Transaction.OwnershipType`

A value that indicates whether the transaction was purchased by the user, or
is made available to them through Family Sharing.

`typealias Transaction.OwnershipType.RawValue`

The type that represents the raw value of a transaction’s ownership type.

`struct Transaction.OwnershipType`

The types the system uses to describe whether the user purchased the product
or it’s available to them through Family Sharing.

`let purchasedQuantity: Int`

The number of consumable products purchased.

Instance Property

# ownershipType

A value that indicates whether the transaction was purchased by the user, or
is made available to them through Family Sharing.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let ownershipType: Transaction.OwnershipType

## See Also

### Getting purchase details

`let isUpgraded: Bool`

A Boolean that indicates whether the user upgraded to another subscription.

`typealias Transaction.OwnershipType.RawValue`

The type that represents the raw value of a transaction’s ownership type.

`struct Transaction.OwnershipType`

The types the system uses to describe whether the user purchased the product
or it’s available to them through Family Sharing.

`let purchasedQuantity: Int`

The number of consumable products purchased.

Type Alias

# Transaction.OwnershipType.RawValue

The type that represents the raw value of a transaction’s ownership type.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    typealias Transaction.OwnershipType.RawValue = String

## See Also

### Accessing the raw value

`let rawValue: String`

The raw string value that represents a transaction ownership type.

Instance Property

# purchasedQuantity

The number of consumable products purchased.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let purchasedQuantity: Int

## See Also

### Getting purchase details

`let isUpgraded: Bool`

A Boolean that indicates whether the user upgraded to another subscription.

`let ownershipType: Transaction.OwnershipType`

A value that indicates whether the transaction was purchased by the user, or
is made available to them through Family Sharing.

`typealias Transaction.OwnershipType.RawValue`

The type that represents the raw value of a transaction’s ownership type.

`struct Transaction.OwnershipType`

The types the system uses to describe whether the user purchased the product
or it’s available to them through Family Sharing.

Instance Property

# subscriptionStatus

An array that contains status information for a subscription group, including
renewal and transaction information.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 17.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    @backDeployed(before: iOS 17.0, macOS 14.0, tvOS 17.0, watchOS 10.0)
    var subscriptionStatus: Product.SubscriptionInfo.Status? { get async }

## Discussion

This value is `nil` if the product in the transaction isn’t an auto-renewable
subscription, specifically, if the `productType` is anything other than
`autoRenewable`.

The array can have more than one subscription status, for example, if your
subscription supports Family Sharing. Provide the customer with service for
the subscription based on the highest level of service where the subscription
status is `subscribed`.

Instance Property

# reason

The cause of the purchase transaction, whether it’s a customer’s purchase or
an auto-renewable subscription renewal that the system initiates.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    let reason: Transaction.Reason

## See Also

### Getting transaction reason

`struct Transaction.Reason`

A cause of a purchase transaction, indicating whether it’s a customer’s
purchase or an auto-renewable subscription renewal that the system initiates.

Instance Property

# offer

The subscription offer that applies to the transaction, including its offer
type, payment mode, and ID.

iOS 17.2+  iPadOS 17.2+  macOS 14.2+  Mac Catalyst 17.2+  tvOS 17.2+  watchOS
10.2+  visionOS 1.1+  Xcode 15.1+

    
    
    let offer: Transaction.Offer?

## Discussion

This value is `nil` if the transaction doesn’t include an offer.

Subscription offers include introductory offers, promotional offers, and offer
codes. You set up subscription offers in App Store Connect. If a customer
redeems an offer, this property contains the offer details, including its
`type`, `paymentMode`, and `id`. For more information about the details, see
`Transaction.Offer`.

## See Also

### Identifying subscription offers

`struct Transaction.Offer`

The subscription offers that apply to a transaction.

Instance Property

# revocationDate

The date that the App Store refunded the transaction or revoked it from Family
Sharing.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let revocationDate: Date?

## See Also

### Getting revocation status

`let revocationReason: Transaction.RevocationReason?`

The reason that the App Store refunded the transaction or revoked it from
Family Sharing.

`struct Transaction.RevocationReason`

Reasons that describe why the App Store may refund a transaction or revoke it
from Family Sharing.

`typealias Transaction.RevocationReason.RawValue`

The type that represents the raw value of a transaction revocation reason.

Instance Property

# revocationReason

The reason that the App Store refunded the transaction or revoked it from
Family Sharing.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let revocationReason: Transaction.RevocationReason?

## See Also

### Getting revocation status

`let revocationDate: Date?`

The date that the App Store refunded the transaction or revoked it from Family
Sharing.

`struct Transaction.RevocationReason`

Reasons that describe why the App Store may refund a transaction or revoke it
from Family Sharing.

`typealias Transaction.RevocationReason.RawValue`

The type that represents the raw value of a transaction revocation reason.

Type Alias

# Transaction.RevocationReason.RawValue

The type that represents the raw value of a transaction revocation reason.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    typealias Transaction.RevocationReason.RawValue = Int

## See Also

### Revocation reasons

`static let developerIssue: Transaction.RevocationReason`

The value that indicates a customer canceled the transaction due to an actual
or perceived issue within your app.

`static let other: Transaction.RevocationReason`

The value that indicates a customer canceled the transaction for other
reasons.

Instance Property

# appAccountToken

A UUID that associates the transaction with a user on your own service.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let appAccountToken: UUID?

## Discussion

You create an `appAccountToken(_:)` and send it to the App Store when a
customer initiates an in-app purchase. The App Store returns the same value in
`appAccountToken` in the transaction information after the customer completes
the purchase.

Instance Property

# environmentStringRepresentation

A string representation of the server environment.

iOS 15.0–16.0  Deprecated  iPadOS 15.0–16.0  Deprecated  macOS 12.0–13.0
Deprecated  Mac Catalyst 16.0–16.0  Deprecated  tvOS 15.0–16.0  Deprecated
watchOS 8.0–9.0  Deprecated  Xcode 13.0–14.0  Deprecated

    
    
    @backDeployed(before: iOS 16.0, macOS 13.0, tvOS 16.0, watchOS 9.0, macCatalyst 16.0)
    var environmentStringRepresentation: String { get }

Deprecated

Use `environment` instead.

## See Also

### Deprecated

`var offerID: String?`

A string that identifies an offer applied to the current subscription.

Deprecated

`@backDeployed(before: iOS 17.2, macOS 14.2, tvOS 17.2, watchOS 10.2) var
offerPaymentModeStringRepresentation: String?`

The string representation of the payment mode for a subscription offer.

Deprecated

`var offerType: Transaction.OfferType?`

The subscription offer type for the current subscription period.

Deprecated

`@backDeployed(before: iOS 17.0, macOS 14.0, tvOS 17.0, watchOS 10.0,
macCatalyst 17.0) var reasonStringRepresentation: String`

The string representation of the transaction reason.

Deprecated

`@backDeployed(before: iOS 17.0, macOS 14.0, tvOS 17.0, watchOS 10.0,
macCatalyst 17.0) var storefrontCountryCode: String`

The three-letter code that represents the country or region associated with
the App Store storefront of the purchase.

Deprecated

Instance Property

# offerID

A string that identifies an offer applied to the current subscription.

iOS 15.0–17.2  Deprecated  iPadOS 15.0–17.2  Deprecated  macOS 12.0–14.2
Deprecated  Mac Catalyst 15.0–17.2  Deprecated  tvOS 15.0–17.2  Deprecated
watchOS 8.0–10.2  Deprecated  visionOS 1.0–1.1  Deprecated  Xcode 13.0–15.1
Deprecated

    
    
    var offerID: String? { get }

Deprecated

Use `offer` instead.

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

### Deprecated

`@backDeployed(before: iOS 16.0, macOS 13.0, tvOS 16.0, watchOS 9.0,
macCatalyst 16.0) var environmentStringRepresentation: String`

A string representation of the server environment.

Deprecated

`@backDeployed(before: iOS 17.2, macOS 14.2, tvOS 17.2, watchOS 10.2) var
offerPaymentModeStringRepresentation: String?`

The string representation of the payment mode for a subscription offer.

Deprecated

`var offerType: Transaction.OfferType?`

The subscription offer type for the current subscription period.

Deprecated

`@backDeployed(before: iOS 17.0, macOS 14.0, tvOS 17.0, watchOS 10.0,
macCatalyst 17.0) var reasonStringRepresentation: String`

The string representation of the transaction reason.

Deprecated

`@backDeployed(before: iOS 17.0, macOS 14.0, tvOS 17.0, watchOS 10.0,
macCatalyst 17.0) var storefrontCountryCode: String`

The three-letter code that represents the country or region associated with
the App Store storefront of the purchase.

Deprecated

Instance Property

# offerPaymentModeStringRepresentation

The string representation of the payment mode for a subscription offer.

iOS 15.0–17.2  Deprecated  iPadOS 15.0–17.2  Deprecated  macOS 12.0–14.2
Deprecated  Mac Catalyst 17.2–17.2  Deprecated  tvOS 15.0–17.2  Deprecated
watchOS 8.0–10.2  Deprecated  visionOS 1.1–1.1  Deprecated  Xcode 13.0–15.1
Deprecated

    
    
    @backDeployed(before: iOS 17.2, macOS 14.2, tvOS 17.2, watchOS 10.2)
    var offerPaymentModeStringRepresentation: String? { get }

Deprecated

Use `paymentMode` instead.

## See Also

### Deprecated

`@backDeployed(before: iOS 16.0, macOS 13.0, tvOS 16.0, watchOS 9.0,
macCatalyst 16.0) var environmentStringRepresentation: String`

A string representation of the server environment.

Deprecated

`var offerID: String?`

A string that identifies an offer applied to the current subscription.

Deprecated

`var offerType: Transaction.OfferType?`

The subscription offer type for the current subscription period.

Deprecated

`@backDeployed(before: iOS 17.0, macOS 14.0, tvOS 17.0, watchOS 10.0,
macCatalyst 17.0) var reasonStringRepresentation: String`

The string representation of the transaction reason.

Deprecated

`@backDeployed(before: iOS 17.0, macOS 14.0, tvOS 17.0, watchOS 10.0,
macCatalyst 17.0) var storefrontCountryCode: String`

The three-letter code that represents the country or region associated with
the App Store storefront of the purchase.

Deprecated

Instance Property

# offerType

The subscription offer type for the current subscription period.

iOS 15.0–17.2  Deprecated  iPadOS 15.0–17.2  Deprecated  macOS 12.0–14.2
Deprecated  Mac Catalyst 15.0–17.2  Deprecated  tvOS 15.0–17.2  Deprecated
watchOS 8.0–10.2  Deprecated  visionOS 1.0–1.1  Deprecated  Xcode 13.0–15.1
Deprecated

    
    
    var offerType: Transaction.OfferType? { get }

Deprecated

Use `offer` instead.

## Discussion

If this value is `nil`, there’s no offer applied.

## See Also

### Deprecated

`@backDeployed(before: iOS 16.0, macOS 13.0, tvOS 16.0, watchOS 9.0,
macCatalyst 16.0) var environmentStringRepresentation: String`

A string representation of the server environment.

Deprecated

`var offerID: String?`

A string that identifies an offer applied to the current subscription.

Deprecated

`@backDeployed(before: iOS 17.2, macOS 14.2, tvOS 17.2, watchOS 10.2) var
offerPaymentModeStringRepresentation: String?`

The string representation of the payment mode for a subscription offer.

Deprecated

`@backDeployed(before: iOS 17.0, macOS 14.0, tvOS 17.0, watchOS 10.0,
macCatalyst 17.0) var reasonStringRepresentation: String`

The string representation of the transaction reason.

Deprecated

`@backDeployed(before: iOS 17.0, macOS 14.0, tvOS 17.0, watchOS 10.0,
macCatalyst 17.0) var storefrontCountryCode: String`

The three-letter code that represents the country or region associated with
the App Store storefront of the purchase.

Deprecated

Instance Property

# reasonStringRepresentation

The string representation of the transaction reason.

iOS 15.0–16.0  Deprecated  iPadOS 15.0–16.0  Deprecated  macOS 12.0–13.0
Deprecated  Mac Catalyst 17.0–17.0  Deprecated  tvOS 15.0–16.0  Deprecated
watchOS 8.0–9.0  Deprecated  Xcode 13.0–14.0  Deprecated

    
    
    @backDeployed(before: iOS 17.0, macOS 14.0, tvOS 17.0, watchOS 10.0, macCatalyst 17.0)
    var reasonStringRepresentation: String { get }

Deprecated

Use `reason` instead.

## Discussion

For more information, see `reason`.

## See Also

### Deprecated

`@backDeployed(before: iOS 16.0, macOS 13.0, tvOS 16.0, watchOS 9.0,
macCatalyst 16.0) var environmentStringRepresentation: String`

A string representation of the server environment.

Deprecated

`var offerID: String?`

A string that identifies an offer applied to the current subscription.

Deprecated

`@backDeployed(before: iOS 17.2, macOS 14.2, tvOS 17.2, watchOS 10.2) var
offerPaymentModeStringRepresentation: String?`

The string representation of the payment mode for a subscription offer.

Deprecated

`var offerType: Transaction.OfferType?`

The subscription offer type for the current subscription period.

Deprecated

`@backDeployed(before: iOS 17.0, macOS 14.0, tvOS 17.0, watchOS 10.0,
macCatalyst 17.0) var storefrontCountryCode: String`

The three-letter code that represents the country or region associated with
the App Store storefront of the purchase.

Deprecated

Instance Property

# storefrontCountryCode

The three-letter code that represents the country or region associated with
the App Store storefront of the purchase.

iOS 15.0–17.0  Deprecated  iPadOS 15.0–17.0  Deprecated  macOS 12.0–14.0
Deprecated  Mac Catalyst 17.0–17.0  Deprecated  tvOS 15.0–17.0  Deprecated
watchOS 8.0–10.0  Deprecated  Xcode 13.0–15.0  Deprecated

    
    
    @backDeployed(before: iOS 17.0, macOS 14.0, tvOS 17.0, watchOS 10.0, macCatalyst 17.0)
    var storefrontCountryCode: String { get }

Deprecated

Use `storefront` instead.

## Discussion

This property uses the ISO 3166-1 alpha-3 country code representation.

## See Also

### Deprecated

`@backDeployed(before: iOS 16.0, macOS 13.0, tvOS 16.0, watchOS 9.0,
macCatalyst 16.0) var environmentStringRepresentation: String`

A string representation of the server environment.

Deprecated

`var offerID: String?`

A string that identifies an offer applied to the current subscription.

Deprecated

`@backDeployed(before: iOS 17.2, macOS 14.2, tvOS 17.2, watchOS 10.2) var
offerPaymentModeStringRepresentation: String?`

The string representation of the payment mode for a subscription offer.

Deprecated

`var offerType: Transaction.OfferType?`

The subscription offer type for the current subscription period.

Deprecated

`@backDeployed(before: iOS 17.0, macOS 14.0, tvOS 17.0, watchOS 10.0,
macCatalyst 17.0) var reasonStringRepresentation: String`

The string representation of the transaction reason.

Deprecated

