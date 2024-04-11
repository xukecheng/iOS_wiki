Initializer

# init(_:)

Creates an environment property to read the specified key path.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(_ keyPath: KeyPath<EnvironmentValues, Value>)

##  Parameters

`keyPath`

    

A key path to a specific resulting value.

## Discussion

Don’t call this initializer directly. Instead, declare a property with the
`Environment` property wrapper, and provide the key path of the environment
value that the property should reflect:

SwiftUI automatically updates any parts of `MyView` that depend on the
property when the associated environment value changes. You can’t modify the
environment value using a property like this. Instead, use the
`environment(_:_:)` view modifier on a view to set a value for a view
hierarchy.

## See Also

### Creating an environment instance

`init(Value.Type)`

Creates an environment property to read an observable object from the
environment.

`init<T>(T.Type)`

Creates an environment property to read an observable object from the
environment, returning `nil` if no corresponding object has been set in the
current view’s environment.

Initializer

# init(_:)

Creates an environment property to read an observable object from the
environment.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init(_ objectType: Value.Type) where Value : AnyObject, Value : Observable

##  Parameters

`objectType`

    

The type of the `Observable` object to read from the environment.

## Discussion

Important

This initializer only accepts objects conforming to the `Observable` protocol.
For reading environment objects that conform to `ObservableObject`, use
`EnvironmentObject` instead.

Don’t call this initializer directly. Instead, declare a property with the
`Environment` property wrapper, passing the object’s type to the wrapper
(using this syntax, the object type can be omitted from the end of property
declaration):

Warning

If no object has been set in the view’s environment, this property will issue
a fatal error when accessed. To safely check for the existence of an
environment object, initialize the environment property with an optional
object type instead.

SwiftUI automatically updates any parts of `MyView` that depend on the
property when the associated environment object changes.

You can’t modify the environment object using a property like this. Instead,
use the `environment(_:)` view modifier on a view to set an object for a view
hierarchy.

## See Also

### Creating an environment instance

`init(KeyPath<EnvironmentValues, Value>)`

Creates an environment property to read the specified key path.

`init<T>(T.Type)`

Creates an environment property to read an observable object from the
environment, returning `nil` if no corresponding object has been set in the
current view’s environment.

Initializer

# init(_:)

Creates an environment property to read an observable object from the
environment, returning `nil` if no corresponding object has been set in the
current view’s environment.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init<T>(_ objectType: T.Type) where Value == T?, T : AnyObject, T : Observable

##  Parameters

`objectType`

    

The type of the `Observable` object to read from the environment.

## Discussion

Important

This initializer only accepts objects conforming to the `Observable` protocol.
For reading environment objects that conform to `ObservableObject`, use
`EnvironmentObject` instead.

Don’t call this initializer directly. Instead, declare an optional property
with the `Environment` property wrapper, passing the object’s type to the
wrapper:

If no object has been set in the view’s environment, this property will return
`nil` as its wrapped value.

SwiftUI automatically updates any parts of `MyView` that depend on the
property when the associated environment object changes.

You can’t modify the environment object using a property like this. Instead,
use the `environment(_:)` view modifier on a view to set an object for a view
hierarchy.

## See Also

### Creating an environment instance

`init(KeyPath<EnvironmentValues, Value>)`

Creates an environment property to read the specified key path.

`init(Value.Type)`

Creates an environment property to read an observable object from the
environment.

Instance Property

# wrappedValue

The current value of the environment property.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var wrappedValue: Value { get }

## Discussion

The wrapped value property provides primary access to the value’s data.
However, you don’t access `wrappedValue` directly. Instead, you read the
property variable created with the `Environment` property wrapper:

