Enumeration Case

# Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus.noIncreasePending

There’s no pending price increase for the auto-renewable subscription.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    case noIncreasePending

## Discussion

For more information about this value, see Managing Price Increases for Auto-
Renewable Subscriptions.

## See Also

### Getting Price Increase Status

`case agreed`

The auto-renewable subscription is subject to a price increase.

`case pending`

The customer hasn’t yet responded to an auto-renewable subscription price
increase that requires customer consent.

Enumeration Case

# Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus.agreed

The auto-renewable subscription is subject to a price increase.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    case agreed

## Discussion

There are two types of price increases for auto-renewable subscriptions: those
that require customer consent, and those that don’t require customer consent.
For a price increase that requires customer consent, this value indicates that
the customer consented to the price increase. For a price increase that
doesn’t require customer consent, this value indicates that the App Store
informed the customer of the price increase and the subscription is subject to
the price increase.

For more information about this value, see Managing Price Increases for Auto-
Renewable Subscriptions.

## See Also

### Getting Price Increase Status

`case noIncreasePending`

There’s no pending price increase for the auto-renewable subscription.

`case pending`

The customer hasn’t yet responded to an auto-renewable subscription price
increase that requires customer consent.

Enumeration Case

# Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus.pending

The customer hasn’t yet responded to an auto-renewable subscription price
increase that requires customer consent.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    case pending

## Discussion

For more information about this value, see Managing Price Increases for Auto-
Renewable Subscriptions.

## See Also

### Getting Price Increase Status

`case noIncreasePending`

There’s no pending price increase for the auto-renewable subscription.

`case agreed`

The auto-renewable subscription is subject to a price increase.

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func != (lhs: Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus, rhs: Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus) -> Bool

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

### Comparing and Hashing Status

`static func == (Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus,
Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus) -> Bool`

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

    
    
    static func == (a: Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus, b: Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus) -> Bool

## See Also

### Comparing and Hashing Status

`static func != (Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus,
Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus) -> Bool`

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

### Comparing and Hashing Status

`static func != (Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus,
Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus,
Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus) -> Bool`

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

### Comparing and Hashing Status

`static func != (Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus,
Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus,
Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus) -> Bool`

Returns a Boolean value indicating whether two values are equal.

`func hash(into: inout Hasher)`

Hashes the essential components of this value by feeding them into the given
hasher.

Instance Property

# localizedDescription

A string containing the localized description of the price increase status.

iOS 15.4+  iPadOS 15.4+  macOS 12.3+  Mac Catalyst 15.4+  tvOS 15.4+  watchOS
8.5+  visionOS 1.0+  Xcode 13.3+

    
    
    var localizedDescription: String { get }

Enumeration Case

# Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus.noIncreasePending

There’s no pending price increase for the auto-renewable subscription.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    case noIncreasePending

## Discussion

For more information about this value, see Managing Price Increases for Auto-
Renewable Subscriptions.

## See Also

### Getting Price Increase Status

`case agreed`

The auto-renewable subscription is subject to a price increase.

`case pending`

The customer hasn’t yet responded to an auto-renewable subscription price
increase that requires customer consent.

Enumeration Case

# Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus.agreed

The auto-renewable subscription is subject to a price increase.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    case agreed

## Discussion

There are two types of price increases for auto-renewable subscriptions: those
that require customer consent, and those that don’t require customer consent.
For a price increase that requires customer consent, this value indicates that
the customer consented to the price increase. For a price increase that
doesn’t require customer consent, this value indicates that the App Store
informed the customer of the price increase and the subscription is subject to
the price increase.

For more information about this value, see Managing Price Increases for Auto-
Renewable Subscriptions.

## See Also

### Getting Price Increase Status

`case noIncreasePending`

There’s no pending price increase for the auto-renewable subscription.

`case pending`

The customer hasn’t yet responded to an auto-renewable subscription price
increase that requires customer consent.

Enumeration Case

# Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus.pending

The customer hasn’t yet responded to an auto-renewable subscription price
increase that requires customer consent.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    case pending

## Discussion

For more information about this value, see Managing Price Increases for Auto-
Renewable Subscriptions.

## See Also

### Getting Price Increase Status

`case noIncreasePending`

There’s no pending price increase for the auto-renewable subscription.

`case agreed`

The auto-renewable subscription is subject to a price increase.

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func != (lhs: Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus, rhs: Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus) -> Bool

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

### Comparing and Hashing Status

`static func == (Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus,
Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus) -> Bool`

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

    
    
    static func == (a: Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus, b: Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus) -> Bool

## See Also

### Comparing and Hashing Status

`static func != (Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus,
Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus) -> Bool`

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

### Comparing and Hashing Status

`static func != (Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus,
Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus,
Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus) -> Bool`

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

### Comparing and Hashing Status

`static func != (Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus,
Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus,
Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus) -> Bool`

Returns a Boolean value indicating whether two values are equal.

`func hash(into: inout Hasher)`

Hashes the essential components of this value by feeding them into the given
hasher.

Instance Property

# localizedDescription

A string containing the localized description of the price increase status.

iOS 15.4+  iPadOS 15.4+  macOS 12.3+  Mac Catalyst 15.4+  tvOS 15.4+  watchOS
8.5+  visionOS 1.0+  Xcode 13.3+

    
    
    var localizedDescription: String { get }

Enumeration Case

# Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus.noIncreasePending

There’s no pending price increase for the auto-renewable subscription.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    case noIncreasePending

## Discussion

For more information about this value, see Managing Price Increases for Auto-
Renewable Subscriptions.

## See Also

### Getting Price Increase Status

`case agreed`

The auto-renewable subscription is subject to a price increase.

`case pending`

The customer hasn’t yet responded to an auto-renewable subscription price
increase that requires customer consent.

Enumeration Case

# Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus.agreed

The auto-renewable subscription is subject to a price increase.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    case agreed

## Discussion

There are two types of price increases for auto-renewable subscriptions: those
that require customer consent, and those that don’t require customer consent.
For a price increase that requires customer consent, this value indicates that
the customer consented to the price increase. For a price increase that
doesn’t require customer consent, this value indicates that the App Store
informed the customer of the price increase and the subscription is subject to
the price increase.

For more information about this value, see Managing Price Increases for Auto-
Renewable Subscriptions.

## See Also

### Getting Price Increase Status

`case noIncreasePending`

There’s no pending price increase for the auto-renewable subscription.

`case pending`

The customer hasn’t yet responded to an auto-renewable subscription price
increase that requires customer consent.

Enumeration Case

# Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus.pending

The customer hasn’t yet responded to an auto-renewable subscription price
increase that requires customer consent.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    case pending

## Discussion

For more information about this value, see Managing Price Increases for Auto-
Renewable Subscriptions.

## See Also

### Getting Price Increase Status

`case noIncreasePending`

There’s no pending price increase for the auto-renewable subscription.

`case agreed`

The auto-renewable subscription is subject to a price increase.

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func != (lhs: Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus, rhs: Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus) -> Bool

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

### Comparing and Hashing Status

`static func == (Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus,
Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus) -> Bool`

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

    
    
    static func == (a: Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus, b: Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus) -> Bool

## See Also

### Comparing and Hashing Status

`static func != (Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus,
Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus) -> Bool`

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

### Comparing and Hashing Status

`static func != (Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus,
Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus,
Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus) -> Bool`

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

### Comparing and Hashing Status

`static func != (Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus,
Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus,
Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus) -> Bool`

Returns a Boolean value indicating whether two values are equal.

`func hash(into: inout Hasher)`

Hashes the essential components of this value by feeding them into the given
hasher.

Instance Property

# localizedDescription

A string containing the localized description of the price increase status.

iOS 15.4+  iPadOS 15.4+  macOS 12.3+  Mac Catalyst 15.4+  tvOS 15.4+  watchOS
8.5+  visionOS 1.0+  Xcode 13.3+

    
    
    var localizedDescription: String { get }

Enumeration Case

# Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus.noIncreasePending

There’s no pending price increase for the auto-renewable subscription.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    case noIncreasePending

## Discussion

For more information about this value, see Managing Price Increases for Auto-
Renewable Subscriptions.

## See Also

### Getting Price Increase Status

`case agreed`

The auto-renewable subscription is subject to a price increase.

`case pending`

The customer hasn’t yet responded to an auto-renewable subscription price
increase that requires customer consent.

Enumeration Case

# Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus.agreed

The auto-renewable subscription is subject to a price increase.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    case agreed

## Discussion

There are two types of price increases for auto-renewable subscriptions: those
that require customer consent, and those that don’t require customer consent.
For a price increase that requires customer consent, this value indicates that
the customer consented to the price increase. For a price increase that
doesn’t require customer consent, this value indicates that the App Store
informed the customer of the price increase and the subscription is subject to
the price increase.

For more information about this value, see Managing Price Increases for Auto-
Renewable Subscriptions.

## See Also

### Getting Price Increase Status

`case noIncreasePending`

There’s no pending price increase for the auto-renewable subscription.

`case pending`

The customer hasn’t yet responded to an auto-renewable subscription price
increase that requires customer consent.

Enumeration Case

# Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus.pending

The customer hasn’t yet responded to an auto-renewable subscription price
increase that requires customer consent.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    case pending

## Discussion

For more information about this value, see Managing Price Increases for Auto-
Renewable Subscriptions.

## See Also

### Getting Price Increase Status

`case noIncreasePending`

There’s no pending price increase for the auto-renewable subscription.

`case agreed`

The auto-renewable subscription is subject to a price increase.

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func != (lhs: Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus, rhs: Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus) -> Bool

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

### Comparing and Hashing Status

`static func == (Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus,
Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus) -> Bool`

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

    
    
    static func == (a: Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus, b: Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus) -> Bool

## See Also

### Comparing and Hashing Status

`static func != (Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus,
Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus) -> Bool`

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

### Comparing and Hashing Status

`static func != (Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus,
Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus,
Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus) -> Bool`

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

### Comparing and Hashing Status

`static func != (Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus,
Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus,
Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus) -> Bool`

Returns a Boolean value indicating whether two values are equal.

`func hash(into: inout Hasher)`

Hashes the essential components of this value by feeding them into the given
hasher.

Instance Property

# localizedDescription

A string containing the localized description of the price increase status.

iOS 15.4+  iPadOS 15.4+  macOS 12.3+  Mac Catalyst 15.4+  tvOS 15.4+  watchOS
8.5+  visionOS 1.0+  Xcode 13.3+

    
    
    var localizedDescription: String { get }

