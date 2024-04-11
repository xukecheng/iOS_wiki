Type Property

# automatic

The default toggle style.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static var automatic: DefaultToggleStyle { get }

Available when `Self` is `DefaultToggleStyle`.

## Discussion

Use this `ToggleStyle` to let SwiftUI pick a suitable style for the current
platform and context. Toggles use the `automatic` style by default, but you
might need to set it explicitly using the `toggleStyle(_:)` modifier to
override another style in the environment. For example, you can request
automatic styling for a toggle in an `HStack` that’s otherwise configured to
use the `button` style:

### Platform defaults

The `automatic` style produces an appearance that varies by platform, using
the following styles in most contexts:

Platform| Default style  
---|---  
iOS, iPadOS| `switch`  
macOS| `checkbox`  
tvOS| A tvOS-specific button style (see below)  
watchOS| `switch`  
  
The default style for tvOS behaves like a button. However, unlike the `button`
style that’s available in some other platforms, the tvOS toggle takes as much
horizontal space as its parent offers, and displays both the toggle’s label
and a text field that indicates the toggle’s state. You typically collect tvOS
toggles into a `List`:

### Contextual defaults

A toggle’s automatic appearance varies in certain contexts:

  * A toggle that appears as part of the content that you provide to one of the toolbar modifiers, like `toolbar(content:)`, uses the `button` style by default.

  * A toggle in a `Menu` uses a style that you can’t create explicitly:

SwiftUI shows the toggle’s label with a checkmark that appears only in the
`on` state:

Platform| Appearance  
---|---  
iOS, iPadOS|  
macOS|  
  

## See Also

### Getting built-in toggle styles

`static var button: ButtonToggleStyle`

A toggle style that displays as a button with its label as the title.

Available when `Self` is `ButtonToggleStyle`.

`static var checkbox: CheckboxToggleStyle`

A toggle style that displays a checkbox followed by its label.

Available when `Self` is `CheckboxToggleStyle`.

`static var `switch`: SwitchToggleStyle`

A toggle style that displays a leading label and a trailing switch.

Available when `Self` is `SwitchToggleStyle`.

Type Property

# button

A toggle style that displays as a button with its label as the title.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  watchOS 9.0+
visionOS 1.0+

    
    
    static var button: ButtonToggleStyle { get }

Available when `Self` is `ButtonToggleStyle`.

## Discussion

Apply this style to a `Toggle` or to a view hierarchy that contains toggles
using the `toggleStyle(_:)` modifier:

The style produces a button with a label that describes the purpose of the
toggle. The user taps or clicks the button to change the toggle’s state. The
button indicates the `on` state by filling in the background with its tint
color. You can change the tint color using the `tint(_:)` modifier. SwiftUI
uses this style as the default for toggles that appear in a toolbar.

The following table shows the toggle in both the `off` and `on` states,
respectively:

Platform| Appearance  
---|---  
iOS, iPadOS|  
macOS|  
  
A `Label` instance is a good choice for a button toggle’s label. Based on the
context, SwiftUI decides whether to display both the title and icon, as in the
example above, or just the icon, like when the toggle appears in a toolbar.
You can also control the label’s style by adding a `labelStyle(_:)` modifier.
In any case, SwiftUI always uses the title to identify the control using
VoiceOver.

## See Also

### Getting built-in toggle styles

`static var automatic: DefaultToggleStyle`

The default toggle style.

Available when `Self` is `DefaultToggleStyle`.

`static var checkbox: CheckboxToggleStyle`

A toggle style that displays a checkbox followed by its label.

Available when `Self` is `CheckboxToggleStyle`.

`static var `switch`: SwitchToggleStyle`

A toggle style that displays a leading label and a trailing switch.

Available when `Self` is `SwitchToggleStyle`.

Type Property

# checkbox

A toggle style that displays a checkbox followed by its label.

macOS 10.15+

    
    
    static var checkbox: CheckboxToggleStyle { get }

Available when `Self` is `CheckboxToggleStyle`.

## Discussion

Apply this style to a `Toggle` or to a view hierarchy that contains toggles
using the `toggleStyle(_:)` modifier:

The style produces a label that describes the purpose of the toggle and a
checkbox that shows the toggle’s state. To change the toggle’s state, the user
clicks the checkbox or its label:

The style aligns the trailing edge of the checkbox with the leading edge of
the label, and takes as much horizontal space as it needs to fit the label, up
to the amount offered by the toggle’s parent view.

This is the default style in macOS in most contexts when you don’t set a
style, or when you apply the `automatic` style. A `Form` is a convenient way
to present a collection of checkboxes with proper spacing and alignment. For
guidance on using checkboxes in your user interface, see Toggles in the Human
Interface Guidelines.

## See Also

### Getting built-in toggle styles

`static var automatic: DefaultToggleStyle`

The default toggle style.

Available when `Self` is `DefaultToggleStyle`.

`static var button: ButtonToggleStyle`

A toggle style that displays as a button with its label as the title.

Available when `Self` is `ButtonToggleStyle`.

`static var `switch`: SwitchToggleStyle`

A toggle style that displays a leading label and a trailing switch.

Available when `Self` is `SwitchToggleStyle`.

Type Property

# switch

A toggle style that displays a leading label and a trailing switch.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    static var `switch`: SwitchToggleStyle { get }

Available when `Self` is `SwitchToggleStyle`.

## Discussion

Apply this style to a `Toggle` or to a view hierarchy that contains toggles
using the `toggleStyle(_:)` modifier:

The style produces a label that describes the purpose of the toggle and a
switch that shows the toggle’s state. The user taps or clicks the switch to
change the toggle’s state. The default appearance is similar across platforms,
although the way you use switches in your user interface varies a little, as
described in Toggles in the Human Interface Guidelines.

  * iOS 
  * macOS 
  * watchOS 

In iOS and watchOS, the label and switch fill as much horizontal space as the
toggle’s parent offers by aligning the label’s leading edge and the switch’s
trailing edge with the containing view’s respective leading and trailing
edges. In macOS, the style uses a minimum of horizontal space by aligning the
trailing edge of the label with the leading edge of the switch. SwiftUI helps
you to manage the spacing and alignment when this style appears in a `Form`.

SwiftUI uses this style as the default for iOS and watchOS in most contexts
when you don’t set a style, or when you apply the `automatic` style.

## See Also

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

Instance Method

# makeBody(configuration:)

Creates a view that represents the body of a toggle.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @ViewBuilder
    func makeBody(configuration: Self.Configuration) -> Self.Body

**Required**

##  Parameters

`configuration`

    

The properties of the toggle, including a label and a binding to the toggle’s
state.

## Return Value

A view that has behavior and appearance that enables it to function as a
`Toggle`.

## Discussion

Implement this method when you define a custom toggle style that conforms to
the `ToggleStyle` protocol. Use the `configuration` input — a
`ToggleStyleConfiguration` instance — to access the toggle’s label and state.
Return a view that has the appearance and behavior of a toggle. For example
you can create a toggle that displays a label and a circle that’s either empty
or filled with a checkmark:

The `ChecklistToggleStyle` toggle style provides a way to both observe and
modify the toggle state: the circle fills for the on state, and users can tap
or click the toggle to change the state. By using a customized `Button` to
compose the toggle’s body, SwiftUI automatically provides the behaviors that
users expect from a control that has button-like characteristics.

You can present a collection of toggles that use this style in a stack:

When updating a view hierarchy, the system calls your implementation of the
`makeBody(configuration:)` method for each `Toggle` instance that uses the
associated style.

### Modify the current style

Rather than create an entirely new style, you can alternatively modify a
toggle’s current style. Use the `init(_:)` initializer inside the
`makeBody(configuration:)` method to create and modify a toggle based on a
`configuration` value. For example, you can create a style that adds padding
and a red border to the current style:

If you create a `redBorder` static variable from this style, you can apply the
style to toggles that already use another style, like the built-in `switch`
and `button` styles:

Both toggles appear with the usual styling, each with a red border:

Apply the custom style closer to the toggle than the modified style because
SwiftUI evaluates style view modifiers in order from outermost to innermost.
If you apply the styles in the other order, the red border style doesn’t have
an effect, because the built-in styles override it completely.

## See Also

### Creating custom toggle styles

`struct ToggleStyleConfiguration`

The properties of a toggle instance.

`typealias Configuration`

The properties of a toggle instance.

`associatedtype Body : View`

A view that represents the appearance and interaction of a toggle.

**Required**

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

Type Alias

# ToggleStyle.Configuration

The properties of a toggle instance.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    typealias Configuration = ToggleStyleConfiguration

## Discussion

You receive a `configuration` parameter of this type — which is an alias for
the `ToggleStyleConfiguration` type — when you implement the required
`makeBody(configuration:)` method in a custom toggle style implementation.

## See Also

### Creating custom toggle styles

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Creates a view that represents the body of a toggle.

**Required**

` struct ToggleStyleConfiguration`

The properties of a toggle instance.

`associatedtype Body : View`

A view that represents the appearance and interaction of a toggle.

**Required**

Associated Type

# Body

A view that represents the appearance and interaction of a toggle.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    associatedtype Body : View

**Required**

## Discussion

SwiftUI infers this type automatically based on the `View` instance that you
return from your implementation of the `makeBody(configuration:)` method.

## See Also

### Creating custom toggle styles

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Creates a view that represents the body of a toggle.

**Required**

` struct ToggleStyleConfiguration`

The properties of a toggle instance.

`typealias Configuration`

The properties of a toggle instance.

Structure

# DefaultToggleStyle

The default toggle style.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    struct DefaultToggleStyle

## Overview

Use the `automatic` static variable to create this style:

## Topics

### Creating the toggle style

`init()`

Creates a default toggle style.

### Supporting types

`func makeBody(configuration: DefaultToggleStyle.Configuration) -> some View`

Creates a view that represents the body of a toggle.

## Relationships

### Conforms To

  * `ToggleStyle`

## See Also

### Supporting types

`struct ButtonToggleStyle`

A toggle style that displays as a button with its label as the title.

`struct CheckboxToggleStyle`

A toggle style that displays a checkbox followed by its label.

`struct SwitchToggleStyle`

A toggle style that displays a leading label and a trailing switch.

Structure

# ButtonToggleStyle

A toggle style that displays as a button with its label as the title.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  watchOS 9.0+
visionOS 1.0+

    
    
    struct ButtonToggleStyle

## Overview

You can also use `button` to construct this style.

## Topics

### Creating the toggle style

`init()`

Creates a button toggle style.

### Supporting types

`func makeBody(configuration: ButtonToggleStyle.Configuration) -> some View`

Creates a view that represents the body of a toggle button.

## Relationships

### Conforms To

  * `ToggleStyle`

## See Also

### Supporting types

`struct DefaultToggleStyle`

The default toggle style.

`struct CheckboxToggleStyle`

A toggle style that displays a checkbox followed by its label.

`struct SwitchToggleStyle`

A toggle style that displays a leading label and a trailing switch.

Structure

# CheckboxToggleStyle

A toggle style that displays a checkbox followed by its label.

macOS 10.15+

    
    
    struct CheckboxToggleStyle

## Overview

Use the `checkbox` static variable to create this style:

## Topics

### Creating the toggle style

`init()`

Creates a checkbox toggle style.

### Supporting types

`func makeBody(configuration: CheckboxToggleStyle.Configuration) -> some View`

Creates a view that represents the body of a toggle checkbox.

## Relationships

### Conforms To

  * `ToggleStyle`

## See Also

### Supporting types

`struct DefaultToggleStyle`

The default toggle style.

`struct ButtonToggleStyle`

A toggle style that displays as a button with its label as the title.

`struct SwitchToggleStyle`

A toggle style that displays a leading label and a trailing switch.

Structure

# SwitchToggleStyle

A toggle style that displays a leading label and a trailing switch.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    struct SwitchToggleStyle

## Overview

Use the `switch` static variable to create this style:

## Topics

### Creating the toggle style

`init()`

Creates a switch toggle style.

### Supporting types

`func makeBody(configuration: SwitchToggleStyle.Configuration) -> some View`

Creates a view that represents the body of a toggle switch.

### Deprecated initializers

`init(tint: Color)`

Creates a switch style with a tint color.

Deprecated

## Relationships

### Conforms To

  * `ToggleStyle`

## See Also

### Supporting types

`struct DefaultToggleStyle`

The default toggle style.

`struct ButtonToggleStyle`

A toggle style that displays as a button with its label as the title.

`struct CheckboxToggleStyle`

A toggle style that displays a checkbox followed by its label.

