Structure

# Rectangle

A rectangular shape aligned inside the frame of the view containing it.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct Rectangle

## Topics

### Creating a rectangle

`init()`

Creates a new rectangle shape.

## Relationships

### Conforms To

  * `Animatable`
  * `InsettableShape`
  * `Sendable`
  * `Shape`
  * `View`

## See Also

### Creating rectangular shapes

`struct RoundedRectangle`

A rectangular shape with rounded corners, aligned inside the frame of the view
containing it.

`enum RoundedCornerStyle`

Defines the shape of a rounded rectangle’s corners.

`struct UnevenRoundedRectangle`

A rectangular shape with rounded corners with different values, aligned inside
the frame of the view containing it.

`struct RectangleCornerRadii`

Describes the corner radius values of a rounded rectangle with uneven corners.

Structure

# RoundedRectangle

A rectangular shape with rounded corners, aligned inside the frame of the view
containing it.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct RoundedRectangle

## Topics

### Creating a rounded rectangle

`init(cornerRadius: CGFloat, style: RoundedCornerStyle)`

Creates a new rounded rectangle shape.

`init(cornerSize: CGSize, style: RoundedCornerStyle)`

Creates a new rounded rectangle shape.

### Getting the shape’s characteristics

`var cornerSize: CGSize`

The width and height of the rounded rectangle’s corners.

`var style: RoundedCornerStyle`

The style of corners drawn by the rounded rectangle.

### Supporting types

`var animatableData: CGSize.AnimatableData`

The data to animate.

## Relationships

### Conforms To

  * `Animatable`
  * `InsettableShape`
  * `Sendable`
  * `Shape`
  * `View`

## See Also

### Creating rectangular shapes

`struct Rectangle`

A rectangular shape aligned inside the frame of the view containing it.

`enum RoundedCornerStyle`

Defines the shape of a rounded rectangle’s corners.

`struct UnevenRoundedRectangle`

A rectangular shape with rounded corners with different values, aligned inside
the frame of the view containing it.

`struct RectangleCornerRadii`

Describes the corner radius values of a rounded rectangle with uneven corners.

Enumeration

# RoundedCornerStyle

Defines the shape of a rounded rectangle’s corners.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    enum RoundedCornerStyle

## Topics

### Getting corner styles

`case circular`

Quarter-circle rounded rect corners.

`case continuous`

Continuous curvature rounded rect corners.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Creating rectangular shapes

`struct Rectangle`

A rectangular shape aligned inside the frame of the view containing it.

`struct RoundedRectangle`

A rectangular shape with rounded corners, aligned inside the frame of the view
containing it.

`struct UnevenRoundedRectangle`

A rectangular shape with rounded corners with different values, aligned inside
the frame of the view containing it.

`struct RectangleCornerRadii`

Describes the corner radius values of a rounded rectangle with uneven corners.

Structure

# UnevenRoundedRectangle

A rectangular shape with rounded corners with different values, aligned inside
the frame of the view containing it.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    @frozen
    struct UnevenRoundedRectangle

## Topics

### Creating an uneven rounded rectangle

`init(cornerRadii: RectangleCornerRadii, style: RoundedCornerStyle)`

Creates a new rounded rectangle shape with uneven corners.

`init(topLeadingRadius: CGFloat, bottomLeadingRadius: CGFloat,
bottomTrailingRadius: CGFloat, topTrailingRadius: CGFloat, style:
RoundedCornerStyle)`

Creates a new rounded rectangle shape with uneven corners.

### Getting the shape’s characteristics

`var cornerRadii: RectangleCornerRadii`

The radii of each corner of the rounded rectangle.

`var style: RoundedCornerStyle`

The style of corners drawn by the rounded rectangle.

### Supporting types

`var animatableData: RectangleCornerRadii.AnimatableData`

The data to animate.

## Relationships

### Conforms To

  * `Animatable`
  * `InsettableShape`
  * `Sendable`
  * `Shape`
  * `View`

## See Also

### Creating rectangular shapes

`struct Rectangle`

A rectangular shape aligned inside the frame of the view containing it.

`struct RoundedRectangle`

A rectangular shape with rounded corners, aligned inside the frame of the view
containing it.

`enum RoundedCornerStyle`

Defines the shape of a rounded rectangle’s corners.

`struct RectangleCornerRadii`

Describes the corner radius values of a rounded rectangle with uneven corners.

Structure

# RectangleCornerRadii

Describes the corner radius values of a rounded rectangle with uneven corners.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    @frozen
    struct RectangleCornerRadii

## Topics

### Creating a set of radii

`init(topLeading: CGFloat, bottomLeading: CGFloat, bottomTrailing: CGFloat,
topTrailing: CGFloat)`

Creates a new set of corner radii for a rounded rectangle with uneven corners.

### Getting values for specific corners

`var topLeading: CGFloat`

The radius of the top-leading corner.

`var topTrailing: CGFloat`

The radius of the top-trailing corner.

`var bottomLeading: CGFloat`

The radius of the bottom-leading corner.

`var bottomTrailing: CGFloat`

The radius of the bottom-trailing corner.

## Relationships

### Conforms To

  * `Animatable`
  * `Equatable`
  * `Sendable`

## See Also

### Creating rectangular shapes

`struct Rectangle`

A rectangular shape aligned inside the frame of the view containing it.

`struct RoundedRectangle`

A rectangular shape with rounded corners, aligned inside the frame of the view
containing it.

`enum RoundedCornerStyle`

Defines the shape of a rounded rectangle’s corners.

`struct UnevenRoundedRectangle`

A rectangular shape with rounded corners with different values, aligned inside
the frame of the view containing it.

Structure

# Circle

A circle centered on the frame of the view containing it.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct Circle

## Overview

The circle’s radius equals half the length of the frame rectangle’s smallest
edge.

## Topics

### Creating a circle

`init()`

Creates a new circle shape.

## Relationships

### Conforms To

  * `Animatable`
  * `ChartSymbolShape`
  * `InsettableShape`
  * `Sendable`
  * `Shape`
  * `View`

## See Also

### Creating circular shapes

`struct Ellipse`

An ellipse aligned inside the frame of the view containing it.

`struct Capsule`

A capsule shape aligned inside the frame of the view containing it.

Structure

# Ellipse

An ellipse aligned inside the frame of the view containing it.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct Ellipse

## Topics

### Creating an ellipse

`init()`

Creates a new ellipse shape.

## Relationships

### Conforms To

  * `Animatable`
  * `InsettableShape`
  * `Sendable`
  * `Shape`
  * `View`

## See Also

### Creating circular shapes

`struct Circle`

A circle centered on the frame of the view containing it.

`struct Capsule`

A capsule shape aligned inside the frame of the view containing it.

Structure

# Capsule

A capsule shape aligned inside the frame of the view containing it.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct Capsule

## Overview

A capsule shape is equivalent to a rounded rectangle where the corner radius
is chosen as half the length of the rectangle’s smallest edge.

## Topics

### Creating a capsule

`init(style: RoundedCornerStyle)`

Creates a new capsule shape.

### Getting the shape’s characteristics

`var style: RoundedCornerStyle`

## Relationships

### Conforms To

  * `Animatable`
  * `InsettableShape`
  * `Sendable`
  * `Shape`
  * `View`

## See Also

### Creating circular shapes

`struct Circle`

A circle centered on the frame of the view containing it.

`struct Ellipse`

An ellipse aligned inside the frame of the view containing it.

Structure

# Path

The outline of a 2D shape.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct Path

## Topics

### Creating a path

`init()`

Creates an empty path.

`init((inout Path) -> ())`

Creates an empty path, then executes a closure to add its initial elements.

`init(CGMutablePath)`

Creates a path from a copy of a mutable shape path.

`init(CGPath)`

Creates a path from an immutable shape path.

`init?(String)`

Initializes from the result of a previous call to `Path.stringRepresentation`.
Fails if the `string` does not describe a valid path.

`init(CGRect)`

Creates a path containing a rectangle.

`init(ellipseIn: CGRect)`

Creates a path as an ellipse within the given rectangle.

`init(roundedRect: CGRect, cornerRadius: CGFloat, style: RoundedCornerStyle)`

Creates a path containing a rounded rectangle.

`init(roundedRect: CGRect, cornerSize: CGSize, style: RoundedCornerStyle)`

Creates a path containing a rounded rectangle.

`init(roundedRect: CGRect, cornerRadii: RectangleCornerRadii, style:
RoundedCornerStyle)`

Creates a path as the given rounded rectangle, which may have uneven corner
radii.

### Getting the path’s characteristics

`var boundingRect: CGRect`

A rectangle containing all path segments.

`var cgPath: CGPath`

An immutable path representing the elements in the path.

`func contains(CGPoint, eoFill: Bool) -> Bool`

Returns true if the path contains a specified point.

`var currentPoint: CGPoint?`

Returns the last point in the path, or nil if the path contains no points.

`var description: String`

A description of the path that may be used to recreate the path via
`init?(_:)`.

`var isEmpty: Bool`

A Boolean value indicating whether the path contains zero elements.

### Drawing a path

`func move(to: CGPoint)`

Begins a new subpath at the specified point.

`func addArc(center: CGPoint, radius: CGFloat, startAngle: Angle, endAngle:
Angle, clockwise: Bool, transform: CGAffineTransform)`

Adds an arc of a circle to the path, specified with a radius and angles.

`func addArc(tangent1End: CGPoint, tangent2End: CGPoint, radius: CGFloat,
transform: CGAffineTransform)`

Adds an arc of a circle to the path, specified with a radius and two tangent
lines.

`func addCurve(to: CGPoint, control1: CGPoint, control2: CGPoint)`

Adds a cubic Bézier curve to the path, with the specified end point and
control points.

`func addEllipse(in: CGRect, transform: CGAffineTransform)`

Adds an ellipse that fits inside the specified rectangle to the path.

`func addLine(to: CGPoint)`

Appends a straight line segment from the current point to the specified point.

`func addLines([CGPoint])`

Adds a sequence of connected straight-line segments to the path.

`func addPath(Path, transform: CGAffineTransform)`

Appends another path value to this path.

`func addQuadCurve(to: CGPoint, control: CGPoint)`

Adds a quadratic Bézier curve to the path, with the specified end point and
control point.

`func addRect(CGRect, transform: CGAffineTransform)`

Adds a rectangular subpath to the path.

`func addRects([CGRect], transform: CGAffineTransform)`

Adds a set of rectangular subpaths to the path.

`func addRelativeArc(center: CGPoint, radius: CGFloat, startAngle: Angle,
delta: Angle, transform: CGAffineTransform)`

Adds an arc of a circle to the path, specified with a radius and a difference
in angle.

`func addRoundedRect(in: CGRect, cornerSize: CGSize, style:
RoundedCornerStyle, transform: CGAffineTransform)`

Adds a rounded rectangle to the path.

`func closeSubpath()`

Closes and completes the current subpath.

### Transforming the path

`func applying(CGAffineTransform) -> Path`

Returns a path constructed by applying the transform to all points of the
path.

`func offsetBy(dx: CGFloat, dy: CGFloat) -> Path`

Returns a path constructed by translating all its points.

`func trimmedPath(from: CGFloat, to: CGFloat) -> Path`

Returns a partial copy of the path.

### Performing operations on the path

`func addRoundedRect(in: CGRect, cornerSize: CGSize, style:
RoundedCornerStyle, transform: CGAffineTransform)`

Adds a rounded rectangle to the path.

`func intersection(Path, eoFill: Bool) -> Path`

Returns a new path with filled regions common to both paths.

`func lineIntersection(Path, eoFill: Bool) -> Path`

Returns a new path with a line from this path that overlaps the filled regions
of the given path.

`func lineSubtraction(Path, eoFill: Bool) -> Path`

Returns a new path with a line from this path that does not overlap the filled
region of the given path.

`func normalized(eoFill: Bool) -> Path`

Returns a new weakly-simple copy of this path.

`func subtracting(Path, eoFill: Bool) -> Path`

Returns a new path with filled regions from this path that are not in the
given path.

`func symmetricDifference(Path, eoFill: Bool) -> Path`

Returns a new path with filled regions either from this path or the given
path, but not in both.

`func union(Path, eoFill: Bool) -> Path`

Returns a new path with filled regions in either this path or the given path.

### Operating over path elements

`func forEach((Path.Element) -> Void)`

Calls `body` with each element in the path.

`enum Element`

An element of a path.

### Applying a style

`func strokedPath(StrokeStyle) -> Path`

Returns a stroked copy of the path using `style` to define how the stroked
outline is created.

### Instance Methods

`func addRoundedRect(in: CGRect, cornerRadii: RectangleCornerRadii, style:
RoundedCornerStyle, transform: CGAffineTransform)`

Adds a rounded rectangle with uneven corners to the path.

## Relationships

### Conforms To

  * `Animatable`
  * `CustomStringConvertible`
  * `Equatable`
  * `LosslessStringConvertible`
  * `Sendable`
  * `Shape`
  * `View`

Protocol

# ShapeView

A view that provides a shape that you can use for drawing operations.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    protocol ShapeView<Content> : View

## Overview

Use this type with the drawing methods on `Shape` to apply multiple fills
and/or strokes to a shape. For example, the following code applies a fill and
stroke to a capsule shape:

## Topics

### Getting the shape

`var shape: Self.Content`

The shape that this type draws and provides for other drawing operations.

**Required**

` associatedtype Content : Shape`

The type of shape this can provide.

**Required**

### Modify the shape

`func fill<S>(S, style: FillStyle) -> FillShapeView<Self.Content, S, Self>`

Fills this shape with a color or gradient.

`func stroke<S>(S, style: StrokeStyle, antialiased: Bool) ->
StrokeShapeView<Self.Content, S, Self>`

Traces the outline of this shape with a color or gradient.

`func stroke<S>(S, lineWidth: CGFloat, antialiased: Bool) ->
StrokeShapeView<Self.Content, S, Self>`

Traces the outline of this shape with a color or gradient.

`func strokeBorder<S>(S, style: StrokeStyle, antialiased: Bool) ->
StrokeBorderShapeView<Self.Content, S, Self>`

Returns a view that’s the result of insetting this view by half of its style’s
line width.

Available when `Content` conforms to `InsettableShape`.

`func strokeBorder<S>(S, lineWidth: CGFloat, antialiased: Bool) ->
StrokeBorderShapeView<Self.Content, S, Self>`

Returns a view that’s the result of filling an inner stroke of this view with
the content you supply.

Available when `Content` conforms to `InsettableShape`.

## Relationships

### Inherits From

  * `View`

### Conforming Types

  * `FillShapeView`
  * `StrokeBorderShapeView`
  * `StrokeShapeView`

## See Also

### Defining shape behavior

`protocol Shape`

A 2D shape that you can use when drawing a view.

`struct AnyShape`

A type-erased shape value.

`enum ShapeRole`

Ways of styling a shape.

`struct StrokeStyle`

The characteristics of a stroke that traces a path.

`struct StrokeShapeView`

A shape provider that strokes its shape.

`struct StrokeBorderShapeView`

A shape provider that strokes the border of its shape.

`struct FillStyle`

A style for rasterizing vector shapes.

`struct FillShapeView`

A shape provider that fills its shape.

Protocol

# Shape

A 2D shape that you can use when drawing a view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    protocol Shape : Sendable, Animatable, View

## Overview

Shapes without an explicit fill or stroke get a default fill based on the
foreground color.

You can define shapes in relation to an implicit frame of reference, such as
the natural size of the view that contains it. Alternatively, you can define
shapes in terms of absolute coordinates.

## Topics

### Getting standard shapes

`static var buttonBorder: ButtonBorderShape`

A shape that defers to the environment to determine the resolved button border
shape.

Available when `Self` is `ButtonBorderShape`.

`static var capsule: Capsule`

A capsule shape aligned inside the frame of the view containing it.

Available when `Self` is `Capsule`.

`static func capsule(style: RoundedCornerStyle) -> Self`

A capsule shape aligned inside the frame of the view containing it.

Available when `Self` is `Capsule`.

`static var circle: Circle`

A circle centered on the frame of the view containing it.

Available when `Self` is `Circle`.

`static var containerRelative: ContainerRelativeShape`

A shape that is replaced by an inset version of the current container shape.
If no container shape was defined, is replaced by a rectangle.

Available when `Self` is `ContainerRelativeShape`.

`static var ellipse: Ellipse`

An ellipse aligned inside the frame of the view containing it.

Available when `Self` is `Ellipse`.

`static var rect: Rectangle`

A rectangular shape aligned inside the frame of the view containing it.

Available when `Self` is `Rectangle`.

`static func rect(cornerRadii: RectangleCornerRadii, style:
RoundedCornerStyle) -> Self`

A rectangular shape with rounded corners with different values, aligned inside
the frame of the view containing it.

Available when `Self` is `UnevenRoundedRectangle`.

`static func rect(cornerRadius: CGFloat, style: RoundedCornerStyle) -> Self`

A rectangular shape with rounded corners, aligned inside the frame of the view
containing it.

Available when `Self` is `RoundedRectangle`.

`static func rect(cornerSize: CGSize, style: RoundedCornerStyle) -> Self`

A rectangular shape with rounded corners, aligned inside the frame of the view
containing it.

Available when `Self` is `RoundedRectangle`.

`static func rect(topLeadingRadius: CGFloat, bottomLeadingRadius: CGFloat,
bottomTrailingRadius: CGFloat, topTrailingRadius: CGFloat, style:
RoundedCornerStyle) -> Self`

A rectangular shape with rounded corners with different values, aligned inside
the frame of the view containing it.

Available when `Self` is `UnevenRoundedRectangle`.

### Defining a shape’s size and path

`func sizeThatFits(ProposedViewSize) -> CGSize`

Returns the size of the view that will render the shape, given a proposed
size.

**Required** Default implementation provided.

`func path(in: CGRect) -> Path`

Describes this shape as a path within a rectangular frame of reference.

**Required**

### Transforming a shape

`func trim(from: CGFloat, to: CGFloat) -> some Shape`

Trims this shape by a fractional amount based on its representation as a path.

`func transform(CGAffineTransform) -> TransformedShape<Self>`

Applies an affine transform to this shape.

`func size(CGSize) -> some Shape`

Returns a new version of self representing the same shape, but that will ask
it to create its path from a rect of `size`. This does not affect the layout
properties of any views created from the shape (e.g. by filling it).

`func size(width: CGFloat, height: CGFloat) -> some Shape`

Returns a new version of self representing the same shape, but that will ask
it to create its path from a rect of size `(width, height)`. This does not
affect the layout properties of any views created from the shape (e.g. by
filling it).

`func scale(CGFloat, anchor: UnitPoint) -> ScaledShape<Self>`

Scales this shape without changing its bounding frame.

`func scale(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> ScaledShape<Self>`

Scales this shape without changing its bounding frame.

`func rotation(Angle, anchor: UnitPoint) -> RotatedShape<Self>`

Rotates this shape around an anchor point at the angle you specify.

`func offset(CGSize) -> OffsetShape<Self>`

Changes the relative position of this shape using the specified size.

`func offset(CGPoint) -> OffsetShape<Self>`

Changes the relative position of this shape using the specified point.

`func offset(x: CGFloat, y: CGFloat) -> OffsetShape<Self>`

Changes the relative position of this shape using the specified point.

### Setting the stroke characteristics

`func stroke<S>(S, lineWidth: CGFloat) -> some View`

Traces the outline of this shape with a color or gradient.

`func stroke<S>(S, lineWidth: CGFloat, antialiased: Bool) ->
StrokeShapeView<Self, S, EmptyView>`

Traces the outline of this shape with a color or gradient.

`func stroke(lineWidth: CGFloat) -> some Shape`

Returns a new shape that is a stroked copy of `self` with line-width defined
by `lineWidth` and all other properties of `StrokeStyle` having their default
values.

`func stroke<S>(S, style: StrokeStyle) -> some View`

Traces the outline of this shape with a color or gradient.

`func stroke<S>(S, style: StrokeStyle, antialiased: Bool) ->
StrokeShapeView<Self, S, EmptyView>`

Traces the outline of this shape with a color or gradient.

`func stroke(style: StrokeStyle) -> some Shape`

Returns a new shape that is a stroked copy of `self`, using the contents of
`style` to define the stroke characteristics.

### Filling a shape

`func fill<S>(S, style: FillStyle) -> _ShapeView<Self, S>`

Fills this shape with a color or gradient.

`func fill<S>(S, style: FillStyle) -> some View`

Fills this shape with a color or gradient.

`func fill(style: FillStyle) -> some View`

Fills this shape with the foreground color.

### Setting the role

`static var role: ShapeRole`

An indication of how to style a shape.

**Required** Default implementation provided.

### Indicating a layout direction

`var layoutDirectionBehavior: LayoutDirectionBehavior`

Returns the behavior this shape should use for different layout directions.

**Required** Default implementation provided.

### Performing operations on a shape

`func intersection<T>(T, eoFill: Bool) -> some Shape`

Returns a new shape with filled regions common to both shapes.

`func lineIntersection<T>(T, eoFill: Bool) -> some Shape`

Returns a new shape with a line from this shape that overlaps the filled
regions of the given shape.

`func lineSubtraction<T>(T, eoFill: Bool) -> some Shape`

Returns a new shape with a line from this shape that does not overlap the
filled region of the given shape.

`func subtracting<T>(T, eoFill: Bool) -> some Shape`

Returns a new shape with filled regions from this shape that are not in the
given shape.

`func symmetricDifference<T>(T, eoFill: Bool) -> some Shape`

Returns a new shape with filled regions either from this shape or the given
shape, but not in both.

`func union<T>(T, eoFill: Bool) -> some Shape`

Returns a new shape with filled regions in either this shape or the given
shape.

## Relationships

### Inherits From

  * `Animatable`
  * `Sendable`
  * `View`

### Inherited By

  * `InsettableShape`

### Conforming Types

  * `AnyShape`
  * `ButtonBorderShape`
  * `Capsule`
  * `Circle`
  * `ContainerRelativeShape`
  * `Ellipse`
  * `OffsetShape`
  * `Path`
  * `Rectangle`
  * `RotatedShape`
  * `RoundedRectangle`
  * `ScaledShape`
  * `TransformedShape`
  * `UnevenRoundedRectangle`

## See Also

### Defining shape behavior

`protocol ShapeView`

A view that provides a shape that you can use for drawing operations.

`struct AnyShape`

A type-erased shape value.

`enum ShapeRole`

Ways of styling a shape.

`struct StrokeStyle`

The characteristics of a stroke that traces a path.

`struct StrokeShapeView`

A shape provider that strokes its shape.

`struct StrokeBorderShapeView`

A shape provider that strokes the border of its shape.

`struct FillStyle`

A style for rasterizing vector shapes.

`struct FillShapeView`

A shape provider that fills its shape.

Structure

# AnyShape

A type-erased shape value.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    @frozen
    struct AnyShape

## Overview

You can use this type to dynamically switch between shape types:

## Topics

### Creating a shape

`init<S>(S)`

Create an any shape instance from a shape.

## Relationships

### Conforms To

  * `Animatable`
  * `Sendable`
  * `Shape`
  * `View`

## See Also

### Defining shape behavior

`protocol ShapeView`

A view that provides a shape that you can use for drawing operations.

`protocol Shape`

A 2D shape that you can use when drawing a view.

`enum ShapeRole`

Ways of styling a shape.

`struct StrokeStyle`

The characteristics of a stroke that traces a path.

`struct StrokeShapeView`

A shape provider that strokes its shape.

`struct StrokeBorderShapeView`

A shape provider that strokes the border of its shape.

`struct FillStyle`

A style for rasterizing vector shapes.

`struct FillShapeView`

A shape provider that fills its shape.

Enumeration

# ShapeRole

Ways of styling a shape.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    enum ShapeRole

## Topics

### Getting shape roles

`case fill`

Indicates to the shape’s style that SwiftUI fills the shape.

`case stroke`

Indicates to the shape’s style that SwiftUI applies a stroke to the shape’s
path.

`case separator`

Indicates to the shape’s style that SwiftUI uses the shape as a separator.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Defining shape behavior

`protocol ShapeView`

A view that provides a shape that you can use for drawing operations.

`protocol Shape`

A 2D shape that you can use when drawing a view.

`struct AnyShape`

A type-erased shape value.

`struct StrokeStyle`

The characteristics of a stroke that traces a path.

`struct StrokeShapeView`

A shape provider that strokes its shape.

`struct StrokeBorderShapeView`

A shape provider that strokes the border of its shape.

`struct FillStyle`

A style for rasterizing vector shapes.

`struct FillShapeView`

A shape provider that fills its shape.

Structure

# StrokeStyle

The characteristics of a stroke that traces a path.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct StrokeStyle

## Topics

### Creating a stroke style

`init(lineWidth: CGFloat, lineCap: CGLineCap, lineJoin: CGLineJoin,
miterLimit: CGFloat, dash: [CGFloat], dashPhase: CGFloat)`

Creates a new stroke style from the given components.

### Setting stroke style properties

`var lineWidth: CGFloat`

The width of the stroked path.

`var lineCap: CGLineCap`

The endpoint style of a line.

`var lineJoin: CGLineJoin`

The join type of a line.

`var miterLimit: CGFloat`

A threshold used to determine whether to use a bevel instead of a miter at a
join.

`var dash: [CGFloat]`

The lengths of painted and unpainted segments used to make a dashed line.

`var dashPhase: CGFloat`

How far into the dash pattern the line starts.

## Relationships

### Conforms To

  * `Animatable`
  * `Equatable`
  * `Sendable`

## See Also

### Defining shape behavior

`protocol ShapeView`

A view that provides a shape that you can use for drawing operations.

`protocol Shape`

A 2D shape that you can use when drawing a view.

`struct AnyShape`

A type-erased shape value.

`enum ShapeRole`

Ways of styling a shape.

`struct StrokeShapeView`

A shape provider that strokes its shape.

`struct StrokeBorderShapeView`

A shape provider that strokes the border of its shape.

`struct FillStyle`

A style for rasterizing vector shapes.

`struct FillShapeView`

A shape provider that fills its shape.

Structure

# StrokeShapeView

A shape provider that strokes its shape.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    @frozen
    struct StrokeShapeView<Content, Style, Background> where Content : Shape, Style : ShapeStyle, Background : View

## Overview

You don’t create this type directly; it’s the return type of `Shape.stroke`.

## Topics

### Creating a stroke shape view

`init(shape: Content, style: Style, strokeStyle: StrokeStyle, isAntialiased:
Bool, background: Background)`

Create a StrokeShapeView.

### Getting shape view properties

`var background: Background`

The background shown beneath this view.

`var isAntialiased: Bool`

Whether this shape should be drawn antialiased.

`var shape: Content`

The shape that this type draws and provides for other drawing operations.

`var strokeStyle: StrokeStyle`

The stroke style used when stroking this view’s shape.

`var style: Style`

The style that strokes this view’s shape.

## Relationships

### Conforms To

  * `ShapeView`
  * `View`

## See Also

### Defining shape behavior

`protocol ShapeView`

A view that provides a shape that you can use for drawing operations.

`protocol Shape`

A 2D shape that you can use when drawing a view.

`struct AnyShape`

A type-erased shape value.

`enum ShapeRole`

Ways of styling a shape.

`struct StrokeStyle`

The characteristics of a stroke that traces a path.

`struct StrokeBorderShapeView`

A shape provider that strokes the border of its shape.

`struct FillStyle`

A style for rasterizing vector shapes.

`struct FillShapeView`

A shape provider that fills its shape.

Structure

# StrokeBorderShapeView

A shape provider that strokes the border of its shape.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    @frozen
    struct StrokeBorderShapeView<Content, Style, Background> where Content : InsettableShape, Style : ShapeStyle, Background : View

## Overview

You don’t create this type directly; it’s the return type of
`Shape.strokeBorder`.

## Topics

### Creating a stroke border shape view

`init(shape: Content, style: Style, strokeStyle: StrokeStyle, isAntialiased:
Bool, background: Background)`

Create a stroke border shape.

### Getting shape view properties

`var background: Background`

The background shown beneath this view.

`var isAntialiased: Bool`

Whether this shape should be drawn antialiased.

`var shape: Content`

The shape that this type draws and provides for other drawing operations.

`var strokeStyle: StrokeStyle`

The stroke style used when stroking this view’s shape.

`var style: Style`

The style that strokes the border of this view’s shape.

## Relationships

### Conforms To

  * `ShapeView`
  * `View`

## See Also

### Defining shape behavior

`protocol ShapeView`

A view that provides a shape that you can use for drawing operations.

`protocol Shape`

A 2D shape that you can use when drawing a view.

`struct AnyShape`

A type-erased shape value.

`enum ShapeRole`

Ways of styling a shape.

`struct StrokeStyle`

The characteristics of a stroke that traces a path.

`struct StrokeShapeView`

A shape provider that strokes its shape.

`struct FillStyle`

A style for rasterizing vector shapes.

`struct FillShapeView`

A shape provider that fills its shape.

Structure

# FillStyle

A style for rasterizing vector shapes.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct FillStyle

## Topics

### Creating a fill style

`init(eoFill: Bool, antialiased: Bool)`

Creates a new fill style with the specified settings.

### Setting fill style properties

`var isEOFilled: Bool`

A Boolean value that indicates whether to use the even-odd rule when rendering
a shape.

`var isAntialiased: Bool`

A Boolean value that indicates whether to apply antialiasing to the edges of a
shape.

## Relationships

### Conforms To

  * `Equatable`
  * `Sendable`

## See Also

### Defining shape behavior

`protocol ShapeView`

A view that provides a shape that you can use for drawing operations.

`protocol Shape`

A 2D shape that you can use when drawing a view.

`struct AnyShape`

A type-erased shape value.

`enum ShapeRole`

Ways of styling a shape.

`struct StrokeStyle`

The characteristics of a stroke that traces a path.

`struct StrokeShapeView`

A shape provider that strokes its shape.

`struct StrokeBorderShapeView`

A shape provider that strokes the border of its shape.

`struct FillShapeView`

A shape provider that fills its shape.

Structure

# FillShapeView

A shape provider that fills its shape.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    @frozen
    struct FillShapeView<Content, Style, Background> where Content : Shape, Style : ShapeStyle, Background : View

## Overview

You do not create this type directly, it is the return type of `Shape.fill`.

## Topics

### Creating a stroke shape view

`init(shape: Content, style: Style, fillStyle: FillStyle, background:
Background)`

Create a FillShapeView.

### Getting shape view properties

`var background: Background`

The background shown beneath this view.

`var fillStyle: FillStyle`

The fill style used when filling this view’s shape.

`var shape: Content`

The shape that this type draws and provides for other drawing operations.

`var style: Style`

The style that fills this view’s shape.

## Relationships

### Conforms To

  * `ShapeView`
  * `View`

## See Also

### Defining shape behavior

`protocol ShapeView`

A view that provides a shape that you can use for drawing operations.

`protocol Shape`

A 2D shape that you can use when drawing a view.

`struct AnyShape`

A type-erased shape value.

`enum ShapeRole`

Ways of styling a shape.

`struct StrokeStyle`

The characteristics of a stroke that traces a path.

`struct StrokeShapeView`

A shape provider that strokes its shape.

`struct StrokeBorderShapeView`

A shape provider that strokes the border of its shape.

`struct FillStyle`

A style for rasterizing vector shapes.

Structure

# ScaledShape

A shape with a scale transform applied to it.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct ScaledShape<Content> where Content : Shape

## Topics

### Creating a scaled shape

`init(shape: Content, scale: CGSize, anchor: UnitPoint)`

### Getting the shape’s characteristics

`var anchor: UnitPoint`

`var scale: CGSize`

`var shape: Content`

### Supporting types

`var animatableData: ScaledShape<Content>.AnimatableData`

The data to animate.

## Relationships

### Conforms To

  * `Animatable`
  * `Sendable`
  * `Shape`
  * `View`

## See Also

### Transforming a shape

`struct RotatedShape`

A shape with a rotation transform applied to it.

`struct OffsetShape`

A shape with a translation offset transform applied to it.

`struct TransformedShape`

A shape with an affine transform applied to it.

Structure

# RotatedShape

A shape with a rotation transform applied to it.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct RotatedShape<Content> where Content : Shape

## Topics

### Creating a rotated shape

`init(shape: Content, angle: Angle, anchor: UnitPoint)`

### Getting the shape’s characteristics

`var anchor: UnitPoint`

`var angle: Angle`

`var shape: Content`

### Supporting types

`var animatableData: RotatedShape<Content>.AnimatableData`

The data to animate.

## Relationships

### Conforms To

  * `Animatable`
  * `InsettableShape`

Conforms when `Content` conforms to `InsettableShape`.

  * `Sendable`
  * `Shape`
  * `View`

## See Also

### Transforming a shape

`struct ScaledShape`

A shape with a scale transform applied to it.

`struct OffsetShape`

A shape with a translation offset transform applied to it.

`struct TransformedShape`

A shape with an affine transform applied to it.

Structure

# OffsetShape

A shape with a translation offset transform applied to it.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct OffsetShape<Content> where Content : Shape

## Topics

### Creating an offset shape

`init(shape: Content, offset: CGSize)`

### Getting the shape’s characteristics

`var offset: CGSize`

`var shape: Content`

### Supporting types

`var animatableData: OffsetShape<Content>.AnimatableData`

The data to animate.

## Relationships

### Conforms To

  * `Animatable`
  * `InsettableShape`

Conforms when `Content` conforms to `InsettableShape`.

  * `Sendable`
  * `Shape`
  * `View`

## See Also

### Transforming a shape

`struct ScaledShape`

A shape with a scale transform applied to it.

`struct RotatedShape`

A shape with a rotation transform applied to it.

`struct TransformedShape`

A shape with an affine transform applied to it.

Structure

# TransformedShape

A shape with an affine transform applied to it.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct TransformedShape<Content> where Content : Shape

## Topics

### Creating a transformed shape

`init(shape: Content, transform: CGAffineTransform)`

### Getting the shape’s characteristics

`var shape: Content`

`var transform: CGAffineTransform`

## Relationships

### Conforms To

  * `Animatable`
  * `Sendable`
  * `Shape`
  * `View`

## See Also

### Transforming a shape

`struct ScaledShape`

A shape with a scale transform applied to it.

`struct RotatedShape`

A shape with a rotation transform applied to it.

`struct OffsetShape`

A shape with a translation offset transform applied to it.

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

Protocol

# InsettableShape

A shape type that is able to inset itself to produce another shape.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    protocol InsettableShape : Shape

## Topics

### Setting the stroke border characteristics

`func strokeBorder<S>(S, lineWidth: CGFloat, antialiased: Bool) ->
StrokeBorderShapeView<Self, S, EmptyView>`

Returns a view that is the result of filling the `lineWidth`-sized border (aka
inner stroke) of `self` with `content`. This is equivalent to insetting `self`
by `lineWidth / 2` and stroking the resulting shape with `lineWidth` as the
line-width.

`func strokeBorder<S>(S, lineWidth: CGFloat, antialiased: Bool) -> some View`

Returns a view that is the result of filling the `lineWidth`-sized border (aka
inner stroke) of `self` with `content`. This is equivalent to insetting `self`
by `lineWidth / 2` and stroking the resulting shape with `lineWidth` as the
line-width.

`func strokeBorder(lineWidth: CGFloat, antialiased: Bool) -> some View`

Returns a view that is the result of filling the `lineWidth`-sized border (aka
inner stroke) of `self` with the foreground color. This is equivalent to
insetting `self` by `lineWidth / 2` and stroking the resulting shape with
`lineWidth` as the line-width.

`func strokeBorder<S>(S, style: StrokeStyle, antialiased: Bool) ->
StrokeBorderShapeView<Self, S, EmptyView>`

Returns a view that is the result of insetting `self` by `style.lineWidth /
2`, stroking the resulting shape with `style`, and then filling with
`content`.

`func strokeBorder<S>(S, style: StrokeStyle, antialiased: Bool) -> some View`

Returns a view that is the result of insetting `self` by `style.lineWidth /
2`, stroking the resulting shape with `style`, and then filling with
`content`.

`func strokeBorder(style: StrokeStyle, antialiased: Bool) -> some View`

Returns a view that is the result of insetting `self` by `style.lineWidth /
2`, stroking the resulting shape with `style`, and then filling with the
foreground color.

### Setting the inset

`func inset(by: CGFloat) -> Self.InsetShape`

Returns `self` inset by `amount`.

**Required**

` associatedtype InsetShape : InsettableShape`

The type of the inset shape.

**Required**

## Relationships

### Inherits From

  * `Animatable`
  * `Sendable`
  * `Shape`
  * `View`

### Conforming Types

  * `ButtonBorderShape`
  * `Capsule`
  * `Circle`
  * `ContainerRelativeShape`
  * `Ellipse`
  * `OffsetShape`

Conforms when `Content` conforms to `InsettableShape`.

  * `Rectangle`
  * `RotatedShape`

Conforms when `Content` conforms to `InsettableShape`.

  * `RoundedRectangle`
  * `UnevenRoundedRectangle`

## See Also

### Setting a container shape

`func containerShape<T>(T) -> some View`

Sets the container shape to use for any container relative shape within this
view.

`struct ContainerRelativeShape`

A shape that is replaced by an inset version of the current container shape.
If no container shape was defined, is replaced by a rectangle.

Structure

# ContainerRelativeShape

A shape that is replaced by an inset version of the current container shape.
If no container shape was defined, is replaced by a rectangle.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    @frozen
    struct ContainerRelativeShape

## Topics

### Creating the shape

`init()`

## Relationships

### Conforms To

  * `Animatable`
  * `InsettableShape`
  * `Sendable`
  * `Shape`
  * `View`

## See Also

### Setting a container shape

`func containerShape<T>(T) -> some View`

Sets the container shape to use for any container relative shape within this
view.

`protocol InsettableShape`

A shape type that is able to inset itself to produce another shape.

