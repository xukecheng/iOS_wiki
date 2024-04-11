Initializer

# init(_:id:content:)

Creates a window with a localized title and an identifier.

macOS 13.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        id: String,
        @ViewBuilder content: () -> Content
    )

##  Parameters

`titleKey`

    

A localized string key to use for the window’s title in system menus and in
the window’s title bar. Provide a title that describes the purpose of the
window.

`id`

    

A unique string identifier that you can use to open the window.

`content`

    

The view content to display in the window.

## Discussion

The window displays the view that you specify.

## See Also

### Creating a window

`init<S>(S, id: String, content: () -> Content)`

Creates a window with a title string and an identifier.

`init(Text, id: String, content: () -> Content)`

Creates a window with a title and an identifier.

Initializer

# init(_:id:content:)

Creates a window with a title string and an identifier.

macOS 13.0+

    
    
    init<S>(
        _ title: S,
        id: String,
        @ViewBuilder content: () -> Content
    ) where S : StringProtocol

##  Parameters

`title`

    

A string to use for the window’s title in system menus and in the window’s
title bar. Provide a title that describes the purpose of the window.

`id`

    

A unique string identifier that you can use to open the window.

`content`

    

The view content to display in the window.

## Discussion

The window displays the view that you specify.

## See Also

### Creating a window

`init(LocalizedStringKey, id: String, content: () -> Content)`

Creates a window with a localized title and an identifier.

`init(Text, id: String, content: () -> Content)`

Creates a window with a title and an identifier.

Initializer

# init(_:id:content:)

Creates a window with a title and an identifier.

macOS 13.0+

    
    
    init(
        _ title: Text,
        id: String,
        @ViewBuilder content: () -> Content
    )

##  Parameters

`title`

    

The `Text` view to use for the window’s title in system menus and in the
window’s title bar. Provide a title that describes the purpose of the window.

`id`

    

A unique string identifier that you can use to open the window.

`content`

    

The view content to display in the window.

## Discussion

The window displays the view that you specify.

Important

The system ignores any text styling that you apply to the `Text` view title,
like bold or italics. However, you can use the formatting controls that the
view offers, like for localization, dates, and numerical representations.

## See Also

### Creating a window

`init(LocalizedStringKey, id: String, content: () -> Content)`

Creates a window with a localized title and an identifier.

`init<S>(S, id: String, content: () -> Content)`

Creates a window with a title string and an identifier.

