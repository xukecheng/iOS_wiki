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

