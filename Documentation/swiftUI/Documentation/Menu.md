Initializer

# init(content:label:)

Creates a menu with a custom label.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 17.0+  visionOS
1.0+

    
    
    init(
        @ViewBuilder content: () -> Content,
        @ViewBuilder label: () -> Label
    )

Available when `Label` conforms to `View` and `Content` conforms to `View`.

##  Parameters

`content`

    

A group of menu items.

`label`

    

A view describing the content of the menu.

## See Also

### Creating a menu from content

`init(LocalizedStringKey, content: () -> Content)`

Creates a menu that generates its label from a localized string key.

Available when `Label` conforms to `View` and `Content` conforms to `View`.

`init<S>(S, content: () -> Content)`

Creates a menu that generates its label from a string.

Available when `Label` conforms to `View` and `Content` conforms to `View`.

Initializer

# init(_:content:)

Creates a menu that generates its label from a localized string key.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 17.0+  visionOS
1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        @ViewBuilder content: () -> Content
    ) where Label == Text

Available when `Label` conforms to `View` and `Content` conforms to `View`.

##  Parameters

`titleKey`

    

The key for the link’s localized title, which describes the contents of the
menu.

`content`

    

A group of menu items.

## See Also

### Creating a menu from content

`init(content: () -> Content, label: () -> Label)`

Creates a menu with a custom label.

Available when `Label` conforms to `View` and `Content` conforms to `View`.

`init<S>(S, content: () -> Content)`

Creates a menu that generates its label from a string.

Available when `Label` conforms to `View` and `Content` conforms to `View`.

Initializer

# init(_:content:)

Creates a menu that generates its label from a string.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 17.0+  visionOS
1.0+

    
    
    init<S>(
        _ title: S,
        @ViewBuilder content: () -> Content
    ) where Label == Text, S : StringProtocol

Available when `Label` conforms to `View` and `Content` conforms to `View`.

##  Parameters

`title`

    

A string that describes the contents of the menu.

`content`

    

A group of menu items.

## Discussion

To create the label with a localized string key, use `init(_:content:)`
instead.

## See Also

### Creating a menu from content

`init(content: () -> Content, label: () -> Label)`

Creates a menu with a custom label.

Available when `Label` conforms to `View` and `Content` conforms to `View`.

`init(LocalizedStringKey, content: () -> Content)`

Creates a menu that generates its label from a localized string key.

Available when `Label` conforms to `View` and `Content` conforms to `View`.

Initializer

# init(content:label:primaryAction:)

Creates a menu with a custom primary action and custom label.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 17.0+  visionOS
1.0+

    
    
    init(
        @ViewBuilder content: () -> Content,
        @ViewBuilder label: () -> Label,
        primaryAction: @escaping () -> Void
    )

Available when `Label` conforms to `View` and `Content` conforms to `View`.

##  Parameters

`content`

    

A group of menu items.

`label`

    

A view describing the content of the menu.

`primaryAction`

    

The action to perform on primary interaction with the menu.

## See Also

### Creating a menu with a primary action

`init(LocalizedStringKey, content: () -> Content, primaryAction: () -> Void)`

Creates a menu with a custom primary action that generates its label from a
localized string key.

Available when `Label` conforms to `View` and `Content` conforms to `View`.

`init<S>(S, content: () -> Content, primaryAction: () -> Void)`

Creates a menu with a custom primary action that generates its label from a
string.

Available when `Label` conforms to `View` and `Content` conforms to `View`.

Initializer

# init(_:content:primaryAction:)

Creates a menu with a custom primary action that generates its label from a
localized string key.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 17.0+  visionOS
1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        @ViewBuilder content: () -> Content,
        primaryAction: @escaping () -> Void
    ) where Label == Text

Available when `Label` conforms to `View` and `Content` conforms to `View`.

##  Parameters

`titleKey`

    

The key for the link’s localized title, which describes the contents of the
menu.

`primaryAction`

    

The action to perform on primary interaction with the menu.

`content`

    

A group of menu items.

## See Also

### Creating a menu with a primary action

`init(content: () -> Content, label: () -> Label, primaryAction: () -> Void)`

Creates a menu with a custom primary action and custom label.

Available when `Label` conforms to `View` and `Content` conforms to `View`.

`init<S>(S, content: () -> Content, primaryAction: () -> Void)`

Creates a menu with a custom primary action that generates its label from a
string.

Available when `Label` conforms to `View` and `Content` conforms to `View`.

Initializer

# init(_:content:primaryAction:)

Creates a menu with a custom primary action that generates its label from a
string.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 17.0+  visionOS
1.0+

    
    
    init<S>(
        _ title: S,
        @ViewBuilder content: () -> Content,
        primaryAction: @escaping () -> Void
    ) where Label == Text, S : StringProtocol

Available when `Label` conforms to `View` and `Content` conforms to `View`.

##  Parameters

`title`

    

A string that describes the contents of the menu.

`primaryAction`

    

The action to perform on primary interaction with the menu.

`content`

    

A group of menu items.

## Discussion

To create the label with a localized string key, use
`Menu(_:primaryAction:content:)` instead.

## See Also

### Creating a menu with a primary action

`init(content: () -> Content, label: () -> Label, primaryAction: () -> Void)`

Creates a menu with a custom primary action and custom label.

Available when `Label` conforms to `View` and `Content` conforms to `View`.

`init(LocalizedStringKey, content: () -> Content, primaryAction: () -> Void)`

Creates a menu with a custom primary action that generates its label from a
localized string key.

Available when `Label` conforms to `View` and `Content` conforms to `View`.

Initializer

# init(_:image:content:)

Creates a menu that generates its label from a string and image resource.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    init<S>(
        _ title: S,
        image: ImageResource,
        @ViewBuilder content: () -> Content
    ) where S : StringProtocol

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

##  Parameters

`title`

    

A string that describes the contents of the menu.

`image`

    

The name of the image resource to lookup.

`content`

    

A group of menu items.

## Discussion

To create the label with a localized string key, use `init(_:content:)`
instead.

## See Also

### Creating a menu with an image label

`init(LocalizedStringKey, image: ImageResource, content: () -> Content)`

Creates a menu that generates its label from a localized string key and image
resource.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init(LocalizedStringKey, image: ImageResource, content: () -> Content,
primaryAction: () -> Void)`

Creates a menu with a custom primary action that generates its label from a
localized string key.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init<S>(S, systemImage: String, content: () -> Content)`

Creates a menu that generates its label from a string and system image.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init(LocalizedStringKey, systemImage: String, content: () -> Content)`

Creates a menu that generates its label from a localized string key and system
image.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init(LocalizedStringKey, systemImage: String, content: () -> Content,
primaryAction: () -> Void)`

Creates a menu with a custom primary action that generates its label from a
localized string key and system image.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

Initializer

# init(_:image:content:)

Creates a menu that generates its label from a localized string key and image
resource.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        image: ImageResource,
        @ViewBuilder content: () -> Content
    )

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

##  Parameters

`titleKey`

    

The key for the link’s localized title, which describes the contents of the
menu.

`image`

    

The name of the image resource to lookup.

`content`

    

A group of menu items.

## See Also

### Creating a menu with an image label

`init<S>(S, image: ImageResource, content: () -> Content)`

Creates a menu that generates its label from a string and image resource.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init(LocalizedStringKey, image: ImageResource, content: () -> Content,
primaryAction: () -> Void)`

Creates a menu with a custom primary action that generates its label from a
localized string key.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init<S>(S, systemImage: String, content: () -> Content)`

Creates a menu that generates its label from a string and system image.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init(LocalizedStringKey, systemImage: String, content: () -> Content)`

Creates a menu that generates its label from a localized string key and system
image.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init(LocalizedStringKey, systemImage: String, content: () -> Content,
primaryAction: () -> Void)`

Creates a menu with a custom primary action that generates its label from a
localized string key and system image.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

Initializer

# init(_:image:content:primaryAction:)

Creates a menu with a custom primary action that generates its label from a
localized string key.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        image: ImageResource,
        @ViewBuilder content: () -> Content,
        primaryAction: @escaping () -> Void
    )

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

##  Parameters

`titleKey`

    

The key for the link’s localized title, which describes the contents of the
menu.

`image`

    

The name of the image resource to lookup.

`primaryAction`

    

The action to perform on primary interaction with the menu.

`content`

    

A group of menu items.

## See Also

### Creating a menu with an image label

`init<S>(S, image: ImageResource, content: () -> Content)`

Creates a menu that generates its label from a string and image resource.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init(LocalizedStringKey, image: ImageResource, content: () -> Content)`

Creates a menu that generates its label from a localized string key and image
resource.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init<S>(S, systemImage: String, content: () -> Content)`

Creates a menu that generates its label from a string and system image.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init(LocalizedStringKey, systemImage: String, content: () -> Content)`

Creates a menu that generates its label from a localized string key and system
image.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init(LocalizedStringKey, systemImage: String, content: () -> Content,
primaryAction: () -> Void)`

Creates a menu with a custom primary action that generates its label from a
localized string key and system image.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

Initializer

# init(_:systemImage:content:)

Creates a menu that generates its label from a string and system image.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 17.0+  visionOS
1.0+

    
    
    init<S>(
        _ title: S,
        systemImage: String,
        @ViewBuilder content: () -> Content
    ) where S : StringProtocol

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

##  Parameters

`title`

    

A string that describes the contents of the menu.

`systemImage`

    

The name of the image resource to lookup.

`content`

    

A group of menu items.

## Discussion

To create the label with a localized string key, use `init(_:content:)`
instead.

## See Also

### Creating a menu with an image label

`init<S>(S, image: ImageResource, content: () -> Content)`

Creates a menu that generates its label from a string and image resource.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init(LocalizedStringKey, image: ImageResource, content: () -> Content)`

Creates a menu that generates its label from a localized string key and image
resource.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init(LocalizedStringKey, image: ImageResource, content: () -> Content,
primaryAction: () -> Void)`

Creates a menu with a custom primary action that generates its label from a
localized string key.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init(LocalizedStringKey, systemImage: String, content: () -> Content)`

Creates a menu that generates its label from a localized string key and system
image.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init(LocalizedStringKey, systemImage: String, content: () -> Content,
primaryAction: () -> Void)`

Creates a menu with a custom primary action that generates its label from a
localized string key and system image.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

Initializer

# init(_:systemImage:content:)

Creates a menu that generates its label from a localized string key and system
image.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 17.0+  visionOS
1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        systemImage: String,
        @ViewBuilder content: () -> Content
    )

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

##  Parameters

`titleKey`

    

The key for the link’s localized title, which describes the contents of the
menu.

`systemImage`

    

The name of the image resource to lookup.

`content`

    

A group of menu items.

## See Also

### Creating a menu with an image label

`init<S>(S, image: ImageResource, content: () -> Content)`

Creates a menu that generates its label from a string and image resource.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init(LocalizedStringKey, image: ImageResource, content: () -> Content)`

Creates a menu that generates its label from a localized string key and image
resource.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init(LocalizedStringKey, image: ImageResource, content: () -> Content,
primaryAction: () -> Void)`

Creates a menu with a custom primary action that generates its label from a
localized string key.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init<S>(S, systemImage: String, content: () -> Content)`

Creates a menu that generates its label from a string and system image.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init(LocalizedStringKey, systemImage: String, content: () -> Content,
primaryAction: () -> Void)`

Creates a menu with a custom primary action that generates its label from a
localized string key and system image.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

Initializer

# init(_:systemImage:content:primaryAction:)

Creates a menu with a custom primary action that generates its label from a
localized string key and system image.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 17.0+  visionOS
1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        systemImage: String,
        @ViewBuilder content: () -> Content,
        primaryAction: @escaping () -> Void
    )

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

##  Parameters

`titleKey`

    

The key for the link’s localized title, which describes the contents of the
menu.

`systemImage`

    

The name of the image resource to lookup.

`primaryAction`

    

The action to perform on primary interaction with the menu.

`content`

    

A group of menu items.

## See Also

### Creating a menu with an image label

`init<S>(S, image: ImageResource, content: () -> Content)`

Creates a menu that generates its label from a string and image resource.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init(LocalizedStringKey, image: ImageResource, content: () -> Content)`

Creates a menu that generates its label from a localized string key and image
resource.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init(LocalizedStringKey, image: ImageResource, content: () -> Content,
primaryAction: () -> Void)`

Creates a menu with a custom primary action that generates its label from a
localized string key.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init<S>(S, systemImage: String, content: () -> Content)`

Creates a menu that generates its label from a string and system image.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

`init(LocalizedStringKey, systemImage: String, content: () -> Content)`

Creates a menu that generates its label from a localized string key and system
image.

Available when `Label` is `Label<Text, Image>` and `Content` conforms to
`View`.

Initializer

# init(_:)

Creates a menu based on a style configuration.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 17.0+  visionOS
1.0+

    
    
    init(_ configuration: MenuStyleConfiguration)

Available when `Label` is `MenuStyleConfiguration.Label` and `Content` is
`MenuStyleConfiguration.Content`.

## Discussion

Use this initializer within the `makeBody(configuration:)` method of a
`MenuStyle` instance to create an instance of the menu being styled. This is
useful for custom menu styles that modify the current menu style.

For example, the following code creates a new, custom style that adds a red
border around the current menu style:

