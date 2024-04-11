Initializer

# init(lineWidth:lineCap:lineJoin:miterLimit:dash:dashPhase:)

Creates a new stroke style from the given components.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        lineWidth: CGFloat = 1,
        lineCap: CGLineCap = .butt,
        lineJoin: CGLineJoin = .miter,
        miterLimit: CGFloat = 10,
        dash: [CGFloat] = [CGFloat](),
        dashPhase: CGFloat = 0
    )

##  Parameters

`lineWidth`

    

The width of the segment.

`lineCap`

    

The endpoint style of a segment.

`lineJoin`

    

The join type of a segment.

`miterLimit`

    

The threshold used to determine whether to use a bevel instead of a miter at a
join.

`dash`

    

The lengths of painted and unpainted segments used to make a dashed line.

`dashPhase`

    

How far into the dash pattern the line starts.

Instance Property

# lineWidth

The width of the stroked path.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var lineWidth: CGFloat

## See Also

### Setting stroke style properties

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

Instance Property

# lineCap

The endpoint style of a line.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var lineCap: CGLineCap

## See Also

### Setting stroke style properties

`var lineWidth: CGFloat`

The width of the stroked path.

`var lineJoin: CGLineJoin`

The join type of a line.

`var miterLimit: CGFloat`

A threshold used to determine whether to use a bevel instead of a miter at a
join.

`var dash: [CGFloat]`

The lengths of painted and unpainted segments used to make a dashed line.

`var dashPhase: CGFloat`

How far into the dash pattern the line starts.

Instance Property

# lineJoin

The join type of a line.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var lineJoin: CGLineJoin

## See Also

### Setting stroke style properties

`var lineWidth: CGFloat`

The width of the stroked path.

`var lineCap: CGLineCap`

The endpoint style of a line.

`var miterLimit: CGFloat`

A threshold used to determine whether to use a bevel instead of a miter at a
join.

`var dash: [CGFloat]`

The lengths of painted and unpainted segments used to make a dashed line.

`var dashPhase: CGFloat`

How far into the dash pattern the line starts.

Instance Property

# miterLimit

A threshold used to determine whether to use a bevel instead of a miter at a
join.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var miterLimit: CGFloat

## See Also

### Setting stroke style properties

`var lineWidth: CGFloat`

The width of the stroked path.

`var lineCap: CGLineCap`

The endpoint style of a line.

`var lineJoin: CGLineJoin`

The join type of a line.

`var dash: [CGFloat]`

The lengths of painted and unpainted segments used to make a dashed line.

`var dashPhase: CGFloat`

How far into the dash pattern the line starts.

Instance Property

# dash

The lengths of painted and unpainted segments used to make a dashed line.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var dash: [CGFloat]

## See Also

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

`var dashPhase: CGFloat`

How far into the dash pattern the line starts.

Instance Property

# dashPhase

How far into the dash pattern the line starts.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var dashPhase: CGFloat

## See Also

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

