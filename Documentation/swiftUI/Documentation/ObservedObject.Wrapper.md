Instance Subscript

# subscript(dynamicMember:)

Gets a binding to the value of a specified key path.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    subscript<Subject>(dynamicMember keyPath: ReferenceWritableKeyPath<ObjectType, Subject>) -> Binding<Subject> { get }

##  Parameters

`keyPath`

    

A key path to a specific value.

## Return Value

A new binding.

