Initializer

# init()

Creates a focus state that binds to an optional type.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init<T>() where Value == T?, T : Hashable

## See Also

### Creating a focus state

`init()`

Creates a focus state that binds to a Boolean.

Initializer

# init()

Creates a focus state that binds to a Boolean.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init() where Value == Bool

## See Also

### Creating a focus state

`init<T>()`

Creates a focus state that binds to an optional type.

Instance Property

# projectedValue

A projection of the focus state value that returns a binding.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var projectedValue: FocusState<Value>.Binding { get }

## Discussion

When focus is outside any view that is bound to this state, the wrapped value
is `nil` for optional-typed state or `false` for Boolean state.

In the following example of a simple navigation sidebar, when the user presses
the Filter Sidebar Contents button, focus moves to the sidebar’s filter text
field. Conversely, if the user moves focus to the sidebar’s filter manually,
then the value of `isFiltering` automatically becomes `true`, and the sidebar
view updates.

## See Also

### Inspecting the focus state

`struct Binding`

A property wrapper type that can read and write a value that indicates the
current focus location.

`var wrappedValue: Value`

The current state value, taking into account whatever bindings might be in
effect due to the current location of focus.

Structure

# FocusState.Binding

A property wrapper type that can read and write a value that indicates the
current focus location.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    @frozen @propertyWrapper
    struct Binding

## Topics

### Inspecting the binding

`var projectedValue: FocusState<Value>.Binding`

A projection of the binding value that returns a binding.

`var wrappedValue: Value`

The underlying value referenced by the bound property.

## See Also

### Inspecting the focus state

`var projectedValue: FocusState<Value>.Binding`

A projection of the focus state value that returns a binding.

`var wrappedValue: Value`

The current state value, taking into account whatever bindings might be in
effect due to the current location of focus.

Instance Property

# wrappedValue

The current state value, taking into account whatever bindings might be in
effect due to the current location of focus.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var wrappedValue: Value { get nonmutating set }

## Discussion

When focus is not in any view that is bound to this state, the wrapped value
will be `nil` (for optional-typed state) or `false` (for `Bool`\- typed
state).

## See Also

### Inspecting the focus state

`var projectedValue: FocusState<Value>.Binding`

A projection of the focus state value that returns a binding.

`struct Binding`

A property wrapper type that can read and write a value that indicates the
current focus location.

