Instance Property

# id

A string that identifies the subscription offer that applies to the
transaction.

iOS 17.2+  iPadOS 17.2+  macOS 14.2+  Mac Catalyst 17.2+  tvOS 17.2+  watchOS
10.2+  visionOS 1.1+  Xcode 15.1+

    
    
    let id: String?

## Discussion

This value is `nil` if the subscription offer is an `introductory` offer.

If the offer type is `promotional`, this value contains the promotional offer
identifier you set up in App Store Connect. For more information about
promotional offers, see Set up promotional offers for auto-renewable
subscriptions.

If the offer type is `code`, this value contains the reference name of the
offer code you set up in App Store Connect. For more information about offer
codes, see Set up offer codes.

## See Also

### Getting offer details

`let type: Transaction.OfferType`

The type of subscription offer that applies to the transaction.

`struct Transaction.OfferType`

The types of offers for auto-renewable subscriptions.

`struct Transaction.Offer.PaymentMode`

The payment modes for subscription offers that apply to a transaction.

Instance Property

# type

The type of subscription offer that applies to the transaction.

iOS 17.2+  iPadOS 17.2+  macOS 14.2+  Mac Catalyst 17.2+  tvOS 17.2+  watchOS
10.2+  visionOS 1.1+  Xcode 15.1+

    
    
    let type: Transaction.OfferType

## Discussion

The offer types are `introductory`, `promotional`, and `code`.

For more information about introductory offers, see Set an introductory offer
for an auto-renewable subscription.

For more information about promotional offers, see Set up promotional offers
for auto-renewable subscriptions.

For more information about offer codes, see Set up offer codes.

## See Also

### Getting offer details

`let id: String?`

A string that identifies the subscription offer that applies to the
transaction.

`struct Transaction.OfferType`

The types of offers for auto-renewable subscriptions.

`struct Transaction.Offer.PaymentMode`

The payment modes for subscription offers that apply to a transaction.

Operator

# ==(_:_:)

Returns a Boolean value that indicates whether two values are equal.

iOS 17.2+  iPadOS 17.2+  macOS 14.2+  Mac Catalyst 17.2+  tvOS 17.2+  watchOS
10.2+  visionOS 1.1+  Xcode 15.1+

    
    
    static func == (a: Transaction.Offer, b: Transaction.Offer) -> Bool

## See Also

### Comparing offers

`static func != (Transaction.Offer, Transaction.Offer) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`func hash(into: inout Hasher)`

Hashes the essential components of this value by feeding them into the given
hasher.

`var hashValue: Int`

The hash value.

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 17.2+  iPadOS 17.2+  macOS 14.2+  Mac Catalyst 17.2+  tvOS 17.2+  watchOS
10.2+  visionOS 1.1+  Xcode 15.1+

    
    
    static func != (lhs: Transaction.Offer, rhs: Transaction.Offer) -> Bool

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

### Comparing offers

`static func == (Transaction.Offer, Transaction.Offer) -> Bool`

Returns a Boolean value that indicates whether two values are equal.

`func hash(into: inout Hasher)`

Hashes the essential components of this value by feeding them into the given
hasher.

`var hashValue: Int`

The hash value.

Instance Method

# hash(into:)

Hashes the essential components of this value by feeding them into the given
hasher.

iOS 17.2+  iPadOS 17.2+  macOS 14.2+  Mac Catalyst 17.2+  tvOS 17.2+  watchOS
10.2+  visionOS 1.1+  Xcode 15.1+

    
    
    func hash(into hasher: inout Hasher)

## Relationships

### From Protocol

  * `Hashable`

## See Also

### Comparing offers

`static func == (Transaction.Offer, Transaction.Offer) -> Bool`

Returns a Boolean value that indicates whether two values are equal.

`static func != (Transaction.Offer, Transaction.Offer) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`var hashValue: Int`

The hash value.

Instance Property

# hashValue

The hash value.

iOS 17.2+  iPadOS 17.2+  macOS 14.2+  Mac Catalyst 17.2+  tvOS 17.2+  watchOS
10.2+  visionOS 1.1+  Xcode 15.1+

    
    
    var hashValue: Int { get }

## Relationships

### From Protocol

  * `Hashable`

## See Also

### Comparing offers

`static func == (Transaction.Offer, Transaction.Offer) -> Bool`

Returns a Boolean value that indicates whether two values are equal.

`static func != (Transaction.Offer, Transaction.Offer) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`func hash(into: inout Hasher)`

Hashes the essential components of this value by feeding them into the given
hasher.

Instance Property

# paymentMode

iOS 17.2+  iPadOS 17.2+  macOS 14.2+  Mac Catalyst 17.2+  tvOS 17.2+  watchOS
10.2+  visionOS 1.1+  Xcode 15.1+

    
    
    let paymentMode: Transaction.Offer.PaymentMode?

