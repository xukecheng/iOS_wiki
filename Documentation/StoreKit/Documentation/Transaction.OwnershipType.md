Type Property

# familyShared

The transaction belongs to a family member who benefits from the service.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let familyShared: Transaction.OwnershipType

## Discussion

For more information about Family Sharing, see Turn on Family Sharing for in-
app purchases.

## See Also

### Getting ownership types

`static let purchased: Transaction.OwnershipType`

The transaction belongs to the purchaser.

Type Property

# purchased

The transaction belongs to the purchaser.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let purchased: Transaction.OwnershipType

## See Also

### Getting ownership types

`static let familyShared: Transaction.OwnershipType`

The transaction belongs to a family member who benefits from the service.

Instance Property

# localizedDescription

The localized text that describes the ownership type.

iOS 15.4+  iPadOS 15.4+  macOS 12.3+  Mac Catalyst 15.4+  tvOS 15.4+  watchOS
8.5+  visionOS 1.0+  Xcode 13.3+

    
    
    var localizedDescription: String { get }

Instance Property

# rawValue

The raw string value that represents a transaction ownership type.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let rawValue: String

## Discussion

Use the raw value to help parse the `jsonRepresentation` property of
`Transaction`. The JSON data contains a string representation of the
transaction ownership type, which is its raw value. You can compare the JSON
data directly to the ownership type’s `rawValue`.

You can also use the `rawValue` to create a transaction ownership type
instance by calling `init(rawValue:)`.

## Relationships

### From Protocol

  * `RawRepresentable`

## See Also

### Accessing the raw value

`typealias Transaction.OwnershipType.RawValue`

The type that represents the raw value of a transaction’s ownership type.

Type Alias

# Transaction.OwnershipType.RawValue

The type that represents the raw value of a transaction’s ownership type.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    typealias Transaction.OwnershipType.RawValue = String

## See Also

### Accessing the raw value

`let rawValue: String`

The raw string value that represents a transaction ownership type.

Initializer

# init(rawValue:)

Creates a transaction ownership type instance from a raw value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    init(rawValue: String)

##  Parameters

`rawValue`

    

A string that represents a transaction ownership type.

## Discussion

Typically, you get a transaction ownership type from the `ownershipType`
property in a `Transaction`, and you don’t need to instantiate it yourself.

However, if you use the `jsonRepresentation` property of `Transaction`, you
can use raw values and the initializer to help parse the JSON. The JSON
contains the string representation of the ownership type, which is its raw
value. Call `init(rawValue:)` to create your own instance from that raw value.
Alternatively, you can compare the JSON data directly to the ownership type’s
`rawValue`.

## Relationships

### From Protocol

  * `RawRepresentable`

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func != (lhs: Transaction.OwnershipType, rhs: Transaction.OwnershipType) -> Bool

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

### Comparing and hashing types

`func hash(into: inout Hasher)`

Hashes the essential components of the value by feeding them into the given
hasher.

`var hashValue: Int`

The hash value.

Instance Method

# hash(into:)

Hashes the essential components of the value by feeding them into the given
hasher.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    func hash(into hasher: inout Hasher)

##  Parameters

`hasher`

    

The hasher to use when combining the components of this instance.

## See Also

### Comparing and hashing types

`static func != (Transaction.OwnershipType, Transaction.OwnershipType) ->
Bool`

Returns a Boolean value indicating whether two values are not equal.

`var hashValue: Int`

The hash value.

Instance Property

# hashValue

The hash value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var hashValue: Int { get }

## See Also

### Comparing and hashing types

`static func != (Transaction.OwnershipType, Transaction.OwnershipType) ->
Bool`

Returns a Boolean value indicating whether two values are not equal.

`func hash(into: inout Hasher)`

Hashes the essential components of the value by feeding them into the given
hasher.

