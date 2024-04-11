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

