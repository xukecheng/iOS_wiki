Instance Property

# displayPrice

The localized string representation of the discounted price of the
subscription offer.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let displayPrice: String

## See Also

### Getting price information

`let price: Decimal`

The decimal representation of the discounted price of the subscription offer.

`let paymentMode: Product.SubscriptionOffer.PaymentMode`

The offer's payment mode.

`struct Product.SubscriptionOffer.PaymentMode`

The payment modes for subscription offers.

Instance Property

# price

The decimal representation of the discounted price of the subscription offer.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let price: Decimal

## See Also

### Getting price information

`let displayPrice: String`

The localized string representation of the discounted price of the
subscription offer.

`let paymentMode: Product.SubscriptionOffer.PaymentMode`

The offer's payment mode.

`struct Product.SubscriptionOffer.PaymentMode`

The payment modes for subscription offers.

Instance Property

# paymentMode

The offer's payment mode.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let paymentMode: Product.SubscriptionOffer.PaymentMode

## See Also

### Getting price information

`let displayPrice: String`

The localized string representation of the discounted price of the
subscription offer.

`let price: Decimal`

The decimal representation of the discounted price of the subscription offer.

`struct Product.SubscriptionOffer.PaymentMode`

The payment modes for subscription offers.

Instance Property

# period

The subscription period for the subscription offer.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let period: Product.SubscriptionPeriod

## See Also

### Getting the subscription duration

`let periodCount: Int`

The number of periods that the subscription offer renews for.

Instance Property

# periodCount

The number of periods that the subscription offer renews for.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let periodCount: Int

## Discussion

If the payment mode is `payAsYouGo`, the period count represents the number of
periods the subscription renews at the discounted `price`.

The period count is 1 for offers with payment modes `freeTrial` and
`payUpFront`.

## See Also

### Getting the subscription duration

`let period: Product.SubscriptionPeriod`

The subscription period for the subscription offer.

Instance Property

# type

The type of subscription offer, either introductory or promotional.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let type: Product.SubscriptionOffer.OfferType

## See Also

### Getting the subscription offer type

`struct Product.SubscriptionOffer.OfferType`

The types of subscription offers.

Instance Property

# id

The promotional offer identifier.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let id: String?

## Discussion

This value is `nil` if the subscription offer is an `introductory` offer.

Pass `id` to `promotionalOffer(offerID:keyID:nonce:signature:timestamp:)` to
apply this promotion to a purchase, in `purchase(options:)`.

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func != (lhs: Product.SubscriptionOffer, rhs: Product.SubscriptionOffer) -> Bool

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

### Comparing and hashing subscription offers

`static func == (Product.SubscriptionOffer, Product.SubscriptionOffer) ->
Bool`

Returns a Boolean value indicating whether two values are equal.

`func hash(into: inout Hasher)`

Hashes the essential components of this value by feeding them into the given
hasher.

`var hashValue: Int`

The hash value.

Operator

# ==(_:_:)

Returns a Boolean value indicating whether two values are equal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func == (a: Product.SubscriptionOffer, b: Product.SubscriptionOffer) -> Bool

## See Also

### Comparing and hashing subscription offers

`static func != (Product.SubscriptionOffer, Product.SubscriptionOffer) ->
Bool`

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

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    func hash(into hasher: inout Hasher)

##  Parameters

`hasher`

    

The hasher to use when combining the components of this instance.

## Relationships

### From Protocol

  * `Hashable`

## See Also

### Comparing and hashing subscription offers

`static func != (Product.SubscriptionOffer, Product.SubscriptionOffer) ->
Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (Product.SubscriptionOffer, Product.SubscriptionOffer) ->
Bool`

Returns a Boolean value indicating whether two values are equal.

`var hashValue: Int`

The hash value.

Instance Property

# hashValue

The hash value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var hashValue: Int { get }

## Relationships

### From Protocol

  * `Hashable`

## See Also

### Comparing and hashing subscription offers

`static func != (Product.SubscriptionOffer, Product.SubscriptionOffer) ->
Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (Product.SubscriptionOffer, Product.SubscriptionOffer) ->
Bool`

Returns a Boolean value indicating whether two values are equal.

`func hash(into: inout Hasher)`

Hashes the essential components of this value by feeding them into the given
hasher.

Instance Property

# displayPrice

The localized string representation of the discounted price of the
subscription offer.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let displayPrice: String

## See Also

### Getting price information

`let price: Decimal`

The decimal representation of the discounted price of the subscription offer.

`let paymentMode: Product.SubscriptionOffer.PaymentMode`

The offer's payment mode.

`struct Product.SubscriptionOffer.PaymentMode`

The payment modes for subscription offers.

Instance Property

# price

The decimal representation of the discounted price of the subscription offer.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let price: Decimal

## See Also

### Getting price information

`let displayPrice: String`

The localized string representation of the discounted price of the
subscription offer.

`let paymentMode: Product.SubscriptionOffer.PaymentMode`

The offer's payment mode.

`struct Product.SubscriptionOffer.PaymentMode`

The payment modes for subscription offers.

Instance Property

# paymentMode

The offer's payment mode.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let paymentMode: Product.SubscriptionOffer.PaymentMode

## See Also

### Getting price information

`let displayPrice: String`

The localized string representation of the discounted price of the
subscription offer.

`let price: Decimal`

The decimal representation of the discounted price of the subscription offer.

`struct Product.SubscriptionOffer.PaymentMode`

The payment modes for subscription offers.

Instance Property

# period

The subscription period for the subscription offer.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let period: Product.SubscriptionPeriod

## See Also

### Getting the subscription duration

`let periodCount: Int`

The number of periods that the subscription offer renews for.

Instance Property

# periodCount

The number of periods that the subscription offer renews for.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let periodCount: Int

## Discussion

If the payment mode is `payAsYouGo`, the period count represents the number of
periods the subscription renews at the discounted `price`.

The period count is 1 for offers with payment modes `freeTrial` and
`payUpFront`.

## See Also

### Getting the subscription duration

`let period: Product.SubscriptionPeriod`

The subscription period for the subscription offer.

Instance Property

# type

The type of subscription offer, either introductory or promotional.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let type: Product.SubscriptionOffer.OfferType

## See Also

### Getting the subscription offer type

`struct Product.SubscriptionOffer.OfferType`

The types of subscription offers.

Instance Property

# id

The promotional offer identifier.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let id: String?

## Discussion

This value is `nil` if the subscription offer is an `introductory` offer.

Pass `id` to `promotionalOffer(offerID:keyID:nonce:signature:timestamp:)` to
apply this promotion to a purchase, in `purchase(options:)`.

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func != (lhs: Product.SubscriptionOffer, rhs: Product.SubscriptionOffer) -> Bool

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

### Comparing and hashing subscription offers

`static func == (Product.SubscriptionOffer, Product.SubscriptionOffer) ->
Bool`

Returns a Boolean value indicating whether two values are equal.

`func hash(into: inout Hasher)`

Hashes the essential components of this value by feeding them into the given
hasher.

`var hashValue: Int`

The hash value.

Operator

# ==(_:_:)

Returns a Boolean value indicating whether two values are equal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func == (a: Product.SubscriptionOffer, b: Product.SubscriptionOffer) -> Bool

## See Also

### Comparing and hashing subscription offers

`static func != (Product.SubscriptionOffer, Product.SubscriptionOffer) ->
Bool`

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

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    func hash(into hasher: inout Hasher)

##  Parameters

`hasher`

    

The hasher to use when combining the components of this instance.

## Relationships

### From Protocol

  * `Hashable`

## See Also

### Comparing and hashing subscription offers

`static func != (Product.SubscriptionOffer, Product.SubscriptionOffer) ->
Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (Product.SubscriptionOffer, Product.SubscriptionOffer) ->
Bool`

Returns a Boolean value indicating whether two values are equal.

`var hashValue: Int`

The hash value.

Instance Property

# hashValue

The hash value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var hashValue: Int { get }

## Relationships

### From Protocol

  * `Hashable`

## See Also

### Comparing and hashing subscription offers

`static func != (Product.SubscriptionOffer, Product.SubscriptionOffer) ->
Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (Product.SubscriptionOffer, Product.SubscriptionOffer) ->
Bool`

Returns a Boolean value indicating whether two values are equal.

`func hash(into: inout Hasher)`

Hashes the essential components of this value by feeding them into the given
hasher.

Instance Property

# displayPrice

The localized string representation of the discounted price of the
subscription offer.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let displayPrice: String

## See Also

### Getting price information

`let price: Decimal`

The decimal representation of the discounted price of the subscription offer.

`let paymentMode: Product.SubscriptionOffer.PaymentMode`

The offer's payment mode.

`struct Product.SubscriptionOffer.PaymentMode`

The payment modes for subscription offers.

Instance Property

# price

The decimal representation of the discounted price of the subscription offer.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let price: Decimal

## See Also

### Getting price information

`let displayPrice: String`

The localized string representation of the discounted price of the
subscription offer.

`let paymentMode: Product.SubscriptionOffer.PaymentMode`

The offer's payment mode.

`struct Product.SubscriptionOffer.PaymentMode`

The payment modes for subscription offers.

Instance Property

# paymentMode

The offer's payment mode.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let paymentMode: Product.SubscriptionOffer.PaymentMode

## See Also

### Getting price information

`let displayPrice: String`

The localized string representation of the discounted price of the
subscription offer.

`let price: Decimal`

The decimal representation of the discounted price of the subscription offer.

`struct Product.SubscriptionOffer.PaymentMode`

The payment modes for subscription offers.

Instance Property

# period

The subscription period for the subscription offer.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let period: Product.SubscriptionPeriod

## See Also

### Getting the subscription duration

`let periodCount: Int`

The number of periods that the subscription offer renews for.

Instance Property

# periodCount

The number of periods that the subscription offer renews for.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let periodCount: Int

## Discussion

If the payment mode is `payAsYouGo`, the period count represents the number of
periods the subscription renews at the discounted `price`.

The period count is 1 for offers with payment modes `freeTrial` and
`payUpFront`.

## See Also

### Getting the subscription duration

`let period: Product.SubscriptionPeriod`

The subscription period for the subscription offer.

Instance Property

# type

The type of subscription offer, either introductory or promotional.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let type: Product.SubscriptionOffer.OfferType

## See Also

### Getting the subscription offer type

`struct Product.SubscriptionOffer.OfferType`

The types of subscription offers.

Instance Property

# id

The promotional offer identifier.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let id: String?

## Discussion

This value is `nil` if the subscription offer is an `introductory` offer.

Pass `id` to `promotionalOffer(offerID:keyID:nonce:signature:timestamp:)` to
apply this promotion to a purchase, in `purchase(options:)`.

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func != (lhs: Product.SubscriptionOffer, rhs: Product.SubscriptionOffer) -> Bool

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

### Comparing and hashing subscription offers

`static func == (Product.SubscriptionOffer, Product.SubscriptionOffer) ->
Bool`

Returns a Boolean value indicating whether two values are equal.

`func hash(into: inout Hasher)`

Hashes the essential components of this value by feeding them into the given
hasher.

`var hashValue: Int`

The hash value.

Operator

# ==(_:_:)

Returns a Boolean value indicating whether two values are equal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func == (a: Product.SubscriptionOffer, b: Product.SubscriptionOffer) -> Bool

## See Also

### Comparing and hashing subscription offers

`static func != (Product.SubscriptionOffer, Product.SubscriptionOffer) ->
Bool`

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

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    func hash(into hasher: inout Hasher)

##  Parameters

`hasher`

    

The hasher to use when combining the components of this instance.

## Relationships

### From Protocol

  * `Hashable`

## See Also

### Comparing and hashing subscription offers

`static func != (Product.SubscriptionOffer, Product.SubscriptionOffer) ->
Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (Product.SubscriptionOffer, Product.SubscriptionOffer) ->
Bool`

Returns a Boolean value indicating whether two values are equal.

`var hashValue: Int`

The hash value.

Instance Property

# hashValue

The hash value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var hashValue: Int { get }

## Relationships

### From Protocol

  * `Hashable`

## See Also

### Comparing and hashing subscription offers

`static func != (Product.SubscriptionOffer, Product.SubscriptionOffer) ->
Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (Product.SubscriptionOffer, Product.SubscriptionOffer) ->
Bool`

Returns a Boolean value indicating whether two values are equal.

`func hash(into: inout Hasher)`

Hashes the essential components of this value by feeding them into the given
hasher.

