Initializer

# init(_:text:onEditingChanged:onCommit:)

Creates a text field with a text label generated from a localized title
string.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        text: Binding<String>,
        onEditingChanged: @escaping (Bool) -> Void,
        onCommit: @escaping () -> Void
    )

Available when `Label` is `Text`.

Deprecated

Use `init(_:text:prompt:)` instead. Add the `onSubmit(of:_:)` view modifier
for the `onCommit` behavior. Use `FocusState` and `focused(_:equals:)` for the
`onEditingChanged` behavior.

##  Parameters

`titleKey`

    

The key for the localized title of the text field, describing its purpose.

`text`

    

The text to display and edit.

`onEditingChanged`

    

The action to perform when the user begins editing `text` and after the user
finishes editing `text`. The closure receives a Boolean value that indicates
the editing status: `true` when the user begins editing, `false` when they
finish.

`onCommit`

    

An action to perform when the user performs an action (for example, when the
user presses the Return key) while the text field has focus.

## See Also

### Creating a text field with a string

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

Initializer

# init(_:text:onEditingChanged:onCommit:)

Creates a text field with a text label generated from a title string.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        text: Binding<String>,
        onEditingChanged: @escaping (Bool) -> Void,
        onCommit: @escaping () -> Void
    ) where S : StringProtocol

Available when `Label` is `Text`.

Deprecated

Use `init(_:text:prompt:)` instead. Add the `onSubmit(of:_:)` view modifier
for the `onCommit` behavior. Use `FocusState` and `focused(_:equals:)` for the
`onEditingChanged` behavior.

##  Parameters

`title`

    

The title of the text view, describing its purpose.

`text`

    

The text to display and edit.

`onEditingChanged`

    

The action to perform when the user begins editing `text` and after the user
finishes editing `text`. The closure receives a Boolean value that indicates
the editing status: `true` when the user begins editing, `false` when they
finish.

`onCommit`

    

An action to perform when the user performs an action (for example, when the
user presses the Return key) while the text field has focus.

## See Also

### Creating a text field with a string

`init(LocalizedStringKey, text: Binding<String>, onEditingChanged: (Bool) ->
Void, onCommit: () -> Void)`

Creates a text field with a text label generated from a localized title
string.

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

Initializer

# init(_:text:onCommit:)

Creates a text field with a text label generated from a title string.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        text: Binding<String>,
        onCommit: @escaping () -> Void
    ) where S : StringProtocol

Available when `Label` is `Text`.

##  Parameters

`title`

    

The title of the text view, describing its purpose.

`text`

    

The text to display and edit.

`onEditingChanged`

    

The action to perform when the user begins editing `text` and after the user
finishes editing `text`. The closure receives a Boolean value that indicates
the editing status: `true` when the user begins editing, `false` when they
finish.

`onCommit`

    

An action to perform when the user performs an action (for example, when the
user presses the Return key) while the text field has focus.

## See Also

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

Initializer

# init(_:text:onCommit:)

Creates a text field with a text label generated from a localized title
string.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        text: Binding<String>,
        onCommit: @escaping () -> Void
    )

Available when `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the localized title of the text field, describing its purpose.

`text`

    

The text to display and edit.

`onCommit`

    

An action to perform when the user performs an action (for example, when the
user presses the Return key) while the text field has focus.

## See Also

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

`init(LocalizedStringKey, text: Binding<String>, onEditingChanged: (Bool) ->
Void)`

Creates a text field with a text label generated from a localized title
string.

Available when `Label` is `Text`.

`init<S>(S, text: Binding<String>, onEditingChanged: (Bool) -> Void)`

Creates a text field with a text label generated from a title string.

Available when `Label` is `Text`.

Initializer

# init(_:text:onEditingChanged:)

Creates a text field with a text label generated from a localized title
string.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        text: Binding<String>,
        onEditingChanged: @escaping (Bool) -> Void
    )

Available when `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the localized title of the text field, describing its purpose.

`text`

    

The text to display and edit.

`onEditingChanged`

    

The action to perform when the user begins editing `text` and after the user
finishes editing `text`. The closure receives a Boolean value that indicates
the editing status: `true` when the user begins editing, `false` when they
finish.

## See Also

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

`init<S>(S, text: Binding<String>, onEditingChanged: (Bool) -> Void)`

Creates a text field with a text label generated from a title string.

Available when `Label` is `Text`.

Initializer

# init(_:text:onEditingChanged:)

Creates a text field with a text label generated from a title string.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        text: Binding<String>,
        onEditingChanged: @escaping (Bool) -> Void
    ) where S : StringProtocol

Available when `Label` is `Text`.

##  Parameters

`title`

    

The title of the text view, describing its purpose.

`text`

    

The text to display and edit.

`onEditingChanged`

    

The action to perform when the user begins editing `text` and after the user
finishes editing `text`. The closure receives a Boolean value that indicates
the editing status: `true` when the user begins editing, `false` when they
finish.

## See Also

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

Initializer

# init(_:value:formatter:onEditingChanged:onCommit:)

Creates an instance which binds over an arbitrary type, `T`.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    init<V>(
        _ titleKey: LocalizedStringKey,
        value: Binding<V>,
        formatter: Formatter,
        onEditingChanged: @escaping (Bool) -> Void,
        onCommit: @escaping () -> Void
    )

Available when `Label` is `Text`.

Deprecated

Use `init(_:value:formatter:prompt:)` instead. Add the `onSubmit(of:_:)` view
modifier for the `onCommit` behavior. Use `FocusState` and
`focused(_:equals:)` for the `onEditingChanged` behavior.

##  Parameters

`titleKey`

    

The key for the localized title of the text field, describing its purpose.

`value`

    

The underlying value to be edited.

`formatter`

    

A formatter to use when converting between the string the user edits and the
underlying value of type `T`. In the event that `formatter` is unable to
perform the conversion, `binding.value` isn’t modified.

`onEditingChanged`

    

The action to perform when the user begins editing `text` and after the user
finishes editing `text`. The closure receives a Boolean value that indicates
the editing status: `true` when the user begins editing, `false` when they
finish.

`onCommit`

    

An action to perform when the user performs an action (for example, when the
user presses the Return key) while the text field has focus.

## See Also

### Creating a text field with a value

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

Initializer

# init(_:value:formatter:onEditingChanged:onCommit:)

Creates an instance which binds over an arbitrary type, `T`.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    init<S, V>(
        _ title: S,
        value: Binding<V>,
        formatter: Formatter,
        onEditingChanged: @escaping (Bool) -> Void,
        onCommit: @escaping () -> Void
    ) where S : StringProtocol

Available when `Label` is `Text`.

Deprecated

Use `init(_:value:formatter:prompt:)` instead. Add the `onSubmit(of:_:)` view
modifier for the `onCommit` behavior. Use `FocusState` and
`focused(_:equals:)` for the `onEditingChanged` behavior.

##  Parameters

`title`

    

The title of the text field, describing its purpose.

`value`

    

The underlying value to be edited.

`formatter`

    

A formatter to use when converting between the string the user edits and the
underlying value of type `T`. In the event that `formatter` is unable to
perform the conversion, `binding.value` isn’t modified.

`onEditingChanged`

    

The action to perform when the user begins editing `text` and after the user
finishes editing `text`. The closure receives a Boolean value that indicates
the editing status: `true` when the user begins editing, `false` when they
finish.

`onCommit`

    

An action to perform when the user performs an action (for example, when the
user presses the Return key) while the text field has focus.

## See Also

### Creating a text field with a value

`init<V>(LocalizedStringKey, value: Binding<V>, formatter: Formatter,
onEditingChanged: (Bool) -> Void, onCommit: () -> Void)`

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

Initializer

# init(_:value:formatter:onCommit:)

Create an instance which binds over an arbitrary type, `V`.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    init<V>(
        _ titleKey: LocalizedStringKey,
        value: Binding<V>,
        formatter: Formatter,
        onCommit: @escaping () -> Void
    )

Available when `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the localized title of the text field, describing its purpose.

`value`

    

The underlying value to be edited.

`formatter`

    

A formatter to use when converting between the string the user edits and the
underlying value of type `V`. In the event that `formatter` is unable to
perform the conversion, `binding.value` isn’t modified.

`onCommit`

    

An action to perform when the user performs an action (for example, when the
user presses the Return key) while the text field has focus.

## See Also

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

Initializer

# init(_:value:formatter:onCommit:)

Create an instance which binds over an arbitrary type, `V`.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    init<S, V>(
        _ title: S,
        value: Binding<V>,
        formatter: Formatter,
        onCommit: @escaping () -> Void
    ) where S : StringProtocol

Available when `Label` is `Text`.

##  Parameters

`title`

    

The title of the text field, describing its purpose.

`value`

    

The underlying value to be edited.

`formatter`

    

A formatter to use when converting between the string the user edits and the
underlying value of type `V`. In the event that `formatter` is unable to
perform the conversion, `binding.value` isn’t modified.

`onCommit`

    

An action to perform when the user performs an action (for example, when the
user presses the Return key) while the text field has focus.

## See Also

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

`init<V>(LocalizedStringKey, value: Binding<V>, formatter: Formatter,
onEditingChanged: (Bool) -> Void)`

Create an instance which binds over an arbitrary type, `V`.

Available when `Label` is `Text`.

`init<S, V>(S, value: Binding<V>, formatter: Formatter, onEditingChanged:
(Bool) -> Void)`

Create an instance which binds over an arbitrary type, `V`.

Available when `Label` is `Text`.

Initializer

# init(_:value:formatter:onEditingChanged:)

Create an instance which binds over an arbitrary type, `V`.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    init<V>(
        _ titleKey: LocalizedStringKey,
        value: Binding<V>,
        formatter: Formatter,
        onEditingChanged: @escaping (Bool) -> Void
    )

Available when `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the localized title of the text field, describing its purpose.

`value`

    

The underlying value to be edited.

`formatter`

    

A formatter to use when converting between the string the user edits and the
underlying value of type `V`. In the event that `formatter` is unable to
perform the conversion, `binding.value` isn’t modified.

`onEditingChanged`

    

The action to perform when the user begins editing `text` and after the user
finishes editing `text`. The closure receives a Boolean value that indicates
the editing status: `true` when the user begins editing, `false` when they
finish.

## See Also

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

`init<S, V>(S, value: Binding<V>, formatter: Formatter, onEditingChanged:
(Bool) -> Void)`

Create an instance which binds over an arbitrary type, `V`.

Available when `Label` is `Text`.

Initializer

# init(_:value:formatter:onEditingChanged:)

Create an instance which binds over an arbitrary type, `V`.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    init<S, V>(
        _ title: S,
        value: Binding<V>,
        formatter: Formatter,
        onEditingChanged: @escaping (Bool) -> Void
    ) where S : StringProtocol

Available when `Label` is `Text`.

##  Parameters

`title`

    

The title of the text field, describing its purpose.

`value`

    

The underlying value to be edited.

`formatter`

    

A formatter to use when converting between the string the user edits and the
underlying value of type `V`. In the event that `formatter` is unable to
perform the conversion, `binding.value` isn’t modified.

`onEditingChanged`

    

The action to perform when the user begins editing `text` and after the user
finishes editing `text`. The closure receives a Boolean value that indicates
the editing status: `true` when the user begins editing, `false` when they
finish.

## See Also

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

