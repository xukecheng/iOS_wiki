Enumeration Case

# Transaction.RefundRequestStatus.userCancelled

The user canceled submission of their refund request.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+  Xcode 13.0+

    
    
    case userCancelled

## See Also

### Getting Refund Request Status

`case success`

The App Store has received the refund request.

Enumeration Case

# Transaction.RefundRequestStatus.success

The App Store has received the refund request.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+  Xcode 13.0+

    
    
    case success

## See Also

### Getting Refund Request Status

`case userCancelled`

The user canceled submission of their refund request.

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func != (lhs: Transaction.RefundRequestStatus, rhs: Transaction.RefundRequestStatus) -> Bool

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

### Comparing and Hashing Refund Request Status

`static func == (Transaction.RefundRequestStatus,
Transaction.RefundRequestStatus) -> Bool`

Returns a Boolean value indicating whether two values are equal.

`func hash(into: inout Hasher)`

Hashes the essential components of this value by feeding them into the given
hasher.

`var hashValue: Int`

The hash value.

Operator

# ==(_:_:)

Returns a Boolean value indicating whether two values are equal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func == (a: Transaction.RefundRequestStatus, b: Transaction.RefundRequestStatus) -> Bool

## See Also

### Comparing and Hashing Refund Request Status

`static func != (Transaction.RefundRequestStatus,
Transaction.RefundRequestStatus) -> Bool`

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

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+  Xcode 13.0+

    
    
    func hash(into hasher: inout Hasher)

##  Parameters

`hasher`

    

The hasher to use when combining the components of this instance.

## Relationships

### From Protocol

  * `Hashable`

## See Also

### Comparing and Hashing Refund Request Status

`static func != (Transaction.RefundRequestStatus,
Transaction.RefundRequestStatus) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (Transaction.RefundRequestStatus,
Transaction.RefundRequestStatus) -> Bool`

Returns a Boolean value indicating whether two values are equal.

`var hashValue: Int`

The hash value.

Instance Property

# hashValue

The hash value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var hashValue: Int { get }

## Relationships

### From Protocol

  * `Hashable`

## See Also

### Comparing and Hashing Refund Request Status

`static func != (Transaction.RefundRequestStatus,
Transaction.RefundRequestStatus) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (Transaction.RefundRequestStatus,
Transaction.RefundRequestStatus) -> Bool`

Returns a Boolean value indicating whether two values are equal.

`func hash(into: inout Hasher)`

Hashes the essential components of this value by feeding them into the given
hasher.

