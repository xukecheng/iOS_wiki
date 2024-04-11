Instance Method

# callAsFunction(id:)

Opens a window that’s associated with the specified identifier.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    func callAsFunction(id: String)

##  Parameters

`id`

    

The identifier of the scene to present.

## Discussion

Don’t call this method directly. SwiftUI calls it when you call the
`openWindow` action with an identifier:

For information about how Swift uses the `callAsFunction()` method to simplify
call site syntax, see Methods with Special Names in _The Swift Programming
Language_.

## See Also

### Calling the action

`func callAsFunction<D>(id: String, value: D)`

Opens a window defined by the window group that presents the specified value
type and that’s associated with the specified identifier.

`func callAsFunction<D>(value: D)`

Opens a window defined by a window group that presents the type of the
specified value.

Instance Method

# callAsFunction(id:value:)

Opens a window defined by the window group that presents the specified value
type and that’s associated with the specified identifier.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    func callAsFunction<D>(
        id: String,
        value: D
    ) where D : Decodable, D : Encodable, D : Hashable

##  Parameters

`id`

    

The identifier of the scene to present.

`value`

    

The value to present.

## Discussion

Don’t call this method directly. SwiftUI calls it when you call the
`openWindow` action with an identifier and a value:

For information about how Swift uses the `callAsFunction()` method to simplify
call site syntax, see Methods with Special Names in _The Swift Programming
Language_.

## See Also

### Calling the action

`func callAsFunction(id: String)`

Opens a window that’s associated with the specified identifier.

`func callAsFunction<D>(value: D)`

Opens a window defined by a window group that presents the type of the
specified value.

Instance Method

# callAsFunction(value:)

Opens a window defined by a window group that presents the type of the
specified value.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    func callAsFunction<D>(value: D) where D : Decodable, D : Encodable, D : Hashable

##  Parameters

`value`

    

The value to present.

## Discussion

Don’t call this method directly. SwiftUI calls it when you call the
`openWindow` action with a value:

For information about how Swift uses the `callAsFunction()` method to simplify
call site syntax, see Methods with Special Names in _The Swift Programming
Language_.

## See Also

### Calling the action

`func callAsFunction(id: String)`

Opens a window that’s associated with the specified identifier.

`func callAsFunction<D>(id: String, value: D)`

Opens a window defined by the window group that presents the specified value
type and that’s associated with the specified identifier.

