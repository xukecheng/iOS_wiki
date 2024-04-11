Instance Method

# preference(key:value:)

Sets a value for the given preference.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func preference<K>(
        key: K.Type = K.self,
        value: K.Value
    ) -> some View where K : PreferenceKey
    

## See Also

### Setting preferences

`func transformPreference<K>(K.Type, (inout K.Value) -> Void) -> some View`

Applies a transformation to a preference value.

Instance Method

# transformPreference(_:_:)

Applies a transformation to a preference value.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func transformPreference<K>(
        _ key: K.Type = K.self,
        _ callback: @escaping (inout K.Value) -> Void
    ) -> some View where K : PreferenceKey
    

## See Also

### Setting preferences

`func preference<K>(key: K.Type, value: K.Value) -> some View`

Sets a value for the given preference.

Protocol

# PreferenceKey

A named value produced by a view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    protocol PreferenceKey

## Overview

A view with multiple children automatically combines its values for a given
preference into a single value visible to its ancestors.

## Topics

### Getting the default value

`static var defaultValue: Self.Value`

The default value of the preference.

**Required** Default implementation provided.

`associatedtype Value`

The type of value produced by this preference.

**Required**

### Combining preferences

`static func reduce(value: inout Self.Value, nextValue: () -> Self.Value)`

Combines a sequence of values by modifying the previously-accumulated value
with the result of a closure that provides the next value.

**Required**

## Relationships

### Conforming Types

  * `PreferredColorSchemeKey`

Instance Method

# anchorPreference(key:value:transform:)

Sets a value for the specified preference key, the value is a function of a
geometry value tied to the current coordinate space, allowing readers of the
value to convert the geometry to their local coordinates.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func anchorPreference<A, K>(
        key _: K.Type = K.self,
        value: Anchor<A>.Source,
        transform: @escaping (Anchor<A>) -> K.Value
    ) -> some View where K : PreferenceKey
    

##  Parameters

`key`

    

the preference key type.

`value`

    

the geometry value in the current coordinate space.

`transform`

    

the function to produce the preference value.

## Return Value

a new version of the view that writes the preference.

## See Also

### Setting preferences based on geometry

`func transformAnchorPreference<A, K>(key: K.Type, value: Anchor<A>.Source,
transform: (inout K.Value, Anchor<A>) -> Void) -> some View`

Sets a value for the specified preference key, the value is a function of the
key’s current value and a geometry value tied to the current coordinate space,
allowing readers of the value to convert the geometry to their local
coordinates.

Instance Method

# transformAnchorPreference(key:value:transform:)

Sets a value for the specified preference key, the value is a function of the
key’s current value and a geometry value tied to the current coordinate space,
allowing readers of the value to convert the geometry to their local
coordinates.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func transformAnchorPreference<A, K>(
        key _: K.Type = K.self,
        value: Anchor<A>.Source,
        transform: @escaping (inout K.Value, Anchor<A>) -> Void
    ) -> some View where K : PreferenceKey
    

##  Parameters

`key`

    

the preference key type.

`value`

    

the geometry value in the current coordinate space.

`transform`

    

the function to produce the preference value.

## Return Value

a new version of the view that writes the preference.

## See Also

### Setting preferences based on geometry

`func anchorPreference<A, K>(key: K.Type, value: Anchor<A>.Source, transform:
(Anchor<A>) -> K.Value) -> some View`

Sets a value for the specified preference key, the value is a function of a
geometry value tied to the current coordinate space, allowing readers of the
value to convert the geometry to their local coordinates.

Instance Method

# onPreferenceChange(_:perform:)

Adds an action to perform when the specified preference key’s value changes.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func onPreferenceChange<K>(
        _ key: K.Type = K.self,
        perform action: @escaping (K.Value) -> Void
    ) -> some View where K : PreferenceKey, K.Value : Equatable
    

##  Parameters

`key`

    

The key to monitor for value changes.

`action`

    

The action to perform when the value for `key` changes. The `action` closure
passes the new value as its parameter.

## Return Value

A view that triggers `action` when the value for `key` changes.

Instance Method

# backgroundPreferenceValue(_:_:)

Reads the specified preference value from the view, using it to produce a
second view that is applied as the background of the original view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func backgroundPreferenceValue<Key, T>(
        _ key: Key.Type = Key.self,
        @ViewBuilder _ transform: @escaping (Key.Value) -> T
    ) -> some View where Key : PreferenceKey, T : View
    

##  Parameters

`key`

    

The preference key type whose value is to be read.

`transform`

    

A function that produces the background view from the preference value read
from the original view.

## Return Value

A view that layers a second view behind the view.

## See Also

### Generating backgrounds and overlays from preferences

`func backgroundPreferenceValue<K, V>(K.Type, alignment: Alignment, (K.Value)
-> V) -> some View`

Reads the specified preference value from the view, using it to produce a
second view that is applied as the background of the original view.

`func overlayPreferenceValue<Key, T>(Key.Type, (Key.Value) -> T) -> some View`

Reads the specified preference value from the view, using it to produce a
second view that is applied as an overlay to the original view.

`func overlayPreferenceValue<K, V>(K.Type, alignment: Alignment, (K.Value) ->
V) -> some View`

Reads the specified preference value from the view, using it to produce a
second view that is applied as an overlay to the original view.

Instance Method

# backgroundPreferenceValue(_:alignment:_:)

Reads the specified preference value from the view, using it to produce a
second view that is applied as the background of the original view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func backgroundPreferenceValue<K, V>(
        _ key: K.Type,
        alignment: Alignment = .center,
        @ViewBuilder _ transform: @escaping (K.Value) -> V
    ) -> some View where K : PreferenceKey, V : View
    

##  Parameters

`key`

    

The preference key type whose value is to be read.

`alignment`

    

An optional alignment to use when positioning the background view relative to
the original view.

`transform`

    

A function that produces the background view from the preference value read
from the original view.

## Return Value

A view that layers a second view behind the view.

## Discussion

The values of the preference key from both views are combined and made visible
to the parent view.

## See Also

### Generating backgrounds and overlays from preferences

`func backgroundPreferenceValue<Key, T>(Key.Type, (Key.Value) -> T) -> some
View`

Reads the specified preference value from the view, using it to produce a
second view that is applied as the background of the original view.

`func overlayPreferenceValue<Key, T>(Key.Type, (Key.Value) -> T) -> some View`

Reads the specified preference value from the view, using it to produce a
second view that is applied as an overlay to the original view.

`func overlayPreferenceValue<K, V>(K.Type, alignment: Alignment, (K.Value) ->
V) -> some View`

Reads the specified preference value from the view, using it to produce a
second view that is applied as an overlay to the original view.

Instance Method

# overlayPreferenceValue(_:_:)

Reads the specified preference value from the view, using it to produce a
second view that is applied as an overlay to the original view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func overlayPreferenceValue<Key, T>(
        _ key: Key.Type = Key.self,
        @ViewBuilder _ transform: @escaping (Key.Value) -> T
    ) -> some View where Key : PreferenceKey, T : View
    

##  Parameters

`key`

    

The preference key type whose value is to be read.

`transform`

    

A function that produces the overlay view from the preference value read from
the original view.

## Return Value

A view that layers a second view in front of the view.

## See Also

### Generating backgrounds and overlays from preferences

`func backgroundPreferenceValue<Key, T>(Key.Type, (Key.Value) -> T) -> some
View`

Reads the specified preference value from the view, using it to produce a
second view that is applied as the background of the original view.

`func backgroundPreferenceValue<K, V>(K.Type, alignment: Alignment, (K.Value)
-> V) -> some View`

Reads the specified preference value from the view, using it to produce a
second view that is applied as the background of the original view.

`func overlayPreferenceValue<K, V>(K.Type, alignment: Alignment, (K.Value) ->
V) -> some View`

Reads the specified preference value from the view, using it to produce a
second view that is applied as an overlay to the original view.

Instance Method

# overlayPreferenceValue(_:alignment:_:)

Reads the specified preference value from the view, using it to produce a
second view that is applied as an overlay to the original view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func overlayPreferenceValue<K, V>(
        _ key: K.Type,
        alignment: Alignment = .center,
        @ViewBuilder _ transform: @escaping (K.Value) -> V
    ) -> some View where K : PreferenceKey, V : View
    

##  Parameters

`key`

    

The preference key type whose value is to be read.

`alignment`

    

An optional alignment to use when positioning the overlay view relative to the
original view.

`transform`

    

A function that produces the overlay view from the preference value read from
the original view.

## Return Value

A view that layers a second view in front of the view.

## Discussion

The values of the preference key from both views are combined and made visible
to the parent view.

## See Also

### Generating backgrounds and overlays from preferences

`func backgroundPreferenceValue<Key, T>(Key.Type, (Key.Value) -> T) -> some
View`

Reads the specified preference value from the view, using it to produce a
second view that is applied as the background of the original view.

`func backgroundPreferenceValue<K, V>(K.Type, alignment: Alignment, (K.Value)
-> V) -> some View`

Reads the specified preference value from the view, using it to produce a
second view that is applied as the background of the original view.

`func overlayPreferenceValue<Key, T>(Key.Type, (Key.Value) -> T) -> some View`

Reads the specified preference value from the view, using it to produce a
second view that is applied as an overlay to the original view.

