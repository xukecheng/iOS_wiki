Initializer

# init()

Creates a focused object.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init()

Instance Property

# projectedValue

A projection of the focused object that creates bindings to its properties
using dynamic member lookup.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    @MainActor
    var projectedValue: FocusedObject<ObjectType>.Wrapper? { get }

## Discussion

Use the projected value to pass a focused object down a view hierarchy.

## See Also

### Getting the value

`var wrappedValue: ObjectType?`

The underlying value referenced by the focused object.

`struct Wrapper`

A wrapper around the underlying focused object that can create bindings to its
properties using dynamic member lookup.

Instance Property

# wrappedValue

The underlying value referenced by the focused object.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    @MainActor
    var wrappedValue: ObjectType? { get }

## Discussion

This property provides primary access to the value’s data. However, you don’t
access `wrappedValue` directly. Instead, you use the property variable created
with the `FocusedObject` attribute.

When a mutable value changes, the new value is immediately available. However,
a view displaying the value is updated asynchronously and may not show the new
value immediately.

## See Also

### Getting the value

`var projectedValue: FocusedObject<ObjectType>.Wrapper?`

A projection of the focused object that creates bindings to its properties
using dynamic member lookup.

`struct Wrapper`

A wrapper around the underlying focused object that can create bindings to its
properties using dynamic member lookup.

Structure

# FocusedObject.Wrapper

A wrapper around the underlying focused object that can create bindings to its
properties using dynamic member lookup.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    @dynamicMemberLookup @frozen
    struct Wrapper

## Topics

### Accessing members

`subscript<T>(dynamicMember _: ReferenceWritableKeyPath<ObjectType, T>) ->
Binding<T>`

Returns a binding to the value of a given key path.

## See Also

### Getting the value

`var projectedValue: FocusedObject<ObjectType>.Wrapper?`

A projection of the focused object that creates bindings to its properties
using dynamic member lookup.

`var wrappedValue: ObjectType?`

The underlying value referenced by the focused object.

