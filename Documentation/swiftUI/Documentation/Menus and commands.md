Structure

# Menu

A control for presenting a menu of actions.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 17.0+  visionOS
1.0+

    
    
    struct Menu<Label, Content> where Label : View, Content : View

## Overview

The following example presents a menu of three buttons and a submenu, which
contains three buttons of its own.

You can create the menu’s title with a `LocalizedStringKey`, as seen in the
previous example, or with a view builder that creates multiple views, such as
an image and a text view:

### Primary action

Menus can be created with a custom primary action. The primary action will be
performed when the user taps or clicks on the body of the control, and the
menu presentation will happen on a secondary gesture, such as on long press or
on click of the menu indicator. The following example creates a menu that adds
bookmarks, with advanced options that are presented in a menu.

### Styling menus

Use the `menuStyle(_:)` modifier to change the style of all menus in a view.
The following example shows how to apply a custom style:

## Topics

### Creating a menu from content

`init(content: () -> Content, label: () -> Label)`

Creates a menu with a custom label.

Available when `Label` conforms to `View` and `Content` conforms to `View`.

`init(LocalizedStringKey, content: () -> Content)`

Creates a menu that generates its label from a localized string key.

Available when `Label` conforms to `View` and `Content` conforms to `View`.

`init<S>(S, content: () -> Content)`

Creates a menu that generates its label from a string.

Available when `Label` conforms to `View` and `Content` conforms to `View`.

### Creating a menu with a primary action

`init(content: () -> Content, label: () -> Label, primaryAction: () -> Void)`

Creates a menu with a custom primary action and custom label.

Available when `Label` conforms to `View` and `Content` conforms to `View`.

`init(LocalizedStringKey, content: () -> Content, primaryAction: () -> Void)`

Creates a menu with a custom primary action that generates its label from a
localized string key.

Available when `Label` conforms to `View` and `Content` conforms to `View`.

`init<S>(S, content: () -> Content, primaryAction: () -> Void)`

Creates a menu with a custom primary action that generates its label from a
string.

Available when `Label` conforms to `View` and `Content` conforms to `View`.

### Creating a menu with an image label

`init<S>(S, image: ImageResource, content: () -> Content)`

Creates a menu that generates its label from a string and image resource.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init(LocalizedStringKey, image: ImageResource, content: () -> Content)`

Creates a menu that generates its label from a localized string key and image
resource.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init(LocalizedStringKey, image: ImageResource, content: () -> Content,
primaryAction: () -> Void)`

Creates a menu with a custom primary action that generates its label from a
localized string key.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init<S>(S, systemImage: String, content: () -> Content)`

Creates a menu that generates its label from a string and system image.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init(LocalizedStringKey, systemImage: String, content: () -> Content)`

Creates a menu that generates its label from a localized string key and system
image.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init(LocalizedStringKey, systemImage: String, content: () -> Content,
primaryAction: () -> Void)`

Creates a menu with a custom primary action that generates its label from a
localized string key and system image.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

### Creating a menu from a configuration

`init(MenuStyleConfiguration)`

Creates a menu based on a style configuration.

Available when `Label` is `MenuStyleConfiguration.Label` and `Content` is
`MenuStyleConfiguration.Content`.

## Relationships

### Conforms To

  * `View`

## See Also

### Creating a menu

`func menuStyle<S>(S) -> some View`

Sets the style for menus within this view.

Instance Method

# menuStyle(_:)

Sets the style for menus within this view.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 17.0+  visionOS
1.0+

    
    
    func menuStyle<S>(_ style: S) -> some View where S : MenuStyle
    

## Discussion

To set a specific style for all menu instances within a view, use the
`menuStyle(_:)` modifier:

## See Also

### Creating a menu

`struct Menu`

A control for presenting a menu of actions.

Instance Method

# contextMenu(menuItems:)

Adds a context menu to a view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 14.0+  watchOS
6.0–7.0  Deprecated  visionOS 1.0+

    
    
    func contextMenu<MenuItems>(@ViewBuilder menuItems: () -> MenuItems) -> some View where MenuItems : View
    

##  Parameters

`menuItems`

    

A closure that produces the menu’s contents. You can deactivate the context
menu by returning nothing from the closure.

## Return Value

A view that can display a context menu.

## Discussion

Use this modifier to add a context menu to a view in your app’s user
interface. Compose the menu by returning controls like `Button`, `Toggle`, and
`Picker` from the `menuItems` closure. You can also use `Menu` to define
submenus or `Section` to group items.

The following example creates a `Text` view that has a context menu with two
buttons:

People can activate the menu with an action like Control-clicking, or by using
the touch and hold gesture in iOS and iPadOS:

The system dismisses the menu if someone makes a selection, or taps or clicks
outside the menu.

If you want to show a preview beside the menu, use
`contextMenu(menuItems:preview:)`. To add a context menu to a container that
supports selection, like a `List` or a `Table`, and to distinguish between
menu activation on a selection and activation in an empty area of the
container, use `contextMenu(forSelectionType:menu:primaryAction:)`.

## See Also

### Creating context menus

`func contextMenu<M, P>(menuItems: () -> M, preview: () -> P) -> some View`

Adds a context menu with a preview to a view.

`func contextMenu<I, M>(forSelectionType: I.Type, menu: (Set<I>) -> M,
primaryAction: ((Set<I>) -> Void)?) -> some View`

Adds an item-based context menu to a view.

Instance Method

# contextMenu(menuItems:preview:)

Adds a context menu with a preview to a view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  visionOS
1.0+

    
    
    func contextMenu<M, P>(
        @ViewBuilder menuItems: () -> M,
        @ViewBuilder preview: () -> P
    ) -> some View where M : View, P : View
    

##  Parameters

`menuItems`

    

A closure that produces the menu’s contents. You can deactivate the context
menu by returning nothing from the closure.

`preview`

    

A view that the system displays along with the menu.

## Return Value

A view that can display a context menu with a preview.

## Discussion

When you use this modifer to add a context menu to a view in your app’s user
interface, the system shows a preview beside the menu. Compose the menu by
returning controls like `Button`, `Toggle`, and `Picker` from the `menuItems`
closure. You can also use `Menu` to define submenus or `Section` to group
items.

Define the preview by returning a view from the `preview` closure. The system
sizes the preview to match the size of its content. For example, you can add a
two button context menu to a `Text` view, and include an `Image` as a preview:

When someone activates the context menu with an action like touch and hold in
iOS or iPadOS, the system displays the image and the menu:

Note

This view modifier produces a context menu on macOS, but that platform doesn’t
display the preview.

If you don’t need a preview, use `contextMenu(menuItems:)` instead. If you
want to add a context menu to a container that supports selection, like a
`List` or a `Table`, and you want to distinguish between menu activation on a
selection and activation in an empty area of the container, use
`contextMenu(forSelectionType:menu:primaryAction:)`.

## See Also

### Creating context menus

`func contextMenu<MenuItems>(menuItems: () -> MenuItems) -> some View`

Adds a context menu to a view.

`func contextMenu<I, M>(forSelectionType: I.Type, menu: (Set<I>) -> M,
primaryAction: ((Set<I>) -> Void)?) -> some View`

Adds an item-based context menu to a view.

Instance Method

# contextMenu(forSelectionType:menu:primaryAction:)

Adds an item-based context menu to a view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    func contextMenu<I, M>(
        forSelectionType itemType: I.Type = I.self,
        @ViewBuilder menu: @escaping (Set<I>) -> M,
        primaryAction: ((Set<I>) -> Void)? = nil
    ) -> some View where I : Hashable, M : View
    

##  Parameters

`itemType`

    

The identifier type of the items. Ensure that this matches the container’s
selection type.

`menu`

    

A closure that produces the menu. A single parameter to the closure contains
the set of items to act on. An empty set indicates menu activation over the
empty area of the selectable container, while a non-empty set indicates menu
activation over selected items. Use controls like `Button`, `Picker`, and
`Toggle` to define the menu items. You can also create submenus using `Menu`,
or group items with `Section`. You can deactivate the context menu by
returning nothing from the closure.

`primaryAction`

    

A closure that defines the action to perform in response to the primary
interaction. A single parameter to the closure contains the set of items to
act on.

## Return Value

A view that can display an item-based context menu.

## Discussion

You can add an item-based context menu to a container that supports selection,
like a `List` or a `Table`. In the closure that you use to define the menu,
you receive a collection of items that depends on the selection state of the
container and the location where the person clicks or taps to activate the
menu. The collection contains:

  * The selected item or items, when people initiate the context menu from any selected item.

  * Nothing, if people tap or click to activate the context menu from an empty part of the container. This is true even when one or more items is currently selected.

You can vary the menu contents according to the number of selected items. For
example, the following code has a list that defines an empty area menu, a
single item menu, and a multi-item menu:

The above example assumes that the `Item` type conforms to the `Identifiable`
protocol, and relies on the associated `ID` type for both selection and
context menu presentation.

If you add the modifier to a view hierarchy that doesn’t have a container that
supports selection, the context menu never activates. To add a context menu
that doesn’t depend on selection behavior, use `contextMenu(menuItems:)`. To
add a context menu to a specific row in a table, use
`contextMenu(menuItems:)`.

### Add a primary action

Optionally, you can add a custom primary action to the context menu. In macOS,
a single click on a row in a selectable container selects that row, and a
double click performs the primary action. In iOS and iPadOS, tapping on the
row activates the primary action. To select a row without performing an
action, either enter edit mode or hold shift or command on a keyboard while
tapping the row.

For example, you can modify the context menu from the previous example so that
double clicking the row on macOS opens a new window for selected items. Get
the `OpenWindowAction` from the environment:

Then call `openWindow` from inside the `primaryAction` closure for each item:

The open window action depends on the declaration of a `WindowGroup` scene in
your `App` that responds to the `Item` type:

## See Also

### Creating context menus

`func contextMenu<MenuItems>(menuItems: () -> MenuItems) -> some View`

Adds a context menu to a view.

`func contextMenu<M, P>(menuItems: () -> M, preview: () -> P) -> some View`

Adds a context menu with a preview to a view.

Instance Method

# commands(content:)

Adds commands to the scene.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    func commands<Content>(@CommandsBuilder content: () -> Content) -> some Scene where Content : Commands
    

## Discussion

Commands are realized in different ways on different platforms. On macOS, the
main menu uses the available command menus and groups to organize its main
menu items. Each menu is represented as a top-level menu bar menu, and each
command group has a corresponding set of menu items in one of the top-level
menus, delimited by separator menu items.

On iPadOS, commands with keyboard shortcuts are exposed in the shortcut
discoverability HUD that users see when they hold down the Command (⌘) key.

## See Also

### Defining commands

`func commandsRemoved() -> some Scene`

Removes all commands defined by the modified scene.

`func commandsReplaced<Content>(content: () -> Content) -> some Scene`

Replaces all commands defined by the modified scene with the commands from the
builder.

`protocol Commands`

Conforming types represent a group of related commands that can be exposed to
the user via the main menu on macOS and key commands on iOS.

`struct CommandMenu`

Command menus are stand-alone, top-level containers for controls that perform
related, app-specific commands.

`struct CommandGroup`

Groups of controls that you can add to existing command menus.

`struct CommandsBuilder`

Constructs command sets from multi-expression closures. Like `ViewBuilder`, it
supports up to ten expressions in the closure body.

`struct CommandGroupPlacement`

The standard locations that you can place new command groups relative to.

Instance Method

# commandsRemoved()

Removes all commands defined by the modified scene.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    func commandsRemoved() -> some Scene
    

## Return Value

A scene that excludes any commands defined by its children.

## Discussion

`WindowGroup`, `Window`, and other scene types all have an associated set of
commands that they include by default. Apply this modifier to a scene to
exclude those commands.

For example, the following code adds a scene for presenting the details of an
individual data model in a separate window. To ensure that the window can only
appear programmatically, we remove the scene’s commands, including File > New
Note Window.

## See Also

### Defining commands

`func commands<Content>(content: () -> Content) -> some Scene`

Adds commands to the scene.

`func commandsReplaced<Content>(content: () -> Content) -> some Scene`

Replaces all commands defined by the modified scene with the commands from the
builder.

`protocol Commands`

Conforming types represent a group of related commands that can be exposed to
the user via the main menu on macOS and key commands on iOS.

`struct CommandMenu`

Command menus are stand-alone, top-level containers for controls that perform
related, app-specific commands.

`struct CommandGroup`

Groups of controls that you can add to existing command menus.

`struct CommandsBuilder`

Constructs command sets from multi-expression closures. Like `ViewBuilder`, it
supports up to ten expressions in the closure body.

`struct CommandGroupPlacement`

The standard locations that you can place new command groups relative to.

Instance Method

# commandsReplaced(content:)

Replaces all commands defined by the modified scene with the commands from the
builder.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    func commandsReplaced<Content>(@CommandsBuilder content: () -> Content) -> some Scene where Content : Commands
    

##  Parameters

`content`

    

A `Commands` builder whose output will be used to replace the commands
normally provided by the modified scene.

## Return Value

A scene that replaces any commands defined by its children with alternative
content.

## Discussion

`WindowGroup`, `Window`, and other scene types all have an associated set of
commands that they include by default. Apply this modifier to a scene to
replace those commands with the output from the given builder.

For example, the following code adds a scene for showing the contents of the
pasteboard in a dedicated window. We replace the scene’s default Window >
Clipboard menu command with a custom Edit > Show Clipboard command that we
place next to the other pasteboard commands.

## See Also

### Defining commands

`func commands<Content>(content: () -> Content) -> some Scene`

Adds commands to the scene.

`func commandsRemoved() -> some Scene`

Removes all commands defined by the modified scene.

`protocol Commands`

Conforming types represent a group of related commands that can be exposed to
the user via the main menu on macOS and key commands on iOS.

`struct CommandMenu`

Command menus are stand-alone, top-level containers for controls that perform
related, app-specific commands.

`struct CommandGroup`

Groups of controls that you can add to existing command menus.

`struct CommandsBuilder`

Constructs command sets from multi-expression closures. Like `ViewBuilder`, it
supports up to ten expressions in the closure body.

`struct CommandGroupPlacement`

The standard locations that you can place new command groups relative to.

Protocol

# Commands

Conforming types represent a group of related commands that can be exposed to
the user via the main menu on macOS and key commands on iOS.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    protocol Commands

## Topics

### Implementing commands

`var body: Self.Body`

The contents of the command hierarchy.

**Required**

` associatedtype Body : Commands`

The type of commands that represents the body of this command hierarchy.

**Required**

## Relationships

### Conforming Types

  * `CommandGroup`
  * `CommandMenu`
  * `EmptyCommands`
  * `Group`

Conforms when `Content` conforms to `Commands`.

  * `ImportFromDevicesCommands`
  * `InspectorCommands`
  * `SidebarCommands`
  * `TextEditingCommands`
  * `TextFormattingCommands`
  * `ToolbarCommands`

## See Also

### Defining commands

`func commands<Content>(content: () -> Content) -> some Scene`

Adds commands to the scene.

`func commandsRemoved() -> some Scene`

Removes all commands defined by the modified scene.

`func commandsReplaced<Content>(content: () -> Content) -> some Scene`

Replaces all commands defined by the modified scene with the commands from the
builder.

`struct CommandMenu`

Command menus are stand-alone, top-level containers for controls that perform
related, app-specific commands.

`struct CommandGroup`

Groups of controls that you can add to existing command menus.

`struct CommandsBuilder`

Constructs command sets from multi-expression closures. Like `ViewBuilder`, it
supports up to ten expressions in the closure body.

`struct CommandGroupPlacement`

The standard locations that you can place new command groups relative to.

Structure

# CommandMenu

Command menus are stand-alone, top-level containers for controls that perform
related, app-specific commands.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    struct CommandMenu<Content> where Content : View

## Overview

Command menus are realized as menu bar menus on macOS, inserted between the
built-in View and Window menus in order of declaration. On iOS, iPadOS, and
tvOS, SwiftUI creates key commands for each of a menu’s commands that has a
keyboard shortcut.

## Topics

### Creating a command menu

`init(LocalizedStringKey, content: () -> Content)`

Creates a new menu with a localized name for a collection of app- specific
commands, inserted in the standard location for app menus (after the View
menu, in order with other menus declared without an explicit location).

`init(Text, content: () -> Content)`

Creates a new menu for a collection of app-specific commands, inserted in the
standard location for app menus (after the View menu, in order with other
menus declared without an explicit location).

`init<S>(S, content: () -> Content)`

Creates a new menu for a collection of app-specific commands, inserted in the
standard location for app menus (after the View menu, in order with other
menus declared without an explicit location).

## Relationships

### Conforms To

  * `Commands`

## See Also

### Defining commands

`func commands<Content>(content: () -> Content) -> some Scene`

Adds commands to the scene.

`func commandsRemoved() -> some Scene`

Removes all commands defined by the modified scene.

`func commandsReplaced<Content>(content: () -> Content) -> some Scene`

Replaces all commands defined by the modified scene with the commands from the
builder.

`protocol Commands`

Conforming types represent a group of related commands that can be exposed to
the user via the main menu on macOS and key commands on iOS.

`struct CommandGroup`

Groups of controls that you can add to existing command menus.

`struct CommandsBuilder`

Constructs command sets from multi-expression closures. Like `ViewBuilder`, it
supports up to ten expressions in the closure body.

`struct CommandGroupPlacement`

The standard locations that you can place new command groups relative to.

Structure

# CommandGroup

Groups of controls that you can add to existing command menus.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    struct CommandGroup<Content> where Content : View

## Overview

In macOS, SwiftUI realizes command groups as collections of menu items in a
menu bar menu. In iOS, iPadOS, and tvOS, SwiftUI creates key commands for each
of a group’s commands that has a keyboard shortcut.

## Topics

### Creating a command group

`init(after: CommandGroupPlacement, addition: () -> Content)`

A value describing the addition of the given views to the end of the indicated
group.

`init(before: CommandGroupPlacement, addition: () -> Content)`

A value describing the addition of the given views to the beginning of the
indicated group.

`init(replacing: CommandGroupPlacement, addition: () -> Content)`

A value describing the complete replacement of the contents of the indicated
group with the given views.

## Relationships

### Conforms To

  * `Commands`

## See Also

### Defining commands

`func commands<Content>(content: () -> Content) -> some Scene`

Adds commands to the scene.

`func commandsRemoved() -> some Scene`

Removes all commands defined by the modified scene.

`func commandsReplaced<Content>(content: () -> Content) -> some Scene`

Replaces all commands defined by the modified scene with the commands from the
builder.

`protocol Commands`

Conforming types represent a group of related commands that can be exposed to
the user via the main menu on macOS and key commands on iOS.

`struct CommandMenu`

Command menus are stand-alone, top-level containers for controls that perform
related, app-specific commands.

`struct CommandsBuilder`

Constructs command sets from multi-expression closures. Like `ViewBuilder`, it
supports up to ten expressions in the closure body.

`struct CommandGroupPlacement`

The standard locations that you can place new command groups relative to.

Structure

# CommandsBuilder

Constructs command sets from multi-expression closures. Like `ViewBuilder`, it
supports up to ten expressions in the closure body.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    @resultBuilder
    struct CommandsBuilder

## Topics

### Building content

`static func buildBlock() -> EmptyCommands`

Builds an empty command set from a block containing no statements.

`static func buildBlock<C>(C) -> C`

Passes a single command group written as a child group through modified.

`static func buildBlock<C0, C1>(C0, C1) -> some Commands`

`static func buildBlock<C0, C1, C2>(C0, C1, C2) -> some Commands`

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) -> some Commands`

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) -> some
Commands`

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
some Commands`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> some Commands`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> some Commands`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> some Commands`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> some Commands`

### Building conditionally

`static func buildEither<T, F>(first: T) -> _ConditionalContent<T, F>`

Produces content for a conditional statement in a multi-statement closure when
the condition is true.

`static func buildEither<T, F>(second: F) -> _ConditionalContent<T, F>`

Produces content for a conditional statement in a multi-statement closure when
the condition is false.

`static func buildIf<C>(C?) -> C?`

Produces an optional widget for conditional statements in multi-statement
closures that’s only visible when the condition evaluates to true.

`static func buildLimitedAvailability<C>(C) -> some Commands`

Processes commands for a conditional compiler-control statement that performs
an availability check.

`static func buildExpression<Content>(Content) -> Content`

Builds an expression within the builder.

## See Also

### Defining commands

`func commands<Content>(content: () -> Content) -> some Scene`

Adds commands to the scene.

`func commandsRemoved() -> some Scene`

Removes all commands defined by the modified scene.

`func commandsReplaced<Content>(content: () -> Content) -> some Scene`

Replaces all commands defined by the modified scene with the commands from the
builder.

`protocol Commands`

Conforming types represent a group of related commands that can be exposed to
the user via the main menu on macOS and key commands on iOS.

`struct CommandMenu`

Command menus are stand-alone, top-level containers for controls that perform
related, app-specific commands.

`struct CommandGroup`

Groups of controls that you can add to existing command menus.

`struct CommandGroupPlacement`

The standard locations that you can place new command groups relative to.

Structure

# CommandGroupPlacement

The standard locations that you can place new command groups relative to.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    struct CommandGroupPlacement

## Overview

The names of these placements aren’t visible in the user interface, but the
discussion for each placement lists the items that it includes.

## Topics

### App interactions

`static let appInfo: CommandGroupPlacement`

Placement for commands that provide information about the app, the terms of
the user’s license agreement, and so on.

`static let appSettings: CommandGroupPlacement`

Placement for commands that expose app settings and preferences.

`static let appTermination: CommandGroupPlacement`

Placement for commands that result in app termination.

`static let appVisibility: CommandGroupPlacement`

Placement for commands that control the visibility of running apps.

`static let systemServices: CommandGroupPlacement`

Placement for commands that expose services other apps provide.

### File manipulation

`static let importExport: CommandGroupPlacement`

Placement for commands that relate to importing and exporting data using
formats that the app doesn’t natively support.

`static let newItem: CommandGroupPlacement`

Placement for commands that create and open different kinds of documents.

`static let printItem: CommandGroupPlacement`

Placement for commands related to printing app content.

`static let saveItem: CommandGroupPlacement`

Placement for commands that save open documents and close windows.

### Content updates

`static let pasteboard: CommandGroupPlacement`

Placement for commands that interact with the Clipboard and manipulate content
that is currently selected in the app’s view hierarchy.

`static let textEditing: CommandGroupPlacement`

Placement for commands that manipulate and transform text selections.

`static let textFormatting: CommandGroupPlacement`

Placement for commands that manipulate and transform the styles applied to
text selections.

`static let undoRedo: CommandGroupPlacement`

Placement for commands that control the Undo Manager.

### Bars

`static let sidebar: CommandGroupPlacement`

Placement for commands that control the app’s sidebar and full-screen modes.

`static let toolbar: CommandGroupPlacement`

Placement for commands that manipulate the toolbar.

### Windows

`static let singleWindowList: CommandGroupPlacement`

Placement for commands that describe and reveal any windows that the app
defines.

`static let windowArrangement: CommandGroupPlacement`

Placement for commands that arrange all of an app’s windows.

`static let windowList: CommandGroupPlacement`

Placement for commands that describe and reveal the app’s open windows.

`static let windowSize: CommandGroupPlacement`

Placement for commands that control the size of the window.

### Help

`static let help: CommandGroupPlacement`

Placement for commands that present documentation and helpful information to
people.

## See Also

### Defining commands

`func commands<Content>(content: () -> Content) -> some Scene`

Adds commands to the scene.

`func commandsRemoved() -> some Scene`

Removes all commands defined by the modified scene.

`func commandsReplaced<Content>(content: () -> Content) -> some Scene`

Replaces all commands defined by the modified scene with the commands from the
builder.

`protocol Commands`

Conforming types represent a group of related commands that can be exposed to
the user via the main menu on macOS and key commands on iOS.

`struct CommandMenu`

Command menus are stand-alone, top-level containers for controls that perform
related, app-specific commands.

`struct CommandGroup`

Groups of controls that you can add to existing command menus.

`struct CommandsBuilder`

Constructs command sets from multi-expression closures. Like `ViewBuilder`, it
supports up to ten expressions in the closure body.

Structure

# SidebarCommands

A built-in set of commands for manipulating window sidebars.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    struct SidebarCommands

## Overview

These commands are optional and can be explicitly requested by passing a value
of this type to the `commands(content:)` modifier.

## Topics

### Creating the command group

`init()`

A new value describing the built-in sidebar-related commands.

## Relationships

### Conforms To

  * `Commands`

## See Also

### Getting built-in command groups

`struct TextEditingCommands`

A built-in group of commands for searching, editing, and transforming
selections of text.

`struct TextFormattingCommands`

A built-in set of commands for transforming the styles applied to selections
of text.

`struct ToolbarCommands`

A built-in set of commands for manipulating window toolbars.

`struct ImportFromDevicesCommands`

A built-in set of commands that enables importing content from nearby devices.

`struct InspectorCommands`

A built-in set of commands for manipulating inspectors.

`struct EmptyCommands`

An empty group of commands.

Structure

# TextEditingCommands

A built-in group of commands for searching, editing, and transforming
selections of text.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    struct TextEditingCommands

## Overview

These commands are optional and can be explicitly requested by passing a value
of this type to the `Scene.commands(_:)` modifier.

## Topics

### Creating the command group

`init()`

A new value describing the built-in text-editing commands.

## Relationships

### Conforms To

  * `Commands`

## See Also

### Getting built-in command groups

`struct SidebarCommands`

A built-in set of commands for manipulating window sidebars.

`struct TextFormattingCommands`

A built-in set of commands for transforming the styles applied to selections
of text.

`struct ToolbarCommands`

A built-in set of commands for manipulating window toolbars.

`struct ImportFromDevicesCommands`

A built-in set of commands that enables importing content from nearby devices.

`struct InspectorCommands`

A built-in set of commands for manipulating inspectors.

`struct EmptyCommands`

An empty group of commands.

Structure

# TextFormattingCommands

A built-in set of commands for transforming the styles applied to selections
of text.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    struct TextFormattingCommands

## Overview

These commands are optional and can be explicitly requested by passing a value
of this type to the `Scene.commands(_:)` modifier.

## Topics

### Creating the command group

`init()`

A new value describing the built-in text-formatting commands.

## Relationships

### Conforms To

  * `Commands`

## See Also

### Getting built-in command groups

`struct SidebarCommands`

A built-in set of commands for manipulating window sidebars.

`struct TextEditingCommands`

A built-in group of commands for searching, editing, and transforming
selections of text.

`struct ToolbarCommands`

A built-in set of commands for manipulating window toolbars.

`struct ImportFromDevicesCommands`

A built-in set of commands that enables importing content from nearby devices.

`struct InspectorCommands`

A built-in set of commands for manipulating inspectors.

`struct EmptyCommands`

An empty group of commands.

Structure

# ToolbarCommands

A built-in set of commands for manipulating window toolbars.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    struct ToolbarCommands

## Overview

These commands are optional and can be explicitly requested by passing a value
of this type to the `commands(content:)` modifier.

## Topics

### Creating the command group

`init()`

A new value describing the built-in toolbar-related commands.

## Relationships

### Conforms To

  * `Commands`

## See Also

### Getting built-in command groups

`struct SidebarCommands`

A built-in set of commands for manipulating window sidebars.

`struct TextEditingCommands`

A built-in group of commands for searching, editing, and transforming
selections of text.

`struct TextFormattingCommands`

A built-in set of commands for transforming the styles applied to selections
of text.

`struct ImportFromDevicesCommands`

A built-in set of commands that enables importing content from nearby devices.

`struct InspectorCommands`

A built-in set of commands for manipulating inspectors.

`struct EmptyCommands`

An empty group of commands.

Structure

# ImportFromDevicesCommands

A built-in set of commands that enables importing content from nearby devices.

macOS 12.0+

    
    
    struct ImportFromDevicesCommands

## Overview

This set of commands adds items based on nearby devices and capabilities, like
taking photos or scanning documents. Views can receive imported content from
these menu items by using the `importsItemProviders(_:onImport:)` modifier.

These commands are optional and you can explicitly request them by passing a
value of this type to the `commands(content:)` modifier.

## Topics

### Creating the command group

`init()`

Creates a new set of device import commands.

## Relationships

### Conforms To

  * `Commands`

## See Also

### Getting built-in command groups

`struct SidebarCommands`

A built-in set of commands for manipulating window sidebars.

`struct TextEditingCommands`

A built-in group of commands for searching, editing, and transforming
selections of text.

`struct TextFormattingCommands`

A built-in set of commands for transforming the styles applied to selections
of text.

`struct ToolbarCommands`

A built-in set of commands for manipulating window toolbars.

`struct InspectorCommands`

A built-in set of commands for manipulating inspectors.

`struct EmptyCommands`

An empty group of commands.

Structure

# InspectorCommands

A built-in set of commands for manipulating inspectors.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    struct InspectorCommands

## Overview

`InspectorCommands` include a command for toggling the presented state of the
inspector with a keyboard shortcut of ⌘⌃I.

These commands are optional and can be explicitly requested by passing a value
of this type to the `commands(content:)` modifier:

## Topics

### Creating a command

`init()`

A new value describing the built-in inspector-related commands.

## Relationships

### Conforms To

  * `Commands`

## See Also

### Getting built-in command groups

`struct SidebarCommands`

A built-in set of commands for manipulating window sidebars.

`struct TextEditingCommands`

A built-in group of commands for searching, editing, and transforming
selections of text.

`struct TextFormattingCommands`

A built-in set of commands for transforming the styles applied to selections
of text.

`struct ToolbarCommands`

A built-in set of commands for manipulating window toolbars.

`struct ImportFromDevicesCommands`

A built-in set of commands that enables importing content from nearby devices.

`struct EmptyCommands`

An empty group of commands.

Structure

# EmptyCommands

An empty group of commands.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    struct EmptyCommands

## Topics

### Creating the command group

`init()`

Creates an empty command hierarchy.

## Relationships

### Conforms To

  * `Commands`

## See Also

### Getting built-in command groups

`struct SidebarCommands`

A built-in set of commands for manipulating window sidebars.

`struct TextEditingCommands`

A built-in group of commands for searching, editing, and transforming
selections of text.

`struct TextFormattingCommands`

A built-in set of commands for transforming the styles applied to selections
of text.

`struct ToolbarCommands`

A built-in set of commands for manipulating window toolbars.

`struct ImportFromDevicesCommands`

A built-in set of commands that enables importing content from nearby devices.

`struct InspectorCommands`

A built-in set of commands for manipulating inspectors.

Instance Method

# menuIndicator(_:)

Sets the menu indicator visibility for controls within this view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 17.0+  visionOS
1.0+

    
    
    func menuIndicator(_ visibility: Visibility) -> some View
    

##  Parameters

`visibility`

    

The menu indicator visibility to apply.

## Discussion

Use this modifier to override the default menu indicator visibility for
controls in this view. For example, the code below creates a menu without an
indicator:

Note

On tvOS, the standard button styles do not include a menu indicator, so this
modifier will have no effect when using a built-in button style. You can
implement an indicator in your own `ButtonStyle` implementation by checking
the value of the `menuIndicatorVisibility` environment value.

## See Also

### Showing a menu indicator

`var menuIndicatorVisibility: Visibility`

The menu indicator visibility to apply to controls within a view.

Instance Property

# menuIndicatorVisibility

The menu indicator visibility to apply to controls within a view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 17.0+  visionOS
1.0+

    
    
    var menuIndicatorVisibility: Visibility { get set }

## Discussion

Note

On tvOS, the standard button styles do not include a menu indicator, so this
modifier will have no effect when using a built-in button style. You can
implement an indicator in your own `ButtonStyle` implementation by checking
the value of this environment value.

## See Also

### Showing a menu indicator

`func menuIndicator(Visibility) -> some View`

Sets the menu indicator visibility for controls within this view.

Instance Method

# menuActionDismissBehavior(_:)

Tells a menu whether to dismiss after performing an action.

iOS 16.4+  iPadOS 16.4+  macOS 13.3+  Mac Catalyst 16.4+  tvOS 16.4+  watchOS
9.4+  visionOS 1.0+

    
    
    func menuActionDismissBehavior(_ behavior: MenuActionDismissBehavior) -> some View
    

##  Parameters

`dismissal`

    

The menu action dismissal behavior to apply.

## Return Value

A view that has the specified menu dismissal behavior.

## Discussion

Use this modifier to control the dismissal behavior of a menu. In the example
below, the menu doesn’t dismiss after someone chooses either the increase or
decrease action:

You can use this modifier on any controls that present a menu, like a `Picker`
that uses the `menu` style or a `ControlGroup`. For example, the code below
creates a picker that disables dismissal when someone selects one of the
options:

You can also use this modifier on context menus. The example below creates a
context menu that stays presented after someone selects an action to run:

## See Also

### Configuring menu dismissal

`struct MenuActionDismissBehavior`

The set of menu dismissal behavior options.

Structure

# MenuActionDismissBehavior

The set of menu dismissal behavior options.

iOS 16.4+  iPadOS 16.4+  macOS 13.3+  Mac Catalyst 16.4+  tvOS 16.4+  watchOS
9.4+  visionOS 1.0+

    
    
    struct MenuActionDismissBehavior

## Overview

Configure the menu dismissal behavior for a view hierarchy using the
`menuActionDismissBehavior(_:)` view modifier.

## Topics

### Getting dismiss behaviors

`static let automatic: MenuActionDismissBehavior`

Use the a dismissal behavior that’s appropriate for the given context.

`static let disabled: MenuActionDismissBehavior`

Never dismiss the presented menu after performing an action.

`static let enabled: MenuActionDismissBehavior`

Always dismiss the presented menu after performing an action.

## Relationships

### Conforms To

  * `Equatable`

## See Also

### Configuring menu dismissal

`func menuActionDismissBehavior(MenuActionDismissBehavior) -> some View`

Tells a menu whether to dismiss after performing an action.

Instance Method

# menuOrder(_:)

Sets the preferred order of items for menus presented from this view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func menuOrder(_ order: MenuOrder) -> some View
    

##  Parameters

`order`

    

The menu item ordering strategy to apply.

## Return Value

A view that uses the specified menu ordering strategy.

## Discussion

Use this modifier to override the default menu order. On supported platforms,
`priority` order keeps the first items closer to the user’s point of
interaction, whereas `fixed` order always orders items from top to bottom.

On iOS, the `automatic` order resolves to `fixed` for menus presented within
scrollable content. Pickers that use the `menu` style also default to `fixed`
order. In all other cases, menus default to `priority` order.

On macOS, tvOS and watchOS, the `automatic` order always resolves to `fixed`
order.

The following example creates a menu that presents its content in a fixed
order from top to bottom:

You can use this modifier on controls that present a menu. For example, the
code below creates a `Picker` using the `menu` style with a priority-based
order:

You can also use this modifier on context menus. The example below creates a
context menu that presents its content in a fixed order:

The modifier has no effect when applied to a subsection or submenu of a menu.

## See Also

### Setting a preferred order

`var menuOrder: MenuOrder`

The preferred order of items for menus presented from this view.

`struct MenuOrder`

The order in which a menu presents its content.

Instance Property

# menuOrder

The preferred order of items for menus presented from this view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var menuOrder: MenuOrder { get set }

## Discussion

Set this value for a view hierarchy by calling the `menuOrder(_:)` view
modifier.

## See Also

### Setting a preferred order

`func menuOrder(MenuOrder) -> some View`

Sets the preferred order of items for menus presented from this view.

`struct MenuOrder`

The order in which a menu presents its content.

Structure

# MenuOrder

The order in which a menu presents its content.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    struct MenuOrder

## Overview

You can configure the preferred menu order using the `menuOrder(_:)` view
modifier.

## Topics

### Getting menu orders

`static let automatic: MenuOrder`

The ordering of the menu chosen by the system for the current context.

`static let fixed: MenuOrder`

Order items from top to bottom.

`static let priority: MenuOrder`

Keep the first items closest to user’s interaction point.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Setting a preferred order

`func menuOrder(MenuOrder) -> some View`

Sets the preferred order of items for menus presented from this view.

`var menuOrder: MenuOrder`

The preferred order of items for menus presented from this view.

Structure

# MenuButton

A button that displays a menu containing a list of choices when pressed.

macOS 10.15–14.4  Deprecated

    
    
    struct MenuButton<Label, Content> where Label : View, Content : View

Deprecated

Use `Menu` instead.

## Topics

### Creating a menu button

`init(LocalizedStringKey, content: () -> Content)`

Creates a menu button with the specified localized title and content.

Available when `Label` is `Text` and `Content` conforms to `View`.

`init<S>(S, content: () -> Content)`

Creates a menu button with the specified title and content.

Available when `Label` is `Text` and `Content` conforms to `View`.

`init(label: Label, content: () -> Content)`

Creates a menu button with the specified label and content.

### Styling a menu button

`func menuButtonStyle<S>(S) -> some View`

Sets the style for menu buttons within this view.

`protocol MenuButtonStyle`

A custom specification for the appearance and interaction of a menu button.

## Relationships

### Conforms To

  * `View`

## See Also

### Deprecated types

`typealias PullDownButton`Deprecated

`struct ContextMenu`

A container for views that you present as menu items in a context menu.

Deprecated

Type Alias

# PullDownButton

macOS 10.15+

    
    
    typealias PullDownButton

Deprecated

Use `Menu` instead.

## See Also

### Deprecated types

`struct MenuButton`

A button that displays a menu containing a list of choices when pressed.

Deprecated

`struct ContextMenu`

A container for views that you present as menu items in a context menu.

Deprecated

Structure

# ContextMenu

A container for views that you present as menu items in a context menu.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  watchOS 6.0–7.0  Deprecated
visionOS 1.0+

    
    
    struct ContextMenu<MenuItems> where MenuItems : View

Deprecated

Use `contextMenu(menuItems:)` instead.

## Overview

A context menu view allows you to present a situationally specific menu that
enables taking actions relevant to the current task.

You can create a context menu by first defining a `ContextMenu` container with
the controls that represent the actions people can take, and then using the
`contextMenu(_:)` view modifier to apply the menu to a view.

The example below creates and applies a two item context menu container to a
`Text` view. The Boolean value `shouldShowMenu`, which defaults to true,
controls the availability of context menu:

## Topics

### Creating a context menu

`init(menuItems: () -> MenuItems)`

Creates a context menu.

## See Also

### Deprecated types

`struct MenuButton`

A button that displays a menu containing a list of choices when pressed.

Deprecated

`typealias PullDownButton`Deprecated

