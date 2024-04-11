Initializer

# init(isOn:label:)

Creates a toggle that displays a custom label.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        isOn: Binding<Bool>,
        @ViewBuilder label: () -> Label
    )

##  Parameters

`isOn`

    

A binding to a property that determines whether the toggle is on or off.

`label`

    

A view that describes the purpose of the toggle.

## See Also

### Creating a toggle

`init(LocalizedStringKey, isOn: Binding<Bool>)`

Creates a toggle that generates its label from a localized string key.

Available when `Label` is `Text`.

`init<S>(S, isOn: Binding<Bool>)`

Creates a toggle that generates its label from a string.

Available when `Label` is `Text`.

Initializer

# init(_:isOn:)

Creates a toggle that generates its label from a localized string key.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        isOn: Binding<Bool>
    )

Available when `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the toggle’s localized title, that describes the purpose of the
toggle.

`isOn`

    

A binding to a property that indicates whether the toggle is on or off.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

To initialize a toggle with a string variable, use `init(_:isOn:)` instead.

## See Also

### Creating a toggle

`init(isOn: Binding<Bool>, label: () -> Label)`

Creates a toggle that displays a custom label.

`init<S>(S, isOn: Binding<Bool>)`

Creates a toggle that generates its label from a string.

Available when `Label` is `Text`.

Initializer

# init(_:isOn:)

Creates a toggle that generates its label from a string.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        isOn: Binding<Bool>
    ) where S : StringProtocol

Available when `Label` is `Text`.

##  Parameters

`title`

    

A string that describes the purpose of the toggle.

`isOn`

    

A binding to a property that indicates whether the toggle is on or off.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the title
similar to `init(_:)`. See `Text` for more information about localizing
strings.

To initialize a toggle with a localized string key, use `init(_:isOn:)`
instead.

## See Also

### Creating a toggle

`init(isOn: Binding<Bool>, label: () -> Label)`

Creates a toggle that displays a custom label.

`init(LocalizedStringKey, isOn: Binding<Bool>)`

Creates a toggle that generates its label from a localized string key.

Available when `Label` is `Text`.

Initializer

# init(sources:isOn:label:)

Creates a toggle representing a collection of values with a custom label.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init<C>(
        sources: C,
        isOn: KeyPath<C.Element, Binding<Bool>>,
        @ViewBuilder label: () -> Label
    ) where C : RandomAccessCollection

##  Parameters

`sources`

    

A collection of values used as the source for rendering the Toggle’s state.

`isOn`

    

The key path of the values that determines whether the toggle is on, mixed or
off.

`label`

    

A view that describes the purpose of the toggle.

## Discussion

The following example creates a single toggle that represents the state of
multiple alarms:

## See Also

### Creating a toggle for a collection

`init<S, C>(S, sources: C, isOn: KeyPath<C.Element, Binding<Bool>>)`

Creates a toggle representing a collection of values that generates its label
from a string.

Available when `Label` is `Text`.

`init<C>(LocalizedStringKey, sources: C, isOn: KeyPath<C.Element,
Binding<Bool>>)`

Creates a toggle representing a collection of values that generates its label
from a localized string key.

Available when `Label` is `Text`.

Initializer

# init(_:sources:isOn:)

Creates a toggle representing a collection of values that generates its label
from a string.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init<S, C>(
        _ title: S,
        sources: C,
        isOn: KeyPath<C.Element, Binding<Bool>>
    ) where S : StringProtocol, C : RandomAccessCollection

Available when `Label` is `Text`.

##  Parameters

`title`

    

A string that describes the purpose of the toggle.

`sources`

    

A collection of values used as the source for rendering the Toggle’s state.

`isOn`

    

The key path of the values that determines whether the toggle is on, mixed or
off.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the title
similar to `init(_:)`. See `Text` for more information about localizing
strings.

The following example creates a single toggle that represents the state of
multiple alarms:

## See Also

### Creating a toggle for a collection

`init<C>(sources: C, isOn: KeyPath<C.Element, Binding<Bool>>, label: () ->
Label)`

Creates a toggle representing a collection of values with a custom label.

`init<C>(LocalizedStringKey, sources: C, isOn: KeyPath<C.Element,
Binding<Bool>>)`

Creates a toggle representing a collection of values that generates its label
from a localized string key.

Available when `Label` is `Text`.

Initializer

# init(_:sources:isOn:)

Creates a toggle representing a collection of values that generates its label
from a localized string key.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init<C>(
        _ titleKey: LocalizedStringKey,
        sources: C,
        isOn: KeyPath<C.Element, Binding<Bool>>
    ) where C : RandomAccessCollection

Available when `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the toggle’s localized title, that describes the purpose of the
toggle.

`sources`

    

A collection of values used as the source for rendering the Toggle’s state.

`isOn`

    

The key path of the values that determines whether the toggle is on, mixed or
off.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

The following example creates a single toggle that represents the state of
multiple alarms:

## See Also

### Creating a toggle for a collection

`init<C>(sources: C, isOn: KeyPath<C.Element, Binding<Bool>>, label: () ->
Label)`

Creates a toggle representing a collection of values with a custom label.

`init<S, C>(S, sources: C, isOn: KeyPath<C.Element, Binding<Bool>>)`

Creates a toggle representing a collection of values that generates its label
from a string.

Available when `Label` is `Text`.

Initializer

# init(_:image:isOn:)

Creates a toggle that generates its label from a localized string key and
image resource.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        image: ImageResource,
        isOn: Binding<Bool>
    )

Available when `Label` is `Label<Text, Image>`.

##  Parameters

`titleKey`

    

The key for the toggle’s localized title, that describes the purpose of the
toggle.

`image`

    

The name of the image resource to lookup.

`isOn`

    

A binding to a property that indicates whether the toggle is on or off.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

To initialize a toggle with a string variable, use `init(_:isOn:)` instead.

## See Also

### Creating a toggle with an image resource label

`init<S>(S, image: ImageResource, isOn: Binding<Bool>)`

Creates a toggle that generates its label from a string and image resource.

Available when `Label` is `Label<Text, Image>`.

`init<C>(LocalizedStringKey, image: ImageResource, sources: C, isOn:
KeyPath<C.Element, Binding<Bool>>)`

Creates a toggle representing a collection of values that generates its label
from a localized string key and image resource.

Available when `Label` is `Label<Text, Image>`.

`init<S, C>(S, image: ImageResource, sources: C, isOn: KeyPath<C.Element,
Binding<Bool>>)`

Creates a toggle representing a collection of values that generates its label
from a string and image resource.

Available when `Label` is `Label<Text, Image>`.

Initializer

# init(_:image:isOn:)

Creates a toggle that generates its label from a string and image resource.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        image: ImageResource,
        isOn: Binding<Bool>
    ) where S : StringProtocol

Available when `Label` is `Label<Text, Image>`.

##  Parameters

`title`

    

A string that describes the purpose of the toggle.

`image`

    

The name of the image resource to lookup.

`isOn`

    

A binding to a property that indicates whether the toggle is on or off.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the title
similar to `init(_:)`. See `Text` for more information about localizing
strings.

To initialize a toggle with a localized string key, use `init(_:isOn:)`
instead.

## See Also

### Creating a toggle with an image resource label

`init(LocalizedStringKey, image: ImageResource, isOn: Binding<Bool>)`

Creates a toggle that generates its label from a localized string key and
image resource.

Available when `Label` is `Label<Text, Image>`.

`init<C>(LocalizedStringKey, image: ImageResource, sources: C, isOn:
KeyPath<C.Element, Binding<Bool>>)`

Creates a toggle representing a collection of values that generates its label
from a localized string key and image resource.

Available when `Label` is `Label<Text, Image>`.

`init<S, C>(S, image: ImageResource, sources: C, isOn: KeyPath<C.Element,
Binding<Bool>>)`

Creates a toggle representing a collection of values that generates its label
from a string and image resource.

Available when `Label` is `Label<Text, Image>`.

Initializer

# init(_:image:sources:isOn:)

Creates a toggle representing a collection of values that generates its label
from a localized string key and image resource.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init<C>(
        _ titleKey: LocalizedStringKey,
        image: ImageResource,
        sources: C,
        isOn: KeyPath<C.Element, Binding<Bool>>
    ) where C : RandomAccessCollection

Available when `Label` is `Label<Text, Image>`.

##  Parameters

`titleKey`

    

The key for the toggle’s localized title, that describes the purpose of the
toggle.

`image`

    

The name of the image resource to lookup.

`sources`

    

A collection of values used as the source for rendering the Toggle’s state.

`isOn`

    

The key path of the values that determines whether the toggle is on, mixed or
off.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

The following example creates a single toggle that represents the state of
multiple alarms:

## See Also

### Creating a toggle with an image resource label

`init(LocalizedStringKey, image: ImageResource, isOn: Binding<Bool>)`

Creates a toggle that generates its label from a localized string key and
image resource.

Available when `Label` is `Label<Text, Image>`.

`init<S>(S, image: ImageResource, isOn: Binding<Bool>)`

Creates a toggle that generates its label from a string and image resource.

Available when `Label` is `Label<Text, Image>`.

`init<S, C>(S, image: ImageResource, sources: C, isOn: KeyPath<C.Element,
Binding<Bool>>)`

Creates a toggle representing a collection of values that generates its label
from a string and image resource.

Available when `Label` is `Label<Text, Image>`.

Initializer

# init(_:image:sources:isOn:)

Creates a toggle representing a collection of values that generates its label
from a string and image resource.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init<S, C>(
        _ title: S,
        image: ImageResource,
        sources: C,
        isOn: KeyPath<C.Element, Binding<Bool>>
    ) where S : StringProtocol, C : RandomAccessCollection

Available when `Label` is `Label<Text, Image>`.

##  Parameters

`title`

    

A string that describes the purpose of the toggle.

`image`

    

The name of the image resource to lookup.

`sources`

    

A collection of values used as the source for rendering the Toggle’s state.

`isOn`

    

The key path of the values that determines whether the toggle is on, mixed or
off.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the title
similar to `init(_:)`. See `Text` for more information about localizing
strings.

The following example creates a single toggle that represents the state of
multiple alarms:

## See Also

### Creating a toggle with an image resource label

`init(LocalizedStringKey, image: ImageResource, isOn: Binding<Bool>)`

Creates a toggle that generates its label from a localized string key and
image resource.

Available when `Label` is `Label<Text, Image>`.

`init<S>(S, image: ImageResource, isOn: Binding<Bool>)`

Creates a toggle that generates its label from a string and image resource.

Available when `Label` is `Label<Text, Image>`.

`init<C>(LocalizedStringKey, image: ImageResource, sources: C, isOn:
KeyPath<C.Element, Binding<Bool>>)`

Creates a toggle representing a collection of values that generates its label
from a localized string key and image resource.

Available when `Label` is `Label<Text, Image>`.

Initializer

# init(_:systemImage:isOn:)

Creates a toggle that generates its label from a localized string key and
system image.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        systemImage: String,
        isOn: Binding<Bool>
    )

Available when `Label` is `Label<Text, Image>`.

##  Parameters

`titleKey`

    

The key for the toggle’s localized title, that describes the purpose of the
toggle.

`systemImage`

    

The name of the image resource to lookup.

`isOn`

    

A binding to a property that indicates whether the toggle is on or off.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

To initialize a toggle with a string variable, use `init(_:isOn:)` instead.

## See Also

### Creating a toggle with an system image

`init<S>(S, systemImage: String, isOn: Binding<Bool>)`

Creates a toggle that generates its label from a string and system image.

Available when `Label` is `Label<Text, Image>`.

`init<C>(LocalizedStringKey, systemImage: String, sources: C, isOn:
KeyPath<C.Element, Binding<Bool>>)`

Creates a toggle representing a collection of values that generates its label
from a localized string key and system image.

Available when `Label` is `Label<Text, Image>`.

`init<S, C>(S, systemImage: String, sources: C, isOn: KeyPath<C.Element,
Binding<Bool>>)`

Creates a toggle representing a collection of values that generates its label
from a string.

Available when `Label` is `Label<Text, Image>`.

Initializer

# init(_:systemImage:isOn:)

Creates a toggle that generates its label from a string and system image.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        systemImage: String,
        isOn: Binding<Bool>
    ) where S : StringProtocol

Available when `Label` is `Label<Text, Image>`.

##  Parameters

`title`

    

A string that describes the purpose of the toggle.

`systemImage`

    

The name of the image resource to lookup.

`isOn`

    

A binding to a property that indicates whether the toggle is on or off.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the title
similar to `init(_:)`. See `Text` for more information about localizing
strings.

To initialize a toggle with a localized string key, use `init(_:isOn:)`
instead.

## See Also

### Creating a toggle with an system image

`init(LocalizedStringKey, systemImage: String, isOn: Binding<Bool>)`

Creates a toggle that generates its label from a localized string key and
system image.

Available when `Label` is `Label<Text, Image>`.

`init<C>(LocalizedStringKey, systemImage: String, sources: C, isOn:
KeyPath<C.Element, Binding<Bool>>)`

Creates a toggle representing a collection of values that generates its label
from a localized string key and system image.

Available when `Label` is `Label<Text, Image>`.

`init<S, C>(S, systemImage: String, sources: C, isOn: KeyPath<C.Element,
Binding<Bool>>)`

Creates a toggle representing a collection of values that generates its label
from a string.

Available when `Label` is `Label<Text, Image>`.

Initializer

# init(_:systemImage:sources:isOn:)

Creates a toggle representing a collection of values that generates its label
from a localized string key and system image.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init<C>(
        _ titleKey: LocalizedStringKey,
        systemImage: String,
        sources: C,
        isOn: KeyPath<C.Element, Binding<Bool>>
    ) where C : RandomAccessCollection

Available when `Label` is `Label<Text, Image>`.

##  Parameters

`titleKey`

    

The key for the toggle’s localized title, that describes the purpose of the
toggle.

`systemImage`

    

The name of the image resource to lookup.

`sources`

    

A collection of values used as the source for rendering the Toggle’s state.

`isOn`

    

The key path of the values that determines whether the toggle is on, mixed or
off.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

The following example creates a single toggle that represents the state of
multiple alarms:

## See Also

### Creating a toggle with an system image

`init(LocalizedStringKey, systemImage: String, isOn: Binding<Bool>)`

Creates a toggle that generates its label from a localized string key and
system image.

Available when `Label` is `Label<Text, Image>`.

`init<S>(S, systemImage: String, isOn: Binding<Bool>)`

Creates a toggle that generates its label from a string and system image.

Available when `Label` is `Label<Text, Image>`.

`init<S, C>(S, systemImage: String, sources: C, isOn: KeyPath<C.Element,
Binding<Bool>>)`

Creates a toggle representing a collection of values that generates its label
from a string.

Available when `Label` is `Label<Text, Image>`.

Initializer

# init(_:systemImage:sources:isOn:)

Creates a toggle representing a collection of values that generates its label
from a string.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init<S, C>(
        _ title: S,
        systemImage: String,
        sources: C,
        isOn: KeyPath<C.Element, Binding<Bool>>
    ) where S : StringProtocol, C : RandomAccessCollection

Available when `Label` is `Label<Text, Image>`.

##  Parameters

`title`

    

A string that describes the purpose of the toggle.

`systemImage`

    

The name of the image resource to lookup.

`sources`

    

A collection of values used as the source for rendering the Toggle’s state.

`isOn`

    

The key path of the values that determines whether the toggle is on, mixed or
off.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the title
similar to `init(_:)`. See `Text` for more information about localizing
strings.

The following example creates a single toggle that represents the state of
multiple alarms:

## See Also

### Creating a toggle with an system image

`init(LocalizedStringKey, systemImage: String, isOn: Binding<Bool>)`

Creates a toggle that generates its label from a localized string key and
system image.

Available when `Label` is `Label<Text, Image>`.

`init<S>(S, systemImage: String, isOn: Binding<Bool>)`

Creates a toggle that generates its label from a string and system image.

Available when `Label` is `Label<Text, Image>`.

`init<C>(LocalizedStringKey, systemImage: String, sources: C, isOn:
KeyPath<C.Element, Binding<Bool>>)`

Creates a toggle representing a collection of values that generates its label
from a localized string key and system image.

Available when `Label` is `Label<Text, Image>`.

Initializer

# init(_:)

Creates a toggle based on a toggle style configuration.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(_ configuration: ToggleStyleConfiguration)

Available when `Label` is `ToggleStyleConfiguration.Label`.

##  Parameters

`configuration`

    

The properties of the toggle, including a label and a binding to the toggle’s
state.

## Discussion

You can use this initializer within the `makeBody(configuration:)` method of a
`ToggleStyle` to create an instance of the styled toggle. This is useful for
custom toggle styles that only modify the current toggle style, as opposed to
implementing a brand new style.

For example, the following style adds a red border around the toggle, but
otherwise preserves the toggle’s current style:

Initializer

# init(isOn:intent:label:)

Creates a toggle performing an `AppIntent`.

AppIntents  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    init<I>(
        isOn: Bool,
        intent: I,
        @ViewBuilder label: () -> Label
    ) where I : AppIntent

Available when `Label` conforms to `View`.

##  Parameters

`isOn`

    

Whether the toggle is on or off.

`intent`

    

The `AppIntent` to be performed.

`label`

    

A view that describes the purpose of the toggle.

## See Also

### Creating a toggle for an App Intent

`init(LocalizedStringKey, isOn: Bool, intent: some AppIntent)`

Creates a toggle performing an `AppIntent` and generates its label from a
localized string key.

Available when `Label` is `Text`.

`init<S>(S, isOn: Bool, intent: some AppIntent)`

Creates a toggle that generates its label from a string.

Available when `Label` is `Text`.

Initializer

# init(_:isOn:intent:)

Creates a toggle performing an `AppIntent` and generates its label from a
localized string key.

AppIntents  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        isOn: Bool,
        intent: some AppIntent
    )

Available when `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the toggle’s localized title, that describes the purpose of the
toggle.

`isOn`

    

Whether the toggle is on or off.

`intent`

    

The `AppIntent` to be performed.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

To initialize a toggle with a string variable, use
`Toggle/init(_:isOn:intent:)` instead.

## See Also

### Creating a toggle for an App Intent

`init<I>(isOn: Bool, intent: I, label: () -> Label)`

Creates a toggle performing an `AppIntent`.

Available when `Label` conforms to `View`.

`init<S>(S, isOn: Bool, intent: some AppIntent)`

Creates a toggle that generates its label from a string.

Available when `Label` is `Text`.

Initializer

# init(_:isOn:intent:)

Creates a toggle that generates its label from a string.

AppIntents  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    init<S>(
        _ title: S,
        isOn: Bool,
        intent: some AppIntent
    ) where S : StringProtocol

Available when `Label` is `Text`.

##  Parameters

`title`

    

A string that describes the purpose of the toggle.

`isOn`

    

Whether the toggle is on or off.

`intent`

    

The `AppIntent` to be performed.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the title
similar to `init(_:)`. See `Text` for more information about localizing
strings.

To initialize a toggle with a localized string key, use
`Toggle/init(_:isOn:intent:)` instead.

## See Also

### Creating a toggle for an App Intent

`init<I>(isOn: Bool, intent: I, label: () -> Label)`

Creates a toggle performing an `AppIntent`.

Available when `Label` conforms to `View`.

`init(LocalizedStringKey, isOn: Bool, intent: some AppIntent)`

Creates a toggle performing an `AppIntent` and generates its label from a
localized string key.

Available when `Label` is `Text`.

