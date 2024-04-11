Initializer

# init(_:)

Creates a new instance from the specified gradient.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init(_ gradient: Gradient)

Instance Method

# colorSpace(_:)

Returns a version of the gradient that will use a specified color space for
interpolating between its colors.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func colorSpace(_ space: Gradient.ColorSpace) -> AnyGradient

##  Parameters

`space`

    

The color space the new gradient will use to interpolate its constituent
colors.

## Return Value

A new gradient that interpolates its colors in the specified color space.

## Discussion

