Instance Method

# tag(_:)

Sets the unique tag value of this view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func tag<V>(_ tag: V) -> some View where V : Hashable
    

##  Parameters

`tag`

    

A `Hashable` value to use as the view’s tag.

## Return Value

A view with the specified tag set.

## Discussion

Use this modifier to differentiate among certain selectable views, like the
possible values of a `Picker` or the tabs of a `TabView`. Tag values can be of
any type that conforms to the `Hashable` protocol.

In the example below, the `ForEach` loop in the `Picker` view builder iterates
over the `Flavor` enumeration. It extracts the string value of each
enumeration element for use in constructing the row label, and uses the
enumeration value, cast as an optional, as input to the `tag(_:)` modifier.
The `Picker` requires the tags to have a type that exactly matches the
selection type, which in this case is an optional `Flavor`.

If you change `selectedFlavor` to be non-optional, you need to remove the
`Optional` cast from the tag input to match.

A `ForEach` automatically applies a default tag to each enumerated view using
the `id` parameter of the corresponding element. If the element’s `id`
parameter and the picker’s `selection` input have exactly the same type, you
can omit the explicit tag modifier. To see examples that don’t require an
explicit tag, see `Picker`.

## See Also

### Managing the view hierarchy

`func id<ID>(ID) -> some View`

Binds a view’s identity to the given proxy value.

`func equatable() -> EquatableView<Self>`

Prevents the view from updating its child view when its new value is the same
as its old value.

Available when `Self` conforms to `Equatable`.

Instance Method

# id(_:)

Binds a view’s identity to the given proxy value.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func id<ID>(_ id: ID) -> some View where ID : Hashable
    

## Discussion

When the proxy value specified by the `id` parameter changes, the identity of
the view — for example, its state — is reset.

## See Also

### Managing the view hierarchy

`func tag<V>(V) -> some View`

Sets the unique tag value of this view.

`func equatable() -> EquatableView<Self>`

Prevents the view from updating its child view when its new value is the same
as its old value.

Available when `Self` conforms to `Equatable`.

Instance Method

# equatable()

Prevents the view from updating its child view when its new value is the same
as its old value.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func equatable() -> EquatableView<Self>

Available when `Self` conforms to `Equatable`.

## See Also

### Managing the view hierarchy

`func id<ID>(ID) -> some View`

Binds a view’s identity to the given proxy value.

`func tag<V>(V) -> some View`

Sets the unique tag value of this view.

Instance Method

# environment(_:)

Places an observable object in the view’s environment.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func environment<T>(_ object: T?) -> some View where T : AnyObject, T : Observable
    

##  Parameters

`object`

    

The object to set for this object’s type in the environment, or `nil` to clear
an object of this type from the environment.

## Return Value

A view that has the specified object in its environment.

## Discussion

Use this modifier to place an object that you declare with the `Observable()`
macro into a view’s environment. For example, you can add an instance of a
custom observable `Profile` class to the environment of a `ContentView`:

You then read the object inside `ContentView` or one of its descendants using
the `Environment` property wrapper:

This modifier affects the given view, as well as that view’s descendant views.
It has no effect outside the view hierarchy on which you call it. The
environment of a given view hierarchy holds only one observable object of a
given type.

Note

This modifier takes an object that conforms to the `Observable` protocol. To
add environment objects that conform to the `ObservableObject` protocol, use
`environmentObject(_:)` instead.

## See Also

### Modifying the environment of a view

`func environment<V>(WritableKeyPath<EnvironmentValues, V>, V) -> some View`

Sets the environment value of the specified key path to the given value.

`func transformEnvironment<V>(WritableKeyPath<EnvironmentValues, V>,
transform: (inout V) -> Void) -> some View`

Transforms the environment value of the specified key path with the given
function.

Instance Method

# environment(_:_:)

Sets the environment value of the specified key path to the given value.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func environment<V>(
        _ keyPath: WritableKeyPath<EnvironmentValues, V>,
        _ value: V
    ) -> some View
    

##  Parameters

`keyPath`

    

A key path that indicates the property of the `EnvironmentValues` structure to
update.

`value`

    

The new value to set for the item specified by `keyPath`.

## Return Value

A view that has the given value set in its environment.

## Discussion

Use this modifier to set one of the writable properties of the
`EnvironmentValues` structure, including custom values that you create. For
example, you can set the value associated with the `truncationMode` key:

You then read the value inside `MyView` or one of its descendants using the
`Environment` property wrapper:

SwiftUI provides dedicated view modifiers for setting most environment values,
like the `truncationMode(_:)` modifier which sets the `truncationMode` value:

Prefer the dedicated modifier when available, and offer your own when defining
custom environment values, as described in `EnvironmentKey`.

This modifier affects the given view, as well as that view’s descendant views.
It has no effect outside the view hierarchy on which you call it.

## See Also

### Modifying the environment of a view

`func environment<T>(T?) -> some View`

Places an observable object in the view’s environment.

`func transformEnvironment<V>(WritableKeyPath<EnvironmentValues, V>,
transform: (inout V) -> Void) -> some View`

Transforms the environment value of the specified key path with the given
function.

Instance Method

# environmentObject(_:)

Supplies an observable object to a view’s hierarchy.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func environmentObject<T>(_ object: T) -> some View where T : ObservableObject
    

##  Parameters

`object`

    

The object to store and make available to the view’s hierarchy.

## Discussion

Use this modifier to add an observable object to a view’s environment. The
object must conform to the `ObservableObject` protocol.

Adding an object to a view’s environment makes the object available to
subviews in the view’s hierarchy. To retrieve the object in a subview, use the
`EnvironmentObject` property wrapper.

Note

If the observable object conforms to the `Observable` protocol, use either
`environment(_:)` or the `environment(_:_:)` modifier to add the object to the
view’s environment.

## See Also

### Distributing model data throughout your app

`func environmentObject<T>(T) -> some Scene`

Supplies an `ObservableObject` to a view subhierarchy.

`struct EnvironmentObject`

A property wrapper type for an observable object that a parent or ancestor
view supplies.

Instance Method

# transformEnvironment(_:transform:)

Transforms the environment value of the specified key path with the given
function.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func transformEnvironment<V>(
        _ keyPath: WritableKeyPath<EnvironmentValues, V>,
        transform: @escaping (inout V) -> Void
    ) -> some View
    

## See Also

### Modifying the environment of a view

`func environment<T>(T?) -> some View`

Places an observable object in the view’s environment.

`func environment<V>(WritableKeyPath<EnvironmentValues, V>, V) -> some View`

Sets the environment value of the specified key path to the given value.

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

Instance Method

# defaultAppStorage(_:)

The default store used by `AppStorage` contained within the view.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func defaultAppStorage(_ store: UserDefaults) -> some View
    

##  Parameters

`store`

    

The user defaults to use as the default store for `AppStorage`.

## Discussion

If unspecified, the default store for a view hierarchy is
`UserDefaults.standard`, but can be set a to a custom one. For example,
sharing defaults between an app and an extension can override the default
store to one created with `UserDefaults.init(suiteName:_)`.

## See Also

### Saving state across app launches

Restoring Your App’s State with SwiftUI

Provide app continuity for users by preserving their current activities.

`struct AppStorage`

A property wrapper type that reflects a value from `UserDefaults` and
invalidates a view on a change in value in that user default.

`struct SceneStorage`

A property wrapper type that reads and writes to persisted, per-scene storage.

Instance Method

# modelContext(_:)

Sets the model context in this view’s environment.

SwiftData  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    func modelContext(_ modelContext: ModelContext) -> some View
    

##  Parameters

`modelContext`

    

The model context to set in this view’s environment.

## Discussion

In this example, the `RecipesList` view sets a model context to use for all of
its content:

The environment’s `modelContext` property will be assigned `myContext`. All
implicit model context operations in this view, such as `Query` properties,
will use the environment’s context.

## See Also

### Configuring a model

`func modelContainer(ModelContainer) -> some View`

Sets the model container and associated model context in this view’s
environment.

`func modelContainer(for: any PersistentModel.Type, inMemory: Bool,
isAutosaveEnabled: Bool, isUndoEnabled: Bool, onSetup: (Result<ModelContainer,
any Error>) -> Void) -> some View`

Sets the model container in this view for storing the provided model type,
creating a new container if necessary, and also sets a model context for that
container in this view’s environment.

`func modelContainer(for: [any PersistentModel.Type], inMemory: Bool,
isAutosaveEnabled: Bool, isUndoEnabled: Bool, onSetup: (Result<ModelContainer,
any Error>) -> Void) -> some View`

Sets the model container in this view for storing the provided model types,
creating a new container if necessary, and also sets a model context for that
container in this view’s environment.

Instance Method

# modelContainer(_:)

Sets the model container and associated model context in this view’s
environment.

SwiftData  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    func modelContainer(_ container: ModelContainer) -> some View
    

##  Parameters

`container`

    

The model container to use for this view.

## Discussion

In this example, `ContentView` sets a model container to use for
`RecipesList`:

The environment’s `modelContext` property will be assigned a new context
associated with this container. All implicit model context operations in this
view, such as `Query` properties, will use the environment’s context.

## See Also

### Configuring a model

`func modelContext(ModelContext) -> some View`

Sets the model context in this view’s environment.

`func modelContainer(for: any PersistentModel.Type, inMemory: Bool,
isAutosaveEnabled: Bool, isUndoEnabled: Bool, onSetup: (Result<ModelContainer,
any Error>) -> Void) -> some View`

Sets the model container in this view for storing the provided model type,
creating a new container if necessary, and also sets a model context for that
container in this view’s environment.

`func modelContainer(for: [any PersistentModel.Type], inMemory: Bool,
isAutosaveEnabled: Bool, isUndoEnabled: Bool, onSetup: (Result<ModelContainer,
any Error>) -> Void) -> some View`

Sets the model container in this view for storing the provided model types,
creating a new container if necessary, and also sets a model context for that
container in this view’s environment.

Instance Method

# modelContainer(for:inMemory:isAutosaveEnabled:isUndoEnabled:onSetup:)

Sets the model container in this view for storing the provided model type,
creating a new container if necessary, and also sets a model context for that
container in this view’s environment.

SwiftData  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    func modelContainer(
        for modelType: any PersistentModel.Type,
        inMemory: Bool = false,
        isAutosaveEnabled: Bool = true,
        isUndoEnabled: Bool = false,
        onSetup: @escaping (Result<ModelContainer, any Error>) -> Void = { _ in }
    ) -> some View
    

##  Parameters

`modelType`

    

The model type defining the schema used to create the model container.

`inMemory`

    

Whether the container should store data only in memory.

`isAutosaveEnabled`

    

`true` if autosave is enabled.

`isUndoEnabled`

    

use `undoManager` in the environment to manage undo operations for the model
container.

`onSetup`

    

A callback that will be invoked when the creation of the container has has
succeeded or failed.

## Discussion

In this example, the `RecipesList` view sets a model container to use for all
of its contents, configured to store instances of `Recipe`:

The environment’s `modelContext` property will be assigned a new context
associated with this container. All implicit model context operations in this
view, such as `Query` properties, will use the environment’s context.

By default, the container stores its model data persistently on disk. To only
store data in memory for the lifetime of the app’s process, pass `true` to the
`inMemory:` parameter.

The container will only be created once. New values that are passed to the
`modelType` and `inMemory` parameters after the view is first created will be
ignored.

## See Also

### Configuring a model

`func modelContext(ModelContext) -> some View`

Sets the model context in this view’s environment.

`func modelContainer(ModelContainer) -> some View`

Sets the model container and associated model context in this view’s
environment.

`func modelContainer(for: [any PersistentModel.Type], inMemory: Bool,
isAutosaveEnabled: Bool, isUndoEnabled: Bool, onSetup: (Result<ModelContainer,
any Error>) -> Void) -> some View`

Sets the model container in this view for storing the provided model types,
creating a new container if necessary, and also sets a model context for that
container in this view’s environment.

Instance Method

# modelContainer(for:inMemory:isAutosaveEnabled:isUndoEnabled:onSetup:)

Sets the model container in this view for storing the provided model types,
creating a new container if necessary, and also sets a model context for that
container in this view’s environment.

SwiftData  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+

    
    
    func modelContainer(
        for modelTypes: [any PersistentModel.Type],
        inMemory: Bool = false,
        isAutosaveEnabled: Bool = true,
        isUndoEnabled: Bool = false,
        onSetup: @escaping (Result<ModelContainer, any Error>) -> Void = { _ in }
    ) -> some View
    

##  Parameters

`modelTypes`

    

The model types defining the schema used to create the model container.

`inMemory`

    

Whether the container should store data only in memory.

`isAutosaveEnabled`

    

`true` if autosave is enabled.

`isUndoEnabled`

    

use `undoManager` in the view’s environment to manage undo operations for the
model container.

`onSetup`

    

A callback that will be invoked when the creation of the container has has
succeeded or failed.

## Discussion

In this example, the `RecipesList` view sets a model container to use for all
of its contents, configured to store instances of `Recipe` and `Ingredient`:

The environment’s `modelContext` property will be assigned a new context
associated with this container. All implicit model context operations in this
view, such as `Query` properties, will use the environment’s context.

By default, the container stores its model data persistently on disk. To only
store data in memory for the lifetime of the app’s process, pass `true` to the
`inMemory:` parameter.

The container will only be created once. New values that are passed to the
`modelTypes` and `inMemory` parameters after the view is first created will be
ignored.

## See Also

### Configuring a model

`func modelContext(ModelContext) -> some View`

Sets the model context in this view’s environment.

`func modelContainer(ModelContainer) -> some View`

Sets the model container and associated model context in this view’s
environment.

`func modelContainer(for: any PersistentModel.Type, inMemory: Bool,
isAutosaveEnabled: Bool, isUndoEnabled: Bool, onSetup: (Result<ModelContainer,
any Error>) -> Void) -> some View`

Sets the model container in this view for storing the provided model type,
creating a new container if necessary, and also sets a model context for that
container in this view’s environment.

