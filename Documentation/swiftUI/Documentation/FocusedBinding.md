Initializer

# init(_:)

A new property wrapper for the given key path.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(_ keyPath: KeyPath<FocusedValues, Binding<Value>?>)

##  Parameters

`keyPath`

    

The key path for the focus value to read.

## Discussion

The value of the property wrapper is updated dynamically as focus changes and
different published bindings go in and out of scope.

Instance Property

# projectedValue

A binding to the optional value.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    var projectedValue: Binding<Value?> { get }

## Discussion

The unwrapped value is `nil` when no focused view hierarchy has published a
corresponding binding.

## See Also

### Getting the value

`var wrappedValue: Value?`

The unwrapped value for the focus key given the current scope and state of the
focused view hierarchy.

Instance Property

# wrappedValue

The unwrapped value for the focus key given the current scope and state of the
focused view hierarchy.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    var wrappedValue: Value? { get nonmutating set }

## See Also

### Getting the value

`var projectedValue: Binding<Value?>`

A binding to the optional value.

