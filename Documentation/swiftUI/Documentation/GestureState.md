Initializer

# init(initialValue:)

Creates a view state that’s derived from a gesture with an initial value.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(initialValue: Value)

##  Parameters

`initialValue`

    

An initial value for the gesture state property.

## See Also

### Creating a gesture state

`init(initialValue: Value, reset: (Value, inout Transaction) -> Void)`

Creates a view state that’s derived from a gesture with an initial state value
and a closure that provides a transaction to reset it.

`init(initialValue: Value, resetTransaction: Transaction)`

Creates a view state that’s derived from a gesture with an initial state value
and a transaction to reset it.

`init(reset: (Value, inout Transaction) -> Void)`

Creates a view state that’s derived from a gesture with a closure that
provides a transaction to reset it.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(resetTransaction: Transaction)`

Creates a view state that’s derived from a gesture with a transaction to reset
it.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(wrappedValue: Value)`

Creates a view state that’s derived from a gesture.

`init(wrappedValue: Value, reset: (Value, inout Transaction) -> Void)`

Creates a view state that’s derived from a gesture with a wrapped state value
and a closure that provides a transaction to reset it.

`init(wrappedValue: Value, resetTransaction: Transaction)`

Creates a view state that’s derived from a gesture with a wrapped state value
and a transaction to reset it.

Initializer

# init(initialValue:reset:)

Creates a view state that’s derived from a gesture with an initial state value
and a closure that provides a transaction to reset it.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        initialValue: Value,
        reset: @escaping (Value, inout Transaction) -> Void
    )

##  Parameters

`initialValue`

    

An initial state value.

`reset`

    

A closure that provides a `Transaction`.

## See Also

### Creating a gesture state

`init(initialValue: Value)`

Creates a view state that’s derived from a gesture with an initial value.

`init(initialValue: Value, resetTransaction: Transaction)`

Creates a view state that’s derived from a gesture with an initial state value
and a transaction to reset it.

`init(reset: (Value, inout Transaction) -> Void)`

Creates a view state that’s derived from a gesture with a closure that
provides a transaction to reset it.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(resetTransaction: Transaction)`

Creates a view state that’s derived from a gesture with a transaction to reset
it.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(wrappedValue: Value)`

Creates a view state that’s derived from a gesture.

`init(wrappedValue: Value, reset: (Value, inout Transaction) -> Void)`

Creates a view state that’s derived from a gesture with a wrapped state value
and a closure that provides a transaction to reset it.

`init(wrappedValue: Value, resetTransaction: Transaction)`

Creates a view state that’s derived from a gesture with a wrapped state value
and a transaction to reset it.

Initializer

# init(initialValue:resetTransaction:)

Creates a view state that’s derived from a gesture with an initial state value
and a transaction to reset it.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        initialValue: Value,
        resetTransaction: Transaction
    )

##  Parameters

`initialValue`

    

An initial state value.

`resetTransaction`

    

A transaction that provides metadata for view updates.

## See Also

### Creating a gesture state

`init(initialValue: Value)`

Creates a view state that’s derived from a gesture with an initial value.

`init(initialValue: Value, reset: (Value, inout Transaction) -> Void)`

Creates a view state that’s derived from a gesture with an initial state value
and a closure that provides a transaction to reset it.

`init(reset: (Value, inout Transaction) -> Void)`

Creates a view state that’s derived from a gesture with a closure that
provides a transaction to reset it.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(resetTransaction: Transaction)`

Creates a view state that’s derived from a gesture with a transaction to reset
it.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(wrappedValue: Value)`

Creates a view state that’s derived from a gesture.

`init(wrappedValue: Value, reset: (Value, inout Transaction) -> Void)`

Creates a view state that’s derived from a gesture with a wrapped state value
and a closure that provides a transaction to reset it.

`init(wrappedValue: Value, resetTransaction: Transaction)`

Creates a view state that’s derived from a gesture with a wrapped state value
and a transaction to reset it.

Initializer

# init(reset:)

Creates a view state that’s derived from a gesture with a closure that
provides a transaction to reset it.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(reset: @escaping (Value, inout Transaction) -> Void)

Available when `Value` conforms to `ExpressibleByNilLiteral`.

##  Parameters

`reset`

    

A closure that provides a `Transaction`.

## See Also

### Creating a gesture state

`init(initialValue: Value)`

Creates a view state that’s derived from a gesture with an initial value.

`init(initialValue: Value, reset: (Value, inout Transaction) -> Void)`

Creates a view state that’s derived from a gesture with an initial state value
and a closure that provides a transaction to reset it.

`init(initialValue: Value, resetTransaction: Transaction)`

Creates a view state that’s derived from a gesture with an initial state value
and a transaction to reset it.

`init(resetTransaction: Transaction)`

Creates a view state that’s derived from a gesture with a transaction to reset
it.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(wrappedValue: Value)`

Creates a view state that’s derived from a gesture.

`init(wrappedValue: Value, reset: (Value, inout Transaction) -> Void)`

Creates a view state that’s derived from a gesture with a wrapped state value
and a closure that provides a transaction to reset it.

`init(wrappedValue: Value, resetTransaction: Transaction)`

Creates a view state that’s derived from a gesture with a wrapped state value
and a transaction to reset it.

Initializer

# init(resetTransaction:)

Creates a view state that’s derived from a gesture with a transaction to reset
it.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(resetTransaction: Transaction = Transaction())

Available when `Value` conforms to `ExpressibleByNilLiteral`.

##  Parameters

`resetTransaction`

    

A transaction that provides metadata for view updates.

## See Also

### Creating a gesture state

`init(initialValue: Value)`

Creates a view state that’s derived from a gesture with an initial value.

`init(initialValue: Value, reset: (Value, inout Transaction) -> Void)`

Creates a view state that’s derived from a gesture with an initial state value
and a closure that provides a transaction to reset it.

`init(initialValue: Value, resetTransaction: Transaction)`

Creates a view state that’s derived from a gesture with an initial state value
and a transaction to reset it.

`init(reset: (Value, inout Transaction) -> Void)`

Creates a view state that’s derived from a gesture with a closure that
provides a transaction to reset it.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(wrappedValue: Value)`

Creates a view state that’s derived from a gesture.

`init(wrappedValue: Value, reset: (Value, inout Transaction) -> Void)`

Creates a view state that’s derived from a gesture with a wrapped state value
and a closure that provides a transaction to reset it.

`init(wrappedValue: Value, resetTransaction: Transaction)`

Creates a view state that’s derived from a gesture with a wrapped state value
and a transaction to reset it.

Initializer

# init(wrappedValue:)

Creates a view state that’s derived from a gesture.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(wrappedValue: Value)

##  Parameters

`wrappedValue`

    

A wrapped value for the gesture state property.

## See Also

### Creating a gesture state

`init(initialValue: Value)`

Creates a view state that’s derived from a gesture with an initial value.

`init(initialValue: Value, reset: (Value, inout Transaction) -> Void)`

Creates a view state that’s derived from a gesture with an initial state value
and a closure that provides a transaction to reset it.

`init(initialValue: Value, resetTransaction: Transaction)`

Creates a view state that’s derived from a gesture with an initial state value
and a transaction to reset it.

`init(reset: (Value, inout Transaction) -> Void)`

Creates a view state that’s derived from a gesture with a closure that
provides a transaction to reset it.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(resetTransaction: Transaction)`

Creates a view state that’s derived from a gesture with a transaction to reset
it.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(wrappedValue: Value, reset: (Value, inout Transaction) -> Void)`

Creates a view state that’s derived from a gesture with a wrapped state value
and a closure that provides a transaction to reset it.

`init(wrappedValue: Value, resetTransaction: Transaction)`

Creates a view state that’s derived from a gesture with a wrapped state value
and a transaction to reset it.

Initializer

# init(wrappedValue:reset:)

Creates a view state that’s derived from a gesture with a wrapped state value
and a closure that provides a transaction to reset it.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        wrappedValue: Value,
        reset: @escaping (Value, inout Transaction) -> Void
    )

##  Parameters

`wrappedValue`

    

A wrapped value for the gesture state property.

`reset`

    

A closure that provides a `Transaction`.

## See Also

### Creating a gesture state

`init(initialValue: Value)`

Creates a view state that’s derived from a gesture with an initial value.

`init(initialValue: Value, reset: (Value, inout Transaction) -> Void)`

Creates a view state that’s derived from a gesture with an initial state value
and a closure that provides a transaction to reset it.

`init(initialValue: Value, resetTransaction: Transaction)`

Creates a view state that’s derived from a gesture with an initial state value
and a transaction to reset it.

`init(reset: (Value, inout Transaction) -> Void)`

Creates a view state that’s derived from a gesture with a closure that
provides a transaction to reset it.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(resetTransaction: Transaction)`

Creates a view state that’s derived from a gesture with a transaction to reset
it.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(wrappedValue: Value)`

Creates a view state that’s derived from a gesture.

`init(wrappedValue: Value, resetTransaction: Transaction)`

Creates a view state that’s derived from a gesture with a wrapped state value
and a transaction to reset it.

Initializer

# init(wrappedValue:resetTransaction:)

Creates a view state that’s derived from a gesture with a wrapped state value
and a transaction to reset it.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        wrappedValue: Value,
        resetTransaction: Transaction
    )

##  Parameters

`wrappedValue`

    

A wrapped value for the gesture state property.

`resetTransaction`

    

A transaction that provides metadata for view updates.

## See Also

### Creating a gesture state

`init(initialValue: Value)`

Creates a view state that’s derived from a gesture with an initial value.

`init(initialValue: Value, reset: (Value, inout Transaction) -> Void)`

Creates a view state that’s derived from a gesture with an initial state value
and a closure that provides a transaction to reset it.

`init(initialValue: Value, resetTransaction: Transaction)`

Creates a view state that’s derived from a gesture with an initial state value
and a transaction to reset it.

`init(reset: (Value, inout Transaction) -> Void)`

Creates a view state that’s derived from a gesture with a closure that
provides a transaction to reset it.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(resetTransaction: Transaction)`

Creates a view state that’s derived from a gesture with a transaction to reset
it.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(wrappedValue: Value)`

Creates a view state that’s derived from a gesture.

`init(wrappedValue: Value, reset: (Value, inout Transaction) -> Void)`

Creates a view state that’s derived from a gesture with a wrapped state value
and a closure that provides a transaction to reset it.

Instance Property

# wrappedValue

The wrapped value referenced by the gesture state property.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var wrappedValue: Value { get }

## See Also

### Getting the state

`var projectedValue: GestureState<Value>`

A binding to the gesture state property.

Instance Property

# projectedValue

A binding to the gesture state property.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var projectedValue: GestureState<Value> { get }

## See Also

### Getting the state

`var wrappedValue: Value`

The wrapped value referenced by the gesture state property.

