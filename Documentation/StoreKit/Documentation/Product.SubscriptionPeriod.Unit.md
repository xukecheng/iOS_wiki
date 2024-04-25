Enumeration Case

# Product.SubscriptionPeriod.Unit.day

A subscription period unit of a day.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    case day

## See Also

### Getting the subscription period units

`case month`

A subscription period unit of a month.

`case week`

A subscription period unit of a week.

`case year`

A subscription period unit of a year.

Enumeration Case

# Product.SubscriptionPeriod.Unit.month

A subscription period unit of a month.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    case month

## See Also

### Getting the subscription period units

`case day`

A subscription period unit of a day.

`case week`

A subscription period unit of a week.

`case year`

A subscription period unit of a year.

Enumeration Case

# Product.SubscriptionPeriod.Unit.week

A subscription period unit of a week.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    case week

## See Also

### Getting the subscription period units

`case day`

A subscription period unit of a day.

`case month`

A subscription period unit of a month.

`case year`

A subscription period unit of a year.

Enumeration Case

# Product.SubscriptionPeriod.Unit.year

A subscription period unit of a year.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    case year

## See Also

### Getting the subscription period units

`case day`

A subscription period unit of a day.

`case month`

A subscription period unit of a month.

`case week`

A subscription period unit of a week.

Instance Property

# localizedDescription

The localized text that describes the subscription period unit.

iOS 15.4+  iPadOS 15.4+  macOS 12.3+  Mac Catalyst 15.4+  tvOS 15.4+  watchOS
8.5+  visionOS 1.0+  Xcode 13.3+

    
    
    var localizedDescription: String { get }

## See Also

### Getting localized and debug descriptions

`var debugDescription: String`

A string that contains the name of the subscription period unit, suitable for
debugging.

Instance Property

# debugDescription

A string that contains the name of the subscription period unit, suitable for
debugging.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var debugDescription: String { get }

## Relationships

### From Protocol

  * `CustomDebugStringConvertible`

## See Also

### Getting localized and debug descriptions

`var localizedDescription: String`

The localized text that describes the subscription period unit.

Generic Instance Method

# formatted(_:)

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    func formatted<S>(_ format: S) -> S.FormatOutput where S : FormatStyle, S.FormatInput == Product.SubscriptionPeriod.Unit

## See Also

### Getting the formatted description

`struct Product.SubscriptionPeriod.Unit.FormatStyle`

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func != (lhs: Product.SubscriptionPeriod.Unit, rhs: Product.SubscriptionPeriod.Unit) -> Bool

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

### Comparing and hashing units

`static func == (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

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

    
    
    static func == (a: Product.SubscriptionPeriod.Unit, b: Product.SubscriptionPeriod.Unit) -> Bool

## See Also

### Comparing and hashing units

`static func != (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

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

### Comparing and hashing units

`static func != (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

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

### Comparing and hashing units

`static func != (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether two values are equal.

`func hash(into: inout Hasher)`

Hashes the essential components of this value by feeding them into the given
hasher.

Enumeration Case

# Product.SubscriptionPeriod.Unit.day

A subscription period unit of a day.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    case day

## See Also

### Getting the subscription period units

`case month`

A subscription period unit of a month.

`case week`

A subscription period unit of a week.

`case year`

A subscription period unit of a year.

Enumeration Case

# Product.SubscriptionPeriod.Unit.month

A subscription period unit of a month.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    case month

## See Also

### Getting the subscription period units

`case day`

A subscription period unit of a day.

`case week`

A subscription period unit of a week.

`case year`

A subscription period unit of a year.

Enumeration Case

# Product.SubscriptionPeriod.Unit.week

A subscription period unit of a week.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    case week

## See Also

### Getting the subscription period units

`case day`

A subscription period unit of a day.

`case month`

A subscription period unit of a month.

`case year`

A subscription period unit of a year.

Enumeration Case

# Product.SubscriptionPeriod.Unit.year

A subscription period unit of a year.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    case year

## See Also

### Getting the subscription period units

`case day`

A subscription period unit of a day.

`case month`

A subscription period unit of a month.

`case week`

A subscription period unit of a week.

Instance Property

# localizedDescription

The localized text that describes the subscription period unit.

iOS 15.4+  iPadOS 15.4+  macOS 12.3+  Mac Catalyst 15.4+  tvOS 15.4+  watchOS
8.5+  visionOS 1.0+  Xcode 13.3+

    
    
    var localizedDescription: String { get }

## See Also

### Getting localized and debug descriptions

`var debugDescription: String`

A string that contains the name of the subscription period unit, suitable for
debugging.

Instance Property

# debugDescription

A string that contains the name of the subscription period unit, suitable for
debugging.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var debugDescription: String { get }

## Relationships

### From Protocol

  * `CustomDebugStringConvertible`

## See Also

### Getting localized and debug descriptions

`var localizedDescription: String`

The localized text that describes the subscription period unit.

Generic Instance Method

# formatted(_:)

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    func formatted<S>(_ format: S) -> S.FormatOutput where S : FormatStyle, S.FormatInput == Product.SubscriptionPeriod.Unit

## See Also

### Getting the formatted description

`struct Product.SubscriptionPeriod.Unit.FormatStyle`

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func != (lhs: Product.SubscriptionPeriod.Unit, rhs: Product.SubscriptionPeriod.Unit) -> Bool

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

### Comparing and hashing units

`static func == (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

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

    
    
    static func == (a: Product.SubscriptionPeriod.Unit, b: Product.SubscriptionPeriod.Unit) -> Bool

## See Also

### Comparing and hashing units

`static func != (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

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

### Comparing and hashing units

`static func != (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

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

### Comparing and hashing units

`static func != (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether two values are equal.

`func hash(into: inout Hasher)`

Hashes the essential components of this value by feeding them into the given
hasher.

Enumeration Case

# Product.SubscriptionPeriod.Unit.day

A subscription period unit of a day.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    case day

## See Also

### Getting the subscription period units

`case month`

A subscription period unit of a month.

`case week`

A subscription period unit of a week.

`case year`

A subscription period unit of a year.

Enumeration Case

# Product.SubscriptionPeriod.Unit.month

A subscription period unit of a month.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    case month

## See Also

### Getting the subscription period units

`case day`

A subscription period unit of a day.

`case week`

A subscription period unit of a week.

`case year`

A subscription period unit of a year.

Enumeration Case

# Product.SubscriptionPeriod.Unit.week

A subscription period unit of a week.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    case week

## See Also

### Getting the subscription period units

`case day`

A subscription period unit of a day.

`case month`

A subscription period unit of a month.

`case year`

A subscription period unit of a year.

Enumeration Case

# Product.SubscriptionPeriod.Unit.year

A subscription period unit of a year.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    case year

## See Also

### Getting the subscription period units

`case day`

A subscription period unit of a day.

`case month`

A subscription period unit of a month.

`case week`

A subscription period unit of a week.

Instance Property

# localizedDescription

The localized text that describes the subscription period unit.

iOS 15.4+  iPadOS 15.4+  macOS 12.3+  Mac Catalyst 15.4+  tvOS 15.4+  watchOS
8.5+  visionOS 1.0+  Xcode 13.3+

    
    
    var localizedDescription: String { get }

## See Also

### Getting localized and debug descriptions

`var debugDescription: String`

A string that contains the name of the subscription period unit, suitable for
debugging.

Instance Property

# debugDescription

A string that contains the name of the subscription period unit, suitable for
debugging.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var debugDescription: String { get }

## Relationships

### From Protocol

  * `CustomDebugStringConvertible`

## See Also

### Getting localized and debug descriptions

`var localizedDescription: String`

The localized text that describes the subscription period unit.

Generic Instance Method

# formatted(_:)

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    func formatted<S>(_ format: S) -> S.FormatOutput where S : FormatStyle, S.FormatInput == Product.SubscriptionPeriod.Unit

## See Also

### Getting the formatted description

`struct Product.SubscriptionPeriod.Unit.FormatStyle`

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func != (lhs: Product.SubscriptionPeriod.Unit, rhs: Product.SubscriptionPeriod.Unit) -> Bool

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

### Comparing and hashing units

`static func == (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

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

    
    
    static func == (a: Product.SubscriptionPeriod.Unit, b: Product.SubscriptionPeriod.Unit) -> Bool

## See Also

### Comparing and hashing units

`static func != (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

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

### Comparing and hashing units

`static func != (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

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

### Comparing and hashing units

`static func != (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether two values are equal.

`func hash(into: inout Hasher)`

Hashes the essential components of this value by feeding them into the given
hasher.

