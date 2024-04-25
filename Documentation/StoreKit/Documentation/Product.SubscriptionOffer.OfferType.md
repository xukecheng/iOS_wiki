Type Property

# introductory

An introductory offer for a subscription.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let introductory: Product.SubscriptionOffer.OfferType

## Discussion

For more information about introductory offers, see Set an introductory offer
for an auto-renewable subscription.

## See Also

### Getting the Offer Types

`static let promotional: Product.SubscriptionOffer.OfferType`

A promotional offer.

Type Property

# promotional

A promotional offer.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let promotional: Product.SubscriptionOffer.OfferType

## Discussion

For more information about promotional offers, see Set up promotional offers
for auto-renewable subscriptions.

## See Also

### Getting the Offer Types

`static let introductory: Product.SubscriptionOffer.OfferType`

An introductory offer for a subscription.

Instance Property

# localizedDescription

iOS 15.4+  iPadOS 15.4+  macOS 12.3+  Mac Catalyst 15.4+  tvOS 15.4+  watchOS
8.5+  visionOS 1.0+  Xcode 13.3+

    
    
    var localizedDescription: String { get }

Initializer

# init(rawValue:)

A raw value representing a subscription offer type.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    init(rawValue: String)

##  Parameters

`rawValue`

    

A string representing the offer type.

## Relationships

### From Protocol

  * `RawRepresentable`

## See Also

### Creating an Offer Type

`typealias Product.SubscriptionOffer.OfferType.RawValue`

`let rawValue: String`

A string representing the raw value of the subscription offer type.

Type Alias

# Product.SubscriptionOffer.OfferType.RawValue

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    typealias Product.SubscriptionOffer.OfferType.RawValue = String

## See Also

### Creating an Offer Type

`init(rawValue: String)`

A raw value representing a subscription offer type.

`let rawValue: String`

A string representing the raw value of the subscription offer type.

Instance Property

# rawValue

A string representing the raw value of the subscription offer type.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let rawValue: String

## Relationships

### From Protocol

  * `RawRepresentable`

## See Also

### Creating an Offer Type

`init(rawValue: String)`

A raw value representing a subscription offer type.

`typealias Product.SubscriptionOffer.OfferType.RawValue`

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func != (lhs: Product.SubscriptionOffer.OfferType, rhs: Product.SubscriptionOffer.OfferType) -> Bool

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

### Comparing and Hashing Offer Types

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

### Comparing and Hashing Offer Types

`static func != (Product.SubscriptionOffer.OfferType,
Product.SubscriptionOffer.OfferType) -> Bool`

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

### Comparing and Hashing Offer Types

`static func != (Product.SubscriptionOffer.OfferType,
Product.SubscriptionOffer.OfferType) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`func hash(into: inout Hasher)`

Hashes the essential components of this value by feeding them into the given
hasher.

Type Property

# introductory

An introductory offer for a subscription.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let introductory: Product.SubscriptionOffer.OfferType

## Discussion

For more information about introductory offers, see Set an introductory offer
for an auto-renewable subscription.

## See Also

### Getting the Offer Types

`static let promotional: Product.SubscriptionOffer.OfferType`

A promotional offer.

Type Property

# promotional

A promotional offer.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let promotional: Product.SubscriptionOffer.OfferType

## Discussion

For more information about promotional offers, see Set up promotional offers
for auto-renewable subscriptions.

## See Also

### Getting the Offer Types

`static let introductory: Product.SubscriptionOffer.OfferType`

An introductory offer for a subscription.

Instance Property

# localizedDescription

iOS 15.4+  iPadOS 15.4+  macOS 12.3+  Mac Catalyst 15.4+  tvOS 15.4+  watchOS
8.5+  visionOS 1.0+  Xcode 13.3+

    
    
    var localizedDescription: String { get }

Initializer

# init(rawValue:)

A raw value representing a subscription offer type.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    init(rawValue: String)

##  Parameters

`rawValue`

    

A string representing the offer type.

## Relationships

### From Protocol

  * `RawRepresentable`

## See Also

### Creating an Offer Type

`typealias Product.SubscriptionOffer.OfferType.RawValue`

`let rawValue: String`

A string representing the raw value of the subscription offer type.

Type Alias

# Product.SubscriptionOffer.OfferType.RawValue

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    typealias Product.SubscriptionOffer.OfferType.RawValue = String

## See Also

### Creating an Offer Type

`init(rawValue: String)`

A raw value representing a subscription offer type.

`let rawValue: String`

A string representing the raw value of the subscription offer type.

Instance Property

# rawValue

A string representing the raw value of the subscription offer type.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let rawValue: String

## Relationships

### From Protocol

  * `RawRepresentable`

## See Also

### Creating an Offer Type

`init(rawValue: String)`

A raw value representing a subscription offer type.

`typealias Product.SubscriptionOffer.OfferType.RawValue`

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func != (lhs: Product.SubscriptionOffer.OfferType, rhs: Product.SubscriptionOffer.OfferType) -> Bool

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

### Comparing and Hashing Offer Types

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

### Comparing and Hashing Offer Types

`static func != (Product.SubscriptionOffer.OfferType,
Product.SubscriptionOffer.OfferType) -> Bool`

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

### Comparing and Hashing Offer Types

`static func != (Product.SubscriptionOffer.OfferType,
Product.SubscriptionOffer.OfferType) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`func hash(into: inout Hasher)`

Hashes the essential components of this value by feeding them into the given
hasher.

Type Property

# introductory

An introductory offer for a subscription.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let introductory: Product.SubscriptionOffer.OfferType

## Discussion

For more information about introductory offers, see Set an introductory offer
for an auto-renewable subscription.

## See Also

### Getting the Offer Types

`static let promotional: Product.SubscriptionOffer.OfferType`

A promotional offer.

Type Property

# promotional

A promotional offer.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let promotional: Product.SubscriptionOffer.OfferType

## Discussion

For more information about promotional offers, see Set up promotional offers
for auto-renewable subscriptions.

## See Also

### Getting the Offer Types

`static let introductory: Product.SubscriptionOffer.OfferType`

An introductory offer for a subscription.

Instance Property

# localizedDescription

iOS 15.4+  iPadOS 15.4+  macOS 12.3+  Mac Catalyst 15.4+  tvOS 15.4+  watchOS
8.5+  visionOS 1.0+  Xcode 13.3+

    
    
    var localizedDescription: String { get }

Initializer

# init(rawValue:)

A raw value representing a subscription offer type.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    init(rawValue: String)

##  Parameters

`rawValue`

    

A string representing the offer type.

## Relationships

### From Protocol

  * `RawRepresentable`

## See Also

### Creating an Offer Type

`typealias Product.SubscriptionOffer.OfferType.RawValue`

`let rawValue: String`

A string representing the raw value of the subscription offer type.

Type Alias

# Product.SubscriptionOffer.OfferType.RawValue

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    typealias Product.SubscriptionOffer.OfferType.RawValue = String

## See Also

### Creating an Offer Type

`init(rawValue: String)`

A raw value representing a subscription offer type.

`let rawValue: String`

A string representing the raw value of the subscription offer type.

Instance Property

# rawValue

A string representing the raw value of the subscription offer type.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let rawValue: String

## Relationships

### From Protocol

  * `RawRepresentable`

## See Also

### Creating an Offer Type

`init(rawValue: String)`

A raw value representing a subscription offer type.

`typealias Product.SubscriptionOffer.OfferType.RawValue`

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func != (lhs: Product.SubscriptionOffer.OfferType, rhs: Product.SubscriptionOffer.OfferType) -> Bool

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

### Comparing and Hashing Offer Types

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

### Comparing and Hashing Offer Types

`static func != (Product.SubscriptionOffer.OfferType,
Product.SubscriptionOffer.OfferType) -> Bool`

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

### Comparing and Hashing Offer Types

`static func != (Product.SubscriptionOffer.OfferType,
Product.SubscriptionOffer.OfferType) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`func hash(into: inout Hasher)`

Hashes the essential components of this value by feeding them into the given
hasher.

