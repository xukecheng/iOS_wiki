Type Method

# color(_:)

Returns a shading instance that fills with a color.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static func color(_ color: Color) -> GraphicsContext.Shading

##  Parameters

`color`

    

A `Color` instance that defines the color of the shading.

## Return Value

A shading instance filled with a color.

## See Also

### Colors

`static func color(Color.RGBColorSpace, red: Double, green: Double, blue:
Double, opacity: Double) -> GraphicsContext.Shading`

Returns a shading instance that fills with a color in the given color space.

`static func color(Color.RGBColorSpace, white: Double, opacity: Double) ->
GraphicsContext.Shading`

Returns a shading instance that fills with a monochrome color in the given
color space.

Type Method

# color(_:red:green:blue:opacity:)

Returns a shading instance that fills with a color in the given color space.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static func color(
        _ colorSpace: Color.RGBColorSpace = .sRGB,
        red: Double,
        green: Double,
        blue: Double,
        opacity: Double = 1
    ) -> GraphicsContext.Shading

##  Parameters

`colorSpace`

    

The RGB color space used to define the color. The default is
`Color.RGBColorSpace.sRGB`.

`red`

    

The red component of the color.

`green`

    

The green component of the color.

`blue`

    

The blue component of the color.

`opacity`

    

The opacity of the color. The default is `1`, which means fully opaque.

## Return Value

A shading instance filled with a color.

## See Also

### Colors

`static func color(Color) -> GraphicsContext.Shading`

Returns a shading instance that fills with a color.

`static func color(Color.RGBColorSpace, white: Double, opacity: Double) ->
GraphicsContext.Shading`

Returns a shading instance that fills with a monochrome color in the given
color space.

Type Method

# color(_:white:opacity:)

Returns a shading instance that fills with a monochrome color in the given
color space.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static func color(
        _ colorSpace: Color.RGBColorSpace = .sRGB,
        white: Double,
        opacity: Double = 1
    ) -> GraphicsContext.Shading

##  Parameters

`colorSpace`

    

The RGB color space used to define the color. The default is
`Color.RGBColorSpace.sRGB`.

`white`

    

The value to use for each of the red, green, and blue components of the color.

`opacity`

    

The opacity of the color. The default is `1`, which means fully opaque.

## Return Value

A shading instance filled with a color.

## See Also

### Colors

`static func color(Color) -> GraphicsContext.Shading`

Returns a shading instance that fills with a color.

`static func color(Color.RGBColorSpace, red: Double, green: Double, blue:
Double, opacity: Double) -> GraphicsContext.Shading`

Returns a shading instance that fills with a color in the given color space.

Type Method

# linearGradient(_:startPoint:endPoint:options:)

Returns a shading instance that fills a linear (axial) gradient.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static func linearGradient(
        _ gradient: Gradient,
        startPoint: CGPoint,
        endPoint: CGPoint,
        options: GraphicsContext.GradientOptions = GradientOptions()
    ) -> GraphicsContext.Shading

##  Parameters

`gradient`

    

A `Gradient` instance that defines the colors of the gradient.

`startPoint`

    

The start point of the gradient axis.

`endPoint`

    

The end point of the gradient axis.

`options`

    

Options that you use to configure the gradient.

## Return Value

A shading instance filled with a linear gradient.

## Discussion

The shading instance defines an axis from `startPoint` to `endPoint` in the
current user space and maps colors from `gradient` to lines perpendicular to
the axis.

## See Also

### Gradients

`static func radialGradient(Gradient, center: CGPoint, startRadius: CGFloat,
endRadius: CGFloat, options: GraphicsContext.GradientOptions) ->
GraphicsContext.Shading`

Returns a shading instance that fills a radial gradient.

`static func conicGradient(Gradient, center: CGPoint, angle: Angle, options:
GraphicsContext.GradientOptions) -> GraphicsContext.Shading`

Returns a shading instance that fills a conic (angular) gradient.

Type Method

# radialGradient(_:center:startRadius:endRadius:options:)

Returns a shading instance that fills a radial gradient.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static func radialGradient(
        _ gradient: Gradient,
        center: CGPoint,
        startRadius: CGFloat,
        endRadius: CGFloat,
        options: GraphicsContext.GradientOptions = GradientOptions()
    ) -> GraphicsContext.Shading

##  Parameters

`gradient`

    

A `Gradient` instance that defines the colors of the gradient.

`center`

    

The point in the current user space on which SwiftUI centers the gradient.

`startRadius`

    

The distance from the center where the gradient starts.

`endRadius`

    

The distance from the center where the gradient ends.

`options`

    

Options that you use to configure the gradient.

## Return Value

A shading instance filled with a radial gradient.

## See Also

### Gradients

`static func linearGradient(Gradient, startPoint: CGPoint, endPoint: CGPoint,
options: GraphicsContext.GradientOptions) -> GraphicsContext.Shading`

Returns a shading instance that fills a linear (axial) gradient.

`static func conicGradient(Gradient, center: CGPoint, angle: Angle, options:
GraphicsContext.GradientOptions) -> GraphicsContext.Shading`

Returns a shading instance that fills a conic (angular) gradient.

Type Method

# conicGradient(_:center:angle:options:)

Returns a shading instance that fills a conic (angular) gradient.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static func conicGradient(
        _ gradient: Gradient,
        center: CGPoint,
        angle: Angle = Angle(),
        options: GraphicsContext.GradientOptions = GradientOptions()
    ) -> GraphicsContext.Shading

##  Parameters

`gradient`

    

A `Gradient` instance that defines the colors of the gradient.

`center`

    

The point in the current user space on which SwiftUI centers the gradient.

`angle`

    

The angle about the center that SwiftUI uses to start and finish the gradient.
The gradient sweeps all the way around the center.

`options`

    

Options that you use to configure the gradient.

## Return Value

A shading instance filled with a conic gradient.

## See Also

### Gradients

`static func linearGradient(Gradient, startPoint: CGPoint, endPoint: CGPoint,
options: GraphicsContext.GradientOptions) -> GraphicsContext.Shading`

Returns a shading instance that fills a linear (axial) gradient.

`static func radialGradient(Gradient, center: CGPoint, startRadius: CGFloat,
endRadius: CGFloat, options: GraphicsContext.GradientOptions) ->
GraphicsContext.Shading`

Returns a shading instance that fills a radial gradient.

Type Method

# style(_:)

Returns a shading instance that fills with the given shape style.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static func style<S>(_ style: S) -> GraphicsContext.Shading where S : ShapeStyle

##  Parameters

`style`

    

A `ShapeStyle` instance to draw with.

## Return Value

A shading instance filled with a shape style.

## Discussion

Styles with geometry defined in a unit coordinate space map that space to the
rectangle associated with the drawn object. You can adjust that using the
`in(_:)` method. The shape style might affect the blend mode and opacity of
the drawn object.

## See Also

### Other shape styles

`static var foreground: GraphicsContext.Shading`

A shading instance that fills with the foreground style from the graphics
context’s environment.

Type Property

# foreground

A shading instance that fills with the foreground style from the graphics
context’s environment.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var foreground: GraphicsContext.Shading { get }

## See Also

### Other shape styles

`static func style<S>(S) -> GraphicsContext.Shading`

Returns a shading instance that fills with the given shape style.

Type Method

# tiledImage(_:origin:sourceRect:scale:)

Returns a shading instance that tiles an image across the infinite plane.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static func tiledImage(
        _ image: Image,
        origin: CGPoint = .zero,
        sourceRect: CGRect = CGRect(x: 0, y: 0, width: 1, height: 1),
        scale: CGFloat = 1
    ) -> GraphicsContext.Shading

##  Parameters

`image`

    

An `Image` to use as fill.

`origin`

    

The point in the current user space where SwiftUI places the bottom left
corner of the part of the image defined by `sourceRect`. The image repeats as
needed.

`sourceRect`

    

A unit space subregion of the image. The default is a unit rectangle, which
selects the whole image.

`scale`

    

A factor that you can use to control the image size.

## Return Value

A shading instance filled with a tiled image.

Type Method

# palette(_:)

Returns a multilevel shading instance constructed from an array of shading
instances.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static func palette(_ array: [GraphicsContext.Shading]) -> GraphicsContext.Shading

##  Parameters

`array`

    

An array of shading instances. The array must contain at least one element.

## Return Value

A shading instance composed from the given instances.

## See Also

### Composite shading types

`static var backdrop: GraphicsContext.Shading`

A shading instance that draws a copy of the current background.

Type Property

# backdrop

A shading instance that draws a copy of the current background.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var backdrop: GraphicsContext.Shading { get }

## See Also

### Composite shading types

`static func palette([GraphicsContext.Shading]) -> GraphicsContext.Shading`

Returns a multilevel shading instance constructed from an array of shading
instances.

Type Method

# shader(_:bounds:)

Returns a shading instance that fills with the results of querying a shader
for each pixel.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    static func shader(
        _ shader: Shader,
        bounds: CGRect = .zero
    ) -> GraphicsContext.Shading

##  Parameters

`shader`

    

The shader defining the filled colors.

`bounds`

    

The rect used to define any `bounds` arguments of the shader.

## Return Value

A shading instance that fills using the shader.

## Discussion

For a shader function to act as a shape fill it must have a function signature
matching:

where `position` is the user-space coordinates of the pixel applied to the
shader, and `args...` should be compatible with the uniform arguments bound to
`shader`. The function should return the premultiplied color value in the
color space of the destination (typically sRGB).

