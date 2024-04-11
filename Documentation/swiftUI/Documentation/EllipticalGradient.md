Initializer

# init(gradient:center:startRadiusFraction:endRadiusFraction:)

Creates an elliptical gradient.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init(
        gradient: Gradient,
        center: UnitPoint = .center,
        startRadiusFraction: CGFloat = 0,
        endRadiusFraction: CGFloat = 0.5
    )

## Discussion

For example, an elliptical gradient centered on the top-leading corner of the
view:

  * gradient: The colors and their parametric locations.

  * center: The center of the circle, in [0, 1] coordinates.

  * startRadiusFraction: The start radius value, as a fraction between zero and one. Zero maps to the center point, one maps to the diameter of the unit circle.

  * endRadiusFraction: The end radius value, as a fraction between zero and one. Zero maps to the center point, one maps to the diameter of the unit circle.

## See Also

### Creating an elliptical gradient

`init(colors: [Color], center: UnitPoint, startRadiusFraction: CGFloat,
endRadiusFraction: CGFloat)`

Creates an elliptical gradient from a collection of colors.

`init(stops: [Gradient.Stop], center: UnitPoint, startRadiusFraction: CGFloat,
endRadiusFraction: CGFloat)`

Creates an elliptical gradient from a collection of color stops.

Initializer

# init(colors:center:startRadiusFraction:endRadiusFraction:)

Creates an elliptical gradient from a collection of colors.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init(
        colors: [Color],
        center: UnitPoint = .center,
        startRadiusFraction: CGFloat = 0,
        endRadiusFraction: CGFloat = 0.5
    )

## Discussion

For example, an elliptical gradient centered on the top-leading corner of the
view:

  * colors: The colors, evenly distributed throughout the gradient.

  * center: The center of the circle, in [0, 1] coordinates.

  * startRadiusFraction: The start radius value, as a fraction between zero and one. Zero maps to the center point, one maps to the diameter of the unit circle.

  * endRadiusFraction: The end radius value, as a fraction between zero and one. Zero maps to the center point, one maps to the diameter of the unit circle.

## See Also

### Creating an elliptical gradient

`init(gradient: Gradient, center: UnitPoint, startRadiusFraction: CGFloat,
endRadiusFraction: CGFloat)`

Creates an elliptical gradient.

`init(stops: [Gradient.Stop], center: UnitPoint, startRadiusFraction: CGFloat,
endRadiusFraction: CGFloat)`

Creates an elliptical gradient from a collection of color stops.

Initializer

# init(stops:center:startRadiusFraction:endRadiusFraction:)

Creates an elliptical gradient from a collection of color stops.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init(
        stops: [Gradient.Stop],
        center: UnitPoint = .center,
        startRadiusFraction: CGFloat = 0,
        endRadiusFraction: CGFloat = 0.5
    )

## Discussion

For example, an elliptical gradient centered on the top-leading corner of the
view, with some extra green area:

  * stops: The colors and their parametric locations.

  * center: The center of the circle, in [0, 1] coordinates.

  * startRadiusFraction: The start radius value, as a fraction between zero and one. Zero maps to the center point, one maps to the diameter of the unit circle.

  * endRadiusFraction: The end radius value, as a fraction between zero and one. Zero maps to the center point, one maps to the diameter of the unit circle.

## See Also

### Creating an elliptical gradient

`init(gradient: Gradient, center: UnitPoint, startRadiusFraction: CGFloat,
endRadiusFraction: CGFloat)`

Creates an elliptical gradient.

`init(colors: [Color], center: UnitPoint, startRadiusFraction: CGFloat,
endRadiusFraction: CGFloat)`

Creates an elliptical gradient from a collection of colors.

