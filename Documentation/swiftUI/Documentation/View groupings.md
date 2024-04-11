Structure

# Group

A type that collects multiple instances of a content type — like views,
scenes, or commands — into a single unit.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct Group<Content>

## Overview

Use a group to collect multiple views into a single instance, without
affecting the layout of those views, like an `HStack`, `VStack`, or `Section`
would. After creating a group, any modifier you apply to the group affects all
of that group’s members. For example, the following code applies the
`headline` font to three views in a group.

Because you create a group of views with a `ViewBuilder`, you can use the
group’s initializer to produce different kinds of views from a conditional,
and then optionally apply modifiers to them. The following example uses a
`Group` to add a navigation bar title, regardless of the type of view the
conditional produces:

The modifier applies to all members of the group — and not to the group
itself. For example, if you apply `onAppear(perform:)` to the above group, it
applies to all of the views produced by the `if isLoggedIn` conditional, and
it executes every time `isLoggedIn` changes.

Because a group of views itself is a view, you can compose a group within
other view builders, including nesting within other groups. This allows you to
add large numbers of views to different view builder containers. The following
example uses a `Group` to collect 10 `Text` instances, meaning that the
vertical stack’s view builder returns only two views — the group, plus an
additional `Text`:

You can initialize groups with several types other than `View`, such as
`Scene` and `ToolbarContent`. The closure you provide to the group initializer
uses the corresponding builder type (`SceneBuilder`, `ToolbarContentBuilder`,
and so on), and the capabilities of these builders vary between types. For
example, you can use groups to return large numbers of scenes or toolbar
content instances, but not to return different scenes or toolbar content based
on conditionals.

## Topics

### Creating a group

`init(content: () -> Content)`

Creates a group of views.

Available when `Content` conforms to `View`.

`init(content: () -> Content)`

Creates a group of scenes.

Available when `Content` conforms to `Scene`.

`init(content: () -> Content)`

Creates a group of commands.

Available when `Content` conforms to `Commands`.

`init(content: () -> Content)`

Creates a group of toolbar content instances.

Available when `Content` conforms to `ToolbarContent`.

`init(content: () -> Content)`

Creates a group of customizable toolbar content instances.

Available when `Content` conforms to `CustomizableToolbarContent`.

`init<R>(content: () -> Content)`

Creates a group of table rows.

Available when `Content` conforms to `TableRowContent`.

`init<R, C>(content: () -> Content)`

Creates a group of table columns.

Available when `Content` conforms to `TableColumnContent`.

`init(content: () -> Content)`

Creates an instance that generates Rotor content by combining, in order, all
the Rotor content specified in the passed-in result builder.

Available when `Content` conforms to `AccessibilityRotorContent`.

### Initializers

`init(content: () -> Content)`

Creates a group of map content.

Available when `Content` conforms to `MapContent`.

### Default Implementations

API Reference

MapContent Implementations

## Relationships

### Conforms To

  * `AccessibilityRotorContent`

Conforms when `Content` conforms to `AccessibilityRotorContent`.

  * `Commands`

Conforms when `Content` conforms to `Commands`.

  * `CustomizableToolbarContent`

Conforms when `Content` conforms to `CustomizableToolbarContent`.

  * `MapContent`
  * `Scene`

Conforms when `Content` conforms to `Scene`.

  * `TableColumnContent`

Conforms when `Content` conforms to `TableColumnContent`.

  * `TableRowContent`

Conforms when `Content` conforms to `TableRowContent`.

  * `ToolbarContent`

Conforms when `Content` conforms to `CustomizableToolbarContent`.

  * `View`

Conforms when `Content` conforms to `View`.

Structure

# GroupBox

A stylized view, with an optional label, that visually collects a logical
grouping of content.

iOS 14.0+  iPadOS 14.0+  macOS 10.15+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    struct GroupBox<Label, Content> where Label : View, Content : View

## Overview

Use a group box when you want to visually distinguish a portion of your user
interface with an optional title for the boxed content.

The following example sets up a `GroupBox` with the label “End-User
Agreement”, and a long `agreementText` string in a `Text` view wrapped by a
`ScrollView`. The box also contains a `Toggle` for the user to interact with
after reading the text.

## Topics

### Creating a group box

`init(content: () -> Content)`

Creates an unlabeled group box with the provided view content.

Available when `Label` is `EmptyView` and `Content` conforms to `View`.

`init(content: () -> Content, label: () -> Label)`

Creates a group box with the provided label and view content.

`init(LocalizedStringKey, content: () -> Content)`

Creates a group box with the provided view content and title.

Available when `Label` is `Text` and `Content` conforms to `View`.

`init<S>(S, content: () -> Content)`

Creates a group box with the provided view content.

Available when `Label` is `Text` and `Content` conforms to `View`.

### Creating a group box from a configuration

`init(GroupBoxStyleConfiguration)`

Creates a group box based on a style configuration.

Available when `Label` is `GroupBoxStyleConfiguration.Label` and `Content` is
`GroupBoxStyleConfiguration.Content`.

### Deprecated initializers

`init(label: Label, content: () -> Content)`

Available when `Label` conforms to `View` and `Content` conforms to `View`.

## Relationships

### Conforms To

  * `View`

## See Also

### Grouping views into a box

`func groupBoxStyle<S>(S) -> some View`

Sets the style for group boxes within this view.

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

Structure

# Form

A container for grouping controls used for data entry, such as in settings or
inspectors.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    struct Form<Content> where Content : View

## Overview

SwiftUI applies platform-appropriate styling to views contained inside a form,
to group them together. Form-specific styling applies to things like buttons,
toggles, labels, lists, and more. Keep in mind that these stylings may be
platform-specific. For example, forms apppear as grouped lists on iOS, and as
aligned vertical stacks on macOS.

The following example shows a simple data entry form on iOS, grouped into two
sections. The supporting types (`NotifyMeAboutType` and `ProfileImageSize`)
and state variables (`notifyMeAbout`, `profileImageSize`,
`playNotificationSounds`, and `sendReadReceipts`) are omitted for simplicity.

On macOS, a similar form renders as a vertical stack. To adhere to macOS
platform conventions, this version doesn’t use sections, and uses colons at
the end of its labels. It also sets the picker to use the `inline` style,
which produces radio buttons on macOS.

## Topics

### Creating a form

`init(content: () -> Content)`

Creates a form with the provided content.

### Creating a form from a configuration

`init(FormStyleConfiguration)`

Creates a form based on a form style configuration.

Available when `Content` is `FormStyleConfiguration.Content`.

## Relationships

### Conforms To

  * `View`

## See Also

### Grouping inputs

`func formStyle<S>(S) -> some View`

Sets the style for forms in a view hierarchy.

`struct LabeledContent`

A container for attaching a label to a value-bearing view.

`func labeledContentStyle<S>(S) -> some View`

Sets a style for labeled content.

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

Structure

# LabeledContent

A container for attaching a label to a value-bearing view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    struct LabeledContent<Label, Content>

## Overview

The instance’s content represents a read-only or read-write value, and its
label identifies or describes the purpose of that value. The resulting element
has a layout that’s consistent with other framework controls and automatically
adapts to its container, like a form or toolbar. Some styles of labeled
content also apply styling or behaviors to the value content, like making
`Text` views selectable.

The following example associates a label with a custom view and has a layout
that matches the label of the `Picker`:

### Custom view labels

You can assemble labeled content with an explicit view for its label using the
`init(content:label:)` initializer. For example, you can rewrite the previous
labeled content example using a `Text` view:

The `label` view builder accepts any kind of view, like a `Label`:

### Textual labeled content

You can construct labeled content with string values or formatted values to
create read-only displays of textual values:

Wherever possible, SwiftUI makes this text selectable.

### Compositional elements

You can use labeled content as the label for other elements. For example, a
`NavigationLink` can present a summary value for the destination it links to:

In some cases, the styling of views used as the value content is specialized
as well. For example, while a `Toggle` in an inset group form on macOS is
styled as a switch by default, it’s styled as a checkbox when used as a value
element within a surrounding `LabeledContent` instance:

### Controlling label visibility

A label communicates the identity or purpose of the value, which is important
for accessibility. However, you might want to hide the label in the display,
and some controls or contexts may visually hide their label by default. The
`labelsHidden()` modifier allows controlling that visibility. The following
example hides both labels, producing only a group of the two value views:

### Styling labeled content

You can set label styles using the `labeledContentStyle(_:)` modifier. You can
also build custom styles using `LabeledContentStyle`.

## Topics

### Creating labeled content

`init(LocalizedStringKey, content: () -> Content)`

Creates a labeled view that generates its label from a localized string key.

Available when `Label` is `Text` and `Content` conforms to `View`.

`init<S>(S, content: () -> Content)`

Creates a labeled view that generates its label from a string.

Available when `Label` is `Text` and `Content` conforms to `View`.

`init(content: () -> Content, label: () -> Label)`

Creates a standard labeled element, with a view that conveys the value of the
element and a label.

Available when `Label` conforms to `View` and `Content` conforms to `View`.

### Creating informational views

`init<S>(LocalizedStringKey, value: S)`

Creates a labeled informational view.

Available when `Label` is `Text` and `Content` is `Text`.

`init<S1, S2>(S1, value: S2)`

Creates a labeled informational view.

Available when `Label` is `Text` and `Content` is `Text`.

### Creating formatted labeled content

`init<F>(LocalizedStringKey, value: F.FormatInput, format: F)`

Creates a labeled informational view from a formatted value.

Available when `Label` is `Text` and `Content` is `Text`.

`init<S, F>(S, value: F.FormatInput, format: F)`

Creates a labeled informational view from a formatted value.

Available when `Label` is `Text` and `Content` is `Text`.

### Creating labeled content from a configuration

`init(LabeledContentStyleConfiguration)`

Creates labeled content based on a labeled content style configuration.

Available when `Label` is `LabeledContentStyleConfiguration.Label` and
`Content` is `LabeledContentStyleConfiguration.Content`.

## Relationships

### Conforms To

  * `View`

Conforms when `Label` conforms to `View` and `Content` conforms to `View`.

## See Also

### Grouping inputs

`struct Form`

A container for grouping controls used for data entry, such as in settings or
inspectors.

`func formStyle<S>(S) -> some View`

Sets the style for forms in a view hierarchy.

`func labeledContentStyle<S>(S) -> some View`

Sets a style for labeled content.

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

Structure

# ControlGroup

A container view that displays semantically-related controls in a visually-
appropriate manner for the context

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 17.0+  visionOS
1.0+

    
    
    struct ControlGroup<Content> where Content : View

## Overview

You can provide an optional label to this view that describes its children.
This view may be used in different ways depending on the surrounding context.
For example, when you place the control group in a toolbar item, SwiftUI uses
the label when the group is moved to the toolbar’s overflow menu.

## Topics

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

`init<C>(LocalizedStringKey, content: () -> C)`

Creates a new control group with the specified content that generates its
label from a localized string key.

Available when `Content` conforms to `View`.

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

`init<C, S>(S, systemImage: String, content: () -> C)`

Creates a new control group with the specified content that generates its
label from a string and image name.

Available when `Content` conforms to `View`.

### Creating a configured control group

`init(ControlGroupStyleConfiguration)`

Creates a control group based on a style configuration.

Available when `Content` is `ControlGroupStyleConfiguration.Content`.

### Supporting types

`struct LabeledControlGroupContent`

A view that represents the body of a control group with a specified label.

## Relationships

### Conforms To

  * `View`

## See Also

### Presenting a group of controls

`func controlGroupStyle<S>(S) -> some View`

Sets the style for control groups within this view.

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

