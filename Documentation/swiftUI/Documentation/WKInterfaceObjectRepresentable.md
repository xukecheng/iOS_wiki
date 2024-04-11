Instance Method

# makeWKInterfaceObject(context:)

Creates a WatchKit interface object and configures its initial state.

watchOS 6.0+

    
    
    @MainActor
    func makeWKInterfaceObject(context: Self.Context) -> Self.WKInterfaceObjectType

**Required**

##  Parameters

`context`

    

A context structure containing information about the current state of the
system.

## Return Value

Your interface object configured with the provided information.

## Discussion

You must implement this method and use it to create your interface object.
Configure the object using your app’s current data and contents of the
`context` parameter. The system calls this method only once, when it creates
your interface object for the first time. For all subsequent updates, the
system calls the `updateWKInterfaceObject(_:context:)` method.

## See Also

### Creating and updating the interface object

`func updateWKInterfaceObject(Self.WKInterfaceObjectType, context:
Self.Context)`

Updates the presented WatchKit interface object (and its coordinator) to the
latest configuration.

**Required**

` typealias Context`

Instance Method

# updateWKInterfaceObject(_:context:)

Updates the presented WatchKit interface object (and its coordinator) to the
latest configuration.

watchOS 6.0+

    
    
    @MainActor
    func updateWKInterfaceObject(
        _ wkInterfaceObject: Self.WKInterfaceObjectType,
        context: Self.Context
    )

**Required**

##  Parameters

`wkInterfaceObject`

    

Your custom interface object.

`context`

    

A context structure containing information about the current state of the
system.

## Discussion

When the state of your app changes, SwiftUI updates the portions of your
interface affected by those changes. SwiftUI calls this method for any changes
affecting the corresponding interface object. Use this method to update the
configuration of your object to match the new state information provided in
the `context` parameter.

## See Also

### Creating and updating the interface object

`func makeWKInterfaceObject(context: Self.Context) ->
Self.WKInterfaceObjectType`

Creates a WatchKit interface object and configures its initial state.

**Required**

` typealias Context`

Type Alias

# WKInterfaceObjectRepresentable.Context

watchOS 6.0+

    
    
    typealias Context = WKInterfaceObjectRepresentableContext<Self>

## See Also

### Creating and updating the interface object

`func makeWKInterfaceObject(context: Self.Context) ->
Self.WKInterfaceObjectType`

Creates a WatchKit interface object and configures its initial state.

**Required**

` func updateWKInterfaceObject(Self.WKInterfaceObjectType, context:
Self.Context)`

Updates the presented WatchKit interface object (and its coordinator) to the
latest configuration.

**Required**

Type Method

# dismantleWKInterfaceObject(_:coordinator:)

Cleans up the presented WatchKit interface object (and its coordinator) in
anticipation of their removal.

watchOS 6.0+

    
    
    @MainActor
    static func dismantleWKInterfaceObject(
        _ wkInterfaceObject: Self.WKInterfaceObjectType,
        coordinator: Self.Coordinator
    )

**Required** Default implementation provided.

##  Parameters

`wkInterfaceObject`

    

Your custom interface object.

`coordinator`

    

The custom coordinator instance you use to communicate changes back to
SwiftUI. If you do not use a custom coordinator, the system provides a default
instance.

## Discussion

Use this method to perform additional clean-up work related to your custom
interface object. For example, you might use this method to remove observers
or update other parts of your SwiftUI interface.

## Default Implementations

### WKInterfaceObjectRepresentable Implementations

`static func dismantleWKInterfaceObject(Self.WKInterfaceObjectType,
coordinator: Self.Coordinator)`

Cleans up the presented interface object (and coordinator) in anticipation of
their removal.

Instance Method

# makeCoordinator()

Creates the custom instance that you use to communicate changes from your
interface object to other parts of your SwiftUI interface.

watchOS 6.0+

    
    
    @MainActor
    func makeCoordinator() -> Self.Coordinator

**Required** Default implementation provided.

## Discussion

Implement this method if changes to your interface object might affect other
parts of your app. In your implementation, create a custom Swift instance that
can communicate with other parts of your interface. For example, you might
provide an instance that binds its variables to SwiftUI properties, causing
the two to remain synchronized. If your interface object doesn’t interact with
other parts of your app, providing a coordinator is unnecessary.

SwiftUI calls this method before calling the `makeWKInterfaceObject(context:)`
method. The system provides your coordinator either directly or as part of a
context structure when calling the other methods of your representable
instance.

## Default Implementations

### WKInterfaceObjectRepresentable Implementations

`func makeCoordinator() -> Self.Coordinator`

Creates the custom instance that you use to communicate changes from your
interface object to other parts of your SwiftUI interface.

Available when `Coordinator` is `()`.

## See Also

### Providing a custom coordinator object

`associatedtype Coordinator = Void`

A type to coordinate with the WatchKit interface object.

**Required**

` associatedtype WKInterfaceObjectType : WKInterfaceObject`

The type of WatchKit interface object to be presented.

**Required**

Associated Type

# Coordinator

A type to coordinate with the WatchKit interface object.

watchOS 6.0+

    
    
    associatedtype Coordinator = Void

**Required**

## See Also

### Providing a custom coordinator object

`func makeCoordinator() -> Self.Coordinator`

Creates the custom instance that you use to communicate changes from your
interface object to other parts of your SwiftUI interface.

**Required** Default implementation provided.

`associatedtype WKInterfaceObjectType : WKInterfaceObject`

The type of WatchKit interface object to be presented.

**Required**

Associated Type

# WKInterfaceObjectType

The type of WatchKit interface object to be presented.

watchOS 6.0+

    
    
    associatedtype WKInterfaceObjectType : WKInterfaceObject

**Required**

## See Also

### Providing a custom coordinator object

`func makeCoordinator() -> Self.Coordinator`

Creates the custom instance that you use to communicate changes from your
interface object to other parts of your SwiftUI interface.

**Required** Default implementation provided.

`associatedtype Coordinator = Void`

A type to coordinate with the WatchKit interface object.

**Required**

