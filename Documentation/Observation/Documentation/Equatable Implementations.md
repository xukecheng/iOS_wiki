Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

Observation  Swift  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+

    
    
    static func != (lhs: Self, rhs: Self) -> Bool

##  Parameters

`lhs`

    

A value to compare.

`rhs`

    

Another value to compare.

## Discussion

Inequality is the inverse of equality. For any values `a` and `b`, `a != b`
implies that `a == b` is `false`.

This is the default implementation of the not-equal-to operator (`!=`) for any
type that conforms to `Equatable`.

Operator

# ==(_:_:)

Returns a Boolean value indicating whether two values are equal.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static func == (lhs: ObservationRegistrar, rhs: ObservationRegistrar) -> Bool

##  Parameters

`lhs`

    

A value to compare.

`rhs`

    

Another value to compare.

## Discussion

Equality is the inverse of inequality. For any values `a` and `b`, `a == b`
implies that `a != b` is `false`.

