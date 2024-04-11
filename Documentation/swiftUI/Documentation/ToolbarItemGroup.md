Initializer

# init(placement:content:)

Creates a toolbar item group with a specified placement and content.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(
        placement: ToolbarItemPlacement = .automatic,
        @ViewBuilder content: () -> Content
    )

## Discussion

  * placement: Which section of the toolbar all of its vended `ToolbarItem`s should be placed in.

  * content: The content of the group. Each view specified in the `ViewBuilder` will be given its own `ToolbarItem` in the toolbar.

## See Also

### Creating a toolbar item group

`init<C, L>(placement: ToolbarItemPlacement, content: () -> C, label: () ->
L)`

Creates a toolbar item group with the specified placement, content, and a
label describing that content.

Available when `Content` conforms to `View`.

Initializer

# init(placement:content:label:)

Creates a toolbar item group with the specified placement, content, and a
label describing that content.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init<C, L>(
        placement: ToolbarItemPlacement = .automatic,
        @ViewBuilder content: () -> C,
        @ViewBuilder label: () -> L
    ) where Content == LabeledToolbarItemGroupContent<C, L>, C : View, L : View

Available when `Content` conforms to `View`.

##  Parameters

`placement`

    

Which section of the toolbar the item should be placed in.

`content`

    

The content of the item.

`label`

    

The label describing the content of the item.

## Discussion

A toolbar item group provided a label wraps its content within a
`ControlGroup` which allows the content to collapse down into a menu that
presents its content based on available space.

## See Also

### Creating a toolbar item group

`init(placement: ToolbarItemPlacement, content: () -> Content)`

Creates a toolbar item group with a specified placement and content.

Structure

# LabeledToolbarItemGroupContent

A view that represents the view of a toolbar item group with a specified
label.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    struct LabeledToolbarItemGroupContent<Content, Label> where Content : View, Label : View

## Overview

You don’t create this type directly. SwiftUI creates it when you build a
`ToolbarItemGroup`.

## Relationships

### Conforms To

  * `View`

