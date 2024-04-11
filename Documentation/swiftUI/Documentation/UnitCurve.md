Type Property

# linear

A linear curve.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static let linear: UnitCurve

## Discussion

As the linear curve is a straight line from (0, 0) to (1, 1), the output
progress is always equal to the input progress, and the velocity is always
equal to 1.0.

Type Property

# easeIn

A bezier curve that starts out slowly, then speeds up as it finishes.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static let easeIn: UnitCurve

## Discussion

The start and end control points are located at (x: 0.42, y: 0) and (x: 1, y:
1).

## See Also

### Getting easing curves

`static let easeOut: UnitCurve`

A bezier curve that starts out quickly, then slows down as it approaches the
end.

`static let easeInOut: UnitCurve`

A bezier curve that starts out slowly, speeds up over the middle, then slows
down again as it approaches the end.

`static let circularEaseIn: UnitCurve`

A curve that starts out slowly, then speeds up as it finishes.

`static let circularEaseOut: UnitCurve`

A circular curve that starts out quickly, then slows down as it approaches the
end.

`static let circularEaseInOut: UnitCurve`

A circular curve that starts out slowly, speeds up over the middle, then slows
down again as it approaches the end.

Type Property

# easeOut

A bezier curve that starts out quickly, then slows down as it approaches the
end.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static let easeOut: UnitCurve

## Discussion

The start and end control points are located at (x: 0, y: 0) and (x: 0.58, y:
1).

## See Also

### Getting easing curves

`static let easeIn: UnitCurve`

A bezier curve that starts out slowly, then speeds up as it finishes.

`static let easeInOut: UnitCurve`

A bezier curve that starts out slowly, speeds up over the middle, then slows
down again as it approaches the end.

`static let circularEaseIn: UnitCurve`

A curve that starts out slowly, then speeds up as it finishes.

`static let circularEaseOut: UnitCurve`

A circular curve that starts out quickly, then slows down as it approaches the
end.

`static let circularEaseInOut: UnitCurve`

A circular curve that starts out slowly, speeds up over the middle, then slows
down again as it approaches the end.

Type Property

# easeInOut

A bezier curve that starts out slowly, speeds up over the middle, then slows
down again as it approaches the end.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static let easeInOut: UnitCurve

## Discussion

The start and end control points are located at (x: 0.42, y: 0) and (x: 0.58,
y: 1).

## See Also

### Getting easing curves

`static let easeIn: UnitCurve`

A bezier curve that starts out slowly, then speeds up as it finishes.

`static let easeOut: UnitCurve`

A bezier curve that starts out quickly, then slows down as it approaches the
end.

`static let circularEaseIn: UnitCurve`

A curve that starts out slowly, then speeds up as it finishes.

`static let circularEaseOut: UnitCurve`

A circular curve that starts out quickly, then slows down as it approaches the
end.

`static let circularEaseInOut: UnitCurve`

A circular curve that starts out slowly, speeds up over the middle, then slows
down again as it approaches the end.

Type Property

# circularEaseIn

A curve that starts out slowly, then speeds up as it finishes.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static let circularEaseIn: UnitCurve

## Discussion

The shape of the curve is equal to the fourth (bottom right) quadrant of a
unit circle.

## See Also

### Getting easing curves

`static let easeIn: UnitCurve`

A bezier curve that starts out slowly, then speeds up as it finishes.

`static let easeOut: UnitCurve`

A bezier curve that starts out quickly, then slows down as it approaches the
end.

`static let easeInOut: UnitCurve`

A bezier curve that starts out slowly, speeds up over the middle, then slows
down again as it approaches the end.

`static let circularEaseOut: UnitCurve`

A circular curve that starts out quickly, then slows down as it approaches the
end.

`static let circularEaseInOut: UnitCurve`

A circular curve that starts out slowly, speeds up over the middle, then slows
down again as it approaches the end.

Type Property

# circularEaseOut

A circular curve that starts out quickly, then slows down as it approaches the
end.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static let circularEaseOut: UnitCurve

## Discussion

The shape of the curve is equal to the second (top left) quadrant of a unit
circle.

## See Also

### Getting easing curves

`static let easeIn: UnitCurve`

A bezier curve that starts out slowly, then speeds up as it finishes.

`static let easeOut: UnitCurve`

A bezier curve that starts out quickly, then slows down as it approaches the
end.

`static let easeInOut: UnitCurve`

A bezier curve that starts out slowly, speeds up over the middle, then slows
down again as it approaches the end.

`static let circularEaseIn: UnitCurve`

A curve that starts out slowly, then speeds up as it finishes.

`static let circularEaseInOut: UnitCurve`

A circular curve that starts out slowly, speeds up over the middle, then slows
down again as it approaches the end.

Type Property

# circularEaseInOut

A circular curve that starts out slowly, speeds up over the middle, then slows
down again as it approaches the end.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static let circularEaseInOut: UnitCurve

## Discussion

The shape of the curve is defined by a piecewise combination of
`circularEaseIn` and `circularEaseOut`.

## See Also

### Getting easing curves

`static let easeIn: UnitCurve`

A bezier curve that starts out slowly, then speeds up as it finishes.

`static let easeOut: UnitCurve`

A bezier curve that starts out quickly, then slows down as it approaches the
end.

`static let easeInOut: UnitCurve`

A bezier curve that starts out slowly, speeds up over the middle, then slows
down again as it approaches the end.

`static let circularEaseIn: UnitCurve`

A curve that starts out slowly, then speeds up as it finishes.

`static let circularEaseOut: UnitCurve`

A circular curve that starts out quickly, then slows down as it approaches the
end.

Type Method

# bezier(startControlPoint:endControlPoint:)

Creates a new curve using bezier control points.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static func bezier(
        startControlPoint: UnitPoint,
        endControlPoint: UnitPoint
    ) -> UnitCurve

##  Parameters

`startControlPoint`

    

The cubic Bézier control point associated with the curve’s start point at (0,
0). The tangent vector from the start point to its control point defines the
initial velocity of the timing function.

`endControlPoint`

    

The cubic Bézier control point associated with the curve’s end point at (1,
1). The tangent vector from the end point to its control point defines the
final velocity of the timing function.

## Discussion

The x components of the control points are clamped to the range [0,1] when the
curve is evaluated.

Instance Property

# inverse

Returns a copy of the curve with its x and y components swapped.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var inverse: UnitCurve { get }

## Discussion

The inverse can be used to solve a curve in reverse: given a known output (y)
value, the corresponding input (x) value can be found by using `inverse`:

Instance Method

# value(at:)

Returns the output value (y component) of the curve at the given time.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func value(at progress: Double) -> Double

##  Parameters

`time`

    

The input progress (x component). The provided value is clamped to the range
[0,1].

## Return Value

The output value (y component) of the curve at the given progress.

## See Also

### Getting curve characteristics

`func velocity(at: Double) -> Double`

Returns the rate of change (first derivative) of the output value of the curve
at the given time.

Instance Method

# velocity(at:)

Returns the rate of change (first derivative) of the output value of the curve
at the given time.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func velocity(at progress: Double) -> Double

##  Parameters

`progress`

    

The input progress (x component). The provided value is clamped to the range
[0,1].

## Return Value

The velocity of the output value (y component) of the curve at the given time.

## See Also

### Getting curve characteristics

`func value(at: Double) -> Double`

Returns the output value (y component) of the curve at the given time.

Type Property

# easeInEaseOut

A bezier curve that starts out slowly, speeds up over the middle, then slows
down again as it approaches the end.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static let easeInEaseOut: UnitCurve

Deprecated

Use `easeInOut` instead.

