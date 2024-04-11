Initializer

# init(content:modifier:)

A structure that the defines the content and modifier needed to produce a new
view or view modifier.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        content: Content,
        modifier: Modifier
    )

##  Parameters

`content`

    

The content that the modifier changes.

`modifier`

    

The modifier to apply to the content.

## Discussion

If `content` is a `View` and `modifier` is a `ViewModifier`, the result is a
`View`. If `content` and `modifier` are both view modifiers, then the result
is a new `ViewModifier` combining them.

## See Also

### Creating a modified content view

`var content: Content`

The content that the modifier transforms into a new view or new view modifier.

`var modifier: Modifier`

The view modifier.

Instance Property

# content

The content that the modifier transforms into a new view or new view modifier.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var content: Content

## See Also

### Creating a modified content view

`init(content: Content, modifier: Modifier)`

A structure that the defines the content and modifier needed to produce a new
view or view modifier.

`var modifier: Modifier`

The view modifier.

Instance Property

# modifier

The view modifier.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var modifier: Modifier

## See Also

### Creating a modified content view

`init(content: Content, modifier: Modifier)`

A structure that the defines the content and modifier needed to produce a new
view or view modifier.

`var content: Content`

The content that the modifier transforms into a new view or new view modifier.

Collection

API Collection

# DynamicMapContent Implementations

## Topics

### Instance Properties

`var data: Content.Data`

The collection of underlying data.

Available when `Content` conforms to `DynamicMapContent` and `Modifier`
conforms to `_MapContentModifier`.

### Type Aliases

`typealias Data`

The type of the underlying collection of data.

Available when `Content` conforms to `DynamicMapContent` and `Modifier`
conforms to `_MapContentModifier`.

Collection

API Collection

# MapContent Implementations

## Topics

### Instance Methods

`func annotationSubtitles(Visibility) -> some MapContent`

Sets the visibility of subtitles for markers and annotations.

`func annotationTitles(Visibility) -> some MapContent`

Sets the visibility of titles for markers and annotations.

`func foregroundStyle(some ShapeStyle) -> some MapContent`

Specifies the shape style used to fill content in drawing map overlays.

`func mapOverlayLevel(level: MKOverlayLevel) -> some MapContent`

Specifies the position of overlays relative to other map content.

`func stroke(some ShapeStyle, lineWidth: CGFloat) -> some MapContent`

Applies the given shape style to drawn map overlays.

`func stroke(some ShapeStyle, style: StrokeStyle) -> some MapContent`

Applies the given shape style to drawn map overlays.

`func stroke(lineWidth: CGFloat) -> some MapContent`

Sets the line width used for drawing map overlays.

`func strokeStyle(style: StrokeStyle) -> some MapContent`

Applies the given stroke style to drawn map overlays.

`func tag<V>(V) -> some MapContent`

Sets the unique tag value of this piece of map content.

`func tint<S>(S) -> some MapContent`

The tint shape style to apply to map content.

