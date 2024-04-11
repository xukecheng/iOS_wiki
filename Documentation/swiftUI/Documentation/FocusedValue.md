Initializer

# init(_:)

A new property wrapper for the given object type.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init(_ objectType: Value.Type) where Value : AnyObject, Value : Observable

##  Parameters

`objectType`

    

The type of object to read the focus value for.

## Discussion

Reads the focused value of the given object type.

Important

This initializer only accepts objects conforming to the `Observable` protocol.
For reading environment objects that conform to `ObservableObject`, use
`FocusedObject`, instead.

To set the focused value that is read by this, use the `focusedValue(_:)` view
modifier.

## See Also

### Creating the value

`init(KeyPath<FocusedValues, Value?>)`

A new property wrapper for the given key path.

Initializer

# init(_:)

A new property wrapper for the given key path.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(_ keyPath: KeyPath<FocusedValues, Value?>)

##  Parameters

`keyPath`

    

The key path for the focus value to read.

## Discussion

The value of the property wrapper is updated dynamically as focus changes and
different published values go in and out of scope.

## See Also

### Creating the value

`init(Value.Type)`

A new property wrapper for the given object type.

Instance Property

# wrappedValue

The value for the focus key given the current scope and state of the focused
view hierarchy.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    var wrappedValue: Value? { get }

## Discussion

Returns `nil` when nothing in the focused view hierarchy exports a value.

