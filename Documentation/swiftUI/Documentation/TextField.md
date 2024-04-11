Initializer

# init(_:text:)

Creates a text field with a text label generated from a localized title
string.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        text: Binding<String>
    )

Available when `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the localized title of the text field, describing its purpose.

`text`

    

The text to display and edit.

## See Also

### Creating a text field with a string

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

Initializer

# init(_:text:)

Creates a text field with a text label generated from a title string.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        text: Binding<String>
    ) where S : StringProtocol

Available when `Label` is `Text`.

##  Parameters

`title`

    

The title of the text view, describing its purpose.

`text`

    

The text to display and edit.

## See Also

### Creating a text field with a string

`init(LocalizedStringKey, text: Binding<String>)`

Creates a text field with a text label generated from a localized title
string.

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

Initializer

# init(_:text:prompt:)

Creates a text field with a text label generated from a localized title
string.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        text: Binding<String>,
        prompt: Text?
    )

Available when `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the localized title of the text field, describing its purpose.

`text`

    

The text to display and edit.

`prompt`

    

A `Text` representing the prompt of the text field which provides users with
guidance on what to type into the text field.

## Discussion

Use the `onSubmit(of:_:)` modifier to invoke an action whenever the user
submits this text field.

## See Also

### Creating a text field with a string

`init(LocalizedStringKey, text: Binding<String>)`

Creates a text field with a text label generated from a localized title
string.

Available when `Label` is `Text`.

`init<S>(S, text: Binding<String>)`

Creates a text field with a text label generated from a title string.

Available when `Label` is `Text`.

`init<S>(S, text: Binding<String>, prompt: Text?)`

Creates a text field with a text label generated from a title string.

Available when `Label` is `Text`.

`init(text: Binding<String>, prompt: Text?, label: () -> Label)`

Creates a text field with a prompt generated from a `Text`.

Available when `Label` conforms to `View`.

Initializer

# init(_:text:prompt:)

Creates a text field with a text label generated from a title string.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        text: Binding<String>,
        prompt: Text?
    ) where S : StringProtocol

Available when `Label` is `Text`.

##  Parameters

`title`

    

The title of the text view, describing its purpose.

`text`

    

The text to display and edit.

`prompt`

    

A `Text` representing the prompt of the text field which provides users with
guidance on what to type into the text field.

## Discussion

Use the `onSubmit(of:_:)` modifier to invoke an action whenever the user
submits this text field.

## See Also

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

`init(text: Binding<String>, prompt: Text?, label: () -> Label)`

Creates a text field with a prompt generated from a `Text`.

Available when `Label` conforms to `View`.

Initializer

# init(text:prompt:label:)

Creates a text field with a prompt generated from a `Text`.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init(
        text: Binding<String>,
        prompt: Text? = nil,
        @ViewBuilder label: () -> Label
    )

Available when `Label` conforms to `View`.

##  Parameters

`text`

    

The text to display and edit.

`prompt`

    

A `Text` representing the prompt of the text field which provides users with
guidance on what to type into the text field.

`label`

    

A view that describes the purpose of the text field.

## Discussion

Use the `onSubmit(of:_:)` modifier to invoke an action whenever the user
submits this text field.

## See Also

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

Initializer

# init(_:text:axis:)

Creates a text field with a preferred axis and a text label generated from a
localized title string.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        text: Binding<String>,
        axis: Axis
    )

Available when `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the localized title of the text field, describing its purpose.

`text`

    

The text to display and edit.

`axis`

    

The axis in which to scroll text when it doesn’t fit in the available space.

## Discussion

Specify a preferred axis in which the text field should scroll its content
when it does not fit in the available space. Depending on the style of the
field, this axis may not be respected.

Use the `onSubmit(of:_:)` modifier to invoke an action whenever the user
submits this text field.

## See Also

### Creating a scrollable text field

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

Initializer

# init(_:text:axis:)

Creates a text field with a preferred axis and a text label generated from a
title string.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        text: Binding<String>,
        axis: Axis
    ) where S : StringProtocol

Available when `Label` is `Text`.

##  Parameters

`title`

    

The title of the text view, describing its purpose.

`text`

    

The text to display and edit.

`axis`

    

The axis in which to scroll text when it doesn’t fit in the available space.

## Discussion

Specify a preferred axis in which the text field should scroll its content
when it does not fit in the available space. Depending on the style of the
field, this axis may not be respected.

Use the `onSubmit(of:_:)` modifier to invoke an action whenever the user
submits this text field.

## See Also

### Creating a scrollable text field

`init(LocalizedStringKey, text: Binding<String>, axis: Axis)`

Creates a text field with a preferred axis and a text label generated from a
localized title string.

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

Initializer

# init(_:text:prompt:axis:)

Creates a text field with a preferred axis and a text label generated from a
localized title string.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        text: Binding<String>,
        prompt: Text?,
        axis: Axis
    )

Available when `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the localized title of the text field, describing its purpose.

`text`

    

The text to display and edit.

`prompt`

    

A `Text` representing the prompt of the text field which provides users with
guidance on what to type into the text field.

`axis`

    

The axis in which to scroll text when it doesn’t fit in the available space.

## Discussion

Specify a preferred axis in which the text field should scroll its content
when it does not fit in the available space. Depending on the style of the
field, this axis may not be respected.

Use the `onSubmit(of:_:)` modifier to invoke an action whenever the user
submits this text field.

## See Also

### Creating a scrollable text field

`init(LocalizedStringKey, text: Binding<String>, axis: Axis)`

Creates a text field with a preferred axis and a text label generated from a
localized title string.

Available when `Label` is `Text`.

`init<S>(S, text: Binding<String>, axis: Axis)`

Creates a text field with a preferred axis and a text label generated from a
title string.

Available when `Label` is `Text`.

`init<S>(S, text: Binding<String>, prompt: Text?, axis: Axis)`

Creates a text field with a text label generated from a title string.

Available when `Label` is `Text`.

`init(text: Binding<String>, prompt: Text?, axis: Axis, label: () -> Label)`

Creates a text field with a preferred axis and a prompt generated from a
`Text`.

Available when `Label` conforms to `View`.

Initializer

# init(_:text:prompt:axis:)

Creates a text field with a text label generated from a title string.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        text: Binding<String>,
        prompt: Text?,
        axis: Axis
    ) where S : StringProtocol

Available when `Label` is `Text`.

##  Parameters

`title`

    

The title of the text view, describing its purpose.

`text`

    

The text to display and edit.

`prompt`

    

A `Text` representing the prompt of the text field which provides users with
guidance on what to type into the text field.

`axis`

    

The axis in which to scroll text when it doesn’t fit in the available space.

## Discussion

Specify a preferred axis in which the text field should scroll its content
when it does not fit in the available space. Depending on the style of the
field, this axis may not be respected.

Use the `onSubmit(of:_:)` modifier to invoke an action whenever the user
submits this text field.

## See Also

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

`init(text: Binding<String>, prompt: Text?, axis: Axis, label: () -> Label)`

Creates a text field with a preferred axis and a prompt generated from a
`Text`.

Available when `Label` conforms to `View`.

Initializer

# init(text:prompt:axis:label:)

Creates a text field with a preferred axis and a prompt generated from a
`Text`.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init(
        text: Binding<String>,
        prompt: Text? = nil,
        axis: Axis,
        @ViewBuilder label: () -> Label
    )

Available when `Label` conforms to `View`.

##  Parameters

`text`

    

The text to display and edit.

`prompt`

    

A `Text` representing the prompt of the text field which provides users with
guidance on what to type into the text field.

`axis`

    

The axis in which to scroll text when it doesn’t fit in the available space.

`label`

    

A view that describes the purpose of the text field.

## Discussion

Specify a preferred axis in which the text field should scroll its content
when it does not fit in the available space. Depending on the style of the
field, this axis may not be respected.

Use the `onSubmit(of:_:)` modifier to invoke an action whenever the user
submits this text field.

## See Also

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

Initializer

# init(_:value:format:prompt:)

Creates a text field that applies a format style to a bound value, with a
label generated from a localized title string.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init<F>(
        _ titleKey: LocalizedStringKey,
        value: Binding<F.FormatInput>,
        format: F,
        prompt: Text? = nil
    ) where F : ParseableFormatStyle, F.FormatOutput == String

Available when `Label` is `Text`.

##  Parameters

`titleKey`

    

The title of the text field, describing its purpose.

`value`

    

The underlying value to edit.

`format`

    

A format style of type `F` to use when converting between the string the user
edits and the underlying value of type `F.FormatInput`. If `format` can’t
perform the conversion, the text field leaves `binding.value` unchanged. If
the user stops editing the text in an invalid state, the text field updates
the field’s text to the last known valid value.

`prompt`

    

A `Text` which provides users with guidance on what to type into the text
field.

## Discussion

Use this initializer to create a text field that binds to a bound value, using
a `ParseableFormatStyle` to convert to and from this type. Changes to the
bound value update the string displayed by the text field. Editing the text
field updates the bound value, as long as the format style can parse the text.
If the format style can’t parse the input, the bound value remains unchanged.

Use the `onSubmit(of:_:)` modifier to invoke an action whenever the user
submits this text field.

The following example uses a `Double` as the bound value, and a
`FloatingPointFormatStyle` instance to convert to and from a string
representation. As the user types, the bound value updates, which in turn
updates three `Text` views that use different format styles. If the user
enters text that doesn’t represent a valid `Double`, the bound value doesn’t
update.

## See Also

### Creating a text field with a value

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

Initializer

# init(_:value:format:prompt:)

Creates a text field that applies a format style to a bound value, with a
label generated from a title string.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init<S, F>(
        _ title: S,
        value: Binding<F.FormatInput>,
        format: F,
        prompt: Text? = nil
    ) where S : StringProtocol, F : ParseableFormatStyle, F.FormatOutput == String

Available when `Label` is `Text`.

##  Parameters

`title`

    

The title of the text field, describing its purpose.

`value`

    

The underlying value to edit.

`format`

    

A format style of type `F` to use when converting between the string the user
edits and the underlying value of type `F.FormatInput`. If `format` can’t
perform the conversion, the text field leaves `binding.value` unchanged. If
the user stops editing the text in an invalid state, the text field updates
the field’s text to the last known valid value.

`prompt`

    

A `Text` which provides users with guidance on what to type into the text
field.

## Discussion

Use this initializer to create a text field that binds to a bound value, using
a `ParseableFormatStyle` to convert to and from this type. Changes to the
bound value update the string displayed by the text field. Editing the text
field updates the bound value, as long as the format style can parse the text.
If the format style can’t parse the input, the bound value remains unchanged.

Use the `onSubmit(of:_:)` modifier to invoke an action whenever the user
submits this text field.

The following example uses a `Double` as the bound value, and a
`FloatingPointFormatStyle` instance to convert to and from a string
representation. As the user types, the bound value updates, which in turn
updates three `Text` views that use different format styles. If the user
enters text that doesn’t represent a valid `Double`, the bound value doesn’t
update.

## See Also

### Creating a text field with a value

`init<F>(LocalizedStringKey, value: Binding<F.FormatInput>, format: F, prompt:
Text?)`

Creates a text field that applies a format style to a bound value, with a
label generated from a localized title string.

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

Initializer

# init(value:format:prompt:label:)

Creates a text field that applies a format style to a bound value, with a
label generated from a view builder.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init<F>(
        value: Binding<F.FormatInput>,
        format: F,
        prompt: Text? = nil,
        @ViewBuilder label: () -> Label
    ) where F : ParseableFormatStyle, F.FormatOutput == String

Available when `Label` conforms to `View`.

##  Parameters

`value`

    

The underlying value to edit.

`format`

    

A format style of type `F` to use when converting between the string the user
edits and the underlying value of type `F.FormatInput`. If `format` can’t
perform the conversion, the text field leaves the value unchanged. If the user
stops editing the text in an invalid state, the text field updates the field’s
text to the last known valid value.

`prompt`

    

A `Text` which provides users with guidance on what to type into the text
field.

`label`

    

A view builder that produces a label for the text field, describing its
purpose.

## Discussion

Use this initializer to create a text field that binds to a bound value, using
a `ParseableFormatStyle` to convert to and from this type. Changes to the
bound value update the string displayed by the text field. Editing the text
field updates the bound value, as long as the format style can parse the text.
If the format style can’t parse the input, the bound value remains unchanged.

Use the `onSubmit(of:_:)` modifier to invoke an action whenever the user
submits this text field.

The following example uses a `Double` as the bound value, and a
`FloatingPointFormatStyle` instance to convert to and from a string
representation. As the user types, the bound value updates, which in turn
updates three `Text` views that use different format styles. If the user
enters text that doesn’t represent a valid `Double`, the bound value doesn’t
update.

## See Also

### Creating a text field with a value

`init<F>(LocalizedStringKey, value: Binding<F.FormatInput>, format: F, prompt:
Text?)`

Creates a text field that applies a format style to a bound value, with a
label generated from a localized title string.

Available when `Label` is `Text`.

`init<S, F>(S, value: Binding<F.FormatInput>, format: F, prompt: Text?)`

Creates a text field that applies a format style to a bound value, with a
label generated from a title string.

Available when `Label` is `Text`.

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

Initializer

# init(_:value:formatter:)

Create an instance which binds over an arbitrary type, `V`.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init<S, V>(
        _ title: S,
        value: Binding<V>,
        formatter: Formatter
    ) where S : StringProtocol

Available when `Label` is `Text`.

##  Parameters

`title`

    

The title of the text view, describing its purpose.

`value`

    

The underlying value to edit.

`formatter`

    

A formatter to use when converting between the string the user edits and the
underlying value of type `V`. If `formatter` can’t perform the conversion, the
text field doesn’t modify `binding.value`.

## Discussion

Use this initializer to create a text field that binds to a bound optional
value, using a `Formatter` to convert to and from this type. Changes to the
bound value update the string displayed by the text field. Editing the text
field updates the bound value, as long as the formatter can parse the text. If
the format style can’t parse the input, the bound value remains unchanged.

Use the `onSubmit(of:_:)` modifier to invoke an action whenever the user
submits this text field.

The following example uses a `Double` as the bound value, and a
`NumberFormatter` instance to convert to and from a string representation. The
formatter uses the `NumberFormatter.Style.decimal` style, to allow entering a
fractional part. As the user types, the bound value updates, which in turn
updates three `Text` views that use different format styles. If the user
enters text that doesn’t represent a valid `Double`, the bound value doesn’t
update.

## See Also

### Creating a text field with a value

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

Initializer

# init(_:value:formatter:)

Create an instance which binds over an arbitrary type, `V`.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init<V>(
        _ titleKey: LocalizedStringKey,
        value: Binding<V>,
        formatter: Formatter
    )

Available when `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the localized title of the text field, describing its purpose.

`value`

    

The underlying value to edit.

`formatter`

    

A formatter to use when converting between the string the user edits and the
underlying value of type `V`. If `formatter` can’t perform the conversion, the
text field doesn’t modify `binding.value`.

## Discussion

Use this initializer to create a text field that binds to a bound optional
value, using a `Formatter` to convert to and from this type. Changes to the
bound value update the string displayed by the text field. Editing the text
field updates the bound value, as long as the formatter can parse the text. If
the format style can’t parse the input, the bound value remains unchanged.

Use the `onSubmit(of:_:)` modifier to invoke an action whenever the user
submits this text field.

The following example uses a `Double` as the bound value, and a
`NumberFormatter` instance to convert to and from a string representation. The
formatter uses the `NumberFormatter.Style.decimal` style, to allow entering a
fractional part. As the user types, the bound value updates, which in turn
updates three `Text` views that use different format styles. If the user
enters text that doesn’t represent a valid `Double`, the bound value doesn’t
update.

## See Also

### Creating a text field with a value

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

Initializer

# init(_:value:formatter:prompt:)

Creates a text field that applies a formatter to a bound value, with a label
generated from a localized title string.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init<V>(
        _ titleKey: LocalizedStringKey,
        value: Binding<V>,
        formatter: Formatter,
        prompt: Text?
    )

Available when `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the localized title of the text field, describing its purpose.

`value`

    

The underlying value to edit.

`formatter`

    

A formatter to use when converting between the string the user edits and the
underlying value of type `V`. If `formatter` can’t perform the conversion, the
text field doesn’t modify `binding.value`.

`prompt`

    

A `Text` which provides users with guidance on what to enter into the text
field.

## Discussion

Use this initializer to create a text field that binds to a bound value, using
a `Formatter` to convert to and from this type. Changes to the bound value
update the string displayed by the text field. Editing the text field updates
the bound value, as long as the formatter can parse the text. If the format
style can’t parse the input, the bound value remains unchanged.

Use the `onSubmit(of:_:)` modifier to invoke an action whenever the user
submits this text field.

The following example uses a `Double` as the bound value, and a
`NumberFormatter` instance to convert to and from a string representation. The
formatter uses the `NumberFormatter.Style.decimal` style, to allow entering a
fractional part. As the user types, the bound value updates, which in turn
updates three `Text` views that use different format styles. If the user
enters text that doesn’t represent a valid `Double`, the bound value doesn’t
update.

## See Also

### Creating a text field with a value

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

`init<S, V>(S, value: Binding<V>, formatter: Formatter, prompt: Text?)`

Creates a text field that applies a formatter to a bound value, with a label
generated from a title string.

Available when `Label` is `Text`.

`init<V>(value: Binding<V>, formatter: Formatter, prompt: Text?, label: () ->
Label)`

Creates a text field that applies a formatter to a bound optional value, with
a label generated from a view builder.

Available when `Label` conforms to `View`.

Initializer

# init(_:value:formatter:prompt:)

Creates a text field that applies a formatter to a bound value, with a label
generated from a title string.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init<S, V>(
        _ title: S,
        value: Binding<V>,
        formatter: Formatter,
        prompt: Text?
    ) where S : StringProtocol

Available when `Label` is `Text`.

##  Parameters

`title`

    

The title of the text field, describing its purpose.

`value`

    

The underlying value to edit.

`formatter`

    

A formatter to use when converting between the string the user edits and the
underlying value of type `V`. If `formatter` can’t perform the conversion, the
text field doesn’t modify `binding.value`.

`prompt`

    

A `Text` which provides users with guidance on what to enter into the text
field.

## Discussion

Use this initializer to create a text field that binds to a bound value, using
a `Formatter` to convert to and from this type. Changes to the bound value
update the string displayed by the text field. Editing the text field updates
the bound value, as long as the formatter can parse the text. If the format
style can’t parse the input, the bound value remains unchanged.

Use the `onSubmit(of:_:)` modifier to invoke an action whenever the user
submits this text field.

The following example uses a `Double` as the bound value, and a
`NumberFormatter` instance to convert to and from a string representation. The
formatter uses the `NumberFormatter.Style.decimal` style, to allow entering a
fractional part. As the user types, the bound value updates, which in turn
updates three `Text` views that use different format styles. If the user
enters text that doesn’t represent a valid `Double`, the bound value doesn’t
update.

## See Also

### Creating a text field with a value

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

`init<V>(value: Binding<V>, formatter: Formatter, prompt: Text?, label: () ->
Label)`

Creates a text field that applies a formatter to a bound optional value, with
a label generated from a view builder.

Available when `Label` conforms to `View`.

Initializer

# init(value:formatter:prompt:label:)

Creates a text field that applies a formatter to a bound optional value, with
a label generated from a view builder.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init<V>(
        value: Binding<V>,
        formatter: Formatter,
        prompt: Text? = nil,
        @ViewBuilder label: () -> Label
    )

Available when `Label` conforms to `View`.

##  Parameters

`value`

    

The underlying value to edit.

`formatter`

    

A formatter to use when converting between the string the user edits and the
underlying value of type `V`. If `formatter` can’t perform the conversion, the
text field doesn’t modify `binding.value`.

`prompt`

    

A `Text` which provides users with guidance on what to enter into the text
field.

`label`

    

A view that describes the purpose of the text field.

## Discussion

Use this initializer to create a text field that binds to a bound optional
value, using a `Formatter` to convert to and from this type. Changes to the
bound value update the string displayed by the text field. Editing the text
field updates the bound value, as long as the formatter can parse the text. If
the format style can’t parse the input, the bound value remains unchanged.

Use the `onSubmit(of:_:)` modifier to invoke an action whenever the user
submits this text field.

The following example uses a `Double` as the bound value, and a
`NumberFormatter` instance to convert to and from a string representation. The
formatter uses the `NumberFormatter.Style.decimal` style, to allow entering a
fractional part. As the user types, the bound value updates, which in turn
updates three `Text` views that use different format styles. If the user
enters text that doesn’t represent a valid `Double`, the bound value doesn’t
update.

## See Also

### Creating a text field with a value

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

Initializer

# init(_:value:format:prompt:)

Creates a text field that applies a format style to a bound optional value,
with a label generated from a localized title string.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init<F>(
        _ titleKey: LocalizedStringKey,
        value: Binding<F.FormatInput?>,
        format: F,
        prompt: Text? = nil
    ) where F : ParseableFormatStyle, F.FormatOutput == String

Available when `Label` is `Text`.

##  Parameters

`titleKey`

    

The title of the text field, describing its purpose.

`value`

    

The underlying value to edit.

`format`

    

A format style of type `F` to use when converting between the string the user
edits and the underlying value of type `F.FormatInput`. If `format` can’t
perform the conversion, the text field sets `binding.value` to `nil`.

`prompt`

    

A `Text` which provides users with guidance on what to type into the text
field.

## Discussion

Use this initializer to create a text field that binds to a bound optional
value, using a `ParseableFormatStyle` to convert to and from this type.
Changes to the bound value update the string displayed by the text field.
Editing the text field updates the bound value, as long as the format style
can parse the text. If the format style can’t parse the input, the text field
sets the bound value to `nil`.

Use the `onSubmit(of:_:)` modifier to invoke an action whenever the user
submits this text field.

The following example uses an optional `Double` as the bound currency value,
and a `FloatingPointFormatStyle.Currency` instance to convert to and from a
representation as U.S. dollars. As the user types, a `View.onChange(of:_:)`
modifier logs the new value to the console. If the user enters an invalid
currency value, like letters or emoji, the console output is `Optional(nil)`.

## See Also

### Creating a text field with an optional

`init<S, F>(S, value: Binding<F.FormatInput?>, format: F, prompt: Text?)`

Creates a text field that applies a format style to a bound optional value,
with a label generated from a title string.

Available when `Label` is `Text`.

`init<F>(value: Binding<F.FormatInput?>, format: F, prompt: Text?, label: ()
-> Label)`

Creates a text field that applies a format style to a bound optional value,
with a label generated from a view builder.

Available when `Label` conforms to `View`.

Initializer

# init(_:value:format:prompt:)

Creates a text field that applies a format style to a bound optional value,
with a label generated from a title string.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init<S, F>(
        _ title: S,
        value: Binding<F.FormatInput?>,
        format: F,
        prompt: Text? = nil
    ) where S : StringProtocol, F : ParseableFormatStyle, F.FormatOutput == String

Available when `Label` is `Text`.

##  Parameters

`title`

    

The title of the text field, describing its purpose.

`value`

    

The underlying value to edit.

`format`

    

A format style of type `F` to use when converting between the string the user
edits and the underlying value of type `F.FormatInput`. If `format` can’t
perform the conversion, the text field sets `binding.value` to `nil`.

`prompt`

    

A `Text` which provides users with guidance on what to type into the text
field.

## Discussion

Use this initializer to create a text field that binds to a bound optional
value, using a `ParseableFormatStyle` to convert to and from this type.
Changes to the bound value update the string displayed by the text field.
Editing the text field updates the bound value, as long as the format style
can parse the text. If the format style can’t parse the input, the text field
sets the bound value to `nil`.

Use the `onSubmit(of:_:)` modifier to invoke an action whenever the user
submits this text field.

The following example uses an optional `Double` as the bound currency value,
and a `FloatingPointFormatStyle.Currency` instance to convert to and from a
representation as U.S. dollars. As the user types, a `View.onChange(of:_:)`
modifier logs the new value to the console. If the user enters an invalid
currency value, like letters or emoji, the console output is `Optional(nil)`.

## See Also

### Creating a text field with an optional

`init<F>(LocalizedStringKey, value: Binding<F.FormatInput?>, format: F,
prompt: Text?)`

Creates a text field that applies a format style to a bound optional value,
with a label generated from a localized title string.

Available when `Label` is `Text`.

`init<F>(value: Binding<F.FormatInput?>, format: F, prompt: Text?, label: ()
-> Label)`

Creates a text field that applies a format style to a bound optional value,
with a label generated from a view builder.

Available when `Label` conforms to `View`.

Initializer

# init(value:format:prompt:label:)

Creates a text field that applies a format style to a bound optional value,
with a label generated from a view builder.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init<F>(
        value: Binding<F.FormatInput?>,
        format: F,
        prompt: Text? = nil,
        @ViewBuilder label: () -> Label
    ) where F : ParseableFormatStyle, F.FormatOutput == String

Available when `Label` conforms to `View`.

##  Parameters

`value`

    

The underlying value to edit.

`format`

    

A format style of type `F` to use when converting between the string the user
edits and the underlying value of type `F.FormatInput`. If `format` can’t
perform the conversion, the text field sets `binding.value` to `nil`.

`prompt`

    

A `Text` which provides users with guidance on what to type into the text
field.

`label`

    

A view builder that produces a label for the text field, describing its
purpose.

## Discussion

Use this initializer to create a text field that binds to a bound optional
value, using a `ParseableFormatStyle` to convert to and from this type.
Changes to the bound value update the string displayed by the text field.
Editing the text field updates the bound value, as long as the format style
can parse the text. If the format style can’t parse the input, the text field
sets the bound value to `nil`.

Use the `onSubmit(of:_:)` modifier to invoke an action whenever the user
submits this text field.

The following example uses an optional `Double` as the bound currency value,
and a `FloatingPointFormatStyle.Currency` instance to convert to and from a
representation as U.S. dollars. As the user types, a `View.onChange(of:_:)`
modifier logs the new value to the console. If the user enters an invalid
currency value, like letters or emoji, the console output is `Optional(nil)`.

## See Also

### Creating a text field with an optional

`init<F>(LocalizedStringKey, value: Binding<F.FormatInput?>, format: F,
prompt: Text?)`

Creates a text field that applies a format style to a bound optional value,
with a label generated from a localized title string.

Available when `Label` is `Text`.

`init<S, F>(S, value: Binding<F.FormatInput?>, format: F, prompt: Text?)`

Creates a text field that applies a format style to a bound optional value,
with a label generated from a title string.

Available when `Label` is `Text`.

Collection

API Collection

# Deprecated initializers

Review deprecated text field initializers.

## Overview

Use view modifiers to specify change and commit behaviors for a text field
when replacing these initializers. Use the `onSubmit(of:_:)` view modifier to
get the behavior provided by the `onCommit` parameter. Use
`focused(_:equals:)` and `FocusState` to get the behavior provided by the
`onEditingChanged` parameter.

## Topics

### Creating a text field with a string

`init(LocalizedStringKey, text: Binding<String>, onEditingChanged: (Bool) ->
Void, onCommit: () -> Void)`

Creates a text field with a text label generated from a localized title
string.

Available when `Label` is `Text`.

Deprecated

`init<S>(S, text: Binding<String>, onEditingChanged: (Bool) -> Void, onCommit:
() -> Void)`

Creates a text field with a text label generated from a title string.

Available when `Label` is `Text`.

Deprecated

`init<S>(S, text: Binding<String>, onCommit: () -> Void)`

Creates a text field with a text label generated from a title string.

Available when `Label` is `Text`.

`init(LocalizedStringKey, text: Binding<String>, onCommit: () -> Void)`

Creates a text field with a text label generated from a localized title
string.

Available when `Label` is `Text`.

`init(LocalizedStringKey, text: Binding<String>, onEditingChanged: (Bool) ->
Void)`

Creates a text field with a text label generated from a localized title
string.

Available when `Label` is `Text`.

`init<S>(S, text: Binding<String>, onEditingChanged: (Bool) -> Void)`

Creates a text field with a text label generated from a title string.

Available when `Label` is `Text`.

### Creating a text field with a value

`init<V>(LocalizedStringKey, value: Binding<V>, formatter: Formatter,
onEditingChanged: (Bool) -> Void, onCommit: () -> Void)`

Creates an instance which binds over an arbitrary type, `T`.

Available when `Label` is `Text`.

Deprecated

`init<S, V>(S, value: Binding<V>, formatter: Formatter, onEditingChanged:
(Bool) -> Void, onCommit: () -> Void)`

Creates an instance which binds over an arbitrary type, `T`.

Available when `Label` is `Text`.

Deprecated

`init<V>(LocalizedStringKey, value: Binding<V>, formatter: Formatter,
onCommit: () -> Void)`

Create an instance which binds over an arbitrary type, `V`.

Available when `Label` is `Text`.

`init<S, V>(S, value: Binding<V>, formatter: Formatter, onCommit: () -> Void)`

Create an instance which binds over an arbitrary type, `V`.

Available when `Label` is `Text`.

`init<V>(LocalizedStringKey, value: Binding<V>, formatter: Formatter,
onEditingChanged: (Bool) -> Void)`

Create an instance which binds over an arbitrary type, `V`.

Available when `Label` is `Text`.

`init<S, V>(S, value: Binding<V>, formatter: Formatter, onEditingChanged:
(Bool) -> Void)`

Create an instance which binds over an arbitrary type, `V`.

Available when `Label` is `Text`.

