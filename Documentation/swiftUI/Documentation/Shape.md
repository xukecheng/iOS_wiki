Type Property

# buttonBorder

A shape that defers to the environment to determine the resolved button border
shape.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static var buttonBorder: ButtonBorderShape { get }

Available when `Self` is `ButtonBorderShape`.

## Discussion

You can override the resolved shape in a given view hierarchy by using the
`buttonBorderShape(_:)` modifier. If no button border shape is specified, it
is resolved automatically for the given context and platform.

## See Also

### Getting standard shapes

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

Type Property

# capsule

A capsule shape aligned inside the frame of the view containing it.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static var capsule: Capsule { get }

Available when `Self` is `Capsule`.

## Discussion

A capsule shape is equivalent to a rounded rectangle where the corner radius
is chosen as half the length of the rectangle’s smallest edge.

## See Also

### Getting standard shapes

`static var buttonBorder: ButtonBorderShape`

A shape that defers to the environment to determine the resolved button border
shape.

Available when `Self` is `ButtonBorderShape`.

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

Type Method

# capsule(style:)

A capsule shape aligned inside the frame of the view containing it.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static func capsule(style: RoundedCornerStyle) -> Self

Available when `Self` is `Capsule`.

## Discussion

A capsule shape is equivalent to a rounded rectangle where the corner radius
is chosen as half the length of the rectangle’s smallest edge.

## See Also

### Getting standard shapes

`static var buttonBorder: ButtonBorderShape`

A shape that defers to the environment to determine the resolved button border
shape.

Available when `Self` is `ButtonBorderShape`.

`static var capsule: Capsule`

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

Type Property

# circle

A circle centered on the frame of the view containing it.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static var circle: Circle { get }

Available when `Self` is `Circle`.

## Discussion

The circle’s radius equals half the length of the frame rectangle’s smallest
edge.

## See Also

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

Type Property

# containerRelative

A shape that is replaced by an inset version of the current container shape.
If no container shape was defined, is replaced by a rectangle.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    static var containerRelative: ContainerRelativeShape { get }

Available when `Self` is `ContainerRelativeShape`.

## See Also

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

Type Property

# ellipse

An ellipse aligned inside the frame of the view containing it.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static var ellipse: Ellipse { get }

Available when `Self` is `Ellipse`.

## See Also

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

Type Property

# rect

A rectangular shape aligned inside the frame of the view containing it.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static var rect: Rectangle { get }

Available when `Self` is `Rectangle`.

## See Also

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

Type Method

# rect(cornerRadii:style:)

A rectangular shape with rounded corners with different values, aligned inside
the frame of the view containing it.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static func rect(
        cornerRadii: RectangleCornerRadii,
        style: RoundedCornerStyle = .continuous
    ) -> Self

Available when `Self` is `UnevenRoundedRectangle`.

## See Also

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

Type Method

# rect(cornerRadius:style:)

A rectangular shape with rounded corners, aligned inside the frame of the view
containing it.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static func rect(
        cornerRadius: CGFloat,
        style: RoundedCornerStyle = .continuous
    ) -> Self

Available when `Self` is `RoundedRectangle`.

## See Also

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

Type Method

# rect(cornerSize:style:)

A rectangular shape with rounded corners, aligned inside the frame of the view
containing it.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static func rect(
        cornerSize: CGSize,
        style: RoundedCornerStyle = .continuous
    ) -> Self

Available when `Self` is `RoundedRectangle`.

## See Also

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

`static func rect(topLeadingRadius: CGFloat, bottomLeadingRadius: CGFloat,
bottomTrailingRadius: CGFloat, topTrailingRadius: CGFloat, style:
RoundedCornerStyle) -> Self`

A rectangular shape with rounded corners with different values, aligned inside
the frame of the view containing it.

Available when `Self` is `UnevenRoundedRectangle`.

Type Method

#
rect(topLeadingRadius:bottomLeadingRadius:bottomTrailingRadius:topTrailingRadius:style:)

A rectangular shape with rounded corners with different values, aligned inside
the frame of the view containing it.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static func rect(
        topLeadingRadius: CGFloat = 0,
        bottomLeadingRadius: CGFloat = 0,
        bottomTrailingRadius: CGFloat = 0,
        topTrailingRadius: CGFloat = 0,
        style: RoundedCornerStyle = .continuous
    ) -> Self

Available when `Self` is `UnevenRoundedRectangle`.

## See Also

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

Instance Method

# sizeThatFits(_:)

Returns the size of the view that will render the shape, given a proposed
size.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func sizeThatFits(_ proposal: ProposedViewSize) -> CGSize

**Required** Default implementation provided.

##  Parameters

`proposal`

    

A size proposal for the container.

## Return Value

A size that indicates how much space the shape needs.

## Discussion

Implement this method to tell the container of the shape how much space the
shape needs to render itself, given a size proposal.

See `sizeThatFits(proposal:subviews:cache:)` for more details about how the
layout system chooses the size of views.

## Default Implementations

### Shape Implementations

`func sizeThatFits(ProposedViewSize) -> CGSize`

Returns the original proposal, with nil components replaced by a small
positive value.

## See Also

### Defining a shape’s size and path

`func path(in: CGRect) -> Path`

Describes this shape as a path within a rectangular frame of reference.

**Required**

Instance Method

# path(in:)

Describes this shape as a path within a rectangular frame of reference.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func path(in rect: CGRect) -> Path

**Required**

##  Parameters

`rect`

    

The frame of reference for describing this shape.

## Return Value

A path that describes this shape.

## See Also

### Defining a shape’s size and path

`func sizeThatFits(ProposedViewSize) -> CGSize`

Returns the size of the view that will render the shape, given a proposed
size.

**Required** Default implementation provided.

Instance Method

# trim(from:to:)

Trims this shape by a fractional amount based on its representation as a path.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func trim(
        from startFraction: CGFloat = 0,
        to endFraction: CGFloat = 1
    ) -> some Shape
    

##  Parameters

`startFraction`

    

The fraction of the way through drawing this shape where drawing starts.

`endFraction`

    

The fraction of the way through drawing this shape where drawing ends.

## Return Value

A shape built by capturing a portion of this shape’s path.

## Discussion

To create a `Shape` instance, you define the shape’s path using lines and
curves. Use the `trim(from:to:)` method to draw a portion of a shape by
ignoring portions of the beginning and ending of the shape’s path.

For example, if you’re drawing a figure eight or infinity symbol (∞) starting
from its center, setting the `startFraction` and `endFraction` to different
values determines the parts of the overall shape.

The following example shows a simplified infinity symbol that draws only three
quarters of the full shape. That is, of the two lobes of the symbol, one lobe
is complete and the other is half complete.

Changing the parameters of `trim(from:to:)` to `.trim(from: 0, to: 1)` draws
the full infinity symbol, while `.trim(from: 0, to: 0.5)` draws only the left
lobe of the symbol.

## See Also

### Transforming a shape

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

Instance Method

# transform(_:)

Applies an affine transform to this shape.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func transform(_ transform: CGAffineTransform) -> TransformedShape<Self>

##  Parameters

`transform`

    

The affine transformation matrix to apply to this shape.

## Return Value

A transformed shape, based on its matrix values.

## Discussion

Affine transforms present a mathematical approach to applying combinations of
rotation, scaling, translation, and skew to shapes.

## See Also

### Transforming a shape

`func trim(from: CGFloat, to: CGFloat) -> some Shape`

Trims this shape by a fractional amount based on its representation as a path.

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

Instance Method

# size(_:)

Returns a new version of self representing the same shape, but that will ask
it to create its path from a rect of `size`. This does not affect the layout
properties of any views created from the shape (e.g. by filling it).

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func size(_ size: CGSize) -> some Shape
    

## See Also

### Transforming a shape

`func trim(from: CGFloat, to: CGFloat) -> some Shape`

Trims this shape by a fractional amount based on its representation as a path.

`func transform(CGAffineTransform) -> TransformedShape<Self>`

Applies an affine transform to this shape.

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

Instance Method

# size(width:height:)

Returns a new version of self representing the same shape, but that will ask
it to create its path from a rect of size `(width, height)`. This does not
affect the layout properties of any views created from the shape (e.g. by
filling it).

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func size(
        width: CGFloat,
        height: CGFloat
    ) -> some Shape
    

## See Also

### Transforming a shape

`func trim(from: CGFloat, to: CGFloat) -> some Shape`

Trims this shape by a fractional amount based on its representation as a path.

`func transform(CGAffineTransform) -> TransformedShape<Self>`

Applies an affine transform to this shape.

`func size(CGSize) -> some Shape`

Returns a new version of self representing the same shape, but that will ask
it to create its path from a rect of `size`. This does not affect the layout
properties of any views created from the shape (e.g. by filling it).

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

Instance Method

# scale(_:anchor:)

Scales this shape without changing its bounding frame.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func scale(
        _ scale: CGFloat,
        anchor: UnitPoint = .center
    ) -> ScaledShape<Self>

##  Parameters

`scale`

    

The multiplication factor used to resize this shape. A value of `0` scales the
shape to have no size, `0.5` scales to half size in both dimensions, `2`
scales to twice the regular size, and so on.

## Return Value

A scaled form of this shape.

## See Also

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

Instance Method

# scale(x:y:anchor:)

Scales this shape without changing its bounding frame.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func scale(
        x: CGFloat = 1,
        y: CGFloat = 1,
        anchor: UnitPoint = .center
    ) -> ScaledShape<Self>

##  Parameters

`x`

    

The multiplication factor used to resize this shape along its x-axis.

`y`

    

The multiplication factor used to resize this shape along its y-axis.

## Return Value

A scaled form of this shape.

## Discussion

Both the `x` and `y` multiplication factors halve their respective dimension’s
size when set to `0.5`, maintain their existing size when set to `1`, double
their size when set to `2`, and so forth.

## See Also

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

`func rotation(Angle, anchor: UnitPoint) -> RotatedShape<Self>`

Rotates this shape around an anchor point at the angle you specify.

`func offset(CGSize) -> OffsetShape<Self>`

Changes the relative position of this shape using the specified size.

`func offset(CGPoint) -> OffsetShape<Self>`

Changes the relative position of this shape using the specified point.

`func offset(x: CGFloat, y: CGFloat) -> OffsetShape<Self>`

Changes the relative position of this shape using the specified point.

Instance Method

# rotation(_:anchor:)

Rotates this shape around an anchor point at the angle you specify.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func rotation(
        _ angle: Angle,
        anchor: UnitPoint = .center
    ) -> RotatedShape<Self>

##  Parameters

`angle`

    

The angle of rotation to apply. Positive angles rotate clockwise; negative
angles rotate counterclockwise.

`anchor`

    

The point to rotate the shape around.

## Return Value

A rotated shape.

## Discussion

The following example rotates a square by 45 degrees to the right to create a
diamond shape:

## See Also

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

`func offset(CGSize) -> OffsetShape<Self>`

Changes the relative position of this shape using the specified size.

`func offset(CGPoint) -> OffsetShape<Self>`

Changes the relative position of this shape using the specified point.

`func offset(x: CGFloat, y: CGFloat) -> OffsetShape<Self>`

Changes the relative position of this shape using the specified point.

Instance Method

# offset(_:)

Changes the relative position of this shape using the specified size.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func offset(_ offset: CGSize) -> OffsetShape<Self>

##  Parameters

`offset`

    

The amount, in points, by which you offset the shape. Negative numbers are to
the left and up; positive numbers are to the right and down.

## Return Value

A shape offset by the specified amount.

## Discussion

The following example renders two circles. It places one circle at its default
position. The second circle is outlined with a stroke, positioned on top of
the first circle and offset by 100 points to the left and 50 points below.

## See Also

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

`func offset(CGPoint) -> OffsetShape<Self>`

Changes the relative position of this shape using the specified point.

`func offset(x: CGFloat, y: CGFloat) -> OffsetShape<Self>`

Changes the relative position of this shape using the specified point.

Instance Method

# offset(_:)

Changes the relative position of this shape using the specified point.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func offset(_ offset: CGPoint) -> OffsetShape<Self>

##  Parameters

`offset`

    

The amount, in points, by which you offset the shape. Negative numbers are to
the left and up; positive numbers are to the right and down.

## Return Value

A shape offset by the specified amount.

## Discussion

The following example renders two circles. It places one circle at its default
position. The second circle is outlined with a stroke, positioned on top of
the first circle and offset by 100 points to the left and 50 points below.

## See Also

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

`func offset(x: CGFloat, y: CGFloat) -> OffsetShape<Self>`

Changes the relative position of this shape using the specified point.

Instance Method

# offset(x:y:)

Changes the relative position of this shape using the specified point.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func offset(
        x: CGFloat = 0,
        y: CGFloat = 0
    ) -> OffsetShape<Self>

##  Parameters

`x`

    

The horizontal amount, in points, by which you offset the shape. Negative
numbers are to the left and positive numbers are to the right.

`y`

    

The vertical amount, in points, by which you offset the shape. Negative
numbers are up and positive numbers are down.

## Return Value

A shape offset by the specified amount.

## Discussion

The following example renders two circles. It places one circle at its default
position. The second circle is outlined with a stroke, positioned on top of
the first circle and offset by 100 points to the left and 50 points below.

## See Also

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

Instance Method

# stroke(_:lineWidth:)

Traces the outline of this shape with a color or gradient.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func stroke<S>(
        _ content: S,
        lineWidth: CGFloat = 1
    ) -> some View where S : ShapeStyle
    

##  Parameters

`content`

    

The color or gradient with which to stroke this shape.

`lineWidth`

    

The width of the stroke that outlines this shape.

## Return Value

A stroked shape.

## Discussion

The following example draws a circle with a purple stroke:

## See Also

### Setting the stroke characteristics

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

Instance Method

# stroke(_:lineWidth:antialiased:)

Traces the outline of this shape with a color or gradient.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func stroke<S>(
        _ content: S,
        lineWidth: CGFloat = 1,
        antialiased: Bool = true
    ) -> StrokeShapeView<Self, S, EmptyView> where S : ShapeStyle

##  Parameters

`content`

    

The color or gradient with which to stroke this shape.

`lineWidth`

    

The width of the stroke that outlines this shape.

## Return Value

A stroked shape.

## Discussion

The following example draws a circle with a purple stroke:

## See Also

### Setting the stroke characteristics

`func stroke<S>(S, lineWidth: CGFloat) -> some View`

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

Instance Method

# stroke(lineWidth:)

Returns a new shape that is a stroked copy of `self` with line-width defined
by `lineWidth` and all other properties of `StrokeStyle` having their default
values.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func stroke(lineWidth: CGFloat = 1) -> some Shape
    

## See Also

### Setting the stroke characteristics

`func stroke<S>(S, lineWidth: CGFloat) -> some View`

Traces the outline of this shape with a color or gradient.

`func stroke<S>(S, lineWidth: CGFloat, antialiased: Bool) ->
StrokeShapeView<Self, S, EmptyView>`

Traces the outline of this shape with a color or gradient.

`func stroke<S>(S, style: StrokeStyle) -> some View`

Traces the outline of this shape with a color or gradient.

`func stroke<S>(S, style: StrokeStyle, antialiased: Bool) ->
StrokeShapeView<Self, S, EmptyView>`

Traces the outline of this shape with a color or gradient.

`func stroke(style: StrokeStyle) -> some Shape`

Returns a new shape that is a stroked copy of `self`, using the contents of
`style` to define the stroke characteristics.

Instance Method

# stroke(_:style:)

Traces the outline of this shape with a color or gradient.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func stroke<S>(
        _ content: S,
        style: StrokeStyle
    ) -> some View where S : ShapeStyle
    

##  Parameters

`content`

    

The color or gradient with which to stroke this shape.

`style`

    

The stroke characteristics — such as the line’s width and whether the stroke
is dashed — that determine how to render this shape.

## Return Value

A stroked shape.

## Discussion

The following example adds a dashed purple stroke to a `Capsule`:

## See Also

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

`func stroke<S>(S, style: StrokeStyle, antialiased: Bool) ->
StrokeShapeView<Self, S, EmptyView>`

Traces the outline of this shape with a color or gradient.

`func stroke(style: StrokeStyle) -> some Shape`

Returns a new shape that is a stroked copy of `self`, using the contents of
`style` to define the stroke characteristics.

Instance Method

# stroke(_:style:antialiased:)

Traces the outline of this shape with a color or gradient.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func stroke<S>(
        _ content: S,
        style: StrokeStyle,
        antialiased: Bool = true
    ) -> StrokeShapeView<Self, S, EmptyView> where S : ShapeStyle

##  Parameters

`content`

    

The color or gradient with which to stroke this shape.

`style`

    

The stroke characteristics — such as the line’s width and whether the stroke
is dashed — that determine how to render this shape.

## Return Value

A stroked shape.

## Discussion

The following example adds a dashed purple stroke to a `Capsule`:

## See Also

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

`func stroke(style: StrokeStyle) -> some Shape`

Returns a new shape that is a stroked copy of `self`, using the contents of
`style` to define the stroke characteristics.

Instance Method

# stroke(style:)

Returns a new shape that is a stroked copy of `self`, using the contents of
`style` to define the stroke characteristics.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func stroke(style: StrokeStyle) -> some Shape
    

## See Also

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

Instance Method

# fill(_:style:)

Fills this shape with a color or gradient.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func fill<S>(
        _ content: S = .foreground,
        style: FillStyle = FillStyle()
    ) -> _ShapeView<Self, S> where S : ShapeStyle

##  Parameters

`content`

    

The color or gradient to use when filling this shape.

`style`

    

The style options that determine how the fill renders.

## Return Value

A shape filled with the color or gradient you supply.

## See Also

### Filling a shape

`func fill<S>(S, style: FillStyle) -> some View`

Fills this shape with a color or gradient.

`func fill(style: FillStyle) -> some View`

Fills this shape with the foreground color.

Instance Method

# fill(_:style:)

Fills this shape with a color or gradient.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func fill<S>(
        _ content: S,
        style: FillStyle = FillStyle()
    ) -> some View where S : ShapeStyle
    

##  Parameters

`content`

    

The color or gradient to use when filling this shape.

`style`

    

The style options that determine how the fill renders.

## Return Value

A shape filled with the color or gradient you supply.

## See Also

### Filling a shape

`func fill<S>(S, style: FillStyle) -> _ShapeView<Self, S>`

Fills this shape with a color or gradient.

`func fill(style: FillStyle) -> some View`

Fills this shape with the foreground color.

Instance Method

# fill(style:)

Fills this shape with the foreground color.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func fill(style: FillStyle = FillStyle()) -> some View
    

##  Parameters

`style`

    

The style options that determine how the fill renders.

## Return Value

A shape filled with the foreground color.

## See Also

### Filling a shape

`func fill<S>(S, style: FillStyle) -> _ShapeView<Self, S>`

Fills this shape with a color or gradient.

`func fill<S>(S, style: FillStyle) -> some View`

Fills this shape with a color or gradient.

Type Property

# role

An indication of how to style a shape.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var role: ShapeRole { get }

**Required** Default implementation provided.

## Discussion

SwiftUI looks at a shape’s role when deciding how to apply a `ShapeStyle` at
render time. The `Shape` protocol provides a default implementation with a
value of `ShapeRole.fill`. If you create a composite shape, you can provide an
override of this property to return another value, if appropriate.

## Default Implementations

### Shape Implementations

`static var role: ShapeRole`

An indication of how to style a shape.

Instance Property

# layoutDirectionBehavior

Returns the behavior this shape should use for different layout directions.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var layoutDirectionBehavior: LayoutDirectionBehavior { get }

**Required** Default implementation provided.

## Discussion

If the layoutDirectionBehavior for a Shape is one that mirrors, the shape’s
path will be mirrored horizontally when in the specified layout direction.
When mirrored, the individual points of the path will be transformed.

Defaults to `.mirrors` when deploying on iOS 17.0, macOS 14.0, tvOS 17.0,
watchOS 10.0 and later, and to `.fixed` if not. To mirror a path when
deploying to earlier releases, either use
`View.flipsForRightToLeftLayoutDirection` for a filled or stroked shape or
conditionally mirror the points in the path of the shape.

## Default Implementations

### Shape Implementations

`var layoutDirectionBehavior: LayoutDirectionBehavior`

Returns the behavior this shape should use for different layout directions.

Instance Method

# intersection(_:eoFill:)

Returns a new shape with filled regions common to both shapes.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func intersection<T>(
        _ other: T,
        eoFill: Bool = false
    ) -> some Shape where T : Shape
    

##  Parameters

`other`

    

The shape to intersect.

`eoFill`

    

Whether to use the even-odd rule for determining which areas to treat as the
interior of the shapes (if true), or the non-zero rule (if false).

## Return Value

A new shape.

## Discussion

The filled region of the resulting shape is the overlapping area of the filled
region of both shapes. This can be used to clip the fill of a shape to a mask.

Any unclosed subpaths in either shape are assumed to be closed. The result of
filling this shape using either even-odd or non-zero fill rules is identical.

## See Also

### Performing operations on a shape

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

Instance Method

# lineIntersection(_:eoFill:)

Returns a new shape with a line from this shape that overlaps the filled
regions of the given shape.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func lineIntersection<T>(
        _ other: T,
        eoFill: Bool = false
    ) -> some Shape where T : Shape
    

##  Parameters

`other`

    

The shape to intersect.

`eoFill`

    

Whether to use the even-odd rule for determining which areas to treat as the
interior of the shapes (if true), or the non-zero rule (if false).

## Return Value

A new shape.

## Discussion

The line of the resulting shape is the line of this shape that overlaps the
filled region of `other`.

Intersected subpaths that are clipped create open subpaths. Closed subpaths
that do not intersect `other` remain closed.

## See Also

### Performing operations on a shape

`func intersection<T>(T, eoFill: Bool) -> some Shape`

Returns a new shape with filled regions common to both shapes.

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

Instance Method

# lineSubtraction(_:eoFill:)

Returns a new shape with a line from this shape that does not overlap the
filled region of the given shape.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func lineSubtraction<T>(
        _ other: T,
        eoFill: Bool = false
    ) -> some Shape where T : Shape
    

##  Parameters

`other`

    

The shape to subtract.

`eoFill`

    

Whether to use the even-odd rule for determining which areas to treat as the
interior of the shapes (if true), or the non-zero rule (if false).

## Return Value

A new shape.

## Discussion

The line of the resulting shape is the line of this shape that does not
overlap the filled region of `other`.

Intersected subpaths that are clipped create open subpaths. Closed subpaths
that do not intersect `other` remain closed.

## See Also

### Performing operations on a shape

`func intersection<T>(T, eoFill: Bool) -> some Shape`

Returns a new shape with filled regions common to both shapes.

`func lineIntersection<T>(T, eoFill: Bool) -> some Shape`

Returns a new shape with a line from this shape that overlaps the filled
regions of the given shape.

`func subtracting<T>(T, eoFill: Bool) -> some Shape`

Returns a new shape with filled regions from this shape that are not in the
given shape.

`func symmetricDifference<T>(T, eoFill: Bool) -> some Shape`

Returns a new shape with filled regions either from this shape or the given
shape, but not in both.

`func union<T>(T, eoFill: Bool) -> some Shape`

Returns a new shape with filled regions in either this shape or the given
shape.

Instance Method

# subtracting(_:eoFill:)

Returns a new shape with filled regions from this shape that are not in the
given shape.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func subtracting<T>(
        _ other: T,
        eoFill: Bool = false
    ) -> some Shape where T : Shape
    

##  Parameters

`other`

    

The shape to subtract.

`eoFill`

    

Whether to use the even-odd rule for determining which areas to treat as the
interior of the shapes (if true), or the non-zero rule (if false).

## Return Value

A new shape.

## Discussion

The filled region of the resulting shape is the filled region of this shape
with the filled region `other` removed from it.

Any unclosed subpaths in either shape are assumed to be closed. The result of
filling this shape using either even-odd or non-zero fill rules is identical.

## See Also

### Performing operations on a shape

`func intersection<T>(T, eoFill: Bool) -> some Shape`

Returns a new shape with filled regions common to both shapes.

`func lineIntersection<T>(T, eoFill: Bool) -> some Shape`

Returns a new shape with a line from this shape that overlaps the filled
regions of the given shape.

`func lineSubtraction<T>(T, eoFill: Bool) -> some Shape`

Returns a new shape with a line from this shape that does not overlap the
filled region of the given shape.

`func symmetricDifference<T>(T, eoFill: Bool) -> some Shape`

Returns a new shape with filled regions either from this shape or the given
shape, but not in both.

`func union<T>(T, eoFill: Bool) -> some Shape`

Returns a new shape with filled regions in either this shape or the given
shape.

Instance Method

# symmetricDifference(_:eoFill:)

Returns a new shape with filled regions either from this shape or the given
shape, but not in both.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func symmetricDifference<T>(
        _ other: T,
        eoFill: Bool = false
    ) -> some Shape where T : Shape
    

##  Parameters

`other`

    

The shape to difference.

`eoFill`

    

Whether to use the even-odd rule for determining which areas to treat as the
interior of the shapes (if true), or the non-zero rule (if false).

## Return Value

A new shape.

## Discussion

The filled region of the resulting shape is the filled region contained in
either this shape or `other`, but not both.

Any unclosed subpaths in either shape are assumed to be closed. The result of
filling this shape using either even-odd or non-zero fill rules is identical.

## See Also

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

`func union<T>(T, eoFill: Bool) -> some Shape`

Returns a new shape with filled regions in either this shape or the given
shape.

Instance Method

# union(_:eoFill:)

Returns a new shape with filled regions in either this shape or the given
shape.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func union<T>(
        _ other: T,
        eoFill: Bool = false
    ) -> some Shape where T : Shape
    

##  Parameters

`other`

    

The shape to union.

`eoFill`

    

Whether to use the even-odd rule for determining which areas to treat as the
interior of the shapes (if true), or the non-zero rule (if false).

## Return Value

A new shape.

## Discussion

The filled region of resulting shape is the combination of the filled region
of both shapes added together.

Any unclosed subpaths in either shape are assumed to be closed. The result of
filling this shape using either even-odd or non-zero fill rules is identical.

## See Also

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

