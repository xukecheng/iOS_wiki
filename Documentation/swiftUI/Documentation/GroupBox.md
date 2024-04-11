Initializer

# init(content:)

Creates an unlabeled group box with the provided view content.

iOS 14.0+  iPadOS 14.0+  macOS 10.15+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    init(@ViewBuilder content: () -> Content)

Available when `Label` is `EmptyView` and `Content` conforms to `View`.

##  Parameters

`content`

    

A `ViewBuilder` that produces the content for the group box.

## See Also

### Creating a group box

`init(content: () -> Content, label: () -> Label)`

Creates a group box with the provided label and view content.

`init(LocalizedStringKey, content: () -> Content)`

Creates a group box with the provided view content and title.

Available when `Label` is `Text` and `Content` conforms to `View`.

`init<S>(S, content: () -> Content)`

Creates a group box with the provided view content.

Available when `Label` is `Text` and `Content` conforms to `View`.

Initializer

# init(content:label:)

Creates a group box with the provided label and view content.

iOS 14.0+  iPadOS 14.0+  macOS 10.15+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    init(
        @ViewBuilder content: () -> Content,
        @ViewBuilder label: () -> Label
    )

##  Parameters

`content`

    

A `ViewBuilder` that produces the content for the group box.

`label`

    

A `ViewBuilder` that produces a label for the group box.

## See Also

### Creating a group box

`init(content: () -> Content)`

Creates an unlabeled group box with the provided view content.

Available when `Label` is `EmptyView` and `Content` conforms to `View`.

`init(LocalizedStringKey, content: () -> Content)`

Creates a group box with the provided view content and title.

Available when `Label` is `Text` and `Content` conforms to `View`.

`init<S>(S, content: () -> Content)`

Creates a group box with the provided view content.

Available when `Label` is `Text` and `Content` conforms to `View`.

Initializer

# init(_:content:)

Creates a group box with the provided view content and title.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        @ViewBuilder content: () -> Content
    )

Available when `Label` is `Text` and `Content` conforms to `View`.

##  Parameters

`titleKey`

    

The key for the group box’s title, which describes the content of the group
box.

`content`

    

A `ViewBuilder` that produces the content for the group box.

## See Also

### Creating a group box

`init(content: () -> Content)`

Creates an unlabeled group box with the provided view content.

Available when `Label` is `EmptyView` and `Content` conforms to `View`.

`init(content: () -> Content, label: () -> Label)`

Creates a group box with the provided label and view content.

`init<S>(S, content: () -> Content)`

Creates a group box with the provided view content.

Available when `Label` is `Text` and `Content` conforms to `View`.

Initializer

# init(_:content:)

Creates a group box with the provided view content.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        @ViewBuilder content: () -> Content
    ) where S : StringProtocol

Available when `Label` is `Text` and `Content` conforms to `View`.

##  Parameters

`title`

    

A string that describes the content of the group box.

`content`

    

A `ViewBuilder` that produces the content for the group box.

## See Also

### Creating a group box

`init(content: () -> Content)`

Creates an unlabeled group box with the provided view content.

Available when `Label` is `EmptyView` and `Content` conforms to `View`.

`init(content: () -> Content, label: () -> Label)`

Creates a group box with the provided label and view content.

`init(LocalizedStringKey, content: () -> Content)`

Creates a group box with the provided view content and title.

Available when `Label` is `Text` and `Content` conforms to `View`.

Initializer

# init(_:)

Creates a group box based on a style configuration.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    init(_ configuration: GroupBoxStyleConfiguration)

Available when `Label` is `GroupBoxStyleConfiguration.Label` and `Content` is
`GroupBoxStyleConfiguration.Content`.

##  Parameters

`configuration`

    

The properties of the group box instance being created.

## Discussion

Use this initializer within the `makeBody(configuration:)` method of a
`GroupBoxStyle` instance to create a styled group box, with customizations,
while preserving its existing style.

The following example adds a pink border around the group box, without
overriding its current style:

Initializer

# init(label:content:)

iOS 14.0–17.4  Deprecated  iPadOS 14.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 14.0–17.4  Deprecated  visionOS 1.0+

    
    
    init(
        label: Label,
        @ViewBuilder content: () -> Content
    )

Available when `Label` conforms to `View` and `Content` conforms to `View`.

