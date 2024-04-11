# CommandMenu

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



# ContentMode

Case

# ContentMode.fill

An option that resizes the content so it occupies all available space, both
vertically and horizontally.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case fill

## Discussion

This mode preserves the content’s aspect ratio. If the content doesn’t have
the same aspect ratio as the available space, the content becomes the same
size as the available space on one axis, and larger on the other axis.

## See Also

### Getting content modes

`case fit`

An option that resizes the content so it’s all within the available space,
both vertically and horizontally.

Case

# ContentMode.fit

An option that resizes the content so it’s all within the available space,
both vertically and horizontally.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case fit

## Discussion

This mode preserves the content’s aspect ratio. If the content doesn’t have
the same aspect ratio as the available space, the content becomes the same
size as the available space on one axis and leaves empty space on the other.

## See Also

### Getting content modes

`case fill`

An option that resizes the content so it occupies all available space, both
vertically and horizontally.



# ColorRenderingMode

Case

# ColorRenderingMode.extendedLinear

The extended linear sRGB working color space.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case extendedLinear

## Discussion

Color component values outside the range `[0, 1]` are preserved. This color
space isn’t gamma corrected.

## See Also

### Getting rendering modes

`case linear`

The linear sRGB working color space.

`case nonLinear`

The non-linear sRGB working color space.

Case

# ColorRenderingMode.linear

The linear sRGB working color space.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case linear

## Discussion

Color component values outside the range `[0, 1]` produce undefined results.
This color space isn’t gamma corrected.

## See Also

### Getting rendering modes

`case extendedLinear`

The extended linear sRGB working color space.

`case nonLinear`

The non-linear sRGB working color space.

Case

# ColorRenderingMode.nonLinear

The non-linear sRGB working color space.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case nonLinear

## Discussion

Color component values outside the range `[0, 1]` produce undefined results.
This color space is gamma corrected.

## See Also

### Getting rendering modes

`case extendedLinear`

The extended linear sRGB working color space.

`case linear`

The linear sRGB working color space.



# ControlGroupStyleConfiguration

Instance Property

# label

A view that provides the optional label of the `ControlGroup`.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 17.0+  visionOS
1.0+

    
    
    let label: ControlGroupStyleConfiguration.Label

## See Also

### Configuring the label

`struct Label`

A type-erased label of a `ControlGroup`.

Structure

# ControlGroupStyleConfiguration.Label

A type-erased label of a `ControlGroup`.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 17.0+  visionOS
1.0+

    
    
    struct Label

## Relationships

### Conforms To

  * `View`

## See Also

### Configuring the label

`let label: ControlGroupStyleConfiguration.Label`

A view that provides the optional label of the `ControlGroup`.

Instance Property

# content

A view that represents the content of the `ControlGroup`.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 17.0+  visionOS
1.0+

    
    
    let content: ControlGroupStyleConfiguration.Content

## See Also

### Configuring the content

`struct Content`

A type-erased content of a `ControlGroup`.

Structure

# ControlGroupStyleConfiguration.Content

A type-erased content of a `ControlGroup`.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 17.0+  visionOS
1.0+

    
    
    struct Content

## Relationships

### Conforms To

  * `View`

## See Also

### Configuring the content

`let content: ControlGroupStyleConfiguration.Content`

A view that represents the content of the `ControlGroup`.



# ControlGroupStyle

Type Property

# automatic

The default control group style.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 17.0+  visionOS
1.0+

    
    
    static var automatic: AutomaticControlGroupStyle { get }

Available when `Self` is `AutomaticControlGroupStyle`.

## Discussion

The default control group style can vary by platform. By default, both
platforms use a momentary segmented control style that’s appropriate for the
environment in which it is rendered.

You can override a control group’s style. To apply the default style to a
control group or to a view that contains a control group, use the
`controlGroupStyle(_:)` modifier.

## See Also

### Getting built-in control group styles

`static var compactMenu: CompactMenuControlGroupStyle`

A control group style that presents its content as a compact menu when the
user presses the control, or as a submenu when nested within a larger menu.

Available when `Self` is `CompactMenuControlGroupStyle`.

`static var menu: MenuControlGroupStyle`

A control group style that presents its content as a menu when the user
presses the control, or as a submenu when nested within a larger menu.

Available when `Self` is `MenuControlGroupStyle`.

`static var navigation: NavigationControlGroupStyle`

The navigation control group style.

Available when `Self` is `NavigationControlGroupStyle`.

`static var palette: PaletteControlGroupStyle`

A control group style that presents its content as a palette.

Available when `Self` is `PaletteControlGroupStyle`.

Type Property

# compactMenu

A control group style that presents its content as a compact menu when the
user presses the control, or as a submenu when nested within a larger menu.

iOS 16.4+  iPadOS 16.4+  macOS 13.3+  Mac Catalyst 16.4+  visionOS 1.0+

    
    
    static var compactMenu: CompactMenuControlGroupStyle { get }

Available when `Self` is `CompactMenuControlGroupStyle`.

## Discussion

To apply this style to a control group, or to a view that contains control
groups, use the `controlGroupStyle(_:)` modifier.

## See Also

### Getting built-in control group styles

`static var automatic: AutomaticControlGroupStyle`

The default control group style.

Available when `Self` is `AutomaticControlGroupStyle`.

`static var menu: MenuControlGroupStyle`

A control group style that presents its content as a menu when the user
presses the control, or as a submenu when nested within a larger menu.

Available when `Self` is `MenuControlGroupStyle`.

`static var navigation: NavigationControlGroupStyle`

The navigation control group style.

Available when `Self` is `NavigationControlGroupStyle`.

`static var palette: PaletteControlGroupStyle`

A control group style that presents its content as a palette.

Available when `Self` is `PaletteControlGroupStyle`.

Type Property

# menu

A control group style that presents its content as a menu when the user
presses the control, or as a submenu when nested within a larger menu.

iOS 16.4+  iPadOS 16.4+  macOS 13.3+  Mac Catalyst 16.4+  tvOS 17.0+  visionOS
1.0+

    
    
    static var menu: MenuControlGroupStyle { get }

Available when `Self` is `MenuControlGroupStyle`.

## Discussion

To apply this style to a control group, or to a view that contains control
groups, use the `controlGroupStyle(_:)` modifier.

## See Also

### Getting built-in control group styles

`static var automatic: AutomaticControlGroupStyle`

The default control group style.

Available when `Self` is `AutomaticControlGroupStyle`.

`static var compactMenu: CompactMenuControlGroupStyle`

A control group style that presents its content as a compact menu when the
user presses the control, or as a submenu when nested within a larger menu.

Available when `Self` is `CompactMenuControlGroupStyle`.

`static var navigation: NavigationControlGroupStyle`

The navigation control group style.

Available when `Self` is `NavigationControlGroupStyle`.

`static var palette: PaletteControlGroupStyle`

A control group style that presents its content as a palette.

Available when `Self` is `PaletteControlGroupStyle`.

Type Property

# navigation

The navigation control group style.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    static var navigation: NavigationControlGroupStyle { get }

Available when `Self` is `NavigationControlGroupStyle`.

## Discussion

Use this style to group controls related to navigation, such as back/forward
buttons or timeline navigation controls.

The navigation control group style can vary by platform. On iOS, it renders as
individual borderless buttons, while on macOS, it displays as a separated
momentary segmented control.

To apply this style to a control group or to a view that contains a control
group, use the `controlGroupStyle(_:)` modifier.

## See Also

### Getting built-in control group styles

`static var automatic: AutomaticControlGroupStyle`

The default control group style.

Available when `Self` is `AutomaticControlGroupStyle`.

`static var compactMenu: CompactMenuControlGroupStyle`

A control group style that presents its content as a compact menu when the
user presses the control, or as a submenu when nested within a larger menu.

Available when `Self` is `CompactMenuControlGroupStyle`.

`static var menu: MenuControlGroupStyle`

A control group style that presents its content as a menu when the user
presses the control, or as a submenu when nested within a larger menu.

Available when `Self` is `MenuControlGroupStyle`.

`static var palette: PaletteControlGroupStyle`

A control group style that presents its content as a palette.

Available when `Self` is `PaletteControlGroupStyle`.

Type Property

# palette

A control group style that presents its content as a palette.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    static var palette: PaletteControlGroupStyle { get }

Available when `Self` is `PaletteControlGroupStyle`.

## Discussion

Note

When used outside of menus, this style is rendered as a segmented control.

Use this style to render a multi-select or a stateless palette. The following
example creates a control group that contains both type of shelves:

To apply this style to a control group, or to a view that contains control
groups, use the `controlGroupStyle(_:)` modifier.

## See Also

### Getting built-in control group styles

`static var automatic: AutomaticControlGroupStyle`

The default control group style.

Available when `Self` is `AutomaticControlGroupStyle`.

`static var compactMenu: CompactMenuControlGroupStyle`

A control group style that presents its content as a compact menu when the
user presses the control, or as a submenu when nested within a larger menu.

Available when `Self` is `CompactMenuControlGroupStyle`.

`static var menu: MenuControlGroupStyle`

A control group style that presents its content as a menu when the user
presses the control, or as a submenu when nested within a larger menu.

Available when `Self` is `MenuControlGroupStyle`.

`static var navigation: NavigationControlGroupStyle`

The navigation control group style.

Available when `Self` is `NavigationControlGroupStyle`.

Instance Method

# makeBody(configuration:)

Creates a view representing the body of a control group.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 17.0+  visionOS
1.0+

    
    
    @ViewBuilder @MainActor
    func makeBody(configuration: Self.Configuration) -> Self.Body

**Required**

##  Parameters

`configuration`

    

The properties of the control group instance being created.

## Discussion

This method will be called for each instance of `ControlGroup` created within
a view hierarchy where this style is the current `ControlGroupStyle`.

## See Also

### Creating custom control group styles

`typealias Configuration`

The properties of a `ControlGroup` instance being created.

`associatedtype Body : View`

A view representing the body of a control group.

**Required**

Type Alias

# ControlGroupStyle.Configuration

The properties of a `ControlGroup` instance being created.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 17.0+  visionOS
1.0+

    
    
    typealias Configuration = ControlGroupStyleConfiguration

## See Also

### Creating custom control group styles

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Creates a view representing the body of a control group.

**Required**

` associatedtype Body : View`

A view representing the body of a control group.

**Required**

Associated Type

# Body

A view representing the body of a control group.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 17.0+  visionOS
1.0+

    
    
    associatedtype Body : View

**Required**

## See Also

### Creating custom control group styles

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Creates a view representing the body of a control group.

**Required**

` typealias Configuration`

The properties of a `ControlGroup` instance being created.

Structure

# AutomaticControlGroupStyle

The default control group style.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 17.0+  visionOS
1.0+

    
    
    struct AutomaticControlGroupStyle

## Overview

You can also use `automatic` to construct this style.

## Relationships

### Conforms To

  * `ControlGroupStyle`

## See Also

### Supporting types

`struct CompactMenuControlGroupStyle`

A control group style that presents its content as a compact menu when the
user presses the control, or as a submenu when nested within a larger menu.

`struct MenuControlGroupStyle`

A control group style that presents its content as a menu when the user
presses the control, or as a submenu when nested within a larger menu.

`struct NavigationControlGroupStyle`

The navigation control group style.

`struct PaletteControlGroupStyle`

A control group style that presents its content as a palette.

Structure

# CompactMenuControlGroupStyle

A control group style that presents its content as a compact menu when the
user presses the control, or as a submenu when nested within a larger menu.

iOS 16.4+  iPadOS 16.4+  macOS 13.3+  Mac Catalyst 16.4+  visionOS 1.0+

    
    
    struct CompactMenuControlGroupStyle

## Overview

Use `compactMenu` to construct this style.

## Topics

### Creating the control group style

`init()`

Creates a compact menu control group style.

## Relationships

### Conforms To

  * `ControlGroupStyle`

## See Also

### Supporting types

`struct AutomaticControlGroupStyle`

The default control group style.

`struct MenuControlGroupStyle`

A control group style that presents its content as a menu when the user
presses the control, or as a submenu when nested within a larger menu.

`struct NavigationControlGroupStyle`

The navigation control group style.

`struct PaletteControlGroupStyle`

A control group style that presents its content as a palette.

Structure

# MenuControlGroupStyle

A control group style that presents its content as a menu when the user
presses the control, or as a submenu when nested within a larger menu.

iOS 16.4+  iPadOS 16.4+  macOS 13.3+  Mac Catalyst 16.4+  tvOS 17.0+  visionOS
1.0+

    
    
    struct MenuControlGroupStyle

## Overview

Use `menu` to construct this style.

## Topics

### Creating the control group style

`init()`

Creates a menu control group style.

## Relationships

### Conforms To

  * `ControlGroupStyle`

## See Also

### Supporting types

`struct AutomaticControlGroupStyle`

The default control group style.

`struct CompactMenuControlGroupStyle`

A control group style that presents its content as a compact menu when the
user presses the control, or as a submenu when nested within a larger menu.

`struct NavigationControlGroupStyle`

The navigation control group style.

`struct PaletteControlGroupStyle`

A control group style that presents its content as a palette.

Structure

# NavigationControlGroupStyle

The navigation control group style.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    struct NavigationControlGroupStyle

## Overview

You can also use `navigation` to construct this style.

## Topics

### Creating the control group style

`init()`

Creates a navigation control group style.

## Relationships

### Conforms To

  * `ControlGroupStyle`

## See Also

### Supporting types

`struct AutomaticControlGroupStyle`

The default control group style.

`struct CompactMenuControlGroupStyle`

A control group style that presents its content as a compact menu when the
user presses the control, or as a submenu when nested within a larger menu.

`struct MenuControlGroupStyle`

A control group style that presents its content as a menu when the user
presses the control, or as a submenu when nested within a larger menu.

`struct PaletteControlGroupStyle`

A control group style that presents its content as a palette.

Structure

# PaletteControlGroupStyle

A control group style that presents its content as a palette.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    struct PaletteControlGroupStyle

## Overview

Use `palette` to construct this style.

## Topics

### Creating the control group style

`init()`

Creates a palette control group style.

## Relationships

### Conforms To

  * `ControlGroupStyle`

## See Also

### Supporting types

`struct AutomaticControlGroupStyle`

The default control group style.

`struct CompactMenuControlGroupStyle`

A control group style that presents its content as a compact menu when the
user presses the control, or as a submenu when nested within a larger menu.

`struct MenuControlGroupStyle`

A control group style that presents its content as a menu when the user
presses the control, or as a submenu when nested within a larger menu.

`struct NavigationControlGroupStyle`

The navigation control group style.



# ColumnsFormStyle

Initializer

# init()

A non-scrolling form style with a trailing aligned column of labels next to a
leading aligned column of values.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init()

## Discussion

Don’t call this initializer directly. Instead, use the `columns` static
variable to create this style:



# CommandGroupPlacement

Type Property

# appInfo

Placement for commands that provide information about the app, the terms of
the user’s license agreement, and so on.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static let appInfo: CommandGroupPlacement

## Discussion

By default, this group includes the following command in macOS:

  * About App

## See Also

### App interactions

`static let appSettings: CommandGroupPlacement`

Placement for commands that expose app settings and preferences.

`static let appTermination: CommandGroupPlacement`

Placement for commands that result in app termination.

`static let appVisibility: CommandGroupPlacement`

Placement for commands that control the visibility of running apps.

`static let systemServices: CommandGroupPlacement`

Placement for commands that expose services other apps provide.

Type Property

# appSettings

Placement for commands that expose app settings and preferences.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static let appSettings: CommandGroupPlacement

## Discussion

By default, this group includes the following command in macOS:

  * Preferences

## See Also

### App interactions

`static let appInfo: CommandGroupPlacement`

Placement for commands that provide information about the app, the terms of
the user’s license agreement, and so on.

`static let appTermination: CommandGroupPlacement`

Placement for commands that result in app termination.

`static let appVisibility: CommandGroupPlacement`

Placement for commands that control the visibility of running apps.

`static let systemServices: CommandGroupPlacement`

Placement for commands that expose services other apps provide.

Type Property

# appTermination

Placement for commands that result in app termination.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static let appTermination: CommandGroupPlacement

## Discussion

By default, this group includes the following command in macOS:

  * Quit App

## See Also

### App interactions

`static let appInfo: CommandGroupPlacement`

Placement for commands that provide information about the app, the terms of
the user’s license agreement, and so on.

`static let appSettings: CommandGroupPlacement`

Placement for commands that expose app settings and preferences.

`static let appVisibility: CommandGroupPlacement`

Placement for commands that control the visibility of running apps.

`static let systemServices: CommandGroupPlacement`

Placement for commands that expose services other apps provide.

Type Property

# appVisibility

Placement for commands that control the visibility of running apps.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static let appVisibility: CommandGroupPlacement

## Discussion

By default, this group includes the following commands in macOS:

  * Hide App

  * Hide Others

  * Show All

## See Also

### App interactions

`static let appInfo: CommandGroupPlacement`

Placement for commands that provide information about the app, the terms of
the user’s license agreement, and so on.

`static let appSettings: CommandGroupPlacement`

Placement for commands that expose app settings and preferences.

`static let appTermination: CommandGroupPlacement`

Placement for commands that result in app termination.

`static let systemServices: CommandGroupPlacement`

Placement for commands that expose services other apps provide.

Type Property

# systemServices

Placement for commands that expose services other apps provide.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static let systemServices: CommandGroupPlacement

## Discussion

By default, this group includes the following command in macOS:

  * Services submenu (managed automatically)

## See Also

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

Type Property

# importExport

Placement for commands that relate to importing and exporting data using
formats that the app doesn’t natively support.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static let importExport: CommandGroupPlacement

## Discussion

Empty by default in macOS.

## See Also

### File manipulation

`static let newItem: CommandGroupPlacement`

Placement for commands that create and open different kinds of documents.

`static let printItem: CommandGroupPlacement`

Placement for commands related to printing app content.

`static let saveItem: CommandGroupPlacement`

Placement for commands that save open documents and close windows.

Type Property

# newItem

Placement for commands that create and open different kinds of documents.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static let newItem: CommandGroupPlacement

## Discussion

By default, this group includes the following commands in macOS:

  * New

  * Open

  * Open Recent submenu (managed automatically)

## See Also

### File manipulation

`static let importExport: CommandGroupPlacement`

Placement for commands that relate to importing and exporting data using
formats that the app doesn’t natively support.

`static let printItem: CommandGroupPlacement`

Placement for commands related to printing app content.

`static let saveItem: CommandGroupPlacement`

Placement for commands that save open documents and close windows.

Type Property

# printItem

Placement for commands related to printing app content.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static let printItem: CommandGroupPlacement

## Discussion

By default, this group includes the following commands in macOS:

  * Page Setup

  * Print

## See Also

### File manipulation

`static let importExport: CommandGroupPlacement`

Placement for commands that relate to importing and exporting data using
formats that the app doesn’t natively support.

`static let newItem: CommandGroupPlacement`

Placement for commands that create and open different kinds of documents.

`static let saveItem: CommandGroupPlacement`

Placement for commands that save open documents and close windows.

Type Property

# saveItem

Placement for commands that save open documents and close windows.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static let saveItem: CommandGroupPlacement

## Discussion

By default, this group includes the following commands in macOS:

  * Close

  * Save

  * Save As/Duplicate

  * Revert to Saved

## See Also

### File manipulation

`static let importExport: CommandGroupPlacement`

Placement for commands that relate to importing and exporting data using
formats that the app doesn’t natively support.

`static let newItem: CommandGroupPlacement`

Placement for commands that create and open different kinds of documents.

`static let printItem: CommandGroupPlacement`

Placement for commands related to printing app content.

Type Property

# pasteboard

Placement for commands that interact with the Clipboard and manipulate content
that is currently selected in the app’s view hierarchy.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static let pasteboard: CommandGroupPlacement

## Discussion

By default, this group includes the following commands in macOS:

  * Cut

  * Copy

  * Paste

  * Paste and Match Style

  * Delete

  * Select All

## See Also

### Content updates

`static let textEditing: CommandGroupPlacement`

Placement for commands that manipulate and transform text selections.

`static let textFormatting: CommandGroupPlacement`

Placement for commands that manipulate and transform the styles applied to
text selections.

`static let undoRedo: CommandGroupPlacement`

Placement for commands that control the Undo Manager.

Type Property

# textEditing

Placement for commands that manipulate and transform text selections.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static let textEditing: CommandGroupPlacement

## Discussion

By default, this group includes the following commands in macOS:

  * Find submenu

  * Spelling and Grammar submenu

  * Substitutions submenu

  * Transformations submenu

  * Speech submenu

## See Also

### Content updates

`static let pasteboard: CommandGroupPlacement`

Placement for commands that interact with the Clipboard and manipulate content
that is currently selected in the app’s view hierarchy.

`static let textFormatting: CommandGroupPlacement`

Placement for commands that manipulate and transform the styles applied to
text selections.

`static let undoRedo: CommandGroupPlacement`

Placement for commands that control the Undo Manager.

Type Property

# textFormatting

Placement for commands that manipulate and transform the styles applied to
text selections.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static let textFormatting: CommandGroupPlacement

## Discussion

By default, this group includes the following commands in macOS:

  * Font submenu

  * Text submenu

## See Also

### Content updates

`static let pasteboard: CommandGroupPlacement`

Placement for commands that interact with the Clipboard and manipulate content
that is currently selected in the app’s view hierarchy.

`static let textEditing: CommandGroupPlacement`

Placement for commands that manipulate and transform text selections.

`static let undoRedo: CommandGroupPlacement`

Placement for commands that control the Undo Manager.

Type Property

# undoRedo

Placement for commands that control the Undo Manager.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static let undoRedo: CommandGroupPlacement

## Discussion

By default, this group includes the following commands in macOS:

  * Undo

  * Redo

## See Also

### Content updates

`static let pasteboard: CommandGroupPlacement`

Placement for commands that interact with the Clipboard and manipulate content
that is currently selected in the app’s view hierarchy.

`static let textEditing: CommandGroupPlacement`

Placement for commands that manipulate and transform text selections.

`static let textFormatting: CommandGroupPlacement`

Placement for commands that manipulate and transform the styles applied to
text selections.

Type Property

# sidebar

Placement for commands that control the app’s sidebar and full-screen modes.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static let sidebar: CommandGroupPlacement

## Discussion

By default, this group includes the following commands in macOS:

  * Show/Hide Sidebar

  * Enter/Exit Full Screen

## See Also

### Bars

`static let toolbar: CommandGroupPlacement`

Placement for commands that manipulate the toolbar.

Type Property

# toolbar

Placement for commands that manipulate the toolbar.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static let toolbar: CommandGroupPlacement

## Discussion

By default, this group includes the following commands in macOS:

  * Show/Hide Toolbar

  * Customize Toolbar

## See Also

### Bars

`static let sidebar: CommandGroupPlacement`

Placement for commands that control the app’s sidebar and full-screen modes.

Type Property

# singleWindowList

Placement for commands that describe and reveal any windows that the app
defines.

macOS 13.0+

    
    
    static let singleWindowList: CommandGroupPlacement

## See Also

### Windows

`static let windowArrangement: CommandGroupPlacement`

Placement for commands that arrange all of an app’s windows.

`static let windowList: CommandGroupPlacement`

Placement for commands that describe and reveal the app’s open windows.

`static let windowSize: CommandGroupPlacement`

Placement for commands that control the size of the window.

Type Property

# windowArrangement

Placement for commands that arrange all of an app’s windows.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static let windowArrangement: CommandGroupPlacement

## Discussion

By default, this group includes the following command in macOS:

  * Bring All to Front

## See Also

### Windows

`static let singleWindowList: CommandGroupPlacement`

Placement for commands that describe and reveal any windows that the app
defines.

`static let windowList: CommandGroupPlacement`

Placement for commands that describe and reveal the app’s open windows.

`static let windowSize: CommandGroupPlacement`

Placement for commands that control the size of the window.

Type Property

# windowList

Placement for commands that describe and reveal the app’s open windows.

macOS 11.0+

    
    
    static let windowList: CommandGroupPlacement

## Discussion

SwiftUI manages this group automatically in macOS.

## See Also

### Windows

`static let singleWindowList: CommandGroupPlacement`

Placement for commands that describe and reveal any windows that the app
defines.

`static let windowArrangement: CommandGroupPlacement`

Placement for commands that arrange all of an app’s windows.

`static let windowSize: CommandGroupPlacement`

Placement for commands that control the size of the window.

Type Property

# windowSize

Placement for commands that control the size of the window.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static let windowSize: CommandGroupPlacement

## Discussion

By default, this group includes the following commands in macOS:

  * Minimize

  * Zoom

## See Also

### Windows

`static let singleWindowList: CommandGroupPlacement`

Placement for commands that describe and reveal any windows that the app
defines.

`static let windowArrangement: CommandGroupPlacement`

Placement for commands that arrange all of an app’s windows.

`static let windowList: CommandGroupPlacement`

Placement for commands that describe and reveal the app’s open windows.

Type Property

# help

Placement for commands that present documentation and helpful information to
people.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static let help: CommandGroupPlacement

## Discussion

By default, this group includes the following command in macOS:

  * App Help



# Custom layout

Protocol

# Layout

A type that defines the geometry of a collection of views.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    protocol Layout : Animatable

## Overview

You traditionally arrange views in your app’s user interface using built-in
layout containers like `HStack` and `Grid`. If you need more complex layout
behavior, you can define a custom layout container by creating a type that
conforms to the `Layout` protocol and implementing its required methods:

  * `sizeThatFits(proposal:subviews:cache:)` reports the size of the composite layout view.

  * `placeSubviews(in:proposal:subviews:cache:)` assigns positions to the container’s subviews.

You can define a basic layout type with only these two methods:

Use your layout the same way you use a built-in layout container, by providing
a `ViewBuilder` with the list of subviews to arrange:

### Support additional behaviors

You can optionally implement other protocol methods and properties to provide
more layout container features:

  * Define explicit horizontal and vertical layout guides for the container by implementing `explicitAlignment(of:in:proposal:subviews:cache:)` and `explicitAlignment(of:in:proposal:subviews:cache:)`, respectively.

  * Establish the preferred spacing around the container by implementing `spacing(subviews:cache:)`.

  * Indicate the axis of orientation for a container that has characteristics of a stack by implementing the `layoutProperties` static property.

  * Create and manage a cache to store computed values across different layout protocol calls by implementing `makeCache(subviews:)`.

The protocol provides default implementations for these symbols if you don’t
implement them. See each method or property for details.

### Add input parameters

You can define parameters as inputs to the layout, like you might for a
`View`:

Set the parameters at the point where you instantiate the layout:

If the layout provides default values for its parameters, you can omit the
parameters at the call site, but you might need to keep the parentheses after
the name of the layout, depending on how you specify the defaults. For
example, suppose you set a default alignment for the basic stack in the
parameter declaration:

To instantiate this layout using the default center alignment, you don’t have
to specify the alignment value, but you do need to add empty parentheses:

The Swift compiler requires the parentheses in this case because of how the
layout protocol implements this call site syntax. Specifically, the layout’s
`callAsFunction(_:)` method looks for an initializer with exactly zero input
arguments when you omit the parentheses from the call site. You can enable the
simpler call site for a layout that doesn’t have an implicit initializer of
this type by explicitly defining one:

For information about Swift initializers, see Initialization in _The Swift
Programming Language_.

### Interact with subviews through their proxies

To perform layout, you need information about all of its subviews, which are
the views that your container arranges. While your layout can’t interact
directly with its subviews, it can access a set of subview proxies through the
`Layout.Subviews` collection that each protocol method receives as an input
parameter. That type is an alias for the `LayoutSubviews` collection type,
which in turn contains `LayoutSubview` instances that are the subview proxies.

You can get information about each subview from its proxy, like its dimensions
and spacing preferences. This enables you to measure subviews before you
commit to placing them. You also assign a position to each subview by calling
its proxy’s `place(at:anchor:proposal:)` method. Call the method on each
subview from within your implementation of the layout’s
`placeSubviews(in:proposal:subviews:cache:)` method.

### Access layout values

Views have layout values that you set with view modifiers. Layout containers
can choose to condition their behavior accordingly. For example, a built-in
`HStack` allocates space to its subviews based in part on the priorities that
you set with the `layoutPriority(_:)` view modifier. Your layout container
accesses this value for a subview by reading the proxy’s `priority` property.

You can also create custom layout values by creating a layout key. Set a value
on a view with the `layoutValue(key:value:)` view modifier. Read the
corresponding value from the subview’s proxy using the key as an index on the
subview. For more information about creating, setting, and accessing custom
layout values, see `LayoutValueKey`.

## Topics

### Sizing the container and placing subviews

`func sizeThatFits(proposal: ProposedViewSize, subviews: Self.Subviews, cache:
inout Self.Cache) -> CGSize`

Returns the size of the composite view, given a proposed size and the view’s
subviews.

**Required**

` func placeSubviews(in: CGRect, proposal: ProposedViewSize, subviews:
Self.Subviews, cache: inout Self.Cache)`

Assigns positions to each of the layout’s subviews.

**Required**

` typealias Subviews`

A collection of proxies for the subviews of a layout view.

### Reporting layout container characteristics

`func explicitAlignment(of: HorizontalAlignment, in: CGRect, proposal:
ProposedViewSize, subviews: Self.Subviews, cache: inout Self.Cache) ->
CGFloat?`

Returns the position of the specified horizontal alignment guide along the x
axis.

**Required** Default implementations provided.

`func explicitAlignment(of: VerticalAlignment, in: CGRect, proposal:
ProposedViewSize, subviews: Self.Subviews, cache: inout Self.Cache) ->
CGFloat?`

Returns the position of the specified vertical alignment guide along the y
axis.

**Required** Default implementations provided.

`func spacing(subviews: Self.Subviews, cache: inout Self.Cache) ->
ViewSpacing`

Returns the preferred spacing values of the composite view.

**Required** Default implementation provided.

`static var layoutProperties: LayoutProperties`

Properties of a layout container.

**Required** Default implementation provided.

### Managing a cache

`func makeCache(subviews: Self.Subviews) -> Self.Cache`

Creates and initializes a cache for a layout instance.

**Required** Default implementation provided.

`func updateCache(inout Self.Cache, subviews: Self.Subviews)`

Updates the layout’s cache when something changes.

**Required** Default implementation provided.

`associatedtype Cache = Void`

Cached values associated with the layout instance.

**Required**

### Supporting types

`func callAsFunction<V>(() -> V) -> some View`

Combines the specified views into a single composite view using the layout
algorithms of the custom layout container.

## Relationships

### Inherits From

  * `Animatable`

### Conforming Types

  * `AnyLayout`
  * `GridLayout`
  * `HStackLayout`
  * `VStackLayout`
  * `ZStackLayout`

## See Also

### Creating a custom layout container

Composing custom layouts with SwiftUI

Arrange views in your app’s interface using layout tools that SwiftUI
provides.

`struct LayoutSubview`

A proxy that represents one subview of a layout.

`struct LayoutSubviews`

A collection of proxy values that represent the subviews of a layout view.

Structure

# LayoutSubview

A proxy that represents one subview of a layout.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    struct LayoutSubview

## Overview

This type acts as a proxy for a view that your custom layout container places
in the user interface. `Layout` protocol methods receive a `LayoutSubviews`
collection that contains exactly one proxy for each of the subviews arranged
by your container.

Use a proxy to get information about the associated subview, like its
dimensions, layout priority, or custom layout values. You also use the proxy
to tell its corresponding subview where to appear by calling the proxy’s
`place(at:anchor:proposal:)` method. Do this once for each subview from your
implementation of the layout’s `placeSubviews(in:proposal:subviews:cache:)`
method.

You can read custom layout values associated with a subview by using the
property’s key as an index on the subview. For more information about
defining, setting, and reading custom values, see `LayoutValueKey`.

## Topics

### Placing the subview

`func place(at: CGPoint, anchor: UnitPoint, proposal: ProposedViewSize)`

Assigns a position and proposed size to the subview.

### Getting subview characteristics

`func dimensions(in: ProposedViewSize) -> ViewDimensions`

Asks the subview for its dimensions and alignment guides.

`func sizeThatFits(ProposedViewSize) -> CGSize`

Asks the subview for its size.

`var spacing: ViewSpacing`

The subviews’s preferred spacing values.

`var priority: Double`

The layout priority of the subview.

### Getting custom values

`subscript<K>(K.Type) -> K.Value`

Gets the value for the subview that’s associated with the specified key.

## Relationships

### Conforms To

  * `Equatable`

## See Also

### Creating a custom layout container

Composing custom layouts with SwiftUI

Arrange views in your app’s interface using layout tools that SwiftUI
provides.

`protocol Layout`

A type that defines the geometry of a collection of views.

`struct LayoutSubviews`

A collection of proxy values that represent the subviews of a layout view.

Structure

# LayoutSubviews

A collection of proxy values that represent the subviews of a layout view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    struct LayoutSubviews

## Overview

You receive a `LayoutSubviews` input to your implementations of `Layout`
protocol methods, like `placeSubviews(in:proposal:subviews:cache:)` and
`sizeThatFits(proposal:subviews:cache:)`. The `subviews` parameter (which the
protocol aliases to the `Layout.Subviews` type) is a collection that contains
proxies for the layout’s subviews (of type `LayoutSubview`). The proxies
appear in the collection in the same order that they appear in the
`ViewBuilder` input to the layout container. Use the proxies to perform layout
operations.

Access the proxies in the collection as you would the contents of any Swift
random-access collection. For example, you can enumerate all of the subviews
and their indices to inspect or operate on them:

## Topics

### Getting the layout direction

`var layoutDirection: LayoutDirection`

The layout direction inherited by the container view.

### Accessing subviews

`subscript(Int) -> LayoutSubviews.Element`

Gets the subview proxy at a specified index.

`subscript<S>(S) -> LayoutSubviews`

Gets the subview proxies with the specified indicies.

`subscript(Range<Int>) -> LayoutSubviews`

Gets the subview proxies in the specified range.

`var startIndex: Int`

The index of the first subview.

`var endIndex: Int`

An index that’s one higher than the last subview.

`typealias Element`

A type that contains a proxy value.

`typealias Index`

A type that you can use to index proxy values.

`typealias SubSequence`

A type that contains a subsequence of proxy values.

## Relationships

### Conforms To

  * `BidirectionalCollection`
  * `Collection`
  * `Equatable`
  * `RandomAccessCollection`
  * `Sendable`
  * `Sequence`

## See Also

### Creating a custom layout container

Composing custom layouts with SwiftUI

Arrange views in your app’s interface using layout tools that SwiftUI
provides.

`protocol Layout`

A type that defines the geometry of a collection of views.

`struct LayoutSubview`

A proxy that represents one subview of a layout.

Structure

# LayoutProperties

Layout-specific properties of a layout container.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    struct LayoutProperties

## Overview

This structure contains configuration information that’s applicable to a
layout container. For example, the `stackOrientation` value indicates the
layout’s primary axis, if any.

You can use an instance of this type to characterize a custom layout
container, which is a type that conforms to the `Layout` protocol. Implement
the protocol’s `layoutProperties` property to return an instance. For example,
you can indicate that your layout has a vertical stack orientation:

If you don’t implement the property in your custom layout, the protocol
provides a default implementation that returns a `LayoutProperties` instance
with default values.

## Topics

### Creating a layout properties instance

`init()`

Creates a default set of properties.

### Getting layout properties

`var stackOrientation: Axis?`

The orientation of the containing stack-like container.

## Relationships

### Conforms To

  * `Sendable`

## See Also

### Configuring a custom layout

`struct ProposedViewSize`

A proposal for the size of a view.

`struct ViewSpacing`

A collection of the geometric spacing preferences of a view.

Structure

# ProposedViewSize

A proposal for the size of a view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    @frozen
    struct ProposedViewSize

## Overview

During layout in SwiftUI, views choose their own size, but they do that in
response to a size proposal from their parent view. When you create a custom
layout using the `Layout` protocol, your layout container participates in this
process using `ProposedViewSize` instances. The layout protocol’s methods take
a proposed size input that you can take into account when arranging views and
calculating the size of the composite container. Similarly, your layout
proposes a size to each of its own subviews when it measures and places them.

Layout containers typically measure their subviews by proposing several sizes
and looking at the responses. The container can use this information to decide
how to allocate space among its subviews. A layout might try the following
special proposals:

  * The `zero` proposal; the view responds with its minimum size.

  * The `infinity` proposal; the view responds with its maximum size.

  * The `unspecified` proposal; the view responds with its ideal size.

A layout might also try special cases for one dimension at a time. For
example, an `HStack` might measure the flexibility of its subviews’ widths,
while using a fixed value for the height.

## Topics

### Getting standard proposals

`static let zero: ProposedViewSize`

A size proposal that contains zero in both dimensions.

`static let infinity: ProposedViewSize`

A size proposal that contains infinity in both dimensions.

`static let unspecified: ProposedViewSize`

The proposed size with both dimensions left unspecified.

### Creating a custom size proposal

`init(CGSize)`

Creates a new proposed size from a specified size.

`init(width: CGFloat?, height: CGFloat?)`

Creates a new proposed size using the specified width and height.

### Getting the proposal’s dimensions

`var height: CGFloat?`

The proposed vertical size measured in points.

`var width: CGFloat?`

The proposed horizontal size measured in points.

### Modifying a proposal

`func replacingUnspecifiedDimensions(by: CGSize) -> CGSize`

Creates a new proposal that replaces unspecified dimensions in this proposal
with the corresponding dimension of the specified size.

## Relationships

### Conforms To

  * `Equatable`
  * `Sendable`

## See Also

### Configuring a custom layout

`struct LayoutProperties`

Layout-specific properties of a layout container.

`struct ViewSpacing`

A collection of the geometric spacing preferences of a view.

Structure

# ViewSpacing

A collection of the geometric spacing preferences of a view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    struct ViewSpacing

## Overview

This type represents how much space a view prefers to have between it and the
next view in a layout. The type stores independent values for each of the top,
bottom, leading, and trailing edges, and can also record different values for
different kinds of adjacent views. For example, it might contain one value for
the spacing to the next text view along the top and bottom edges, other values
for the spacing to text views on other edges, and yet other values for other
kinds of views. Spacing preferences can also vary by platform.

Your `Layout` type doesn’t have to take preferred spacing into account, but if
it does, you can use the `spacing` preferences of the subviews in your layout
container to:

  * Add space between subviews when you implement the `placeSubviews(in:proposal:subviews:cache:)` method.

  * Create a spacing preferences instance for the container view by implementing the `spacing(subviews:cache:)` method.

## Topics

### Creating spacing instances

`init()`

Initializes an instance with default spacing values.

`static let zero: ViewSpacing`

A view spacing instance that contains zero on all edges.

### Measuring spacing distance

`func distance(to: ViewSpacing, along: Axis) -> CGFloat`

Gets the preferred spacing distance along the specified axis to the view that
returns a specified spacing preference.

### Merging spacing instances

`func formUnion(ViewSpacing, edges: Edge.Set)`

Merges the spacing preferences of another spacing instance with this instance
for a specified set of edges.

`func union(ViewSpacing, edges: Edge.Set) -> ViewSpacing`

Gets a new value that merges the spacing preferences of another spacing
instance with this instance for a specified set of edges.

## Relationships

### Conforms To

  * `Sendable`

## See Also

### Configuring a custom layout

`struct LayoutProperties`

Layout-specific properties of a layout container.

`struct ProposedViewSize`

A proposal for the size of a view.

Instance Method

# layoutValue(key:value:)

Associates a value with a custom layout property.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func layoutValue<K>(
        key: K.Type,
        value: K.Value
    ) -> some View where K : LayoutValueKey
    

##  Parameters

`key`

    

The type of the key that you want to set a value for. Create the key as a type
that conforms to the `LayoutValueKey` protocol.

`value`

    

The value to assign to the key for this view. The value must be of the type
that you establish for the key’s associated value when you implement the key’s
`defaultValue` property.

## Return Value

A view that has the specified value for the specified key.

## Discussion

Use this method to set a value for a custom property that you define with
`LayoutValueKey`. For example, if you define a `Flexibility` key, you can set
the key on a `Text` view using the key’s type and a value:

For convenience, you might define a method that does this in an extension to
`View`:

This method makes the call site easier to read:

If you perform layout operations in a type that conforms to the `Layout`
protocol, you can read the key’s associated value for each subview of your
custom layout type. Do this by indexing the subview’s proxy with the key. For
more information, see `LayoutValueKey`.

## See Also

### Associating values with views in a custom layout

`protocol LayoutValueKey`

A key for accessing a layout value of a layout container’s subviews.

Protocol

# LayoutValueKey

A key for accessing a layout value of a layout container’s subviews.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    protocol LayoutValueKey

## Overview

If you create a custom layout by defining a type that conforms to the `Layout`
protocol, you can also create custom layout values that you set on individual
views, and that your container view can access to guide its layout behavior.
Your custom values resemble the built-in layout values that you set with view
modifiers like `layoutPriority(_:)` and `zIndex(_:)`, but have a purpose that
you define.

To create a custom layout value, define a type that conforms to the
`LayoutValueKey` protocol and implement the one required property that returns
the default value of the property. For example, you can create a property that
defines an amount of flexibility for a view, defined as an optional floating
point number with a default value of `nil`:

The Swift compiler infers this particular key’s associated type as an optional
`CGFloat` from this definition.

### Set a value on a view

Set the value on a view by adding the `layoutValue(key:value:)` view modifier
to the view. To make your custom value easier to work with, you can do this in
a convenience modifier in an extension of the `View` protocol:

Use your modifier to set the value on any views that need a nondefault value:

Any view that you don’t explicitly set a value for uses the default value, as
with the first `Text` view, above.

### Retrieve a value during layout

Access a custom layout value using the key as an index on subview’s proxy (an
instance of `LayoutSubview`) and use the value to make decisions about sizing,
placement, or other layout operations. For example, you might read the
flexibility value in your layout view’s `sizeThatFits(_:)` method, and adjust
your size calculations accordingly:

## Topics

### Providing a default value

`static var defaultValue: Self.Value`

The default value of the key.

**Required**

` associatedtype Value`

The type of the key’s value.

**Required**

## See Also

### Associating values with views in a custom layout

`func layoutValue<K>(key: K.Type, value: K.Value) -> some View`

Associates a value with a custom layout property.

Structure

# AnyLayout

A type-erased instance of the layout protocol.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    @frozen
    struct AnyLayout

## Overview

Use an `AnyLayout` instance to enable dynamically changing the type of a
layout container without destroying the state of the subviews. For example,
you can create a layout that changes between horizontal and vertical layouts
based on the current Dynamic Type setting:

The types that you use with `AnyLayout` must conform to the `Layout` protocol.
The above example chooses between the `HStackLayout` and `VStackLayout` types,
which are versions of the built-in `HStack` and `VStack` containers that
conform to the protocol. You can also use custom layout types that you define.

## Topics

### Creating the layout

`init<L>(L)`

Creates a type-erased value that wraps the specified layout.

## Relationships

### Conforms To

  * `Animatable`
  * `Layout`

## See Also

### Transitioning between layout types

`struct HStackLayout`

A horizontal container that you can use in conditional layouts.

`struct VStackLayout`

A vertical container that you can use in conditional layouts.

`struct ZStackLayout`

An overlaying container that you can use in conditional layouts.

`struct GridLayout`

A grid that you can use in conditional layouts.

Structure

# HStackLayout

A horizontal container that you can use in conditional layouts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    @frozen
    struct HStackLayout

## Overview

This layout container behaves like an `HStack`, but conforms to the `Layout`
protocol so you can use it in the conditional layouts that you construct with
`AnyLayout`. If you don’t need a conditional layout, use `HStack` instead.

## Topics

### Creating a horizontal stack

`init(alignment: VerticalAlignment, spacing: CGFloat?)`

Creates a horizontal stack with the specified spacing and vertical alignment.

### Getting the stack’s properties

`var alignment: VerticalAlignment`

The vertical alignment of subviews.

`var spacing: CGFloat?`

The distance between adjacent subviews.

## Relationships

### Conforms To

  * `Animatable`
  * `Layout`
  * `Sendable`

## See Also

### Transitioning between layout types

`struct AnyLayout`

A type-erased instance of the layout protocol.

`struct VStackLayout`

A vertical container that you can use in conditional layouts.

`struct ZStackLayout`

An overlaying container that you can use in conditional layouts.

`struct GridLayout`

A grid that you can use in conditional layouts.

Structure

# VStackLayout

A vertical container that you can use in conditional layouts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    @frozen
    struct VStackLayout

## Overview

This layout container behaves like a `VStack`, but conforms to the `Layout`
protocol so you can use it in the conditional layouts that you construct with
`AnyLayout`. If you don’t need a conditional layout, use `VStack` instead.

## Topics

### Creating a vertical stack

`init(alignment: HorizontalAlignment, spacing: CGFloat?)`

Creates a vertical stack with the specified spacing and horizontal alignment.

### Getting the stack’s properties

`var alignment: HorizontalAlignment`

The horizontal alignment of subviews.

`var spacing: CGFloat?`

The distance between adjacent subviews.

## Relationships

### Conforms To

  * `Animatable`
  * `Layout`
  * `Sendable`

## See Also

### Transitioning between layout types

`struct AnyLayout`

A type-erased instance of the layout protocol.

`struct HStackLayout`

A horizontal container that you can use in conditional layouts.

`struct ZStackLayout`

An overlaying container that you can use in conditional layouts.

`struct GridLayout`

A grid that you can use in conditional layouts.

Structure

# ZStackLayout

An overlaying container that you can use in conditional layouts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    @frozen
    struct ZStackLayout

## Overview

This layout container behaves like a `ZStack`, but conforms to the `Layout`
protocol so you can use it in the conditional layouts that you construct with
`AnyLayout`. If you don’t need a conditional layout, use `ZStack` instead.

## Topics

### Creating a stack

`init(alignment: Alignment)`

Creates a stack with the specified alignment.

### Getting the stack’s properties

`var alignment: Alignment`

The alignment of subviews.

## Relationships

### Conforms To

  * `Animatable`
  * `Layout`
  * `Sendable`

## See Also

### Transitioning between layout types

`struct AnyLayout`

A type-erased instance of the layout protocol.

`struct HStackLayout`

A horizontal container that you can use in conditional layouts.

`struct VStackLayout`

A vertical container that you can use in conditional layouts.

`struct GridLayout`

A grid that you can use in conditional layouts.

Structure

# GridLayout

A grid that you can use in conditional layouts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    @frozen
    struct GridLayout

## Overview

This layout container behaves like a `Grid`, but conforms to the `Layout`
protocol so you can use it in the conditional layouts that you construct with
`AnyLayout`. If you don’t need a conditional layout, use `Grid` instead.

## Topics

### Creating a grid

`init(alignment: Alignment, horizontalSpacing: CGFloat?, verticalSpacing:
CGFloat?)`

Creates a grid with the specified spacing and alignment.

### Getting the grid’s properties

`var alignment: Alignment`

The alignment of subviews.

`var horizontalSpacing: CGFloat?`

The horizontal distance between adjacent subviews.

`var verticalSpacing: CGFloat?`

The vertical distance between adjacent subviews.

### Default Implementations

API Reference

Layout Implementations

## Relationships

### Conforms To

  * `Animatable`
  * `Layout`
  * `Sendable`

## See Also

### Transitioning between layout types

`struct AnyLayout`

A type-erased instance of the layout protocol.

`struct HStackLayout`

A horizontal container that you can use in conditional layouts.

`struct VStackLayout`

A vertical container that you can use in conditional layouts.

`struct ZStackLayout`

An overlaying container that you can use in conditional layouts.



# CardButtonStyle

Initializer

# init()

Creates a style that doesn’t pad a button’s content and applies a motion
effect to a focused button.

tvOS 14.0+

    
    
    init()

Instance Method

# makeBody(configuration:)

Creates a view that represents the body of a button.

tvOS 14.0+

    
    
    func makeBody(configuration: CardButtonStyle.Configuration) -> some View
    

##  Parameters

`configuration`

    

The properties of the button.

## Discussion

The system calls this method for each `Button` instance in a view hierarchy in
which `CardButtonStyle` is the current button style.



# Commands

Instance Property

# body

The contents of the command hierarchy.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    @CommandsBuilder
    var body: Self.Body { get }

**Required**

## Discussion

For any commands that you create, provide a computed `body` property that
defines the scene as a composition of other scenes. You can assemble a command
hierarchy from built-in commands that SwiftUI provides, as well as other
commands that you’ve defined.

## See Also

### Implementing commands

`associatedtype Body : Commands`

The type of commands that represents the body of this command hierarchy.

**Required**

Associated Type

# Body

The type of commands that represents the body of this command hierarchy.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    associatedtype Body : Commands

**Required**

## Discussion

When you create custom commands, Swift infers this type from your
implementation of the required `body` property.

## See Also

### Implementing commands

`var body: Self.Body`

The contents of the command hierarchy.

**Required**



# ContentMarginPlacement

Type Property

# automatic

The automatic placement.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static var automatic: ContentMarginPlacement { get }

## Discussion

Views that support margin customization can automatically use margins with
this placement. For example, a `ScrollView` will use this placement to
automatically inset both its content and scroll indicators by the specified
amount.

## See Also

### Getting the placement

`static var scrollContent: ContentMarginPlacement`

The scroll content placement.

`static var scrollIndicators: ContentMarginPlacement`

The scroll indicators placement.

Type Property

# scrollContent

The scroll content placement.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static var scrollContent: ContentMarginPlacement { get }

## Discussion

Scrollable views like `ScrollView` will use this placement to inset their
content, but not their scroll indicators.

## See Also

### Getting the placement

`static var automatic: ContentMarginPlacement`

The automatic placement.

`static var scrollIndicators: ContentMarginPlacement`

The scroll indicators placement.

Type Property

# scrollIndicators

The scroll indicators placement.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static var scrollIndicators: ContentMarginPlacement { get }

## Discussion

Scrollable views like `ScrollView` will use this placement to inset their
scroll indicators, but not their content.

## See Also

### Getting the placement

`static var automatic: ContentMarginPlacement`

The automatic placement.

`static var scrollContent: ContentMarginPlacement`

The scroll content placement.



# ControlSize

Case

# ControlSize.mini

A control version that is minimally sized.

iOS 15.0+  iPadOS 15.0+  macOS 10.15+  Mac Catalyst 15.0+  watchOS 9.0+
visionOS 1.0+

    
    
    case mini

## See Also

### Getting control sizes

`case small`

A control version that is proportionally smaller size for space-constrained
views.

`case regular`

A control version that is the default size.

`case large`

A control version that is prominently sized.

`case extraLarge`

Case

# ControlSize.small

A control version that is proportionally smaller size for space-constrained
views.

iOS 15.0+  iPadOS 15.0+  macOS 10.15+  Mac Catalyst 15.0+  watchOS 9.0+
visionOS 1.0+

    
    
    case small

## See Also

### Getting control sizes

`case mini`

A control version that is minimally sized.

`case regular`

A control version that is the default size.

`case large`

A control version that is prominently sized.

`case extraLarge`

Case

# ControlSize.regular

A control version that is the default size.

iOS 15.0+  iPadOS 15.0+  macOS 10.15+  Mac Catalyst 15.0+  watchOS 9.0+
visionOS 1.0+

    
    
    case regular

## See Also

### Getting control sizes

`case mini`

A control version that is minimally sized.

`case small`

A control version that is proportionally smaller size for space-constrained
views.

`case large`

A control version that is prominently sized.

`case extraLarge`

Case

# ControlSize.large

A control version that is prominently sized.

iOS 15.0+  iPadOS 15.0+  macOS 11.0+  Mac Catalyst 15.0+  watchOS 9.0+
visionOS 1.0+

    
    
    case large

## See Also

### Getting control sizes

`case mini`

A control version that is minimally sized.

`case small`

A control version that is proportionally smaller size for space-constrained
views.

`case regular`

A control version that is the default size.

`case extraLarge`

Case

# ControlSize.extraLarge

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  watchOS 10.0+
visionOS 1.0+

    
    
    case extraLarge

## See Also

### Getting control sizes

`case mini`

A control version that is minimally sized.

`case small`

A control version that is proportionally smaller size for space-constrained
views.

`case regular`

A control version that is the default size.

`case large`

A control version that is prominently sized.



# ContextMenu

Initializer

# init(menuItems:)

Creates a context menu.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  watchOS 6.0–7.0  Deprecated
visionOS 1.0+

    
    
    init(@ViewBuilder menuItems: () -> MenuItems)

Deprecated

Use `contextMenu(menuItems:)` instead.



# ContentShapeKinds

Type Property

# interaction

The kind for hit-testing and accessibility.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static let interaction: ContentShapeKinds

## Discussion

Setting a content shape with this kind causes the view to hit-test using the
specified shape.

## See Also

### Getting shape kinds

`static let dragPreview: ContentShapeKinds`

The kind for drag and drop previews.

`static let contextMenuPreview: ContentShapeKinds`

The kind for context menu previews.

`static let focusEffect: ContentShapeKinds`

The kind for the focus effect.

`static let hoverEffect: ContentShapeKinds`

The kind for hover effects.

`static let accessibility: ContentShapeKinds`

The kind for accessibility visuals and sorting.

Type Property

# dragPreview

The kind for drag and drop previews.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    static let dragPreview: ContentShapeKinds

## Discussion

When using this kind, only the preview shape is affected. To control the shape
used to hit-test and start the drag preview, use the `interaction` kind.

## See Also

### Getting shape kinds

`static let interaction: ContentShapeKinds`

The kind for hit-testing and accessibility.

`static let contextMenuPreview: ContentShapeKinds`

The kind for context menu previews.

`static let focusEffect: ContentShapeKinds`

The kind for the focus effect.

`static let hoverEffect: ContentShapeKinds`

The kind for hover effects.

`static let accessibility: ContentShapeKinds`

The kind for accessibility visuals and sorting.

Type Property

# contextMenuPreview

The kind for context menu previews.

iOS 15.0+  iPadOS 15.0+  Mac Catalyst 15.0+  tvOS 17.0+  visionOS 1.0+

    
    
    static let contextMenuPreview: ContentShapeKinds

## Discussion

When using this kind, only the preview shape will be affected. To control the
shape used to hit-test and start the context menu presentation, use the
`.interaction` kind.

## See Also

### Getting shape kinds

`static let interaction: ContentShapeKinds`

The kind for hit-testing and accessibility.

`static let dragPreview: ContentShapeKinds`

The kind for drag and drop previews.

`static let focusEffect: ContentShapeKinds`

The kind for the focus effect.

`static let hoverEffect: ContentShapeKinds`

The kind for hover effects.

`static let accessibility: ContentShapeKinds`

The kind for accessibility visuals and sorting.

Type Property

# focusEffect

The kind for the focus effect.

macOS 12.0+  watchOS 8.0+

    
    
    static let focusEffect: ContentShapeKinds

## See Also

### Getting shape kinds

`static let interaction: ContentShapeKinds`

The kind for hit-testing and accessibility.

`static let dragPreview: ContentShapeKinds`

The kind for drag and drop previews.

`static let contextMenuPreview: ContentShapeKinds`

The kind for context menu previews.

`static let hoverEffect: ContentShapeKinds`

The kind for hover effects.

`static let accessibility: ContentShapeKinds`

The kind for accessibility visuals and sorting.

Type Property

# hoverEffect

The kind for hover effects.

iOS 15.0+  iPadOS 15.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    static let hoverEffect: ContentShapeKinds

## Discussion

When using this kind, only the preview shape is affected. To control the shape
used to hit-test and start the effect, use the `interaction` kind.

This kind does not affect the `onHover` modifier.

## See Also

### Getting shape kinds

`static let interaction: ContentShapeKinds`

The kind for hit-testing and accessibility.

`static let dragPreview: ContentShapeKinds`

The kind for drag and drop previews.

`static let contextMenuPreview: ContentShapeKinds`

The kind for context menu previews.

`static let focusEffect: ContentShapeKinds`

The kind for the focus effect.

`static let accessibility: ContentShapeKinds`

The kind for accessibility visuals and sorting.

Initializer

# init(rawValue:)

Creates a content shape kind.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init(rawValue: Int)



# ContentUnavailableView

Type Property

# search

Creates a `ContentUnavailableView` instance that conveys a search state.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static var search: ContentUnavailableView<SearchUnavailableContent.Label, SearchUnavailableContent.Description, SearchUnavailableContent.Actions> { get }

Available when `Label` is `SearchUnavailableContent.Label`, `Description` is
`SearchUnavailableContent.Description`, and `Actions` is
`SearchUnavailableContent.Actions`.

## Discussion

A `ContentUnavailableView` initialized with this static member is expected to
be contained within a searchable view hierarchy. Such a configuration enables
the search query to be parsed into the view’s description.

For example, consider the usage of this static member in _ContactsListView_ :

## See Also

### Getting built-in unavailable views

`static func search(text: String) -> ContentUnavailableView<Label,
Description, Actions>`

Creates a `ContentUnavailableView` instance that conveys a search state.

Available when `Label` is `SearchUnavailableContent.Label`, `Description` is
`SearchUnavailableContent.Description`, and `Actions` is
`SearchUnavailableContent.Actions`.

Type Method

# search(text:)

Creates a `ContentUnavailableView` instance that conveys a search state.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static func search(text: String) -> ContentUnavailableView<Label, Description, Actions>

Available when `Label` is `SearchUnavailableContent.Label`, `Description` is
`SearchUnavailableContent.Description`, and `Actions` is
`SearchUnavailableContent.Actions`.

##  Parameters

`text`

    

The search text query.

## Discussion

For example, consider the usage of this static member in _ContactsListView_ :

## See Also

### Getting built-in unavailable views

`static var search: ContentUnavailableView<SearchUnavailableContent.Label,
SearchUnavailableContent.Description, SearchUnavailableContent.Actions>`

Creates a `ContentUnavailableView` instance that conveys a search state.

Available when `Label` is `SearchUnavailableContent.Label`, `Description` is
`SearchUnavailableContent.Description`, and `Actions` is
`SearchUnavailableContent.Actions`.

Initializer

# init(label:description:actions:)

Creates an interface, consisting of a label and additional content, that you
display when the content of your app is unavailable to users.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init(
        @ViewBuilder label: () -> Label,
        @ViewBuilder description: () -> Description = { EmptyView() },
        @ViewBuilder actions: () -> Actions = { EmptyView() }
    )

##  Parameters

`label`

    

The label that describes the view.

`description`

    

The view that describes the interface.

`actions`

    

The content of the interface actions.

Initializer

# init(_:image:description:)

Creates an interface, consisting of a title generated from a localized string,
an image and additional content, that you display when the content of your app
is unavailable to users.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init(
        _ title: LocalizedStringKey,
        image name: String,
        description: Text? = nil
    )

Available when `Label` is `Label<Text, Image>`, `Description` is `Text?`, and
`Actions` is `EmptyView`.

##  Parameters

`title`

    

A title generated from a localized string.

`image`

    

The name of the image resource to lookup.

`description`

    

The view that describes the interface.

## See Also

### Creating an unavailable view with an image

`init<S>(S, image: String, description: Text?)`

Creates an interface, consisting of a title generated from a string, an image
and additional content, that you display when the content of your app is
unavailable to users.

Available when `Label` is `Label<Text, Image>`, `Description` is `Text?`, and
`Actions` is `EmptyView`.

Initializer

# init(_:image:description:)

Creates an interface, consisting of a title generated from a string, an image
and additional content, that you display when the content of your app is
unavailable to users.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        image name: String,
        description: Text? = nil
    ) where S : StringProtocol

Available when `Label` is `Label<Text, Image>`, `Description` is `Text?`, and
`Actions` is `EmptyView`.

##  Parameters

`title`

    

A string used as the title.

`image`

    

The name of the image resource to lookup.

`description`

    

The view that describes the interface.

## See Also

### Creating an unavailable view with an image

`init(LocalizedStringKey, image: String, description: Text?)`

Creates an interface, consisting of a title generated from a localized string,
an image and additional content, that you display when the content of your app
is unavailable to users.

Available when `Label` is `Label<Text, Image>`, `Description` is `Text?`, and
`Actions` is `EmptyView`.

Initializer

# init(_:systemImage:description:)

Creates an interface, consisting of a title generated from a localized string,
a system icon image and additional content, that you display when the content
of your app is unavailable to users.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init(
        _ title: LocalizedStringKey,
        systemImage name: String,
        description: Text? = nil
    )

Available when `Label` is `Label<Text, Image>`, `Description` is `Text?`, and
`Actions` is `EmptyView`.

##  Parameters

`title`

    

A title generated from a localized string.

`systemImage`

    

The name of the system symbol image resource to lookup. Use the SF Symbols app
to look up the names of system symbol images.

`description`

    

The view that describes the interface.

## See Also

### Creating an unavailable view with a system image

`init<S>(S, systemImage: String, description: Text?)`

Creates an interface, consisting of a title generated from a string, a system
icon image and additional content, that you display when the content of your
app is unavailable to users.

Available when `Label` is `Label<Text, Image>`, `Description` is `Text?`, and
`Actions` is `EmptyView`.

Initializer

# init(_:systemImage:description:)

Creates an interface, consisting of a title generated from a string, a system
icon image and additional content, that you display when the content of your
app is unavailable to users.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        systemImage name: String,
        description: Text? = nil
    ) where S : StringProtocol

Available when `Label` is `Label<Text, Image>`, `Description` is `Text?`, and
`Actions` is `EmptyView`.

##  Parameters

`title`

    

A string used as the title.

`systemImage`

    

The name of the system symbol image resource to lookup. Use the SF Symbols app
to look up the names of system symbol images.

`description`

    

The view that describes the interface.

## See Also

### Creating an unavailable view with a system image

`init(LocalizedStringKey, systemImage: String, description: Text?)`

Creates an interface, consisting of a title generated from a localized string,
a system icon image and additional content, that you display when the content
of your app is unavailable to users.

Available when `Label` is `Label<Text, Image>`, `Description` is `Text?`, and
`Actions` is `EmptyView`.

Structure

# SearchUnavailableContent

A structure that represents the body of a static placeholder search view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct SearchUnavailableContent

## Overview

You don’t create this type directly. SwiftUI creates it when you build a
search`ContentUnavailableView`.

## Topics

### Getting content types

`struct Actions`

A view that represents the actions of a static `ContentUnavailableView.search`
view.

`struct Description`

A view that represents the description of a static
`ContentUnavailableView.search` view.

`struct Label`

A view that represents the label of a static placeholder search view.



# Canvas

Initializer

# init(opaque:colorMode:rendersAsynchronously:renderer:)

Creates and configures a canvas.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init(
        opaque: Bool = false,
        colorMode: ColorRenderingMode = .nonLinear,
        rendersAsynchronously: Bool = false,
        renderer: @escaping (inout GraphicsContext, CGSize) -> Void
    )

Available when `Symbols` is `EmptyView`.

##  Parameters

`opaque`

    

A Boolean that indicates whether the canvas is fully opaque. You might be able
to improve performance by setting this value to `true`, but then drawing a
non-opaque image into the context produces undefined results. The default is
`false`.

`colorMode`

    

A working color space and storage format of the canvas. The default is
`ColorRenderingMode.nonLinear`.

`rendersAsynchronously`

    

A Boolean that indicates whether the canvas can present its contents to its
parent view asynchronously. The default is `false`.

`renderer`

    

A closure in which you conduct immediate mode drawing. The closure takes two
inputs: a context that you use to issue drawing commands and a size —
representing the current size of the canvas — that you can use to customize
the content. The canvas calls the renderer any time it needs to redraw the
content.

## Discussion

Use this initializer to create a new canvas that you can draw into. For
example, you can draw a path:

The example above draws the outline of an ellipse that exactly inscribes a
canvas with a blue border:

For information about using a context to draw into a canvas, see
`GraphicsContext`. If you want to provide SwiftUI views for the renderer to
use as drawing elements, use
`init(opaque:colorMode:rendersAsynchronously:renderer:symbols:)` instead.

## See Also

### Creating a canvas

`init(opaque: Bool, colorMode: ColorRenderingMode, rendersAsynchronously:
Bool, renderer: (inout GraphicsContext, CGSize) -> Void, symbols: () ->
Symbols)`

Creates and configures a canvas that you supply with renderable child views.

Initializer

# init(opaque:colorMode:rendersAsynchronously:renderer:symbols:)

Creates and configures a canvas that you supply with renderable child views.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init(
        opaque: Bool = false,
        colorMode: ColorRenderingMode = .nonLinear,
        rendersAsynchronously: Bool = false,
        renderer: @escaping (inout GraphicsContext, CGSize) -> Void,
        @ViewBuilder symbols: () -> Symbols
    )

##  Parameters

`opaque`

    

A Boolean that indicates whether the canvas is fully opaque. You might be able
to improve performance by setting this value to `true`, but then drawing a
non-opaque image into the context produces undefined results. The default is
`false`.

`colorMode`

    

A working color space and storage format of the canvas. The default is
`ColorRenderingMode.nonLinear`.

`rendersAsynchronously`

    

A Boolean that indicates whether the canvas can present its contents to its
parent view asynchronously. The default is `false`.

`renderer`

    

A closure in which you conduct immediate mode drawing. The closure takes two
inputs: a context that you use to issue drawing commands and a size —
representing the current size of the canvas — that you can use to customize
the content. The canvas calls the renderer any time it needs to redraw the
content.

`symbols`

    

A `ViewBuilder` that you use to supply SwiftUI views to the canvas for use
during drawing. Uniquely tag each view using the `tag(_:)` modifier, so that
you can find them from within your renderer using the `resolveSymbol(id:)`
method.

## Discussion

This initializer behaves like the
`init(opaque:colorMode:rendersAsynchronously:renderer:)` initializer, except
that you also provide a collection of SwiftUI views for the renderer to use as
drawing elements.

SwiftUI stores a rendered version of each child view that you specify in the
`symbols` view builder and makes these available to the canvas. Tag each child
view so that you can retrieve it from within the renderer using the
`resolveSymbol(id:)` method. For example, you can create a scatter plot using
a passed-in child view as the mark for each data point:

You can use any SwiftUI view for the `mark` input:

If the `rects` input contains 50 randomly arranged `CGRect` instances, SwiftUI
draws a plot like this:

The symbol inputs, like all other elements that you draw to the canvas, lack
individual accessibility and interactivity, even if the original SwiftUI view
has these attributes. However, you can add accessibility and interactivity
modifers to the canvas as a whole.

## See Also

### Creating a canvas

`init(opaque: Bool, colorMode: ColorRenderingMode, rendersAsynchronously:
Bool, renderer: (inout GraphicsContext, CGSize) -> Void)`

Creates and configures a canvas.

Available when `Symbols` is `EmptyView`.

Instance Property

# isOpaque

A Boolean that indicates whether the canvas is fully opaque.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var isOpaque: Bool { get set }

## Discussion

You might be able to improve performance by setting this value to `true`,
making the canvas is fully opaque. However, in that case, the result of
drawing a non-opaque image into the canvas is undefined.

## See Also

### Managing opacity and color

`var colorMode: ColorRenderingMode`

The working color space and storage format of the canvas.

Instance Property

# colorMode

The working color space and storage format of the canvas.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var colorMode: ColorRenderingMode { get set }

## See Also

### Managing opacity and color

`var isOpaque: Bool`

A Boolean that indicates whether the canvas is fully opaque.

Instance Property

# symbols

A view that provides child views that you can use in the drawing callback.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var symbols: Symbols

## Discussion

Uniquely tag each child view using the `tag(_:)` modifier, so that you can
find them from within your renderer using the `resolveSymbol(id:)` method.

Instance Property

# rendersAsynchronously

A Boolean that indicates whether the canvas can present its contents to its
parent view asynchronously.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var rendersAsynchronously: Bool { get set }

## See Also

### Rendering

`var renderer: (inout GraphicsContext, CGSize) -> Void`

The drawing callback that you use to draw into the canvas.

Instance Property

# renderer

The drawing callback that you use to draw into the canvas.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var renderer: (inout GraphicsContext, CGSize) -> Void

##  Parameters

`context`

    

The graphics context to draw into.

`size`

    

The current size of the view.

## See Also

### Rendering

`var rendersAsynchronously: Bool`

A Boolean that indicates whether the canvas can present its contents to its
parent view asynchronously.



# ColorScheme

Case

# ColorScheme.light

The color scheme that corresponds to a light appearance.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case light

## See Also

### Getting color schemes

`case dark`

The color scheme that corresponds to a dark appearance.

Case

# ColorScheme.dark

The color scheme that corresponds to a dark appearance.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case dark

## See Also

### Getting color schemes

`case light`

The color scheme that corresponds to a light appearance.

Initializer

# init(_:)

Creates a color scheme from its user interface style equivalent.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  tvOS 14.0+  visionOS 1.0+

    
    
    init?(_ uiUserInterfaceStyle: UIUserInterfaceStyle)

Structure

# PreferredColorSchemeKey

A key for specifying the preferred color scheme.

iOS 13.0+  iPadOS 13.0+  macOS 11.0+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    struct PreferredColorSchemeKey

## Overview

Don’t use this key directly. Instead, set a preferred color scheme for a view
using the `preferredColorScheme(_:)` view modifier. Get the current color
scheme for a view by accessing the `colorScheme` value.

## Relationships

### Conforms To

  * `PreferenceKey`



# CompactDatePickerStyle

Initializer

# init()

Creates an instance of the compact date picker style.

iOS 14.0+  iPadOS 14.0+  macOS 10.15.4+  Mac Catalyst 13.4+  visionOS 1.0+

    
    
    init()



# Clipboard

Instance Method

# copyable(_:)

Specifies a list of items to copy in response to the system’s Copy command.

macOS 13.0+

    
    
    func copyable<T>(_ payload: @autoclosure @escaping () -> [T]) -> some View where T : Transferable
    

##  Parameters

`payload`

    

A closure that returns an array of items to copy to the Clipboard when someone
issues a Copy command. The items in the array must conform to the
`Transferable` protocol.

## Return Value

A view that adds one or more items to the Clipboard in response to a Copy
command.

## Discussion

Use this modifier to specify one or more items that the system copies to the
Clipboard when someone issues a Copy command while the modified view has
focus. People issue a Copy command by choosing Edit > Copy from the app’s
menu, or by using the Command-C keyboard shortcut. The system enables the Copy
command for your app when it detects copyable content.

For example, the following code enables people to copy all of the strings that
they select in a `List`:

The command copies each item’s representation as specified by the item’s
conformance to the `Transferable` protocol. The above example records
selection using each list item’s corresponding string, and strings conform to
the `Transferable` protocol by default. For more complex cases, you might need
to take additional steps.

For example, the following code displays colors composed from a list of `Item`
instances that contain both a color and its name, as well as an identifier.
The list manages selection using item identifiers:

This example does two things that the previous example didn’t have to:

  * It converts the list of selected item identifiers into a list of selected items for use with the copyable modifier.

  * It ensures that the copyable items conform to the `Transferable` protocol, using the item’s `name` property as the representation.

When someone copies the first item in the list, which appears in the interface
as a red rectangle, and then pastes into a text editor, they get the string
“red”.

Note

To enable people to copy using a custom action — like from a context menu item
— rather than using the system Copy command, update the Clipboard directly
using an `NSPasteboard` or a `UIPasteboard` instance.

## See Also

### Copying transferable items

`func cuttable<T>(for: T.Type, action: () -> [T]) -> some View`

Specifies an action that moves items to the Clipboard in response to the
system’s Cut command.

`func pasteDestination<T>(for: T.Type, action: ([T]) -> Void, validator: ([T])
-> [T]) -> some View`

Specifies an action that adds validated items to a view in response to the
system’s Paste command.

Instance Method

# cuttable(for:action:)

Specifies an action that moves items to the Clipboard in response to the
system’s Cut command.

macOS 13.0+

    
    
    func cuttable<T>(
        for payloadType: T.Type = T.self,
        action: @escaping () -> [T]
    ) -> some View where T : Transferable
    

##  Parameters

`payloadType`

    

The type of items to cut.

`action`

    

A closure that you implement to delete the selected items from the collection,
and return them for addition to the Clipboard. The items must conform to the
`Transferable` protocol.

## Return Value

A view that sends one or more items to the Clipboard in response to a Cut
command.

## Discussion

Use this modifier to remove one or more items from a collection of items and
then move the items to the Clipboard when someone issues a Cut command. People
issue a Cut command by choosing Edit > Cut from the app’s menu, or by using
the Command-X keyboard shortcut. The system enables the Cut command for your
app when it detects cuttable content.

For example, the following code enables people to remove bird names from a
list of birds:

When someone selects “owl” and issues a Cut command, the `action` closure
removes the selected item from the list and returns it. In response, SwiftUI
moves it to the Clipboard. If you want to copy the item without removing it,
use the `copyable(_:)` modifier instead.

Note

To enable people to cut using a custom action — like from a context menu item
— rather than using the system Cut command, update the Clipboard directly
using an `NSPasteboard` or a `UIPasteboard` instance.

## See Also

### Copying transferable items

`func copyable<T>(() -> [T]) -> some View`

Specifies a list of items to copy in response to the system’s Copy command.

`func pasteDestination<T>(for: T.Type, action: ([T]) -> Void, validator: ([T])
-> [T]) -> some View`

Specifies an action that adds validated items to a view in response to the
system’s Paste command.

Instance Method

# pasteDestination(for:action:validator:)

Specifies an action that adds validated items to a view in response to the
system’s Paste command.

macOS 13.0+

    
    
    func pasteDestination<T>(
        for payloadType: T.Type = T.self,
        action: @escaping ([T]) -> Void,
        validator: @escaping ([T]) -> [T] = { $0 }
    ) -> some View where T : Transferable
    

##  Parameters

`payloadType`

    

The type of data that the paste destination accepts. The type must conform to
the `Transferable` protocol.

`action`

    

The action to perform when someone uses the system’s Paste command to paste
one or more items of the payload type. The closure takes one parameter, which
is the array of items to paste.

`validator`

    

A closure that you implement to validate the data to paste. SwiftUI calls this
before it calls the `action` closure, and passes in an array of items to
validate. Inspect the items, and return an array that includes only those from
the input array that you consider valid. The array that you return from this
closure becomes the input to the `action` closure. If you return an empty
array, SwiftUI doesn’t call the `action` closure.

## Return Value

A view that people can paste into using the system Paste command.

## Discussion

Use this modifier to paste one or more items into a view from the Clipboard
when someone issues a Paste command. People issue a Paste command by choosing
Edit > Paste from the app’s menu, or by using the Command-V keyboard shortcut.
The system enables the Paste command for your app when the view in focus
provides a paste destination.

For example, the following code enables people to paste bird names into a
list:

The paste destination handles only pasted content with a type that matches the
`payloadType` that you specify. The list in the above example only accepts
strings.

Use the `validator` closure to restrict the pasted content to items that make
sense in the context of the view. The above example allows people to paste
only strings that match one of a known list of bird names because the list is
meant to contain only birds. You can omit the final closure if you don’t need
to perform any validation.

Note

To enable people to paste using a custom action — like from a context menu
item — rather than using the system Paste command, access the Clipboard
directly using an `NSPasteboard` or a `UIPasteboard` instance.

## See Also

### Copying transferable items

`func copyable<T>(() -> [T]) -> some View`

Specifies a list of items to copy in response to the system’s Copy command.

`func cuttable<T>(for: T.Type, action: () -> [T]) -> some View`

Specifies an action that moves items to the Clipboard in response to the
system’s Cut command.

Instance Method

# onCopyCommand(perform:)

Adds an action to perform in response to the system’s Copy command.

macOS 10.15+

    
    
    func onCopyCommand(perform payloadAction: (() -> [NSItemProvider])?) -> some View
    

##  Parameters

`payloadAction`

    

An action closure returning the `NSItemProvider` items that should be copied
to the Clipboard when the Copy command is triggered. If `action` is `nil`, the
Copy command is considered disabled.

## Return Value

A view that triggers `action` when a system Copy command occurs.

## See Also

### Copying items using item providers

`func onCutCommand(perform: (() -> [NSItemProvider])?) -> some View`

Adds an action to perform in response to the system’s Cut command.

`func onPasteCommand(of: [UTType], perform: ([NSItemProvider]) -> Void) ->
some View`

Adds an action to perform in response to the system’s Paste command.

`func onPasteCommand<Payload>(of: [UTType], validator: ([NSItemProvider]) ->
Payload?, perform: (Payload) -> Void) -> some View`

Adds an action to perform in response to the system’s Paste command with items
that you validate.

Instance Method

# onCutCommand(perform:)

Adds an action to perform in response to the system’s Cut command.

macOS 10.15+

    
    
    func onCutCommand(perform payloadAction: (() -> [NSItemProvider])?) -> some View
    

##  Parameters

`payloadAction`

    

An action closure that should delete the selected data and return
`NSItemProvider` items corresponding to that data, which should be written to
the Clipboard. If `action` is `nil`, the Cut command is considered disabled.

## Return Value

A view that triggers `action` when a system Cut command occurs.

## See Also

### Copying items using item providers

`func onCopyCommand(perform: (() -> [NSItemProvider])?) -> some View`

Adds an action to perform in response to the system’s Copy command.

`func onPasteCommand(of: [UTType], perform: ([NSItemProvider]) -> Void) ->
some View`

Adds an action to perform in response to the system’s Paste command.

`func onPasteCommand<Payload>(of: [UTType], validator: ([NSItemProvider]) ->
Payload?, perform: (Payload) -> Void) -> some View`

Adds an action to perform in response to the system’s Paste command with items
that you validate.

Instance Method

# onPasteCommand(of:perform:)

Adds an action to perform in response to the system’s Paste command.

macOS 11.0+

    
    
    func onPasteCommand(
        of supportedContentTypes: [UTType],
        perform payloadAction: @escaping ([NSItemProvider]) -> Void
    ) -> some View
    

##  Parameters

`supportedContentTypes`

    

The uniform type identifiers that describe the types of content this view can
accept through a paste action. If the Clipboard doesn’t contain any of the
supported types, the Paste command doesn’t trigger.

`payloadAction`

    

The action to perform when the Paste command triggers. The action closure’s
parameter contains items from the Clipboard with the types you specify in the
`supportedContentTypes` parameter.

## Return Value

A view that triggers `action` when a system Paste command occurs.

## Discussion

Pass an array of uniform type identifiers to the `supportedContentTypes`
parameter. Place the higher priority types closer to the beginning of the
array. The Clipboard items that the `action` closure receives have the most
preferred type out of all the types the source supports.

For example, if your app can handle plain text and rich text, but you prefer
rich text, place the rich text type first in the array. If rich text is
available when the paste action occurs, the `action` closure passes that rich
text along.

## See Also

### Copying items using item providers

`func onCopyCommand(perform: (() -> [NSItemProvider])?) -> some View`

Adds an action to perform in response to the system’s Copy command.

`func onCutCommand(perform: (() -> [NSItemProvider])?) -> some View`

Adds an action to perform in response to the system’s Cut command.

`func onPasteCommand<Payload>(of: [UTType], validator: ([NSItemProvider]) ->
Payload?, perform: (Payload) -> Void) -> some View`

Adds an action to perform in response to the system’s Paste command with items
that you validate.

Instance Method

# onPasteCommand(of:validator:perform:)

Adds an action to perform in response to the system’s Paste command with items
that you validate.

macOS 11.0+

    
    
    func onPasteCommand<Payload>(
        of supportedContentTypes: [UTType],
        validator: @escaping ([NSItemProvider]) -> Payload?,
        perform payloadAction: @escaping (Payload) -> Void
    ) -> some View
    

##  Parameters

`supportedContentTypes`

    

The uniform type identifiers that describe the types of content this view can
accept through a paste action. If the Clipboard doesn’t contain any of the
supported types, the Paste command doesn’t trigger.

`validator`

    

A handler that validates the command. This handler receives items from the
Clipboard with the types you specify in the `supportedContentTypes`. Use this
handler to decide whether the items are valid and preprocess them for the
`action` closure. If you return `nil` instead, the Paste command doesn’t
trigger.

`payloadAction`

    

The action to perform when the Paste command triggers.

## Return Value

A view that triggers `action` when the system Paste command is invoked,
validating the Paste command with `validator`.

## Discussion

Pass an array of uniform type identifiers to the `supportedContentTypes`
parameter. Place the higher priority types closer to the beginning of the
array. The Clipboard items that the `validator` closure receives have the most
preferred type out of all the types the source supports.

For example, if your app can handle plain text and rich text, but you prefer
rich text, place the rich text type first in the array. If rich text is
available when the paste action occurs, the `validator` closure passes that
rich text along.

## See Also

### Copying items using item providers

`func onCopyCommand(perform: (() -> [NSItemProvider])?) -> some View`

Adds an action to perform in response to the system’s Copy command.

`func onCutCommand(perform: (() -> [NSItemProvider])?) -> some View`

Adds an action to perform in response to the system’s Cut command.

`func onPasteCommand(of: [UTType], perform: ([NSItemProvider]) -> Void) ->
some View`

Adds an action to perform in response to the system’s Paste command.



# CoordinateSpace

Case

# CoordinateSpace.global

The global coordinate space at the root of the view hierarchy.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case global

## See Also

### Getting coordinate spaces

`case local`

The local coordinate space of the current view.

`case named(AnyHashable)`

A named reference to a view’s local coordinate space.

Case

# CoordinateSpace.local

The local coordinate space of the current view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case local

## See Also

### Getting coordinate spaces

`case global`

The global coordinate space at the root of the view hierarchy.

`case named(AnyHashable)`

A named reference to a view’s local coordinate space.

Case

# CoordinateSpace.named(_:)

A named reference to a view’s local coordinate space.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case named(AnyHashable)

## See Also

### Getting coordinate spaces

`case global`

The global coordinate space at the root of the view hierarchy.

`case local`

The local coordinate space of the current view.

Instance Property

# isGlobal

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var isGlobal: Bool { get }

## See Also

### Testing a space

`var isLocal: Bool`

Instance Property

# isLocal

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var isLocal: Bool { get }

## See Also

### Testing a space

`var isGlobal: Bool`



# ColorMatrix

Initializer

# init()

Creates the identity matrix.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init()

Instance Property

# r1

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var r1: Float

## See Also

### First column

`var g1: Float`

`var b1: Float`

`var a1: Float`

Instance Property

# g1

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var g1: Float

## See Also

### First column

`var r1: Float`

`var b1: Float`

`var a1: Float`

Instance Property

# b1

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var b1: Float

## See Also

### First column

`var r1: Float`

`var g1: Float`

`var a1: Float`

Instance Property

# a1

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var a1: Float

## See Also

### First column

`var r1: Float`

`var g1: Float`

`var b1: Float`

Instance Property

# r2

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var r2: Float

## See Also

### Second column

`var g2: Float`

`var b2: Float`

`var a2: Float`

Instance Property

# g2

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var g2: Float

## See Also

### Second column

`var r2: Float`

`var b2: Float`

`var a2: Float`

Instance Property

# b2

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var b2: Float

## See Also

### Second column

`var r2: Float`

`var g2: Float`

`var a2: Float`

Instance Property

# a2

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var a2: Float

## See Also

### Second column

`var r2: Float`

`var g2: Float`

`var b2: Float`

Instance Property

# r3

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var r3: Float

## See Also

### Third column

`var g3: Float`

`var b3: Float`

`var a3: Float`

Instance Property

# g3

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var g3: Float

## See Also

### Third column

`var r3: Float`

`var b3: Float`

`var a3: Float`

Instance Property

# b3

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var b3: Float

## See Also

### Third column

`var r3: Float`

`var g3: Float`

`var a3: Float`

Instance Property

# a3

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var a3: Float

## See Also

### Third column

`var r3: Float`

`var g3: Float`

`var b3: Float`

Instance Property

# r4

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var r4: Float

## See Also

### Fourth column

`var g4: Float`

`var b4: Float`

`var a4: Float`

Instance Property

# g4

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var g4: Float

## See Also

### Fourth column

`var r4: Float`

`var b4: Float`

`var a4: Float`

Instance Property

# b4

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var b4: Float

## See Also

### Fourth column

`var r4: Float`

`var g4: Float`

`var a4: Float`

Instance Property

# a4

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var a4: Float

## See Also

### Fourth column

`var r4: Float`

`var g4: Float`

`var b4: Float`

Instance Property

# r5

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var r5: Float

## See Also

### Fifth column

`var g5: Float`

`var b5: Float`

`var a5: Float`

Instance Property

# g5

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var g5: Float

## See Also

### Fifth column

`var r5: Float`

`var b5: Float`

`var a5: Float`

Instance Property

# b5

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var b5: Float

## See Also

### Fifth column

`var r5: Float`

`var g5: Float`

`var a5: Float`

Instance Property

# a5

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var a5: Float

## See Also

### Fifth column

`var r5: Float`

`var g5: Float`

`var b5: Float`



# CheckboxToggleStyle

Initializer

# init()

Creates a checkbox toggle style.

macOS 10.15+

    
    
    init()

## Discussion

Don’t call this initializer directly. Instead, use the `checkbox` static
variable to create this style:

Instance Method

# makeBody(configuration:)

Creates a view that represents the body of a toggle checkbox.

macOS 10.15+

    
    
    func makeBody(configuration: CheckboxToggleStyle.Configuration) -> some View
    

##  Parameters

`configuration`

    

The properties of the toggle, including a label and a binding to the toggle’s
state.

## Return Value

A view that represents a checkbox.

## Discussion

SwiftUI implements this required method of the `ToggleStyle` protocol to
define the behavior and appearance of the `checkbox` toggle style. Don’t call
this method directly. Rather, the system calls this method for each `Toggle`
instance in a view hierarchy that’s styled as a checkbox.



# ContentSizeCategory

Case

# ContentSizeCategory.extraExtraExtraLarge

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    case extraExtraExtraLarge

## See Also

### Content size categories

`case accessibilityExtraExtraExtraLarge`

`case accessibilityExtraExtraLarge`

`case accessibilityExtraLarge`

`case accessibilityLarge`

`case accessibilityMedium`

`case extraExtraLarge`

`case extraLarge`

`case extraSmall`

`case large`

`case medium`

`case small`

Case

# ContentSizeCategory.extraExtraLarge

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    case extraExtraLarge

## See Also

### Content size categories

`case accessibilityExtraExtraExtraLarge`

`case accessibilityExtraExtraLarge`

`case accessibilityExtraLarge`

`case accessibilityLarge`

`case accessibilityMedium`

`case extraExtraExtraLarge`

`case extraLarge`

`case extraSmall`

`case large`

`case medium`

`case small`

Case

# ContentSizeCategory.extraLarge

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    case extraLarge

## See Also

### Content size categories

`case accessibilityExtraExtraExtraLarge`

`case accessibilityExtraExtraLarge`

`case accessibilityExtraLarge`

`case accessibilityLarge`

`case accessibilityMedium`

`case extraExtraExtraLarge`

`case extraExtraLarge`

`case extraSmall`

`case large`

`case medium`

`case small`

Case

# ContentSizeCategory.extraSmall

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    case extraSmall

## See Also

### Content size categories

`case accessibilityExtraExtraExtraLarge`

`case accessibilityExtraExtraLarge`

`case accessibilityExtraLarge`

`case accessibilityLarge`

`case accessibilityMedium`

`case extraExtraExtraLarge`

`case extraExtraLarge`

`case extraLarge`

`case large`

`case medium`

`case small`

Case

# ContentSizeCategory.large

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    case large

## See Also

### Content size categories

`case accessibilityExtraExtraExtraLarge`

`case accessibilityExtraExtraLarge`

`case accessibilityExtraLarge`

`case accessibilityLarge`

`case accessibilityMedium`

`case extraExtraExtraLarge`

`case extraExtraLarge`

`case extraLarge`

`case extraSmall`

`case medium`

`case small`

Case

# ContentSizeCategory.medium

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    case medium

## See Also

### Content size categories

`case accessibilityExtraExtraExtraLarge`

`case accessibilityExtraExtraLarge`

`case accessibilityExtraLarge`

`case accessibilityLarge`

`case accessibilityMedium`

`case extraExtraExtraLarge`

`case extraExtraLarge`

`case extraLarge`

`case extraSmall`

`case large`

`case small`

Case

# ContentSizeCategory.small

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    case small

## See Also

### Content size categories

`case accessibilityExtraExtraExtraLarge`

`case accessibilityExtraExtraLarge`

`case accessibilityExtraLarge`

`case accessibilityLarge`

`case accessibilityMedium`

`case extraExtraExtraLarge`

`case extraExtraLarge`

`case extraLarge`

`case extraSmall`

`case large`

`case medium`

Initializer

# init(_:)

Create a size category from its UIContentSizeCategory equivalent.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  tvOS 14.0+  visionOS 1.0+

    
    
    init?(_ uiSizeCategory: UIContentSizeCategory)

Instance Property

# isAccessibilityCategory

A Boolean value indicating whether the content size category is one that is
associated with accessibility.

iOS 13.4–17.4  Deprecated  iPadOS 13.4–17.4  Deprecated  macOS 10.15.4–14.4
Deprecated  Mac Catalyst 13.4–17.4  Deprecated  tvOS 13.4–17.4  Deprecated
watchOS 6.2–10.4  Deprecated  visionOS 1.0+

    
    
    var isAccessibilityCategory: Bool { get }

Operator

# <(_:_:)

Returns a Boolean value indicating whether the value of the first argument is
less than that of the second argument.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    static func < (lhs: ContentSizeCategory, rhs: ContentSizeCategory) -> Bool

Operator

# >(_:_:)

Returns a Boolean value indicating whether the value of the first argument is
greater than that of the second argument.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    static func > (lhs: ContentSizeCategory, rhs: ContentSizeCategory) -> Bool

Operator

# <=(_:_:)

Returns a Boolean value indicating whether the value of the first argument is
less than or equal to that of the second argument.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    static func <= (lhs: ContentSizeCategory, rhs: ContentSizeCategory) -> Bool

Operator

# >=(_:_:)

Returns a Boolean value indicating whether the value of the first argument is
greater than or equal to that of the second argument.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    static func >= (lhs: ContentSizeCategory, rhs: ContentSizeCategory) -> Bool



# Capsule

Initializer

# init(style:)

Creates a new capsule shape.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(style: RoundedCornerStyle = .continuous)

##  Parameters

`style`

    

the style of corners drawn by the shape.

Instance Property

# style

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var style: RoundedCornerStyle



# Color

Initializer

# init(_:bundle:)

Creates a color from a color set that you indicate by name.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        _ name: String,
        bundle: Bundle? = nil
    )

##  Parameters

`name`

    

The name of the color resource to look up.

`bundle`

    

The bundle in which to search for the color resource. If you don’t indicate a
bundle, the initializer looks in your app’s main bundle by default.

## Discussion

Use this initializer to load a color from a color set stored in an Asset
Catalog. The system determines which color within the set to use based on the
environment at render time. For example, you can provide light and dark
versions for background and foreground colors:

You can then instantiate colors by referencing the names of the assets:

SwiftUI renders the appropriate colors for each appearance:

Initializer

# init(hue:saturation:brightness:opacity:)

Creates a constant color from hue, saturation, and brightness values.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        hue: Double,
        saturation: Double,
        brightness: Double,
        opacity: Double = 1
    )

##  Parameters

`hue`

    

A value in the range `0` to `1` that maps to an angle from 0° to 360° to
represent a shade on the color wheel.

`saturation`

    

A value in the range `0` to `1` that indicates how strongly the hue affects
the color. A value of `0` removes the effect of the hue, resulting in gray. As
the value increases, the hue becomes more prominent.

`brightness`

    

A value in the range `0` to `1` that indicates how bright a color is. A value
of `0` results in black, regardless of the other components. The color
lightens as you increase this component.

`opacity`

    

An optional degree of opacity, given in the range `0` to `1`. A value of `0`
means 100% transparency, while a value of `1` means 100% opacity. The default
is `1`.

## Discussion

This initializer creates a constant color that doesn’t change based on
context. For example, it doesn’t have distinct light and dark appearances,
unlike various system-defined colors, or a color that you load from an Asset
Catalog with `init(_:bundle:)`.

## See Also

### Creating a color from component values

`init(Color.RGBColorSpace, white: Double, opacity: Double)`

Creates a constant grayscale color.

`init(Color.RGBColorSpace, red: Double, green: Double, blue: Double, opacity:
Double)`

Creates a constant color from red, green, and blue component values.

`enum RGBColorSpace`

A profile that specifies how to interpret a color value for display.

Initializer

# init(_:white:opacity:)

Creates a constant grayscale color.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        _ colorSpace: Color.RGBColorSpace = .sRGB,
        white: Double,
        opacity: Double = 1
    )

##  Parameters

`colorSpace`

    

The profile that specifies how to interpret the color for display. The default
is `Color.RGBColorSpace.sRGB`.

`white`

    

A value that indicates how white the color is, with higher values closer to
100% white, and lower values closer to 100% black.

`opacity`

    

An optional degree of opacity, given in the range `0` to `1`. A value of `0`
means 100% transparency, while a value of `1` means 100% opacity. The default
is `1`.

## Discussion

This initializer creates a constant color that doesn’t change based on
context. For example, it doesn’t have distinct light and dark appearances,
unlike various system-defined colors, or a color that you load from an Asset
Catalog with `init(_:bundle:)`.

A standard sRGB color space clamps the `white` component to a range of `0` to
`1`, but SwiftUI colors use an extended sRGB color space, so you can use
component values outside that range. This makes it possible to create colors
using the `Color.RGBColorSpace.sRGB` or `Color.RGBColorSpace.sRGBLinear` color
space that make full use of the wider gamut of a diplay that supports
`Color.RGBColorSpace.displayP3`.

## See Also

### Creating a color from component values

`init(hue: Double, saturation: Double, brightness: Double, opacity: Double)`

Creates a constant color from hue, saturation, and brightness values.

`init(Color.RGBColorSpace, red: Double, green: Double, blue: Double, opacity:
Double)`

Creates a constant color from red, green, and blue component values.

`enum RGBColorSpace`

A profile that specifies how to interpret a color value for display.

Initializer

# init(_:red:green:blue:opacity:)

Creates a constant color from red, green, and blue component values.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        _ colorSpace: Color.RGBColorSpace = .sRGB,
        red: Double,
        green: Double,
        blue: Double,
        opacity: Double = 1
    )

##  Parameters

`colorSpace`

    

The profile that specifies how to interpret the color for display. The default
is `Color.RGBColorSpace.sRGB`.

`red`

    

The amount of red in the color.

`green`

    

The amount of green in the color.

`blue`

    

The amount of blue in the color.

`opacity`

    

An optional degree of opacity, given in the range `0` to `1`. A value of `0`
means 100% transparency, while a value of `1` means 100% opacity. The default
is `1`.

## Discussion

This initializer creates a constant color that doesn’t change based on
context. For example, it doesn’t have distinct light and dark appearances,
unlike various system-defined colors, or a color that you load from an Asset
Catalog with `init(_:bundle:)`.

A standard sRGB color space clamps each color component — `red`, `green`, and
`blue` — to a range of `0` to `1`, but SwiftUI colors use an extended sRGB
color space, so you can use component values outside that range. This makes it
possible to create colors using the `Color.RGBColorSpace.sRGB` or
`Color.RGBColorSpace.sRGBLinear` color space that make full use of the wider
gamut of a diplay that supports `Color.RGBColorSpace.displayP3`.

## See Also

### Creating a color from component values

`init(hue: Double, saturation: Double, brightness: Double, opacity: Double)`

Creates a constant color from hue, saturation, and brightness values.

`init(Color.RGBColorSpace, white: Double, opacity: Double)`

Creates a constant grayscale color.

`enum RGBColorSpace`

A profile that specifies how to interpret a color value for display.

Enumeration

# Color.RGBColorSpace

A profile that specifies how to interpret a color value for display.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    enum RGBColorSpace

## Topics

### Getting color spaces

`case sRGB`

The extended red, green, blue (sRGB) color space.

`case sRGBLinear`

The extended sRGB color space with a linear transfer function.

`case displayP3`

The Display P3 color space.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Creating a color from component values

`init(hue: Double, saturation: Double, brightness: Double, opacity: Double)`

Creates a constant color from hue, saturation, and brightness values.

`init(Color.RGBColorSpace, white: Double, opacity: Double)`

Creates a constant grayscale color.

`init(Color.RGBColorSpace, red: Double, green: Double, blue: Double, opacity:
Double)`

Creates a constant color from red, green, and blue component values.

Initializer

# init(uiColor:)

Creates a color from a UIKit color.

iOS 15.0+  iPadOS 15.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS 8.0+
visionOS 1.0+

    
    
    init(uiColor: UIColor)

##  Parameters

`color`

    

A `UIColor` instance from which to create a color.

## Discussion

Use this method to create a SwiftUI color from a `UIColor` instance. The new
color preserves the adaptability of the original. For example, you can create
a rectangle using `link` to see how the shade adjusts to match the user’s
system settings:

The `Box` view defined above automatically changes its appearance when the
user turns on Dark Mode. With the light and dark appearances placed side by
side, you can see the subtle difference in shades:

Note

Use this initializer only if you need to convert an existing `UIColor` to a
SwiftUI color. Otherwise, create a SwiftUI `Color` using an initializer like
`init(_:red:green:blue:opacity:)`, or use a system color like `blue`.

## See Also

### Creating a color from another color

`init(nsColor: NSColor)`

Creates a color from an AppKit color.

`init(cgColor: CGColor)`

Creates a color from a Core Graphics color.

Initializer

# init(nsColor:)

Creates a color from an AppKit color.

macOS 12.0+

    
    
    init(nsColor: NSColor)

##  Parameters

`color`

    

An `NSColor` instance from which to create a color.

## Discussion

Use this method to create a SwiftUI color from an `NSColor` instance. The new
color preserves the adaptability of the original. For example, you can create
a rectangle using `linkColor` to see how the shade adjusts to match the user’s
system settings:

The `Box` view defined above automatically changes its appearance when the
user turns on Dark Mode. With the light and dark appearances placed side by
side, you can see the subtle difference in shades:

Note

Use this initializer only if you need to convert an existing `NSColor` to a
SwiftUI color. Otherwise, create a SwiftUI `Color` using an initializer like
`init(_:red:green:blue:opacity:)`, or use a system color like `blue`.

## See Also

### Creating a color from another color

`init(uiColor: UIColor)`

Creates a color from a UIKit color.

`init(cgColor: CGColor)`

Creates a color from a Core Graphics color.

Initializer

# init(cgColor:)

Creates a color from a Core Graphics color.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init(cgColor: CGColor)

##  Parameters

`color`

    

A `CGColor` instance from which to create a color.

## See Also

### Creating a color from another color

`init(uiColor: UIColor)`

Creates a color from a UIKit color.

`init(nsColor: NSColor)`

Creates a color from an AppKit color.

Initializer

# init(_:)

Initialize a `Color` with a color resource.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init(_ resource: ColorResource)

Initializer

# init(_:)

Creates a color that represents the specified custom color.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init<T>(_ color: T) where T : Hashable, T : ShapeStyle, T.Resolved == Color.Resolved

## See Also

### Creating a custom color

`init(Color.Resolved)`

Creates a constant color with the values specified by the resolved color.

`func resolve(in: EnvironmentValues) -> Color.Resolved`

Evaluates this color to a resolved color given the current `context`.

Initializer

# init(_:)

Creates a constant color with the values specified by the resolved color.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init(_ resolved: Color.Resolved)

## See Also

### Creating a custom color

`init<T>(T)`

Creates a color that represents the specified custom color.

`func resolve(in: EnvironmentValues) -> Color.Resolved`

Evaluates this color to a resolved color given the current `context`.

Instance Method

# resolve(in:)

Evaluates this color to a resolved color given the current `context`.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func resolve(in environment: EnvironmentValues) -> Color.Resolved

## See Also

### Creating a custom color

`init<T>(T)`

Creates a color that represents the specified custom color.

`init(Color.Resolved)`

Creates a constant color with the values specified by the resolved color.

Type Property

# black

A black color suitable for use in UI elements.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let black: Color

## See Also

### Getting standard colors

`static let blue: Color`

A context-dependent blue color suitable for use in UI elements.

`static let brown: Color`

A context-dependent brown color suitable for use in UI elements.

`static let clear: Color`

A clear color suitable for use in UI elements.

`static let cyan: Color`

A context-dependent cyan color suitable for use in UI elements.

`static let gray: Color`

A context-dependent gray color suitable for use in UI elements.

`static let green: Color`

A context-dependent green color suitable for use in UI elements.

`static let indigo: Color`

A context-dependent indigo color suitable for use in UI elements.

`static let mint: Color`

A context-dependent mint color suitable for use in UI elements.

`static let orange: Color`

A context-dependent orange color suitable for use in UI elements.

`static let pink: Color`

A context-dependent pink color suitable for use in UI elements.

`static let purple: Color`

A context-dependent purple color suitable for use in UI elements.

`static let red: Color`

A context-dependent red color suitable for use in UI elements.

`static let teal: Color`

A context-dependent teal color suitable for use in UI elements.

`static let white: Color`

A white color suitable for use in UI elements.

`static let yellow: Color`

A context-dependent yellow color suitable for use in UI elements.

Type Property

# blue

A context-dependent blue color suitable for use in UI elements.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let blue: Color

## See Also

### Getting standard colors

`static let black: Color`

A black color suitable for use in UI elements.

`static let brown: Color`

A context-dependent brown color suitable for use in UI elements.

`static let clear: Color`

A clear color suitable for use in UI elements.

`static let cyan: Color`

A context-dependent cyan color suitable for use in UI elements.

`static let gray: Color`

A context-dependent gray color suitable for use in UI elements.

`static let green: Color`

A context-dependent green color suitable for use in UI elements.

`static let indigo: Color`

A context-dependent indigo color suitable for use in UI elements.

`static let mint: Color`

A context-dependent mint color suitable for use in UI elements.

`static let orange: Color`

A context-dependent orange color suitable for use in UI elements.

`static let pink: Color`

A context-dependent pink color suitable for use in UI elements.

`static let purple: Color`

A context-dependent purple color suitable for use in UI elements.

`static let red: Color`

A context-dependent red color suitable for use in UI elements.

`static let teal: Color`

A context-dependent teal color suitable for use in UI elements.

`static let white: Color`

A white color suitable for use in UI elements.

`static let yellow: Color`

A context-dependent yellow color suitable for use in UI elements.

Type Property

# brown

A context-dependent brown color suitable for use in UI elements.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static let brown: Color

## See Also

### Getting standard colors

`static let black: Color`

A black color suitable for use in UI elements.

`static let blue: Color`

A context-dependent blue color suitable for use in UI elements.

`static let clear: Color`

A clear color suitable for use in UI elements.

`static let cyan: Color`

A context-dependent cyan color suitable for use in UI elements.

`static let gray: Color`

A context-dependent gray color suitable for use in UI elements.

`static let green: Color`

A context-dependent green color suitable for use in UI elements.

`static let indigo: Color`

A context-dependent indigo color suitable for use in UI elements.

`static let mint: Color`

A context-dependent mint color suitable for use in UI elements.

`static let orange: Color`

A context-dependent orange color suitable for use in UI elements.

`static let pink: Color`

A context-dependent pink color suitable for use in UI elements.

`static let purple: Color`

A context-dependent purple color suitable for use in UI elements.

`static let red: Color`

A context-dependent red color suitable for use in UI elements.

`static let teal: Color`

A context-dependent teal color suitable for use in UI elements.

`static let white: Color`

A white color suitable for use in UI elements.

`static let yellow: Color`

A context-dependent yellow color suitable for use in UI elements.

Type Property

# clear

A clear color suitable for use in UI elements.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let clear: Color

## See Also

### Getting standard colors

`static let black: Color`

A black color suitable for use in UI elements.

`static let blue: Color`

A context-dependent blue color suitable for use in UI elements.

`static let brown: Color`

A context-dependent brown color suitable for use in UI elements.

`static let cyan: Color`

A context-dependent cyan color suitable for use in UI elements.

`static let gray: Color`

A context-dependent gray color suitable for use in UI elements.

`static let green: Color`

A context-dependent green color suitable for use in UI elements.

`static let indigo: Color`

A context-dependent indigo color suitable for use in UI elements.

`static let mint: Color`

A context-dependent mint color suitable for use in UI elements.

`static let orange: Color`

A context-dependent orange color suitable for use in UI elements.

`static let pink: Color`

A context-dependent pink color suitable for use in UI elements.

`static let purple: Color`

A context-dependent purple color suitable for use in UI elements.

`static let red: Color`

A context-dependent red color suitable for use in UI elements.

`static let teal: Color`

A context-dependent teal color suitable for use in UI elements.

`static let white: Color`

A white color suitable for use in UI elements.

`static let yellow: Color`

A context-dependent yellow color suitable for use in UI elements.

Type Property

# cyan

A context-dependent cyan color suitable for use in UI elements.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static let cyan: Color

## See Also

### Getting standard colors

`static let black: Color`

A black color suitable for use in UI elements.

`static let blue: Color`

A context-dependent blue color suitable for use in UI elements.

`static let brown: Color`

A context-dependent brown color suitable for use in UI elements.

`static let clear: Color`

A clear color suitable for use in UI elements.

`static let gray: Color`

A context-dependent gray color suitable for use in UI elements.

`static let green: Color`

A context-dependent green color suitable for use in UI elements.

`static let indigo: Color`

A context-dependent indigo color suitable for use in UI elements.

`static let mint: Color`

A context-dependent mint color suitable for use in UI elements.

`static let orange: Color`

A context-dependent orange color suitable for use in UI elements.

`static let pink: Color`

A context-dependent pink color suitable for use in UI elements.

`static let purple: Color`

A context-dependent purple color suitable for use in UI elements.

`static let red: Color`

A context-dependent red color suitable for use in UI elements.

`static let teal: Color`

A context-dependent teal color suitable for use in UI elements.

`static let white: Color`

A white color suitable for use in UI elements.

`static let yellow: Color`

A context-dependent yellow color suitable for use in UI elements.

Type Property

# gray

A context-dependent gray color suitable for use in UI elements.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let gray: Color

## See Also

### Getting standard colors

`static let black: Color`

A black color suitable for use in UI elements.

`static let blue: Color`

A context-dependent blue color suitable for use in UI elements.

`static let brown: Color`

A context-dependent brown color suitable for use in UI elements.

`static let clear: Color`

A clear color suitable for use in UI elements.

`static let cyan: Color`

A context-dependent cyan color suitable for use in UI elements.

`static let green: Color`

A context-dependent green color suitable for use in UI elements.

`static let indigo: Color`

A context-dependent indigo color suitable for use in UI elements.

`static let mint: Color`

A context-dependent mint color suitable for use in UI elements.

`static let orange: Color`

A context-dependent orange color suitable for use in UI elements.

`static let pink: Color`

A context-dependent pink color suitable for use in UI elements.

`static let purple: Color`

A context-dependent purple color suitable for use in UI elements.

`static let red: Color`

A context-dependent red color suitable for use in UI elements.

`static let teal: Color`

A context-dependent teal color suitable for use in UI elements.

`static let white: Color`

A white color suitable for use in UI elements.

`static let yellow: Color`

A context-dependent yellow color suitable for use in UI elements.

Type Property

# green

A context-dependent green color suitable for use in UI elements.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let green: Color

## See Also

### Getting standard colors

`static let black: Color`

A black color suitable for use in UI elements.

`static let blue: Color`

A context-dependent blue color suitable for use in UI elements.

`static let brown: Color`

A context-dependent brown color suitable for use in UI elements.

`static let clear: Color`

A clear color suitable for use in UI elements.

`static let cyan: Color`

A context-dependent cyan color suitable for use in UI elements.

`static let gray: Color`

A context-dependent gray color suitable for use in UI elements.

`static let indigo: Color`

A context-dependent indigo color suitable for use in UI elements.

`static let mint: Color`

A context-dependent mint color suitable for use in UI elements.

`static let orange: Color`

A context-dependent orange color suitable for use in UI elements.

`static let pink: Color`

A context-dependent pink color suitable for use in UI elements.

`static let purple: Color`

A context-dependent purple color suitable for use in UI elements.

`static let red: Color`

A context-dependent red color suitable for use in UI elements.

`static let teal: Color`

A context-dependent teal color suitable for use in UI elements.

`static let white: Color`

A white color suitable for use in UI elements.

`static let yellow: Color`

A context-dependent yellow color suitable for use in UI elements.

Type Property

# indigo

A context-dependent indigo color suitable for use in UI elements.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static let indigo: Color

## See Also

### Getting standard colors

`static let black: Color`

A black color suitable for use in UI elements.

`static let blue: Color`

A context-dependent blue color suitable for use in UI elements.

`static let brown: Color`

A context-dependent brown color suitable for use in UI elements.

`static let clear: Color`

A clear color suitable for use in UI elements.

`static let cyan: Color`

A context-dependent cyan color suitable for use in UI elements.

`static let gray: Color`

A context-dependent gray color suitable for use in UI elements.

`static let green: Color`

A context-dependent green color suitable for use in UI elements.

`static let mint: Color`

A context-dependent mint color suitable for use in UI elements.

`static let orange: Color`

A context-dependent orange color suitable for use in UI elements.

`static let pink: Color`

A context-dependent pink color suitable for use in UI elements.

`static let purple: Color`

A context-dependent purple color suitable for use in UI elements.

`static let red: Color`

A context-dependent red color suitable for use in UI elements.

`static let teal: Color`

A context-dependent teal color suitable for use in UI elements.

`static let white: Color`

A white color suitable for use in UI elements.

`static let yellow: Color`

A context-dependent yellow color suitable for use in UI elements.

Type Property

# mint

A context-dependent mint color suitable for use in UI elements.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static let mint: Color

## See Also

### Getting standard colors

`static let black: Color`

A black color suitable for use in UI elements.

`static let blue: Color`

A context-dependent blue color suitable for use in UI elements.

`static let brown: Color`

A context-dependent brown color suitable for use in UI elements.

`static let clear: Color`

A clear color suitable for use in UI elements.

`static let cyan: Color`

A context-dependent cyan color suitable for use in UI elements.

`static let gray: Color`

A context-dependent gray color suitable for use in UI elements.

`static let green: Color`

A context-dependent green color suitable for use in UI elements.

`static let indigo: Color`

A context-dependent indigo color suitable for use in UI elements.

`static let orange: Color`

A context-dependent orange color suitable for use in UI elements.

`static let pink: Color`

A context-dependent pink color suitable for use in UI elements.

`static let purple: Color`

A context-dependent purple color suitable for use in UI elements.

`static let red: Color`

A context-dependent red color suitable for use in UI elements.

`static let teal: Color`

A context-dependent teal color suitable for use in UI elements.

`static let white: Color`

A white color suitable for use in UI elements.

`static let yellow: Color`

A context-dependent yellow color suitable for use in UI elements.

Type Property

# orange

A context-dependent orange color suitable for use in UI elements.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let orange: Color

## See Also

### Getting standard colors

`static let black: Color`

A black color suitable for use in UI elements.

`static let blue: Color`

A context-dependent blue color suitable for use in UI elements.

`static let brown: Color`

A context-dependent brown color suitable for use in UI elements.

`static let clear: Color`

A clear color suitable for use in UI elements.

`static let cyan: Color`

A context-dependent cyan color suitable for use in UI elements.

`static let gray: Color`

A context-dependent gray color suitable for use in UI elements.

`static let green: Color`

A context-dependent green color suitable for use in UI elements.

`static let indigo: Color`

A context-dependent indigo color suitable for use in UI elements.

`static let mint: Color`

A context-dependent mint color suitable for use in UI elements.

`static let pink: Color`

A context-dependent pink color suitable for use in UI elements.

`static let purple: Color`

A context-dependent purple color suitable for use in UI elements.

`static let red: Color`

A context-dependent red color suitable for use in UI elements.

`static let teal: Color`

A context-dependent teal color suitable for use in UI elements.

`static let white: Color`

A white color suitable for use in UI elements.

`static let yellow: Color`

A context-dependent yellow color suitable for use in UI elements.

Type Property

# pink

A context-dependent pink color suitable for use in UI elements.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let pink: Color

## See Also

### Getting standard colors

`static let black: Color`

A black color suitable for use in UI elements.

`static let blue: Color`

A context-dependent blue color suitable for use in UI elements.

`static let brown: Color`

A context-dependent brown color suitable for use in UI elements.

`static let clear: Color`

A clear color suitable for use in UI elements.

`static let cyan: Color`

A context-dependent cyan color suitable for use in UI elements.

`static let gray: Color`

A context-dependent gray color suitable for use in UI elements.

`static let green: Color`

A context-dependent green color suitable for use in UI elements.

`static let indigo: Color`

A context-dependent indigo color suitable for use in UI elements.

`static let mint: Color`

A context-dependent mint color suitable for use in UI elements.

`static let orange: Color`

A context-dependent orange color suitable for use in UI elements.

`static let purple: Color`

A context-dependent purple color suitable for use in UI elements.

`static let red: Color`

A context-dependent red color suitable for use in UI elements.

`static let teal: Color`

A context-dependent teal color suitable for use in UI elements.

`static let white: Color`

A white color suitable for use in UI elements.

`static let yellow: Color`

A context-dependent yellow color suitable for use in UI elements.

Type Property

# purple

A context-dependent purple color suitable for use in UI elements.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let purple: Color

## See Also

### Getting standard colors

`static let black: Color`

A black color suitable for use in UI elements.

`static let blue: Color`

A context-dependent blue color suitable for use in UI elements.

`static let brown: Color`

A context-dependent brown color suitable for use in UI elements.

`static let clear: Color`

A clear color suitable for use in UI elements.

`static let cyan: Color`

A context-dependent cyan color suitable for use in UI elements.

`static let gray: Color`

A context-dependent gray color suitable for use in UI elements.

`static let green: Color`

A context-dependent green color suitable for use in UI elements.

`static let indigo: Color`

A context-dependent indigo color suitable for use in UI elements.

`static let mint: Color`

A context-dependent mint color suitable for use in UI elements.

`static let orange: Color`

A context-dependent orange color suitable for use in UI elements.

`static let pink: Color`

A context-dependent pink color suitable for use in UI elements.

`static let red: Color`

A context-dependent red color suitable for use in UI elements.

`static let teal: Color`

A context-dependent teal color suitable for use in UI elements.

`static let white: Color`

A white color suitable for use in UI elements.

`static let yellow: Color`

A context-dependent yellow color suitable for use in UI elements.

Type Property

# red

A context-dependent red color suitable for use in UI elements.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let red: Color

## See Also

### Getting standard colors

`static let black: Color`

A black color suitable for use in UI elements.

`static let blue: Color`

A context-dependent blue color suitable for use in UI elements.

`static let brown: Color`

A context-dependent brown color suitable for use in UI elements.

`static let clear: Color`

A clear color suitable for use in UI elements.

`static let cyan: Color`

A context-dependent cyan color suitable for use in UI elements.

`static let gray: Color`

A context-dependent gray color suitable for use in UI elements.

`static let green: Color`

A context-dependent green color suitable for use in UI elements.

`static let indigo: Color`

A context-dependent indigo color suitable for use in UI elements.

`static let mint: Color`

A context-dependent mint color suitable for use in UI elements.

`static let orange: Color`

A context-dependent orange color suitable for use in UI elements.

`static let pink: Color`

A context-dependent pink color suitable for use in UI elements.

`static let purple: Color`

A context-dependent purple color suitable for use in UI elements.

`static let teal: Color`

A context-dependent teal color suitable for use in UI elements.

`static let white: Color`

A white color suitable for use in UI elements.

`static let yellow: Color`

A context-dependent yellow color suitable for use in UI elements.

Type Property

# teal

A context-dependent teal color suitable for use in UI elements.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static let teal: Color

## See Also

### Getting standard colors

`static let black: Color`

A black color suitable for use in UI elements.

`static let blue: Color`

A context-dependent blue color suitable for use in UI elements.

`static let brown: Color`

A context-dependent brown color suitable for use in UI elements.

`static let clear: Color`

A clear color suitable for use in UI elements.

`static let cyan: Color`

A context-dependent cyan color suitable for use in UI elements.

`static let gray: Color`

A context-dependent gray color suitable for use in UI elements.

`static let green: Color`

A context-dependent green color suitable for use in UI elements.

`static let indigo: Color`

A context-dependent indigo color suitable for use in UI elements.

`static let mint: Color`

A context-dependent mint color suitable for use in UI elements.

`static let orange: Color`

A context-dependent orange color suitable for use in UI elements.

`static let pink: Color`

A context-dependent pink color suitable for use in UI elements.

`static let purple: Color`

A context-dependent purple color suitable for use in UI elements.

`static let red: Color`

A context-dependent red color suitable for use in UI elements.

`static let white: Color`

A white color suitable for use in UI elements.

`static let yellow: Color`

A context-dependent yellow color suitable for use in UI elements.

Type Property

# white

A white color suitable for use in UI elements.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let white: Color

## See Also

### Getting standard colors

`static let black: Color`

A black color suitable for use in UI elements.

`static let blue: Color`

A context-dependent blue color suitable for use in UI elements.

`static let brown: Color`

A context-dependent brown color suitable for use in UI elements.

`static let clear: Color`

A clear color suitable for use in UI elements.

`static let cyan: Color`

A context-dependent cyan color suitable for use in UI elements.

`static let gray: Color`

A context-dependent gray color suitable for use in UI elements.

`static let green: Color`

A context-dependent green color suitable for use in UI elements.

`static let indigo: Color`

A context-dependent indigo color suitable for use in UI elements.

`static let mint: Color`

A context-dependent mint color suitable for use in UI elements.

`static let orange: Color`

A context-dependent orange color suitable for use in UI elements.

`static let pink: Color`

A context-dependent pink color suitable for use in UI elements.

`static let purple: Color`

A context-dependent purple color suitable for use in UI elements.

`static let red: Color`

A context-dependent red color suitable for use in UI elements.

`static let teal: Color`

A context-dependent teal color suitable for use in UI elements.

`static let yellow: Color`

A context-dependent yellow color suitable for use in UI elements.

Type Property

# yellow

A context-dependent yellow color suitable for use in UI elements.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let yellow: Color

## See Also

### Getting standard colors

`static let black: Color`

A black color suitable for use in UI elements.

`static let blue: Color`

A context-dependent blue color suitable for use in UI elements.

`static let brown: Color`

A context-dependent brown color suitable for use in UI elements.

`static let clear: Color`

A clear color suitable for use in UI elements.

`static let cyan: Color`

A context-dependent cyan color suitable for use in UI elements.

`static let gray: Color`

A context-dependent gray color suitable for use in UI elements.

`static let green: Color`

A context-dependent green color suitable for use in UI elements.

`static let indigo: Color`

A context-dependent indigo color suitable for use in UI elements.

`static let mint: Color`

A context-dependent mint color suitable for use in UI elements.

`static let orange: Color`

A context-dependent orange color suitable for use in UI elements.

`static let pink: Color`

A context-dependent pink color suitable for use in UI elements.

`static let purple: Color`

A context-dependent purple color suitable for use in UI elements.

`static let red: Color`

A context-dependent red color suitable for use in UI elements.

`static let teal: Color`

A context-dependent teal color suitable for use in UI elements.

`static let white: Color`

A white color suitable for use in UI elements.

Type Property

# accentColor

A color that reflects the accent color of the system or app.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static var accentColor: Color { get }

## Discussion

The accent color is a broad theme color applied to views and controls. You can
set it at the application level by specifying an accent color in your app’s
asset catalog.

Note

In macOS, SwiftUI applies customization of the accent color only if the user
chooses Multicolor under General > Accent color in System Preferences.

The following code renders a `Text` view using the app’s accent color:

## See Also

### Getting semantic colors

`static let primary: Color`

The color to use for primary content.

`static let secondary: Color`

The color to use for secondary content.

Type Property

# primary

The color to use for primary content.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let primary: Color

## See Also

### Getting semantic colors

`static var accentColor: Color`

A color that reflects the accent color of the system or app.

`static let secondary: Color`

The color to use for secondary content.

Type Property

# secondary

The color to use for secondary content.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let secondary: Color

## See Also

### Getting semantic colors

`static var accentColor: Color`

A color that reflects the accent color of the system or app.

`static let primary: Color`

The color to use for primary content.

Instance Method

# opacity(_:)

Multiplies the opacity of the color by the given amount.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func opacity(_ opacity: Double) -> Color

##  Parameters

`opacity`

    

The amount by which to multiply the opacity of the color.

## Return Value

A view with modified opacity.

## See Also

### Modifying a color

`var gradient: AnyGradient`

Returns the standard gradient for the color `self`.

Instance Property

# gradient

Returns the standard gradient for the color `self`.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var gradient: AnyGradient { get }

## Discussion

For example, filling a rectangle with a gradient derived from the standard
blue color:

## See Also

### Modifying a color

`func opacity(Double) -> Color`

Multiplies the opacity of the color by the given amount.

Instance Property

# description

A textual representation of the color.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var description: String { get }

## Discussion

Use this method to get a string that represents the color. The
`print(_:separator:terminator:)` function uses this property to get a string
representing an instance:

Operator

# ==(_:_:)

Indicates whether two colors are equal.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static func == (lhs: Color, rhs: Color) -> Bool

##  Parameters

`lhs`

    

The first color to compare.

`rhs`

    

The second color to compare.

## Return Value

A Boolean that’s set to `true` if the two colors are equal.

## See Also

### Comparing colors

`func hash(into: inout Hasher)`

Hashes the essential components of the color by feeding them into the given
hash function.

Instance Method

# hash(into:)

Hashes the essential components of the color by feeding them into the given
hash function.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func hash(into hasher: inout Hasher)

##  Parameters

`hasher`

    

The hash function to use when combining the components of the color.

## See Also

### Comparing colors

`static func == (Color, Color) -> Bool`

Indicates whether two colors are equal.

Initializer

# init(_:)

Creates a color from a UIKit color.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  Mac Catalyst
13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated  watchOS 6.0–10.4
Deprecated  visionOS 1.0+

    
    
    init(_ color: UIColor)

Deprecated

Use `init(uiColor:)` instead.

##  Parameters

`color`

    

A `UIColor` instance from which to create a color.

## Discussion

Use this method to create a SwiftUI color from a `UIColor` instance. The new
color preserves the adaptability of the original. For example, you can create
a rectangle using `link` to see how the shade adjusts to match the user’s
system settings:

The `Box` view defined above automatically changes its appearance when the
user turns on Dark Mode. With the light and dark appearances placed side by
side, you can see the subtle difference in shades:

Note

Use this initializer only if you need to convert an existing `UIColor` to a
SwiftUI color. Otherwise, create a SwiftUI `Color` using an initializer like
`init(_:red:green:blue:opacity:)`, or use a system color like `blue`.

## See Also

### Deprecated symbols

`init(NSColor)`

Creates a color from an AppKit color.

Deprecated

`init(CGColor)`

Creates a color from a Core Graphics color.

Deprecated

`var cgColor: CGColor?`

A Core Graphics representation of the color, if available.

Initializer

# init(_:)

Creates a color from an AppKit color.

macOS 10.15–14.4  Deprecated

    
    
    init(_ color: NSColor)

Deprecated

Use `init(nsColor:)` instead.

##  Parameters

`color`

    

An `NSColor` instance from which to create a color.

## Discussion

Use this method to create a SwiftUI color from an `NSColor` instance. The new
color preserves the adaptability of the original. For example, you can create
a rectangle using `linkColor` to see how the shade adjusts to match the user’s
system settings:

The `Box` view defined above automatically changes its appearance when the
user turns on Dark Mode. With the light and dark appearances placed side by
side, you can see the subtle difference in shades:

Note

Use this initializer only if you need to convert an existing `NSColor` to a
SwiftUI color. Otherwise, create a SwiftUI `Color` using an initializer like
`init(_:red:green:blue:opacity:)`, or use a system color like `blue`.

## See Also

### Deprecated symbols

`init(UIColor)`

Creates a color from a UIKit color.

Deprecated

`init(CGColor)`

Creates a color from a Core Graphics color.

Deprecated

`var cgColor: CGColor?`

A Core Graphics representation of the color, if available.

Initializer

# init(_:)

Creates a color from a Core Graphics color.

iOS 14.0–17.4  Deprecated  iPadOS 14.0–17.4  Deprecated  macOS 11.0–14.4
Deprecated  Mac Catalyst 14.0–17.4  Deprecated  tvOS 14.0–17.4  Deprecated
watchOS 7.0–10.4  Deprecated  visionOS 1.0+

    
    
    init(_ cgColor: CGColor)

Deprecated

Use `init(cgColor:)` instead.

##  Parameters

`color`

    

A `CGColor` instance from which to create a color.

## See Also

### Deprecated symbols

`init(UIColor)`

Creates a color from a UIKit color.

Deprecated

`init(NSColor)`

Creates a color from an AppKit color.

Deprecated

`var cgColor: CGColor?`

A Core Graphics representation of the color, if available.

Instance Property

# cgColor

A Core Graphics representation of the color, if available.

iOS 14.0–17.4  Deprecated  iPadOS 14.0–17.4  Deprecated  macOS 11.0–14.4
Deprecated  Mac Catalyst 14.0–17.4  Deprecated  tvOS 14.0–17.4  Deprecated
watchOS 7.0–10.4  Deprecated  visionOS 1.0+

    
    
    var cgColor: CGColor? { get }

## Discussion

You can get a `CGColor` instance from a constant SwiftUI color. This includes
colors you create from a Core Graphics color, from RGB or HSB components, or
from constant UIKit and AppKit colors.

For a dynamic color, like one you load from an Asset Catalog using
`init(_:bundle:)`, or one you create from a dynamic UIKit or AppKit color,
this property is `nil`. To evaluate all types of colors, use the
`resolve(in:)` method.

## See Also

### Deprecated symbols

`init(UIColor)`

Creates a color from a UIKit color.

Deprecated

`init(NSColor)`

Creates a color from an AppKit color.

Deprecated

`init(CGColor)`

Creates a color from a Core Graphics color.

Deprecated

Collection

API Collection

# ShapeStyle Implementations

## Topics

### Structures

`struct Resolved`

A concrete color value.

Collection

API Collection

# Transferable Implementations

## Topics

### Type Properties

`static var transferRepresentation: some TransferRepresentation`

One group of colors–constant colors–created with explicitly specified
component values are transferred as is.



# CustomizableToolbarContent

Instance Method

# defaultCustomization()

Configures customizable toolbar content with the default visibility and
options.

iOS 16.0–16.0  Deprecated  iPadOS 16.0–16.0  Deprecated  macOS 13.0–13.0
Deprecated  Mac Catalyst 16.0–16.0  Deprecated  tvOS 16.0–16.0  Deprecated
watchOS 9.0–9.0  Deprecated  visionOS 1.0+

    
    
    func defaultCustomization() -> some CustomizableToolbarContent
    

## Discussion

Use the `defaultCustomization(_:options:)` modifier providing either a
`defaultVisibility` or `options` instead.

## See Also

### Using default options

`func defaultCustomization(Visibility, options: ToolbarCustomizationOptions)
-> some CustomizableToolbarContent`

Configures the way customizable toolbar items with the default behavior
behave.

Instance Method

# defaultCustomization(_:options:)

Configures the way customizable toolbar items with the default behavior
behave.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func defaultCustomization(
        _ defaultVisibility: Visibility = .automatic,
        options: ToolbarCustomizationOptions = []
    ) -> some CustomizableToolbarContent
    

##  Parameters

`defaultVisibility`

    

The default visibility of toolbar content with the default customization
behavior.

`options`

    

The customization options to configure the behavior of toolbar content with
the default customization behavior.

## Discussion

Default customizable items support a variety of edits by the user.

  * A user can add an an item that is not in the toolbar.

  * A user can remove an item that is in the toolbar.

  * A user can move an item within the toolbar.

By default, all default customizable items will be initially present in the
toolbar. Provide a value of `Visibility.hidden` to this modifier to specify
that items should initially be hidden from the user, and require them to add
those items to the toolbar if desired.

You can ensure that the user can always use an item with default
customizability, even if it’s removed from the customizable toolbar. To do
this, provide the `alwaysAvailable` option. Unlike a customizable item with a
customization behavior of `ToolbarCustomizationBehavior/none` which always
remain in the toolbar itself, these items will remain in the overflow if the
user removes them from the toolbar.

Provide a value of `alwaysAvailable` to the options parameter of this modifier
to receive this behavior.

## See Also

### Using default options

`func defaultCustomization() -> some CustomizableToolbarContent`

Configures customizable toolbar content with the default visibility and
options.

Instance Method

# customizationBehavior(_:)

Configures the customization behavior of customizable toolbar content.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func customizationBehavior(_ behavior: ToolbarCustomizationBehavior) -> some CustomizableToolbarContent
    

##  Parameters

`behavior`

    

The customization behavior of the customizable toolbar content.

## Discussion

Customizable toolbar items support different kinds of customization:

  * A user can add an an item that is not in the toolbar.

  * A user can remove an item that is in the toolbar.

  * A user can move an item within the toolbar.

Based on the customization behavior of the toolbar items, different edits will
be supported.

Use this modifier to the customization behavior a user can perform on your
toolbar items. In the following example, the customizable toolbar item
supports all of the different kinds of toolbar customizations and starts in
the toolbar.

You can create an item that can not be removed from the toolbar or moved
within the toolbar by passing a value of `disabled` to this modifier.

You can create an item that can not be removed from the toolbar, but can be
moved by passing a value of `reorderable`.



# Controls and indicators

Structure

# Button

A control that initiates an action.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    struct Button<Label> where Label : View

## Overview

You create a button by providing an action and a label. The action is either a
method or closure property that does something when a user clicks or taps the
button. The label is a view that describes the button’s action — for example,
by showing text, an icon, or both.

The label of a button can be any kind of view, such as a `Text` view for text-
only labels:

Or a `Label` view, for buttons with both a title and an icon:

For those common cases, you can also use the convenience initializers that
take a title string or `LocalizedStringKey` as their first parameter, and
optionally a system image name or `ImageResource` as their second parameter,
instead of a trailing closure:

Prefer to use these convenience initializers, or a `Label` view, when
providing both a title and an icon. This allows the button to dynamically
adapt its appearance to render its title and icon correctly in containers such
as toolbars and menus. For example, on iOS, buttons only display their icons
by default when placed in toolbars, but show both a leading title and trailing
icon in menus. Defining labels this way also helps with accessibility — for
example, applying the `labelStyle(_:)` modifier with an `iconOnly` style to
the button will cause it to only visually display its icon, but still use its
title to describe the button in accessibility modes like VoiceOver:

Avoid labels that only use images or exclusively visual components without an
accessibility label.

How the user activates the button varies by platform:

  * In iOS and watchOS, the user taps the button.

  * In macOS, the user clicks the button.

  * In tvOS, the user presses “select” on an external remote, like the Siri Remote, while focusing on the button.

The appearance of the button depends on factors like where you place it,
whether you assign it a role, and how you style it.

### Adding buttons to containers

Use buttons for any user interface element that initiates an action. Buttons
automatically adapt their visual style to match the expected style within
these different containers and contexts. For example, to create a `List` cell
that initiates an action when selected by the user, add a button to the list’s
content:

Similarly, to create a context menu item that initiates an action, add a
button to the `contextMenu(_:)` modifier’s content closure:

This pattern extends to most other container views in SwiftUI that have
customizable, interactive content, like `Form` instances.

### Assigning a role

You can optionally initialize a button with a `ButtonRole` that characterizes
the button’s purpose. For example, you can create a `destructive` button for a
deletion action:

The system uses the button’s role to style the button appropriately in every
context. For example, a destructive button in a contextual menu appears with a
red foreground color:

If you don’t specify a role for a button, the system applies an appropriate
default appearance.

### Styling buttons

You can customize a button’s appearance using one of the standard button
styles, like `bordered`, and apply the style with the `buttonStyle(_:)`
modifier:

If you apply the style to a container view, as in the example above, all the
buttons in the container use the style:

You can also create custom styles. To add a custom appearance with standard
interaction behavior, create a style that conforms to the `ButtonStyle`
protocol. To customize both appearance and interaction behavior, create a
style that conforms to the `PrimitiveButtonStyle` protocol. Custom styles can
also read the button’s role and use it to adjust the button’s appearance.

## Topics

### Creating a button

`init(action: () -> Void, label: () -> Label)`

Creates a button that displays a custom label.

`init(LocalizedStringKey, action: () -> Void)`

Creates a button that generates its label from a localized string key.

Available when `Label` is `Text`.

`init<S>(S, action: () -> Void)`

Creates a button that generates its label from a string.

Available when `Label` is `Text`.

### Creating a button with a role

`init(role: ButtonRole?, action: () -> Void, label: () -> Label)`

Creates a button with a specified role that displays a custom label.

Available when `Label` conforms to `View`.

`init(LocalizedStringKey, role: ButtonRole?, action: () -> Void)`

Creates a button with a specified role that generates its label from a
localized string key.

Available when `Label` is `Text`.

`init<S>(S, role: ButtonRole?, action: () -> Void)`

Creates a button with a specified role that generates its label from a string.

Available when `Label` is `Text`.

### Creating a button with an image resource

`init(LocalizedStringKey, image: ImageResource, action: () -> Void)`

Creates a button that generates its label from a localized string key and
image resource.

Available when `Label` is `Label<Text, Image>`.

`init<S>(S, image: ImageResource, action: () -> Void)`

Creates a button that generates its label from a string and image resource.

Available when `Label` is `Label<Text, Image>`.

`init(LocalizedStringKey, image: ImageResource, role: ButtonRole?, action: ()
-> Void)`

Creates a button with a specified role that generates its label from a
localized string key and an image resource.

Available when `Label` is `Label<Text, Image>`.

`init<S>(S, image: ImageResource, role: ButtonRole?, action: () -> Void)`

Creates a button with a specified role that generates its label from a string
and an image resource.

Available when `Label` is `Label<Text, Image>`.

### Creating a button with a system image

`init<S>(S, systemImage: String, action: () -> Void)`

Creates a button that generates its label from a string and system image name.

Available when `Label` is `Label<Text, Image>`.

`init(LocalizedStringKey, systemImage: String, action: () -> Void)`

Creates a button that generates its label from a localized string key and
system image name.

Available when `Label` is `Label<Text, Image>`.

`init<S>(S, systemImage: String, role: ButtonRole?, action: () -> Void)`

Creates a button with a specified role that generates its label from a string
and a system image and an image resource.

Available when `Label` is `Label<Text, Image>`.

`init(LocalizedStringKey, systemImage: String, role: ButtonRole?, action: ()
-> Void)`

Creates a button with a specified role that generates its label from a
localized string key and a system image.

Available when `Label` is `Label<Text, Image>`.

### Creating a button from a configuration

`init(PrimitiveButtonStyleConfiguration)`

Creates a button based on a configuration for a style with a custom appearance
and custom interaction behavior.

Available when `Label` is `PrimitiveButtonStyleConfiguration.Label`.

### Creating a button to perform an App Intent

`init<I>(intent: I, label: () -> Label)`

Creates a button that performs an `AppIntent`.

Available when `Label` conforms to `View`.

`init(LocalizedStringKey, intent: some AppIntent)`

Creates a button that performs an `AppIntent` and generates its label from a
localized string key.

Available when `Label` is `Text`.

`init<S>(S, intent: some AppIntent)`

Creates a button that performs an `AppIntent` and generates its label from a
string.

Available when `Label` is `Text`.

`init(LocalizedStringKey, image: ImageResource, role: ButtonRole?, intent:
some AppIntent)`

Creates a button with a specified role that performs an `AppIntent` and
generates its label from a localized string key and an image resource.

Available when `Label` is `Label<Text, Image>`.

`init(some StringProtocol, image: ImageResource, role: ButtonRole?, intent:
some AppIntent)`

Creates a button with a specified role that generates its label from a string
and an image resource.

Available when `Label` is `Label<Text, Image>`.

`init(LocalizedStringKey, role: ButtonRole?, intent: some AppIntent)`

Creates a button with a specified role that performs an `AppIntent` and
generates its label from a localized string key.

Available when `Label` is `Text`.

`init(some StringProtocol, role: ButtonRole?, intent: some AppIntent)`

Creates a button with a specified role that performs an `AppIntent` and
generates its label from a string.

Available when `Label` is `Text`.

`init(LocalizedStringKey, systemImage: String, role: ButtonRole?, intent: some
AppIntent)`

Creates a button with a specified role that performs an `AppIntent` and
generates its label from a localized string key and a system image.

Available when `Label` is `Label<Text, Image>`.

`init(some StringProtocol, systemImage: String, role: ButtonRole?, intent:
some AppIntent)`

Creates a button with a specified role that generates its label from a string
and a system image.

Available when `Label` is `Label<Text, Image>`.

`init(role: ButtonRole?, intent: some AppIntent, label: () -> Label)`

Creates a button with a specified role that performs an `AppIntent`.

Available when `Label` conforms to `View`.

## Relationships

### Conforms To

  * `View`

## See Also

### Creating buttons

`func buttonStyle<S>(S) -> some View`

Sets the style for buttons within this view to a button style with a custom
appearance and standard interaction behavior.

`func buttonStyle<S>(S) -> some View`

Sets the style for buttons within this view to a button style with a custom
appearance and custom interaction behavior.

`func buttonBorderShape(ButtonBorderShape) -> some View`

Sets the border shape for buttons in this view.

`func buttonRepeatBehavior(ButtonRepeatBehavior) -> some View`

Sets whether buttons in this view should repeatedly trigger their actions on
prolonged interactions.

`var buttonRepeatBehavior: ButtonRepeatBehavior`

Whether buttons with this associated environment should repeatedly trigger
their actions on prolonged interactions.

`struct ButtonBorderShape`

A shape that is used to draw a button’s border.

`struct ButtonRole`

A value that describes the purpose of a button.

`struct ButtonRepeatBehavior`

The options for controlling the repeatability of button actions.

Instance Method

# buttonStyle(_:)

Sets the style for buttons within this view to a button style with a custom
appearance and standard interaction behavior.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func buttonStyle<S>(_ style: S) -> some View where S : ButtonStyle
    

## Discussion

Use this modifier to set a specific style for all button instances within a
view:

You can also use this modifier to set the style for controls that acquire a
button style through composition, like the `Menu` and `Toggle` views in the
following example:

The `menuStyle(_:)` modifier causes the Terms and Conditions menu to render as
a button. Similarly, the `toggleStyle(_:)` modifier causes the two toggles to
render as buttons. The button style modifier then causes not only the explicit
Sign In `Button`, but also the menu and toggles with button styling, to render
with the bordered button style.

## See Also

### Creating buttons

`struct Button`

A control that initiates an action.

`func buttonStyle<S>(S) -> some View`

Sets the style for buttons within this view to a button style with a custom
appearance and custom interaction behavior.

`func buttonBorderShape(ButtonBorderShape) -> some View`

Sets the border shape for buttons in this view.

`func buttonRepeatBehavior(ButtonRepeatBehavior) -> some View`

Sets whether buttons in this view should repeatedly trigger their actions on
prolonged interactions.

`var buttonRepeatBehavior: ButtonRepeatBehavior`

Whether buttons with this associated environment should repeatedly trigger
their actions on prolonged interactions.

`struct ButtonBorderShape`

A shape that is used to draw a button’s border.

`struct ButtonRole`

A value that describes the purpose of a button.

`struct ButtonRepeatBehavior`

The options for controlling the repeatability of button actions.

Instance Method

# buttonStyle(_:)

Sets the style for buttons within this view to a button style with a custom
appearance and custom interaction behavior.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func buttonStyle<S>(_ style: S) -> some View where S : PrimitiveButtonStyle
    

## Discussion

Use this modifier to set a specific style for button instances within a view:

## See Also

### Creating buttons

`struct Button`

A control that initiates an action.

`func buttonStyle<S>(S) -> some View`

Sets the style for buttons within this view to a button style with a custom
appearance and standard interaction behavior.

`func buttonBorderShape(ButtonBorderShape) -> some View`

Sets the border shape for buttons in this view.

`func buttonRepeatBehavior(ButtonRepeatBehavior) -> some View`

Sets whether buttons in this view should repeatedly trigger their actions on
prolonged interactions.

`var buttonRepeatBehavior: ButtonRepeatBehavior`

Whether buttons with this associated environment should repeatedly trigger
their actions on prolonged interactions.

`struct ButtonBorderShape`

A shape that is used to draw a button’s border.

`struct ButtonRole`

A value that describes the purpose of a button.

`struct ButtonRepeatBehavior`

The options for controlling the repeatability of button actions.

Instance Method

# buttonBorderShape(_:)

Sets the border shape for buttons in this view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func buttonBorderShape(_ shape: ButtonBorderShape) -> some View
    

##  Parameters

`shape`

    

the shape to use.

## Discussion

The border shape is used to draw the platter for a bordered button. On macOS,
the specified border shape is only applied to bordered buttons in widgets.

## See Also

### Creating buttons

`struct Button`

A control that initiates an action.

`func buttonStyle<S>(S) -> some View`

Sets the style for buttons within this view to a button style with a custom
appearance and standard interaction behavior.

`func buttonStyle<S>(S) -> some View`

Sets the style for buttons within this view to a button style with a custom
appearance and custom interaction behavior.

`func buttonRepeatBehavior(ButtonRepeatBehavior) -> some View`

Sets whether buttons in this view should repeatedly trigger their actions on
prolonged interactions.

`var buttonRepeatBehavior: ButtonRepeatBehavior`

Whether buttons with this associated environment should repeatedly trigger
their actions on prolonged interactions.

`struct ButtonBorderShape`

A shape that is used to draw a button’s border.

`struct ButtonRole`

A value that describes the purpose of a button.

`struct ButtonRepeatBehavior`

The options for controlling the repeatability of button actions.

Instance Method

# buttonRepeatBehavior(_:)

Sets whether buttons in this view should repeatedly trigger their actions on
prolonged interactions.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func buttonRepeatBehavior(_ behavior: ButtonRepeatBehavior) -> some View
    

##  Parameters

`behavior`

    

A value of `enabled` means that buttons should enable repeating behavior and a
value of `disabled` means that buttons should disallow repeating behavior.

## Discussion

Apply this to buttons that increment or decrement a value or perform some
other inherently iterative operation. Interactions such as pressing-and-
holding on the button, holding the button’s keyboard shortcut, or holding down
the space key while the button is focused will trigger this repeat behavior.

This affects all system button styles, as well as automatically affects custom
`ButtonStyle` conforming types. This does not automatically apply to custom
`PrimitiveButtonStyle` conforming types, and the
`EnvironmentValues.buttonRepeatBehavior` value should be used to adjust their
custom gestures as appropriate.

## See Also

### Creating buttons

`struct Button`

A control that initiates an action.

`func buttonStyle<S>(S) -> some View`

Sets the style for buttons within this view to a button style with a custom
appearance and standard interaction behavior.

`func buttonStyle<S>(S) -> some View`

Sets the style for buttons within this view to a button style with a custom
appearance and custom interaction behavior.

`func buttonBorderShape(ButtonBorderShape) -> some View`

Sets the border shape for buttons in this view.

`var buttonRepeatBehavior: ButtonRepeatBehavior`

Whether buttons with this associated environment should repeatedly trigger
their actions on prolonged interactions.

`struct ButtonBorderShape`

A shape that is used to draw a button’s border.

`struct ButtonRole`

A value that describes the purpose of a button.

`struct ButtonRepeatBehavior`

The options for controlling the repeatability of button actions.

Instance Property

# buttonRepeatBehavior

Whether buttons with this associated environment should repeatedly trigger
their actions on prolonged interactions.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var buttonRepeatBehavior: ButtonRepeatBehavior { get }

## Discussion

A value of `enabled` means that buttons will be able to repeatedly trigger
their action, and `disabled` means they should not. A value of `automatic`
means that buttons will defer to default behavior.

## See Also

### Creating buttons

`struct Button`

A control that initiates an action.

`func buttonStyle<S>(S) -> some View`

Sets the style for buttons within this view to a button style with a custom
appearance and standard interaction behavior.

`func buttonStyle<S>(S) -> some View`

Sets the style for buttons within this view to a button style with a custom
appearance and custom interaction behavior.

`func buttonBorderShape(ButtonBorderShape) -> some View`

Sets the border shape for buttons in this view.

`func buttonRepeatBehavior(ButtonRepeatBehavior) -> some View`

Sets whether buttons in this view should repeatedly trigger their actions on
prolonged interactions.

`struct ButtonBorderShape`

A shape that is used to draw a button’s border.

`struct ButtonRole`

A value that describes the purpose of a button.

`struct ButtonRepeatBehavior`

The options for controlling the repeatability of button actions.

Structure

# ButtonBorderShape

A shape that is used to draw a button’s border.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    struct ButtonBorderShape

## Topics

### Getting border shapes

`static let automatic: ButtonBorderShape`

A shape that defers to the system to determine an appropriate shape for the
given context and platform.

`static let capsule: ButtonBorderShape`

A capsule shape.

`static let circle: ButtonBorderShape`

`static let roundedRectangle: ButtonBorderShape`

A rounded rectangle shape.

`static func roundedRectangle(radius: CGFloat) -> ButtonBorderShape`

A rounded rectangle shape.

## Relationships

### Conforms To

  * `Animatable`
  * `Equatable`
  * `InsettableShape`
  * `Sendable`
  * `Shape`
  * `View`

## See Also

### Creating buttons

`struct Button`

A control that initiates an action.

`func buttonStyle<S>(S) -> some View`

Sets the style for buttons within this view to a button style with a custom
appearance and standard interaction behavior.

`func buttonStyle<S>(S) -> some View`

Sets the style for buttons within this view to a button style with a custom
appearance and custom interaction behavior.

`func buttonBorderShape(ButtonBorderShape) -> some View`

Sets the border shape for buttons in this view.

`func buttonRepeatBehavior(ButtonRepeatBehavior) -> some View`

Sets whether buttons in this view should repeatedly trigger their actions on
prolonged interactions.

`var buttonRepeatBehavior: ButtonRepeatBehavior`

Whether buttons with this associated environment should repeatedly trigger
their actions on prolonged interactions.

`struct ButtonRole`

A value that describes the purpose of a button.

`struct ButtonRepeatBehavior`

The options for controlling the repeatability of button actions.

Structure

# ButtonRole

A value that describes the purpose of a button.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    struct ButtonRole

## Overview

A button role provides a description of a button’s purpose. For example, the
`destructive` role indicates that a button performs a destructive action, like
delete user data:

## Topics

### Getting button roles

`static let cancel: ButtonRole`

A role that indicates a button that cancels an operation.

`static let destructive: ButtonRole`

A role that indicates a destructive button.

## Relationships

### Conforms To

  * `Equatable`
  * `Sendable`

## See Also

### Creating buttons

`struct Button`

A control that initiates an action.

`func buttonStyle<S>(S) -> some View`

Sets the style for buttons within this view to a button style with a custom
appearance and standard interaction behavior.

`func buttonStyle<S>(S) -> some View`

Sets the style for buttons within this view to a button style with a custom
appearance and custom interaction behavior.

`func buttonBorderShape(ButtonBorderShape) -> some View`

Sets the border shape for buttons in this view.

`func buttonRepeatBehavior(ButtonRepeatBehavior) -> some View`

Sets whether buttons in this view should repeatedly trigger their actions on
prolonged interactions.

`var buttonRepeatBehavior: ButtonRepeatBehavior`

Whether buttons with this associated environment should repeatedly trigger
their actions on prolonged interactions.

`struct ButtonBorderShape`

A shape that is used to draw a button’s border.

`struct ButtonRepeatBehavior`

The options for controlling the repeatability of button actions.

Structure

# ButtonRepeatBehavior

The options for controlling the repeatability of button actions.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct ButtonRepeatBehavior

## Overview

Use values of this type with the `buttonRepeatBehavior(_:)` modifier.

## Topics

### Getting repeat behaviors

`static let automatic: ButtonRepeatBehavior`

The automatic repeat behavior.

`static let enabled: ButtonRepeatBehavior`

Repeating button actions will be enabled.

`static let disabled: ButtonRepeatBehavior`

Repeating button actions will be disabled.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Creating buttons

`struct Button`

A control that initiates an action.

`func buttonStyle<S>(S) -> some View`

Sets the style for buttons within this view to a button style with a custom
appearance and standard interaction behavior.

`func buttonStyle<S>(S) -> some View`

Sets the style for buttons within this view to a button style with a custom
appearance and custom interaction behavior.

`func buttonBorderShape(ButtonBorderShape) -> some View`

Sets the border shape for buttons in this view.

`func buttonRepeatBehavior(ButtonRepeatBehavior) -> some View`

Sets whether buttons in this view should repeatedly trigger their actions on
prolonged interactions.

`var buttonRepeatBehavior: ButtonRepeatBehavior`

Whether buttons with this associated environment should repeatedly trigger
their actions on prolonged interactions.

`struct ButtonBorderShape`

A shape that is used to draw a button’s border.

`struct ButtonRole`

A value that describes the purpose of a button.

Structure

# EditButton

A button that toggles the edit mode environment value.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  visionOS 1.0+

    
    
    struct EditButton

## Overview

An edit button toggles the environment’s `editMode` value for content within a
container that supports edit mode. In the following example, an edit button
placed inside a `NavigationView` supports editing of a `List`:

Because the `ForEach` in the above example defines behaviors for
`onDelete(perform:)` and `onMove(perform:)`, the editable list displays the
delete and move UI when the user taps Edit. Notice that the Edit button
displays the title “Done” while edit mode is active:

You can also create custom views that react to changes in the edit mode state,
as described in `EditMode`.

## Topics

### Creating an edit button

`init()`

Creates an Edit button instance.

## Relationships

### Conforms To

  * `View`

## See Also

### Creating special-purpose buttons

`struct PasteButton`

A system button that reads items from the pasteboard and delivers it to a
closure.

`struct RenameButton`

A button that triggers a standard rename action.

Structure

# PasteButton

A system button that reads items from the pasteboard and delivers it to a
closure.

iOS 16.0+  iPadOS 16.0+  macOS 10.15+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    @MainActor
    struct PasteButton

## Overview

Use a paste button when you want to provide a button for pasting items from
the system pasteboard into your app. The system provides a button appearance
and label appropriate to the current environment. However, you can use view
modifiers like `buttonBorderShape(_:)`, `labelStyle(_:)`, and `tint(_:)` to
customize the button in some contexts.

You declare what type of items your app will accept; use a type that conforms
to the `Transferable` protocol. When the user taps or clicks the button, your
closure receives the pasteboard items in the specified type.

In the following example, a paste button declares that it accepts a string.
When the user taps or clicks the button, the sample’s closure receives an
array of strings and sets the first as the value of `pastedText`, which
updates a nearby `Text` view.

A paste button automatically validates and invalidates based on changes to the
pasteboard on iOS, but not on macOS.

## Topics

### Creating a paste button

`init(supportedContentTypes: [UTType], payloadAction: ([NSItemProvider]) ->
Void)`

Creates a Paste button that accepts specific types of data from the
pasteboard.

`init<T>(payloadType: T.Type, onPaste: ([T]) -> Void)`

Creates an instance that accepts values of the specified type.

### Deprecated initializers

`init(supportedTypes: [String], payloadAction: ([NSItemProvider]) -> Void)`

Creates a Paste button that accepts specific types of data from the
pasteboard.

Deprecated

`init<Payload>(supportedTypes: [String], validator: ([NSItemProvider]) ->
Payload?, payloadAction: (Payload) -> Void)`

Creates a Paste button that accepts specific types of data from the
pasteboard, performing a custom validation of the data before sending it to
your app.

Deprecated

`init<Payload>(supportedContentTypes: [UTType], validator: ([NSItemProvider])
-> Payload?, payloadAction: (Payload) -> Void)`

Creates a Paste button that accepts specific types of data from the
pasteboard, performing a custom validation of the data before sending it to
your app.

Deprecated

## Relationships

### Conforms To

  * `View`

## See Also

### Creating special-purpose buttons

`struct EditButton`

A button that toggles the edit mode environment value.

`struct RenameButton`

A button that triggers a standard rename action.

Structure

# RenameButton

A button that triggers a standard rename action.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    struct RenameButton<Label> where Label : View

## Overview

A rename button receives its action from the environment. Use the
`renameAction(_:)` modifier to set the action. The system disables the button
if you don’t define an action.

When someone taps the rename button in the context menu, the rename action
focuses the text field by setting the `isFocused` property to true.

You can use this button inside of a navigation title menu and the navigation
title modifier automatically configures the environment with the appropriate
rename action.

## Topics

### Creating an rename button

`init()`

Creates a rename button.

## Relationships

### Conforms To

  * `View`

## See Also

### Creating special-purpose buttons

`struct EditButton`

A button that toggles the edit mode environment value.

`struct PasteButton`

A system button that reads items from the pasteboard and delivers it to a
closure.

Structure

# Link

A control for navigating to a URL.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    struct Link<Label> where Label : View

## Overview

Create a link by providing a destination URL and a title. The title tells the
user the purpose of the link, and can be a string, a title key that produces a
localized string, or a view that acts as a label. The example below creates a
link to `example.com` and displays the title string as a link-styled view:

When a user taps or clicks a `Link`, the default behavior depends on the
contents of the URL. For example, SwiftUI opens a Universal Link in the
associated app if possible, or in the user’s default web browser if not.
Alternatively, you can override the default behavior by setting the `openURL`
environment value with a custom `OpenURLAction`:

As with other views, you can style links using standard view modifiers
depending on the view type of the link’s label. For example, a `Text` label
could be modified with a custom `font(_:)` or `foregroundColor(_:)` to
customize the appearance of the link in your app’s UI.

## Topics

### Creating a link

`init(LocalizedStringKey, destination: URL)`

Creates a control, consisting of a URL and a title key, used to navigate to a
URL.

Available when `Label` is `Text`.

`init<S>(S, destination: URL)`

Creates a control, consisting of a URL and a title string, used to navigate to
a URL.

Available when `Label` is `Text`.

`init(destination: URL, label: () -> Label)`

Creates a control, consisting of a URL and a label, used to navigate to the
given URL.

## Relationships

### Conforms To

  * `View`

## See Also

### Linking to other content

`struct ShareLink`

A view that controls a sharing presentation.

`struct SharePreview`

A representation of a type to display in a share preview.

`struct TextFieldLink`

A control that requests text input from the user when pressed.

`struct HelpLink`

A button with a standard appearance that opens app-specific help
documentation.

Structure

# ShareLink

A view that controls a sharing presentation.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    struct ShareLink<Data, PreviewImage, PreviewIcon, Label> where Data : RandomAccessCollection, PreviewImage : Transferable, PreviewIcon : Transferable, Label : View, Data.Element : Transferable

## Overview

People tap or click on a share link to present a share interface. The link
typically uses a system-standard appearance; you only need to supply the
content to share:

You can control the appearance of the link by providing view content. For
example, you can use a `Label` to display a link with a custom icon:

If you only wish to customize the link’s title, you can use one of the
convenience initializers that takes a string and creates a `Label` for you:

The link can share any content that is `Transferable`. Many framework types,
like `URL`, already conform to this protocol. You can also make your own types
transferable.

For example, you can use `ProxyRepresentation` to resolve your own type to a
framework type:

Sometimes the content that your app shares isn’t immediately available. You
can use `FileRepresentation` or `DataRepresentation` when you need an
asynchronous operation, like a network request, to retrieve and prepare the
content.

A `Transferable` type also lets you provide multiple content types for a
single shareable item. The share interface shows relevant sharing services
based on the types that you provide.

The previous example also shows how you provide a preview of your content to
show in the share interface.

A preview isn’t required when sharing URLs or non-attributed strings. When
sharing these types of content, the system can automatically determine a
preview.

You can provide a preview even when it’s optional. For instance, when sharing
URLs, the automatic preview first shows a placeholder link icon alongside the
base URL while fetching the link’s metadata over the network. The preview
updates once the link’s icon and title become available. If you provide a
preview instead, the preview appears immediately without fetching data over
the network.

Some share activities support subject and message fields. You can pre-populate
these fields with the `subject` and `message` parameters:

## Topics

### Sharing an item

`init(item: String, subject: Text?, message: Text?)`

Creates an instance that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` conforms to `Transferable`.

`init(item: URL, subject: Text?, message: Text?)`

Creates an instance that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` conforms to `Transferable`.

`init(item: String, subject: Text?, message: Text?, label: () -> Label)`

Creates an instance that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` conforms to `View`, and
`Data.Element` conforms to `Transferable`.

`init(item: URL, subject: Text?, message: Text?, label: () -> Label)`

Creates an instance that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` conforms to `View`, and
`Data.Element` conforms to `Transferable`.

### Sharing an item with a preview

`init<I>(item: I, subject: Text?, message: Text?, preview:
SharePreview<PreviewImage, PreviewIcon>)`

Creates an instance that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage`
conforms to `Transferable`, `PreviewIcon` conforms to `Transferable`, `Label`
is `DefaultShareLinkLabel`, and `Data.Element` conforms to `Transferable`.

`init<I>(item: I, subject: Text?, message: Text?, preview:
SharePreview<PreviewImage, PreviewIcon>, label: () -> Label)`

Creates an instance that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage`
conforms to `Transferable`, `PreviewIcon` conforms to `Transferable`, `Label`
conforms to `View`, and `Data.Element` conforms to `Transferable`.

### Sharing an item with a label

`init<S>(S, item: URL, subject: Text?, message: Text?)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` conforms to `Transferable`.

`init(LocalizedStringKey, item: URL, subject: Text?, message: Text?)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` conforms to `Transferable`.

`init(Text, item: String, subject: Text?, message: Text?)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` conforms to `Transferable`.

`init<S>(S, item: String, subject: Text?, message: Text?)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` conforms to `Transferable`.

`init(LocalizedStringKey, item: String, subject: Text?, message: Text?)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` conforms to `Transferable`.

`init(Text, item: URL, subject: Text?, message: Text?)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` conforms to `Transferable`.

### Sharing an item with a label and a preview

`init<S, I>(S, item: I, subject: Text?, message: Text?, preview:
SharePreview<PreviewImage, PreviewIcon>)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage`
conforms to `Transferable`, `PreviewIcon` conforms to `Transferable`, `Label`
is `DefaultShareLinkLabel`, and `Data.Element` conforms to `Transferable`.

`init<I>(Text, item: I, subject: Text?, message: Text?, preview:
SharePreview<PreviewImage, PreviewIcon>)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage`
conforms to `Transferable`, `PreviewIcon` conforms to `Transferable`, `Label`
is `DefaultShareLinkLabel`, and `Data.Element` conforms to `Transferable`.

`init<I>(LocalizedStringKey, item: I, subject: Text?, message: Text?, preview:
SharePreview<PreviewImage, PreviewIcon>)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage`
conforms to `Transferable`, `PreviewIcon` conforms to `Transferable`, `Label`
is `DefaultShareLinkLabel`, and `Data.Element` conforms to `Transferable`.

### Sharing items

`init(items: Data, subject: Text?, message: Text?)`

Creates an instance that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` is `String`.

`init(items: Data, subject: Text?, message: Text?)`

Creates an instance that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` is `URL`.

`init(items: Data, subject: Text?, message: Text?, label: () -> Label)`

Creates an instance that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` conforms to `View`, and
`Data.Element` is `String`.

`init(items: Data, subject: Text?, message: Text?, label: () -> Label)`

Creates an instance that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` conforms to `View`, and
`Data.Element` is `URL`.

### Sharing items with a preview

`init(items: Data, subject: Text?, message: Text?, preview: (Data.Element) ->
SharePreview<PreviewImage, PreviewIcon>)`

Creates an instance that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage`
conforms to `Transferable`, `PreviewIcon` conforms to `Transferable`, `Label`
is `DefaultShareLinkLabel`, and `Data.Element` conforms to `Transferable`.

`init(items: Data, subject: Text?, message: Text?, preview: (Data.Element) ->
SharePreview<PreviewImage, PreviewIcon>, label: () -> Label)`

Creates an instance that presents the share interface.

### Sharing items with a label

`init<S>(S, items: Data, subject: Text?, message: Text?)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` is `String`.

`init<S>(S, items: Data, subject: Text?, message: Text?)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` is `URL`.

`init(LocalizedStringKey, items: Data, subject: Text?, message: Text?)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` is `String`.

`init(LocalizedStringKey, items: Data, subject: Text?, message: Text?)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` is `URL`.

`init(Text, items: Data, subject: Text?, message: Text?)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` is `URL`.

`init(Text, items: Data, subject: Text?, message: Text?)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is
`Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and
`Data.Element` is `String`.

### Sharing items with a label and preview

`init<S>(S, items: Data, subject: Text?, message: Text?, preview:
(Data.Element) -> SharePreview<PreviewImage, PreviewIcon>)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage`
conforms to `Transferable`, `PreviewIcon` conforms to `Transferable`, `Label`
is `DefaultShareLinkLabel`, and `Data.Element` conforms to `Transferable`.

`init(LocalizedStringKey, items: Data, subject: Text?, message: Text?,
preview: (Data.Element) -> SharePreview<PreviewImage, PreviewIcon>)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage`
conforms to `Transferable`, `PreviewIcon` conforms to `Transferable`, `Label`
is `DefaultShareLinkLabel`, and `Data.Element` conforms to `Transferable`.

`init(Text, items: Data, subject: Text?, message: Text?, preview:
(Data.Element) -> SharePreview<PreviewImage, PreviewIcon>)`

Creates an instance, with a custom label, that presents the share interface.

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage`
conforms to `Transferable`, `PreviewIcon` conforms to `Transferable`, `Label`
is `DefaultShareLinkLabel`, and `Data.Element` conforms to `Transferable`.

### Supporting types

`struct DefaultShareLinkLabel`

The default label used for a share link.

## Relationships

### Conforms To

  * `View`

## See Also

### Linking to other content

`struct Link`

A control for navigating to a URL.

`struct SharePreview`

A representation of a type to display in a share preview.

`struct TextFieldLink`

A control that requests text input from the user when pressed.

`struct HelpLink`

A button with a standard appearance that opens app-specific help
documentation.

Structure

# SharePreview

A representation of a type to display in a share preview.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    struct SharePreview<Image, Icon> where Image : Transferable, Icon : Transferable

## Overview

Use this type when sharing content that the system can’t preview
automatically:

You can also provide a preview to speed up the sharing process. In the
following example the preview appears immediately; if you omit the preview
instead, the system fetches the link’s metadata over the network:

You can provide unique previews for each item in a collection of items that a
`ShareLink` links to:

The share interface decides how to combine those previews.

Each preview specifies text and images that describe an item of the type. The
preview’s `image` parameter is typically a full-size representation of the
item. For instance, if the system prepares a preview for a link to a webpage,
the image might be the hero image on that webpage.

The preview’s `icon` parameter is typically a thumbnail-sized representation
of the source of the item. For instance, if the system prepares a preview for
a link to a webpage, the icon might be an image that represents the website
overall.

The system may reuse a single preview representation for multiple previews,
and show different images in each context. For more information and
recommended sizes for each image, see TN2444: Best Practices for Link Previews
in Messages.

## Topics

### Displaying a preview

`init<S>(S)`

Creates a preview representation.

Available when `Image` is `Never` and `Icon` is `Never`.

`init(LocalizedStringKey)`

Creates a preview representation.

Available when `Image` is `Never` and `Icon` is `Never`.

`init(Text)`

Creates a preview representation.

Available when `Image` is `Never` and `Icon` is `Never`.

### Displaying a preview with an image

`init<S>(S, image: Image)`

Creates a preview representation.

Available when `Image` conforms to `Transferable` and `Icon` is `Never`.

`init(LocalizedStringKey, image: Image)`

Creates a preview representation.

Available when `Image` conforms to `Transferable` and `Icon` is `Never`.

`init(Text, image: Image)`

Creates a preview representation.

Available when `Image` conforms to `Transferable` and `Icon` is `Never`.

### Displaying a preview with an icon

`init<S>(S, icon: Icon)`

Creates a preview representation.

Available when `Image` is `Never` and `Icon` conforms to `Transferable`.

`init(LocalizedStringKey, icon: Icon)`

Creates a preview representation.

Available when `Image` is `Never` and `Icon` conforms to `Transferable`.

`init(Text, icon: Icon)`

Creates a preview representation.

Available when `Image` is `Never` and `Icon` conforms to `Transferable`.

### Displaying a preview with an image and an icon

`init<S>(S, image: Image, icon: Icon)`

Creates a preview representation.

`init(LocalizedStringKey, image: Image, icon: Icon)`

Creates a preview representation.

`init(Text, image: Image, icon: Icon)`

Creates a preview representation.

## See Also

### Linking to other content

`struct Link`

A control for navigating to a URL.

`struct ShareLink`

A view that controls a sharing presentation.

`struct TextFieldLink`

A control that requests text input from the user when pressed.

`struct HelpLink`

A button with a standard appearance that opens app-specific help
documentation.

Structure

# TextFieldLink

A control that requests text input from the user when pressed.

watchOS 9.0+

    
    
    struct TextFieldLink<Label> where Label : View

## Overview

A `TextFieldLink` should be used to request text input from the user through a
button interface.

## Topics

### Creating a text field link

`init(LocalizedStringKey, prompt: Text?, onSubmit: (String) -> Void)`

Creates a TextFieldLink which when pressed will request text input from the
user.

Available when `Label` is `Text`.

`init<S>(S, prompt: Text?, onSubmit: (String) -> Void)`

Creates a TextFieldLink which when pressed will request text input from the
user.

Available when `Label` is `Text`.

`init(prompt: Text?, label: () -> Label, onSubmit: (String) -> Void)`

Creates a TextFieldLink which when pressed will request text input from the
user.

Available when `Label` conforms to `View`.

## Relationships

### Conforms To

  * `View`

## See Also

### Linking to other content

`struct Link`

A control for navigating to a URL.

`struct ShareLink`

A view that controls a sharing presentation.

`struct SharePreview`

A representation of a type to display in a share preview.

`struct HelpLink`

A button with a standard appearance that opens app-specific help
documentation.

Structure

# HelpLink

A button with a standard appearance that opens app-specific help
documentation.

macOS 14.0+  visionOS 1.0+

    
    
    struct HelpLink

## Overview

A help link opens documentation relevant to the context where they are used.
Typically this is by opening to an anchor in an Apple Help book, but can also
perform an arbitrary action such as opening a URL or opening a window.

Help links have a standard appearance, as well as conventional placement
within a view. When used within an alert or confirmation dialog’s actions, the
help link will automatically be placed in the top trailing corner. Or when
used in a sheet toolbar, the help link is automatically placed in the lower
leading corner.

## Topics

### Creating a help link

`init(action: () -> Void)`

Constructs a new help link with the specified action.

`init(destination: URL)`

Constructs a new help link that opens the specified destination URL.

`init(anchor: NSHelpManager.AnchorName)`

Constructs a new help link with the specified anchor in the main app bundle’s
book.

`init(anchor: NSHelpManager.AnchorName, book: NSHelpManager.BookName)`

Constructs a new help link with the specified anchor and book.

## Relationships

### Conforms To

  * `View`

## See Also

### Linking to other content

`struct Link`

A control for navigating to a URL.

`struct ShareLink`

A view that controls a sharing presentation.

`struct SharePreview`

A representation of a type to display in a share preview.

`struct TextFieldLink`

A control that requests text input from the user when pressed.

Structure

# Slider

A control for selecting a value from a bounded linear range of values.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    struct Slider<Label, ValueLabel> where Label : View, ValueLabel : View

## Overview

A slider consists of a “thumb” image that the user moves between two extremes
of a linear “track”. The ends of the track represent the minimum and maximum
possible values. As the user moves the thumb, the slider updates its bound
value.

The following example shows a slider bound to the value `speed`. As the slider
updates this value, a bound `Text` view shows the value updating. The
`onEditingChanged` closure passed to the slider receives callbacks when the
user drags the slider. The example uses this to change the color of the value
text.

You can also use a `step` parameter to provide incremental steps along the
path of the slider. For example, if you have a slider with a range of `0` to
`100`, and you set the `step` value to `5`, the slider’s increments would be
`0`, `5`, `10`, and so on. The following example shows this approach, and also
adds optional minimum and maximum value labels.

The slider also uses the `step` to increase or decrease the value when a
VoiceOver user adjusts the slider with voice commands.

## Topics

### Creating a slider

`init<V>(value: Binding<V>, in: ClosedRange<V>, onEditingChanged: (Bool) ->
Void)`

Creates a slider to select a value from a given range.

Available when `Label` is `EmptyView` and `ValueLabel` is `EmptyView`.

`init<V>(value: Binding<V>, in: ClosedRange<V>, step: V.Stride,
onEditingChanged: (Bool) -> Void)`

Creates a slider to select a value from a given range, subject to a step
increment.

Available when `Label` is `EmptyView` and `ValueLabel` is `EmptyView`.

### Creating a slider with labels

`init<V>(value: Binding<V>, in: ClosedRange<V>, label: () -> Label,
onEditingChanged: (Bool) -> Void)`

Creates a slider to select a value from a given range, which displays the
provided label.

Available when `Label` conforms to `View` and `ValueLabel` is `EmptyView`.

`init<V>(value: Binding<V>, in: ClosedRange<V>, step: V.Stride, label: () ->
Label, onEditingChanged: (Bool) -> Void)`

Creates a slider to select a value from a given range, subject to a step
increment, which displays the provided label.

Available when `Label` conforms to `View` and `ValueLabel` is `EmptyView`.

`init<V>(value: Binding<V>, in: ClosedRange<V>, label: () -> Label,
minimumValueLabel: () -> ValueLabel, maximumValueLabel: () -> ValueLabel,
onEditingChanged: (Bool) -> Void)`

Creates a slider to select a value from a given range, which displays the
provided labels.

Available when `Label` conforms to `View` and `ValueLabel` conforms to `View`.

`init<V>(value: Binding<V>, in: ClosedRange<V>, step: V.Stride, label: () ->
Label, minimumValueLabel: () -> ValueLabel, maximumValueLabel: () ->
ValueLabel, onEditingChanged: (Bool) -> Void)`

Creates a slider to select a value from a given range, subject to a step
increment, which displays the provided labels.

Available when `Label` conforms to `View` and `ValueLabel` conforms to `View`.

### Deprecated initializers

`init<V>(value: Binding<V>, in: ClosedRange<V>, onEditingChanged: (Bool) ->
Void, label: () -> Label)`

Creates a slider to select a value from a given range, which displays the
provided label.

Available when `Label` conforms to `View` and `ValueLabel` is `EmptyView`.

Deprecated

`init<V>(value: Binding<V>, in: ClosedRange<V>, step: V.Stride,
onEditingChanged: (Bool) -> Void, label: () -> Label)`

Creates a slider to select a value from a given range, subject to a step
increment, which displays the provided label.

Available when `Label` conforms to `View` and `ValueLabel` is `EmptyView`.

Deprecated

`init<V>(value: Binding<V>, in: ClosedRange<V>, onEditingChanged: (Bool) ->
Void, minimumValueLabel: ValueLabel, maximumValueLabel: ValueLabel, label: ()
-> Label)`

Creates a slider to select a value from a given range, which displays the
provided labels.

Available when `Label` conforms to `View` and `ValueLabel` conforms to `View`.

Deprecated

`init<V>(value: Binding<V>, in: ClosedRange<V>, step: V.Stride,
onEditingChanged: (Bool) -> Void, minimumValueLabel: ValueLabel,
maximumValueLabel: ValueLabel, label: () -> Label)`

Creates a slider to select a value from a given range, subject to a step
increment, which displays the provided labels.

Available when `Label` conforms to `View` and `ValueLabel` conforms to `View`.

Deprecated

## Relationships

### Conforms To

  * `View`

## See Also

### Getting numeric inputs

`struct Stepper`

A control that performs increment and decrement actions.

`struct Toggle`

A control that toggles between on and off states.

`func toggleStyle<S>(S) -> some View`

Sets the style for toggles in a view hierarchy.

Structure

# Stepper

A control that performs increment and decrement actions.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 9.0+
visionOS 1.0+

    
    
    struct Stepper<Label> where Label : View

## Overview

Use a stepper control when you want the user to have granular control while
incrementing or decrementing a value. For example, you can use a stepper to:

  * Change a value up or down by `1`.

  * Operate strictly over a prescribed range.

  * Step by specific amounts over a stepper’s range of possible values.

The example below uses an array that holds a number of `Color` values, a local
state variable, `value`, to set the control’s background color, and title
label. When the user clicks or taps the stepper’s increment or decrement
buttons, SwiftUI executes the relevant closure that updates `value`, wrapping
the `value` to prevent overflow. SwiftUI then re-renders the view, updating
the text and background color to match the current index:

The following example shows a stepper that displays the effect of incrementing
or decrementing a value with the step size of `step` with the bounds defined
by `range`:

## Topics

### Creating a stepper

`init<V>(value: Binding<V>, step: V.Stride, label: () -> Label,
onEditingChanged: (Bool) -> Void)`

Creates a stepper configured to increment or decrement a binding to a value
using a step value you provide.

Available when `Label` conforms to `View`.

`init<F>(value: Binding<F.FormatInput>, step: F.FormatInput.Stride, format: F,
label: () -> Label, onEditingChanged: (Bool) -> Void)`

Creates a stepper configured to increment or decrement a binding to a value
using a step value you provide, displaying its value with an applied format
style.

Available when `Label` conforms to `View`.

`init<V>(LocalizedStringKey, value: Binding<V>, step: V.Stride,
onEditingChanged: (Bool) -> Void)`

Creates a stepper with a title key and configured to increment and decrement a
binding to a value and step amount you provide.

Available when `Label` is `Text`.

`init<S, V>(S, value: Binding<V>, step: V.Stride, onEditingChanged: (Bool) ->
Void)`

Creates a stepper with a title and configured to increment and decrement a
binding to a value and step amount you provide.

Available when `Label` is `Text`.

`init<S, F>(S, value: Binding<F.FormatInput>, step: F.FormatInput.Stride,
format: F, onEditingChanged: (Bool) -> Void)`

Creates a stepper with a title and configured to increment and decrement a
binding to a value and step amount you provide, displaying its value with an
applied format style.

Available when `Label` is `Text`.

`init<F>(LocalizedStringKey, value: Binding<F.FormatInput>, step:
F.FormatInput.Stride, format: F, onEditingChanged: (Bool) -> Void)`

Creates a stepper with a title key and configured to increment and decrement a
binding to a value and step amount you provide, displaying its value with an
applied format style.

Available when `Label` is `Text`.

### Creating a stepper over a range

`init<V>(value: Binding<V>, in: ClosedRange<V>, step: V.Stride, label: () ->
Label, onEditingChanged: (Bool) -> Void)`

Creates a stepper configured to increment or decrement a binding to a value
using a step value and within a range of values you provide.

Available when `Label` conforms to `View`.

`init<F>(value: Binding<F.FormatInput>, in: ClosedRange<F.FormatInput>, step:
F.FormatInput.Stride, format: F, label: () -> Label, onEditingChanged: (Bool)
-> Void)`

Creates a stepper configured to increment or decrement a binding to a value
using a step value and within a range of values you provide, displaying its
value with an applied format style.

Available when `Label` conforms to `View`.

`init<V>(LocalizedStringKey, value: Binding<V>, in: ClosedRange<V>, step:
V.Stride, onEditingChanged: (Bool) -> Void)`

Creates a stepper instance that increments and decrements a binding to a
value, by a step size and within a closed range that you provide.

Available when `Label` is `Text`.

`init<S, V>(S, value: Binding<V>, in: ClosedRange<V>, step: V.Stride,
onEditingChanged: (Bool) -> Void)`

Creates a stepper instance that increments and decrements a binding to a
value, by a step size and within a closed range that you provide.

Available when `Label` is `Text`.

`init<F>(LocalizedStringKey, value: Binding<F.FormatInput>, in:
ClosedRange<F.FormatInput>, step: F.FormatInput.Stride, format: F,
onEditingChanged: (Bool) -> Void)`

Creates a stepper instance that increments and decrements a binding to a
value, by a step size and within a closed range that you provide, displaying
its value with an applied format style.

Available when `Label` is `Text`.

`init<S, F>(S, value: Binding<F.FormatInput>, in: ClosedRange<F.FormatInput>,
step: F.FormatInput.Stride, format: F, onEditingChanged: (Bool) -> Void)`

Creates a stepper instance that increments and decrements a binding to a
value, by a step size and within a closed range that you provide, displaying
its value with an applied format style.

Available when `Label` is `Text`.

### Creating a stepper with change behavior

`init(label: () -> Label, onIncrement: (() -> Void)?, onDecrement: (() ->
Void)?, onEditingChanged: (Bool) -> Void)`

Creates a stepper instance that performs the closures you provide when the
user increments or decrements the stepper.

`init(LocalizedStringKey, onIncrement: (() -> Void)?, onDecrement: (() ->
Void)?, onEditingChanged: (Bool) -> Void)`

Creates a stepper that uses a title key and executes the closures you provide
when the user clicks or taps the stepper’s increment and decrement buttons.

Available when `Label` is `Text`.

`init<S>(S, onIncrement: (() -> Void)?, onDecrement: (() -> Void)?,
onEditingChanged: (Bool) -> Void)`

Creates a stepper using a title string and that executes closures you provide
when the user clicks or taps the stepper’s increment or decrement buttons.

Available when `Label` is `Text`.

### Deprecated initializers

`init<V>(value: Binding<V>, step: V.Stride, onEditingChanged: (Bool) -> Void,
label: () -> Label)`

Creates a stepper configured to increment or decrement a binding to a value
using a step value you provide.

Available when `Label` conforms to `View`.

Deprecated

`init<V>(value: Binding<V>, in: ClosedRange<V>, step: V.Stride,
onEditingChanged: (Bool) -> Void, label: () -> Label)`

Creates a stepper configured to increment or decrement a binding to a value
using a step value and within a range of values you provide.

Available when `Label` conforms to `View`.

Deprecated

`init(onIncrement: (() -> Void)?, onDecrement: (() -> Void)?,
onEditingChanged: (Bool) -> Void, label: () -> Label)`

Creates a stepper instance that performs the closures you provide when the
user increments or decrements the stepper.

Available when `Label` conforms to `View`.

Deprecated

## Relationships

### Conforms To

  * `View`

## See Also

### Getting numeric inputs

`struct Slider`

A control for selecting a value from a bounded linear range of values.

`struct Toggle`

A control that toggles between on and off states.

`func toggleStyle<S>(S) -> some View`

Sets the style for toggles in a view hierarchy.

Structure

# Toggle

A control that toggles between on and off states.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    struct Toggle<Label> where Label : View

## Overview

You create a toggle by providing an `isOn` binding and a label. Bind `isOn` to
a Boolean property that determines whether the toggle is on or off. Set the
label to a view that visually describes the purpose of switching between
toggle states. For example:

For the common case of `Label` based labels, you can use the convenience
initializer that takes a title string (or localized string key) and the name
of a system image:

For text-only labels, you can use the convenience initializer that takes a
title string (or localized string key) as its first parameter, instead of a
trailing closure:

### Styling toggles

Toggles use a default style that varies based on both the platform and the
context. For more information, read about the `automatic` toggle style.

You can customize the appearance and interaction of toggles by applying styles
using the `toggleStyle(_:)` modifier. You can apply built-in styles, like
`switch`, to either a toggle, or to a view hierarchy that contains toggles:

You can also define custom styles by creating a type that conforms to the
`ToggleStyle` protocol.

## Topics

### Creating a toggle

`init(isOn: Binding<Bool>, label: () -> Label)`

Creates a toggle that displays a custom label.

`init(LocalizedStringKey, isOn: Binding<Bool>)`

Creates a toggle that generates its label from a localized string key.

Available when `Label` is `Text`.

`init<S>(S, isOn: Binding<Bool>)`

Creates a toggle that generates its label from a string.

Available when `Label` is `Text`.

### Creating a toggle for a collection

`init<C>(sources: C, isOn: KeyPath<C.Element, Binding<Bool>>, label: () ->
Label)`

Creates a toggle representing a collection of values with a custom label.

`init<S, C>(S, sources: C, isOn: KeyPath<C.Element, Binding<Bool>>)`

Creates a toggle representing a collection of values that generates its label
from a string.

Available when `Label` is `Text`.

`init<C>(LocalizedStringKey, sources: C, isOn: KeyPath<C.Element,
Binding<Bool>>)`

Creates a toggle representing a collection of values that generates its label
from a localized string key.

Available when `Label` is `Text`.

### Creating a toggle with an image resource label

`init(LocalizedStringKey, image: ImageResource, isOn: Binding<Bool>)`

Creates a toggle that generates its label from a localized string key and
image resource.

Available when `Label` is `Label<Text, Image>`.

`init<S>(S, image: ImageResource, isOn: Binding<Bool>)`

Creates a toggle that generates its label from a string and image resource.

Available when `Label` is `Label<Text, Image>`.

`init<C>(LocalizedStringKey, image: ImageResource, sources: C, isOn:
KeyPath<C.Element, Binding<Bool>>)`

Creates a toggle representing a collection of values that generates its label
from a localized string key and image resource.

Available when `Label` is `Label<Text, Image>`.

`init<S, C>(S, image: ImageResource, sources: C, isOn: KeyPath<C.Element,
Binding<Bool>>)`

Creates a toggle representing a collection of values that generates its label
from a string and image resource.

Available when `Label` is `Label<Text, Image>`.

### Creating a toggle with an system image

`init(LocalizedStringKey, systemImage: String, isOn: Binding<Bool>)`

Creates a toggle that generates its label from a localized string key and
system image.

Available when `Label` is `Label<Text, Image>`.

`init<S>(S, systemImage: String, isOn: Binding<Bool>)`

Creates a toggle that generates its label from a string and system image.

Available when `Label` is `Label<Text, Image>`.

`init<C>(LocalizedStringKey, systemImage: String, sources: C, isOn:
KeyPath<C.Element, Binding<Bool>>)`

Creates a toggle representing a collection of values that generates its label
from a localized string key and system image.

Available when `Label` is `Label<Text, Image>`.

`init<S, C>(S, systemImage: String, sources: C, isOn: KeyPath<C.Element,
Binding<Bool>>)`

Creates a toggle representing a collection of values that generates its label
from a string.

Available when `Label` is `Label<Text, Image>`.

### Creating a toggle from a configuration

`init(ToggleStyleConfiguration)`

Creates a toggle based on a toggle style configuration.

Available when `Label` is `ToggleStyleConfiguration.Label`.

### Creating a toggle for an App Intent

`init<I>(isOn: Bool, intent: I, label: () -> Label)`

Creates a toggle performing an `AppIntent`.

Available when `Label` conforms to `View`.

`init(LocalizedStringKey, isOn: Bool, intent: some AppIntent)`

Creates a toggle performing an `AppIntent` and generates its label from a
localized string key.

Available when `Label` is `Text`.

`init<S>(S, isOn: Bool, intent: some AppIntent)`

Creates a toggle that generates its label from a string.

Available when `Label` is `Text`.

## Relationships

### Conforms To

  * `View`

## See Also

### Getting numeric inputs

`struct Slider`

A control for selecting a value from a bounded linear range of values.

`struct Stepper`

A control that performs increment and decrement actions.

`func toggleStyle<S>(S) -> some View`

Sets the style for toggles in a view hierarchy.

Instance Method

# toggleStyle(_:)

Sets the style for toggles in a view hierarchy.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func toggleStyle<S>(_ style: S) -> some View where S : ToggleStyle
    

##  Parameters

`style`

    

The toggle style to set. Use one of the built-in values, like `switch` or
`button`, or a custom style that you define by creating a type that conforms
to the `ToggleStyle` protocol.

## Return Value

A view that uses the specified toggle style for itself and its child views.

## Discussion

Use this modifier on a `Toggle` instance to set a style that defines the
control’s appearance and behavior. For example, you can choose the `switch`
style:

Built-in styles typically have a similar appearance across platforms, tailored
to the platform’s overall style:

Platform| Appearance  
---|---  
iOS, iPadOS|  
macOS|  
  
### Styling toggles in a hierarchy

You can set a style for all toggle instances within a view hierarchy by
applying the style modifier to a container view. For example, you can apply
the `button` style to an `HStack`:

The example above has the following appearance when `isFlagged` is `true` and
`isMuted` is `false`:

Platform| Appearance  
---|---  
iOS, iPadOS|  
macOS|  
  
### Automatic styling

If you don’t set a style, SwiftUI assumes a value of `automatic`, which
corresponds to a context-specific default. Specify the automatic style
explicitly to override a container’s style and revert to the default:

The style that SwiftUI uses as the default depends on both the platform and
the context. In macOS, the default in most contexts is a `checkbox`, while in
iOS, the default toggle style is a `switch`:

Platform| Appearance  
---|---  
iOS, iPadOS|  
macOS|  
  
Note

Like toggle style does for toggles, the `labelStyle(_:)` modifier sets the
style for `Label` instances in the hierarchy. The example above demostrates
the compact `iconOnly` style, which is useful for button toggles in space-
constrained contexts. Always include a descriptive title for better
accessibility.

For more information about how SwiftUI chooses a default toggle style, see the
`automatic` style.

## See Also

### Getting numeric inputs

`struct Slider`

A control for selecting a value from a bounded linear range of values.

`struct Stepper`

A control that performs increment and decrement actions.

`struct Toggle`

A control that toggles between on and off states.

Structure

# Picker

A control for selecting from a set of mutually exclusive values.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    struct Picker<Label, SelectionValue, Content> where Label : View, SelectionValue : Hashable, Content : View

## Overview

You create a picker by providing a selection binding, a label, and the content
for the picker to display. Set the `selection` parameter to a bound property
that provides the value to display as the current selection. Set the label to
a view that visually describes the purpose of selecting content in the picker,
and then provide the content for the picker to display.

For example, consider an enumeration of ice cream flavors and a `State`
variable to hold the selected flavor:

You can create a picker to select among the values by providing a label, a
binding to the current selection, and a collection of views for the picker’s
content. Append a tag to each of these content views using the `tag(_:)` view
modifier so that the type of each selection matches the type of the bound
state variable:

If you provide a string label for the picker, as the example above does, the
picker uses it to initialize a `Text` view as a label. Alternatively, you can
use the `init(selection:content:label:)` initializer to compose the label from
other views. The exact appearance of the picker depends on the context. If you
use a picker in a `List` in iOS, it appears in a row with the label and
selected value, and a chevron to indicate that you can tap the row to select a
new value:

### Iterating over a picker’s options

To provide selection values for the `Picker` without explicitly listing each
option, you can create the picker with a `ForEach`:

`ForEach` automatically assigns a tag to the selection views using each
option’s `id`. This is possible because `Flavor` conforms to the
`Identifiable` protocol.

The example above relies on the fact that `Flavor` defines the type of its
`id` parameter to exactly match the selection type. If that’s not the case,
you need to override the tag. For example, consider a `Topping` type and a
suggested topping for each flavor:

The following example shows a picker that’s bound to a `Topping` type, while
the options are all `Flavor` instances. Each option uses the tag modifier to
associate the suggested topping with the flavor it displays:

When the user selects chocolate, the picker sets `suggestedTopping` to the
value in the associated tag:

Other examples of when the views in a picker’s `ForEach` need an explicit tag
modifier include when you:

  * Select over the cases of an enumeration that conforms to the `Identifiable` protocol by using anything besides `Self` as the `id` parameter type. For example, a string enumeration might use the case’s `rawValue` string as the `id`. That identifier type doesn’t match the selection type, which is the type of the enumeration itself.

  * Use an optional value for the `selection` input parameter. For that to work, you need to explicitly cast the tag modifier’s input as `Optional` to match. For an example of this, see `tag(_:)`.

### Styling pickers

You can customize the appearance and interaction of pickers using styles that
conform to the `PickerStyle` protocol, like `segmented` or `menu`. To set a
specific style for all picker instances within a view, use the
`pickerStyle(_:)` modifier. The following example applies the `segmented`
style to two pickers that independently select a flavor and a topping:

## Topics

### Creating a picker

`init(selection: Binding<SelectionValue>, content: () -> Content, label: () ->
Label)`

Creates a picker that displays a custom label.

Available when `Label` conforms to `View`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

`init(LocalizedStringKey, selection: Binding<SelectionValue>, content: () ->
Content)`

Creates a picker that generates its label from a localized string key.

Available when `Label` is `Text`, `SelectionValue` conforms to `Hashable`, and
`Content` conforms to `View`.

`init<S>(S, selection: Binding<SelectionValue>, content: () -> Content)`

Creates a picker that generates its label from a string.

Available when `Label` is `Text`, `SelectionValue` conforms to `Hashable`, and
`Content` conforms to `View`.

### Creating a picker for a collection

`init<C>(LocalizedStringKey, sources: C, selection: KeyPath<C.Element,
Binding<SelectionValue>>, content: () -> Content)`

Creates a picker that generates its label from a localized string key.

Available when `Label` is `Text`, `SelectionValue` conforms to `Hashable`, and
`Content` conforms to `View`.

`init<C, S>(S, sources: C, selection: KeyPath<C.Element,
Binding<SelectionValue>>, content: () -> Content)`

Creates a picker bound to a collection of bindings that generates its label
from a string.

Available when `Label` is `Text`, `SelectionValue` conforms to `Hashable`, and
`Content` conforms to `View`.

`init<C>(sources: C, selection: KeyPath<C.Element, Binding<SelectionValue>>,
content: () -> Content, label: () -> Label)`

Creates a picker that displays a custom label.

Available when `Label` conforms to `View`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

### Creating a picker with an image resource label

`init<S>(S, image: ImageResource, selection: Binding<SelectionValue>, content:
() -> Content)`

Creates a picker that generates its label from a string and image resource.

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

`init(LocalizedStringKey, image: ImageResource, selection:
Binding<SelectionValue>, content: () -> Content)`

Creates a picker that generates its label from a localized string key and
image resource

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

`init<C, S>(S, image: ImageResource, sources: C, selection: KeyPath<C.Element,
Binding<SelectionValue>>, content: () -> Content)`

Creates a picker bound to a collection of bindings that generates its label
from a string and image resource.

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

`init<C>(LocalizedStringKey, image: ImageResource, sources: C, selection:
KeyPath<C.Element, Binding<SelectionValue>>, content: () -> Content)`

Creates a picker that generates its label from a localized string key and
image resource.

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

### Creating a picker with an system image label

`init<S>(S, systemImage: String, selection: Binding<SelectionValue>, content:
() -> Content)`

Creates a picker that generates its label from a string and system image.

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

`init(LocalizedStringKey, systemImage: String, selection:
Binding<SelectionValue>, content: () -> Content)`

Creates a picker that generates its label from a localized string key and
system image.

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

`init<C>(LocalizedStringKey, systemImage: String, sources: C, selection:
KeyPath<C.Element, Binding<SelectionValue>>, content: () -> Content)`

Creates a picker that generates its label from a localized string key.

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

`init<C, S>(S, systemImage: String, sources: C, selection: KeyPath<C.Element,
Binding<SelectionValue>>, content: () -> Content)`

Creates a picker bound to a collection of bindings that generates its label
from a string.

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

### Deprecated initializers

`init(selection: Binding<SelectionValue>, label: Label, content: () ->
Content)`

Creates a picker that displays a custom label.

Available when `Label` conforms to `View`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

Deprecated

## Relationships

### Conforms To

  * `View`

## See Also

### Choosing from a set of options

`func pickerStyle<S>(S) -> some View`

Sets the style for pickers within this view.

`func horizontalRadioGroupLayout() -> some View`

Sets the style for radio group style pickers within this view to be
horizontally positioned with the radio buttons inside the layout.

`func defaultWheelPickerItemHeight(CGFloat) -> some View`

Sets the default wheel-style picker item height.

`var defaultWheelPickerItemHeight: CGFloat`

The default height of an item in a wheel-style picker, such as a date picker.

`func paletteSelectionEffect(PaletteSelectionEffect) -> some View`

Specifies the selection effect to apply to a palette item.

`struct PaletteSelectionEffect`

The selection effect to apply to a palette item.

Instance Method

# pickerStyle(_:)

Sets the style for pickers within this view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func pickerStyle<S>(_ style: S) -> some View where S : PickerStyle
    

## See Also

### Choosing from a set of options

`struct Picker`

A control for selecting from a set of mutually exclusive values.

`func horizontalRadioGroupLayout() -> some View`

Sets the style for radio group style pickers within this view to be
horizontally positioned with the radio buttons inside the layout.

`func defaultWheelPickerItemHeight(CGFloat) -> some View`

Sets the default wheel-style picker item height.

`var defaultWheelPickerItemHeight: CGFloat`

The default height of an item in a wheel-style picker, such as a date picker.

`func paletteSelectionEffect(PaletteSelectionEffect) -> some View`

Specifies the selection effect to apply to a palette item.

`struct PaletteSelectionEffect`

The selection effect to apply to a palette item.

Instance Method

# horizontalRadioGroupLayout()

Sets the style for radio group style pickers within this view to be
horizontally positioned with the radio buttons inside the layout.

macOS 10.15+

    
    
    func horizontalRadioGroupLayout() -> some View
    

## Discussion

Use `horizontalRadioGroupLayout()` to configure the visual layout of radio
buttons in a `Picker` so that the radio buttons are arranged horizontally in
the view.

The example below shows two `Picker` controls configured as radio button
groups; the first group shows the default vertical layout; the second group
shows the effect of `horizontalRadioGroupLayout()` which renders the radio
buttons horizontally.

## See Also

### Choosing from a set of options

`struct Picker`

A control for selecting from a set of mutually exclusive values.

`func pickerStyle<S>(S) -> some View`

Sets the style for pickers within this view.

`func defaultWheelPickerItemHeight(CGFloat) -> some View`

Sets the default wheel-style picker item height.

`var defaultWheelPickerItemHeight: CGFloat`

The default height of an item in a wheel-style picker, such as a date picker.

`func paletteSelectionEffect(PaletteSelectionEffect) -> some View`

Specifies the selection effect to apply to a palette item.

`struct PaletteSelectionEffect`

The selection effect to apply to a palette item.

Instance Method

# defaultWheelPickerItemHeight(_:)

Sets the default wheel-style picker item height.

watchOS 6.0+  visionOS 1.0+

    
    
    func defaultWheelPickerItemHeight(_ height: CGFloat) -> some View
    

##  Parameters

`height`

    

The height for the picker items.

## Discussion

Use `defaultWheelPickerItemHeight(_:)` when you need to change the default
item height in a picker control. In this example, the view sets the default
height for picker elements to 30 points.

## See Also

### Choosing from a set of options

`struct Picker`

A control for selecting from a set of mutually exclusive values.

`func pickerStyle<S>(S) -> some View`

Sets the style for pickers within this view.

`func horizontalRadioGroupLayout() -> some View`

Sets the style for radio group style pickers within this view to be
horizontally positioned with the radio buttons inside the layout.

`var defaultWheelPickerItemHeight: CGFloat`

The default height of an item in a wheel-style picker, such as a date picker.

`func paletteSelectionEffect(PaletteSelectionEffect) -> some View`

Specifies the selection effect to apply to a palette item.

`struct PaletteSelectionEffect`

The selection effect to apply to a palette item.

Instance Property

# defaultWheelPickerItemHeight

The default height of an item in a wheel-style picker, such as a date picker.

watchOS 6.0+

    
    
    var defaultWheelPickerItemHeight: CGFloat { get set }

## See Also

### Choosing from a set of options

`struct Picker`

A control for selecting from a set of mutually exclusive values.

`func pickerStyle<S>(S) -> some View`

Sets the style for pickers within this view.

`func horizontalRadioGroupLayout() -> some View`

Sets the style for radio group style pickers within this view to be
horizontally positioned with the radio buttons inside the layout.

`func defaultWheelPickerItemHeight(CGFloat) -> some View`

Sets the default wheel-style picker item height.

`func paletteSelectionEffect(PaletteSelectionEffect) -> some View`

Specifies the selection effect to apply to a palette item.

`struct PaletteSelectionEffect`

The selection effect to apply to a palette item.

Instance Method

# paletteSelectionEffect(_:)

Specifies the selection effect to apply to a palette item.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func paletteSelectionEffect(_ effect: PaletteSelectionEffect) -> some View
    

##  Parameters

`effect`

    

The type of effect to apply when a palette item is selected.

## Discussion

`automatic` applies the system’s default appearance when selected. When using
un-tinted SF Symbols or template images, the current tint color is applied to
the selected items’ image. If the provided SF Symbols have custom tints, a
stroke is drawn around selected items.

If you wish to provide a specific image (or SF Symbol) to indicate selection,
use `custom` to forgo the system’s default selection appearance allowing the
provided image to solely indicate selection instead.

The following example creates a palette picker that disables the system
selection behavior:

If a specific SF Symbol variant is preferable instead, use
`symbolVariant(_:)`.

## See Also

### Choosing from a set of options

`struct Picker`

A control for selecting from a set of mutually exclusive values.

`func pickerStyle<S>(S) -> some View`

Sets the style for pickers within this view.

`func horizontalRadioGroupLayout() -> some View`

Sets the style for radio group style pickers within this view to be
horizontally positioned with the radio buttons inside the layout.

`func defaultWheelPickerItemHeight(CGFloat) -> some View`

Sets the default wheel-style picker item height.

`var defaultWheelPickerItemHeight: CGFloat`

The default height of an item in a wheel-style picker, such as a date picker.

`struct PaletteSelectionEffect`

The selection effect to apply to a palette item.

Structure

# PaletteSelectionEffect

The selection effect to apply to a palette item.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    struct PaletteSelectionEffect

## Overview

You can configure the selection effect of a palette item by using the
`paletteSelectionEffect(_:)` view modifier.

## Topics

### Getting palette selection effects

`static var automatic: PaletteSelectionEffect`

Applies the system’s default effect when selected.

`static var custom: PaletteSelectionEffect`

Does not apply any system effect when selected.

`static func symbolVariant(SymbolVariants) -> PaletteSelectionEffect`

Applies the specified symbol variant when selected.

## Relationships

### Conforms To

  * `Equatable`
  * `Sendable`

## See Also

### Choosing from a set of options

`struct Picker`

A control for selecting from a set of mutually exclusive values.

`func pickerStyle<S>(S) -> some View`

Sets the style for pickers within this view.

`func horizontalRadioGroupLayout() -> some View`

Sets the style for radio group style pickers within this view to be
horizontally positioned with the radio buttons inside the layout.

`func defaultWheelPickerItemHeight(CGFloat) -> some View`

Sets the default wheel-style picker item height.

`var defaultWheelPickerItemHeight: CGFloat`

The default height of an item in a wheel-style picker, such as a date picker.

`func paletteSelectionEffect(PaletteSelectionEffect) -> some View`

Specifies the selection effect to apply to a palette item.

Structure

# DatePicker

A control for selecting an absolute date.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 10.0+
visionOS 1.0+

    
    
    struct DatePicker<Label> where Label : View

## Overview

Use a `DatePicker` when you want to provide a view that allows the user to
select a calendar date, and optionally a time. The view binds to a `Date`
instance.

The following example creates a basic `DatePicker`, which appears on iOS as
text representing the date. This example limits the display to only the
calendar date, not the time. When the user taps or clicks the text, a calendar
view animates in, from which the user can select a date. When the user
dismisses the calendar view, the view updates the bound `Date`.

You can limit the `DatePicker` to specific ranges of dates, allowing
selections only before or after a certain date, or between two dates. The
following example shows a date-and-time picker that only permits selections
within the year 2021 (in the `UTC` time zone).

### Styling date pickers

To use a different style of date picker, use the `datePickerStyle(_:)` view
modifier. The following example shows the graphical date picker style.

## Topics

### Creating a date picker for any date

`init(selection: Binding<Date>, displayedComponents:
DatePicker<Label>.Components, label: () -> Label)`

Creates an instance that selects a `Date` with an unbounded range.

Available when `Label` conforms to `View`.

`init(LocalizedStringKey, selection: Binding<Date>, displayedComponents:
DatePicker<Label>.Components)`

Creates an instance that selects a `Date` with an unbounded range.

Available when `Label` is `Text`.

`init<S>(S, selection: Binding<Date>, displayedComponents:
DatePicker<Label>.Components)`

Creates an instance that selects a `Date` within the given range.

Available when `Label` is `Text`.

### Creating a date picker for a range

`init(selection: Binding<Date>, in: ClosedRange<Date>, displayedComponents:
DatePicker<Label>.Components, label: () -> Label)`

Creates an instance that selects a `Date` in a closed range.

Available when `Label` conforms to `View`.

`init(LocalizedStringKey, selection: Binding<Date>, in: ClosedRange<Date>,
displayedComponents: DatePicker<Label>.Components)`

Creates an instance that selects a `Date` in a closed range.

Available when `Label` is `Text`.

`init<S>(S, selection: Binding<Date>, in: ClosedRange<Date>,
displayedComponents: DatePicker<Label>.Components)`

Creates an instance that selects a `Date` in a closed range.

Available when `Label` is `Text`.

### Creating a date picker with a start date

`init(selection: Binding<Date>, in: PartialRangeFrom<Date>,
displayedComponents: DatePicker<Label>.Components, label: () -> Label)`

Creates an instance that selects a `Date` on or after some start date.

Available when `Label` conforms to `View`.

`init(LocalizedStringKey, selection: Binding<Date>, in:
PartialRangeFrom<Date>, displayedComponents: DatePicker<Label>.Components)`

Creates an instance that selects a `Date` on or after some start date.

Available when `Label` is `Text`.

`init<S>(S, selection: Binding<Date>, in: PartialRangeFrom<Date>,
displayedComponents: DatePicker<Label>.Components)`

Creates an instance that selects a `Date` on or after some start date.

Available when `Label` is `Text`.

### Creating a date picker with an end date

`init(selection: Binding<Date>, in: PartialRangeThrough<Date>,
displayedComponents: DatePicker<Label>.Components, label: () -> Label)`

Creates an instance that selects a `Date` on or before some end date.

Available when `Label` conforms to `View`.

`init(LocalizedStringKey, selection: Binding<Date>, in:
PartialRangeThrough<Date>, displayedComponents: DatePicker<Label>.Components)`

Creates an instance that selects a `Date` on or before some end date.

Available when `Label` is `Text`.

`init<S>(S, selection: Binding<Date>, in: PartialRangeThrough<Date>,
displayedComponents: DatePicker<Label>.Components)`

Creates an instance that selects a `Date` on or before some end date.

Available when `Label` is `Text`.

### Setting date picker components

`typealias Components`

`struct DatePickerComponents`

## Relationships

### Conforms To

  * `View`

## See Also

### Choosing dates

`func datePickerStyle<S>(S) -> some View`

Sets the style for date pickers within this view.

`struct MultiDatePicker`

A control for picking multiple dates.

`var calendar: Calendar`

The current calendar that views should use when handling dates.

`var timeZone: TimeZone`

The current time zone that views should use when handling dates.

Instance Method

# datePickerStyle(_:)

Sets the style for date pickers within this view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 10.0+
visionOS 1.0+

    
    
    func datePickerStyle<S>(_ style: S) -> some View where S : DatePickerStyle
    

## See Also

### Choosing dates

`struct DatePicker`

A control for selecting an absolute date.

`struct MultiDatePicker`

A control for picking multiple dates.

`var calendar: Calendar`

The current calendar that views should use when handling dates.

`var timeZone: TimeZone`

The current time zone that views should use when handling dates.

Structure

# MultiDatePicker

A control for picking multiple dates.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    struct MultiDatePicker<Label> where Label : View

## Overview

Use a `MultiDatePicker` when you want to provide a view that allows the user
to select multiple dates.

The following example creates a basic `MultiDatePicker`, which appears as a
calendar view representing the selected dates:

You can limit the `MultiDatePicker` to specific ranges of dates allowing
selections only before or after a certain date or between two dates. The
following example shows a multi-date picker that only permits selections
within the 6th and (excluding) the 16th of December 2021 (in the `UTC` time
zone):

You can also specify an alternative locale, calendar and time zone through
environment values. This can be useful when using a `PreviewProvider` to see
how your multi-date picker behaves in environments that differ from your own.

The following example shows a multi-date picker with a custom locale, calendar
and time zone:

## Topics

### Picking dates

`init(LocalizedStringKey, selection: Binding<Set<DateComponents>>)`

Creates an instance that selects multiple dates with an unbounded range.

Available when `Label` is `Text`.

`init<S>(S, selection: Binding<Set<DateComponents>>)`

Creates an instance that selects multiple dates with an unbounded range.

Available when `Label` is `Text`.

`init(selection: Binding<Set<DateComponents>>, label: () -> Label)`

Creates an instance that selects multiple dates with an unbounded range.

Available when `Label` conforms to `View`.

### Picking dates in a range

`init(LocalizedStringKey, selection: Binding<Set<DateComponents>>, in:
Range<Date>)`

Creates an instance that selects multiple dates in a range.

Available when `Label` is `Text`.

`init<S>(S, selection: Binding<Set<DateComponents>>, in: Range<Date>)`

Creates an instance that selects multiple dates in a range.

Available when `Label` is `Text`.

`init(selection: Binding<Set<DateComponents>>, in: Range<Date>, label: () ->
Label)`

Creates an instance that selects multiple dates in a range.

Available when `Label` conforms to `View`.

### Picking dates after a date

`init(LocalizedStringKey, selection: Binding<Set<DateComponents>>, in:
PartialRangeFrom<Date>)`

Creates an instance that selects multiple dates on or after some start date.

Available when `Label` is `Text`.

`init<S>(S, selection: Binding<Set<DateComponents>>, in:
PartialRangeFrom<Date>)`

Creates an instance that selects multiple dates on or after some start date.

Available when `Label` is `Text`.

`init(selection: Binding<Set<DateComponents>>, in: PartialRangeFrom<Date>,
label: () -> Label)`

Creates an instance that selects multiple dates on or after some start date.

Available when `Label` conforms to `View`.

### Picking dates before a date

`init(LocalizedStringKey, selection: Binding<Set<DateComponents>>, in:
PartialRangeUpTo<Date>)`

Creates an instance that selects multiple dates before some end date.

Available when `Label` is `Text`.

`init<S>(S, selection: Binding<Set<DateComponents>>, in:
PartialRangeUpTo<Date>)`

Creates an instance that selects multiple dates before some end date.

Available when `Label` is `Text`.

`init(selection: Binding<Set<DateComponents>>, in: PartialRangeUpTo<Date>,
label: () -> Label)`

Creates an instance that selects multiple dates before some end date.

Available when `Label` conforms to `View`.

## Relationships

### Conforms To

  * `View`

## See Also

### Choosing dates

`struct DatePicker`

A control for selecting an absolute date.

`func datePickerStyle<S>(S) -> some View`

Sets the style for date pickers within this view.

`var calendar: Calendar`

The current calendar that views should use when handling dates.

`var timeZone: TimeZone`

The current time zone that views should use when handling dates.

Instance Property

# calendar

The current calendar that views should use when handling dates.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var calendar: Calendar { get set }

## See Also

### Choosing dates

`struct DatePicker`

A control for selecting an absolute date.

`func datePickerStyle<S>(S) -> some View`

Sets the style for date pickers within this view.

`struct MultiDatePicker`

A control for picking multiple dates.

`var timeZone: TimeZone`

The current time zone that views should use when handling dates.

Instance Property

# timeZone

The current time zone that views should use when handling dates.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var timeZone: TimeZone { get set }

## See Also

### Choosing dates

`struct DatePicker`

A control for selecting an absolute date.

`func datePickerStyle<S>(S) -> some View`

Sets the style for date pickers within this view.

`struct MultiDatePicker`

A control for picking multiple dates.

`var calendar: Calendar`

The current calendar that views should use when handling dates.

Structure

# ColorPicker

A control used to select a color from the system color picker UI.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    struct ColorPicker<Label> where Label : View

## Overview

The color picker provides a color well that shows the currently selected
color, and displays the larger system color picker that allows users to select
a new color.

By default color picker supports colors with opacity; to disable opacity
support, set the `supportsOpacity` parameter to `false`. In this mode the
color picker won’t show controls for adjusting the opacity of the selected
color, and strips out opacity from any color set programmatically or selected
from the user’s system favorites.

You use `ColorPicker` by embedding it inside a view hierarchy and initializing
it with a title string and a `Binding` to a `Color`:

## Topics

### Creating a color picker

`init(selection: Binding<Color>, supportsOpacity: Bool, label: () -> Label)`

Creates an instance that selects a color.

`init(LocalizedStringKey, selection: Binding<Color>, supportsOpacity: Bool)`

Creates a color picker with a text label generated from a title string key.

Available when `Label` is `Text`.

`init<S>(S, selection: Binding<Color>, supportsOpacity: Bool)`

Creates a color picker with a text label generated from a title string.

Available when `Label` is `Text`.

### Creating a core graphics color picker

`init(selection: Binding<CGColor>, supportsOpacity: Bool, label: () -> Label)`

Creates an instance that selects a color.

`init(LocalizedStringKey, selection: Binding<CGColor>, supportsOpacity: Bool)`

Creates a color picker with a text label generated from a title string key.

Available when `Label` is `Text`.

`init<S>(S, selection: Binding<CGColor>, supportsOpacity: Bool)`

Creates a color picker with a text label generated from a title string.

Available when `Label` is `Text`.

## Relationships

### Conforms To

  * `View`

Structure

# Gauge

A view that shows a value within a range.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 7.0+
visionOS 1.0+

    
    
    struct Gauge<Label, CurrentValueLabel, BoundsLabel, MarkedValueLabels> where Label : View, CurrentValueLabel : View, BoundsLabel : View, MarkedValueLabels : View

## Overview

A gauge is a view that shows a current level of a value in relation to a
specified finite capacity, very much like a fuel gauge in an automobile. Gauge
displays are configurable; they can show any combination of the gauge’s
current value, the range the gauge can display, and a label describing the
purpose of the gauge itself.

In its most basic form, a gauge displays a single value along the path of the
gauge mapped into a range from 0 to 100 percent. The example below sets the
gauge’s indicator to a position 40 percent along the gauge’s path:

You can make a gauge more descriptive by describing its purpose, showing its
current value and its start and end values. This example shows the gauge
variant that accepts a range and adds labels using multiple trailing closures
describing the current value and the minimum and maximum values of the gauge:

As shown above, the default style for gauges is a linear, continuous bar with
an indicator showing the current value, and optional labels describing the
gauge’s purpose, current, minimum, and maximum values.

Note

Some visual presentations of `Gauge` don’t display all the labels required by
the API. However, the accessibility system does use the label content and you
should use these labels to fully describe the gauge for accessibility users.

To change the style of a gauge, use the `gaugeStyle(_:)` view modifier and
supply an initializer for a specific gauge style. For example, to display the
same gauge in a circular style, apply the `circular` style to the view:

To style elements of a gauge’s presentation, you apply view modifiers to the
elements that you want to change. In the example below, the current value,
minimum and maximum value labels have custom colors:

You can further style a gauge’s appearance by supplying a tint color or a
gradient to the style’s initializer. The following example shows the effect of
a gradient in the initialization of a `CircularGaugeStyle` gauge with a
colorful gradient across the length of the gauge:

## Topics

### Creating a gauge

`init<V>(value: V, in: ClosedRange<V>, label: () -> Label)`

Creates a gauge showing a value within a range and describes the gauge’s
purpose and current value.

`init<V>(value: V, in: ClosedRange<V>, label: () -> Label, currentValueLabel:
() -> CurrentValueLabel)`

Creates a gauge showing a value within a range and that describes the gauge’s
purpose and current value.

`init<V>(value: V, in: ClosedRange<V>, label: () -> Label, currentValueLabel:
() -> CurrentValueLabel, markedValueLabels: () -> MarkedValueLabels)`

Creates a gauge representing a value within a range.

`init<V>(value: V, in: ClosedRange<V>, label: () -> Label, currentValueLabel:
() -> CurrentValueLabel, minimumValueLabel: () -> BoundsLabel,
maximumValueLabel: () -> BoundsLabel)`

Creates a gauge showing a value within a range and describes the gauge’s
current, minimum, and maximum values.

`init<V>(value: V, in: ClosedRange<V>, label: () -> Label, currentValueLabel:
() -> CurrentValueLabel, minimumValueLabel: () -> BoundsLabel,
maximumValueLabel: () -> BoundsLabel, markedValueLabels: () ->
MarkedValueLabels)`

Creates a gauge representing a value within a range.

## Relationships

### Conforms To

  * `View`

## See Also

### Indicating a value

`func gaugeStyle<S>(S) -> some View`

Sets the style for gauges within this view.

`struct ProgressView`

A view that shows the progress toward completion of a task.

`func progressViewStyle<S>(S) -> some View`

Sets the style for progress views in this view.

`struct DefaultDateProgressLabel`

The default type of the current value label when used by a date-relative
progress view.

Instance Method

# gaugeStyle(_:)

Sets the style for gauges within this view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 7.0+
visionOS 1.0+

    
    
    func gaugeStyle<S>(_ style: S) -> some View where S : GaugeStyle
    

## See Also

### Indicating a value

`struct Gauge`

A view that shows a value within a range.

`struct ProgressView`

A view that shows the progress toward completion of a task.

`func progressViewStyle<S>(S) -> some View`

Sets the style for progress views in this view.

`struct DefaultDateProgressLabel`

The default type of the current value label when used by a date-relative
progress view.

Structure

# ProgressView

A view that shows the progress toward completion of a task.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    struct ProgressView<Label, CurrentValueLabel> where Label : View, CurrentValueLabel : View

## Overview

Use a progress view to show that a task is incomplete but advancing toward
completion. A progress view can show both determinate (percentage complete)
and indeterminate (progressing or not) types of progress.

Create a determinate progress view by initializing a `ProgressView` with a
binding to a numeric value that indicates the progress, and a `total` value
that represents completion of the task. By default, the progress is `0.0` and
the total is `1.0`.

The example below uses the state property `progress` to show progress in a
determinate `ProgressView`. The progress view uses its default total of `1.0`,
and because `progress` starts with an initial value of `0.5`, the progress
view begins half-complete. A “More” button below the progress view allows
people to increment the progress in increments of five percent:

To create an indeterminate progress view, use an initializer that doesn’t take
a progress value:

You can also create a progress view that covers a closed range of `Date`
values. As long as the current date is within the range, the progress view
automatically updates, filling or depleting the progress view as it nears the
end of the range. The following example shows a five-minute timer whose start
time is that of the progress view’s initialization:

### Styling progress views

You can customize the appearance and interaction of progress views by creating
styles that conform to the `ProgressViewStyle` protocol. To set a specific
style for all progress view instances within a view, use the
`progressViewStyle(_:)` modifier. In the following example, a custom style
adds a rounded pink border to all progress views within the enclosing
`VStack`:

SwiftUI provides two built-in progress view styles, `linear` and `circular`,
as well as an automatic style that defaults to the most appropriate style in
the current context. The following example shows a circular progress view that
starts at 60 percent completed.

On platforms other than macOS, the circular style may appear as an
indeterminate indicator instead.

## Topics

### Creating an indeterminate progress view

`init()`

Creates a progress view for showing indeterminate progress, without a label.

Available when `Label` conforms to `View` and `CurrentValueLabel` is
`EmptyView`.

`init(label: () -> Label)`

Creates a progress view for showing indeterminate progress that displays a
custom label.

Available when `Label` conforms to `View` and `CurrentValueLabel` is
`EmptyView`.

`init(LocalizedStringKey)`

Creates a progress view for showing indeterminate progress that generates its
label from a localized string.

Available when `Label` conforms to `View` and `CurrentValueLabel` is
`EmptyView`.

`init<S>(S)`

Creates a progress view for showing indeterminate progress that generates its
label from a string.

Available when `Label` conforms to `View` and `CurrentValueLabel` is
`EmptyView`.

### Creating a determinate progress view

`init(Progress)`

Creates a progress view for visualizing the given progress instance.

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

`init<V>(value: V?, total: V)`

Creates a progress view for showing determinate progress.

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

`init<V>(LocalizedStringKey, value: V?, total: V)`

Creates a progress view for showing determinate progress that generates its
label from a localized string.

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

`init<S, V>(S, value: V?, total: V)`

Creates a progress view for showing determinate progress that generates its
label from a string.

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

`init<V>(value: V?, total: V, label: () -> Label)`

Creates a progress view for showing determinate progress, with a custom label.

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

`init<V>(value: V?, total: V, label: () -> Label, currentValueLabel: () ->
CurrentValueLabel)`

Creates a progress view for showing determinate progress, with a custom label.

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

### Create a progress view spanning a date range

`init(timerInterval: ClosedRange<Date>, countsDown: Bool)`

Creates a progress view for showing continuous progress as time passes.

Available when `Label` is `EmptyView` and `CurrentValueLabel` is
`DefaultDateProgressLabel`.

`init(timerInterval: ClosedRange<Date>, countsDown: Bool, label: () -> Label)`

Creates a progress view for showing continuous progress as time passes, with a
descriptive label.

Available when `Label` conforms to `View` and `CurrentValueLabel` is
`DefaultDateProgressLabel`.

`init(timerInterval: ClosedRange<Date>, countsDown: Bool, label: () -> Label,
currentValueLabel: () -> CurrentValueLabel)`

Creates a progress view for showing continuous progress as time passes, with
descriptive and current progress labels.

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

### Creating a configured progress view

`init(ProgressViewStyleConfiguration)`

Creates a progress view based on a style configuration.

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

## Relationships

### Conforms To

  * `View`

## See Also

### Indicating a value

`struct Gauge`

A view that shows a value within a range.

`func gaugeStyle<S>(S) -> some View`

Sets the style for gauges within this view.

`func progressViewStyle<S>(S) -> some View`

Sets the style for progress views in this view.

`struct DefaultDateProgressLabel`

The default type of the current value label when used by a date-relative
progress view.

Instance Method

# progressViewStyle(_:)

Sets the style for progress views in this view.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func progressViewStyle<S>(_ style: S) -> some View where S : ProgressViewStyle
    

##  Parameters

`style`

    

The progress view style to use for this view.

## Discussion

For example, the following code creates a progress view that uses the
“circular” style:

## See Also

### Indicating a value

`struct Gauge`

A view that shows a value within a range.

`func gaugeStyle<S>(S) -> some View`

Sets the style for gauges within this view.

`struct ProgressView`

A view that shows the progress toward completion of a task.

`struct DefaultDateProgressLabel`

The default type of the current value label when used by a date-relative
progress view.

Structure

# DefaultDateProgressLabel

The default type of the current value label when used by a date-relative
progress view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    struct DefaultDateProgressLabel

## Relationships

### Conforms To

  * `View`

## See Also

### Indicating a value

`struct Gauge`

A view that shows a value within a range.

`func gaugeStyle<S>(S) -> some View`

Sets the style for gauges within this view.

`struct ProgressView`

A view that shows the progress toward completion of a task.

`func progressViewStyle<S>(S) -> some View`

Sets the style for progress views in this view.

Structure

# ContentUnavailableView

An interface, consisting of a label and additional content, that you display
when the content of your app is unavailable to users.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct ContentUnavailableView<Label, Description, Actions> where Label : View, Description : View, Actions : View

## Overview

It is recommended to use `ContentUnavailableView` in situations where a view’s
content cannot be displayed. That could be caused by a network error, a list
without items, a search that returns no results etc.

You create an `ContentUnavailableView` in its simplest form, by providing a
label and some additional content such as a description or a call to action:

The system provides default `ContentUnavailableView`s that you can use in
specific situations. The example below illustrates the usage of the `search`
view:

## Topics

### Getting built-in unavailable views

`static var search: ContentUnavailableView<SearchUnavailableContent.Label,
SearchUnavailableContent.Description, SearchUnavailableContent.Actions>`

Creates a `ContentUnavailableView` instance that conveys a search state.

Available when `Label` is `SearchUnavailableContent.Label`, `Description` is
`SearchUnavailableContent.Description`, and `Actions` is
`SearchUnavailableContent.Actions`.

`static func search(text: String) -> ContentUnavailableView<Label,
Description, Actions>`

Creates a `ContentUnavailableView` instance that conveys a search state.

Available when `Label` is `SearchUnavailableContent.Label`, `Description` is
`SearchUnavailableContent.Description`, and `Actions` is
`SearchUnavailableContent.Actions`.

### Creating an unavailable view

`init(label: () -> Label, description: () -> Description, actions: () ->
Actions)`

Creates an interface, consisting of a label and additional content, that you
display when the content of your app is unavailable to users.

### Creating an unavailable view with an image

`init(LocalizedStringKey, image: String, description: Text?)`

Creates an interface, consisting of a title generated from a localized string,
an image and additional content, that you display when the content of your app
is unavailable to users.

Available when `Label` is `Label<Text, Image>`, `Description` is `Text?`, and
`Actions` is `EmptyView`.

`init<S>(S, image: String, description: Text?)`

Creates an interface, consisting of a title generated from a string, an image
and additional content, that you display when the content of your app is
unavailable to users.

Available when `Label` is `Label<Text, Image>`, `Description` is `Text?`, and
`Actions` is `EmptyView`.

### Creating an unavailable view with a system image

`init(LocalizedStringKey, systemImage: String, description: Text?)`

Creates an interface, consisting of a title generated from a localized string,
a system icon image and additional content, that you display when the content
of your app is unavailable to users.

Available when `Label` is `Label<Text, Image>`, `Description` is `Text?`, and
`Actions` is `EmptyView`.

`init<S>(S, systemImage: String, description: Text?)`

Creates an interface, consisting of a title generated from a string, a system
icon image and additional content, that you display when the content of your
app is unavailable to users.

Available when `Label` is `Label<Text, Image>`, `Description` is `Text?`, and
`Actions` is `EmptyView`.

### Supporting types

`struct SearchUnavailableContent`

A structure that represents the body of a static placeholder search view.

## Relationships

### Conforms To

  * `View`

Instance Method

# sensoryFeedback(_:trigger:)

Plays the specified `feedback` when the provided `trigger` value changes.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+

    
    
    func sensoryFeedback<T>(
        _ feedback: SensoryFeedback,
        trigger: T
    ) -> some View where T : Equatable
    

##  Parameters

`feedback`

    

Which type of feedback to play.

`trigger`

    

A value to monitor for changes to determine when to play.

## Discussion

For example, you could play feedback when a state value changes:

## See Also

### Providing haptic feedback

`func sensoryFeedback<T>(trigger: T, (T, T) -> SensoryFeedback?) -> some View`

Plays feedback when returned from the `feedback` closure after the provided
`trigger` value changes.

`func sensoryFeedback<T>(SensoryFeedback, trigger: T, condition: (T, T) ->
Bool) -> some View`

Plays the specified `feedback` when the provided `trigger` value changes and
the `condition` closure returns `true`.

`struct SensoryFeedback`

Represents a type of haptic and/or audio feedback that can be played.

Instance Method

# sensoryFeedback(trigger:_:)

Plays feedback when returned from the `feedback` closure after the provided
`trigger` value changes.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+

    
    
    func sensoryFeedback<T>(
        trigger: T,
        _ feedback: @escaping (T, T) -> SensoryFeedback?
    ) -> some View where T : Equatable
    

##  Parameters

`trigger`

    

A value to monitor for changes to determine when to play.

`feedback`

    

A closure to determine whether to play the feedback and what type of feedback
to play when `trigger` changes.

## Discussion

For example, you could play different feedback for different state
transitions:

## See Also

### Providing haptic feedback

`func sensoryFeedback<T>(SensoryFeedback, trigger: T) -> some View`

Plays the specified `feedback` when the provided `trigger` value changes.

`func sensoryFeedback<T>(SensoryFeedback, trigger: T, condition: (T, T) ->
Bool) -> some View`

Plays the specified `feedback` when the provided `trigger` value changes and
the `condition` closure returns `true`.

`struct SensoryFeedback`

Represents a type of haptic and/or audio feedback that can be played.

Instance Method

# sensoryFeedback(_:trigger:condition:)

Plays the specified `feedback` when the provided `trigger` value changes and
the `condition` closure returns `true`.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+

    
    
    func sensoryFeedback<T>(
        _ feedback: SensoryFeedback,
        trigger: T,
        condition: @escaping (T, T) -> Bool
    ) -> some View where T : Equatable
    

##  Parameters

`feedback`

    

Which type of feedback to play.

`trigger`

    

A value to monitor for changes to determine when to play.

`condition`

    

A closure to determine whether to play the feedback when `trigger` changes.

## Discussion

For example, you could play feedback for certain state transitions:

## See Also

### Providing haptic feedback

`func sensoryFeedback<T>(SensoryFeedback, trigger: T) -> some View`

Plays the specified `feedback` when the provided `trigger` value changes.

`func sensoryFeedback<T>(trigger: T, (T, T) -> SensoryFeedback?) -> some View`

Plays feedback when returned from the `feedback` closure after the provided
`trigger` value changes.

`struct SensoryFeedback`

Represents a type of haptic and/or audio feedback that can be played.

Structure

# SensoryFeedback

Represents a type of haptic and/or audio feedback that can be played.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+

    
    
    struct SensoryFeedback

## Overview

This feedback can be passed to `View.sensoryFeedback` to play it.

## Topics

### Indicating start and stop

`static let start: SensoryFeedback`

Indicates that an activity started.

`static let stop: SensoryFeedback`

Indicates that an activity stopped.

### Indicating changes and selections

`static let alignment: SensoryFeedback`

Indicates the alignment of a dragged item.

`static let decrease: SensoryFeedback`

Indicates that an important value decreased below a significant threshold.

`static let increase: SensoryFeedback`

Indicates that an important value increased above a significant threshold.

`static let levelChange: SensoryFeedback`

Indicates movement between discrete levels of pressure.

`static let selection: SensoryFeedback`

Indicates that a UI element’s values are changing.

### Indicating the outcome of an operation

`static let success: SensoryFeedback`

Indicates that a task or action has completed.

`static let warning: SensoryFeedback`

Indicates that a task or action has produced a warning of some kind.

`static let error: SensoryFeedback`

Indicates that an error has occurred.

### Producing a physical impact

`static let impact: SensoryFeedback`

Provides a physical metaphor you can use to complement a visual experience.

`static func impact(weight: SensoryFeedback.Weight, intensity: Double) ->
SensoryFeedback`

Provides a physical metaphor you can use to complement a visual experience.

`static func impact(flexibility: SensoryFeedback.Flexibility, intensity:
Double) -> SensoryFeedback`

Provides a physical metaphor you can use to complement a visual experience.

`struct Flexibility`

The flexibility to be represented by a type of feedback.

`struct Weight`

The weight to be represented by a type of feedback.

## Relationships

### Conforms To

  * `Equatable`
  * `Sendable`

## See Also

### Providing haptic feedback

`func sensoryFeedback<T>(SensoryFeedback, trigger: T) -> some View`

Plays the specified `feedback` when the provided `trigger` value changes.

`func sensoryFeedback<T>(trigger: T, (T, T) -> SensoryFeedback?) -> some View`

Plays feedback when returned from the `feedback` closure after the provided
`trigger` value changes.

`func sensoryFeedback<T>(SensoryFeedback, trigger: T, condition: (T, T) ->
Bool) -> some View`

Plays the specified `feedback` when the provided `trigger` value changes and
the `condition` closure returns `true`.

Instance Method

# controlSize(_:)

Sets the size for controls within this view.

iOS 15.0+  iPadOS 15.0+  macOS 10.15+  Mac Catalyst 15.0+  watchOS 9.0+
visionOS 1.0+

    
    
    func controlSize(_ controlSize: ControlSize) -> some View
    

##  Parameters

`controlSize`

    

One of the control sizes specified in the `ControlSize` enumeration.

## Discussion

Use `controlSize(_:)` to override the system default size for controls in this
view. In this example, a view displays several typical controls at `.mini`,
`.small` and `.regular` sizes.

## See Also

### Sizing controls

`var controlSize: ControlSize`

The size to apply to controls within a view.

`enum ControlSize`

The size classes, like regular or small, that you can apply to controls within
a view.

Instance Property

# controlSize

The size to apply to controls within a view.

iOS 15.0+  iPadOS 15.0+  macOS 10.15+  Mac Catalyst 15.0+  watchOS 9.0+
visionOS 1.0+

    
    
    var controlSize: ControlSize { get set }

## Discussion

The default is `ControlSize.regular`.

## See Also

### Sizing controls

`func controlSize(ControlSize) -> some View`

Sets the size for controls within this view.

`enum ControlSize`

The size classes, like regular or small, that you can apply to controls within
a view.

Enumeration

# ControlSize

The size classes, like regular or small, that you can apply to controls within
a view.

iOS 15.0+  iPadOS 15.0+  macOS 10.15+  Mac Catalyst 15.0+  watchOS 9.0+
visionOS 1.0+

    
    
    enum ControlSize

## Topics

### Getting control sizes

`case mini`

A control version that is minimally sized.

`case small`

A control version that is proportionally smaller size for space-constrained
views.

`case regular`

A control version that is the default size.

`case large`

A control version that is prominently sized.

`case extraLarge`

## Relationships

### Conforms To

  * `CaseIterable`
  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Sizing controls

`func controlSize(ControlSize) -> some View`

Sets the size for controls within this view.

`var controlSize: ControlSize`

The size to apply to controls within a view.

Instance Property

# controlActiveState

The active state of controls in the view.

macOS 10.15+

    
    
    var controlActiveState: ControlActiveState { get set }

## Discussion

The default is `ControlActiveState.key`.

## See Also

### Activating controls

`enum ControlActiveState`

Enumeration

# ControlActiveState

macOS 10.15+  Mac Catalyst 13.0+

    
    
    enum ControlActiveState

## Topics

### Getting control active states

`case key`

`case active`

`case inactive`

## Relationships

### Conforms To

  * `CaseIterable`
  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Activating controls

`var controlActiveState: ControlActiveState`

The active state of controls in the view.



# CustomAnimation

Instance Method

# animate(value:time:context:)

Calculates the value of the animation at the specified time.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func animate<V>(
        value: V,
        time: TimeInterval,
        context: inout AnimationContext<V>
    ) -> V? where V : VectorArithmetic

**Required**

##  Parameters

`value`

    

The vector to animate towards.

`time`

    

The elapsed time since the start of the animation.

`context`

    

An instance of `AnimationContext` that provides access to state and the
animation environment.

## Return Value

The current value of the animation, or `nil` if the animation has finished.

## Discussion

Implement this method to calculate and return the value of the animation at a
given point in time. If the animation has finished, return `nil` as the value.
This signals to the system that it can remove the animation.

If your custom animation needs to maintain state between calls to the
`animate(value:time:context:)` method, store the state data in `context`. This
makes the data available to the method next time the system calls it. To learn
more about managing state data in a custom animation, see `AnimationContext`.

Instance Method

# velocity(value:time:context:)

Calculates the velocity of the animation at a specified time.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func velocity<V>(
        value: V,
        time: TimeInterval,
        context: AnimationContext<V>
    ) -> V? where V : VectorArithmetic

**Required** Default implementation provided.

##  Parameters

`value`

    

The vector to animate towards.

`time`

    

The amount of time since the start of the animation.

`context`

    

An instance of `AnimationContext` that provides access to state and the
animation environment.

## Return Value

The current velocity of the animation, or `nil` if the animation has finished.

## Discussion

Implement this method to provide the velocity of the animation at a given
time. Should subsequent animations merge with the animation, the system
preserves continuity of the velocity between animations.

The default implementation of this method returns `nil`.

Note

State and environment data is available to this method via the `context`
parameter, but `context` is read-only. This behavior is different than with
`animate(value:time:context:)` and `shouldMerge(previous:value:time:context:)`
where `context` is an `inout` parameter, letting you change the context
including state data of the animation. For more information about managing
state data in a custom animation, see `AnimationContext`.

## Default Implementations

### CustomAnimation Implementations

`func velocity<V>(value: V, time: TimeInterval, context: AnimationContext<V>)
-> V?`

Calculates the velocity of the animation at a specified time.

Instance Method

# shouldMerge(previous:value:time:context:)

Determines whether an instance of the animation can merge with other instance
of the same type.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func shouldMerge<V>(
        previous: Animation,
        value: V,
        time: TimeInterval,
        context: inout AnimationContext<V>
    ) -> Bool where V : VectorArithmetic

**Required** Default implementation provided.

##  Parameters

`previous`

    

The previous running animation.

`value`

    

The vector to animate towards.

`time`

    

The amount of time since the start of the previous animation.

`context`

    

An instance of `AnimationContext` that provides access to state and the
animation environment.

## Return Value

A Boolean value of `true` if the animation should merge with the previous
animation; otherwise, `false`.

## Discussion

When a view creates a new animation on an animatable value that already has a
running animation of the same animation type, the system calls the
`shouldMerge(previous:value:time:context:)` method on the new instance to
determine whether it can merge the two instance. Implement this method if the
animation can merge with another instance. The default implementation returns
`false`.

If `shouldMerge(previous:value:time:context:)` returns `true`, the system
merges the new animation instance with the previous animation. The system
provides to the new instance the state and elapsed time from the previous one.
Then it removes the previous animation.

If this method returns `false`, the system doesn’t merge the animation with
the previous one. Instead, both animations run together and the system
combines their results.

If your custom animation needs to maintain state between calls to the
`shouldMerge(previous:value:time:context:)` method, store the state data in
`context`. This makes the data available to the method next time the system
calls it. To learn more, see `AnimationContext`.

## Default Implementations

### CustomAnimation Implementations

`func shouldMerge<V>(previous: Animation, value: V, time: TimeInterval,
context: inout AnimationContext<V>) -> Bool`

Determines whether an instance of the animation can merge with other instance
of the same type.



# CompactMenuControlGroupStyle

Initializer

# init()

Creates a compact menu control group style.

iOS 16.4+  iPadOS 16.4+  macOS 13.3+  Mac Catalyst 16.4+  visionOS 1.0+

    
    
    init()



# CarouselListStyle

Initializer

# init()

Creates a carousel list style.

watchOS 6.0+

    
    
    init()



# ColorPicker

Initializer

# init(selection:supportsOpacity:label:)

Creates an instance that selects a color.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    init(
        selection: Binding<Color>,
        supportsOpacity: Bool = true,
        @ViewBuilder label: () -> Label
    )

##  Parameters

`selection`

    

A `Binding` to the variable that displays the selected `Color`.

`supportsOpacity`

    

A Boolean value that indicates whether the color picker allows adjusting the
selected color’s opacity; the default is `true`.

`label`

    

A view that describes the use of the selected color. The system color picker
UI sets it’s title using the text from this view.

## See Also

### Creating a color picker

`init(LocalizedStringKey, selection: Binding<Color>, supportsOpacity: Bool)`

Creates a color picker with a text label generated from a title string key.

Available when `Label` is `Text`.

`init<S>(S, selection: Binding<Color>, supportsOpacity: Bool)`

Creates a color picker with a text label generated from a title string.

Available when `Label` is `Text`.

Initializer

# init(_:selection:supportsOpacity:)

Creates a color picker with a text label generated from a title string key.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        selection: Binding<Color>,
        supportsOpacity: Bool = true
    )

Available when `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the localized title of the picker.

`selection`

    

A `Binding` to the variable that displays the selected `Color`.

`supportsOpacity`

    

A Boolean value that indicates whether the color picker allows adjustments to
the selected color’s opacity; the default is `true`.

## Discussion

Use `ColorPicker` to create a color well that your app uses to allow the
selection of a `Color`. The example below creates a color well using a
`Binding` to a property stored in a settings object and title you provide:

## See Also

### Creating a color picker

`init(selection: Binding<Color>, supportsOpacity: Bool, label: () -> Label)`

Creates an instance that selects a color.

`init<S>(S, selection: Binding<Color>, supportsOpacity: Bool)`

Creates a color picker with a text label generated from a title string.

Available when `Label` is `Text`.

Initializer

# init(_:selection:supportsOpacity:)

Creates a color picker with a text label generated from a title string.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        selection: Binding<Color>,
        supportsOpacity: Bool = true
    ) where S : StringProtocol

Available when `Label` is `Text`.

##  Parameters

`title`

    

The title displayed by the color picker.

`selection`

    

A `Binding` to the variable containing a `Color`.

`supportsOpacity`

    

A Boolean value that indicates whether the color picker allows adjustments to
the selected color’s opacity; the default is `true`.

## Discussion

Use `ColorPicker` to create a color well that your app uses to allow the
selection of a `Color`. The example below creates a color well using a
`Binding` and title you provide:

## See Also

### Creating a color picker

`init(selection: Binding<Color>, supportsOpacity: Bool, label: () -> Label)`

Creates an instance that selects a color.

`init(LocalizedStringKey, selection: Binding<Color>, supportsOpacity: Bool)`

Creates a color picker with a text label generated from a title string key.

Available when `Label` is `Text`.

Initializer

# init(selection:supportsOpacity:label:)

Creates an instance that selects a color.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    init(
        selection: Binding<CGColor>,
        supportsOpacity: Bool = true,
        @ViewBuilder label: () -> Label
    )

##  Parameters

`selection`

    

A `Binding` to the variable that displays the selected `CGColor`.

`supportsOpacity`

    

A Boolean value that indicates whether the color picker allows adjusting the
selected color’s opacity; the default is `true`.

`label`

    

A view that describes the use of the selected color. The system color picker
UI sets it’s title using the text from this view.

## See Also

### Creating a core graphics color picker

`init(LocalizedStringKey, selection: Binding<CGColor>, supportsOpacity: Bool)`

Creates a color picker with a text label generated from a title string key.

Available when `Label` is `Text`.

`init<S>(S, selection: Binding<CGColor>, supportsOpacity: Bool)`

Creates a color picker with a text label generated from a title string.

Available when `Label` is `Text`.

Initializer

# init(_:selection:supportsOpacity:)

Creates a color picker with a text label generated from a title string key.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        selection: Binding<CGColor>,
        supportsOpacity: Bool = true
    )

Available when `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the localized title of the picker.

`selection`

    

A `Binding` to the variable that displays the selected `CGColor`.

`supportsOpacity`

    

A Boolean value that indicates whether the color picker allows adjustments to
the selected color’s opacity; the default is `true`.

## See Also

### Creating a core graphics color picker

`init(selection: Binding<CGColor>, supportsOpacity: Bool, label: () -> Label)`

Creates an instance that selects a color.

`init<S>(S, selection: Binding<CGColor>, supportsOpacity: Bool)`

Creates a color picker with a text label generated from a title string.

Available when `Label` is `Text`.

Initializer

# init(_:selection:supportsOpacity:)

Creates a color picker with a text label generated from a title string.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        selection: Binding<CGColor>,
        supportsOpacity: Bool = true
    ) where S : StringProtocol

Available when `Label` is `Text`.

##  Parameters

`title`

    

The title displayed by the color picker.

`selection`

    

A `Binding` to the variable containing a `CGColor`.

`supportsOpacity`

    

A Boolean value that indicates whether the color picker allows adjustments to
the selected color’s opacity; the default is `true`.

## See Also

### Creating a core graphics color picker

`init(selection: Binding<CGColor>, supportsOpacity: Bool, label: () -> Label)`

Creates an instance that selects a color.

`init(LocalizedStringKey, selection: Binding<CGColor>, supportsOpacity: Bool)`

Creates a color picker with a text label generated from a title string key.

Available when `Label` is `Text`.



# CubicKeyframe

Initializer

# init(_:duration:startVelocity:endVelocity:)

Creates a new keyframe using the given value and timestamp.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init(
        _ to: Value,
        duration: TimeInterval,
        startVelocity: Value? = nil,
        endVelocity: Value? = nil
    )

##  Parameters

`to`

    

The value of the keyframe.

`startVelocity`

    

The velocity of the value at the beginning of the segment, or `nil` to
automatically compute the velocity to maintain smooth motion.

`endVelocity`

    

The velocity of the value at the end of the segment, or `nil` to automatically
compute the velocity to maintain smooth motion.

`duration`

    

The duration of the segment defined by this keyframe.



# ColorSchemeContrast

Case

# ColorSchemeContrast.standard

SwiftUI displays views with standard contrast between the app’s foreground and
background colors.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case standard

## See Also

### Getting contrast options

`case increased`

SwiftUI displays views with increased contrast between the app’s foreground
and background colors.

Case

# ColorSchemeContrast.increased

SwiftUI displays views with increased contrast between the app’s foreground
and background colors.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case increased

## See Also

### Getting contrast options

`case standard`

SwiftUI displays views with standard contrast between the app’s foreground and
background colors.

Initializer

# init(_:)

Creates a contrast from its accessibility contrast equivalent.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  tvOS 14.0+  visionOS 1.0+

    
    
    init?(_ uiAccessibilityContrast: UIAccessibilityContrast)



# CustomPresentationDetent

Type Method

# height(in:)

Calculates and returns a height based on the context.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static func height(in context: Self.Context) -> CGFloat?

**Required**

##  Parameters

`context`

    

Information that can help to determine the height of the detent.

## Return Value

The height of the detent, or `nil` if the detent should be inactive based on
the `contenxt` input.

## See Also

### Getting the height

`typealias Context`

Information that you can use to calculate the height of a custom detent.

Type Alias

# CustomPresentationDetent.Context

Information that you can use to calculate the height of a custom detent.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    typealias Context = PresentationDetent.Context

## See Also

### Getting the height

`static func height(in: Self.Context) -> CGFloat?`

Calculates and returns a height based on the context.

**Required**



# CarouselTabViewStyle

Initializer

# init()

Creates a carousel table view style.

watchOS 7.0–10.4  Deprecated

    
    
    init()

Deprecated

Use `verticalPage` instead.



# CommandsBuilder

Type Method

# buildBlock()

Builds an empty command set from a block containing no statements.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static func buildBlock() -> EmptyCommands

## See Also

### Building content

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

Type Method

# buildBlock(_:)

Passes a single command group written as a child group through modified.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static func buildBlock<C>(_ content: C) -> C where C : Commands

## See Also

### Building content

`static func buildBlock() -> EmptyCommands`

Builds an empty command set from a block containing no statements.

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

Type Method

# buildBlock(_:_:)

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static func buildBlock<C0, C1>(
        _ c0: C0,
        _ c1: C1
    ) -> some Commands where C0 : Commands, C1 : Commands
    

## See Also

### Building content

`static func buildBlock() -> EmptyCommands`

Builds an empty command set from a block containing no statements.

`static func buildBlock<C>(C) -> C`

Passes a single command group written as a child group through modified.

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

Type Method

# buildBlock(_:_:_:)

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static func buildBlock<C0, C1, C2>(
        _ c0: C0,
        _ c1: C1,
        _ c2: C2
    ) -> some Commands where C0 : Commands, C1 : Commands, C2 : Commands
    

## See Also

### Building content

`static func buildBlock() -> EmptyCommands`

Builds an empty command set from a block containing no statements.

`static func buildBlock<C>(C) -> C`

Passes a single command group written as a child group through modified.

`static func buildBlock<C0, C1>(C0, C1) -> some Commands`

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

Type Method

# buildBlock(_:_:_:_:)

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static func buildBlock<C0, C1, C2, C3>(
        _ c0: C0,
        _ c1: C1,
        _ c2: C2,
        _ c3: C3
    ) -> some Commands where C0 : Commands, C1 : Commands, C2 : Commands, C3 : Commands
    

## See Also

### Building content

`static func buildBlock() -> EmptyCommands`

Builds an empty command set from a block containing no statements.

`static func buildBlock<C>(C) -> C`

Passes a single command group written as a child group through modified.

`static func buildBlock<C0, C1>(C0, C1) -> some Commands`

`static func buildBlock<C0, C1, C2>(C0, C1, C2) -> some Commands`

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

Type Method

# buildBlock(_:_:_:_:_:)

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static func buildBlock<C0, C1, C2, C3, C4>(
        _ c0: C0,
        _ c1: C1,
        _ c2: C2,
        _ c3: C3,
        _ c4: C4
    ) -> some Commands where C0 : Commands, C1 : Commands, C2 : Commands, C3 : Commands, C4 : Commands
    

## See Also

### Building content

`static func buildBlock() -> EmptyCommands`

Builds an empty command set from a block containing no statements.

`static func buildBlock<C>(C) -> C`

Passes a single command group written as a child group through modified.

`static func buildBlock<C0, C1>(C0, C1) -> some Commands`

`static func buildBlock<C0, C1, C2>(C0, C1, C2) -> some Commands`

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) -> some Commands`

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

Type Method

# buildBlock(_:_:_:_:_:_:)

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static func buildBlock<C0, C1, C2, C3, C4, C5>(
        _ c0: C0,
        _ c1: C1,
        _ c2: C2,
        _ c3: C3,
        _ c4: C4,
        _ c5: C5
    ) -> some Commands where C0 : Commands, C1 : Commands, C2 : Commands, C3 : Commands, C4 : Commands, C5 : Commands
    

## See Also

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

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> some Commands`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> some Commands`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> some Commands`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> some Commands`

Type Method

# buildBlock(_:_:_:_:_:_:_:)

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(
        _ c0: C0,
        _ c1: C1,
        _ c2: C2,
        _ c3: C3,
        _ c4: C4,
        _ c5: C5,
        _ c6: C6
    ) -> some Commands where C0 : Commands, C1 : Commands, C2 : Commands, C3 : Commands, C4 : Commands, C5 : Commands, C6 : Commands
    

## See Also

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

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> some Commands`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> some Commands`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> some Commands`

Type Method

# buildBlock(_:_:_:_:_:_:_:_:)

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(
        _ c0: C0,
        _ c1: C1,
        _ c2: C2,
        _ c3: C3,
        _ c4: C4,
        _ c5: C5,
        _ c6: C6,
        _ c7: C7
    ) -> some Commands where C0 : Commands, C1 : Commands, C2 : Commands, C3 : Commands, C4 : Commands, C5 : Commands, C6 : Commands, C7 : Commands
    

## See Also

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

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> some Commands`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> some Commands`

Type Method

# buildBlock(_:_:_:_:_:_:_:_:_:)

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(
        _ c0: C0,
        _ c1: C1,
        _ c2: C2,
        _ c3: C3,
        _ c4: C4,
        _ c5: C5,
        _ c6: C6,
        _ c7: C7,
        _ c8: C8
    ) -> some Commands where C0 : Commands, C1 : Commands, C2 : Commands, C3 : Commands, C4 : Commands, C5 : Commands, C6 : Commands, C7 : Commands, C8 : Commands
    

## See Also

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

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> some Commands`

Type Method

# buildBlock(_:_:_:_:_:_:_:_:_:_:)

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(
        _ c0: C0,
        _ c1: C1,
        _ c2: C2,
        _ c3: C3,
        _ c4: C4,
        _ c5: C5,
        _ c6: C6,
        _ c7: C7,
        _ c8: C8,
        _ c9: C9
    ) -> some Commands where C0 : Commands, C1 : Commands, C2 : Commands, C3 : Commands, C4 : Commands, C5 : Commands, C6 : Commands, C7 : Commands, C8 : Commands, C9 : Commands
    

## See Also

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

Type Method

# buildEither(first:)

Produces content for a conditional statement in a multi-statement closure when
the condition is true.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    static func buildEither<T, F>(first: T) -> _ConditionalContent<T, F> where T : Commands, F : Commands

## See Also

### Building conditionally

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

Type Method

# buildEither(second:)

Produces content for a conditional statement in a multi-statement closure when
the condition is false.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    static func buildEither<T, F>(second: F) -> _ConditionalContent<T, F> where T : Commands, F : Commands

## See Also

### Building conditionally

`static func buildEither<T, F>(first: T) -> _ConditionalContent<T, F>`

Produces content for a conditional statement in a multi-statement closure when
the condition is true.

`static func buildIf<C>(C?) -> C?`

Produces an optional widget for conditional statements in multi-statement
closures that’s only visible when the condition evaluates to true.

`static func buildLimitedAvailability<C>(C) -> some Commands`

Processes commands for a conditional compiler-control statement that performs
an availability check.

`static func buildExpression<Content>(Content) -> Content`

Builds an expression within the builder.

Type Method

# buildIf(_:)

Produces an optional widget for conditional statements in multi-statement
closures that’s only visible when the condition evaluates to true.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    static func buildIf<C>(_ content: C?) -> C? where C : Commands

## See Also

### Building conditionally

`static func buildEither<T, F>(first: T) -> _ConditionalContent<T, F>`

Produces content for a conditional statement in a multi-statement closure when
the condition is true.

`static func buildEither<T, F>(second: F) -> _ConditionalContent<T, F>`

Produces content for a conditional statement in a multi-statement closure when
the condition is false.

`static func buildLimitedAvailability<C>(C) -> some Commands`

Processes commands for a conditional compiler-control statement that performs
an availability check.

`static func buildExpression<Content>(Content) -> Content`

Builds an expression within the builder.

Type Method

# buildLimitedAvailability(_:)

Processes commands for a conditional compiler-control statement that performs
an availability check.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    static func buildLimitedAvailability<C>(_ content: C) -> some Commands where C : Commands
    

## See Also

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

`static func buildExpression<Content>(Content) -> Content`

Builds an expression within the builder.

Type Method

# buildExpression(_:)

Builds an expression within the builder.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static func buildExpression<Content>(_ content: Content) -> Content where Content : Commands

## See Also

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



# CoordinateSpaceProtocol

Type Property

# immersiveSpace

The named coordinate space that represents the currently opened
`ImmersiveSpace` scene. If no immersive space is currently opened, this
CoordinateSpace provides the same behavior as the `.global` coordinate space.

visionOS 1.1+

    
    
    static var immersiveSpace: NamedCoordinateSpace { get }

Available when `Self` is `NamedCoordinateSpace`.

## See Also

### Getting built-in coordinate spaces

`static var global: GlobalCoordinateSpace`

The global coordinate space at the root of the view hierarchy.

Available when `Self` is `GlobalCoordinateSpace`.

`static var local: LocalCoordinateSpace`

The local coordinate space of the current view.

Available when `Self` is `LocalCoordinateSpace`.

`static func named(some Hashable) -> NamedCoordinateSpace`

Creates a named coordinate space using the given value.

Available when `Self` is `NamedCoordinateSpace`.

`static var scrollView: NamedCoordinateSpace`

The named coordinate space that is added by the system for the innermost
containing scroll view.

Available when `Self` is `NamedCoordinateSpace`.

`static func scrollView(axis: Axis) -> Self`

The named coordinate space that is added by the system for the innermost
containing scroll view that allows scrolling along the provided axis.

Available when `Self` is `NamedCoordinateSpace`.

Type Property

# global

The global coordinate space at the root of the view hierarchy.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static var global: GlobalCoordinateSpace { get }

Available when `Self` is `GlobalCoordinateSpace`.

## See Also

### Getting built-in coordinate spaces

`static var immersiveSpace: NamedCoordinateSpace`

The named coordinate space that represents the currently opened
`ImmersiveSpace` scene. If no immersive space is currently opened, this
CoordinateSpace provides the same behavior as the `.global` coordinate space.

Available when `Self` is `NamedCoordinateSpace`.

`static var local: LocalCoordinateSpace`

The local coordinate space of the current view.

Available when `Self` is `LocalCoordinateSpace`.

`static func named(some Hashable) -> NamedCoordinateSpace`

Creates a named coordinate space using the given value.

Available when `Self` is `NamedCoordinateSpace`.

`static var scrollView: NamedCoordinateSpace`

The named coordinate space that is added by the system for the innermost
containing scroll view.

Available when `Self` is `NamedCoordinateSpace`.

`static func scrollView(axis: Axis) -> Self`

The named coordinate space that is added by the system for the innermost
containing scroll view that allows scrolling along the provided axis.

Available when `Self` is `NamedCoordinateSpace`.

Type Property

# local

The local coordinate space of the current view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static var local: LocalCoordinateSpace { get }

Available when `Self` is `LocalCoordinateSpace`.

## See Also

### Getting built-in coordinate spaces

`static var immersiveSpace: NamedCoordinateSpace`

The named coordinate space that represents the currently opened
`ImmersiveSpace` scene. If no immersive space is currently opened, this
CoordinateSpace provides the same behavior as the `.global` coordinate space.

Available when `Self` is `NamedCoordinateSpace`.

`static var global: GlobalCoordinateSpace`

The global coordinate space at the root of the view hierarchy.

Available when `Self` is `GlobalCoordinateSpace`.

`static func named(some Hashable) -> NamedCoordinateSpace`

Creates a named coordinate space using the given value.

Available when `Self` is `NamedCoordinateSpace`.

`static var scrollView: NamedCoordinateSpace`

The named coordinate space that is added by the system for the innermost
containing scroll view.

Available when `Self` is `NamedCoordinateSpace`.

`static func scrollView(axis: Axis) -> Self`

The named coordinate space that is added by the system for the innermost
containing scroll view that allows scrolling along the provided axis.

Available when `Self` is `NamedCoordinateSpace`.

Type Method

# named(_:)

Creates a named coordinate space using the given value.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static func named(_ name: some Hashable) -> NamedCoordinateSpace

Available when `Self` is `NamedCoordinateSpace`.

##  Parameters

`name`

    

A unique value that identifies the coordinate space.

## Return Value

A named coordinate space identified by the given value.

## Discussion

Use the `coordinateSpace(_:)` modifier to assign a name to the local
coordinate space of a parent view. Child views can then refer to that
coordinate space using `.named(_:)`.

## See Also

### Getting built-in coordinate spaces

`static var immersiveSpace: NamedCoordinateSpace`

The named coordinate space that represents the currently opened
`ImmersiveSpace` scene. If no immersive space is currently opened, this
CoordinateSpace provides the same behavior as the `.global` coordinate space.

Available when `Self` is `NamedCoordinateSpace`.

`static var global: GlobalCoordinateSpace`

The global coordinate space at the root of the view hierarchy.

Available when `Self` is `GlobalCoordinateSpace`.

`static var local: LocalCoordinateSpace`

The local coordinate space of the current view.

Available when `Self` is `LocalCoordinateSpace`.

`static var scrollView: NamedCoordinateSpace`

The named coordinate space that is added by the system for the innermost
containing scroll view.

Available when `Self` is `NamedCoordinateSpace`.

`static func scrollView(axis: Axis) -> Self`

The named coordinate space that is added by the system for the innermost
containing scroll view that allows scrolling along the provided axis.

Available when `Self` is `NamedCoordinateSpace`.

Type Property

# scrollView

The named coordinate space that is added by the system for the innermost
containing scroll view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static var scrollView: NamedCoordinateSpace { get }

Available when `Self` is `NamedCoordinateSpace`.

## See Also

### Getting built-in coordinate spaces

`static var immersiveSpace: NamedCoordinateSpace`

The named coordinate space that represents the currently opened
`ImmersiveSpace` scene. If no immersive space is currently opened, this
CoordinateSpace provides the same behavior as the `.global` coordinate space.

Available when `Self` is `NamedCoordinateSpace`.

`static var global: GlobalCoordinateSpace`

The global coordinate space at the root of the view hierarchy.

Available when `Self` is `GlobalCoordinateSpace`.

`static var local: LocalCoordinateSpace`

The local coordinate space of the current view.

Available when `Self` is `LocalCoordinateSpace`.

`static func named(some Hashable) -> NamedCoordinateSpace`

Creates a named coordinate space using the given value.

Available when `Self` is `NamedCoordinateSpace`.

`static func scrollView(axis: Axis) -> Self`

The named coordinate space that is added by the system for the innermost
containing scroll view that allows scrolling along the provided axis.

Available when `Self` is `NamedCoordinateSpace`.

Type Method

# scrollView(axis:)

The named coordinate space that is added by the system for the innermost
containing scroll view that allows scrolling along the provided axis.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static func scrollView(axis: Axis) -> Self

Available when `Self` is `NamedCoordinateSpace`.

## See Also

### Getting built-in coordinate spaces

`static var immersiveSpace: NamedCoordinateSpace`

The named coordinate space that represents the currently opened
`ImmersiveSpace` scene. If no immersive space is currently opened, this
CoordinateSpace provides the same behavior as the `.global` coordinate space.

Available when `Self` is `NamedCoordinateSpace`.

`static var global: GlobalCoordinateSpace`

The global coordinate space at the root of the view hierarchy.

Available when `Self` is `GlobalCoordinateSpace`.

`static var local: LocalCoordinateSpace`

The local coordinate space of the current view.

Available when `Self` is `LocalCoordinateSpace`.

`static func named(some Hashable) -> NamedCoordinateSpace`

Creates a named coordinate space using the given value.

Available when `Self` is `NamedCoordinateSpace`.

`static var scrollView: NamedCoordinateSpace`

The named coordinate space that is added by the system for the innermost
containing scroll view.

Available when `Self` is `NamedCoordinateSpace`.

Instance Property

# coordinateSpace

The resolved coordinate space.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var coordinateSpace: CoordinateSpace { get }

**Required**

Structure

# GlobalCoordinateSpace

The global coordinate space at the root of the view hierarchy.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct GlobalCoordinateSpace

## Topics

### Creating the coordinate space

`init()`

## Relationships

### Conforms To

  * `CoordinateSpaceProtocol`

## See Also

### Supporting types

`struct LocalCoordinateSpace`

The local coordinate space of the current view.

`struct NamedCoordinateSpace`

A named coordinate space.

Structure

# LocalCoordinateSpace

The local coordinate space of the current view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct LocalCoordinateSpace

## Topics

### Creating the coordinate space

`init()`

## Relationships

### Conforms To

  * `CoordinateSpaceProtocol`

## See Also

### Supporting types

`struct GlobalCoordinateSpace`

The global coordinate space at the root of the view hierarchy.

`struct NamedCoordinateSpace`

A named coordinate space.

Structure

# NamedCoordinateSpace

A named coordinate space.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct NamedCoordinateSpace

## Overview

Use the `coordinateSpace(_:)` modifier to assign a name to the local
coordinate space of a parent view. Child views can then refer to that
coordinate space using `.named(_:)`.

## Relationships

### Conforms To

  * `CoordinateSpaceProtocol`
  * `Equatable`

## See Also

### Supporting types

`struct GlobalCoordinateSpace`

The global coordinate space at the root of the view hierarchy.

`struct LocalCoordinateSpace`

The local coordinate space of the current view.



# ControlActiveState

Case

# ControlActiveState.key

macOS 10.15+  Mac Catalyst 13.0+

    
    
    case key

## See Also

### Getting control active states

`case active`

`case inactive`

Case

# ControlActiveState.active

macOS 10.15+  Mac Catalyst 13.0+

    
    
    case active

## See Also

### Getting control active states

`case key`

`case inactive`

Case

# ControlActiveState.inactive

macOS 10.15+  Mac Catalyst 13.0+

    
    
    case inactive

## See Also

### Getting control active states

`case key`

`case active`



# CircularProgressViewStyle

Initializer

# init()

Creates a circular progress view style.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init()

Initializer

# init(tint:)

Creates a circular progress view style with a tint color.

iOS 14.0–17.4  Deprecated  iPadOS 14.0–17.4  Deprecated  macOS 11.0–14.4
Deprecated  Mac Catalyst 14.0–17.4  Deprecated  tvOS 14.0–17.4  Deprecated
watchOS 7.0–10.4  Deprecated  visionOS 1.0+

    
    
    init(tint: Color)

Deprecated

Use the `tint(_:)` view modifier instead.



# ContainerRelativeShape

Initializer

# init()

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init()



# Color.RGBColorSpace

Case

# Color.RGBColorSpace.sRGB

The extended red, green, blue (sRGB) color space.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case sRGB

## Discussion

For information about the sRGB colorimetry and nonlinear transform function,
see the IEC 61966-2-1 specification.

Standard sRGB color spaces clamp the red, green, and blue components of a
color to a range of `0` to `1`, but SwiftUI colors use an extended sRGB color
space, so you can use component values outside that range.

## See Also

### Getting color spaces

`case sRGBLinear`

The extended sRGB color space with a linear transfer function.

`case displayP3`

The Display P3 color space.

Case

# Color.RGBColorSpace.sRGBLinear

The extended sRGB color space with a linear transfer function.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case sRGBLinear

## Discussion

This color space has the same colorimetry as `Color.RGBColorSpace.sRGB`, but
uses a linear transfer function.

Standard sRGB color spaces clamp the red, green, and blue components of a
color to a range of `0` to `1`, but SwiftUI colors use an extended sRGB color
space, so you can use component values outside that range.

## See Also

### Getting color spaces

`case sRGB`

The extended red, green, blue (sRGB) color space.

`case displayP3`

The Display P3 color space.

Case

# Color.RGBColorSpace.displayP3

The Display P3 color space.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case displayP3

## Discussion

This color space uses the Digital Cinema Initiatives - Protocol 3 (DCI-P3)
primary colors, a D65 white point, and the `Color.RGBColorSpace.sRGB` transfer
function.

## See Also

### Getting color spaces

`case sRGB`

The extended red, green, blue (sRGB) color space.

`case sRGBLinear`

The extended sRGB color space with a linear transfer function.



# ContentTransition

Type Property

# identity

The identity content transition, which indicates that content changes
shouldn’t animate.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static let identity: ContentTransition

## Discussion

You can pass this value to a `contentTransition(_:)` modifier to selectively
disable animations that would otherwise be applied by a `withAnimation(_:_:)`
block.

## See Also

### Getting content transitions

`static let interpolate: ContentTransition`

A content transition that indicates the views attempt to interpolate their
contents during transitions, where appropriate.

`static func numericText(countsDown: Bool) -> ContentTransition`

Creates a content transition intended to be used with `Text` views displaying
numeric text. In certain environments changes to the text will enable a
nonstandard transition tailored to numeric characters that count up or down.

`static func numericText(value: Double) -> ContentTransition`

Creates a content transition intended to be used with `Text` views displaying
numbers.

`static let opacity: ContentTransition`

A content transition that indicates content fades from transparent to opaque
on insertion, and from opaque to transparent on removal.

`static var symbolEffect: ContentTransition`

A content transition that applies the default symbol effect transition to
symbol images within the inserted or removed view hierarchy. Other views are
unaffected by this transition.

`static func symbolEffect<T>(T, options: SymbolEffectOptions) ->
ContentTransition`

Creates a content transition that applies the symbol Replace animation to
symbol images that it is applied to.

Type Property

# interpolate

A content transition that indicates the views attempt to interpolate their
contents during transitions, where appropriate.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static let interpolate: ContentTransition

## Discussion

Text views can interpolate transitions when the text views have identical
strings. Matching glyph pairs can animate changes to their color, position,
size, and any variable properties. Interpolation can apply within a
`Font.Design` case, but not between cases, or between entirely different
fonts. For example, you can interpolate a change between `thin` and `black`
variations of a font, since these are both cases of `Font.Weight`. However,
you can’t interpolate between the default design of a font and its Italic
version, because these are different fonts. Any changes that can’t show an
interpolated animation use an opacity animation instead.

Symbol images created with the `init(systemName:)` initializer work the same
way as text: changes within the same symbol attempt to interpolate the
symbol’s paths. When interpolation is unavailable, the system uses an opacity
transition instead.

## See Also

### Getting content transitions

`static let identity: ContentTransition`

The identity content transition, which indicates that content changes
shouldn’t animate.

`static func numericText(countsDown: Bool) -> ContentTransition`

Creates a content transition intended to be used with `Text` views displaying
numeric text. In certain environments changes to the text will enable a
nonstandard transition tailored to numeric characters that count up or down.

`static func numericText(value: Double) -> ContentTransition`

Creates a content transition intended to be used with `Text` views displaying
numbers.

`static let opacity: ContentTransition`

A content transition that indicates content fades from transparent to opaque
on insertion, and from opaque to transparent on removal.

`static var symbolEffect: ContentTransition`

A content transition that applies the default symbol effect transition to
symbol images within the inserted or removed view hierarchy. Other views are
unaffected by this transition.

`static func symbolEffect<T>(T, options: SymbolEffectOptions) ->
ContentTransition`

Creates a content transition that applies the symbol Replace animation to
symbol images that it is applied to.

Type Method

# numericText(countsDown:)

Creates a content transition intended to be used with `Text` views displaying
numeric text. In certain environments changes to the text will enable a
nonstandard transition tailored to numeric characters that count up or down.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static func numericText(countsDown: Bool = false) -> ContentTransition

##  Parameters

`countsDown`

    

true if the numbers represented by the text are counting downwards.

## Return Value

a new content transition.

## See Also

### Getting content transitions

`static let identity: ContentTransition`

The identity content transition, which indicates that content changes
shouldn’t animate.

`static let interpolate: ContentTransition`

A content transition that indicates the views attempt to interpolate their
contents during transitions, where appropriate.

`static func numericText(value: Double) -> ContentTransition`

Creates a content transition intended to be used with `Text` views displaying
numbers.

`static let opacity: ContentTransition`

A content transition that indicates content fades from transparent to opaque
on insertion, and from opaque to transparent on removal.

`static var symbolEffect: ContentTransition`

A content transition that applies the default symbol effect transition to
symbol images within the inserted or removed view hierarchy. Other views are
unaffected by this transition.

`static func symbolEffect<T>(T, options: SymbolEffectOptions) ->
ContentTransition`

Creates a content transition that applies the symbol Replace animation to
symbol images that it is applied to.

Type Method

# numericText(value:)

Creates a content transition intended to be used with `Text` views displaying
numbers.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static func numericText(value: Double) -> ContentTransition

##  Parameters

`value`

    

the value represented by the `Text` view being animated. The difference
between the old and new values when the text changes will be used to determine
the animation direction.

## Return Value

a new content transition.

## Discussion

The example below creates a text view displaying a particular value, assigning
the same value to the associated transition:

## See Also

### Getting content transitions

`static let identity: ContentTransition`

The identity content transition, which indicates that content changes
shouldn’t animate.

`static let interpolate: ContentTransition`

A content transition that indicates the views attempt to interpolate their
contents during transitions, where appropriate.

`static func numericText(countsDown: Bool) -> ContentTransition`

Creates a content transition intended to be used with `Text` views displaying
numeric text. In certain environments changes to the text will enable a
nonstandard transition tailored to numeric characters that count up or down.

`static let opacity: ContentTransition`

A content transition that indicates content fades from transparent to opaque
on insertion, and from opaque to transparent on removal.

`static var symbolEffect: ContentTransition`

A content transition that applies the default symbol effect transition to
symbol images within the inserted or removed view hierarchy. Other views are
unaffected by this transition.

`static func symbolEffect<T>(T, options: SymbolEffectOptions) ->
ContentTransition`

Creates a content transition that applies the symbol Replace animation to
symbol images that it is applied to.

Type Property

# opacity

A content transition that indicates content fades from transparent to opaque
on insertion, and from opaque to transparent on removal.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static let opacity: ContentTransition

## See Also

### Getting content transitions

`static let identity: ContentTransition`

The identity content transition, which indicates that content changes
shouldn’t animate.

`static let interpolate: ContentTransition`

A content transition that indicates the views attempt to interpolate their
contents during transitions, where appropriate.

`static func numericText(countsDown: Bool) -> ContentTransition`

Creates a content transition intended to be used with `Text` views displaying
numeric text. In certain environments changes to the text will enable a
nonstandard transition tailored to numeric characters that count up or down.

`static func numericText(value: Double) -> ContentTransition`

Creates a content transition intended to be used with `Text` views displaying
numbers.

`static var symbolEffect: ContentTransition`

A content transition that applies the default symbol effect transition to
symbol images within the inserted or removed view hierarchy. Other views are
unaffected by this transition.

`static func symbolEffect<T>(T, options: SymbolEffectOptions) ->
ContentTransition`

Creates a content transition that applies the symbol Replace animation to
symbol images that it is applied to.

Type Property

# symbolEffect

A content transition that applies the default symbol effect transition to
symbol images within the inserted or removed view hierarchy. Other views are
unaffected by this transition.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static var symbolEffect: ContentTransition { get }

## See Also

### Getting content transitions

`static let identity: ContentTransition`

The identity content transition, which indicates that content changes
shouldn’t animate.

`static let interpolate: ContentTransition`

A content transition that indicates the views attempt to interpolate their
contents during transitions, where appropriate.

`static func numericText(countsDown: Bool) -> ContentTransition`

Creates a content transition intended to be used with `Text` views displaying
numeric text. In certain environments changes to the text will enable a
nonstandard transition tailored to numeric characters that count up or down.

`static func numericText(value: Double) -> ContentTransition`

Creates a content transition intended to be used with `Text` views displaying
numbers.

`static let opacity: ContentTransition`

A content transition that indicates content fades from transparent to opaque
on insertion, and from opaque to transparent on removal.

`static func symbolEffect<T>(T, options: SymbolEffectOptions) ->
ContentTransition`

Creates a content transition that applies the symbol Replace animation to
symbol images that it is applied to.

Type Method

# symbolEffect(_:options:)

Creates a content transition that applies the symbol Replace animation to
symbol images that it is applied to.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static func symbolEffect<T>(
        _ effect: T,
        options: SymbolEffectOptions = .default
    ) -> ContentTransition where T : ContentTransitionSymbolEffect, T : SymbolEffect

##  Parameters

`config`

    

the animation configuration value.

## Return Value

a new content transition.

## See Also

### Getting content transitions

`static let identity: ContentTransition`

The identity content transition, which indicates that content changes
shouldn’t animate.

`static let interpolate: ContentTransition`

A content transition that indicates the views attempt to interpolate their
contents during transitions, where appropriate.

`static func numericText(countsDown: Bool) -> ContentTransition`

Creates a content transition intended to be used with `Text` views displaying
numeric text. In certain environments changes to the text will enable a
nonstandard transition tailored to numeric characters that count up or down.

`static func numericText(value: Double) -> ContentTransition`

Creates a content transition intended to be used with `Text` views displaying
numbers.

`static let opacity: ContentTransition`

A content transition that indicates content fades from transparent to opaque
on insertion, and from opaque to transparent on removal.

`static var symbolEffect: ContentTransition`

A content transition that applies the default symbol effect transition to
symbol images within the inserted or removed view hierarchy. Other views are
unaffected by this transition.



# Chart view modifiers

Instance Method

# chartBackground(alignment:content:)

Adds a background to a view that contains a chart.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartBackground<V>(
        alignment: Alignment = .center,
        @ViewBuilder content: @escaping (ChartProxy) -> V
    ) -> some View where V : View
    

##  Parameters

`alignment`

    

The alignment of the content.

`content`

    

The content of the background.

## Discussion

You can use this modifier to define a background view as a function of the
chart in the view. You can access the chart with the `ChartProxy` object
passed into the closure.

Note

If `self` contains more than one chart, the chart proxy will refer to the
first chart.

## See Also

### Styles

`func chartForegroundStyleScale<DataValue, S>(KeyValuePairs<DataValue, S>) ->
some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<Domain, Range>(domain: Domain, range: Range,
type: ScaleType?) -> some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<Domain>(domain: Domain, type: ScaleType?) ->
some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<Domain, S>(domain: Domain, mapping:
(Domain.Element) -> S) -> some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<DataValue, S>(mapping: (DataValue) -> S) ->
some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<Range>(range: Range, type: ScaleType?) -> some
View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale(type: ScaleType?) -> some View`

Configures the foreground style scale for charts.

`func chartPlotStyle<Content>(content: (ChartPlotContent) -> Content) -> some
View`

Configures the plot area of charts.

Instance Method

# chartForegroundStyleScale(_:)

Configures the foreground style scale for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartForegroundStyleScale<DataValue, S>(_ mapping: KeyValuePairs<DataValue, S>) -> some View where DataValue : Plottable, S : ShapeStyle
    

##  Parameters

`mapping`

    

Maps data categories to foreground styles.

## See Also

### Styles

`func chartBackground<V>(alignment: Alignment, content: (ChartProxy) -> V) ->
some View`

Adds a background to a view that contains a chart.

`func chartForegroundStyleScale<Domain, Range>(domain: Domain, range: Range,
type: ScaleType?) -> some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<Domain>(domain: Domain, type: ScaleType?) ->
some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<Domain, S>(domain: Domain, mapping:
(Domain.Element) -> S) -> some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<DataValue, S>(mapping: (DataValue) -> S) ->
some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<Range>(range: Range, type: ScaleType?) -> some
View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale(type: ScaleType?) -> some View`

Configures the foreground style scale for charts.

`func chartPlotStyle<Content>(content: (ChartPlotContent) -> Content) -> some
View`

Configures the plot area of charts.

Instance Method

# chartForegroundStyleScale(domain:range:type:)

Configures the foreground style scale for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartForegroundStyleScale<Domain, Range>(
        domain: Domain,
        range: Range,
        type: ScaleType? = nil
    ) -> some View where Domain : ScaleDomain, Range : ScaleRange, Range.VisualValue : ShapeStyle
    

##  Parameters

`domain`

    

The possible data values plotted as foreground style in the chart. You can
define the domain with a `ClosedRange` for number or `Date` values (e.g., `0
... 500`), and with an array for categorical values (e.g., `["A", "B", "C"]`)

`range`

    

The range of foreground styles that correspond to the scale domain.

`type`

    

The scale type.

## See Also

### Styles

`func chartBackground<V>(alignment: Alignment, content: (ChartProxy) -> V) ->
some View`

Adds a background to a view that contains a chart.

`func chartForegroundStyleScale<DataValue, S>(KeyValuePairs<DataValue, S>) ->
some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<Domain>(domain: Domain, type: ScaleType?) ->
some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<Domain, S>(domain: Domain, mapping:
(Domain.Element) -> S) -> some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<DataValue, S>(mapping: (DataValue) -> S) ->
some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<Range>(range: Range, type: ScaleType?) -> some
View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale(type: ScaleType?) -> some View`

Configures the foreground style scale for charts.

`func chartPlotStyle<Content>(content: (ChartPlotContent) -> Content) -> some
View`

Configures the plot area of charts.

Instance Method

# chartForegroundStyleScale(domain:type:)

Configures the foreground style scale for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartForegroundStyleScale<Domain>(
        domain: Domain,
        type: ScaleType? = nil
    ) -> some View where Domain : ScaleDomain
    

##  Parameters

`domain`

    

The possible data values plotted as foreground style in the chart. You can
define the domain with a `ClosedRange` for number or `Date` values (e.g., `0
... 500`), and with an array for categorical values (e.g., `["A", "B", "C"]`)

`type`

    

The scale type.

## See Also

### Styles

`func chartBackground<V>(alignment: Alignment, content: (ChartProxy) -> V) ->
some View`

Adds a background to a view that contains a chart.

`func chartForegroundStyleScale<DataValue, S>(KeyValuePairs<DataValue, S>) ->
some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<Domain, Range>(domain: Domain, range: Range,
type: ScaleType?) -> some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<Domain, S>(domain: Domain, mapping:
(Domain.Element) -> S) -> some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<DataValue, S>(mapping: (DataValue) -> S) ->
some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<Range>(range: Range, type: ScaleType?) -> some
View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale(type: ScaleType?) -> some View`

Configures the foreground style scale for charts.

`func chartPlotStyle<Content>(content: (ChartPlotContent) -> Content) -> some
View`

Configures the plot area of charts.

Instance Method

# chartForegroundStyleScale(domain:mapping:)

Configures the foreground style scale for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartForegroundStyleScale<Domain, S>(
        domain: Domain,
        mapping: @escaping (Domain.Element) -> S
    ) -> some View where Domain : Collection, S : ShapeStyle, Domain.Element : Plottable
    

##  Parameters

`domain`

    

The possible data values plotted as foreground style in the chart.

`mapping`

    

Maps data categories to foreground styles.

## See Also

### Styles

`func chartBackground<V>(alignment: Alignment, content: (ChartProxy) -> V) ->
some View`

Adds a background to a view that contains a chart.

`func chartForegroundStyleScale<DataValue, S>(KeyValuePairs<DataValue, S>) ->
some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<Domain, Range>(domain: Domain, range: Range,
type: ScaleType?) -> some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<Domain>(domain: Domain, type: ScaleType?) ->
some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<DataValue, S>(mapping: (DataValue) -> S) ->
some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<Range>(range: Range, type: ScaleType?) -> some
View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale(type: ScaleType?) -> some View`

Configures the foreground style scale for charts.

`func chartPlotStyle<Content>(content: (ChartPlotContent) -> Content) -> some
View`

Configures the plot area of charts.

Instance Method

# chartForegroundStyleScale(mapping:)

Configures the foreground style scale for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartForegroundStyleScale<DataValue, S>(mapping: @escaping (DataValue) -> S) -> some View where DataValue : Plottable, S : ShapeStyle
    

##  Parameters

`mapping`

    

Maps data categories to foreground styles.

## See Also

### Styles

`func chartBackground<V>(alignment: Alignment, content: (ChartProxy) -> V) ->
some View`

Adds a background to a view that contains a chart.

`func chartForegroundStyleScale<DataValue, S>(KeyValuePairs<DataValue, S>) ->
some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<Domain, Range>(domain: Domain, range: Range,
type: ScaleType?) -> some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<Domain>(domain: Domain, type: ScaleType?) ->
some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<Domain, S>(domain: Domain, mapping:
(Domain.Element) -> S) -> some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<Range>(range: Range, type: ScaleType?) -> some
View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale(type: ScaleType?) -> some View`

Configures the foreground style scale for charts.

`func chartPlotStyle<Content>(content: (ChartPlotContent) -> Content) -> some
View`

Configures the plot area of charts.

Instance Method

# chartForegroundStyleScale(range:type:)

Configures the foreground style scale for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartForegroundStyleScale<Range>(
        range: Range,
        type: ScaleType? = nil
    ) -> some View where Range : ScaleRange, Range.VisualValue : ShapeStyle
    

##  Parameters

`range`

    

The range of foreground styles that correspond to the scale domain.

`type`

    

The scale type.

## See Also

### Styles

`func chartBackground<V>(alignment: Alignment, content: (ChartProxy) -> V) ->
some View`

Adds a background to a view that contains a chart.

`func chartForegroundStyleScale<DataValue, S>(KeyValuePairs<DataValue, S>) ->
some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<Domain, Range>(domain: Domain, range: Range,
type: ScaleType?) -> some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<Domain>(domain: Domain, type: ScaleType?) ->
some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<Domain, S>(domain: Domain, mapping:
(Domain.Element) -> S) -> some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<DataValue, S>(mapping: (DataValue) -> S) ->
some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale(type: ScaleType?) -> some View`

Configures the foreground style scale for charts.

`func chartPlotStyle<Content>(content: (ChartPlotContent) -> Content) -> some
View`

Configures the plot area of charts.

Instance Method

# chartForegroundStyleScale(type:)

Configures the foreground style scale for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartForegroundStyleScale(type: ScaleType? = nil) -> some View
    

##  Parameters

`type`

    

The scale type.

## See Also

### Styles

`func chartBackground<V>(alignment: Alignment, content: (ChartProxy) -> V) ->
some View`

Adds a background to a view that contains a chart.

`func chartForegroundStyleScale<DataValue, S>(KeyValuePairs<DataValue, S>) ->
some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<Domain, Range>(domain: Domain, range: Range,
type: ScaleType?) -> some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<Domain>(domain: Domain, type: ScaleType?) ->
some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<Domain, S>(domain: Domain, mapping:
(Domain.Element) -> S) -> some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<DataValue, S>(mapping: (DataValue) -> S) ->
some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<Range>(range: Range, type: ScaleType?) -> some
View`

Configures the foreground style scale for charts.

`func chartPlotStyle<Content>(content: (ChartPlotContent) -> Content) -> some
View`

Configures the plot area of charts.

Instance Method

# chartPlotStyle(content:)

Configures the plot area of charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartPlotStyle<Content>(@ViewBuilder content: @escaping (ChartPlotContent) -> Content) -> some View where Content : View
    

##  Parameters

`content`

    

A closure that returns the content of the plot area.

## Discussion

Use this modifier to configure the size or aspect ratio of the plot area of
charts.

For example:

## See Also

### Styles

`func chartBackground<V>(alignment: Alignment, content: (ChartProxy) -> V) ->
some View`

Adds a background to a view that contains a chart.

`func chartForegroundStyleScale<DataValue, S>(KeyValuePairs<DataValue, S>) ->
some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<Domain, Range>(domain: Domain, range: Range,
type: ScaleType?) -> some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<Domain>(domain: Domain, type: ScaleType?) ->
some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<Domain, S>(domain: Domain, mapping:
(Domain.Element) -> S) -> some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<DataValue, S>(mapping: (DataValue) -> S) ->
some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<Range>(range: Range, type: ScaleType?) -> some
View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale(type: ScaleType?) -> some View`

Configures the foreground style scale for charts.

Instance Method

# chartLegend(_:)

Configures the legend for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartLegend(_ visibility: Visibility) -> some View
    

##  Parameters

`visibility`

    

The visibility of the legend.

## See Also

### Legends

`func chartLegend(position: AnnotationPosition, alignment: Alignment?,
spacing: CGFloat?) -> some View`

Configures the legend for charts.

`func chartLegend<Content>(position: AnnotationPosition, alignment:
Alignment?, spacing: CGFloat?, content: () -> Content) -> some View`

Configures the legend for charts.

Instance Method

# chartLegend(position:alignment:spacing:)

Configures the legend for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartLegend(
        position: AnnotationPosition = .automatic,
        alignment: Alignment? = nil,
        spacing: CGFloat? = nil
    ) -> some View
    

##  Parameters

`position`

    

Configures the position of the legend.

`alignment`

    

Alignment of the legend within the space available to it. Use `nil` for
default alignment.

`spacing`

    

Distance between the legend and the chart. Use `nil` for the default spacing.

## See Also

### Legends

`func chartLegend(Visibility) -> some View`

Configures the legend for charts.

`func chartLegend<Content>(position: AnnotationPosition, alignment:
Alignment?, spacing: CGFloat?, content: () -> Content) -> some View`

Configures the legend for charts.

Instance Method

# chartLegend(position:alignment:spacing:content:)

Configures the legend for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartLegend<Content>(
        position: AnnotationPosition = .automatic,
        alignment: Alignment? = nil,
        spacing: CGFloat? = nil,
        @ViewBuilder content: () -> Content
    ) -> some View where Content : View
    

##  Parameters

`position`

    

Configures the position of the legend.

`alignment`

    

Alignment of the legend within the space available to it. Use `nil` for
default alignment.

`spacing`

    

Distance between the legend and the chart. Use `nil` for the default spacing.

`content`

    

The content of the legend.

## See Also

### Legends

`func chartLegend(Visibility) -> some View`

Configures the legend for charts.

`func chartLegend(position: AnnotationPosition, alignment: Alignment?,
spacing: CGFloat?) -> some View`

Configures the legend for charts.

Instance Method

# chartOverlay(alignment:content:)

Adds an overlay to a view that contains a chart.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartOverlay<V>(
        alignment: Alignment = .center,
        @ViewBuilder content: @escaping (ChartProxy) -> V
    ) -> some View where V : View
    

##  Parameters

`alignment`

    

The alignment of the content.

`content`

    

The content of the overlay.

## Discussion

You can use this modifier to define an overlay view as a function of the chart
in the view. You can access the chart with the `ChartProxy` object passed into
the closure.

Below is an example where we define an overlay view that handles drag gestures
and use the proxy to convert the gesture coordinates to data values in the
chart.

Note

If `self` contains more than one chart, the chart proxy will refer to the
first chart.

Instance Method

# chartXAxis(_:)

Sets the visibility of the x axis.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartXAxis(_ visibility: Visibility) -> some View
    

## See Also

### Axes

`func chartXAxis<Content>(content: () -> Content) -> some View`

Configures the x-axis for charts in the view.

`func chartXAxisStyle<Content>(content: (ChartAxisContent) -> Content) -> some
View`

Configures the x axis content of charts.

`func chartYAxis(Visibility) -> some View`

Sets the visibility of the y axis.

`func chartYAxis<Content>(content: () -> Content) -> some View`

Configures the y-axis for charts in the view.

`func chartYAxisStyle<Content>(content: (ChartAxisContent) -> Content) -> some
View`

Configures the y axis content of charts.

Instance Method

# chartXAxis(content:)

Configures the x-axis for charts in the view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartXAxis<Content>(@AxisContentBuilder content: () -> Content) -> some View where Content : AxisContent
    

##  Parameters

`content`

    

The axis content.

## Discussion

Use this modifier to customize the x-axis of a chart. Provide an `AxisMarks`
builder that composes `AxisGridLine`, `AxisTick`, and `AxisValueLabel`
structures to form the axis. Omit components from the builder to omit them
from the resulting axis. For example, the following code adds grid lines to
the x-axis:

You can also compose multiple `AxisMarks` to create more complex axes:

The above example above customizes the x-axis using two `AxisMarks`
declarations. The first creates a grid line for every hour in the day. The
second adds a tick and label for every six hours in the day, with a second
line showing the date for the very beginning of the axis.

Note

To add an axis label, use one of the label modifiers, like
`chartXAxisLabel(position:alignment:spacing:content:)`.

## See Also

### Axes

`func chartXAxis(Visibility) -> some View`

Sets the visibility of the x axis.

`func chartXAxisStyle<Content>(content: (ChartAxisContent) -> Content) -> some
View`

Configures the x axis content of charts.

`func chartYAxis(Visibility) -> some View`

Sets the visibility of the y axis.

`func chartYAxis<Content>(content: () -> Content) -> some View`

Configures the y-axis for charts in the view.

`func chartYAxisStyle<Content>(content: (ChartAxisContent) -> Content) -> some
View`

Configures the y axis content of charts.

Instance Method

# chartXAxisStyle(content:)

Configures the x axis content of charts.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func chartXAxisStyle<Content>(@ViewBuilder content: @escaping (ChartAxisContent) -> Content) -> some View where Content : View
    

##  Parameters

`content`

    

A closure that returns the content of the axis.

## Discussion

Use this modifier to configure the size or aspect ratio of the plot area of
charts.

For example:

## See Also

### Axes

`func chartXAxis(Visibility) -> some View`

Sets the visibility of the x axis.

`func chartXAxis<Content>(content: () -> Content) -> some View`

Configures the x-axis for charts in the view.

`func chartYAxis(Visibility) -> some View`

Sets the visibility of the y axis.

`func chartYAxis<Content>(content: () -> Content) -> some View`

Configures the y-axis for charts in the view.

`func chartYAxisStyle<Content>(content: (ChartAxisContent) -> Content) -> some
View`

Configures the y axis content of charts.

Instance Method

# chartYAxis(_:)

Sets the visibility of the y axis.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartYAxis(_ visibility: Visibility) -> some View
    

## See Also

### Axes

`func chartXAxis(Visibility) -> some View`

Sets the visibility of the x axis.

`func chartXAxis<Content>(content: () -> Content) -> some View`

Configures the x-axis for charts in the view.

`func chartXAxisStyle<Content>(content: (ChartAxisContent) -> Content) -> some
View`

Configures the x axis content of charts.

`func chartYAxis<Content>(content: () -> Content) -> some View`

Configures the y-axis for charts in the view.

`func chartYAxisStyle<Content>(content: (ChartAxisContent) -> Content) -> some
View`

Configures the y axis content of charts.

Instance Method

# chartYAxis(content:)

Configures the y-axis for charts in the view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartYAxis<Content>(@AxisContentBuilder content: () -> Content) -> some View where Content : AxisContent
    

##  Parameters

`content`

    

The axis content.

## Discussion

Use this modifier to customize the y-axis of a chart. Provide an `AxisMarks`
builder that composes `AxisGridLine`, `AxisTick`, and `AxisValueLabel`
structures to form the axis. Omit components from the builder to omit them
from the resulting axis. For example, the following code adds grid lines to
the y-axis:

Use arguments such as `position:` or `values:` to control the placement of the
axis values it displays.

The above code customizes the y-axis to appear on the leading edge of the
chart, with a solid grid line at the 0% and 100% marks.

Note

To add an axis label, use one of the label modifiers, like
`chartYAxisLabel(position:alignment:spacing:content:)`.

## See Also

### Axes

`func chartXAxis(Visibility) -> some View`

Sets the visibility of the x axis.

`func chartXAxis<Content>(content: () -> Content) -> some View`

Configures the x-axis for charts in the view.

`func chartXAxisStyle<Content>(content: (ChartAxisContent) -> Content) -> some
View`

Configures the x axis content of charts.

`func chartYAxis(Visibility) -> some View`

Sets the visibility of the y axis.

`func chartYAxisStyle<Content>(content: (ChartAxisContent) -> Content) -> some
View`

Configures the y axis content of charts.

Instance Method

# chartYAxisStyle(content:)

Configures the y axis content of charts.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func chartYAxisStyle<Content>(@ViewBuilder content: @escaping (ChartAxisContent) -> Content) -> some View where Content : View
    

##  Parameters

`content`

    

A closure that returns the content of the axis.

## Discussion

Use this modifier to configure the size or aspect ratio of the plot area of
charts.

For example:

## See Also

### Axes

`func chartXAxis(Visibility) -> some View`

Sets the visibility of the x axis.

`func chartXAxis<Content>(content: () -> Content) -> some View`

Configures the x-axis for charts in the view.

`func chartXAxisStyle<Content>(content: (ChartAxisContent) -> Content) -> some
View`

Configures the x axis content of charts.

`func chartYAxis(Visibility) -> some View`

Sets the visibility of the y axis.

`func chartYAxis<Content>(content: () -> Content) -> some View`

Configures the y-axis for charts in the view.

Instance Method

# chartXAxisLabel(_:position:alignment:spacing:)

Adds x axis label for charts in the view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartXAxisLabel<S>(
        _ label: S,
        position: AnnotationPosition = .automatic,
        alignment: Alignment? = nil,
        spacing: CGFloat? = nil
    ) -> some View where S : StringProtocol
    

##  Parameters

`title`

    

The label string.

`position`

    

The position of the label.

`alignment`

    

The alignment of the label.

`spacing`

    

The spacing of the label from the axis markers.

## See Also

### Axis Labels

`func chartXAxisLabel(LocalizedStringKey, position: AnnotationPosition,
alignment: Alignment?, spacing: CGFloat?) -> some View`

Adds x axis label for charts in the view.

`func chartXAxisLabel<C>(position: AnnotationPosition, alignment: Alignment?,
spacing: CGFloat?, content: () -> C) -> some View`

Adds x axis label for charts in the view.

`func chartYAxisLabel<S>(S, position: AnnotationPosition, alignment:
Alignment?, spacing: CGFloat?) -> some View`

Adds y axis label for charts in the view.

`func chartYAxisLabel(LocalizedStringKey, position: AnnotationPosition,
alignment: Alignment?, spacing: CGFloat?) -> some View`

Adds y axis label for charts in the view.

`func chartYAxisLabel<C>(position: AnnotationPosition, alignment: Alignment?,
spacing: CGFloat?, content: () -> C) -> some View`

Adds y axis label for charts in the view.

Instance Method

# chartXAxisLabel(_:position:alignment:spacing:)

Adds x axis label for charts in the view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartXAxisLabel(
        _ labelKey: LocalizedStringKey,
        position: AnnotationPosition = .automatic,
        alignment: Alignment? = nil,
        spacing: CGFloat? = nil
    ) -> some View
    

##  Parameters

`labelKey`

    

The key for the localized label string.

`position`

    

The position of the label.

`alignment`

    

The alignment of the label.

`spacing`

    

The spacing of the label from the axis markers.

## See Also

### Axis Labels

`func chartXAxisLabel<S>(S, position: AnnotationPosition, alignment:
Alignment?, spacing: CGFloat?) -> some View`

Adds x axis label for charts in the view.

`func chartXAxisLabel<C>(position: AnnotationPosition, alignment: Alignment?,
spacing: CGFloat?, content: () -> C) -> some View`

Adds x axis label for charts in the view.

`func chartYAxisLabel<S>(S, position: AnnotationPosition, alignment:
Alignment?, spacing: CGFloat?) -> some View`

Adds y axis label for charts in the view.

`func chartYAxisLabel(LocalizedStringKey, position: AnnotationPosition,
alignment: Alignment?, spacing: CGFloat?) -> some View`

Adds y axis label for charts in the view.

`func chartYAxisLabel<C>(position: AnnotationPosition, alignment: Alignment?,
spacing: CGFloat?, content: () -> C) -> some View`

Adds y axis label for charts in the view.

Instance Method

# chartXAxisLabel(position:alignment:spacing:content:)

Adds x axis label for charts in the view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartXAxisLabel<C>(
        position: AnnotationPosition = .automatic,
        alignment: Alignment? = nil,
        spacing: CGFloat? = nil,
        @ViewBuilder content: () -> C
    ) -> some View where C : View
    

##  Parameters

`position`

    

The position of the label.

`alignment`

    

The alignment of the label.

`spacing`

    

The spacing of the label from the axis markers.

`content`

    

The label content.

## See Also

### Axis Labels

`func chartXAxisLabel<S>(S, position: AnnotationPosition, alignment:
Alignment?, spacing: CGFloat?) -> some View`

Adds x axis label for charts in the view.

`func chartXAxisLabel(LocalizedStringKey, position: AnnotationPosition,
alignment: Alignment?, spacing: CGFloat?) -> some View`

Adds x axis label for charts in the view.

`func chartYAxisLabel<S>(S, position: AnnotationPosition, alignment:
Alignment?, spacing: CGFloat?) -> some View`

Adds y axis label for charts in the view.

`func chartYAxisLabel(LocalizedStringKey, position: AnnotationPosition,
alignment: Alignment?, spacing: CGFloat?) -> some View`

Adds y axis label for charts in the view.

`func chartYAxisLabel<C>(position: AnnotationPosition, alignment: Alignment?,
spacing: CGFloat?, content: () -> C) -> some View`

Adds y axis label for charts in the view.

Instance Method

# chartYAxisLabel(_:position:alignment:spacing:)

Adds y axis label for charts in the view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartYAxisLabel<S>(
        _ label: S,
        position: AnnotationPosition = .automatic,
        alignment: Alignment? = nil,
        spacing: CGFloat? = nil
    ) -> some View where S : StringProtocol
    

##  Parameters

`label`

    

The label string.

`position`

    

The position of the label.

`alignment`

    

The alignment of the label.

`spacing`

    

The spacing of the label from the axis markers.

## See Also

### Axis Labels

`func chartXAxisLabel<S>(S, position: AnnotationPosition, alignment:
Alignment?, spacing: CGFloat?) -> some View`

Adds x axis label for charts in the view.

`func chartXAxisLabel(LocalizedStringKey, position: AnnotationPosition,
alignment: Alignment?, spacing: CGFloat?) -> some View`

Adds x axis label for charts in the view.

`func chartXAxisLabel<C>(position: AnnotationPosition, alignment: Alignment?,
spacing: CGFloat?, content: () -> C) -> some View`

Adds x axis label for charts in the view.

`func chartYAxisLabel(LocalizedStringKey, position: AnnotationPosition,
alignment: Alignment?, spacing: CGFloat?) -> some View`

Adds y axis label for charts in the view.

`func chartYAxisLabel<C>(position: AnnotationPosition, alignment: Alignment?,
spacing: CGFloat?, content: () -> C) -> some View`

Adds y axis label for charts in the view.

Instance Method

# chartYAxisLabel(_:position:alignment:spacing:)

Adds y axis label for charts in the view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartYAxisLabel(
        _ labelKey: LocalizedStringKey,
        position: AnnotationPosition = .automatic,
        alignment: Alignment? = nil,
        spacing: CGFloat? = nil
    ) -> some View
    

##  Parameters

`labelKey`

    

The key for the localized label string.

`position`

    

The position of the label.

`alignment`

    

The alignment of the label.

`spacing`

    

The spacing of the label from the axis markers.

## See Also

### Axis Labels

`func chartXAxisLabel<S>(S, position: AnnotationPosition, alignment:
Alignment?, spacing: CGFloat?) -> some View`

Adds x axis label for charts in the view.

`func chartXAxisLabel(LocalizedStringKey, position: AnnotationPosition,
alignment: Alignment?, spacing: CGFloat?) -> some View`

Adds x axis label for charts in the view.

`func chartXAxisLabel<C>(position: AnnotationPosition, alignment: Alignment?,
spacing: CGFloat?, content: () -> C) -> some View`

Adds x axis label for charts in the view.

`func chartYAxisLabel<S>(S, position: AnnotationPosition, alignment:
Alignment?, spacing: CGFloat?) -> some View`

Adds y axis label for charts in the view.

`func chartYAxisLabel<C>(position: AnnotationPosition, alignment: Alignment?,
spacing: CGFloat?, content: () -> C) -> some View`

Adds y axis label for charts in the view.

Instance Method

# chartYAxisLabel(position:alignment:spacing:content:)

Adds y axis label for charts in the view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartYAxisLabel<C>(
        position: AnnotationPosition = .automatic,
        alignment: Alignment? = nil,
        spacing: CGFloat? = nil,
        @ViewBuilder content: () -> C
    ) -> some View where C : View
    

##  Parameters

`position`

    

The position of the label.

`alignment`

    

The alignment of the label.

`spacing`

    

The spacing of the label from the axis markers.

`content`

    

The label content.

## See Also

### Axis Labels

`func chartXAxisLabel<S>(S, position: AnnotationPosition, alignment:
Alignment?, spacing: CGFloat?) -> some View`

Adds x axis label for charts in the view.

`func chartXAxisLabel(LocalizedStringKey, position: AnnotationPosition,
alignment: Alignment?, spacing: CGFloat?) -> some View`

Adds x axis label for charts in the view.

`func chartXAxisLabel<C>(position: AnnotationPosition, alignment: Alignment?,
spacing: CGFloat?, content: () -> C) -> some View`

Adds x axis label for charts in the view.

`func chartYAxisLabel<S>(S, position: AnnotationPosition, alignment:
Alignment?, spacing: CGFloat?) -> some View`

Adds y axis label for charts in the view.

`func chartYAxisLabel(LocalizedStringKey, position: AnnotationPosition,
alignment: Alignment?, spacing: CGFloat?) -> some View`

Adds y axis label for charts in the view.

Instance Method

# chartXScale(domain:range:type:)

Configures the x scale for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartXScale<Domain, Range>(
        domain: Domain,
        range: Range,
        type: ScaleType? = nil
    ) -> some View where Domain : ScaleDomain, Range : PositionScaleRange
    

##  Parameters

`domain`

    

The possible data values along the x axis in the chart. You can define the
domain with a `ClosedRange` for number or `Date` values (e.g., `0 ... 500`),
and with an array for categorical values (e.g., `["A", "B", "C"]`)

`range`

    

The range of x positions that correspond to the scale domain. By default the
range is determined by the dimension of the plot area. You can use `range:
.plotDimension(startPadding:, endPadding:)` to add padding to the scale range.

`type`

    

The scale type.

## See Also

### Axis scales

`func chartXScale<Domain>(domain: Domain, type: ScaleType?) -> some View`

Configures the x scale for charts.

`func chartXScale<Range>(range: Range, type: ScaleType?) -> some View`

Configures the x scale for charts.

`func chartXScale(type: ScaleType?) -> some View`

Configures the x scale for charts.

`func chartYScale<Domain, Range>(domain: Domain, range: Range, type:
ScaleType?) -> some View`

Configures the y scale for charts.

`func chartYScale<Domain>(domain: Domain, type: ScaleType?) -> some View`

Configures the y scale for charts.

`func chartYScale<Range>(range: Range, type: ScaleType?) -> some View`

Configures the y scale for charts.

`func chartYScale(type: ScaleType?) -> some View`

Configures the y scale for charts.

Instance Method

# chartXScale(domain:type:)

Configures the x scale for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartXScale<Domain>(
        domain: Domain,
        type: ScaleType? = nil
    ) -> some View where Domain : ScaleDomain
    

##  Parameters

`domain`

    

The possible data values along the x axis in the chart. You can define the
domain with a `ClosedRange` for number or `Date` values (e.g., `0 ... 500`),
and with an array for categorical values (e.g., `["A", "B", "C"]`)

`type`

    

The scale type.

## See Also

### Axis scales

`func chartXScale<Domain, Range>(domain: Domain, range: Range, type:
ScaleType?) -> some View`

Configures the x scale for charts.

`func chartXScale<Range>(range: Range, type: ScaleType?) -> some View`

Configures the x scale for charts.

`func chartXScale(type: ScaleType?) -> some View`

Configures the x scale for charts.

`func chartYScale<Domain, Range>(domain: Domain, range: Range, type:
ScaleType?) -> some View`

Configures the y scale for charts.

`func chartYScale<Domain>(domain: Domain, type: ScaleType?) -> some View`

Configures the y scale for charts.

`func chartYScale<Range>(range: Range, type: ScaleType?) -> some View`

Configures the y scale for charts.

`func chartYScale(type: ScaleType?) -> some View`

Configures the y scale for charts.

Instance Method

# chartXScale(range:type:)

Configures the x scale for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartXScale<Range>(
        range: Range,
        type: ScaleType? = nil
    ) -> some View where Range : PositionScaleRange
    

##  Parameters

`range`

    

The range of x positions that correspond to the scale domain. By default the
range is determined by the dimension of the plot area. You can use `range:
.plotDimension(startPadding:, endPadding:)` to add padding to the scale range.

`type`

    

The scale type.

## See Also

### Axis scales

`func chartXScale<Domain, Range>(domain: Domain, range: Range, type:
ScaleType?) -> some View`

Configures the x scale for charts.

`func chartXScale<Domain>(domain: Domain, type: ScaleType?) -> some View`

Configures the x scale for charts.

`func chartXScale(type: ScaleType?) -> some View`

Configures the x scale for charts.

`func chartYScale<Domain, Range>(domain: Domain, range: Range, type:
ScaleType?) -> some View`

Configures the y scale for charts.

`func chartYScale<Domain>(domain: Domain, type: ScaleType?) -> some View`

Configures the y scale for charts.

`func chartYScale<Range>(range: Range, type: ScaleType?) -> some View`

Configures the y scale for charts.

`func chartYScale(type: ScaleType?) -> some View`

Configures the y scale for charts.

Instance Method

# chartXScale(type:)

Configures the x scale for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartXScale(type: ScaleType? = nil) -> some View
    

##  Parameters

`type`

    

The scale type.

## See Also

### Axis scales

`func chartXScale<Domain, Range>(domain: Domain, range: Range, type:
ScaleType?) -> some View`

Configures the x scale for charts.

`func chartXScale<Domain>(domain: Domain, type: ScaleType?) -> some View`

Configures the x scale for charts.

`func chartXScale<Range>(range: Range, type: ScaleType?) -> some View`

Configures the x scale for charts.

`func chartYScale<Domain, Range>(domain: Domain, range: Range, type:
ScaleType?) -> some View`

Configures the y scale for charts.

`func chartYScale<Domain>(domain: Domain, type: ScaleType?) -> some View`

Configures the y scale for charts.

`func chartYScale<Range>(range: Range, type: ScaleType?) -> some View`

Configures the y scale for charts.

`func chartYScale(type: ScaleType?) -> some View`

Configures the y scale for charts.

Instance Method

# chartYScale(domain:range:type:)

Configures the y scale for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartYScale<Domain, Range>(
        domain: Domain,
        range: Range,
        type: ScaleType? = nil
    ) -> some View where Domain : ScaleDomain, Range : PositionScaleRange
    

##  Parameters

`domain`

    

The possible data values along the y axis in the chart. You can define the
domain with a `ClosedRange` for number or `Date` values (e.g., `0 ... 500`),
and with an array for categorical values (e.g., `["A", "B", "C"]`)

`range`

    

The range of y positions that correspond to the scale domain. By default the
range is determined by the dimension of the plot area. You can use `range:
.plotDimension(startPadding:, endPadding:)` to add padding to the scale range.

`type`

    

The scale type.

## See Also

### Axis scales

`func chartXScale<Domain, Range>(domain: Domain, range: Range, type:
ScaleType?) -> some View`

Configures the x scale for charts.

`func chartXScale<Domain>(domain: Domain, type: ScaleType?) -> some View`

Configures the x scale for charts.

`func chartXScale<Range>(range: Range, type: ScaleType?) -> some View`

Configures the x scale for charts.

`func chartXScale(type: ScaleType?) -> some View`

Configures the x scale for charts.

`func chartYScale<Domain>(domain: Domain, type: ScaleType?) -> some View`

Configures the y scale for charts.

`func chartYScale<Range>(range: Range, type: ScaleType?) -> some View`

Configures the y scale for charts.

`func chartYScale(type: ScaleType?) -> some View`

Configures the y scale for charts.

Instance Method

# chartYScale(domain:type:)

Configures the y scale for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartYScale<Domain>(
        domain: Domain,
        type: ScaleType? = nil
    ) -> some View where Domain : ScaleDomain
    

##  Parameters

`domain`

    

The possible data values along the y axis in the chart. You can define the
domain with a `ClosedRange` for number or `Date` values (e.g., `0 ... 500`),
and with an array for categorical values (e.g., `["A", "B", "C"]`)

`type`

    

The scale type.

## See Also

### Axis scales

`func chartXScale<Domain, Range>(domain: Domain, range: Range, type:
ScaleType?) -> some View`

Configures the x scale for charts.

`func chartXScale<Domain>(domain: Domain, type: ScaleType?) -> some View`

Configures the x scale for charts.

`func chartXScale<Range>(range: Range, type: ScaleType?) -> some View`

Configures the x scale for charts.

`func chartXScale(type: ScaleType?) -> some View`

Configures the x scale for charts.

`func chartYScale<Domain, Range>(domain: Domain, range: Range, type:
ScaleType?) -> some View`

Configures the y scale for charts.

`func chartYScale<Range>(range: Range, type: ScaleType?) -> some View`

Configures the y scale for charts.

`func chartYScale(type: ScaleType?) -> some View`

Configures the y scale for charts.

Instance Method

# chartYScale(range:type:)

Configures the y scale for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartYScale<Range>(
        range: Range,
        type: ScaleType? = nil
    ) -> some View where Range : PositionScaleRange
    

##  Parameters

`range`

    

The range of y positions that correspond to the scale domain. By default the
range is determined by the dimension of the plot area. You can use `range:
.plotDimension(startPadding:, endPadding:)` to add padding to the scale range.

`type`

    

The scale type.

## See Also

### Axis scales

`func chartXScale<Domain, Range>(domain: Domain, range: Range, type:
ScaleType?) -> some View`

Configures the x scale for charts.

`func chartXScale<Domain>(domain: Domain, type: ScaleType?) -> some View`

Configures the x scale for charts.

`func chartXScale<Range>(range: Range, type: ScaleType?) -> some View`

Configures the x scale for charts.

`func chartXScale(type: ScaleType?) -> some View`

Configures the x scale for charts.

`func chartYScale<Domain, Range>(domain: Domain, range: Range, type:
ScaleType?) -> some View`

Configures the y scale for charts.

`func chartYScale<Domain>(domain: Domain, type: ScaleType?) -> some View`

Configures the y scale for charts.

`func chartYScale(type: ScaleType?) -> some View`

Configures the y scale for charts.

Instance Method

# chartYScale(type:)

Configures the y scale for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartYScale(type: ScaleType? = nil) -> some View
    

##  Parameters

`type`

    

The scale type.

## See Also

### Axis scales

`func chartXScale<Domain, Range>(domain: Domain, range: Range, type:
ScaleType?) -> some View`

Configures the x scale for charts.

`func chartXScale<Domain>(domain: Domain, type: ScaleType?) -> some View`

Configures the x scale for charts.

`func chartXScale<Range>(range: Range, type: ScaleType?) -> some View`

Configures the x scale for charts.

`func chartXScale(type: ScaleType?) -> some View`

Configures the x scale for charts.

`func chartYScale<Domain, Range>(domain: Domain, range: Range, type:
ScaleType?) -> some View`

Configures the y scale for charts.

`func chartYScale<Domain>(domain: Domain, type: ScaleType?) -> some View`

Configures the y scale for charts.

`func chartYScale<Range>(range: Range, type: ScaleType?) -> some View`

Configures the y scale for charts.

Instance Method

# chartSymbolScale(_:)

Configures the symbol scale for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartSymbolScale<DataValue, S>(_ mapping: KeyValuePairs<DataValue, S>) -> some View where DataValue : Plottable, S : ChartSymbolShape
    

##  Parameters

`mapping`

    

Maps data categories to symbol shapes.

## See Also

### Symbol scales

`func chartSymbolScale<DataValue>(KeyValuePairs<DataValue, any
ChartSymbolShape>) -> some View`

Configures the symbol scale for charts.

`func chartSymbolScale<Domain>(domain: Domain) -> some View`

Configures the symbol style scale for charts.

`func chartSymbolScale<Domain, Range>(domain: Domain, range: Range) -> some
View`

Configures the symbol style scale for charts.

`func chartSymbolScale<Domain>(domain: Domain, range: [any ChartSymbolShape])
-> some View`

Configures the symbol style scale for charts.

`func chartSymbolScale<Domain, S>(domain: Domain, mapping: (Domain.Element) ->
S) -> some View`

Configures the symbol scale for charts.

`func chartSymbolScale<DataValue, S>(mapping: (DataValue) -> S) -> some View`

Configures the symbol scale for charts.

`func chartSymbolScale(range: [any ChartSymbolShape]) -> some View`

Configures the symbol style scale for charts.

`func chartSymbolScale<Range>(range: Range) -> some View`

Configures the symbol style scale for charts.

Instance Method

# chartSymbolScale(_:)

Configures the symbol scale for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartSymbolScale<DataValue>(_ mapping: KeyValuePairs<DataValue, any ChartSymbolShape>) -> some View where DataValue : Plottable
    

##  Parameters

`mapping`

    

Maps data categories to symbol shapes.

## See Also

### Symbol scales

`func chartSymbolScale<DataValue, S>(KeyValuePairs<DataValue, S>) -> some
View`

Configures the symbol scale for charts.

`func chartSymbolScale<Domain>(domain: Domain) -> some View`

Configures the symbol style scale for charts.

`func chartSymbolScale<Domain, Range>(domain: Domain, range: Range) -> some
View`

Configures the symbol style scale for charts.

`func chartSymbolScale<Domain>(domain: Domain, range: [any ChartSymbolShape])
-> some View`

Configures the symbol style scale for charts.

`func chartSymbolScale<Domain, S>(domain: Domain, mapping: (Domain.Element) ->
S) -> some View`

Configures the symbol scale for charts.

`func chartSymbolScale<DataValue, S>(mapping: (DataValue) -> S) -> some View`

Configures the symbol scale for charts.

`func chartSymbolScale(range: [any ChartSymbolShape]) -> some View`

Configures the symbol style scale for charts.

`func chartSymbolScale<Range>(range: Range) -> some View`

Configures the symbol style scale for charts.

Instance Method

# chartSymbolScale(domain:)

Configures the symbol style scale for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartSymbolScale<Domain>(domain: Domain) -> some View where Domain : ScaleDomain
    

##  Parameters

`domain`

    

The possible data values plotted as symbols in the chart. You can define the
domain with an array for categorical values (e.g., `["A", "B", "C"]`)

## See Also

### Symbol scales

`func chartSymbolScale<DataValue, S>(KeyValuePairs<DataValue, S>) -> some
View`

Configures the symbol scale for charts.

`func chartSymbolScale<DataValue>(KeyValuePairs<DataValue, any
ChartSymbolShape>) -> some View`

Configures the symbol scale for charts.

`func chartSymbolScale<Domain, Range>(domain: Domain, range: Range) -> some
View`

Configures the symbol style scale for charts.

`func chartSymbolScale<Domain>(domain: Domain, range: [any ChartSymbolShape])
-> some View`

Configures the symbol style scale for charts.

`func chartSymbolScale<Domain, S>(domain: Domain, mapping: (Domain.Element) ->
S) -> some View`

Configures the symbol scale for charts.

`func chartSymbolScale<DataValue, S>(mapping: (DataValue) -> S) -> some View`

Configures the symbol scale for charts.

`func chartSymbolScale(range: [any ChartSymbolShape]) -> some View`

Configures the symbol style scale for charts.

`func chartSymbolScale<Range>(range: Range) -> some View`

Configures the symbol style scale for charts.

Instance Method

# chartSymbolScale(domain:range:)

Configures the symbol style scale for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartSymbolScale<Domain, Range>(
        domain: Domain,
        range: Range
    ) -> some View where Domain : ScaleDomain, Range : ScaleRange, Range.VisualValue : ChartSymbolShape
    

##  Parameters

`domain`

    

The possible data values plotted as symbols in the chart. You can define the
domain with an array for categorical values (e.g., `["A", "B", "C"]`)

`range`

    

The range of symbols that correspond to the scale domain.

## See Also

### Symbol scales

`func chartSymbolScale<DataValue, S>(KeyValuePairs<DataValue, S>) -> some
View`

Configures the symbol scale for charts.

`func chartSymbolScale<DataValue>(KeyValuePairs<DataValue, any
ChartSymbolShape>) -> some View`

Configures the symbol scale for charts.

`func chartSymbolScale<Domain>(domain: Domain) -> some View`

Configures the symbol style scale for charts.

`func chartSymbolScale<Domain>(domain: Domain, range: [any ChartSymbolShape])
-> some View`

Configures the symbol style scale for charts.

`func chartSymbolScale<Domain, S>(domain: Domain, mapping: (Domain.Element) ->
S) -> some View`

Configures the symbol scale for charts.

`func chartSymbolScale<DataValue, S>(mapping: (DataValue) -> S) -> some View`

Configures the symbol scale for charts.

`func chartSymbolScale(range: [any ChartSymbolShape]) -> some View`

Configures the symbol style scale for charts.

`func chartSymbolScale<Range>(range: Range) -> some View`

Configures the symbol style scale for charts.

Instance Method

# chartSymbolScale(domain:range:)

Configures the symbol style scale for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartSymbolScale<Domain>(
        domain: Domain,
        range: [any ChartSymbolShape]
    ) -> some View where Domain : ScaleDomain
    

##  Parameters

`domain`

    

The possible data values plotted as symbols in the chart. You can define the
domain with an array for categorical values (e.g., `["A", "B", "C"]`)

`range`

    

The range of symbols that correspond to the scale domain.

## See Also

### Symbol scales

`func chartSymbolScale<DataValue, S>(KeyValuePairs<DataValue, S>) -> some
View`

Configures the symbol scale for charts.

`func chartSymbolScale<DataValue>(KeyValuePairs<DataValue, any
ChartSymbolShape>) -> some View`

Configures the symbol scale for charts.

`func chartSymbolScale<Domain>(domain: Domain) -> some View`

Configures the symbol style scale for charts.

`func chartSymbolScale<Domain, Range>(domain: Domain, range: Range) -> some
View`

Configures the symbol style scale for charts.

`func chartSymbolScale<Domain, S>(domain: Domain, mapping: (Domain.Element) ->
S) -> some View`

Configures the symbol scale for charts.

`func chartSymbolScale<DataValue, S>(mapping: (DataValue) -> S) -> some View`

Configures the symbol scale for charts.

`func chartSymbolScale(range: [any ChartSymbolShape]) -> some View`

Configures the symbol style scale for charts.

`func chartSymbolScale<Range>(range: Range) -> some View`

Configures the symbol style scale for charts.

Instance Method

# chartSymbolScale(domain:mapping:)

Configures the symbol scale for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartSymbolScale<Domain, S>(
        domain: Domain,
        mapping: @escaping (Domain.Element) -> S
    ) -> some View where Domain : Collection, S : ChartSymbolShape, Domain.Element : Plottable
    

##  Parameters

`domain`

    

The possible data values plotted as symbol in the chart.

`mapping`

    

Maps data categories to symbol shapes.

## See Also

### Symbol scales

`func chartSymbolScale<DataValue, S>(KeyValuePairs<DataValue, S>) -> some
View`

Configures the symbol scale for charts.

`func chartSymbolScale<DataValue>(KeyValuePairs<DataValue, any
ChartSymbolShape>) -> some View`

Configures the symbol scale for charts.

`func chartSymbolScale<Domain>(domain: Domain) -> some View`

Configures the symbol style scale for charts.

`func chartSymbolScale<Domain, Range>(domain: Domain, range: Range) -> some
View`

Configures the symbol style scale for charts.

`func chartSymbolScale<Domain>(domain: Domain, range: [any ChartSymbolShape])
-> some View`

Configures the symbol style scale for charts.

`func chartSymbolScale<DataValue, S>(mapping: (DataValue) -> S) -> some View`

Configures the symbol scale for charts.

`func chartSymbolScale(range: [any ChartSymbolShape]) -> some View`

Configures the symbol style scale for charts.

`func chartSymbolScale<Range>(range: Range) -> some View`

Configures the symbol style scale for charts.

Instance Method

# chartSymbolScale(mapping:)

Configures the symbol scale for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartSymbolScale<DataValue, S>(mapping: @escaping (DataValue) -> S) -> some View where DataValue : Plottable, S : ChartSymbolShape
    

##  Parameters

`mapping`

    

Maps data categories to symbol shapes.

## See Also

### Symbol scales

`func chartSymbolScale<DataValue, S>(KeyValuePairs<DataValue, S>) -> some
View`

Configures the symbol scale for charts.

`func chartSymbolScale<DataValue>(KeyValuePairs<DataValue, any
ChartSymbolShape>) -> some View`

Configures the symbol scale for charts.

`func chartSymbolScale<Domain>(domain: Domain) -> some View`

Configures the symbol style scale for charts.

`func chartSymbolScale<Domain, Range>(domain: Domain, range: Range) -> some
View`

Configures the symbol style scale for charts.

`func chartSymbolScale<Domain>(domain: Domain, range: [any ChartSymbolShape])
-> some View`

Configures the symbol style scale for charts.

`func chartSymbolScale<Domain, S>(domain: Domain, mapping: (Domain.Element) ->
S) -> some View`

Configures the symbol scale for charts.

`func chartSymbolScale(range: [any ChartSymbolShape]) -> some View`

Configures the symbol style scale for charts.

`func chartSymbolScale<Range>(range: Range) -> some View`

Configures the symbol style scale for charts.

Instance Method

# chartSymbolScale(range:)

Configures the symbol style scale for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartSymbolScale(range: [any ChartSymbolShape]) -> some View
    

##  Parameters

`range`

    

The range of symbols that correspond to the scale domain.

## See Also

### Symbol scales

`func chartSymbolScale<DataValue, S>(KeyValuePairs<DataValue, S>) -> some
View`

Configures the symbol scale for charts.

`func chartSymbolScale<DataValue>(KeyValuePairs<DataValue, any
ChartSymbolShape>) -> some View`

Configures the symbol scale for charts.

`func chartSymbolScale<Domain>(domain: Domain) -> some View`

Configures the symbol style scale for charts.

`func chartSymbolScale<Domain, Range>(domain: Domain, range: Range) -> some
View`

Configures the symbol style scale for charts.

`func chartSymbolScale<Domain>(domain: Domain, range: [any ChartSymbolShape])
-> some View`

Configures the symbol style scale for charts.

`func chartSymbolScale<Domain, S>(domain: Domain, mapping: (Domain.Element) ->
S) -> some View`

Configures the symbol scale for charts.

`func chartSymbolScale<DataValue, S>(mapping: (DataValue) -> S) -> some View`

Configures the symbol scale for charts.

`func chartSymbolScale<Range>(range: Range) -> some View`

Configures the symbol style scale for charts.

Instance Method

# chartSymbolScale(range:)

Configures the symbol style scale for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartSymbolScale<Range>(range: Range) -> some View where Range : ScaleRange, Range.VisualValue : ChartSymbolShape
    

##  Parameters

`range`

    

The range of symbols that correspond to the scale domain.

## See Also

### Symbol scales

`func chartSymbolScale<DataValue, S>(KeyValuePairs<DataValue, S>) -> some
View`

Configures the symbol scale for charts.

`func chartSymbolScale<DataValue>(KeyValuePairs<DataValue, any
ChartSymbolShape>) -> some View`

Configures the symbol scale for charts.

`func chartSymbolScale<Domain>(domain: Domain) -> some View`

Configures the symbol style scale for charts.

`func chartSymbolScale<Domain, Range>(domain: Domain, range: Range) -> some
View`

Configures the symbol style scale for charts.

`func chartSymbolScale<Domain>(domain: Domain, range: [any ChartSymbolShape])
-> some View`

Configures the symbol style scale for charts.

`func chartSymbolScale<Domain, S>(domain: Domain, mapping: (Domain.Element) ->
S) -> some View`

Configures the symbol scale for charts.

`func chartSymbolScale<DataValue, S>(mapping: (DataValue) -> S) -> some View`

Configures the symbol scale for charts.

`func chartSymbolScale(range: [any ChartSymbolShape]) -> some View`

Configures the symbol style scale for charts.

Instance Method

# chartSymbolSizeScale(_:)

Configures the symbol size scale for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartSymbolSizeScale<DataValue>(_ mapping: KeyValuePairs<DataValue, CGFloat>) -> some View where DataValue : Plottable
    

##  Parameters

`mapping`

    

Maps data categories to symbol sizes.

## See Also

### Symbol size scales

`func chartSymbolSizeScale<Domain, Range>(domain: Domain, range: Range, type:
ScaleType?) -> some View`

Configures the symbol size scale for charts.

`func chartSymbolSizeScale<Domain>(domain: Domain, type: ScaleType?) -> some
View`

Configures the symbol size scale for charts.

`func chartSymbolSizeScale<Domain>(domain: Domain, mapping: (Domain.Element)
-> CGFloat) -> some View`

Configures the symbol size scale for charts.

`func chartSymbolSizeScale<DataValue>(mapping: (DataValue) -> CGFloat) -> some
View`

Configures the symbol size scale for charts.

`func chartSymbolSizeScale<Range>(range: Range, type: ScaleType?) -> some
View`

Configures the symbol size scale for charts.

`func chartSymbolSizeScale(type: ScaleType?) -> some View`

Configures the symbol size scale for charts.

Instance Method

# chartSymbolSizeScale(domain:range:type:)

Configures the symbol size scale for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartSymbolSizeScale<Domain, Range>(
        domain: Domain,
        range: Range,
        type: ScaleType? = nil
    ) -> some View where Domain : ScaleDomain, Range : ScaleRange, Range.VisualValue == CGFloat
    

##  Parameters

`domain`

    

The possible data values plotted as symbol sizes in the chart. You can define
the domain with an array for categorical values (e.g., `["A", "B", "C"]`)

`range`

    

The range of symbol size that correspond to the scale domain.

`type`

    

The scale type.

## See Also

### Symbol size scales

`func chartSymbolSizeScale<DataValue>(KeyValuePairs<DataValue, CGFloat>) ->
some View`

Configures the symbol size scale for charts.

`func chartSymbolSizeScale<Domain>(domain: Domain, type: ScaleType?) -> some
View`

Configures the symbol size scale for charts.

`func chartSymbolSizeScale<Domain>(domain: Domain, mapping: (Domain.Element)
-> CGFloat) -> some View`

Configures the symbol size scale for charts.

`func chartSymbolSizeScale<DataValue>(mapping: (DataValue) -> CGFloat) -> some
View`

Configures the symbol size scale for charts.

`func chartSymbolSizeScale<Range>(range: Range, type: ScaleType?) -> some
View`

Configures the symbol size scale for charts.

`func chartSymbolSizeScale(type: ScaleType?) -> some View`

Configures the symbol size scale for charts.

Instance Method

# chartSymbolSizeScale(domain:type:)

Configures the symbol size scale for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartSymbolSizeScale<Domain>(
        domain: Domain,
        type: ScaleType? = nil
    ) -> some View where Domain : ScaleDomain
    

##  Parameters

`domain`

    

The possible data values plotted as symbol sizes in the chart. You can define
the domain with an array for categorical values (e.g., `["A", "B", "C"]`)

`type`

    

The scale type.

## See Also

### Symbol size scales

`func chartSymbolSizeScale<DataValue>(KeyValuePairs<DataValue, CGFloat>) ->
some View`

Configures the symbol size scale for charts.

`func chartSymbolSizeScale<Domain, Range>(domain: Domain, range: Range, type:
ScaleType?) -> some View`

Configures the symbol size scale for charts.

`func chartSymbolSizeScale<Domain>(domain: Domain, mapping: (Domain.Element)
-> CGFloat) -> some View`

Configures the symbol size scale for charts.

`func chartSymbolSizeScale<DataValue>(mapping: (DataValue) -> CGFloat) -> some
View`

Configures the symbol size scale for charts.

`func chartSymbolSizeScale<Range>(range: Range, type: ScaleType?) -> some
View`

Configures the symbol size scale for charts.

`func chartSymbolSizeScale(type: ScaleType?) -> some View`

Configures the symbol size scale for charts.

Instance Method

# chartSymbolSizeScale(domain:mapping:)

Configures the symbol size scale for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartSymbolSizeScale<Domain>(
        domain: Domain,
        mapping: @escaping (Domain.Element) -> CGFloat
    ) -> some View where Domain : Collection, Domain.Element : Plottable
    

##  Parameters

`domain`

    

The possible data values plotted as symbol size in the chart.

`mapping`

    

Maps data categories to symbol sizes.

## See Also

### Symbol size scales

`func chartSymbolSizeScale<DataValue>(KeyValuePairs<DataValue, CGFloat>) ->
some View`

Configures the symbol size scale for charts.

`func chartSymbolSizeScale<Domain, Range>(domain: Domain, range: Range, type:
ScaleType?) -> some View`

Configures the symbol size scale for charts.

`func chartSymbolSizeScale<Domain>(domain: Domain, type: ScaleType?) -> some
View`

Configures the symbol size scale for charts.

`func chartSymbolSizeScale<DataValue>(mapping: (DataValue) -> CGFloat) -> some
View`

Configures the symbol size scale for charts.

`func chartSymbolSizeScale<Range>(range: Range, type: ScaleType?) -> some
View`

Configures the symbol size scale for charts.

`func chartSymbolSizeScale(type: ScaleType?) -> some View`

Configures the symbol size scale for charts.

Instance Method

# chartSymbolSizeScale(mapping:)

Configures the symbol size scale for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartSymbolSizeScale<DataValue>(mapping: @escaping (DataValue) -> CGFloat) -> some View where DataValue : Plottable
    

##  Parameters

`mapping`

    

Maps data categories to symbol sizes.

## See Also

### Symbol size scales

`func chartSymbolSizeScale<DataValue>(KeyValuePairs<DataValue, CGFloat>) ->
some View`

Configures the symbol size scale for charts.

`func chartSymbolSizeScale<Domain, Range>(domain: Domain, range: Range, type:
ScaleType?) -> some View`

Configures the symbol size scale for charts.

`func chartSymbolSizeScale<Domain>(domain: Domain, type: ScaleType?) -> some
View`

Configures the symbol size scale for charts.

`func chartSymbolSizeScale<Domain>(domain: Domain, mapping: (Domain.Element)
-> CGFloat) -> some View`

Configures the symbol size scale for charts.

`func chartSymbolSizeScale<Range>(range: Range, type: ScaleType?) -> some
View`

Configures the symbol size scale for charts.

`func chartSymbolSizeScale(type: ScaleType?) -> some View`

Configures the symbol size scale for charts.

Instance Method

# chartSymbolSizeScale(range:type:)

Configures the symbol size scale for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartSymbolSizeScale<Range>(
        range: Range,
        type: ScaleType? = nil
    ) -> some View where Range : ScaleRange, Range.VisualValue == CGFloat
    

##  Parameters

`range`

    

The range of symbol size that correspond to the scale domain.

`type`

    

The scale type.

## See Also

### Symbol size scales

`func chartSymbolSizeScale<DataValue>(KeyValuePairs<DataValue, CGFloat>) ->
some View`

Configures the symbol size scale for charts.

`func chartSymbolSizeScale<Domain, Range>(domain: Domain, range: Range, type:
ScaleType?) -> some View`

Configures the symbol size scale for charts.

`func chartSymbolSizeScale<Domain>(domain: Domain, type: ScaleType?) -> some
View`

Configures the symbol size scale for charts.

`func chartSymbolSizeScale<Domain>(domain: Domain, mapping: (Domain.Element)
-> CGFloat) -> some View`

Configures the symbol size scale for charts.

`func chartSymbolSizeScale<DataValue>(mapping: (DataValue) -> CGFloat) -> some
View`

Configures the symbol size scale for charts.

`func chartSymbolSizeScale(type: ScaleType?) -> some View`

Configures the symbol size scale for charts.

Instance Method

# chartSymbolSizeScale(type:)

Configures the symbol size scale for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartSymbolSizeScale(type: ScaleType? = nil) -> some View
    

##  Parameters

`type`

    

The scale type.

## See Also

### Symbol size scales

`func chartSymbolSizeScale<DataValue>(KeyValuePairs<DataValue, CGFloat>) ->
some View`

Configures the symbol size scale for charts.

`func chartSymbolSizeScale<Domain, Range>(domain: Domain, range: Range, type:
ScaleType?) -> some View`

Configures the symbol size scale for charts.

`func chartSymbolSizeScale<Domain>(domain: Domain, type: ScaleType?) -> some
View`

Configures the symbol size scale for charts.

`func chartSymbolSizeScale<Domain>(domain: Domain, mapping: (Domain.Element)
-> CGFloat) -> some View`

Configures the symbol size scale for charts.

`func chartSymbolSizeScale<DataValue>(mapping: (DataValue) -> CGFloat) -> some
View`

Configures the symbol size scale for charts.

`func chartSymbolSizeScale<Range>(range: Range, type: ScaleType?) -> some
View`

Configures the symbol size scale for charts.

Instance Method

# chartLineStyleScale(_:)

Configures the line style scale for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartLineStyleScale<DataValue>(_ mapping: KeyValuePairs<DataValue, StrokeStyle>) -> some View where DataValue : Plottable
    

##  Parameters

`mapping`

    

Maps data categories to line styles.

## See Also

### Line style scales

`func chartLineStyleScale<Domain>(domain: Domain) -> some View`

Configures the line style scale for charts.

`func chartLineStyleScale<Domain, Range>(domain: Domain, range: Range) -> some
View`

Configures the line style scale for charts.

`func chartLineStyleScale<Range>(range: Range) -> some View`

Configures the line style scale for charts.

`func chartLineStyleScale<Domain>(domain: Domain, mapping: (Domain.Element) ->
StrokeStyle) -> some View`

Configures the line style scale for charts.

`func chartLineStyleScale<DataValue>(mapping: (DataValue) -> StrokeStyle) ->
some View`

Configures the line style scale for charts.

Instance Method

# chartLineStyleScale(domain:)

Configures the line style scale for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartLineStyleScale<Domain>(domain: Domain) -> some View where Domain : ScaleDomain
    

##  Parameters

`domain`

    

The possible data values plotted as line styles in the chart. You can define
the domain with an array for categorical values (e.g., `["A", "B", "C"]`)

## See Also

### Line style scales

`func chartLineStyleScale<DataValue>(KeyValuePairs<DataValue, StrokeStyle>) ->
some View`

Configures the line style scale for charts.

`func chartLineStyleScale<Domain, Range>(domain: Domain, range: Range) -> some
View`

Configures the line style scale for charts.

`func chartLineStyleScale<Range>(range: Range) -> some View`

Configures the line style scale for charts.

`func chartLineStyleScale<Domain>(domain: Domain, mapping: (Domain.Element) ->
StrokeStyle) -> some View`

Configures the line style scale for charts.

`func chartLineStyleScale<DataValue>(mapping: (DataValue) -> StrokeStyle) ->
some View`

Configures the line style scale for charts.

Instance Method

# chartLineStyleScale(domain:range:)

Configures the line style scale for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartLineStyleScale<Domain, Range>(
        domain: Domain,
        range: Range
    ) -> some View where Domain : ScaleDomain, Range : ScaleRange, Range.VisualValue == StrokeStyle
    

##  Parameters

`domain`

    

The possible data values plotted as line styles in the chart. You can define
the domain with an array for categorical values (e.g., `["A", "B", "C"]`)

`range`

    

The range of line styles that correspond to the scale domain.

## See Also

### Line style scales

`func chartLineStyleScale<DataValue>(KeyValuePairs<DataValue, StrokeStyle>) ->
some View`

Configures the line style scale for charts.

`func chartLineStyleScale<Domain>(domain: Domain) -> some View`

Configures the line style scale for charts.

`func chartLineStyleScale<Range>(range: Range) -> some View`

Configures the line style scale for charts.

`func chartLineStyleScale<Domain>(domain: Domain, mapping: (Domain.Element) ->
StrokeStyle) -> some View`

Configures the line style scale for charts.

`func chartLineStyleScale<DataValue>(mapping: (DataValue) -> StrokeStyle) ->
some View`

Configures the line style scale for charts.

Instance Method

# chartLineStyleScale(range:)

Configures the line style scale for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartLineStyleScale<Range>(range: Range) -> some View where Range : ScaleRange, Range.VisualValue == StrokeStyle
    

##  Parameters

`range`

    

The range of line styles that correspond to the scale domain.

## See Also

### Line style scales

`func chartLineStyleScale<DataValue>(KeyValuePairs<DataValue, StrokeStyle>) ->
some View`

Configures the line style scale for charts.

`func chartLineStyleScale<Domain>(domain: Domain) -> some View`

Configures the line style scale for charts.

`func chartLineStyleScale<Domain, Range>(domain: Domain, range: Range) -> some
View`

Configures the line style scale for charts.

`func chartLineStyleScale<Domain>(domain: Domain, mapping: (Domain.Element) ->
StrokeStyle) -> some View`

Configures the line style scale for charts.

`func chartLineStyleScale<DataValue>(mapping: (DataValue) -> StrokeStyle) ->
some View`

Configures the line style scale for charts.

Instance Method

# chartLineStyleScale(domain:mapping:)

Configures the line style scale for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartLineStyleScale<Domain>(
        domain: Domain,
        mapping: @escaping (Domain.Element) -> StrokeStyle
    ) -> some View where Domain : Collection, Domain.Element : Plottable
    

##  Parameters

`domain`

    

The possible data values plotted as line style in the chart.

`mapping`

    

Maps data categories to line styles.

## See Also

### Line style scales

`func chartLineStyleScale<DataValue>(KeyValuePairs<DataValue, StrokeStyle>) ->
some View`

Configures the line style scale for charts.

`func chartLineStyleScale<Domain>(domain: Domain) -> some View`

Configures the line style scale for charts.

`func chartLineStyleScale<Domain, Range>(domain: Domain, range: Range) -> some
View`

Configures the line style scale for charts.

`func chartLineStyleScale<Range>(range: Range) -> some View`

Configures the line style scale for charts.

`func chartLineStyleScale<DataValue>(mapping: (DataValue) -> StrokeStyle) ->
some View`

Configures the line style scale for charts.

Instance Method

# chartLineStyleScale(mapping:)

Configures the line style scale for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartLineStyleScale<DataValue>(mapping: @escaping (DataValue) -> StrokeStyle) -> some View where DataValue : Plottable
    

##  Parameters

`mapping`

    

Maps data categories to line styles.

## See Also

### Line style scales

`func chartLineStyleScale<DataValue>(KeyValuePairs<DataValue, StrokeStyle>) ->
some View`

Configures the line style scale for charts.

`func chartLineStyleScale<Domain>(domain: Domain) -> some View`

Configures the line style scale for charts.

`func chartLineStyleScale<Domain, Range>(domain: Domain, range: Range) -> some
View`

Configures the line style scale for charts.

`func chartLineStyleScale<Range>(range: Range) -> some View`

Configures the line style scale for charts.

`func chartLineStyleScale<Domain>(domain: Domain, mapping: (Domain.Element) ->
StrokeStyle) -> some View`

Configures the line style scale for charts.

Instance Method

# chartScrollPosition(initialX:)

Sets the initial scroll position along the x-axis. Once the user scrolls the
scroll view, the value provided to this modifier will have no effect.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func chartScrollPosition(initialX: some Plottable) -> some View
    

##  Parameters

`initialValue`

    

The initial scroll position as a value.

## See Also

### Scrolling

`func chartScrollPosition(initialY: some Plottable) -> some View`

Sets the initial scroll position along the y-axis. Once the user scrolls the
scroll view, the value provided to this modifier will have no effect.

`func chartScrollPosition(x: Binding<some Plottable>) -> some View`

Associates a binding to be updated when the chart scrolls along the x-axis.

`func chartScrollPosition(y: Binding<some Plottable>) -> some View`

Associates a binding to be updated when the chart scrolls along the y-axis.

`func chartScrollTargetBehavior(some ChartScrollTargetBehavior) -> some View`

Sets the scroll behavior of the scrollable chart.

`func chartScrollableAxes(Axis.Set) -> some View`

Configures the scrollable behavior of charts in this view.

Instance Method

# chartScrollPosition(initialY:)

Sets the initial scroll position along the y-axis. Once the user scrolls the
scroll view, the value provided to this modifier will have no effect.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func chartScrollPosition(initialY: some Plottable) -> some View
    

##  Parameters

`initialValue`

    

The initial scroll position as a value.

## See Also

### Scrolling

`func chartScrollPosition(initialX: some Plottable) -> some View`

Sets the initial scroll position along the x-axis. Once the user scrolls the
scroll view, the value provided to this modifier will have no effect.

`func chartScrollPosition(x: Binding<some Plottable>) -> some View`

Associates a binding to be updated when the chart scrolls along the x-axis.

`func chartScrollPosition(y: Binding<some Plottable>) -> some View`

Associates a binding to be updated when the chart scrolls along the y-axis.

`func chartScrollTargetBehavior(some ChartScrollTargetBehavior) -> some View`

Sets the scroll behavior of the scrollable chart.

`func chartScrollableAxes(Axis.Set) -> some View`

Configures the scrollable behavior of charts in this view.

Instance Method

# chartScrollPosition(x:)

Associates a binding to be updated when the chart scrolls along the x-axis.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func chartScrollPosition(x: Binding<some Plottable>) -> some View
    

##  Parameters

`value`

    

The scroll position as a value.

## See Also

### Scrolling

`func chartScrollPosition(initialX: some Plottable) -> some View`

Sets the initial scroll position along the x-axis. Once the user scrolls the
scroll view, the value provided to this modifier will have no effect.

`func chartScrollPosition(initialY: some Plottable) -> some View`

Sets the initial scroll position along the y-axis. Once the user scrolls the
scroll view, the value provided to this modifier will have no effect.

`func chartScrollPosition(y: Binding<some Plottable>) -> some View`

Associates a binding to be updated when the chart scrolls along the y-axis.

`func chartScrollTargetBehavior(some ChartScrollTargetBehavior) -> some View`

Sets the scroll behavior of the scrollable chart.

`func chartScrollableAxes(Axis.Set) -> some View`

Configures the scrollable behavior of charts in this view.

Instance Method

# chartScrollPosition(y:)

Associates a binding to be updated when the chart scrolls along the y-axis.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func chartScrollPosition(y: Binding<some Plottable>) -> some View
    

##  Parameters

`value`

    

The scroll position as a value.

## See Also

### Scrolling

`func chartScrollPosition(initialX: some Plottable) -> some View`

Sets the initial scroll position along the x-axis. Once the user scrolls the
scroll view, the value provided to this modifier will have no effect.

`func chartScrollPosition(initialY: some Plottable) -> some View`

Sets the initial scroll position along the y-axis. Once the user scrolls the
scroll view, the value provided to this modifier will have no effect.

`func chartScrollPosition(x: Binding<some Plottable>) -> some View`

Associates a binding to be updated when the chart scrolls along the x-axis.

`func chartScrollTargetBehavior(some ChartScrollTargetBehavior) -> some View`

Sets the scroll behavior of the scrollable chart.

`func chartScrollableAxes(Axis.Set) -> some View`

Configures the scrollable behavior of charts in this view.

Instance Method

# chartScrollTargetBehavior(_:)

Sets the scroll behavior of the scrollable chart.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func chartScrollTargetBehavior(_ behavior: some ChartScrollTargetBehavior) -> some View
    

##  Parameters

`behavior`

    

The chart scroll target behavior.

## Discussion

Use this method to control how the chart scrolls and aligns when the user
finishes scrolling. The example below sets the scroll target behavior to align
to the values in the chart. When the user finishes scrolling, the chart will
settle to align with the values in the chart.

## See Also

### Scrolling

`func chartScrollPosition(initialX: some Plottable) -> some View`

Sets the initial scroll position along the x-axis. Once the user scrolls the
scroll view, the value provided to this modifier will have no effect.

`func chartScrollPosition(initialY: some Plottable) -> some View`

Sets the initial scroll position along the y-axis. Once the user scrolls the
scroll view, the value provided to this modifier will have no effect.

`func chartScrollPosition(x: Binding<some Plottable>) -> some View`

Associates a binding to be updated when the chart scrolls along the x-axis.

`func chartScrollPosition(y: Binding<some Plottable>) -> some View`

Associates a binding to be updated when the chart scrolls along the y-axis.

`func chartScrollableAxes(Axis.Set) -> some View`

Configures the scrollable behavior of charts in this view.

Instance Method

# chartScrollableAxes(_:)

Configures the scrollable behavior of charts in this view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func chartScrollableAxes(_ axes: Axis.Set) -> some View
    

##  Parameters

`axes`

    

The set of axes to enable scrolling.

## Discussion

Use this method to make a chart scrollable. Below is an example that makes a
chart scrollable along the horizontal axis.

Note

When scrolling is enabled along an axis, a default portion of the chart will
be made visible. You can use the `chartXVisibleDomain` or
`chartYVisibleDomain` modifiers to configure the visible domain.

## See Also

### Scrolling

`func chartScrollPosition(initialX: some Plottable) -> some View`

Sets the initial scroll position along the x-axis. Once the user scrolls the
scroll view, the value provided to this modifier will have no effect.

`func chartScrollPosition(initialY: some Plottable) -> some View`

Sets the initial scroll position along the y-axis. Once the user scrolls the
scroll view, the value provided to this modifier will have no effect.

`func chartScrollPosition(x: Binding<some Plottable>) -> some View`

Associates a binding to be updated when the chart scrolls along the x-axis.

`func chartScrollPosition(y: Binding<some Plottable>) -> some View`

Associates a binding to be updated when the chart scrolls along the y-axis.

`func chartScrollTargetBehavior(some ChartScrollTargetBehavior) -> some View`

Sets the scroll behavior of the scrollable chart.

Instance Method

# chartXSelection(range:)

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func chartXSelection<P>(range: Binding<ClosedRange<P>?>) -> some View where P : Plottable, P : Comparable
    

## See Also

### Selection

`func chartXSelection<P>(value: Binding<P?>) -> some View`

`func chartYSelection<P>(range: Binding<ClosedRange<P>?>) -> some View`

`func chartYSelection<P>(value: Binding<P?>) -> some View`

`func chartAngleSelection<P>(value: Binding<P?>) -> some View`

Instance Method

# chartXSelection(value:)

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func chartXSelection<P>(value: Binding<P?>) -> some View where P : Plottable
    

## See Also

### Selection

`func chartXSelection<P>(range: Binding<ClosedRange<P>?>) -> some View`

`func chartYSelection<P>(range: Binding<ClosedRange<P>?>) -> some View`

`func chartYSelection<P>(value: Binding<P?>) -> some View`

`func chartAngleSelection<P>(value: Binding<P?>) -> some View`

Instance Method

# chartYSelection(range:)

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func chartYSelection<P>(range: Binding<ClosedRange<P>?>) -> some View where P : Plottable, P : Comparable
    

## See Also

### Selection

`func chartXSelection<P>(range: Binding<ClosedRange<P>?>) -> some View`

`func chartXSelection<P>(value: Binding<P?>) -> some View`

`func chartYSelection<P>(value: Binding<P?>) -> some View`

`func chartAngleSelection<P>(value: Binding<P?>) -> some View`

Instance Method

# chartYSelection(value:)

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func chartYSelection<P>(value: Binding<P?>) -> some View where P : Plottable
    

## See Also

### Selection

`func chartXSelection<P>(range: Binding<ClosedRange<P>?>) -> some View`

`func chartXSelection<P>(value: Binding<P?>) -> some View`

`func chartYSelection<P>(range: Binding<ClosedRange<P>?>) -> some View`

`func chartAngleSelection<P>(value: Binding<P?>) -> some View`

Instance Method

# chartAngleSelection(value:)

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func chartAngleSelection<P>(value: Binding<P?>) -> some View where P : Plottable
    

## See Also

### Selection

`func chartXSelection<P>(range: Binding<ClosedRange<P>?>) -> some View`

`func chartXSelection<P>(value: Binding<P?>) -> some View`

`func chartYSelection<P>(range: Binding<ClosedRange<P>?>) -> some View`

`func chartYSelection<P>(value: Binding<P?>) -> some View`

Instance Method

# chartXVisibleDomain(length:)

Sets the length of the visible domain in the X dimension.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func chartXVisibleDomain<P>(length: P) -> some View where P : Plottable, P : Numeric
    

##  Parameters

`length`

    

The length of the visible domain measured in data units. For categorical data,
this should be the number of visible categories.

## Discussion

Use this method to control how much of the chart is visible in a scrollable
chart. The example below sets the visible portion of the chart to 10 units in
the X axis.

## See Also

### Visible domain

`func chartYVisibleDomain<P>(length: P) -> some View`

Sets the length of the visible domain in the Y dimension.

Instance Method

# chartYVisibleDomain(length:)

Sets the length of the visible domain in the Y dimension.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func chartYVisibleDomain<P>(length: P) -> some View where P : Plottable, P : Numeric
    

##  Parameters

`length`

    

The length of the visible domain measured in data units. For categorical data,
this should be the number of visible categories.

## Discussion

Use this method to control how much of the chart is visible in a scrollable
chart. The example below sets the visible portion of the chart to 10 units in
the Y axis.

## See Also

### Visible domain

`func chartXVisibleDomain<P>(length: P) -> some View`

Sets the length of the visible domain in the X dimension.

Instance Method

# chartGesture(_:)

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func chartGesture(_ gesture: @escaping (ChartProxy) -> some Gesture) -> some View
    



# CircularGaugeStyle

Initializer

# init()

Creates a circular gauge.

watchOS 7.0+

    
    
    init()

## See Also

### Creating the gauge style

`init(tint: Color)`

Creates a circular gauge that draws with a specified color.

`init(tint: Gradient)`

Creates a circular gauge that draws with a specified gradient.

Initializer

# init(tint:)

Creates a circular gauge that draws with a specified color.

watchOS 7.0+

    
    
    init(tint: Color)

## See Also

### Creating the gauge style

`init()`

Creates a circular gauge.

`init(tint: Gradient)`

Creates a circular gauge that draws with a specified gradient.

Initializer

# init(tint:)

Creates a circular gauge that draws with a specified gradient.

watchOS 7.0+

    
    
    init(tint: Gradient)

## See Also

### Creating the gauge style

`init()`

Creates a circular gauge.

`init(tint: Color)`

Creates a circular gauge that draws with a specified color.



# Color.Resolved

Initializer

# init(colorSpace:red:green:blue:opacity:)

Creates a resolved color from red, green, and blue component values.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init(
        colorSpace: Color.RGBColorSpace = .sRGB,
        red: Float,
        green: Float,
        blue: Float,
        opacity: Float = 1
    )

##  Parameters

`colorSpace`

    

The profile that specifies how to interpret the color for display. The default
is `Color.RGBColorSpace.sRGB`.

`red`

    

The amount of red in the color.

`green`

    

The amount of green in the color.

`blue`

    

The amount of blue in the color.

`opacity`

    

An optional degree of opacity, given in the range `0` to `1`. A value of `0`
means 100% transparency, while a value of `1` means 100% opacity. The default
is `1`.

## Discussion

A standard sRGB color space clamps each color component — `red`, `green`, and
`blue` — to a range of `0` to `1`, but SwiftUI colors use an extended sRGB
color space, so you can use component values outside that range. This makes it
possible to create colors using the `Color.RGBColorSpace.sRGB` or
`Color.RGBColorSpace.sRGBLinear` color space that make full use of the wider
gamut of a diplay that supports `Color.RGBColorSpace.displayP3`.

Instance Property

# blue

The amount of blue in the color in the sRGB color space.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var blue: Float { get set }

Instance Property

# cgColor

A Core Graphics representation of the color.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var cgColor: CGColor { get }

## Discussion

You can get a `CGColor` instance from a resolved color.

Instance Property

# green

The amount of green in the color in the sRGB color space.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var green: Float { get set }

Instance Property

# linearBlue

The amount of blue in the color in the sRGB linear color space.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var linearBlue: Float

Instance Property

# linearGreen

The amount of green in the color in the sRGB linear color space.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var linearGreen: Float

Instance Property

# linearRed

The amount of red in the color in the sRGB linear color space.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var linearRed: Float

Instance Property

# opacity

The degree of opacity in the color, given in the range `0` to `1`.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var opacity: Float

## Discussion

A value of `0` means 100% transparency, while a value of `1` means 100%
opacity.

Instance Property

# red

The amount of red in the color in the sRGB color space.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var red: Float { get set }



# ContainerBackgroundPlacement

Type Property

# navigation

A background placement inside a `NavigationStack` or `NavigationSplitView`

watchOS 10.0+

    
    
    static let navigation: ContainerBackgroundPlacement

## See Also

### Getting placements

`static let tabView: ContainerBackgroundPlacement`

A background placement inside a `TabView`.

`static let widget: ContainerBackgroundPlacement`

The container background placement for a widget.

Type Property

# tabView

A background placement inside a `TabView`.

watchOS 10.0+

    
    
    static let tabView: ContainerBackgroundPlacement

## See Also

### Getting placements

`static let navigation: ContainerBackgroundPlacement`

A background placement inside a `NavigationStack` or `NavigationSplitView`

`static let widget: ContainerBackgroundPlacement`

The container background placement for a widget.

Type Property

# widget

The container background placement for a widget.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  watchOS 10.0+
visionOS 1.0+

    
    
    static let widget: ContainerBackgroundPlacement

## Discussion

Pass the container background placement to the `containerBackground(_:for:)`
function to configure the background of your widgets.

## See Also

### Getting placements

`static let navigation: ContainerBackgroundPlacement`

A background placement inside a `NavigationStack` or `NavigationSplitView`

`static let tabView: ContainerBackgroundPlacement`

A background placement inside a `TabView`.

Type Property

# subscriptionStore

A background placement inside a `SubscriptionStoreView`.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+

    
    
    static var subscriptionStore: ContainerBackgroundPlacement { get }

## See Also

### Getting StoreKit placements

`static var subscriptionStoreFullHeight: ContainerBackgroundPlacement`

A background placement that spans the full height of a
`SubscriptionStoreView`.

`static var subscriptionStoreHeader: ContainerBackgroundPlacement`

A background placement inside the marketing content of a
`SubscriptionStoreView`

Type Property

# subscriptionStoreFullHeight

A background placement that spans the full height of a
`SubscriptionStoreView`.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+

    
    
    static var subscriptionStoreFullHeight: ContainerBackgroundPlacement { get }

## See Also

### Getting StoreKit placements

`static var subscriptionStore: ContainerBackgroundPlacement`

A background placement inside a `SubscriptionStoreView`.

`static var subscriptionStoreHeader: ContainerBackgroundPlacement`

A background placement inside the marketing content of a
`SubscriptionStoreView`

Type Property

# subscriptionStoreHeader

A background placement inside the marketing content of a
`SubscriptionStoreView`

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+

    
    
    static var subscriptionStoreHeader: ContainerBackgroundPlacement { get }

## See Also

### Getting StoreKit placements

`static var subscriptionStore: ContainerBackgroundPlacement`

A background placement inside a `SubscriptionStoreView`.

`static var subscriptionStoreFullHeight: ContainerBackgroundPlacement`

A background placement that spans the full height of a
`SubscriptionStoreView`.



# Circle

Initializer

# init()

Creates a new circle shape.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init()



# ControlGroup

Initializer

# init(content:)

Creates a new ControlGroup with the specified children

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 17.0+  visionOS
1.0+

    
    
    init(@ViewBuilder content: () -> Content)

##  Parameters

`content`

    

the children to display

## See Also

### Creating a control group

`init<C, L>(content: () -> C, label: () -> L)`

Creates a new control group with the specified content and a label.

Available when `Content` conforms to `View`.

`init<C, S>(S, content: () -> C)`

Creates a new control group with the specified content that generates its
label from a string.

Available when `Content` conforms to `View`.

`init<C>(LocalizedStringKey, content: () -> C)`

Creates a new control group with the specified content that generates its
label from a localized string key.

Available when `Content` conforms to `View`.

Initializer

# init(content:label:)

Creates a new control group with the specified content and a label.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 17.0+  visionOS
1.0+

    
    
    init<C, L>(
        @ViewBuilder content: () -> C,
        @ViewBuilder label: () -> L
    ) where Content == LabeledControlGroupContent<C, L>, C : View, L : View

Available when `Content` conforms to `View`.

##  Parameters

`content`

    

The content to display.

`label`

    

A view that describes the purpose of the group.

## See Also

### Creating a control group

`init(content: () -> Content)`

Creates a new ControlGroup with the specified children

`init<C, S>(S, content: () -> C)`

Creates a new control group with the specified content that generates its
label from a string.

Available when `Content` conforms to `View`.

`init<C>(LocalizedStringKey, content: () -> C)`

Creates a new control group with the specified content that generates its
label from a localized string key.

Available when `Content` conforms to `View`.

Initializer

# init(_:content:)

Creates a new control group with the specified content that generates its
label from a string.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 17.0+  visionOS
1.0+

    
    
    init<C, S>(
        _ title: S,
        @ViewBuilder content: () -> C
    ) where Content == LabeledControlGroupContent<C, Text>, C : View, S : StringProtocol

Available when `Content` conforms to `View`.

##  Parameters

`title`

    

A string that describes the contents of the group.

`label`

    

A view that describes the purpose of the group.

## See Also

### Creating a control group

`init(content: () -> Content)`

Creates a new ControlGroup with the specified children

`init<C, L>(content: () -> C, label: () -> L)`

Creates a new control group with the specified content and a label.

Available when `Content` conforms to `View`.

`init<C>(LocalizedStringKey, content: () -> C)`

Creates a new control group with the specified content that generates its
label from a localized string key.

Available when `Content` conforms to `View`.

Initializer

# init(_:content:)

Creates a new control group with the specified content that generates its
label from a localized string key.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 17.0+  visionOS
1.0+

    
    
    init<C>(
        _ titleKey: LocalizedStringKey,
        @ViewBuilder content: () -> C
    ) where Content == LabeledControlGroupContent<C, Text>, C : View

Available when `Content` conforms to `View`.

##  Parameters

`titleKey`

    

The key for the group’s localized title, that describes the contents of the
group.

`label`

    

A view that describes the purpose of the group.

## See Also

### Creating a control group

`init(content: () -> Content)`

Creates a new ControlGroup with the specified children

`init<C, L>(content: () -> C, label: () -> L)`

Creates a new control group with the specified content and a label.

Available when `Content` conforms to `View`.

`init<C, S>(S, content: () -> C)`

Creates a new control group with the specified content that generates its
label from a string.

Available when `Content` conforms to `View`.

Initializer

# init(_:image:content:)

Creates a new control group with the specified content that generates its
label from a localized string key and image resource.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    init<C>(
        _ titleKey: LocalizedStringKey,
        image: ImageResource,
        @ViewBuilder content: () -> C
    ) where Content == LabeledControlGroupContent<C, Label<Text, Image>>, C : View

Available when `Content` conforms to `View`.

##  Parameters

`titleKey`

    

The key for the group’s localized title, that describes the contents of the
group.

`systemImage`

    

The name of the image resource to lookup.

`label`

    

A view that describes the purpose of the group.

## See Also

### Creating a control group with an image

`init<C, S>(S, image: ImageResource, content: () -> C)`

Creates a new control group with the specified content that generates its
label from a string and image name.

Available when `Content` conforms to `View`.

`init<C>(LocalizedStringKey, systemImage: String, content: () -> C)`

Creates a new control group with the specified content that generates its
label from a localized string key and image name.

Available when `Content` conforms to `View`.

`init<C, S>(S, systemImage: String, content: () -> C)`

Creates a new control group with the specified content that generates its
label from a string and image name.

Available when `Content` conforms to `View`.

Initializer

# init(_:image:content:)

Creates a new control group with the specified content that generates its
label from a string and image name.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    init<C, S>(
        _ title: S,
        image: ImageResource,
        @ViewBuilder content: () -> C
    ) where Content == LabeledControlGroupContent<C, Label<Text, Image>>, C : View, S : StringProtocol

Available when `Content` conforms to `View`.

##  Parameters

`title`

    

A string that describes the contents of the group.

`systemImage`

    

The name of the image resource to lookup.

`label`

    

A view that describes the purpose of the group.

## See Also

### Creating a control group with an image

`init<C>(LocalizedStringKey, image: ImageResource, content: () -> C)`

Creates a new control group with the specified content that generates its
label from a localized string key and image resource.

Available when `Content` conforms to `View`.

`init<C>(LocalizedStringKey, systemImage: String, content: () -> C)`

Creates a new control group with the specified content that generates its
label from a localized string key and image name.

Available when `Content` conforms to `View`.

`init<C, S>(S, systemImage: String, content: () -> C)`

Creates a new control group with the specified content that generates its
label from a string and image name.

Available when `Content` conforms to `View`.

Initializer

# init(_:systemImage:content:)

Creates a new control group with the specified content that generates its
label from a localized string key and image name.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 17.0+  visionOS
1.0+

    
    
    init<C>(
        _ titleKey: LocalizedStringKey,
        systemImage: String,
        @ViewBuilder content: () -> C
    ) where Content == LabeledControlGroupContent<C, Label<Text, Image>>, C : View

Available when `Content` conforms to `View`.

##  Parameters

`titleKey`

    

The key for the group’s localized title, that describes the contents of the
group.

`systemImage`

    

The name of the image resource to lookup.

`label`

    

A view that describes the purpose of the group.

## See Also

### Creating a control group with an image

`init<C>(LocalizedStringKey, image: ImageResource, content: () -> C)`

Creates a new control group with the specified content that generates its
label from a localized string key and image resource.

Available when `Content` conforms to `View`.

`init<C, S>(S, image: ImageResource, content: () -> C)`

Creates a new control group with the specified content that generates its
label from a string and image name.

Available when `Content` conforms to `View`.

`init<C, S>(S, systemImage: String, content: () -> C)`

Creates a new control group with the specified content that generates its
label from a string and image name.

Available when `Content` conforms to `View`.

Initializer

# init(_:systemImage:content:)

Creates a new control group with the specified content that generates its
label from a string and image name.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 17.0+  visionOS
1.0+

    
    
    init<C, S>(
        _ title: S,
        systemImage: String,
        @ViewBuilder content: () -> C
    ) where Content == LabeledControlGroupContent<C, Label<Text, Image>>, C : View, S : StringProtocol

Available when `Content` conforms to `View`.

##  Parameters

`title`

    

A string that describes the contents of the group.

`systemImage`

    

The name of the image resource to lookup.

`label`

    

A view that describes the purpose of the group.

## See Also

### Creating a control group with an image

`init<C>(LocalizedStringKey, image: ImageResource, content: () -> C)`

Creates a new control group with the specified content that generates its
label from a localized string key and image resource.

Available when `Content` conforms to `View`.

`init<C, S>(S, image: ImageResource, content: () -> C)`

Creates a new control group with the specified content that generates its
label from a string and image name.

Available when `Content` conforms to `View`.

`init<C>(LocalizedStringKey, systemImage: String, content: () -> C)`

Creates a new control group with the specified content that generates its
label from a localized string key and image name.

Available when `Content` conforms to `View`.

Initializer

# init(_:)

Creates a control group based on a style configuration.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 17.0+  visionOS
1.0+

    
    
    init(_ configuration: ControlGroupStyleConfiguration)

Available when `Content` is `ControlGroupStyleConfiguration.Content`.

## Discussion

Use this initializer within the `makeBody(configuration:)` method of a
`ControlGroupStyle` instance to create an instance of the control group being
styled. This is useful for custom control group styles that modify the current
control group style.

For example, the following code creates a new, custom style that places a red
border around the current control group:

Structure

# LabeledControlGroupContent

A view that represents the body of a control group with a specified label.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 17.0+  visionOS
1.0+

    
    
    struct LabeledControlGroupContent<Content, Label> where Content : View, Label : View

## Overview

You don’t create this type directly. SwiftUI creates it when you build a
`ControlGroup`.

## Relationships

### Conforms To

  * `View`



# CommandGroup

Initializer

# init(after:addition:)

A value describing the addition of the given views to the end of the indicated
group.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    init(
        after group: CommandGroupPlacement,
        @ViewBuilder addition: () -> Content
    )

## See Also

### Creating a command group

`init(before: CommandGroupPlacement, addition: () -> Content)`

A value describing the addition of the given views to the beginning of the
indicated group.

`init(replacing: CommandGroupPlacement, addition: () -> Content)`

A value describing the complete replacement of the contents of the indicated
group with the given views.

Initializer

# init(before:addition:)

A value describing the addition of the given views to the beginning of the
indicated group.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    init(
        before group: CommandGroupPlacement,
        @ViewBuilder addition: () -> Content
    )

## See Also

### Creating a command group

`init(after: CommandGroupPlacement, addition: () -> Content)`

A value describing the addition of the given views to the end of the indicated
group.

`init(replacing: CommandGroupPlacement, addition: () -> Content)`

A value describing the complete replacement of the contents of the indicated
group with the given views.

Initializer

# init(replacing:addition:)

A value describing the complete replacement of the contents of the indicated
group with the given views.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    init(
        replacing group: CommandGroupPlacement,
        @ViewBuilder addition: () -> Content
    )

## See Also

### Creating a command group

`init(after: CommandGroupPlacement, addition: () -> Content)`

A value describing the addition of the given views to the end of the indicated
group.

`init(before: CommandGroupPlacement, addition: () -> Content)`

A value describing the addition of the given views to the beginning of the
indicated group.



