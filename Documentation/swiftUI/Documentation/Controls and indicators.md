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

