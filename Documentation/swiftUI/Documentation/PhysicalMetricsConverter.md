Instance Method

# convert(_:from:)

Converts a point, whose coordinates are in the specified unit, to a point
suitable for use in the environment this converter is associated with.

visionOS 1.0+

    
    
    func convert(
        _ point: CGPoint,
        from unit: UnitLength
    ) -> CGPoint

## Return Value

A value in points. Use this value only in the scene this converter was
associated with.

## See Also

### Converting from a unit length

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

Instance Method

# convert(_:from:)

Converts a `Rect3D`, whose coordinates are in the specified unit, to a
`Rect3D` with coordinates specified in points, suitable for use in the
environment this converter is associated with.

visionOS 1.0+

    
    
    func convert(
        _ rect: Rect3D,
        from unit: UnitLength
    ) -> Rect3D

## Return Value

A value in points. Use this value only in the scene this converter was
associated with.

## See Also

### Converting from a unit length

`func convert(CGPoint, from: UnitLength) -> CGPoint`

Converts a point, whose coordinates are in the specified unit, to a point
suitable for use in the environment this converter is associated with.

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

Instance Method

# convert(_:from:)

Converts a size, given in the specified unit, to a size in points suitable for
use in the environment this converter is associated with.

visionOS 1.0+

    
    
    func convert(
        _ size: Size3D,
        from unit: UnitLength
    ) -> Size3D

## Return Value

A value in points. Use this value only in the scene this converter was
associated with.

## See Also

### Converting from a unit length

`func convert(CGPoint, from: UnitLength) -> CGPoint`

Converts a point, whose coordinates are in the specified unit, to a point
suitable for use in the environment this converter is associated with.

`func convert(Rect3D, from: UnitLength) -> Rect3D`

Converts a `Rect3D`, whose coordinates are in the specified unit, to a
`Rect3D` with coordinates specified in points, suitable for use in the
environment this converter is associated with.

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

Instance Method

# convert(_:from:)

Converts a length in the specified unit to a length in points suitable for use
in the environment this converter is associated with.

visionOS 1.0+

    
    
    func convert(
        _ lengthValue: CGFloat,
        from unit: UnitLength
    ) -> CGFloat

## Return Value

A value in points. Use this value only in the scene this converter was
associated with.

## See Also

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

Instance Method

# convert(_:from:)

Converts a point, whose coordinates are in the specified unit, to a point
value suitable for use in the environment this converter is associated with.

visionOS 1.0+

    
    
    func convert(
        _ point: Point3D,
        from unit: UnitLength
    ) -> Point3D

## Return Value

A value in points. Use this value only in the scene this converter was
associated with.

## See Also

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

Instance Method

# convert(_:from:)

Converts a size, given in the specified unit, to a size in points suitable for
use in the environment this converter is associated with.

visionOS 1.0+

    
    
    func convert(
        _ size: CGSize,
        from unit: UnitLength
    ) -> CGSize

## Return Value

A value in points. Use this value only in the scene this converter was
associated with.

## See Also

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

`func convert<V>(V, from: UnitLength) -> V`

Converts a vector of physical length measurements, in the specified unit, to a
vector of values in points suitable for use in the environment this converter
is associated with.

`func convert(CGRect, from: UnitLength) -> CGRect`

Converts a rectangle, whose coordinates are in the specified unit, to a
rectangle with coordinates specified in points, suitable for use in the
environment this converter is associated with.

Instance Method

# convert(_:from:)

Converts a vector of physical length measurements, in the specified unit, to a
vector of values in points suitable for use in the environment this converter
is associated with.

visionOS 1.0+

    
    
    func convert<V>(
        _ lengthValues: V,
        from unit: UnitLength
    ) -> V where V : VectorArithmetic

## Return Value

A value in points. Use this value only in the scene this converter was
associated with.

## See Also

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

`func convert(CGRect, from: UnitLength) -> CGRect`

Converts a rectangle, whose coordinates are in the specified unit, to a
rectangle with coordinates specified in points, suitable for use in the
environment this converter is associated with.

Instance Method

# convert(_:from:)

Converts a rectangle, whose coordinates are in the specified unit, to a
rectangle with coordinates specified in points, suitable for use in the
environment this converter is associated with.

visionOS 1.0+

    
    
    func convert(
        _ rect: CGRect,
        from unit: UnitLength
    ) -> CGRect

## Return Value

A value in points. Use this value only in the scene this converter was
associated with.

## See Also

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

Instance Method

# convert(_:to:)

Converts a `Rect3D`’s coordinates to physical length measurements in the
specified unit.

visionOS 1.0+

    
    
    func convert(
        _ rect: Rect3D,
        to unit: UnitLength
    ) -> Rect3D

## Return Value

A `Rect3D` value with physical length measurements, in the given unit

## Discussion

The `Rect3D` is assumed to be in the coordinate system of the scene that this
converter is associated with. If the scene is scaled, the physical measurement
will take this scale into account.

## See Also

### Converting to a unit length

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

Instance Method

# convert(_:to:)

Converts a rectangle’s coordinates to physical length measurements in the
specified unit.

visionOS 1.0+

    
    
    func convert(
        _ rect: CGRect,
        to unit: UnitLength
    ) -> CGRect

## Return Value

A rectangle with physical length measurements, in the given unit

## Discussion

The rectangle is assumed to be in the coordinate system of the scene that this
converter is associated with. If the scene is scaled, the physical measurement
will take this scale into account.

## See Also

### Converting to a unit length

`func convert(Rect3D, to: UnitLength) -> Rect3D`

Converts a `Rect3D`’s coordinates to physical length measurements in the
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

Instance Method

# convert(_:to:)

Converts a point’s coordinates to physical length measurements in the
specified unit.

visionOS 1.0+

    
    
    func convert(
        _ point: CGPoint,
        to unit: UnitLength
    ) -> CGPoint

## Return Value

A point value with physical length measurements, in the given unit

## Discussion

The point is assumed to be in the coordinate system of the scene that this
converter is associated with. If the scene is scaled, the physical measurement
will take this scale into account.

## See Also

### Converting to a unit length

`func convert(Rect3D, to: UnitLength) -> Rect3D`

Converts a `Rect3D`’s coordinates to physical length measurements in the
specified unit.

`func convert(CGRect, to: UnitLength) -> CGRect`

Converts a rectangle’s coordinates to physical length measurements in the
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

Instance Method

# convert(_:to:)

Converts a vector of values in points to corresponding physical length
measurements in the specified unit.

visionOS 1.0+

    
    
    func convert<V>(
        _ pointValues: V,
        to unit: UnitLength
    ) -> V where V : VectorArithmetic

## Return Value

A vector of physical length measurements, each converted from the points value
in the input vector at the same position. converter was associated with.

## Discussion

The point values are assumed to be in the coordinate system of the scene that
this converter is associated with. If the scene was scaled by user action, the
physical measurement will take this scale into account.

## See Also

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

Instance Method

# convert(_:to:)

Converts a point’s coordinates to physical length measurements in the
specified unit.

visionOS 1.0+

    
    
    func convert(
        _ point: Point3D,
        to unit: UnitLength
    ) -> Point3D

## Return Value

A point value with physical length measurements, in the given unit

## Discussion

The point is assumed to be in the coordinate system of the scene that this
converter is associated with. If the scene is scaled, the physical measurement
will take this scale into account.

## See Also

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

`func convert(CGSize, to: UnitLength) -> CGSize`

Converts a size, specified in points, to physical length measurements in the
specified unit.

`func convert(Size3D, to: UnitLength) -> Size3D`

Converts a size, specified in points, to physical length measurements in the
specified unit.

`func convert(CGFloat, to: UnitLength) -> CGFloat`

Converts a length in points to a physical length measurement in the specified
unit.

Instance Method

# convert(_:to:)

Converts a size, specified in points, to physical length measurements in the
specified unit.

visionOS 1.0+

    
    
    func convert(
        _ size: CGSize,
        to unit: UnitLength
    ) -> CGSize

## Return Value

A size in the given unit

## Discussion

The size is assumed to be in the coordinate system of the scene that this
converter is associated with. If the scene is scaled, the physical measurement
will take this scale into account.

## See Also

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

`func convert(Size3D, to: UnitLength) -> Size3D`

Converts a size, specified in points, to physical length measurements in the
specified unit.

`func convert(CGFloat, to: UnitLength) -> CGFloat`

Converts a length in points to a physical length measurement in the specified
unit.

Instance Method

# convert(_:to:)

Converts a size, specified in points, to physical length measurements in the
specified unit.

visionOS 1.0+

    
    
    func convert(
        _ size: Size3D,
        to unit: UnitLength
    ) -> Size3D

## Return Value

A size in the given unit

## Discussion

The size is assumed to be in the coordinate system of the scene that this
converter is associated with. If the scene is scaled, the physical measurement
will take this scale into account.

## See Also

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

`func convert(CGFloat, to: UnitLength) -> CGFloat`

Converts a length in points to a physical length measurement in the specified
unit.

Instance Method

# convert(_:to:)

Converts a length in points to a physical length measurement in the specified
unit.

visionOS 1.0+

    
    
    func convert(
        _ pointsValue: CGFloat,
        to unit: UnitLength
    ) -> CGFloat

## Return Value

A physical length in the given unit

## Discussion

The length is assumed to be in the coordinate system of the scene that this
converter is associated with. If the scene is scaled, the physical measurement
will take this scale into account.

## See Also

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

