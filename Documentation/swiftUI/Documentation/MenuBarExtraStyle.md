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

