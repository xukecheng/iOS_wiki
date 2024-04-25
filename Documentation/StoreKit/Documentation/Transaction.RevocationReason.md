Type Property

# developerIssue

The value that indicates a customer canceled the transaction due to an actual
or perceived issue within your app.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let developerIssue: Transaction.RevocationReason

## See Also

### Revocation reasons

`static let other: Transaction.RevocationReason`

The value that indicates a customer canceled the transaction for other
reasons.

`typealias Transaction.RevocationReason.RawValue`

The type that represents the raw value of a transaction revocation reason.

Type Property

# other

The value that indicates a customer canceled the transaction for other
reasons.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let other: Transaction.RevocationReason

## Discussion

Other reasons may include, for example, an accidental purchase.

## See Also

### Revocation reasons

`static let developerIssue: Transaction.RevocationReason`

The value that indicates a customer canceled the transaction due to an actual
or perceived issue within your app.

`typealias Transaction.RevocationReason.RawValue`

The type that represents the raw value of a transaction revocation reason.

Type Alias

# Transaction.RevocationReason.RawValue

The type that represents the raw value of a transaction revocation reason.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    typealias Transaction.RevocationReason.RawValue = Int

## See Also

### Revocation reasons

`static let developerIssue: Transaction.RevocationReason`

The value that indicates a customer canceled the transaction due to an actual
or perceived issue within your app.

`static let other: Transaction.RevocationReason`

The value that indicates a customer canceled the transaction for other
reasons.

Instance Property

# localizedDescription

The localized text that describes the revocation reason.

iOS 15.4+  iPadOS 15.4+  macOS 12.3+  Mac Catalyst 15.4+  tvOS 15.4+  watchOS
8.5+  visionOS 1.0+  Xcode 13.3+

    
    
    var localizedDescription: String { get }

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func != (lhs: Transaction.RevocationReason, rhs: Transaction.RevocationReason) -> Bool

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

### Comparing and hashing reasons

`func hash(into: inout Hasher)`

Hashes the essential components of this value by feeding them into the given
hasher.

`var hashValue: Int`

The hash value.

`let rawValue: Int`

The raw value of a transaction revocation reason.

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

## See Also

### Comparing and hashing reasons

`static func != (Transaction.RevocationReason, Transaction.RevocationReason)
-> Bool`

Returns a Boolean value indicating whether two values are not equal.

`var hashValue: Int`

The hash value.

`let rawValue: Int`

The raw value of a transaction revocation reason.

Instance Property

# hashValue

The hash value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var hashValue: Int { get }

## See Also

### Comparing and hashing reasons

`static func != (Transaction.RevocationReason, Transaction.RevocationReason)
-> Bool`

Returns a Boolean value indicating whether two values are not equal.

`func hash(into: inout Hasher)`

Hashes the essential components of this value by feeding them into the given
hasher.

`let rawValue: Int`

The raw value of a transaction revocation reason.

Instance Property

# rawValue

The raw value of a transaction revocation reason.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let rawValue: Int

## Relationships

### From Protocol

  * `RawRepresentable`

## See Also

### Comparing and hashing reasons

`static func != (Transaction.RevocationReason, Transaction.RevocationReason)
-> Bool`

Returns a Boolean value indicating whether two values are not equal.

`func hash(into: inout Hasher)`

Hashes the essential components of this value by feeding them into the given
hasher.

`var hashValue: Int`

The hash value.

Initializer

# init(rawValue:)

Creates a revocation reason from a raw value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    init(rawValue: Int)

## Relationships

### From Protocol

  * `RawRepresentable`

