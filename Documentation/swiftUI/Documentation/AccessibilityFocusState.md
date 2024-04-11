Initializer

# init()

Creates a new accessibility focus state of the type you provide.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init<T>() where Value == T?, T : Hashable

## See Also

### Creating a focus state

`init()`

Creates a new accessibility focus state for a Boolean value.

`init<T>(for: AccessibilityTechnologies)`

Creates a new accessibility focus state of the type and using the
accessibility technologies you specify.

`init(for: AccessibilityTechnologies)`

Creates a new accessibility focus state for a Boolean value, using the
accessibility technologies you specify.

Initializer

# init()

Creates a new accessibility focus state for a Boolean value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init() where Value == Bool

## See Also

### Creating a focus state

`init<T>()`

Creates a new accessibility focus state of the type you provide.

`init<T>(for: AccessibilityTechnologies)`

Creates a new accessibility focus state of the type and using the
accessibility technologies you specify.

`init(for: AccessibilityTechnologies)`

Creates a new accessibility focus state for a Boolean value, using the
accessibility technologies you specify.

Initializer

# init(for:)

Creates a new accessibility focus state of the type and using the
accessibility technologies you specify.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init<T>(for technologies: AccessibilityTechnologies) where Value == T?, T : Hashable

##  Parameters

`technologies`

    

One or more of the available `AccessibilityTechnologies`.

## See Also

### Creating a focus state

`init<T>()`

Creates a new accessibility focus state of the type you provide.

`init()`

Creates a new accessibility focus state for a Boolean value.

`init(for: AccessibilityTechnologies)`

Creates a new accessibility focus state for a Boolean value, using the
accessibility technologies you specify.

Initializer

# init(for:)

Creates a new accessibility focus state for a Boolean value, using the
accessibility technologies you specify.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init(for technologies: AccessibilityTechnologies) where Value == Bool

##  Parameters

`technologies`

    

One of the available `AccessibilityTechnologies`.

## See Also

### Creating a focus state

`init<T>()`

Creates a new accessibility focus state of the type you provide.

`init()`

Creates a new accessibility focus state for a Boolean value.

`init<T>(for: AccessibilityTechnologies)`

Creates a new accessibility focus state of the type and using the
accessibility technologies you specify.

Instance Property

# projectedValue

A projection of the state value that can be used to establish bindings between
view content and accessibility focus placement.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var projectedValue: AccessibilityFocusState<Value>.Binding { get }

## Discussion

Use `projectedValue` in conjunction with `accessibilityFocused(_:equals:)` to
establish bindings between view content and accessibility focus placement.

## See Also

### Getting the state

`var wrappedValue: Value`

The current state value, taking into account whatever bindings might be in
effect due to the current location of focus.

`struct Binding`

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

### Getting the state

`var projectedValue: AccessibilityFocusState<Value>.Binding`

A projection of the state value that can be used to establish bindings between
view content and accessibility focus placement.

`struct Binding`

Structure

# AccessibilityFocusState.Binding

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    @propertyWrapper @frozen
    struct Binding

## Topics

### Getting the state

`var projectedValue: AccessibilityFocusState<Value>.Binding`

The currently focused element.

`var wrappedValue: Value`

The underlying value referenced by the bound property.

## See Also

### Getting the state

`var projectedValue: AccessibilityFocusState<Value>.Binding`

A projection of the state value that can be used to establish bindings between
view content and accessibility focus placement.

`var wrappedValue: Value`

The current state value, taking into account whatever bindings might be in
effect due to the current location of focus.

