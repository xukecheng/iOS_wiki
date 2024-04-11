# ViewDimensions

Instance Property

# height

The view’s height.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var height: CGFloat { get }

## See Also

### Getting dimensions

`var width: CGFloat`

The view’s width.

Instance Property

# width

The view’s width.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var width: CGFloat { get }

## See Also

### Getting dimensions

`var height: CGFloat`

The view’s height.

Instance Subscript

# subscript(_:)

Gets the value of the given vertical guide.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    subscript(guide: VerticalAlignment) -> CGFloat { get }

## Overview

Find the offset of a particular guide in the corresponding view by using that
guide as an index to read from the context:

For information about using subscripts in Swift to access member elements of a
collection, list, or, sequence, see Subscripts in _The Swift Programming
Language_.

## See Also

### Accessing guide values

`subscript(HorizontalAlignment) -> CGFloat`

Gets the value of the given horizontal guide.

`subscript(explicit _: VerticalAlignment) -> CGFloat?`

Gets the explicit value of the given vertical alignment guide

`subscript(explicit _: HorizontalAlignment) -> CGFloat?`

Gets the explicit value of the given horizontal alignment guide.

Instance Subscript

# subscript(_:)

Gets the value of the given horizontal guide.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    subscript(guide: HorizontalAlignment) -> CGFloat { get }

## Overview

Find the offset of a particular guide in the corresponding view by using that
guide as an index to read from the context:

For information about using subscripts in Swift to access member elements of a
collection, list, or, sequence, see Subscripts in _The Swift Programming
Language_.

## See Also

### Accessing guide values

`subscript(VerticalAlignment) -> CGFloat`

Gets the value of the given vertical guide.

`subscript(explicit _: VerticalAlignment) -> CGFloat?`

Gets the explicit value of the given vertical alignment guide

`subscript(explicit _: HorizontalAlignment) -> CGFloat?`

Gets the explicit value of the given horizontal alignment guide.

Instance Subscript

# subscript(explicit:)

Gets the explicit value of the given vertical alignment guide

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    subscript(explicit guide: VerticalAlignment) -> CGFloat? { get }

## Overview

Find the vertical offset of a particular guide in the corresponding view by
using that guide as an index to read from the context:

This subscript returns `nil` if no value exists for the guide.

For information about using subscripts in Swift to access member elements of a
collection, list, or, sequence, see Subscripts in _The Swift Programming
Language_.

## See Also

### Accessing guide values

`subscript(VerticalAlignment) -> CGFloat`

Gets the value of the given vertical guide.

`subscript(HorizontalAlignment) -> CGFloat`

Gets the value of the given horizontal guide.

`subscript(explicit _: HorizontalAlignment) -> CGFloat?`

Gets the explicit value of the given horizontal alignment guide.

Instance Subscript

# subscript(explicit:)

Gets the explicit value of the given horizontal alignment guide.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    subscript(explicit guide: HorizontalAlignment) -> CGFloat? { get }

## Overview

Find the horizontal offset of a particular guide in the corresponding view by
using that guide as an index to read from the context:

This subscript returns `nil` if no value exists for the guide.

For information about using subscripts in Swift to access member elements of a
collection, list, or, sequence, see Subscripts in _The Swift Programming
Language_.

## See Also

### Accessing guide values

`subscript(VerticalAlignment) -> CGFloat`

Gets the value of the given vertical guide.

`subscript(HorizontalAlignment) -> CGFloat`

Gets the value of the given horizontal guide.

`subscript(explicit _: VerticalAlignment) -> CGFloat?`

Gets the explicit value of the given vertical alignment guide



# Visibility

Case

# Visibility.automatic

The element may be visible or hidden depending on the policies of the
component accepting the visibility configuration.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    case automatic

## Discussion

For example, some components employ different automatic behavior depending on
factors including the platform, the surrounding container, user settings, etc.

## See Also

### Getting visibility options

`case visible`

The element may be visible.

`case hidden`

The element may be hidden.

Case

# Visibility.visible

The element may be visible.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    case visible

## Discussion

Some APIs may use this value to represent a hint or preference, rather than a
mandatory assertion. For example, setting list row separator visibility to
`visible` using the `listRowSeparator(_:edges:)` modifier may not always
result in any visible separators, especially for list styles that do not
include separators as part of their design.

## See Also

### Getting visibility options

`case automatic`

The element may be visible or hidden depending on the policies of the
component accepting the visibility configuration.

`case hidden`

The element may be hidden.

Case

# Visibility.hidden

The element may be hidden.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    case hidden

## Discussion

Some APIs may use this value to represent a hint or preference, rather than a
mandatory assertion. For example, setting confirmation dialog title visibility
to `hidden` using the
`confirmationDialog(_:isPresented:titleVisibility:actions:)` modifier may not
always hide the dialog title, which is required on some platforms.

## See Also

### Getting visibility options

`case automatic`

The element may be visible or hidden depending on the policies of the
component accepting the visibility configuration.

`case visible`

The element may be visible.



# VerticalPageTabViewStyle.TransitionStyle

Type Property

# automatic

Automatic transition style

watchOS 10.0+

    
    
    static let automatic: VerticalPageTabViewStyle.TransitionStyle

## See Also

### Getting the transition styles

`static let blur: VerticalPageTabViewStyle.TransitionStyle`

A transition style that blurs content between each tab

`static let identity: VerticalPageTabViewStyle.TransitionStyle`

A transition style that has no animation between each tab

Type Property

# blur

A transition style that blurs content between each tab

watchOS 10.0+

    
    
    static let blur: VerticalPageTabViewStyle.TransitionStyle

## See Also

### Getting the transition styles

`static let automatic: VerticalPageTabViewStyle.TransitionStyle`

Automatic transition style

`static let identity: VerticalPageTabViewStyle.TransitionStyle`

A transition style that has no animation between each tab

Type Property

# identity

A transition style that has no animation between each tab

watchOS 10.0+

    
    
    static let identity: VerticalPageTabViewStyle.TransitionStyle

## See Also

### Getting the transition styles

`static let automatic: VerticalPageTabViewStyle.TransitionStyle`

Automatic transition style

`static let blur: VerticalPageTabViewStyle.TransitionStyle`

A transition style that blurs content between each tab



# View groupings

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



# View

Instance Property

# body

The content and behavior of the view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @ViewBuilder @MainActor
    var body: Self.Body { get }

**Required** Default implementations provided.

## Discussion

When you implement a custom view, you must implement a computed `body`
property to provide the content for your view. Return a view that’s composed
of built-in views that SwiftUI provides, plus other composite views that
you’ve already defined:

For more information about composing views and a view hierarchy, see Declaring
a custom view.

## Default Implementations

### View Implementations

`var body: Never`

Declares the content and behavior of this view.

`var body: Never`

Declares the content and behavior of this view.

`var body: _ShapeView<Self, ForegroundStyle>`

The content and behavior of the view.

`var body: Never`

Declares the content and behavior of this view.

`var body: Never`

Declares the content and behavior of this view.

`var body: Never`

Declares the content and behavior of this view.

## See Also

### Implementing a custom view

`associatedtype Body : View`

The type of view representing the body of this view.

**Required**

` func modifier<T>(T) -> ModifiedContent<Self, T>`

Applies a modifier to a view and returns a new view.

API Reference

Previews in Xcode

Generate dynamic, interactive previews of your custom views.

Associated Type

# Body

The type of view representing the body of this view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    associatedtype Body : View

**Required**

## Discussion

When you create a custom view, Swift infers this type from your implementation
of the required `body` property.

## See Also

### Implementing a custom view

`var body: Self.Body`

The content and behavior of the view.

**Required** Default implementations provided.

`func modifier<T>(T) -> ModifiedContent<Self, T>`

Applies a modifier to a view and returns a new view.

API Reference

Previews in Xcode

Generate dynamic, interactive previews of your custom views.

Instance Method

# modifier(_:)

Applies a modifier to a view and returns a new view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func modifier<T>(_ modifier: T) -> ModifiedContent<Self, T>

##  Parameters

`modifier`

    

The modifier to apply to this view.

## Discussion

Use this modifier to combine a `View` and a `ViewModifier`, to create a new
view. For example, if you create a view modifier for a new kind of caption
with blue text surrounded by a rounded rectangle:

You can use `modifier(_:)` to extend `View` to create new modifier for
applying the `BorderedCaption` defined above:

Then you can apply the bordered caption to any view:

## See Also

### Modifying a view

Configuring views

Adjust the characteristics of a view by applying view modifiers.

Reducing view modifier maintenance

Bundle view modifiers that you regularly reuse into a custom view modifier.

`protocol ViewModifier`

A modifier that you apply to a view or another view modifier, producing a
different version of the original value.

`struct EmptyModifier`

An empty, or identity, modifier, used during development to switch modifiers
at compile time.

`struct ModifiedContent`

A value with a modifier applied to it.

`protocol EnvironmentalModifier`

A modifier that must resolve to a concrete modifier in an environment before
use.

Collection

API Collection

# Previews in Xcode

Generate dynamic, interactive previews of your custom views.

## Overview

When you create a custom `View` with SwiftUI, Xcode can display a preview of
the view’s content that stays up-to-date as you make changes to the view’s
code. You use one of the preview macros — like `Preview(_:body:)` — to tell
Xcode what to display. Xcode shows the preview in a canvas beside your code.

Different preview macros enable different kinds of configuration. For example,
you can add traits that affect the preview’s appearance using the
`Preview(_:traits:_:body:)` macro or add custom viewpoints for the preview
using the `Preview(_:traits:body:cameras:)` macro. You can also check how your
view behaves inside a specific scene type. For example, in visionOS you can
use the `Preview(_:immersionStyle:traits:body:)` macro to preview your view
inside an `ImmersiveSpace`.

You typically rely on preview macros to create previews in your code. However,
if you can’t get the behavior you need using a preview macro, you can use the
`PreviewProvider` protocol and its associated supporting types to define and
configure a preview.

## Topics

### Creating a preview

`macro Preview(String?, body: () -> any View)`

Creates a preview of a SwiftUI view.

`macro Preview(String?, traits: PreviewTrait<Preview.ViewTraits>,
PreviewTrait<Preview.ViewTraits>..., body: () -> any View)`

Creates a preview of a SwiftUI view using the specified traits.

`macro Preview(String?, traits: PreviewTrait<Preview.ViewTraits>..., body: ()
-> any View, cameras: () -> [PreviewCamera])`

Creates a preview of a SwiftUI view using the specified traits and custom
viewpoints.

### Creating a preview in the context of a scene

`macro Preview<Style>(String?, immersionStyle: Style, traits:
PreviewTrait<Preview.ViewTraits>..., body: () -> any View)`

Creates a preview of a SwiftUI view in an immersive space.

`macro Preview<Style>(String?, immersionStyle: Style, traits:
PreviewTrait<Preview.ViewTraits>..., body: () -> any View, cameras: () ->
[PreviewCamera])`

Creates a preview of a SwiftUI view in an immersive space with custom
viewpoints.

`macro Preview<Style>(String?, windowStyle: Style, traits:
PreviewTrait<Preview.ViewTraits>..., body: () -> any View)`

Creates a preview of a SwiftUI view in a window.

`macro Preview<Style>(String?, windowStyle: Style, traits:
PreviewTrait<Preview.ViewTraits>..., body: () -> any View, cameras: () ->
[PreviewCamera])`

Creates a preview of a SwiftUI view in a window with custom viewpoints.

### Defining a preview

`protocol PreviewProvider`

A type that produces view previews in Xcode.

`enum PreviewPlatform`

Platforms that can run the preview.

`func previewDisplayName(String?) -> some View`

Sets a user visible name to show in the canvas for a preview.

### Customizing a preview

`func previewDevice(PreviewDevice?) -> some View`

Overrides the device for a preview.

`struct PreviewDevice`

A simulator device that runs a preview.

`func previewLayout(PreviewLayout) -> some View`

Overrides the size of the container for the preview.

`func previewInterfaceOrientation(InterfaceOrientation) -> some View`

Overrides the orientation of the preview.

`struct InterfaceOrientation`

The orientation of the interface from the user’s perspective.

### Setting a context

`func previewContext<C>(C) -> some View`

Declares a context for the preview.

`protocol PreviewContext`

A context type for use with a preview.

`protocol PreviewContextKey`

A key type for a preview context.

## See Also

### Tool support

API Reference

Xcode library customization

Expose custom views and modifiers in the Xcode library.

Collection

API Collection

# Accessibility modifiers

Make your SwiftUI apps accessible to everyone, including people with
disabilities.

## Overview

Like all Apple UI frameworks, SwiftUI comes with built-in accessibility
support. The framework introspects common elements like navigation views,
lists, text fields, sliders, buttons, and so on, and provides basic
accessibility labels and values by default. You don’t have to do any extra
work to enable these standard accessibility features.

SwiftUI also provides tools to help you enhance the accessibility of your app.
For example, you can explicitly add accessibility labels to elements in your
UI using the `accessibilityLabel(_:)` or the `accessibilityValue(_:)` view
modifier.

To learn more about adding accessibility features to your app, see
Accessibility fundamentals.

## Topics

### Labels

`func accessibilityLabel<S>(S) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Adds a label to the view that describes its contents.

`func accessibilityLabel(Text) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Adds a label to the view that describes its contents.

`func accessibilityLabel(LocalizedStringKey) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Adds a label to the view that describes its contents.

`func accessibilityInputLabels([LocalizedStringKey]) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Sets alternate input labels with which users identify a view.

`func accessibilityInputLabels<S>([S]) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Sets alternate input labels with which users identify a view.

`func accessibilityInputLabels([Text]) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Sets alternate input labels with which users identify a view.

`func accessibilityLabeledPair<ID>(role: AccessibilityLabeledPairRole, id: ID,
in: Namespace.ID) -> some View`

Pairs an accessibility element representing a label with the element for the
matching content.

### Values

`func accessibilityValue<S>(S) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Adds a textual description of the value that the view contains.

`func accessibilityValue(LocalizedStringKey) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Adds a textual description of the value that the view contains.

`func accessibilityValue(Text) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Adds a textual description of the value that the view contains.

### Hints

`func accessibilityHint(LocalizedStringKey) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Communicates to the user what happens after performing the view’s action.

`func accessibilityHint(Text) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Communicates to the user what happens after performing the view’s action.

`func accessibilityHint<S>(S) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Communicates to the user what happens after performing the view’s action.

### Actions

`func accessibilityAction(AccessibilityActionKind, () -> Void) ->
ModifiedContent<Self, AccessibilityAttachmentModifier>`

Adds an accessibility action to the view. Actions allow assistive
technologies, such as the VoiceOver, to interact with the view by invoking the
action.

`func accessibilityActions<Content>(() -> Content) -> some View`

Adds multiple accessibility actions to the view.

`func accessibilityAction(named: Text, () -> Void) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Adds an accessibility action to the view. Actions allow assistive
technologies, such as the VoiceOver, to interact with the view by invoking the
action.

`func accessibilityAction<S>(named: S, () -> Void) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Adds an accessibility action to the view. Actions allow assistive
technologies, such as the VoiceOver, to interact with the view by invoking the
action.

`func accessibilityAction(named: LocalizedStringKey, () -> Void) ->
ModifiedContent<Self, AccessibilityAttachmentModifier>`

Adds an accessibility action to the view. Actions allow assistive
technologies, such as the VoiceOver, to interact with the view by invoking the
action.

`func accessibilityAction<Label>(action: () -> Void, label: () -> Label) ->
some View`

Adds an accessibility action to the view. Actions allow assistive
technologies, such as the VoiceOver, to interact with the view by invoking the
action.

`func accessibilityAdjustableAction((AccessibilityAdjustmentDirection) ->
Void) -> ModifiedContent<Self, AccessibilityAttachmentModifier>`

Adds an accessibility adjustable action to the view. Actions allow assistive
technologies, such as the VoiceOver, to interact with the view by invoking the
action.

`func accessibilityScrollAction((Edge) -> Void) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Adds an accessibility scroll action to the view. Actions allow assistive
technologies, such as the VoiceOver, to interact with the view by invoking the
action.

### Gestures

`func accessibilityActivationPoint(CGPoint) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

The activation point for an element is the location assistive technologies use
to initiate gestures.

`func accessibilityActivationPoint(UnitPoint) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

The activation point for an element is the location assistive technologies use
to initiate gestures.

`func accessibilityDirectTouch(Bool, options: AccessibilityDirectTouchOptions)
-> ModifiedContent<Self, AccessibilityAttachmentModifier>`

Explicitly set whether this accessibility element is a direct touch area.
Direct touch areas passthrough touch events to the app rather than being
handled through an assistive technology, such as VoiceOver. The modifier
accepts an optional `AccessibilityDirectTouchOptions` option set to customize
the functionality of the direct touch area.

`func accessibilityZoomAction((AccessibilityZoomGestureAction) -> Void) ->
ModifiedContent<Self, AccessibilityAttachmentModifier>`

Adds an accessibility zoom action to the view. Actions allow assistive
technologies, such as VoiceOver, to interact with the view by invoking the
action.

### Elements

`func accessibilityElement(children: AccessibilityChildBehavior) -> some View`

Creates a new accessibility element, or modifies the
`AccessibilityChildBehavior` of the existing accessibility element.

`func accessibilityChildren<V>(children: () -> V) -> some View`

Replaces the existing accessibility element’s children with one or more new
synthetic accessibility elements.

`func accessibilityHidden(Bool) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Specifies whether to hide this view from system accessibility features.

### Custom controls

`func accessibilityRepresentation<V>(representation: () -> V) -> some View`

Replaces one or more accessibility elements for this view with new
accessibility elements.

`func accessibilityRespondsToUserInteraction(Bool) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Explicitly set whether this Accessibility element responds to user interaction
and would thus be interacted with by technologies such as Switch Control,
Voice Control or Full Keyboard Access.

### Custom content

`func accessibilityCustomContent(AccessibilityCustomContentKey,
LocalizedStringKey, importance: AXCustomContent.Importance) ->
ModifiedContent<Self, AccessibilityAttachmentModifier>`

Add additional accessibility information to the view.

`func accessibilityCustomContent(AccessibilityCustomContentKey, Text?,
importance: AXCustomContent.Importance) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Add additional accessibility information to the view.

`func accessibilityCustomContent<V>(LocalizedStringKey, V, importance:
AXCustomContent.Importance) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Add additional accessibility information to the view.

`func accessibilityCustomContent(Text, Text, importance:
AXCustomContent.Importance) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Add additional accessibility information to the view.

`func accessibilityCustomContent(LocalizedStringKey, LocalizedStringKey,
importance: AXCustomContent.Importance) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Add additional accessibility information to the view.

`func accessibilityCustomContent<V>(AccessibilityCustomContentKey, V,
importance: AXCustomContent.Importance) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Add additional accessibility information to the view.

`func accessibilityCustomContent(LocalizedStringKey, Text, importance:
AXCustomContent.Importance) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Add additional accessibility information to the view.

### Creating rotors

`func accessibilityRotor<Content>(LocalizedStringKey, entries: () -> Content)
-> some View`

Create an Accessibility Rotor with the specified user-visible label, and
entries generated from the content closure.

`func accessibilityRotor<Content>(Text, entries: () -> Content) -> some View`

Create an Accessibility Rotor with the specified user-visible label, and
entries generated from the content closure.

`func accessibilityRotor<L, Content>(L, entries: () -> Content) -> some View`

Create an Accessibility Rotor with the specified user-visible label, and
entries generated from the content closure.

`func accessibilityRotor<EntryModel, ID>(LocalizedStringKey, entries:
[EntryModel], entryID: KeyPath<EntryModel, ID>, entryLabel:
KeyPath<EntryModel, String>) -> some View`

Create an Accessibility Rotor with the specified user-visible label and
entries.

`func accessibilityRotor<EntryModel, ID>(Text, entries: [EntryModel], entryID:
KeyPath<EntryModel, ID>, entryLabel: KeyPath<EntryModel, String>) -> some
View`

Create an Accessibility Rotor with the specified user-visible label and
entries.

`func accessibilityRotor<L, EntryModel, ID>(L, entries: [EntryModel], entryID:
KeyPath<EntryModel, ID>, entryLabel: KeyPath<EntryModel, String>) -> some
View`

Create an Accessibility Rotor with the specified user-visible label and
entries.

`func accessibilityRotor<EntryModel>(LocalizedStringKey, entries:
[EntryModel], entryLabel: KeyPath<EntryModel, String>) -> some View`

Create an Accessibility Rotor with the specified user-visible label and
entries.

`func accessibilityRotor<EntryModel>(Text, entries: [EntryModel], entryLabel:
KeyPath<EntryModel, String>) -> some View`

Create an Accessibility Rotor with the specified user-visible label and
entries.

`func accessibilityRotor<L, EntryModel>(L, entries: [EntryModel], entryLabel:
KeyPath<EntryModel, String>) -> some View`

Create an Accessibility Rotor with the specified user-visible label and
entries.

`func accessibilityRotor(LocalizedStringKey, textRanges:
[Range<String.Index>]) -> some View`

Create an Accessibility Rotor with the specified user-visible label and
entries for each of the specified ranges. The Rotor will be attached to the
current Accessibility element, and each entry will go the specified range of
that element.

`func accessibilityRotor(Text, textRanges: [Range<String.Index>]) -> some
View`

Create an Accessibility Rotor with the specified user-visible label and
entries for each of the specified ranges. The Rotor will be attached to the
current Accessibility element, and each entry will go the specified range of
that element.

`func accessibilityRotor<L>(L, textRanges: [Range<String.Index>]) -> some
View`

Create an Accessibility Rotor with the specified user-visible label and
entries for each of the specified ranges. The Rotor will be attached to the
current Accessibility element, and each entry will go the specified range of
that element.

### Replacing system rotors

`func accessibilityRotor<Content>(AccessibilitySystemRotor, entries: () ->
Content) -> some View`

Create an Accessibility Rotor replacing the specified system-provided Rotor.

`func accessibilityRotor<EntryModel, ID>(AccessibilitySystemRotor, entries:
[EntryModel], entryID: KeyPath<EntryModel, ID>, entryLabel:
KeyPath<EntryModel, String>) -> some View`

Create an Accessibility Rotor replacing the specified system-provided Rotor.

`func accessibilityRotor<EntryModel>(AccessibilitySystemRotor, entries:
[EntryModel], entryLabel: KeyPath<EntryModel, String>) -> some View`

Create an Accessibility Rotor replacing the specified system-provided Rotor.

`func accessibilityRotor(AccessibilitySystemRotor, textRanges:
[Range<String.Index>]) -> some View`

Create an Accessibility Rotor replacing the specified system-provided Rotor.
The Rotor will be attached to the current Accessibility element, and each
entry will go the specified range of that element.

### Configuring rotors

`func accessibilityRotorEntry<ID>(id: ID, in: Namespace.ID) -> some View`

Defines an explicit identifier tying an Accessibility element for this view to
an entry in an Accessibility Rotor.

`func accessibilityLinkedGroup<ID>(id: ID, in: Namespace.ID) -> some View`

Links multiple accessibility elements so that the user can quickly navigate
from one element to another, even when the elements are not near each other in
the accessibility hierarchy.

`func accessibilitySortPriority(Double) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Sets the sort priority order for this view’s accessibility element, relative
to other elements at the same level.

### Focus

`func accessibilityFocused(AccessibilityFocusState<Bool>.Binding) -> some
View`

Modifies this view by binding its accessibility element’s focus state to the
given boolean state value.

`func accessibilityFocused<Value>(AccessibilityFocusState<Value>.Binding,
equals: Value) -> some View`

Modifies this view by binding its accessibility element’s focus state to the
given state value.

### Traits

`func accessibilityAddTraits(AccessibilityTraits) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Adds the given traits to the view.

`func accessibilityRemoveTraits(AccessibilityTraits) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Removes the given traits from this view.

### Identity

`func accessibilityIdentifier(String) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Uses the string you specify to identify the view.

### Color inversion

`func accessibilityIgnoresInvertColors(Bool) -> some View`

Sets whether this view should ignore the system Smart Invert setting.

### Content descriptions

`func accessibilityTextContentType(AccessibilityTextContentType) ->
ModifiedContent<Self, AccessibilityAttachmentModifier>`

Sets an accessibility text content type.

`func accessibilityHeading(AccessibilityHeadingLevel) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Sets the accessibility level of this heading.

### VoiceOver

`func speechAdjustedPitch(Double) -> some View`

Raises or lowers the pitch of spoken text.

`func speechAlwaysIncludesPunctuation(Bool) -> some View`

Sets whether VoiceOver should always speak all punctuation in the text view.

`func speechAnnouncementsQueued(Bool) -> some View`

Controls whether to queue pending announcements behind existing speech rather
than interrupting speech in progress.

`func speechSpellsOutCharacters(Bool) -> some View`

Sets whether VoiceOver should speak the contents of the text view character by
character.

### Charts

`func accessibilityChartDescriptor<R>(R) -> some View`

Adds a descriptor to a View that represents a chart to make the chart’s
contents accessible to all users.

### Large content

`func accessibilityShowsLargeContentViewer() -> some View`

Adds a default large content view to be shown by the large content viewer.

`func accessibilityShowsLargeContentViewer<V>(() -> V) -> some View`

Adds a custom large content view to be shown by the large content viewer.

### Quick actions

`func accessibilityQuickAction<Style, Content>(style: Style, content: () ->
Content) -> some View`

Adds a quick action to be shown by the system when active.

`func accessibilityQuickAction<Style, Content>(style: Style, isActive:
Binding<Bool>, content: () -> Content) -> some View`

Adds a quick action to be shown by the system when active.

## See Also

### Configuring view elements

API Reference

Appearance modifiers

Configure a view’s foreground and background styles, controls, and visibility.

API Reference

Text and symbol modifiers

Manage the rendering, selection, and entry of text in your view.

API Reference

Auxiliary view modifiers

Add and configure supporting views, like toolbars and context menus.

API Reference

Chart view modifiers

Configure charts that you declare with Swift Charts.

Collection

API Collection

# Appearance modifiers

Configure a view’s foreground and background styles, controls, and visibility.

## Overview

Use these modifiers to configure the appearance of a view, including the use
of color and tint, and the application of overlays and background elements.
Control the visibility of a view and specific elements within a view. Manage
the shape and size of various controls.

For information about configuring views, see View configuration.

## Topics

### Colors and patterns

`func backgroundStyle<S>(S) -> some View`

Sets the specified style to render backgrounds within the view.

`func foregroundStyle<S>(S) -> some View`

Sets a view’s foreground elements to use a given style.

`func foregroundStyle<S1, S2>(S1, S2) -> some View`

Sets the primary and secondary levels of the foreground style in the child
view.

`func foregroundStyle<S1, S2, S3>(S1, S2, S3) -> some View`

Sets the primary, secondary, and tertiary levels of the foreground style.

`func allowedDynamicRange(Image.DynamicRange?) -> some View`

Returns a new view configured with the specified allowed dynamic range.

### Tint

`func tint<S>(S?) -> some View`

Sets the tint within this view.

`func tint(Color?) -> some View`

Sets the tint color within this view.

`func listRowSeparatorTint(Color?, edges: VerticalEdge.Set) -> some View`

Sets the tint color associated with a row.

`func listSectionSeparatorTint(Color?, edges: VerticalEdge.Set) -> some View`

Sets the tint color associated with a section.

`func listItemTint(Color?) -> some View`

Sets a fixed tint color for content in a list.

`func listItemTint(ListItemTint?) -> some View`

Sets the tint effect for content in a list.

### Light and dark appearance

`func preferredColorScheme(ColorScheme?) -> some View`

Sets the preferred color scheme for this presentation.

`func preferredSurroundingsEffect(SurroundingsEffect?) -> some View`

Applies an effect to passthrough video.

### Foreground elements

`func border<S>(S, width: CGFloat) -> some View`

Adds a border to this view with the specified style and width.

`func overlay<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify in front of this view.

`func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Layers the specified style in front of this view.

`func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Layers a shape that you specify in front of this view.

### Background elements

`func background<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify behind this view.

`func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to a style.

`func background(ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to the default background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with the default
background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with the default background
style.

`func alternatingRowBackgrounds(AlternatingRowBackgroundBehavior) -> some
View`

Overrides whether lists and tables in this view have alternating row
backgrounds.

`func listRowBackground<V>(V?) -> some View`

Places a custom background view behind a list row item.

`func scrollContentBackground(Visibility) -> some View`

Specifies the visibility of the background for scrollable views within this
view.

`func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some
View`

Sets the container background of the enclosing container using a view.

`func containerBackground<V>(for: ContainerBackgroundPlacement, alignment:
Alignment, content: () -> V) -> some View`

Sets the container background of the enclosing container using a view.

`func glassBackgroundEffect(displayMode: GlassBackgroundDisplayMode) -> some
View`

Fills the view’s background with a glass material that’s shaped as a
container-relative rounded rectangle.

`func glassBackgroundEffect<S>(in: S, displayMode: GlassBackgroundDisplayMode)
-> some View`

Fills the view’s background with a glass material using a shape that you
specify.

### Control configuration

`func defaultWheelPickerItemHeight(CGFloat) -> some View`

Sets the default wheel-style picker item height.

`func horizontalRadioGroupLayout() -> some View`

Sets the style for radio group style pickers within this view to be
horizontally positioned with the radio buttons inside the layout.

`func controlSize(ControlSize) -> some View`

Sets the size for controls within this view.

`func buttonBorderShape(ButtonBorderShape) -> some View`

Sets the border shape for buttons in this view.

`func buttonRepeatBehavior(ButtonRepeatBehavior) -> some View`

Sets whether buttons in this view should repeatedly trigger their actions on
prolonged interactions.

`func headerProminence(Prominence) -> some View`

Sets the header prominence for this view.

`func scrollDisabled(Bool) -> some View`

Disables or enables scrolling in scrollable views.

`func scrollBounceBehavior(ScrollBounceBehavior, axes: Axis.Set) -> some View`

Configures the bounce behavior of scrollable views along the specified axis.

`func scrollIndicatorsFlash(onAppear: Bool) -> some View`

Flashes the scroll indicators of a scrollable view when it appears.

`func scrollIndicatorsFlash(trigger: some Equatable) -> some View`

Flashes the scroll indicators of scrollable views when a value changes.

`func menuOrder(MenuOrder) -> some View`

Sets the preferred order of items for menus presented from this view.

`func menuActionDismissBehavior(MenuActionDismissBehavior) -> some View`

Tells a menu whether to dismiss after performing an action.

`func paletteSelectionEffect(PaletteSelectionEffect) -> some View`

Specifies the selection effect to apply to a palette item.

`func typeSelectEquivalent(Text?) -> some View`

Sets an explicit type select equivalent text in a collection, such as a list
or table.

`func typeSelectEquivalent(LocalizedStringKey) -> some View`

Sets an explicit type select equivalent text in a collection, such as a list
or table.

`func typeSelectEquivalent<S>(S) -> some View`

Sets an explicit type select equivalent text in a collection, such as a list
or table.

### Symbol effects

`func symbolEffect<T>(T, options: SymbolEffectOptions, isActive: Bool) -> some
View`

Returns a new view with a symbol effect added to it.

`func symbolEffect<T, U>(T, options: SymbolEffectOptions, value: U) -> some
View`

Returns a new view with a symbol effect added to it.

`func symbolEffectsRemoved(Bool) -> some View`

Returns a new view with its inherited symbol image effects either removed or
left unchanged.

### Privacy and redaction

`func privacySensitive(Bool) -> some View`

Marks the view as containing sensitive, private user data.

`func redacted(reason: RedactionReasons) -> some View`

Adds a reason to apply a redaction to this view hierarchy.

`func unredacted() -> some View`

Removes any reason to apply a redaction to this view hierarchy.

`func invalidatableContent(Bool) -> some View`

Mark the receiver as their content might be invalidated.

### Visibility

`func hidden() -> some View`

Hides this view unconditionally.

`func labelsHidden() -> some View`

Hides the labels of any controls contained within this view.

`func menuIndicator(Visibility) -> some View`

Sets the menu indicator visibility for controls within this view.

`func listRowSeparator(Visibility, edges: VerticalEdge.Set) -> some View`

Sets the display mode for the separator associated with this specific row.

`func listSectionSeparator(Visibility, edges: VerticalEdge.Set) -> some View`

Sets whether to hide the separator associated with a list section.

`func persistentSystemOverlays(Visibility) -> some View`

Sets the preferred visibility of the non-transient system views overlaying the
app.

`func scrollIndicators(ScrollIndicatorVisibility, axes: Axis.Set) -> some
View`

Sets the visibility of scroll indicators within this view.

`func scrollClipDisabled(Bool) -> some View`

Sets whether a scroll view clips its content to its bounds.

`func tableColumnHeaders(Visibility) -> some View`

Controls the visibility of a `Table`’s column header views.

`func upperLimbVisibility(Visibility) -> some View`

Sets the preferred visibility of the user’s upper limbs, while an
`ImmersiveSpace` scene is presented.

### Sensory feedback

`func sensoryFeedback<T>(SensoryFeedback, trigger: T) -> some View`

Plays the specified `feedback` when the provided `trigger` value changes.

`func sensoryFeedback<T>(trigger: T, (T, T) -> SensoryFeedback?) -> some View`

Plays feedback when returned from the `feedback` closure after the provided
`trigger` value changes.

`func sensoryFeedback<T>(SensoryFeedback, trigger: T, condition: (T, T) ->
Bool) -> some View`

Plays the specified `feedback` when the provided `trigger` value changes and
the `condition` closure returns `true`.

### Widget configuration

`func widgetAccentable(Bool) -> some View`

Adds the view and all of its subviews to the accented group.

`func widgetCurvesContent(Bool) -> some View`

Displays the widget’s content along a curve if the context allows it.

`func widgetLabel<S>(S) -> some View`

Returns a text label that displays additional content outside the accessory
family widget’s main SwiftUI view.

`func widgetLabel(LocalizedStringKey) -> some View`

Returns a localized text label that displays additional content outside the
accessory family widget’s main SwiftUI view.

`func widgetLabel<Label>(label: () -> Label) -> some View`

Creates a label for displaying additional content outside an accessory family
widget’s main SwiftUI view.

`func dynamicIsland(verticalPlacement:
DynamicIslandExpandedRegionVerticalPlacement) -> some View`

Specifies the vertical placement for a view of an expanded Live Activity that
appears in the Dynamic Island.

## See Also

### Configuring view elements

API Reference

Accessibility modifiers

Make your SwiftUI apps accessible to everyone, including people with
disabilities.

API Reference

Text and symbol modifiers

Manage the rendering, selection, and entry of text in your view.

API Reference

Auxiliary view modifiers

Add and configure supporting views, like toolbars and context menus.

API Reference

Chart view modifiers

Configure charts that you declare with Swift Charts.

Collection

API Collection

# Text and symbol modifiers

Manage the rendering, selection, and entry of text in your view.

## Overview

SwiftUI provides built-in views that display text to the user, like `Text` and
`Label`, or that collect text from the user, like `TextField` and
`TextEditor`. Use text and symbol modifiers to control how SwiftUI displays
and manages that text. For example, you can set a font, specify text layout
parameters, and indicate what kind of input to expect.

To learn more about the kinds of views that you use to display text and the
ways in which you can configure those views, see Text input and output.

## Topics

### Fonts

`func font(Font?) -> some View`

Sets the default font for text in this view.

### Dynamic type

`func dynamicTypeSize(DynamicTypeSize) -> some View`

Sets the Dynamic Type size within the view to the given value.

`func dynamicTypeSize<T>(T) -> some View`

Limits the Dynamic Type size within the view to the given range.

### Text style

`func bold(Bool) -> some View`

Applies a bold font weight to the text in this view.

`func fontDesign(Font.Design?) -> some View`

Sets the font design of the text in this view.

`func fontWeight(Font.Weight?) -> some View`

Sets the font weight of the text in this view.

`func fontWidth(Font.Width?) -> some View`

Sets the font width of the text in this view.

`func italic(Bool) -> some View`

Applies italics to the text in this view.

`func monospaced(Bool) -> some View`

Modifies the fonts of all child views to use the fixed-width variant of the
current font, if possible.

`func monospacedDigit() -> some View`

Modifies the fonts of all child views to use fixed-width digits, if possible,
while leaving other characters proportionally spaced.

`func strikethrough(Bool, pattern: Text.LineStyle.Pattern, color: Color?) ->
some View`

Applies a strikethrough to the text in this view.

`func textCase(Text.Case?) -> some View`

Sets a transform for the case of the text contained in this view when
displayed.

`func textScale(Text.Scale, isEnabled: Bool) -> some View`

Applies a text scale to text in the view.

`func underline(Bool, pattern: Text.LineStyle.Pattern, color: Color?) -> some
View`

Applies an underline to the text in this view.

### Text layout

`func allowsTightening(Bool) -> some View`

Sets whether text in this view can compress the space between characters when
necessary to fit text in a line.

`func baselineOffset(CGFloat) -> some View`

Sets the vertical offset for the text relative to its baseline in this view.

`func flipsForRightToLeftLayoutDirection(Bool) -> some View`

Sets whether this view mirrors its contents horizontally when the layout
direction is right-to-left.

`func kerning(CGFloat) -> some View`

Sets the spacing, or kerning, between characters for the text in this view.

`func minimumScaleFactor(CGFloat) -> some View`

Sets the minimum amount that text in this view scales down to fit in the
available space.

`func tracking(CGFloat) -> some View`

Sets the tracking for the text in this view.

`func truncationMode(Text.TruncationMode) -> some View`

Sets the truncation mode for lines of text that are too long to fit in the
available space.

`func typesettingLanguage(Locale.Language, isEnabled: Bool) -> some View`

Specifies the language for typesetting.

`func typesettingLanguage(TypesettingLanguage, isEnabled: Bool) -> some View`

Specifies the language for typesetting.

### Multiline text

`func lineLimit(Int?) -> some View`

Sets the maximum number of lines that text can occupy in this view.

`func lineLimit(PartialRangeFrom<Int>) -> some View`

Sets to a partial range the number of lines that text can occupy in this view.

`func lineLimit(PartialRangeThrough<Int>) -> some View`

Sets to a partial range the number of lines that text can occupy in this view.

`func lineLimit(ClosedRange<Int>) -> some View`

Sets to a closed range the number of lines that text can occupy in this view.

`func lineLimit(Int, reservesSpace: Bool) -> some View`

Sets a limit for the number of lines text can occupy in this view.

`func lineSpacing(CGFloat) -> some View`

Sets the amount of space between lines of text in this view.

`func multilineTextAlignment(TextAlignment) -> some View`

Sets the alignment of a text view that contains multiple lines of text.

### Text selection

`func textSelection<S>(S) -> some View`

Controls whether people can select text within this view.

### Text entry

`func autocorrectionDisabled(Bool) -> some View`

Sets whether to disable autocorrection for this view.

`func keyboardType(UIKeyboardType) -> some View`

Sets the keyboard type for this view.

`func scrollDismissesKeyboard(ScrollDismissesKeyboardMode) -> some View`

Configures the behavior in which scrollable content interacts with the
software keyboard.

`func textInputAutocapitalization(TextInputAutocapitalization?) -> some View`

Sets how often the shift key in the keyboard is automatically enabled.

`func textContentType(UITextContentType?) -> some View`

Sets the text content type for this view, which the system uses to offer
suggestions while the user enters text on an iOS or tvOS device.

`func textContentType(NSTextContentType?) -> some View`

Sets the text content type for this view, which the system uses to offer
suggestions while the user enters text on macOS.

`func textContentType(WKTextContentType?) -> some View`

Sets the text content type for this view, which the system uses to offer
suggestions while the user enters text on a watchOS device.

### Find and replace

`func findNavigator(isPresented: Binding<Bool>) -> some View`

Programmatically presents the find and replace interface for text editor
views.

`func findDisabled(Bool) -> some View`

Prevents find and replace operations in a text editor.

`func replaceDisabled(Bool) -> some View`

Prevents replace operations in a text editor.

### Symbol appearance

`func symbolRenderingMode(SymbolRenderingMode?) -> some View`

Sets the rendering mode for symbol images within this view.

`func symbolVariant(SymbolVariants) -> some View`

Makes symbols within the view show a particular variant.

## See Also

### Configuring view elements

API Reference

Accessibility modifiers

Make your SwiftUI apps accessible to everyone, including people with
disabilities.

API Reference

Appearance modifiers

Configure a view’s foreground and background styles, controls, and visibility.

API Reference

Auxiliary view modifiers

Add and configure supporting views, like toolbars and context menus.

API Reference

Chart view modifiers

Configure charts that you declare with Swift Charts.

Collection

API Collection

# Auxiliary view modifiers

Add and configure supporting views, like toolbars and context menus.

## Overview

Use these modifiers to manage supplemental views that present context-specific
controls and information. For example, you can add titles and buttons to
navigation bars, manage the status bar, create context menus, and add badges
many different kinds of views.

## Topics

### Navigation titles

Configure your apps navigation titles

Use a navigation title to display the current navigation state of an
interface.

`func navigationTitle(LocalizedStringKey) -> some View`

Configures the view’s title for purposes of navigation, using a localized
string.

`func navigationTitle(Text) -> some View`

Configures the view’s title for purposes of navigation.

`func navigationTitle<S>(S) -> some View`

Configures the view’s title for purposes of navigation, using a string.

`func navigationTitle<V>(() -> V) -> some View`

Configures the view’s title for purposes of navigation, using a custom view.

`func navigationTitle(Binding<String>) -> some View`

Configures the view’s title for purposes of navigation, using a string
binding.

`func navigationSubtitle<S>(S) -> some View`

Configures the view’s subtitle for purposes of navigation, using a string.

`func navigationSubtitle(Text) -> some View`

Configures the view’s subtitle for purposes of navigation.

`func navigationSubtitle(LocalizedStringKey) -> some View`

Configures the view’s subtitle for purposes of navigation, using a localized
string.

### Navigation title configuration

`func navigationDocument<D>(D) -> some View`

Configures the view’s document for purposes of navigation.

`func navigationDocument(URL) -> some View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I>(D, preview: SharePreview<I, Never>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I>(D, preview: SharePreview<Never, I>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D>(D, preview: SharePreview<Never, Never>) -> some
View`

Configures the view’s document for purposes of navigation.

`func navigationDocument<D, I1, I2>(D, preview: SharePreview<I1, I2>) -> some
View`

Configures the view’s document for purposes of navigation.

### Navigation bars

`func navigationBarBackButtonHidden(Bool) -> some View`

Hides the navigation bar back button for the view.

`func navigationBarTitleDisplayMode(NavigationBarItem.TitleDisplayMode) ->
some View`

Configures the title display mode for this view.

### Navigation stacks and columns

`func navigationDestination<D, C>(for: D.Type, destination: (D) -> C) -> some
View`

Associates a destination view with a presented data type for use within a
navigation stack.

`func navigationDestination<V>(isPresented: Binding<Bool>, destination: () ->
V) -> some View`

Associates a destination view with a binding that can be used to push the view
onto a `NavigationStack`.

`func navigationDestination<D, C>(item: Binding<Optional<D>>, destination: (D)
-> C) -> some View`

Associates a destination view with a bound value for use within a navigation
stack or navigation split view

`func navigationSplitViewColumnWidth(CGFloat) -> some View`

Sets a fixed, preferred width for the column containing this view.

`func navigationSplitViewColumnWidth(min: CGFloat?, ideal: CGFloat, max:
CGFloat?) -> some View`

Sets a flexible, preferred width for the column containing this view.

### Tab views

`func tabItem<V>(() -> V) -> some View`

Sets the tab bar item associated with this view.

### Toolbars

For information about toolbars, see Toolbars.

`func toolbar<Content>(content: () -> Content) -> some View`

Populates the toolbar or navigation bar with the specified items.

`func toolbar<Content>(content: () -> Content) -> some View`

Populates the toolbar or navigation bar with the views you provide.

`func toolbar<Content>(id: String, content: () -> Content) -> some View`

Populates the toolbar or navigation bar with the specified items, allowing for
user customization.

`func toolbar(Visibility, for: ToolbarPlacement...) -> some View`

Specifies the visibility of a bar managed by SwiftUI.

`func toolbar(removing: ToolbarDefaultItemKind?) -> some View`

Remove a toolbar item present by default

`func toolbarBackground<S>(S, for: ToolbarPlacement...) -> some View`

Specifies the preferred shape style of the background of a bar managed by
SwiftUI.

`func toolbarBackground(Visibility, for: ToolbarPlacement...) -> some View`

Specifies the preferred visibility of backgrounds on a bar managed by SwiftUI.

`func toolbarColorScheme(ColorScheme?, for: ToolbarPlacement...) -> some View`

Specifies the preferred color scheme of a bar managed by SwiftUI.

`func toolbarRole(ToolbarRole) -> some View`

Configures the semantic role for the content populating the toolbar.

`func toolbarTitleMenu<C>(content: () -> C) -> some View`

Configure the title menu of a toolbar.

`func toolbarTitleDisplayMode(ToolbarTitleDisplayMode) -> some View`

Configures the toolbar title display mode for this view.

`func ornament<Content>(visibility: Visibility, attachmentAnchor:
OrnamentAttachmentAnchor, contentAlignment: Alignment, ornament: () ->
Content) -> some View`

Presents an ornament.

### Context menus

For information about menus in your app, see Menus and commands.

`func contextMenu<MenuItems>(menuItems: () -> MenuItems) -> some View`

Adds a context menu to a view.

`func contextMenu<M, P>(menuItems: () -> M, preview: () -> P) -> some View`

Adds a context menu with a preview to a view.

`func contextMenu<I, M>(forSelectionType: I.Type, menu: (Set<I>) -> M,
primaryAction: ((Set<I>) -> Void)?) -> some View`

Adds an item-based context menu to a view.

### Badges

`func badge(Text?) -> some View`

Generates a badge for the view from a text view.

`func badge<S>(S?) -> some View`

Generates a badge for the view from a string.

`func badge(LocalizedStringKey?) -> some View`

Generates a badge for the view from a localized string key.

`func badge(Int) -> some View`

Generates a badge for the view from an integer value.

`func badgeProminence(BadgeProminence) -> some View`

Specifies the prominence of badges created by this view.

### Help text

`func help(LocalizedStringKey) -> some View`

Adds help text to a view using a localized string that you provide.

`func help<S>(S) -> some View`

Adds help text to a view using a string that you provide.

`func help(Text) -> some View`

Adds help text to a view using a text view that you provide.

### Status bar

`func statusBarHidden(Bool) -> some View`

Sets the visibility of the status bar.

### Touch Bar

`func touchBar<Content>(content: () -> Content) -> some View`

Sets the content that the Touch Bar displays.

`func touchBar<Content>(TouchBar<Content>) -> some View`

Sets the Touch Bar content to be shown in the Touch Bar when applicable.

`func touchBarItemPrincipal(Bool) -> some View`

Sets principal views that have special significance to this Touch Bar.

`func touchBarCustomizationLabel(Text) -> some View`

Sets a user-visible string that identifies the view’s functionality.

`func touchBarItemPresence(TouchBarItemPresence) -> some View`

Sets the behavior of the user-customized view.

## See Also

### Configuring view elements

API Reference

Accessibility modifiers

Make your SwiftUI apps accessible to everyone, including people with
disabilities.

API Reference

Appearance modifiers

Configure a view’s foreground and background styles, controls, and visibility.

API Reference

Text and symbol modifiers

Manage the rendering, selection, and entry of text in your view.

API Reference

Chart view modifiers

Configure charts that you declare with Swift Charts.

Collection

API Collection

# Chart view modifiers

Configure charts that you declare with Swift Charts.

## Overview

Use these modifiers to configure a `Chart` view that you add to your SwiftUI
app.

## Topics

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

`func chartPlotStyle<Content>(content: (ChartPlotContent) -> Content) -> some
View`

Configures the plot area of charts.

### Legends

`func chartLegend(Visibility) -> some View`

Configures the legend for charts.

`func chartLegend(position: AnnotationPosition, alignment: Alignment?,
spacing: CGFloat?) -> some View`

Configures the legend for charts.

`func chartLegend<Content>(position: AnnotationPosition, alignment:
Alignment?, spacing: CGFloat?, content: () -> Content) -> some View`

Configures the legend for charts.

### Overlays

`func chartOverlay<V>(alignment: Alignment, content: (ChartProxy) -> V) ->
some View`

Adds an overlay to a view that contains a chart.

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

`func chartYAxisStyle<Content>(content: (ChartAxisContent) -> Content) -> some
View`

Configures the y axis content of charts.

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

`func chartYAxisLabel<C>(position: AnnotationPosition, alignment: Alignment?,
spacing: CGFloat?, content: () -> C) -> some View`

Adds y axis label for charts in the view.

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

`func chartYScale(type: ScaleType?) -> some View`

Configures the y scale for charts.

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

`func chartSymbolScale<Range>(range: Range) -> some View`

Configures the symbol style scale for charts.

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

`func chartSymbolSizeScale(type: ScaleType?) -> some View`

Configures the symbol size scale for charts.

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

`func chartLineStyleScale<DataValue>(mapping: (DataValue) -> StrokeStyle) ->
some View`

Configures the line style scale for charts.

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

`func chartScrollableAxes(Axis.Set) -> some View`

Configures the scrollable behavior of charts in this view.

### Selection

`func chartXSelection<P>(range: Binding<ClosedRange<P>?>) -> some View`

`func chartXSelection<P>(value: Binding<P?>) -> some View`

`func chartYSelection<P>(range: Binding<ClosedRange<P>?>) -> some View`

`func chartYSelection<P>(value: Binding<P?>) -> some View`

`func chartAngleSelection<P>(value: Binding<P?>) -> some View`

### Visible domain

`func chartXVisibleDomain<P>(length: P) -> some View`

Sets the length of the visible domain in the X dimension.

`func chartYVisibleDomain<P>(length: P) -> some View`

Sets the length of the visible domain in the Y dimension.

### Interaction

`func chartGesture((ChartProxy) -> some Gesture) -> some View`

## See Also

### Configuring view elements

API Reference

Accessibility modifiers

Make your SwiftUI apps accessible to everyone, including people with
disabilities.

API Reference

Appearance modifiers

Configure a view’s foreground and background styles, controls, and visibility.

API Reference

Text and symbol modifiers

Manage the rendering, selection, and entry of text in your view.

API Reference

Auxiliary view modifiers

Add and configure supporting views, like toolbars and context menus.

Collection

API Collection

# Style modifiers

Apply built-in styles to different types of views.

## Overview

SwiftUI defines built-in styles for certain kinds of views, and chooses the
appropriate style for a particular presentation context. For example, a
`Label` might appear as an icon, a string title, or both, depending on factors
like the platform, whether the view appears in a toolbar, and so on.

You can override the automatic style by using one of the style modifiers.
These modifiers typically propagate through container views, so you can wrap
an entire view hierarchy in a style modifier to affect all the views of the
given type within the hierarchy. Some view types enable you to create custom
styles, which you also apply using style modifiers.

For more information about styling views, see View styles.

## Topics

### Controls

`func buttonStyle<S>(S) -> some View`

Sets the style for buttons within this view to a button style with a custom
appearance and custom interaction behavior.

`func buttonStyle<S>(S) -> some View`

Sets the style for buttons within this view to a button style with a custom
appearance and standard interaction behavior.

`func datePickerStyle<S>(S) -> some View`

Sets the style for date pickers within this view.

`func menuStyle<S>(S) -> some View`

Sets the style for menus within this view.

`func pickerStyle<S>(S) -> some View`

Sets the style for pickers within this view.

`func toggleStyle<S>(S) -> some View`

Sets the style for toggles in a view hierarchy.

### Indicators

`func gaugeStyle<S>(S) -> some View`

Sets the style for gauges within this view.

`func progressViewStyle<S>(S) -> some View`

Sets the style for progress views in this view.

### Text

`func labelStyle<S>(S) -> some View`

Sets the style for labels within this view.

`func textFieldStyle<S>(S) -> some View`

Sets the style for text fields within this view.

`func textEditorStyle(some TextEditorStyle) -> some View`

Sets the style for text editors within this view.

### Collections

`func listStyle<S>(S) -> some View`

Sets the style for lists within this view.

`func tableStyle<S>(S) -> some View`

Sets the style for tables within this view.

`func disclosureGroupStyle<S>(S) -> some View`

Sets the style for disclosure groups within this view.

### Presentation

`func navigationSplitViewStyle<S>(S) -> some View`

Sets the style for navigation split views within this view.

`func tabViewStyle<S>(S) -> some View`

Sets the style for the tab view within the current environment.

`func presentedWindowStyle<S>(S) -> some View`

Sets the style for windows created by interacting with this view.

`func presentedWindowToolbarStyle<S>(S) -> some View`

Sets the style for the toolbar in windows created by interacting with this
view.

### Groups

`func controlGroupStyle<S>(S) -> some View`

Sets the style for control groups within this view.

`func groupBoxStyle<S>(S) -> some View`

Sets the style for group boxes within this view.

`func indexViewStyle<S>(S) -> some View`

Sets the style for the index view within the current environment.

## See Also

### Drawing views

API Reference

Layout modifiers

Tell a view how to arrange itself within a view hierarchy by adjusting its
size, position, alignment, padding, and so on.

API Reference

Graphics and rendering modifiers

Affect the way the system draws a view, for example by scaling or masking a
view, or by applying graphical effects.

Collection

API Collection

# Layout modifiers

Tell a view how to arrange itself within a view hierarchy by adjusting its
size, position, alignment, padding, and so on.

## Overview

Use layout modifiers to fine tune the placement of views in a view hierarchy.
You can adjust or constrain the size, position, and alignment of a view. You
can also add padding around a view, and indicate how the view interacts with
system-defined safe areas.

To get started arranging views, see Layout fundamentals. To make adjustments
to a basic layout, see Layout adjustments.

## Topics

### Size

`func frame(width: CGFloat?, height: CGFloat?, alignment: Alignment) -> some
View`

Positions this view within an invisible frame with the specified size.

`func frame(depth: CGFloat?, alignment: DepthAlignment) -> some View`

Positions this view within an invisible frame with the specified depth.

`func frame(minWidth: CGFloat?, idealWidth: CGFloat?, maxWidth: CGFloat?,
minHeight: CGFloat?, idealHeight: CGFloat?, maxHeight: CGFloat?, alignment:
Alignment) -> some View`

Positions this view within an invisible frame having the specified size
constraints.

`func frame(minDepth: CGFloat?, idealDepth: CGFloat?, maxDepth: CGFloat?,
alignment: DepthAlignment) -> some View`

Positions this view within an invisible frame having the specified depth
constraints.

`func containerRelativeFrame(Axis.Set, alignment: Alignment) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func containerRelativeFrame(Axis.Set, alignment: Alignment, (CGFloat, Axis)
-> CGFloat) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func containerRelativeFrame(Axis.Set, count: Int, span: Int, spacing:
CGFloat, alignment: Alignment) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func fixedSize() -> some View`

Fixes this view at its ideal size.

`func fixedSize(horizontal: Bool, vertical: Bool) -> some View`

Fixes this view at its ideal size in the specified dimensions.

`func layoutPriority(Double) -> some View`

Sets the priority by which a parent layout should apportion space to this
child.

### Position

`func position(CGPoint) -> some View`

Positions the center of this view at the specified point in its parent’s
coordinate space.

`func position(x: CGFloat, y: CGFloat) -> some View`

Positions the center of this view at the specified coordinates in its parent’s
coordinate space.

`func offset(CGSize) -> some View`

Offset this view by the horizontal and vertical amount specified in the offset
parameter.

`func offset(x: CGFloat, y: CGFloat) -> some View`

Offset this view by the specified horizontal and vertical distances.

`func offset(z: CGFloat) -> some View`

Brings a view forward in Z by the provided distance in points.

`func coordinateSpace(NamedCoordinateSpace) -> some View`

Assigns a name to the view’s coordinate space, so other code can operate on
dimensions like points and sizes relative to the named space.

### Alignment

`func alignmentGuide(HorizontalAlignment, computeValue: (ViewDimensions) ->
CGFloat) -> some View`

Sets the view’s horizontal alignment.

`func alignmentGuide(VerticalAlignment, computeValue: (ViewDimensions) ->
CGFloat) -> some View`

Sets the view’s vertical alignment.

### Padding and spacing

`func padding(CGFloat) -> some View`

Adds a specific padding amount to each edge of this view.

`func padding(Edge.Set, CGFloat?) -> some View`

Adds an equal padding amount to specific edges of this view.

`func padding(EdgeInsets) -> some View`

Adds a different padding amount to each edge of this view.

`func padding3D(CGFloat) -> some View`

Pads this view along all edge insets by the amount you specify.

`func padding3D(EdgeInsets3D) -> some View`

Pads this view using the edge insets you specify.

`func padding3D(Edge3D.Set, CGFloat?) -> some View`

Pads this view using the edge insets you specify.

`func listRowInsets(EdgeInsets?) -> some View`

Applies an inset to the rows in a list.

`func scenePadding(Edge.Set) -> some View`

Adds padding to the specified edges of this view using an amount that’s
appropriate for the current scene.

`func scenePadding(ScenePadding, edges: Edge.Set) -> some View`

Adds a specified kind of padding to the specified edges of this view using an
amount that’s appropriate for the current scene.

`func listRowSpacing(CGFloat?) -> some View`

Sets the vertical spacing between two adjacent rows in a List.

`func listSectionSpacing(CGFloat) -> some View`

Sets the spacing to a custom value between adjacent sections in a List.

`func listSectionSpacing(ListSectionSpacing) -> some View`

Sets the spacing between adjacent sections in a List.

### Grid configuration

`func gridCellColumns(Int) -> some View`

Tells a view that acts as a cell in a grid to span the specified number of
columns.

`func gridCellAnchor(UnitPoint) -> some View`

Specifies a custom alignment anchor for a view that acts as a grid cell.

`func gridCellUnsizedAxes(Axis.Set) -> some View`

Asks grid layouts not to offer the view extra size in the specified axes.

`func gridColumnAlignment(HorizontalAlignment) -> some View`

Overrides the default horizontal alignment of the grid column that the view
appears in.

### Safe area and margins

`func ignoresSafeArea(SafeAreaRegions, edges: Edge.Set) -> some View`

Expands the safe area of a view.

`func safeAreaInset<V>(edge: HorizontalEdge, alignment: VerticalAlignment,
spacing: CGFloat?, content: () -> V) -> some View`

Shows the specified content beside the modified view.

`func safeAreaInset<V>(edge: VerticalEdge, alignment: HorizontalAlignment,
spacing: CGFloat?, content: () -> V) -> some View`

Shows the specified content above or below the modified view.

`func safeAreaPadding(EdgeInsets) -> some View`

Adds the provided insets into the safe area of this view.

`func safeAreaPadding(CGFloat) -> some View`

Adds the provided insets into the safe area of this view.

`func safeAreaPadding(Edge.Set, CGFloat?) -> some View`

Adds the provided insets into the safe area of this view.

`func contentMargins(CGFloat, for: ContentMarginPlacement) -> some View`

Configures the content margin for a provided placement.

`func contentMargins(Edge.Set, CGFloat?, for: ContentMarginPlacement) -> some
View`

Configures the content margin for a provided placement.

`func contentMargins(Edge.Set, EdgeInsets, for: ContentMarginPlacement) ->
some View`

Configures the content margin for a provided placement.

### Layer order

`func zIndex(Double) -> some View`

Controls the display order of overlapping views.

### Layout direction

`func layoutDirectionBehavior(LayoutDirectionBehavior) -> some View`

Sets the behavior of this view for different layout directions.

### Custom layout characteristics

`func layoutValue<K>(key: K.Type, value: K.Value) -> some View`

Associates a value with a custom layout property.

## See Also

### Drawing views

API Reference

Style modifiers

Apply built-in styles to different types of views.

API Reference

Graphics and rendering modifiers

Affect the way the system draws a view, for example by scaling or masking a
view, or by applying graphical effects.

Collection

API Collection

# Graphics and rendering modifiers

Affect the way the system draws a view, for example by scaling or masking a
view, or by applying graphical effects.

## Overview

Use these view modifiers to apply many of the rendering effects typically
associated with a graphics context, like adding masks and creating composites.
You can apply these effects to graphical views, like Shapes, as well as any
other SwiftUI view.

When you do need the flexibility of immediate mode drawing in a graphics
context, use a `Canvas` view instead. This can be particularly helpful when
you want to draw an extremely large number of dynamic shapes — for example, to
create particle effects.

For more information about using these effects in your app, see Drawing and
graphics.

## Topics

### Masks and clipping

`func mask<Mask>(alignment: Alignment, () -> Mask) -> some View`

Masks this view using the alpha channel of the given view.

`func clipped(antialiased: Bool) -> some View`

Clips this view to its bounding rectangular frame.

`func clipShape<S>(S, style: FillStyle) -> some View`

Sets a clipping shape for this view.

`func containerShape<T>(T) -> some View`

Sets the container shape to use for any container relative shape within this
view.

### Scale

`func scaledToFill() -> some View`

Scales this view to fill its parent.

`func scaledToFit() -> some View`

Scales this view to fit its parent.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(CGSize, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified factor.

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified size in each dimension.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> ModifiedContent<Self,
_UniformScaleEffect>`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
some View`

Scales this view by the specified horizontal, vertical, and depth factors.

`func imageScale(Image.Scale) -> some View`

Scales images within the view according to one of the relative sizes available
including small, medium, and large images sizes.

`func aspectRatio(CGFloat?, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the specified aspect ratio.

`func aspectRatio(CGSize, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the aspect ratio of the given size.

### Rotation and transformation

`func rotationEffect(Angle, anchor: UnitPoint) -> some View`

Rotates a view’s rendered output in two dimensions around the specified point.

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some View`

Rotates the view’s content by the specified 3D rotation value.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> some View`

Rotates the view’s content by an angle about an axis that you specify as a
tuple of elements.

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
some View`

Rotates the view’s content by an angle about an axis that you specify as a
rotation axis value.

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some
View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func projectionEffect(ProjectionTransform) -> some View`

Applies a projection transformation to this view’s rendered output.

`func transformEffect(CGAffineTransform) -> some View`

Applies an affine transformation to this view’s rendered output.

`func transform3DEffect(AffineTransform3D) -> some View`

Applies a 3D transformation to the receiver.

### Graphical effects

`func blur(radius: CGFloat, opaque: Bool) -> some View`

Applies a Gaussian blur to this view.

`func opacity(Double) -> some View`

Sets the transparency of this view.

`func brightness(Double) -> some View`

Brightens this view by the specified amount.

`func contrast(Double) -> some View`

Sets the contrast and separation between similar colors in this view.

`func colorInvert() -> some View`

Inverts the colors in this view.

`func colorMultiply(Color) -> some View`

Adds a color multiplication effect to this view.

`func saturation(Double) -> some View`

Adjusts the color saturation of this view.

`func grayscale(Double) -> some View`

Adds a grayscale effect to this view.

`func hueRotation(Angle) -> some View`

Applies a hue rotation effect to this view.

`func luminanceToAlpha() -> some View`

Adds a luminance to alpha effect to this view.

`func shadow(color: Color, radius: CGFloat, x: CGFloat, y: CGFloat) -> some
View`

Adds a shadow to this view.

`func visualEffect((EmptyVisualEffect, GeometryProxy) -> some VisualEffect) ->
some View`

Applies effects to this view, while providing access to layout information
through a geometry proxy.

`func visualEffect3D((EmptyVisualEffect, GeometryProxy3D) -> some
VisualEffect) -> some View`

Applies effects to this view, while providing access to layout information
through a 3D geometry proxy.

### Shaders

`func colorEffect(Shader, isEnabled: Bool) -> some View`

Returns a new view that applies `shader` to `self` as a filter effect on the
color of each pixel.

`func distortionEffect(Shader, maxSampleOffset: CGSize, isEnabled: Bool) ->
some View`

Returns a new view that applies `shader` to `self` as a geometric distortion
effect on the location of each pixel.

`func layerEffect(Shader, maxSampleOffset: CGSize, isEnabled: Bool) -> some
View`

Returns a new view that applies `shader` to `self` as a filter on the raster
layer created from `self`.

### Composites

`func blendMode(BlendMode) -> some View`

Sets the blend mode for compositing this view with overlapping views.

`func compositingGroup() -> some View`

Wraps this view in a compositing group.

`func drawingGroup(opaque: Bool, colorMode: ColorRenderingMode) -> some View`

Composites this view’s contents into an offscreen image before final display.

### Animations

`func animation(Animation?) -> some View`

Applies the given animation to this view when this view changes.

Available when `Self` conforms to `Equatable`.

`func animation<V>(Animation?, value: V) -> some View`

Applies the given animation to this view when the specified value changes.

`func animation<V>(Animation?, body: (PlaceholderContentView<Self>) -> V) ->
some View`

Applies the given animation to all animatable values within the `body`
closure.

`func keyframeAnimator<Value>(initialValue: Value, repeating: Bool, content:
(PlaceholderContentView<Self>, Value) -> some View, keyframes: (Value) -> some
Keyframes) -> some View`

Loops the given keyframes continuously, updating the view using the modifiers
you apply in `body`.

`func keyframeAnimator<Value>(initialValue: Value, trigger: some Equatable,
content: (PlaceholderContentView<Self>, Value) -> some View, keyframes:
(Value) -> some Keyframes) -> some View`

Plays the given keyframes when the given trigger value changes, updating the
view using the modifiers you apply in `body`.

`func phaseAnimator<Phase>(some Sequence, content:
(PlaceholderContentView<Self>, Phase) -> some View, animation: (Phase) ->
Animation?) -> some View`

Animates effects that you apply to a view over a sequence of phases that
change continuously.

`func phaseAnimator<Phase>(some Sequence, trigger: some Equatable, content:
(PlaceholderContentView<Self>, Phase) -> some View, animation: (Phase) ->
Animation?) -> some View`

Animates effects that you apply to a view over a sequence of phases that
change based on a trigger.

`func contentTransition(ContentTransition) -> some View`

Modifies the view to use a given transition as its method of animating changes
to the contents of its views.

`func transition<T>(T) -> some View`

Associates a transition with the view.

`func transition(AnyTransition) -> some View`

Associates a transition with the view.

`func transaction((inout Transaction) -> Void) -> some View`

Applies the given transaction mutation function to all animations used within
the view.

`func transaction(value: some Equatable, (inout Transaction) -> Void) -> some
View`

Applies the given transaction mutation function to all animations used within
the view.

`func transaction<V>((inout Transaction) -> Void, body:
(PlaceholderContentView<Self>) -> V) -> some View`

Applies the given transaction mutation function to all animations used within
the `body` closure.

`func contentTransition(ContentTransition) -> some View`

Modifies the view to use a given transition as its method of animating changes
to the contents of its views.

`func matchedGeometryEffect<ID>(id: ID, in: Namespace.ID, properties:
MatchedGeometryProperties, anchor: UnitPoint, isSource: Bool) -> some View`

Defines a group of views with synchronized geometry using an identifier and
namespace that you provide.

`func geometryGroup() -> some View`

Isolates the geometry (e.g. position and size) of the view from its parent
view.

## See Also

### Drawing views

API Reference

Style modifiers

Apply built-in styles to different types of views.

API Reference

Layout modifiers

Tell a view how to arrange itself within a view hierarchy by adjusting its
size, position, alignment, padding, and so on.

Collection

API Collection

# Input and event modifiers

Supply actions for a view to perform in response to user input and system
events.

## Overview

Use input and event modifiers to configure and provide handlers for a wide
variety of user inputs or system events. For example, you can detect and
control focus, respond to life cycle events like view appearance and
disappearance, manage keyboard shortcuts, and much more.

## Topics

### Interactivity

`func disabled(Bool) -> some View`

Adds a condition that controls whether users can interact with this view.

`func interactionActivityTrackingTag(String) -> some View`

Sets a tag that you use for tracking interactivity.

### List controls

`func swipeActions<T>(edge: HorizontalEdge, allowsFullSwipe: Bool, content: ()
-> T) -> some View`

Adds custom swipe actions to a row in a list.

`func refreshable(action: () async -> Void) -> some View`

Marks this view as refreshable.

`func selectionDisabled(Bool) -> some View`

Adds a condition that controls whether users can select this view.

### Scroll controls

`func scrollPosition(id: Binding<(some Hashable)?>, anchor: UnitPoint?) ->
some View`

Associates a binding to be updated when a scroll view within this view
scrolls.

`func defaultScrollAnchor(UnitPoint?) -> some View`

Associates an anchor to control which part of the scroll view’s content should
be rendered by default.

`func scrollTargetBehavior(some ScrollTargetBehavior) -> some View`

Sets the scroll behavior of views scrollable in the provided axes.

`func scrollTargetLayout(isEnabled: Bool) -> some View`

Configures the outermost layout as a scroll target layout.

`func scrollTransition(ScrollTransitionConfiguration, axis: Axis?, transition:
(EmptyVisualEffect, ScrollTransitionPhase) -> some VisualEffect) -> some View`

Applies the given transition, animating between the phases of the transition
as this view appears and disappears within the visible region of the
containing scroll view, or other container specified using the
`coordinateSpace` parameter.

`func scrollTransition(topLeading: ScrollTransitionConfiguration,
bottomTrailing: ScrollTransitionConfiguration, axis: Axis?, transition:
(EmptyVisualEffect, ScrollTransitionPhase) -> some VisualEffect) -> some View`

Applies the given transition, animating between the phases of the transition
as this view appears and disappears within the visible region of the
containing scroll view, or other container specified using the
`coordinateSpace` parameter.

### Taps and gestures

For more information, see Gestures.

`func onTapGesture(count: Int, perform: () -> Void) -> some View`

Adds an action to perform when this view recognizes a tap gesture.

`func onTapGesture(count: Int, coordinateSpace: some CoordinateSpaceProtocol,
perform: (CGPoint) -> Void) -> some View`

Adds an action to perform when this view recognizes a tap gesture, and
provides the action with the location of the interaction.

`func onLongPressGesture(minimumDuration: Double, maximumDistance: CGFloat,
perform: () -> Void, onPressingChanged: ((Bool) -> Void)?) -> some View`

Adds an action to perform when this view recognizes a long press gesture.

`func onLongPressGesture(minimumDuration: Double, perform: () -> Void,
onPressingChanged: ((Bool) -> Void)?) -> some View`

Adds an action to perform when this view recognizes a long press gesture.

`func onLongTouchGesture(minimumDuration: Double, perform: () -> Void,
onTouchingChanged: ((Bool) -> Void)?) -> some View`

Adds an action to perform when this view recognizes a remote long touch
gesture. A long touch gesture is when the finger is on the remote touch
surface without actually pressing.

`func gesture<T>(T, including: GestureMask) -> some View`

Attaches a gesture to the view with a lower precedence than gestures defined
by the view.

`func highPriorityGesture<T>(T, including: GestureMask) -> some View`

Attaches a gesture to the view with a higher precedence than gestures defined
by the view.

`func simultaneousGesture<T>(T, including: GestureMask) -> some View`

Attaches a gesture to the view to process simultaneously with gestures defined
by the view.

`func defersSystemGestures(on: Edge.Set) -> some View`

Sets the screen edge from which you want your gesture to take precedence over
the system gesture.

### Keyboard input

`func onKeyPress(KeyEquivalent, action: () -> KeyPress.Result) -> some View`

Performs an action if the user presses a key on a hardware keyboard while the
view has focus.

`func onKeyPress(phases: KeyPress.Phases, action: (KeyPress) ->
KeyPress.Result) -> some View`

Performs an action if the user presses any key on a hardware keyboard while
the view has focus.

`func onKeyPress(KeyEquivalent, phases: KeyPress.Phases, action: (KeyPress) ->
KeyPress.Result) -> some View`

Performs an action if the user presses a key on a hardware keyboard while the
view has focus.

`func onKeyPress(characters: CharacterSet, phases: KeyPress.Phases, action:
(KeyPress) -> KeyPress.Result) -> some View`

Performs an action if the user presses one or more keys on a hardware keyboard
while the view has focus.

`func onKeyPress(keys: Set<KeyEquivalent>, phases: KeyPress.Phases, action:
(KeyPress) -> KeyPress.Result) -> some View`

Performs an action if the user presses one or more keys on a hardware keyboard
while the view has focus.

### Keyboard shortcuts

`func keyboardShortcut(KeyboardShortcut) -> some View`

Assigns a keyboard shortcut to the modified control.

`func keyboardShortcut(KeyboardShortcut?) -> some View`

Assigns an optional keyboard shortcut to the modified control.

`func keyboardShortcut(KeyEquivalent, modifiers: EventModifiers) -> some View`

Defines a keyboard shortcut and assigns it to the modified control.

`func keyboardShortcut(KeyEquivalent, modifiers: EventModifiers, localization:
KeyboardShortcut.Localization) -> some View`

Defines a keyboard shortcut and assigns it to the modified control.

### Hover

`func onHover(perform: (Bool) -> Void) -> some View`

Adds an action to perform when the user moves the pointer over or away from
the view’s frame.

`func onContinuousHover(coordinateSpace: some CoordinateSpaceProtocol,
perform: (HoverPhase) -> Void) -> some View`

Adds an action to perform when the pointer enters, moves within, and exits the
view’s bounds.

`func hoverEffect(HoverEffect) -> some View`

Applies a hover effect to this view.

`func hoverEffect(HoverEffect, isEnabled: Bool) -> some View`

Applies a hover effect to this view.

`func hoverEffectDisabled(Bool) -> some View`

Adds a condition that controls whether this view can display hover effects.

`func defaultHoverEffect(HoverEffect?) -> some View`

Sets the default hover effect to use for views within this view.

`func listRowHoverEffect(HoverEffect?) -> some View`

Requests that the containing list row use the provided hover effect.

`func listRowHoverEffectDisabled(Bool) -> some View`

Requests that the containing list row have its hover effect disabled.

### Focus

For more information, see Focus.

`func focused<Value>(FocusState<Value>.Binding, equals: Value) -> some View`

Modifies this view by binding its focus state to the given state value.

`func focused(FocusState<Bool>.Binding) -> some View`

Modifies this view by binding its focus state to the given Boolean state
value.

`func focusedValue<T>(T?) -> some View`

Sets the focused value for the given object type.

`func focusedValue<Value>(WritableKeyPath<FocusedValues, Value?>, Value) ->
some View`

Modifies this view by injecting a value that you provide for use by other
views whose state depends on the focused view hierarchy.

`func focusedValue<Value>(WritableKeyPath<FocusedValues, Value?>, Value?) ->
some View`

Creates a new view that exposes the provided value to other views whose state
depends on the focused view hierarchy.

`func focusedSceneValue<T>(WritableKeyPath<FocusedValues, T?>, T?) -> some
View`

Creates a new view that exposes the provided value to other views whose state
depends on the active scene.

`func focusedSceneValue<T>(WritableKeyPath<FocusedValues, T?>, T) -> some
View`

Modifies this view by injecting a value that you provide for use by other
views whose state depends on the focused scene.

`func focusedObject<T>(T?) -> some View`

Creates a new view that exposes the provided object to other views whose state
depends on the focused view hierarchy.

`func focusedObject<T>(T) -> some View`

Creates a new view that exposes the provided object to other views whose whose
state depends on the focused view hierarchy.

`func focusedSceneObject<T>(T?) -> some View`

Creates a new view that exposes the provided object to other views whose whose
state depends on the active scene.

`func focusedSceneObject<T>(T) -> some View`

Creates a new view that exposes the provided object to other views whose whose
state depends on the active scene.

`func prefersDefaultFocus(Bool, in: Namespace.ID) -> some View`

Indicates that the view should receive focus by default for a given namespace.

`func focusScope(Namespace.ID) -> some View`

Creates a focus scope that SwiftUI uses to limit default focus preferences.

`func focusSection() -> some View`

Indicates that the view’s frame and cohort of focusable descendants should be
used to guide focus movement.

`func focusable(Bool) -> some View`

Specifies if the view is focusable.

`func focusable(Bool, interactions: FocusInteractions) -> some View`

Specifies if the view is focusable, and if so, what focus-driven interactions
it supports.

`func focusEffectDisabled(Bool) -> some View`

Adds a condition that controls whether this view can display focus effects,
such as a default focus ring or hover effect.

`func defaultFocus<V>(FocusState<V>.Binding, V, priority:
DefaultFocusEvaluationPriority) -> some View`

Defines a region of the window in which default focus is evaluated by
assigning a value to a given focus state binding.

### Copy and paste

For more information, see Clipboard.

`func copyable<T>(() -> [T]) -> some View`

Specifies a list of items to copy in response to the system’s Copy command.

`func cuttable<T>(for: T.Type, action: () -> [T]) -> some View`

Specifies an action that moves items to the Clipboard in response to the
system’s Cut command.

`func pasteDestination<T>(for: T.Type, action: ([T]) -> Void, validator: ([T])
-> [T]) -> some View`

Specifies an action that adds validated items to a view in response to the
system’s Paste command.

`func onCopyCommand(perform: (() -> [NSItemProvider])?) -> some View`

Adds an action to perform in response to the system’s Copy command.

`func onCutCommand(perform: (() -> [NSItemProvider])?) -> some View`

Adds an action to perform in response to the system’s Cut command.

`func onPasteCommand(of: [UTType], perform: ([NSItemProvider]) -> Void) ->
some View`

Adds an action to perform in response to the system’s Paste command.

`func onPasteCommand<Payload>(of: [UTType], validator: ([NSItemProvider]) ->
Payload?, perform: (Payload) -> Void) -> some View`

Adds an action to perform in response to the system’s Paste command with items
that you validate.

### Drag and drop

For more information, see Drag and drop.

`func onDrag<V>(() -> NSItemProvider, preview: () -> V) -> some View`

Activates this view as the source of a drag and drop operation.

`func onDrag(() -> NSItemProvider) -> some View`

Activates this view as the source of a drag and drop operation.

`func itemProvider(Optional<() -> NSItemProvider?>) -> some View`

Provides a closure that vends the drag representation to be used for a
particular data element.

`func onDrop(of: [UTType], isTargeted: Binding<Bool>?, perform:
([NSItemProvider]) -> Bool) -> some View`

Defines the destination of a drag-and-drop operation that handles the dropped
content with a closure that you specify.

`func onDrop(of: [UTType], isTargeted: Binding<Bool>?, perform:
([NSItemProvider], CGPoint) -> Bool) -> some View`

Defines the destination of a drag and drop operation that handles the dropped
content with a closure that you specify.

`func onDrop(of: [UTType], delegate: any DropDelegate) -> some View`

Defines the destination of a drag and drop operation using behavior controlled
by the delegate that you provide.

`func dropDestination<T>(for: T.Type, action: ([T], CGPoint) -> Bool,
isTargeted: (Bool) -> Void) -> some View`

Defines the destination of a drag and drop operation that handles the dropped
content with a closure that you specify.

`func draggable<T>(() -> T) -> some View`

Activates this view as the source of a drag and drop operation.

`func draggable<V, T>(() -> T, preview: () -> V) -> some View`

Activates this view as the source of a drag and drop operation.

`func springLoadingBehavior(SpringLoadingBehavior) -> some View`

Sets the spring loading behavior this view.

### Submission

`func onSubmit(of: SubmitTriggers, (() -> Void)) -> some View`

Adds an action to perform when the user submits a value to this view.

`func submitScope(Bool) -> some View`

Prevents submission triggers originating from this view to invoke a submission
action configured by a submission modifier higher up in the view hierarchy.

`func submitLabel(SubmitLabel) -> some View`

Sets the submit label for this view.

### Movement

`func onMoveCommand(perform: ((MoveCommandDirection) -> Void)?) -> some View`

Adds an action to perform in response to a move command, like when the user
presses an arrow key on a Mac keyboard, or taps the edge of the Siri Remote
when controlling an Apple TV.

`func moveDisabled(Bool) -> some View`

Adds a condition for whether the view’s view hierarchy is movable.

### Deletion

`func onDeleteCommand(perform: (() -> Void)?) -> some View`

Adds an action to perform in response to the system’s Delete command, or
pressing either the ⌫ (backspace) or ⌦ (forward delete) keys while the view
has focus.

`func deleteDisabled(Bool) -> some View`

Adds a condition for whether the view’s view hierarchy is deletable.

### Commands

`func pageCommand<V>(value: Binding<V>, in: ClosedRange<V>, step: V) -> some
View`

Steps a value through a range in response to page up or page down commands.

`func onExitCommand(perform: (() -> Void)?) -> some View`

Sets up an action that triggers in response to receiving the exit command
while the view has focus.

`func onPlayPauseCommand(perform: (() -> Void)?) -> some View`

Adds an action to perform in response to the system’s Play/Pause command.

`func onCommand(Selector, perform: (() -> Void)?) -> some View`

Adds an action to perform in response to the given selector.

### Digital crown

`func digitalCrownAccessory(Visibility) -> some View`

Specifies the visibility of Digital Crown accessory Views on Apple Watch.

`func digitalCrownAccessory<Content>(content: () -> Content) -> some View`

Places an accessory View next to the Digital Crown on Apple Watch.

`func digitalCrownRotation<V>(Binding<V>, from: V, through: V, sensitivity:
DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>, onChange: (DigitalCrownEvent) ->
Void, onIdle: () -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(detent: Binding<V>, from: V, through: V, by:
V.Stride, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(detent: Binding<V>, from: V, through: V, by:
V.Stride, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>, from: V, through: V, by: V.Stride?,
sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

### User activities

`func userActivity<P>(String, element: P?, (P, NSUserActivity) -> ()) -> some
View`

Advertises a user activity type.

`func userActivity(String, isActive: Bool, (NSUserActivity) -> ()) -> some
View`

Advertises a user activity type.

`func onContinueUserActivity(String, perform: (NSUserActivity) -> ()) -> some
View`

Registers a handler to invoke in response to a user activity that your app
receives.

`func handlesExternalEvents(preferring: Set<String>, allowing: Set<String>) ->
some View`

Specifies the external events that the view’s scene handles if the scene is
already open.

### View life cycle

`func onAppear(perform: (() -> Void)?) -> some View`

Adds an action to perform before this view appears.

`func onDisappear(perform: (() -> Void)?) -> some View`

Adds an action to perform after this view disappears.

`func onChange<V>(of: V, initial: Bool, () -> Void) -> some View`

Adds a modifier for this view that fires an action when a specific value
changes.

`func onChange<V>(of: V, initial: Bool, (V, V) -> Void) -> some View`

Adds a modifier for this view that fires an action when a specific value
changes.

`func task(priority: TaskPriority, () async -> Void) -> some View`

Adds an asynchronous task to perform before this view appears.

`func task<T>(id: T, priority: TaskPriority, () async -> Void) -> some View`

Adds a task to perform before this view appears or when a specified value
changes.

### File renaming

`func renameAction(() -> Void) -> some View`

Sets a closure to run for the rename action.

`func renameAction(FocusState<Bool>.Binding) -> some View`

Sets the rename action in the environment to update focus state.

### URLs

`func onOpenURL(perform: (URL) -> ()) -> some View`

Registers a handler to invoke in response to a URL that your app receives.

`func widgetURL(URL?) -> some View`

Sets the URL to open in the containing app when the user clicks the widget.

### Publisher events

`func onReceive<P>(P, perform: (P.Output) -> Void) -> some View`

Adds an action to perform when this view detects data emitted by the given
publisher.

### Hit testing

`func allowsHitTesting(Bool) -> some View`

Configures whether this view participates in hit test operations.

### Content shape

`func contentShape<S>(S, eoFill: Bool) -> some View`

Defines the content shape for hit testing.

`func contentShape<S>(ContentShapeKinds, S, eoFill: Bool) -> some View`

Sets the content shape for this view.

### Import and export

`func exportsItemProviders([UTType], onExport: () -> [NSItemProvider]) -> some
View`

Exports a read-only item provider for consumption by shortcuts, quick actions,
and services.

`func exportsItemProviders([UTType], onExport: () -> [NSItemProvider], onEdit:
([NSItemProvider]) -> Bool) -> some View`

Exports a read-write item provider for consumption by shortcuts, quick
actions, and services.

`func importsItemProviders([UTType], onImport: ([NSItemProvider]) -> Bool) ->
some View`

Enables importing item providers from services, such as Continuity Camera on
macOS.

`func exportableToServices<T>(() -> [T]) -> some View`

Exports items for consumption by shortcuts, quick actions, and services.

`func exportableToServices<T>(() -> [T], onEdit: ([T]) -> Bool) -> some View`

Exports read-write items for consumption by shortcuts, quick actions, and
services.

`func importableFromServices<T>(for: T.Type, action: ([T]) -> Bool) -> some
View`

Enables importing items from services, such as Continuity Camera on macOS.

### App intents

`func shortcutsLinkStyle(ShortcutsLinkStyle) -> some View`

Sets the given style for ShortcutsLinks within the view hierarchy

`func siriTipViewStyle(SiriTipViewStyle) -> some View`

Sets the given style for SiriTipView within the view hierarchy

## See Also

### Providing interactivity

API Reference

Search modifiers

Enable people to search for content in your app.

API Reference

Presentation modifiers

Define additional views for the view to present under specified conditions.

API Reference

State modifiers

Access storage and provide child views with configuration data.

Collection

API Collection

# Search modifiers

Enable people to search for content in your app.

## Overview

Use search view modifiers to add search capability to your app. For more
information, see Search.

## Topics

### Displaying a search interface

`func searchable(text: Binding<String>, placement: SearchFieldPlacement,
prompt: Text?) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable(text: Binding<String>, placement: SearchFieldPlacement,
prompt: LocalizedStringKey) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<S>(text: Binding<String>, placement: SearchFieldPlacement,
prompt: S) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable(text: Binding<String>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: LocalizedStringKey) -> some View`

Marks this view as searchable with programmatic presentation of the search
field.

`func searchable(text: Binding<String>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: Text?) -> some View`

Marks this view as searchable with programmatic presentation of the search
field.

`func searchable<S>(text: Binding<String>, isPresented: Binding<Bool>,
placement: SearchFieldPlacement, prompt: S) -> some View`

Marks this view as searchable with programmatic presentation of the search
field.

`func searchPresentationToolbarBehavior(SearchPresentationToolbarBehavior) ->
some View`

Configures the search toolbar presentation behavior for any searchable
modifiers within this view.

### Searching with tokens

`func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>,
placement: SearchFieldPlacement, prompt: S, token: (C.Element) -> T) -> some
View`

Marks this view as searchable with text and tokens.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, placement:
SearchFieldPlacement, prompt: LocalizedStringKey, token: (C.Element) -> T) ->
some View`

Marks this view as searchable with text and tokens.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, placement:
SearchFieldPlacement, prompt: Text?, token: (C.Element) -> T) -> some View`

Marks this view as searchable with text and tokens.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, isPresented:
Binding<Bool>, placement: SearchFieldPlacement, prompt: LocalizedStringKey,
token: (C.Element) -> T) -> some View`

Marks this view as searchable with text and tokens, as well as programmatic
presentation.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, isPresented:
Binding<Bool>, placement: SearchFieldPlacement, prompt: Text?, token:
(C.Element) -> T) -> some View`

Marks this view as searchable with text and tokens, as well as programmatic
presentation.

`func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: S, token:
(C.Element) -> T) -> some View`

Marks this view as searchable with text and tokens, as well as programmatic
presentation.

### Searching with editable tokens

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: some
StringProtocol, token: (Binding<C.Element>) -> some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: Text?,
token: (Binding<C.Element>) -> some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt:
LocalizedStringKey, token: (Binding<C.Element>) -> some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
placement: SearchFieldPlacement, prompt: Text?, token: (Binding<C.Element>) ->
some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
placement: SearchFieldPlacement, prompt: LocalizedStringKey, token:
(Binding<C.Element>) -> some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
placement: SearchFieldPlacement, prompt: some StringProtocol, token:
(Binding<C.Element>) -> some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

### Making search suggestions

`func searchSuggestions<S>(() -> S) -> some View`

Configures the search suggestions for this view.

`func searchSuggestions(Visibility, for: SearchSuggestionsPlacement.Set) ->
some View`

Configures how to display search suggestions within this view.

`func searchCompletion<T>(T) -> some View`

Associates a search token with the value of this view.

`func searchCompletion(String) -> some View`

Associates a fully formed string with the value of this view.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, placement: SearchFieldPlacement, prompt:
LocalizedStringKey, token: (C.Element) -> T) -> some View`

Marks this view as searchable with text, tokens, and suggestions.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, placement: SearchFieldPlacement, prompt: Text?,
token: (C.Element) -> T) -> some View`

Marks this view as searchable with text, tokens, and suggestions.

`func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, placement: SearchFieldPlacement, prompt: S,
token: (C.Element) -> T) -> some View`

Marks this view as searchable with text, tokens, and suggestions.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: LocalizedStringKey, token: (C.Element) -> T) ->
some View`

Marks this view as searchable with text, tokens, and suggestions, as well as
programmatic presentation.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: Text?, token: (C.Element) -> T) -> some View`

Marks this view as searchable with text, tokens, and suggestions, as well as
programmatic presentation.

`func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: S, token: (C.Element) -> T) -> some View`

Marks this view as searchable with text, tokens, and suggestions, as well as
programmatic presentation.

### Limiting search scope

`func searchScopes<V, S>(Binding<V>, scopes: () -> S) -> some View`

Configures the search scopes for this view.

`func searchScopes<V, S>(Binding<V>, activation: SearchScopeActivation, () ->
S) -> some View`

Configures the search scopes for this view with the specified activation
strategy.

### Searching through dictation

`func searchDictationBehavior(TextInputDictationBehavior) -> some View`

## See Also

### Providing interactivity

API Reference

Input and event modifiers

Supply actions for a view to perform in response to user input and system
events.

API Reference

Presentation modifiers

Define additional views for the view to present under specified conditions.

API Reference

State modifiers

Access storage and provide child views with configuration data.

Collection

API Collection

# Presentation modifiers

Define additional views for the view to present under specified conditions.

## Overview

Use presentation modifiers to show different kinds of modal presentations,
like alerts, popovers, sheets, and confirmation dialogs.

Because SwiftUI is a declarative framework, you don’t call a method at the
moment you want to present the modal. Rather, you define how the presentation
looks and the condition under which SwiftUI should present it. SwiftUI detects
when the condition changes and makes the presentation for you. Because you
provide a `Binding` to the condition that initiates the presentation, SwiftUI
can reset the underlying value when the user dismisses the presentation.

For more information about how to use these modifiers, see Modal
presentations.

## Topics

### Alerts

`func alert<S, A>(S, isPresented: Binding<Bool>, actions: () -> A) -> some
View`

Presents an alert when a given condition is true, using a string variable as a
title.

`func alert<A>(Text, isPresented: Binding<Bool>, actions: () -> A) -> some
View`

Presents an alert when a given condition is true, using a text view for the
title.

`func alert<A>(LocalizedStringKey, isPresented: Binding<Bool>, actions: () ->
A) -> some View`

Presents an alert when a given condition is true, using a localized string key
for the title.

`func alert<A, T>(Text, isPresented: Binding<Bool>, presenting: T?, actions:
(T) -> A) -> some View`

Presents an alert using the given data to produce the alert’s content and a
text view as a title.

`func alert<A, T>(LocalizedStringKey, isPresented: Binding<Bool>, presenting:
T?, actions: (T) -> A) -> some View`

Presents an alert using the given data to produce the alert’s content and a
localized string key for a title.

`func alert<S, A, T>(S, isPresented: Binding<Bool>, presenting: T?, actions:
(T) -> A) -> some View`

Presents an alert using the given data to produce the alert’s content and a
string variable as a title.

`func alert<E, A>(isPresented: Binding<Bool>, error: E?, actions: () -> A) ->
some View`

Presents an alert when an error is present.

### Alerts with a message

`func alert<S, A, M>(S, isPresented: Binding<Bool>, actions: () -> A, message:
() -> M) -> some View`

Presents an alert with a message when a given condition is true using a string
variable as a title.

`func alert<A, M>(LocalizedStringKey, isPresented: Binding<Bool>, actions: ()
-> A, message: () -> M) -> some View`

Presents an alert with a message when a given condition is true, using a
localized string key for a title.

`func alert<A, M>(Text, isPresented: Binding<Bool>, actions: () -> A, message:
() -> M) -> some View`

Presents an alert with a message when a given condition is true using a text
view as a title.

`func alert<A, M, T>(LocalizedStringKey, isPresented: Binding<Bool>,
presenting: T?, actions: (T) -> A, message: (T) -> M) -> some View`

Presents an alert with a message using the given data to produce the alert’s
content and a localized string key for a title.

`func alert<A, M, T>(Text, isPresented: Binding<Bool>, presenting: T?,
actions: (T) -> A, message: (T) -> M) -> some View`

Presents an alert with a message using the given data to produce the alert’s
content and a text view for a title.

`func alert<S, A, M, T>(S, isPresented: Binding<Bool>, presenting: T?,
actions: (T) -> A, message: (T) -> M) -> some View`

Presents an alert with a message using the given data to produce the alert’s
content and a string variable as a title.

`func alert<E, A, M>(isPresented: Binding<Bool>, error: E?, actions: (E) -> A,
message: (E) -> M) -> some View`

Presents an alert with a message when an error is present.

### Confirmation dialogs

`func confirmationDialog<S, A>(S, isPresented: Binding<Bool>, titleVisibility:
Visibility, actions: () -> A) -> some View`

Presents a confirmation dialog when a given condition is true, using a string
variable as a title.

`func confirmationDialog<A>(Text, isPresented: Binding<Bool>, titleVisibility:
Visibility, actions: () -> A) -> some View`

Presents a confirmation dialog when a given condition is true, using a text
view for the title.

`func confirmationDialog<A>(LocalizedStringKey, isPresented: Binding<Bool>,
titleVisibility: Visibility, actions: () -> A) -> some View`

Presents a confirmation dialog when a given condition is true, using a
localized string key for the title.

`func confirmationDialog<A, T>(Text, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A) -> some View`

Presents a confirmation dialog using data to produce the dialog’s content and
a text view for the title.

`func confirmationDialog<A, T>(LocalizedStringKey, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A) -> some View`

Presents a confirmation dialog using data to produce the dialog’s content and
a localized string key for the title.

`func confirmationDialog<S, A, T>(S, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A) -> some View`

Presents a confirmation dialog using data to produce the dialog’s content and
a string variable for the title.

### Confirmation dialogs with a message

`func confirmationDialog<S, A, M>(S, isPresented: Binding<Bool>,
titleVisibility: Visibility, actions: () -> A, message: () -> M) -> some View`

Presents a confirmation dialog with a message when a given condition is true,
using a string variable for the title.

`func confirmationDialog<A, M>(LocalizedStringKey, isPresented: Binding<Bool>,
titleVisibility: Visibility, actions: () -> A, message: () -> M) -> some View`

Presents a confirmation dialog with a message when a given condition is true,
using a localized string key for the title.

`func confirmationDialog<A, M>(Text, isPresented: Binding<Bool>,
titleVisibility: Visibility, actions: () -> A, message: () -> M) -> some View`

Presents a confirmation dialog with a message when a given condition is true,
using a text view for the title.

`func confirmationDialog<A, M, T>(Text, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A, message: (T)
-> M) -> some View`

Presents a confirmation dialog with a message using data to produce the
dialog’s content and a text view for the message.

`func confirmationDialog<S, A, M, T>(S, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A, message: (T)
-> M) -> some View`

Presents a confirmation dialog with a message using data to produce the
dialog’s content and a string variable for the title.

`func confirmationDialog<A, M, T>(LocalizedStringKey, isPresented:
Binding<Bool>, titleVisibility: Visibility, presenting: T?, actions: (T) -> A,
message: (T) -> M) -> some View`

Presents a confirmation dialog with a message using data to produce the
dialog’s content and a localized string key for the title.

### Dialog configuration

`func dialogIcon(Image?) -> some View`

Configures the icon used by dialogs within this view.

`func dialogSeverity(DialogSeverity) -> some View`

`func dialogSuppressionToggle(isSuppressed: Binding<Bool>) -> some View`

Enables user suppression of dialogs and alerts presented within `self`, with a
default suppression message on macOS. Unused on other platforms.

`func dialogSuppressionToggle<S>(S, isSuppressed: Binding<Bool>) -> some View`

Enables user suppression of dialogs and alerts presented within `self`, with a
custom suppression message on macOS. Unused on other platforms.

`func dialogSuppressionToggle(Text, isSuppressed: Binding<Bool>) -> some View`

Enables user suppression of dialogs and alerts presented within `self`, with a
custom suppression message on macOS. Unused on other platforms.

`func dialogSuppressionToggle(LocalizedStringKey, isSuppressed: Binding<Bool>)
-> some View`

Enables user suppression of dialogs and alerts presented within `self`, with a
custom suppression message on macOS. Unused on other platforms.

### Sheets

`func sheet<Content>(isPresented: Binding<Bool>, onDismiss: (() -> Void)?,
content: () -> Content) -> some View`

Presents a sheet when a binding to a Boolean value that you provide is true.

`func sheet<Item, Content>(item: Binding<Item?>, onDismiss: (() -> Void)?,
content: (Item) -> Content) -> some View`

Presents a sheet using the given item as a data source for the sheet’s
content.

`func fullScreenCover<Content>(isPresented: Binding<Bool>, onDismiss: (() ->
Void)?, content: () -> Content) -> some View`

Presents a modal view that covers as much of the screen as possible when
binding to a Boolean value you provide is true.

`func fullScreenCover<Item, Content>(item: Binding<Item?>, onDismiss: (() ->
Void)?, content: (Item) -> Content) -> some View`

Presents a modal view that covers as much of the screen as possible using the
binding you provide as a data source for the sheet’s content.

### Popovers

`func popover<Content>(isPresented: Binding<Bool>, attachmentAnchor:
PopoverAttachmentAnchor, arrowEdge: Edge, content: () -> Content) -> some
View`

Presents a popover when a given condition is true.

`func popover<Item, Content>(item: Binding<Item?>, attachmentAnchor:
PopoverAttachmentAnchor, arrowEdge: Edge, content: (Item) -> Content) -> some
View`

Presents a popover using the given item as a data source for the popover’s
content.

### Sheet and popover configuration

`func interactiveDismissDisabled(Bool) -> some View`

Conditionally prevents interactive dismissal of presentations like popovers,
sheets, and inspectors.

`func presentationDetents(Set<PresentationDetent>) -> some View`

Sets the available detents for the enclosing sheet.

`func presentationDetents(Set<PresentationDetent>, selection:
Binding<PresentationDetent>) -> some View`

Sets the available detents for the enclosing sheet, giving you programmatic
control of the currently selected detent.

`func presentationDragIndicator(Visibility) -> some View`

Sets the visibility of the drag indicator on top of a sheet.

`func presentationBackground<S>(S) -> some View`

Sets the presentation background of the enclosing sheet using a shape style.

`func presentationBackground<V>(alignment: Alignment, content: () -> V) ->
some View`

Sets the presentation background of the enclosing sheet to a custom view.

`func presentationBackgroundInteraction(PresentationBackgroundInteraction) ->
some View`

Controls whether people can interact with the view behind a presentation.

`func presentationCompactAdaptation(horizontal: PresentationAdaptation,
vertical: PresentationAdaptation) -> some View`

Specifies how to adapt a presentation to horizontally and vertically compact
size classes.

`func presentationCompactAdaptation(PresentationAdaptation) -> some View`

Specifies how to adapt a presentation to compact size classes.

`func presentationContentInteraction(PresentationContentInteraction) -> some
View`

Configures the behavior of swipe gestures on a presentation.

`func presentationCornerRadius(CGFloat?) -> some View`

Requests that the presentation have a specific corner radius.

### File exporter

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType:
UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void) -> some View`

Presents a system interface for exporting a document that’s stored in a value
type, like a structure, to a file on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType:
UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void) -> some View`

Presents a system interface for exporting a document that’s stored in a
reference type, like a class, to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType:
UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for exporting a collection of reference type
documents to files on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType:
UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for exporting a collection of value type documents
to files on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system interface for allowing the user to export a `FileDocument`
to a file on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system dialog for allowing the user to export a
`ReferenceFileDocument` to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system dialog for allowing the user to export a collection of
documents that conform to `ReferenceFileDocument` to files on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system dialog for allowing the user to export a collection of
documents that conform to `FileDocument` to files on disk.

`func fileExporter<T>(isPresented: Binding<Bool>, item: T?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system interface allowing the user to export a `Transferable` item
to file on disk.

`func fileExporter<C, T>(isPresented: Binding<Bool>, items: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system interface allowing the user to export a collection of items
to files on disk.

`func fileExporterFilenameLabel(LocalizedStringKey) -> some View`

On macOS, configures the `fileExporter` with a label for the file name field.

`func fileExporterFilenameLabel(Text?) -> some View`

On macOS, configures the `fileExporter` with a text to use as a label for the
file name field.

`func fileExporterFilenameLabel<S>(S) -> some View`

On macOS, configures the `fileExporter` with a label for the file name field.

### File importer

`func fileImporter(isPresented: Binding<Bool>, allowedContentTypes: [UTType],
allowsMultipleSelection: Bool, onCompletion: (Result<[URL], any Error>) ->
Void) -> some View`

Presents a system interface for allowing the user to import multiple files.

`func fileImporter(isPresented: Binding<Bool>, allowedContentTypes: [UTType],
onCompletion: (Result<URL, any Error>) -> Void) -> some View`

Presents a system interface for allowing the user to import an existing file.

`func fileImporter(isPresented: Binding<Bool>, allowedContentTypes: [UTType],
allowsMultipleSelection: Bool, onCompletion: (Result<[URL], any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system dialog for allowing the user to import multiple files.

### File mover

`func fileMover(isPresented: Binding<Bool>, file: URL?, onCompletion:
(Result<URL, any Error>) -> Void) -> some View`

Presents a system interface for allowing the user to move an existing file to
a new location.

`func fileMover<C>(isPresented: Binding<Bool>, files: C, onCompletion:
(Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for allowing the user to move a collection of
existing files to a new location.

`func fileMover(isPresented: Binding<Bool>, file: URL?, onCompletion:
(Result<URL, any Error>) -> Void, onCancellation: () -> Void) -> some View`

Presents a system dialog for allowing the user to move an existing file to a
new location.

`func fileMover<C>(isPresented: Binding<Bool>, files: C, onCompletion:
(Result<[URL], any Error>) -> Void, onCancellation: () -> Void) -> some View`

Presents a system dialog for allowing the user to move a collection of
existing files to a new location.

### File dialog configuration

`func fileDialogBrowserOptions(FileDialogBrowserOptions) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to
provide a refined URL search experience: include or exclude hidden files,
allow searching by tag, etc.

`func fileDialogConfirmationLabel<S>(S) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom confirmation button label.

`func fileDialogConfirmationLabel(Text?) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with custom text as a confirmation button label.

`func fileDialogConfirmationLabel(LocalizedStringKey) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom confirmation button label.

`func fileDialogCustomizationID(String) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to
persist and restore the file dialog configuration.

`func fileDialogDefaultDirectory(URL?) -> some View`

Configures the `fileExporter`, `fileImporter`, or `fileMover` to open with the
specified default directory.

`func fileDialogImportsUnresolvedAliases(Bool) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover`
behavior when a user chooses an alias.

`func fileDialogMessage<S>(S) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom message that is presented to the user, similar to a title.

`func fileDialogMessage(Text?) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom text that is presented to the user, similar to a title.

`func fileDialogMessage(LocalizedStringKey) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom message that is presented to the user, similar to a title.

`func fileDialogURLEnabled(Predicate<URL>) -> some View`

On macOS, configures the the `fileImporter` or `fileMover` to conditionally
disable presented URLs.

### Inspectors

`func inspector<V>(isPresented: Binding<Bool>, content: () -> V) -> some View`

Inserts an inspector at the applied position in the view hierarchy.

`func inspectorColumnWidth(CGFloat) -> some View`

Sets a fixed, preferred width for the inspector containing this view when
presented as a trailing column.

`func inspectorColumnWidth(min: CGFloat?, ideal: CGFloat, max: CGFloat?) ->
some View`

Sets a flexible, preferred width for the inspector in a trailing-column
presentation.

### Quick look previews

`func quickLookPreview(Binding<URL?>) -> some View`

Presents a Quick Look preview of the contents of a single URL.

`func quickLookPreview<Items>(Binding<Items.Element?>, in: Items) -> some
View`

Presents a Quick Look preview of the URLs you provide.

### Family Sharing

`func familyActivityPicker(isPresented: Binding<Bool>, selection:
Binding<FamilyActivitySelection>) -> some View`

Presents an activity picker view as a sheet.

`func familyActivityPicker(headerText: String?, footerText: String?,
isPresented: Binding<Bool>, selection: Binding<FamilyActivitySelection>) ->
some View`

Presents an activity picker view as a sheet.

### Live Activities

`func activitySystemActionForegroundColor(Color?) -> some View`

The text color for the auxiliary action button that the system shows next to a
Live Activity on the Lock Screen.

`func activityBackgroundTint(Color?) -> some View`

Sets the tint color for the background of a Live Activity that appears on the
Lock Screen.

### Apple Music

`func musicSubscriptionOffer(isPresented: Binding<Bool>, options:
MusicSubscriptionOffer.Options, onLoadCompletion: ((any Error)?) -> Void) ->
some View`

Initiates the process of presenting a sheet with subscription offers for Apple
Music when the `isPresented` binding is `true`.

### StoreKit

`func appStoreOverlay(isPresented: Binding<Bool>, configuration: () ->
SKOverlay.Configuration) -> some View`

Presents a StoreKit overlay when a given condition is true.

`func manageSubscriptionsSheet(isPresented: Binding<Bool>) -> some View`

`func refundRequestSheet(for: Transaction.ID, isPresented: Binding<Bool>,
onDismiss: ((Result<Transaction.RefundRequestStatus,
Transaction.RefundRequestError>) -> ())?) -> some View`

Display the refund request sheet for the given transaction.

`func offerCodeRedemption(isPresented: Binding<Bool>, onCompletion:
(Result<Void, any Error>) -> Void) -> some View`

Presents a sheet that enables users to redeem subscription offer codes that
you configure in App Store Connect.

### PhotoKit

`func photosPicker(isPresented: Binding<Bool>, selection:
Binding<PhotosPickerItem?>, matching: PHPickerFilter?, preferredItemEncoding:
PhotosPickerItem.EncodingDisambiguationPolicy) -> some View`

Presents a Photos picker that selects a `PhotosPickerItem`.

`func photosPicker(isPresented: Binding<Bool>, selection:
Binding<PhotosPickerItem?>, matching: PHPickerFilter?, preferredItemEncoding:
PhotosPickerItem.EncodingDisambiguationPolicy, photoLibrary: PHPhotoLibrary)
-> some View`

Presents a Photos picker that selects a `PhotosPickerItem` from a given photo
library.

`func photosPicker(isPresented: Binding<Bool>, selection:
Binding<[PhotosPickerItem]>, maxSelectionCount: Int?, selectionBehavior:
PhotosPickerSelectionBehavior, matching: PHPickerFilter?,
preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy) -> some
View`

Presents a Photos picker that selects a collection of `PhotosPickerItem`.

`func photosPicker(isPresented: Binding<Bool>, selection:
Binding<[PhotosPickerItem]>, maxSelectionCount: Int?, selectionBehavior:
PhotosPickerSelectionBehavior, matching: PHPickerFilter?,
preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy,
photoLibrary: PHPhotoLibrary) -> some View`

Presents a Photos picker that selects a collection of `PhotosPickerItem` from
a given photo library.

`func photosPickerAccessoryVisibility(Visibility, edges: Edge.Set) -> some
View`

Sets the accessory visibility of the Photos picker. Accessories include
anything between the content and the edge, like the navigation bar or the
sidebar.

`func photosPickerDisabledCapabilities(PHPickerCapabilities) -> some View`

Disables capabilities of the Photos picker.

`func photosPickerStyle(PhotosPickerStyle) -> some View`

Sets the mode of the Photos picker.

## See Also

### Providing interactivity

API Reference

Input and event modifiers

Supply actions for a view to perform in response to user input and system
events.

API Reference

Search modifiers

Enable people to search for content in your app.

API Reference

State modifiers

Access storage and provide child views with configuration data.

Collection

API Collection

# State modifiers

Access storage and provide child views with configuration data.

## Overview

SwiftUI provides tools for managing data in your app. For example, you can
store values and objects in an environment that’s shared among the views in a
view hierarchy. Any view that shares the environment — typically all the
descendant views of the view that stores the item — can then access the stored
item.

For more information about the types that SwiftUI provides to help manage data
in your app, see Model data.

## Topics

### Identity

`func tag<V>(V) -> some View`

Sets the unique tag value of this view.

`func id<ID>(ID) -> some View`

Binds a view’s identity to the given proxy value.

`func equatable() -> EquatableView<Self>`

Prevents the view from updating its child view when its new value is the same
as its old value.

Available when `Self` conforms to `Equatable`.

### Environment values

`func environment<T>(T?) -> some View`

Places an observable object in the view’s environment.

`func environment<V>(WritableKeyPath<EnvironmentValues, V>, V) -> some View`

Sets the environment value of the specified key path to the given value.

`func environmentObject<T>(T) -> some View`

Supplies an observable object to a view’s hierarchy.

`func transformEnvironment<V>(WritableKeyPath<EnvironmentValues, V>,
transform: (inout V) -> Void) -> some View`

Transforms the environment value of the specified key path with the given
function.

### Preferences

`func preference<K>(key: K.Type, value: K.Value) -> some View`

Sets a value for the given preference.

`func transformPreference<K>(K.Type, (inout K.Value) -> Void) -> some View`

Applies a transformation to a preference value.

`func anchorPreference<A, K>(key: K.Type, value: Anchor<A>.Source, transform:
(Anchor<A>) -> K.Value) -> some View`

Sets a value for the specified preference key, the value is a function of a
geometry value tied to the current coordinate space, allowing readers of the
value to convert the geometry to their local coordinates.

`func transformAnchorPreference<A, K>(key: K.Type, value: Anchor<A>.Source,
transform: (inout K.Value, Anchor<A>) -> Void) -> some View`

Sets a value for the specified preference key, the value is a function of the
key’s current value and a geometry value tied to the current coordinate space,
allowing readers of the value to convert the geometry to their local
coordinates.

`func onPreferenceChange<K>(K.Type, perform: (K.Value) -> Void) -> some View`

Adds an action to perform when the specified preference key’s value changes.

`func backgroundPreferenceValue<Key, T>(Key.Type, (Key.Value) -> T) -> some
View`

Reads the specified preference value from the view, using it to produce a
second view that is applied as the background of the original view.

`func backgroundPreferenceValue<K, V>(K.Type, alignment: Alignment, (K.Value)
-> V) -> some View`

Reads the specified preference value from the view, using it to produce a
second view that is applied as the background of the original view.

`func overlayPreferenceValue<Key, T>(Key.Type, (Key.Value) -> T) -> some View`

Reads the specified preference value from the view, using it to produce a
second view that is applied as an overlay to the original view.

`func overlayPreferenceValue<K, V>(K.Type, alignment: Alignment, (K.Value) ->
V) -> some View`

Reads the specified preference value from the view, using it to produce a
second view that is applied as an overlay to the original view.

### Default storage

`func defaultAppStorage(UserDefaults) -> some View`

The default store used by `AppStorage` contained within the view.

### Configuring a model

`func modelContext(ModelContext) -> some View`

Sets the model context in this view’s environment.

`func modelContainer(ModelContainer) -> some View`

Sets the model container and associated model context in this view’s
environment.

`func modelContainer(for: any PersistentModel.Type, inMemory: Bool,
isAutosaveEnabled: Bool, isUndoEnabled: Bool, onSetup: (Result<ModelContainer,
any Error>) -> Void) -> some View`

Sets the model container in this view for storing the provided model type,
creating a new container if necessary, and also sets a model context for that
container in this view’s environment.

`func modelContainer(for: [any PersistentModel.Type], inMemory: Bool,
isAutosaveEnabled: Bool, isUndoEnabled: Bool, onSetup: (Result<ModelContainer,
any Error>) -> Void) -> some View`

Sets the model container in this view for storing the provided model types,
creating a new container if necessary, and also sets a model context for that
container in this view’s environment.

## See Also

### Providing interactivity

API Reference

Input and event modifiers

Supply actions for a view to perform in response to user input and system
events.

API Reference

Search modifiers

Enable people to search for content in your app.

API Reference

Presentation modifiers

Define additional views for the view to present under specified conditions.

Collection

API Collection

# Deprecated modifiers

Review unsupported modifiers and their replacements.

## Overview

Avoid using deprecated modifiers in your app. Select a modifier to see the
replacement that you should use instead.

## Topics

### Accessibility modifiers

`func accessibility(label: Text) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Adds a label to the view that describes its contents.

Deprecated

`func accessibility(value: Text) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Adds a textual description of the value that the view contains.

Deprecated

`func accessibility(hidden: Bool) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Specifies whether to hide this view from system accessibility features.

Deprecated

`func accessibility(identifier: String) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Uses the specified string to identify the view.

Deprecated

`func accessibility(selectionIdentifier: AnyHashable) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Sets a selection identifier for this view’s accessibility element.

Deprecated

`func accessibility(hint: Text) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Communicates to the user what happens after performing the view’s action.

Deprecated

`func accessibility(activationPoint: UnitPoint) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Specifies the unit point where activations occur in the view.

Deprecated

`func accessibility(activationPoint: CGPoint) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Specifies the point where activations occur in the view.

Deprecated

`func accessibility(inputLabels: [Text]) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Sets alternate input labels with which users identify a view.

Deprecated

`func accessibility(addTraits: AccessibilityTraits) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Adds the given traits to the view.

Deprecated

`func accessibility(removeTraits: AccessibilityTraits) ->
ModifiedContent<Self, AccessibilityAttachmentModifier>`

Removes the given traits from this view.

Deprecated

`func accessibility(sortPriority: Double) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Sets the sort priority order for this view’s accessibility element, relative
to other elements at the same level.

Deprecated

### Appearance modifiers

`func colorScheme(ColorScheme) -> some View`

Sets this view’s color scheme.

Deprecated

`func listRowPlatterColor(Color?) -> some View`

Sets the color that the system applies to the row background when this view is
placed in a list.

Deprecated

`func background<Background>(Background, alignment: Alignment) -> some View`

Layers the given view behind this view.

Deprecated

`func overlay<Overlay>(Overlay, alignment: Alignment) -> some View`

Layers a secondary view in front of this view.

Deprecated

`func foregroundColor(Color?) -> some View`

Sets the color of the foreground elements displayed by this view.

Deprecated

### Text modifiers

`func autocapitalization(UITextAutocapitalizationType) -> some View`

Sets whether to apply auto-capitalization to this view.

Deprecated

`func disableAutocorrection(Bool?) -> some View`

Sets whether to disable autocorrection for this view.

Deprecated

### Auxiliary view modifiers

`func navigationBarTitle(Text) -> some View`

Sets the title in the navigation bar for this view.

Deprecated

`func navigationBarTitle(Text, displayMode:
NavigationBarItem.TitleDisplayMode) -> some View`

Sets the title and display mode in the navigation bar for this view.

Deprecated

`func navigationBarTitle(LocalizedStringKey) -> some View`

Sets the title of this view’s navigation bar with a localized string.

Deprecated

`func navigationBarTitle<S>(S) -> some View`

Sets the title of this view’s navigation bar with a string.

Deprecated

`func navigationBarTitle(LocalizedStringKey, displayMode:
NavigationBarItem.TitleDisplayMode) -> some View`

Sets the title and display mode in the navigation bar for this view.

Deprecated

`func navigationBarTitle<S>(S, displayMode:
NavigationBarItem.TitleDisplayMode) -> some View`

Sets the title and display mode in the navigation bar for this view.

Deprecated

`func navigationBarItems<L>(leading: L) -> some View`

Sets the navigation bar items for this view.

Deprecated

`func navigationBarItems<L, T>(leading: L, trailing: T) -> some View`

Sets the navigation bar items for this view.

Deprecated

`func navigationBarItems<T>(trailing: T) -> some View`

Configures the navigation bar items for this view.

Deprecated

`func navigationBarHidden(Bool) -> some View`

Hides the navigation bar for this view.

Deprecated

`func statusBar(hidden: Bool) -> some View`

Sets the visibility of the status bar.

Deprecated

`func contextMenu<MenuItems>(ContextMenu<MenuItems>?) -> some View`

Adds a context menu to the view.

Deprecated

### Style modifiers

`func menuButtonStyle<S>(S) -> some View`

Sets the style for menu buttons within this view.

Deprecated

`func navigationViewStyle<S>(S) -> some View`

Sets the style for navigation views within this view.

Deprecated

### Layout modifiers

`func frame() -> some View`

Positions this view within an invisible frame.

Deprecated

`func edgesIgnoringSafeArea(Edge.Set) -> some View`

Changes the view’s proposed area to extend outside the screen’s safe areas.

Deprecated

`func coordinateSpace<T>(name: T) -> some View`

Assigns a name to the view’s coordinate space, so other code can operate on
dimensions like points and sizes relative to the named space.

Deprecated

### Graphics and rendering modifiers

`func accentColor(Color?) -> some View`

Sets the accent color for this view and the views it contains.

Deprecated

`func mask<Mask>(Mask) -> some View`

Masks this view using the alpha channel of the given view.

Deprecated

`func animation(Animation?) -> some View`

Applies the given animation to all animatable values within this view.

Deprecated

`func cornerRadius(CGFloat, antialiased: Bool) -> some View`

Clips this view to its bounding frame, with the specified corner radius.

Deprecated

### Input and events modifiers

`func onChange<V>(of: V, perform: (V) -> Void) -> some View`

Adds an action to perform when the given value changes.

Deprecated

`func onTapGesture(count: Int, coordinateSpace: CoordinateSpace, perform:
(CGPoint) -> Void) -> some View`

Adds an action to perform when this view recognizes a tap gesture, and
provides the action with the location of the interaction.

Deprecated

`func onLongPressGesture(minimumDuration: Double, maximumDistance: CGFloat,
pressing: ((Bool) -> Void)?, perform: () -> Void) -> some View`

Adds an action to perform when this view recognizes a long press gesture.

Deprecated

`func onLongPressGesture(minimumDuration: Double, pressing: ((Bool) -> Void)?,
perform: () -> Void) -> some View`

Adds an action to perform when this view recognizes a long press gesture.

Deprecated

`func onPasteCommand(of: [String], perform: ([NSItemProvider]) -> Void) ->
some View`

Adds an action to perform in response to the system’s Paste command.

Deprecated

`func onPasteCommand<Payload>(of: [String], validator: ([NSItemProvider]) ->
Payload?, perform: (Payload) -> Void) -> some View`

Adds an action to perform in response to the system’s Paste command with items
that you validate.

Deprecated

`func onDrop(of: [String], delegate: any DropDelegate) -> some View`

Defines the destination for a drag and drop operation with the same size and
position as this view, with behavior controlled by the given delegate.

Deprecated

`func onDrop(of: [String], isTargeted: Binding<Bool>?, perform:
([NSItemProvider]) -> Bool) -> some View`

Defines the destination for a drag and drop operation, using the same size and
position as this view, handling dropped content with the given closure.

Deprecated

`func onDrop(of: [String], isTargeted: Binding<Bool>?, perform:
([NSItemProvider], CGPoint) -> Bool) -> some View`

Defines the destination for a drag and drop operation with the same size and
position as this view, handling dropped content and the drop location with the
given closure.

Deprecated

`func focusable(Bool, onFocusChange: (Bool) -> Void) -> some View`

Specifies if the view is focusable and, if so, adds an action to perform when
the view comes into focus.

Deprecated

`func onContinuousHover(coordinateSpace: CoordinateSpace, perform:
(HoverPhase) -> Void) -> some View`

Adds an action to perform when the pointer enters, moves within, and exits the
view’s bounds.

Deprecated

### View presentation modifiers

`func actionSheet(isPresented: Binding<Bool>, content: () -> ActionSheet) ->
some View`

Presents an action sheet when a given condition is true.

Deprecated

`func actionSheet<T>(item: Binding<T?>, content: (T) -> ActionSheet) -> some
View`

Presents an action sheet using the given item as a data source for the sheet’s
content.

Deprecated

`func alert(isPresented: Binding<Bool>, content: () -> Alert) -> some View`

Presents an alert to the user.

Deprecated

`func alert<Item>(item: Binding<Item?>, content: (Item) -> Alert) -> some
View`

Presents an alert to the user.

Deprecated

### Search modifiers

`func searchable<S>(text: Binding<String>, placement: SearchFieldPlacement,
prompt: Text?, suggestions: () -> S) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<S>(text: Binding<String>, placement: SearchFieldPlacement,
prompt: LocalizedStringKey, suggestions: () -> S) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<V, S>(text: Binding<String>, placement: SearchFieldPlacement,
prompt: S, suggestions: () -> V) -> some View`

Marks this view as searchable, which configures the display of a search field.

Instance Method

# addOrderToWalletButtonStyle(_:)

Sets the button’s style.

iOS 17.0+  iPadOS 17.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func addOrderToWalletButtonStyle(_ style: AddOrderToWalletButtonStyle) -> some View
    

## Discussion

(see `AddOrderToWalletButtonStyle`).

Instance Method

# addPassToWalletButtonStyle(_:)

Sets the style to be used by the button. (see `PKAddPassButtonStyle`).

PassKit  SwiftUI  iOS 16.0+  iPadOS 16.0+

    
    
    func addPassToWalletButtonStyle(_ style: AddPassToWalletButtonStyle) -> some View
    

Instance Method

# automatedDeviceEnrollmentAddition(isPresented:)

Presents a modal view that enables users to add devices to their organization.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    func automatedDeviceEnrollmentAddition(isPresented: Binding<Bool>) -> some View
    

##  Parameters

`isPresented`

    

A binding to a Boolean value that determines whether to present the view.

## Return Value

The modal view that the system presents to the user.

## Discussion

Use this view modifier to present UI in your app for device administrators to
add devices purchased outside of the official channel to their organization —
Apple School Manager, Apple Business Manager, or Apple Business Essentials.
The system requires sign in with a Managed Apple ID that includes device
enrollment privileges.

The following code example shows one way to present this view to your users:

Example Usage:

Instance Method

# complicationForeground()

Promotes this view to the foreground in a complication.

ClockKit  SwiftUI  watchOS 7.0–10.4  Deprecated

    
    
    func complicationForeground() -> some View
    

Deprecated

On watchOS 9.0 or later, use WidgetKit instead

## Return Value

A view that is in the complication foreground.

## Discussion

A view in the foreground will be tinted alongside other foreground views. The
color for both the foreground and background layers is determined by the watch
face.

Instance Method

# continuityDevicePicker(isPresented:onDidConnect:)

A `continuityDevicePicker` should be used to discover and connect nearby
continuity device through a button interface or other form of activation. On
tvOS, this presents a fullscreen continuity device picker experience when
selected. The modal view covers as much the screen of `self` as possible when
a given condition is true.

AVKit  SwiftUI  tvOS 17.0+

    
    
    func continuityDevicePicker(
        isPresented: Binding<Bool>,
        onDidConnect: ((AVContinuityDevice?) -> Void)? = nil
    ) -> some View
    

##  Parameters

`isPresented`

    

A `Binding` to whether the modal view is presented.

`onDidConnect`

    

A closure executed when the picker successfully, connects AVContinuityDevice
or nil if cancelled by a user.

Instance Method

#
lookAroundViewer(isPresented:initialScene:allowsNavigation:showsRoadLabels:pointsOfInterest:onDismiss:)

MapKit  SwiftUI  iOS 17.0+  iPadOS 17.0+

    
    
    func lookAroundViewer(
        isPresented: Binding<Bool>,
        initialScene: MKLookAroundScene?,
        allowsNavigation: Bool = true,
        showsRoadLabels: Bool = true,
        pointsOfInterest: PointOfInterestCategories = .all,
        onDismiss: (() -> Void)? = nil
    ) -> some View
    

Instance Method

#
lookAroundViewer(isPresented:scene:allowsNavigation:showsRoadLabels:pointsOfInterest:onDismiss:)

MapKit  SwiftUI  iOS 17.0+  iPadOS 17.0+

    
    
    func lookAroundViewer(
        isPresented: Binding<Bool>,
        scene: Binding<MKLookAroundScene?>,
        allowsNavigation: Bool = true,
        showsRoadLabels: Bool = true,
        pointsOfInterest: PointOfInterestCategories = .all,
        onDismiss: (() -> Void)? = nil
    ) -> some View
    

Instance Method

# mapCameraKeyframeAnimator(trigger:keyframes:)

Uses the given keyframes to animate the camera of a `Map` when the given
trigger value changes.

MapKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    func mapCameraKeyframeAnimator(
        trigger: some Equatable,
        @KeyframesBuilder<MapCamera> keyframes: @escaping (MapCamera) -> some Keyframes<MapCamera>
    ) -> some View
    

##  Parameters

`trigger`

    

A value to observe for changes.

`keyframes`

    

A keyframes builder closure that is called when starting a new keyframe
animation. The current map camera is provided as the only parameter.

## Discussion

When the trigger value changes, the map calls the `keyframes` closure to
generate the keyframes that will animate the camera. The animation will
continue for the duration of the keyframes that you specify.

If the user performs a gesture while the animation is in progress, the
animation will be immediately removed, allowing the interaction to take
control of the camera.

Instance Method

# mapControlVisibility(_:)

Configures all Map controls in the environment to have the specified
visibility

MapKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    func mapControlVisibility(_ visibility: Visibility) -> some View
    

##  Parameters

`visibility`

    

how modified map controls should show or hide

## Discussion

MapCompass, MapScaleView, and MapPitchToggle may automatically show and hide
based on the current state of the Map. That may not be appropriate for all use
cases, where always showing a control may be desirable.

Other controls don’t have an automatic visibility behavior, so they will
always be visible when automatic is specified. Controls may also be hidden via
this modifier when conditionalizing the view is not appropriate

Instance Method

# mapControls(_:)

Configures all `Map` views in the associated environment to have standard size
and position controls

MapKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    func mapControls(@ViewBuilder _ content: () -> some View) -> some View
    

##  Parameters

`content`

    

A view builder returning the controls you wish your `Map`

## Discussion

You provide the controls you want to appear atop your map. When using a
control in conjunction with `.mapControls` you don’t need to specify a scope.
Views that are not MapKit controls will be ignored.

Controls can be modified individually or all at once. Custom frames and
alignments set on controls are ignored.

On watchOS, space is at a premium. When using the mapControls modifier,
MapUserLocationButton and MapCompass are automatically combined if present.

Instance Method

# mapFeatureSelectionContent(content:)

Specifies a custom presentation for the currently selected feature.

MapKit  SwiftUI  iOS 17.0+  iPadOS 17.0+

    
    
    func mapFeatureSelectionContent(@MapContentBuilder content: @escaping (MapFeature) -> some MapContent) -> some View
    

##  Parameters

`content`

    

Generates the custom presentation for a given map feature.

## Discussion

The supported presentation options are `Annotation`, and `Marker`. Other types
of map content will be ignored and handled as though no content was returned.

If empty map content is returned, the system presentation will be used.

Instance Method

# mapFeatureSelectionDisabled(_:)

Specifies which map features should have selection disabled.

MapKit  SwiftUI  iOS 17.0+  iPadOS 17.0+

    
    
    func mapFeatureSelectionDisabled(_ selectionDisabled: @escaping (MapFeature) -> Bool) -> some View
    

##  Parameters

`selectionDisabled`

    

Determines if selection should be disabled for a given map feature.

## Discussion

The `selectionDisabled` parameter takes a closure which maps map features, to
booleans. If that closure returns true for a given map feature, that map
feature will be considered unselectable.

Instance Method

# mapScope(_:)

Creates a mapScope that SwiftUI uses to connect map controls to an associated
map.

MapKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    func mapScope(_ scope: Namespace.ID) -> some View
    

Instance Method

# mapStyle(_:)

Specifies the map style to be used.

MapKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    func mapStyle(_ value: MapStyle) -> some View
    

Instance Method

# onApplePayCouponCodeChange(perform:)

Called when a user has entered or updated a coupon code. This is required if
the user is being asked to provide a coupon code.

PassKit  SwiftUI  iOS 15.5+  iPadOS 15.5+  macOS 12.5+

    
    
    func onApplePayCouponCodeChange(perform action: @escaping (String) async -> PKPaymentRequestCouponCodeUpdate) -> some View
    

## Return Value

An update to the payment request with the coupon code.

Instance Method

# onApplePayPaymentMethodChange(perform:)

Called when a payment method has changed and asks for an update payment
request. If this modifier isn’t provided Wallet will assume the payment method
is valid.

PassKit  SwiftUI  iOS 15.5+  iPadOS 15.5+  macOS 12.5+  watchOS 8.5+

    
    
    func onApplePayPaymentMethodChange(perform action: @escaping (PKPaymentMethod) async -> PKPaymentRequestPaymentMethodUpdate) -> some View
    

## Return Value

An update to the payment request method.

Instance Method

# onApplePayShippingContactChange(perform:)

Called when a user selected a shipping address. This is required if the user
is being asked to provide a shipping contact.

PassKit  SwiftUI  iOS 15.5+  iPadOS 15.5+  macOS 12.5+  watchOS 8.5+

    
    
    func onApplePayShippingContactChange(perform action: @escaping (PKContact) async -> PKPaymentRequestShippingContactUpdate) -> some View
    

## Return Value

An update to the payment request shipping methods.

Instance Method

# onApplePayShippingMethodChange(perform:)

Called when a user selected a shipping method. This is required if the user is
being asked to provide a shipping method.

PassKit  SwiftUI  iOS 15.5+  iPadOS 15.5+  macOS 12.5+  watchOS 8.5+

    
    
    func onApplePayShippingMethodChange(perform action: @escaping (PKShippingMethod) async -> PKPaymentRequestShippingMethodUpdate) -> some View
    

## Return Value

An update to the payment request shipping method.

Instance Method

# onMapCameraChange(frequency:_:)

Performs an action when Map camera framing changes

MapKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    func onMapCameraChange(
        frequency: MapCameraUpdateFrequency = .onEnd,
        _ action: @escaping () -> Void
    ) -> some View
    

##  Parameters

`frequency`

    

How frequently the action should be performed during a camera interaction.

`action`

    

A closure to run when the camera framing changes.

Instance Method

# onMapCameraChange(frequency:_:)

Performs an action when Map camera framing changes

MapKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    func onMapCameraChange(
        frequency: MapCameraUpdateFrequency = .onEnd,
        _ action: @escaping (MapCameraUpdateContext) -> Void
    ) -> some View
    

##  Parameters

`frequency`

    

How frequently the action should be performed during a camera interaction.

`action`

    

A closure to run when the camera framing changes. The closure takes a
`MapCameraUpdateContext` parameter that indicates the camera and the framed
area.

Instance Method

# payLaterViewAction(_:)

Sets the action on the PayLaterView. See `PKPayLaterAction`.

PassKit  SwiftUI  iOS 17.0+  iPadOS 17.0+

    
    
    func payLaterViewAction(_ action: PayLaterViewAction) -> some View
    

Instance Method

# payLaterViewDisplayStyle(_:)

Sets the display style on the PayLaterView. See `PKPayLaterDisplayStyle`.

PassKit  SwiftUI  iOS 17.0+  iPadOS 17.0+

    
    
    func payLaterViewDisplayStyle(_ displayStyle: PayLaterViewDisplayStyle) -> some View
    

Instance Method

# payWithApplePayButtonStyle(_:)

Sets the style to be used by the button. (see `PayWithApplePayButtonStyle`).

PassKit  SwiftUI  iOS 16.0+  iPadOS 16.0+  macOS 13.0+  watchOS 9.0+

    
    
    func payWithApplePayButtonStyle(_ style: PayWithApplePayButtonStyle) -> some View
    

Instance Method

#
translationPresentation(isPresented:text:attachmentAnchor:arrowEdge:replacementAction:)

Translation  SwiftUI  iOS 17.4+  iPadOS 17.4+  macOS 14.4+

    
    
    func translationPresentation(
        isPresented: Binding<Bool>,
        text: String,
        attachmentAnchor: PopoverAttachmentAnchor = .rect(.bounds),
        arrowEdge: Edge = .top,
        replacementAction: ((String) -> Void)? = nil
    ) -> some View
    

Instance Method

# verifyIdentityWithWalletButtonStyle(_:)

Sets the style to be used by the button. (see `PKIdentityButtonStyle`).

PassKit  SwiftUI  iOS 16.0+  iPadOS 16.0+

    
    
    func verifyIdentityWithWalletButtonStyle(_ style: VerifyIdentityWithWalletButtonStyle) -> some View
    



# VerticalEdge.Set

Type Property

# all

A set containing the top and bottom vertical edges.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static let all: VerticalEdge.Set

## See Also

### Getting edge sets

`static let top: VerticalEdge.Set`

A set containing only the top vertical edge.

`static let bottom: VerticalEdge.Set`

A set containing only the bottom vertical edge.

Type Property

# top

A set containing only the top vertical edge.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static let top: VerticalEdge.Set

## See Also

### Getting edge sets

`static let all: VerticalEdge.Set`

A set containing the top and bottom vertical edges.

`static let bottom: VerticalEdge.Set`

A set containing only the bottom vertical edge.

Type Property

# bottom

A set containing only the bottom vertical edge.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static let bottom: VerticalEdge.Set

## See Also

### Getting edge sets

`static let all: VerticalEdge.Set`

A set containing the top and bottom vertical edges.

`static let top: VerticalEdge.Set`

A set containing only the top vertical edge.

Initializer

# init(_:)

Creates a set of edges containing only the specified vertical edge.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init(_ e: VerticalEdge)



# ViewAlignedScrollTargetBehavior

Initializer

# init(limitBehavior:)

Creates a view aligned scroll behavior.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init(limitBehavior: ViewAlignedScrollTargetBehavior.LimitBehavior = .automatic)

## See Also

### Creating the target behavior

`struct LimitBehavior`

A type that defines the amount of views that can be scrolled at a time.

Structure

# ViewAlignedScrollTargetBehavior.LimitBehavior

A type that defines the amount of views that can be scrolled at a time.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct LimitBehavior

## Topics

### Getting the limit behavior

`static var automatic: ViewAlignedScrollTargetBehavior.LimitBehavior`

The automatic limit behavior.

`static var always: ViewAlignedScrollTargetBehavior.LimitBehavior`

The always limit behavior.

`static var never: ViewAlignedScrollTargetBehavior.LimitBehavior`

The never limit behavior.

## See Also

### Creating the target behavior

`init(limitBehavior: ViewAlignedScrollTargetBehavior.LimitBehavior)`

Creates a view aligned scroll behavior.



# VSplitView

Initializer

# init(content:)

macOS 10.15+

    
    
    init(@ViewBuilder content: () -> Content)



# VerticalEdge

Case

# VerticalEdge.top

The top edge.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    case top

## See Also

### Getting the edges

`case bottom`

The bottom edge.

Case

# VerticalEdge.bottom

The bottom edge.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    case bottom

## See Also

### Getting the edges

`case top`

The top edge.

Structure

# VerticalEdge.Set

An efficient set of vertical edges.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    @frozen
    struct Set

## Topics

### Getting edge sets

`static let all: VerticalEdge.Set`

A set containing the top and bottom vertical edges.

`static let top: VerticalEdge.Set`

A set containing only the top vertical edge.

`static let bottom: VerticalEdge.Set`

A set containing only the bottom vertical edge.

### Creating an edge set

`init(VerticalEdge)`

Creates a set of edges containing only the specified vertical edge.

## Relationships

### Conforms To

  * `Equatable`
  * `ExpressibleByArrayLiteral`
  * `OptionSet`
  * `RawRepresentable`
  * `Sendable`
  * `SetAlgebra`



# VolumetricWindowStyle

Initializer

# init()

visionOS 1.0+

    
    
    init()



# VisualEffect

Instance Method

# brightness(_:)

Brightens the view by the specified amount.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func brightness(_ amount: Double) -> some VisualEffect
    

##  Parameters

`amount`

    

A value between 0 (no effect) and 1 (full white brightening) that represents
the intensity of the brightness effect.

## Return Value

An effect that brightens the view by the specified amount.

## See Also

### Adjusting Color

`func colorEffect(Shader, isEnabled: Bool) -> some VisualEffect`

Returns a new visual effect that applies `shader` to `self` as a filter effect
on the color of each pixel.

`func contrast(Double) -> some VisualEffect`

Sets the contrast and separation between similar colors in the view.

`func grayscale(Double) -> some VisualEffect`

Adds a grayscale effect to the view.

`func hueRotation(Angle) -> some VisualEffect`

Applies a hue rotation effect to the view.

`func saturation(Double) -> some VisualEffect`

Adjusts the color saturation of the view.

`func opacity(Double) -> some VisualEffect`

Sets the transparency of the view.

Instance Method

# colorEffect(_:isEnabled:)

Returns a new visual effect that applies `shader` to `self` as a filter effect
on the color of each pixel.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    func colorEffect(
        _ shader: Shader,
        isEnabled: Bool = true
    ) -> some VisualEffect
    

##  Parameters

`shader`

    

The shader to apply to `self` as a color filter.

`isEnabled`

    

Whether the effect is enabled or not.

## Return Value

A new view that renders `self` with the shader applied as a color filter.

## Discussion

For a shader function to act as a color filter it must have a function
signature matching:

where `position` is the user-space coordinates of the pixel applied to the
shader and `color` its source color, as a pre-multiplied color in the
destination color space. `args...` should be compatible with the uniform
arguments bound to `shader`. The function should return the modified color
value.

Important

Views backed by AppKit or UIKit views may not render into the filtered layer.
Instead, they log a warning and display a placeholder image to highlight the
error.

## See Also

### Adjusting Color

`func brightness(Double) -> some VisualEffect`

Brightens the view by the specified amount.

`func contrast(Double) -> some VisualEffect`

Sets the contrast and separation between similar colors in the view.

`func grayscale(Double) -> some VisualEffect`

Adds a grayscale effect to the view.

`func hueRotation(Angle) -> some VisualEffect`

Applies a hue rotation effect to the view.

`func saturation(Double) -> some VisualEffect`

Adjusts the color saturation of the view.

`func opacity(Double) -> some VisualEffect`

Sets the transparency of the view.

Instance Method

# contrast(_:)

Sets the contrast and separation between similar colors in the view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func contrast(_ amount: Double) -> some VisualEffect
    

##  Parameters

`amount`

    

The intensity of color contrast to apply. negative values invert colors in
addition to applying contrast.

## Return Value

An effect that applies color contrast to the view.

## Discussion

Apply contrast to a view to increase or decrease the separation between
similar colors in the view.

## See Also

### Adjusting Color

`func brightness(Double) -> some VisualEffect`

Brightens the view by the specified amount.

`func colorEffect(Shader, isEnabled: Bool) -> some VisualEffect`

Returns a new visual effect that applies `shader` to `self` as a filter effect
on the color of each pixel.

`func grayscale(Double) -> some VisualEffect`

Adds a grayscale effect to the view.

`func hueRotation(Angle) -> some VisualEffect`

Applies a hue rotation effect to the view.

`func saturation(Double) -> some VisualEffect`

Adjusts the color saturation of the view.

`func opacity(Double) -> some VisualEffect`

Sets the transparency of the view.

Instance Method

# grayscale(_:)

Adds a grayscale effect to the view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func grayscale(_ amount: Double) -> some VisualEffect
    

##  Parameters

`amount`

    

The intensity of grayscale to apply from 0.0 to less than 1.0. Values closer
to 0.0 are more colorful, and values closer to 1.0 are less colorful.

## Return Value

An effect that reduces the intensity of colors in the view.

## Discussion

A grayscale effect reduces the intensity of colors in the view.

## See Also

### Adjusting Color

`func brightness(Double) -> some VisualEffect`

Brightens the view by the specified amount.

`func colorEffect(Shader, isEnabled: Bool) -> some VisualEffect`

Returns a new visual effect that applies `shader` to `self` as a filter effect
on the color of each pixel.

`func contrast(Double) -> some VisualEffect`

Sets the contrast and separation between similar colors in the view.

`func hueRotation(Angle) -> some VisualEffect`

Applies a hue rotation effect to the view.

`func saturation(Double) -> some VisualEffect`

Adjusts the color saturation of the view.

`func opacity(Double) -> some VisualEffect`

Sets the transparency of the view.

Instance Method

# hueRotation(_:)

Applies a hue rotation effect to the view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func hueRotation(_ angle: Angle) -> some VisualEffect
    

##  Parameters

`angle`

    

The hue rotation angle to apply to the colors in the view.

## Return Value

An effect that shifts all of the colors in the view.

## Discussion

Use hue rotation effect to shift all of the colors in a view according to the
angle you specify.

## See Also

### Adjusting Color

`func brightness(Double) -> some VisualEffect`

Brightens the view by the specified amount.

`func colorEffect(Shader, isEnabled: Bool) -> some VisualEffect`

Returns a new visual effect that applies `shader` to `self` as a filter effect
on the color of each pixel.

`func contrast(Double) -> some VisualEffect`

Sets the contrast and separation between similar colors in the view.

`func grayscale(Double) -> some VisualEffect`

Adds a grayscale effect to the view.

`func saturation(Double) -> some VisualEffect`

Adjusts the color saturation of the view.

`func opacity(Double) -> some VisualEffect`

Sets the transparency of the view.

Instance Method

# saturation(_:)

Adjusts the color saturation of the view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func saturation(_ amount: Double) -> some VisualEffect
    

##  Parameters

`amount`

    

The amount of saturation to apply to the view.

## Return Value

An effect that adjusts the saturation of the view.

## Discussion

Use color saturation to increase or decrease the intensity of colors in a
view.

See Also

`contrast(_:)`

## See Also

### Adjusting Color

`func brightness(Double) -> some VisualEffect`

Brightens the view by the specified amount.

`func colorEffect(Shader, isEnabled: Bool) -> some VisualEffect`

Returns a new visual effect that applies `shader` to `self` as a filter effect
on the color of each pixel.

`func contrast(Double) -> some VisualEffect`

Sets the contrast and separation between similar colors in the view.

`func grayscale(Double) -> some VisualEffect`

Adds a grayscale effect to the view.

`func hueRotation(Angle) -> some VisualEffect`

Applies a hue rotation effect to the view.

`func opacity(Double) -> some VisualEffect`

Sets the transparency of the view.

Instance Method

# opacity(_:)

Sets the transparency of the view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func opacity(_ opacity: Double) -> some VisualEffect
    

##  Parameters

`opacity`

    

A value between 0 (fully transparent) and 1 (fully opaque).

## Return Value

An effect that sets the transparency of the view.

## Discussion

When applying the `opacity(_:)` effect to a view that has already had its
opacity transformed, the effect of the underlying opacity transformation is
multiplied.

## See Also

### Adjusting Color

`func brightness(Double) -> some VisualEffect`

Brightens the view by the specified amount.

`func colorEffect(Shader, isEnabled: Bool) -> some VisualEffect`

Returns a new visual effect that applies `shader` to `self` as a filter effect
on the color of each pixel.

`func contrast(Double) -> some VisualEffect`

Sets the contrast and separation between similar colors in the view.

`func grayscale(Double) -> some VisualEffect`

Adds a grayscale effect to the view.

`func hueRotation(Angle) -> some VisualEffect`

Applies a hue rotation effect to the view.

`func saturation(Double) -> some VisualEffect`

Adjusts the color saturation of the view.

Instance Method

# scaleEffect(_:anchor:)

Scales the view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func scaleEffect(
        _ scale: CGFloat,
        anchor: UnitPoint = .center
    ) -> some VisualEffect
    

##  Parameters

`s`

    

The amount to scale the view in the view in both the horizontal and vertical
directions.

`anchor`

    

The point with a default of `center` that defines the location within the view
from which to apply the transformation.

## Return Value

An effect that scales the view’s rendered output.

## See Also

### Scaling

`func scaleEffect(CGSize, anchor: UnitPoint) -> some VisualEffect`

Scales the view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some
VisualEffect`

Scales the view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> some VisualEffect`

Scales this view uniformly by the specified size in each dimension.

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> some VisualEffect`

Scales this view uniformly by the specified factor.

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
some VisualEffect`

Scales this view by the specified horizontal, vertical, and depth factors.

Instance Method

# scaleEffect(_:anchor:)

Scales the view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func scaleEffect(
        _ scale: CGSize,
        anchor: UnitPoint = .center
    ) -> some VisualEffect
    

##  Parameters

`scale`

    

A `CGSize` that represents the horizontal and vertical amount to scale the
view.

`anchor`

    

The point with a default of `center` that defines the location within the view
from which to apply the transformation.

## Return Value

An effect that scales the view’s rendered output.

## See Also

### Scaling

`func scaleEffect(CGFloat, anchor: UnitPoint) -> some VisualEffect`

Scales the view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some
VisualEffect`

Scales the view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> some VisualEffect`

Scales this view uniformly by the specified size in each dimension.

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> some VisualEffect`

Scales this view uniformly by the specified factor.

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
some VisualEffect`

Scales this view by the specified horizontal, vertical, and depth factors.

Instance Method

# scaleEffect(x:y:anchor:)

Scales the view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func scaleEffect(
        x: CGFloat = 1.0,
        y: CGFloat = 1.0,
        anchor: UnitPoint = .center
    ) -> some VisualEffect
    

##  Parameters

`x`

    

An amount that represents the horizontal amount to scale the view. The default
value is `1.0`.

`y`

    

An amount that represents the vertical amount to scale the view. The default
value is `1.0`.

`anchor`

    

The point with a default of `center` that defines the location within the view
from which to apply the transformation.

## Return Value

An effect that scales the view’s rendered output.

## See Also

### Scaling

`func scaleEffect(CGFloat, anchor: UnitPoint) -> some VisualEffect`

Scales the view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(CGSize, anchor: UnitPoint) -> some VisualEffect`

Scales the view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> some VisualEffect`

Scales this view uniformly by the specified size in each dimension.

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> some VisualEffect`

Scales this view uniformly by the specified factor.

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
some VisualEffect`

Scales this view by the specified horizontal, vertical, and depth factors.

Instance Method

# scaleEffect(_:anchor:)

Scales this view uniformly by the specified size in each dimension.

visionOS 1.0+

    
    
    func scaleEffect(
        _ scale: Size3D,
        anchor: UnitPoint3D = .center
    ) -> some VisualEffect
    

##  Parameters

`scale`

    

The scale factor for this view in each dimension.

`anchor`

    

The anchor point about which to scale the view. Defaults to center.

## Return Value

An effect that scales this view by `scale`.

## Discussion

The original dimensions of the view are considered to be unchanged by scaling
the contents. To change the dimensions of the view, use a modifier like
`frame()` instead.

## See Also

### Scaling

`func scaleEffect(CGFloat, anchor: UnitPoint) -> some VisualEffect`

Scales the view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(CGSize, anchor: UnitPoint) -> some VisualEffect`

Scales the view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some
VisualEffect`

Scales the view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> some VisualEffect`

Scales this view uniformly by the specified factor.

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
some VisualEffect`

Scales this view by the specified horizontal, vertical, and depth factors.

Instance Method

# scaleEffect(_:anchor:)

Scales this view uniformly by the specified factor.

visionOS 1.0+

    
    
    func scaleEffect(
        _ s: CGFloat,
        anchor: UnitPoint3D = .center
    ) -> some VisualEffect
    

##  Parameters

`s`

    

The scale factor for this view.

`anchor`

    

The anchor point about which to scale the view. Defaults to center.

## Return Value

An effect that scales this view by `s` in all dimensions.

## Discussion

The original dimensions of the view are considered to be unchanged by scaling
the contents. To change the dimensions of the view, use a modifier like
`frame()` instead.

## See Also

### Scaling

`func scaleEffect(CGFloat, anchor: UnitPoint) -> some VisualEffect`

Scales the view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(CGSize, anchor: UnitPoint) -> some VisualEffect`

Scales the view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some
VisualEffect`

Scales the view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> some VisualEffect`

Scales this view uniformly by the specified size in each dimension.

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
some VisualEffect`

Scales this view by the specified horizontal, vertical, and depth factors.

Instance Method

# scaleEffect(x:y:z:anchor:)

Scales this view by the specified horizontal, vertical, and depth factors.

visionOS 1.0+

    
    
    func scaleEffect(
        x: CGFloat = 1.0,
        y: CGFloat = 1.0,
        z: CGFloat = 1.0,
        anchor: UnitPoint3D = .center
    ) -> some VisualEffect
    

##  Parameters

`x`

    

The horizontal scale factor for this view.

`y`

    

The vertical scale factor for this view.

`z`

    

The depth scale factor for this view.

`anchor`

    

The anchor point about which to scale the view. Defaults to center.

## Return Value

An effect that scales this view by `x`,`y`, and `z`.

## Discussion

The original dimensions of the view are considered to be unchanged by scaling
the contents. To change the dimensions of the view, use a modifier like
`frame()` instead.

## See Also

### Scaling

`func scaleEffect(CGFloat, anchor: UnitPoint) -> some VisualEffect`

Scales the view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(CGSize, anchor: UnitPoint) -> some VisualEffect`

Scales the view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some
VisualEffect`

Scales the view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> some VisualEffect`

Scales this view uniformly by the specified size in each dimension.

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> some VisualEffect`

Scales this view uniformly by the specified factor.

Instance Method

# rotationEffect(_:anchor:)

Rotates content in two dimensions around the specified point.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func rotationEffect(
        _ angle: Angle,
        anchor: UnitPoint = .center
    ) -> some VisualEffect
    

##  Parameters

`angle`

    

The angle by which to rotate the content.

`anchor`

    

A unit point within the content about which to perform the rotation. The
default value is `center`.

## Return Value

A rotation effect.

## Discussion

This effect rotates the content around the axis that points out of the xy-
plane. It has no effect on the content’s frame. The following code rotates
text by 22˚ and then draws a border around the modified view to show that the
frame remains unchanged by the rotation:

## See Also

### Rotating

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some
VisualEffect`

Renders content as if it’s rotated in three dimensions around the specified
axis.

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint3D, perspective: CGFloat) -> some VisualEffect`

Renders content as if it’s rotated in three dimensions around the specified
axis.

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some VisualEffect`

Rotates content by the specified 3D rotation value.

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
some VisualEffect`

Rotates content by an angle about an axis that you specify as a rotation axis
value.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> some VisualEffect`

Rotates content by an angle about an axis that you specify as a tuple of
elements.

Instance Method

# rotation3DEffect(_:axis:anchor:anchorZ:perspective:)

Renders content as if it’s rotated in three dimensions around the specified
axis.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func rotation3DEffect(
        _ angle: Angle,
        axis: (x: CGFloat, y: CGFloat, z: CGFloat),
        anchor: UnitPoint = .center,
        anchorZ: CGFloat = 0,
        perspective: CGFloat = 1
    ) -> some VisualEffect
    

##  Parameters

`angle`

    

The angle by which to rotate the content.

`axis`

    

The axis of rotation, specified as a tuple with named elements for each of the
three spatial dimensions.

`anchor`

    

A two dimensional unit point within the content about which to perform the
rotation. The default value is `center`.

`anchorZ`

    

The location on the z-axis around which to rotate the content. The default is
`0`.

`perspective`

    

The relative vanishing point for the rotation. The default is `1`.

## Return Value

A rotation effect.

## Discussion

Use this method to create the effect of rotating a two dimensional view in
three dimensions around a specified axis of rotation. The effect projects the
rotated content onto the original content’s plane. Use the `perspective` input
to control the renderer’s vanishing point. The following example creates the
appearance of rotating text 45˚ about the y-axis:

Important

In visionOS, create this effect with
`perspectiveRotationEffect(_:axis:anchor:perspective:)` instead. To truly
rotate a view in three dimensions, use a 3D rotation effect without a
perspective input like `rotation3DEffect(_:axis:anchor:)`.

## See Also

### Rotating

`func rotationEffect(Angle, anchor: UnitPoint) -> some VisualEffect`

Rotates content in two dimensions around the specified point.

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint3D, perspective: CGFloat) -> some VisualEffect`

Renders content as if it’s rotated in three dimensions around the specified
axis.

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some VisualEffect`

Rotates content by the specified 3D rotation value.

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
some VisualEffect`

Rotates content by an angle about an axis that you specify as a rotation axis
value.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> some VisualEffect`

Rotates content by an angle about an axis that you specify as a tuple of
elements.

Instance Method

# perspectiveRotationEffect(_:axis:anchor:perspective:)

Renders content as if it’s rotated in three dimensions around the specified
axis.

visionOS 1.0+

    
    
    func perspectiveRotationEffect(
        _ angle: Angle,
        axis: (x: CGFloat, y: CGFloat, z: CGFloat),
        anchor: UnitPoint3D = .back,
        perspective: CGFloat = 1
    ) -> some VisualEffect
    

##  Parameters

`angle`

    

The angle by which to rotate the content.

`axis`

    

The axis of rotation, specified as a tuple with named elements for each of the
three spatial dimensions.

`anchor`

    

A unit point within the content about which to perform the rotation. The
default value is `center`.

`perspective`

    

The relative vanishing point for the rotation. The default is `1`.

## Return Value

A rotation effect.

## Discussion

Use this method to create the effect of rotating content in three dimensions
around a specified axis of rotation. The modifier projects two dimensional
content onto the original content’s plane. Use the `perspective` input to
control the renderer’s vanishing point. The following example creates the
appearance of rotating text 45˚ about the y-axis:

Important

To truly rotate content in three dimensions, use a 3D rotation effect without
a perspective input like `rotation3DEffect(_:axis:anchor:)`.

## See Also

### Rotating

`func rotationEffect(Angle, anchor: UnitPoint) -> some VisualEffect`

Rotates content in two dimensions around the specified point.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some
VisualEffect`

Renders content as if it’s rotated in three dimensions around the specified
axis.

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some VisualEffect`

Rotates content by the specified 3D rotation value.

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
some VisualEffect`

Rotates content by an angle about an axis that you specify as a rotation axis
value.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> some VisualEffect`

Rotates content by an angle about an axis that you specify as a tuple of
elements.

Instance Method

# rotation3DEffect(_:anchor:)

Rotates content by the specified 3D rotation value.

visionOS 1.0+

    
    
    func rotation3DEffect(
        _ rotation: Rotation3D,
        anchor: UnitPoint3D = .center
    ) -> some VisualEffect
    

##  Parameters

`rotation`

    

A rotation to apply to the content.

`anchor`

    

The unit point within the content about which to perform the rotation. The
default value is `center`.

## Return Value

A rotation effect.

## Discussion

This effect causes the content to appear rotated, but doesn’t change the
content’s frame. The following code applies a rotation of 45° about the
y-axis, using the default anchor point at the center of the content:

## See Also

### Rotating

`func rotationEffect(Angle, anchor: UnitPoint) -> some VisualEffect`

Rotates content in two dimensions around the specified point.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some
VisualEffect`

Renders content as if it’s rotated in three dimensions around the specified
axis.

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint3D, perspective: CGFloat) -> some VisualEffect`

Renders content as if it’s rotated in three dimensions around the specified
axis.

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
some VisualEffect`

Rotates content by an angle about an axis that you specify as a rotation axis
value.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> some VisualEffect`

Rotates content by an angle about an axis that you specify as a tuple of
elements.

Instance Method

# rotation3DEffect(_:axis:anchor:)

Rotates content by an angle about an axis that you specify as a rotation axis
value.

visionOS 1.0+

    
    
    func rotation3DEffect(
        _ angle: Angle,
        axis: RotationAxis3D,
        anchor: UnitPoint3D = .center
    ) -> some VisualEffect
    

##  Parameters

`angle`

    

The angle by which to rotate the view’s content.

`axis`

    

The axis of rotation.

`anchor`

    

The unit point within the content about which to perform the rotation. The
default value is `center`.

## Return Value

A rotation effect.

## Discussion

This effect causes the content to appear rotated, but doesn’t change the
content’s frame. The following code applies a rotation of 45° about the
y-axis, using the default anchor point at the center of the content:

## See Also

### Rotating

`func rotationEffect(Angle, anchor: UnitPoint) -> some VisualEffect`

Rotates content in two dimensions around the specified point.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some
VisualEffect`

Renders content as if it’s rotated in three dimensions around the specified
axis.

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint3D, perspective: CGFloat) -> some VisualEffect`

Renders content as if it’s rotated in three dimensions around the specified
axis.

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some VisualEffect`

Rotates content by the specified 3D rotation value.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> some VisualEffect`

Rotates content by an angle about an axis that you specify as a tuple of
elements.

Instance Method

# rotation3DEffect(_:axis:anchor:)

Rotates content by an angle about an axis that you specify as a tuple of
elements.

visionOS 1.0+

    
    
    func rotation3DEffect(
        _ angle: Angle,
        axis: (x: CGFloat, y: CGFloat, z: CGFloat),
        anchor: UnitPoint3D = .center
    ) -> some VisualEffect
    

##  Parameters

`angle`

    

The angle by which to rotate the content.

`axis`

    

The axis of rotation, specified as a tuple with named elements for each of the
three spatial dimensions.

`anchor`

    

The unit point within the content about which to perform the rotation. The
default value is `center`.

## Return Value

A rotation effect.

## Discussion

This effect causes the content to appear rotated, but doesn’t change the
content’s frame. The following code applies a rotation of 45° about the
y-axis, using the default anchor point at the center of the content:

## See Also

### Rotating

`func rotationEffect(Angle, anchor: UnitPoint) -> some VisualEffect`

Rotates content in two dimensions around the specified point.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some
VisualEffect`

Renders content as if it’s rotated in three dimensions around the specified
axis.

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint3D, perspective: CGFloat) -> some VisualEffect`

Renders content as if it’s rotated in three dimensions around the specified
axis.

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some VisualEffect`

Rotates content by the specified 3D rotation value.

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
some VisualEffect`

Rotates content by an angle about an axis that you specify as a rotation axis
value.

Instance Method

# offset(_:)

Offsets the view by the horizontal and vertical amount specified in the offset
parameter.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func offset(_ offset: CGSize) -> some VisualEffect
    

##  Parameters

`offset`

    

The distance to offset the view.

## Return Value

An effect that offsets the view by `offset`.

## See Also

### Translating

`func offset(x: CGFloat, y: CGFloat) -> some VisualEffect`

Offsets the view by the specified horizontal and vertical distances.

`func offset(z: CGFloat) -> some VisualEffect`

Brings a view forward in Z by the provided distance in points.

Instance Method

# offset(x:y:)

Offsets the view by the specified horizontal and vertical distances.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func offset(
        x: CGFloat = 0,
        y: CGFloat = 0
    ) -> some VisualEffect
    

##  Parameters

`x`

    

The horizontal distance to offset the view.

`y`

    

The vertical distance to offset the view.

## Return Value

An effect that offsets the view by `x` and `y`.

## See Also

### Translating

`func offset(CGSize) -> some VisualEffect`

Offsets the view by the horizontal and vertical amount specified in the offset
parameter.

`func offset(z: CGFloat) -> some VisualEffect`

Brings a view forward in Z by the provided distance in points.

Instance Method

# offset(z:)

Brings a view forward in Z by the provided distance in points.

visionOS 1.0+

    
    
    func offset(z: CGFloat) -> some VisualEffect
    

##  Parameters

`distance`

    

The distance to extrude the view forward in Z, in points.

## Return Value

An effect that is extruded forward in Z by `distance`.

## See Also

### Translating

`func offset(CGSize) -> some VisualEffect`

Offsets the view by the horizontal and vertical amount specified in the offset
parameter.

`func offset(x: CGFloat, y: CGFloat) -> some VisualEffect`

Offsets the view by the specified horizontal and vertical distances.

Instance Method

# transform3DEffect(_:)

Applies a 3D transformation to the receiver.

visionOS 1.0+

    
    
    func transform3DEffect(_ transform: AffineTransform3D) -> some VisualEffect
    

##  Parameters

`transform`

    

The 3D transformation to apply to the view, interpreting it as a 3D plane in
space.

## Return Value

An effect that renders transformed according to the provided `transform`

## See Also

### Applying a transform

`func transformEffect(CGAffineTransform) -> some VisualEffect`

Applies an affine transformation to the view’s rendered output.

`func transformEffect(ProjectionTransform) -> some VisualEffect`

Applies a projection transformation to the view’s rendered output.

Instance Method

# transformEffect(_:)

Applies an affine transformation to the view’s rendered output.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func transformEffect(_ transform: CGAffineTransform) -> some VisualEffect
    

##  Parameters

`transform`

    

A `CGAffineTransform` to apply to the view.

## Return Value

An effect that applies an affine transformation to the view’s rendered output.

## Discussion

Use `transformEffect(_:)` to rotate, scale, translate, or skew the output of
the view according to the provided `CGAffineTransform`.

## See Also

### Applying a transform

`func transform3DEffect(AffineTransform3D) -> some VisualEffect`

Applies a 3D transformation to the receiver.

`func transformEffect(ProjectionTransform) -> some VisualEffect`

Applies a projection transformation to the view’s rendered output.

Instance Method

# transformEffect(_:)

Applies a projection transformation to the view’s rendered output.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func transformEffect(_ transform: ProjectionTransform) -> some VisualEffect
    

##  Parameters

`transform`

    

A `ProjectionTransform` to apply to the view.

## Return Value

An effect that applies a projection transformation to the view’s rendered
output.

## Discussion

Use `transformEffect(_:)` to rotate, scale, translate, or skew the output of
the view according to the provided `ProjectionTransform`.

## See Also

### Applying a transform

`func transform3DEffect(AffineTransform3D) -> some VisualEffect`

Applies a 3D transformation to the receiver.

`func transformEffect(CGAffineTransform) -> some VisualEffect`

Applies an affine transformation to the view’s rendered output.

Instance Method

# blur(radius:opaque:)

Applies a Gaussian blur to the view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func blur(
        radius: CGFloat,
        opaque: Bool = false
    ) -> some VisualEffect
    

##  Parameters

`radius`

    

The radial size of the blur. A blur is more diffuse when its radius is large.

`opaque`

    

A Boolean value that indicates whether the blur renderer permits transparency
in the blur output. Set to `true` to create an opaque blur, or set to `false`
to permit transparency.

## Return Value

An effect that blurs the view.

## Discussion

Use `blur(radius:opaque:)` to apply a gaussian blur effect to the rendering of
the view.

## See Also

### Applying other effects

`func distortionEffect(Shader, maxSampleOffset: CGSize, isEnabled: Bool) ->
some VisualEffect`

Returns a new visual effect that applies `shader` to `self` as a geometric
distortion effect on the location of each pixel.

`func layerEffect(Shader, maxSampleOffset: CGSize, isEnabled: Bool) -> some
VisualEffect`

Returns a new visual effect that applies `shader` to `self` as a filter on the
raster layer created from `self`.

Instance Method

# distortionEffect(_:maxSampleOffset:isEnabled:)

Returns a new visual effect that applies `shader` to `self` as a geometric
distortion effect on the location of each pixel.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    func distortionEffect(
        _ shader: Shader,
        maxSampleOffset: CGSize,
        isEnabled: Bool = true
    ) -> some VisualEffect
    

##  Parameters

`shader`

    

The shader to apply as a distortion effect.

`maxSampleOffset`

    

The maximum distance in each axis between the returned source pixel position
and the destination pixel position, for all source pixels.

`isEnabled`

    

Whether the effect is enabled or not.

## Return Value

A new view that renders `self` with the shader applied as a distortion effect.

## Discussion

For a shader function to act as a distortion effect it must have a function
signature matching:

where `position` is the user-space coordinates of the destination pixel
applied to the shader. `args...` should be compatible with the uniform
arguments bound to `shader`. The function should return the user-space
coordinates of the corresponding source pixel.

Important

Views backed by AppKit or UIKit views may not render into the filtered layer.
Instead, they log a warning and display a placeholder image to highlight the
error.

## See Also

### Applying other effects

`func blur(radius: CGFloat, opaque: Bool) -> some VisualEffect`

Applies a Gaussian blur to the view.

`func layerEffect(Shader, maxSampleOffset: CGSize, isEnabled: Bool) -> some
VisualEffect`

Returns a new visual effect that applies `shader` to `self` as a filter on the
raster layer created from `self`.

Instance Method

# layerEffect(_:maxSampleOffset:isEnabled:)

Returns a new visual effect that applies `shader` to `self` as a filter on the
raster layer created from `self`.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    func layerEffect(
        _ shader: Shader,
        maxSampleOffset: CGSize,
        isEnabled: Bool = true
    ) -> some VisualEffect
    

##  Parameters

`shader`

    

The shader to apply as a layer effect.

`maxSampleOffset`

    

If the shader function samples from the layer at locations not equal to the
destination position, this value must specify the maximum sampling distance in
each axis, for all source pixels.

`isEnabled`

    

Whether the effect is enabled or not.

## Return Value

A new view that renders `self` with the shader applied as a distortion effect.

## Discussion

For a shader function to act as a layer effect it must have a function
signature matching:

where `position` is the user-space coordinates of the destination pixel
applied to the shader, and `layer` is a subregion of the rasterized contents
of `self`. `args...` should be compatible with the uniform arguments bound to
`shader`.

The `SwiftUI::Layer` type is defined in the `<SwiftUI/SwiftUI.h>` header file.
It exports a single `sample()` function that returns a linearly-filtered pixel
value from a position in the source content, as a premultiplied RGBA pixel
value:

The function should return the color mapping to the destination pixel,
typically by sampling one or more pixels from `layer` at location(s) derived
from `position` and them applying some kind of transformation to produce a new
color.

Important

Views backed by AppKit or UIKit views may not render into the filtered layer.
Instead, they log a warning and display a placeholder image to highlight the
error.

## See Also

### Applying other effects

`func blur(radius: CGFloat, opaque: Bool) -> some VisualEffect`

Applies a Gaussian blur to the view.

`func distortionEffect(Shader, maxSampleOffset: CGSize, isEnabled: Bool) ->
some VisualEffect`

Returns a new visual effect that applies `shader` to `self` as a geometric
distortion effect on the location of each pixel.



# ViewBuilder

Type Method

# buildBlock()

Builds an empty view from a block containing no statements.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static func buildBlock() -> EmptyView

## See Also

### Building content

`static func buildBlock<Content>(Content) -> Content`

Passes a single view written as a child view through unmodified.

`static func buildBlock<each Content>(repeat each Content) ->
TupleView<(repeat each Content)>`

`static func buildExpression<Content>(Content) -> Content`

Builds an expression within the builder.

Type Method

# buildBlock(_:)

Passes a single view written as a child view through unmodified.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static func buildBlock<Content>(_ content: Content) -> Content where Content : View

## Discussion

An example of a single view written as a child view is `{ Text("Hello") }`.

## See Also

### Building content

`static func buildBlock() -> EmptyView`

Builds an empty view from a block containing no statements.

`static func buildBlock<each Content>(repeat each Content) ->
TupleView<(repeat each Content)>`

`static func buildExpression<Content>(Content) -> Content`

Builds an expression within the builder.

Type Method

# buildBlock(_:)

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static func buildBlock<each Content>(_ content: repeat each Content) -> TupleView<(repeat each Content)> where repeat each Content : View

## See Also

### Building content

`static func buildBlock() -> EmptyView`

Builds an empty view from a block containing no statements.

`static func buildBlock<Content>(Content) -> Content`

Passes a single view written as a child view through unmodified.

`static func buildExpression<Content>(Content) -> Content`

Builds an expression within the builder.

Type Method

# buildExpression(_:)

Builds an expression within the builder.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static func buildExpression<Content>(_ content: Content) -> Content where Content : View

## See Also

### Building content

`static func buildBlock() -> EmptyView`

Builds an empty view from a block containing no statements.

`static func buildBlock<Content>(Content) -> Content`

Passes a single view written as a child view through unmodified.

`static func buildBlock<each Content>(repeat each Content) ->
TupleView<(repeat each Content)>`

Type Method

# buildEither(first:)

Produces content for a conditional statement in a multi-statement closure when
the condition is true.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static func buildEither<TrueContent, FalseContent>(first: TrueContent) -> _ConditionalContent<TrueContent, FalseContent> where TrueContent : View, FalseContent : View

## See Also

### Conditionally building content

`static func buildEither<TrueContent, FalseContent>(second: FalseContent) ->
_ConditionalContent<TrueContent, FalseContent>`

Produces content for a conditional statement in a multi-statement closure when
the condition is false.

`static func buildIf<Content>(Content?) -> Content?`

Produces an optional view for conditional statements in multi-statement
closures that’s only visible when the condition evaluates to true.

`static func buildLimitedAvailability<Content>(Content) -> AnyView`

Processes view content for a conditional compiler-control statement that
performs an availability check.

Type Method

# buildEither(second:)

Produces content for a conditional statement in a multi-statement closure when
the condition is false.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static func buildEither<TrueContent, FalseContent>(second: FalseContent) -> _ConditionalContent<TrueContent, FalseContent> where TrueContent : View, FalseContent : View

## See Also

### Conditionally building content

`static func buildEither<TrueContent, FalseContent>(first: TrueContent) ->
_ConditionalContent<TrueContent, FalseContent>`

Produces content for a conditional statement in a multi-statement closure when
the condition is true.

`static func buildIf<Content>(Content?) -> Content?`

Produces an optional view for conditional statements in multi-statement
closures that’s only visible when the condition evaluates to true.

`static func buildLimitedAvailability<Content>(Content) -> AnyView`

Processes view content for a conditional compiler-control statement that
performs an availability check.

Type Method

# buildIf(_:)

Produces an optional view for conditional statements in multi-statement
closures that’s only visible when the condition evaluates to true.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static func buildIf<Content>(_ content: Content?) -> Content? where Content : View

## See Also

### Conditionally building content

`static func buildEither<TrueContent, FalseContent>(first: TrueContent) ->
_ConditionalContent<TrueContent, FalseContent>`

Produces content for a conditional statement in a multi-statement closure when
the condition is true.

`static func buildEither<TrueContent, FalseContent>(second: FalseContent) ->
_ConditionalContent<TrueContent, FalseContent>`

Produces content for a conditional statement in a multi-statement closure when
the condition is false.

`static func buildLimitedAvailability<Content>(Content) -> AnyView`

Processes view content for a conditional compiler-control statement that
performs an availability check.

Type Method

# buildLimitedAvailability(_:)

Processes view content for a conditional compiler-control statement that
performs an availability check.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    static func buildLimitedAvailability<Content>(_ content: Content) -> AnyView where Content : View

## See Also

### Conditionally building content

`static func buildEither<TrueContent, FalseContent>(first: TrueContent) ->
_ConditionalContent<TrueContent, FalseContent>`

Produces content for a conditional statement in a multi-statement closure when
the condition is true.

`static func buildEither<TrueContent, FalseContent>(second: FalseContent) ->
_ConditionalContent<TrueContent, FalseContent>`

Produces content for a conditional statement in a multi-statement closure when
the condition is false.

`static func buildIf<Content>(Content?) -> Content?`

Produces an optional view for conditional statements in multi-statement
closures that’s only visible when the condition evaluates to true.



# VStackLayout

Initializer

# init(alignment:spacing:)

Creates a vertical stack with the specified spacing and horizontal alignment.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init(
        alignment: HorizontalAlignment = .center,
        spacing: CGFloat? = nil
    )

##  Parameters

`alignment`

    

The guide for aligning the subviews in this stack. It has the same horizontal
screen coordinate for all subviews.

`spacing`

    

The distance between adjacent subviews. Set this value to `nil` to use default
distances between subviews.

Instance Property

# alignment

The horizontal alignment of subviews.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var alignment: HorizontalAlignment

## See Also

### Getting the stack’s properties

`var spacing: CGFloat?`

The distance between adjacent subviews.

Instance Property

# spacing

The distance between adjacent subviews.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var spacing: CGFloat?

## Discussion

Set this value to `nil` to use default distances between subviews.

## See Also

### Getting the stack’s properties

`var alignment: HorizontalAlignment`

The horizontal alignment of subviews.



# ViewModifier

Instance Method

# body(content:)

Gets the current body of the caller.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @ViewBuilder @MainActor
    func body(content: Self.Content) -> Self.Body

**Required** Default implementation provided.

## Discussion

`content` is a proxy for the view that will have the modifier represented by
`Self` applied to it.

## Default Implementations

### ViewModifier Implementations

`func body(content: Self.Content) -> Self.Body`

Gets the current body of the caller.

Available when `Body` is `Never`.

## See Also

### Creating a view modifier

`associatedtype Body : View`

The type of view representing the body.

**Required**

` typealias Content`

The content view type passed to `body()`.

Associated Type

# Body

The type of view representing the body.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    associatedtype Body : View

**Required**

## See Also

### Creating a view modifier

`func body(content: Self.Content) -> Self.Body`

Gets the current body of the caller.

**Required** Default implementation provided.

`typealias Content`

The content view type passed to `body()`.

Type Alias

# ViewModifier.Content

The content view type passed to `body()`.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    typealias Content

## See Also

### Creating a view modifier

`func body(content: Self.Content) -> Self.Body`

Gets the current body of the caller.

**Required** Default implementation provided.

`associatedtype Body : View`

The type of view representing the body.

**Required**

Instance Method

# animation(_:)

Returns a new version of the modifier that will apply `animation` to all
animatable values within the modifier.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func animation(_ animation: Animation?) -> some ViewModifier
    

## See Also

### Adding animations to a view

`func concat<T>(T) -> ModifiedContent<Self, T>`

Returns a new modifier that is the result of concatenating `self` with
`modifier`.

Instance Method

# concat(_:)

Returns a new modifier that is the result of concatenating `self` with
`modifier`.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func concat<T>(_ modifier: T) -> ModifiedContent<Self, T>

## See Also

### Adding animations to a view

`func animation(Animation?) -> some ViewModifier`

Returns a new version of the modifier that will apply `animation` to all
animatable values within the modifier.

Instance Method

# transaction(_:)

Returns a new version of the modifier that will apply the transaction mutation
function `transform` to all transactions within the modifier.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func transaction(_ transform: @escaping (inout Transaction) -> Void) -> some ViewModifier
    



# VStack

Initializer

# init(alignment:spacing:content:)

Creates an instance with the given spacing and horizontal alignment.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        alignment: HorizontalAlignment = .center,
        spacing: CGFloat? = nil,
        @ViewBuilder content: () -> Content
    )

##  Parameters

`alignment`

    

The guide for aligning the subviews in this stack. This guide has the same
vertical screen coordinate for every subview.

`spacing`

    

The distance between adjacent subviews, or `nil` if you want the stack to
choose a default distance for each pair of subviews.

`content`

    

A view builder that creates the content of this stack.



# VerticalAlignment

Type Property

# top

A guide that marks the top edge of the view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let top: VerticalAlignment

## Discussion

Use this guide to align the top edges of views:

The following code generates the image above using an `HStack`:

## See Also

### Getting guides

`static let center: VerticalAlignment`

A guide that marks the vertical center of the view.

`static let bottom: VerticalAlignment`

A guide that marks the bottom edge of the view.

`static let firstTextBaseline: VerticalAlignment`

A guide that marks the top-most text baseline in a view.

`static let lastTextBaseline: VerticalAlignment`

A guide that marks the bottom-most text baseline in a view.

Type Property

# center

A guide that marks the vertical center of the view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let center: VerticalAlignment

## Discussion

Use this guide to align the centers of views:

The following code generates the image above using an `HStack`:

## See Also

### Getting guides

`static let top: VerticalAlignment`

A guide that marks the top edge of the view.

`static let bottom: VerticalAlignment`

A guide that marks the bottom edge of the view.

`static let firstTextBaseline: VerticalAlignment`

A guide that marks the top-most text baseline in a view.

`static let lastTextBaseline: VerticalAlignment`

A guide that marks the bottom-most text baseline in a view.

Type Property

# bottom

A guide that marks the bottom edge of the view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let bottom: VerticalAlignment

## Discussion

Use this guide to align the bottom edges of views:

The following code generates the image above using an `HStack`:

## See Also

### Getting guides

`static let top: VerticalAlignment`

A guide that marks the top edge of the view.

`static let center: VerticalAlignment`

A guide that marks the vertical center of the view.

`static let firstTextBaseline: VerticalAlignment`

A guide that marks the top-most text baseline in a view.

`static let lastTextBaseline: VerticalAlignment`

A guide that marks the bottom-most text baseline in a view.

Type Property

# firstTextBaseline

A guide that marks the top-most text baseline in a view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let firstTextBaseline: VerticalAlignment

## Discussion

Use this guide to align with the baseline of the top-most text in a view. The
guide aligns with the bottom of a view that contains no text:

The following code generates the image above using an `HStack`:

## See Also

### Getting guides

`static let top: VerticalAlignment`

A guide that marks the top edge of the view.

`static let center: VerticalAlignment`

A guide that marks the vertical center of the view.

`static let bottom: VerticalAlignment`

A guide that marks the bottom edge of the view.

`static let lastTextBaseline: VerticalAlignment`

A guide that marks the bottom-most text baseline in a view.

Type Property

# lastTextBaseline

A guide that marks the bottom-most text baseline in a view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let lastTextBaseline: VerticalAlignment

## Discussion

Use this guide to align with the baseline of the bottom-most text in a view.
The guide aligns with the bottom of a view that contains no text.

The following code generates the image above using an `HStack`:

## See Also

### Getting guides

`static let top: VerticalAlignment`

A guide that marks the top edge of the view.

`static let center: VerticalAlignment`

A guide that marks the vertical center of the view.

`static let bottom: VerticalAlignment`

A guide that marks the bottom edge of the view.

`static let firstTextBaseline: VerticalAlignment`

A guide that marks the top-most text baseline in a view.

Initializer

# init(_:)

Creates a custom vertical alignment of the specified type.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(_ id: any AlignmentID.Type)

##  Parameters

`id`

    

The type of an identifier that uniquely identifies a vertical alignment.

## Discussion

Use this initializer to create a custom vertical alignment. Define an
`AlignmentID` type, and then use that type to create a new static property on
`VerticalAlignment`:

Every vertical alignment instance that you create needs a unique identifier.
For more information, see `AlignmentID`.

## See Also

### Creating a custom alignment

`func combineExplicit<S>(S) -> CGFloat?`

Merges a sequence of explicit alignment values produced by this instance.

Instance Method

# combineExplicit(_:)

Merges a sequence of explicit alignment values produced by this instance.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func combineExplicit<S>(_ values: S) -> CGFloat? where S : Sequence, S.Element == CGFloat?

## Discussion

For most alignment types, this method returns the mean of all non-`nil`
values. However, some types use other rules. For example, `firstTextBaseline`
returns the minimum value, while `lastTextBaseline` returns the maximum value.

## See Also

### Creating a custom alignment

`init(any AlignmentID.Type)`

Creates a custom vertical alignment of the specified type.



# View fundamentals

Article

# Declaring a custom view

Define views and assemble them into a view hierarchy.

## Overview

SwiftUI offers a declarative approach to user interface design. With a
traditional imperative approach, the burden is on your controller code not
only to instantiate, lay out, and configure views, but also to continually
make updates as conditions change. In contrast, with a declarative approach,
you create a lightweight description of your user interface by declaring views
in a hierarchy that mirrors the desired layout of your interface. SwiftUI then
manages drawing and updating these views in response to events like user input
or state changes.

SwiftUI provides tools for defining and configuring the views in your user
interface. You compose custom views out of built-in views that SwiftUI
provides, plus other composite views that you’ve already defined. You
configure these views with view modifiers and connect them to your data model.
You then place your custom views within your app’s view hierarchy.

### Conform to the view protocol

Declare a custom view type by defining a structure that conforms to the `View`
protocol:

Like other Swift protocols, the `View` protocol provides a blueprint for
functionality — in this case, the behavior of an element that SwiftUI draws
onscreen. Conformance to the protocol comes with both requirements that a view
must fulfill, and functionality that the protocol provides. After you fulfill
the requirements, you can insert your custom view into a view hierarchy so
that it becomes part of your app’s user interface.

### Declare a body

The `View` protocol’s main requirement is that conforming types must define a
`body` computed property:

SwiftUI reads the value of this property any time it needs to update the view,
which can happen repeatedly during the life of the view, typically in response
to user input or system events. The value that the view returns is an element
that SwiftUI draws onscreen.

The `View` protocol’s secondary requirement is that conforming types must
indicate an associated type for the body property. However, you don’t make an
explicit declaration. Instead, you declare the body property as an opaque
type, using the `some View` syntax, to indicate only that the body’s type
conforms to `View`. The exact type depends on the body’s content, which varies
as you edit the body during development. Swift infers the exact type
automatically.

### Assemble the view’s content

Describe your view’s appearance by adding content to the view’s body property.
You can compose the body from built-in views that SwiftUI provides, as well as
custom views that you’ve defined elsewhere. For example, you can create a body
that draws the string “Hello, World!” using a built-in `Text` view:

In addition to views for specific kinds of content, controls, and indicators,
like `Text`, `Toggle`, and `ProgressView`, SwiftUI also provides built-in
views that you can use to arrange other views. For example, you can vertically
stack two `Text` views using a `VStack`:

Views that take multiple input child views, like the stack in the example
above, typically do so using a closure marked with the `ViewBuilder`
attribute. This enables a multiple-statement closure that doesn’t require
additional syntax at the call site. You only need to list the input views in
succession.

For examples of views that contain other views, see Layout fundamentals.

### Configure views with modifiers

To configure the views in your view’s body, you apply view modifiers. A
modifier is nothing more than a method called on a particular view. The method
returns a new, altered view that effectively takes the place of the original
in the view hierarchy.

SwiftUI extends the `View` protocol with a large set of methods for this
purpose. All `View` protocol conformers — both built-in and custom views —
have access to these methods that alter the behavior of a view in some way.
For example, you can change the font of a text view by applying the `font(_:)`
modifier:

For more information about how view modifiers work, and how to use them on
your views, see Configuring views.

### Manage data

To supply inputs to your views, add properties. For example, you can make the
font of the “Hello, World!” string configurable:

If an input value changes, SwiftUI notices the change and redraws only the
affected parts of your interface. This might involve reinitializing your
entire view, but SwiftUI manages that for you.

Because the system may reinitialize a view at any time, it’s important to
avoid doing any significant work in your view’s initialization code. It’s
often best to omit an explicit initializer, as in the example above, allowing
Swift to synthesize a _member-wise initializer_ instead.

SwiftUI provides many tools to help you manage your app’s data under these
constraints, as described in Model data. For information about Swift
initializers, see Initialization in _The Swift Programming Language_.

### Add your view to the view hierarchy

After you define a view, you can incorporate it in other views, just like you
do with built-in views. You add your view by declaring it at the point in the
hierarchy at which you want it to appear. For example, you could put `MyView`
in your app’s `ContentView`, which Xcode creates automatically as the root
view of a new app:

Alternatively, you could add your view as the root view of a new scene in your
app, like the `Settings` scene that declares content for a macOS preferences
window, or a `WKNotificationScene` scene that declares the content for a
watchOS notification. For more information about defining your app structure
with SwiftUI, see App organization.

## See Also

### Creating a view

`protocol View`

A type that represents part of your app’s user interface and provides
modifiers that you use to configure views.

`struct ViewBuilder`

A custom parameter attribute that constructs views from closures.

Protocol

# View

A type that represents part of your app’s user interface and provides
modifiers that you use to configure views.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    protocol View

## Overview

You create custom views by declaring types that conform to the `View`
protocol. Implement the required `body` computed property to provide the
content for your custom view.

Assemble the view’s body by combining one or more of the built-in views
provided by SwiftUI, like the `Text` instance in the example above, plus other
custom views that you define, into a hierarchy of views. For more information
about creating custom views, see Declaring a custom view.

The `View` protocol provides a set of modifiers — protocol methods with
default implementations — that you use to configure views in the layout of
your app. Modifiers work by wrapping the view instance on which you call them
in another view with the specified characteristics, as described in
Configuring views. For example, adding the `opacity(_:)` modifier to a text
view returns a new view with some amount of transparency:

The complete list of default modifiers provides a large set of controls for
managing views. For example, you can fine tune Layout modifiers, add
Accessibility modifiers information, and respond to Input and event modifiers.
You can also collect groups of default modifiers into new, custom view
modifiers for easy reuse.

## Topics

### Implementing a custom view

`var body: Self.Body`

The content and behavior of the view.

**Required** Default implementations provided.

`associatedtype Body : View`

The type of view representing the body of this view.

**Required**

` func modifier<T>(T) -> ModifiedContent<Self, T>`

Applies a modifier to a view and returns a new view.

API Reference

Previews in Xcode

Generate dynamic, interactive previews of your custom views.

### Configuring view elements

API Reference

Accessibility modifiers

Make your SwiftUI apps accessible to everyone, including people with
disabilities.

API Reference

Appearance modifiers

Configure a view’s foreground and background styles, controls, and visibility.

API Reference

Text and symbol modifiers

Manage the rendering, selection, and entry of text in your view.

API Reference

Auxiliary view modifiers

Add and configure supporting views, like toolbars and context menus.

API Reference

Chart view modifiers

Configure charts that you declare with Swift Charts.

### Drawing views

API Reference

Style modifiers

Apply built-in styles to different types of views.

API Reference

Layout modifiers

Tell a view how to arrange itself within a view hierarchy by adjusting its
size, position, alignment, padding, and so on.

API Reference

Graphics and rendering modifiers

Affect the way the system draws a view, for example by scaling or masking a
view, or by applying graphical effects.

### Providing interactivity

API Reference

Input and event modifiers

Supply actions for a view to perform in response to user input and system
events.

API Reference

Search modifiers

Enable people to search for content in your app.

API Reference

Presentation modifiers

Define additional views for the view to present under specified conditions.

API Reference

State modifiers

Access storage and provide child views with configuration data.

### Deprecated modifiers

API Reference

Deprecated modifiers

Review unsupported modifiers and their replacements.

### Instance Methods

`func addOrderToWalletButtonStyle(AddOrderToWalletButtonStyle) -> some View`

Sets the button’s style.

`func addPassToWalletButtonStyle(AddPassToWalletButtonStyle) -> some View`

Sets the style to be used by the button. (see `PKAddPassButtonStyle`).

`func automatedDeviceEnrollmentAddition(isPresented: Binding<Bool>) -> some
View`

Presents a modal view that enables users to add devices to their organization.

`func complicationForeground() -> some View`

Promotes this view to the foreground in a complication.

Deprecated

`func continuityDevicePicker(isPresented: Binding<Bool>, onDidConnect:
((AVContinuityDevice?) -> Void)?) -> some View`

A `continuityDevicePicker` should be used to discover and connect nearby
continuity device through a button interface or other form of activation. On
tvOS, this presents a fullscreen continuity device picker experience when
selected. The modal view covers as much the screen of `self` as possible when
a given condition is true.

`func lookAroundViewer(isPresented: Binding<Bool>, initialScene:
MKLookAroundScene?, allowsNavigation: Bool, showsRoadLabels: Bool,
pointsOfInterest: PointOfInterestCategories, onDismiss: (() -> Void)?) -> some
View`

`func lookAroundViewer(isPresented: Binding<Bool>, scene:
Binding<MKLookAroundScene?>, allowsNavigation: Bool, showsRoadLabels: Bool,
pointsOfInterest: PointOfInterestCategories, onDismiss: (() -> Void)?) -> some
View`

`func mapCameraKeyframeAnimator(trigger: some Equatable, keyframes:
(MapCamera) -> some Keyframes<MapCamera>) -> some View`

Uses the given keyframes to animate the camera of a `Map` when the given
trigger value changes.

`func mapControlVisibility(Visibility) -> some View`

Configures all Map controls in the environment to have the specified
visibility

`func mapControls(() -> some View) -> some View`

Configures all `Map` views in the associated environment to have standard size
and position controls

`func mapFeatureSelectionContent(content: (MapFeature) -> some MapContent) ->
some View`

Specifies a custom presentation for the currently selected feature.

`func mapFeatureSelectionDisabled((MapFeature) -> Bool) -> some View`

Specifies which map features should have selection disabled.

`func mapScope(Namespace.ID) -> some View`

Creates a mapScope that SwiftUI uses to connect map controls to an associated
map.

`func mapStyle(MapStyle) -> some View`

Specifies the map style to be used.

`func onApplePayCouponCodeChange(perform: (String) async ->
PKPaymentRequestCouponCodeUpdate) -> some View`

Called when a user has entered or updated a coupon code. This is required if
the user is being asked to provide a coupon code.

`func onApplePayPaymentMethodChange(perform: (PKPaymentMethod) async ->
PKPaymentRequestPaymentMethodUpdate) -> some View`

Called when a payment method has changed and asks for an update payment
request. If this modifier isn’t provided Wallet will assume the payment method
is valid.

`func onApplePayShippingContactChange(perform: (PKContact) async ->
PKPaymentRequestShippingContactUpdate) -> some View`

Called when a user selected a shipping address. This is required if the user
is being asked to provide a shipping contact.

`func onApplePayShippingMethodChange(perform: (PKShippingMethod) async ->
PKPaymentRequestShippingMethodUpdate) -> some View`

Called when a user selected a shipping method. This is required if the user is
being asked to provide a shipping method.

`func onMapCameraChange(frequency: MapCameraUpdateFrequency, () -> Void) ->
some View`

Performs an action when Map camera framing changes

`func onMapCameraChange(frequency: MapCameraUpdateFrequency,
(MapCameraUpdateContext) -> Void) -> some View`

Performs an action when Map camera framing changes

`func payLaterViewAction(PayLaterViewAction) -> some View`

Sets the action on the PayLaterView. See `PKPayLaterAction`.

`func payLaterViewDisplayStyle(PayLaterViewDisplayStyle) -> some View`

Sets the display style on the PayLaterView. See `PKPayLaterDisplayStyle`.

`func payWithApplePayButtonStyle(PayWithApplePayButtonStyle) -> some View`

Sets the style to be used by the button. (see `PayWithApplePayButtonStyle`).

`func translationPresentation(isPresented: Binding<Bool>, text: String,
attachmentAnchor: PopoverAttachmentAnchor, arrowEdge: Edge, replacementAction:
((String) -> Void)?) -> some View`

`func verifyIdentityWithWalletButtonStyle(VerifyIdentityWithWalletButtonStyle)
-> some View`

Sets the style to be used by the button. (see `PKIdentityButtonStyle`).

## Relationships

### Inherited By

  * `DynamicViewContent`
  * `InsettableShape`
  * `NSViewControllerRepresentable`
  * `NSViewRepresentable`
  * `Shape`
  * `ShapeView`
  * `UIViewControllerRepresentable`
  * `UIViewRepresentable`
  * `WKInterfaceObjectRepresentable`

### Conforming Types

  * `AngularGradient`
  * `AnyShape`
  * `AnyView`
  * `AsyncImage`
  * `Button`
  * `ButtonBorderShape`
  * `ButtonStyleConfiguration.Label`
  * `Canvas`

Conforms when `Symbols` conforms to `View`.

  * `Capsule`
  * `Circle`
  * `Color`
  * `ColorPicker`
  * `ContainerRelativeShape`
  * `ContentUnavailableView`
  * `ControlGroup`
  * `ControlGroupStyleConfiguration.Content`
  * `ControlGroupStyleConfiguration.Label`
  * `DatePicker`
  * `DatePickerStyleConfiguration.Label`
  * `DefaultDateProgressLabel`
  * `DefaultSettingsLinkLabel`
  * `DefaultShareLinkLabel`
  * `DisclosureGroup`
  * `DisclosureGroupStyleConfiguration.Content`
  * `DisclosureGroupStyleConfiguration.Label`
  * `Divider`
  * `EditButton`
  * `EditableCollectionContent`

Conforms when `Content` conforms to `View`.

  * `Ellipse`
  * `EllipticalGradient`
  * `EmptyView`
  * `EquatableView`
  * `FillShapeView`
  * `ForEach`

Conforms when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `View`.

  * `Form`
  * `FormStyleConfiguration.Content`
  * `Gauge`
  * `GaugeStyleConfiguration.CurrentValueLabel`
  * `GaugeStyleConfiguration.Label`
  * `GaugeStyleConfiguration.MarkedValueLabel`
  * `GaugeStyleConfiguration.MaximumValueLabel`
  * `GaugeStyleConfiguration.MinimumValueLabel`
  * `GeometryReader`
  * `GeometryReader3D`
  * `Grid`

Conforms when `Content` conforms to `View`.

  * `GridRow`

Conforms when `Content` conforms to `View`.

  * `Group`

Conforms when `Content` conforms to `View`.

  * `GroupBox`
  * `GroupBoxStyleConfiguration.Content`
  * `GroupBoxStyleConfiguration.Label`
  * `HSplitView`
  * `HStack`
  * `HelpLink`
  * `Image`
  * `KeyframeAnimator`
  * `Label`
  * `LabelStyleConfiguration.Icon`
  * `LabelStyleConfiguration.Title`
  * `LabeledContent`

Conforms when `Label` conforms to `View` and `Content` conforms to `View`.

  * `LabeledContentStyleConfiguration.Content`
  * `LabeledContentStyleConfiguration.Label`
  * `LabeledControlGroupContent`
  * `LabeledToolbarItemGroupContent`
  * `LazyHGrid`
  * `LazyHStack`
  * `LazyVGrid`
  * `LazyVStack`
  * `LinearGradient`
  * `Link`
  * `List`
  * `Menu`
  * `MenuButton`
  * `MenuStyleConfiguration.Content`
  * `MenuStyleConfiguration.Label`
  * `ModifiedContent`

Conforms when `Content` conforms to `DynamicViewContent` and `Modifier`
conforms to `ViewModifier`.

  * `MultiDatePicker`
  * `NavigationLink`
  * `NavigationSplitView`
  * `NavigationStack`
  * `NavigationView`
  * `OffsetShape`
  * `OutlineGroup`

Conforms when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, `Parent` conforms to `View`, `Leaf` conforms to `View`, and
`Subgroup` conforms to `View`.

  * `OutlineSubgroupChildren`
  * `PasteButton`
  * `Path`
  * `PhaseAnimator`
  * `Picker`
  * `PlaceholderContentView`
  * `PresentedWindowContent`
  * `PrimitiveButtonStyleConfiguration.Label`
  * `ProgressView`
  * `ProgressViewStyleConfiguration.CurrentValueLabel`
  * `ProgressViewStyleConfiguration.Label`
  * `RadialGradient`
  * `Rectangle`
  * `RenameButton`
  * `RotatedShape`
  * `RoundedRectangle`
  * `ScaledShape`
  * `ScrollView`
  * `ScrollViewReader`
  * `SearchUnavailableContent.Actions`
  * `SearchUnavailableContent.Description`
  * `SearchUnavailableContent.Label`
  * `Section`

Conforms when `Parent` conforms to `View`, `Content` conforms to `View`, and
`Footer` conforms to `View`.

  * `SecureField`
  * `SettingsLink`
  * `ShareLink`
  * `Slider`
  * `Spacer`
  * `Stepper`
  * `StrokeBorderShapeView`
  * `StrokeShapeView`
  * `SubscriptionView`
  * `TabView`
  * `Table`
  * `Text`
  * `TextEditor`
  * `TextField`
  * `TextFieldLink`
  * `TimelineView`

Conforms when `Schedule` conforms to `TimelineSchedule` and `Content` conforms
to `View`.

  * `Toggle`
  * `ToggleStyleConfiguration.Label`
  * `TransformedShape`
  * `TupleView`
  * `UnevenRoundedRectangle`
  * `VSplitView`
  * `VStack`
  * `ViewThatFits`
  * `ZStack`

## See Also

### Creating a view

Declaring a custom view

Define views and assemble them into a view hierarchy.

`struct ViewBuilder`

A custom parameter attribute that constructs views from closures.

Structure

# ViewBuilder

A custom parameter attribute that constructs views from closures.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @resultBuilder
    struct ViewBuilder

## Overview

You typically use `ViewBuilder` as a parameter attribute for child view-
producing closure parameters, allowing those closures to provide multiple
child views. For example, the following `contextMenu` function accepts a
closure that produces one or more views via the view builder.

Clients of this function can use multiple-statement closures to provide
several child views, as shown in the following example:

## Topics

### Building content

`static func buildBlock() -> EmptyView`

Builds an empty view from a block containing no statements.

`static func buildBlock<Content>(Content) -> Content`

Passes a single view written as a child view through unmodified.

`static func buildBlock<each Content>(repeat each Content) ->
TupleView<(repeat each Content)>`

`static func buildExpression<Content>(Content) -> Content`

Builds an expression within the builder.

### Conditionally building content

`static func buildEither<TrueContent, FalseContent>(first: TrueContent) ->
_ConditionalContent<TrueContent, FalseContent>`

Produces content for a conditional statement in a multi-statement closure when
the condition is true.

`static func buildEither<TrueContent, FalseContent>(second: FalseContent) ->
_ConditionalContent<TrueContent, FalseContent>`

Produces content for a conditional statement in a multi-statement closure when
the condition is false.

`static func buildIf<Content>(Content?) -> Content?`

Produces an optional view for conditional statements in multi-statement
closures that’s only visible when the condition evaluates to true.

`static func buildLimitedAvailability<Content>(Content) -> AnyView`

Processes view content for a conditional compiler-control statement that
performs an availability check.

## See Also

### Creating a view

Declaring a custom view

Define views and assemble them into a view hierarchy.

`protocol View`

A type that represents part of your app’s user interface and provides
modifiers that you use to configure views.

Article

# Configuring views

Adjust the characteristics of a view by applying view modifiers.

## Overview

In SwiftUI, you assemble views into a hierarchy that describes your app’s user
interface. To help you customize the appearance and behavior of your app’s
views, you use _view modifiers_. For example, you can use modifiers to:

  * Add accessibility features to a view.

  * Adjust a view’s styling, layout, and other appearance characteristics.

  * Respond to events, like copy and paste.

  * Conditionally present modal views, like popovers.

  * Configure supporting views, like toolbars.

Because view modifiers are Swift methods with behavior provided by the `View`
protocol, you can apply them to any type that conforms to the `View` protocol.
That includes built-in views like `Text`, `Image`, and `Button`, as well as
views that you define.

### Configure a view with a modifier

Like other Swift methods, a modifier operates on an instance — a view of some
kind in this case — and can optionally take input parameters. For example, you
can apply the `foregroundColor(_:)` modifier to set the color of a `Text`
view:

Modifiers return a view that wraps the original view and replaces it in the
view hierarchy. You can think of the two lines in the example above as
resolving to a single view that displays red text.

While the code above follows the rules of Swift, the code’s structure might be
unfamiliar for developers new to SwiftUI. SwiftUI uses a declarative approach,
where you declare and configure a view at the point in your code that
corresponds to the view’s position in the view hierarchy. For more
information, see Declaring a custom view.

### Chain modifiers to achieve complex effects

You commonly chain modifiers, each wrapping the result of the previous one, by
calling them one after the other. For example, you can wrap a text view in an
invisible box with a given width using the `frame(width:height:alignment:)`
modifier to influence its layout, and then use the `border(_:width:)` modifier
to draw an outline around that:

The order in which you apply modifiers matters. For example, the border that
results from the code above outlines the full width of the frame.

By specifying the frame modifier after the border modifier, SwiftUI applies
the border only to the text view, which never takes more space than it needs
to render its contents.

Wrapping that view in an invisible one with a fixed 100 point width affects
the layout of the composite view, but has no effect on the border.

### Configure child views

You can apply any view modifier defined by the `View` protocol to any concrete
view, even when the modifier doesn’t have an immediate effect on its target
view. The effects of a modifier propagate to child views that don’t explicitly
override the modifier.

For example, a `VStack` instance on its own acts only to vertically stack
other views — it doesn’t have any text to display. Therefore, applying a
`font(_:)` modifier to the stack has no effect on the stack. Yet the font
modifier does apply to any of the stack’s child views, some of which might
display text. You can, however, locally override the stack’s modifier by
adding another to a specific child view:

### Use view-specific modifiers

While many view types rely on standard view modifiers for customization and
control, some views do define modifiers that are specific to that view type.
You can’t use such a modifier on anything but the appropriate kind of view.
For example, `Text` defines the `bold()` modifier as a convenience for adding
a bold effect to the view’s text. While you can use `font(_:)` on any view
because it’s part of the `View` protocol, you can use `bold()` only on `Text`
views. As a result, you can’t use it on a container view:

You also can’t use it on a `Text` view after applying another general modifier
because general modifiers return an opaque type. For example, the return value
from the padding modifier isn’t `Text`, but rather an opaque result type that
can’t take a bold modifier:

Instead, apply the bold modifier directly to the `Text` view and then add the
padding:

## See Also

### Modifying a view

Reducing view modifier maintenance

Bundle view modifiers that you regularly reuse into a custom view modifier.

`func modifier<T>(T) -> ModifiedContent<Self, T>`

Applies a modifier to a view and returns a new view.

`protocol ViewModifier`

A modifier that you apply to a view or another view modifier, producing a
different version of the original value.

`struct EmptyModifier`

An empty, or identity, modifier, used during development to switch modifiers
at compile time.

`struct ModifiedContent`

A value with a modifier applied to it.

`protocol EnvironmentalModifier`

A modifier that must resolve to a concrete modifier in an environment before
use.

Article

# Reducing view modifier maintenance

Bundle view modifiers that you regularly reuse into a custom view modifier.

## Overview

To create consistent views, you might reuse the same view modifier or group of
modifiers repeatedly across your views. For example, you might apply the same
font and foreground color to many text instances throughout your app, so they
all match. Unfortunately, this can lead to maintenance challenges, because
even a small change in format, like a different font size, requires changes in
many different parts of your code.

To avoid this overhead, collect a set of modifiers into a single location
using an instance of the `ViewModifier` protocol. Then, extend the `View`
protocol with a method that uses your modifier, making it easy to use and
understand. Collecting the modifiers together provides a single location to
update when you want to change them.

### Create a custom view modifier

When you create your custom modifier, name it to reflect the purpose of the
collection. For example, if you repeatedly apply the `caption` font style and
a secondary color scheme to views to represent a secondary styling, collect
them together as `CaptionTextFormat`:

Apply your modifier using the `modifier(_:)` method. The following code
applies the above example to a `Text` instance:

### Extend the view protocol to provide fluent modifier access

To make your custom view modifier conveniently accessible, extend the `View`
protocol with a function that applies your modifier:

Apply the modifier to a text view by including this extension:

## See Also

### Modifying a view

Configuring views

Adjust the characteristics of a view by applying view modifiers.

`func modifier<T>(T) -> ModifiedContent<Self, T>`

Applies a modifier to a view and returns a new view.

`protocol ViewModifier`

A modifier that you apply to a view or another view modifier, producing a
different version of the original value.

`struct EmptyModifier`

An empty, or identity, modifier, used during development to switch modifiers
at compile time.

`struct ModifiedContent`

A value with a modifier applied to it.

`protocol EnvironmentalModifier`

A modifier that must resolve to a concrete modifier in an environment before
use.

Instance Method

# modifier(_:)

Applies a modifier to a view and returns a new view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func modifier<T>(_ modifier: T) -> ModifiedContent<Self, T>

##  Parameters

`modifier`

    

The modifier to apply to this view.

## Discussion

Use this modifier to combine a `View` and a `ViewModifier`, to create a new
view. For example, if you create a view modifier for a new kind of caption
with blue text surrounded by a rounded rectangle:

You can use `modifier(_:)` to extend `View` to create new modifier for
applying the `BorderedCaption` defined above:

Then you can apply the bordered caption to any view:

## See Also

### Modifying a view

Configuring views

Adjust the characteristics of a view by applying view modifiers.

Reducing view modifier maintenance

Bundle view modifiers that you regularly reuse into a custom view modifier.

`protocol ViewModifier`

A modifier that you apply to a view or another view modifier, producing a
different version of the original value.

`struct EmptyModifier`

An empty, or identity, modifier, used during development to switch modifiers
at compile time.

`struct ModifiedContent`

A value with a modifier applied to it.

`protocol EnvironmentalModifier`

A modifier that must resolve to a concrete modifier in an environment before
use.

Protocol

# ViewModifier

A modifier that you apply to a view or another view modifier, producing a
different version of the original value.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    protocol ViewModifier

## Overview

Adopt the `ViewModifier` protocol when you want to create a reusable modifier
that you can apply to any view. The example below combines several modifiers
to create a new modifier that you can use to create blue caption text
surrounded by a rounded rectangle:

You can apply `modifier(_:)` directly to a view, but a more common and
idiomatic approach uses `modifier(_:)` to define an extension to `View` itself
that incorporates the view modifier:

You can then apply the bordered caption to any view, similar to this:

## Topics

### Creating a view modifier

`func body(content: Self.Content) -> Self.Body`

Gets the current body of the caller.

**Required** Default implementation provided.

`associatedtype Body : View`

The type of view representing the body.

**Required**

` typealias Content`

The content view type passed to `body()`.

### Adding animations to a view

`func animation(Animation?) -> some ViewModifier`

Returns a new version of the modifier that will apply `animation` to all
animatable values within the modifier.

`func concat<T>(T) -> ModifiedContent<Self, T>`

Returns a new modifier that is the result of concatenating `self` with
`modifier`.

### Handling view taps and gestures

`func transaction((inout Transaction) -> Void) -> some ViewModifier`

Returns a new version of the modifier that will apply the transaction mutation
function `transform` to all transactions within the modifier.

## Relationships

### Inherited By

  * `AnimatableModifier`
  * `EnvironmentalModifier`
  * `GeometryEffect`

### Conforming Types

  * `AccessibilityAttachmentModifier`
  * `EmptyModifier`
  * `ModifiedContent`

Conforms when `Content` conforms to `ViewModifier` and `Modifier` conforms to
`ViewModifier`.

## See Also

### Modifying a view

Configuring views

Adjust the characteristics of a view by applying view modifiers.

Reducing view modifier maintenance

Bundle view modifiers that you regularly reuse into a custom view modifier.

`func modifier<T>(T) -> ModifiedContent<Self, T>`

Applies a modifier to a view and returns a new view.

`struct EmptyModifier`

An empty, or identity, modifier, used during development to switch modifiers
at compile time.

`struct ModifiedContent`

A value with a modifier applied to it.

Available when `Content` conforms to `ViewModifier` and `Modifier` conforms to
`ViewModifier`.

`protocol EnvironmentalModifier`

A modifier that must resolve to a concrete modifier in an environment before
use.

Structure

# EmptyModifier

An empty, or identity, modifier, used during development to switch modifiers
at compile time.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct EmptyModifier

## Overview

Use the empty modifier to switch modifiers at compile time during development.
In the example below, in a debug build the `Text` view inside `ContentView`
has a yellow background and a red border. A non-debug build reflects the
default system, or container supplied appearance.

## Topics

### Creating an empty modifier

`init()`

### Getting the identity modifier

`static let identity: EmptyModifier`

## Relationships

### Conforms To

  * `Sendable`
  * `ViewModifier`

## See Also

### Modifying a view

Configuring views

Adjust the characteristics of a view by applying view modifiers.

Reducing view modifier maintenance

Bundle view modifiers that you regularly reuse into a custom view modifier.

`func modifier<T>(T) -> ModifiedContent<Self, T>`

Applies a modifier to a view and returns a new view.

`protocol ViewModifier`

A modifier that you apply to a view or another view modifier, producing a
different version of the original value.

`struct ModifiedContent`

A value with a modifier applied to it.

`protocol EnvironmentalModifier`

A modifier that must resolve to a concrete modifier in an environment before
use.

Structure

# ModifiedContent

A value with a modifier applied to it.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct ModifiedContent<Content, Modifier>

## Topics

### Creating a modified content view

`init(content: Content, modifier: Modifier)`

A structure that the defines the content and modifier needed to produce a new
view or view modifier.

`var content: Content`

The content that the modifier transforms into a new view or new view modifier.

`var modifier: Modifier`

The view modifier.

### Instance Methods

`func accessibility(activationPoint: CGPoint) -> ModifiedContent<Content,
Modifier>`

Specifies the point where activations occur in the view.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

Deprecated

`func accessibility(activationPoint: UnitPoint) -> ModifiedContent<Content,
Modifier>`

Specifies the unit point where activations occur in the view.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

Deprecated

`func accessibility(addTraits: AccessibilityTraits) ->
ModifiedContent<Content, Modifier>`

Adds the given traits to the view.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

Deprecated

`func accessibility(hidden: Bool) -> ModifiedContent<Content, Modifier>`

Specifies whether to hide this view from system accessibility features.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

Deprecated

`func accessibility(hint: Text) -> ModifiedContent<Content, Modifier>`

Communicates to the user what happens after performing the view’s action.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

Deprecated

`func accessibility(identifier: String) -> ModifiedContent<Content, Modifier>`

Uses the specified string to identify the view.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

Deprecated

`func accessibility(inputLabels: [Text]) -> ModifiedContent<Content,
Modifier>`

Sets alternate input labels with which users identify a view.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

Deprecated

`func accessibility(label: Text) -> ModifiedContent<Content, Modifier>`

Adds a label to the view that describes its contents.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

Deprecated

`func accessibility(removeTraits: AccessibilityTraits) ->
ModifiedContent<Content, Modifier>`

Removes the given traits from this view.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

Deprecated

`func accessibility(selectionIdentifier: AnyHashable) ->
ModifiedContent<Content, Modifier>`

Sets a selection identifier for this view’s accessibility element.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

Deprecated

`func accessibility(sortPriority: Double) -> ModifiedContent<Content,
Modifier>`

Sets the sort priority order for this view’s accessibility element, relative
to other elements at the same level.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

Deprecated

`func accessibility(value: Text) -> ModifiedContent<Content, Modifier>`

Adds a textual description of the value that the view contains.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

Deprecated

`func accessibilityAction(AccessibilityActionKind, () -> Void) ->
ModifiedContent<Content, Modifier>`

Adds an accessibility action to the view. Actions allow assistive
technologies, such as the VoiceOver, to interact with the view by invoking the
action.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

`func accessibilityAction(named: Text, () -> Void) -> ModifiedContent<Content,
Modifier>`

Adds an accessibility action to the view. Actions allow assistive
technologies, such as the VoiceOver, to interact with the view by invoking the
action.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

`func accessibilityAction(named: LocalizedStringKey, () -> Void) ->
ModifiedContent<Content, Modifier>`

Adds an accessibility action to the view. Actions allow assistive
technologies, such as the VoiceOver, to interact with the view by invoking the
action.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

`func accessibilityAction<S>(named: S, () -> Void) -> ModifiedContent<Content,
Modifier>`

Adds an accessibility action to the view. Actions allow assistive
technologies, such as the VoiceOver, to interact with the view by invoking the
action.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

`func accessibilityActivationPoint(CGPoint) -> ModifiedContent<Content,
Modifier>`

The activation point for an element is the location assistive technologies use
to initiate gestures.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

`func accessibilityActivationPoint(UnitPoint) -> ModifiedContent<Content,
Modifier>`

The activation point for an element is the location assistive technologies use
to initiate gestures.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

`func accessibilityAddTraits(AccessibilityTraits) -> ModifiedContent<Content,
Modifier>`

Adds the given traits to the view.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

`func accessibilityAdjustableAction((AccessibilityAdjustmentDirection) ->
Void) -> ModifiedContent<Content, Modifier>`

Adds an accessibility adjustable action to the view. Actions allow assistive
technologies, such as the VoiceOver, to interact with the view by invoking the
action.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

`func accessibilityCustomContent(Text, Text, importance:
AXCustomContent.Importance) -> ModifiedContent<Content, Modifier>`

Add additional accessibility information to the view.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

`func accessibilityCustomContent(LocalizedStringKey, Text, importance:
AXCustomContent.Importance) -> ModifiedContent<Content, Modifier>`

Add additional accessibility information to the view.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

`func accessibilityCustomContent<V>(AccessibilityCustomContentKey, V,
importance: AXCustomContent.Importance) -> ModifiedContent<Content, Modifier>`

Add additional accessibility information to the view.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

`func accessibilityCustomContent(AccessibilityCustomContentKey,
LocalizedStringKey, importance: AXCustomContent.Importance) ->
ModifiedContent<Content, Modifier>`

Add additional accessibility information to the view.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

`func accessibilityCustomContent(AccessibilityCustomContentKey, Text?,
importance: AXCustomContent.Importance) -> ModifiedContent<Content, Modifier>`

Add additional accessibility information to the view.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

`func accessibilityCustomContent(LocalizedStringKey, LocalizedStringKey,
importance: AXCustomContent.Importance) -> ModifiedContent<Content, Modifier>`

Add additional accessibility information to the view.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

`func accessibilityCustomContent<V>(LocalizedStringKey, V, importance:
AXCustomContent.Importance) -> ModifiedContent<Content, Modifier>`

Add additional accessibility information to the view.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

`func accessibilityDirectTouch(Bool, options: AccessibilityDirectTouchOptions)
-> ModifiedContent<Content, Modifier>`

Explicitly set whether this accessibility element is a direct touch area.
Direct touch areas passthrough touch events to the app rather than being
handled through an assistive technology, such as VoiceOver. The modifier
accepts an optional `AccessibilityDirectTouchOptions` option set to customize
the functionality of the direct touch area.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

`func accessibilityHeading(AccessibilityHeadingLevel) ->
ModifiedContent<Content, Modifier>`

Set the level of this heading.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

`func accessibilityHidden(Bool) -> ModifiedContent<Content, Modifier>`

Specifies whether to hide this view from system accessibility features.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

`func accessibilityHint(LocalizedStringKey) -> ModifiedContent<Content,
Modifier>`

Communicates to the user what happens after performing the view’s action.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

`func accessibilityHint(Text) -> ModifiedContent<Content, Modifier>`

Communicates to the user what happens after performing the view’s action.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

`func accessibilityHint<S>(S) -> ModifiedContent<Content, Modifier>`

Communicates to the user what happens after performing the view’s action.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

`func accessibilityIdentifier(String) -> ModifiedContent<Content, Modifier>`

Uses the string you specify to identify the view.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

`func accessibilityInputLabels([LocalizedStringKey]) ->
ModifiedContent<Content, Modifier>`

Sets alternate input labels with which users identify a view.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

`func accessibilityInputLabels([Text]) -> ModifiedContent<Content, Modifier>`

Sets alternate input labels with which users identify a view.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

`func accessibilityInputLabels<S>([S]) -> ModifiedContent<Content, Modifier>`

Sets alternate input labels with which users identify a view.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

`func accessibilityLabel<S>(S) -> ModifiedContent<Content, Modifier>`

Adds a label to the view that describes its contents.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

`func accessibilityLabel(Text) -> ModifiedContent<Content, Modifier>`

Adds a label to the view that describes its contents.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

`func accessibilityLabel(LocalizedStringKey) -> ModifiedContent<Content,
Modifier>`

Adds a label to the view that describes its contents.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

`func accessibilityRemoveTraits(AccessibilityTraits) ->
ModifiedContent<Content, Modifier>`

Removes the given traits from this view.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

`func accessibilityRespondsToUserInteraction(Bool) -> ModifiedContent<Content,
Modifier>`

Explicitly set whether this Accessibility element responds to user interaction
and would thus be interacted with by technologies such as Switch Control,
Voice Control or Full Keyboard Access.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

`func accessibilityScrollAction((Edge) -> Void) -> ModifiedContent<Content,
Modifier>`

Adds an accessibility scroll action to the view. Actions allow assistive
technologies, such as the VoiceOver, to interact with the view by invoking the
action.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

`func accessibilitySortPriority(Double) -> ModifiedContent<Content, Modifier>`

Sets the sort priority order for this view’s accessibility element, relative
to other elements at the same level.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

`func accessibilityTextContentType(AccessibilityTextContentType) ->
ModifiedContent<Content, Modifier>`

Sets an accessibility text content type.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

`func accessibilityValue(Text) -> ModifiedContent<Content, Modifier>`

Adds a textual description of the value that the view contains.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

`func accessibilityValue(LocalizedStringKey) -> ModifiedContent<Content,
Modifier>`

Adds a textual description of the value that the view contains.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

`func accessibilityValue<S>(S) -> ModifiedContent<Content, Modifier>`

Adds a textual description of the value that the view contains.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

`func accessibilityZoomAction((AccessibilityZoomGestureAction) -> Void) ->
ModifiedContent<Content, Modifier>`

Adds an accessibility zoom action to the view. Actions allow assistive
technologies, such as VoiceOver, to interact with the view by invoking the
action.

Available when `Modifier` is `AccessibilityAttachmentModifier`.

### Default Implementations

API Reference

DynamicMapContent Implementations

API Reference

MapContent Implementations

## Relationships

### Conforms To

  * `DynamicMapContent`
  * `DynamicTableRowContent`

Conforms when `Content` conforms to `DynamicTableRowContent` and `Modifier`
conforms to `_TableRowContentModifier`.

  * `DynamicViewContent`

Conforms when `Content` conforms to `DynamicViewContent` and `Modifier`
conforms to `ViewModifier`.

  * `Equatable`
  * `MapContent`
  * `Scene`

Conforms when `Content` conforms to `Scene` and `Modifier` conforms to
`_SceneModifier`.

  * `TableRowContent`

Conforms when `Content` conforms to `TableRowContent` and `Modifier` conforms
to `_TableRowContentModifier`.

  * `View`

Conforms when `Content` conforms to `DynamicViewContent` and `Modifier`
conforms to `ViewModifier`.

  * `ViewModifier`

Conforms when `Content` conforms to `ViewModifier` and `Modifier` conforms to
`ViewModifier`.

## See Also

### Modifying a view

Configuring views

Adjust the characteristics of a view by applying view modifiers.

Reducing view modifier maintenance

Bundle view modifiers that you regularly reuse into a custom view modifier.

`func modifier<T>(T) -> ModifiedContent<Self, T>`

Applies a modifier to a view and returns a new view.

`protocol ViewModifier`

A modifier that you apply to a view or another view modifier, producing a
different version of the original value.

Available when `Content` conforms to `ViewModifier` and `Modifier` conforms to
`ViewModifier`.

`struct EmptyModifier`

An empty, or identity, modifier, used during development to switch modifiers
at compile time.

`protocol EnvironmentalModifier`

A modifier that must resolve to a concrete modifier in an environment before
use.

Protocol

# EnvironmentalModifier

A modifier that must resolve to a concrete modifier in an environment before
use.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    protocol EnvironmentalModifier : ViewModifier where Self.Body == Never

## Topics

### Resolving a modifier

`func resolve(in: EnvironmentValues) -> Self.ResolvedModifier`

Resolve to a concrete modifier in the given `environment`.

**Required**

` associatedtype ResolvedModifier : ViewModifier`

The type of modifier to use after being resolved.

**Required**

## Relationships

### Inherits From

  * `ViewModifier`

## See Also

### Modifying a view

Configuring views

Adjust the characteristics of a view by applying view modifiers.

Reducing view modifier maintenance

Bundle view modifiers that you regularly reuse into a custom view modifier.

`func modifier<T>(T) -> ModifiedContent<Self, T>`

Applies a modifier to a view and returns a new view.

`protocol ViewModifier`

A modifier that you apply to a view or another view modifier, producing a
different version of the original value.

`struct EmptyModifier`

An empty, or identity, modifier, used during development to switch modifiers
at compile time.

`struct ModifiedContent`

A value with a modifier applied to it.

Instance Method

# onAppear(perform:)

Adds an action to perform before this view appears.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func onAppear(perform action: (() -> Void)? = nil) -> some View
    

##  Parameters

`action`

    

The action to perform. If `action` is `nil`, the call has no effect.

## Return Value

A view that triggers `action` before it appears.

## Discussion

The exact moment that SwiftUI calls this method depends on the specific view
type that you apply it to, but the `action` closure completes before the first
rendered frame appears.

## See Also

### Responding to view life cycle updates

`func onDisappear(perform: (() -> Void)?) -> some View`

Adds an action to perform after this view disappears.

`func task(priority: TaskPriority, () async -> Void) -> some View`

Adds an asynchronous task to perform before this view appears.

`func task<T>(id: T, priority: TaskPriority, () async -> Void) -> some View`

Adds a task to perform before this view appears or when a specified value
changes.

Instance Method

# onDisappear(perform:)

Adds an action to perform after this view disappears.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func onDisappear(perform action: (() -> Void)? = nil) -> some View
    

##  Parameters

`action`

    

The action to perform. If `action` is `nil`, the call has no effect.

## Return Value

A view that triggers `action` after it disappears.

## Discussion

The exact moment that SwiftUI calls this method depends on the specific view
type that you apply it to, but the `action` closure doesn’t execute until the
view disappears from the interface.

## See Also

### Responding to view life cycle updates

`func onAppear(perform: (() -> Void)?) -> some View`

Adds an action to perform before this view appears.

`func task(priority: TaskPriority, () async -> Void) -> some View`

Adds an asynchronous task to perform before this view appears.

`func task<T>(id: T, priority: TaskPriority, () async -> Void) -> some View`

Adds a task to perform before this view appears or when a specified value
changes.

Instance Method

# task(priority:_:)

Adds an asynchronous task to perform before this view appears.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func task(
        priority: TaskPriority = .userInitiated,
        _ action: @escaping () async -> Void
    ) -> some View
    

##  Parameters

`priority`

    

The task priority to use when creating the asynchronous task. The default
priority is `userInitiated`.

`action`

    

A closure that SwiftUI calls as an asynchronous task before the view appears.
SwiftUI will automatically cancel the task at some point after the view
disappears before the action completes.

## Return Value

A view that runs the specified action asynchronously before the view appears.

## Discussion

Use this modifier to perform an asynchronous task with a lifetime that matches
that of the modified view. If the task doesn’t finish before SwiftUI removes
the view or the view changes identity, SwiftUI cancels the task.

Use the `await` keyword inside the task to wait for an asynchronous call to
complete, or to wait on the values of an `AsyncSequence` instance. For
example, you can modify a `Text` view to start a task that loads content from
a remote resource:

This example uses the `lines` method to get the content stored at the
specified `URL` as an asynchronous sequence of strings. When each new line
arrives, the body of the `for`-`await`-`in` loop stores the line in an array
of strings and updates the content of the text view to report the latest line
count.

## See Also

### Responding to view life cycle updates

`func onAppear(perform: (() -> Void)?) -> some View`

Adds an action to perform before this view appears.

`func onDisappear(perform: (() -> Void)?) -> some View`

Adds an action to perform after this view disappears.

`func task<T>(id: T, priority: TaskPriority, () async -> Void) -> some View`

Adds a task to perform before this view appears or when a specified value
changes.

Instance Method

# task(id:priority:_:)

Adds a task to perform before this view appears or when a specified value
changes.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func task<T>(
        id value: T,
        priority: TaskPriority = .userInitiated,
        _ action: @escaping () async -> Void
    ) -> some View where T : Equatable
    

##  Parameters

`id`

    

The value to observe for changes. The value must conform to the `Equatable`
protocol.

`priority`

    

The task priority to use when creating the asynchronous task. The default
priority is `userInitiated`.

`action`

    

A closure that SwiftUI calls as an asynchronous task before the view appears.
SwiftUI can automatically cancel the task after the view disappears before the
action completes. If the `id` value changes, SwiftUI cancels and restarts the
task.

## Return Value

A view that runs the specified action asynchronously before the view appears,
or restarts the task when the `id` value changes.

## Discussion

This method behaves like `task(priority:_:)`, except that it also cancels and
recreates the task when a specified value changes. To detect a change, the
modifier tests whether a new value for the `id` parameter equals the previous
value. For this to work, the value’s type must conform to the `Equatable`
protocol.

For example, if you define an equatable `Server` type that posts custom
notifications whenever its state changes — for example, from _signed out_ to
_signed in_ — you can use the task modifier to update the contents of a `Text`
view to reflect the state of the currently selected server:

This example uses the `notifications(named:object:)` method to create an
asynchronous sequence of notifications, given by an `AsyncSequence` instance.
The example then maps the notification sequence to a sequence of strings that
correspond to values stored with each notification.

Elsewhere, the server defines a custom `didUpdateStatus` notification:

Whenever the server status changes, like after the user signs in, the server
posts a notification of this custom type:

The task attached to the `Text` view gets and displays the status value from
the notification’s user information dictionary. When the user chooses a
different server, SwiftUI cancels the task and creates a new one, which then
waits for notifications from the new server.

## See Also

### Responding to view life cycle updates

`func onAppear(perform: (() -> Void)?) -> some View`

Adds an action to perform before this view appears.

`func onDisappear(perform: (() -> Void)?) -> some View`

Adds an action to perform after this view disappears.

`func task(priority: TaskPriority, () async -> Void) -> some View`

Adds an asynchronous task to perform before this view appears.

Instance Method

# id(_:)

Binds a view’s identity to the given proxy value.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func id<ID>(_ id: ID) -> some View where ID : Hashable
    

## Discussion

When the proxy value specified by the `id` parameter changes, the identity of
the view — for example, its state — is reset.

## See Also

### Managing the view hierarchy

`func tag<V>(V) -> some View`

Sets the unique tag value of this view.

`func equatable() -> EquatableView<Self>`

Prevents the view from updating its child view when its new value is the same
as its old value.

Available when `Self` conforms to `Equatable`.

Instance Method

# tag(_:)

Sets the unique tag value of this view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func tag<V>(_ tag: V) -> some View where V : Hashable
    

##  Parameters

`tag`

    

A `Hashable` value to use as the view’s tag.

## Return Value

A view with the specified tag set.

## Discussion

Use this modifier to differentiate among certain selectable views, like the
possible values of a `Picker` or the tabs of a `TabView`. Tag values can be of
any type that conforms to the `Hashable` protocol.

In the example below, the `ForEach` loop in the `Picker` view builder iterates
over the `Flavor` enumeration. It extracts the string value of each
enumeration element for use in constructing the row label, and uses the
enumeration value, cast as an optional, as input to the `tag(_:)` modifier.
The `Picker` requires the tags to have a type that exactly matches the
selection type, which in this case is an optional `Flavor`.

If you change `selectedFlavor` to be non-optional, you need to remove the
`Optional` cast from the tag input to match.

A `ForEach` automatically applies a default tag to each enumerated view using
the `id` parameter of the corresponding element. If the element’s `id`
parameter and the picker’s `selection` input have exactly the same type, you
can omit the explicit tag modifier. To see examples that don’t require an
explicit tag, see `Picker`.

## See Also

### Managing the view hierarchy

`func id<ID>(ID) -> some View`

Binds a view’s identity to the given proxy value.

`func equatable() -> EquatableView<Self>`

Prevents the view from updating its child view when its new value is the same
as its old value.

Available when `Self` conforms to `Equatable`.

Instance Method

# equatable()

Prevents the view from updating its child view when its new value is the same
as its old value.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func equatable() -> EquatableView<Self>

Available when `Self` conforms to `Equatable`.

## See Also

### Managing the view hierarchy

`func id<ID>(ID) -> some View`

Binds a view’s identity to the given proxy value.

`func tag<V>(V) -> some View`

Sets the unique tag value of this view.

Structure

# AnyView

A type-erased view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct AnyView

## Overview

An `AnyView` allows changing the type of view used in a given view hierarchy.
Whenever the type of view used with an `AnyView` changes, the old hierarchy is
destroyed and a new hierarchy is created for the new type.

## Topics

### Creating a view

`init<V>(V)`

Create an instance that type-erases `view`.

`init<V>(erasing: V)`

## Relationships

### Conforms To

  * `View`

## See Also

### Supporting view types

`struct EmptyView`

A view that doesn’t contain any content.

`struct EquatableView`

A view type that compares itself against its previous value and prevents its
child updating if its new value is the same as its old value.

`struct SubscriptionView`

A view that subscribes to a publisher with an action.

`struct TupleView`

A View created from a swift tuple of View values.

Structure

# EmptyView

A view that doesn’t contain any content.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct EmptyView

## Overview

You will rarely, if ever, need to create an `EmptyView` directly. Instead,
`EmptyView` represents the absence of a view.

SwiftUI uses `EmptyView` in situations where a SwiftUI view type defines one
or more child views with generic parameters, and allows the child views to be
absent. When absent, the child view’s type in the generic type parameter is
`EmptyView`.

The following example creates an indeterminate `ProgressView` without a label.
The `ProgressView` type declares two generic parameters, `Label` and
`CurrentValueLabel`, for the types used by its subviews. When both subviews
are absent, like they are here, the resulting type is `ProgressView<EmptyView,
EmptyView>`, as indicated by the example’s output:

## Topics

### Creating an empty view

`init()`

Creates an empty view.

## Relationships

### Conforms To

  * `Sendable`
  * `View`

## See Also

### Supporting view types

`struct AnyView`

A type-erased view.

`struct EquatableView`

A view type that compares itself against its previous value and prevents its
child updating if its new value is the same as its old value.

`struct SubscriptionView`

A view that subscribes to a publisher with an action.

`struct TupleView`

A View created from a swift tuple of View values.

Structure

# EquatableView

A view type that compares itself against its previous value and prevents its
child updating if its new value is the same as its old value.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct EquatableView<Content> where Content : Equatable, Content : View

## Topics

### Creating an equatable view

`init(content: Content)`

`var content: Content`

## Relationships

### Conforms To

  * `View`

## See Also

### Supporting view types

`struct AnyView`

A type-erased view.

`struct EmptyView`

A view that doesn’t contain any content.

`struct SubscriptionView`

A view that subscribes to a publisher with an action.

`struct TupleView`

A View created from a swift tuple of View values.

Structure

# SubscriptionView

A view that subscribes to a publisher with an action.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct SubscriptionView<PublisherType, Content> where PublisherType : Publisher, Content : View, PublisherType.Failure == Never

## Topics

### Creating a subscription view

`init(content: Content, publisher: PublisherType, action:
(PublisherType.Output) -> Void)`

### Managing the subscription

`var publisher: PublisherType`

The `Publisher` that is being subscribed.

`var action: (PublisherType.Output) -> Void`

The `Action` executed when `publisher` emits an event.

`var content: Content`

The content view.

## Relationships

### Conforms To

  * `View`

## See Also

### Supporting view types

`struct AnyView`

A type-erased view.

`struct EmptyView`

A view that doesn’t contain any content.

`struct EquatableView`

A view type that compares itself against its previous value and prevents its
child updating if its new value is the same as its old value.

`struct TupleView`

A View created from a swift tuple of View values.

Structure

# TupleView

A View created from a swift tuple of View values.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct TupleView<T>

## Topics

### Creating a tuple view

`init(T)`

`var value: T`

## Relationships

### Conforms To

  * `View`

## See Also

### Supporting view types

`struct AnyView`

A type-erased view.

`struct EmptyView`

A view that doesn’t contain any content.

`struct EquatableView`

A view type that compares itself against its previous value and prevents its
child updating if its new value is the same as its old value.

`struct SubscriptionView`

A view that subscribes to a publisher with an action.



# ViewThatFits

Initializer

# init(in:content:)

Produces a view constrained in the given axes from one of several alternatives
provided by a view builder.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init(
        in axes: Axis.Set = [.horizontal, .vertical],
        @ViewBuilder content: () -> Content
    )

##  Parameters

`axes`

    

A set of axes to constrain children to. The set may contain `Axis.horizontal`,
`Axis.vertical`, or both of these. `ViewThatFits` chooses the first child
whose size fits within the proposed size on these axes. If `axes` is an empty
set, `ViewThatFits` uses the first child view. By default, `ViewThatFits` uses
both axes.

`content`

    

A view builder that provides the child views for this container, in order of
preference. The builder chooses the first child view that fits within the
proposed width, height, or both, as defined by `axes`.



# ViewSpacing

Initializer

# init()

Initializes an instance with default spacing values.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init()

## Discussion

Use this initializer to create a spacing preferences instance with default
values. Then use `formUnion(_:edges:)` to combine preferences from other views
with the new instance. You typically do this in a custom layout’s
implementation of the `spacing(subviews:cache:)` method.

## See Also

### Creating spacing instances

`static let zero: ViewSpacing`

A view spacing instance that contains zero on all edges.

Type Property

# zero

A view spacing instance that contains zero on all edges.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static let zero: ViewSpacing

## Discussion

You typically only use this value for an empty view.

## See Also

### Creating spacing instances

`init()`

Initializes an instance with default spacing values.

Instance Method

# distance(to:along:)

Gets the preferred spacing distance along the specified axis to the view that
returns a specified spacing preference.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func distance(
        to next: ViewSpacing,
        along axis: Axis
    ) -> CGFloat

##  Parameters

`next`

    

The spacing preferences instance of the adjacent view.

`axis`

    

The axis that the two views align on.

## Return Value

A floating point value that represents the smallest distance in points between
two views that satisfies the spacing preferences of both this view and the
adjacent views on their shared edge.

## Discussion

Call this method from your implementation of `Layout` protocol methods if you
need to measure the default spacing between two views in a custom layout. Call
the method on the first view’s preferences instance, and provide the second
view’s preferences instance as input.

For example, consider two views that appear in a custom horizontal stack. The
following distance call gets the preferred spacing between these views, where
`spacing1` contains the preferences of a first view, and `spacing2` contains
the preferences of a second view:

The method first determines, based on the axis and the ordering, that the
views abut on the trailing edge of the first view and the leading edge of the
second. It then gets the spacing preferences for the corresponding edges of
each view, and returns the greater of the two values. This results in the
smallest value that provides enough space to satisfy the preferences of both
views.

Note

This method returns the default spacing between views, but a layout can choose
to ignore the value and use custom spacing instead.

Instance Method

# formUnion(_:edges:)

Merges the spacing preferences of another spacing instance with this instance
for a specified set of edges.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    mutating func formUnion(
        _ other: ViewSpacing,
        edges: Edge.Set = .all
    )

##  Parameters

`other`

    

Another spacing preferences instances to merge with this one.

`edges`

    

The edges to merge. Edges that you don’t specify are unchanged after the
method completes.

## Discussion

When you merge another spacing preference instance with this one, this
instance ends up with the greater of its original value or the other
instance’s value for each of the specified edges. You can call the method
repeatedly with each value in a collection to merge a collection of
preferences. The result has the smallest preferences on each edge that meets
the largest requirements of all the inputs for that edge.

If you want to merge preferences without modifying the original instance, use
`union(_:edges:)` instead.

## See Also

### Merging spacing instances

`func union(ViewSpacing, edges: Edge.Set) -> ViewSpacing`

Gets a new value that merges the spacing preferences of another spacing
instance with this instance for a specified set of edges.

Instance Method

# union(_:edges:)

Gets a new value that merges the spacing preferences of another spacing
instance with this instance for a specified set of edges.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func union(
        _ other: ViewSpacing,
        edges: Edge.Set = .all
    ) -> ViewSpacing

##  Parameters

`other`

    

Another spacing preferences instance to merge with this one.

`edges`

    

The edges to merge. Edges that you don’t specify are unchanged after the
method completes.

## Return Value

A new view spacing preferences instance with the merged values.

## Discussion

This method behaves like `formUnion(_:edges:)`, except that it creates a copy
of the original spacing preferences instance before merging, leaving the
original instance unmodified.

## See Also

### Merging spacing instances

`func formUnion(ViewSpacing, edges: Edge.Set)`

Merges the spacing preferences of another spacing instance with this instance
for a specified set of edges.



# VectorArithmetic

Instance Property

# magnitudeSquared

Returns the dot-product of this vector arithmetic instance with itself.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var magnitudeSquared: Double { get }

**Required**

## See Also

### Manipulating values

`func scale(by: Double)`

Multiplies each component of this value by the given value.

**Required** Default implementation provided.

`func scaled(by: Double) -> Self`

Returns a value with each component of this value multiplied by the given
value.

`func interpolate(towards: Self, amount: Double)`

Interpolates this value with `other` by the specified `amount`.

`func interpolated(towards: Self, amount: Double) -> Self`

Returns this value interpolated with `other` by the specified `amount`.

Instance Method

# scale(by:)

Multiplies each component of this value by the given value.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    mutating func scale(by rhs: Double)

**Required** Default implementation provided.

## Default Implementations

### VectorArithmetic Implementations

`func scale(by: Double)`

Multiplies each component of this value by the given value.

Available when `Self` conforms to `Scalable3D`.

## See Also

### Manipulating values

`var magnitudeSquared: Double`

Returns the dot-product of this vector arithmetic instance with itself.

**Required**

` func scaled(by: Double) -> Self`

Returns a value with each component of this value multiplied by the given
value.

`func interpolate(towards: Self, amount: Double)`

Interpolates this value with `other` by the specified `amount`.

`func interpolated(towards: Self, amount: Double) -> Self`

Returns this value interpolated with `other` by the specified `amount`.

Instance Method

# scaled(by:)

Returns a value with each component of this value multiplied by the given
value.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func scaled(by rhs: Double) -> Self

## See Also

### Manipulating values

`var magnitudeSquared: Double`

Returns the dot-product of this vector arithmetic instance with itself.

**Required**

` func scale(by: Double)`

Multiplies each component of this value by the given value.

**Required** Default implementation provided.

`func interpolate(towards: Self, amount: Double)`

Interpolates this value with `other` by the specified `amount`.

`func interpolated(towards: Self, amount: Double) -> Self`

Returns this value interpolated with `other` by the specified `amount`.

Instance Method

# interpolate(towards:amount:)

Interpolates this value with `other` by the specified `amount`.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    mutating func interpolate(
        towards other: Self,
        amount: Double
    )

## Discussion

This is equivalent to `self = self + (other - self) * amount`.

## See Also

### Manipulating values

`var magnitudeSquared: Double`

Returns the dot-product of this vector arithmetic instance with itself.

**Required**

` func scale(by: Double)`

Multiplies each component of this value by the given value.

**Required** Default implementation provided.

`func scaled(by: Double) -> Self`

Returns a value with each component of this value multiplied by the given
value.

`func interpolated(towards: Self, amount: Double) -> Self`

Returns this value interpolated with `other` by the specified `amount`.

Instance Method

# interpolated(towards:amount:)

Returns this value interpolated with `other` by the specified `amount`.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func interpolated(
        towards other: Self,
        amount: Double
    ) -> Self

## Discussion

This result is equivalent to `self + (other - self) * amount`.

## See Also

### Manipulating values

`var magnitudeSquared: Double`

Returns the dot-product of this vector arithmetic instance with itself.

**Required**

` func scale(by: Double)`

Multiplies each component of this value by the given value.

**Required** Default implementation provided.

`func scaled(by: Double) -> Self`

Returns a value with each component of this value multiplied by the given
value.

`func interpolate(towards: Self, amount: Double)`

Interpolates this value with `other` by the specified `amount`.



# View styles

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



# ViewAlignedScrollTargetBehavior.LimitBehavior

Type Property

# automatic

The automatic limit behavior.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static var automatic: ViewAlignedScrollTargetBehavior.LimitBehavior { get }

## Discussion

By default, the behavior will be limited in compact horizontal size classes
and will not be limited otherwise.

## See Also

### Getting the limit behavior

`static var always: ViewAlignedScrollTargetBehavior.LimitBehavior`

The always limit behavior.

`static var never: ViewAlignedScrollTargetBehavior.LimitBehavior`

The never limit behavior.

Type Property

# always

The always limit behavior.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static var always: ViewAlignedScrollTargetBehavior.LimitBehavior { get }

## Discussion

Always limit the amount of views that can be scrolled.

## See Also

### Getting the limit behavior

`static var automatic: ViewAlignedScrollTargetBehavior.LimitBehavior`

The automatic limit behavior.

`static var never: ViewAlignedScrollTargetBehavior.LimitBehavior`

The never limit behavior.

Type Property

# never

The never limit behavior.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static var never: ViewAlignedScrollTargetBehavior.LimitBehavior { get }

## Discussion

Never limit the amount of views that can be scrolled.

## See Also

### Getting the limit behavior

`static var automatic: ViewAlignedScrollTargetBehavior.LimitBehavior`

The automatic limit behavior.

`static var always: ViewAlignedScrollTargetBehavior.LimitBehavior`

The always limit behavior.



# View configuration

Instance Method

# opacity(_:)

Sets the transparency of this view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func opacity(_ opacity: Double) -> some View
    

##  Parameters

`opacity`

    

A value between 0 (fully transparent) and 1 (fully opaque).

## Return Value

A view that sets the transparency of this view.

## Discussion

Apply opacity to reveal views that are behind another view or to de-emphasize
a view.

When applying the `opacity(_:)` modifier to a view that has already had its
opacity transformed, the modifier multiplies the effect of the underlying
opacity transformation.

The example below shows yellow and red rectangles configured to overlap. The
top yellow rectangle has its opacity set to 50%, allowing the occluded portion
of the bottom rectangle to be visible:

## See Also

### Hiding views

`func hidden() -> some View`

Hides this view unconditionally.

Instance Method

# hidden()

Hides this view unconditionally.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func hidden() -> some View
    

## Return Value

A hidden view.

## Discussion

Hidden views are invisible and can’t receive or respond to interactions.
However, they do remain in the view hierarchy and affect layout. Use this
modifier if you want to include a view for layout purposes, but don’t want it
to display.

The third circle takes up space, because it’s still present, but SwiftUI
doesn’t draw it onscreen.

If you want to conditionally include a view in the view hierarchy, use an `if`
statement instead:

Depending on the current value of the `isHidden` state variable in the example
above, controlled by the `Toggle` instance, SwiftUI draws the circle or
completely omits it from the layout.

## See Also

### Hiding views

`func opacity(Double) -> some View`

Sets the transparency of this view.

Instance Method

# labelsHidden()

Hides the labels of any controls contained within this view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func labelsHidden() -> some View
    

## Discussion

Use this modifier when you want to omit a label from one or more controls in
your user interface. For example, the first `Toggle` in the following example
hides its label:

The `VStack` in the example above centers the first toggle’s control element
in the available space, while it centers the second toggle’s combined label
and control element:

Always provide a label for controls, even when you hide the label, because
SwiftUI uses labels for other purposes, including accessibility.

Note

This modifier doesn’t work for all labels. It applies to labels that are
separate from the rest of the control’s interface, like they are for `Toggle`,
but not to controls like a bordered button where the label is inside the
button’s border.

## See Also

### Hiding system elements

`func menuIndicator(Visibility) -> some View`

Sets the menu indicator visibility for controls within this view.

`func statusBarHidden(Bool) -> some View`

Sets the visibility of the status bar.

`func persistentSystemOverlays(Visibility) -> some View`

Sets the preferred visibility of the non-transient system views overlaying the
app.

`enum Visibility`

The visibility of a UI element, chosen automatically based on the platform,
current context, and other factors.

Instance Method

# menuIndicator(_:)

Sets the menu indicator visibility for controls within this view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 17.0+  visionOS
1.0+

    
    
    func menuIndicator(_ visibility: Visibility) -> some View
    

##  Parameters

`visibility`

    

The menu indicator visibility to apply.

## Discussion

Use this modifier to override the default menu indicator visibility for
controls in this view. For example, the code below creates a menu without an
indicator:

Note

On tvOS, the standard button styles do not include a menu indicator, so this
modifier will have no effect when using a built-in button style. You can
implement an indicator in your own `ButtonStyle` implementation by checking
the value of the `menuIndicatorVisibility` environment value.

## See Also

### Showing a menu indicator

`var menuIndicatorVisibility: Visibility`

The menu indicator visibility to apply to controls within a view.

Instance Method

# statusBarHidden(_:)

Sets the visibility of the status bar.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  visionOS 1.0+

    
    
    func statusBarHidden(_ hidden: Bool = true) -> some View
    

##  Parameters

`hidden`

    

A Boolean value that indicates whether to hide the status bar.

## See Also

### Hiding system elements

`func labelsHidden() -> some View`

Hides the labels of any controls contained within this view.

`func menuIndicator(Visibility) -> some View`

Sets the menu indicator visibility for controls within this view.

`func persistentSystemOverlays(Visibility) -> some View`

Sets the preferred visibility of the non-transient system views overlaying the
app.

`enum Visibility`

The visibility of a UI element, chosen automatically based on the platform,
current context, and other factors.

Instance Method

# persistentSystemOverlays(_:)

Sets the preferred visibility of the non-transient system views overlaying the
app.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func persistentSystemOverlays(_ visibility: Visibility) -> some View
    

##  Parameters

`visibility`

    

A value that indicates the visibility of the non-transient system views
overlaying the app.

## Discussion

Use this modifier if you would like to customise the immersive experience of
your app by hiding or showing system overlays that may affect user experience.
The following example hides every persistent system overlay.

Note that this modifier only sets a preference and, ultimately the system will
decide if it will honour it or not.

These non-transient system views include:

  * The Home indicator

  * The SharePlay indicator

  * The Multi-task indicator and Picture-in-picture on iPad

## See Also

### Hiding system elements

`func labelsHidden() -> some View`

Hides the labels of any controls contained within this view.

`func menuIndicator(Visibility) -> some View`

Sets the menu indicator visibility for controls within this view.

`func statusBarHidden(Bool) -> some View`

Sets the visibility of the status bar.

`enum Visibility`

The visibility of a UI element, chosen automatically based on the platform,
current context, and other factors.

Enumeration

# Visibility

The visibility of a UI element, chosen automatically based on the platform,
current context, and other factors.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    @frozen
    enum Visibility

## Overview

For example, the preferred visibility of list row separators can be configured
using the `listRowSeparator(_:edges:)`.

## Topics

### Getting visibility options

`case automatic`

The element may be visible or hidden depending on the policies of the
component accepting the visibility configuration.

`case visible`

The element may be visible.

`case hidden`

The element may be hidden.

## Relationships

### Conforms To

  * `CaseIterable`
  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Hiding system elements

`func labelsHidden() -> some View`

Hides the labels of any controls contained within this view.

`func menuIndicator(Visibility) -> some View`

Sets the menu indicator visibility for controls within this view.

`func statusBarHidden(Bool) -> some View`

Sets the visibility of the status bar.

`func persistentSystemOverlays(Visibility) -> some View`

Sets the preferred visibility of the non-transient system views overlaying the
app.

Instance Method

# disabled(_:)

Adds a condition that controls whether users can interact with this view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func disabled(_ disabled: Bool) -> some View
    

##  Parameters

`disabled`

    

A Boolean value that determines whether users can interact with this view.

## Return Value

A view that controls whether users can interact with this view.

## Discussion

The higher views in a view hierarchy can override the value you set on this
view. In the following example, the button isn’t interactive because the outer
`disabled(_:)` modifier overrides the inner one:

## See Also

### Managing view interaction

`var isEnabled: Bool`

A Boolean value that indicates whether the view associated with this
environment allows user interaction.

`func interactionActivityTrackingTag(String) -> some View`

Sets a tag that you use for tracking interactivity.

`func invalidatableContent(Bool) -> some View`

Mark the receiver as their content might be invalidated.

Instance Property

# isEnabled

A Boolean value that indicates whether the view associated with this
environment allows user interaction.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var isEnabled: Bool { get set }

## Discussion

The default value is `true`.

## See Also

### Managing view interaction

`func disabled(Bool) -> some View`

Adds a condition that controls whether users can interact with this view.

`func interactionActivityTrackingTag(String) -> some View`

Sets a tag that you use for tracking interactivity.

`func invalidatableContent(Bool) -> some View`

Mark the receiver as their content might be invalidated.

Instance Method

# interactionActivityTrackingTag(_:)

Sets a tag that you use for tracking interactivity.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func interactionActivityTrackingTag(_ tag: String) -> some View
    

##  Parameters

`tag`

    

The tag used to track user interactions hosted by this view as activities.

## Return Value

A view that uses a tracking tag.

## Discussion

The following example tracks the scrolling activity of a `List`:

The resolved activity tracking tag is additive, so using the modifier across
the view hierarchy builds the tag from top to bottom. The example below shows
a hierarchical usage of this modifier with the resulting tag `Home-Feed`:

## See Also

### Managing view interaction

`func disabled(Bool) -> some View`

Adds a condition that controls whether users can interact with this view.

`var isEnabled: Bool`

A Boolean value that indicates whether the view associated with this
environment allows user interaction.

`func invalidatableContent(Bool) -> some View`

Mark the receiver as their content might be invalidated.

Instance Method

# invalidatableContent(_:)

Mark the receiver as their content might be invalidated.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func invalidatableContent(_ invalidatable: Bool = true) -> some View
    

##  Parameters

`invalidatable`

    

Whether the receiver content might be invalidated.

## Discussion

Use this modifier to annotate views that display values that are derived from
the current state of your data and might be invalidated in response of, for
example, user interaction.

The view will change its appearance when `RedactionReasons.invalidated` is
present in the environment.

In an interactive widget a view is invalidated from the moment the user
interacts with a control on the widget to the moment when a new timeline
update has been presented.

## See Also

### Managing view interaction

`func disabled(Bool) -> some View`

Adds a condition that controls whether users can interact with this view.

`var isEnabled: Bool`

A Boolean value that indicates whether the view associated with this
environment allows user interaction.

`func interactionActivityTrackingTag(String) -> some View`

Sets a tag that you use for tracking interactivity.

Instance Method

# help(_:)

Adds help text to a view using a localized string that you provide.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func help(_ textKey: LocalizedStringKey) -> some View
    

##  Parameters

`textKey`

    

The key for the localized text to use as help.

## Discussion

Adding help to a view configures the view’s accessibility hint and its help
tag (also called a _tooltip_) in macOS or visionOS. For more information on
using help tags, see Offering help in the Human Interface Guidelines.

## See Also

### Providing contextual help

`func help<S>(S) -> some View`

Adds help text to a view using a string that you provide.

`func help(Text) -> some View`

Adds help text to a view using a text view that you provide.

Instance Method

# help(_:)

Adds help text to a view using a string that you provide.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func help<S>(_ text: S) -> some View where S : StringProtocol
    

##  Parameters

`text`

    

The text to use as help.

## Discussion

Adding help to a view configures the view’s accessibility hint and its help
tag (also called a _tooltip_) in macOS or visionOS. For more information on
using help tags, see Offering help in the Human Interface Guidelines.

## See Also

### Providing contextual help

`func help(LocalizedStringKey) -> some View`

Adds help text to a view using a localized string that you provide.

`func help(Text) -> some View`

Adds help text to a view using a text view that you provide.

Instance Method

# help(_:)

Adds help text to a view using a text view that you provide.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func help(_ text: Text) -> some View
    

##  Parameters

`text`

    

The `Text` view to use as help.

## Discussion

Adding help to a view configures the view’s accessibility hint and its help
tag (also called a _tooltip_) in macOS or visionOS. For more information on
using help tags, see Offering help in the Human Interface Guidelines.

## See Also

### Providing contextual help

`func help(LocalizedStringKey) -> some View`

Adds help text to a view using a localized string that you provide.

`func help<S>(S) -> some View`

Adds help text to a view using a string that you provide.

Instance Method

# glassBackgroundEffect(displayMode:)

Fills the view’s background with a glass material that’s shaped as a
container-relative rounded rectangle.

visionOS 1.0+

    
    
    func glassBackgroundEffect(displayMode: GlassBackgroundDisplayMode = .always) -> some View
    

##  Parameters

`displayMode`

    

When to display the glass background. The default is
`GlassBackgroundDisplayMode.always`.

## Return Value

A view with a glass background.

## Discussion

Use this modifier to add a 3D glass background material that includes
thickness, specularity, glass blur, shadows, and other effects. Because of its
physical depth, the glass background influences z-axis layout.

To ensure that the effect renders properly when you add it to a collection of
views in a `ZStack`, add the modifier to the stack rather to one of the views
in the stack. This includes when you create an implicit stack with view
modifiers like `overlay(alignment:content:)` or
`background(alignment:content:)`. In those cases, you might need to create an
explicit `ZStack` inside the `content` closure to have a place to add the
glass background modifier.

## See Also

### Adding a glass background

`func glassBackgroundEffect<S>(in: S, displayMode: GlassBackgroundDisplayMode)
-> some View`

Fills the view’s background with a glass material using a shape that you
specify.

`enum GlassBackgroundDisplayMode`

The display mode of a glass background.

Instance Method

# glassBackgroundEffect(in:displayMode:)

Fills the view’s background with a glass material using a shape that you
specify.

visionOS 1.0+

    
    
    func glassBackgroundEffect<S>(
        in shape: S,
        displayMode: GlassBackgroundDisplayMode = .always
    ) -> some View where S : InsettableShape
    

##  Parameters

`shape`

    

An `InsettableShape` instance that SwiftUI draws behind the view. Unsupported
shapes resolve to a rectangle.

`displayMode`

    

When to display the glass background. The default is
`GlassBackgroundDisplayMode.always`.

## Return Value

A view with a glass background.

## Discussion

Use this modifier to add a 3D glass background material that includes
thickness, specularity, glass blur, shadows, and other effects. Because of its
physical depth, the glass background influences z-axis layout.

To ensure that the effect renders properly when you add it to a collection of
views in a `ZStack`, add the modifier to the stack rather to one of the views
in the stack. This includes when you create an implicit stack with view
modifiers like `overlay(alignment:content:)` or
`background(alignment:content:)`. In those cases, you might need to create an
explicit `ZStack` inside the `content` closure to have a place to add the
glass background modifier.

Prefer a shape for the background that has rounded corners. An unsupported
shape style resolves to a rectangle.

## See Also

### Adding a glass background

`func glassBackgroundEffect(displayMode: GlassBackgroundDisplayMode) -> some
View`

Fills the view’s background with a glass material that’s shaped as a
container-relative rounded rectangle.

`enum GlassBackgroundDisplayMode`

The display mode of a glass background.

Enumeration

# GlassBackgroundDisplayMode

The display mode of a glass background.

visionOS 1.0+

    
    
    enum GlassBackgroundDisplayMode

## Overview

Use a value of this type to indicate when to display a glass background that
you add to a view using a view modifier like
`glassBackgroundEffect(displayMode:)`.

## Topics

### Getting the mode

`case always`

Always display the glass material.

`case implicit`

Display the glass material only when the view isn’t already contained in
glass.

`case never`

Never display the glass material.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Adding a glass background

`func glassBackgroundEffect(displayMode: GlassBackgroundDisplayMode) -> some
View`

Fills the view’s background with a glass material that’s shaped as a
container-relative rounded rectangle.

`func glassBackgroundEffect<S>(in: S, displayMode: GlassBackgroundDisplayMode)
-> some View`

Fills the view’s background with a glass material using a shape that you
specify.

Instance Method

# preferredColorScheme(_:)

Sets the preferred color scheme for this presentation.

iOS 13.0+  iPadOS 13.0+  macOS 11.0+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func preferredColorScheme(_ colorScheme: ColorScheme?) -> some View
    

##  Parameters

`colorScheme`

    

The preferred color scheme for this view.

## Return Value

A view that sets the color scheme.

## Discussion

Use one of the values in `ColorScheme` with this modifier to set a preferred
color scheme for the nearest enclosing presentation, like a popover, a sheet,
or a window. The value that you set overrides the user’s Dark Mode selection
for that presentation. In the example below, the `Toggle` controls an
`isDarkMode` state variable, which in turn controls the color scheme of the
sheet that contains the toggle:

If you apply the modifier to any of the views in the sheet — which in this
case are a `List` and a `Toggle` — the value that you set propagates up
through the view hierarchy to the enclosing presentation, or until another
color scheme modifier higher in the hierarchy overrides it. The value you set
also flows down to all child views of the enclosing presentation.

A common use for this modifier is to create side-by-side previews of the same
view with light and dark appearances:

If you need to detect the color scheme that currently applies to a view, read
the `colorScheme` environment value:

## See Also

### Detecting and requesting the light or dark appearance

`var colorScheme: ColorScheme`

The color scheme of this environment.

`enum ColorScheme`

The possible color schemes, corresponding to the light and dark appearances.

Instance Property

# colorScheme

The color scheme of this environment.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var colorScheme: ColorScheme { get set }

## Discussion

Read this environment value from within a view to find out if SwiftUI is
currently displaying the view using the `ColorScheme.light` or
`ColorScheme.dark` appearance. The value that you receive depends on whether
the user has enabled Dark Mode, possibly superseded by the configuration of
the current presentation’s view hierarchy.

You can set the `colorScheme` environment value directly, but that usually
isn’t what you want. Doing so changes the color scheme of the given view and
its child views but _not_ the views above it in the view hierarchy. Instead,
set a color scheme using the `preferredColorScheme(_:)` modifier, which also
propagates the value up through the view hierarchy to the enclosing
presentation, like a sheet or a window.

When adjusting your app’s user interface to match the color scheme, consider
also checking the `colorSchemeContrast` property, which reflects a system-wide
contrast setting that the user controls. For information, see Accessibility in
the Human Interface Guidelines.

Note

If you only need to provide different colors or images for different color
scheme and contrast settings, do that in your app’s Asset Catalog. See Asset
management.

## See Also

### Detecting and requesting the light or dark appearance

`func preferredColorScheme(ColorScheme?) -> some View`

Sets the preferred color scheme for this presentation.

`enum ColorScheme`

The possible color schemes, corresponding to the light and dark appearances.

Enumeration

# ColorScheme

The possible color schemes, corresponding to the light and dark appearances.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    enum ColorScheme

## Overview

You receive a color scheme value when you read the `colorScheme` environment
value. The value tells you if a light or dark appearance currently applies to
the view. SwiftUI updates the value whenever the appearance changes, and
redraws views that depend on the value. For example, the following `Text` view
automatically updates when the user enables Dark Mode:

Set a preferred appearance for a particular view hierarchy to override the
user’s Dark Mode setting using the `preferredColorScheme(_:)` view modifier.

## Topics

### Getting color schemes

`case light`

The color scheme that corresponds to a light appearance.

`case dark`

The color scheme that corresponds to a dark appearance.

### Creating a color scheme

`init?(UIUserInterfaceStyle)`

Creates a color scheme from its user interface style equivalent.

### Supporting types

`struct PreferredColorSchemeKey`

A key for specifying the preferred color scheme.

## Relationships

### Conforms To

  * `CaseIterable`
  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Detecting and requesting the light or dark appearance

`func preferredColorScheme(ColorScheme?) -> some View`

Sets the preferred color scheme for this presentation.

`var colorScheme: ColorScheme`

The color scheme of this environment.

Instance Property

# colorSchemeContrast

The contrast associated with the color scheme of this environment.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var colorSchemeContrast: ColorSchemeContrast { get }

## Discussion

Read this environment value from within a view to find out if SwiftUI is
currently displaying the view using `ColorSchemeContrast.standard` or
`ColorSchemeContrast.increased` contrast. The value that you read depends
entirely on user settings, and you can’t change it.

When adjusting your app’s user interface to match the contrast, consider also
checking the `colorScheme` property to find out if SwiftUI is displaying the
view with a light or dark appearance. For information, see Accessibility in
the Human Interface Guidelines.

Note

If you only need to provide different colors or images for different color
scheme and contrast settings, do that in your app’s Asset Catalog. See Asset
management.

## See Also

### Getting the color scheme contrast

`enum ColorSchemeContrast`

The contrast between the app’s foreground and background colors.

Enumeration

# ColorSchemeContrast

The contrast between the app’s foreground and background colors.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    enum ColorSchemeContrast

## Overview

You receive a contrast value when you read the `colorSchemeContrast`
environment value. The value tells you if a standard or increased contrast
currently applies to the view. SwiftUI updates the value whenever the contrast
changes, and redraws views that depend on the value. For example, the
following `Text` view automatically updates when the user enables increased
contrast:

The user sets the contrast by selecting the Increase Contrast option in
Accessibility > Display in System Preferences on macOS, or Accessibility >
Display & Text Size in the Settings app on iOS. Your app can’t override the
user’s choice. For information about using color and contrast in your app, see
Accessibility in the Human Interface Guidelines.

## Topics

### Getting contrast options

`case standard`

SwiftUI displays views with standard contrast between the app’s foreground and
background colors.

`case increased`

SwiftUI displays views with increased contrast between the app’s foreground
and background colors.

### Creating a color scheme contrast

`init?(UIAccessibilityContrast)`

Creates a contrast from its accessibility contrast equivalent.

## Relationships

### Conforms To

  * `CaseIterable`
  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Getting the color scheme contrast

`var colorSchemeContrast: ColorSchemeContrast`

The contrast associated with the color scheme of this environment.

Instance Method

# preferredSurroundingsEffect(_:)

Applies an effect to passthrough video.

visionOS 1.0+

    
    
    func preferredSurroundingsEffect(_ effect: SurroundingsEffect?) -> some View
    

##  Parameters

`effect`

    

The effect that you want to apply.

## Return Value

A view that exhibits the specified preference.

## Discussion

Use this modifier to indicate a preference for the appearance of passthrough
video when displaying the modified view. For example, you can enhance the
immersiveness of a scene that uses the default `mixed` immersion style by
applying the `systemDark` preference to a view inside the scene:

When the system presents the `Orbit` view in the above code, it also dims
passthrough video. This helps to draw attention to the scene’s virtual content
while still enabling people to remain aware of their surroundings.

Note

This modifier expresses a preference, but the system might not be able to
honor it.

Use a value of `nil` to indicate that you have no preference. You typically do
this to counteract a preference expressed by a view lower in the view
hierarchy.

## See Also

### Configuring passthrough

`struct SurroundingsEffect`

Effects that the system can apply to passthrough video.

Structure

# SurroundingsEffect

Effects that the system can apply to passthrough video.

visionOS 1.0+

    
    
    struct SurroundingsEffect

## Overview

Use one of these values with the `preferredSurroundingsEffect(_:)` view
modifier to indicate what effect to apply to passthrough video when the
modified view is displayed.

## Topics

### Getting the effect

`static var systemDark: SurroundingsEffect`

An effect that dims passthrough video.

## Relationships

### Conforms To

  * `Equatable`

## See Also

### Configuring passthrough

`func preferredSurroundingsEffect(SurroundingsEffect?) -> some View`

Applies an effect to passthrough video.

Article

# Designing your app for the Always On state

Customize your watchOS app’s user interface for continuous display.

## Overview

The launch of watchOS 6 introduced the Always On state. Supported devices
continued to display the time, even when the user isn’t actively interacting
with the watch; however, when running an app, the system blurs the app’s user
interface and displays the time over it.

In watchOS 8, Always On expands to include your apps. Apple Watch continues to
display your app’s user interface as long as it’s either the frontmost app or
running a background session. To preserve battery life, the system updates the
user interface at a much lower frequency than when running in the foreground.
It also dims the watch.

Even though your app is inactive or running in the background, the system
continues to update and monitor many of the user interface elements. For
example, when displaying dates and times, using `Text.DateStyle` values like
`relative`, `offset`, and `timer`, the system automatically updates the `Text`
view while in Always On.

Additionally, any controls in the user interface remain interactive. Users can
tap buttons, toggle switches, or select items from a list. When the user
interacts with a control, the system runs the associated action and
transitions your app back to the active state.

Note

Always On isn’t available on Apple Watch SE or Apple Watch Series 4 and
earlier. For these devices, the screen turns off when the app transitions to
the background or inactive states.

Apps compiled for watchOS 8 and later have Always On enabled by default. You
can disable this feature by setting the `WKSupportsAlwaysOnDisplay` key to
`false` in the WatchKit Extension’s `Info.plist` file. Users can also disable
Always On for the entire device or on a per-app basis by choosing Settings >
Display & Brightness > Always On.

### Understand frontmost app behavior

By default, when the user lowers their wrist or stops interacting with their
watch, your app transitions to the inactive state. The system continues to
display your app’s user interface as long as your app remains the frontmost
app (usually two minutes) before transitioning to the background and becoming
suspended. If the user dismisses the app (for example, by pressing the Digital
Crown or by covering the screen), the app transitions immediately to the
background and doesn’t become the frontmost app.

Users can set the amount of time that apps remain the frontmost app by
changing the settings at Settings > General > Wake Screen > Return to Clock.
They can also specify a custom time for individual apps from the Wake Screen.
In watchOS 8 and later, apps can remain in the frontmost app state for a
maximum of 1 hour.

When the app is inactive, the user interface doesn’t update by default.
However, you can use a `TimelineView` to schedule periodic updates. For more
information, see Updating watchOS apps with timelines.

### Update the display during background sessions

Apps running a background session, such as a workout session or background
audio session, remain onscreen as long as the session is active. Unlike
frontmost apps, apps running a background session can continue to update their
user interface; however, to save battery life, the system reduces the update
frequency.

For the best user experience when the app transitions to the background, pause
any animation and show the final state (or a good static image), and remove
any subsecond updates. For example, when the workout app is running in the
foreground, the duration shows hundredths of a second, and the BPM row shows
an animated heart beat. When it transitions to the background, the app
displays a static heart image and the duration only shows time to the nearest
second.

For animation or updates driven by a `TimelineView`, check the view’s cadence
and update the appearance to match. For more information on timelines, see
Updating watchOS apps with timelines.

For other views, monitor the app’s `scenePhase` environment variable, and hide
or stop subsecond updates when it becomes `ScenePhase.inactive` or
`ScenePhase.background`.

### Hide sensitive information

Because displayed information may be visible to casual observers, be sure to
hide any sensitive data while your app is in Always On. Add the
`privacySensitive(_:)` view modifier to blur out specific user interface
elements during Always On.

Or access the `redactionReasons` environment variable.

Check if this variable contains the `privacy` value. If it does, eliminate or
obscure any sensitive data.

The resulting user interface displays the private data while the app is
running in the foreground.

But the interface obscures sensitive data, such as the account number and
balance, when the app is in the Always On state.

To protect the user’s privacy, always hide any highly sensitive information,
such as financial information or health data. For information that may or may
not be sensitive, such as incoming messages or appointments, default to
showing the information. If the user has any concerns, they can disable Always
On on a per-app basis.

### Customize the reduced luminance appearance

To preserve battery life, the system dims the screen during Always On. The
system determines the screen’s overall luminance by comparing the ratio of lit
pixels to dark pixels. It then reduces the overall brightness to an
appropriate level.

Many system controls also automatically update their appearance during Always
On. For example, the `List` view automatically dims the background for the
`CarouselListStyle`.

Many apps can use the system’s default Always On appearance. For example, if
your view is mostly black and uses system controls, you may not need to change
anything. However, you can customize the appearance during Always On to
highlight glanceable, important information in your user interface.

For example, you may consider replacing large blocks of bright content with
stroked outlines and dimmed interiors, as shown on the Numerals Duo watch
face.

You can also dim or remove nonessential information. To customize your
interface, use the `isLuminanceReduced` environment variable.

You can then use this value to modify your user interface, as needed.

The resulting interface displays the title text at full brightness when
active.

Then it dims the title in Always On. Because the ratio of lit to dark pixels
is low, the system doesn’t need to make any other changes to the view.

### Preview both interfaces in Xcode

You can preview both the regular and Always On interfaces in Xcode. To see the
Always On interface, set the `isLuminanceReduced` and `redactionReasons`
environment variables in the preview.

The resulting preview shows both the regular and the Always On interfaces.

Note

The system doesn’t automatically dim the user interface when previewing in
Xcode. To see how the system automatically dims the user interface, you must
test it on a device or in the simulator.

### Test Always On in the Simulator

Xcode supports Always On in the simulator. Simply click the Toggle Always On
button in the status bar to test.

You can view any changes to your user interface related to privacy, reduced
luminance, or transitioning to an inactive state.

## See Also

### Related Documentation

`property list key WKSupportsAlwaysOnDisplay`

A Boolean value that determines whether the system displays the app in the
Always On state.

### User interface

Supporting multiple watch sizes

Customize the layout of your user interface to support all Apple Watch screen
sizes.

Setting the app’s accent color

Set your app’s accent color.

Instance Method

# privacySensitive(_:)

Marks the view as containing sensitive, private user data.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func privacySensitive(_ sensitive: Bool = true) -> some View
    

## Discussion

SwiftUI redacts views marked with this modifier when you apply the `privacy`
redaction reason.

## See Also

### Redacting private content

Designing your app for the Always On state

Customize your watchOS app’s user interface for continuous display.

`func redacted(reason: RedactionReasons) -> some View`

Adds a reason to apply a redaction to this view hierarchy.

`func unredacted() -> some View`

Removes any reason to apply a redaction to this view hierarchy.

`var redactionReasons: RedactionReasons`

The current redaction reasons applied to the view hierarchy.

`var isSceneCaptured: Bool`

The current capture state.

`struct RedactionReasons`

The reasons to apply a redaction to data displayed on screen.

Instance Method

# redacted(reason:)

Adds a reason to apply a redaction to this view hierarchy.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func redacted(reason: RedactionReasons) -> some View
    

## Discussion

Adding a redaction is an additive process: any redaction provided will be
added to the reasons provided by the parent.

## See Also

### Redacting private content

Designing your app for the Always On state

Customize your watchOS app’s user interface for continuous display.

`func privacySensitive(Bool) -> some View`

Marks the view as containing sensitive, private user data.

`func unredacted() -> some View`

Removes any reason to apply a redaction to this view hierarchy.

`var redactionReasons: RedactionReasons`

The current redaction reasons applied to the view hierarchy.

`var isSceneCaptured: Bool`

The current capture state.

`struct RedactionReasons`

The reasons to apply a redaction to data displayed on screen.

Instance Method

# unredacted()

Removes any reason to apply a redaction to this view hierarchy.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func unredacted() -> some View
    

## See Also

### Redacting private content

Designing your app for the Always On state

Customize your watchOS app’s user interface for continuous display.

`func privacySensitive(Bool) -> some View`

Marks the view as containing sensitive, private user data.

`func redacted(reason: RedactionReasons) -> some View`

Adds a reason to apply a redaction to this view hierarchy.

`var redactionReasons: RedactionReasons`

The current redaction reasons applied to the view hierarchy.

`var isSceneCaptured: Bool`

The current capture state.

`struct RedactionReasons`

The reasons to apply a redaction to data displayed on screen.

Instance Property

# redactionReasons

The current redaction reasons applied to the view hierarchy.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    var redactionReasons: RedactionReasons { get set }

## See Also

### Redacting private content

Designing your app for the Always On state

Customize your watchOS app’s user interface for continuous display.

`func privacySensitive(Bool) -> some View`

Marks the view as containing sensitive, private user data.

`func redacted(reason: RedactionReasons) -> some View`

Adds a reason to apply a redaction to this view hierarchy.

`func unredacted() -> some View`

Removes any reason to apply a redaction to this view hierarchy.

`var isSceneCaptured: Bool`

The current capture state.

`struct RedactionReasons`

The reasons to apply a redaction to data displayed on screen.

Instance Property

# isSceneCaptured

The current capture state.

iOS 17.0+  iPadOS 17.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    var isSceneCaptured: Bool { get set }

## Discussion

Use this value to determine whether the scene is actively being cloned to
another destination (like during AirPlay) or is being mirrored or recorded.

Your app can respond to changes in this value to take appropriate action, like
obscuring content.

## See Also

### Redacting private content

Designing your app for the Always On state

Customize your watchOS app’s user interface for continuous display.

`func privacySensitive(Bool) -> some View`

Marks the view as containing sensitive, private user data.

`func redacted(reason: RedactionReasons) -> some View`

Adds a reason to apply a redaction to this view hierarchy.

`func unredacted() -> some View`

Removes any reason to apply a redaction to this view hierarchy.

`var redactionReasons: RedactionReasons`

The current redaction reasons applied to the view hierarchy.

`struct RedactionReasons`

The reasons to apply a redaction to data displayed on screen.

Structure

# RedactionReasons

The reasons to apply a redaction to data displayed on screen.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    struct RedactionReasons

## Topics

### Getting redaction reasons

`static let invalidated: RedactionReasons`

Displayed data should appear as invalidated and pending a new update.

`static let placeholder: RedactionReasons`

Displayed data should appear as generic placeholders.

`static let privacy: RedactionReasons`

Displayed data should be obscured to protect private information.

### Creating redaction reasons

`init(rawValue: Int)`

Creates a new set from a raw value.

`let rawValue: Int`

The raw value.

## Relationships

### Conforms To

  * `Equatable`
  * `ExpressibleByArrayLiteral`
  * `OptionSet`
  * `RawRepresentable`
  * `Sendable`
  * `SetAlgebra`

## See Also

### Redacting private content

Designing your app for the Always On state

Customize your watchOS app’s user interface for continuous display.

`func privacySensitive(Bool) -> some View`

Marks the view as containing sensitive, private user data.

`func redacted(reason: RedactionReasons) -> some View`

Adds a reason to apply a redaction to this view hierarchy.

`func unredacted() -> some View`

Removes any reason to apply a redaction to this view hierarchy.

`var redactionReasons: RedactionReasons`

The current redaction reasons applied to the view hierarchy.

`var isSceneCaptured: Bool`

The current capture state.



# VerticalPageTabViewStyle

Initializer

# init()

watchOS 10.0+

    
    
    init()

## See Also

### Creating the tab view style

`init(transitionStyle: VerticalPageTabViewStyle.TransitionStyle)`

Creates a new `VerticalPageTabViewStyle` with a transition style.

`struct TransitionStyle`

A transition style used between tabs.

Initializer

# init(transitionStyle:)

Creates a new `VerticalPageTabViewStyle` with a transition style.

watchOS 10.0+

    
    
    init(transitionStyle: VerticalPageTabViewStyle.TransitionStyle)

## See Also

### Creating the tab view style

`init()`

`struct TransitionStyle`

A transition style used between tabs.

Structure

# VerticalPageTabViewStyle.TransitionStyle

A transition style used between tabs.

watchOS 10.0+

    
    
    struct TransitionStyle

## Topics

### Getting the transition styles

`static let automatic: VerticalPageTabViewStyle.TransitionStyle`

Automatic transition style

`static let blur: VerticalPageTabViewStyle.TransitionStyle`

A transition style that blurs content between each tab

`static let identity: VerticalPageTabViewStyle.TransitionStyle`

A transition style that has no animation between each tab

## See Also

### Creating the tab view style

`init()`

`init(transitionStyle: VerticalPageTabViewStyle.TransitionStyle)`

Creates a new `VerticalPageTabViewStyle` with a transition style.



