Instance Property

# label

A view that describes the purpose of the gauge.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 7.0+
visionOS 1.0+

    
    
    var label: GaugeStyleConfiguration.Label

## See Also

### Describing the purpose of the gauge

`struct Label`

A type-erased label of a gauge, describing its purpose.

Structure

# GaugeStyleConfiguration.Label

A type-erased label of a gauge, describing its purpose.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 7.0+
visionOS 1.0+

    
    
    struct Label

## Relationships

### Conforms To

  * `View`

## See Also

### Describing the purpose of the gauge

`var label: GaugeStyleConfiguration.Label`

A view that describes the purpose of the gauge.

Instance Property

# minimumValueLabel

A view that describes the minimum of the range for the current value.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 7.0+
visionOS 1.0+

    
    
    var minimumValueLabel: GaugeStyleConfiguration.MinimumValueLabel?

## See Also

### Reporting the range

`struct MinimumValueLabel`

A type-erased value label of a gauge describing the minimum value.

`var maximumValueLabel: GaugeStyleConfiguration.MaximumValueLabel?`

A view that describes the maximum of the range for the current value.

`struct MaximumValueLabel`

A type-erased value label of a gauge describing the maximum value.

Structure

# GaugeStyleConfiguration.MinimumValueLabel

A type-erased value label of a gauge describing the minimum value.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 7.0+
visionOS 1.0+

    
    
    struct MinimumValueLabel

## Relationships

### Conforms To

  * `View`

## See Also

### Reporting the range

`var minimumValueLabel: GaugeStyleConfiguration.MinimumValueLabel?`

A view that describes the minimum of the range for the current value.

`var maximumValueLabel: GaugeStyleConfiguration.MaximumValueLabel?`

A view that describes the maximum of the range for the current value.

`struct MaximumValueLabel`

A type-erased value label of a gauge describing the maximum value.

Instance Property

# maximumValueLabel

A view that describes the maximum of the range for the current value.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 7.0+
visionOS 1.0+

    
    
    var maximumValueLabel: GaugeStyleConfiguration.MaximumValueLabel?

## See Also

### Reporting the range

`var minimumValueLabel: GaugeStyleConfiguration.MinimumValueLabel?`

A view that describes the minimum of the range for the current value.

`struct MinimumValueLabel`

A type-erased value label of a gauge describing the minimum value.

`struct MaximumValueLabel`

A type-erased value label of a gauge describing the maximum value.

Structure

# GaugeStyleConfiguration.MaximumValueLabel

A type-erased value label of a gauge describing the maximum value.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 7.0+
visionOS 1.0+

    
    
    struct MaximumValueLabel

## Relationships

### Conforms To

  * `View`

## See Also

### Reporting the range

`var minimumValueLabel: GaugeStyleConfiguration.MinimumValueLabel?`

A view that describes the minimum of the range for the current value.

`struct MinimumValueLabel`

A type-erased value label of a gauge describing the minimum value.

`var maximumValueLabel: GaugeStyleConfiguration.MaximumValueLabel?`

A view that describes the maximum of the range for the current value.

Instance Property

# value

The current value of the gauge.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 7.0+
visionOS 1.0+

    
    
    var value: Double

## Discussion

The valid range is `0.0...1.0`.

## See Also

### Setting the value

`var currentValueLabel: GaugeStyleConfiguration.CurrentValueLabel?`

A view that describes the current value.

`struct CurrentValueLabel`

A type-erased value label of a gauge that contains the current value.

`struct MarkedValueLabel`

A type-erased label describing a specific value of a gauge.

Instance Property

# currentValueLabel

A view that describes the current value.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 7.0+
visionOS 1.0+

    
    
    var currentValueLabel: GaugeStyleConfiguration.CurrentValueLabel?

## See Also

### Setting the value

`var value: Double`

The current value of the gauge.

`struct CurrentValueLabel`

A type-erased value label of a gauge that contains the current value.

`struct MarkedValueLabel`

A type-erased label describing a specific value of a gauge.

Structure

# GaugeStyleConfiguration.CurrentValueLabel

A type-erased value label of a gauge that contains the current value.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 7.0+
visionOS 1.0+

    
    
    struct CurrentValueLabel

## Relationships

### Conforms To

  * `View`

## See Also

### Setting the value

`var value: Double`

The current value of the gauge.

`var currentValueLabel: GaugeStyleConfiguration.CurrentValueLabel?`

A view that describes the current value.

`struct MarkedValueLabel`

A type-erased label describing a specific value of a gauge.

Structure

# GaugeStyleConfiguration.MarkedValueLabel

A type-erased label describing a specific value of a gauge.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 7.0+
visionOS 1.0+

    
    
    struct MarkedValueLabel

## Relationships

### Conforms To

  * `View`

## See Also

### Setting the value

`var value: Double`

The current value of the gauge.

`var currentValueLabel: GaugeStyleConfiguration.CurrentValueLabel?`

A view that describes the current value.

`struct CurrentValueLabel`

A type-erased value label of a gauge that contains the current value.

