Initializer

# init(_:destination:)

Creates a navigation link that presents a destination view, with a text label
that the link generates from a localized string key.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        @ViewBuilder destination: () -> Destination
    )

Available when `Label` is `Text` and `Destination` conforms to `View`.

##  Parameters

`titleKey`

    

A localized string key for creating a text label.

`destination`

    

A view for the navigation link to present.

## See Also

### Presenting a destination view

`init<S>(S, destination: () -> Destination)`

Creates a navigation link that presents a destination view, with a text label
that the link generates from a title string.

Available when `Label` is `Text` and `Destination` conforms to `View`.

`init(destination: () -> Destination, label: () -> Label)`

Creates a navigation link that presents the destination view.

Initializer

# init(_:destination:)

Creates a navigation link that presents a destination view, with a text label
that the link generates from a title string.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        @ViewBuilder destination: () -> Destination
    ) where S : StringProtocol

Available when `Label` is `Text` and `Destination` conforms to `View`.

##  Parameters

`title`

    

A string for creating a text label.

`destination`

    

A view for the navigation link to present.

## See Also

### Presenting a destination view

`init(LocalizedStringKey, destination: () -> Destination)`

Creates a navigation link that presents a destination view, with a text label
that the link generates from a localized string key.

Available when `Label` is `Text` and `Destination` conforms to `View`.

`init(destination: () -> Destination, label: () -> Label)`

Creates a navigation link that presents the destination view.

Initializer

# init(destination:label:)

Creates a navigation link that presents the destination view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        @ViewBuilder destination: () -> Destination,
        @ViewBuilder label: () -> Label
    )

##  Parameters

`destination`

    

A view for the navigation link to present.

`label`

    

A view builder to produce a label describing the `destination` to present.

## See Also

### Presenting a destination view

`init(LocalizedStringKey, destination: () -> Destination)`

Creates a navigation link that presents a destination view, with a text label
that the link generates from a localized string key.

Available when `Label` is `Text` and `Destination` conforms to `View`.

`init<S>(S, destination: () -> Destination)`

Creates a navigation link that presents a destination view, with a text label
that the link generates from a title string.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Initializer

# init(_:value:)

Creates a navigation link that presents the view corresponding to a value,
with a text label that the link generates from a localized string key.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init<P>(
        _ titleKey: LocalizedStringKey,
        value: P?
    ) where Label == Text, P : Hashable

Available when `Label` conforms to `View` and `Destination` is `Never`.

##  Parameters

`titleKey`

    

A localized string that describes the view that this link presents.

`value`

    

An optional value to present. When the user selects the link, SwiftUI stores a
copy of the value. Pass a `nil` value to disable the link.

## Discussion

When someone activates the navigation link that this initializer creates,
SwiftUI looks for a nearby `navigationDestination(for:destination:)` view
modifier with a `data` input parameter that matches the type of this
initializer’s `value` input, with one of the following outcomes:

  * If SwiftUI finds a matching modifier within the view hierarchy of an enclosing `NavigationStack`, it pushes the modifier’s corresponding `destination` view onto the stack.

  * If SwiftUI finds a matching modifier in the view hierarchy of a stack that’s in a later column of a `NavigationSplitView`, it puts the modifier’s destination view as the first and only item onto the stack while preserving the stack’s root view.

  * If there’s no matching modifier, but the link appears in a `List` with selection inside a leading column of a navigation split view, the link updates the selection, which might affect the appearance of a trailing view. For an example of this, see `NavigationLink`.

  * In other cases, the link doesn’t do anything.

If you want to be able to serialize a `NavigationPath` that includes this
link, use use a `value` that conforms to the `Codable` protocol.

## See Also

### Presenting a data value

`init<S, P>(S, value: P?)`

Creates a navigation link that presents the view corresponding to a value,
with a text label that the link generates from a title string.

Available when `Label` conforms to `View` and `Destination` is `Never`.

`init<P>(value: P?, label: () -> Label)`

Creates a navigation link that presents the view corresponding to a value.

Available when `Label` conforms to `View` and `Destination` is `Never`.

Initializer

# init(_:value:)

Creates a navigation link that presents the view corresponding to a value,
with a text label that the link generates from a title string.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init<S, P>(
        _ title: S,
        value: P?
    ) where Label == Text, S : StringProtocol, P : Hashable

Available when `Label` conforms to `View` and `Destination` is `Never`.

##  Parameters

`title`

    

A string that describes the view that this link presents.

`value`

    

An optional value to present. When the user selects the link, SwiftUI stores a
copy of the value. Pass a `nil` value to disable the link.

## Discussion

When someone activates the navigation link that this initializer creates,
SwiftUI looks for a nearby `navigationDestination(for:destination:)` view
modifier with a `data` input parameter that matches the type of this
initializer’s `value` input, with one of the following outcomes:

  * If SwiftUI finds a matching modifier within the view hierarchy of an enclosing `NavigationStack`, it pushes the modifier’s corresponding `destination` view onto the stack.

  * If SwiftUI finds a matching modifier in the view hierarchy of a stack that’s in a later column of a `NavigationSplitView`, it puts the modifier’s destination view as the first and only item onto the stack while preserving the stack’s root view.

  * If there’s no matching modifier, but the link appears in a `List` with selection inside a leading column of a navigation split view, the link updates the selection, which might affect the appearance of a trailing view. For an example of this, see `NavigationLink`.

  * In other cases, the link doesn’t do anything.

If you want to be able to serialize a `NavigationPath` that includes this
link, use use a `value` that conforms to the `Codable` protocol.

## See Also

### Presenting a data value

`init<P>(LocalizedStringKey, value: P?)`

Creates a navigation link that presents the view corresponding to a value,
with a text label that the link generates from a localized string key.

Available when `Label` conforms to `View` and `Destination` is `Never`.

`init<P>(value: P?, label: () -> Label)`

Creates a navigation link that presents the view corresponding to a value.

Available when `Label` conforms to `View` and `Destination` is `Never`.

Initializer

# init(value:label:)

Creates a navigation link that presents the view corresponding to a value.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init<P>(
        value: P?,
        @ViewBuilder label: () -> Label
    ) where P : Hashable

Available when `Label` conforms to `View` and `Destination` is `Never`.

##  Parameters

`value`

    

An optional value to present. When the user selects the link, SwiftUI stores a
copy of the value. Pass a `nil` value to disable the link.

`label`

    

A label that describes the view that this link presents.

## Discussion

When someone activates the navigation link that this initializer creates,
SwiftUI looks for a nearby `navigationDestination(for:destination:)` view
modifier with a `data` input parameter that matches the type of this
initializer’s `value` input, with one of the following outcomes:

  * If SwiftUI finds a matching modifier within the view hierarchy of an enclosing `NavigationStack`, it pushes the modifier’s corresponding `destination` view onto the stack.

  * If SwiftUI finds a matching modifier in the view hierarchy of a stack that’s in a later column of a `NavigationSplitView`, it puts the modifier’s destination view as the first and only item onto the stack while preserving the stack’s root view.

  * If there’s no matching modifier, but the link appears in a `List` with selection inside a leading column of a navigation split view, the link updates the selection, which might affect the appearance of a trailing view. For an example of this, see `NavigationLink`.

  * In other cases, the link doesn’t do anything.

If you want to be able to serialize a `NavigationPath` that includes this
link, use use a `value` that conforms to the `Codable` protocol.

## See Also

### Presenting a data value

`init<P>(LocalizedStringKey, value: P?)`

Creates a navigation link that presents the view corresponding to a value,
with a text label that the link generates from a localized string key.

Available when `Label` conforms to `View` and `Destination` is `Never`.

`init<S, P>(S, value: P?)`

Creates a navigation link that presents the view corresponding to a value,
with a text label that the link generates from a title string.

Available when `Label` conforms to `View` and `Destination` is `Never`.

Initializer

# init(_:value:)

Creates a navigation link that presents the view corresponding to a codable
value, with a text label that the link generates from a localized string key.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init<P>(
        _ titleKey: LocalizedStringKey,
        value: P?
    ) where Label == Text, P : Decodable, P : Encodable, P : Hashable

Available when `Label` conforms to `View` and `Destination` is `Never`.

##  Parameters

`titleKey`

    

A localized string that describes the view that this link presents.

`value`

    

An optional value to present. When someone taps or clicks the link, SwiftUI
stores a copy of the value. Pass a `nil` value to disable the link.

## Discussion

When someone activates the navigation link that this initializer creates,
SwiftUI looks for a nearby `navigationDestination(for:destination:)` view
modifier with a `data` input parameter that matches the type of this
initializer’s `value` input, with one of the following outcomes:

  * If SwiftUI finds a matching modifier within the view hierarchy of an enclosing `NavigationStack`, it pushes the modifier’s corresponding `destination` view onto the stack.

  * If SwiftUI finds a matching modifier in the view hierarchy of a stack that’s in a later column of a `NavigationSplitView`, it puts the modifier’s destination view as the first and only item onto the stack while preserving the stack’s root view.

  * If there’s no matching modifier, but the link appears in a `List` with selection inside a leading column of a navigation split view, the link updates the selection, which might affect the appearance of a trailing view. For an example of this, see `NavigationLink`.

  * In other cases, the link doesn’t do anything.

Because this initializer takes a value that conforms to the `Codable`
protocol, you ensure that a `NavigationPath` that includes this link can
produce a non-`nil` value for its `codable` property. This helps to make the
path serializable.

## See Also

### Presenting a codable value

`init<S, P>(S, value: P?)`

Creates a navigation link that presents the view corresponding to a codable
value, with a text label that the link generates from a title string.

Available when `Label` conforms to `View` and `Destination` is `Never`.

`init<P>(value: P?, label: () -> Label)`

Creates a navigation link that presents the view corresponding to a codable
value.

Available when `Label` conforms to `View` and `Destination` is `Never`.

Initializer

# init(_:value:)

Creates a navigation link that presents the view corresponding to a codable
value, with a text label that the link generates from a title string.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init<S, P>(
        _ title: S,
        value: P?
    ) where Label == Text, S : StringProtocol, P : Decodable, P : Encodable, P : Hashable

Available when `Label` conforms to `View` and `Destination` is `Never`.

##  Parameters

`title`

    

A string that describes the view that this link presents.

`value`

    

An optional value to present. When the user selects the link, SwiftUI stores a
copy of the value. Pass a `nil` value to disable the link.

## Discussion

When someone activates the navigation link that this initializer creates,
SwiftUI looks for a nearby `navigationDestination(for:destination:)` view
modifier with a `data` input parameter that matches the type of this
initializer’s `value` input, with one of the following outcomes:

  * If SwiftUI finds a matching modifier within the view hierarchy of an enclosing `NavigationStack`, it pushes the modifier’s corresponding `destination` view onto the stack.

  * If SwiftUI finds a matching modifier in the view hierarchy of a stack that’s in a later column of a `NavigationSplitView`, it puts the modifier’s destination view as the first and only item onto the stack while preserving the stack’s root view.

  * If there’s no matching modifier, but the link appears in a `List` with selection inside a leading column of a navigation split view, the link updates the selection, which might affect the appearance of a trailing view. For an example of this, see `NavigationLink`.

  * In other cases, the link doesn’t do anything.

Because this initializer takes a value that conforms to the `Codable`
protocol, you ensure that a `NavigationPath` that includes this link can
produce a non-`nil` value for its `codable` property. This helps to make the
path serializable.

## See Also

### Presenting a codable value

`init<P>(LocalizedStringKey, value: P?)`

Creates a navigation link that presents the view corresponding to a codable
value, with a text label that the link generates from a localized string key.

Available when `Label` conforms to `View` and `Destination` is `Never`.

`init<P>(value: P?, label: () -> Label)`

Creates a navigation link that presents the view corresponding to a codable
value.

Available when `Label` conforms to `View` and `Destination` is `Never`.

Initializer

# init(value:label:)

Creates a navigation link that presents the view corresponding to a codable
value.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init<P>(
        value: P?,
        @ViewBuilder label: () -> Label
    ) where P : Decodable, P : Encodable, P : Hashable

Available when `Label` conforms to `View` and `Destination` is `Never`.

##  Parameters

`value`

    

An optional value to present. When the user selects the link, SwiftUI stores a
copy of the value. Pass a `nil` value to disable the link.

`label`

    

A label that describes the view that this link presents.

## Discussion

When someone activates the navigation link that this initializer creates,
SwiftUI looks for a nearby `navigationDestination(for:destination:)` view
modifier with a `data` input parameter that matches the type of this
initializer’s `value` input, with one of the following outcomes:

  * If SwiftUI finds a matching modifier within the view hierarchy of an enclosing `NavigationStack`, it pushes the modifier’s corresponding `destination` view onto the stack.

  * If SwiftUI finds a matching modifier in the view hierarchy of a stack that’s in a later column of a `NavigationSplitView`, it puts the modifier’s destination view as the first and only item onto the stack while preserving the stack’s root view.

  * If there’s no matching modifier, but the link appears in a `List` with selection inside a leading column of a navigation split view, the link updates the selection, which might affect the appearance of a trailing view. For an example of this, see `NavigationLink`.

  * In other cases, the link doesn’t do anything.

Because this initializer takes a value that conforms to the `Codable`
protocol, you ensure that a `NavigationPath` that includes this link can
produce a non-`nil` value for its `codable` property. This helps to make the
path serializable.

## See Also

### Presenting a codable value

`init<P>(LocalizedStringKey, value: P?)`

Creates a navigation link that presents the view corresponding to a codable
value, with a text label that the link generates from a localized string key.

Available when `Label` conforms to `View` and `Destination` is `Never`.

`init<S, P>(S, value: P?)`

Creates a navigation link that presents the view corresponding to a codable
value, with a text label that the link generates from a title string.

Available when `Label` conforms to `View` and `Destination` is `Never`.

Instance Method

# isDetailLink(_:)

Sets the navigation link to present its destination as the detail component of
the containing navigation view.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  visionOS 1.0+

    
    
    func isDetailLink(_ isDetailLink: Bool) -> some View
    

Available when `Label` conforms to `View` and `Destination` conforms to
`View`.

##  Parameters

`isDetailLink`

    

A Boolean value that specifies whether this link presents its destination as
the detail component when used in a multi-column navigation view.

## Return Value

A view that applies the specified detail link behavior.

## Discussion

This method sets the behavior when the navigation link is used in a
`NavigationSplitView`, or a multi-column navigation view, such as one using
`ColumnNavigationViewStyle`.

For example, in a two-column navigation split view, if `isDetailLink` is
`true`, triggering the link in the sidebar column sets the contents of the
detail column to be the link’s destination view. If `isDetailLink` is `false`,
the link navigates to the destination view within the primary column.

If you do not set the detail link behavior with this method, the behavior
defaults to `true`.

The `isDetailLink` modifier only affects view-destination links. Links that
present data values always search for a matching navigation destination
beginning in the column that contains the link.

Collection

API Collection

# Deprecated symbols

Review deprecated navigation link initializers.

## Overview

For information about updating your use of navigation symbols, see Migrating
to new navigation types.

## Topics

### Creating links with view builders

`init(LocalizedStringKey, isActive: Binding<Bool>, destination: () ->
Destination)`

Creates a navigation link that presents a destination view when active, with a
text label that the link generates from a localized string key.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init<S>(S, isActive: Binding<Bool>, destination: () -> Destination)`

Creates a navigation link that presents a destination view when active, with a
text label that the link generates from a title string.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init(isActive: Binding<Bool>, destination: () -> Destination, label: () ->
Label)`

Creates a navigation link that presents the destination view when active.

Deprecated

`init<V>(LocalizedStringKey, tag: V, selection: Binding<V?>, destination: ()
-> Destination)`

Creates a navigation link that presents a destination view when a bound
selection variable matches a value you provide, using a text label that the
link generates from a localized string key.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init<S, V>(S, tag: V, selection: Binding<V?>, destination: () ->
Destination)`

Creates a navigation link that presents a destination view when a bound
selection variable matches a value you provide, using a text label that the
link generates from a title string.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init<V>(tag: V, selection: Binding<V?>, destination: () -> Destination,
label: () -> Label)`

Creates a navigation link that presents the destination view when a bound
selection variable equals a given tag value.

Deprecated

### Creating links for WatchKit

`init(destinationName: String, isActive: Binding<Bool>, label: () -> Label)`

Creates a navigation link that presents a view from a WatchKit storyboard when
active.

Available when `Label` conforms to `View` and `Destination` is
`_WKStoryboardContent`.

Deprecated

`init<V>(destinationName: String, tag: V, selection: Binding<V?>, label: () ->
Label)`

Creates a navigation link that presents a view from a WatchKit storyboard when
a bound selection variable matches a value you provide.

Available when `Label` conforms to `View` and `Destination` is
`_WKStoryboardContent`.

Deprecated

`init(destinationName: String, label: () -> Label)`

Creates a navigation link that presents a view from a WatchKit storyboard.

Available when `Label` conforms to `View` and `Destination` is
`_WKStoryboardContent`.

Deprecated

### Creating links with view arguments

`init(LocalizedStringKey, destination: Destination)`

Creates a navigation link that presents a destination view, with a text label
that the link generates from a localized string key.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init<S>(S, destination: Destination)`

Creates a navigation link that presents a destination view, with a text label
that the link generates from a title string.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init(destination: Destination, label: () -> Label)`

Creates a navigation link that presents the destination view.

Deprecated

`init(LocalizedStringKey, destination: Destination, isActive: Binding<Bool>)`

Creates a navigation link that presents a destination view when active, with a
text label that the link generates from a localized string key.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init<S>(S, destination: Destination, isActive: Binding<Bool>)`

Creates a navigation link that presents a destination view when active, with a
text label that the link generates from a title string.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init(destination: Destination, isActive: Binding<Bool>, label: () -> Label)`

Creates a navigation link that presents the destination view when active.

Deprecated

`init<V>(LocalizedStringKey, destination: Destination, tag: V, selection:
Binding<V?>)`

Creates a navigation link that presents a destination view when a bound
selection variable matches a value you provide, using a text label that the
link generates from a localized string key.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init<S, V>(S, destination: Destination, tag: V, selection: Binding<V?>)`

Creates a navigation link that presents a destination view when a bound
selection variable matches a value you provide, using a text label that the
link generates from a title string.

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

`init<V>(destination: Destination, tag: V, selection: Binding<V?>, label: ()
-> Label)`

Creates a navigation link that presents the destination view when a bound
selection variable equals a given tag value.

Deprecated

