# MenuStyleConfiguration

Structure

# MenuStyleConfiguration.Label

A type-erased label of a menu.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 17.0+  visionOS
1.0+

    
    
    struct Label

## Relationships

### Conforms To

  * `View`

## See Also

### Setting the label and content

`struct Content`

A type-erased content of a menu.

Structure

# MenuStyleConfiguration.Content

A type-erased content of a menu.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 17.0+  visionOS
1.0+

    
    
    struct Content

## Relationships

### Conforms To

  * `View`

## See Also

### Setting the label and content

`struct Label`

A type-erased label of a menu.



# Menus and commands

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



# Menu

Initializer

# init(content:label:)

Creates a menu with a custom label.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 17.0+  visionOS
1.0+

    
    
    init(
        @ViewBuilder content: () -> Content,
        @ViewBuilder label: () -> Label
    )

Available when `Label` conforms to `View` and `Content` conforms to `View`.

##  Parameters

`content`

    

A group of menu items.

`label`

    

A view describing the content of the menu.

## See Also

### Creating a menu from content

`init(LocalizedStringKey, content: () -> Content)`

Creates a menu that generates its label from a localized string key.

Available when `Label` conforms to `View` and `Content` conforms to `View`.

`init<S>(S, content: () -> Content)`

Creates a menu that generates its label from a string.

Available when `Label` conforms to `View` and `Content` conforms to `View`.

Initializer

# init(_:content:)

Creates a menu that generates its label from a localized string key.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 17.0+  visionOS
1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        @ViewBuilder content: () -> Content
    ) where Label == Text

Available when `Label` conforms to `View` and `Content` conforms to `View`.

##  Parameters

`titleKey`

    

The key for the link’s localized title, which describes the contents of the
menu.

`content`

    

A group of menu items.

## See Also

### Creating a menu from content

`init(content: () -> Content, label: () -> Label)`

Creates a menu with a custom label.

Available when `Label` conforms to `View` and `Content` conforms to `View`.

`init<S>(S, content: () -> Content)`

Creates a menu that generates its label from a string.

Available when `Label` conforms to `View` and `Content` conforms to `View`.

Initializer

# init(_:content:)

Creates a menu that generates its label from a string.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 17.0+  visionOS
1.0+

    
    
    init<S>(
        _ title: S,
        @ViewBuilder content: () -> Content
    ) where Label == Text, S : StringProtocol

Available when `Label` conforms to `View` and `Content` conforms to `View`.

##  Parameters

`title`

    

A string that describes the contents of the menu.

`content`

    

A group of menu items.

## Discussion

To create the label with a localized string key, use `init(_:content:)`
instead.

## See Also

### Creating a menu from content

`init(content: () -> Content, label: () -> Label)`

Creates a menu with a custom label.

Available when `Label` conforms to `View` and `Content` conforms to `View`.

`init(LocalizedStringKey, content: () -> Content)`

Creates a menu that generates its label from a localized string key.

Available when `Label` conforms to `View` and `Content` conforms to `View`.

Initializer

# init(content:label:primaryAction:)

Creates a menu with a custom primary action and custom label.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 17.0+  visionOS
1.0+

    
    
    init(
        @ViewBuilder content: () -> Content,
        @ViewBuilder label: () -> Label,
        primaryAction: @escaping () -> Void
    )

Available when `Label` conforms to `View` and `Content` conforms to `View`.

##  Parameters

`content`

    

A group of menu items.

`label`

    

A view describing the content of the menu.

`primaryAction`

    

The action to perform on primary interaction with the menu.

## See Also

### Creating a menu with a primary action

`init(LocalizedStringKey, content: () -> Content, primaryAction: () -> Void)`

Creates a menu with a custom primary action that generates its label from a
localized string key.

Available when `Label` conforms to `View` and `Content` conforms to `View`.

`init<S>(S, content: () -> Content, primaryAction: () -> Void)`

Creates a menu with a custom primary action that generates its label from a
string.

Available when `Label` conforms to `View` and `Content` conforms to `View`.

Initializer

# init(_:content:primaryAction:)

Creates a menu with a custom primary action that generates its label from a
localized string key.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 17.0+  visionOS
1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        @ViewBuilder content: () -> Content,
        primaryAction: @escaping () -> Void
    ) where Label == Text

Available when `Label` conforms to `View` and `Content` conforms to `View`.

##  Parameters

`titleKey`

    

The key for the link’s localized title, which describes the contents of the
menu.

`primaryAction`

    

The action to perform on primary interaction with the menu.

`content`

    

A group of menu items.

## See Also

### Creating a menu with a primary action

`init(content: () -> Content, label: () -> Label, primaryAction: () -> Void)`

Creates a menu with a custom primary action and custom label.

Available when `Label` conforms to `View` and `Content` conforms to `View`.

`init<S>(S, content: () -> Content, primaryAction: () -> Void)`

Creates a menu with a custom primary action that generates its label from a
string.

Available when `Label` conforms to `View` and `Content` conforms to `View`.

Initializer

# init(_:content:primaryAction:)

Creates a menu with a custom primary action that generates its label from a
string.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 17.0+  visionOS
1.0+

    
    
    init<S>(
        _ title: S,
        @ViewBuilder content: () -> Content,
        primaryAction: @escaping () -> Void
    ) where Label == Text, S : StringProtocol

Available when `Label` conforms to `View` and `Content` conforms to `View`.

##  Parameters

`title`

    

A string that describes the contents of the menu.

`primaryAction`

    

The action to perform on primary interaction with the menu.

`content`

    

A group of menu items.

## Discussion

To create the label with a localized string key, use
`Menu(_:primaryAction:content:)` instead.

## See Also

### Creating a menu with a primary action

`init(content: () -> Content, label: () -> Label, primaryAction: () -> Void)`

Creates a menu with a custom primary action and custom label.

Available when `Label` conforms to `View` and `Content` conforms to `View`.

`init(LocalizedStringKey, content: () -> Content, primaryAction: () -> Void)`

Creates a menu with a custom primary action that generates its label from a
localized string key.

Available when `Label` conforms to `View` and `Content` conforms to `View`.

Initializer

# init(_:image:content:)

Creates a menu that generates its label from a string and image resource.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    init<S>(
        _ title: S,
        image: ImageResource,
        @ViewBuilder content: () -> Content
    ) where S : StringProtocol

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

##  Parameters

`title`

    

A string that describes the contents of the menu.

`image`

    

The name of the image resource to lookup.

`content`

    

A group of menu items.

## Discussion

To create the label with a localized string key, use `init(_:content:)`
instead.

## See Also

### Creating a menu with an image label

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

Initializer

# init(_:image:content:)

Creates a menu that generates its label from a localized string key and image
resource.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        image: ImageResource,
        @ViewBuilder content: () -> Content
    )

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

##  Parameters

`titleKey`

    

The key for the link’s localized title, which describes the contents of the
menu.

`image`

    

The name of the image resource to lookup.

`content`

    

A group of menu items.

## See Also

### Creating a menu with an image label

`init<S>(S, image: ImageResource, content: () -> Content)`

Creates a menu that generates its label from a string and image resource.

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

Initializer

# init(_:image:content:primaryAction:)

Creates a menu with a custom primary action that generates its label from a
localized string key.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        image: ImageResource,
        @ViewBuilder content: () -> Content,
        primaryAction: @escaping () -> Void
    )

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

##  Parameters

`titleKey`

    

The key for the link’s localized title, which describes the contents of the
menu.

`image`

    

The name of the image resource to lookup.

`primaryAction`

    

The action to perform on primary interaction with the menu.

`content`

    

A group of menu items.

## See Also

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

Initializer

# init(_:systemImage:content:)

Creates a menu that generates its label from a string and system image.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 17.0+  visionOS
1.0+

    
    
    init<S>(
        _ title: S,
        systemImage: String,
        @ViewBuilder content: () -> Content
    ) where S : StringProtocol

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

##  Parameters

`title`

    

A string that describes the contents of the menu.

`systemImage`

    

The name of the image resource to lookup.

`content`

    

A group of menu items.

## Discussion

To create the label with a localized string key, use `init(_:content:)`
instead.

## See Also

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

Initializer

# init(_:systemImage:content:)

Creates a menu that generates its label from a localized string key and system
image.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 17.0+  visionOS
1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        systemImage: String,
        @ViewBuilder content: () -> Content
    )

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

##  Parameters

`titleKey`

    

The key for the link’s localized title, which describes the contents of the
menu.

`systemImage`

    

The name of the image resource to lookup.

`content`

    

A group of menu items.

## See Also

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

`init(LocalizedStringKey, systemImage: String, content: () -> Content,
primaryAction: () -> Void)`

Creates a menu with a custom primary action that generates its label from a
localized string key and system image.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

Initializer

# init(_:systemImage:content:primaryAction:)

Creates a menu with a custom primary action that generates its label from a
localized string key and system image.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 17.0+  visionOS
1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        systemImage: String,
        @ViewBuilder content: () -> Content,
        primaryAction: @escaping () -> Void
    )

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

##  Parameters

`titleKey`

    

The key for the link’s localized title, which describes the contents of the
menu.

`systemImage`

    

The name of the image resource to lookup.

`primaryAction`

    

The action to perform on primary interaction with the menu.

`content`

    

A group of menu items.

## See Also

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

Initializer

# init(_:)

Creates a menu based on a style configuration.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 17.0+  visionOS
1.0+

    
    
    init(_ configuration: MenuStyleConfiguration)

Available when `Label` is `MenuStyleConfiguration.Label` and `Content` is
`MenuStyleConfiguration.Content`.

## Discussion

Use this initializer within the `makeBody(configuration:)` method of a
`MenuStyle` instance to create an instance of the menu being styled. This is
useful for custom menu styles that modify the current menu style.

For example, the following code creates a new, custom style that adds a red
border around the current menu style:



# MultiDatePicker

Initializer

# init(_:selection:)

Creates an instance that selects multiple dates with an unbounded range.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        selection: Binding<Set<DateComponents>>
    )

Available when `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the localized title of `self`, describing its purpose.

`selection`

    

The date values being displayed and selected.

## See Also

### Picking dates

`init<S>(S, selection: Binding<Set<DateComponents>>)`

Creates an instance that selects multiple dates with an unbounded range.

Available when `Label` is `Text`.

`init(selection: Binding<Set<DateComponents>>, label: () -> Label)`

Creates an instance that selects multiple dates with an unbounded range.

Available when `Label` conforms to `View`.

Initializer

# init(_:selection:)

Creates an instance that selects multiple dates with an unbounded range.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        selection: Binding<Set<DateComponents>>
    ) where S : StringProtocol

Available when `Label` is `Text`.

##  Parameters

`title`

    

The title of `self`, describing its purpose.

`selection`

    

The date values being displayed and selected.

## See Also

### Picking dates

`init(LocalizedStringKey, selection: Binding<Set<DateComponents>>)`

Creates an instance that selects multiple dates with an unbounded range.

Available when `Label` is `Text`.

`init(selection: Binding<Set<DateComponents>>, label: () -> Label)`

Creates an instance that selects multiple dates with an unbounded range.

Available when `Label` conforms to `View`.

Initializer

# init(selection:label:)

Creates an instance that selects multiple dates with an unbounded range.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init(
        selection: Binding<Set<DateComponents>>,
        @ViewBuilder label: () -> Label
    )

Available when `Label` conforms to `View`.

##  Parameters

`selection`

    

The date values being displayed and selected.

`label`

    

A view that describes the use of the dates.

## See Also

### Picking dates

`init(LocalizedStringKey, selection: Binding<Set<DateComponents>>)`

Creates an instance that selects multiple dates with an unbounded range.

Available when `Label` is `Text`.

`init<S>(S, selection: Binding<Set<DateComponents>>)`

Creates an instance that selects multiple dates with an unbounded range.

Available when `Label` is `Text`.

Initializer

# init(_:selection:in:)

Creates an instance that selects multiple dates in a range.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        selection: Binding<Set<DateComponents>>,
        in bounds: Range<Date>
    )

Available when `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the localized title of `self`, describing its purpose.

`selection`

    

The date values being displayed and selected.

`bounds`

    

The exclusive range of selectable dates.

## See Also

### Picking dates in a range

`init<S>(S, selection: Binding<Set<DateComponents>>, in: Range<Date>)`

Creates an instance that selects multiple dates in a range.

Available when `Label` is `Text`.

`init(selection: Binding<Set<DateComponents>>, in: Range<Date>, label: () ->
Label)`

Creates an instance that selects multiple dates in a range.

Available when `Label` conforms to `View`.

Initializer

# init(_:selection:in:)

Creates an instance that selects multiple dates in a range.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        selection: Binding<Set<DateComponents>>,
        in bounds: Range<Date>
    ) where S : StringProtocol

Available when `Label` is `Text`.

##  Parameters

`title`

    

The title of `self`, describing its purpose.

`selection`

    

The date values being displayed and selected.

`bounds`

    

The exclusive range of selectable dates.

## See Also

### Picking dates in a range

`init(LocalizedStringKey, selection: Binding<Set<DateComponents>>, in:
Range<Date>)`

Creates an instance that selects multiple dates in a range.

Available when `Label` is `Text`.

`init(selection: Binding<Set<DateComponents>>, in: Range<Date>, label: () ->
Label)`

Creates an instance that selects multiple dates in a range.

Available when `Label` conforms to `View`.

Initializer

# init(selection:in:label:)

Creates an instance that selects multiple dates in a range.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init(
        selection: Binding<Set<DateComponents>>,
        in bounds: Range<Date>,
        @ViewBuilder label: () -> Label
    )

Available when `Label` conforms to `View`.

##  Parameters

`selection`

    

The date values being displayed and selected.

`bounds`

    

The exclusive range of selectable dates.

`label`

    

A view that describes the use of the dates.

## See Also

### Picking dates in a range

`init(LocalizedStringKey, selection: Binding<Set<DateComponents>>, in:
Range<Date>)`

Creates an instance that selects multiple dates in a range.

Available when `Label` is `Text`.

`init<S>(S, selection: Binding<Set<DateComponents>>, in: Range<Date>)`

Creates an instance that selects multiple dates in a range.

Available when `Label` is `Text`.

Initializer

# init(_:selection:in:)

Creates an instance that selects multiple dates on or after some start date.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        selection: Binding<Set<DateComponents>>,
        in bounds: PartialRangeFrom<Date>
    )

Available when `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the localized title of `self`, describing its purpose.

`selection`

    

The date values being displayed and selected.

`bounds`

    

The open range from some selectable start date.

## See Also

### Picking dates after a date

`init<S>(S, selection: Binding<Set<DateComponents>>, in:
PartialRangeFrom<Date>)`

Creates an instance that selects multiple dates on or after some start date.

Available when `Label` is `Text`.

`init(selection: Binding<Set<DateComponents>>, in: PartialRangeFrom<Date>,
label: () -> Label)`

Creates an instance that selects multiple dates on or after some start date.

Available when `Label` conforms to `View`.

Initializer

# init(_:selection:in:)

Creates an instance that selects multiple dates on or after some start date.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        selection: Binding<Set<DateComponents>>,
        in bounds: PartialRangeFrom<Date>
    ) where S : StringProtocol

Available when `Label` is `Text`.

##  Parameters

`title`

    

The title of `self`, describing its purpose.

`selection`

    

The date values being displayed and selected.

`bounds`

    

The open range from some selectable start date.

## See Also

### Picking dates after a date

`init(LocalizedStringKey, selection: Binding<Set<DateComponents>>, in:
PartialRangeFrom<Date>)`

Creates an instance that selects multiple dates on or after some start date.

Available when `Label` is `Text`.

`init(selection: Binding<Set<DateComponents>>, in: PartialRangeFrom<Date>,
label: () -> Label)`

Creates an instance that selects multiple dates on or after some start date.

Available when `Label` conforms to `View`.

Initializer

# init(selection:in:label:)

Creates an instance that selects multiple dates on or after some start date.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init(
        selection: Binding<Set<DateComponents>>,
        in bounds: PartialRangeFrom<Date>,
        @ViewBuilder label: () -> Label
    )

Available when `Label` conforms to `View`.

##  Parameters

`selection`

    

The date values being displayed and selected.

`bounds`

    

The open range from some selectable start date.

`label`

    

A view that describes the use of the dates.

## See Also

### Picking dates after a date

`init(LocalizedStringKey, selection: Binding<Set<DateComponents>>, in:
PartialRangeFrom<Date>)`

Creates an instance that selects multiple dates on or after some start date.

Available when `Label` is `Text`.

`init<S>(S, selection: Binding<Set<DateComponents>>, in:
PartialRangeFrom<Date>)`

Creates an instance that selects multiple dates on or after some start date.

Available when `Label` is `Text`.

Initializer

# init(_:selection:in:)

Creates an instance that selects multiple dates before some end date.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        selection: Binding<Set<DateComponents>>,
        in bounds: PartialRangeUpTo<Date>
    )

Available when `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the localized title of `self`, describing its purpose.

`selection`

    

The date values being displayed and selected.

`bounds`

    

The open range before some end date.

## See Also

### Picking dates before a date

`init<S>(S, selection: Binding<Set<DateComponents>>, in:
PartialRangeUpTo<Date>)`

Creates an instance that selects multiple dates before some end date.

Available when `Label` is `Text`.

`init(selection: Binding<Set<DateComponents>>, in: PartialRangeUpTo<Date>,
label: () -> Label)`

Creates an instance that selects multiple dates before some end date.

Available when `Label` conforms to `View`.

Initializer

# init(_:selection:in:)

Creates an instance that selects multiple dates before some end date.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        selection: Binding<Set<DateComponents>>,
        in bounds: PartialRangeUpTo<Date>
    ) where S : StringProtocol

Available when `Label` is `Text`.

##  Parameters

`title`

    

The title of `self`, describing its purpose.

`selection`

    

The date values being displayed and selected.

`bounds`

    

The open range before some end date.

## See Also

### Picking dates before a date

`init(LocalizedStringKey, selection: Binding<Set<DateComponents>>, in:
PartialRangeUpTo<Date>)`

Creates an instance that selects multiple dates before some end date.

Available when `Label` is `Text`.

`init(selection: Binding<Set<DateComponents>>, in: PartialRangeUpTo<Date>,
label: () -> Label)`

Creates an instance that selects multiple dates before some end date.

Available when `Label` conforms to `View`.

Initializer

# init(selection:in:label:)

Creates an instance that selects multiple dates before some end date.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init(
        selection: Binding<Set<DateComponents>>,
        in bounds: PartialRangeUpTo<Date>,
        @ViewBuilder label: () -> Label
    )

Available when `Label` conforms to `View`.

##  Parameters

`selection`

    

The date values being displayed and selected.

`bounds`

    

The open range before some end date.

`label`

    

A view that describes the use of the dates.

## See Also

### Picking dates before a date

`init(LocalizedStringKey, selection: Binding<Set<DateComponents>>, in:
PartialRangeUpTo<Date>)`

Creates an instance that selects multiple dates before some end date.

Available when `Label` is `Text`.

`init<S>(S, selection: Binding<Set<DateComponents>>, in:
PartialRangeUpTo<Date>)`

Creates an instance that selects multiple dates before some end date.

Available when `Label` is `Text`.



# ModifiedContent

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



# MenuActionDismissBehavior

Type Property

# automatic

Use the a dismissal behavior that’s appropriate for the given context.

iOS 16.4+  iPadOS 16.4+  macOS 13.3+  Mac Catalyst 16.4+  tvOS 16.4+  watchOS
9.4+  visionOS 1.0+

    
    
    static let automatic: MenuActionDismissBehavior

## Discussion

In most cases, the default behavior is `enabled`. There are some cases, like
`Stepper`, that use `disabled` by default.

## See Also

### Getting dismiss behaviors

`static let disabled: MenuActionDismissBehavior`

Never dismiss the presented menu after performing an action.

`static let enabled: MenuActionDismissBehavior`

Always dismiss the presented menu after performing an action.

Type Property

# disabled

Never dismiss the presented menu after performing an action.

iOS 16.4+  iPadOS 16.4+  Mac Catalyst 16.4+  tvOS 17.0+  visionOS 1.0+

    
    
    static let disabled: MenuActionDismissBehavior

## See Also

### Getting dismiss behaviors

`static let automatic: MenuActionDismissBehavior`

Use the a dismissal behavior that’s appropriate for the given context.

`static let enabled: MenuActionDismissBehavior`

Always dismiss the presented menu after performing an action.

Type Property

# enabled

Always dismiss the presented menu after performing an action.

iOS 16.4+  iPadOS 16.4+  macOS 13.3+  Mac Catalyst 16.4+  tvOS 16.4+  watchOS
9.4+  visionOS 1.0+

    
    
    static let enabled: MenuActionDismissBehavior

## See Also

### Getting dismiss behaviors

`static let automatic: MenuActionDismissBehavior`

Use the a dismissal behavior that’s appropriate for the given context.

`static let disabled: MenuActionDismissBehavior`

Never dismiss the presented menu after performing an action.



# MenuButtonStyle

Structure

# BorderlessButtonMenuButtonStyle

A menu button style which manifests as a borderless button with no visual
embelishments.

macOS 10.15–14.4  Deprecated

    
    
    struct BorderlessButtonMenuButtonStyle

Deprecated

Use `BorderlessButtonMenuStyle` instead.

## Topics

### Creating a borderless button menu button style

`init()`

## Relationships

### Conforms To

  * `MenuButtonStyle`

## See Also

### Supporting types

`struct BorderlessPullDownMenuButtonStyle`

A menu button style which manifests as a borderless pull-down button.

Deprecated

`struct DefaultMenuButtonStyle`

The default menu button style.

Deprecated

`struct PullDownMenuButtonStyle`

A menu button style which manifests as a pull-down button.

Deprecated

Structure

# BorderlessPullDownMenuButtonStyle

A menu button style which manifests as a borderless pull-down button.

macOS 10.15–14.4  Deprecated

    
    
    struct BorderlessPullDownMenuButtonStyle

Deprecated

Use `BorderlessButtonMenuStyle` instead.

## Topics

### Creating a borderless pull down menu button style

`init()`

## Relationships

### Conforms To

  * `MenuButtonStyle`

## See Also

### Supporting types

`struct BorderlessButtonMenuButtonStyle`

A menu button style which manifests as a borderless button with no visual
embelishments.

Deprecated

`struct DefaultMenuButtonStyle`

The default menu button style.

Deprecated

`struct PullDownMenuButtonStyle`

A menu button style which manifests as a pull-down button.

Deprecated

Structure

# DefaultMenuButtonStyle

The default menu button style.

macOS 10.15–14.4  Deprecated

    
    
    struct DefaultMenuButtonStyle

Deprecated

Use `DefaultMenuStyle` instead.

## Topics

### Creating a default menu button style

`init()`

## Relationships

### Conforms To

  * `MenuButtonStyle`

## See Also

### Supporting types

`struct BorderlessButtonMenuButtonStyle`

A menu button style which manifests as a borderless button with no visual
embelishments.

Deprecated

`struct BorderlessPullDownMenuButtonStyle`

A menu button style which manifests as a borderless pull-down button.

Deprecated

`struct PullDownMenuButtonStyle`

A menu button style which manifests as a pull-down button.

Deprecated

Structure

# PullDownMenuButtonStyle

A menu button style which manifests as a pull-down button.

macOS 10.15–14.4  Deprecated

    
    
    struct PullDownMenuButtonStyle

Deprecated

Use `BorderedButtonMenuStyle` instead.

## Topics

### Creating a pull down menu button style

`init()`

## Relationships

### Conforms To

  * `MenuButtonStyle`

## See Also

### Supporting types

`struct BorderlessButtonMenuButtonStyle`

A menu button style which manifests as a borderless button with no visual
embelishments.

Deprecated

`struct BorderlessPullDownMenuButtonStyle`

A menu button style which manifests as a borderless pull-down button.

Deprecated

`struct DefaultMenuButtonStyle`

The default menu button style.

Deprecated



# MatchedGeometryProperties

Type Property

# frame

Both the `position` and `size` properties.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    static let frame: MatchedGeometryProperties

## See Also

### Matching properties

`static let position: MatchedGeometryProperties`

The view’s position, in window coordinates.

`static let size: MatchedGeometryProperties`

The view’s size, in local coordinates.

Type Property

# position

The view’s position, in window coordinates.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    static let position: MatchedGeometryProperties

## See Also

### Matching properties

`static let frame: MatchedGeometryProperties`

Both the `position` and `size` properties.

`static let size: MatchedGeometryProperties`

The view’s size, in local coordinates.

Type Property

# size

The view’s size, in local coordinates.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    static let size: MatchedGeometryProperties

## See Also

### Matching properties

`static let frame: MatchedGeometryProperties`

Both the `position` and `size` properties.

`static let position: MatchedGeometryProperties`

The view’s position, in window coordinates.



# MenuButton

Initializer

# init(_:content:)

Creates a menu button with the specified localized title and content.

macOS 10.15–14.4  Deprecated

    
    
    init(
        _ titleKey: LocalizedStringKey,
        @ViewBuilder content: () -> Content
    )

Available when `Label` is `Text` and `Content` conforms to `View`.

Deprecated

Use `Menu` instead.

## See Also

### Creating a menu button

`init<S>(S, content: () -> Content)`

Creates a menu button with the specified title and content.

Available when `Label` is `Text` and `Content` conforms to `View`.

Deprecated

`init(label: Label, content: () -> Content)`

Creates a menu button with the specified label and content.

Deprecated

Initializer

# init(_:content:)

Creates a menu button with the specified title and content.

macOS 10.15–14.4  Deprecated

    
    
    init<S>(
        _ title: S,
        @ViewBuilder content: () -> Content
    ) where S : StringProtocol

Available when `Label` is `Text` and `Content` conforms to `View`.

Deprecated

Use `Menu` instead.

## See Also

### Creating a menu button

`init(LocalizedStringKey, content: () -> Content)`

Creates a menu button with the specified localized title and content.

Available when `Label` is `Text` and `Content` conforms to `View`.

Deprecated

`init(label: Label, content: () -> Content)`

Creates a menu button with the specified label and content.

Deprecated

Initializer

# init(label:content:)

Creates a menu button with the specified label and content.

macOS 10.15–14.4  Deprecated

    
    
    init(
        label: Label,
        @ViewBuilder content: () -> Content
    )

Deprecated

Use `Menu` instead.

## See Also

### Creating a menu button

`init(LocalizedStringKey, content: () -> Content)`

Creates a menu button with the specified localized title and content.

Available when `Label` is `Text` and `Content` conforms to `View`.

Deprecated

`init<S>(S, content: () -> Content)`

Creates a menu button with the specified title and content.

Available when `Label` is `Text` and `Content` conforms to `View`.

Deprecated

Instance Method

# menuButtonStyle(_:)

Sets the style for menu buttons within this view.

macOS 10.15–14.4  Deprecated

    
    
    func menuButtonStyle<S>(_ style: S) -> some View where S : MenuButtonStyle
    

Deprecated

Use `menuStyle(_:)` instead.

## See Also

### Styling a menu button

`protocol MenuButtonStyle`

A custom specification for the appearance and interaction of a menu button.

Deprecated

Protocol

# MenuButtonStyle

A custom specification for the appearance and interaction of a menu button.

macOS 10.15–14.4  Deprecated

    
    
    protocol MenuButtonStyle

Deprecated

Use `MenuStyle` instead.

## Topics

### Supporting types

`struct BorderlessButtonMenuButtonStyle`

A menu button style which manifests as a borderless button with no visual
embelishments.

`struct BorderlessPullDownMenuButtonStyle`

A menu button style which manifests as a borderless pull-down button.

`struct DefaultMenuButtonStyle`

The default menu button style.

`struct PullDownMenuButtonStyle`

A menu button style which manifests as a pull-down button.

## Relationships

### Conforming Types

  * `BorderlessButtonMenuButtonStyle`
  * `BorderlessPullDownMenuButtonStyle`
  * `DefaultMenuButtonStyle`
  * `PullDownMenuButtonStyle`

## See Also

### Styling a menu button

`func menuButtonStyle<S>(S) -> some View`

Sets the style for menu buttons within this view.

Deprecated



# Modal presentations

Instance Method

# sheet(isPresented:onDismiss:content:)

Presents a sheet when a binding to a Boolean value that you provide is true.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func sheet<Content>(
        isPresented: Binding<Bool>,
        onDismiss: (() -> Void)? = nil,
        @ViewBuilder content: @escaping () -> Content
    ) -> some View where Content : View
    

##  Parameters

`isPresented`

    

A binding to a Boolean value that determines whether to present the sheet that
you create in the modifier’s `content` closure.

`onDismiss`

    

The closure to execute when dismissing the sheet.

`content`

    

A closure that returns the content of the sheet.

## Discussion

Use this method when you want to present a modal view to the user when a
Boolean value you provide is true. The example below displays a modal view of
the mockup for a software license agreement when the user toggles the
`isShowingSheet` variable by clicking or tapping on the “Show License
Agreement” button:

In vertically compact environments, such as iPhone in landscape orientation, a
sheet presentation automatically adapts to appear as a full-screen cover. Use
the `presentationCompactAdaptation(_:)` or
`presentationCompactAdaptation(horizontal:vertical:)` modifier to override
this behavior.

## See Also

### Showing a sheet, cover, or popover

`func sheet<Item, Content>(item: Binding<Item?>, onDismiss: (() -> Void)?,
content: (Item) -> Content) -> some View`

Presents a sheet using the given item as a data source for the sheet’s
content.

`func fullScreenCover<Content>(isPresented: Binding<Bool>, onDismiss: (() ->
Void)?, content: () -> Content) -> some View`

Presents a modal view that covers as much of the screen as possible when
binding to a Boolean value you provide is true.

`func fullScreenCover<Item, Content>(item: Binding<Item?>, onDismiss: (() ->
Void)?, content: (Item) -> Content) -> some View`

Presents a modal view that covers as much of the screen as possible using the
binding you provide as a data source for the sheet’s content.

`func popover<Content>(isPresented: Binding<Bool>, attachmentAnchor:
PopoverAttachmentAnchor, arrowEdge: Edge, content: () -> Content) -> some
View`

Presents a popover when a given condition is true.

`func popover<Item, Content>(item: Binding<Item?>, attachmentAnchor:
PopoverAttachmentAnchor, arrowEdge: Edge, content: (Item) -> Content) -> some
View`

Presents a popover using the given item as a data source for the popover’s
content.

`enum PopoverAttachmentAnchor`

An attachment anchor for a popover.

Instance Method

# sheet(item:onDismiss:content:)

Presents a sheet using the given item as a data source for the sheet’s
content.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func sheet<Item, Content>(
        item: Binding<Item?>,
        onDismiss: (() -> Void)? = nil,
        @ViewBuilder content: @escaping (Item) -> Content
    ) -> some View where Item : Identifiable, Content : View
    

##  Parameters

`item`

    

A binding to an optional source of truth for the sheet. When `item` is
non-`nil`, the system passes the item’s content to the modifier’s closure. You
display this content in a sheet that you create that the system displays to
the user. If `item` changes, the system dismisses the sheet and replaces it
with a new one using the same process.

`onDismiss`

    

The closure to execute when dismissing the sheet.

`content`

    

A closure returning the content of the sheet.

## Discussion

Use this method when you need to present a modal view with content from a
custom data source. The example below shows a custom data source
`InventoryItem` that the `content` closure uses to populate the display the
action sheet shows to the user:

In vertically compact environments, such as iPhone in landscape orientation, a
sheet presentation automatically adapts to appear as a full-screen cover. Use
the `presentationCompactAdaptation(_:)` or
`presentationCompactAdaptation(horizontal:vertical:)` modifier to override
this behavior.

## See Also

### Showing a sheet, cover, or popover

`func sheet<Content>(isPresented: Binding<Bool>, onDismiss: (() -> Void)?,
content: () -> Content) -> some View`

Presents a sheet when a binding to a Boolean value that you provide is true.

`func fullScreenCover<Content>(isPresented: Binding<Bool>, onDismiss: (() ->
Void)?, content: () -> Content) -> some View`

Presents a modal view that covers as much of the screen as possible when
binding to a Boolean value you provide is true.

`func fullScreenCover<Item, Content>(item: Binding<Item?>, onDismiss: (() ->
Void)?, content: (Item) -> Content) -> some View`

Presents a modal view that covers as much of the screen as possible using the
binding you provide as a data source for the sheet’s content.

`func popover<Content>(isPresented: Binding<Bool>, attachmentAnchor:
PopoverAttachmentAnchor, arrowEdge: Edge, content: () -> Content) -> some
View`

Presents a popover when a given condition is true.

`func popover<Item, Content>(item: Binding<Item?>, attachmentAnchor:
PopoverAttachmentAnchor, arrowEdge: Edge, content: (Item) -> Content) -> some
View`

Presents a popover using the given item as a data source for the popover’s
content.

`enum PopoverAttachmentAnchor`

An attachment anchor for a popover.

Instance Method

# fullScreenCover(isPresented:onDismiss:content:)

Presents a modal view that covers as much of the screen as possible when
binding to a Boolean value you provide is true.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS 7.0+
visionOS 1.0+

    
    
    func fullScreenCover<Content>(
        isPresented: Binding<Bool>,
        onDismiss: (() -> Void)? = nil,
        @ViewBuilder content: @escaping () -> Content
    ) -> some View where Content : View
    

##  Parameters

`isPresented`

    

A binding to a Boolean value that determines whether to present the sheet.

`onDismiss`

    

The closure to execute when dismissing the modal view.

`content`

    

A closure that returns the content of the modal view.

## Discussion

Use this method to show a modal view that covers as much of the screen as
possible. The example below displays a custom view when the user toggles the
value of the `isPresenting` binding:

## See Also

### Showing a sheet, cover, or popover

`func sheet<Content>(isPresented: Binding<Bool>, onDismiss: (() -> Void)?,
content: () -> Content) -> some View`

Presents a sheet when a binding to a Boolean value that you provide is true.

`func sheet<Item, Content>(item: Binding<Item?>, onDismiss: (() -> Void)?,
content: (Item) -> Content) -> some View`

Presents a sheet using the given item as a data source for the sheet’s
content.

`func fullScreenCover<Item, Content>(item: Binding<Item?>, onDismiss: (() ->
Void)?, content: (Item) -> Content) -> some View`

Presents a modal view that covers as much of the screen as possible using the
binding you provide as a data source for the sheet’s content.

`func popover<Content>(isPresented: Binding<Bool>, attachmentAnchor:
PopoverAttachmentAnchor, arrowEdge: Edge, content: () -> Content) -> some
View`

Presents a popover when a given condition is true.

`func popover<Item, Content>(item: Binding<Item?>, attachmentAnchor:
PopoverAttachmentAnchor, arrowEdge: Edge, content: (Item) -> Content) -> some
View`

Presents a popover using the given item as a data source for the popover’s
content.

`enum PopoverAttachmentAnchor`

An attachment anchor for a popover.

Instance Method

# fullScreenCover(item:onDismiss:content:)

Presents a modal view that covers as much of the screen as possible using the
binding you provide as a data source for the sheet’s content.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS 7.0+
visionOS 1.0+

    
    
    func fullScreenCover<Item, Content>(
        item: Binding<Item?>,
        onDismiss: (() -> Void)? = nil,
        @ViewBuilder content: @escaping (Item) -> Content
    ) -> some View where Item : Identifiable, Content : View
    

##  Parameters

`item`

    

A binding to an optional source of truth for the sheet. When `item` is
non-`nil`, the system passes the contents to the modifier’s closure. You
display this content in a sheet that you create that the system displays to
the user. If `item` changes, the system dismisses the currently displayed
sheet and replaces it with a new one using the same process.

`onDismiss`

    

The closure to execute when dismissing the modal view.

`content`

    

A closure returning the content of the modal view.

## Discussion

Use this method to display a modal view that covers as much of the screen as
possible. In the example below a custom structure — `CoverData` — provides
data for the full-screen view to display in the `content` closure when the
user clicks or taps the “Present Full-Screen Cover With Data” button:

## See Also

### Showing a sheet, cover, or popover

`func sheet<Content>(isPresented: Binding<Bool>, onDismiss: (() -> Void)?,
content: () -> Content) -> some View`

Presents a sheet when a binding to a Boolean value that you provide is true.

`func sheet<Item, Content>(item: Binding<Item?>, onDismiss: (() -> Void)?,
content: (Item) -> Content) -> some View`

Presents a sheet using the given item as a data source for the sheet’s
content.

`func fullScreenCover<Content>(isPresented: Binding<Bool>, onDismiss: (() ->
Void)?, content: () -> Content) -> some View`

Presents a modal view that covers as much of the screen as possible when
binding to a Boolean value you provide is true.

`func popover<Content>(isPresented: Binding<Bool>, attachmentAnchor:
PopoverAttachmentAnchor, arrowEdge: Edge, content: () -> Content) -> some
View`

Presents a popover when a given condition is true.

`func popover<Item, Content>(item: Binding<Item?>, attachmentAnchor:
PopoverAttachmentAnchor, arrowEdge: Edge, content: (Item) -> Content) -> some
View`

Presents a popover using the given item as a data source for the popover’s
content.

`enum PopoverAttachmentAnchor`

An attachment anchor for a popover.

Instance Method

# popover(isPresented:attachmentAnchor:arrowEdge:content:)

Presents a popover when a given condition is true.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  visionOS 1.0+

    
    
    func popover<Content>(
        isPresented: Binding<Bool>,
        attachmentAnchor: PopoverAttachmentAnchor = .rect(.bounds),
        arrowEdge: Edge = .top,
        @ViewBuilder content: @escaping () -> Content
    ) -> some View where Content : View
    

##  Parameters

`isPresented`

    

A binding to a Boolean value that determines whether to present the popover
content that you return from the modifier’s `content` closure.

`attachmentAnchor`

    

The positioning anchor that defines the attachment point of the popover. The
default is `bounds`.

`arrowEdge`

    

The edge of the `attachmentAnchor` that defines the location of the popover’s
arrow in macOS. The default is `Edge.top`. iOS ignores this parameter.

`content`

    

A closure returning the content of the popover.

## Discussion

Use this method to show a popover whose contents are a SwiftUI view that you
provide when a bound Boolean variable is `true`. In the example below, a
popover displays whenever the user toggles the `isShowingPopover` state
variable by pressing the “Show Popover” button:

## See Also

### Showing a sheet, cover, or popover

`func sheet<Content>(isPresented: Binding<Bool>, onDismiss: (() -> Void)?,
content: () -> Content) -> some View`

Presents a sheet when a binding to a Boolean value that you provide is true.

`func sheet<Item, Content>(item: Binding<Item?>, onDismiss: (() -> Void)?,
content: (Item) -> Content) -> some View`

Presents a sheet using the given item as a data source for the sheet’s
content.

`func fullScreenCover<Content>(isPresented: Binding<Bool>, onDismiss: (() ->
Void)?, content: () -> Content) -> some View`

Presents a modal view that covers as much of the screen as possible when
binding to a Boolean value you provide is true.

`func fullScreenCover<Item, Content>(item: Binding<Item?>, onDismiss: (() ->
Void)?, content: (Item) -> Content) -> some View`

Presents a modal view that covers as much of the screen as possible using the
binding you provide as a data source for the sheet’s content.

`func popover<Item, Content>(item: Binding<Item?>, attachmentAnchor:
PopoverAttachmentAnchor, arrowEdge: Edge, content: (Item) -> Content) -> some
View`

Presents a popover using the given item as a data source for the popover’s
content.

`enum PopoverAttachmentAnchor`

An attachment anchor for a popover.

Instance Method

# popover(item:attachmentAnchor:arrowEdge:content:)

Presents a popover using the given item as a data source for the popover’s
content.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  visionOS 1.0+

    
    
    func popover<Item, Content>(
        item: Binding<Item?>,
        attachmentAnchor: PopoverAttachmentAnchor = .rect(.bounds),
        arrowEdge: Edge = .top,
        @ViewBuilder content: @escaping (Item) -> Content
    ) -> some View where Item : Identifiable, Content : View
    

##  Parameters

`item`

    

A binding to an optional source of truth for the popover. When `item` is
non-`nil`, the system passes the contents to the modifier’s closure. You use
this content to populate the fields of a popover that you create that the
system displays to the user. If `item` changes, the system dismisses the
currently presented popover and replaces it with a new popover using the same
process.

`attachmentAnchor`

    

The positioning anchor that defines the attachment point of the popover. The
default is `bounds`.

`arrowEdge`

    

The edge of the `attachmentAnchor` that defines the location of the popover’s
arrow in macOS. The default is `Edge.top`. iOS ignores this parameter.

`content`

    

A closure returning the content of the popover.

## Discussion

Use this method when you need to present a popover with content from a custom
data source. The example below uses data in the `PopoverModel` structure to
populate the view in the `content` closure that the popover displays to the
user:

## See Also

### Showing a sheet, cover, or popover

`func sheet<Content>(isPresented: Binding<Bool>, onDismiss: (() -> Void)?,
content: () -> Content) -> some View`

Presents a sheet when a binding to a Boolean value that you provide is true.

`func sheet<Item, Content>(item: Binding<Item?>, onDismiss: (() -> Void)?,
content: (Item) -> Content) -> some View`

Presents a sheet using the given item as a data source for the sheet’s
content.

`func fullScreenCover<Content>(isPresented: Binding<Bool>, onDismiss: (() ->
Void)?, content: () -> Content) -> some View`

Presents a modal view that covers as much of the screen as possible when
binding to a Boolean value you provide is true.

`func fullScreenCover<Item, Content>(item: Binding<Item?>, onDismiss: (() ->
Void)?, content: (Item) -> Content) -> some View`

Presents a modal view that covers as much of the screen as possible using the
binding you provide as a data source for the sheet’s content.

`func popover<Content>(isPresented: Binding<Bool>, attachmentAnchor:
PopoverAttachmentAnchor, arrowEdge: Edge, content: () -> Content) -> some
View`

Presents a popover when a given condition is true.

`enum PopoverAttachmentAnchor`

An attachment anchor for a popover.

Enumeration

# PopoverAttachmentAnchor

An attachment anchor for a popover.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    enum PopoverAttachmentAnchor

## Topics

### Getting attachment anchors

`case point(UnitPoint)`

The anchor point for the popover expressed as a unit point that describes
possible alignments relative to a SwiftUI view.

`case rect(Anchor<CGRect>.Source)`

The anchor point for the popover relative to the source’s frame.

## See Also

### Showing a sheet, cover, or popover

`func sheet<Content>(isPresented: Binding<Bool>, onDismiss: (() -> Void)?,
content: () -> Content) -> some View`

Presents a sheet when a binding to a Boolean value that you provide is true.

`func sheet<Item, Content>(item: Binding<Item?>, onDismiss: (() -> Void)?,
content: (Item) -> Content) -> some View`

Presents a sheet using the given item as a data source for the sheet’s
content.

`func fullScreenCover<Content>(isPresented: Binding<Bool>, onDismiss: (() ->
Void)?, content: () -> Content) -> some View`

Presents a modal view that covers as much of the screen as possible when
binding to a Boolean value you provide is true.

`func fullScreenCover<Item, Content>(item: Binding<Item?>, onDismiss: (() ->
Void)?, content: (Item) -> Content) -> some View`

Presents a modal view that covers as much of the screen as possible using the
binding you provide as a data source for the sheet’s content.

`func popover<Content>(isPresented: Binding<Bool>, attachmentAnchor:
PopoverAttachmentAnchor, arrowEdge: Edge, content: () -> Content) -> some
View`

Presents a popover when a given condition is true.

`func popover<Item, Content>(item: Binding<Item?>, attachmentAnchor:
PopoverAttachmentAnchor, arrowEdge: Edge, content: (Item) -> Content) -> some
View`

Presents a popover using the given item as a data source for the popover’s
content.

Instance Method

# presentationCompactAdaptation(horizontal:vertical:)

Specifies how to adapt a presentation to horizontally and vertically compact
size classes.

iOS 16.4+  iPadOS 16.4+  macOS 13.3+  Mac Catalyst 16.4+  tvOS 16.4+  watchOS
9.4+  visionOS 1.0+

    
    
    func presentationCompactAdaptation(
        horizontal horizontalAdaptation: PresentationAdaptation,
        vertical verticalAdaptation: PresentationAdaptation
    ) -> some View
    

##  Parameters

`horizontalAdaptation`

    

The adaptation to use in a horizontally compact size class.

`verticalAdaptation`

    

The adaptation to use in a vertically compact size class. In a size class that
is both horizontally and vertically compact, SwiftUI uses the
`verticalAdaptation` value.

## Discussion

Some presentations adapt their appearance depending on the context. For
example, a popover presentation over a horizontally-compact view uses a sheet
appearance by default. Use this modifier to indicate a custom adaptation
preference.

If you want to specify the same adaptation for both dimensions, use the
`presentationCompactAdaptation(_:)` method instead.

## See Also

### Adapting a presentation to size classes

`func presentationCompactAdaptation(PresentationAdaptation) -> some View`

Specifies how to adapt a presentation to compact size classes.

`struct PresentationAdaptation`

Strategies for adapting a presentation to a different size class.

Instance Method

# presentationCompactAdaptation(_:)

Specifies how to adapt a presentation to compact size classes.

iOS 16.4+  iPadOS 16.4+  macOS 13.3+  Mac Catalyst 16.4+  tvOS 16.4+  watchOS
9.4+  visionOS 1.0+

    
    
    func presentationCompactAdaptation(_ adaptation: PresentationAdaptation) -> some View
    

##  Parameters

`adaptation`

    

The adaptation to use in either a horizontally or vertically compact size
class.

## Discussion

Some presentations adapt their appearance depending on the context. For
example, a sheet presentation over a vertically-compact view uses a full-
screen-cover appearance by default. Use this modifier to indicate a custom
adaptation preference. For example, the following code uses a presentation
adaptation value of `none` to request that the system not adapt the sheet in
compact size classes:

If you want to specify different adaptations for each dimension, use the
`presentationCompactAdaptation(horizontal:vertical:)` method instead.

## See Also

### Adapting a presentation to size classes

`func presentationCompactAdaptation(horizontal: PresentationAdaptation,
vertical: PresentationAdaptation) -> some View`

Specifies how to adapt a presentation to horizontally and vertically compact
size classes.

`struct PresentationAdaptation`

Strategies for adapting a presentation to a different size class.

Structure

# PresentationAdaptation

Strategies for adapting a presentation to a different size class.

iOS 16.4+  iPadOS 16.4+  macOS 13.3+  Mac Catalyst 16.4+  tvOS 16.4+  watchOS
9.4+  visionOS 1.0+

    
    
    struct PresentationAdaptation

## Overview

Use values of this type with the `presentationCompactAdaptation(_:)` and
`presentationCompactAdaptation(horizontal:vertical:)` modifiers.

## Topics

### Getting adaptation strategies

`static var automatic: PresentationAdaptation`

Use the default presentation adaptation.

`static var none: PresentationAdaptation`

Don’t adapt for the size class, if possible.

`static var fullScreenCover: PresentationAdaptation`

Prefer a full-screen-cover appearance when adapting for size classes.

`static var popover: PresentationAdaptation`

Prefer a popover appearance when adapting for size classes.

`static var sheet: PresentationAdaptation`

Prefer a sheet appearance when adapting for size classes.

## Relationships

### Conforms To

  * `Sendable`

## See Also

### Adapting a presentation to size classes

`func presentationCompactAdaptation(horizontal: PresentationAdaptation,
vertical: PresentationAdaptation) -> some View`

Specifies how to adapt a presentation to horizontally and vertically compact
size classes.

`func presentationCompactAdaptation(PresentationAdaptation) -> some View`

Specifies how to adapt a presentation to compact size classes.

Instance Method

# presentationDetents(_:)

Sets the available detents for the enclosing sheet.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func presentationDetents(_ detents: Set<PresentationDetent>) -> some View
    

##  Parameters

`detents`

    

A set of supported detents for the sheet. If you provide more that one detent,
people can drag the sheet to resize it.

## Discussion

By default, sheets support the `large` detent.

## See Also

### Configuring a sheet’s height

`func presentationDetents(Set<PresentationDetent>, selection:
Binding<PresentationDetent>) -> some View`

Sets the available detents for the enclosing sheet, giving you programmatic
control of the currently selected detent.

`func presentationContentInteraction(PresentationContentInteraction) -> some
View`

Configures the behavior of swipe gestures on a presentation.

`func presentationDragIndicator(Visibility) -> some View`

Sets the visibility of the drag indicator on top of a sheet.

`struct PresentationDetent`

A type that represents a height where a sheet naturally rests.

`protocol CustomPresentationDetent`

The definition of a custom detent with a calculated height.

`struct PresentationContentInteraction`

A behavior that you can use to influence how a presentation responds to swipe
gestures.

Instance Method

# presentationDetents(_:selection:)

Sets the available detents for the enclosing sheet, giving you programmatic
control of the currently selected detent.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func presentationDetents(
        _ detents: Set<PresentationDetent>,
        selection: Binding<PresentationDetent>
    ) -> some View
    

##  Parameters

`detents`

    

A set of supported detents for the sheet. If you provide more that one detent,
people can drag the sheet to resize it.

`selection`

    

A `Binding` to the currently selected detent. Ensure that the value matches
one of the detents that you provide for the `detents` parameter.

## Discussion

By default, sheets support the `large` detent.

## See Also

### Configuring a sheet’s height

`func presentationDetents(Set<PresentationDetent>) -> some View`

Sets the available detents for the enclosing sheet.

`func presentationContentInteraction(PresentationContentInteraction) -> some
View`

Configures the behavior of swipe gestures on a presentation.

`func presentationDragIndicator(Visibility) -> some View`

Sets the visibility of the drag indicator on top of a sheet.

`struct PresentationDetent`

A type that represents a height where a sheet naturally rests.

`protocol CustomPresentationDetent`

The definition of a custom detent with a calculated height.

`struct PresentationContentInteraction`

A behavior that you can use to influence how a presentation responds to swipe
gestures.

Instance Method

# presentationContentInteraction(_:)

Configures the behavior of swipe gestures on a presentation.

iOS 16.4+  iPadOS 16.4+  macOS 13.3+  Mac Catalyst 16.4+  tvOS 16.4+  watchOS
9.4+  visionOS 1.0+

    
    
    func presentationContentInteraction(_ behavior: PresentationContentInteraction) -> some View
    

##  Parameters

`behavior`

    

The requested behavior.

## Discussion

By default, when a person swipes up on a scroll view in a resizable
presentation, the presentation grows to the next detent. A scroll view
embedded in the presentation only scrolls after the presentation reaches its
largest size. Use this modifier to control which action takes precedence.

For example, you can request that swipe gestures scroll content first,
resizing the sheet only after hitting the end of the scroll view, by passing
the `scrolls` value to this modifier:

People can always resize your presentation using the drag indicator.

## See Also

### Configuring a sheet’s height

`func presentationDetents(Set<PresentationDetent>) -> some View`

Sets the available detents for the enclosing sheet.

`func presentationDetents(Set<PresentationDetent>, selection:
Binding<PresentationDetent>) -> some View`

Sets the available detents for the enclosing sheet, giving you programmatic
control of the currently selected detent.

`func presentationDragIndicator(Visibility) -> some View`

Sets the visibility of the drag indicator on top of a sheet.

`struct PresentationDetent`

A type that represents a height where a sheet naturally rests.

`protocol CustomPresentationDetent`

The definition of a custom detent with a calculated height.

`struct PresentationContentInteraction`

A behavior that you can use to influence how a presentation responds to swipe
gestures.

Instance Method

# presentationDragIndicator(_:)

Sets the visibility of the drag indicator on top of a sheet.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func presentationDragIndicator(_ visibility: Visibility) -> some View
    

##  Parameters

`visibility`

    

The preferred visibility of the drag indicator.

## Discussion

You can show a drag indicator when it isn’t apparent that a sheet can resize
or when the sheet can’t dismiss interactively.

## See Also

### Configuring a sheet’s height

`func presentationDetents(Set<PresentationDetent>) -> some View`

Sets the available detents for the enclosing sheet.

`func presentationDetents(Set<PresentationDetent>, selection:
Binding<PresentationDetent>) -> some View`

Sets the available detents for the enclosing sheet, giving you programmatic
control of the currently selected detent.

`func presentationContentInteraction(PresentationContentInteraction) -> some
View`

Configures the behavior of swipe gestures on a presentation.

`struct PresentationDetent`

A type that represents a height where a sheet naturally rests.

`protocol CustomPresentationDetent`

The definition of a custom detent with a calculated height.

`struct PresentationContentInteraction`

A behavior that you can use to influence how a presentation responds to swipe
gestures.

Structure

# PresentationDetent

A type that represents a height where a sheet naturally rests.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    struct PresentationDetent

## Topics

### Getting built-in detents

`static let large: PresentationDetent`

The system detent for a sheet at full height.

`static let medium: PresentationDetent`

The system detent for a sheet that’s approximately half the height of the
screen, and is inactive in compact height.

### Creating custom detents

`static func custom<D>(D.Type) -> PresentationDetent`

A custom detent with a calculated height.

`static func fraction(CGFloat) -> PresentationDetent`

A custom detent with the specified fractional height.

`static func height(CGFloat) -> PresentationDetent`

A custom detent with the specified height.

`struct Context`

Information that you use to calculate the presentation’s height.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Configuring a sheet’s height

`func presentationDetents(Set<PresentationDetent>) -> some View`

Sets the available detents for the enclosing sheet.

`func presentationDetents(Set<PresentationDetent>, selection:
Binding<PresentationDetent>) -> some View`

Sets the available detents for the enclosing sheet, giving you programmatic
control of the currently selected detent.

`func presentationContentInteraction(PresentationContentInteraction) -> some
View`

Configures the behavior of swipe gestures on a presentation.

`func presentationDragIndicator(Visibility) -> some View`

Sets the visibility of the drag indicator on top of a sheet.

`protocol CustomPresentationDetent`

The definition of a custom detent with a calculated height.

`struct PresentationContentInteraction`

A behavior that you can use to influence how a presentation responds to swipe
gestures.

Protocol

# CustomPresentationDetent

The definition of a custom detent with a calculated height.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    protocol CustomPresentationDetent

## Overview

You can create and use a custom detent with built-in detents.

## Topics

### Getting the height

`static func height(in: Self.Context) -> CGFloat?`

Calculates and returns a height based on the context.

**Required**

` typealias Context`

Information that you can use to calculate the height of a custom detent.

## See Also

### Configuring a sheet’s height

`func presentationDetents(Set<PresentationDetent>) -> some View`

Sets the available detents for the enclosing sheet.

`func presentationDetents(Set<PresentationDetent>, selection:
Binding<PresentationDetent>) -> some View`

Sets the available detents for the enclosing sheet, giving you programmatic
control of the currently selected detent.

`func presentationContentInteraction(PresentationContentInteraction) -> some
View`

Configures the behavior of swipe gestures on a presentation.

`func presentationDragIndicator(Visibility) -> some View`

Sets the visibility of the drag indicator on top of a sheet.

`struct PresentationDetent`

A type that represents a height where a sheet naturally rests.

`struct PresentationContentInteraction`

A behavior that you can use to influence how a presentation responds to swipe
gestures.

Instance Method

# presentationCornerRadius(_:)

Requests that the presentation have a specific corner radius.

iOS 16.4+  iPadOS 16.4+  macOS 13.3+  Mac Catalyst 16.4+  tvOS 16.4+  watchOS
9.4+  visionOS 1.0+

    
    
    func presentationCornerRadius(_ cornerRadius: CGFloat?) -> some View
    

##  Parameters

`cornerRadius`

    

The corner radius, or `nil` to use the system default.

## Discussion

Use this modifier to change the corner radius of a presentation.

## See Also

### Styling a sheet and its background

`func presentationBackground<S>(S) -> some View`

Sets the presentation background of the enclosing sheet using a shape style.

`func presentationBackground<V>(alignment: Alignment, content: () -> V) ->
some View`

Sets the presentation background of the enclosing sheet to a custom view.

`func presentationBackgroundInteraction(PresentationBackgroundInteraction) ->
some View`

Controls whether people can interact with the view behind a presentation.

`struct PresentationBackgroundInteraction`

The kinds of interaction available to views behind a presentation.

Instance Method

# presentationBackground(_:)

Sets the presentation background of the enclosing sheet using a shape style.

iOS 16.4+  iPadOS 16.4+  macOS 13.3+  Mac Catalyst 16.4+  tvOS 16.4+  watchOS
9.4+  visionOS 1.0+

    
    
    func presentationBackground<S>(_ style: S) -> some View where S : ShapeStyle
    

##  Parameters

`style`

    

The shape style to use as the presentation background.

## Discussion

The following example uses the `thick` material as the sheet background:

The `presentationBackground(_:)` modifier differs from the
`background(_:ignoresSafeAreaEdges:)` modifier in several key ways. A
presentation background:

  * Automatically fills the entire presentation.

  * Allows views behind the presentation to show through translucent styles.

## See Also

### Styling a sheet and its background

`func presentationCornerRadius(CGFloat?) -> some View`

Requests that the presentation have a specific corner radius.

`func presentationBackground<V>(alignment: Alignment, content: () -> V) ->
some View`

Sets the presentation background of the enclosing sheet to a custom view.

`func presentationBackgroundInteraction(PresentationBackgroundInteraction) ->
some View`

Controls whether people can interact with the view behind a presentation.

`struct PresentationBackgroundInteraction`

The kinds of interaction available to views behind a presentation.

Instance Method

# presentationBackground(alignment:content:)

Sets the presentation background of the enclosing sheet to a custom view.

iOS 16.4+  iPadOS 16.4+  macOS 13.3+  Mac Catalyst 16.4+  tvOS 16.4+  watchOS
9.4+  visionOS 1.0+

    
    
    func presentationBackground<V>(
        alignment: Alignment = .center,
        @ViewBuilder content: () -> V
    ) -> some View where V : View
    

##  Parameters

`alignment`

    

The alignment that the modifier uses to position the implicit `ZStack` that
groups the background views. The default is `center`.

`content`

    

The view to use as the background of the presentation.

## Discussion

The following example uses a yellow view as the sheet background:

The `presentationBackground(alignment:content:)` modifier differs from the
`background(alignment:content:)` modifier in several key ways. A presentation
background:

  * Automatically fills the entire presentation.

  * Allows views behind the presentation to show through translucent areas of the `content`.

## See Also

### Styling a sheet and its background

`func presentationCornerRadius(CGFloat?) -> some View`

Requests that the presentation have a specific corner radius.

`func presentationBackground<S>(S) -> some View`

Sets the presentation background of the enclosing sheet using a shape style.

`func presentationBackgroundInteraction(PresentationBackgroundInteraction) ->
some View`

Controls whether people can interact with the view behind a presentation.

`struct PresentationBackgroundInteraction`

The kinds of interaction available to views behind a presentation.

Instance Method

# presentationBackgroundInteraction(_:)

Controls whether people can interact with the view behind a presentation.

iOS 16.4+  iPadOS 16.4+  macOS 13.3+  Mac Catalyst 16.4+  tvOS 16.4+  watchOS
9.4+  visionOS 1.0+

    
    
    func presentationBackgroundInteraction(_ interaction: PresentationBackgroundInteraction) -> some View
    

##  Parameters

`interaction`

    

A specification of how people can interact with the view behind a
presentation.

## Discussion

On many platforms, SwiftUI automatically disables the view behind a sheet that
you present, so that people can’t interact with the backing view until they
dismiss the sheet. Use this modifier if you want to enable interaction.

The following example enables people to interact with the view behind the
sheet when the sheet is at the smallest detent, but not at the other detents:

## See Also

### Styling a sheet and its background

`func presentationCornerRadius(CGFloat?) -> some View`

Requests that the presentation have a specific corner radius.

`func presentationBackground<S>(S) -> some View`

Sets the presentation background of the enclosing sheet using a shape style.

`func presentationBackground<V>(alignment: Alignment, content: () -> V) ->
some View`

Sets the presentation background of the enclosing sheet to a custom view.

`struct PresentationBackgroundInteraction`

The kinds of interaction available to views behind a presentation.

Structure

# PresentationBackgroundInteraction

The kinds of interaction available to views behind a presentation.

iOS 16.4+  iPadOS 16.4+  macOS 13.3+  Mac Catalyst 16.4+  tvOS 16.4+  watchOS
9.4+  visionOS 1.0+

    
    
    struct PresentationBackgroundInteraction

## Overview

Use values of this type with the `presentationBackgroundInteraction(_:)`
modifier.

## Topics

### Getting interaction types

`static var automatic: PresentationBackgroundInteraction`

The default background interaction for the presentation.

`static var disabled: PresentationBackgroundInteraction`

People can’t interact with the view behind a presentation.

`static var enabled: PresentationBackgroundInteraction`

People can interact with the view behind a presentation.

`static func enabled(upThrough: PresentationDetent) ->
PresentationBackgroundInteraction`

People can interact with the view behind a presentation up through a specified
detent.

## Relationships

### Conforms To

  * `Sendable`

## See Also

### Styling a sheet and its background

`func presentationCornerRadius(CGFloat?) -> some View`

Requests that the presentation have a specific corner radius.

`func presentationBackground<S>(S) -> some View`

Sets the presentation background of the enclosing sheet using a shape style.

`func presentationBackground<V>(alignment: Alignment, content: () -> V) ->
some View`

Sets the presentation background of the enclosing sheet to a custom view.

`func presentationBackgroundInteraction(PresentationBackgroundInteraction) ->
some View`

Controls whether people can interact with the view behind a presentation.

Instance Method

# alert(_:isPresented:actions:)

Presents an alert when a given condition is true, using a string variable as a
title.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func alert<S, A>(
        _ title: S,
        isPresented: Binding<Bool>,
        @ViewBuilder actions: () -> A
    ) -> some View where S : StringProtocol, A : View
    

##  Parameters

`title`

    

A text string used as the title of the alert.

`isPresented`

    

A binding to a Boolean value that determines whether to present the alert.
When the user presses or taps one of the alert’s actions, the system sets this
value to `false` and dismisses.

`actions`

    

A `ViewBuilder` returning the alert’s actions.

## Discussion

In the example below, a login form conditionally presents an alert by setting
the `didFail` state variable. When the form sets the value to to `true`, the
system displays an alert with an “OK” action.

All actions in an alert dismiss the alert after the action runs. The default
button is shown with greater prominence. You can influence the default button
by assigning it the `defaultAction` keyboard shortcut.

The system may reorder the buttons based on their role and prominence.

If no actions are present, the system includes a standard “OK” action. No
default cancel action is provided. If you want to show a cancel action, use a
button with a role of `cancel`.

On iOS, tvOS, and watchOS, alerts only support controls with labels that are
`Text`. Passing any other type of view results in the content being omitted.

## See Also

### Presenting an alert

`func alert<A>(Text, isPresented: Binding<Bool>, actions: () -> A) -> some
View`

Presents an alert when a given condition is true, using a text view for the
title.

`func alert<A>(LocalizedStringKey, isPresented: Binding<Bool>, actions: () ->
A) -> some View`

Presents an alert when a given condition is true, using a localized string key
for the title.

`func alert<A, T>(Text, isPresented: Binding<Bool>, presenting: T?, actions:
(T) -> A) -> some View`

Presents an alert using the given data to produce the alert’s content and a
text view as a title.

`func alert<A, T>(LocalizedStringKey, isPresented: Binding<Bool>, presenting:
T?, actions: (T) -> A) -> some View`

Presents an alert using the given data to produce the alert’s content and a
localized string key for a title.

`func alert<S, A, T>(S, isPresented: Binding<Bool>, presenting: T?, actions:
(T) -> A) -> some View`

Presents an alert using the given data to produce the alert’s content and a
string variable as a title.

`func alert<E, A>(isPresented: Binding<Bool>, error: E?, actions: () -> A) ->
some View`

Presents an alert when an error is present.

Instance Method

# alert(_:isPresented:actions:)

Presents an alert when a given condition is true, using a text view for the
title.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func alert<A>(
        _ title: Text,
        isPresented: Binding<Bool>,
        @ViewBuilder actions: () -> A
    ) -> some View where A : View
    

##  Parameters

`title`

    

The title of the alert.

`isPresented`

    

A binding to a Boolean value that determines whether to present the alert.
When the user presses or taps one of the alert’s actions, the system sets this
value to `false` and dismisses.

`actions`

    

A `ViewBuilder` returning the alert’s actions.

## Discussion

In the example below, a login form conditionally presents an alert by setting
the `didFail` state variable. When the form sets the value to to `true`, the
system displays an alert with an “OK” action.

All actions in an alert dismiss the alert after the action runs. The default
button is shown with greater prominence. You can influence the default button
by assigning it the `defaultAction` keyboard shortcut.

The system may reorder the buttons based on their role and prominence.

If no actions are present, the system includes a standard “OK” action. No
default cancel action is provided. If you want to show a cancel action, use a
button with a role of `cancel`.

On iOS, tvOS, and watchOS, alerts only support controls with labels that are
`Text`. Passing any other type of view results in the content being omitted.

## See Also

### Presenting an alert

`func alert<S, A>(S, isPresented: Binding<Bool>, actions: () -> A) -> some
View`

Presents an alert when a given condition is true, using a string variable as a
title.

`func alert<A>(LocalizedStringKey, isPresented: Binding<Bool>, actions: () ->
A) -> some View`

Presents an alert when a given condition is true, using a localized string key
for the title.

`func alert<A, T>(Text, isPresented: Binding<Bool>, presenting: T?, actions:
(T) -> A) -> some View`

Presents an alert using the given data to produce the alert’s content and a
text view as a title.

`func alert<A, T>(LocalizedStringKey, isPresented: Binding<Bool>, presenting:
T?, actions: (T) -> A) -> some View`

Presents an alert using the given data to produce the alert’s content and a
localized string key for a title.

`func alert<S, A, T>(S, isPresented: Binding<Bool>, presenting: T?, actions:
(T) -> A) -> some View`

Presents an alert using the given data to produce the alert’s content and a
string variable as a title.

`func alert<E, A>(isPresented: Binding<Bool>, error: E?, actions: () -> A) ->
some View`

Presents an alert when an error is present.

Instance Method

# alert(_:isPresented:actions:)

Presents an alert when a given condition is true, using a localized string key
for the title.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func alert<A>(
        _ titleKey: LocalizedStringKey,
        isPresented: Binding<Bool>,
        @ViewBuilder actions: () -> A
    ) -> some View where A : View
    

##  Parameters

`titleKey`

    

The key for the localized string that describes the title of the alert.

`isPresented`

    

A binding to a Boolean value that determines whether to present the alert.
When the user presses or taps one of the alert’s actions, the system sets this
value to `false` and dismisses.

`actions`

    

A `ViewBuilder` returning the alert’s actions.

## Discussion

In the example below, a login form conditionally presents an alert by setting
the `didFail` state variable. When the form sets the value to to `true`, the
system displays an alert with an “OK” action.

All actions in an alert dismiss the alert after the action runs. The default
button is shown with greater prominence. You can influence the default button
by assigning it the `defaultAction` keyboard shortcut.

The system may reorder the buttons based on their role and prominence.

If no actions are present, the system includes a standard “OK” action. No
default cancel action is provided. If you want to show a cancel action, use a
button with a role of `cancel`.

On iOS, tvOS, and watchOS, alerts only support controls with labels that are
`Text`. Passing any other type of view results in the content being omitted.

This modifier creates a `Text` view for the title on your behalf, and treats
the localized key similar to `init(_:tableName:bundle:comment:)`. See `Text`
for more information about localizing strings.

## See Also

### Presenting an alert

`func alert<S, A>(S, isPresented: Binding<Bool>, actions: () -> A) -> some
View`

Presents an alert when a given condition is true, using a string variable as a
title.

`func alert<A>(Text, isPresented: Binding<Bool>, actions: () -> A) -> some
View`

Presents an alert when a given condition is true, using a text view for the
title.

`func alert<A, T>(Text, isPresented: Binding<Bool>, presenting: T?, actions:
(T) -> A) -> some View`

Presents an alert using the given data to produce the alert’s content and a
text view as a title.

`func alert<A, T>(LocalizedStringKey, isPresented: Binding<Bool>, presenting:
T?, actions: (T) -> A) -> some View`

Presents an alert using the given data to produce the alert’s content and a
localized string key for a title.

`func alert<S, A, T>(S, isPresented: Binding<Bool>, presenting: T?, actions:
(T) -> A) -> some View`

Presents an alert using the given data to produce the alert’s content and a
string variable as a title.

`func alert<E, A>(isPresented: Binding<Bool>, error: E?, actions: () -> A) ->
some View`

Presents an alert when an error is present.

Instance Method

# alert(_:isPresented:presenting:actions:)

Presents an alert using the given data to produce the alert’s content and a
text view as a title.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func alert<A, T>(
        _ title: Text,
        isPresented: Binding<Bool>,
        presenting data: T?,
        @ViewBuilder actions: (T) -> A
    ) -> some View where A : View
    

##  Parameters

`title`

    

the title of the alert.

`isPresented`

    

A binding to a Boolean value that determines whether to present the alert.
When the user presses or taps one of the alert’s actions, the system sets this
value to `false` and dismisses.

`data`

    

An optional source of truth for the alert. The system passes the contents to
the modifier’s closures. You use this data to populate the fields of an alert
that you create that the system displays to the user.

`actions`

    

A `ViewBuilder` returning the alert’s actions given the currently available
data.

## Discussion

For the alert to appear, both `isPresented` must be `true` and `data` must not
be `nil`. The data should not change after the presentation occurs. Any
changes that you make after the presentation occurs are ignored.

Use this method when you need to populate the fields of an alert with content
from a data source. The example below shows a custom data source,
`SaveDetails`, that provides data to populate the alert:

All actions in an alert dismiss the alert after the action runs. The default
button is shown with greater prominence. You can influence the default button
by assigning it the `defaultAction` keyboard shortcut.

The system may reorder the buttons based on their role and prominence.

If no actions are present, the system includes a standard “OK” action. No
default cancel action is provided. If you want to show a cancel action, use a
button with a role of `cancel`.

On iOS, tvOS, and watchOS, alerts only support controls with labels that are
`Text`. Passing any other type of view results in the content being omitted.

## See Also

### Presenting an alert

`func alert<S, A>(S, isPresented: Binding<Bool>, actions: () -> A) -> some
View`

Presents an alert when a given condition is true, using a string variable as a
title.

`func alert<A>(Text, isPresented: Binding<Bool>, actions: () -> A) -> some
View`

Presents an alert when a given condition is true, using a text view for the
title.

`func alert<A>(LocalizedStringKey, isPresented: Binding<Bool>, actions: () ->
A) -> some View`

Presents an alert when a given condition is true, using a localized string key
for the title.

`func alert<A, T>(LocalizedStringKey, isPresented: Binding<Bool>, presenting:
T?, actions: (T) -> A) -> some View`

Presents an alert using the given data to produce the alert’s content and a
localized string key for a title.

`func alert<S, A, T>(S, isPresented: Binding<Bool>, presenting: T?, actions:
(T) -> A) -> some View`

Presents an alert using the given data to produce the alert’s content and a
string variable as a title.

`func alert<E, A>(isPresented: Binding<Bool>, error: E?, actions: () -> A) ->
some View`

Presents an alert when an error is present.

Instance Method

# alert(_:isPresented:presenting:actions:)

Presents an alert using the given data to produce the alert’s content and a
localized string key for a title.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func alert<A, T>(
        _ titleKey: LocalizedStringKey,
        isPresented: Binding<Bool>,
        presenting data: T?,
        @ViewBuilder actions: (T) -> A
    ) -> some View where A : View
    

##  Parameters

`titleKey`

    

The key for the localized string that describes the title of the alert.

`isPresented`

    

A binding to a Boolean value that determines whether to present the alert.
When the user presses or taps one of the alert’s actions, the system sets this
value to `false` and dismisses.

`data`

    

An optional source of truth for the alert. The system passes the contents to
the modifier’s closures. You use this data to populate the fields of an alert
that you create that the system displays to the user.

`actions`

    

A `ViewBuilder` returning the alert’s actions given the currently available
data.

## Discussion

For the alert to appear, both `isPresented` must be `true` and `data` must not
be `nil`. The data should not change after the presentation occurs. Any
changes that you make after the presentation occurs are ignored.

Use this method when you need to populate the fields of an alert with content
from a data source. The example below shows a custom data source,
`SaveDetails`, that provides data to populate the alert:

This modifier creates a `Text` view for the title on your behalf, and treats
the localized key similar to `init(_:tableName:bundle:comment:)`. See `Text`
for more information about localizing strings.

All actions in an alert dismiss the alert after the action runs. The default
button is shown with greater prominence. You can influence the default button
by assigning it the `defaultAction` keyboard shortcut.

The system may reorder the buttons based on their role and prominence.

If no actions are present, the system includes a standard “OK” action. No
default cancel action is provided. If you want to show a cancel action, use a
button with a role of `cancel`.

On iOS, tvOS, and watchOS, alerts only support controls with labels that are
`Text`. Passing any other type of view results in the content being omitted.

## See Also

### Presenting an alert

`func alert<S, A>(S, isPresented: Binding<Bool>, actions: () -> A) -> some
View`

Presents an alert when a given condition is true, using a string variable as a
title.

`func alert<A>(Text, isPresented: Binding<Bool>, actions: () -> A) -> some
View`

Presents an alert when a given condition is true, using a text view for the
title.

`func alert<A>(LocalizedStringKey, isPresented: Binding<Bool>, actions: () ->
A) -> some View`

Presents an alert when a given condition is true, using a localized string key
for the title.

`func alert<A, T>(Text, isPresented: Binding<Bool>, presenting: T?, actions:
(T) -> A) -> some View`

Presents an alert using the given data to produce the alert’s content and a
text view as a title.

`func alert<S, A, T>(S, isPresented: Binding<Bool>, presenting: T?, actions:
(T) -> A) -> some View`

Presents an alert using the given data to produce the alert’s content and a
string variable as a title.

`func alert<E, A>(isPresented: Binding<Bool>, error: E?, actions: () -> A) ->
some View`

Presents an alert when an error is present.

Instance Method

# alert(_:isPresented:presenting:actions:)

Presents an alert using the given data to produce the alert’s content and a
string variable as a title.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func alert<S, A, T>(
        _ title: S,
        isPresented: Binding<Bool>,
        presenting data: T?,
        @ViewBuilder actions: (T) -> A
    ) -> some View where S : StringProtocol, A : View
    

##  Parameters

`title`

    

A text string used as the title of the alert.

`isPresented`

    

A binding to a Boolean value that determines whether to present the alert.
When the user presses or taps one of the alert’s actions, the system sets this
value to `false` and dismisses.

`data`

    

An optional source of truth for the alert. The system passes the contents to
the modifier’s closures. You use this data to populate the fields of an alert
that you create that the system displays to the user.

`actions`

    

A `ViewBuilder` returning the alert’s actions given the currently available
data.

## Discussion

For the alert to appear, both `isPresented` must be `true` and `data` must not
be `nil`. The data should not change after the presentation occurs. Any
changes that you make after the presentation occurs are ignored.

Use this method when you need to populate the fields of an alert with content
from a data source. The example below shows a custom data source,
`SaveDetails`, that provides data to populate the alert:

All actions in an alert dismiss the alert after the action runs. The default
button is shown with greater prominence. You can influence the default button
by assigning it the `defaultAction` keyboard shortcut.

The system may reorder the buttons based on their role and prominence.

If no actions are present, the system includes a standard “OK” action. No
default cancel action is provided. If you want to show a cancel action, use a
button with a role of `cancel`.

On iOS, tvOS, and watchOS, alerts only support controls with labels that are
`Text`. Passing any other type of view results in the content being omitted.

## See Also

### Presenting an alert

`func alert<S, A>(S, isPresented: Binding<Bool>, actions: () -> A) -> some
View`

Presents an alert when a given condition is true, using a string variable as a
title.

`func alert<A>(Text, isPresented: Binding<Bool>, actions: () -> A) -> some
View`

Presents an alert when a given condition is true, using a text view for the
title.

`func alert<A>(LocalizedStringKey, isPresented: Binding<Bool>, actions: () ->
A) -> some View`

Presents an alert when a given condition is true, using a localized string key
for the title.

`func alert<A, T>(Text, isPresented: Binding<Bool>, presenting: T?, actions:
(T) -> A) -> some View`

Presents an alert using the given data to produce the alert’s content and a
text view as a title.

`func alert<A, T>(LocalizedStringKey, isPresented: Binding<Bool>, presenting:
T?, actions: (T) -> A) -> some View`

Presents an alert using the given data to produce the alert’s content and a
localized string key for a title.

`func alert<E, A>(isPresented: Binding<Bool>, error: E?, actions: () -> A) ->
some View`

Presents an alert when an error is present.

Instance Method

# alert(isPresented:error:actions:)

Presents an alert when an error is present.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func alert<E, A>(
        isPresented: Binding<Bool>,
        error: E?,
        @ViewBuilder actions: () -> A
    ) -> some View where E : LocalizedError, A : View
    

##  Parameters

`isPresented`

    

A binding to a Boolean value that determines whether to present the alert.
When the user presses or taps one of the alert’s actions, the system sets this
value to `false` and dismisses.

`error`

    

An optional localized Error that is used to generate the alert’s title. The
system passes the contents to the modifier’s closures. You use this data to
populate the fields of an alert that you create that the system displays to
the user.

`actions`

    

A `ViewBuilder` returning the alert’s actions.

## Discussion

In the example below, a form conditionally presents an alert depending upon
the value of an error. When the error value isn’t `nil`, the system presents
an alert with an “OK” action.

The title of the alert is inferred from the error’s `errorDescription`.

All actions in an alert dismiss the alert after the action runs. The default
button is shown with greater prominence. You can influence the default button
by assigning it the `defaultAction` keyboard shortcut.

The system may reorder the buttons based on their role and prominence.

If no actions are present, the system includes a standard “OK” action. No
default cancel action is provided. If you want to show a cancel action, use a
button with a role of `cancel`.

On iOS, tvOS, and watchOS, alerts only support controls with labels that are
`Text`. Passing any other type of view results in the content being omitted.

This modifier creates a `Text` view for the title on your behalf, and treats
the localized key similar to `init(_:tableName:bundle:comment:)`. See `Text`
for more information about localizing strings.

## See Also

### Presenting an alert

`func alert<S, A>(S, isPresented: Binding<Bool>, actions: () -> A) -> some
View`

Presents an alert when a given condition is true, using a string variable as a
title.

`func alert<A>(Text, isPresented: Binding<Bool>, actions: () -> A) -> some
View`

Presents an alert when a given condition is true, using a text view for the
title.

`func alert<A>(LocalizedStringKey, isPresented: Binding<Bool>, actions: () ->
A) -> some View`

Presents an alert when a given condition is true, using a localized string key
for the title.

`func alert<A, T>(Text, isPresented: Binding<Bool>, presenting: T?, actions:
(T) -> A) -> some View`

Presents an alert using the given data to produce the alert’s content and a
text view as a title.

`func alert<A, T>(LocalizedStringKey, isPresented: Binding<Bool>, presenting:
T?, actions: (T) -> A) -> some View`

Presents an alert using the given data to produce the alert’s content and a
localized string key for a title.

`func alert<S, A, T>(S, isPresented: Binding<Bool>, presenting: T?, actions:
(T) -> A) -> some View`

Presents an alert using the given data to produce the alert’s content and a
string variable as a title.

Instance Method

# alert(_:isPresented:actions:message:)

Presents an alert with a message when a given condition is true using a string
variable as a title.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func alert<S, A, M>(
        _ title: S,
        isPresented: Binding<Bool>,
        @ViewBuilder actions: () -> A,
        @ViewBuilder message: () -> M
    ) -> some View where S : StringProtocol, A : View, M : View
    

##  Parameters

`title`

    

A text string used as the title of the alert.

`isPresented`

    

A binding to a Boolean value that determines whether to present the alert.
When the user presses or taps one of the alert’s actions, the system sets this
value to `false` and dismisses.

`actions`

    

A `ViewBuilder` returning the alert’s actions.

`message`

    

A `ViewBuilder` returning the message for the alert.

## Discussion

In the example below, a login form conditionally presents an alert by setting
the `didFail` state variable. When the form sets the value to to `true`, the
system displays an alert with an “OK” action.

All actions in an alert dismiss the alert after the action runs. The default
button is shown with greater prominence. You can influence the default button
by assigning it the `defaultAction` keyboard shortcut.

The system may reorder the buttons based on their role and prominence.

If no actions are present, the system includes a standard “OK” action. No
default cancel action is provided. If you want to show a cancel action, use a
button with a role of `cancel`.

On iOS, tvOS, and watchOS, alerts only support controls with labels that are
`Text`. Passing any other type of view results in the content being omitted.

Only unstyled text is supported for the message.

## See Also

### Presenting an alert with a message

`func alert<A, M>(LocalizedStringKey, isPresented: Binding<Bool>, actions: ()
-> A, message: () -> M) -> some View`

Presents an alert with a message when a given condition is true, using a
localized string key for a title.

`func alert<A, M>(Text, isPresented: Binding<Bool>, actions: () -> A, message:
() -> M) -> some View`

Presents an alert with a message when a given condition is true using a text
view as a title.

`func alert<A, M, T>(LocalizedStringKey, isPresented: Binding<Bool>,
presenting: T?, actions: (T) -> A, message: (T) -> M) -> some View`

Presents an alert with a message using the given data to produce the alert’s
content and a localized string key for a title.

`func alert<A, M, T>(Text, isPresented: Binding<Bool>, presenting: T?,
actions: (T) -> A, message: (T) -> M) -> some View`

Presents an alert with a message using the given data to produce the alert’s
content and a text view for a title.

`func alert<S, A, M, T>(S, isPresented: Binding<Bool>, presenting: T?,
actions: (T) -> A, message: (T) -> M) -> some View`

Presents an alert with a message using the given data to produce the alert’s
content and a string variable as a title.

`func alert<E, A, M>(isPresented: Binding<Bool>, error: E?, actions: (E) -> A,
message: (E) -> M) -> some View`

Presents an alert with a message when an error is present.

Instance Method

# alert(_:isPresented:actions:message:)

Presents an alert with a message when a given condition is true, using a
localized string key for a title.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func alert<A, M>(
        _ titleKey: LocalizedStringKey,
        isPresented: Binding<Bool>,
        @ViewBuilder actions: () -> A,
        @ViewBuilder message: () -> M
    ) -> some View where A : View, M : View
    

##  Parameters

`titleKey`

    

The key for the localized string that describes the title of the alert.

`isPresented`

    

A binding to a Boolean value that determines whether to present the alert.
When the user presses or taps one of the alert’s actions, the system sets this
value to `false` and dismisses.

`actions`

    

A `ViewBuilder` returning the alert’s actions.

`message`

    

A `ViewBuilder` returning the message for the alert.

## Discussion

In the example below, a login form conditionally presents an alert by setting
the `didFail` state variable. When the form sets the value to to `true`, the
system displays an alert with an “OK” action.

All actions in an alert dismiss the alert after the action runs. The default
button is shown with greater prominence. You can influence the default button
by assigning it the `defaultAction` keyboard shortcut.

The system may reorder the buttons based on their role and prominence.

If no actions are present, the system includes a standard “OK” action. No
default cancel action is provided. If you want to show a cancel action, use a
button with a role of `cancel`.

On iOS, tvOS, and watchOS, alerts only support controls with labels that are
`Text`. Passing any other type of view results in the content being omitted.

Only unstyled text is supported for the message.

This modifier creates a `Text` view for the title on your behalf, and treats
the localized key similar to `init(_:tableName:bundle:comment:)`. See `Text`
for more information about localizing strings.

## See Also

### Presenting an alert with a message

`func alert<S, A, M>(S, isPresented: Binding<Bool>, actions: () -> A, message:
() -> M) -> some View`

Presents an alert with a message when a given condition is true using a string
variable as a title.

`func alert<A, M>(Text, isPresented: Binding<Bool>, actions: () -> A, message:
() -> M) -> some View`

Presents an alert with a message when a given condition is true using a text
view as a title.

`func alert<A, M, T>(LocalizedStringKey, isPresented: Binding<Bool>,
presenting: T?, actions: (T) -> A, message: (T) -> M) -> some View`

Presents an alert with a message using the given data to produce the alert’s
content and a localized string key for a title.

`func alert<A, M, T>(Text, isPresented: Binding<Bool>, presenting: T?,
actions: (T) -> A, message: (T) -> M) -> some View`

Presents an alert with a message using the given data to produce the alert’s
content and a text view for a title.

`func alert<S, A, M, T>(S, isPresented: Binding<Bool>, presenting: T?,
actions: (T) -> A, message: (T) -> M) -> some View`

Presents an alert with a message using the given data to produce the alert’s
content and a string variable as a title.

`func alert<E, A, M>(isPresented: Binding<Bool>, error: E?, actions: (E) -> A,
message: (E) -> M) -> some View`

Presents an alert with a message when an error is present.

Instance Method

# alert(_:isPresented:actions:message:)

Presents an alert with a message when a given condition is true using a text
view as a title.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func alert<A, M>(
        _ title: Text,
        isPresented: Binding<Bool>,
        @ViewBuilder actions: () -> A,
        @ViewBuilder message: () -> M
    ) -> some View where A : View, M : View
    

##  Parameters

`title`

    

The title of the alert.

`isPresented`

    

A binding to a Boolean value that determines whether to present the alert.
When the user presses or taps one of the alert’s actions, the system sets this
value to `false` and dismisses.

`actions`

    

A `ViewBuilder` returning the alert’s actions.

`message`

    

A `ViewBuilder` returning the message for the alert.

## Discussion

In the example below, a login form conditionally presents an alert by setting
the `didFail` state variable. When the form sets the value to to `true`, the
system displays an alert with an “OK” action.

All actions in an alert dismiss the alert after the action runs. The default
button is shown with greater prominence. You can influence the default button
by assigning it the `defaultAction` keyboard shortcut.

The system may reorder the buttons based on their role and prominence.

If no actions are present, the system includes a standard “OK” action. No
default cancel action is provided. If you want to show a cancel action, use a
button with a role of `cancel`.

On iOS, tvOS, and watchOS, alerts only support controls with labels that are
`Text`. Passing any other type of view results in the content being omitted.

Only unstyled text is supported for the message.

## See Also

### Presenting an alert with a message

`func alert<S, A, M>(S, isPresented: Binding<Bool>, actions: () -> A, message:
() -> M) -> some View`

Presents an alert with a message when a given condition is true using a string
variable as a title.

`func alert<A, M>(LocalizedStringKey, isPresented: Binding<Bool>, actions: ()
-> A, message: () -> M) -> some View`

Presents an alert with a message when a given condition is true, using a
localized string key for a title.

`func alert<A, M, T>(LocalizedStringKey, isPresented: Binding<Bool>,
presenting: T?, actions: (T) -> A, message: (T) -> M) -> some View`

Presents an alert with a message using the given data to produce the alert’s
content and a localized string key for a title.

`func alert<A, M, T>(Text, isPresented: Binding<Bool>, presenting: T?,
actions: (T) -> A, message: (T) -> M) -> some View`

Presents an alert with a message using the given data to produce the alert’s
content and a text view for a title.

`func alert<S, A, M, T>(S, isPresented: Binding<Bool>, presenting: T?,
actions: (T) -> A, message: (T) -> M) -> some View`

Presents an alert with a message using the given data to produce the alert’s
content and a string variable as a title.

`func alert<E, A, M>(isPresented: Binding<Bool>, error: E?, actions: (E) -> A,
message: (E) -> M) -> some View`

Presents an alert with a message when an error is present.

Instance Method

# alert(_:isPresented:presenting:actions:message:)

Presents an alert with a message using the given data to produce the alert’s
content and a localized string key for a title.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func alert<A, M, T>(
        _ titleKey: LocalizedStringKey,
        isPresented: Binding<Bool>,
        presenting data: T?,
        @ViewBuilder actions: (T) -> A,
        @ViewBuilder message: (T) -> M
    ) -> some View where A : View, M : View
    

##  Parameters

`titleKey`

    

The key for the localized string that describes the title of the alert.

`isPresented`

    

A binding to a Boolean value that determines whether to present the alert.
When the user presses or taps one of the alert’s actions, the system sets this
value to `false` and dismisses.

`data`

    

An optional source of truth for the alert. The system passes the contents to
the modifier’s closures. You use this data to populate the fields of an alert
that you create that the system displays to the user.

`actions`

    

A `ViewBuilder` returning the alert’s actions given the currently available
data.

`message`

    

A `ViewBuilder` returning the message for the alert given the currently
available data.

## Discussion

For the alert to appear, both `isPresented` must be `true` and `data` must not
be `nil`. The data should not change after the presentation occurs. Any
changes that you make after the presentation occurs are ignored.

Use this method when you need to populate the fields of an alert with content
from a data source. The example below shows a custom data source,
`SaveDetails`, that provides data to populate the alert:

This modifier creates a `Text` view for the title on your behalf, and treats
the localized key similar to `init(_:tableName:bundle:comment:)`. See `Text`
for more information about localizing strings.

All actions in an alert dismiss the alert after the action runs. The default
button is shown with greater prominence. You can influence the default button
by assigning it the `defaultAction` keyboard shortcut.

The system may reorder the buttons based on their role and prominence.

If no actions are present, the system includes a standard “OK” action. No
default cancel action is provided. If you want to show a cancel action, use a
button with a role of `cancel`.

On iOS, tvOS, and watchOS, alerts only support controls with labels that are
`Text`. Passing any other type of view results in the content being omitted.

Only unstyled text is supported for the message.

## See Also

### Presenting an alert with a message

`func alert<S, A, M>(S, isPresented: Binding<Bool>, actions: () -> A, message:
() -> M) -> some View`

Presents an alert with a message when a given condition is true using a string
variable as a title.

`func alert<A, M>(LocalizedStringKey, isPresented: Binding<Bool>, actions: ()
-> A, message: () -> M) -> some View`

Presents an alert with a message when a given condition is true, using a
localized string key for a title.

`func alert<A, M>(Text, isPresented: Binding<Bool>, actions: () -> A, message:
() -> M) -> some View`

Presents an alert with a message when a given condition is true using a text
view as a title.

`func alert<A, M, T>(Text, isPresented: Binding<Bool>, presenting: T?,
actions: (T) -> A, message: (T) -> M) -> some View`

Presents an alert with a message using the given data to produce the alert’s
content and a text view for a title.

`func alert<S, A, M, T>(S, isPresented: Binding<Bool>, presenting: T?,
actions: (T) -> A, message: (T) -> M) -> some View`

Presents an alert with a message using the given data to produce the alert’s
content and a string variable as a title.

`func alert<E, A, M>(isPresented: Binding<Bool>, error: E?, actions: (E) -> A,
message: (E) -> M) -> some View`

Presents an alert with a message when an error is present.

Instance Method

# alert(_:isPresented:presenting:actions:message:)

Presents an alert with a message using the given data to produce the alert’s
content and a text view for a title.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func alert<A, M, T>(
        _ title: Text,
        isPresented: Binding<Bool>,
        presenting data: T?,
        @ViewBuilder actions: (T) -> A,
        @ViewBuilder message: (T) -> M
    ) -> some View where A : View, M : View
    

##  Parameters

`title`

    

the title of the alert.

`isPresented`

    

A binding to a Boolean value that determines whether to present the alert.
When the user presses or taps one of the alert’s actions, the system sets this
value to `false` and dismisses.

`data`

    

An optional source of truth for the alert. The system passes the contents to
the modifier’s closures. You use this data to populate the fields of an alert
that you create that the system displays to the user.

`actions`

    

A `ViewBuilder` returning the alert’s actions given the currently available
data.

`message`

    

A `ViewBuilder` returning the message for the alert given the currently
available data.

## Discussion

For the alert to appear, both `isPresented` must be `true` and `data` must not
be `nil`. The data should not change after the presentation occurs. Any
changes that you make after the presentation occurs are ignored.

Use this method when you need to populate the fields of an alert with content
from a data source. The example below shows a custom data source,
`SaveDetails`, that provides data to populate the alert:

All actions in an alert dismiss the alert after the action runs. The default
button is shown with greater prominence. You can influence the default button
by assigning it the `defaultAction` keyboard shortcut.

The system may reorder the buttons based on their role and prominence.

If no actions are present, the system includes a standard “OK” action. No
default cancel action is provided. If you want to show a cancel action, use a
button with a role of `cancel`.

On iOS, tvOS, and watchOS, alerts only support controls with labels that are
`Text`. Passing any other type of view results in the content being omitted.

Only unstyled text is supported for the message.

## See Also

### Presenting an alert with a message

`func alert<S, A, M>(S, isPresented: Binding<Bool>, actions: () -> A, message:
() -> M) -> some View`

Presents an alert with a message when a given condition is true using a string
variable as a title.

`func alert<A, M>(LocalizedStringKey, isPresented: Binding<Bool>, actions: ()
-> A, message: () -> M) -> some View`

Presents an alert with a message when a given condition is true, using a
localized string key for a title.

`func alert<A, M>(Text, isPresented: Binding<Bool>, actions: () -> A, message:
() -> M) -> some View`

Presents an alert with a message when a given condition is true using a text
view as a title.

`func alert<A, M, T>(LocalizedStringKey, isPresented: Binding<Bool>,
presenting: T?, actions: (T) -> A, message: (T) -> M) -> some View`

Presents an alert with a message using the given data to produce the alert’s
content and a localized string key for a title.

`func alert<S, A, M, T>(S, isPresented: Binding<Bool>, presenting: T?,
actions: (T) -> A, message: (T) -> M) -> some View`

Presents an alert with a message using the given data to produce the alert’s
content and a string variable as a title.

`func alert<E, A, M>(isPresented: Binding<Bool>, error: E?, actions: (E) -> A,
message: (E) -> M) -> some View`

Presents an alert with a message when an error is present.

Instance Method

# alert(_:isPresented:presenting:actions:message:)

Presents an alert with a message using the given data to produce the alert’s
content and a string variable as a title.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func alert<S, A, M, T>(
        _ title: S,
        isPresented: Binding<Bool>,
        presenting data: T?,
        @ViewBuilder actions: (T) -> A,
        @ViewBuilder message: (T) -> M
    ) -> some View where S : StringProtocol, A : View, M : View
    

##  Parameters

`title`

    

A text string used as the title of the alert.

`isPresented`

    

A binding to a Boolean value that determines whether to present the alert.
When the user presses or taps one of the alert’s actions, the system sets this
value to `false` and dismisses.

`data`

    

An optional source of truth for the alert. The system passes the contents to
the modifier’s closures. You use this data to populate the fields of an alert
that you create that the system displays to the user.

`actions`

    

A `ViewBuilder` returning the alert’s actions given the currently available
data.

`message`

    

A `ViewBuilder` returning the message for the alert given the currently
available data.

## Discussion

For the alert to appear, both `isPresented` must be `true` and `data` must not
be `nil`. The data should not change after the presentation occurs. Any
changes that you make after the presentation occurs are ignored.

Use this method when you need to populate the fields of an alert with content
from a data source. The example below shows a custom data source,
`SaveDetails`, that provides data to populate the alert:

All actions in an alert dismiss the alert after the action runs. The default
button is shown with greater prominence. You can influence the default button
by assigning it the `defaultAction` keyboard shortcut.

The system may reorder the buttons based on their role and prominence.

If no actions are present, the system includes a standard “OK” action. No
default cancel action is provided. If you want to show a cancel action, use a
button with a role of `cancel`.

On iOS, tvOS, and watchOS, alerts only support controls with labels that are
`Text`. Passing any other type of view results in the content being omitted.

Only unstyled text is supported for the message.

## See Also

### Presenting an alert with a message

`func alert<S, A, M>(S, isPresented: Binding<Bool>, actions: () -> A, message:
() -> M) -> some View`

Presents an alert with a message when a given condition is true using a string
variable as a title.

`func alert<A, M>(LocalizedStringKey, isPresented: Binding<Bool>, actions: ()
-> A, message: () -> M) -> some View`

Presents an alert with a message when a given condition is true, using a
localized string key for a title.

`func alert<A, M>(Text, isPresented: Binding<Bool>, actions: () -> A, message:
() -> M) -> some View`

Presents an alert with a message when a given condition is true using a text
view as a title.

`func alert<A, M, T>(LocalizedStringKey, isPresented: Binding<Bool>,
presenting: T?, actions: (T) -> A, message: (T) -> M) -> some View`

Presents an alert with a message using the given data to produce the alert’s
content and a localized string key for a title.

`func alert<A, M, T>(Text, isPresented: Binding<Bool>, presenting: T?,
actions: (T) -> A, message: (T) -> M) -> some View`

Presents an alert with a message using the given data to produce the alert’s
content and a text view for a title.

`func alert<E, A, M>(isPresented: Binding<Bool>, error: E?, actions: (E) -> A,
message: (E) -> M) -> some View`

Presents an alert with a message when an error is present.

Instance Method

# alert(isPresented:error:actions:message:)

Presents an alert with a message when an error is present.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func alert<E, A, M>(
        isPresented: Binding<Bool>,
        error: E?,
        @ViewBuilder actions: (E) -> A,
        @ViewBuilder message: (E) -> M
    ) -> some View where E : LocalizedError, A : View, M : View
    

##  Parameters

`isPresented`

    

A binding to a Boolean value that determines whether to present the alert.
When the user presses or taps one of the alert’s actions, the system sets this
value to `false` and dismisses.

`error`

    

An optional localized Error that is used to generate the alert’s title. The
system passes the contents to the modifier’s closures. You use this data to
populate the fields of an alert that you create that the system displays to
the user.

`actions`

    

A `ViewBuilder` returning the alert’s actions.

`message`

    

A view builder returning the message for the alert given the current error.

## Discussion

In the example below, a form conditionally presents an alert depending upon
the value of an error. When the error value isn’t `nil`, the system presents
an alert with an “OK” action.

The title of the alert is inferred from the error’s `errorDescription`.

All actions in an alert dismiss the alert after the action runs. The default
button is shown with greater prominence. You can influence the default button
by assigning it the `defaultAction` keyboard shortcut.

The system may reorder the buttons based on their role and prominence.

If no actions are present, the system includes a standard “OK” action. No
default cancel action is provided. If you want to show a cancel action, use a
button with a role of `cancel`.

On iOS, tvOS, and watchOS, alerts only support controls with labels that are
`Text`. Passing any other type of view results in the content being omitted.

This modifier creates a `Text` view for the title on your behalf, and treats
the localized key similar to `init(_:tableName:bundle:comment:)`. See `Text`
for more information about localizing strings.

## See Also

### Presenting an alert with a message

`func alert<S, A, M>(S, isPresented: Binding<Bool>, actions: () -> A, message:
() -> M) -> some View`

Presents an alert with a message when a given condition is true using a string
variable as a title.

`func alert<A, M>(LocalizedStringKey, isPresented: Binding<Bool>, actions: ()
-> A, message: () -> M) -> some View`

Presents an alert with a message when a given condition is true, using a
localized string key for a title.

`func alert<A, M>(Text, isPresented: Binding<Bool>, actions: () -> A, message:
() -> M) -> some View`

Presents an alert with a message when a given condition is true using a text
view as a title.

`func alert<A, M, T>(LocalizedStringKey, isPresented: Binding<Bool>,
presenting: T?, actions: (T) -> A, message: (T) -> M) -> some View`

Presents an alert with a message using the given data to produce the alert’s
content and a localized string key for a title.

`func alert<A, M, T>(Text, isPresented: Binding<Bool>, presenting: T?,
actions: (T) -> A, message: (T) -> M) -> some View`

Presents an alert with a message using the given data to produce the alert’s
content and a text view for a title.

`func alert<S, A, M, T>(S, isPresented: Binding<Bool>, presenting: T?,
actions: (T) -> A, message: (T) -> M) -> some View`

Presents an alert with a message using the given data to produce the alert’s
content and a string variable as a title.

Instance Method

# confirmationDialog(_:isPresented:titleVisibility:actions:)

Presents a confirmation dialog when a given condition is true, using a string
variable as a title.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func confirmationDialog<S, A>(
        _ title: S,
        isPresented: Binding<Bool>,
        titleVisibility: Visibility = .automatic,
        @ViewBuilder actions: () -> A
    ) -> some View where S : StringProtocol, A : View
    

##  Parameters

`title`

    

A text string used as the title of the dialog.

`isPresented`

    

A binding to a Boolean value that determines whether to present the dialog.
When the user presses or taps the dialog’s default action button, the system
sets this value to `false`, dismissing the dialog.

`titleVisibility`

    

The visibility of the dialog’s title. The default value is
`Visibility.automatic`.

`actions`

    

A view builder returning the dialog’s actions.

## Discussion

In the example below, a button conditionally presents a confirmation dialog
depending upon the value of a bound Boolean variable. When the Boolean value
is set to `true`, the system displays a confirmation dialog with a cancel
action and a destructive action.

All actions in a confirmation dialog will dismiss the dialog after the action
runs. The default button will be shown with greater prominence. You can
influence the default button by assigning it the `defaultAction` keyboard
shortcut.

The system may reorder the buttons based on their role and prominence.

Dialogs include a standard dismiss action by default. If you provide a button
with a role of `cancel`, that button takes the place of the default dismiss
action. You don’t have to dismiss the presentation with the cancel button’s
action.

Note

In regular size classes in iOS, the system renders confirmation dialogs as a
popover that the user dismisses by tapping anywhere outside the popover,
rather than displaying the standard dismiss action.

## See Also

### Getting confirmation for an action

`func confirmationDialog<A>(Text, isPresented: Binding<Bool>, titleVisibility:
Visibility, actions: () -> A) -> some View`

Presents a confirmation dialog when a given condition is true, using a text
view for the title.

`func confirmationDialog<A>(LocalizedStringKey, isPresented: Binding<Bool>,
titleVisibility: Visibility, actions: () -> A) -> some View`

Presents a confirmation dialog when a given condition is true, using a
localized string key for the title.

`func confirmationDialog<A, T>(Text, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A) -> some View`

Presents a confirmation dialog using data to produce the dialog’s content and
a text view for the title.

`func confirmationDialog<A, T>(LocalizedStringKey, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A) -> some View`

Presents a confirmation dialog using data to produce the dialog’s content and
a localized string key for the title.

`func confirmationDialog<S, A, T>(S, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A) -> some View`

Presents a confirmation dialog using data to produce the dialog’s content and
a string variable for the title.

Instance Method

# confirmationDialog(_:isPresented:titleVisibility:actions:)

Presents a confirmation dialog when a given condition is true, using a text
view for the title.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func confirmationDialog<A>(
        _ title: Text,
        isPresented: Binding<Bool>,
        titleVisibility: Visibility = .automatic,
        @ViewBuilder actions: () -> A
    ) -> some View where A : View
    

##  Parameters

`title`

    

the title of the dialog.

`isPresented`

    

A binding to a Boolean value that determines whether to present the dialog.
When the user presses or taps the dialog’s default action button, the system
sets this value to `false`, dismissing the dialog.

`titleVisibility`

    

The visibility of the dialog’s title. The default value is
`Visibility.automatic`.

`actions`

    

A view builder returning the dialog’s actions.

## Discussion

In the example below, a button conditionally presents a confirmation dialog
depending upon the value of a bound Boolean variable. When the Boolean value
is set to `true`, the system displays a confirmation dialog with a cancel
action and a destructive action.

All actions in a confirmation dialog will dismiss the dialog after the action
runs. The default button will be shown with greater prominence. You can
influence the default button by assigning it the `defaultAction` keyboard
shortcut.

The system may reorder the buttons based on their role and prominence.

Dialogs include a standard dismiss action by default. If you provide a button
with a role of `cancel`, that button takes the place of the default dismiss
action. You don’t have to dismiss the presentation with the cancel button’s
action.

Note

In regular size classes in iOS, the system renders confirmation dialogs as a
popover that the user dismisses by tapping anywhere outside the popover,
rather than displaying the standard dismiss action.

## See Also

### Getting confirmation for an action

`func confirmationDialog<S, A>(S, isPresented: Binding<Bool>, titleVisibility:
Visibility, actions: () -> A) -> some View`

Presents a confirmation dialog when a given condition is true, using a string
variable as a title.

`func confirmationDialog<A>(LocalizedStringKey, isPresented: Binding<Bool>,
titleVisibility: Visibility, actions: () -> A) -> some View`

Presents a confirmation dialog when a given condition is true, using a
localized string key for the title.

`func confirmationDialog<A, T>(Text, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A) -> some View`

Presents a confirmation dialog using data to produce the dialog’s content and
a text view for the title.

`func confirmationDialog<A, T>(LocalizedStringKey, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A) -> some View`

Presents a confirmation dialog using data to produce the dialog’s content and
a localized string key for the title.

`func confirmationDialog<S, A, T>(S, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A) -> some View`

Presents a confirmation dialog using data to produce the dialog’s content and
a string variable for the title.

Instance Method

# confirmationDialog(_:isPresented:titleVisibility:actions:)

Presents a confirmation dialog when a given condition is true, using a
localized string key for the title.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func confirmationDialog<A>(
        _ titleKey: LocalizedStringKey,
        isPresented: Binding<Bool>,
        titleVisibility: Visibility = .automatic,
        @ViewBuilder actions: () -> A
    ) -> some View where A : View
    

##  Parameters

`titleKey`

    

The key for the localized string that describes the title of the dialog.

`isPresented`

    

A binding to a Boolean value that determines whether to present the dialog.
When the user presses or taps the dialog’s default action button, the system
sets this value to `false`, dismissing the dialog.

`titleVisibility`

    

The visibility of the dialog’s title. The default value is
`Visibility.automatic`.

`actions`

    

A view builder returning the dialog’s actions.

## Discussion

In the example below, a button conditionally presents a confirmation dialog
depending upon the value of a bound Boolean variable. When the Boolean value
is set to `true`, the system displays a confirmation dialog with a cancel
action and a destructive action.

All actions in a confirmation dialog will dismiss the dialog after the action
runs. The default button will be shown with greater prominence. You can
influence the default button by assigning it the `defaultAction` keyboard
shortcut.

The system may reorder the buttons based on their role and prominence.

Dialogs include a standard dismiss action by default. If you provide a button
with a role of `cancel`, that button takes the place of the default dismiss
action. You don’t have to dismiss the presentation with the cancel button’s
action.

Note

In regular size classes in iOS, the system renders confirmation dialogs as a
popover that the user dismisses by tapping anywhere outside the popover,
rather than displaying the standard dismiss action.

On iOS, tvOS, and watchOS, confirmation dialogs only support controls with
labels that are `Text`. Passing any other type of view results in the content
being omitted.

This modifier creates a `Text` view for the title on your behalf, and treats
the localized key similar to `init(_:tableName:bundle:comment:)`. See `Text`
for more information about localizing strings.

## See Also

### Getting confirmation for an action

`func confirmationDialog<S, A>(S, isPresented: Binding<Bool>, titleVisibility:
Visibility, actions: () -> A) -> some View`

Presents a confirmation dialog when a given condition is true, using a string
variable as a title.

`func confirmationDialog<A>(Text, isPresented: Binding<Bool>, titleVisibility:
Visibility, actions: () -> A) -> some View`

Presents a confirmation dialog when a given condition is true, using a text
view for the title.

`func confirmationDialog<A, T>(Text, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A) -> some View`

Presents a confirmation dialog using data to produce the dialog’s content and
a text view for the title.

`func confirmationDialog<A, T>(LocalizedStringKey, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A) -> some View`

Presents a confirmation dialog using data to produce the dialog’s content and
a localized string key for the title.

`func confirmationDialog<S, A, T>(S, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A) -> some View`

Presents a confirmation dialog using data to produce the dialog’s content and
a string variable for the title.

Instance Method

# confirmationDialog(_:isPresented:titleVisibility:presenting:actions:)

Presents a confirmation dialog using data to produce the dialog’s content and
a text view for the title.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func confirmationDialog<A, T>(
        _ title: Text,
        isPresented: Binding<Bool>,
        titleVisibility: Visibility = .automatic,
        presenting data: T?,
        @ViewBuilder actions: (T) -> A
    ) -> some View where A : View
    

##  Parameters

`title`

    

the title of the dialog.

`isPresented`

    

A binding to a Boolean value that determines whether to present the dialog.
When the user presses or taps the dialog’s default action button, the system
sets this value to `false`, dismissing the dialog.

`titleVisibility`

    

The visibility of the dialog’s title. The default value is
`Visibility.automatic`.

`data`

    

An optional source of truth for the confirmation dialog. The system passes the
contents to the modifier’s closures. You use this data to populate the fields
of a confirmation dialog that you create that the system displays to the user.

`actions`

    

A view builder returning the dialog’s actions given the currently available
data.

## Discussion

In order for the interface to appear, both `isPresented` must be `true` and
`data` must not be `nil`. `data` should not change after the presentation
occurs. Any changes which occur after the presentation occurs will be ignored.

Use this method when you need to populate the fields of a confirmation dialog
with content from a data source. The example below shows a custom data source,
`FileDetails`, that provides data to populate the dialog:

All actions in a confirmation dialog will dismiss the dialog after the action
runs. The default button will be shown with greater prominence. You can
influence the default button by assigning it the `defaultAction` keyboard
shortcut.

The system may reorder the buttons based on their role and prominence.

Dialogs include a standard dismiss action by default. If you provide a button
with a role of `cancel`, that button takes the place of the default dismiss
action. You don’t have to dismiss the presentation with the cancel button’s
action.

Note

In regular size classes in iOS, the system renders confirmation dialogs as a
popover that the user dismisses by tapping anywhere outside the popover,
rather than displaying the standard dismiss action.

On iOS, tvOS, and watchOS, confirmation dialogs only support controls with
labels that are `Text`. Passing any other type of view results in the content
being omitted.

## See Also

### Getting confirmation for an action

`func confirmationDialog<S, A>(S, isPresented: Binding<Bool>, titleVisibility:
Visibility, actions: () -> A) -> some View`

Presents a confirmation dialog when a given condition is true, using a string
variable as a title.

`func confirmationDialog<A>(Text, isPresented: Binding<Bool>, titleVisibility:
Visibility, actions: () -> A) -> some View`

Presents a confirmation dialog when a given condition is true, using a text
view for the title.

`func confirmationDialog<A>(LocalizedStringKey, isPresented: Binding<Bool>,
titleVisibility: Visibility, actions: () -> A) -> some View`

Presents a confirmation dialog when a given condition is true, using a
localized string key for the title.

`func confirmationDialog<A, T>(LocalizedStringKey, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A) -> some View`

Presents a confirmation dialog using data to produce the dialog’s content and
a localized string key for the title.

`func confirmationDialog<S, A, T>(S, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A) -> some View`

Presents a confirmation dialog using data to produce the dialog’s content and
a string variable for the title.

Instance Method

# confirmationDialog(_:isPresented:titleVisibility:presenting:actions:)

Presents a confirmation dialog using data to produce the dialog’s content and
a localized string key for the title.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func confirmationDialog<A, T>(
        _ titleKey: LocalizedStringKey,
        isPresented: Binding<Bool>,
        titleVisibility: Visibility = .automatic,
        presenting data: T?,
        @ViewBuilder actions: (T) -> A
    ) -> some View where A : View
    

##  Parameters

`titleKey`

    

The key for the localized string that describes the title of the dialog.

`isPresented`

    

A binding to a Boolean value that determines whether to present the dialog.
When the user presses or taps the dialog’s default action button, the system
sets this value to `false`, dismissing the dialog.

`titleVisibility`

    

The visibility of the dialog’s title. The default value is
`Visibility.automatic`.

`data`

    

An optional source of truth for the confirmation dialog. The system passes the
contents to the modifier’s closures. You use this data to populate the fields
of a confirmation dialog that you create that the system displays to the user.

`actions`

    

A view builder returning the dialog’s actions given the currently available
data.

## Discussion

In order for the interface to appear, both `isPresented` must be `true` and
`data` must not be `nil`. `data` should not change after the presentation
occurs. Any changes which occur after the presentation occurs will be ignored.

Use this method when you need to populate the fields of a confirmation dialog
with content from a data source. The example below shows a custom data source,
`FileDetails`, that provides data to populate the dialog:

This modifier creates a `Text` view for the title on your behalf, and treats
the localized key similar to `init(_:tableName:bundle:comment:)`. See `Text`
for more information about localizing strings.

All actions in a confirmation dialog will dismiss the dialog after the action
runs. The default button will be shown with greater prominence. You can
influence the default button by assigning it the `defaultAction` keyboard
shortcut.

The system may reorder the buttons based on their role and prominence.

Dialogs include a standard dismiss action by default. If you provide a button
with a role of `cancel`, that button takes the place of the default dismiss
action. You don’t have to dismiss the presentation with the cancel button’s
action.

Note

In regular size classes in iOS, the system renders confirmation dialogs as a
popover that the user dismisses by tapping anywhere outside the popover,
rather than displaying the standard dismiss action.

On iOS, tvOS, and watchOS, confirmation dialogs only support controls with
labels that are `Text`. Passing any other type of view results in the content
being omitted.

## See Also

### Getting confirmation for an action

`func confirmationDialog<S, A>(S, isPresented: Binding<Bool>, titleVisibility:
Visibility, actions: () -> A) -> some View`

Presents a confirmation dialog when a given condition is true, using a string
variable as a title.

`func confirmationDialog<A>(Text, isPresented: Binding<Bool>, titleVisibility:
Visibility, actions: () -> A) -> some View`

Presents a confirmation dialog when a given condition is true, using a text
view for the title.

`func confirmationDialog<A>(LocalizedStringKey, isPresented: Binding<Bool>,
titleVisibility: Visibility, actions: () -> A) -> some View`

Presents a confirmation dialog when a given condition is true, using a
localized string key for the title.

`func confirmationDialog<A, T>(Text, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A) -> some View`

Presents a confirmation dialog using data to produce the dialog’s content and
a text view for the title.

`func confirmationDialog<S, A, T>(S, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A) -> some View`

Presents a confirmation dialog using data to produce the dialog’s content and
a string variable for the title.

Instance Method

# confirmationDialog(_:isPresented:titleVisibility:presenting:actions:)

Presents a confirmation dialog using data to produce the dialog’s content and
a string variable for the title.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func confirmationDialog<S, A, T>(
        _ title: S,
        isPresented: Binding<Bool>,
        titleVisibility: Visibility = .automatic,
        presenting data: T?,
        @ViewBuilder actions: (T) -> A
    ) -> some View where S : StringProtocol, A : View
    

##  Parameters

`title`

    

A text string used as the title of the dialog.

`isPresented`

    

A binding to a Boolean value that determines whether to present the dialog.
When the user presses or taps the dialog’s default action button, the system
sets this value to `false`, dismissing the dialog.

`titleVisibility`

    

The visibility of the dialog’s title. The default value is
`Visibility.automatic`.

`data`

    

An optional source of truth for the confirmation dialog. The system passes the
contents to the modifier’s closures. You use this data to populate the fields
of a confirmation dialog that you create that the system displays to the user.

`actions`

    

A view builder returning the dialog’s actions given the currently available
data.

## Discussion

In order for the interface to appear, both `isPresented` must be `true` and
`data` must not be `nil`. `data` should not change after the presentation
occurs. Any changes which occur after the presentation occurs will be ignored.

Use this method when you need to populate the fields of a confirmation dialog
with content from a data source. The example below shows a custom data source,
`FileDetails`, that provides data to populate the dialog:

All actions in a confirmation dialog will dismiss the dialog after the action
runs. The default button will be shown with greater prominence. You can
influence the default button by assigning it the `defaultAction` keyboard
shortcut.

The system may reorder the buttons based on their role and prominence.

Dialogs include a standard dismiss action by default. If you provide a button
with a role of `cancel`, that button takes the place of the default dismiss
action. You don’t have to dismiss the presentation with the cancel button’s
action.

Note

In regular size classes in iOS, the system renders confirmation dialogs as a
popover that the user dismisses by tapping anywhere outside the popover,
rather than displaying the standard dismiss action.

On iOS, tvOS, and watchOS, confirmation dialogs only support controls with
labels that are `Text`. Passing any other type of view results in the content
being omitted.

## See Also

### Getting confirmation for an action

`func confirmationDialog<S, A>(S, isPresented: Binding<Bool>, titleVisibility:
Visibility, actions: () -> A) -> some View`

Presents a confirmation dialog when a given condition is true, using a string
variable as a title.

`func confirmationDialog<A>(Text, isPresented: Binding<Bool>, titleVisibility:
Visibility, actions: () -> A) -> some View`

Presents a confirmation dialog when a given condition is true, using a text
view for the title.

`func confirmationDialog<A>(LocalizedStringKey, isPresented: Binding<Bool>,
titleVisibility: Visibility, actions: () -> A) -> some View`

Presents a confirmation dialog when a given condition is true, using a
localized string key for the title.

`func confirmationDialog<A, T>(Text, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A) -> some View`

Presents a confirmation dialog using data to produce the dialog’s content and
a text view for the title.

`func confirmationDialog<A, T>(LocalizedStringKey, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A) -> some View`

Presents a confirmation dialog using data to produce the dialog’s content and
a localized string key for the title.

Instance Method

# confirmationDialog(_:isPresented:titleVisibility:actions:message:)

Presents a confirmation dialog with a message when a given condition is true,
using a string variable for the title.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func confirmationDialog<S, A, M>(
        _ title: S,
        isPresented: Binding<Bool>,
        titleVisibility: Visibility = .automatic,
        @ViewBuilder actions: () -> A,
        @ViewBuilder message: () -> M
    ) -> some View where S : StringProtocol, A : View, M : View
    

##  Parameters

`title`

    

A text string used as the title of the dialog.

`isPresented`

    

A binding to a Boolean value that determines whether to present the dialog.
When the user presses or taps the dialog’s default action button, the system
sets this value to `false`, dismissing the dialog.

`titleVisibility`

    

The visibility of the dialog’s title. The default value is
`Visibility.automatic`.

`actions`

    

A view builder returning the dialog’s actions.

`message`

    

A view builder returning the message for the dialog.

## Discussion

In the example below, a button conditionally presents a confirmation dialog
depending upon the value of a bound Boolean variable. When the Boolean value
is set to `true`, the system displays a confirmation dialog with a cancel
action and a destructive action.

All actions in a confirmation dialog will dismiss the dialog after the action
runs. The default button will be shown with greater prominence. You can
influence the default button by assigning it the `defaultAction` keyboard
shortcut.

The system may reorder the buttons based on their role and prominence.

Dialogs include a standard dismiss action by default. If you provide a button
with a role of `cancel`, that button takes the place of the default dismiss
action. You don’t have to dismiss the presentation with the cancel button’s
action.

Note

In regular size classes in iOS, the system renders confirmation dialogs as a
popover that the user dismisses by tapping anywhere outside the popover,
rather than displaying the standard dismiss action.

## See Also

### Showing a confirmation dialog with a message

`func confirmationDialog<A, M>(LocalizedStringKey, isPresented: Binding<Bool>,
titleVisibility: Visibility, actions: () -> A, message: () -> M) -> some View`

Presents a confirmation dialog with a message when a given condition is true,
using a localized string key for the title.

`func confirmationDialog<A, M>(Text, isPresented: Binding<Bool>,
titleVisibility: Visibility, actions: () -> A, message: () -> M) -> some View`

Presents a confirmation dialog with a message when a given condition is true,
using a text view for the title.

`func confirmationDialog<A, M, T>(Text, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A, message: (T)
-> M) -> some View`

Presents a confirmation dialog with a message using data to produce the
dialog’s content and a text view for the message.

`func confirmationDialog<S, A, M, T>(S, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A, message: (T)
-> M) -> some View`

Presents a confirmation dialog with a message using data to produce the
dialog’s content and a string variable for the title.

`func confirmationDialog<A, M, T>(LocalizedStringKey, isPresented:
Binding<Bool>, titleVisibility: Visibility, presenting: T?, actions: (T) -> A,
message: (T) -> M) -> some View`

Presents a confirmation dialog with a message using data to produce the
dialog’s content and a localized string key for the title.

Instance Method

# confirmationDialog(_:isPresented:titleVisibility:actions:message:)

Presents a confirmation dialog with a message when a given condition is true,
using a localized string key for the title.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func confirmationDialog<A, M>(
        _ titleKey: LocalizedStringKey,
        isPresented: Binding<Bool>,
        titleVisibility: Visibility = .automatic,
        @ViewBuilder actions: () -> A,
        @ViewBuilder message: () -> M
    ) -> some View where A : View, M : View
    

##  Parameters

`titleKey`

    

The key for the localized string that describes the title of the dialog.

`isPresented`

    

A binding to a Boolean value that determines whether to present the dialog.
When the user presses or taps the dialog’s default action button, the system
sets this value to `false`, dismissing the dialog.

`titleVisibility`

    

The visibility of the dialog’s title. The default value is
`Visibility.automatic`.

`actions`

    

A view builder returning the dialog’s actions.

`message`

    

A view builder returning the message for the dialog.

## Discussion

In the example below, a button conditionally presents a confirmation dialog
depending upon the value of a bound Boolean variable. When the Boolean value
is set to `true`, the system displays a confirmation dialog with a cancel
action and a destructive action.

All actions in a confirmation dialog will dismiss the dialog after the action
runs. The default button will be shown with greater prominence. You can
influence the default button by assigning it the `defaultAction` keyboard
shortcut.

The system may reorder the buttons based on their role and prominence.

Dialogs include a standard dismiss action by default. If you provide a button
with a role of `cancel`, that button takes the place of the default dismiss
action. You don’t have to dismiss the presentation with the cancel button’s
action.

Note

In regular size classes in iOS, the system renders confirmation dialogs as a
popover that the user dismisses by tapping anywhere outside the popover,
rather than displaying the standard dismiss action.

On iOS, tvOS, and watchOS, confirmation dialogs only support controls with
labels that are `Text`. Passing any other type of view results in the content
being omitted.

This modifier creates a `Text` view for the title on your behalf, and treats
the localized key similar to `init(_:tableName:bundle:comment:)`. See `Text`
for more information about localizing strings.

## See Also

### Showing a confirmation dialog with a message

`func confirmationDialog<S, A, M>(S, isPresented: Binding<Bool>,
titleVisibility: Visibility, actions: () -> A, message: () -> M) -> some View`

Presents a confirmation dialog with a message when a given condition is true,
using a string variable for the title.

`func confirmationDialog<A, M>(Text, isPresented: Binding<Bool>,
titleVisibility: Visibility, actions: () -> A, message: () -> M) -> some View`

Presents a confirmation dialog with a message when a given condition is true,
using a text view for the title.

`func confirmationDialog<A, M, T>(Text, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A, message: (T)
-> M) -> some View`

Presents a confirmation dialog with a message using data to produce the
dialog’s content and a text view for the message.

`func confirmationDialog<S, A, M, T>(S, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A, message: (T)
-> M) -> some View`

Presents a confirmation dialog with a message using data to produce the
dialog’s content and a string variable for the title.

`func confirmationDialog<A, M, T>(LocalizedStringKey, isPresented:
Binding<Bool>, titleVisibility: Visibility, presenting: T?, actions: (T) -> A,
message: (T) -> M) -> some View`

Presents a confirmation dialog with a message using data to produce the
dialog’s content and a localized string key for the title.

Instance Method

# confirmationDialog(_:isPresented:titleVisibility:actions:message:)

Presents a confirmation dialog with a message when a given condition is true,
using a text view for the title.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func confirmationDialog<A, M>(
        _ title: Text,
        isPresented: Binding<Bool>,
        titleVisibility: Visibility = .automatic,
        @ViewBuilder actions: () -> A,
        @ViewBuilder message: () -> M
    ) -> some View where A : View, M : View
    

##  Parameters

`title`

    

the title of the dialog.

`isPresented`

    

A binding to a Boolean value that determines whether to present the dialog.
When the user presses or taps the dialog’s default action button, the system
sets this value to `false`, dismissing the dialog.

`titleVisibility`

    

The visibility of the dialog’s title. The default value is
`Visibility.automatic`.

`actions`

    

A view builder returning the dialog’s actions.

`message`

    

A view builder returning the message for the dialog.

## Discussion

In the example below, a button conditionally presents a confirmation dialog
depending upon the value of a bound Boolean variable. When the Boolean value
is set to `true`, the system displays a confirmation dialog with a cancel
action and a destructive action.

All actions in a confirmation dialog will dismiss the dialog after the action
runs. The default button will be shown with greater prominence. You can
influence the default button by assigning it the `defaultAction` keyboard
shortcut.

The system may reorder the buttons based on their role and prominence.

Dialogs include a standard dismiss action by default. If you provide a button
with a role of `cancel`, that button takes the place of the default dismiss
action. You don’t have to dismiss the presentation with the cancel button’s
action.

Note

In regular size classes in iOS, the system renders confirmation dialogs as a
popover that the user dismisses by tapping anywhere outside the popover,
rather than displaying the standard dismiss action.

## See Also

### Showing a confirmation dialog with a message

`func confirmationDialog<S, A, M>(S, isPresented: Binding<Bool>,
titleVisibility: Visibility, actions: () -> A, message: () -> M) -> some View`

Presents a confirmation dialog with a message when a given condition is true,
using a string variable for the title.

`func confirmationDialog<A, M>(LocalizedStringKey, isPresented: Binding<Bool>,
titleVisibility: Visibility, actions: () -> A, message: () -> M) -> some View`

Presents a confirmation dialog with a message when a given condition is true,
using a localized string key for the title.

`func confirmationDialog<A, M, T>(Text, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A, message: (T)
-> M) -> some View`

Presents a confirmation dialog with a message using data to produce the
dialog’s content and a text view for the message.

`func confirmationDialog<S, A, M, T>(S, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A, message: (T)
-> M) -> some View`

Presents a confirmation dialog with a message using data to produce the
dialog’s content and a string variable for the title.

`func confirmationDialog<A, M, T>(LocalizedStringKey, isPresented:
Binding<Bool>, titleVisibility: Visibility, presenting: T?, actions: (T) -> A,
message: (T) -> M) -> some View`

Presents a confirmation dialog with a message using data to produce the
dialog’s content and a localized string key for the title.

Instance Method

#
confirmationDialog(_:isPresented:titleVisibility:presenting:actions:message:)

Presents a confirmation dialog with a message using data to produce the
dialog’s content and a text view for the message.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func confirmationDialog<A, M, T>(
        _ title: Text,
        isPresented: Binding<Bool>,
        titleVisibility: Visibility = .automatic,
        presenting data: T?,
        @ViewBuilder actions: (T) -> A,
        @ViewBuilder message: (T) -> M
    ) -> some View where A : View, M : View
    

##  Parameters

`title`

    

the title of the dialog.

`isPresented`

    

A binding to a Boolean value that determines whether to present the dialog.
When the user presses or taps the dialog’s default action button, the system
sets this value to `false`, dismissing the dialog.

`titleVisibility`

    

The visibility of the dialog’s title. The default value is
`Visibility.automatic`.

`data`

    

An optional source of truth for the confirmation dialog. The system passes the
contents to the modifier’s closures. You use this data to populate the fields
of a confirmation dialog that you create that the system displays to the user.

`actions`

    

A view builder returning the dialog’s actions given the currently available
data.

`message`

    

A view builder returning the message for the dialog given the currently
available data.

## Discussion

In order for the interface to appear, both `isPresented` must be `true` and
`data` must not be `nil`. `data` should not change after the presentation
occurs. Any changes which occur after the presentation occurs will be ignored.

Use this method when you need to populate the fields of a confirmation dialog
with content from a data source. The example below shows a custom data source,
`FileDetails`, that provides data to populate the dialog:

All actions in a confirmation dialog will dismiss the dialog after the action
runs. The default button will be shown with greater prominence. You can
influence the default button by assigning it the `defaultAction` keyboard
shortcut.

The system may reorder the buttons based on their role and prominence.

Dialogs include a standard dismiss action by default. If you provide a button
with a role of `cancel`, that button takes the place of the default dismiss
action. You don’t have to dismiss the presentation with the cancel button’s
action.

Note

In regular size classes in iOS, the system renders confirmation dialogs as a
popover that the user dismisses by tapping anywhere outside the popover,
rather than displaying the standard dismiss action.

On iOS, tvOS, and watchOS, confirmation dialogs only support controls with
labels that are `Text`. Passing any other type of view results in the content
being omitted.

## See Also

### Showing a confirmation dialog with a message

`func confirmationDialog<S, A, M>(S, isPresented: Binding<Bool>,
titleVisibility: Visibility, actions: () -> A, message: () -> M) -> some View`

Presents a confirmation dialog with a message when a given condition is true,
using a string variable for the title.

`func confirmationDialog<A, M>(LocalizedStringKey, isPresented: Binding<Bool>,
titleVisibility: Visibility, actions: () -> A, message: () -> M) -> some View`

Presents a confirmation dialog with a message when a given condition is true,
using a localized string key for the title.

`func confirmationDialog<A, M>(Text, isPresented: Binding<Bool>,
titleVisibility: Visibility, actions: () -> A, message: () -> M) -> some View`

Presents a confirmation dialog with a message when a given condition is true,
using a text view for the title.

`func confirmationDialog<S, A, M, T>(S, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A, message: (T)
-> M) -> some View`

Presents a confirmation dialog with a message using data to produce the
dialog’s content and a string variable for the title.

`func confirmationDialog<A, M, T>(LocalizedStringKey, isPresented:
Binding<Bool>, titleVisibility: Visibility, presenting: T?, actions: (T) -> A,
message: (T) -> M) -> some View`

Presents a confirmation dialog with a message using data to produce the
dialog’s content and a localized string key for the title.

Instance Method

#
confirmationDialog(_:isPresented:titleVisibility:presenting:actions:message:)

Presents a confirmation dialog with a message using data to produce the
dialog’s content and a string variable for the title.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func confirmationDialog<S, A, M, T>(
        _ title: S,
        isPresented: Binding<Bool>,
        titleVisibility: Visibility = .automatic,
        presenting data: T?,
        @ViewBuilder actions: (T) -> A,
        @ViewBuilder message: (T) -> M
    ) -> some View where S : StringProtocol, A : View, M : View
    

##  Parameters

`title`

    

A text string used as the title of the dialog.

`isPresented`

    

A binding to a Boolean value that determines whether to present the dialog.
When the user presses or taps the dialog’s default action button, the system
sets this value to `false`, dismissing the dialog.

`titleVisibility`

    

The visibility of the dialog’s title. The default value is
`Visibility.automatic`.

`data`

    

An optional source of truth for the confirmation dialog. The system passes the
contents to the modifier’s closures. You use this data to populate the fields
of a confirmation dialog that you create that the system displays to the user.

`actions`

    

A view builder returning the dialog’s actions given the currently available
data.

`message`

    

A view builder returning the message for the dialog given the currently
available data.

## Discussion

In order for the interface to appear, both `isPresented` must be `true` and
`data` must not be `nil`. `data` should not change after the presentation
occurs. Any changes which occur after the presentation occurs will be ignored.

Use this method when you need to populate the fields of a confirmation dialog
with content from a data source. The example below shows a custom data source,
`FileDetails`, that provides data to populate the dialog:

All actions in a confirmation dialog will dismiss the dialog after the action
runs. The default button will be shown with greater prominence. You can
influence the default button by assigning it the `defaultAction` keyboard
shortcut.

The system may reorder the buttons based on their role and prominence.

Dialogs include a standard dismiss action by default. If you provide a button
with a role of `cancel`, that button takes the place of the default dismiss
action. You don’t have to dismiss the presentation with the cancel button’s
action.

Note

In regular size classes in iOS, the system renders confirmation dialogs as a
popover that the user dismisses by tapping anywhere outside the popover,
rather than displaying the standard dismiss action.

On iOS, tvOS, and watchOS, confirmation dialogs only support controls with
labels that are `Text`. Passing any other type of view results in the content
being omitted.

## See Also

### Showing a confirmation dialog with a message

`func confirmationDialog<S, A, M>(S, isPresented: Binding<Bool>,
titleVisibility: Visibility, actions: () -> A, message: () -> M) -> some View`

Presents a confirmation dialog with a message when a given condition is true,
using a string variable for the title.

`func confirmationDialog<A, M>(LocalizedStringKey, isPresented: Binding<Bool>,
titleVisibility: Visibility, actions: () -> A, message: () -> M) -> some View`

Presents a confirmation dialog with a message when a given condition is true,
using a localized string key for the title.

`func confirmationDialog<A, M>(Text, isPresented: Binding<Bool>,
titleVisibility: Visibility, actions: () -> A, message: () -> M) -> some View`

Presents a confirmation dialog with a message when a given condition is true,
using a text view for the title.

`func confirmationDialog<A, M, T>(Text, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A, message: (T)
-> M) -> some View`

Presents a confirmation dialog with a message using data to produce the
dialog’s content and a text view for the message.

`func confirmationDialog<A, M, T>(LocalizedStringKey, isPresented:
Binding<Bool>, titleVisibility: Visibility, presenting: T?, actions: (T) -> A,
message: (T) -> M) -> some View`

Presents a confirmation dialog with a message using data to produce the
dialog’s content and a localized string key for the title.

Instance Method

#
confirmationDialog(_:isPresented:titleVisibility:presenting:actions:message:)

Presents a confirmation dialog with a message using data to produce the
dialog’s content and a localized string key for the title.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func confirmationDialog<A, M, T>(
        _ titleKey: LocalizedStringKey,
        isPresented: Binding<Bool>,
        titleVisibility: Visibility = .automatic,
        presenting data: T?,
        @ViewBuilder actions: (T) -> A,
        @ViewBuilder message: (T) -> M
    ) -> some View where A : View, M : View
    

##  Parameters

`titleKey`

    

The key for the localized string that describes the title of the dialog.

`isPresented`

    

A binding to a Boolean value that determines whether to present the dialog.
When the user presses or taps the dialog’s default action button, the system
sets this value to `false`, dismissing the dialog.

`titleVisibility`

    

The visibility of the dialog’s title. The default value is
`Visibility.automatic`.

`data`

    

An optional source of truth for the confirmation dialog. The system passes the
contents to the modifier’s closures. You use this data to populate the fields
of a confirmation dialog that you create that the system displays to the user.

`actions`

    

A view builder returning the dialog’s actions given the currently available
data.

`message`

    

A view builder returning the message for the dialog given the currently
available data.

## Discussion

In order for the interface to appear, both `isPresented` must be `true` and
`data` must not be `nil`. `data` should not change after the presentation
occurs. Any changes which occur after the presentation occurs will be ignored.

Use this method when you need to populate the fields of a confirmation dialog
with content from a data source. The example below shows a custom data source,
`FileDetails`, that provides data to populate the dialog:

This modifier creates a `Text` view for the title on your behalf, and treats
the localized key similar to `init(_:tableName:bundle:comment:)`. See `Text`
for more information about localizing strings.

All actions in a confirmation dialog will dismiss the dialog after the action
runs. The default button will be shown with greater prominence. You can
influence the default button by assigning it the `defaultAction` keyboard
shortcut.

The system may reorder the buttons based on their role and prominence.

Dialogs include a standard dismiss action by default. If you provide a button
with a role of `cancel`, that button takes the place of the default dismiss
action. You don’t have to dismiss the presentation with the cancel button’s
action.

Note

In regular size classes in iOS, the system renders confirmation dialogs as a
popover that the user dismisses by tapping anywhere outside the popover,
rather than displaying the standard dismiss action.

On iOS, tvOS, and watchOS, confirmation dialogs only support controls with
labels that are `Text`. Passing any other type of view results in the content
being omitted.

## See Also

### Showing a confirmation dialog with a message

`func confirmationDialog<S, A, M>(S, isPresented: Binding<Bool>,
titleVisibility: Visibility, actions: () -> A, message: () -> M) -> some View`

Presents a confirmation dialog with a message when a given condition is true,
using a string variable for the title.

`func confirmationDialog<A, M>(LocalizedStringKey, isPresented: Binding<Bool>,
titleVisibility: Visibility, actions: () -> A, message: () -> M) -> some View`

Presents a confirmation dialog with a message when a given condition is true,
using a localized string key for the title.

`func confirmationDialog<A, M>(Text, isPresented: Binding<Bool>,
titleVisibility: Visibility, actions: () -> A, message: () -> M) -> some View`

Presents a confirmation dialog with a message when a given condition is true,
using a text view for the title.

`func confirmationDialog<A, M, T>(Text, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A, message: (T)
-> M) -> some View`

Presents a confirmation dialog with a message using data to produce the
dialog’s content and a text view for the message.

`func confirmationDialog<S, A, M, T>(S, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A, message: (T)
-> M) -> some View`

Presents a confirmation dialog with a message using data to produce the
dialog’s content and a string variable for the title.

Instance Method

# dialogIcon(_:)

Configures the icon used by dialogs within this view.

iOS 17.0+  iPadOS 17.0+  macOS 13.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+

    
    
    func dialogIcon(_ icon: Image?) -> some View
    

##  Parameters

`icon`

    

The custom icon to use for confirmation dialogs and alerts. Passing `nil` will
use the default app icon.

## Discussion

On macOS, this icon replaces the default icon of the app.

On watchOS, this icon will be shown in any dialogs presented.

This modifier has no effect on other platforms.

The following example configures a `confirmationDialog` with a custom image.

## See Also

### Configuring a dialog

`func dialogSeverity(DialogSeverity) -> some View`

`func dialogSuppressionToggle(isSuppressed: Binding<Bool>) -> some View`

Enables user suppression of dialogs and alerts presented within `self`, with a
default suppression message on macOS. Unused on other platforms.

`func dialogSuppressionToggle<S>(S, isSuppressed: Binding<Bool>) -> some View`

Enables user suppression of dialogs and alerts presented within `self`, with a
custom suppression message on macOS. Unused on other platforms.

`func dialogSuppressionToggle(Text, isSuppressed: Binding<Bool>) -> some View`

Enables user suppression of dialogs and alerts presented within `self`, with a
custom suppression message on macOS. Unused on other platforms.

`func dialogSuppressionToggle(LocalizedStringKey, isSuppressed: Binding<Bool>)
-> some View`

Enables user suppression of dialogs and alerts presented within `self`, with a
custom suppression message on macOS. Unused on other platforms.

Instance Method

# dialogSeverity(_:)

macOS 13.0+  watchOS 10.0+  visionOS 1.0+

    
    
    func dialogSeverity(_ severity: DialogSeverity) -> some View
    

##  Parameters

`severity`

    

The severity to use for confirmation dialogs and alerts.

## See Also

### Configuring a dialog

`func dialogIcon(Image?) -> some View`

Configures the icon used by dialogs within this view.

`func dialogSuppressionToggle(isSuppressed: Binding<Bool>) -> some View`

Enables user suppression of dialogs and alerts presented within `self`, with a
default suppression message on macOS. Unused on other platforms.

`func dialogSuppressionToggle<S>(S, isSuppressed: Binding<Bool>) -> some View`

Enables user suppression of dialogs and alerts presented within `self`, with a
custom suppression message on macOS. Unused on other platforms.

`func dialogSuppressionToggle(Text, isSuppressed: Binding<Bool>) -> some View`

Enables user suppression of dialogs and alerts presented within `self`, with a
custom suppression message on macOS. Unused on other platforms.

`func dialogSuppressionToggle(LocalizedStringKey, isSuppressed: Binding<Bool>)
-> some View`

Enables user suppression of dialogs and alerts presented within `self`, with a
custom suppression message on macOS. Unused on other platforms.

Instance Method

# dialogSuppressionToggle(isSuppressed:)

Enables user suppression of dialogs and alerts presented within `self`, with a
default suppression message on macOS. Unused on other platforms.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func dialogSuppressionToggle(isSuppressed: Binding<Bool>) -> some View
    

##  Parameters

`isSuppressed`

    

Whether the suppression toggle is on or off in the dialog.

## Discussion

Applying dialog suppression adds a toggle to dialogs on macOS, which allows
the user to request the alert not be displayed again. Typically whether a
dialog is suppressed is stored in `AppStorage` and used to decide whether to
present the dialog in the future.

The following example configures a `confirmationDialog` with a suppression
toggle. The toggle’s state is stored in `AppStorage` and used to determine
whether or not to show the dialog when the “Delete Items” button is pressed.

## See Also

### Configuring a dialog

`func dialogIcon(Image?) -> some View`

Configures the icon used by dialogs within this view.

`func dialogSeverity(DialogSeverity) -> some View`

`func dialogSuppressionToggle<S>(S, isSuppressed: Binding<Bool>) -> some View`

Enables user suppression of dialogs and alerts presented within `self`, with a
custom suppression message on macOS. Unused on other platforms.

`func dialogSuppressionToggle(Text, isSuppressed: Binding<Bool>) -> some View`

Enables user suppression of dialogs and alerts presented within `self`, with a
custom suppression message on macOS. Unused on other platforms.

`func dialogSuppressionToggle(LocalizedStringKey, isSuppressed: Binding<Bool>)
-> some View`

Enables user suppression of dialogs and alerts presented within `self`, with a
custom suppression message on macOS. Unused on other platforms.

Instance Method

# dialogSuppressionToggle(_:isSuppressed:)

Enables user suppression of dialogs and alerts presented within `self`, with a
custom suppression message on macOS. Unused on other platforms.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func dialogSuppressionToggle<S>(
        _ title: S,
        isSuppressed: Binding<Bool>
    ) -> some View where S : StringProtocol
    

##  Parameters

`title`

    

The title of the suppression toggle in the dialog. This parameter can be
elided to use the default suppression title.

`isSuppressed`

    

Whether the suppression toggle is on or off in the dialog.

## Discussion

Applying dialog suppression adds a toggle to dialogs on macOS, which allows
the user to request the alert not be displayed again. Typically whether a
dialog is suppressed is stored in `AppStorage` and used to decide whether to
present the dialog in the future.

The following example configures a `confirmationDialog` with a suppression
toggle. The toggle’s state is stored in `AppStorage` and used to determine
whether or not to show the dialog when the “Delete Items” button is pressed.

## See Also

### Configuring a dialog

`func dialogIcon(Image?) -> some View`

Configures the icon used by dialogs within this view.

`func dialogSeverity(DialogSeverity) -> some View`

`func dialogSuppressionToggle(isSuppressed: Binding<Bool>) -> some View`

Enables user suppression of dialogs and alerts presented within `self`, with a
default suppression message on macOS. Unused on other platforms.

`func dialogSuppressionToggle(Text, isSuppressed: Binding<Bool>) -> some View`

Enables user suppression of dialogs and alerts presented within `self`, with a
custom suppression message on macOS. Unused on other platforms.

`func dialogSuppressionToggle(LocalizedStringKey, isSuppressed: Binding<Bool>)
-> some View`

Enables user suppression of dialogs and alerts presented within `self`, with a
custom suppression message on macOS. Unused on other platforms.

Instance Method

# dialogSuppressionToggle(_:isSuppressed:)

Enables user suppression of dialogs and alerts presented within `self`, with a
custom suppression message on macOS. Unused on other platforms.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func dialogSuppressionToggle(
        _ label: Text,
        isSuppressed: Binding<Bool>
    ) -> some View
    

##  Parameters

`label`

    

The label of the suppression toggle in the dialog. This parameter can be
elided to use the default suppression title.

`isSuppressed`

    

Whether the suppression toggle is on or off in the dialog.

## Discussion

Applying dialog suppression adds a toggle to dialogs on macOS, which allows
the user to request the alert not be displayed again. Typically whether a
dialog is suppressed is stored in `AppStorage` and used to decide whether to
present the dialog in the future.

The following example configures a `confirmationDialog` with a suppression
toggle. The toggle’s state is stored in `AppStorage` and used to determine
whether or not to show the dialog when the “Delete Items” button is pressed.

## See Also

### Configuring a dialog

`func dialogIcon(Image?) -> some View`

Configures the icon used by dialogs within this view.

`func dialogSeverity(DialogSeverity) -> some View`

`func dialogSuppressionToggle(isSuppressed: Binding<Bool>) -> some View`

Enables user suppression of dialogs and alerts presented within `self`, with a
default suppression message on macOS. Unused on other platforms.

`func dialogSuppressionToggle<S>(S, isSuppressed: Binding<Bool>) -> some View`

Enables user suppression of dialogs and alerts presented within `self`, with a
custom suppression message on macOS. Unused on other platforms.

`func dialogSuppressionToggle(LocalizedStringKey, isSuppressed: Binding<Bool>)
-> some View`

Enables user suppression of dialogs and alerts presented within `self`, with a
custom suppression message on macOS. Unused on other platforms.

Instance Method

# dialogSuppressionToggle(_:isSuppressed:)

Enables user suppression of dialogs and alerts presented within `self`, with a
custom suppression message on macOS. Unused on other platforms.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func dialogSuppressionToggle(
        _ titleKey: LocalizedStringKey,
        isSuppressed: Binding<Bool>
    ) -> some View
    

##  Parameters

`titleKey`

    

The title of the suppression toggle in the dialog. This parameter can be
elided to use the default suppression title.

`isSuppressed`

    

Whether the suppression toggle is on or off in the dialog.

## Discussion

Applying dialog suppression adds a toggle to dialogs on macOS, which allows
the user to request the alert not be displayed again. Typically whether a
dialog is suppressed is stored in `AppStorage` and used to decide whether to
present the dialog in the future.

The following example configures a `confirmationDialog` with a suppression
toggle. The toggle’s state is stored in `AppStorage` and used to determine
whether or not to show the dialog when the “Delete Items” button is pressed.

## See Also

### Configuring a dialog

`func dialogIcon(Image?) -> some View`

Configures the icon used by dialogs within this view.

`func dialogSeverity(DialogSeverity) -> some View`

`func dialogSuppressionToggle(isSuppressed: Binding<Bool>) -> some View`

Enables user suppression of dialogs and alerts presented within `self`, with a
default suppression message on macOS. Unused on other platforms.

`func dialogSuppressionToggle<S>(S, isSuppressed: Binding<Bool>) -> some View`

Enables user suppression of dialogs and alerts presented within `self`, with a
custom suppression message on macOS. Unused on other platforms.

`func dialogSuppressionToggle(Text, isSuppressed: Binding<Bool>) -> some View`

Enables user suppression of dialogs and alerts presented within `self`, with a
custom suppression message on macOS. Unused on other platforms.

Instance Method

# fileExporter(isPresented:document:contentType:defaultFilename:onCompletion:)

Presents a system interface for exporting a document that’s stored in a value
type, like a structure, to a file on disk.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    func fileExporter<D>(
        isPresented: Binding<Bool>,
        document: D?,
        contentType: UTType,
        defaultFilename: String? = nil,
        onCompletion: @escaping (Result<URL, any Error>) -> Void
    ) -> some View where D : FileDocument
    

##  Parameters

`isPresented`

    

A binding to whether the interface should be shown.

`document`

    

The in-memory document to export.

`contentType`

    

The content type to use for the exported file.

`defaultFilename`

    

If provided, the default name to use for the exported file, which will the
user will have an opportunity to edit prior to the export.

`onCompletion`

    

A callback that will be invoked when the operation has has succeeded or
failed.

`result`

    

A `Result` indicating whether the operation succeeded or failed.

## Discussion

In order for the interface to appear, both `isPresented` must be `true` and
`document` must not be `nil`. When the operation is finished, `isPresented`
will be set to `false` before `onCompletion` is called. If the user cancels
the operation, `isPresented` will be set to `false` and `onCompletion` will
not be called.

The `contentType` provided must be included within the document type’s
`writableContentTypes`, otherwise the first valid writable content type will
be used instead.

## See Also

### Exporting to file

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType:
UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void) -> some View`

Presents a system interface for exporting a document that’s stored in a
reference type, like a class, to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType:
UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for exporting a collection of value type documents
to files on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType:
UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for exporting a collection of reference type
documents to files on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system interface for allowing the user to export a `FileDocument`
to a file on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system dialog for allowing the user to export a
`ReferenceFileDocument` to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system dialog for allowing the user to export a collection of
documents that conform to `ReferenceFileDocument` to files on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system dialog for allowing the user to export a collection of
documents that conform to `FileDocument` to files on disk.

`func fileExporter<T>(isPresented: Binding<Bool>, item: T?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system interface allowing the user to export a `Transferable` item
to file on disk.

`func fileExporter<C, T>(isPresented: Binding<Bool>, items: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system interface allowing the user to export a collection of items
to files on disk.

`func fileExporterFilenameLabel(LocalizedStringKey) -> some View`

On macOS, configures the `fileExporter` with a label for the file name field.

`func fileExporterFilenameLabel(Text?) -> some View`

On macOS, configures the `fileExporter` with a text to use as a label for the
file name field.

`func fileExporterFilenameLabel<S>(S) -> some View`

On macOS, configures the `fileExporter` with a label for the file name field.

Instance Method

# fileExporter(isPresented:document:contentType:defaultFilename:onCompletion:)

Presents a system interface for exporting a document that’s stored in a
reference type, like a class, to a file on disk.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    func fileExporter<D>(
        isPresented: Binding<Bool>,
        document: D?,
        contentType: UTType,
        defaultFilename: String? = nil,
        onCompletion: @escaping (Result<URL, any Error>) -> Void
    ) -> some View where D : ReferenceFileDocument
    

##  Parameters

`isPresented`

    

A binding to whether the interface should be shown.

`document`

    

The in-memory document to export.

`contentType`

    

The content type to use for the exported file.

`defaultFilename`

    

If provided, the default name to use for the exported file, which will the
user will have an opportunity to edit prior to the export.

`onCompletion`

    

A callback that will be invoked when the operation has has succeeded or
failed.

`result`

    

A `Result` indicating whether the operation succeeded or failed.

## Discussion

In order for the interface to appear, both `isPresented` must be `true` and
`document` must not be `nil`. When the operation is finished, `isPresented`
will be set to `false` before `onCompletion` is called. If the user cancels
the operation, `isPresented` will be set to `false` and `onCompletion` will
not be called.

The `contentType` provided must be included within the document type’s
`writableContentTypes`, otherwise the first valid writable content type will
be used instead.

## See Also

### Exporting to file

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType:
UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void) -> some View`

Presents a system interface for exporting a document that’s stored in a value
type, like a structure, to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType:
UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for exporting a collection of value type documents
to files on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType:
UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for exporting a collection of reference type
documents to files on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system interface for allowing the user to export a `FileDocument`
to a file on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system dialog for allowing the user to export a
`ReferenceFileDocument` to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system dialog for allowing the user to export a collection of
documents that conform to `ReferenceFileDocument` to files on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system dialog for allowing the user to export a collection of
documents that conform to `FileDocument` to files on disk.

`func fileExporter<T>(isPresented: Binding<Bool>, item: T?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system interface allowing the user to export a `Transferable` item
to file on disk.

`func fileExporter<C, T>(isPresented: Binding<Bool>, items: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system interface allowing the user to export a collection of items
to files on disk.

`func fileExporterFilenameLabel(LocalizedStringKey) -> some View`

On macOS, configures the `fileExporter` with a label for the file name field.

`func fileExporterFilenameLabel(Text?) -> some View`

On macOS, configures the `fileExporter` with a text to use as a label for the
file name field.

`func fileExporterFilenameLabel<S>(S) -> some View`

On macOS, configures the `fileExporter` with a label for the file name field.

Instance Method

# fileExporter(isPresented:documents:contentType:onCompletion:)

Presents a system interface for exporting a collection of value type documents
to files on disk.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    func fileExporter<C>(
        isPresented: Binding<Bool>,
        documents: C,
        contentType: UTType,
        onCompletion: @escaping (Result<[URL], any Error>) -> Void
    ) -> some View where C : Collection, C.Element : FileDocument
    

##  Parameters

`isPresented`

    

A binding to whether the interface should be shown.

`documents`

    

The collection of in-memory documents to export.

`contentType`

    

The content type to use for the exported file.

`onCompletion`

    

A callback that will be invoked when the operation has has succeeded or
failed.

`result`

    

A `Result` indicating whether the operation succeeded or failed.

## Discussion

In order for the interface to appear, both `isPresented` must be `true` and
`documents` must not be empty. When the operation is finished, `isPresented`
will be set to `false` before `onCompletion` is called. If the user cancels
the operation, `isPresented` will be set to `false` and `onCompletion` will
not be called.

The `contentType` provided must be included within the document type’s
`writableContentTypes`, otherwise the first valid writable content type will
be used instead.

## See Also

### Exporting to file

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType:
UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void) -> some View`

Presents a system interface for exporting a document that’s stored in a value
type, like a structure, to a file on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType:
UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void) -> some View`

Presents a system interface for exporting a document that’s stored in a
reference type, like a class, to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType:
UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for exporting a collection of reference type
documents to files on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system interface for allowing the user to export a `FileDocument`
to a file on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system dialog for allowing the user to export a
`ReferenceFileDocument` to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system dialog for allowing the user to export a collection of
documents that conform to `ReferenceFileDocument` to files on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system dialog for allowing the user to export a collection of
documents that conform to `FileDocument` to files on disk.

`func fileExporter<T>(isPresented: Binding<Bool>, item: T?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system interface allowing the user to export a `Transferable` item
to file on disk.

`func fileExporter<C, T>(isPresented: Binding<Bool>, items: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system interface allowing the user to export a collection of items
to files on disk.

`func fileExporterFilenameLabel(LocalizedStringKey) -> some View`

On macOS, configures the `fileExporter` with a label for the file name field.

`func fileExporterFilenameLabel(Text?) -> some View`

On macOS, configures the `fileExporter` with a text to use as a label for the
file name field.

`func fileExporterFilenameLabel<S>(S) -> some View`

On macOS, configures the `fileExporter` with a label for the file name field.

Instance Method

# fileExporter(isPresented:documents:contentType:onCompletion:)

Presents a system interface for exporting a collection of reference type
documents to files on disk.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    func fileExporter<C>(
        isPresented: Binding<Bool>,
        documents: C,
        contentType: UTType,
        onCompletion: @escaping (Result<[URL], any Error>) -> Void
    ) -> some View where C : Collection, C.Element : ReferenceFileDocument
    

##  Parameters

`isPresented`

    

A binding to whether the interface should be shown.

`documents`

    

The collection of in-memory documents to export.

`contentType`

    

The content type to use for the exported file.

`onCompletion`

    

A callback that will be invoked when the operation has has succeeded or
failed.

`result`

    

A `Result` indicating whether the operation succeeded or failed.

## Discussion

In order for the interface to appear, both `isPresented` must be `true` and
`documents` must not be empty. When the operation is finished, `isPresented`
will be set to `false` before `onCompletion` is called. If the user cancels
the operation, `isPresented` will be set to `false` and `onCompletion` will
not be called.

The `contentType` provided must be included within the document type’s
`writableContentTypes`, otherwise the first valid writable content type will
be used instead.

## See Also

### Exporting to file

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType:
UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void) -> some View`

Presents a system interface for exporting a document that’s stored in a value
type, like a structure, to a file on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType:
UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void) -> some View`

Presents a system interface for exporting a document that’s stored in a
reference type, like a class, to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType:
UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for exporting a collection of value type documents
to files on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system interface for allowing the user to export a `FileDocument`
to a file on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system dialog for allowing the user to export a
`ReferenceFileDocument` to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system dialog for allowing the user to export a collection of
documents that conform to `ReferenceFileDocument` to files on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system dialog for allowing the user to export a collection of
documents that conform to `FileDocument` to files on disk.

`func fileExporter<T>(isPresented: Binding<Bool>, item: T?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system interface allowing the user to export a `Transferable` item
to file on disk.

`func fileExporter<C, T>(isPresented: Binding<Bool>, items: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system interface allowing the user to export a collection of items
to files on disk.

`func fileExporterFilenameLabel(LocalizedStringKey) -> some View`

On macOS, configures the `fileExporter` with a label for the file name field.

`func fileExporterFilenameLabel(Text?) -> some View`

On macOS, configures the `fileExporter` with a text to use as a label for the
file name field.

`func fileExporterFilenameLabel<S>(S) -> some View`

On macOS, configures the `fileExporter` with a label for the file name field.

Instance Method

#
fileExporter(isPresented:document:contentTypes:defaultFilename:onCompletion:onCancellation:)

Presents a system interface for allowing the user to export a `FileDocument`
to a file on disk.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func fileExporter<D>(
        isPresented: Binding<Bool>,
        document: D?,
        contentTypes: [UTType] = [],
        defaultFilename: String? = nil,
        onCompletion: @escaping (Result<URL, any Error>) -> Void,
        onCancellation: @escaping () -> Void = {}
    ) -> some View where D : FileDocument
    

##  Parameters

`isPresented`

    

A binding to whether the interface should be shown.

`document`

    

The in-memory document to export.

`contentTypes`

    

The list of supported content types which can be exported. If not provided,
`FileDocument.writableContentTypes` are used.

`defaultFilename`

    

If provided, the default name to use for the exported file, which will the
user will have an opportunity to edit prior to the export.

`onCompletion`

    

A callback that will be invoked when the operation has succeeded or failed.
The `result` indicates whether the operation succeeded or failed.

`onCancellation`

    

A callback that will be invoked if the user cancels the operation.

## Discussion

In order for the interface to appear, `isPresented` must be `true`. When the
operation is finished, `isPresented` will be set to `false` before
`onCompletion` is called. If the user cancels the operation, `isPresented`
will be set to `false` and `onCancellation` will be called.

## See Also

### Exporting to file

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType:
UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void) -> some View`

Presents a system interface for exporting a document that’s stored in a value
type, like a structure, to a file on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType:
UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void) -> some View`

Presents a system interface for exporting a document that’s stored in a
reference type, like a class, to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType:
UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for exporting a collection of value type documents
to files on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType:
UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for exporting a collection of reference type
documents to files on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system dialog for allowing the user to export a
`ReferenceFileDocument` to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system dialog for allowing the user to export a collection of
documents that conform to `ReferenceFileDocument` to files on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system dialog for allowing the user to export a collection of
documents that conform to `FileDocument` to files on disk.

`func fileExporter<T>(isPresented: Binding<Bool>, item: T?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system interface allowing the user to export a `Transferable` item
to file on disk.

`func fileExporter<C, T>(isPresented: Binding<Bool>, items: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system interface allowing the user to export a collection of items
to files on disk.

`func fileExporterFilenameLabel(LocalizedStringKey) -> some View`

On macOS, configures the `fileExporter` with a label for the file name field.

`func fileExporterFilenameLabel(Text?) -> some View`

On macOS, configures the `fileExporter` with a text to use as a label for the
file name field.

`func fileExporterFilenameLabel<S>(S) -> some View`

On macOS, configures the `fileExporter` with a label for the file name field.

Instance Method

#
fileExporter(isPresented:document:contentTypes:defaultFilename:onCompletion:onCancellation:)

Presents a system dialog for allowing the user to export a
`ReferenceFileDocument` to a file on disk.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func fileExporter<D>(
        isPresented: Binding<Bool>,
        document: D?,
        contentTypes: [UTType] = [],
        defaultFilename: String? = nil,
        onCompletion: @escaping (Result<URL, any Error>) -> Void,
        onCancellation: @escaping () -> Void = {}
    ) -> some View where D : ReferenceFileDocument
    

##  Parameters

`isPresented`

    

A binding to whether the dialog should be shown.

`document`

    

The in-memory document to export.

`contentTypes`

    

The list of supported content types which can be exported. If not provided,
`ReferenceFileDocument.writableContentTypes` are used.

`defaultFilename`

    

If provided, the default name to use for the exported file, which will the
user will have an opportunity to edit prior to the export.

`onCompletion`

    

A callback that will be invoked when the operation has succeeded or failed.
The `result` indicates whether the operation succeeded or failed.

`onCancellation`

    

A callback that will be invoked if the user cancels the operation.

## Discussion

In order for the dialog to appear, `isPresented` must be `true`. When the
operation is finished, `isPresented` will be set to `false` before
`onCompletion` is called. If the user cancels the operation, `isPresented`
will be set to `false` and `onCancellation` will be called.

## See Also

### Exporting to file

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType:
UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void) -> some View`

Presents a system interface for exporting a document that’s stored in a value
type, like a structure, to a file on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType:
UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void) -> some View`

Presents a system interface for exporting a document that’s stored in a
reference type, like a class, to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType:
UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for exporting a collection of value type documents
to files on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType:
UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for exporting a collection of reference type
documents to files on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system interface for allowing the user to export a `FileDocument`
to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system dialog for allowing the user to export a collection of
documents that conform to `ReferenceFileDocument` to files on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system dialog for allowing the user to export a collection of
documents that conform to `FileDocument` to files on disk.

`func fileExporter<T>(isPresented: Binding<Bool>, item: T?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system interface allowing the user to export a `Transferable` item
to file on disk.

`func fileExporter<C, T>(isPresented: Binding<Bool>, items: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system interface allowing the user to export a collection of items
to files on disk.

`func fileExporterFilenameLabel(LocalizedStringKey) -> some View`

On macOS, configures the `fileExporter` with a label for the file name field.

`func fileExporterFilenameLabel(Text?) -> some View`

On macOS, configures the `fileExporter` with a text to use as a label for the
file name field.

`func fileExporterFilenameLabel<S>(S) -> some View`

On macOS, configures the `fileExporter` with a label for the file name field.

Instance Method

#
fileExporter(isPresented:documents:contentTypes:onCompletion:onCancellation:)

Presents a system dialog for allowing the user to export a collection of
documents that conform to `ReferenceFileDocument` to files on disk.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func fileExporter<C>(
        isPresented: Binding<Bool>,
        documents: C,
        contentTypes: [UTType] = [],
        onCompletion: @escaping (Result<[URL], any Error>) -> Void,
        onCancellation: @escaping () -> Void = {}
    ) -> some View where C : Collection, C.Element : ReferenceFileDocument
    

##  Parameters

`isPresented`

    

A binding to whether the dialog should be shown.

`documents`

    

The in-memory documents to export.

`contentTypes`

    

The list of supported content types which can be exported. If not provided,
`ReferenceFileDocument.writableContentTypes` are used.

`onCompletion`

    

A callback that will be invoked when the operation has succeeded or failed.
The `result` indicates whether the operation succeeded or failed.

`onCancellation`

    

A callback that will be invoked if the user cancels the operation.

## Discussion

In order for the dialog to appear, `isPresented` must be `true`. When the
operation is finished, `isPresented` will be set to `false` before
`onCompletion` is called. If the user cancels the operation, `isPresented`
will be set to `false` and `onCancellation` will be called.

## See Also

### Exporting to file

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType:
UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void) -> some View`

Presents a system interface for exporting a document that’s stored in a value
type, like a structure, to a file on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType:
UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void) -> some View`

Presents a system interface for exporting a document that’s stored in a
reference type, like a class, to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType:
UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for exporting a collection of value type documents
to files on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType:
UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for exporting a collection of reference type
documents to files on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system interface for allowing the user to export a `FileDocument`
to a file on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system dialog for allowing the user to export a
`ReferenceFileDocument` to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system dialog for allowing the user to export a collection of
documents that conform to `FileDocument` to files on disk.

`func fileExporter<T>(isPresented: Binding<Bool>, item: T?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system interface allowing the user to export a `Transferable` item
to file on disk.

`func fileExporter<C, T>(isPresented: Binding<Bool>, items: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system interface allowing the user to export a collection of items
to files on disk.

`func fileExporterFilenameLabel(LocalizedStringKey) -> some View`

On macOS, configures the `fileExporter` with a label for the file name field.

`func fileExporterFilenameLabel(Text?) -> some View`

On macOS, configures the `fileExporter` with a text to use as a label for the
file name field.

`func fileExporterFilenameLabel<S>(S) -> some View`

On macOS, configures the `fileExporter` with a label for the file name field.

Instance Method

#
fileExporter(isPresented:documents:contentTypes:onCompletion:onCancellation:)

Presents a system dialog for allowing the user to export a collection of
documents that conform to `FileDocument` to files on disk.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func fileExporter<C>(
        isPresented: Binding<Bool>,
        documents: C,
        contentTypes: [UTType] = [],
        onCompletion: @escaping (Result<[URL], any Error>) -> Void,
        onCancellation: @escaping () -> Void = {}
    ) -> some View where C : Collection, C.Element : FileDocument
    

##  Parameters

`isPresented`

    

A binding to whether the dialog should be shown.

`documents`

    

The in-memory documents to export.

`contentTypes`

    

The list of supported content types which can be exported. If not provided,
`FileDocument.writableContentTypes` are used.

`onCompletion`

    

A callback that will be invoked when the operation has succeeded or failed.
The `result` indicates whether the operation succeeded or failed.

`onCancellation`

    

A callback that will be invoked if the user cancels the operation.

## Discussion

In order for the dialog to appear, `isPresented` must be `true`. When the
operation is finished, `isPresented` will be set to `false` before
`onCompletion` is called. If the user cancels the operation, `isPresented`
will be set to `false` and `onCancellation` will be called.

## See Also

### Exporting to file

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType:
UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void) -> some View`

Presents a system interface for exporting a document that’s stored in a value
type, like a structure, to a file on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType:
UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void) -> some View`

Presents a system interface for exporting a document that’s stored in a
reference type, like a class, to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType:
UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for exporting a collection of value type documents
to files on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType:
UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for exporting a collection of reference type
documents to files on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system interface for allowing the user to export a `FileDocument`
to a file on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system dialog for allowing the user to export a
`ReferenceFileDocument` to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system dialog for allowing the user to export a collection of
documents that conform to `ReferenceFileDocument` to files on disk.

`func fileExporter<T>(isPresented: Binding<Bool>, item: T?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system interface allowing the user to export a `Transferable` item
to file on disk.

`func fileExporter<C, T>(isPresented: Binding<Bool>, items: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system interface allowing the user to export a collection of items
to files on disk.

`func fileExporterFilenameLabel(LocalizedStringKey) -> some View`

On macOS, configures the `fileExporter` with a label for the file name field.

`func fileExporterFilenameLabel(Text?) -> some View`

On macOS, configures the `fileExporter` with a text to use as a label for the
file name field.

`func fileExporterFilenameLabel<S>(S) -> some View`

On macOS, configures the `fileExporter` with a label for the file name field.

Instance Method

#
fileExporter(isPresented:item:contentTypes:defaultFilename:onCompletion:onCancellation:)

Presents a system interface allowing the user to export a `Transferable` item
to file on disk.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func fileExporter<T>(
        isPresented: Binding<Bool>,
        item: T?,
        contentTypes: [UTType] = [],
        defaultFilename: String? = nil,
        onCompletion: @escaping (Result<URL, any Error>) -> Void,
        onCancellation: @escaping () -> Void = { }
    ) -> some View where T : Transferable
    

##  Parameters

`isPresented`

    

A binding to whether the interface should be shown.

`item`

    

The item to be saved on disk.

`contentTypes`

    

The optional content types to use for the exported file. If empty, SwiftUI
uses the content types from the `transferRepresentation` property provided for
`Transferable` conformance.

`onCompletion`

    

A callback that will be invoked when the operation has succeeded or failed.

`onCancellation`

    

A callback that will be invoked if the operation was cancelled.

## Discussion

In order for the interface to appear `isPresented` must be set to `true`. When
the operation is finished, `isPresented` will be set to `false` before
`onCompletion` is called. If the user cancels the operation, `isPresented`
will be set to `false` and `onCompletion` will not be called.

## See Also

### Exporting to file

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType:
UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void) -> some View`

Presents a system interface for exporting a document that’s stored in a value
type, like a structure, to a file on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType:
UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void) -> some View`

Presents a system interface for exporting a document that’s stored in a
reference type, like a class, to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType:
UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for exporting a collection of value type documents
to files on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType:
UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for exporting a collection of reference type
documents to files on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system interface for allowing the user to export a `FileDocument`
to a file on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system dialog for allowing the user to export a
`ReferenceFileDocument` to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system dialog for allowing the user to export a collection of
documents that conform to `ReferenceFileDocument` to files on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system dialog for allowing the user to export a collection of
documents that conform to `FileDocument` to files on disk.

`func fileExporter<C, T>(isPresented: Binding<Bool>, items: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system interface allowing the user to export a collection of items
to files on disk.

`func fileExporterFilenameLabel(LocalizedStringKey) -> some View`

On macOS, configures the `fileExporter` with a label for the file name field.

`func fileExporterFilenameLabel(Text?) -> some View`

On macOS, configures the `fileExporter` with a text to use as a label for the
file name field.

`func fileExporterFilenameLabel<S>(S) -> some View`

On macOS, configures the `fileExporter` with a label for the file name field.

Instance Method

# fileExporter(isPresented:items:contentTypes:onCompletion:onCancellation:)

Presents a system interface allowing the user to export a collection of items
to files on disk.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func fileExporter<C, T>(
        isPresented: Binding<Bool>,
        items: C,
        contentTypes: [UTType] = [],
        onCompletion: @escaping (Result<[URL], any Error>) -> Void,
        onCancellation: @escaping () -> Void = { }
    ) -> some View where C : Collection, T : Transferable, T == C.Element
    

##  Parameters

`isPresented`

    

A binding to whether the interface should be shown.

`items`

    

Collection of values to be saved on disk.

`contentTypes`

    

The content types to use for the exported file. If empty, SwiftUI uses the
content types from the `transferRepresentation` property provided for
`Transferable` conformance.

`allowsOtherContentTypes`

    

A Boolean value that indicates if the users are allowed to save the files with
a different file extension than specified by the `contentType` property.

`onCompletion`

    

A callback that will be invoked when the operation has has succeeded or
failed.

`onCancellation`

    

A callback that will be invoked if the operation was cancelled.

## Discussion

In order for the interface to appear `isPresented` must be set to `true`. When
the operation is finished, `isPresented` will be set to `false` before
`onCompletion` is called. If the user cancels the operation, `isPresented`
will be set to `false` and `onCompletion` will not be called.

## See Also

### Exporting to file

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType:
UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void) -> some View`

Presents a system interface for exporting a document that’s stored in a value
type, like a structure, to a file on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType:
UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void) -> some View`

Presents a system interface for exporting a document that’s stored in a
reference type, like a class, to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType:
UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for exporting a collection of value type documents
to files on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType:
UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for exporting a collection of reference type
documents to files on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system interface for allowing the user to export a `FileDocument`
to a file on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system dialog for allowing the user to export a
`ReferenceFileDocument` to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system dialog for allowing the user to export a collection of
documents that conform to `ReferenceFileDocument` to files on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system dialog for allowing the user to export a collection of
documents that conform to `FileDocument` to files on disk.

`func fileExporter<T>(isPresented: Binding<Bool>, item: T?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system interface allowing the user to export a `Transferable` item
to file on disk.

`func fileExporterFilenameLabel(LocalizedStringKey) -> some View`

On macOS, configures the `fileExporter` with a label for the file name field.

`func fileExporterFilenameLabel(Text?) -> some View`

On macOS, configures the `fileExporter` with a text to use as a label for the
file name field.

`func fileExporterFilenameLabel<S>(S) -> some View`

On macOS, configures the `fileExporter` with a label for the file name field.

Instance Method

# fileExporterFilenameLabel(_:)

On macOS, configures the `fileExporter` with a label for the file name field.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func fileExporterFilenameLabel(_ labelKey: LocalizedStringKey) -> some View
    

##  Parameters

`labelKey`

    

The key to a localized string to display.

## See Also

### Exporting to file

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType:
UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void) -> some View`

Presents a system interface for exporting a document that’s stored in a value
type, like a structure, to a file on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType:
UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void) -> some View`

Presents a system interface for exporting a document that’s stored in a
reference type, like a class, to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType:
UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for exporting a collection of value type documents
to files on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType:
UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for exporting a collection of reference type
documents to files on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system interface for allowing the user to export a `FileDocument`
to a file on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system dialog for allowing the user to export a
`ReferenceFileDocument` to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system dialog for allowing the user to export a collection of
documents that conform to `ReferenceFileDocument` to files on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system dialog for allowing the user to export a collection of
documents that conform to `FileDocument` to files on disk.

`func fileExporter<T>(isPresented: Binding<Bool>, item: T?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system interface allowing the user to export a `Transferable` item
to file on disk.

`func fileExporter<C, T>(isPresented: Binding<Bool>, items: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system interface allowing the user to export a collection of items
to files on disk.

`func fileExporterFilenameLabel(Text?) -> some View`

On macOS, configures the `fileExporter` with a text to use as a label for the
file name field.

`func fileExporterFilenameLabel<S>(S) -> some View`

On macOS, configures the `fileExporter` with a label for the file name field.

Instance Method

# fileExporterFilenameLabel(_:)

On macOS, configures the `fileExporter` with a text to use as a label for the
file name field.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func fileExporterFilenameLabel(_ label: Text?) -> some View
    

##  Parameters

`label`

    

The optional text to use as the label for the file name field.

## See Also

### Exporting to file

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType:
UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void) -> some View`

Presents a system interface for exporting a document that’s stored in a value
type, like a structure, to a file on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType:
UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void) -> some View`

Presents a system interface for exporting a document that’s stored in a
reference type, like a class, to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType:
UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for exporting a collection of value type documents
to files on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType:
UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for exporting a collection of reference type
documents to files on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system interface for allowing the user to export a `FileDocument`
to a file on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system dialog for allowing the user to export a
`ReferenceFileDocument` to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system dialog for allowing the user to export a collection of
documents that conform to `ReferenceFileDocument` to files on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system dialog for allowing the user to export a collection of
documents that conform to `FileDocument` to files on disk.

`func fileExporter<T>(isPresented: Binding<Bool>, item: T?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system interface allowing the user to export a `Transferable` item
to file on disk.

`func fileExporter<C, T>(isPresented: Binding<Bool>, items: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system interface allowing the user to export a collection of items
to files on disk.

`func fileExporterFilenameLabel(LocalizedStringKey) -> some View`

On macOS, configures the `fileExporter` with a label for the file name field.

`func fileExporterFilenameLabel<S>(S) -> some View`

On macOS, configures the `fileExporter` with a label for the file name field.

Instance Method

# fileExporterFilenameLabel(_:)

On macOS, configures the `fileExporter` with a label for the file name field.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func fileExporterFilenameLabel<S>(_ label: S) -> some View where S : StringProtocol
    

##  Parameters

`label`

    

The string to use as the label for the file name field.

## See Also

### Exporting to file

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType:
UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void) -> some View`

Presents a system interface for exporting a document that’s stored in a value
type, like a structure, to a file on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType:
UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void) -> some View`

Presents a system interface for exporting a document that’s stored in a
reference type, like a class, to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType:
UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for exporting a collection of value type documents
to files on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType:
UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for exporting a collection of reference type
documents to files on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system interface for allowing the user to export a `FileDocument`
to a file on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system dialog for allowing the user to export a
`ReferenceFileDocument` to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system dialog for allowing the user to export a collection of
documents that conform to `ReferenceFileDocument` to files on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system dialog for allowing the user to export a collection of
documents that conform to `FileDocument` to files on disk.

`func fileExporter<T>(isPresented: Binding<Bool>, item: T?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system interface allowing the user to export a `Transferable` item
to file on disk.

`func fileExporter<C, T>(isPresented: Binding<Bool>, items: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system interface allowing the user to export a collection of items
to files on disk.

`func fileExporterFilenameLabel(LocalizedStringKey) -> some View`

On macOS, configures the `fileExporter` with a label for the file name field.

`func fileExporterFilenameLabel(Text?) -> some View`

On macOS, configures the `fileExporter` with a text to use as a label for the
file name field.

Instance Method

#
fileImporter(isPresented:allowedContentTypes:allowsMultipleSelection:onCompletion:)

Presents a system interface for allowing the user to import multiple files.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    func fileImporter(
        isPresented: Binding<Bool>,
        allowedContentTypes: [UTType],
        allowsMultipleSelection: Bool,
        onCompletion: @escaping (Result<[URL], any Error>) -> Void
    ) -> some View
    

##  Parameters

`isPresented`

    

A binding to whether the interface should be shown.

`allowedContentTypes`

    

The list of supported content types which can be imported.

`allowsMultipleSelection`

    

Whether the importer allows the user to select more than one file to import.

`onCompletion`

    

A callback that will be invoked when the operation has succeeded or failed. To
access the received URLs, call `startAccessingSecurityScopedResource`. When
the access is no longer required, call `stopAccessingSecurityScopedResource`.

`result`

    

A `Result` indicating whether the operation succeeded or failed.

## Discussion

In order for the interface to appear, `isPresented` must be `true`. When the
operation is finished, `isPresented` will be set to `false` before
`onCompletion` is called. If the user cancels the operation, `isPresented`
will be set to `false` and `onCompletion` will not be called.

Note

This dialog provides security-scoped URLs. Call the
`startAccessingSecurityScopedResource` method to access or bookmark the URLs,
and the `stopAccessingSecurityScopedResource` method to release the access.

For example, a button that allows the user to choose multiple PDF files for
the application to combine them later, might look like this:

Note

Changing `allowedContentTypes` or `allowsMultipleSelection` while the file
importer is presented will have no immediate effect, however will apply the
next time it is presented.

## See Also

### Importing from file

`func fileImporter(isPresented: Binding<Bool>, allowedContentTypes: [UTType],
onCompletion: (Result<URL, any Error>) -> Void) -> some View`

Presents a system interface for allowing the user to import an existing file.

`func fileImporter(isPresented: Binding<Bool>, allowedContentTypes: [UTType],
allowsMultipleSelection: Bool, onCompletion: (Result<[URL], any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system dialog for allowing the user to import multiple files.

Instance Method

# fileImporter(isPresented:allowedContentTypes:onCompletion:)

Presents a system interface for allowing the user to import an existing file.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    func fileImporter(
        isPresented: Binding<Bool>,
        allowedContentTypes: [UTType],
        onCompletion: @escaping (Result<URL, any Error>) -> Void
    ) -> some View
    

##  Parameters

`isPresented`

    

A binding to whether the interface should be shown.

`allowedContentTypes`

    

The list of supported content types which can be imported.

`onCompletion`

    

A callback that will be invoked when the operation has succeeded or failed. To
access the received URLs, call `startAccessingSecurityScopedResource`. When
the access is no longer required, call `stopAccessingSecurityScopedResource`.

`result`

    

A `Result` indicating whether the operation succeeded or failed.

## Discussion

In order for the interface to appear, `isPresented` must be `true`. When the
operation is finished, `isPresented` will be set to `false` before
`onCompletion` is called. If the user cancels the operation, `isPresented`
will be set to `false` and `onCompletion` will not be called.

Note

This dialog provides security-scoped URLs. Call the
`startAccessingSecurityScopedResource` method to access or bookmark the URLs,
and the `stopAccessingSecurityScopedResource` method to release the access.

For example, an application can have a button that allows the user to choose
the default directory with document templates loaded on every launch. Such a
button might look like this:

Note

Changing `allowedContentTypes` while the file importer is presented will have
no immediate effect, however will apply the next time it is presented.

## See Also

### Importing from file

`func fileImporter(isPresented: Binding<Bool>, allowedContentTypes: [UTType],
allowsMultipleSelection: Bool, onCompletion: (Result<[URL], any Error>) ->
Void) -> some View`

Presents a system interface for allowing the user to import multiple files.

`func fileImporter(isPresented: Binding<Bool>, allowedContentTypes: [UTType],
allowsMultipleSelection: Bool, onCompletion: (Result<[URL], any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system dialog for allowing the user to import multiple files.

Instance Method

#
fileImporter(isPresented:allowedContentTypes:allowsMultipleSelection:onCompletion:onCancellation:)

Presents a system dialog for allowing the user to import multiple files.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func fileImporter(
        isPresented: Binding<Bool>,
        allowedContentTypes: [UTType],
        allowsMultipleSelection: Bool,
        onCompletion: @escaping (Result<[URL], any Error>) -> Void,
        onCancellation: @escaping () -> Void
    ) -> some View
    

##  Parameters

`isPresented`

    

A binding to whether the dialog should be shown.

`allowedContentTypes`

    

The list of supported content types which can be imported.

`allowsMultipleSelection`

    

Whether the importer allows the user to select more than one file to import.

`onCompletion`

    

A callback that will be invoked when the operation has succeeded or failed.
The `result` indicates whether the operation succeeded or failed. To access
the received URLs, call `startAccessingSecurityScopedResource`. When the
access is no longer required, call `stopAccessingSecurityScopedResource`.

`onCancellation`

    

A callback that will be invoked if the user cancels the operation.

## Discussion

In order for the dialog to appear, `isPresented` must be `true`. When the
operation is finished, `isPresented` will be set to `false` before
`onCompletion` is called. If the user cancels the operation, `isPresented`
will be set to `false` and `onCompletion` will not be called.

Note

This dialog provides security-scoped URLs. Call the
`startAccessingSecurityScopedResource` method to access or bookmark the URLs,
and the `stopAccessingSecurityScopedResource` method to release the access.

For example, a button that allows the user to choose multiple PDF files for
the application to combine them later, might look like this:

Note

Changing `allowedContentTypes` or `allowsMultipleSelection` while the file
importer is presented will have no immediate effect, however will apply the
next time it is presented.

## See Also

### Importing from file

`func fileImporter(isPresented: Binding<Bool>, allowedContentTypes: [UTType],
allowsMultipleSelection: Bool, onCompletion: (Result<[URL], any Error>) ->
Void) -> some View`

Presents a system interface for allowing the user to import multiple files.

`func fileImporter(isPresented: Binding<Bool>, allowedContentTypes: [UTType],
onCompletion: (Result<URL, any Error>) -> Void) -> some View`

Presents a system interface for allowing the user to import an existing file.

Instance Method

# fileMover(isPresented:file:onCompletion:)

Presents a system interface for allowing the user to move an existing file to
a new location.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    func fileMover(
        isPresented: Binding<Bool>,
        file: URL?,
        onCompletion: @escaping (Result<URL, any Error>) -> Void
    ) -> some View
    

##  Parameters

`isPresented`

    

A binding to whether the interface should be shown.

`file`

    

The `URL` of the file to be moved.

`onCompletion`

    

A callback that will be invoked when the operation has has succeeded or
failed. To access the received URLs, call
`startAccessingSecurityScopedResource`. When the access is no longer required,
call `stopAccessingSecurityScopedResource`.

`result`

    

A `Result` indicating whether the operation succeeded or failed.

## Discussion

Note

This interface provides security-scoped URLs. Call the
`startAccessingSecurityScopedResource` method to access or bookmark the URLs,
and the `stopAccessingSecurityScopedResource` method to release the access.

In order for the interface to appear, both `isPresented` must be `true` and
`file` must not be `nil`. When the operation is finished, `isPresented` will
be set to `false` before `onCompletion` is called. If the user cancels the
operation, `isPresented` will be set to `false` and `onCompletion` will not be
called.

## See Also

### Moving a file

`func fileMover<C>(isPresented: Binding<Bool>, files: C, onCompletion:
(Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for allowing the user to move a collection of
existing files to a new location.

`func fileMover(isPresented: Binding<Bool>, file: URL?, onCompletion:
(Result<URL, any Error>) -> Void, onCancellation: () -> Void) -> some View`

Presents a system dialog for allowing the user to move an existing file to a
new location.

`func fileMover<C>(isPresented: Binding<Bool>, files: C, onCompletion:
(Result<[URL], any Error>) -> Void, onCancellation: () -> Void) -> some View`

Presents a system dialog for allowing the user to move a collection of
existing files to a new location.

Instance Method

# fileMover(isPresented:files:onCompletion:)

Presents a system interface for allowing the user to move a collection of
existing files to a new location.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    func fileMover<C>(
        isPresented: Binding<Bool>,
        files: C,
        onCompletion: @escaping (Result<[URL], any Error>) -> Void
    ) -> some View where C : Collection, C.Element == URL
    

##  Parameters

`isPresented`

    

A binding to whether the interface should be shown.

`files`

    

A collection of `URL`s for the files to be moved.

`onCompletion`

    

A callback that will be invoked when the operation has has succeeded or
failed. To access the received URLs, call
`startAccessingSecurityScopedResource`. When the access is no longer required,
call `stopAccessingSecurityScopedResource`.

`result`

    

A `Result` indicating whether the operation succeeded or failed.

## Discussion

Note

This interface provides security-scoped URLs. Call the
`startAccessingSecurityScopedResource` method to access or bookmark the URLs,
and the `stopAccessingSecurityScopedResource` method to release the access.

In order for the interface to appear, both `isPresented` must be `true` and
`files` must not be empty. When the operation is finished, `isPresented` will
be set to `false` before `onCompletion` is called. If the user cancels the
operation, `isPresented` will be set to `false` and `onCompletion` will not be
called.

## See Also

### Moving a file

`func fileMover(isPresented: Binding<Bool>, file: URL?, onCompletion:
(Result<URL, any Error>) -> Void) -> some View`

Presents a system interface for allowing the user to move an existing file to
a new location.

`func fileMover(isPresented: Binding<Bool>, file: URL?, onCompletion:
(Result<URL, any Error>) -> Void, onCancellation: () -> Void) -> some View`

Presents a system dialog for allowing the user to move an existing file to a
new location.

`func fileMover<C>(isPresented: Binding<Bool>, files: C, onCompletion:
(Result<[URL], any Error>) -> Void, onCancellation: () -> Void) -> some View`

Presents a system dialog for allowing the user to move a collection of
existing files to a new location.

Instance Method

# fileMover(isPresented:file:onCompletion:onCancellation:)

Presents a system dialog for allowing the user to move an existing file to a
new location.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func fileMover(
        isPresented: Binding<Bool>,
        file: URL?,
        onCompletion: @escaping (Result<URL, any Error>) -> Void,
        onCancellation: @escaping () -> Void
    ) -> some View
    

##  Parameters

`isPresented`

    

A binding to whether the dialog should be shown.

`file`

    

The URL of the file to be moved.

`onCompletion`

    

A callback that will be invoked when the operation has succeeded or failed.
The `result` indicates whether the operation succeeded or failed. To access
the received URLs, call `startAccessingSecurityScopedResource`. When the
access is no longer required, call `stopAccessingSecurityScopedResource`.

`onCancellation`

    

A callback that will be invoked if the user cancels the operation.

## Discussion

Note

This dialog provides security-scoped URLs. Call the
`startAccessingSecurityScopedResource` method to access or bookmark the URLs,
and the `stopAccessingSecurityScopedResource` method to release the access.

For example, a button that allows the user to move a file might look like
this:

## See Also

### Moving a file

`func fileMover(isPresented: Binding<Bool>, file: URL?, onCompletion:
(Result<URL, any Error>) -> Void) -> some View`

Presents a system interface for allowing the user to move an existing file to
a new location.

`func fileMover<C>(isPresented: Binding<Bool>, files: C, onCompletion:
(Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for allowing the user to move a collection of
existing files to a new location.

`func fileMover<C>(isPresented: Binding<Bool>, files: C, onCompletion:
(Result<[URL], any Error>) -> Void, onCancellation: () -> Void) -> some View`

Presents a system dialog for allowing the user to move a collection of
existing files to a new location.

Instance Method

# fileMover(isPresented:files:onCompletion:onCancellation:)

Presents a system dialog for allowing the user to move a collection of
existing files to a new location.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func fileMover<C>(
        isPresented: Binding<Bool>,
        files: C,
        onCompletion: @escaping (Result<[URL], any Error>) -> Void,
        onCancellation: @escaping () -> Void
    ) -> some View where C : Collection, C.Element == URL
    

##  Parameters

`isPresented`

    

A binding to whether the dialog should be shown.

`files`

    

A collection of URLs for the files to be moved.

`onCompletion`

    

A callback that will be invoked when the operation has succeeded or failed.
The `result` indicates whether the operation succeeded or failed. To access
the received URLs, call `startAccessingSecurityScopedResource`. When the
access is no longer required, call `stopAccessingSecurityScopedResource`.

`onCancellation`

    

A callback that will be invoked if the user cancels the operation.

## Discussion

Note

This dialog provides security-scoped URLs. Call the
`startAccessingSecurityScopedResource` method to access or bookmark the URLs,
and the `stopAccessingSecurityScopedResource` method to release the access.

For example, a button that allows the user to move files might look like this:

## See Also

### Moving a file

`func fileMover(isPresented: Binding<Bool>, file: URL?, onCompletion:
(Result<URL, any Error>) -> Void) -> some View`

Presents a system interface for allowing the user to move an existing file to
a new location.

`func fileMover<C>(isPresented: Binding<Bool>, files: C, onCompletion:
(Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for allowing the user to move a collection of
existing files to a new location.

`func fileMover(isPresented: Binding<Bool>, file: URL?, onCompletion:
(Result<URL, any Error>) -> Void, onCancellation: () -> Void) -> some View`

Presents a system dialog for allowing the user to move an existing file to a
new location.

Instance Method

# fileDialogBrowserOptions(_:)

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to
provide a refined URL search experience: include or exclude hidden files,
allow searching by tag, etc.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func fileDialogBrowserOptions(_ options: FileDialogBrowserOptions) -> some View
    

##  Parameters

`options`

    

The search options to apply to a given file dialog.

## See Also

### Configuring a file dialog

`func fileDialogConfirmationLabel<S>(S) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom confirmation button label.

`func fileDialogConfirmationLabel(Text?) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with custom text as a confirmation button label.

`func fileDialogConfirmationLabel(LocalizedStringKey) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom confirmation button label.

`func fileDialogCustomizationID(String) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to
persist and restore the file dialog configuration.

`func fileDialogDefaultDirectory(URL?) -> some View`

Configures the `fileExporter`, `fileImporter`, or `fileMover` to open with the
specified default directory.

`func fileDialogImportsUnresolvedAliases(Bool) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover`
behavior when a user chooses an alias.

`func fileDialogMessage<S>(S) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom message that is presented to the user, similar to a title.

`func fileDialogMessage(Text?) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom text that is presented to the user, similar to a title.

`func fileDialogMessage(LocalizedStringKey) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom message that is presented to the user, similar to a title.

`func fileDialogURLEnabled(Predicate<URL>) -> some View`

On macOS, configures the the `fileImporter` or `fileMover` to conditionally
disable presented URLs.

`struct FileDialogBrowserOptions`

The way that file dialogs present the file system.

Instance Method

# fileDialogConfirmationLabel(_:)

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom confirmation button label.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func fileDialogConfirmationLabel<S>(_ label: S) -> some View where S : StringProtocol
    

##  Parameters

`label`

    

The string to use as the label for the confirmation button.

## See Also

### Configuring a file dialog

`func fileDialogBrowserOptions(FileDialogBrowserOptions) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to
provide a refined URL search experience: include or exclude hidden files,
allow searching by tag, etc.

`func fileDialogConfirmationLabel(Text?) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with custom text as a confirmation button label.

`func fileDialogConfirmationLabel(LocalizedStringKey) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom confirmation button label.

`func fileDialogCustomizationID(String) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to
persist and restore the file dialog configuration.

`func fileDialogDefaultDirectory(URL?) -> some View`

Configures the `fileExporter`, `fileImporter`, or `fileMover` to open with the
specified default directory.

`func fileDialogImportsUnresolvedAliases(Bool) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover`
behavior when a user chooses an alias.

`func fileDialogMessage<S>(S) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom message that is presented to the user, similar to a title.

`func fileDialogMessage(Text?) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom text that is presented to the user, similar to a title.

`func fileDialogMessage(LocalizedStringKey) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom message that is presented to the user, similar to a title.

`func fileDialogURLEnabled(Predicate<URL>) -> some View`

On macOS, configures the the `fileImporter` or `fileMover` to conditionally
disable presented URLs.

`struct FileDialogBrowserOptions`

The way that file dialogs present the file system.

Instance Method

# fileDialogConfirmationLabel(_:)

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with custom text as a confirmation button label.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func fileDialogConfirmationLabel(_ label: Text?) -> some View
    

##  Parameters

`label`

    

The optional text to use as the label for the confirmation button.

## See Also

### Configuring a file dialog

`func fileDialogBrowserOptions(FileDialogBrowserOptions) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to
provide a refined URL search experience: include or exclude hidden files,
allow searching by tag, etc.

`func fileDialogConfirmationLabel<S>(S) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom confirmation button label.

`func fileDialogConfirmationLabel(LocalizedStringKey) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom confirmation button label.

`func fileDialogCustomizationID(String) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to
persist and restore the file dialog configuration.

`func fileDialogDefaultDirectory(URL?) -> some View`

Configures the `fileExporter`, `fileImporter`, or `fileMover` to open with the
specified default directory.

`func fileDialogImportsUnresolvedAliases(Bool) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover`
behavior when a user chooses an alias.

`func fileDialogMessage<S>(S) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom message that is presented to the user, similar to a title.

`func fileDialogMessage(Text?) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom text that is presented to the user, similar to a title.

`func fileDialogMessage(LocalizedStringKey) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom message that is presented to the user, similar to a title.

`func fileDialogURLEnabled(Predicate<URL>) -> some View`

On macOS, configures the the `fileImporter` or `fileMover` to conditionally
disable presented URLs.

`struct FileDialogBrowserOptions`

The way that file dialogs present the file system.

Instance Method

# fileDialogConfirmationLabel(_:)

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom confirmation button label.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func fileDialogConfirmationLabel(_ labelKey: LocalizedStringKey) -> some View
    

##  Parameters

`labelKey`

    

The key to a localized string to display.

## See Also

### Configuring a file dialog

`func fileDialogBrowserOptions(FileDialogBrowserOptions) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to
provide a refined URL search experience: include or exclude hidden files,
allow searching by tag, etc.

`func fileDialogConfirmationLabel<S>(S) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom confirmation button label.

`func fileDialogConfirmationLabel(Text?) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with custom text as a confirmation button label.

`func fileDialogCustomizationID(String) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to
persist and restore the file dialog configuration.

`func fileDialogDefaultDirectory(URL?) -> some View`

Configures the `fileExporter`, `fileImporter`, or `fileMover` to open with the
specified default directory.

`func fileDialogImportsUnresolvedAliases(Bool) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover`
behavior when a user chooses an alias.

`func fileDialogMessage<S>(S) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom message that is presented to the user, similar to a title.

`func fileDialogMessage(Text?) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom text that is presented to the user, similar to a title.

`func fileDialogMessage(LocalizedStringKey) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom message that is presented to the user, similar to a title.

`func fileDialogURLEnabled(Predicate<URL>) -> some View`

On macOS, configures the the `fileImporter` or `fileMover` to conditionally
disable presented URLs.

`struct FileDialogBrowserOptions`

The way that file dialogs present the file system.

Instance Method

# fileDialogCustomizationID(_:)

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to
persist and restore the file dialog configuration.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func fileDialogCustomizationID(_ id: String) -> some View
    

##  Parameters

`id`

    

An identifier of the configuration.

## Discussion

Among other parameters, it stores the current directory, view style (e.g.,
Icons, List, Columns), recent places, and expanded window size. It enables a
refined user experience; for example, when importing an image, the user might
switch to the Icons view, but the List view could be more convenient in
another context. The file dialog stores these settings and applies them every
time before presenting the panel. If not provided, on every launch, the file
dialog uses the default configuration.

## See Also

### Configuring a file dialog

`func fileDialogBrowserOptions(FileDialogBrowserOptions) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to
provide a refined URL search experience: include or exclude hidden files,
allow searching by tag, etc.

`func fileDialogConfirmationLabel<S>(S) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom confirmation button label.

`func fileDialogConfirmationLabel(Text?) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with custom text as a confirmation button label.

`func fileDialogConfirmationLabel(LocalizedStringKey) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom confirmation button label.

`func fileDialogDefaultDirectory(URL?) -> some View`

Configures the `fileExporter`, `fileImporter`, or `fileMover` to open with the
specified default directory.

`func fileDialogImportsUnresolvedAliases(Bool) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover`
behavior when a user chooses an alias.

`func fileDialogMessage<S>(S) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom message that is presented to the user, similar to a title.

`func fileDialogMessage(Text?) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom text that is presented to the user, similar to a title.

`func fileDialogMessage(LocalizedStringKey) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom message that is presented to the user, similar to a title.

`func fileDialogURLEnabled(Predicate<URL>) -> some View`

On macOS, configures the the `fileImporter` or `fileMover` to conditionally
disable presented URLs.

`struct FileDialogBrowserOptions`

The way that file dialogs present the file system.

Instance Method

# fileDialogDefaultDirectory(_:)

Configures the `fileExporter`, `fileImporter`, or `fileMover` to open with the
specified default directory.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func fileDialogDefaultDirectory(_ defaultDirectory: URL?) -> some View
    

##  Parameters

`defaultDirectory`

    

The directory to show when the system file dialog launches. If the given file
dialog has a `fileDialogCustomizationID` if stores the user-chosen directory
and subsequently opens with it, ignoring the default value provided in this
modifier.

## See Also

### Configuring a file dialog

`func fileDialogBrowserOptions(FileDialogBrowserOptions) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to
provide a refined URL search experience: include or exclude hidden files,
allow searching by tag, etc.

`func fileDialogConfirmationLabel<S>(S) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom confirmation button label.

`func fileDialogConfirmationLabel(Text?) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with custom text as a confirmation button label.

`func fileDialogConfirmationLabel(LocalizedStringKey) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom confirmation button label.

`func fileDialogCustomizationID(String) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to
persist and restore the file dialog configuration.

`func fileDialogImportsUnresolvedAliases(Bool) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover`
behavior when a user chooses an alias.

`func fileDialogMessage<S>(S) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom message that is presented to the user, similar to a title.

`func fileDialogMessage(Text?) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom text that is presented to the user, similar to a title.

`func fileDialogMessage(LocalizedStringKey) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom message that is presented to the user, similar to a title.

`func fileDialogURLEnabled(Predicate<URL>) -> some View`

On macOS, configures the the `fileImporter` or `fileMover` to conditionally
disable presented URLs.

`struct FileDialogBrowserOptions`

The way that file dialogs present the file system.

Instance Method

# fileDialogImportsUnresolvedAliases(_:)

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover`
behavior when a user chooses an alias.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func fileDialogImportsUnresolvedAliases(_ imports: Bool) -> some View
    

##  Parameters

`imports`

    

A Boolean value that indicates if the application receives unresolved or
resolved URLs when a user chooses aliases.

## Discussion

By default, file dialogs resolve aliases and provide the URL of the item
referred to by the chosen alias. This modifier allows control of this
behavior: pass `true` if the application doesn’t want file dialog to resolve
aliases.

## See Also

### Configuring a file dialog

`func fileDialogBrowserOptions(FileDialogBrowserOptions) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to
provide a refined URL search experience: include or exclude hidden files,
allow searching by tag, etc.

`func fileDialogConfirmationLabel<S>(S) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom confirmation button label.

`func fileDialogConfirmationLabel(Text?) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with custom text as a confirmation button label.

`func fileDialogConfirmationLabel(LocalizedStringKey) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom confirmation button label.

`func fileDialogCustomizationID(String) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to
persist and restore the file dialog configuration.

`func fileDialogDefaultDirectory(URL?) -> some View`

Configures the `fileExporter`, `fileImporter`, or `fileMover` to open with the
specified default directory.

`func fileDialogMessage<S>(S) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom message that is presented to the user, similar to a title.

`func fileDialogMessage(Text?) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom text that is presented to the user, similar to a title.

`func fileDialogMessage(LocalizedStringKey) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom message that is presented to the user, similar to a title.

`func fileDialogURLEnabled(Predicate<URL>) -> some View`

On macOS, configures the the `fileImporter` or `fileMover` to conditionally
disable presented URLs.

`struct FileDialogBrowserOptions`

The way that file dialogs present the file system.

Instance Method

# fileDialogMessage(_:)

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom message that is presented to the user, similar to a title.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func fileDialogMessage<S>(_ message: S) -> some View where S : StringProtocol
    

##  Parameters

`message`

    

The string to use as the file dialog message.

## See Also

### Configuring a file dialog

`func fileDialogBrowserOptions(FileDialogBrowserOptions) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to
provide a refined URL search experience: include or exclude hidden files,
allow searching by tag, etc.

`func fileDialogConfirmationLabel<S>(S) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom confirmation button label.

`func fileDialogConfirmationLabel(Text?) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with custom text as a confirmation button label.

`func fileDialogConfirmationLabel(LocalizedStringKey) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom confirmation button label.

`func fileDialogCustomizationID(String) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to
persist and restore the file dialog configuration.

`func fileDialogDefaultDirectory(URL?) -> some View`

Configures the `fileExporter`, `fileImporter`, or `fileMover` to open with the
specified default directory.

`func fileDialogImportsUnresolvedAliases(Bool) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover`
behavior when a user chooses an alias.

`func fileDialogMessage(Text?) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom text that is presented to the user, similar to a title.

`func fileDialogMessage(LocalizedStringKey) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom message that is presented to the user, similar to a title.

`func fileDialogURLEnabled(Predicate<URL>) -> some View`

On macOS, configures the the `fileImporter` or `fileMover` to conditionally
disable presented URLs.

`struct FileDialogBrowserOptions`

The way that file dialogs present the file system.

Instance Method

# fileDialogMessage(_:)

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom text that is presented to the user, similar to a title.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func fileDialogMessage(_ message: Text?) -> some View
    

##  Parameters

`message`

    

The optional text to use as the file dialog message.

## See Also

### Configuring a file dialog

`func fileDialogBrowserOptions(FileDialogBrowserOptions) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to
provide a refined URL search experience: include or exclude hidden files,
allow searching by tag, etc.

`func fileDialogConfirmationLabel<S>(S) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom confirmation button label.

`func fileDialogConfirmationLabel(Text?) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with custom text as a confirmation button label.

`func fileDialogConfirmationLabel(LocalizedStringKey) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom confirmation button label.

`func fileDialogCustomizationID(String) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to
persist and restore the file dialog configuration.

`func fileDialogDefaultDirectory(URL?) -> some View`

Configures the `fileExporter`, `fileImporter`, or `fileMover` to open with the
specified default directory.

`func fileDialogImportsUnresolvedAliases(Bool) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover`
behavior when a user chooses an alias.

`func fileDialogMessage<S>(S) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom message that is presented to the user, similar to a title.

`func fileDialogMessage(LocalizedStringKey) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom message that is presented to the user, similar to a title.

`func fileDialogURLEnabled(Predicate<URL>) -> some View`

On macOS, configures the the `fileImporter` or `fileMover` to conditionally
disable presented URLs.

`struct FileDialogBrowserOptions`

The way that file dialogs present the file system.

Instance Method

# fileDialogMessage(_:)

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom message that is presented to the user, similar to a title.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func fileDialogMessage(_ messageKey: LocalizedStringKey) -> some View
    

##  Parameters

`messageKey`

    

The key to a localized string to display.

## See Also

### Configuring a file dialog

`func fileDialogBrowserOptions(FileDialogBrowserOptions) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to
provide a refined URL search experience: include or exclude hidden files,
allow searching by tag, etc.

`func fileDialogConfirmationLabel<S>(S) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom confirmation button label.

`func fileDialogConfirmationLabel(Text?) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with custom text as a confirmation button label.

`func fileDialogConfirmationLabel(LocalizedStringKey) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom confirmation button label.

`func fileDialogCustomizationID(String) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to
persist and restore the file dialog configuration.

`func fileDialogDefaultDirectory(URL?) -> some View`

Configures the `fileExporter`, `fileImporter`, or `fileMover` to open with the
specified default directory.

`func fileDialogImportsUnresolvedAliases(Bool) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover`
behavior when a user chooses an alias.

`func fileDialogMessage<S>(S) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom message that is presented to the user, similar to a title.

`func fileDialogMessage(Text?) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom text that is presented to the user, similar to a title.

`func fileDialogURLEnabled(Predicate<URL>) -> some View`

On macOS, configures the the `fileImporter` or `fileMover` to conditionally
disable presented URLs.

`struct FileDialogBrowserOptions`

The way that file dialogs present the file system.

Instance Method

# fileDialogURLEnabled(_:)

On macOS, configures the the `fileImporter` or `fileMover` to conditionally
disable presented URLs.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func fileDialogURLEnabled(_ predicate: Predicate<URL>) -> some View
    

##  Parameters

`predicate`

    

The predicate that evaluates the URLs presented to the user to conditionally
disable them. The implementation is expected to have constant complexity and
should not access the files contents or metadata. A common use case is
inspecting the path or the file name.

## See Also

### Configuring a file dialog

`func fileDialogBrowserOptions(FileDialogBrowserOptions) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to
provide a refined URL search experience: include or exclude hidden files,
allow searching by tag, etc.

`func fileDialogConfirmationLabel<S>(S) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom confirmation button label.

`func fileDialogConfirmationLabel(Text?) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with custom text as a confirmation button label.

`func fileDialogConfirmationLabel(LocalizedStringKey) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom confirmation button label.

`func fileDialogCustomizationID(String) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to
persist and restore the file dialog configuration.

`func fileDialogDefaultDirectory(URL?) -> some View`

Configures the `fileExporter`, `fileImporter`, or `fileMover` to open with the
specified default directory.

`func fileDialogImportsUnresolvedAliases(Bool) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover`
behavior when a user chooses an alias.

`func fileDialogMessage<S>(S) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom message that is presented to the user, similar to a title.

`func fileDialogMessage(Text?) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom text that is presented to the user, similar to a title.

`func fileDialogMessage(LocalizedStringKey) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom message that is presented to the user, similar to a title.

`struct FileDialogBrowserOptions`

The way that file dialogs present the file system.

Structure

# FileDialogBrowserOptions

The way that file dialogs present the file system.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    struct FileDialogBrowserOptions

## Overview

Apply the options using the `fileDialogBrowserOptions(_:)` modifier.

## Topics

### Getting browser options

`static let displayFileExtensions: FileDialogBrowserOptions`

On iOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to show
or hide file extensions. Default behavior is to hide them. On macOS, this
option has no effect.

`static let enumeratePackages: FileDialogBrowserOptions`

Allows enumerating packages contents in contrast to the default behavior when
packages are represented flatly, similar to files.

`static let includeHiddenFiles: FileDialogBrowserOptions`

Displays the files that are hidden by default.

## Relationships

### Conforms To

  * `Equatable`
  * `ExpressibleByArrayLiteral`
  * `OptionSet`
  * `RawRepresentable`
  * `Sendable`
  * `SetAlgebra`

## See Also

### Configuring a file dialog

`func fileDialogBrowserOptions(FileDialogBrowserOptions) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to
provide a refined URL search experience: include or exclude hidden files,
allow searching by tag, etc.

`func fileDialogConfirmationLabel<S>(S) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom confirmation button label.

`func fileDialogConfirmationLabel(Text?) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with custom text as a confirmation button label.

`func fileDialogConfirmationLabel(LocalizedStringKey) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom confirmation button label.

`func fileDialogCustomizationID(String) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to
persist and restore the file dialog configuration.

`func fileDialogDefaultDirectory(URL?) -> some View`

Configures the `fileExporter`, `fileImporter`, or `fileMover` to open with the
specified default directory.

`func fileDialogImportsUnresolvedAliases(Bool) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover`
behavior when a user chooses an alias.

`func fileDialogMessage<S>(S) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom message that is presented to the user, similar to a title.

`func fileDialogMessage(Text?) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom text that is presented to the user, similar to a title.

`func fileDialogMessage(LocalizedStringKey) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom message that is presented to the user, similar to a title.

`func fileDialogURLEnabled(Predicate<URL>) -> some View`

On macOS, configures the the `fileImporter` or `fileMover` to conditionally
disable presented URLs.

Instance Method

# inspector(isPresented:content:)

Inserts an inspector at the applied position in the view hierarchy.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+

    
    
    func inspector<V>(
        isPresented: Binding<Bool>,
        @ViewBuilder content: () -> V
    ) -> some View where V : View
    

##  Parameters

`isPresented`

    

A binding to `Bool` controlling the presented state.

`content`

    

The inspector content.

## Discussion

Apply this modifier to declare an inspector with a context-dependent
presentation. For example, an inspector can present as a trailing column in a
horizontally regular size class, but adapt to a sheet in a horizontally
compact size class.

Note

Trailing column inspectors have their presentation state restored by the
framework.

See Also

`InspectorCommands` for including the default inspector commands and keyboard
shortcuts.

## See Also

### Presenting an inspector

`func inspectorColumnWidth(CGFloat) -> some View`

Sets a fixed, preferred width for the inspector containing this view when
presented as a trailing column.

`func inspectorColumnWidth(min: CGFloat?, ideal: CGFloat, max: CGFloat?) ->
some View`

Sets a flexible, preferred width for the inspector in a trailing-column
presentation.

Instance Method

# inspectorColumnWidth(_:)

Sets a fixed, preferred width for the inspector containing this view when
presented as a trailing column.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+

    
    
    func inspectorColumnWidth(_ width: CGFloat) -> some View
    

##  Parameters

`width`

    

The preferred fixed width for the inspector if presented as a trailing column.

## Discussion

Apply this modifier on the content of a `inspector(isPresented:content:)` to
specify a fixed preferred width for the trailing column. Use
`inspectorColumnWidth(min:ideal:max:)` if you need to specify a flexible
width.

The following example shows an editor interface with an inspector, which when
presented as a trailing-column, has a fixed width of 225 points. The example
also uses `interactiveDismissDisabled(_:)` to prevent the inspector from being
collapsed by user action like dragging a divider.

Note

A fixed width does not prevent the user collapsing the inspector on macOS. See
`interactiveDismissDisabled(_:)`.

## See Also

### Presenting an inspector

`func inspector<V>(isPresented: Binding<Bool>, content: () -> V) -> some View`

Inserts an inspector at the applied position in the view hierarchy.

`func inspectorColumnWidth(min: CGFloat?, ideal: CGFloat, max: CGFloat?) ->
some View`

Sets a flexible, preferred width for the inspector in a trailing-column
presentation.

Instance Method

# inspectorColumnWidth(min:ideal:max:)

Sets a flexible, preferred width for the inspector in a trailing-column
presentation.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+

    
    
    func inspectorColumnWidth(
        min: CGFloat? = nil,
        ideal: CGFloat,
        max: CGFloat? = nil
    ) -> some View
    

##  Parameters

`min`

    

The minimum allowed width for the trailing column inspector

`ideal`

    

The initial width of the inspector in the absence of state restoration.
`ideal` influences the resulting width on macOS when a user double-clicks the
divider on the leading edge of the inspector. clicks a divider to readjust

`max`

    

The maximum allowed width for the trailing column inspector

## Discussion

Apply this modifier on the content of a `inspector(isPresented:content:)` to
specify a preferred flexible width for the column. Use
`inspectorColumnWidth(_:)` if you need to specify a fixed width.

The following example shows an editor interface with an inspector, which when
presented as a trailing-column, has a preferred width of 225 points, maximum
of 400, and a minimum of 150 at which point it will collapse, if allowed.

Only some platforms enable flexible inspector columns. If you specify a width
that the current presentation environment doesn’t support, SwiftUI may use a
different width for your column.

## See Also

### Presenting an inspector

`func inspector<V>(isPresented: Binding<Bool>, content: () -> V) -> some View`

Inserts an inspector at the applied position in the view hierarchy.

`func inspectorColumnWidth(CGFloat) -> some View`

Sets a fixed, preferred width for the inspector containing this view when
presented as a trailing column.

Instance Property

# isPresented

A Boolean value that indicates whether the view associated with this
environment is currently presented.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var isPresented: Bool { get }

## Discussion

You can read this value like any of the other `EnvironmentValues` by creating
a property with the `Environment` property wrapper:

Read the value inside a view if you need to know when SwiftUI presents that
view. For example, you can take an action when SwiftUI presents a view by
using the `onChange(of:initial:_:)` modifier:

This behaves differently than `onAppear(perform:)`, which SwiftUI can call
more than once for a given presentation, like when you navigate back to a view
that’s already in the navigation hierarchy.

To dismiss the currently presented view, use `dismiss`.

## See Also

### Dismissing a presentation

`var dismiss: DismissAction`

An action that dismisses the current presentation.

`struct DismissAction`

An action that dismisses a presentation.

`func interactiveDismissDisabled(Bool) -> some View`

Conditionally prevents interactive dismissal of presentations like popovers,
sheets, and inspectors.

Instance Property

# dismiss

An action that dismisses the current presentation.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var dismiss: DismissAction { get }

## Discussion

Use this environment value to get the `DismissAction` instance for the current
`Environment`. Then call the instance to perform the dismissal. You call the
instance directly because it defines a `callAsFunction()` method that Swift
calls when you call the instance.

You can use this action to:

  * Dismiss a modal presentation, like a sheet or a popover.

  * Pop the current view from a `NavigationStack`.

  * Close a window that you create with `WindowGroup` or `Window`.

The specific behavior of the action depends on where you call it from. For
example, you can create a button that calls the `DismissAction` inside a view
that acts as a sheet:

When you present the `SheetContents` view, someone can dismiss the sheet by
tapping or clicking the sheet’s button:

Be sure that you define the action in the appropriate environment. For
example, don’t reorganize the `DetailView` in the example above so that it
creates the `dismiss` property and calls it from the
`sheet(item:onDismiss:content:)` view modifier’s `content` closure:

If you do this, the sheet fails to dismiss because the action applies to the
environment where you declared it, which is that of the detail view, rather
than the sheet. In fact, in macOS and iPadOS, if the `DetailView` is the root
view of a window, the dismiss action closes the window instead.

The dismiss action has no effect on a view that isn’t currently presented. If
you need to query whether SwiftUI is currently presenting a view, read the
`isPresented` environment value.

## See Also

### Dismissing a presentation

`var isPresented: Bool`

A Boolean value that indicates whether the view associated with this
environment is currently presented.

`struct DismissAction`

An action that dismisses a presentation.

`func interactiveDismissDisabled(Bool) -> some View`

Conditionally prevents interactive dismissal of presentations like popovers,
sheets, and inspectors.

Structure

# DismissAction

An action that dismisses a presentation.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    struct DismissAction

## Overview

Use the `dismiss` environment value to get the instance of this structure for
a given `Environment`. Then call the instance to perform the dismissal. You
call the instance directly because it defines a `callAsFunction()` method that
Swift calls when you call the instance.

You can use this action to:

  * Dismiss a modal presentation, like a sheet or a popover.

  * Pop the current view from a `NavigationStack`.

  * Close a window that you create with `WindowGroup` or `Window`.

The specific behavior of the action depends on where you call it from. For
example, you can create a button that calls the `DismissAction` inside a view
that acts as a sheet:

When you present the `SheetContents` view, someone can dismiss the sheet by
tapping or clicking the sheet’s button:

Be sure that you define the action in the appropriate environment. For
example, don’t reorganize the `DetailView` in the example above so that it
creates the `dismiss` property and calls it from the
`sheet(item:onDismiss:content:)` view modifier’s `content` closure:

If you do this, the sheet fails to dismiss because the action applies to the
environment where you declared it, which is that of the detail view, rather
than the sheet. In fact, in macOS and iPadOS, if the `DetailView` is the root
view of a window, the dismiss action closes the window instead.

The dismiss action has no effect on a view that isn’t currently presented. If
you need to query whether SwiftUI is currently presenting a view, read the
`isPresented` environment value.

## Topics

### Calling the action

`func callAsFunction()`

Dismisses the view if it is currently presented.

## See Also

### Dismissing a presentation

`var isPresented: Bool`

A Boolean value that indicates whether the view associated with this
environment is currently presented.

`var dismiss: DismissAction`

An action that dismisses the current presentation.

`func interactiveDismissDisabled(Bool) -> some View`

Conditionally prevents interactive dismissal of presentations like popovers,
sheets, and inspectors.

Instance Method

# interactiveDismissDisabled(_:)

Conditionally prevents interactive dismissal of presentations like popovers,
sheets, and inspectors.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func interactiveDismissDisabled(_ isDisabled: Bool = true) -> some View
    

##  Parameters

`isDisabled`

    

A Boolean value that indicates whether to prevent nonprogrammatic dismissal of
the containing view hierarchy when presented in a sheet or popover.

## Discussion

Users can dismiss certain kinds of presentations using built-in gestures. In
particular, a user can dismiss a sheet by dragging it down, or a popover by
clicking or tapping outside of the presented view. Use the
`interactiveDismissDisabled(_:)` modifier to conditionally prevent this kind
of dismissal. You typically do this to prevent the user from dismissing a
presentation before providing needed data or completing a required action.

For instance, suppose you have a view that displays a licensing agreement that
the user must acknowledge before continuing:

If you present this view in a sheet, the user can dismiss it by either tapping
the button — which calls `dismiss` from its `action` closure — or by dragging
the sheet down. To ensure that the user accepts the terms by tapping the
button, disable interactive dismissal, conditioned on the `areTermsAccepted`
property:

You can apply the modifier to any view in the sheet’s view hierarchy,
including to the sheet’s top level view, as the example demonstrates, or to
any child view, like the `Form` or the Accept `Button`.

The modifier has no effect on programmatic dismissal, which you can invoke by
updating the `Binding` that controls the presentation, or by calling the
environment’s `dismiss` action. On macOS, disabling interactive dismissal in a
popover makes the popover nontransient.

## See Also

### Dismissing a presentation

`var isPresented: Bool`

A Boolean value that indicates whether the view associated with this
environment is currently presented.

`var dismiss: DismissAction`

An action that dismisses the current presentation.

`struct DismissAction`

An action that dismisses a presentation.

Structure

# Alert

A representation of an alert presentation.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    struct Alert

Deprecated

Use a `View` modifier like `alert(_:isPresented:presenting:actions:message:)`
instead.

## Overview

Use an alert when you want the user to act in response to the state of the app
or system. If you want the user to make a choice in response to their action,
use an `ActionSheet` instead.

You show an alert by using the `alert(isPresented:content:)` view modifier to
create an alert, which then appears whenever the bound `isPresented` value is
`true`. The `content` closure you provide to this modifer produces a
customized instance of the `Alert` type.

In the following example, a button presents a simple alert when tapped, by
updating a local `showAlert` property that binds to the alert.

To customize the alert, add instances of the `Alert.Button` type, which
provides standardized buttons for common tasks like canceling and performing
destructive actions. The following example uses two buttons: a default button
labeled “Try Again” that calls a `saveWorkoutData` method, and a “Delete”
button that calls a destructive `deleteWorkoutData` method.

The alert handles its own dismissal when the user taps one of the buttons in
the alert, by setting the bound `isPresented` value back to `false`.

## Topics

### Creating an alert

`init(title: Text, message: Text?, dismissButton: Alert.Button?)`

Creates an alert with one button.

`init(title: Text, message: Text?, primaryButton: Alert.Button,
secondaryButton: Alert.Button)`

Creates an alert with two buttons.

`static func sideBySideButtons(title: Text, message: Text?, primaryButton:
Alert.Button, secondaryButton: Alert.Button) -> Alert`

Creates a side by side button alert.

### Specifying the button type

`struct Button`

A button that represents an operation of an alert presentation.

## See Also

### Deprecated modal presentations

`struct ActionSheet`

A representation of an action sheet presentation.

Deprecated

Structure

# ActionSheet

A representation of an action sheet presentation.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  Mac Catalyst
13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated  watchOS 6.0–10.4
Deprecated  visionOS 1.0+

    
    
    struct ActionSheet

Deprecated

Use a `View` modifier like
`confirmationDialog(_:isPresented:titleVisibility:presenting:actions:message:)`
instead.

## Overview

Use an action sheet when you want the user to make a choice between two or
more options, in response to their own action. If you want the user to act in
response to the state of the app or the system, rather than a user action, use
an `Alert` instead.

You show an action sheet by using the `actionSheet(isPresented:content:)` view
modifier to create an action sheet, which then appears whenever the bound
`isPresented` value is `true`. The `content` closure you provide to this
modifier produces a customized instance of the `ActionSheet` type. To supply
the options, create instances of `ActionSheet.Button` to distinguish between
ordinary options, destructive options, and cancellation of the user’s original
action.

The action sheet handles its dismissal by setting the bound `isPresented`
value back to `false` when the user taps a button in the action sheet.

The following example creates an action sheet with three options: a Cancel
button, a destructive button, and a default button. The second and third of
these call methods are named `overwriteWorkout` and `appendWorkout`,
respectively.

The system may interpret the order of items as they appear in the `buttons`
array to accommodate platform conventions. In this example, the Cancel button
is the first member of the array, but the action sheet puts it in its standard
position at the bottom of the sheet.

## Topics

### Creating an action sheet

`init(title: Text, message: Text?, buttons: [ActionSheet.Button])`

Creates an action sheet with the provided buttons.

### Specifying the button type

`typealias Button`

A button representing an operation of an action sheet presentation.

## See Also

### Deprecated modal presentations

`struct Alert`

A representation of an alert presentation.

Deprecated



# MoveKeyframe

Initializer

# init(_:)

Creates a new keyframe using the given value.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init(_ to: Value)

##  Parameters

`to`

    

The value of the keyframe.



# MenuStyle

Type Property

# automatic

The default menu style, based on the menu’s context.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 17.0+  visionOS
1.0+

    
    
    static var automatic: DefaultMenuStyle { get }

Available when `Self` is `DefaultMenuStyle`.

## Discussion

The default menu style can vary by platform. By default, macOS uses the
bordered button style.

If you create a menu inside a container, the style resolves to the recommended
style for menus inside that container for that specific platform. For example,
a menu nested within another menu will resolve to a submenu:

You can override a menu’s style. To apply the default style to a menu, or to a
view that contains a menu, use the `menuStyle(_:)` modifier.

## See Also

### Getting built-in menu styles

`static var button: ButtonMenuStyle`

A menu style that displays a button that toggles the display of the menu’s
contents when pressed.

Available when `Self` is `ButtonMenuStyle`.

`static var borderedButton: BorderedButtonMenuStyle`

A menu style that displays a bordered button that toggles the display of the
menu’s contents when pressed.

Available when `Self` is `BorderedButtonMenuStyle`.

Deprecated

`static var borderlessButton: BorderlessButtonMenuStyle`

A menu style that displays a borderless button that toggles the display of the
menu’s contents when pressed.

Available when `Self` is `BorderlessButtonMenuStyle`.

Deprecated

Type Property

# button

A menu style that displays a button that toggles the display of the menu’s
contents when pressed.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 17.0+  visionOS
1.0+

    
    
    static var button: ButtonMenuStyle { get }

Available when `Self` is `ButtonMenuStyle`.

## Discussion

On macOS, the button displays an arrow to indicate that it presents a menu.

Pressing and then dragging into the contents activates the selected action on
release.

## See Also

### Getting built-in menu styles

`static var automatic: DefaultMenuStyle`

The default menu style, based on the menu’s context.

Available when `Self` is `DefaultMenuStyle`.

`static var borderedButton: BorderedButtonMenuStyle`

A menu style that displays a bordered button that toggles the display of the
menu’s contents when pressed.

Available when `Self` is `BorderedButtonMenuStyle`.

Deprecated

`static var borderlessButton: BorderlessButtonMenuStyle`

A menu style that displays a borderless button that toggles the display of the
menu’s contents when pressed.

Available when `Self` is `BorderlessButtonMenuStyle`.

Deprecated

Type Property

# borderedButton

A menu style that displays a bordered button that toggles the display of the
menu’s contents when pressed.

macOS 11.0–14.4  Deprecated

    
    
    static var borderedButton: BorderedButtonMenuStyle { get }

Available when `Self` is `BorderedButtonMenuStyle`.

Deprecated

Use `menuStyle(_:)` with `button` and `buttonStyle(_:)` with `bordered`.

## Discussion

On macOS, the button displays an arrow indicating that it presents a menu.

Pressing and then dragging into the contents triggers the chosen action on
release.

## See Also

### Getting built-in menu styles

`static var automatic: DefaultMenuStyle`

The default menu style, based on the menu’s context.

Available when `Self` is `DefaultMenuStyle`.

`static var button: ButtonMenuStyle`

A menu style that displays a button that toggles the display of the menu’s
contents when pressed.

Available when `Self` is `ButtonMenuStyle`.

`static var borderlessButton: BorderlessButtonMenuStyle`

A menu style that displays a borderless button that toggles the display of the
menu’s contents when pressed.

Available when `Self` is `BorderlessButtonMenuStyle`.

Deprecated

Type Property

# borderlessButton

A menu style that displays a borderless button that toggles the display of the
menu’s contents when pressed.

iOS 14.0–17.4  Deprecated  iPadOS 14.0–17.4  Deprecated  macOS 11.0–14.4
Deprecated  Mac Catalyst 14.0–17.4  Deprecated  tvOS 17.0–17.4  Deprecated
visionOS 1.0+

    
    
    static var borderlessButton: BorderlessButtonMenuStyle { get }

Available when `Self` is `BorderlessButtonMenuStyle`.

Deprecated

Use `menuStyle(_:)` with `button` and `buttonStyle(_:)` with `borderless`.

## Discussion

On macOS, the button optionally displays an arrow indicating that it presents
a menu.

Pressing and then dragging into the contents triggers the chosen action on
release.

## See Also

### Getting built-in menu styles

`static var automatic: DefaultMenuStyle`

The default menu style, based on the menu’s context.

Available when `Self` is `DefaultMenuStyle`.

`static var button: ButtonMenuStyle`

A menu style that displays a button that toggles the display of the menu’s
contents when pressed.

Available when `Self` is `ButtonMenuStyle`.

`static var borderedButton: BorderedButtonMenuStyle`

A menu style that displays a bordered button that toggles the display of the
menu’s contents when pressed.

Available when `Self` is `BorderedButtonMenuStyle`.

Deprecated

Instance Method

# makeBody(configuration:)

Creates a view that represents the body of a menu.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 17.0+  visionOS
1.0+

    
    
    @ViewBuilder
    func makeBody(configuration: Self.Configuration) -> Self.Body

**Required**

##  Parameters

`configuration`

    

The properties of the menu.

## Discussion

The system calls this method for each `Menu` instance in a view hierarchy
where this style is the current menu style.

## See Also

### Creating custom menu styles

`typealias Configuration`

The properties of a menu.

`associatedtype Body : View`

A view that represents the body of a menu.

**Required**

Type Alias

# MenuStyle.Configuration

The properties of a menu.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 17.0+  visionOS
1.0+

    
    
    typealias Configuration = MenuStyleConfiguration

## See Also

### Creating custom menu styles

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Creates a view that represents the body of a menu.

**Required**

` associatedtype Body : View`

A view that represents the body of a menu.

**Required**

Associated Type

# Body

A view that represents the body of a menu.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 17.0+  visionOS
1.0+

    
    
    associatedtype Body : View

**Required**

## See Also

### Creating custom menu styles

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Creates a view that represents the body of a menu.

**Required**

` typealias Configuration`

The properties of a menu.

Structure

# DefaultMenuStyle

The default menu style, based on the menu’s context.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 17.0+  visionOS
1.0+

    
    
    struct DefaultMenuStyle

## Overview

You can also use `automatic` to construct this style.

## Topics

### Creating the menu style

`init()`

Creates a default menu style.

## Relationships

### Conforms To

  * `MenuStyle`

## See Also

### Supporting types

`struct ButtonMenuStyle`

A menu style that displays a button that toggles the display of the menu’s
contents when pressed.

`struct BorderlessButtonMenuStyle`

A menu style that displays a borderless button that toggles the display of the
menu’s contents when pressed.

Deprecated

`struct BorderedButtonMenuStyle`

A menu style that displays a bordered button that toggles the display of the
menu’s contents when pressed.

Deprecated

Structure

# ButtonMenuStyle

A menu style that displays a button that toggles the display of the menu’s
contents when pressed.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 17.0+  visionOS
1.0+

    
    
    struct ButtonMenuStyle

## Overview

Use `button` to construct this style.

## Topics

### Creating the menu style

`init()`

Creates a button menu style.

## Relationships

### Conforms To

  * `MenuStyle`

## See Also

### Supporting types

`struct DefaultMenuStyle`

The default menu style, based on the menu’s context.

`struct BorderlessButtonMenuStyle`

A menu style that displays a borderless button that toggles the display of the
menu’s contents when pressed.

Deprecated

`struct BorderedButtonMenuStyle`

A menu style that displays a bordered button that toggles the display of the
menu’s contents when pressed.

Deprecated

Structure

# BorderlessButtonMenuStyle

A menu style that displays a borderless button that toggles the display of the
menu’s contents when pressed.

iOS 14.0–17.4  Deprecated  iPadOS 14.0–17.4  Deprecated  macOS 11.0–14.4
Deprecated  Mac Catalyst 14.0–17.4  Deprecated  tvOS 17.0–17.4  Deprecated
visionOS 1.0+

    
    
    struct BorderlessButtonMenuStyle

Deprecated

Use `menuStyle(_:)` with `button` and `buttonStyle(_:)` with `borderless`.

## Overview

Use `borderlessButton` to construct this style.

## Topics

### Creating a bordeless button menu style

`init()`

Creates a borderless button menu style.

`init(showsMenuIndicator: Bool)`

Creates a borderless button menu style, specifying whether to show a visual
menu indicator.

## Relationships

### Conforms To

  * `MenuStyle`

## See Also

### Supporting types

`struct DefaultMenuStyle`

The default menu style, based on the menu’s context.

`struct ButtonMenuStyle`

A menu style that displays a button that toggles the display of the menu’s
contents when pressed.

`struct BorderedButtonMenuStyle`

A menu style that displays a bordered button that toggles the display of the
menu’s contents when pressed.

Deprecated

Structure

# BorderedButtonMenuStyle

A menu style that displays a bordered button that toggles the display of the
menu’s contents when pressed.

macOS 11.0–14.4  Deprecated

    
    
    struct BorderedButtonMenuStyle

Deprecated

Use `menuStyle(_:)` with `button` and `buttonStyle(_:)` with `bordered`.

## Overview

Use `borderedButton` to construct this style.

## Topics

### Creating a bordered button menu style

`init()`

Creates a bordered button menu style.

## Relationships

### Conforms To

  * `MenuStyle`

## See Also

### Supporting types

`struct DefaultMenuStyle`

The default menu style, based on the menu’s context.

`struct ButtonMenuStyle`

A menu style that displays a button that toggles the display of the menu’s
contents when pressed.

`struct BorderlessButtonMenuStyle`

A menu style that displays a borderless button that toggles the display of the
menu’s contents when pressed.

Deprecated



# MagnifyGesture

Initializer

# init(minimumScaleDelta:)

Creates a magnify gesture with a given minimum delta for the gesture to start.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    init(minimumScaleDelta: CGFloat = 0.01)

##  Parameters

`minimumScaleDelta`

    

The minimum scale delta required before the gesture starts.

## See Also

### Creating the gesture

`var minimumScaleDelta: CGFloat`

The minimum required delta before the gesture starts.

Instance Property

# minimumScaleDelta

The minimum required delta before the gesture starts.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    var minimumScaleDelta: CGFloat

## See Also

### Creating the gesture

`init(minimumScaleDelta: CGFloat)`

Creates a magnify gesture with a given minimum delta for the gesture to start.



# MoveTransition

Initializer

# init(edge:)

Creates a transition that moves the view away, towards the specified edge of
the view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init(edge: Edge)

## See Also

### Creating the transition

`var edge: Edge`

The edge to move the view towards.

Instance Property

# edge

The edge to move the view towards.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var edge: Edge

## See Also

### Creating the transition

`init(edge: Edge)`

Creates a transition that moves the view away, towards the specified edge of
the view.



# Material

Type Property

# ultraThin

A mostly translucent material.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static let ultraThin: Material

## See Also

### Getting material types

`static let thin: Material`

A material that’s more translucent than opaque.

`static let regular: Material`

A material that’s somewhat translucent.

`static let thick: Material`

A material that’s more opaque than translucent.

`static let ultraThick: Material`

A mostly opaque material.

`static let bar: Material`

A material matching the style of system toolbars.

Type Property

# thin

A material that’s more translucent than opaque.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static let thin: Material

## See Also

### Getting material types

`static let ultraThin: Material`

A mostly translucent material.

`static let regular: Material`

A material that’s somewhat translucent.

`static let thick: Material`

A material that’s more opaque than translucent.

`static let ultraThick: Material`

A mostly opaque material.

`static let bar: Material`

A material matching the style of system toolbars.

Type Property

# regular

A material that’s somewhat translucent.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static let regular: Material

## See Also

### Getting material types

`static let ultraThin: Material`

A mostly translucent material.

`static let thin: Material`

A material that’s more translucent than opaque.

`static let thick: Material`

A material that’s more opaque than translucent.

`static let ultraThick: Material`

A mostly opaque material.

`static let bar: Material`

A material matching the style of system toolbars.

Type Property

# thick

A material that’s more opaque than translucent.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static let thick: Material

## See Also

### Getting material types

`static let ultraThin: Material`

A mostly translucent material.

`static let thin: Material`

A material that’s more translucent than opaque.

`static let regular: Material`

A material that’s somewhat translucent.

`static let ultraThick: Material`

A mostly opaque material.

`static let bar: Material`

A material matching the style of system toolbars.

Type Property

# ultraThick

A mostly opaque material.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static let ultraThick: Material

## See Also

### Getting material types

`static let ultraThin: Material`

A mostly translucent material.

`static let thin: Material`

A material that’s more translucent than opaque.

`static let regular: Material`

A material that’s somewhat translucent.

`static let thick: Material`

A material that’s more opaque than translucent.

`static let bar: Material`

A material matching the style of system toolbars.

Type Property

# bar

A material matching the style of system toolbars.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    static let bar: Material

## See Also

### Getting material types

`static let ultraThin: Material`

A mostly translucent material.

`static let thin: Material`

A material that’s more translucent than opaque.

`static let regular: Material`

A material that’s somewhat translucent.

`static let thick: Material`

A material that’s more opaque than translucent.

`static let ultraThick: Material`

A mostly opaque material.



# MenuBarExtra

Initializer

# init(_:content:)

Creates a menu bar extra with a key for a localized string to use as the
label. The extra defines the primary scene of an `App`.

macOS 13.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        @ViewBuilder content: () -> Content
    )

Available when `Label` is `Text` and `Content` conforms to `View`.

##  Parameters

`titleKey`

    

The title key to use for the label of the item.

`content`

    

A `View` to display when the user selects the item.

## Discussion

When this item is removed from the system menu bar by the user, the
application will be automatically quit. As such, it should not be used in
conjunction with other scene types in your `App`.

## See Also

### Creating a menu bar extra

`init<S>(S, content: () -> Content)`

Creates a menu bar extra with a string to use as the label. The item defines
the primary scene of an `App`.

Available when `Label` is `Text` and `Content` conforms to `View`.

`init(content: () -> Content, label: () -> Label)`

Creates a menu bar extra that will be displayed in the system menu bar, and
defines the primary scene of an `App`.

`init(LocalizedStringKey, isInserted: Binding<Bool>, content: () -> Content)`

Creates a menu bar extra with a key for a localized string to use as the
label. The item will be displayed in the system menu bar when the specified
binding is set to `true`. If the user removes the item from the menu bar, the
binding will be set to `false`.

Available when `Label` is `Text` and `Content` conforms to `View`.

`init<S>(S, isInserted: Binding<Bool>, content: () -> Content)`

Creates a menu bar extra with a string to use as the label. The item will be
displayed in the system menu bar when the specified binding is set to `true`.
If the user removes the item from the menu bar, the binding will be set to
`false`.

Available when `Label` is `Text` and `Content` conforms to `View`.

`init(isInserted: Binding<Bool>, content: () -> Content, label: () -> Label)`

Creates a menu bar extra. The item will be displayed in the system menu bar
when the specified binding is set to `true`. If the user removes the item from
the menu bar, the binding will be set to `false`.

Initializer

# init(_:content:)

Creates a menu bar extra with a string to use as the label. The item defines
the primary scene of an `App`.

macOS 13.0+

    
    
    init<S>(
        _ title: S,
        @ViewBuilder content: () -> Content
    ) where S : StringProtocol

Available when `Label` is `Text` and `Content` conforms to `View`.

##  Parameters

`title`

    

The string to use for the label of the item. as a `Menu`.

`content`

    

A `View` to display when the user selects the item.

## Discussion

When this item is removed from the system menu bar by the user, the
application will be automatically quit. As such, it should not be used in
conjunction with other scene types in your `App`.

## See Also

### Creating a menu bar extra

`init(LocalizedStringKey, content: () -> Content)`

Creates a menu bar extra with a key for a localized string to use as the
label. The extra defines the primary scene of an `App`.

Available when `Label` is `Text` and `Content` conforms to `View`.

`init(content: () -> Content, label: () -> Label)`

Creates a menu bar extra that will be displayed in the system menu bar, and
defines the primary scene of an `App`.

`init(LocalizedStringKey, isInserted: Binding<Bool>, content: () -> Content)`

Creates a menu bar extra with a key for a localized string to use as the
label. The item will be displayed in the system menu bar when the specified
binding is set to `true`. If the user removes the item from the menu bar, the
binding will be set to `false`.

Available when `Label` is `Text` and `Content` conforms to `View`.

`init<S>(S, isInserted: Binding<Bool>, content: () -> Content)`

Creates a menu bar extra with a string to use as the label. The item will be
displayed in the system menu bar when the specified binding is set to `true`.
If the user removes the item from the menu bar, the binding will be set to
`false`.

Available when `Label` is `Text` and `Content` conforms to `View`.

`init(isInserted: Binding<Bool>, content: () -> Content, label: () -> Label)`

Creates a menu bar extra. The item will be displayed in the system menu bar
when the specified binding is set to `true`. If the user removes the item from
the menu bar, the binding will be set to `false`.

Initializer

# init(content:label:)

Creates a menu bar extra that will be displayed in the system menu bar, and
defines the primary scene of an `App`.

macOS 13.0+

    
    
    init(
        @ViewBuilder content: () -> Content,
        @ViewBuilder label: () -> Label
    )

##  Parameters

`content`

    

A `View` to display when the user selects the item.

`label`

    

A `View` to use as the label in the system menu bar.

## Discussion

When this item is removed from the system menu bar by the user, the
application will be automatically quit. As such, it should not be used in
conjunction with other scene types in your `App`.

## See Also

### Creating a menu bar extra

`init(LocalizedStringKey, content: () -> Content)`

Creates a menu bar extra with a key for a localized string to use as the
label. The extra defines the primary scene of an `App`.

Available when `Label` is `Text` and `Content` conforms to `View`.

`init<S>(S, content: () -> Content)`

Creates a menu bar extra with a string to use as the label. The item defines
the primary scene of an `App`.

Available when `Label` is `Text` and `Content` conforms to `View`.

`init(LocalizedStringKey, isInserted: Binding<Bool>, content: () -> Content)`

Creates a menu bar extra with a key for a localized string to use as the
label. The item will be displayed in the system menu bar when the specified
binding is set to `true`. If the user removes the item from the menu bar, the
binding will be set to `false`.

Available when `Label` is `Text` and `Content` conforms to `View`.

`init<S>(S, isInserted: Binding<Bool>, content: () -> Content)`

Creates a menu bar extra with a string to use as the label. The item will be
displayed in the system menu bar when the specified binding is set to `true`.
If the user removes the item from the menu bar, the binding will be set to
`false`.

Available when `Label` is `Text` and `Content` conforms to `View`.

`init(isInserted: Binding<Bool>, content: () -> Content, label: () -> Label)`

Creates a menu bar extra. The item will be displayed in the system menu bar
when the specified binding is set to `true`. If the user removes the item from
the menu bar, the binding will be set to `false`.

Initializer

# init(_:isInserted:content:)

Creates a menu bar extra with a key for a localized string to use as the
label. The item will be displayed in the system menu bar when the specified
binding is set to `true`. If the user removes the item from the menu bar, the
binding will be set to `false`.

macOS 13.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        isInserted: Binding<Bool>,
        @ViewBuilder content: () -> Content
    )

Available when `Label` is `Text` and `Content` conforms to `View`.

##  Parameters

`titleKey`

    

The title key to use for the label of the item.

`isInserted`

    

Whether the item is inserted in the menu bar. The item may or may not be
visible, depending on the number of items present.

`content`

    

A `View` to display when the user selects the item.

## See Also

### Creating a menu bar extra

`init(LocalizedStringKey, content: () -> Content)`

Creates a menu bar extra with a key for a localized string to use as the
label. The extra defines the primary scene of an `App`.

Available when `Label` is `Text` and `Content` conforms to `View`.

`init<S>(S, content: () -> Content)`

Creates a menu bar extra with a string to use as the label. The item defines
the primary scene of an `App`.

Available when `Label` is `Text` and `Content` conforms to `View`.

`init(content: () -> Content, label: () -> Label)`

Creates a menu bar extra that will be displayed in the system menu bar, and
defines the primary scene of an `App`.

`init<S>(S, isInserted: Binding<Bool>, content: () -> Content)`

Creates a menu bar extra with a string to use as the label. The item will be
displayed in the system menu bar when the specified binding is set to `true`.
If the user removes the item from the menu bar, the binding will be set to
`false`.

Available when `Label` is `Text` and `Content` conforms to `View`.

`init(isInserted: Binding<Bool>, content: () -> Content, label: () -> Label)`

Creates a menu bar extra. The item will be displayed in the system menu bar
when the specified binding is set to `true`. If the user removes the item from
the menu bar, the binding will be set to `false`.

Initializer

# init(_:isInserted:content:)

Creates a menu bar extra with a string to use as the label. The item will be
displayed in the system menu bar when the specified binding is set to `true`.
If the user removes the item from the menu bar, the binding will be set to
`false`.

macOS 13.0+

    
    
    init<S>(
        _ title: S,
        isInserted: Binding<Bool>,
        @ViewBuilder content: () -> Content
    ) where S : StringProtocol

Available when `Label` is `Text` and `Content` conforms to `View`.

##  Parameters

`title`

    

The string to use for the label of the item.

`isInserted`

    

Whether the item is inserted in the menu bar. The item may or may not be
visible, depending on the number of items present.

`content`

    

A `View` to display when the user selects the item.

## See Also

### Creating a menu bar extra

`init(LocalizedStringKey, content: () -> Content)`

Creates a menu bar extra with a key for a localized string to use as the
label. The extra defines the primary scene of an `App`.

Available when `Label` is `Text` and `Content` conforms to `View`.

`init<S>(S, content: () -> Content)`

Creates a menu bar extra with a string to use as the label. The item defines
the primary scene of an `App`.

Available when `Label` is `Text` and `Content` conforms to `View`.

`init(content: () -> Content, label: () -> Label)`

Creates a menu bar extra that will be displayed in the system menu bar, and
defines the primary scene of an `App`.

`init(LocalizedStringKey, isInserted: Binding<Bool>, content: () -> Content)`

Creates a menu bar extra with a key for a localized string to use as the
label. The item will be displayed in the system menu bar when the specified
binding is set to `true`. If the user removes the item from the menu bar, the
binding will be set to `false`.

Available when `Label` is `Text` and `Content` conforms to `View`.

`init(isInserted: Binding<Bool>, content: () -> Content, label: () -> Label)`

Creates a menu bar extra. The item will be displayed in the system menu bar
when the specified binding is set to `true`. If the user removes the item from
the menu bar, the binding will be set to `false`.

Initializer

# init(isInserted:content:label:)

Creates a menu bar extra. The item will be displayed in the system menu bar
when the specified binding is set to `true`. If the user removes the item from
the menu bar, the binding will be set to `false`.

macOS 13.0+

    
    
    init(
        isInserted: Binding<Bool>,
        @ViewBuilder content: () -> Content,
        @ViewBuilder label: () -> Label
    )

##  Parameters

`isInserted`

    

Whether the item is inserted in the menu bar. The item may or may not be
visible, depending on the number of items present.

`content`

    

A `View` to display when the user selects the item.

`label`

    

A `View` to use as the label in the system menu bar.

## See Also

### Creating a menu bar extra

`init(LocalizedStringKey, content: () -> Content)`

Creates a menu bar extra with a key for a localized string to use as the
label. The extra defines the primary scene of an `App`.

Available when `Label` is `Text` and `Content` conforms to `View`.

`init<S>(S, content: () -> Content)`

Creates a menu bar extra with a string to use as the label. The item defines
the primary scene of an `App`.

Available when `Label` is `Text` and `Content` conforms to `View`.

`init(content: () -> Content, label: () -> Label)`

Creates a menu bar extra that will be displayed in the system menu bar, and
defines the primary scene of an `App`.

`init(LocalizedStringKey, isInserted: Binding<Bool>, content: () -> Content)`

Creates a menu bar extra with a key for a localized string to use as the
label. The item will be displayed in the system menu bar when the specified
binding is set to `true`. If the user removes the item from the menu bar, the
binding will be set to `false`.

Available when `Label` is `Text` and `Content` conforms to `View`.

`init<S>(S, isInserted: Binding<Bool>, content: () -> Content)`

Creates a menu bar extra with a string to use as the label. The item will be
displayed in the system menu bar when the specified binding is set to `true`.
If the user removes the item from the menu bar, the binding will be set to
`false`.

Available when `Label` is `Text` and `Content` conforms to `View`.

Initializer

# init(_:image:content:)

Creates a menu bar extra with a named image to use as the items label. The
provided title will be used by the accessibility system.

macOS 13.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        image: String,
        @ViewBuilder content: () -> Content
    )

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

##  Parameters

`titleKey`

    

The localized string key to use for the accessibility label of the item.

`image`

    

The name of an image in the app’s bundle to use as the label.

`content`

    

A `View` to display when the user selects the item.

## Discussion

The item defines the primary scene of an `App`.

When this item is removed from the system menu bar by the user, the
application will be automatically quit. As such, it should not be used in
conjunction with other scene types in your `App`.

## See Also

### Creating a menu bar extra with a named image

`init(LocalizedStringKey, image: String, isInserted: Binding<Bool>, content:
() -> Content)`

Creates a menu bar extra with a named image to use as the items label. The
provided title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init<S>(S, image: String, content: () -> Content)`

Creates a menu bar extra with a named image to use as the items label. The
provided title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init<S>(S, image: String, isInserted: Binding<Bool>, content: () -> Content)`

Creates a menu bar extra with a named image to use as the items label. The
provided title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

Initializer

# init(_:image:isInserted:content:)

Creates a menu bar extra with a named image to use as the items label. The
provided title will be used by the accessibility system.

macOS 13.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        image: String,
        isInserted: Binding<Bool>,
        @ViewBuilder content: () -> Content
    )

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

##  Parameters

`titleKey`

    

The localized string key to use for the accessibility label of the item.

`image`

    

The name of an image in the app’s bundle to use as the label.

`isInserted`

    

Whether the item is inserted in the menu bar. The item may or may not be
visible, depending on the number of items present.

`content`

    

A `View` to display when the user selects the item.

## Discussion

The item will be displayed in the system menu bar when the specified binding
is set to `true`. If the user removes the item from the menu bar, the binding
will be set to `false`.

## See Also

### Creating a menu bar extra with a named image

`init(LocalizedStringKey, image: String, content: () -> Content)`

Creates a menu bar extra with a named image to use as the items label. The
provided title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init<S>(S, image: String, content: () -> Content)`

Creates a menu bar extra with a named image to use as the items label. The
provided title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init<S>(S, image: String, isInserted: Binding<Bool>, content: () -> Content)`

Creates a menu bar extra with a named image to use as the items label. The
provided title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

Initializer

# init(_:image:content:)

Creates a menu bar extra with a named image to use as the items label. The
provided title will be used by the accessibility system.

macOS 13.0+

    
    
    init<S>(
        _ title: S,
        image: String,
        @ViewBuilder content: () -> Content
    ) where S : StringProtocol

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

##  Parameters

`title`

    

The string to use for the accessibility label of the item.

`image`

    

The name of an image in the app’s bundle to use as the label.

`content`

    

A `View` to display when the user selects the item.

## Discussion

The item defines the primary scene of an `App`.

When this item is removed from the system menu bar by the user, the
application will be automatically quit. As such, it should not be used in
conjunction with other scene types in your `App`.

## See Also

### Creating a menu bar extra with a named image

`init(LocalizedStringKey, image: String, content: () -> Content)`

Creates a menu bar extra with a named image to use as the items label. The
provided title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init(LocalizedStringKey, image: String, isInserted: Binding<Bool>, content:
() -> Content)`

Creates a menu bar extra with a named image to use as the items label. The
provided title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init<S>(S, image: String, isInserted: Binding<Bool>, content: () -> Content)`

Creates a menu bar extra with a named image to use as the items label. The
provided title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

Initializer

# init(_:image:isInserted:content:)

Creates a menu bar extra with a named image to use as the items label. The
provided title will be used by the accessibility system.

macOS 13.0+

    
    
    init<S>(
        _ title: S,
        image: String,
        isInserted: Binding<Bool>,
        @ViewBuilder content: () -> Content
    ) where S : StringProtocol

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

##  Parameters

`title`

    

The string to use for the accessibility label of the item.

`image`

    

The name of an image in the app’s bundle to use as the label.

`isInserted`

    

Whether the item is inserted in the menu bar. The item may or may not be
visible, depending on the number of items present.

`content`

    

A `View` to display when the user selects the item.

## Discussion

The item will be displayed in the system menu bar when the specified binding
is set to `true`. If the user removes the item from the menu bar, the binding
will be set to `false`.

## See Also

### Creating a menu bar extra with a named image

`init(LocalizedStringKey, image: String, content: () -> Content)`

Creates a menu bar extra with a named image to use as the items label. The
provided title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init(LocalizedStringKey, image: String, isInserted: Binding<Bool>, content:
() -> Content)`

Creates a menu bar extra with a named image to use as the items label. The
provided title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init<S>(S, image: String, content: () -> Content)`

Creates a menu bar extra with a named image to use as the items label. The
provided title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

Initializer

# init(_:systemImage:content:)

Creates a menu bar extra with a system image to use as the items label. The
provided title will be used by the accessibility system.

macOS 13.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        systemImage: String,
        @ViewBuilder content: () -> Content
    )

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

##  Parameters

`titleKey`

    

The localized string key to use for the accessibility label of the item.

`systemImage`

    

The name of a system image to use as the label.

`content`

    

A `View` to display when the user selects the item.

## Discussion

The item defines the primary scene of an `App`.

When this item is removed from the system menu bar by the user, the
application will be automatically quit. As such, it should not be used in
conjunction with other scene types in your `App`.

## See Also

### Creating a menu bar extra with a system image

`init(LocalizedStringKey, systemImage: String, isInserted: Binding<Bool>,
content: () -> Content)`

Creates a menu bar extra with a system image to use as the items label. The
provided title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init<S>(S, systemImage: String, content: () -> Content)`

Creates a menu bar extra with a system image to use as the items label. The
provided title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init<S>(S, systemImage: String, isInserted: Binding<Bool>, content: () ->
Content)`

Creates a menu bar extra with a system image to use as the items label. The
provided title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

Initializer

# init(_:systemImage:isInserted:content:)

Creates a menu bar extra with a system image to use as the items label. The
provided title will be used by the accessibility system.

macOS 13.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        systemImage: String,
        isInserted: Binding<Bool>,
        @ViewBuilder content: () -> Content
    )

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

##  Parameters

`titleKey`

    

The localized string key to use for the accessibility label of the item.

`systemImage`

    

The name of a system image to use as the label.

`isInserted`

    

Whether the item is inserted in the menu bar. The item may or may not be
visible, depending on the number of items present.

`content`

    

A `View` to display when the user selects the item.

## Discussion

The item will be displayed in the system menu bar when the specified binding
is set to `true`. If the user removes the item from the menu bar, the binding
will be set to `false`.

## See Also

### Creating a menu bar extra with a system image

`init(LocalizedStringKey, systemImage: String, content: () -> Content)`

Creates a menu bar extra with a system image to use as the items label. The
provided title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init<S>(S, systemImage: String, content: () -> Content)`

Creates a menu bar extra with a system image to use as the items label. The
provided title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init<S>(S, systemImage: String, isInserted: Binding<Bool>, content: () ->
Content)`

Creates a menu bar extra with a system image to use as the items label. The
provided title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

Initializer

# init(_:systemImage:content:)

Creates a menu bar extra with a system image to use as the items label. The
provided title will be used by the accessibility system.

macOS 13.0+

    
    
    init<S>(
        _ title: S,
        systemImage: String,
        @ViewBuilder content: () -> Content
    ) where S : StringProtocol

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

##  Parameters

`title`

    

The string to use for the accessibility label of the item.

`systemImage`

    

The name of a system image to use as the label.

`content`

    

A `View` to display when the user selects the item.

## Discussion

The item defines the primary scene of an `App`.

When this item is removed from the system menu bar by the user, the
application will be automatically quit. As such, it should not be used in
conjunction with other scene types in your `App`.

## See Also

### Creating a menu bar extra with a system image

`init(LocalizedStringKey, systemImage: String, content: () -> Content)`

Creates a menu bar extra with a system image to use as the items label. The
provided title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init(LocalizedStringKey, systemImage: String, isInserted: Binding<Bool>,
content: () -> Content)`

Creates a menu bar extra with a system image to use as the items label. The
provided title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init<S>(S, systemImage: String, isInserted: Binding<Bool>, content: () ->
Content)`

Creates a menu bar extra with a system image to use as the items label. The
provided title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

Initializer

# init(_:systemImage:isInserted:content:)

Creates a menu bar extra with a system image to use as the items label. The
provided title will be used by the accessibility system.

macOS 13.0+

    
    
    init<S>(
        _ title: S,
        systemImage: String,
        isInserted: Binding<Bool>,
        @ViewBuilder content: () -> Content
    ) where S : StringProtocol

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

##  Parameters

`title`

    

The string to use for the accessibility label of the item.

`systemImage`

    

The name of a system image to use as the label.

`isInserted`

    

Whether the item is inserted in the menu bar. The item may or may not be
visible, depending on the number of items present.

`content`

    

A `View` to display when the user selects the item.

## Discussion

The item will be displayed in the system menu bar when the specified binding
is set to `true`. If the user removes the item from the menu bar, the binding
will be set to `false`.

## See Also

### Creating a menu bar extra with a system image

`init(LocalizedStringKey, systemImage: String, content: () -> Content)`

Creates a menu bar extra with a system image to use as the items label. The
provided title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init(LocalizedStringKey, systemImage: String, isInserted: Binding<Bool>,
content: () -> Content)`

Creates a menu bar extra with a system image to use as the items label. The
provided title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init<S>(S, systemImage: String, content: () -> Content)`

Creates a menu bar extra with a system image to use as the items label. The
provided title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

Initializer

# init(_:image:content:)

Creates a menu bar extra with an image to use as the items label. The provided
title will be used by the accessibility system.

macOS 14.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        image: ImageResource,
        @ViewBuilder content: () -> Content
    )

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

##  Parameters

`titleKey`

    

The localized string key to use for the accessibility label of the item.

`image`

    

The image resource to use as the label.

`content`

    

A `View` to display when the user selects the item.

## Discussion

The item defines the primary scene of an `App`.

When this item is removed from the system menu bar by the user, the
application will be automatically quit. As such, it should not be used in
conjunction with other scene types in your `App`.

## See Also

### Creating a menu bar extra with an image resource

`init(LocalizedStringKey, image: ImageResource, isInserted: Binding<Bool>,
content: () -> Content)`

Creates a menu bar extra with an image to use as the items label. The provided
title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init<S>(S, image: ImageResource, content: () -> Content)`

Creates a menu bar extra with an image to use as the items label. The provided
title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init<S>(S, image: ImageResource, isInserted: Binding<Bool>, content: () ->
Content)`

Creates a menu bar extra with an image to use as the items label. The provided
title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

Initializer

# init(_:image:isInserted:content:)

Creates a menu bar extra with an image to use as the items label. The provided
title will be used by the accessibility system.

macOS 14.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        image: ImageResource,
        isInserted: Binding<Bool>,
        @ViewBuilder content: () -> Content
    )

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

##  Parameters

`titleKey`

    

The localized string key to use for the accessibility label of the item.

`image`

    

The image resource to use as the label.

`isInserted`

    

Whether the item is inserted in the menu bar. The item may or may not be
visible, depending on the number of items present.

`content`

    

A `View` to display when the user selects the item.

## Discussion

The item will be displayed in the system menu bar when the specified binding
is set to `true`. If the user removes the item from the menu bar, the binding
will be set to `false`.

## See Also

### Creating a menu bar extra with an image resource

`init(LocalizedStringKey, image: ImageResource, content: () -> Content)`

Creates a menu bar extra with an image to use as the items label. The provided
title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init<S>(S, image: ImageResource, content: () -> Content)`

Creates a menu bar extra with an image to use as the items label. The provided
title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init<S>(S, image: ImageResource, isInserted: Binding<Bool>, content: () ->
Content)`

Creates a menu bar extra with an image to use as the items label. The provided
title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

Initializer

# init(_:image:content:)

Creates a menu bar extra with an image to use as the items label. The provided
title will be used by the accessibility system.

macOS 14.0+

    
    
    init<S>(
        _ title: S,
        image: ImageResource,
        @ViewBuilder content: () -> Content
    ) where S : StringProtocol

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

##  Parameters

`title`

    

The string to use for the accessibility label of the item.

`image`

    

The image resource to use as the label.

`content`

    

A `View` to display when the user selects the item.

## Discussion

The item defines the primary scene of an `App`.

When this item is removed from the system menu bar by the user, the
application will be automatically quit. As such, it should not be used in
conjunction with other scene types in your `App`.

## See Also

### Creating a menu bar extra with an image resource

`init(LocalizedStringKey, image: ImageResource, content: () -> Content)`

Creates a menu bar extra with an image to use as the items label. The provided
title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init(LocalizedStringKey, image: ImageResource, isInserted: Binding<Bool>,
content: () -> Content)`

Creates a menu bar extra with an image to use as the items label. The provided
title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init<S>(S, image: ImageResource, isInserted: Binding<Bool>, content: () ->
Content)`

Creates a menu bar extra with an image to use as the items label. The provided
title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

Initializer

# init(_:image:isInserted:content:)

Creates a menu bar extra with an image to use as the items label. The provided
title will be used by the accessibility system.

macOS 14.0+

    
    
    init<S>(
        _ title: S,
        image: ImageResource,
        isInserted: Binding<Bool>,
        @ViewBuilder content: () -> Content
    ) where S : StringProtocol

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

##  Parameters

`title`

    

The string to use for the accessibility label of the item.

`image`

    

The image resource to use as the label.

`isInserted`

    

Whether the item is inserted in the menu bar. The item may or may not be
visible, depending on the number of items present.

`content`

    

A `View` to display when the user selects the item.

## Discussion

The item will be displayed in the system menu bar when the specified binding
is set to `true`. If the user removes the item from the menu bar, the binding
will be set to `false`.

## See Also

### Creating a menu bar extra with an image resource

`init(LocalizedStringKey, image: ImageResource, content: () -> Content)`

Creates a menu bar extra with an image to use as the items label. The provided
title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init(LocalizedStringKey, image: ImageResource, isInserted: Binding<Bool>,
content: () -> Content)`

Creates a menu bar extra with an image to use as the items label. The provided
title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init<S>(S, image: ImageResource, content: () -> Content)`

Creates a menu bar extra with an image to use as the items label. The provided
title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.



# MenuPickerStyle

Initializer

# init()

Creates a menu picker style.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 17.0+  visionOS
1.0+

    
    
    init()



# MapContent Implementations

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



# MenuControlGroupStyle

Initializer

# init()

Creates a menu control group style.

iOS 16.4+  iPadOS 16.4+  macOS 13.3+  Mac Catalyst 16.4+  tvOS 17.0+  visionOS
1.0+

    
    
    init()



# Model data

Article

# Managing user interface state

Encapsulate view-specific data within your app’s view hierarchy to make your
views reusable.

## Overview

Store data as state in the least common ancestor of the views that need the
data to establish a single _source of truth_ that’s shared across views.
Provide the data as read-only through a Swift property, or create a two-way
connection to the state with a binding. SwiftUI watches for changes in the
data, and updates any affected views as needed.

Don’t use state properties for persistent storage because the life cycle of
state variables mirrors the view life cycle. Instead, use them to manage
transient state that only affects the user interface, like the highlight state
of a button, filter settings, or the currently selected list item. You might
also find this kind of storage convenient while you prototype, before you’re
ready to make changes to your app’s data model.

### Manage mutable values as state

If a view needs to store data that it can modify, declare a variable with the
`State` property wrapper. For example, you can create an `isPlaying` Boolean
inside a podcast player view to keep track of when a podcast is running:

Marking the property as state tells the framework to manage the underlying
storage. Your view reads and writes the data, found in the state’s
`wrappedValue` property, by using the property name. When you change the
value, SwiftUI updates the affected parts of the view. For example, you can
add a button to the `PlayerView` that toggles the stored value when tapped,
and that displays a different image depending on the stored value:

Limit the scope of state variables by declaring them as private. This ensures
that the variables remain encapsulated in the view hierarchy that declares
them.

### Declare Swift properties to store immutable values

To provide a view with data that the view doesn’t modify, declare a standard
Swift property. For example, you can extend the podcast player to have an
input structure that contains strings for the episode title and the show name:

While the value of the episode property is a constant for `PlayerView`, it
doesn’t need to be constant in this view’s parent view. When the user selects
a different episode in the parent, SwiftUI detects the state change and
recreates the `PlayerView` with a new input.

### Share access to state with bindings

If a view needs to share control of state with a child view, declare a
property in the child with the `Binding` property wrapper. A binding
represents a reference to existing storage, preserving a single source of
truth for the underlying data. For example, if you refactor the podcast player
view’s button into a child view called `PlayButton`, you can give it a binding
to the `isPlaying` property:

As shown above, you read and write the binding’s wrapped value by referring
directly to the property, just like state. But unlike a state property, the
binding doesn’t have its own storage. Instead, it references a state property
stored somewhere else, and provides a two-way connection to that storage.

When you instantiate `PlayButton`, provide a binding to the corresponding
state variable declared in the parent view by prefixing it with the dollar
sign (`$`):

The `$` prefix asks a wrapped property for its `projectedValue`, which for
state is a binding to the underlying storage. Similarly, you can get a binding
from a binding using the `$` prefix, allowing you to pass a binding through an
arbitrary number of levels of view hierarchy.

You can also get a binding to a scoped value within a state variable. For
example, if you declare `episode` as a state variable in the player’s parent
view, and the episode structure also contains an `isFavorite` Boolean that you
want to control with a toggle, then you can refer to `$episode.isFavorite` to
get a binding to the episode’s favorite status:

### Animate state transitions

When the view state changes, SwiftUI updates affected views right away. If you
want to smooth visual transitions, you can tell SwiftUI to animate them by
wrapping the state change that triggers them in a call to the
`withAnimation(_:_:)` function. For example, you can animate changes
controlled by the `isPlaying` Boolean:

By changing `isPlaying` inside the animation function’s trailing closure, you
tell SwiftUI to animate anything that depends on the wrapped value, like a
scale effect on the button’s image:

SwiftUI transitions the scale effect input over time between the given values
of `1` and `1.5`, using the curve and duration that you specify, or reasonable
default values if you provide none. On the other hand, the image content isn’t
affected by the animation, even though the same Boolean dictates which system
image to display. That’s because SwiftUI can’t incrementally transition in a
meaningful way between the two strings `pause.circle` and `play.circle`.

You can add animation to a state property, or as in the above example, to a
binding. Either way, SwiftUI animates any view changes that happen when the
underlying stored value changes. For example, if you add a background color to
the `PlayerView` — at a level of view hierarchy above the location of the
animation block — SwiftUI animates that as well:

When you want to apply animations to specific views, rather than across all
views triggered by a change in state, use the `animation(_:value:)` view
modifier instead.

## See Also

### Creating and sharing view state

`struct State`

A property wrapper type that can read and write a value managed by SwiftUI.

`struct Bindable`

A property wrapper type that supports creating bindings to the mutable
properties of observable objects.

`struct Binding`

A property wrapper type that can read and write a value owned by a source of
truth.

Structure

# State

A property wrapper type that can read and write a value managed by SwiftUI.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen @propertyWrapper
    struct State<Value>

## Overview

Use state as the single source of truth for a given value type that you store
in a view hierarchy. Create a state value in an `App`, `Scene`, or `View` by
applying the `@State` attribute to a property declaration and providing an
initial value. Declare state as private to prevent setting it in a memberwise
initializer, which can conflict with the storage management that SwiftUI
provides:

SwiftUI manages the property’s storage. When the value changes, SwiftUI
updates the parts of the view hierarchy that depend on the value. To access a
state’s underlying value, you use its `wrappedValue` property. However, as a
shortcut Swift enables you to access the wrapped value by referring directly
to the state instance. The above example reads and writes the `isPlaying`
state property’s wrapped value by referring to the property directly.

Declare state as private in the highest view in the view hierarchy that needs
access to the value. Then share the state with any subviews that also need
access, either directly for read-only access, or as a binding for read-write
access. You can safely mutate state properties from any thread.

### Share state with subviews

If you pass a state property to a subview, SwiftUI updates the subview any
time the value changes in the container view, but the subview can’t modify the
value. To enable the subview to modify the state’s stored value, pass a
`Binding` instead.

For example, you can remove the `isPlaying` state from the play button in the
above example, and instead make the button take a binding:

Then you can define a player view that declares the state and creates a
binding to the state. Get the binding to the state value by accessing the
state’s `projectedValue`, which you get by prefixing the property name with a
dollar sign (`$`):

Like you do for a `StateObject`, declare `State` as private to prevent setting
it in a memberwise initializer, which can conflict with the storage management
that SwiftUI provides. Unlike a state object, always initialize state by
providing a default value in the state’s declaration, as in the above
examples. Use state only for storage that’s local to a view and its subviews.

### Store observable objects

You can also store observable objects that you create with the `Observable()`
macro in `State`; for example:

A `State` property always instantiates its default value when SwiftUI
instantiates the view. For this reason, avoid side effects and performance-
intensive work when initializing the default value. For example, if a view
updates frequently, allocating a new default object each time the view
initializes can become expensive. Instead, you can defer the creation of the
object using the `task(priority:_:)` modifier, which is called only once when
the view first appears:

Delaying the creation of the observable state object ensures that unnecessary
allocations of the object doesn’t happen each time SwiftUI initializes the
view. Using the `task(priority:_:)` modifier is also an effective way to defer
any other kind of work required to create the initial state of the view, such
as network calls or file access.

Note

It’s possible to store an object that conforms to the `ObservableObject`
protocol in a `State` property. However the view will only update when the
reference to the object changes, such as when setting the property with a
reference to another object. The view will not update if any of the object’s
published properties change. To track changes to both the reference and the
object’s published properties, use `StateObject` instead of `State` when
storing the object.

### Share observable state objects with subviews

To share an `Observable` object stored in `State` with a subview, pass the
object reference to the subview. SwiftUI updates the subview anytime an
observable property of the object changes, but only when the subview’s `body`
reads the property. For example, in the following code `BookView` updates each
time `title` changes but not when `isAvailable` changes:

`State` properties provide bindings to their value. When storing an object,
you can get a `Binding` to that object, specifically the reference to the
object. This is useful when you need to change the reference stored in state
in some other subview, such as setting the reference to `nil`:

However, passing a `Binding` to an object stored in `State` isn’t necessary
when you need to change properties of that object. For example, you can set
the properties of the object to new values in a subview by passing the object
reference instead of a binding to the reference:

If you need a binding to a specific property of the object, pass either the
binding to the object and extract bindings to specific properties where
needed, or pass the object reference and use the `Bindable` property wrapper
to create bindings to specific properties. For example, in the following code
`BookEditorView` wraps `book` with `@Bindable`. Then the view uses the `$`
syntax to pass to a `TextField` a binding to `title`:

## Topics

### Creating a state

`init(wrappedValue: Value)`

Creates a state property that stores an initial wrapped value.

`init(initialValue: Value)`

Creates a state property that stores an initial value.

`init()`

Creates a state property without an initial value.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

### Getting the value

`var wrappedValue: Value`

The underlying value referenced by the state variable.

`var projectedValue: Binding<Value>`

A binding to the state value.

## Relationships

### Conforms To

  * `DynamicProperty`

## See Also

### Creating and sharing view state

Managing user interface state

Encapsulate view-specific data within your app’s view hierarchy to make your
views reusable.

`struct Bindable`

A property wrapper type that supports creating bindings to the mutable
properties of observable objects.

`struct Binding`

A property wrapper type that can read and write a value owned by a source of
truth.

Structure

# Bindable

A property wrapper type that supports creating bindings to the mutable
properties of observable objects.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    @dynamicMemberLookup @propertyWrapper
    struct Bindable<Value>

## Overview

Use this property wrapper to create bindings to mutable properties of a data
model object that conforms to the `Observable` protocol. For example, the
following code wraps the `book` input with `@Bindable`. Then it uses a
`TextField` to change the `title` property of a book, and a `Toggle` to change
the `isAvailable` property, using the `$` syntax to pass a binding for each
property to those controls.

You can use the `Bindable` property wrapper on properties and variables to an
`Observable` object. This includes global variables, properties that exists
outside of SwiftUI types, or even local variables. For example, you can create
a `@Bindable` variable within a view’s `body`:

The `@Bindable` variable `book` provides a binding that connects `TextField`
to the `title` property of a book so that a person can make changes directly
to the model data.

Use this same approach when you need a binding to a property of an observable
object stored in a view’s environment. For example, the following code uses
the `Environment` property wrapper to retrieve an instance of the observable
type `Book`. Then the code creates a `@Bindable` variable `book` and passes a
binding for the `title` property to a `TextField` using the `$` syntax.

## Topics

### Creating a bindable value

`init(Value)`

Creates a bindable object from an observable object.

Available when `Value` conforms to `Observable`.

`init(wrappedValue: Value)`

Creates a bindable object from an observable object.

Available when `Value` conforms to `Observable`.

`init(projectedValue: Bindable<Value>)`

Creates a bindable from the value of another bindable.

Available when `Value` conforms to `Observable`.

### Getting the value

`var wrappedValue: Value`

The wrapped object.

`var projectedValue: Bindable<Value>`

The bindable wrapper for the object that creates bindings to its properties
using dynamic member lookup.

`subscript<Subject>(dynamicMember _: ReferenceWritableKeyPath<Value, Subject>)
-> Binding<Subject>`

Returns a binding to the value of a given key path.

## Relationships

### Conforms To

  * `Identifiable`
  * `Sendable`

## See Also

### Creating and sharing view state

Managing user interface state

Encapsulate view-specific data within your app’s view hierarchy to make your
views reusable.

`struct State`

A property wrapper type that can read and write a value managed by SwiftUI.

`struct Binding`

A property wrapper type that can read and write a value owned by a source of
truth.

Structure

# Binding

A property wrapper type that can read and write a value owned by a source of
truth.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen @propertyWrapper @dynamicMemberLookup
    struct Binding<Value>

## Overview

Use a binding to create a two-way connection between a property that stores
data, and a view that displays and changes the data. A binding connects a
property to a source of truth stored elsewhere, instead of storing data
directly. For example, a button that toggles between play and pause can create
a binding to a property of its parent view using the `Binding` property
wrapper.

The parent view declares a property to hold the playing state, using the
`State` property wrapper to indicate that this property is the value’s source
of truth.

When `PlayerView` initializes `PlayButton`, it passes a binding of its state
property into the button’s binding property. Applying the `$` prefix to a
property wrapped value returns its `projectedValue`, which for a state
property wrapper returns a binding to the value.

Whenever the user taps the `PlayButton`, the `PlayerView` updates its
`isPlaying` state.

Note

To create bindings to properties of a type that conforms to the `Observable`
protocol, use the `Bindable` property wrapper. For more information, see
Migrating from the Observable Object protocol to the Observable macro.

## Topics

### Creating a binding

`init?(Binding<Value?>)`

Creates a binding by projecting the base value to an unwrapped value.

`init<V>(Binding<V>)`

Creates a binding by projecting the base value to an optional value.

`init<V>(Binding<V>)`

Creates a binding by projecting the base value to a hashable value.

`init(projectedValue: Binding<Value>)`

Creates a binding from the value of another binding.

`init(get: () -> Value, set: (Value, Transaction) -> Void)`

Creates a binding with a closure that reads from the binding value, and a
closure that applies a transaction when writing to the binding value.

`init(get: () -> Value, set: (Value) -> Void)`

Creates a binding with closures that read and write the binding value.

`static func constant(Value) -> Binding<Value>`

Creates a binding with an immutable value.

### Getting the value

`var wrappedValue: Value`

The underlying value referenced by the binding variable.

`var projectedValue: Binding<Value>`

A projection of the binding value that returns a binding.

`subscript<Subject>(dynamicMember _: WritableKeyPath<Value, Subject>) ->
Binding<Subject>`

Returns a binding to the resulting value of a given key path.

### Managing changes

`var id: Value.ID`

The stable identity of the entity associated with this instance, corresponding
to the `id` of the binding’s wrapped value.

Available when `Value` conforms to `Identifiable`.

`func animation(Animation?) -> Binding<Value>`

Specifies an animation to perform when the binding value changes.

`func transaction(Transaction) -> Binding<Value>`

Specifies a transaction for the binding.

`var transaction: Transaction`

The binding’s transaction.

### Default Implementations

API Reference

Identifiable Implementations

## Relationships

### Conforms To

  * `BidirectionalCollection`
  * `Collection`
  * `DynamicProperty`
  * `Identifiable`
  * `RandomAccessCollection`
  * `Sequence`

## See Also

### Creating and sharing view state

Managing user interface state

Encapsulate view-specific data within your app’s view hierarchy to make your
views reusable.

`struct State`

A property wrapper type that can read and write a value managed by SwiftUI.

`struct Bindable`

A property wrapper type that supports creating bindings to the mutable
properties of observable objects.

Macro

# Observable()

Defines and implements conformance of the Observable protocol.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    @attached(member, names: named(_$observationRegistrar), named(access), named(withMutation)) @attached(memberAttribute) @attached(extension, conformances: Observable) macro Observable()

## Overview

This macro adds observation support to a custom type and conforms the type to
the `Observable` protocol. For example, the following code applies the
`Observable` macro to the type `Car` making it observable:

## See Also

### Observable conformance

`protocol Observable`

A type that emits notifications to observers when underlying data changes.

Structure

# StateObject

A property wrapper type that instantiates an observable object.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    @frozen @propertyWrapper
    struct StateObject<ObjectType> where ObjectType : ObservableObject

## Overview

Use a state object as the single source of truth for a reference type that you
store in a view hierarchy. Create a state object in an `App`, `Scene`, or
`View` by applying the `@StateObject` attribute to a property declaration and
providing an initial value that conforms to the `ObservableObject` protocol.
Declare state objects as private to prevent setting them from a memberwise
initializer, which can conflict with the storage management that SwiftUI
provides:

SwiftUI creates a new instance of the model object only once during the
lifetime of the container that declares the state object. For example, SwiftUI
doesn’t create a new instance if a view’s inputs change, but does create a new
instance if the identity of a view changes. When published properties of the
observable object change, SwiftUI updates any view that depends on those
properties, like the `Text` view in the above example.

Note

If you need to store a value type, like a structure, string, or integer, use
the `State` property wrapper instead. Also use `State` if you need to store a
reference type that conforms to the `Observable()` protocol. To learn more
about Observation in SwiftUI, see Managing model data in your app.

### Share state objects with subviews

You can pass a state object into a subview through a property that has the
`ObservedObject` attribute. Alternatively, add the object to the environment
of a view hierarchy by applying the `environmentObject(_:)` modifier to a
view, like `MySubView` in the above code. You can then read the object inside
`MySubView` or any of its descendants using the `EnvironmentObject` attribute:

Get a `Binding` to the state object’s properties using the dollar sign (`$`)
operator. Use a binding when you want to create a two-way connection. In the
above code, the `Toggle` controls the model’s `isEnabled` value through a
binding.

### Initialize state objects using external data

When a state object’s initial state depends on data that comes from outside
its container, you can call the object’s initializer explicitly from within
its container’s initializer. For example, suppose the data model from the
previous example takes a `name` input during initialization and you want to
use a value for that name that comes from outside the view. You can do this
with a call to the state object’s initializer inside an explicit initializer
that you create for the view:

Use caution when doing this. SwiftUI only initializes a state object the first
time you call its initializer in a given view. This ensures that the object
provides stable storage even as the view’s inputs change. However, it might
result in unexpected behavior or unwanted side effects if you explicitly
initialize the state object.

In the above example, if the `name` input to `MyInitializableView` changes,
SwiftUI reruns the view’s initializer with the new value. However, SwiftUI
runs the autoclosure that you provide to the state object’s initializer only
the first time you call the state object’s initializer, so the model’s stored
`name` value doesn’t change.

Explicit state object initialization works well when the external data that
the object depends on doesn’t change for a given instance of the object’s
container. For example, you can create two views with different constant
names:

Important

Even for a configurable state object, you still declare it as private. This
ensures that you can’t accidentally set the parameter through a memberwise
initializer of the view, because doing so can conflict with the framework’s
storage management and produce unexpected results.

### Force reinitialization by changing view identity

If you want SwiftUI to reinitialize a state object when a view input changes,
make sure that the view’s identity changes at the same time. One way to do
this is to bind the view’s identity to the value that changes using the
`id(_:)` modifier. For example, you can ensure that the identity of an
instance of `MyInitializableView` changes when its `name` input changes:

Note

If your view appears inside a `ForEach`, it implicitly receives an `id(_:)`
modifier that uses the identifier of the corresponding data element.

If you need the view to reinitialize state based on changes in more than one
value, you can combine the values into a single identifier using a `Hasher`.
For example, if you want to update the data model in `MyInitializableView`
when the values of either `name` or `isEnabled` change, you can combine both
variables into a single hash:

Then apply the combined hash to the view as an identifier:

Be mindful of the performance cost of reinitializing the state object every
time the input changes. Also, changing view identity can have side effects.
For example, SwiftUI doesn’t automatically animate changes inside the view if
the view’s identity changes at the same time. Also, changing the identity
resets _all_ state held by the view, including values that you manage as
`State`, `FocusState`, `GestureState`, and so on.

## Topics

### Creating a state object

`init(wrappedValue: () -> ObjectType)`

Creates a new state object with an initial wrapped value.

### Getting the value

`var wrappedValue: ObjectType`

The underlying value referenced by the state object.

`var projectedValue: ObservedObject<ObjectType>.Wrapper`

A projection of the state object that creates bindings to its properties.

## Relationships

### Conforms To

  * `DynamicProperty`

## See Also

### Creating model data

Managing model data in your app

Create connections between your app’s data model and views.

Migrating from the Observable Object protocol to the Observable macro

Update your existing app to leverage the benefits of Observation in Swift.

`macro Observable()`

Defines and implements conformance of the Observable protocol.

Monitoring data changes in your app

Show changes to data in your app’s user interface by using observable objects.

`struct ObservedObject`

A property wrapper type that subscribes to an observable object and
invalidates a view whenever the observable object changes.

`protocol ObservableObject`

A type of object with a publisher that emits before the object has changed.

Structure

# ObservedObject

A property wrapper type that subscribes to an observable object and
invalidates a view whenever the observable object changes.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @propertyWrapper @frozen
    struct ObservedObject<ObjectType> where ObjectType : ObservableObject

## Overview

Add the `@ObservedObject` attribute to a parameter of a SwiftUI `View` when
the input is an `ObservableObject` and you want the view to update when the
object’s published properties change. You typically do this to pass a
`StateObject` into a subview.

The following example defines a data model as an observable object,
instantiates the model in a view as a state object, and then passes the
instance to a subview as an observed object:

When any published property of the observable object changes, SwiftUI updates
any view that depends on the object. Subviews can also make updates to the
model properties, like the `Toggle` in the above example, that propagate to
other observers throughout the view hierarchy.

Don’t specify a default or initial value for the observed object. Use the
attribute only for a property that acts as an input for a view, as in the
above example.

Note

Don’t wrap objects conforming to the `Observable` protocol with
`@ObservedObject`. SwiftUI automatically tracks dependencies to `Observable`
objects used within body and updates dependent views when their data changes.
Attempting to wrap an `Observable` object with `@ObservedObject` may cause a
compiler error, because it requires that its wrapped object to conform to the
`ObservableObject` protocol.

If the view needs a binding to a property of an `Observable` object in its
body, wrap the object with the `Bindable` property wrapper instead; for
example, `@Bindable var model: DataModel`. For more information, see Managing
model data in your app.

## Topics

### Creating an observed object

`init(wrappedValue: ObjectType)`

Creates an observed object with an initial wrapped value.

`init(initialValue: ObjectType)`

Creates an observed object with an initial value.

### Getting the value

`var wrappedValue: ObjectType`

The underlying value that the observed object references.

`var projectedValue: ObservedObject<ObjectType>.Wrapper`

A projection of the observed object that creates bindings to its properties.

`struct Wrapper`

A wrapper of the underlying observable object that can create bindings to its
properties.

## Relationships

### Conforms To

  * `DynamicProperty`

## See Also

### Creating model data

Managing model data in your app

Create connections between your app’s data model and views.

Migrating from the Observable Object protocol to the Observable macro

Update your existing app to leverage the benefits of Observation in Swift.

`macro Observable()`

Defines and implements conformance of the Observable protocol.

Monitoring data changes in your app

Show changes to data in your app’s user interface by using observable objects.

`struct StateObject`

A property wrapper type that instantiates an observable object.

`protocol ObservableObject`

A type of object with a publisher that emits before the object has changed.

Protocol

# ObservableObject

A type of object with a publisher that emits before the object has changed.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    protocol ObservableObject : AnyObject

## Overview

By default an `ObservableObject` synthesizes an `objectWillChange` publisher
that emits the changed value before any of its `@Published` properties
changes.

## Topics

### Publishing Changes

`var objectWillChange: Self.ObjectWillChangePublisher`

A publisher that emits before the object has changed.

**Required** Default implementation provided.

`associatedtype ObjectWillChangePublisher : Publisher =
ObservableObjectPublisher`

The type of publisher that emits before the object has changed.

**Required**

## See Also

### Observable Objects

`class ObservableObjectPublisher`

A publisher that publishes changes from observable objects.

Instance Method

# onChange(of:initial:_:)

Adds a modifier for this view that fires an action when a specific value
changes.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func onChange<V>(
        of value: V,
        initial: Bool = false,
        _ action: @escaping () -> Void
    ) -> some View where V : Equatable
    

##  Parameters

`value`

    

The value to check against when determining whether to run the closure.

`initial`

    

Whether the action should be run when this view initially appears.

`action`

    

A closure to run when the value changes.

## Return Value

A view that fires an action when the specified value changes.

## Discussion

You can use `onChange` to trigger a side effect as the result of a value
changing, such as an `Environment` key or a `Binding`.

The system may call the action closure on the main actor, so avoid long-
running tasks in the closure. If you need to perform such tasks, detach an
asynchronous background task.

When the value changes, the new version of the closure will be called, so any
captured values will have their values from the time that the observed value
has its new value. In the following code example, `PlayerView` calls into its
model when `playState` changes model.

## See Also

### Responding to data changes

`func onChange<V>(of: V, initial: Bool, (V, V) -> Void) -> some View`

Adds a modifier for this view that fires an action when a specific value
changes.

`func onReceive<P>(P, perform: (P.Output) -> Void) -> some View`

Adds an action to perform when this view detects data emitted by the given
publisher.

Instance Method

# onChange(of:initial:_:)

Adds a modifier for this view that fires an action when a specific value
changes.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func onChange<V>(
        of value: V,
        initial: Bool = false,
        _ action: @escaping (V, V) -> Void
    ) -> some View where V : Equatable
    

##  Parameters

`value`

    

The value to check against when determining whether to run the closure.

`initial`

    

Whether the action should be run when this view initially appears.

`action`

    

A closure to run when the value changes.

`oldValue`

    

The old value that failed the comparison check (or the initial value when
requested).

`newValue`

    

The new value that failed the comparison check.

## Return Value

A view that fires an action when the specified value changes.

## Discussion

You can use `onChange` to trigger a side effect as the result of a value
changing, such as an `Environment` key or a `Binding`.

The system may call the action closure on the main actor, so avoid long-
running tasks in the closure. If you need to perform such tasks, detach an
asynchronous background task.

When the value changes, the new version of the closure will be called, so any
captured values will have their values from the time that the observed value
has its new value. The old and new observed values are passed into the
closure. In the following code example, `PlayerView` passes both the old and
new values to the model.

## See Also

### Responding to data changes

`func onChange<V>(of: V, initial: Bool, () -> Void) -> some View`

Adds a modifier for this view that fires an action when a specific value
changes.

`func onReceive<P>(P, perform: (P.Output) -> Void) -> some View`

Adds an action to perform when this view detects data emitted by the given
publisher.

Instance Method

# onReceive(_:perform:)

Adds an action to perform when this view detects data emitted by the given
publisher.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func onReceive<P>(
        _ publisher: P,
        perform action: @escaping (P.Output) -> Void
    ) -> some View where P : Publisher, P.Failure == Never
    

##  Parameters

`publisher`

    

The publisher to subscribe to.

`action`

    

The action to perform when an event is emitted by `publisher`. The event
emitted by publisher is passed as a parameter to `action`.

## Return Value

A view that triggers `action` when `publisher` emits an event.

## See Also

### Responding to data changes

`func onChange<V>(of: V, initial: Bool, () -> Void) -> some View`

Adds a modifier for this view that fires an action when a specific value
changes.

`func onChange<V>(of: V, initial: Bool, (V, V) -> Void) -> some View`

Adds a modifier for this view that fires an action when a specific value
changes.

Instance Method

# environmentObject(_:)

Supplies an observable object to a view’s hierarchy.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func environmentObject<T>(_ object: T) -> some View where T : ObservableObject
    

##  Parameters

`object`

    

The object to store and make available to the view’s hierarchy.

## Discussion

Use this modifier to add an observable object to a view’s environment. The
object must conform to the `ObservableObject` protocol.

Adding an object to a view’s environment makes the object available to
subviews in the view’s hierarchy. To retrieve the object in a subview, use the
`EnvironmentObject` property wrapper.

Note

If the observable object conforms to the `Observable` protocol, use either
`environment(_:)` or the `environment(_:_:)` modifier to add the object to the
view’s environment.

## See Also

### Distributing model data throughout your app

`func environmentObject<T>(T) -> some Scene`

Supplies an `ObservableObject` to a view subhierarchy.

`struct EnvironmentObject`

A property wrapper type for an observable object that a parent or ancestor
view supplies.

Instance Method

# environmentObject(_:)

Supplies an `ObservableObject` to a view subhierarchy.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func environmentObject<T>(_ object: T) -> some Scene where T : ObservableObject
    

##  Parameters

`object`

    

the object to store and make available to the scene’s subhierarchy.

## Discussion

The object can be read by any child by using `EnvironmentObject`:

You then read the object inside `ContentView` or one of its descendants using
the `EnvironmentObject` property wrapper:

## See Also

### Distributing model data throughout your app

`func environmentObject<T>(T) -> some View`

Supplies an observable object to a view’s hierarchy.

`struct EnvironmentObject`

A property wrapper type for an observable object that a parent or ancestor
view supplies.

Structure

# EnvironmentObject

A property wrapper type for an observable object that a parent or ancestor
view supplies.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen @propertyWrapper
    struct EnvironmentObject<ObjectType> where ObjectType : ObservableObject

## Overview

An environment object invalidates the current view whenever the observable
object that conforms to `ObservableObject` changes. If you declare a property
as an environment object, be sure to set a corresponding model object on an
ancestor view by calling its `environmentObject(_:)` modifier.

Note

If your observable object conforms to the `Observable` protocol, use
`Environment` instead of `EnvironmentObject` and set the model object in an
ancestor view by calling its `environment(_:)` or `environment(_:_:)`
modifiers.

## Topics

### Creating an environment object

`init()`

Creates an environment object.

### Getting the value

`var wrappedValue: ObjectType`

The underlying value referenced by the environment object.

`var projectedValue: EnvironmentObject<ObjectType>.Wrapper`

A projection of the environment object that creates bindings to its properties
using dynamic member lookup.

`struct Wrapper`

A wrapper of the underlying environment object that can create bindings to its
properties using dynamic member lookup.

## Relationships

### Conforms To

  * `DynamicProperty`

## See Also

### Distributing model data throughout your app

`func environmentObject<T>(T) -> some View`

Supplies an observable object to a view’s hierarchy.

`func environmentObject<T>(T) -> some Scene`

Supplies an `ObservableObject` to a view subhierarchy.

Protocol

# DynamicProperty

An interface for a stored variable that updates an external property of a
view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    protocol DynamicProperty

## Overview

The view gives values to these properties prior to recomputing the view’s
`body`.

## Topics

### Updating the value

`func update()`

Updates the underlying value of the stored value.

**Required** Default implementation provided.

## Relationships

### Conforming Types

  * `AccessibilityFocusState`
  * `AppStorage`
  * `Binding`
  * `Environment`
  * `EnvironmentObject`
  * `FetchRequest`

Conforms when `Result` conforms to `NSFetchRequestResult`.

  * `FocusState`
  * `FocusedBinding`
  * `FocusedObject`
  * `FocusedValue`
  * `GestureState`
  * `NSApplicationDelegateAdaptor`
  * `Namespace`
  * `ObservedObject`
  * `PhysicalMetric`
  * `ScaledMetric`
  * `SceneStorage`
  * `SectionedFetchRequest`

Conforms when `SectionIdentifier` conforms to `Hashable` and `Result` conforms
to `NSFetchRequestResult`.

  * `State`
  * `StateObject`
  * `UIApplicationDelegateAdaptor`
  * `WKApplicationDelegateAdaptor`
  * `WKExtensionDelegateAdaptor`



# MenuBarExtraStyle

Type Property

# automatic

The default menu bar extra style.

macOS 13.0+

    
    
    static var automatic: AutomaticMenuBarExtraStyle { get }

Available when `Self` is `AutomaticMenuBarExtraStyle`.

## See Also

### Getting menu bar extra styles

`static var menu: PullDownMenuBarExtraStyle`

A menu bar extra style that renders its contents as a menu that pulls down
from the icon in the menu bar.

Available when `Self` is `PullDownMenuBarExtraStyle`.

`static var window: WindowMenuBarExtraStyle`

A menu bar extra style that renders its contents in a popover-like window.

Available when `Self` is `WindowMenuBarExtraStyle`.

Type Property

# menu

A menu bar extra style that renders its contents as a menu that pulls down
from the icon in the menu bar.

macOS 13.0+

    
    
    static var menu: PullDownMenuBarExtraStyle { get }

Available when `Self` is `PullDownMenuBarExtraStyle`.

## See Also

### Getting menu bar extra styles

`static var automatic: AutomaticMenuBarExtraStyle`

The default menu bar extra style.

Available when `Self` is `AutomaticMenuBarExtraStyle`.

`static var window: WindowMenuBarExtraStyle`

A menu bar extra style that renders its contents in a popover-like window.

Available when `Self` is `WindowMenuBarExtraStyle`.

Type Property

# window

A menu bar extra style that renders its contents in a popover-like window.

macOS 13.0+

    
    
    static var window: WindowMenuBarExtraStyle { get }

Available when `Self` is `WindowMenuBarExtraStyle`.

## Discussion

The styling and layout of controls is similar to that when contained in a
normal window, compared to the menu-like layout that the `menu` style
provides.

## See Also

### Getting menu bar extra styles

`static var automatic: AutomaticMenuBarExtraStyle`

The default menu bar extra style.

Available when `Self` is `AutomaticMenuBarExtraStyle`.

`static var menu: PullDownMenuBarExtraStyle`

A menu bar extra style that renders its contents as a menu that pulls down
from the icon in the menu bar.

Available when `Self` is `PullDownMenuBarExtraStyle`.

Structure

# AutomaticMenuBarExtraStyle

The default menu bar extra style. You can also use `automatic` to construct
this style.

macOS 13.0+

    
    
    struct AutomaticMenuBarExtraStyle

## Topics

### Creating the menu bar extra style

`init()`

Creates an automatic menu bar extra style.

## Relationships

### Conforms To

  * `MenuBarExtraStyle`

## See Also

### Supporting types

`struct PullDownMenuBarExtraStyle`

A menu bar extra style that renders its contents as a menu that pulls down
from the icon in the menu bar.

`struct WindowMenuBarExtraStyle`

A menu bar extra style that renders its contents in a popover-like window.

Structure

# PullDownMenuBarExtraStyle

A menu bar extra style that renders its contents as a menu that pulls down
from the icon in the menu bar.

macOS 13.0+

    
    
    struct PullDownMenuBarExtraStyle

## Overview

Use `menu` to construct this style.

## Topics

### Creating the menu bar extra style

`init()`

Creates a pull down menu bar extra style.

## Relationships

### Conforms To

  * `MenuBarExtraStyle`

## See Also

### Supporting types

`struct AutomaticMenuBarExtraStyle`

The default menu bar extra style. You can also use `automatic` to construct
this style.

`struct WindowMenuBarExtraStyle`

A menu bar extra style that renders its contents in a popover-like window.

Structure

# WindowMenuBarExtraStyle

A menu bar extra style that renders its contents in a popover-like window.

macOS 13.0+

    
    
    struct WindowMenuBarExtraStyle

## Overview

Use `window` to construct this style.

## Topics

### Creating the menu bar extra style

`init()`

Creates a window menu bar extra style.

## Relationships

### Conforms To

  * `MenuBarExtraStyle`

## See Also

### Supporting types

`struct AutomaticMenuBarExtraStyle`

The default menu bar extra style. You can also use `automatic` to construct
this style.

`struct PullDownMenuBarExtraStyle`

A menu bar extra style that renders its contents as a menu that pulls down
from the icon in the menu bar.



# MagnificationGesture

Initializer

# init(minimumScaleDelta:)

Creates a magnification gesture with a given minimum delta for the gesture to
start.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  visionOS 1.0+

    
    
    init(minimumScaleDelta: CGFloat = 0.01)

Deprecated

Use `MagnifyGesture` instead.

## See Also

### Creating the gesture

`var minimumScaleDelta: CGFloat`

The minimum required delta before the gesture starts.

Deprecated

Instance Property

# minimumScaleDelta

The minimum required delta before the gesture starts.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  visionOS 1.0+

    
    
    var minimumScaleDelta: CGFloat

Deprecated

Use `MagnifyGesture` instead.

## See Also

### Creating the gesture

`init(minimumScaleDelta: CGFloat)`

Creates a magnification gesture with a given minimum delta for the gesture to
start.

Deprecated



# MenuOrder

Type Property

# automatic

The ordering of the menu chosen by the system for the current context.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static let automatic: MenuOrder

## Discussion

On iOS, this order resolves to `fixed` for menus presented within scrollable
content. Pickers that use the `menu` style also default to `fixed` order. In
all other cases, menus default to `priority` order.

On macOS, tvOS and watchOS, the `automatic` order always resolves to `fixed`
order.

## See Also

### Getting menu orders

`static let fixed: MenuOrder`

Order items from top to bottom.

`static let priority: MenuOrder`

Keep the first items closest to user’s interaction point.

Type Property

# fixed

Order items from top to bottom.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static let fixed: MenuOrder

## See Also

### Getting menu orders

`static let automatic: MenuOrder`

The ordering of the menu chosen by the system for the current context.

`static let priority: MenuOrder`

Keep the first items closest to user’s interaction point.

Type Property

# priority

Keep the first items closest to user’s interaction point.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    static let priority: MenuOrder

## See Also

### Getting menu orders

`static let automatic: MenuOrder`

The ordering of the menu chosen by the system for the current context.

`static let fixed: MenuOrder`

Order items from top to bottom.



# MoveCommandDirection

Case

# MoveCommandDirection.up

macOS 10.15+  tvOS 13.0+

    
    
    case up

## See Also

### Getting move command directions

`case down`

`case left`

`case right`

Case

# MoveCommandDirection.down

macOS 10.15+  tvOS 13.0+

    
    
    case down

## See Also

### Getting move command directions

`case up`

`case left`

`case right`

Case

# MoveCommandDirection.left

macOS 10.15+  tvOS 13.0+

    
    
    case left

## See Also

### Getting move command directions

`case up`

`case down`

`case right`

Case

# MoveCommandDirection.right

macOS 10.15+  tvOS 13.0+

    
    
    case right

## See Also

### Getting move command directions

`case up`

`case down`

`case left`



# MixedImmersionStyle

Initializer

# init()

visionOS 1.0+

    
    
    init()



