Type Property

# updates

The asynchronous sequence that emits a transaction when the system creates or
updates transactions that occur outside of the app or on other devices.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static var updates: Transaction.Transactions { get }

## Discussion

Use `updates` to receive new transactions while the app is running. This
sequence receives transactions that occur outside of the app, such as Ask to
Buy transactions, subscription offer code redemptions, and purchases that
customers make in the App Store. It also emits transactions that customers
complete in your app on another device.

Note that after a successful in-app purchase on the same device, StoreKit
returns the transaction through `Product.PurchaseResult.success(_:)`.

Important

Create a `Task` to iterate through the transactions from the listener as soon
as your app launches. If your app has unfinished transactions, the `updates`
listener receives them once, immediately after the app launches. Without the
`Task` to listen for these transactions, your app may miss them.

The following example shows a class that creates a `Task` when it initializes.
The task retrieves and processes any unfinished transactions.

The `updates` listener receives unfinished transactions just once at app
launch, but you can use the `unfinished` listener to get your app’s unfinished
transactions at any time. For information on finishing transactions, see
`finish()`.

## See Also

### Monitoring transaction-related changes

`struct Transaction.Transactions`

An asynchronous sequence of transactions.

### Related Documentation

Supporting subscription offer codes in your app

Provide subscription service for customers who redeem offer codes through the
App Store or within your app.

Type Method

# latest(for:)

Gets the user’s latest transaction for an in-app purchase.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func latest(for productID: String) async -> VerificationResult<Transaction>?

##  Parameters

`productID`

    

The product identifier that the function uses to look up the latest
transaction.

## Return Value

A `VerificationResult` with a single `Transaction`, or `nil` if the user
hasn't purchased the product.

## Discussion

Call this function for any type of in-app purchase. The following example
illustrates requesting the latest transaction to determine if the user
purchased the product indicated by the string `productIdentifier`.

## See Also

### Getting transaction history

`static var all: Transaction.Transactions`

A sequence that emits all the transactions for the user for your app.

`static var unfinished: Transaction.Transactions`

A sequence that emits unfinished transactions for the user.

Type Property

# all

A sequence that emits all the transactions for the user for your app.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static var all: Transaction.Transactions { get }

## Discussion

This sequence returns the user’s transaction history current to the moment you
access it. The sequence emits a finite number of transactions. If the App
Store processes additional transactions for the user while you’re accessing
this sequence, they appear in the transaction listener `updates`.

The transaction history includes consumable in-app purchases that the app
hasn’t finished by calling `finish()`. It doesn’t include finished consumable
products or finished non-renewing subscriptions, repurchased non-consumable
products or subscriptions, or restored purchases.

## See Also

### Getting transaction history

`static func latest(for: String) -> VerificationResult<Transaction>?`

Gets the user’s latest transaction for an in-app purchase.

`static var unfinished: Transaction.Transactions`

A sequence that emits unfinished transactions for the user.

Type Property

# unfinished

A sequence that emits unfinished transactions for the user.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static var unfinished: Transaction.Transactions { get }

## Discussion

A transaction is unfinished until you call `finish()`. Use the `unfinished`
sequence to find the transactions your app needs to process to deliver
purchased content or enable service.

## See Also

### Finishing the transaction

`func finish()`

Indicates to the App Store that the app delivered the purchased content or
enabled the service to finish the transaction.

Type Property

# currentEntitlements

A sequence of the latest transactions that entitle a user to in-app purchases
and subscriptions.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static var currentEntitlements: Transaction.Transactions { get }

## Discussion

The current entitlements sequence emits the latest transaction for each
product the user has an entitlement to, specifically:

  * A transaction for each non-consumable in-app purchase

  * The latest transaction for each auto-renewable subscription that has a `Product.SubscriptionInfo.RenewalState` state of `subscribed` or `inGracePeriod`

  * The latest transaction for each non-renewing subscription, including finished ones

Products that the App Store has refunded or revoked don’t appear in the
current entitlements. Consumable in-app purchases also don't appear in the
current entitlements. To get transactions for unfinished consumables, use the
`unfinished` or `all` sequences in `Transaction`.

The following example illustrates iterating through the current entitlements:

## See Also

### Getting current entitlements

`static func currentEntitlement(for: String) ->
VerificationResult<Transaction>?`

Gets the latest transactions that entitle the user to a specified product.

Type Method

# currentEntitlement(for:)

Gets the latest transactions that entitle the user to a specified product.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func currentEntitlement(for productID: String) async -> VerificationResult<Transaction>?

##  Parameters

`productID`

    

In-app purchase product identifier.

## Return Value

A `VerificationResult` or `nil` if the user has no current in-app purchases.

## See Also

### Getting current entitlements

`static var currentEntitlements: Transaction.Transactions`

A sequence of the latest transactions that entitle a user to in-app purchases
and subscriptions.

Instance Method

# finish()

Indicates to the App Store that the app delivered the purchased content or
enabled the service to finish the transaction.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    func finish() async

## Discussion

Call `finish()` to complete a transaction after you deliver the purchased
content or enable the purchased service. For on-demand resources, don’t finish
the transaction until the app completes downloading the resource or you’ve
otherwise delivered the resource.

## See Also

### Finishing the transaction

`static var unfinished: Transaction.Transactions`

A sequence that emits unfinished transactions for the user.

Type Property

# unfinished

A sequence that emits unfinished transactions for the user.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static var unfinished: Transaction.Transactions { get }

## Discussion

A transaction is unfinished until you call `finish()`. Use the `unfinished`
sequence to find the transactions your app needs to process to deliver
purchased content or enable service.

## See Also

### Finishing the transaction

`func finish()`

Indicates to the App Store that the app delivered the purchased content or
enabled the service to finish the transaction.

Instance Property

# deviceVerification

The device verification value you use to verify whether the transaction
belongs to the device.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let deviceVerification: Data

## Discussion

Whenever StoreKit returns a verified transaction, the transaction is valid for
the device. To perform your own verification, compute the device verification
hash as follows:

  1. Get the lowercase UUID string representation of `deviceVerificationNonce`.

  2. Append the lowercase UUID string representation of `deviceVerificationID`.

  3. Compute the SHA-384 hash of the ASCII representation of the combined string.

Compare the value you calculated to the transaction’s `deviceVerification`
value. If the values match, the transaction is valid for the device.
Otherwise, the verification fails and the transaction isn’t valid for the
device. The following example illustrates validating a transaction.

## See Also

### Verifying transactions

`let deviceVerificationNonce: UUID`

The UUID used to compute the device verification value.

`let signedDate: Date`

The date that the App Store signed the JWS transaction.

Instance Property

# deviceVerificationNonce

The UUID used to compute the device verification value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let deviceVerificationNonce: UUID

## Discussion

Use the lowercased nonce when computing the `deviceVerification` value.

## See Also

### Verifying transactions

`let deviceVerification: Data`

The device verification value you use to verify whether the transaction
belongs to the device.

`let signedDate: Date`

The date that the App Store signed the JWS transaction.

Instance Property

# signedDate

The date that the App Store signed the JWS transaction.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let signedDate: Date

## Discussion

Use the `signedDate` to verify whether the certificate used to sign the
transaction was valid when the App Store signed the transaction.

## See Also

### Verifying transactions

`let deviceVerification: Data`

The device verification value you use to verify whether the transaction
belongs to the device.

`let deviceVerificationNonce: UUID`

The UUID used to compute the device verification value.

Instance Property

# jsonRepresentation

The raw JSON representation of the transaction information.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var jsonRepresentation: Data { get }

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

Instance Method

# beginRefundRequest(in:)

Presents the refund request sheet for the transaction in a window scene.

iOS 15.0+  iPadOS 15.0+  Mac Catalyst 15.0+  visionOS 1.0+  Xcode 13.0+

    
    
    func beginRefundRequest(in scene: UIWindowScene) async throws -> Transaction.RefundRequestStatus

##  Parameters

`scene`

    

The `UIWindowScene` that the system displays the sheet on.

## Return Value

`Transaction.RefundRequestStatus`

## Discussion

Call this function from account settings or a help menu to enable customers to
request a refund for an in-app purchase within your app. When you call this
function, the system displays a refund sheet with the customer’s purchase
details and a list of reason codes for the customer to choose from. For design
guidance, see Human Interface Guidelines > In-app purchase > Providing help
with in-app purchases.

When a customer requests a refund for consumable in-app purchases through your
app, the App Stores sends a `CONSUMPTION_REQUEST` `notificationType` to your
server. If the customer provided consent, respond by sending consumption data
to the App Store using the Send Consumption Information endpoint. If not,
don’t respond to the `CONSUMPTION_REQUEST` notification.

The App Store takes up to 48 hours to either approve or deny a refund.

For information about setting up your server to receive notifications, see
Enabling App Store Server Notifications.

Note

If your app uses SwiftUI, use `refundRequestSheet(for:isPresented:onDismiss:)`
instead. For example usage, see Food Truck: Building a SwiftUI multiplatform
app.

### Test refund requests

The sandbox environment and StoreKit Testing in Xcode both support testing
refund requests. For more information, see Testing refund requests.

## See Also

### Requesting refunds

Testing refund requests

Test your app’s implementation of refund requests, and your app’s and server’s
handling of approved and declined refunds.

`func beginRefundRequest(in: NSViewController) ->
Transaction.RefundRequestStatus`

Presents the refund request sheet for the transaction in a view controller.

`static func beginRefundRequest(for: UInt64, in: UIWindowScene) ->
Transaction.RefundRequestStatus`

Presents the refund request sheet for the specified transaction in a window
scene.

`static func beginRefundRequest(for: UInt64, in: NSViewController) ->
Transaction.RefundRequestStatus`

Presents the refund request sheet for the specified transaction in a view
controller.

`enum Transaction.RefundRequestError`

The error codes for refund requests.

`enum Transaction.RefundRequestStatus`

The status codes for refund requests.

Instance Method

# beginRefundRequest(in:)

Presents the refund request sheet for the transaction in a view controller.

macOS 12.0+  Xcode 13.0+

    
    
    func beginRefundRequest(in controller: NSViewController) async throws -> Transaction.RefundRequestStatus

##  Parameters

`controller`

    

The `NSViewController` that the system displays the sheet on.

## Return Value

`Transaction.RefundRequestStatus`

## Discussion

Call this function from account settings or a help menu to enable customers to
request a refund for an in-app purchase within your app. When you call this
function, the system displays a refund sheet with the customer’s purchase
details and a list of reason codes for the customer to choose from. For design
guidance, see Human Interface Guidelines > In-app purchase > Providing help
with in-app purchases.

When a customer requests a refund for consumable in-app purchases through your
app, the App Stores sends a `CONSUMPTION_REQUEST` `notificationType` to your
server. If the customer provided consent, respond by sending consumption data
to the App Store using the Send Consumption Information endpoint. If not,
don’t respond to the `CONSUMPTION_REQUEST` notification.

The App Store takes up to 48 hours to either approve or deny a refund.

For information about setting up your server to receive notifications, see
Enabling App Store Server Notifications.

Note

If your app uses SwiftUI, use `refundRequestSheet(for:isPresented:onDismiss:)`
instead. For example usage, see Food Truck: Building a SwiftUI multiplatform
app.

### Test refund requests

The sandbox environment and StoreKit Testing in Xcode both support testing
refund requests. For more information, see Testing refund requests.

## See Also

### Requesting refunds

Testing refund requests

Test your app’s implementation of refund requests, and your app’s and server’s
handling of approved and declined refunds.

`func beginRefundRequest(in: UIWindowScene) ->
Transaction.RefundRequestStatus`

Presents the refund request sheet for the transaction in a window scene.

`static func beginRefundRequest(for: UInt64, in: UIWindowScene) ->
Transaction.RefundRequestStatus`

Presents the refund request sheet for the specified transaction in a window
scene.

`static func beginRefundRequest(for: UInt64, in: NSViewController) ->
Transaction.RefundRequestStatus`

Presents the refund request sheet for the specified transaction in a view
controller.

`enum Transaction.RefundRequestError`

The error codes for refund requests.

`enum Transaction.RefundRequestStatus`

The status codes for refund requests.

Type Method

# beginRefundRequest(for:in:)

Presents the refund request sheet for the specified transaction in a window
scene.

iOS 15.0+  iPadOS 15.0+  Mac Catalyst 15.0+  visionOS 1.0+  Xcode 13.0+

    
    
    @MainActor
    static func beginRefundRequest(
        for transactionID: UInt64,
        in scene: UIWindowScene
    ) async throws -> Transaction.RefundRequestStatus

##  Parameters

`transactionID`

    

The identifier of the transaction the user is requesting a refund for.

`scene`

    

The `UIWindowScene` that the system displays the sheet on.

## Return Value

`Transaction.RefundRequestStatus`

## Discussion

Call this function from account settings or a help menu to enable customers to
request a refund for an in-app purchase within your app. When you call this
function, the system displays a refund sheet with the customer’s purchase
details and a list of reason codes for the customer to choose from. For design
guidance, see Human Interface Guidelines > In-app purchase > Providing help
with in-app purchases.

When a customer requests a refund for consumable in-app purchases through your
app, the App Stores sends a `CONSUMPTION_REQUEST` `notificationType` to your
server. If the customer provided consent, respond by sending consumption data
to the App Store using the Send Consumption Information endpoint. If not,
don’t respond to the `CONSUMPTION_REQUEST` notification.

The App Store takes up to 48 hours to either approve or deny a refund.

For information about setting up your server to receive notifications, see
Enabling App Store Server Notifications.

Note

If your app uses SwiftUI, use `refundRequestSheet(for:isPresented:onDismiss:)`
instead. For example usage, see Food Truck: Building a SwiftUI multiplatform
app.

### Test refund requests

The sandbox environment and StoreKit Testing in Xcode both support testing
refund requests. For more information, see Testing refund requests.

## See Also

### Requesting refunds

Testing refund requests

Test your app’s implementation of refund requests, and your app’s and server’s
handling of approved and declined refunds.

`func beginRefundRequest(in: UIWindowScene) ->
Transaction.RefundRequestStatus`

Presents the refund request sheet for the transaction in a window scene.

`func beginRefundRequest(in: NSViewController) ->
Transaction.RefundRequestStatus`

Presents the refund request sheet for the transaction in a view controller.

`static func beginRefundRequest(for: UInt64, in: NSViewController) ->
Transaction.RefundRequestStatus`

Presents the refund request sheet for the specified transaction in a view
controller.

`enum Transaction.RefundRequestError`

The error codes for refund requests.

`enum Transaction.RefundRequestStatus`

The status codes for refund requests.

Type Method

# beginRefundRequest(for:in:)

Presents the refund request sheet for the specified transaction in a view
controller.

macOS 12.0+  Xcode 13.0+

    
    
    static func beginRefundRequest(
        for transactionID: UInt64,
        in controller: NSViewController
    ) async throws -> Transaction.RefundRequestStatus

##  Parameters

`transactionID`

    

The identifier of the transaction the user is requesting a refund for.

`controller`

    

The `NSViewController` that the system displays the sheet on.

## Return Value

`Transaction.RefundRequestStatus`

## Discussion

Call this function from account settings or a help menu to enable customers to
request a refund for an in-app purchase within your app. When you call this
function, the system displays a refund sheet with the customer’s purchase
details and a list of reason codes for the customer to choose from. For design
guidance, see Human Interface Guidelines > In-app purchase > Providing help
with in-app purchases.

When a customer requests a refund for consumable in-app purchases through your
app, the App Stores sends a `CONSUMPTION_REQUEST` `notificationType` to your
server. If the customer provided consent, respond by sending consumption data
to the App Store using the Send Consumption Information endpoint. If not,
don’t respond to the `CONSUMPTION_REQUEST` notification.

The App Store takes up to 48 hours to either approve or deny a refund.

For information about setting up your server to receive notifications, see
Enabling App Store Server Notifications.

Note

If your app uses SwiftUI, use `refundRequestSheet(for:isPresented:onDismiss:)`
instead. For example usage, see Food Truck: Building a SwiftUI multiplatform
app.

### Test refund requests

The sandbox environment and StoreKit Testing in Xcode both support testing
refund requests. For more information, see Testing refund requests.

## See Also

### Requesting refunds

Testing refund requests

Test your app’s implementation of refund requests, and your app’s and server’s
handling of approved and declined refunds.

`func beginRefundRequest(in: UIWindowScene) ->
Transaction.RefundRequestStatus`

Presents the refund request sheet for the transaction in a window scene.

`func beginRefundRequest(in: NSViewController) ->
Transaction.RefundRequestStatus`

Presents the refund request sheet for the transaction in a view controller.

`static func beginRefundRequest(for: UInt64, in: UIWindowScene) ->
Transaction.RefundRequestStatus`

Presents the refund request sheet for the specified transaction in a window
scene.

`enum Transaction.RefundRequestError`

The error codes for refund requests.

`enum Transaction.RefundRequestStatus`

The status codes for refund requests.

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func != (lhs: Transaction, rhs: Transaction) -> Bool

##  Parameters

`lhs`

    

A value to compare.

`rhs`

    

Another value to compare.

## Discussion

Inequality is the inverse of equality. For any values `a` and `b`, `a != b`
implies that `a == b` is `false`.

This is the default implementation of the not-equal-to operator (`!=`) for any
type that conforms to `Equatable`.

## See Also

### Comparing and hashing transactions

`static func == (Transaction, Transaction) -> Bool`

Returns a Boolean value indicating whether two values are equal.

`func hash(into: inout Hasher)`

Hashes the essential components of this value by feeding them into the given
hasher.

`var hashValue: Int`

The hash value.

Operator

# ==(_:_:)

Returns a Boolean value indicating whether two values are equal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func == (lhs: Transaction, rhs: Transaction) -> Bool

## See Also

### Comparing and hashing transactions

`static func != (Transaction, Transaction) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`func hash(into: inout Hasher)`

Hashes the essential components of this value by feeding them into the given
hasher.

`var hashValue: Int`

The hash value.

Instance Method

# hash(into:)

Hashes the essential components of this value by feeding them into the given
hasher.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    func hash(into hasher: inout Hasher)

##  Parameters

`hasher`

    

The hasher to use when combining the components of this instance.

## Relationships

### From Protocol

  * `Hashable`

## See Also

### Comparing and hashing transactions

`static func != (Transaction, Transaction) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (Transaction, Transaction) -> Bool`

Returns a Boolean value indicating whether two values are equal.

`var hashValue: Int`

The hash value.

Instance Property

# hashValue

The hash value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var hashValue: Int { get }

## Relationships

### From Protocol

  * `Hashable`

## See Also

### Comparing and hashing transactions

`static func != (Transaction, Transaction) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (Transaction, Transaction) -> Bool`

Returns a Boolean value indicating whether two values are equal.

`func hash(into: inout Hasher)`

Hashes the essential components of this value by feeding them into the given
hasher.

Instance Property

# debugDescription

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var debugDescription: String { get }

## Relationships

### From Protocol

  * `CustomDebugStringConvertible`

Instance Property

# currency

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 17.2+  tvOS 16.0+  watchOS
9.0+  visionOS 1.1+  Xcode 14.0+

    
    
    @backDeployed(before: iOS 17.2, macOS 14.2, tvOS 17.2, watchOS 10.2, visionOS 1.1)
    var currency: Locale.Currency? { get }

Instance Property

# currencyCode

iOS 15.0–16.0  Deprecated  iPadOS 15.0–16.0  Deprecated  macOS 12.0–13.0
Deprecated  Mac Catalyst 17.2–17.2  Deprecated  tvOS 15.0–16.0  Deprecated
watchOS 8.0–9.0  Deprecated  visionOS 1.1–1.1  Deprecated  Xcode 13.0–14.0
Deprecated

    
    
    @backDeployed(before: iOS 16.0, macOS 13.0, tvOS 16.0, watchOS 9.0)
    var currencyCode: String? { get }

Instance Property

# price

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 17.2+  tvOS 15.0+  watchOS
8.0+  visionOS 1.1+  Xcode 13.0+

    
    
    @backDeployed(before: iOS 17.2, macOS 14.2, tvOS 17.2, watchOS 10.2, visionOS 1.1)
    var price: Decimal? { get }

