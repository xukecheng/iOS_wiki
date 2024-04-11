Initializer

# init(_:)

Creates an `WKApplicationDelegateAdaptor` using a WatchKit Application
Delegate.

watchOS 7.0+

    
    
    @MainActor
    init(_ delegateType: DelegateType.Type = DelegateType.self)

##  Parameters

`delegate`

    

the type of `WKApplicationDelegate` to use.

## Discussion

The framework will initialize the provided delegate and manage its lifetime,
calling out to it when appropriate after performing its own work.

## See Also

### Creating a delegate adaptor

`init(DelegateType.Type)`

Creates an `WKApplicationDelegateAdaptor` using a WatchKit Application
Delegate.

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`ObservableObject`, and `DelegateType` conforms to `WKApplicationDelegate`.

`init(DelegateType.Type)`

Creates an `WKApplicationDelegateAdaptor` using a WatchKit Application
Delegate.

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`Observable`, and `DelegateType` conforms to `WKApplicationDelegate`.

Initializer

# init(_:)

Creates an `WKApplicationDelegateAdaptor` using a WatchKit Application
Delegate.

watchOS 7.0+

    
    
    @MainActor
    init(_ delegateType: DelegateType.Type = DelegateType.self)

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`ObservableObject`, and `DelegateType` conforms to `WKApplicationDelegate`.

##  Parameters

`delegate`

    

the type of `WKApplicationDelegate` to use.

## Discussion

The framework will initialize the provided delegate and manage its lifetime,
calling out to it when appropriate after performing its own work.

Note

the instantiated delegate will be placed in the Environment and may be
accessed by using the `@EnvironmentObject` property wrapper in the view
hierarchy.

## See Also

### Creating a delegate adaptor

`init(DelegateType.Type)`

Creates an `WKApplicationDelegateAdaptor` using a WatchKit Application
Delegate.

`init(DelegateType.Type)`

Creates an `WKApplicationDelegateAdaptor` using a WatchKit Application
Delegate.

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`Observable`, and `DelegateType` conforms to `WKApplicationDelegate`.

Initializer

# init(_:)

Creates an `WKApplicationDelegateAdaptor` using a WatchKit Application
Delegate.

watchOS 10.0+

    
    
    @MainActor
    init(_ delegateType: DelegateType.Type = DelegateType.self)

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`Observable`, and `DelegateType` conforms to `WKApplicationDelegate`.

##  Parameters

`delegate`

    

the type of `WKApplicationDelegate` to use.

## Discussion

The framework will initialize the provided delegate and manage its lifetime,
calling out to it when appropriate after performing its own work.

Note

the instantiated delegate will be placed in the Environment and may be
accessed by using the `@Environment` property wrapper in the view hierarchy.

## See Also

### Creating a delegate adaptor

`init(DelegateType.Type)`

Creates an `WKApplicationDelegateAdaptor` using a WatchKit Application
Delegate.

`init(DelegateType.Type)`

Creates an `WKApplicationDelegateAdaptor` using a WatchKit Application
Delegate.

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`ObservableObject`, and `DelegateType` conforms to `WKApplicationDelegate`.

Instance Property

# projectedValue

A projection of the observed object that creates bindings to its properties
using dynamic member lookup.

watchOS 7.0+

    
    
    @MainActor
    var projectedValue: ObservedObject<DelegateType>.Wrapper { get }

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`ObservableObject`, and `DelegateType` conforms to `WKApplicationDelegate`.

## Discussion

Use the projected value to pass a binding value down a view hierarchy. To get
the `projectedValue`, prefix the property variable with `$`.

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

A projection of the observed object that creates bindings to its properties
using dynamic member lookup.

Available when `DelegateType` inherits `NSObject`, `DelegateType` conforms to
`ObservableObject`, and `DelegateType` conforms to `WKApplicationDelegate`.

