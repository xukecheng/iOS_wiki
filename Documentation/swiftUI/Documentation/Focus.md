Instance Method

# focusable(_:)

Specifies if the view is focusable.

iOS 17.0+  iPadOS 17.0+  macOS 12.0+  Mac Catalyst 17.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func focusable(_ isFocusable: Bool = true) -> some View
    

##  Parameters

`isFocusable`

    

A Boolean value that indicates whether this view is focusable.

## Return Value

A view that sets whether a view is focusable.

## See Also

### Indicating that a view can receive focus

`func focusable(Bool, interactions: FocusInteractions) -> some View`

Specifies if the view is focusable, and if so, what focus-driven interactions
it supports.

`struct FocusInteractions`

Values describe different focus interactions that a view can support.

Instance Method

# focusable(_:interactions:)

Specifies if the view is focusable, and if so, what focus-driven interactions
it supports.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func focusable(
        _ isFocusable: Bool = true,
        interactions: FocusInteractions
    ) -> some View
    

##  Parameters

`isFocusable`

    

`true` if the view should participate in focus; `false` otherwise. The default
value is `true`.

`interactions`

    

The types of focus interactions supported by the view. The default value is
`.automatic`.

## Return Value

A view that sets whether its child is focusable.

## Discussion

By default, SwiftUI enables all possible focus interactions. However, on macOS
and iOS it is conventional for button-like views to only accept focus when the
user has enabled keyboard navigation system-wide in the Settings app. Clients
can reproduce this behavior with custom views by only supporting `.activate`
interactions.

Note

The focus interactions allowed for custom views changed in macOS
14—previously, custom views could only become focused with keyboard navigation
enabled system-wide. Clients built using older SDKs will continue to see the
older focus behavior, while custom views in clients built using macOS 14 or
later will always be focusable unless the client requests otherwise by
specifying a restricted set of focus interactions.

## See Also

### Indicating that a view can receive focus

`func focusable(Bool) -> some View`

Specifies if the view is focusable.

`struct FocusInteractions`

Values describe different focus interactions that a view can support.

Structure

# FocusInteractions

Values describe different focus interactions that a view can support.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct FocusInteractions

## Topics

### Creating the interaction types

`static var automatic: FocusInteractions`

The view supports whatever focus-driven interactions are commonly expected for
interactive content on the current platform.

`static let activate: FocusInteractions`

The view has a primary action that can be activated via focus gestures.

`static let edit: FocusInteractions`

The view captures input from non-spatial sources like a keyboard or Digital
Crown.

## Relationships

### Conforms To

  * `Equatable`
  * `ExpressibleByArrayLiteral`
  * `OptionSet`
  * `RawRepresentable`
  * `Sendable`
  * `SetAlgebra`

## See Also

### Indicating that a view can receive focus

`func focusable(Bool) -> some View`

Specifies if the view is focusable.

`func focusable(Bool, interactions: FocusInteractions) -> some View`

Specifies if the view is focusable, and if so, what focus-driven interactions
it supports.

Instance Method

# focused(_:equals:)

Modifies this view by binding its focus state to the given state value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func focused<Value>(
        _ binding: FocusState<Value>.Binding,
        equals value: Value
    ) -> some View where Value : Hashable
    

##  Parameters

`binding`

    

The state binding to register. When focus moves to the modified view, the
binding sets the bound value to the corresponding match value. If a caller
sets the state value programmatically to the matching value, then focus moves
to the modified view. When focus leaves the modified view, the binding sets
the bound value to `nil`. If a caller sets the value to `nil`, SwiftUI
automatically dismisses focus.

`value`

    

The value to match against when determining whether the binding should change.

## Return Value

The modified view.

## Discussion

Use this modifier to cause the view to receive focus whenever the the
`binding` equals the `value`. Typically, you create an enumeration of fields
that may receive focus, bind an instance of this enumeration, and assign its
cases to focusable views.

The following example uses the cases of a `LoginForm` enumeration to bind the
focus state of two `TextField` views. A sign-in button validates the fields
and sets the bound `focusedField` value to any field that requires the user to
correct a problem.

To control focus using a Boolean, use the `focused(_:)` method instead.

## See Also

### Managing focus state

`func focused(FocusState<Bool>.Binding) -> some View`

Modifies this view by binding its focus state to the given Boolean state
value.

`var isFocused: Bool`

Returns whether the nearest focusable ancestor has focus.

`struct FocusState`

A property wrapper type that can read and write a value that SwiftUI updates
as the placement of focus within the scene changes.

`struct FocusedValue`

A property wrapper for observing values from the focused view or one of its
ancestors.

`protocol FocusedValueKey`

A protocol for identifier types used when publishing and observing focused
values.

`struct FocusedBinding`

A convenience property wrapper for observing and automatically unwrapping
state bindings from the focused view or one of its ancestors.

Instance Method

# focused(_:)

Modifies this view by binding its focus state to the given Boolean state
value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func focused(_ condition: FocusState<Bool>.Binding) -> some View
    

##  Parameters

`condition`

    

The focus state to bind. When focus moves to the view, the binding sets the
bound value to `true`. If a caller sets the value to `true` programmatically,
then focus moves to the modified view. When focus leaves the modified view,
the binding sets the value to `false`. If a caller sets the value to `false`,
SwiftUI automatically dismisses focus.

## Return Value

The modified view.

## Discussion

Use this modifier to cause the view to receive focus whenever the the
`condition` value is `true`. You can use this modifier to observe the focus
state of a single view, or programmatically set and remove focus from the
view.

In the following example, a single `TextField` accepts a user’s desired
`username`. The text field binds its focus state to the Boolean value
`usernameFieldIsFocused`. A “Submit” button’s action verifies whether the name
is available. If the name is unavailable, the button sets
`usernameFieldIsFocused` to `true`, which causes focus to return to the text
field, so the user can enter a different name.

To control focus by matching a value, use the `focused(_:equals:)` method
instead.

## See Also

### Managing focus state

`func focused<Value>(FocusState<Value>.Binding, equals: Value) -> some View`

Modifies this view by binding its focus state to the given state value.

`var isFocused: Bool`

Returns whether the nearest focusable ancestor has focus.

`struct FocusState`

A property wrapper type that can read and write a value that SwiftUI updates
as the placement of focus within the scene changes.

`struct FocusedValue`

A property wrapper for observing values from the focused view or one of its
ancestors.

`protocol FocusedValueKey`

A protocol for identifier types used when publishing and observing focused
values.

`struct FocusedBinding`

A convenience property wrapper for observing and automatically unwrapping
state bindings from the focused view or one of its ancestors.

Instance Property

# isFocused

Returns whether the nearest focusable ancestor has focus.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    var isFocused: Bool { get }

## Discussion

If there is no focusable ancestor, the value is `false`.

## See Also

### Managing focus state

`func focused<Value>(FocusState<Value>.Binding, equals: Value) -> some View`

Modifies this view by binding its focus state to the given state value.

`func focused(FocusState<Bool>.Binding) -> some View`

Modifies this view by binding its focus state to the given Boolean state
value.

`struct FocusState`

A property wrapper type that can read and write a value that SwiftUI updates
as the placement of focus within the scene changes.

`struct FocusedValue`

A property wrapper for observing values from the focused view or one of its
ancestors.

`protocol FocusedValueKey`

A protocol for identifier types used when publishing and observing focused
values.

`struct FocusedBinding`

A convenience property wrapper for observing and automatically unwrapping
state bindings from the focused view or one of its ancestors.

Structure

# FocusState

A property wrapper type that can read and write a value that SwiftUI updates
as the placement of focus within the scene changes.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    @frozen @propertyWrapper
    struct FocusState<Value> where Value : Hashable

## Overview

Use this property wrapper in conjunction with `focused(_:equals:)` and
`focused(_:)` to describe views whose appearance and contents relate to the
location of focus in the scene. When focus enters the modified view, the
wrapped value of this property updates to match a given prototype value.
Similarly, when focus leaves, the wrapped value of this property resets to
`nil` or `false`. Setting the property’s value programmatically has the
reverse effect, causing focus to move to the view associated with the updated
value.

In the following example of a simple login screen, when the user presses the
Sign In button and one of the fields is still empty, focus moves to that
field. Otherwise, the sign-in process proceeds.

To allow for cases where focus is completely absent from a view tree, the
wrapped value must be either an optional or a Boolean. Set the focus binding
to `false` or `nil` as appropriate to remove focus from all bound fields. You
can also use this to remove focus from a `TextField` and thereby dismiss the
keyboard.

### Avoid ambiguous focus bindings

The same view can have multiple focus bindings. In the following example,
setting `focusedField` to either `name` or `fullName` causes the field to
receive focus:

On the other hand, binding the same value to two views is ambiguous. In the
following example, two separate fields bind focus to the `name` value:

If the user moves focus to either field, the `focusedField` binding updates to
`name`. However, if the app programmatically sets the value to `name`, SwiftUI
chooses the first candidate, which in this case is the “Name” field. SwiftUI
also emits a runtime warning in this case, since the repeated binding is
likely a programmer error.

## Topics

### Creating a focus state

`init<T>()`

Creates a focus state that binds to an optional type.

`init()`

Creates a focus state that binds to a Boolean.

### Inspecting the focus state

`var projectedValue: FocusState<Value>.Binding`

A projection of the focus state value that returns a binding.

`struct Binding`

A property wrapper type that can read and write a value that indicates the
current focus location.

`var wrappedValue: Value`

The current state value, taking into account whatever bindings might be in
effect due to the current location of focus.

## Relationships

### Conforms To

  * `DynamicProperty`

## See Also

### Managing focus state

`func focused<Value>(FocusState<Value>.Binding, equals: Value) -> some View`

Modifies this view by binding its focus state to the given state value.

`func focused(FocusState<Bool>.Binding) -> some View`

Modifies this view by binding its focus state to the given Boolean state
value.

`var isFocused: Bool`

Returns whether the nearest focusable ancestor has focus.

`struct FocusedValue`

A property wrapper for observing values from the focused view or one of its
ancestors.

`protocol FocusedValueKey`

A protocol for identifier types used when publishing and observing focused
values.

`struct FocusedBinding`

A convenience property wrapper for observing and automatically unwrapping
state bindings from the focused view or one of its ancestors.

Structure

# FocusedValue

A property wrapper for observing values from the focused view or one of its
ancestors.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    @propertyWrapper
    struct FocusedValue<Value>

## Overview

If multiple views publish values using the same key, the wrapped property will
reflect the value from the view closest to focus.

## Topics

### Creating the value

`init(Value.Type)`

A new property wrapper for the given object type.

`init(KeyPath<FocusedValues, Value?>)`

A new property wrapper for the given key path.

### Getting the value

`var wrappedValue: Value?`

The value for the focus key given the current scope and state of the focused
view hierarchy.

## Relationships

### Conforms To

  * `DynamicProperty`

## See Also

### Managing focus state

`func focused<Value>(FocusState<Value>.Binding, equals: Value) -> some View`

Modifies this view by binding its focus state to the given state value.

`func focused(FocusState<Bool>.Binding) -> some View`

Modifies this view by binding its focus state to the given Boolean state
value.

`var isFocused: Bool`

Returns whether the nearest focusable ancestor has focus.

`struct FocusState`

A property wrapper type that can read and write a value that SwiftUI updates
as the placement of focus within the scene changes.

`protocol FocusedValueKey`

A protocol for identifier types used when publishing and observing focused
values.

`struct FocusedBinding`

A convenience property wrapper for observing and automatically unwrapping
state bindings from the focused view or one of its ancestors.

Protocol

# FocusedValueKey

A protocol for identifier types used when publishing and observing focused
values.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    protocol FocusedValueKey

## Overview

Unlike `EnvironmentKey`, `FocusedValueKey` has no default value requirement,
because the default value for a key is always `nil`.

## Topics

### Specifying the value type

`associatedtype Value`

**Required**

## See Also

### Managing focus state

`func focused<Value>(FocusState<Value>.Binding, equals: Value) -> some View`

Modifies this view by binding its focus state to the given state value.

`func focused(FocusState<Bool>.Binding) -> some View`

Modifies this view by binding its focus state to the given Boolean state
value.

`var isFocused: Bool`

Returns whether the nearest focusable ancestor has focus.

`struct FocusState`

A property wrapper type that can read and write a value that SwiftUI updates
as the placement of focus within the scene changes.

`struct FocusedValue`

A property wrapper for observing values from the focused view or one of its
ancestors.

`struct FocusedBinding`

A convenience property wrapper for observing and automatically unwrapping
state bindings from the focused view or one of its ancestors.

Structure

# FocusedBinding

A convenience property wrapper for observing and automatically unwrapping
state bindings from the focused view or one of its ancestors.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    @propertyWrapper
    struct FocusedBinding<Value>

## Overview

If multiple views publish bindings using the same key, the wrapped property
will reflect the value of the binding from the view closest to focus.

## Topics

### Creating the binding

`init(KeyPath<FocusedValues, Binding<Value>?>)`

A new property wrapper for the given key path.

### Getting the value

`var projectedValue: Binding<Value?>`

A binding to the optional value.

`var wrappedValue: Value?`

The unwrapped value for the focus key given the current scope and state of the
focused view hierarchy.

## Relationships

### Conforms To

  * `DynamicProperty`

## See Also

### Managing focus state

`func focused<Value>(FocusState<Value>.Binding, equals: Value) -> some View`

Modifies this view by binding its focus state to the given state value.

`func focused(FocusState<Bool>.Binding) -> some View`

Modifies this view by binding its focus state to the given Boolean state
value.

`var isFocused: Bool`

Returns whether the nearest focusable ancestor has focus.

`struct FocusState`

A property wrapper type that can read and write a value that SwiftUI updates
as the placement of focus within the scene changes.

`struct FocusedValue`

A property wrapper for observing values from the focused view or one of its
ancestors.

`protocol FocusedValueKey`

A protocol for identifier types used when publishing and observing focused
values.

Instance Method

# focusedValue(_:)

Sets the focused value for the given object type.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func focusedValue<T>(_ object: T?) -> some View where T : AnyObject, T : Observable
    

## Discussion

Important

This initializer only accepts objects conforming to the `Observable` protocol.
For reading environment objects that conform to `ObservableObject`, use
`focusedObject(_:)`, instead.

To read this value, use the `FocusedValue` property wrapper.

## See Also

### Exposing value types to focused views

`func focusedValue<Value>(WritableKeyPath<FocusedValues, Value?>, Value) ->
some View`

Modifies this view by injecting a value that you provide for use by other
views whose state depends on the focused view hierarchy.

`func focusedValue<Value>(WritableKeyPath<FocusedValues, Value?>, Value?) ->
some View`

Creates a new view that exposes the provided value to other views whose state
depends on the focused view hierarchy.

`func focusedSceneValue<T>(WritableKeyPath<FocusedValues, T?>, T?) -> some
View`

Creates a new view that exposes the provided value to other views whose state
depends on the active scene.

`func focusedSceneValue<T>(WritableKeyPath<FocusedValues, T?>, T) -> some
View`

Modifies this view by injecting a value that you provide for use by other
views whose state depends on the focused scene.

`struct FocusedValues`

A collection of state exported by the focused view and its ancestors.

Instance Method

# focusedValue(_:_:)

Modifies this view by injecting a value that you provide for use by other
views whose state depends on the focused view hierarchy.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func focusedValue<Value>(
        _ keyPath: WritableKeyPath<FocusedValues, Value?>,
        _ value: Value
    ) -> some View
    

##  Parameters

`keyPath`

    

The key path to associate `value` with when adding it to the existing table of
exported focus values.

`value`

    

The focus value to export.

## Return Value

A modified representation of this view.

## See Also

### Exposing value types to focused views

`func focusedValue<T>(T?) -> some View`

Sets the focused value for the given object type.

`func focusedValue<Value>(WritableKeyPath<FocusedValues, Value?>, Value?) ->
some View`

Creates a new view that exposes the provided value to other views whose state
depends on the focused view hierarchy.

`func focusedSceneValue<T>(WritableKeyPath<FocusedValues, T?>, T?) -> some
View`

Creates a new view that exposes the provided value to other views whose state
depends on the active scene.

`func focusedSceneValue<T>(WritableKeyPath<FocusedValues, T?>, T) -> some
View`

Modifies this view by injecting a value that you provide for use by other
views whose state depends on the focused scene.

`struct FocusedValues`

A collection of state exported by the focused view and its ancestors.

Instance Method

# focusedValue(_:_:)

Creates a new view that exposes the provided value to other views whose state
depends on the focused view hierarchy.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func focusedValue<Value>(
        _ keyPath: WritableKeyPath<FocusedValues, Value?>,
        _ value: Value?
    ) -> some View
    

##  Parameters

`keyPath`

    

The key path to associate `value` with when adding it to the existing table of
exported focus values.

`value`

    

The focus value to export, or `nil` if no value is currently available.

## Return Value

A modified representation of this view.

## Discussion

Use this method instead of `View/focusedSceneValue(_:_:)` when your scene
includes multiple focusable views with their own associated values, and you
need an app- or scene-scoped element like a command or toolbar item that
operates on the value associated with whichever view currently has focus. Each
focusable view can supply its own value:

## See Also

### Exposing value types to focused views

`func focusedValue<T>(T?) -> some View`

Sets the focused value for the given object type.

`func focusedValue<Value>(WritableKeyPath<FocusedValues, Value?>, Value) ->
some View`

Modifies this view by injecting a value that you provide for use by other
views whose state depends on the focused view hierarchy.

`func focusedSceneValue<T>(WritableKeyPath<FocusedValues, T?>, T?) -> some
View`

Creates a new view that exposes the provided value to other views whose state
depends on the active scene.

`func focusedSceneValue<T>(WritableKeyPath<FocusedValues, T?>, T) -> some
View`

Modifies this view by injecting a value that you provide for use by other
views whose state depends on the focused scene.

`struct FocusedValues`

A collection of state exported by the focused view and its ancestors.

Instance Method

# focusedSceneValue(_:_:)

Creates a new view that exposes the provided value to other views whose state
depends on the active scene.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func focusedSceneValue<T>(
        _ keyPath: WritableKeyPath<FocusedValues, T?>,
        _ value: T?
    ) -> some View
    

##  Parameters

`keyPath`

    

The key path to associate `value` with when adding it to the existing table of
published focus values.

`value`

    

The focus value to publish, or `nil` if no value is currently available.

## Return Value

A modified representation of this view.

## Discussion

Use this method instead of `View/focusedValue(_:_:)` for values that must be
visible regardless of where focus is located in the active scene. For example,
if an app needs a command for moving focus to a particular text field in the
sidebar, it could use this modifier to publish a button action that’s visible
to command views as long as the scene is active, and regardless of where focus
happens to be in it.

    
    
    struct Sidebar: View {
        @FocusState var isFiltering: Bool
    
    
        var body: some View {
            VStack {
                TextField(...)
                    .focused(when: $isFiltering)
                    .focusedSceneValue(\.filterAction) {
                        isFiltering = true
                    }
            }
        }
    }
    
    
    struct NavigationCommands: Commands {
        @FocusedValue(\.filterAction) var filterAction
    
    
        var body: some Commands {
            CommandMenu("Navigate") {
                Button("Filter in Sidebar") {
                    filterAction?()
                }
            }
            .disabled(filterAction == nil)
        }
    }
    
    
    struct FilterActionKey: FocusedValuesKey {
        typealias Value = () -> Void
    }
    
    
    extension FocusedValues {
        var filterAction: (() -> Void)? {
            get { self[FilterActionKey.self] }
            set { self[FilterActionKey.self] = newValue }
        }
    }
    

## See Also

### Exposing value types to focused views

`func focusedValue<T>(T?) -> some View`

Sets the focused value for the given object type.

`func focusedValue<Value>(WritableKeyPath<FocusedValues, Value?>, Value) ->
some View`

Modifies this view by injecting a value that you provide for use by other
views whose state depends on the focused view hierarchy.

`func focusedValue<Value>(WritableKeyPath<FocusedValues, Value?>, Value?) ->
some View`

Creates a new view that exposes the provided value to other views whose state
depends on the focused view hierarchy.

`func focusedSceneValue<T>(WritableKeyPath<FocusedValues, T?>, T) -> some
View`

Modifies this view by injecting a value that you provide for use by other
views whose state depends on the focused scene.

`struct FocusedValues`

A collection of state exported by the focused view and its ancestors.

Instance Method

# focusedSceneValue(_:_:)

Modifies this view by injecting a value that you provide for use by other
views whose state depends on the focused scene.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func focusedSceneValue<T>(
        _ keyPath: WritableKeyPath<FocusedValues, T?>,
        _ value: T
    ) -> some View
    

##  Parameters

`keyPath`

    

The key path to associate `value` with when adding it to the existing table of
published focus values.

`value`

    

The focus value to publish.

## Return Value

A modified representation of this view.

## Discussion

Use this method instead of `View/focusedValue(_:_:)` for values that must be
visible regardless of where focus is located in the active scene. For example,
if an app needs a command for moving focus to a particular text field in the
sidebar, it could use this modifier to publish a button action that’s visible
to command views as long as the scene is active, and regardless of where focus
happens to be in it.

## See Also

### Exposing value types to focused views

`func focusedValue<T>(T?) -> some View`

Sets the focused value for the given object type.

`func focusedValue<Value>(WritableKeyPath<FocusedValues, Value?>, Value) ->
some View`

Modifies this view by injecting a value that you provide for use by other
views whose state depends on the focused view hierarchy.

`func focusedValue<Value>(WritableKeyPath<FocusedValues, Value?>, Value?) ->
some View`

Creates a new view that exposes the provided value to other views whose state
depends on the focused view hierarchy.

`func focusedSceneValue<T>(WritableKeyPath<FocusedValues, T?>, T?) -> some
View`

Creates a new view that exposes the provided value to other views whose state
depends on the active scene.

`struct FocusedValues`

A collection of state exported by the focused view and its ancestors.

Structure

# FocusedValues

A collection of state exported by the focused view and its ancestors.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    struct FocusedValues

## Topics

### Getting the value for a key

`subscript<Key>(Key.Type) -> Key.Value?`

Reads and writes values associated with a given focused value key.

## Relationships

### Conforms To

  * `Equatable`

## See Also

### Exposing value types to focused views

`func focusedValue<T>(T?) -> some View`

Sets the focused value for the given object type.

`func focusedValue<Value>(WritableKeyPath<FocusedValues, Value?>, Value) ->
some View`

Modifies this view by injecting a value that you provide for use by other
views whose state depends on the focused view hierarchy.

`func focusedValue<Value>(WritableKeyPath<FocusedValues, Value?>, Value?) ->
some View`

Creates a new view that exposes the provided value to other views whose state
depends on the focused view hierarchy.

`func focusedSceneValue<T>(WritableKeyPath<FocusedValues, T?>, T?) -> some
View`

Creates a new view that exposes the provided value to other views whose state
depends on the active scene.

`func focusedSceneValue<T>(WritableKeyPath<FocusedValues, T?>, T) -> some
View`

Modifies this view by injecting a value that you provide for use by other
views whose state depends on the focused scene.

Instance Method

# focusedObject(_:)

Creates a new view that exposes the provided object to other views whose state
depends on the focused view hierarchy.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func focusedObject<T>(_ object: T?) -> some View where T : ObservableObject
    

##  Parameters

`object`

    

The observable object to associate with focus, or `nil` if no object is
currently available.

## Return Value

A view that supplies an observable object when in focus.

## Discussion

Use this method instead of `View/focusedSceneObject(_:)` when your scene
includes multiple focusable views with their own associated data, and you need
an app- or scene-scoped element like a command or toolbar item that operates
on the data associated with whichever view currently has focus. Each focusable
view can supply its own object:

Interested views can then use the `FocusedObject` property wrapper to observe
and update the focused view’s object. In this example, an app command updates
the focused view’s data, and is automatically disabled when focus is in an
unrelated part of the scene:

## See Also

### Exposing reference types to focused views

`func focusedObject<T>(T) -> some View`

Creates a new view that exposes the provided object to other views whose whose
state depends on the focused view hierarchy.

`func focusedSceneObject<T>(T?) -> some View`

Creates a new view that exposes the provided object to other views whose whose
state depends on the active scene.

`func focusedSceneObject<T>(T) -> some View`

Creates a new view that exposes the provided object to other views whose whose
state depends on the active scene.

`struct FocusedObject`

A property wrapper type for an observable object supplied by the focused view
or one of its ancestors.

Instance Method

# focusedObject(_:)

Creates a new view that exposes the provided object to other views whose whose
state depends on the focused view hierarchy.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func focusedObject<T>(_ object: T) -> some View where T : ObservableObject
    

##  Parameters

`object`

    

The observable object to associate with focus.

## Return Value

A view that supplies an observable object when in focus.

## Discussion

Use this method instead of `View/focusedSceneObject(_:)` when your scene
includes multiple focusable views with their own associated data, and you need
an app- or scene-scoped element like a command or toolbar item that operates
on the data associated with whichever view currently has focus. Each focusable
view can supply its own object:

Interested views can then use the `FocusedObject` property wrapper to observe
and update the focused view’s object. In this example, an app command updates
the focused view’s data, and is automatically disabled when focus is in an
unrelated part of the scene:

## See Also

### Exposing reference types to focused views

`func focusedObject<T>(T?) -> some View`

Creates a new view that exposes the provided object to other views whose state
depends on the focused view hierarchy.

`func focusedSceneObject<T>(T?) -> some View`

Creates a new view that exposes the provided object to other views whose whose
state depends on the active scene.

`func focusedSceneObject<T>(T) -> some View`

Creates a new view that exposes the provided object to other views whose whose
state depends on the active scene.

`struct FocusedObject`

A property wrapper type for an observable object supplied by the focused view
or one of its ancestors.

Instance Method

# focusedSceneObject(_:)

Creates a new view that exposes the provided object to other views whose whose
state depends on the active scene.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func focusedSceneObject<T>(_ object: T?) -> some View where T : ObservableObject
    

##  Parameters

`object`

    

The observable object to associate with the scene, or `nil` if no object is
currently available.

## Return Value

A view that supplies an observable object while the scene is active.

## Discussion

Use this method instead of `View/focusedObject(_:)` for observable objects
that must be visible regardless of where focus is located in the active scene.
This is sometimes needed for things like main menu and discoverability HUD
commands that observe and update data from the active scene but aren’t
concerned with what the user is actually focused on. The scene’s root view can
supply the scene’s state object:

Interested views can then use the `FocusedObject` property wrapper to observe
and update the active scene’s state object. In this example, an app command
updates the active scene’s data, and is enabled as long as any scene is
active.

## See Also

### Exposing reference types to focused views

`func focusedObject<T>(T?) -> some View`

Creates a new view that exposes the provided object to other views whose state
depends on the focused view hierarchy.

`func focusedObject<T>(T) -> some View`

Creates a new view that exposes the provided object to other views whose whose
state depends on the focused view hierarchy.

`func focusedSceneObject<T>(T) -> some View`

Creates a new view that exposes the provided object to other views whose whose
state depends on the active scene.

`struct FocusedObject`

A property wrapper type for an observable object supplied by the focused view
or one of its ancestors.

Instance Method

# focusedSceneObject(_:)

Creates a new view that exposes the provided object to other views whose whose
state depends on the active scene.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func focusedSceneObject<T>(_ object: T) -> some View where T : ObservableObject
    

##  Parameters

`object`

    

The observable object to associate with the scene.

## Return Value

A view that supplies an observable object while the scene is active.

## Discussion

Use this method instead of `View/focusedObject(_:)` for observable objects
that must be visible regardless of where focus is located in the active scene.
This is sometimes needed for things like main menu and discoverability HUD
commands that observe and update data from the active scene but aren’t
concerned with what the user is actually focused on. The scene’s root view can
supply the scene’s state object:

Interested views can then use the `FocusedObject` property wrapper to observe
and update the active scene’s state object. In this example, an app command
updates the active scene’s data, and is enabled as long as any scene is
active.

## See Also

### Exposing reference types to focused views

`func focusedObject<T>(T?) -> some View`

Creates a new view that exposes the provided object to other views whose state
depends on the focused view hierarchy.

`func focusedObject<T>(T) -> some View`

Creates a new view that exposes the provided object to other views whose whose
state depends on the focused view hierarchy.

`func focusedSceneObject<T>(T?) -> some View`

Creates a new view that exposes the provided object to other views whose whose
state depends on the active scene.

`struct FocusedObject`

A property wrapper type for an observable object supplied by the focused view
or one of its ancestors.

Structure

# FocusedObject

A property wrapper type for an observable object supplied by the focused view
or one of its ancestors.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    @frozen @propertyWrapper
    struct FocusedObject<ObjectType> where ObjectType : ObservableObject

## Overview

Focused objects invalidate the current view whenever the observable object
changes. If multiple views publish a focused object using the same key, the
wrapped property will reflect the object that’s closest to the focused view.

## Topics

### Creating the focused object

`init()`

Creates a focused object.

### Getting the value

`var projectedValue: FocusedObject<ObjectType>.Wrapper?`

A projection of the focused object that creates bindings to its properties
using dynamic member lookup.

`var wrappedValue: ObjectType?`

The underlying value referenced by the focused object.

`struct Wrapper`

A wrapper around the underlying focused object that can create bindings to its
properties using dynamic member lookup.

## Relationships

### Conforms To

  * `DynamicProperty`

## See Also

### Exposing reference types to focused views

`func focusedObject<T>(T?) -> some View`

Creates a new view that exposes the provided object to other views whose state
depends on the focused view hierarchy.

`func focusedObject<T>(T) -> some View`

Creates a new view that exposes the provided object to other views whose whose
state depends on the focused view hierarchy.

`func focusedSceneObject<T>(T?) -> some View`

Creates a new view that exposes the provided object to other views whose whose
state depends on the active scene.

`func focusedSceneObject<T>(T) -> some View`

Creates a new view that exposes the provided object to other views whose whose
state depends on the active scene.

Instance Method

# focusScope(_:)

Creates a focus scope that SwiftUI uses to limit default focus preferences.

macOS 12.0+  tvOS 14.0+  watchOS 7.0+

    
    
    func focusScope(_ namespace: Namespace.ID) -> some View
    

##  Parameters

`namespace`

    

A namespace identifier that SwiftUI can use to scope default focus
preferences.

## Return Value

A view that sets the namespace of descendants for default focus.

## Discussion

The returned view gets associated with the provided namespace. Pass this
namespace to `prefersDefaultFocus(_:in:)` and the `resetFocus` function.

## See Also

### Setting focus scope

`func focusSection() -> some View`

Indicates that the view’s frame and cohort of focusable descendants should be
used to guide focus movement.

Instance Method

# focusSection()

Indicates that the view’s frame and cohort of focusable descendants should be
used to guide focus movement.

macOS 13.0+  tvOS 15.0+

    
    
    func focusSection() -> some View
    

## Return Value

A view that can guide focus to its focusable descendents.

## Discussion

Use focus sections to customize SwiftUI’s behavior when the user moves focus
between views.

The following tvOS example places three buttons (“1”, “2”, and “3”) at the
upper left of the screen and three buttons (“A”, “B”, and “C”) at the bottom
right. By default, swiping right on the Siri Remote on any of the buttons in
the “1” - “3” group would do nothing, since the focus system finds no
focusable views directly to their right. But by declaring the `VStack` that
encloses buttons “A” - “C” as a focus section, the `VStack` can receive focus,
and deliver that focus to its first focusable child (button “A”). The example
puts a border on the `VStack` to illustrate this spatial arrangement.

Note that because the `VStack` containing buttons “1” - “3” does not declare
itself as a focus section, it is impossible to direct focus back to the left
from buttons “A” - “C”. None of those buttons has a focusable view — in this
case either a button or a `VStack` with the `focusSection()` modifier —
directly to its left.

Applying this modifier to a view affects focus behavior based on the style of
movement:

  * **Directional movement** : Navigating with Siri Remote gestures, arrow keys on a keyboard, or any other type of input that works in terms of cardinal directions (up, down, left, right) produces directional movement. When modified with `focusSection()`, the view’s frame becomes capable of accepting focus in order to direct it at its nearest focusable descendant in the direction of travel. In the earlier example, declaring the right-side `VStack` as a focus section allowed it to receive right-directed focus from the buttons on the left.

  * **Sequential movement** : Navigating with a Digital Crown, the Tab key on a keyboard, or any other type of input that works in terms of the next or previous item in a sequence, produces sequential movement. When you use the `focusSection()` modifier, SwiftUI deviates from its default layout-based sequence to visit each of the modified view’s focusable descendants before resuming the default sequence. Within the set of focusable descendants, SwiftUI continues to visit views in layout order (leading-to-trailing, top-to-bottom).

`focusSection()` does not affect the focusability of the modified view. If the
modified view has no focusable descendants, then the modifier does nothing.

## See Also

### Setting focus scope

`func focusScope(Namespace.ID) -> some View`

Creates a focus scope that SwiftUI uses to limit default focus preferences.

Instance Method

# prefersDefaultFocus(_:in:)

Indicates that the view should receive focus by default for a given namespace.

macOS 12.0+  tvOS 14.0+  watchOS 7.0+

    
    
    func prefersDefaultFocus(
        _ prefersDefaultFocus: Bool = true,
        in namespace: Namespace.ID
    ) -> some View
    

##  Parameters

`prefersDefaultFocus`

    

A Boolean value that indicates whether this view prefers to receive focus by
default. The default value, `true`, causes the view to receive focus by
default.

`namespace`

    

The namespace associated with the focus scope within which this view prefers
default focus.

## Return Value

A modified view that sets whether it prefers to be focused by default.

## Discussion

This modifier sets the initial focus preference when no other view has focus.
Use the environment value `resetFocus` to force a reevaluation of default
focus at any time.

The following tvOS example shows three buttons, labeled “1”, “2”, and “3”, in
a `VStack`. By default, the “1” button would receive focus, because it is the
first child in the stack. However, the `prefersDefaultFocus(_:in:)` modifier
allows button “3” to receive default focus instead. Once the buttons are
visible, the user can move down to and focus the “Reset to default focus”
button. When the user activates this button, it uses the `ResetFocusAction` to
reevaluate default focus in the `mainNamespace`, which returns the focus to
button “3”.

The default focus preference is limited to the focusable ancestor that matches
the provided namespace. If multiple views express this preference, then
SwiftUI applies the current platform rules to determine which view receives
focus.

## See Also

### Controlling default focus

`func defaultFocus<V>(FocusState<V>.Binding, V, priority:
DefaultFocusEvaluationPriority) -> some View`

Defines a region of the window in which default focus is evaluated by
assigning a value to a given focus state binding.

`struct DefaultFocusEvaluationPriority`

Prioritizations for default focus preferences when evaluating where to move
focus in different circumstances.

Instance Method

# defaultFocus(_:_:priority:)

Defines a region of the window in which default focus is evaluated by
assigning a value to a given focus state binding.

iOS 17.0+  iPadOS 17.0+  macOS 13.0+  Mac Catalyst 17.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func defaultFocus<V>(
        _ binding: FocusState<V>.Binding,
        _ value: V,
        priority: DefaultFocusEvaluationPriority = .automatic
    ) -> some View where V : Hashable
    

##  Parameters

`binding`

    

A focus state binding to update when evaluating default focus in the modified
view hierarchy.

`value`

    

The value to set the binding to during evaluation.

`priority`

    

An indication of how to prioritize the preferred default focus target when
focus moves into the modified view hierarchy. The default value is
`automatic`, which means the preference will be given priority when focus is
being initialized or relocated programmatically, but not when responding to
user-directed navigation commands.

## Return Value

The modified view.

## Discussion

By default, SwiftUI evaluates default focus when the window first appears, and
when a focus state binding update moves focus automatically, but not when
responding to user-driven navigation commands.

Clients can override the default behavior by specifying an evaluation priority
of `userInitiated`, which causes SwiftUI to use the client’s preferred default
focus in response to user-driven focus navigation as well as automatic
changes.

In the following example, focus automatically goes to the second of the two
text fields when the view is first presented in the window.

## See Also

### Controlling default focus

`func prefersDefaultFocus(Bool, in: Namespace.ID) -> some View`

Indicates that the view should receive focus by default for a given namespace.

`struct DefaultFocusEvaluationPriority`

Prioritizations for default focus preferences when evaluating where to move
focus in different circumstances.

Structure

# DefaultFocusEvaluationPriority

Prioritizations for default focus preferences when evaluating where to move
focus in different circumstances.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    struct DefaultFocusEvaluationPriority

## Topics

### Getting the priorities

`static let automatic: DefaultFocusEvaluationPriority`

Use the default focus preference when focus moves into the affected branch
automatically, but ignore it when the movement is driven by a user-initiated
navigation command.

`static let userInitiated: DefaultFocusEvaluationPriority`

Always use the default focus preference when focus moves into the affected
branch.

## Relationships

### Conforms To

  * `Sendable`

## See Also

### Controlling default focus

`func prefersDefaultFocus(Bool, in: Namespace.ID) -> some View`

Indicates that the view should receive focus by default for a given namespace.

`func defaultFocus<V>(FocusState<V>.Binding, V, priority:
DefaultFocusEvaluationPriority) -> some View`

Defines a region of the window in which default focus is evaluated by
assigning a value to a given focus state binding.

Instance Property

# resetFocus

An action that requests the focus system to reevaluate default focus.

macOS 12.0+  tvOS 14.0+  watchOS 7.0+

    
    
    var resetFocus: ResetFocusAction { get }

## Discussion

Get this environment value and call and call it as a function to force a
default focus reevaluation at runtime.

## See Also

### Resetting focus

`struct ResetFocusAction`

An environment value that provides the ability to reevaluate default focus.

Structure

# ResetFocusAction

An environment value that provides the ability to reevaluate default focus.

macOS 12.0+  tvOS 14.0+  watchOS 7.0+

    
    
    struct ResetFocusAction

## Overview

Get the `resetFocus` environment value and call it as a function to force a
default focus reevaluation at runtime.

## Topics

### Calling the action

`func callAsFunction(in: Namespace.ID)`

Asks the focus sytem to reevaluate the default focus item.

## See Also

### Resetting focus

`var resetFocus: ResetFocusAction`

An action that requests the focus system to reevaluate default focus.

Instance Method

# focusEffectDisabled(_:)

Adds a condition that controls whether this view can display focus effects,
such as a default focus ring or hover effect.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func focusEffectDisabled(_ disabled: Bool = true) -> some View
    

##  Parameters

`disabled`

    

A Boolean value that determines whether this view can display focus effects.

## Return Value

A view that controls whether focus effects can be displayed in this view.

## Discussion

The higher views in a view hierarchy can override the value you set on this
view. In the following example, the button does not display a focus effect
because the outer `focusEffectDisabled(_:)` modifier overrides the inner one:

## See Also

### Configuring effects

`var isFocusEffectEnabled: Bool`

A Boolean value that indicates whether the view associated with this
environment allows focus effects to be displayed.

Instance Property

# isFocusEffectEnabled

A Boolean value that indicates whether the view associated with this
environment allows focus effects to be displayed.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var isFocusEffectEnabled: Bool { get set }

## Discussion

The default value is `true`.

## See Also

### Configuring effects

`func focusEffectDisabled(Bool) -> some View`

Adds a condition that controls whether this view can display focus effects,
such as a default focus ring or hover effect.

