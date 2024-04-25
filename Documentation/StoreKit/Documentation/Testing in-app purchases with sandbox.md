Article

# Testing fetching product identifiers

Verify that your app receives the correct product identifiers by inspecting or
replicating your app’s process for retrieving the identifiers.

## Overview

If you embed your product identifiers in your app, set a breakpoint in your
code after the code loads the identifiers. Verify that the instance of
`NSArray` contains your expected list of product identifiers.

Note

Changes that you make to product metadata in App Store Connect can take up to
one hour to appear in the sandbox environment.

If your app fetches your product identifiers from a server, manually fetch the
JSON file using a web browser such as Safari, or a command-line utility such
as `curl`. Verify that the data your server returns contains the expected list
of product identifiers and that your server correctly implements standard HTTP
caching mechanisms.

For more information on fetching product identifiers, see Loading in-app
product identifiers.

## See Also

### Product identifiers and requests

Testing invalid product identifier handling

Verify that your app correctly handles invalid product identifiers.

Testing a product request

Verify that requests for products function properly in the sandbox environment
by inspecting the App Store response.

Article

# Testing invalid product identifier handling

Verify that your app correctly handles invalid product identifiers.

## Overview

Intentionally include an invalid identifier in your app’s list of product
identifiers. Then do one of the following:

  * In a production build, verify that the app displays the rest of its store UI and that users can purchase the valid products.

  * In a development build, verify that the app brings the issue to your attention.

Check the console log and verify that you can correctly identify the invalid
product identifier. Make sure you remove it after testing.

For more information on fetching product identifiers, see Loading in-app
product identifiers.

## See Also

### Product identifiers and requests

Testing fetching product identifiers

Verify that your app receives the correct product identifiers by inspecting or
replicating your app’s process for retrieving the identifiers.

Testing a product request

Verify that requests for products function properly in the sandbox environment
by inspecting the App Store response.

Article

# Testing a product request

Verify that requests for products function properly in the sandbox environment
by inspecting the App Store response.

## Overview

After setting a breakpoint in your code, use the list of product identifiers
that you tested in Testing fetching product identifiers to create and submit
an instance of `SKProductsRequest`. Then inspect the lists of valid and
invalid product identifiers. If there are invalid product identifiers, review
your products in App Store Connect and correct your JSON file or property
list.

Note

Changes that you make to product metadata in App Store Connect can take up to
one hour to appear in the sandbox environment.

See Testing invalid product identifier handling for more information.

## See Also

### Product identifiers and requests

Testing fetching product identifiers

Verify that your app receives the correct product identifiers by inspecting or
replicating your app’s process for retrieving the identifiers.

Testing invalid product identifier handling

Verify that your app correctly handles invalid product identifiers.

Article

# Testing purchases made outside your app

Verify that your app receives and handles transactions that occur outside of
your app, such as subscription purchases, renewals, and offer and promo code
redemptions.

## Overview

When your app offers in-app purchases, customers typically buy the products
from within your app. However, purchase transactions can also occur on another
device or even outside your app. Your app needs to handle these transactions
when it launches. Use the Test Transactions feature in Account Settings in iOS
to simulate and test such transactions in the sandbox environment.

### Simulate a variety of purchase events

Several types of events result in a purchase transaction that occurs outside
your app, including the following:

Redeeming offer codes

    

People can redeem offer codes on the Redeem Gift Card or Code page in their
App Store account settings, by using a redemption URL, and when your app calls
`presentCodeRedemptionSheet()`. For more information, see Set up offer codes.

Redeeming a promo code for an in-app purchase

    

People can redeem a promo codes in the App Store. For more information, see
Request and manage promo codes.

Renewing an auto-renewable subscription

    

Apple bills customers when an auto-renewable subscription renews, and the
renewal transaction occurs outside your app.

Resubscribing from the Apple Subscriptions page

    

People can resubscribe to expired subscriptions from their Account >
Subscriptions page in the App Store.

All of these events result in StoreKit sending a transaction to your app
through the `updates` asynchronous sequence in `Transaction`. Test your app to
be sure it handles the transaction.

### Set up and perform a test

To create a transaction outside your app for the testing environment, first
open Account Settings on the iOS device, as follows:

  1. Open Settings and select App Store.

  2. Select the Sandbox Apple ID. 

  3. Select Manage on the popup sheet. The Account Settings page appears.

Next, you need the product ID for a product you set up in App Store Connect,
and your app’s bundle ID.

Note

Changes that you make to product metadata in App Store Connect can take up to
one hour to appear in the sandbox environment.

To simulate a purchase outside your app, follow these steps:

  1. On the Account Settings page, select Test Transactions.

  2. Enter your product ID and the bundle ID in the text boxes labeled Product ID and Bundle ID, respectively.

  3. Click Next.

  4. The system brings up the payment sheet for the sandbox environment, which is labeled with "App Store [Sandbox]". Confirm the purchase. Note: The sandbox environment doesn’t process actual payments. Instead, it returns transactions as if payments were processed successfully.

After you confirm the purchase, use the following steps to test your app:

  1. Open your app. The system delivers the new transaction to your app through the `updates` asynchronous sequence in `Transaction`.

  2. Confirm that your app receives and processes the transaction to provide access to the purchased product.

### Conclude or restart a test

You can repeat the test by purchasing the product again through the Test
Transactions feature in Account Settings. To repurchase some products you
might first need to clear the transactions for the Sandbox Apple ID, following
these steps:

  1. Open Settings and select App Store.

  2. Select the Sandbox Apple ID.

  3. Select Manage on the popup sheet.

  4. On the Account Settings page, select Clear Purchase History.

Restart your app. The purchase history for the Sandbox Apple ID will be empty
and ready for testing. Clearing the purchase history for Sandbox Apple IDs
with a high number of purchases may take longer.

## See Also

### Payment transactions

Testing an interrupted purchase

Verify that your app handles an interrupted purchase by inspecting and
invoking payment transactions.

Testing failing subscription renewals and in-app purchases

Verify that your app handles failed subscription renewals that are in the
billing retry or billing grace period states, as well as failed in-app
purchases.

Testing a payment request

Verify that requests for payment function properly in the sandbox environment
by inspecting the calls to the payment transaction observer.

Article

# Testing an interrupted purchase

Verify that your app handles an interrupted purchase by inspecting and
invoking payment transactions.

## Overview

An interrupted purchase is a transaction that requires the user to perform
some action outside of your app before completing their transaction. For
example, the user may need to update their payment method or accept new terms
and conditions before continuing with their transaction.

In sandbox testing, you can simulate an interrupted purchase by turning on the
interrupted purchase feature in App Store Connect for a tester Sandbox Apple
ID. This interrupts all purchase attempts by that Sandbox Apple ID until you
agree to the updated terms and conditions on the iOS device, or until you turn
off the feature in App Store Connect. To learn how to set up interrupted
purchase testing, see Enable interrupted purchases for a Sandbox Apple ID.

### Set up testing

To enable interrupted purchases for the Sandbox Apple ID, log in to App Store
Connect, and do the following:

  1. From Users and Access, open the Users and Access Panel in the sidebar, under the Sandbox header, select Testers. On the right, you can view your Sandbox Apple IDs.

  2. Select a Sandbox Apple ID to use for testing interrupted purchases. If it’s already enabled, you’ll see a checkmark under the Interrupted Purchases column.

  3. In the dialog that appears, select Interrupt Purchases for This Tester.

### Begin testing

After setting up interrupted purchase testing in App Store Connect, use the
following steps to test your app:

  1. On the test device, sign in with the Sandbox Apple ID that has interrupted purchases enabled.

  2. In your app, select Buy or Subscribe to make an in-app purchase. 

  3. Observe that the system displays a payment sheet.

  4. In Xcode, verify that the payment queue receives a new transaction in the state `SKPaymentTransactionState.purchasing`.

  5. On the device, authenticate the payment sheet.

  6. In Xcode, observe that the payment fails. The payment queue receives an updated transaction in the state `SKPaymentTransactionState.failed`.

  7. Check that your code calls `finishTransaction(_:)` to remove it from the queue.

  8. On the device, observe that the system displays Terms & Conditions, interrupting the purchase (because you configured the sandbox environment to do so).

  9. On the device, tap to agree to the Terms & Conditions.

  10. In Xcode, verify that the payment queue receives a new transaction in the `SKPaymentTransactionState.purchased` state for the same `productIdentifier` and in the same quantity as the failed transaction.

  11. In Xcode, validate the receipt. Check that your app provides the service or the product, and calls `finishTransaction(_:)`.

  12. On the device, the user should observe a successful purchase.

### Conclude testing

The Sandbox Apple ID continues to experience interrupted purchases until you
disable it in App Store Connect, or until the user agrees to the terms and
conditions on the device. To disable interrupted purchases in App Store
Connect, deselect Interrupt Purchases for This Tester. For more information,
see Enable interrupted purchases for a Sandbox Apple ID.

## See Also

### Payment transactions

Testing purchases made outside your app

Verify that your app receives and handles transactions that occur outside of
your app, such as subscription purchases, renewals, and offer and promo code
redemptions.

Testing failing subscription renewals and in-app purchases

Verify that your app handles failed subscription renewals that are in the
billing retry or billing grace period states, as well as failed in-app
purchases.

Testing a payment request

Verify that requests for payment function properly in the sandbox environment
by inspecting the calls to the payment transaction observer.

Article

# Testing failing subscription renewals and in-app purchases

Verify that your app handles failed subscription renewals that are in the
billing retry or billing grace period states, as well as failed in-app
purchases.

## Overview

Payments can fail unexpectedly at any stage of the billing cycle, such as when
a payment card expires. Test your app’s user experience to ensure it handles
these unexpected events, and provides appropriate levels of service when
billing issues occur.

In sandbox testing, you can simulate billing issues that cause in-app
purchases to fail, and auto-renewable subscriptions not to renew. You can also
enable Billing Grace Period for the sandbox environment. Use these sandbox
features to test how your app handles auto-renewable subscriptions with
billing issues that do or don’t recover.

The sandbox environment sends App Store Server Notifications as you perform
tests. For more information, see Enabling App Store Server Notifications.

The sandbox environment renews auto-renewable subscriptions up to 12 times.
For more information about renewal rates in the sandbox environment, see Edit
subscription renewal speed.

For more information about subscription state changes when billing issues
occur, see Reducing Involuntary Subscriber Churn. For information about how
apps determine access to subscription content, see Handling Subscriptions
Billing.

### Configure the sandbox environment to simulate billing issues

Follow these steps on a test device running iOS 16 or iPadOS 16, or later:

  1. Sign in to the App Store using a Sandbox Apple ID.

  2. Choose Settings > App Store > Sandbox Account > Manage > Account Settings.

  3. Disable the Allow Purchases & Renewals setting. 

Disabling this setting causes in-app purchases to fail, and auto-renewable
subscriptions to not renew in the sandbox environment.

Note

This setting applies to all devices that the Sandbox Apple ID signs in to, and
to all active auto-renewable subscriptions belonging to that account.

This setting stays in a disabled state until you reenable it. Reenable it to
simulate a customer resolving a billing issue.

### Enable Billing Grace Period in the sandbox environment

To enable Billing Grace Period in the sandbox environment, log in to App Store
Connect, and do the following:

  1. From My Apps, select your app.

  2. In the sidebar under Features, click Subscriptions.

  3. In the Billing Grace Period section, click Set Up Billing Grace Period.

  4. Select a duration from the drop-down menu.

  5. Select whether to apply the grace period to all renewals or to only paid-to-paid renewals. For more information about the configurable settings, see Enable Billing Grace Period for auto-renewable subscriptions.

  6. Select Only Sandbox Environment to enable Billing Grace Period for testing only.

  7. Click Next.

  8. Click Confirm.

To test billing issues for subscriptions with Billing Grace Period, first,
purchase an auto-renewable subscription, and then configure the setting to
simulate billing issues (as described above in Configure the sandbox
environment to simulate billing issues).

### Test subscriptions that enter a billing retry state

Auto-renewable subscriptions expire and enter a billing retry state when a
subscription fails to auto-renew.

This test case assumes that Billing Grace Period is in a disabled state for
the sandbox enviroment. To test subscriptions entering a billing retry state:

  1. Successfully purchase an auto-renewable subscription in your app.

  2. Set the environment to simulate billing issues, as described above in Configure the sandbox environment to simulate billing issues. 

  3. Wait for the subscription period to renew. The renewal fails, and it enters a billing retry state.

  4. Check that your app recognizes the state. Subscriptions in a billing retry state that aren't in a billing grace period are not entitled to service. StoreKit provides the `isInBillingRetry` value in the `Product.SubscriptionInfo.RenewalState` object.

### Test subscriptions that enter a billing grace period

Auto-renewable subscriptions enter a billing grace period when both of the
following occur:

  * Billing Grace Period is enabled for your app

  * The subscription fails to auto-renew

To test subscriptions entering a billing grace period:

  1. Follow the steps as described above in Enable Billing Grace Period in the sandbox environment.

  2. Successfully purchase an auto-renewable subscription in your app.

  3. Set the environment to simulate billing issues, as described above in Configure the sandbox environment to simulate billing issues. 

  4. Wait for the subscription period to renew. The subscription enters the billing grace period.

  5. Check that your app recognizes the state and provides service for the subscription during the billing grace period. StoreKit provides the grace period expiration date in the `gracePeriodExpirationDate` property of the `Product.SubscriptionInfo.RenewalInfo` object.

  6. Wait for the billing grace period to expire. The subscription remains in the billing retry state. 

  7. Check that your app recognizes the billing retry state. Subscriptions aren’t entitled to service after the billing grace period expires.

Note

Auto-renewable subscriptions in a billing grace period state are entitled to
service.

### Test billing problem messaging after a subscription enters a billing retry
state

Auto-renewable subscriptions expire and enter a billing retry state when a
subscription fails to auto-renew. The system displays a Billing Problem
message when your app launches, unless your app chooses to delay the
`billingIssue` message. Use these steps to trigger the message and test how
your app responds to the message in various views. For more information about
managing these system messages, see `Message`.

To test when the system presents the Billing Problem sheet after subscriptions
enter the billing retry state:

  1. Successfully purchase an auto-renewable subscription in your app.

  2. Set the environment to simulate billing issues, as described above in Configure the sandbox environment to simulate billing issues. 

  3. Wait for the subscription period to renew. The renewal fails, and enters a billing retry state.

  4. The App Store sends the `billingIssue` message. Launch the app or bring it to the foreground. 

  5. If your app doesn't implement `messages`, the system presents the Billing Problem sheet.

  6. If your app implements `messages` and delays the message, perform the steps your app requires for it to call `display(in:)`. As long as the billing issue is still active, the system presents the Billing Problem sheet. If you resolve the billing issue before the app calls `display(in:)`, the system doesn't present the sheet.

You may perform this test with or without Billing Grace Period enabled.

### Test subscriptions that recover from billing issues

A subscription is _recovered_ when a billing retry succeeds. It exits a
billing retry or billing grace period state, and is active again.

To test recovered auto-renewable subscriptions, follow these steps:

  1. Start with a subscription in the billing retry state, as described above in Test subscriptions that enter a billing retry state.

  2. Choose Settings > App Store > Sandbox Account > Manage > Account Settings, and enable the Allow Purchases & Renewals setting, which causes the next subscription renewal attempt to succeed.

  3. Check that your app recognizes the active subscription state, which is entitled to service.

Repeat the test starting with a subscription in the billing grace period, as
described above in Test subscriptions that enter a billing grace period.

The subscription billing cycle for a subscription that recovers from a billing
retry state starts on the recovery date. The billing cycle for a subscription
that recovers during a billing grace period doesn't change.

### Test subscriptions that don't recover from billing issues

Subscriptions exit a billing retry state when any of the following happens:

  * The billing retry period expires without recovering the subscription.

  * The customer cancels the subscription.

  * The subscription is recovered because billing succeeds.

To test subscriptions that expire and don't recover, follow these steps:

  1. Start with a subscription in a billing retry state, as described above in Test subscriptions that enter a billing retry state.

  2. Wait for the billing retry period to expire — don’t enable the Allow Purchases & Renewals setting. 

  3. Check that your app recognizes the subscription state. The subscription is inactive and not entitled to service.

To test a subscription that a customer cancels, follow these steps:

  1. Start with a subscription in a billing grace period, as described above in Test subscriptions that enter a billing grace period.

  2. Cancel the subscription by managing subscriptions in Settings, or by using your app’s implementation of `showManageSubscriptions(in:)`. For more information about managing subscriptions in Settings, see If you want to cancel a subscription from Apple.

  3. The system immediately cancels the subscription. 

  4. Check that your app recognizes the subscription state. The subscription is inactive and not entitled to service.

Repeat the test starting with a subscription in the billing retry state, as
described above in Test subscriptions that enter a billing retry state.

### Test a failed in-app purchase

To test a failed purchase attempt, follow these steps:

  1. Set the environment to simulate billing issues, as described above in Configure the sandbox environment to simulate billing issues. 

  2. In your app, attempt to buy an in-app purchase product. The system displays an error message for the sandbox environment that shows the purchase failed. 

  3. To continue testing billing issues, select OK. Alternatively, to simulate a user resolving a billing issue, select Settings to return to Account Settings, where you can enable Allow Purchases & Renewals.

## See Also

### Payment transactions

Testing purchases made outside your app

Verify that your app receives and handles transactions that occur outside of
your app, such as subscription purchases, renewals, and offer and promo code
redemptions.

Testing an interrupted purchase

Verify that your app handles an interrupted purchase by inspecting and
invoking payment transactions.

Testing a payment request

Verify that requests for payment function properly in the sandbox environment
by inspecting the calls to the payment transaction observer.

Article

# Testing a payment request

Verify that requests for payment function properly in the sandbox environment
by inspecting the calls to the payment transaction observer.

## Overview

Create an instance of `SKPayment` using a valid product identifier that you’ve
already tested, as described in Testing fetching product identifiers. Set a
breakpoint and inspect the payment request. Add the payment request to the
transaction queue, and set a breakpoint to confirm that the system calls your
observer’s `paymentQueue(_:updatedTransactions:)` method.

Though you can finish the transaction immediately without providing the
content of the purchase during testing, failing to finish the transaction can
cause problems. Unfinished transactions remain in the queue indefinitely,
which could interfere with later testing. Complete the transaction as
described in Finishing a transaction at the end of each test.

## See Also

### Payment transactions

Testing purchases made outside your app

Verify that your app receives and handles transactions that occur outside of
your app, such as subscription purchases, renewals, and offer and promo code
redemptions.

Testing an interrupted purchase

Verify that your app handles an interrupted purchase by inspecting and
invoking payment transactions.

Testing failing subscription renewals and in-app purchases

Verify that your app handles failed subscription renewals that are in the
billing retry or billing grace period states, as well as failed in-app
purchases.

Article

# Testing an auto-renewable subscription

Verify that your app handles a subscription lapse properly using the
accelerated time rates within the sandbox environment.

## Overview

Auto-renewable subscriptions behave differently in the sandbox environment and
the production environment.

In the sandbox environment, subscription renewals happen at an accelerated
rate, and auto-renewable subscriptions renew up to 12 times after the initial
purchase. This enables you to test how your app handles a subscription
renewal, a subscription lapse, and a subscription history that includes gaps.

You can choose a subscription renewal speed for each Sandbox Apple ID account
in App Store Connect. For a complete list of subscription durations within the
sandbox environment and more information, see Manage Sandbox Apple ID
settings.

The accelerated expiration and renewal rates in the sandbox environment make
it possible for subscriptions to expire before the system tries to renew them.
When a subscription expires before the system tries to renew it, it results in
a short lapse in the subscription period. These lapses are possible in
production; verify that your app handles them appropriately.

## See Also

### Subscriptions

Testing resubscribing from the subscriptions page

Verify that your app can reactivate an expired subscription by receiving a
transaction callback or inspecting an updated receipt.

Testing disabling auto-renew

Verify that your app receives subscription updates when a user cancels a
subscription by verifying the receipt or receiving a notification.

Article

# Testing resubscribing from the subscriptions page

Verify that your app can reactivate an expired subscription by receiving a
transaction callback or inspecting an updated receipt.

## Overview

Customers can manage their active subscriptions, as well as their expired
subscriptions for up to a year after expiry, on the Subscriptions page in iOS,
tvOS, iPadOS, and macOS. From this page, customers can upgrade, downgrade,
cancel, or change the type of their subscriptions.

In this test scenario, the customer resubscribes to an expired subscription
from the Subscriptions page in the App Store.

### Set up testing

This test case requires one or more subscriptions configured in App Store
Connect and an expired subscription for your Sandbox Apple ID. If you don’t
already have an expired subscription, purchase an auto-renewable subscription
and let it expire.

### Begin testing

To test resubscribing from the Subscriptions page:

  1. On the test iOS device, open Settings > App Store. 

  2. In the Sandbox Account section, tap your highlighted Sandbox Apple ID, and tap Manage.

  3. On devices running iOS 16 or later, tap Subscriptions on the Account Settings sheet.

  4. In the sandbox Subscriptions page, select the expired subscription you want to reactivate. The subscription products that appear are those you configured in App Store Connect under the same subscription group.

  5. Select a subscription product to resubscribe to. 

  6. To complete the purchase, authenticate the payment sheet that appears.

  7. Open your app.

  8. In Xcode, verify that your `SKPaymentTransactionObserver` gets a callback on `paymentQueue(_:updatedTransactions:)` with a transaction in the `SKPaymentTransactionState.purchased` state.

  9. Check that your app retrieves and verifies the app receipt. Verify that the successful transaction is in the receipt.

  10. Check that your app makes the in-app purchase available and updates the subscriber’s status.

  11. In Xcode, check that your app calls `finishTransaction(_:)`. For more information, see Finishing a transaction.

### Conclude testing

This test case requires no cleanup. For auto-renewable subscriptions, you can
perform the test again when the subscription expires.

## See Also

### Subscriptions

Testing an auto-renewable subscription

Verify that your app handles a subscription lapse properly using the
accelerated time rates within the sandbox environment.

Testing disabling auto-renew

Verify that your app receives subscription updates when a user cancels a
subscription by verifying the receipt or receiving a notification.

Article

# Testing disabling auto-renew

Verify that your app receives subscription updates when a user cancels a
subscription by verifying the receipt or receiving a notification.

## Overview

Customers can manage their active subscriptions, as well as their expired
subscriptions for up to a year after expiry, in the Subscriptions page on iOS,
tvOS, iPadOS, and macOS. In this test scenario, the customer cancels a
subscription, which disables auto-renew.

To set up for this test, purchase an auto-renewable subscription for the
Sandbox Apple ID account.

### Begin testing

To test disabling auto-renew:

  1. On the test iOS device, open Settings > App Store. 

  2. In the Sandbox Account section, tap your highlighted Sandbox Apple ID, and tap Manage. 

  3. In the sandbox Subscriptions page, select the subscription product that you want to cancel. 

  4. Tap the Cancel Subscription button. 

Verify the change in the subscription status using either of these two
methods:

  * If you’ve configured App Store Connect settings to receive App Store server notifications, your server receives the `notification_type` `DID_CHANGE_RENEWAL_STATUS` each time the subscription’s auto-renew status changes. For more information, see Enabling App Store Server Notifications.

  * Verify the receipt by calling verifyReceipt with the latest receipt. Check that the `auto_renew_status` property of the `responseBody.Pending_renewal_info` object changes to `0`. The `auto_renew_status_change_date_ms` property of `responseBody` contains the timestamp of the change.

### Test reenabling the subscription renewal

After disabling auto-renew, reenable the subscription on the same Manage
Subscriptions page by tapping the subscription and confirming payment.

Verify the change in the subscription status using either of these two
methods:

  * If you’ve configured App Store Connect settings to receive App Store server notifications, your server receives the `notification_type` `DID_CHANGE_RENEWAL_STATUS` each time the subscription’s auto-renew status changes. For more information, see Enabling App Store Server Notifications.

  * Verify the receipt by calling verifyReceipt with the latest receipt. Check that the `auto_renew_status` property of the `responseBody.Pending_renewal_info` object changes to `1`. The `auto_renew_status_change_date_ms` property of `responseBody` contains the timestamp of the change.

## See Also

### Subscriptions

Testing an auto-renewable subscription

Verify that your app handles a subscription lapse properly using the
accelerated time rates within the sandbox environment.

Testing resubscribing from the subscriptions page

Verify that your app can reactivate an expired subscription by receiving a
transaction callback or inspecting an updated receipt.

Article

# Testing Family Sharing

Verify that your app handles auto-renewable subscriptions and non-consumable
in-app purchases that family members share with Family Sharing.

## Overview

Family Sharing lets people share access to auto-renewable subscriptions or
non-consumables that have Family Sharing enabled with up to five family
members. You can use Sandbox Test Families to test whether your app works with
Family Sharing as expected.

Note

Changes that you make to product metadata in App Store Connect can take up to
one hour to appear in the sandbox environment.

To test Family Sharing in your app:

  * Ensure your in-app purchases are set up to support Family Sharing. For more information, see Turn on Family Sharing for in-app purchases.

  * Create two or more Sandbox Apple IDs to add to a Sandbox Test Family, or use existing accounts. A family group can have up to six members. For more information, see Create Sandbox Apple IDs.

  * Create the Sandbox Test Family in App Store Connect. For more information, see Create a Sandbox Test Family.

  * To make testing easier, have a separate device to use for each test family member. You can also use a single device and sign in using each family member’s Sandbox Apple ID in turn.

### Manage sharing for the Sandbox Test Family

You can set the sharing status for each member of the Sandbox Test Family
individually, as follows:

  * _Sharing_ indicates the family member shares their in-app purchases with the Sandbox Test Family, and gets access to in-app purchases shared by family members.

  * _Not Sharing_ indicates the family member isn’t sharing, and doesn’t get access to family-shared purchases. Changing the setting to Not Sharing revokes any family-shared purchases they have access to. In the test environment, turning off sharing is the equivalent of a family member leaving the group.

Modify the sharing status on the Family Sharing page in iOS by following these
steps:

  1. Open Settings and select App Store.

  2. Select the Sandbox Apple ID.

  3. On the popup sheet, select Manage.

  4. On the Account Settings page, select Family Sharing.

  5. Select a family member.

  6. Select Stop Sharing Purchases or Start Sharing Purchases, as appropriate.

You can also change these settings in App Store Connect. For more information,
see Manage a Sandbox Test Family.

### Test sharing an in-app purchase in a family group

The two main test cases for Family Sharing are a family member gaining and
losing access to family-shared purchases. You can simulate these situations as
follows.

To test family members gaining access to a shared purchase:

  1. Start with a Sandbox Test Family where members are sharing.

  2. In your app, purchase a shareable product.

  3. Open your app on a device signed in with the Sandbox Apple ID of another test family member.

  4. Verify that your app receives a transaction for the shared purchase and unlocks the content for the family member. Note that the transaction has a `familyShared` ownership type.

  5. When sharing auto-renewable subscriptions, if you have App Store Server Notifications V2 enabled in the sandbox environment, your server receives a notification for each test family member that has sharing enabled. For more information, see the `SUBSCRIBED` `notificationType`.

### Test revoked access to shared in-app purchases

To test a family member losing access to shared purchases:

  1. Start with a Sandbox Test Family with two or more members, and at least one shared purchase.

  2. In Account Settings > Family Sharing, select a test family member that is receiving access to a shared in-app purchase.

  3. Select Stop Sharing Purchases, and Stop Sharing to confirm.

  4. The test family member loses accesses to shared purchases. Open your app using their Sandbox Apple ID and confirm that your app receives an updated transaction that includes a `revocationDate` and `revocationReason`.

  5. If you have App Store Server Notifications V2 enabled in the sandbox environment, your server receives a `REVOKE` `notificationType` for the test family member that has sharing disabled.

Note that you can also change the sharing status using App Store Connect
instead of Account Settings in iOS.

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

# Testing App Store server notifications

Confirm that App Store Server Notifications service responds properly in the
sandbox environment.

## Overview

If you enabled notifications from the App Store for your app, test your logic
for transactions in the sandbox environment. To determine if a notification
for a subscription event occurred in the test environment, check whether the
value of the `environment` field equals `Sandbox` in the `data` object of the
App Store Server Notifications `responseBodyV2DecodedPayload` object.

For more information about the App Store Server Notifications service, see App
Store Server Notifications. To ask the App Store to send test notifications,
and to get a history of notifications sent to your server, see Request a Test
Notification and Get Notification History in the App Store Server API.

Article

# Testing transaction observer code

Verify that your app activates its payment transaction observer by using
breakpoints.

## Overview

Review the transaction observer’s implementation of the
`SKPaymentTransactionObserver` protocol. Verify that the
`SKPaymentTransactionObserver` listens for transactions when:

  * Your app isn’t displaying its store UI

  * If you didn’t recently initiate a purchase

Locate the call to the `add(_:)` method of `SKPaymentQueue` in your code.
Verify that your app calls this method at app launch. For more information,
see Setting up the transaction observer for the payment queue.

## See Also

### Transaction observer

Testing a successful transaction

Confirm that your app can make a successful transaction in the sandbox
environment by inspecting the transaction.

Testing complete transactions

Verify that your app completes transactions properly by confirming that any
downloadable purchases are present on your test device.

Article

# Testing a successful transaction

Confirm that your app can make a successful transaction in the sandbox
environment by inspecting the transaction.

## Overview

Set a breakpoint in your implementation of the transaction queue observer’s
`paymentQueue(_:updatedTransactions:)` method. Then sign in to the App Store
with a Sandbox Apple ID, and make a purchase in your app. Inspect the
transaction to verify that its status is
`SKPaymentTransactionState.purchased`.

Set a breakpoint at the point in your code where your app stores the purchase,
and confirm that your code saves the data in response to a successful
purchase. Inspect the user default or iCloud key-value store, to verify that
your code correctly records the information. For more information on saving
data in response to a successful purchase, see Persisting a purchase.

## See Also

### Transaction observer

Testing transaction observer code

Verify that your app activates its payment transaction observer by using
breakpoints.

Testing complete transactions

Verify that your app completes transactions properly by confirming that any
downloadable purchases are present on your test device.

Article

# Testing complete transactions

Verify that your app completes transactions properly by confirming that any
downloadable purchases are present on your test device.

## Overview

Locate where your app calls the `finishTransaction(_:)` method, and verify
that your app completes all work related to the transaction before calling the
method. For example, if the purchase includes downloadable content, verify
your app downloaded the content to your test device as described in Persisting
a purchase. Verify that you call `finishTransaction(_:)` for every
transaction, whether it succeeded or failed. For more information, see
Finishing a transaction.

## See Also

### Transaction observer

Testing transaction observer code

Verify that your app activates its payment transaction observer by using
breakpoints.

Testing a successful transaction

Confirm that your app can make a successful transaction in the sandbox
environment by inspecting the transaction.

Article

# Testing fetching product identifiers

Verify that your app receives the correct product identifiers by inspecting or
replicating your app’s process for retrieving the identifiers.

## Overview

If you embed your product identifiers in your app, set a breakpoint in your
code after the code loads the identifiers. Verify that the instance of
`NSArray` contains your expected list of product identifiers.

Note

Changes that you make to product metadata in App Store Connect can take up to
one hour to appear in the sandbox environment.

If your app fetches your product identifiers from a server, manually fetch the
JSON file using a web browser such as Safari, or a command-line utility such
as `curl`. Verify that the data your server returns contains the expected list
of product identifiers and that your server correctly implements standard HTTP
caching mechanisms.

For more information on fetching product identifiers, see Loading in-app
product identifiers.

## See Also

### Product identifiers and requests

Testing invalid product identifier handling

Verify that your app correctly handles invalid product identifiers.

Testing a product request

Verify that requests for products function properly in the sandbox environment
by inspecting the App Store response.

Article

# Testing invalid product identifier handling

Verify that your app correctly handles invalid product identifiers.

## Overview

Intentionally include an invalid identifier in your app’s list of product
identifiers. Then do one of the following:

  * In a production build, verify that the app displays the rest of its store UI and that users can purchase the valid products.

  * In a development build, verify that the app brings the issue to your attention.

Check the console log and verify that you can correctly identify the invalid
product identifier. Make sure you remove it after testing.

For more information on fetching product identifiers, see Loading in-app
product identifiers.

## See Also

### Product identifiers and requests

Testing fetching product identifiers

Verify that your app receives the correct product identifiers by inspecting or
replicating your app’s process for retrieving the identifiers.

Testing a product request

Verify that requests for products function properly in the sandbox environment
by inspecting the App Store response.

Article

# Testing a product request

Verify that requests for products function properly in the sandbox environment
by inspecting the App Store response.

## Overview

After setting a breakpoint in your code, use the list of product identifiers
that you tested in Testing fetching product identifiers to create and submit
an instance of `SKProductsRequest`. Then inspect the lists of valid and
invalid product identifiers. If there are invalid product identifiers, review
your products in App Store Connect and correct your JSON file or property
list.

Note

Changes that you make to product metadata in App Store Connect can take up to
one hour to appear in the sandbox environment.

See Testing invalid product identifier handling for more information.

## See Also

### Product identifiers and requests

Testing fetching product identifiers

Verify that your app receives the correct product identifiers by inspecting or
replicating your app’s process for retrieving the identifiers.

Testing invalid product identifier handling

Verify that your app correctly handles invalid product identifiers.

Article

# Testing purchases made outside your app

Verify that your app receives and handles transactions that occur outside of
your app, such as subscription purchases, renewals, and offer and promo code
redemptions.

## Overview

When your app offers in-app purchases, customers typically buy the products
from within your app. However, purchase transactions can also occur on another
device or even outside your app. Your app needs to handle these transactions
when it launches. Use the Test Transactions feature in Account Settings in iOS
to simulate and test such transactions in the sandbox environment.

### Simulate a variety of purchase events

Several types of events result in a purchase transaction that occurs outside
your app, including the following:

Redeeming offer codes

    

People can redeem offer codes on the Redeem Gift Card or Code page in their
App Store account settings, by using a redemption URL, and when your app calls
`presentCodeRedemptionSheet()`. For more information, see Set up offer codes.

Redeeming a promo code for an in-app purchase

    

People can redeem a promo codes in the App Store. For more information, see
Request and manage promo codes.

Renewing an auto-renewable subscription

    

Apple bills customers when an auto-renewable subscription renews, and the
renewal transaction occurs outside your app.

Resubscribing from the Apple Subscriptions page

    

People can resubscribe to expired subscriptions from their Account >
Subscriptions page in the App Store.

All of these events result in StoreKit sending a transaction to your app
through the `updates` asynchronous sequence in `Transaction`. Test your app to
be sure it handles the transaction.

### Set up and perform a test

To create a transaction outside your app for the testing environment, first
open Account Settings on the iOS device, as follows:

  1. Open Settings and select App Store.

  2. Select the Sandbox Apple ID. 

  3. Select Manage on the popup sheet. The Account Settings page appears.

Next, you need the product ID for a product you set up in App Store Connect,
and your app’s bundle ID.

Note

Changes that you make to product metadata in App Store Connect can take up to
one hour to appear in the sandbox environment.

To simulate a purchase outside your app, follow these steps:

  1. On the Account Settings page, select Test Transactions.

  2. Enter your product ID and the bundle ID in the text boxes labeled Product ID and Bundle ID, respectively.

  3. Click Next.

  4. The system brings up the payment sheet for the sandbox environment, which is labeled with "App Store [Sandbox]". Confirm the purchase. Note: The sandbox environment doesn’t process actual payments. Instead, it returns transactions as if payments were processed successfully.

After you confirm the purchase, use the following steps to test your app:

  1. Open your app. The system delivers the new transaction to your app through the `updates` asynchronous sequence in `Transaction`.

  2. Confirm that your app receives and processes the transaction to provide access to the purchased product.

### Conclude or restart a test

You can repeat the test by purchasing the product again through the Test
Transactions feature in Account Settings. To repurchase some products you
might first need to clear the transactions for the Sandbox Apple ID, following
these steps:

  1. Open Settings and select App Store.

  2. Select the Sandbox Apple ID.

  3. Select Manage on the popup sheet.

  4. On the Account Settings page, select Clear Purchase History.

Restart your app. The purchase history for the Sandbox Apple ID will be empty
and ready for testing. Clearing the purchase history for Sandbox Apple IDs
with a high number of purchases may take longer.

## See Also

### Payment transactions

Testing an interrupted purchase

Verify that your app handles an interrupted purchase by inspecting and
invoking payment transactions.

Testing failing subscription renewals and in-app purchases

Verify that your app handles failed subscription renewals that are in the
billing retry or billing grace period states, as well as failed in-app
purchases.

Testing a payment request

Verify that requests for payment function properly in the sandbox environment
by inspecting the calls to the payment transaction observer.

Article

# Testing an interrupted purchase

Verify that your app handles an interrupted purchase by inspecting and
invoking payment transactions.

## Overview

An interrupted purchase is a transaction that requires the user to perform
some action outside of your app before completing their transaction. For
example, the user may need to update their payment method or accept new terms
and conditions before continuing with their transaction.

In sandbox testing, you can simulate an interrupted purchase by turning on the
interrupted purchase feature in App Store Connect for a tester Sandbox Apple
ID. This interrupts all purchase attempts by that Sandbox Apple ID until you
agree to the updated terms and conditions on the iOS device, or until you turn
off the feature in App Store Connect. To learn how to set up interrupted
purchase testing, see Enable interrupted purchases for a Sandbox Apple ID.

### Set up testing

To enable interrupted purchases for the Sandbox Apple ID, log in to App Store
Connect, and do the following:

  1. From Users and Access, open the Users and Access Panel in the sidebar, under the Sandbox header, select Testers. On the right, you can view your Sandbox Apple IDs.

  2. Select a Sandbox Apple ID to use for testing interrupted purchases. If it’s already enabled, you’ll see a checkmark under the Interrupted Purchases column.

  3. In the dialog that appears, select Interrupt Purchases for This Tester.

### Begin testing

After setting up interrupted purchase testing in App Store Connect, use the
following steps to test your app:

  1. On the test device, sign in with the Sandbox Apple ID that has interrupted purchases enabled.

  2. In your app, select Buy or Subscribe to make an in-app purchase. 

  3. Observe that the system displays a payment sheet.

  4. In Xcode, verify that the payment queue receives a new transaction in the state `SKPaymentTransactionState.purchasing`.

  5. On the device, authenticate the payment sheet.

  6. In Xcode, observe that the payment fails. The payment queue receives an updated transaction in the state `SKPaymentTransactionState.failed`.

  7. Check that your code calls `finishTransaction(_:)` to remove it from the queue.

  8. On the device, observe that the system displays Terms & Conditions, interrupting the purchase (because you configured the sandbox environment to do so).

  9. On the device, tap to agree to the Terms & Conditions.

  10. In Xcode, verify that the payment queue receives a new transaction in the `SKPaymentTransactionState.purchased` state for the same `productIdentifier` and in the same quantity as the failed transaction.

  11. In Xcode, validate the receipt. Check that your app provides the service or the product, and calls `finishTransaction(_:)`.

  12. On the device, the user should observe a successful purchase.

### Conclude testing

The Sandbox Apple ID continues to experience interrupted purchases until you
disable it in App Store Connect, or until the user agrees to the terms and
conditions on the device. To disable interrupted purchases in App Store
Connect, deselect Interrupt Purchases for This Tester. For more information,
see Enable interrupted purchases for a Sandbox Apple ID.

## See Also

### Payment transactions

Testing purchases made outside your app

Verify that your app receives and handles transactions that occur outside of
your app, such as subscription purchases, renewals, and offer and promo code
redemptions.

Testing failing subscription renewals and in-app purchases

Verify that your app handles failed subscription renewals that are in the
billing retry or billing grace period states, as well as failed in-app
purchases.

Testing a payment request

Verify that requests for payment function properly in the sandbox environment
by inspecting the calls to the payment transaction observer.

Article

# Testing failing subscription renewals and in-app purchases

Verify that your app handles failed subscription renewals that are in the
billing retry or billing grace period states, as well as failed in-app
purchases.

## Overview

Payments can fail unexpectedly at any stage of the billing cycle, such as when
a payment card expires. Test your app’s user experience to ensure it handles
these unexpected events, and provides appropriate levels of service when
billing issues occur.

In sandbox testing, you can simulate billing issues that cause in-app
purchases to fail, and auto-renewable subscriptions not to renew. You can also
enable Billing Grace Period for the sandbox environment. Use these sandbox
features to test how your app handles auto-renewable subscriptions with
billing issues that do or don’t recover.

The sandbox environment sends App Store Server Notifications as you perform
tests. For more information, see Enabling App Store Server Notifications.

The sandbox environment renews auto-renewable subscriptions up to 12 times.
For more information about renewal rates in the sandbox environment, see Edit
subscription renewal speed.

For more information about subscription state changes when billing issues
occur, see Reducing Involuntary Subscriber Churn. For information about how
apps determine access to subscription content, see Handling Subscriptions
Billing.

### Configure the sandbox environment to simulate billing issues

Follow these steps on a test device running iOS 16 or iPadOS 16, or later:

  1. Sign in to the App Store using a Sandbox Apple ID.

  2. Choose Settings > App Store > Sandbox Account > Manage > Account Settings.

  3. Disable the Allow Purchases & Renewals setting. 

Disabling this setting causes in-app purchases to fail, and auto-renewable
subscriptions to not renew in the sandbox environment.

Note

This setting applies to all devices that the Sandbox Apple ID signs in to, and
to all active auto-renewable subscriptions belonging to that account.

This setting stays in a disabled state until you reenable it. Reenable it to
simulate a customer resolving a billing issue.

### Enable Billing Grace Period in the sandbox environment

To enable Billing Grace Period in the sandbox environment, log in to App Store
Connect, and do the following:

  1. From My Apps, select your app.

  2. In the sidebar under Features, click Subscriptions.

  3. In the Billing Grace Period section, click Set Up Billing Grace Period.

  4. Select a duration from the drop-down menu.

  5. Select whether to apply the grace period to all renewals or to only paid-to-paid renewals. For more information about the configurable settings, see Enable Billing Grace Period for auto-renewable subscriptions.

  6. Select Only Sandbox Environment to enable Billing Grace Period for testing only.

  7. Click Next.

  8. Click Confirm.

To test billing issues for subscriptions with Billing Grace Period, first,
purchase an auto-renewable subscription, and then configure the setting to
simulate billing issues (as described above in Configure the sandbox
environment to simulate billing issues).

### Test subscriptions that enter a billing retry state

Auto-renewable subscriptions expire and enter a billing retry state when a
subscription fails to auto-renew.

This test case assumes that Billing Grace Period is in a disabled state for
the sandbox enviroment. To test subscriptions entering a billing retry state:

  1. Successfully purchase an auto-renewable subscription in your app.

  2. Set the environment to simulate billing issues, as described above in Configure the sandbox environment to simulate billing issues. 

  3. Wait for the subscription period to renew. The renewal fails, and it enters a billing retry state.

  4. Check that your app recognizes the state. Subscriptions in a billing retry state that aren't in a billing grace period are not entitled to service. StoreKit provides the `isInBillingRetry` value in the `Product.SubscriptionInfo.RenewalState` object.

### Test subscriptions that enter a billing grace period

Auto-renewable subscriptions enter a billing grace period when both of the
following occur:

  * Billing Grace Period is enabled for your app

  * The subscription fails to auto-renew

To test subscriptions entering a billing grace period:

  1. Follow the steps as described above in Enable Billing Grace Period in the sandbox environment.

  2. Successfully purchase an auto-renewable subscription in your app.

  3. Set the environment to simulate billing issues, as described above in Configure the sandbox environment to simulate billing issues. 

  4. Wait for the subscription period to renew. The subscription enters the billing grace period.

  5. Check that your app recognizes the state and provides service for the subscription during the billing grace period. StoreKit provides the grace period expiration date in the `gracePeriodExpirationDate` property of the `Product.SubscriptionInfo.RenewalInfo` object.

  6. Wait for the billing grace period to expire. The subscription remains in the billing retry state. 

  7. Check that your app recognizes the billing retry state. Subscriptions aren’t entitled to service after the billing grace period expires.

Note

Auto-renewable subscriptions in a billing grace period state are entitled to
service.

### Test billing problem messaging after a subscription enters a billing retry
state

Auto-renewable subscriptions expire and enter a billing retry state when a
subscription fails to auto-renew. The system displays a Billing Problem
message when your app launches, unless your app chooses to delay the
`billingIssue` message. Use these steps to trigger the message and test how
your app responds to the message in various views. For more information about
managing these system messages, see `Message`.

To test when the system presents the Billing Problem sheet after subscriptions
enter the billing retry state:

  1. Successfully purchase an auto-renewable subscription in your app.

  2. Set the environment to simulate billing issues, as described above in Configure the sandbox environment to simulate billing issues. 

  3. Wait for the subscription period to renew. The renewal fails, and enters a billing retry state.

  4. The App Store sends the `billingIssue` message. Launch the app or bring it to the foreground. 

  5. If your app doesn't implement `messages`, the system presents the Billing Problem sheet.

  6. If your app implements `messages` and delays the message, perform the steps your app requires for it to call `display(in:)`. As long as the billing issue is still active, the system presents the Billing Problem sheet. If you resolve the billing issue before the app calls `display(in:)`, the system doesn't present the sheet.

You may perform this test with or without Billing Grace Period enabled.

### Test subscriptions that recover from billing issues

A subscription is _recovered_ when a billing retry succeeds. It exits a
billing retry or billing grace period state, and is active again.

To test recovered auto-renewable subscriptions, follow these steps:

  1. Start with a subscription in the billing retry state, as described above in Test subscriptions that enter a billing retry state.

  2. Choose Settings > App Store > Sandbox Account > Manage > Account Settings, and enable the Allow Purchases & Renewals setting, which causes the next subscription renewal attempt to succeed.

  3. Check that your app recognizes the active subscription state, which is entitled to service.

Repeat the test starting with a subscription in the billing grace period, as
described above in Test subscriptions that enter a billing grace period.

The subscription billing cycle for a subscription that recovers from a billing
retry state starts on the recovery date. The billing cycle for a subscription
that recovers during a billing grace period doesn't change.

### Test subscriptions that don't recover from billing issues

Subscriptions exit a billing retry state when any of the following happens:

  * The billing retry period expires without recovering the subscription.

  * The customer cancels the subscription.

  * The subscription is recovered because billing succeeds.

To test subscriptions that expire and don't recover, follow these steps:

  1. Start with a subscription in a billing retry state, as described above in Test subscriptions that enter a billing retry state.

  2. Wait for the billing retry period to expire — don’t enable the Allow Purchases & Renewals setting. 

  3. Check that your app recognizes the subscription state. The subscription is inactive and not entitled to service.

To test a subscription that a customer cancels, follow these steps:

  1. Start with a subscription in a billing grace period, as described above in Test subscriptions that enter a billing grace period.

  2. Cancel the subscription by managing subscriptions in Settings, or by using your app’s implementation of `showManageSubscriptions(in:)`. For more information about managing subscriptions in Settings, see If you want to cancel a subscription from Apple.

  3. The system immediately cancels the subscription. 

  4. Check that your app recognizes the subscription state. The subscription is inactive and not entitled to service.

Repeat the test starting with a subscription in the billing retry state, as
described above in Test subscriptions that enter a billing retry state.

### Test a failed in-app purchase

To test a failed purchase attempt, follow these steps:

  1. Set the environment to simulate billing issues, as described above in Configure the sandbox environment to simulate billing issues. 

  2. In your app, attempt to buy an in-app purchase product. The system displays an error message for the sandbox environment that shows the purchase failed. 

  3. To continue testing billing issues, select OK. Alternatively, to simulate a user resolving a billing issue, select Settings to return to Account Settings, where you can enable Allow Purchases & Renewals.

## See Also

### Payment transactions

Testing purchases made outside your app

Verify that your app receives and handles transactions that occur outside of
your app, such as subscription purchases, renewals, and offer and promo code
redemptions.

Testing an interrupted purchase

Verify that your app handles an interrupted purchase by inspecting and
invoking payment transactions.

Testing a payment request

Verify that requests for payment function properly in the sandbox environment
by inspecting the calls to the payment transaction observer.

Article

# Testing a payment request

Verify that requests for payment function properly in the sandbox environment
by inspecting the calls to the payment transaction observer.

## Overview

Create an instance of `SKPayment` using a valid product identifier that you’ve
already tested, as described in Testing fetching product identifiers. Set a
breakpoint and inspect the payment request. Add the payment request to the
transaction queue, and set a breakpoint to confirm that the system calls your
observer’s `paymentQueue(_:updatedTransactions:)` method.

Though you can finish the transaction immediately without providing the
content of the purchase during testing, failing to finish the transaction can
cause problems. Unfinished transactions remain in the queue indefinitely,
which could interfere with later testing. Complete the transaction as
described in Finishing a transaction at the end of each test.

## See Also

### Payment transactions

Testing purchases made outside your app

Verify that your app receives and handles transactions that occur outside of
your app, such as subscription purchases, renewals, and offer and promo code
redemptions.

Testing an interrupted purchase

Verify that your app handles an interrupted purchase by inspecting and
invoking payment transactions.

Testing failing subscription renewals and in-app purchases

Verify that your app handles failed subscription renewals that are in the
billing retry or billing grace period states, as well as failed in-app
purchases.

Article

# Testing an auto-renewable subscription

Verify that your app handles a subscription lapse properly using the
accelerated time rates within the sandbox environment.

## Overview

Auto-renewable subscriptions behave differently in the sandbox environment and
the production environment.

In the sandbox environment, subscription renewals happen at an accelerated
rate, and auto-renewable subscriptions renew up to 12 times after the initial
purchase. This enables you to test how your app handles a subscription
renewal, a subscription lapse, and a subscription history that includes gaps.

You can choose a subscription renewal speed for each Sandbox Apple ID account
in App Store Connect. For a complete list of subscription durations within the
sandbox environment and more information, see Manage Sandbox Apple ID
settings.

The accelerated expiration and renewal rates in the sandbox environment make
it possible for subscriptions to expire before the system tries to renew them.
When a subscription expires before the system tries to renew it, it results in
a short lapse in the subscription period. These lapses are possible in
production; verify that your app handles them appropriately.

## See Also

### Subscriptions

Testing resubscribing from the subscriptions page

Verify that your app can reactivate an expired subscription by receiving a
transaction callback or inspecting an updated receipt.

Testing disabling auto-renew

Verify that your app receives subscription updates when a user cancels a
subscription by verifying the receipt or receiving a notification.

Article

# Testing resubscribing from the subscriptions page

Verify that your app can reactivate an expired subscription by receiving a
transaction callback or inspecting an updated receipt.

## Overview

Customers can manage their active subscriptions, as well as their expired
subscriptions for up to a year after expiry, on the Subscriptions page in iOS,
tvOS, iPadOS, and macOS. From this page, customers can upgrade, downgrade,
cancel, or change the type of their subscriptions.

In this test scenario, the customer resubscribes to an expired subscription
from the Subscriptions page in the App Store.

### Set up testing

This test case requires one or more subscriptions configured in App Store
Connect and an expired subscription for your Sandbox Apple ID. If you don’t
already have an expired subscription, purchase an auto-renewable subscription
and let it expire.

### Begin testing

To test resubscribing from the Subscriptions page:

  1. On the test iOS device, open Settings > App Store. 

  2. In the Sandbox Account section, tap your highlighted Sandbox Apple ID, and tap Manage.

  3. On devices running iOS 16 or later, tap Subscriptions on the Account Settings sheet.

  4. In the sandbox Subscriptions page, select the expired subscription you want to reactivate. The subscription products that appear are those you configured in App Store Connect under the same subscription group.

  5. Select a subscription product to resubscribe to. 

  6. To complete the purchase, authenticate the payment sheet that appears.

  7. Open your app.

  8. In Xcode, verify that your `SKPaymentTransactionObserver` gets a callback on `paymentQueue(_:updatedTransactions:)` with a transaction in the `SKPaymentTransactionState.purchased` state.

  9. Check that your app retrieves and verifies the app receipt. Verify that the successful transaction is in the receipt.

  10. Check that your app makes the in-app purchase available and updates the subscriber’s status.

  11. In Xcode, check that your app calls `finishTransaction(_:)`. For more information, see Finishing a transaction.

### Conclude testing

This test case requires no cleanup. For auto-renewable subscriptions, you can
perform the test again when the subscription expires.

## See Also

### Subscriptions

Testing an auto-renewable subscription

Verify that your app handles a subscription lapse properly using the
accelerated time rates within the sandbox environment.

Testing disabling auto-renew

Verify that your app receives subscription updates when a user cancels a
subscription by verifying the receipt or receiving a notification.

Article

# Testing disabling auto-renew

Verify that your app receives subscription updates when a user cancels a
subscription by verifying the receipt or receiving a notification.

## Overview

Customers can manage their active subscriptions, as well as their expired
subscriptions for up to a year after expiry, in the Subscriptions page on iOS,
tvOS, iPadOS, and macOS. In this test scenario, the customer cancels a
subscription, which disables auto-renew.

To set up for this test, purchase an auto-renewable subscription for the
Sandbox Apple ID account.

### Begin testing

To test disabling auto-renew:

  1. On the test iOS device, open Settings > App Store. 

  2. In the Sandbox Account section, tap your highlighted Sandbox Apple ID, and tap Manage. 

  3. In the sandbox Subscriptions page, select the subscription product that you want to cancel. 

  4. Tap the Cancel Subscription button. 

Verify the change in the subscription status using either of these two
methods:

  * If you’ve configured App Store Connect settings to receive App Store server notifications, your server receives the `notification_type` `DID_CHANGE_RENEWAL_STATUS` each time the subscription’s auto-renew status changes. For more information, see Enabling App Store Server Notifications.

  * Verify the receipt by calling verifyReceipt with the latest receipt. Check that the `auto_renew_status` property of the `responseBody.Pending_renewal_info` object changes to `0`. The `auto_renew_status_change_date_ms` property of `responseBody` contains the timestamp of the change.

### Test reenabling the subscription renewal

After disabling auto-renew, reenable the subscription on the same Manage
Subscriptions page by tapping the subscription and confirming payment.

Verify the change in the subscription status using either of these two
methods:

  * If you’ve configured App Store Connect settings to receive App Store server notifications, your server receives the `notification_type` `DID_CHANGE_RENEWAL_STATUS` each time the subscription’s auto-renew status changes. For more information, see Enabling App Store Server Notifications.

  * Verify the receipt by calling verifyReceipt with the latest receipt. Check that the `auto_renew_status` property of the `responseBody.Pending_renewal_info` object changes to `1`. The `auto_renew_status_change_date_ms` property of `responseBody` contains the timestamp of the change.

## See Also

### Subscriptions

Testing an auto-renewable subscription

Verify that your app handles a subscription lapse properly using the
accelerated time rates within the sandbox environment.

Testing resubscribing from the subscriptions page

Verify that your app can reactivate an expired subscription by receiving a
transaction callback or inspecting an updated receipt.

Article

# Testing Family Sharing

Verify that your app handles auto-renewable subscriptions and non-consumable
in-app purchases that family members share with Family Sharing.

## Overview

Family Sharing lets people share access to auto-renewable subscriptions or
non-consumables that have Family Sharing enabled with up to five family
members. You can use Sandbox Test Families to test whether your app works with
Family Sharing as expected.

Note

Changes that you make to product metadata in App Store Connect can take up to
one hour to appear in the sandbox environment.

To test Family Sharing in your app:

  * Ensure your in-app purchases are set up to support Family Sharing. For more information, see Turn on Family Sharing for in-app purchases.

  * Create two or more Sandbox Apple IDs to add to a Sandbox Test Family, or use existing accounts. A family group can have up to six members. For more information, see Create Sandbox Apple IDs.

  * Create the Sandbox Test Family in App Store Connect. For more information, see Create a Sandbox Test Family.

  * To make testing easier, have a separate device to use for each test family member. You can also use a single device and sign in using each family member’s Sandbox Apple ID in turn.

### Manage sharing for the Sandbox Test Family

You can set the sharing status for each member of the Sandbox Test Family
individually, as follows:

  * _Sharing_ indicates the family member shares their in-app purchases with the Sandbox Test Family, and gets access to in-app purchases shared by family members.

  * _Not Sharing_ indicates the family member isn’t sharing, and doesn’t get access to family-shared purchases. Changing the setting to Not Sharing revokes any family-shared purchases they have access to. In the test environment, turning off sharing is the equivalent of a family member leaving the group.

Modify the sharing status on the Family Sharing page in iOS by following these
steps:

  1. Open Settings and select App Store.

  2. Select the Sandbox Apple ID.

  3. On the popup sheet, select Manage.

  4. On the Account Settings page, select Family Sharing.

  5. Select a family member.

  6. Select Stop Sharing Purchases or Start Sharing Purchases, as appropriate.

You can also change these settings in App Store Connect. For more information,
see Manage a Sandbox Test Family.

### Test sharing an in-app purchase in a family group

The two main test cases for Family Sharing are a family member gaining and
losing access to family-shared purchases. You can simulate these situations as
follows.

To test family members gaining access to a shared purchase:

  1. Start with a Sandbox Test Family where members are sharing.

  2. In your app, purchase a shareable product.

  3. Open your app on a device signed in with the Sandbox Apple ID of another test family member.

  4. Verify that your app receives a transaction for the shared purchase and unlocks the content for the family member. Note that the transaction has a `familyShared` ownership type.

  5. When sharing auto-renewable subscriptions, if you have App Store Server Notifications V2 enabled in the sandbox environment, your server receives a notification for each test family member that has sharing enabled. For more information, see the `SUBSCRIBED` `notificationType`.

### Test revoked access to shared in-app purchases

To test a family member losing access to shared purchases:

  1. Start with a Sandbox Test Family with two or more members, and at least one shared purchase.

  2. In Account Settings > Family Sharing, select a test family member that is receiving access to a shared in-app purchase.

  3. Select Stop Sharing Purchases, and Stop Sharing to confirm.

  4. The test family member loses accesses to shared purchases. Open your app using their Sandbox Apple ID and confirm that your app receives an updated transaction that includes a `revocationDate` and `revocationReason`.

  5. If you have App Store Server Notifications V2 enabled in the sandbox environment, your server receives a `REVOKE` `notificationType` for the test family member that has sharing disabled.

Note that you can also change the sharing status using App Store Connect
instead of Account Settings in iOS.

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

# Testing App Store server notifications

Confirm that App Store Server Notifications service responds properly in the
sandbox environment.

## Overview

If you enabled notifications from the App Store for your app, test your logic
for transactions in the sandbox environment. To determine if a notification
for a subscription event occurred in the test environment, check whether the
value of the `environment` field equals `Sandbox` in the `data` object of the
App Store Server Notifications `responseBodyV2DecodedPayload` object.

For more information about the App Store Server Notifications service, see App
Store Server Notifications. To ask the App Store to send test notifications,
and to get a history of notifications sent to your server, see Request a Test
Notification and Get Notification History in the App Store Server API.

Article

# Testing transaction observer code

Verify that your app activates its payment transaction observer by using
breakpoints.

## Overview

Review the transaction observer’s implementation of the
`SKPaymentTransactionObserver` protocol. Verify that the
`SKPaymentTransactionObserver` listens for transactions when:

  * Your app isn’t displaying its store UI

  * If you didn’t recently initiate a purchase

Locate the call to the `add(_:)` method of `SKPaymentQueue` in your code.
Verify that your app calls this method at app launch. For more information,
see Setting up the transaction observer for the payment queue.

## See Also

### Transaction observer

Testing a successful transaction

Confirm that your app can make a successful transaction in the sandbox
environment by inspecting the transaction.

Testing complete transactions

Verify that your app completes transactions properly by confirming that any
downloadable purchases are present on your test device.

Article

# Testing a successful transaction

Confirm that your app can make a successful transaction in the sandbox
environment by inspecting the transaction.

## Overview

Set a breakpoint in your implementation of the transaction queue observer’s
`paymentQueue(_:updatedTransactions:)` method. Then sign in to the App Store
with a Sandbox Apple ID, and make a purchase in your app. Inspect the
transaction to verify that its status is
`SKPaymentTransactionState.purchased`.

Set a breakpoint at the point in your code where your app stores the purchase,
and confirm that your code saves the data in response to a successful
purchase. Inspect the user default or iCloud key-value store, to verify that
your code correctly records the information. For more information on saving
data in response to a successful purchase, see Persisting a purchase.

## See Also

### Transaction observer

Testing transaction observer code

Verify that your app activates its payment transaction observer by using
breakpoints.

Testing complete transactions

Verify that your app completes transactions properly by confirming that any
downloadable purchases are present on your test device.

Article

# Testing complete transactions

Verify that your app completes transactions properly by confirming that any
downloadable purchases are present on your test device.

## Overview

Locate where your app calls the `finishTransaction(_:)` method, and verify
that your app completes all work related to the transaction before calling the
method. For example, if the purchase includes downloadable content, verify
your app downloaded the content to your test device as described in Persisting
a purchase. Verify that you call `finishTransaction(_:)` for every
transaction, whether it succeeded or failed. For more information, see
Finishing a transaction.

## See Also

### Transaction observer

Testing transaction observer code

Verify that your app activates its payment transaction observer by using
breakpoints.

Testing a successful transaction

Confirm that your app can make a successful transaction in the sandbox
environment by inspecting the transaction.

