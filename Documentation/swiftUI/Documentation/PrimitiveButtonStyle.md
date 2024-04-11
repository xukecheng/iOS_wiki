Type Property

# automatic

The default button style, based on the button’s context.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static var automatic: DefaultButtonStyle { get }

Available when `Self` is `DefaultButtonStyle`.

## Discussion

If you create a button directly on a blank canvas, the style varies by
platform. iOS uses the borderless button style by default, whereas macOS,
tvOS, and watchOS use the bordered button style.

If you create a button inside a container, like a `List`, the style resolves
to the recommended style for buttons inside that container for that specific
platform.

You can override a button’s style. To apply the default style to a button, or
to a view that contains buttons, use the `buttonStyle(_:)` modifier.

## See Also

### Getting built-in button styles

`static var accessoryBar: AccessoryBarButtonStyle`

A button style that is typically used in the context of an accessory toolbar
(sometimes refererred to as a “scope bar”), for buttons that narrow the focus
of a search or other operation.

Available when `Self` is `AccessoryBarButtonStyle`.

`static var accessoryBarAction: AccessoryBarActionButtonStyle`

A button style that you use for extra actions in an accessory toolbar.

Available when `Self` is `AccessoryBarActionButtonStyle`.

`static var bordered: BorderedButtonStyle`

A button style that applies standard border artwork based on the button’s
context.

Available when `Self` is `BorderedButtonStyle`.

`static var borderedProminent: BorderedProminentButtonStyle`

A button style that applies standard border prominent artwork based on the
button’s context.

Available when `Self` is `BorderedProminentButtonStyle`.

`static var borderless: BorderlessButtonStyle`

A button style that doesn’t apply a border.

Available when `Self` is `BorderlessButtonStyle`.

`static var card: CardButtonStyle`

A button style that doesn’t pad the content, and applies a motion effect when
a button has focus.

Available when `Self` is `CardButtonStyle`.

`static var link: LinkButtonStyle`

A button style for buttons that emulate links.

Available when `Self` is `LinkButtonStyle`.

`static var plain: PlainButtonStyle`

A button style that doesn’t style or decorate its content while idle, but may
apply a visual effect to indicate the pressed, focused, or enabled state of
the button.

Available when `Self` is `PlainButtonStyle`.

Type Property

# accessoryBar

A button style that is typically used in the context of an accessory toolbar
(sometimes refererred to as a “scope bar”), for buttons that narrow the focus
of a search or other operation.

macOS 14.0+  visionOS 1.0+

    
    
    static var accessoryBar: AccessoryBarButtonStyle { get }

Available when `Self` is `AccessoryBarButtonStyle`.

## Discussion

This is the default button style for views in accessory toolbars, created with
`ToolbarItemPlacement.init(id:_)`, and for searchable scopes.

This style will also affect button style `Toggle`s, as well as button style
`Picker`s and `Menu`s.

## See Also

### Getting built-in button styles

`static var automatic: DefaultButtonStyle`

The default button style, based on the button’s context.

Available when `Self` is `DefaultButtonStyle`.

`static var accessoryBarAction: AccessoryBarActionButtonStyle`

A button style that you use for extra actions in an accessory toolbar.

Available when `Self` is `AccessoryBarActionButtonStyle`.

`static var bordered: BorderedButtonStyle`

A button style that applies standard border artwork based on the button’s
context.

Available when `Self` is `BorderedButtonStyle`.

`static var borderedProminent: BorderedProminentButtonStyle`

A button style that applies standard border prominent artwork based on the
button’s context.

Available when `Self` is `BorderedProminentButtonStyle`.

`static var borderless: BorderlessButtonStyle`

A button style that doesn’t apply a border.

Available when `Self` is `BorderlessButtonStyle`.

`static var card: CardButtonStyle`

A button style that doesn’t pad the content, and applies a motion effect when
a button has focus.

Available when `Self` is `CardButtonStyle`.

`static var link: LinkButtonStyle`

A button style for buttons that emulate links.

Available when `Self` is `LinkButtonStyle`.

`static var plain: PlainButtonStyle`

A button style that doesn’t style or decorate its content while idle, but may
apply a visual effect to indicate the pressed, focused, or enabled state of
the button.

Available when `Self` is `PlainButtonStyle`.

Type Property

# accessoryBarAction

A button style that you use for extra actions in an accessory toolbar.

macOS 14.0+  visionOS 1.0+

    
    
    static var accessoryBarAction: AccessoryBarActionButtonStyle { get }

Available when `Self` is `AccessoryBarActionButtonStyle`.

## Discussion

Use this style for buttons that perform extra actions relative to the
accessory toolbar’s main functions, like adding or editing filters. This style
also affects other view types that you apply a button style to, like `Toggle`,
`Picker`, and `Menu` instances.

## See Also

### Getting built-in button styles

`static var automatic: DefaultButtonStyle`

The default button style, based on the button’s context.

Available when `Self` is `DefaultButtonStyle`.

`static var accessoryBar: AccessoryBarButtonStyle`

A button style that is typically used in the context of an accessory toolbar
(sometimes refererred to as a “scope bar”), for buttons that narrow the focus
of a search or other operation.

Available when `Self` is `AccessoryBarButtonStyle`.

`static var bordered: BorderedButtonStyle`

A button style that applies standard border artwork based on the button’s
context.

Available when `Self` is `BorderedButtonStyle`.

`static var borderedProminent: BorderedProminentButtonStyle`

A button style that applies standard border prominent artwork based on the
button’s context.

Available when `Self` is `BorderedProminentButtonStyle`.

`static var borderless: BorderlessButtonStyle`

A button style that doesn’t apply a border.

Available when `Self` is `BorderlessButtonStyle`.

`static var card: CardButtonStyle`

A button style that doesn’t pad the content, and applies a motion effect when
a button has focus.

Available when `Self` is `CardButtonStyle`.

`static var link: LinkButtonStyle`

A button style for buttons that emulate links.

Available when `Self` is `LinkButtonStyle`.

`static var plain: PlainButtonStyle`

A button style that doesn’t style or decorate its content while idle, but may
apply a visual effect to indicate the pressed, focused, or enabled state of
the button.

Available when `Self` is `PlainButtonStyle`.

Type Property

# bordered

A button style that applies standard border artwork based on the button’s
context.

iOS 15.0+  iPadOS 15.0+  macOS 10.15+  Mac Catalyst 15.0+  tvOS 13.0+  watchOS
7.0+  visionOS 1.0+

    
    
    static var bordered: BorderedButtonStyle { get }

Available when `Self` is `BorderedButtonStyle`.

## Discussion

To apply this style to a button, or to a view that contains buttons, use the
`buttonStyle(_:)` modifier.

## See Also

### Getting built-in button styles

`static var automatic: DefaultButtonStyle`

The default button style, based on the button’s context.

Available when `Self` is `DefaultButtonStyle`.

`static var accessoryBar: AccessoryBarButtonStyle`

A button style that is typically used in the context of an accessory toolbar
(sometimes refererred to as a “scope bar”), for buttons that narrow the focus
of a search or other operation.

Available when `Self` is `AccessoryBarButtonStyle`.

`static var accessoryBarAction: AccessoryBarActionButtonStyle`

A button style that you use for extra actions in an accessory toolbar.

Available when `Self` is `AccessoryBarActionButtonStyle`.

`static var borderedProminent: BorderedProminentButtonStyle`

A button style that applies standard border prominent artwork based on the
button’s context.

Available when `Self` is `BorderedProminentButtonStyle`.

`static var borderless: BorderlessButtonStyle`

A button style that doesn’t apply a border.

Available when `Self` is `BorderlessButtonStyle`.

`static var card: CardButtonStyle`

A button style that doesn’t pad the content, and applies a motion effect when
a button has focus.

Available when `Self` is `CardButtonStyle`.

`static var link: LinkButtonStyle`

A button style for buttons that emulate links.

Available when `Self` is `LinkButtonStyle`.

`static var plain: PlainButtonStyle`

A button style that doesn’t style or decorate its content while idle, but may
apply a visual effect to indicate the pressed, focused, or enabled state of
the button.

Available when `Self` is `PlainButtonStyle`.

Type Property

# borderedProminent

A button style that applies standard border prominent artwork based on the
button’s context.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var borderedProminent: BorderedProminentButtonStyle { get }

Available when `Self` is `BorderedProminentButtonStyle`.

## Discussion

To apply this style to a button, or to a view that contains buttons, use the
`buttonStyle(_:)` modifier.

## See Also

### Getting built-in button styles

`static var automatic: DefaultButtonStyle`

The default button style, based on the button’s context.

Available when `Self` is `DefaultButtonStyle`.

`static var accessoryBar: AccessoryBarButtonStyle`

A button style that is typically used in the context of an accessory toolbar
(sometimes refererred to as a “scope bar”), for buttons that narrow the focus
of a search or other operation.

Available when `Self` is `AccessoryBarButtonStyle`.

`static var accessoryBarAction: AccessoryBarActionButtonStyle`

A button style that you use for extra actions in an accessory toolbar.

Available when `Self` is `AccessoryBarActionButtonStyle`.

`static var bordered: BorderedButtonStyle`

A button style that applies standard border artwork based on the button’s
context.

Available when `Self` is `BorderedButtonStyle`.

`static var borderless: BorderlessButtonStyle`

A button style that doesn’t apply a border.

Available when `Self` is `BorderlessButtonStyle`.

`static var card: CardButtonStyle`

A button style that doesn’t pad the content, and applies a motion effect when
a button has focus.

Available when `Self` is `CardButtonStyle`.

`static var link: LinkButtonStyle`

A button style for buttons that emulate links.

Available when `Self` is `LinkButtonStyle`.

`static var plain: PlainButtonStyle`

A button style that doesn’t style or decorate its content while idle, but may
apply a visual effect to indicate the pressed, focused, or enabled state of
the button.

Available when `Self` is `PlainButtonStyle`.

Type Property

# borderless

A button style that doesn’t apply a border.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 17.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var borderless: BorderlessButtonStyle { get }

Available when `Self` is `BorderlessButtonStyle`.

## Discussion

To apply this style to a button, or to a view that contains buttons, use the
`buttonStyle(_:)` modifier.

On tvOS, this button style adds a default hover effect to the first image of
the button’s content, if one exists. You can supply a different hover effect
by using the `hoverEffect(_:)` modifier in the button’s label.

## See Also

### Getting built-in button styles

`static var automatic: DefaultButtonStyle`

The default button style, based on the button’s context.

Available when `Self` is `DefaultButtonStyle`.

`static var accessoryBar: AccessoryBarButtonStyle`

A button style that is typically used in the context of an accessory toolbar
(sometimes refererred to as a “scope bar”), for buttons that narrow the focus
of a search or other operation.

Available when `Self` is `AccessoryBarButtonStyle`.

`static var accessoryBarAction: AccessoryBarActionButtonStyle`

A button style that you use for extra actions in an accessory toolbar.

Available when `Self` is `AccessoryBarActionButtonStyle`.

`static var bordered: BorderedButtonStyle`

A button style that applies standard border artwork based on the button’s
context.

Available when `Self` is `BorderedButtonStyle`.

`static var borderedProminent: BorderedProminentButtonStyle`

A button style that applies standard border prominent artwork based on the
button’s context.

Available when `Self` is `BorderedProminentButtonStyle`.

`static var card: CardButtonStyle`

A button style that doesn’t pad the content, and applies a motion effect when
a button has focus.

Available when `Self` is `CardButtonStyle`.

`static var link: LinkButtonStyle`

A button style for buttons that emulate links.

Available when `Self` is `LinkButtonStyle`.

`static var plain: PlainButtonStyle`

A button style that doesn’t style or decorate its content while idle, but may
apply a visual effect to indicate the pressed, focused, or enabled state of
the button.

Available when `Self` is `PlainButtonStyle`.

Type Property

# card

A button style that doesn’t pad the content, and applies a motion effect when
a button has focus.

tvOS 14.0+

    
    
    static var card: CardButtonStyle { get }

Available when `Self` is `CardButtonStyle`.

## Discussion

This style doesn’t apply padding to its contents, so images, text, and other
content display edge-to-edge. A button with this style appears partially
translucent. When the user focuses on a card button, the button animates up to
a raised position with more opacity. This style also applies the standard
background colors for unfocused and focused states in both light and dark
mode.

To apply this style to a button, or to a view that contains buttons, use the
`buttonStyle(_:)` modifier.

## See Also

### Getting built-in button styles

`static var automatic: DefaultButtonStyle`

The default button style, based on the button’s context.

Available when `Self` is `DefaultButtonStyle`.

`static var accessoryBar: AccessoryBarButtonStyle`

A button style that is typically used in the context of an accessory toolbar
(sometimes refererred to as a “scope bar”), for buttons that narrow the focus
of a search or other operation.

Available when `Self` is `AccessoryBarButtonStyle`.

`static var accessoryBarAction: AccessoryBarActionButtonStyle`

A button style that you use for extra actions in an accessory toolbar.

Available when `Self` is `AccessoryBarActionButtonStyle`.

`static var bordered: BorderedButtonStyle`

A button style that applies standard border artwork based on the button’s
context.

Available when `Self` is `BorderedButtonStyle`.

`static var borderedProminent: BorderedProminentButtonStyle`

A button style that applies standard border prominent artwork based on the
button’s context.

Available when `Self` is `BorderedProminentButtonStyle`.

`static var borderless: BorderlessButtonStyle`

A button style that doesn’t apply a border.

Available when `Self` is `BorderlessButtonStyle`.

`static var link: LinkButtonStyle`

A button style for buttons that emulate links.

Available when `Self` is `LinkButtonStyle`.

`static var plain: PlainButtonStyle`

A button style that doesn’t style or decorate its content while idle, but may
apply a visual effect to indicate the pressed, focused, or enabled state of
the button.

Available when `Self` is `PlainButtonStyle`.

Type Property

# link

A button style for buttons that emulate links.

macOS 10.15+

    
    
    static var link: LinkButtonStyle { get }

Available when `Self` is `LinkButtonStyle`.

## Discussion

To apply this style to a button, or to a view that contains buttons, use the
`buttonStyle(_:)` modifier.

## See Also

### Getting built-in button styles

`static var automatic: DefaultButtonStyle`

The default button style, based on the button’s context.

Available when `Self` is `DefaultButtonStyle`.

`static var accessoryBar: AccessoryBarButtonStyle`

A button style that is typically used in the context of an accessory toolbar
(sometimes refererred to as a “scope bar”), for buttons that narrow the focus
of a search or other operation.

Available when `Self` is `AccessoryBarButtonStyle`.

`static var accessoryBarAction: AccessoryBarActionButtonStyle`

A button style that you use for extra actions in an accessory toolbar.

Available when `Self` is `AccessoryBarActionButtonStyle`.

`static var bordered: BorderedButtonStyle`

A button style that applies standard border artwork based on the button’s
context.

Available when `Self` is `BorderedButtonStyle`.

`static var borderedProminent: BorderedProminentButtonStyle`

A button style that applies standard border prominent artwork based on the
button’s context.

Available when `Self` is `BorderedProminentButtonStyle`.

`static var borderless: BorderlessButtonStyle`

A button style that doesn’t apply a border.

Available when `Self` is `BorderlessButtonStyle`.

`static var card: CardButtonStyle`

A button style that doesn’t pad the content, and applies a motion effect when
a button has focus.

Available when `Self` is `CardButtonStyle`.

`static var plain: PlainButtonStyle`

A button style that doesn’t style or decorate its content while idle, but may
apply a visual effect to indicate the pressed, focused, or enabled state of
the button.

Available when `Self` is `PlainButtonStyle`.

Type Property

# plain

A button style that doesn’t style or decorate its content while idle, but may
apply a visual effect to indicate the pressed, focused, or enabled state of
the button.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static var plain: PlainButtonStyle { get }

Available when `Self` is `PlainButtonStyle`.

## Discussion

To apply this style to a button, or to a view that contains buttons, use the
`buttonStyle(_:)` modifier.

## See Also

### Getting built-in button styles

`static var automatic: DefaultButtonStyle`

The default button style, based on the button’s context.

Available when `Self` is `DefaultButtonStyle`.

`static var accessoryBar: AccessoryBarButtonStyle`

A button style that is typically used in the context of an accessory toolbar
(sometimes refererred to as a “scope bar”), for buttons that narrow the focus
of a search or other operation.

Available when `Self` is `AccessoryBarButtonStyle`.

`static var accessoryBarAction: AccessoryBarActionButtonStyle`

A button style that you use for extra actions in an accessory toolbar.

Available when `Self` is `AccessoryBarActionButtonStyle`.

`static var bordered: BorderedButtonStyle`

A button style that applies standard border artwork based on the button’s
context.

Available when `Self` is `BorderedButtonStyle`.

`static var borderedProminent: BorderedProminentButtonStyle`

A button style that applies standard border prominent artwork based on the
button’s context.

Available when `Self` is `BorderedProminentButtonStyle`.

`static var borderless: BorderlessButtonStyle`

A button style that doesn’t apply a border.

Available when `Self` is `BorderlessButtonStyle`.

`static var card: CardButtonStyle`

A button style that doesn’t pad the content, and applies a motion effect when
a button has focus.

Available when `Self` is `CardButtonStyle`.

`static var link: LinkButtonStyle`

A button style for buttons that emulate links.

Available when `Self` is `LinkButtonStyle`.

Instance Method

# makeBody(configuration:)

Creates a view that represents the body of a button.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @ViewBuilder
    func makeBody(configuration: Self.Configuration) -> Self.Body

**Required**

##  Parameters

`configuration `

    

The properties of the button.

## Discussion

The system calls this method for each `Button` instance in a view hierarchy
where this style is the current button style.

## See Also

### Creating custom button styles

`typealias Configuration`

The properties of a button.

`associatedtype Body : View`

A view that represents the body of a button.

**Required**

Type Alias

# PrimitiveButtonStyle.Configuration

The properties of a button.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    typealias Configuration = PrimitiveButtonStyleConfiguration

## See Also

### Creating custom button styles

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Creates a view that represents the body of a button.

**Required**

` associatedtype Body : View`

A view that represents the body of a button.

**Required**

Associated Type

# Body

A view that represents the body of a button.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    associatedtype Body : View

**Required**

## See Also

### Creating custom button styles

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Creates a view that represents the body of a button.

**Required**

` typealias Configuration`

The properties of a button.

Structure

# DefaultButtonStyle

The default button style, based on the button’s context.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    struct DefaultButtonStyle

## Overview

You can also use `automatic` to construct this style.

## Topics

### Creating the button style

`init()`

Creates a default button style.

### Supporting types

`func makeBody(configuration: DefaultButtonStyle.Configuration) -> some View`

Creates a view that represents the body of a button.

## Relationships

### Conforms To

  * `PrimitiveButtonStyle`

## See Also

### Supporting types

`struct AccessoryBarButtonStyle`

A button style that you use for actions in an accessory toolbar that narrow
the focus of a search or other operation.

`struct AccessoryBarActionButtonStyle`

A button style that you use for extra actions in an accessory toolbar.

`struct BorderedButtonStyle`

A button style that applies standard border artwork based on the button’s
context.

`struct BorderedProminentButtonStyle`

A button style that applies standard border prominent artwork based on the
button’s context.

`struct BorderlessButtonStyle`

A button style that doesn’t apply a border.

`struct CardButtonStyle`

A button style that doesn’t pad the content, and applies a motion effect when
a button has focus.

`struct LinkButtonStyle`

A button style for buttons that emulate links.

`struct PlainButtonStyle`

A button style that doesn’t style or decorate its content while idle, but may
apply a visual effect to indicate the pressed, focused, or enabled state of
the button.

Structure

# AccessoryBarButtonStyle

A button style that you use for actions in an accessory toolbar that narrow
the focus of a search or other operation.

macOS 14.0+  visionOS 1.0+

    
    
    struct AccessoryBarButtonStyle

## Overview

This is the default button style for views in accessory toolbars, which you
create with `init(id:)`, and for searchable scopes. This style also affects
other view types that you apply a button style to, like `Toggle`, `Picker`,
and `Menu` instances.

Use `accessoryBar` to construct this style.

## Topics

### Creating the button style

`init()`

Creates an accessory toolbar style

### Supporting types

`func makeBody(configuration: AccessoryBarButtonStyle.Configuration) -> some
View`

Creates a view that represents the body of a button.

## Relationships

### Conforms To

  * `PrimitiveButtonStyle`

## See Also

### Supporting types

`struct DefaultButtonStyle`

The default button style, based on the button’s context.

`struct AccessoryBarActionButtonStyle`

A button style that you use for extra actions in an accessory toolbar.

`struct BorderedButtonStyle`

A button style that applies standard border artwork based on the button’s
context.

`struct BorderedProminentButtonStyle`

A button style that applies standard border prominent artwork based on the
button’s context.

`struct BorderlessButtonStyle`

A button style that doesn’t apply a border.

`struct CardButtonStyle`

A button style that doesn’t pad the content, and applies a motion effect when
a button has focus.

`struct LinkButtonStyle`

A button style for buttons that emulate links.

`struct PlainButtonStyle`

A button style that doesn’t style or decorate its content while idle, but may
apply a visual effect to indicate the pressed, focused, or enabled state of
the button.

Structure

# AccessoryBarActionButtonStyle

A button style that you use for extra actions in an accessory toolbar.

macOS 14.0+  visionOS 1.0+

    
    
    struct AccessoryBarActionButtonStyle

## Overview

Use this style for buttons that perform extra actions relative to the
accessory toolbar’s main functions, like adding or editing filters. This style
also affects other view types that you apply a button style to, like `Toggle`,
`Picker`, and `Menu` instances.

Use `accessoryBarAction` to construct this style.

## Topics

### Creating the button style

`init()`

Creates an accessory toolbar action button style

### Supporting types

`func makeBody(configuration: AccessoryBarActionButtonStyle.Configuration) ->
some View`

Creates a view that represents the body of a button.

## Relationships

### Conforms To

  * `PrimitiveButtonStyle`

## See Also

### Supporting types

`struct DefaultButtonStyle`

The default button style, based on the button’s context.

`struct AccessoryBarButtonStyle`

A button style that you use for actions in an accessory toolbar that narrow
the focus of a search or other operation.

`struct BorderedButtonStyle`

A button style that applies standard border artwork based on the button’s
context.

`struct BorderedProminentButtonStyle`

A button style that applies standard border prominent artwork based on the
button’s context.

`struct BorderlessButtonStyle`

A button style that doesn’t apply a border.

`struct CardButtonStyle`

A button style that doesn’t pad the content, and applies a motion effect when
a button has focus.

`struct LinkButtonStyle`

A button style for buttons that emulate links.

`struct PlainButtonStyle`

A button style that doesn’t style or decorate its content while idle, but may
apply a visual effect to indicate the pressed, focused, or enabled state of
the button.

Structure

# BorderedButtonStyle

A button style that applies standard border artwork based on the button’s
context.

iOS 15.0+  iPadOS 15.0+  macOS 10.15+  Mac Catalyst 15.0+  tvOS 13.0+  watchOS
7.0+  visionOS 1.0+

    
    
    struct BorderedButtonStyle

## Overview

You can also use `bordered` to construct this style.

## Topics

### Creating the button style

`init()`

Creates a bordered button style.

### Supporting types

`func makeBody(configuration: BorderedButtonStyle.Configuration) -> some View`

Creates a view that represents the body of a button.

### Deprecated symbols

`init(tint: Color)`

Creates a bordered button style with a tint color.

Deprecated

## Relationships

### Conforms To

  * `PrimitiveButtonStyle`

## See Also

### Supporting types

`struct DefaultButtonStyle`

The default button style, based on the button’s context.

`struct AccessoryBarButtonStyle`

A button style that you use for actions in an accessory toolbar that narrow
the focus of a search or other operation.

`struct AccessoryBarActionButtonStyle`

A button style that you use for extra actions in an accessory toolbar.

`struct BorderedProminentButtonStyle`

A button style that applies standard border prominent artwork based on the
button’s context.

`struct BorderlessButtonStyle`

A button style that doesn’t apply a border.

`struct CardButtonStyle`

A button style that doesn’t pad the content, and applies a motion effect when
a button has focus.

`struct LinkButtonStyle`

A button style for buttons that emulate links.

`struct PlainButtonStyle`

A button style that doesn’t style or decorate its content while idle, but may
apply a visual effect to indicate the pressed, focused, or enabled state of
the button.

Structure

# BorderedProminentButtonStyle

A button style that applies standard border prominent artwork based on the
button’s context.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    struct BorderedProminentButtonStyle

## Overview

Use `borderedProminent` to construct this style.

## Topics

### Creating the button style

`init()`

Creates a bordered prominent button style.

## Relationships

### Conforms To

  * `PrimitiveButtonStyle`

## See Also

### Supporting types

`struct DefaultButtonStyle`

The default button style, based on the button’s context.

`struct AccessoryBarButtonStyle`

A button style that you use for actions in an accessory toolbar that narrow
the focus of a search or other operation.

`struct AccessoryBarActionButtonStyle`

A button style that you use for extra actions in an accessory toolbar.

`struct BorderedButtonStyle`

A button style that applies standard border artwork based on the button’s
context.

`struct BorderlessButtonStyle`

A button style that doesn’t apply a border.

`struct CardButtonStyle`

A button style that doesn’t pad the content, and applies a motion effect when
a button has focus.

`struct LinkButtonStyle`

A button style for buttons that emulate links.

`struct PlainButtonStyle`

A button style that doesn’t style or decorate its content while idle, but may
apply a visual effect to indicate the pressed, focused, or enabled state of
the button.

Structure

# BorderlessButtonStyle

A button style that doesn’t apply a border.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 17.0+  watchOS
8.0+  visionOS 1.0+

    
    
    struct BorderlessButtonStyle

## Overview

You can also use `borderless` to construct this style.

## Topics

### Creating the button style

`init()`

Creates a borderless button style.

### Supporting types

`func makeBody(configuration: BorderlessButtonStyle.Configuration) -> some
View`

Creates a view that represents the body of a button.

## Relationships

### Conforms To

  * `PrimitiveButtonStyle`

## See Also

### Supporting types

`struct DefaultButtonStyle`

The default button style, based on the button’s context.

`struct AccessoryBarButtonStyle`

A button style that you use for actions in an accessory toolbar that narrow
the focus of a search or other operation.

`struct AccessoryBarActionButtonStyle`

A button style that you use for extra actions in an accessory toolbar.

`struct BorderedButtonStyle`

A button style that applies standard border artwork based on the button’s
context.

`struct BorderedProminentButtonStyle`

A button style that applies standard border prominent artwork based on the
button’s context.

`struct CardButtonStyle`

A button style that doesn’t pad the content, and applies a motion effect when
a button has focus.

`struct LinkButtonStyle`

A button style for buttons that emulate links.

`struct PlainButtonStyle`

A button style that doesn’t style or decorate its content while idle, but may
apply a visual effect to indicate the pressed, focused, or enabled state of
the button.

Structure

# CardButtonStyle

A button style that doesn’t pad the content, and applies a motion effect when
a button has focus.

tvOS 14.0+

    
    
    struct CardButtonStyle

## Overview

You can also use `card` to construct this style.

## Topics

### Creating the button style

`init()`

Creates a style that doesn’t pad a button’s content and applies a motion
effect to a focused button.

### Supporting types

`func makeBody(configuration: CardButtonStyle.Configuration) -> some View`

Creates a view that represents the body of a button.

## Relationships

### Conforms To

  * `PrimitiveButtonStyle`

## See Also

### Related Documentation

`class TVCardView`

A view that responds to focus interaction with a motion effect it applies to
all of its subviews.

### Supporting types

`struct DefaultButtonStyle`

The default button style, based on the button’s context.

`struct AccessoryBarButtonStyle`

A button style that you use for actions in an accessory toolbar that narrow
the focus of a search or other operation.

`struct AccessoryBarActionButtonStyle`

A button style that you use for extra actions in an accessory toolbar.

`struct BorderedButtonStyle`

A button style that applies standard border artwork based on the button’s
context.

`struct BorderedProminentButtonStyle`

A button style that applies standard border prominent artwork based on the
button’s context.

`struct BorderlessButtonStyle`

A button style that doesn’t apply a border.

`struct LinkButtonStyle`

A button style for buttons that emulate links.

`struct PlainButtonStyle`

A button style that doesn’t style or decorate its content while idle, but may
apply a visual effect to indicate the pressed, focused, or enabled state of
the button.

Structure

# LinkButtonStyle

A button style for buttons that emulate links.

macOS 10.15+

    
    
    struct LinkButtonStyle

## Overview

You can also use `link` to construct this style.

## Topics

### Creating the button style

`init()`

Creates a link button style.

### Supporting types

`func makeBody(configuration: LinkButtonStyle.Configuration) -> some View`

Creates a view that represents the body of a button.

## Relationships

### Conforms To

  * `PrimitiveButtonStyle`

## See Also

### Supporting types

`struct DefaultButtonStyle`

The default button style, based on the button’s context.

`struct AccessoryBarButtonStyle`

A button style that you use for actions in an accessory toolbar that narrow
the focus of a search or other operation.

`struct AccessoryBarActionButtonStyle`

A button style that you use for extra actions in an accessory toolbar.

`struct BorderedButtonStyle`

A button style that applies standard border artwork based on the button’s
context.

`struct BorderedProminentButtonStyle`

A button style that applies standard border prominent artwork based on the
button’s context.

`struct BorderlessButtonStyle`

A button style that doesn’t apply a border.

`struct CardButtonStyle`

A button style that doesn’t pad the content, and applies a motion effect when
a button has focus.

`struct PlainButtonStyle`

A button style that doesn’t style or decorate its content while idle, but may
apply a visual effect to indicate the pressed, focused, or enabled state of
the button.

Structure

# PlainButtonStyle

A button style that doesn’t style or decorate its content while idle, but may
apply a visual effect to indicate the pressed, focused, or enabled state of
the button.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    struct PlainButtonStyle

## Overview

You can also use `plain` to construct this style.

## Topics

### Creating the button style

`init()`

Creates a plain button style.

### Supporting types

`func makeBody(configuration: PlainButtonStyle.Configuration) -> some View`

Creates a view that represents the body of a button.

## Relationships

### Conforms To

  * `PrimitiveButtonStyle`

## See Also

### Supporting types

`struct DefaultButtonStyle`

The default button style, based on the button’s context.

`struct AccessoryBarButtonStyle`

A button style that you use for actions in an accessory toolbar that narrow
the focus of a search or other operation.

`struct AccessoryBarActionButtonStyle`

A button style that you use for extra actions in an accessory toolbar.

`struct BorderedButtonStyle`

A button style that applies standard border artwork based on the button’s
context.

`struct BorderedProminentButtonStyle`

A button style that applies standard border prominent artwork based on the
button’s context.

`struct BorderlessButtonStyle`

A button style that doesn’t apply a border.

`struct CardButtonStyle`

A button style that doesn’t pad the content, and applies a motion effect when
a button has focus.

`struct LinkButtonStyle`

A button style for buttons that emulate links.

