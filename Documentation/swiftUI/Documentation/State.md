Initializer

# init(wrappedValue:)

Creates a state property that stores an initial wrapped value.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(wrappedValue value: Value)

##  Parameters

`value`

    

An initial value to store in the state property.

## Discussion

You don’t call this initializer directly. Instead, SwiftUI calls it for you
when you declare a property with the `@State` attribute and provide an initial
value:

SwiftUI initializes the state’s storage only once for each container instance
that you declare. In the above code, SwiftUI creates `isPlaying` only the
first time it initializes a particular instance of `MyView`. On the other
hand, each instance of `MyView` creates a distinct instance of the state. For
example, each of the views in the following `VStack` has its own `isPlaying`
value:

## See Also

### Creating a state

`init(initialValue: Value)`

Creates a state property that stores an initial value.

`init()`

Creates a state property without an initial value.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

Initializer

# init(initialValue:)

Creates a state property that stores an initial value.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(initialValue value: Value)

##  Parameters

`value`

    

An initial value to store in the state property.

## Discussion

This initializer has the same behavior as the `init(wrappedValue:)`
initializer. See that initializer for more information.

## See Also

### Creating a state

`init(wrappedValue: Value)`

Creates a state property that stores an initial wrapped value.

`init()`

Creates a state property without an initial value.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

Initializer

# init()

Creates a state property without an initial value.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init()

Available when `Value` conforms to `ExpressibleByNilLiteral`.

## Discussion

This initializer behaves like the `init(wrappedValue:)` initializer with an
input of `nil`. See that initializer for more information.

## See Also

### Creating a state

`init(wrappedValue: Value)`

Creates a state property that stores an initial wrapped value.

`init(initialValue: Value)`

Creates a state property that stores an initial value.

Instance Property

# wrappedValue

The underlying value referenced by the state variable.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var wrappedValue: Value { get nonmutating set }

## Discussion

This property provides primary access to the value’s data. However, you don’t
typically access `wrappedValue` explicitly. Instead, you gain access to the
wrapped value by referring to the property variable that you create with the
`@State` attribute.

In the following example, the button’s label depends on the value of
`isPlaying` and the button’s action toggles the value of `isPlaying`. Both of
these accesses implicitly access the state property’s wrapped value:

## See Also

### Getting the value

`var projectedValue: Binding<Value>`

A binding to the state value.

Instance Property

# projectedValue

A binding to the state value.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var projectedValue: Binding<Value> { get }

## Discussion

Use the projected value to get a `Binding` to the stored value. The binding
provides a two-way connection to the stored value. To access the
`projectedValue`, prefix the property variable with a dollar sign (`$`).

In the following example, `PlayerView` projects a binding of the state
property `isPlaying` to the `PlayButton` view using `$isPlaying`. That enables
the play button to both read and write the value:

## See Also

### Getting the value

`var wrappedValue: Value`

The underlying value referenced by the state variable.

