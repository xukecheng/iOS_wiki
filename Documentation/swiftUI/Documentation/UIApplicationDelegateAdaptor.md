Initializer

# init(_:)

Creates a UIKit app delegate adaptor.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  tvOS 14.0+  visionOS 1.0+

    
    
    @MainActor
    init(_ delegateType: DelegateType.Type = DelegateType.self)

##  Parameters

`delegateType`

    

The type of application delegate that you define in your app, which conforms
to the `UIApplicationDelegate` protocol.

## Discussion

Call this initializer indirectly by creating a property with the
`UIApplicationDelegateAdaptor` property wrapper from inside your `App`
declaration:

SwiftUI initializes the delegate and manages its lifetime, calling upon it to
handle application delegate callbacks.

If you want SwiftUI to put the instantiated delegate in the `Environment`,
make sure the delegate class also conforms to the `ObservableObject` protocol.
That causes SwiftUI to invoke the `init(_:)` initializer rather than this one.

## See Also

### Creating a delegate adaptor

`init(DelegateType.Type)`

Creates a UIKit app delegate adaptor using a delegate that’s an observable
object.

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`ObservableObject`, and `DelegateType` conforms to `UIApplicationDelegate`.

`init(DelegateType.Type)`

Creates a UIKit app delegate adaptor using an observable delegate.

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`Observable`, and `DelegateType` conforms to `UIApplicationDelegate`.

Initializer

# init(_:)

Creates a UIKit app delegate adaptor using a delegate that’s an observable
object.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  tvOS 14.0+  visionOS 1.0+

    
    
    @MainActor
    init(_ delegateType: DelegateType.Type = DelegateType.self)

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`ObservableObject`, and `DelegateType` conforms to `UIApplicationDelegate`.

##  Parameters

`delegateType`

    

The type of application delegate that you define in your app, which conforms
to the `UIApplicationDelegate` and `ObservableObject` protocols.

## Discussion

Call this initializer indirectly by creating a property with the
`UIApplicationDelegateAdaptor` property wrapper from inside your `App`
declaration:

SwiftUI initializes the delegate and manages its lifetime, calling it as
needed to handle application delegate callbacks.

SwiftUI invokes this method when your app delegate conforms to the
`ObservableObject` protocol. In this case, SwiftUI automatically places the
delegate in the `Environment`. You can access such a delegate from any scene
or view in your app using the `EnvironmentObject` property wrapper:

If your delegate isn’t an observable object, SwiftUI invokes the `init(_:)`
initializer rather than this one, and doesn’t put the delegate instance in the
environment.

## See Also

### Creating a delegate adaptor

`init(DelegateType.Type)`

Creates a UIKit app delegate adaptor.

`init(DelegateType.Type)`

Creates a UIKit app delegate adaptor using an observable delegate.

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`Observable`, and `DelegateType` conforms to `UIApplicationDelegate`.

Initializer

# init(_:)

Creates a UIKit app delegate adaptor using an observable delegate.

iOS 17.0+  iPadOS 17.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS 1.0+

    
    
    @MainActor
    init(_ delegateType: DelegateType.Type = DelegateType.self)

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`Observable`, and `DelegateType` conforms to `UIApplicationDelegate`.

##  Parameters

`delegateType`

    

The type of application delegate that you define in your app, which conforms
to the `UIApplicationDelegate` and `Observable` protocols.

## Discussion

Call this initializer indirectly by creating a property with the
`UIApplicationDelegateAdaptor` property wrapper from inside your `App`
declaration:

SwiftUI initializes the delegate and manages its lifetime, calling it as
needed to handle application delegate callbacks.

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

Creates a UIKit app delegate adaptor.

`init(DelegateType.Type)`

Creates a UIKit app delegate adaptor using a delegate that’s an observable
object.

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`ObservableObject`, and `DelegateType` conforms to `UIApplicationDelegate`.

Instance Property

# projectedValue

A projection of the observed object that provides bindings to its properties.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  tvOS 14.0+  visionOS 1.0+

    
    
    @MainActor
    var projectedValue: ObservedObject<DelegateType>.Wrapper { get }

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`ObservableObject`, and `DelegateType` conforms to `UIApplicationDelegate`.

## Discussion

Use the projected value to get a binding to a value that the delegate
publishes. Access the projected value by prefixing the name of the delegate
instance with a dollar sign (`$`). For example, you might publish a Boolean
value in your application delegate:

If you declare the delegate in your `App` using the
`UIApplicationDelegateAdaptor` property wrapper, you can get the delegate that
SwiftUI instantiates from the environment and access a binding to its
published values from any view in your app:

## See Also

### Getting the delegate adaptor

`var wrappedValue: DelegateType`

The underlying app delegate.

Instance Property

# wrappedValue

The underlying app delegate.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  tvOS 14.0+  visionOS 1.0+

    
    
    @MainActor
    var wrappedValue: DelegateType { get }

## See Also

### Getting the delegate adaptor

`var projectedValue: ObservedObject<DelegateType>.Wrapper`

A projection of the observed object that provides bindings to its properties.

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`ObservableObject`, and `DelegateType` conforms to `UIApplicationDelegate`.

