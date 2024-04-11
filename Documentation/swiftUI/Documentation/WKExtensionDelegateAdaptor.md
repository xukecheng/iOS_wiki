Initializer

# init(_:)

Creates a WatchKit extension delegate adaptor.

watchOS 7.0+

    
    
    @MainActor
    init(_ delegateType: DelegateType.Type = DelegateType.self)

##  Parameters

`delegateType`

    

The type of extension delegate that you define in your app, which conforms to
the `WKExtensionDelegate` protocol.

## Discussion

Call this initializer indirectly by creating a property with the
`WKExtensionDelegateAdaptor` property wrapper from inside your `App`
declaration:

SwiftUI initializes the delegate and manages its lifetime, calling upon it to
handle extension delegate callbacks.

If you want SwiftUI to put the instantiated delegate in the `Environment`,
make sure the delegate class also conforms to the `ObservableObject` protocol.
That causes SwiftUI to invoke the `init(_:)` initializer rather than this one.

## See Also

### Creating a delegate adaptor

`init(DelegateType.Type)`

Creates a WatchKit extension delegate adaptor using a delegate that’s an
observable object.

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`ObservableObject`, and `DelegateType` conforms to `WKExtensionDelegate`.

`init(DelegateType.Type)`

Creates a WatchKit extension delegate adaptor using an observable delegate.

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`Observable`, and `DelegateType` conforms to `WKExtensionDelegate`.

Initializer

# init(_:)

Creates a WatchKit extension delegate adaptor using a delegate that’s an
observable object.

watchOS 7.0+

    
    
    @MainActor
    init(_ delegateType: DelegateType.Type = DelegateType.self)

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`ObservableObject`, and `DelegateType` conforms to `WKExtensionDelegate`.

##  Parameters

`delegateType`

    

The type of extension delegate that you define in your app, which conforms to
the `WKExtensionDelegate` and `ObservableObject` protocols.

## Discussion

Call this initializer indirectly by creating a property with the
`WKExtensionDelegateAdaptor` property wrapper from inside your `App`
declaration:

SwiftUI initializes the delegate and manages its lifetime, calling it as
needed to handle extension delegate callbacks.

SwiftUI invokes this method when your extension delegate conforms to the
`ObservableObject` protocol. In this case, SwiftUI automatically places the
delegate in the `Environment`. You can access such a delegate from any scene
or view in your app using the `EnvironmentObject` property wrapper:

If your delegate isn’t an observable object, SwiftUI invokes the `init(_:)`
initializer rather than this one, and doesn’t put the delegate instance in the
environment.

## See Also

### Creating a delegate adaptor

`init(DelegateType.Type)`

Creates a WatchKit extension delegate adaptor.

`init(DelegateType.Type)`

Creates a WatchKit extension delegate adaptor using an observable delegate.

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`Observable`, and `DelegateType` conforms to `WKExtensionDelegate`.

Initializer

# init(_:)

Creates a WatchKit extension delegate adaptor using an observable delegate.

watchOS 10.0+

    
    
    @MainActor
    init(_ delegateType: DelegateType.Type = DelegateType.self)

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`Observable`, and `DelegateType` conforms to `WKExtensionDelegate`.

##  Parameters

`delegateType`

    

The type of extension delegate that you define in your app, which conforms to
the `WKExtensionDelegate` and `Observable` protocols.

## Discussion

Call this initializer indirectly by creating a property with the
`WKExtensionDelegateAdaptor` property wrapper from inside your `App`
declaration:

SwiftUI initializes the delegate and manages its lifetime, calling it as
needed to handle extension delegate callbacks.

SwiftUI invokes this method when your app delegate conforms to the
`Observable` protocol. In this case, SwiftUI automatically places the delegate
in the `Environment`. You can access such a delegate from any scene or view in
your app using the `Environment` property wrapper:

If your delegate isn’t observable, SwiftUI invokes the `init(_:)` initializer
rather than this one, and doesn’t put the delegate instance in the
environment.

## See Also

### Creating a delegate adaptor

`init(DelegateType.Type)`

Creates a WatchKit extension delegate adaptor.

`init(DelegateType.Type)`

Creates a WatchKit extension delegate adaptor using a delegate that’s an
observable object.

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`ObservableObject`, and `DelegateType` conforms to `WKExtensionDelegate`.

Instance Property

# projectedValue

A projection of the observed object that provides bindings to its properties.

watchOS 7.0+

    
    
    @MainActor
    var projectedValue: ObservedObject<DelegateType>.Wrapper { get }

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`ObservableObject`, and `DelegateType` conforms to `WKExtensionDelegate`.

## Discussion

Use the projected value to get a binding to a value that the delegate
publishes. Access the projected value by prefixing the name of the delegate
instance with a dollar sign (`$`). For example, you might publish a Boolean
value in your extension delegate:

If you declare the delegate in your `App` using the
`WKExtensionDelegateAdaptor` property wrapper, you can get the delegate that
SwiftUI instantiates from the environment and access a binding to its
published values from any view in your extension:

## See Also

### Getting the delegate adaptor

`var wrappedValue: DelegateType`

The underlying delegate.

Instance Property

# wrappedValue

The underlying delegate.

watchOS 7.0+

    
    
    @MainActor
    var wrappedValue: DelegateType { get }

## See Also

### Getting the delegate adaptor

`var projectedValue: ObservedObject<DelegateType>.Wrapper`

A projection of the observed object that provides bindings to its properties.

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`ObservableObject`, and `DelegateType` conforms to `WKExtensionDelegate`.

