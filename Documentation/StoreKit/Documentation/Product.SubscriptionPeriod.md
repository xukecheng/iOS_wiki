Instance Property

# value

The number of period units.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let value: Int

## Discussion

Use the value and the unit together to determine the subscription period. For
example, if the `unit` is `Product.SubscriptionPeriod.Unit.month`, and the
`value` is `3`, the subscription period is three months.

## See Also

### Getting the subscription period

`let unit: Product.SubscriptionPeriod.Unit`

The increment of time for the subscription period.

`enum Product.SubscriptionPeriod.Unit`

Units of time that describe subscription periods.

Instance Property

# unit

The increment of time for the subscription period.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let unit: Product.SubscriptionPeriod.Unit

## Discussion

The units used to specify a subscription period include day, week, month, and
year, as defined in `Product.SubscriptionPeriod.Unit`.

To calculate the duration of one subscription period, multiply the `unit` by
the number of units (`value`).

## See Also

### Getting the subscription period

`let value: Int`

The number of period units.

`enum Product.SubscriptionPeriod.Unit`

Units of time that describe subscription periods.

Instance Method

# dateRange(referenceDate:)

The calculated date range of a subscription period, starting at the reference
date.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 16.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    @backDeployed(before: iOS 16.0, macOS 13.0, tvOS 16.0, watchOS 9.0, macCatalyst 16.0)
    func dateRange(referenceDate: Date = .now) -> Range<Date>

##  Parameters

`referenceDate`

    

A date you provide that indicates the lower bound of the returned date range.
The default value is `now`.

## Return Value

The subscription period represented by two dates that are the lower bound and
upper bound of the subscription period.

## Discussion

The date range calculates a single subscription period starting from the date
you provide in `referenceDate`.

For example, if a subscription period is one month, and the `referenceDate` is
February 1, the date range contains February 1 and March 1. If the
`referenceDate` is Feb 15, the date range contains February 15 and March 15.

Use the `dateRange(referenceDate:)` with a `Date.ComponentsFormatStyle` to get
a human-readable string representation of the subscription period.

Get the format style (`Date.ComponentsFormatStyle`) corresponding to product’s
storefront using the `subscriptionPeriodFormatStyle`.

Generic Instance Method

# formatted(_:referenceDate:)

Formats the subscription period using a format style that takes a date range
as an input.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 16.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    @backDeployed(before: iOS 16.0, macOS 13.0, tvOS 16.0, watchOS 9.0, macCatalyst 16.0)
    func formatted<S>(
        _ format: S,
        referenceDate: Date = .now
    ) -> S.FormatOutput where S : FormatStyle, S.FormatInput == Range<Date>

##  Parameters

`format`

    

A format style that has a date range input. The format style for a product is
`subscriptionPeriodFormatStyle`.

`referenceDate`

    

The lower bound date for a date range representing the subscription period.
The default value is `now`.

## Discussion

## See Also

### Formatting the subscription period

`func formatted<S>(S, referenceDate: Date) -> S.FormatOutput`

Formats the subscription period using a format style that takes a duration as
an input.

Generic Instance Method

# formatted(_:referenceDate:)

Formats the subscription period using a format style that takes a duration as
an input.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    func formatted<S>(
        _ format: S,
        referenceDate: Date = .now
    ) -> S.FormatOutput where S : FormatStyle, S.FormatInput == Duration

##  Parameters

`format`

    

A format style that has a duration as an input.

`referenceDate`

    

The starting date of the subscription period. The default value is `now`.

## See Also

### Formatting the subscription period

`@backDeployed(before: iOS 16.0, macOS 13.0, tvOS 16.0, watchOS 9.0,
macCatalyst 16.0) func formatted<S>(S, referenceDate: Date) -> S.FormatOutput`

Formats the subscription period using a format style that takes a date range
as an input.

Instance Property

# debugDescription

A string representation of the subscription period, suitable for debugging.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var debugDescription: String { get }

## Relationships

### From Protocol

  * `CustomDebugStringConvertible`

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func != (lhs: Product.SubscriptionPeriod, rhs: Product.SubscriptionPeriod) -> Bool

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

### Comparing and hashing subscription periods

`static func == (Product.SubscriptionPeriod, Product.SubscriptionPeriod) ->
Bool`

Returns a Boolean value that indicates whether two values are equal.

`func hash(into: inout Hasher)`

Hashes the essential components of the value by feeding them into the given
hasher.

`var hashValue: Int`

The hash value.

Operator

# ==(_:_:)

Returns a Boolean value that indicates whether two values are equal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func == (a: Product.SubscriptionPeriod, b: Product.SubscriptionPeriod) -> Bool

## See Also

### Comparing and hashing subscription periods

`static func != (Product.SubscriptionPeriod, Product.SubscriptionPeriod) ->
Bool`

Returns a Boolean value indicating whether two values are not equal.

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

## Relationships

### From Protocol

  * `Hashable`

## See Also

### Comparing and hashing subscription periods

`static func != (Product.SubscriptionPeriod, Product.SubscriptionPeriod) ->
Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (Product.SubscriptionPeriod, Product.SubscriptionPeriod) ->
Bool`

Returns a Boolean value that indicates whether two values are equal.

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

### Comparing and hashing subscription periods

`static func != (Product.SubscriptionPeriod, Product.SubscriptionPeriod) ->
Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (Product.SubscriptionPeriod, Product.SubscriptionPeriod) ->
Bool`

Returns a Boolean value that indicates whether two values are equal.

`func hash(into: inout Hasher)`

Hashes the essential components of the value by feeding them into the given
hasher.

Instance Property

# value

The number of period units.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let value: Int

## Discussion

Use the value and the unit together to determine the subscription period. For
example, if the `unit` is `Product.SubscriptionPeriod.Unit.month`, and the
`value` is `3`, the subscription period is three months.

## See Also

### Getting the subscription period

`let unit: Product.SubscriptionPeriod.Unit`

The increment of time for the subscription period.

`enum Product.SubscriptionPeriod.Unit`

Units of time that describe subscription periods.

Instance Property

# unit

The increment of time for the subscription period.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let unit: Product.SubscriptionPeriod.Unit

## Discussion

The units used to specify a subscription period include day, week, month, and
year, as defined in `Product.SubscriptionPeriod.Unit`.

To calculate the duration of one subscription period, multiply the `unit` by
the number of units (`value`).

## See Also

### Getting the subscription period

`let value: Int`

The number of period units.

`enum Product.SubscriptionPeriod.Unit`

Units of time that describe subscription periods.

Instance Method

# dateRange(referenceDate:)

The calculated date range of a subscription period, starting at the reference
date.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 16.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    @backDeployed(before: iOS 16.0, macOS 13.0, tvOS 16.0, watchOS 9.0, macCatalyst 16.0)
    func dateRange(referenceDate: Date = .now) -> Range<Date>

##  Parameters

`referenceDate`

    

A date you provide that indicates the lower bound of the returned date range.
The default value is `now`.

## Return Value

The subscription period represented by two dates that are the lower bound and
upper bound of the subscription period.

## Discussion

The date range calculates a single subscription period starting from the date
you provide in `referenceDate`.

For example, if a subscription period is one month, and the `referenceDate` is
February 1, the date range contains February 1 and March 1. If the
`referenceDate` is Feb 15, the date range contains February 15 and March 15.

Use the `dateRange(referenceDate:)` with a `Date.ComponentsFormatStyle` to get
a human-readable string representation of the subscription period.

Get the format style (`Date.ComponentsFormatStyle`) corresponding to product’s
storefront using the `subscriptionPeriodFormatStyle`.

Generic Instance Method

# formatted(_:referenceDate:)

Formats the subscription period using a format style that takes a date range
as an input.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 16.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    @backDeployed(before: iOS 16.0, macOS 13.0, tvOS 16.0, watchOS 9.0, macCatalyst 16.0)
    func formatted<S>(
        _ format: S,
        referenceDate: Date = .now
    ) -> S.FormatOutput where S : FormatStyle, S.FormatInput == Range<Date>

##  Parameters

`format`

    

A format style that has a date range input. The format style for a product is
`subscriptionPeriodFormatStyle`.

`referenceDate`

    

The lower bound date for a date range representing the subscription period.
The default value is `now`.

## Discussion

    
    
    // Get a human-readable representation of a subscription period.
    subscriptionPeriod.formatted(product.subscriptionPeriodFormatStyle, referenceDate: /* some date */)
    
    
    

## See Also

### Formatting the subscription period

`func formatted<S>(S, referenceDate: Date) -> S.FormatOutput`

Formats the subscription period using a format style that takes a duration as
an input.

Generic Instance Method

# formatted(_:referenceDate:)

Formats the subscription period using a format style that takes a duration as
an input.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    func formatted<S>(
        _ format: S,
        referenceDate: Date = .now
    ) -> S.FormatOutput where S : FormatStyle, S.FormatInput == Duration

##  Parameters

`format`

    

A format style that has a duration as an input.

`referenceDate`

    

The starting date of the subscription period. The default value is `now`.

## See Also

### Formatting the subscription period

`@backDeployed(before: iOS 16.0, macOS 13.0, tvOS 16.0, watchOS 9.0,
macCatalyst 16.0) func formatted<S>(S, referenceDate: Date) -> S.FormatOutput`

Formats the subscription period using a format style that takes a date range
as an input.

Instance Property

# debugDescription

A string representation of the subscription period, suitable for debugging.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var debugDescription: String { get }

## Relationships

### From Protocol

  * `CustomDebugStringConvertible`

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func != (lhs: Product.SubscriptionPeriod, rhs: Product.SubscriptionPeriod) -> Bool

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

### Comparing and hashing subscription periods

`static func == (Product.SubscriptionPeriod, Product.SubscriptionPeriod) ->
Bool`

Returns a Boolean value that indicates whether two values are equal.

`func hash(into: inout Hasher)`

Hashes the essential components of the value by feeding them into the given
hasher.

`var hashValue: Int`

The hash value.

Operator

# ==(_:_:)

Returns a Boolean value that indicates whether two values are equal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func == (a: Product.SubscriptionPeriod, b: Product.SubscriptionPeriod) -> Bool

## See Also

### Comparing and hashing subscription periods

`static func != (Product.SubscriptionPeriod, Product.SubscriptionPeriod) ->
Bool`

Returns a Boolean value indicating whether two values are not equal.

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

## Relationships

### From Protocol

  * `Hashable`

## See Also

### Comparing and hashing subscription periods

`static func != (Product.SubscriptionPeriod, Product.SubscriptionPeriod) ->
Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (Product.SubscriptionPeriod, Product.SubscriptionPeriod) ->
Bool`

Returns a Boolean value that indicates whether two values are equal.

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

### Comparing and hashing subscription periods

`static func != (Product.SubscriptionPeriod, Product.SubscriptionPeriod) ->
Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (Product.SubscriptionPeriod, Product.SubscriptionPeriod) ->
Bool`

Returns a Boolean value that indicates whether two values are equal.

`func hash(into: inout Hasher)`

Hashes the essential components of the value by feeding them into the given
hasher.

Instance Property

# value

The number of period units.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let value: Int

## Discussion

Use the value and the unit together to determine the subscription period. For
example, if the `unit` is `Product.SubscriptionPeriod.Unit.month`, and the
`value` is `3`, the subscription period is three months.

## See Also

### Getting the subscription period

`let unit: Product.SubscriptionPeriod.Unit`

The increment of time for the subscription period.

`enum Product.SubscriptionPeriod.Unit`

Units of time that describe subscription periods.

Instance Property

# unit

The increment of time for the subscription period.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    let unit: Product.SubscriptionPeriod.Unit

## Discussion

The units used to specify a subscription period include day, week, month, and
year, as defined in `Product.SubscriptionPeriod.Unit`.

To calculate the duration of one subscription period, multiply the `unit` by
the number of units (`value`).

## See Also

### Getting the subscription period

`let value: Int`

The number of period units.

`enum Product.SubscriptionPeriod.Unit`

Units of time that describe subscription periods.

Instance Method

# dateRange(referenceDate:)

The calculated date range of a subscription period, starting at the reference
date.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 16.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    @backDeployed(before: iOS 16.0, macOS 13.0, tvOS 16.0, watchOS 9.0, macCatalyst 16.0)
    func dateRange(referenceDate: Date = .now) -> Range<Date>

##  Parameters

`referenceDate`

    

A date you provide that indicates the lower bound of the returned date range.
The default value is `now`.

## Return Value

The subscription period represented by two dates that are the lower bound and
upper bound of the subscription period.

## Discussion

The date range calculates a single subscription period starting from the date
you provide in `referenceDate`.

For example, if a subscription period is one month, and the `referenceDate` is
February 1, the date range contains February 1 and March 1. If the
`referenceDate` is Feb 15, the date range contains February 15 and March 15.

Use the `dateRange(referenceDate:)` with a `Date.ComponentsFormatStyle` to get
a human-readable string representation of the subscription period.

Get the format style (`Date.ComponentsFormatStyle`) corresponding to product’s
storefront using the `subscriptionPeriodFormatStyle`.

Generic Instance Method

# formatted(_:referenceDate:)

Formats the subscription period using a format style that takes a date range
as an input.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 16.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    @backDeployed(before: iOS 16.0, macOS 13.0, tvOS 16.0, watchOS 9.0, macCatalyst 16.0)
    func formatted<S>(
        _ format: S,
        referenceDate: Date = .now
    ) -> S.FormatOutput where S : FormatStyle, S.FormatInput == Range<Date>

##  Parameters

`format`

    

A format style that has a date range input. The format style for a product is
`subscriptionPeriodFormatStyle`.

`referenceDate`

    

The lower bound date for a date range representing the subscription period.
The default value is `now`.

## Discussion

    
    
    // Get a human-readable representation of a subscription period.
    subscriptionPeriod.formatted(product.subscriptionPeriodFormatStyle, referenceDate: /* some date */)
    
    
    

## See Also

### Formatting the subscription period

`func formatted<S>(S, referenceDate: Date) -> S.FormatOutput`

Formats the subscription period using a format style that takes a duration as
an input.

Generic Instance Method

# formatted(_:referenceDate:)

Formats the subscription period using a format style that takes a duration as
an input.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    func formatted<S>(
        _ format: S,
        referenceDate: Date = .now
    ) -> S.FormatOutput where S : FormatStyle, S.FormatInput == Duration

##  Parameters

`format`

    

A format style that has a duration as an input.

`referenceDate`

    

The starting date of the subscription period. The default value is `now`.

## See Also

### Formatting the subscription period

`@backDeployed(before: iOS 16.0, macOS 13.0, tvOS 16.0, watchOS 9.0,
macCatalyst 16.0) func formatted<S>(S, referenceDate: Date) -> S.FormatOutput`

Formats the subscription period using a format style that takes a date range
as an input.

Instance Property

# debugDescription

A string representation of the subscription period, suitable for debugging.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var debugDescription: String { get }

## Relationships

### From Protocol

  * `CustomDebugStringConvertible`

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func != (lhs: Product.SubscriptionPeriod, rhs: Product.SubscriptionPeriod) -> Bool

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

### Comparing and hashing subscription periods

`static func == (Product.SubscriptionPeriod, Product.SubscriptionPeriod) ->
Bool`

Returns a Boolean value that indicates whether two values are equal.

`func hash(into: inout Hasher)`

Hashes the essential components of the value by feeding them into the given
hasher.

`var hashValue: Int`

The hash value.

Operator

# ==(_:_:)

Returns a Boolean value that indicates whether two values are equal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func == (a: Product.SubscriptionPeriod, b: Product.SubscriptionPeriod) -> Bool

## See Also

### Comparing and hashing subscription periods

`static func != (Product.SubscriptionPeriod, Product.SubscriptionPeriod) ->
Bool`

Returns a Boolean value indicating whether two values are not equal.

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

## Relationships

### From Protocol

  * `Hashable`

## See Also

### Comparing and hashing subscription periods

`static func != (Product.SubscriptionPeriod, Product.SubscriptionPeriod) ->
Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (Product.SubscriptionPeriod, Product.SubscriptionPeriod) ->
Bool`

Returns a Boolean value that indicates whether two values are equal.

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

### Comparing and hashing subscription periods

`static func != (Product.SubscriptionPeriod, Product.SubscriptionPeriod) ->
Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (Product.SubscriptionPeriod, Product.SubscriptionPeriod) ->
Bool`

Returns a Boolean value that indicates whether two values are equal.

`func hash(into: inout Hasher)`

Hashes the essential components of the value by feeding them into the given
hasher.

