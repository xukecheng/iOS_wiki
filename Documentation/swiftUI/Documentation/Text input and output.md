Structure

# Text

A view that displays one or more lines of read-only text.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct Text

## Overview

A text view draws a string in your app’s user interface using a `body` font
that’s appropriate for the current platform. You can choose a different
standard font, like `title` or `caption`, using the `font(_:)` view modifier.

If you need finer control over the styling of the text, you can use the same
modifier to configure a system font or choose a custom font. You can also
apply view modifiers like `bold()` or `italic()` to further adjust the
formatting.

To apply styling within specific portions of the text, you can create the text
view from an `AttributedString`, which in turn allows you to use Markdown to
style runs of text. You can mix string attributes and SwiftUI modifiers, with
the string attributes taking priority.

A text view always uses exactly the amount of space it needs to display its
rendered contents, but you can affect the view’s layout. For example, you can
use the `frame(width:height:alignment:)` modifier to propose specific
dimensions to the view. If the view accepts the proposal but the text doesn’t
fit into the available space, the view uses a combination of wrapping,
tightening, scaling, and truncation to make it fit. With a width of `100`
points but no constraint on the height, a text view might wrap a long string:

Use modifiers like `lineLimit(_:)`, `allowsTightening(_:)`,
`minimumScaleFactor(_:)`, and `truncationMode(_:)` to configure how the view
handles space constraints. For example, combining a fixed width and a line
limit of `1` results in truncation for text that doesn’t fit in that space:

### Localizing strings

If you initialize a text view with a string literal, the view uses the
`init(_:tableName:bundle:comment:)` initializer, which interprets the string
as a localization key and searches for the key in the table you specify, or in
the default table if you don’t specify one.

For an app localized in both English and Spanish, the above view displays
“pencil” and “lápiz” for English and Spanish users, respectively. If the view
can’t perform localization, it displays the key instead. For example, if the
same app lacks Danish localization, the view displays “pencil” for users in
that locale. Similarly, an app that lacks any localization information
displays “pencil” in any locale.

To explicitly bypass localization for a string literal, use the
`init(verbatim:)` initializer.

If you intialize a text view with a variable value, the view uses the
`init(_:)` initializer, which doesn’t localize the string. However, you can
request localization by creating a `LocalizedStringKey` instance first, which
triggers the `init(_:tableName:bundle:comment:)` initializer instead:

When localizing a string variable, you can use the default table by omitting
the optional initialization parameters — as in the above example — just like
you might for a string literal.

## Topics

### Creating a text view from a string

`init(LocalizedStringKey, tableName: String?, bundle: Bundle?, comment:
StaticString?)`

Creates a text view that displays localized content identified by a key.

`init(LocalizedStringResource)`

Creates a text view that displays a localized string resource.

`init<S>(S)`

Creates a text view that displays a stored string without localization.

`init(verbatim: String)`

Creates a text view that displays a string literal without localization.

### Creating a text view from an attributed string

`init(AttributedString)`

Creates a text view that displays styled attributed content.

### Creating a text view for a date

`init(ClosedRange<Date>)`

Creates an instance that displays a localized range between two dates.

`init(DateInterval)`

Creates an instance that displays a localized time interval.

`init(Date, style: Text.DateStyle)`

Creates an instance that displays localized dates and times using a specific
style.

### Creating a text view with formatting

`init<F>(F.FormatInput, format: F)`

Creates a text view that displays the formatted representation of a nonstring
type supported by a corresponding format style.

`init<Subject>(Subject, formatter: Formatter)`

Creates a text view that displays the formatted representation of a reference-
convertible value.

`init<Subject>(Subject, formatter: Formatter)`

Creates a text view that displays the formatted representation of a Foundation
object.

### Creating a text view from an image

`init(Image)`

Creates an instance that wraps an `Image`, suitable for concatenating with
other `Text`

### Creating a text view with a timer

`init(timerInterval: ClosedRange<Date>, pauseTime: Date?, countsDown: Bool,
showsHours: Bool)`

Creates an instance that displays a timer counting within the provided
interval.

### Choosing a font

`func font(Font?) -> Text`

Sets the default font for text in the view.

`func fontWeight(Font.Weight?) -> Text`

Sets the font weight of the text.

`func fontDesign(Font.Design?) -> Text`

Sets the font design of the text.

`func fontWidth(Font.Width?) -> Text`

Sets the font width of the text.

### Styling the view’s text

`func foregroundStyle<S>(S) -> Text`

Sets the style of the text displayed by this view.

`func bold() -> Text`

Applies a bold font weight to the text.

`func bold(Bool) -> Text`

Applies a bold font weight to the text.

`func italic() -> Text`

Applies italics to the text.

`func italic(Bool) -> Text`

Applies italics to the text.

`func strikethrough(Bool, color: Color?) -> Text`

Applies a strikethrough to the text.

`func strikethrough(Bool, pattern: Text.LineStyle.Pattern, color: Color?) ->
Text`

Applies a strikethrough to the text.

`func underline(Bool, color: Color?) -> Text`

Applies an underline to the text.

`func underline(Bool, pattern: Text.LineStyle.Pattern, color: Color?) -> Text`

Applies an underline to the text.

`func monospaced(Bool) -> Text`

Modifies the font of the text to use the fixed-width variant of the current
font, if possible.

`func monospacedDigit() -> Text`

Modifies the text view’s font to use fixed-width digits, while leaving other
characters proportionally spaced.

`func kerning(CGFloat) -> Text`

Sets the spacing, or kerning, between characters.

`func tracking(CGFloat) -> Text`

Sets the tracking for the text.

`func baselineOffset(CGFloat) -> Text`

Sets the vertical offset for the text relative to its baseline.

`enum Case`

A scheme for transforming the capitalization of characters within text.

`struct DateStyle`

A predefined style used to display a `Date`.

`struct LineStyle`

Description of the style used to draw the line for
`StrikethroughStyleAttribute` and `UnderlineStyleAttribute`.

### Fitting text into available space

`func textScale(Text.Scale, isEnabled: Bool) -> Text`

Applies a text scale to the text.

`struct Scale`

Defines text scales

`enum TruncationMode`

The type of truncation to apply to a line of text when it’s too long to fit in
the available space.

### Localizing text

`func typesettingLanguage(TypesettingLanguage, isEnabled: Bool) -> Text`

Specifies the language for typesetting.

`func typesettingLanguage(Locale.Language, isEnabled: Bool) -> Text`

Specifies the language for typesetting.

### Configuring voiceover

`func speechAdjustedPitch(Double) -> Text`

Raises or lowers the pitch of spoken text.

`func speechAlwaysIncludesPunctuation(Bool) -> Text`

Sets whether VoiceOver should always speak all punctuation in the text view.

`func speechAnnouncementsQueued(Bool) -> Text`

Controls whether to queue pending announcements behind existing speech rather
than interrupting speech in progress.

`func speechSpellsOutCharacters(Bool) -> Text`

Sets whether VoiceOver should speak the contents of the text view character by
character.

### Providing accessibility information

`func accessibilityHeading(AccessibilityHeadingLevel) -> Text`

Sets the accessibility level of this heading.

`func accessibilityLabel<S>(S) -> Text`

Adds a label to the view that describes its contents.

`func accessibilityLabel(Text) -> Text`

Adds a label to the view that describes its contents.

`func accessibilityLabel(LocalizedStringKey) -> Text`

Adds a label to the view that describes its contents.

`func accessibilityTextContentType(AccessibilityTextContentType) -> Text`

Sets an accessibility text content type.

### Combining text views

`static func + (Text, Text) -> Text`

Concatenates the text in two text views in a new text view.

### Deprecated symbols

`func foregroundColor(Color?) -> Text`

Sets the color of the text displayed by this view.

Deprecated

## Relationships

### Conforms To

  * `Equatable`
  * `Sendable`
  * `View`

## See Also

### Displaying text

`struct Label`

A standard label for user interface items, consisting of an icon with a title.

`func labelStyle<S>(S) -> some View`

Sets the style for labels within this view.

Structure

# Label

A standard label for user interface items, consisting of an icon with a title.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    struct Label<Title, Icon> where Title : View, Icon : View

## Overview

One of the most common and recognizable user interface components is the
combination of an icon and a label. This idiom appears across many kinds of
apps and shows up in collections, lists, menus of action items, and
disclosable lists, just to name a few.

You create a label, in its simplest form, by providing a title and the name of
an image, such as an icon from the SF Symbols collection:

You can also apply styles to labels in several ways. In the case of dynamic
changes to the view after device rotation or change to a window size you might
want to show only the text portion of the label using the `titleOnly` label
style:

Conversely, there’s also an icon-only label style:

Some containers might apply a different default label style, such as only
showing icons within toolbars on macOS and iOS. To opt in to showing both the
title and the icon, you can apply the `titleAndIcon` label style:

You can also create a customized label style by modifying an existing style;
this example adds a red border to the default label style:

For more extensive customization or to create a completely new label style,
you’ll need to adopt the `LabelStyle` protocol and implement a
`LabelStyleConfiguration` for the new style.

To apply a common label style to a group of labels, apply the style to the
view hierarchy that contains the labels:

It’s also possible to make labels using views to compose the label’s icon
programmatically, rather than using a pre-made image. In this example, the
icon portion of the label uses a filled `Circle` overlaid with the user’s
initials:

## Topics

### Creating a label from text and an image

`init(LocalizedStringKey, image: String)`

Creates a label with an icon image and a title generated from a localized
string.

Available when `Title` is `Text` and `Icon` is `Image`.

`init<S>(S, image: String)`

Creates a label with an icon image and a title generated from a string.

Available when `Title` is `Text` and `Icon` is `Image`.

### Creating a label from text and an SF Symbol

`init(LocalizedStringKey, systemImage: String)`

Creates a label with a system icon image and a title generated from a
localized string.

Available when `Title` is `Text` and `Icon` is `Image`.

`init<S>(S, systemImage: String)`

Creates a label with a system icon image and a title generated from a string.

Available when `Title` is `Text` and `Icon` is `Image`.

### Creating a label from a title and icon

`init(title: () -> Title, icon: () -> Icon)`

Creates a label with a custom title and icon.

### Creating a label from a configuration

`init(LabelStyleConfiguration)`

Creates a label representing the configuration of a style.

Available when `Title` is `LabelStyleConfiguration.Title` and `Icon` is
`LabelStyleConfiguration.Icon`.

### Creating a label from an image resource

`init(LocalizedStringKey, image: ImageResource)`

Creates a label with an icon image and a title generated from a localized
string.

Available when `Title` is `Text` and `Icon` is `Image`.

`init<S>(S, image: ImageResource)`

Creates a label with an icon image and a title generated from a string.

Available when `Title` is `Text` and `Icon` is `Image`.

### Creating a family activity label

`init(ApplicationToken)`

Creates a label representing a family activity application.

Available when `Title` is `FamilyActivityTitleView` and `Icon` is
`FamilyActivityIconView`.

`init(WebDomainToken)`

Creates a label representing a family activity web domain.

Available when `Title` is `FamilyActivityTitleView` and `Icon` is
`FamilyActivityIconView`.

`init(ActivityCategoryToken)`

Creates a label representing a family activity category.

Available when `Title` is `FamilyActivityTitleView` and `Icon` is
`FamilyActivityIconView`.

## Relationships

### Conforms To

  * `View`

## See Also

### Displaying text

`struct Text`

A view that displays one or more lines of read-only text.

`func labelStyle<S>(S) -> some View`

Sets the style for labels within this view.

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

Structure

# TextField

A control that displays an editable text interface.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    struct TextField<Label> where Label : View

## Overview

You create a text field with a label and a binding to a value. If the value is
a string, the text field updates this value continuously as the user types or
otherwise edits the text in the field. For non-string types, it updates the
value when the user commits their edits, such as by pressing the Return key.

The following example shows a text field to accept a username, and a `Text`
view below it that shadows the continuously updated value of `username`. The
`Text` view changes color as the user begins and ends editing. When the user
submits their completed entry to the text field, the `onSubmit(of:_:)` modifer
calls an internal `validate(name:)` method.

The bound value doesn’t have to be a string. By using a `FormatStyle`, you can
bind the text field to a nonstring type, using the format style to convert the
typed text into an instance of the bound type. The following example uses a
`PersonNameComponents.FormatStyle` to convert the name typed in the text field
to a `PersonNameComponents` instance. A `Text` view below the text field shows
the debug description string of this instance.

### Text field prompts

You can set an explicit prompt on the text field to guide users on what text
they should provide. Each text field style determines where and when the text
field uses a prompt and label. For example, a form on macOS always places the
label at the leading edge of the field and uses a prompt, when available, as
placeholder text within the field itself. In the same context on iOS, the text
field uses either the prompt or label as placeholder text, depending on
whether the initializer provided a prompt.

The following example shows a `Form` with two text fields, each of which
provides a prompt to indicate that the field is required, and a view builder
to provide a label:

### Styling text fields

SwiftUI provides a default text field style that reflects an appearance and
behavior appropriate to the platform. The default style also takes the current
context into consideration, like whether the text field is in a container that
presents text fields with a special style. Beyond this, you can customize the
appearance and interaction of text fields using the `textFieldStyle(_:)`
modifier, passing in an instance of `TextFieldStyle`. The following example
applies the `roundedBorder` style to both text fields within a `VStack`.

## Topics

### Creating a text field with a string

`init(LocalizedStringKey, text: Binding<String>)`

Creates a text field with a text label generated from a localized title
string.

Available when `Label` is `Text`.

`init<S>(S, text: Binding<String>)`

Creates a text field with a text label generated from a title string.

Available when `Label` is `Text`.

`init(LocalizedStringKey, text: Binding<String>, prompt: Text?)`

Creates a text field with a text label generated from a localized title
string.

Available when `Label` is `Text`.

`init<S>(S, text: Binding<String>, prompt: Text?)`

Creates a text field with a text label generated from a title string.

Available when `Label` is `Text`.

`init(text: Binding<String>, prompt: Text?, label: () -> Label)`

Creates a text field with a prompt generated from a `Text`.

Available when `Label` conforms to `View`.

### Creating a scrollable text field

`init(LocalizedStringKey, text: Binding<String>, axis: Axis)`

Creates a text field with a preferred axis and a text label generated from a
localized title string.

Available when `Label` is `Text`.

`init<S>(S, text: Binding<String>, axis: Axis)`

Creates a text field with a preferred axis and a text label generated from a
title string.

Available when `Label` is `Text`.

`init(LocalizedStringKey, text: Binding<String>, prompt: Text?, axis: Axis)`

Creates a text field with a preferred axis and a text label generated from a
localized title string.

Available when `Label` is `Text`.

`init<S>(S, text: Binding<String>, prompt: Text?, axis: Axis)`

Creates a text field with a text label generated from a title string.

Available when `Label` is `Text`.

`init(text: Binding<String>, prompt: Text?, axis: Axis, label: () -> Label)`

Creates a text field with a preferred axis and a prompt generated from a
`Text`.

Available when `Label` conforms to `View`.

### Creating a text field with a value

Use these initializers to create a text field that binds to a value of an
arbitrary type.

`init<F>(LocalizedStringKey, value: Binding<F.FormatInput>, format: F, prompt:
Text?)`

Creates a text field that applies a format style to a bound value, with a
label generated from a localized title string.

Available when `Label` is `Text`.

`init<S, F>(S, value: Binding<F.FormatInput>, format: F, prompt: Text?)`

Creates a text field that applies a format style to a bound value, with a
label generated from a title string.

Available when `Label` is `Text`.

`init<F>(value: Binding<F.FormatInput>, format: F, prompt: Text?, label: () ->
Label)`

Creates a text field that applies a format style to a bound value, with a
label generated from a view builder.

Available when `Label` conforms to `View`.

`init<S, V>(S, value: Binding<V>, formatter: Formatter)`

Create an instance which binds over an arbitrary type, `V`.

Available when `Label` is `Text`.

`init<V>(LocalizedStringKey, value: Binding<V>, formatter: Formatter)`

Create an instance which binds over an arbitrary type, `V`.

Available when `Label` is `Text`.

`init<V>(LocalizedStringKey, value: Binding<V>, formatter: Formatter, prompt:
Text?)`

Creates a text field that applies a formatter to a bound value, with a label
generated from a localized title string.

Available when `Label` is `Text`.

`init<S, V>(S, value: Binding<V>, formatter: Formatter, prompt: Text?)`

Creates a text field that applies a formatter to a bound value, with a label
generated from a title string.

Available when `Label` is `Text`.

`init<V>(value: Binding<V>, formatter: Formatter, prompt: Text?, label: () ->
Label)`

Creates a text field that applies a formatter to a bound optional value, with
a label generated from a view builder.

Available when `Label` conforms to `View`.

### Creating a text field with an optional

Use these initializers to create a text field binds to an optional value of an
arbitrary type.

`init<F>(LocalizedStringKey, value: Binding<F.FormatInput?>, format: F,
prompt: Text?)`

Creates a text field that applies a format style to a bound optional value,
with a label generated from a localized title string.

Available when `Label` is `Text`.

`init<S, F>(S, value: Binding<F.FormatInput?>, format: F, prompt: Text?)`

Creates a text field that applies a format style to a bound optional value,
with a label generated from a title string.

Available when `Label` is `Text`.

`init<F>(value: Binding<F.FormatInput?>, format: F, prompt: Text?, label: ()
-> Label)`

Creates a text field that applies a format style to a bound optional value,
with a label generated from a view builder.

Available when `Label` conforms to `View`.

### Deprecated initializers

API Reference

Deprecated initializers

Review deprecated text field initializers.

## Relationships

### Conforms To

  * `View`

## See Also

### Getting text input

`func textFieldStyle<S>(S) -> some View`

Sets the style for text fields within this view.

`struct SecureField`

A control into which people securely enter private text.

`struct TextEditor`

A view that can display and edit long-form text.

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

Structure

# SecureField

A control into which people securely enter private text.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    struct SecureField<Label> where Label : View

## Overview

Use a secure field when you want the behavior of a `TextField`, but you want
to hide the field’s text. Typically, you use this for entering passwords and
other sensitive information, as the second field in the following screenshot
demonstrates:

  * macOS 
  * iOS 

The field:

  * Displays one dot for each character someone types.

  * Hides the dots when someone takes a screenshot in iOS.

  * Prevents anyone from cutting or copying the field’s contents.

  * Displays an indicator when Caps Lock is enabled.

### Bind to a string

A secure field binds to a string value and updates the string on every
keystroke or other edit, so you can read its value at any time from elsewhere
in your code. The following code shows how to create the above interface, with
the secure field bound to a `password` string:

The field in the above example has an `onSubmit(of:_:)` modifier that sends
the `username` and `password` strings to a custom
`handleLogin(username:password:)` method if someone presses the Return key
while the secure field has focus. You can alternatively provide another
mechanism — like a button — to do the same thing.

### Guide people with a prompt

In addition to the string or view that you provide as a label, you can also
provide a `Text` view prompt to help guide someone who uses the field, as the
following `Form` does:

The system uses the label and prompt in different ways depending on the
context. For example, a form in macOS places the label against the leading
edge of the field and uses the prompt as placeholder text inside the field.
The same form in iOS also uses the prompt as placeholder text, but doesn’t
display the label:

  * macOS 
  * iOS 

If you remove the prompt from the previous example, the field keeps the label
on the leading edge and omits the placeholder text in macOS, but displays the
label as a placeholder in iOS:

  * macOS 
  * iOS 

## Topics

### Creating a secure text field

`init(LocalizedStringKey, text: Binding<String>, prompt: Text?)`

Creates a secure field with a prompt generated from a `Text`.

Available when `Label` is `Text`.

`init<S>(S, text: Binding<String>, prompt: Text?)`

Creates a secure field with a prompt generated from a `Text`.

Available when `Label` is `Text`.

`init(text: Binding<String>, prompt: Text?, label: () -> Label)`

Creates a secure field with a prompt generated from a `Text`.

Available when `Label` conforms to `View`.

`init(LocalizedStringKey, text: Binding<String>)`

Creates a secure field with a prompt generated from a `Text`.

Available when `Label` is `Text`.

`init<S>(S, text: Binding<String>)`

Creates a secure field with a prompt generated from a `Text`.

Available when `Label` is `Text`.

### Deprecated initializers

`init(LocalizedStringKey, text: Binding<String>, onCommit: () -> Void)`

Creates an instance.

Available when `Label` is `Text`.

Deprecated

`init<S>(S, text: Binding<String>, onCommit: () -> Void)`

Creates an instance.

Available when `Label` is `Text`.

Deprecated

## Relationships

### Conforms To

  * `View`

## See Also

### Getting text input

`struct TextField`

A control that displays an editable text interface.

`func textFieldStyle<S>(S) -> some View`

Sets the style for text fields within this view.

`struct TextEditor`

A view that can display and edit long-form text.

Structure

# TextEditor

A view that can display and edit long-form text.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    struct TextEditor

## Overview

A text editor view allows you to display and edit multiline, scrollable text
in your app’s user interface. By default, the text editor view styles the text
using characteristics inherited from the environment, like `font(_:)`,
`foregroundColor(_:)`, and `multilineTextAlignment(_:)`.

You create a text editor by adding a `TextEditor` instance to the body of your
view, and initialize it by passing in a `Binding` to a string variable in your
app:

To style the text, use the standard view modifiers to configure a system font,
set a custom font, or change the color of the view’s text.

In this example, the view renders the editor’s text in gray with a custom
font:

If you want to change the spacing or font scaling aspects of the text, you can
use modifiers like `lineLimit(_:)`, `lineSpacing(_:)`, and
`minimumScaleFactor(_:)` to configure how the view displays text depending on
the space constraints. For example, here the `lineSpacing(_:)` modifier sets
the spacing between lines to 5 points:

## Topics

### Creating a text editor

`init(text: Binding<String>)`

Creates a plain text editor.

## Relationships

### Conforms To

  * `View`

## See Also

### Getting text input

`struct TextField`

A control that displays an editable text interface.

`func textFieldStyle<S>(S) -> some View`

Sets the style for text fields within this view.

`struct SecureField`

A control into which people securely enter private text.

Instance Method

# textSelection(_:)

Controls whether people can select text within this view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    func textSelection<S>(_ selectability: S) -> some View where S : TextSelectability
    

## Discussion

People sometimes need to copy useful information from `Text` views — including
error messages, serial numbers, or IP addresses — so they can then paste the
text into another context. Enable text selection to let people select text in
a platform-appropriate way.

You can apply this method to an individual text view, or to a container to
make each contained text view selectable. In the following example, the person
using the app can select text that shows the date of an event or the name or
email of any of the event participants:

On macOS, people use the mouse or trackpad to select a range of text, which
they can quickly copy by choosing Edit > Copy, or with the standard keyboard
shortcut.

On iOS, the person using the app touches and holds on a selectable `Text`
view, which brings up a system menu with menu items appropriate for the
current context. These menu items operate on the entire contents of the `Text`
view; the person can’t select a range of text like they can on macOS.

Note

`Button` views don’t support text selection.

## See Also

### Selecting text

`protocol TextSelectability`

A type that describes the ability to select text.

Protocol

# TextSelectability

A type that describes the ability to select text.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    protocol TextSelectability

## Overview

To configure whether people can select text in your app, use the
`textSelection(_:)` modifier, passing in a text selectability value like
`enabled` or `disabled`.

## Topics

### Getting selectability options

`static var enabled: EnabledTextSelectability`

A selectability value that enables text selection by a person using your app.

Available when `Self` is `EnabledTextSelectability`.

`static var disabled: DisabledTextSelectability`

A selectability value that disables text selection by the person using your
app.

Available when `Self` is `DisabledTextSelectability`.

### Specifying selectability

`static var allowsSelection: Bool`

A Boolean value that indicates whether the selectability type allows
selection.

**Required**

### Supporting types

`struct EnabledTextSelectability`

A selectability type that enables text selection by the person using your app.

`struct DisabledTextSelectability`

A selectability type that disables text selection by the person using your
app.

## Relationships

### Conforming Types

  * `DisabledTextSelectability`
  * `EnabledTextSelectability`

## See Also

### Selecting text

`func textSelection<S>(S) -> some View`

Controls whether people can select text within this view.

Article

# Applying custom fonts to text

Add and use a font in your app that scales with Dynamic Type.

## Overview

SwiftUI supports styling text views using the built-in fonts, and uses a
system font by default. Rather than using a system-provided font, you can use
custom fonts by including the font files in your Xcode project. To use a
custom font, add the font file that contains your licensed font to your app,
and then apply the font to a text view or set it as a default font within a
container view. SwiftUI’s adaptive text display scales the font automtically
using Dynamic Type.

Dynamic Type allows users to choose the size of textual content displayed
onscreen. It helps users who need larger text for better readability and
accommodates those who can read smaller text, allowing more information to
appear onscreen.

### Add the font files to the project

To add the font files to your Xcode project:

  1. In Xcode, select the Project navigator.

  2. Drag your fonts from a Finder window into your project. This copies the fonts to your project.

  3. Select the font or folder with the fonts, and verify that the files show their target membership checked for your app’s targets.

### Identify the font files to include in the app bundle

For iOS, watchOS, tvOS, or Mac Catalyst targets, add the `UIAppFonts` key to
your app’s `Info.plist` file. For the key’s value, provide an array of strings
containing the relative paths to any added font files. For a macOS app target,
use the `ATSApplicationFontsPath` key in your target’s `Info.plist` file, and
provide the name of the folder that holds the fonts as the value for that key.

In the following example, the font file is inside the `project_fonts`
directory, so you use `project_fonts/MyFont.ttf` as the string value in the
`Info.plist` file.

### Apply a font supporting dynamic sizing

Use the `custom(_:size:)` method to retrieve an instance of your font and
apply it to a text view with the `font(_:)` modifier. When retrieving the font
with `custom(_:size:)`, match the name of the font with the font’s PostScript
name. You can find the postscript name of a font by opening it with the Font
Book app and selecting the Font Info tab. If SwiftUI can’t retrieve and apply
your font, it renders the text view with the default system font instead.

The following example applies the font `MyFont` to a text view:

The font scales adaptively from the size provided to align with the default
text style of `body`. Use the `relativeTo` parameter to specify a text style
to scale with other than the default of `body`. For example, to set the font
size to `32` points and adaptively scale relative to the text style of
`title`:

SwiftUI doesn’t synthesize bold or italic styling for fonts. If the font
supports weighted or italic variants, you can customize the typography of the
text view by styling the font using the `weight(_:)` or `italic()` modifiers.

For design guidance on choosing fonts to enhance your app on your target
platform, see the Human Interface Guidelines > Typography for iOS, macOS,
watchOS, or tvOS.

### Scale padding using scaled metric

The `ScaledMetric` property wrapper on a view property provides a scaled value
that changes automatically with accessibility settings. When working with
adpatively sized fonts, you can scale the spacing between or around the text
to improve the visual design with this property wrapper.

The following example uses `@ScaledMetric` to scale the padding value
surrounding a text view relative to the `body` text style, with a blue border
added to identify the spacing that padding adds:

The preview shows the following image without any accessibility settings
turned on:

Use the `environment(_:_:)` modifier to set the accessibility size category on
the preview to `ContentSizeCategory.accessibilityLarge`:

The preview then shows the following image that reflects the increased
accessibility size and the scaled padding:

## See Also

### Setting a font

`func font(Font?) -> some View`

Sets the default font for text in this view.

`func fontDesign(Font.Design?) -> some View`

Sets the font design of the text in this view.

`func fontWeight(Font.Weight?) -> some View`

Sets the font weight of the text in this view.

`func fontWidth(Font.Width?) -> some View`

Sets the font width of the text in this view.

`var font: Font?`

The default font of this environment.

`struct Font`

An environment-dependent font.

Instance Method

# font(_:)

Sets the default font for text in this view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func font(_ font: Font?) -> some View
    

##  Parameters

`font`

    

The default font to use in this view.

## Return Value

A view with the default font set to the value you supply.

## Discussion

Use `font(_:)` to apply a specific font to all of the text in a view.

The example below shows the effects of applying fonts to individual views and
to view hierarchies. Font information flows down the view hierarchy as part of
the environment, and remains in effect unless overridden at the level of an
individual view or view container.

Here, the outermost `VStack` applies a 16-point system font as a default font
to views contained in that `VStack`. Inside that stack, the example applies a
`largeTitle` font to just the first text view; this explicitly overrides the
default. The remaining stack and the views contained with it continue to use
the 16-point system font set by their containing view:

## See Also

### Setting a font

Applying custom fonts to text

Add and use a font in your app that scales with Dynamic Type.

`func fontDesign(Font.Design?) -> some View`

Sets the font design of the text in this view.

`func fontWeight(Font.Weight?) -> some View`

Sets the font weight of the text in this view.

`func fontWidth(Font.Width?) -> some View`

Sets the font width of the text in this view.

`var font: Font?`

The default font of this environment.

`struct Font`

An environment-dependent font.

Instance Method

# fontDesign(_:)

Sets the font design of the text in this view.

iOS 16.1+  iPadOS 16.1+  macOS 13.0+  Mac Catalyst 16.1+  tvOS 16.1+  watchOS
9.1+  visionOS 1.0+

    
    
    func fontDesign(_ design: Font.Design?) -> some View
    

##  Parameters

`design`

    

One of the available font designs. Providing `nil` removes the effect of any
font design modifier applied higher in the view hierarchy.

## Return Value

A view that uses the font design you specify.

## See Also

### Setting a font

Applying custom fonts to text

Add and use a font in your app that scales with Dynamic Type.

`func font(Font?) -> some View`

Sets the default font for text in this view.

`func fontWeight(Font.Weight?) -> some View`

Sets the font weight of the text in this view.

`func fontWidth(Font.Width?) -> some View`

Sets the font width of the text in this view.

`var font: Font?`

The default font of this environment.

`struct Font`

An environment-dependent font.

Instance Method

# fontWeight(_:)

Sets the font weight of the text in this view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func fontWeight(_ weight: Font.Weight?) -> some View
    

##  Parameters

`weight`

    

One of the available font weights. Providing `nil` removes the effect of any
font weight modifier applied higher in the view hierarchy.

## Return Value

A view that uses the font weight you specify.

## See Also

### Setting a font

Applying custom fonts to text

Add and use a font in your app that scales with Dynamic Type.

`func font(Font?) -> some View`

Sets the default font for text in this view.

`func fontDesign(Font.Design?) -> some View`

Sets the font design of the text in this view.

`func fontWidth(Font.Width?) -> some View`

Sets the font width of the text in this view.

`var font: Font?`

The default font of this environment.

`struct Font`

An environment-dependent font.

Instance Method

# fontWidth(_:)

Sets the font width of the text in this view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func fontWidth(_ width: Font.Width?) -> some View
    

##  Parameters

`width`

    

One of the available font widths. Providing `nil` removes the effect of any
font width modifier applied higher in the view hierarchy.

## Return Value

A view that uses the font width you specify.

## See Also

### Setting a font

Applying custom fonts to text

Add and use a font in your app that scales with Dynamic Type.

`func font(Font?) -> some View`

Sets the default font for text in this view.

`func fontDesign(Font.Design?) -> some View`

Sets the font design of the text in this view.

`func fontWeight(Font.Weight?) -> some View`

Sets the font weight of the text in this view.

`var font: Font?`

The default font of this environment.

`struct Font`

An environment-dependent font.

Instance Property

# font

The default font of this environment.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var font: Font? { get set }

## See Also

### Setting a font

Applying custom fonts to text

Add and use a font in your app that scales with Dynamic Type.

`func font(Font?) -> some View`

Sets the default font for text in this view.

`func fontDesign(Font.Design?) -> some View`

Sets the font design of the text in this view.

`func fontWeight(Font.Weight?) -> some View`

Sets the font weight of the text in this view.

`func fontWidth(Font.Width?) -> some View`

Sets the font width of the text in this view.

`struct Font`

An environment-dependent font.

Structure

# Font

An environment-dependent font.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct Font

## Overview

The system resolves a font’s value at the time it uses the font in a given
environment because `Font` is a late-binding token.

## Topics

### Getting standard fonts

`static let extraLargeTitle2: Font`

Create a font with the second level extra large title text style.

`static let extraLargeTitle: Font`

Create a font with the extra large title text style.

`static let largeTitle: Font`

A font with the large title text style.

`static let title: Font`

A font with the title text style.

`static let title2: Font`

Create a font for second level hierarchical headings.

`static let title3: Font`

Create a font for third level hierarchical headings.

`static let headline: Font`

A font with the headline text style.

`static let subheadline: Font`

A font with the subheadline text style.

`static let body: Font`

A font with the body text style.

`static let callout: Font`

A font with the callout text style.

`static let caption: Font`

A font with the caption text style.

`static let caption2: Font`

Create a font with the alternate caption text style.

`static let footnote: Font`

A font with the footnote text style.

### Getting system fonts

`static func system(Font.TextStyle, design: Font.Design?, weight:
Font.Weight?) -> Font`

Gets a system font that uses the specified style, design, and weight.

`static func system(size: CGFloat, weight: Font.Weight?, design: Font.Design?)
-> Font`

Specifies a system font to use, along with the style, weight, and any design
parameters you want applied to the text.

`enum Design`

A design to use for fonts.

`enum TextStyle`

A dynamic text style to use for fonts.

`struct Weight`

A weight to use for fonts.

### Creating custom fonts

`static func custom(String, fixedSize: CGFloat) -> Font`

Create a custom font with the given `name` and a fixed `size` that does not
scale with Dynamic Type.

`static func custom(String, size: CGFloat, relativeTo: Font.TextStyle) ->
Font`

Create a custom font with the given `name` and `size` that scales relative to
the given `textStyle`.

`static func custom(String, size: CGFloat) -> Font`

Create a custom font with the given `name` and `size` that scales with the
body text style.

### Getting a font from another font

`init(CTFont)`

Creates a custom font from a platform font instance.

### Styling a font

`func bold() -> Font`

Adds bold styling to the font.

`func italic() -> Font`

Adds italics to the font.

`func monospaced() -> Font`

Returns a fixed-width font from the same family as the base font.

`func monospacedDigit() -> Font`

Returns a modified font that uses fixed-width digits, while leaving other
characters proportionally spaced.

`func smallCaps() -> Font`

Adjusts the font to enable all small capitals.

`func lowercaseSmallCaps() -> Font`

Adjusts the font to enable lowercase small capitals.

`func uppercaseSmallCaps() -> Font`

Adjusts the font to enable uppercase small capitals.

`func weight(Font.Weight) -> Font`

Sets the weight of the font.

`func width(Font.Width) -> Font`

Sets the width of the font.

`struct Width`

A width to use for fonts that have multiple widths.

`func leading(Font.Leading) -> Font`

Adjusts the line spacing of a font.

`enum Leading`

A line spacing adjustment that you can apply to a font.

### Deprecated symbols

`static func system(Font.TextStyle, design: Font.Design) -> Font`

Gets a system font with the given text style and design.

Deprecated

`static func system(size: CGFloat, weight: Font.Weight, design: Font.Design)
-> Font`

Specifies a system font to use, along with the style, weight, and any design
parameters you want applied to the text.

Deprecated

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Setting a font

Applying custom fonts to text

Add and use a font in your app that scales with Dynamic Type.

`func font(Font?) -> some View`

Sets the default font for text in this view.

`func fontDesign(Font.Design?) -> some View`

Sets the font design of the text in this view.

`func fontWeight(Font.Weight?) -> some View`

Sets the font weight of the text in this view.

`func fontWidth(Font.Width?) -> some View`

Sets the font width of the text in this view.

`var font: Font?`

The default font of this environment.

Instance Method

# textScale(_:isEnabled:)

Applies a text scale to text in the view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func textScale(
        _ scale: Text.Scale,
        isEnabled: Bool = true
    ) -> some View
    

##  Parameters

`scale`

    

The text scale to apply.

`isEnabled`

    

If true the text scale is applied; otherwise text scale is unchanged.

## Return Value

A view with the specified text scale applied.

## See Also

### Adjusting text size

`func dynamicTypeSize<T>(T) -> some View`

Limits the Dynamic Type size within the view to the given range.

`func dynamicTypeSize(DynamicTypeSize) -> some View`

Sets the Dynamic Type size within the view to the given value.

`var dynamicTypeSize: DynamicTypeSize`

The current Dynamic Type size.

`enum DynamicTypeSize`

A Dynamic Type size, which specifies how large scalable content should be.

`struct ScaledMetric`

A dynamic property that scales a numeric value.

Instance Method

# dynamicTypeSize(_:)

Limits the Dynamic Type size within the view to the given range.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func dynamicTypeSize<T>(_ range: T) -> some View where T : RangeExpression, T.Bound == DynamicTypeSize
    

##  Parameters

`range`

    

The range of sizes that are allowed in this view.

## Return Value

A view that constrains the Dynamic Type size of this view within the specified
`range`.

## Discussion

As an example, you can constrain the maximum Dynamic Type size in
`ContentView` to be no larger than `DynamicTypeSize.large`:

If the Dynamic Type size is limited to multiple ranges, the result is their
intersection:

A specific Dynamic Type size can still be set after a range is applied:

When limiting the Dynamic Type size, consider if adding a large content view
with `accessibilityShowsLargeContentViewer()` would be appropriate.

## See Also

### Adjusting text size

`func textScale(Text.Scale, isEnabled: Bool) -> some View`

Applies a text scale to text in the view.

`func dynamicTypeSize(DynamicTypeSize) -> some View`

Sets the Dynamic Type size within the view to the given value.

`var dynamicTypeSize: DynamicTypeSize`

The current Dynamic Type size.

`enum DynamicTypeSize`

A Dynamic Type size, which specifies how large scalable content should be.

`struct ScaledMetric`

A dynamic property that scales a numeric value.

Instance Method

# dynamicTypeSize(_:)

Sets the Dynamic Type size within the view to the given value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func dynamicTypeSize(_ size: DynamicTypeSize) -> some View
    

##  Parameters

`size`

    

The size to set for this view.

## Return Value

A view that sets the Dynamic Type size to the specified `size`.

## Discussion

As an example, you can set a Dynamic Type size in `ContentView` to be
`DynamicTypeSize.xLarge` (this can be useful in previews to see your content
at a different size) like this:

If a Dynamic Type size range is applied after setting a value, the value is
limited by that range:

When limiting the Dynamic Type size, consider if adding a large content view
with `accessibilityShowsLargeContentViewer()` would be appropriate.

## See Also

### Adjusting text size

`func textScale(Text.Scale, isEnabled: Bool) -> some View`

Applies a text scale to text in the view.

`func dynamicTypeSize<T>(T) -> some View`

Limits the Dynamic Type size within the view to the given range.

`var dynamicTypeSize: DynamicTypeSize`

The current Dynamic Type size.

`enum DynamicTypeSize`

A Dynamic Type size, which specifies how large scalable content should be.

`struct ScaledMetric`

A dynamic property that scales a numeric value.

Instance Property

# dynamicTypeSize

The current Dynamic Type size.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var dynamicTypeSize: DynamicTypeSize { get set }

## Discussion

This value changes as the user’s chosen Dynamic Type size changes. The default
value is device-dependent.

When limiting the Dynamic Type size, consider if adding a large content view
with `accessibilityShowsLargeContentViewer()` would be appropriate.

On macOS, this value cannot be changed by users and does not affect the text
size.

## See Also

### Adjusting text size

`func textScale(Text.Scale, isEnabled: Bool) -> some View`

Applies a text scale to text in the view.

`func dynamicTypeSize<T>(T) -> some View`

Limits the Dynamic Type size within the view to the given range.

`func dynamicTypeSize(DynamicTypeSize) -> some View`

Sets the Dynamic Type size within the view to the given value.

`enum DynamicTypeSize`

A Dynamic Type size, which specifies how large scalable content should be.

`struct ScaledMetric`

A dynamic property that scales a numeric value.

Enumeration

# DynamicTypeSize

A Dynamic Type size, which specifies how large scalable content should be.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    enum DynamicTypeSize

## Overview

For more information, see Typography in the Human Interface Guidelines.

## Topics

### Getting type sizes

`case xSmall`

An extra small size.

`case small`

A small size.

`case medium`

A medium size.

`case large`

A large size.

`case xLarge`

An extra large size.

`case xxLarge`

An extra extra large size.

`case xxxLarge`

An extra extra extra large size.

### Getting accessibility type sizes

`case accessibility1`

The first accessibility size.

`case accessibility2`

The second accessibility size.

`case accessibility3`

The third accessibility size.

`case accessibility4`

The fourth accessibility size.

`case accessibility5`

The fifth accessibility size.

`var isAccessibilitySize: Bool`

A Boolean value indicating whether the size is one that is associated with
accessibility.

### Creating a type size

`init?(UIContentSizeCategory)`

Create a Dynamic Type size from its `UIContentSizeCategory` equivalent.

## Relationships

### Conforms To

  * `CaseIterable`
  * `Comparable`
  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Adjusting text size

`func textScale(Text.Scale, isEnabled: Bool) -> some View`

Applies a text scale to text in the view.

`func dynamicTypeSize<T>(T) -> some View`

Limits the Dynamic Type size within the view to the given range.

`func dynamicTypeSize(DynamicTypeSize) -> some View`

Sets the Dynamic Type size within the view to the given value.

`var dynamicTypeSize: DynamicTypeSize`

The current Dynamic Type size.

`struct ScaledMetric`

A dynamic property that scales a numeric value.

Structure

# ScaledMetric

A dynamic property that scales a numeric value.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    @propertyWrapper
    struct ScaledMetric<Value> where Value : BinaryFloatingPoint

## Topics

### Creating the metric

`init(wrappedValue: Value)`

Creates the scaled metric with an unscaled value using the default scaling.

`init(wrappedValue: Value, relativeTo: Font.TextStyle)`

Creates the scaled metric with an unscaled value and a text style to scale
relative to.

### Getting the metric

`var wrappedValue: Value`

The value scaled based on the current environment.

## Relationships

### Conforms To

  * `DynamicProperty`

## See Also

### Adjusting text size

`func textScale(Text.Scale, isEnabled: Bool) -> some View`

Applies a text scale to text in the view.

`func dynamicTypeSize<T>(T) -> some View`

Limits the Dynamic Type size within the view to the given range.

`func dynamicTypeSize(DynamicTypeSize) -> some View`

Sets the Dynamic Type size within the view to the given value.

`var dynamicTypeSize: DynamicTypeSize`

The current Dynamic Type size.

`enum DynamicTypeSize`

A Dynamic Type size, which specifies how large scalable content should be.

Instance Method

# bold(_:)

Applies a bold font weight to the text in this view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func bold(_ isActive: Bool = true) -> some View
    

##  Parameters

`isActive`

    

A Boolean value that indicates whether bold font styling is added. The default
value is `true`.

## Return Value

A view with bold text.

## See Also

### Controlling text style

`func italic(Bool) -> some View`

Applies italics to the text in this view.

`func underline(Bool, pattern: Text.LineStyle.Pattern, color: Color?) -> some
View`

Applies an underline to the text in this view.

`func strikethrough(Bool, pattern: Text.LineStyle.Pattern, color: Color?) ->
some View`

Applies a strikethrough to the text in this view.

`func textCase(Text.Case?) -> some View`

Sets a transform for the case of the text contained in this view when
displayed.

`var textCase: Text.Case?`

A stylistic override to transform the case of `Text` when displayed, using the
environment’s locale.

`func monospaced(Bool) -> some View`

Modifies the fonts of all child views to use the fixed-width variant of the
current font, if possible.

`func monospacedDigit() -> some View`

Modifies the fonts of all child views to use fixed-width digits, if possible,
while leaving other characters proportionally spaced.

Instance Method

# italic(_:)

Applies italics to the text in this view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func italic(_ isActive: Bool = true) -> some View
    

##  Parameters

`isActive`

    

A Boolean value that indicates whether italic styling is added. The default
value is `true`.

## Return Value

A View with italic text.

## See Also

### Controlling text style

`func bold(Bool) -> some View`

Applies a bold font weight to the text in this view.

`func underline(Bool, pattern: Text.LineStyle.Pattern, color: Color?) -> some
View`

Applies an underline to the text in this view.

`func strikethrough(Bool, pattern: Text.LineStyle.Pattern, color: Color?) ->
some View`

Applies a strikethrough to the text in this view.

`func textCase(Text.Case?) -> some View`

Sets a transform for the case of the text contained in this view when
displayed.

`var textCase: Text.Case?`

A stylistic override to transform the case of `Text` when displayed, using the
environment’s locale.

`func monospaced(Bool) -> some View`

Modifies the fonts of all child views to use the fixed-width variant of the
current font, if possible.

`func monospacedDigit() -> some View`

Modifies the fonts of all child views to use fixed-width digits, if possible,
while leaving other characters proportionally spaced.

Instance Method

# underline(_:pattern:color:)

Applies an underline to the text in this view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func underline(
        _ isActive: Bool = true,
        pattern: Text.LineStyle.Pattern = .solid,
        color: Color? = nil
    ) -> some View
    

##  Parameters

`isActive`

    

A Boolean value that indicates whether underline is added. The default value
is `true`.

`pattern`

    

The pattern of the line. The default value is `solid`.

`color`

    

The color of the underline. If `color` is `nil`, the underline uses the
default foreground color.

## Return Value

A view where text has a line running along its baseline.

## See Also

### Controlling text style

`func bold(Bool) -> some View`

Applies a bold font weight to the text in this view.

`func italic(Bool) -> some View`

Applies italics to the text in this view.

`func strikethrough(Bool, pattern: Text.LineStyle.Pattern, color: Color?) ->
some View`

Applies a strikethrough to the text in this view.

`func textCase(Text.Case?) -> some View`

Sets a transform for the case of the text contained in this view when
displayed.

`var textCase: Text.Case?`

A stylistic override to transform the case of `Text` when displayed, using the
environment’s locale.

`func monospaced(Bool) -> some View`

Modifies the fonts of all child views to use the fixed-width variant of the
current font, if possible.

`func monospacedDigit() -> some View`

Modifies the fonts of all child views to use fixed-width digits, if possible,
while leaving other characters proportionally spaced.

Instance Method

# strikethrough(_:pattern:color:)

Applies a strikethrough to the text in this view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func strikethrough(
        _ isActive: Bool = true,
        pattern: Text.LineStyle.Pattern = .solid,
        color: Color? = nil
    ) -> some View
    

##  Parameters

`isActive`

    

A Boolean value that indicates whether strikethrough is added. The default
value is `true`.

`pattern`

    

The pattern of the line. The default value is `solid`.

`color`

    

The color of the strikethrough. If `color` is `nil`, the strikethrough uses
the default foreground color.

## Return Value

A view where text has a line through its center.

## See Also

### Controlling text style

`func bold(Bool) -> some View`

Applies a bold font weight to the text in this view.

`func italic(Bool) -> some View`

Applies italics to the text in this view.

`func underline(Bool, pattern: Text.LineStyle.Pattern, color: Color?) -> some
View`

Applies an underline to the text in this view.

`func textCase(Text.Case?) -> some View`

Sets a transform for the case of the text contained in this view when
displayed.

`var textCase: Text.Case?`

A stylistic override to transform the case of `Text` when displayed, using the
environment’s locale.

`func monospaced(Bool) -> some View`

Modifies the fonts of all child views to use the fixed-width variant of the
current font, if possible.

`func monospacedDigit() -> some View`

Modifies the fonts of all child views to use fixed-width digits, if possible,
while leaving other characters proportionally spaced.

Instance Method

# textCase(_:)

Sets a transform for the case of the text contained in this view when
displayed.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func textCase(_ textCase: Text.Case?) -> some View
    

##  Parameters

`textCase`

    

One of the `Text.Case` enumerations; the default is `nil`.

## Return Value

A view that transforms the case of the text.

## Discussion

The default value is `nil`, displaying the text without any case changes.

## See Also

### Controlling text style

`func bold(Bool) -> some View`

Applies a bold font weight to the text in this view.

`func italic(Bool) -> some View`

Applies italics to the text in this view.

`func underline(Bool, pattern: Text.LineStyle.Pattern, color: Color?) -> some
View`

Applies an underline to the text in this view.

`func strikethrough(Bool, pattern: Text.LineStyle.Pattern, color: Color?) ->
some View`

Applies a strikethrough to the text in this view.

`var textCase: Text.Case?`

A stylistic override to transform the case of `Text` when displayed, using the
environment’s locale.

`func monospaced(Bool) -> some View`

Modifies the fonts of all child views to use the fixed-width variant of the
current font, if possible.

`func monospacedDigit() -> some View`

Modifies the fonts of all child views to use fixed-width digits, if possible,
while leaving other characters proportionally spaced.

Instance Property

# textCase

A stylistic override to transform the case of `Text` when displayed, using the
environment’s locale.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    var textCase: Text.Case? { get set }

## Discussion

The default value is `nil`, displaying the `Text` without any case changes.

## See Also

### Controlling text style

`func bold(Bool) -> some View`

Applies a bold font weight to the text in this view.

`func italic(Bool) -> some View`

Applies italics to the text in this view.

`func underline(Bool, pattern: Text.LineStyle.Pattern, color: Color?) -> some
View`

Applies an underline to the text in this view.

`func strikethrough(Bool, pattern: Text.LineStyle.Pattern, color: Color?) ->
some View`

Applies a strikethrough to the text in this view.

`func textCase(Text.Case?) -> some View`

Sets a transform for the case of the text contained in this view when
displayed.

`func monospaced(Bool) -> some View`

Modifies the fonts of all child views to use the fixed-width variant of the
current font, if possible.

`func monospacedDigit() -> some View`

Modifies the fonts of all child views to use fixed-width digits, if possible,
while leaving other characters proportionally spaced.

Instance Method

# monospaced(_:)

Modifies the fonts of all child views to use the fixed-width variant of the
current font, if possible.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func monospaced(_ isActive: Bool = true) -> some View
    

## Return Value

A view whose child views’ fonts use fixed-width characters, while leaving
other characters proportionally spaced.

## Discussion

If a child view’s base font doesn’t support fixed-width, the font remains
unchanged.

## See Also

### Controlling text style

`func bold(Bool) -> some View`

Applies a bold font weight to the text in this view.

`func italic(Bool) -> some View`

Applies italics to the text in this view.

`func underline(Bool, pattern: Text.LineStyle.Pattern, color: Color?) -> some
View`

Applies an underline to the text in this view.

`func strikethrough(Bool, pattern: Text.LineStyle.Pattern, color: Color?) ->
some View`

Applies a strikethrough to the text in this view.

`func textCase(Text.Case?) -> some View`

Sets a transform for the case of the text contained in this view when
displayed.

`var textCase: Text.Case?`

A stylistic override to transform the case of `Text` when displayed, using the
environment’s locale.

`func monospacedDigit() -> some View`

Modifies the fonts of all child views to use fixed-width digits, if possible,
while leaving other characters proportionally spaced.

Instance Method

# monospacedDigit()

Modifies the fonts of all child views to use fixed-width digits, if possible,
while leaving other characters proportionally spaced.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func monospacedDigit() -> some View
    

## Return Value

A view whose child views’ fonts use fixed-width numeric characters, while
leaving other characters proportionally spaced.

## Discussion

Using fixed-width digits allows you to easily align numbers of the same size
in a table-like arrangement. This feature is also known as “tabular figures”
or “tabular numbers.”

This modifier only affects numeric characters, and leaves all other characters
unchanged.

The following example shows the effect of `monospacedDigit()` on multiple
child views. The example consists of two `VStack` views inside an `HStack`.
Each `VStack` contains two `Button` views, with the second `VStack` applying
the `monospacedDigit()` modifier to its contents. As a result, the digits in
the buttons in the trailing `VStack` are the same width, which in turn gives
the buttons equal widths.

If a child view’s base font doesn’t support fixed-width digits, the font
remains unchanged.

## See Also

### Controlling text style

`func bold(Bool) -> some View`

Applies a bold font weight to the text in this view.

`func italic(Bool) -> some View`

Applies italics to the text in this view.

`func underline(Bool, pattern: Text.LineStyle.Pattern, color: Color?) -> some
View`

Applies an underline to the text in this view.

`func strikethrough(Bool, pattern: Text.LineStyle.Pattern, color: Color?) ->
some View`

Applies a strikethrough to the text in this view.

`func textCase(Text.Case?) -> some View`

Sets a transform for the case of the text contained in this view when
displayed.

`var textCase: Text.Case?`

A stylistic override to transform the case of `Text` when displayed, using the
environment’s locale.

`func monospaced(Bool) -> some View`

Modifies the fonts of all child views to use the fixed-width variant of the
current font, if possible.

Instance Method

# truncationMode(_:)

Sets the truncation mode for lines of text that are too long to fit in the
available space.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func truncationMode(_ mode: Text.TruncationMode) -> some View
    

##  Parameters

`mode`

    

The truncation mode that specifies where to truncate the text within the text
view, if needed. You can truncate at the beginning, middle, or end of the text
view.

## Return Value

A view that truncates text at different points in a line depending on the mode
you select.

## Discussion

Use the `truncationMode(_:)` modifier to determine whether text in a long line
is truncated at the beginning, middle, or end. Truncation is indicated by
adding an ellipsis (…) to the line when removing text to indicate to readers
that text is missing.

In the example below, the bounds of text view constrains the amount of text
that the view displays and the `truncationMode(_:)` specifies from which
direction and where to display the truncation indicator:

## See Also

### Managing text layout

`var truncationMode: Text.TruncationMode`

A value that indicates how the layout truncates the last line of text to fit
into the available space.

`func allowsTightening(Bool) -> some View`

Sets whether text in this view can compress the space between characters when
necessary to fit text in a line.

`var allowsTightening: Bool`

A Boolean value that indicates whether inter-character spacing should tighten
to fit the text into the available space.

`func minimumScaleFactor(CGFloat) -> some View`

Sets the minimum amount that text in this view scales down to fit in the
available space.

`var minimumScaleFactor: CGFloat`

The minimum permissible proportion to shrink the font size to fit the text
into the available space.

`func baselineOffset(CGFloat) -> some View`

Sets the vertical offset for the text relative to its baseline in this view.

`func kerning(CGFloat) -> some View`

Sets the spacing, or kerning, between characters for the text in this view.

`func tracking(CGFloat) -> some View`

Sets the tracking for the text in this view.

`func flipsForRightToLeftLayoutDirection(Bool) -> some View`

Sets whether this view mirrors its contents horizontally when the layout
direction is right-to-left.

`enum TextAlignment`

An alignment position for text along the horizontal axis.

Instance Property

# truncationMode

A value that indicates how the layout truncates the last line of text to fit
into the available space.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var truncationMode: Text.TruncationMode { get set }

## Discussion

The default value is `Text.TruncationMode.tail`. Some controls, however, might
have a different default if appropriate.

## See Also

### Managing text layout

`func truncationMode(Text.TruncationMode) -> some View`

Sets the truncation mode for lines of text that are too long to fit in the
available space.

`func allowsTightening(Bool) -> some View`

Sets whether text in this view can compress the space between characters when
necessary to fit text in a line.

`var allowsTightening: Bool`

A Boolean value that indicates whether inter-character spacing should tighten
to fit the text into the available space.

`func minimumScaleFactor(CGFloat) -> some View`

Sets the minimum amount that text in this view scales down to fit in the
available space.

`var minimumScaleFactor: CGFloat`

The minimum permissible proportion to shrink the font size to fit the text
into the available space.

`func baselineOffset(CGFloat) -> some View`

Sets the vertical offset for the text relative to its baseline in this view.

`func kerning(CGFloat) -> some View`

Sets the spacing, or kerning, between characters for the text in this view.

`func tracking(CGFloat) -> some View`

Sets the tracking for the text in this view.

`func flipsForRightToLeftLayoutDirection(Bool) -> some View`

Sets whether this view mirrors its contents horizontally when the layout
direction is right-to-left.

`enum TextAlignment`

An alignment position for text along the horizontal axis.

Instance Method

# allowsTightening(_:)

Sets whether text in this view can compress the space between characters when
necessary to fit text in a line.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func allowsTightening(_ flag: Bool) -> some View
    

##  Parameters

`flag`

    

A Boolean value that indicates whether the space between characters compresses
when necessary.

## Return Value

A view that can compress the space between characters when necessary to fit
text in a line.

## Discussion

Use `allowsTightening(_:)` to enable the compression of inter-character
spacing of text in a view to try to fit the text in the view’s bounds.

In the example below, two identically configured text views show the effects
of `allowsTightening(_:)` on the compression of the spacing between
characters:

## See Also

### Controlling hit testing

`func contentShape<S>(S, eoFill: Bool) -> some View`

Defines the content shape for hit testing.

`func contentShape<S>(ContentShapeKinds, S, eoFill: Bool) -> some View`

Sets the content shape for this view.

`struct ContentShapeKinds`

A kind for the content shape of a view.

Instance Property

# allowsTightening

A Boolean value that indicates whether inter-character spacing should tighten
to fit the text into the available space.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var allowsTightening: Bool { get set }

## Discussion

The default value is `false`.

## See Also

### Managing text layout

`func truncationMode(Text.TruncationMode) -> some View`

Sets the truncation mode for lines of text that are too long to fit in the
available space.

`var truncationMode: Text.TruncationMode`

A value that indicates how the layout truncates the last line of text to fit
into the available space.

`func allowsTightening(Bool) -> some View`

Sets whether text in this view can compress the space between characters when
necessary to fit text in a line.

`func minimumScaleFactor(CGFloat) -> some View`

Sets the minimum amount that text in this view scales down to fit in the
available space.

`var minimumScaleFactor: CGFloat`

The minimum permissible proportion to shrink the font size to fit the text
into the available space.

`func baselineOffset(CGFloat) -> some View`

Sets the vertical offset for the text relative to its baseline in this view.

`func kerning(CGFloat) -> some View`

Sets the spacing, or kerning, between characters for the text in this view.

`func tracking(CGFloat) -> some View`

Sets the tracking for the text in this view.

`func flipsForRightToLeftLayoutDirection(Bool) -> some View`

Sets whether this view mirrors its contents horizontally when the layout
direction is right-to-left.

`enum TextAlignment`

An alignment position for text along the horizontal axis.

Instance Method

# minimumScaleFactor(_:)

Sets the minimum amount that text in this view scales down to fit in the
available space.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func minimumScaleFactor(_ factor: CGFloat) -> some View
    

##  Parameters

`factor`

    

A fraction between 0 and 1 (inclusive) you use to specify the minimum amount
of text scaling that this view permits.

## Return Value

A view that limits the amount of text downscaling.

## Discussion

Use the `minimumScaleFactor(_:)` modifier if the text you place in a view
doesn’t fit and it’s okay if the text shrinks to accommodate. For example, a
label with a minimum scale factor of `0.5` draws its text in a font size as
small as half of the actual font if needed.

In the example below, the `HStack` contains a `Text` label with a line limit
of `1`, that is next to a `TextField`. To allow the label to fit into the
available space, the `minimumScaleFactor(_:)` modifier shrinks the text as
needed to fit into the available space.

## See Also

### Managing text layout

`func truncationMode(Text.TruncationMode) -> some View`

Sets the truncation mode for lines of text that are too long to fit in the
available space.

`var truncationMode: Text.TruncationMode`

A value that indicates how the layout truncates the last line of text to fit
into the available space.

`func allowsTightening(Bool) -> some View`

Sets whether text in this view can compress the space between characters when
necessary to fit text in a line.

`var allowsTightening: Bool`

A Boolean value that indicates whether inter-character spacing should tighten
to fit the text into the available space.

`var minimumScaleFactor: CGFloat`

The minimum permissible proportion to shrink the font size to fit the text
into the available space.

`func baselineOffset(CGFloat) -> some View`

Sets the vertical offset for the text relative to its baseline in this view.

`func kerning(CGFloat) -> some View`

Sets the spacing, or kerning, between characters for the text in this view.

`func tracking(CGFloat) -> some View`

Sets the tracking for the text in this view.

`func flipsForRightToLeftLayoutDirection(Bool) -> some View`

Sets whether this view mirrors its contents horizontally when the layout
direction is right-to-left.

`enum TextAlignment`

An alignment position for text along the horizontal axis.

Instance Property

# minimumScaleFactor

The minimum permissible proportion to shrink the font size to fit the text
into the available space.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var minimumScaleFactor: CGFloat { get set }

## Discussion

In the example below, a label with a `minimumScaleFactor` of `0.5` draws its
text in a font size as small as half of the actual font if needed to fit into
the space next to the text input field:

You can set the minimum scale factor to any value greater than `0` and less
than or equal to `1`. The default value is `1`.

SwiftUI uses this value to shrink text that doesn’t fit in a view when it’s
okay to shrink the text. For example, a label with a `minimumScaleFactor` of
`0.5` draws its text in a font size as small as half the actual font if
needed.

## See Also

### Managing text layout

`func truncationMode(Text.TruncationMode) -> some View`

Sets the truncation mode for lines of text that are too long to fit in the
available space.

`var truncationMode: Text.TruncationMode`

A value that indicates how the layout truncates the last line of text to fit
into the available space.

`func allowsTightening(Bool) -> some View`

Sets whether text in this view can compress the space between characters when
necessary to fit text in a line.

`var allowsTightening: Bool`

A Boolean value that indicates whether inter-character spacing should tighten
to fit the text into the available space.

`func minimumScaleFactor(CGFloat) -> some View`

Sets the minimum amount that text in this view scales down to fit in the
available space.

`func baselineOffset(CGFloat) -> some View`

Sets the vertical offset for the text relative to its baseline in this view.

`func kerning(CGFloat) -> some View`

Sets the spacing, or kerning, between characters for the text in this view.

`func tracking(CGFloat) -> some View`

Sets the tracking for the text in this view.

`func flipsForRightToLeftLayoutDirection(Bool) -> some View`

Sets whether this view mirrors its contents horizontally when the layout
direction is right-to-left.

`enum TextAlignment`

An alignment position for text along the horizontal axis.

Instance Method

# baselineOffset(_:)

Sets the vertical offset for the text relative to its baseline in this view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func baselineOffset(_ baselineOffset: CGFloat) -> some View
    

##  Parameters

`baselineOffset`

    

The amount to shift the text vertically (up or down) relative to its baseline.

## Return Value

A view where text is above or below its baseline.

## See Also

### Managing text layout

`func truncationMode(Text.TruncationMode) -> some View`

Sets the truncation mode for lines of text that are too long to fit in the
available space.

`var truncationMode: Text.TruncationMode`

A value that indicates how the layout truncates the last line of text to fit
into the available space.

`func allowsTightening(Bool) -> some View`

Sets whether text in this view can compress the space between characters when
necessary to fit text in a line.

`var allowsTightening: Bool`

A Boolean value that indicates whether inter-character spacing should tighten
to fit the text into the available space.

`func minimumScaleFactor(CGFloat) -> some View`

Sets the minimum amount that text in this view scales down to fit in the
available space.

`var minimumScaleFactor: CGFloat`

The minimum permissible proportion to shrink the font size to fit the text
into the available space.

`func kerning(CGFloat) -> some View`

Sets the spacing, or kerning, between characters for the text in this view.

`func tracking(CGFloat) -> some View`

Sets the tracking for the text in this view.

`func flipsForRightToLeftLayoutDirection(Bool) -> some View`

Sets whether this view mirrors its contents horizontally when the layout
direction is right-to-left.

`enum TextAlignment`

An alignment position for text along the horizontal axis.

Instance Method

# kerning(_:)

Sets the spacing, or kerning, between characters for the text in this view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func kerning(_ kerning: CGFloat) -> some View
    

##  Parameters

`kerning`

    

The spacing to use between individual characters in text. Value of `0` sets
the kerning to the system default value.

## Return Value

A view where text has the specified amount of kerning.

## See Also

### Managing text layout

`func truncationMode(Text.TruncationMode) -> some View`

Sets the truncation mode for lines of text that are too long to fit in the
available space.

`var truncationMode: Text.TruncationMode`

A value that indicates how the layout truncates the last line of text to fit
into the available space.

`func allowsTightening(Bool) -> some View`

Sets whether text in this view can compress the space between characters when
necessary to fit text in a line.

`var allowsTightening: Bool`

A Boolean value that indicates whether inter-character spacing should tighten
to fit the text into the available space.

`func minimumScaleFactor(CGFloat) -> some View`

Sets the minimum amount that text in this view scales down to fit in the
available space.

`var minimumScaleFactor: CGFloat`

The minimum permissible proportion to shrink the font size to fit the text
into the available space.

`func baselineOffset(CGFloat) -> some View`

Sets the vertical offset for the text relative to its baseline in this view.

`func tracking(CGFloat) -> some View`

Sets the tracking for the text in this view.

`func flipsForRightToLeftLayoutDirection(Bool) -> some View`

Sets whether this view mirrors its contents horizontally when the layout
direction is right-to-left.

`enum TextAlignment`

An alignment position for text along the horizontal axis.

Instance Method

# tracking(_:)

Sets the tracking for the text in this view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func tracking(_ tracking: CGFloat) -> some View
    

##  Parameters

`tracking`

    

The amount of additional space, in points, that the view should add to each
character cluster after layout. Value of `0` sets the tracking to the system
default value.

## Return Value

A view where text has the specified amount of tracking.

## See Also

### Managing text layout

`func truncationMode(Text.TruncationMode) -> some View`

Sets the truncation mode for lines of text that are too long to fit in the
available space.

`var truncationMode: Text.TruncationMode`

A value that indicates how the layout truncates the last line of text to fit
into the available space.

`func allowsTightening(Bool) -> some View`

Sets whether text in this view can compress the space between characters when
necessary to fit text in a line.

`var allowsTightening: Bool`

A Boolean value that indicates whether inter-character spacing should tighten
to fit the text into the available space.

`func minimumScaleFactor(CGFloat) -> some View`

Sets the minimum amount that text in this view scales down to fit in the
available space.

`var minimumScaleFactor: CGFloat`

The minimum permissible proportion to shrink the font size to fit the text
into the available space.

`func baselineOffset(CGFloat) -> some View`

Sets the vertical offset for the text relative to its baseline in this view.

`func kerning(CGFloat) -> some View`

Sets the spacing, or kerning, between characters for the text in this view.

`func flipsForRightToLeftLayoutDirection(Bool) -> some View`

Sets whether this view mirrors its contents horizontally when the layout
direction is right-to-left.

`enum TextAlignment`

An alignment position for text along the horizontal axis.

Instance Method

# flipsForRightToLeftLayoutDirection(_:)

Sets whether this view mirrors its contents horizontally when the layout
direction is right-to-left.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func flipsForRightToLeftLayoutDirection(_ enabled: Bool) -> some View
    

##  Parameters

`enabled`

    

A Boolean value that indicates whether this view should have its content
flipped horizontally when the layout direction is right-to-left. By default,
views will adjust their layouts automatically in a right-to-left context and
do not need to be mirrored.

## Return Value

A view that conditionally mirrors its contents horizontally when the layout
direction is right-to-left.

## Discussion

Use `flipsForRightToLeftLayoutDirection(_:)` when you need the system to
horizontally mirror the contents of the view when presented in a right-to-left
layout.

To override the layout direction for a specific view, use the
`environment(_:_:)` view modifier to explicitly override the `layoutDirection`
environment value for the view.

## See Also

### Managing text layout

`func truncationMode(Text.TruncationMode) -> some View`

Sets the truncation mode for lines of text that are too long to fit in the
available space.

`var truncationMode: Text.TruncationMode`

A value that indicates how the layout truncates the last line of text to fit
into the available space.

`func allowsTightening(Bool) -> some View`

Sets whether text in this view can compress the space between characters when
necessary to fit text in a line.

`var allowsTightening: Bool`

A Boolean value that indicates whether inter-character spacing should tighten
to fit the text into the available space.

`func minimumScaleFactor(CGFloat) -> some View`

Sets the minimum amount that text in this view scales down to fit in the
available space.

`var minimumScaleFactor: CGFloat`

The minimum permissible proportion to shrink the font size to fit the text
into the available space.

`func baselineOffset(CGFloat) -> some View`

Sets the vertical offset for the text relative to its baseline in this view.

`func kerning(CGFloat) -> some View`

Sets the spacing, or kerning, between characters for the text in this view.

`func tracking(CGFloat) -> some View`

Sets the tracking for the text in this view.

`enum TextAlignment`

An alignment position for text along the horizontal axis.

Enumeration

# TextAlignment

An alignment position for text along the horizontal axis.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    enum TextAlignment

## Topics

### Getting text alignments

`case center`

`case leading`

`case trailing`

## Relationships

### Conforms To

  * `CaseIterable`
  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Managing text layout

`func truncationMode(Text.TruncationMode) -> some View`

Sets the truncation mode for lines of text that are too long to fit in the
available space.

`var truncationMode: Text.TruncationMode`

A value that indicates how the layout truncates the last line of text to fit
into the available space.

`func allowsTightening(Bool) -> some View`

Sets whether text in this view can compress the space between characters when
necessary to fit text in a line.

`var allowsTightening: Bool`

A Boolean value that indicates whether inter-character spacing should tighten
to fit the text into the available space.

`func minimumScaleFactor(CGFloat) -> some View`

Sets the minimum amount that text in this view scales down to fit in the
available space.

`var minimumScaleFactor: CGFloat`

The minimum permissible proportion to shrink the font size to fit the text
into the available space.

`func baselineOffset(CGFloat) -> some View`

Sets the vertical offset for the text relative to its baseline in this view.

`func kerning(CGFloat) -> some View`

Sets the spacing, or kerning, between characters for the text in this view.

`func tracking(CGFloat) -> some View`

Sets the tracking for the text in this view.

`func flipsForRightToLeftLayoutDirection(Bool) -> some View`

Sets whether this view mirrors its contents horizontally when the layout
direction is right-to-left.

Instance Method

# lineLimit(_:)

Sets the maximum number of lines that text can occupy in this view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func lineLimit(_ number: Int?) -> some View
    

##  Parameters

`number`

    

The line limit. If `nil`, no line limit applies.

## Return Value

A view that limits the number of lines that `Text` instances display.

## Discussion

Use this modifier to cap the number of lines that an individual text element
can display.

The line limit applies to all `Text` instances within a hierarchy. For
example, an `HStack` with multiple pieces of text longer than three lines caps
each piece of text to three lines rather than capping the total number of
lines across the `HStack`.

In the example below, the modifier limits the very long line in the `Text`
element to the 2 lines that fit within the view’s bounds:

## See Also

### Limiting line count for multiline text

`func lineLimit(PartialRangeFrom<Int>) -> some View`

Sets to a partial range the number of lines that text can occupy in this view.

`func lineLimit(PartialRangeThrough<Int>) -> some View`

Sets to a partial range the number of lines that text can occupy in this view.

`func lineLimit(ClosedRange<Int>) -> some View`

Sets to a closed range the number of lines that text can occupy in this view.

`func lineLimit(Int, reservesSpace: Bool) -> some View`

Sets a limit for the number of lines text can occupy in this view.

`var lineLimit: Int?`

The maximum number of lines that text can occupy in a view.

Instance Method

# lineLimit(_:)

Sets to a partial range the number of lines that text can occupy in this view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func lineLimit(_ limit: PartialRangeFrom<Int>) -> some View
    

##  Parameters

`limit`

    

The line limit.

## Discussion

Use this modifier to specify a partial range of lines that a `Text` view or a
vertical `TextField` can occupy. When the text of such views occupies less
space than the provided limit, that view expands to occupy the minimum number
of lines.

## See Also

### Limiting line count for multiline text

`func lineLimit(Int?) -> some View`

Sets the maximum number of lines that text can occupy in this view.

`func lineLimit(PartialRangeThrough<Int>) -> some View`

Sets to a partial range the number of lines that text can occupy in this view.

`func lineLimit(ClosedRange<Int>) -> some View`

Sets to a closed range the number of lines that text can occupy in this view.

`func lineLimit(Int, reservesSpace: Bool) -> some View`

Sets a limit for the number of lines text can occupy in this view.

`var lineLimit: Int?`

The maximum number of lines that text can occupy in a view.

Instance Method

# lineLimit(_:)

Sets to a partial range the number of lines that text can occupy in this view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func lineLimit(_ limit: PartialRangeThrough<Int>) -> some View
    

##  Parameters

`limit`

    

The line limit.

## Discussion

Use this modifier to specify a partial range of lines that a `Text` view or a
vertical `TextField` can occupy. When the text of such views occupies more
space than the provided limit, a `Text` view truncates its content while a
`TextField` becomes scrollable.

Note

This modifier is equivalent to the `lineLimit(_:)` modifier taking just an
integer.

## See Also

### Limiting line count for multiline text

`func lineLimit(Int?) -> some View`

Sets the maximum number of lines that text can occupy in this view.

`func lineLimit(PartialRangeFrom<Int>) -> some View`

Sets to a partial range the number of lines that text can occupy in this view.

`func lineLimit(ClosedRange<Int>) -> some View`

Sets to a closed range the number of lines that text can occupy in this view.

`func lineLimit(Int, reservesSpace: Bool) -> some View`

Sets a limit for the number of lines text can occupy in this view.

`var lineLimit: Int?`

The maximum number of lines that text can occupy in a view.

Instance Method

# lineLimit(_:)

Sets to a closed range the number of lines that text can occupy in this view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func lineLimit(_ limit: ClosedRange<Int>) -> some View
    

##  Parameters

`limit`

    

The line limit.

## Discussion

Use this modifier to specify a closed range of lines that a `Text` view or a
vertical `TextField` can occupy. When the text of such views occupies more
space than the provided limit, a `Text` view truncates its content while a
`TextField` becomes scrollable.

## See Also

### Limiting line count for multiline text

`func lineLimit(Int?) -> some View`

Sets the maximum number of lines that text can occupy in this view.

`func lineLimit(PartialRangeFrom<Int>) -> some View`

Sets to a partial range the number of lines that text can occupy in this view.

`func lineLimit(PartialRangeThrough<Int>) -> some View`

Sets to a partial range the number of lines that text can occupy in this view.

`func lineLimit(Int, reservesSpace: Bool) -> some View`

Sets a limit for the number of lines text can occupy in this view.

`var lineLimit: Int?`

The maximum number of lines that text can occupy in a view.

Instance Method

# lineLimit(_:reservesSpace:)

Sets a limit for the number of lines text can occupy in this view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func lineLimit(
        _ limit: Int,
        reservesSpace: Bool
    ) -> some View
    

##  Parameters

`limit`

    

The line limit.

`reservesSpace`

    

Whether text reserves space so that it always occupies the height required to
display the specified number of lines.

## Discussion

Use this modifier to specify a limit to the lines that a `Text` or a vertical
`TextField` may occupy. If passed a value of true for the `reservesSpace`
parameter, and the text of such views occupies less space than the provided
limit, that view expands to occupy the minimum number of lines. When the text
occupies more space than the provided limit, a `Text` view truncates its
content while a `TextField` becomes scrollable.

## See Also

### Limiting line count for multiline text

`func lineLimit(Int?) -> some View`

Sets the maximum number of lines that text can occupy in this view.

`func lineLimit(PartialRangeFrom<Int>) -> some View`

Sets to a partial range the number of lines that text can occupy in this view.

`func lineLimit(PartialRangeThrough<Int>) -> some View`

Sets to a partial range the number of lines that text can occupy in this view.

`func lineLimit(ClosedRange<Int>) -> some View`

Sets to a closed range the number of lines that text can occupy in this view.

`var lineLimit: Int?`

The maximum number of lines that text can occupy in a view.

Instance Property

# lineLimit

The maximum number of lines that text can occupy in a view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var lineLimit: Int? { get set }

## Discussion

The maximum number of lines is `1` if the value is less than `1`. If the value
is `nil`, the text uses as many lines as required. The default is `nil`.

## See Also

### Limiting line count for multiline text

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

Instance Method

# lineSpacing(_:)

Sets the amount of space between lines of text in this view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func lineSpacing(_ lineSpacing: CGFloat) -> some View
    

##  Parameters

`lineSpacing`

    

The amount of space between the bottom of one line and the top of the next
line in points.

## Discussion

Use `lineSpacing(_:)` to set the amount of spacing from the bottom of one line
to the top of the next for text elements in the view.

In the `Text` view in the example below, 10 points separate the bottom of one
line to the top of the next as the text field wraps inside this view. Applying
`lineSpacing(_:)` to a view hierarchy applies the line spacing to all text
elements contained in the view.

## See Also

### Formatting multiline text

`var lineSpacing: CGFloat`

The distance in points between the bottom of one line fragment and the top of
the next.

`func multilineTextAlignment(TextAlignment) -> some View`

Sets the alignment of a text view that contains multiple lines of text.

`var multilineTextAlignment: TextAlignment`

An environment value that indicates how a text view aligns its lines when the
content wraps or contains newlines.

Instance Property

# lineSpacing

The distance in points between the bottom of one line fragment and the top of
the next.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var lineSpacing: CGFloat { get set }

## Discussion

This value is always nonnegative.

## See Also

### Formatting multiline text

`func lineSpacing(CGFloat) -> some View`

Sets the amount of space between lines of text in this view.

`func multilineTextAlignment(TextAlignment) -> some View`

Sets the alignment of a text view that contains multiple lines of text.

`var multilineTextAlignment: TextAlignment`

An environment value that indicates how a text view aligns its lines when the
content wraps or contains newlines.

Instance Method

# multilineTextAlignment(_:)

Sets the alignment of a text view that contains multiple lines of text.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func multilineTextAlignment(_ alignment: TextAlignment) -> some View
    

##  Parameters

`alignment`

    

A value that you use to align multiple lines of text within a view.

## Return Value

A view that aligns the lines of multiline `Text` instances it contains.

## Discussion

Use this modifier to set an alignment for a multiline block of text. For
example, the modifier centers the contents of the following `Text` view:

The text in the above example spans more than one line because:

  * The newline character introduces a line break.

  * The frame modifier limits the space available to the text view, and by default a text view wraps lines that don’t fit in the available width. As a result, the text before the explicit line break wraps to three lines, and the text after uses two lines.

The modifier applies the alignment to the all the lines of text in the view,
regardless of why wrapping occurs:

The modifier has no effect on a `Text` view that contains only one line of
text, because a text view has a width that exactly matches the width of its
widest line. If you want to align an entire text view rather than its
contents, set the aligment of its container, like a `VStack` or a frame that
you create with the
`frame(minWidth:idealWidth:maxWidth:minHeight:idealHeight:maxHeight:alignment:)`
modifier.

Note

You can use this modifier to control the alignment of a `Text` view that you
create with the `init(_:style:)` initializer to display localized dates and
times, including when the view uses only a single line, but only when that
view appears in a widget.

The modifier also affects the content alignment of other text container types,
like `TextEditor` and `TextField`. In those cases, the modifier sets the
alignment even when the view contains only a single line because view’s width
isn’t dictated by the width of the text it contains.

The modifier operates by setting the `multilineTextAlignment` value in the
environment, so it affects all the text containers in the modified view
hierarchy. For example, you can apply the modifier to a `VStack` to configure
all the text views inside the stack.

## See Also

### Formatting multiline text

`func lineSpacing(CGFloat) -> some View`

Sets the amount of space between lines of text in this view.

`var lineSpacing: CGFloat`

The distance in points between the bottom of one line fragment and the top of
the next.

`var multilineTextAlignment: TextAlignment`

An environment value that indicates how a text view aligns its lines when the
content wraps or contains newlines.

Instance Property

# multilineTextAlignment

An environment value that indicates how a text view aligns its lines when the
content wraps or contains newlines.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var multilineTextAlignment: TextAlignment { get set }

## Discussion

Set this value for a view hierarchy by applying the
`multilineTextAlignment(_:)` view modifier. Views in the hierarchy that
display text, like `Text` or `TextEditor`, read the value from the environment
and adjust their text alignment accordingly.

This value has no effect on a `Text` view that contains only one line of text,
because a text view has a width that exactly matches the width of its widest
line. If you want to align an entire text view rather than its contents, set
the aligment of its container, like a `VStack` or a frame that you create with
the
`frame(minWidth:idealWidth:maxWidth:minHeight:idealHeight:maxHeight:alignment:)`
modifier.

Note

You can use this value to control the alignment of a `Text` view that you
create with the `init(_:style:)` initializer to display localized dates and
times, including when the view uses only a single line, but only when that
view appears in a widget.

## See Also

### Formatting multiline text

`func lineSpacing(CGFloat) -> some View`

Sets the amount of space between lines of text in this view.

`var lineSpacing: CGFloat`

The distance in points between the bottom of one line fragment and the top of
the next.

`func multilineTextAlignment(TextAlignment) -> some View`

Sets the alignment of a text view that contains multiple lines of text.

Instance Method

# autocorrectionDisabled(_:)

Sets whether to disable autocorrection for this view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func autocorrectionDisabled(_ disable: Bool = true) -> some View
    

##  Parameters

`disable`

    

A Boolean value that indicates whether autocorrection is disabled for this
view. The default value is `true`.

## Discussion

Use this method when the effect of autocorrection would make it more difficult
for the user to input information. The entry of proper names and street
addresses are examples where autocorrection can negatively affect the user’s
ability complete a data entry task.

The example below configures a `TextField` with the default keyboard.
Disabling autocorrection allows the user to enter arbitrary text without the
autocorrection system offering suggestions or attempting to override their
input.

## See Also

### Managing text entry

`var autocorrectionDisabled: Bool`

A Boolean value that determines whether the view hierarchy has auto-correction
enabled.

`func keyboardType(UIKeyboardType) -> some View`

Sets the keyboard type for this view.

`func scrollDismissesKeyboard(ScrollDismissesKeyboardMode) -> some View`

Configures the behavior in which scrollable content interacts with the
software keyboard.

`func textContentType(UITextContentType?) -> some View`

Sets the text content type for this view, which the system uses to offer
suggestions while the user enters text on an iOS or tvOS device.

`func textContentType(NSTextContentType?) -> some View`

Sets the text content type for this view, which the system uses to offer
suggestions while the user enters text on macOS.

`func textContentType(WKTextContentType?) -> some View`

Sets the text content type for this view, which the system uses to offer
suggestions while the user enters text on a watchOS device.

`func textInputAutocapitalization(TextInputAutocapitalization?) -> some View`

Sets how often the shift key in the keyboard is automatically enabled.

`struct TextInputAutocapitalization`

The kind of autocapitalization behavior applied during text input.

Instance Property

# autocorrectionDisabled

A Boolean value that determines whether the view hierarchy has auto-correction
enabled.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var autocorrectionDisabled: Bool { get set }

## Discussion

The default value is `false`.

## See Also

### Managing text entry

`func autocorrectionDisabled(Bool) -> some View`

Sets whether to disable autocorrection for this view.

`func keyboardType(UIKeyboardType) -> some View`

Sets the keyboard type for this view.

`func scrollDismissesKeyboard(ScrollDismissesKeyboardMode) -> some View`

Configures the behavior in which scrollable content interacts with the
software keyboard.

`func textContentType(UITextContentType?) -> some View`

Sets the text content type for this view, which the system uses to offer
suggestions while the user enters text on an iOS or tvOS device.

`func textContentType(NSTextContentType?) -> some View`

Sets the text content type for this view, which the system uses to offer
suggestions while the user enters text on macOS.

`func textContentType(WKTextContentType?) -> some View`

Sets the text content type for this view, which the system uses to offer
suggestions while the user enters text on a watchOS device.

`func textInputAutocapitalization(TextInputAutocapitalization?) -> some View`

Sets how often the shift key in the keyboard is automatically enabled.

`struct TextInputAutocapitalization`

The kind of autocapitalization behavior applied during text input.

Instance Method

# keyboardType(_:)

Sets the keyboard type for this view.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  visionOS 1.0+

    
    
    func keyboardType(_ type: UIKeyboardType) -> some View
    

##  Parameters

`type`

    

One of the keyboard types defined in the `UIKeyboardType` enumeration.

## Discussion

Use `keyboardType(_:)` to specify the keyboard type to use for text entry. A
number of different keyboard types are available to meet specialized input
needs, such as entering email addresses or phone numbers.

The example below presents a `TextField` to input an email address. Setting
the text field’s keyboard type to `.emailAddress` ensures the user can only
enter correctly formatted email addresses.

There are several different kinds of specialized keyboard types available
though the `UIKeyboardType` enumeration. To specify the default system
keyboard type, use `.default`.

## See Also

### Managing text entry

`func autocorrectionDisabled(Bool) -> some View`

Sets whether to disable autocorrection for this view.

`var autocorrectionDisabled: Bool`

A Boolean value that determines whether the view hierarchy has auto-correction
enabled.

`func scrollDismissesKeyboard(ScrollDismissesKeyboardMode) -> some View`

Configures the behavior in which scrollable content interacts with the
software keyboard.

`func textContentType(UITextContentType?) -> some View`

Sets the text content type for this view, which the system uses to offer
suggestions while the user enters text on an iOS or tvOS device.

`func textContentType(NSTextContentType?) -> some View`

Sets the text content type for this view, which the system uses to offer
suggestions while the user enters text on macOS.

`func textContentType(WKTextContentType?) -> some View`

Sets the text content type for this view, which the system uses to offer
suggestions while the user enters text on a watchOS device.

`func textInputAutocapitalization(TextInputAutocapitalization?) -> some View`

Sets how often the shift key in the keyboard is automatically enabled.

`struct TextInputAutocapitalization`

The kind of autocapitalization behavior applied during text input.

Instance Method

# scrollDismissesKeyboard(_:)

Configures the behavior in which scrollable content interacts with the
software keyboard.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+

    
    
    func scrollDismissesKeyboard(_ mode: ScrollDismissesKeyboardMode) -> some View
    

##  Parameters

`mode`

    

The keyboard dismissal mode that scrollable content uses.

## Return Value

A view that uses the specified keyboard dismissal mode.

## Discussion

You use this modifier to customize how scrollable content interacts with the
software keyboard. For example, you can specify a value of `immediately` to
indicate that you would like scrollable content to immediately dismiss the
keyboard if present when a scroll drag gesture begins.

You can also use this modifier to customize the keyboard dismissal behavior
for other kinds of scrollable views, like a `List` or a `TextEditor`.

By default, a `TextEditor` is interactive while other kinds of scrollable
content always dismiss the keyboard on a scroll when linked against iOS 16 or
later. Pass a value of `never` to indicate that scrollable content should
never automatically dismiss the keyboard.

## See Also

### Interacting with a software keyboard

`var scrollDismissesKeyboardMode: ScrollDismissesKeyboardMode`

The way that scrollable content interacts with the software keyboard.

`struct ScrollDismissesKeyboardMode`

The ways that scrollable content can interact with the software keyboard.

Instance Method

# textContentType(_:)

Sets the text content type for this view, which the system uses to offer
suggestions while the user enters text on an iOS or tvOS device.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  visionOS 1.0+

    
    
    func textContentType(_ textContentType: UITextContentType?) -> some View
    

##  Parameters

`textContentType`

    

One of the content types available in the `UITextContentType` structure that
identify the semantic meaning expected for a text-entry area. These include
support for email addresses, location names, URLs, and telephone numbers, to
name just a few.

## Discussion

Use this method to set the content type for input text. For example, you can
configure a `TextField` for the entry of email addresses:

## See Also

### Managing text entry

`func autocorrectionDisabled(Bool) -> some View`

Sets whether to disable autocorrection for this view.

`var autocorrectionDisabled: Bool`

A Boolean value that determines whether the view hierarchy has auto-correction
enabled.

`func keyboardType(UIKeyboardType) -> some View`

Sets the keyboard type for this view.

`func scrollDismissesKeyboard(ScrollDismissesKeyboardMode) -> some View`

Configures the behavior in which scrollable content interacts with the
software keyboard.

`func textContentType(NSTextContentType?) -> some View`

Sets the text content type for this view, which the system uses to offer
suggestions while the user enters text on macOS.

`func textContentType(WKTextContentType?) -> some View`

Sets the text content type for this view, which the system uses to offer
suggestions while the user enters text on a watchOS device.

`func textInputAutocapitalization(TextInputAutocapitalization?) -> some View`

Sets how often the shift key in the keyboard is automatically enabled.

`struct TextInputAutocapitalization`

The kind of autocapitalization behavior applied during text input.

Instance Method

# textContentType(_:)

Sets the text content type for this view, which the system uses to offer
suggestions while the user enters text on macOS.

macOS 11.0+

    
    
    func textContentType(_ textContentType: NSTextContentType?) -> some View
    

##  Parameters

`textContentType`

    

One of the content types available in the `NSTextContentType` structure that
identify the semantic meaning expected for a text-entry area.

## Discussion

Use this method to set the content type for input text. For example, you can
configure a `TextField` for the entry of a username:

## See Also

### Managing text entry

`func autocorrectionDisabled(Bool) -> some View`

Sets whether to disable autocorrection for this view.

`var autocorrectionDisabled: Bool`

A Boolean value that determines whether the view hierarchy has auto-correction
enabled.

`func keyboardType(UIKeyboardType) -> some View`

Sets the keyboard type for this view.

`func scrollDismissesKeyboard(ScrollDismissesKeyboardMode) -> some View`

Configures the behavior in which scrollable content interacts with the
software keyboard.

`func textContentType(UITextContentType?) -> some View`

Sets the text content type for this view, which the system uses to offer
suggestions while the user enters text on an iOS or tvOS device.

`func textContentType(WKTextContentType?) -> some View`

Sets the text content type for this view, which the system uses to offer
suggestions while the user enters text on a watchOS device.

`func textInputAutocapitalization(TextInputAutocapitalization?) -> some View`

Sets how often the shift key in the keyboard is automatically enabled.

`struct TextInputAutocapitalization`

The kind of autocapitalization behavior applied during text input.

Instance Method

# textContentType(_:)

Sets the text content type for this view, which the system uses to offer
suggestions while the user enters text on a watchOS device.

watchOS 6.0+

    
    
    func textContentType(_ textContentType: WKTextContentType?) -> some View
    

##  Parameters

`textContentType`

    

One of the content types available in the `WKTextContentType` structure that
identify the semantic meaning expected for a text-entry area. These include
support for email addresses, location names, URLs, and telephone numbers, to
name just a few.

## Discussion

Use this method to set the content type for input text. For example, you can
configure a `TextField` for the entry of email addresses:

## See Also

### Managing text entry

`func autocorrectionDisabled(Bool) -> some View`

Sets whether to disable autocorrection for this view.

`var autocorrectionDisabled: Bool`

A Boolean value that determines whether the view hierarchy has auto-correction
enabled.

`func keyboardType(UIKeyboardType) -> some View`

Sets the keyboard type for this view.

`func scrollDismissesKeyboard(ScrollDismissesKeyboardMode) -> some View`

Configures the behavior in which scrollable content interacts with the
software keyboard.

`func textContentType(UITextContentType?) -> some View`

Sets the text content type for this view, which the system uses to offer
suggestions while the user enters text on an iOS or tvOS device.

`func textContentType(NSTextContentType?) -> some View`

Sets the text content type for this view, which the system uses to offer
suggestions while the user enters text on macOS.

`func textInputAutocapitalization(TextInputAutocapitalization?) -> some View`

Sets how often the shift key in the keyboard is automatically enabled.

`struct TextInputAutocapitalization`

The kind of autocapitalization behavior applied during text input.

Instance Method

# textInputAutocapitalization(_:)

Sets how often the shift key in the keyboard is automatically enabled.

iOS 15.0+  iPadOS 15.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS 8.0+
visionOS 1.0+

    
    
    func textInputAutocapitalization(_ autocapitalization: TextInputAutocapitalization?) -> some View
    

##  Parameters

`autocapitalization`

    

One of the capitalizing behaviors defined in the `TextInputAutocapitalization`
struct or nil.

## Discussion

Use `textInputAutocapitalization(_:)` when you need to automatically
capitalize words, sentences, or other text like proper nouns.

In example below, as the user enters text the shift key is automatically
enabled before every word:

The `TextInputAutocapitalization` struct defines the available
autocapitalizing behavior. Providing `nil` to this view modifier does not
change the autocapitalization behavior. The default is
`TextInputAutocapitalization.sentences`.

## See Also

### Managing text entry

`func autocorrectionDisabled(Bool) -> some View`

Sets whether to disable autocorrection for this view.

`var autocorrectionDisabled: Bool`

A Boolean value that determines whether the view hierarchy has auto-correction
enabled.

`func keyboardType(UIKeyboardType) -> some View`

Sets the keyboard type for this view.

`func scrollDismissesKeyboard(ScrollDismissesKeyboardMode) -> some View`

Configures the behavior in which scrollable content interacts with the
software keyboard.

`func textContentType(UITextContentType?) -> some View`

Sets the text content type for this view, which the system uses to offer
suggestions while the user enters text on an iOS or tvOS device.

`func textContentType(NSTextContentType?) -> some View`

Sets the text content type for this view, which the system uses to offer
suggestions while the user enters text on macOS.

`func textContentType(WKTextContentType?) -> some View`

Sets the text content type for this view, which the system uses to offer
suggestions while the user enters text on a watchOS device.

`struct TextInputAutocapitalization`

The kind of autocapitalization behavior applied during text input.

Structure

# TextInputAutocapitalization

The kind of autocapitalization behavior applied during text input.

iOS 15.0+  iPadOS 15.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS 8.0+
visionOS 1.0+

    
    
    struct TextInputAutocapitalization

## Overview

Pass an instance of `TextInputAutocapitalization` to the
`textInputAutocapitalization(_:)` view modifier.

## Topics

### Getting autocapitalization options

`static var characters: TextInputAutocapitalization`

Defines an autocapitalizing behavior that will capitalize every letter.

`static var sentences: TextInputAutocapitalization`

Defines an autocapitalizing behavior that will capitalize the first letter in
every sentence.

`static var words: TextInputAutocapitalization`

Defines an autocapitalizing behavior that will capitalize the first letter of
every word.

`static var never: TextInputAutocapitalization`

Defines an autocapitalizing behavior that will not capitalize anything.

### Creating an autocapitalization type

`init?(UITextAutocapitalizationType)`

Creates a new `TextInputAutocapitalization` struct from a
`UITextAutocapitalizationType` enum.

## Relationships

### Conforms To

  * `Sendable`

## See Also

### Managing text entry

`func autocorrectionDisabled(Bool) -> some View`

Sets whether to disable autocorrection for this view.

`var autocorrectionDisabled: Bool`

A Boolean value that determines whether the view hierarchy has auto-correction
enabled.

`func keyboardType(UIKeyboardType) -> some View`

Sets the keyboard type for this view.

`func scrollDismissesKeyboard(ScrollDismissesKeyboardMode) -> some View`

Configures the behavior in which scrollable content interacts with the
software keyboard.

`func textContentType(UITextContentType?) -> some View`

Sets the text content type for this view, which the system uses to offer
suggestions while the user enters text on an iOS or tvOS device.

`func textContentType(NSTextContentType?) -> some View`

Sets the text content type for this view, which the system uses to offer
suggestions while the user enters text on macOS.

`func textContentType(WKTextContentType?) -> some View`

Sets the text content type for this view, which the system uses to offer
suggestions while the user enters text on a watchOS device.

`func textInputAutocapitalization(TextInputAutocapitalization?) -> some View`

Sets how often the shift key in the keyboard is automatically enabled.

Instance Method

# searchDictationBehavior(_:)

iOS 17.0+  iPadOS 17.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func searchDictationBehavior(_ dictationBehavior: TextInputDictationBehavior) -> some View
    

## See Also

### Dictating text

`struct TextInputDictationActivation`

`struct TextInputDictationBehavior`

Structure

# TextInputDictationActivation

iOS 17.0+  iPadOS 17.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    struct TextInputDictationActivation

## Topics

### Getting activation values

`static let onLook: TextInputDictationActivation`

A configuration that activates dictation when someone selects the microphone
or looks at the entry field.

`static let onSelect: TextInputDictationActivation`

A configuration that activates dictation when someone selects the microphone.

## Relationships

### Conforms To

  * `Equatable`
  * `Sendable`

## See Also

### Dictating text

`func searchDictationBehavior(TextInputDictationBehavior) -> some View`

`struct TextInputDictationBehavior`

Structure

# TextInputDictationBehavior

iOS 17.0+  iPadOS 17.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    struct TextInputDictationBehavior

## Topics

### Getting behavior values

`static let automatic: TextInputDictationBehavior`

A platform-appropriate default text input dictation behavior.

`static func inline(activation: TextInputDictationActivation) ->
TextInputDictationBehavior`

Adds a dictation microphone in the search bar.

`static let preventDictation: TextInputDictationBehavior`

Prevents the search bar from having a dictation microphone.

## Relationships

### Conforms To

  * `Equatable`
  * `Sendable`

## See Also

### Dictating text

`func searchDictationBehavior(TextInputDictationBehavior) -> some View`

`struct TextInputDictationActivation`

Instance Method

# typeSelectEquivalent(_:)

Sets an explicit type select equivalent text in a collection, such as a list
or table.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func typeSelectEquivalent(_ text: Text?) -> some View
    

##  Parameters

`text`

    

The explicit text value to use as a type select equivalent for a view in a
collection.

## Discussion

By default, a type select equivalent is automatically derived from any `Text`
or `TextField` content in a list or table. In the below example, type select
can be used to select a person, even though no explicit value has been set.

An explicit type select value should be set when there is no textual content
or when a different value is desired compared to what’s displayed in the view.
Explicit values also provide a more performant for complex view types. In the
below example, type select is explicitly set to allow selection of views that
otherwise only display an image.

Setting an empty string value disables text selection for the view, and a
value of `nil` results in the view using its default value.

## See Also

### Specifying text equivalents

`func typeSelectEquivalent(LocalizedStringKey) -> some View`

Sets an explicit type select equivalent text in a collection, such as a list
or table.

`func typeSelectEquivalent<S>(S) -> some View`

Sets an explicit type select equivalent text in a collection, such as a list
or table.

Instance Method

# typeSelectEquivalent(_:)

Sets an explicit type select equivalent text in a collection, such as a list
or table.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func typeSelectEquivalent(_ stringKey: LocalizedStringKey) -> some View
    

##  Parameters

`stringKey`

    

The localized string key to use as a type select equivalent for a view in a
collection.

## Discussion

By default, a type select equivalent is automatically derived from any `Text`
or `TextField` content in a list or table. In the below example, type select
can be used to select a person, even though no explicit value has been set.

An explicit type select value should be set when there is no textual content
or when a different value is desired compared to what’s displayed in the view.
Explicit values also provide a more performant for complex view types. In the
below example, type select is explicitly set to allow selection of views that
otherwise only display an image.

Setting an empty string value disables text selection for the view, and a
value of `nil` results in the view using its default value.

## See Also

### Specifying text equivalents

`func typeSelectEquivalent(Text?) -> some View`

Sets an explicit type select equivalent text in a collection, such as a list
or table.

`func typeSelectEquivalent<S>(S) -> some View`

Sets an explicit type select equivalent text in a collection, such as a list
or table.

Instance Method

# typeSelectEquivalent(_:)

Sets an explicit type select equivalent text in a collection, such as a list
or table.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func typeSelectEquivalent<S>(_ string: S) -> some View where S : StringProtocol
    

##  Parameters

`string`

    

The string to use as a type select equivalent for a view in a collection.

## Discussion

By default, a type select equivalent is automatically derived from any `Text`
or `TextField` content in a list or table. In the below example, type select
can be used to select a person, even though no explicit value has been set.

An explicit type select value should be set when there is no textual content
or when a different value is desired compared to what’s displayed in the view.
Explicit values also provide a more performant for complex view types. In the
below example, type select is explicitly set to allow selection of views that
otherwise only display an image.

Setting an empty string value disables text selection for the view, and a
value of `nil` results in the view using its default value.

## See Also

### Specifying text equivalents

`func typeSelectEquivalent(Text?) -> some View`

Sets an explicit type select equivalent text in a collection, such as a list
or table.

`func typeSelectEquivalent(LocalizedStringKey) -> some View`

Sets an explicit type select equivalent text in a collection, such as a list
or table.

Article

# Preparing views for localization

Specify hints and add strings to localize your SwiftUI views.

## Overview

Localize SwiftUI views so users experience your app in their own native
language, region, and culture. Xcode parses SwiftUI views for strings to
localize when exporting a localization catalog. You can add hints so that
Xcode generates correct, hinted strings to localize for your app.

For information about string catalogs, see Localizing and varying text with a
string catalog.

### Add comments to text views

To ease the translation process, provide hints to translators that share how
and where your app displays the strings of a `Text` view. To add a hint, use
the optional `comment` parameter to the text view initializer
`init(_:tableName:bundle:comment:)`. When you localize your app with Xcode, it
includes the comment string along with the string. For example, the following
text view includes a comment:

Xcode creates the following entry in your string catalog file for this view:

### Provide additional information with text views

You can localize many SwiftUI views that have a string label by providing a
string that SwiftUI interprets as a `LocalizedStringKey`. The system uses the
key to retrieve a localized value from your string catalog at runtime, or uses
the string directly if it can’t find the key in the catalog. For example,
SwiftUI uses the string input to the following `Label` initializer as a
localized string key:

If you additionally want to provide a comment for localization, you can use an
explicit `Text` view instead:

Many SwiftUI controls have view builder initializers that enable you to follow
this pattern. For more information on how to make your app’s text
translatable, see Preparing your app’s text for translation.

## See Also

### Localizing text

`struct LocalizedStringKey`

The key used to look up an entry in a strings file or strings dictionary file.

`var locale: Locale`

The current locale that views should use.

`func typesettingLanguage(Locale.Language, isEnabled: Bool) -> some View`

Specifies the language for typesetting.

`func typesettingLanguage(TypesettingLanguage, isEnabled: Bool) -> some View`

Specifies the language for typesetting.

`struct TypesettingLanguage`

Defines how typesetting language is determined for text.

Structure

# LocalizedStringKey

The key used to look up an entry in a strings file or strings dictionary file.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct LocalizedStringKey

## Overview

Initializers for several SwiftUI types – such as `Text`, `Toggle`, `Picker`
and others – implicitly look up a localized string when you provide a string
literal. When you use the initializer `Text("Hello")`, SwiftUI creates a
`LocalizedStringKey` for you and uses that to look up a localization of the
`Hello` string. This works because `LocalizedStringKey` conforms to
`ExpressibleByStringLiteral`.

Types whose initializers take a `LocalizedStringKey` usually have a
corresponding initializer that accepts a parameter that conforms to
`StringProtocol`. Passing a `String` variable to these initializers avoids
localization, which is usually appropriate when the variable contains a user-
provided value.

As a general rule, use a string literal argument when you want localization,
and a string variable argument when you don’t. In the case where you want to
localize the value of a string variable, use the string to create a new
`LocalizedStringKey` instance.

The following example shows how to create `Text` instances both with and
without localization. The title parameter provided to the `Section` is a
literal string, so SwiftUI creates a `LocalizedStringKey` for it. However, the
string entries in the `messageStore.today` array are `String` variables, so
the `Text` views in the list use the string values verbatim.

If the app is localized into Japanese with the following translation of its
`Localizable.strings` file:

    
    
    "Today" = "今日";
    

When run in Japanese, the example produces a list like the following,
localizing “Today” for the section header, but not the list items.

## Topics

### Creating a key from a literal value

`init(String)`

Creates a localized string key from the given string value.

`init(stringLiteral: String)`

Creates a localized string key from the given string literal.

### Creating a key from an interpolation

`init(stringInterpolation: LocalizedStringKey.StringInterpolation)`

Creates a localized string key from the given string interpolation.

`struct StringInterpolation`

Represents the contents of a string literal with interpolations while it’s
being built, for use in creating a localized string key.

## Relationships

### Conforms To

  * `Equatable`
  * `ExpressibleByExtendedGraphemeClusterLiteral`
  * `ExpressibleByStringInterpolation`
  * `ExpressibleByStringLiteral`
  * `ExpressibleByUnicodeScalarLiteral`

## See Also

### Localizing text

Preparing views for localization

Specify hints and add strings to localize your SwiftUI views.

`var locale: Locale`

The current locale that views should use.

`func typesettingLanguage(Locale.Language, isEnabled: Bool) -> some View`

Specifies the language for typesetting.

`func typesettingLanguage(TypesettingLanguage, isEnabled: Bool) -> some View`

Specifies the language for typesetting.

`struct TypesettingLanguage`

Defines how typesetting language is determined for text.

Instance Property

# locale

The current locale that views should use.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var locale: Locale { get set }

## See Also

### Localizing text

Preparing views for localization

Specify hints and add strings to localize your SwiftUI views.

`struct LocalizedStringKey`

The key used to look up an entry in a strings file or strings dictionary file.

`func typesettingLanguage(Locale.Language, isEnabled: Bool) -> some View`

Specifies the language for typesetting.

`func typesettingLanguage(TypesettingLanguage, isEnabled: Bool) -> some View`

Specifies the language for typesetting.

`struct TypesettingLanguage`

Defines how typesetting language is determined for text.

Instance Method

# typesettingLanguage(_:isEnabled:)

Specifies the language for typesetting.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func typesettingLanguage(
        _ language: Locale.Language,
        isEnabled: Bool = true
    ) -> some View
    

##  Parameters

`language`

    

The explicit language to use for typesetting.

`isEnabled`

    

A Boolean value that indicates whether text langauge is added

## Return Value

A view with the typesetting language set to the value you supply.

## Discussion

In some cases `Text` may contain text of a particular language which doesn’t
match the device UI language. In that case it’s useful to specify a language
so line height, line breaking and spacing will respect the script used for
that language. For example:

Note: this language does not affect text localization.

## See Also

### Localizing text

Preparing views for localization

Specify hints and add strings to localize your SwiftUI views.

`struct LocalizedStringKey`

The key used to look up an entry in a strings file or strings dictionary file.

`var locale: Locale`

The current locale that views should use.

`func typesettingLanguage(TypesettingLanguage, isEnabled: Bool) -> some View`

Specifies the language for typesetting.

`struct TypesettingLanguage`

Defines how typesetting language is determined for text.

Instance Method

# typesettingLanguage(_:isEnabled:)

Specifies the language for typesetting.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func typesettingLanguage(
        _ language: TypesettingLanguage,
        isEnabled: Bool = true
    ) -> some View
    

##  Parameters

`language`

    

The language to use for typesetting.

`isEnabled`

    

A Boolean value that indicates whether text language is added

## Return Value

A view with the typesetting language set to the value you supply.

## Discussion

In some cases `Text` may contain text of a particular language which doesn’t
match the device UI language. In that case it’s useful to specify a language
so line height, line breaking and spacing will respect the script used for
that language. For example:

Note: this language does not affect text localized localization.

## See Also

### Localizing text

Preparing views for localization

Specify hints and add strings to localize your SwiftUI views.

`struct LocalizedStringKey`

The key used to look up an entry in a strings file or strings dictionary file.

`var locale: Locale`

The current locale that views should use.

`func typesettingLanguage(Locale.Language, isEnabled: Bool) -> some View`

Specifies the language for typesetting.

`struct TypesettingLanguage`

Defines how typesetting language is determined for text.

Structure

# TypesettingLanguage

Defines how typesetting language is determined for text.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct TypesettingLanguage

## Overview

Use a modifier like `typesettingLanguage(_:isEnabled:)` to specify the
typesetting language.

## Topics

### Getting language behavior

`static let automatic: TypesettingLanguage`

Automatic language behavior.

`static func explicit(Locale.Language) -> TypesettingLanguage`

Use explicit language.

## Relationships

### Conforms To

  * `Equatable`
  * `Sendable`

## See Also

### Localizing text

Preparing views for localization

Specify hints and add strings to localize your SwiftUI views.

`struct LocalizedStringKey`

The key used to look up an entry in a strings file or strings dictionary file.

`var locale: Locale`

The current locale that views should use.

`func typesettingLanguage(Locale.Language, isEnabled: Bool) -> some View`

Specifies the language for typesetting.

`func typesettingLanguage(TypesettingLanguage, isEnabled: Bool) -> some View`

Specifies the language for typesetting.

Enumeration

# ContentSizeCategory

The sizes that you can specify for content.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    enum ContentSizeCategory

Deprecated

Use `DynamicTypeSize` instead.

## Topics

### Content size categories

`case accessibilityExtraExtraExtraLarge`

`case accessibilityExtraExtraLarge`

`case accessibilityExtraLarge`

`case accessibilityLarge`

`case accessibilityMedium`

`case extraExtraExtraLarge`

`case extraExtraLarge`

`case extraLarge`

`case extraSmall`

`case large`

`case medium`

`case small`

### Creating a size category

`init?(UIContentSizeCategory)`

Create a size category from its UIContentSizeCategory equivalent.

### Comparing content size categories

`var isAccessibilityCategory: Bool`

A Boolean value indicating whether the content size category is one that is
associated with accessibility.

### Operators

`static func < (ContentSizeCategory, ContentSizeCategory) -> Bool`

Returns a Boolean value indicating whether the value of the first argument is
less than that of the second argument.

`static func > (ContentSizeCategory, ContentSizeCategory) -> Bool`

Returns a Boolean value indicating whether the value of the first argument is
greater than that of the second argument.

`static func <= (ContentSizeCategory, ContentSizeCategory) -> Bool`

Returns a Boolean value indicating whether the value of the first argument is
less than or equal to that of the second argument.

`static func >= (ContentSizeCategory, ContentSizeCategory) -> Bool`

Returns a Boolean value indicating whether the value of the first argument is
greater than or equal to that of the second argument.

## Relationships

### Conforms To

  * `CaseIterable`
  * `Equatable`
  * `Hashable`

