Article

# Handling Subscriptions Billing

Build logic around the date and time constraints of subscription products,
while planning for all scenarios where you control access to content.

## Overview

Apps that offer subscriptions have some unique behaviors and considerations.
Because subscriptions involve an element of time, your app must be able to
determine whether the subscription is currently active and determine the
subscription states for past dates. Your app must also react to new, renewed,
and lapsed subscriptions, and properly handle expired auto-renewable
subscriptions that may be in a billing retry state.

To validate changes in and identify the status of a subscription, you can use
the different values in the receipt, which provides details on app and in-app
purchases. For information about server-side receipt validation, see
Validating receipts with the App Store.

Note

Each subscription has a unique product identifier associated with a single
app. Apps with an iOS and a macOS version have separate products, with a
unique product identifier on each platform. You could let users who have a
subscription in an iOS app access the content from a macOS app, or vice versa,
but implementing that functionality is your responsibility. In order to
support cross-platform subscription products, you would need a system to
identify users and keep track of the content to which they subscribe. For more
information, see Offering a Subscription Across Multiple Apps.

There are two types of subscriptions you can offer in your app: _non-renewing_
and _auto-renewable_. Non-renewing subscriptions differ from auto-renewable
subscriptions in a few key ways. These differences give your app the
flexibility to implement the correct behavior for a non-renewing subscription,
as follows:

  * Your app is responsible for calculating the time period that the subscription is active and determining what content needs to be made available to the user.

  * Your app is responsible for detecting that a non-renewing subscription is approaching its expiration date and prompting the user to renew the subscription by purchasing the same product again.

  * Your app is responsible for making purchased subscriptions available across all the user’s devices and for letting users restore past purchases. For example, most subscriptions are provided by a server; your server would need some mechanism to identify users and associate subscription purchases with the user who purchased them.

The following sections provide guidance for handling auto-renewable
subscriptions. To quickly react to changes in users' auto-renewable
subscriptions, you can choose to receive status update notifications on your
server. Status update notifications inform you of real-time changes in a
user's subscription status and are only supported for auto-renewable
subscriptions. For more information on setting up and handling server
notifications, see Enabling App Store Server Notifications.

### Calculate a Subscription's Promotional Offer Status

You can set up promotional offers in App Store Connect to provide users with
free or discounted service for a subscription. All new and eligible
subscribers can redeem an introductory offer, and all lapsed and existing
subscribers can redeem a subscription offer. There are multiple types of
introductory and subscription offers, each with different billing cycles.
Customers who redeem a free trial introductory offer or a downgrade
subscription offer will not be billed for the subscription until the end of
the free trial period. For more information, see Implementing introductory
offers in your app and Implementing promotional offers in your app.

Check the `is_in_intro_offer_period` or `is_trial_period` field from each
receipt entry to validate whether the user redeemed an introductory offer at
the beginning of their subscription. You can use this information to
accurately present subscription products from the same subscription group at
the end of the introductory offer period for that user. Check the
`promotional_offer_id` field from each receipt entry to validate whether the
user redeemed a subscription offer. You can use this information to determine
eligibility for this user to redeem subscription offers in the future.

### Calculate a Subscription’s Active Period

Your app needs to determine which content the user has access to based on the
period of time their auto-renewable subscription is active. To provide the
customer access to the content to which they are entitled, keep a record of
the date that each piece of content is published. Read the
`original_purchase_date`, `purchase_date`, and `expires_date` field from each
receipt entry to determine the start and end dates of each subscription
period. The user has access to all content published between each subscription
start and end date in addition to the content that was initially unlocked when
the subscription was purchased.

For example, because purchasing a subscription always unlocks content, a user
who purchases a monthly subscription mid-month to a magazine that publishes a
new issue on the first day of every month gets access to two issues in their
first month of subscribing: the most recently published issue, which is
unlocked at the time that the subscription is purchased, and the issue you
publish on the subsequent first day of the month, which is unlocked at the
time you publish it.

Important

Don’t calculate the subscription period by adding a subscription duration to
the purchase date. That approach fails to take into account the free trial
period, the marketing opt-in period, and the content made available
immediately after the user purchased the subscription.

If the subscription lapsed, there will be multiple periods of time during
which the subscription was active, and there will be pieces of content
unlocked at the beginning of a subscription period. To identify lapses in a
subscription, compare the `expires_date` field from each receipt entry to the
`purchase_date` field of the previous receipt entry for all entries in the
receipt.

### Detect an Expiration or Renewal

The subscription renewal process begins in the 10 days before the expiration
date. During those 10 days, the App Store checks for any billing issues that
might delay or prevent the subscription from being automatically renewed, for
example, whether:

  * The customer’s payment method is active.

  * The product increased in price since the user bought the subscription.

  * The product is no longer available.

The App Store notifies users of any issue so that they can resolve it before
the subscription expires and avoid an interruption in their service.

During the 24-hour period before the subscription expires, the App Store
starts trying to renew it automatically. The App Store makes several attempts
to automatically renew the subscription over a period of time but eventually
stops if there are too many failed attempts.

### Handle Lapsed Subscriptions

The App Store renews the subscription slightly before it expires, to prevent
any lapse in the subscription. However, lapses are still possible. For
example, if the user’s payment information is no longer valid, the first
renewal attempt fails. Billing-related issues trigger the subscription to
enter a billing retry state where the App Store attempts to renew the
subscription for up to 60 days. You can check the `expiration_intent` and
`is_in_billing_retry_period` values to monitor the retry status of the
subscription. During this period, your app may optionally offer a grace period
to the user and show them a message in the app to update their payment
information. Additionally, your app can deep link customers to the payment
details page within App Store on their device by opening this URL

    
    
    https://apps.apple.com/account/billing
    

The user can also cancel their subscription by disabling auto-renew and
intentionally letting their subscription lapse. This action triggers the App
Store to send your server a status update notification of type
`DID_CHANGE_RENEWAL_STATUS`. Your server can parse the `auto_renew_status` and
the `auto_renew_status_change_date` to determine the current renewal status of
the subscription.

You can also check the `expiration_intent` field in the receipt to further
validate the reason for the subscription to lapse. Make sure your app’s
subscription logic can handle different values of `expiration_intent` along
with `expires_date` to show the appropriate message to the user.

### Detect a Refund

Users pay for a subscription when they purchase it, and they can receive a
refund by contacting Apple customer service. For example, if the user
accidentally buys the wrong product and requests a refund, customer support
can cancel the subscription and issue a full or partial refund. Customers may
cancel a subscription in the middle of a subscription period, but the
subscription remains paid through the end of the same period. Additionally,
users may also receive a refund when they upgrade their subscription to
another subscription product at a higher level in the same subscription group.

To identify whether a subscription has been refunded, look for the
`cancellation_date` field in the receipt. The App Store notifies your server
of refunds with a status update notification of type `CANCEL`, at which point
you can handle the refund. For example, if the user upgraded the subscription,
immediately unlock service for the higher level subscription product
purchased.

### Identify a Renewed Subscription After a Lapse

A user-initiated payment information update for an auto-renewable subscription
in the billing retry period triggers an automatic renewal attempt to succeed.
For this event, the App Store notifies your server with a notification of type
`RENEWAL` and a new receipt will be generated for the successful transaction.
You can look for a new value of the `expires_date` field to know the next
renewal date of the subscription.

StoreKit adds a new transaction for the renewal to the transaction queue on
the device. Your app can check the transaction queue on launch and handle the
renewal the same way as any other transaction. If your app is already running
when the subscription renews, the transaction observer is not called; your app
finds out about the renewal the next time the app launches.

### Detect Upgrades or Plan Changes

Users can manage their auto-renewable subscriptions in their App Store
settings on-device or within your app’s interface. For each subscription
purchased by the user, the App Store shows all the renewal options that the
subscription group offers. Users can easily change their service levels and
choose to upgrade, downgrade, or cross-grade as often as they like. Upgrades
of any duration or cross-grades with same durations go into effect
immediately. Downgrades of any duration or cross-grades with different
durations go into effect at the next renewal date.

You can check the receipt’s `auto_renew_product_id` field to learn about any
plan changes the user selected that will go into effect at the next renewal
date. Additionally, you can also use the notification of type
`DID_CHANGE_RENEWAL_PREF` to get notified for any user initiated plan changes
that will go into effect at the next renewal date.

### Manage Subscription Price Consent

When you increase the price of a subscription, the App Store informs the
affected subscribers with an email, push notification, and in-app price
consent sheet, and asks your subscribers to agree to the new price. In the
app, the system asks your delegate’s function
`paymentQueueShouldShowPriceConsent(_:)` whether to immediately display the
price consent sheet, or to delay displaying the sheet until later. For
example, you may want to delay showing the sheet if it would interrupt a
multistep user interaction, such as setting up a user account. Return `false`
in `paymentQueueShouldShowPriceConsent(_:)` to prevent the dialog from
displaying immediately.

To show the price consent sheet after a delay, call
`showPriceConsentIfNeeded()`, which shows the sheet only if the user hasn’t
responded to the price increase notifications.

If users don’t agree to the subscription price increase or take no action,
their subscription expires at the end of their current billing cycle. App
Store attempts to notify users in the app twice. For a notification schedule,
see Increase the price of an auto-renewable subscription.

Note

The price consent sheet appears only on devices running iOS. All affected
subscribers receive an email and push notification.

### Enable Users to Manage Subscriptions

Consider building auto-renewable subscription management UI in the app for
subscribers to easily move between different subscription levels in their
subscription group. Use the `subscriptionGroupIdentifier` property of
`SKProduct` to determine which products to display in the UI. For users who
wish to cancel their subscription, your app can open the following URL:

    
    
    https://apps.apple.com/account/subscriptions
    

Opening this URL launches iTunes or iTunes Store and displays the Manage
Subscriptions page where the user can upgrade, downgrade, or cancel their
subscription by disabling auto-renew. If you configure your backend server to
receive status update notifications, your server receives a
`DID_CHANGE_RENEWAL_STATUS` notification if the user cancels their
subscription.

## See Also

### Essentials

Enabling App Store Server Notifications

Configure your server and provide an HTTPS URL to receive notifications about
in-app purchase events and unreported external purchase tokens.

Offering a Subscription Across Multiple Apps

Support a single auto-renewable subscription across multiple apps.

Reducing Involuntary Subscriber Churn

Prevent unintentional loss of subscribers due to billing issues.

Article

# Enabling App Store Server Notifications

Configure your server and provide an HTTPS URL to receive notifications about
in-app purchase events and unreported external purchase tokens.

## Overview

App Store Server Notifications is a server-to-server service that sends real-
time notifications for in-app purchase events, and notifications for
unreported external purchase tokens. To enable notifications, set up an HTTPS
URL on your server, and configure settings in App Store Connect.

For information about parsing and interpreting notifications, see Receiving
App Store Server Notifications.

### Set up your server and App Store Connect settings

To receive server notifications from the App Store, your server must support
the Transport Layer Security (TLS) 1.2 protocol or later.

To enable App Store Server Notifications, follow these steps:

  1. Determine the HTTPS URL on your server to receive notifications for the production environment. 

  2. Optionally, determine the HTTPS URL on your server to receive notifications for the sandbox environment for testing notifications. You may use the same URL for both the production and the sandbox environments.

  3. App Store Connect gives you the choice of receiving version 2 or version 1 notifications for each environment. To choose version 2, set up your endpoint as App Store Server Notifications V2. 

  4. Configure your URL in App Store Connect. For more information, see Enter a URL for App Store Server Notifications. 

Important

If you specify a port in your URL, the port must be either `443` or greater
than or equal to `1024`. For example, the URL
`https://example.com:1234/notifications` specifies the port `1234`.

Configure your server to respond with HTTP status codes to indicate whether
the App Store server notification `POST` is successful. For more information,
see Responding to App Store Server Notifications.

For new implementations, use App Store Server Notifications V2. To transition
from using version 1 notifications to version 2, test version 2 notifications
in the sandbox environment before you update your production environment to
version 2.

For information about changes to App Store Server Notifications, see App Store
Server Notifications changelog.

### Configure an allow list

If your server requires IP addresses to be on an allow list, add the IP
address subnet `17.0.0.0/8` to allow your server to receive notifications from
the App Store server. This subnet applies to both the sandbox and the
production environments.

### Test your server setup

To determine whether your server is receiving notifications, call the Request
a Test Notification endpoint in the App Store Server API. This endpoint asks
the App Store server to send a notification with the `notificationType`
`TEST`. Use the `testNotificationToken` you receive to call the Get Test
Notification Status endpoint to learn how your server responds to the test
notification.

The App Store server sends the `TEST` notification in the version 2
notification format. However, it sends it to your server regardless of whether
you configure a version 1 or version 2 notification URL in App Store Connect.

## See Also

### Essentials

Handling Subscriptions Billing

Build logic around the date and time constraints of subscription products,
while planning for all scenarios where you control access to content.

Offering a Subscription Across Multiple Apps

Support a single auto-renewable subscription across multiple apps.

Reducing Involuntary Subscriber Churn

Prevent unintentional loss of subscribers due to billing issues.

Article

# Offering a Subscription Across Multiple Apps

Support a single auto-renewable subscription across multiple apps.

## Overview

You can offer customers auto-renewable subscription services that are
accessible through multiple apps across one or more operating systems.

To offer this functionality, your server must grant access to the subscription
content across all apps, despite the user having purchased the subscription
within a specific app. You can use a unified account management database along
with server-side receipt validation to validate a user’s purchase and handle
in-app transactions. By entitling subscription access from your server, you
can provide users the ability to access your subscription across multiple
apps.

### Create the Subscription for Each App

To get started, use App Store Connect to create a separate and equivalent
auto-renewable subscription for each app that offers the multi-app
subscription so that users can subscribe from any app. For design guidance,
see Human Interface Guidelines > In-App Purchase.

Tip

Use an app bundle to group apps that share auto-renewable subscriptions on the
same platform in a single App Store product page. An app bundle enables
customers to view and download apps in a single purchase.

The following image illustrates the steps for implementing a multi-app
subscription:

### Authenticate the User

When providing auto-renewable subscription access across multiple apps, you
must authenticate the user in a way that correlates across apps.
Authenticating users using a login allows you to determine if the user has
access to the content. To provide a consistent user experience, ensure that
the login process is similar across your apps.

To provide an easy and secure login, take advantage of Sign in with Apple.
Sign in with Apple allows you to identify a user across your apps, while
maintaining user privacy and protecting your app against fraud. You can store
and retrieve user account data across your apps and the user’s devices, and
use that data to unlock access appropriately.

### Check Billing Status

After authenticating the user, determine whether to grant access to the
content based on their transaction history in the receipt.

Check if the user has purchased any subscription products before showing a
subscription offer in the app. If there’s a subscription purchase from any
app, verify if the subscription is active by looking at the subscription
expiration date in the receipt.

Present users who don’t have an active subscription with the subscription for
purchase. Consider all potential billing scenarios within your account
database when determining eligibility and granting access to a user.

Important

If the user has purchased the subscription from an app, you must propagate the
purchase across all the apps that provide the subscription service. Failing to
persist the purchase to the other apps opens the possibility of a user paying
multiple times for the same service.

### Validate Subscription Status

A user’s subscription status can change any time. Validate the receipt and
check the latest subscription expiration date to maintain the billing status
for each user and reflect any changes.

Enabling App Store Server Notifications keeps your server aware of changes
made to a customer’s subscription status. Update your records to keep users'
subscription status and content current. The billing status must be accurate
in your account database to provide the expected user experience across all
apps.

### Enable Access to Purchased Content

After determining that the user should have access, you can enable access in
each app based on the subscription expiration date. The user can access the
subscription within any app that offers the same service. Repeat the previous
steps as necessary across each app or user’s session to unlock the
subscription.

## See Also

### Essentials

Handling Subscriptions Billing

Build logic around the date and time constraints of subscription products,
while planning for all scenarios where you control access to content.

Enabling App Store Server Notifications

Configure your server and provide an HTTPS URL to receive notifications about
in-app purchase events and unreported external purchase tokens.

Reducing Involuntary Subscriber Churn

Prevent unintentional loss of subscribers due to billing issues.

Article

# Reducing Involuntary Subscriber Churn

Prevent unintentional loss of subscribers due to billing issues.

## Overview

After acquiring new customers for your subscription service, you can minimize
subscriber loss, known as churn, by keeping them engaged as active
subscribers. However, irregular billing events can occur throughout the
lifecycle of a subscription that can impact your customer's subscription
status.

Involuntary churn occurs when users do not intend to leave your service but
their subscription fails to renew, usually due to billing issues. Because
involuntary churn is not related to customer satisfaction, consider creating a
user experience that avoids subscriber loss due to a failed renewal. For
business guidance on retaining subscribers, see Keeping Subscribers.

Billing-related issues trigger a subscription to automatically enter a billing
retry state, where the App Store attempts to recover the subscription. While
the App Store tries to recover these customers, you have the option to prompt
users to update their billing information or implement a grace period, or
both, to assist in recovery efforts. Enabling a grace period and providing
uninterrupted service provides a great customer experience, and avoids
interrupting your days of paid service and revenue loss if Apple is able to
recover the subscription within the grace period. For information on auto-
renewable subscription proceeds and days of paid service, see Net Revenue
After a Year.

### React to Billing Issues

If the customer's billing is invalid, the renewal fails and the user's
subscription enters a billing retry state, where the App Store attempts to
collect payment for up to 60 days. This billing retry lowers the rate of
involuntary churn and prevents the need to re-acquire subscribers if they
churned. If the user is recovered within the 60 days, the new billing date is
established on the date of recovery and subsequent renewal dates are based on
this new billing date, as shown in the figure below.

**Figure 1**  An example timeline for a monthly subscription that enters a
billing retry state

For example, if the user’s payment information is no longer valid, the first
renewal attempt fails. If you have server-to-server notifications enabled, you
receive a server notification of type `DID_FAIL_TO_RENEW`. You can check the
`expiration_intent` and `is_in_billing_retry_period` values in the
verifyReceipt response or `unified_receipt` object in the server notification
to validate the reason for the subscription to lapse and monitor the retry
status of the subscription. If the user is recovered during this period, you
receive a server notification of types `RENEWAL` and `DID_RECOVER` when the
retry is successful. For more information on server-to-server notifications,
see App Store Server Notifications.

Important

The `RENEWAL` notification type is scheduled for deprecation. Update any
existing code to rely on the identical `DID_RECOVER` notification type
instead.

Your app may optionally present in-app messaging that informs users they can
avoid losing access to paid service by taking action and resolving their
billing error. If you choose to prompt the user, ensure your app's
subscription logic can handle different values of `expiration_intent` along
with `expires_date_ms`, to show the appropriate message. An invalid payment
method could be due to a number of things, such as a low balance on a stored
value card or an expired credit card. Your app should be ready to react
immediately to a billing information update. Your app can deep link customers
to the Manage Payments page on their account settings by opening this URL:

    
    
    https://apps.apple.com/account/billing
    

Note

This URL is only supported for iOS and macOS.

For more general guidance on handling subscriptions that enter a billing retry
state, see WWDC 2018 > Engineering Subscriptions. You can also agree to
provide a grace period for subscribers in a billing retry state. Billing error
recoveries made within the set grace period automatically recover subscribers
onto their current billing cycle, also providing revenue continuity.

### Enable Billing Grace Period

To avoid interrupting days of paid service, you can enable Billing Grace
Period in App Store Connect, which allows subscribers to retain full access to
your app’s paid content while Apple attempts to collect payment. For guidance
on opting in to enable Billing Grace Period for your app, see Enable Billing
Grace Period for Auto-Renewable Subscriptions.

Billing Grace Period is applied at the time of a billing error when it's
enabled for subscriptions in the app, and cannot be altered once assigned to a
user. Grace period durations are dependent on the subscription period length
as follows:

  * 6 days for a weekly subscription

  * 16 days for monthly and longer subscriptions

If you choose to enable Billing Grace Period, ensure that you provide full
service for the subscription throughout the grace period. You can check the
`grace_period_expires_date_ms` field in the
`responseBody.Pending_renewal_info` array of the `verifyReceipt` response or
`unified_receipt` object in the server notification to determine the end of
this grace period duration. For more information on reducing involuntary churn
using a grace period, see WWDC 2019 > In-App Purchases and Using Server-to-
Server Notifications.

If the user is recovered within this grace period, neither the subscriber's
days of paid service, nor your revenue for auto-renewable subscriptions will
be interrupted. Billing error recoveries made after the grace period expires,
but within the overall billing retry period, will maintain existing behavior
and renew on the recovery date, starting a new billing cycle. Payment for the
provided full service during the grace period would not be collected.

**Figure 2**  Example timelines for a monthly subscription that enters a
billing retry state, in an app with Billing Grace Period enabled

When implementing Billing Grace Period, use the verifyReceipt JSON response
and server-to-server notifications. Consider using `expiration_intent`,
`is_in_billing_retry_period`, and `grace_period_expires_date_ms` of the
`unified_receipt` object in the server notifications of type `RENEWAL` and
`DID_RECOVER` to identify whether the subscription is in a grace period.

The `expiration_intent` value can tell you if a subscription renewal failed
due to a billing error, or simply because the user chose to cancel service.
You can also see if the App Store is actively trying to recover a subscription
by looking for an active `is_in_billing_retry_period flag`.

Consider all scenarios for subscription recovery:

  * If the subscription renews before the time specified in `grace_period_expires_date_ms`, the `grace_period_expires_date` fields are removed along with the `is_in_billing_retry_period` indicator. You can look up a past transaction’s `purchase_date_ms` and `expires_date_ms` values to determine if a user’s subscription renewed after a lapse.

  * If the subscription renews after the time specified in `grace_period_expires_date_ms` while still in the billing retry state, the `grace_period_expires_date` fields are removed along with the `is_in_billing_retry_period` indicator. You can use the `expires_date_ms` value for a past transaction to determine the lapse period. 

  * If attempts to renew the subscription fail, the `grace_period_expires_date` fields persist along with a value of `0` for the `auto_renew_status` and `is_in_billing_retry_period` indicators.

### Restore Service

When users update their payment information, the App Store immediately
attempts to renew the payment. Once the App Store successfully bills the
customer in a billing retry state, the App Store notifies your server with
notifications of types `RENEWAL` and `DID_RECOVER`, and a new receipt is
generated for the successful transaction. A new value appears in the
`expires_date_ms` field in the app transaction receipt, based on the date of
recovery, to mark the next renewal date of the subscription.

StoreKit adds a new transaction for the renewal to the transaction queue on
the device. Your app can check the transaction queue on launch and handle the
renewal the same way as any other transaction. If your app is already running
when the subscription renews, the transaction observer is not called; your app
finds out about the renewal the next time the app launches. Restore service
once the subscription is renewed if needed.

## See Also

### Essentials

Handling Subscriptions Billing

Build logic around the date and time constraints of subscription products,
while planning for all scenarios where you control access to content.

Enabling App Store Server Notifications

Configure your server and provide an HTTPS URL to receive notifications about
in-app purchase events and unreported external purchase tokens.

Offering a Subscription Across Multiple Apps

Support a single auto-renewable subscription across multiple apps.

Article

# Implementing introductory offers in your app

Offer introductory pricing for auto-renewable subscriptions to eligible users.

## Overview

Apps with auto-renewable subscriptions can offer a discounted introductory
price, including a free trial, to eligible users. You can make introductory
offers to customers who haven’t previously received an introductory offer for
the given product, or for any products in the same subscription group.

Start by setting up introductory offers in App Store Connect. Then, in your
app, determine if the user is eligible to receive an introductory offer. When
the app queries the App Store for a list of available products, display the
introductory pricing if the user is eligible to receive them.

### Set Up Introductory Offers

Before you can display introductory offers in your app, you must first
configure the offers in App Store Connect. For more information, see Set an
introductory offer for an auto-renewable subscription.

Choose from one of three types of introductory offers, which differ in their
mode of payment. All subscriptions renew at the regular price when the
introductory period is over. The offer types are “pay as you go”, “pay up
front”, and “free trial”.

#### Pay As You Go

The `SKProductDiscount.PaymentMode.payAsYouGo` value represents the pay as you
go offer type. In this introductory offer, new subscribers pay an introductory
price each billing period for a specific duration (for example, $1.99 per
month for 3 months).

#### Pay Up Front

The `SKProductDiscount.PaymentMode.payUpFront` value represents the pay up
front offer type. In this introductory offer, new subscribers pay a one-time
introductory price for a specific duration (for example, $1.99 for 2 months).

#### Free Trial

The `SKProductDiscount.PaymentMode.freeTrial` value represents a free trial
offer type. In this introductory offer, new subscribers access content for
free for a specified duration. Subscriptions begin immediately, but
subscribers won’t be billed until the free trial period is over.

### Determine Eligibility

To determine if a user is eligible for an introductory offer, check their
receipt:

  1. Validate the receipt as described in Validating receipts with the App Store.

  2. In the receipt, check the values of the `is_trial_period` and the `is_in_intro_offer_period` for all in-app purchase transactions. If either of these fields are `true` for a given subscription, the user is not eligible for an introductory offer on that subscription product or any other products within the same subscription group. Use `subscription_group_identifier` in the `responseBody.Pending_renewal_info` array to determine the subscription group to which the subscription belongs. 

Typically, you check the user's eligibility from your server. Determine
eligibility early—for example, on the first launch of the app, if possible.

Based on the receipt, you will find that new and returning customers are
eligible for introductory offers, including free trials:

  * New subscribers are always eligible. 

  * Lapsed subscribers who renew are eligible if they haven't previously used an introductory offer for the given product (or any product within the same subscription group).

Existing subscribers are not eligible for an introductory offer for any
product within the same subscription group. For example, customers are not
eligible if they are upgrading, downgrading, or crossgrading their
subscription from another product, regardless of whether they consumed an
introductory offer in the past.

### Display the Introductory Offer

Once you determine the user is eligible for an introductory offer, query the
App Store for available products, and present the offer to the user:

  1. Retrieve localized information from the App Store about a specified list of subscription products using the `SKProductsRequest` class. Products that have an available discount defined in App Store Connect always include an `introductoryPrice` object. 

  2. Use the properties in the `introductoryPrice` object to display the discounted price for the subscription. Based on the type of the introductory offer (represented by `SKProductDiscount.PaymentMode`), display a UI that describes the offer accordingly.

For design guidance, see Human Interface Guidelines > In-App Purchase.

## See Also

### Introductory offers

Testing introductory offers

Test your introductory pricing in a variety of user scenarios.

`class SKProductDiscount`

The details of an introductory offer or a promotional offer for an auto-
renewable subscription.

### Related Documentation

Receipt Validation Programming Guide

Article

# Testing introductory offers

Test your introductory pricing in a variety of user scenarios.

## Overview

To test introductory offers, verify that users see the same subscription and
introductory offer prices in your app as they do in the App Store. As part of
your test, make sure your app presents introductory offers only to users that
are eligible for them.

To test introductory offers:

  1. Configure test accounts, as described in Create a sandbox tester account. Create a variety of accounts that are eligible or ineligible for offers.

  2. Initiate in-app purchases from within the app for each test user.

  3. Verify that the user experience and pricing information dynamically represent the accurate price of your subscription.

Introductory offers are only offered once, but when testing your app, you can
reset the status of the test account to allow you to redeem an introductory
offer more than once. To reset offer eligibility for the sandbox account:

  1. On the test iOS device, open Settings > Apple ID > Media & Purchases (or iTunes & App Store for iOS 13 and earlier). Under the Sandbox Account section, tap your highlighted Sandbox Apple ID then tap Manage to open the sandbox Subscription Management page.

  2. Tap the expired subscription you want to reactivate. The subscription products that appear are those you configured in App Store Connect under the same subscription group.

  3. If the test account used an introductory offer, then the system diplays a Reset Eligibility button that lets you reset and redeem another introductory offer.

## See Also

### Introductory offers

Implementing introductory offers in your app

Offer introductory pricing for auto-renewable subscriptions to eligible users.

`class SKProductDiscount`

The details of an introductory offer or a promotional offer for an auto-
renewable subscription.

Article

# Setting up promotional offers

Generate a key and configure offers for auto-renewable subscriptions in App
Store Connect.

## Overview

You can offer a discounted or free period of service for auto-renewable
subscription products on macOS, iOS, and tvOS using promotional offers.
Limited-time, discounted promotional offers can be effective in winning back
lapsed subscribers or retaining current subscribers.

Before you can provide promotional offers in your app, you must first generate
a subscription key and set up the offers in your App Store Connect account.

Note

If your goal is to attract new users, use introductory offers and promote the
in-app purchase on the App Store. Redeeming an introductory offer doesn’t
affect a user’s eligibility for a promotional offer. For more information, see
Implementing introductory offers in your app.

### Generate a Private Key

You generate a private key in App Store Connect that you use on your server to
sign promotional offers. This key allows Apple to authenticate and validate
subscription requests.

Keys don’t expire, and you can use them with any apps in your account. To get
started, generate a subscriptions access key in App Store Connect.

#### Download and Store the Private Key

Once you’ve generated your subscription key, you’re given the opportunity to
download the private half of the key. You can only download this key one time.

The keys are provided in base64-encoded PEM format. Apple doesn’t keep a copy
of the private key.

Important

Store your private subscription key in a safe place. You should never share
your keys, store keys in a code repository, or include keys in apps or client-
side code.

If the key becomes lost or compromised, revoke it immediately and update your
promotional offers. See Revoke a subscription key for more information.

### Configure Promotional Offers

You configure promotional offers in App Store Connect, providing details such
as a reference name, payment mode, duration, and price. To configure your
offer, see Set up promotional offers for auto-renewable subscriptions. You can
have up to 10 promotional offers active at any given time per subscription.

For business guidance on using promotional offers, see Auto-renewable
Subscriptions > Providing Subscription Offers.

## See Also

### Promotional offers

Implementing promotional offers in your app

Offer discounted pricing for auto-renewable subscription products to eligible
subscribers.

Generating a signature for promotional offers

Create a signature to validate a promotional offer using your private key.

Generating a Promotional Offer Signature on the Server

Generate a signature using your private key and lightweight cryptography
libraries.

`class SKPaymentDiscount`

The signed discount to apply to a payment.

Article

# Implementing promotional offers in your app

Offer discounted pricing for auto-renewable subscription products to eligible
subscribers.

## Overview

Promotional offers can be effective in winning back lapsed subscribers or
retaining current subscribers. You can provide lapsed or current subscribers a
limited-time offer of a discounted or free period of service for auto-
renewable subscriptions on macOS, iOS, and tvOS. To implement the offers,
first complete the setup on App Store Connect, including generating a private
key. See Setting up promotional offers for more details.

You decide the criteria for which subscribers qualify for an offer. In your
app, the details of the offers you set up in App Store Connect appear in the
`discounts` array in `SKProduct`. To indicate the offer you want to give to a
user, include a signed `paymentDiscount` in the `SKMutablePayment` object.

For business guidance on using promotional offers, see Auto-renewable
Subscriptions > Providing Subscription Offers.

Note

If your goal is to attract new users, you can use introductory offers and
promote the in-app purchase on the App Store. Users are eligible to receive
only one introductory offer, but redeeming an introductory offer doesn’t
affect their eligibility for a promotional offer. For more information on
introductory offers, see Implementing introductory offers in your app.

### Prepare Your Offer

To present a promotional offer, first determine the subscriber’s eligibility,
get the product details from the App Store, and generate a signature on your
server.

**Figure 1**  Steps for determining a user's eligibility and preparing the
offer

#### Determine Eligibility

There are two aspects to determining a user’s eligibility for promotional
offers:

  * The App Store deems all customers with an existing or expired subscription in the app eligible to redeem a promotional offer. You can check whether the receipt contains any existing or expired subscription purchases to identify these current or lapsed subscribers.

  * You determine any additional eligibility criteria for a specific promotional offer. Eligibility can be contingent on a wide range of business logic determined by your business needs.

Consider using the App Store server notification `DID_CHANGE_RENEWAL_STATUS`
to determine eligibility. This notification is triggered by changes in a
subscription’s auto-renew status. For example, you receive a notification when
a subscriber disables auto-renew in Manage Subscriptions or contacts AppleCare
to cancel their subscription. For more information on server notifications,
see App Store Server Notifications. Your server can notify your app if the
user is eligible for an offer so the app can present it to the customer.

Note

Customers can redeem promotional offers only on devices running iOS 12.2 and
later, macOS 10.14.4 and later, and tvOS 12.2 and later. Consider providing
messaging prompting your customer to update their OS if they try to redeem a
promotional offer in your app on a device running an older OS version.

Consider also implementing DeviceCheck to keep track of devices that have
previously redeemed offers. `TwoBitKit` allows you to maintain user privacy
while defining parameters you use to determine eligibility.

#### Request Product Details

Once you determine that the subscriber is eligible for an offer, the next step
is requesting the product details, including offers, from the App Store. To
fetch the details, use `SKProductsRequest` with the subscription’s product
identifier.

In response, the App Store returns the localized information in `SKProduct`.
The `discounts` array of `SKProduct` contains all promotional offers you
configured in App Store Connect for that product. The `SKProductDiscount`
object contains offer details including the localized price.

You determine which offer from the `discounts` array to present to the user.

#### Create a Signature

A signature is a unique string that your server generates using specified
parameters and your private key. You include it in the `signature` parameter
of `SKPaymentDiscount`, and the App Store uses it to validate the promotional
offer. The signature is time sensitive, unique per offer, and redeemable only
once.

To generate the signature, send a secure request to your server. The server
will need to know the `applicationUsername`, `productIdentifier`, and
`identifier`. Your app should supply these parameters in the request if the
server doesn’t already know them. See Generating a signature for promotional
offers for more information.

Your server should respond with the signature string and the additional values
it used to generate the signature: a `nonce`, `timestamp`, and the
`keyIdentifier`. Use these values to complete the parameters in the
`SKPaymentDiscount` object nested in the `SKMutablePayment` object
representing the offer. If the App Store determines that the signature isn’t a
match for the parameters in the payment, the transaction fails.

Tip

To minimize latency, consider generating the signature when you display the
offer.

The following code example shows how to request a signature from your server
and prepare the discount offer.

#### Present Your Offer

You can present offers to users through various channels, such as email, but
they must interact with the offer inside your app’s UI. Display the offer in
your app at the time you choose, using the pricing and terms from the
`SKProductDiscount` object. By using the details from this object, you ensure
that the offer displayed to the user accurately reflects the offer you intend
to give. For design guidance, see Auto-Renewable Subscriptions > Clearly
Describing Subscriptions.

Present offers to eligible subscribers only, to avoid misleading or confusing
users.

### Complete the Transaction

After a user chooses to buy the promotional offer, submit the payment request,
verify the receipt, and unlock the offer.

**Figure 2**  Steps for creating a payment request with a signed offer,
verifying the receipt, and unlocking the service

#### Create a Payment Request

When the user initiates a buy of the offer in the app, send an
`SKMutablePayment` to the App Store with the signed offer. Create an
`SKPaymentDiscount` object that includes the signature you generated and its
`identifier`, `keyIdentifier`, `nonce` (one-time use), and `timestamp`
parameters. Add this object as the `paymentDiscount` property to the
`SKMutablePayment` object.

Include in the `SKMutablePayment` object the same `applicationUsername`, often
a unique hash of the username, that the signature contains. Add the
`SKMutablePayment` object to the queue.

#### Notify the User of the Transaction State

Once the App Store validates the offer, it processes your payment request and
generates an `SKPaymentTransaction`. Your app uses it to validate the
transaction and unlock content accordingly.

Handle the transaction state of the payment request and notify the customer as
needed. If the transaction is successful, the App Store automatically updates
the app receipt with the transaction in the
`SKPaymentTransactionState.purchased` state. Base64-encode the receipt on-
device and securely send the receipt data to your server.

Note

If the transaction fails with a state of `SKPaymentTransactionState.failed`,
you must generate a new signature and a new payment request for any further
attempts to purchase the offer.

#### Verify the Receipt

As you do for all purchases, verify the receipt with the App Store by calling
the verifyReceipt endpoint from your server. The App Store sends a JSON
response containing information about the user’s purchase. See Validating
Receipts With the App Store for more information.

When a subscriber redeems an offer, the receipt contains a
`promotional_offer_id` in the purchase transaction. This receipt field is a
string containing the offer ID that you configured in App Store Connect. You
can look at past transactions in the receipt to identify the offers the
customer redeemed.

#### Unlock the Service

After validating that the user has purchased the subscription product, unlock
the subscription service in the app for the user. Update the customer’s
eligibility criteria for offers, as needed.

When a customer redeems a promotional offer, the offer period starts at the
next billing event.

  * For upgrades or crossgrades to a different subscription with the same duration, the promotional offer triggers a billing event and goes into effect immediately.

  * For downgrades or crossgrades to a different subscription with different durations, the promotional offer period goes into effect at the next renewal date.

  * For the same subscription in an introductory offer, this promotional offer period goes into effect at the next scheduled billing event.

Once the offer period concludes, a promotional offer auto-renews at the
standard price.

A user can redeem and have active only one promotional offer at a time. If the
user accepts another offer before a current offer ends, the current offer is
canceled in the following billing event and the new offer takes effect.

## See Also

### Promotional offers

Setting up promotional offers

Generate a key and configure offers for auto-renewable subscriptions in App
Store Connect.

Generating a signature for promotional offers

Create a signature to validate a promotional offer using your private key.

Generating a Promotional Offer Signature on the Server

Generate a signature using your private key and lightweight cryptography
libraries.

`class SKPaymentDiscount`

The signed discount to apply to a payment.

Article

# Generating a signature for promotional offers

Create a signature to validate a promotional offer using your private key.

## Overview

Before you can create a signature on your server, you need to complete the
one-time setup to generate a private key in App Store Connect, as Setting up
promotional offers describes. Always use a secure connection when sending
data, including the signature, between your app and server. For more
information on ensuring your data’s security, see Preventing Insecure Network
Connections.

To create the signature, you use parameters that identify the product and the
offer, parameters your server generates, and your private key. To generate the
signature, you combine the required parameters, then sign and encode the
resulting string.

### Combine the parameters

In the first step of generating the signature, you need the following
parameters, most of which you also supply for `SKPaymentDiscount`:

`appBundleID`

    

The app bundle identifier.

`keyIdentifier`

    

A string that identifies the private key you use to generate the signature.
You can find this identifier in App Store Connect Users and Access > Keys in
the Key ID column for the subscription key you generate.

`productIdentifier`

    

The subscription product identifier, `productIdentifier`. The app can provide
this value.

`offerIdentifier`

    

The subscription discount identifier, `identifier`. The app can provide this
value.

`applicationUsername or appAccountToken`

    

An optional string value that you define; may be an empty string. If your app
uses `applicationUsername`, provide `applicationUsername`. If your app uses
`appAccountToken`, provide `appAccountToken`. The string representation of the
`appAccountToken` must be lowercase.

`nonce`

    

A one-time `UUID` value that your server generates. Generate a new `nonce` for
every signature. The string representation of the `nonce` you use in the
signature must be lowercase.

`timestamp`

    

A timestamp your server generates in UNIX time format, in milliseconds. The
timestamp keeps the offer active for 24 hours.

Important

Use lowercase for the string representation of the `nonce` and the
`appAccountToken`.

Combine the parameters into a UTF-8 string with an invisible separator
(`'\u2063'`) between them in the same order as the following example:

    
    
    appBundleId + '\u2063' + keyIdentifier + '\u2063' + productIdentifier + '\u2063' + offerIdentifier + '\u2063' + appAccountToken + '\u2063' + nonce + '\u2063' + timestamp
    

If you provide `applicationUsername` instead of `appAccountToken`, replace it
accordingly in the UTF-8 string above.

### Sign the combined string

Sign the combined UTF-8 string with the following key and algorithm:

  * Your PKCS #8 private key (downloaded from App Store Connect) that corresponds to the `keyIdentifier` in the UTF-8 string

  * The Elliptic Curve Digital Signature Algorithm (ECDSA) with a SHA-256 hash

The result is a Digital Encoding Rules (DER)-formatted binary value, which is
the signature.

### Validate locally and encode the signature

Consider validating your signatures locally to ensure your signing process
works correctly. You can create a public key derivative of your private key to
test against. One way to create this key is by running the `openSSL` command
from the terminal app, as the example below shows:

    
    
    openssl ec -in {downloaded_private_key} -pubout -out public_key.pem
    

Use Base64 encoding for the binary signature you generated to obtain the final
signature string to send to the App Store for validation. The signature string
resembles the following:

    
    
    MEQCIEQlmZRNfYzKBSE8QnhLTIHZZZWCFgZpRqRxHss65KoFAiAJgJKjdrWdkLUOCCjuEx2RmFS7daRzSVZRVZ8RyMyUXg==
    

### Respond to the request

Respond to the app’s request for the signature over a secure connection,
providing the encoded signature string, the `nonce`, the `timestamp`, and the
`keyIdentifier`. Note that each payload, signature, and `nonce` is only valid
for one buy request, even if the buy fails.

See Create a Signature for information about the app’s request and how it uses
the signature.

## See Also

### Promotional offers

Setting up promotional offers

Generate a key and configure offers for auto-renewable subscriptions in App
Store Connect.

Implementing promotional offers in your app

Offer discounted pricing for auto-renewable subscription products to eligible
subscribers.

Generating a Promotional Offer Signature on the Server

Generate a signature using your private key and lightweight cryptography
libraries.

`class SKPaymentDiscount`

The signed discount to apply to a payment.

Article

# Implementing offer codes in your app

Provide subscription service for customers who redeem offer codes through the
App Store or within your app.

## Overview

To help you acquire, retain, and win back subscribers, you can use offer
codes.

Note

If your app uses the In-App Purchase API and manages transactions using the
`Transaction` class, see Supporting subscription offer codes in your app
instead, which describes an app’s transaction processing using `Transaction`
rather than receipts.

Offer codes are alphanumeric codes that provide subscriptions at a discount or
for free for a specific duration. Configure the offers and create offer codes
in App Store Connect, and distribute them to your customers. Customers can
redeem offer codes in the App Store, using offer code redemption URLs, or in
your app if you’ve implemented one of the following APIs:

  * `offerCodeRedemption(isPresented:onCompletion:)` or `presentOfferCodeRedeemSheet(in:)`, which are available in iOS 16 and later and iPadOS 16 and later

  * `presentCodeRedemptionSheet()`, which is available in iOS 14 and later and iPadOS 14 and later.

When customers redeem a valid offer code, your app receives a successful
transaction on the payment queue, and you receive a server notification if
you’ve enabled App Store Server Notifications. The receipt contains an
`offer_code_ref_name` field that identifies the offer.

For information on subscription offer types and choosing the offer type to
suit your business needs, see Providing subscription offers.

### Set up offer codes in App Store Connect

Configure offers and manage your offer codes in App Store Connect. You can
have up to 10 active offers per subscription, and create codes for a maximum
of 1,000,000 redemptions per app, per quarter. There are two types of offer
codes: one-time use codes, and custom codes. The offer code redemption APIs
support both.

Download the offer codes from App Store Connect to distribute them to your
customers. For more information on creating and distributing offer codes, and
to learn which type of offer code may work for your campaign, see Set up offer
codes.

### Redeem offer codes in your app

To display the system sheet for customers to redeem offer codes within your
app, call one of the redemption APIs, depending on your app’s UI
implementation:

  * Call `offerCodeRedemption(isPresented:onCompletion:)` if your app uses SwiftUI.

  * Call `presentOfferCodeRedeemSheet(in:)` if your app uses UIKit.

  * Call `presentCodeRedemptionSheet()` for apps running on devices prior to iOS 16 and iPadOS 16.

The redemption sheet takes care of the redemption flow, including alerting
users about invalid entries, as appropriate. Invalid entries may include, for
example, expired offer codes, invalid codes, or codes that would result in a
subscription downgrade.

Including the redemption sheet in your app is recommended, but optional. For
more guidance on supporting offer code redemption within your app, see Human
Interface Guidelines > In-app purchase.

### Support offer codes redeemed outside your app

Customers may redeem subscription offer codes outside your app. If a customer
doesn’t have your app, the App Store prompts them to download it as part of
the redemption flow.

To handle offer codes — and other transactions that can occur outside of your
app – you need to set up a transaction observer at app launch. For more
information on this best practice, see Setting up the transaction observer for
the payment queue. Check that your app’s user-onboarding experience verifies
the receipt and provides subscription service. Update your records if you keep
a backend system to manage your subscribers.

### Identify subscriptions purchased with offer codes, in receipts

When a customer successfully redeems a subscription offer code, the receipt
contains a transaction with the field: `offer_code_ref_name`. This field’s
value is the offer reference name that you configured in App Store Connect.
The field appears in the `responseBody.Latest_receipt_info` and
`responseBody.Pending_renewal_info` objects for receipts, and in the
`unified_receipt.Latest_receipt_info` and
`unified_receipt.Pending_renewal_info` objects for server notifications.

### Provide subscription service to existing and new customers

When an existing customer redeems an offer code, your app receives a
transaction on the payment queue (`paymentQueue(_:updatedTransactions:)` in
the `SKPaymentTransactionState.purchased` state. This flow is the same as a
typical subscription purchase flow, but the receipt contains the offer code
reference. Your app follows these steps:

  1. Validates the receipt. For more information, see Validating receipts with the App Store.

  2. Looks for the `offer_code_ref_name` field in the receipt to determine if the subscription is from an offer code.

  3. Provides the subscription service based on the offer.

  4. Calls `finishTransaction(_:)`.

When you acquire new customers with an offer code, they open your app for the
first time already having a subscription. In addition to providing
subscription service, you may need to update your backend system’s records.
Your app follows these steps:

  1. When the app first launches, validate the receipt.

  2. In the receipt, look for a transaction with the `offer_code_ref_name` field to determine if the subscription is from an offer code.

  3. Provide the subscription service based on the offer.

  4. Guide the customer through your new-user experience as needed. Update your backend system’s records.

  5. Call `finishTransaction(_:)`.

