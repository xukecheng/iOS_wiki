Instance Property

# payment

The payment for the transaction.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    var payment: SKPayment { get }

## Discussion

Each payment transaction is created in response to a payment that your
application added to the payment queue.

## See Also

### Getting Transaction Information

`var transactionIdentifier: String?`

A string that uniquely identifies a successful payment transaction.

`var transactionDate: Date?`

The date the transaction was added to the App Store’s payment queue.

`var original: SKPaymentTransaction?`

The transaction that was restored by the App Store.

`var error: (any Error)?`

An object describing the error that occurred while processing the transaction.

`var transactionReceipt: Data?`

A signed receipt that records all information about a successful payment
transaction.

Instance Property

# transactionIdentifier

A string that uniquely identifies a successful payment transaction.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    var transactionIdentifier: String? { get }

## Discussion

The contents of this property are undefined except when `transactionState` is
set to `SKPaymentTransactionState.purchased` or
`SKPaymentTransactionState.restored`. The `transactionIdentifier` is a string
that uniquely identifies an interaction between the user's device and the App
Store, such as a purchase or restore.

This value has the same format as the transaction’s `transaction_id` in the
receipt; however, the values may not be the same.

## See Also

### Getting Transaction Information

`var payment: SKPayment`

The payment for the transaction.

`var transactionDate: Date?`

The date the transaction was added to the App Store’s payment queue.

`var original: SKPaymentTransaction?`

The transaction that was restored by the App Store.

`var error: (any Error)?`

An object describing the error that occurred while processing the transaction.

`var transactionReceipt: Data?`

A signed receipt that records all information about a successful payment
transaction.

Instance Property

# transactionDate

The date the transaction was added to the App Store’s payment queue.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    var transactionDate: Date? { get }

## Discussion

The contents of this property are undefined except when `transactionState` is
set to `SKPaymentTransactionState.purchased` or
`SKPaymentTransactionState.restored`.

## See Also

### Getting Transaction Information

`var payment: SKPayment`

The payment for the transaction.

`var transactionIdentifier: String?`

A string that uniquely identifies a successful payment transaction.

`var original: SKPaymentTransaction?`

The transaction that was restored by the App Store.

`var error: (any Error)?`

An object describing the error that occurred while processing the transaction.

`var transactionReceipt: Data?`

A signed receipt that records all information about a successful payment
transaction.

Instance Property

# original

The transaction that was restored by the App Store.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    var original: SKPaymentTransaction? { get }

## Discussion

The contents of this property are undefined except when `transactionState` is
set to `SKPaymentTransactionState.restored`. When a transaction is restored,
the current transaction holds a new transaction identifier, receipt, and so
on. Your application will read this property to retrieve the restored
transaction.

## See Also

### Getting Transaction Information

`var payment: SKPayment`

The payment for the transaction.

`var transactionIdentifier: String?`

A string that uniquely identifies a successful payment transaction.

`var transactionDate: Date?`

The date the transaction was added to the App Store’s payment queue.

`var error: (any Error)?`

An object describing the error that occurred while processing the transaction.

`var transactionReceipt: Data?`

A signed receipt that records all information about a successful payment
transaction.

Instance Property

# error

An object describing the error that occurred while processing the transaction.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    var error: (any Error)? { get }

## Discussion

The `error` property is undefined except when `transactionState` is set to
`SKPaymentTransactionState.failed`. Your application can read the `error`
property to determine why the transaction failed. For a list of error
constants, see SKErrorDomain in `StoreKit Constants`.

## See Also

### Getting Transaction Information

`var payment: SKPayment`

The payment for the transaction.

`var transactionIdentifier: String?`

A string that uniquely identifies a successful payment transaction.

`var transactionDate: Date?`

The date the transaction was added to the App Store’s payment queue.

`var original: SKPaymentTransaction?`

The transaction that was restored by the App Store.

`var transactionReceipt: Data?`

A signed receipt that records all information about a successful payment
transaction.

### Related Documentation

In-App Purchase Programming Guide

Instance Property

# transactionReceipt

A signed receipt that records all information about a successful payment
transaction.

iOS 3.0–7.0  Deprecated  iPadOS 3.0–7.0  Deprecated  Mac Catalyst 13.0–13.0
Deprecated  tvOS 9.0+

    
    
    var transactionReceipt: Data? { get }

Deprecated

Use the app receipt instead, as described in Receipt Validation Programming
Guide.

## Discussion

The contents of this property are undefined except when `transactionState` is
set to `SKPaymentTransactionState.purchased`.

The receipt is a signed chunk of data that can be sent to the App Store to
verify that the payment was successfully processed. This is most useful when
designing a store that uses a server separate from the iPhone to verify that
payment was processed. For more information on verifying receipts, see Receipt
Validation Programming Guide.

## See Also

### Getting Transaction Information

`var payment: SKPayment`

The payment for the transaction.

`var transactionIdentifier: String?`

A string that uniquely identifies a successful payment transaction.

`var transactionDate: Date?`

The date the transaction was added to the App Store’s payment queue.

`var original: SKPaymentTransaction?`

The transaction that was restored by the App Store.

`var error: (any Error)?`

An object describing the error that occurred while processing the transaction.

Instance Property

# downloads

An array of download objects representing the downloadable content associated
with the transaction.

iOS 6.0–16.0  Deprecated  iPadOS 6.0–16.0  Deprecated  macOS 10.8–13.0
Deprecated  Mac Catalyst 13.1–16.0  Deprecated  tvOS 9.0–16.0  Deprecated
watchOS 6.2–9.0  Deprecated

    
    
    var downloads: [SKDownload] { get }

## Discussion

The contents of this property are undefined except when `transactionState` is
set to `SKPaymentTransactionState.purchased`. The `SKDownload` objects stored
in this property must be used to download the transaction’s content before the
transaction is finished. After the transaction is finished, the download
objects are no longer queueable.

Instance Property

# transactionState

The current state of the transaction.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    var transactionState: SKPaymentTransactionState { get }

## See Also

### Getting Transaction State

`enum SKPaymentTransactionState`

Values representing the state of a transaction.

Instance Property

# payment

The payment for the transaction.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    var payment: SKPayment { get }

## Discussion

Each payment transaction is created in response to a payment that your
application added to the payment queue.

## See Also

### Getting Transaction Information

`var transactionIdentifier: String?`

A string that uniquely identifies a successful payment transaction.

`var transactionDate: Date?`

The date the transaction was added to the App Store’s payment queue.

`var original: SKPaymentTransaction?`

The transaction that was restored by the App Store.

`var error: (any Error)?`

An object describing the error that occurred while processing the transaction.

`var transactionReceipt: Data?`

A signed receipt that records all information about a successful payment
transaction.

Instance Property

# transactionIdentifier

A string that uniquely identifies a successful payment transaction.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    var transactionIdentifier: String? { get }

## Discussion

The contents of this property are undefined except when `transactionState` is
set to `SKPaymentTransactionState.purchased` or
`SKPaymentTransactionState.restored`. The `transactionIdentifier` is a string
that uniquely identifies an interaction between the user's device and the App
Store, such as a purchase or restore.

This value has the same format as the transaction’s `transaction_id` in the
receipt; however, the values may not be the same.

## See Also

### Getting Transaction Information

`var payment: SKPayment`

The payment for the transaction.

`var transactionDate: Date?`

The date the transaction was added to the App Store’s payment queue.

`var original: SKPaymentTransaction?`

The transaction that was restored by the App Store.

`var error: (any Error)?`

An object describing the error that occurred while processing the transaction.

`var transactionReceipt: Data?`

A signed receipt that records all information about a successful payment
transaction.

Instance Property

# transactionDate

The date the transaction was added to the App Store’s payment queue.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    var transactionDate: Date? { get }

## Discussion

The contents of this property are undefined except when `transactionState` is
set to `SKPaymentTransactionState.purchased` or
`SKPaymentTransactionState.restored`.

## See Also

### Getting Transaction Information

`var payment: SKPayment`

The payment for the transaction.

`var transactionIdentifier: String?`

A string that uniquely identifies a successful payment transaction.

`var original: SKPaymentTransaction?`

The transaction that was restored by the App Store.

`var error: (any Error)?`

An object describing the error that occurred while processing the transaction.

`var transactionReceipt: Data?`

A signed receipt that records all information about a successful payment
transaction.

Instance Property

# original

The transaction that was restored by the App Store.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    var original: SKPaymentTransaction? { get }

## Discussion

The contents of this property are undefined except when `transactionState` is
set to `SKPaymentTransactionState.restored`. When a transaction is restored,
the current transaction holds a new transaction identifier, receipt, and so
on. Your application will read this property to retrieve the restored
transaction.

## See Also

### Getting Transaction Information

`var payment: SKPayment`

The payment for the transaction.

`var transactionIdentifier: String?`

A string that uniquely identifies a successful payment transaction.

`var transactionDate: Date?`

The date the transaction was added to the App Store’s payment queue.

`var error: (any Error)?`

An object describing the error that occurred while processing the transaction.

`var transactionReceipt: Data?`

A signed receipt that records all information about a successful payment
transaction.

Instance Property

# error

An object describing the error that occurred while processing the transaction.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    var error: (any Error)? { get }

## Discussion

The `error` property is undefined except when `transactionState` is set to
`SKPaymentTransactionState.failed`. Your application can read the `error`
property to determine why the transaction failed. For a list of error
constants, see SKErrorDomain in `StoreKit Constants`.

## See Also

### Getting Transaction Information

`var payment: SKPayment`

The payment for the transaction.

`var transactionIdentifier: String?`

A string that uniquely identifies a successful payment transaction.

`var transactionDate: Date?`

The date the transaction was added to the App Store’s payment queue.

`var original: SKPaymentTransaction?`

The transaction that was restored by the App Store.

`var transactionReceipt: Data?`

A signed receipt that records all information about a successful payment
transaction.

### Related Documentation

In-App Purchase Programming Guide

Instance Property

# transactionReceipt

A signed receipt that records all information about a successful payment
transaction.

iOS 3.0–7.0  Deprecated  iPadOS 3.0–7.0  Deprecated  Mac Catalyst 13.0–13.0
Deprecated  tvOS 9.0+

    
    
    var transactionReceipt: Data? { get }

Deprecated

Use the app receipt instead, as described in Receipt Validation Programming
Guide.

## Discussion

The contents of this property are undefined except when `transactionState` is
set to `SKPaymentTransactionState.purchased`.

The receipt is a signed chunk of data that can be sent to the App Store to
verify that the payment was successfully processed. This is most useful when
designing a store that uses a server separate from the iPhone to verify that
payment was processed. For more information on verifying receipts, see Receipt
Validation Programming Guide.

## See Also

### Getting Transaction Information

`var payment: SKPayment`

The payment for the transaction.

`var transactionIdentifier: String?`

A string that uniquely identifies a successful payment transaction.

`var transactionDate: Date?`

The date the transaction was added to the App Store’s payment queue.

`var original: SKPaymentTransaction?`

The transaction that was restored by the App Store.

`var error: (any Error)?`

An object describing the error that occurred while processing the transaction.

Instance Property

# downloads

An array of download objects representing the downloadable content associated
with the transaction.

iOS 6.0–16.0  Deprecated  iPadOS 6.0–16.0  Deprecated  macOS 10.8–13.0
Deprecated  Mac Catalyst 13.1–16.0  Deprecated  tvOS 9.0–16.0  Deprecated
watchOS 6.2–9.0  Deprecated

    
    
    var downloads: [SKDownload] { get }

## Discussion

The contents of this property are undefined except when `transactionState` is
set to `SKPaymentTransactionState.purchased`. The `SKDownload` objects stored
in this property must be used to download the transaction’s content before the
transaction is finished. After the transaction is finished, the download
objects are no longer queueable.

Instance Property

# transactionState

The current state of the transaction.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    var transactionState: SKPaymentTransactionState { get }

## See Also

### Getting Transaction State

`enum SKPaymentTransactionState`

Values representing the state of a transaction.

