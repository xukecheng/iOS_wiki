Initializer

# init(action:label:)

Creates a button that displays a custom label.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        action: @escaping () -> Void,
        @ViewBuilder label: () -> Label
    )

##  Parameters

`action`

    

The action to perform when the user triggers the button.

`label`

    

A view that describes the purpose of the button’s `action`.

## See Also

### Creating a button

`init(LocalizedStringKey, action: () -> Void)`

Creates a button that generates its label from a localized string key.

Available when `Label` is `Text`.

`init<S>(S, action: () -> Void)`

Creates a button that generates its label from a string.

Available when `Label` is `Text`.

Initializer

# init(_:action:)

Creates a button that generates its label from a localized string key.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        action: @escaping () -> Void
    )

Available when `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the button’s localized title, that describes the purpose of the
button’s `action`.

`action`

    

The action to perform when the user triggers the button.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

To initialize a button with a string variable, use `init(_:action:)` instead.

## See Also

### Creating a button

`init(action: () -> Void, label: () -> Label)`

Creates a button that displays a custom label.

`init<S>(S, action: () -> Void)`

Creates a button that generates its label from a string.

Available when `Label` is `Text`.

Initializer

# init(_:action:)

Creates a button that generates its label from a string.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        action: @escaping () -> Void
    ) where S : StringProtocol

Available when `Label` is `Text`.

##  Parameters

`title`

    

A string that describes the purpose of the button’s `action`.

`action`

    

The action to perform when the user triggers the button.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the title
similar to `init(_:)`. See `Text` for more information about localizing
strings.

To initialize a button with a localized string key, use `init(_:action:)`
instead.

## See Also

### Creating a button

`init(action: () -> Void, label: () -> Label)`

Creates a button that displays a custom label.

`init(LocalizedStringKey, action: () -> Void)`

Creates a button that generates its label from a localized string key.

Available when `Label` is `Text`.

Initializer

# init(role:action:label:)

Creates a button with a specified role that displays a custom label.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init(
        role: ButtonRole?,
        action: @escaping () -> Void,
        @ViewBuilder label: () -> Label
    )

Available when `Label` conforms to `View`.

##  Parameters

`role`

    

An optional semantic role that describes the button. A value of `nil` means
that the button doesn’t have an assigned role.

`action`

    

The action to perform when the user interacts with the button.

`label`

    

A view that describes the purpose of the button’s `action`.

## See Also

### Creating a button with a role

`init(LocalizedStringKey, role: ButtonRole?, action: () -> Void)`

Creates a button with a specified role that generates its label from a
localized string key.

Available when `Label` is `Text`.

`init<S>(S, role: ButtonRole?, action: () -> Void)`

Creates a button with a specified role that generates its label from a string.

Available when `Label` is `Text`.

Initializer

# init(_:role:action:)

Creates a button with a specified role that generates its label from a
localized string key.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        role: ButtonRole?,
        action: @escaping () -> Void
    )

Available when `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the button’s localized title, that describes the purpose of the
button’s `action`.

`role`

    

An optional semantic role describing the button. A value of `nil` means that
the button doesn’t have an assigned role.

`action`

    

The action to perform when the user triggers the button.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

To initialize a button with a string variable, use `init(_:role:action:)`
instead.

## See Also

### Creating a button with a role

`init(role: ButtonRole?, action: () -> Void, label: () -> Label)`

Creates a button with a specified role that displays a custom label.

Available when `Label` conforms to `View`.

`init<S>(S, role: ButtonRole?, action: () -> Void)`

Creates a button with a specified role that generates its label from a string.

Available when `Label` is `Text`.

Initializer

# init(_:role:action:)

Creates a button with a specified role that generates its label from a string.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        role: ButtonRole?,
        action: @escaping () -> Void
    ) where S : StringProtocol

Available when `Label` is `Text`.

##  Parameters

`title`

    

A string that describes the purpose of the button’s `action`.

`role`

    

An optional semantic role describing the button. A value of `nil` means that
the button doesn’t have an assigned role.

`action`

    

The action to perform when the user interacts with the button.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the title
similar to `init(_:)`. See `Text` for more information about localizing
strings.

To initialize a button with a localized string key, use `init(_:role:action:)`
instead.

## See Also

### Creating a button with a role

`init(role: ButtonRole?, action: () -> Void, label: () -> Label)`

Creates a button with a specified role that displays a custom label.

Available when `Label` conforms to `View`.

`init(LocalizedStringKey, role: ButtonRole?, action: () -> Void)`

Creates a button with a specified role that generates its label from a
localized string key.

Available when `Label` is `Text`.

Initializer

# init(_:image:action:)

Creates a button that generates its label from a localized string key and
image resource.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        image: ImageResource,
        action: @escaping () -> Void
    )

Available when `Label` is `Label<Text, Image>`.

##  Parameters

`titleKey`

    

The key for the button’s localized title, that describes the purpose of the
button’s `action`.

`image`

    

The image resource to lookup.

`action`

    

The action to perform when the user triggers the button.

## Discussion

This initializer creates a `Label` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

### Creating a button with an image resource

`init<S>(S, image: ImageResource, action: () -> Void)`

Creates a button that generates its label from a string and image resource.

Available when `Label` is `Label<Text, Image>`.

`init(LocalizedStringKey, image: ImageResource, role: ButtonRole?, action: ()
-> Void)`

Creates a button with a specified role that generates its label from a
localized string key and an image resource.

Available when `Label` is `Label<Text, Image>`.

`init<S>(S, image: ImageResource, role: ButtonRole?, action: () -> Void)`

Creates a button with a specified role that generates its label from a string
and an image resource.

Available when `Label` is `Label<Text, Image>`.

Initializer

# init(_:image:action:)

Creates a button that generates its label from a string and image resource.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        image: ImageResource,
        action: @escaping () -> Void
    ) where S : StringProtocol

Available when `Label` is `Label<Text, Image>`.

##  Parameters

`title`

    

A string that describes the purpose of the button’s `action`.

`image`

    

The image resource to lookup.

`action`

    

The action to perform when the user triggers the button.

## Discussion

This initializer creates a `Label` view on your behalf, and treats the title
similar to `init(_:)`. See `Text` for more information about localizing
strings.

## See Also

### Creating a button with an image resource

`init(LocalizedStringKey, image: ImageResource, action: () -> Void)`

Creates a button that generates its label from a localized string key and
image resource.

Available when `Label` is `Label<Text, Image>`.

`init(LocalizedStringKey, image: ImageResource, role: ButtonRole?, action: ()
-> Void)`

Creates a button with a specified role that generates its label from a
localized string key and an image resource.

Available when `Label` is `Label<Text, Image>`.

`init<S>(S, image: ImageResource, role: ButtonRole?, action: () -> Void)`

Creates a button with a specified role that generates its label from a string
and an image resource.

Available when `Label` is `Label<Text, Image>`.

Initializer

# init(_:image:role:action:)

Creates a button with a specified role that generates its label from a
localized string key and an image resource.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        image: ImageResource,
        role: ButtonRole?,
        action: @escaping () -> Void
    )

Available when `Label` is `Label<Text, Image>`.

##  Parameters

`titleKey`

    

The key for the button’s localized title, that describes the purpose of the
button’s `action`.

`image`

    

The image resource to lookup.

`role`

    

An optional semantic role describing the button. A value of `nil` means that
the button doesn’t have an assigned role.

`action`

    

The action to perform when the user triggers the button.

## Discussion

This initializer creates a `Label` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

### Creating a button with an image resource

`init(LocalizedStringKey, image: ImageResource, action: () -> Void)`

Creates a button that generates its label from a localized string key and
image resource.

Available when `Label` is `Label<Text, Image>`.

`init<S>(S, image: ImageResource, action: () -> Void)`

Creates a button that generates its label from a string and image resource.

Available when `Label` is `Label<Text, Image>`.

`init<S>(S, image: ImageResource, role: ButtonRole?, action: () -> Void)`

Creates a button with a specified role that generates its label from a string
and an image resource.

Available when `Label` is `Label<Text, Image>`.

Initializer

# init(_:image:role:action:)

Creates a button with a specified role that generates its label from a string
and an image resource.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        image: ImageResource,
        role: ButtonRole?,
        action: @escaping () -> Void
    ) where S : StringProtocol

Available when `Label` is `Label<Text, Image>`.

##  Parameters

`title`

    

A string that describes the purpose of the button’s `action`.

`image`

    

The image resource to lookup.

`role`

    

An optional semantic role describing the button. A value of `nil` means that
the button doesn’t have an assigned role.

`action`

    

The action to perform when the user interacts with the button.

## Discussion

This initializer creates a `Label` view on your behalf, and treats the title
similar to `init(_:)`. See `Text` for more information about localizing
strings.

## See Also

### Creating a button with an image resource

`init(LocalizedStringKey, image: ImageResource, action: () -> Void)`

Creates a button that generates its label from a localized string key and
image resource.

Available when `Label` is `Label<Text, Image>`.

`init<S>(S, image: ImageResource, action: () -> Void)`

Creates a button that generates its label from a string and image resource.

Available when `Label` is `Label<Text, Image>`.

`init(LocalizedStringKey, image: ImageResource, role: ButtonRole?, action: ()
-> Void)`

Creates a button with a specified role that generates its label from a
localized string key and an image resource.

Available when `Label` is `Label<Text, Image>`.

Initializer

# init(_:systemImage:action:)

Creates a button that generates its label from a string and system image name.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        systemImage: String,
        action: @escaping () -> Void
    ) where S : StringProtocol

Available when `Label` is `Label<Text, Image>`.

##  Parameters

`title`

    

A string that describes the purpose of the button’s `action`.

`systemImage`

    

The name of the image resource to lookup.

`action`

    

The action to perform when the user triggers the button.

## Discussion

This initializer creates a `Label` view on your behalf, and treats the title
similar to `init(_:)`. See `Text` for more information about localizing
strings.

## See Also

### Creating a button with a system image

`init(LocalizedStringKey, systemImage: String, action: () -> Void)`

Creates a button that generates its label from a localized string key and
system image name.

Available when `Label` is `Label<Text, Image>`.

`init<S>(S, systemImage: String, role: ButtonRole?, action: () -> Void)`

Creates a button with a specified role that generates its label from a string
and a system image and an image resource.

Available when `Label` is `Label<Text, Image>`.

`init(LocalizedStringKey, systemImage: String, role: ButtonRole?, action: ()
-> Void)`

Creates a button with a specified role that generates its label from a
localized string key and a system image.

Available when `Label` is `Label<Text, Image>`.

Initializer

# init(_:systemImage:action:)

Creates a button that generates its label from a localized string key and
system image name.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        systemImage: String,
        action: @escaping () -> Void
    )

Available when `Label` is `Label<Text, Image>`.

##  Parameters

`titleKey`

    

The key for the button’s localized title, that describes the purpose of the
button’s `action`.

`systemImage`

    

The name of the image resource to lookup.

`action`

    

The action to perform when the user triggers the button.

## Discussion

This initializer creates a `Label` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

### Creating a button with a system image

`init<S>(S, systemImage: String, action: () -> Void)`

Creates a button that generates its label from a string and system image name.

Available when `Label` is `Label<Text, Image>`.

`init<S>(S, systemImage: String, role: ButtonRole?, action: () -> Void)`

Creates a button with a specified role that generates its label from a string
and a system image and an image resource.

Available when `Label` is `Label<Text, Image>`.

`init(LocalizedStringKey, systemImage: String, role: ButtonRole?, action: ()
-> Void)`

Creates a button with a specified role that generates its label from a
localized string key and a system image.

Available when `Label` is `Label<Text, Image>`.

Initializer

# init(_:systemImage:role:action:)

Creates a button with a specified role that generates its label from a string
and a system image and an image resource.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        systemImage: String,
        role: ButtonRole?,
        action: @escaping () -> Void
    ) where S : StringProtocol

Available when `Label` is `Label<Text, Image>`.

##  Parameters

`title`

    

A string that describes the purpose of the button’s `action`.

`systemImage`

    

The name of the image resource to lookup.

`role`

    

An optional semantic role describing the button. A value of `nil` means that
the button doesn’t have an assigned role.

`action`

    

The action to perform when the user interacts with the button.

## Discussion

This initializer creates a `Label` view on your behalf, and treats the title
similar to `init(_:)`. See `Text` for more information about localizing
strings.

## See Also

### Creating a button with a system image

`init<S>(S, systemImage: String, action: () -> Void)`

Creates a button that generates its label from a string and system image name.

Available when `Label` is `Label<Text, Image>`.

`init(LocalizedStringKey, systemImage: String, action: () -> Void)`

Creates a button that generates its label from a localized string key and
system image name.

Available when `Label` is `Label<Text, Image>`.

`init(LocalizedStringKey, systemImage: String, role: ButtonRole?, action: ()
-> Void)`

Creates a button with a specified role that generates its label from a
localized string key and a system image.

Available when `Label` is `Label<Text, Image>`.

Initializer

# init(_:systemImage:role:action:)

Creates a button with a specified role that generates its label from a
localized string key and a system image.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        systemImage: String,
        role: ButtonRole?,
        action: @escaping () -> Void
    )

Available when `Label` is `Label<Text, Image>`.

##  Parameters

`titleKey`

    

The key for the button’s localized title, that describes the purpose of the
button’s `action`.

`systemImage`

    

The name of the image resource to lookup.

`role`

    

An optional semantic role describing the button. A value of `nil` means that
the button doesn’t have an assigned role.

`action`

    

The action to perform when the user triggers the button.

## Discussion

This initializer creates a `Label` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

### Creating a button with a system image

`init<S>(S, systemImage: String, action: () -> Void)`

Creates a button that generates its label from a string and system image name.

Available when `Label` is `Label<Text, Image>`.

`init(LocalizedStringKey, systemImage: String, action: () -> Void)`

Creates a button that generates its label from a localized string key and
system image name.

Available when `Label` is `Label<Text, Image>`.

`init<S>(S, systemImage: String, role: ButtonRole?, action: () -> Void)`

Creates a button with a specified role that generates its label from a string
and a system image and an image resource.

Available when `Label` is `Label<Text, Image>`.

Initializer

# init(_:)

Creates a button based on a configuration for a style with a custom appearance
and custom interaction behavior.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(_ configuration: PrimitiveButtonStyleConfiguration)

Available when `Label` is `PrimitiveButtonStyleConfiguration.Label`.

##  Parameters

`configuration`

    

A configuration for a style with a custom appearance and custom interaction
behavior.

## Discussion

Use this initializer within the `makeBody(configuration:)` method of a
`PrimitiveButtonStyle` to create an instance of the button that you want to
style. This is useful for custom button styles that modify the current button
style, rather than implementing a brand new style.

For example, the following style adds a red border around the button, but
otherwise preserves the button’s current style:

Initializer

# init(intent:label:)

Creates a button that performs an `AppIntent`.

AppIntents  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    init<I>(
        intent: I,
        @ViewBuilder label: () -> Label
    ) where I : AppIntent

Available when `Label` conforms to `View`.

##  Parameters

`intent`

    

The `AppIntent` to execute.

`label`

    

A view that describes the purpose of the button’s `action`.

## See Also

### Creating a button to perform an App Intent

`init(LocalizedStringKey, intent: some AppIntent)`

Creates a button that performs an `AppIntent` and generates its label from a
localized string key.

Available when `Label` is `Text`.

`init<S>(S, intent: some AppIntent)`

Creates a button that performs an `AppIntent` and generates its label from a
string.

Available when `Label` is `Text`.

`init(LocalizedStringKey, image: ImageResource, role: ButtonRole?, intent:
some AppIntent)`

Creates a button with a specified role that performs an `AppIntent` and
generates its label from a localized string key and an image resource.

Available when `Label` is `Label<Text, Image>`.

`init(some StringProtocol, image: ImageResource, role: ButtonRole?, intent:
some AppIntent)`

Creates a button with a specified role that generates its label from a string
and an image resource.

Available when `Label` is `Label<Text, Image>`.

`init(LocalizedStringKey, role: ButtonRole?, intent: some AppIntent)`

Creates a button with a specified role that performs an `AppIntent` and
generates its label from a localized string key.

Available when `Label` is `Text`.

`init(some StringProtocol, role: ButtonRole?, intent: some AppIntent)`

Creates a button with a specified role that performs an `AppIntent` and
generates its label from a string.

Available when `Label` is `Text`.

`init(LocalizedStringKey, systemImage: String, role: ButtonRole?, intent: some
AppIntent)`

Creates a button with a specified role that performs an `AppIntent` and
generates its label from a localized string key and a system image.

Available when `Label` is `Label<Text, Image>`.

`init(some StringProtocol, systemImage: String, role: ButtonRole?, intent:
some AppIntent)`

Creates a button with a specified role that generates its label from a string
and a system image.

Available when `Label` is `Label<Text, Image>`.

`init(role: ButtonRole?, intent: some AppIntent, label: () -> Label)`

Creates a button with a specified role that performs an `AppIntent`.

Available when `Label` conforms to `View`.

Initializer

# init(_:intent:)

Creates a button that performs an `AppIntent` and generates its label from a
localized string key.

AppIntents  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        intent: some AppIntent
    )

Available when `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the button’s localized title, that describes the purpose of the
button’s `intent`.

`intent`

    

The `AppIntent` to execute.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

To initialize a button with a string variable, use `Button/init(_:intent:)`
instead.

## See Also

### Creating a button to perform an App Intent

`init<I>(intent: I, label: () -> Label)`

Creates a button that performs an `AppIntent`.

Available when `Label` conforms to `View`.

`init<S>(S, intent: some AppIntent)`

Creates a button that performs an `AppIntent` and generates its label from a
string.

Available when `Label` is `Text`.

`init(LocalizedStringKey, image: ImageResource, role: ButtonRole?, intent:
some AppIntent)`

Creates a button with a specified role that performs an `AppIntent` and
generates its label from a localized string key and an image resource.

Available when `Label` is `Label<Text, Image>`.

`init(some StringProtocol, image: ImageResource, role: ButtonRole?, intent:
some AppIntent)`

Creates a button with a specified role that generates its label from a string
and an image resource.

Available when `Label` is `Label<Text, Image>`.

`init(LocalizedStringKey, role: ButtonRole?, intent: some AppIntent)`

Creates a button with a specified role that performs an `AppIntent` and
generates its label from a localized string key.

Available when `Label` is `Text`.

`init(some StringProtocol, role: ButtonRole?, intent: some AppIntent)`

Creates a button with a specified role that performs an `AppIntent` and
generates its label from a string.

Available when `Label` is `Text`.

`init(LocalizedStringKey, systemImage: String, role: ButtonRole?, intent: some
AppIntent)`

Creates a button with a specified role that performs an `AppIntent` and
generates its label from a localized string key and a system image.

Available when `Label` is `Label<Text, Image>`.

`init(some StringProtocol, systemImage: String, role: ButtonRole?, intent:
some AppIntent)`

Creates a button with a specified role that generates its label from a string
and a system image.

Available when `Label` is `Label<Text, Image>`.

`init(role: ButtonRole?, intent: some AppIntent, label: () -> Label)`

Creates a button with a specified role that performs an `AppIntent`.

Available when `Label` conforms to `View`.

Initializer

# init(_:intent:)

Creates a button that performs an `AppIntent` and generates its label from a
string.

AppIntents  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    init<S>(
        _ title: S,
        intent: some AppIntent
    ) where S : StringProtocol

Available when `Label` is `Text`.

##  Parameters

`title`

    

A string that describes the purpose of the button’s `intent`.

`intent`

    

The `AppIntent` to execute.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the title
similar to `init(_:)`. See `Text` for more information about localizing
strings.

To initialize a button with a localized string key, use
`Button/init(_:intent:)` instead.

## See Also

### Creating a button to perform an App Intent

`init<I>(intent: I, label: () -> Label)`

Creates a button that performs an `AppIntent`.

Available when `Label` conforms to `View`.

`init(LocalizedStringKey, intent: some AppIntent)`

Creates a button that performs an `AppIntent` and generates its label from a
localized string key.

Available when `Label` is `Text`.

`init(LocalizedStringKey, image: ImageResource, role: ButtonRole?, intent:
some AppIntent)`

Creates a button with a specified role that performs an `AppIntent` and
generates its label from a localized string key and an image resource.

Available when `Label` is `Label<Text, Image>`.

`init(some StringProtocol, image: ImageResource, role: ButtonRole?, intent:
some AppIntent)`

Creates a button with a specified role that generates its label from a string
and an image resource.

Available when `Label` is `Label<Text, Image>`.

`init(LocalizedStringKey, role: ButtonRole?, intent: some AppIntent)`

Creates a button with a specified role that performs an `AppIntent` and
generates its label from a localized string key.

Available when `Label` is `Text`.

`init(some StringProtocol, role: ButtonRole?, intent: some AppIntent)`

Creates a button with a specified role that performs an `AppIntent` and
generates its label from a string.

Available when `Label` is `Text`.

`init(LocalizedStringKey, systemImage: String, role: ButtonRole?, intent: some
AppIntent)`

Creates a button with a specified role that performs an `AppIntent` and
generates its label from a localized string key and a system image.

Available when `Label` is `Label<Text, Image>`.

`init(some StringProtocol, systemImage: String, role: ButtonRole?, intent:
some AppIntent)`

Creates a button with a specified role that generates its label from a string
and a system image.

Available when `Label` is `Label<Text, Image>`.

`init(role: ButtonRole?, intent: some AppIntent, label: () -> Label)`

Creates a button with a specified role that performs an `AppIntent`.

Available when `Label` conforms to `View`.

Initializer

# init(_:image:role:intent:)

Creates a button with a specified role that performs an `AppIntent` and
generates its label from a localized string key and an image resource.

AppIntents  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        image: ImageResource,
        role: ButtonRole? = nil,
        intent: some AppIntent
    )

Available when `Label` is `Label<Text, Image>`.

##  Parameters

`titleKey`

    

The key for the button’s localized title, that describes the purpose of the
button’s `intent`.

`image`

    

The image resource to lookup.

`role`

    

An optional semantic role describing the button. A value of `nil` means that
the button doesn’t have an assigned role.

`intent`

    

The `AppIntent` to execute.

## Discussion

This initializer creates a `Label` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

### Creating a button to perform an App Intent

`init<I>(intent: I, label: () -> Label)`

Creates a button that performs an `AppIntent`.

Available when `Label` conforms to `View`.

`init(LocalizedStringKey, intent: some AppIntent)`

Creates a button that performs an `AppIntent` and generates its label from a
localized string key.

Available when `Label` is `Text`.

`init<S>(S, intent: some AppIntent)`

Creates a button that performs an `AppIntent` and generates its label from a
string.

Available when `Label` is `Text`.

`init(some StringProtocol, image: ImageResource, role: ButtonRole?, intent:
some AppIntent)`

Creates a button with a specified role that generates its label from a string
and an image resource.

Available when `Label` is `Label<Text, Image>`.

`init(LocalizedStringKey, role: ButtonRole?, intent: some AppIntent)`

Creates a button with a specified role that performs an `AppIntent` and
generates its label from a localized string key.

Available when `Label` is `Text`.

`init(some StringProtocol, role: ButtonRole?, intent: some AppIntent)`

Creates a button with a specified role that performs an `AppIntent` and
generates its label from a string.

Available when `Label` is `Text`.

`init(LocalizedStringKey, systemImage: String, role: ButtonRole?, intent: some
AppIntent)`

Creates a button with a specified role that performs an `AppIntent` and
generates its label from a localized string key and a system image.

Available when `Label` is `Label<Text, Image>`.

`init(some StringProtocol, systemImage: String, role: ButtonRole?, intent:
some AppIntent)`

Creates a button with a specified role that generates its label from a string
and a system image.

Available when `Label` is `Label<Text, Image>`.

`init(role: ButtonRole?, intent: some AppIntent, label: () -> Label)`

Creates a button with a specified role that performs an `AppIntent`.

Available when `Label` conforms to `View`.

Initializer

# init(_:image:role:intent:)

Creates a button with a specified role that generates its label from a string
and an image resource.

AppIntents  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    init(
        _ title: some StringProtocol,
        image: ImageResource,
        role: ButtonRole? = nil,
        intent: some AppIntent
    )

Available when `Label` is `Label<Text, Image>`.

##  Parameters

`title`

    

A string that describes the purpose of the button’s `intent`.

`image`

    

The image resource to lookup.

`role`

    

An optional semantic role describing the button. A value of `nil` means that
the button doesn’t have an assigned role.

`intent`

    

The `AppIntent` to execute.

## Discussion

This initializer creates a `Label` view on your behalf, and treats the title
similar to `init(_:)`. See `Text` for more information about localizing
strings.

## See Also

### Creating a button to perform an App Intent

`init<I>(intent: I, label: () -> Label)`

Creates a button that performs an `AppIntent`.

Available when `Label` conforms to `View`.

`init(LocalizedStringKey, intent: some AppIntent)`

Creates a button that performs an `AppIntent` and generates its label from a
localized string key.

Available when `Label` is `Text`.

`init<S>(S, intent: some AppIntent)`

Creates a button that performs an `AppIntent` and generates its label from a
string.

Available when `Label` is `Text`.

`init(LocalizedStringKey, image: ImageResource, role: ButtonRole?, intent:
some AppIntent)`

Creates a button with a specified role that performs an `AppIntent` and
generates its label from a localized string key and an image resource.

Available when `Label` is `Label<Text, Image>`.

`init(LocalizedStringKey, role: ButtonRole?, intent: some AppIntent)`

Creates a button with a specified role that performs an `AppIntent` and
generates its label from a localized string key.

Available when `Label` is `Text`.

`init(some StringProtocol, role: ButtonRole?, intent: some AppIntent)`

Creates a button with a specified role that performs an `AppIntent` and
generates its label from a string.

Available when `Label` is `Text`.

`init(LocalizedStringKey, systemImage: String, role: ButtonRole?, intent: some
AppIntent)`

Creates a button with a specified role that performs an `AppIntent` and
generates its label from a localized string key and a system image.

Available when `Label` is `Label<Text, Image>`.

`init(some StringProtocol, systemImage: String, role: ButtonRole?, intent:
some AppIntent)`

Creates a button with a specified role that generates its label from a string
and a system image.

Available when `Label` is `Label<Text, Image>`.

`init(role: ButtonRole?, intent: some AppIntent, label: () -> Label)`

Creates a button with a specified role that performs an `AppIntent`.

Available when `Label` conforms to `View`.

Initializer

# init(_:role:intent:)

Creates a button with a specified role that performs an `AppIntent` and
generates its label from a localized string key.

AppIntents  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        role: ButtonRole?,
        intent: some AppIntent
    )

Available when `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the button’s localized title, that describes the purpose of the
button’s `intent`.

`role`

    

An optional semantic role describing the button. A value of `nil` means that
the button doesn’t have an assigned role.

`intent`

    

The `AppIntent` to execute.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

### Creating a button to perform an App Intent

`init<I>(intent: I, label: () -> Label)`

Creates a button that performs an `AppIntent`.

Available when `Label` conforms to `View`.

`init(LocalizedStringKey, intent: some AppIntent)`

Creates a button that performs an `AppIntent` and generates its label from a
localized string key.

Available when `Label` is `Text`.

`init<S>(S, intent: some AppIntent)`

Creates a button that performs an `AppIntent` and generates its label from a
string.

Available when `Label` is `Text`.

`init(LocalizedStringKey, image: ImageResource, role: ButtonRole?, intent:
some AppIntent)`

Creates a button with a specified role that performs an `AppIntent` and
generates its label from a localized string key and an image resource.

Available when `Label` is `Label<Text, Image>`.

`init(some StringProtocol, image: ImageResource, role: ButtonRole?, intent:
some AppIntent)`

Creates a button with a specified role that generates its label from a string
and an image resource.

Available when `Label` is `Label<Text, Image>`.

`init(some StringProtocol, role: ButtonRole?, intent: some AppIntent)`

Creates a button with a specified role that performs an `AppIntent` and
generates its label from a string.

Available when `Label` is `Text`.

`init(LocalizedStringKey, systemImage: String, role: ButtonRole?, intent: some
AppIntent)`

Creates a button with a specified role that performs an `AppIntent` and
generates its label from a localized string key and a system image.

Available when `Label` is `Label<Text, Image>`.

`init(some StringProtocol, systemImage: String, role: ButtonRole?, intent:
some AppIntent)`

Creates a button with a specified role that generates its label from a string
and a system image.

Available when `Label` is `Label<Text, Image>`.

`init(role: ButtonRole?, intent: some AppIntent, label: () -> Label)`

Creates a button with a specified role that performs an `AppIntent`.

Available when `Label` conforms to `View`.

Initializer

# init(_:role:intent:)

Creates a button with a specified role that performs an `AppIntent` and
generates its label from a string.

AppIntents  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    init(
        _ title: some StringProtocol,
        role: ButtonRole?,
        intent: some AppIntent
    )

Available when `Label` is `Text`.

##  Parameters

`title`

    

A string that describes the purpose of the button’s `intent`.

`role`

    

An optional semantic role describing the button. A value of `nil` means that
the button doesn’t have an assigned role.

`intent`

    

The `AppIntent` to execute.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the title
similar to `init(_:)`. See `Text` for more information about localizing
strings.

## See Also

### Creating a button to perform an App Intent

`init<I>(intent: I, label: () -> Label)`

Creates a button that performs an `AppIntent`.

Available when `Label` conforms to `View`.

`init(LocalizedStringKey, intent: some AppIntent)`

Creates a button that performs an `AppIntent` and generates its label from a
localized string key.

Available when `Label` is `Text`.

`init<S>(S, intent: some AppIntent)`

Creates a button that performs an `AppIntent` and generates its label from a
string.

Available when `Label` is `Text`.

`init(LocalizedStringKey, image: ImageResource, role: ButtonRole?, intent:
some AppIntent)`

Creates a button with a specified role that performs an `AppIntent` and
generates its label from a localized string key and an image resource.

Available when `Label` is `Label<Text, Image>`.

`init(some StringProtocol, image: ImageResource, role: ButtonRole?, intent:
some AppIntent)`

Creates a button with a specified role that generates its label from a string
and an image resource.

Available when `Label` is `Label<Text, Image>`.

`init(LocalizedStringKey, role: ButtonRole?, intent: some AppIntent)`

Creates a button with a specified role that performs an `AppIntent` and
generates its label from a localized string key.

Available when `Label` is `Text`.

`init(LocalizedStringKey, systemImage: String, role: ButtonRole?, intent: some
AppIntent)`

Creates a button with a specified role that performs an `AppIntent` and
generates its label from a localized string key and a system image.

Available when `Label` is `Label<Text, Image>`.

`init(some StringProtocol, systemImage: String, role: ButtonRole?, intent:
some AppIntent)`

Creates a button with a specified role that generates its label from a string
and a system image.

Available when `Label` is `Label<Text, Image>`.

`init(role: ButtonRole?, intent: some AppIntent, label: () -> Label)`

Creates a button with a specified role that performs an `AppIntent`.

Available when `Label` conforms to `View`.

Initializer

# init(_:systemImage:role:intent:)

Creates a button with a specified role that performs an `AppIntent` and
generates its label from a localized string key and a system image.

AppIntents  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        systemImage: String,
        role: ButtonRole? = nil,
        intent: some AppIntent
    )

Available when `Label` is `Label<Text, Image>`.

##  Parameters

`titleKey`

    

The key for the button’s localized title, that describes the purpose of the
button’s `intent`.

`systemImage`

    

The name of the image resource to lookup.

`role`

    

An optional semantic role describing the button. A value of `nil` means that
the button doesn’t have an assigned role.

`intent`

    

The `AppIntent` to execute.

## Discussion

This initializer creates a `Label` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

### Creating a button to perform an App Intent

`init<I>(intent: I, label: () -> Label)`

Creates a button that performs an `AppIntent`.

Available when `Label` conforms to `View`.

`init(LocalizedStringKey, intent: some AppIntent)`

Creates a button that performs an `AppIntent` and generates its label from a
localized string key.

Available when `Label` is `Text`.

`init<S>(S, intent: some AppIntent)`

Creates a button that performs an `AppIntent` and generates its label from a
string.

Available when `Label` is `Text`.

`init(LocalizedStringKey, image: ImageResource, role: ButtonRole?, intent:
some AppIntent)`

Creates a button with a specified role that performs an `AppIntent` and
generates its label from a localized string key and an image resource.

Available when `Label` is `Label<Text, Image>`.

`init(some StringProtocol, image: ImageResource, role: ButtonRole?, intent:
some AppIntent)`

Creates a button with a specified role that generates its label from a string
and an image resource.

Available when `Label` is `Label<Text, Image>`.

`init(LocalizedStringKey, role: ButtonRole?, intent: some AppIntent)`

Creates a button with a specified role that performs an `AppIntent` and
generates its label from a localized string key.

Available when `Label` is `Text`.

`init(some StringProtocol, role: ButtonRole?, intent: some AppIntent)`

Creates a button with a specified role that performs an `AppIntent` and
generates its label from a string.

Available when `Label` is `Text`.

`init(some StringProtocol, systemImage: String, role: ButtonRole?, intent:
some AppIntent)`

Creates a button with a specified role that generates its label from a string
and a system image.

Available when `Label` is `Label<Text, Image>`.

`init(role: ButtonRole?, intent: some AppIntent, label: () -> Label)`

Creates a button with a specified role that performs an `AppIntent`.

Available when `Label` conforms to `View`.

Initializer

# init(_:systemImage:role:intent:)

Creates a button with a specified role that generates its label from a string
and a system image.

AppIntents  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    init(
        _ title: some StringProtocol,
        systemImage: String,
        role: ButtonRole? = nil,
        intent: some AppIntent
    )

Available when `Label` is `Label<Text, Image>`.

##  Parameters

`title`

    

A string that describes the purpose of the button’s `intent`.

`systemImage`

    

The name of the image resource to lookup.

`role`

    

An optional semantic role describing the button. A value of `nil` means that
the button doesn’t have an assigned role.

`intent`

    

The `AppIntent` to execute.

## Discussion

This initializer creates a `Label` view on your behalf, and treats the title
similar to `init(_:)`. See `Text` for more information about localizing
strings.

## See Also

### Creating a button to perform an App Intent

`init<I>(intent: I, label: () -> Label)`

Creates a button that performs an `AppIntent`.

Available when `Label` conforms to `View`.

`init(LocalizedStringKey, intent: some AppIntent)`

Creates a button that performs an `AppIntent` and generates its label from a
localized string key.

Available when `Label` is `Text`.

`init<S>(S, intent: some AppIntent)`

Creates a button that performs an `AppIntent` and generates its label from a
string.

Available when `Label` is `Text`.

`init(LocalizedStringKey, image: ImageResource, role: ButtonRole?, intent:
some AppIntent)`

Creates a button with a specified role that performs an `AppIntent` and
generates its label from a localized string key and an image resource.

Available when `Label` is `Label<Text, Image>`.

`init(some StringProtocol, image: ImageResource, role: ButtonRole?, intent:
some AppIntent)`

Creates a button with a specified role that generates its label from a string
and an image resource.

Available when `Label` is `Label<Text, Image>`.

`init(LocalizedStringKey, role: ButtonRole?, intent: some AppIntent)`

Creates a button with a specified role that performs an `AppIntent` and
generates its label from a localized string key.

Available when `Label` is `Text`.

`init(some StringProtocol, role: ButtonRole?, intent: some AppIntent)`

Creates a button with a specified role that performs an `AppIntent` and
generates its label from a string.

Available when `Label` is `Text`.

`init(LocalizedStringKey, systemImage: String, role: ButtonRole?, intent: some
AppIntent)`

Creates a button with a specified role that performs an `AppIntent` and
generates its label from a localized string key and a system image.

Available when `Label` is `Label<Text, Image>`.

`init(role: ButtonRole?, intent: some AppIntent, label: () -> Label)`

Creates a button with a specified role that performs an `AppIntent`.

Available when `Label` conforms to `View`.

Initializer

# init(role:intent:label:)

Creates a button with a specified role that performs an `AppIntent`.

AppIntents  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    init(
        role: ButtonRole?,
        intent: some AppIntent,
        @ViewBuilder label: () -> Label
    )

Available when `Label` conforms to `View`.

##  Parameters

`role`

    

An optional semantic role describing the button. A value of `nil` means that
the button doesn’t have an assigned role.

`intent`

    

The `AppIntent` to execute.

`label`

    

A view that describes the purpose of the button’s `action`.

## See Also

### Creating a button to perform an App Intent

`init<I>(intent: I, label: () -> Label)`

Creates a button that performs an `AppIntent`.

Available when `Label` conforms to `View`.

`init(LocalizedStringKey, intent: some AppIntent)`

Creates a button that performs an `AppIntent` and generates its label from a
localized string key.

Available when `Label` is `Text`.

`init<S>(S, intent: some AppIntent)`

Creates a button that performs an `AppIntent` and generates its label from a
string.

Available when `Label` is `Text`.

`init(LocalizedStringKey, image: ImageResource, role: ButtonRole?, intent:
some AppIntent)`

Creates a button with a specified role that performs an `AppIntent` and
generates its label from a localized string key and an image resource.

Available when `Label` is `Label<Text, Image>`.

`init(some StringProtocol, image: ImageResource, role: ButtonRole?, intent:
some AppIntent)`

Creates a button with a specified role that generates its label from a string
and an image resource.

Available when `Label` is `Label<Text, Image>`.

`init(LocalizedStringKey, role: ButtonRole?, intent: some AppIntent)`

Creates a button with a specified role that performs an `AppIntent` and
generates its label from a localized string key.

Available when `Label` is `Text`.

`init(some StringProtocol, role: ButtonRole?, intent: some AppIntent)`

Creates a button with a specified role that performs an `AppIntent` and
generates its label from a string.

Available when `Label` is `Text`.

`init(LocalizedStringKey, systemImage: String, role: ButtonRole?, intent: some
AppIntent)`

Creates a button with a specified role that performs an `AppIntent` and
generates its label from a localized string key and a system image.

Available when `Label` is `Label<Text, Image>`.

`init(some StringProtocol, systemImage: String, role: ButtonRole?, intent:
some AppIntent)`

Creates a button with a specified role that generates its label from a string
and a system image.

Available when `Label` is `Label<Text, Image>`.

