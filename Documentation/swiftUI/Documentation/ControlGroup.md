Initializer

# init(content:)

Creates a new ControlGroup with the specified children

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 17.0+  visionOS
1.0+

    
    
    init(@ViewBuilder content: () -> Content)

##  Parameters

`content`

    

the children to display

## See Also

### Creating a control group

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

Initializer

# init(content:label:)

Creates a new control group with the specified content and a label.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 17.0+  visionOS
1.0+

    
    
    init<C, L>(
        @ViewBuilder content: () -> C,
        @ViewBuilder label: () -> L
    ) where Content == LabeledControlGroupContent<C, L>, C : View, L : View

Available when `Content` conforms to `View`.

##  Parameters

`content`

    

The content to display.

`label`

    

A view that describes the purpose of the group.

## See Also

### Creating a control group

`init(content: () -> Content)`

Creates a new ControlGroup with the specified children

`init<C, S>(S, content: () -> C)`

Creates a new control group with the specified content that generates its
label from a string.

Available when `Content` conforms to `View`.

`init<C>(LocalizedStringKey, content: () -> C)`

Creates a new control group with the specified content that generates its
label from a localized string key.

Available when `Content` conforms to `View`.

Initializer

# init(_:content:)

Creates a new control group with the specified content that generates its
label from a string.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 17.0+  visionOS
1.0+

    
    
    init<C, S>(
        _ title: S,
        @ViewBuilder content: () -> C
    ) where Content == LabeledControlGroupContent<C, Text>, C : View, S : StringProtocol

Available when `Content` conforms to `View`.

##  Parameters

`title`

    

A string that describes the contents of the group.

`label`

    

A view that describes the purpose of the group.

## See Also

### Creating a control group

`init(content: () -> Content)`

Creates a new ControlGroup with the specified children

`init<C, L>(content: () -> C, label: () -> L)`

Creates a new control group with the specified content and a label.

Available when `Content` conforms to `View`.

`init<C>(LocalizedStringKey, content: () -> C)`

Creates a new control group with the specified content that generates its
label from a localized string key.

Available when `Content` conforms to `View`.

Initializer

# init(_:content:)

Creates a new control group with the specified content that generates its
label from a localized string key.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 17.0+  visionOS
1.0+

    
    
    init<C>(
        _ titleKey: LocalizedStringKey,
        @ViewBuilder content: () -> C
    ) where Content == LabeledControlGroupContent<C, Text>, C : View

Available when `Content` conforms to `View`.

##  Parameters

`titleKey`

    

The key for the group’s localized title, that describes the contents of the
group.

`label`

    

A view that describes the purpose of the group.

## See Also

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

Initializer

# init(_:image:content:)

Creates a new control group with the specified content that generates its
label from a localized string key and image resource.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    init<C>(
        _ titleKey: LocalizedStringKey,
        image: ImageResource,
        @ViewBuilder content: () -> C
    ) where Content == LabeledControlGroupContent<C, Label<Text, Image>>, C : View

Available when `Content` conforms to `View`.

##  Parameters

`titleKey`

    

The key for the group’s localized title, that describes the contents of the
group.

`systemImage`

    

The name of the image resource to lookup.

`label`

    

A view that describes the purpose of the group.

## See Also

### Creating a control group with an image

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

Initializer

# init(_:image:content:)

Creates a new control group with the specified content that generates its
label from a string and image name.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    init<C, S>(
        _ title: S,
        image: ImageResource,
        @ViewBuilder content: () -> C
    ) where Content == LabeledControlGroupContent<C, Label<Text, Image>>, C : View, S : StringProtocol

Available when `Content` conforms to `View`.

##  Parameters

`title`

    

A string that describes the contents of the group.

`systemImage`

    

The name of the image resource to lookup.

`label`

    

A view that describes the purpose of the group.

## See Also

### Creating a control group with an image

`init<C>(LocalizedStringKey, image: ImageResource, content: () -> C)`

Creates a new control group with the specified content that generates its
label from a localized string key and image resource.

Available when `Content` conforms to `View`.

`init<C>(LocalizedStringKey, systemImage: String, content: () -> C)`

Creates a new control group with the specified content that generates its
label from a localized string key and image name.

Available when `Content` conforms to `View`.

`init<C, S>(S, systemImage: String, content: () -> C)`

Creates a new control group with the specified content that generates its
label from a string and image name.

Available when `Content` conforms to `View`.

Initializer

# init(_:systemImage:content:)

Creates a new control group with the specified content that generates its
label from a localized string key and image name.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 17.0+  visionOS
1.0+

    
    
    init<C>(
        _ titleKey: LocalizedStringKey,
        systemImage: String,
        @ViewBuilder content: () -> C
    ) where Content == LabeledControlGroupContent<C, Label<Text, Image>>, C : View

Available when `Content` conforms to `View`.

##  Parameters

`titleKey`

    

The key for the group’s localized title, that describes the contents of the
group.

`systemImage`

    

The name of the image resource to lookup.

`label`

    

A view that describes the purpose of the group.

## See Also

### Creating a control group with an image

`init<C>(LocalizedStringKey, image: ImageResource, content: () -> C)`

Creates a new control group with the specified content that generates its
label from a localized string key and image resource.

Available when `Content` conforms to `View`.

`init<C, S>(S, image: ImageResource, content: () -> C)`

Creates a new control group with the specified content that generates its
label from a string and image name.

Available when `Content` conforms to `View`.

`init<C, S>(S, systemImage: String, content: () -> C)`

Creates a new control group with the specified content that generates its
label from a string and image name.

Available when `Content` conforms to `View`.

Initializer

# init(_:systemImage:content:)

Creates a new control group with the specified content that generates its
label from a string and image name.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 17.0+  visionOS
1.0+

    
    
    init<C, S>(
        _ title: S,
        systemImage: String,
        @ViewBuilder content: () -> C
    ) where Content == LabeledControlGroupContent<C, Label<Text, Image>>, C : View, S : StringProtocol

Available when `Content` conforms to `View`.

##  Parameters

`title`

    

A string that describes the contents of the group.

`systemImage`

    

The name of the image resource to lookup.

`label`

    

A view that describes the purpose of the group.

## See Also

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

Initializer

# init(_:)

Creates a control group based on a style configuration.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 17.0+  visionOS
1.0+

    
    
    init(_ configuration: ControlGroupStyleConfiguration)

Available when `Content` is `ControlGroupStyleConfiguration.Content`.

## Discussion

Use this initializer within the `makeBody(configuration:)` method of a
`ControlGroupStyle` instance to create an instance of the control group being
styled. This is useful for custom control group styles that modify the current
control group style.

For example, the following code creates a new, custom style that places a red
border around the current control group:

Structure

# LabeledControlGroupContent

A view that represents the body of a control group with a specified label.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 17.0+  visionOS
1.0+

    
    
    struct LabeledControlGroupContent<Content, Label> where Content : View, Label : View

## Overview

You don’t create this type directly. SwiftUI creates it when you build a
`ControlGroup`.

## Relationships

### Conforms To

  * `View`

