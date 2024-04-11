Instance Property

# projectedValue

A projection of the binding value that returns a binding.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var projectedValue: FocusState<Value>.Binding { get }

## Discussion

Use the projected value to pass a binding value down a view hierarchy.

## See Also

### Inspecting the binding

`var wrappedValue: Value`

The underlying value referenced by the bound property.

Instance Property

# wrappedValue

The underlying value referenced by the bound property.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var wrappedValue: Value { get nonmutating set }

## See Also

### Inspecting the binding

`var projectedValue: FocusState<Value>.Binding`

A projection of the binding value that returns a binding.

