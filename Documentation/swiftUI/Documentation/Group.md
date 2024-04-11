Initializer

# init(content:)

Creates a group of views.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(@ViewBuilder content: () -> Content)

Available when `Content` conforms to `View`.

##  Parameters

`content`

    

A `ViewBuilder` that produces the views to group.

## See Also

### Creating a group

`init(content: () -> Content)`

Creates a group of scenes.

Available when `Content` conforms to `Scene`.

`init(content: () -> Content)`

Creates a group of commands.

Available when `Content` conforms to `Commands`.

`init(content: () -> Content)`

Creates a group of toolbar content instances.

Available when `Content` conforms to `ToolbarContent`.

`init(content: () -> Content)`

Creates a group of customizable toolbar content instances.

Available when `Content` conforms to `CustomizableToolbarContent`.

`init<R>(content: () -> Content)`

Creates a group of table rows.

Available when `Content` conforms to `TableRowContent`.

`init<R, C>(content: () -> Content)`

Creates a group of table columns.

Available when `Content` conforms to `TableColumnContent`.

`init(content: () -> Content)`

Creates an instance that generates Rotor content by combining, in order, all
the Rotor content specified in the passed-in result builder.

Available when `Content` conforms to `AccessibilityRotorContent`.

Initializer

# init(content:)

Creates a group of scenes.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(@SceneBuilder content: () -> Content)

Available when `Content` conforms to `Scene`.

##  Parameters

`content`

    

A `SceneBuilder` that produces the scenes to group.

## See Also

### Creating a group

`init(content: () -> Content)`

Creates a group of views.

Available when `Content` conforms to `View`.

`init(content: () -> Content)`

Creates a group of commands.

Available when `Content` conforms to `Commands`.

`init(content: () -> Content)`

Creates a group of toolbar content instances.

Available when `Content` conforms to `ToolbarContent`.

`init(content: () -> Content)`

Creates a group of customizable toolbar content instances.

Available when `Content` conforms to `CustomizableToolbarContent`.

`init<R>(content: () -> Content)`

Creates a group of table rows.

Available when `Content` conforms to `TableRowContent`.

`init<R, C>(content: () -> Content)`

Creates a group of table columns.

Available when `Content` conforms to `TableColumnContent`.

`init(content: () -> Content)`

Creates an instance that generates Rotor content by combining, in order, all
the Rotor content specified in the passed-in result builder.

Available when `Content` conforms to `AccessibilityRotorContent`.

Initializer

# init(content:)

Creates a group of commands.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    init(@CommandsBuilder content: () -> Content)

Available when `Content` conforms to `Commands`.

##  Parameters

`content`

    

A `CommandsBuilder` that produces the commands to group.

## See Also

### Creating a group

`init(content: () -> Content)`

Creates a group of views.

Available when `Content` conforms to `View`.

`init(content: () -> Content)`

Creates a group of scenes.

Available when `Content` conforms to `Scene`.

`init(content: () -> Content)`

Creates a group of toolbar content instances.

Available when `Content` conforms to `ToolbarContent`.

`init(content: () -> Content)`

Creates a group of customizable toolbar content instances.

Available when `Content` conforms to `CustomizableToolbarContent`.

`init<R>(content: () -> Content)`

Creates a group of table rows.

Available when `Content` conforms to `TableRowContent`.

`init<R, C>(content: () -> Content)`

Creates a group of table columns.

Available when `Content` conforms to `TableColumnContent`.

`init(content: () -> Content)`

Creates an instance that generates Rotor content by combining, in order, all
the Rotor content specified in the passed-in result builder.

Available when `Content` conforms to `AccessibilityRotorContent`.

Initializer

# init(content:)

Creates a group of toolbar content instances.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(@ToolbarContentBuilder content: () -> Content)

Available when `Content` conforms to `ToolbarContent`.

##  Parameters

`content`

    

A `ToolbarContentBuilder` that produces the toolbar content instances to
group.

## See Also

### Creating a group

`init(content: () -> Content)`

Creates a group of views.

Available when `Content` conforms to `View`.

`init(content: () -> Content)`

Creates a group of scenes.

Available when `Content` conforms to `Scene`.

`init(content: () -> Content)`

Creates a group of commands.

Available when `Content` conforms to `Commands`.

`init(content: () -> Content)`

Creates a group of customizable toolbar content instances.

Available when `Content` conforms to `CustomizableToolbarContent`.

`init<R>(content: () -> Content)`

Creates a group of table rows.

Available when `Content` conforms to `TableRowContent`.

`init<R, C>(content: () -> Content)`

Creates a group of table columns.

Available when `Content` conforms to `TableColumnContent`.

`init(content: () -> Content)`

Creates an instance that generates Rotor content by combining, in order, all
the Rotor content specified in the passed-in result builder.

Available when `Content` conforms to `AccessibilityRotorContent`.

Initializer

# init(content:)

Creates a group of customizable toolbar content instances.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(@ToolbarContentBuilder content: () -> Content)

Available when `Content` conforms to `CustomizableToolbarContent`.

##  Parameters

`content`

    

A `ToolbarContentBuilder` that produces the customizable toolbar content
instances to group.

## See Also

### Creating a group

`init(content: () -> Content)`

Creates a group of views.

Available when `Content` conforms to `View`.

`init(content: () -> Content)`

Creates a group of scenes.

Available when `Content` conforms to `Scene`.

`init(content: () -> Content)`

Creates a group of commands.

Available when `Content` conforms to `Commands`.

`init(content: () -> Content)`

Creates a group of toolbar content instances.

Available when `Content` conforms to `ToolbarContent`.

`init<R>(content: () -> Content)`

Creates a group of table rows.

Available when `Content` conforms to `TableRowContent`.

`init<R, C>(content: () -> Content)`

Creates a group of table columns.

Available when `Content` conforms to `TableColumnContent`.

`init(content: () -> Content)`

Creates an instance that generates Rotor content by combining, in order, all
the Rotor content specified in the passed-in result builder.

Available when `Content` conforms to `AccessibilityRotorContent`.

Initializer

# init(content:)

Creates a group of table rows.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<R>(@TableRowBuilder<R> content: () -> Content) where R == Content.TableRowValue

Available when `Content` conforms to `TableRowContent`.

##  Parameters

`content`

    

A `TableRowBuilder` that produces the rows to group.

## See Also

### Creating a group

`init(content: () -> Content)`

Creates a group of views.

Available when `Content` conforms to `View`.

`init(content: () -> Content)`

Creates a group of scenes.

Available when `Content` conforms to `Scene`.

`init(content: () -> Content)`

Creates a group of commands.

Available when `Content` conforms to `Commands`.

`init(content: () -> Content)`

Creates a group of toolbar content instances.

Available when `Content` conforms to `ToolbarContent`.

`init(content: () -> Content)`

Creates a group of customizable toolbar content instances.

Available when `Content` conforms to `CustomizableToolbarContent`.

`init<R, C>(content: () -> Content)`

Creates a group of table columns.

Available when `Content` conforms to `TableColumnContent`.

`init(content: () -> Content)`

Creates an instance that generates Rotor content by combining, in order, all
the Rotor content specified in the passed-in result builder.

Available when `Content` conforms to `AccessibilityRotorContent`.

Initializer

# init(content:)

Creates a group of table columns.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<R, C>(@TableColumnBuilder<R, C> content: () -> Content) where R == Content.TableRowValue, C == Content.TableColumnSortComparator

Available when `Content` conforms to `TableColumnContent`.

##  Parameters

`content`

    

A `TableColumnBuilder` that produces the columns to group.

## See Also

### Creating a group

`init(content: () -> Content)`

Creates a group of views.

Available when `Content` conforms to `View`.

`init(content: () -> Content)`

Creates a group of scenes.

Available when `Content` conforms to `Scene`.

`init(content: () -> Content)`

Creates a group of commands.

Available when `Content` conforms to `Commands`.

`init(content: () -> Content)`

Creates a group of toolbar content instances.

Available when `Content` conforms to `ToolbarContent`.

`init(content: () -> Content)`

Creates a group of customizable toolbar content instances.

Available when `Content` conforms to `CustomizableToolbarContent`.

`init<R>(content: () -> Content)`

Creates a group of table rows.

Available when `Content` conforms to `TableRowContent`.

`init(content: () -> Content)`

Creates an instance that generates Rotor content by combining, in order, all
the Rotor content specified in the passed-in result builder.

Available when `Content` conforms to `AccessibilityRotorContent`.

Initializer

# init(content:)

Creates an instance that generates Rotor content by combining, in order, all
the Rotor content specified in the passed-in result builder.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init(@AccessibilityRotorContentBuilder content: () -> Content)

Available when `Content` conforms to `AccessibilityRotorContent`.

##  Parameters

`content`

    

The result builder that generates Rotor content for the group.

## See Also

### Creating a group

`init(content: () -> Content)`

Creates a group of views.

Available when `Content` conforms to `View`.

`init(content: () -> Content)`

Creates a group of scenes.

Available when `Content` conforms to `Scene`.

`init(content: () -> Content)`

Creates a group of commands.

Available when `Content` conforms to `Commands`.

`init(content: () -> Content)`

Creates a group of toolbar content instances.

Available when `Content` conforms to `ToolbarContent`.

`init(content: () -> Content)`

Creates a group of customizable toolbar content instances.

Available when `Content` conforms to `CustomizableToolbarContent`.

`init<R>(content: () -> Content)`

Creates a group of table rows.

Available when `Content` conforms to `TableRowContent`.

`init<R, C>(content: () -> Content)`

Creates a group of table columns.

Available when `Content` conforms to `TableColumnContent`.

Initializer

# init(content:)

Creates a group of map content.

MapKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    init(@MapContentBuilder content: () -> Content)

Available when `Content` conforms to `MapContent`.

##  Parameters

`content`

    

A map content builder that produces the map content to group.

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

