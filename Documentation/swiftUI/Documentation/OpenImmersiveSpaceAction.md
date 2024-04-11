Instance Method

# callAsFunction(id:)

Presents an immersive space for the scene with the specified identifier.

visionOS 1.0+

    
    
    @discardableResult @MainActor
    func callAsFunction(id: String) async -> OpenImmersiveSpaceAction.Result

##  Parameters

`id`

    

The identifier of the immersive space to present.

## Discussion

Don’t call this method directly. SwiftUI calls it when you call the
`openImmersiveSpace` action with a string identifier:

For information about how Swift uses the `callAsFunction()` method to simplify
call site syntax, see Methods with Special Names in _The Swift Programming
Language_.

## See Also

### Calling the action

`func callAsFunction<D>(id: String, value: D) async ->
OpenImmersiveSpaceAction.Result`

Presents the immersive space that your app defines for the specified
identifier and that handles the type of the presented value.

`func callAsFunction<D>(value: D) async -> OpenImmersiveSpaceAction.Result`

Presents the immersive space that handles the type of the presented value.

Instance Method

# callAsFunction(id:value:)

Presents the immersive space that your app defines for the specified
identifier and that handles the type of the presented value.

visionOS 1.0+

    
    
    @discardableResult
    func callAsFunction<D>(
        id: String,
        value: D
    ) async -> OpenImmersiveSpaceAction.Result where D : Decodable, D : Encodable, D : Hashable

##  Parameters

`id`

    

The identifier of the immersive space to present.

`value`

    

The value to present.

## Discussion

Don’t call this method directly. SwiftUI calls it when you call the
`openImmersiveSpace` action with a string identifier and a value:

For information about how Swift uses the `callAsFunction()` method to simplify
call site syntax, see Methods with Special Names in _The Swift Programming
Language_.

## See Also

### Calling the action

`func callAsFunction(id: String) async -> OpenImmersiveSpaceAction.Result`

Presents an immersive space for the scene with the specified identifier.

`func callAsFunction<D>(value: D) async -> OpenImmersiveSpaceAction.Result`

Presents the immersive space that handles the type of the presented value.

Instance Method

# callAsFunction(value:)

Presents the immersive space that handles the type of the presented value.

visionOS 1.0+

    
    
    @discardableResult @MainActor
    func callAsFunction<D>(value: D) async -> OpenImmersiveSpaceAction.Result where D : Decodable, D : Encodable, D : Hashable

##  Parameters

`value`

    

The value to present.

## Discussion

Don’t call this method directly. SwiftUI calls it when you call the
`openImmersiveSpace` action with a value:

For information about how Swift uses the `callAsFunction()` method to simplify
call site syntax, see Methods with Special Names in _The Swift Programming
Language_.

## See Also

### Calling the action

`func callAsFunction(id: String) async -> OpenImmersiveSpaceAction.Result`

Presents an immersive space for the scene with the specified identifier.

`func callAsFunction<D>(id: String, value: D) async ->
OpenImmersiveSpaceAction.Result`

Presents the immersive space that your app defines for the specified
identifier and that handles the type of the presented value.

Enumeration

# OpenImmersiveSpaceAction.Result

The outcome of an attempt to open an immersive space.

visionOS 1.0+

    
    
    enum Result

## Topics

### Getting the result

`case opened`

The immersive space opened.

`case userCancelled`

The immersive space didn’t open because the user cancelled the operation.

`case error`

The system was unable to open the immersive space.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

