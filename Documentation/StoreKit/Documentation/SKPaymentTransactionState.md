Enumeration Case

# SKPaymentTransactionState.purchasing

A transaction that is being processed by the App Store.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    case purchasing = 0

Enumeration Case

# SKPaymentTransactionState.purchased

A successfully processed transaction.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    case purchased = 1

## Discussion

Your application should provide the content the user purchased.

Enumeration Case

# SKPaymentTransactionState.failed

A failed transaction.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    case failed = 2

## Discussion

Check the `error` property to determine what happened.

Enumeration Case

# SKPaymentTransactionState.restored

A transaction that restores content previously purchased by the user.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    case restored = 3

## Discussion

Read the `original` property to obtain information about the original
purchase.

Enumeration Case

# SKPaymentTransactionState.deferred

A transaction that is in the queue, but its final status is pending external
action such as Ask to Buy.

iOS 8.0+  iPadOS 8.0+  macOS 10.10+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    case deferred = 4

## Discussion

Update your UI to show the deferred state, and wait for another callback that
indicates the final status.

Enumeration Case

# SKPaymentTransactionState.purchasing

A transaction that is being processed by the App Store.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    case purchasing = 0

Enumeration Case

# SKPaymentTransactionState.purchased

A successfully processed transaction.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    case purchased = 1

## Discussion

Your application should provide the content the user purchased.

Enumeration Case

# SKPaymentTransactionState.failed

A failed transaction.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    case failed = 2

## Discussion

Check the `error` property to determine what happened.

Enumeration Case

# SKPaymentTransactionState.restored

A transaction that restores content previously purchased by the user.

iOS 3.0+  iPadOS 3.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    case restored = 3

## Discussion

Read the `original` property to obtain information about the original
purchase.

Enumeration Case

# SKPaymentTransactionState.deferred

A transaction that is in the queue, but its final status is pending external
action such as Ask to Buy.

iOS 8.0+  iPadOS 8.0+  macOS 10.10+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
6.2+  visionOS 1.0+

    
    
    case deferred = 4

## Discussion

Update your UI to show the deferred state, and wait for another callback that
indicates the final status.

