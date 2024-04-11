Initializer

# init(_:content:)

Creates a labeled view that generates its label from a localized string key.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        @ViewBuilder content: () -> Content
    )

Available when `Label` is `Text` and `Content` conforms to `View`.

##  Parameters

`titleKey`

    

The key for the view’s localized title, that describes the purpose of the
view.

`content`

    

The value content being labeled.

## Discussion

This initializer creates a `Text` label on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

### Creating labeled content

`init<S>(S, content: () -> Content)`

Creates a labeled view that generates its label from a string.

Available when `Label` is `Text` and `Content` conforms to `View`.

`init(content: () -> Content, label: () -> Label)`

Creates a standard labeled element, with a view that conveys the value of the
element and a label.

Available when `Label` conforms to `View` and `Content` conforms to `View`.

Initializer

# init(_:content:)

Creates a labeled view that generates its label from a string.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        @ViewBuilder content: () -> Content
    ) where S : StringProtocol

Available when `Label` is `Text` and `Content` conforms to `View`.

##  Parameters

`title`

    

A string that describes the purpose of the view.

`content`

    

The value content being labeled.

## Discussion

This initializer creates a `Text` label on your behalf, and treats the title
similar to `init(_:)`. See `Text` for more information about localizing
strings.

## See Also

### Creating labeled content

`init(LocalizedStringKey, content: () -> Content)`

Creates a labeled view that generates its label from a localized string key.

Available when `Label` is `Text` and `Content` conforms to `View`.

`init(content: () -> Content, label: () -> Label)`

Creates a standard labeled element, with a view that conveys the value of the
element and a label.

Available when `Label` conforms to `View` and `Content` conforms to `View`.

Initializer

# init(content:label:)

Creates a standard labeled element, with a view that conveys the value of the
element and a label.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init(
        @ViewBuilder content: () -> Content,
        @ViewBuilder label: () -> Label
    )

Available when `Label` conforms to `View` and `Content` conforms to `View`.

##  Parameters

`content`

    

The view that conveys the value of the resulting labeled element.

`label`

    

The label that describes the purpose of the result.

## See Also

### Creating labeled content

`init(LocalizedStringKey, content: () -> Content)`

Creates a labeled view that generates its label from a localized string key.

Available when `Label` is `Text` and `Content` conforms to `View`.

`init<S>(S, content: () -> Content)`

Creates a labeled view that generates its label from a string.

Available when `Label` is `Text` and `Content` conforms to `View`.

Initializer

# init(_:value:)

Creates a labeled informational view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init<S>(
        _ titleKey: LocalizedStringKey,
        value: S
    ) where S : StringProtocol

Available when `Label` is `Text` and `Content` is `Text`.

##  Parameters

`titleKey`

    

The key for the view’s localized title, that describes the purpose of the
view.

`value`

    

The value being labeled.

## Discussion

This initializer creates a `Text` label on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

In some contexts, this text will be selectable by default.

## See Also

### Creating informational views

`init<S1, S2>(S1, value: S2)`

Creates a labeled informational view.

Available when `Label` is `Text` and `Content` is `Text`.

Initializer

# init(_:value:)

Creates a labeled informational view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init<S1, S2>(
        _ title: S1,
        value: S2
    ) where S1 : StringProtocol, S2 : StringProtocol

Available when `Label` is `Text` and `Content` is `Text`.

##  Parameters

`title`

    

A string that describes the purpose of the view.

`value`

    

The value being labeled.

## Discussion

This initializer creates a `Text` label on your behalf, and treats the title
similar to `init(_:)`. See `Text` for more information about localizing
strings.

## See Also

### Creating informational views

`init<S>(LocalizedStringKey, value: S)`

Creates a labeled informational view.

Available when `Label` is `Text` and `Content` is `Text`.

Initializer

# init(_:value:format:)

Creates a labeled informational view from a formatted value.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init<F>(
        _ titleKey: LocalizedStringKey,
        value: F.FormatInput,
        format: F
    ) where F : FormatStyle, F.FormatInput : Equatable, F.FormatOutput == String

Available when `Label` is `Text` and `Content` is `Text`.

##  Parameters

`titleKey`

    

The key for the view’s localized title, that describes the purpose of the
view.

`value`

    

The value being labeled.

`format`

    

A format style of type `F` to convert the underlying value of type
`F.FormatInput` to a string representation.

## Discussion

This initializer creates a `Text` label on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

### Creating formatted labeled content

`init<S, F>(S, value: F.FormatInput, format: F)`

Creates a labeled informational view from a formatted value.

Available when `Label` is `Text` and `Content` is `Text`.

Initializer

# init(_:value:format:)

Creates a labeled informational view from a formatted value.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init<S, F>(
        _ title: S,
        value: F.FormatInput,
        format: F
    ) where S : StringProtocol, F : FormatStyle, F.FormatInput : Equatable, F.FormatOutput == String

Available when `Label` is `Text` and `Content` is `Text`.

##  Parameters

`title`

    

A string that describes the purpose of the view.

`value`

    

The value being labeled.

`format`

    

A format style of type `F` to convert the underlying value of type
`F.FormatInput` to a string representation.

## Discussion

This initializer creates a `Text` label on your behalf, and treats the title
similar to `init(_:)`. See `Text` for more information about localizing
strings.

## See Also

### Creating formatted labeled content

`init<F>(LocalizedStringKey, value: F.FormatInput, format: F)`

Creates a labeled informational view from a formatted value.

Available when `Label` is `Text` and `Content` is `Text`.

Initializer

# init(_:)

Creates labeled content based on a labeled content style configuration.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init(_ configuration: LabeledContentStyleConfiguration)

Available when `Label` is `LabeledContentStyleConfiguration.Label` and
`Content` is `LabeledContentStyleConfiguration.Content`.

##  Parameters

`configuration`

    

The properties of the labeled content

## Discussion

You can use this initializer within the `makeBody(configuration:)` method of a
`LabeledContentStyle` to create a labeled content instance. This is useful for
custom styles that only modify the current style, as opposed to implementing a
brand new style.

For example, the following style adds a red border around the labeled content,
but otherwise preserves the current style:

