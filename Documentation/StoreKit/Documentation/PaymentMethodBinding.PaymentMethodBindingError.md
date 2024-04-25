Enumeration Case

# PaymentMethodBinding.PaymentMethodBindingError.failed

The initialization or binding operation failed.

iOS 16.4+  iPadOS 16.4+  Mac Catalyst 16.4+  visionOS 1.0+  Xcode 14.3+

    
    
    case failed

## Discussion

The methods of the `PaymentMethodBinding` struct can fail if the app isn’t
entitled to use this API, or if other errors occur.

## See Also

### Getting error codes

`case invalidPinningID`

The in-app binding identifier is invalid or expired.

`case notEligible`

The user isn’t eligible.

Enumeration Case

# PaymentMethodBinding.PaymentMethodBindingError.invalidPinningID

The in-app binding identifier is invalid or expired.

iOS 16.4+  iPadOS 16.4+  Mac Catalyst 16.4+  visionOS 1.0+  Xcode 14.3+

    
    
    case invalidPinningID

## Discussion

For more information about the identifier, see `id`.

## See Also

### Getting error codes

`case failed`

The initialization or binding operation failed.

`case notEligible`

The user isn’t eligible.

Enumeration Case

# PaymentMethodBinding.PaymentMethodBindingError.notEligible

The user isn’t eligible.

iOS 16.4+  iPadOS 16.4+  Mac Catalyst 16.4+  visionOS 1.0+  Xcode 14.3+

    
    
    case notEligible

## See Also

### Getting error codes

`case failed`

The initialization or binding operation failed.

`case invalidPinningID`

The in-app binding identifier is invalid or expired.

Instance Property

# errorDescription

A description of the error, suitable for debugging.

iOS 16.4+  iPadOS 16.4+  Mac Catalyst 16.4+  visionOS 1.0+  Xcode 14.3+

    
    
    var errorDescription: String? { get }

## Relationships

### From Protocol

  * `LocalizedError`

## See Also

### Getting error descriptions

`var failureReason: String?`

A string that describes the reason for the failure.

`var helpAnchor: String?`

A localized message that provides additional information if the user requests
help.

`var localizedDescription: String`

A localized message that describes the error.

`var recoverySuggestion: String?`

A message that contains a suggestion for recovering from the error.

Instance Property

# failureReason

A string that describes the reason for the failure.

iOS 16.4+  iPadOS 16.4+  Mac Catalyst 16.4+  visionOS 1.0+  Xcode 14.3+

    
    
    var failureReason: String? { get }

## Relationships

### From Protocol

  * `LocalizedError`

## See Also

### Getting error descriptions

`var errorDescription: String?`

A description of the error, suitable for debugging.

`var helpAnchor: String?`

A localized message that provides additional information if the user requests
help.

`var localizedDescription: String`

A localized message that describes the error.

`var recoverySuggestion: String?`

A message that contains a suggestion for recovering from the error.

Instance Property

# helpAnchor

A localized message that provides additional information if the user requests
help.

iOS 8.0+  iPadOS 8.0+  Mac Catalyst 16.4+  visionOS 1.0+  Xcode 14.3+

    
    
    var helpAnchor: String? { get }

## See Also

### Getting error descriptions

`var errorDescription: String?`

A description of the error, suitable for debugging.

`var failureReason: String?`

A string that describes the reason for the failure.

`var localizedDescription: String`

A localized message that describes the error.

`var recoverySuggestion: String?`

A message that contains a suggestion for recovering from the error.

Instance Property

# localizedDescription

A localized message that describes the error.

iOS 8.0+  iPadOS 8.0+  Mac Catalyst 16.4+  visionOS 1.0+  Xcode 14.3+

    
    
    var localizedDescription: String { get }

## See Also

### Getting error descriptions

`var errorDescription: String?`

A description of the error, suitable for debugging.

`var failureReason: String?`

A string that describes the reason for the failure.

`var helpAnchor: String?`

A localized message that provides additional information if the user requests
help.

`var recoverySuggestion: String?`

A message that contains a suggestion for recovering from the error.

Instance Property

# recoverySuggestion

A message that contains a suggestion for recovering from the error.

iOS 16.4+  iPadOS 16.4+  Mac Catalyst 16.4+  visionOS 1.0+  Xcode 14.3+

    
    
    var recoverySuggestion: String? { get }

## Relationships

### From Protocol

  * `LocalizedError`

## See Also

### Getting error descriptions

`var errorDescription: String?`

A description of the error, suitable for debugging.

`var failureReason: String?`

A string that describes the reason for the failure.

`var helpAnchor: String?`

A localized message that provides additional information if the user requests
help.

`var localizedDescription: String`

A localized message that describes the error.

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 16.4+  iPadOS 16.4+  Mac Catalyst 16.4+  visionOS 1.0+  Xcode 14.3+

    
    
    static func != (lhs: PaymentMethodBinding.PaymentMethodBindingError, rhs: PaymentMethodBinding.PaymentMethodBindingError) -> Bool

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

### Comparing and hashing errors

`static func == (PaymentMethodBinding.PaymentMethodBindingError,
PaymentMethodBinding.PaymentMethodBindingError) -> Bool`

Returns a Boolean value that indicates whether two values are equal.

`func hash(into: inout Hasher)`

Hashes the essential components of the value by feeding them into the given
hasher.

`var hashValue: Int`

The hash value.

Operator

# ==(_:_:)

Returns a Boolean value that indicates whether two values are equal.

iOS 16.4+  iPadOS 16.4+  Mac Catalyst 16.4+  visionOS 1.0+  Xcode 14.3+

    
    
    static func == (a: PaymentMethodBinding.PaymentMethodBindingError, b: PaymentMethodBinding.PaymentMethodBindingError) -> Bool

## See Also

### Comparing and hashing errors

`static func != (PaymentMethodBinding.PaymentMethodBindingError,
PaymentMethodBinding.PaymentMethodBindingError) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`func hash(into: inout Hasher)`

Hashes the essential components of the value by feeding them into the given
hasher.

`var hashValue: Int`

The hash value.

Instance Method

# hash(into:)

Hashes the essential components of the value by feeding them into the given
hasher.

iOS 16.4+  iPadOS 16.4+  Mac Catalyst 16.4+  visionOS 1.0+  Xcode 14.3+

    
    
    func hash(into hasher: inout Hasher)

## Relationships

### From Protocol

  * `Hashable`

## See Also

### Comparing and hashing errors

`static func != (PaymentMethodBinding.PaymentMethodBindingError,
PaymentMethodBinding.PaymentMethodBindingError) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (PaymentMethodBinding.PaymentMethodBindingError,
PaymentMethodBinding.PaymentMethodBindingError) -> Bool`

Returns a Boolean value that indicates whether two values are equal.

`var hashValue: Int`

The hash value.

Instance Property

# hashValue

The hash value.

iOS 16.4+  iPadOS 16.4+  Mac Catalyst 16.4+  visionOS 1.0+  Xcode 14.3+

    
    
    var hashValue: Int { get }

## Relationships

### From Protocol

  * `Hashable`

## See Also

### Comparing and hashing errors

`static func != (PaymentMethodBinding.PaymentMethodBindingError,
PaymentMethodBinding.PaymentMethodBindingError) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (PaymentMethodBinding.PaymentMethodBindingError,
PaymentMethodBinding.PaymentMethodBindingError) -> Bool`

Returns a Boolean value that indicates whether two values are equal.

`func hash(into: inout Hasher)`

Hashes the essential components of the value by feeding them into the given
hasher.

