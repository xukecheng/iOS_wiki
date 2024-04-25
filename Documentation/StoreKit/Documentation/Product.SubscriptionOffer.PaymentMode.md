Type Property

# freeTrial

A payment mode of a product discount that indicates a free trial offer.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let freeTrial: Product.SubscriptionOffer.PaymentMode

## Discussion

With a Free trial payment mode, customers pay nothing during the discount
period.

## See Also

### Getting the payment modes

`static let payAsYouGo: Product.SubscriptionOffer.PaymentMode`

A payment mode of a product discount that indicates the discount applies over
a single billing period or multiple billing periods.

`static let payUpFront: Product.SubscriptionOffer.PaymentMode`

A payment mode of a product discount that indicates the system applies the
discount up front.

Type Property

# payAsYouGo

A payment mode of a product discount that indicates the discount applies over
a single billing period or multiple billing periods.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let payAsYouGo: Product.SubscriptionOffer.PaymentMode

## Discussion

With a Pay As You Go payment mode, subscribers pay a discounted price for each
billing period for the duration of the discount.

## See Also

### Getting the payment modes

`static let freeTrial: Product.SubscriptionOffer.PaymentMode`

A payment mode of a product discount that indicates a free trial offer.

`static let payUpFront: Product.SubscriptionOffer.PaymentMode`

A payment mode of a product discount that indicates the system applies the
discount up front.

Type Property

# payUpFront

A payment mode of a product discount that indicates the system applies the
discount up front.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let payUpFront: Product.SubscriptionOffer.PaymentMode

## Discussion

With a Pay Up Front payment mode, subscribers pay a one-time discounted price
for a specific duration.

## See Also

### Getting the payment modes

`static let freeTrial: Product.SubscriptionOffer.PaymentMode`

A payment mode of a product discount that indicates a free trial offer.

`static let payAsYouGo: Product.SubscriptionOffer.PaymentMode`

A payment mode of a product discount that indicates the discount applies over
a single billing period or multiple billing periods.

Instance Property

# localizedDescription

The localized text that describes the payment mode.

iOS 15.4+  iPadOS 15.4+  macOS 12.3+  Mac Catalyst 15.4+  tvOS 15.4+  watchOS
8.5+  visionOS 1.0+  Xcode 13.3+

    
    
    var localizedDescription: String { get }

Instance Property

# rawValue

The raw string value that represents a payment mode for a subscription offer.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let rawValue: String

## Discussion

Use the raw value to help parse the `jsonRepresentation` property of
`Product`. If a product is a subscription with an offer, the JSON contains a
string representation of the payment mode, which is its raw value. You can
compare the JSON data directly to the payment mode’s `rawValue`.

You can also use the `rawValue` to create a payment mode instance by calling
`init(rawValue:)`.

## Relationships

### From Protocol

  * `RawRepresentable`

## See Also

### Accessing the raw value

`typealias Product.SubscriptionOffer.PaymentMode.RawValue`

A type that represents the raw value of a payment mode for a subscription
offer.

Type Alias

# Product.SubscriptionOffer.PaymentMode.RawValue

A type that represents the raw value of a payment mode for a subscription
offer.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    typealias Product.SubscriptionOffer.PaymentMode.RawValue = String

## See Also

### Accessing the raw value

`let rawValue: String`

The raw string value that represents a payment mode for a subscription offer.

Initializer

# init(rawValue:)

Creates a subscription offer payment mode instance from a raw value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    init(rawValue: String)

##  Parameters

`rawValue`

    

A string that represents a payment mode for a subscription offer.

## Discussion

Typically, you get a payment mode from the `paymentMode` property in
subscription offer information, and you don’t need to instantiate it yourself.

However, if you use the `jsonRepresentation` property of `Product`, you can
use raw values and the initializer to help parse the JSON. If the product is a
subscription with an offer, the JSON contains the string representation of the
payment mode, which is its raw value. Call `init(rawValue:)` to create your
own instance from that raw value. Alternatively, you can compare the JSON data
directly to the payment mode’s `rawValue`.

## Relationships

### From Protocol

  * `RawRepresentable`

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func != (lhs: Product.SubscriptionOffer.PaymentMode, rhs: Product.SubscriptionOffer.PaymentMode) -> Bool

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

### Comparing and hashing payment modes

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

### Comparing and hashing payment modes

`static func != (Product.SubscriptionOffer.PaymentMode,
Product.SubscriptionOffer.PaymentMode) -> Bool`

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

### Comparing and hashing payment modes

`static func != (Product.SubscriptionOffer.PaymentMode,
Product.SubscriptionOffer.PaymentMode) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`func hash(into: inout Hasher)`

Hashes the essential components of the value by feeding them into the given
hasher.

Type Property

# freeTrial

A payment mode of a product discount that indicates a free trial offer.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let freeTrial: Product.SubscriptionOffer.PaymentMode

## Discussion

With a Free trial payment mode, customers pay nothing during the discount
period.

## See Also

### Getting the payment modes

`static let payAsYouGo: Product.SubscriptionOffer.PaymentMode`

A payment mode of a product discount that indicates the discount applies over
a single billing period or multiple billing periods.

`static let payUpFront: Product.SubscriptionOffer.PaymentMode`

A payment mode of a product discount that indicates the system applies the
discount up front.

Type Property

# payAsYouGo

A payment mode of a product discount that indicates the discount applies over
a single billing period or multiple billing periods.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let payAsYouGo: Product.SubscriptionOffer.PaymentMode

## Discussion

With a Pay As You Go payment mode, subscribers pay a discounted price for each
billing period for the duration of the discount.

## See Also

### Getting the payment modes

`static let freeTrial: Product.SubscriptionOffer.PaymentMode`

A payment mode of a product discount that indicates a free trial offer.

`static let payUpFront: Product.SubscriptionOffer.PaymentMode`

A payment mode of a product discount that indicates the system applies the
discount up front.

Type Property

# payUpFront

A payment mode of a product discount that indicates the system applies the
discount up front.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let payUpFront: Product.SubscriptionOffer.PaymentMode

## Discussion

With a Pay Up Front payment mode, subscribers pay a one-time discounted price
for a specific duration.

## See Also

### Getting the payment modes

`static let freeTrial: Product.SubscriptionOffer.PaymentMode`

A payment mode of a product discount that indicates a free trial offer.

`static let payAsYouGo: Product.SubscriptionOffer.PaymentMode`

A payment mode of a product discount that indicates the discount applies over
a single billing period or multiple billing periods.

Instance Property

# localizedDescription

The localized text that describes the payment mode.

iOS 15.4+  iPadOS 15.4+  macOS 12.3+  Mac Catalyst 15.4+  tvOS 15.4+  watchOS
8.5+  visionOS 1.0+  Xcode 13.3+

    
    
    var localizedDescription: String { get }

Instance Property

# rawValue

The raw string value that represents a payment mode for a subscription offer.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let rawValue: String

## Discussion

Use the raw value to help parse the `jsonRepresentation` property of
`Product`. If a product is a subscription with an offer, the JSON contains a
string representation of the payment mode, which is its raw value. You can
compare the JSON data directly to the payment mode’s `rawValue`.

You can also use the `rawValue` to create a payment mode instance by calling
`init(rawValue:)`.

## Relationships

### From Protocol

  * `RawRepresentable`

## See Also

### Accessing the raw value

`typealias Product.SubscriptionOffer.PaymentMode.RawValue`

A type that represents the raw value of a payment mode for a subscription
offer.

Type Alias

# Product.SubscriptionOffer.PaymentMode.RawValue

A type that represents the raw value of a payment mode for a subscription
offer.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    typealias Product.SubscriptionOffer.PaymentMode.RawValue = String

## See Also

### Accessing the raw value

`let rawValue: String`

The raw string value that represents a payment mode for a subscription offer.

Initializer

# init(rawValue:)

Creates a subscription offer payment mode instance from a raw value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    init(rawValue: String)

##  Parameters

`rawValue`

    

A string that represents a payment mode for a subscription offer.

## Discussion

Typically, you get a payment mode from the `paymentMode` property in
subscription offer information, and you don’t need to instantiate it yourself.

However, if you use the `jsonRepresentation` property of `Product`, you can
use raw values and the initializer to help parse the JSON. If the product is a
subscription with an offer, the JSON contains the string representation of the
payment mode, which is its raw value. Call `init(rawValue:)` to create your
own instance from that raw value. Alternatively, you can compare the JSON data
directly to the payment mode’s `rawValue`.

## Relationships

### From Protocol

  * `RawRepresentable`

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func != (lhs: Product.SubscriptionOffer.PaymentMode, rhs: Product.SubscriptionOffer.PaymentMode) -> Bool

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

### Comparing and hashing payment modes

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

### Comparing and hashing payment modes

`static func != (Product.SubscriptionOffer.PaymentMode,
Product.SubscriptionOffer.PaymentMode) -> Bool`

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

### Comparing and hashing payment modes

`static func != (Product.SubscriptionOffer.PaymentMode,
Product.SubscriptionOffer.PaymentMode) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`func hash(into: inout Hasher)`

Hashes the essential components of the value by feeding them into the given
hasher.

Type Property

# freeTrial

A payment mode of a product discount that indicates a free trial offer.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let freeTrial: Product.SubscriptionOffer.PaymentMode

## Discussion

With a Free trial payment mode, customers pay nothing during the discount
period.

## See Also

### Getting the payment modes

`static let payAsYouGo: Product.SubscriptionOffer.PaymentMode`

A payment mode of a product discount that indicates the discount applies over
a single billing period or multiple billing periods.

`static let payUpFront: Product.SubscriptionOffer.PaymentMode`

A payment mode of a product discount that indicates the system applies the
discount up front.

Type Property

# payAsYouGo

A payment mode of a product discount that indicates the discount applies over
a single billing period or multiple billing periods.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let payAsYouGo: Product.SubscriptionOffer.PaymentMode

## Discussion

With a Pay As You Go payment mode, subscribers pay a discounted price for each
billing period for the duration of the discount.

## See Also

### Getting the payment modes

`static let freeTrial: Product.SubscriptionOffer.PaymentMode`

A payment mode of a product discount that indicates a free trial offer.

`static let payUpFront: Product.SubscriptionOffer.PaymentMode`

A payment mode of a product discount that indicates the system applies the
discount up front.

Type Property

# payUpFront

A payment mode of a product discount that indicates the system applies the
discount up front.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let payUpFront: Product.SubscriptionOffer.PaymentMode

## Discussion

With a Pay Up Front payment mode, subscribers pay a one-time discounted price
for a specific duration.

## See Also

### Getting the payment modes

`static let freeTrial: Product.SubscriptionOffer.PaymentMode`

A payment mode of a product discount that indicates a free trial offer.

`static let payAsYouGo: Product.SubscriptionOffer.PaymentMode`

A payment mode of a product discount that indicates the discount applies over
a single billing period or multiple billing periods.

Instance Property

# localizedDescription

The localized text that describes the payment mode.

iOS 15.4+  iPadOS 15.4+  macOS 12.3+  Mac Catalyst 15.4+  tvOS 15.4+  watchOS
8.5+  visionOS 1.0+  Xcode 13.3+

    
    
    var localizedDescription: String { get }

Instance Property

# rawValue

The raw string value that represents a payment mode for a subscription offer.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let rawValue: String

## Discussion

Use the raw value to help parse the `jsonRepresentation` property of
`Product`. If a product is a subscription with an offer, the JSON contains a
string representation of the payment mode, which is its raw value. You can
compare the JSON data directly to the payment mode’s `rawValue`.

You can also use the `rawValue` to create a payment mode instance by calling
`init(rawValue:)`.

## Relationships

### From Protocol

  * `RawRepresentable`

## See Also

### Accessing the raw value

`typealias Product.SubscriptionOffer.PaymentMode.RawValue`

A type that represents the raw value of a payment mode for a subscription
offer.

Type Alias

# Product.SubscriptionOffer.PaymentMode.RawValue

A type that represents the raw value of a payment mode for a subscription
offer.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    typealias Product.SubscriptionOffer.PaymentMode.RawValue = String

## See Also

### Accessing the raw value

`let rawValue: String`

The raw string value that represents a payment mode for a subscription offer.

Initializer

# init(rawValue:)

Creates a subscription offer payment mode instance from a raw value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    init(rawValue: String)

##  Parameters

`rawValue`

    

A string that represents a payment mode for a subscription offer.

## Discussion

Typically, you get a payment mode from the `paymentMode` property in
subscription offer information, and you don’t need to instantiate it yourself.

However, if you use the `jsonRepresentation` property of `Product`, you can
use raw values and the initializer to help parse the JSON. If the product is a
subscription with an offer, the JSON contains the string representation of the
payment mode, which is its raw value. Call `init(rawValue:)` to create your
own instance from that raw value. Alternatively, you can compare the JSON data
directly to the payment mode’s `rawValue`.

## Relationships

### From Protocol

  * `RawRepresentable`

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func != (lhs: Product.SubscriptionOffer.PaymentMode, rhs: Product.SubscriptionOffer.PaymentMode) -> Bool

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

### Comparing and hashing payment modes

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

### Comparing and hashing payment modes

`static func != (Product.SubscriptionOffer.PaymentMode,
Product.SubscriptionOffer.PaymentMode) -> Bool`

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

### Comparing and hashing payment modes

`static func != (Product.SubscriptionOffer.PaymentMode,
Product.SubscriptionOffer.PaymentMode) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`func hash(into: inout Hasher)`

Hashes the essential components of the value by feeding them into the given
hasher.

