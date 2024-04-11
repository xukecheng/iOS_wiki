Initializer

# init(_:content:)

Creates a new menu with a localized name for a collection of app- specific
commands, inserted in the standard location for app menus (after the View
menu, in order with other menus declared without an explicit location).

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    init(
        _ nameKey: LocalizedStringKey,
        @ViewBuilder content: () -> Content
    )

## See Also

### Creating a command menu

`init(Text, content: () -> Content)`

Creates a new menu for a collection of app-specific commands, inserted in the
standard location for app menus (after the View menu, in order with other
menus declared without an explicit location).

`init<S>(S, content: () -> Content)`

Creates a new menu for a collection of app-specific commands, inserted in the
standard location for app menus (after the View menu, in order with other
menus declared without an explicit location).

Initializer

# init(_:content:)

Creates a new menu for a collection of app-specific commands, inserted in the
standard location for app menus (after the View menu, in order with other
menus declared without an explicit location).

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    init(
        _ name: Text,
        @ViewBuilder content: () -> Content
    )

## See Also

### Creating a command menu

`init(LocalizedStringKey, content: () -> Content)`

Creates a new menu with a localized name for a collection of app- specific
commands, inserted in the standard location for app menus (after the View
menu, in order with other menus declared without an explicit location).

`init<S>(S, content: () -> Content)`

Creates a new menu for a collection of app-specific commands, inserted in the
standard location for app menus (after the View menu, in order with other
menus declared without an explicit location).

Initializer

# init(_:content:)

Creates a new menu for a collection of app-specific commands, inserted in the
standard location for app menus (after the View menu, in order with other
menus declared without an explicit location).

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    init<S>(
        _ name: S,
        @ViewBuilder content: () -> Content
    ) where S : StringProtocol

## See Also

### Creating a command menu

`init(LocalizedStringKey, content: () -> Content)`

Creates a new menu with a localized name for a collection of app- specific
commands, inserted in the standard location for app menus (after the View
menu, in order with other menus declared without an explicit location).

`init(Text, content: () -> Content)`

Creates a new menu for a collection of app-specific commands, inserted in the
standard location for app menus (after the View menu, in order with other
menus declared without an explicit location).

