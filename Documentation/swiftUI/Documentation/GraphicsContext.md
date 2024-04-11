Instance Method

# stroke(_:with:lineWidth:)

Draws a path into the context with a specified line width.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func stroke(
        _ path: Path,
        with shading: GraphicsContext.Shading,
        lineWidth: CGFloat = 1
    )

##  Parameters

`path`

    

The path to outline.

`shading`

    

The color or pattern to use when outlining the `path`.

`lineWidth`

    

The width of the stroke, which defaults to `1`.

## Discussion

When you call this method, all `StrokeStyle` properties other than `lineWidth`
take their default values. To control other style properties, use
`stroke(_:with:style:)` instead.

## See Also

### Drawing a path

`func stroke(Path, with: GraphicsContext.Shading, style: StrokeStyle)`

Draws a path into the context with a specified stroke style.

`func fill(Path, with: GraphicsContext.Shading, style: FillStyle)`

Draws a path into the context and fills the outlined region.

`func resolve(GraphicsContext.Shading) -> GraphicsContext.Shading`

Returns a version of a shading resolved with the current values of the
graphics context’s environment.

`struct Shading`

A color or pattern that you can use to outline or fill a path.

`struct GradientOptions`

Options that affect the rendering of color gradients.

Instance Method

# stroke(_:with:style:)

Draws a path into the context with a specified stroke style.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func stroke(
        _ path: Path,
        with shading: GraphicsContext.Shading,
        style: StrokeStyle
    )

##  Parameters

`path`

    

The path to outline.

`shading`

    

The color or pattern to use when outlining the `path`.

`style`

    

A style that indicates how to outline the path.

## Discussion

If you only need to control the style’s `lineWidth` property, use
`stroke(_:with:lineWidth:)` instead.

## See Also

### Drawing a path

`func stroke(Path, with: GraphicsContext.Shading, lineWidth: CGFloat)`

Draws a path into the context with a specified line width.

`func fill(Path, with: GraphicsContext.Shading, style: FillStyle)`

Draws a path into the context and fills the outlined region.

`func resolve(GraphicsContext.Shading) -> GraphicsContext.Shading`

Returns a version of a shading resolved with the current values of the
graphics context’s environment.

`struct Shading`

A color or pattern that you can use to outline or fill a path.

`struct GradientOptions`

Options that affect the rendering of color gradients.

Instance Method

# fill(_:with:style:)

Draws a path into the context and fills the outlined region.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func fill(
        _ path: Path,
        with shading: GraphicsContext.Shading,
        style: FillStyle = FillStyle()
    )

##  Parameters

`path`

    

The outline of the region to fill.

`shading`

    

The color or pattern to use when filling the region bounded by `path`.

`style`

    

A style that indicates how to rasterize the path.

## Discussion

The current drawing state of the context defines the full drawing operation.
For example, the current transformation and clip shapes, and any styles
applied to the result, affect the final result.

## See Also

### Drawing a path

`func stroke(Path, with: GraphicsContext.Shading, lineWidth: CGFloat)`

Draws a path into the context with a specified line width.

`func stroke(Path, with: GraphicsContext.Shading, style: StrokeStyle)`

Draws a path into the context with a specified stroke style.

`func resolve(GraphicsContext.Shading) -> GraphicsContext.Shading`

Returns a version of a shading resolved with the current values of the
graphics context’s environment.

`struct Shading`

A color or pattern that you can use to outline or fill a path.

`struct GradientOptions`

Options that affect the rendering of color gradients.

Instance Method

# resolve(_:)

Returns a version of a shading resolved with the current values of the
graphics context’s environment.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func resolve(_ shading: GraphicsContext.Shading) -> GraphicsContext.Shading

## Discussion

Calling this function once and then drawing multiple times with the result
will often have less overhead than drawing with the original shading multiple
times.

## See Also

### Drawing a path

`func stroke(Path, with: GraphicsContext.Shading, lineWidth: CGFloat)`

Draws a path into the context with a specified line width.

`func stroke(Path, with: GraphicsContext.Shading, style: StrokeStyle)`

Draws a path into the context with a specified stroke style.

`func fill(Path, with: GraphicsContext.Shading, style: FillStyle)`

Draws a path into the context and fills the outlined region.

`struct Shading`

A color or pattern that you can use to outline or fill a path.

`struct GradientOptions`

Options that affect the rendering of color gradients.

Structure

# GraphicsContext.Shading

A color or pattern that you can use to outline or fill a path.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    struct Shading

## Overview

Use a shading instance to describe the color or pattern of a path that you
outline with a method like `stroke(_:with:style:)`, or of the interior of a
region that you fill with the `fill(_:with:style:)` method. Get a shading
instance by calling one of the `Shading` structure’s factory methods. You can
base shading on:

  * A `Color`.

  * A `Gradient`.

  * Any type that conforms to `ShapeStyle`.

  * An `Image`.

  * What you’ve already drawn into the context.

  * A collection of other shading instances.

## Topics

### Colors

`static func color(Color) -> GraphicsContext.Shading`

Returns a shading instance that fills with a color.

`static func color(Color.RGBColorSpace, red: Double, green: Double, blue:
Double, opacity: Double) -> GraphicsContext.Shading`

Returns a shading instance that fills with a color in the given color space.

`static func color(Color.RGBColorSpace, white: Double, opacity: Double) ->
GraphicsContext.Shading`

Returns a shading instance that fills with a monochrome color in the given
color space.

### Gradients

`static func linearGradient(Gradient, startPoint: CGPoint, endPoint: CGPoint,
options: GraphicsContext.GradientOptions) -> GraphicsContext.Shading`

Returns a shading instance that fills a linear (axial) gradient.

`static func radialGradient(Gradient, center: CGPoint, startRadius: CGFloat,
endRadius: CGFloat, options: GraphicsContext.GradientOptions) ->
GraphicsContext.Shading`

Returns a shading instance that fills a radial gradient.

`static func conicGradient(Gradient, center: CGPoint, angle: Angle, options:
GraphicsContext.GradientOptions) -> GraphicsContext.Shading`

Returns a shading instance that fills a conic (angular) gradient.

### Other shape styles

`static func style<S>(S) -> GraphicsContext.Shading`

Returns a shading instance that fills with the given shape style.

`static var foreground: GraphicsContext.Shading`

A shading instance that fills with the foreground style from the graphics
context’s environment.

### Images

`static func tiledImage(Image, origin: CGPoint, sourceRect: CGRect, scale:
CGFloat) -> GraphicsContext.Shading`

Returns a shading instance that tiles an image across the infinite plane.

### Composite shading types

`static func palette([GraphicsContext.Shading]) -> GraphicsContext.Shading`

Returns a multilevel shading instance constructed from an array of shading
instances.

`static var backdrop: GraphicsContext.Shading`

A shading instance that draws a copy of the current background.

### Using a custom Metal shader

`static func shader(Shader, bounds: CGRect) -> GraphicsContext.Shading`

Returns a shading instance that fills with the results of querying a shader
for each pixel.

## Relationships

### Conforms To

  * `Sendable`

## See Also

### Drawing a path

`func stroke(Path, with: GraphicsContext.Shading, lineWidth: CGFloat)`

Draws a path into the context with a specified line width.

`func stroke(Path, with: GraphicsContext.Shading, style: StrokeStyle)`

Draws a path into the context with a specified stroke style.

`func fill(Path, with: GraphicsContext.Shading, style: FillStyle)`

Draws a path into the context and fills the outlined region.

`func resolve(GraphicsContext.Shading) -> GraphicsContext.Shading`

Returns a version of a shading resolved with the current values of the
graphics context’s environment.

`struct GradientOptions`

Options that affect the rendering of color gradients.

Structure

# GraphicsContext.GradientOptions

Options that affect the rendering of color gradients.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    @frozen
    struct GradientOptions

## Overview

Use these options to affect how SwiftUI manages a gradient that you create for
a `GraphicsContext.Shading` instance for use in a `GraphicsContext`.

## Topics

### Getting gradient options

`static var linearColor: GraphicsContext.GradientOptions`

An option that interpolates between colors in a linear color space.

`static var mirror: GraphicsContext.GradientOptions`

An option that repeats the gradient outside its nominal range, reflecting
every other instance.

`static var `repeat`: GraphicsContext.GradientOptions`

An option that repeats the gradient outside its nominal range.

## Relationships

### Conforms To

  * `Equatable`
  * `ExpressibleByArrayLiteral`
  * `OptionSet`
  * `RawRepresentable`
  * `Sendable`
  * `SetAlgebra`

## See Also

### Drawing a path

`func stroke(Path, with: GraphicsContext.Shading, lineWidth: CGFloat)`

Draws a path into the context with a specified line width.

`func stroke(Path, with: GraphicsContext.Shading, style: StrokeStyle)`

Draws a path into the context with a specified stroke style.

`func fill(Path, with: GraphicsContext.Shading, style: FillStyle)`

Draws a path into the context and fills the outlined region.

`func resolve(GraphicsContext.Shading) -> GraphicsContext.Shading`

Returns a version of a shading resolved with the current values of the
graphics context’s environment.

`struct Shading`

A color or pattern that you can use to outline or fill a path.

Instance Method

# draw(_:at:anchor:)

Draws an image into the context, aligning an anchor within the image to a
point in the context.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func draw(
        _ image: Image,
        at point: CGPoint,
        anchor: UnitPoint = .center
    )

##  Parameters

`image`

    

The `Image` to draw. Before drawing, the method converts the image to a
`GraphicsContext.ResolvedImage` by calling `resolve(_:)`.

`point`

    

A point within the rectangle of the resolved image to anchor to a point in the
context.

`anchor`

    

A `UnitPoint` within the context to align the image with. The default is
`center`.

## Discussion

The current context state defines the full drawing operation. For example, the
current transformation and clip shapes affect how SwiftUI draws the image.

## See Also

### Drawing an image

`func draw(Image, in: CGRect, style: FillStyle)`

Draws an image into the context, using the specified rectangle as a layout
frame.

`func draw(GraphicsContext.ResolvedImage, at: CGPoint, anchor: UnitPoint)`

Draws a resolved image into the context, aligning an anchor within the image
to a point in the context.

`func draw(GraphicsContext.ResolvedImage, in: CGRect, style: FillStyle)`

Draws a resolved image into the context, using the specified rectangle as a
layout frame.

`func resolve(Image) -> GraphicsContext.ResolvedImage`

Gets a version of an image that’s fixed with the current values of the
graphics context’s environment.

`struct ResolvedImage`

An image resolved to a particular environment.

Instance Method

# draw(_:in:style:)

Draws an image into the context, using the specified rectangle as a layout
frame.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func draw(
        _ image: Image,
        in rect: CGRect,
        style: FillStyle = FillStyle()
    )

##  Parameters

`image`

    

The `Image` to draw. Before drawing, the method converts the image to a
`GraphicsContext.ResolvedImage` by calling `resolve(_:)`.

`rect`

    

The rectangle in the current user space to draw the image in.

`style`

    

A fill style to use when rasterizing the image.

## Discussion

The current context state defines the full drawing operation. For example, the
current transformation and clip shapes affect how SwiftUI draws the image.

## See Also

### Drawing an image

`func draw(Image, at: CGPoint, anchor: UnitPoint)`

Draws an image into the context, aligning an anchor within the image to a
point in the context.

`func draw(GraphicsContext.ResolvedImage, at: CGPoint, anchor: UnitPoint)`

Draws a resolved image into the context, aligning an anchor within the image
to a point in the context.

`func draw(GraphicsContext.ResolvedImage, in: CGRect, style: FillStyle)`

Draws a resolved image into the context, using the specified rectangle as a
layout frame.

`func resolve(Image) -> GraphicsContext.ResolvedImage`

Gets a version of an image that’s fixed with the current values of the
graphics context’s environment.

`struct ResolvedImage`

An image resolved to a particular environment.

Instance Method

# draw(_:at:anchor:)

Draws a resolved image into the context, aligning an anchor within the image
to a point in the context.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func draw(
        _ image: GraphicsContext.ResolvedImage,
        at point: CGPoint,
        anchor: UnitPoint = .center
    )

##  Parameters

`image`

    

The `GraphicsContext.ResolvedImage` to draw. Get a resolved image from an
`Image` by calling `resolve(_:)`. Alternatively, you can call
`draw(_:at:anchor:)` with an `Image`, and that method performs the resolution
automatically.

`point`

    

A point within the rectangle of the resolved image to anchor to a point in the
context.

`anchor`

    

A `UnitPoint` within the context to align the image with. The default is
`center`.

## Discussion

The current context state defines the full drawing operation. For example, the
current transformation and clip shapes affect how SwiftUI draws the image.

## See Also

### Drawing an image

`func draw(Image, at: CGPoint, anchor: UnitPoint)`

Draws an image into the context, aligning an anchor within the image to a
point in the context.

`func draw(Image, in: CGRect, style: FillStyle)`

Draws an image into the context, using the specified rectangle as a layout
frame.

`func draw(GraphicsContext.ResolvedImage, in: CGRect, style: FillStyle)`

Draws a resolved image into the context, using the specified rectangle as a
layout frame.

`func resolve(Image) -> GraphicsContext.ResolvedImage`

Gets a version of an image that’s fixed with the current values of the
graphics context’s environment.

`struct ResolvedImage`

An image resolved to a particular environment.

Instance Method

# draw(_:in:style:)

Draws a resolved image into the context, using the specified rectangle as a
layout frame.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func draw(
        _ image: GraphicsContext.ResolvedImage,
        in rect: CGRect,
        style: FillStyle = FillStyle()
    )

##  Parameters

`image`

    

The `GraphicsContext.ResolvedImage` to draw. Get a resolved image from an
`Image` by calling `resolve(_:)`. Alternatively, you can call
`draw(_:in:style:)` with an `Image`, and that method performs the resolution
automatically.

`rect`

    

The rectangle in the current user space to draw the image in.

`style`

    

A fill style to use when rasterizing the image.

## Discussion

The current context state defines the full drawing operation. For example, the
current transformation and clip shapes affect how SwiftUI draws the image.

## See Also

### Drawing an image

`func draw(Image, at: CGPoint, anchor: UnitPoint)`

Draws an image into the context, aligning an anchor within the image to a
point in the context.

`func draw(Image, in: CGRect, style: FillStyle)`

Draws an image into the context, using the specified rectangle as a layout
frame.

`func draw(GraphicsContext.ResolvedImage, at: CGPoint, anchor: UnitPoint)`

Draws a resolved image into the context, aligning an anchor within the image
to a point in the context.

`func resolve(Image) -> GraphicsContext.ResolvedImage`

Gets a version of an image that’s fixed with the current values of the
graphics context’s environment.

`struct ResolvedImage`

An image resolved to a particular environment.

Instance Method

# resolve(_:)

Gets a version of an image that’s fixed with the current values of the
graphics context’s environment.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func resolve(_ image: Image) -> GraphicsContext.ResolvedImage

##  Parameters

`image`

    

The `Image` to resolve.

## Return Value

An image that’s resolved into the current context’s environment, taking into
account environment values like the display resolution and current color
scheme.

## Discussion

You can measure the resolved image by looking at its `size` and `baseline`
properties. You can draw the resolved image with the context’s
`draw(_:in:style:)` or `draw(_:at:anchor:)` method.

## See Also

### Drawing an image

`func draw(Image, at: CGPoint, anchor: UnitPoint)`

Draws an image into the context, aligning an anchor within the image to a
point in the context.

`func draw(Image, in: CGRect, style: FillStyle)`

Draws an image into the context, using the specified rectangle as a layout
frame.

`func draw(GraphicsContext.ResolvedImage, at: CGPoint, anchor: UnitPoint)`

Draws a resolved image into the context, aligning an anchor within the image
to a point in the context.

`func draw(GraphicsContext.ResolvedImage, in: CGRect, style: FillStyle)`

Draws a resolved image into the context, using the specified rectangle as a
layout frame.

`struct ResolvedImage`

An image resolved to a particular environment.

Structure

# GraphicsContext.ResolvedImage

An image resolved to a particular environment.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    struct ResolvedImage

## Overview

You resolve an `Image` in preparation for drawing it into a context, either
manually by calling `resolve(_:)`, or automatically when calling
`draw(_:in:style:)` or `draw(_:at:anchor:)`. The resolved image takes into
account environment values like the display resolution and current color
scheme.

## Topics

### Getting the image properties

`var size: CGSize`

The size of the image.

`let baseline: CGFloat`

The distance from the top of the image to its baseline.

`var shading: GraphicsContext.Shading?`

An optional shading to fill the image with.

## See Also

### Drawing an image

`func draw(Image, at: CGPoint, anchor: UnitPoint)`

Draws an image into the context, aligning an anchor within the image to a
point in the context.

`func draw(Image, in: CGRect, style: FillStyle)`

Draws an image into the context, using the specified rectangle as a layout
frame.

`func draw(GraphicsContext.ResolvedImage, at: CGPoint, anchor: UnitPoint)`

Draws a resolved image into the context, aligning an anchor within the image
to a point in the context.

`func draw(GraphicsContext.ResolvedImage, in: CGRect, style: FillStyle)`

Draws a resolved image into the context, using the specified rectangle as a
layout frame.

`func resolve(Image) -> GraphicsContext.ResolvedImage`

Gets a version of an image that’s fixed with the current values of the
graphics context’s environment.

Instance Method

# draw(_:at:anchor:)

Draws text into the context, aligning an anchor within the ideal size of the
rendered text to a point in the context.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func draw(
        _ text: Text,
        at point: CGPoint,
        anchor: UnitPoint = .center
    )

##  Parameters

`text`

    

The `Text` view to draw. Before drawing, the method converts the view to
`GraphicsContext.ResolvedText` by calling `resolve(_:)`.

`point`

    

A point within the rectangle of the resolved text to anchor to a point in the
context.

`anchor`

    

A `UnitPoint` within the context to align the text with. The default is
`center`.

## Discussion

The current context state defines the full drawing operation. For example, the
current transformation and clip shapes affect how SwiftUI draws the text.

## See Also

### Drawing text

`func draw(Text, in: CGRect)`

Draws text into the context using the specified rectangle as a layout frame.

`func draw(GraphicsContext.ResolvedText, at: CGPoint, anchor: UnitPoint)`

Draws resolved text into the context, aligning an anchor within the ideal size
of the text to a point in the context.

`func draw(GraphicsContext.ResolvedText, in: CGRect)`

Draws resolved text into the context using the specified rectangle as a layout
frame.

`func resolve(Text) -> GraphicsContext.ResolvedText`

Gets a version of a text view that’s fixed with the current values of the
graphics context’s environment.

`struct ResolvedText`

A text view resolved to a particular environment.

Instance Method

# draw(_:in:)

Draws text into the context using the specified rectangle as a layout frame.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func draw(
        _ text: Text,
        in rect: CGRect
    )

##  Parameters

`text`

    

The `Text` view to draw. Before drawing, the method converts the view to
`GraphicsContext.ResolvedText` by calling `resolve(_:)`.

`rect`

    

The rectangle in the current user space to draw the text in.

## Discussion

The current context state defines the full drawing operation. For example, the
current transformation and clip shapes affect how SwiftUI draws the text.

## See Also

### Drawing text

`func draw(Text, at: CGPoint, anchor: UnitPoint)`

Draws text into the context, aligning an anchor within the ideal size of the
rendered text to a point in the context.

`func draw(GraphicsContext.ResolvedText, at: CGPoint, anchor: UnitPoint)`

Draws resolved text into the context, aligning an anchor within the ideal size
of the text to a point in the context.

`func draw(GraphicsContext.ResolvedText, in: CGRect)`

Draws resolved text into the context using the specified rectangle as a layout
frame.

`func resolve(Text) -> GraphicsContext.ResolvedText`

Gets a version of a text view that’s fixed with the current values of the
graphics context’s environment.

`struct ResolvedText`

A text view resolved to a particular environment.

Instance Method

# draw(_:at:anchor:)

Draws resolved text into the context, aligning an anchor within the ideal size
of the text to a point in the context.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func draw(
        _ text: GraphicsContext.ResolvedText,
        at point: CGPoint,
        anchor: UnitPoint = .center
    )

##  Parameters

`text`

    

The `GraphicsContext.ResolvedText` to draw. Get resolved text from a `Text`
view by calling `resolve(_:)`. Alternatively, you can call
`draw(_:at:anchor:)` with a `Text` view, and that method performs the
resolution automatically.

`point`

    

A point within the rectangle of the ideal size of the resolved text to anchor
to a point in the context.

`anchor`

    

A `UnitPoint` within the context to align the text with. The default is
`center`.

## Discussion

The current context state defines the full drawing operation. For example, the
current transformation and clip shapes affect how SwiftUI draws the text.

## See Also

### Drawing text

`func draw(Text, at: CGPoint, anchor: UnitPoint)`

Draws text into the context, aligning an anchor within the ideal size of the
rendered text to a point in the context.

`func draw(Text, in: CGRect)`

Draws text into the context using the specified rectangle as a layout frame.

`func draw(GraphicsContext.ResolvedText, in: CGRect)`

Draws resolved text into the context using the specified rectangle as a layout
frame.

`func resolve(Text) -> GraphicsContext.ResolvedText`

Gets a version of a text view that’s fixed with the current values of the
graphics context’s environment.

`struct ResolvedText`

A text view resolved to a particular environment.

Instance Method

# draw(_:in:)

Draws resolved text into the context using the specified rectangle as a layout
frame.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func draw(
        _ text: GraphicsContext.ResolvedText,
        in rect: CGRect
    )

##  Parameters

`text`

    

The `GraphicsContext.ResolvedText` to draw. Get resolved text from a `Text`
view by calling `resolve(_:)`. Alternatively, you can call `draw(_:in:)` with
a `Text` view, and that method performs the resolution automatically.

`rect`

    

The rectangle in the current user space to draw the text in.

## Discussion

The current context state defines the full drawing operation. For example, the
current transformation and clip shapes affect how SwiftUI draws the text.

## See Also

### Drawing text

`func draw(Text, at: CGPoint, anchor: UnitPoint)`

Draws text into the context, aligning an anchor within the ideal size of the
rendered text to a point in the context.

`func draw(Text, in: CGRect)`

Draws text into the context using the specified rectangle as a layout frame.

`func draw(GraphicsContext.ResolvedText, at: CGPoint, anchor: UnitPoint)`

Draws resolved text into the context, aligning an anchor within the ideal size
of the text to a point in the context.

`func resolve(Text) -> GraphicsContext.ResolvedText`

Gets a version of a text view that’s fixed with the current values of the
graphics context’s environment.

`struct ResolvedText`

A text view resolved to a particular environment.

Instance Method

# resolve(_:)

Gets a version of a text view that’s fixed with the current values of the
graphics context’s environment.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func resolve(_ text: Text) -> GraphicsContext.ResolvedText

##  Parameters

`text`

    

The `Text` view to resolve.

## Return Value

A text view that’s resolved into the current context’s environment, taking
into account environment values like the display resolution and current color
scheme.

## Discussion

You can measure the resolved text by calling its `measure(in:)` method. You
can draw the resolved text with the context’s `draw(_:in:)` or
`draw(_:at:anchor:)` method.

## See Also

### Drawing text

`func draw(Text, at: CGPoint, anchor: UnitPoint)`

Draws text into the context, aligning an anchor within the ideal size of the
rendered text to a point in the context.

`func draw(Text, in: CGRect)`

Draws text into the context using the specified rectangle as a layout frame.

`func draw(GraphicsContext.ResolvedText, at: CGPoint, anchor: UnitPoint)`

Draws resolved text into the context, aligning an anchor within the ideal size
of the text to a point in the context.

`func draw(GraphicsContext.ResolvedText, in: CGRect)`

Draws resolved text into the context using the specified rectangle as a layout
frame.

`struct ResolvedText`

A text view resolved to a particular environment.

Structure

# GraphicsContext.ResolvedText

A text view resolved to a particular environment.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    struct ResolvedText

## Overview

You resolve a `Text` view in preparation for drawing it into a context, either
manually by calling `resolve(_:)` or automatically when calling `draw(_:in:)`
or `draw(_:at:anchor:)`. The resolved text view takes into account environment
values like the display resolution and current color scheme.

## Topics

### Getting the text properties

`func firstBaseline(in: CGSize) -> CGFloat`

Gets the distance from the first line’s ascender to its baseline.

`func lastBaseline(in: CGSize) -> CGFloat`

Gets the distance from the first line’s ascender to the last line’s baseline.

`func measure(in: CGSize) -> CGSize`

Measures the size of the resolved text for a given area into which the text
should be placed.

`var shading: GraphicsContext.Shading`

The shading to fill uncolored text regions with.

## See Also

### Drawing text

`func draw(Text, at: CGPoint, anchor: UnitPoint)`

Draws text into the context, aligning an anchor within the ideal size of the
rendered text to a point in the context.

`func draw(Text, in: CGRect)`

Draws text into the context using the specified rectangle as a layout frame.

`func draw(GraphicsContext.ResolvedText, at: CGPoint, anchor: UnitPoint)`

Draws resolved text into the context, aligning an anchor within the ideal size
of the text to a point in the context.

`func draw(GraphicsContext.ResolvedText, in: CGRect)`

Draws resolved text into the context using the specified rectangle as a layout
frame.

`func resolve(Text) -> GraphicsContext.ResolvedText`

Gets a version of a text view that’s fixed with the current values of the
graphics context’s environment.

Instance Method

# draw(_:at:anchor:)

Draws a resolved symbol into the context, aligning an anchor within the symbol
to a point in the context.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func draw(
        _ symbol: GraphicsContext.ResolvedSymbol,
        at point: CGPoint,
        anchor: UnitPoint = .center
    )

##  Parameters

`symbol`

    

The `GraphicsContext.ResolvedSymbol` view to draw. Get a resolved symbol by
calling `resolveSymbol(id:)` with the identifier that you use to tag the
corresponding child view during `Canvas` initialization.

`point`

    

A point within the rectangle of the resolved symbol to anchor to a point in
the context.

`anchor`

    

A `UnitPoint` within the context to align the symbol with. The default is
`center`.

## Discussion

The current context state defines the full drawing operation. For example, the
current transformation and clip shapes affect how SwiftUI draws the symbol.

## See Also

### Drawing a child view

`func draw(GraphicsContext.ResolvedSymbol, in: CGRect)`

Draws a resolved symbol into the context, using the specified rectangle as a
layout frame.

`func resolveSymbol<ID>(id: ID) -> GraphicsContext.ResolvedSymbol?`

Gets the identified child view as a resolved symbol, if the view exists.

`struct ResolvedSymbol`

A static sequence of drawing operations that may be drawn multiple times,
preserving their resolution independence.

Instance Method

# draw(_:in:)

Draws a resolved symbol into the context, using the specified rectangle as a
layout frame.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func draw(
        _ symbol: GraphicsContext.ResolvedSymbol,
        in rect: CGRect
    )

##  Parameters

`symbol`

    

The `GraphicsContext.ResolvedSymbol` to draw. Get a resolved symbol by calling
`resolveSymbol(id:)` with the identifier that you use to tag the corresponding
child view during `Canvas` initialization.

`rect`

    

The rectangle in the current user space to draw the symbol in.

## Discussion

The current context state defines the full drawing operation. For example, the
current transformation and clip shapes affect how SwiftUI draws the symbol.

## See Also

### Drawing a child view

`func draw(GraphicsContext.ResolvedSymbol, at: CGPoint, anchor: UnitPoint)`

Draws a resolved symbol into the context, aligning an anchor within the symbol
to a point in the context.

`func resolveSymbol<ID>(id: ID) -> GraphicsContext.ResolvedSymbol?`

Gets the identified child view as a resolved symbol, if the view exists.

`struct ResolvedSymbol`

A static sequence of drawing operations that may be drawn multiple times,
preserving their resolution independence.

Instance Method

# resolveSymbol(id:)

Gets the identified child view as a resolved symbol, if the view exists.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func resolveSymbol<ID>(id: ID) -> GraphicsContext.ResolvedSymbol? where ID : Hashable

##  Parameters

`id`

    

The value that you used to tag the view when you define it in the `symbols`
parameter of the `Canvas` initializer
`init(opaque:colorMode:rendersAsynchronously:renderer:symbols:)`.

## Return Value

The resolved symbol, or `nil` if SwiftUI can’t find a child view with the
given `id`.

## See Also

### Drawing a child view

`func draw(GraphicsContext.ResolvedSymbol, at: CGPoint, anchor: UnitPoint)`

Draws a resolved symbol into the context, aligning an anchor within the symbol
to a point in the context.

`func draw(GraphicsContext.ResolvedSymbol, in: CGRect)`

Draws a resolved symbol into the context, using the specified rectangle as a
layout frame.

`struct ResolvedSymbol`

A static sequence of drawing operations that may be drawn multiple times,
preserving their resolution independence.

Structure

# GraphicsContext.ResolvedSymbol

A static sequence of drawing operations that may be drawn multiple times,
preserving their resolution independence.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    struct ResolvedSymbol

## Overview

You resolve a child view in preparation for drawing it into a context by
calling `resolveSymbol(id:)`. The resolved view takes into account environment
values like the display resolution and current color scheme.

## Topics

### Getting the symbol properties

`var size: CGSize`

The dimensions of the resolved symbol.

## See Also

### Drawing a child view

`func draw(GraphicsContext.ResolvedSymbol, at: CGPoint, anchor: UnitPoint)`

Draws a resolved symbol into the context, aligning an anchor within the symbol
to a point in the context.

`func draw(GraphicsContext.ResolvedSymbol, in: CGRect)`

Draws a resolved symbol into the context, using the specified rectangle as a
layout frame.

`func resolveSymbol<ID>(id: ID) -> GraphicsContext.ResolvedSymbol?`

Gets the identified child view as a resolved symbol, if the view exists.

Instance Method

# drawLayer(content:)

Draws a new layer, created by drawing code that you provide, into the context.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func drawLayer(content: (inout GraphicsContext) throws -> Void) rethrows

##  Parameters

`context`

    

A closure that receives a new `GraphicsContext` as input. This context
represents a new transparency layer that you can draw into. When the closure
returns, SwiftUI draws the new layer into the current context.

Instance Method

# clip(to:style:options:)

Adds a path to the context’s array of clip shapes.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    mutating func clip(
        to path: Path,
        style: FillStyle = FillStyle(),
        options: GraphicsContext.ClipOptions = ClipOptions()
    )

##  Parameters

`path`

    

A `Path` that defines the shape of the clipping mask.

`style`

    

A `FillStyle` that defines how to rasterize the shape.

`options`

    

Clip options that tell SwiftUI how to interpret the `path` as a clip shape.
For example, you can invert the clip shape by setting the `inverse` option.

## Discussion

Call this method to add a shape to the array of clip shapes that the context
uses to define a clipping mask. Shapes that you add affect only subsequent
drawing operations.

## See Also

### Masking

`func clipToLayer(opacity: Double, options: GraphicsContext.ClipOptions,
content: (inout GraphicsContext) throws -> Void) rethrows`

Adds a clip shape that you define in a new layer to the context’s array of
clip shapes.

`var clipBoundingRect: CGRect`

The bounding rectangle of the intersection of all current clip shapes in the
current user space.

`struct ClipOptions`

Options that affect the use of clip shapes.

Instance Method

# clipToLayer(opacity:options:content:)

Adds a clip shape that you define in a new layer to the context’s array of
clip shapes.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    mutating func clipToLayer(
        opacity: Double = 1,
        options: GraphicsContext.ClipOptions = ClipOptions(),
        content: (inout GraphicsContext) throws -> Void
    ) rethrows

##  Parameters

`opacity`

    

A value that SwiftUI uses to multiply the alpha channel of the rasterized
layer that you define in the `content` closure. The alpha values that result
define the clip shape.

`options`

    

A set of options that tell SwiftUI how to interpret the clip shape. For
example, you can invert the clip shape by setting the `inverse` option.

`content`

    

A closure that receives as input a new `GraphicsContext`, which represents a
new transparency layer. The alpha channel of content that you draw into this
context, multiplied by the `opacity` parameter, defines the clip shape.

## Discussion

Call this method to add a shape to the array of clip shapes that the context
uses to define a clipping mask. Shapes that you add affect only subsequent
drawing operations.

## See Also

### Masking

`func clip(to: Path, style: FillStyle, options: GraphicsContext.ClipOptions)`

Adds a path to the context’s array of clip shapes.

`var clipBoundingRect: CGRect`

The bounding rectangle of the intersection of all current clip shapes in the
current user space.

`struct ClipOptions`

Options that affect the use of clip shapes.

Instance Property

# clipBoundingRect

The bounding rectangle of the intersection of all current clip shapes in the
current user space.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var clipBoundingRect: CGRect { get }

## See Also

### Masking

`func clip(to: Path, style: FillStyle, options: GraphicsContext.ClipOptions)`

Adds a path to the context’s array of clip shapes.

`func clipToLayer(opacity: Double, options: GraphicsContext.ClipOptions,
content: (inout GraphicsContext) throws -> Void) rethrows`

Adds a clip shape that you define in a new layer to the context’s array of
clip shapes.

`struct ClipOptions`

Options that affect the use of clip shapes.

Structure

# GraphicsContext.ClipOptions

Options that affect the use of clip shapes.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    @frozen
    struct ClipOptions

## Overview

Use these options to affect how SwiftUI interprets a clip shape when you call
`clip(to:style:options:)` to add a path to the array of clip shapes, or when
you call `clipToLayer(opacity:options:content:)` to add a clipping layer.

## Topics

### Getting clip options

`static var inverse: GraphicsContext.ClipOptions`

An option to invert the shape or layer alpha as the clip mask.

## Relationships

### Conforms To

  * `Equatable`
  * `ExpressibleByArrayLiteral`
  * `OptionSet`
  * `RawRepresentable`
  * `Sendable`
  * `SetAlgebra`

## See Also

### Masking

`func clip(to: Path, style: FillStyle, options: GraphicsContext.ClipOptions)`

Adds a path to the context’s array of clip shapes.

`func clipToLayer(opacity: Double, options: GraphicsContext.ClipOptions,
content: (inout GraphicsContext) throws -> Void) rethrows`

Adds a clip shape that you define in a new layer to the context’s array of
clip shapes.

`var clipBoundingRect: CGRect`

The bounding rectangle of the intersection of all current clip shapes in the
current user space.

Instance Property

# opacity

The opacity of drawing operations in the context.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var opacity: Double { get set }

## Discussion

Set this value to affect the opacity of content that you subsequently draw
into the context. Changing this value has no impact on the content you
previously drew into the context.

## See Also

### Setting opacity and the blend mode

`var blendMode: GraphicsContext.BlendMode`

The blend mode used by drawing operations in the context.

`struct BlendMode`

The ways that a graphics context combines new content with background content.

Instance Property

# blendMode

The blend mode used by drawing operations in the context.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var blendMode: GraphicsContext.BlendMode { get set }

## Discussion

Set this value to affect how any content that you subsequently draw into the
context blends with content that’s already in the context. Use one of the
`GraphicsContext.BlendMode` values.

## See Also

### Setting opacity and the blend mode

`var opacity: Double`

The opacity of drawing operations in the context.

`struct BlendMode`

The ways that a graphics context combines new content with background content.

Structure

# GraphicsContext.BlendMode

The ways that a graphics context combines new content with background content.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    @frozen
    struct BlendMode

## Overview

Use one of these values to set the `blendMode` property of a
`GraphicsContext`. The value that you set affects how content that you draw
replaces or combines with content that you previously drew into the context.

## Topics

### Getting the default

`static var normal: GraphicsContext.BlendMode`

A mode that paints source image samples over the background image samples.

### Darkening

`static var darken: GraphicsContext.BlendMode`

A mode that creates composite image samples by choosing the darker samples
from either the source image or the background.

`static var multiply: GraphicsContext.BlendMode`

A mode that multiplies the source image samples with the background image
samples.

`static var colorBurn: GraphicsContext.BlendMode`

A mode that darkens background image samples to reflect the source image
samples.

`static var plusDarker: GraphicsContext.BlendMode`

A mode that adds the inverse of the color components of the source and
background images, and then inverts the result, producing a darkened
composite.

### Lightening

`static var lighten: GraphicsContext.BlendMode`

A mode that creates composite image samples by choosing the lighter samples
from either the source image or the background.

`static var screen: GraphicsContext.BlendMode`

A mode that multiplies the inverse of the source image samples with the
inverse of the background image samples.

`static var colorDodge: GraphicsContext.BlendMode`

A mode that brightens the background image samples to reflect the source image
samples.

`static var plusLighter: GraphicsContext.BlendMode`

A mode that adds the components of the source and background images, resulting
in a lightened composite.

### Adding contrast

`static var overlay: GraphicsContext.BlendMode`

A mode that either multiplies or screens the source image samples with the
background image samples, depending on the background color.

`static var softLight: GraphicsContext.BlendMode`

A mode that either darkens or lightens colors, depending on the source image
sample color.

`static var hardLight: GraphicsContext.BlendMode`

A mode that either multiplies or screens colors, depending on the source image
sample color.

### Inverting

`static var difference: GraphicsContext.BlendMode`

A mode that subtracts the brighter of the source image sample color or the
background image sample color from the other.

`static var exclusion: GraphicsContext.BlendMode`

A mode that produces an effect similar to that produced by the difference
blend mode, but with lower contrast.

### Mixing color components

`static var hue: GraphicsContext.BlendMode`

A mode that uses the luminance and saturation values of the background with
the hue of the source image.

`static var saturation: GraphicsContext.BlendMode`

A mode that uses the luminance and hue values of the background with the
saturation of the source image.

`static var color: GraphicsContext.BlendMode`

A mode that uses the luminance values of the background with the hue and
saturation values of the source image.

`static var luminosity: GraphicsContext.BlendMode`

A mode that uses the hue and saturation of the background with the luminance
of the source image.

### Accessing porter-duff modes

`static var clear: GraphicsContext.BlendMode`

A mode that clears any pixels that the source image overwrites.

`static var copy: GraphicsContext.BlendMode`

A mode that replaces background image samples with source image samples.

`static var sourceIn: GraphicsContext.BlendMode`

A mode that you use to paint the source image, including its transparency,
onto the opaque parts of the background.

`static var sourceOut: GraphicsContext.BlendMode`

A mode that you use to paint the source image onto the transparent parts of
the background, while erasing the background.

`static var sourceAtop: GraphicsContext.BlendMode`

A mode that you use to paint the opaque parts of the source image onto the
opaque parts of the background.

`static var destinationOver: GraphicsContext.BlendMode`

A mode that you use to paint the source image under the background.

`static var destinationIn: GraphicsContext.BlendMode`

A mode that you use to erase any of the background that isn’t covered by
opaque source pixels.

`static var destinationOut: GraphicsContext.BlendMode`

A mode that you use to erase any of the background that is covered by opaque
source pixels.

`static var destinationAtop: GraphicsContext.BlendMode`

A mode that you use to paint the source image under the background, while
erasing any of the background not matched by opaque pixels from the source
image.

`static var xor: GraphicsContext.BlendMode`

A mode that you use to clear pixels where both the source and background
images are opaque.

## Relationships

### Conforms To

  * `Equatable`
  * `RawRepresentable`
  * `Sendable`

## See Also

### Setting opacity and the blend mode

`var opacity: Double`

The opacity of drawing operations in the context.

`var blendMode: GraphicsContext.BlendMode`

The blend mode used by drawing operations in the context.

Instance Method

# addFilter(_:options:)

Adds a filter that applies to subsequent drawing operations.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    mutating func addFilter(
        _ filter: GraphicsContext.Filter,
        options: GraphicsContext.FilterOptions = FilterOptions()
    )

##  Parameters

`filter`

    

A graphics context filter that you create by calling one of the
`GraphicsContext.Filter` factory methods.

`options`

    

A set of options from `GraphicsContext.FilterOptions` that you can use to
configure filter operations.

## Discussion

To draw with filtering, SwiftUI:

  * Rasterizes the drawing operation to an implicit transparency layer without blending, adjusting opacity, or applying any clipping.

  * Applies the filter to the layer containing the rasterized image.

  * Composites the layer onto the background, using the context’s current blend mode, opacity setting, and clip shapes.

When SwiftUI draws with a filter, the blend mode might apply to regions
outside the drawing operation’s intrinsic shape, but inside its clip shape.
That might result in unexpected behavior for certain blend modes like `copy`,
where the drawing operation completely overwrites the background even if the
source alpha is zero.

## See Also

### Filtering

`struct Filter`

A type that applies image processing operations to rendered content.

`struct FilterOptions`

Options that configure a filter that you add to a graphics context.

`struct BlurOptions`

Options that configure the graphics context filter that creates blur.

`struct ShadowOptions`

Options that configure the graphics context filter that creates shadows.

Structure

# GraphicsContext.Filter

A type that applies image processing operations to rendered content.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    struct Filter

## Overview

Create and configure a filter that produces an image processing effect, like
adding a drop shadow or a blur effect, by calling one of the factory methods
defined by the `Filter` structure. Call the `addFilter(_:options:)` method to
add the filter to a `GraphicsContext`. The filter only affects content that
you draw into the context after adding the filter.

## Topics

### Changing brightness and contrast

`static func brightness(Double) -> GraphicsContext.Filter`

Returns a filter that applies a brightness adjustment.

`static func contrast(Double) -> GraphicsContext.Filter`

Returns a filter that applies a contrast adjustment.

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

`static func colorMatrix(ColorMatrix) -> GraphicsContext.Filter`

Returns a filter that multiplies by a given color matrix.

### Adding blur

`static func blur(radius: CGFloat, options: GraphicsContext.BlurOptions) ->
GraphicsContext.Filter`

Returns a filter that applies a Gaussian blur.

### Adding a shadow

`static func shadow(color: Color, radius: CGFloat, x: CGFloat, y: CGFloat,
blendMode: GraphicsContext.BlendMode, options: GraphicsContext.ShadowOptions)
-> GraphicsContext.Filter`

Returns a filter that adds a shadow.

### Adjusting opacity

`static var luminanceToAlpha: GraphicsContext.Filter`

Returns a filter that sets the opacity of each pixel based on its luminance.

`static func alphaThreshold(min: Double, max: Double, color: Color) ->
GraphicsContext.Filter`

Returns a filter that replaces each pixel with alpha components within a range
by a constant color, or transparency otherwise.

### Adding a transformation

`static func projectionTransform(ProjectionTransform) ->
GraphicsContext.Filter`

Returns a filter that that transforms the rasterized form of subsequent
graphics primitives.

### Using a custom Metal shader

`static func colorShader(Shader) -> GraphicsContext.Filter`

Returns a filter that applies `shader` to the color of each source pixel.

`static func distortionShader(Shader, maxSampleOffset: CGSize) ->
GraphicsContext.Filter`

Returns a filter that applies `shader` as a geometric distortion effect on the
location of each pixel.

`static func layerShader(Shader, maxSampleOffset: CGSize) ->
GraphicsContext.Filter`

Returns a filter that applies `shader` to the contents of the source layer.

## Relationships

### Conforms To

  * `Sendable`

## See Also

### Filtering

`func addFilter(GraphicsContext.Filter, options:
GraphicsContext.FilterOptions)`

Adds a filter that applies to subsequent drawing operations.

`struct FilterOptions`

Options that configure a filter that you add to a graphics context.

`struct BlurOptions`

Options that configure the graphics context filter that creates blur.

`struct ShadowOptions`

Options that configure the graphics context filter that creates shadows.

Structure

# GraphicsContext.FilterOptions

Options that configure a filter that you add to a graphics context.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    @frozen
    struct FilterOptions

## Overview

You can use filter options to configure a `GraphicsContext.Filter` that you
apply to a `GraphicsContext` with the `addFilter(_:options:)` method.

## Topics

### Getting filter options

`static var linearColor: GraphicsContext.FilterOptions`

An option that causes the filter to perform calculations in a linear color
space.

## Relationships

### Conforms To

  * `Equatable`
  * `ExpressibleByArrayLiteral`
  * `OptionSet`
  * `RawRepresentable`
  * `Sendable`
  * `SetAlgebra`

## See Also

### Filtering

`func addFilter(GraphicsContext.Filter, options:
GraphicsContext.FilterOptions)`

Adds a filter that applies to subsequent drawing operations.

`struct Filter`

A type that applies image processing operations to rendered content.

`struct BlurOptions`

Options that configure the graphics context filter that creates blur.

`struct ShadowOptions`

Options that configure the graphics context filter that creates shadows.

Structure

# GraphicsContext.BlurOptions

Options that configure the graphics context filter that creates blur.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    @frozen
    struct BlurOptions

## Overview

You can use a set of these options when you call `blur(radius:options:)` to
create a `GraphicsContext.Filter` that adds blur to an object that you draw
into a `GraphicsContext`.

## Topics

### Getting blur options

`static var dithersResult: GraphicsContext.BlurOptions`

An option that causes the filter to dither the result, to reduce banding.

`static var opaque: GraphicsContext.BlurOptions`

An option that causes the filter to ensure the result is completely opaque.

## Relationships

### Conforms To

  * `Equatable`
  * `ExpressibleByArrayLiteral`
  * `OptionSet`
  * `RawRepresentable`
  * `Sendable`
  * `SetAlgebra`

## See Also

### Filtering

`func addFilter(GraphicsContext.Filter, options:
GraphicsContext.FilterOptions)`

Adds a filter that applies to subsequent drawing operations.

`struct Filter`

A type that applies image processing operations to rendered content.

`struct FilterOptions`

Options that configure a filter that you add to a graphics context.

`struct ShadowOptions`

Options that configure the graphics context filter that creates shadows.

Structure

# GraphicsContext.ShadowOptions

Options that configure the graphics context filter that creates shadows.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    @frozen
    struct ShadowOptions

## Overview

You can use a set of these options when you call
`shadow(color:radius:x:y:blendMode:options:)` to create a
`GraphicsContext.Filter` that adds a drop shadow to an object that you draw
into a `GraphicsContext`.

## Topics

### Getting shadow options

`static var disablesGroup: GraphicsContext.ShadowOptions`

An option that causes the filter to composite the object and its shadow
separately in the current layer.

`static var invertsAlpha: GraphicsContext.ShadowOptions`

An option that causes the filter to invert the alpha of the shadow.

`static var shadowAbove: GraphicsContext.ShadowOptions`

An option that causes the filter to draw the shadow above the object, rather
than below it.

`static var shadowOnly: GraphicsContext.ShadowOptions`

An option that causes the filter to draw only the shadow, and omit the source
object.

## Relationships

### Conforms To

  * `Equatable`
  * `ExpressibleByArrayLiteral`
  * `OptionSet`
  * `RawRepresentable`
  * `Sendable`
  * `SetAlgebra`

## See Also

### Filtering

`func addFilter(GraphicsContext.Filter, options:
GraphicsContext.FilterOptions)`

Adds a filter that applies to subsequent drawing operations.

`struct Filter`

A type that applies image processing operations to rendered content.

`struct FilterOptions`

Options that configure a filter that you add to a graphics context.

`struct BlurOptions`

Options that configure the graphics context filter that creates blur.

Instance Method

# scaleBy(x:y:)

Scales subsequent drawing operations by an amount in each dimension.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    mutating func scaleBy(
        x: CGFloat,
        y: CGFloat
    )

##  Parameters

`x`

    

The amount to scale in the horizontal direction.

`y`

    

The amount to scale in the vertical direction.

## Discussion

Calling this method is equivalent to updating the context’s `transform`
directly using the given scale factors:

## See Also

### Applying transforms

`func rotate(by: Angle)`

Rotates subsequent drawing operations by an angle.

`func translateBy(x: CGFloat, y: CGFloat)`

Moves subsequent drawing operations by an amount in each dimension.

`func concatenate(CGAffineTransform)`

Appends the given transform to the context’s existing transform.

`var transform: CGAffineTransform`

The current transform matrix, defining user space coordinates.

Instance Method

# rotate(by:)

Rotates subsequent drawing operations by an angle.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    mutating func rotate(by angle: Angle)

##  Parameters

`angle`

    

The amount to rotate.

## Discussion

Calling this method is equivalent to updating the context’s `transform`
directly using the `angle` parameter:

## See Also

### Applying transforms

`func scaleBy(x: CGFloat, y: CGFloat)`

Scales subsequent drawing operations by an amount in each dimension.

`func translateBy(x: CGFloat, y: CGFloat)`

Moves subsequent drawing operations by an amount in each dimension.

`func concatenate(CGAffineTransform)`

Appends the given transform to the context’s existing transform.

`var transform: CGAffineTransform`

The current transform matrix, defining user space coordinates.

Instance Method

# translateBy(x:y:)

Moves subsequent drawing operations by an amount in each dimension.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    mutating func translateBy(
        x: CGFloat,
        y: CGFloat
    )

##  Parameters

`x`

    

The amount to move in the horizontal direction.

`y`

    

The amount to move in the vertical direction.

## Discussion

Calling this method is equivalent to updating the context’s `transform`
directly using the given translation amount:

## See Also

### Applying transforms

`func scaleBy(x: CGFloat, y: CGFloat)`

Scales subsequent drawing operations by an amount in each dimension.

`func rotate(by: Angle)`

Rotates subsequent drawing operations by an angle.

`func concatenate(CGAffineTransform)`

Appends the given transform to the context’s existing transform.

`var transform: CGAffineTransform`

The current transform matrix, defining user space coordinates.

Instance Method

# concatenate(_:)

Appends the given transform to the context’s existing transform.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    mutating func concatenate(_ matrix: CGAffineTransform)

##  Parameters

`matrix`

    

A transform to append to the existing transform.

## Discussion

Calling this method is equivalent to updating the context’s `transform`
directly using the `matrix` parameter:

## See Also

### Applying transforms

`func scaleBy(x: CGFloat, y: CGFloat)`

Scales subsequent drawing operations by an amount in each dimension.

`func rotate(by: Angle)`

Rotates subsequent drawing operations by an angle.

`func translateBy(x: CGFloat, y: CGFloat)`

Moves subsequent drawing operations by an amount in each dimension.

`var transform: CGAffineTransform`

The current transform matrix, defining user space coordinates.

Instance Property

# transform

The current transform matrix, defining user space coordinates.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var transform: CGAffineTransform { get set }

## Discussion

Modify this matrix to transform content that you subsequently draw into the
context. Changes that you make don’t affect existing content.

## See Also

### Applying transforms

`func scaleBy(x: CGFloat, y: CGFloat)`

Scales subsequent drawing operations by an amount in each dimension.

`func rotate(by: Angle)`

Rotates subsequent drawing operations by an angle.

`func translateBy(x: CGFloat, y: CGFloat)`

Moves subsequent drawing operations by an amount in each dimension.

`func concatenate(CGAffineTransform)`

Appends the given transform to the context’s existing transform.

Instance Method

# withCGContext(content:)

Provides a Core Graphics context that you can use as a proxy to draw into this
context.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func withCGContext(content: (CGContext) throws -> Void) rethrows

##  Parameters

`content`

    

A closure that receives a `CGContext` that you use to perform drawing
operations, just like you draw into a `GraphicsContext` instance. Any filters,
blend mode settings, clip masks, and other state set before calling
`withCGContext(content:)` apply to drawing operations in the Core Graphics
context as well. Any state you set on the Core Graphics context is lost when
the closure returns. Accessing the Core Graphics context after the closure
returns produces undefined behavior.

## Discussion

Use this method to use existing drawing code that relies on Core Graphics
primitives.

Instance Property

# environment

The environment associated with the graphics context.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var environment: EnvironmentValues { get }

## Discussion

SwiftUI initially sets this to the environment of the context’s enclosing
view. The context uses values like display resolution and the color scheme
from the environment to resolve types like `Image` and `Color`. You can also
access values stored in the environment for your own purposes.

