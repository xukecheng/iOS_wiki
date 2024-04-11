Initializer

# init(_:content:)

Creates a disclosure group, using a provided string to create a text view for
the label.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    init<S>(
        _ label: S,
        @ViewBuilder content: @escaping () -> Content
    ) where S : StringProtocol

Available when `Label` is `Text` and `Content` conforms to `View`.

##  Parameters

`label`

    

A description of the content of the disclosure group.

`content`

    

The content shown when the disclosure group expands.

## See Also

### Creating a group with a string label

`init(LocalizedStringKey, content: () -> Content)`

Creates a disclosure group, using a provided localized string key to create a
text view for the label.

Available when `Label` is `Text` and `Content` conforms to `View`.

`init(LocalizedStringKey, isExpanded: Binding<Bool>, content: () -> Content)`

Creates a disclosure group, using a provided localized string key to create a
text view for the label, and a binding to the expansion state (expanded or
collapsed).

Available when `Label` is `Text` and `Content` conforms to `View`.

`init<S>(S, isExpanded: Binding<Bool>, content: () -> Content)`

Creates a disclosure group, using a provided string to create a text view for
the label, and a binding to the expansion state (expanded or collapsed).

Available when `Label` is `Text` and `Content` conforms to `View`.

Initializer

# init(_:content:)

Creates a disclosure group, using a provided localized string key to create a
text view for the label.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        @ViewBuilder content: @escaping () -> Content
    )

Available when `Label` is `Text` and `Content` conforms to `View`.

##  Parameters

`titleKey`

    

The key for the localized label of `self` that describes the content of the
disclosure group.

`content`

    

The content shown when the disclosure group expands.

## See Also

### Creating a group with a string label

`init<S>(S, content: () -> Content)`

Creates a disclosure group, using a provided string to create a text view for
the label.

Available when `Label` is `Text` and `Content` conforms to `View`.

`init(LocalizedStringKey, isExpanded: Binding<Bool>, content: () -> Content)`

Creates a disclosure group, using a provided localized string key to create a
text view for the label, and a binding to the expansion state (expanded or
collapsed).

Available when `Label` is `Text` and `Content` conforms to `View`.

`init<S>(S, isExpanded: Binding<Bool>, content: () -> Content)`

Creates a disclosure group, using a provided string to create a text view for
the label, and a binding to the expansion state (expanded or collapsed).

Available when `Label` is `Text` and `Content` conforms to `View`.

Initializer

# init(_:isExpanded:content:)

Creates a disclosure group, using a provided localized string key to create a
text view for the label, and a binding to the expansion state (expanded or
collapsed).

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        isExpanded: Binding<Bool>,
        @ViewBuilder content: @escaping () -> Content
    )

Available when `Label` is `Text` and `Content` conforms to `View`.

##  Parameters

`titleKey`

    

The key for the localized label of `self` that describes the content of the
disclosure group.

`isExpanded`

    

A binding to a Boolean value that determines the group’s expansion state
(expanded or collapsed).

`content`

    

The content shown when the disclosure group expands.

## See Also

### Creating a group with a string label

`init<S>(S, content: () -> Content)`

Creates a disclosure group, using a provided string to create a text view for
the label.

Available when `Label` is `Text` and `Content` conforms to `View`.

`init(LocalizedStringKey, content: () -> Content)`

Creates a disclosure group, using a provided localized string key to create a
text view for the label.

Available when `Label` is `Text` and `Content` conforms to `View`.

`init<S>(S, isExpanded: Binding<Bool>, content: () -> Content)`

Creates a disclosure group, using a provided string to create a text view for
the label, and a binding to the expansion state (expanded or collapsed).

Available when `Label` is `Text` and `Content` conforms to `View`.

Initializer

# init(_:isExpanded:content:)

Creates a disclosure group, using a provided string to create a text view for
the label, and a binding to the expansion state (expanded or collapsed).

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    init<S>(
        _ label: S,
        isExpanded: Binding<Bool>,
        @ViewBuilder content: @escaping () -> Content
    ) where S : StringProtocol

Available when `Label` is `Text` and `Content` conforms to `View`.

##  Parameters

`label`

    

A description of the content of the disclosure group.

`isExpanded`

    

A binding to a Boolean value that determines the group’s expansion state
(expanded or collapsed).

`content`

    

The content shown when the disclosure group expands.

## See Also

### Creating a group with a string label

`init<S>(S, content: () -> Content)`

Creates a disclosure group, using a provided string to create a text view for
the label.

Available when `Label` is `Text` and `Content` conforms to `View`.

`init(LocalizedStringKey, content: () -> Content)`

Creates a disclosure group, using a provided localized string key to create a
text view for the label.

Available when `Label` is `Text` and `Content` conforms to `View`.

`init(LocalizedStringKey, isExpanded: Binding<Bool>, content: () -> Content)`

Creates a disclosure group, using a provided localized string key to create a
text view for the label, and a binding to the expansion state (expanded or
collapsed).

Available when `Label` is `Text` and `Content` conforms to `View`.

Initializer

# init(content:label:)

Creates a disclosure group with the given label and content views.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    init(
        @ViewBuilder content: @escaping () -> Content,
        @ViewBuilder label: () -> Label
    )

##  Parameters

`content`

    

The content shown when the disclosure group expands.

`label`

    

A view that describes the content of the disclosure group.

## See Also

### Creating a group with a label view

`init(isExpanded: Binding<Bool>, content: () -> Content, label: () -> Label)`

Creates a disclosure group with the given label and content views, and a
binding to the expansion state (expanded or collapsed).

Initializer

# init(isExpanded:content:label:)

Creates a disclosure group with the given label and content views, and a
binding to the expansion state (expanded or collapsed).

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    init(
        isExpanded: Binding<Bool>,
        @ViewBuilder content: @escaping () -> Content,
        @ViewBuilder label: () -> Label
    )

##  Parameters

`isExpanded`

    

A binding to a Boolean value that determines the group’s expansion state
(expanded or collapsed).

`content`

    

The content shown when the disclosure group expands.

`label`

    

A view that describes the content of the disclosure group.

## See Also

### Creating a group with a label view

`init(content: () -> Content, label: () -> Label)`

Creates a disclosure group with the given label and content views.

