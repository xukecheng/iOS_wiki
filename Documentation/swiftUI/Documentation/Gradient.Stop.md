Initializer

# init(color:location:)

Creates a color stop with a color and location.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        color: Color,
        location: CGFloat
    )

Instance Property

# color

The color for the stop.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var color: Color

## See Also

### Configuring a gradient stop

`var location: CGFloat`

The parametric location of the stop.

Instance Property

# location

The parametric location of the stop.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var location: CGFloat

## Discussion

This value must be in the range `[0, 1]`.

## See Also

### Configuring a gradient stop

`var color: Color`

The color for the stop.

