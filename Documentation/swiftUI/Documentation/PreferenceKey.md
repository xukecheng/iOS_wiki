Type Property

# defaultValue

The default value of the preference.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static var defaultValue: Self.Value { get }

**Required** Default implementation provided.

## Discussion

Views that have no explicit value for the key produce this default value.
Combining child views may remove an implicit value produced by using the
default. This means that `reduce(value: &x, nextValue: {defaultValue})`
shouldn’t change the meaning of `x`.

## Default Implementations

### PreferenceKey Implementations

`static var defaultValue: Self.Value`

Let nil-expressible values default-initialize to nil.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

## See Also

### Getting the default value

`associatedtype Value`

The type of value produced by this preference.

**Required**

Associated Type

# Value

The type of value produced by this preference.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    associatedtype Value

**Required**

## See Also

### Getting the default value

`static var defaultValue: Self.Value`

The default value of the preference.

**Required** Default implementation provided.

Type Method

# reduce(value:nextValue:)

Combines a sequence of values by modifying the previously-accumulated value
with the result of a closure that provides the next value.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static func reduce(
        value: inout Self.Value,
        nextValue: () -> Self.Value
    )

**Required**

##  Parameters

`value`

    

The value accumulated through previous calls to this method. The
implementation should modify this value.

`nextValue`

    

A closure that returns the next value in the sequence.

## Discussion

This method receives its values in view-tree order. Conceptually, this
combines the preference value from one tree with that of its next sibling.

