Type

# originalTransactionId

The original transaction identifier of a purchase.

App Store Server Notifications 2.0+

    
    
    string originalTransactionId

## Discussion

This value is identical to the transaction identifier (`transactionId`) except
when the user restores or renews a subscription.

## See Also

### Transaction identifiers

`type transactionId`

The unique identifier for a transaction such as an in-app purchase, restored
purchase, or subscription renewal.

`type webOrderLineItemId`

The unique identifier of subscription purchase events across devices,
including subscription renewals.

Type

# transactionId

The unique identifier for a transaction such as an in-app purchase, restored
purchase, or subscription renewal.

App Store Server Notifications 2.0+

    
    
    string transactionId

## Discussion

The App Store generates a new value for transaction identifier every time the
subscription automatically renews or the user restores it on a new device.

When a user first purchases a subscription, the transaction identifier always
matches the original transaction identifier (`originalTransactionId`). For a
restore or renewal, the transaction identifier doesn’t match the original
transaction identifier. If a user restores or renews the same subscription
multiple times, each restore or renewal has a unique transaction identifier.

## See Also

### Transaction identifiers

`type originalTransactionId`

The original transaction identifier of a purchase.

`type webOrderLineItemId`

The unique identifier of subscription purchase events across devices,
including subscription renewals.

Type

# webOrderLineItemId

The unique identifier of subscription purchase events across devices,
including subscription renewals.

App Store Server Notifications 2.0+

    
    
    string webOrderLineItemId

## Discussion

This value applies only to auto-renewable subscriptions.

## See Also

### Transaction identifiers

`type originalTransactionId`

The original transaction identifier of a purchase.

`type transactionId`

The unique identifier for a transaction such as an in-app purchase, restored
purchase, or subscription renewal.

Type

# bundleId

The bundle identifier of an app.

App Store Server Notifications 2.0+

    
    
    string bundleId

## See Also

### App metadata and environment

`type appAppleId`

The unique identifier of an app in the App Store.

`type bundleVersion`

The version of the build that identifies an iteration of the bundle.

`type environment`

The server environment, either sandbox or production.

`type status`

The status of an auto-renewable subscription at the time the App Store signs
the notification.

Type

# appAccountToken

A UUID that associates the transaction with a user on your service.

App Store Server Notifications 2.0+

    
    
    uuid appAccountToken

## Discussion

When a customer initiates an in-app purchase, your app may create an
`appAccountToken(_:)` and send it to the App Store. The App Store returns the
same value in `appAccountToken` in the transaction information after the
customer completes the purchase.

If you’re using the Original API for in-app purchase and provide a UUID in the
`applicationUsername` property, then the `appAccountToken` field contains that
value.

Type

# productId

The product identifier of the in-app purchase.

App Store Server Notifications 2.0+

    
    
    string productId

## Discussion

You create product identifiers for in-app purchases in App Store Connect.

## See Also

### Product information

`type type`

The product type of the in-app purchase.

`type subscriptionGroupIdentifier`

The identifier of the subscription group that the subscription belongs to.

`type quantity`

The number of consumable products purchased.

Type

# type

The product type of the in-app purchase.

App Store Server Notifications 2.0+

    
    
    string type

##  Possible Values

`Auto-Renewable Subscription`

    

An auto-renewable subscription.

`Non-Consumable`

    

A non-consumable in-app purchase.

`Consumable`

    

A consumable in-app purchase.

`Non-Renewing Subscription`

    

A non-renewing subscription.

## See Also

### Product information

`type productId`

The product identifier of the in-app purchase.

`type subscriptionGroupIdentifier`

The identifier of the subscription group that the subscription belongs to.

`type quantity`

The number of consumable products purchased.

Type

# subscriptionGroupIdentifier

The identifier of the subscription group that the subscription belongs to.

App Store Server Notifications 2.0+

    
    
    string subscriptionGroupIdentifier

## Discussion

Auto-renewable subscriptions always belong to a subscription group. You create
the subscription group identifiers in App Store Connect before you create and
add an auto-renewable subscription. For more information about subscription
groups, see Offer auto-renewable subscriptions.

## See Also

### Product information

`type productId`

The product identifier of the in-app purchase.

`type type`

The product type of the in-app purchase.

`type quantity`

The number of consumable products purchased.

Type

# quantity

The number of consumable products purchased.

App Store Server Notifications 2.0+

    
    
    int32 quantity

## See Also

### Product information

`type productId`

The product identifier of the in-app purchase.

`type type`

The product type of the in-app purchase.

`type subscriptionGroupIdentifier`

The identifier of the subscription group that the subscription belongs to.

Type

# price

The price, in milliunits, of the in-app purchase or subscription offer that
you configured in App Store Connect.

App Store Server Notifications 2.9+

    
    
    int64 price

## Discussion

This value represents the price, in milliunits of the `currency`, of the in-
app purchase or subscription offer that you configured in App Store Connect.
One unit of the currency equals 1,000 milliunits.

The following table shows some examples of the values you may see in the
`price` and `currency` parameters based on prices that you may configure in
App Store Connect:

Price configured in App Store Connect| `price` parameter| `currency` parameter  
---|---|---  
$1.99 (US dollar)| 1990| USD  
KRW 3,300 (South Korean won)| 3300000| KRW  
JPY 300 (Japanese Yen)| 300000| JPY  
  
To determine the storefront, use the `storefront` value in the transaction.
Don’t use the `currency` to infer the storefront.

Important

Don’t use the `price` or `currency` values for any revenue reconciliation or
recognition. App Store Connect reporting is your source of record for
financial and accounting purposes. For more information, see Overview of
reporting tools.

For more information on how you set prices, see Set a price and Set a price
for an in-app purchase.

## See Also

### Product price and currency

`type currency`

The three-letter ISO 4217 currency code for the price of the product.

Type

# currency

The three-letter ISO 4217 currency code for the price of the product.

App Store Server Notifications 2.9+

    
    
    string currency

## Discussion

The currency property contains an ISO 4217 alpha-3 string that represents the
currency of the price of the product.

Important

Don't use the `price` or `currency` values for any revenue reconciliation or
recognition. App Store Connect reporting is your source of record for
financial and accounting purposes. For more information, see Overview of
reporting tools.

Don’t use the `currency` to infer the storefront. Use the `storefront` value
in the transaction, instead.

For more information on how you set prices, see Set a price and Set a price
for an in-app purchase.

## See Also

### Product price and currency

`type price`

The price, in milliunits, of the in-app purchase or subscription offer that
you configured in App Store Connect.

Type

# storefront

The three-letter code that represents the country or region associated with
the App Store storefront for the purchase.

App Store Server Notifications 2.8+

    
    
    string storefront

## Discussion

This property uses the ISO 3166-1 alpha-3 country code representation. This
property is the same as the `countryCode` in StoreKit.

## See Also

### Storefront info

`type storefrontId`

An Apple-defined value that uniquely identifies an App Store storefront.

Type

# storefrontId

An Apple-defined value that uniquely identifies an App Store storefront.

App Store Server Notifications 2.8+

    
    
    string storefrontId

## Discussion

This value is the same as the `id` value in StoreKit.

## See Also

### Storefront info

`type storefront`

The three-letter code that represents the country or region associated with
the App Store storefront for the purchase.

Type

# offerIdentifier

The identifier that contains the offer code or the promotional offer
identifier.

App Store Server Notifications 2.0+

    
    
    string offerIdentifier

## Discussion

The `offerIdentifier` applies only when the `offerType` has a value of `2` or
`3`.

The `offerIdentifier` provides details about the subscription offer in effect
for the transaction. Its value is either the offer code or the promotional
offer.

For more information on offer codes, see Supporting subscription offer codes
in your app and Set up offer codes. For more information on promotional
offers, see Set up promotional offers for auto-renewable subscriptions.

## See Also

### Promotional offers

`type offerType`

The type of subscription offer.

`type offerDiscountType`

The payment mode you configure for an introductory offer, promotional offer,
or offer code on an auto-renewable subscription.

Type

# offerType

The type of subscription offer.

App Store Server Notifications 2.0+

    
    
    int32 offerType

##  Possible Values

`1`

    

An introductory offer.

`2`

    

A promotional offer.

`3`

    

An offer with a subscription offer code.

## Discussion

The offer types `2` and `3` have an `offerIdentifier`.

For more information about introductory offers, see Implementing introductory
offers in your app. For more information about promotional offers, see Set up
promotional offers for auto-renewable subscriptions. For more information
about promo codes, see Promo codes overview.

## See Also

### Promotional offers

`type offerIdentifier`

The identifier that contains the offer code or the promotional offer
identifier.

`type offerDiscountType`

The payment mode you configure for an introductory offer, promotional offer,
or offer code on an auto-renewable subscription.

Type

# offerDiscountType

The payment mode you configure for an introductory offer, promotional offer,
or offer code on an auto-renewable subscription.

App Store Server Notifications 2.9+

    
    
    string offerDiscountType

##  Possible Values

`FREE_TRIAL`

    

A payment mode of a product discount that indicates a free trial.

`PAY_AS_YOU_GO`

    

A payment mode of a product discount that is billed over a single or multiple
billing periods.

`PAY_UP_FRONT`

    

A payment mode of a product discount that is paid up front.

## Discussion

You set up subscription offers and determine the payment mode when you
configure subscriptions in App Store Connect. For more information about the
Free Trial, Pay As You Go, and Pay Up Front payment modes, see Pricing and
availability.

For more information about configuring subscription offers, see: Set up
introductory offers for auto-renewable subscriptions, Set up promotional
offers for auto-renewable subscriptions, and Set up offer codes.

## See Also

### Promotional offers

`type offerIdentifier`

The identifier that contains the offer code or the promotional offer
identifier.

`type offerType`

The type of subscription offer.

Type

# originalPurchaseDate

The purchase date of the transaction associated with the original transaction
identifier.

App Store Server Notifications 2.0+

    
    
    timestamp originalPurchaseDate

## Discussion

The original purchase date is in UNIX time, in milliseconds.

## See Also

### Purchase dates

`type purchaseDate`

The time that the App Store charged the user’s account for a purchase, a
restored product, a subscription, or a subscription renewal after a lapse.

`type recentSubscriptionStartDate`

The earliest start date of a subscription in a series of auto-renewable
subscription purchases that ignores all lapses of paid service shorter than 60
days.

Type

# purchaseDate

The time that the App Store charged the user’s account for a purchase, a
restored product, a subscription, or a subscription renewal after a lapse.

App Store Server Notifications 2.0+

    
    
    timestamp purchaseDate

## Discussion

The purchase date is in UNIX time, in milliseconds.

## See Also

### Purchase dates

`type originalPurchaseDate`

The purchase date of the transaction associated with the original transaction
identifier.

`type recentSubscriptionStartDate`

The earliest start date of a subscription in a series of auto-renewable
subscription purchases that ignores all lapses of paid service shorter than 60
days.

Type

# recentSubscriptionStartDate

The earliest start date of a subscription in a series of auto-renewable
subscription purchases that ignores all lapses of paid service shorter than 60
days.

App Store Server Notifications 2.5+

    
    
    timestamp recentSubscriptionStartDate

## Discussion

For more information about the recent subscription start date, see
`recentSubscriptionStartDate`.

Important

Don’t use the `recentSubscriptionStartDate` date to calculate days of paid
service. For more information about paid days of service, see Net revenue
after a year.

## See Also

### Purchase dates

`type originalPurchaseDate`

The purchase date of the transaction associated with the original transaction
identifier.

`type purchaseDate`

The time that the App Store charged the user’s account for a purchase, a
restored product, a subscription, or a subscription renewal after a lapse.

Type

# isInBillingRetryPeriod

A Boolean value that indicates whether the App Store is attempting to
automatically renew a subscription that expired due to a billing issue.

App Store Server Notifications 2.0+

    
    
    boolean isInBillingRetryPeriod

## See Also

### Billing status

`type gracePeriodExpiresDate`

The time when the billing grace period for a subscription renewal expires.

Type

# gracePeriodExpiresDate

The time when the billing grace period for a subscription renewal expires.

App Store Server Notifications 2.0+

    
    
    timestamp gracePeriodExpiresDate

## Discussion

For more information about billing grace periods, see Enable Billing Grace
Period for auto-renewable subscriptions.

## See Also

### Billing status

`type isInBillingRetryPeriod`

A Boolean value that indicates whether the App Store is attempting to
automatically renew a subscription that expired due to a billing issue.

Type

# autoRenewStatus

The renewal status for an auto-renewable subscription.

App Store Server Notifications 2.0+

    
    
    int32 autoRenewStatus

##  Possible Values

`0`

    

Automatic renewal is off. The customer has turned off automatic renewal for
the subscription, and it won’t renew at the end of the current subscription
period.

`1`

    

Automatic renewal is on. The subscription renews at the end of the current
subscription period.

## See Also

### Subscripton renewal and expiration

`type autoRenewProductId`

The product identifier of the product that will renew at the next billing
period.

`type expirationIntent`

The reason a subscription expired.

`type expiresDate`

The UNIX time, in milliseconds, an auto-renewable subscription purchase
expires or renews.

`type isUpgraded`

A Boolean value that indicates whether the user upgraded to another
subscription.

`type renewalDate`

The UNIX time, in milliseconds, when the most recent auto-renewable
subscription purchase expires.

Type

# autoRenewProductId

The product identifier of the product that will renew at the next billing
period.

App Store Server Notifications 2.0+

    
    
    string autoRenewProductId

## See Also

### Subscripton renewal and expiration

`type autoRenewStatus`

The renewal status for an auto-renewable subscription.

`type expirationIntent`

The reason a subscription expired.

`type expiresDate`

The UNIX time, in milliseconds, an auto-renewable subscription purchase
expires or renews.

`type isUpgraded`

A Boolean value that indicates whether the user upgraded to another
subscription.

`type renewalDate`

The UNIX time, in milliseconds, when the most recent auto-renewable
subscription purchase expires.

Type

# expirationIntent

The reason a subscription expired.

App Store Server Notifications 2.0+

    
    
    int32 expirationIntent

##  Possible Values

`1`

    

The customer canceled their subscription.

`2`

    

Billing error; for example, the customer’s payment information is no longer
valid.

`3`

    

The customer didn’t consent to an auto-renewable subscription price increase
that requires customer consent, allowing the subscription to expire.

`4`

    

The product wasn’t available for purchase at the time of renewal.

`5`

    

The subscription expired for some other reason.

## See Also

### Subscripton renewal and expiration

`type autoRenewStatus`

The renewal status for an auto-renewable subscription.

`type autoRenewProductId`

The product identifier of the product that will renew at the next billing
period.

`type expiresDate`

The UNIX time, in milliseconds, an auto-renewable subscription purchase
expires or renews.

`type isUpgraded`

A Boolean value that indicates whether the user upgraded to another
subscription.

`type renewalDate`

The UNIX time, in milliseconds, when the most recent auto-renewable
subscription purchase expires.

Type

# expiresDate

The UNIX time, in milliseconds, an auto-renewable subscription purchase
expires or renews.

App Store Server Notifications 2.0+

    
    
    timestamp expiresDate

## Discussion

The `expiresDate` is a static value that applies for each transaction. When
the auto-renewable subscription renews, the App Store creates a new
transaction with a new `expiresDate`.

## See Also

### Subscripton renewal and expiration

`type autoRenewStatus`

The renewal status for an auto-renewable subscription.

`type autoRenewProductId`

The product identifier of the product that will renew at the next billing
period.

`type expirationIntent`

The reason a subscription expired.

`type isUpgraded`

A Boolean value that indicates whether the user upgraded to another
subscription.

`type renewalDate`

The UNIX time, in milliseconds, when the most recent auto-renewable
subscription purchase expires.

Type

# isUpgraded

A Boolean value that indicates whether the user upgraded to another
subscription.

App Store Server Notifications 2.0+

    
    
    boolean isUpgraded

## Discussion

If `isUpgraded` is `true`, the user has upgraded the subscription represented
by this transaction to another subscription. This value appears in the
transaction only when the value is `true`. To determine the service that the
customer is entitled to, look for another transaction that has a subscription
with a higher level of service. For more information about subscription groups
and levels of service, see Auto-renewable Subscriptions.

## See Also

### Subscripton renewal and expiration

`type autoRenewStatus`

The renewal status for an auto-renewable subscription.

`type autoRenewProductId`

The product identifier of the product that will renew at the next billing
period.

`type expirationIntent`

The reason a subscription expired.

`type expiresDate`

The UNIX time, in milliseconds, an auto-renewable subscription purchase
expires or renews.

`type renewalDate`

The UNIX time, in milliseconds, when the most recent auto-renewable
subscription purchase expires.

Type

# renewalDate

The UNIX time, in milliseconds, when the most recent auto-renewable
subscription purchase expires.

App Store Server Notifications 2.8+

    
    
    timestamp renewalDate

## Discussion

The `renewalDate` is a value that’s always present in the payload for auto-
renewable subscriptions, even for expired subscriptions. This date indicates
the expiration date of the most recent auto-renewable subscription purchase,
including renewals, and may be in the past. For subscriptions that renew
successfully, the `renewalDate` is the date when the subscription renews.

## See Also

### Subscripton renewal and expiration

`type autoRenewStatus`

The renewal status for an auto-renewable subscription.

`type autoRenewProductId`

The product identifier of the product that will renew at the next billing
period.

`type expirationIntent`

The reason a subscription expired.

`type expiresDate`

The UNIX time, in milliseconds, an auto-renewable subscription purchase
expires or renews.

`type isUpgraded`

A Boolean value that indicates whether the user upgraded to another
subscription.

Type

# inAppOwnershipType

A string that describes whether the transaction was purchased by the user, or
is available to them through Family Sharing.

App Store Server Notifications 2.0+

    
    
    string inAppOwnershipType

##  Possible Values

`FAMILY_SHARED`

    

The transaction belongs to a family member who benefits from the service.

`PURCHASED`

    

The transaction belongs to the purchaser.

Type

# priceIncreaseStatus

The status that indicates whether an auto-renewable subscription is subject to
a price increase.

App Store Server Notifications 2.0+

    
    
    int32 priceIncreaseStatus

##  Possible Values

`0`

    

The customer hasn’t yet responded to an auto-renewable subscription price
increase that requires customer consent.

`1`

    

The customer consented to an auto-renewable subscription price increase that
requires customer consent, or the App Store has notified the customer of an
auto-renewable subscription price increase that doesn’t require consent.

## Discussion

For more information about managing prices, see Managing Prices and Manage
pricing for auto-renewable subscriptions.

Type

# revocationDate

The UNIX time, in milliseconds, that the App Store refunded the transaction or
revoked it from Family Sharing.

App Store Server Notifications 2.0+

    
    
    timestamp revocationDate

## See Also

### Revocation date and reason

`type revocationReason`

The reason for a refunded transaction.

Type

# revocationReason

The reason for a refunded transaction.

App Store Server Notifications 2.0+

    
    
    int32 revocationReason

##  Possible Values

`0`

    

The App Store refunded the transaction on behalf of the customer for other
reasons, for example, an accidental purchase.

`1`

    

The App Store refunded the transaction on behalf of the customer due to an
actual or perceived issue within your app.

## See Also

### Revocation date and reason

`type revocationDate`

The UNIX time, in milliseconds, that the App Store refunded the transaction or
revoked it from Family Sharing.

Type

# transactionReason

The cause of a purchase transaction, which indicates whether it’s a customer’s
purchase or a renewal for an auto-renewable subscription that the system
initiates.

App Store Server Notifications 2.8+

    
    
    string transactionReason

##  Possible Values

`PURCHASE`

    

The customer initiated the purchase, which may be for any in-app purchase
type: consumable, non-consumable, non-renewing subscription, or auto-renewable
subscription.

`RENEWAL`

    

The App Store server initiated the purchase transaction to renew an auto-
renewable subscription.

## Discussion

If a customer upgrades an auto-renewable subscription, the upgrade is
effective immediately and the `transactionReason` is `PURCHASE`.

If a customer downgrades an auto-renewable subscription, the product change
occurs on the subscription renewal date. The resulting `transactionReason` is
`RENEWAL`.

Type

# signedDate

The UNIX time, in milliseconds, that the App Store signed the JSON Web
Signature data.

App Store Server Notifications 2.0+

    
    
    timestamp signedDate

## See Also

### Response types

`type notificationType`

The type that describes the in-app purchase or external purchase event for
which the App Store sends the version 2 notification.

`type subtype`

A string that provides details about select notification types in version 2.

`type version`

A string that indicates the notification’s App Store Server Notifications
version number.

`type notificationUUID`

A unique identifier for the notification.

Type

# originalTransactionId

The original transaction identifier of a purchase.

App Store Server Notifications 2.0+

    
    
    string originalTransactionId

## Discussion

This value is identical to the transaction identifier (`transactionId`) except
when the user restores or renews a subscription.

## See Also

### Transaction identifiers

`type transactionId`

The unique identifier for a transaction such as an in-app purchase, restored
purchase, or subscription renewal.

`type webOrderLineItemId`

The unique identifier of subscription purchase events across devices,
including subscription renewals.

Type

# transactionId

The unique identifier for a transaction such as an in-app purchase, restored
purchase, or subscription renewal.

App Store Server Notifications 2.0+

    
    
    string transactionId

## Discussion

The App Store generates a new value for transaction identifier every time the
subscription automatically renews or the user restores it on a new device.

When a user first purchases a subscription, the transaction identifier always
matches the original transaction identifier (`originalTransactionId`). For a
restore or renewal, the transaction identifier doesn’t match the original
transaction identifier. If a user restores or renews the same subscription
multiple times, each restore or renewal has a unique transaction identifier.

## See Also

### Transaction identifiers

`type originalTransactionId`

The original transaction identifier of a purchase.

`type webOrderLineItemId`

The unique identifier of subscription purchase events across devices,
including subscription renewals.

Type

# webOrderLineItemId

The unique identifier of subscription purchase events across devices,
including subscription renewals.

App Store Server Notifications 2.0+

    
    
    string webOrderLineItemId

## Discussion

This value applies only to auto-renewable subscriptions.

## See Also

### Transaction identifiers

`type originalTransactionId`

The original transaction identifier of a purchase.

`type transactionId`

The unique identifier for a transaction such as an in-app purchase, restored
purchase, or subscription renewal.

Type

# bundleId

The bundle identifier of an app.

App Store Server Notifications 2.0+

    
    
    string bundleId

## See Also

### App metadata and environment

`type appAppleId`

The unique identifier of an app in the App Store.

`type bundleVersion`

The version of the build that identifies an iteration of the bundle.

`type environment`

The server environment, either sandbox or production.

`type status`

The status of an auto-renewable subscription at the time the App Store signs
the notification.

Type

# appAccountToken

A UUID that associates the transaction with a user on your service.

App Store Server Notifications 2.0+

    
    
    uuid appAccountToken

## Discussion

When a customer initiates an in-app purchase, your app may create an
`appAccountToken(_:)` and send it to the App Store. The App Store returns the
same value in `appAccountToken` in the transaction information after the
customer completes the purchase.

If you’re using the Original API for in-app purchase and provide a UUID in the
`applicationUsername` property, then the `appAccountToken` field contains that
value.

Type

# productId

The product identifier of the in-app purchase.

App Store Server Notifications 2.0+

    
    
    string productId

## Discussion

You create product identifiers for in-app purchases in App Store Connect.

## See Also

### Product information

`type type`

The product type of the in-app purchase.

`type subscriptionGroupIdentifier`

The identifier of the subscription group that the subscription belongs to.

`type quantity`

The number of consumable products purchased.

Type

# type

The product type of the in-app purchase.

App Store Server Notifications 2.0+

    
    
    string type

##  Possible Values

`Auto-Renewable Subscription`

    

An auto-renewable subscription.

`Non-Consumable`

    

A non-consumable in-app purchase.

`Consumable`

    

A consumable in-app purchase.

`Non-Renewing Subscription`

    

A non-renewing subscription.

## See Also

### Product information

`type productId`

The product identifier of the in-app purchase.

`type subscriptionGroupIdentifier`

The identifier of the subscription group that the subscription belongs to.

`type quantity`

The number of consumable products purchased.

Type

# subscriptionGroupIdentifier

The identifier of the subscription group that the subscription belongs to.

App Store Server Notifications 2.0+

    
    
    string subscriptionGroupIdentifier

## Discussion

Auto-renewable subscriptions always belong to a subscription group. You create
the subscription group identifiers in App Store Connect before you create and
add an auto-renewable subscription. For more information about subscription
groups, see Offer auto-renewable subscriptions.

## See Also

### Product information

`type productId`

The product identifier of the in-app purchase.

`type type`

The product type of the in-app purchase.

`type quantity`

The number of consumable products purchased.

Type

# quantity

The number of consumable products purchased.

App Store Server Notifications 2.0+

    
    
    int32 quantity

## See Also

### Product information

`type productId`

The product identifier of the in-app purchase.

`type type`

The product type of the in-app purchase.

`type subscriptionGroupIdentifier`

The identifier of the subscription group that the subscription belongs to.

Type

# price

The price, in milliunits, of the in-app purchase or subscription offer that
you configured in App Store Connect.

App Store Server Notifications 2.9+

    
    
    int64 price

## Discussion

This value represents the price, in milliunits of the `currency`, of the in-
app purchase or subscription offer that you configured in App Store Connect.
One unit of the currency equals 1,000 milliunits.

The following table shows some examples of the values you may see in the
`price` and `currency` parameters based on prices that you may configure in
App Store Connect:

Price configured in App Store Connect| `price` parameter| `currency` parameter  
---|---|---  
$1.99 (US dollar)| 1990| USD  
KRW 3,300 (South Korean won)| 3300000| KRW  
JPY 300 (Japanese Yen)| 300000| JPY  
  
To determine the storefront, use the `storefront` value in the transaction.
Don’t use the `currency` to infer the storefront.

Important

Don’t use the `price` or `currency` values for any revenue reconciliation or
recognition. App Store Connect reporting is your source of record for
financial and accounting purposes. For more information, see Overview of
reporting tools.

For more information on how you set prices, see Set a price and Set a price
for an in-app purchase.

## See Also

### Product price and currency

`type currency`

The three-letter ISO 4217 currency code for the price of the product.

Type

# currency

The three-letter ISO 4217 currency code for the price of the product.

App Store Server Notifications 2.9+

    
    
    string currency

## Discussion

The currency property contains an ISO 4217 alpha-3 string that represents the
currency of the price of the product.

Important

Don't use the `price` or `currency` values for any revenue reconciliation or
recognition. App Store Connect reporting is your source of record for
financial and accounting purposes. For more information, see Overview of
reporting tools.

Don’t use the `currency` to infer the storefront. Use the `storefront` value
in the transaction, instead.

For more information on how you set prices, see Set a price and Set a price
for an in-app purchase.

## See Also

### Product price and currency

`type price`

The price, in milliunits, of the in-app purchase or subscription offer that
you configured in App Store Connect.

Type

# storefront

The three-letter code that represents the country or region associated with
the App Store storefront for the purchase.

App Store Server Notifications 2.8+

    
    
    string storefront

## Discussion

This property uses the ISO 3166-1 alpha-3 country code representation. This
property is the same as the `countryCode` in StoreKit.

## See Also

### Storefront info

`type storefrontId`

An Apple-defined value that uniquely identifies an App Store storefront.

Type

# storefrontId

An Apple-defined value that uniquely identifies an App Store storefront.

App Store Server Notifications 2.8+

    
    
    string storefrontId

## Discussion

This value is the same as the `id` value in StoreKit.

## See Also

### Storefront info

`type storefront`

The three-letter code that represents the country or region associated with
the App Store storefront for the purchase.

Type

# offerIdentifier

The identifier that contains the offer code or the promotional offer
identifier.

App Store Server Notifications 2.0+

    
    
    string offerIdentifier

## Discussion

The `offerIdentifier` applies only when the `offerType` has a value of `2` or
`3`.

The `offerIdentifier` provides details about the subscription offer in effect
for the transaction. Its value is either the offer code or the promotional
offer.

For more information on offer codes, see Supporting subscription offer codes
in your app and Set up offer codes. For more information on promotional
offers, see Set up promotional offers for auto-renewable subscriptions.

## See Also

### Promotional offers

`type offerType`

The type of subscription offer.

`type offerDiscountType`

The payment mode you configure for an introductory offer, promotional offer,
or offer code on an auto-renewable subscription.

Type

# offerType

The type of subscription offer.

App Store Server Notifications 2.0+

    
    
    int32 offerType

##  Possible Values

`1`

    

An introductory offer.

`2`

    

A promotional offer.

`3`

    

An offer with a subscription offer code.

## Discussion

The offer types `2` and `3` have an `offerIdentifier`.

For more information about introductory offers, see Implementing introductory
offers in your app. For more information about promotional offers, see Set up
promotional offers for auto-renewable subscriptions. For more information
about promo codes, see Promo codes overview.

## See Also

### Promotional offers

`type offerIdentifier`

The identifier that contains the offer code or the promotional offer
identifier.

`type offerDiscountType`

The payment mode you configure for an introductory offer, promotional offer,
or offer code on an auto-renewable subscription.

Type

# offerDiscountType

The payment mode you configure for an introductory offer, promotional offer,
or offer code on an auto-renewable subscription.

App Store Server Notifications 2.9+

    
    
    string offerDiscountType

##  Possible Values

`FREE_TRIAL`

    

A payment mode of a product discount that indicates a free trial.

`PAY_AS_YOU_GO`

    

A payment mode of a product discount that is billed over a single or multiple
billing periods.

`PAY_UP_FRONT`

    

A payment mode of a product discount that is paid up front.

## Discussion

You set up subscription offers and determine the payment mode when you
configure subscriptions in App Store Connect. For more information about the
Free Trial, Pay As You Go, and Pay Up Front payment modes, see Pricing and
availability.

For more information about configuring subscription offers, see: Set up
introductory offers for auto-renewable subscriptions, Set up promotional
offers for auto-renewable subscriptions, and Set up offer codes.

## See Also

### Promotional offers

`type offerIdentifier`

The identifier that contains the offer code or the promotional offer
identifier.

`type offerType`

The type of subscription offer.

Type

# originalPurchaseDate

The purchase date of the transaction associated with the original transaction
identifier.

App Store Server Notifications 2.0+

    
    
    timestamp originalPurchaseDate

## Discussion

The original purchase date is in UNIX time, in milliseconds.

## See Also

### Purchase dates

`type purchaseDate`

The time that the App Store charged the user’s account for a purchase, a
restored product, a subscription, or a subscription renewal after a lapse.

`type recentSubscriptionStartDate`

The earliest start date of a subscription in a series of auto-renewable
subscription purchases that ignores all lapses of paid service shorter than 60
days.

Type

# purchaseDate

The time that the App Store charged the user’s account for a purchase, a
restored product, a subscription, or a subscription renewal after a lapse.

App Store Server Notifications 2.0+

    
    
    timestamp purchaseDate

## Discussion

The purchase date is in UNIX time, in milliseconds.

## See Also

### Purchase dates

`type originalPurchaseDate`

The purchase date of the transaction associated with the original transaction
identifier.

`type recentSubscriptionStartDate`

The earliest start date of a subscription in a series of auto-renewable
subscription purchases that ignores all lapses of paid service shorter than 60
days.

Type

# recentSubscriptionStartDate

The earliest start date of a subscription in a series of auto-renewable
subscription purchases that ignores all lapses of paid service shorter than 60
days.

App Store Server Notifications 2.5+

    
    
    timestamp recentSubscriptionStartDate

## Discussion

For more information about the recent subscription start date, see
`recentSubscriptionStartDate`.

Important

Don’t use the `recentSubscriptionStartDate` date to calculate days of paid
service. For more information about paid days of service, see Net revenue
after a year.

## See Also

### Purchase dates

`type originalPurchaseDate`

The purchase date of the transaction associated with the original transaction
identifier.

`type purchaseDate`

The time that the App Store charged the user’s account for a purchase, a
restored product, a subscription, or a subscription renewal after a lapse.

Type

# isInBillingRetryPeriod

A Boolean value that indicates whether the App Store is attempting to
automatically renew a subscription that expired due to a billing issue.

App Store Server Notifications 2.0+

    
    
    boolean isInBillingRetryPeriod

## See Also

### Billing status

`type gracePeriodExpiresDate`

The time when the billing grace period for a subscription renewal expires.

Type

# gracePeriodExpiresDate

The time when the billing grace period for a subscription renewal expires.

App Store Server Notifications 2.0+

    
    
    timestamp gracePeriodExpiresDate

## Discussion

For more information about billing grace periods, see Enable Billing Grace
Period for auto-renewable subscriptions.

## See Also

### Billing status

`type isInBillingRetryPeriod`

A Boolean value that indicates whether the App Store is attempting to
automatically renew a subscription that expired due to a billing issue.

Type

# autoRenewStatus

The renewal status for an auto-renewable subscription.

App Store Server Notifications 2.0+

    
    
    int32 autoRenewStatus

##  Possible Values

`0`

    

Automatic renewal is off. The customer has turned off automatic renewal for
the subscription, and it won’t renew at the end of the current subscription
period.

`1`

    

Automatic renewal is on. The subscription renews at the end of the current
subscription period.

## See Also

### Subscripton renewal and expiration

`type autoRenewProductId`

The product identifier of the product that will renew at the next billing
period.

`type expirationIntent`

The reason a subscription expired.

`type expiresDate`

The UNIX time, in milliseconds, an auto-renewable subscription purchase
expires or renews.

`type isUpgraded`

A Boolean value that indicates whether the user upgraded to another
subscription.

`type renewalDate`

The UNIX time, in milliseconds, when the most recent auto-renewable
subscription purchase expires.

Type

# autoRenewProductId

The product identifier of the product that will renew at the next billing
period.

App Store Server Notifications 2.0+

    
    
    string autoRenewProductId

## See Also

### Subscripton renewal and expiration

`type autoRenewStatus`

The renewal status for an auto-renewable subscription.

`type expirationIntent`

The reason a subscription expired.

`type expiresDate`

The UNIX time, in milliseconds, an auto-renewable subscription purchase
expires or renews.

`type isUpgraded`

A Boolean value that indicates whether the user upgraded to another
subscription.

`type renewalDate`

The UNIX time, in milliseconds, when the most recent auto-renewable
subscription purchase expires.

Type

# expirationIntent

The reason a subscription expired.

App Store Server Notifications 2.0+

    
    
    int32 expirationIntent

##  Possible Values

`1`

    

The customer canceled their subscription.

`2`

    

Billing error; for example, the customer’s payment information is no longer
valid.

`3`

    

The customer didn’t consent to an auto-renewable subscription price increase
that requires customer consent, allowing the subscription to expire.

`4`

    

The product wasn’t available for purchase at the time of renewal.

`5`

    

The subscription expired for some other reason.

## See Also

### Subscripton renewal and expiration

`type autoRenewStatus`

The renewal status for an auto-renewable subscription.

`type autoRenewProductId`

The product identifier of the product that will renew at the next billing
period.

`type expiresDate`

The UNIX time, in milliseconds, an auto-renewable subscription purchase
expires or renews.

`type isUpgraded`

A Boolean value that indicates whether the user upgraded to another
subscription.

`type renewalDate`

The UNIX time, in milliseconds, when the most recent auto-renewable
subscription purchase expires.

Type

# expiresDate

The UNIX time, in milliseconds, an auto-renewable subscription purchase
expires or renews.

App Store Server Notifications 2.0+

    
    
    timestamp expiresDate

## Discussion

The `expiresDate` is a static value that applies for each transaction. When
the auto-renewable subscription renews, the App Store creates a new
transaction with a new `expiresDate`.

## See Also

### Subscripton renewal and expiration

`type autoRenewStatus`

The renewal status for an auto-renewable subscription.

`type autoRenewProductId`

The product identifier of the product that will renew at the next billing
period.

`type expirationIntent`

The reason a subscription expired.

`type isUpgraded`

A Boolean value that indicates whether the user upgraded to another
subscription.

`type renewalDate`

The UNIX time, in milliseconds, when the most recent auto-renewable
subscription purchase expires.

Type

# isUpgraded

A Boolean value that indicates whether the user upgraded to another
subscription.

App Store Server Notifications 2.0+

    
    
    boolean isUpgraded

## Discussion

If `isUpgraded` is `true`, the user has upgraded the subscription represented
by this transaction to another subscription. This value appears in the
transaction only when the value is `true`. To determine the service that the
customer is entitled to, look for another transaction that has a subscription
with a higher level of service. For more information about subscription groups
and levels of service, see Auto-renewable Subscriptions.

## See Also

### Subscripton renewal and expiration

`type autoRenewStatus`

The renewal status for an auto-renewable subscription.

`type autoRenewProductId`

The product identifier of the product that will renew at the next billing
period.

`type expirationIntent`

The reason a subscription expired.

`type expiresDate`

The UNIX time, in milliseconds, an auto-renewable subscription purchase
expires or renews.

`type renewalDate`

The UNIX time, in milliseconds, when the most recent auto-renewable
subscription purchase expires.

Type

# renewalDate

The UNIX time, in milliseconds, when the most recent auto-renewable
subscription purchase expires.

App Store Server Notifications 2.8+

    
    
    timestamp renewalDate

## Discussion

The `renewalDate` is a value that’s always present in the payload for auto-
renewable subscriptions, even for expired subscriptions. This date indicates
the expiration date of the most recent auto-renewable subscription purchase,
including renewals, and may be in the past. For subscriptions that renew
successfully, the `renewalDate` is the date when the subscription renews.

## See Also

### Subscripton renewal and expiration

`type autoRenewStatus`

The renewal status for an auto-renewable subscription.

`type autoRenewProductId`

The product identifier of the product that will renew at the next billing
period.

`type expirationIntent`

The reason a subscription expired.

`type expiresDate`

The UNIX time, in milliseconds, an auto-renewable subscription purchase
expires or renews.

`type isUpgraded`

A Boolean value that indicates whether the user upgraded to another
subscription.

Type

# inAppOwnershipType

A string that describes whether the transaction was purchased by the user, or
is available to them through Family Sharing.

App Store Server Notifications 2.0+

    
    
    string inAppOwnershipType

##  Possible Values

`FAMILY_SHARED`

    

The transaction belongs to a family member who benefits from the service.

`PURCHASED`

    

The transaction belongs to the purchaser.

Type

# priceIncreaseStatus

The status that indicates whether an auto-renewable subscription is subject to
a price increase.

App Store Server Notifications 2.0+

    
    
    int32 priceIncreaseStatus

##  Possible Values

`0`

    

The customer hasn’t yet responded to an auto-renewable subscription price
increase that requires customer consent.

`1`

    

The customer consented to an auto-renewable subscription price increase that
requires customer consent, or the App Store has notified the customer of an
auto-renewable subscription price increase that doesn’t require consent.

## Discussion

For more information about managing prices, see Managing Prices and Manage
pricing for auto-renewable subscriptions.

Type

# revocationDate

The UNIX time, in milliseconds, that the App Store refunded the transaction or
revoked it from Family Sharing.

App Store Server Notifications 2.0+

    
    
    timestamp revocationDate

## See Also

### Revocation date and reason

`type revocationReason`

The reason for a refunded transaction.

Type

# revocationReason

The reason for a refunded transaction.

App Store Server Notifications 2.0+

    
    
    int32 revocationReason

##  Possible Values

`0`

    

The App Store refunded the transaction on behalf of the customer for other
reasons, for example, an accidental purchase.

`1`

    

The App Store refunded the transaction on behalf of the customer due to an
actual or perceived issue within your app.

## See Also

### Revocation date and reason

`type revocationDate`

The UNIX time, in milliseconds, that the App Store refunded the transaction or
revoked it from Family Sharing.

Type

# transactionReason

The cause of a purchase transaction, which indicates whether it’s a customer’s
purchase or a renewal for an auto-renewable subscription that the system
initiates.

App Store Server Notifications 2.8+

    
    
    string transactionReason

##  Possible Values

`PURCHASE`

    

The customer initiated the purchase, which may be for any in-app purchase
type: consumable, non-consumable, non-renewing subscription, or auto-renewable
subscription.

`RENEWAL`

    

The App Store server initiated the purchase transaction to renew an auto-
renewable subscription.

## Discussion

If a customer upgrades an auto-renewable subscription, the upgrade is
effective immediately and the `transactionReason` is `PURCHASE`.

If a customer downgrades an auto-renewable subscription, the product change
occurs on the subscription renewal date. The resulting `transactionReason` is
`RENEWAL`.

Type

# signedDate

The UNIX time, in milliseconds, that the App Store signed the JSON Web
Signature data.

App Store Server Notifications 2.0+

    
    
    timestamp signedDate

## See Also

### Response types

`type notificationType`

The type that describes the in-app purchase or external purchase event for
which the App Store sends the version 2 notification.

`type subtype`

A string that provides details about select notification types in version 2.

`type version`

A string that indicates the notification’s App Store Server Notifications
version number.

`type notificationUUID`

A unique identifier for the notification.

Type

# originalTransactionId

The original transaction identifier of a purchase.

App Store Server Notifications 2.0+

    
    
    string originalTransactionId

## Discussion

This value is identical to the transaction identifier (`transactionId`) except
when the user restores or renews a subscription.

## See Also

### Transaction identifiers

`type transactionId`

The unique identifier for a transaction such as an in-app purchase, restored
purchase, or subscription renewal.

`type webOrderLineItemId`

The unique identifier of subscription purchase events across devices,
including subscription renewals.

Type

# transactionId

The unique identifier for a transaction such as an in-app purchase, restored
purchase, or subscription renewal.

App Store Server Notifications 2.0+

    
    
    string transactionId

## Discussion

The App Store generates a new value for transaction identifier every time the
subscription automatically renews or the user restores it on a new device.

When a user first purchases a subscription, the transaction identifier always
matches the original transaction identifier (`originalTransactionId`). For a
restore or renewal, the transaction identifier doesn’t match the original
transaction identifier. If a user restores or renews the same subscription
multiple times, each restore or renewal has a unique transaction identifier.

## See Also

### Transaction identifiers

`type originalTransactionId`

The original transaction identifier of a purchase.

`type webOrderLineItemId`

The unique identifier of subscription purchase events across devices,
including subscription renewals.

Type

# webOrderLineItemId

The unique identifier of subscription purchase events across devices,
including subscription renewals.

App Store Server Notifications 2.0+

    
    
    string webOrderLineItemId

## Discussion

This value applies only to auto-renewable subscriptions.

## See Also

### Transaction identifiers

`type originalTransactionId`

The original transaction identifier of a purchase.

`type transactionId`

The unique identifier for a transaction such as an in-app purchase, restored
purchase, or subscription renewal.

Type

# bundleId

The bundle identifier of an app.

App Store Server Notifications 2.0+

    
    
    string bundleId

## See Also

### App metadata and environment

`type appAppleId`

The unique identifier of an app in the App Store.

`type bundleVersion`

The version of the build that identifies an iteration of the bundle.

`type environment`

The server environment, either sandbox or production.

`type status`

The status of an auto-renewable subscription at the time the App Store signs
the notification.

Type

# appAccountToken

A UUID that associates the transaction with a user on your service.

App Store Server Notifications 2.0+

    
    
    uuid appAccountToken

## Discussion

When a customer initiates an in-app purchase, your app may create an
`appAccountToken(_:)` and send it to the App Store. The App Store returns the
same value in `appAccountToken` in the transaction information after the
customer completes the purchase.

If you’re using the Original API for in-app purchase and provide a UUID in the
`applicationUsername` property, then the `appAccountToken` field contains that
value.

Type

# productId

The product identifier of the in-app purchase.

App Store Server Notifications 2.0+

    
    
    string productId

## Discussion

You create product identifiers for in-app purchases in App Store Connect.

## See Also

### Product information

`type type`

The product type of the in-app purchase.

`type subscriptionGroupIdentifier`

The identifier of the subscription group that the subscription belongs to.

`type quantity`

The number of consumable products purchased.

Type

# type

The product type of the in-app purchase.

App Store Server Notifications 2.0+

    
    
    string type

##  Possible Values

`Auto-Renewable Subscription`

    

An auto-renewable subscription.

`Non-Consumable`

    

A non-consumable in-app purchase.

`Consumable`

    

A consumable in-app purchase.

`Non-Renewing Subscription`

    

A non-renewing subscription.

## See Also

### Product information

`type productId`

The product identifier of the in-app purchase.

`type subscriptionGroupIdentifier`

The identifier of the subscription group that the subscription belongs to.

`type quantity`

The number of consumable products purchased.

Type

# subscriptionGroupIdentifier

The identifier of the subscription group that the subscription belongs to.

App Store Server Notifications 2.0+

    
    
    string subscriptionGroupIdentifier

## Discussion

Auto-renewable subscriptions always belong to a subscription group. You create
the subscription group identifiers in App Store Connect before you create and
add an auto-renewable subscription. For more information about subscription
groups, see Offer auto-renewable subscriptions.

## See Also

### Product information

`type productId`

The product identifier of the in-app purchase.

`type type`

The product type of the in-app purchase.

`type quantity`

The number of consumable products purchased.

Type

# quantity

The number of consumable products purchased.

App Store Server Notifications 2.0+

    
    
    int32 quantity

## See Also

### Product information

`type productId`

The product identifier of the in-app purchase.

`type type`

The product type of the in-app purchase.

`type subscriptionGroupIdentifier`

The identifier of the subscription group that the subscription belongs to.

Type

# price

The price, in milliunits, of the in-app purchase or subscription offer that
you configured in App Store Connect.

App Store Server Notifications 2.9+

    
    
    int64 price

## Discussion

This value represents the price, in milliunits of the `currency`, of the in-
app purchase or subscription offer that you configured in App Store Connect.
One unit of the currency equals 1,000 milliunits.

The following table shows some examples of the values you may see in the
`price` and `currency` parameters based on prices that you may configure in
App Store Connect:

Price configured in App Store Connect| `price` parameter| `currency` parameter  
---|---|---  
$1.99 (US dollar)| 1990| USD  
KRW 3,300 (South Korean won)| 3300000| KRW  
JPY 300 (Japanese Yen)| 300000| JPY  
  
To determine the storefront, use the `storefront` value in the transaction.
Don’t use the `currency` to infer the storefront.

Important

Don’t use the `price` or `currency` values for any revenue reconciliation or
recognition. App Store Connect reporting is your source of record for
financial and accounting purposes. For more information, see Overview of
reporting tools.

For more information on how you set prices, see Set a price and Set a price
for an in-app purchase.

## See Also

### Product price and currency

`type currency`

The three-letter ISO 4217 currency code for the price of the product.

Type

# currency

The three-letter ISO 4217 currency code for the price of the product.

App Store Server Notifications 2.9+

    
    
    string currency

## Discussion

The currency property contains an ISO 4217 alpha-3 string that represents the
currency of the price of the product.

Important

Don't use the `price` or `currency` values for any revenue reconciliation or
recognition. App Store Connect reporting is your source of record for
financial and accounting purposes. For more information, see Overview of
reporting tools.

Don’t use the `currency` to infer the storefront. Use the `storefront` value
in the transaction, instead.

For more information on how you set prices, see Set a price and Set a price
for an in-app purchase.

## See Also

### Product price and currency

`type price`

The price, in milliunits, of the in-app purchase or subscription offer that
you configured in App Store Connect.

Type

# storefront

The three-letter code that represents the country or region associated with
the App Store storefront for the purchase.

App Store Server Notifications 2.8+

    
    
    string storefront

## Discussion

This property uses the ISO 3166-1 alpha-3 country code representation. This
property is the same as the `countryCode` in StoreKit.

## See Also

### Storefront info

`type storefrontId`

An Apple-defined value that uniquely identifies an App Store storefront.

Type

# storefrontId

An Apple-defined value that uniquely identifies an App Store storefront.

App Store Server Notifications 2.8+

    
    
    string storefrontId

## Discussion

This value is the same as the `id` value in StoreKit.

## See Also

### Storefront info

`type storefront`

The three-letter code that represents the country or region associated with
the App Store storefront for the purchase.

Type

# offerIdentifier

The identifier that contains the offer code or the promotional offer
identifier.

App Store Server Notifications 2.0+

    
    
    string offerIdentifier

## Discussion

The `offerIdentifier` applies only when the `offerType` has a value of `2` or
`3`.

The `offerIdentifier` provides details about the subscription offer in effect
for the transaction. Its value is either the offer code or the promotional
offer.

For more information on offer codes, see Supporting subscription offer codes
in your app and Set up offer codes. For more information on promotional
offers, see Set up promotional offers for auto-renewable subscriptions.

## See Also

### Promotional offers

`type offerType`

The type of subscription offer.

`type offerDiscountType`

The payment mode you configure for an introductory offer, promotional offer,
or offer code on an auto-renewable subscription.

Type

# offerType

The type of subscription offer.

App Store Server Notifications 2.0+

    
    
    int32 offerType

##  Possible Values

`1`

    

An introductory offer.

`2`

    

A promotional offer.

`3`

    

An offer with a subscription offer code.

## Discussion

The offer types `2` and `3` have an `offerIdentifier`.

For more information about introductory offers, see Implementing introductory
offers in your app. For more information about promotional offers, see Set up
promotional offers for auto-renewable subscriptions. For more information
about promo codes, see Promo codes overview.

## See Also

### Promotional offers

`type offerIdentifier`

The identifier that contains the offer code or the promotional offer
identifier.

`type offerDiscountType`

The payment mode you configure for an introductory offer, promotional offer,
or offer code on an auto-renewable subscription.

Type

# offerDiscountType

The payment mode you configure for an introductory offer, promotional offer,
or offer code on an auto-renewable subscription.

App Store Server Notifications 2.9+

    
    
    string offerDiscountType

##  Possible Values

`FREE_TRIAL`

    

A payment mode of a product discount that indicates a free trial.

`PAY_AS_YOU_GO`

    

A payment mode of a product discount that is billed over a single or multiple
billing periods.

`PAY_UP_FRONT`

    

A payment mode of a product discount that is paid up front.

## Discussion

You set up subscription offers and determine the payment mode when you
configure subscriptions in App Store Connect. For more information about the
Free Trial, Pay As You Go, and Pay Up Front payment modes, see Pricing and
availability.

For more information about configuring subscription offers, see: Set up
introductory offers for auto-renewable subscriptions, Set up promotional
offers for auto-renewable subscriptions, and Set up offer codes.

## See Also

### Promotional offers

`type offerIdentifier`

The identifier that contains the offer code or the promotional offer
identifier.

`type offerType`

The type of subscription offer.

Type

# originalPurchaseDate

The purchase date of the transaction associated with the original transaction
identifier.

App Store Server Notifications 2.0+

    
    
    timestamp originalPurchaseDate

## Discussion

The original purchase date is in UNIX time, in milliseconds.

## See Also

### Purchase dates

`type purchaseDate`

The time that the App Store charged the user’s account for a purchase, a
restored product, a subscription, or a subscription renewal after a lapse.

`type recentSubscriptionStartDate`

The earliest start date of a subscription in a series of auto-renewable
subscription purchases that ignores all lapses of paid service shorter than 60
days.

Type

# purchaseDate

The time that the App Store charged the user’s account for a purchase, a
restored product, a subscription, or a subscription renewal after a lapse.

App Store Server Notifications 2.0+

    
    
    timestamp purchaseDate

## Discussion

The purchase date is in UNIX time, in milliseconds.

## See Also

### Purchase dates

`type originalPurchaseDate`

The purchase date of the transaction associated with the original transaction
identifier.

`type recentSubscriptionStartDate`

The earliest start date of a subscription in a series of auto-renewable
subscription purchases that ignores all lapses of paid service shorter than 60
days.

Type

# recentSubscriptionStartDate

The earliest start date of a subscription in a series of auto-renewable
subscription purchases that ignores all lapses of paid service shorter than 60
days.

App Store Server Notifications 2.5+

    
    
    timestamp recentSubscriptionStartDate

## Discussion

For more information about the recent subscription start date, see
`recentSubscriptionStartDate`.

Important

Don’t use the `recentSubscriptionStartDate` date to calculate days of paid
service. For more information about paid days of service, see Net revenue
after a year.

## See Also

### Purchase dates

`type originalPurchaseDate`

The purchase date of the transaction associated with the original transaction
identifier.

`type purchaseDate`

The time that the App Store charged the user’s account for a purchase, a
restored product, a subscription, or a subscription renewal after a lapse.

Type

# isInBillingRetryPeriod

A Boolean value that indicates whether the App Store is attempting to
automatically renew a subscription that expired due to a billing issue.

App Store Server Notifications 2.0+

    
    
    boolean isInBillingRetryPeriod

## See Also

### Billing status

`type gracePeriodExpiresDate`

The time when the billing grace period for a subscription renewal expires.

Type

# gracePeriodExpiresDate

The time when the billing grace period for a subscription renewal expires.

App Store Server Notifications 2.0+

    
    
    timestamp gracePeriodExpiresDate

## Discussion

For more information about billing grace periods, see Enable Billing Grace
Period for auto-renewable subscriptions.

## See Also

### Billing status

`type isInBillingRetryPeriod`

A Boolean value that indicates whether the App Store is attempting to
automatically renew a subscription that expired due to a billing issue.

Type

# autoRenewStatus

The renewal status for an auto-renewable subscription.

App Store Server Notifications 2.0+

    
    
    int32 autoRenewStatus

##  Possible Values

`0`

    

Automatic renewal is off. The customer has turned off automatic renewal for
the subscription, and it won’t renew at the end of the current subscription
period.

`1`

    

Automatic renewal is on. The subscription renews at the end of the current
subscription period.

## See Also

### Subscripton renewal and expiration

`type autoRenewProductId`

The product identifier of the product that will renew at the next billing
period.

`type expirationIntent`

The reason a subscription expired.

`type expiresDate`

The UNIX time, in milliseconds, an auto-renewable subscription purchase
expires or renews.

`type isUpgraded`

A Boolean value that indicates whether the user upgraded to another
subscription.

`type renewalDate`

The UNIX time, in milliseconds, when the most recent auto-renewable
subscription purchase expires.

Type

# autoRenewProductId

The product identifier of the product that will renew at the next billing
period.

App Store Server Notifications 2.0+

    
    
    string autoRenewProductId

## See Also

### Subscripton renewal and expiration

`type autoRenewStatus`

The renewal status for an auto-renewable subscription.

`type expirationIntent`

The reason a subscription expired.

`type expiresDate`

The UNIX time, in milliseconds, an auto-renewable subscription purchase
expires or renews.

`type isUpgraded`

A Boolean value that indicates whether the user upgraded to another
subscription.

`type renewalDate`

The UNIX time, in milliseconds, when the most recent auto-renewable
subscription purchase expires.

Type

# expirationIntent

The reason a subscription expired.

App Store Server Notifications 2.0+

    
    
    int32 expirationIntent

##  Possible Values

`1`

    

The customer canceled their subscription.

`2`

    

Billing error; for example, the customer’s payment information is no longer
valid.

`3`

    

The customer didn’t consent to an auto-renewable subscription price increase
that requires customer consent, allowing the subscription to expire.

`4`

    

The product wasn’t available for purchase at the time of renewal.

`5`

    

The subscription expired for some other reason.

## See Also

### Subscripton renewal and expiration

`type autoRenewStatus`

The renewal status for an auto-renewable subscription.

`type autoRenewProductId`

The product identifier of the product that will renew at the next billing
period.

`type expiresDate`

The UNIX time, in milliseconds, an auto-renewable subscription purchase
expires or renews.

`type isUpgraded`

A Boolean value that indicates whether the user upgraded to another
subscription.

`type renewalDate`

The UNIX time, in milliseconds, when the most recent auto-renewable
subscription purchase expires.

Type

# expiresDate

The UNIX time, in milliseconds, an auto-renewable subscription purchase
expires or renews.

App Store Server Notifications 2.0+

    
    
    timestamp expiresDate

## Discussion

The `expiresDate` is a static value that applies for each transaction. When
the auto-renewable subscription renews, the App Store creates a new
transaction with a new `expiresDate`.

## See Also

### Subscripton renewal and expiration

`type autoRenewStatus`

The renewal status for an auto-renewable subscription.

`type autoRenewProductId`

The product identifier of the product that will renew at the next billing
period.

`type expirationIntent`

The reason a subscription expired.

`type isUpgraded`

A Boolean value that indicates whether the user upgraded to another
subscription.

`type renewalDate`

The UNIX time, in milliseconds, when the most recent auto-renewable
subscription purchase expires.

Type

# isUpgraded

A Boolean value that indicates whether the user upgraded to another
subscription.

App Store Server Notifications 2.0+

    
    
    boolean isUpgraded

## Discussion

If `isUpgraded` is `true`, the user has upgraded the subscription represented
by this transaction to another subscription. This value appears in the
transaction only when the value is `true`. To determine the service that the
customer is entitled to, look for another transaction that has a subscription
with a higher level of service. For more information about subscription groups
and levels of service, see Auto-renewable Subscriptions.

## See Also

### Subscripton renewal and expiration

`type autoRenewStatus`

The renewal status for an auto-renewable subscription.

`type autoRenewProductId`

The product identifier of the product that will renew at the next billing
period.

`type expirationIntent`

The reason a subscription expired.

`type expiresDate`

The UNIX time, in milliseconds, an auto-renewable subscription purchase
expires or renews.

`type renewalDate`

The UNIX time, in milliseconds, when the most recent auto-renewable
subscription purchase expires.

Type

# renewalDate

The UNIX time, in milliseconds, when the most recent auto-renewable
subscription purchase expires.

App Store Server Notifications 2.8+

    
    
    timestamp renewalDate

## Discussion

The `renewalDate` is a value that’s always present in the payload for auto-
renewable subscriptions, even for expired subscriptions. This date indicates
the expiration date of the most recent auto-renewable subscription purchase,
including renewals, and may be in the past. For subscriptions that renew
successfully, the `renewalDate` is the date when the subscription renews.

## See Also

### Subscripton renewal and expiration

`type autoRenewStatus`

The renewal status for an auto-renewable subscription.

`type autoRenewProductId`

The product identifier of the product that will renew at the next billing
period.

`type expirationIntent`

The reason a subscription expired.

`type expiresDate`

The UNIX time, in milliseconds, an auto-renewable subscription purchase
expires or renews.

`type isUpgraded`

A Boolean value that indicates whether the user upgraded to another
subscription.

Type

# inAppOwnershipType

A string that describes whether the transaction was purchased by the user, or
is available to them through Family Sharing.

App Store Server Notifications 2.0+

    
    
    string inAppOwnershipType

##  Possible Values

`FAMILY_SHARED`

    

The transaction belongs to a family member who benefits from the service.

`PURCHASED`

    

The transaction belongs to the purchaser.

Type

# priceIncreaseStatus

The status that indicates whether an auto-renewable subscription is subject to
a price increase.

App Store Server Notifications 2.0+

    
    
    int32 priceIncreaseStatus

##  Possible Values

`0`

    

The customer hasn’t yet responded to an auto-renewable subscription price
increase that requires customer consent.

`1`

    

The customer consented to an auto-renewable subscription price increase that
requires customer consent, or the App Store has notified the customer of an
auto-renewable subscription price increase that doesn’t require consent.

## Discussion

For more information about managing prices, see Managing Prices and Manage
pricing for auto-renewable subscriptions.

Type

# revocationDate

The UNIX time, in milliseconds, that the App Store refunded the transaction or
revoked it from Family Sharing.

App Store Server Notifications 2.0+

    
    
    timestamp revocationDate

## See Also

### Revocation date and reason

`type revocationReason`

The reason for a refunded transaction.

Type

# revocationReason

The reason for a refunded transaction.

App Store Server Notifications 2.0+

    
    
    int32 revocationReason

##  Possible Values

`0`

    

The App Store refunded the transaction on behalf of the customer for other
reasons, for example, an accidental purchase.

`1`

    

The App Store refunded the transaction on behalf of the customer due to an
actual or perceived issue within your app.

## See Also

### Revocation date and reason

`type revocationDate`

The UNIX time, in milliseconds, that the App Store refunded the transaction or
revoked it from Family Sharing.

Type

# transactionReason

The cause of a purchase transaction, which indicates whether it’s a customer’s
purchase or a renewal for an auto-renewable subscription that the system
initiates.

App Store Server Notifications 2.8+

    
    
    string transactionReason

##  Possible Values

`PURCHASE`

    

The customer initiated the purchase, which may be for any in-app purchase
type: consumable, non-consumable, non-renewing subscription, or auto-renewable
subscription.

`RENEWAL`

    

The App Store server initiated the purchase transaction to renew an auto-
renewable subscription.

## Discussion

If a customer upgrades an auto-renewable subscription, the upgrade is
effective immediately and the `transactionReason` is `PURCHASE`.

If a customer downgrades an auto-renewable subscription, the product change
occurs on the subscription renewal date. The resulting `transactionReason` is
`RENEWAL`.

Type

# signedDate

The UNIX time, in milliseconds, that the App Store signed the JSON Web
Signature data.

App Store Server Notifications 2.0+

    
    
    timestamp signedDate

## See Also

### Response types

`type notificationType`

The type that describes the in-app purchase or external purchase event for
which the App Store sends the version 2 notification.

`type subtype`

A string that provides details about select notification types in version 2.

`type version`

A string that indicates the notification’s App Store Server Notifications
version number.

`type notificationUUID`

A unique identifier for the notification.

Type

# originalTransactionId

The original transaction identifier of a purchase.

App Store Server Notifications 2.0+

    
    
    string originalTransactionId

## Discussion

This value is identical to the transaction identifier (`transactionId`) except
when the user restores or renews a subscription.

## See Also

### Transaction identifiers

`type transactionId`

The unique identifier for a transaction such as an in-app purchase, restored
purchase, or subscription renewal.

`type webOrderLineItemId`

The unique identifier of subscription purchase events across devices,
including subscription renewals.

Type

# transactionId

The unique identifier for a transaction such as an in-app purchase, restored
purchase, or subscription renewal.

App Store Server Notifications 2.0+

    
    
    string transactionId

## Discussion

The App Store generates a new value for transaction identifier every time the
subscription automatically renews or the user restores it on a new device.

When a user first purchases a subscription, the transaction identifier always
matches the original transaction identifier (`originalTransactionId`). For a
restore or renewal, the transaction identifier doesn’t match the original
transaction identifier. If a user restores or renews the same subscription
multiple times, each restore or renewal has a unique transaction identifier.

## See Also

### Transaction identifiers

`type originalTransactionId`

The original transaction identifier of a purchase.

`type webOrderLineItemId`

The unique identifier of subscription purchase events across devices,
including subscription renewals.

Type

# webOrderLineItemId

The unique identifier of subscription purchase events across devices,
including subscription renewals.

App Store Server Notifications 2.0+

    
    
    string webOrderLineItemId

## Discussion

This value applies only to auto-renewable subscriptions.

## See Also

### Transaction identifiers

`type originalTransactionId`

The original transaction identifier of a purchase.

`type transactionId`

The unique identifier for a transaction such as an in-app purchase, restored
purchase, or subscription renewal.

Type

# bundleId

The bundle identifier of an app.

App Store Server Notifications 2.0+

    
    
    string bundleId

## See Also

### App metadata and environment

`type appAppleId`

The unique identifier of an app in the App Store.

`type bundleVersion`

The version of the build that identifies an iteration of the bundle.

`type environment`

The server environment, either sandbox or production.

`type status`

The status of an auto-renewable subscription at the time the App Store signs
the notification.

Type

# appAccountToken

A UUID that associates the transaction with a user on your service.

App Store Server Notifications 2.0+

    
    
    uuid appAccountToken

## Discussion

When a customer initiates an in-app purchase, your app may create an
`appAccountToken(_:)` and send it to the App Store. The App Store returns the
same value in `appAccountToken` in the transaction information after the
customer completes the purchase.

If you’re using the Original API for in-app purchase and provide a UUID in the
`applicationUsername` property, then the `appAccountToken` field contains that
value.

Type

# productId

The product identifier of the in-app purchase.

App Store Server Notifications 2.0+

    
    
    string productId

## Discussion

You create product identifiers for in-app purchases in App Store Connect.

## See Also

### Product information

`type type`

The product type of the in-app purchase.

`type subscriptionGroupIdentifier`

The identifier of the subscription group that the subscription belongs to.

`type quantity`

The number of consumable products purchased.

Type

# type

The product type of the in-app purchase.

App Store Server Notifications 2.0+

    
    
    string type

##  Possible Values

`Auto-Renewable Subscription`

    

An auto-renewable subscription.

`Non-Consumable`

    

A non-consumable in-app purchase.

`Consumable`

    

A consumable in-app purchase.

`Non-Renewing Subscription`

    

A non-renewing subscription.

## See Also

### Product information

`type productId`

The product identifier of the in-app purchase.

`type subscriptionGroupIdentifier`

The identifier of the subscription group that the subscription belongs to.

`type quantity`

The number of consumable products purchased.

Type

# subscriptionGroupIdentifier

The identifier of the subscription group that the subscription belongs to.

App Store Server Notifications 2.0+

    
    
    string subscriptionGroupIdentifier

## Discussion

Auto-renewable subscriptions always belong to a subscription group. You create
the subscription group identifiers in App Store Connect before you create and
add an auto-renewable subscription. For more information about subscription
groups, see Offer auto-renewable subscriptions.

## See Also

### Product information

`type productId`

The product identifier of the in-app purchase.

`type type`

The product type of the in-app purchase.

`type quantity`

The number of consumable products purchased.

Type

# quantity

The number of consumable products purchased.

App Store Server Notifications 2.0+

    
    
    int32 quantity

## See Also

### Product information

`type productId`

The product identifier of the in-app purchase.

`type type`

The product type of the in-app purchase.

`type subscriptionGroupIdentifier`

The identifier of the subscription group that the subscription belongs to.

Type

# price

The price, in milliunits, of the in-app purchase or subscription offer that
you configured in App Store Connect.

App Store Server Notifications 2.9+

    
    
    int64 price

## Discussion

This value represents the price, in milliunits of the `currency`, of the in-
app purchase or subscription offer that you configured in App Store Connect.
One unit of the currency equals 1,000 milliunits.

The following table shows some examples of the values you may see in the
`price` and `currency` parameters based on prices that you may configure in
App Store Connect:

Price configured in App Store Connect| `price` parameter| `currency` parameter  
---|---|---  
$1.99 (US dollar)| 1990| USD  
KRW 3,300 (South Korean won)| 3300000| KRW  
JPY 300 (Japanese Yen)| 300000| JPY  
  
To determine the storefront, use the `storefront` value in the transaction.
Don’t use the `currency` to infer the storefront.

Important

Don’t use the `price` or `currency` values for any revenue reconciliation or
recognition. App Store Connect reporting is your source of record for
financial and accounting purposes. For more information, see Overview of
reporting tools.

For more information on how you set prices, see Set a price and Set a price
for an in-app purchase.

## See Also

### Product price and currency

`type currency`

The three-letter ISO 4217 currency code for the price of the product.

Type

# currency

The three-letter ISO 4217 currency code for the price of the product.

App Store Server Notifications 2.9+

    
    
    string currency

## Discussion

The currency property contains an ISO 4217 alpha-3 string that represents the
currency of the price of the product.

Important

Don't use the `price` or `currency` values for any revenue reconciliation or
recognition. App Store Connect reporting is your source of record for
financial and accounting purposes. For more information, see Overview of
reporting tools.

Don’t use the `currency` to infer the storefront. Use the `storefront` value
in the transaction, instead.

For more information on how you set prices, see Set a price and Set a price
for an in-app purchase.

## See Also

### Product price and currency

`type price`

The price, in milliunits, of the in-app purchase or subscription offer that
you configured in App Store Connect.

Type

# storefront

The three-letter code that represents the country or region associated with
the App Store storefront for the purchase.

App Store Server Notifications 2.8+

    
    
    string storefront

## Discussion

This property uses the ISO 3166-1 alpha-3 country code representation. This
property is the same as the `countryCode` in StoreKit.

## See Also

### Storefront info

`type storefrontId`

An Apple-defined value that uniquely identifies an App Store storefront.

Type

# storefrontId

An Apple-defined value that uniquely identifies an App Store storefront.

App Store Server Notifications 2.8+

    
    
    string storefrontId

## Discussion

This value is the same as the `id` value in StoreKit.

## See Also

### Storefront info

`type storefront`

The three-letter code that represents the country or region associated with
the App Store storefront for the purchase.

Type

# offerIdentifier

The identifier that contains the offer code or the promotional offer
identifier.

App Store Server Notifications 2.0+

    
    
    string offerIdentifier

## Discussion

The `offerIdentifier` applies only when the `offerType` has a value of `2` or
`3`.

The `offerIdentifier` provides details about the subscription offer in effect
for the transaction. Its value is either the offer code or the promotional
offer.

For more information on offer codes, see Supporting subscription offer codes
in your app and Set up offer codes. For more information on promotional
offers, see Set up promotional offers for auto-renewable subscriptions.

## See Also

### Promotional offers

`type offerType`

The type of subscription offer.

`type offerDiscountType`

The payment mode you configure for an introductory offer, promotional offer,
or offer code on an auto-renewable subscription.

Type

# offerType

The type of subscription offer.

App Store Server Notifications 2.0+

    
    
    int32 offerType

##  Possible Values

`1`

    

An introductory offer.

`2`

    

A promotional offer.

`3`

    

An offer with a subscription offer code.

## Discussion

The offer types `2` and `3` have an `offerIdentifier`.

For more information about introductory offers, see Implementing introductory
offers in your app. For more information about promotional offers, see Set up
promotional offers for auto-renewable subscriptions. For more information
about promo codes, see Promo codes overview.

## See Also

### Promotional offers

`type offerIdentifier`

The identifier that contains the offer code or the promotional offer
identifier.

`type offerDiscountType`

The payment mode you configure for an introductory offer, promotional offer,
or offer code on an auto-renewable subscription.

Type

# offerDiscountType

The payment mode you configure for an introductory offer, promotional offer,
or offer code on an auto-renewable subscription.

App Store Server Notifications 2.9+

    
    
    string offerDiscountType

##  Possible Values

`FREE_TRIAL`

    

A payment mode of a product discount that indicates a free trial.

`PAY_AS_YOU_GO`

    

A payment mode of a product discount that is billed over a single or multiple
billing periods.

`PAY_UP_FRONT`

    

A payment mode of a product discount that is paid up front.

## Discussion

You set up subscription offers and determine the payment mode when you
configure subscriptions in App Store Connect. For more information about the
Free Trial, Pay As You Go, and Pay Up Front payment modes, see Pricing and
availability.

For more information about configuring subscription offers, see: Set up
introductory offers for auto-renewable subscriptions, Set up promotional
offers for auto-renewable subscriptions, and Set up offer codes.

## See Also

### Promotional offers

`type offerIdentifier`

The identifier that contains the offer code or the promotional offer
identifier.

`type offerType`

The type of subscription offer.

Type

# originalPurchaseDate

The purchase date of the transaction associated with the original transaction
identifier.

App Store Server Notifications 2.0+

    
    
    timestamp originalPurchaseDate

## Discussion

The original purchase date is in UNIX time, in milliseconds.

## See Also

### Purchase dates

`type purchaseDate`

The time that the App Store charged the user’s account for a purchase, a
restored product, a subscription, or a subscription renewal after a lapse.

`type recentSubscriptionStartDate`

The earliest start date of a subscription in a series of auto-renewable
subscription purchases that ignores all lapses of paid service shorter than 60
days.

Type

# purchaseDate

The time that the App Store charged the user’s account for a purchase, a
restored product, a subscription, or a subscription renewal after a lapse.

App Store Server Notifications 2.0+

    
    
    timestamp purchaseDate

## Discussion

The purchase date is in UNIX time, in milliseconds.

## See Also

### Purchase dates

`type originalPurchaseDate`

The purchase date of the transaction associated with the original transaction
identifier.

`type recentSubscriptionStartDate`

The earliest start date of a subscription in a series of auto-renewable
subscription purchases that ignores all lapses of paid service shorter than 60
days.

Type

# recentSubscriptionStartDate

The earliest start date of a subscription in a series of auto-renewable
subscription purchases that ignores all lapses of paid service shorter than 60
days.

App Store Server Notifications 2.5+

    
    
    timestamp recentSubscriptionStartDate

## Discussion

For more information about the recent subscription start date, see
`recentSubscriptionStartDate`.

Important

Don’t use the `recentSubscriptionStartDate` date to calculate days of paid
service. For more information about paid days of service, see Net revenue
after a year.

## See Also

### Purchase dates

`type originalPurchaseDate`

The purchase date of the transaction associated with the original transaction
identifier.

`type purchaseDate`

The time that the App Store charged the user’s account for a purchase, a
restored product, a subscription, or a subscription renewal after a lapse.

Type

# isInBillingRetryPeriod

A Boolean value that indicates whether the App Store is attempting to
automatically renew a subscription that expired due to a billing issue.

App Store Server Notifications 2.0+

    
    
    boolean isInBillingRetryPeriod

## See Also

### Billing status

`type gracePeriodExpiresDate`

The time when the billing grace period for a subscription renewal expires.

Type

# gracePeriodExpiresDate

The time when the billing grace period for a subscription renewal expires.

App Store Server Notifications 2.0+

    
    
    timestamp gracePeriodExpiresDate

## Discussion

For more information about billing grace periods, see Enable Billing Grace
Period for auto-renewable subscriptions.

## See Also

### Billing status

`type isInBillingRetryPeriod`

A Boolean value that indicates whether the App Store is attempting to
automatically renew a subscription that expired due to a billing issue.

Type

# autoRenewStatus

The renewal status for an auto-renewable subscription.

App Store Server Notifications 2.0+

    
    
    int32 autoRenewStatus

##  Possible Values

`0`

    

Automatic renewal is off. The customer has turned off automatic renewal for
the subscription, and it won’t renew at the end of the current subscription
period.

`1`

    

Automatic renewal is on. The subscription renews at the end of the current
subscription period.

## See Also

### Subscripton renewal and expiration

`type autoRenewProductId`

The product identifier of the product that will renew at the next billing
period.

`type expirationIntent`

The reason a subscription expired.

`type expiresDate`

The UNIX time, in milliseconds, an auto-renewable subscription purchase
expires or renews.

`type isUpgraded`

A Boolean value that indicates whether the user upgraded to another
subscription.

`type renewalDate`

The UNIX time, in milliseconds, when the most recent auto-renewable
subscription purchase expires.

Type

# autoRenewProductId

The product identifier of the product that will renew at the next billing
period.

App Store Server Notifications 2.0+

    
    
    string autoRenewProductId

## See Also

### Subscripton renewal and expiration

`type autoRenewStatus`

The renewal status for an auto-renewable subscription.

`type expirationIntent`

The reason a subscription expired.

`type expiresDate`

The UNIX time, in milliseconds, an auto-renewable subscription purchase
expires or renews.

`type isUpgraded`

A Boolean value that indicates whether the user upgraded to another
subscription.

`type renewalDate`

The UNIX time, in milliseconds, when the most recent auto-renewable
subscription purchase expires.

Type

# expirationIntent

The reason a subscription expired.

App Store Server Notifications 2.0+

    
    
    int32 expirationIntent

##  Possible Values

`1`

    

The customer canceled their subscription.

`2`

    

Billing error; for example, the customer’s payment information is no longer
valid.

`3`

    

The customer didn’t consent to an auto-renewable subscription price increase
that requires customer consent, allowing the subscription to expire.

`4`

    

The product wasn’t available for purchase at the time of renewal.

`5`

    

The subscription expired for some other reason.

## See Also

### Subscripton renewal and expiration

`type autoRenewStatus`

The renewal status for an auto-renewable subscription.

`type autoRenewProductId`

The product identifier of the product that will renew at the next billing
period.

`type expiresDate`

The UNIX time, in milliseconds, an auto-renewable subscription purchase
expires or renews.

`type isUpgraded`

A Boolean value that indicates whether the user upgraded to another
subscription.

`type renewalDate`

The UNIX time, in milliseconds, when the most recent auto-renewable
subscription purchase expires.

Type

# expiresDate

The UNIX time, in milliseconds, an auto-renewable subscription purchase
expires or renews.

App Store Server Notifications 2.0+

    
    
    timestamp expiresDate

## Discussion

The `expiresDate` is a static value that applies for each transaction. When
the auto-renewable subscription renews, the App Store creates a new
transaction with a new `expiresDate`.

## See Also

### Subscripton renewal and expiration

`type autoRenewStatus`

The renewal status for an auto-renewable subscription.

`type autoRenewProductId`

The product identifier of the product that will renew at the next billing
period.

`type expirationIntent`

The reason a subscription expired.

`type isUpgraded`

A Boolean value that indicates whether the user upgraded to another
subscription.

`type renewalDate`

The UNIX time, in milliseconds, when the most recent auto-renewable
subscription purchase expires.

Type

# isUpgraded

A Boolean value that indicates whether the user upgraded to another
subscription.

App Store Server Notifications 2.0+

    
    
    boolean isUpgraded

## Discussion

If `isUpgraded` is `true`, the user has upgraded the subscription represented
by this transaction to another subscription. This value appears in the
transaction only when the value is `true`. To determine the service that the
customer is entitled to, look for another transaction that has a subscription
with a higher level of service. For more information about subscription groups
and levels of service, see Auto-renewable Subscriptions.

## See Also

### Subscripton renewal and expiration

`type autoRenewStatus`

The renewal status for an auto-renewable subscription.

`type autoRenewProductId`

The product identifier of the product that will renew at the next billing
period.

`type expirationIntent`

The reason a subscription expired.

`type expiresDate`

The UNIX time, in milliseconds, an auto-renewable subscription purchase
expires or renews.

`type renewalDate`

The UNIX time, in milliseconds, when the most recent auto-renewable
subscription purchase expires.

Type

# renewalDate

The UNIX time, in milliseconds, when the most recent auto-renewable
subscription purchase expires.

App Store Server Notifications 2.8+

    
    
    timestamp renewalDate

## Discussion

The `renewalDate` is a value that’s always present in the payload for auto-
renewable subscriptions, even for expired subscriptions. This date indicates
the expiration date of the most recent auto-renewable subscription purchase,
including renewals, and may be in the past. For subscriptions that renew
successfully, the `renewalDate` is the date when the subscription renews.

## See Also

### Subscripton renewal and expiration

`type autoRenewStatus`

The renewal status for an auto-renewable subscription.

`type autoRenewProductId`

The product identifier of the product that will renew at the next billing
period.

`type expirationIntent`

The reason a subscription expired.

`type expiresDate`

The UNIX time, in milliseconds, an auto-renewable subscription purchase
expires or renews.

`type isUpgraded`

A Boolean value that indicates whether the user upgraded to another
subscription.

Type

# inAppOwnershipType

A string that describes whether the transaction was purchased by the user, or
is available to them through Family Sharing.

App Store Server Notifications 2.0+

    
    
    string inAppOwnershipType

##  Possible Values

`FAMILY_SHARED`

    

The transaction belongs to a family member who benefits from the service.

`PURCHASED`

    

The transaction belongs to the purchaser.

Type

# priceIncreaseStatus

The status that indicates whether an auto-renewable subscription is subject to
a price increase.

App Store Server Notifications 2.0+

    
    
    int32 priceIncreaseStatus

##  Possible Values

`0`

    

The customer hasn’t yet responded to an auto-renewable subscription price
increase that requires customer consent.

`1`

    

The customer consented to an auto-renewable subscription price increase that
requires customer consent, or the App Store has notified the customer of an
auto-renewable subscription price increase that doesn’t require consent.

## Discussion

For more information about managing prices, see Managing Prices and Manage
pricing for auto-renewable subscriptions.

Type

# revocationDate

The UNIX time, in milliseconds, that the App Store refunded the transaction or
revoked it from Family Sharing.

App Store Server Notifications 2.0+

    
    
    timestamp revocationDate

## See Also

### Revocation date and reason

`type revocationReason`

The reason for a refunded transaction.

Type

# revocationReason

The reason for a refunded transaction.

App Store Server Notifications 2.0+

    
    
    int32 revocationReason

##  Possible Values

`0`

    

The App Store refunded the transaction on behalf of the customer for other
reasons, for example, an accidental purchase.

`1`

    

The App Store refunded the transaction on behalf of the customer due to an
actual or perceived issue within your app.

## See Also

### Revocation date and reason

`type revocationDate`

The UNIX time, in milliseconds, that the App Store refunded the transaction or
revoked it from Family Sharing.

Type

# transactionReason

The cause of a purchase transaction, which indicates whether it’s a customer’s
purchase or a renewal for an auto-renewable subscription that the system
initiates.

App Store Server Notifications 2.8+

    
    
    string transactionReason

##  Possible Values

`PURCHASE`

    

The customer initiated the purchase, which may be for any in-app purchase
type: consumable, non-consumable, non-renewing subscription, or auto-renewable
subscription.

`RENEWAL`

    

The App Store server initiated the purchase transaction to renew an auto-
renewable subscription.

## Discussion

If a customer upgrades an auto-renewable subscription, the upgrade is
effective immediately and the `transactionReason` is `PURCHASE`.

If a customer downgrades an auto-renewable subscription, the product change
occurs on the subscription renewal date. The resulting `transactionReason` is
`RENEWAL`.

Type

# signedDate

The UNIX time, in milliseconds, that the App Store signed the JSON Web
Signature data.

App Store Server Notifications 2.0+

    
    
    timestamp signedDate

## See Also

### Response types

`type notificationType`

The type that describes the in-app purchase or external purchase event for
which the App Store sends the version 2 notification.

`type subtype`

A string that provides details about select notification types in version 2.

`type version`

A string that indicates the notification’s App Store Server Notifications
version number.

`type notificationUUID`

A unique identifier for the notification.

Type

# originalTransactionId

The original transaction identifier of a purchase.

App Store Server Notifications 2.0+

    
    
    string originalTransactionId

## Discussion

This value is identical to the transaction identifier (`transactionId`) except
when the user restores or renews a subscription.

## See Also

### Transaction identifiers

`type transactionId`

The unique identifier for a transaction such as an in-app purchase, restored
purchase, or subscription renewal.

`type webOrderLineItemId`

The unique identifier of subscription purchase events across devices,
including subscription renewals.

Type

# transactionId

The unique identifier for a transaction such as an in-app purchase, restored
purchase, or subscription renewal.

App Store Server Notifications 2.0+

    
    
    string transactionId

## Discussion

The App Store generates a new value for transaction identifier every time the
subscription automatically renews or the user restores it on a new device.

When a user first purchases a subscription, the transaction identifier always
matches the original transaction identifier (`originalTransactionId`). For a
restore or renewal, the transaction identifier doesn’t match the original
transaction identifier. If a user restores or renews the same subscription
multiple times, each restore or renewal has a unique transaction identifier.

## See Also

### Transaction identifiers

`type originalTransactionId`

The original transaction identifier of a purchase.

`type webOrderLineItemId`

The unique identifier of subscription purchase events across devices,
including subscription renewals.

Type

# webOrderLineItemId

The unique identifier of subscription purchase events across devices,
including subscription renewals.

App Store Server Notifications 2.0+

    
    
    string webOrderLineItemId

## Discussion

This value applies only to auto-renewable subscriptions.

## See Also

### Transaction identifiers

`type originalTransactionId`

The original transaction identifier of a purchase.

`type transactionId`

The unique identifier for a transaction such as an in-app purchase, restored
purchase, or subscription renewal.

Type

# bundleId

The bundle identifier of an app.

App Store Server Notifications 2.0+

    
    
    string bundleId

## See Also

### App metadata and environment

`type appAppleId`

The unique identifier of an app in the App Store.

`type bundleVersion`

The version of the build that identifies an iteration of the bundle.

`type environment`

The server environment, either sandbox or production.

`type status`

The status of an auto-renewable subscription at the time the App Store signs
the notification.

Type

# appAccountToken

A UUID that associates the transaction with a user on your service.

App Store Server Notifications 2.0+

    
    
    uuid appAccountToken

## Discussion

When a customer initiates an in-app purchase, your app may create an
`appAccountToken(_:)` and send it to the App Store. The App Store returns the
same value in `appAccountToken` in the transaction information after the
customer completes the purchase.

If you’re using the Original API for in-app purchase and provide a UUID in the
`applicationUsername` property, then the `appAccountToken` field contains that
value.

Type

# productId

The product identifier of the in-app purchase.

App Store Server Notifications 2.0+

    
    
    string productId

## Discussion

You create product identifiers for in-app purchases in App Store Connect.

## See Also

### Product information

`type type`

The product type of the in-app purchase.

`type subscriptionGroupIdentifier`

The identifier of the subscription group that the subscription belongs to.

`type quantity`

The number of consumable products purchased.

Type

# type

The product type of the in-app purchase.

App Store Server Notifications 2.0+

    
    
    string type

##  Possible Values

`Auto-Renewable Subscription`

    

An auto-renewable subscription.

`Non-Consumable`

    

A non-consumable in-app purchase.

`Consumable`

    

A consumable in-app purchase.

`Non-Renewing Subscription`

    

A non-renewing subscription.

## See Also

### Product information

`type productId`

The product identifier of the in-app purchase.

`type subscriptionGroupIdentifier`

The identifier of the subscription group that the subscription belongs to.

`type quantity`

The number of consumable products purchased.

Type

# subscriptionGroupIdentifier

The identifier of the subscription group that the subscription belongs to.

App Store Server Notifications 2.0+

    
    
    string subscriptionGroupIdentifier

## Discussion

Auto-renewable subscriptions always belong to a subscription group. You create
the subscription group identifiers in App Store Connect before you create and
add an auto-renewable subscription. For more information about subscription
groups, see Offer auto-renewable subscriptions.

## See Also

### Product information

`type productId`

The product identifier of the in-app purchase.

`type type`

The product type of the in-app purchase.

`type quantity`

The number of consumable products purchased.

Type

# quantity

The number of consumable products purchased.

App Store Server Notifications 2.0+

    
    
    int32 quantity

## See Also

### Product information

`type productId`

The product identifier of the in-app purchase.

`type type`

The product type of the in-app purchase.

`type subscriptionGroupIdentifier`

The identifier of the subscription group that the subscription belongs to.

Type

# price

The price, in milliunits, of the in-app purchase or subscription offer that
you configured in App Store Connect.

App Store Server Notifications 2.9+

    
    
    int64 price

## Discussion

This value represents the price, in milliunits of the `currency`, of the in-
app purchase or subscription offer that you configured in App Store Connect.
One unit of the currency equals 1,000 milliunits.

The following table shows some examples of the values you may see in the
`price` and `currency` parameters based on prices that you may configure in
App Store Connect:

Price configured in App Store Connect| `price` parameter| `currency` parameter  
---|---|---  
$1.99 (US dollar)| 1990| USD  
KRW 3,300 (South Korean won)| 3300000| KRW  
JPY 300 (Japanese Yen)| 300000| JPY  
  
To determine the storefront, use the `storefront` value in the transaction.
Don’t use the `currency` to infer the storefront.

Important

Don’t use the `price` or `currency` values for any revenue reconciliation or
recognition. App Store Connect reporting is your source of record for
financial and accounting purposes. For more information, see Overview of
reporting tools.

For more information on how you set prices, see Set a price and Set a price
for an in-app purchase.

## See Also

### Product price and currency

`type currency`

The three-letter ISO 4217 currency code for the price of the product.

Type

# currency

The three-letter ISO 4217 currency code for the price of the product.

App Store Server Notifications 2.9+

    
    
    string currency

## Discussion

The currency property contains an ISO 4217 alpha-3 string that represents the
currency of the price of the product.

Important

Don't use the `price` or `currency` values for any revenue reconciliation or
recognition. App Store Connect reporting is your source of record for
financial and accounting purposes. For more information, see Overview of
reporting tools.

Don’t use the `currency` to infer the storefront. Use the `storefront` value
in the transaction, instead.

For more information on how you set prices, see Set a price and Set a price
for an in-app purchase.

## See Also

### Product price and currency

`type price`

The price, in milliunits, of the in-app purchase or subscription offer that
you configured in App Store Connect.

Type

# storefront

The three-letter code that represents the country or region associated with
the App Store storefront for the purchase.

App Store Server Notifications 2.8+

    
    
    string storefront

## Discussion

This property uses the ISO 3166-1 alpha-3 country code representation. This
property is the same as the `countryCode` in StoreKit.

## See Also

### Storefront info

`type storefrontId`

An Apple-defined value that uniquely identifies an App Store storefront.

Type

# storefrontId

An Apple-defined value that uniquely identifies an App Store storefront.

App Store Server Notifications 2.8+

    
    
    string storefrontId

## Discussion

This value is the same as the `id` value in StoreKit.

## See Also

### Storefront info

`type storefront`

The three-letter code that represents the country or region associated with
the App Store storefront for the purchase.

Type

# offerIdentifier

The identifier that contains the offer code or the promotional offer
identifier.

App Store Server Notifications 2.0+

    
    
    string offerIdentifier

## Discussion

The `offerIdentifier` applies only when the `offerType` has a value of `2` or
`3`.

The `offerIdentifier` provides details about the subscription offer in effect
for the transaction. Its value is either the offer code or the promotional
offer.

For more information on offer codes, see Supporting subscription offer codes
in your app and Set up offer codes. For more information on promotional
offers, see Set up promotional offers for auto-renewable subscriptions.

## See Also

### Promotional offers

`type offerType`

The type of subscription offer.

`type offerDiscountType`

The payment mode you configure for an introductory offer, promotional offer,
or offer code on an auto-renewable subscription.

Type

# offerType

The type of subscription offer.

App Store Server Notifications 2.0+

    
    
    int32 offerType

##  Possible Values

`1`

    

An introductory offer.

`2`

    

A promotional offer.

`3`

    

An offer with a subscription offer code.

## Discussion

The offer types `2` and `3` have an `offerIdentifier`.

For more information about introductory offers, see Implementing introductory
offers in your app. For more information about promotional offers, see Set up
promotional offers for auto-renewable subscriptions. For more information
about promo codes, see Promo codes overview.

## See Also

### Promotional offers

`type offerIdentifier`

The identifier that contains the offer code or the promotional offer
identifier.

`type offerDiscountType`

The payment mode you configure for an introductory offer, promotional offer,
or offer code on an auto-renewable subscription.

Type

# offerDiscountType

The payment mode you configure for an introductory offer, promotional offer,
or offer code on an auto-renewable subscription.

App Store Server Notifications 2.9+

    
    
    string offerDiscountType

##  Possible Values

`FREE_TRIAL`

    

A payment mode of a product discount that indicates a free trial.

`PAY_AS_YOU_GO`

    

A payment mode of a product discount that is billed over a single or multiple
billing periods.

`PAY_UP_FRONT`

    

A payment mode of a product discount that is paid up front.

## Discussion

You set up subscription offers and determine the payment mode when you
configure subscriptions in App Store Connect. For more information about the
Free Trial, Pay As You Go, and Pay Up Front payment modes, see Pricing and
availability.

For more information about configuring subscription offers, see: Set up
introductory offers for auto-renewable subscriptions, Set up promotional
offers for auto-renewable subscriptions, and Set up offer codes.

## See Also

### Promotional offers

`type offerIdentifier`

The identifier that contains the offer code or the promotional offer
identifier.

`type offerType`

The type of subscription offer.

Type

# originalPurchaseDate

The purchase date of the transaction associated with the original transaction
identifier.

App Store Server Notifications 2.0+

    
    
    timestamp originalPurchaseDate

## Discussion

The original purchase date is in UNIX time, in milliseconds.

## See Also

### Purchase dates

`type purchaseDate`

The time that the App Store charged the user’s account for a purchase, a
restored product, a subscription, or a subscription renewal after a lapse.

`type recentSubscriptionStartDate`

The earliest start date of a subscription in a series of auto-renewable
subscription purchases that ignores all lapses of paid service shorter than 60
days.

Type

# purchaseDate

The time that the App Store charged the user’s account for a purchase, a
restored product, a subscription, or a subscription renewal after a lapse.

App Store Server Notifications 2.0+

    
    
    timestamp purchaseDate

## Discussion

The purchase date is in UNIX time, in milliseconds.

## See Also

### Purchase dates

`type originalPurchaseDate`

The purchase date of the transaction associated with the original transaction
identifier.

`type recentSubscriptionStartDate`

The earliest start date of a subscription in a series of auto-renewable
subscription purchases that ignores all lapses of paid service shorter than 60
days.

Type

# recentSubscriptionStartDate

The earliest start date of a subscription in a series of auto-renewable
subscription purchases that ignores all lapses of paid service shorter than 60
days.

App Store Server Notifications 2.5+

    
    
    timestamp recentSubscriptionStartDate

## Discussion

For more information about the recent subscription start date, see
`recentSubscriptionStartDate`.

Important

Don’t use the `recentSubscriptionStartDate` date to calculate days of paid
service. For more information about paid days of service, see Net revenue
after a year.

## See Also

### Purchase dates

`type originalPurchaseDate`

The purchase date of the transaction associated with the original transaction
identifier.

`type purchaseDate`

The time that the App Store charged the user’s account for a purchase, a
restored product, a subscription, or a subscription renewal after a lapse.

Type

# isInBillingRetryPeriod

A Boolean value that indicates whether the App Store is attempting to
automatically renew a subscription that expired due to a billing issue.

App Store Server Notifications 2.0+

    
    
    boolean isInBillingRetryPeriod

## See Also

### Billing status

`type gracePeriodExpiresDate`

The time when the billing grace period for a subscription renewal expires.

Type

# gracePeriodExpiresDate

The time when the billing grace period for a subscription renewal expires.

App Store Server Notifications 2.0+

    
    
    timestamp gracePeriodExpiresDate

## Discussion

For more information about billing grace periods, see Enable Billing Grace
Period for auto-renewable subscriptions.

## See Also

### Billing status

`type isInBillingRetryPeriod`

A Boolean value that indicates whether the App Store is attempting to
automatically renew a subscription that expired due to a billing issue.

Type

# autoRenewStatus

The renewal status for an auto-renewable subscription.

App Store Server Notifications 2.0+

    
    
    int32 autoRenewStatus

##  Possible Values

`0`

    

Automatic renewal is off. The customer has turned off automatic renewal for
the subscription, and it won’t renew at the end of the current subscription
period.

`1`

    

Automatic renewal is on. The subscription renews at the end of the current
subscription period.

## See Also

### Subscripton renewal and expiration

`type autoRenewProductId`

The product identifier of the product that will renew at the next billing
period.

`type expirationIntent`

The reason a subscription expired.

`type expiresDate`

The UNIX time, in milliseconds, an auto-renewable subscription purchase
expires or renews.

`type isUpgraded`

A Boolean value that indicates whether the user upgraded to another
subscription.

`type renewalDate`

The UNIX time, in milliseconds, when the most recent auto-renewable
subscription purchase expires.

Type

# autoRenewProductId

The product identifier of the product that will renew at the next billing
period.

App Store Server Notifications 2.0+

    
    
    string autoRenewProductId

## See Also

### Subscripton renewal and expiration

`type autoRenewStatus`

The renewal status for an auto-renewable subscription.

`type expirationIntent`

The reason a subscription expired.

`type expiresDate`

The UNIX time, in milliseconds, an auto-renewable subscription purchase
expires or renews.

`type isUpgraded`

A Boolean value that indicates whether the user upgraded to another
subscription.

`type renewalDate`

The UNIX time, in milliseconds, when the most recent auto-renewable
subscription purchase expires.

Type

# expirationIntent

The reason a subscription expired.

App Store Server Notifications 2.0+

    
    
    int32 expirationIntent

##  Possible Values

`1`

    

The customer canceled their subscription.

`2`

    

Billing error; for example, the customer’s payment information is no longer
valid.

`3`

    

The customer didn’t consent to an auto-renewable subscription price increase
that requires customer consent, allowing the subscription to expire.

`4`

    

The product wasn’t available for purchase at the time of renewal.

`5`

    

The subscription expired for some other reason.

## See Also

### Subscripton renewal and expiration

`type autoRenewStatus`

The renewal status for an auto-renewable subscription.

`type autoRenewProductId`

The product identifier of the product that will renew at the next billing
period.

`type expiresDate`

The UNIX time, in milliseconds, an auto-renewable subscription purchase
expires or renews.

`type isUpgraded`

A Boolean value that indicates whether the user upgraded to another
subscription.

`type renewalDate`

The UNIX time, in milliseconds, when the most recent auto-renewable
subscription purchase expires.

Type

# expiresDate

The UNIX time, in milliseconds, an auto-renewable subscription purchase
expires or renews.

App Store Server Notifications 2.0+

    
    
    timestamp expiresDate

## Discussion

The `expiresDate` is a static value that applies for each transaction. When
the auto-renewable subscription renews, the App Store creates a new
transaction with a new `expiresDate`.

## See Also

### Subscripton renewal and expiration

`type autoRenewStatus`

The renewal status for an auto-renewable subscription.

`type autoRenewProductId`

The product identifier of the product that will renew at the next billing
period.

`type expirationIntent`

The reason a subscription expired.

`type isUpgraded`

A Boolean value that indicates whether the user upgraded to another
subscription.

`type renewalDate`

The UNIX time, in milliseconds, when the most recent auto-renewable
subscription purchase expires.

Type

# isUpgraded

A Boolean value that indicates whether the user upgraded to another
subscription.

App Store Server Notifications 2.0+

    
    
    boolean isUpgraded

## Discussion

If `isUpgraded` is `true`, the user has upgraded the subscription represented
by this transaction to another subscription. This value appears in the
transaction only when the value is `true`. To determine the service that the
customer is entitled to, look for another transaction that has a subscription
with a higher level of service. For more information about subscription groups
and levels of service, see Auto-renewable Subscriptions.

## See Also

### Subscripton renewal and expiration

`type autoRenewStatus`

The renewal status for an auto-renewable subscription.

`type autoRenewProductId`

The product identifier of the product that will renew at the next billing
period.

`type expirationIntent`

The reason a subscription expired.

`type expiresDate`

The UNIX time, in milliseconds, an auto-renewable subscription purchase
expires or renews.

`type renewalDate`

The UNIX time, in milliseconds, when the most recent auto-renewable
subscription purchase expires.

Type

# renewalDate

The UNIX time, in milliseconds, when the most recent auto-renewable
subscription purchase expires.

App Store Server Notifications 2.8+

    
    
    timestamp renewalDate

## Discussion

The `renewalDate` is a value that’s always present in the payload for auto-
renewable subscriptions, even for expired subscriptions. This date indicates
the expiration date of the most recent auto-renewable subscription purchase,
including renewals, and may be in the past. For subscriptions that renew
successfully, the `renewalDate` is the date when the subscription renews.

## See Also

### Subscripton renewal and expiration

`type autoRenewStatus`

The renewal status for an auto-renewable subscription.

`type autoRenewProductId`

The product identifier of the product that will renew at the next billing
period.

`type expirationIntent`

The reason a subscription expired.

`type expiresDate`

The UNIX time, in milliseconds, an auto-renewable subscription purchase
expires or renews.

`type isUpgraded`

A Boolean value that indicates whether the user upgraded to another
subscription.

Type

# inAppOwnershipType

A string that describes whether the transaction was purchased by the user, or
is available to them through Family Sharing.

App Store Server Notifications 2.0+

    
    
    string inAppOwnershipType

##  Possible Values

`FAMILY_SHARED`

    

The transaction belongs to a family member who benefits from the service.

`PURCHASED`

    

The transaction belongs to the purchaser.

Type

# priceIncreaseStatus

The status that indicates whether an auto-renewable subscription is subject to
a price increase.

App Store Server Notifications 2.0+

    
    
    int32 priceIncreaseStatus

##  Possible Values

`0`

    

The customer hasn’t yet responded to an auto-renewable subscription price
increase that requires customer consent.

`1`

    

The customer consented to an auto-renewable subscription price increase that
requires customer consent, or the App Store has notified the customer of an
auto-renewable subscription price increase that doesn’t require consent.

## Discussion

For more information about managing prices, see Managing Prices and Manage
pricing for auto-renewable subscriptions.

Type

# revocationDate

The UNIX time, in milliseconds, that the App Store refunded the transaction or
revoked it from Family Sharing.

App Store Server Notifications 2.0+

    
    
    timestamp revocationDate

## See Also

### Revocation date and reason

`type revocationReason`

The reason for a refunded transaction.

Type

# revocationReason

The reason for a refunded transaction.

App Store Server Notifications 2.0+

    
    
    int32 revocationReason

##  Possible Values

`0`

    

The App Store refunded the transaction on behalf of the customer for other
reasons, for example, an accidental purchase.

`1`

    

The App Store refunded the transaction on behalf of the customer due to an
actual or perceived issue within your app.

## See Also

### Revocation date and reason

`type revocationDate`

The UNIX time, in milliseconds, that the App Store refunded the transaction or
revoked it from Family Sharing.

Type

# transactionReason

The cause of a purchase transaction, which indicates whether it’s a customer’s
purchase or a renewal for an auto-renewable subscription that the system
initiates.

App Store Server Notifications 2.8+

    
    
    string transactionReason

##  Possible Values

`PURCHASE`

    

The customer initiated the purchase, which may be for any in-app purchase
type: consumable, non-consumable, non-renewing subscription, or auto-renewable
subscription.

`RENEWAL`

    

The App Store server initiated the purchase transaction to renew an auto-
renewable subscription.

## Discussion

If a customer upgrades an auto-renewable subscription, the upgrade is
effective immediately and the `transactionReason` is `PURCHASE`.

If a customer downgrades an auto-renewable subscription, the product change
occurs on the subscription renewal date. The resulting `transactionReason` is
`RENEWAL`.

Type

# signedDate

The UNIX time, in milliseconds, that the App Store signed the JSON Web
Signature data.

App Store Server Notifications 2.0+

    
    
    timestamp signedDate

## See Also

### Response types

`type notificationType`

The type that describes the in-app purchase or external purchase event for
which the App Store sends the version 2 notification.

`type subtype`

A string that provides details about select notification types in version 2.

`type version`

A string that indicates the notification’s App Store Server Notifications
version number.

`type notificationUUID`

A unique identifier for the notification.

