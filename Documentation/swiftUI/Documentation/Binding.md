Initializer

# init(_:)

Creates a binding by projecting the base value to an unwrapped value.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init?(_ base: Binding<Value?>)

##  Parameters

`base`

    

A value to project to an unwrapped value.

## Return Value

A new binding or `nil` when `base` is `nil`.

## See Also

### Creating a binding

`init<V>(Binding<V>)`

Creates a binding by projecting the base value to an optional value.

`init<V>(Binding<V>)`

Creates a binding by projecting the base value to a hashable value.

`init(projectedValue: Binding<Value>)`

Creates a binding from the value of another binding.

`init(get: () -> Value, set: (Value, Transaction) -> Void)`

Creates a binding with a closure that reads from the binding value, and a
closure that applies a transaction when writing to the binding value.

`init(get: () -> Value, set: (Value) -> Void)`

Creates a binding with closures that read and write the binding value.

`static func constant(Value) -> Binding<Value>`

Creates a binding with an immutable value.

Initializer

# init(_:)

Creates a binding by projecting the base value to an optional value.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init<V>(_ base: Binding<V>) where Value == V?

##  Parameters

`base`

    

A value to project to an optional value.

## See Also

### Creating a binding

`init?(Binding<Value?>)`

Creates a binding by projecting the base value to an unwrapped value.

`init<V>(Binding<V>)`

Creates a binding by projecting the base value to a hashable value.

`init(projectedValue: Binding<Value>)`

Creates a binding from the value of another binding.

`init(get: () -> Value, set: (Value, Transaction) -> Void)`

Creates a binding with a closure that reads from the binding value, and a
closure that applies a transaction when writing to the binding value.

`init(get: () -> Value, set: (Value) -> Void)`

Creates a binding with closures that read and write the binding value.

`static func constant(Value) -> Binding<Value>`

Creates a binding with an immutable value.

Initializer

# init(_:)

Creates a binding by projecting the base value to a hashable value.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init<V>(_ base: Binding<V>) where Value == AnyHashable, V : Hashable

##  Parameters

`base`

    

A `Hashable` value to project to an `AnyHashable` value.

## See Also

### Creating a binding

`init?(Binding<Value?>)`

Creates a binding by projecting the base value to an unwrapped value.

`init<V>(Binding<V>)`

Creates a binding by projecting the base value to an optional value.

`init(projectedValue: Binding<Value>)`

Creates a binding from the value of another binding.

`init(get: () -> Value, set: (Value, Transaction) -> Void)`

Creates a binding with a closure that reads from the binding value, and a
closure that applies a transaction when writing to the binding value.

`init(get: () -> Value, set: (Value) -> Void)`

Creates a binding with closures that read and write the binding value.

`static func constant(Value) -> Binding<Value>`

Creates a binding with an immutable value.

Initializer

# init(projectedValue:)

Creates a binding from the value of another binding.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(projectedValue: Binding<Value>)

## See Also

### Creating a binding

`init?(Binding<Value?>)`

Creates a binding by projecting the base value to an unwrapped value.

`init<V>(Binding<V>)`

Creates a binding by projecting the base value to an optional value.

`init<V>(Binding<V>)`

Creates a binding by projecting the base value to a hashable value.

`init(get: () -> Value, set: (Value, Transaction) -> Void)`

Creates a binding with a closure that reads from the binding value, and a
closure that applies a transaction when writing to the binding value.

`init(get: () -> Value, set: (Value) -> Void)`

Creates a binding with closures that read and write the binding value.

`static func constant(Value) -> Binding<Value>`

Creates a binding with an immutable value.

Initializer

# init(get:set:)

Creates a binding with a closure that reads from the binding value, and a
closure that applies a transaction when writing to the binding value.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        get: @escaping () -> Value,
        set: @escaping (Value, Transaction) -> Void
    )

##  Parameters

`get`

    

A closure to retrieve the binding value. The closure has no parameters, and
returns a value.

`set`

    

A closure to set the binding value. The closure has the following parameters:

  * newValue: The new value of the binding value.

  * transaction: The transaction to apply when setting a new value.

## See Also

### Creating a binding

`init?(Binding<Value?>)`

Creates a binding by projecting the base value to an unwrapped value.

`init<V>(Binding<V>)`

Creates a binding by projecting the base value to an optional value.

`init<V>(Binding<V>)`

Creates a binding by projecting the base value to a hashable value.

`init(projectedValue: Binding<Value>)`

Creates a binding from the value of another binding.

`init(get: () -> Value, set: (Value) -> Void)`

Creates a binding with closures that read and write the binding value.

`static func constant(Value) -> Binding<Value>`

Creates a binding with an immutable value.

Initializer

# init(get:set:)

Creates a binding with closures that read and write the binding value.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        get: @escaping () -> Value,
        set: @escaping (Value) -> Void
    )

##  Parameters

`get`

    

A closure that retrieves the binding value. The closure has no parameters, and
returns a value.

`set`

    

A closure that sets the binding value. The closure has the following
parameter:

  * newValue: The new value of the binding value.

## See Also

### Creating a binding

`init?(Binding<Value?>)`

Creates a binding by projecting the base value to an unwrapped value.

`init<V>(Binding<V>)`

Creates a binding by projecting the base value to an optional value.

`init<V>(Binding<V>)`

Creates a binding by projecting the base value to a hashable value.

`init(projectedValue: Binding<Value>)`

Creates a binding from the value of another binding.

`init(get: () -> Value, set: (Value, Transaction) -> Void)`

Creates a binding with a closure that reads from the binding value, and a
closure that applies a transaction when writing to the binding value.

`static func constant(Value) -> Binding<Value>`

Creates a binding with an immutable value.

Type Method

# constant(_:)

Creates a binding with an immutable value.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static func constant(_ value: Value) -> Binding<Value>

##  Parameters

`value`

    

An immutable value.

## Discussion

Use this method to create a binding to a value that cannot change. This can be
useful when using a `PreviewProvider` to see how a view represents different
values.

## See Also

### Creating a binding

`init?(Binding<Value?>)`

Creates a binding by projecting the base value to an unwrapped value.

`init<V>(Binding<V>)`

Creates a binding by projecting the base value to an optional value.

`init<V>(Binding<V>)`

Creates a binding by projecting the base value to a hashable value.

`init(projectedValue: Binding<Value>)`

Creates a binding from the value of another binding.

`init(get: () -> Value, set: (Value, Transaction) -> Void)`

Creates a binding with a closure that reads from the binding value, and a
closure that applies a transaction when writing to the binding value.

`init(get: () -> Value, set: (Value) -> Void)`

Creates a binding with closures that read and write the binding value.

Instance Property

# wrappedValue

The underlying value referenced by the binding variable.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var wrappedValue: Value { get nonmutating set }

## Discussion

This property provides primary access to the value’s data. However, you don’t
access `wrappedValue` directly. Instead, you use the property variable created
with the `Binding` attribute. In the following code example, the binding
variable `isPlaying` returns the value of `wrappedValue`:

When a mutable binding value changes, the new value is immediately available.
However, updates to a view displaying the value happens asynchronously, so the
view may not show the change immediately.

## See Also

### Getting the value

`var projectedValue: Binding<Value>`

A projection of the binding value that returns a binding.

`subscript<Subject>(dynamicMember _: WritableKeyPath<Value, Subject>) ->
Binding<Subject>`

Returns a binding to the resulting value of a given key path.

Instance Property

# projectedValue

A projection of the binding value that returns a binding.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var projectedValue: Binding<Value> { get }

## Discussion

Use the projected value to pass a binding value down a view hierarchy. To get
the `projectedValue`, prefix the property variable with `$`. For example, in
the following code example `PlayerView` projects a binding of the state
property `isPlaying` to the `PlayButton` view using `$isPlaying`.

## See Also

### Getting the value

`var wrappedValue: Value`

The underlying value referenced by the binding variable.

`subscript<Subject>(dynamicMember _: WritableKeyPath<Value, Subject>) ->
Binding<Subject>`

Returns a binding to the resulting value of a given key path.

Instance Subscript

# subscript(dynamicMember:)

Returns a binding to the resulting value of a given key path.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    subscript<Subject>(dynamicMember keyPath: WritableKeyPath<Value, Subject>) -> Binding<Subject> { get }

##  Parameters

`keyPath`

    

A key path to a specific resulting value.

## Return Value

A new binding.

## See Also

### Getting the value

`var wrappedValue: Value`

The underlying value referenced by the binding variable.

`var projectedValue: Binding<Value>`

A projection of the binding value that returns a binding.

Instance Property

# id

The stable identity of the entity associated with this instance, corresponding
to the `id` of the binding’s wrapped value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var id: Value.ID { get }

Available when `Value` conforms to `Identifiable`.

## See Also

### Managing changes

`func animation(Animation?) -> Binding<Value>`

Specifies an animation to perform when the binding value changes.

`func transaction(Transaction) -> Binding<Value>`

Specifies a transaction for the binding.

`var transaction: Transaction`

The binding’s transaction.

Instance Method

# animation(_:)

Specifies an animation to perform when the binding value changes.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func animation(_ animation: Animation? = .default) -> Binding<Value>

##  Parameters

`animation`

    

An animation sequence performed when the binding value changes.

## Return Value

A new binding.

## See Also

### Managing changes

`var id: Value.ID`

The stable identity of the entity associated with this instance, corresponding
to the `id` of the binding’s wrapped value.

Available when `Value` conforms to `Identifiable`.

`func transaction(Transaction) -> Binding<Value>`

Specifies a transaction for the binding.

`var transaction: Transaction`

The binding’s transaction.

Instance Method

# transaction(_:)

Specifies a transaction for the binding.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func transaction(_ transaction: Transaction) -> Binding<Value>

##  Parameters

`transaction `

    

An instance of a `Transaction`.

## Return Value

A new binding.

## See Also

### Managing changes

`var id: Value.ID`

The stable identity of the entity associated with this instance, corresponding
to the `id` of the binding’s wrapped value.

Available when `Value` conforms to `Identifiable`.

`func animation(Animation?) -> Binding<Value>`

Specifies an animation to perform when the binding value changes.

`var transaction: Transaction`

The binding’s transaction.

Instance Property

# transaction

The binding’s transaction.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var transaction: Transaction

## Discussion

The transaction captures the information needed to update the view when the
binding value changes.

## See Also

### Managing changes

`var id: Value.ID`

The stable identity of the entity associated with this instance, corresponding
to the `id` of the binding’s wrapped value.

Available when `Value` conforms to `Identifiable`.

`func animation(Animation?) -> Binding<Value>`

Specifies an animation to perform when the binding value changes.

`func transaction(Transaction) -> Binding<Value>`

Specifies a transaction for the binding.

Collection

API Collection

# Identifiable Implementations

## Topics

### Instance Properties

`var id: Value.ID`

The stable identity of the entity associated with this instance, corresponding
to the `id` of the binding’s wrapped value.

Available when `Value` conforms to `Identifiable`.

