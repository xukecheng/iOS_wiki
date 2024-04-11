Initializer

# init()

Creates an environment object.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init()

Instance Property

# wrappedValue

The underlying value referenced by the environment object.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @MainActor
    var wrappedValue: ObjectType { get }

## Discussion

This property provides primary access to the value’s data. However, you don’t
access `wrappedValue` directly. Instead, you use the property variable created
with the `EnvironmentObject` attribute.

When a mutable value changes, the new value is immediately available. However,
a view displaying the value is updated asynchronously and may not show the new
value immediately.

## See Also

### Getting the value

`var projectedValue: EnvironmentObject<ObjectType>.Wrapper`

A projection of the environment object that creates bindings to its properties
using dynamic member lookup.

`struct Wrapper`

A wrapper of the underlying environment object that can create bindings to its
properties using dynamic member lookup.

Instance Property

# projectedValue

A projection of the environment object that creates bindings to its properties
using dynamic member lookup.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @MainActor
    var projectedValue: EnvironmentObject<ObjectType>.Wrapper { get }

## Discussion

Use the projected value to pass an environment object down a view hierarchy.

## See Also

### Getting the value

`var wrappedValue: ObjectType`

The underlying value referenced by the environment object.

`struct Wrapper`

A wrapper of the underlying environment object that can create bindings to its
properties using dynamic member lookup.

Structure

# EnvironmentObject.Wrapper

A wrapper of the underlying environment object that can create bindings to its
properties using dynamic member lookup.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @dynamicMemberLookup @frozen
    struct Wrapper

## Topics

### Getting a binding value

`subscript<Subject>(dynamicMember _: ReferenceWritableKeyPath<ObjectType,
Subject>) -> Binding<Subject>`

Returns a binding to the resulting value of a given key path.

## See Also

### Getting the value

`var wrappedValue: ObjectType`

The underlying value referenced by the environment object.

`var projectedValue: EnvironmentObject<ObjectType>.Wrapper`

A projection of the environment object that creates bindings to its properties
using dynamic member lookup.

