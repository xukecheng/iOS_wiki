Article

# Setting up the transaction observer for the payment queue

Enable your app to receive and handle transactions by adding an observer.

## Overview

To process transactions in your app, you need to create and add an observer to
the payment queue. The observer object responds to new transactions and
synchronizes the queue of pending transactions with the App Store, and the
payment queue prompts users to authorize payment. It’s important to add the
transaction observer at app launch to ensure you don't miss payment queue
notifications that the system may send when the app launches.

### Create an observer

Create and build a custom observer class to handle changes to the payment
queue.

Create an instance of this observer class to act as the observer of changes to
the payment queue.

Tip

Consider creating your observer as a shared instance of the class for global
reference in any other class. A shared instance also ensures the lifetime of
the object, so that the same instance handles callbacks for the
`SKPaymentTransactionObserver` protocol.

After you create the transaction observer, you can add it to the payment
queue.

### Add an observer

StoreKit attaches your observer to the queue when your app calls.

StoreKit can notify your `SKPaymentTransactionObserver` instance automatically
when the content of the payment queue changes upon resuming or while running
your app.

Implement the transaction observer.

It’s important to add the observer at launch, in
`application(_:didFinishLaunchingWithOptions:)`, to ensure that it persists
during all launches of your app, receives all payment queue notifications, and
continues transactions that may initiate outside the app, such as:

  * Promoted in-app purchases. For more information, see Promoting in-app purchases.

  * Background subscription renewals

  * Interrupted purchases

The observer needs to be persistent so the system doesn't deallocate it when
it sends the app to the background. Only a persistent observer can receive
transactions that may occur while your app is in the background, such as a
renewal transaction for an auto-renewable subscription.

## See Also

### Essentials

Offering, completing, and restoring in-app purchases

Fetch, display, purchase, validate, and finish transactions in your app.

`class SKPaymentQueue`

A queue of payment transactions for the App Store to process.

`protocol SKPaymentTransactionObserver`

A set of methods that process transactions, unlock purchased functionality,
and continue promoted in-app purchases.

`protocol SKPaymentQueueDelegate`

The protocol that provides information needed to complete transactions.

`class SKRequest`

An abstract class that represents a request to the App Store.

### Related Documentation

`func add(any SKPaymentTransactionObserver)`

Adds an observer to the payment queue.

Article

# Loading in-app product identifiers

Load the unique identifiers for your in-app products to retrieve product
information from the App Store.

## Overview

Implementing an in-app purchase flow consists of three stages. In the first
stage, your app retrieves product information. Then your app requests payment
when the user selects a product in your app’s store. Finally, your app
delivers the product.

To begin the purchase process, your app needs the product identifiers so it
can retrieve information about the products from the App Store and present its
store UI to the user. Every product you sell in your app has a unique product
identifier. You provide this value in App Store Connect when you create a new
in-app purchase product (see Create in-app purchases for more information).
Your app uses these product identifiers to fetch information about products
available for sale in the App Store, such as pricing, and to submit payment
requests when users purchase those products.

There are several strategies for storing a list of product identifiers in your
app, such as embedding them in the app bundle or storing them on your server.
You can then retrieve the product identifiers by reading them locally in the
app bundle or fetching them from your server. Choose the method that best
serves your app’s needs.

Note

There’s no runtime mechanism to fetch a list of the configured products in App
Store Connect for a particular app. You’re responsible for managing your app’s
list of products and providing that information to your app.

### Retrieve product IDs from the app bundle

Embed the product identifiers in your app bundle if:

  * Your app has a fixed list of in-app purchase products. For example, apps with an in-app purchase to remove ads or unlock functionality can embed the product identifier list in the app bundle.

  * You expect users to update the app to see new in-app purchase products.

  * The app or product doesn’t require a server.

Include a property list file in your app bundle containing an array of product
identifiers, such as the following:

    
    
    <?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
     "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
    <plist version="1.0">
    <array>
        <string>com.example.level1</string>
        <string>com.example.level2</string>
        <string>com.example.rocket_car</string>
    </array>
    </plist>
    

To get product identifiers from the property list, locate the file in the app
bundle and read it.

### Retrieve product IDs from your server

Store the product identifiers on your server if:

  * You update the list of in-app products frequently, without updating your app. For example, games that support additional levels or characters can fetch the product identifiers list from your server.

  * The products consist of delivered content.

  * Your app or product requires a server.

Host a JSON file on your server with the product identifiers. For example, the
following JSON file contains three product IDs:

    
    
    [
        "com.example.level1",
        "com.example.level2",
        "com.example.rocket_car"
    ]
    

To get product identifiers from your server, fetch and read the JSON file.

Consider versioning the JSON file so future versions of your app can change
its structure without breaking older versions of your app. For example, you
might name the file that uses the old structure `products_v1.json` and the
file that uses a new structure `products_v2.json`. This is especially useful
if your JSON file is more complex than the simple array in the example.

To ensure that your app remains responsive, use a background thread to
download the JSON file and extract the list of product identifiers. To
minimize the data that transfers, use standard HTTP caching mechanisms, such
as the `Last-Modified` and `If-Modified-Since` headers.

After loading all in-app product identifiers, pass them into the product
information request to the App Store. For details on obtaining product
information, see Fetching product information from the App Store.

## See Also

### Product information

Fetching product information from the App Store

Retrieve up-to-date information about the products for sale in your app to
display to your customers.

`class SKProductsRequest`

An object that can retrieve localized information from the App Store about a
specified list of products.

`class SKProductsResponse`

An App Store response to a request for information about a list of products.

`class SKProduct`

Information about a registered product in App Store Connect.

Article

# Fetching product information from the App Store

Retrieve up-to-date information about the products for sale in your app to
display to your customers.

## Overview

To ensure your customers see only products that are available for them to
purchase, query the App Store before displaying your app’s store UI. Compare
the App Store’s list of product identifiers to your local product identifiers.
To retrieve a list of your app’s product identifiers, see Loading in-app
product identifiers.

### Request product information

To query the App Store, create an `SKProductsRequest` and initialize it with a
list of your product identifiers. Keep a strong reference to the request
object; otherwise, the system might deallocate the request before it can
complete.

The products request retrieves information about valid products, along with a
list of invalid product identifiers, and then calls its delegate to process
the result. The delegate needs to implement the `SKProductsRequestDelegate`
protocol to handle the response from the App Store. Here’s a simple
implementation of both pieces of code:

Keep a reference to the array of `SKProduct` objects that the delegate
receives. Use these same product objects to create a payment request when a
user purchases a product.

If the list of products you sell in your app is subject to change, such as
when you add or remove a product from sale, consider creating a custom class
that encapsulates a reference to the product object along with other
information, such as pictures or descriptions that you fetch from your server.
For more information on payment requests, see Requesting a payment from the
App Store.

### Troubleshoot invalid product IDs

Invalid product identifiers in the App Store response to your products request
usually indicate an error in your app’s list of product identifiers. Invalid
product identifiers may also indicate an incorrectly configured product in App
Store Connect. Actionable UI and insightful logging can help you resolve this
type of issue, as follows:

  * In production builds, display your app’s store UI and omit the invalid product.

  * In development builds, display an error to call attention to the issue. 

  * In both production and development builds, use `NSLog` to write a message to the console to record the invalid identifier.

  * If your app fetches the list from your server, you can define a logging mechanism to let your app send the list of invalid identifiers back to your server.

  * Verify that you have a signed Paid Applications Agreement for your developer account. For more information about this agreement, see Sign and update agreements.

For more information about troubleshooting invalid product identifiers, see
`invalidProductIdentifiers`.

## See Also

### Product information

Loading in-app product identifiers

Load the unique identifiers for your in-app products to retrieve product
information from the App Store.

`class SKProductsRequest`

An object that can retrieve localized information from the App Store about a
specified list of products.

`class SKProductsResponse`

An App Store response to a request for information about a list of products.

`class SKProduct`

Information about a registered product in App Store Connect.

Article

# Requesting a payment from the App Store

Submit a payment request to the App Store when a user selects a product to
buy.

## Overview

After you present your app’s store UI, users can make purchases from within
your app. When the user chooses a product, your app creates and submits a
payment request to the App Store.

Implementing an in-app purchase flow consists of three stages. In the first
stage, your app retrieves product information. Then your app requests payment
when the user selects a product in your app’s store. Finally, your app
delivers the products.

### Create a payment request

When the user selects a product to buy, create a payment request using the
corresponding `SKProduct` object and set the quantity if needed, as the code
below shows. The product object comes from the array of products that your
app’s products request returns, as described in Fetching product information
from the App Store.

### Submit a payment request

Submit your payment request to the App Store by adding it to the payment
queue. If you add a payment object to the queue more than once, the system
submits it to the App Store multiple times, charging the user and requiring
your app to deliver the product each time.

For each payment request your app submits, it receives a corresponding
transaction to process. For more information about transactions and the
payment queue, see Processing a transaction.

For auto-renewable subscriptions, you may submit a payment request with a
subscription offer for users you determine eligible to receive an offer. For
more information, see Implementing promotional offers in your app.

## See Also

### Purchases

Processing a transaction

Register a transaction queue observer to get and handle transaction updates
from the App Store.

`class SKPayment`

A request to the App Store to process payment for additional functionality
that your app offers.

`class SKMutablePayment`

A mutable request to the App Store to process payment for additional
functionality that your app offers.

`class SKPaymentTransaction`

An object in the payment queue.

Article

# Processing a transaction

Register a transaction queue observer to get and handle transaction updates
from the App Store.

## Overview

Implementing an in-app purchase flow consists of three stages. In the first
stage, your app retrieves product information. Then your app requests payment
when the user selects a product in your app’s store. Finally, your app
delivers the product.

The App Store calls the transaction queue observer after it processes the
payment request. Your app then records information about the purchase for
future launches, downloads the purchased content, and marks the transaction as
finished.

### Monitor transactions in the queue

The transaction queue plays a central role in letting your app communicate
with the App Store through the StoreKit framework. You add work to the queue
that the App Store needs to act on, such as a payment request for processing.
When the transaction’s state changes, such as when a payment request succeeds,
StoreKit calls the app’s transaction queue observer. You decide which class
acts as the observer. In very small apps, you might handle all the StoreKit
logic in the app delegate, including observing the transaction queue. In most
apps, however, you create a separate class that handles this observer logic,
along with the rest of your app’s store logic. The observer needs to conform
to the `SKPaymentTransactionObserver` protocol.

By adding an observer, your app doesn’t need to constantly poll the status of
its active transactions. Your app uses the transaction queue for payment
requests, to download Apple-hosted content, and to determine when
subscriptions renew.

It’s important to register a transaction queue observer as soon as your app
launches, as the code shows below. For more guidance, see Setting up the
transaction observer for the payment queue.

Make sure that the observer is ready to handle a transaction at any time, not
only after you add a transaction to the queue. For example, if a user buys
something in your app just before entering a tunnel, your app may not be able
to deliver the purchased content if there isn't a network connection. The next
time your app launches, StoreKit calls your transaction queue observer again
so your app can handle the transaction and deliver the purchased content.
Similarly, if your app fails to mark a transaction as finished, StoreKit calls
the observer every time your app launches until the transaction finishes.

Implement the `paymentQueue(_:updatedTransactions:)` method on your
transaction queue observer. StoreKit calls this method when the status of a
transaction changes, such as when a payment request has been processed. The
transaction status tells you what action your app needs to perform, as
described in the table below:

Status| Action to take in your app  
---|---  
`SKPaymentTransactionState.purchasing`| Update your UI to reflect the in-
progress status, and wait for StoreKit to call the method again.  
`SKPaymentTransactionState.deferred`| Update your UI to reflect the deferred
status, and wait for StoreKit to call the method again.  
`SKPaymentTransactionState.failed`| Use the value of the `error` property to
present a message to the user. For a list of error constants, see
`SKErrorDomain`.  
`SKPaymentTransactionState.purchased`| Provide the purchased functionality,
typically by unlocking features or delivering content.  
`SKPaymentTransactionState.restored`| Restore the previously purchased
functionality.  
  
Transactions in the queue can change state in any order. Your app needs to be
ready to work on any active transaction at any time. Act on every transaction
according to its transaction state, as in this example:

### Update the app's UI to reflect transaction changes

To keep your user interface up to date while waiting, the transaction queue
observer can implement optional methods from the
`SKPaymentTransactionObserver` protocol as follows:

  * StoreKit calls the `paymentQueue(_:removedTransactions:)` method when it removes transactions from the queue. In your implementation of this method, remove the corresponding items from your app’s UI. 

  * StoreKit calls the `paymentQueueRestoreCompletedTransactionsFinished(_:)` or `paymentQueue(_:restoreCompletedTransactionsFailedWithError:)` methods when it finishes restoring transactions, depending on whether there is an error. In your implementation of these methods, update your app’s UI to reflect the success or failure.

For successfully processed transactions, validate the receipt associated with
the transaction to verify the items the user purchased, and unlock content
accordingly. For more information on validating receipts serverside, see
Validating receipts with the App Store.

## See Also

### Purchases

Requesting a payment from the App Store

Submit a payment request to the App Store when a user selects a product to
buy.

`class SKPayment`

A request to the App Store to process payment for additional functionality
that your app offers.

`class SKMutablePayment`

A mutable request to the App Store to process payment for additional
functionality that your app offers.

`class SKPaymentTransaction`

An object in the payment queue.

Article

# Choosing a receipt validation technique

Select the type of receipt validation, on the device or on your server, that
works for your app.

## Overview

Note

The receipt isn’t necessary if you use `AppTransaction` to validate the app
download, or `Transaction` to validate in-app purchases. Only use the receipt
if your app uses the Original API for in-app purchase, or needs the receipt to
validate the app download because it can’t use `AppTransaction`.

An App Store receipt provides a record of the sale of an app and any purchases
the person makes within the app. You can authenticate purchased content by
adding receipt validation code to your app or server. Receipt validation
requires an understanding of secure coding techniques to employ a solution
that’s secure and unique to your app.

### Choose a validation technique

There are two ways to verify a receipt’s authenticity:

  * Locally, on the device. Validating receipts locally requires code that reads and validates a binary file that Apple encodes and signs as a PKCS #7 container. For more information, see Validating receipts on the device. 

  * On your server with the App Store. Validating receipts with the App Store requires secure connections between your app and your server, and between your server and the App Store. For more information, see Validating receipts with the App Store.

Compare the approaches and determine the method that best fits your app and
your infrastructure. You can also choose to implement both approaches. For
managing auto-renewable subscriptions, see the following table for the key
advantages that server-side receipt validation provides over on-device receipt
validation:

Capability| On-device validation| Server-side validation  
---|---|---  
Validates authenticity of receipt| Yes| Yes  
Includes subscription renewal transactions| Yes| Yes  
Includes additional subscription information| No| Yes  
Resistant to device clock change| No| Yes  
  
Receipts contain non-consumable in-app purchases, auto-renewable
subscriptions, and non-renewing subscriptions indefinitely. Consumable in-app
purchases remain in the receipt until you call `finishTransaction(_:)`. You
may choose to maintain and manage records of consumable in-app purchases on
your server.

### Get the latest receipt

The App Store updates receipts immediately after completed purchases. When you
call verifyReceipt from your server, the App Store returns the latest
transaction information, regardless of the contents of the receipt you send in
the request.

On the device, the system updates the receipt immediately when it has an
internet connection, and any of the following occur:

  * The customer completes an in-app purchase.

  * The app launches its transaction observer (`SKPaymentTransactionObserver`) and has unfinished transactions or subscription renewals.

  * The app calls `restoreCompletedTransactions()` or `restoreCompletedTransactions(withApplicationUsername:)` to restore transactions.

  * The app sends a request to `SKReceiptRefreshRequest` to get a receipt if the receipt is invalid or missing.

Transactions can also occur at times when the app isn’t running. When
necessary, call `restoreCompletedTransactions()` to ensure the receipt you’re
working with is up-to-date. For example, if a customer purchases an auto-
renewable subscription on another device, call this method to get those
transactions and update the receipt.

To ensure that your app receives all transactions, add the transaction
observer, `add(_:)`, at app launch time. For more information, see Setting up
the transaction observer for the payment queue.

Related Sessions from WWDC 2018

Session 705: Engineering Subscriptions

## See Also

### Purchase validation

Validating receipts with the App Store

Verify transactions with the App Store on a secure server.

`var appStoreReceiptURL: URL?`

The file URL for the bundle’s App Store receipt.

`class SKReceiptRefreshRequest`

A request to the App Store to get the app receipt, which represents the user’s
transactions with your app.

Article

# Validating receipts with the App Store

Verify transactions with the App Store on a secure server.

## Overview

Important

The verifyReceipt endpoint is deprecated. To validate receipts on your server,
follow the steps in Validating receipts on the device on your server. To
validate in-app purchases on your server without using receipts, call the App
Store Server API to get Apple-signed transaction and subscription information
for your customers, or verify the `AppTransaction` and `Transaction` signed
data that your app obtains. You can also get the same signed transaction and
subscription information from the App Store Server Notifications V2.

An App Store receipt is a binary encrypted file signed with an Apple
certificate. To read the contents of the encrypted file, you need to pass it
through the verifyReceipt endpoint. The endpoint’s response includes a
readable JSON body. Communication with the App Store is structured as JSON
dictionaries, as defined in RFC 4627. Binary data is Base64-encoded, as
defined in RFC 4648. Validate receipts with the App Store through a secure
server. For information on establishing a secure network connection with the
App Store, see Preventing Insecure Network Connections.

Warning

Don’t call the App Store server verifyReceipt endpoint from your app. You
can’t build a trusted connection between a user’s device and the App Store
directly because you don’t control either end of that connection, which makes
it susceptible to a machine-in-the-middle attack.

### Fetch the receipt data

The app receipt is always present in the production environment on devices
running macOS, iOS, and iPadOS. The app receipt is also always present in
TestFlight on devices running macOS. In the sandbox environment and in
StoreKit Testing in Xcode, the app receipt is present only after the tester
makes the first in-app purchase. If the app calls `SKReceiptRefreshRequest` or
`restoreCompletedTransactions()`, the app receipt is present only if the app
has at least one in-app purchase.

To retrieve the receipt data from the app on the device, use the
`appStoreReceiptURL` method of `Bundle` to locate the app’s receipt, and
encode the data in Base64. Send this Base64-encoded data to your server.

### Send the receipt data to the App Store

On your server, create a JSON object with the `receipt-data`, `password`, and
`exclude-old-transactions` keys detailed in `requestBody`.

Submit this JSON object as the payload of an HTTP POST request. Use the test
environment URL `https://sandbox.itunes.apple.com/verifyReceipt` when testing
your app in the sandbox and while your app is in review. Use the production
URL `https://buy.itunes.apple.com/verifyReceipt` when your app is live in the
App Store. For more information, see verifyReceipt.

Important

Verify your receipt first with the production URL; then verify with the
sandbox URL if you receive a `21007` status code. This approach ensures you
don’t have to switch between URLs while your app is in testing, in review by
App Review, or live in the App Store.

### Parse the response

The App Store’s response payload is a JSON object that contains the keys and
values detailed in `responseBody`.

The `in_app` array contains the non-consumable, non-renewing subscription, and
auto-renewable subscription items that the user previously purchased. Check
the values in the response for these in-app purchase types to verify
transactions as needed.

For auto-renewable subscription items, parse the response to get information
about the currently active subscription period. When you validate the receipt
for a subscription, `latest_receipt` contains the latest encoded receipt,
which is the same as the value for `receipt-data` in the request, and
`latest_receipt_info` contains all the transactions for the subscription,
including the initial purchase and subsequent renewals, but not including any
restores.

You can use these values to check whether an auto-renewable subscription has
expired. Use these values along with the `expiration_intent` subscription
field to get the reason for expiration.

## See Also

### Purchase validation

Choosing a receipt validation technique

Select the type of receipt validation, on the device or on your server, that
works for your app.

`var appStoreReceiptURL: URL?`

The file URL for the bundle’s App Store receipt.

`class SKReceiptRefreshRequest`

A request to the App Store to get the app receipt, which represents the user’s
transactions with your app.

### Related Documentation

App Store Receipts

Validate app and in-app purchase receipts with the App Store.

Instance Property

# appStoreReceiptURL

The file URL for the bundle’s App Store receipt.

iOS 7.0+  iPadOS 7.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var appStoreReceiptURL: URL? { get }

## Discussion

Note

The receipt isn’t necessary if you use `AppTransaction` to validate the app
download, or `Transaction` to validate in-app purchases. Only use the receipt
if your app uses the Original API for in-app purchase, or needs the receipt to
validate the app download because it can’t use `AppTransaction`.

Use this app bundle property to locate the app receipt if it's present; this
property is `nil` if the receipt isn’t present. In the rare case a receipt is
invalid or missing in an app that a user downloads from the App Store, use
`SKReceiptRefreshRequest` to request a new receipt. For information about
validating receipts, see Choosing a receipt validation technique.

You can’t use the general best practice of weak linking using the
`responds(to:)` method here; the method’s implementation uses the
`doesNotRecognizeSelector(_:)` method.

### Get the receipt in testing environments

Receipts aren't initially present in iOS and iPadOS apps in the sandbox
environment and in Xcode. Apps get a receipt after the tester completes the
first in-app purchase. When your app checks `appStoreReceiptURL` and finds
that it’s `nil`, assume the tester is a new customer and has no access to
premium content. For Mac apps running in TestFlight, the receipt is always
present.

## See Also

### Getting the Standard Bundle Directories

`var resourceURL: URL?`

The file URL of the bundle’s subdirectory containing resource files.

`var executableURL: URL?`

The file URL of the receiver's executable file.

`var privateFrameworksURL: URL?`

The file URL of the bundle’s subdirectory containing private frameworks.

`var sharedFrameworksURL: URL?`

The file URL of the receiver's subdirectory containing shared frameworks.

`var builtInPlugInsURL: URL?`

The file URL of the receiver's subdirectory containing plug-ins.

`func url(forAuxiliaryExecutable: String) -> URL?`

Returns the file URL of the executable with the specified name in the
receiver’s bundle.

`var sharedSupportURL: URL?`

The file URL of the bundle’s subdirectory containing shared support files.

`var resourcePath: String?`

The full pathname of the bundle’s subdirectory containing resources.

`var executablePath: String?`

The full pathname of the receiver's executable file.

`var privateFrameworksPath: String?`

The full pathname of the bundle’s subdirectory containing private frameworks.

`var sharedFrameworksPath: String?`

The full pathname of the bundle’s subdirectory containing shared frameworks.

`var builtInPlugInsPath: String?`

The full pathname of the receiver's subdirectory containing plug-ins.

`func path(forAuxiliaryExecutable: String) -> String?`

Returns the full pathname of the executable with the specified name in the
receiver’s bundle.

`var sharedSupportPath: String?`

The full pathname of the bundle’s subdirectory containing shared support
files.

Article

# Unlocking purchased content

Deliver content to the user after validating the purchase.

## Overview

After a purchase is complete, it’s your responsibility to make sure that you
programmatically make the content available to the user.

### Identify the purchased content

For an in-app purchase product that enables app functionality, such as a
premium subscription, set a Boolean value to enable the code path and update
your user interface as needed. Consult your app's persistent transaction
record to determine the functionality to unlock. Your app needs to update this
Boolean value whenever the user completes a purchase and at app launch. For
information on making a persistent record, see Persisting a purchase.

For example, using the app receipt, your code might look like the following:

Or, using the user defaults system.

After you define the Boolean variable that represents the in-app purchase
content, use the purchase information to enable the appropriate code paths in
your app.

### Deliver associated content

Your app needs to deliver any content associated with the purchased product to
the user. For example, purchasing instruments in a music app requires
delivering the sound files needed to let the user play those instruments. You
can embed that content in your app bundle or download it as necessary. Each
approach has its advantages and disadvantages.

Embed smaller files (up to a few megabytes) in your app, especially if you
expect most users to buy that product. You can make the content in your app
bundle available immediately after the user purchases it. However, to add or
update content in your app bundle, you need to submit an updated version of
your app.

Download larger files only when needed. Separating content from your app
bundle keeps your app’s initial download small. For example, a game can
include the first level in its app bundle and let users download additional
levels as they purchase them. Assuming your app fetches its list of product
identifiers from your server and the information isn’t hard-coded in the app
bundle, you don’t need to resubmit your app to add or update content that your
app downloads.

Note

You can’t patch your app binary or download executable code. Your app needs to
contain all executable code necessary to support all of its functionality when
you submit it. If a new product requires code changes, submit an updated
version of your app.

### Load local content

Load local content using the `NSBundle` class as you load other resources from
your app bundle.

### Download content from your own server

As with all interactions between your app and your server, the details and
process of downloading content from your own server are your responsibility.
The communication consists of, at a minimum, the following steps:

  1. Your app sends the receipt to your server and requests the content.

  2. Your server validates the receipt to establish that the user purchased the content, as described in Validating receipts with the App Store.

  3. Assuming the receipt is valid, your server responds to your app with the content.

Ensure that your app handles errors gracefully. For example, if the device
runs out of disk space during a download, give the user the option to discard
the partial download or to resume the download later when space becomes
available.

Consider the security implications of how you host your content and how your
app communicates with your server. For more information, see Security
Overview.

### Download content using on-demand resources

You can use On-Demand Resources (ODR) for flexibility in downloading data in
your app. ODR is an Apple-hosted service you use to store in-app purchase data
that your app downloads after you verify the user’s purchase using the app
receipt. ODR doesn’t require a call to restore transactions and authenticate
the user to download content hosted on Apple’s server.

### Download hosted content from Apple’s server

Important

`SKDownload` and its related functionality are deprecated. The following
information is for apps that already host content on Apple’s servers and use
`SKDownload`.

Apps can use Apple-hosted content for downloaded files. You create an Apple-
hosted content bundle using the In-App Purchase Content target in Xcode and
submit it to App Store Connect. Apple’s servers store your app’s content using
the same infrastructure that supports other large-scale operations, such as
the App Store. Apple-hosted content automatically downloads in the background
even if your app isn’t running.

If you need to support older versions of iOS or share your server
infrastructure across multiple platforms, you may choose to host your own
content using your own server infrastructure.

When the user purchases a product that has associated Apple-hosted content,
the transaction that passes to your transaction queue observer also includes
an instance of `SKDownload` that lets you download the associated content.

To download the content, add the download objects from the transaction’s
`downloads` property to the transaction queue by calling the `start(_:)`
method of `SKPaymentQueue`. If the value of the `downloads` property is `nil`,
there’s no Apple-hosted content for that transaction. Unlike downloading apps,
downloading content doesn’t automatically require a Wi-Fi connection for
content larger than a certain size. Avoid using cellular networks to download
large files without an explicit action from the user.

Implement the `paymentQueue(_:updatedDownloads:)` method on the transaction
queue observer to respond to changes in a download’s state, such as by
updating progress in your UI. If a download fails, use the information in its
`error` property to present the error to the user.

Ensure that your app handles errors gracefully. For example, if the device
runs out of disk space during a download, give the user the option to discard
the partial download or to resume the download later when space becomes
available.

While the content is downloading, update your user interface using the values
of the `progress` and `timeRemaining` properties. You can use the `pause(_:)`,
`resume(_:)`, and `cancel(_:)` methods of `SKPaymentQueue` from your UI to let
the user control in-progress downloads. Use the `downloadState` property to
determine whether the download completes. Don’t use the `progress` or
`timeRemaining` property of the download object to check its status; these
properties are for updating your UI.

Note

Download all Apple-hosted content before finishing the transaction. After a
transaction is complete, its download objects become unusable.

In iOS, your app can manage the downloaded files. The StoreKit framework saves
these files for you in the `Caches` directory with the backup flag unset.
After the download completes, your app is responsible for moving these files
to the appropriate location. For content that can be deleted if the device
runs out of disk space (and downloaded again later by your app), keep the
files in the `Caches` directory. Otherwise, move the files to the `Documents`
folder and set the flag to exclude them from user backups.

In macOS, the system manages the downloaded files; your app can’t move or
delete them directly. To locate the content after downloading it, use the
`contentURL` property of the download object. To locate the file on subsequent
launches, use the `contentURL(forProductID:)` class method of `SKDownload`. To
delete a file, use the `deleteContent(forProductID:)` class method. For
information about reading the app receipt, see Validating receipts with the
App Store.

## See Also

### Content delivery

Persisting a purchase

Keep a persistent record of a purchase to continue making the product
available as needed.

Finishing a transaction

Finish the transaction to complete the purchase process.

`class SKDownload`

Downloadable content associated with a product.

Deprecated

Article

# Persisting a purchase

Keep a persistent record of a purchase to continue making the product
available as needed.

## Overview

After making a product available, your app needs to make a persistent record
of the purchase. Your app uses that persistent record to continue making the
product available on launch and to restore purchases. Your app’s persistence
strategy depends on the type of products you sell:

  * For non-consumable products and auto-renewable subscriptions, use the app receipt as your persistent record. If the app receipt isn’t available, use the user defaults system or iCloud to keep a persistent record.

  * For non-renewing subscriptions, use iCloud or your own server to keep a persistent record.

  * For consumable products, your app updates its internal state to reflect the purchase. Ensure that the updated state is part of an object that supports state preservation (in iOS) or that you manually preserve the state across app launches (in iOS or macOS). 

When using the user defaults system or iCloud, your app can store a value,
such as a number or Boolean value, or a copy of the transaction receipt. In
macOS, users can edit the user defaults system using the `defaults` command.
Storing a receipt requires more application logic, but protects the persistent
record from tampering.

Note

When persisting with iCloud, your app’s persistent record syncs across
devices, but your app is responsible for downloading any associated content on
other devices.

### Persist purchases using the app receipt

The app receipt contains a record of the user’s purchases, cryptographically
signed by Apple. For more information, see Choosing a receipt validation
technique.

The system adds information about consumable products to the receipt when the
user purchases them, and it remains in the receipt until you finish the
transaction. After you finish the transaction, the system removes this
information the next time it updates the receipt, such as the next time the
user makes a purchase.

The system adds information about all other kinds of purchases to the receipt
when the user purchases the products, and it remains in the receipt
indefinitely.

### Persist a value in user defaults or iCloud

To store information in user defaults or iCloud, set the value for a key.

### Persist purchases using your own server

Send a copy of the receipt to your server, along with credentials or an
identifier, so you can keep track of which receipts belong to a particular
user. For example, let users identify themselves to your server with a user
name and password. Don’t use the `identifierForVendor` property of `UIDevice`.
Different devices have different values for this property, so you can’t use it
to identify and restore purchases that the same user makes on a different
device.

## See Also

### Content delivery

Unlocking purchased content

Deliver content to the user after validating the purchase.

Finishing a transaction

Finish the transaction to complete the purchase process.

`class SKDownload`

Downloadable content associated with a product.

Deprecated

Article

# Finishing a transaction

Finish the transaction to complete the purchase process.

## Overview

Finishing a transaction tells StoreKit that your app completed its workflow to
make a purchase complete. Unfinished transactions remain in the queue until
they’re finished, so be sure to add the transaction queue observer every time
your app launches, to enable your app to finish the transactions. Your app
needs to finish each transaction, whether it succeeds or fails.

Do all of the following before you finish a transaction:

  * Persist the purchase.

  * Deliver, download, or unlock the purchased content.

  * Update your app’s UI so the user can access the product.

To finish the transaction, call the `finishTransaction(_:)` method on the
payment queue.

After you finish a transaction, don’t take any actions on it or do any work to
deliver the product. If any work remains, your app isn’t ready to finish the
transaction.

Important

Don’t call the `finishTransaction(_:)` method before the transaction is
actually complete and attempt to use some other mechanism in your app to track
the transaction as unfinished. StoreKit doesn’t function that way, and doing
that prevents your app from downloading Apple-hosted content and can lead to
other issues.

## See Also

### Content delivery

Unlocking purchased content

Deliver content to the user after validating the purchase.

Persisting a purchase

Keep a persistent record of a purchase to continue making the product
available as needed.

`class SKDownload`

Downloadable content associated with a product.

Deprecated

Article

# Handling refund notifications

Respond to notifications about customer refunds for consumable, non-
consumable, and non-renewing subscription products.

## Overview

The App Store server sends near real-time notifications when customers receive
refunds for in-app purchases. If you offer content across multiple platforms,
for example gems or coins for games, and you update player account balances on
your server, receiving refund notifications is important. Respond to refund
notifications by interpreting and handling the refund information, and
informing customers in the app of any actions you take as a result of the
refund.

To enable notifications, see Enabling App Store Server Notifications and App
Store Server Notifications.

### Receive notifications of customer refunds for one-time purchases

Customers request refunds in several ways, such as:

  * Contacting Apple Customer Support and asking for a refund

  * Logging in and using Apple’s self-service tool, reportaproblem.apple.com, to request a refund

  * Asking their payment method issuer for a refund

When the App Store processes a refund, the App Store server sends a `REFUND`
notification to your server, at the URL you configure. Your server must
respond to the post with a 200 response code. The `REFUND` notification
applies to consumable, non-consumable, and non-renewing subscriptions only. To
detect refunds for auto-renewable subscriptions, see Detect a Refund.

### Interpret and handle the refund notification

Your server is responsible for parsing and interpreting all notifications from
the App Store server. For the `REFUND` notification, identify the specific
transaction, product ID, and relevant dates from the response:

  * Find the most recent transaction for the `product_id i`n the `unified_receipt.latest_receipt_info` by checking the `purchase_date` to select the most recent transaction.

  * The date when App Store issued the refund is in the `cancellation_date_ms` field for the transaction.

For more information about the response, see App Store Server Notifications.

You’re responsible to store, monitor, and take appropriate action for each
refunded transaction when you receive a `REFUND` notification. For example,
you might build your own in-game currency-rebalancing logic that handles
refunded transactions by linking a notification to a player account or
session.

Inform customers by presenting contextual messaging in the app for any actions
you take as a result of the refund.

### Identify refund abuse

Reduce refund abuse and identify repeated refunded purchases by mapping
`REFUND` notifications to the player accounts on your server. Monitor and
analyze your data to identify suspicious refund activity.

If you offer content across multiple platforms, keep the balances for user
accounts up to date on your server. Use App Store Server Notifications to get
near real-time status updates for the transactions that affect your customers.

## See Also

### Refunds

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

# Restoring purchased products

Give users functionality that restores their purchases in your app to maintain
access to purchased content.

## Overview

Users sometimes need to restore purchased content, such as when they upgrade
to a new phone. Include some mechanism in your app, such as a Restore
Purchases button, to let them restore their purchases.

Important

Don’t automatically restore purchases, especially when your app launches.
Restoring purchases prompts for the user’s App Store credentials, which
interrupts the flow of your app.

In most cases, you only need to refresh the app receipt and deliver the
products on the receipt. The refreshed receipt contains a record of the user’s
purchases in the app, from any device the user’s App Store account is logged
into. However, an app might require an alternative approach under the given
circumstances:

  * You use Apple-hosted content — Restore completed transactions to give your app the transaction objects it uses to download the content.

  * You need to support your app on devices where the app receipt isn’t available — Restore completed transactions instead.

  * Your app uses non-renewing subscriptions — Your app is responsible for the restoration process.

Refreshing a receipt doesn’t create new transactions; it requests the latest
copy of the receipt from the App Store. Refresh the receipt only once;
refreshing it multiple times in a row has the same result.

Restoring completed transactions creates a new transaction for each previously
completed transaction, essentially replaying history for your transaction
queue observer. Your app maintains its own state to keep track of why it’s
restoring completed transactions and how to handle them. Restoring multiple
times creates multiple restored transactions for each completed transaction.

Note

If the user attempts to purchase a product that they’ve already purchased, the
App Store creates a regular transaction instead of a restore transaction, but
the user isn’t charged again for the product. Unlock the content for these
transactions the same way you do for original transactions.

Give the user an appropriate level of control over the content that’s
downloaded again. For example, don’t automatically download three years of
daily newspapers or hundreds of megabytes of game levels at the same time.

### Refresh the app receipt

Create a receipt refresh request, set a delegate, and start the request. The
request supports optional properties for obtaining receipts in various states,
such as expired receipts, during testing. For details, see the
`init(receiptProperties:)` method of `SKReceiptRefreshRequest`.

After the app receipt refreshes, examine it and deliver any additional
products, as necessary.

### Restore completed transactions

Your app starts restoring completed transactions by calling the
`restoreCompletedTransactions()` method of `SKPaymentQueue`. This call sends a
request to the App Store to restore all of your app’s completed transactions.
If your app sets a value for the `applicationUsername` property of its payment
requests, use the `restoreCompletedTransactions(withApplicationUsername:)`
method to provide the same information when restoring the transactions.

The App Store generates a new transaction to restore each previously completed
transaction. The restored transaction refers to the original transaction.
Instances of `SKPaymentTransaction` have an `original` property, and the
entries in the receipt have an `original_transaction_id` field value.

Note

The date fields have slightly different meanings for restored purchases. For
details, see the `purchase_date` and `original_purchase_date` fields in the
`responseBody.Receipt.In_app`.

StoreKit calls the transaction queue observer with a status of
`SKPaymentTransactionState.restored` for each restored transaction, as
described in Processing a transaction. The action you take depends on your
app’s design.

If your app uses the app receipt and doesn’t have Apple-hosted content, this
code isn’t needed because your app doesn’t restore completed transactions.
Finish any restored transactions immediately.

If your app uses the app receipt and has Apple-hosted content, let the user
select which products to restore before starting the restoration process.
During restoration, download the user-selected content before finishing those
transactions, and finish any other transactions immediately.

If your app doesn’t use the app receipt, it examines all completed
transactions as it restores them. It uses a similar code path to the original
purchase logic to make the product available and then finishes the
transaction. Apps with more than a few products, especially products with
associated content, let the user select which products to restore instead of
restoring everything. These apps keep track of which completed transactions to
process as they restore them, and which transactions to ignore by finishing
them immediately without restoring them.

## See Also

### Providing access to previously purchased products

`class SKReceiptRefreshRequest`

A request to the App Store to get the app receipt, which represents the user’s
transactions with your app.

`class SKRequest`

An abstract class that represents a request to the App Store.

`class SKPaymentTransaction`

An object in the payment queue.

`func SKTerminateForInvalidReceipt()`

Terminates an app if the license to use the app has expired.

Function

# SKTerminateForInvalidReceipt()

Terminates an app if the license to use the app has expired.

iOS 7.1+  iPadOS 7.1+  macOS 10.14+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    func SKTerminateForInvalidReceipt()

## See Also

### Providing access to previously purchased products

Restoring purchased products

Give users functionality that restores their purchases in your app to maintain
access to purchased content.

`class SKReceiptRefreshRequest`

A request to the App Store to get the app receipt, which represents the user’s
transactions with your app.

`class SKRequest`

An abstract class that represents a request to the App Store.

`class SKPaymentTransaction`

An object in the payment queue.

Article

# Supporting Family Sharing in your app

Provide service to share subscriptions and non-consumable products to family
members.

## Overview

Family Sharing allows a user to share access to auto-renewable subscriptions
or non-consumables with up to five family members on all of their Apple
devices. Enabling Family Sharing for a subscription can make your content or
service more appealing to subscribers, and may encourage conversion to a paid
subscription, increase user engagement, and improve retention. Developers can
choose to turn on Family Sharing for in-app purchases and non-consumables in
App Store Connect. Users can also choose whether to share their purchases with
family.

When users share a purchase through Family Sharing, each family member gets
their own unique receipts and transactions. Process the transactions in the
same way you already handle purchases — you don’t need any special logic for
shared products. However, you do need to implement a new method in your
transaction observer, and listen for a new notification type in server
notifications. Specifically, to support Family Sharing, you need to:

  * Enable Family Sharing for your in-app purchases in App Store Connect. For more information, see Turn on Family Sharing for in-app purchases. 

  * During runtime, check whether in-app purchases support Family Sharing using either `isFamilyShareable` in `Product` or `isFamilyShareable` in `SKProduct`. Then inform users when merchandising your subscriptions.

  * Process purchased and restored transactions in your app. This is standard processing you already do for any purchases.

  * Implement `paymentQueue(_:didRevokeEntitlementsForProductIdentifiers:)` in your transaction observer to handle conditions in which products are no longer shared.

  * Listen for the `REVOKE` `notification_type` from App Store Server Notifications on your server.

Related Sessions from WWDC20

Session 10661: What's new with in-app purchase

### Enable Family Sharing for in-app purchases

To make Family Sharing available for an in-app purchase, developers need to
turn on Family Sharing in App Store Connect. After you enable Family Sharing
for an in-app purchase, you can’t turn it off. For more information, see Turn
on Family Sharing for in-app purchases.

Users can choose whether to share their purchases with family. As users join
or leave family groups and enable or disable sharing, your app needs to update
the family’s access to your products. For information about how users manage
their Family Sharing choices, see Set Up Family Sharing on iPhone.

### Provide access to shared purchases

Your app receives a unique receipt for each family member entitled to a shared
purchase, on each of their devices. For subscriptions, your app unlocks access
through the normal purchase flow. For non-consumable products, unlocking
access may require users to initiate a restored purchase, depending on the
Family Sharing settings at the time of purchase.

To provide access for family members to a subscription or non-consumable, your
app needs to handle purchased and restored transactions as usual.
Specifically, follow these steps:

  1. Set up a transaction observer at app launch so your app receives transactions that occur outside of your app, such as receiving a Family Sharing purchase. For more information on this best practice, see Setting up the transaction observer for the payment queue.

  2. Verify the receipt. Look for a transaction in the latest receipt info array (`responseBody.Latest_receipt_info`) with the new Family Sharing purchase.

  3. Handle purchased (`SKPaymentTransactionState.purchased`) transactions. This is a standard state apps need to handle, and you don’t need anything special for Family Sharing. For shared subscriptions, the transaction always has a purchased state. For shared non-consumable products, the transaction has a purchased state if Family Sharing was enabled for the product at the time of the purchase. For more information about handling transactions, see Processing a transaction.

  4. Handle restored (`SKPaymentTransactionState.restored`) transactions, which is also a standard state apps need to handle. For shared non-consumable products, your app gets a restored transaction if developers enable Family Sharing after the user purchases the product. To gain access to the shared product, family members use your app’s restore functionality. For more information about restoring, see Restoring purchased products.

  5. Unlock access to the shared subscription or non-consumable product.

  6. Call `finishTransaction(_:)`.

### Revoke access if Family Sharing is disabled

With Family Sharing products, users have access to products only while Family
Sharing is enabled. If the purchaser leaves the group, gets a refund, or stops
sharing, the expectation is that the family’s access to the product stops
immediately.

When a condition occurs that disables sharing, StoreKit informs your app by
updating the receipt, and then calling the
`paymentQueue(_:didRevokeEntitlementsForProductIdentifiers:)` method of the
`SKPaymentTransactionObserver` protocol. Implement this method on your
transaction observer, and do the following:

  1. Verify the receipt. Revoked products appear in the receipt with a `cancellation_date` field present.

  2. Provide the app with access to all the products to which the user is entitled.

For more information, including a list of conditions that trigger this call,
see `paymentQueue(_:didRevokeEntitlementsForProductIdentifiers:)`.

### Listen for the revoke notification

If you set up your server to receive App Store Server Notifications, your
server gets a `REVOKE` `notification_type` as soon as a shared purchase is no
longer shared. This notification serves the same purpose as the
`paymentQueue(_:didRevokeEntitlementsForProductIdentifiers:)`call. Listen for
and process this notification by:

  1. Checking the latest receipt (`unified_receipt.Latest_receipt_info`) in the response body. Revoked products appear in the receipt with a `cancellation_date` field present. 

  2. Providing the app with access to all products to which the user is entitled.

  3. Updating your records, if you keep server-based records to manage your customers' subscriptions.

### Indicate to users when products support Family Sharing

When your app displays in-app purchases, indicate in your UI whether users can
share the product with family. Call `isFamilyShareable` to determine at
runtime whether the in-app purchase supports Family Sharing. Knowing whether a
product is shareable helps users make a selection that best fits their needs.

## See Also

### Family Sharing

`var isFamilyShareable: Bool`

A Boolean value that indicates whether the product is available for Family
Sharing in App Store Connect.

`func paymentQueue(SKPaymentQueue, didRevokeEntitlementsForProductIdentifiers:
[String])`

Tells an observer that the user is no longer entitled to one or more Family
Sharing purchases.

Instance Property

# isFamilyShareable

A Boolean value that indicates whether the product is available for Family
Sharing in App Store Connect.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    var isFamilyShareable: Bool { get }

## Discussion

Check the value of `isFamilyShareable` to learn whether an in-app purchase is
sharable with the family group.

When displaying in-app purchases in your app, indicate whether the product
includes Family Sharing to help customers make a selection that best fits
their needs.

Configure your in-app purchases to allow Family Sharing in App Store Connect.
For more information about setting up Family Sharing, see Turn-on Family
Sharing for in-app purchases.

## See Also

### Getting Product Attributes

`var localizedDescription: String`

A description of the product.

`var localizedTitle: String`

The name of the product.

`var contentVersion: String`

A string that identifies the version of the content.

`var contentLengths: [NSNumber]`

The total size of the content, in bytes.

Deprecated

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

### Get visibility settings

To get the visibility settings for a promoted product, call
`fetchStorePromotionVisibility(for:completionHandler:)`, providing the product
information.

### Override visibility settings

For each device, you can decide whether to make in-app purchases visible or
hidden. For example, you may want to hide products the customer already
purchased, and show only the products they can buy.

For example, to hide the Pro Subscription product after a user purchases it,
fetch the product information and update the store promotion controller with
the `.hide` setting, as the following code example shows. The Pro Subscription
promoted in-app purchase no longer appears in the App Store on the device.

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

## See Also

### Promotions

Testing promoted in-app purchases

Test your in-app purchases before making your app available in the App Store.

`class SKProductStorePromotionController`

A product promotion controller for customizing the order and visibility of in-
app purchases per device.

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

# Setting up StoreKit Testing in Xcode

Prepare your test environment to test in-app purchases with data you configure
locally.

## Overview

StoreKit Testing in Xcode is a local test environment for testing in-app
purchases without requiring a connection to App Store servers. Set up in-app
purchases in a local StoreKit configuration file in your Xcode project, or
create a synced StoreKit configuration file in Xcode from your in-app purchase
settings in App Store Connect. After you enable the configuration file, the
test environment uses this local data when your app calls StoreKit APIs.

Note

Enable Developer Mode to test your app on devices running iOS 16 and later,
visionOS, or watchOS 9 and later. For more information about how to enable
Developer Mode, see Enabling Developer Mode on a device.

As you test transactions, the test environment displays a payment sheet with
localized values, and produces receipts for you to verify.

Testing in-app purchase scenarios with StoreKit in Xcode is useful for:

  * Developing features that use in-app purchases before configuring them in App Store Connect.

  * Testing locally when a network connection isn’t available.

  * Debugging in-app purchase use cases that are harder to set up in the sandbox environment, such as eligibility for promotional offers.

  * Viewing localized product information in the payment sheet.

  * Testing transactions end-to-end, including failed transactions.

The full functionality of StoreKit Testing in Xcode is available for
automation. See StoreKit Test for information about automating in-app purchase
testing. For more information about testing StoreKit at different stages of
development, see Testing at all stages of development with Xcode and the
sandbox.

### Create a StoreKit configuration file

A StoreKit configuration file contains descriptions of in-app purchases,
subscription groups, auto-renewable subscriptions, and non-renewing
subscriptions. When the configuration file is active, StoreKit uses this data
when your app calls StoreKit APIs in the test environment. There are two types
of StoreKit configuration files: local and, in Xcode 14 and later, synced.

  * Set up a local configuration file if you haven’t set up your app in App Store Connect, or you want to try out new types of in-app purchases or subscriptions before you set them up in App Store Connect. The local data is convenient to edit in Xcode, and stands in for the data that otherwise comes from App Store Connect.

  * Set up a synced configuration file if you have in-app purchases or subscriptions already set up in App Store Connect that you want to test in Xcode.

To create a StoreKit configuration file:

  1. Launch Xcode, then choose File > New > File.

  2. In the sheet that appears, enter _storekit_ in the Filter search field.

  3. Select StoreKit Configuration File, then click Next.

  4. In the dialog, enter a name for the file. For a synced configuration file, select the checkbox, specify your team and app in the drop-down menus that appear, then click Next. For a local configuration, leave the checkbox unselected, then click Next.

  5. Select a location, and click Create.

  6. Save the file to your project.

If you rename the configuration file, be sure to keep its file extension
.`storekit`.

Note

You can convert a synced configuration file to a local configuration file. If
you want to sync again, create a new synced configuration file.

### Set up a StoreKit configuration

To edit the settings in a local StoreKit configuration file, select the file
in the Project navigator to open the custom editor. Click the Add button (+)
in the editor to add product details to the configuration file.

Note

You can’t edit a synced configuration file unless you convert it to be a local
configuration file. To convert a synced configuration file, select the file,
then choose Editor > Convert to Local StoreKit Configuration from the Xcode
menu. Click Convert File in the confirmation dialog. When you’re viewing a
synced configuration file, click the Sync button in the bottom left corner to
pull the latest updates from App Store Connect.

Enter the information in your local StoreKit configuration file manually. The
product names, IDs, prices, localizations, and any other data you provide in
the StoreKit configuration file don’t upload to App Store Connect, and don’t
appear in App Store-signed apps. App Store Connect data transfers only to a
synced StoreKit configuration file, which you can’t edit in Xcode.

Tip

If you have a synced configuration file with items you want to test in a local
configuration file, you may copy an item from your synced configuration file
to your local configuration file. To do this, Control-click an item in your
synced configuration file, and choose Copy. In your local configuration file,
select where you want to place the item, and choose Edit > Paste from the
Xcode menu.

Each in-app purchase and non-renewing subscription has a reference name,
product ID, and price. In-app purchases and non-renewing subscriptions
optionally have localizations. This metadata shows up in the payment sheet
after you click to buy a product in your app. Note that the price is a
placeholder value that’s not connected to price tiers or real pricing
information. However, it appears using the correct currency symbols for the
storefront you’re testing.

For non-consumable in-app purchases and auto-renewable subscriptions, select
Family Sharing to mark the product for sharing as the following image shows:

When you set up the first auto-renewable subscription, Xcode prompts you to
create the first subscription group. After adding subscriptions to a group,
the level you assign to each subscription determines their upgrade and
downgrade options. For more information, see Offer auto-renewable
subscriptions.

For auto-renewable subscriptions, set up introductory offers and promotional
offers with the options available in App Store Connect. To begin testing,
configure at least one in-app purchase product.

### Enable StoreKit Testing in Xcode

To enable StoreKit Testing in Xcode, your project must have an active StoreKit
configuration file. By default, StoreKit Testing in Xcode is disabled. To
select a configuration file and make it active:

  1. Click the scheme to open the Scheme menu and choose Edit Scheme.

  2. In the scheme editor, select the Run action.

  3. Click the Options tab.

  4. For the StoreKit Configuration option, select a configuration file and click Close.

You can also add an existing StoreKit configuration file to the project from
this menu. Choose a configuration file with a .`storekit` file extension.

An Xcode project can contain multiple StoreKit configuration files, but only
one can be active at a time. When it’s active, build and run your app as
usual. Instead of accessing App Store Connect or the sandbox server, your app
gets StoreKit data from the test environment.

### Disable StoreKit Testing in Xcode

To disable StoreKit Testing in Xcode, remove the StoreKit configuration file
from the scheme’s run options:

  1. Click the scheme to open the Scheme menu and choose Edit Scheme.

  2. In the scheme editor, select the Run action.

  3. Click the Options tab.

  4. For the StoreKit Configuration option, select None.

Your app stops using the local data from the configuration file and starts
using the data from App Store Connect. For more information, see Overview for
configuring in-app purchases.

### Prepare to validate receipts in the test environment

StoreKit Testing in Xcode generates locally signed receipts that your app
validates locally. Obtain the certificate you need for local validation and
add it to your project as follows:

  1. In Xcode’s Project navigator, click the StoreKit configuration file.

  2. From the Xcode menu, choose Editor > Save Public Certificate.

  3. Select a location in your project to save the file.

Note

The test environment’s certificate is a root certificate. There’s no
certificate chain to validate when you validate the receipt signature.

Be sure your code uses the correct certificate in all environments. Add the
following conditional compilation block to your receipt validation code to
select the test certificate for testing, and the Apple root certificate,
otherwise:

Your code is ready to validate receipts by selecting the appropriate
certificate in the test environment and in the production environment.

Important

Receipts you produce in the test environment aren’t signed by the App Store
and aren’t valid for apps in production.

## See Also

### StoreKit

Testing in-app purchases with StoreKit transaction manager in Xcode

Use the transaction manager within Xcode to test in-app purchases without
requiring a connection to App Store servers.

Article

# Testing in-app purchases in Xcode

Use locally configured product data to test and debug your in-app purchases
implementation.

## Overview

Testing your StoreKit implementation in Xcode ensures that your app behaves
correctly when your users perform various tasks associated with subscriptions
and in-app purchase transactions. Be sure to test a variety of in-app purchase
scenarios, such as receipt validation, promotional offers, interrupted
purchases, introductory offers, subscription renewals, and purchase
restoration.

### Perform basic setup

Before you begin StoreKit testing in Xcode, complete the steps in Setting up
StoreKit Testing in Xcode, including creating a StoreKit configuration file,
enabling StoreKit testing in Xcode, and preparing to validate receipts in the
test environment. The test scenarios in this article require this basic setup.

Select the relevant test scenarios to build a test plan for your app. Each
test scenario provides additional setup steps, if necessary, along with
instructions about how to minimally reset the environment to repeat the test.

### Validate a receipt in the test environment

Validating receipts is an integral part of handling and testing in-app
purchases. As you test in-app purchases, StoreKit in Xcode generates receipts
that are valid only in the test environment. Your app can validate the
receipts locally using a certificate that Xcode provides.

Important

You can’t validate receipts from the test environment with verifyReceipt
because the App Store doesn’t sign these receipts, and the verification fails.

The test environment’s certificate is a root certificate. There’s no
certificate chain to validate when you verify the receipt signature. The
following code example retrieves the local receipt:

For more information, see Validating receipts on the device.

### Test a promotional offer

For this test scenario, let’s assume the app determines that customers are
eligible for the promotional offer when the subscription expires. Use the test
environment to speed up the time rate so the subscription expires. Then,
you’re ready to test the offer eligibility logic in your app.

Additional setup steps for this test scenario are:

  * Add a subscription offer to your StoreKit configuration file.

  * In the app, purchase a subscription within the same subscription group to be eligible for a promotional offer.

Ensure your test user is eligible for the offer according to your app’s
requirements, then purchase the subscription with the offer. Test users can
redeem subscription offers if:

  * They have an existing or expired subscription, including free, discount, or discounted with a subscription offers.

  * They qualify for the offer according to criteria that you define.

See Implementing promotional offers in your app for more information.

  1. In Xcode, select the StoreKit configuration file in the Project navigator, and then choose Editor > Subscription Renewal Rate > Monthly Renewal Every 30 Seconds.

  2. Wait until the subscription expires.

  3. Reset the Subscription Renewal rate to Monthly Renewal Every 30 Minutes.

  4. In the app, select the option to buy the subscription with the offer.

  5. In your code, verify that the payment request includes the discount, `paymentDiscount`.

  6. Observe that the system displays the payment sheet with the promotional offer.

  7. In your code, verify that `paymentQueue(_:updatedTransactions:)` receives the transaction in the `SKPaymentTransactionState.purchasing` state.

  8. In the app, tap Confirm on the payment sheet.

  9. In your code, verify that `paymentQueue(_:updatedTransactions:)` receives the transaction in the `SKPaymentTransactionState.purchased` state.

To test the same promotional offer purchase again, delete the transaction. In
Xcode, choose Debug > StoreKit > Manage Transactions. Select the transaction
for the promotional offer purchase, and click Delete.

### Test an interrupted purchase

An interrupted purchase is a transaction that requires the user to perform
some action outside your app before the transaction can complete successfully.
For example, the user may need to update a payment method or approve new terms
and conditions. In Xcode, you can simulate a purchase interruption and its
resolution to test how your code handles this scenario end-to-end. You can
test this scenario for all in-app purchase product types.

  1. In the Xcode Project navigator, select the StoreKit configuration file. Choose Editor > Enable Interrupted Purchases. Run the app in the simulator or on a device.

  2. In the app, buy an in-app purchase.

  3. Observe that the system displays the payment sheet in the app.

  4. In your code, verify that your `SKPaymentTransactionObserver` gets a callback on `paymentQueue(_:updatedTransactions:)` with a transaction in the `SKPaymentTransactionState.purchasing` state.

  5. In the app, tap Confirm on the payment sheet.

  6. In your code, observe that the payment fails (because you enabled interrupted purchases in the test environment). The payment queue receives a transaction in the `SKPaymentTransactionState.failed` state.

  7. Check that your code calls `finishTransaction(_:)` to remove it from the queue.

  8. In Xcode, choose Debug > StoreKit > Manage Transactions.

  9. Select the transaction and click Resolve. The test environment resumes a successful purchase.

  10. In your code, verify that the payment queue receives a transaction in the `SKPaymentTransactionState.purchased` state for the same `productIdentifier` in the same quantity as the failed transaction.

  11. In your code, validate the receipt. 

  12. Check that your app provides the service or product, and then calls `finishTransaction(_:)`.

To perform the test again for non-consumable products and subscriptions,
delete the transaction to run the test again. To delete the transaction,
choose Debug > StoreKit > Manage Transactions. Select the transaction and
click Delete.

For consumable in-app purchases, you can test again without additional setup.
To reset the test environment to its default behavior, select the StoreKit
configuration file in Xcode, then choose Editor > Disable Interrupted
Purchases.

### Test an introductory offer

Customers are eligible to redeem an introductory offer one time. Configure an
introductory offer for a subscription in your StoreKit configuration file. For
more information, see Implementing introductory offers in your app.

Ensure that your app is eligible for an introductory offer by verifying
there’s no subscription purchase for the product ID that includes the offer.
Either verify the receipt in your code or check the transactions in Xcode by
choosing Debug > StoreKit > Manage Transactions.

  1. In the app, buy the subscription that has an introductory offer.

  2. Observe that the system displays the payment sheet with the introductory offer in the app.

  3. In your code, verify your `SKPaymentTransactionObserver` receives a callback on `paymentQueue(_:updatedTransactions:)` with the transaction in the `SKPaymentTransactionState.purchasing` state.

  4. In the app, tap Confirm on the payment sheet.

  5. In your code, verify your `SKPaymentTransactionObserver` receives a callback on `paymentQueue(_:updatedTransactions:)` with the transaction in the `SKPaymentTransactionState.purchased` state.

  6. In your code, validate the receipt.

  7. Check that your app provides the service or product, and then calls `finishTransaction(_:)`.

To retry the same test scenario, delete the transaction that contains the
introductory offer purchase. In Xcode, choose Debug > StoreKit > Manage
Transactions. Select the transaction and click Delete. This resets the
eligibility for the test user.

### Test restoring purchases without existing purchases

All apps need to provide a way for customers to restore purchases, such as by
providing a Restore Purchases button. Test how your app handles this request
when the customer has no existing purchases. For more information, see
Restoring purchased products.

Include at least one non-consumable product, auto-renewable subscription, or
non-renewable subscription in the StoreKit configuration file. To simulate a
user account with no in-app purchases, delete all the transactions before
starting the test. In Xcode, choose Debug > StoreKit > Manage Transactions,
select all the transactions, and click Delete.

  1. In the app, select the option your app provides to restore purchases.

  2. In your code, verify that it calls `restoreCompletedTransactions()` or `restoreCompletedTransactions(withApplicationUsername:)`.

  3. In your code, verify that StoreKit notifies your observer that the restore is complete by calling `paymentQueueRestoreCompletedTransactionsFinished(_:)`. Note that StoreKit doesn’t notify the queue of any restored transactions.

You can repeat this test scenario without additional steps.

### Test presenting the App Store sheet for managing subscriptions

Your app can present an App Store sheet that customers can use to manage their
subscriptions.

Additional setup steps for this test scenario are:

  * Include two auto-renewable subscriptions that belong to the same subscription group in the StoreKit configuration file.

  * Subscribe the sandbox user to the subscription with the lowest level of service in that subscription group.

  * In the app, implement a Manage Subscriptions button that invokes the `showManageSubscriptions(in:)` or `manageSubscriptionsSheet(isPresented:)` method.

See `showManageSubscriptions(in:)` and
`manageSubscriptionsSheet(isPresented:)` for more information.

  1. In the app, tap the Manage Subscriptions button.

  2. Observe that the system displays the App Store sheet for managing subscriptions.

  3. Verify that the test user is a subscriber of the lower-grade subscription.

  4. Upgrade the test user to the higher-grade subscription in that group.

  5. Verify that the user is a subscriber of the higher-grade subscription.

  6. Cancel the subscription and confirm it in the Confirm Cancellation dialog.

  7. Verify that the user is no longer a subscriber of any subscription.

You can repeat this test scenario without additional steps.

### Test an offer code

Your app can present a sheet to redeem preconfigured subscription offer codes.

Additional setup steps for this test scenario are:

  * Include one auto-renewable subscription in the StoreKit configuration file.

  * Configure an offer code for the above subscription in your StoreKit configuration file under the Offer Codes heading.

  * In the app, implement a Redeem Offer Code button that invokes the `presentCodeRedemptionSheet()` method.

See `presentCodeRedemptionSheet()` for more information.

  1. In the app, tap the Redeem Offer Code button.

  2. Observe that the system displays the Redeem Offer Code sheet.

  3. Select the offer code that you configured and redeem it.

  4. Observe that the system displays the payment sheet with the applied offer.

  5. In the app, tap Confirm on the payment sheet.

  6. In your code, verify your `SKPaymentTransactionObserver` receives a callback on `paymentQueue(_:updatedTransactions:)` with the transaction in the `SKPaymentTransactionState.purchased` state.

  7. Check that your app provides the service or product, and then calls `finishTransaction(_:)`.

To retry the same test scenario, delete the transaction that contains the
offer code purchase. In Xcode, choose Debug > StoreKit > Manage Transactions.
Select the transaction and click Delete.

### Test billing retry and grace period for auto-renewable subscriptions

When billing for a subscription renewal fails, such as due to an expired card,
the App Store retries billing and attempts to recover the subscription. You
can enable a billing grace period for your app in App Store Connect so your
subscribers can continue accessing paid content while the App Store retries
billing. For more information about the billing grace period, see Reducing
Involuntary Subscriber Churn.

Test these scenarios in Xcode to ensure your app detects subscriptions that
are in billing retry or billing grace period states. In your code, look at the
`renewalInfo` for the subscription to inspect its
`Product.SubscriptionInfo.RenewalState`. For subscriptions in a billing grace
period state, ensure your app continues to provide uninterrupted subscription
features.

Additional setup steps for this scenario are:

  * Choose Editor > Enable Billing Grace Period. This step simulates enabling the billing grace period for your app in App Store Connect. To test billing retry without a billing grace period, leave this setting disabled.

  * Choose Editor > Enable Billing Retry on Renewal. This step causes all subscription renewals to go into a billing retry state.

  * Select your StoreKit configuration file in the Project navigator.

  * Create an auto-renewable subscription in-app purchase in your StoreKit configuration file.

  * Purchase the auto-renewable subscription in your app.

  * Adjust the time rate of subscription renewals in the testing environment by choosing Editor > Subscription Renewal Rate, and select an option. For more information about the time rates available in the testing environment, see `timeRate`.

Test your app’s handling of a billing grace period:

  1. In the testing environment, wait for the subscription period to elapse. The subscription goes into a billing retry state and a billing grace period.

  2. Run your app, then choose Debug > StoreKit > Manage Transactions.

  3. Find and select the subscription transaction.

  4. Verify the subscription transaction is in the billing grace period state.

  5. Test your app to verify that it supports the billing grace period by continuing to provide uninterrupted access to the features the subscription provides.

Test your app’s handling of a billing grace period expiration:

  1. In the testing environment, wait until the billing grace period elapses for the subscription.

  2. Run your app, then choose Debug > StoreKit > Manage Transactions.

  3. Find and select the subscription transaction.

  4. Verify the subscription transaction is in the billing retry state, and is no longer in the billing grace period state.

  5. Test your app to verify that it works consistently with a subscription expiration.

Test resolving a billing issue for billing retry, either with a billing grace
period or without:

  1. In the testing environment, wait for the subscription period to elapse. Verify your app works consistently with a subscription expiration if you’re not testing a billing grace period.

  2. Run your app, then choose Debug > StoreKit > Manage Transactions.

  3. Find and select the subscription transaction.

  4. Verify the subscription transaction is in either the billing grace period state or the billing retry state.

  5. Click the Resolve Issues button to resolve the billing issue.

  6. Test your app to verify that it provides access to the subscription features as you expect.

### Test price increase consent

When you increase the price of an auto-renewable subscription by an amount
that requires user consent, the App Store gives the user an opportunity to
consent to the price increase by presenting a sheet in your app. Your app may
defer presentation of the sheet to prevent it from appearing at an
inconvenient time in the user interface. Users may also consent to a price
increase outside your app. Test these scenarios in Xcode to verify that your
app handles deferring or displaying the sheet.

Additional setup steps for this scenario are:

  * Create an auto-renewable subscription purchase in your StoreKit configuration file.

  * Purchase the subscription in your app.

  * Optionally, increase the price for your subscription in your StoreKit configuration file. You can still test this scenario without increasing the price.

Test for the deferred price increase consent sheet presentation:

  1. Navigate to a place in your app where you defer presentation of the price increase consent sheet.

  2. Run your app, then choose Debug > StoreKit > Manage Transactions.

  3. Find and select the subscription transaction.

  4. Click Request Price Increase Consent.

  5. Verify that the price increase consent sheet doesn’t display in your app.

  6. Navigate away from the view where you defer presentation.

  7. Verify that the price increase consent sheet displays in your app.

  8. On the price increase consent sheet in the app, select the Agree to New Price button to test a user consenting to the price increase, or select Close to test the user not giving consent for the price increase.

Test for the price increase consent sheet presentation:

  1. Navigate to a place in your app where you don’t defer presenting the price increase consent sheet.

  2. In the StoreKit transaction manager, select the subscription purchase, then click Request Price Increase Consent.

  3. Verify that the price increase consent sheet displays in your app.

  4. On the price increase consent sheet in the app, select the Agree to New Price button to test a user consenting to the price increase, or select Close to test the user not giving consent for the price increase.

For information about testing price increase consent in an automated test
suite, see `requestPriceIncreaseConsentForTransaction(identifier:)`,
`consentToPriceIncreaseForTransaction(identifier:)`, and
`declinePriceIncreaseForTransaction(identifier:)`.

## See Also

### Testing in-app purchases

Testing at all stages of development with Xcode and the sandbox

Verify your implementation of in-app purchases by testing your code throughout
its development.

Setting up StoreKit Testing in Xcode

Prepare your test environment to test in-app purchases with data you configure
locally.

Testing in-app purchases with sandbox

Test your implementation of in-app purchases using real product information
and server-to-server transactions in the sandbox environment.

Article

# Handling errors

Determine the underlying cause of errors that result from StoreKit requests.

## Overview

A StoreKit request may fail for one of many possible reasons, including
invalid product information, invalid payment details, problems with your App
Store Connect account, or networking issues. When an error occurs, check the
error code to find out what went wrong.

### Determine the cause of the error

When handling errors, such as with the `request(_:didFailWithError:)` delegate
method, it’s important to use the `domain` and `code` of the resulting error
to determine the underlying cause of failure.

StoreKit uses `SKErrorDomain` for errors related to payments, store products,
and cloud services, as described in `SKError.Code`. For additional information
on troubleshooting StoreKit framework issues, see the In-App Purchase FAQ.

Errors related to networking use `NSURLErrorDomain`. The following table
describes some of the most common networking errors that may occur when using
StoreKit:

Error code| Description  
---|---  
`NSURLErrorTimedOut` (`-1001`)| The connection timed out.  
`NSURLErrorCannotFindHost` (`-1003`)| The connection failed because it can't
find the host.  
`NSURLErrorCannotConnectToHost` (`-1004`)| The connection failed because it
can't connect to the host.  
`NSURLErrorNetworkConnectionLost` (`-1005`)| The connection failed because it
lost the network connection.  
`NSURLErrorNotConnectedToInternet` (`-1009`)| The connection failed because
the device isn't connected to the internet.  
`NSURLErrorUserCancelledAuthentication` (`-1012`)| The connection failed
because the user canceled required authentication.  
`NSURLErrorSecureConnectionFailed` (`-1200`)| The secure connection failed for
an unknown reason.  
  
## See Also

### Errors

`enum SKError.Code`

Error codes for StoreKit errors.

`struct SKError`

StoreKit error descriptions, codes, and domains.

`let SKErrorDomain: String`

The error domain name for StoreKit errors.

Global Variable

# SKErrorDomain

The error domain name for StoreKit errors.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    let SKErrorDomain: String

## See Also

### Errors

Handling errors

Determine the underlying cause of errors that result from StoreKit requests.

`enum SKError.Code`

Error codes for StoreKit errors.

`struct SKError`

StoreKit error descriptions, codes, and domains.

