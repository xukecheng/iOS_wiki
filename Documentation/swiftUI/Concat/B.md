# BorderedButtonMenuStyle

Initializer

# init()

Creates a bordered button menu style.

macOS 11.0–14.4  Deprecated

    
    
    init()

Deprecated

Use `menuStyle(_:)` with `button` and `buttonStyle(_:)` with `bordered`.



# ButtonMenuStyle

Initializer

# init()

Creates a button menu style.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 17.0+  visionOS
1.0+

    
    
    init()



# BorderedTableStyle

Initializer

# init()

Creates a default bordered table style, with alternating row backgrounds.

macOS 12.0+

    
    
    init()

## See Also

### Creating the table style

`init(alternatesRowBackgrounds: Bool)`

Creates an inset table style with optional alternating row backgrounds.

Deprecated

Initializer

# init(alternatesRowBackgrounds:)

Creates an inset table style with optional alternating row backgrounds.

macOS 12.0–14.4  Deprecated

    
    
    init(alternatesRowBackgrounds: Bool)

Deprecated

Use the `bordered` style and add the `alternatingRowBackgrounds(_:)` view
modifier instead.

## See Also

### Creating the table style

`init()`

Creates a default bordered table style, with alternating row backgrounds.



# ButtonStyleConfiguration

Instance Property

# label

A view that describes the effect of pressing the button.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    let label: ButtonStyleConfiguration.Label

## See Also

### Configuring a button’s label

`struct Label`

A type-erased label of a button.

Structure

# ButtonStyleConfiguration.Label

A type-erased label of a button.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    struct Label

## Relationships

### Conforms To

  * `View`

## See Also

### Configuring a button’s label

`let label: ButtonStyleConfiguration.Label`

A view that describes the effect of pressing the button.

Instance Property

# isPressed

A Boolean that indicates whether the user is currently pressing the button.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    let isPressed: Bool

Instance Property

# role

An optional semantic role that describes the button’s purpose.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    let role: ButtonRole?

## Discussion

A value of `nil` means that the Button doesn’t have an assigned role. If the
button does have a role, use it to make adjustments to the button’s
appearance. The following example shows a custom style that uses bold text
when the role is `cancel`, `red` text when the role is `destructive`, and adds
no special styling otherwise:

You can create one of each button using this style to see the effect:



# BackgroundStyle

Initializer

# init()

Creates a background style instance.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init()



# BlurReplaceTransition

Initializer

# init(configuration:)

Creates a new transition.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init(configuration: BlurReplaceTransition.Configuration)

##  Parameters

`configuration`

    

the transition configuration.

## See Also

### Creating the transition

`var configuration: BlurReplaceTransition.Configuration`

The transition configuration.

`struct Configuration`

Configuration properties for a transition.

Instance Property

# configuration

The transition configuration.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var configuration: BlurReplaceTransition.Configuration

## See Also

### Creating the transition

`init(configuration: BlurReplaceTransition.Configuration)`

Creates a new transition.

`struct Configuration`

Configuration properties for a transition.

Structure

# BlurReplaceTransition.Configuration

Configuration properties for a transition.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct Configuration

## Topics

### Getting the transition configuration

`static let downUp: BlurReplaceTransition.Configuration`

A configuration that requests a transition that scales the view down while
removing it and up while inserting it.

`static let upUp: BlurReplaceTransition.Configuration`

A configuration that requests a transition that scales the view up while both
removing and inserting it.

## Relationships

### Conforms To

  * `Equatable`

## See Also

### Creating the transition

`init(configuration: BlurReplaceTransition.Configuration)`

Creates a new transition.

`var configuration: BlurReplaceTransition.Configuration`

The transition configuration.



# Button

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



# Bindable

Initializer

# init(_:)

Creates a bindable object from an observable object.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init(_ wrappedValue: Value)

Available when `Value` conforms to `Observable`.

## Discussion

This initializer is equivalent to `init(wrappedValue:)`, but is more succinct
when when creating bindable objects nested within other expressions. For
example, you can use the initializer to create a bindable object inline with
code that declares a view that takes a binding as a parameter:

## See Also

### Creating a bindable value

`init(wrappedValue: Value)`

Creates a bindable object from an observable object.

Available when `Value` conforms to `Observable`.

`init(projectedValue: Bindable<Value>)`

Creates a bindable from the value of another bindable.

Available when `Value` conforms to `Observable`.

Initializer

# init(wrappedValue:)

Creates a bindable object from an observable object.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init(wrappedValue: Value)

Available when `Value` conforms to `Observable`.

## Discussion

You should not call this initializer directly. Instead, declare a property
with the `@Bindable` attribute, and provide an initial value.

## See Also

### Creating a bindable value

`init(Value)`

Creates a bindable object from an observable object.

Available when `Value` conforms to `Observable`.

`init(projectedValue: Bindable<Value>)`

Creates a bindable from the value of another bindable.

Available when `Value` conforms to `Observable`.

Initializer

# init(projectedValue:)

Creates a bindable from the value of another bindable.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init(projectedValue: Bindable<Value>)

Available when `Value` conforms to `Observable`.

## See Also

### Creating a bindable value

`init(Value)`

Creates a bindable object from an observable object.

Available when `Value` conforms to `Observable`.

`init(wrappedValue: Value)`

Creates a bindable object from an observable object.

Available when `Value` conforms to `Observable`.

Instance Property

# wrappedValue

The wrapped object.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var wrappedValue: Value

## See Also

### Getting the value

`var projectedValue: Bindable<Value>`

The bindable wrapper for the object that creates bindings to its properties
using dynamic member lookup.

`subscript<Subject>(dynamicMember _: ReferenceWritableKeyPath<Value, Subject>)
-> Binding<Subject>`

Returns a binding to the value of a given key path.

Instance Property

# projectedValue

The bindable wrapper for the object that creates bindings to its properties
using dynamic member lookup.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var projectedValue: Bindable<Value> { get }

## See Also

### Getting the value

`var wrappedValue: Value`

The wrapped object.

`subscript<Subject>(dynamicMember _: ReferenceWritableKeyPath<Value, Subject>)
-> Binding<Subject>`

Returns a binding to the value of a given key path.

Instance Subscript

# subscript(dynamicMember:)

Returns a binding to the value of a given key path.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    subscript<Subject>(dynamicMember keyPath: ReferenceWritableKeyPath<Value, Subject>) -> Binding<Subject> { get }

## See Also

### Getting the value

`var wrappedValue: Value`

The wrapped object.

`var projectedValue: Bindable<Value>`

The bindable wrapper for the object that creates bindings to its properties
using dynamic member lookup.



# ButtonToggleStyle

Initializer

# init()

Creates a button toggle style.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  watchOS 9.0+
visionOS 1.0+

    
    
    init()

## Discussion

Don’t call this initializer directly. Instead, use the `button` static
variable to create this style:

Instance Method

# makeBody(configuration:)

Creates a view that represents the body of a toggle button.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  watchOS 9.0+
visionOS 1.0+

    
    
    func makeBody(configuration: ButtonToggleStyle.Configuration) -> some View
    

##  Parameters

`configuration`

    

The properties of the toggle, including a label and a binding to the toggle’s
state.

## Return Value

A view that acts as a button that controls a Boolean state.

## Discussion

SwiftUI implements this required method of the `ToggleStyle` protocol to
define the behavior and appearance of the `button` toggle style. Don’t call
this method directly; the system calls this method for each `Toggle` instance
in a view hierarchy that’s styled as a button.



# BorderedButtonStyle

Initializer

# init()

Creates a bordered button style.

iOS 15.0+  iPadOS 15.0+  macOS 10.15+  Mac Catalyst 15.0+  tvOS 13.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init()

Instance Method

# makeBody(configuration:)

Creates a view that represents the body of a button.

iOS 15.0+  iPadOS 15.0+  macOS 10.15+  Mac Catalyst 15.0+  tvOS 13.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func makeBody(configuration: BorderedButtonStyle.Configuration) -> some View
    

##  Parameters

`configuration`

    

The properties of the button.

## Discussion

The system calls this method for each `Button` instance in a view hierarchy
where this style is the current button style.

Initializer

# init(tint:)

Creates a bordered button style with a tint color.

watchOS 7.0–10.4  Deprecated

    
    
    init(tint: Color)

Deprecated

Use `tint(_:)` instead.



# BlurReplaceTransition.Configuration

Type Property

# downUp

A configuration that requests a transition that scales the view down while
removing it and up while inserting it.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static let downUp: BlurReplaceTransition.Configuration

## See Also

### Getting the transition configuration

`static let upUp: BlurReplaceTransition.Configuration`

A configuration that requests a transition that scales the view up while both
removing and inserting it.

Type Property

# upUp

A configuration that requests a transition that scales the view up while both
removing and inserting it.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static let upUp: BlurReplaceTransition.Configuration

## See Also

### Getting the transition configuration

`static let downUp: BlurReplaceTransition.Configuration`

A configuration that requests a transition that scales the view down while
removing it and up while inserting it.



# BorderedProminentButtonStyle

Initializer

# init()

Creates a bordered prominent button style.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init()



# Binding

Initializer

# init(_:)

Creates a binding by projecting the base value to an unwrapped value.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init?(_ base: Binding<Value?>)

##  Parameters

`base`

    

A value to project to an unwrapped value.

## Return Value

A new binding or `nil` when `base` is `nil`.

## See Also

### Creating a binding

`init<V>(Binding<V>)`

Creates a binding by projecting the base value to an optional value.

`init<V>(Binding<V>)`

Creates a binding by projecting the base value to a hashable value.

`init(projectedValue: Binding<Value>)`

Creates a binding from the value of another binding.

`init(get: () -> Value, set: (Value, Transaction) -> Void)`

Creates a binding with a closure that reads from the binding value, and a
closure that applies a transaction when writing to the binding value.

`init(get: () -> Value, set: (Value) -> Void)`

Creates a binding with closures that read and write the binding value.

`static func constant(Value) -> Binding<Value>`

Creates a binding with an immutable value.

Initializer

# init(_:)

Creates a binding by projecting the base value to an optional value.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init<V>(_ base: Binding<V>) where Value == V?

##  Parameters

`base`

    

A value to project to an optional value.

## See Also

### Creating a binding

`init?(Binding<Value?>)`

Creates a binding by projecting the base value to an unwrapped value.

`init<V>(Binding<V>)`

Creates a binding by projecting the base value to a hashable value.

`init(projectedValue: Binding<Value>)`

Creates a binding from the value of another binding.

`init(get: () -> Value, set: (Value, Transaction) -> Void)`

Creates a binding with a closure that reads from the binding value, and a
closure that applies a transaction when writing to the binding value.

`init(get: () -> Value, set: (Value) -> Void)`

Creates a binding with closures that read and write the binding value.

`static func constant(Value) -> Binding<Value>`

Creates a binding with an immutable value.

Initializer

# init(_:)

Creates a binding by projecting the base value to a hashable value.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init<V>(_ base: Binding<V>) where Value == AnyHashable, V : Hashable

##  Parameters

`base`

    

A `Hashable` value to project to an `AnyHashable` value.

## See Also

### Creating a binding

`init?(Binding<Value?>)`

Creates a binding by projecting the base value to an unwrapped value.

`init<V>(Binding<V>)`

Creates a binding by projecting the base value to an optional value.

`init(projectedValue: Binding<Value>)`

Creates a binding from the value of another binding.

`init(get: () -> Value, set: (Value, Transaction) -> Void)`

Creates a binding with a closure that reads from the binding value, and a
closure that applies a transaction when writing to the binding value.

`init(get: () -> Value, set: (Value) -> Void)`

Creates a binding with closures that read and write the binding value.

`static func constant(Value) -> Binding<Value>`

Creates a binding with an immutable value.

Initializer

# init(projectedValue:)

Creates a binding from the value of another binding.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(projectedValue: Binding<Value>)

## See Also

### Creating a binding

`init?(Binding<Value?>)`

Creates a binding by projecting the base value to an unwrapped value.

`init<V>(Binding<V>)`

Creates a binding by projecting the base value to an optional value.

`init<V>(Binding<V>)`

Creates a binding by projecting the base value to a hashable value.

`init(get: () -> Value, set: (Value, Transaction) -> Void)`

Creates a binding with a closure that reads from the binding value, and a
closure that applies a transaction when writing to the binding value.

`init(get: () -> Value, set: (Value) -> Void)`

Creates a binding with closures that read and write the binding value.

`static func constant(Value) -> Binding<Value>`

Creates a binding with an immutable value.

Initializer

# init(get:set:)

Creates a binding with a closure that reads from the binding value, and a
closure that applies a transaction when writing to the binding value.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        get: @escaping () -> Value,
        set: @escaping (Value, Transaction) -> Void
    )

##  Parameters

`get`

    

A closure to retrieve the binding value. The closure has no parameters, and
returns a value.

`set`

    

A closure to set the binding value. The closure has the following parameters:

  * newValue: The new value of the binding value.

  * transaction: The transaction to apply when setting a new value.

## See Also

### Creating a binding

`init?(Binding<Value?>)`

Creates a binding by projecting the base value to an unwrapped value.

`init<V>(Binding<V>)`

Creates a binding by projecting the base value to an optional value.

`init<V>(Binding<V>)`

Creates a binding by projecting the base value to a hashable value.

`init(projectedValue: Binding<Value>)`

Creates a binding from the value of another binding.

`init(get: () -> Value, set: (Value) -> Void)`

Creates a binding with closures that read and write the binding value.

`static func constant(Value) -> Binding<Value>`

Creates a binding with an immutable value.

Initializer

# init(get:set:)

Creates a binding with closures that read and write the binding value.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        get: @escaping () -> Value,
        set: @escaping (Value) -> Void
    )

##  Parameters

`get`

    

A closure that retrieves the binding value. The closure has no parameters, and
returns a value.

`set`

    

A closure that sets the binding value. The closure has the following
parameter:

  * newValue: The new value of the binding value.

## See Also

### Creating a binding

`init?(Binding<Value?>)`

Creates a binding by projecting the base value to an unwrapped value.

`init<V>(Binding<V>)`

Creates a binding by projecting the base value to an optional value.

`init<V>(Binding<V>)`

Creates a binding by projecting the base value to a hashable value.

`init(projectedValue: Binding<Value>)`

Creates a binding from the value of another binding.

`init(get: () -> Value, set: (Value, Transaction) -> Void)`

Creates a binding with a closure that reads from the binding value, and a
closure that applies a transaction when writing to the binding value.

`static func constant(Value) -> Binding<Value>`

Creates a binding with an immutable value.

Type Method

# constant(_:)

Creates a binding with an immutable value.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static func constant(_ value: Value) -> Binding<Value>

##  Parameters

`value`

    

An immutable value.

## Discussion

Use this method to create a binding to a value that cannot change. This can be
useful when using a `PreviewProvider` to see how a view represents different
values.

## See Also

### Creating a binding

`init?(Binding<Value?>)`

Creates a binding by projecting the base value to an unwrapped value.

`init<V>(Binding<V>)`

Creates a binding by projecting the base value to an optional value.

`init<V>(Binding<V>)`

Creates a binding by projecting the base value to a hashable value.

`init(projectedValue: Binding<Value>)`

Creates a binding from the value of another binding.

`init(get: () -> Value, set: (Value, Transaction) -> Void)`

Creates a binding with a closure that reads from the binding value, and a
closure that applies a transaction when writing to the binding value.

`init(get: () -> Value, set: (Value) -> Void)`

Creates a binding with closures that read and write the binding value.

Instance Property

# wrappedValue

The underlying value referenced by the binding variable.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var wrappedValue: Value { get nonmutating set }

## Discussion

This property provides primary access to the value’s data. However, you don’t
access `wrappedValue` directly. Instead, you use the property variable created
with the `Binding` attribute. In the following code example, the binding
variable `isPlaying` returns the value of `wrappedValue`:

When a mutable binding value changes, the new value is immediately available.
However, updates to a view displaying the value happens asynchronously, so the
view may not show the change immediately.

## See Also

### Getting the value

`var projectedValue: Binding<Value>`

A projection of the binding value that returns a binding.

`subscript<Subject>(dynamicMember _: WritableKeyPath<Value, Subject>) ->
Binding<Subject>`

Returns a binding to the resulting value of a given key path.

Instance Property

# projectedValue

A projection of the binding value that returns a binding.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var projectedValue: Binding<Value> { get }

## Discussion

Use the projected value to pass a binding value down a view hierarchy. To get
the `projectedValue`, prefix the property variable with `$`. For example, in
the following code example `PlayerView` projects a binding of the state
property `isPlaying` to the `PlayButton` view using `$isPlaying`.

## See Also

### Getting the value

`var wrappedValue: Value`

The underlying value referenced by the binding variable.

`subscript<Subject>(dynamicMember _: WritableKeyPath<Value, Subject>) ->
Binding<Subject>`

Returns a binding to the resulting value of a given key path.

Instance Subscript

# subscript(dynamicMember:)

Returns a binding to the resulting value of a given key path.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    subscript<Subject>(dynamicMember keyPath: WritableKeyPath<Value, Subject>) -> Binding<Subject> { get }

##  Parameters

`keyPath`

    

A key path to a specific resulting value.

## Return Value

A new binding.

## See Also

### Getting the value

`var wrappedValue: Value`

The underlying value referenced by the binding variable.

`var projectedValue: Binding<Value>`

A projection of the binding value that returns a binding.

Instance Property

# id

The stable identity of the entity associated with this instance, corresponding
to the `id` of the binding’s wrapped value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var id: Value.ID { get }

Available when `Value` conforms to `Identifiable`.

## See Also

### Managing changes

`func animation(Animation?) -> Binding<Value>`

Specifies an animation to perform when the binding value changes.

`func transaction(Transaction) -> Binding<Value>`

Specifies a transaction for the binding.

`var transaction: Transaction`

The binding’s transaction.

Instance Method

# animation(_:)

Specifies an animation to perform when the binding value changes.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func animation(_ animation: Animation? = .default) -> Binding<Value>

##  Parameters

`animation`

    

An animation sequence performed when the binding value changes.

## Return Value

A new binding.

## See Also

### Managing changes

`var id: Value.ID`

The stable identity of the entity associated with this instance, corresponding
to the `id` of the binding’s wrapped value.

Available when `Value` conforms to `Identifiable`.

`func transaction(Transaction) -> Binding<Value>`

Specifies a transaction for the binding.

`var transaction: Transaction`

The binding’s transaction.

Instance Method

# transaction(_:)

Specifies a transaction for the binding.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func transaction(_ transaction: Transaction) -> Binding<Value>

##  Parameters

`transaction `

    

An instance of a `Transaction`.

## Return Value

A new binding.

## See Also

### Managing changes

`var id: Value.ID`

The stable identity of the entity associated with this instance, corresponding
to the `id` of the binding’s wrapped value.

Available when `Value` conforms to `Identifiable`.

`func animation(Animation?) -> Binding<Value>`

Specifies an animation to perform when the binding value changes.

`var transaction: Transaction`

The binding’s transaction.

Instance Property

# transaction

The binding’s transaction.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var transaction: Transaction

## Discussion

The transaction captures the information needed to update the view when the
binding value changes.

## See Also

### Managing changes

`var id: Value.ID`

The stable identity of the entity associated with this instance, corresponding
to the `id` of the binding’s wrapped value.

Available when `Value` conforms to `Identifiable`.

`func animation(Animation?) -> Binding<Value>`

Specifies an animation to perform when the binding value changes.

`func transaction(Transaction) -> Binding<Value>`

Specifies a transaction for the binding.

Collection

API Collection

# Identifiable Implementations

## Topics

### Instance Properties

`var id: Value.ID`

The stable identity of the entity associated with this instance, corresponding
to the `id` of the binding’s wrapped value.

Available when `Value` conforms to `Identifiable`.



# BorderlessButtonMenuStyle

Initializer

# init()

Creates a borderless button menu style.

iOS 14.0–17.4  Deprecated  iPadOS 14.0–17.4  Deprecated  macOS 11.0–14.4
Deprecated  Mac Catalyst 14.0–17.4  Deprecated  tvOS 17.0–17.4  Deprecated
visionOS 1.0+

    
    
    init()

Deprecated

Use `menuStyle(_:)` with `button` and `buttonStyle(_:)` with `borderless`.

## See Also

### Creating a bordeless button menu style

`init(showsMenuIndicator: Bool)`

Creates a borderless button menu style, specifying whether to show a visual
menu indicator.

Deprecated

Initializer

# init(showsMenuIndicator:)

Creates a borderless button menu style, specifying whether to show a visual
menu indicator.

macOS 11.0–12.0  Deprecated  tvOS 17.0–17.4  Deprecated

    
    
    init(showsMenuIndicator: Bool)

Deprecated

Use `View/menuIndicator(_)` instead.

##  Parameters

`showsMenuIndicator`

    

A Boolean that indicates whether the button should include a visual indicator
that it represents a menu, such as an arrow.

## See Also

### Creating a bordeless button menu style

`init()`

Creates a borderless button menu style.

Deprecated



# BlendMode

Case

# BlendMode.normal

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case normal

Case

# BlendMode.darken

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case darken

## See Also

### Darkening

`case multiply`

`case colorBurn`

`case plusDarker`

Case

# BlendMode.multiply

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case multiply

## See Also

### Darkening

`case darken`

`case colorBurn`

`case plusDarker`

Case

# BlendMode.colorBurn

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case colorBurn

## See Also

### Darkening

`case darken`

`case multiply`

`case plusDarker`

Case

# BlendMode.plusDarker

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case plusDarker

## See Also

### Darkening

`case darken`

`case multiply`

`case colorBurn`

Case

# BlendMode.lighten

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case lighten

## See Also

### Lightening

`case screen`

`case colorDodge`

`case plusLighter`

Case

# BlendMode.screen

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case screen

## See Also

### Lightening

`case lighten`

`case colorDodge`

`case plusLighter`

Case

# BlendMode.colorDodge

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case colorDodge

## See Also

### Lightening

`case lighten`

`case screen`

`case plusLighter`

Case

# BlendMode.plusLighter

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case plusLighter

## See Also

### Lightening

`case lighten`

`case screen`

`case colorDodge`

Case

# BlendMode.overlay

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case overlay

## See Also

### Adding contrast

`case softLight`

`case hardLight`

Case

# BlendMode.softLight

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case softLight

## See Also

### Adding contrast

`case overlay`

`case hardLight`

Case

# BlendMode.hardLight

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case hardLight

## See Also

### Adding contrast

`case overlay`

`case softLight`

Case

# BlendMode.difference

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case difference

## See Also

### Inverting

`case exclusion`

Case

# BlendMode.exclusion

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case exclusion

## See Also

### Inverting

`case difference`

Case

# BlendMode.hue

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case hue

## See Also

### Mixing color components

`case saturation`

`case color`

`case luminosity`

Case

# BlendMode.saturation

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case saturation

## See Also

### Mixing color components

`case hue`

`case color`

`case luminosity`

Case

# BlendMode.color

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case color

## See Also

### Mixing color components

`case hue`

`case saturation`

`case luminosity`

Case

# BlendMode.luminosity

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case luminosity

## See Also

### Mixing color components

`case hue`

`case saturation`

`case color`

Case

# BlendMode.sourceAtop

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case sourceAtop

## See Also

### Accessing porter-duff modes

`case destinationOver`

`case destinationOut`

Case

# BlendMode.destinationOver

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case destinationOver

## See Also

### Accessing porter-duff modes

`case sourceAtop`

`case destinationOut`

Case

# BlendMode.destinationOut

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case destinationOut

## See Also

### Accessing porter-duff modes

`case sourceAtop`

`case destinationOver`



# ButtonStyle

Instance Method

# makeBody(configuration:)

Creates a view that represents the body of a button.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @ViewBuilder
    func makeBody(configuration: Self.Configuration) -> Self.Body

**Required**

##  Parameters

`configuration `

    

The properties of the button.

## Discussion

The system calls this method for each `Button` instance in a view hierarchy
where this style is the current button style.

## See Also

### Custom button styles

`typealias Configuration`

The properties of a button.

`associatedtype Body : View`

A view that represents the body of a button.

**Required**

Type Alias

# ButtonStyle.Configuration

The properties of a button.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    typealias Configuration = ButtonStyleConfiguration

## See Also

### Custom button styles

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Creates a view that represents the body of a button.

**Required**

` associatedtype Body : View`

A view that represents the body of a button.

**Required**

Associated Type

# Body

A view that represents the body of a button.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    associatedtype Body : View

**Required**

## See Also

### Custom button styles

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Creates a view that represents the body of a button.

**Required**

` typealias Configuration`

The properties of a button.



# BorderlessButtonMenuButtonStyle

Initializer

# init()

macOS 10.15–14.4  Deprecated

    
    
    init()

Deprecated

Use `BorderlessButtonMenuStyle` instead.



# ButtonBorderShape

Type Property

# automatic

A shape that defers to the system to determine an appropriate shape for the
given context and platform.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static let automatic: ButtonBorderShape

## See Also

### Getting border shapes

`static let capsule: ButtonBorderShape`

A capsule shape.

`static let circle: ButtonBorderShape`

`static let roundedRectangle: ButtonBorderShape`

A rounded rectangle shape.

`static func roundedRectangle(radius: CGFloat) -> ButtonBorderShape`

A rounded rectangle shape.

Type Property

# capsule

A capsule shape.

iOS 15.0+  iPadOS 15.0+  macOS 14.0+  Mac Catalyst 15.0+  tvOS 17.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static let capsule: ButtonBorderShape

## Discussion

Note

This has no effect on non-widget system buttons on macOS.

## See Also

### Getting border shapes

`static let automatic: ButtonBorderShape`

A shape that defers to the system to determine an appropriate shape for the
given context and platform.

`static let circle: ButtonBorderShape`

`static let roundedRectangle: ButtonBorderShape`

A rounded rectangle shape.

`static func roundedRectangle(radius: CGFloat) -> ButtonBorderShape`

A rounded rectangle shape.

Type Property

# circle

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 16.4+  watchOS
10.0+  visionOS 1.0+

    
    
    static let circle: ButtonBorderShape

## See Also

### Getting border shapes

`static let automatic: ButtonBorderShape`

A shape that defers to the system to determine an appropriate shape for the
given context and platform.

`static let capsule: ButtonBorderShape`

A capsule shape.

`static let roundedRectangle: ButtonBorderShape`

A rounded rectangle shape.

`static func roundedRectangle(radius: CGFloat) -> ButtonBorderShape`

A rounded rectangle shape.

Type Property

# roundedRectangle

A rounded rectangle shape.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static let roundedRectangle: ButtonBorderShape

## See Also

### Getting border shapes

`static let automatic: ButtonBorderShape`

A shape that defers to the system to determine an appropriate shape for the
given context and platform.

`static let capsule: ButtonBorderShape`

A capsule shape.

`static let circle: ButtonBorderShape`

`static func roundedRectangle(radius: CGFloat) -> ButtonBorderShape`

A rounded rectangle shape.

Type Method

# roundedRectangle(radius:)

A rounded rectangle shape.

iOS 15.0+  iPadOS 15.0+  macOS 14.0+  Mac Catalyst 15.0+  tvOS 17.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static func roundedRectangle(radius: CGFloat) -> ButtonBorderShape

##  Parameters

`radius`

    

the corner radius of the rectangle.

## Discussion

Note

This has no effect on non-widget system buttons on macOS.

## See Also

### Getting border shapes

`static let automatic: ButtonBorderShape`

A shape that defers to the system to determine an appropriate shape for the
given context and platform.

`static let capsule: ButtonBorderShape`

A capsule shape.

`static let circle: ButtonBorderShape`

`static let roundedRectangle: ButtonBorderShape`

A rounded rectangle shape.



# ButtonRepeatBehavior

Type Property

# automatic

The automatic repeat behavior.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static let automatic: ButtonRepeatBehavior

## See Also

### Getting repeat behaviors

`static let enabled: ButtonRepeatBehavior`

Repeating button actions will be enabled.

`static let disabled: ButtonRepeatBehavior`

Repeating button actions will be disabled.

Type Property

# enabled

Repeating button actions will be enabled.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static let enabled: ButtonRepeatBehavior

## See Also

### Getting repeat behaviors

`static let automatic: ButtonRepeatBehavior`

The automatic repeat behavior.

`static let disabled: ButtonRepeatBehavior`

Repeating button actions will be disabled.

Type Property

# disabled

Repeating button actions will be disabled.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static let disabled: ButtonRepeatBehavior

## See Also

### Getting repeat behaviors

`static let automatic: ButtonRepeatBehavior`

The automatic repeat behavior.

`static let enabled: ButtonRepeatBehavior`

Repeating button actions will be enabled.



# BalancedNavigationSplitViewStyle

Initializer

# init()

Creates an instance of `BalancedNavigationSplitViewStyle`.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init()

## Discussion

You can also use `balanced` to construct this style.



# BadgeProminence

Type Property

# standard

The standard level of prominence for a badge.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    static let standard: BadgeProminence

## Discussion

This level of prominence should be used for badges that display a value that
suggests user action, such as a count of unread messages or new invitations.

In lists on macOS, this results in a badge label on a grayscale platter; and
in lists on iOS, this prominence of badge has no platter.

## See Also

### Getting background prominence

`static let increased: BadgeProminence`

The highest level of prominence for a badge.

`static let decreased: BadgeProminence`

The lowest level of prominence for a badge.

Type Property

# increased

The highest level of prominence for a badge.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    static let increased: BadgeProminence

## Discussion

This level of prominence should be used for badges that display a value that
requires user action, such as number of updates or account errors.

In lists on iOS and macOS, this results in badge labels being displayed on a
red platter.

## See Also

### Getting background prominence

`static let standard: BadgeProminence`

The standard level of prominence for a badge.

`static let decreased: BadgeProminence`

The lowest level of prominence for a badge.

Type Property

# decreased

The lowest level of prominence for a badge.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    static let decreased: BadgeProminence

## Discussion

This level or prominence should be used for badges that display a value of
passive information that requires no user action, such as total number of
messages or content.

In lists on iOS and macOS, this results in badge labels being displayed
without any extra decoration. On iOS, this looks the same as `.standard`.

## See Also

### Getting background prominence

`static let standard: BadgeProminence`

The standard level of prominence for a badge.

`static let increased: BadgeProminence`

The highest level of prominence for a badge.



# ButtonRole

Type Property

# cancel

A role that indicates a button that cancels an operation.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static let cancel: ButtonRole

## Discussion

Use this role for a button that cancels the current operation.

## See Also

### Getting button roles

`static let destructive: ButtonRole`

A role that indicates a destructive button.

Type Property

# destructive

A role that indicates a destructive button.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static let destructive: ButtonRole

## Discussion

Use this role for a button that deletes user data, or performs an irreversible
operation. A destructive button signals by its appearance that the user should
carefully consider whether to tap or click the button. For example, SwiftUI
presents a destructive button that you add with the
`swipeActions(edge:allowsFullSwipe:content:)` modifier using a red background:

## See Also

### Getting button roles

`static let cancel: ButtonRole`

A role that indicates a button that cancels an operation.



# BorderedListStyle

Initializer

# init()

Creates a bordered list style.

macOS 12.0+

    
    
    init()

## See Also

### Creating the list style

`init(alternatesRowBackgrounds: Bool)`

Creates a bordered list style with optional alternating row backgrounds.

Deprecated

Initializer

# init(alternatesRowBackgrounds:)

Creates a bordered list style with optional alternating row backgrounds.

macOS 12.0–14.4  Deprecated

    
    
    init(alternatesRowBackgrounds: Bool)

Deprecated

Use the `bordered` style and add the `alternatingRowBackgrounds(_:)` view
modifier instead.

## See Also

### Creating the list style

`init()`

Creates a bordered list style.



# BackgroundTask

Type Property

# appRefresh

A task that updates your app’s state in the background.

watchOS 9.0+

    
    
    static var appRefresh: BackgroundTask<String?, Void> { get }

## See Also

### Refreshing the app

`static func appRefresh(String) -> BackgroundTask<Void, Void>`

A task that updates your app’s state in the background for a matching
identifier.

Type Method

# appRefresh(_:)

A task that updates your app’s state in the background for a matching
identifier.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    static func appRefresh(_ identifier: String) -> BackgroundTask<Void, Void>

##  Parameters

`matching`

    

The identifier to match.

## Return Value

A background task that you can handle with your app or extension.

## See Also

### Refreshing the app

`static var appRefresh: BackgroundTask<String?, Void>`

A task that updates your app’s state in the background.

Type Property

# snapshot

A background task used to update your app’s user interface in preparation for
a snapshot.

watchOS 9.0+

    
    
    static var snapshot: BackgroundTask<SnapshotData, SnapshotResponse> { get }

Type Property

# bluetoothAlert

A background task used to receive critical alerts from paired bluetooth
accessories.

watchOS 9.0+

    
    
    static var bluetoothAlert: BackgroundTask<Void, Void> { get }

## See Also

### Receiving connectivity updates

`static var watchConnectivity: BackgroundTask<Void, Void>`

A background task used to receive background updates from the Watch
Connectivity framework.

Type Property

# watchConnectivity

A background task used to receive background updates from the Watch
Connectivity framework.

watchOS 9.0+

    
    
    static var watchConnectivity: BackgroundTask<Void, Void> { get }

## See Also

### Receiving connectivity updates

`static var bluetoothAlert: BackgroundTask<Void, Void>`

A background task used to receive critical alerts from paired bluetooth
accessories.

Type Property

# urlSession

A task that responds to background URL sessions.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static var urlSession: BackgroundTask<String, Void> { get }

## See Also

### Responding to URL sessions

`static func urlSession(String) -> BackgroundTask<Void, Void>`

A task that responds to background URL sessions matching the given identifier.

`static func urlSession(matching: (String) -> Bool) -> BackgroundTask<String,
Void>`

A task that responds to background URL sessions matching the given predicate.

Type Method

# urlSession(_:)

A task that responds to background URL sessions matching the given identifier.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static func urlSession(_ identifier: String) -> BackgroundTask<Void, Void>

##  Parameters

`identifier`

    

The identifier to match.

## Return Value

A background task that you can handle with your app or extension.

## See Also

### Responding to URL sessions

`static var urlSession: BackgroundTask<String, Void>`

A task that responds to background URL sessions.

`static func urlSession(matching: (String) -> Bool) -> BackgroundTask<String,
Void>`

A task that responds to background URL sessions matching the given predicate.

Type Method

# urlSession(matching:)

A task that responds to background URL sessions matching the given predicate.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static func urlSession(matching: @escaping (String) -> Bool) -> BackgroundTask<String, Void>

##  Parameters

`matching`

    

The predicate to match.

## Return Value

A background task that you can handle with your app or extension.

## See Also

### Responding to URL sessions

`static var urlSession: BackgroundTask<String, Void>`

A task that responds to background URL sessions.

`static func urlSession(String) -> BackgroundTask<Void, Void>`

A task that responds to background URL sessions matching the given identifier.

Type Property

# intentDidRun

A background task used to update your app after a SiriKit intent runs.

watchOS 9.0+

    
    
    static var intentDidRun: BackgroundTask<Void, Void> { get }

## See Also

### Updating intents and shortcuts

`static var relevantShortcut: BackgroundTask<Void, Void>`

A background task used to periodically donate relevant Siri shortcuts.

Type Property

# relevantShortcut

A background task used to periodically donate relevant Siri shortcuts.

watchOS 9.0+

    
    
    static var relevantShortcut: BackgroundTask<Void, Void> { get }

## See Also

### Updating intents and shortcuts

`static var intentDidRun: BackgroundTask<Void, Void>`

A background task used to update your app after a SiriKit intent runs.



# BackgroundProminence

Type Property

# standard

The standard prominence of a background

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static let standard: BackgroundProminence

## Discussion

This is the default level of prominence and doesn’t require any adjustment to
achieve satisfactory contrast with the background.

## See Also

### Getting background prominence

`static let increased: BackgroundProminence`

A more prominent background that likely requires some changes to the views
above it.

Type Property

# increased

A more prominent background that likely requires some changes to the views
above it.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static let increased: BackgroundProminence

## Discussion

This is the level of prominence for more highly saturated and full color
backgrounds, such as focused/emphasized selected list rows. Typically
foreground content should take on monochrome styling to have greater contrast
against the background.

## See Also

### Getting background prominence

`static let standard: BackgroundProminence`

The standard prominence of a background



# BorderlessPullDownMenuButtonStyle

Initializer

# init()

macOS 10.15–14.4  Deprecated

    
    
    init()

Deprecated

Use `BorderlessButtonMenuStyle` instead.



# BorderlessButtonStyle

Initializer

# init()

Creates a borderless button style.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 17.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init()

Instance Method

# makeBody(configuration:)

Creates a view that represents the body of a button.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 17.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func makeBody(configuration: BorderlessButtonStyle.Configuration) -> some View
    

##  Parameters

`configuration `

    

The properties of the button.

## Discussion

The system calls this method for each `Button` instance in a view hierarchy
where this style is the current button style.



