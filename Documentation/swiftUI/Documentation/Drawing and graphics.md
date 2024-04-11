Structure

# Canvas

A view type that supports immediate mode drawing.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    struct Canvas<Symbols> where Symbols : View

## Overview

Use a canvas to draw rich and dynamic 2D graphics inside a SwiftUI view. The
canvas passes a `GraphicsContext` to the closure that you use to perform
immediate mode drawing operations. The canvas also passes a `CGSize` value
that you can use to customize what you draw. For example, you can use the
context’s `stroke(_:with:lineWidth:)` command to draw a `Path` instance:

The example above draws the outline of an ellipse that exactly inscribes a
canvas with a blue border:

In addition to outlined and filled paths, you can draw images, text, and
complete SwiftUI views. To draw views, use the
`init(opaque:colorMode:rendersAsynchronously:renderer:symbols:)` method to
supply views that you can reference from inside the renderer. You can also add
masks, apply filters, perform transforms, control blending, and more. For
information about how to draw, see `GraphicsContext`.

A canvas doesn’t offer interactivity or accessibility for individual elements,
including for views that you pass in as symbols. However, it might provide
better performance for a complex drawing that involves dynamic data. Use a
canvas to improve performance for a drawing that doesn’t primarily involve
text or require interactive elements.

## Topics

### Creating a canvas

`init(opaque: Bool, colorMode: ColorRenderingMode, rendersAsynchronously:
Bool, renderer: (inout GraphicsContext, CGSize) -> Void)`

Creates and configures a canvas.

Available when `Symbols` is `EmptyView`.

`init(opaque: Bool, colorMode: ColorRenderingMode, rendersAsynchronously:
Bool, renderer: (inout GraphicsContext, CGSize) -> Void, symbols: () ->
Symbols)`

Creates and configures a canvas that you supply with renderable child views.

### Managing opacity and color

`var isOpaque: Bool`

A Boolean that indicates whether the canvas is fully opaque.

`var colorMode: ColorRenderingMode`

The working color space and storage format of the canvas.

### Referencing symbols

`var symbols: Symbols`

A view that provides child views that you can use in the drawing callback.

### Rendering

`var rendersAsynchronously: Bool`

A Boolean that indicates whether the canvas can present its contents to its
parent view asynchronously.

`var renderer: (inout GraphicsContext, CGSize) -> Void`

The drawing callback that you use to draw into the canvas.

## Relationships

### Conforms To

  * `View`

Conforms when `Symbols` conforms to `View`.

## See Also

### Immediate mode drawing

Add Rich Graphics to Your SwiftUI App

Make your apps stand out by adding background materials, vibrancy, custom
graphics, and animations.

`struct GraphicsContext`

An immediate mode drawing destination, and its current state.

Structure

# GraphicsContext

An immediate mode drawing destination, and its current state.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    @frozen
    struct GraphicsContext

## Overview

Use a context to execute 2D drawing primitives. For example, you can draw
filled shapes using the `fill(_:with:style:)` method inside a `Canvas` view:

The example above draws an ellipse that just fits inside a canvas that’s
constrained to 300 points wide and 200 points tall:

In addition to outlining or filling paths, you can draw images, text, and
SwiftUI views. You can also use the context to perform many common graphical
operations, like adding masks, applying filters and transforms, and setting a
blend mode. For example you can add a mask using the `clip(to:style:options:)`
method:

The rectangular mask hides all but one quadrant of the ellipse:

The order of operations matters. Changes that you make to the state of the
context, like adding a mask or a filter, apply to later drawing operations. If
you reverse the fill and clip operations in the example above, so that the
fill comes first, the mask doesn’t affect the ellipse.

Each context references a particular layer in a tree of transparency layers,
and also contains a full copy of the drawing state. You can modify the state
of one context without affecting the state of any other, even if they refer to
the same layer. For example you can draw the masked ellipse from the previous
example into a copy of the main context, and then add a rectangle into the
main context:

The mask doesn’t clip the rectangle because the mask isn’t part of the main
context. However, both contexts draw into the same view because you created
one context as a copy of the other:

The context has access to an `EnvironmentValues` instance called `environment`
that’s initially copied from the environment of its enclosing view. SwiftUI
uses environment values — like the display resolution and color scheme — to
resolve types like `Image` and `Color` that appear in the context. You can
also access values stored in the environment for your own purposes.

## Topics

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

`struct GradientOptions`

Options that affect the rendering of color gradients.

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

`struct ResolvedImage`

An image resolved to a particular environment.

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

`struct ResolvedText`

A text view resolved to a particular environment.

### Drawing a child view

`func draw(GraphicsContext.ResolvedSymbol, at: CGPoint, anchor: UnitPoint)`

Draws a resolved symbol into the context, aligning an anchor within the symbol
to a point in the context.

`func draw(GraphicsContext.ResolvedSymbol, in: CGRect)`

Draws a resolved symbol into the context, using the specified rectangle as a
layout frame.

`func resolveSymbol<ID>(id: ID) -> GraphicsContext.ResolvedSymbol?`

Gets the identified child view as a resolved symbol, if the view exists.

`struct ResolvedSymbol`

A static sequence of drawing operations that may be drawn multiple times,
preserving their resolution independence.

### Drawing into a new layer

`func drawLayer(content: (inout GraphicsContext) throws -> Void) rethrows`

Draws a new layer, created by drawing code that you provide, into the context.

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

`struct ClipOptions`

Options that affect the use of clip shapes.

### Setting opacity and the blend mode

`var opacity: Double`

The opacity of drawing operations in the context.

`var blendMode: GraphicsContext.BlendMode`

The blend mode used by drawing operations in the context.

`struct BlendMode`

The ways that a graphics context combines new content with background content.

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

`struct ShadowOptions`

Options that configure the graphics context filter that creates shadows.

### Applying transforms

`func scaleBy(x: CGFloat, y: CGFloat)`

Scales subsequent drawing operations by an amount in each dimension.

`func rotate(by: Angle)`

Rotates subsequent drawing operations by an angle.

`func translateBy(x: CGFloat, y: CGFloat)`

Moves subsequent drawing operations by an amount in each dimension.

`func concatenate(CGAffineTransform)`

Appends the given transform to the context’s existing transform.

`var transform: CGAffineTransform`

The current transform matrix, defining user space coordinates.

### Drawing with a core graphics context

`func withCGContext(content: (CGContext) throws -> Void) rethrows`

Provides a Core Graphics context that you can use as a proxy to draw into this
context.

### Accessing the environment

`var environment: EnvironmentValues`

The environment associated with the graphics context.

## See Also

### Immediate mode drawing

Add Rich Graphics to Your SwiftUI App

Make your apps stand out by adding background materials, vibrancy, custom
graphics, and animations.

`struct Canvas`

A view type that supports immediate mode drawing.

Instance Method

# tint(_:)

Sets the tint within this view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func tint<S>(_ tint: S?) -> some View where S : ShapeStyle
    

##  Parameters

`tint`

    

The tint to apply.

## Discussion

Use this method to override the default accent color for this view with a
given styling. Unlike an app’s accent color, which can be overridden by user
preference, tint is always respected and should be used as a way to provide
additional meaning to the control.

Controls which are unable to style themselves using the given type of
`ShapeStyle` will try to approximate the styling as best as they can (i.e.
controls which can not style themselves using a gradient will attempt to use
the color of the gradient’s first stop).

This example shows a linear dashboard styled gauge tinted with a gradient from
`green` to `red`.

Some controls adapt to the tint color differently based on their style, the
current platform, and the surrounding context. For example, in macOS, a button
with the `bordered` style doesn’t tint its background, but one with the
`borderedProminent` style does. In macOS, neither of these button styles tint
their label, but they do in other platforms.

## See Also

### Setting a color

`func tint(Color?) -> some View`

Sets the tint color within this view.

`struct Color`

A representation of a color that adapts to a given context.

Instance Method

# tint(_:)

Sets the tint color within this view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func tint(_ tint: Color?) -> some View
    

##  Parameters

`tint`

    

The tint `Color` to apply.

## Discussion

Use this method to override the default accent color for this view. Unlike an
app’s accent color, which can be overridden by user preference, the tint color
is always respected and should be used as a way to provide additional meaning
to the control.

This example shows Answer and Decline buttons with `green` and `red` tint
colors, respectively.

Some controls adapt to the tint color differently based on their style, the
current platform, and the surrounding context. For example, in macOS, a button
with the `bordered` style doesn’t tint its background, but one with the
`borderedProminent` style does. In macOS, neither of these button styles tint
their label, but they do in other platforms.

## See Also

### Setting a color

`func tint<S>(S?) -> some View`

Sets the tint within this view.

`struct Color`

A representation of a color that adapts to a given context.

Structure

# Color

A representation of a color that adapts to a given context.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct Color

## Overview

You can create a color in one of several ways:

  * Load a color from an Asset Catalog:

  * Specify component values, like red, green, and blue; hue, saturation, and brightness; or white level:

  * Create a color instance from another color, like a `UIColor` or an `NSColor`:

  * Use one of a palette of predefined colors, like `black`, `green`, and `purple`.

Some view modifiers can take a color as an argument. For example,
`foregroundStyle(_:)` uses the color you provide to set the foreground color
for view elements, like text or SF Symbols:

Because SwiftUI treats colors as `View` instances, you can also directly add
them to a view hierarchy. For example, you can layer a rectangle beneath a sun
image using colors defined above:

A color used as a view expands to fill all the space it’s given, as defined by
the frame of the enclosing `ZStack` in the above example:

SwiftUI only resolves a color to a concrete value just before using it in a
given environment. This enables a context-dependent appearance for system
defined colors, or those that you load from an Asset Catalog. For example, a
color can have distinct light and dark variants that the system chooses from
at render time.

## Topics

### Creating a color from an asset

`init(String, bundle: Bundle?)`

Creates a color from a color set that you indicate by name.

### Creating a color from component values

`init(hue: Double, saturation: Double, brightness: Double, opacity: Double)`

Creates a constant color from hue, saturation, and brightness values.

`init(Color.RGBColorSpace, white: Double, opacity: Double)`

Creates a constant grayscale color.

`init(Color.RGBColorSpace, red: Double, green: Double, blue: Double, opacity:
Double)`

Creates a constant color from red, green, and blue component values.

`enum RGBColorSpace`

A profile that specifies how to interpret a color value for display.

### Creating a color from another color

`init(uiColor: UIColor)`

Creates a color from a UIKit color.

`init(nsColor: NSColor)`

Creates a color from an AppKit color.

`init(cgColor: CGColor)`

Creates a color from a Core Graphics color.

### Creating a color from a color resource

`init(ColorResource)`

Initialize a `Color` with a color resource.

### Creating a custom color

`init<T>(T)`

Creates a color that represents the specified custom color.

`init(Color.Resolved)`

Creates a constant color with the values specified by the resolved color.

`func resolve(in: EnvironmentValues) -> Color.Resolved`

Evaluates this color to a resolved color given the current `context`.

### Getting standard colors

`static let black: Color`

A black color suitable for use in UI elements.

`static let blue: Color`

A context-dependent blue color suitable for use in UI elements.

`static let brown: Color`

A context-dependent brown color suitable for use in UI elements.

`static let clear: Color`

A clear color suitable for use in UI elements.

`static let cyan: Color`

A context-dependent cyan color suitable for use in UI elements.

`static let gray: Color`

A context-dependent gray color suitable for use in UI elements.

`static let green: Color`

A context-dependent green color suitable for use in UI elements.

`static let indigo: Color`

A context-dependent indigo color suitable for use in UI elements.

`static let mint: Color`

A context-dependent mint color suitable for use in UI elements.

`static let orange: Color`

A context-dependent orange color suitable for use in UI elements.

`static let pink: Color`

A context-dependent pink color suitable for use in UI elements.

`static let purple: Color`

A context-dependent purple color suitable for use in UI elements.

`static let red: Color`

A context-dependent red color suitable for use in UI elements.

`static let teal: Color`

A context-dependent teal color suitable for use in UI elements.

`static let white: Color`

A white color suitable for use in UI elements.

`static let yellow: Color`

A context-dependent yellow color suitable for use in UI elements.

### Getting semantic colors

`static var accentColor: Color`

A color that reflects the accent color of the system or app.

`static let primary: Color`

The color to use for primary content.

`static let secondary: Color`

The color to use for secondary content.

### Modifying a color

`func opacity(Double) -> Color`

Multiplies the opacity of the color by the given amount.

`var gradient: AnyGradient`

Returns the standard gradient for the color `self`.

### Describing a color

`var description: String`

A textual representation of the color.

### Comparing colors

`static func == (Color, Color) -> Bool`

Indicates whether two colors are equal.

`func hash(into: inout Hasher)`

Hashes the essential components of the color by feeding them into the given
hash function.

### Deprecated symbols

`init(UIColor)`

Creates a color from a UIKit color.

Deprecated

`init(NSColor)`

Creates a color from an AppKit color.

Deprecated

`init(CGColor)`

Creates a color from a Core Graphics color.

Deprecated

`var cgColor: CGColor?`

A Core Graphics representation of the color, if available.

### Default Implementations

API Reference

ShapeStyle Implementations

API Reference

Transferable Implementations

## Relationships

### Conforms To

  * `CustomStringConvertible`
  * `Equatable`
  * `Hashable`
  * `Sendable`
  * `ShapeStyle`
  * `Transferable`
  * `View`

## See Also

### Setting a color

`func tint<S>(S?) -> some View`

Sets the tint within this view.

`func tint(Color?) -> some View`

Sets the tint color within this view.

Instance Method

# border(_:width:)

Adds a border to this view with the specified style and width.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func border<S>(
        _ content: S,
        width: CGFloat = 1
    ) -> some View where S : ShapeStyle
    

##  Parameters

`content`

    

A value that conforms to the `ShapeStyle` protocol, like a `Color` or
`HierarchicalShapeStyle`, that SwiftUI uses to fill the border.

`width`

    

The thickness of the border. The default is 1 pixel.

## Return Value

A view that adds a border with the specified style and width to this view.

## Discussion

Use this modifier to draw a border of a specified width around the view’s
frame. By default, the border appears inside the bounds of this view. For
example, you can add a four-point wide border covers the text:

To place a border around the outside of this view, apply padding of the same
width before adding the border:

## See Also

### Styling content

`func foregroundStyle<S>(S) -> some View`

Sets a view’s foreground elements to use a given style.

`func foregroundStyle<S1, S2>(S1, S2) -> some View`

Sets the primary and secondary levels of the foreground style in the child
view.

`func foregroundStyle<S1, S2, S3>(S1, S2, S3) -> some View`

Sets the primary, secondary, and tertiary levels of the foreground style.

`func backgroundStyle<S>(S) -> some View`

Sets the specified style to render backgrounds within the view.

`var backgroundStyle: AnyShapeStyle?`

An optional style that overrides the default system background style when set.

`protocol ShapeStyle`

A color or pattern to use when rendering a shape.

`struct AnyShapeStyle`

A type-erased ShapeStyle value.

`struct Gradient`

A color gradient represented as an array of color stops, each having a
parametric location value.

`struct AnyGradient`

A color gradient.

`struct ShadowStyle`

A style to use when rendering shadows.

Instance Method

# foregroundStyle(_:)

Sets a view’s foreground elements to use a given style.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func foregroundStyle<S>(_ style: S) -> some View where S : ShapeStyle
    

##  Parameters

`style`

    

The color or pattern to use when filling in the foreground elements. To
indicate a specific value, use `Color` or `image(_:sourceRect:scale:)`, or one
of the gradient types, like `linearGradient(colors:startPoint:endPoint:)`. To
set a style that’s relative to the containing view’s style, use one of the
semantic styles, like `primary`.

## Return Value

A view that uses the given foreground style.

## Discussion

Use this method to style foreground content like text, shapes, and template
images (including symbols):

The example above creates a row of `teal` foreground elements:

You can use any style that conforms to the `ShapeStyle` protocol, like the
`teal` color in the example above, or the
`linearGradient(colors:startPoint:endPoint:)` gradient shown below:

Tip

If you want to fill a single `Shape` instance with a style, use the
`fill(style:)` shape modifier instead because it’s more efficient.

SwiftUI creates a context-dependent render for a given style. For example, a
`Color` that you load from an asset catalog can have different light and dark
appearances, while some styles also vary by platform.

Hierarchical foreground styles like `ShapeStyle/secondary` don’t impose a
style of their own, but instead modify other styles. In particular, they
modify the primary level of the current foreground style to the degree given
by the hierarchical style’s name. To find the current foreground style to
modify, SwiftUI looks for the innermost containing style that you apply with
the `foregroundStyle(_:)` or the `foregroundColor(_:)` modifier. If you
haven’t specified a style, SwiftUI uses the default foreground style, as in
the following example:

If you add a foreground style on the enclosing `VStack`, the hierarchical
styling responds accordingly:

When you apply a custom style to a view, the view disables the vibrancy effect
for foreground elements in that view, or in any of its child views, that it
would otherwise gain from adding a background material — for example, using
the `background(_:ignoresSafeAreaEdges:)` modifier. However, hierarchical
styles applied to the default foreground don’t disable vibrancy.

## See Also

### Styling content

`func border<S>(S, width: CGFloat) -> some View`

Adds a border to this view with the specified style and width.

`func foregroundStyle<S1, S2>(S1, S2) -> some View`

Sets the primary and secondary levels of the foreground style in the child
view.

`func foregroundStyle<S1, S2, S3>(S1, S2, S3) -> some View`

Sets the primary, secondary, and tertiary levels of the foreground style.

`func backgroundStyle<S>(S) -> some View`

Sets the specified style to render backgrounds within the view.

`var backgroundStyle: AnyShapeStyle?`

An optional style that overrides the default system background style when set.

`protocol ShapeStyle`

A color or pattern to use when rendering a shape.

`struct AnyShapeStyle`

A type-erased ShapeStyle value.

`struct Gradient`

A color gradient represented as an array of color stops, each having a
parametric location value.

`struct AnyGradient`

A color gradient.

`struct ShadowStyle`

A style to use when rendering shadows.

Instance Method

# foregroundStyle(_:_:)

Sets the primary and secondary levels of the foreground style in the child
view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func foregroundStyle<S1, S2>(
        _ primary: S1,
        _ secondary: S2
    ) -> some View where S1 : ShapeStyle, S2 : ShapeStyle
    

##  Parameters

`primary`

    

The primary color or pattern to use when filling in the foreground elements.
To indicate a specific value, use `Color` or `image(_:sourceRect:scale:)`, or
one of the gradient types, like `linearGradient(colors:startPoint:endPoint:)`.
To set a style that’s relative to the containing view’s style, use one of the
semantic styles, like `primary`.

`secondary`

    

The secondary color or pattern to use when filling in the foreground elements.

## Return Value

A view that uses the given foreground styles.

## Discussion

SwiftUI uses these styles when rendering child views that don’t have an
explicit rendering style, like images, text, shapes, and so on.

Symbol images within the view hierarchy use the `palette` rendering mode when
you apply this modifier, if you don’t explicitly specify another mode.

## See Also

### Styling content

`func border<S>(S, width: CGFloat) -> some View`

Adds a border to this view with the specified style and width.

`func foregroundStyle<S>(S) -> some View`

Sets a view’s foreground elements to use a given style.

`func foregroundStyle<S1, S2, S3>(S1, S2, S3) -> some View`

Sets the primary, secondary, and tertiary levels of the foreground style.

`func backgroundStyle<S>(S) -> some View`

Sets the specified style to render backgrounds within the view.

`var backgroundStyle: AnyShapeStyle?`

An optional style that overrides the default system background style when set.

`protocol ShapeStyle`

A color or pattern to use when rendering a shape.

`struct AnyShapeStyle`

A type-erased ShapeStyle value.

`struct Gradient`

A color gradient represented as an array of color stops, each having a
parametric location value.

`struct AnyGradient`

A color gradient.

`struct ShadowStyle`

A style to use when rendering shadows.

Instance Method

# foregroundStyle(_:_:_:)

Sets the primary, secondary, and tertiary levels of the foreground style.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func foregroundStyle<S1, S2, S3>(
        _ primary: S1,
        _ secondary: S2,
        _ tertiary: S3
    ) -> some View where S1 : ShapeStyle, S2 : ShapeStyle, S3 : ShapeStyle
    

##  Parameters

`primary`

    

The primary color or pattern to use when filling in the foreground elements.
To indicate a specific value, use `Color` or `image(_:sourceRect:scale:)`, or
one of the gradient types, like `linearGradient(colors:startPoint:endPoint:)`.
To set a style that’s relative to the containing view’s style, use one of the
semantic styles, like `primary`.

`secondary`

    

The secondary color or pattern to use when filling in the foreground elements.

`tertiary`

    

The tertiary color or pattern to use when filling in the foreground elements.

## Return Value

A view that uses the given foreground styles.

## Discussion

SwiftUI uses these styles when rendering child views that don’t have an
explicit rendering style, like images, text, shapes, and so on.

Symbol images within the view hierarchy use the `palette` rendering mode when
you apply this modifier, if you don’t explicitly specify another mode.

## See Also

### Styling content

`func border<S>(S, width: CGFloat) -> some View`

Adds a border to this view with the specified style and width.

`func foregroundStyle<S>(S) -> some View`

Sets a view’s foreground elements to use a given style.

`func foregroundStyle<S1, S2>(S1, S2) -> some View`

Sets the primary and secondary levels of the foreground style in the child
view.

`func backgroundStyle<S>(S) -> some View`

Sets the specified style to render backgrounds within the view.

`var backgroundStyle: AnyShapeStyle?`

An optional style that overrides the default system background style when set.

`protocol ShapeStyle`

A color or pattern to use when rendering a shape.

`struct AnyShapeStyle`

A type-erased ShapeStyle value.

`struct Gradient`

A color gradient represented as an array of color stops, each having a
parametric location value.

`struct AnyGradient`

A color gradient.

`struct ShadowStyle`

A style to use when rendering shadows.

Instance Method

# backgroundStyle(_:)

Sets the specified style to render backgrounds within the view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func backgroundStyle<S>(_ style: S) -> some View where S : ShapeStyle
    

## Discussion

The following example uses this modifier to set the `backgroundStyle`
environment value to a `blue` color that includes a subtle `gradient`. SwiftUI
fills the `Circle` shape that acts as a background element with this style:

To restore the default background style, set the `backgroundStyle` environment
value to `nil` using the `environment(_:_:)` modifer:

## See Also

### Styling content

`func border<S>(S, width: CGFloat) -> some View`

Adds a border to this view with the specified style and width.

`func foregroundStyle<S>(S) -> some View`

Sets a view’s foreground elements to use a given style.

`func foregroundStyle<S1, S2>(S1, S2) -> some View`

Sets the primary and secondary levels of the foreground style in the child
view.

`func foregroundStyle<S1, S2, S3>(S1, S2, S3) -> some View`

Sets the primary, secondary, and tertiary levels of the foreground style.

`var backgroundStyle: AnyShapeStyle?`

An optional style that overrides the default system background style when set.

`protocol ShapeStyle`

A color or pattern to use when rendering a shape.

`struct AnyShapeStyle`

A type-erased ShapeStyle value.

`struct Gradient`

A color gradient represented as an array of color stops, each having a
parametric location value.

`struct AnyGradient`

A color gradient.

`struct ShadowStyle`

A style to use when rendering shadows.

Instance Property

# backgroundStyle

An optional style that overrides the default system background style when set.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var backgroundStyle: AnyShapeStyle? { get set }

## See Also

### Styling content

`func border<S>(S, width: CGFloat) -> some View`

Adds a border to this view with the specified style and width.

`func foregroundStyle<S>(S) -> some View`

Sets a view’s foreground elements to use a given style.

`func foregroundStyle<S1, S2>(S1, S2) -> some View`

Sets the primary and secondary levels of the foreground style in the child
view.

`func foregroundStyle<S1, S2, S3>(S1, S2, S3) -> some View`

Sets the primary, secondary, and tertiary levels of the foreground style.

`func backgroundStyle<S>(S) -> some View`

Sets the specified style to render backgrounds within the view.

`protocol ShapeStyle`

A color or pattern to use when rendering a shape.

`struct AnyShapeStyle`

A type-erased ShapeStyle value.

`struct Gradient`

A color gradient represented as an array of color stops, each having a
parametric location value.

`struct AnyGradient`

A color gradient.

`struct ShadowStyle`

A style to use when rendering shadows.

Protocol

# ShapeStyle

A color or pattern to use when rendering a shape.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    protocol ShapeStyle : Sendable

## Overview

You create custom shape styles by declaring a type that conforms to the
`ShapeStyle` protocol and implementing the required `resolve` function to
return a shape style that represents the desired appearance based on the
current environment.

For example this shape style reads the current color scheme from the
environment to choose the blend mode its color will be composited with:

In addition to creating a custom shape style, you can also use one of the
concrete styles that SwiftUI defines. To indicate a specific color or pattern,
you can use `Color` or the style returned by `image(_:sourceRect:scale:)`, or
one of the gradient types, like the one returned by
`radialGradient(_:center:startRadius:endRadius:)`. To set a color that’s
appropriate for a given context on a given platform, use one of the semantic
styles, like `background` or `primary`.

You can use a shape style by:

  * Filling a shape with a style with the `fill(_:style:)` modifier:

  * Tracing the outline of a shape with a style with either the `stroke(_:lineWidth:)` or the `stroke(_:style:)` modifier:

  * Styling the foreground elements in a view with the `foregroundStyle(_:)` modifier:

## Topics

### System colors

`static var black: Color`

A black color suitable for use in UI elements.

Available when `Self` is `Color`.

`static var blue: Color`

A context-dependent blue color suitable for use in UI elements.

Available when `Self` is `Color`.

`static var brown: Color`

A context-dependent brown color suitable for use in UI elements.

Available when `Self` is `Color`.

`static var clear: Color`

A clear color suitable for use in UI elements.

Available when `Self` is `Color`.

`static var cyan: Color`

A context-dependent cyan color suitable for use in UI elements.

Available when `Self` is `Color`.

`static var gray: Color`

A context-dependent gray color suitable for use in UI elements.

Available when `Self` is `Color`.

`static var green: Color`

A context-dependent green color suitable for use in UI elements.

Available when `Self` is `Color`.

`static var indigo: Color`

A context-dependent indigo color suitable for use in UI elements.

Available when `Self` is `Color`.

`static var mint: Color`

A context-dependent mint color suitable for use in UI elements.

Available when `Self` is `Color`.

`static var orange: Color`

A context-dependent orange color suitable for use in UI elements.

Available when `Self` is `Color`.

`static var pink: Color`

A context-dependent pink color suitable for use in UI elements.

Available when `Self` is `Color`.

`static var purple: Color`

A context-dependent purple color suitable for use in UI elements.

Available when `Self` is `Color`.

`static var red: Color`

A context-dependent red color suitable for use in UI elements.

Available when `Self` is `Color`.

`static var teal: Color`

A context-dependent teal color suitable for use in UI elements.

Available when `Self` is `Color`.

`static var white: Color`

A white color suitable for use in UI elements.

Available when `Self` is `Color`.

`static var yellow: Color`

A context-dependent yellow color suitable for use in UI elements.

Available when `Self` is `Color`.

### Angular gradients

`static func angularGradient(Gradient, center: UnitPoint, startAngle: Angle,
endAngle: Angle) -> AngularGradient`

An angular gradient, which applies the color function as the angle changes
between the start and end angles, and anchored to a relative center point
within the filled shape.

Available when `Self` is `AngularGradient`.

`static func angularGradient(AnyGradient, center: UnitPoint, startAngle:
Angle, endAngle: Angle) -> some ShapeStyle`

An angular gradient, which applies the color function as the angle changes
between the start and end angles, and anchored to a relative center point
within the filled shape.

Available when `Self` is `AngularGradient`.

`static func angularGradient(colors: [Color], center: UnitPoint, startAngle:
Angle, endAngle: Angle) -> AngularGradient`

An angular gradient defined by a collection of colors.

Available when `Self` is `AngularGradient`.

`static func angularGradient(stops: [Gradient.Stop], center: UnitPoint,
startAngle: Angle, endAngle: Angle) -> AngularGradient`

An angular gradient defined by a collection of color stops.

Available when `Self` is `AngularGradient`.

### Conic gradients

`static func conicGradient(Gradient, center: UnitPoint, angle: Angle) ->
AngularGradient`

A conic gradient that completes a full turn, optionally starting from a given
angle and anchored to a relative center point within the filled shape.

Available when `Self` is `AngularGradient`.

`static func conicGradient(AnyGradient, center: UnitPoint, angle: Angle) ->
some ShapeStyle`

A conic gradient that completes a full turn, optionally starting from a given
angle and anchored to a relative center point within the filled shape.

Available when `Self` is `AngularGradient`.

`static func conicGradient(colors: [Color], center: UnitPoint, angle: Angle)
-> AngularGradient`

A conic gradient defined by a collection of colors that completes a full turn.

Available when `Self` is `AngularGradient`.

`static func conicGradient(stops: [Gradient.Stop], center: UnitPoint, angle:
Angle) -> AngularGradient`

A conic gradient defined by a collection of color stops that completes a full
turn.

Available when `Self` is `AngularGradient`.

### Elliptical gradients

`static func ellipticalGradient(Gradient, center: UnitPoint,
startRadiusFraction: CGFloat, endRadiusFraction: CGFloat) ->
EllipticalGradient`

A radial gradient that draws an ellipse.

Available when `Self` is `EllipticalGradient`.

`static func ellipticalGradient(AnyGradient, center: UnitPoint,
startRadiusFraction: CGFloat, endRadiusFraction: CGFloat) -> some ShapeStyle`

A radial gradient that draws an ellipse.

Available when `Self` is `EllipticalGradient`.

`static func ellipticalGradient(colors: [Color], center: UnitPoint,
startRadiusFraction: CGFloat, endRadiusFraction: CGFloat) ->
EllipticalGradient`

A radial gradient that draws an ellipse defined by a collection of colors.

Available when `Self` is `EllipticalGradient`.

`static func ellipticalGradient(stops: [Gradient.Stop], center: UnitPoint,
startRadiusFraction: CGFloat, endRadiusFraction: CGFloat) ->
EllipticalGradient`

A radial gradient that draws an ellipse defined by a collection of color
stops.

Available when `Self` is `EllipticalGradient`.

### Linear gradients

`static func linearGradient(Gradient, startPoint: UnitPoint, endPoint:
UnitPoint) -> LinearGradient`

A linear gradient.

Available when `Self` is `LinearGradient`.

`static func linearGradient(AnyGradient, startPoint: UnitPoint, endPoint:
UnitPoint) -> some ShapeStyle`

A linear gradient.

Available when `Self` is `LinearGradient`.

`static func linearGradient(colors: [Color], startPoint: UnitPoint, endPoint:
UnitPoint) -> LinearGradient`

A linear gradient defined by a collection of colors.

Available when `Self` is `LinearGradient`.

`static func linearGradient(stops: [Gradient.Stop], startPoint: UnitPoint,
endPoint: UnitPoint) -> LinearGradient`

A linear gradient defined by a collection of color stops.

Available when `Self` is `LinearGradient`.

### Radial gradients

`static func radialGradient(Gradient, center: UnitPoint, startRadius: CGFloat,
endRadius: CGFloat) -> RadialGradient`

A radial gradient.

Available when `Self` is `RadialGradient`.

`static func radialGradient(AnyGradient, center: UnitPoint, startRadius:
CGFloat, endRadius: CGFloat) -> some ShapeStyle`

A radial gradient.

Available when `Self` is `RadialGradient`.

`static func radialGradient(colors: [Color], center: UnitPoint, startRadius:
CGFloat, endRadius: CGFloat) -> RadialGradient`

A radial gradient defined by a collection of colors.

Available when `Self` is `RadialGradient`.

`static func radialGradient(stops: [Gradient.Stop], center: UnitPoint,
startRadius: CGFloat, endRadius: CGFloat) -> RadialGradient`

A radial gradient defined by a collection of color stops.

Available when `Self` is `RadialGradient`.

### Materials

`static var ultraThinMaterial: Material`

A mostly translucent material.

Available when `Self` is `Material`.

`static var thinMaterial: Material`

A material that’s more translucent than opaque.

Available when `Self` is `Material`.

`static var regularMaterial: Material`

A material that’s somewhat translucent.

Available when `Self` is `Material`.

`static var thickMaterial: Material`

A material that’s more opaque than translucent.

Available when `Self` is `Material`.

`static var ultraThickMaterial: Material`

A mostly opaque material.

Available when `Self` is `Material`.

`static var bar: Material`

A material matching the style of system toolbars.

Available when `Self` is `Material`.

### Image paint styles

`static func image(Image, sourceRect: CGRect, scale: CGFloat) -> ImagePaint`

A shape style that fills a shape by repeating a region of an image.

Available when `Self` is `ImagePaint`.

### Hierarchical styles

`var secondary: some ShapeStyle`

Returns the second level of this shape style.

`var tertiary: some ShapeStyle`

Returns the third level of this shape style.

`var quaternary: some ShapeStyle`

Returns the fourth level of this shape style.

`var quinary: some ShapeStyle`

Returns the fifth level of this shape style.

`static var primary: HierarchicalShapeStyle`

A shape style that maps to the first level of the current content style.

Available when `Self` is `HierarchicalShapeStyle`.

`static var secondary: HierarchicalShapeStyle`

A shape style that maps to the second level of the current content style.

Available when `Self` is `HierarchicalShapeStyle`.

`static var tertiary: HierarchicalShapeStyle`

A shape style that maps to the third level of the current content style.

Available when `Self` is `HierarchicalShapeStyle`.

`static var quaternary: HierarchicalShapeStyle`

A shape style that maps to the fourth level of the current content style.

Available when `Self` is `HierarchicalShapeStyle`.

`static var quinary: HierarchicalShapeStyle`

A shape style that maps to the fifth level of the current content style.

Available when `Self` is `HierarchicalShapeStyle`.

### Semantic styles

`static var foreground: ForegroundStyle`

The foreground style in the current context.

Available when `Self` is `ForegroundStyle`.

`static var background: BackgroundStyle`

The background style in the current context.

Available when `Self` is `BackgroundStyle`.

`static var selection: SelectionShapeStyle`

A style used to visually indicate selection following platform conventional
colors and behaviors.

Available when `Self` is `SelectionShapeStyle`.

`static var separator: SeparatorShapeStyle`

A style appropriate for foreground separator or border lines.

Available when `Self` is `SeparatorShapeStyle`.

`static var tint: TintShapeStyle`

A style that reflects the current tint color.

Available when `Self` is `TintShapeStyle`.

`static var placeholder: PlaceholderTextShapeStyle`

A style appropriate for placeholder text.

Available when `Self` is `PlaceholderTextShapeStyle`.

`static var link: LinkShapeStyle`

A style appropriate for links.

Available when `Self` is `LinkShapeStyle`.

`static var fill: FillShapeStyle`

An overlay fill style for filling shapes.

Available when `Self` is `FillShapeStyle`.

`static var windowBackground: WindowBackgroundShapeStyle`

A style appropriate for elements that should match the background of their
containing window.

Available when `Self` is `WindowBackgroundShapeStyle`.

### Modifying a shape style

`func blendMode(BlendMode) -> some ShapeStyle`

Returns a new style based on `self` that applies the specified blend mode when
drawing.

`func opacity(Double) -> some ShapeStyle`

Returns a new style based on `self` that multiplies by the specified opacity
when drawing.

`func shadow(ShadowStyle) -> some ShapeStyle`

Applies the specified shadow effect to the shape style.

### Configuring the default shape style

`static func blendMode(BlendMode) -> some ShapeStyle`

Returns a new style based on the current style that uses `mode` as its blend
mode when drawing.

Available when `Self` is `AnyShapeStyle`.

`static func opacity(Double) -> some ShapeStyle`

Returns a new style based on the current style that multiplies by `opacity`
when drawing.

Available when `Self` is `AnyShapeStyle`.

`static func shadow(ShadowStyle) -> some ShapeStyle`

Returns a shape style that applies the specified shadow style to the current
style.

Available when `Self` is `AnyShapeStyle`.

### Mapping to absolute coordinates

`func `in`(CGRect) -> some ShapeStyle`

Maps a shape style’s unit-space coordinates to the absolute coordinates of a
given rectangle.

### Resolving a shape style in an environment

`func resolve(in: EnvironmentValues) -> Self.Resolved`

Evaluate to a resolved shape style given the current `environment`.

**Required** Default implementation provided.

`associatedtype Resolved : ShapeStyle = Never`

The type of shape style this will resolve to.

**Required**

### Using a shape style as a view

`var body: _ShapeView<Rectangle, Self>`

A rectangular view that’s filled with the shape style.

Available when `Self` conforms to `View` and `Body` is `_ShapeView<Rectangle,
Self>`.

### Supporting types

Construct instances of these styles using the properties and methods of the
shape style protocol.

`struct AngularGradient`

An angular gradient.

`struct EllipticalGradient`

A radial gradient that draws an ellipse.

`struct LinearGradient`

A linear gradient.

`struct RadialGradient`

A radial gradient.

`struct Material`

A background material type.

`struct ImagePaint`

A shape style that fills a shape by repeating a region of an image.

`struct HierarchicalShapeStyle`

A shape style that maps to one of the numbered content styles.

`struct HierarchicalShapeStyleModifier`

Styles that you can apply to hierarchical shapes.

`struct ForegroundStyle`

The foreground style in the current context.

`struct BackgroundStyle`

The background style in the current context.

`struct SelectionShapeStyle`

A style used to visually indicate selection following platform conventional
colors and behaviors.

`struct SeparatorShapeStyle`

A style appropriate for foreground separator or border lines.

`struct TintShapeStyle`

A style that reflects the current tint color.

`struct FillShapeStyle`

A shape style that displays one of the overlay fills.

`struct LinkShapeStyle`

A style appropriate for links.

`struct PlaceholderTextShapeStyle`

A style appropriate for placeholder text.

`struct WindowBackgroundShapeStyle`

A style appropriate for elements that should match the background of their
containing window.

## Relationships

### Inherits From

  * `Sendable`

### Conforming Types

  * `AngularGradient`
  * `AnyGradient`
  * `AnyShapeStyle`
  * `BackgroundStyle`
  * `Color`
  * `Color.Resolved`
  * `EllipticalGradient`
  * `FillShapeStyle`
  * `ForegroundStyle`
  * `Gradient`
  * `HierarchicalShapeStyle`
  * `HierarchicalShapeStyleModifier`
  * `ImagePaint`
  * `LinearGradient`
  * `LinkShapeStyle`
  * `Material`
  * `PlaceholderTextShapeStyle`
  * `RadialGradient`
  * `SelectionShapeStyle`
  * `SeparatorShapeStyle`
  * `Shader`
  * `TintShapeStyle`
  * `WindowBackgroundShapeStyle`

## See Also

### Styling content

`func border<S>(S, width: CGFloat) -> some View`

Adds a border to this view with the specified style and width.

`func foregroundStyle<S>(S) -> some View`

Sets a view’s foreground elements to use a given style.

`func foregroundStyle<S1, S2>(S1, S2) -> some View`

Sets the primary and secondary levels of the foreground style in the child
view.

`func foregroundStyle<S1, S2, S3>(S1, S2, S3) -> some View`

Sets the primary, secondary, and tertiary levels of the foreground style.

`func backgroundStyle<S>(S) -> some View`

Sets the specified style to render backgrounds within the view.

`var backgroundStyle: AnyShapeStyle?`

An optional style that overrides the default system background style when set.

`struct AnyShapeStyle`

A type-erased ShapeStyle value.

`struct Gradient`

A color gradient represented as an array of color stops, each having a
parametric location value.

`struct AnyGradient`

A color gradient.

`struct ShadowStyle`

A style to use when rendering shadows.

Structure

# AnyShapeStyle

A type-erased ShapeStyle value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    @frozen
    struct AnyShapeStyle

## Topics

### Creating a shape style

`init<S>(S)`

Create an instance from `style`.

## Relationships

### Conforms To

  * `Sendable`
  * `ShapeStyle`

## See Also

### Styling content

`func border<S>(S, width: CGFloat) -> some View`

Adds a border to this view with the specified style and width.

`func foregroundStyle<S>(S) -> some View`

Sets a view’s foreground elements to use a given style.

`func foregroundStyle<S1, S2>(S1, S2) -> some View`

Sets the primary and secondary levels of the foreground style in the child
view.

`func foregroundStyle<S1, S2, S3>(S1, S2, S3) -> some View`

Sets the primary, secondary, and tertiary levels of the foreground style.

`func backgroundStyle<S>(S) -> some View`

Sets the specified style to render backgrounds within the view.

`var backgroundStyle: AnyShapeStyle?`

An optional style that overrides the default system background style when set.

`protocol ShapeStyle`

A color or pattern to use when rendering a shape.

`struct Gradient`

A color gradient represented as an array of color stops, each having a
parametric location value.

`struct AnyGradient`

A color gradient.

`struct ShadowStyle`

A style to use when rendering shadows.

Structure

# Gradient

A color gradient represented as an array of color stops, each having a
parametric location value.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct Gradient

## Topics

### Creating a gradient from colors

`init(colors: [Color])`

Creates a gradient from an array of colors.

### Creating a gradient from stops

`init(stops: [Gradient.Stop])`

Creates a gradient from an array of color stops.

`var stops: [Gradient.Stop]`

The array of color stops.

`struct Stop`

One color stop in the gradient.

### Working with color spaces

`func colorSpace(Gradient.ColorSpace) -> AnyGradient`

Returns a version of the gradient that will use a specified color space for
interpolating between its colors.

`struct ColorSpace`

A method of interpolating between the colors in a gradient.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `ScaleRange`
  * `Sendable`
  * `ShapeStyle`

## See Also

### Styling content

`func border<S>(S, width: CGFloat) -> some View`

Adds a border to this view with the specified style and width.

`func foregroundStyle<S>(S) -> some View`

Sets a view’s foreground elements to use a given style.

`func foregroundStyle<S1, S2>(S1, S2) -> some View`

Sets the primary and secondary levels of the foreground style in the child
view.

`func foregroundStyle<S1, S2, S3>(S1, S2, S3) -> some View`

Sets the primary, secondary, and tertiary levels of the foreground style.

`func backgroundStyle<S>(S) -> some View`

Sets the specified style to render backgrounds within the view.

`var backgroundStyle: AnyShapeStyle?`

An optional style that overrides the default system background style when set.

`protocol ShapeStyle`

A color or pattern to use when rendering a shape.

`struct AnyShapeStyle`

A type-erased ShapeStyle value.

`struct AnyGradient`

A color gradient.

`struct ShadowStyle`

A style to use when rendering shadows.

Structure

# AnyGradient

A color gradient.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    @frozen
    struct AnyGradient

## Overview

When used as a `ShapeStyle`, this type draws a linear gradient with start-
point [0.5, 0] and end-point [0.5, 1].

## Topics

### Creating a gradient

`init(Gradient)`

Creates a new instance from the specified gradient.

### Working with color spaces

`func colorSpace(Gradient.ColorSpace) -> AnyGradient`

Returns a version of the gradient that will use a specified color space for
interpolating between its colors.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `ScaleRange`
  * `Sendable`
  * `ShapeStyle`

## See Also

### Styling content

`func border<S>(S, width: CGFloat) -> some View`

Adds a border to this view with the specified style and width.

`func foregroundStyle<S>(S) -> some View`

Sets a view’s foreground elements to use a given style.

`func foregroundStyle<S1, S2>(S1, S2) -> some View`

Sets the primary and secondary levels of the foreground style in the child
view.

`func foregroundStyle<S1, S2, S3>(S1, S2, S3) -> some View`

Sets the primary, secondary, and tertiary levels of the foreground style.

`func backgroundStyle<S>(S) -> some View`

Sets the specified style to render backgrounds within the view.

`var backgroundStyle: AnyShapeStyle?`

An optional style that overrides the default system background style when set.

`protocol ShapeStyle`

A color or pattern to use when rendering a shape.

`struct AnyShapeStyle`

A type-erased ShapeStyle value.

`struct Gradient`

A color gradient represented as an array of color stops, each having a
parametric location value.

`struct ShadowStyle`

A style to use when rendering shadows.

Structure

# ShadowStyle

A style to use when rendering shadows.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    struct ShadowStyle

## Topics

### Getting shadow styles

`static func drop(color: Color, radius: CGFloat, x: CGFloat, y: CGFloat) ->
ShadowStyle`

Creates a custom drop shadow style.

`static func inner(color: Color, radius: CGFloat, x: CGFloat, y: CGFloat) ->
ShadowStyle`

Creates a custom inner shadow style.

## Relationships

### Conforms To

  * `Equatable`
  * `Sendable`

## See Also

### Styling content

`func border<S>(S, width: CGFloat) -> some View`

Adds a border to this view with the specified style and width.

`func foregroundStyle<S>(S) -> some View`

Sets a view’s foreground elements to use a given style.

`func foregroundStyle<S1, S2>(S1, S2) -> some View`

Sets the primary and secondary levels of the foreground style in the child
view.

`func foregroundStyle<S1, S2, S3>(S1, S2, S3) -> some View`

Sets the primary, secondary, and tertiary levels of the foreground style.

`func backgroundStyle<S>(S) -> some View`

Sets the specified style to render backgrounds within the view.

`var backgroundStyle: AnyShapeStyle?`

An optional style that overrides the default system background style when set.

`protocol ShapeStyle`

A color or pattern to use when rendering a shape.

`struct AnyShapeStyle`

A type-erased ShapeStyle value.

`struct Gradient`

A color gradient represented as an array of color stops, each having a
parametric location value.

`struct AnyGradient`

A color gradient.

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

Structure

# ProjectionTransform

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct ProjectionTransform

## Topics

### Creating a transform

`init()`

`init(CGAffineTransform)`

`init(CATransform3D)`

### Getting transform characteristics

`var isAffine: Bool`

`var isIdentity: Bool`

### Manipulating transforms

`func invert() -> Bool`

`func inverted() -> ProjectionTransform`

`func concatenating(ProjectionTransform) -> ProjectionTransform`

### Accessing the transform’s coefficients

`var m11: CGFloat`

`var m12: CGFloat`

`var m13: CGFloat`

`var m21: CGFloat`

`var m22: CGFloat`

`var m23: CGFloat`

`var m31: CGFloat`

`var m32: CGFloat`

`var m33: CGFloat`

## Relationships

### Conforms To

  * `Equatable`
  * `Sendable`

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

`func projectionEffect(ProjectionTransform) -> some View`

Applies a projection transformation to this view’s rendered output.

`enum ContentMode`

Constants that define how a view’s content fills the available space.

Enumeration

# ContentMode

Constants that define how a view’s content fills the available space.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    enum ContentMode

## Topics

### Getting content modes

`case fill`

An option that resizes the content so it occupies all available space, both
vertically and horizontally.

`case fit`

An option that resizes the content so it’s all within the available space,
both vertically and horizontally.

## Relationships

### Conforms To

  * `CaseIterable`
  * `Equatable`
  * `Hashable`
  * `Sendable`

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

`func projectionEffect(ProjectionTransform) -> some View`

Applies a projection transformation to this view’s rendered output.

`struct ProjectionTransform`

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

Structure

# ColorMatrix

A matrix to use in an RGBA color transformation.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    @frozen
    struct ColorMatrix

## Overview

The matrix has five columns, each with a red, green, blue, and alpha
component. You can use the matrix for tasks like creating a color
transformation `GraphicsContext.Filter` for a `GraphicsContext` using the
`colorMatrix(_:)` method.

## Topics

### Creating an identity matrix

`init()`

Creates the identity matrix.

### First column

`var r1: Float`

`var g1: Float`

`var b1: Float`

`var a1: Float`

### Second column

`var r2: Float`

`var g2: Float`

`var b2: Float`

`var a2: Float`

### Third column

`var r3: Float`

`var g3: Float`

`var b3: Float`

`var a3: Float`

### Fourth column

`var r4: Float`

`var g4: Float`

`var b4: Float`

`var a4: Float`

### Fifth column

`var r5: Float`

`var g5: Float`

`var b5: Float`

`var a5: Float`

## Relationships

### Conforms To

  * `Equatable`
  * `Sendable`

## See Also

### Applying blur and shadows

`func blur(radius: CGFloat, opaque: Bool) -> some View`

Applies a Gaussian blur to this view.

`func shadow(color: Color, radius: CGFloat, x: CGFloat, y: CGFloat) -> some
View`

Adds a shadow to this view.

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

Protocol

# VisualEffect

Visual Effects change the visual appearance of a view without changing its
ancestors or descendents.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    protocol VisualEffect : Sendable, Animatable

## Overview

Because effects do not impact layout, they are safe to use in situations where
layout modification is not allowed. For example, effects may be applied as a
function of position, accessed through a geometry proxy:

You don’t conform to this protocol yourself. Instead, visual effects are
created by calling modifier functions (such as `.offset(x:y:)` on other
effects, as seen in the example above.

## Topics

### Adjusting Color

`func brightness(Double) -> some VisualEffect`

Brightens the view by the specified amount.

`func colorEffect(Shader, isEnabled: Bool) -> some VisualEffect`

Returns a new visual effect that applies `shader` to `self` as a filter effect
on the color of each pixel.

`func contrast(Double) -> some VisualEffect`

Sets the contrast and separation between similar colors in the view.

`func grayscale(Double) -> some VisualEffect`

Adds a grayscale effect to the view.

`func hueRotation(Angle) -> some VisualEffect`

Applies a hue rotation effect to the view.

`func saturation(Double) -> some VisualEffect`

Adjusts the color saturation of the view.

`func opacity(Double) -> some VisualEffect`

Sets the transparency of the view.

### Scaling

`func scaleEffect(CGFloat, anchor: UnitPoint) -> some VisualEffect`

Scales the view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(CGSize, anchor: UnitPoint) -> some VisualEffect`

Scales the view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some
VisualEffect`

Scales the view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> some VisualEffect`

Scales this view uniformly by the specified size in each dimension.

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> some VisualEffect`

Scales this view uniformly by the specified factor.

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
some VisualEffect`

Scales this view by the specified horizontal, vertical, and depth factors.

### Rotating

`func rotationEffect(Angle, anchor: UnitPoint) -> some VisualEffect`

Rotates content in two dimensions around the specified point.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some
VisualEffect`

Renders content as if it’s rotated in three dimensions around the specified
axis.

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint3D, perspective: CGFloat) -> some VisualEffect`

Renders content as if it’s rotated in three dimensions around the specified
axis.

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some VisualEffect`

Rotates content by the specified 3D rotation value.

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
some VisualEffect`

Rotates content by an angle about an axis that you specify as a rotation axis
value.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> some VisualEffect`

Rotates content by an angle about an axis that you specify as a tuple of
elements.

### Translating

`func offset(CGSize) -> some VisualEffect`

Offsets the view by the horizontal and vertical amount specified in the offset
parameter.

`func offset(x: CGFloat, y: CGFloat) -> some VisualEffect`

Offsets the view by the specified horizontal and vertical distances.

`func offset(z: CGFloat) -> some VisualEffect`

Brings a view forward in Z by the provided distance in points.

### Applying a transform

`func transform3DEffect(AffineTransform3D) -> some VisualEffect`

Applies a 3D transformation to the receiver.

`func transformEffect(CGAffineTransform) -> some VisualEffect`

Applies an affine transformation to the view’s rendered output.

`func transformEffect(ProjectionTransform) -> some VisualEffect`

Applies a projection transformation to the view’s rendered output.

### Applying other effects

`func blur(radius: CGFloat, opaque: Bool) -> some VisualEffect`

Applies a Gaussian blur to the view.

`func distortionEffect(Shader, maxSampleOffset: CGSize, isEnabled: Bool) ->
some VisualEffect`

Returns a new visual effect that applies `shader` to `self` as a geometric
distortion effect on the location of each pixel.

`func layerEffect(Shader, maxSampleOffset: CGSize, isEnabled: Bool) -> some
VisualEffect`

Returns a new visual effect that applies `shader` to `self` as a filter on the
raster layer created from `self`.

## Relationships

### Inherits From

  * `Animatable`
  * `Sendable`

### Conforming Types

  * `EmptyVisualEffect`

## See Also

### Applying effects based on geometry

`func visualEffect((EmptyVisualEffect, GeometryProxy) -> some VisualEffect) ->
some View`

Applies effects to this view, while providing access to layout information
through a geometry proxy.

`func visualEffect3D((EmptyVisualEffect, GeometryProxy3D) -> some
VisualEffect) -> some View`

Applies effects to this view, while providing access to layout information
through a 3D geometry proxy.

`struct EmptyVisualEffect`

The base visual effect that you apply additional effect to.

Structure

# EmptyVisualEffect

The base visual effect that you apply additional effect to.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct EmptyVisualEffect

## Overview

`EmptyVisualEffect` does not change the appearance of the view that it is
applied to.

## Topics

### Creating an empty visual effect

`init()`

Creates a new empty visual effect.

## Relationships

### Conforms To

  * `Animatable`
  * `Sendable`
  * `VisualEffect`

## See Also

### Applying effects based on geometry

`func visualEffect((EmptyVisualEffect, GeometryProxy) -> some VisualEffect) ->
some View`

Applies effects to this view, while providing access to layout information
through a geometry proxy.

`func visualEffect3D((EmptyVisualEffect, GeometryProxy3D) -> some
VisualEffect) -> some View`

Applies effects to this view, while providing access to layout information
through a 3D geometry proxy.

`protocol VisualEffect`

Visual Effects change the visual appearance of a view without changing its
ancestors or descendents.

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

Enumeration

# BlendMode

Modes for compositing a view with overlapping content.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    enum BlendMode

## Topics

### Getting the default

`case normal`

### Darkening

`case darken`

`case multiply`

`case colorBurn`

`case plusDarker`

### Lightening

`case lighten`

`case screen`

`case colorDodge`

`case plusLighter`

### Adding contrast

`case overlay`

`case softLight`

`case hardLight`

### Inverting

`case difference`

`case exclusion`

### Mixing color components

`case hue`

`case saturation`

`case color`

`case luminosity`

### Accessing porter-duff modes

`case sourceAtop`

`case destinationOver`

`case destinationOut`

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Compositing views

`func blendMode(BlendMode) -> some View`

Sets the blend mode for compositing this view with overlapping views.

`func compositingGroup() -> some View`

Wraps this view in a compositing group.

`func drawingGroup(opaque: Bool, colorMode: ColorRenderingMode) -> some View`

Composites this view’s contents into an offscreen image before final display.

`enum ColorRenderingMode`

The set of possible working color spaces for color-compositing operations.

Enumeration

# ColorRenderingMode

The set of possible working color spaces for color-compositing operations.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    enum ColorRenderingMode

## Overview

Each color space guarantees the preservation of a particular range of color
values.

## Topics

### Getting rendering modes

`case extendedLinear`

The extended linear sRGB working color space.

`case linear`

The linear sRGB working color space.

`case nonLinear`

The non-linear sRGB working color space.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Compositing views

`func blendMode(BlendMode) -> some View`

Sets the blend mode for compositing this view with overlapping views.

`func compositingGroup() -> some View`

Wraps this view in a compositing group.

`func drawingGroup(opaque: Bool, colorMode: ColorRenderingMode) -> some View`

Composites this view’s contents into an offscreen image before final display.

`enum BlendMode`

Modes for compositing a view with overlapping content.

Structure

# GeometryReader

A container view that defines its content as a function of its own size and
coordinate space.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct GeometryReader<Content> where Content : View

## Overview

This view returns a flexible preferred size to its parent layout.

## Topics

### Creating a geometry reader

`init(content: (GeometryProxy) -> Content)`

`var content: (GeometryProxy) -> Content`

## Relationships

### Conforms To

  * `View`

## See Also

### Measuring a view

`struct GeometryReader3D`

A container view that defines its content as a function of its own size and
coordinate space.

`struct GeometryProxy`

A proxy for access to the size and coordinate space (for anchor resolution) of
the container view.

`struct GeometryProxy3D`

A proxy for access to the size and coordinate space of the container view.

`func coordinateSpace(NamedCoordinateSpace) -> some View`

Assigns a name to the view’s coordinate space, so other code can operate on
dimensions like points and sizes relative to the named space.

`enum CoordinateSpace`

A resolved coordinate space created by the coordinate space protocol.

`protocol CoordinateSpaceProtocol`

A frame of reference within the layout system.

`struct PhysicalMetric`

Provides access to a value in points that corresponds to the specified
physical measurement.

`struct PhysicalMetricsConverter`

A physical metrics converter provides conversion between point values and
their extent in 3D space, in the form of physical length measurements.

Structure

# GeometryReader3D

A container view that defines its content as a function of its own size and
coordinate space.

visionOS 1.0+

    
    
    @frozen
    struct GeometryReader3D<Content> where Content : View

## Overview

This view returns a flexible preferred size to its own container view.

This container differs from `GeometryReader` in that it also reads available
depth, and thus also returns a flexible preferred depth to its parent layout.
Use the 3D version only in situations where you need to read depth, because it
affects depth layout when used in a container like a `ZStack`.

## Topics

### Creating a geometry reader

`init(content: (GeometryProxy3D) -> Content)`

`var content: (GeometryProxy3D) -> Content`

## Relationships

### Conforms To

  * `View`

## See Also

### Measuring a view

`struct GeometryReader`

A container view that defines its content as a function of its own size and
coordinate space.

`struct GeometryProxy`

A proxy for access to the size and coordinate space (for anchor resolution) of
the container view.

`struct GeometryProxy3D`

A proxy for access to the size and coordinate space of the container view.

`func coordinateSpace(NamedCoordinateSpace) -> some View`

Assigns a name to the view’s coordinate space, so other code can operate on
dimensions like points and sizes relative to the named space.

`enum CoordinateSpace`

A resolved coordinate space created by the coordinate space protocol.

`protocol CoordinateSpaceProtocol`

A frame of reference within the layout system.

`struct PhysicalMetric`

Provides access to a value in points that corresponds to the specified
physical measurement.

`struct PhysicalMetricsConverter`

A physical metrics converter provides conversion between point values and
their extent in 3D space, in the form of physical length measurements.

Structure

# GeometryProxy

A proxy for access to the size and coordinate space (for anchor resolution) of
the container view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    struct GeometryProxy

## Topics

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

`func transform(in: some CoordinateSpaceProtocol) -> AffineTransform3D?`

The container view’s 3D transform converted to a defined coordinate space.

## See Also

### Measuring a view

`struct GeometryReader`

A container view that defines its content as a function of its own size and
coordinate space.

`struct GeometryReader3D`

A container view that defines its content as a function of its own size and
coordinate space.

`struct GeometryProxy3D`

A proxy for access to the size and coordinate space of the container view.

`func coordinateSpace(NamedCoordinateSpace) -> some View`

Assigns a name to the view’s coordinate space, so other code can operate on
dimensions like points and sizes relative to the named space.

`enum CoordinateSpace`

A resolved coordinate space created by the coordinate space protocol.

`protocol CoordinateSpaceProtocol`

A frame of reference within the layout system.

`struct PhysicalMetric`

Provides access to a value in points that corresponds to the specified
physical measurement.

`struct PhysicalMetricsConverter`

A physical metrics converter provides conversion between point values and
their extent in 3D space, in the form of physical length measurements.

Structure

# GeometryProxy3D

A proxy for access to the size and coordinate space of the container view.

visionOS 1.0+

    
    
    struct GeometryProxy3D

## Overview

You can use a proxy for anchor resolution.

## Topics

### Accessing geometry characteristics

`func frame(in: some CoordinateSpaceProtocol) -> Rect3D`

The container view’s bounds rectangle converted to a defined coordinate space.

`var size: Size3D`

The size of the container view.

`var safeAreaInsets: EdgeInsets3D`

The safe area inset of the container view.

`subscript<T>(Anchor<T>) -> T`

Resolves the value of an anchor to the container view.

`func transform(in: some CoordinateSpaceProtocol) -> AffineTransform3D?`

The container view’s 3D transform converted to a defined coordinate space.

## See Also

### Measuring a view

`struct GeometryReader`

A container view that defines its content as a function of its own size and
coordinate space.

`struct GeometryReader3D`

A container view that defines its content as a function of its own size and
coordinate space.

`struct GeometryProxy`

A proxy for access to the size and coordinate space (for anchor resolution) of
the container view.

`func coordinateSpace(NamedCoordinateSpace) -> some View`

Assigns a name to the view’s coordinate space, so other code can operate on
dimensions like points and sizes relative to the named space.

`enum CoordinateSpace`

A resolved coordinate space created by the coordinate space protocol.

`protocol CoordinateSpaceProtocol`

A frame of reference within the layout system.

`struct PhysicalMetric`

Provides access to a value in points that corresponds to the specified
physical measurement.

`struct PhysicalMetricsConverter`

A physical metrics converter provides conversion between point values and
their extent in 3D space, in the form of physical length measurements.

Instance Method

# coordinateSpace(_:)

Assigns a name to the view’s coordinate space, so other code can operate on
dimensions like points and sizes relative to the named space.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func coordinateSpace(_ name: NamedCoordinateSpace) -> some View
    

##  Parameters

`name`

    

A name used to identify this coordinate space.

## Discussion

Use `coordinateSpace(_:)` to allow another function to find and operate on a
view and operate on dimensions relative to that view.

The example below demonstrates how a nested view can find and operate on its
enclosing view’s coordinate space:

Here, the `VStack` in the `ContentView` named “stack” is composed of a red
frame with a custom `Circle` view `overlay(_:alignment:)` at its center.

The `circle` view has an attached `DragGesture` that targets the enclosing
VStack’s coordinate space. As the gesture recognizer’s closure registers
events inside `circle` it stores them in the shared `location` state variable
and the `VStack` displays the coordinates in a `Text` view.

## See Also

### Measuring a view

`struct GeometryReader`

A container view that defines its content as a function of its own size and
coordinate space.

`struct GeometryReader3D`

A container view that defines its content as a function of its own size and
coordinate space.

`struct GeometryProxy`

A proxy for access to the size and coordinate space (for anchor resolution) of
the container view.

`struct GeometryProxy3D`

A proxy for access to the size and coordinate space of the container view.

`enum CoordinateSpace`

A resolved coordinate space created by the coordinate space protocol.

`protocol CoordinateSpaceProtocol`

A frame of reference within the layout system.

`struct PhysicalMetric`

Provides access to a value in points that corresponds to the specified
physical measurement.

`struct PhysicalMetricsConverter`

A physical metrics converter provides conversion between point values and
their extent in 3D space, in the form of physical length measurements.

Enumeration

# CoordinateSpace

A resolved coordinate space created by the coordinate space protocol.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    enum CoordinateSpace

## Overview

You don’t typically use `CoordinateSpace` directly. Instead, use the static
properties and functions of `CoordinateSpaceProtocol` such as `.global`,
`.local`, and `.named(_:)`.

## Topics

### Getting coordinate spaces

`case global`

The global coordinate space at the root of the view hierarchy.

`case local`

The local coordinate space of the current view.

`case named(AnyHashable)`

A named reference to a view’s local coordinate space.

### Testing a space

`var isGlobal: Bool`

`var isLocal: Bool`

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`

## See Also

### Measuring a view

`struct GeometryReader`

A container view that defines its content as a function of its own size and
coordinate space.

`struct GeometryReader3D`

A container view that defines its content as a function of its own size and
coordinate space.

`struct GeometryProxy`

A proxy for access to the size and coordinate space (for anchor resolution) of
the container view.

`struct GeometryProxy3D`

A proxy for access to the size and coordinate space of the container view.

`func coordinateSpace(NamedCoordinateSpace) -> some View`

Assigns a name to the view’s coordinate space, so other code can operate on
dimensions like points and sizes relative to the named space.

`protocol CoordinateSpaceProtocol`

A frame of reference within the layout system.

`struct PhysicalMetric`

Provides access to a value in points that corresponds to the specified
physical measurement.

`struct PhysicalMetricsConverter`

A physical metrics converter provides conversion between point values and
their extent in 3D space, in the form of physical length measurements.

Protocol

# CoordinateSpaceProtocol

A frame of reference within the layout system.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    protocol CoordinateSpaceProtocol

## Overview

All geometric properties of a view, including size, position, and transform,
are defined within the local coordinate space of the view’s parent. These
values can be converted into other coordinate spaces by passing types
conforming to this protocol into functions such as `GeometryProxy.frame(in:)`.

For example, a named coordinate space allows you to convert the frame of a
view into the local coordinate space of an ancestor view by defining a named
coordinate space using the `coordinateSpace(_:)` modifier, then passing that
same named coordinate space into the `frame(in:)` function.

You don’t typically create types conforming to this protocol yourself.
Instead, use the system-provided `.global`, `.local`, and `.named(_:)`
implementations.

## Topics

### Getting built-in coordinate spaces

`static var immersiveSpace: NamedCoordinateSpace`

The named coordinate space that represents the currently opened
`ImmersiveSpace` scene. If no immersive space is currently opened, this
CoordinateSpace provides the same behavior as the `.global` coordinate space.

Available when `Self` is `NamedCoordinateSpace`.

`static var global: GlobalCoordinateSpace`

The global coordinate space at the root of the view hierarchy.

Available when `Self` is `GlobalCoordinateSpace`.

`static var local: LocalCoordinateSpace`

The local coordinate space of the current view.

Available when `Self` is `LocalCoordinateSpace`.

`static func named(some Hashable) -> NamedCoordinateSpace`

Creates a named coordinate space using the given value.

Available when `Self` is `NamedCoordinateSpace`.

`static var scrollView: NamedCoordinateSpace`

The named coordinate space that is added by the system for the innermost
containing scroll view.

Available when `Self` is `NamedCoordinateSpace`.

`static func scrollView(axis: Axis) -> Self`

The named coordinate space that is added by the system for the innermost
containing scroll view that allows scrolling along the provided axis.

Available when `Self` is `NamedCoordinateSpace`.

### Getting the resolved coordinate space

`var coordinateSpace: CoordinateSpace`

The resolved coordinate space.

**Required**

### Supporting types

`struct GlobalCoordinateSpace`

The global coordinate space at the root of the view hierarchy.

`struct LocalCoordinateSpace`

The local coordinate space of the current view.

`struct NamedCoordinateSpace`

A named coordinate space.

## Relationships

### Conforming Types

  * `GlobalCoordinateSpace`
  * `LocalCoordinateSpace`
  * `NamedCoordinateSpace`

## See Also

### Measuring a view

`struct GeometryReader`

A container view that defines its content as a function of its own size and
coordinate space.

`struct GeometryReader3D`

A container view that defines its content as a function of its own size and
coordinate space.

`struct GeometryProxy`

A proxy for access to the size and coordinate space (for anchor resolution) of
the container view.

`struct GeometryProxy3D`

A proxy for access to the size and coordinate space of the container view.

`func coordinateSpace(NamedCoordinateSpace) -> some View`

Assigns a name to the view’s coordinate space, so other code can operate on
dimensions like points and sizes relative to the named space.

`enum CoordinateSpace`

A resolved coordinate space created by the coordinate space protocol.

`struct PhysicalMetric`

Provides access to a value in points that corresponds to the specified
physical measurement.

`struct PhysicalMetricsConverter`

A physical metrics converter provides conversion between point values and
their extent in 3D space, in the form of physical length measurements.

Structure

# PhysicalMetric

Provides access to a value in points that corresponds to the specified
physical measurement.

visionOS 1.0+

    
    
    @propertyWrapper @frozen
    struct PhysicalMetric<Value>

## Overview

Use this property wrapper inside a `View` or a type that inherits a `View`’s
environment, like a `ViewModifier`. Its value will be the equivalent in points
of the physical measurement of length you specify.

For example, to have a variable that contains the amount of points
corresponding to one meter, you can do the following:

Using this wrapper for a property of a type not associated with a scene’s view
contents, like an `App` or a `Scene`, is unsupported.

## Topics

### Creating a metric

`init(wrappedValue: Value, from: UnitLength)`

Creates a value that maps the specified set of physical length measurements,
in the specified unit, to a corresponding set of values measured in points in
the associated scene.

`init(wrappedValue: CGPoint, from: UnitLength)`

Creates a value that maps the specified point, whose dimensions are specified
in physical length measurements in the given unit, to the corresponding value
in points in the associated scene.

`init(wrappedValue: CGSize, from: UnitLength)`

Creates a value that maps the specified size, in the specified unit to the
corresponding value in points in the associated scene.

`init(wrappedValue: Size3D, from: UnitLength)`

Creates a value that maps the specified size, in the specified unit to the
corresponding value in points in the associated scene.

`init(wrappedValue: Point3D, from: UnitLength)`

Creates a value that maps the specified point, whose dimensions are specified
in physical length measurements in the given unit, to the corresponding value
in points in the associated scene.

`init(wrappedValue: Value, from: UnitLength)`

Creates a value that maps the specified single physical length measurement, in
the specified unit, to the corresponding value in points in the associated
scene.

`init(wrappedValue: CGRect, from: UnitLength)`

Creates a value that maps the specified rectangle, whose dimensions are
specified in physical length measurements in the given unit, to the
corresponding value in points in the associated scene.

`init(wrappedValue: Rect3D, from: UnitLength)`

Creates a value that maps the specified `Rect3D`, whose dimensions are
specified in physical length measurements in the given unit, to the
corresponding value in points in the associated scene.

### Getting the value

`var wrappedValue: Value`

A value in points in the coordinate system of the associated scene.

## Relationships

### Conforms To

  * `DynamicProperty`

## See Also

### Measuring a view

`struct GeometryReader`

A container view that defines its content as a function of its own size and
coordinate space.

`struct GeometryReader3D`

A container view that defines its content as a function of its own size and
coordinate space.

`struct GeometryProxy`

A proxy for access to the size and coordinate space (for anchor resolution) of
the container view.

`struct GeometryProxy3D`

A proxy for access to the size and coordinate space of the container view.

`func coordinateSpace(NamedCoordinateSpace) -> some View`

Assigns a name to the view’s coordinate space, so other code can operate on
dimensions like points and sizes relative to the named space.

`enum CoordinateSpace`

A resolved coordinate space created by the coordinate space protocol.

`protocol CoordinateSpaceProtocol`

A frame of reference within the layout system.

`struct PhysicalMetricsConverter`

A physical metrics converter provides conversion between point values and
their extent in 3D space, in the form of physical length measurements.

Structure

# PhysicalMetricsConverter

A physical metrics converter provides conversion between point values and
their extent in 3D space, in the form of physical length measurements.

visionOS 1.0+

    
    
    struct PhysicalMetricsConverter

## Overview

Converters are available from the environment of a `View` or other type that
inherits a `View`‘s environments, and are associated with the scene that
contains that environment. The conversions expect (or emit) values in points
in that scene’s coordinate system, and convert these to (or from) measurements
of length in the user’s reference frame. For example, if the scene is scaled,
that scale will be taken into account.

To obtain a converter, use the `physicalMetrics` key:

When user action modifies a scene so that measurements have changed (e.g., by
changing its scale), the view that accessed that environment key and its
hierarchy will be reevaluated.

Attempting to obtain a converter inside a type not associated with a scene’s
contents (for example, from an `App` or `Scene`’s environment) is not
supported.

## Topics

### Converting from a unit length

`func convert(CGPoint, from: UnitLength) -> CGPoint`

Converts a point, whose coordinates are in the specified unit, to a point
suitable for use in the environment this converter is associated with.

`func convert(Rect3D, from: UnitLength) -> Rect3D`

Converts a `Rect3D`, whose coordinates are in the specified unit, to a
`Rect3D` with coordinates specified in points, suitable for use in the
environment this converter is associated with.

`func convert(Size3D, from: UnitLength) -> Size3D`

Converts a size, given in the specified unit, to a size in points suitable for
use in the environment this converter is associated with.

`func convert(CGFloat, from: UnitLength) -> CGFloat`

Converts a length in the specified unit to a length in points suitable for use
in the environment this converter is associated with.

`func convert(Point3D, from: UnitLength) -> Point3D`

Converts a point, whose coordinates are in the specified unit, to a point
value suitable for use in the environment this converter is associated with.

`func convert(CGSize, from: UnitLength) -> CGSize`

Converts a size, given in the specified unit, to a size in points suitable for
use in the environment this converter is associated with.

`func convert<V>(V, from: UnitLength) -> V`

Converts a vector of physical length measurements, in the specified unit, to a
vector of values in points suitable for use in the environment this converter
is associated with.

`func convert(CGRect, from: UnitLength) -> CGRect`

Converts a rectangle, whose coordinates are in the specified unit, to a
rectangle with coordinates specified in points, suitable for use in the
environment this converter is associated with.

### Converting to a unit length

`func convert(Rect3D, to: UnitLength) -> Rect3D`

Converts a `Rect3D`’s coordinates to physical length measurements in the
specified unit.

`func convert(CGRect, to: UnitLength) -> CGRect`

Converts a rectangle’s coordinates to physical length measurements in the
specified unit.

`func convert(CGPoint, to: UnitLength) -> CGPoint`

Converts a point’s coordinates to physical length measurements in the
specified unit.

`func convert<V>(V, to: UnitLength) -> V`

Converts a vector of values in points to corresponding physical length
measurements in the specified unit.

`func convert(Point3D, to: UnitLength) -> Point3D`

Converts a point’s coordinates to physical length measurements in the
specified unit.

`func convert(CGSize, to: UnitLength) -> CGSize`

Converts a size, specified in points, to physical length measurements in the
specified unit.

`func convert(Size3D, to: UnitLength) -> Size3D`

Converts a size, specified in points, to physical length measurements in the
specified unit.

`func convert(CGFloat, to: UnitLength) -> CGFloat`

Converts a length in points to a physical length measurement in the specified
unit.

## Relationships

### Conforms To

  * `Equatable`

## See Also

### Measuring a view

`struct GeometryReader`

A container view that defines its content as a function of its own size and
coordinate space.

`struct GeometryReader3D`

A container view that defines its content as a function of its own size and
coordinate space.

`struct GeometryProxy`

A proxy for access to the size and coordinate space (for anchor resolution) of
the container view.

`struct GeometryProxy3D`

A proxy for access to the size and coordinate space of the container view.

`func coordinateSpace(NamedCoordinateSpace) -> some View`

Assigns a name to the view’s coordinate space, so other code can operate on
dimensions like points and sizes relative to the named space.

`enum CoordinateSpace`

A resolved coordinate space created by the coordinate space protocol.

`protocol CoordinateSpaceProtocol`

A frame of reference within the layout system.

`struct PhysicalMetric`

Provides access to a value in points that corresponds to the specified
physical measurement.

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

Structure

# Shader

A reference to a function in a Metal shader library, along with its bound
uniform argument values.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    struct Shader

## Overview

Shader values can be used as filter effects on views, see the
`colorEffect(_:isEnabled:)`, `distortionEffect(_:maxSampleOffset:isEnabled:)`,
and `layerEffect(_:maxSampleOffset:isEnabled:)` functions.

Shaders also conform to the `ShapeStyle` protocol, letting their MSL shader
function provide per-pixel color to fill any shape or text view. For a shader
function to act as a fill pattern it must have a function signature matching:

where `position` is the user-space coordinates of the pixel applied to the
shader, and `args...` should be compatible with the uniform arguments bound to
`shader`. The function should return the premultiplied color value in the
color space of the destination (typically extended sRGB).

## Topics

### Creating a shader

`init(function: ShaderFunction, arguments: [Shader.Argument])`

Creates a new shader from a function and the uniform argument values to bind
to the function.

`struct Argument`

A single uniform argument value to a shader function.

### Getting the shader function

`var function: ShaderFunction`

The shader function called by the shader.

`var arguments: [Shader.Argument]`

The uniform argument values passed to the shader function.

### Configuring the shader

`var dithersColor: Bool`

For shader functions that return color values, whether the returned color has
dither noise added to it, or is simply rounded to the output bit-depth. For
shaders generating smooth gradients, dithering is usually necessary to prevent
visible banding in the result.

## Relationships

### Conforms To

  * `Equatable`
  * `Sendable`
  * `ShapeStyle`

## See Also

### Accessing Metal shaders

`func colorEffect(Shader, isEnabled: Bool) -> some View`

Returns a new view that applies `shader` to `self` as a filter effect on the
color of each pixel.

`func distortionEffect(Shader, maxSampleOffset: CGSize, isEnabled: Bool) ->
some View`

Returns a new view that applies `shader` to `self` as a geometric distortion
effect on the location of each pixel.

`func layerEffect(Shader, maxSampleOffset: CGSize, isEnabled: Bool) -> some
View`

Returns a new view that applies `shader` to `self` as a filter on the raster
layer created from `self`.

`struct ShaderFunction`

A reference to a function in a Metal shader library.

`struct ShaderLibrary`

A Metal shader library.

Structure

# ShaderFunction

A reference to a function in a Metal shader library.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    @dynamicCallable
    struct ShaderFunction

## Topics

### Creating a shader function

`init(library: ShaderLibrary, name: String)`

Creates a new function reference from the provided shader library and function
name string.

### Configuring a function

`var library: ShaderLibrary`

The shader library storing the function.

`var name: String`

The name of the shader function in the library.

`func dynamicallyCall(withArguments: [Shader.Argument]) -> Shader`

Returns a new shader by applying the provided argument values to the
referenced function.

## Relationships

### Conforms To

  * `Equatable`
  * `Sendable`

## See Also

### Accessing Metal shaders

`func colorEffect(Shader, isEnabled: Bool) -> some View`

Returns a new view that applies `shader` to `self` as a filter effect on the
color of each pixel.

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

`struct ShaderLibrary`

A Metal shader library.

Structure

# ShaderLibrary

A Metal shader library.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    @dynamicMemberLookup
    struct ShaderLibrary

## Topics

### Getting the default shader library

`static let `default`: ShaderLibrary`

The default shader library of the main (i.e. app) bundle.

`static func bundle(Bundle) -> ShaderLibrary`

Returns the default shader library of the specified bundle.

### Creating a shader library

`init(url: URL)`

Creates a new Metal shader library from the contents of `url`, which must be
the location of precompiled Metal library. Functions compiled from the
returned library will only be cached as long as the returned library exists.

`init(data: Data)`

Creates a new Metal shader library from `data`, which must be the contents of
precompiled Metal library. Functions compiled from the returned library will
only be cached as long as the returned library exists.

### Access shader functions

`static subscript(dynamicMember _: String) -> ShaderFunction`

Returns a new shader function representing the stitchable MSL function called
`name` in the default shader library.

### Subscripts

`subscript(dynamicMember _: String) -> ShaderFunction`

Returns a new shader function representing the stitchable MSL function in the
library called `name`.

## Relationships

### Conforms To

  * `Equatable`
  * `Sendable`

## See Also

### Accessing Metal shaders

`func colorEffect(Shader, isEnabled: Bool) -> some View`

Returns a new view that applies `shader` to `self` as a filter effect on the
color of each pixel.

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

Enumeration

# Axis

The horizontal or vertical dimension in a 2D coordinate system.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    enum Axis

## Topics

### Getting axes

`case horizontal`

The horizontal dimension.

`case vertical`

The vertical dimension.

### Getting all axes

`struct Set`

An efficient set of axes.

## Relationships

### Conforms To

  * `CaseIterable`
  * `CustomStringConvertible`
  * `Equatable`
  * `Hashable`
  * `RawRepresentable`
  * `Sendable`

## See Also

### Accessing geometric constructs

`struct Angle`

A geometric angle whose value you access in either radians or degrees.

`struct UnitPoint`

A normalized 2D point in a view’s coordinate space.

`struct UnitPoint3D`

A normalized 3D point in a view’s coordinate space.

`struct Anchor`

An opaque value derived from an anchor source and a particular view.

Structure

# Angle

A geometric angle whose value you access in either radians or degrees.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct Angle

## Topics

### Getting constant angles

`static var zero: Angle`

`static func degrees(Double) -> Angle`

`static func radians(Double) -> Angle`

### Creating an angle

`init()`

`init(degrees: Double)`

`init(radians: Double)`

`init(Angle2D)`

### Getting the angle size

`var degrees: Double`

`var radians: Double`

## Relationships

### Conforms To

  * `Animatable`
  * `Comparable`
  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Accessing geometric constructs

`enum Axis`

The horizontal or vertical dimension in a 2D coordinate system.

`struct UnitPoint`

A normalized 2D point in a view’s coordinate space.

`struct UnitPoint3D`

A normalized 3D point in a view’s coordinate space.

`struct Anchor`

An opaque value derived from an anchor source and a particular view.

Structure

# UnitPoint

A normalized 2D point in a view’s coordinate space.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct UnitPoint

## Overview

Use a unit point to represent a location in a view without having to know the
view’s rendered size. The point stores a value in each dimension that
indicates the fraction of the view’s size in that dimension — measured from
the view’s origin — where the point appears. For example, you can create a
unit point that represents the center of any view by using the value `0.5` for
each dimension:

To project the unit point into the rendered view’s coordinate space, multiply
each component of the unit point with the corresponding component of the
view’s size:

You can perform this calculation yourself if you happen to know a view’s size,
or if you want to use the unit point for some custom purpose, but SwiftUI
typically does this for you to carry out operations that you request, like
when you:

  * Transform a shape using a shape modifier. For example, to rotate a shape with `rotation(_:anchor:)`, you indicate an anchor point that you want to rotate the shape around.

  * Override the alignment of the view in a `Grid` cell using the `gridCellAnchor(_:)` view modifier. The grid aligns the projection of a unit point onto the view with the projection of the same unit point onto the cell.

  * Create a gradient that has a center, or start and stop points, relative to the shape that you are styling. See the gradient methods in `ShapeStyle`.

You can create custom unit points with explicit values, like the example
above, or you can use one of the built-in unit points that SwiftUI provides,
like `zero`, `center`, or `topTrailing`. The built-in values correspond to the
alignment positions of the similarly named, built-in `Alignment` types.

Note

A unit point with one or more components outside the range `[0, 1]` projects
to a point outside of the view.

### Layout direction

When a person configures their device to use a left-to-right language like
English, the system places the view’s origin in its top-left corner, with
positive x toward the right and positive y toward the bottom of the view. In a
right-to-left environment, the origin moves to the upper-right corner, and the
positive x direction changes to be toward the left. You don’t typically need
to do anything to handle this change, because SwiftUI applies the change to
all aspects of the system. For example, see the discussion about layout
direction in `HorizontalAlignment`.

It’s important to test your app for the different locales that you distribute
your app in. For more information about the localization process, see
Localization.

## Topics

### Getting the origin

`static let zero: UnitPoint`

The origin of a view.

### Getting top points

`static let topLeading: UnitPoint`

A point that’s in the top, leading corner of a view.

`static let top: UnitPoint`

A point that’s centered horizontally on the top edge of a view.

`static let topTrailing: UnitPoint`

A point that’s in the top, trailing corner of a view.

### Getting middle points

`static let leading: UnitPoint`

A point that’s centered vertically on the leading edge of a view.

`static let center: UnitPoint`

A point that’s centered in a view.

`static let trailing: UnitPoint`

A point that’s centered vertically on the trailing edge of a view.

### Getting bottom points

`static let bottomLeading: UnitPoint`

A point that’s in the bottom, leading corner of a view.

`static let bottom: UnitPoint`

A point that’s centered horizontally on the bottom edge of a view.

`static let bottomTrailing: UnitPoint`

A point that’s in the bottom, trailing corner of a view.

### Creating a point

`init()`

Creates a unit point at the origin.

`init(x: CGFloat, y: CGFloat)`

Creates a unit point with the specified horizontal and vertical offsets.

### Getting the point’s coordinates

`var x: CGFloat`

The normalized distance from the origin to the point in the horizontal
direction.

`var y: CGFloat`

The normalized distance from the origin to the point in the vertical
dimension.

## Relationships

### Conforms To

  * `Animatable`
  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Accessing geometric constructs

`enum Axis`

The horizontal or vertical dimension in a 2D coordinate system.

`struct Angle`

A geometric angle whose value you access in either radians or degrees.

`struct UnitPoint3D`

A normalized 3D point in a view’s coordinate space.

`struct Anchor`

An opaque value derived from an anchor source and a particular view.

Structure

# UnitPoint3D

A normalized 3D point in a view’s coordinate space.

visionOS 1.0+

    
    
    @frozen
    struct UnitPoint3D

## Overview

Use a 3D unit point to represent a three-dimensional location in a view
without having to know the view’s rendered size. The point stores a value in
each dimension that indicates the fraction of the view’s size in that
dimension — measured from the view’s origin — where the point appears. For
example, you can create a unit point that represents the center of any view by
using the value `0.5` for each dimension:

Note

If you need a two-dimensional unit point, use `UnitPoint` instead.

To project the unit point into the rendered view’s coordinate space, multiply
each component of the unit point with the corresponding component of the
view’s size:

You can perform this calculation yourself if you happen to know a view’s size,
or if you want to use a unit point for some custom purpose, but SwiftUI
typically does this for you to carry out operations that you request, like
when you rotate a view with the `rotation3DEffect(_:anchor:)` modifier and
indicate the anchor point that you want to rotate the view around.

You can create custom unit points with explicit values, like the example
above, or you can use one of the built-in unit points that SwiftUI provides,
like `zero`, `center`, or `topTrailing`. The built-in values correspond to
common anchor points that you might want to refer to, like the center of one
of a view’s edges.

Note

A unit point with one or more components outside the range `[0, 1]` projects
to a point outside of the view.

### Layout direction

When a person configures their device to use a left-to-right language like
English, the system places the view’s origin in its top-left-back corner, with
positive x toward the right, positive y toward the bottom of the view, and
positive z toward the front. In a right-to-left environment, the origin moves
to the upper-right-back corner, and the positive x direction changes to be
toward the left. You don’t typically need to do anything to handle this
change, because SwiftUI applies the change to all aspects of the system. For
example, see the discussion about layout direction in `HorizontalAlignment`.

It’s important to test your app for the different locales that you distribute
your app in. For more information about the localization process, see
Localization.

## Topics

### Getting the origin

`static let origin: UnitPoint3D`

The origin of a view.

`static let zero: UnitPoint3D`

A 3D unit point with all components equal to zero.

### Getting top points

`static let topLeadingBack: UnitPoint3D`

A point that’s in the top-leading-back corner of a view.

`static let topLeading: UnitPoint3D`

A point that’s centered in the depth dimension on the top-leading edge of a
view.

`static let topLeadingFront: UnitPoint3D`

A point that’s in the top-leading-front corner of a view.

`static let topBack: UnitPoint3D`

A point that’s centered horizontally on the top-back edge of a view.

`static let top: UnitPoint3D`

A point that’s centered horizontally and in the depth dimension on the top
face of a view.

`static let topFront: UnitPoint3D`

A point that’s centered horizontally on the top-front edge of a view.

`static let topTrailingBack: UnitPoint3D`

A point that’s in the top-trailing-back corner of a view.

`static let topTrailing: UnitPoint3D`

A point that’s centered in the depth dimension on the top-trailing edge of a
view.

`static let topTrailingFront: UnitPoint3D`

A point that’s in the top-trailing-front corner of a view.

### Getting middle points

`static let leadingBack: UnitPoint3D`

A point that’s centered vertically on the leading-back edge of a view.

`static let leading: UnitPoint3D`

A point that’s centered vertically and in the depth dimension on the leading
face of a view.

`static let leadingFront: UnitPoint3D`

A point that’s centered vertically on the leading-front edge of a view.

`static let back: UnitPoint3D`

A point that’s centered horizontally and vertically on the back face of a
view.

`static let center: UnitPoint3D`

A point that’s centered in a view.

`static let front: UnitPoint3D`

A point that’s centered horizontally and vertically on the front face of a
view.

`static let trailingBack: UnitPoint3D`

A point that’s centered vertically on the trailing-back edge of a view.

`static let trailing: UnitPoint3D`

A point that’s centered vertically and in the depth dimension on the trailing
face of a view.

`static let trailingFront: UnitPoint3D`

A point that’s centered vertically on the trailing-front edge of a view.

### Getting bottom points

`static let bottomLeadingBack: UnitPoint3D`

A point that’s in the bottom-leading-back corner of a view.

`static let bottomLeading: UnitPoint3D`

A point that’s centered in the depth dimension on the bottom-leading edge of a
view.

`static let bottomLeadingFront: UnitPoint3D`

A point that’s in the bottom-leading-front corner of a view.

`static let bottomBack: UnitPoint3D`

A point that’s centered horizontally on the bottom-back edge of a view.

`static let bottom: UnitPoint3D`

A point that’s centered horizontally and in the depth dimension on the bottom
face of a view.

`static let bottomFront: UnitPoint3D`

A point that’s centered horizontally on the bottom-front edge of a view.

`static let bottomTrailingBack: UnitPoint3D`

A point that’s in the bottom-trailing-back corner of a view.

`static let bottomTrailing: UnitPoint3D`

A point that’s centered in the depth dimension on the bottom-trailing edge of
a view.

`static let bottomTrailingFront: UnitPoint3D`

A point that’s in the bottom-trailing-front corner of a view.

### Creating a point

`init()`

Creates a 3D unit point at the origin.

`init(x: CGFloat, y: CGFloat, z: CGFloat)`

Creates a 3D unit point with the specified offsets.

### Getting the point’s coordinates

`var x: CGFloat`

The normalized distance from the origin to the point in the horizontal
direction.

`var y: CGFloat`

The normalized distance from the origin to the point in the vertical
dimension.

`var z: CGFloat`

The normalized distance from the origin to the point in the depth dimension.

## Relationships

### Conforms To

  * `Animatable`
  * `Decodable`
  * `Encodable`
  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Accessing geometric constructs

`enum Axis`

The horizontal or vertical dimension in a 2D coordinate system.

`struct Angle`

A geometric angle whose value you access in either radians or degrees.

`struct UnitPoint`

A normalized 2D point in a view’s coordinate space.

`struct Anchor`

An opaque value derived from an anchor source and a particular view.

Structure

# Anchor

An opaque value derived from an anchor source and a particular view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct Anchor<Value>

## Overview

You can convert the anchor to a `Value` in the coordinate space of a target
view by using a `GeometryProxy` to specify the target view.

## Topics

### Getting the anchor’s source

`struct Source`

A type-erased geometry value that produces an anchored value of a given type.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Accessing geometric constructs

`enum Axis`

The horizontal or vertical dimension in a 2D coordinate system.

`struct Angle`

A geometric angle whose value you access in either radians or degrees.

`struct UnitPoint`

A normalized 2D point in a view’s coordinate space.

`struct UnitPoint3D`

A normalized 3D point in a view’s coordinate space.

