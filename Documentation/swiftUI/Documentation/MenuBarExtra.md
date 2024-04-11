Initializer

# init(_:content:)

Creates a menu bar extra with a key for a localized string to use as the
label. The extra defines the primary scene of an `App`.

macOS 13.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        @ViewBuilder content: () -> Content
    )

Available when `Label` is `Text` and `Content` conforms to `View`.

##  Parameters

`titleKey`

    

The title key to use for the label of the item.

`content`

    

A `View` to display when the user selects the item.

## Discussion

When this item is removed from the system menu bar by the user, the
application will be automatically quit. As such, it should not be used in
conjunction with other scene types in your `App`.

## See Also

### Creating a menu bar extra

`init<S>(S, content: () -> Content)`

Creates a menu bar extra with a string to use as the label. The item defines
the primary scene of an `App`.

Available when `Label` is `Text` and `Content` conforms to `View`.

`init(content: () -> Content, label: () -> Label)`

Creates a menu bar extra that will be displayed in the system menu bar, and
defines the primary scene of an `App`.

`init(LocalizedStringKey, isInserted: Binding<Bool>, content: () -> Content)`

Creates a menu bar extra with a key for a localized string to use as the
label. The item will be displayed in the system menu bar when the specified
binding is set to `true`. If the user removes the item from the menu bar, the
binding will be set to `false`.

Available when `Label` is `Text` and `Content` conforms to `View`.

`init<S>(S, isInserted: Binding<Bool>, content: () -> Content)`

Creates a menu bar extra with a string to use as the label. The item will be
displayed in the system menu bar when the specified binding is set to `true`.
If the user removes the item from the menu bar, the binding will be set to
`false`.

Available when `Label` is `Text` and `Content` conforms to `View`.

`init(isInserted: Binding<Bool>, content: () -> Content, label: () -> Label)`

Creates a menu bar extra. The item will be displayed in the system menu bar
when the specified binding is set to `true`. If the user removes the item from
the menu bar, the binding will be set to `false`.

Initializer

# init(_:content:)

Creates a menu bar extra with a string to use as the label. The item defines
the primary scene of an `App`.

macOS 13.0+

    
    
    init<S>(
        _ title: S,
        @ViewBuilder content: () -> Content
    ) where S : StringProtocol

Available when `Label` is `Text` and `Content` conforms to `View`.

##  Parameters

`title`

    

The string to use for the label of the item. as a `Menu`.

`content`

    

A `View` to display when the user selects the item.

## Discussion

When this item is removed from the system menu bar by the user, the
application will be automatically quit. As such, it should not be used in
conjunction with other scene types in your `App`.

## See Also

### Creating a menu bar extra

`init(LocalizedStringKey, content: () -> Content)`

Creates a menu bar extra with a key for a localized string to use as the
label. The extra defines the primary scene of an `App`.

Available when `Label` is `Text` and `Content` conforms to `View`.

`init(content: () -> Content, label: () -> Label)`

Creates a menu bar extra that will be displayed in the system menu bar, and
defines the primary scene of an `App`.

`init(LocalizedStringKey, isInserted: Binding<Bool>, content: () -> Content)`

Creates a menu bar extra with a key for a localized string to use as the
label. The item will be displayed in the system menu bar when the specified
binding is set to `true`. If the user removes the item from the menu bar, the
binding will be set to `false`.

Available when `Label` is `Text` and `Content` conforms to `View`.

`init<S>(S, isInserted: Binding<Bool>, content: () -> Content)`

Creates a menu bar extra with a string to use as the label. The item will be
displayed in the system menu bar when the specified binding is set to `true`.
If the user removes the item from the menu bar, the binding will be set to
`false`.

Available when `Label` is `Text` and `Content` conforms to `View`.

`init(isInserted: Binding<Bool>, content: () -> Content, label: () -> Label)`

Creates a menu bar extra. The item will be displayed in the system menu bar
when the specified binding is set to `true`. If the user removes the item from
the menu bar, the binding will be set to `false`.

Initializer

# init(content:label:)

Creates a menu bar extra that will be displayed in the system menu bar, and
defines the primary scene of an `App`.

macOS 13.0+

    
    
    init(
        @ViewBuilder content: () -> Content,
        @ViewBuilder label: () -> Label
    )

##  Parameters

`content`

    

A `View` to display when the user selects the item.

`label`

    

A `View` to use as the label in the system menu bar.

## Discussion

When this item is removed from the system menu bar by the user, the
application will be automatically quit. As such, it should not be used in
conjunction with other scene types in your `App`.

## See Also

### Creating a menu bar extra

`init(LocalizedStringKey, content: () -> Content)`

Creates a menu bar extra with a key for a localized string to use as the
label. The extra defines the primary scene of an `App`.

Available when `Label` is `Text` and `Content` conforms to `View`.

`init<S>(S, content: () -> Content)`

Creates a menu bar extra with a string to use as the label. The item defines
the primary scene of an `App`.

Available when `Label` is `Text` and `Content` conforms to `View`.

`init(LocalizedStringKey, isInserted: Binding<Bool>, content: () -> Content)`

Creates a menu bar extra with a key for a localized string to use as the
label. The item will be displayed in the system menu bar when the specified
binding is set to `true`. If the user removes the item from the menu bar, the
binding will be set to `false`.

Available when `Label` is `Text` and `Content` conforms to `View`.

`init<S>(S, isInserted: Binding<Bool>, content: () -> Content)`

Creates a menu bar extra with a string to use as the label. The item will be
displayed in the system menu bar when the specified binding is set to `true`.
If the user removes the item from the menu bar, the binding will be set to
`false`.

Available when `Label` is `Text` and `Content` conforms to `View`.

`init(isInserted: Binding<Bool>, content: () -> Content, label: () -> Label)`

Creates a menu bar extra. The item will be displayed in the system menu bar
when the specified binding is set to `true`. If the user removes the item from
the menu bar, the binding will be set to `false`.

Initializer

# init(_:isInserted:content:)

Creates a menu bar extra with a key for a localized string to use as the
label. The item will be displayed in the system menu bar when the specified
binding is set to `true`. If the user removes the item from the menu bar, the
binding will be set to `false`.

macOS 13.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        isInserted: Binding<Bool>,
        @ViewBuilder content: () -> Content
    )

Available when `Label` is `Text` and `Content` conforms to `View`.

##  Parameters

`titleKey`

    

The title key to use for the label of the item.

`isInserted`

    

Whether the item is inserted in the menu bar. The item may or may not be
visible, depending on the number of items present.

`content`

    

A `View` to display when the user selects the item.

## See Also

### Creating a menu bar extra

`init(LocalizedStringKey, content: () -> Content)`

Creates a menu bar extra with a key for a localized string to use as the
label. The extra defines the primary scene of an `App`.

Available when `Label` is `Text` and `Content` conforms to `View`.

`init<S>(S, content: () -> Content)`

Creates a menu bar extra with a string to use as the label. The item defines
the primary scene of an `App`.

Available when `Label` is `Text` and `Content` conforms to `View`.

`init(content: () -> Content, label: () -> Label)`

Creates a menu bar extra that will be displayed in the system menu bar, and
defines the primary scene of an `App`.

`init<S>(S, isInserted: Binding<Bool>, content: () -> Content)`

Creates a menu bar extra with a string to use as the label. The item will be
displayed in the system menu bar when the specified binding is set to `true`.
If the user removes the item from the menu bar, the binding will be set to
`false`.

Available when `Label` is `Text` and `Content` conforms to `View`.

`init(isInserted: Binding<Bool>, content: () -> Content, label: () -> Label)`

Creates a menu bar extra. The item will be displayed in the system menu bar
when the specified binding is set to `true`. If the user removes the item from
the menu bar, the binding will be set to `false`.

Initializer

# init(_:isInserted:content:)

Creates a menu bar extra with a string to use as the label. The item will be
displayed in the system menu bar when the specified binding is set to `true`.
If the user removes the item from the menu bar, the binding will be set to
`false`.

macOS 13.0+

    
    
    init<S>(
        _ title: S,
        isInserted: Binding<Bool>,
        @ViewBuilder content: () -> Content
    ) where S : StringProtocol

Available when `Label` is `Text` and `Content` conforms to `View`.

##  Parameters

`title`

    

The string to use for the label of the item.

`isInserted`

    

Whether the item is inserted in the menu bar. The item may or may not be
visible, depending on the number of items present.

`content`

    

A `View` to display when the user selects the item.

## See Also

### Creating a menu bar extra

`init(LocalizedStringKey, content: () -> Content)`

Creates a menu bar extra with a key for a localized string to use as the
label. The extra defines the primary scene of an `App`.

Available when `Label` is `Text` and `Content` conforms to `View`.

`init<S>(S, content: () -> Content)`

Creates a menu bar extra with a string to use as the label. The item defines
the primary scene of an `App`.

Available when `Label` is `Text` and `Content` conforms to `View`.

`init(content: () -> Content, label: () -> Label)`

Creates a menu bar extra that will be displayed in the system menu bar, and
defines the primary scene of an `App`.

`init(LocalizedStringKey, isInserted: Binding<Bool>, content: () -> Content)`

Creates a menu bar extra with a key for a localized string to use as the
label. The item will be displayed in the system menu bar when the specified
binding is set to `true`. If the user removes the item from the menu bar, the
binding will be set to `false`.

Available when `Label` is `Text` and `Content` conforms to `View`.

`init(isInserted: Binding<Bool>, content: () -> Content, label: () -> Label)`

Creates a menu bar extra. The item will be displayed in the system menu bar
when the specified binding is set to `true`. If the user removes the item from
the menu bar, the binding will be set to `false`.

Initializer

# init(isInserted:content:label:)

Creates a menu bar extra. The item will be displayed in the system menu bar
when the specified binding is set to `true`. If the user removes the item from
the menu bar, the binding will be set to `false`.

macOS 13.0+

    
    
    init(
        isInserted: Binding<Bool>,
        @ViewBuilder content: () -> Content,
        @ViewBuilder label: () -> Label
    )

##  Parameters

`isInserted`

    

Whether the item is inserted in the menu bar. The item may or may not be
visible, depending on the number of items present.

`content`

    

A `View` to display when the user selects the item.

`label`

    

A `View` to use as the label in the system menu bar.

## See Also

### Creating a menu bar extra

`init(LocalizedStringKey, content: () -> Content)`

Creates a menu bar extra with a key for a localized string to use as the
label. The extra defines the primary scene of an `App`.

Available when `Label` is `Text` and `Content` conforms to `View`.

`init<S>(S, content: () -> Content)`

Creates a menu bar extra with a string to use as the label. The item defines
the primary scene of an `App`.

Available when `Label` is `Text` and `Content` conforms to `View`.

`init(content: () -> Content, label: () -> Label)`

Creates a menu bar extra that will be displayed in the system menu bar, and
defines the primary scene of an `App`.

`init(LocalizedStringKey, isInserted: Binding<Bool>, content: () -> Content)`

Creates a menu bar extra with a key for a localized string to use as the
label. The item will be displayed in the system menu bar when the specified
binding is set to `true`. If the user removes the item from the menu bar, the
binding will be set to `false`.

Available when `Label` is `Text` and `Content` conforms to `View`.

`init<S>(S, isInserted: Binding<Bool>, content: () -> Content)`

Creates a menu bar extra with a string to use as the label. The item will be
displayed in the system menu bar when the specified binding is set to `true`.
If the user removes the item from the menu bar, the binding will be set to
`false`.

Available when `Label` is `Text` and `Content` conforms to `View`.

Initializer

# init(_:image:content:)

Creates a menu bar extra with a named image to use as the items label. The
provided title will be used by the accessibility system.

macOS 13.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        image: String,
        @ViewBuilder content: () -> Content
    )

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

##  Parameters

`titleKey`

    

The localized string key to use for the accessibility label of the item.

`image`

    

The name of an image in the app’s bundle to use as the label.

`content`

    

A `View` to display when the user selects the item.

## Discussion

The item defines the primary scene of an `App`.

When this item is removed from the system menu bar by the user, the
application will be automatically quit. As such, it should not be used in
conjunction with other scene types in your `App`.

## See Also

### Creating a menu bar extra with a named image

`init(LocalizedStringKey, image: String, isInserted: Binding<Bool>, content:
() -> Content)`

Creates a menu bar extra with a named image to use as the items label. The
provided title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init<S>(S, image: String, content: () -> Content)`

Creates a menu bar extra with a named image to use as the items label. The
provided title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init<S>(S, image: String, isInserted: Binding<Bool>, content: () -> Content)`

Creates a menu bar extra with a named image to use as the items label. The
provided title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

Initializer

# init(_:image:isInserted:content:)

Creates a menu bar extra with a named image to use as the items label. The
provided title will be used by the accessibility system.

macOS 13.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        image: String,
        isInserted: Binding<Bool>,
        @ViewBuilder content: () -> Content
    )

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

##  Parameters

`titleKey`

    

The localized string key to use for the accessibility label of the item.

`image`

    

The name of an image in the app’s bundle to use as the label.

`isInserted`

    

Whether the item is inserted in the menu bar. The item may or may not be
visible, depending on the number of items present.

`content`

    

A `View` to display when the user selects the item.

## Discussion

The item will be displayed in the system menu bar when the specified binding
is set to `true`. If the user removes the item from the menu bar, the binding
will be set to `false`.

## See Also

### Creating a menu bar extra with a named image

`init(LocalizedStringKey, image: String, content: () -> Content)`

Creates a menu bar extra with a named image to use as the items label. The
provided title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init<S>(S, image: String, content: () -> Content)`

Creates a menu bar extra with a named image to use as the items label. The
provided title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init<S>(S, image: String, isInserted: Binding<Bool>, content: () -> Content)`

Creates a menu bar extra with a named image to use as the items label. The
provided title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

Initializer

# init(_:image:content:)

Creates a menu bar extra with a named image to use as the items label. The
provided title will be used by the accessibility system.

macOS 13.0+

    
    
    init<S>(
        _ title: S,
        image: String,
        @ViewBuilder content: () -> Content
    ) where S : StringProtocol

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

##  Parameters

`title`

    

The string to use for the accessibility label of the item.

`image`

    

The name of an image in the app’s bundle to use as the label.

`content`

    

A `View` to display when the user selects the item.

## Discussion

The item defines the primary scene of an `App`.

When this item is removed from the system menu bar by the user, the
application will be automatically quit. As such, it should not be used in
conjunction with other scene types in your `App`.

## See Also

### Creating a menu bar extra with a named image

`init(LocalizedStringKey, image: String, content: () -> Content)`

Creates a menu bar extra with a named image to use as the items label. The
provided title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init(LocalizedStringKey, image: String, isInserted: Binding<Bool>, content:
() -> Content)`

Creates a menu bar extra with a named image to use as the items label. The
provided title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init<S>(S, image: String, isInserted: Binding<Bool>, content: () -> Content)`

Creates a menu bar extra with a named image to use as the items label. The
provided title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

Initializer

# init(_:image:isInserted:content:)

Creates a menu bar extra with a named image to use as the items label. The
provided title will be used by the accessibility system.

macOS 13.0+

    
    
    init<S>(
        _ title: S,
        image: String,
        isInserted: Binding<Bool>,
        @ViewBuilder content: () -> Content
    ) where S : StringProtocol

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

##  Parameters

`title`

    

The string to use for the accessibility label of the item.

`image`

    

The name of an image in the app’s bundle to use as the label.

`isInserted`

    

Whether the item is inserted in the menu bar. The item may or may not be
visible, depending on the number of items present.

`content`

    

A `View` to display when the user selects the item.

## Discussion

The item will be displayed in the system menu bar when the specified binding
is set to `true`. If the user removes the item from the menu bar, the binding
will be set to `false`.

## See Also

### Creating a menu bar extra with a named image

`init(LocalizedStringKey, image: String, content: () -> Content)`

Creates a menu bar extra with a named image to use as the items label. The
provided title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init(LocalizedStringKey, image: String, isInserted: Binding<Bool>, content:
() -> Content)`

Creates a menu bar extra with a named image to use as the items label. The
provided title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init<S>(S, image: String, content: () -> Content)`

Creates a menu bar extra with a named image to use as the items label. The
provided title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

Initializer

# init(_:systemImage:content:)

Creates a menu bar extra with a system image to use as the items label. The
provided title will be used by the accessibility system.

macOS 13.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        systemImage: String,
        @ViewBuilder content: () -> Content
    )

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

##  Parameters

`titleKey`

    

The localized string key to use for the accessibility label of the item.

`systemImage`

    

The name of a system image to use as the label.

`content`

    

A `View` to display when the user selects the item.

## Discussion

The item defines the primary scene of an `App`.

When this item is removed from the system menu bar by the user, the
application will be automatically quit. As such, it should not be used in
conjunction with other scene types in your `App`.

## See Also

### Creating a menu bar extra with a system image

`init(LocalizedStringKey, systemImage: String, isInserted: Binding<Bool>,
content: () -> Content)`

Creates a menu bar extra with a system image to use as the items label. The
provided title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init<S>(S, systemImage: String, content: () -> Content)`

Creates a menu bar extra with a system image to use as the items label. The
provided title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init<S>(S, systemImage: String, isInserted: Binding<Bool>, content: () ->
Content)`

Creates a menu bar extra with a system image to use as the items label. The
provided title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

Initializer

# init(_:systemImage:isInserted:content:)

Creates a menu bar extra with a system image to use as the items label. The
provided title will be used by the accessibility system.

macOS 13.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        systemImage: String,
        isInserted: Binding<Bool>,
        @ViewBuilder content: () -> Content
    )

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

##  Parameters

`titleKey`

    

The localized string key to use for the accessibility label of the item.

`systemImage`

    

The name of a system image to use as the label.

`isInserted`

    

Whether the item is inserted in the menu bar. The item may or may not be
visible, depending on the number of items present.

`content`

    

A `View` to display when the user selects the item.

## Discussion

The item will be displayed in the system menu bar when the specified binding
is set to `true`. If the user removes the item from the menu bar, the binding
will be set to `false`.

## See Also

### Creating a menu bar extra with a system image

`init(LocalizedStringKey, systemImage: String, content: () -> Content)`

Creates a menu bar extra with a system image to use as the items label. The
provided title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init<S>(S, systemImage: String, content: () -> Content)`

Creates a menu bar extra with a system image to use as the items label. The
provided title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init<S>(S, systemImage: String, isInserted: Binding<Bool>, content: () ->
Content)`

Creates a menu bar extra with a system image to use as the items label. The
provided title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

Initializer

# init(_:systemImage:content:)

Creates a menu bar extra with a system image to use as the items label. The
provided title will be used by the accessibility system.

macOS 13.0+

    
    
    init<S>(
        _ title: S,
        systemImage: String,
        @ViewBuilder content: () -> Content
    ) where S : StringProtocol

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

##  Parameters

`title`

    

The string to use for the accessibility label of the item.

`systemImage`

    

The name of a system image to use as the label.

`content`

    

A `View` to display when the user selects the item.

## Discussion

The item defines the primary scene of an `App`.

When this item is removed from the system menu bar by the user, the
application will be automatically quit. As such, it should not be used in
conjunction with other scene types in your `App`.

## See Also

### Creating a menu bar extra with a system image

`init(LocalizedStringKey, systemImage: String, content: () -> Content)`

Creates a menu bar extra with a system image to use as the items label. The
provided title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init(LocalizedStringKey, systemImage: String, isInserted: Binding<Bool>,
content: () -> Content)`

Creates a menu bar extra with a system image to use as the items label. The
provided title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init<S>(S, systemImage: String, isInserted: Binding<Bool>, content: () ->
Content)`

Creates a menu bar extra with a system image to use as the items label. The
provided title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

Initializer

# init(_:systemImage:isInserted:content:)

Creates a menu bar extra with a system image to use as the items label. The
provided title will be used by the accessibility system.

macOS 13.0+

    
    
    init<S>(
        _ title: S,
        systemImage: String,
        isInserted: Binding<Bool>,
        @ViewBuilder content: () -> Content
    ) where S : StringProtocol

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

##  Parameters

`title`

    

The string to use for the accessibility label of the item.

`systemImage`

    

The name of a system image to use as the label.

`isInserted`

    

Whether the item is inserted in the menu bar. The item may or may not be
visible, depending on the number of items present.

`content`

    

A `View` to display when the user selects the item.

## Discussion

The item will be displayed in the system menu bar when the specified binding
is set to `true`. If the user removes the item from the menu bar, the binding
will be set to `false`.

## See Also

### Creating a menu bar extra with a system image

`init(LocalizedStringKey, systemImage: String, content: () -> Content)`

Creates a menu bar extra with a system image to use as the items label. The
provided title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init(LocalizedStringKey, systemImage: String, isInserted: Binding<Bool>,
content: () -> Content)`

Creates a menu bar extra with a system image to use as the items label. The
provided title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init<S>(S, systemImage: String, content: () -> Content)`

Creates a menu bar extra with a system image to use as the items label. The
provided title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

Initializer

# init(_:image:content:)

Creates a menu bar extra with an image to use as the items label. The provided
title will be used by the accessibility system.

macOS 14.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        image: ImageResource,
        @ViewBuilder content: () -> Content
    )

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

##  Parameters

`titleKey`

    

The localized string key to use for the accessibility label of the item.

`image`

    

The image resource to use as the label.

`content`

    

A `View` to display when the user selects the item.

## Discussion

The item defines the primary scene of an `App`.

When this item is removed from the system menu bar by the user, the
application will be automatically quit. As such, it should not be used in
conjunction with other scene types in your `App`.

## See Also

### Creating a menu bar extra with an image resource

`init(LocalizedStringKey, image: ImageResource, isInserted: Binding<Bool>,
content: () -> Content)`

Creates a menu bar extra with an image to use as the items label. The provided
title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init<S>(S, image: ImageResource, content: () -> Content)`

Creates a menu bar extra with an image to use as the items label. The provided
title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init<S>(S, image: ImageResource, isInserted: Binding<Bool>, content: () ->
Content)`

Creates a menu bar extra with an image to use as the items label. The provided
title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

Initializer

# init(_:image:isInserted:content:)

Creates a menu bar extra with an image to use as the items label. The provided
title will be used by the accessibility system.

macOS 14.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        image: ImageResource,
        isInserted: Binding<Bool>,
        @ViewBuilder content: () -> Content
    )

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

##  Parameters

`titleKey`

    

The localized string key to use for the accessibility label of the item.

`image`

    

The image resource to use as the label.

`isInserted`

    

Whether the item is inserted in the menu bar. The item may or may not be
visible, depending on the number of items present.

`content`

    

A `View` to display when the user selects the item.

## Discussion

The item will be displayed in the system menu bar when the specified binding
is set to `true`. If the user removes the item from the menu bar, the binding
will be set to `false`.

## See Also

### Creating a menu bar extra with an image resource

`init(LocalizedStringKey, image: ImageResource, content: () -> Content)`

Creates a menu bar extra with an image to use as the items label. The provided
title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init<S>(S, image: ImageResource, content: () -> Content)`

Creates a menu bar extra with an image to use as the items label. The provided
title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init<S>(S, image: ImageResource, isInserted: Binding<Bool>, content: () ->
Content)`

Creates a menu bar extra with an image to use as the items label. The provided
title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

Initializer

# init(_:image:content:)

Creates a menu bar extra with an image to use as the items label. The provided
title will be used by the accessibility system.

macOS 14.0+

    
    
    init<S>(
        _ title: S,
        image: ImageResource,
        @ViewBuilder content: () -> Content
    ) where S : StringProtocol

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

##  Parameters

`title`

    

The string to use for the accessibility label of the item.

`image`

    

The image resource to use as the label.

`content`

    

A `View` to display when the user selects the item.

## Discussion

The item defines the primary scene of an `App`.

When this item is removed from the system menu bar by the user, the
application will be automatically quit. As such, it should not be used in
conjunction with other scene types in your `App`.

## See Also

### Creating a menu bar extra with an image resource

`init(LocalizedStringKey, image: ImageResource, content: () -> Content)`

Creates a menu bar extra with an image to use as the items label. The provided
title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init(LocalizedStringKey, image: ImageResource, isInserted: Binding<Bool>,
content: () -> Content)`

Creates a menu bar extra with an image to use as the items label. The provided
title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init<S>(S, image: ImageResource, isInserted: Binding<Bool>, content: () ->
Content)`

Creates a menu bar extra with an image to use as the items label. The provided
title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

Initializer

# init(_:image:isInserted:content:)

Creates a menu bar extra with an image to use as the items label. The provided
title will be used by the accessibility system.

macOS 14.0+

    
    
    init<S>(
        _ title: S,
        image: ImageResource,
        isInserted: Binding<Bool>,
        @ViewBuilder content: () -> Content
    ) where S : StringProtocol

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

##  Parameters

`title`

    

The string to use for the accessibility label of the item.

`image`

    

The image resource to use as the label.

`isInserted`

    

Whether the item is inserted in the menu bar. The item may or may not be
visible, depending on the number of items present.

`content`

    

A `View` to display when the user selects the item.

## Discussion

The item will be displayed in the system menu bar when the specified binding
is set to `true`. If the user removes the item from the menu bar, the binding
will be set to `false`.

## See Also

### Creating a menu bar extra with an image resource

`init(LocalizedStringKey, image: ImageResource, content: () -> Content)`

Creates a menu bar extra with an image to use as the items label. The provided
title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init(LocalizedStringKey, image: ImageResource, isInserted: Binding<Bool>,
content: () -> Content)`

Creates a menu bar extra with an image to use as the items label. The provided
title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init<S>(S, image: ImageResource, content: () -> Content)`

Creates a menu bar extra with an image to use as the items label. The provided
title will be used by the accessibility system.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

