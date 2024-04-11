Initializer

# init(colors:)

Creates a gradient from an array of colors.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(colors: [Color])

## Discussion

The gradient synthesizes its location values to evenly space the colors along
the gradient.

Initializer

# init(stops:)

Creates a gradient from an array of color stops.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(stops: [Gradient.Stop])

## See Also

### Creating a gradient from stops

`var stops: [Gradient.Stop]`

The array of color stops.

`struct Stop`

One color stop in the gradient.

Instance Property

# stops

The array of color stops.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var stops: [Gradient.Stop]

## See Also

### Creating a gradient from stops

`init(stops: [Gradient.Stop])`

Creates a gradient from an array of color stops.

`struct Stop`

One color stop in the gradient.

Structure

# Gradient.Stop

One color stop in the gradient.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct Stop

## Topics

### Creating a gradient stop

`init(color: Color, location: CGFloat)`

Creates a color stop with a color and location.

### Configuring a gradient stop

`var color: Color`

The color for the stop.

`var location: CGFloat`

The parametric location of the stop.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Creating a gradient from stops

`init(stops: [Gradient.Stop])`

Creates a gradient from an array of color stops.

`var stops: [Gradient.Stop]`

The array of color stops.

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

## See Also

### Working with color spaces

`struct ColorSpace`

A method of interpolating between the colors in a gradient.

Structure

# Gradient.ColorSpace

A method of interpolating between the colors in a gradient.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    struct ColorSpace

## Topics

### Getting an interpolation method

`static let device: Gradient.ColorSpace`

Interpolates gradient colors in the output color space.

`static let perceptual: Gradient.ColorSpace`

Interpolates gradient colors in a perceptual color space.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Working with color spaces

`func colorSpace(Gradient.ColorSpace) -> AnyGradient`

Returns a version of the gradient that will use a specified color space for
interpolating between its colors.

