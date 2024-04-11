# GraphicsContext.ResolvedSymbol

Instance Property

# size

The dimensions of the resolved symbol.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var size: CGSize { get }



# GraphicsContext.Shading

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



# Gradient.Stop

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



# GroupBoxStyleConfiguration

Instance Property

# label

A view that provides the title of the group box.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    let label: GroupBoxStyleConfiguration.Label

## See Also

### Configuring the label

`struct Label`

A type-erased label of a group box.

Structure

# GroupBoxStyleConfiguration.Label

A type-erased label of a group box.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    struct Label

## Relationships

### Conforms To

  * `View`

## See Also

### Configuring the label

`let label: GroupBoxStyleConfiguration.Label`

A view that provides the title of the group box.

Instance Property

# content

A view that represents the content of the group box.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    let content: GroupBoxStyleConfiguration.Content

## See Also

### Configuring the content

`struct Content`

A type-erased content of a group box.

Structure

# GroupBoxStyleConfiguration.Content

A type-erased content of a group box.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    struct Content

## Relationships

### Conforms To

  * `View`

## See Also

### Configuring the content

`let content: GroupBoxStyleConfiguration.Content`

A view that represents the content of the group box.



# Graphics and rendering modifiers

Instance Method

# mask(alignment:_:)

Masks this view using the alpha channel of the given view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func mask<Mask>(
        alignment: Alignment = .center,
        @ViewBuilder _ mask: () -> Mask
    ) -> some View where Mask : View
    

##  Parameters

`alignment`

    

The alignment for `mask` in relation to this view.

`mask`

    

The view whose alpha the rendering system applies to the specified view.

## Discussion

Use `mask(_:)` when you want to apply the alpha (opacity) value of another
view to the current view.

This example shows an image masked by rectangle with a 10% opacity:

## See Also

### Masking and clipping

`func clipped(antialiased: Bool) -> some View`

Clips this view to its bounding rectangular frame.

`func clipShape<S>(S, style: FillStyle) -> some View`

Sets a clipping shape for this view.

Instance Method

# clipped(antialiased:)

Clips this view to its bounding rectangular frame.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func clipped(antialiased: Bool = false) -> some View
    

##  Parameters

`antialiased`

    

A Boolean value that indicates whether the rendering system applies smoothing
to the edges of the clipping rectangle.

## Return Value

A view that clips this view to its bounding frame.

## Discussion

Use the `clipped(antialiased:)` modifier to hide any content that extends
beyond the layout bounds of the shape.

By default, a view’s bounding frame is used only for layout, so any content
that extends beyond the edges of the frame is still visible.

## See Also

### Masking and clipping

`func mask<Mask>(alignment: Alignment, () -> Mask) -> some View`

Masks this view using the alpha channel of the given view.

`func clipShape<S>(S, style: FillStyle) -> some View`

Sets a clipping shape for this view.

Instance Method

# clipShape(_:style:)

Sets a clipping shape for this view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func clipShape<S>(
        _ shape: S,
        style: FillStyle = FillStyle()
    ) -> some View where S : Shape
    

##  Parameters

`shape`

    

The clipping shape to use for this view. The `shape` fills the view’s frame,
while maintaining its aspect ratio.

`style`

    

The fill style to use when rasterizing `shape`.

## Return Value

A view that clips this view to `shape`, using `style` to define the shape’s
rasterization.

## Discussion

Use `clipShape(_:style:)` to clip the view to the provided shape. By applying
a clipping shape to a view, you preserve the parts of the view covered by the
shape, while eliminating other parts of the view. The clipping shape itself
isn’t visible.

For example, this code applies a circular clipping shape to a `Text` view:

The resulting view shows only the portion of the text that lies within the
bounds of the circle.

## See Also

### Masking and clipping

`func mask<Mask>(alignment: Alignment, () -> Mask) -> some View`

Masks this view using the alpha channel of the given view.

`func clipped(antialiased: Bool) -> some View`

Clips this view to its bounding rectangular frame.

Instance Method

# containerShape(_:)

Sets the container shape to use for any container relative shape within this
view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func containerShape<T>(_ shape: T) -> some View where T : InsettableShape
    

## Discussion

The example below defines a view that shows its content with a rounded
rectangle background and the same container shape. Any
`ContainerRelativeShape` within the `content` matches the rounded rectangle
shape from this container inset as appropriate.

## See Also

### Setting a container shape

`protocol InsettableShape`

A shape type that is able to inset itself to produce another shape.

`struct ContainerRelativeShape`

A shape that is replaced by an inset version of the current container shape.
If no container shape was defined, is replaced by a rectangle.

Instance Method

# scaledToFill()

Scales this view to fill its parent.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func scaledToFill() -> some View
    

## Return Value

A view that scales this view to fill its parent, maintaining this view’s
aspect ratio.

## Discussion

Use `scaledToFill()` to scale this view to fill its parent, while maintaining
the view’s aspect ratio as the view scales:

This method is equivalent to calling `aspectRatio(_:contentMode:)` with a
`nil` aspectRatio and a content mode of `ContentMode.fill`.

## See Also

### Scaling, rotating, or transforming a view

`func scaledToFit() -> some View`

Scales this view to fit its parent.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(CGSize, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified factor.

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified size in each dimension.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> ModifiedContent<Self,
_UniformScaleEffect>`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
some View`

Scales this view by the specified horizontal, vertical, and depth factors.

`func aspectRatio(CGFloat?, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the specified aspect ratio.

`func aspectRatio(CGSize, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the aspect ratio of the given size.

`func rotationEffect(Angle, anchor: UnitPoint) -> some View`

Rotates a view’s rendered output in two dimensions around the specified point.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some
View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some View`

Rotates the view’s content by the specified 3D rotation value.

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
some View`

Rotates the view’s content by an angle about an axis that you specify as a
rotation axis value.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> some View`

Rotates the view’s content by an angle about an axis that you specify as a
tuple of elements.

`func transformEffect(CGAffineTransform) -> some View`

Applies an affine transformation to this view’s rendered output.

`func transform3DEffect(AffineTransform3D) -> some View`

Applies a 3D transformation to the receiver.

`func projectionEffect(ProjectionTransform) -> some View`

Applies a projection transformation to this view’s rendered output.

`struct ProjectionTransform`

`enum ContentMode`

Constants that define how a view’s content fills the available space.

Instance Method

# scaledToFit()

Scales this view to fit its parent.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func scaledToFit() -> some View
    

## Return Value

A view that scales this view to fit its parent, maintaining this view’s aspect
ratio.

## Discussion

Use `scaledToFit()` to scale this view to fit its parent, while maintaining
the view’s aspect ratio as the view scales.

This method is equivalent to calling `aspectRatio(_:contentMode:)` with a
`nil` aspectRatio and a content mode of `ContentMode.fit`.

## See Also

### Scaling, rotating, or transforming a view

`func scaledToFill() -> some View`

Scales this view to fill its parent.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(CGSize, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified factor.

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified size in each dimension.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> ModifiedContent<Self,
_UniformScaleEffect>`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
some View`

Scales this view by the specified horizontal, vertical, and depth factors.

`func aspectRatio(CGFloat?, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the specified aspect ratio.

`func aspectRatio(CGSize, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the aspect ratio of the given size.

`func rotationEffect(Angle, anchor: UnitPoint) -> some View`

Rotates a view’s rendered output in two dimensions around the specified point.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some
View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some View`

Rotates the view’s content by the specified 3D rotation value.

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
some View`

Rotates the view’s content by an angle about an axis that you specify as a
rotation axis value.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> some View`

Rotates the view’s content by an angle about an axis that you specify as a
tuple of elements.

`func transformEffect(CGAffineTransform) -> some View`

Applies an affine transformation to this view’s rendered output.

`func transform3DEffect(AffineTransform3D) -> some View`

Applies a 3D transformation to the receiver.

`func projectionEffect(ProjectionTransform) -> some View`

Applies a projection transformation to this view’s rendered output.

`struct ProjectionTransform`

`enum ContentMode`

Constants that define how a view’s content fills the available space.

Instance Method

# scaleEffect(_:anchor:)

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func scaleEffect(
        _ s: CGFloat,
        anchor: UnitPoint = .center
    ) -> some View
    

##  Parameters

`s`

    

The amount to scale the view in the view in both the horizontal and vertical
directions.

`anchor`

    

The anchor point with a default of `center` that indicates the starting
position for the scale operation.

## Discussion

Use `scaleEffect(_:anchor:)` to apply a horizontally and vertically scaling
transform to a view.

## See Also

### Scaling, rotating, or transforming a view

`func scaledToFill() -> some View`

Scales this view to fill its parent.

`func scaledToFit() -> some View`

Scales this view to fit its parent.

`func scaleEffect(CGSize, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified factor.

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified size in each dimension.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> ModifiedContent<Self,
_UniformScaleEffect>`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
some View`

Scales this view by the specified horizontal, vertical, and depth factors.

`func aspectRatio(CGFloat?, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the specified aspect ratio.

`func aspectRatio(CGSize, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the aspect ratio of the given size.

`func rotationEffect(Angle, anchor: UnitPoint) -> some View`

Rotates a view’s rendered output in two dimensions around the specified point.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some
View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some View`

Rotates the view’s content by the specified 3D rotation value.

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
some View`

Rotates the view’s content by an angle about an axis that you specify as a
rotation axis value.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> some View`

Rotates the view’s content by an angle about an axis that you specify as a
tuple of elements.

`func transformEffect(CGAffineTransform) -> some View`

Applies an affine transformation to this view’s rendered output.

`func transform3DEffect(AffineTransform3D) -> some View`

Applies a 3D transformation to the receiver.

`func projectionEffect(ProjectionTransform) -> some View`

Applies a projection transformation to this view’s rendered output.

`struct ProjectionTransform`

`enum ContentMode`

Constants that define how a view’s content fills the available space.

Instance Method

# scaleEffect(_:anchor:)

Scales this view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func scaleEffect(
        _ scale: CGSize,
        anchor: UnitPoint = .center
    ) -> some View
    

##  Parameters

`scale`

    

A `CGSize` that represents the horizontal and vertical amount to scale the
view.

`anchor`

    

The point with a default of `center` that defines the location within the view
from which to apply the transformation.

## Discussion

Use `scaleEffect(_:anchor:)` to scale a view by applying a scaling transform
of a specific size, specified by `scale`.

## See Also

### Scaling, rotating, or transforming a view

`func scaledToFill() -> some View`

Scales this view to fill its parent.

`func scaledToFit() -> some View`

Scales this view to fit its parent.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified factor.

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified size in each dimension.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> ModifiedContent<Self,
_UniformScaleEffect>`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
some View`

Scales this view by the specified horizontal, vertical, and depth factors.

`func aspectRatio(CGFloat?, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the specified aspect ratio.

`func aspectRatio(CGSize, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the aspect ratio of the given size.

`func rotationEffect(Angle, anchor: UnitPoint) -> some View`

Rotates a view’s rendered output in two dimensions around the specified point.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some
View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some View`

Rotates the view’s content by the specified 3D rotation value.

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
some View`

Rotates the view’s content by an angle about an axis that you specify as a
rotation axis value.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> some View`

Rotates the view’s content by an angle about an axis that you specify as a
tuple of elements.

`func transformEffect(CGAffineTransform) -> some View`

Applies an affine transformation to this view’s rendered output.

`func transform3DEffect(AffineTransform3D) -> some View`

Applies a 3D transformation to the receiver.

`func projectionEffect(ProjectionTransform) -> some View`

Applies a projection transformation to this view’s rendered output.

`struct ProjectionTransform`

`enum ContentMode`

Constants that define how a view’s content fills the available space.

Instance Method

# scaleEffect(_:anchor:)

Scales this view uniformly by the specified factor.

visionOS 1.0+

    
    
    func scaleEffect(
        _ s: CGFloat,
        anchor: UnitPoint3D = .center
    ) -> some View
    

##  Parameters

`s`

    

The scale factor for this view.

`anchor`

    

The anchor point about which to scale the view. Defaults to center.

## Return Value

A view that scales this view by `s` in all dimensions.

## Discussion

The original dimensions of the view are considered to be unchanged by scaling
the contents. To change the dimensions of the view, use a modifier like
`frame()` instead.

## See Also

### Scaling, rotating, or transforming a view

`func scaledToFill() -> some View`

Scales this view to fill its parent.

`func scaledToFit() -> some View`

Scales this view to fit its parent.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(CGSize, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified size in each dimension.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> ModifiedContent<Self,
_UniformScaleEffect>`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
some View`

Scales this view by the specified horizontal, vertical, and depth factors.

`func aspectRatio(CGFloat?, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the specified aspect ratio.

`func aspectRatio(CGSize, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the aspect ratio of the given size.

`func rotationEffect(Angle, anchor: UnitPoint) -> some View`

Rotates a view’s rendered output in two dimensions around the specified point.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some
View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some View`

Rotates the view’s content by the specified 3D rotation value.

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
some View`

Rotates the view’s content by an angle about an axis that you specify as a
rotation axis value.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> some View`

Rotates the view’s content by an angle about an axis that you specify as a
tuple of elements.

`func transformEffect(CGAffineTransform) -> some View`

Applies an affine transformation to this view’s rendered output.

`func transform3DEffect(AffineTransform3D) -> some View`

Applies a 3D transformation to the receiver.

`func projectionEffect(ProjectionTransform) -> some View`

Applies a projection transformation to this view’s rendered output.

`struct ProjectionTransform`

`enum ContentMode`

Constants that define how a view’s content fills the available space.

Instance Method

# scaleEffect(_:anchor:)

Scales this view uniformly by the specified size in each dimension.

visionOS 1.0+

    
    
    func scaleEffect(
        _ scale: Size3D,
        anchor: UnitPoint3D = .center
    ) -> some View
    

##  Parameters

`scale`

    

The scale factor for this view in each dimension.

`anchor`

    

The anchor point about which to scale the view. Defaults to center.

## Return Value

A view that scales this view by `scale`.

## Discussion

The original dimensions of the view are considered to be unchanged by scaling
the contents. To change the dimensions of the view, use a modifier like
`frame()` instead.

## See Also

### Scaling, rotating, or transforming a view

`func scaledToFill() -> some View`

Scales this view to fill its parent.

`func scaledToFit() -> some View`

Scales this view to fit its parent.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(CGSize, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified factor.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> ModifiedContent<Self,
_UniformScaleEffect>`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
some View`

Scales this view by the specified horizontal, vertical, and depth factors.

`func aspectRatio(CGFloat?, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the specified aspect ratio.

`func aspectRatio(CGSize, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the aspect ratio of the given size.

`func rotationEffect(Angle, anchor: UnitPoint) -> some View`

Rotates a view’s rendered output in two dimensions around the specified point.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some
View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some View`

Rotates the view’s content by the specified 3D rotation value.

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
some View`

Rotates the view’s content by an angle about an axis that you specify as a
rotation axis value.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> some View`

Rotates the view’s content by an angle about an axis that you specify as a
tuple of elements.

`func transformEffect(CGAffineTransform) -> some View`

Applies an affine transformation to this view’s rendered output.

`func transform3DEffect(AffineTransform3D) -> some View`

Applies a 3D transformation to the receiver.

`func projectionEffect(ProjectionTransform) -> some View`

Applies a projection transformation to this view’s rendered output.

`struct ProjectionTransform`

`enum ContentMode`

Constants that define how a view’s content fills the available space.

Instance Method

# scaleEffect(_:anchor:)

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func scaleEffect(
        _ s: CGFloat,
        anchor: UnitPoint = .center
    ) -> ModifiedContent<Self, _UniformScaleEffect>

##  Parameters

`s`

    

The amount to scale the view in the view in both the horizontal and vertical
directions.

`anchor`

    

The anchor point with a default of `center` that indicates the starting
position for the scale operation.

## Discussion

Use `scaleEffect(_:anchor:)` to apply a horizontally and vertically scaling
transform to a view.

## See Also

### Scaling, rotating, or transforming a view

`func scaledToFill() -> some View`

Scales this view to fill its parent.

`func scaledToFit() -> some View`

Scales this view to fit its parent.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(CGSize, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified factor.

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified size in each dimension.

`func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
some View`

Scales this view by the specified horizontal, vertical, and depth factors.

`func aspectRatio(CGFloat?, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the specified aspect ratio.

`func aspectRatio(CGSize, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the aspect ratio of the given size.

`func rotationEffect(Angle, anchor: UnitPoint) -> some View`

Rotates a view’s rendered output in two dimensions around the specified point.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some
View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some View`

Rotates the view’s content by the specified 3D rotation value.

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
some View`

Rotates the view’s content by an angle about an axis that you specify as a
rotation axis value.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> some View`

Rotates the view’s content by an angle about an axis that you specify as a
tuple of elements.

`func transformEffect(CGAffineTransform) -> some View`

Applies an affine transformation to this view’s rendered output.

`func transform3DEffect(AffineTransform3D) -> some View`

Applies a 3D transformation to the receiver.

`func projectionEffect(ProjectionTransform) -> some View`

Applies a projection transformation to this view’s rendered output.

`struct ProjectionTransform`

`enum ContentMode`

Constants that define how a view’s content fills the available space.

Instance Method

# scaleEffect(x:y:anchor:)

Scales this view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func scaleEffect(
        x: CGFloat = 1.0,
        y: CGFloat = 1.0,
        anchor: UnitPoint = .center
    ) -> some View
    

##  Parameters

`x`

    

An amount that represents the horizontal amount to scale the view. The default
value is `1.0`.

`y`

    

An amount that represents the vertical amount to scale the view. The default
value is `1.0`.

`anchor`

    

The anchor point that indicates the starting position for the scale operation.

## Discussion

Use `scaleEffect(x:y:anchor:)` to apply a scaling transform to a view by a
specific horizontal and vertical amount.

## See Also

### Scaling, rotating, or transforming a view

`func scaledToFill() -> some View`

Scales this view to fill its parent.

`func scaledToFit() -> some View`

Scales this view to fit its parent.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(CGSize, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified factor.

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified size in each dimension.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> ModifiedContent<Self,
_UniformScaleEffect>`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
some View`

Scales this view by the specified horizontal, vertical, and depth factors.

`func aspectRatio(CGFloat?, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the specified aspect ratio.

`func aspectRatio(CGSize, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the aspect ratio of the given size.

`func rotationEffect(Angle, anchor: UnitPoint) -> some View`

Rotates a view’s rendered output in two dimensions around the specified point.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some
View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some View`

Rotates the view’s content by the specified 3D rotation value.

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
some View`

Rotates the view’s content by an angle about an axis that you specify as a
rotation axis value.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> some View`

Rotates the view’s content by an angle about an axis that you specify as a
tuple of elements.

`func transformEffect(CGAffineTransform) -> some View`

Applies an affine transformation to this view’s rendered output.

`func transform3DEffect(AffineTransform3D) -> some View`

Applies a 3D transformation to the receiver.

`func projectionEffect(ProjectionTransform) -> some View`

Applies a projection transformation to this view’s rendered output.

`struct ProjectionTransform`

`enum ContentMode`

Constants that define how a view’s content fills the available space.

Instance Method

# scaleEffect(x:y:z:anchor:)

Scales this view by the specified horizontal, vertical, and depth factors.

visionOS 1.0+

    
    
    func scaleEffect(
        x: CGFloat = 1.0,
        y: CGFloat = 1.0,
        z: CGFloat = 1.0,
        anchor: UnitPoint3D = .center
    ) -> some View
    

##  Parameters

`x`

    

The horizontal scale factor for this view.

`y`

    

The vertical scale factor for this view.

`z`

    

The depth scale factor for this view.

`anchor`

    

The anchor point about which to scale the view. Defaults to center.

## Return Value

A view that scales this view by `x`,`y`, and `z`.

## Discussion

The original dimensions of the view are considered to be unchanged by scaling
the contents. To change the dimensions of the view, use a modifier like
`frame()` instead.

## See Also

### Scaling, rotating, or transforming a view

`func scaledToFill() -> some View`

Scales this view to fill its parent.

`func scaledToFit() -> some View`

Scales this view to fit its parent.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(CGSize, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified factor.

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified size in each dimension.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> ModifiedContent<Self,
_UniformScaleEffect>`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

`func aspectRatio(CGFloat?, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the specified aspect ratio.

`func aspectRatio(CGSize, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the aspect ratio of the given size.

`func rotationEffect(Angle, anchor: UnitPoint) -> some View`

Rotates a view’s rendered output in two dimensions around the specified point.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some
View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some View`

Rotates the view’s content by the specified 3D rotation value.

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
some View`

Rotates the view’s content by an angle about an axis that you specify as a
rotation axis value.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> some View`

Rotates the view’s content by an angle about an axis that you specify as a
tuple of elements.

`func transformEffect(CGAffineTransform) -> some View`

Applies an affine transformation to this view’s rendered output.

`func transform3DEffect(AffineTransform3D) -> some View`

Applies a 3D transformation to the receiver.

`func projectionEffect(ProjectionTransform) -> some View`

Applies a projection transformation to this view’s rendered output.

`struct ProjectionTransform`

`enum ContentMode`

Constants that define how a view’s content fills the available space.

Instance Method

# imageScale(_:)

Scales images within the view according to one of the relative sizes available
including small, medium, and large images sizes.

iOS 13.0+  iPadOS 13.0+  macOS 11.0+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func imageScale(_ scale: Image.Scale) -> some View
    

##  Parameters

`scale`

    

One of the relative sizes provided by the image scale enumeration.

## Discussion

The example below shows the relative scaling effect. The system renders the
image at a relative size based on the available space and configuration
options of the image it is scaling.

## See Also

### Configuring an image

Fitting images into available space

Adjust the size and shape of images in your app’s user interface by applying
view modifiers.

`var imageScale: Image.Scale`

The image scale for this environment.

`enum Scale`

A scale to apply to vector images relative to text.

`enum Orientation`

The orientation of an image.

`enum ResizingMode`

The modes that SwiftUI uses to resize an image to fit within its containing
view.

Instance Method

# aspectRatio(_:contentMode:)

Constrains this view’s dimensions to the specified aspect ratio.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func aspectRatio(
        _ aspectRatio: CGFloat? = nil,
        contentMode: ContentMode
    ) -> some View
    

##  Parameters

`aspectRatio`

    

The ratio of width to height to use for the resulting view. Use `nil` to
maintain the current aspect ratio in the resulting view.

`contentMode`

    

A flag that indicates whether this view fits or fills the parent context.

## Return Value

A view that constrains this view’s dimensions to the aspect ratio of the given
size using `contentMode` as its scaling algorithm.

## Discussion

Use `aspectRatio(_:contentMode:)` to constrain a view’s dimensions to an
aspect ratio specified by a `CGFloat` using the specified content mode.

If this view is resizable, the resulting view will have `aspectRatio` as its
aspect ratio. In this example, the purple ellipse has a 3:4 width-to-height
ratio, and scales to fit its frame:

## See Also

### Scaling, rotating, or transforming a view

`func scaledToFill() -> some View`

Scales this view to fill its parent.

`func scaledToFit() -> some View`

Scales this view to fit its parent.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(CGSize, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified factor.

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified size in each dimension.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> ModifiedContent<Self,
_UniformScaleEffect>`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
some View`

Scales this view by the specified horizontal, vertical, and depth factors.

`func aspectRatio(CGSize, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the aspect ratio of the given size.

`func rotationEffect(Angle, anchor: UnitPoint) -> some View`

Rotates a view’s rendered output in two dimensions around the specified point.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some
View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some View`

Rotates the view’s content by the specified 3D rotation value.

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
some View`

Rotates the view’s content by an angle about an axis that you specify as a
rotation axis value.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> some View`

Rotates the view’s content by an angle about an axis that you specify as a
tuple of elements.

`func transformEffect(CGAffineTransform) -> some View`

Applies an affine transformation to this view’s rendered output.

`func transform3DEffect(AffineTransform3D) -> some View`

Applies a 3D transformation to the receiver.

`func projectionEffect(ProjectionTransform) -> some View`

Applies a projection transformation to this view’s rendered output.

`struct ProjectionTransform`

`enum ContentMode`

Constants that define how a view’s content fills the available space.

Instance Method

# aspectRatio(_:contentMode:)

Constrains this view’s dimensions to the aspect ratio of the given size.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func aspectRatio(
        _ aspectRatio: CGSize,
        contentMode: ContentMode
    ) -> some View
    

##  Parameters

`aspectRatio`

    

A size that specifies the ratio of width to height to use for the resulting
view.

`contentMode`

    

A flag indicating whether this view should fit or fill the parent context.

## Return Value

A view that constrains this view’s dimensions to `aspectRatio`, using
`contentMode` as its scaling algorithm.

## Discussion

Use `aspectRatio(_:contentMode:)` to constrain a view’s dimensions to an
aspect ratio specified by a `CGSize`.

If this view is resizable, the resulting view uses `aspectRatio` as its own
aspect ratio. In this example, the purple ellipse has a 3:4 width-to-height
ratio, and scales to fill its frame:

## See Also

### Scaling, rotating, or transforming a view

`func scaledToFill() -> some View`

Scales this view to fill its parent.

`func scaledToFit() -> some View`

Scales this view to fit its parent.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(CGSize, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified factor.

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified size in each dimension.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> ModifiedContent<Self,
_UniformScaleEffect>`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
some View`

Scales this view by the specified horizontal, vertical, and depth factors.

`func aspectRatio(CGFloat?, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the specified aspect ratio.

`func rotationEffect(Angle, anchor: UnitPoint) -> some View`

Rotates a view’s rendered output in two dimensions around the specified point.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some
View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some View`

Rotates the view’s content by the specified 3D rotation value.

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
some View`

Rotates the view’s content by an angle about an axis that you specify as a
rotation axis value.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> some View`

Rotates the view’s content by an angle about an axis that you specify as a
tuple of elements.

`func transformEffect(CGAffineTransform) -> some View`

Applies an affine transformation to this view’s rendered output.

`func transform3DEffect(AffineTransform3D) -> some View`

Applies a 3D transformation to the receiver.

`func projectionEffect(ProjectionTransform) -> some View`

Applies a projection transformation to this view’s rendered output.

`struct ProjectionTransform`

`enum ContentMode`

Constants that define how a view’s content fills the available space.

Instance Method

# rotationEffect(_:anchor:)

Rotates a view’s rendered output in two dimensions around the specified point.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func rotationEffect(
        _ angle: Angle,
        anchor: UnitPoint = .center
    ) -> some View
    

##  Parameters

`angle`

    

The angle by which to rotate the view.

`anchor`

    

A unit point within the view about which to perform the rotation. The default
value is `center`.

## Return Value

A view with rotated content.

## Discussion

This modifier rotates the view’s content around the axis that points out of
the xy-plane. It has no effect on the view’s frame. The following code rotates
text by 22˚ and then draws a border around the modified view to show that the
frame remains unchanged by the rotation modifier:

## See Also

### Scaling, rotating, or transforming a view

`func scaledToFill() -> some View`

Scales this view to fill its parent.

`func scaledToFit() -> some View`

Scales this view to fit its parent.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(CGSize, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified factor.

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified size in each dimension.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> ModifiedContent<Self,
_UniformScaleEffect>`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
some View`

Scales this view by the specified horizontal, vertical, and depth factors.

`func aspectRatio(CGFloat?, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the specified aspect ratio.

`func aspectRatio(CGSize, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the aspect ratio of the given size.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some
View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some View`

Rotates the view’s content by the specified 3D rotation value.

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
some View`

Rotates the view’s content by an angle about an axis that you specify as a
rotation axis value.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> some View`

Rotates the view’s content by an angle about an axis that you specify as a
tuple of elements.

`func transformEffect(CGAffineTransform) -> some View`

Applies an affine transformation to this view’s rendered output.

`func transform3DEffect(AffineTransform3D) -> some View`

Applies a 3D transformation to the receiver.

`func projectionEffect(ProjectionTransform) -> some View`

Applies a projection transformation to this view’s rendered output.

`struct ProjectionTransform`

`enum ContentMode`

Constants that define how a view’s content fills the available space.

Instance Method

# rotation3DEffect(_:anchor:)

Rotates the view’s content by the specified 3D rotation value.

visionOS 1.0+

    
    
    func rotation3DEffect(
        _ rotation: Rotation3D,
        anchor: UnitPoint3D = .center
    ) -> some View
    

##  Parameters

`rotation`

    

A rotation to apply to the view’s content.

`anchor`

    

The unit point within the view about which to perform the rotation. The
default value is `center`.

## Return Value

A view with rotated content.

## Discussion

This modifier rotates the view’s content without changing the view’s frame.
The following code displays a 3D model with a rotation of 45° about the y-axis
using the default anchor point at the center of the view:

## See Also

### Scaling, rotating, or transforming a view

`func scaledToFill() -> some View`

Scales this view to fill its parent.

`func scaledToFit() -> some View`

Scales this view to fit its parent.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(CGSize, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified factor.

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified size in each dimension.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> ModifiedContent<Self,
_UniformScaleEffect>`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
some View`

Scales this view by the specified horizontal, vertical, and depth factors.

`func aspectRatio(CGFloat?, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the specified aspect ratio.

`func aspectRatio(CGSize, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the aspect ratio of the given size.

`func rotationEffect(Angle, anchor: UnitPoint) -> some View`

Rotates a view’s rendered output in two dimensions around the specified point.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some
View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
some View`

Rotates the view’s content by an angle about an axis that you specify as a
rotation axis value.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> some View`

Rotates the view’s content by an angle about an axis that you specify as a
tuple of elements.

`func transformEffect(CGAffineTransform) -> some View`

Applies an affine transformation to this view’s rendered output.

`func transform3DEffect(AffineTransform3D) -> some View`

Applies a 3D transformation to the receiver.

`func projectionEffect(ProjectionTransform) -> some View`

Applies a projection transformation to this view’s rendered output.

`struct ProjectionTransform`

`enum ContentMode`

Constants that define how a view’s content fills the available space.

Instance Method

# rotation3DEffect(_:axis:anchor:anchorZ:perspective:)

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func rotation3DEffect(
        _ angle: Angle,
        axis: (x: CGFloat, y: CGFloat, z: CGFloat),
        anchor: UnitPoint = .center,
        anchorZ: CGFloat = 0,
        perspective: CGFloat = 1
    ) -> some View
    

##  Parameters

`angle`

    

The angle by which to rotate the view’s content.

`axis`

    

The axis of rotation, specified as a tuple with named elements for each of the
three spatial dimensions.

`anchor`

    

A two dimensional unit point within the view about which to perform the
rotation. The default value is `center`.

`anchorZ`

    

The location on the z-axis around which to rotate the content. The default is
`0`.

`perspective`

    

The relative vanishing point for the rotation. The default is `1`.

## Return Value

A view with rotated content.

## Discussion

Use this method to create the effect of rotating a view in three dimensions
around a specified axis of rotation. The modifier projects the rotated content
onto the original view’s plane. Use the `perspective` value to control the
renderer’s vanishing point. The following example creates the appearance of
rotating text 45˚ about the y-axis:

Important

In visionOS, create this effect with
`perspectiveRotationEffect(_:axis:anchor:anchorZ:perspective:)` instead. To
truly rotate a view in three dimensions, use a 3D rotation modifier without a
perspective input like `rotation3DEffect(_:axis:anchor:)`.

## See Also

### Scaling, rotating, or transforming a view

`func scaledToFill() -> some View`

Scales this view to fill its parent.

`func scaledToFit() -> some View`

Scales this view to fit its parent.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(CGSize, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified factor.

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified size in each dimension.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> ModifiedContent<Self,
_UniformScaleEffect>`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
some View`

Scales this view by the specified horizontal, vertical, and depth factors.

`func aspectRatio(CGFloat?, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the specified aspect ratio.

`func aspectRatio(CGSize, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the aspect ratio of the given size.

`func rotationEffect(Angle, anchor: UnitPoint) -> some View`

Rotates a view’s rendered output in two dimensions around the specified point.

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some
View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some View`

Rotates the view’s content by the specified 3D rotation value.

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
some View`

Rotates the view’s content by an angle about an axis that you specify as a
rotation axis value.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> some View`

Rotates the view’s content by an angle about an axis that you specify as a
tuple of elements.

`func transformEffect(CGAffineTransform) -> some View`

Applies an affine transformation to this view’s rendered output.

`func transform3DEffect(AffineTransform3D) -> some View`

Applies a 3D transformation to the receiver.

`func projectionEffect(ProjectionTransform) -> some View`

Applies a projection transformation to this view’s rendered output.

`struct ProjectionTransform`

`enum ContentMode`

Constants that define how a view’s content fills the available space.

Instance Method

# rotation3DEffect(_:axis:anchor:)

Rotates the view’s content by an angle about an axis that you specify as a
tuple of elements.

visionOS 1.0+

    
    
    func rotation3DEffect(
        _ angle: Angle,
        axis: (x: CGFloat, y: CGFloat, z: CGFloat),
        anchor: UnitPoint3D = .center
    ) -> some View
    

##  Parameters

`angle`

    

The angle by which to rotate the view’s content.

`axis`

    

The axis of rotation, specified as a tuple with named elements for each of the
three spatial dimensions.

`anchor`

    

The unit point within the view about which to perform the rotation. The
default value is `center`.

## Return Value

A view with rotated content.

## Discussion

This modifier rotates the view’s content without changing the view’s frame.
The following code displays a 3D model with a rotation of 45° about the y-axis
using the default anchor point at the center of the view:

## See Also

### Scaling, rotating, or transforming a view

`func scaledToFill() -> some View`

Scales this view to fill its parent.

`func scaledToFit() -> some View`

Scales this view to fit its parent.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(CGSize, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified factor.

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified size in each dimension.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> ModifiedContent<Self,
_UniformScaleEffect>`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
some View`

Scales this view by the specified horizontal, vertical, and depth factors.

`func aspectRatio(CGFloat?, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the specified aspect ratio.

`func aspectRatio(CGSize, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the aspect ratio of the given size.

`func rotationEffect(Angle, anchor: UnitPoint) -> some View`

Rotates a view’s rendered output in two dimensions around the specified point.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some
View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some View`

Rotates the view’s content by the specified 3D rotation value.

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
some View`

Rotates the view’s content by an angle about an axis that you specify as a
rotation axis value.

`func transformEffect(CGAffineTransform) -> some View`

Applies an affine transformation to this view’s rendered output.

`func transform3DEffect(AffineTransform3D) -> some View`

Applies a 3D transformation to the receiver.

`func projectionEffect(ProjectionTransform) -> some View`

Applies a projection transformation to this view’s rendered output.

`struct ProjectionTransform`

`enum ContentMode`

Constants that define how a view’s content fills the available space.

Instance Method

# rotation3DEffect(_:axis:anchor:)

Rotates the view’s content by an angle about an axis that you specify as a
rotation axis value.

visionOS 1.0+

    
    
    func rotation3DEffect(
        _ angle: Angle,
        axis: RotationAxis3D,
        anchor: UnitPoint3D = .center
    ) -> some View
    

##  Parameters

`angle`

    

The angle by which to rotate the view’s content.

`axis`

    

The axis of rotation.

`anchor`

    

The unit point within the view about which to perform the rotation. The
default value is `center`.

## Return Value

A view with rotated content.

## Discussion

This modifier rotates the view’s content without changing the view’s frame.
The following code displays a 3D model with a rotation of 45° about the y-axis
using the default anchor point at the center of the view:

## See Also

### Scaling, rotating, or transforming a view

`func scaledToFill() -> some View`

Scales this view to fill its parent.

`func scaledToFit() -> some View`

Scales this view to fit its parent.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(CGSize, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified factor.

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified size in each dimension.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> ModifiedContent<Self,
_UniformScaleEffect>`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
some View`

Scales this view by the specified horizontal, vertical, and depth factors.

`func aspectRatio(CGFloat?, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the specified aspect ratio.

`func aspectRatio(CGSize, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the aspect ratio of the given size.

`func rotationEffect(Angle, anchor: UnitPoint) -> some View`

Rotates a view’s rendered output in two dimensions around the specified point.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some
View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some View`

Rotates the view’s content by the specified 3D rotation value.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> some View`

Rotates the view’s content by an angle about an axis that you specify as a
tuple of elements.

`func transformEffect(CGAffineTransform) -> some View`

Applies an affine transformation to this view’s rendered output.

`func transform3DEffect(AffineTransform3D) -> some View`

Applies a 3D transformation to the receiver.

`func projectionEffect(ProjectionTransform) -> some View`

Applies a projection transformation to this view’s rendered output.

`struct ProjectionTransform`

`enum ContentMode`

Constants that define how a view’s content fills the available space.

Instance Method

# perspectiveRotationEffect(_:axis:anchor:anchorZ:perspective:)

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

visionOS 1.0+

    
    
    func perspectiveRotationEffect(
        _ angle: Angle,
        axis: (x: CGFloat, y: CGFloat, z: CGFloat),
        anchor: UnitPoint = .center,
        anchorZ: CGFloat = 0,
        perspective: CGFloat = 1
    ) -> some View
    

##  Parameters

`angle`

    

The angle by which to rotate the view’s content.

`axis`

    

The axis of rotation, specified as a tuple with named elements for each of the
three spatial dimensions.

`anchor`

    

A two dimensional unit point within the view about which to perform the
rotation. The default value is `center`.

`anchorZ`

    

The location on the z-axis around which to rotate the content. The default is
`0`.

`perspective`

    

The relative vanishing point for the rotation. The default is `1`.

## Return Value

A view with rotated content.

## Discussion

Use this method to create the effect of rotating a view in three dimensions
around a specified axis of rotation. The modifier projects the rotated, two-
dimensional content onto the original view’s plane. Use the `perspective`
input to control the renderer’s vanishing point. The following example creates
the appearance of rotating text 45˚ about the y-axis:

Important

To truly rotate a view in three dimensions, use a 3D rotation modifier without
a perspective input like `rotation3DEffect(_:axis:anchor:)`.

## See Also

### Scaling, rotating, or transforming a view

`func scaledToFill() -> some View`

Scales this view to fill its parent.

`func scaledToFit() -> some View`

Scales this view to fit its parent.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(CGSize, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified factor.

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified size in each dimension.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> ModifiedContent<Self,
_UniformScaleEffect>`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
some View`

Scales this view by the specified horizontal, vertical, and depth factors.

`func aspectRatio(CGFloat?, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the specified aspect ratio.

`func aspectRatio(CGSize, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the aspect ratio of the given size.

`func rotationEffect(Angle, anchor: UnitPoint) -> some View`

Rotates a view’s rendered output in two dimensions around the specified point.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some View`

Rotates the view’s content by the specified 3D rotation value.

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
some View`

Rotates the view’s content by an angle about an axis that you specify as a
rotation axis value.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> some View`

Rotates the view’s content by an angle about an axis that you specify as a
tuple of elements.

`func transformEffect(CGAffineTransform) -> some View`

Applies an affine transformation to this view’s rendered output.

`func transform3DEffect(AffineTransform3D) -> some View`

Applies a 3D transformation to the receiver.

`func projectionEffect(ProjectionTransform) -> some View`

Applies a projection transformation to this view’s rendered output.

`struct ProjectionTransform`

`enum ContentMode`

Constants that define how a view’s content fills the available space.

Instance Method

# projectionEffect(_:)

Applies a projection transformation to this view’s rendered output.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func projectionEffect(_ transform: ProjectionTransform) -> some View
    

##  Parameters

`transform`

    

A `ProjectionTransform` to apply to the view.

## Discussion

Use `projectionEffect(_:)` to apply a 3D transformation to the view.

The example below rotates the text 30˚ around the `z` axis, which is the axis
pointing out of the screen:

## See Also

### Scaling, rotating, or transforming a view

`func scaledToFill() -> some View`

Scales this view to fill its parent.

`func scaledToFit() -> some View`

Scales this view to fit its parent.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(CGSize, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified factor.

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified size in each dimension.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> ModifiedContent<Self,
_UniformScaleEffect>`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
some View`

Scales this view by the specified horizontal, vertical, and depth factors.

`func aspectRatio(CGFloat?, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the specified aspect ratio.

`func aspectRatio(CGSize, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the aspect ratio of the given size.

`func rotationEffect(Angle, anchor: UnitPoint) -> some View`

Rotates a view’s rendered output in two dimensions around the specified point.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some
View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some View`

Rotates the view’s content by the specified 3D rotation value.

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
some View`

Rotates the view’s content by an angle about an axis that you specify as a
rotation axis value.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> some View`

Rotates the view’s content by an angle about an axis that you specify as a
tuple of elements.

`func transformEffect(CGAffineTransform) -> some View`

Applies an affine transformation to this view’s rendered output.

`func transform3DEffect(AffineTransform3D) -> some View`

Applies a 3D transformation to the receiver.

`struct ProjectionTransform`

`enum ContentMode`

Constants that define how a view’s content fills the available space.

Instance Method

# transformEffect(_:)

Applies an affine transformation to this view’s rendered output.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func transformEffect(_ transform: CGAffineTransform) -> some View
    

##  Parameters

`transform`

    

A `CGAffineTransform` to apply to the view.

## Discussion

Use `transformEffect(_:)` to rotate, scale, translate, or skew the output of
the view according to the provided `CGAffineTransform`.

In the example below, the text is rotated at -30˚ on the `y` axis.

## See Also

### Scaling, rotating, or transforming a view

`func scaledToFill() -> some View`

Scales this view to fill its parent.

`func scaledToFit() -> some View`

Scales this view to fit its parent.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(CGSize, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified factor.

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified size in each dimension.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> ModifiedContent<Self,
_UniformScaleEffect>`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
some View`

Scales this view by the specified horizontal, vertical, and depth factors.

`func aspectRatio(CGFloat?, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the specified aspect ratio.

`func aspectRatio(CGSize, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the aspect ratio of the given size.

`func rotationEffect(Angle, anchor: UnitPoint) -> some View`

Rotates a view’s rendered output in two dimensions around the specified point.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some
View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some View`

Rotates the view’s content by the specified 3D rotation value.

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
some View`

Rotates the view’s content by an angle about an axis that you specify as a
rotation axis value.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> some View`

Rotates the view’s content by an angle about an axis that you specify as a
tuple of elements.

`func transform3DEffect(AffineTransform3D) -> some View`

Applies a 3D transformation to the receiver.

`func projectionEffect(ProjectionTransform) -> some View`

Applies a projection transformation to this view’s rendered output.

`struct ProjectionTransform`

`enum ContentMode`

Constants that define how a view’s content fills the available space.

Instance Method

# transform3DEffect(_:)

Applies a 3D transformation to the receiver.

visionOS 1.0+

    
    
    func transform3DEffect(_ transform: AffineTransform3D) -> some View
    

##  Parameters

`transform`

    

The 3D transformation to apply to the view, interpreting it as a 3D plane in
space.

## Return Value

A view that renders transformed according to the provided `transform`

## See Also

### Scaling, rotating, or transforming a view

`func scaledToFill() -> some View`

Scales this view to fill its parent.

`func scaledToFit() -> some View`

Scales this view to fit its parent.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(CGSize, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified factor.

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified size in each dimension.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> ModifiedContent<Self,
_UniformScaleEffect>`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
some View`

Scales this view by the specified horizontal, vertical, and depth factors.

`func aspectRatio(CGFloat?, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the specified aspect ratio.

`func aspectRatio(CGSize, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the aspect ratio of the given size.

`func rotationEffect(Angle, anchor: UnitPoint) -> some View`

Rotates a view’s rendered output in two dimensions around the specified point.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some
View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some View`

Rotates the view’s content by the specified 3D rotation value.

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
some View`

Rotates the view’s content by an angle about an axis that you specify as a
rotation axis value.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> some View`

Rotates the view’s content by an angle about an axis that you specify as a
tuple of elements.

`func transformEffect(CGAffineTransform) -> some View`

Applies an affine transformation to this view’s rendered output.

`func projectionEffect(ProjectionTransform) -> some View`

Applies a projection transformation to this view’s rendered output.

`struct ProjectionTransform`

`enum ContentMode`

Constants that define how a view’s content fills the available space.

Instance Method

# blur(radius:opaque:)

Applies a Gaussian blur to this view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func blur(
        radius: CGFloat,
        opaque: Bool = false
    ) -> some View
    

##  Parameters

`radius`

    

The radial size of the blur. A blur is more diffuse when its radius is large.

`opaque`

    

A Boolean value that indicates whether the blur renderer permits transparency
in the blur output. Set to `true` to create an opaque blur, or set to `false`
to permit transparency.

## Discussion

Use `blur(radius:opaque:)` to apply a gaussian blur effect to the rendering of
this view.

The example below shows two `Text` views, the first with no blur effects, the
second with `blur(radius:opaque:)` applied with the `radius` set to `2`. The
larger the radius, the more diffuse the effect.

## See Also

### Applying blur and shadows

`func shadow(color: Color, radius: CGFloat, x: CGFloat, y: CGFloat) -> some
View`

Adds a shadow to this view.

`struct ColorMatrix`

A matrix to use in an RGBA color transformation.

Instance Method

# opacity(_:)

Sets the transparency of this view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func opacity(_ opacity: Double) -> some View
    

##  Parameters

`opacity`

    

A value between 0 (fully transparent) and 1 (fully opaque).

## Return Value

A view that sets the transparency of this view.

## Discussion

Apply opacity to reveal views that are behind another view or to de-emphasize
a view.

When applying the `opacity(_:)` modifier to a view that has already had its
opacity transformed, the modifier multiplies the effect of the underlying
opacity transformation.

The example below shows yellow and red rectangles configured to overlap. The
top yellow rectangle has its opacity set to 50%, allowing the occluded portion
of the bottom rectangle to be visible:

## See Also

### Hiding views

`func hidden() -> some View`

Hides this view unconditionally.

Instance Method

# brightness(_:)

Brightens this view by the specified amount.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func brightness(_ amount: Double) -> some View
    

##  Parameters

`amount`

    

A value between 0 (no effect) and 1 (full white brightening) that represents
the intensity of the brightness effect.

## Return Value

A view that brightens this view by the specified amount.

## Discussion

Use `brightness(_:)` to brighten the intensity of the colors in a view. The
example below shows a series of red squares, with their brightness increasing
from 0 (fully red) to 100% (white) in 20% increments.

## See Also

### Transforming colors

`func contrast(Double) -> some View`

Sets the contrast and separation between similar colors in this view.

`func colorInvert() -> some View`

Inverts the colors in this view.

`func colorMultiply(Color) -> some View`

Adds a color multiplication effect to this view.

`func saturation(Double) -> some View`

Adjusts the color saturation of this view.

`func grayscale(Double) -> some View`

Adds a grayscale effect to this view.

`func hueRotation(Angle) -> some View`

Applies a hue rotation effect to this view.

`func luminanceToAlpha() -> some View`

Adds a luminance to alpha effect to this view.

Instance Method

# contrast(_:)

Sets the contrast and separation between similar colors in this view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func contrast(_ amount: Double) -> some View
    

##  Parameters

`amount`

    

The intensity of color contrast to apply. negative values invert colors in
addition to applying contrast.

## Return Value

A view that applies color contrast to this view.

## Discussion

Apply contrast to a view to increase or decrease the separation between
similar colors in the view.

In the example below, the `contrast(_:)` modifier is applied to a set of red
squares each containing a contrasting green inner circle. At each step in the
loop, the `contrast(_:)` modifier changes the contrast of the circle/square
view in 20% increments. This ranges from -20% contrast (yielding inverted
colors — turning the red square to pale-green and the green circle to mauve),
to neutral-gray at 0%, to 100% contrast (bright-red square / bright-green
circle). Applying negative contrast values, as shown in the -20% square, will
apply contrast in addition to inverting colors.

## See Also

### Transforming colors

`func brightness(Double) -> some View`

Brightens this view by the specified amount.

`func colorInvert() -> some View`

Inverts the colors in this view.

`func colorMultiply(Color) -> some View`

Adds a color multiplication effect to this view.

`func saturation(Double) -> some View`

Adjusts the color saturation of this view.

`func grayscale(Double) -> some View`

Adds a grayscale effect to this view.

`func hueRotation(Angle) -> some View`

Applies a hue rotation effect to this view.

`func luminanceToAlpha() -> some View`

Adds a luminance to alpha effect to this view.

Instance Method

# colorInvert()

Inverts the colors in this view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func colorInvert() -> some View
    

## Return Value

A view that inverts its colors.

## Discussion

The `colorInvert()` modifier inverts all of the colors in a view so that each
color displays as its complementary color. For example, blue converts to
yellow, and white converts to black.

In the example below, two red squares each have an interior green circle. The
inverted square shows the effect of the square’s colors: complimentary colors
for red and green — teal and purple.

## See Also

### Transforming colors

`func brightness(Double) -> some View`

Brightens this view by the specified amount.

`func contrast(Double) -> some View`

Sets the contrast and separation between similar colors in this view.

`func colorMultiply(Color) -> some View`

Adds a color multiplication effect to this view.

`func saturation(Double) -> some View`

Adjusts the color saturation of this view.

`func grayscale(Double) -> some View`

Adds a grayscale effect to this view.

`func hueRotation(Angle) -> some View`

Applies a hue rotation effect to this view.

`func luminanceToAlpha() -> some View`

Adds a luminance to alpha effect to this view.

Instance Method

# colorMultiply(_:)

Adds a color multiplication effect to this view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func colorMultiply(_ color: Color) -> some View
    

##  Parameters

`color`

    

The color to bias this view toward.

## Return Value

A view with a color multiplication effect.

## Discussion

The following example shows two versions of the same image side by side; at
left is the original, and at right is a duplicate with the `colorMultiply(_:)`
modifier applied with `purple`.

## See Also

### Transforming colors

`func brightness(Double) -> some View`

Brightens this view by the specified amount.

`func contrast(Double) -> some View`

Sets the contrast and separation between similar colors in this view.

`func colorInvert() -> some View`

Inverts the colors in this view.

`func saturation(Double) -> some View`

Adjusts the color saturation of this view.

`func grayscale(Double) -> some View`

Adds a grayscale effect to this view.

`func hueRotation(Angle) -> some View`

Applies a hue rotation effect to this view.

`func luminanceToAlpha() -> some View`

Adds a luminance to alpha effect to this view.

Instance Method

# saturation(_:)

Adjusts the color saturation of this view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func saturation(_ amount: Double) -> some View
    

##  Parameters

`amount`

    

The amount of saturation to apply to this view.

## Return Value

A view that adjusts the saturation of this view.

## Discussion

Use color saturation to increase or decrease the intensity of colors in a
view.

The example below shows a series of red squares with their saturation
increasing from 0 (gray) to 100% (fully-red) in 20% increments:

See Also

`contrast(_:)`

## See Also

### Transforming colors

`func brightness(Double) -> some View`

Brightens this view by the specified amount.

`func contrast(Double) -> some View`

Sets the contrast and separation between similar colors in this view.

`func colorInvert() -> some View`

Inverts the colors in this view.

`func colorMultiply(Color) -> some View`

Adds a color multiplication effect to this view.

`func grayscale(Double) -> some View`

Adds a grayscale effect to this view.

`func hueRotation(Angle) -> some View`

Applies a hue rotation effect to this view.

`func luminanceToAlpha() -> some View`

Adds a luminance to alpha effect to this view.

Instance Method

# grayscale(_:)

Adds a grayscale effect to this view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func grayscale(_ amount: Double) -> some View
    

##  Parameters

`amount`

    

The intensity of grayscale to apply from 0.0 to less than 1.0. Values closer
to 0.0 are more colorful, and values closer to 1.0 are less colorful.

## Return Value

A view that adds a grayscale effect to this view.

## Discussion

A grayscale effect reduces the intensity of colors in this view.

The example below shows a series of red squares with their grayscale effect
increasing from 0 (reddest) to 99% (fully desaturated) in approximate 20%
increments:

## See Also

### Transforming colors

`func brightness(Double) -> some View`

Brightens this view by the specified amount.

`func contrast(Double) -> some View`

Sets the contrast and separation between similar colors in this view.

`func colorInvert() -> some View`

Inverts the colors in this view.

`func colorMultiply(Color) -> some View`

Adds a color multiplication effect to this view.

`func saturation(Double) -> some View`

Adjusts the color saturation of this view.

`func hueRotation(Angle) -> some View`

Applies a hue rotation effect to this view.

`func luminanceToAlpha() -> some View`

Adds a luminance to alpha effect to this view.

Instance Method

# hueRotation(_:)

Applies a hue rotation effect to this view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func hueRotation(_ angle: Angle) -> some View
    

##  Parameters

`angle`

    

The hue rotation angle to apply to the colors in this view.

## Return Value

A view that applies a hue rotation effect to this view.

## Discussion

Use hue rotation effect to shift all of the colors in a view according to the
angle you specify.

The example below shows a series of squares filled with a linear gradient.
Each square shows the effect of a 36˚ hueRotation (a total of 180˚ across the
5 squares) on the gradient:

## See Also

### Transforming colors

`func brightness(Double) -> some View`

Brightens this view by the specified amount.

`func contrast(Double) -> some View`

Sets the contrast and separation between similar colors in this view.

`func colorInvert() -> some View`

Inverts the colors in this view.

`func colorMultiply(Color) -> some View`

Adds a color multiplication effect to this view.

`func saturation(Double) -> some View`

Adjusts the color saturation of this view.

`func grayscale(Double) -> some View`

Adds a grayscale effect to this view.

`func luminanceToAlpha() -> some View`

Adds a luminance to alpha effect to this view.

Instance Method

# luminanceToAlpha()

Adds a luminance to alpha effect to this view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func luminanceToAlpha() -> some View
    

## Return Value

A view with the luminance to alpha effect applied.

## Discussion

Use this modifier to create a semitransparent mask, with the opacity of each
part of the modified view controlled by the luminance of the corresponding
part of the original view. Regions of lower luminance become more transparent,
while higher luminance yields greater opacity.

In particular, the modifier maps the red, green, and blue components of each
input pixel’s color to a grayscale value, and that value becomes the alpha
component of a black pixel in the output. This modifier produces an effect
that’s equivalent to using the `feColorMatrix` filter primitive with the
`luminanceToAlpha` type attribute, as defined by the Scalable Vector Graphics
(SVG) 2 specification.

The example below defines a `Palette` view as a series of rectangles, each
composed as a `Color` with a particular white value, and then displays two
versions of the palette over a blue background:

The unmodified version of the palette contains rectangles that range from
solid black to solid white, thus with increasing luminance. The second version
of the palette, which has the `luminanceToAlpha()` modifier applied, allows
the background to show through in an amount that corresponds inversely to the
luminance of the input.

## See Also

### Transforming colors

`func brightness(Double) -> some View`

Brightens this view by the specified amount.

`func contrast(Double) -> some View`

Sets the contrast and separation between similar colors in this view.

`func colorInvert() -> some View`

Inverts the colors in this view.

`func colorMultiply(Color) -> some View`

Adds a color multiplication effect to this view.

`func saturation(Double) -> some View`

Adjusts the color saturation of this view.

`func grayscale(Double) -> some View`

Adds a grayscale effect to this view.

`func hueRotation(Angle) -> some View`

Applies a hue rotation effect to this view.

Instance Method

# shadow(color:radius:x:y:)

Adds a shadow to this view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func shadow(
        color: Color = Color(.sRGBLinear, white: 0, opacity: 0.33),
        radius: CGFloat,
        x: CGFloat = 0,
        y: CGFloat = 0
    ) -> some View
    

##  Parameters

`color`

    

The shadow’s color.

`radius`

    

A measure of how much to blur the shadow. Larger values result in more blur.

`x`

    

An amount to offset the shadow horizontally from the view.

`y`

    

An amount to offset the shadow vertically from the view.

## Return Value

A view that adds a shadow to this view.

## Discussion

Use this modifier to add a shadow of a specified color behind a view. You can
offset the shadow from its view independently in the horizontal and vertical
dimensions using the `x` and `y` parameters. You can also blur the edges of
the shadow using the `radius` parameter. Use a radius of zero to create a
sharp shadow. Larger radius values produce softer shadows.

The example below creates a grid of boxes with varying offsets and blur. Each
box displays its radius and offset values for reference.

The example above uses `primary` as the color to make the shadow easy to see
for the purpose of illustration. In practice, you might prefer something more
subtle, like `gray`. If you don’t specify a color, the method uses a semi-
transparent black.

## See Also

### Applying blur and shadows

`func blur(radius: CGFloat, opaque: Bool) -> some View`

Applies a Gaussian blur to this view.

`struct ColorMatrix`

A matrix to use in an RGBA color transformation.

Instance Method

# visualEffect(_:)

Applies effects to this view, while providing access to layout information
through a geometry proxy.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func visualEffect(_ effect: @escaping (EmptyVisualEffect, GeometryProxy) -> some VisualEffect) -> some View
    

##  Parameters

`effect`

    

A closure that returns the effect to be applied. The first argument provided
to the closure is a placeholder representing this view. The second argument is
a `GeometryProxy`.

## Return Value

A view with the effect applied.

## Discussion

You return new effects by calling functions on the first argument provided to
the `effect` closure. In this example, `ContentView` is offset by its own
size, causing its top left corner to appear where the bottom right corner was
originally located:

## See Also

### Applying effects based on geometry

`func visualEffect3D((EmptyVisualEffect, GeometryProxy3D) -> some
VisualEffect) -> some View`

Applies effects to this view, while providing access to layout information
through a 3D geometry proxy.

`protocol VisualEffect`

Visual Effects change the visual appearance of a view without changing its
ancestors or descendents.

`struct EmptyVisualEffect`

The base visual effect that you apply additional effect to.

Instance Method

# visualEffect3D(_:)

Applies effects to this view, while providing access to layout information
through a 3D geometry proxy.

visionOS 1.0+

    
    
    func visualEffect3D(_ effect: @escaping (EmptyVisualEffect, GeometryProxy3D) -> some VisualEffect) -> some View
    

##  Parameters

`effect`

    

A closure that returns the effect to be applied. The first argument provided
to the closure is a placeholder representing this view. The second argument is
a `GeometryProxy3D`.

## Return Value

A view with the effect applied.

## Discussion

You return new effects by calling functions on the first argument provided to
the `effect` closure. In this example, `ContentView` is offset in Z by its own
depth, causing its back face to appear where the front face of the view was
originally located:

## See Also

### Applying effects based on geometry

`func visualEffect((EmptyVisualEffect, GeometryProxy) -> some VisualEffect) ->
some View`

Applies effects to this view, while providing access to layout information
through a geometry proxy.

`protocol VisualEffect`

Visual Effects change the visual appearance of a view without changing its
ancestors or descendents.

`struct EmptyVisualEffect`

The base visual effect that you apply additional effect to.

Instance Method

# colorEffect(_:isEnabled:)

Returns a new view that applies `shader` to `self` as a filter effect on the
color of each pixel.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    func colorEffect(
        _ shader: Shader,
        isEnabled: Bool = true
    ) -> some View
    

##  Parameters

`shader`

    

The shader to apply to `self` as a color filter.

`isEnabled`

    

Whether the effect is enabled or not.

## Return Value

A new view that renders `self` with the shader applied as a color filter.

## Discussion

For a shader function to act as a color filter it must have a function
signature matching:

where `position` is the user-space coordinates of the pixel applied to the
shader and `color` its source color, as a pre-multiplied color in the
destination color space. `args...` should be compatible with the uniform
arguments bound to `shader`. The function should return the modified color
value.

Important

Views backed by AppKit or UIKit views may not render into the filtered layer.
Instead, they log a warning and display a placeholder image to highlight the
error.

## See Also

### Accessing Metal shaders

`func distortionEffect(Shader, maxSampleOffset: CGSize, isEnabled: Bool) ->
some View`

Returns a new view that applies `shader` to `self` as a geometric distortion
effect on the location of each pixel.

`func layerEffect(Shader, maxSampleOffset: CGSize, isEnabled: Bool) -> some
View`

Returns a new view that applies `shader` to `self` as a filter on the raster
layer created from `self`.

`struct Shader`

A reference to a function in a Metal shader library, along with its bound
uniform argument values.

`struct ShaderFunction`

A reference to a function in a Metal shader library.

`struct ShaderLibrary`

A Metal shader library.

Instance Method

# distortionEffect(_:maxSampleOffset:isEnabled:)

Returns a new view that applies `shader` to `self` as a geometric distortion
effect on the location of each pixel.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    func distortionEffect(
        _ shader: Shader,
        maxSampleOffset: CGSize,
        isEnabled: Bool = true
    ) -> some View
    

##  Parameters

`shader`

    

The shader to apply as a distortion effect.

`maxSampleOffset`

    

The maximum distance in each axis between the returned source pixel position
and the destination pixel position, for all source pixels.

`isEnabled`

    

Whether the effect is enabled or not.

## Return Value

A new view that renders `self` with the shader applied as a distortion effect.

## Discussion

For a shader function to act as a distortion effect it must have a function
signature matching:

where `position` is the user-space coordinates of the destination pixel
applied to the shader. `args...` should be compatible with the uniform
arguments bound to `shader`. The function should return the user-space
coordinates of the corresponding source pixel.

Important

Views backed by AppKit or UIKit views may not render into the filtered layer.
Instead, they log a warning and display a placeholder image to highlight the
error.

## See Also

### Accessing Metal shaders

`func colorEffect(Shader, isEnabled: Bool) -> some View`

Returns a new view that applies `shader` to `self` as a filter effect on the
color of each pixel.

`func layerEffect(Shader, maxSampleOffset: CGSize, isEnabled: Bool) -> some
View`

Returns a new view that applies `shader` to `self` as a filter on the raster
layer created from `self`.

`struct Shader`

A reference to a function in a Metal shader library, along with its bound
uniform argument values.

`struct ShaderFunction`

A reference to a function in a Metal shader library.

`struct ShaderLibrary`

A Metal shader library.

Instance Method

# layerEffect(_:maxSampleOffset:isEnabled:)

Returns a new view that applies `shader` to `self` as a filter on the raster
layer created from `self`.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    func layerEffect(
        _ shader: Shader,
        maxSampleOffset: CGSize,
        isEnabled: Bool = true
    ) -> some View
    

##  Parameters

`shader`

    

The shader to apply as a layer effect.

`maxSampleOffset`

    

If the shader function samples from the layer at locations not equal to the
destination position, this value must specify the maximum sampling distance in
each axis, for all source pixels.

`isEnabled`

    

Whether the effect is enabled or not.

## Return Value

A new view that renders `self` with the shader applied as a distortion effect.

## Discussion

For a shader function to act as a layer effect it must have a function
signature matching:

where `position` is the user-space coordinates of the destination pixel
applied to the shader, and `layer` is a subregion of the rasterized contents
of `self`. `args...` should be compatible with the uniform arguments bound to
`shader`.

The `SwiftUI::Layer` type is defined in the `<SwiftUI/SwiftUI.h>` header file.
It exports a single `sample()` function that returns a linearly-filtered pixel
value from a position in the source content, as a premultiplied RGBA pixel
value:

The function should return the color mapping to the destination pixel,
typically by sampling one or more pixels from `layer` at location(s) derived
from `position` and them applying some kind of transformation to produce a new
color.

Important

Views backed by AppKit or UIKit views may not render into the filtered layer.
Instead, they log a warning and display a placeholder image to highlight the
error.

## See Also

### Accessing Metal shaders

`func colorEffect(Shader, isEnabled: Bool) -> some View`

Returns a new view that applies `shader` to `self` as a filter effect on the
color of each pixel.

`func distortionEffect(Shader, maxSampleOffset: CGSize, isEnabled: Bool) ->
some View`

Returns a new view that applies `shader` to `self` as a geometric distortion
effect on the location of each pixel.

`struct Shader`

A reference to a function in a Metal shader library, along with its bound
uniform argument values.

`struct ShaderFunction`

A reference to a function in a Metal shader library.

`struct ShaderLibrary`

A Metal shader library.

Instance Method

# blendMode(_:)

Sets the blend mode for compositing this view with overlapping views.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func blendMode(_ blendMode: BlendMode) -> some View
    

##  Parameters

`blendMode`

    

The `BlendMode` for compositing this view.

## Return Value

A view that applies `blendMode` to this view.

## Discussion

Use `blendMode(_:)` to combine overlapping views and use a different visual
effect to produce the result. The `BlendMode` enumeration defines many
possible effects.

In the example below, the two overlapping rectangles have a
`BlendMode.colorBurn` effect applied, which effectively removes the non-
overlapping portion of the second image:

## See Also

### Compositing views

`func compositingGroup() -> some View`

Wraps this view in a compositing group.

`func drawingGroup(opaque: Bool, colorMode: ColorRenderingMode) -> some View`

Composites this view’s contents into an offscreen image before final display.

`enum BlendMode`

Modes for compositing a view with overlapping content.

`enum ColorRenderingMode`

The set of possible working color spaces for color-compositing operations.

Instance Method

# compositingGroup()

Wraps this view in a compositing group.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func compositingGroup() -> some View
    

## Return Value

A view that wraps this view in a compositing group.

## Discussion

A compositing group makes compositing effects in this view’s ancestor views,
such as opacity and the blend mode, take effect before this view is rendered.

Use `compositingGroup()` to apply effects to a parent view before applying
effects to this view.

In the example below the `compositingGroup()` modifier separates the
application of effects into stages. It applies the `opacity(_:)` effect to the
VStack before the `blur(radius:)` effect is applied to the views inside the
enclosed `ZStack`. This limits the scope of the opacity change to the
outermost view.

## See Also

### Compositing views

`func blendMode(BlendMode) -> some View`

Sets the blend mode for compositing this view with overlapping views.

`func drawingGroup(opaque: Bool, colorMode: ColorRenderingMode) -> some View`

Composites this view’s contents into an offscreen image before final display.

`enum BlendMode`

Modes for compositing a view with overlapping content.

`enum ColorRenderingMode`

The set of possible working color spaces for color-compositing operations.

Instance Method

# drawingGroup(opaque:colorMode:)

Composites this view’s contents into an offscreen image before final display.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func drawingGroup(
        opaque: Bool = false,
        colorMode: ColorRenderingMode = .nonLinear
    ) -> some View
    

##  Parameters

`opaque`

    

A Boolean value that indicates whether the image is opaque. The default is
`false`; if set to `true`, the alpha channel of the image must be `1`.

`colorMode`

    

One of the working color space and storage formats defined in
`ColorRenderingMode`. The default is `ColorRenderingMode.nonLinear`.

## Return Value

A view that composites this view’s contents into an offscreen image before
display.

## Discussion

The `drawingGroup(opaque:colorMode:)` modifier flattens a subtree of views
into a single view before rendering it.

In the example below, the contents of the view are composited to a single
bitmap; the bitmap is then displayed in place of the view:

Note

Views backed by native platform views may not render into the image. Instead,
they log a warning and display a placeholder image to highlight the error.

## See Also

### Compositing views

`func blendMode(BlendMode) -> some View`

Sets the blend mode for compositing this view with overlapping views.

`func compositingGroup() -> some View`

Wraps this view in a compositing group.

`enum BlendMode`

Modes for compositing a view with overlapping content.

`enum ColorRenderingMode`

The set of possible working color spaces for color-compositing operations.

Instance Method

# animation(_:)

Applies the given animation to this view when this view changes.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func animation(_ animation: Animation?) -> some View
    

Available when `Self` conforms to `Equatable`.

##  Parameters

`animation`

    

The animation to apply. If `animation` is `nil`, the view doesn’t animate.

## Return Value

A view that applies `animation` to this view whenever it changes.

## See Also

### Adding state-based animation to a view

`func animation<V>(Animation?, value: V) -> some View`

Applies the given animation to this view when the specified value changes.

`func animation<V>(Animation?, body: (PlaceholderContentView<Self>) -> V) ->
some View`

Applies the given animation to all animatable values within the `body`
closure.

Instance Method

# animation(_:value:)

Applies the given animation to this view when the specified value changes.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func animation<V>(
        _ animation: Animation?,
        value: V
    ) -> some View where V : Equatable
    

##  Parameters

`animation`

    

The animation to apply. If `animation` is `nil`, the view doesn’t animate.

`value`

    

A value to monitor for changes.

## Return Value

A view that applies `animation` to this view whenever `value` changes.

## See Also

### Adding state-based animation to a view

`func animation(Animation?) -> some View`

Applies the given animation to this view when this view changes.

Available when `Self` conforms to `Equatable`.

`func animation<V>(Animation?, body: (PlaceholderContentView<Self>) -> V) ->
some View`

Applies the given animation to all animatable values within the `body`
closure.

Instance Method

# animation(_:body:)

Applies the given animation to all animatable values within the `body`
closure.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func animation<V>(
        _ animation: Animation?,
        @ViewBuilder body: (PlaceholderContentView<Self>) -> V
    ) -> some View where V : View
    

## Discussion

Any modifiers applied to the content of `body` will be applied to this view,
and the `animation` will only be used on the modifiers defined in the `body`.

The following code animates the opacity changing with an easeInOut animation,
while the contents of MyView are animated with the implicit transaction’s
animation:

## See Also

### Adding state-based animation to a view

`func animation(Animation?) -> some View`

Applies the given animation to this view when this view changes.

Available when `Self` conforms to `Equatable`.

`func animation<V>(Animation?, value: V) -> some View`

Applies the given animation to this view when the specified value changes.

Instance Method

# keyframeAnimator(initialValue:repeating:content:keyframes:)

Loops the given keyframes continuously, updating the view using the modifiers
you apply in `body`.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func keyframeAnimator<Value>(
        initialValue: Value,
        repeating: Bool = true,
        @ViewBuilder content: @escaping (PlaceholderContentView<Self>, Value) -> some View,
        @KeyframesBuilder<Value> keyframes: @escaping (Value) -> some Keyframes
    ) -> some View
    

##  Parameters

`initialValue`

    

The initial value that the keyframes will animate from.

`repeating`

    

Whether the keyframes are currently repeating. If false, the value at the
beginning of the keyframe timeline will be provided to the content closure.

`content`

    

A view builder closure that takes two parameters. The first parameter is a
proxy value representing the modified view. The second parameter is the
interpolated value generated by the keyframes.

`keyframes`

    

Keyframes defining how the value changes over time. The current value of the
animator is the single argument, which is equal to `initialValue` when the
view first appears, then is equal to the end value of the previous keyframe
animation on subsequent calls.

## Discussion

Note that the `content` closure will be updated on every frame while
animating, so avoid performing any expensive operations directly within
`content`.

## See Also

### Creating keyframe-based animation

`func keyframeAnimator<Value>(initialValue: Value, trigger: some Equatable,
content: (PlaceholderContentView<Self>, Value) -> some View, keyframes:
(Value) -> some Keyframes) -> some View`

Plays the given keyframes when the given trigger value changes, updating the
view using the modifiers you apply in `body`.

`struct KeyframeAnimator`

A container that animates its content with keyframes.

`protocol Keyframes`

A type that defines changes to a value over time.

`struct KeyframeTimeline`

A description of how a value changes over time, modeled using keyframes.

`struct KeyframeTrack`

A sequence of keyframes animating a single property of a root type.

`struct KeyframeTrackContentBuilder`

The builder that creates keyframe track content from the keyframes that you
define within a closure.

`struct KeyframesBuilder`

A builder that combines keyframe content values into a single value.

`protocol KeyframeTrackContent`

A group of keyframes that define an interpolation curve of an animatable
value.

`struct CubicKeyframe`

A keyframe that uses a cubic curve to smoothly interpolate between values.

`struct LinearKeyframe`

A keyframe that uses simple linear interpolation.

`struct MoveKeyframe`

A keyframe that immediately moves to the given value without interpolating.

`struct SpringKeyframe`

A keyframe that uses a spring function to interpolate to the given value.

Instance Method

# keyframeAnimator(initialValue:trigger:content:keyframes:)

Plays the given keyframes when the given trigger value changes, updating the
view using the modifiers you apply in `body`.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func keyframeAnimator<Value>(
        initialValue: Value,
        trigger: some Equatable,
        @ViewBuilder content: @escaping (PlaceholderContentView<Self>, Value) -> some View,
        @KeyframesBuilder<Value> keyframes: @escaping (Value) -> some Keyframes
    ) -> some View
    

##  Parameters

`initialValue`

    

The initial value that the keyframes will animate from.

`trigger`

    

A value to observe for changes.

`content`

    

A view builder closure that takes two parameters. The first parameter is a
proxy value representing the modified view. The second parameter is the
interpolated value generated by the keyframes.

`keyframes`

    

Keyframes defining how the value changes over time. The current value of the
animator is the single argument, which is equal to `initialValue` when the
view first appears, then is equal to the end value of the previous keyframe
animation on subsequent calls.

## Discussion

Note that the `content` closure will be updated on every frame while
animating, so avoid performing any expensive operations directly within
`content`.

If the trigger value changes while animating, the `keyframes` closure will be
called with the current interpolated value, and the keyframes that you return
define a new animation that replaces the old one. The previous velocity will
be preserved, so cubic or spring keyframes will maintain continuity from the
previous animation if they do not specify a custom initial velocity.

When a keyframe animation finishes, the animator will remain at the end value,
which becomes the initial value for the next animation.

## See Also

### Creating keyframe-based animation

`func keyframeAnimator<Value>(initialValue: Value, repeating: Bool, content:
(PlaceholderContentView<Self>, Value) -> some View, keyframes: (Value) -> some
Keyframes) -> some View`

Loops the given keyframes continuously, updating the view using the modifiers
you apply in `body`.

`struct KeyframeAnimator`

A container that animates its content with keyframes.

`protocol Keyframes`

A type that defines changes to a value over time.

`struct KeyframeTimeline`

A description of how a value changes over time, modeled using keyframes.

`struct KeyframeTrack`

A sequence of keyframes animating a single property of a root type.

`struct KeyframeTrackContentBuilder`

The builder that creates keyframe track content from the keyframes that you
define within a closure.

`struct KeyframesBuilder`

A builder that combines keyframe content values into a single value.

`protocol KeyframeTrackContent`

A group of keyframes that define an interpolation curve of an animatable
value.

`struct CubicKeyframe`

A keyframe that uses a cubic curve to smoothly interpolate between values.

`struct LinearKeyframe`

A keyframe that uses simple linear interpolation.

`struct MoveKeyframe`

A keyframe that immediately moves to the given value without interpolating.

`struct SpringKeyframe`

A keyframe that uses a spring function to interpolate to the given value.

Instance Method

# phaseAnimator(_:content:animation:)

Animates effects that you apply to a view over a sequence of phases that
change continuously.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func phaseAnimator<Phase>(
        _ phases: some Sequence,
        @ViewBuilder content: @escaping (PlaceholderContentView<Self>, Phase) -> some View,
        animation: @escaping (Phase) -> Animation? = { _ in .default }
    ) -> some View where Phase : Equatable
    

##  Parameters

`phases`

    

The sequence of phases to cycle through. Ensure that the sequence isn’t empty.
If it is, SwiftUI logs a runtime warning and also returns a visual warning as
the output view.

`content`

    

A view builder closure that takes two parameters: a proxy value representing
the modified view and the current phase. You can apply effects to the proxy
based on the current phase.

`animation`

    

A closure that takes the current phase as input. Return the animation to use
when transitioning to the next phase. If you return `nil`, the transition
doesn’t animate. If you don’t set this parameter, SwiftUI uses a default
animation.

## Discussion

When the modified view first appears, this modifier renders its `content`
closure using the first phase as input to the closure, along with a proxy for
the modified view. Apply effects to the proxy — and thus to the modified view
— in a way that’s appropriate for the first phase value.

Right away, the modifier provides its `content` closure with the value of the
second phase. Update the effects that you apply to the proxy view accordingly,
and the modifier animates the change for you. As soon as the animation
completes, the procedure repeats using successive phases until reaching the
last phase, at which point the modifier loops back to the first phase.

## See Also

### Creating phase-based animation

Controlling the timing and movements of your animations

Build sophisticated animations that you control using phase and keyframe
animators.

`func phaseAnimator<Phase>(some Sequence, trigger: some Equatable, content:
(PlaceholderContentView<Self>, Phase) -> some View, animation: (Phase) ->
Animation?) -> some View`

Animates effects that you apply to a view over a sequence of phases that
change based on a trigger.

`struct PhaseAnimator`

A container that animates its content by automatically cycling through a
collection of phases that you provide, each defining a discrete step within an
animation.

Instance Method

# phaseAnimator(_:trigger:content:animation:)

Animates effects that you apply to a view over a sequence of phases that
change based on a trigger.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func phaseAnimator<Phase>(
        _ phases: some Sequence,
        trigger: some Equatable,
        @ViewBuilder content: @escaping (PlaceholderContentView<Self>, Phase) -> some View,
        animation: @escaping (Phase) -> Animation? = { _ in .default }
    ) -> some View where Phase : Equatable
    

##  Parameters

`phases`

    

The sequence of phases to cycle through. Ensure that the sequence isn’t empty.
If it is, SwiftUI logs a runtime warning and also returns a visual warning as
the output view.

`trigger`

    

A value whose changes cause the animator to use the next phase.

`content`

    

A view builder closure that takes two parameters: a proxy value representing
the modified view and the current phase. You can apply effects to the proxy
based on the current phase.

`animation`

    

A closure that takes the current phase as input. Return the animation to use
when transitioning to the next phase. If you return `nil`, the transition
doesn’t animate. If you don’t set this parameter, SwiftUI uses a default
animation.

## Discussion

When the modified view first appears, this modifier renders its `content`
closure using the first phase as input to the closure, along with a proxy for
the modified view. Apply effects to the proxy — and thus to the modified view
— in a way that’s appropriate for the first phase value.

Later, when the value of the `trigger` input changes, the modifier provides
its `content` closure with the value of the second phase. Update the effects
that you apply to the proxy view accordingly, and the modifier animates the
change for you. The next time the `trigger` input changes, this procedure
repeats using successive phases until reaching the last phase, at which point
the modifier loops back to the first phase.

## See Also

### Creating phase-based animation

Controlling the timing and movements of your animations

Build sophisticated animations that you control using phase and keyframe
animators.

`func phaseAnimator<Phase>(some Sequence, content:
(PlaceholderContentView<Self>, Phase) -> some View, animation: (Phase) ->
Animation?) -> some View`

Animates effects that you apply to a view over a sequence of phases that
change continuously.

`struct PhaseAnimator`

A container that animates its content by automatically cycling through a
collection of phases that you provide, each defining a discrete step within an
animation.

Instance Method

# contentTransition(_:)

Modifies the view to use a given transition as its method of animating changes
to the contents of its views.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func contentTransition(_ transition: ContentTransition) -> some View
    

##  Parameters

`transition`

    

The transition to apply when animating the content change.

## Discussion

This modifier allows you to perform a transition that animates a change within
a single view. The provided `ContentTransition` can present an opacity
animation for content changes, an interpolated animation of the content’s
paths as they change, or perform no animation at all.

Tip

The `contentTransition(_:)` modifier only has an effect within the context of
an `Animation`.

In the following example, a `Button` changes the color and font size of a
`Text` view. Since both of these properties apply to the paths of the text,
the `interpolate` transition can animate a gradual change to these properties
through the entire transition. By contrast, the `opacity` transition would
simply fade between the start and end states.

This example uses an ease-in–ease-out animation with a five-second duration to
make it easier to see the effect of the interpolation. The figure below shows
the `Text` at the beginning of the animation, halfway through, and at the end.

Time| Display  
---|---  
Start|  
Middle|  
End|  
  
To control whether content transitions use GPU-accelerated rendering, set the
value of the `contentTransitionAddsDrawingGroup` environment variable.

## See Also

### Defining transitions

`func transition<T>(T) -> some View`

Associates a transition with the view.

`func transition(AnyTransition) -> some View`

Associates a transition with the view.

`protocol Transition`

A description of view changes to apply when a view is added to and removed
from the view hierarchy.

`struct TransitionProperties`

The properties a `Transition` can have.

`enum TransitionPhase`

An indication of which the current stage of a transition.

`struct AsymmetricTransition`

A composite `Transition` that uses a different transition for insertion versus
removal.

`struct AnyTransition`

A type-erased transition.

`var contentTransition: ContentTransition`

The current method of animating the contents of views.

`var contentTransitionAddsDrawingGroup: Bool`

A Boolean value that controls whether views that render content transitions
use GPU-accelerated rendering.

`struct ContentTransition`

A kind of transition that applies to the content within a single view, rather
than to the insertion or removal of a view.

`struct PlaceholderContentView`

A placeholder used to construct an inline modifier, transition, or other
helper type.

Instance Method

# transition(_:)

Associates a transition with the view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func transition<T>(_ transition: T) -> some View where T : Transition
    

## Discussion

When this view appears or disappears, the transition will be applied to it,
allowing for animating it in and out.

The following code will conditionally show MyView, and when it appears or
disappears, will use a custom RotatingFadeTransition transition to show it.

## See Also

### Defining transitions

`func transition(AnyTransition) -> some View`

Associates a transition with the view.

`protocol Transition`

A description of view changes to apply when a view is added to and removed
from the view hierarchy.

`struct TransitionProperties`

The properties a `Transition` can have.

`enum TransitionPhase`

An indication of which the current stage of a transition.

`struct AsymmetricTransition`

A composite `Transition` that uses a different transition for insertion versus
removal.

`struct AnyTransition`

A type-erased transition.

`func contentTransition(ContentTransition) -> some View`

Modifies the view to use a given transition as its method of animating changes
to the contents of its views.

`var contentTransition: ContentTransition`

The current method of animating the contents of views.

`var contentTransitionAddsDrawingGroup: Bool`

A Boolean value that controls whether views that render content transitions
use GPU-accelerated rendering.

`struct ContentTransition`

A kind of transition that applies to the content within a single view, rather
than to the insertion or removal of a view.

`struct PlaceholderContentView`

A placeholder used to construct an inline modifier, transition, or other
helper type.

Instance Method

# transition(_:)

Associates a transition with the view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func transition(_ t: AnyTransition) -> some View
    

## Discussion

When this view appears or disappears, the transition will be applied to it,
allowing for animating it in and out.

The following code will conditionally show MyView, and when it appears or
disappears, will use a slide transition to show it.

## See Also

### Defining transitions

`func transition<T>(T) -> some View`

Associates a transition with the view.

`protocol Transition`

A description of view changes to apply when a view is added to and removed
from the view hierarchy.

`struct TransitionProperties`

The properties a `Transition` can have.

`enum TransitionPhase`

An indication of which the current stage of a transition.

`struct AsymmetricTransition`

A composite `Transition` that uses a different transition for insertion versus
removal.

`struct AnyTransition`

A type-erased transition.

`func contentTransition(ContentTransition) -> some View`

Modifies the view to use a given transition as its method of animating changes
to the contents of its views.

`var contentTransition: ContentTransition`

The current method of animating the contents of views.

`var contentTransitionAddsDrawingGroup: Bool`

A Boolean value that controls whether views that render content transitions
use GPU-accelerated rendering.

`struct ContentTransition`

A kind of transition that applies to the content within a single view, rather
than to the insertion or removal of a view.

`struct PlaceholderContentView`

A placeholder used to construct an inline modifier, transition, or other
helper type.

Instance Method

# transaction(_:)

Applies the given transaction mutation function to all animations used within
the view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func transaction(_ transform: @escaping (inout Transaction) -> Void) -> some View
    

##  Parameters

`transform`

    

The transformation to apply to transactions within this view.

## Return Value

A view that wraps this view and applies a transformation to all transactions
used within the view.

## Discussion

Use this modifier to change or replace the animation used in a view. Consider
three identical animations controlled by a button that executes all three
animations simultaneously:

  * The first animation rotates the “Rotation” `Text` view by 360 degrees.

  * The second uses the `transaction(_:)` modifier to change the animation by adding a delay to the start of the animation by two seconds and then increases the rotational speed of the “Rotation\nModified” `Text` view animation by a factor of 2.

  * The third animation uses the `transaction(_:)` modifier to replace the rotation animation affecting the “Animation\nReplaced” `Text` view with a spring animation.

The following code implements these animations:

Use this modifier on leaf views such as `Image` or `Button` rather than
container views such as `VStack` or `HStack`. The transformation applies to
all child views within this view; calling `transaction(_:)` on a container
view can lead to unbounded scope of execution depending on the depth of the
view hierarchy.

## See Also

### Moving an animation to another view

`func withTransaction<Result>(Transaction, () throws -> Result) rethrows ->
Result`

Executes a closure with the specified transaction and returns the result.

`func withTransaction<R, V>(WritableKeyPath<Transaction, V>, V, () throws ->
R) rethrows -> R`

Executes a closure with the specified transaction key path and value and
returns the result.

`func transaction(value: some Equatable, (inout Transaction) -> Void) -> some
View`

Applies the given transaction mutation function to all animations used within
the view.

`func transaction<V>((inout Transaction) -> Void, body:
(PlaceholderContentView<Self>) -> V) -> some View`

Applies the given transaction mutation function to all animations used within
the `body` closure.

`struct Transaction`

The context of the current state-processing update.

`protocol TransactionKey`

A key for accessing values in a transaction.

Instance Method

# transaction(value:_:)

Applies the given transaction mutation function to all animations used within
the view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func transaction(
        value: some Equatable,
        _ transform: @escaping (inout Transaction) -> Void
    ) -> some View
    

##  Parameters

`value`

    

A value to monitor for changes.

`transform`

    

The transformation to apply to transactions within this view.

## Return Value

A view that wraps this view and applies a transformation to all transactions
used within the view whenever `value` changes.

## Discussion

Use this modifier to change or replace the animation used in a view. Consider
three identical views controlled by a button that changes all three
simultaneously:

  * The first view animates rotating the “Rotation” `Text` view by 360 degrees.

  * The second uses the `transaction(_:)` modifier to change the animation by adding a delay to the start of the animation by two seconds and then increases the rotational speed of the “Rotation\nModified” `Text` view animation by a factor of 2.

  * The third uses the `transaction(_:)` modifier to disable animations affecting the “Animation\nReplaced” `Text` view.

The following code implements these animations:

## See Also

### Moving an animation to another view

`func withTransaction<Result>(Transaction, () throws -> Result) rethrows ->
Result`

Executes a closure with the specified transaction and returns the result.

`func withTransaction<R, V>(WritableKeyPath<Transaction, V>, V, () throws ->
R) rethrows -> R`

Executes a closure with the specified transaction key path and value and
returns the result.

`func transaction((inout Transaction) -> Void) -> some View`

Applies the given transaction mutation function to all animations used within
the view.

`func transaction<V>((inout Transaction) -> Void, body:
(PlaceholderContentView<Self>) -> V) -> some View`

Applies the given transaction mutation function to all animations used within
the `body` closure.

`struct Transaction`

The context of the current state-processing update.

`protocol TransactionKey`

A key for accessing values in a transaction.

Instance Method

# transaction(_:body:)

Applies the given transaction mutation function to all animations used within
the `body` closure.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func transaction<V>(
        _ transform: @escaping (inout Transaction) -> Void,
        @ViewBuilder body: (PlaceholderContentView<Self>) -> V
    ) -> some View where V : View
    

## Discussion

Any modifiers applied to the content of `body` will be applied to this view,
and the changes to the transaction performed in the `transform` will only
affect the modifiers defined in the `body`.

The following code animates the opacity changing with a faster animation,
while the contents of MyView are animated with the implicit transaction:

  * See Also: `Transaction.disablesAnimations`

## See Also

### Moving an animation to another view

`func withTransaction<Result>(Transaction, () throws -> Result) rethrows ->
Result`

Executes a closure with the specified transaction and returns the result.

`func withTransaction<R, V>(WritableKeyPath<Transaction, V>, V, () throws ->
R) rethrows -> R`

Executes a closure with the specified transaction key path and value and
returns the result.

`func transaction((inout Transaction) -> Void) -> some View`

Applies the given transaction mutation function to all animations used within
the view.

`func transaction(value: some Equatable, (inout Transaction) -> Void) -> some
View`

Applies the given transaction mutation function to all animations used within
the view.

`struct Transaction`

The context of the current state-processing update.

`protocol TransactionKey`

A key for accessing values in a transaction.

Instance Method

# contentTransition(_:)

Modifies the view to use a given transition as its method of animating changes
to the contents of its views.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func contentTransition(_ transition: ContentTransition) -> some View
    

##  Parameters

`transition`

    

The transition to apply when animating the content change.

## Discussion

This modifier allows you to perform a transition that animates a change within
a single view. The provided `ContentTransition` can present an opacity
animation for content changes, an interpolated animation of the content’s
paths as they change, or perform no animation at all.

Tip

The `contentTransition(_:)` modifier only has an effect within the context of
an `Animation`.

In the following example, a `Button` changes the color and font size of a
`Text` view. Since both of these properties apply to the paths of the text,
the `interpolate` transition can animate a gradual change to these properties
through the entire transition. By contrast, the `opacity` transition would
simply fade between the start and end states.

This example uses an ease-in–ease-out animation with a five-second duration to
make it easier to see the effect of the interpolation. The figure below shows
the `Text` at the beginning of the animation, halfway through, and at the end.

Time| Display  
---|---  
Start|  
Middle|  
End|  
  
To control whether content transitions use GPU-accelerated rendering, set the
value of the `contentTransitionAddsDrawingGroup` environment variable.

## See Also

### Defining transitions

`func transition<T>(T) -> some View`

Associates a transition with the view.

`func transition(AnyTransition) -> some View`

Associates a transition with the view.

`protocol Transition`

A description of view changes to apply when a view is added to and removed
from the view hierarchy.

`struct TransitionProperties`

The properties a `Transition` can have.

`enum TransitionPhase`

An indication of which the current stage of a transition.

`struct AsymmetricTransition`

A composite `Transition` that uses a different transition for insertion versus
removal.

`struct AnyTransition`

A type-erased transition.

`var contentTransition: ContentTransition`

The current method of animating the contents of views.

`var contentTransitionAddsDrawingGroup: Bool`

A Boolean value that controls whether views that render content transitions
use GPU-accelerated rendering.

`struct ContentTransition`

A kind of transition that applies to the content within a single view, rather
than to the insertion or removal of a view.

`struct PlaceholderContentView`

A placeholder used to construct an inline modifier, transition, or other
helper type.

Instance Method

# matchedGeometryEffect(id:in:properties:anchor:isSource:)

Defines a group of views with synchronized geometry using an identifier and
namespace that you provide.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func matchedGeometryEffect<ID>(
        id: ID,
        in namespace: Namespace.ID,
        properties: MatchedGeometryProperties = .frame,
        anchor: UnitPoint = .center,
        isSource: Bool = true
    ) -> some View where ID : Hashable
    

##  Parameters

`id`

    

The identifier, often derived from the identifier of the data being displayed
by the view.

`namespace`

    

The namespace in which defines the `id`. New namespaces are created by adding
an `@Namespace` variable to a `View` type and reading its value in the view’s
body method.

`properties`

    

The properties to copy from the source view.

`anchor`

    

The relative location in the view used to produce its shared position value.

`isSource`

    

True if the view should be used as the source of geometry for other views in
the group.

## Return Value

A new view that defines an entry in the global database of views synchronizing
their geometry.

## Discussion

This method sets the geometry of each view in the group from the inserted view
with `isSource = true` (known as the “source” view), updating the values
marked by `properties`.

If inserting a view in the same transaction that another view with the same
key is removed, the system will interpolate their frame rectangles in window
space to make it appear that there is a single view moving from its old
position to its new position. The usual transition mechanisms define how each
of the two views is rendered during the transition (e.g. fade in/out, scale,
etc), the `matchedGeometryEffect()` modifier only arranges for the geometry of
the views to be linked, not their rendering.

If the number of currently-inserted views in the group with `isSource = true`
is not exactly one results are undefined, due to it not being clear which is
the source view.

## See Also

### Synchronizing geometries

`struct MatchedGeometryProperties`

A set of view properties that may be synchronized between views using the
`View.matchedGeometryEffect()` function.

`protocol GeometryEffect`

An effect that changes the visual appearance of a view, largely without
changing its ancestors or descendants.

`struct Namespace`

A dynamic property type that allows access to a namespace defined by the
persistent identity of the object containing the property (e.g. a view).

`func geometryGroup() -> some View`

Isolates the geometry (e.g. position and size) of the view from its parent
view.

Instance Method

# geometryGroup()

Isolates the geometry (e.g. position and size) of the view from its parent
view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func geometryGroup() -> some View
    

## Discussion

By default SwiftUI views push position and size changes down through the view
hierarchy, so that only views that draw something (known as leaf views) apply
the current animation to their frame rectangle. However in some cases this
coalescing behavior can give undesirable results; inserting a geometry group
can correct that. A group acts as a barrier between the parent view and its
subviews, forcing the position and size values to be resolved and animated by
the parent, before being passed down to each subview.

The example below shows one use of this function: ensuring that the member
views of each row in the stack apply (and animate as) a single geometric
transform from their ancestor view, rather than letting the effects of the
ancestor views be applied separately to each leaf view. If the members of
`ItemView` may be added and removed at different times the group ensures that
they stay locked together as animations are applied.

Returns: a new view whose geometry is isolated from that of its parent view.

## See Also

### Synchronizing geometries

`func matchedGeometryEffect<ID>(id: ID, in: Namespace.ID, properties:
MatchedGeometryProperties, anchor: UnitPoint, isSource: Bool) -> some View`

Defines a group of views with synchronized geometry using an identifier and
namespace that you provide.

`struct MatchedGeometryProperties`

A set of view properties that may be synchronized between views using the
`View.matchedGeometryEffect()` function.

`protocol GeometryEffect`

An effect that changes the visual appearance of a view, largely without
changing its ancestors or descendants.

`struct Namespace`

A dynamic property type that allows access to a namespace defined by the
persistent identity of the object containing the property (e.g. a view).



# Gestures

Article

# Adding interactivity with gestures

Use gesture modifiers to add interactivity to your app.

## Overview

Gesture modifiers handle all of the logic needed to process user-input events
such as touches, and recognize when those events match a known gesture
pattern, such as a long press or rotation. When recognizing a pattern, SwiftUI
runs a callback you use to update the state of a view or perform an action.

### Add gesture modifiers to a view

Each gesture you add applies to a specific view in the view hierarchy. To
recognize a gesture event on a particular view, create and configure the
gesture, and then use the `gesture(_:including:)` modifier:

### Respond to gesture callbacks

Depending on the callbacks you add to a gesture modifier, SwiftUI reports back
to your code whenever the state of the gesture changes. Gesture modifiers
offer three ways to receive updates: `updating(_:body:)`, `onChanged(_:)`, and
`onEnded(_:)`.

#### Update transient UI state

To update a view as a gesture changes, add a `GestureState` property to your
view and update it in the `updating(_:body:)` callback. SwiftUI invokes the
updating callback as soon as it recognizes the gesture and whenever the value
of the gesture changes. For example, SwiftUI invokes the updating callback as
soon as a magnification gesture begins and then again whenever the
magnification value changes. SwiftUI doesn’t invoke the updating callback when
the user ends or cancels a gesture. Instead, the gesture state property
automatically resets its state back to its initial value.

For example, to make a view that changes color while the user performs a long
press, add a gesture state property and update it in the updating callback.

#### Update permanent state during a gesture

To track changes to a gesture that shouldn’t reset once the gesture ends, use
the `onChanged(_:)` callback. For example, to count the number of times your
app recognizes a long press, add an `onChanged(_:)` callback and increment a
counter.

#### Update permanent state when a gesture ends

To recognize when a gesture successfully completes and to retrieve the
gesture’s final value, use the `onEnded(_:)` function to update your app’s
state in the callback. SwiftUI only invokes the `onEnded(_:)` callback when
the gesture succeeds. For example, during a `LongPressGesture` if the user
stops touching the view before `minimumDuration` seconds have elapsed or moves
their finger more than `maximumDistance` points SwiftUI does not invoke the
`onEnded(_:)` callback.

For example, to stop counting long press attempts after the user completes a
long press, add an `onEnded(_:)` callback and conditionally apply the gesture
modifier.

Instance Method

# onTapGesture(count:perform:)

Adds an action to perform when this view recognizes a tap gesture.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 16.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func onTapGesture(
        count: Int = 1,
        perform action: @escaping () -> Void
    ) -> some View
    

##  Parameters

`count`

    

The number of taps or clicks required to trigger the action closure provided
in `action`. Defaults to `1`.

`action`

    

The action to perform.

## Discussion

Use this method to perform the specified `action` when the user clicks or taps
on the view or container `count` times.

Note

If you create a control that’s functionally equivalent to a `Button`, use
`ButtonStyle` to create a customized button instead.

In the example below, the color of the heart images changes to a random color
from the `colors` array whenever the user clicks or taps on the view twice:

## See Also

### Recognizing tap gestures

`func onTapGesture(count: Int, coordinateSpace: some CoordinateSpaceProtocol,
perform: (CGPoint) -> Void) -> some View`

Adds an action to perform when this view recognizes a tap gesture, and
provides the action with the location of the interaction.

`struct TapGesture`

A gesture that recognizes one or more taps.

`struct SpatialTapGesture`

A gesture that recognizes one or more taps and reports their location.

Instance Method

# onTapGesture(count:coordinateSpace:perform:)

Adds an action to perform when this view recognizes a tap gesture, and
provides the action with the location of the interaction.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  watchOS 10.0+
visionOS 1.0+

    
    
    func onTapGesture(
        count: Int = 1,
        coordinateSpace: some CoordinateSpaceProtocol = .local,
        perform action: @escaping (CGPoint) -> Void
    ) -> some View
    

##  Parameters

`count`

    

The number of taps or clicks required to trigger the action closure provided
in `action`. Defaults to `1`.

`coordinateSpace`

    

The coordinate space in which to receive location values. Defaults to
`CoordinateSpace.local`.

`action`

    

The action to perform. This closure receives an input that indicates where the
interaction occurred.

## Discussion

Use this method to perform the specified `action` when the user clicks or taps
on the modified view `count` times. The action closure receives the location
of the interaction.

Note

If you create a control that’s functionally equivalent to a `Button`, use
`ButtonStyle` to create a customized button instead.

The following code adds a tap gesture to a `Circle` that toggles the color of
the circle based on the tap location.

## See Also

### Recognizing tap gestures

`func onTapGesture(count: Int, perform: () -> Void) -> some View`

Adds an action to perform when this view recognizes a tap gesture.

`struct TapGesture`

A gesture that recognizes one or more taps.

`struct SpatialTapGesture`

A gesture that recognizes one or more taps and reports their location.

Structure

# TapGesture

A gesture that recognizes one or more taps.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 16.0+  watchOS
6.0+  visionOS 1.0+

    
    
    struct TapGesture

## Overview

To recognize a tap gesture on a view, create and configure the gesture, and
then add it to the view using the `gesture(_:including:)` modifier. The
following code adds a tap gesture to a `Circle` that toggles the color of the
circle:

## Topics

### Creating a tap gesture

`init(count: Int)`

Creates a tap gesture with the number of required taps.

`var count: Int`

The required number of tap events.

## Relationships

### Conforms To

  * `Gesture`

## See Also

### Recognizing tap gestures

`func onTapGesture(count: Int, perform: () -> Void) -> some View`

Adds an action to perform when this view recognizes a tap gesture.

`func onTapGesture(count: Int, coordinateSpace: some CoordinateSpaceProtocol,
perform: (CGPoint) -> Void) -> some View`

Adds an action to perform when this view recognizes a tap gesture, and
provides the action with the location of the interaction.

`struct SpatialTapGesture`

A gesture that recognizes one or more taps and reports their location.

Structure

# SpatialTapGesture

A gesture that recognizes one or more taps and reports their location.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    struct SpatialTapGesture

## Overview

To recognize a tap gesture on a view, create and configure the gesture, and
then add it to the view using the `gesture(_:including:)` modifier. The
following code adds a tap gesture to a `Circle` that toggles the color of the
circle based on the tap location:

## Topics

### Creating a spatial tap gesture

`init(count: Int, coordinateSpace: some CoordinateSpaceProtocol)`

Creates a tap gesture with the number of required taps and the coordinate
space of the gesture’s location.

`var coordinateSpace: CoordinateSpace`

The coordinate space in which to receive location values.

`var count: Int`

The required number of tap events.

### Getting the gesture’s value

`struct Value`

The attributes of a tap gesture.

### Deprecated initializers

`init(count: Int, coordinateSpace: CoordinateSpace)`

Creates a tap gesture with the number of required taps and the coordinate
space of the gesture’s location.

Deprecated

## Relationships

### Conforms To

  * `Gesture`

## See Also

### Recognizing tap gestures

`func onTapGesture(count: Int, perform: () -> Void) -> some View`

Adds an action to perform when this view recognizes a tap gesture.

`func onTapGesture(count: Int, coordinateSpace: some CoordinateSpaceProtocol,
perform: (CGPoint) -> Void) -> some View`

Adds an action to perform when this view recognizes a tap gesture, and
provides the action with the location of the interaction.

`struct TapGesture`

A gesture that recognizes one or more taps.

Instance Method

#
onLongPressGesture(minimumDuration:maximumDistance:perform:onPressingChanged:)

Adds an action to perform when this view recognizes a long press gesture.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    func onLongPressGesture(
        minimumDuration: Double = 0.5,
        maximumDistance: CGFloat = 10,
        perform action: @escaping () -> Void,
        onPressingChanged: ((Bool) -> Void)? = nil
    ) -> some View
    

##  Parameters

`minimumDuration`

    

The minimum duration of the long press that must elapse before the gesture
succeeds.

`maximumDistance`

    

The maximum distance that the fingers or cursor performing the long press can
move before the gesture fails.

`action`

    

The action to perform when a long press is recognized.

`onPressingChanged`

    

A closure to run when the pressing state of the gesture changes, passing the
current state as a parameter.

## See Also

### Recognizing long press gestures

`func onLongPressGesture(minimumDuration: Double, perform: () -> Void,
onPressingChanged: ((Bool) -> Void)?) -> some View`

Adds an action to perform when this view recognizes a long press gesture.

`func onLongTouchGesture(minimumDuration: Double, perform: () -> Void,
onTouchingChanged: ((Bool) -> Void)?) -> some View`

Adds an action to perform when this view recognizes a remote long touch
gesture. A long touch gesture is when the finger is on the remote touch
surface without actually pressing.

`struct LongPressGesture`

A gesture that succeeds when the user performs a long press.

Instance Method

# onLongPressGesture(minimumDuration:perform:onPressingChanged:)

Adds an action to perform when this view recognizes a long press gesture.

tvOS 14.0+

    
    
    func onLongPressGesture(
        minimumDuration: Double = 0.5,
        perform action: @escaping () -> Void,
        onPressingChanged: ((Bool) -> Void)? = nil
    ) -> some View
    

##  Parameters

`minimumDuration`

    

The minimum duration of the long press that must elapse before the gesture
succeeds.

`action`

    

The action to perform when a long press is recognized.

`onPressingChanged`

    

A closure to run when the pressing state of the gesture changes, passing the
current state as a parameter.

## See Also

### Recognizing long press gestures

`func onLongPressGesture(minimumDuration: Double, maximumDistance: CGFloat,
perform: () -> Void, onPressingChanged: ((Bool) -> Void)?) -> some View`

Adds an action to perform when this view recognizes a long press gesture.

`func onLongTouchGesture(minimumDuration: Double, perform: () -> Void,
onTouchingChanged: ((Bool) -> Void)?) -> some View`

Adds an action to perform when this view recognizes a remote long touch
gesture. A long touch gesture is when the finger is on the remote touch
surface without actually pressing.

`struct LongPressGesture`

A gesture that succeeds when the user performs a long press.

Instance Method

# onLongTouchGesture(minimumDuration:perform:onTouchingChanged:)

Adds an action to perform when this view recognizes a remote long touch
gesture. A long touch gesture is when the finger is on the remote touch
surface without actually pressing.

tvOS 16.0+

    
    
    func onLongTouchGesture(
        minimumDuration: Double = 0.5,
        perform action: @escaping () -> Void,
        onTouchingChanged: ((Bool) -> Void)? = nil
    ) -> some View
    

##  Parameters

`minimumDuration`

    

The minimum duration of the long touch that must elapse before the gesture
succeeds.

`action`

    

The action to perform when a long touch is recognized

`onTouchingChanged`

    

A closure to run when the touching state of the gesture changes, passing the
current state as a parameter.

## See Also

### Recognizing long press gestures

`func onLongPressGesture(minimumDuration: Double, maximumDistance: CGFloat,
perform: () -> Void, onPressingChanged: ((Bool) -> Void)?) -> some View`

Adds an action to perform when this view recognizes a long press gesture.

`func onLongPressGesture(minimumDuration: Double, perform: () -> Void,
onPressingChanged: ((Bool) -> Void)?) -> some View`

Adds an action to perform when this view recognizes a long press gesture.

`struct LongPressGesture`

A gesture that succeeds when the user performs a long press.

Structure

# LongPressGesture

A gesture that succeeds when the user performs a long press.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 14.0+  watchOS
6.0+  visionOS 1.0+

    
    
    struct LongPressGesture

## Overview

To recognize a long-press gesture on a view, create and configure the gesture,
then add it to the view using the `gesture(_:including:)` modifier.

Add a long-press gesture to a `Circle` to animate its color from blue to red,
and then change it to green when the gesture ends:

## Topics

### Creating a long press gesture

`init(minimumDuration: Double)`

Creates a long-press gesture with a minimum duration

`init(minimumDuration: Double, maximumDistance: CGFloat)`

Creates a long-press gesture with a minimum duration and a maximum distance
that the interaction can move before the gesture fails.

`var minimumDuration: Double`

The minimum duration of the long press that must elapse before the gesture
succeeds.

`var maximumDistance: CGFloat`

The maximum distance that the long press can move before the gesture fails.

## Relationships

### Conforms To

  * `Gesture`

## See Also

### Recognizing long press gestures

`func onLongPressGesture(minimumDuration: Double, maximumDistance: CGFloat,
perform: () -> Void, onPressingChanged: ((Bool) -> Void)?) -> some View`

Adds an action to perform when this view recognizes a long press gesture.

`func onLongPressGesture(minimumDuration: Double, perform: () -> Void,
onPressingChanged: ((Bool) -> Void)?) -> some View`

Adds an action to perform when this view recognizes a long press gesture.

`func onLongTouchGesture(minimumDuration: Double, perform: () -> Void,
onTouchingChanged: ((Bool) -> Void)?) -> some View`

Adds an action to perform when this view recognizes a remote long touch
gesture. A long touch gesture is when the finger is on the remote touch
surface without actually pressing.

Structure

# SpatialEventGesture

A gesture that provides information about ongoing spatial events like clicks
and touches.

visionOS 1.0+

    
    
    struct SpatialEventGesture

## Overview

Use a gesture of this type to track multiple simultaneous spatial events and
gain access to detailed information about each. For example, you can place a
particle emitter at every location in a `Canvas` that has an ongoing spatial
event:

The gesture provides a `SpatialEventCollection` structure when it detects
changes. The collection contains `SpatialEventCollection.Event` values that
represent ongoing spatial events. Each event contains a stable, unique
identifier so that you can track how the event changes over time. The event
also indicates its current location, a timestamp, the pose of the input device
that creates it, and other useful information.

The phase of events in the collection can change to
`SpatialEventCollection.Event.Phase.ended` or
`SpatialEventCollection.Event.Phase.cancelled` while the gesture itself
remains active. Individually track state for each event inside `onChanged(_:)`
or `updating(_:body:)` and clean up all state in `onEnded(_:)`.

Tip

Only use a spatial event gesture if you need to access low-level event
information, like when you create a complex multi-touch experience. For most
use cases, it’s better to rely on gestures that recognize targeted
interactions, like a `SpatialTapGesture`, `MagnifyGesture`, or `DragGesture`.

## Topics

### Creating a spatial event gesture

`init(coordinateSpace: any CoordinateSpaceProtocol)`

Creates the gesture with a desired coordinate space.

### Getting gesture properties

`let coordinateSpace: CoordinateSpace`

The coordinate space of the gesture.

## Relationships

### Conforms To

  * `Gesture`

## See Also

### Recognizing spatial events

`struct SpatialEventCollection`

A collection of spatial input events that target a specific view.

Structure

# SpatialEventCollection

A collection of spatial input events that target a specific view.

visionOS 1.0+

    
    
    struct SpatialEventCollection

## Overview

You receive a structure of this type as an input to the `onChanged(_:)` or
`onEnded(_:)` method of a `SpatialEventGesture`. The structure contains a
collection of `SpatialEventCollection.Event` values that correspond to ongoing
input events. You can look up a specific event in the collection by its `id`
value or iterate over all events in the collection to apply logic depending on
the event’s state.

## Topics

### Accessing the collection’s events

`struct Event`

A spatial event generated from an input like a touch or click that can drive
gestures in the system.

`subscript(SpatialEventCollection.Event.ID) -> SpatialEventCollection.Event?`

Retrieves an event using its unique identifier.

### Iterating over events in the collection

`func makeIterator() -> SpatialEventCollection.Iterator`

Makes an iterator over all events in the collection.

`struct Iterator`

An iterator over all events in the collection.

## Relationships

### Conforms To

  * `Collection`
  * `Equatable`
  * `Sequence`

## See Also

### Recognizing spatial events

`struct SpatialEventGesture`

A gesture that provides information about ongoing spatial events like clicks
and touches.

Instance Method

# gesture(_:including:)

Attaches a gesture to the view with a lower precedence than gestures defined
by the view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func gesture<T>(
        _ gesture: T,
        including mask: GestureMask = .all
    ) -> some View where T : Gesture
    

##  Parameters

`gesture`

    

A gesture to attach to the view.

`mask`

    

A value that controls how adding this gesture to the view affects other
gestures recognized by the view and its subviews. Defaults to `all`.

## Discussion

Use this method when you need to attach a gesture to a view. The example below
defines a custom gesture that prints a message to the console and attaches it
to the view’s `VStack`. Inside the `VStack` a red heart `Image` defines its
own `TapGesture` handler that also prints a message to the console, and blue
rectangle with no custom gesture handlers. Tapping or clicking the image
prints a message to the console from the tap gesture handler on the image,
while tapping or clicking the rectangle inside the `VStack` prints a message
in the console from the enclosing vertical stack gesture handler.

## See Also

### Recognizing gestures that change over time

`struct DragGesture`

A dragging motion that invokes an action as the drag-event sequence changes.

`struct MagnifyGesture`

A gesture that recognizes a magnification motion and tracks the amount of
magnification.

`struct RotateGesture`

A gesture that recognizes a rotation motion and tracks the angle of the
rotation.

`struct RotateGesture3D`

A gesture that recognizes 3D rotation motion and tracks the angle and axis of
the rotation.

`struct GestureMask`

Options that control how adding a gesture to a view affects other gestures
recognized by the view and its subviews.

Structure

# DragGesture

A dragging motion that invokes an action as the drag-event sequence changes.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    struct DragGesture

## Overview

To recognize a drag gesture on a view, create and configure the gesture, and
then add it to the view using the `gesture(_:including:)` modifier.

Add a drag gesture to a `Circle` and change its color while the user performs
the drag gesture:

## Topics

### Creating a drag gesture

`init(minimumDistance: CGFloat, coordinateSpace: some
CoordinateSpaceProtocol)`

Creates a dragging gesture with the minimum dragging distance before the
gesture succeeds and the coordinate space of the gesture’s location.

`var minimumDistance: CGFloat`

The minimum dragging distance before the gesture succeeds.

`var coordinateSpace: CoordinateSpace`

The coordinate space in which to receive location values.

### Deprecated initializers

`init(minimumDistance: CGFloat, coordinateSpace: CoordinateSpace)`

Creates a dragging gesture with the minimum dragging distance before the
gesture succeeds and the coordinate space of the gesture’s location.

Deprecated

### Structures

`struct Value`

The attributes of a drag gesture.

## Relationships

### Conforms To

  * `Gesture`

## See Also

### Recognizing gestures that change over time

`func gesture<T>(T, including: GestureMask) -> some View`

Attaches a gesture to the view with a lower precedence than gestures defined
by the view.

`struct MagnifyGesture`

A gesture that recognizes a magnification motion and tracks the amount of
magnification.

`struct RotateGesture`

A gesture that recognizes a rotation motion and tracks the angle of the
rotation.

`struct RotateGesture3D`

A gesture that recognizes 3D rotation motion and tracks the angle and axis of
the rotation.

`struct GestureMask`

Options that control how adding a gesture to a view affects other gestures
recognized by the view and its subviews.

Structure

# MagnifyGesture

A gesture that recognizes a magnification motion and tracks the amount of
magnification.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    struct MagnifyGesture

## Overview

A magnify gesture tracks how a magnification event sequence changes. To
recognize a magnify gesture on a view, create and configure the gesture, and
then add it to the view using the `gesture(_:including:)` modifier.

Add a magnify gesture to a `Circle` that changes its size while the user
performs the gesture:

## Topics

### Creating the gesture

`init(minimumScaleDelta: CGFloat)`

Creates a magnify gesture with a given minimum delta for the gesture to start.

`var minimumScaleDelta: CGFloat`

The minimum required delta before the gesture starts.

## Relationships

### Conforms To

  * `Gesture`

## See Also

### Recognizing gestures that change over time

`func gesture<T>(T, including: GestureMask) -> some View`

Attaches a gesture to the view with a lower precedence than gestures defined
by the view.

`struct DragGesture`

A dragging motion that invokes an action as the drag-event sequence changes.

`struct RotateGesture`

A gesture that recognizes a rotation motion and tracks the angle of the
rotation.

`struct RotateGesture3D`

A gesture that recognizes 3D rotation motion and tracks the angle and axis of
the rotation.

`struct GestureMask`

Options that control how adding a gesture to a view affects other gestures
recognized by the view and its subviews.

Structure

# RotateGesture

A gesture that recognizes a rotation motion and tracks the angle of the
rotation.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    struct RotateGesture

## Overview

A rotate gesture tracks how a rotation event sequence changes. To recognize a
rotate gesture on a view, create and configure the gesture, and then add it to
the view using the `gesture(_:including:)` modifier.

Add a rotate gesture to a `Rectangle` and apply a rotation effect:

## Topics

### Creating the gesture

`init(minimumAngleDelta: Angle)`

Creates a rotation gesture with a minimum delta for the gesture to start.

`var minimumAngleDelta: Angle`

The minimum delta required before the gesture succeeds.

## Relationships

### Conforms To

  * `Gesture`

## See Also

### Recognizing gestures that change over time

`func gesture<T>(T, including: GestureMask) -> some View`

Attaches a gesture to the view with a lower precedence than gestures defined
by the view.

`struct DragGesture`

A dragging motion that invokes an action as the drag-event sequence changes.

`struct MagnifyGesture`

A gesture that recognizes a magnification motion and tracks the amount of
magnification.

`struct RotateGesture3D`

A gesture that recognizes 3D rotation motion and tracks the angle and axis of
the rotation.

`struct GestureMask`

Options that control how adding a gesture to a view affects other gestures
recognized by the view and its subviews.

Structure

# RotateGesture3D

A gesture that recognizes 3D rotation motion and tracks the angle and axis of
the rotation.

visionOS 1.0+

    
    
    struct RotateGesture3D

## Overview

You can constrain this gesture to recognize rotation about a specific 3D axis.
For example, `RotateGesture3D(constrainedToAxis: .x)` creates a gesture that
recognizes rotation only around the global X axis. The axis you provide will
be normalized.

A rotation gesture tracks how a rotation event sequence changes. To recognize
a rotation gesture on a view, create and configure the gesture, and then add
it to the view using the `gesture(_:including:)` modifier.

## Topics

### Creating the gesture

`init(constrainedToAxis: RotationAxis3D?, minimumAngleDelta: Angle)`

Creates a rotation gesture with a minimum delta for the gesture to start and
axis to constrain measurement of rotation.

`var minimumAngleDelta: Angle`

The minimum angle delta before the gesture becomes active.

`var constrainedAxis: RotationAxis3D?`

An axis around which the rotation is constrained.

## Relationships

### Conforms To

  * `Gesture`

## See Also

### Recognizing gestures that change over time

`func gesture<T>(T, including: GestureMask) -> some View`

Attaches a gesture to the view with a lower precedence than gestures defined
by the view.

`struct DragGesture`

A dragging motion that invokes an action as the drag-event sequence changes.

`struct MagnifyGesture`

A gesture that recognizes a magnification motion and tracks the amount of
magnification.

`struct RotateGesture`

A gesture that recognizes a rotation motion and tracks the angle of the
rotation.

`struct GestureMask`

Options that control how adding a gesture to a view affects other gestures
recognized by the view and its subviews.

Structure

# GestureMask

Options that control how adding a gesture to a view affects other gestures
recognized by the view and its subviews.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct GestureMask

## Topics

### Getting gesture options

`static let all: GestureMask`

Enable both the added gesture as well as all other gestures on the view and
its subviews.

`static let gesture: GestureMask`

Enable the added gesture but disable all gestures in the subview hierarchy.

`static let subviews: GestureMask`

Enable all gestures in the subview hierarchy but disable the added gesture.

`static let none: GestureMask`

Disable all gestures in the subview hierarchy, including the added gesture.

## Relationships

### Conforms To

  * `Equatable`
  * `ExpressibleByArrayLiteral`
  * `OptionSet`
  * `RawRepresentable`
  * `Sendable`
  * `SetAlgebra`

## See Also

### Recognizing gestures that change over time

`func gesture<T>(T, including: GestureMask) -> some View`

Attaches a gesture to the view with a lower precedence than gestures defined
by the view.

`struct DragGesture`

A dragging motion that invokes an action as the drag-event sequence changes.

`struct MagnifyGesture`

A gesture that recognizes a magnification motion and tracks the amount of
magnification.

`struct RotateGesture`

A gesture that recognizes a rotation motion and tracks the angle of the
rotation.

`struct RotateGesture3D`

A gesture that recognizes 3D rotation motion and tracks the angle and axis of
the rotation.

Article

# Composing SwiftUI gestures

Combine gestures to create complex interactions.

## Overview

When you add multiple gestures to your app’s view hierarchy, you need to
decide how the gestures interact with each other. You use gesture composition
to define the order SwiftUI recognizes gestures. There are three gesture
composition types:

  * Simultaneous

  * Sequenced

  * Exclusive

When you combine gesture modifiers simultaneously, SwiftUI must recognize all
subgesture patterns at the same time for it to recognize the combining
gesture. When you sequence gesture modifiers one after the other, SwiftUI must
recognize each subgesture in order. Finally, when you combine gestures
exclusively, SwiftUI recognizes the entire gesture pattern when SwiftUI only
recognizes one subgesture but not the others.

### Sequence one gesture after another

When you sequence one gesture after another, SwiftUI recognizes the first
gesture before it recognizes the second. For example, to require a long press
before the user can drag a view, you sequence a `DragGesture` after a
`LongPressGesture`.

#### Model sequenced gesture states

To make it easier to track complicated states, use an enumeration that
captures all of the states you need to configure your views. In the following
example, there are three important states: no interaction (`inactive`), long
press in progress (`pressing`), and dragging (`dragging`).

#### Create gestures and update the UI state

When you sequence two gestures, the callbacks capture the state of both
gestures. In the update callback, the new `value` uses an enumeration to
represent the combination of the possible gesture states. The code below
converts the underlying gesture states into the high-level `DragState`
enumeration defined above.

When the user begins pressing the view, the drag state changes to `pressing`
and a shadow animates under the shape. After the user finishes the long press
and the drag state changes to `dragging`, a border appears around the shape to
indicate that the user may begin moving the view.

## See Also

### Combining gestures

`func simultaneousGesture<T>(T, including: GestureMask) -> some View`

Attaches a gesture to the view to process simultaneously with gestures defined
by the view.

`struct SequenceGesture`

A gesture that’s a sequence of two gestures.

`struct SimultaneousGesture`

A gesture containing two gestures that can happen at the same time with
neither of them preceding the other.

`struct ExclusiveGesture`

A gesture that consists of two gestures where only one of them can succeed.

Instance Method

# simultaneousGesture(_:including:)

Attaches a gesture to the view to process simultaneously with gestures defined
by the view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func simultaneousGesture<T>(
        _ gesture: T,
        including mask: GestureMask = .all
    ) -> some View where T : Gesture
    

##  Parameters

`gesture`

    

A gesture to attach to the view.

`mask`

    

A value that controls how adding this gesture to the view affects other
gestures recognized by the view and its subviews. Defaults to `all`.

## Discussion

Use this method when you need to define and process a view specific gesture
simultaneously with the same priority as the view’s existing gestures. The
example below defines a custom gesture that prints a message to the console
and attaches it to the view’s `VStack`. Inside the `VStack` is a red heart
`Image` defines its own `TapGesture` handler that also prints a message to the
console and a blue rectangle with no custom gesture handlers.

Tapping or clicking the “heart” image sends two messages to the console: one
for the image’s tap gesture handler, and the other from a custom gesture
handler attached to the enclosing vertical stack. Tapping or clicking on the
blue rectangle results only in the single message to the console from the tap
recognizer attached to the `VStack`:

## See Also

### Combining gestures

Composing SwiftUI gestures

Combine gestures to create complex interactions.

`struct SequenceGesture`

A gesture that’s a sequence of two gestures.

`struct SimultaneousGesture`

A gesture containing two gestures that can happen at the same time with
neither of them preceding the other.

`struct ExclusiveGesture`

A gesture that consists of two gestures where only one of them can succeed.

Structure

# SequenceGesture

A gesture that’s a sequence of two gestures.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct SequenceGesture<First, Second> where First : Gesture, Second : Gesture

## Overview

Read Composing SwiftUI gestures to learn how you can create a sequence of two
gestures.

## Topics

### Creating the gesture

`init(First, Second)`

Creates a sequence gesture with two gestures.

`var first: First`

The first gesture in a sequence of two gestures.

`var second: Second`

The second gesture in a sequence of two gestures.

### Getting the gesture’s values

`enum Value`

The value of a sequence gesture that helps to detect whether the first gesture
succeeded, so the second gesture can start.

## Relationships

### Conforms To

  * `Gesture`

## See Also

### Combining gestures

Composing SwiftUI gestures

Combine gestures to create complex interactions.

`func simultaneousGesture<T>(T, including: GestureMask) -> some View`

Attaches a gesture to the view to process simultaneously with gestures defined
by the view.

`struct SimultaneousGesture`

A gesture containing two gestures that can happen at the same time with
neither of them preceding the other.

`struct ExclusiveGesture`

A gesture that consists of two gestures where only one of them can succeed.

Structure

# SimultaneousGesture

A gesture containing two gestures that can happen at the same time with
neither of them preceding the other.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct SimultaneousGesture<First, Second> where First : Gesture, Second : Gesture

## Overview

A simultaneous gesture is a container-event handler that evaluates its two
child gestures at the same time. Its value is a struct with two optional
values, each representing the phases of one of the two gestures.

## Topics

### Creating the gesture

`init(First, Second)`

Creates a gesture with two gestures that can receive updates or succeed
independently of each other.

`var first: First`

The first of two gestures that can happen simultaneously.

`var second: Second`

The second of two gestures that can happen simultaneously.

### Getting the gesture’s values

`struct Value`

The value of a simultaneous gesture that indicates which of its two gestures
receives events.

## Relationships

### Conforms To

  * `Gesture`

## See Also

### Combining gestures

Composing SwiftUI gestures

Combine gestures to create complex interactions.

`func simultaneousGesture<T>(T, including: GestureMask) -> some View`

Attaches a gesture to the view to process simultaneously with gestures defined
by the view.

`struct SequenceGesture`

A gesture that’s a sequence of two gestures.

`struct ExclusiveGesture`

A gesture that consists of two gestures where only one of them can succeed.

Structure

# ExclusiveGesture

A gesture that consists of two gestures where only one of them can succeed.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct ExclusiveGesture<First, Second> where First : Gesture, Second : Gesture

## Overview

The `ExclusiveGesture` gives precedence to its first gesture.

## Topics

### Creating the gesture

`init(First, Second)`

Creates a gesture from two gestures where only one of them succeeds.

`var first: First`

The first of two gestures.

`var second: Second`

The second of two gestures.

### Supporting types

`enum Value`

The value of an exclusive gesture that indicates which of two gestures
succeeded.

## Relationships

### Conforms To

  * `Gesture`

## See Also

### Combining gestures

Composing SwiftUI gestures

Combine gestures to create complex interactions.

`func simultaneousGesture<T>(T, including: GestureMask) -> some View`

Attaches a gesture to the view to process simultaneously with gestures defined
by the view.

`struct SequenceGesture`

A gesture that’s a sequence of two gestures.

`struct SimultaneousGesture`

A gesture containing two gestures that can happen at the same time with
neither of them preceding the other.

Instance Method

# highPriorityGesture(_:including:)

Attaches a gesture to the view with a higher precedence than gestures defined
by the view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func highPriorityGesture<T>(
        _ gesture: T,
        including mask: GestureMask = .all
    ) -> some View where T : Gesture
    

##  Parameters

`gesture`

    

A gesture to attach to the view.

`mask`

    

A value that controls how adding this gesture to the view affects other
gestures recognized by the view and its subviews. Defaults to `all`.

## Discussion

Use this method when you need to define a high priority gesture to take
precedence over the view’s existing gestures. The example below defines a
custom gesture that prints a message to the console and attaches it to the
view’s `VStack`. Inside the `VStack` a red heart `Image` defines its own
`TapGesture` handler that also prints a message to the console, and a blue
rectangle with no custom gesture handlers. Tapping or clicking any of the
views results in a console message from the high priority gesture attached to
the enclosing `VStack`.

## See Also

### Defining custom gestures

`func defersSystemGestures(on: Edge.Set) -> some View`

Sets the screen edge from which you want your gesture to take precedence over
the system gesture.

`protocol Gesture`

An instance that matches a sequence of events to a gesture, and returns a
stream of values for each of its states.

`struct AnyGesture`

A type-erased gesture.

`struct HandActivationBehavior`

An activation behavior specific to hand-driven input.

Instance Method

# defersSystemGestures(on:)

Sets the screen edge from which you want your gesture to take precedence over
the system gesture.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+

    
    
    func defersSystemGestures(on edges: Edge.Set) -> some View
    

##  Parameters

`edges`

    

A value that indicates the screen edge from which you want your gesture to
take precedence over the system gesture.

## Discussion

The following code defers the vertical screen edges system gestures of a given
canvas.

## See Also

### Defining custom gestures

`func highPriorityGesture<T>(T, including: GestureMask) -> some View`

Attaches a gesture to the view with a higher precedence than gestures defined
by the view.

`protocol Gesture`

An instance that matches a sequence of events to a gesture, and returns a
stream of values for each of its states.

`struct AnyGesture`

A type-erased gesture.

`struct HandActivationBehavior`

An activation behavior specific to hand-driven input.

Protocol

# Gesture

An instance that matches a sequence of events to a gesture, and returns a
stream of values for each of its states.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    protocol Gesture<Value>

## Overview

Create custom gestures by declaring types that conform to the `Gesture`
protocol.

## Topics

### Implementing a custom gesture

`var body: Self.Body`

The content and behavior of the gesture.

**Required**

` associatedtype Body : Gesture`

The type of gesture representing the body of `Self`.

**Required**

### Performing the gesture

`func updating<State>(GestureState<State>, body: (Self.Value, inout State,
inout Transaction) -> Void) -> GestureStateGesture<Self, State>`

Updates the provided gesture state property as the gesture’s value changes.

`func onChanged((Self.Value) -> Void) -> _ChangedGesture<Self>`

Adds an action to perform when the gesture’s value changes.

Available when `Value` conforms to `Equatable`.

`func onEnded((Self.Value) -> Void) -> _EndedGesture<Self>`

Adds an action to perform when the gesture ends.

`associatedtype Value`

The type representing the gesture’s value.

**Required**

### Composing gestures

`func simultaneously<Other>(with: Other) -> SimultaneousGesture<Self, Other>`

Combines a gesture with another gesture to create a new gesture that
recognizes both gestures at the same time.

`func sequenced<Other>(before: Other) -> SequenceGesture<Self, Other>`

Sequences a gesture with another one to create a new gesture, which results in
the second gesture only receiving events after the first gesture succeeds.

`func exclusively<Other>(before: Other) -> ExclusiveGesture<Self, Other>`

Combines two gestures exclusively to create a new gesture where only one
gesture succeeds, giving precedence to the first gesture.

### Adding modifier keys to a gesture

`func modifiers(EventModifiers) -> _ModifiersGesture<Self>`

Combines a gesture with keyboard modifiers.

### Transforming a gesture

`func map<T>((Self.Value) -> T) -> _MapGesture<Self, T>`

Returns a gesture that’s the result of mapping the given closure over the
gesture.

### Customizing gesture activation

`func handActivationBehavior(HandActivationBehavior) -> some
Gesture<Self.Value> `

Customizes the activation behavior for a gesture when driven by hand or hand-
like input.

### Using a gesture with a RealityKit entity

`func targetedToAnyEntity() -> some Gesture<EntityTargetValue<Self.Value>> `

Require this gesture to target an entity.

`func targetedToEntity(Entity) -> some Gesture<EntityTargetValue<Self.Value>>
`

Require this gesture to target `entity` or a descendant of `entity`. This is
equivalent to `targetedToEntity(.descendingFrom(entity))`.

`func targetedToEntity(where: QueryPredicate<Entity>) -> some
Gesture<EntityTargetValue<Self.Value>> `

Require this gesture to target an entity that can be found in the results of
the specified QueryPredicate

## Relationships

### Conforming Types

  * `AnyGesture`
  * `DragGesture`
  * `ExclusiveGesture`
  * `GestureStateGesture`
  * `LongPressGesture`
  * `MagnificationGesture`
  * `MagnifyGesture`
  * `RotateGesture`
  * `RotateGesture3D`
  * `RotationGesture`
  * `SequenceGesture`
  * `SimultaneousGesture`
  * `SpatialEventGesture`
  * `SpatialTapGesture`
  * `TapGesture`

## See Also

### Defining custom gestures

`func highPriorityGesture<T>(T, including: GestureMask) -> some View`

Attaches a gesture to the view with a higher precedence than gestures defined
by the view.

`func defersSystemGestures(on: Edge.Set) -> some View`

Sets the screen edge from which you want your gesture to take precedence over
the system gesture.

`struct AnyGesture`

A type-erased gesture.

`struct HandActivationBehavior`

An activation behavior specific to hand-driven input.

Structure

# AnyGesture

A type-erased gesture.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct AnyGesture<Value>

## Topics

### Implementing a custom gesture

`init<T>(T)`

Creates an instance from another gesture.

## Relationships

### Conforms To

  * `Gesture`

## See Also

### Defining custom gestures

`func highPriorityGesture<T>(T, including: GestureMask) -> some View`

Attaches a gesture to the view with a higher precedence than gestures defined
by the view.

`func defersSystemGestures(on: Edge.Set) -> some View`

Sets the screen edge from which you want your gesture to take precedence over
the system gesture.

`protocol Gesture`

An instance that matches a sequence of events to a gesture, and returns a
stream of values for each of its states.

`struct HandActivationBehavior`

An activation behavior specific to hand-driven input.

Structure

# HandActivationBehavior

An activation behavior specific to hand-driven input.

visionOS 1.0+

    
    
    struct HandActivationBehavior

## Overview

Hand activation behavior determines what hand input modes activate a gesture.

## Topics

### Getting the behaviors

`static let automatic: HandActivationBehavior`

The default activation behavior, including direct touch, direct pinch, and
indirect pinch.

`static let pinch: HandActivationBehavior`

Activation that requires a pinched hand.

## Relationships

### Conforms To

  * `Equatable`

## See Also

### Defining custom gestures

`func highPriorityGesture<T>(T, including: GestureMask) -> some View`

Attaches a gesture to the view with a higher precedence than gestures defined
by the view.

`func defersSystemGestures(on: Edge.Set) -> some View`

Sets the screen edge from which you want your gesture to take precedence over
the system gesture.

`protocol Gesture`

An instance that matches a sequence of events to a gesture, and returns a
stream of values for each of its states.

`struct AnyGesture`

A type-erased gesture.

Structure

# GestureState

A property wrapper type that updates a property while the user performs a
gesture and resets the property back to its initial state when the gesture
ends.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @propertyWrapper @frozen
    struct GestureState<Value>

## Overview

Declare a property as `@GestureState`, pass as a binding to it as a parameter
to a gesture’s `updating(_:body:)` callback, and receive updates to it. A
property that’s declared as `@GestureState` implicitly resets when the gesture
becomes inactive, making it suitable for tracking transient state.

Add a long-press gesture to a `Circle`, and update the interface during the
gesture by declaring a property as `@GestureState`:

## Topics

### Creating a gesture state

`init(initialValue: Value)`

Creates a view state that’s derived from a gesture with an initial value.

`init(initialValue: Value, reset: (Value, inout Transaction) -> Void)`

Creates a view state that’s derived from a gesture with an initial state value
and a closure that provides a transaction to reset it.

`init(initialValue: Value, resetTransaction: Transaction)`

Creates a view state that’s derived from a gesture with an initial state value
and a transaction to reset it.

`init(reset: (Value, inout Transaction) -> Void)`

Creates a view state that’s derived from a gesture with a closure that
provides a transaction to reset it.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(resetTransaction: Transaction)`

Creates a view state that’s derived from a gesture with a transaction to reset
it.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(wrappedValue: Value)`

Creates a view state that’s derived from a gesture.

`init(wrappedValue: Value, reset: (Value, inout Transaction) -> Void)`

Creates a view state that’s derived from a gesture with a wrapped state value
and a closure that provides a transaction to reset it.

`init(wrappedValue: Value, resetTransaction: Transaction)`

Creates a view state that’s derived from a gesture with a wrapped state value
and a transaction to reset it.

### Getting the state

`var wrappedValue: Value`

The wrapped value referenced by the gesture state property.

`var projectedValue: GestureState<Value>`

A binding to the gesture state property.

## Relationships

### Conforms To

  * `DynamicProperty`

## See Also

### Managing gesture state

`struct GestureStateGesture`

A gesture that updates the state provided by a gesture’s updating callback.

Structure

# GestureStateGesture

A gesture that updates the state provided by a gesture’s updating callback.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct GestureStateGesture<Base, State> where Base : Gesture

## Overview

A gesture’s `updating(_:body:)` callback returns a `GestureStateGesture`
instance for updating a transient state property that’s annotated with the
`GestureState` property wrapper.

## Topics

### Creating an in-progress gesture

`init(base: Base, state: GestureState<State>, body: (GestureStateGesture<Base,
State>.Value, inout State, inout Transaction) -> Void)`

Creates a new gesture that’s the result of an ongoing gesture.

`var base: Base`

The originating gesture.

`var state: GestureState<State>`

A value that changes as the user performs the gesture.

### Supporting types

`var body: (GestureStateGesture<Base, State>.Value, inout State, inout
Transaction) -> Void`

The updating gesture containing the originating gesture’s value, the updated
state of the gesture, and a transaction.

## Relationships

### Conforms To

  * `Gesture`

## See Also

### Managing gesture state

`struct GestureState`

A property wrapper type that updates a property while the user performs a
gesture and resets the property back to its initial state when the gesture
ends.

Structure

# MagnificationGesture

A gesture that recognizes a magnification motion and tracks the amount of
magnification.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  visionOS 1.0+

    
    
    struct MagnificationGesture

Deprecated

Use `MagnifyGesture` instead.

## Topics

### Creating the gesture

`init(minimumScaleDelta: CGFloat)`

Creates a magnification gesture with a given minimum delta for the gesture to
start.

`var minimumScaleDelta: CGFloat`

The minimum required delta before the gesture starts.

## Relationships

### Conforms To

  * `Gesture`

## See Also

### Deprecated gestures

`struct RotationGesture`

A gesture that recognizes a rotation motion and tracks the angle of the
rotation.

Deprecated

Structure

# RotationGesture

A gesture that recognizes a rotation motion and tracks the angle of the
rotation.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  visionOS 1.0+

    
    
    struct RotationGesture

Deprecated

Use `RotateGesture` instead.

## Topics

### Creating the gesture

`init(minimumAngleDelta: Angle)`

Creates a rotation gesture with a minimum delta for the gesture to start.

`var minimumAngleDelta: Angle`

The minimum delta required before the gesture succeeds.

## Relationships

### Conforms To

  * `Gesture`

## See Also

### Deprecated gestures

`struct MagnificationGesture`

A gesture that recognizes a magnification motion and tracks the amount of
magnification.

Deprecated



# GeometryProxy

Instance Method

# bounds(of:)

Returns the given coordinate space’s bounds rectangle, converted to the local
coordinate space.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func bounds(of coordinateSpace: NamedCoordinateSpace) -> CGRect?

## See Also

### Accessing geometry characteristics

`func frame(in: CoordinateSpace) -> CGRect`

Returns the container view’s bounds rectangle, converted to a defined
coordinate space.

`func frame(in: some CoordinateSpaceProtocol) -> CGRect`

Returns the container view’s bounds rectangle, converted to a defined
coordinate space.

`var size: CGSize`

The size of the container view.

`var safeAreaInsets: EdgeInsets`

The safe area inset of the container view.

`subscript<T>(Anchor<T>) -> T`

Resolves the value of an anchor to the container view.

`func transform(in: some CoordinateSpaceProtocol) -> AffineTransform3D?`

The container view’s 3D transform converted to a defined coordinate space.

Instance Method

# frame(in:)

Returns the container view’s bounds rectangle, converted to a defined
coordinate space.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    func frame(in coordinateSpace: CoordinateSpace) -> CGRect

## See Also

### Accessing geometry characteristics

`func bounds(of: NamedCoordinateSpace) -> CGRect?`

Returns the given coordinate space’s bounds rectangle, converted to the local
coordinate space.

`func frame(in: some CoordinateSpaceProtocol) -> CGRect`

Returns the container view’s bounds rectangle, converted to a defined
coordinate space.

`var size: CGSize`

The size of the container view.

`var safeAreaInsets: EdgeInsets`

The safe area inset of the container view.

`subscript<T>(Anchor<T>) -> T`

Resolves the value of an anchor to the container view.

`func transform(in: some CoordinateSpaceProtocol) -> AffineTransform3D?`

The container view’s 3D transform converted to a defined coordinate space.

Instance Method

# frame(in:)

Returns the container view’s bounds rectangle, converted to a defined
coordinate space.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func frame(in coordinateSpace: some CoordinateSpaceProtocol) -> CGRect

## See Also

### Accessing geometry characteristics

`func bounds(of: NamedCoordinateSpace) -> CGRect?`

Returns the given coordinate space’s bounds rectangle, converted to the local
coordinate space.

`func frame(in: CoordinateSpace) -> CGRect`

Returns the container view’s bounds rectangle, converted to a defined
coordinate space.

`var size: CGSize`

The size of the container view.

`var safeAreaInsets: EdgeInsets`

The safe area inset of the container view.

`subscript<T>(Anchor<T>) -> T`

Resolves the value of an anchor to the container view.

`func transform(in: some CoordinateSpaceProtocol) -> AffineTransform3D?`

The container view’s 3D transform converted to a defined coordinate space.

Instance Property

# size

The size of the container view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var size: CGSize { get }

## See Also

### Accessing geometry characteristics

`func bounds(of: NamedCoordinateSpace) -> CGRect?`

Returns the given coordinate space’s bounds rectangle, converted to the local
coordinate space.

`func frame(in: CoordinateSpace) -> CGRect`

Returns the container view’s bounds rectangle, converted to a defined
coordinate space.

`func frame(in: some CoordinateSpaceProtocol) -> CGRect`

Returns the container view’s bounds rectangle, converted to a defined
coordinate space.

`var safeAreaInsets: EdgeInsets`

The safe area inset of the container view.

`subscript<T>(Anchor<T>) -> T`

Resolves the value of an anchor to the container view.

`func transform(in: some CoordinateSpaceProtocol) -> AffineTransform3D?`

The container view’s 3D transform converted to a defined coordinate space.

Instance Property

# safeAreaInsets

The safe area inset of the container view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var safeAreaInsets: EdgeInsets { get }

## See Also

### Accessing geometry characteristics

`func bounds(of: NamedCoordinateSpace) -> CGRect?`

Returns the given coordinate space’s bounds rectangle, converted to the local
coordinate space.

`func frame(in: CoordinateSpace) -> CGRect`

Returns the container view’s bounds rectangle, converted to a defined
coordinate space.

`func frame(in: some CoordinateSpaceProtocol) -> CGRect`

Returns the container view’s bounds rectangle, converted to a defined
coordinate space.

`var size: CGSize`

The size of the container view.

`subscript<T>(Anchor<T>) -> T`

Resolves the value of an anchor to the container view.

`func transform(in: some CoordinateSpaceProtocol) -> AffineTransform3D?`

The container view’s 3D transform converted to a defined coordinate space.

Instance Subscript

# subscript(_:)

Resolves the value of an anchor to the container view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    subscript<T>(anchor: Anchor<T>) -> T { get }

## See Also

### Accessing geometry characteristics

`func bounds(of: NamedCoordinateSpace) -> CGRect?`

Returns the given coordinate space’s bounds rectangle, converted to the local
coordinate space.

`func frame(in: CoordinateSpace) -> CGRect`

Returns the container view’s bounds rectangle, converted to a defined
coordinate space.

`func frame(in: some CoordinateSpaceProtocol) -> CGRect`

Returns the container view’s bounds rectangle, converted to a defined
coordinate space.

`var size: CGSize`

The size of the container view.

`var safeAreaInsets: EdgeInsets`

The safe area inset of the container view.

`func transform(in: some CoordinateSpaceProtocol) -> AffineTransform3D?`

The container view’s 3D transform converted to a defined coordinate space.

Instance Method

# transform(in:)

The container view’s 3D transform converted to a defined coordinate space.

visionOS 1.0+

    
    
    func transform(in coordinateSpace: some CoordinateSpaceProtocol) -> AffineTransform3D?

## Discussion

If the view doesn’t have a well defined transform, such as if it is affected
by a projection transform, this function may return `nil`.

## See Also

### Accessing geometry characteristics

`func bounds(of: NamedCoordinateSpace) -> CGRect?`

Returns the given coordinate space’s bounds rectangle, converted to the local
coordinate space.

`func frame(in: CoordinateSpace) -> CGRect`

Returns the container view’s bounds rectangle, converted to a defined
coordinate space.

`func frame(in: some CoordinateSpaceProtocol) -> CGRect`

Returns the container view’s bounds rectangle, converted to a defined
coordinate space.

`var size: CGSize`

The size of the container view.

`var safeAreaInsets: EdgeInsets`

The safe area inset of the container view.

`subscript<T>(Anchor<T>) -> T`

Resolves the value of an anchor to the container view.



# Group

Initializer

# init(content:)

Creates a group of views.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(@ViewBuilder content: () -> Content)

Available when `Content` conforms to `View`.

##  Parameters

`content`

    

A `ViewBuilder` that produces the views to group.

## See Also

### Creating a group

`init(content: () -> Content)`

Creates a group of scenes.

Available when `Content` conforms to `Scene`.

`init(content: () -> Content)`

Creates a group of commands.

Available when `Content` conforms to `Commands`.

`init(content: () -> Content)`

Creates a group of toolbar content instances.

Available when `Content` conforms to `ToolbarContent`.

`init(content: () -> Content)`

Creates a group of customizable toolbar content instances.

Available when `Content` conforms to `CustomizableToolbarContent`.

`init<R>(content: () -> Content)`

Creates a group of table rows.

Available when `Content` conforms to `TableRowContent`.

`init<R, C>(content: () -> Content)`

Creates a group of table columns.

Available when `Content` conforms to `TableColumnContent`.

`init(content: () -> Content)`

Creates an instance that generates Rotor content by combining, in order, all
the Rotor content specified in the passed-in result builder.

Available when `Content` conforms to `AccessibilityRotorContent`.

Initializer

# init(content:)

Creates a group of scenes.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(@SceneBuilder content: () -> Content)

Available when `Content` conforms to `Scene`.

##  Parameters

`content`

    

A `SceneBuilder` that produces the scenes to group.

## See Also

### Creating a group

`init(content: () -> Content)`

Creates a group of views.

Available when `Content` conforms to `View`.

`init(content: () -> Content)`

Creates a group of commands.

Available when `Content` conforms to `Commands`.

`init(content: () -> Content)`

Creates a group of toolbar content instances.

Available when `Content` conforms to `ToolbarContent`.

`init(content: () -> Content)`

Creates a group of customizable toolbar content instances.

Available when `Content` conforms to `CustomizableToolbarContent`.

`init<R>(content: () -> Content)`

Creates a group of table rows.

Available when `Content` conforms to `TableRowContent`.

`init<R, C>(content: () -> Content)`

Creates a group of table columns.

Available when `Content` conforms to `TableColumnContent`.

`init(content: () -> Content)`

Creates an instance that generates Rotor content by combining, in order, all
the Rotor content specified in the passed-in result builder.

Available when `Content` conforms to `AccessibilityRotorContent`.

Initializer

# init(content:)

Creates a group of commands.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    init(@CommandsBuilder content: () -> Content)

Available when `Content` conforms to `Commands`.

##  Parameters

`content`

    

A `CommandsBuilder` that produces the commands to group.

## See Also

### Creating a group

`init(content: () -> Content)`

Creates a group of views.

Available when `Content` conforms to `View`.

`init(content: () -> Content)`

Creates a group of scenes.

Available when `Content` conforms to `Scene`.

`init(content: () -> Content)`

Creates a group of toolbar content instances.

Available when `Content` conforms to `ToolbarContent`.

`init(content: () -> Content)`

Creates a group of customizable toolbar content instances.

Available when `Content` conforms to `CustomizableToolbarContent`.

`init<R>(content: () -> Content)`

Creates a group of table rows.

Available when `Content` conforms to `TableRowContent`.

`init<R, C>(content: () -> Content)`

Creates a group of table columns.

Available when `Content` conforms to `TableColumnContent`.

`init(content: () -> Content)`

Creates an instance that generates Rotor content by combining, in order, all
the Rotor content specified in the passed-in result builder.

Available when `Content` conforms to `AccessibilityRotorContent`.

Initializer

# init(content:)

Creates a group of toolbar content instances.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(@ToolbarContentBuilder content: () -> Content)

Available when `Content` conforms to `ToolbarContent`.

##  Parameters

`content`

    

A `ToolbarContentBuilder` that produces the toolbar content instances to
group.

## See Also

### Creating a group

`init(content: () -> Content)`

Creates a group of views.

Available when `Content` conforms to `View`.

`init(content: () -> Content)`

Creates a group of scenes.

Available when `Content` conforms to `Scene`.

`init(content: () -> Content)`

Creates a group of commands.

Available when `Content` conforms to `Commands`.

`init(content: () -> Content)`

Creates a group of customizable toolbar content instances.

Available when `Content` conforms to `CustomizableToolbarContent`.

`init<R>(content: () -> Content)`

Creates a group of table rows.

Available when `Content` conforms to `TableRowContent`.

`init<R, C>(content: () -> Content)`

Creates a group of table columns.

Available when `Content` conforms to `TableColumnContent`.

`init(content: () -> Content)`

Creates an instance that generates Rotor content by combining, in order, all
the Rotor content specified in the passed-in result builder.

Available when `Content` conforms to `AccessibilityRotorContent`.

Initializer

# init(content:)

Creates a group of customizable toolbar content instances.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(@ToolbarContentBuilder content: () -> Content)

Available when `Content` conforms to `CustomizableToolbarContent`.

##  Parameters

`content`

    

A `ToolbarContentBuilder` that produces the customizable toolbar content
instances to group.

## See Also

### Creating a group

`init(content: () -> Content)`

Creates a group of views.

Available when `Content` conforms to `View`.

`init(content: () -> Content)`

Creates a group of scenes.

Available when `Content` conforms to `Scene`.

`init(content: () -> Content)`

Creates a group of commands.

Available when `Content` conforms to `Commands`.

`init(content: () -> Content)`

Creates a group of toolbar content instances.

Available when `Content` conforms to `ToolbarContent`.

`init<R>(content: () -> Content)`

Creates a group of table rows.

Available when `Content` conforms to `TableRowContent`.

`init<R, C>(content: () -> Content)`

Creates a group of table columns.

Available when `Content` conforms to `TableColumnContent`.

`init(content: () -> Content)`

Creates an instance that generates Rotor content by combining, in order, all
the Rotor content specified in the passed-in result builder.

Available when `Content` conforms to `AccessibilityRotorContent`.

Initializer

# init(content:)

Creates a group of table rows.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<R>(@TableRowBuilder<R> content: () -> Content) where R == Content.TableRowValue

Available when `Content` conforms to `TableRowContent`.

##  Parameters

`content`

    

A `TableRowBuilder` that produces the rows to group.

## See Also

### Creating a group

`init(content: () -> Content)`

Creates a group of views.

Available when `Content` conforms to `View`.

`init(content: () -> Content)`

Creates a group of scenes.

Available when `Content` conforms to `Scene`.

`init(content: () -> Content)`

Creates a group of commands.

Available when `Content` conforms to `Commands`.

`init(content: () -> Content)`

Creates a group of toolbar content instances.

Available when `Content` conforms to `ToolbarContent`.

`init(content: () -> Content)`

Creates a group of customizable toolbar content instances.

Available when `Content` conforms to `CustomizableToolbarContent`.

`init<R, C>(content: () -> Content)`

Creates a group of table columns.

Available when `Content` conforms to `TableColumnContent`.

`init(content: () -> Content)`

Creates an instance that generates Rotor content by combining, in order, all
the Rotor content specified in the passed-in result builder.

Available when `Content` conforms to `AccessibilityRotorContent`.

Initializer

# init(content:)

Creates a group of table columns.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<R, C>(@TableColumnBuilder<R, C> content: () -> Content) where R == Content.TableRowValue, C == Content.TableColumnSortComparator

Available when `Content` conforms to `TableColumnContent`.

##  Parameters

`content`

    

A `TableColumnBuilder` that produces the columns to group.

## See Also

### Creating a group

`init(content: () -> Content)`

Creates a group of views.

Available when `Content` conforms to `View`.

`init(content: () -> Content)`

Creates a group of scenes.

Available when `Content` conforms to `Scene`.

`init(content: () -> Content)`

Creates a group of commands.

Available when `Content` conforms to `Commands`.

`init(content: () -> Content)`

Creates a group of toolbar content instances.

Available when `Content` conforms to `ToolbarContent`.

`init(content: () -> Content)`

Creates a group of customizable toolbar content instances.

Available when `Content` conforms to `CustomizableToolbarContent`.

`init<R>(content: () -> Content)`

Creates a group of table rows.

Available when `Content` conforms to `TableRowContent`.

`init(content: () -> Content)`

Creates an instance that generates Rotor content by combining, in order, all
the Rotor content specified in the passed-in result builder.

Available when `Content` conforms to `AccessibilityRotorContent`.

Initializer

# init(content:)

Creates an instance that generates Rotor content by combining, in order, all
the Rotor content specified in the passed-in result builder.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init(@AccessibilityRotorContentBuilder content: () -> Content)

Available when `Content` conforms to `AccessibilityRotorContent`.

##  Parameters

`content`

    

The result builder that generates Rotor content for the group.

## See Also

### Creating a group

`init(content: () -> Content)`

Creates a group of views.

Available when `Content` conforms to `View`.

`init(content: () -> Content)`

Creates a group of scenes.

Available when `Content` conforms to `Scene`.

`init(content: () -> Content)`

Creates a group of commands.

Available when `Content` conforms to `Commands`.

`init(content: () -> Content)`

Creates a group of toolbar content instances.

Available when `Content` conforms to `ToolbarContent`.

`init(content: () -> Content)`

Creates a group of customizable toolbar content instances.

Available when `Content` conforms to `CustomizableToolbarContent`.

`init<R>(content: () -> Content)`

Creates a group of table rows.

Available when `Content` conforms to `TableRowContent`.

`init<R, C>(content: () -> Content)`

Creates a group of table columns.

Available when `Content` conforms to `TableColumnContent`.

Initializer

# init(content:)

Creates a group of map content.

MapKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    init(@MapContentBuilder content: () -> Content)

Available when `Content` conforms to `MapContent`.

##  Parameters

`content`

    

A map content builder that produces the map content to group.

Collection

API Collection

# MapContent Implementations

## Topics

### Instance Methods

`func annotationSubtitles(Visibility) -> some MapContent`

Sets the visibility of subtitles for markers and annotations.

`func annotationTitles(Visibility) -> some MapContent`

Sets the visibility of titles for markers and annotations.

`func foregroundStyle(some ShapeStyle) -> some MapContent`

Specifies the shape style used to fill content in drawing map overlays.

`func mapOverlayLevel(level: MKOverlayLevel) -> some MapContent`

Specifies the position of overlays relative to other map content.

`func stroke(some ShapeStyle, lineWidth: CGFloat) -> some MapContent`

Applies the given shape style to drawn map overlays.

`func stroke(some ShapeStyle, style: StrokeStyle) -> some MapContent`

Applies the given shape style to drawn map overlays.

`func stroke(lineWidth: CGFloat) -> some MapContent`

Sets the line width used for drawing map overlays.

`func strokeStyle(style: StrokeStyle) -> some MapContent`

Applies the given stroke style to drawn map overlays.

`func tag<V>(V) -> some MapContent`

Sets the unique tag value of this piece of map content.

`func tint<S>(S) -> some MapContent`

The tint shape style to apply to map content.



# GlobalCoordinateSpace

Initializer

# init()

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init()



# GaugeStyleConfiguration

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



# Gradient.ColorSpace

Type Property

# device

Interpolates gradient colors in the output color space.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static let device: Gradient.ColorSpace

## See Also

### Getting an interpolation method

`static let perceptual: Gradient.ColorSpace`

Interpolates gradient colors in a perceptual color space.

Type Property

# perceptual

Interpolates gradient colors in a perceptual color space.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static let perceptual: Gradient.ColorSpace

## See Also

### Getting an interpolation method

`static let device: Gradient.ColorSpace`

Interpolates gradient colors in the output color space.



# GraphicsContext.ShadowOptions

Type Property

# disablesGroup

An option that causes the filter to composite the object and its shadow
separately in the current layer.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var disablesGroup: GraphicsContext.ShadowOptions { get }

## See Also

### Getting shadow options

`static var invertsAlpha: GraphicsContext.ShadowOptions`

An option that causes the filter to invert the alpha of the shadow.

`static var shadowAbove: GraphicsContext.ShadowOptions`

An option that causes the filter to draw the shadow above the object, rather
than below it.

`static var shadowOnly: GraphicsContext.ShadowOptions`

An option that causes the filter to draw only the shadow, and omit the source
object.

Type Property

# invertsAlpha

An option that causes the filter to invert the alpha of the shadow.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var invertsAlpha: GraphicsContext.ShadowOptions { get }

## Discussion

You can create an “inner shadow” effect by combining this option with
`shadowAbove` and using the `sourceAtop` blend mode.

## See Also

### Getting shadow options

`static var disablesGroup: GraphicsContext.ShadowOptions`

An option that causes the filter to composite the object and its shadow
separately in the current layer.

`static var shadowAbove: GraphicsContext.ShadowOptions`

An option that causes the filter to draw the shadow above the object, rather
than below it.

`static var shadowOnly: GraphicsContext.ShadowOptions`

An option that causes the filter to draw only the shadow, and omit the source
object.

Type Property

# shadowAbove

An option that causes the filter to draw the shadow above the object, rather
than below it.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var shadowAbove: GraphicsContext.ShadowOptions { get }

## See Also

### Getting shadow options

`static var disablesGroup: GraphicsContext.ShadowOptions`

An option that causes the filter to composite the object and its shadow
separately in the current layer.

`static var invertsAlpha: GraphicsContext.ShadowOptions`

An option that causes the filter to invert the alpha of the shadow.

`static var shadowOnly: GraphicsContext.ShadowOptions`

An option that causes the filter to draw only the shadow, and omit the source
object.

Type Property

# shadowOnly

An option that causes the filter to draw only the shadow, and omit the source
object.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var shadowOnly: GraphicsContext.ShadowOptions { get }

## See Also

### Getting shadow options

`static var disablesGroup: GraphicsContext.ShadowOptions`

An option that causes the filter to composite the object and its shadow
separately in the current layer.

`static var invertsAlpha: GraphicsContext.ShadowOptions`

An option that causes the filter to invert the alpha of the shadow.

`static var shadowAbove: GraphicsContext.ShadowOptions`

An option that causes the filter to draw the shadow above the object, rather
than below it.



# GraphicsContext.GradientOptions

Type Property

# linearColor

An option that interpolates between colors in a linear color space.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var linearColor: GraphicsContext.GradientOptions { get }

## See Also

### Getting gradient options

`static var mirror: GraphicsContext.GradientOptions`

An option that repeats the gradient outside its nominal range, reflecting
every other instance.

`static var `repeat`: GraphicsContext.GradientOptions`

An option that repeats the gradient outside its nominal range.

Type Property

# mirror

An option that repeats the gradient outside its nominal range, reflecting
every other instance.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var mirror: GraphicsContext.GradientOptions { get }

## Discussion

Use this option to cause the gradient to repeat its pattern in areas that
exceed the bounds of its start and end points. The repetitions alternately
reverse the start and end points, producing a pattern like `0 -> 1`, `1 -> 0`,
`0 -> 1`, and so on.

Without either this option or `repeat`, the gradient stops at the end of its
range. This option takes precendence if you set both this one and `repeat`.

## See Also

### Getting gradient options

`static var linearColor: GraphicsContext.GradientOptions`

An option that interpolates between colors in a linear color space.

`static var `repeat`: GraphicsContext.GradientOptions`

An option that repeats the gradient outside its nominal range.

Type Property

# repeat

An option that repeats the gradient outside its nominal range.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var `repeat`: GraphicsContext.GradientOptions { get }

## Discussion

Use this option to cause the gradient to repeat its pattern in areas that
exceed the bounds of its start and end points. The repetitions use the same
start and end value for each repetition.

Without this option or `mirror`, the gradient stops at the end of its range.
The `mirror` option takes precendence if you set both this one and that one.

## See Also

### Getting gradient options

`static var linearColor: GraphicsContext.GradientOptions`

An option that interpolates between colors in a linear color space.

`static var mirror: GraphicsContext.GradientOptions`

An option that repeats the gradient outside its nominal range, reflecting
every other instance.



# GestureStateGesture

Initializer

# init(base:state:body:)

Creates a new gesture that’s the result of an ongoing gesture.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        base: Base,
        state: GestureState<State>,
        body: @escaping (GestureStateGesture<Base, State>.Value, inout State, inout Transaction) -> Void
    )

##  Parameters

`base`

    

The originating gesture.

`state`

    

The wrapped value of a `GestureState` property.

`body`

    

The callback that SwiftUI invokes as the gesture’s value changes.

## See Also

### Creating an in-progress gesture

`var base: Base`

The originating gesture.

`var state: GestureState<State>`

A value that changes as the user performs the gesture.

Instance Property

# base

The originating gesture.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var base: Base

## See Also

### Creating an in-progress gesture

`init(base: Base, state: GestureState<State>, body: (GestureStateGesture<Base,
State>.Value, inout State, inout Transaction) -> Void)`

Creates a new gesture that’s the result of an ongoing gesture.

`var state: GestureState<State>`

A value that changes as the user performs the gesture.

Instance Property

# state

A value that changes as the user performs the gesture.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var state: GestureState<State>

## See Also

### Creating an in-progress gesture

`init(base: Base, state: GestureState<State>, body: (GestureStateGesture<Base,
State>.Value, inout State, inout Transaction) -> Void)`

Creates a new gesture that’s the result of an ongoing gesture.

`var base: Base`

The originating gesture.

Instance Property

# body

The updating gesture containing the originating gesture’s value, the updated
state of the gesture, and a transaction.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var body: (GestureStateGesture<Base, State>.Value, inout State, inout Transaction) -> Void



# GeometryProxy3D

Instance Method

# frame(in:)

The container view’s bounds rectangle converted to a defined coordinate space.

visionOS 1.0+

    
    
    func frame(in coordinateSpace: some CoordinateSpaceProtocol) -> Rect3D

## See Also

### Accessing geometry characteristics

`var size: Size3D`

The size of the container view.

`var safeAreaInsets: EdgeInsets3D`

The safe area inset of the container view.

`subscript<T>(Anchor<T>) -> T`

Resolves the value of an anchor to the container view.

`func transform(in: some CoordinateSpaceProtocol) -> AffineTransform3D?`

The container view’s 3D transform converted to a defined coordinate space.

Instance Property

# size

The size of the container view.

visionOS 1.0+

    
    
    var size: Size3D { get }

## See Also

### Accessing geometry characteristics

`func frame(in: some CoordinateSpaceProtocol) -> Rect3D`

The container view’s bounds rectangle converted to a defined coordinate space.

`var safeAreaInsets: EdgeInsets3D`

The safe area inset of the container view.

`subscript<T>(Anchor<T>) -> T`

Resolves the value of an anchor to the container view.

`func transform(in: some CoordinateSpaceProtocol) -> AffineTransform3D?`

The container view’s 3D transform converted to a defined coordinate space.

Instance Property

# safeAreaInsets

The safe area inset of the container view.

visionOS 1.0+

    
    
    var safeAreaInsets: EdgeInsets3D { get }

## See Also

### Accessing geometry characteristics

`func frame(in: some CoordinateSpaceProtocol) -> Rect3D`

The container view’s bounds rectangle converted to a defined coordinate space.

`var size: Size3D`

The size of the container view.

`subscript<T>(Anchor<T>) -> T`

Resolves the value of an anchor to the container view.

`func transform(in: some CoordinateSpaceProtocol) -> AffineTransform3D?`

The container view’s 3D transform converted to a defined coordinate space.

Instance Subscript

# subscript(_:)

Resolves the value of an anchor to the container view.

visionOS 1.0+

    
    
    subscript<T>(anchor: Anchor<T>) -> T { get }

## See Also

### Accessing geometry characteristics

`func frame(in: some CoordinateSpaceProtocol) -> Rect3D`

The container view’s bounds rectangle converted to a defined coordinate space.

`var size: Size3D`

The size of the container view.

`var safeAreaInsets: EdgeInsets3D`

The safe area inset of the container view.

`func transform(in: some CoordinateSpaceProtocol) -> AffineTransform3D?`

The container view’s 3D transform converted to a defined coordinate space.

Instance Method

# transform(in:)

The container view’s 3D transform converted to a defined coordinate space.

visionOS 1.0+

    
    
    func transform(in coordinateSpace: some CoordinateSpaceProtocol) -> AffineTransform3D?

## Discussion

If the view doesn’t have a well-defined transform, such as if it’s affected by
a projection transform, this function may return `nil`.

## See Also

### Accessing geometry characteristics

`func frame(in: some CoordinateSpaceProtocol) -> Rect3D`

The container view’s bounds rectangle converted to a defined coordinate space.

`var size: Size3D`

The size of the container view.

`var safeAreaInsets: EdgeInsets3D`

The safe area inset of the container view.

`subscript<T>(Anchor<T>) -> T`

Resolves the value of an anchor to the container view.



# GraphicsContext.BlurOptions

Type Property

# dithersResult

An option that causes the filter to dither the result, to reduce banding.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var dithersResult: GraphicsContext.BlurOptions { get }

## See Also

### Getting blur options

`static var opaque: GraphicsContext.BlurOptions`

An option that causes the filter to ensure the result is completely opaque.

Type Property

# opaque

An option that causes the filter to ensure the result is completely opaque.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var opaque: GraphicsContext.BlurOptions { get }

## Discussion

The filter ensure opacity by dividing each pixel by its alpha value. The
result may be undefined if the input to the filter isn’t also completely
opaque.

## See Also

### Getting blur options

`static var dithersResult: GraphicsContext.BlurOptions`

An option that causes the filter to dither the result, to reduce banding.



# GroupedFormStyle

Initializer

# init()

Creates a form style with scrolling, grouped rows.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init()

## Discussion

Don’t call this initializer directly. Instead, use the `grouped` static
variable to create this style:



# GeometryReader3D

Initializer

# init(content:)

visionOS 1.0+

    
    
    init(@ViewBuilder content: @escaping (GeometryProxy3D) -> Content)

## See Also

### Creating a geometry reader

`var content: (GeometryProxy3D) -> Content`

Instance Property

# content

visionOS 1.0+

    
    
    var content: (GeometryProxy3D) -> Content

## See Also

### Creating a geometry reader

`init(content: (GeometryProxy3D) -> Content)`



# GroupBox

Initializer

# init(content:)

Creates an unlabeled group box with the provided view content.

iOS 14.0+  iPadOS 14.0+  macOS 10.15+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    init(@ViewBuilder content: () -> Content)

Available when `Label` is `EmptyView` and `Content` conforms to `View`.

##  Parameters

`content`

    

A `ViewBuilder` that produces the content for the group box.

## See Also

### Creating a group box

`init(content: () -> Content, label: () -> Label)`

Creates a group box with the provided label and view content.

`init(LocalizedStringKey, content: () -> Content)`

Creates a group box with the provided view content and title.

Available when `Label` is `Text` and `Content` conforms to `View`.

`init<S>(S, content: () -> Content)`

Creates a group box with the provided view content.

Available when `Label` is `Text` and `Content` conforms to `View`.

Initializer

# init(content:label:)

Creates a group box with the provided label and view content.

iOS 14.0+  iPadOS 14.0+  macOS 10.15+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    init(
        @ViewBuilder content: () -> Content,
        @ViewBuilder label: () -> Label
    )

##  Parameters

`content`

    

A `ViewBuilder` that produces the content for the group box.

`label`

    

A `ViewBuilder` that produces a label for the group box.

## See Also

### Creating a group box

`init(content: () -> Content)`

Creates an unlabeled group box with the provided view content.

Available when `Label` is `EmptyView` and `Content` conforms to `View`.

`init(LocalizedStringKey, content: () -> Content)`

Creates a group box with the provided view content and title.

Available when `Label` is `Text` and `Content` conforms to `View`.

`init<S>(S, content: () -> Content)`

Creates a group box with the provided view content.

Available when `Label` is `Text` and `Content` conforms to `View`.

Initializer

# init(_:content:)

Creates a group box with the provided view content and title.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        @ViewBuilder content: () -> Content
    )

Available when `Label` is `Text` and `Content` conforms to `View`.

##  Parameters

`titleKey`

    

The key for the group box’s title, which describes the content of the group
box.

`content`

    

A `ViewBuilder` that produces the content for the group box.

## See Also

### Creating a group box

`init(content: () -> Content)`

Creates an unlabeled group box with the provided view content.

Available when `Label` is `EmptyView` and `Content` conforms to `View`.

`init(content: () -> Content, label: () -> Label)`

Creates a group box with the provided label and view content.

`init<S>(S, content: () -> Content)`

Creates a group box with the provided view content.

Available when `Label` is `Text` and `Content` conforms to `View`.

Initializer

# init(_:content:)

Creates a group box with the provided view content.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        @ViewBuilder content: () -> Content
    ) where S : StringProtocol

Available when `Label` is `Text` and `Content` conforms to `View`.

##  Parameters

`title`

    

A string that describes the content of the group box.

`content`

    

A `ViewBuilder` that produces the content for the group box.

## See Also

### Creating a group box

`init(content: () -> Content)`

Creates an unlabeled group box with the provided view content.

Available when `Label` is `EmptyView` and `Content` conforms to `View`.

`init(content: () -> Content, label: () -> Label)`

Creates a group box with the provided label and view content.

`init(LocalizedStringKey, content: () -> Content)`

Creates a group box with the provided view content and title.

Available when `Label` is `Text` and `Content` conforms to `View`.

Initializer

# init(_:)

Creates a group box based on a style configuration.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    init(_ configuration: GroupBoxStyleConfiguration)

Available when `Label` is `GroupBoxStyleConfiguration.Label` and `Content` is
`GroupBoxStyleConfiguration.Content`.

##  Parameters

`configuration`

    

The properties of the group box instance being created.

## Discussion

Use this initializer within the `makeBody(configuration:)` method of a
`GroupBoxStyle` instance to create a styled group box, with customizations,
while preserving its existing style.

The following example adds a pink border around the group box, without
overriding its current style:

Initializer

# init(label:content:)

iOS 14.0–17.4  Deprecated  iPadOS 14.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 14.0–17.4  Deprecated  visionOS 1.0+

    
    
    init(
        label: Label,
        @ViewBuilder content: () -> Content
    )

Available when `Label` conforms to `View` and `Content` conforms to `View`.



# GlassBackgroundDisplayMode

Case

# GlassBackgroundDisplayMode.always

Always display the glass material.

visionOS 1.0+

    
    
    case always

## See Also

### Getting the mode

`case implicit`

Display the glass material only when the view isn’t already contained in
glass.

`case never`

Never display the glass material.

Case

# GlassBackgroundDisplayMode.implicit

Display the glass material only when the view isn’t already contained in
glass.

visionOS 1.0+

    
    
    case implicit

## Discussion

Use this value to avoid duplicate backgrounds when a view that has a glass
background contains another view that also has a glass background.

This display mode doesn’t suppress duplicate glass backgrounds for views that
are offset by any amount in the z-axis. For example, the two subviews of the
following `HStack` behave differently:

The first instance of `MyView` doesn’t display a background because its
container displays one. However the second instance does display a background
because that view is offset from its container by 100 points along the z-axis.

## See Also

### Getting the mode

`case always`

Always display the glass material.

`case never`

Never display the glass material.

Case

# GlassBackgroundDisplayMode.never

Never display the glass material.

visionOS 1.0+

    
    
    case never

## See Also

### Getting the mode

`case always`

Always display the glass material.

`case implicit`

Display the glass material only when the view isn’t already contained in
glass.



# GraphicsContext

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



# GraphicalDatePickerStyle

Initializer

# init()

Creates an instance of the graphical date picker style.

iOS 14.0+  iPadOS 14.0+  macOS 10.15+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    init()



# GraphicsContext.ResolvedText

Instance Method

# firstBaseline(in:)

Gets the distance from the first line’s ascender to its baseline.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func firstBaseline(in size: CGSize) -> CGFloat

## See Also

### Getting the text properties

`func lastBaseline(in: CGSize) -> CGFloat`

Gets the distance from the first line’s ascender to the last line’s baseline.

`func measure(in: CGSize) -> CGSize`

Measures the size of the resolved text for a given area into which the text
should be placed.

`var shading: GraphicsContext.Shading`

The shading to fill uncolored text regions with.

Instance Method

# lastBaseline(in:)

Gets the distance from the first line’s ascender to the last line’s baseline.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func lastBaseline(in size: CGSize) -> CGFloat

## See Also

### Getting the text properties

`func firstBaseline(in: CGSize) -> CGFloat`

Gets the distance from the first line’s ascender to its baseline.

`func measure(in: CGSize) -> CGSize`

Measures the size of the resolved text for a given area into which the text
should be placed.

`var shading: GraphicsContext.Shading`

The shading to fill uncolored text regions with.

Instance Method

# measure(in:)

Measures the size of the resolved text for a given area into which the text
should be placed.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func measure(in size: CGSize) -> CGSize

##  Parameters

`size`

    

The area to place the `Text` view in.

## See Also

### Getting the text properties

`func firstBaseline(in: CGSize) -> CGFloat`

Gets the distance from the first line’s ascender to its baseline.

`func lastBaseline(in: CGSize) -> CGFloat`

Gets the distance from the first line’s ascender to the last line’s baseline.

`var shading: GraphicsContext.Shading`

The shading to fill uncolored text regions with.

Instance Property

# shading

The shading to fill uncolored text regions with.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var shading: GraphicsContext.Shading

## Discussion

This value defaults to the `foreground` shading.

## See Also

### Getting the text properties

`func firstBaseline(in: CGSize) -> CGFloat`

Gets the distance from the first line’s ascender to its baseline.

`func lastBaseline(in: CGSize) -> CGFloat`

Gets the distance from the first line’s ascender to the last line’s baseline.

`func measure(in: CGSize) -> CGSize`

Measures the size of the resolved text for a given area into which the text
should be placed.



# GraphicsContext.ResolvedImage

Instance Property

# size

The size of the image.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var size: CGSize { get }

## See Also

### Getting the image properties

`let baseline: CGFloat`

The distance from the top of the image to its baseline.

`var shading: GraphicsContext.Shading?`

An optional shading to fill the image with.

Instance Property

# baseline

The distance from the top of the image to its baseline.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    let baseline: CGFloat

## Discussion

If the image has no baseline, this value is equivalent to the image’s height.

## See Also

### Getting the image properties

`var size: CGSize`

The size of the image.

`var shading: GraphicsContext.Shading?`

An optional shading to fill the image with.

Instance Property

# shading

An optional shading to fill the image with.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var shading: GraphicsContext.Shading?

## Discussion

The value of this property defaults to `foreground` for template images, and
to `nil` otherwise.

## See Also

### Getting the image properties

`var size: CGSize`

The size of the image.

`let baseline: CGFloat`

The distance from the top of the image to its baseline.



# GraphicsContext.Filter

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



# Gesture

Instance Property

# body

The content and behavior of the gesture.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var body: Self.Body { get }

**Required**

## See Also

### Implementing a custom gesture

`associatedtype Body : Gesture`

The type of gesture representing the body of `Self`.

**Required**

Associated Type

# Body

The type of gesture representing the body of `Self`.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    associatedtype Body : Gesture

**Required**

## See Also

### Implementing a custom gesture

`var body: Self.Body`

The content and behavior of the gesture.

**Required**

Instance Method

# updating(_:body:)

Updates the provided gesture state property as the gesture’s value changes.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func updating<State>(
        _ state: GestureState<State>,
        body: @escaping (Self.Value, inout State, inout Transaction) -> Void
    ) -> GestureStateGesture<Self, State>

##  Parameters

`state`

    

A binding to a view’s `GestureState` property.

`body`

    

The callback that SwiftUI invokes as the gesture’s value changes. Its
`currentState` parameter is the updated state of the gesture. The
`gestureState` parameter is the previous state of the gesture, and the
`transaction` is the context of the gesture.

## Return Value

A version of the gesture that updates the provided `state` as the originating
gesture’s value changes and that resets the `state` to its initial value when
the user or the system ends or cancels the gesture.

## Discussion

Use this callback to update transient UI state as described in Adding
interactivity with gestures.

## See Also

### Performing the gesture

`func onChanged((Self.Value) -> Void) -> _ChangedGesture<Self>`

Adds an action to perform when the gesture’s value changes.

Available when `Value` conforms to `Equatable`.

`func onEnded((Self.Value) -> Void) -> _EndedGesture<Self>`

Adds an action to perform when the gesture ends.

`associatedtype Value`

The type representing the gesture’s value.

**Required**

Instance Method

# onChanged(_:)

Adds an action to perform when the gesture’s value changes.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func onChanged(_ action: @escaping (Self.Value) -> Void) -> _ChangedGesture<Self>

Available when `Value` conforms to `Equatable`.

##  Parameters

`action`

    

The action to perform when this gesture’s value changes. The `action`
closure’s parameter contains the gesture’s new value.

## Return Value

A gesture that triggers `action` when this gesture’s value changes.

## See Also

### Performing the gesture

`func updating<State>(GestureState<State>, body: (Self.Value, inout State,
inout Transaction) -> Void) -> GestureStateGesture<Self, State>`

Updates the provided gesture state property as the gesture’s value changes.

`func onEnded((Self.Value) -> Void) -> _EndedGesture<Self>`

Adds an action to perform when the gesture ends.

`associatedtype Value`

The type representing the gesture’s value.

**Required**

Instance Method

# onEnded(_:)

Adds an action to perform when the gesture ends.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func onEnded(_ action: @escaping (Self.Value) -> Void) -> _EndedGesture<Self>

##  Parameters

`action`

    

The action to perform when this gesture ends. The `action` closure’s parameter
contains the final value of the gesture.

## Return Value

A gesture that triggers `action` when the gesture ends.

## See Also

### Performing the gesture

`func updating<State>(GestureState<State>, body: (Self.Value, inout State,
inout Transaction) -> Void) -> GestureStateGesture<Self, State>`

Updates the provided gesture state property as the gesture’s value changes.

`func onChanged((Self.Value) -> Void) -> _ChangedGesture<Self>`

Adds an action to perform when the gesture’s value changes.

Available when `Value` conforms to `Equatable`.

`associatedtype Value`

The type representing the gesture’s value.

**Required**

Associated Type

# Value

The type representing the gesture’s value.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    associatedtype Value

**Required**

## See Also

### Performing the gesture

`func updating<State>(GestureState<State>, body: (Self.Value, inout State,
inout Transaction) -> Void) -> GestureStateGesture<Self, State>`

Updates the provided gesture state property as the gesture’s value changes.

`func onChanged((Self.Value) -> Void) -> _ChangedGesture<Self>`

Adds an action to perform when the gesture’s value changes.

Available when `Value` conforms to `Equatable`.

`func onEnded((Self.Value) -> Void) -> _EndedGesture<Self>`

Adds an action to perform when the gesture ends.

Instance Method

# simultaneously(with:)

Combines a gesture with another gesture to create a new gesture that
recognizes both gestures at the same time.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func simultaneously<Other>(with other: Other) -> SimultaneousGesture<Self, Other> where Other : Gesture

##  Parameters

`other`

    

A gesture that you want to combine with your gesture to create a new, combined
gesture.

## Return Value

A gesture with two simultaneous gestures.

## See Also

### Composing gestures

`func sequenced<Other>(before: Other) -> SequenceGesture<Self, Other>`

Sequences a gesture with another one to create a new gesture, which results in
the second gesture only receiving events after the first gesture succeeds.

`func exclusively<Other>(before: Other) -> ExclusiveGesture<Self, Other>`

Combines two gestures exclusively to create a new gesture where only one
gesture succeeds, giving precedence to the first gesture.

Instance Method

# sequenced(before:)

Sequences a gesture with another one to create a new gesture, which results in
the second gesture only receiving events after the first gesture succeeds.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func sequenced<Other>(before other: Other) -> SequenceGesture<Self, Other> where Other : Gesture

##  Parameters

`other`

    

A gesture you want to combine with another gesture to create a new, sequenced
gesture.

## Return Value

A gesture that’s a sequence of two gestures.

## See Also

### Composing gestures

`func simultaneously<Other>(with: Other) -> SimultaneousGesture<Self, Other>`

Combines a gesture with another gesture to create a new gesture that
recognizes both gestures at the same time.

`func exclusively<Other>(before: Other) -> ExclusiveGesture<Self, Other>`

Combines two gestures exclusively to create a new gesture where only one
gesture succeeds, giving precedence to the first gesture.

Instance Method

# exclusively(before:)

Combines two gestures exclusively to create a new gesture where only one
gesture succeeds, giving precedence to the first gesture.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func exclusively<Other>(before other: Other) -> ExclusiveGesture<Self, Other> where Other : Gesture

##  Parameters

`other`

    

A gesture you combine with your gesture, to create a new, combined gesture.

## Return Value

A gesture that’s the result of combining two gestures where only one of them
can succeed. SwiftUI gives precedence to the first gesture.

## See Also

### Composing gestures

`func simultaneously<Other>(with: Other) -> SimultaneousGesture<Self, Other>`

Combines a gesture with another gesture to create a new gesture that
recognizes both gestures at the same time.

`func sequenced<Other>(before: Other) -> SequenceGesture<Self, Other>`

Sequences a gesture with another one to create a new gesture, which results in
the second gesture only receiving events after the first gesture succeeds.

Instance Method

# modifiers(_:)

Combines a gesture with keyboard modifiers.

macOS 10.15+

    
    
    func modifiers(_ modifiers: EventModifiers) -> _ModifiersGesture<Self>

##  Parameters

`modifiers`

    

A set of flags that correspond to the modifier keys that the user needs to
hold down.

## Return Value

A new gesture that combines a gesture with keyboard modifiers.

## Discussion

The gesture receives updates while the user presses the modifier keys that
correspond to the given modifiers option set.

Instance Method

# map(_:)

Returns a gesture that’s the result of mapping the given closure over the
gesture.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func map<T>(_ body: @escaping (Self.Value) -> T) -> _MapGesture<Self, T>

Instance Method

# handActivationBehavior(_:)

Customizes the activation behavior for a gesture when driven by hand or hand-
like input.

visionOS 1.0+

    
    
    func handActivationBehavior(_ behavior: HandActivationBehavior) -> some Gesture<Self.Value>
    

##  Parameters

`behavior`

    

The hand activation behavior to use for the gesture.

## Return Value

A new gesture with a preference to activate with the provided behavior.

## Discussion

Use `automatic` to allow a gesture to activate with default system behaviors.
Use `pinch` when a gesture should only trigger when the hand is pinched.

For example, in a 3D chess application, a `DragGesture` that enables movement
of the pieces could use the pinch behavior to ensure that piece movement is
only possible when a hand is pinched in order to avoid pushing the piece
around by only touching it:

Instance Method

# targetedToAnyEntity()

Require this gesture to target an entity.

RealityKit  SwiftUI  visionOS 1.0+

    
    
    func targetedToAnyEntity() -> some Gesture<EntityTargetValue<Self.Value>>
    

## Return Value

A `RealityCoordinateSpaceConvertible`value containing the original gesture
value along with the targeted entity.

## See Also

### Using a gesture with a RealityKit entity

`func targetedToEntity(Entity) -> some Gesture<EntityTargetValue<Self.Value>>
`

Require this gesture to target `entity` or a descendant of `entity`. This is
equivalent to `targetedToEntity(.descendingFrom(entity))`.

`func targetedToEntity(where: QueryPredicate<Entity>) -> some
Gesture<EntityTargetValue<Self.Value>> `

Require this gesture to target an entity that can be found in the results of
the specified QueryPredicate

Instance Method

# targetedToEntity(_:)

Require this gesture to target `entity` or a descendant of `entity`. This is
equivalent to `targetedToEntity(.descendingFrom(entity))`.

RealityKit  SwiftUI  visionOS 1.0+

    
    
    func targetedToEntity(_ entity: Entity) -> some Gesture<EntityTargetValue<Self.Value>>
    

##  Parameters

`entity`

    

The entity the gesture should target.

## Return Value

A `RealityCoordinateSpaceConverting` value containing the original gesture
value along with the targeted entity.

## See Also

### Using a gesture with a RealityKit entity

`func targetedToAnyEntity() -> some Gesture<EntityTargetValue<Self.Value>> `

Require this gesture to target an entity.

`func targetedToEntity(where: QueryPredicate<Entity>) -> some
Gesture<EntityTargetValue<Self.Value>> `

Require this gesture to target an entity that can be found in the results of
the specified QueryPredicate

Instance Method

# targetedToEntity(where:)

Require this gesture to target an entity that can be found in the results of
the specified QueryPredicate

RealityKit  SwiftUI  visionOS 1.0+

    
    
    func targetedToEntity(where query: QueryPredicate<Entity>) -> some Gesture<EntityTargetValue<Self.Value>>
    

##  Parameters

`query`

    

a `QueryPredicate<Entity>` to filter which entity the gesture should target

## Return Value

A `RealityCoordinateSpaceConverting` value containing the original gesture
value along with the targeted entity.

## See Also

### Using a gesture with a RealityKit entity

`func targetedToAnyEntity() -> some Gesture<EntityTargetValue<Self.Value>> `

Require this gesture to target an entity.

`func targetedToEntity(Entity) -> some Gesture<EntityTargetValue<Self.Value>>
`

Require this gesture to target `entity` or a descendant of `entity`. This is
equivalent to `targetedToEntity(.descendingFrom(entity))`.



# GaugeStyle

Type Property

# automatic

The default gauge view style in the current context of the view being styled.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 7.0+
visionOS 1.0+

    
    
    static var automatic: DefaultGaugeStyle { get }

Available when `Self` is `DefaultGaugeStyle`.

Type Property

# circular

A gauge style that displays an open ring with a marker that appears at a point
along the ring to indicate the gauge’s current value.

watchOS 7.0+

    
    
    static var circular: CircularGaugeStyle { get }

Available when `Self` is `CircularGaugeStyle`.

## Discussion

Apply this style to a `Gauge` or to a view hierarchy that contains gauges
using the `gaugeStyle(_:)` modifier:

This style displays the gauge’s `currentValueLabel` value at the center of the
gauge. If you provide `minimumValueLabel` and `maximumValueLabel` parameters
when you create the gauge, they appear in the opening at the bottom of the
ring. Otherwise, the gauge places its label in that location.

## See Also

### Getting circular gauge styles

`static var accessoryCircular: AccessoryCircularGaugeStyle`

A gauge style that displays an open ring with a marker that appears at a point
along the ring to indicate the gauge’s current value.

Available when `Self` is `AccessoryCircularGaugeStyle`.

`static var accessoryCircularCapacity: AccessoryCircularCapacityGaugeStyle`

A gauge style that displays a closed ring that’s partially filled in to
indicate the gauge’s current value.

Available when `Self` is `AccessoryCircularCapacityGaugeStyle`.

Type Property

# accessoryCircular

A gauge style that displays an open ring with a marker that appears at a point
along the ring to indicate the gauge’s current value.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    static var accessoryCircular: AccessoryCircularGaugeStyle { get }

Available when `Self` is `AccessoryCircularGaugeStyle`.

## Discussion

Apply this style to a `Gauge` or to a view hierarchy that contains gauges
using the `gaugeStyle(_:)` modifier:

This style displays the gauge’s `currentValueLabel` value at the center of the
gauge. If you provide `minimumValueLabel` and `maximumValueLabel` parameters
when you create the gauge, they appear in the opening at the bottom of the
ring. Otherwise, the gauge places its label in that location.

## See Also

### Getting circular gauge styles

`static var circular: CircularGaugeStyle`

A gauge style that displays an open ring with a marker that appears at a point
along the ring to indicate the gauge’s current value.

Available when `Self` is `CircularGaugeStyle`.

`static var accessoryCircularCapacity: AccessoryCircularCapacityGaugeStyle`

A gauge style that displays a closed ring that’s partially filled in to
indicate the gauge’s current value.

Available when `Self` is `AccessoryCircularCapacityGaugeStyle`.

Type Property

# accessoryCircularCapacity

A gauge style that displays a closed ring that’s partially filled in to
indicate the gauge’s current value.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    static var accessoryCircularCapacity: AccessoryCircularCapacityGaugeStyle { get }

Available when `Self` is `AccessoryCircularCapacityGaugeStyle`.

## Discussion

Apply this style to a `Gauge` or to a view hierarchy that contains gauges
using the `gaugeStyle(_:)` modifier:

This style displays the gauge’s `currentValueLabel` value at the center of the
gauge.

## See Also

### Getting circular gauge styles

`static var circular: CircularGaugeStyle`

A gauge style that displays an open ring with a marker that appears at a point
along the ring to indicate the gauge’s current value.

Available when `Self` is `CircularGaugeStyle`.

`static var accessoryCircular: AccessoryCircularGaugeStyle`

A gauge style that displays an open ring with a marker that appears at a point
along the ring to indicate the gauge’s current value.

Available when `Self` is `AccessoryCircularGaugeStyle`.

Type Property

# linear

A gauge style that displays a bar with a marker that appears at a point along
the bar to indicate the gauge’s current value.

watchOS 7.0+

    
    
    static var linear: LinearGaugeStyle { get }

Available when `Self` is `LinearGaugeStyle`.

## Discussion

Apply this style to a `Gauge` or to a view hierarchy that contains gauges
using the `gaugeStyle(_:)` modifier:

If you provide `minimumValueLabel` and `maximumValueLabel` parameters when you
create the gauge, they appear on leading and trailing edges of the bar,
respectively. Otherwise, the gauge displays the `currentValueLabel` value on
the leading edge.

## See Also

### Getting linear gauge styles

`static var linearCapacity: LinearCapacityGaugeStyle`

A gauge style that displays a bar that fills from leading to trailing edges as
the gauge’s current value increases.

Available when `Self` is `LinearCapacityGaugeStyle`.

`static var accessoryLinear: AccessoryLinearGaugeStyle`

A gauge style that displays bar with a marker that appears at a point along
the bar to indicate the gauge’s current value.

Available when `Self` is `AccessoryLinearGaugeStyle`.

`static var accessoryLinearCapacity: AccessoryLinearCapacityGaugeStyle`

A gauge style that displays bar that fills from leading to trailing edges as
the gauge’s current value increases.

Available when `Self` is `AccessoryLinearCapacityGaugeStyle`.

Type Property

# linearCapacity

A gauge style that displays a bar that fills from leading to trailing edges as
the gauge’s current value increases.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    static var linearCapacity: LinearCapacityGaugeStyle { get }

Available when `Self` is `LinearCapacityGaugeStyle`.

## Discussion

Apply this style to a `Gauge` or to a view hierarchy that contains gauges
using the `gaugeStyle(_:)` modifier:

If you provide `minimumValueLabel` and `maximumValueLabel` parameters when you
create the gauge, they appear on leading and trailing edges of the bar,
respectively. The `label` appears above the gauge, and the `currentValueLabel`
appears below.

## See Also

### Getting linear gauge styles

`static var linear: LinearGaugeStyle`

A gauge style that displays a bar with a marker that appears at a point along
the bar to indicate the gauge’s current value.

Available when `Self` is `LinearGaugeStyle`.

`static var accessoryLinear: AccessoryLinearGaugeStyle`

A gauge style that displays bar with a marker that appears at a point along
the bar to indicate the gauge’s current value.

Available when `Self` is `AccessoryLinearGaugeStyle`.

`static var accessoryLinearCapacity: AccessoryLinearCapacityGaugeStyle`

A gauge style that displays bar that fills from leading to trailing edges as
the gauge’s current value increases.

Available when `Self` is `AccessoryLinearCapacityGaugeStyle`.

Type Property

# accessoryLinear

A gauge style that displays bar with a marker that appears at a point along
the bar to indicate the gauge’s current value.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    static var accessoryLinear: AccessoryLinearGaugeStyle { get }

Available when `Self` is `AccessoryLinearGaugeStyle`.

## Discussion

Apply this style to a `Gauge` or to a view hierarchy that contains gauges
using the `gaugeStyle(_:)` modifier:

If you provide `minimumValueLabel` and `maximumValueLabel` parameters when you
create the gauge, they appear on leading and trailing edges of the bar,
respectively. Otherwise, the gauge displays the `currentValueLabel` value on
the leading edge.

## See Also

### Getting linear gauge styles

`static var linear: LinearGaugeStyle`

A gauge style that displays a bar with a marker that appears at a point along
the bar to indicate the gauge’s current value.

Available when `Self` is `LinearGaugeStyle`.

`static var linearCapacity: LinearCapacityGaugeStyle`

A gauge style that displays a bar that fills from leading to trailing edges as
the gauge’s current value increases.

Available when `Self` is `LinearCapacityGaugeStyle`.

`static var accessoryLinearCapacity: AccessoryLinearCapacityGaugeStyle`

A gauge style that displays bar that fills from leading to trailing edges as
the gauge’s current value increases.

Available when `Self` is `AccessoryLinearCapacityGaugeStyle`.

Type Property

# accessoryLinearCapacity

A gauge style that displays bar that fills from leading to trailing edges as
the gauge’s current value increases.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    static var accessoryLinearCapacity: AccessoryLinearCapacityGaugeStyle { get }

Available when `Self` is `AccessoryLinearCapacityGaugeStyle`.

## Discussion

Apply this style to a `Gauge` or to a view hierarchy that contains gauges
using the `gaugeStyle(_:)` modifier:

If you provide `minimumValueLabel` and `maximumValueLabel` parameters when you
create the gauge, they appear on leading and trailing edges of the bar,
respectively. The `label` appears above the gauge, and the `currentValueLabel`
appears below.

## See Also

### Getting linear gauge styles

`static var linear: LinearGaugeStyle`

A gauge style that displays a bar with a marker that appears at a point along
the bar to indicate the gauge’s current value.

Available when `Self` is `LinearGaugeStyle`.

`static var linearCapacity: LinearCapacityGaugeStyle`

A gauge style that displays a bar that fills from leading to trailing edges as
the gauge’s current value increases.

Available when `Self` is `LinearCapacityGaugeStyle`.

`static var accessoryLinear: AccessoryLinearGaugeStyle`

A gauge style that displays bar with a marker that appears at a point along
the bar to indicate the gauge’s current value.

Available when `Self` is `AccessoryLinearGaugeStyle`.

Instance Method

# makeBody(configuration:)

Creates a view representing the body of a gauge.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 7.0+
visionOS 1.0+

    
    
    @ViewBuilder
    func makeBody(configuration: Self.Configuration) -> Self.Body

**Required**

##  Parameters

`configuration`

    

The properties to apply to the gauge instance.

## Discussion

The system calls this modifier on each instance of gauge within a view
hierarchy where this style is the current gauge style.

## See Also

### Creating custom gauge styles

`typealias Configuration`

The properties of a gauge instance.

`associatedtype Body : View`

A view representing the body of a gauge.

**Required**

Type Alias

# GaugeStyle.Configuration

The properties of a gauge instance.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 7.0+
visionOS 1.0+

    
    
    typealias Configuration = GaugeStyleConfiguration

## See Also

### Creating custom gauge styles

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Creates a view representing the body of a gauge.

**Required**

` associatedtype Body : View`

A view representing the body of a gauge.

**Required**

Associated Type

# Body

A view representing the body of a gauge.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 7.0+
visionOS 1.0+

    
    
    associatedtype Body : View

**Required**

## See Also

### Creating custom gauge styles

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Creates a view representing the body of a gauge.

**Required**

` typealias Configuration`

The properties of a gauge instance.

Structure

# DefaultGaugeStyle

The default gauge view style in the current context of the view being styled.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 7.0+
visionOS 1.0+

    
    
    struct DefaultGaugeStyle

## Overview

You can also use `automatic` to construct this style.

## Topics

### Creating the gauge style

`init()`

Creates a default gauge style.

## Relationships

### Conforms To

  * `GaugeStyle`

## See Also

### Supporting types

`struct CircularGaugeStyle`

A gauge style that displays an open ring with a marker that appears at a point
along the ring to indicate the gauge’s current value.

`struct AccessoryCircularGaugeStyle`

A gauge style that displays an open ring with a marker that appears at a point
along the ring to indicate the gauge’s current value.

`struct AccessoryCircularCapacityGaugeStyle`

A gauge style that displays a closed ring that’s partially filled in to
indicate the gauge’s current value.

`struct LinearGaugeStyle`

A gauge style that displays a bar with a marker that appears at a point along
the bar to indicate the gauge’s current value.

`struct LinearCapacityGaugeStyle`

A gauge style that displays bar that fills from leading to trailing edges as
the gauge’s current value increases.

`struct AccessoryLinearGaugeStyle`

A gauge style that displays bar with a marker that appears at a point along
the bar to indicate the gauge’s current value.

`struct AccessoryLinearCapacityGaugeStyle`

A gauge style that displays bar that fills from leading to trailing edges as
the gauge’s current value increases.

Structure

# CircularGaugeStyle

A gauge style that displays an open ring with a marker that appears at a point
along the ring to indicate the gauge’s current value.

watchOS 7.0+

    
    
    struct CircularGaugeStyle

## Overview

Use `circular` to construct this style.

## Topics

### Creating the gauge style

`init()`

Creates a circular gauge.

`init(tint: Color)`

Creates a circular gauge that draws with a specified color.

`init(tint: Gradient)`

Creates a circular gauge that draws with a specified gradient.

## Relationships

### Conforms To

  * `GaugeStyle`

## See Also

### Supporting types

`struct DefaultGaugeStyle`

The default gauge view style in the current context of the view being styled.

`struct AccessoryCircularGaugeStyle`

A gauge style that displays an open ring with a marker that appears at a point
along the ring to indicate the gauge’s current value.

`struct AccessoryCircularCapacityGaugeStyle`

A gauge style that displays a closed ring that’s partially filled in to
indicate the gauge’s current value.

`struct LinearGaugeStyle`

A gauge style that displays a bar with a marker that appears at a point along
the bar to indicate the gauge’s current value.

`struct LinearCapacityGaugeStyle`

A gauge style that displays bar that fills from leading to trailing edges as
the gauge’s current value increases.

`struct AccessoryLinearGaugeStyle`

A gauge style that displays bar with a marker that appears at a point along
the bar to indicate the gauge’s current value.

`struct AccessoryLinearCapacityGaugeStyle`

A gauge style that displays bar that fills from leading to trailing edges as
the gauge’s current value increases.

Structure

# AccessoryCircularGaugeStyle

A gauge style that displays an open ring with a marker that appears at a point
along the ring to indicate the gauge’s current value.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    struct AccessoryCircularGaugeStyle

## Overview

Use `accessoryCircular` to construct this style.

## Topics

### Creating the gauge style

`init()`

Creates an accessory circular gauge style.

## Relationships

### Conforms To

  * `GaugeStyle`

## See Also

### Supporting types

`struct DefaultGaugeStyle`

The default gauge view style in the current context of the view being styled.

`struct CircularGaugeStyle`

A gauge style that displays an open ring with a marker that appears at a point
along the ring to indicate the gauge’s current value.

`struct AccessoryCircularCapacityGaugeStyle`

A gauge style that displays a closed ring that’s partially filled in to
indicate the gauge’s current value.

`struct LinearGaugeStyle`

A gauge style that displays a bar with a marker that appears at a point along
the bar to indicate the gauge’s current value.

`struct LinearCapacityGaugeStyle`

A gauge style that displays bar that fills from leading to trailing edges as
the gauge’s current value increases.

`struct AccessoryLinearGaugeStyle`

A gauge style that displays bar with a marker that appears at a point along
the bar to indicate the gauge’s current value.

`struct AccessoryLinearCapacityGaugeStyle`

A gauge style that displays bar that fills from leading to trailing edges as
the gauge’s current value increases.

Structure

# AccessoryCircularCapacityGaugeStyle

A gauge style that displays a closed ring that’s partially filled in to
indicate the gauge’s current value.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    struct AccessoryCircularCapacityGaugeStyle

## Overview

Use `accessoryCircularCapacity` to construct this style.

## Topics

### Creating the gauge style

`init()`

Creates an accessory circular capacity gauge style.

## Relationships

### Conforms To

  * `GaugeStyle`

## See Also

### Supporting types

`struct DefaultGaugeStyle`

The default gauge view style in the current context of the view being styled.

`struct CircularGaugeStyle`

A gauge style that displays an open ring with a marker that appears at a point
along the ring to indicate the gauge’s current value.

`struct AccessoryCircularGaugeStyle`

A gauge style that displays an open ring with a marker that appears at a point
along the ring to indicate the gauge’s current value.

`struct LinearGaugeStyle`

A gauge style that displays a bar with a marker that appears at a point along
the bar to indicate the gauge’s current value.

`struct LinearCapacityGaugeStyle`

A gauge style that displays bar that fills from leading to trailing edges as
the gauge’s current value increases.

`struct AccessoryLinearGaugeStyle`

A gauge style that displays bar with a marker that appears at a point along
the bar to indicate the gauge’s current value.

`struct AccessoryLinearCapacityGaugeStyle`

A gauge style that displays bar that fills from leading to trailing edges as
the gauge’s current value increases.

Structure

# LinearGaugeStyle

A gauge style that displays a bar with a marker that appears at a point along
the bar to indicate the gauge’s current value.

watchOS 7.0+

    
    
    struct LinearGaugeStyle

## Overview

Use `linear` to construct this style.

## Topics

### Creating the gauge style

`init()`

Creates a linear gauge style.

### Deprecated initializers

`init(tint: Color)`

Creates a linear gauge style with a tint color.

Deprecated

`init(tint: Gradient)`

Creates a linear gauge style with a tint gradient.

Deprecated

## Relationships

### Conforms To

  * `GaugeStyle`

## See Also

### Supporting types

`struct DefaultGaugeStyle`

The default gauge view style in the current context of the view being styled.

`struct CircularGaugeStyle`

A gauge style that displays an open ring with a marker that appears at a point
along the ring to indicate the gauge’s current value.

`struct AccessoryCircularGaugeStyle`

A gauge style that displays an open ring with a marker that appears at a point
along the ring to indicate the gauge’s current value.

`struct AccessoryCircularCapacityGaugeStyle`

A gauge style that displays a closed ring that’s partially filled in to
indicate the gauge’s current value.

`struct LinearCapacityGaugeStyle`

A gauge style that displays bar that fills from leading to trailing edges as
the gauge’s current value increases.

`struct AccessoryLinearGaugeStyle`

A gauge style that displays bar with a marker that appears at a point along
the bar to indicate the gauge’s current value.

`struct AccessoryLinearCapacityGaugeStyle`

A gauge style that displays bar that fills from leading to trailing edges as
the gauge’s current value increases.

Structure

# LinearCapacityGaugeStyle

A gauge style that displays bar that fills from leading to trailing edges as
the gauge’s current value increases.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    struct LinearCapacityGaugeStyle

## Overview

Use `linearCapacity` to construct this style.

## Topics

### Creating the gauge style

`init()`

Creates a linear capacity gauge style.

## Relationships

### Conforms To

  * `GaugeStyle`

## See Also

### Supporting types

`struct DefaultGaugeStyle`

The default gauge view style in the current context of the view being styled.

`struct CircularGaugeStyle`

A gauge style that displays an open ring with a marker that appears at a point
along the ring to indicate the gauge’s current value.

`struct AccessoryCircularGaugeStyle`

A gauge style that displays an open ring with a marker that appears at a point
along the ring to indicate the gauge’s current value.

`struct AccessoryCircularCapacityGaugeStyle`

A gauge style that displays a closed ring that’s partially filled in to
indicate the gauge’s current value.

`struct LinearGaugeStyle`

A gauge style that displays a bar with a marker that appears at a point along
the bar to indicate the gauge’s current value.

`struct AccessoryLinearGaugeStyle`

A gauge style that displays bar with a marker that appears at a point along
the bar to indicate the gauge’s current value.

`struct AccessoryLinearCapacityGaugeStyle`

A gauge style that displays bar that fills from leading to trailing edges as
the gauge’s current value increases.

Structure

# AccessoryLinearGaugeStyle

A gauge style that displays bar with a marker that appears at a point along
the bar to indicate the gauge’s current value.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    struct AccessoryLinearGaugeStyle

## Overview

Use `accessoryLinear` to construct this style.

## Topics

### Creating the gauge style

`init()`

Creates an accessory linear gauge style.

## Relationships

### Conforms To

  * `GaugeStyle`

## See Also

### Supporting types

`struct DefaultGaugeStyle`

The default gauge view style in the current context of the view being styled.

`struct CircularGaugeStyle`

A gauge style that displays an open ring with a marker that appears at a point
along the ring to indicate the gauge’s current value.

`struct AccessoryCircularGaugeStyle`

A gauge style that displays an open ring with a marker that appears at a point
along the ring to indicate the gauge’s current value.

`struct AccessoryCircularCapacityGaugeStyle`

A gauge style that displays a closed ring that’s partially filled in to
indicate the gauge’s current value.

`struct LinearGaugeStyle`

A gauge style that displays a bar with a marker that appears at a point along
the bar to indicate the gauge’s current value.

`struct LinearCapacityGaugeStyle`

A gauge style that displays bar that fills from leading to trailing edges as
the gauge’s current value increases.

`struct AccessoryLinearCapacityGaugeStyle`

A gauge style that displays bar that fills from leading to trailing edges as
the gauge’s current value increases.

Structure

# AccessoryLinearCapacityGaugeStyle

A gauge style that displays bar that fills from leading to trailing edges as
the gauge’s current value increases.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    struct AccessoryLinearCapacityGaugeStyle

## Overview

Use `accessoryLinearCapacity` to construct this style.

## Topics

### Creating the gauge style

`init()`

Creates an accessory linear capacity gauge style.

## Relationships

### Conforms To

  * `GaugeStyle`

## See Also

### Supporting types

`struct DefaultGaugeStyle`

The default gauge view style in the current context of the view being styled.

`struct CircularGaugeStyle`

A gauge style that displays an open ring with a marker that appears at a point
along the ring to indicate the gauge’s current value.

`struct AccessoryCircularGaugeStyle`

A gauge style that displays an open ring with a marker that appears at a point
along the ring to indicate the gauge’s current value.

`struct AccessoryCircularCapacityGaugeStyle`

A gauge style that displays a closed ring that’s partially filled in to
indicate the gauge’s current value.

`struct LinearGaugeStyle`

A gauge style that displays a bar with a marker that appears at a point along
the bar to indicate the gauge’s current value.

`struct LinearCapacityGaugeStyle`

A gauge style that displays bar that fills from leading to trailing edges as
the gauge’s current value increases.

`struct AccessoryLinearGaugeStyle`

A gauge style that displays bar with a marker that appears at a point along
the bar to indicate the gauge’s current value.



# GeometryReader

Initializer

# init(content:)

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(@ViewBuilder content: @escaping (GeometryProxy) -> Content)

## See Also

### Creating a geometry reader

`var content: (GeometryProxy) -> Content`

Instance Property

# content

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var content: (GeometryProxy) -> Content

## See Also

### Creating a geometry reader

`init(content: (GeometryProxy) -> Content)`



# GridRow

Initializer

# init(alignment:content:)

Creates a horizontal row of child views in a grid.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init(
        alignment: VerticalAlignment? = nil,
        @ViewBuilder content: () -> Content
    )

##  Parameters

`alignment`

    

An optional `VerticalAlignment` for the row. If you don’t specify a value, the
row uses the vertical alignment component of the `Alignment` parameter that
you specify in the grid’s
`init(alignment:horizontalSpacing:verticalSpacing:content:)` initializer,
which is `center` by default.

`content`

    

The builder closure that contains the child views. Each view in the closure
implicitly maps to a cell in the grid.

## Discussion

Use this initializer to create a `GridRow` inside of a `Grid`. Provide a
content closure that defines the cells of the row, and optionally customize
the vertical alignment of content within each cell. The following example
customizes the vertical alignment of the cells in the first and third rows:

The example above specifies `trailing` alignment for the grid, which is
composed of `center` vertical alignment and `trailing` horizontal alignment.
The middle row relies on the center vertical alignment, but the other two rows
specify custom vertical alignments:

Important

A grid row behaves like a `Group` if you create it outside of a grid.

To override column alignment, use `gridColumnAlignment(_:)`. To override
alignment for a single cell, use `gridCellAnchor(_:)`.



# GridItem

Initializer

# init(_:spacing:alignment:)

Creates a grid item with the specified size, spacing, and alignment.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(
        _ size: GridItem.Size = .flexible(),
        spacing: CGFloat? = nil,
        alignment: Alignment? = nil
    )

##  Parameters

`size`

    

The size of the grid item.

`spacing`

    

The spacing to use between this and the next item.

`alignment`

    

The alignment to use for this grid item.

Instance Property

# alignment

The alignment to use when placing each view.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    var alignment: Alignment?

## Discussion

Use this property to anchor the view’s relative position to the same relative
position in the view’s assigned grid space.

## See Also

### Inspecting grid item properties

`var spacing: CGFloat?`

The spacing to the next item.

`var size: GridItem.Size`

The size of the item, which is the width of a column item or the height of a
row item.

`enum Size`

The size in the minor axis of one or more rows or columns in a grid layout.

Instance Property

# spacing

The spacing to the next item.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    var spacing: CGFloat?

## Discussion

If this value is `nil`, the item uses a reasonable default for the current
platform.

## See Also

### Inspecting grid item properties

`var alignment: Alignment?`

The alignment to use when placing each view.

`var size: GridItem.Size`

The size of the item, which is the width of a column item or the height of a
row item.

`enum Size`

The size in the minor axis of one or more rows or columns in a grid layout.

Instance Property

# size

The size of the item, which is the width of a column item or the height of a
row item.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    var size: GridItem.Size

## See Also

### Inspecting grid item properties

`var alignment: Alignment?`

The alignment to use when placing each view.

`var spacing: CGFloat?`

The spacing to the next item.

`enum Size`

The size in the minor axis of one or more rows or columns in a grid layout.

Enumeration

# GridItem.Size

The size in the minor axis of one or more rows or columns in a grid layout.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    enum Size

## Overview

Use a `Size` instance when you create a `GridItem`. The value tells a
`LazyHGrid` how to size its rows, or a `LazyVGrid` how to size its columns.

## Topics

### Getting the sizes

`case adaptive(minimum: CGFloat, maximum: CGFloat)`

Multiple items in the space of a single flexible item.

`case fixed(CGFloat)`

A single item with the specified fixed size.

`case flexible(minimum: CGFloat, maximum: CGFloat)`

A single flexible item.

## Relationships

### Conforms To

  * `Sendable`

## See Also

### Inspecting grid item properties

`var alignment: Alignment?`

The alignment to use when placing each view.

`var spacing: CGFloat?`

The spacing to the next item.

`var size: GridItem.Size`

The size of the item, which is the width of a column item or the height of a
row item.



# Gauge

Initializer

# init(value:in:label:)

Creates a gauge showing a value within a range and describes the gauge’s
purpose and current value.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 7.0+
visionOS 1.0+

    
    
    init<V>(
        value: V,
        in bounds: ClosedRange<V> = 0...1,
        @ViewBuilder label: () -> Label
    ) where CurrentValueLabel == EmptyView, BoundsLabel == EmptyView, MarkedValueLabels == EmptyView, V : BinaryFloatingPoint

##  Parameters

`value`

    

The value to show in the gauge.

`bounds`

    

The range of the valid values. Defaults to `0...1`.

`label`

    

A view that describes the purpose of the gauge.

## Discussion

Use this modifier to create a gauge that shows the value at its relative
position along the gauge and a label describing the gauge’s purpose. In the
example below, the gauge has a range of `0...1`, the indicator is set to
`0.4`, or 40 percent of the distance along the gauge:

## See Also

### Creating a gauge

`init<V>(value: V, in: ClosedRange<V>, label: () -> Label, currentValueLabel:
() -> CurrentValueLabel)`

Creates a gauge showing a value within a range and that describes the gauge’s
purpose and current value.

`init<V>(value: V, in: ClosedRange<V>, label: () -> Label, currentValueLabel:
() -> CurrentValueLabel, markedValueLabels: () -> MarkedValueLabels)`

Creates a gauge representing a value within a range.

`init<V>(value: V, in: ClosedRange<V>, label: () -> Label, currentValueLabel:
() -> CurrentValueLabel, minimumValueLabel: () -> BoundsLabel,
maximumValueLabel: () -> BoundsLabel)`

Creates a gauge showing a value within a range and describes the gauge’s
current, minimum, and maximum values.

`init<V>(value: V, in: ClosedRange<V>, label: () -> Label, currentValueLabel:
() -> CurrentValueLabel, minimumValueLabel: () -> BoundsLabel,
maximumValueLabel: () -> BoundsLabel, markedValueLabels: () ->
MarkedValueLabels)`

Creates a gauge representing a value within a range.

Initializer

# init(value:in:label:currentValueLabel:)

Creates a gauge showing a value within a range and that describes the gauge’s
purpose and current value.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 7.0+
visionOS 1.0+

    
    
    init<V>(
        value: V,
        in bounds: ClosedRange<V> = 0...1,
        @ViewBuilder label: () -> Label,
        @ViewBuilder currentValueLabel: () -> CurrentValueLabel
    ) where BoundsLabel == EmptyView, MarkedValueLabels == EmptyView, V : BinaryFloatingPoint

##  Parameters

`value`

    

The value to show on the gauge.

`bounds`

    

The range of the valid values. Defaults to `0...1`.

`label`

    

A view that describes the purpose of the gauge.

`currentValueLabel`

    

A view that describes the current value of the gauge.

## Discussion

Use this method to create a gauge that displays a value within a range you
supply with labels that describe the purpose of the gauge and its current
value. In the example below, a gauge using the `circular` style shows its
current value of `67` along with a label describing the (BPM) for the gauge:

## See Also

### Creating a gauge

`init<V>(value: V, in: ClosedRange<V>, label: () -> Label)`

Creates a gauge showing a value within a range and describes the gauge’s
purpose and current value.

`init<V>(value: V, in: ClosedRange<V>, label: () -> Label, currentValueLabel:
() -> CurrentValueLabel, markedValueLabels: () -> MarkedValueLabels)`

Creates a gauge representing a value within a range.

`init<V>(value: V, in: ClosedRange<V>, label: () -> Label, currentValueLabel:
() -> CurrentValueLabel, minimumValueLabel: () -> BoundsLabel,
maximumValueLabel: () -> BoundsLabel)`

Creates a gauge showing a value within a range and describes the gauge’s
current, minimum, and maximum values.

`init<V>(value: V, in: ClosedRange<V>, label: () -> Label, currentValueLabel:
() -> CurrentValueLabel, minimumValueLabel: () -> BoundsLabel,
maximumValueLabel: () -> BoundsLabel, markedValueLabels: () ->
MarkedValueLabels)`

Creates a gauge representing a value within a range.

Initializer

# init(value:in:label:currentValueLabel:markedValueLabels:)

Creates a gauge representing a value within a range.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 7.0+
visionOS 1.0+

    
    
    init<V>(
        value: V,
        in bounds: ClosedRange<V> = 0...1,
        @ViewBuilder label: () -> Label,
        @ViewBuilder currentValueLabel: () -> CurrentValueLabel,
        @ViewBuilder markedValueLabels: () -> MarkedValueLabels
    ) where BoundsLabel == EmptyView, V : BinaryFloatingPoint

##  Parameters

`value`

    

The value to show in the instance.

`bounds`

    

The range of the valid values. Defaults to `0...1`.

`label`

    

A view that describes the purpose of the gauge.

`currentValueLabel`

    

A view that describes the current value of the gauge.

`minimumValueLabel`

    

A view that describes the lower bounds of the gauge.

`maximumValueLabel`

    

A view that describes the upper bounds of the gauge.

`markedValueLabels`

    

A view builder containing tagged views, each of which describes a particular
value of the gauge. The method ignores this parameter.

## See Also

### Creating a gauge

`init<V>(value: V, in: ClosedRange<V>, label: () -> Label)`

Creates a gauge showing a value within a range and describes the gauge’s
purpose and current value.

`init<V>(value: V, in: ClosedRange<V>, label: () -> Label, currentValueLabel:
() -> CurrentValueLabel)`

Creates a gauge showing a value within a range and that describes the gauge’s
purpose and current value.

`init<V>(value: V, in: ClosedRange<V>, label: () -> Label, currentValueLabel:
() -> CurrentValueLabel, minimumValueLabel: () -> BoundsLabel,
maximumValueLabel: () -> BoundsLabel)`

Creates a gauge showing a value within a range and describes the gauge’s
current, minimum, and maximum values.

`init<V>(value: V, in: ClosedRange<V>, label: () -> Label, currentValueLabel:
() -> CurrentValueLabel, minimumValueLabel: () -> BoundsLabel,
maximumValueLabel: () -> BoundsLabel, markedValueLabels: () ->
MarkedValueLabels)`

Creates a gauge representing a value within a range.

Initializer

# init(value:in:label:currentValueLabel:minimumValueLabel:maximumValueLabel:)

Creates a gauge showing a value within a range and describes the gauge’s
current, minimum, and maximum values.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 7.0+
visionOS 1.0+

    
    
    init<V>(
        value: V,
        in bounds: ClosedRange<V> = 0...1,
        @ViewBuilder label: () -> Label,
        @ViewBuilder currentValueLabel: () -> CurrentValueLabel,
        @ViewBuilder minimumValueLabel: () -> BoundsLabel,
        @ViewBuilder maximumValueLabel: () -> BoundsLabel
    ) where MarkedValueLabels == EmptyView, V : BinaryFloatingPoint

##  Parameters

`value`

    

The value to show on the gauge.

`bounds`

    

The range of the valid values. Defaults to `0...1`.

`label`

    

A view that describes the purpose of the gauge.

`currentValueLabel`

    

A view that describes the current value of the gauge.

`minimumValueLabel`

    

A view that describes the lower bounds of the gauge.

`maximumValueLabel`

    

A view that describes the upper bounds of the gauge.

## Discussion

Use this method to create a gauge that shows a value within a prescribed
bounds. The gauge has labels that describe its purpose, and for the gauge’s
current, minimum, and maximum values.

## See Also

### Creating a gauge

`init<V>(value: V, in: ClosedRange<V>, label: () -> Label)`

Creates a gauge showing a value within a range and describes the gauge’s
purpose and current value.

`init<V>(value: V, in: ClosedRange<V>, label: () -> Label, currentValueLabel:
() -> CurrentValueLabel)`

Creates a gauge showing a value within a range and that describes the gauge’s
purpose and current value.

`init<V>(value: V, in: ClosedRange<V>, label: () -> Label, currentValueLabel:
() -> CurrentValueLabel, markedValueLabels: () -> MarkedValueLabels)`

Creates a gauge representing a value within a range.

`init<V>(value: V, in: ClosedRange<V>, label: () -> Label, currentValueLabel:
() -> CurrentValueLabel, minimumValueLabel: () -> BoundsLabel,
maximumValueLabel: () -> BoundsLabel, markedValueLabels: () ->
MarkedValueLabels)`

Creates a gauge representing a value within a range.

Initializer

#
init(value:in:label:currentValueLabel:minimumValueLabel:maximumValueLabel:markedValueLabels:)

Creates a gauge representing a value within a range.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 7.0+
visionOS 1.0+

    
    
    init<V>(
        value: V,
        in bounds: ClosedRange<V> = 0...1,
        @ViewBuilder label: () -> Label,
        @ViewBuilder currentValueLabel: () -> CurrentValueLabel,
        @ViewBuilder minimumValueLabel: () -> BoundsLabel,
        @ViewBuilder maximumValueLabel: () -> BoundsLabel,
        @ViewBuilder markedValueLabels: () -> MarkedValueLabels
    ) where V : BinaryFloatingPoint

##  Parameters

`value`

    

The value to show in the gauge.

`bounds`

    

The range of the valid values. Defaults to `0...1`.

`label`

    

A view that describes the purpose of the gauge.

`currentValueLabel`

    

A view that describes the current value of the gauge.

`minimumValueLabel`

    

A view that describes the lower bounds of the gauge.

`maximumValueLabel`

    

A view that describes the upper bounds of the gauge.

`markedValueLabels`

    

A view builder containing tagged views. each of which describes a particular
value of the gauge. The method ignores this parameter.

## See Also

### Creating a gauge

`init<V>(value: V, in: ClosedRange<V>, label: () -> Label)`

Creates a gauge showing a value within a range and describes the gauge’s
purpose and current value.

`init<V>(value: V, in: ClosedRange<V>, label: () -> Label, currentValueLabel:
() -> CurrentValueLabel)`

Creates a gauge showing a value within a range and that describes the gauge’s
purpose and current value.

`init<V>(value: V, in: ClosedRange<V>, label: () -> Label, currentValueLabel:
() -> CurrentValueLabel, markedValueLabels: () -> MarkedValueLabels)`

Creates a gauge representing a value within a range.

`init<V>(value: V, in: ClosedRange<V>, label: () -> Label, currentValueLabel:
() -> CurrentValueLabel, minimumValueLabel: () -> BoundsLabel,
maximumValueLabel: () -> BoundsLabel)`

Creates a gauge showing a value within a range and describes the gauge’s
current, minimum, and maximum values.



# GraphicsContext.ClipOptions

Type Property

# inverse

An option to invert the shape or layer alpha as the clip mask.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var inverse: GraphicsContext.ClipOptions { get }

## Discussion

When you use this option, SwiftUI uses `1 - alpha` instead of `alpha` for the
given clip shape.



# Grid

Initializer

# init(alignment:horizontalSpacing:verticalSpacing:content:)

Creates a grid with the specified spacing, alignment, and child views.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init(
        alignment: Alignment = .center,
        horizontalSpacing: CGFloat? = nil,
        verticalSpacing: CGFloat? = nil,
        @ViewBuilder content: () -> Content
    )

##  Parameters

`alignment`

    

The guide for aligning the child views within the space allocated for a given
cell. The default is `center`.

`horizontalSpacing`

    

The horizontal distance between each cell, given in points. The value is `nil`
by default, which results in a default distance between cells that’s
appropriate for the platform.

`verticalSpacing`

    

The vertical distance between each cell, given in points. The value is `nil`
by default, which results in a default distance between cells that’s
appropriate for the platform.

`content`

    

A closure that creates the grid’s rows.

## Discussion

Use this initializer to create a `Grid`. Provide a content closure that
defines the rows of the grid, and optionally customize the spacing between
cells and the alignment of content within each cell. The following example
customizes the spacing between cells:

You can list rows and the cells within rows directly, or you can use a
`ForEach` structure to generate either, as the example above does:

By default, the grid’s alignment value applies to all of the cells in the
grid. However, you can also change the alignment for particular cells or
groups of cells:

  * Override the vertical alignment for the cells in a row by specifying a `VerticalAlignment` parameter to the corresponding row’s `init(alignment:content:)` initializer.

  * Override the horizontal alignment for the cells in a column by adding a `gridColumnAlignment(_:)` view modifier to exactly one of the cells in the column, and specifying a `HorizontalAlignment` parameter.

  * Specify a custom alignment anchor for a particular cell by using the `gridCellAnchor(_:)` modifier on the cell’s view.



# GroupedListStyle

Initializer

# init()

Creates a grouped list style.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  visionOS 1.0+

    
    
    init()



# GraphicsContext.FilterOptions

Type Property

# linearColor

An option that causes the filter to perform calculations in a linear color
space.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var linearColor: GraphicsContext.FilterOptions { get }



# GridLayout

Initializer

# init(alignment:horizontalSpacing:verticalSpacing:)

Creates a grid with the specified spacing and alignment.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init(
        alignment: Alignment = .center,
        horizontalSpacing: CGFloat? = nil,
        verticalSpacing: CGFloat? = nil
    )

##  Parameters

`alignment`

    

The guide for aligning subviews within the space allocated for a given cell.
The default is `center`.

`horizontalSpacing`

    

The horizontal distance between each cell, given in points. The value is `nil`
by default, which results in a default distance between cells that’s
appropriate for the platform.

`verticalSpacing`

    

The vertical distance between each cell, given in points. The value is `nil`
by default, which results in a default distance between cells that’s
appropriate for the platform.

Instance Property

# alignment

The alignment of subviews.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var alignment: Alignment

## See Also

### Getting the grid’s properties

`var horizontalSpacing: CGFloat?`

The horizontal distance between adjacent subviews.

`var verticalSpacing: CGFloat?`

The vertical distance between adjacent subviews.

Instance Property

# horizontalSpacing

The horizontal distance between adjacent subviews.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var horizontalSpacing: CGFloat?

## Discussion

Set this value to `nil` to use default horizonal distances between subviews.

## See Also

### Getting the grid’s properties

`var alignment: Alignment`

The alignment of subviews.

`var verticalSpacing: CGFloat?`

The vertical distance between adjacent subviews.

Instance Property

# verticalSpacing

The vertical distance between adjacent subviews.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var verticalSpacing: CGFloat?

## Discussion

Set this value to `nil` to use default vertical distances between subviews.

## See Also

### Getting the grid’s properties

`var alignment: Alignment`

The alignment of subviews.

`var horizontalSpacing: CGFloat?`

The horizontal distance between adjacent subviews.

Collection

API Collection

# Layout Implementations

## Topics

### Structures

`struct Cache`

A stateful grid layout algorithm.



# GestureMask

Type Property

# all

Enable both the added gesture as well as all other gestures on the view and
its subviews.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let all: GestureMask

## See Also

### Getting gesture options

`static let gesture: GestureMask`

Enable the added gesture but disable all gestures in the subview hierarchy.

`static let subviews: GestureMask`

Enable all gestures in the subview hierarchy but disable the added gesture.

`static let none: GestureMask`

Disable all gestures in the subview hierarchy, including the added gesture.

Type Property

# gesture

Enable the added gesture but disable all gestures in the subview hierarchy.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let gesture: GestureMask

## See Also

### Getting gesture options

`static let all: GestureMask`

Enable both the added gesture as well as all other gestures on the view and
its subviews.

`static let subviews: GestureMask`

Enable all gestures in the subview hierarchy but disable the added gesture.

`static let none: GestureMask`

Disable all gestures in the subview hierarchy, including the added gesture.

Type Property

# subviews

Enable all gestures in the subview hierarchy but disable the added gesture.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let subviews: GestureMask

## See Also

### Getting gesture options

`static let all: GestureMask`

Enable both the added gesture as well as all other gestures on the view and
its subviews.

`static let gesture: GestureMask`

Enable the added gesture but disable all gestures in the subview hierarchy.

`static let none: GestureMask`

Disable all gestures in the subview hierarchy, including the added gesture.

Type Property

# none

Disable all gestures in the subview hierarchy, including the added gesture.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let none: GestureMask

## See Also

### Getting gesture options

`static let all: GestureMask`

Enable both the added gesture as well as all other gestures on the view and
its subviews.

`static let gesture: GestureMask`

Enable the added gesture but disable all gestures in the subview hierarchy.

`static let subviews: GestureMask`

Enable all gestures in the subview hierarchy but disable the added gesture.



# GroupBoxStyle

Type Property

# automatic

The default style for group box views.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static var automatic: DefaultGroupBoxStyle { get }

Available when `Self` is `DefaultGroupBoxStyle`.

Instance Method

# makeBody(configuration:)

Creates a view representing the body of a group box.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    @ViewBuilder
    func makeBody(configuration: Self.Configuration) -> Self.Body

**Required**

##  Parameters

`configuration`

    

The properties of the group box instance being created.

## Discussion

SwiftUI calls this method for each instance of `GroupBox` created within a
view hierarchy where this style is the current group box style.

## See Also

### Creating custom group box styles

`typealias Configuration`

The properties of a group box instance.

`associatedtype Body : View`

A view that represents the body of a group box.

**Required**

Type Alias

# GroupBoxStyle.Configuration

The properties of a group box instance.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    typealias Configuration = GroupBoxStyleConfiguration

## See Also

### Creating custom group box styles

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Creates a view representing the body of a group box.

**Required**

` associatedtype Body : View`

A view that represents the body of a group box.

**Required**

Associated Type

# Body

A view that represents the body of a group box.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    associatedtype Body : View

**Required**

## See Also

### Creating custom group box styles

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Creates a view representing the body of a group box.

**Required**

` typealias Configuration`

The properties of a group box instance.

Structure

# DefaultGroupBoxStyle

The default style for group box views.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    struct DefaultGroupBoxStyle

## Overview

You can also use `automatic` to construct this style.

## Topics

### Creating the group box style

`init()`

## Relationships

### Conforms To

  * `GroupBoxStyle`



# GraphicsContext.BlendMode

Type Property

# normal

A mode that paints source image samples over the background image samples.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var normal: GraphicsContext.BlendMode { get }

## Discussion

This is the default blend mode.

Type Property

# darken

A mode that creates composite image samples by choosing the darker samples
from either the source image or the background.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var darken: GraphicsContext.BlendMode { get }

## Discussion

When you draw in this mode, source image samples that are darker than the
background replace the background. Otherwise, the background image samples
remain unchanged.

## See Also

### Darkening

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

Type Property

# multiply

A mode that multiplies the source image samples with the background image
samples.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var multiply: GraphicsContext.BlendMode { get }

## Discussion

Drawing in this mode results in colors that are at least as dark as either of
the two contributing sample colors.

## See Also

### Darkening

`static var darken: GraphicsContext.BlendMode`

A mode that creates composite image samples by choosing the darker samples
from either the source image or the background.

`static var colorBurn: GraphicsContext.BlendMode`

A mode that darkens background image samples to reflect the source image
samples.

`static var plusDarker: GraphicsContext.BlendMode`

A mode that adds the inverse of the color components of the source and
background images, and then inverts the result, producing a darkened
composite.

Type Property

# colorBurn

A mode that darkens background image samples to reflect the source image
samples.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var colorBurn: GraphicsContext.BlendMode { get }

## Discussion

Source image sample values that specify white do not produce a change.

## See Also

### Darkening

`static var darken: GraphicsContext.BlendMode`

A mode that creates composite image samples by choosing the darker samples
from either the source image or the background.

`static var multiply: GraphicsContext.BlendMode`

A mode that multiplies the source image samples with the background image
samples.

`static var plusDarker: GraphicsContext.BlendMode`

A mode that adds the inverse of the color components of the source and
background images, and then inverts the result, producing a darkened
composite.

Type Property

# plusDarker

A mode that adds the inverse of the color components of the source and
background images, and then inverts the result, producing a darkened
composite.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var plusDarker: GraphicsContext.BlendMode { get }

## Discussion

This mode implements the equation `R = MAX(0, 1 - ((1 - D) + (1 - S)))` where

  * `R` is the composite image.

  * `S` is the source image.

  * `D` is the background.

## See Also

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

Type Property

# lighten

A mode that creates composite image samples by choosing the lighter samples
from either the source image or the background.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var lighten: GraphicsContext.BlendMode { get }

## Discussion

When you draw in this mode, source image samples that are lighter than the
background replace the background. Otherwise, the background image samples
remain unchanged.

## See Also

### Lightening

`static var screen: GraphicsContext.BlendMode`

A mode that multiplies the inverse of the source image samples with the
inverse of the background image samples.

`static var colorDodge: GraphicsContext.BlendMode`

A mode that brightens the background image samples to reflect the source image
samples.

`static var plusLighter: GraphicsContext.BlendMode`

A mode that adds the components of the source and background images, resulting
in a lightened composite.

Type Property

# screen

A mode that multiplies the inverse of the source image samples with the
inverse of the background image samples.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var screen: GraphicsContext.BlendMode { get }

## Discussion

Drawing in this mode results in colors that are at least as light as either of
the two contributing sample colors.

## See Also

### Lightening

`static var lighten: GraphicsContext.BlendMode`

A mode that creates composite image samples by choosing the lighter samples
from either the source image or the background.

`static var colorDodge: GraphicsContext.BlendMode`

A mode that brightens the background image samples to reflect the source image
samples.

`static var plusLighter: GraphicsContext.BlendMode`

A mode that adds the components of the source and background images, resulting
in a lightened composite.

Type Property

# colorDodge

A mode that brightens the background image samples to reflect the source image
samples.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var colorDodge: GraphicsContext.BlendMode { get }

## Discussion

Source image sample values that specify black do not produce a change.

## See Also

### Lightening

`static var lighten: GraphicsContext.BlendMode`

A mode that creates composite image samples by choosing the lighter samples
from either the source image or the background.

`static var screen: GraphicsContext.BlendMode`

A mode that multiplies the inverse of the source image samples with the
inverse of the background image samples.

`static var plusLighter: GraphicsContext.BlendMode`

A mode that adds the components of the source and background images, resulting
in a lightened composite.

Type Property

# plusLighter

A mode that adds the components of the source and background images, resulting
in a lightened composite.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var plusLighter: GraphicsContext.BlendMode { get }

## Discussion

This mode implements the equation `R = MIN(1, S + D)` where

  * `R` is the composite image.

  * `S` is the source image.

  * `D` is the background.

## See Also

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

Type Property

# overlay

A mode that either multiplies or screens the source image samples with the
background image samples, depending on the background color.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var overlay: GraphicsContext.BlendMode { get }

## Discussion

Drawing in this mode overlays the existing image samples while preserving the
highlights and shadows of the background. The background color mixes with the
source image to reflect the lightness or darkness of the background.

## See Also

### Adding contrast

`static var softLight: GraphicsContext.BlendMode`

A mode that either darkens or lightens colors, depending on the source image
sample color.

`static var hardLight: GraphicsContext.BlendMode`

A mode that either multiplies or screens colors, depending on the source image
sample color.

Type Property

# softLight

A mode that either darkens or lightens colors, depending on the source image
sample color.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var softLight: GraphicsContext.BlendMode { get }

## Discussion

If the source image sample color is lighter than 50% gray, the background is
lightened, similar to dodging. If the source image sample color is darker than
50% gray, the background is darkened, similar to burning. If the source image
sample color is equal to 50% gray, the background is not changed. Image
samples that are equal to pure black or pure white produce darker or lighter
areas, but do not result in pure black or white. The overall effect is similar
to what you’d achieve by shining a diffuse spotlight on the source image. Use
this to add highlights to a scene.

## See Also

### Adding contrast

`static var overlay: GraphicsContext.BlendMode`

A mode that either multiplies or screens the source image samples with the
background image samples, depending on the background color.

`static var hardLight: GraphicsContext.BlendMode`

A mode that either multiplies or screens colors, depending on the source image
sample color.

Type Property

# hardLight

A mode that either multiplies or screens colors, depending on the source image
sample color.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var hardLight: GraphicsContext.BlendMode { get }

## Discussion

If the source image sample color is lighter than 50% gray, the background is
lightened, similar to screening. If the source image sample color is darker
than 50% gray, the background is darkened, similar to multiplying. If the
source image sample color is equal to 50% gray, the source image is not
changed. Image samples that are equal to pure black or pure white result in
pure black or white. The overall effect is similar to what you’d achieve by
shining a harsh spotlight on the source image. Use this to add highlights to a
scene.

## See Also

### Adding contrast

`static var overlay: GraphicsContext.BlendMode`

A mode that either multiplies or screens the source image samples with the
background image samples, depending on the background color.

`static var softLight: GraphicsContext.BlendMode`

A mode that either darkens or lightens colors, depending on the source image
sample color.

Type Property

# difference

A mode that subtracts the brighter of the source image sample color or the
background image sample color from the other.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var difference: GraphicsContext.BlendMode { get }

## Discussion

Source image sample values that are black produce no change; white inverts the
background color values.

## See Also

### Inverting

`static var exclusion: GraphicsContext.BlendMode`

A mode that produces an effect similar to that produced by the difference
blend mode, but with lower contrast.

Type Property

# exclusion

A mode that produces an effect similar to that produced by the difference
blend mode, but with lower contrast.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var exclusion: GraphicsContext.BlendMode { get }

## Discussion

Source image sample values that are black don’t produce a change; white
inverts the background color values.

## See Also

### Inverting

`static var difference: GraphicsContext.BlendMode`

A mode that subtracts the brighter of the source image sample color or the
background image sample color from the other.

Type Property

# hue

A mode that uses the luminance and saturation values of the background with
the hue of the source image.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var hue: GraphicsContext.BlendMode { get }

## See Also

### Mixing color components

`static var saturation: GraphicsContext.BlendMode`

A mode that uses the luminance and hue values of the background with the
saturation of the source image.

`static var color: GraphicsContext.BlendMode`

A mode that uses the luminance values of the background with the hue and
saturation values of the source image.

`static var luminosity: GraphicsContext.BlendMode`

A mode that uses the hue and saturation of the background with the luminance
of the source image.

Type Property

# saturation

A mode that uses the luminance and hue values of the background with the
saturation of the source image.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var saturation: GraphicsContext.BlendMode { get }

## Discussion

Areas of the background that have no saturation — namely, pure gray areas —
don’t produce a change.

## See Also

### Mixing color components

`static var hue: GraphicsContext.BlendMode`

A mode that uses the luminance and saturation values of the background with
the hue of the source image.

`static var color: GraphicsContext.BlendMode`

A mode that uses the luminance values of the background with the hue and
saturation values of the source image.

`static var luminosity: GraphicsContext.BlendMode`

A mode that uses the hue and saturation of the background with the luminance
of the source image.

Type Property

# color

A mode that uses the luminance values of the background with the hue and
saturation values of the source image.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var color: GraphicsContext.BlendMode { get }

## Discussion

This mode preserves the gray levels in the image. You can use this mode to
color monochrome images or to tint color images.

## See Also

### Mixing color components

`static var hue: GraphicsContext.BlendMode`

A mode that uses the luminance and saturation values of the background with
the hue of the source image.

`static var saturation: GraphicsContext.BlendMode`

A mode that uses the luminance and hue values of the background with the
saturation of the source image.

`static var luminosity: GraphicsContext.BlendMode`

A mode that uses the hue and saturation of the background with the luminance
of the source image.

Type Property

# luminosity

A mode that uses the hue and saturation of the background with the luminance
of the source image.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var luminosity: GraphicsContext.BlendMode { get }

## Discussion

This mode creates an effect that is inverse to the effect created by the
`color` mode.

## See Also

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

Type Property

# clear

A mode that clears any pixels that the source image overwrites.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var clear: GraphicsContext.BlendMode { get }

## Discussion

With this mode, you can use the source image like an eraser.

This mode implements the equation `R = 0` where `R` is the composite image.

## See Also

### Accessing porter-duff modes

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

Type Property

# copy

A mode that replaces background image samples with source image samples.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var copy: GraphicsContext.BlendMode { get }

## Discussion

Unlike the `normal` mode, the source image completely replaces the background,
so that even transparent pixels in the source image replace opaque pixels in
the background, rather than letting the background show through.

This mode implements the equation `R = S` where

  * `R` is the composite image.

  * `S` is the source image.

## See Also

### Accessing porter-duff modes

`static var clear: GraphicsContext.BlendMode`

A mode that clears any pixels that the source image overwrites.

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

Type Property

# sourceIn

A mode that you use to paint the source image, including its transparency,
onto the opaque parts of the background.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var sourceIn: GraphicsContext.BlendMode { get }

## Discussion

This mode implements the equation `R = S*Da` where

  * `R` is the composite image.

  * `S` is the source image.

  * `Da` is the source background’s alpha value.

## See Also

### Accessing porter-duff modes

`static var clear: GraphicsContext.BlendMode`

A mode that clears any pixels that the source image overwrites.

`static var copy: GraphicsContext.BlendMode`

A mode that replaces background image samples with source image samples.

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

Type Property

# sourceOut

A mode that you use to paint the source image onto the transparent parts of
the background, while erasing the background.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var sourceOut: GraphicsContext.BlendMode { get }

## Discussion

This mode implements the equation `R = S*(1 - Da)` where

  * `R` is the composite image.

  * `S` is the source image.

  * `Da` is the source background’s alpha value.

## See Also

### Accessing porter-duff modes

`static var clear: GraphicsContext.BlendMode`

A mode that clears any pixels that the source image overwrites.

`static var copy: GraphicsContext.BlendMode`

A mode that replaces background image samples with source image samples.

`static var sourceIn: GraphicsContext.BlendMode`

A mode that you use to paint the source image, including its transparency,
onto the opaque parts of the background.

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

Type Property

# sourceAtop

A mode that you use to paint the opaque parts of the source image onto the
opaque parts of the background.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var sourceAtop: GraphicsContext.BlendMode { get }

## Discussion

This mode implements the equation `R = S*Da + D*(1 - Sa)` where

  * `R` is the composite image.

  * `S` is the source image.

  * `D` is the background.

  * `Sa` is the source image’s alpha value.

  * `Da` is the source background’s alpha value.

## See Also

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

Type Property

# destinationOver

A mode that you use to paint the source image under the background.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var destinationOver: GraphicsContext.BlendMode { get }

## Discussion

This mode implements the equation `R = S*(1 - Da) + D` where

  * `R` is the composite image.

  * `S` is the source image.

  * `D` is the background.

  * `Da` is the source background’s alpha value.

## See Also

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

Type Property

# destinationIn

A mode that you use to erase any of the background that isn’t covered by
opaque source pixels.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var destinationIn: GraphicsContext.BlendMode { get }

## Discussion

This mode implements the equation `R = D*Sa` where

  * `R` is the composite image.

  * `S` is the source image.

  * `Da` is the source background’s alpha value.

## See Also

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

Type Property

# destinationOut

A mode that you use to erase any of the background that is covered by opaque
source pixels.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var destinationOut: GraphicsContext.BlendMode { get }

## Discussion

This mode implements the equation `R = D*(1 - Sa)` where

  * `R` is the composite image.

  * `D` is the background.

  * `Sa` is the source image’s alpha value.

## See Also

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

`static var destinationAtop: GraphicsContext.BlendMode`

A mode that you use to paint the source image under the background, while
erasing any of the background not matched by opaque pixels from the source
image.

`static var xor: GraphicsContext.BlendMode`

A mode that you use to clear pixels where both the source and background
images are opaque.

Type Property

# destinationAtop

A mode that you use to paint the source image under the background, while
erasing any of the background not matched by opaque pixels from the source
image.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var destinationAtop: GraphicsContext.BlendMode { get }

## Discussion

This mode implements the equation `R = S*(1 - Da) + D*Sa` where

  * `R` is the composite image.

  * `S` is the source image.

  * `D` is the background.

  * `Sa` is the source image’s alpha value.

  * `Da` is the source background’s alpha value.

## See Also

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

`static var xor: GraphicsContext.BlendMode`

A mode that you use to clear pixels where both the source and background
images are opaque.

Type Property

# xor

A mode that you use to clear pixels where both the source and background
images are opaque.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var xor: GraphicsContext.BlendMode { get }

## Discussion

This mode implements the equation `R = S*(1 - Da) + D*(1 - Sa)` where

  * `R` is the composite image.

  * `S` is the source image.

  * `D` is the background.

  * `Sa` is the source image’s alpha value.

  * `Da` is the source background’s alpha value.

This XOR mode is only nominally related to the classical bitmap XOR operation,
which SwiftUI doesn’t support.

## See Also

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



# Gradient

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



# GridItem.Size

Case

# GridItem.Size.adaptive(minimum:maximum:)

Multiple items in the space of a single flexible item.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    case adaptive(
        minimum: CGFloat,
        maximum: CGFloat = .infinity
    )

## Discussion

This size case places one or more items into the space assigned to a single
`flexible` item, using the provided bounds and spacing to decide exactly how
many items fit. This approach prefers to insert as many items of the `minimum`
size as possible but lets them increase to the `maximum` size.

## See Also

### Getting the sizes

`case fixed(CGFloat)`

A single item with the specified fixed size.

`case flexible(minimum: CGFloat, maximum: CGFloat)`

A single flexible item.

Case

# GridItem.Size.fixed(_:)

A single item with the specified fixed size.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    case fixed(CGFloat)

## See Also

### Getting the sizes

`case adaptive(minimum: CGFloat, maximum: CGFloat)`

Multiple items in the space of a single flexible item.

`case flexible(minimum: CGFloat, maximum: CGFloat)`

A single flexible item.

Case

# GridItem.Size.flexible(minimum:maximum:)

A single flexible item.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    case flexible(
        minimum: CGFloat = 10,
        maximum: CGFloat = .infinity
    )

## Discussion

The size of this item is the size of the grid with spacing and inflexible
items removed, divided by the number of flexible items, clamped to the
provided bounds.

## See Also

### Getting the sizes

`case adaptive(minimum: CGFloat, maximum: CGFloat)`

Multiple items in the space of a single flexible item.

`case fixed(CGFloat)`

A single item with the specified fixed size.



# GeometryEffect

Instance Method

# effectValue(size:)

Returns the current value of the effect.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func effectValue(size: CGSize) -> ProjectionTransform

**Required**

## See Also

### Applying effects

`func ignoredByLayout() -> _IgnoredByLayoutEffect<Self>`

Returns an effect that produces the same geometry transform as this effect,
but only applies the transform while rendering its view.

Instance Method

# ignoredByLayout()

Returns an effect that produces the same geometry transform as this effect,
but only applies the transform while rendering its view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func ignoredByLayout() -> _IgnoredByLayoutEffect<Self>

## Discussion

Use this method to disable layout changes during transitions. The view ignores
the transform returned by this method while the view is performing its layout
calculations.

## See Also

### Applying effects

`func effectValue(size: CGSize) -> ProjectionTransform`

Returns the current value of the effect.

**Required**



# GestureState

Initializer

# init(initialValue:)

Creates a view state that’s derived from a gesture with an initial value.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(initialValue: Value)

##  Parameters

`initialValue`

    

An initial value for the gesture state property.

## See Also

### Creating a gesture state

`init(initialValue: Value, reset: (Value, inout Transaction) -> Void)`

Creates a view state that’s derived from a gesture with an initial state value
and a closure that provides a transaction to reset it.

`init(initialValue: Value, resetTransaction: Transaction)`

Creates a view state that’s derived from a gesture with an initial state value
and a transaction to reset it.

`init(reset: (Value, inout Transaction) -> Void)`

Creates a view state that’s derived from a gesture with a closure that
provides a transaction to reset it.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(resetTransaction: Transaction)`

Creates a view state that’s derived from a gesture with a transaction to reset
it.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(wrappedValue: Value)`

Creates a view state that’s derived from a gesture.

`init(wrappedValue: Value, reset: (Value, inout Transaction) -> Void)`

Creates a view state that’s derived from a gesture with a wrapped state value
and a closure that provides a transaction to reset it.

`init(wrappedValue: Value, resetTransaction: Transaction)`

Creates a view state that’s derived from a gesture with a wrapped state value
and a transaction to reset it.

Initializer

# init(initialValue:reset:)

Creates a view state that’s derived from a gesture with an initial state value
and a closure that provides a transaction to reset it.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        initialValue: Value,
        reset: @escaping (Value, inout Transaction) -> Void
    )

##  Parameters

`initialValue`

    

An initial state value.

`reset`

    

A closure that provides a `Transaction`.

## See Also

### Creating a gesture state

`init(initialValue: Value)`

Creates a view state that’s derived from a gesture with an initial value.

`init(initialValue: Value, resetTransaction: Transaction)`

Creates a view state that’s derived from a gesture with an initial state value
and a transaction to reset it.

`init(reset: (Value, inout Transaction) -> Void)`

Creates a view state that’s derived from a gesture with a closure that
provides a transaction to reset it.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(resetTransaction: Transaction)`

Creates a view state that’s derived from a gesture with a transaction to reset
it.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(wrappedValue: Value)`

Creates a view state that’s derived from a gesture.

`init(wrappedValue: Value, reset: (Value, inout Transaction) -> Void)`

Creates a view state that’s derived from a gesture with a wrapped state value
and a closure that provides a transaction to reset it.

`init(wrappedValue: Value, resetTransaction: Transaction)`

Creates a view state that’s derived from a gesture with a wrapped state value
and a transaction to reset it.

Initializer

# init(initialValue:resetTransaction:)

Creates a view state that’s derived from a gesture with an initial state value
and a transaction to reset it.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        initialValue: Value,
        resetTransaction: Transaction
    )

##  Parameters

`initialValue`

    

An initial state value.

`resetTransaction`

    

A transaction that provides metadata for view updates.

## See Also

### Creating a gesture state

`init(initialValue: Value)`

Creates a view state that’s derived from a gesture with an initial value.

`init(initialValue: Value, reset: (Value, inout Transaction) -> Void)`

Creates a view state that’s derived from a gesture with an initial state value
and a closure that provides a transaction to reset it.

`init(reset: (Value, inout Transaction) -> Void)`

Creates a view state that’s derived from a gesture with a closure that
provides a transaction to reset it.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(resetTransaction: Transaction)`

Creates a view state that’s derived from a gesture with a transaction to reset
it.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(wrappedValue: Value)`

Creates a view state that’s derived from a gesture.

`init(wrappedValue: Value, reset: (Value, inout Transaction) -> Void)`

Creates a view state that’s derived from a gesture with a wrapped state value
and a closure that provides a transaction to reset it.

`init(wrappedValue: Value, resetTransaction: Transaction)`

Creates a view state that’s derived from a gesture with a wrapped state value
and a transaction to reset it.

Initializer

# init(reset:)

Creates a view state that’s derived from a gesture with a closure that
provides a transaction to reset it.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(reset: @escaping (Value, inout Transaction) -> Void)

Available when `Value` conforms to `ExpressibleByNilLiteral`.

##  Parameters

`reset`

    

A closure that provides a `Transaction`.

## See Also

### Creating a gesture state

`init(initialValue: Value)`

Creates a view state that’s derived from a gesture with an initial value.

`init(initialValue: Value, reset: (Value, inout Transaction) -> Void)`

Creates a view state that’s derived from a gesture with an initial state value
and a closure that provides a transaction to reset it.

`init(initialValue: Value, resetTransaction: Transaction)`

Creates a view state that’s derived from a gesture with an initial state value
and a transaction to reset it.

`init(resetTransaction: Transaction)`

Creates a view state that’s derived from a gesture with a transaction to reset
it.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(wrappedValue: Value)`

Creates a view state that’s derived from a gesture.

`init(wrappedValue: Value, reset: (Value, inout Transaction) -> Void)`

Creates a view state that’s derived from a gesture with a wrapped state value
and a closure that provides a transaction to reset it.

`init(wrappedValue: Value, resetTransaction: Transaction)`

Creates a view state that’s derived from a gesture with a wrapped state value
and a transaction to reset it.

Initializer

# init(resetTransaction:)

Creates a view state that’s derived from a gesture with a transaction to reset
it.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(resetTransaction: Transaction = Transaction())

Available when `Value` conforms to `ExpressibleByNilLiteral`.

##  Parameters

`resetTransaction`

    

A transaction that provides metadata for view updates.

## See Also

### Creating a gesture state

`init(initialValue: Value)`

Creates a view state that’s derived from a gesture with an initial value.

`init(initialValue: Value, reset: (Value, inout Transaction) -> Void)`

Creates a view state that’s derived from a gesture with an initial state value
and a closure that provides a transaction to reset it.

`init(initialValue: Value, resetTransaction: Transaction)`

Creates a view state that’s derived from a gesture with an initial state value
and a transaction to reset it.

`init(reset: (Value, inout Transaction) -> Void)`

Creates a view state that’s derived from a gesture with a closure that
provides a transaction to reset it.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(wrappedValue: Value)`

Creates a view state that’s derived from a gesture.

`init(wrappedValue: Value, reset: (Value, inout Transaction) -> Void)`

Creates a view state that’s derived from a gesture with a wrapped state value
and a closure that provides a transaction to reset it.

`init(wrappedValue: Value, resetTransaction: Transaction)`

Creates a view state that’s derived from a gesture with a wrapped state value
and a transaction to reset it.

Initializer

# init(wrappedValue:)

Creates a view state that’s derived from a gesture.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(wrappedValue: Value)

##  Parameters

`wrappedValue`

    

A wrapped value for the gesture state property.

## See Also

### Creating a gesture state

`init(initialValue: Value)`

Creates a view state that’s derived from a gesture with an initial value.

`init(initialValue: Value, reset: (Value, inout Transaction) -> Void)`

Creates a view state that’s derived from a gesture with an initial state value
and a closure that provides a transaction to reset it.

`init(initialValue: Value, resetTransaction: Transaction)`

Creates a view state that’s derived from a gesture with an initial state value
and a transaction to reset it.

`init(reset: (Value, inout Transaction) -> Void)`

Creates a view state that’s derived from a gesture with a closure that
provides a transaction to reset it.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(resetTransaction: Transaction)`

Creates a view state that’s derived from a gesture with a transaction to reset
it.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(wrappedValue: Value, reset: (Value, inout Transaction) -> Void)`

Creates a view state that’s derived from a gesture with a wrapped state value
and a closure that provides a transaction to reset it.

`init(wrappedValue: Value, resetTransaction: Transaction)`

Creates a view state that’s derived from a gesture with a wrapped state value
and a transaction to reset it.

Initializer

# init(wrappedValue:reset:)

Creates a view state that’s derived from a gesture with a wrapped state value
and a closure that provides a transaction to reset it.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        wrappedValue: Value,
        reset: @escaping (Value, inout Transaction) -> Void
    )

##  Parameters

`wrappedValue`

    

A wrapped value for the gesture state property.

`reset`

    

A closure that provides a `Transaction`.

## See Also

### Creating a gesture state

`init(initialValue: Value)`

Creates a view state that’s derived from a gesture with an initial value.

`init(initialValue: Value, reset: (Value, inout Transaction) -> Void)`

Creates a view state that’s derived from a gesture with an initial state value
and a closure that provides a transaction to reset it.

`init(initialValue: Value, resetTransaction: Transaction)`

Creates a view state that’s derived from a gesture with an initial state value
and a transaction to reset it.

`init(reset: (Value, inout Transaction) -> Void)`

Creates a view state that’s derived from a gesture with a closure that
provides a transaction to reset it.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(resetTransaction: Transaction)`

Creates a view state that’s derived from a gesture with a transaction to reset
it.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(wrappedValue: Value)`

Creates a view state that’s derived from a gesture.

`init(wrappedValue: Value, resetTransaction: Transaction)`

Creates a view state that’s derived from a gesture with a wrapped state value
and a transaction to reset it.

Initializer

# init(wrappedValue:resetTransaction:)

Creates a view state that’s derived from a gesture with a wrapped state value
and a transaction to reset it.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        wrappedValue: Value,
        resetTransaction: Transaction
    )

##  Parameters

`wrappedValue`

    

A wrapped value for the gesture state property.

`resetTransaction`

    

A transaction that provides metadata for view updates.

## See Also

### Creating a gesture state

`init(initialValue: Value)`

Creates a view state that’s derived from a gesture with an initial value.

`init(initialValue: Value, reset: (Value, inout Transaction) -> Void)`

Creates a view state that’s derived from a gesture with an initial state value
and a closure that provides a transaction to reset it.

`init(initialValue: Value, resetTransaction: Transaction)`

Creates a view state that’s derived from a gesture with an initial state value
and a transaction to reset it.

`init(reset: (Value, inout Transaction) -> Void)`

Creates a view state that’s derived from a gesture with a closure that
provides a transaction to reset it.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(resetTransaction: Transaction)`

Creates a view state that’s derived from a gesture with a transaction to reset
it.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(wrappedValue: Value)`

Creates a view state that’s derived from a gesture.

`init(wrappedValue: Value, reset: (Value, inout Transaction) -> Void)`

Creates a view state that’s derived from a gesture with a wrapped state value
and a closure that provides a transaction to reset it.

Instance Property

# wrappedValue

The wrapped value referenced by the gesture state property.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var wrappedValue: Value { get }

## See Also

### Getting the state

`var projectedValue: GestureState<Value>`

A binding to the gesture state property.

Instance Property

# projectedValue

A binding to the gesture state property.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var projectedValue: GestureState<Value> { get }

## See Also

### Getting the state

`var wrappedValue: Value`

The wrapped value referenced by the gesture state property.



