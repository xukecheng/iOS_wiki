Instance Property

# label

A view that describes the task represented by the progress view.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    var label: ProgressViewStyleConfiguration.Label?

## Discussion

If `nil`, then the task is self-evident from the surrounding context, and the
style does not need to provide any additional description.

If the progress view is defined using a `Progress` instance, then this label
is equivalent to its `localizedDescription`.

## See Also

### Configuring the label

`struct Label`

A type-erased label describing the task represented by the progress view.

Structure

# ProgressViewStyleConfiguration.Label

A type-erased label describing the task represented by the progress view.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    struct Label

## Relationships

### Conforms To

  * `View`

## See Also

### Configuring the label

`var label: ProgressViewStyleConfiguration.Label?`

A view that describes the task represented by the progress view.

Instance Property

# currentValueLabel

A view that describes the current value of a progress view.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    var currentValueLabel: ProgressViewStyleConfiguration.CurrentValueLabel?

## Discussion

If `nil`, then the value of the progress view is either self-evident from the
surrounding context or unknown, and the style does not need to provide any
additional description.

If the progress view is defined using a `Progress` instance, then this label
is equivalent to its `localizedAdditionalDescription`.

## See Also

### Configuring the current value label

`struct CurrentValueLabel`

A type-erased label that describes the current value of a progress view.

Structure

# ProgressViewStyleConfiguration.CurrentValueLabel

A type-erased label that describes the current value of a progress view.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    struct CurrentValueLabel

## Relationships

### Conforms To

  * `View`

## See Also

### Configuring the current value label

`var currentValueLabel: ProgressViewStyleConfiguration.CurrentValueLabel?`

A view that describes the current value of a progress view.

Instance Property

# fractionCompleted

The completed fraction of the task represented by the progress view, from
`0.0` (not yet started) to `1.0` (fully complete), or `nil` if the progress is
indeterminate or relative to a date interval.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    let fractionCompleted: Double?

