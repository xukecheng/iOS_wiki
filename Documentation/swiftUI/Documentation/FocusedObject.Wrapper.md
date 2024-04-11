Instance Subscript

# subscript(dynamicMember:)

Returns a binding to the value of a given key path.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    subscript<T>(dynamicMember keyPath: ReferenceWritableKeyPath<ObjectType, T>) -> Binding<T> { get }

##  Parameters

`keyPath`

    

A key path to a specific value on the wrapped object.

## Return Value

A new binding.

