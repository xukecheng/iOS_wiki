Instance Method

# paymentQueue(_:updatedTransactions:)

Tells an observer that one or more transactions have been updated.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    func paymentQueue(
        _ queue: SKPaymentQueue,
        updatedTransactions transactions: [SKPaymentTransaction]
    )

**Required**

##  Parameters

`queue`

    

The payment queue that updated the transactions.

`transactions`

    

An array of the transactions that were updated.

## Discussion

The application should process each transaction by examining the transaction’s
`transactionState` property. If `transactionState` is
`SKPaymentTransactionState.purchased`, payment was successfully received for
the desired functionality. The application should make the functionality
available to the user. If `transactionState` is
`SKPaymentTransactionState.failed`, the application can read the transaction’s
error property to return a meaningful error to the user.

Once a transaction is processed, it should be removed from the payment queue
by calling the payment queue’s `finishTransaction(_:)` method, passing the
transaction as a parameter.

Important

Once the transaction is finished, StoreKit can’t tell you that this item is
already purchased. It is important that applications process the transaction
completely before calling `finishTransaction(_:)`.

## See Also

### Handling transactions

`func paymentQueue(SKPaymentQueue, removedTransactions:
[SKPaymentTransaction])`

Tells an observer that one or more transactions have been removed from the
queue.

### Related Documentation

In-App Purchase Programming Guide

Instance Method

# paymentQueue(_:removedTransactions:)

Tells an observer that one or more transactions have been removed from the
queue.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    optional func paymentQueue(
        _ queue: SKPaymentQueue,
        removedTransactions transactions: [SKPaymentTransaction]
    )

##  Parameters

`queue`

    

The payment queue that updated the transactions.

`transactions`

    

An array of the transactions that were removed.

## Discussion

Your application does not typically need to implement this method but might
implement it to update its own user interface to reflect that a transaction
has been completed.

## See Also

### Handling transactions

`func paymentQueue(SKPaymentQueue, updatedTransactions:
[SKPaymentTransaction])`

Tells an observer that one or more transactions have been updated.

**Required**

Instance Method

# paymentQueue(_:restoreCompletedTransactionsFailedWithError:)

Tells the observer that an error occurred while restoring transactions.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    optional func paymentQueue(
        _ queue: SKPaymentQueue,
        restoreCompletedTransactionsFailedWithError error: any Error
    )

##  Parameters

`queue`

    

The payment queue that was restoring transactions.

`error`

    

The error that occurred.

## See Also

### Restoring transactions

`func paymentQueueRestoreCompletedTransactionsFinished(SKPaymentQueue)`

Tells the observer that the payment queue has finished sending restored
transactions.

Instance Method

# paymentQueueRestoreCompletedTransactionsFinished(_:)

Tells the observer that the payment queue has finished sending restored
transactions.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    optional func paymentQueueRestoreCompletedTransactionsFinished(_ queue: SKPaymentQueue)

##  Parameters

`queue`

    

The payment queue that restored the transactions.

## Discussion

This method is called after all restorable transactions have been processed by
the payment queue. Your application is not required to do anything in this
method.

## See Also

### Restoring transactions

`func paymentQueue(SKPaymentQueue,
restoreCompletedTransactionsFailedWithError: any Error)`

Tells the observer that an error occurred while restoring transactions.

Article

# Promoting in-app purchases

Show promoted in-app purchases on your product page and handle purchases that
users initiate on the App Store.

## Overview

Starting in iOS 11, you can promote in-app purchases on the App Store.

Note

To support promoted in-app purchases in apps with a minimum version of iOS
16.4 and later, use `PurchaseIntent`. For more information, see Supporting
promoted in-app purchases in your app.

Promoted in-app purchases appear on your product page, can appear in search
results, and can appear as featured items on an appropriate tab on the App
Store. Users can start an in-app purchase on the App Store and then transition
to your app to continue the transaction. If your app isn’t installed, they
receive a prompt to download it.

Promoting in-app purchases requires two steps:

  1. In App Store Connect, set up promotions by uploading promotional images. Use the App Store Promotions feature in App Store Connect to manage their order and visibility. For more information about the setup, see Promote in-app purchases.

  2. In your app, implement the delegate method `paymentQueue(_:shouldAddStorePayment:for:)` from the `SKPaymentTransactionObserver` protocol to handle the purchase. 

Important

To enable promoted in-app purchases, your app needs to use either
`PurchaseIntent` (starting in iOS 16.4) or
`paymentQueue(_:shouldAddStorePayment:for:)` (starting in iOS 11). Don’t use
both at the same time. If necessary, use conditional compilation to identify
the OS version the app is running in. For more information, see Running code
on a specific platform or OS version.

To customize the list of promoted in-app purchases for users, you can override
their default order and visibility using `SKProductStorePromotionController`.
Use overrides to show promotions that are relevant to the user. Overrides are
specific to a device, and take effect after the user launches the app at least
once. Using `SKProductStorePromotionController` is optional and isn’t required
for your in-app purchases to appear on the App Store.

For marketing guidance on this feature, see Promoting Your In-App Purchases.

Note

Promoted in-app purchases aren’t available to compatible iPad or iPhone apps
running in visionOS.

### Complete the purchase in the app

When a user selects an in-app product to purchase on the App Store, StoreKit
automatically opens your app and sends the transaction information to the
delegate in the `SKPaymentTransactionObserver` protocol. Your app needs to
complete the purchase transaction and any related actions that are specific to
it.

In the delegate method, return `true` to continue the transaction, or `false`
to defer or cancel it.

If your app isn’t installed when the user selects to purchase the in-app
product, the App Store automatically downloads the app or prompts the user to
purchase it. If the installed version of your app is an older version that
doesn’t support in-app purchase promotions, the App Store prompts the user to
upgrade the app.

### Continue the transaction

To continue an in-app purchase transaction, implement the delegate method in
the `SKPaymentTransactionObserver` protocol and return `true`. StoreKit then
displays the payment sheet, and the user can complete the transaction.

    
    
    //Continuing a transaction from the App Store.
    
    
    //MARK: - SKPaymentTransactionObserver
    
    
    func paymentQueue(_ queue: SKPaymentQueue, shouldAddStorePayment payment: SKPayment,
            for product: SKProduct) -> Bool {
        // Check to see if you can complete the transaction.
        // Return true if you can.
        return true
    }
    

### Defer or cancel the transaction

If your app needs to defer or cancel a transaction, return `false`. For
example, you may need to defer a transaction if the user is in the middle of
onboarding, and continue it after they complete the onboarding. Or, you may
need to cancel a transaction if the user has already unlocked the product
they’re trying to buy.

To defer a transaction:

  1. Save the `payment` to use when the app is ready. The payment already contains information about the product. Don’t create a new `SKPayment` with the same product.

  2. Return `false`.

  3. After the user finishes the onboarding or other actions that require a deferral, send the saved payment to the payment queue as you do with a typical in-app purchase.

To cancel a transaction:

  1. Return `false`.

  2. Provide feedback to the user. Although this step is optional, if you don’t provide feedback, the app’s lack of action after the user selects to purchase an in-app product in the App Store may seem like a bug.

    
    
    //Handling a transaction from the App Store.
    
    
    //MARK: - SKPaymentTransactionObserver
    
    
    func paymentQueue(_ queue: SKPaymentQueue, shouldAddStorePayment payment: SKPayment,
            for product: SKProduct) -> Bool {
    
    
        // Add code here to check if your app needs to defer the transaction.
        let shouldDeferPayment = ...
        // If you need to defer until onboarding is complete, save the payment and return false.
        if shouldDeferPayment {
            self.savedPayment = payment
            return false
        }
    
    
        // Add code here to check if your app needs to cancel the transaction.
        let shouldCancelPayment = ...
        // If you need to cancel the transaction, then return false:
        if shouldCancelPayment {
            return false
        }
    }
    
    
    // If you cancel the transaction, provide feedback to the user.
    
    
    // Continuing a previously deferred payment.
    SKPaymentQueue.default().add(savedPayment)
    

### Get visibility settings

To get the visibility settings for a promoted product, call
`fetchStorePromotionVisibility(for:completionHandler:)`, providing the product
information.

    
    
    // Reading visibility override of a promoted in-app purchase.
    
    
    // Fetch product info for "Hidden Beaches pack."
    
    
    let storePromotionController = SKProductStorePromotionController.default()
    storePromotionController.fetchStorePromotionVisibility(forProduct: hiddenBeaches,
        completionHandler: { visibility: SKProductSTorePromotionVisiblity, error: Error?) in
            // visibility == .default
    })
    

### Override visibility settings

For each device, you can decide whether to make in-app purchases visible or
hidden. For example, you may want to hide products the customer already
purchased, and show only the products they can buy.

For example, to hide the Pro Subscription product after a user purchases it,
fetch the product information and update the store promotion controller with
the `.hide` setting, as the following code example shows. The Pro Subscription
promoted in-app purchase no longer appears in the App Store on the device.

    
    
    // Hide the promoted product Pro Subscription after the user purchases it.
    
    
    let storePromotionController = SKProductStorePromotionController.default()
    storePromotionController.update(storePromotionVisibility: .hide, for: proSubscription,
        completionHandler: { (error: Error?) in
            // Completion.
        })
    

### Override the order of promoted products

You can customize the promoted in-app purchases on each device by overriding
their default order. Use overrides to show promotions that are relevant to the
user. For example, you can override the order to promote an in-app purchase
that unlocks a level in your game when a user reaches the preceding level.

To override the promotion order, add the product information to an array in
the order they are to appear. Pass the array to the
`update(storePromotionOrder:completionHandler:)` method. The App Store
displays the products in the array, followed by the remaining promoted
products, which appear in the same relative order that you set in App Store
Connect.

    
    
    // Overriding the order of promoted in-app purchases.
    
    
    // Fetch product information for three products: Pro Subscription, Fishing Hot Spots, and Hidden Beaches.
    let storePromotionController = SKProductStorePromotionController.default()
    
    
    // Update the order.
    let newProductsOrder = [hiddenBeaches, proSubscription, fishingHotSpots]
    storePromotionController.updateStorePromotionOrder(newProductsOrder,
        completionHandler: { (error: Error?) in
            // Complete.
        })
    

### Cancel order overrides

To remove overrides and use the default promotion order, send an empty product
array to the `update(storePromotionOrder:completionHandler:)` method. The App
Store then displays the promoted in-app purchase products in the default order
that you set in App Store Connect.

### Fetch order overrides

To get the product promotion order for the device, call
`fetchStorePromotionOrder(completionHandler:)`. This method returns an array
of products that have an overridden order. If you get an empty array, there
aren’t any overrides and the products are in the default order.

    
    
    // Getting the order override of promoted in-app purchases.
    
    
    let storePromotionController = SKProductStorePromotionController.default()
    storePromotionController.fetchStorePromotionOrder(completionHandler: {
        (products: [SKProduct], error: Error?) in
            // products == [hiddenBeaches, proSubscription, fishingHotSpots]
        })
    

## See Also

### Promotions

Testing promoted in-app purchases

Test your in-app purchases before making your app available in the App Store.

`class SKProductStorePromotionController`

A product promotion controller for customizing the order and visibility of in-
app purchases per device.

Instance Method

# paymentQueue(_:shouldAddStorePayment:for:)

Tells the observer when a user initiates an in-app purchase from the App
Store.

iOS 11.0+  iPadOS 11.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 11.0+  visionOS
1.0+

    
    
    optional func paymentQueue(
        _ queue: SKPaymentQueue,
        shouldAddStorePayment payment: SKPayment,
        for product: SKProduct
    ) -> Bool

##  Parameters

`queue`

    

The payment queue the app uses to make the payment request.

`payment`

    

The payment request.

`product`

    

The in-app purchase product.

## Return Value

Return `true` to continue the transaction in your app.

Return `false` to defer or cancel the transaction.

If you return `false`, you can continue the transaction later by manually
adding the `SKPayment` `payment` to the `SKPaymentQueue` `queue`.

## Discussion

The system calls this delegate method when the user starts an in-app purchase
in the App Store, and the transaction continues in your app. Specifically, if
your app is already installed, StoreKit calls this method automatically.

If your app isn’t installed when the user starts the in-app purchase in the
App Store, the user receives a notification when the app installation is
complete. StoreKit calls this method when the user taps the notification.
Otherwise, if the user opens the app manually, StoreKit calls this method only
if they open the app soon after they initiate the purchase.

Important

To enable promoted in-app purchases, your app needs to use either
`PurchaseIntent` (starting in iOS 16.4) or
`paymentQueue(_:shouldAddStorePayment:for:)` (starting in iOS 11). Don’t use
both at the same time. If necessary, use conditional compilation to identify
the OS version the app is running in. For more information, see Running code
on a specific platform or OS version.

For more information, see Promoting in-app purchases.

## See Also

### Handling promoted in-app purchases

Promoting in-app purchases

Show promoted in-app purchases on your product page and handle purchases that
users initiate on the App Store.

Instance Method

# paymentQueue(_:didRevokeEntitlementsForProductIdentifiers:)

Tells an observer that the user is no longer entitled to one or more Family
Sharing purchases.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    optional func paymentQueue(
        _ queue: SKPaymentQueue,
        didRevokeEntitlementsForProductIdentifiers productIdentifiers: [String]
    )

##  Parameters

`queue`

    

The payment queue that calls the delegate method.

`productIdentifiers`

    

The list of product identifiers with revoked entitlements.

## Discussion

The system calls this delegate method whenever App Store revokes in-app
purchases for a family member based on changes in Family Sharing, or when the
purchaser gets a refund for an in-app purchase. Implement this method in your
payment queue observer to reestablish a user’s access to products. Revoked
transactions have the `cancellation_date` populated in the receipt.

For products with Family Sharing enabled, the following conditions may trigger
this method in the family member’s app:

  * The purchaser receives a refund for a non-consumable or an auto-renewable subscription they shared.

  * The purchaser leaves the family group in which they were sharing subscriptions or non-consumables.

  * The purchaser disables Family Sharing for a non-consumable or stops sharing a subscription.

  * The purchaser hides an app, which makes their non-consumable purchase unavailable for sharing.

  * The family member leaves the group and no longer gets access to shared purchases.

  * The family organizer stops sharing payment in iCloud family settings. This change affects non-consumables.

By leaving a family group, or disabling sharing in any of the ways listed
above, family members are no longer entitled to family-shared purchases. The
`productIdentifiers` parameter contains the revoked product IDs. Your app
needs to check the receipt on the device, which the system automatically
updates prior to calling this method, and provide the correct level of access
for the in-app purchases.

If you receive App Store Server Notifications, your server receives a
`notificationType` `REVOKE` for the family member when the conditions listed
above occur.

Important

Always check the receipt to determine the users’s correct level of access for
the product. A user may lose access through Family Sharing, but may have
purchased the product directly.

StoreKit also calls this method in the purchaser’s app when the purchaser
receives a refund for a non-consumable or an auto-renewable subscription,
regardless if the product is shared with the family. If you receive App Store
Server Notifications, your server receives a `notificationType` `REFUND` for
the purchaser.

If you use server-side receipt validation with the App Store, call your server
to reprocess the receipt and update your purchase records.

Instance Method

# paymentQueueDidChangeStorefront(_:)

Tells the observer that the storefront for the payment queue has changed.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.1+  tvOS 13.0+  watchOS
6.2+  visionOS 1.0+

    
    
    optional func paymentQueueDidChangeStorefront(_ queue: SKPaymentQueue)

## Discussion

See `SKStorefront` for more information.

Instance Method

# paymentQueue(_:updatedDownloads:)

Tells the observer that the payment queue has updated one or more download
objects.

iOS 6.0–16.0  Deprecated  iPadOS 6.0–16.0  Deprecated  macOS 10.8–13.0
Deprecated  Mac Catalyst 13.1–16.0  Deprecated  tvOS 9.0–16.0  Deprecated
watchOS 6.2–9.0  Deprecated

    
    
    optional func paymentQueue(
        _ queue: SKPaymentQueue,
        updatedDownloads downloads: [SKDownload]
    )

##  Parameters

`queue`

    

The payment queue that updated the downloads.

`downloads`

    

The download objects that were updated.

## Discussion

When a download object is updated, its `downloadState` property describes how
it changed.

