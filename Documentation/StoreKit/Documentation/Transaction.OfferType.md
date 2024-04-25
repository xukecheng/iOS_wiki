Type Property

# introductory

An introductory offer for an auto-renewable subscription.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let introductory: Transaction.OfferType

## Discussion

For more information about introductory offers, see Set up introductory offers
for auto-renewable subscriptions.

## See Also

### Getting offer types

`static let promotional: Transaction.OfferType`

A promotional offer for an auto-renewable subscription.

`static let code: Transaction.OfferType`

An offer with a subscription offer code, for an auto-renewable subscription.

Type Property

# promotional

A promotional offer for an auto-renewable subscription.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let promotional: Transaction.OfferType

## Discussion

For more information about promotional offers, see Set up promotional offers
for auto-renewable subscriptions.

## See Also

### Getting offer types

`static let introductory: Transaction.OfferType`

An introductory offer for an auto-renewable subscription.

`static let code: Transaction.OfferType`

An offer with a subscription offer code, for an auto-renewable subscription.

Type Property

# code

An offer with a subscription offer code, for an auto-renewable subscription.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let code: Transaction.OfferType

## Discussion

For more information about offer codes, see Set up offer codes.

## See Also

### Getting offer types

`static let introductory: Transaction.OfferType`

An introductory offer for an auto-renewable subscription.

`static let promotional: Transaction.OfferType`

A promotional offer for an auto-renewable subscription.

Instance Property

# localizedDescription

The localized text that describes the offer type.

iOS 15.4+  iPadOS 15.4+  macOS 12.3+  Mac Catalyst 15.4+  tvOS 15.4+  watchOS
8.5+  visionOS 1.0+  Xcode 13.3+

    
    
    var localizedDescription: String { get }

Initializer

# init(rawValue:)

Create an offer type from a raw value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    init(rawValue: Int)

## Relationships

### From Protocol

  * `RawRepresentable`

## See Also

### Creating an offer type

`let rawValue: Int`

The offer type as a raw value.

`typealias Transaction.OfferType.RawValue`

A type representing the raw value of an offer type.

Instance Property

# rawValue

The offer type as a raw value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let rawValue: Int

## Relationships

### From Protocol

  * `RawRepresentable`

## See Also

### Creating an offer type

`init(rawValue: Int)`

Create an offer type from a raw value.

`typealias Transaction.OfferType.RawValue`

A type representing the raw value of an offer type.

Type Alias

# Transaction.OfferType.RawValue

A type representing the raw value of an offer type.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    typealias Transaction.OfferType.RawValue = Int

## See Also

### Creating an offer type

`init(rawValue: Int)`

Create an offer type from a raw value.

`let rawValue: Int`

The offer type as a raw value.

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func != (lhs: Transaction.OfferType, rhs: Transaction.OfferType) -> Bool

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

### Comparing and hashing offer types

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

## See Also

### Comparing and hashing offer types

`static func != (Transaction.OfferType, Transaction.OfferType) -> Bool`

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

### Comparing and hashing offer types

`static func != (Transaction.OfferType, Transaction.OfferType) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`func hash(into: inout Hasher)`

Hashes the essential components of this value by feeding them into the given
hasher.

