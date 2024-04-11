Type Property

# search

Creates a `ContentUnavailableView` instance that conveys a search state.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static var search: ContentUnavailableView<SearchUnavailableContent.Label, SearchUnavailableContent.Description, SearchUnavailableContent.Actions> { get }

Available when `Label` is `SearchUnavailableContent.Label`, `Description` is
`SearchUnavailableContent.Description`, and `Actions` is
`SearchUnavailableContent.Actions`.

## Discussion

A `ContentUnavailableView` initialized with this static member is expected to
be contained within a searchable view hierarchy. Such a configuration enables
the search query to be parsed into the view’s description.

For example, consider the usage of this static member in _ContactsListView_ :

## See Also

### Getting built-in unavailable views

`static func search(text: String) -> ContentUnavailableView<Label,
Description, Actions>`

Creates a `ContentUnavailableView` instance that conveys a search state.

Available when `Label` is `SearchUnavailableContent.Label`, `Description` is
`SearchUnavailableContent.Description`, and `Actions` is
`SearchUnavailableContent.Actions`.

Type Method

# search(text:)

Creates a `ContentUnavailableView` instance that conveys a search state.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static func search(text: String) -> ContentUnavailableView<Label, Description, Actions>

Available when `Label` is `SearchUnavailableContent.Label`, `Description` is
`SearchUnavailableContent.Description`, and `Actions` is
`SearchUnavailableContent.Actions`.

##  Parameters

`text`

    

The search text query.

## Discussion

For example, consider the usage of this static member in _ContactsListView_ :

## See Also

### Getting built-in unavailable views

`static var search: ContentUnavailableView<SearchUnavailableContent.Label,
SearchUnavailableContent.Description, SearchUnavailableContent.Actions>`

Creates a `ContentUnavailableView` instance that conveys a search state.

Available when `Label` is `SearchUnavailableContent.Label`, `Description` is
`SearchUnavailableContent.Description`, and `Actions` is
`SearchUnavailableContent.Actions`.

Initializer

# init(label:description:actions:)

Creates an interface, consisting of a label and additional content, that you
display when the content of your app is unavailable to users.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init(
        @ViewBuilder label: () -> Label,
        @ViewBuilder description: () -> Description = { EmptyView() },
        @ViewBuilder actions: () -> Actions = { EmptyView() }
    )

##  Parameters

`label`

    

The label that describes the view.

`description`

    

The view that describes the interface.

`actions`

    

The content of the interface actions.

Initializer

# init(_:image:description:)

Creates an interface, consisting of a title generated from a localized string,
an image and additional content, that you display when the content of your app
is unavailable to users.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init(
        _ title: LocalizedStringKey,
        image name: String,
        description: Text? = nil
    )

Available when `Label` is `Label<Text, Image>`, `Description` is `Text?`, and
`Actions` is `EmptyView`.

##  Parameters

`title`

    

A title generated from a localized string.

`image`

    

The name of the image resource to lookup.

`description`

    

The view that describes the interface.

## See Also

### Creating an unavailable view with an image

`init<S>(S, image: String, description: Text?)`

Creates an interface, consisting of a title generated from a string, an image
and additional content, that you display when the content of your app is
unavailable to users.

Available when `Label` is `Label<Text, Image>`, `Description` is `Text?`, and
`Actions` is `EmptyView`.

Initializer

# init(_:image:description:)

Creates an interface, consisting of a title generated from a string, an image
and additional content, that you display when the content of your app is
unavailable to users.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        image name: String,
        description: Text? = nil
    ) where S : StringProtocol

Available when `Label` is `Label<Text, Image>`, `Description` is `Text?`, and
`Actions` is `EmptyView`.

##  Parameters

`title`

    

A string used as the title.

`image`

    

The name of the image resource to lookup.

`description`

    

The view that describes the interface.

## See Also

### Creating an unavailable view with an image

`init(LocalizedStringKey, image: String, description: Text?)`

Creates an interface, consisting of a title generated from a localized string,
an image and additional content, that you display when the content of your app
is unavailable to users.

Available when `Label` is `Label<Text, Image>`, `Description` is `Text?`, and
`Actions` is `EmptyView`.

Initializer

# init(_:systemImage:description:)

Creates an interface, consisting of a title generated from a localized string,
a system icon image and additional content, that you display when the content
of your app is unavailable to users.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init(
        _ title: LocalizedStringKey,
        systemImage name: String,
        description: Text? = nil
    )

Available when `Label` is `Label<Text, Image>`, `Description` is `Text?`, and
`Actions` is `EmptyView`.

##  Parameters

`title`

    

A title generated from a localized string.

`systemImage`

    

The name of the system symbol image resource to lookup. Use the SF Symbols app
to look up the names of system symbol images.

`description`

    

The view that describes the interface.

## See Also

### Creating an unavailable view with a system image

`init<S>(S, systemImage: String, description: Text?)`

Creates an interface, consisting of a title generated from a string, a system
icon image and additional content, that you display when the content of your
app is unavailable to users.

Available when `Label` is `Label<Text, Image>`, `Description` is `Text?`, and
`Actions` is `EmptyView`.

Initializer

# init(_:systemImage:description:)

Creates an interface, consisting of a title generated from a string, a system
icon image and additional content, that you display when the content of your
app is unavailable to users.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        systemImage name: String,
        description: Text? = nil
    ) where S : StringProtocol

Available when `Label` is `Label<Text, Image>`, `Description` is `Text?`, and
`Actions` is `EmptyView`.

##  Parameters

`title`

    

A string used as the title.

`systemImage`

    

The name of the system symbol image resource to lookup. Use the SF Symbols app
to look up the names of system symbol images.

`description`

    

The view that describes the interface.

## See Also

### Creating an unavailable view with a system image

`init(LocalizedStringKey, systemImage: String, description: Text?)`

Creates an interface, consisting of a title generated from a localized string,
a system icon image and additional content, that you display when the content
of your app is unavailable to users.

Available when `Label` is `Label<Text, Image>`, `Description` is `Text?`, and
`Actions` is `EmptyView`.

Structure

# SearchUnavailableContent

A structure that represents the body of a static placeholder search view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct SearchUnavailableContent

## Overview

You don’t create this type directly. SwiftUI creates it when you build a
search`ContentUnavailableView`.

## Topics

### Getting content types

`struct Actions`

A view that represents the actions of a static `ContentUnavailableView.search`
view.

`struct Description`

A view that represents the description of a static
`ContentUnavailableView.search` view.

`struct Label`

A view that represents the label of a static placeholder search view.

