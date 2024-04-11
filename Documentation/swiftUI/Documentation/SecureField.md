Initializer

# init(_:text:prompt:)

Creates a secure field with a prompt generated from a `Text`.

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

    

The key for the field’s localized title. The title describes the purpose of
the field.

`text`

    

A binding to the text that the field displays and edits.

`prompt`

    

A `Text` view that represents the secure field’s prompt. The prompt provides
guidance on what people should type into the secure field.

## Discussion

Use the `onSubmit(of:_:)` modifier to invoke an action whenever someone
submits this secure field — for example, by pressing the Return key.

## See Also

### Creating a secure text field

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

Initializer

# init(_:text:prompt:)

Creates a secure field with a prompt generated from a `Text`.

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

    

A string that describes the purpose of the field.

`text`

    

A binding to the text that the field displays and edits.

`prompt`

    

A `Text` view that represents the secure field’s prompt. The prompt provides
guidance on what people should type into the secure field.

## Discussion

Use the `onSubmit(of:_:)` modifier to invoke an action whenever someone
submits this secure field — for example, by pressing the Return key.

## See Also

### Creating a secure text field

`init(LocalizedStringKey, text: Binding<String>, prompt: Text?)`

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

Initializer

# init(text:prompt:label:)

Creates a secure field with a prompt generated from a `Text`.

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

    

A binding to the text that the field displays and edits.

`prompt`

    

A `Text` view that represents the secure field’s prompt. The prompt provides
guidance on what people should type into the secure field.

`label`

    

A view that describes the purpose of the secure field.

## Discussion

Use the `onSubmit(of:_:)` modifier to invoke an action whenever someone
submits this secure field — for example, by pressing the Return key.

## See Also

### Creating a secure text field

`init(LocalizedStringKey, text: Binding<String>, prompt: Text?)`

Creates a secure field with a prompt generated from a `Text`.

Available when `Label` is `Text`.

`init<S>(S, text: Binding<String>, prompt: Text?)`

Creates a secure field with a prompt generated from a `Text`.

Available when `Label` is `Text`.

`init(LocalizedStringKey, text: Binding<String>)`

Creates a secure field with a prompt generated from a `Text`.

Available when `Label` is `Text`.

`init<S>(S, text: Binding<String>)`

Creates a secure field with a prompt generated from a `Text`.

Available when `Label` is `Text`.

Initializer

# init(_:text:)

Creates a secure field with a prompt generated from a `Text`.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        text: Binding<String>
    )

Available when `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the field’s localized title. The title describes the purpose of
the field.

`text`

    

A binding to the text that the field displays and edits.

## Discussion

Use the `onSubmit(of:_:)` modifier to invoke an action whenever someone
submits this secure field — for example, by pressing the Return key.

## See Also

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

`init<S>(S, text: Binding<String>)`

Creates a secure field with a prompt generated from a `Text`.

Available when `Label` is `Text`.

Initializer

# init(_:text:)

Creates a secure field with a prompt generated from a `Text`.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        text: Binding<String>
    ) where S : StringProtocol

Available when `Label` is `Text`.

##  Parameters

`title`

    

A string that describes the purpose of the field.

`text`

    

A binding to the text that the field displays and edits.

## Discussion

Use the `onSubmit(of:_:)` modifier to invoke an action whenever someone
submits this secure field — for example, by pressing the Return key.

## See Also

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

Initializer

# init(_:text:onCommit:)

Creates an instance.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        text: Binding<String>,
        onCommit: @escaping () -> Void
    )

Available when `Label` is `Text`.

Deprecated

Use `init(_:text:prompt:)` instead. Add the `onSubmit(of:_:)` view modifier
for the `onCommit` behavior.

##  Parameters

`titleKey`

    

The key for the localized title of `self`, describing its purpose.

`text`

    

The text to display and edit.

`onCommit`

    

The action to perform when the user performs an action (usually pressing the
Return key) while the secure field has focus.

## See Also

### Deprecated initializers

`init<S>(S, text: Binding<String>, onCommit: () -> Void)`

Creates an instance.

Available when `Label` is `Text`.

Deprecated

Initializer

# init(_:text:onCommit:)

Creates an instance.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        text: Binding<String>,
        onCommit: @escaping () -> Void
    ) where S : StringProtocol

Available when `Label` is `Text`.

Deprecated

Use `init(_:text:prompt:)` instead. Add the `onSubmit(of:_:)` view modifier
for the `onCommit` behavior.

##  Parameters

`title`

    

The title of `self`, describing its purpose.

`text`

    

The text to display and edit.

`onCommit`

    

The action to perform when the user performs an action (usually pressing the
Return key) while the secure field has focus.

## See Also

### Deprecated initializers

`init(LocalizedStringKey, text: Binding<String>, onCommit: () -> Void)`

Creates an instance.

Available when `Label` is `Text`.

Deprecated

