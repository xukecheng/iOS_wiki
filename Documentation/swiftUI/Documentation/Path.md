Initializer

# init()

Creates an empty path.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init()

## See Also

### Creating a path

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

Initializer

# init(_:)

Creates an empty path, then executes a closure to add its initial elements.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(_ callback: (inout Path) -> ())

##  Parameters

`callback`

    

The Swift function that will be called to initialize the new path.

## See Also

### Creating a path

`init()`

Creates an empty path.

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

Initializer

# init(_:)

Creates a path from a copy of a mutable shape path.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(_ path: CGMutablePath)

##  Parameters

`path`

    

The CoreGraphics path to initialize the new path from.

## See Also

### Creating a path

`init()`

Creates an empty path.

`init((inout Path) -> ())`

Creates an empty path, then executes a closure to add its initial elements.

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

Initializer

# init(_:)

Creates a path from an immutable shape path.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(_ path: CGPath)

##  Parameters

`path`

    

The immutable CoreGraphics path to initialize the new path from.

## See Also

### Creating a path

`init()`

Creates an empty path.

`init((inout Path) -> ())`

Creates an empty path, then executes a closure to add its initial elements.

`init(CGMutablePath)`

Creates a path from a copy of a mutable shape path.

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

Initializer

# init(_:)

Initializes from the result of a previous call to `Path.stringRepresentation`.
Fails if the `string` does not describe a valid path.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init?(_ string: String)

## See Also

### Creating a path

`init()`

Creates an empty path.

`init((inout Path) -> ())`

Creates an empty path, then executes a closure to add its initial elements.

`init(CGMutablePath)`

Creates a path from a copy of a mutable shape path.

`init(CGPath)`

Creates a path from an immutable shape path.

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

Initializer

# init(_:)

Creates a path containing a rectangle.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(_ rect: CGRect)

##  Parameters

`rect`

    

The rectangle to add.

## Discussion

This is a convenience function that creates a path of a rectangle. Using this
convenience function is more efficient than creating a path and adding a
rectangle to it.

Calling this function is equivalent to using `minX` and related properties to
find the corners of the rectangle, then using the `move(to:)`, `addLine(to:)`,
and `closeSubpath()` functions to add the rectangle.

## See Also

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

Initializer

# init(ellipseIn:)

Creates a path as an ellipse within the given rectangle.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(ellipseIn rect: CGRect)

##  Parameters

`rect`

    

The rectangle that bounds the ellipse.

## Discussion

This is a convenience function that creates a path of an ellipse. Using this
convenience function is more efficient than creating a path and adding an
ellipse to it.

The ellipse is approximated by a sequence of Bézier curves. Its center is the
midpoint of the rectangle defined by the rect parameter. If the rectangle is
square, then the ellipse is circular with a radius equal to one-half the width
(or height) of the rectangle. If the rect parameter specifies a rectangular
shape, then the major and minor axes of the ellipse are defined by the width
and height of the rectangle.

The ellipse forms a complete subpath of the path—that is, the ellipse drawing
starts with a move-to operation and ends with a close-subpath operation, with
all moves oriented in the clockwise direction. If you supply an affine
transform, then the constructed Bézier curves that define the ellipse are
transformed before they are added to the path.

## See Also

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

`init(roundedRect: CGRect, cornerRadius: CGFloat, style: RoundedCornerStyle)`

Creates a path containing a rounded rectangle.

`init(roundedRect: CGRect, cornerSize: CGSize, style: RoundedCornerStyle)`

Creates a path containing a rounded rectangle.

`init(roundedRect: CGRect, cornerRadii: RectangleCornerRadii, style:
RoundedCornerStyle)`

Creates a path as the given rounded rectangle, which may have uneven corner
radii.

Initializer

# init(roundedRect:cornerRadius:style:)

Creates a path containing a rounded rectangle.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        roundedRect rect: CGRect,
        cornerRadius: CGFloat,
        style: RoundedCornerStyle = .continuous
    )

##  Parameters

`rect`

    

A rectangle, specified in user space coordinates.

`cornerRadius`

    

The radius of all corners of the rectangle, specified in user space
coordinates.

`style`

    

The corner style. Defaults to the `continous` style if not specified.

## Discussion

This is a convenience function that creates a path of a rounded rectangle.
Using this convenience function is more efficient than creating a path and
adding a rounded rectangle to it.

## See Also

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

`init(roundedRect: CGRect, cornerSize: CGSize, style: RoundedCornerStyle)`

Creates a path containing a rounded rectangle.

`init(roundedRect: CGRect, cornerRadii: RectangleCornerRadii, style:
RoundedCornerStyle)`

Creates a path as the given rounded rectangle, which may have uneven corner
radii.

Initializer

# init(roundedRect:cornerSize:style:)

Creates a path containing a rounded rectangle.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        roundedRect rect: CGRect,
        cornerSize: CGSize,
        style: RoundedCornerStyle = .continuous
    )

##  Parameters

`rect`

    

A rectangle, specified in user space coordinates.

`cornerSize`

    

The size of the corners, specified in user space coordinates.

`style`

    

The corner style. Defaults to the `continous` style if not specified.

## Discussion

This is a convenience function that creates a path of a rounded rectangle.
Using this convenience function is more efficient than creating a path and
adding a rounded rectangle to it.

## See Also

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

`init(roundedRect: CGRect, cornerRadii: RectangleCornerRadii, style:
RoundedCornerStyle)`

Creates a path as the given rounded rectangle, which may have uneven corner
radii.

Initializer

# init(roundedRect:cornerRadii:style:)

Creates a path as the given rounded rectangle, which may have uneven corner
radii.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init(
        roundedRect rect: CGRect,
        cornerRadii: RectangleCornerRadii,
        style: RoundedCornerStyle = .continuous
    )

##  Parameters

`rect`

    

A rectangle, specified in user space coordinates.

`cornerRadii`

    

The radius of each corner of the rectangle, specified in user space
coordinates.

`style`

    

The corner style. Defaults to the `continous` style if not specified.

## Discussion

This is a convenience function that creates a path of a rounded rectangle.
Using this function is more efficient than creating a path and adding a
rounded rectangle to it.

## See Also

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

Instance Property

# boundingRect

A rectangle containing all path segments.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var boundingRect: CGRect { get }

## Discussion

This is the smallest rectangle completely enclosing all points in the path but
not including control points for Bézier curves.

## See Also

### Getting the path’s characteristics

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

Instance Property

# cgPath

An immutable path representing the elements in the path.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var cgPath: CGPath { get }

## See Also

### Getting the path’s characteristics

`var boundingRect: CGRect`

A rectangle containing all path segments.

`func contains(CGPoint, eoFill: Bool) -> Bool`

Returns true if the path contains a specified point.

`var currentPoint: CGPoint?`

Returns the last point in the path, or nil if the path contains no points.

`var description: String`

A description of the path that may be used to recreate the path via
`init?(_:)`.

`var isEmpty: Bool`

A Boolean value indicating whether the path contains zero elements.

Instance Method

# contains(_:eoFill:)

Returns true if the path contains a specified point.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func contains(
        _ p: CGPoint,
        eoFill: Bool = false
    ) -> Bool

## Discussion

If `eoFill` is true, this method uses the even-odd rule to define which points
are inside the path. Otherwise, it uses the non-zero rule.

## See Also

### Getting the path’s characteristics

`var boundingRect: CGRect`

A rectangle containing all path segments.

`var cgPath: CGPath`

An immutable path representing the elements in the path.

`var currentPoint: CGPoint?`

Returns the last point in the path, or nil if the path contains no points.

`var description: String`

A description of the path that may be used to recreate the path via
`init?(_:)`.

`var isEmpty: Bool`

A Boolean value indicating whether the path contains zero elements.

Instance Property

# currentPoint

Returns the last point in the path, or nil if the path contains no points.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var currentPoint: CGPoint? { get }

## See Also

### Getting the path’s characteristics

`var boundingRect: CGRect`

A rectangle containing all path segments.

`var cgPath: CGPath`

An immutable path representing the elements in the path.

`func contains(CGPoint, eoFill: Bool) -> Bool`

Returns true if the path contains a specified point.

`var description: String`

A description of the path that may be used to recreate the path via
`init?(_:)`.

`var isEmpty: Bool`

A Boolean value indicating whether the path contains zero elements.

Instance Property

# description

A description of the path that may be used to recreate the path via
`init?(_:)`.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var description: String { get }

## See Also

### Getting the path’s characteristics

`var boundingRect: CGRect`

A rectangle containing all path segments.

`var cgPath: CGPath`

An immutable path representing the elements in the path.

`func contains(CGPoint, eoFill: Bool) -> Bool`

Returns true if the path contains a specified point.

`var currentPoint: CGPoint?`

Returns the last point in the path, or nil if the path contains no points.

`var isEmpty: Bool`

A Boolean value indicating whether the path contains zero elements.

Instance Property

# isEmpty

A Boolean value indicating whether the path contains zero elements.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var isEmpty: Bool { get }

## See Also

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

Instance Method

# move(to:)

Begins a new subpath at the specified point.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    mutating func move(to end: CGPoint)

##  Parameters

`end`

    

The point, in user space coordinates, at which to start a new subpath.

## Discussion

The specified point becomes the start point of a new subpath. The current
point is set to this start point.

## See Also

### Drawing a path

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

Instance Method

# addArc(center:radius:startAngle:endAngle:clockwise:transform:)

Adds an arc of a circle to the path, specified with a radius and angles.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    mutating func addArc(
        center: CGPoint,
        radius: CGFloat,
        startAngle: Angle,
        endAngle: Angle,
        clockwise: Bool,
        transform: CGAffineTransform = .identity
    )

##  Parameters

`center`

    

The center of the arc, in user space coordinates.

`radius`

    

The radius of the arc, in user space coordinates.

`startAngle`

    

The angle to the starting point of the arc, measured from the positive x-axis.

`endAngle`

    

The angle to the end point of the arc, measured from the positive x-axis.

`clockwise`

    

true to make a clockwise arc; false to make a counterclockwise arc.

`transform`

    

An affine transform to apply to the arc before adding to the path. Defaults to
the identity transform if not specified.

## Discussion

This method calculates starting and ending points using the radius and angles
you specify, uses a sequence of cubic Bézier curves to approximate a segment
of a circle between those points, and then appends those curves to the path.

The `clockwise` parameter determines the direction in which the arc is
created; the actual direction of the final path is dependent on the
`transform` parameter and the current transform of a context where the path is
drawn. However, because SwiftUI by default uses a vertically-flipped
coordinate system (with the origin in the top-left of the view), specifying a
clockwise arc results in a counterclockwise arc after the transformation is
applied.

If the path ends with an unclosed subpath, this method adds a line connecting
the current point to the starting point of the arc. If there is no unclosed
subpath, this method creates a new subpath whose starting point is the
starting point of the arc. The ending point of the arc becomes the new current
point of the path.

## See Also

### Drawing a path

`func move(to: CGPoint)`

Begins a new subpath at the specified point.

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

Instance Method

# addArc(tangent1End:tangent2End:radius:transform:)

Adds an arc of a circle to the path, specified with a radius and two tangent
lines.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    mutating func addArc(
        tangent1End: CGPoint,
        tangent2End: CGPoint,
        radius: CGFloat,
        transform: CGAffineTransform = .identity
    )

##  Parameters

`tangent1End`

    

The end point, in user space coordinates, for the first tangent line to be
used in constructing the arc. (The start point for this tangent line is the
path’s current point.)

`tangent2End`

    

The end point, in user space coordinates, for the second tangent line to be
used in constructing the arc. (The start point for this tangent line is the
tangent1End point.)

`radius`

    

The radius of the arc, in user space coordinates.

`transform`

    

An affine transform to apply to the arc before adding to the path. Defaults to
the identity transform if not specified.

## Discussion

This method calculates two tangent lines—the first from the current point to
the tangent1End point, and the second from the `tangent1End` point to the
`tangent2End` point—then calculates the start and end points for a circular
arc of the specified radius such that the arc is tangent to both lines.
Finally, this method approximates that arc with a sequence of cubic Bézier
curves and appends those curves to the path.

If the starting point of the arc (that is, the point where a circle of the
specified radius must meet the first tangent line in order to also be tangent
to the second line) is not the current point, this method appends a straight
line segment from the current point to the starting point of the arc.

The ending point of the arc (that is, the point where a circle of the
specified radius must meet the second tangent line in order to also be tangent
to the first line) becomes the new current point of the path.

## See Also

### Drawing a path

`func move(to: CGPoint)`

Begins a new subpath at the specified point.

`func addArc(center: CGPoint, radius: CGFloat, startAngle: Angle, endAngle:
Angle, clockwise: Bool, transform: CGAffineTransform)`

Adds an arc of a circle to the path, specified with a radius and angles.

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

Instance Method

# addCurve(to:control1:control2:)

Adds a cubic Bézier curve to the path, with the specified end point and
control points.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    mutating func addCurve(
        to end: CGPoint,
        control1: CGPoint,
        control2: CGPoint
    )

##  Parameters

`control1`

    

The first control point of the curve, in user space coordinates.

`control2`

    

The second control point of the curve, in user space coordinates.

## Discussion

This method constructs a curve starting from the path’s current point and
ending at the specified end point, with curvature defined by the two control
points. After this method appends that curve to the current path, the end
point of the curve becomes the path’s current point.

## See Also

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

Instance Method

# addEllipse(in:transform:)

Adds an ellipse that fits inside the specified rectangle to the path.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    mutating func addEllipse(
        in rect: CGRect,
        transform: CGAffineTransform = .identity
    )

## Discussion

The ellipse is approximated by a sequence of Bézier curves. Its center is the
midpoint of the rectangle defined by the `rect` parameter. If the rectangle is
square, then the ellipse is circular with a radius equal to one-half the width
(or height) of the rectangle. If the `rect` parameter specifies a rectangular
shape, then the major and minor axes of the ellipse are defined by the width
and height of the rectangle.

The ellipse forms a complete subpath of the path— that is, the ellipse drawing
starts with a move-to operation and ends with a close-subpath operation, with
all moves oriented in the clockwise direction.

  * Parameter:

    * rect: A rectangle that defines the area for the ellipse to fit in.

    * transform: An affine transform to apply to the ellipse before adding to the path. Defaults to the identity transform if not specified.

## See Also

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

Instance Method

# addLine(to:)

Appends a straight line segment from the current point to the specified point.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    mutating func addLine(to end: CGPoint)

##  Parameters

`end`

    

The location, in user space coordinates, for the end of the new line segment.

## Discussion

After adding the line segment, the current point is set to the endpoint of the
line segment.

## See Also

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

Instance Method

# addLines(_:)

Adds a sequence of connected straight-line segments to the path.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    mutating func addLines(_ lines: [CGPoint])

## Discussion

Calling this convenience method is equivalent to applying the transform to all
points in the array, then calling the `move(to:)` method with the first value
in the `points` array, then calling the `addLine(to:)` method for each
subsequent point until the array is exhausted. After calling this method, the
path’s current point is the last point in the array.

  * Parameter:

    * lines: An array of values that specify the start and end points of the line segments to draw. Each point in the array specifies a position in user space. The first point in the array specifies the initial starting point.

    * transform: An affine transform to apply to the points before adding to the path. Defaults to the identity transform if not specified.

## See Also

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

Instance Method

# addPath(_:transform:)

Appends another path value to this path.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    mutating func addPath(
        _ path: Path,
        transform: CGAffineTransform = .identity
    )

##  Parameters

`path`

    

The path to add.

`transform`

    

An affine transform to apply to the path parameter before adding to this path.
Defaults to the identity transform if not specified.

## Discussion

If the `path` parameter is a non-empty empty path, its elements are appended
in order to this path. Afterward, the start point and current point of this
path are those of the last subpath in the `path` parameter.

## See Also

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

Instance Method

# addQuadCurve(to:control:)

Adds a quadratic Bézier curve to the path, with the specified end point and
control point.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    mutating func addQuadCurve(
        to end: CGPoint,
        control: CGPoint
    )

##  Parameters

`control`

    

The control point of the curve, in user space coordinates.

## Discussion

This method constructs a curve starting from the path’s current point and
ending at the specified end point, with curvature defined by the control
point. After this method appends that curve to the current path, the end point
of the curve becomes the path’s current point.

## See Also

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

Instance Method

# addRect(_:transform:)

Adds a rectangular subpath to the path.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    mutating func addRect(
        _ rect: CGRect,
        transform: CGAffineTransform = .identity
    )

##  Parameters

`rect`

    

A rectangle, specified in user space coordinates.

`transform`

    

An affine transform to apply to the rectangle before adding to the path.
Defaults to the identity transform if not specified.

## Discussion

This is a convenience function that adds a rectangle to a path, starting by
moving to the bottom-left corner and then adding lines counter-clockwise to
create a rectangle, closing the subpath.

## See Also

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

Instance Method

# addRects(_:transform:)

Adds a set of rectangular subpaths to the path.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    mutating func addRects(
        _ rects: [CGRect],
        transform: CGAffineTransform = .identity
    )

## Discussion

Calling this convenience method is equivalent to repeatedly calling the
`addRect(_:transform:)` method for each rectangle in the array.

  * Parameter:

    * rects: An array of rectangles, specified in user space coordinates.

    * transform: An affine transform to apply to the ellipse before adding to the path. Defaults to the identity transform if not specified.

## See Also

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

`func addRelativeArc(center: CGPoint, radius: CGFloat, startAngle: Angle,
delta: Angle, transform: CGAffineTransform)`

Adds an arc of a circle to the path, specified with a radius and a difference
in angle.

`func addRoundedRect(in: CGRect, cornerSize: CGSize, style:
RoundedCornerStyle, transform: CGAffineTransform)`

Adds a rounded rectangle to the path.

`func closeSubpath()`

Closes and completes the current subpath.

Instance Method

# addRelativeArc(center:radius:startAngle:delta:transform:)

Adds an arc of a circle to the path, specified with a radius and a difference
in angle.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    mutating func addRelativeArc(
        center: CGPoint,
        radius: CGFloat,
        startAngle: Angle,
        delta: Angle,
        transform: CGAffineTransform = .identity
    )

##  Parameters

`center`

    

The center of the arc, in user space coordinates.

`radius`

    

The radius of the arc, in user space coordinates.

`startAngle`

    

The angle to the starting point of the arc, measured from the positive x-axis.

`delta`

    

The difference between the starting angle and ending angle of the arc. A
positive value creates a counter- clockwise arc (in user space coordinates),
and vice versa.

`transform`

    

An affine transform to apply to the arc before adding to the path. Defaults to
the identity transform if not specified. /

## Discussion

This method calculates starting and ending points using the radius and angles
you specify, uses a sequence of cubic Bézier curves to approximate a segment
of a circle between those points, and then appends those curves to the path.

The `delta` parameter determines both the length of the arc the direction in
which the arc is created; the actual direction of the final path is dependent
on the `transform` parameter and the current transform of a context where the
path is drawn. However, because SwiftUI by default uses a vertically-flipped
coordinate system (with the origin in the top-left of the view), specifying a
clockwise arc results in a counterclockwise arc after the transformation is
applied.

If the path ends with an unclosed subpath, this method adds a line connecting
the current point to the starting point of the arc. If there is no unclosed
subpath, this method creates a new subpath whose starting point is the
starting point of the arc. The ending point of the arc becomes the new current
point of the path.

## See Also

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

`func addRoundedRect(in: CGRect, cornerSize: CGSize, style:
RoundedCornerStyle, transform: CGAffineTransform)`

Adds a rounded rectangle to the path.

`func closeSubpath()`

Closes and completes the current subpath.

Instance Method

# addRoundedRect(in:cornerSize:style:transform:)

Adds a rounded rectangle to the path.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    mutating func addRoundedRect(
        in rect: CGRect,
        cornerSize: CGSize,
        style: RoundedCornerStyle = .continuous,
        transform: CGAffineTransform = .identity
    )

##  Parameters

`rect`

    

A rectangle, specified in user space coordinates.

`cornerSize`

    

The size of the corners, specified in user space coordinates.

`style`

    

The corner style. Defaults to the `continous` style if not specified.

`transform`

    

An affine transform to apply to the rectangle before adding to the path.
Defaults to the identity transform if not specified.

## Discussion

This is a convenience function that adds a rounded rectangle to a path,
starting by moving to the center of the right edge and then adding lines and
curves counter-clockwise to create a rounded rectangle, closing the subpath.

## See Also

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

`func closeSubpath()`

Closes and completes the current subpath.

Instance Method

# closeSubpath()

Closes and completes the current subpath.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    mutating func closeSubpath()

## Discussion

Appends a line from the current point to the starting point of the current
subpath and ends the subpath.

After closing the subpath, your application can begin a new subpath without
first calling `move(to:)`. In this case, a new subpath is implicitly created
with a starting and current point equal to the previous subpath’s starting
point.

## See Also

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

Instance Method

# applying(_:)

Returns a path constructed by applying the transform to all points of the
path.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func applying(_ transform: CGAffineTransform) -> Path

##  Parameters

`transform`

    

An affine transform to apply to the path.

## Return Value

a new copy of the path with the transform applied to all points.

## See Also

### Transforming the path

`func offsetBy(dx: CGFloat, dy: CGFloat) -> Path`

Returns a path constructed by translating all its points.

`func trimmedPath(from: CGFloat, to: CGFloat) -> Path`

Returns a partial copy of the path.

Instance Method

# offsetBy(dx:dy:)

Returns a path constructed by translating all its points.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func offsetBy(
        dx: CGFloat,
        dy: CGFloat
    ) -> Path

##  Parameters

`dx`

    

The offset to apply in the horizontal axis.

`dy`

    

The offset to apply in the vertical axis.

## Return Value

a new copy of the path with the offset applied to all points.

## See Also

### Transforming the path

`func applying(CGAffineTransform) -> Path`

Returns a path constructed by applying the transform to all points of the
path.

`func trimmedPath(from: CGFloat, to: CGFloat) -> Path`

Returns a partial copy of the path.

Instance Method

# trimmedPath(from:to:)

Returns a partial copy of the path.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func trimmedPath(
        from: CGFloat,
        to: CGFloat
    ) -> Path

## Discussion

The returned path contains the region between `from` and `to`, both of which
must be fractions between zero and one defining points linearly-interpolated
along the path.

## See Also

### Transforming the path

`func applying(CGAffineTransform) -> Path`

Returns a path constructed by applying the transform to all points of the
path.

`func offsetBy(dx: CGFloat, dy: CGFloat) -> Path`

Returns a path constructed by translating all its points.

Instance Method

# addRoundedRect(in:cornerSize:style:transform:)

Adds a rounded rectangle to the path.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    mutating func addRoundedRect(
        in rect: CGRect,
        cornerSize: CGSize,
        style: RoundedCornerStyle = .continuous,
        transform: CGAffineTransform = .identity
    )

##  Parameters

`rect`

    

A rectangle, specified in user space coordinates.

`cornerSize`

    

The size of the corners, specified in user space coordinates.

`style`

    

The corner style. Defaults to the `continous` style if not specified.

`transform`

    

An affine transform to apply to the rectangle before adding to the path.
Defaults to the identity transform if not specified.

## Discussion

This is a convenience function that adds a rounded rectangle to a path,
starting by moving to the center of the right edge and then adding lines and
curves counter-clockwise to create a rounded rectangle, closing the subpath.

## See Also

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

`func closeSubpath()`

Closes and completes the current subpath.

Instance Method

# intersection(_:eoFill:)

Returns a new path with filled regions common to both paths.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func intersection(
        _ other: Path,
        eoFill: Bool = false
    ) -> Path

##  Parameters

`other`

    

The path to intersect.

`eoFill`

    

Whether to use the even-odd rule for determining which areas to treat as the
interior of the paths (if true), or the non-zero rule (if false).

## Return Value

A new path.

## Discussion

The filled region of the resulting path is the overlapping area of the filled
region of both paths. This can be used to clip the fill of a path to a mask.

Any unclosed subpaths in either path are assumed to be closed. The result of
filling this path using either even-odd or non-zero fill rules is identical.

## See Also

### Performing operations on the path

`func addRoundedRect(in: CGRect, cornerSize: CGSize, style:
RoundedCornerStyle, transform: CGAffineTransform)`

Adds a rounded rectangle to the path.

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

Instance Method

# lineIntersection(_:eoFill:)

Returns a new path with a line from this path that overlaps the filled regions
of the given path.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func lineIntersection(
        _ other: Path,
        eoFill: Bool = false
    ) -> Path

##  Parameters

`other`

    

The path to intersect.

`eoFill`

    

Whether to use the even-odd rule for determining which areas to treat as the
interior of the paths (if true), or the non-zero rule (if false).

## Return Value

A new path.

## Discussion

The line of the resulting path is the line of this path that overlaps the
filled region of `other`.

Intersected subpaths that are clipped create open subpaths. Closed subpaths
that do not intersect `other` remain closed.

## See Also

### Performing operations on the path

`func addRoundedRect(in: CGRect, cornerSize: CGSize, style:
RoundedCornerStyle, transform: CGAffineTransform)`

Adds a rounded rectangle to the path.

`func intersection(Path, eoFill: Bool) -> Path`

Returns a new path with filled regions common to both paths.

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

Instance Method

# lineSubtraction(_:eoFill:)

Returns a new path with a line from this path that does not overlap the filled
region of the given path.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func lineSubtraction(
        _ other: Path,
        eoFill: Bool = false
    ) -> Path

##  Parameters

`other`

    

The path to subtract.

`eoFill`

    

Whether to use the even-odd rule for determining which areas to treat as the
interior of the paths (if true), or the non-zero rule (if false).

## Return Value

A new path.

## Discussion

The line of the resulting path is the line of this path that does not overlap
the filled region of `other`.

Intersected subpaths that are clipped create open subpaths. Closed subpaths
that do not intersect `other` remain closed.

## See Also

### Performing operations on the path

`func addRoundedRect(in: CGRect, cornerSize: CGSize, style:
RoundedCornerStyle, transform: CGAffineTransform)`

Adds a rounded rectangle to the path.

`func intersection(Path, eoFill: Bool) -> Path`

Returns a new path with filled regions common to both paths.

`func lineIntersection(Path, eoFill: Bool) -> Path`

Returns a new path with a line from this path that overlaps the filled regions
of the given path.

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

Instance Method

# normalized(eoFill:)

Returns a new weakly-simple copy of this path.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func normalized(eoFill: Bool = true) -> Path

##  Parameters

`eoFill`

    

Whether to use the even-odd rule for determining which areas to treat as the
interior of the paths (if true), or the non-zero rule (if false).

## Return Value

A new path.

## Discussion

The returned path is a weakly-simple path, has no self-intersections, and has
a normalized orientation. The result of filling this path using either even-
odd or non-zero fill rules is identical.

## See Also

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

`func subtracting(Path, eoFill: Bool) -> Path`

Returns a new path with filled regions from this path that are not in the
given path.

`func symmetricDifference(Path, eoFill: Bool) -> Path`

Returns a new path with filled regions either from this path or the given
path, but not in both.

`func union(Path, eoFill: Bool) -> Path`

Returns a new path with filled regions in either this path or the given path.

Instance Method

# subtracting(_:eoFill:)

Returns a new path with filled regions from this path that are not in the
given path.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func subtracting(
        _ other: Path,
        eoFill: Bool = false
    ) -> Path

##  Parameters

`other`

    

The path to subtract.

`eoFill`

    

Whether to use the even-odd rule for determining which areas to treat as the
interior of the paths (if true), or the non-zero rule (if false).

## Return Value

A new path.

## Discussion

The filled region of the resulting path is the filled region of this path with
the filled region `other` removed from it.

Any unclosed subpaths in either path are assumed to be closed. The result of
filling this path using either even-odd or non-zero fill rules is identical.

## See Also

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

`func symmetricDifference(Path, eoFill: Bool) -> Path`

Returns a new path with filled regions either from this path or the given
path, but not in both.

`func union(Path, eoFill: Bool) -> Path`

Returns a new path with filled regions in either this path or the given path.

Instance Method

# symmetricDifference(_:eoFill:)

Returns a new path with filled regions either from this path or the given
path, but not in both.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func symmetricDifference(
        _ other: Path,
        eoFill: Bool = false
    ) -> Path

##  Parameters

`other`

    

The path to difference.

`eoFill`

    

Whether to use the even-odd rule for determining which areas to treat as the
interior of the paths (if true), or the non-zero rule (if false).

## Return Value

A new path.

## Discussion

The filled region of the resulting path is the filled region contained in
either this path or `other`, but not both.

Any unclosed subpaths in either path are assumed to be closed. The result of
filling this path using either even-odd or non-zero fill rules is identical.

## See Also

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

`func union(Path, eoFill: Bool) -> Path`

Returns a new path with filled regions in either this path or the given path.

Instance Method

# union(_:eoFill:)

Returns a new path with filled regions in either this path or the given path.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func union(
        _ other: Path,
        eoFill: Bool = false
    ) -> Path

##  Parameters

`other`

    

The path to union.

`eoFill`

    

Whether to use the even-odd rule for determining which areas to treat as the
interior of the paths (if true), or the non-zero rule (if false).

## Return Value

A new path.

## Discussion

The filled region of resulting path is the combination of the filled region of
both paths added together.

Any unclosed subpaths in either path are assumed to be closed. The result of
filling this path using either even-odd or non-zero fill rules is identical.

## See Also

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

Instance Method

# forEach(_:)

Calls `body` with each element in the path.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func forEach(_ body: (Path.Element) -> Void)

## See Also

### Operating over path elements

`enum Element`

An element of a path.

Enumeration

# Path.Element

An element of a path.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    enum Element

## Topics

### Getting path elements

`case closeSubpath`

A line from the start point of the current subpath (if any) to the current
point, which terminates the subpath.

`case curve(to: CGPoint, control1: CGPoint, control2: CGPoint)`

A cubic Bézier curve from the previous current point to the given end-point,
using the two control points to define the curve.

`case line(to: CGPoint)`

A line from the previous current point to the given point, which becomes the
new current point.

`case move(to: CGPoint)`

A path element that terminates the current subpath (without closing it) and
defines a new current point.

`case quadCurve(to: CGPoint, control: CGPoint)`

A quadratic Bézier curve from the previous current point to the given end-
point, using the single control point to define the curve.

## Relationships

### Conforms To

  * `Equatable`
  * `Sendable`

## See Also

### Operating over path elements

`func forEach((Path.Element) -> Void)`

Calls `body` with each element in the path.

Instance Method

# strokedPath(_:)

Returns a stroked copy of the path using `style` to define how the stroked
outline is created.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func strokedPath(_ style: StrokeStyle) -> Path

Instance Method

# addRoundedRect(in:cornerRadii:style:transform:)

Adds a rounded rectangle with uneven corners to the path.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    mutating func addRoundedRect(
        in rect: CGRect,
        cornerRadii: RectangleCornerRadii,
        style: RoundedCornerStyle = .continuous,
        transform: CGAffineTransform = .identity
    )

##  Parameters

`rect`

    

A rectangle, specified in user space coordinates.

`cornerRadii`

    

The radius of each corner of the rectangle, specified in user space
coordinates.

`style`

    

The corner style. Defaults to the `continous` style if not specified.

`transform`

    

An affine transform to apply to the rectangle before adding to the path.
Defaults to the identity transform if not specified.

## Discussion

This is a convenience function that adds a rounded rectangle to a path,
starting by moving to the center of the right edge and then adding lines and
curves counter-clockwise to create a rounded rectangle, closing the subpath.

