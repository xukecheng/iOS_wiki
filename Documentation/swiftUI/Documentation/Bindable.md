Initializer

# init(_:)

Creates a bindable object from an observable object.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init(_ wrappedValue: Value)

Available when `Value` conforms to `Observable`.

## Discussion

This initializer is equivalent to `init(wrappedValue:)`, but is more succinct
when when creating bindable objects nested within other expressions. For
example, you can use the initializer to create a bindable object inline with
code that declares a view that takes a binding as a parameter:

## See Also

### Creating a bindable value

`init(wrappedValue: Value)`

Creates a bindable object from an observable object.

Available when `Value` conforms to `Observable`.

`init(projectedValue: Bindable<Value>)`

Creates a bindable from the value of another bindable.

Available when `Value` conforms to `Observable`.

Initializer

# init(wrappedValue:)

Creates a bindable object from an observable object.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init(wrappedValue: Value)

Available when `Value` conforms to `Observable`.

## Discussion

You should not call this initializer directly. Instead, declare a property
with the `@Bindable` attribute, and provide an initial value.

## See Also

### Creating a bindable value

`init(Value)`

Creates a bindable object from an observable object.

Available when `Value` conforms to `Observable`.

`init(projectedValue: Bindable<Value>)`

Creates a bindable from the value of another bindable.

Available when `Value` conforms to `Observable`.

Initializer

# init(projectedValue:)

Creates a bindable from the value of another bindable.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init(projectedValue: Bindable<Value>)

Available when `Value` conforms to `Observable`.

## See Also

### Creating a bindable value

`init(Value)`

Creates a bindable object from an observable object.

Available when `Value` conforms to `Observable`.

`init(wrappedValue: Value)`

Creates a bindable object from an observable object.

Available when `Value` conforms to `Observable`.

Instance Property

# wrappedValue

The wrapped object.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var wrappedValue: Value

## See Also

### Getting the value

`var projectedValue: Bindable<Value>`

The bindable wrapper for the object that creates bindings to its properties
using dynamic member lookup.

`subscript<Subject>(dynamicMember _: ReferenceWritableKeyPath<Value, Subject>)
-> Binding<Subject>`

Returns a binding to the value of a given key path.

Instance Property

# projectedValue

The bindable wrapper for the object that creates bindings to its properties
using dynamic member lookup.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var projectedValue: Bindable<Value> { get }

## See Also

### Getting the value

`var wrappedValue: Value`

The wrapped object.

`subscript<Subject>(dynamicMember _: ReferenceWritableKeyPath<Value, Subject>)
-> Binding<Subject>`

Returns a binding to the value of a given key path.

Instance Subscript

# subscript(dynamicMember:)

Returns a binding to the value of a given key path.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    subscript<Subject>(dynamicMember keyPath: ReferenceWritableKeyPath<Value, Subject>) -> Binding<Subject> { get }

## See Also

### Getting the value

`var wrappedValue: Value`

The wrapped object.

`var projectedValue: Bindable<Value>`

The bindable wrapper for the object that creates bindings to its properties
using dynamic member lookup.

