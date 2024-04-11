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

