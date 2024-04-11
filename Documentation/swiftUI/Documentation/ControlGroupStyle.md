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

