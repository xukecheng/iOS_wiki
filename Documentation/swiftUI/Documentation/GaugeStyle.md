Type Property

# automatic

The default gauge view style in the current context of the view being styled.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 7.0+
visionOS 1.0+

    
    
    static var automatic: DefaultGaugeStyle { get }

Available when `Self` is `DefaultGaugeStyle`.

Type Property

# circular

A gauge style that displays an open ring with a marker that appears at a point
along the ring to indicate the gauge’s current value.

watchOS 7.0+

    
    
    static var circular: CircularGaugeStyle { get }

Available when `Self` is `CircularGaugeStyle`.

## Discussion

Apply this style to a `Gauge` or to a view hierarchy that contains gauges
using the `gaugeStyle(_:)` modifier:

This style displays the gauge’s `currentValueLabel` value at the center of the
gauge. If you provide `minimumValueLabel` and `maximumValueLabel` parameters
when you create the gauge, they appear in the opening at the bottom of the
ring. Otherwise, the gauge places its label in that location.

## See Also

### Getting circular gauge styles

`static var accessoryCircular: AccessoryCircularGaugeStyle`

A gauge style that displays an open ring with a marker that appears at a point
along the ring to indicate the gauge’s current value.

Available when `Self` is `AccessoryCircularGaugeStyle`.

`static var accessoryCircularCapacity: AccessoryCircularCapacityGaugeStyle`

A gauge style that displays a closed ring that’s partially filled in to
indicate the gauge’s current value.

Available when `Self` is `AccessoryCircularCapacityGaugeStyle`.

Type Property

# accessoryCircular

A gauge style that displays an open ring with a marker that appears at a point
along the ring to indicate the gauge’s current value.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    static var accessoryCircular: AccessoryCircularGaugeStyle { get }

Available when `Self` is `AccessoryCircularGaugeStyle`.

## Discussion

Apply this style to a `Gauge` or to a view hierarchy that contains gauges
using the `gaugeStyle(_:)` modifier:

This style displays the gauge’s `currentValueLabel` value at the center of the
gauge. If you provide `minimumValueLabel` and `maximumValueLabel` parameters
when you create the gauge, they appear in the opening at the bottom of the
ring. Otherwise, the gauge places its label in that location.

## See Also

### Getting circular gauge styles

`static var circular: CircularGaugeStyle`

A gauge style that displays an open ring with a marker that appears at a point
along the ring to indicate the gauge’s current value.

Available when `Self` is `CircularGaugeStyle`.

`static var accessoryCircularCapacity: AccessoryCircularCapacityGaugeStyle`

A gauge style that displays a closed ring that’s partially filled in to
indicate the gauge’s current value.

Available when `Self` is `AccessoryCircularCapacityGaugeStyle`.

Type Property

# accessoryCircularCapacity

A gauge style that displays a closed ring that’s partially filled in to
indicate the gauge’s current value.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    static var accessoryCircularCapacity: AccessoryCircularCapacityGaugeStyle { get }

Available when `Self` is `AccessoryCircularCapacityGaugeStyle`.

## Discussion

Apply this style to a `Gauge` or to a view hierarchy that contains gauges
using the `gaugeStyle(_:)` modifier:

This style displays the gauge’s `currentValueLabel` value at the center of the
gauge.

## See Also

### Getting circular gauge styles

`static var circular: CircularGaugeStyle`

A gauge style that displays an open ring with a marker that appears at a point
along the ring to indicate the gauge’s current value.

Available when `Self` is `CircularGaugeStyle`.

`static var accessoryCircular: AccessoryCircularGaugeStyle`

A gauge style that displays an open ring with a marker that appears at a point
along the ring to indicate the gauge’s current value.

Available when `Self` is `AccessoryCircularGaugeStyle`.

Type Property

# linear

A gauge style that displays a bar with a marker that appears at a point along
the bar to indicate the gauge’s current value.

watchOS 7.0+

    
    
    static var linear: LinearGaugeStyle { get }

Available when `Self` is `LinearGaugeStyle`.

## Discussion

Apply this style to a `Gauge` or to a view hierarchy that contains gauges
using the `gaugeStyle(_:)` modifier:

If you provide `minimumValueLabel` and `maximumValueLabel` parameters when you
create the gauge, they appear on leading and trailing edges of the bar,
respectively. Otherwise, the gauge displays the `currentValueLabel` value on
the leading edge.

## See Also

### Getting linear gauge styles

`static var linearCapacity: LinearCapacityGaugeStyle`

A gauge style that displays a bar that fills from leading to trailing edges as
the gauge’s current value increases.

Available when `Self` is `LinearCapacityGaugeStyle`.

`static var accessoryLinear: AccessoryLinearGaugeStyle`

A gauge style that displays bar with a marker that appears at a point along
the bar to indicate the gauge’s current value.

Available when `Self` is `AccessoryLinearGaugeStyle`.

`static var accessoryLinearCapacity: AccessoryLinearCapacityGaugeStyle`

A gauge style that displays bar that fills from leading to trailing edges as
the gauge’s current value increases.

Available when `Self` is `AccessoryLinearCapacityGaugeStyle`.

Type Property

# linearCapacity

A gauge style that displays a bar that fills from leading to trailing edges as
the gauge’s current value increases.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    static var linearCapacity: LinearCapacityGaugeStyle { get }

Available when `Self` is `LinearCapacityGaugeStyle`.

## Discussion

Apply this style to a `Gauge` or to a view hierarchy that contains gauges
using the `gaugeStyle(_:)` modifier:

If you provide `minimumValueLabel` and `maximumValueLabel` parameters when you
create the gauge, they appear on leading and trailing edges of the bar,
respectively. The `label` appears above the gauge, and the `currentValueLabel`
appears below.

## See Also

### Getting linear gauge styles

`static var linear: LinearGaugeStyle`

A gauge style that displays a bar with a marker that appears at a point along
the bar to indicate the gauge’s current value.

Available when `Self` is `LinearGaugeStyle`.

`static var accessoryLinear: AccessoryLinearGaugeStyle`

A gauge style that displays bar with a marker that appears at a point along
the bar to indicate the gauge’s current value.

Available when `Self` is `AccessoryLinearGaugeStyle`.

`static var accessoryLinearCapacity: AccessoryLinearCapacityGaugeStyle`

A gauge style that displays bar that fills from leading to trailing edges as
the gauge’s current value increases.

Available when `Self` is `AccessoryLinearCapacityGaugeStyle`.

Type Property

# accessoryLinear

A gauge style that displays bar with a marker that appears at a point along
the bar to indicate the gauge’s current value.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    static var accessoryLinear: AccessoryLinearGaugeStyle { get }

Available when `Self` is `AccessoryLinearGaugeStyle`.

## Discussion

Apply this style to a `Gauge` or to a view hierarchy that contains gauges
using the `gaugeStyle(_:)` modifier:

If you provide `minimumValueLabel` and `maximumValueLabel` parameters when you
create the gauge, they appear on leading and trailing edges of the bar,
respectively. Otherwise, the gauge displays the `currentValueLabel` value on
the leading edge.

## See Also

### Getting linear gauge styles

`static var linear: LinearGaugeStyle`

A gauge style that displays a bar with a marker that appears at a point along
the bar to indicate the gauge’s current value.

Available when `Self` is `LinearGaugeStyle`.

`static var linearCapacity: LinearCapacityGaugeStyle`

A gauge style that displays a bar that fills from leading to trailing edges as
the gauge’s current value increases.

Available when `Self` is `LinearCapacityGaugeStyle`.

`static var accessoryLinearCapacity: AccessoryLinearCapacityGaugeStyle`

A gauge style that displays bar that fills from leading to trailing edges as
the gauge’s current value increases.

Available when `Self` is `AccessoryLinearCapacityGaugeStyle`.

Type Property

# accessoryLinearCapacity

A gauge style that displays bar that fills from leading to trailing edges as
the gauge’s current value increases.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    static var accessoryLinearCapacity: AccessoryLinearCapacityGaugeStyle { get }

Available when `Self` is `AccessoryLinearCapacityGaugeStyle`.

## Discussion

Apply this style to a `Gauge` or to a view hierarchy that contains gauges
using the `gaugeStyle(_:)` modifier:

If you provide `minimumValueLabel` and `maximumValueLabel` parameters when you
create the gauge, they appear on leading and trailing edges of the bar,
respectively. The `label` appears above the gauge, and the `currentValueLabel`
appears below.

## See Also

### Getting linear gauge styles

`static var linear: LinearGaugeStyle`

A gauge style that displays a bar with a marker that appears at a point along
the bar to indicate the gauge’s current value.

Available when `Self` is `LinearGaugeStyle`.

`static var linearCapacity: LinearCapacityGaugeStyle`

A gauge style that displays a bar that fills from leading to trailing edges as
the gauge’s current value increases.

Available when `Self` is `LinearCapacityGaugeStyle`.

`static var accessoryLinear: AccessoryLinearGaugeStyle`

A gauge style that displays bar with a marker that appears at a point along
the bar to indicate the gauge’s current value.

Available when `Self` is `AccessoryLinearGaugeStyle`.

Instance Method

# makeBody(configuration:)

Creates a view representing the body of a gauge.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 7.0+
visionOS 1.0+

    
    
    @ViewBuilder
    func makeBody(configuration: Self.Configuration) -> Self.Body

**Required**

##  Parameters

`configuration`

    

The properties to apply to the gauge instance.

## Discussion

The system calls this modifier on each instance of gauge within a view
hierarchy where this style is the current gauge style.

## See Also

### Creating custom gauge styles

`typealias Configuration`

The properties of a gauge instance.

`associatedtype Body : View`

A view representing the body of a gauge.

**Required**

Type Alias

# GaugeStyle.Configuration

The properties of a gauge instance.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 7.0+
visionOS 1.0+

    
    
    typealias Configuration = GaugeStyleConfiguration

## See Also

### Creating custom gauge styles

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Creates a view representing the body of a gauge.

**Required**

` associatedtype Body : View`

A view representing the body of a gauge.

**Required**

Associated Type

# Body

A view representing the body of a gauge.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 7.0+
visionOS 1.0+

    
    
    associatedtype Body : View

**Required**

## See Also

### Creating custom gauge styles

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Creates a view representing the body of a gauge.

**Required**

` typealias Configuration`

The properties of a gauge instance.

Structure

# DefaultGaugeStyle

The default gauge view style in the current context of the view being styled.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 7.0+
visionOS 1.0+

    
    
    struct DefaultGaugeStyle

## Overview

You can also use `automatic` to construct this style.

## Topics

### Creating the gauge style

`init()`

Creates a default gauge style.

## Relationships

### Conforms To

  * `GaugeStyle`

## See Also

### Supporting types

`struct CircularGaugeStyle`

A gauge style that displays an open ring with a marker that appears at a point
along the ring to indicate the gauge’s current value.

`struct AccessoryCircularGaugeStyle`

A gauge style that displays an open ring with a marker that appears at a point
along the ring to indicate the gauge’s current value.

`struct AccessoryCircularCapacityGaugeStyle`

A gauge style that displays a closed ring that’s partially filled in to
indicate the gauge’s current value.

`struct LinearGaugeStyle`

A gauge style that displays a bar with a marker that appears at a point along
the bar to indicate the gauge’s current value.

`struct LinearCapacityGaugeStyle`

A gauge style that displays bar that fills from leading to trailing edges as
the gauge’s current value increases.

`struct AccessoryLinearGaugeStyle`

A gauge style that displays bar with a marker that appears at a point along
the bar to indicate the gauge’s current value.

`struct AccessoryLinearCapacityGaugeStyle`

A gauge style that displays bar that fills from leading to trailing edges as
the gauge’s current value increases.

Structure

# CircularGaugeStyle

A gauge style that displays an open ring with a marker that appears at a point
along the ring to indicate the gauge’s current value.

watchOS 7.0+

    
    
    struct CircularGaugeStyle

## Overview

Use `circular` to construct this style.

## Topics

### Creating the gauge style

`init()`

Creates a circular gauge.

`init(tint: Color)`

Creates a circular gauge that draws with a specified color.

`init(tint: Gradient)`

Creates a circular gauge that draws with a specified gradient.

## Relationships

### Conforms To

  * `GaugeStyle`

## See Also

### Supporting types

`struct DefaultGaugeStyle`

The default gauge view style in the current context of the view being styled.

`struct AccessoryCircularGaugeStyle`

A gauge style that displays an open ring with a marker that appears at a point
along the ring to indicate the gauge’s current value.

`struct AccessoryCircularCapacityGaugeStyle`

A gauge style that displays a closed ring that’s partially filled in to
indicate the gauge’s current value.

`struct LinearGaugeStyle`

A gauge style that displays a bar with a marker that appears at a point along
the bar to indicate the gauge’s current value.

`struct LinearCapacityGaugeStyle`

A gauge style that displays bar that fills from leading to trailing edges as
the gauge’s current value increases.

`struct AccessoryLinearGaugeStyle`

A gauge style that displays bar with a marker that appears at a point along
the bar to indicate the gauge’s current value.

`struct AccessoryLinearCapacityGaugeStyle`

A gauge style that displays bar that fills from leading to trailing edges as
the gauge’s current value increases.

Structure

# AccessoryCircularGaugeStyle

A gauge style that displays an open ring with a marker that appears at a point
along the ring to indicate the gauge’s current value.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    struct AccessoryCircularGaugeStyle

## Overview

Use `accessoryCircular` to construct this style.

## Topics

### Creating the gauge style

`init()`

Creates an accessory circular gauge style.

## Relationships

### Conforms To

  * `GaugeStyle`

## See Also

### Supporting types

`struct DefaultGaugeStyle`

The default gauge view style in the current context of the view being styled.

`struct CircularGaugeStyle`

A gauge style that displays an open ring with a marker that appears at a point
along the ring to indicate the gauge’s current value.

`struct AccessoryCircularCapacityGaugeStyle`

A gauge style that displays a closed ring that’s partially filled in to
indicate the gauge’s current value.

`struct LinearGaugeStyle`

A gauge style that displays a bar with a marker that appears at a point along
the bar to indicate the gauge’s current value.

`struct LinearCapacityGaugeStyle`

A gauge style that displays bar that fills from leading to trailing edges as
the gauge’s current value increases.

`struct AccessoryLinearGaugeStyle`

A gauge style that displays bar with a marker that appears at a point along
the bar to indicate the gauge’s current value.

`struct AccessoryLinearCapacityGaugeStyle`

A gauge style that displays bar that fills from leading to trailing edges as
the gauge’s current value increases.

Structure

# AccessoryCircularCapacityGaugeStyle

A gauge style that displays a closed ring that’s partially filled in to
indicate the gauge’s current value.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    struct AccessoryCircularCapacityGaugeStyle

## Overview

Use `accessoryCircularCapacity` to construct this style.

## Topics

### Creating the gauge style

`init()`

Creates an accessory circular capacity gauge style.

## Relationships

### Conforms To

  * `GaugeStyle`

## See Also

### Supporting types

`struct DefaultGaugeStyle`

The default gauge view style in the current context of the view being styled.

`struct CircularGaugeStyle`

A gauge style that displays an open ring with a marker that appears at a point
along the ring to indicate the gauge’s current value.

`struct AccessoryCircularGaugeStyle`

A gauge style that displays an open ring with a marker that appears at a point
along the ring to indicate the gauge’s current value.

`struct LinearGaugeStyle`

A gauge style that displays a bar with a marker that appears at a point along
the bar to indicate the gauge’s current value.

`struct LinearCapacityGaugeStyle`

A gauge style that displays bar that fills from leading to trailing edges as
the gauge’s current value increases.

`struct AccessoryLinearGaugeStyle`

A gauge style that displays bar with a marker that appears at a point along
the bar to indicate the gauge’s current value.

`struct AccessoryLinearCapacityGaugeStyle`

A gauge style that displays bar that fills from leading to trailing edges as
the gauge’s current value increases.

Structure

# LinearGaugeStyle

A gauge style that displays a bar with a marker that appears at a point along
the bar to indicate the gauge’s current value.

watchOS 7.0+

    
    
    struct LinearGaugeStyle

## Overview

Use `linear` to construct this style.

## Topics

### Creating the gauge style

`init()`

Creates a linear gauge style.

### Deprecated initializers

`init(tint: Color)`

Creates a linear gauge style with a tint color.

Deprecated

`init(tint: Gradient)`

Creates a linear gauge style with a tint gradient.

Deprecated

## Relationships

### Conforms To

  * `GaugeStyle`

## See Also

### Supporting types

`struct DefaultGaugeStyle`

The default gauge view style in the current context of the view being styled.

`struct CircularGaugeStyle`

A gauge style that displays an open ring with a marker that appears at a point
along the ring to indicate the gauge’s current value.

`struct AccessoryCircularGaugeStyle`

A gauge style that displays an open ring with a marker that appears at a point
along the ring to indicate the gauge’s current value.

`struct AccessoryCircularCapacityGaugeStyle`

A gauge style that displays a closed ring that’s partially filled in to
indicate the gauge’s current value.

`struct LinearCapacityGaugeStyle`

A gauge style that displays bar that fills from leading to trailing edges as
the gauge’s current value increases.

`struct AccessoryLinearGaugeStyle`

A gauge style that displays bar with a marker that appears at a point along
the bar to indicate the gauge’s current value.

`struct AccessoryLinearCapacityGaugeStyle`

A gauge style that displays bar that fills from leading to trailing edges as
the gauge’s current value increases.

Structure

# LinearCapacityGaugeStyle

A gauge style that displays bar that fills from leading to trailing edges as
the gauge’s current value increases.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    struct LinearCapacityGaugeStyle

## Overview

Use `linearCapacity` to construct this style.

## Topics

### Creating the gauge style

`init()`

Creates a linear capacity gauge style.

## Relationships

### Conforms To

  * `GaugeStyle`

## See Also

### Supporting types

`struct DefaultGaugeStyle`

The default gauge view style in the current context of the view being styled.

`struct CircularGaugeStyle`

A gauge style that displays an open ring with a marker that appears at a point
along the ring to indicate the gauge’s current value.

`struct AccessoryCircularGaugeStyle`

A gauge style that displays an open ring with a marker that appears at a point
along the ring to indicate the gauge’s current value.

`struct AccessoryCircularCapacityGaugeStyle`

A gauge style that displays a closed ring that’s partially filled in to
indicate the gauge’s current value.

`struct LinearGaugeStyle`

A gauge style that displays a bar with a marker that appears at a point along
the bar to indicate the gauge’s current value.

`struct AccessoryLinearGaugeStyle`

A gauge style that displays bar with a marker that appears at a point along
the bar to indicate the gauge’s current value.

`struct AccessoryLinearCapacityGaugeStyle`

A gauge style that displays bar that fills from leading to trailing edges as
the gauge’s current value increases.

Structure

# AccessoryLinearGaugeStyle

A gauge style that displays bar with a marker that appears at a point along
the bar to indicate the gauge’s current value.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    struct AccessoryLinearGaugeStyle

## Overview

Use `accessoryLinear` to construct this style.

## Topics

### Creating the gauge style

`init()`

Creates an accessory linear gauge style.

## Relationships

### Conforms To

  * `GaugeStyle`

## See Also

### Supporting types

`struct DefaultGaugeStyle`

The default gauge view style in the current context of the view being styled.

`struct CircularGaugeStyle`

A gauge style that displays an open ring with a marker that appears at a point
along the ring to indicate the gauge’s current value.

`struct AccessoryCircularGaugeStyle`

A gauge style that displays an open ring with a marker that appears at a point
along the ring to indicate the gauge’s current value.

`struct AccessoryCircularCapacityGaugeStyle`

A gauge style that displays a closed ring that’s partially filled in to
indicate the gauge’s current value.

`struct LinearGaugeStyle`

A gauge style that displays a bar with a marker that appears at a point along
the bar to indicate the gauge’s current value.

`struct LinearCapacityGaugeStyle`

A gauge style that displays bar that fills from leading to trailing edges as
the gauge’s current value increases.

`struct AccessoryLinearCapacityGaugeStyle`

A gauge style that displays bar that fills from leading to trailing edges as
the gauge’s current value increases.

Structure

# AccessoryLinearCapacityGaugeStyle

A gauge style that displays bar that fills from leading to trailing edges as
the gauge’s current value increases.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    struct AccessoryLinearCapacityGaugeStyle

## Overview

Use `accessoryLinearCapacity` to construct this style.

## Topics

### Creating the gauge style

`init()`

Creates an accessory linear capacity gauge style.

## Relationships

### Conforms To

  * `GaugeStyle`

## See Also

### Supporting types

`struct DefaultGaugeStyle`

The default gauge view style in the current context of the view being styled.

`struct CircularGaugeStyle`

A gauge style that displays an open ring with a marker that appears at a point
along the ring to indicate the gauge’s current value.

`struct AccessoryCircularGaugeStyle`

A gauge style that displays an open ring with a marker that appears at a point
along the ring to indicate the gauge’s current value.

`struct AccessoryCircularCapacityGaugeStyle`

A gauge style that displays a closed ring that’s partially filled in to
indicate the gauge’s current value.

`struct LinearGaugeStyle`

A gauge style that displays a bar with a marker that appears at a point along
the bar to indicate the gauge’s current value.

`struct LinearCapacityGaugeStyle`

A gauge style that displays bar that fills from leading to trailing edges as
the gauge’s current value increases.

`struct AccessoryLinearGaugeStyle`

A gauge style that displays bar with a marker that appears at a point along
the bar to indicate the gauge’s current value.

