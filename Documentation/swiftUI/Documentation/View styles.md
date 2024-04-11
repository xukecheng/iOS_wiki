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

Protocol

# ButtonStyle

A type that applies standard interaction behavior and a custom appearance to
all buttons within a view hierarchy.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    protocol ButtonStyle

## Overview

To configure the current button style for a view hierarchy, use the
`buttonStyle(_:)` modifier. Specify a style that conforms to `ButtonStyle`
when creating a button that uses the standard button interaction behavior
defined for each platform. To create a button with custom interaction
behavior, use `PrimitiveButtonStyle` instead.

## Topics

### Custom button styles

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Creates a view that represents the body of a button.

**Required**

` typealias Configuration`

The properties of a button.

`associatedtype Body : View`

A view that represents the body of a button.

**Required**

## See Also

### Styling buttons

`func buttonStyle<S>(S) -> some View`

Sets the style for buttons within this view to a button style with a custom
appearance and standard interaction behavior.

`struct ButtonStyleConfiguration`

The properties of a button.

`func buttonStyle<S>(S) -> some View`

Sets the style for buttons within this view to a button style with a custom
appearance and custom interaction behavior.

`protocol PrimitiveButtonStyle`

A type that applies custom interaction behavior and a custom appearance to all
buttons within a view hierarchy.

`struct PrimitiveButtonStyleConfiguration`

The properties of a button.

`func signInWithAppleButtonStyle(SignInWithAppleButton.Style) -> some View`

Sets the style used for displaying the control (see
`SignInWithAppleButton.Style`).

Structure

# ButtonStyleConfiguration

The properties of a button.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    struct ButtonStyleConfiguration

## Topics

### Configuring a button’s label

`let label: ButtonStyleConfiguration.Label`

A view that describes the effect of pressing the button.

`struct Label`

A type-erased label of a button.

### Configuring a button’s interaction state

`let isPressed: Bool`

A Boolean that indicates whether the user is currently pressing the button.

### Defining the button’s purpose

`let role: ButtonRole?`

An optional semantic role that describes the button’s purpose.

## See Also

### Styling buttons

`func buttonStyle<S>(S) -> some View`

Sets the style for buttons within this view to a button style with a custom
appearance and standard interaction behavior.

`protocol ButtonStyle`

A type that applies standard interaction behavior and a custom appearance to
all buttons within a view hierarchy.

`func buttonStyle<S>(S) -> some View`

Sets the style for buttons within this view to a button style with a custom
appearance and custom interaction behavior.

`protocol PrimitiveButtonStyle`

A type that applies custom interaction behavior and a custom appearance to all
buttons within a view hierarchy.

`struct PrimitiveButtonStyleConfiguration`

The properties of a button.

`func signInWithAppleButtonStyle(SignInWithAppleButton.Style) -> some View`

Sets the style used for displaying the control (see
`SignInWithAppleButton.Style`).

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

Protocol

# PrimitiveButtonStyle

A type that applies custom interaction behavior and a custom appearance to all
buttons within a view hierarchy.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    protocol PrimitiveButtonStyle

## Overview

To configure the current button style for a view hierarchy, use the
`buttonStyle(_:)` modifier. Specify a style that conforms to
`PrimitiveButtonStyle` to create a button with custom interaction behavior. To
create a button with the standard button interaction behavior defined for each
platform, use `ButtonStyle` instead.

## Topics

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

`static var plain: PlainButtonStyle`

A button style that doesn’t style or decorate its content while idle, but may
apply a visual effect to indicate the pressed, focused, or enabled state of
the button.

Available when `Self` is `PlainButtonStyle`.

### Creating custom button styles

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Creates a view that represents the body of a button.

**Required**

` typealias Configuration`

The properties of a button.

`associatedtype Body : View`

A view that represents the body of a button.

**Required**

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

`struct PlainButtonStyle`

A button style that doesn’t style or decorate its content while idle, but may
apply a visual effect to indicate the pressed, focused, or enabled state of
the button.

## Relationships

### Conforming Types

  * `AccessoryBarActionButtonStyle`
  * `AccessoryBarButtonStyle`
  * `BorderedButtonStyle`
  * `BorderedProminentButtonStyle`
  * `BorderlessButtonStyle`
  * `CardButtonStyle`
  * `DefaultButtonStyle`
  * `LinkButtonStyle`
  * `PlainButtonStyle`

## See Also

### Styling buttons

`func buttonStyle<S>(S) -> some View`

Sets the style for buttons within this view to a button style with a custom
appearance and standard interaction behavior.

`protocol ButtonStyle`

A type that applies standard interaction behavior and a custom appearance to
all buttons within a view hierarchy.

`struct ButtonStyleConfiguration`

The properties of a button.

`func buttonStyle<S>(S) -> some View`

Sets the style for buttons within this view to a button style with a custom
appearance and custom interaction behavior.

`struct PrimitiveButtonStyleConfiguration`

The properties of a button.

`func signInWithAppleButtonStyle(SignInWithAppleButton.Style) -> some View`

Sets the style used for displaying the control (see
`SignInWithAppleButton.Style`).

Structure

# PrimitiveButtonStyleConfiguration

The properties of a button.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    struct PrimitiveButtonStyleConfiguration

## Topics

### Configuring a button’s label

`let label: PrimitiveButtonStyleConfiguration.Label`

A view that describes the effect of calling the button’s action.

`struct Label`

A type-erased label of a button.

### Initiating a button’s action

`func trigger()`

Performs the button’s action.

### Defining the button’s purpose

`let role: ButtonRole?`

An optional semantic role describing the button’s purpose.

## See Also

### Styling buttons

`func buttonStyle<S>(S) -> some View`

Sets the style for buttons within this view to a button style with a custom
appearance and standard interaction behavior.

`protocol ButtonStyle`

A type that applies standard interaction behavior and a custom appearance to
all buttons within a view hierarchy.

`struct ButtonStyleConfiguration`

The properties of a button.

`func buttonStyle<S>(S) -> some View`

Sets the style for buttons within this view to a button style with a custom
appearance and custom interaction behavior.

`protocol PrimitiveButtonStyle`

A type that applies custom interaction behavior and a custom appearance to all
buttons within a view hierarchy.

`func signInWithAppleButtonStyle(SignInWithAppleButton.Style) -> some View`

Sets the style used for displaying the control (see
`SignInWithAppleButton.Style`).

Instance Method

# signInWithAppleButtonStyle(_:)

Sets the style used for displaying the control (see
`SignInWithAppleButton.Style`).

AuthenticationServices  SwiftUI  iOS 14.0+  iPadOS 14.0+  macOS 11.0+  tvOS
14.0+  watchOS 7.0+

    
    
    func signInWithAppleButtonStyle(_ style: SignInWithAppleButton.Style) -> some View
    

##  Parameters

`style`

    

The sign in style to apply to this button.

## See Also

### Authorizing and authenticating

`struct LocalAuthenticationView`

A SwiftUI view that displays an authentication interface.

`struct SignInWithAppleButton`

The view that creates the Sign in with Apple button for display.

`var authorizationController: AuthorizationController`

A value provided in the SwiftUI environment that views can use to perform
authorization requests.

`var webAuthenticationSession: WebAuthenticationSession`

A value provided in the SwiftUI environment that views can use to authenticate
a user through a web service.

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

Protocol

# PickerStyle

A type that specifies the appearance and interaction of all pickers within a
view hierarchy.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    protocol PickerStyle

## Topics

### Getting built-in picker styles

`static var automatic: DefaultPickerStyle`

The default picker style, based on the picker’s context.

Available when `Self` is `DefaultPickerStyle`.

`static var inline: InlinePickerStyle`

A `PickerStyle` where each option is displayed inline with other views in the
current container.

Available when `Self` is `InlinePickerStyle`.

`static var menu: MenuPickerStyle`

A picker style that presents the options as a menu when the user presses a
button, or as a submenu when nested within a larger menu.

Available when `Self` is `MenuPickerStyle`.

`static var navigationLink: NavigationLinkPickerStyle`

A picker style represented by a navigation link that presents the options by
pushing a List-style picker view.

Available when `Self` is `NavigationLinkPickerStyle`.

`static var palette: PalettePickerStyle`

A picker style that presents the options as a row of compact elements.

Available when `Self` is `PalettePickerStyle`.

`static var radioGroup: RadioGroupPickerStyle`

A picker style that presents the options as a group of radio buttons.

Available when `Self` is `RadioGroupPickerStyle`.

`static var segmented: SegmentedPickerStyle`

A picker style that presents the options in a segmented control.

Available when `Self` is `SegmentedPickerStyle`.

`static var wheel: WheelPickerStyle`

A picker style that presents the options in a scrollable wheel that shows the
selected option and a few neighboring options.

Available when `Self` is `WheelPickerStyle`.

### Supporting types

`struct DefaultPickerStyle`

The default picker style, based on the picker’s context.

`struct InlinePickerStyle`

A `PickerStyle` where each option is displayed inline with other views in the
current container.

`struct MenuPickerStyle`

A picker style that presents the options as a menu when the user presses a
button, or as a submenu when nested within a larger menu.

`struct NavigationLinkPickerStyle`

A picker style represented by a navigation link that presents the options by
pushing a List-style picker view.

`struct PalettePickerStyle`

A picker style that presents the options as a row of compact elements.

`struct RadioGroupPickerStyle`

A picker style that presents the options as a group of radio buttons.

`struct SegmentedPickerStyle`

A picker style that presents the options in a segmented control.

`struct WheelPickerStyle`

A picker style that presents the options in a scrollable wheel that shows the
selected option and a few neighboring options.

### Deprecated styles

`struct PopUpButtonPickerStyle`

A picker style that presents the options as a menu when the user presses a
button.

Deprecated

## Relationships

### Conforming Types

  * `DefaultPickerStyle`
  * `InlinePickerStyle`
  * `MenuPickerStyle`
  * `NavigationLinkPickerStyle`
  * `PalettePickerStyle`
  * `PopUpButtonPickerStyle`
  * `RadioGroupPickerStyle`
  * `SegmentedPickerStyle`
  * `WheelPickerStyle`

## See Also

### Styling pickers

`func pickerStyle<S>(S) -> some View`

Sets the style for pickers within this view.

`func datePickerStyle<S>(S) -> some View`

Sets the style for date pickers within this view.

`protocol DatePickerStyle`

A type that specifies the appearance and interaction of all date pickers
within a view hierarchy.

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

Protocol

# DatePickerStyle

A type that specifies the appearance and interaction of all date pickers
within a view hierarchy.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 10.0+
visionOS 1.0+

    
    
    protocol DatePickerStyle

## Overview

To configure the current date picker style for a view hierarchy, use the
`datePickerStyle(_:)` modifier.

## Topics

### Getting built-in date picker styles

`static var automatic: DefaultDatePickerStyle`

The default style for date pickers.

Available when `Self` is `DefaultDatePickerStyle`.

`static var compact: CompactDatePickerStyle`

A date picker style that displays the components in a compact, textual format.

Available when `Self` is `CompactDatePickerStyle`.

`static var field: FieldDatePickerStyle`

A date picker style that displays the components in an editable field.

Available when `Self` is `FieldDatePickerStyle`.

`static var graphical: GraphicalDatePickerStyle`

A date picker style that displays an interactive calendar or clock.

Available when `Self` is `GraphicalDatePickerStyle`.

`static var stepperField: StepperFieldDatePickerStyle`

A system style that displays the components in an editable field, with
adjoining stepper that can increment/decrement the selected component.

Available when `Self` is `StepperFieldDatePickerStyle`.

`static var wheel: WheelDatePickerStyle`

A date picker style that displays each component as columns in a scrollable
wheel.

Available when `Self` is `WheelDatePickerStyle`.

### Creating custom date picker styles

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Returns the appearance and interaction content for a `DatePicker`.

**Required**

` struct DatePickerStyleConfiguration`

The properties of a `DatePicker`.

`typealias Configuration`

A type alias for the properties of a `DatePicker`.

`associatedtype Body : View`

A view representing the appearance and interaction of a `DatePicker`.

**Required**

### Suporting types

`struct DefaultDatePickerStyle`

The default style for date pickers.

`struct CompactDatePickerStyle`

A date picker style that displays the components in a compact, textual format.

`struct FieldDatePickerStyle`

A date picker style that displays the components in an editable field.

`struct GraphicalDatePickerStyle`

A date picker style that displays an interactive calendar or clock.

`struct StepperFieldDatePickerStyle`

A system style that displays the components in an editable field, with
adjoining stepper that can increment/decrement the selected component.

`struct WheelDatePickerStyle`

A date picker style that displays each component as columns in a scrollable
wheel.

## Relationships

### Conforming Types

  * `CompactDatePickerStyle`
  * `DefaultDatePickerStyle`
  * `FieldDatePickerStyle`
  * `GraphicalDatePickerStyle`
  * `StepperFieldDatePickerStyle`
  * `WheelDatePickerStyle`

## See Also

### Styling pickers

`func pickerStyle<S>(S) -> some View`

Sets the style for pickers within this view.

`protocol PickerStyle`

A type that specifies the appearance and interaction of all pickers within a
view hierarchy.

`func datePickerStyle<S>(S) -> some View`

Sets the style for date pickers within this view.

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

Protocol

# MenuStyle

A type that applies standard interaction behavior and a custom appearance to
all menus within a view hierarchy.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 17.0+  visionOS
1.0+

    
    
    protocol MenuStyle

## Overview

To configure the current menu style for a view hierarchy, use the
`menuStyle(_:)` modifier.

## Topics

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

`static var borderlessButton: BorderlessButtonMenuStyle`

A menu style that displays a borderless button that toggles the display of the
menu’s contents when pressed.

Available when `Self` is `BorderlessButtonMenuStyle`.

Deprecated

### Creating custom menu styles

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Creates a view that represents the body of a menu.

**Required**

` typealias Configuration`

The properties of a menu.

`associatedtype Body : View`

A view that represents the body of a menu.

**Required**

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

`struct BorderedButtonMenuStyle`

A menu style that displays a bordered button that toggles the display of the
menu’s contents when pressed.

Deprecated

## Relationships

### Conforming Types

  * `BorderedButtonMenuStyle`
  * `BorderlessButtonMenuStyle`
  * `ButtonMenuStyle`
  * `DefaultMenuStyle`

## See Also

### Styling menus

`func menuStyle<S>(S) -> some View`

Sets the style for menus within this view.

`struct MenuStyleConfiguration`

A configuration of a menu.

Structure

# MenuStyleConfiguration

A configuration of a menu.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 17.0+  visionOS
1.0+

    
    
    struct MenuStyleConfiguration

## Overview

Use the `init(_:)` initializer of `Menu` to create an instance using the
current menu style, which you can modify to create a custom style.

For example, the following code creates a new, custom style that adds a red
border to the current menu style:

## Topics

### Setting the label and content

`struct Label`

A type-erased label of a menu.

`struct Content`

A type-erased content of a menu.

## See Also

### Styling menus

`func menuStyle<S>(S) -> some View`

Sets the style for menus within this view.

`protocol MenuStyle`

A type that applies standard interaction behavior and a custom appearance to
all menus within a view hierarchy.

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

Protocol

# ToggleStyle

The appearance and behavior of a toggle.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    protocol ToggleStyle

## Overview

To configure the style for a single `Toggle` or for all toggle instances in a
view hierarchy, use the `toggleStyle(_:)` modifier. You can specify one of the
built-in toggle styles, like `switch` or `button`:

Alternatively, you can create and apply a custom style.

### Custom styles

To create a custom style, declare a type that conforms to the `ToggleStyle`
protocol and implement the required `makeBody(configuration:)` method. For
example, you can define a checklist toggle style:

Inside the method, use the `configuration` parameter, which is an instance of
the `ToggleStyleConfiguration` structure, to get the label and a binding to
the toggle state. To see examples of how to use these items to construct a
view that has the appearance and behavior of a toggle, see
`makeBody(configuration:)`.

To provide easy access to the new style, declare a corresponding static
variable in an extension to `ToggleStyle`:

You can then use your custom style:

## Topics

### Getting built-in toggle styles

`static var automatic: DefaultToggleStyle`

The default toggle style.

Available when `Self` is `DefaultToggleStyle`.

`static var button: ButtonToggleStyle`

A toggle style that displays as a button with its label as the title.

Available when `Self` is `ButtonToggleStyle`.

`static var checkbox: CheckboxToggleStyle`

A toggle style that displays a checkbox followed by its label.

Available when `Self` is `CheckboxToggleStyle`.

`static var `switch`: SwitchToggleStyle`

A toggle style that displays a leading label and a trailing switch.

Available when `Self` is `SwitchToggleStyle`.

### Creating custom toggle styles

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Creates a view that represents the body of a toggle.

**Required**

` struct ToggleStyleConfiguration`

The properties of a toggle instance.

`typealias Configuration`

The properties of a toggle instance.

`associatedtype Body : View`

A view that represents the appearance and interaction of a toggle.

**Required**

### Supporting types

`struct DefaultToggleStyle`

The default toggle style.

`struct ButtonToggleStyle`

A toggle style that displays as a button with its label as the title.

`struct CheckboxToggleStyle`

A toggle style that displays a checkbox followed by its label.

`struct SwitchToggleStyle`

A toggle style that displays a leading label and a trailing switch.

## Relationships

### Conforming Types

  * `ButtonToggleStyle`
  * `CheckboxToggleStyle`
  * `DefaultToggleStyle`
  * `SwitchToggleStyle`

## See Also

### Styling toggles

`func toggleStyle<S>(S) -> some View`

Sets the style for toggles in a view hierarchy.

`struct ToggleStyleConfiguration`

The properties of a toggle instance.

Structure

# ToggleStyleConfiguration

The properties of a toggle instance.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    struct ToggleStyleConfiguration

## Overview

When you define a custom toggle style by creating a type that conforms to the
`ToggleStyle` protocol, you implement the `makeBody(configuration:)` method.
That method takes a `ToggleStyleConfiguration` input that has the information
you need to define the behavior and appearance of a `Toggle`.

The configuration structure’s `label` reflects the toggle’s content, which
might be the value that you supply to the `label` parameter of the
`init(isOn:label:)` initializer. Alternatively, it could be another view that
SwiftUI builds from an initializer that takes a string input, like
`init(_:isOn:)`. In either case, incorporate the label into the toggle’s view
to help the user understand what the toggle does. For example, the built-in
`switch` style horizontally stacks the label with the control element.

The structure’s `isOn` property provides a `Binding` to the state of the
toggle. Adjust the appearance of the toggle based on this value. For example,
the built-in `button` style fills the button’s background when the property is
`true`, but leaves the background empty when the property is `false`. Change
the value when the user performs an action that’s meant to change the toggle,
like the button does when tapped or clicked by the user.

## Topics

### Getting the label view

`let label: ToggleStyleConfiguration.Label`

A view that describes the effect of switching the toggle between states.

`struct Label`

A type-erased label of a toggle.

### Managing the toggle state

`var isMixed: Bool`

Whether the `Toggle` is currently in a mixed state.

`var isOn: Bool`

A binding to a state property that indicates whether the toggle is on.

`var $isOn: Binding<Bool>`

## See Also

### Styling toggles

`func toggleStyle<S>(S) -> some View`

Sets the style for toggles in a view hierarchy.

`protocol ToggleStyle`

The appearance and behavior of a toggle.

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

Protocol

# GaugeStyle

Defines the implementation of all gauge instances within a view hierarchy.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 7.0+
visionOS 1.0+

    
    
    protocol GaugeStyle

## Overview

To configure the style for all the `Gauge` instances in a view hierarchy, use
the `gaugeStyle(_:)` modifier. For example, you can configure a gauge to use
the `circular` style:

## Topics

### Getting the automatic style

`static var automatic: DefaultGaugeStyle`

The default gauge view style in the current context of the view being styled.

Available when `Self` is `DefaultGaugeStyle`.

### Getting circular gauge styles

`static var circular: CircularGaugeStyle`

A gauge style that displays an open ring with a marker that appears at a point
along the ring to indicate the gauge’s current value.

Available when `Self` is `CircularGaugeStyle`.

`static var accessoryCircular: AccessoryCircularGaugeStyle`

A gauge style that displays an open ring with a marker that appears at a point
along the ring to indicate the gauge’s current value.

Available when `Self` is `AccessoryCircularGaugeStyle`.

`static var accessoryCircularCapacity: AccessoryCircularCapacityGaugeStyle`

A gauge style that displays a closed ring that’s partially filled in to
indicate the gauge’s current value.

Available when `Self` is `AccessoryCircularCapacityGaugeStyle`.

### Getting linear gauge styles

`static var linear: LinearGaugeStyle`

A gauge style that displays a bar with a marker that appears at a point along
the bar to indicate the gauge’s current value.

Available when `Self` is `LinearGaugeStyle`.

`static var linearCapacity: LinearCapacityGaugeStyle`

A gauge style that displays a bar that fills from leading to trailing edges as
the gauge’s current value increases.

Available when `Self` is `LinearCapacityGaugeStyle`.

`static var accessoryLinear: AccessoryLinearGaugeStyle`

A gauge style that displays bar with a marker that appears at a point along
the bar to indicate the gauge’s current value.

Available when `Self` is `AccessoryLinearGaugeStyle`.

`static var accessoryLinearCapacity: AccessoryLinearCapacityGaugeStyle`

A gauge style that displays bar that fills from leading to trailing edges as
the gauge’s current value increases.

Available when `Self` is `AccessoryLinearCapacityGaugeStyle`.

### Creating custom gauge styles

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Creates a view representing the body of a gauge.

**Required**

` typealias Configuration`

The properties of a gauge instance.

`associatedtype Body : View`

A view representing the body of a gauge.

**Required**

### Supporting types

`struct DefaultGaugeStyle`

The default gauge view style in the current context of the view being styled.

`struct CircularGaugeStyle`

A gauge style that displays an open ring with a marker that appears at a point
along the ring to indicate the gauge’s current value.

`struct AccessoryCircularGaugeStyle`

A gauge style that displays an open ring with a marker that appears at a point
along the ring to indicate the gauge’s current value.

`struct AccessoryCircularCapacityGaugeStyle`

A gauge style that displays a closed ring that’s partially filled in to
indicate the gauge’s current value.

`struct LinearGaugeStyle`

A gauge style that displays a bar with a marker that appears at a point along
the bar to indicate the gauge’s current value.

`struct LinearCapacityGaugeStyle`

A gauge style that displays bar that fills from leading to trailing edges as
the gauge’s current value increases.

`struct AccessoryLinearGaugeStyle`

A gauge style that displays bar with a marker that appears at a point along
the bar to indicate the gauge’s current value.

`struct AccessoryLinearCapacityGaugeStyle`

A gauge style that displays bar that fills from leading to trailing edges as
the gauge’s current value increases.

## Relationships

### Conforming Types

  * `AccessoryCircularCapacityGaugeStyle`
  * `AccessoryCircularGaugeStyle`
  * `AccessoryLinearCapacityGaugeStyle`
  * `AccessoryLinearGaugeStyle`
  * `CircularGaugeStyle`
  * `DefaultGaugeStyle`
  * `LinearCapacityGaugeStyle`
  * `LinearGaugeStyle`

## See Also

### Styling indicators

`func gaugeStyle<S>(S) -> some View`

Sets the style for gauges within this view.

`struct GaugeStyleConfiguration`

The properties of a gauge instance.

`func progressViewStyle<S>(S) -> some View`

Sets the style for progress views in this view.

`protocol ProgressViewStyle`

A type that applies standard interaction behavior to all progress views within
a view hierarchy.

`struct ProgressViewStyleConfiguration`

The properties of a progress view instance.

Structure

# GaugeStyleConfiguration

The properties of a gauge instance.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 7.0+
visionOS 1.0+

    
    
    struct GaugeStyleConfiguration

## Topics

### Describing the purpose of the gauge

`var label: GaugeStyleConfiguration.Label`

A view that describes the purpose of the gauge.

`struct Label`

A type-erased label of a gauge, describing its purpose.

### Reporting the range

`var minimumValueLabel: GaugeStyleConfiguration.MinimumValueLabel?`

A view that describes the minimum of the range for the current value.

`struct MinimumValueLabel`

A type-erased value label of a gauge describing the minimum value.

`var maximumValueLabel: GaugeStyleConfiguration.MaximumValueLabel?`

A view that describes the maximum of the range for the current value.

`struct MaximumValueLabel`

A type-erased value label of a gauge describing the maximum value.

### Setting the value

`var value: Double`

The current value of the gauge.

`var currentValueLabel: GaugeStyleConfiguration.CurrentValueLabel?`

A view that describes the current value.

`struct CurrentValueLabel`

A type-erased value label of a gauge that contains the current value.

`struct MarkedValueLabel`

A type-erased label describing a specific value of a gauge.

## See Also

### Styling indicators

`func gaugeStyle<S>(S) -> some View`

Sets the style for gauges within this view.

`protocol GaugeStyle`

Defines the implementation of all gauge instances within a view hierarchy.

`func progressViewStyle<S>(S) -> some View`

Sets the style for progress views in this view.

`protocol ProgressViewStyle`

A type that applies standard interaction behavior to all progress views within
a view hierarchy.

`struct ProgressViewStyleConfiguration`

The properties of a progress view instance.

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

Protocol

# ProgressViewStyle

A type that applies standard interaction behavior to all progress views within
a view hierarchy.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    protocol ProgressViewStyle

## Overview

To configure the current progress view style for a view hierarchy, use the
`progressViewStyle(_:)` modifier.

## Topics

### Getting built-in progress view styles

`static var automatic: DefaultProgressViewStyle`

The default progress view style in the current context of the view being
styled.

Available when `Self` is `DefaultProgressViewStyle`.

`static var circular: CircularProgressViewStyle`

The style of a progress view that uses a circular gauge to indicate the
partial completion of an activity.

Available when `Self` is `CircularProgressViewStyle`.

`static var linear: LinearProgressViewStyle`

A progress view that visually indicates its progress using a horizontal bar.

Available when `Self` is `LinearProgressViewStyle`.

### Creating custom progress view styles

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Creates a view representing the body of a progress view.

**Required**

` typealias Configuration`

A type alias for the properties of a progress view instance.

`associatedtype Body : View`

A view representing the body of a progress view.

**Required**

### Supporting types

`struct DefaultProgressViewStyle`

The default progress view style in the current context of the view being
styled.

`struct CircularProgressViewStyle`

A progress view that uses a circular gauge to indicate the partial completion
of an activity.

`struct LinearProgressViewStyle`

A progress view that visually indicates its progress using a horizontal bar.

## Relationships

### Conforming Types

  * `CircularProgressViewStyle`
  * `DefaultProgressViewStyle`
  * `LinearProgressViewStyle`

## See Also

### Styling indicators

`func gaugeStyle<S>(S) -> some View`

Sets the style for gauges within this view.

`protocol GaugeStyle`

Defines the implementation of all gauge instances within a view hierarchy.

`struct GaugeStyleConfiguration`

The properties of a gauge instance.

`func progressViewStyle<S>(S) -> some View`

Sets the style for progress views in this view.

`struct ProgressViewStyleConfiguration`

The properties of a progress view instance.

Structure

# ProgressViewStyleConfiguration

The properties of a progress view instance.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    struct ProgressViewStyleConfiguration

## Topics

### Configuring the label

`var label: ProgressViewStyleConfiguration.Label?`

A view that describes the task represented by the progress view.

`struct Label`

A type-erased label describing the task represented by the progress view.

### Configuring the current value label

`var currentValueLabel: ProgressViewStyleConfiguration.CurrentValueLabel?`

A view that describes the current value of a progress view.

`struct CurrentValueLabel`

A type-erased label that describes the current value of a progress view.

### Configuring progress completion

`let fractionCompleted: Double?`

The completed fraction of the task represented by the progress view, from
`0.0` (not yet started) to `1.0` (fully complete), or `nil` if the progress is
indeterminate or relative to a date interval.

## See Also

### Styling indicators

`func gaugeStyle<S>(S) -> some View`

Sets the style for gauges within this view.

`protocol GaugeStyle`

Defines the implementation of all gauge instances within a view hierarchy.

`struct GaugeStyleConfiguration`

The properties of a gauge instance.

`func progressViewStyle<S>(S) -> some View`

Sets the style for progress views in this view.

`protocol ProgressViewStyle`

A type that applies standard interaction behavior to all progress views within
a view hierarchy.

Instance Method

# labelStyle(_:)

Sets the style for labels within this view.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func labelStyle<S>(_ style: S) -> some View where S : LabelStyle
    

## Discussion

Use this modifier to set a specific style for all labels within a view:

## See Also

### Displaying text

`struct Text`

A view that displays one or more lines of read-only text.

`struct Label`

A standard label for user interface items, consisting of an icon with a title.

Protocol

# LabelStyle

A type that applies a custom appearance to all labels within a view.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    protocol LabelStyle

## Overview

To configure the current label style for a view hierarchy, use the
`labelStyle(_:)` modifier.

## Topics

### Getting built-in label styles

`static var automatic: DefaultLabelStyle`

A label style that resolves its appearance automatically based on the current
context.

Available when `Self` is `DefaultLabelStyle`.

`static var iconOnly: IconOnlyLabelStyle`

A label style that only displays the icon of the label.

Available when `Self` is `IconOnlyLabelStyle`.

`static var titleAndIcon: TitleAndIconLabelStyle`

A label style that shows both the title and icon of the label using a system-
standard layout.

Available when `Self` is `TitleAndIconLabelStyle`.

`static var titleOnly: TitleOnlyLabelStyle`

A label style that only displays the title of the label.

Available when `Self` is `TitleOnlyLabelStyle`.

### Creating custom label styles

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Creates a view that represents the body of a label.

**Required**

` typealias Configuration`

The properties of a label.

`associatedtype Body : View`

A view that represents the body of a label.

**Required**

### Supporting types

`struct DefaultLabelStyle`

The default label style in the current context.

`struct IconOnlyLabelStyle`

A label style that only displays the icon of the label.

`struct TitleAndIconLabelStyle`

A label style that shows both the title and icon of the label using a system-
standard layout.

`struct TitleOnlyLabelStyle`

A label style that only displays the title of the label.

## Relationships

### Conforming Types

  * `DefaultLabelStyle`
  * `IconOnlyLabelStyle`
  * `TitleAndIconLabelStyle`
  * `TitleOnlyLabelStyle`

## See Also

### Styling views that display text

`func labelStyle<S>(S) -> some View`

Sets the style for labels within this view.

`struct LabelStyleConfiguration`

The properties of a label.

`func textFieldStyle<S>(S) -> some View`

Sets the style for text fields within this view.

`protocol TextFieldStyle`

A specification for the appearance and interaction of a text field.

`func textEditorStyle(some TextEditorStyle) -> some View`

Sets the style for text editors within this view.

`protocol TextEditorStyle`

A specification for the appearance and interaction of a text editor.

`struct TextEditorStyleConfiguration`

The properties of a text editor.

Structure

# LabelStyleConfiguration

The properties of a label.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    struct LabelStyleConfiguration

## Topics

### Setting the icon

`var icon: LabelStyleConfiguration.Icon`

A symbolic representation of the labeled item.

`struct Icon`

A type-erased icon view of a label.

### Setting the title

`var title: LabelStyleConfiguration.Title`

A description of the labeled item.

`struct Title`

A type-erased title view of a label.

## See Also

### Styling views that display text

`func labelStyle<S>(S) -> some View`

Sets the style for labels within this view.

`protocol LabelStyle`

A type that applies a custom appearance to all labels within a view.

`func textFieldStyle<S>(S) -> some View`

Sets the style for text fields within this view.

`protocol TextFieldStyle`

A specification for the appearance and interaction of a text field.

`func textEditorStyle(some TextEditorStyle) -> some View`

Sets the style for text editors within this view.

`protocol TextEditorStyle`

A specification for the appearance and interaction of a text editor.

`struct TextEditorStyleConfiguration`

The properties of a text editor.

Instance Method

# textFieldStyle(_:)

Sets the style for text fields within this view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func textFieldStyle<S>(_ style: S) -> some View where S : TextFieldStyle
    

## See Also

### Getting text input

`struct TextField`

A control that displays an editable text interface.

`struct SecureField`

A control into which people securely enter private text.

`struct TextEditor`

A view that can display and edit long-form text.

Protocol

# TextFieldStyle

A specification for the appearance and interaction of a text field.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    protocol TextFieldStyle

## Topics

### Getting built-in text field styles

`static var automatic: DefaultTextFieldStyle`

The default text field style, based on the text field’s context.

Available when `Self` is `DefaultTextFieldStyle`.

`static var plain: PlainTextFieldStyle`

A text field style with no decoration.

Available when `Self` is `PlainTextFieldStyle`.

`static var roundedBorder: RoundedBorderTextFieldStyle`

A text field style with a system-defined rounded border.

Available when `Self` is `RoundedBorderTextFieldStyle`.

`static var squareBorder: SquareBorderTextFieldStyle`

A text field style with a system-defined square border.

Available when `Self` is `SquareBorderTextFieldStyle`.

### Supporting types

`struct DefaultTextFieldStyle`

The default text field style, based on the text field’s context.

`struct PlainTextFieldStyle`

A text field style with no decoration.

`struct RoundedBorderTextFieldStyle`

A text field style with a system-defined rounded border.

`struct SquareBorderTextFieldStyle`

A text field style with a system-defined square border.

## Relationships

### Conforming Types

  * `DefaultTextFieldStyle`
  * `PlainTextFieldStyle`
  * `RoundedBorderTextFieldStyle`
  * `SquareBorderTextFieldStyle`

## See Also

### Styling views that display text

`func labelStyle<S>(S) -> some View`

Sets the style for labels within this view.

`protocol LabelStyle`

A type that applies a custom appearance to all labels within a view.

`struct LabelStyleConfiguration`

The properties of a label.

`func textFieldStyle<S>(S) -> some View`

Sets the style for text fields within this view.

`func textEditorStyle(some TextEditorStyle) -> some View`

Sets the style for text editors within this view.

`protocol TextEditorStyle`

A specification for the appearance and interaction of a text editor.

`struct TextEditorStyleConfiguration`

The properties of a text editor.

Instance Method

# textEditorStyle(_:)

Sets the style for text editors within this view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func textEditorStyle(_ style: some TextEditorStyle) -> some View
    

## See Also

### Styling views that display text

`func labelStyle<S>(S) -> some View`

Sets the style for labels within this view.

`protocol LabelStyle`

A type that applies a custom appearance to all labels within a view.

`struct LabelStyleConfiguration`

The properties of a label.

`func textFieldStyle<S>(S) -> some View`

Sets the style for text fields within this view.

`protocol TextFieldStyle`

A specification for the appearance and interaction of a text field.

`protocol TextEditorStyle`

A specification for the appearance and interaction of a text editor.

`struct TextEditorStyleConfiguration`

The properties of a text editor.

Protocol

# TextEditorStyle

A specification for the appearance and interaction of a text editor.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    protocol TextEditorStyle

## Topics

### Getting built-in styles

`static var automatic: AutomaticTextEditorStyle`

The default text editor style, based on the text editor’s context.

Available when `Self` is `AutomaticTextEditorStyle`.

`static var plain: PlainTextEditorStyle`

A text editor style with no decoration.

Available when `Self` is `PlainTextEditorStyle`.

`static var roundedBorder: RoundedBorderTextEditorStyle`

A text editor style with a system-defined rounded border.

Available when `Self` is `RoundedBorderTextEditorStyle`.

### Creating custom styles

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Creates a view that represents the body of a text editor.

**Required**

` typealias Configuration`

The properties of a text editor.

`associatedtype Body : View`

A view that represents the body of a text editor.

**Required**

### Supporting types

`struct AutomaticTextEditorStyle`

The default text editor style, based on the text editor’s context.

`struct PlainTextEditorStyle`

A text editor style with no decoration.

`struct RoundedBorderTextEditorStyle`

A text editor style with a system-defined rounded border.

## Relationships

### Conforming Types

  * `AutomaticTextEditorStyle`
  * `PlainTextEditorStyle`
  * `RoundedBorderTextEditorStyle`

## See Also

### Styling views that display text

`func labelStyle<S>(S) -> some View`

Sets the style for labels within this view.

`protocol LabelStyle`

A type that applies a custom appearance to all labels within a view.

`struct LabelStyleConfiguration`

The properties of a label.

`func textFieldStyle<S>(S) -> some View`

Sets the style for text fields within this view.

`protocol TextFieldStyle`

A specification for the appearance and interaction of a text field.

`func textEditorStyle(some TextEditorStyle) -> some View`

Sets the style for text editors within this view.

`struct TextEditorStyleConfiguration`

The properties of a text editor.

Structure

# TextEditorStyleConfiguration

The properties of a text editor.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    struct TextEditorStyleConfiguration

## See Also

### Styling views that display text

`func labelStyle<S>(S) -> some View`

Sets the style for labels within this view.

`protocol LabelStyle`

A type that applies a custom appearance to all labels within a view.

`struct LabelStyleConfiguration`

The properties of a label.

`func textFieldStyle<S>(S) -> some View`

Sets the style for text fields within this view.

`protocol TextFieldStyle`

A specification for the appearance and interaction of a text field.

`func textEditorStyle(some TextEditorStyle) -> some View`

Sets the style for text editors within this view.

`protocol TextEditorStyle`

A specification for the appearance and interaction of a text editor.

Instance Method

# listStyle(_:)

Sets the style for lists within this view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func listStyle<S>(_ style: S) -> some View where S : ListStyle
    

## See Also

### Creating a list

Displaying data in lists

Visualize collections of data with platform-appropriate appearance.

`struct List`

A container that presents rows of data arranged in a single column, optionally
providing the ability to select one or more members.

`struct Section`

A container view that you can use to add hierarchy within certain views.

Protocol

# ListStyle

A protocol that describes the behavior and appearance of a list.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    protocol ListStyle

## Topics

### Getting built-in list styles

`static var automatic: DefaultListStyle`

The list style that describes a platform’s default behavior and appearance for
a list.

Available when `Self` is `DefaultListStyle`.

`static var bordered: BorderedListStyle`

The list style that describes the behavior and appearance of a list with
standard border.

Available when `Self` is `BorderedListStyle`.

`static var carousel: CarouselListStyle`

The carousel list style.

Available when `Self` is `CarouselListStyle`.

`static var elliptical: EllipticalListStyle`

The list style that describes the behavior and appearance of an elliptical
list.

Available when `Self` is `EllipticalListStyle`.

`static var grouped: GroupedListStyle`

The list style that describes the behavior and appearance of a grouped list.

Available when `Self` is `GroupedListStyle`.

`static var inset: InsetListStyle`

The list style that describes the behavior and appearance of an inset list.

Available when `Self` is `InsetListStyle`.

`static var insetGrouped: InsetGroupedListStyle`

The list style that describes the behavior and appearance of an inset grouped
list.

Available when `Self` is `InsetGroupedListStyle`.

`static var plain: PlainListStyle`

The list style that describes the behavior and appearance of a plain list.

Available when `Self` is `PlainListStyle`.

`static var sidebar: SidebarListStyle`

The list style that describes the behavior and appearance of a sidebar list.

Available when `Self` is `SidebarListStyle`.

### Deprecated styles

`static func bordered(alternatesRowBackgrounds: Bool) -> BorderedListStyle`

The list style that describes the behavior and appearance of a list with
standard border.

Available when `Self` is `BorderedListStyle`.

Deprecated

`static func inset(alternatesRowBackgrounds: Bool) -> InsetListStyle`

The list style that describes the behavior and appearance of an inset list
with optional alternating row backgrounds.

Available when `Self` is `InsetListStyle`.

Deprecated

### Supporting types

`struct DefaultListStyle`

The list style that describes a platform’s default behavior and appearance for
a list.

`struct BorderedListStyle`

The list style that describes the behavior and appearance of a list with
standard border.

`struct CarouselListStyle`

The carousel list style.

`struct EllipticalListStyle`

The list style that describes the behavior and appearance of an elliptical
list.

`struct GroupedListStyle`

The list style that describes the behavior and appearance of a grouped list.

`struct InsetListStyle`

The list style that describes the behavior and appearance of an inset list.

`struct InsetGroupedListStyle`

The list style that describes the behavior and appearance of an inset grouped
list.

`struct PlainListStyle`

The list style that describes the behavior and appearance of a plain list.

`struct SidebarListStyle`

The list style that describes the behavior and appearance of a sidebar list.

## Relationships

### Conforming Types

  * `BorderedListStyle`
  * `CarouselListStyle`
  * `DefaultListStyle`
  * `EllipticalListStyle`
  * `GroupedListStyle`
  * `InsetGroupedListStyle`
  * `InsetListStyle`
  * `PlainListStyle`
  * `SidebarListStyle`

## See Also

### Styling collection views

`func listStyle<S>(S) -> some View`

Sets the style for lists within this view.

`func tableStyle<S>(S) -> some View`

Sets the style for tables within this view.

`protocol TableStyle`

A type that applies a custom appearance to all tables within a view.

`struct TableStyleConfiguration`

The properties of a table.

`func disclosureGroupStyle<S>(S) -> some View`

Sets the style for disclosure groups within this view.

`protocol DisclosureGroupStyle`

A type that specifies the appearance and interaction of disclosure groups
within a view hierarchy.

Instance Method

# tableStyle(_:)

Sets the style for tables within this view.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    func tableStyle<S>(_ style: S) -> some View where S : TableStyle
    

## See Also

### Creating a table

Building a Great Mac App with SwiftUI

Create engaging SwiftUI Mac apps by incorporating side bars, tables, toolbars,
and several other popular user interface elements.

`struct Table`

A container that presents rows of data arranged in one or more columns,
optionally providing the ability to select one or more members.

Protocol

# TableStyle

A type that applies a custom appearance to all tables within a view.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    protocol TableStyle

## Overview

To configure the current table style for a view hierarchy, use the
`tableStyle(_:)` modifier.

## Topics

### Getting built-in table styles

`static var automatic: AutomaticTableStyle`

The default table style in the current context.

Available when `Self` is `AutomaticTableStyle`.

`static var inset: InsetTableStyle`

The table style that describes the behavior and appearance of a table with its
content and selection inset from the table edges.

Available when `Self` is `InsetTableStyle`.

`static var bordered: BorderedTableStyle`

The table style that describes the behavior and appearance of a table with
standard border.

Available when `Self` is `BorderedTableStyle`.

### Creating custom table styles

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Creates a view that represents the body of a table.

**Required**

` typealias Configuration`

The properties of a table.

`associatedtype Body : View`

A view that represents the body of a table.

**Required**

### Deprecated styles

`static func inset(alternatesRowBackgrounds: Bool) -> InsetTableStyle`

The table style that describes the behavior and appearance of a table with its
content and selection inset from the table edges.

Available when `Self` is `InsetTableStyle`.

Deprecated

`static func bordered(alternatesRowBackgrounds: Bool) -> BorderedTableStyle`

The table style that describes the behavior and appearance of a table with
standard border.

Available when `Self` is `BorderedTableStyle`.

Deprecated

### Supporting types

`struct AutomaticTableStyle`

The default table style in the current context.

`struct InsetTableStyle`

The table style that describes the behavior and appearance of a table with its
content and selection inset from the table edges.

`struct BorderedTableStyle`

The table style that describes the behavior and appearance of a table with
standard border.

## Relationships

### Conforming Types

  * `AutomaticTableStyle`
  * `BorderedTableStyle`
  * `InsetTableStyle`

## See Also

### Styling collection views

`func listStyle<S>(S) -> some View`

Sets the style for lists within this view.

`protocol ListStyle`

A protocol that describes the behavior and appearance of a list.

`func tableStyle<S>(S) -> some View`

Sets the style for tables within this view.

`struct TableStyleConfiguration`

The properties of a table.

`func disclosureGroupStyle<S>(S) -> some View`

Sets the style for disclosure groups within this view.

`protocol DisclosureGroupStyle`

A type that specifies the appearance and interaction of disclosure groups
within a view hierarchy.

Structure

# TableStyleConfiguration

The properties of a table.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    struct TableStyleConfiguration

## See Also

### Styling collection views

`func listStyle<S>(S) -> some View`

Sets the style for lists within this view.

`protocol ListStyle`

A protocol that describes the behavior and appearance of a list.

`func tableStyle<S>(S) -> some View`

Sets the style for tables within this view.

`protocol TableStyle`

A type that applies a custom appearance to all tables within a view.

`func disclosureGroupStyle<S>(S) -> some View`

Sets the style for disclosure groups within this view.

`protocol DisclosureGroupStyle`

A type that specifies the appearance and interaction of disclosure groups
within a view hierarchy.

Instance Method

# disclosureGroupStyle(_:)

Sets the style for disclosure groups within this view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    func disclosureGroupStyle<S>(_ style: S) -> some View where S : DisclosureGroupStyle
    

## See Also

### Disclosing information progressively

`struct OutlineGroup`

A structure that computes views and disclosure groups on demand from an
underlying collection of tree-structured, identified data.

`struct DisclosureGroup`

A view that shows or hides another content view, based on the state of a
disclosure control.

Protocol

# DisclosureGroupStyle

A type that specifies the appearance and interaction of disclosure groups
within a view hierarchy.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    protocol DisclosureGroupStyle

## Overview

To configure the disclosure group style for a view hierarchy, use the
`disclosureGroupStyle(_:)` modifier.

To create a custom disclosure group style, declare a type that conforms to
`DisclosureGroupStyle`. Implement the `makeBody(configuration:)` method to
return a view that composes the elements of the `configuration` that SwiftUI
provides to your method.

## Topics

### Getting the styles

`static var automatic: AutomaticDisclosureGroupStyle`

A disclosure group style that resolves its appearance automatically based on
the current context.

Available when `Self` is `AutomaticDisclosureGroupStyle`.

### Creating custom disclosure group styles

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Creates a view that represents the body of a disclosure group.

**Required**

` struct DisclosureGroupStyleConfiguration`

The properties of a disclosure group instance.

`typealias Configuration`

The properties of a disclosure group instance.

`associatedtype Body : View`

A view that represents the body of a disclosure group.

**Required**

### Supporting types

`struct AutomaticDisclosureGroupStyle`

A disclosure group style that resolves its appearance automatically based on
the current context.

## Relationships

### Conforming Types

  * `AutomaticDisclosureGroupStyle`

## See Also

### Styling collection views

`func listStyle<S>(S) -> some View`

Sets the style for lists within this view.

`protocol ListStyle`

A protocol that describes the behavior and appearance of a list.

`func tableStyle<S>(S) -> some View`

Sets the style for tables within this view.

`protocol TableStyle`

A type that applies a custom appearance to all tables within a view.

`struct TableStyleConfiguration`

The properties of a table.

`func disclosureGroupStyle<S>(S) -> some View`

Sets the style for disclosure groups within this view.

Instance Method

# navigationSplitViewStyle(_:)

Sets the style for navigation split views within this view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func navigationSplitViewStyle<S>(_ style: S) -> some View where S : NavigationSplitViewStyle
    

##  Parameters

`style`

    

The style to set.

## Return Value

A view that uses the specified navigation split view style.

## See Also

### Presenting views in columns

Bringing robust navigation structure to your SwiftUI app

Use navigation links, stacks, destinations, and paths to provide a streamlined
experience for all platforms, as well as behaviors such as deep linking and
state restoration.

Migrating to new navigation types

Improve navigation behavior in your app by replacing navigation views with
navigation stacks and navigation split views.

`struct NavigationSplitView`

A view that presents views in two or three columns, where selections in
leading columns control presentations in subsequent columns.

`func navigationSplitViewColumnWidth(CGFloat) -> some View`

Sets a fixed, preferred width for the column containing this view.

`func navigationSplitViewColumnWidth(min: CGFloat?, ideal: CGFloat, max:
CGFloat?) -> some View`

Sets a flexible, preferred width for the column containing this view.

`struct NavigationSplitViewVisibility`

The visibility of the leading columns in a navigation split view.

`struct NavigationLink`

A view that controls a navigation presentation.

Protocol

# NavigationSplitViewStyle

A type that specifies the appearance and interaction of navigation split views
within a view hierarchy.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    protocol NavigationSplitViewStyle

## Overview

To configure the navigation split view style for a view hierarchy, use the
`navigationSplitViewStyle(_:)` modifier.

## Topics

### Creating built-in styles

`static var automatic: AutomaticNavigationSplitViewStyle`

A navigation split style that resolves its appearance automatically based on
the current context.

Available when `Self` is `AutomaticNavigationSplitViewStyle`.

`static var balanced: BalancedNavigationSplitViewStyle`

A navigation split style that reduces the size of the detail content to make
room when showing the leading column or columns.

Available when `Self` is `BalancedNavigationSplitViewStyle`.

`static var prominentDetail: ProminentDetailNavigationSplitViewStyle`

A navigation split style that attempts to maintain the size of the detail
content when hiding or showing the leading columns.

Available when `Self` is `ProminentDetailNavigationSplitViewStyle`.

### Creating custom styles

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Creates a view that represents the body of a navigation split view.

**Required**

` typealias Configuration`

The properties of a navigation split view instance.

`associatedtype Body : View`

A view that represents the body of a navigation split view.

**Required**

### Supporting types

`struct AutomaticNavigationSplitViewStyle`

A navigation split style that resolves its appearance automatically based on
the current context.

`struct BalancedNavigationSplitViewStyle`

A navigation split style that reduces the size of the detail content to make
room when showing the leading column or columns.

`struct ProminentDetailNavigationSplitViewStyle`

A navigation split style that attempts to maintain the size of the detail
content when hiding or showing the leading columns.

`struct NavigationSplitViewStyleConfiguration`

The properties of a navigation split view instance.

## Relationships

### Conforming Types

  * `AutomaticNavigationSplitViewStyle`
  * `BalancedNavigationSplitViewStyle`
  * `ProminentDetailNavigationSplitViewStyle`

## See Also

### Styling navigation views

`func navigationSplitViewStyle<S>(S) -> some View`

Sets the style for navigation split views within this view.

`func tabViewStyle<S>(S) -> some View`

Sets the style for the tab view within the current environment.

`protocol TabViewStyle`

A specification for the appearance and interaction of a `TabView`.

Instance Method

# tabViewStyle(_:)

Sets the style for the tab view within the current environment.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func tabViewStyle<S>(_ style: S) -> some View where S : TabViewStyle
    

##  Parameters

`style`

    

The style to apply to this tab view.

## See Also

### Presenting views in tabs

`struct TabView`

A view that switches between multiple child views using interactive user
interface elements.

`func tabItem<V>(() -> V) -> some View`

Sets the tab bar item associated with this view.

Protocol

# TabViewStyle

A specification for the appearance and interaction of a `TabView`.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    protocol TabViewStyle

## Topics

### Getting built-in tab view styles

`static var automatic: DefaultTabViewStyle`

The default `TabView` style.

Available when `Self` is `DefaultTabViewStyle`.

`static var carousel: CarouselTabViewStyle`

A style that implements the carousel interaction and appearance.

Available when `Self` is `CarouselTabViewStyle`.

Deprecated

`static var page: PageTabViewStyle`

A `TabViewStyle` that implements a paged scrolling `TabView`.

Available when `Self` is `PageTabViewStyle`.

`static func page(indexDisplayMode: PageTabViewStyle.IndexDisplayMode) ->
PageTabViewStyle`

A `TabViewStyle` that implements a paged scrolling `TabView` with an index
display mode.

Available when `Self` is `PageTabViewStyle`.

`static var verticalPage: VerticalPageTabViewStyle`

A `TabViewStyle` that implements the vertical page `TabView` interaction and
appearance.

Available when `Self` is `VerticalPageTabViewStyle`.

`static func verticalPage(transitionStyle:
VerticalPageTabViewStyle.TransitionStyle) -> VerticalPageTabViewStyle`

A `TabViewStyle` that implements the vertical page `TabView` interaction and
appearance, and performs the specified transition.

Available when `Self` is `VerticalPageTabViewStyle`.

### Supporting types

`struct DefaultTabViewStyle`

The default `TabView` style.

`struct CarouselTabViewStyle`

A style that implements the carousel interaction and appearance.

Deprecated

`struct PageTabViewStyle`

A `TabViewStyle` that implements a paged scrolling `TabView`.

`struct VerticalPageTabViewStyle`

A `TabViewStyle` that implements the vertical `TabView` interaction and
appearance.

## Relationships

### Conforming Types

  * `CarouselTabViewStyle`
  * `DefaultTabViewStyle`
  * `PageTabViewStyle`
  * `VerticalPageTabViewStyle`

## See Also

### Styling navigation views

`func navigationSplitViewStyle<S>(S) -> some View`

Sets the style for navigation split views within this view.

`protocol NavigationSplitViewStyle`

A type that specifies the appearance and interaction of navigation split views
within a view hierarchy.

`func tabViewStyle<S>(S) -> some View`

Sets the style for the tab view within the current environment.

Instance Method

# controlGroupStyle(_:)

Sets the style for control groups within this view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 17.0+  visionOS
1.0+

    
    
    func controlGroupStyle<S>(_ style: S) -> some View where S : ControlGroupStyle
    

##  Parameters

`style`

    

The style to apply to controls within this view.

## See Also

### Presenting a group of controls

`struct ControlGroup`

A container view that displays semantically-related controls in a visually-
appropriate manner for the context

Protocol

# ControlGroupStyle

Defines the implementation of all control groups within a view hierarchy.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 17.0+  visionOS
1.0+

    
    
    protocol ControlGroupStyle

## Overview

To configure the current `ControlGroupStyle` for a view hierarchy, use the
`controlGroupStyle(_:)` modifier.

## Topics

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

`static var palette: PaletteControlGroupStyle`

A control group style that presents its content as a palette.

Available when `Self` is `PaletteControlGroupStyle`.

### Creating custom control group styles

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Creates a view representing the body of a control group.

**Required**

` typealias Configuration`

The properties of a `ControlGroup` instance being created.

`associatedtype Body : View`

A view representing the body of a control group.

**Required**

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

`struct PaletteControlGroupStyle`

A control group style that presents its content as a palette.

## Relationships

### Conforming Types

  * `AutomaticControlGroupStyle`
  * `CompactMenuControlGroupStyle`
  * `MenuControlGroupStyle`
  * `NavigationControlGroupStyle`
  * `PaletteControlGroupStyle`

## See Also

### Styling groups

`func controlGroupStyle<S>(S) -> some View`

Sets the style for control groups within this view.

`struct ControlGroupStyleConfiguration`

The properties of a control group.

`func formStyle<S>(S) -> some View`

Sets the style for forms in a view hierarchy.

`protocol FormStyle`

The appearance and behavior of a form.

`struct FormStyleConfiguration`

The properties of a form instance.

`func groupBoxStyle<S>(S) -> some View`

Sets the style for group boxes within this view.

`protocol GroupBoxStyle`

A type that specifies the appearance and interaction of all group boxes within
a view hierarchy.

`struct GroupBoxStyleConfiguration`

The properties of a group box instance.

`func indexViewStyle<S>(S) -> some View`

Sets the style for the index view within the current environment.

`protocol IndexViewStyle`

Defines the implementation of all `IndexView` instances within a view
hierarchy.

`func labeledContentStyle<S>(S) -> some View`

Sets a style for labeled content.

`protocol LabeledContentStyle`

The appearance and behavior of a labeled content instance..

`struct LabeledContentStyleConfiguration`

The properties of a labeled content instance.

Structure

# ControlGroupStyleConfiguration

The properties of a control group.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 17.0+  visionOS
1.0+

    
    
    struct ControlGroupStyleConfiguration

## Topics

### Configuring the label

`let label: ControlGroupStyleConfiguration.Label`

A view that provides the optional label of the `ControlGroup`.

`struct Label`

A type-erased label of a `ControlGroup`.

### Configuring the content

`let content: ControlGroupStyleConfiguration.Content`

A view that represents the content of the `ControlGroup`.

`struct Content`

A type-erased content of a `ControlGroup`.

## See Also

### Styling groups

`func controlGroupStyle<S>(S) -> some View`

Sets the style for control groups within this view.

`protocol ControlGroupStyle`

Defines the implementation of all control groups within a view hierarchy.

`func formStyle<S>(S) -> some View`

Sets the style for forms in a view hierarchy.

`protocol FormStyle`

The appearance and behavior of a form.

`struct FormStyleConfiguration`

The properties of a form instance.

`func groupBoxStyle<S>(S) -> some View`

Sets the style for group boxes within this view.

`protocol GroupBoxStyle`

A type that specifies the appearance and interaction of all group boxes within
a view hierarchy.

`struct GroupBoxStyleConfiguration`

The properties of a group box instance.

`func indexViewStyle<S>(S) -> some View`

Sets the style for the index view within the current environment.

`protocol IndexViewStyle`

Defines the implementation of all `IndexView` instances within a view
hierarchy.

`func labeledContentStyle<S>(S) -> some View`

Sets a style for labeled content.

`protocol LabeledContentStyle`

The appearance and behavior of a labeled content instance..

`struct LabeledContentStyleConfiguration`

The properties of a labeled content instance.

Instance Method

# formStyle(_:)

Sets the style for forms in a view hierarchy.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func formStyle<S>(_ style: S) -> some View where S : FormStyle
    

##  Parameters

`style`

    

The form style to set.

## Return Value

A view that uses the specified form style for itself and its child views.

## See Also

### Grouping inputs

`struct Form`

A container for grouping controls used for data entry, such as in settings or
inspectors.

`struct LabeledContent`

A container for attaching a label to a value-bearing view.

`func labeledContentStyle<S>(S) -> some View`

Sets a style for labeled content.

Protocol

# FormStyle

The appearance and behavior of a form.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    protocol FormStyle

## Overview

To configure the style for a single `Form` or for all form instances in a view
hierarchy, use the `formStyle(_:)` modifier.

## Topics

### Getting built-in form styles

`static var automatic: AutomaticFormStyle`

The default form style.

Available when `Self` is `AutomaticFormStyle`.

`static var columns: ColumnsFormStyle`

A non-scrolling form style with a trailing aligned column of labels next to a
leading aligned column of values.

Available when `Self` is `ColumnsFormStyle`.

`static var grouped: GroupedFormStyle`

A form style with grouped rows.

Available when `Self` is `GroupedFormStyle`.

### Creating custom form styles

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Creates a view that represents the body of a form.

**Required**

` typealias Configuration`

The properties of a form instance.

`associatedtype Body : View`

A view that represents the appearance and interaction of a form.

**Required**

### Supporting types

`struct AutomaticFormStyle`

The default form style.

`struct ColumnsFormStyle`

A non-scrolling form style with a trailing aligned column of labels next to a
leading aligned column of values.

`struct GroupedFormStyle`

A form style with grouped rows.

## Relationships

### Conforming Types

  * `AutomaticFormStyle`
  * `ColumnsFormStyle`
  * `GroupedFormStyle`

## See Also

### Styling groups

`func controlGroupStyle<S>(S) -> some View`

Sets the style for control groups within this view.

`protocol ControlGroupStyle`

Defines the implementation of all control groups within a view hierarchy.

`struct ControlGroupStyleConfiguration`

The properties of a control group.

`func formStyle<S>(S) -> some View`

Sets the style for forms in a view hierarchy.

`struct FormStyleConfiguration`

The properties of a form instance.

`func groupBoxStyle<S>(S) -> some View`

Sets the style for group boxes within this view.

`protocol GroupBoxStyle`

A type that specifies the appearance and interaction of all group boxes within
a view hierarchy.

`struct GroupBoxStyleConfiguration`

The properties of a group box instance.

`func indexViewStyle<S>(S) -> some View`

Sets the style for the index view within the current environment.

`protocol IndexViewStyle`

Defines the implementation of all `IndexView` instances within a view
hierarchy.

`func labeledContentStyle<S>(S) -> some View`

Sets a style for labeled content.

`protocol LabeledContentStyle`

The appearance and behavior of a labeled content instance..

`struct LabeledContentStyleConfiguration`

The properties of a labeled content instance.

Structure

# FormStyleConfiguration

The properties of a form instance.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    struct FormStyleConfiguration

## Topics

### Getting configuration content

`let content: FormStyleConfiguration.Content`

A view that is the content of the form.

`struct Content`

A type-erased content of a form.

## See Also

### Styling groups

`func controlGroupStyle<S>(S) -> some View`

Sets the style for control groups within this view.

`protocol ControlGroupStyle`

Defines the implementation of all control groups within a view hierarchy.

`struct ControlGroupStyleConfiguration`

The properties of a control group.

`func formStyle<S>(S) -> some View`

Sets the style for forms in a view hierarchy.

`protocol FormStyle`

The appearance and behavior of a form.

`func groupBoxStyle<S>(S) -> some View`

Sets the style for group boxes within this view.

`protocol GroupBoxStyle`

A type that specifies the appearance and interaction of all group boxes within
a view hierarchy.

`struct GroupBoxStyleConfiguration`

The properties of a group box instance.

`func indexViewStyle<S>(S) -> some View`

Sets the style for the index view within the current environment.

`protocol IndexViewStyle`

Defines the implementation of all `IndexView` instances within a view
hierarchy.

`func labeledContentStyle<S>(S) -> some View`

Sets a style for labeled content.

`protocol LabeledContentStyle`

The appearance and behavior of a labeled content instance..

`struct LabeledContentStyleConfiguration`

The properties of a labeled content instance.

Instance Method

# groupBoxStyle(_:)

Sets the style for group boxes within this view.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    func groupBoxStyle<S>(_ style: S) -> some View where S : GroupBoxStyle
    

##  Parameters

`style`

    

The style to apply to boxes within this view.

## See Also

### Grouping views into a box

`struct GroupBox`

A stylized view, with an optional label, that visually collects a logical
grouping of content.

Protocol

# GroupBoxStyle

A type that specifies the appearance and interaction of all group boxes within
a view hierarchy.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    protocol GroupBoxStyle

## Overview

To configure the current `GroupBoxStyle` for a view hierarchy, use the
`groupBoxStyle(_:)` modifier.

## Topics

### Getting built-in group box styles

`static var automatic: DefaultGroupBoxStyle`

The default style for group box views.

Available when `Self` is `DefaultGroupBoxStyle`.

### Creating custom group box styles

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Creates a view representing the body of a group box.

**Required**

` typealias Configuration`

The properties of a group box instance.

`associatedtype Body : View`

A view that represents the body of a group box.

**Required**

### Supporting types

`struct DefaultGroupBoxStyle`

The default style for group box views.

## Relationships

### Conforming Types

  * `DefaultGroupBoxStyle`

## See Also

### Styling groups

`func controlGroupStyle<S>(S) -> some View`

Sets the style for control groups within this view.

`protocol ControlGroupStyle`

Defines the implementation of all control groups within a view hierarchy.

`struct ControlGroupStyleConfiguration`

The properties of a control group.

`func formStyle<S>(S) -> some View`

Sets the style for forms in a view hierarchy.

`protocol FormStyle`

The appearance and behavior of a form.

`struct FormStyleConfiguration`

The properties of a form instance.

`func groupBoxStyle<S>(S) -> some View`

Sets the style for group boxes within this view.

`struct GroupBoxStyleConfiguration`

The properties of a group box instance.

`func indexViewStyle<S>(S) -> some View`

Sets the style for the index view within the current environment.

`protocol IndexViewStyle`

Defines the implementation of all `IndexView` instances within a view
hierarchy.

`func labeledContentStyle<S>(S) -> some View`

Sets a style for labeled content.

`protocol LabeledContentStyle`

The appearance and behavior of a labeled content instance..

`struct LabeledContentStyleConfiguration`

The properties of a labeled content instance.

Structure

# GroupBoxStyleConfiguration

The properties of a group box instance.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    struct GroupBoxStyleConfiguration

## Topics

### Configuring the label

`let label: GroupBoxStyleConfiguration.Label`

A view that provides the title of the group box.

`struct Label`

A type-erased label of a group box.

### Configuring the content

`let content: GroupBoxStyleConfiguration.Content`

A view that represents the content of the group box.

`struct Content`

A type-erased content of a group box.

## See Also

### Styling groups

`func controlGroupStyle<S>(S) -> some View`

Sets the style for control groups within this view.

`protocol ControlGroupStyle`

Defines the implementation of all control groups within a view hierarchy.

`struct ControlGroupStyleConfiguration`

The properties of a control group.

`func formStyle<S>(S) -> some View`

Sets the style for forms in a view hierarchy.

`protocol FormStyle`

The appearance and behavior of a form.

`struct FormStyleConfiguration`

The properties of a form instance.

`func groupBoxStyle<S>(S) -> some View`

Sets the style for group boxes within this view.

`protocol GroupBoxStyle`

A type that specifies the appearance and interaction of all group boxes within
a view hierarchy.

`func indexViewStyle<S>(S) -> some View`

Sets the style for the index view within the current environment.

`protocol IndexViewStyle`

Defines the implementation of all `IndexView` instances within a view
hierarchy.

`func labeledContentStyle<S>(S) -> some View`

Sets a style for labeled content.

`protocol LabeledContentStyle`

The appearance and behavior of a labeled content instance..

`struct LabeledContentStyleConfiguration`

The properties of a labeled content instance.

Instance Method

# indexViewStyle(_:)

Sets the style for the index view within the current environment.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS 8.0+
visionOS 1.0+

    
    
    func indexViewStyle<S>(_ style: S) -> some View where S : IndexViewStyle
    

##  Parameters

`style`

    

The style to apply to this view.

## See Also

### Styling groups

`func controlGroupStyle<S>(S) -> some View`

Sets the style for control groups within this view.

`protocol ControlGroupStyle`

Defines the implementation of all control groups within a view hierarchy.

`struct ControlGroupStyleConfiguration`

The properties of a control group.

`func formStyle<S>(S) -> some View`

Sets the style for forms in a view hierarchy.

`protocol FormStyle`

The appearance and behavior of a form.

`struct FormStyleConfiguration`

The properties of a form instance.

`func groupBoxStyle<S>(S) -> some View`

Sets the style for group boxes within this view.

`protocol GroupBoxStyle`

A type that specifies the appearance and interaction of all group boxes within
a view hierarchy.

`struct GroupBoxStyleConfiguration`

The properties of a group box instance.

`protocol IndexViewStyle`

Defines the implementation of all `IndexView` instances within a view
hierarchy.

`func labeledContentStyle<S>(S) -> some View`

Sets a style for labeled content.

`protocol LabeledContentStyle`

The appearance and behavior of a labeled content instance..

`struct LabeledContentStyleConfiguration`

The properties of a labeled content instance.

Protocol

# IndexViewStyle

Defines the implementation of all `IndexView` instances within a view
hierarchy.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS 8.0+
visionOS 1.0+

    
    
    protocol IndexViewStyle

## Overview

To configure the current `IndexViewStyle` for a view hierarchy, use the
`.indexViewStyle()` modifier.

## Topics

### Getting built-in index view styles

`static var page: PageIndexViewStyle`

An index view style that places a page index view over its content.

Available when `Self` is `PageIndexViewStyle`.

`static func page(backgroundDisplayMode:
PageIndexViewStyle.BackgroundDisplayMode) -> PageIndexViewStyle`

An index view style that places a page index view over its content.

Available when `Self` is `PageIndexViewStyle`.

### Supporting types

`struct PageIndexViewStyle`

An index view style that places a page index view over its content.

## Relationships

### Conforming Types

  * `PageIndexViewStyle`

## See Also

### Styling groups

`func controlGroupStyle<S>(S) -> some View`

Sets the style for control groups within this view.

`protocol ControlGroupStyle`

Defines the implementation of all control groups within a view hierarchy.

`struct ControlGroupStyleConfiguration`

The properties of a control group.

`func formStyle<S>(S) -> some View`

Sets the style for forms in a view hierarchy.

`protocol FormStyle`

The appearance and behavior of a form.

`struct FormStyleConfiguration`

The properties of a form instance.

`func groupBoxStyle<S>(S) -> some View`

Sets the style for group boxes within this view.

`protocol GroupBoxStyle`

A type that specifies the appearance and interaction of all group boxes within
a view hierarchy.

`struct GroupBoxStyleConfiguration`

The properties of a group box instance.

`func indexViewStyle<S>(S) -> some View`

Sets the style for the index view within the current environment.

`func labeledContentStyle<S>(S) -> some View`

Sets a style for labeled content.

`protocol LabeledContentStyle`

The appearance and behavior of a labeled content instance..

`struct LabeledContentStyleConfiguration`

The properties of a labeled content instance.

Instance Method

# labeledContentStyle(_:)

Sets a style for labeled content.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func labeledContentStyle<S>(_ style: S) -> some View where S : LabeledContentStyle
    

## See Also

### Grouping inputs

`struct Form`

A container for grouping controls used for data entry, such as in settings or
inspectors.

`func formStyle<S>(S) -> some View`

Sets the style for forms in a view hierarchy.

`struct LabeledContent`

A container for attaching a label to a value-bearing view.

Protocol

# LabeledContentStyle

The appearance and behavior of a labeled content instance..

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    protocol LabeledContentStyle

## Overview

Use `labeledContentStyle(_:)` to set a style on a view.

## Topics

### Getting built-in labeled content styles

`static var automatic: AutomaticLabeledContentStyle`

A labeled content style that resolves its appearance automatically based on
the current context.

Available when `Self` is `AutomaticLabeledContentStyle`.

### Creating custom labeled content styles

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Creates a view that represents the body of labeled content.

**Required**

` typealias Configuration`

The properties of a labeled content instance.

`associatedtype Body : View`

A view that represents the appearance and behavior of labeled content.

**Required**

### Supporting types

`struct AutomaticLabeledContentStyle`

The default labeled content style.

## Relationships

### Conforming Types

  * `AutomaticLabeledContentStyle`

## See Also

### Styling groups

`func controlGroupStyle<S>(S) -> some View`

Sets the style for control groups within this view.

`protocol ControlGroupStyle`

Defines the implementation of all control groups within a view hierarchy.

`struct ControlGroupStyleConfiguration`

The properties of a control group.

`func formStyle<S>(S) -> some View`

Sets the style for forms in a view hierarchy.

`protocol FormStyle`

The appearance and behavior of a form.

`struct FormStyleConfiguration`

The properties of a form instance.

`func groupBoxStyle<S>(S) -> some View`

Sets the style for group boxes within this view.

`protocol GroupBoxStyle`

A type that specifies the appearance and interaction of all group boxes within
a view hierarchy.

`struct GroupBoxStyleConfiguration`

The properties of a group box instance.

`func indexViewStyle<S>(S) -> some View`

Sets the style for the index view within the current environment.

`protocol IndexViewStyle`

Defines the implementation of all `IndexView` instances within a view
hierarchy.

`func labeledContentStyle<S>(S) -> some View`

Sets a style for labeled content.

`struct LabeledContentStyleConfiguration`

The properties of a labeled content instance.

Structure

# LabeledContentStyleConfiguration

The properties of a labeled content instance.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    struct LabeledContentStyleConfiguration

## Topics

### Configuring the label

`let label: LabeledContentStyleConfiguration.Label`

The label of the labeled content instance.

`struct Label`

A type-erased label of a labeled content instance.

### Configuring the content

`let content: LabeledContentStyleConfiguration.Content`

The content of the labeled content instance.

`struct Content`

A type-erased content of a labeled content instance.

## See Also

### Styling groups

`func controlGroupStyle<S>(S) -> some View`

Sets the style for control groups within this view.

`protocol ControlGroupStyle`

Defines the implementation of all control groups within a view hierarchy.

`struct ControlGroupStyleConfiguration`

The properties of a control group.

`func formStyle<S>(S) -> some View`

Sets the style for forms in a view hierarchy.

`protocol FormStyle`

The appearance and behavior of a form.

`struct FormStyleConfiguration`

The properties of a form instance.

`func groupBoxStyle<S>(S) -> some View`

Sets the style for group boxes within this view.

`protocol GroupBoxStyle`

A type that specifies the appearance and interaction of all group boxes within
a view hierarchy.

`struct GroupBoxStyleConfiguration`

The properties of a group box instance.

`func indexViewStyle<S>(S) -> some View`

Sets the style for the index view within the current environment.

`protocol IndexViewStyle`

Defines the implementation of all `IndexView` instances within a view
hierarchy.

`func labeledContentStyle<S>(S) -> some View`

Sets a style for labeled content.

`protocol LabeledContentStyle`

The appearance and behavior of a labeled content instance..

Instance Method

# presentedWindowStyle(_:)

Sets the style for windows created by interacting with this view.

macOS 11.0+

    
    
    func presentedWindowStyle<S>(_ style: S) -> some View where S : WindowStyle
    

## See Also

### Styling windows from a view inside the window

`func presentedWindowToolbarStyle<S>(S) -> some View`

Sets the style for the toolbar in windows created by interacting with this
view.

Instance Method

# presentedWindowToolbarStyle(_:)

Sets the style for the toolbar in windows created by interacting with this
view.

macOS 11.0+

    
    
    func presentedWindowToolbarStyle<S>(_ style: S) -> some View where S : WindowToolbarStyle
    

## See Also

### Styling windows from a view inside the window

`func presentedWindowStyle<S>(S) -> some View`

Sets the style for windows created by interacting with this view.

