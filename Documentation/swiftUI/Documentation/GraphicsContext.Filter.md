Type Method

# brightness(_:)

Returns a filter that applies a brightness adjustment.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static func brightness(_ amount: Double) -> GraphicsContext.Filter

##  Parameters

`amount`

    

An amount to add to the pixel’s color components.

## Return Value

A filter that applies a brightness adjustment.

## Discussion

This filter is different than `brightness` filter primitive defined by the
Scalable Vector Graphics (SVG) specification. You can obtain an effect like
that filter using a `grayscale(_:)` color multiply. However, this filter does
match the `CIColorControls` filter’s brightness adjustment.

## See Also

### Changing brightness and contrast

`static func contrast(Double) -> GraphicsContext.Filter`

Returns a filter that applies a contrast adjustment.

Type Method

# contrast(_:)

Returns a filter that applies a contrast adjustment.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static func contrast(_ amount: Double) -> GraphicsContext.Filter

##  Parameters

`amount`

    

An amount to adjust the contrast. A value of zero leaves the result completely
gray. A value of one leaves the result unchanged. You can use values greater
than one.

## Return Value

A filter that applies a contrast adjustment.

## Discussion

This filter is equivalent to the `contrast` filter primitive defined by the
Scalable Vector Graphics (SVG) specification.

## See Also

### Changing brightness and contrast

`static func brightness(Double) -> GraphicsContext.Filter`

Returns a filter that applies a brightness adjustment.

Type Method

# saturation(_:)

Returns a filter that applies a saturation adjustment.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static func saturation(_ amount: Double) -> GraphicsContext.Filter

##  Parameters

`amount`

    

The amount of the saturation adjustment. A value of zero to completely
desaturates each pixel, while a value of one makes no change. You can use
values greater than one.

## Return Value

A filter that applies a saturation adjustment.

## Discussion

This filter is equivalent to the `saturate` filter primitive defined by the
Scalable Vector Graphics (SVG) specification.

## See Also

### Manipulating color

`static func colorInvert(Double) -> GraphicsContext.Filter`

Returns a filter that inverts the color of their results.

`static func colorMultiply(Color) -> GraphicsContext.Filter`

Returns a filter that multiplies each color component by the matching
component of a given color.

`static func hueRotation(Angle) -> GraphicsContext.Filter`

Returns a filter that applies a hue rotation adjustment.

`static func grayscale(Double) -> GraphicsContext.Filter`

Returns a filter that applies a grayscale adjustment.

`static func colorMatrix(ColorMatrix) -> GraphicsContext.Filter`

Returns a filter that multiplies by a given color matrix.

Type Method

# colorInvert(_:)

Returns a filter that inverts the color of their results.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static func colorInvert(_ amount: Double = 1) -> GraphicsContext.Filter

##  Parameters

`amount`

    

The inversion amount. A value of one results in total inversion, while a value
of zero leaves the result unchanged. Other values apply a linear multiplier
effect.

## Return Value

A filter that applies a color inversion.

## Discussion

This filter is equivalent to the `invert` filter primitive defined by the
Scalable Vector Graphics (SVG) specification.

## See Also

### Manipulating color

`static func saturation(Double) -> GraphicsContext.Filter`

Returns a filter that applies a saturation adjustment.

`static func colorMultiply(Color) -> GraphicsContext.Filter`

Returns a filter that multiplies each color component by the matching
component of a given color.

`static func hueRotation(Angle) -> GraphicsContext.Filter`

Returns a filter that applies a hue rotation adjustment.

`static func grayscale(Double) -> GraphicsContext.Filter`

Returns a filter that applies a grayscale adjustment.

`static func colorMatrix(ColorMatrix) -> GraphicsContext.Filter`

Returns a filter that multiplies by a given color matrix.

Type Method

# colorMultiply(_:)

Returns a filter that multiplies each color component by the matching
component of a given color.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static func colorMultiply(_ color: Color) -> GraphicsContext.Filter

##  Parameters

`color`

    

The color that the filter uses for the multiplication operation.

## Return Value

A filter that multiplies color components.

## See Also

### Manipulating color

`static func saturation(Double) -> GraphicsContext.Filter`

Returns a filter that applies a saturation adjustment.

`static func colorInvert(Double) -> GraphicsContext.Filter`

Returns a filter that inverts the color of their results.

`static func hueRotation(Angle) -> GraphicsContext.Filter`

Returns a filter that applies a hue rotation adjustment.

`static func grayscale(Double) -> GraphicsContext.Filter`

Returns a filter that applies a grayscale adjustment.

`static func colorMatrix(ColorMatrix) -> GraphicsContext.Filter`

Returns a filter that multiplies by a given color matrix.

Type Method

# hueRotation(_:)

Returns a filter that applies a hue rotation adjustment.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static func hueRotation(_ angle: Angle) -> GraphicsContext.Filter

##  Parameters

`angle`

    

The amount by which to rotate the hue value of each pixel.

## Return Value

A filter that applies a hue rotation adjustment.

## Discussion

This filter is equivalent to the `hue-rotate` filter primitive defined by the
Scalable Vector Graphics (SVG) specification.

## See Also

### Manipulating color

`static func saturation(Double) -> GraphicsContext.Filter`

Returns a filter that applies a saturation adjustment.

`static func colorInvert(Double) -> GraphicsContext.Filter`

Returns a filter that inverts the color of their results.

`static func colorMultiply(Color) -> GraphicsContext.Filter`

Returns a filter that multiplies each color component by the matching
component of a given color.

`static func grayscale(Double) -> GraphicsContext.Filter`

Returns a filter that applies a grayscale adjustment.

`static func colorMatrix(ColorMatrix) -> GraphicsContext.Filter`

Returns a filter that multiplies by a given color matrix.

Type Method

# grayscale(_:)

Returns a filter that applies a grayscale adjustment.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static func grayscale(_ amount: Double) -> GraphicsContext.Filter

##  Parameters

`amount`

    

An amount that controls the effect. A value of one makes the image completely
gray. A value of zero leaves the result unchanged. Other values apply a linear
multiplier effect.

## Return Value

A filter that applies a grayscale adjustment.

## Discussion

This filter is equivalent to the `grayscale` filter primitive defined by the
Scalable Vector Graphics (SVG) specification.

## See Also

### Manipulating color

`static func saturation(Double) -> GraphicsContext.Filter`

Returns a filter that applies a saturation adjustment.

`static func colorInvert(Double) -> GraphicsContext.Filter`

Returns a filter that inverts the color of their results.

`static func colorMultiply(Color) -> GraphicsContext.Filter`

Returns a filter that multiplies each color component by the matching
component of a given color.

`static func hueRotation(Angle) -> GraphicsContext.Filter`

Returns a filter that applies a hue rotation adjustment.

`static func colorMatrix(ColorMatrix) -> GraphicsContext.Filter`

Returns a filter that multiplies by a given color matrix.

Type Method

# colorMatrix(_:)

Returns a filter that multiplies by a given color matrix.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static func colorMatrix(_ matrix: ColorMatrix) -> GraphicsContext.Filter

##  Parameters

`matrix`

    

A `ColorMatrix` instance used by the filter.

## Return Value

A filter that transforms color using the given matrix.

## Discussion

This filter is equivalent to the `feColorMatrix` filter primitive defined by
the Scalable Vector Graphics (SVG) specification.

The filter creates the output color `[R', G', B', A']` at each pixel from an
input color `[R, G, B, A]` by multiplying the input color by the square matrix
formed by the first four columns of the `ColorMatrix`, then adding the fifth
column to the result:

## See Also

### Manipulating color

`static func saturation(Double) -> GraphicsContext.Filter`

Returns a filter that applies a saturation adjustment.

`static func colorInvert(Double) -> GraphicsContext.Filter`

Returns a filter that inverts the color of their results.

`static func colorMultiply(Color) -> GraphicsContext.Filter`

Returns a filter that multiplies each color component by the matching
component of a given color.

`static func hueRotation(Angle) -> GraphicsContext.Filter`

Returns a filter that applies a hue rotation adjustment.

`static func grayscale(Double) -> GraphicsContext.Filter`

Returns a filter that applies a grayscale adjustment.

Type Method

# blur(radius:options:)

Returns a filter that applies a Gaussian blur.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static func blur(
        radius: CGFloat,
        options: GraphicsContext.BlurOptions = BlurOptions()
    ) -> GraphicsContext.Filter

##  Parameters

`radius`

    

The standard deviation of the Gaussian blur.

`options`

    

A set of options controlling the application of the effect.

## Return Value

A filter that applies Gaussian blur.

Type Method

# shadow(color:radius:x:y:blendMode:options:)

Returns a filter that adds a shadow.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static func shadow(
        color: Color = Color(.sRGBLinear, white: 0, opacity: 0.33),
        radius: CGFloat,
        x: CGFloat = 0,
        y: CGFloat = 0,
        blendMode: GraphicsContext.BlendMode = .normal,
        options: GraphicsContext.ShadowOptions = ShadowOptions()
    ) -> GraphicsContext.Filter

##  Parameters

`color`

    

A `Color` that tints the shadow.

`radius`

    

A measure of how far the shadow extends from the edges of the content
receiving the shadow.

`x`

    

An amount to translate the shadow horizontally.

`y`

    

An amount to translate the shadow vertically.

`blendMode`

    

The `GraphicsContext.BlendMode` to use when blending the shadow into the
background layer.

`options`

    

A set of options that you can use to customize the process of adding the
shadow. Use one or more of the options in `GraphicsContext.ShadowOptions`.

## Return Value

A filter that adds a shadow style.

## Discussion

SwiftUI produces the shadow by blurring the alpha channel of the object
receiving the shadow, multiplying the result by a color, optionally
translating the shadow by an amount, and then blending the resulting shadow
into a new layer below the source primitive. You can customize some of these
steps by adding one or more shadow options.

Type Property

# luminanceToAlpha

Returns a filter that sets the opacity of each pixel based on its luminance.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var luminanceToAlpha: GraphicsContext.Filter { get }

## Return Value

A filter that applies a luminance to alpha transformation.

## Discussion

The filter computes the luminance of each pixel and uses it to define the
opacity of the result, combined with black (zero) color components.

## See Also

### Adjusting opacity

`static func alphaThreshold(min: Double, max: Double, color: Color) ->
GraphicsContext.Filter`

Returns a filter that replaces each pixel with alpha components within a range
by a constant color, or transparency otherwise.

Type Method

# alphaThreshold(min:max:color:)

Returns a filter that replaces each pixel with alpha components within a range
by a constant color, or transparency otherwise.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static func alphaThreshold(
        min: Double,
        max: Double = 1,
        color: Color = Color.black
    ) -> GraphicsContext.Filter

##  Parameters

`min`

    

The minimum alpha threshold. Pixels whose alpha component is less than this
value will render as transparent. Results are undefined unless `min < max`.

`max`

    

The maximum alpha threshold. Pixels whose alpha component is greater than this
value will render as transparent. Results are undefined unless `min < max`.

`color`

    

The color that is output for pixels with an alpha component between the two
threshold values.

## Return Value

A filter that applies a threshold to alpha values.

## See Also

### Adjusting opacity

`static var luminanceToAlpha: GraphicsContext.Filter`

Returns a filter that sets the opacity of each pixel based on its luminance.

Type Method

# projectionTransform(_:)

Returns a filter that that transforms the rasterized form of subsequent
graphics primitives.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static func projectionTransform(_ matrix: ProjectionTransform) -> GraphicsContext.Filter

##  Parameters

`matrix`

    

A projection transform to apply to the rasterized form of graphics primitives.

## Return Value

A filter that applies a transform.

Type Method

# colorShader(_:)

Returns a filter that applies `shader` to the color of each source pixel.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    static func colorShader(_ shader: Shader) -> GraphicsContext.Filter

##  Parameters

`shader`

    

The shader to apply to `self` as a color filter.

## Return Value

A filter that applies the shader as a color filter.

## Discussion

For a shader function to act as a color filter it must have a function
signature matching:

where `position` is the user-space coordinates of the pixel applied to the
shader and `color` its source color, as a pre-multiplied color in the
destination color space. `args...` should be compatible with the uniform
arguments bound to `shader`. The function should return the modified color
value.

## See Also

### Using a custom Metal shader

`static func distortionShader(Shader, maxSampleOffset: CGSize) ->
GraphicsContext.Filter`

Returns a filter that applies `shader` as a geometric distortion effect on the
location of each pixel.

`static func layerShader(Shader, maxSampleOffset: CGSize) ->
GraphicsContext.Filter`

Returns a filter that applies `shader` to the contents of the source layer.

Type Method

# distortionShader(_:maxSampleOffset:)

Returns a filter that applies `shader` as a geometric distortion effect on the
location of each pixel.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    static func distortionShader(
        _ shader: Shader,
        maxSampleOffset: CGSize
    ) -> GraphicsContext.Filter

##  Parameters

`shader`

    

The shader to apply as a distortion effect.

`maxSampleOffset`

    

The maximum distance in each axis between the returned source pixel position
and the destination pixel position, for all source pixels.

## Return Value

A new filter that applies the shader as a distortion effect.

## Discussion

For a shader function to act as a distortion effect it must have a function
signature matching:

where `position` is the user-space coordinates of the destination pixel
applied to the shader. `args...` should be compatible with the uniform
arguments bound to `shader`. The function should return the user-space
coordinates of the corresponding source pixel.

## See Also

### Using a custom Metal shader

`static func colorShader(Shader) -> GraphicsContext.Filter`

Returns a filter that applies `shader` to the color of each source pixel.

`static func layerShader(Shader, maxSampleOffset: CGSize) ->
GraphicsContext.Filter`

Returns a filter that applies `shader` to the contents of the source layer.

Type Method

# layerShader(_:maxSampleOffset:)

Returns a filter that applies `shader` to the contents of the source layer.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    static func layerShader(
        _ shader: Shader,
        maxSampleOffset: CGSize
    ) -> GraphicsContext.Filter

##  Parameters

`shader`

    

The shader to apply as a layer effect.

`maxSampleOffset`

    

If the shader function samples from the layer at locations not equal to the
destination position, this value must specify the maximum sampling distance in
each axis, for all source pixels.

## Return Value

A filter applies the shader as a layer effect.

## Discussion

For a shader function to act as a layer effect it must have a function
signature matching:

where `position` is the user-space coordinates of the destination pixel
applied to the shader, and `layer` is a rasterized subregion of the source
layer. `args...` should be compatible with the uniform arguments bound to
`shader`.

The `SwiftUI::Layer` type is defined in the `<SwiftUI/SwiftUI.h>` header file.
It exports a single `sample()` function that returns a linearly-filtered pixel
value from a position in the source content, as a premultiplied RGBA pixel
value:

The function should return the color mapping to the destination pixel,
typically by sampling one or more pixels from `layer` at location(s) derived
from `position` and them applying some kind of transformation to produce a new
color.

## See Also

### Using a custom Metal shader

`static func colorShader(Shader) -> GraphicsContext.Filter`

Returns a filter that applies `shader` to the color of each source pixel.

`static func distortionShader(Shader, maxSampleOffset: CGSize) ->
GraphicsContext.Filter`

Returns a filter that applies `shader` as a geometric distortion effect on the
location of each pixel.

