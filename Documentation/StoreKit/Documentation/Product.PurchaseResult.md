Enumeration Case

# Product.PurchaseResult.success(_:)

The purchase succeeded and results in a transaction.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    case success(VerificationResult<Transaction>)

## See Also

### Getting the Purchase Results

`case userCancelled`

The user canceled the purchase.

`case pending`

The purchase is pending, and requires action from the customer.

Enumeration Case

# Product.PurchaseResult.userCancelled

The user canceled the purchase.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    case userCancelled

## See Also

### Getting the Purchase Results

`case success(VerificationResult<Transaction>)`

The purchase succeeded and results in a transaction.

`case pending`

The purchase is pending, and requires action from the customer.

Enumeration Case

# Product.PurchaseResult.pending

The purchase is pending, and requires action from the customer.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    case pending

## Discussion

If a pending purchase succeeds, StoreKit delivers the resulting `Transaction`
in the transaction `updates`.

## See Also

### Getting the Purchase Results

`case success(VerificationResult<Transaction>)`

The purchase succeeded and results in a transaction.

`case userCancelled`

The user canceled the purchase.

