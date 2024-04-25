Article

# Supporting promoted in-app purchases in your app

Display promoted in-app purchases on your product page and handle purchases
that users initiate on the App Store.

## Overview

With iOS, you can promote in-app purchases so users can browse them directly
on the App Store. Promoted in-app purchases display on your product page,
appear in search results, and may be featured on an appropriate tab on the App
Store. Users can start a purchase on the App Store, which takes them into your
app to continue the transaction.

If your app isn’t installed when the user selects to purchase the in-app
product, the App Store automatically downloads the app or prompts the user to
purchase it. If the installed version of your app is an older version that
doesn’t support in-app purchase promotions, the App Store prompts the user to
upgrade the app.

Promoting in-app purchases requires two steps:

  1. In your app, starting in iOS 16.4, implement `PurchaseIntent` to complete the purchase users initiate on the App Store. To support this feature in apps that run in iOS 11–16.3, see Promoting in-app purchases.

  2. In App Store Connect, configure promoted in-app purchases. For more information, see Promote in-app purchases.

Important

To enable promoted in-app purchases, your app needs to use either
`PurchaseIntent` (starting in iOS 16.4) or
`paymentQueue(_:shouldAddStorePayment:for:)` (starting in iOS 11). Don’t use
both at the same time. If necessary, use conditional compilation to identify
the OS version the app is running in. For more information, see Running code
on a specific platform or OS version.

You can optionally customize which promoted in-app purchases a users sees on a
specific device using the `Product.PromotionInfo` API. Using
`Product.PromotionInfo` isn’t required for your promoted in-app purchases to
appear on the App Store.

For marketing guidance on this feature, see Promoting Your In-App Purchases.

To test promoted in-app purchases, see Testing promoted in-app purchases.

Note

Promoted in-app purchases aren’t available to compatible iPad or iPhone apps
running in visionOS.

### Set up promoted in-app purchases using App Store Connect

In App Store Connect, set up promoted in-app purchases by uploading
promotional images. Use the App Store Promotions feature in App Store Connect
to manage their default order and visibility. For more information about the
setup, see Promote in-app purchases.

### Complete the purchase in your app

When users initiate an in-app purchase on the App Store, StoreKit
automatically opens your app and sends the product information in the
`intents` asynchronous sequence of `PurchaseIntent`. Your app needs to
complete the purchase transaction and perform any related actions that are
specific to it.

To complete the transaction, call the `purchase(options:)` method on the
`product` of the `PurchaseIntent`. Follow the same workflow your app uses for
any in-app purchase, such as unlocking the purchased content and finishing the
transaction (`finish()`).

The following code example listens for purchase intents from the App Store. It
receives a `Product` object when the user taps a promoted in-app purchase on
the App Store, and performs its purchase workflow.

### Defer or cancel the purchase

In some cases, your app may need to defer or cancel the purchase transaction.
For example, you may need to defer the transaction if the user is in the
middle of onboarding, and complete it after they finish. Or, you may need to
cancel the transaction if the user has already unlocked the product they’re
trying to buy.

To defer the transaction, store the purchase intent and process it later after
the user finishes onboarding or other actions that require deferring.

To cancel the transaction, don’t call `purchase(options:)`. Instead, provide
feedback to the user. Although this step is optional, if you don’t provide
feedback, the app’s lack of action after the user initiates the purchase on
the App Store may seem like a bug.

### Customize promoted product order and visibility on a device

To customize promoted in-app purchases on a device, you can override their
default order and visibility using `Product.PromotionInfo`. Use it to show
only promotions that are relevant to your user, based on their experience with
your app, or based on their previous purchases. For example, suppose a game
has in-app purchases to promote for each game level. You can show only the
promoted products for the user’s game level, and hide those they already
purchased.

To control whether a promoted in-app purchase appears in the App Store on the
device, use any of these methods:

  * Add or remove it from the list. Set the product order by calling `updateAll(_:)` or `updateProductOrder(byID:)`. Leave out the products you don’t want to display.

  * Set its visibility. Show or hide the product by setting its `visibility` value and calling `update()` or `updateAll(_:)`, or call `updateProductVisibility(_:for:)`. 

These overrides are specific to the device, and take effect after the user
launches the app at least once.

The following code example uses an array of product identifiers to set their
order. It calls `currentOrder` to get the `Product.PromotionInfo` objects, and
sets their visibility directly. It then calls `updateAll(_:)` to save the
changes.

The following code example hides a promoted product after the user purchases
it:

### Control a promotion's visibility from App Store Connect

To control a promotion’s visibility from App Store Connect, set its
`visibility` value in the app to the default of
`Product.PromotionInfo.Visibility.appStoreConnectDefault`. Products with this
value are visible or hidden based on the setting you configure in App Store
Connect. For more information about using App Store Connect, see Promote in-
app purchases.

For example, to promote a product on a holiday for all users, ensure the app
sets the product’s visibility to
`Product.PromotionInfo.Visibility.appStoreConnectDefault`. In App Store
Connect, start with its visibility set as hidden. On the holiday, use App
Store Connect to manually change the product to be visible. The promoted
product becomes visible in the App Store for all users automatically.

### Cancel overrides

To reset changes your app makes to the promoted products' order and
visibility, call the `updateAll(_:)` or `updateProductOrder(byID:)` methods
with an empty array. This cancels the overrides so the user can see the
promoted in-app purchases in their default order.

Call `currentOrder` to get a list of your overrides. If the list is empty, the
device displays promoted in-app purchases in their default order.

## See Also

### Promoted in-app purchases

`struct PurchaseIntent`

An instance that emits purchase intents, which indicates that the customer
initiated a promoted in-app purchase on the App Store for your app to
complete.

`struct Product.PromotionInfo`

Information about a promoted in-app purchase that customizes its order and
visibility on the device.

Testing promoted in-app purchases

Test your in-app purchases before making your app available in the App Store.

Article

# Testing promoted in-app purchases

Test your in-app purchases before making your app available in the App Store.

## Overview

Users can buy promoted in-app purchases from the App Store, but you need to
test this flow before making your product publicly available. Apple provides a
system URL that triggers your app using the `itms-services://` protocol, so
you can test in-app purchases before they’re available in the App Store.

**Protocol**| `itms-services://`  
---|---  
**Parameter** `action`| `purchaseIntent`  
**Parameter** `bundleId`| The bundle ID for your app; for
example:`com.example.app`  
**Parameter** `productIdentifier`| The in-app purchase product name you want
to test; for example:`product_name`  
  
The resulting URL looks like this:

`itms-
services://?action=purchaseIntent&bundleId=com.example.app&productIdentifier=product_name`

Send this URL to yourself in an email or iMessage, and open it from your
device. You’ll know the test is running when your app opens automatically. You
can then test how your app handles the promoted in-app purchase.

## See Also

### Promoted in-app purchases

Supporting promoted in-app purchases in your app

Display promoted in-app purchases on your product page and handle purchases
that users initiate on the App Store.

`struct PurchaseIntent`

An instance that emits purchase intents, which indicates that the customer
initiated a promoted in-app purchase on the App Store for your app to
complete.

`struct Product.PromotionInfo`

Information about a promoted in-app purchase that customizes its order and
visibility on the device.

Article

# Supporting subscription offer codes in your app

Provide subscription service for customers who redeem offer codes through the
App Store or within your app.

## Overview

To help you acquire, retain, and win back subscribers, you can use offer
codes. Offer codes are alphanumeric codes that provide subscriptions at a
discount or for free for a specific duration. Configure the offers and create
offer codes in App Store Connect, and distribute them to your customers.
Customers can redeem offer codes in the App Store, using offer code redemption
URLs, or in your app if you’ve implemented one of the following APIs:

  * `offerCodeRedemption(isPresented:onCompletion:)` or `presentOfferCodeRedeemSheet(in:)`, which are available in iOS 16 and later and iPadOS 16 and later

  * `presentCodeRedemptionSheet()`, which is available in iOS 14 and later and iPadOS 14 and later

When customers redeem a valid offer code, your app receives a successful
transaction. If customers redeem offer codes in the App Store and don’t have
your app installed, they’re prompted to download it as part of the redemption
flow. Successfully redeeming an offer code entitles the customer to the auto-
renewable subscription, the same as a purchase does. Your app needs to provide
service for the product.

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

### Support offer codes redeemed outside of your app

Customers may redeem offer codes outside your app, by entering the offer code
in the App Store, or by using a redemption URL. To handle offer codes — and
other transactions that can occur outside of your app — your app needs to use
`updates` on `Transaction` to receive new transactions while the app is
running. Create a `Task` to iterate through the transactions from the listener
as soon as your app launches. For more information and sample code, see
`updates`.

When the app launches, it needs to check `all` or `currentEntitlements` on
`Transaction` to get any transactions that may have occurred while the app
wasn’t running. Process the transactions to ensure your app provides service
for all products it’s entitled to.

### Identify subscriptions purchased with offer codes

When customers successfully redeem subscription offer codes, the transaction
or subscription renewal information contain fields that identify the offer and
its offer type. Find the offer code details in the transaction information, in
your app and on your server, as follows.

In your app, use the following StoreKit APIs to locate the offer code
information:

  * See the `Transaction` properties `offerID` and `offerType`. An offer type value of `code` indicates the customer redeemed an offer code.

  * Some offer code redemptions may apply to an auto-renewable subscription’s next renewal period, for example, if the customer is already subscribed. In this case, see the `Product.SubscriptionInfo.RenewalInfo` properties `offerID` and `offerType`. An offer type value of `code` indicates the customer redeemed an offer code.

On your server, use the following server-side APIs to locate offer code
information:

  * In the App Store Server API, when you call endpoints such as Get Transaction History, Get All Subscription Statuses, and others, the response contains the signed transaction, `JWSTransaction`. In its decoded payload, `JWSTransactionDecodedPayload`, look for the fields `offerIdentifier` and `offerType`. An `offerType` value of `3` indicates the customer redeemed an offer code.

  * The App Store Server Notifications V2 sends a notification with an `OFFER_REDEEMED` `notificationType` when someone redeems an offer code. The decoded payloads `JWSTransactionDecodedPayload` and `JWSRenewalInfoDecodedPayload` contain the fields `offerIdentifier` and `offerType`. An `offerType` value of `3` indicates the customer redeemed an offer code.

### Provide subscription service to new and existing customers

When you acquire new customers with an offer code, they already have an auto-
renewable subscription when they open your app for the first time. In addition
to providing subscription service, you may need to update your backend
system’s records. Your app follows these steps:

  1. When the app launches, check `all` or `currentEntitlements` on `Transaction` to get all transactions or current entitlements, respectively. StoreKit automatically validates the transactions, and returns verified results in `VerificationResult.verified(_:)`. To perform your own validation, use the `jwsRepresentation` property.

  2. To determine if a subscription results from an offer code redemption, check the `offerID` and `offerType` properties on the subscription’s `Transaction`. 

  3. Provide the subscription service based on the offer and call `finish()` on `Transaction`. 

  4. Guide new customers through your new-user experience, as needed. Update your backend system’s records.

When an existing customer redeems an offer code within your app, the
transaction comes in through the `updates` sequence on `Transaction`. Process
the transaction as usual, providing service based on the offer, and call
`finish()`.

Article

# Testing at all stages of development with Xcode and the sandbox

Verify your implementation of in-app purchases by testing your code throughout
its development.

## Overview

Use the Apple sandbox and Xcode test environments to test your implementation
of in-app purchases using the StoreKit framework. Comprehensive testing can
help you:

  * Ensure a seamless purchase flow to provide a positive customer experience in your app.

  * Implement sound logic that covers all scenarios, such as purchases, restores, and subscription offers.

  * Validate that purchases behave correctly in production after your app is available in the App Store.

The tools you need to test in-app purchases, non-renewing subscriptions, and
auto-renewable subscriptions from early development through beta testing are:

StoreKit Testing in Xcode

    

For early development, continuous integration, and debugging. For more
information, see StoreKit Test.

Sandbox

    

For testing scenarios using in-app purchase data you set up in App Store
Connect. For more information, see Testing in-app purchases with sandbox.

TestFlight

    

For managing beta testing with internal and external testers. TestFlight uses
a beta build of your app or App Clip that you upload to App Store Connect. For
more information, see Beta Testing Made Simple with TestFlight.

Choose the tools that support the test scenarios you need. Make sure you’re
able to perform the setup required for the tools you choose.

During the early stages of development, you may not be ready to configure in-
app purchases in App Store Connect. StoreKit Testing in Xcode lets you
configure the information locally. You can test StoreKit transactions before
you create Sandbox Apple IDs, without a network connection. You can test your
app in Simulator or on real devices.

After you set up in-app purchases in App Store Connect, start using the
sandbox environment to test the product information your app will use in
production. Testing in the sandbox lets you test transactions from end-to-end
and from your app to your server. You can also test any server-to-server
functionalities your app depends on, such as transaction validation and App
Store Server Notifications.

TestFlight lets you get feedback from members of your team or from external
testers. TestFlight uses the sandbox environment for in-app purchases.
Transactions and purchases that occur in the sandbox don’t incur charges. The
following table compares the test environments and features:

Test environment| Requires App Store Connect setup| Provides receipts and JSON
Web Signature (JWS) transactions signed by the App Store| Provides
subscription renewal information signed by the App Store  
---|---|---|---  
StoreKit Testing in Xcode| No| No (signed by Xcode)| No (signed by Xcode)  
Sandbox| Yes| Yes| Yes  
TestFlight (uses the sandbox)| Yes| Yes| Yes  
  
None of the test environments charge users when they test buying a product.
The App Store doesn’t send emails for purchases or refunds made in the test
environments.

### Control the test environment

To set up and run test scenarios, you often need to control the test
environment. For example, you may want to reset a test account to rerun the
same test multiple times, or mimic actions users take outside your app that
affect the test conditions. The following table shows the capabilities each
tool has to control the test environment:

Test scenario| Sandbox| StoreKit Testing in Xcode  
---|---|---  
Test different storefronts to affect price tiers and locale| Yes| Limited (no
price tiers)  
Clear the purchase history| Yes| Yes  
Test subscription upgrades, downgrades, cross-grades, and auto-renew
cancellations| Yes| Yes  
Reset eligibility for introductory offers| Yes| Yes  
Introduce forced StoreKit errors for testing| No| Yes  
Speed up or slow down the rate of time for testing subscription renewals| Yes|
Yes  
  
For more information about speeding up renewal periods for testing, see Test
in-app purchases.

### Test common StoreKit scenarios

All apps that offer in-app purchases need to support restoring purchases,
displaying in-app purchases to the customer, and handling basic transactions.
The following table lists common test scenarios and whether they’re testable
in the sandbox or Xcode:

Test scenario| Sandbox| StoreKit Testing in Xcode  
---|---|---  
Restore purchases| Yes| Yes  
Finish a transaction with `finish()` or `finishTransaction(_:)`| Yes| Yes  
Buy a consumable or non-consumable in-app purchase| Yes| Yes  
Repurchase a non-consumable purchase for repeated testing| Yes| Yes  
Purchase an auto-renewable subscription| Yes| Yes  
Purchase a non-renewing subscription| Yes| Yes  
Refund an in-app purchase| Yes| Yes  
Test an interrupted purchase, where the user must complete actions outside the
app| Yes| Yes  
Test a failed purchase attempt when payment authorization fails| No| Yes  
Retrieve configured in-app purchases from App Store Connect| Yes| Yes
(optionally); can also retrieve data from a StoreKit configuration file  
Manage subscriptions within your app with `showManageSubscriptions(in:)` and
`manageSubscriptionsSheet(isPresented:)`| Yes| Yes  
Initiate a refund request. For more information, see Testing refund requests.|
Yes| Yes  
  
### Test subscriptions and Ask to Buy

Depending on the in-app purchases your app offers, you may need to test
scenarios that involve auto-renewing subscriptions, introductory offers,
promotional offers, and Ask to Buy. The following table lists test scenarios
and whether they’re testable in the sandbox or Xcode:

Test scenario| Sandbox| StoreKit Testing in Xcode  
---|---|---  
Initiate an Ask to Buy transaction that results in a deferred state| Yes| Yes  
Resolve an Ask to Buy transaction by approving or rejecting it| No| Yes  
Redeem an introductory offer for an auto-renewable subscription| Yes| Yes  
Redeem a promotional offer for an auto-renewable subscription| Yes| Yes  
Redeem an offer code for an auto-renewable subscription| No| Yes  
Process a subscription renewal| Yes| Yes  
Process a revoked or refunded subscription| Yes| Yes  
Respond to a customer canceling a subscription and disabling auto-renew| Yes|
Yes  
Respond to an expired subscription| Yes| Yes  
Process a subscription upgrade or downgrade| Yes| Yes  
Process a subscription cross-grade with the same or different duration| Yes|
Yes  
Test a price increase for an auto-renewable subscription| No| Yes  
Test billing retry and billing grace period| No| Yes  
  
For more information, see Approve what kids buy with Ask to Buy and Testing
introductory offers.

## See Also

### Testing in-app purchases

Testing in-app purchases with sandbox

Test your implementation of in-app purchases using real product information
and server-to-server transactions in the sandbox environment.

Testing refund requests

Test your app’s implementation of refund requests, and your app’s and server’s
handling of approved and declined refunds.

Article

# Testing refund requests

Test your app’s implementation of refund requests, and your app’s and server’s
handling of approved and declined refunds.

## Overview

The sandbox environment and StoreKit Testing in Xcode both support testing
refund requests, which enable your customers to request a refund from within
your app. Your app displays the refund request sheet by calling any of these
methods: `beginRefundRequest(for:in:)` , `beginRefundRequest(in:)`,
`beginRefundRequest(for:in:)`, `beginRefundRequest(in:)`, or
`refundRequestSheet(for:isPresented:onDismiss:)`. Customers fill out the sheet
to submit the request.

Depending on your testing setup, the App Store automatically approves or
declines the refund request in the testing environment. Note that the App
Store doesn’t send emails for refund requests in testing environments.

### Test approved refunds

To set up a test for approved refunds, select any refund reason on the refund
request sheet, and submit the sheet. The App Store automatically approves the
refund request in the testing environment.

Your app receives a `Transaction` with refund information in the
`revocationDate` and `revocationReason` properties. If you’re testing in the
sandbox environment and your server receives App Store Server Notifications V2
for the sandbox, it gets a notification with a `REFUND` `notificationType`.

### Test declined refunds

To set up a test for declined refunds, follow these steps on the refund
request sheet with your app running in the sandbox environment:

  1. Under Issue, select Other.

  2. In the text box, type REJECT.

  3. Tap Request Refund.

The App Store automatically rejects the refund request in the testing
environment.

If your server receives App Store Server Notifications V2 for the sandbox
environment, it gets a notification with a `REFUND_DECLINED`
`notificationType`.

For more information on receiving server notifications for the sandbox
environment, see Enabling App Store Server Notifications. For more information
on testing, see Testing at all stages of development with Xcode and the
sandbox and Setting up StoreKit Testing in Xcode.

## See Also

### Testing in-app purchases

Testing at all stages of development with Xcode and the sandbox

Verify your implementation of in-app purchases by testing your code throughout
its development.

Testing in-app purchases with sandbox

Test your implementation of in-app purchases using real product information
and server-to-server transactions in the sandbox environment.

Article

# Choosing a StoreKit API for in-app purchases

Use the latest API to support in-app purchases in new or existing apps, or the
original API to support in-app purchases in earlier operating systems.

## Overview

The StoreKit framework provides two APIs to implement a store in your app and
offer in-app purchases:

  * In-App Purchase is a Swift-based API that provides App Store-signed transactions in JSON Web Signature (JWS) format, available starting in iOS 15, macOS 12, tvOS 15, watchOS 8, and visionOS 1.

  * Original API for in-app purchase provides transaction information using App Store receipts, available starting in iOS 3, macOS 10.7, tvOS 9, watchOS 6.2, and visionOS 1.

If your app has a minimum required operating system that the In-App Purchase
API supports, use this API to take advantage of Swift concurrency and
simplified in-app purchase workflows. Use this API for visionOS apps that use
multiple scenes.

Use the Original API for in-app purchase to maintain and update app versions
that have a minimum required operating system of the following versions: macOS
11 or earlier, iOS 14 or earlier, iPadOS 14 or earlier, tvOS 14 or earlier, or
watchOS 7 or earlier.

An app can use both the In-App Purchase API and the Original API for in-app
purchase if the app runs in iOS 15, macOS 12, tvOS 15, watchOS 8, and visionOS
1 or later. However, only the In-App Purchase API supports multi-scene apps
for visionOS.

Both APIs provide access to your data in the App Store, such as your
configured in-app purchases and transaction information for your customers.
In-app purchases that users make using either API are fully available to both
APIs.

### Use the In-App Purchase API to access new features

The following features are available only with the Swift-based In-App Purchase
APIs:

  * StoreKit views, which provide the UI to build a store in your app

  * Refund request sheets, such as `beginRefundRequest(for:in:)`, that enable customers to request refunds

  * Information about a subscription's renewal status, such as auto-renew preferences. For more information, see `Product.SubscriptionInfo.Status`.

  * Information about available promotional offers and a subscriber’s eligibility for an introductory offer. For more information, see `Product.SubscriptionInfo`.

  * Deferring or suppressing Billing Issue messages that the system displays. For more information, see `Message`.

  * Presenting the App Store sheet for managing subscriptions. For more information, see `showManageSubscriptions(in:subscriptionGroupID:)`.

  * Transaction information in JSON Web Signature (JWS) format. For more information, see `Transaction`.

### Use the Original API to support certain features

You might need to use the Original API for in-app purchase for the following
features, if your app supports them:

  * Promoting in-app purchases in apps that run in iOS 11 through 16.3. For more informaton, see Promoting in-app purchases. For information about this feature in iOS 16.4, see Supporting promoted in-app purchases in your app.

  * The Volume Purchase Program (VPP). For more information, see Device Management.

## See Also

### Original API for in-app purchase

API Reference

Original API for in-app purchase

Offer users additional content and services using the original In-App Purchase
API.

