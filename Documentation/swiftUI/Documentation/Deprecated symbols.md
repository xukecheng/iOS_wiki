Initializer

# init(_:isActive:destination:)

Creates a navigation link that presents a destination view when active, with a
text label that the link generates from a localized string key.

iOS 13.0–16.0  Deprecated  iPadOS 13.0–16.0  Deprecated  macOS 10.15–13.0
Deprecated  Mac Catalyst 13.0–16.0  Deprecated  tvOS 13.0–16.0  Deprecated
watchOS 6.0–9.0  Deprecated  visionOS 1.0–1.0  Deprecated

    
    
    init(
        _ titleKey: LocalizedStringKey,
        isActive: Binding<Bool>,
        @ViewBuilder destination: () -> Destination
    )

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

Use `init(_:value:)` inside a `NavigationStack` or `NavigationSplitView`. For
more information, see Migrating to new navigation types.

##  Parameters

`titleKey`

    

A localized string key for creating a text label.

`isActive`

    

A binding to a Boolean value that indicates whether `destination` is currently
presented.

`destination`

    

A view for the navigation link to present.

## See Also

### Creating links with view builders

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

Initializer

# init(_:isActive:destination:)

Creates a navigation link that presents a destination view when active, with a
text label that the link generates from a title string.

iOS 13.0–16.0  Deprecated  iPadOS 13.0–16.0  Deprecated  macOS 10.15–13.0
Deprecated  Mac Catalyst 13.0–16.0  Deprecated  tvOS 13.0–16.0  Deprecated
watchOS 6.0–9.0  Deprecated  visionOS 1.0–1.0  Deprecated

    
    
    init<S>(
        _ title: S,
        isActive: Binding<Bool>,
        @ViewBuilder destination: () -> Destination
    ) where S : StringProtocol

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

Use `init(_:value:)` inside a `NavigationStack` or `NavigationSplitView`. For
more information, see Migrating to new navigation types.

##  Parameters

`title`

    

A string for creating a text label.

`isActive`

    

A binding to a Boolean value that indicates whether `destination` is currently
presented.

`destination`

    

A view for the navigation link to present.

## See Also

### Creating links with view builders

`init(LocalizedStringKey, isActive: Binding<Bool>, destination: () ->
Destination)`

Creates a navigation link that presents a destination view when active, with a
text label that the link generates from a localized string key.

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

Initializer

# init(isActive:destination:label:)

Creates a navigation link that presents the destination view when active.

iOS 13.0–16.0  Deprecated  iPadOS 13.0–16.0  Deprecated  macOS 10.15–13.0
Deprecated  Mac Catalyst 13.0–16.0  Deprecated  tvOS 13.0–16.0  Deprecated
watchOS 6.0–9.0  Deprecated  visionOS 1.0–1.0  Deprecated

    
    
    init(
        isActive: Binding<Bool>,
        @ViewBuilder destination: () -> Destination,
        @ViewBuilder label: () -> Label
    )

Deprecated

Use `init(value:label:)` inside a `NavigationStack` or `NavigationSplitView`.
For more information, see Migrating to new navigation types.

##  Parameters

`isActive`

    

A binding to a Boolean value that indicates whether `destination` is currently
presented.

`destination`

    

A view for the navigation link to present.

`label`

    

A view builder to produce a label describing the `destination` to present.

## See Also

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

Initializer

# init(_:tag:selection:destination:)

Creates a navigation link that presents a destination view when a bound
selection variable matches a value you provide, using a text label that the
link generates from a localized string key.

iOS 13.0–16.0  Deprecated  iPadOS 13.0–16.0  Deprecated  macOS 10.15–13.0
Deprecated  Mac Catalyst 13.0–16.0  Deprecated  tvOS 13.0–16.0  Deprecated
watchOS 6.0–9.0  Deprecated  visionOS 1.0–1.0  Deprecated

    
    
    init<V>(
        _ titleKey: LocalizedStringKey,
        tag: V,
        selection: Binding<V?>,
        @ViewBuilder destination: () -> Destination
    ) where V : Hashable

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

Use `init(_:value:)` inside a `List` within a `NavigationStack` or
`NavigationSplitView`. For more information, see Migrating to new navigation
types.

##  Parameters

`titleKey`

    

A localized string key for creating a text label.

`tag`

    

The value of `selection` that causes the link to present `destination`.

`selection`

    

A bound variable that causes the link to present `destination` when
`selection` becomes equal to `tag`.

`destination`

    

A view for the navigation link to present.

## See Also

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

Initializer

# init(_:tag:selection:destination:)

Creates a navigation link that presents a destination view when a bound
selection variable matches a value you provide, using a text label that the
link generates from a title string.

iOS 13.0–16.0  Deprecated  iPadOS 13.0–16.0  Deprecated  macOS 10.15–13.0
Deprecated  Mac Catalyst 13.0–16.0  Deprecated  tvOS 13.0–16.0  Deprecated
watchOS 6.0–9.0  Deprecated  visionOS 1.0–1.0  Deprecated

    
    
    init<S, V>(
        _ title: S,
        tag: V,
        selection: Binding<V?>,
        @ViewBuilder destination: () -> Destination
    ) where S : StringProtocol, V : Hashable

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

Use `init(_:value:)` inside a `List` within a `NavigationStack` or
`NavigationSplitView`. For more information, see Migrating to new navigation
types.

##  Parameters

`title`

    

A string for creating a text label.

`tag`

    

The value of `selection` that causes the link to present `destination`.

`selection`

    

A bound variable that causes the link to present `destination` when
`selection` becomes equal to `tag`.

`destination`

    

A view for the navigation link to present.

## See Also

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

`init<V>(tag: V, selection: Binding<V?>, destination: () -> Destination,
label: () -> Label)`

Creates a navigation link that presents the destination view when a bound
selection variable equals a given tag value.

Deprecated

Initializer

# init(tag:selection:destination:label:)

Creates a navigation link that presents the destination view when a bound
selection variable equals a given tag value.

iOS 13.0–16.0  Deprecated  iPadOS 13.0–16.0  Deprecated  macOS 10.15–13.0
Deprecated  Mac Catalyst 13.0–16.0  Deprecated  tvOS 13.0–16.0  Deprecated
watchOS 6.0–9.0  Deprecated  visionOS 1.0–1.0  Deprecated

    
    
    init<V>(
        tag: V,
        selection: Binding<V?>,
        @ViewBuilder destination: () -> Destination,
        @ViewBuilder label: () -> Label
    ) where V : Hashable

Deprecated

Use `init(value:label:)` inside a `List` within a `NavigationStack` or
`NavigationSplitView`. For more information, see Migrating to new navigation
types.

##  Parameters

`tag`

    

The value of `selection` that causes the link to present `destination`.

`selection`

    

A bound variable that causes the link to present `destination` when
`selection` becomes equal to `tag`.

`destination`

    

A view for the navigation link to present.

`label`

    

A view builder to produce a label describing the `destination` to present.

## See Also

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

Initializer

# init(destinationName:isActive:label:)

Creates a navigation link that presents a view from a WatchKit storyboard when
active.

watchOS 6.0–10.4  Deprecated

    
    
    init(
        destinationName: String,
        isActive: Binding<Bool>,
        @ViewBuilder label: () -> Label
    )

Available when `Label` conforms to `View` and `Destination` is
`_WKStoryboardContent`.

Deprecated

Use `init(value:label:)` instead. For more information, see Migrating to new
navigation types.

##  Parameters

`destinationName`

    

The storyboard name of a view for the navigation link to present.

`isActive`

    

A binding to a Boolean value that indicates whether `destination` is currently
presented.

`label`

    

A view builder to produce a label describing the `destination` to present.

## See Also

### Creating links for WatchKit

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

Initializer

# init(destinationName:tag:selection:label:)

Creates a navigation link that presents a view from a WatchKit storyboard when
a bound selection variable matches a value you provide.

watchOS 6.0–10.4  Deprecated

    
    
    init<V>(
        destinationName: String,
        tag: V,
        selection: Binding<V?>,
        @ViewBuilder label: () -> Label
    ) where V : Hashable

Available when `Label` conforms to `View` and `Destination` is
`_WKStoryboardContent`.

Deprecated

Use `init(value:label:)` inside a `List` within a `NavigationStack` or
`NavigationSplitView`. For more information, see Migrating to new navigation
types.

##  Parameters

`destinationName`

    

The storyboard name of a view for the navigation link to present.

`tag`

    

The value of `selection` that causes the link to present `destination`.

`selection`

    

A bound variable that causes the link to present `destination` when
`selection` becomes equal to `tag`.

`label`

    

A view builder to produce a label describing the `destination` to present.

## See Also

### Creating links for WatchKit

`init(destinationName: String, isActive: Binding<Bool>, label: () -> Label)`

Creates a navigation link that presents a view from a WatchKit storyboard when
active.

Available when `Label` conforms to `View` and `Destination` is
`_WKStoryboardContent`.

Deprecated

`init(destinationName: String, label: () -> Label)`

Creates a navigation link that presents a view from a WatchKit storyboard.

Available when `Label` conforms to `View` and `Destination` is
`_WKStoryboardContent`.

Deprecated

Initializer

# init(destinationName:label:)

Creates a navigation link that presents a view from a WatchKit storyboard.

watchOS 6.0–10.4  Deprecated

    
    
    init(
        destinationName: String,
        @ViewBuilder label: () -> Label
    )

Available when `Label` conforms to `View` and `Destination` is
`_WKStoryboardContent`.

Deprecated

Use `init(destination:label:)` instead.

##  Parameters

`destinationName`

    

The storyboard name of a view for the navigation link to present.

`label`

    

A view builder to produce a label describing the `destination` to present.

## See Also

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

Initializer

# init(_:destination:)

Creates a navigation link that presents a destination view, with a text label
that the link generates from a localized string key.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        destination: Destination
    )

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

Use `init(_:destination:)` instead.

##  Parameters

`titleKey`

    

A localized string key for creating a text label.

`destination`

    

A view for the navigation link to present.

## See Also

### Creating links with view arguments

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

Initializer

# init(_:destination:)

Creates a navigation link that presents a destination view, with a text label
that the link generates from a title string.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        destination: Destination
    ) where S : StringProtocol

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

Use `init(_:destination:)` instead.

##  Parameters

`title`

    

A string for creating a text label.

`destination`

    

A view for the navigation link to present.

## See Also

### Creating links with view arguments

`init(LocalizedStringKey, destination: Destination)`

Creates a navigation link that presents a destination view, with a text label
that the link generates from a localized string key.

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

Initializer

# init(destination:label:)

Creates a navigation link that presents the destination view.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    init(
        destination: Destination,
        @ViewBuilder label: () -> Label
    )

Deprecated

Use `init(destination:label:)` instead.

##  Parameters

`destination`

    

A view for the navigation link to present.

`label`

    

A view builder to produce a label describing the `destination` to present.

## See Also

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

Initializer

# init(_:destination:isActive:)

Creates a navigation link that presents a destination view when active, with a
text label that the link generates from a localized string key.

iOS 13.0–16.0  Deprecated  iPadOS 13.0–16.0  Deprecated  macOS 10.15–13.0
Deprecated  Mac Catalyst 13.0–16.0  Deprecated  tvOS 13.0–16.0  Deprecated
watchOS 6.0–9.0  Deprecated  visionOS 1.0–1.0  Deprecated

    
    
    init(
        _ titleKey: LocalizedStringKey,
        destination: Destination,
        isActive: Binding<Bool>
    )

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

Use `init(_:value:)` instead. For more information, see Migrating to new
navigation types.

##  Parameters

`titleKey`

    

A localized string key for creating a text label.

`destination`

    

A view for the navigation link to present.

`isActive`

    

A binding to a Boolean value that indicates whether `destination` is currently
presented.

## See Also

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

Initializer

# init(_:destination:isActive:)

Creates a navigation link that presents a destination view when active, with a
text label that the link generates from a title string.

iOS 13.0–16.0  Deprecated  iPadOS 13.0–16.0  Deprecated  macOS 10.15–13.0
Deprecated  Mac Catalyst 13.0–16.0  Deprecated  tvOS 13.0–16.0  Deprecated
watchOS 6.0–9.0  Deprecated  visionOS 1.0–1.0  Deprecated

    
    
    init<S>(
        _ title: S,
        destination: Destination,
        isActive: Binding<Bool>
    ) where S : StringProtocol

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

Use `init(_:value:)` instead. For more information, see Migrating to new
navigation types.

##  Parameters

`title`

    

A string for creating a text label.

`destination`

    

A view for the navigation link to present.

`isActive`

    

A binding to a Boolean value that indicates whether `destination` is currently
presented.

## See Also

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

Initializer

# init(destination:isActive:label:)

Creates a navigation link that presents the destination view when active.

iOS 13.0–16.0  Deprecated  iPadOS 13.0–16.0  Deprecated  macOS 10.15–13.0
Deprecated  Mac Catalyst 13.0–16.0  Deprecated  tvOS 13.0–16.0  Deprecated
watchOS 6.0–9.0  Deprecated  visionOS 1.0–1.0  Deprecated

    
    
    init(
        destination: Destination,
        isActive: Binding<Bool>,
        @ViewBuilder label: () -> Label
    )

Deprecated

Use `init(value:label:)` instead. For more information, see Migrating to new
navigation types.

##  Parameters

`destination`

    

A view for the navigation link to present.

`isActive`

    

A binding to a Boolean value that indicates whether `destination` is currently
presented.

`label`

    

A view builder to produce a label describing the `destination` to present.

## See Also

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

Initializer

# init(_:destination:tag:selection:)

Creates a navigation link that presents a destination view when a bound
selection variable matches a value you provide, using a text label that the
link generates from a localized string key.

iOS 13.0–16.0  Deprecated  iPadOS 13.0–16.0  Deprecated  macOS 10.15–13.0
Deprecated  Mac Catalyst 13.0–16.0  Deprecated  tvOS 13.0–16.0  Deprecated
watchOS 6.0–9.0  Deprecated  visionOS 1.0–1.0  Deprecated

    
    
    init<V>(
        _ titleKey: LocalizedStringKey,
        destination: Destination,
        tag: V,
        selection: Binding<V?>
    ) where V : Hashable

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

Use `init(_:value:)` inside a `List` within a `NavigationStack` or
`NavigationSplitView`. For more information, see Migrating to new navigation
types.

##  Parameters

`titleKey`

    

A localized string key for creating a text label.

`destination`

    

A view for the navigation link to present.

`tag`

    

The value of `selection` that causes the link to present `destination`.

`selection`

    

A bound variable that causes the link to present `destination` when
`selection` becomes equal to `tag`.

## See Also

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

Initializer

# init(_:destination:tag:selection:)

Creates a navigation link that presents a destination view when a bound
selection variable matches a value you provide, using a text label that the
link generates from a title string.

iOS 13.0–16.0  Deprecated  iPadOS 13.0–16.0  Deprecated  macOS 10.15–13.0
Deprecated  Mac Catalyst 13.0–16.0  Deprecated  tvOS 13.0–16.0  Deprecated
watchOS 6.0–9.0  Deprecated  visionOS 1.0–1.0  Deprecated

    
    
    init<S, V>(
        _ title: S,
        destination: Destination,
        tag: V,
        selection: Binding<V?>
    ) where S : StringProtocol, V : Hashable

Available when `Label` is `Text` and `Destination` conforms to `View`.

Deprecated

Use `init(_:value:)` inside a `List` within a `NavigationStack` or
`NavigationSplitView`. For more information, see Migrating to new navigation
types.

##  Parameters

`title`

    

A string for creating a text label.

`destination`

    

A view for the navigation link to present.

`tag`

    

The value of `selection` that causes the link to present `destination`.

`selection`

    

A bound variable that causes the link to present `destination` when
`selection` becomes equal to `tag`.

## See Also

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

`init<V>(destination: Destination, tag: V, selection: Binding<V?>, label: ()
-> Label)`

Creates a navigation link that presents the destination view when a bound
selection variable equals a given tag value.

Deprecated

Initializer

# init(destination:tag:selection:label:)

Creates a navigation link that presents the destination view when a bound
selection variable equals a given tag value.

iOS 13.0–16.0  Deprecated  iPadOS 13.0–16.0  Deprecated  macOS 10.15–13.0
Deprecated  Mac Catalyst 13.0–16.0  Deprecated  tvOS 13.0–16.0  Deprecated
watchOS 6.0–9.0  Deprecated  visionOS 1.0–1.0  Deprecated

    
    
    init<V>(
        destination: Destination,
        tag: V,
        selection: Binding<V?>,
        @ViewBuilder label: () -> Label
    ) where V : Hashable

Deprecated

Use `init(value:label:)` inside a `List` within a `NavigationStack` or
`NavigationSplitView`. For more information, see Migrating to new navigation
types.

##  Parameters

`destination`

    

A view for the navigation link to present.

`tag`

    

The value of `selection` that causes the link to present `destination`.

`selection`

    

A bound variable that causes the link to present `destination` when
`selection` becomes equal to `tag`.

`label`

    

A view builder to produce a label describing the `destination` to present.

## See Also

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

