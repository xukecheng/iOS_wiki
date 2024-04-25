Type Property

# purchase

A transaction reason that indicates a purchase is initiated by a customer.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    static let purchase: Transaction.Reason

## Discussion

The customer initiated the purchase, which may be for any in-app purchase
type: consumable, non-consumable, non-renewing subscription, or auto-renewable
subscription.

## See Also

### Transaction reasons

`static let renewal: Transaction.Reason`

A transaction reason that indicates the App Store server initiated a purchase
transaction to renew an auto-renewable subscription.

Type Property

# renewal

A transaction reason that indicates the App Store server initiated a purchase
transaction to renew an auto-renewable subscription.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    static let renewal: Transaction.Reason

## See Also

### Transaction reasons

`static let purchase: Transaction.Reason`

A transaction reason that indicates a purchase is initiated by a customer.

Initializer

# init(rawValue:)

Returns a new transaction reason with the specified raw value.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    init(rawValue: String)

## Relationships

### From Protocol

  * `RawRepresentable`

## See Also

### Creating transaction reasons

`let rawValue: String`

The corresponding value of the raw type.

`typealias Transaction.Reason.RawValue`

A type that represents the raw value of a transaction reason.

Instance Property

# rawValue

The corresponding value of the raw type.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    let rawValue: String

## Relationships

### From Protocol

  * `RawRepresentable`

## See Also

### Creating transaction reasons

`init(rawValue: String)`

Returns a new transaction reason with the specified raw value.

`typealias Transaction.Reason.RawValue`

A type that represents the raw value of a transaction reason.

Type Alias

# Transaction.Reason.RawValue

A type that represents the raw value of a transaction reason.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    typealias Transaction.Reason.RawValue = String

## See Also

### Creating transaction reasons

`init(rawValue: String)`

Returns a new transaction reason with the specified raw value.

`let rawValue: String`

The corresponding value of the raw type.

Instance Property

# hashValue

The hash value.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    var hashValue: Int { get }

## See Also

### Comparing and hashing

`func hash(into: inout Hasher)`

Hashes the essential components of the value by feeding them into the given
hasher.

`static func != (Transaction.Reason, Transaction.Reason) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

Instance Method

# hash(into:)

Hashes the essential components of the value by feeding them into the given
hasher.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    func hash(into hasher: inout Hasher)

## See Also

### Comparing and hashing

`var hashValue: Int`

The hash value.

`static func != (Transaction.Reason, Transaction.Reason) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    static func != (lhs: Transaction.Reason, rhs: Transaction.Reason) -> Bool

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

### Comparing and hashing

`var hashValue: Int`

The hash value.

`func hash(into: inout Hasher)`

Hashes the essential components of the value by feeding them into the given
hasher.

