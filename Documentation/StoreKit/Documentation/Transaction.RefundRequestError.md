Enumeration Case

# Transaction.RefundRequestError.duplicateRequest

The App Store has already received a refund request for this in-app purchase.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+  Xcode 13.0+

    
    
    case duplicateRequest

## Discussion

StoreKit returns this error if the App Store has previously received a refund
request for this transaction and the refund decision is still pending, has
been previously denied, or has been previously approved.

Consider checking the transaction’s `revocationDate` or `revocationReason`
before calling `beginRefundRequest(for:in:)` to identify whether the App Store
has already refunded the transaction.

## See Also

### Error Enumeration

`case failed`

The refund request submission failed.

Enumeration Case

# Transaction.RefundRequestError.failed

The refund request submission failed.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+  Xcode 13.0+

    
    
    case failed

## Discussion

A refund request submission can fail for many reasons, such as having an
invalid transaction identifier, or if the App Store can’t process the request
for some other reason.

## See Also

### Error Enumeration

`case duplicateRequest`

The App Store has already received a refund request for this in-app purchase.

Instance Property

# errorDescription

A description of the error, suitable for debugging.

iOS 15.4+  iPadOS 15.4+  macOS 12.3+  Mac Catalyst 15.4+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+  Xcode 13.3+

    
    
    var errorDescription: String? { get }

## Relationships

### From Protocol

  * `LocalizedError`

## See Also

### Error Descriptions

`var localizedDescription: String`

A localized error description.

`var failureReason: String?`

A localized message describing the reason for the failure.

`var helpAnchor: String?`

A message providing “help” text if the user requests help by pressing an alert
panel help anchor button.

`var recoverySuggestion: String?`

A message containing a suggestion for recovering from the error.

Instance Property

# localizedDescription

A localized error description.

iOS 8.0+  iPadOS 8.0+  macOS 10.10+  Mac Catalyst 15.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+  Xcode 7.1+

    
    
    var localizedDescription: String { get }

## See Also

### Error Descriptions

`var errorDescription: String?`

A description of the error, suitable for debugging.

`var failureReason: String?`

A localized message describing the reason for the failure.

`var helpAnchor: String?`

A message providing “help” text if the user requests help by pressing an alert
panel help anchor button.

`var recoverySuggestion: String?`

A message containing a suggestion for recovering from the error.

Instance Property

# failureReason

A localized message describing the reason for the failure.

iOS 15.4+  iPadOS 15.4+  macOS 12.3+  Mac Catalyst 15.4+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+  Xcode 13.3+

    
    
    var failureReason: String? { get }

## Relationships

### From Protocol

  * `LocalizedError`

## See Also

### Error Descriptions

`var errorDescription: String?`

A description of the error, suitable for debugging.

`var localizedDescription: String`

A localized error description.

`var helpAnchor: String?`

A message providing “help” text if the user requests help by pressing an alert
panel help anchor button.

`var recoverySuggestion: String?`

A message containing a suggestion for recovering from the error.

Instance Property

# helpAnchor

A message providing “help” text if the user requests help by pressing an alert
panel help anchor button.

iOS 8.0+  iPadOS 8.0+  macOS 10.10+  Mac Catalyst 15.4+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+  Xcode 7.1+

    
    
    var helpAnchor: String? { get }

## See Also

### Error Descriptions

`var errorDescription: String?`

A description of the error, suitable for debugging.

`var localizedDescription: String`

A localized error description.

`var failureReason: String?`

A localized message describing the reason for the failure.

`var recoverySuggestion: String?`

A message containing a suggestion for recovering from the error.

Instance Property

# recoverySuggestion

A message containing a suggestion for recovering from the error.

iOS 15.4+  iPadOS 15.4+  macOS 12.3+  Mac Catalyst 15.4+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+  Xcode 13.3+

    
    
    var recoverySuggestion: String? { get }

## Relationships

### From Protocol

  * `LocalizedError`

## See Also

### Error Descriptions

`var errorDescription: String?`

A description of the error, suitable for debugging.

`var localizedDescription: String`

A localized error description.

`var failureReason: String?`

A localized message describing the reason for the failure.

`var helpAnchor: String?`

A message providing “help” text if the user requests help by pressing an alert
panel help anchor button.

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func != (lhs: Transaction.RefundRequestError, rhs: Transaction.RefundRequestError) -> Bool

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

### Error Comparisons

`static func == (Transaction.RefundRequestError,
Transaction.RefundRequestError) -> Bool`

`var hashValue: Int`

`func hash(into: inout Hasher)`

Operator

# ==(_:_:)

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func == (a: Transaction.RefundRequestError, b: Transaction.RefundRequestError) -> Bool

## See Also

### Error Comparisons

`static func != (Transaction.RefundRequestError,
Transaction.RefundRequestError) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`var hashValue: Int`

`func hash(into: inout Hasher)`

Instance Property

# hashValue

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var hashValue: Int { get }

## Relationships

### From Protocol

  * `Hashable`

## See Also

### Error Comparisons

`static func != (Transaction.RefundRequestError,
Transaction.RefundRequestError) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (Transaction.RefundRequestError,
Transaction.RefundRequestError) -> Bool`

`func hash(into: inout Hasher)`

Instance Method

# hash(into:)

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+  Xcode 13.0+

    
    
    func hash(into hasher: inout Hasher)

## Relationships

### From Protocol

  * `Hashable`

## See Also

### Error Comparisons

`static func != (Transaction.RefundRequestError,
Transaction.RefundRequestError) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (Transaction.RefundRequestError,
Transaction.RefundRequestError) -> Bool`

`var hashValue: Int`

