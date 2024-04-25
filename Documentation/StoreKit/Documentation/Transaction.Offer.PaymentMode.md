Type Property

# freeTrial

A payment mode of a product discount that indicates a free trial.

iOS 17.2+  iPadOS 17.2+  macOS 14.2+  Mac Catalyst 17.2+  tvOS 17.2+  watchOS
10.2+  visionOS 1.1+  Xcode 15.1+

    
    
    static let freeTrial: Transaction.Offer.PaymentMode

## Discussion

With a Free trial payment mode, customers pay nothing during the discount
period.

## See Also

### Getting payment modes

`static let payAsYouGo: Transaction.Offer.PaymentMode`

A payment mode of a product discount that’s billed over a single or multiple
billing periods.

`static let payUpFront: Transaction.Offer.PaymentMode`

A payment mode of a product discount that’s paid up front.

Type Property

# payAsYouGo

A payment mode of a product discount that’s billed over a single or multiple
billing periods.

iOS 17.2+  iPadOS 17.2+  macOS 14.2+  Mac Catalyst 17.2+  tvOS 17.2+  watchOS
10.2+  visionOS 1.1+  Xcode 15.1+

    
    
    static let payAsYouGo: Transaction.Offer.PaymentMode

## Discussion

With a Pay As You Go payment mode, subscribers pay a discounted price for each
billing period for the duration of the discount.

## See Also

### Getting payment modes

`static let freeTrial: Transaction.Offer.PaymentMode`

A payment mode of a product discount that indicates a free trial.

`static let payUpFront: Transaction.Offer.PaymentMode`

A payment mode of a product discount that’s paid up front.

Type Property

# payUpFront

A payment mode of a product discount that’s paid up front.

iOS 17.2+  iPadOS 17.2+  macOS 14.2+  Mac Catalyst 17.2+  tvOS 17.2+  watchOS
10.2+  visionOS 1.1+  Xcode 15.1+

    
    
    static let payUpFront: Transaction.Offer.PaymentMode

## Discussion

With a Pay Up Front payment mode, subscribers pay a one-time discounted price
for a specific duration.

## See Also

### Getting payment modes

`static let freeTrial: Transaction.Offer.PaymentMode`

A payment mode of a product discount that indicates a free trial.

`static let payAsYouGo: Transaction.Offer.PaymentMode`

A payment mode of a product discount that’s billed over a single or multiple
billing periods.

Type Alias

# Transaction.Offer.PaymentMode.RawValue

A type that represents the subscription offer payment mode of a transaction.

iOS 17.2+  iPadOS 17.2+  macOS 14.2+  Mac Catalyst 17.2+  tvOS 17.2+  watchOS
10.2+  visionOS 1.1+  Xcode 15.1+

    
    
    typealias Transaction.Offer.PaymentMode.RawValue = String

Initializer

# init(rawValue:)

Creates a payment mode.

iOS 17.2+  iPadOS 17.2+  macOS 14.2+  Mac Catalyst 17.2+  tvOS 17.2+  watchOS
10.2+  visionOS 1.1+  Xcode 15.1+

    
    
    init(rawValue: String)

## Relationships

### From Protocol

  * `RawRepresentable`

## See Also

### Initializing payment modes

`let rawValue: String`

A string that represents a payment mode.

Instance Property

# rawValue

A string that represents a payment mode.

iOS 17.2+  iPadOS 17.2+  macOS 14.2+  Mac Catalyst 17.2+  tvOS 17.2+  watchOS
10.2+  visionOS 1.1+  Xcode 15.1+

    
    
    let rawValue: String

## Relationships

### From Protocol

  * `RawRepresentable`

## See Also

### Initializing payment modes

`init(rawValue: String)`

Creates a payment mode.

Instance Property

# hashValue

The hash value.

iOS 17.2+  iPadOS 17.2+  macOS 14.2+  Mac Catalyst 17.2+  tvOS 17.2+  watchOS
10.2+  visionOS 1.1+  Xcode 15.1+

    
    
    var hashValue: Int { get }

## See Also

### Comparing payment modes

`func hash(into: inout Hasher)`

Hashes the essential components of this value by feeding them into the given
hasher.

`static func != (Transaction.Offer.PaymentMode, Transaction.Offer.PaymentMode)
-> Bool`

Returns a Boolean value indicating whether two values are not equal.

Instance Method

# hash(into:)

Hashes the essential components of this value by feeding them into the given
hasher.

iOS 17.2+  iPadOS 17.2+  macOS 14.2+  Mac Catalyst 17.2+  tvOS 17.2+  watchOS
10.2+  visionOS 1.1+  Xcode 15.1+

    
    
    func hash(into hasher: inout Hasher)

## See Also

### Comparing payment modes

`var hashValue: Int`

The hash value.

`static func != (Transaction.Offer.PaymentMode, Transaction.Offer.PaymentMode)
-> Bool`

Returns a Boolean value indicating whether two values are not equal.

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 17.2+  iPadOS 17.2+  macOS 14.2+  Mac Catalyst 17.2+  tvOS 17.2+  watchOS
10.2+  visionOS 1.1+  Xcode 15.1+

    
    
    static func != (lhs: Transaction.Offer.PaymentMode, rhs: Transaction.Offer.PaymentMode) -> Bool

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

### Comparing payment modes

`var hashValue: Int`

The hash value.

`func hash(into: inout Hasher)`

Hashes the essential components of this value by feeding them into the given
hasher.

