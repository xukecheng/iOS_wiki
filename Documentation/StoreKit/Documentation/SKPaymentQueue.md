Type Method

# canMakePayments()

A method that indicates whether the person can make purchases.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    class func canMakePayments() -> Bool

## Discussion

The Boolean value that this method returns is identical to the value of the
type property `canMakePayments` in the `AppStore` object. For more information
about using and interpreting this value, see the type property page
`canMakePayments`.

Instance Property

# storefront

The App Store storefront of the device.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.1+  tvOS 13.0+  watchOS
6.2+  visionOS 1.0+

    
    
    var storefront: SKStorefront? { get }

## Discussion

The storefront information tells you the device's App Store region. You can
use this information to display products that your app makes available in
specific regions. You maintain your own list of product identifiers and the
storefronts in which you make them available.

If the storefront changes during a transaction, StoreKit notifies your app by
calling the `paymentQueueDidChangeStorefront(_:)` method of the
`SKPaymentTransactionObserver` protocol. Implement
`paymentQueue(_:shouldContinue:in:)` to indicate whether the transaction
should continue with the new storefront.

Important

`storefront` is a synchronous API that may take significant time to return.
Don't use `storefront` in a time-sensitive thread, such as during app launch.
To get asynchronous behavior, dispatch it to a separate queue, or use the
asynchronous `current` property of `Storefront` instead.

Type Method

# default()

Returns the default payment queue instance.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    class func `default`() -> Self

## Return Value

The default payment queue.

## Discussion

Apps do not create a payment queue. Instead, they retrieve the queue by
calling this class method.

### Special Considerations

The payment queue is not available in Simulator. Attempting to retrieve the
payment queue logs a warning.

Instance Method

# add(_:)

Adds an observer to the payment queue.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    func add(_ observer: any SKPaymentTransactionObserver)

##  Parameters

`observer`

    

The observer to add to the queue.

## Discussion

Your application should add an observer to the payment queue during
application initialization. If there are no observers attached to the queue,
the payment queue does not synchronize its list of pending transactions with
the Apple App Store, because there is no observer to respond to updated
transactions.

If an application quits when transactions are still being processed, those
transactions are not lost. The next time the application launches, the payment
queue resumes processing the transactions. Your application should always
expect to be notified of completed transactions.

If more than one transaction observer is attached to the payment queue, no
guarantees are made as to the order which they will be called. It is safe for
multiple observers to call `finishTransaction(_:)`, but not recommended. It is
recommended that you use a single observer to process and finish the
transaction.

## See Also

### Adding, Getting, and Removing Observers

`var transactionObservers: [any SKPaymentTransactionObserver]`

An array of all active payment queue observers.

`func remove(any SKPaymentTransactionObserver)`

Removes an observer from the payment queue.

### Related Documentation

`var transactions: [SKPaymentTransaction]`

Returns an array of pending transactions.

Instance Property

# transactionObservers

An array of all active payment queue observers.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    var transactionObservers: [any SKPaymentTransactionObserver] { get }

## See Also

### Adding, Getting, and Removing Observers

`func add(any SKPaymentTransactionObserver)`

Adds an observer to the payment queue.

`func remove(any SKPaymentTransactionObserver)`

Removes an observer from the payment queue.

Instance Method

# remove(_:)

Removes an observer from the payment queue.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    func remove(_ observer: any SKPaymentTransactionObserver)

##  Parameters

`observer`

    

The observer to remove.

## Discussion

If there are no observers attached to the queue, the payment queue does not
synchronize its list of pending transactions with the Apple App Store, because
there is no observer to respond to updated transactions.

## See Also

### Adding, Getting, and Removing Observers

`func add(any SKPaymentTransactionObserver)`

Adds an observer to the payment queue.

`var transactionObservers: [any SKPaymentTransactionObserver]`

An array of all active payment queue observers.

### Related Documentation

`var transactions: [SKPaymentTransaction]`

Returns an array of pending transactions.

Instance Property

# delegate

A delegate that provides information needed to complete transactions.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.1+  tvOS 13.0+  watchOS
6.2+  visionOS 1.0+

    
    
    weak var delegate: (any SKPaymentQueueDelegate)? { get set }

## Discussion

This delegate implements the `SKPaymentQueueDelegate` protocol.

## See Also

### Managing Transactions

`var transactions: [SKPaymentTransaction]`

Returns an array of pending transactions.

`func add(SKPayment)`

Adds a payment request to the queue.

`func finishTransaction(SKPaymentTransaction)`

Notifies the App Store that the app finished processing the transaction.

Instance Property

# transactions

Returns an array of pending transactions.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    var transactions: [SKPaymentTransaction] { get }

## Discussion

The value of this property is undefined when there are no observers attached
to the payment queue.

## See Also

### Managing Transactions

`var delegate: (any SKPaymentQueueDelegate)?`

A delegate that provides information needed to complete transactions.

`func add(SKPayment)`

Adds a payment request to the queue.

`func finishTransaction(SKPaymentTransaction)`

Notifies the App Store that the app finished processing the transaction.

### Related Documentation

`func add(any SKPaymentTransactionObserver)`

Adds an observer to the payment queue.

Instance Method

# add(_:)

Adds a payment request to the queue.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    func add(_ payment: SKPayment)

##  Parameters

`payment`

    

A payment request.

## Discussion

An application should always have at least one observer of the payment queue
before adding payment requests.

The payment request must have a product identifier registered with the Apple
App Store and a quantity greater than `0`. If either property is invalid,
`add(_:)` throws an exception.

When a payment request is added to the queue, the payment queue processes that
request with the Apple App Store and arranges for payment from the user. When
that transaction is complete or if a failure occurs, the payment queue sends
the `SKPaymentTransaction` object that encapsulates the request to all
transaction observers.

## See Also

### Managing Transactions

`var delegate: (any SKPaymentQueueDelegate)?`

A delegate that provides information needed to complete transactions.

`var transactions: [SKPaymentTransaction]`

Returns an array of pending transactions.

`func finishTransaction(SKPaymentTransaction)`

Notifies the App Store that the app finished processing the transaction.

Instance Method

# finishTransaction(_:)

Notifies the App Store that the app finished processing the transaction.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    func finishTransaction(_ transaction: SKPaymentTransaction)

##  Parameters

`transaction`

    

The transaction to finish.

## Discussion

Transactions on the payment queue are persistent until they are completed.
StoreKit calls your observer’s `paymentQueue(_:updatedTransactions:)` method
every time your app launches or resumes from background to tell you about
transactions in the queue. After you've finished processing a transaction in
your app, always call the `finishTransaction(_:)` method to finish the
transaction and remove it from the queue.

Call `finishTransaction(_:)` only after the app has finished all work it
performs to complete the transaction. The transaction's state determines which
steps you might take:

  * For a failed transaction (`SKPaymentTransactionState.failed`), update your user interface, track information in analytics, and perform other similar tasks.

  * For a successful transaction (`SKPaymentTransactionState.purchased` or `SKPaymentTransactionState.restored`), perform all necessary actions to unlock the functionality the user has purchased before finishing the transaction. For example, if you are downloading content, finish the transaction only after the downloads are complete.

If you validate receipts, validate them before completing the transaction, and
take one of the paths described above.

In rare circumstances, this call might fail, and you'll receive updates for
that transaction again. For this reason, you should record information in your
app about the transactions it has processed and which steps the app has
already completed. That way, you don't repeat steps that shouldn't be
performed multiple times. For example, if you are processing a consumable
transaction, you only want to add the consumable benefit once.

If you call `finishTransaction(_:)` on a transaction that is in the
`SKPaymentTransactionState.purchasing` state, StoreKit raises an exception.

## See Also

### Managing Transactions

`var delegate: (any SKPaymentQueueDelegate)?`

A delegate that provides information needed to complete transactions.

`var transactions: [SKPaymentTransaction]`

Returns an array of pending transactions.

`func add(SKPayment)`

Adds a payment request to the queue.

### Related Documentation

`func paymentQueue(SKPaymentQueue, updatedTransactions:
[SKPaymentTransaction])`

Tells an observer that one or more transactions have been updated.

Instance Method

# restoreCompletedTransactions()

Asks the payment queue to restore previously completed purchases.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    func restoreCompletedTransactions()

## Discussion

Use this method to restore finished transactions—that is, transactions for
which you have already called `finishTransaction(_:)`. You call this method in
one of the following situations:

  * To install purchases on additional devices

  * To restore purchases for an application that the user deleted and reinstalled

When you create a new product to be sold in your store, you choose whether
that product can be restored or not. See the In-App Purchase Programming Guide
for more information.

The payment queue delivers a new transaction for each previously completed
transaction that can be restored. Each transaction includes a copy of the
original transaction.

After the transactions are delivered, the payment queue calls the observer’s
`paymentQueueRestoreCompletedTransactionsFinished(_:)` method. If an error
occurred while restoring transactions, the observer will be notified through
its `paymentQueue(_:restoreCompletedTransactionsFailedWithError:)` method.

This method has no effect in the following situations:

  * All transactions are unfinished.

  * The user did not purchase anything that is restorable.

  * You tried to restore items that are not restorable, such as a non-renewing subscription or a consumable product.

  * Your app's build version does not meet the guidelines for the `CFBundleVersion` key.

Important

If you are using the In-App Purchase API and managing transactions using the
`Transaction` API, use `currentEntitlements` to determine which in-app
purchases the customer is currently entitled to. The
`restoreCompletedTransactions()` function doesn't affect transactions in the
`Transaction` API. In rare cases when a user suspects the app isn’t showing
all the transactions, call `sync()` in response to an explicit user action,
like tapping a button.

## See Also

### Restoring Purchases

`func restoreCompletedTransactions(withApplicationUsername: String?)`

Asks the payment queue to restore previously completed purchases, providing an
opaque identifier for the user’s account.

Instance Method

# restoreCompletedTransactions(withApplicationUsername:)

Asks the payment queue to restore previously completed purchases, providing an
opaque identifier for the user’s account.

iOS 7.0+  iPadOS 7.0+  macOS 10.9+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    func restoreCompletedTransactions(withApplicationUsername username: String?)

##  Parameters

`username`

    

An opaque identifier for the user’s account on your system.

## See Also

### Restoring Purchases

`func restoreCompletedTransactions()`

Asks the payment queue to restore previously completed purchases.

### Related Documentation

`var applicationUsername: String?`

A string that associates the transaction with a user account on your service.

Instance Method

# showPriceConsentIfNeeded()

Asks the system to display the price consent sheet if the user hasn’t yet
responded to a subscription price increase.

iOS 13.4+  iPadOS 13.4+  Mac Catalyst 13.4+  visionOS 1.0+

    
    
    func showPriceConsentIfNeeded()

## Discussion

Call this method if the system called your delegate’s
`paymentQueueShouldShowPriceConsent(_:)` method, and you chose to delay
showing the price consent sheet.

This function displays the price consent sheet if both of the following are
true:

  * You’ve increased the price of the subscription in App Store Connect.

  * The subscriber hasn’t yet responded to a price consent query.

Otherwise, this function has no effect.

Note

When you increase the price of a subscription, Apple informs affected
subscribers through an email, push notification, and in-app price consent
sheet and asks them to agree to the new price. If they don’t agree or take no
action, their subscription expires at the end of their current billing cycle.
For more information, see Managing Prices and Manage pricing for auto-
renewable subscriptions.

In Mac apps built with Mac Catalyst, this function has no effect.

## See Also

### Related Documentation

`func paymentQueueShouldShowPriceConsent(SKPaymentQueue) -> Bool`

Asks the delegate whether to immediately display a price consent sheet.

Instance Method

# presentCodeRedemptionSheet()

Displays a sheet that enables users to redeem subscription offer codes that
you configure in App Store Connect.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    func presentCodeRedemptionSheet()

## Discussion

The `presentCodeRedemptionSheet()` function displays a system sheet where
customers can enter and redeem subscription offer codes. If you generate
subscription offer codes in App Store Connect, call this function to enable
users to redeem the offer.

Note

For apps with more than one scene, and on iOS 16 or later and iPadOS 16 or
later, use `offerCodeRedemption(isPresented:onCompletion:)` or
`presentOfferCodeRedeemSheet(in:)` instead.

When your app calls `presentCodeRedemptionSheet()`, the system determines
where to display the screen. Use `presentCodeRedemptionSheet()` to support
devices running iOS 14 through iOS 15, and iPadOS 14 through iPadOS 15.

For information on implementing subscription offer codes, see Implementing
offer codes in your app.

Important

Set up subscription offer codes in App Store Connect before calling this API.
Customers can only redeem these offers in your app through the redemption
sheet; don’t use a custom UI. For information on configuring and generating
subscription offer codes, see Set up offer codes.

This method applies to subscription offer codes only; it doesn’t apply to
promo codes for apps or in-app purchases. For more information on promo codes,
see Request and manage promo codes.

This function doesn’t affect Mac apps built with Mac Catalyst.

Instance Method

# start(_:)

Adds a set of downloads to the download list.

iOS 6.0–16.0  Deprecated  iPadOS 6.0–16.0  Deprecated  macOS 10.8–13.0
Deprecated  Mac Catalyst 13.1–16.0  Deprecated  tvOS 9.0–16.0  Deprecated
watchOS 6.2–9.0  Deprecated

    
    
    func start(_ downloads: [SKDownload])

##  Parameters

`downloads`

    

An array of `SKDownload` objects to begin downloading.

## Discussion

In order for a download object to be queued, it must be associated with a
transaction that has been successfully purchased, but not yet finished.

## See Also

### Downloading Content

`func cancel([SKDownload])`

Removes a set of downloads from the download list.

Deprecated

`func pause([SKDownload])`

Pauses a set of downloads.

Deprecated

`func resume([SKDownload])`

Resumes a set of downloads.

Deprecated

Instance Method

# cancel(_:)

Removes a set of downloads from the download list.

iOS 6.0–16.0  Deprecated  iPadOS 6.0–16.0  Deprecated  macOS 10.8–13.0
Deprecated  Mac Catalyst 13.1–16.0  Deprecated  tvOS 9.0–16.0  Deprecated
watchOS 6.2–9.0  Deprecated

    
    
    func cancel(_ downloads: [SKDownload])

##  Parameters

`downloads`

    

An array of `SKDownload` objects to cancel.

## See Also

### Downloading Content

`func start([SKDownload])`

Adds a set of downloads to the download list.

Deprecated

`func pause([SKDownload])`

Pauses a set of downloads.

Deprecated

`func resume([SKDownload])`

Resumes a set of downloads.

Deprecated

Instance Method

# pause(_:)

Pauses a set of downloads.

iOS 6.0–16.0  Deprecated  iPadOS 6.0–16.0  Deprecated  macOS 10.8–13.0
Deprecated  Mac Catalyst 13.1–16.0  Deprecated  tvOS 9.0–16.0  Deprecated
watchOS 6.2–9.0  Deprecated

    
    
    func pause(_ downloads: [SKDownload])

##  Parameters

`downloads`

    

An array of `SKDownload` objects to pause.

## See Also

### Downloading Content

`func start([SKDownload])`

Adds a set of downloads to the download list.

Deprecated

`func cancel([SKDownload])`

Removes a set of downloads from the download list.

Deprecated

`func resume([SKDownload])`

Resumes a set of downloads.

Deprecated

Instance Method

# resume(_:)

Resumes a set of downloads.

iOS 6.0–16.0  Deprecated  iPadOS 6.0–16.0  Deprecated  macOS 10.8–13.0
Deprecated  Mac Catalyst 13.1–16.0  Deprecated  tvOS 9.0–16.0  Deprecated
watchOS 6.2–9.0  Deprecated

    
    
    func resume(_ downloads: [SKDownload])

##  Parameters

`downloads`

    

An array of `SKDownload` objects to resume.

## See Also

### Downloading Content

`func start([SKDownload])`

Adds a set of downloads to the download list.

Deprecated

`func cancel([SKDownload])`

Removes a set of downloads from the download list.

Deprecated

`func pause([SKDownload])`

Pauses a set of downloads.

Deprecated

