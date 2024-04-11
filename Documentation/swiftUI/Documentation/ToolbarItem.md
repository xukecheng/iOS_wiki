Initializer

# init(placement:content:)

Creates a toolbar item with the specified placement and content.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(
        placement: ToolbarItemPlacement = .automatic,
        @ViewBuilder content: () -> Content
    )

Available when `ID` is `()` and `Content` conforms to `View`.

##  Parameters

`placement`

    

Which section of the toolbar the item should be placed in.

`content`

    

The content of the item.

## See Also

### Creating a toolbar item

`init(id: String, placement: ToolbarItemPlacement, content: () -> Content)`

Creates a toolbar item with the specified placement and content, which allows
for user customization.

Available when `ID` is `String` and `Content` conforms to `View`.

`init(id: String, placement: ToolbarItemPlacement, showsByDefault: Bool,
content: () -> Content)`

Creates a toolbar item with the specified placement and content, which allows
for user customization.

Available when `ID` is `String` and `Content` conforms to `View`.

Initializer

# init(id:placement:content:)

Creates a toolbar item with the specified placement and content, which allows
for user customization.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(
        id: String,
        placement: ToolbarItemPlacement = .automatic,
        @ViewBuilder content: () -> Content
    )

Available when `ID` is `String` and `Content` conforms to `View`.

##  Parameters

`id`

    

A unique identifier for this item.

`placement`

    

Which section of the toolbar the item should be placed in.

`content`

    

The content of the item.

## See Also

### Creating a toolbar item

`init(placement: ToolbarItemPlacement, content: () -> Content)`

Creates a toolbar item with the specified placement and content.

Available when `ID` is `()` and `Content` conforms to `View`.

`init(id: String, placement: ToolbarItemPlacement, showsByDefault: Bool,
content: () -> Content)`

Creates a toolbar item with the specified placement and content, which allows
for user customization.

Available when `ID` is `String` and `Content` conforms to `View`.

Initializer

# init(id:placement:showsByDefault:content:)

Creates a toolbar item with the specified placement and content, which allows
for user customization.

iOS 14.0–17.4  Deprecated  iPadOS 14.0–17.4  Deprecated  macOS 11.0–14.4
Deprecated  Mac Catalyst 14.0–17.4  Deprecated  tvOS 14.0–17.4  Deprecated
watchOS 7.0–10.4  Deprecated  visionOS 1.0+

    
    
    init(
        id: String,
        placement: ToolbarItemPlacement = .automatic,
        showsByDefault: Bool,
        @ViewBuilder content: () -> Content
    )

Available when `ID` is `String` and `Content` conforms to `View`.

##  Parameters

`id`

    

A unique identifier for this item.

`placement`

    

Which section of the toolbar the item should be placed in.

`showsByDefault`

    

Whether the item appears by default in the toolbar, or only shows if the user
explicitly adds it via customization.

`content`

    

The content of the item.

## See Also

### Creating a toolbar item

`init(placement: ToolbarItemPlacement, content: () -> Content)`

Creates a toolbar item with the specified placement and content.

Available when `ID` is `()` and `Content` conforms to `View`.

`init(id: String, placement: ToolbarItemPlacement, content: () -> Content)`

Creates a toolbar item with the specified placement and content, which allows
for user customization.

Available when `ID` is `String` and `Content` conforms to `View`.

