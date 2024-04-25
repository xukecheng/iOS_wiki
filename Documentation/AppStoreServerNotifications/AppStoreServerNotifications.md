# App Store Server Notifications Version 1

Web Service Endpoint

# App Store Server Notifications V1

Specify your secure server’s URL in App Store Connect to receive version 1
notifications.

App Store Server Notifications 1.0–2.8  Deprecated

Deprecated

The App Store Server Notifications V1 endpoint and version 1 notifications are
deprecated. Implement the App Store Server Notifications V2 endpoint on your
server to receive version 2 notifications instead.

## URL

    
    
    POST https://example.com/v1

## Response Codes

` 200 OK`

``responseBodyV1``

`OK`

The response body for a version 1 notification.

Content-Type: application/json

## Discussion

To receive server notifications from the App Store, provide your secure
server’s HTTPS URL in App Store Connect. For more information, see Enabling
App Store Server Notifications. To secure your server and receive
notifications, your server must support the Transport Layer Security (TLS)
protocol version 1.2 or later.

Upon receiving a server notification, respond to the App Store with an HTTP
status code of `200` if the post was successful. If the post was unsuccessful,
send HTTP `50x` or `40x` to have the App Store retry the notification. For
more information, see Responding to App Store Server Notifications.

Note

For version 2 notifications, see App Store Server Notifications V2.

## See Also

### Version 1 notifications

`object responseBodyV1`

The response body containing JSON data that the App Store sends in a version 1
server notification.

Deprecated

`type notification_type`

The type that describes the in-app purchase event for which the App Store
sends the version 1 notification.

Deprecated

Type

# notification_type

The type that describes the in-app purchase event for which the App Store
sends the version 1 notification.

App Store Server Notifications 1.0–2.8  Deprecated

    
    
    string notification_type

Deprecated

Implement the App Store Server Notifications V2 endpoint on your server to
receive version 2 notifications instead.

##  Possible Values

`CANCEL`

    

Indicates that Apple Support canceled the auto-renewable subscription and the
customer received a refund as of the timestamp in `cancellation_date_ms`.

`CONSUMPTION_REQUEST`

    

Indicates that the customer initiated a refund request for a consumable in-app
purchase, and the App Store is requesting that you provide consumption data.
For more information, see Send Consumption Information.

`DID_CHANGE_RENEWAL_PREF`

    

Indicates that the customer made a change in their subscription plan that
takes effect at the next renewal. The currently active plan isn’t affected.
Check the `auto_renew_product_id` field in
`unified_receipt.Pending_renewal_info` to retrieve the product identifier for
the product the customer’s subscription renews.

`DID_CHANGE_RENEWAL_STATUS`

    

Indicates a change in the subscription renewal status. In the JSON response,
check `auto_renew_status_change_date_ms` to retrieve the date and time of the
last status update. Check `auto_renew_status` to get the current renewal
status.

`DID_FAIL_TO_RENEW`

    

Indicates a subscription that failed to renew due to a billing issue. Check
`is_in_billing_retry_period` to retrieve the current retry status of the
subscription. Check `grace_period_expires_date` to get the new service
expiration date if the subscription is in a billing grace period.

`DID_RECOVER`

    

Indicates a successful automatic renewal of an expired subscription that
failed to renew in the past. Check `expires_date` to determine the next
renewal date and time.

`DID_RENEW`

    

Indicates that a customer’s subscription has successfully auto-renewed for a
new transaction period. Provide the customer with access to the subscription’s
content or service.

`INITIAL_BUY`

    

Occurs at the user’s initial purchase of the subscription. Store
`latest_receipt` on your server as a token to verify the user’s subscription
status at any time by validating it with the App Store.

`INTERACTIVE_RENEWAL`

    

Indicates the customer renewed a subscription interactively, either by using
your app’s interface, or on the App Store in the account’s Subscriptions
settings. Make service available immediately.

`PRICE_INCREASE_CONSENT`

    

Indicates that the App Store has started asking the customer to consent to
your app’s auto-renewable subscription price increase that requires consent.

In the `unified_receipt.Pending_renewal_info` object, the
`price_consent_status` value is `0` to indicate that the user hasn’t yet
responded to the price increase.

The App Store server sets the `price_consent_status` to `1` when the customer
consents to the price increase.

Check the latest price consent status by calling the Get All Subscription
Statuses endpoint in the App Store Server API. Check the `priceIncreaseStatus`
field in the `JWSRenewalInfoDecodedPayload`. You can also call verifyReceipt
to view the updated price consent status.

For more information about how StoreKit calls your app before it displays the
price consent sheet for subscription price increases that require customer
consent, see `paymentQueueShouldShowPriceConsent(_:)`. For more information
about managing subscription prices, see Managing Prices.

`REFUND`

    

Indicates that the App Store successfully refunded a transaction for a
consumable in-app purchase, a non-consumable in-app purchase, or a non-
renewing subscription. The `cancellation_date_ms` contains the timestamp of
the refunded transaction. The `original_transaction_id` and `product_id`
identify the original transaction and product. The `cancellation_reason`
contains the reason.

`REVOKE`

    

Indicates that an in-app purchase the user was entitled to through Family
Sharing is no longer available through sharing. StoreKit sends this
notification when a purchaser disabled Family Sharing for a product, the
purchaser (or family member) left the family group, or the purchaser asked for
and received a refund. Your app will also receive a
`paymentQueue(_:didRevokeEntitlementsForProductIdentifiers:)` call. For more
information about Family Sharing, see Supporting Family Sharing in your app.

`RENEWAL (DEPRECATED)`

    

As of March 10, 2021 this notification is no longer sent in production and
sandbox environments. Update your existing code to rely on the `DID_RECOVER`
notification type instead.

## Discussion

You receive and can react to server notifications in real time for the
subscription and refund events that these notification type values describe.
The `notification_type` appears in the `responseBodyV1`.

Note

If you’re receiving App Store Server Notifications Version 2, see
`responseBodyV2` and `notificationType` instead.

### Handle use cases for notification events

When events occur that affect the customer’s product and subscription life-
cycle, your server receives notifications from the App Store. Here are some
examples of product events and the server notifications you can expect to
receive:

Subscription or in-app purchase event| Notification types  
---|---  
Customer completed an initial purchase of a subscription| `INITIAL_BUY`  
Subscription is active; customer upgraded to another SKU|
`DID_CHANGE_RENEWAL_STATUS`, `INTERACTIVE_RENEWAL`  
Subscription is active; customer downgraded to another SKU|
`DID_CHANGE_RENEWAL_PREF`  
Subscription has expired; customer resubscribed to the same SKU|
`DID_CHANGE_RENEWAL_STATUS`  
Subscription has expired; customer resubscribed to another SKU (upgrade or
downgrade)| `INTERACTIVE_RENEWAL`, `DID_CHANGE_RENEWAL_STATUS`  
Customer canceled the subscription from the App Store Subscriptions settings
page. Their subscription will not auto-renew and will expire on the
`expires_date`| `DID_CHANGE_RENEWAL_STATUS`  
Customer previously canceled the subscription, but now resubscribed to same
product before the subscription expired. The subscription will auto-renew on
the `expires_date`| `DID_CHANGE_RENEWAL_STATUS`  
AppleCare refunded a subscription| `CANCEL`, `DID_CHANGE_RENEWAL_STATUS`  
Subscription failed to renew because of a billing issue| `DID_FAIL_TO_RENEW`  
Expired subscription recovered by App Store through a billing retry|
`DID_RECOVER`  
Subscription churned after failed billing retry attempts|
`DID_CHANGE_RENEWAL_STATUS`  
AppleCare successfully refunded the transaction for a consumable, non-
consumable, or a non-renewing subscription| `REFUND`  
You’ve increased the price of an auto-renewable subscription and the price
increase requires customer consent before the subscription auto-renews|
`PRICE_INCREASE_CONSENT`  
Subscription successfully auto-renewed| `DID_RENEW`  
A purchaser disabled Family Sharing for a product, the purchaser (or family
member) left the family group, or the purchaser asked for and received a
refund| `REVOKE`  
The customer initiated a refund request for a consumable in-app purchase|
`CONSUMPTION_REQUEST`  
  
### Receive notifications for the purchaser and family members

The following table identifies the notifications you receive for the purchaser
and for their family members who share products through Family Sharing. To
determine if a notification is for the purchaser or a family member, check the
value of the `in_app_ownership_type` field, which appears in the
`unified_receipt.Latest_receipt_info` of the `responseBody` object. For more
information about Family Sharing, see Supporting Family Sharing in your app.

Notification type| Received for Purchaser | Received for Family Members  
---|---|---  
`CANCEL`| YES| NO  
`CONSUMPTION_REQUEST`| YES| N/A  
`DID_CHANGE_RENEWAL_PREF`| YES| YES  
`DID_CHANGE_RENEWAL_STATUS`| YES| YES  
`DID_FAIL_TO_RENEW`| YES| YES  
`DID_RECOVER`| YES| YES  
`DID_RENEW`| YES| YES  
`INITIAL_BUY`| YES| NO  
`INTERACTIVE_RENEWAL`| YES| YES  
`PRICE_INCREASE_CONSENT`| YES| NO  
`REFUND`| YES| NO  
`REVOKE`| NO| YES  
`RENEWAL` (Deprecated)| N/A| N/A  
  
The `CONSUMPTION_REQUEST` notification applies to consumable in-app purchases,
which aren’t eligible for Family Sharing.

### Test notification events with sandbox

Your development-signed apps use the sandbox environment when you sign in to
App Store using a Sandbox Apple ID. To create a Sandbox Apple ID or test
account in App Store Connect, see Create a sandbox tester account.

If you enabled App Store Server Notifications, test your logic for
transactions in the sandbox environment. To determine if a notification for a
subscription event occurred in the test environment, check whether the value
of the `environment` field in the JSON `responseBodyV1` object equals
`Sandbox`.

The following notification types are available in sandbox: `INITIAL_BUY`,
`DID_CHANGE_RENEWAL_PREF`, `DID_CHANGE_RENEWAL_STATUS`, `DID_RENEW`,
`INTERACTIVE_RENEWAL`, `CANCEL`, and `REFUND`. Notifications in the sandbox
environment are for the purchaser only, and have `in_app_ownership_type` equal
to `PURCHASED`. For more information about testing in-app purchases, see
Testing in-app purchases with sandbox.

## See Also

### Version 1 notifications

Web Service Endpoint

`App Store Server Notifications V1`

Specify your secure server’s URL in App Store Connect to receive version 1
notifications.

Deprecated

`object responseBodyV1`

The response body containing JSON data that the App Store sends in a version 1
server notification.

Deprecated



# object externalPurchaseToken

Type

# externalPurchaseId

The field of an external purchase token that uniquely identifies the token.

App Store Server Notifications 2.10+

    
    
    string externalPurchaseId

## Discussion

The `externalPurchaseId` is the field of an `externalPurchaseToken` that
uniquely identifies the token.

## See Also

### External purchase token fields

`type tokenCreationDate`

The field of an external purchase token that contains the UNIX date, in
milliseconds, when the system created the token.

Type

# tokenCreationDate

The field of an external purchase token that contains the UNIX date, in
milliseconds, when the system created the token.

App Store Server Notifications 2.10+

    
    
    int64 tokenCreationDate

## Discussion

This field represents the date when the system created the
`externalPurchaseToken`.

## See Also

### External purchase token fields

`type externalPurchaseId`

The field of an external purchase token that uniquely identifies the token.



# Transaction data types

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



# object data

Type

# appAppleId

The unique identifier of an app in the App Store.

App Store Server Notifications 2.0+

    
    
    int64 appAppleId

## See Also

### App metadata and environment

`type bundleId`

The bundle identifier of an app.

`type bundleVersion`

The version of the build that identifies an iteration of the bundle.

`type environment`

The server environment, either sandbox or production.

`type status`

The status of an auto-renewable subscription at the time the App Store signs
the notification.

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

# bundleVersion

The version of the build that identifies an iteration of the bundle.

App Store Server Notifications 2.0+

    
    
    string bundleVersion

## See Also

### App metadata and environment

`type appAppleId`

The unique identifier of an app in the App Store.

`type bundleId`

The bundle identifier of an app.

`type environment`

The server environment, either sandbox or production.

`type status`

The status of an auto-renewable subscription at the time the App Store signs
the notification.

Type

# environment

The server environment, either sandbox or production.

App Store Server Notifications 2.0+

    
    
    string environment

##  Possible Values

`Sandbox`

    

Indicates that the notification applies to testing in the sandbox environment.

`Production`

    

Indicates that the notification applies to the production environment.

## Discussion

You receive notifications in the sandbox environment when you opt in to
receive notifications in the sandbox environment and test your app in the
sandbox environment. TestFlight also uses the sandbox environment to send
notifications. To opt in to receive notifications, see Enter a URL for App
Store Server Notifications. For more information about testing, see Testing at
all stages of development with Xcode and the sandbox, and Beta Testing Made
Simple with TestFlight.

## See Also

### App metadata and environment

`type appAppleId`

The unique identifier of an app in the App Store.

`type bundleId`

The bundle identifier of an app.

`type bundleVersion`

The version of the build that identifies an iteration of the bundle.

`type status`

The status of an auto-renewable subscription at the time the App Store signs
the notification.

Type

# status

The status of an auto-renewable subscription at the time the App Store signs
the notification.

App Store Server Notifications 2.8+

    
    
    int32 status

##  Possible Values

`1`

    

The auto-renewable subscription is active.

`2`

    

The auto-renewable subscription is expired.

`3`

    

The auto-renewable subscription is in a billing retry period.

`4`

    

The auto-renewable subscription is in a Billing Grace Period.

`5`

    

The auto-renewable subscription is revoked.

## Discussion

This status value is current as of the `signedDate` in the decoded payload,
`responseBodyV2DecodedPayload`.

## See Also

### App metadata and environment

`type appAppleId`

The unique identifier of an app in the App Store.

`type bundleId`

The bundle identifier of an app.

`type bundleVersion`

The version of the build that identifies an iteration of the bundle.

`type environment`

The server environment, either sandbox or production.

Type

# JWSRenewalInfo

Subscription renewal information signed by the App Store, in JSON Web
Signature (JWS) format.

App Store Server Notifications 2.0+

    
    
    string JWSRenewalInfo

## Discussion

The `JWSRenewalInfo` type is a string of three Base64 URL-encoded components,
separated by a period. The string contains the JWS representation of the
subscription renewal information, signed by the App Store according to the
JSON Web Signature (JWS) IETF RFC 7515 specification.

The three components in the string are a header, a payload, and a signature,
in that order.

To read the subscription renewal information, Base64 URL-decode the payload.
Use a `JWSRenewalInfoDecodedPayload` object to read the payload information.

To read the header, Base64 URL-decode it and use a `JWSDecodedHeader` object
to access the information. Use the information in the header to verify the
signature.

## See Also

### JWS transaction and renewal info

`object JWSRenewalInfoDecodedPayload`

A decoded payload containing subscription renewal information for an auto-
renewable subscription.

`type JWSTransaction`

Transaction information signed by the App Store, in JSON Web Signature (JWS)
format.

`object JWSTransactionDecodedPayload`

A decoded payload that contains transaction information.

Type

# JWSTransaction

Transaction information signed by the App Store, in JSON Web Signature (JWS)
format.

App Store Server Notifications 2.0+

    
    
    string JWSTransaction

## Discussion

The `JWSTransaction` type is a string of three Base64 URL-encoded components,
separated by a period. The string contains the JWS representation of the
transaction information, signed by the App Store according to the JSON Web
Signature (JWS) IETF RFC 7515 specification.

The three components of the string are a header, a payload, and a signature,
in that order.

To read the transaction information, Base64 URL-decode the payload. Use a
`JWSTransactionDecodedPayload` object to read the payload information.

To read the header, decode it and use a `JWSDecodedHeader` object to access
the information. Use the information in the header to verify the signature.

## See Also

### JWS transaction and renewal info

`type JWSRenewalInfo`

Subscription renewal information signed by the App Store, in JSON Web
Signature (JWS) format.

`object JWSRenewalInfoDecodedPayload`

A decoded payload containing subscription renewal information for an auto-
renewable subscription.

`object JWSTransactionDecodedPayload`

A decoded payload that contains transaction information.

Type

# consumptionRequestReason

The customer-provided reason for a refund request.

App Store Server Notifications 2.11+

    
    
    string consumptionRequestReason

##  Possible Values

`UNINTENDED_PURCHASE`

    

The customer didn't intend to make the in-app purchase.

`FULFILLMENT_ISSUE`

    

The customer had issues with receiving or using the in-app purchase.

`UNSATISFIED_WITH_PURCHASE`

    

The customer wasn't satisfied with the in-app purchase.

`LEGAL`

    

The customer requested a refund based on a legal reason.

`OTHER`

    

The customer requested a refund for other reasons.

## Discussion

When a customer initiates a refund request for a consumable in-app purchase or
auto-renewable subscription, the App Store sends a `CONSUMPTION_REQUEST`
`notificationType` to your server. The notification includes the
`consumptionRequestReason` in the `data` object.



# object summary

Type

# requestIdentifier

A string that contains a unique identifier for a subscription-renewal-date
extension request.

App Store Server Notifications 2.7+

    
    
    uuid requestIdentifier

## Discussion

You originally specify the `requestIdentifier` when you call Extend
Subscription Renewal Dates for All Active Subscribers in the App Store Server
API.

## See Also

### Data types

`type environment`

The server environment, either sandbox or production.

`type appAppleId`

The unique identifier of an app in the App Store.

`type bundleId`

The bundle identifier of an app.

`type productId`

The product identifier of the in-app purchase.

`type storefrontCountryCodes`

A list of storefront country codes for limiting the storefronts for a
subscription-renewal-date extension.

`type storefrontCountryCode`

The three-letter code that represents the country or region associated with
the App Store storefront.

`type failedCount`

The count of subscriptions that fail to receive a subscription-renewal-date
extension.

`type succeededCount`

The count of subscriptions that successfully receive a subscription-renewal-
date extension.

Type

# environment

The server environment, either sandbox or production.

App Store Server Notifications 2.0+

    
    
    string environment

##  Possible Values

`Sandbox`

    

Indicates that the notification applies to testing in the sandbox environment.

`Production`

    

Indicates that the notification applies to the production environment.

## Discussion

You receive notifications in the sandbox environment when you opt in to
receive notifications in the sandbox environment and test your app in the
sandbox environment. TestFlight also uses the sandbox environment to send
notifications. To opt in to receive notifications, see Enter a URL for App
Store Server Notifications. For more information about testing, see Testing at
all stages of development with Xcode and the sandbox, and Beta Testing Made
Simple with TestFlight.

## See Also

### App metadata and environment

`type appAppleId`

The unique identifier of an app in the App Store.

`type bundleId`

The bundle identifier of an app.

`type bundleVersion`

The version of the build that identifies an iteration of the bundle.

`type status`

The status of an auto-renewable subscription at the time the App Store signs
the notification.

Type

# appAppleId

The unique identifier of an app in the App Store.

App Store Server Notifications 2.0+

    
    
    int64 appAppleId

## See Also

### App metadata and environment

`type bundleId`

The bundle identifier of an app.

`type bundleVersion`

The version of the build that identifies an iteration of the bundle.

`type environment`

The server environment, either sandbox or production.

`type status`

The status of an auto-renewable subscription at the time the App Store signs
the notification.

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

# storefrontCountryCodes

A list of storefront country codes for limiting the storefronts for a
subscription-renewal-date extension.

App Store Server Notifications 2.7+

    
    
    [storefrontCountryCode] storefrontCountryCodes

## Discussion

If you provide a list of storefronts when you call the Extend Subscription
Renewal Dates for All Active Subscribers endpoint, the notification returns
only those storefronts. If you don’t use the `storefrontCountryCodes`, the
subscription-renewal-date extension applies to all storefronts.

For information about providing the list of storefronts, see
`MassExtendRenewalDateRequest`.

## See Also

### Data types

`type requestIdentifier`

A string that contains a unique identifier for a subscription-renewal-date
extension request.

`type environment`

The server environment, either sandbox or production.

`type appAppleId`

The unique identifier of an app in the App Store.

`type bundleId`

The bundle identifier of an app.

`type productId`

The product identifier of the in-app purchase.

`type storefrontCountryCode`

The three-letter code that represents the country or region associated with
the App Store storefront.

`type failedCount`

The count of subscriptions that fail to receive a subscription-renewal-date
extension.

`type succeededCount`

The count of subscriptions that successfully receive a subscription-renewal-
date extension.

Type

# storefrontCountryCode

The three-letter code that represents the country or region associated with
the App Store storefront.

App Store Server Notifications 2.7+

    
    
    string storefrontCountryCode

## Discussion

This type uses the ISO 3166-1 Alpha-3 country code representation.

## See Also

### Data types

`type requestIdentifier`

A string that contains a unique identifier for a subscription-renewal-date
extension request.

`type environment`

The server environment, either sandbox or production.

`type appAppleId`

The unique identifier of an app in the App Store.

`type bundleId`

The bundle identifier of an app.

`type productId`

The product identifier of the in-app purchase.

`type storefrontCountryCodes`

A list of storefront country codes for limiting the storefronts for a
subscription-renewal-date extension.

`type failedCount`

The count of subscriptions that fail to receive a subscription-renewal-date
extension.

`type succeededCount`

The count of subscriptions that successfully receive a subscription-renewal-
date extension.

Type

# failedCount

The count of subscriptions that fail to receive a subscription-renewal-date
extension.

App Store Server Notifications 2.7+

    
    
    int64 failedCount

## See Also

### Data types

`type requestIdentifier`

A string that contains a unique identifier for a subscription-renewal-date
extension request.

`type environment`

The server environment, either sandbox or production.

`type appAppleId`

The unique identifier of an app in the App Store.

`type bundleId`

The bundle identifier of an app.

`type productId`

The product identifier of the in-app purchase.

`type storefrontCountryCodes`

A list of storefront country codes for limiting the storefronts for a
subscription-renewal-date extension.

`type storefrontCountryCode`

The three-letter code that represents the country or region associated with
the App Store storefront.

`type succeededCount`

The count of subscriptions that successfully receive a subscription-renewal-
date extension.

Type

# succeededCount

The count of subscriptions that successfully receive a subscription-renewal-
date extension.

App Store Server Notifications 2.7+

    
    
    int64 succeededCount

## See Also

### Data types

`type requestIdentifier`

A string that contains a unique identifier for a subscription-renewal-date
extension request.

`type environment`

The server environment, either sandbox or production.

`type appAppleId`

The unique identifier of an app in the App Store.

`type bundleId`

The bundle identifier of an app.

`type productId`

The product identifier of the in-app purchase.

`type storefrontCountryCodes`

A list of storefront country codes for limiting the storefronts for a
subscription-renewal-date extension.

`type storefrontCountryCode`

The three-letter code that represents the country or region associated with
the App Store storefront.

`type failedCount`

The count of subscriptions that fail to receive a subscription-renewal-date
extension.



# object responseBodyV2

Type

# signedPayload

A cryptographically signed payload, in JSON Web Signature (JWS) format, that
contains the response body for a version 2 notification.

App Store Server Notifications 2.0+

    
    
    string signedPayload

## Discussion

The `signedPayload` is a string of three Base64URL-encoded components,
separated by a period. The string contains a JWS representation of the
notification response body, signed by the App Store according to the JSON Web
Signature (JWS) IETF RFC 7515 specification.

The three components of the string are a header, a payload, and a signature,
in that order.

To read the notification response body, Base64URL-decode the payload. Use a
`responseBodyV2DecodedPayload` object to read the payload information.

To read the header, Base64URL-decode it and use a `JWSDecodedHeader` object to
access the information. Use the information in the decoded header to verify
the signature.



# object unified_receipt

Object

# unified_receipt.Latest_receipt_info

An object that contains information about the latest in-app subscription
transaction.

App Store Server Notifications 1.2+

## Properties

`app_account_token`

`string`

The `appAccountToken` associated with this transaction. This field is only
present if your app supplied an `appAccountToken(_:)` or provided a UUID for
the `applicationUsername` property when the user made the purchase.

`cancellation_date`

`string`

The time the App Store refunded a transaction or revoked it from family
sharing, in a date-time format similar to the ISO 8601. This field is present
only for refunded or revoked transactions.

`cancellation_date_ms`

`string`

The time the App Store refunded a transaction or revoked it from family
sharing, in UNIX epoch time format, in milliseconds. This field is present
only for refunded or revoked transactions. Use this time format for processing
dates. For more information, see `cancellation_date_ms`.

`cancellation_date_pst`

`string`

The time the App Store refunded a transaction or revoked it from family
sharing, in Pacific Standard Time. This field is present only for refunded or
revoked transactions.

`cancellation_reason`

`string`

The reason for a refunded or revoked transaction. A value of `1 `indicates
that the customer canceled their transaction due to an actual or perceived
issue within your app. A value of `0 `indicates that the transaction was
canceled for another reason, for example, if the customer made the purchase
accidentally.

Possible Values: `1, 0`

`expires_date`

`string`

The time a subscription expires or when it will renew, in a date-time format
similar to the ISO 8601.

`expires_date_ms`

`string`

The time when a subscription expires or when it will renew, in UNIX epoch time
format, in milliseconds. Use this time format for processing dates. For more
information, see `expires_date_ms`.

`expires_date_pst`

`string`

The time when a subscription expires or when it will renew, in Pacific
Standard Time.

`in_app_ownership_type`

`string`

A value that indicates whether the user is the purchaser of the product or is
a family member with access to the product through Family Sharing. See
`in_app_ownership_type` for more information.

Possible Values: `FAMILY_SHARED, PURCHASED`

`is_in_intro_offer_period`

`string`

An indicator of whether an auto-renewable subscription is in the introductory
price period. For more information, see `is_in_intro_offer_period`.

Possible Values: `true, false`

`is_trial_period`

`string`

An indicator of whether a subscription is in the free trial period. For more
information, see `is_trial_period`.

Possible Values: `true, false`

`is_upgraded`

`string`

An indicator that the system canceled a subscription because the user
upgraded. This field is only present for subscription upgrade transactions.

Value: `true`

`offer_code_ref_name`

`string`

The reference name of a subscription offer you configured in App Store
Connect. This field is present when a customer redeemed a subscription offer
code. For more information, see `offer_code_ref_name`.

`original_purchase_date`

`string`

The time of the original app purchase, in a date-time format similar to the
ISO 8601 standard.

`original_purchase_date_ms`

`string`

The time of the original app purchase, in UNIX epoch time format, in
milliseconds. Use this time format for processing dates. This value indicates
the date of the subscription’s initial purchase. The original purchase date
applies to all product types and remains the same in all transactions for the
same product ID. This value corresponds to the original transaction’s
`transactionDate` property in StoreKit.

`original_purchase_date_pst`

`string`

The time of the original app purchase, in Pacific Standard Time.

`original_transaction_id`

`string`

The transaction identifier of the original purchase. For more information, see
`original_transaction_id`.

`promotional_offer_id`

`string`

The identifier of the subscription offer redeemed by the user. For more
information, see `promotional_offer_id`.

`product_id`

`string`

The unique identifier of the product purchased. You provide this value when
creating the product in App Store Connect, and it corresponds to the
`productIdentifier` property of the `SKPayment` object stored in the
transaction’s `payment` property.

`purchase_date`

`string`

The time when the App Store charged the user’s account for a subscription
purchase or renewal after a lapse, in a date-time format similar to the ISO
8601 standard.

`purchase_date_ms`

`string`

The time when the App Store charged the user’s account for a subscription
purchase or renewal after a lapse, in the UNIX epoch time format, in
milliseconds. Use this time format for processing dates.

`purchase_date_pst`

`string`

The time when the App Store charged the user’s account for a subscription
purchase or renewal after a lapse, in Pacific Standard Time.

`quantity`

`string`

The number of consumable products purchased. This value corresponds to the
`quantity` property of the `SKPayment` object stored in the transaction’s
`payment` property. The value is usually `1` unless modified with a mutable
payment. The maximum value is `10`.

`subscription_group_identifier`

`string`

The identifier of the subscription group to which the subscription belongs.
The value for this field is identical to the `subscriptionGroupIdentifier`
property in `SKProduct`.

`transaction_id`

`string`

A unique identifier for a transaction such as a purchase, restore, or renewal.
For more information, see `transaction_id`.

`web_order_line_item_id`

`string`

A unique identifier for purchase events across devices, including
subscription-renewal events. This value is the primary key to identify
subscription purchases.

Object

# unified_receipt.Pending_renewal_info

An array of elements that refers to open auto-renewable subscription renewals
or ones that failed in the past.

App Store Server Notifications 1.2+

## Properties

`auto_renew_product_id`

`string`

The current renewal preference for the auto-renewable subscription. The value
for this key corresponds to the `productIdentifier` property of the product
that the customer’s subscription renews.

`auto_renew_status`

`string`

The current renewal status for the auto-renewable subscription. For more
information, see `auto_renew_status`.

Possible Values: `1, 0`

`expiration_intent`

`string`

The reason a subscription expired. This field is only present for a receipt
that contains an expired, auto-renewable subscription. For more information,
see `expiration_intent`.

Possible Values: `1, 2, 3, 4, 5`

`grace_period_expires_date`

`string`

The time at which the grace period for subscription renewals expires, in a
date-time format similar to the ISO 8601.

`grace_period_expires_date_ms`

`string`

The time at which the grace period for subscription renewals expires, in UNIX
epoch time format, in milliseconds. This key is only present for apps that
have Billing Grace Period enabled and when the user experiences a billing
error at the time of renewal. Use this time format for processing dates.

`grace_period_expires_date_pst`

`string`

The time at which the grace period for subscription renewals expires, in the
Pacific Time zone.

`is_in_billing_retry_period`

`string`

A flag that indicates Apple is attempting to renew an expired subscription
automatically. This field is only present if an auto-renewable subscription is
in the billing retry state. For more information, see
`is_in_billing_retry_period`.

Possible Values: `1, 0`

`offer_code_ref_name`

`string`

The reference name of a subscription offer you configured in App Store
Connect. This field is present when a customer redeemed a subscription offer
code. For more information, see `offer_code_ref_name`.

`original_transaction_id`

`string`

The transaction identifier of the original purchase.

`price_consent_status`

`string`

The price consent status for a subscription price increase. This field is
present only if App Store notified the customer of the price increase. The
default value is `"0"` and changes to `"1" `if the customer consents.

Possible Values: `1, 0`

`product_id`

`string`

The unique identifier of the product purchased. You provide this value when
creating the product in App Store Connect, and it corresponds to the
`productIdentifier` property of the `SKPayment` object stored in the
transaction’s `payment` property.

`promotional_offer_id`

`string`

The identifier of the promotional offer for an auto-renewable subscription
that the user redeemed. You provide this value in the Promotional Offer
Identifier field when you create the promotional offer in App Store Connect.
For more information, see `promotional_offer_id`.

`price_increase_status`

`string`

Possible Values: `1, 0`



# object JWSDecodedHeader

Type

# alg

The JSON Web Signature (JWS) header parameter that identifies the
cryptographic algorithm used to secure the JWS.

App Store Server Notifications 2.0+

    
    
    string alg

## See Also

### JWS header types

`type x5c`

The JSON Web Signature (JWS) header parameter that contains the certificate
chain that corresponds to the key used to digitally sign the JWS.

Type

# x5c

The JSON Web Signature (JWS) header parameter that contains the certificate
chain that corresponds to the key used to digitally sign the JWS.

App Store Server Notifications 2.0+

    
    
    [string] x5c

## Discussion

For more information, or to download Apple’s root and intermediate
certificates, see Apple PKI.

## See Also

### JWS header types

`type alg`

The JSON Web Signature (JWS) header parameter that identifies the
cryptographic algorithm used to secure the JWS.



# object responseBodyV2DecodedPayload

Type

# notificationType

The type that describes the in-app purchase or external purchase event for
which the App Store sends the version 2 notification.

App Store Server Notifications 2.0+

    
    
    string notificationType

##  Possible Values

`CONSUMPTION_REQUEST`

    

A notification type that indicates that the customer initiated a refund
request for a consumable in-app purchase or auto-renewable subscription, and
the App Store is requesting that you provide consumption data. For more
information, see Send Consumption Information.

`DID_CHANGE_RENEWAL_PREF`

    

A notification type that, along with its `subtype`, indicates that the user
made a change to their subscription plan. If the `subtype` is `UPGRADE`, the
user upgraded their subscription. The upgrade goes into effect immediately,
starting a new billing period, and the user receives a prorated refund for the
unused portion of the previous period. If the `subtype` is `DOWNGRADE`, the
user downgraded their subscription. Downgrades take effect at the next renewal
date and don’t affect the currently active plan.

If the `subtype` is empty, the user changed their renewal preference back to
the current subscription, effectively canceling a downgrade.

For more information on subscription levels, see Ranking subscriptions within
the group.

`DID_CHANGE_RENEWAL_STATUS`

    

A notification type that, along with its `subtype`, indicates that the user
made a change to the subscription renewal status. If the `subtype` is
`AUTO_RENEW_ENABLED`, the user reenabled subscription auto-renewal. If the
`subtype` is `AUTO_RENEW_DISABLED`, the user disabled subscription auto-
renewal, or the App Store disabled subscription auto-renewal after the user
requested a refund.

`DID_FAIL_TO_RENEW`

    

A notification type that, along with its `subtype`, indicates that the
subscription failed to renew due to a billing issue. The subscription enters
the billing retry period. If the `subtype` is `GRACE_PERIOD`, continue to
provide service through the grace period. If the `subtype` is empty, the
subscription isn’t in a grace period and you can stop providing the
subscription service.

Inform the user that there may be an issue with their billing information. The
App Store continues to retry billing for 60 days, or until the user resolves
their billing issue or cancels their subscription, whichever comes first. For
more information, see Reducing Involuntary Subscriber Churn.

`DID_RENEW`

    

A notification type that, along with its `subtype`, indicates that the
subscription successfully renewed. If the `subtype` is `BILLING_RECOVERY`, the
expired subscription that previously failed to renew has successfully renewed.
If the substate is empty, the active subscription has successfully auto-
renewed for a new transaction period. Provide the customer with access to the
subscription’s content or service.

`EXPIRED`

    

A notification type that, along with its `subtype`, indicates that a
subscription expired. If the `subtype` is `VOLUNTARY`, the subscription
expired after the user disabled subscription renewal. If the `subtype` is
`BILLING_RETRY`, the subscription expired because the billing retry period
ended without a successful billing transaction. If the `subtype` is
`PRICE_INCREASE`, the subscription expired because the user didn’t consent to
a price increase that requires user consent. If the `subtype` is
`PRODUCT_NOT_FOR_SALE`, the subscription expired because the product wasn’t
available for purchase at the time the subscription attempted to renew.

A notification without a `subtype` indicates that the subscription expired for
some other reason.

`EXTERNAL_PURCHASE_TOKEN`

    

A notification type that, along with its `subtype` `UNREPORTED`, indicates
that Apple created an external purchase token for your app but didn't receive
a report. For more information about reporting the token, see
`externalPurchaseToken`.

This notification applies only to apps that use the External Purchase API to
provide alternative payment options.

`GRACE_PERIOD_EXPIRED`

    

A notification type that indicates that the billing grace period has ended
without renewing the subscription, so you can turn off access to the service
or content. Inform the user that there may be an issue with their billing
information. The App Store continues to retry billing for 60 days, or until
the user resolves their billing issue or cancels their subscription, whichever
comes first. For more information, see Reducing Involuntary Subscriber Churn.

`OFFER_REDEEMED`

    

A notification type that, along with its `subtype`, indicates that the user
redeemed a promotional offer or offer code.

If the `subtype` is `INITIAL_BUY`, the user redeemed the offer for a first-
time purchase. If the `subtype` is `RESUBSCRIBE`, the user redeemed an offer
to resubscribe to an inactive subscription. If the `subtype` is `UPGRADE`, the
user redeemed an offer to upgrade their active subscription, which goes into
effect immediately. If the `subtype` is `DOWNGRADE`, the user redeemed an
offer to downgrade their active subscription, which goes into effect at the
next renewal date. If the user redeemed an offer for their active
subscription, you receive an `OFFER_REDEEMED` notification type without a
`subtype`.

For more information about promotional offers, see Implementing promotional
offers in your app. For more information about subscription offer codes, see
Implementing offer codes in your app.

`PRICE_INCREASE`

    

A notification type that, along with its `subtype`, indicates that the system
has informed the user of an auto-renewable subscription price increase.

If the price increase requires user consent, the `subtype` is `PENDING` if the
user hasn’t responded to the price increase, or `ACCEPTED` if the user has
consented to the price increase.

If the price increase doesn’t require user consent, the `subtype` is
`ACCEPTED`.

For information about how the system calls your app before it displays the
price consent sheet for subscription price increases that require customer
consent, see `paymentQueueShouldShowPriceConsent(_:)`. For information about
managing subscription prices, see Managing Price Increases for Auto-Renewable
Subscriptions and Managing Prices.

`REFUND`

    

A notification type that indicates that the App Store successfully refunded a
transaction for a consumable in-app purchase, a non-consumable in-app
purchase, an auto-renewable subscription, or a non-renewing subscription.

The `revocationDate` contains the timestamp of the refunded transaction. The
`originalTransactionId` and `productId` identify the original transaction and
product. The `revocationReason` contains the reason.

To request a list of all refunded transactions for a user, see Get Refund
History in the App Store Server API.

`REFUND_DECLINED`

    

A notification type that indicates the App Store declined a refund request
initiated by the app developer using any of the following methods:
`beginRefundRequest(for:in:)`, `beginRefundRequest(in:)`,
`beginRefundRequest(for:in:)`, `beginRefundRequest(in:)`, and
`refundRequestSheet(for:isPresented:onDismiss:)`.

`REFUND_REVERSED`

    

A notification type that indicates the App Store reversed a previously granted
refund due to a dispute that the customer raised. If your app revoked content
or services as a result of the related refund, it needs to reinstate them.

This notification type can apply to any in-app purchase type: consumable, non-
consumable, non-renewing subscription, and auto-renewable subscription. For
auto-renewable subscriptions, the renewal date remains unchanged when the App
Store reverses a refund.

`RENEWAL_EXTENDED`

    

A notification type that indicates the App Store extended the subscription
renewal date for a specific subscription. You request subscription-renewal-
date extensions by calling Extend a Subscription Renewal Date or Extend
Subscription Renewal Dates for All Active Subscribers in the App Store Server
API.

`RENEWAL_EXTENSION`

    

A notification type that, along with its `subtype`, indicates that the App
Store is attempting to extend the subscription renewal date that you request
by calling Extend Subscription Renewal Dates for All Active Subscribers.

If the `subtype` is `SUMMARY`, the App Store completed extending the renewal
date for all eligible subscribers. See the `summary` in the
`responseBodyV2DecodedPayload` for details. If the `subtype` is `FAILURE`, the
renewal date extension didn’t succeed for a specific subscription. See the
`data` in the `responseBodyV2DecodedPayload` for details.

`REVOKE`

    

A notification type that indicates that an in-app purchase the user was
entitled to through Family Sharing is no longer available through sharing. The
App Store sends this notification when a purchaser disables Family Sharing for
their purchase, the purchaser (or family member) leaves the family group, or
the purchaser receives a refund. Your app also receives a
`paymentQueue(_:didRevokeEntitlementsForProductIdentifiers:)` call. Family
Sharing applies to non-consumable in-app purchases and auto-renewable
subscriptions. For more information about Family Sharing, see Supporting
Family Sharing in your app.

`SUBSCRIBED`

    

A notification type that, along with its `subtype`, indicates that the user
subscribed to a product. If the `subtype` is `INITIAL_BUY`, the user either
purchased or received access through Family Sharing to the subscription for
the first time. If the `subtype` is `RESUBSCRIBE`, the user resubscribed or
received access through Family Sharing to the same subscription or to another
subscription within the same subscription group.

`TEST`

    

A notification type that the App Store server sends when you request it by
calling the Request a Test Notification endpoint. Call that endpoint to test
whether your server is receiving notifications. You receive this notification
only at your request. For troubleshooting information, see the Get Test
Notification Status endpoint.

## Discussion

The `notificationType` appears in the notification payload,
`responseBodyV2DecodedPayload`. It describes the event that leads to the
notification. Some notifications also have a `subtype` that further describes
the event. See the `responseBodyV2DecodedPayload` for more information about
the notification in the `data`, `summary`, or `externalPurchaseToken` object.

### Handle use cases for in-app purchase life-cycle events

When events occur that affect the customer’s in-app purchase and subscription
life cycle, the App Store server sends you notifications. The following tables
list the notifications by life-cycle events.

Events that enable service for subscriptions, including initial subscriptions,
resubscribing, and successful auto-renewals result in the following
notifications:

Event| Notification type| Notification subtype  
---|---|---  
Customer subscribes for the first time to any subscription within a
subscription group.| `SUBSCRIBED`| `INITIAL_BUY`  
Customer resubscribes to any subscription from the same subscription group as
their expired subscription.| `SUBSCRIBED`| `RESUBSCRIBE`  
The subscription successfully auto-renews.| `DID_RENEW`|  
A family member gains access to the subscription through Family Sharing after
the purchaser subscribes for the first time.| `SUBSCRIBED`| `INITIAL_BUY`  
A family member gains access to the subscription through Family Sharing after
the purchaser resubscribes.| `SUBSCRIBED`| `RESUBSCRIBE`  
  
Customers changing their subscription options, including upgrading,
downgrading or canceling result in the following notifications:

Event| Notification type| Notification subtype  
---|---|---  
Customer downgrades a subscription within the same subscription group.|
`DID_CHANGE_RENEWAL_PREF`| `DOWNGRADE`  
Customer reverts to the previous subscription, effectively canceling their
downgrade.| `DID_CHANGE_RENEWAL_PREF`|  
Customer upgrades a subscription within the same subscription group.|
`DID_CHANGE_RENEWAL_PREF`| `UPGRADE`  
Customer cancels the subscription from the App Store Subscriptions settings
page.| `DID_CHANGE_RENEWAL_STATUS`| `AUTO_RENEW_DISABLED`  
Customer subscribes again after canceling a subscription, which re-enables
auto-renew.| `DID_CHANGE_RENEWAL_STATUS`| `AUTO_RENEW_ENABLED`  
The system disabled auto-renew because the customer initiated a refund through
your app using the refund request API.| `DID_CHANGE_RENEWAL_STATUS`|
`AUTO_RENEW_DISABLED`  
  
Customers redeeming promotional offer or subscription offer codes result in
the following notifications:

Event| Notification type| Notification subtype  
---|---|---  
Customer redeems a promotional offer or offer code for an active
subscription.| `OFFER_REDEEMED `|  
Customer redeems an offer code to subscribe for the first time.|
`OFFER_REDEEMED`| `INITIAL_BUY`  
Customer redeems a promotional offer or offer code after their subscription
expired.| `OFFER_REDEEMED`| `RESUBSCRIBE`  
Customer redeems a promotional offer or offer code to upgrade their
subscription.| `OFFER_REDEEMED`| `UPGRADE`  
Customer redeems a promotional offer and downgrades their subscription.|
`OFFER_REDEEMED`| `DOWNGRADE`  
  
Billing events, including billing retries, entering and exiting Billing Grace
Period, and expiring subscriptions result in the following notifications:

Event| Notification type| Notification subtype  
---|---|---  
The subscription expires because the customer chose to cancel it.| `EXPIRED`|
`VOLUNTARY`  
The subscription expires because the developer removed the subscription from
sale and the renewal fails.| `EXPIRED`| `PRODUCT_NOT_FOR_SALE`  
The subscription expires because the billing retry period ends without
recovering the subscription.| `EXPIRED`| `BILLING_RETRY`  
The subscription fails to renew and enters the billing retry period. | `DID_FAIL_TO_RENEW`|   
The subscription fails to renew and enters the billing retry period with
Billing Grace Period enabled.| `DID_FAIL_TO_RENEW`| `GRACE_PERIOD`  
The billing retry successfully recovers the subscription.| `DID_RENEW`|
`BILLING_RECOVERY`  
The subscription exits the Billing Grace Period (and continues in billing
retry).| `GRACE_PERIOD_EXPIRED`|  
  
Events or notifications that occur when you increase the price of an auto-
renewable subscription include:

Event| Notification type| Notification subtype  
---|---|---  
The system informs the customer of the auto-renewable subscription price
increase that requires customer consent, and the customer doesn’t respond.|
`PRICE_INCREASE`| `PENDING`  
The auto-renewable subscription expires because the customer didn’t consent to
the price increase that requires consent.| `EXPIRED`| `PRICE_INCREASE`  
Customer consents to an auto-renewable subscription price increase that
requires consent.| `PRICE_INCREASE`| `ACCEPTED`  
The system notifies the customer of the auto-renewable subscription price
increase that doesn’t require customer consent.| `PRICE_INCREASE`| `ACCEPTED`  
Customer canceled the subscription after receiving a price increase notice or
a request to consent to a price increase.| `DID_CHANGE_RENEWAL_STATUS`|  
  
Customers requesting refunds or canceling Family Sharing result in the
following notifications:

Event| Notification type| Notification subtype  
---|---|---  
Apple refunds the transaction for a consumable or non-consumable in-app
purchase, a non-renewing subscription, or an auto-renewable subscription.|
`REFUND`|  
Apple reverses a previously granted refund due to a dispute that the customer
raised.| `REFUND_REVERSED`|  
Apple declines a refund that the customer initiated in the app, using the
request refund API.| `REFUND_DECLINED`|  
Apple requests consumption information for a refund request that a customer
initiates.| `CONSUMPTION_REQUEST`|  
A family member loses access to the subscription through Family Sharing.|
`REVOKE`|  
  
Developers requesting subscription-renewal-date extensions result in the
following notifications:

Event| Notification type| Notification subtype  
---|---|---  
The App Store successfully extends a subscription-renewal date for a specific
subscription.| `RENEWAL_EXTENDED`|  
The App Store successfully completes extending the subscription-renewal date
for all eligible subscribers.| `RENEWAL_EXTENSION`| `SUMMARY`  
The App Store failed to extend the subscription-renewal date for a specific
subscriber.| `RENEWAL_EXTENSION`| `FAILURE`  
  
## See Also

### Server notifications version 2

Web Service Endpoint

`App Store Server Notifications V2`

Specify your secure server’s URL in App Store Connect to receive version 2
notifications.

`object responseBodyV2`

The response body the App Store sends in a version 2 server notification.

`object responseBodyV2DecodedPayload`

A decoded payload that contains the version 2 notification data.

`type subtype`

A string that provides details about select notification types in version 2.

Type

# subtype

A string that provides details about select notification types in version 2.

App Store Server Notifications 2.0+

    
    
    string subtype

##  Possible Values

`ACCEPTED`

    

Applies to the `PRICE_INCREASE` `notificationType`. A notification with this
`subtype` indicates that the customer consented to the subscription price
increase if the price increase requires customer consent, or that the system
notified them of a price increase if the price increase doesn't require
customer consent.

`AUTO_RENEW_DISABLED`

    

Applies to the `DID_CHANGE_RENEWAL_STATUS` `notificationType`. A notification
with this `subtype` indicates that the user disabled subscription auto-
renewal, or the App Store disabled subscription auto-renewal after the user
requested a refund.

`AUTO_RENEW_ENABLED`

    

Applies to the `DID_CHANGE_RENEWAL_STATUS` `notificationType`. A notification
with this `subtype` indicates that the user enabled subscription auto-renewal.

`BILLING_RECOVERY`

    

Applies to the `DID_RENEW` `notificationType`. A notification with this
`subtype` indicates that the expired subscription that previously failed to
renew has successfully renewed.

`BILLING_RETRY`

    

Applies to the `EXPIRED` `notificationType`. A notification with this
`subtype` indicates that the subscription expired because the subscription
failed to renew before the billing retry period ended.

`DOWNGRADE`

    

Applies to the `DID_CHANGE_RENEWAL_PREF` `notificationType`. A notification
with this `subtype` indicates that the user downgraded their subscription or
cross-graded to a subscription with a different duration. Downgrades take
effect at the next renewal date.

`FAILURE`

    

Applies to the `RENEWAL_EXTENSION ``notificationType`. A notification with
this `subtype` indicates that the subscription-renewal-date extension failed
for an individual subscription. For details, see the `data` object in the
`responseBodyV2DecodedPayload`. For information on the request, see Extend
Subscription Renewal Dates for All Active Subscribers.

`GRACE_PERIOD`

    

Applies to the `DID_FAIL_TO_RENEW` `notificationType`. A notification with
this `subtype` indicates that the subscription failed to renew due to a
billing issue. Continue to provide access to the subscription during the grace
period.

`INITIAL_BUY`

    

Applies to the `SUBSCRIBED` `notificationType`. A notification with this
`subtype` indicates that the user purchased the subscription for the first
time or that the user received access to the subscription through Family
Sharing for the first time.

`PENDING`

    

Applies to the `PRICE_INCREASE` `notificationType`. A notification with this
`subtype` indicates that the system informed the user of the subscription
price increase, but the user hasn’t accepted it.

`PRICE_INCREASE`

    

Applies to the `EXPIRED` `notificationType`. A notification with this
`subtype` indicates that the subscription expired because the user didn’t
consent to a price increase.

`PRODUCT_NOT_FOR_SALE`

    

Applies to the `EXPIRED` `notificationType`. A notification with this
`subtype` indicates that the subscription expired because the product wasn’t
available for purchase at the time the subscription attempted to renew.

`RESUBSCRIBE`

    

Applies to the `SUBSCRIBED` `notificationType`. A notification with this
`subtype` indicates that the user resubscribed or received access through
Family Sharing to the same subscription or to another subscription within the
same subscription group.

`SUMMARY`

    

Applies to the `RENEWAL_EXTENSION ``notificationType`. A notification with
this `subtype` indicates that the App Store server completed your request to
extend the subscription renewal date for all eligible subscribers. For the
summary details, see the `summary` object in the
`responseBodyV2DecodedPayload`. For information on the request, see Extend
Subscription Renewal Dates for All Active Subscribers.

`UPGRADE`

    

Applies to the `DID_CHANGE_RENEWAL_PREF` `notificationType`. A notification
with this `subtype` indicates that the user upgraded their subscription or
cross-graded to a subscription with the same duration. Upgrades take effect
immediately.

`UNREPORTED`

    

Applies to the `EXTERNAL_PURCHASE_TOKEN` `notificationType`. A notification
with this `subtype` indicates that Apple created a token for your app but
didn't receive a report. For more information about reporting the token, see
`externalPurchaseToken`.

`VOLUNTARY`

    

Applies to the `EXPIRED` `notificationType`. A notification with this
`subtype` indicates that the subscription expired after the user disabled
subscription auto-renewal.

## Discussion

This `subtype` field is part of the `responseBodyV2DecodedPayload`, and
further describes an event of type `notificationType`. It’s present only for
specific version 2 notifications.

## See Also

### Server notifications version 2

Web Service Endpoint

`App Store Server Notifications V2`

Specify your secure server’s URL in App Store Connect to receive version 2
notifications.

`object responseBodyV2`

The response body the App Store sends in a version 2 server notification.

`object responseBodyV2DecodedPayload`

A decoded payload that contains the version 2 notification data.

`type notificationType`

The type that describes the in-app purchase or external purchase event for
which the App Store sends the version 2 notification.

Type

# version

A string that indicates the notification’s App Store Server Notifications
version number.

App Store Server Notifications 2.5+

    
    
    string version

## Discussion

The version string is `“2.0”`. It’s present in `responseBodyV2DecodedPayload`
for version 2 notifications.

For more information about App Store Server Notification changes, see App
Store Server Notifications changelog.

## See Also

### Response types

`type notificationType`

The type that describes the in-app purchase or external purchase event for
which the App Store sends the version 2 notification.

`type subtype`

A string that provides details about select notification types in version 2.

`type signedDate`

The UNIX time, in milliseconds, that the App Store signed the JSON Web
Signature data.

`type notificationUUID`

A unique identifier for the notification.

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

# notificationUUID

A unique identifier for the notification.

App Store Server Notifications 2.0+

    
    
    string notificationUUID

## Discussion

The App Store server assigns a unique identifer to each notification it sends.
Use this value to identify, and ignore, duplicate notifications.

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

`type signedDate`

The UNIX time, in milliseconds, that the App Store signed the JSON Web
Signature data.



