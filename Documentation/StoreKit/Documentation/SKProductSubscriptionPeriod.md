Instance Property

# numberOfUnits

The number of units per subscription period.

iOS 11.2+  iPadOS 11.2+  macOS 10.13.2+  Mac Catalyst 13.1+  tvOS 11.2+
watchOS 6.2+  visionOS 1.0+

    
    
    var numberOfUnits: Int { get }

## Discussion

A subscription period duration is calculated by multiplying the number of
units by the `unit`.

For example, if the number of units is `3`, and the unit is
`SKProduct.PeriodUnit.month`, the subscription period is 3 months.

## See Also

### Getting Subscription Period Details

`var unit: SKProduct.PeriodUnit`

The increment of time that a subscription period is specified in.

`enum SKProduct.PeriodUnit`

Values representing the duration of an interval, from a day up to a year.

Instance Property

# unit

The increment of time that a subscription period is specified in.

iOS 11.2+  iPadOS 11.2+  macOS 10.13.2+  Mac Catalyst 13.1+  tvOS 11.2+
watchOS 6.2+  visionOS 1.0+

    
    
    var unit: SKProduct.PeriodUnit { get }

## Discussion

The units used to specify a subscription period include day, week, month, and
year, as defined in `SKProduct.PeriodUnit`.

To calculate the duration of one subscription period, multiply the `unit` by
the number of units (`numberOfUnits`).

## See Also

### Getting Subscription Period Details

`var numberOfUnits: Int`

The number of units per subscription period.

`enum SKProduct.PeriodUnit`

Values representing the duration of an interval, from a day up to a year.

