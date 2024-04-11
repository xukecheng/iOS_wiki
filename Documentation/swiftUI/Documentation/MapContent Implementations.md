Instance Method

# annotationSubtitles(_:)

Sets the visibility of subtitles for markers and annotations.

MapKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    func annotationSubtitles(_ visibility: Visibility) -> some MapContent
    

## Discussion

With the default .automatic visibility, subtitle is visible only when the
annotation is selected.

Instance Method

# annotationTitles(_:)

Sets the visibility of titles for markers and annotations.

MapKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    func annotationTitles(_ visibility: Visibility) -> some MapContent
    

## Discussion

With the default .automatic visibility, title is always visible.

Instance Method

# foregroundStyle(_:)

Specifies the shape style used to fill content in drawing map overlays.

MapKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    func foregroundStyle(_ content: some ShapeStyle) -> some MapContent
    

##  Parameters

`content`

    

The shape style to apply.

Instance Method

# mapOverlayLevel(level:)

Specifies the position of overlays relative to other map content.

MapKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    func mapOverlayLevel(level: MKOverlayLevel) -> some MapContent
    

Instance Method

# stroke(_:lineWidth:)

Applies the given shape style to drawn map overlays.

MapKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    func stroke(
        _ content: some ShapeStyle,
        lineWidth: CGFloat = 1
    ) -> some MapContent
    

##  Parameters

`content`

    

The shape style to apply.

`lineWidth`

    

The line width to draw the stroke with.

Instance Method

# stroke(_:style:)

Applies the given shape style to drawn map overlays.

MapKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    func stroke(
        _ content: some ShapeStyle,
        style: StrokeStyle
    ) -> some MapContent
    

##  Parameters

`content`

    

The shape style to apply.

`lineWidth`

    

The line width to draw the stroke with.

Instance Method

# stroke(lineWidth:)

Sets the line width used for drawing map overlays.

MapKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    func stroke(lineWidth: CGFloat = 1) -> some MapContent
    

##  Parameters

`lineWidth`

    

The line width to draw the stroke with.

Instance Method

# strokeStyle(style:)

Applies the given stroke style to drawn map overlays.

MapKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    func strokeStyle(style: StrokeStyle) -> some MapContent
    

##  Parameters

`style`

    

The stroke style to apply.

Instance Method

# tag(_:)

Sets the unique tag value of this piece of map content.

MapKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    func tag<V>(_ tag: V) -> some MapContent where V : Hashable
    

##  Parameters

`tag`

    

A `Hashable` value to use as the map content’s tag.

## Return Value

Map content with the specified tag set.

## Discussion

Use this modifier to differentiate between selectable content in the map. When
the map’s selection binding has the same value as the tag applied to a piece
of map content, that content is considered selected.

A `ForEach` automatically applies a default tag to each enumerated view using
the `id` parameter of the corresponding element. If the element’s `id`
parameter and the the map’s selection input have the same type, you can omit
the explicit tag modifier.

Instance Method

# tint(_:)

The tint shape style to apply to map content.

MapKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    func tint<S>(_ tint: S) -> some MapContent where S : ShapeStyle
    

##  Parameters

`tint`

    

The tint to apply.

## Discussion

The tint is always respected and should be used as a way to provide additional
meaning to map content.

Instance Method

# annotationSubtitles(_:)

Sets the visibility of subtitles for markers and annotations.

MapKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    func annotationSubtitles(_ visibility: Visibility) -> some MapContent
    

## Discussion

With the default .automatic visibility, subtitle is visible only when the
annotation is selected.

Instance Method

# annotationTitles(_:)

Sets the visibility of titles for markers and annotations.

MapKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    func annotationTitles(_ visibility: Visibility) -> some MapContent
    

## Discussion

With the default .automatic visibility, title is always visible.

Instance Method

# foregroundStyle(_:)

Specifies the shape style used to fill content in drawing map overlays.

MapKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    func foregroundStyle(_ content: some ShapeStyle) -> some MapContent
    

##  Parameters

`content`

    

The shape style to apply.

Instance Method

# mapOverlayLevel(level:)

Specifies the position of overlays relative to other map content.

MapKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    func mapOverlayLevel(level: MKOverlayLevel) -> some MapContent
    

Instance Method

# stroke(_:lineWidth:)

Applies the given shape style to drawn map overlays.

MapKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    func stroke(
        _ content: some ShapeStyle,
        lineWidth: CGFloat = 1
    ) -> some MapContent
    

##  Parameters

`content`

    

The shape style to apply.

`lineWidth`

    

The line width to draw the stroke with.

Instance Method

# stroke(_:style:)

Applies the given shape style to drawn map overlays.

MapKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    func stroke(
        _ content: some ShapeStyle,
        style: StrokeStyle
    ) -> some MapContent
    

##  Parameters

`content`

    

The shape style to apply.

`lineWidth`

    

The line width to draw the stroke with.

Instance Method

# stroke(lineWidth:)

Sets the line width used for drawing map overlays.

MapKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    func stroke(lineWidth: CGFloat = 1) -> some MapContent
    

##  Parameters

`lineWidth`

    

The line width to draw the stroke with.

Instance Method

# strokeStyle(style:)

Applies the given stroke style to drawn map overlays.

MapKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    func strokeStyle(style: StrokeStyle) -> some MapContent
    

##  Parameters

`style`

    

The stroke style to apply.

Instance Method

# tag(_:)

Sets the unique tag value of this piece of map content.

MapKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    func tag<V>(_ tag: V) -> some MapContent where V : Hashable
    

##  Parameters

`tag`

    

A `Hashable` value to use as the map content’s tag.

## Return Value

Map content with the specified tag set.

## Discussion

Use this modifier to differentiate between selectable content in the map. When
the map’s selection binding has the same value as the tag applied to a piece
of map content, that content is considered selected.

A `ForEach` automatically applies a default tag to each enumerated view using
the `id` parameter of the corresponding element. If the element’s `id`
parameter and the the map’s selection input have the same type, you can omit
the explicit tag modifier.

Instance Method

# tint(_:)

The tint shape style to apply to map content.

MapKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    func tint<S>(_ tint: S) -> some MapContent where S : ShapeStyle
    

##  Parameters

`tint`

    

The tint to apply.

## Discussion

The tint is always respected and should be used as a way to provide additional
meaning to map content.

Type Alias

# ForEach.Body

MapKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    typealias Body = Never

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `MapContent`.

Instance Method

# annotationSubtitles(_:)

Sets the visibility of subtitles for markers and annotations.

MapKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    func annotationSubtitles(_ visibility: Visibility) -> some MapContent
    

## Discussion

With the default .automatic visibility, subtitle is visible only when the
annotation is selected.

Instance Method

# annotationTitles(_:)

Sets the visibility of titles for markers and annotations.

MapKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    func annotationTitles(_ visibility: Visibility) -> some MapContent
    

## Discussion

With the default .automatic visibility, title is always visible.

Instance Method

# foregroundStyle(_:)

Specifies the shape style used to fill content in drawing map overlays.

MapKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    func foregroundStyle(_ content: some ShapeStyle) -> some MapContent
    

##  Parameters

`content`

    

The shape style to apply.

Instance Method

# mapOverlayLevel(level:)

Specifies the position of overlays relative to other map content.

MapKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    func mapOverlayLevel(level: MKOverlayLevel) -> some MapContent
    

Instance Method

# stroke(_:lineWidth:)

Applies the given shape style to drawn map overlays.

MapKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    func stroke(
        _ content: some ShapeStyle,
        lineWidth: CGFloat = 1
    ) -> some MapContent
    

##  Parameters

`content`

    

The shape style to apply.

`lineWidth`

    

The line width to draw the stroke with.

Instance Method

# stroke(_:style:)

Applies the given shape style to drawn map overlays.

MapKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    func stroke(
        _ content: some ShapeStyle,
        style: StrokeStyle
    ) -> some MapContent
    

##  Parameters

`content`

    

The shape style to apply.

`lineWidth`

    

The line width to draw the stroke with.

Instance Method

# stroke(lineWidth:)

Sets the line width used for drawing map overlays.

MapKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    func stroke(lineWidth: CGFloat = 1) -> some MapContent
    

##  Parameters

`lineWidth`

    

The line width to draw the stroke with.

Instance Method

# strokeStyle(style:)

Applies the given stroke style to drawn map overlays.

MapKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    func strokeStyle(style: StrokeStyle) -> some MapContent
    

##  Parameters

`style`

    

The stroke style to apply.

Instance Method

# tag(_:)

Sets the unique tag value of this piece of map content.

MapKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    func tag<V>(_ tag: V) -> some MapContent where V : Hashable
    

##  Parameters

`tag`

    

A `Hashable` value to use as the map content’s tag.

## Return Value

Map content with the specified tag set.

## Discussion

Use this modifier to differentiate between selectable content in the map. When
the map’s selection binding has the same value as the tag applied to a piece
of map content, that content is considered selected.

A `ForEach` automatically applies a default tag to each enumerated view using
the `id` parameter of the corresponding element. If the element’s `id`
parameter and the the map’s selection input have the same type, you can omit
the explicit tag modifier.

Instance Method

# tint(_:)

The tint shape style to apply to map content.

MapKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    func tint<S>(_ tint: S) -> some MapContent where S : ShapeStyle
    

##  Parameters

`tint`

    

The tint to apply.

## Discussion

The tint is always respected and should be used as a way to provide additional
meaning to map content.

