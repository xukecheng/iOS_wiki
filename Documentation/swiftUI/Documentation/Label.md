Initializer

# init(_:image:)

Creates a label with an icon image and a title generated from a localized
string.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        image name: String
    )

Available when `Title` is `Text` and `Icon` is `Image`.

##  Parameters

`titleKey`

    

A title generated from a localized string.

`image`

    

The name of the image resource to lookup.

## See Also

### Creating a label from text and an image

`init<S>(S, image: String)`

Creates a label with an icon image and a title generated from a string.

Available when `Title` is `Text` and `Icon` is `Image`.

Initializer

# init(_:image:)

Creates a label with an icon image and a title generated from a string.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        image name: String
    ) where S : StringProtocol

Available when `Title` is `Text` and `Icon` is `Image`.

##  Parameters

`title`

    

A string used as the label’s title.

`image`

    

The name of the image resource to lookup.

## See Also

### Creating a label from text and an image

`init(LocalizedStringKey, image: String)`

Creates a label with an icon image and a title generated from a localized
string.

Available when `Title` is `Text` and `Icon` is `Image`.

Initializer

# init(_:systemImage:)

Creates a label with a system icon image and a title generated from a
localized string.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        systemImage name: String
    )

Available when `Title` is `Text` and `Icon` is `Image`.

##  Parameters

`titleKey`

    

A title generated from a localized string.

`systemImage`

    

The name of the image resource to lookup.

## See Also

### Creating a label from text and an SF Symbol

`init<S>(S, systemImage: String)`

Creates a label with a system icon image and a title generated from a string.

Available when `Title` is `Text` and `Icon` is `Image`.

Initializer

# init(_:systemImage:)

Creates a label with a system icon image and a title generated from a string.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        systemImage name: String
    ) where S : StringProtocol

Available when `Title` is `Text` and `Icon` is `Image`.

##  Parameters

`title`

    

A string used as the label’s title.

`systemImage`

    

The name of the image resource to lookup.

## See Also

### Creating a label from text and an SF Symbol

`init(LocalizedStringKey, systemImage: String)`

Creates a label with a system icon image and a title generated from a
localized string.

Available when `Title` is `Text` and `Icon` is `Image`.

Initializer

# init(title:icon:)

Creates a label with a custom title and icon.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(
        @ViewBuilder title: () -> Title,
        @ViewBuilder icon: () -> Icon
    )

Initializer

# init(_:)

Creates a label representing the configuration of a style.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(_ configuration: LabelStyleConfiguration)

Available when `Title` is `LabelStyleConfiguration.Title` and `Icon` is
`LabelStyleConfiguration.Icon`.

##  Parameters

`configuration`

    

The label style to use.

## Discussion

You can use this initializer within the `makeBody(configuration:)` method of a
`LabelStyle` instance to create an instance of the label that’s being styled.
This is useful for custom label styles that only wish to modify the current
style, as opposed to implementing a brand new style.

For example, the following style adds a red border around the label, but
otherwise preserves the current style:

Initializer

# init(_:image:)

Creates a label with an icon image and a title generated from a localized
string.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        image resource: ImageResource
    )

Available when `Title` is `Text` and `Icon` is `Image`.

##  Parameters

`titleKey`

    

A title generated from a localized string.

`image`

    

The image resource to lookup.

## See Also

### Creating a label from an image resource

`init<S>(S, image: ImageResource)`

Creates a label with an icon image and a title generated from a string.

Available when `Title` is `Text` and `Icon` is `Image`.

Initializer

# init(_:image:)

Creates a label with an icon image and a title generated from a string.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        image resource: ImageResource
    ) where S : StringProtocol

Available when `Title` is `Text` and `Icon` is `Image`.

##  Parameters

`title`

    

A string used as the label’s title.

`image`

    

The image resource to lookup.

## See Also

### Creating a label from an image resource

`init(LocalizedStringKey, image: ImageResource)`

Creates a label with an icon image and a title generated from a localized
string.

Available when `Title` is `Text` and `Icon` is `Image`.

Initializer

# init(_:)

Creates a label representing a family activity application.

iOS 15.2+  iPadOS 15.2+  Mac Catalyst 15.2+  visionOS 1.0+

    
    
    init(_ applicationToken: ApplicationToken)

Available when `Title` is `FamilyActivityTitleView` and `Icon` is
`FamilyActivityIconView`.

## See Also

### Creating a family activity label

`init(WebDomainToken)`

Creates a label representing a family activity web domain.

Available when `Title` is `FamilyActivityTitleView` and `Icon` is
`FamilyActivityIconView`.

`init(ActivityCategoryToken)`

Creates a label representing a family activity category.

Available when `Title` is `FamilyActivityTitleView` and `Icon` is
`FamilyActivityIconView`.

Initializer

# init(_:)

Creates a label representing a family activity web domain.

iOS 15.2+  iPadOS 15.2+  Mac Catalyst 15.2+  visionOS 1.0+

    
    
    init(_ webDomainToken: WebDomainToken)

Available when `Title` is `FamilyActivityTitleView` and `Icon` is
`FamilyActivityIconView`.

## See Also

### Creating a family activity label

`init(ApplicationToken)`

Creates a label representing a family activity application.

Available when `Title` is `FamilyActivityTitleView` and `Icon` is
`FamilyActivityIconView`.

`init(ActivityCategoryToken)`

Creates a label representing a family activity category.

Available when `Title` is `FamilyActivityTitleView` and `Icon` is
`FamilyActivityIconView`.

Initializer

# init(_:)

Creates a label representing a family activity category.

iOS 15.2+  iPadOS 15.2+  Mac Catalyst 15.2+  visionOS 1.0+

    
    
    init(_ categoryToken: ActivityCategoryToken)

Available when `Title` is `FamilyActivityTitleView` and `Icon` is
`FamilyActivityIconView`.

## See Also

### Creating a family activity label

`init(ApplicationToken)`

Creates a label representing a family activity application.

Available when `Title` is `FamilyActivityTitleView` and `Icon` is
`FamilyActivityIconView`.

`init(WebDomainToken)`

Creates a label representing a family activity web domain.

Available when `Title` is `FamilyActivityTitleView` and `Icon` is
`FamilyActivityIconView`.

