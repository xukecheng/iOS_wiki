Initializer

# init(wrappedValue:)

Creates the scaled metric with an unscaled value using the default scaling.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(wrappedValue: Value)

## See Also

### Creating the metric

`init(wrappedValue: Value, relativeTo: Font.TextStyle)`

Creates the scaled metric with an unscaled value and a text style to scale
relative to.

Initializer

# init(wrappedValue:relativeTo:)

Creates the scaled metric with an unscaled value and a text style to scale
relative to.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(
        wrappedValue: Value,
        relativeTo textStyle: Font.TextStyle
    )

## See Also

### Creating the metric

`init(wrappedValue: Value)`

Creates the scaled metric with an unscaled value using the default scaling.

Instance Property

# wrappedValue

The value scaled based on the current environment.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    var wrappedValue: Value { get }

