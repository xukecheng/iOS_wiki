Initializer

# init(value:in:label:)

Creates a gauge showing a value within a range and describes the gauge’s
purpose and current value.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 7.0+
visionOS 1.0+

    
    
    init<V>(
        value: V,
        in bounds: ClosedRange<V> = 0...1,
        @ViewBuilder label: () -> Label
    ) where CurrentValueLabel == EmptyView, BoundsLabel == EmptyView, MarkedValueLabels == EmptyView, V : BinaryFloatingPoint

##  Parameters

`value`

    

The value to show in the gauge.

`bounds`

    

The range of the valid values. Defaults to `0...1`.

`label`

    

A view that describes the purpose of the gauge.

## Discussion

Use this modifier to create a gauge that shows the value at its relative
position along the gauge and a label describing the gauge’s purpose. In the
example below, the gauge has a range of `0...1`, the indicator is set to
`0.4`, or 40 percent of the distance along the gauge:

## See Also

### Creating a gauge

`init<V>(value: V, in: ClosedRange<V>, label: () -> Label, currentValueLabel:
() -> CurrentValueLabel)`

Creates a gauge showing a value within a range and that describes the gauge’s
purpose and current value.

`init<V>(value: V, in: ClosedRange<V>, label: () -> Label, currentValueLabel:
() -> CurrentValueLabel, markedValueLabels: () -> MarkedValueLabels)`

Creates a gauge representing a value within a range.

`init<V>(value: V, in: ClosedRange<V>, label: () -> Label, currentValueLabel:
() -> CurrentValueLabel, minimumValueLabel: () -> BoundsLabel,
maximumValueLabel: () -> BoundsLabel)`

Creates a gauge showing a value within a range and describes the gauge’s
current, minimum, and maximum values.

`init<V>(value: V, in: ClosedRange<V>, label: () -> Label, currentValueLabel:
() -> CurrentValueLabel, minimumValueLabel: () -> BoundsLabel,
maximumValueLabel: () -> BoundsLabel, markedValueLabels: () ->
MarkedValueLabels)`

Creates a gauge representing a value within a range.

Initializer

# init(value:in:label:currentValueLabel:)

Creates a gauge showing a value within a range and that describes the gauge’s
purpose and current value.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 7.0+
visionOS 1.0+

    
    
    init<V>(
        value: V,
        in bounds: ClosedRange<V> = 0...1,
        @ViewBuilder label: () -> Label,
        @ViewBuilder currentValueLabel: () -> CurrentValueLabel
    ) where BoundsLabel == EmptyView, MarkedValueLabels == EmptyView, V : BinaryFloatingPoint

##  Parameters

`value`

    

The value to show on the gauge.

`bounds`

    

The range of the valid values. Defaults to `0...1`.

`label`

    

A view that describes the purpose of the gauge.

`currentValueLabel`

    

A view that describes the current value of the gauge.

## Discussion

Use this method to create a gauge that displays a value within a range you
supply with labels that describe the purpose of the gauge and its current
value. In the example below, a gauge using the `circular` style shows its
current value of `67` along with a label describing the (BPM) for the gauge:

## See Also

### Creating a gauge

`init<V>(value: V, in: ClosedRange<V>, label: () -> Label)`

Creates a gauge showing a value within a range and describes the gauge’s
purpose and current value.

`init<V>(value: V, in: ClosedRange<V>, label: () -> Label, currentValueLabel:
() -> CurrentValueLabel, markedValueLabels: () -> MarkedValueLabels)`

Creates a gauge representing a value within a range.

`init<V>(value: V, in: ClosedRange<V>, label: () -> Label, currentValueLabel:
() -> CurrentValueLabel, minimumValueLabel: () -> BoundsLabel,
maximumValueLabel: () -> BoundsLabel)`

Creates a gauge showing a value within a range and describes the gauge’s
current, minimum, and maximum values.

`init<V>(value: V, in: ClosedRange<V>, label: () -> Label, currentValueLabel:
() -> CurrentValueLabel, minimumValueLabel: () -> BoundsLabel,
maximumValueLabel: () -> BoundsLabel, markedValueLabels: () ->
MarkedValueLabels)`

Creates a gauge representing a value within a range.

Initializer

# init(value:in:label:currentValueLabel:markedValueLabels:)

Creates a gauge representing a value within a range.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 7.0+
visionOS 1.0+

    
    
    init<V>(
        value: V,
        in bounds: ClosedRange<V> = 0...1,
        @ViewBuilder label: () -> Label,
        @ViewBuilder currentValueLabel: () -> CurrentValueLabel,
        @ViewBuilder markedValueLabels: () -> MarkedValueLabels
    ) where BoundsLabel == EmptyView, V : BinaryFloatingPoint

##  Parameters

`value`

    

The value to show in the instance.

`bounds`

    

The range of the valid values. Defaults to `0...1`.

`label`

    

A view that describes the purpose of the gauge.

`currentValueLabel`

    

A view that describes the current value of the gauge.

`minimumValueLabel`

    

A view that describes the lower bounds of the gauge.

`maximumValueLabel`

    

A view that describes the upper bounds of the gauge.

`markedValueLabels`

    

A view builder containing tagged views, each of which describes a particular
value of the gauge. The method ignores this parameter.

## See Also

### Creating a gauge

`init<V>(value: V, in: ClosedRange<V>, label: () -> Label)`

Creates a gauge showing a value within a range and describes the gauge’s
purpose and current value.

`init<V>(value: V, in: ClosedRange<V>, label: () -> Label, currentValueLabel:
() -> CurrentValueLabel)`

Creates a gauge showing a value within a range and that describes the gauge’s
purpose and current value.

`init<V>(value: V, in: ClosedRange<V>, label: () -> Label, currentValueLabel:
() -> CurrentValueLabel, minimumValueLabel: () -> BoundsLabel,
maximumValueLabel: () -> BoundsLabel)`

Creates a gauge showing a value within a range and describes the gauge’s
current, minimum, and maximum values.

`init<V>(value: V, in: ClosedRange<V>, label: () -> Label, currentValueLabel:
() -> CurrentValueLabel, minimumValueLabel: () -> BoundsLabel,
maximumValueLabel: () -> BoundsLabel, markedValueLabels: () ->
MarkedValueLabels)`

Creates a gauge representing a value within a range.

Initializer

# init(value:in:label:currentValueLabel:minimumValueLabel:maximumValueLabel:)

Creates a gauge showing a value within a range and describes the gauge’s
current, minimum, and maximum values.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 7.0+
visionOS 1.0+

    
    
    init<V>(
        value: V,
        in bounds: ClosedRange<V> = 0...1,
        @ViewBuilder label: () -> Label,
        @ViewBuilder currentValueLabel: () -> CurrentValueLabel,
        @ViewBuilder minimumValueLabel: () -> BoundsLabel,
        @ViewBuilder maximumValueLabel: () -> BoundsLabel
    ) where MarkedValueLabels == EmptyView, V : BinaryFloatingPoint

##  Parameters

`value`

    

The value to show on the gauge.

`bounds`

    

The range of the valid values. Defaults to `0...1`.

`label`

    

A view that describes the purpose of the gauge.

`currentValueLabel`

    

A view that describes the current value of the gauge.

`minimumValueLabel`

    

A view that describes the lower bounds of the gauge.

`maximumValueLabel`

    

A view that describes the upper bounds of the gauge.

## Discussion

Use this method to create a gauge that shows a value within a prescribed
bounds. The gauge has labels that describe its purpose, and for the gauge’s
current, minimum, and maximum values.

## See Also

### Creating a gauge

`init<V>(value: V, in: ClosedRange<V>, label: () -> Label)`

Creates a gauge showing a value within a range and describes the gauge’s
purpose and current value.

`init<V>(value: V, in: ClosedRange<V>, label: () -> Label, currentValueLabel:
() -> CurrentValueLabel)`

Creates a gauge showing a value within a range and that describes the gauge’s
purpose and current value.

`init<V>(value: V, in: ClosedRange<V>, label: () -> Label, currentValueLabel:
() -> CurrentValueLabel, markedValueLabels: () -> MarkedValueLabels)`

Creates a gauge representing a value within a range.

`init<V>(value: V, in: ClosedRange<V>, label: () -> Label, currentValueLabel:
() -> CurrentValueLabel, minimumValueLabel: () -> BoundsLabel,
maximumValueLabel: () -> BoundsLabel, markedValueLabels: () ->
MarkedValueLabels)`

Creates a gauge representing a value within a range.

Initializer

#
init(value:in:label:currentValueLabel:minimumValueLabel:maximumValueLabel:markedValueLabels:)

Creates a gauge representing a value within a range.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 7.0+
visionOS 1.0+

    
    
    init<V>(
        value: V,
        in bounds: ClosedRange<V> = 0...1,
        @ViewBuilder label: () -> Label,
        @ViewBuilder currentValueLabel: () -> CurrentValueLabel,
        @ViewBuilder minimumValueLabel: () -> BoundsLabel,
        @ViewBuilder maximumValueLabel: () -> BoundsLabel,
        @ViewBuilder markedValueLabels: () -> MarkedValueLabels
    ) where V : BinaryFloatingPoint

##  Parameters

`value`

    

The value to show in the gauge.

`bounds`

    

The range of the valid values. Defaults to `0...1`.

`label`

    

A view that describes the purpose of the gauge.

`currentValueLabel`

    

A view that describes the current value of the gauge.

`minimumValueLabel`

    

A view that describes the lower bounds of the gauge.

`maximumValueLabel`

    

A view that describes the upper bounds of the gauge.

`markedValueLabels`

    

A view builder containing tagged views. each of which describes a particular
value of the gauge. The method ignores this parameter.

## See Also

### Creating a gauge

`init<V>(value: V, in: ClosedRange<V>, label: () -> Label)`

Creates a gauge showing a value within a range and describes the gauge’s
purpose and current value.

`init<V>(value: V, in: ClosedRange<V>, label: () -> Label, currentValueLabel:
() -> CurrentValueLabel)`

Creates a gauge showing a value within a range and that describes the gauge’s
purpose and current value.

`init<V>(value: V, in: ClosedRange<V>, label: () -> Label, currentValueLabel:
() -> CurrentValueLabel, markedValueLabels: () -> MarkedValueLabels)`

Creates a gauge representing a value within a range.

`init<V>(value: V, in: ClosedRange<V>, label: () -> Label, currentValueLabel:
() -> CurrentValueLabel, minimumValueLabel: () -> BoundsLabel,
maximumValueLabel: () -> BoundsLabel)`

Creates a gauge showing a value within a range and describes the gauge’s
current, minimum, and maximum values.

