Instance Property

# shape

The shape that this type draws and provides for other drawing operations.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var shape: Self.Content { get }

**Required**

## See Also

### Getting the shape

`associatedtype Content : Shape`

The type of shape this can provide.

**Required**

Associated Type

# Content

The type of shape this can provide.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    associatedtype Content : Shape

**Required**

## See Also

### Getting the shape

`var shape: Self.Content`

The shape that this type draws and provides for other drawing operations.

**Required**

Instance Method

# fill(_:style:)

Fills this shape with a color or gradient.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func fill<S>(
        _ content: S = .foreground,
        style: FillStyle = FillStyle()
    ) -> FillShapeView<Self.Content, S, Self> where S : ShapeStyle

##  Parameters

`content`

    

The color or gradient to use when filling this shape.

`style`

    

The style options that determine how the fill renders.

## Return Value

A shape filled with the color or gradient you supply.

## See Also

### Modify the shape

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

Instance Method

# stroke(_:style:antialiased:)

Traces the outline of this shape with a color or gradient.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func stroke<S>(
        _ content: S,
        style: StrokeStyle,
        antialiased: Bool = true
    ) -> StrokeShapeView<Self.Content, S, Self> where S : ShapeStyle

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

### Modify the shape

`func fill<S>(S, style: FillStyle) -> FillShapeView<Self.Content, S, Self>`

Fills this shape with a color or gradient.

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

Instance Method

# stroke(_:lineWidth:antialiased:)

Traces the outline of this shape with a color or gradient.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func stroke<S>(
        _ content: S,
        lineWidth: CGFloat = 1,
        antialiased: Bool = true
    ) -> StrokeShapeView<Self.Content, S, Self> where S : ShapeStyle

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

### Modify the shape

`func fill<S>(S, style: FillStyle) -> FillShapeView<Self.Content, S, Self>`

Fills this shape with a color or gradient.

`func stroke<S>(S, style: StrokeStyle, antialiased: Bool) ->
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

Instance Method

# strokeBorder(_:style:antialiased:)

Returns a view that’s the result of insetting this view by half of its style’s
line width.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func strokeBorder<S>(
        _ content: S = .foreground,
        style: StrokeStyle,
        antialiased: Bool = true
    ) -> StrokeBorderShapeView<Self.Content, S, Self> where S : ShapeStyle

Available when `Content` conforms to `InsettableShape`.

## Discussion

This method strokes the resulting shape with `style` and fills it with
`content`.

## See Also

### Modify the shape

`func fill<S>(S, style: FillStyle) -> FillShapeView<Self.Content, S, Self>`

Fills this shape with a color or gradient.

`func stroke<S>(S, style: StrokeStyle, antialiased: Bool) ->
StrokeShapeView<Self.Content, S, Self>`

Traces the outline of this shape with a color or gradient.

`func stroke<S>(S, lineWidth: CGFloat, antialiased: Bool) ->
StrokeShapeView<Self.Content, S, Self>`

Traces the outline of this shape with a color or gradient.

`func strokeBorder<S>(S, lineWidth: CGFloat, antialiased: Bool) ->
StrokeBorderShapeView<Self.Content, S, Self>`

Returns a view that’s the result of filling an inner stroke of this view with
the content you supply.

Available when `Content` conforms to `InsettableShape`.

Instance Method

# strokeBorder(_:lineWidth:antialiased:)

Returns a view that’s the result of filling an inner stroke of this view with
the content you supply.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func strokeBorder<S>(
        _ content: S = .foreground,
        lineWidth: CGFloat = 1,
        antialiased: Bool = true
    ) -> StrokeBorderShapeView<Self.Content, S, Self> where S : ShapeStyle

Available when `Content` conforms to `InsettableShape`.

## Discussion

This is equivalent to insetting `self` by `lineWidth / 2` and stroking the
resulting shape with `lineWidth` as the line-width.

## See Also

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

