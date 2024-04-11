Instance Method

# strokeBorder(_:lineWidth:antialiased:)

Returns a view that is the result of filling the `lineWidth`-sized border (aka
inner stroke) of `self` with `content`. This is equivalent to insetting `self`
by `lineWidth / 2` and stroking the resulting shape with `lineWidth` as the
line-width.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func strokeBorder<S>(
        _ content: S = .foreground,
        lineWidth: CGFloat = 1,
        antialiased: Bool = true
    ) -> StrokeBorderShapeView<Self, S, EmptyView> where S : ShapeStyle

## See Also

### Setting the stroke border characteristics

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

Instance Method

# strokeBorder(_:lineWidth:antialiased:)

Returns a view that is the result of filling the `lineWidth`-sized border (aka
inner stroke) of `self` with `content`. This is equivalent to insetting `self`
by `lineWidth / 2` and stroking the resulting shape with `lineWidth` as the
line-width.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func strokeBorder<S>(
        _ content: S,
        lineWidth: CGFloat = 1,
        antialiased: Bool = true
    ) -> some View where S : ShapeStyle
    

## See Also

### Setting the stroke border characteristics

`func strokeBorder<S>(S, lineWidth: CGFloat, antialiased: Bool) ->
StrokeBorderShapeView<Self, S, EmptyView>`

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

Instance Method

# strokeBorder(lineWidth:antialiased:)

Returns a view that is the result of filling the `lineWidth`-sized border (aka
inner stroke) of `self` with the foreground color. This is equivalent to
insetting `self` by `lineWidth / 2` and stroking the resulting shape with
`lineWidth` as the line-width.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func strokeBorder(
        lineWidth: CGFloat = 1,
        antialiased: Bool = true
    ) -> some View
    

## See Also

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

Instance Method

# strokeBorder(_:style:antialiased:)

Returns a view that is the result of insetting `self` by `style.lineWidth /
2`, stroking the resulting shape with `style`, and then filling with
`content`.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func strokeBorder<S>(
        _ content: S = .foreground,
        style: StrokeStyle,
        antialiased: Bool = true
    ) -> StrokeBorderShapeView<Self, S, EmptyView> where S : ShapeStyle

## See Also

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

`func strokeBorder<S>(S, style: StrokeStyle, antialiased: Bool) -> some View`

Returns a view that is the result of insetting `self` by `style.lineWidth /
2`, stroking the resulting shape with `style`, and then filling with
`content`.

`func strokeBorder(style: StrokeStyle, antialiased: Bool) -> some View`

Returns a view that is the result of insetting `self` by `style.lineWidth /
2`, stroking the resulting shape with `style`, and then filling with the
foreground color.

Instance Method

# strokeBorder(_:style:antialiased:)

Returns a view that is the result of insetting `self` by `style.lineWidth /
2`, stroking the resulting shape with `style`, and then filling with
`content`.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func strokeBorder<S>(
        _ content: S,
        style: StrokeStyle,
        antialiased: Bool = true
    ) -> some View where S : ShapeStyle
    

## See Also

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

`func strokeBorder(style: StrokeStyle, antialiased: Bool) -> some View`

Returns a view that is the result of insetting `self` by `style.lineWidth /
2`, stroking the resulting shape with `style`, and then filling with the
foreground color.

Instance Method

# strokeBorder(style:antialiased:)

Returns a view that is the result of insetting `self` by `style.lineWidth /
2`, stroking the resulting shape with `style`, and then filling with the
foreground color.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func strokeBorder(
        style: StrokeStyle,
        antialiased: Bool = true
    ) -> some View
    

## See Also

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

Instance Method

# inset(by:)

Returns `self` inset by `amount`.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func inset(by amount: CGFloat) -> Self.InsetShape

**Required**

## See Also

### Setting the inset

`associatedtype InsetShape : InsettableShape`

The type of the inset shape.

**Required**

Associated Type

# InsetShape

The type of the inset shape.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    associatedtype InsetShape : InsettableShape

**Required**

## See Also

### Setting the inset

`func inset(by: CGFloat) -> Self.InsetShape`

Returns `self` inset by `amount`.

**Required**

