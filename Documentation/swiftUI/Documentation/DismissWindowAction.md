Instance Method

# callAsFunction()

Dismisses the current window.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func callAsFunction()

## Discussion

Don’t call this method directly. SwiftUI calls it when you call the
`dismissWindow` action:

For information about how Swift uses the `callAsFunction()` method to simplify
call site syntax, see Methods with Special Names in _The Swift Programming
Language_.

## See Also

### Calling the action

`func callAsFunction(id: String)`

Dismisses the window that’s associated with the specified identifier.

`func callAsFunction<D>(id: String, value: D)`

Dismisses the window defined by the window group that is presenting the
specified value type and that’s associated with the specified identifier.

`func callAsFunction<D>(value: D)`

Dismisses the window defined by the window group that is presenting the
specified value type.

Instance Method

# callAsFunction(id:)

Dismisses the window that’s associated with the specified identifier.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func callAsFunction(id: String)

##  Parameters

`id`

    

The identifier of the scene to dismiss.

## Discussion

When the specified identifier represents a `WindowGroup`, all of the open
windows in that group will be dismissed. For dismissing a single window
associated to a `WindowGroup` scene, use `dismissWindow(value:)` or
`dismissWindow(id:value:)`.

Don’t call this method directly. SwiftUI calls it when you call the
`dismissWindow` action with an identifier:

For information about how Swift uses the `callAsFunction()` method to simplify
call site syntax, see Methods with Special Names in _The Swift Programming
Language_.

## See Also

### Calling the action

`func callAsFunction()`

Dismisses the current window.

`func callAsFunction<D>(id: String, value: D)`

Dismisses the window defined by the window group that is presenting the
specified value type and that’s associated with the specified identifier.

`func callAsFunction<D>(value: D)`

Dismisses the window defined by the window group that is presenting the
specified value type.

Instance Method

# callAsFunction(id:value:)

Dismisses the window defined by the window group that is presenting the
specified value type and that’s associated with the specified identifier.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func callAsFunction<D>(
        id: String,
        value: D
    ) where D : Decodable, D : Encodable, D : Hashable

##  Parameters

`id`

    

The identifier of the scene to dismiss.

`value`

    

The value which is currently presented.

## Discussion

Don’t call this method directly. SwiftUI calls it when you call the
`dismissWindow` action with an identifier and a value:

For information about how Swift uses the `callAsFunction()` method to simplify
call site syntax, see Methods with Special Names in _The Swift Programming
Language_.

## See Also

### Calling the action

`func callAsFunction()`

Dismisses the current window.

`func callAsFunction(id: String)`

Dismisses the window that’s associated with the specified identifier.

`func callAsFunction<D>(value: D)`

Dismisses the window defined by the window group that is presenting the
specified value type.

Instance Method

# callAsFunction(value:)

Dismisses the window defined by the window group that is presenting the
specified value type.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func callAsFunction<D>(value: D) where D : Decodable, D : Encodable, D : Hashable

##  Parameters

`value`

    

The value which is currently presented.

## Discussion

If multiple windows match the provided value, then they all will be dismissed.
For dismissing a specific window in a specific group, use
`dismissWindow(id:value:)`.

Don’t call this method directly. SwiftUI calls it when you call the
`dismissWindow` action with an identifier and a value:

For information about how Swift uses the `callAsFunction()` method to simplify
call site syntax, see Methods with Special Names in _The Swift Programming
Language_.

## See Also

### Calling the action

`func callAsFunction()`

Dismisses the current window.

`func callAsFunction(id: String)`

Dismisses the window that’s associated with the specified identifier.

`func callAsFunction<D>(id: String, value: D)`

Dismisses the window defined by the window group that is presenting the
specified value type and that’s associated with the specified identifier.

