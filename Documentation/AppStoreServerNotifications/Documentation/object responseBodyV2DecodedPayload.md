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

