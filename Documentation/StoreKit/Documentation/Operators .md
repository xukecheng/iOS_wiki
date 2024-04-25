Operator

# ...(_:)

Returns a partial range extending upward from a lower bound.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    postfix static func ... (minimum: Product.SubscriptionPeriod.Unit) -> PartialRangeFrom<Product.SubscriptionPeriod.Unit>

##  Parameters

`minimum`

    

The lower bound for the range.

## Discussion

Use the postfix range operator (postfix `...`) to create a partial range of
any type that conforms to the `Comparable` protocol. This example creates a
`PartialRangeFrom<Double>` instance that includes any value greater than or
equal to `5.0`.

You can use this type of partial range of a collection’s indices to represent
the range from the partial range’s lower bound up to the end of the
collection.

Precondition: `minimum` must compare equal to itself (i.e. cannot be NaN).

## See Also

### Inherited operators

`static func ... (Product.SubscriptionPeriod.Unit) ->
PartialRangeThrough<Product.SubscriptionPeriod.Unit>`

Returns a partial range up to, and including, its upper bound.

`static func ... (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) ->
ClosedRange<Product.SubscriptionPeriod.Unit>`

Returns a closed range that contains both of its bounds.

`static func ..< (Product.SubscriptionPeriod.Unit) ->
PartialRangeUpTo<Product.SubscriptionPeriod.Unit>`

Returns a partial range up to, but not including, its upper bound.

`static func ..< (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Range<Product.SubscriptionPeriod.Unit>`

Returns a half-open range that contains its lower bound but not its upper
bound.

`static func < (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

`static func <= (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether the value of the first argument is
less than or equal to that of the second argument.

`static func > (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether the value of the first argument is
greater than that of the second argument.

`static func >= (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether the value of the first argument is
greater than or equal to that of the second argument.

Operator

# ...(_:)

Returns a partial range up to, and including, its upper bound.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    prefix static func ... (maximum: Product.SubscriptionPeriod.Unit) -> PartialRangeThrough<Product.SubscriptionPeriod.Unit>

##  Parameters

`maximum`

    

The upper bound for the range.

## Discussion

Use the prefix closed range operator (prefix `...`) to create a partial range
of any type that conforms to the `Comparable` protocol. This example creates a
`PartialRangeThrough<Double>` instance that includes any value less than or
equal to `5.0`.

You can use this type of partial range of a collection’s indices to represent
the range from the start of the collection up to, and including, the partial
range’s upper bound.

Precondition: `maximum` must compare equal to itself (i.e. cannot be NaN).

## See Also

### Inherited operators

`static func ... (Product.SubscriptionPeriod.Unit) ->
PartialRangeFrom<Product.SubscriptionPeriod.Unit>`

Returns a partial range extending upward from a lower bound.

`static func ... (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) ->
ClosedRange<Product.SubscriptionPeriod.Unit>`

Returns a closed range that contains both of its bounds.

`static func ..< (Product.SubscriptionPeriod.Unit) ->
PartialRangeUpTo<Product.SubscriptionPeriod.Unit>`

Returns a partial range up to, but not including, its upper bound.

`static func ..< (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Range<Product.SubscriptionPeriod.Unit>`

Returns a half-open range that contains its lower bound but not its upper
bound.

`static func < (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

`static func <= (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether the value of the first argument is
less than or equal to that of the second argument.

`static func > (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether the value of the first argument is
greater than that of the second argument.

`static func >= (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether the value of the first argument is
greater than or equal to that of the second argument.

Operator

# ...(_:_:)

Returns a closed range that contains both of its bounds.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    static func ... (minimum: Product.SubscriptionPeriod.Unit, maximum: Product.SubscriptionPeriod.Unit) -> ClosedRange<Product.SubscriptionPeriod.Unit>

##  Parameters

`minimum`

    

The lower bound for the range.

`maximum`

    

The upper bound for the range.

## Discussion

Use the closed range operator (`...`) to create a closed range of any type
that conforms to the `Comparable` protocol. This example creates a
`ClosedRange<Character>` from “a” up to, and including, “z”.

Precondition: `minimum <= maximum`.

## See Also

### Inherited operators

`static func ... (Product.SubscriptionPeriod.Unit) ->
PartialRangeFrom<Product.SubscriptionPeriod.Unit>`

Returns a partial range extending upward from a lower bound.

`static func ... (Product.SubscriptionPeriod.Unit) ->
PartialRangeThrough<Product.SubscriptionPeriod.Unit>`

Returns a partial range up to, and including, its upper bound.

`static func ..< (Product.SubscriptionPeriod.Unit) ->
PartialRangeUpTo<Product.SubscriptionPeriod.Unit>`

Returns a partial range up to, but not including, its upper bound.

`static func ..< (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Range<Product.SubscriptionPeriod.Unit>`

Returns a half-open range that contains its lower bound but not its upper
bound.

`static func < (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

`static func <= (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether the value of the first argument is
less than or equal to that of the second argument.

`static func > (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether the value of the first argument is
greater than that of the second argument.

`static func >= (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether the value of the first argument is
greater than or equal to that of the second argument.

Operator

# ..<(_:)

Returns a partial range up to, but not including, its upper bound.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    prefix static func ..< (maximum: Product.SubscriptionPeriod.Unit) -> PartialRangeUpTo<Product.SubscriptionPeriod.Unit>

##  Parameters

`maximum`

    

The upper bound for the range.

## Discussion

Use the prefix half-open range operator (prefix `..<`) to create a partial
range of any type that conforms to the `Comparable` protocol. This example
creates a `PartialRangeUpTo<Double>` instance that includes any value less
than `5.0`.

You can use this type of partial range of a collection’s indices to represent
the range from the start of the collection up to, but not including, the
partial range’s upper bound.

Precondition: `maximum` must compare equal to itself (i.e. cannot be NaN).

## See Also

### Inherited operators

`static func ... (Product.SubscriptionPeriod.Unit) ->
PartialRangeFrom<Product.SubscriptionPeriod.Unit>`

Returns a partial range extending upward from a lower bound.

`static func ... (Product.SubscriptionPeriod.Unit) ->
PartialRangeThrough<Product.SubscriptionPeriod.Unit>`

Returns a partial range up to, and including, its upper bound.

`static func ... (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) ->
ClosedRange<Product.SubscriptionPeriod.Unit>`

Returns a closed range that contains both of its bounds.

`static func ..< (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Range<Product.SubscriptionPeriod.Unit>`

Returns a half-open range that contains its lower bound but not its upper
bound.

`static func < (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

`static func <= (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether the value of the first argument is
less than or equal to that of the second argument.

`static func > (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether the value of the first argument is
greater than that of the second argument.

`static func >= (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether the value of the first argument is
greater than or equal to that of the second argument.

Operator

# ..<(_:_:)

Returns a half-open range that contains its lower bound but not its upper
bound.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    static func ..< (minimum: Product.SubscriptionPeriod.Unit, maximum: Product.SubscriptionPeriod.Unit) -> Range<Product.SubscriptionPeriod.Unit>

##  Parameters

`minimum`

    

The lower bound for the range.

`maximum`

    

The upper bound for the range.

## Discussion

Use the half-open range operator (`..<`) to create a range of any type that
conforms to the `Comparable` protocol. This example creates a `Range<Double>`
from zero up to, but not including, 5.0.

Precondition: `minimum <= maximum`.

## See Also

### Inherited operators

`static func ... (Product.SubscriptionPeriod.Unit) ->
PartialRangeFrom<Product.SubscriptionPeriod.Unit>`

Returns a partial range extending upward from a lower bound.

`static func ... (Product.SubscriptionPeriod.Unit) ->
PartialRangeThrough<Product.SubscriptionPeriod.Unit>`

Returns a partial range up to, and including, its upper bound.

`static func ... (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) ->
ClosedRange<Product.SubscriptionPeriod.Unit>`

Returns a closed range that contains both of its bounds.

`static func ..< (Product.SubscriptionPeriod.Unit) ->
PartialRangeUpTo<Product.SubscriptionPeriod.Unit>`

Returns a partial range up to, but not including, its upper bound.

`static func < (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

`static func <= (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether the value of the first argument is
less than or equal to that of the second argument.

`static func > (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether the value of the first argument is
greater than that of the second argument.

`static func >= (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether the value of the first argument is
greater than or equal to that of the second argument.

Operator

# <(_:_:)

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    static func < (lhs: Product.SubscriptionPeriod.Unit, rhs: Product.SubscriptionPeriod.Unit) -> Bool

## Relationships

### From Protocol

  * `Comparable`

## See Also

### Inherited operators

`static func ... (Product.SubscriptionPeriod.Unit) ->
PartialRangeFrom<Product.SubscriptionPeriod.Unit>`

Returns a partial range extending upward from a lower bound.

`static func ... (Product.SubscriptionPeriod.Unit) ->
PartialRangeThrough<Product.SubscriptionPeriod.Unit>`

Returns a partial range up to, and including, its upper bound.

`static func ... (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) ->
ClosedRange<Product.SubscriptionPeriod.Unit>`

Returns a closed range that contains both of its bounds.

`static func ..< (Product.SubscriptionPeriod.Unit) ->
PartialRangeUpTo<Product.SubscriptionPeriod.Unit>`

Returns a partial range up to, but not including, its upper bound.

`static func ..< (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Range<Product.SubscriptionPeriod.Unit>`

Returns a half-open range that contains its lower bound but not its upper
bound.

`static func <= (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether the value of the first argument is
less than or equal to that of the second argument.

`static func > (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether the value of the first argument is
greater than that of the second argument.

`static func >= (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether the value of the first argument is
greater than or equal to that of the second argument.

Operator

# <=(_:_:)

Returns a Boolean value indicating whether the value of the first argument is
less than or equal to that of the second argument.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    static func <= (lhs: Product.SubscriptionPeriod.Unit, rhs: Product.SubscriptionPeriod.Unit) -> Bool

##  Parameters

`lhs`

    

A value to compare.

`rhs`

    

Another value to compare.

## Discussion

This is the default implementation of the less-than-or-equal-to operator
(`<=`) for any type that conforms to `Comparable`.

## See Also

### Inherited operators

`static func ... (Product.SubscriptionPeriod.Unit) ->
PartialRangeFrom<Product.SubscriptionPeriod.Unit>`

Returns a partial range extending upward from a lower bound.

`static func ... (Product.SubscriptionPeriod.Unit) ->
PartialRangeThrough<Product.SubscriptionPeriod.Unit>`

Returns a partial range up to, and including, its upper bound.

`static func ... (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) ->
ClosedRange<Product.SubscriptionPeriod.Unit>`

Returns a closed range that contains both of its bounds.

`static func ..< (Product.SubscriptionPeriod.Unit) ->
PartialRangeUpTo<Product.SubscriptionPeriod.Unit>`

Returns a partial range up to, but not including, its upper bound.

`static func ..< (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Range<Product.SubscriptionPeriod.Unit>`

Returns a half-open range that contains its lower bound but not its upper
bound.

`static func < (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

`static func > (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether the value of the first argument is
greater than that of the second argument.

`static func >= (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether the value of the first argument is
greater than or equal to that of the second argument.

Operator

# >(_:_:)

Returns a Boolean value indicating whether the value of the first argument is
greater than that of the second argument.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    static func > (lhs: Product.SubscriptionPeriod.Unit, rhs: Product.SubscriptionPeriod.Unit) -> Bool

##  Parameters

`lhs`

    

A value to compare.

`rhs`

    

Another value to compare.

## Discussion

This is the default implementation of the greater-than operator (`>`) for any
type that conforms to `Comparable`.

## See Also

### Inherited operators

`static func ... (Product.SubscriptionPeriod.Unit) ->
PartialRangeFrom<Product.SubscriptionPeriod.Unit>`

Returns a partial range extending upward from a lower bound.

`static func ... (Product.SubscriptionPeriod.Unit) ->
PartialRangeThrough<Product.SubscriptionPeriod.Unit>`

Returns a partial range up to, and including, its upper bound.

`static func ... (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) ->
ClosedRange<Product.SubscriptionPeriod.Unit>`

Returns a closed range that contains both of its bounds.

`static func ..< (Product.SubscriptionPeriod.Unit) ->
PartialRangeUpTo<Product.SubscriptionPeriod.Unit>`

Returns a partial range up to, but not including, its upper bound.

`static func ..< (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Range<Product.SubscriptionPeriod.Unit>`

Returns a half-open range that contains its lower bound but not its upper
bound.

`static func < (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

`static func <= (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether the value of the first argument is
less than or equal to that of the second argument.

`static func >= (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether the value of the first argument is
greater than or equal to that of the second argument.

Operator

# >=(_:_:)

Returns a Boolean value indicating whether the value of the first argument is
greater than or equal to that of the second argument.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    static func >= (lhs: Product.SubscriptionPeriod.Unit, rhs: Product.SubscriptionPeriod.Unit) -> Bool

##  Parameters

`lhs`

    

A value to compare.

`rhs`

    

Another value to compare.

## Return Value

`true` if `lhs` is greater than or equal to `rhs`; otherwise, `false`.

## Discussion

This is the default implementation of the greater-than-or-equal-to operator
(`>=`) for any type that conforms to `Comparable`.

## See Also

### Inherited operators

`static func ... (Product.SubscriptionPeriod.Unit) ->
PartialRangeFrom<Product.SubscriptionPeriod.Unit>`

Returns a partial range extending upward from a lower bound.

`static func ... (Product.SubscriptionPeriod.Unit) ->
PartialRangeThrough<Product.SubscriptionPeriod.Unit>`

Returns a partial range up to, and including, its upper bound.

`static func ... (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) ->
ClosedRange<Product.SubscriptionPeriod.Unit>`

Returns a closed range that contains both of its bounds.

`static func ..< (Product.SubscriptionPeriod.Unit) ->
PartialRangeUpTo<Product.SubscriptionPeriod.Unit>`

Returns a partial range up to, but not including, its upper bound.

`static func ..< (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Range<Product.SubscriptionPeriod.Unit>`

Returns a half-open range that contains its lower bound but not its upper
bound.

`static func < (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

`static func <= (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether the value of the first argument is
less than or equal to that of the second argument.

`static func > (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether the value of the first argument is
greater than that of the second argument.

Operator

# ...(_:)

Returns a partial range extending upward from a lower bound.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    postfix static func ... (minimum: Product.SubscriptionPeriod.Unit) -> PartialRangeFrom<Product.SubscriptionPeriod.Unit>

##  Parameters

`minimum`

    

The lower bound for the range.

## Discussion

Use the postfix range operator (postfix `...`) to create a partial range of
any type that conforms to the `Comparable` protocol. This example creates a
`PartialRangeFrom<Double>` instance that includes any value greater than or
equal to `5.0`.

You can use this type of partial range of a collection’s indices to represent
the range from the partial range’s lower bound up to the end of the
collection.

Precondition: `minimum` must compare equal to itself (i.e. cannot be NaN).

## See Also

### Inherited operators

`static func ... (Product.SubscriptionPeriod.Unit) ->
PartialRangeThrough<Product.SubscriptionPeriod.Unit>`

Returns a partial range up to, and including, its upper bound.

`static func ... (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) ->
ClosedRange<Product.SubscriptionPeriod.Unit>`

Returns a closed range that contains both of its bounds.

`static func ..< (Product.SubscriptionPeriod.Unit) ->
PartialRangeUpTo<Product.SubscriptionPeriod.Unit>`

Returns a partial range up to, but not including, its upper bound.

`static func ..< (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Range<Product.SubscriptionPeriod.Unit>`

Returns a half-open range that contains its lower bound but not its upper
bound.

`static func < (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

`static func <= (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether the value of the first argument is
less than or equal to that of the second argument.

`static func > (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether the value of the first argument is
greater than that of the second argument.

`static func >= (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether the value of the first argument is
greater than or equal to that of the second argument.

Operator

# ...(_:)

Returns a partial range up to, and including, its upper bound.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    prefix static func ... (maximum: Product.SubscriptionPeriod.Unit) -> PartialRangeThrough<Product.SubscriptionPeriod.Unit>

##  Parameters

`maximum`

    

The upper bound for the range.

## Discussion

Use the prefix closed range operator (prefix `...`) to create a partial range
of any type that conforms to the `Comparable` protocol. This example creates a
`PartialRangeThrough<Double>` instance that includes any value less than or
equal to `5.0`.

You can use this type of partial range of a collection’s indices to represent
the range from the start of the collection up to, and including, the partial
range’s upper bound.

Precondition: `maximum` must compare equal to itself (i.e. cannot be NaN).

## See Also

### Inherited operators

`static func ... (Product.SubscriptionPeriod.Unit) ->
PartialRangeFrom<Product.SubscriptionPeriod.Unit>`

Returns a partial range extending upward from a lower bound.

`static func ... (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) ->
ClosedRange<Product.SubscriptionPeriod.Unit>`

Returns a closed range that contains both of its bounds.

`static func ..< (Product.SubscriptionPeriod.Unit) ->
PartialRangeUpTo<Product.SubscriptionPeriod.Unit>`

Returns a partial range up to, but not including, its upper bound.

`static func ..< (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Range<Product.SubscriptionPeriod.Unit>`

Returns a half-open range that contains its lower bound but not its upper
bound.

`static func < (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

`static func <= (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether the value of the first argument is
less than or equal to that of the second argument.

`static func > (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether the value of the first argument is
greater than that of the second argument.

`static func >= (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether the value of the first argument is
greater than or equal to that of the second argument.

Operator

# ...(_:_:)

Returns a closed range that contains both of its bounds.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    static func ... (minimum: Product.SubscriptionPeriod.Unit, maximum: Product.SubscriptionPeriod.Unit) -> ClosedRange<Product.SubscriptionPeriod.Unit>

##  Parameters

`minimum`

    

The lower bound for the range.

`maximum`

    

The upper bound for the range.

## Discussion

Use the closed range operator (`...`) to create a closed range of any type
that conforms to the `Comparable` protocol. This example creates a
`ClosedRange<Character>` from “a” up to, and including, “z”.

    
    
    let lowercase = "a"..."z"
    print(lowercase.contains("z"))
    // Prints "true"
    

Precondition: `minimum <= maximum`.

## See Also

### Inherited operators

`static func ... (Product.SubscriptionPeriod.Unit) ->
PartialRangeFrom<Product.SubscriptionPeriod.Unit>`

Returns a partial range extending upward from a lower bound.

`static func ... (Product.SubscriptionPeriod.Unit) ->
PartialRangeThrough<Product.SubscriptionPeriod.Unit>`

Returns a partial range up to, and including, its upper bound.

`static func ..< (Product.SubscriptionPeriod.Unit) ->
PartialRangeUpTo<Product.SubscriptionPeriod.Unit>`

Returns a partial range up to, but not including, its upper bound.

`static func ..< (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Range<Product.SubscriptionPeriod.Unit>`

Returns a half-open range that contains its lower bound but not its upper
bound.

`static func < (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

`static func <= (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether the value of the first argument is
less than or equal to that of the second argument.

`static func > (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether the value of the first argument is
greater than that of the second argument.

`static func >= (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether the value of the first argument is
greater than or equal to that of the second argument.

Operator

# ..<(_:)

Returns a partial range up to, but not including, its upper bound.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    prefix static func ..< (maximum: Product.SubscriptionPeriod.Unit) -> PartialRangeUpTo<Product.SubscriptionPeriod.Unit>

##  Parameters

`maximum`

    

The upper bound for the range.

## Discussion

Use the prefix half-open range operator (prefix `..<`) to create a partial
range of any type that conforms to the `Comparable` protocol. This example
creates a `PartialRangeUpTo<Double>` instance that includes any value less
than `5.0`.

You can use this type of partial range of a collection’s indices to represent
the range from the start of the collection up to, but not including, the
partial range’s upper bound.

Precondition: `maximum` must compare equal to itself (i.e. cannot be NaN).

## See Also

### Inherited operators

`static func ... (Product.SubscriptionPeriod.Unit) ->
PartialRangeFrom<Product.SubscriptionPeriod.Unit>`

Returns a partial range extending upward from a lower bound.

`static func ... (Product.SubscriptionPeriod.Unit) ->
PartialRangeThrough<Product.SubscriptionPeriod.Unit>`

Returns a partial range up to, and including, its upper bound.

`static func ... (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) ->
ClosedRange<Product.SubscriptionPeriod.Unit>`

Returns a closed range that contains both of its bounds.

`static func ..< (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Range<Product.SubscriptionPeriod.Unit>`

Returns a half-open range that contains its lower bound but not its upper
bound.

`static func < (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

`static func <= (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether the value of the first argument is
less than or equal to that of the second argument.

`static func > (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether the value of the first argument is
greater than that of the second argument.

`static func >= (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether the value of the first argument is
greater than or equal to that of the second argument.

Operator

# ..<(_:_:)

Returns a half-open range that contains its lower bound but not its upper
bound.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    static func ..< (minimum: Product.SubscriptionPeriod.Unit, maximum: Product.SubscriptionPeriod.Unit) -> Range<Product.SubscriptionPeriod.Unit>

##  Parameters

`minimum`

    

The lower bound for the range.

`maximum`

    

The upper bound for the range.

## Discussion

Use the half-open range operator (`..<`) to create a range of any type that
conforms to the `Comparable` protocol. This example creates a `Range<Double>`
from zero up to, but not including, 5.0.

Precondition: `minimum <= maximum`.

## See Also

### Inherited operators

`static func ... (Product.SubscriptionPeriod.Unit) ->
PartialRangeFrom<Product.SubscriptionPeriod.Unit>`

Returns a partial range extending upward from a lower bound.

`static func ... (Product.SubscriptionPeriod.Unit) ->
PartialRangeThrough<Product.SubscriptionPeriod.Unit>`

Returns a partial range up to, and including, its upper bound.

`static func ... (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) ->
ClosedRange<Product.SubscriptionPeriod.Unit>`

Returns a closed range that contains both of its bounds.

`static func ..< (Product.SubscriptionPeriod.Unit) ->
PartialRangeUpTo<Product.SubscriptionPeriod.Unit>`

Returns a partial range up to, but not including, its upper bound.

`static func < (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

`static func <= (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether the value of the first argument is
less than or equal to that of the second argument.

`static func > (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether the value of the first argument is
greater than that of the second argument.

`static func >= (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether the value of the first argument is
greater than or equal to that of the second argument.

Operator

# <(_:_:)

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    static func < (lhs: Product.SubscriptionPeriod.Unit, rhs: Product.SubscriptionPeriod.Unit) -> Bool

## Relationships

### From Protocol

  * `Comparable`

## See Also

### Inherited operators

`static func ... (Product.SubscriptionPeriod.Unit) ->
PartialRangeFrom<Product.SubscriptionPeriod.Unit>`

Returns a partial range extending upward from a lower bound.

`static func ... (Product.SubscriptionPeriod.Unit) ->
PartialRangeThrough<Product.SubscriptionPeriod.Unit>`

Returns a partial range up to, and including, its upper bound.

`static func ... (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) ->
ClosedRange<Product.SubscriptionPeriod.Unit>`

Returns a closed range that contains both of its bounds.

`static func ..< (Product.SubscriptionPeriod.Unit) ->
PartialRangeUpTo<Product.SubscriptionPeriod.Unit>`

Returns a partial range up to, but not including, its upper bound.

`static func ..< (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Range<Product.SubscriptionPeriod.Unit>`

Returns a half-open range that contains its lower bound but not its upper
bound.

`static func <= (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether the value of the first argument is
less than or equal to that of the second argument.

`static func > (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether the value of the first argument is
greater than that of the second argument.

`static func >= (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether the value of the first argument is
greater than or equal to that of the second argument.

Operator

# <=(_:_:)

Returns a Boolean value indicating whether the value of the first argument is
less than or equal to that of the second argument.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    static func <= (lhs: Product.SubscriptionPeriod.Unit, rhs: Product.SubscriptionPeriod.Unit) -> Bool

##  Parameters

`lhs`

    

A value to compare.

`rhs`

    

Another value to compare.

## Discussion

This is the default implementation of the less-than-or-equal-to operator
(`<=`) for any type that conforms to `Comparable`.

## See Also

### Inherited operators

`static func ... (Product.SubscriptionPeriod.Unit) ->
PartialRangeFrom<Product.SubscriptionPeriod.Unit>`

Returns a partial range extending upward from a lower bound.

`static func ... (Product.SubscriptionPeriod.Unit) ->
PartialRangeThrough<Product.SubscriptionPeriod.Unit>`

Returns a partial range up to, and including, its upper bound.

`static func ... (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) ->
ClosedRange<Product.SubscriptionPeriod.Unit>`

Returns a closed range that contains both of its bounds.

`static func ..< (Product.SubscriptionPeriod.Unit) ->
PartialRangeUpTo<Product.SubscriptionPeriod.Unit>`

Returns a partial range up to, but not including, its upper bound.

`static func ..< (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Range<Product.SubscriptionPeriod.Unit>`

Returns a half-open range that contains its lower bound but not its upper
bound.

`static func < (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

`static func > (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether the value of the first argument is
greater than that of the second argument.

`static func >= (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether the value of the first argument is
greater than or equal to that of the second argument.

Operator

# >(_:_:)

Returns a Boolean value indicating whether the value of the first argument is
greater than that of the second argument.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    static func > (lhs: Product.SubscriptionPeriod.Unit, rhs: Product.SubscriptionPeriod.Unit) -> Bool

##  Parameters

`lhs`

    

A value to compare.

`rhs`

    

Another value to compare.

## Discussion

This is the default implementation of the greater-than operator (`>`) for any
type that conforms to `Comparable`.

## See Also

### Inherited operators

`static func ... (Product.SubscriptionPeriod.Unit) ->
PartialRangeFrom<Product.SubscriptionPeriod.Unit>`

Returns a partial range extending upward from a lower bound.

`static func ... (Product.SubscriptionPeriod.Unit) ->
PartialRangeThrough<Product.SubscriptionPeriod.Unit>`

Returns a partial range up to, and including, its upper bound.

`static func ... (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) ->
ClosedRange<Product.SubscriptionPeriod.Unit>`

Returns a closed range that contains both of its bounds.

`static func ..< (Product.SubscriptionPeriod.Unit) ->
PartialRangeUpTo<Product.SubscriptionPeriod.Unit>`

Returns a partial range up to, but not including, its upper bound.

`static func ..< (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Range<Product.SubscriptionPeriod.Unit>`

Returns a half-open range that contains its lower bound but not its upper
bound.

`static func < (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

`static func <= (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether the value of the first argument is
less than or equal to that of the second argument.

`static func >= (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether the value of the first argument is
greater than or equal to that of the second argument.

Operator

# >=(_:_:)

Returns a Boolean value indicating whether the value of the first argument is
greater than or equal to that of the second argument.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    static func >= (lhs: Product.SubscriptionPeriod.Unit, rhs: Product.SubscriptionPeriod.Unit) -> Bool

##  Parameters

`lhs`

    

A value to compare.

`rhs`

    

Another value to compare.

## Return Value

`true` if `lhs` is greater than or equal to `rhs`; otherwise, `false`.

## Discussion

This is the default implementation of the greater-than-or-equal-to operator
(`>=`) for any type that conforms to `Comparable`.

## See Also

### Inherited operators

`static func ... (Product.SubscriptionPeriod.Unit) ->
PartialRangeFrom<Product.SubscriptionPeriod.Unit>`

Returns a partial range extending upward from a lower bound.

`static func ... (Product.SubscriptionPeriod.Unit) ->
PartialRangeThrough<Product.SubscriptionPeriod.Unit>`

Returns a partial range up to, and including, its upper bound.

`static func ... (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) ->
ClosedRange<Product.SubscriptionPeriod.Unit>`

Returns a closed range that contains both of its bounds.

`static func ..< (Product.SubscriptionPeriod.Unit) ->
PartialRangeUpTo<Product.SubscriptionPeriod.Unit>`

Returns a partial range up to, but not including, its upper bound.

`static func ..< (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Range<Product.SubscriptionPeriod.Unit>`

Returns a half-open range that contains its lower bound but not its upper
bound.

`static func < (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

`static func <= (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether the value of the first argument is
less than or equal to that of the second argument.

`static func > (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether the value of the first argument is
greater than that of the second argument.

Operator

# ...(_:)

Returns a partial range extending upward from a lower bound.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    postfix static func ... (minimum: Product.SubscriptionPeriod.Unit) -> PartialRangeFrom<Product.SubscriptionPeriod.Unit>

##  Parameters

`minimum`

    

The lower bound for the range.

## Discussion

Use the postfix range operator (postfix `...`) to create a partial range of
any type that conforms to the `Comparable` protocol. This example creates a
`PartialRangeFrom<Double>` instance that includes any value greater than or
equal to `5.0`.

    
    
    let atLeastFive = 5.0...
    
    
    atLeastFive.contains(4.0)     // false
    atLeastFive.contains(5.0)     // true
    atLeastFive.contains(6.0)     // true
    

You can use this type of partial range of a collection’s indices to represent
the range from the partial range’s lower bound up to the end of the
collection.

    
    
    let numbers = [10, 20, 30, 40, 50, 60, 70]
    print(numbers[3...])
    // Prints "[40, 50, 60, 70]"
    

Precondition: `minimum` must compare equal to itself (i.e. cannot be NaN).

## See Also

### Inherited operators

`static func ... (Product.SubscriptionPeriod.Unit) ->
PartialRangeThrough<Product.SubscriptionPeriod.Unit>`

Returns a partial range up to, and including, its upper bound.

`static func ... (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) ->
ClosedRange<Product.SubscriptionPeriod.Unit>`

Returns a closed range that contains both of its bounds.

`static func ..< (Product.SubscriptionPeriod.Unit) ->
PartialRangeUpTo<Product.SubscriptionPeriod.Unit>`

Returns a partial range up to, but not including, its upper bound.

`static func ..< (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Range<Product.SubscriptionPeriod.Unit>`

Returns a half-open range that contains its lower bound but not its upper
bound.

`static func < (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

`static func <= (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether the value of the first argument is
less than or equal to that of the second argument.

`static func > (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether the value of the first argument is
greater than that of the second argument.

`static func >= (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether the value of the first argument is
greater than or equal to that of the second argument.

Operator

# ...(_:)

Returns a partial range up to, and including, its upper bound.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    prefix static func ... (maximum: Product.SubscriptionPeriod.Unit) -> PartialRangeThrough<Product.SubscriptionPeriod.Unit>

##  Parameters

`maximum`

    

The upper bound for the range.

## Discussion

Use the prefix closed range operator (prefix `...`) to create a partial range
of any type that conforms to the `Comparable` protocol. This example creates a
`PartialRangeThrough<Double>` instance that includes any value less than or
equal to `5.0`.

    
    
    let throughFive = ...5.0
    
    
    throughFive.contains(4.0)     // true
    throughFive.contains(5.0)     // true
    throughFive.contains(6.0)     // false
    

You can use this type of partial range of a collection’s indices to represent
the range from the start of the collection up to, and including, the partial
range’s upper bound.

    
    
    let numbers = [10, 20, 30, 40, 50, 60, 70]
    print(numbers[...3])
    // Prints "[10, 20, 30, 40]"
    

Precondition: `maximum` must compare equal to itself (i.e. cannot be NaN).

## See Also

### Inherited operators

`static func ... (Product.SubscriptionPeriod.Unit) ->
PartialRangeFrom<Product.SubscriptionPeriod.Unit>`

Returns a partial range extending upward from a lower bound.

`static func ... (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) ->
ClosedRange<Product.SubscriptionPeriod.Unit>`

Returns a closed range that contains both of its bounds.

`static func ..< (Product.SubscriptionPeriod.Unit) ->
PartialRangeUpTo<Product.SubscriptionPeriod.Unit>`

Returns a partial range up to, but not including, its upper bound.

`static func ..< (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Range<Product.SubscriptionPeriod.Unit>`

Returns a half-open range that contains its lower bound but not its upper
bound.

`static func < (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

`static func <= (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether the value of the first argument is
less than or equal to that of the second argument.

`static func > (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether the value of the first argument is
greater than that of the second argument.

`static func >= (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether the value of the first argument is
greater than or equal to that of the second argument.

Operator

# ...(_:_:)

Returns a closed range that contains both of its bounds.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    static func ... (minimum: Product.SubscriptionPeriod.Unit, maximum: Product.SubscriptionPeriod.Unit) -> ClosedRange<Product.SubscriptionPeriod.Unit>

##  Parameters

`minimum`

    

The lower bound for the range.

`maximum`

    

The upper bound for the range.

## Discussion

Use the closed range operator (`...`) to create a closed range of any type
that conforms to the `Comparable` protocol. This example creates a
`ClosedRange<Character>` from “a” up to, and including, “z”.

    
    
    let lowercase = "a"..."z"
    print(lowercase.contains("z"))
    // Prints "true"
    

Precondition: `minimum <= maximum`.

## See Also

### Inherited operators

`static func ... (Product.SubscriptionPeriod.Unit) ->
PartialRangeFrom<Product.SubscriptionPeriod.Unit>`

Returns a partial range extending upward from a lower bound.

`static func ... (Product.SubscriptionPeriod.Unit) ->
PartialRangeThrough<Product.SubscriptionPeriod.Unit>`

Returns a partial range up to, and including, its upper bound.

`static func ..< (Product.SubscriptionPeriod.Unit) ->
PartialRangeUpTo<Product.SubscriptionPeriod.Unit>`

Returns a partial range up to, but not including, its upper bound.

`static func ..< (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Range<Product.SubscriptionPeriod.Unit>`

Returns a half-open range that contains its lower bound but not its upper
bound.

`static func < (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

`static func <= (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether the value of the first argument is
less than or equal to that of the second argument.

`static func > (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether the value of the first argument is
greater than that of the second argument.

`static func >= (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether the value of the first argument is
greater than or equal to that of the second argument.

Operator

# ..<(_:)

Returns a partial range up to, but not including, its upper bound.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    prefix static func ..< (maximum: Product.SubscriptionPeriod.Unit) -> PartialRangeUpTo<Product.SubscriptionPeriod.Unit>

##  Parameters

`maximum`

    

The upper bound for the range.

## Discussion

Use the prefix half-open range operator (prefix `..<`) to create a partial
range of any type that conforms to the `Comparable` protocol. This example
creates a `PartialRangeUpTo<Double>` instance that includes any value less
than `5.0`.

    
    
    let upToFive = ..<5.0
    
    
    upToFive.contains(3.14)       // true
    upToFive.contains(6.28)       // false
    upToFive.contains(5.0)        // false
    

You can use this type of partial range of a collection’s indices to represent
the range from the start of the collection up to, but not including, the
partial range’s upper bound.

    
    
    let numbers = [10, 20, 30, 40, 50, 60, 70]
    print(numbers[..<3])
    // Prints "[10, 20, 30]"
    

Precondition: `maximum` must compare equal to itself (i.e. cannot be NaN).

## See Also

### Inherited operators

`static func ... (Product.SubscriptionPeriod.Unit) ->
PartialRangeFrom<Product.SubscriptionPeriod.Unit>`

Returns a partial range extending upward from a lower bound.

`static func ... (Product.SubscriptionPeriod.Unit) ->
PartialRangeThrough<Product.SubscriptionPeriod.Unit>`

Returns a partial range up to, and including, its upper bound.

`static func ... (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) ->
ClosedRange<Product.SubscriptionPeriod.Unit>`

Returns a closed range that contains both of its bounds.

`static func ..< (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Range<Product.SubscriptionPeriod.Unit>`

Returns a half-open range that contains its lower bound but not its upper
bound.

`static func < (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

`static func <= (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether the value of the first argument is
less than or equal to that of the second argument.

`static func > (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether the value of the first argument is
greater than that of the second argument.

`static func >= (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether the value of the first argument is
greater than or equal to that of the second argument.

Operator

# ..<(_:_:)

Returns a half-open range that contains its lower bound but not its upper
bound.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    static func ..< (minimum: Product.SubscriptionPeriod.Unit, maximum: Product.SubscriptionPeriod.Unit) -> Range<Product.SubscriptionPeriod.Unit>

##  Parameters

`minimum`

    

The lower bound for the range.

`maximum`

    

The upper bound for the range.

## Discussion

Use the half-open range operator (`..<`) to create a range of any type that
conforms to the `Comparable` protocol. This example creates a `Range<Double>`
from zero up to, but not including, 5.0.

    
    
    let lessThanFive = 0.0..<5.0
    print(lessThanFive.contains(3.14))  // Prints "true"
    print(lessThanFive.contains(5.0))   // Prints "false"
    

Precondition: `minimum <= maximum`.

## See Also

### Inherited operators

`static func ... (Product.SubscriptionPeriod.Unit) ->
PartialRangeFrom<Product.SubscriptionPeriod.Unit>`

Returns a partial range extending upward from a lower bound.

`static func ... (Product.SubscriptionPeriod.Unit) ->
PartialRangeThrough<Product.SubscriptionPeriod.Unit>`

Returns a partial range up to, and including, its upper bound.

`static func ... (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) ->
ClosedRange<Product.SubscriptionPeriod.Unit>`

Returns a closed range that contains both of its bounds.

`static func ..< (Product.SubscriptionPeriod.Unit) ->
PartialRangeUpTo<Product.SubscriptionPeriod.Unit>`

Returns a partial range up to, but not including, its upper bound.

`static func < (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

`static func <= (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether the value of the first argument is
less than or equal to that of the second argument.

`static func > (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether the value of the first argument is
greater than that of the second argument.

`static func >= (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether the value of the first argument is
greater than or equal to that of the second argument.

Operator

# <(_:_:)

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    static func < (lhs: Product.SubscriptionPeriod.Unit, rhs: Product.SubscriptionPeriod.Unit) -> Bool

## Relationships

### From Protocol

  * `Comparable`

## See Also

### Inherited operators

`static func ... (Product.SubscriptionPeriod.Unit) ->
PartialRangeFrom<Product.SubscriptionPeriod.Unit>`

Returns a partial range extending upward from a lower bound.

`static func ... (Product.SubscriptionPeriod.Unit) ->
PartialRangeThrough<Product.SubscriptionPeriod.Unit>`

Returns a partial range up to, and including, its upper bound.

`static func ... (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) ->
ClosedRange<Product.SubscriptionPeriod.Unit>`

Returns a closed range that contains both of its bounds.

`static func ..< (Product.SubscriptionPeriod.Unit) ->
PartialRangeUpTo<Product.SubscriptionPeriod.Unit>`

Returns a partial range up to, but not including, its upper bound.

`static func ..< (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Range<Product.SubscriptionPeriod.Unit>`

Returns a half-open range that contains its lower bound but not its upper
bound.

`static func <= (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether the value of the first argument is
less than or equal to that of the second argument.

`static func > (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether the value of the first argument is
greater than that of the second argument.

`static func >= (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether the value of the first argument is
greater than or equal to that of the second argument.

Operator

# <=(_:_:)

Returns a Boolean value indicating whether the value of the first argument is
less than or equal to that of the second argument.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    static func <= (lhs: Product.SubscriptionPeriod.Unit, rhs: Product.SubscriptionPeriod.Unit) -> Bool

##  Parameters

`lhs`

    

A value to compare.

`rhs`

    

Another value to compare.

## Discussion

This is the default implementation of the less-than-or-equal-to operator
(`<=`) for any type that conforms to `Comparable`.

## See Also

### Inherited operators

`static func ... (Product.SubscriptionPeriod.Unit) ->
PartialRangeFrom<Product.SubscriptionPeriod.Unit>`

Returns a partial range extending upward from a lower bound.

`static func ... (Product.SubscriptionPeriod.Unit) ->
PartialRangeThrough<Product.SubscriptionPeriod.Unit>`

Returns a partial range up to, and including, its upper bound.

`static func ... (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) ->
ClosedRange<Product.SubscriptionPeriod.Unit>`

Returns a closed range that contains both of its bounds.

`static func ..< (Product.SubscriptionPeriod.Unit) ->
PartialRangeUpTo<Product.SubscriptionPeriod.Unit>`

Returns a partial range up to, but not including, its upper bound.

`static func ..< (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Range<Product.SubscriptionPeriod.Unit>`

Returns a half-open range that contains its lower bound but not its upper
bound.

`static func < (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

`static func > (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether the value of the first argument is
greater than that of the second argument.

`static func >= (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether the value of the first argument is
greater than or equal to that of the second argument.

Operator

# >(_:_:)

Returns a Boolean value indicating whether the value of the first argument is
greater than that of the second argument.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    static func > (lhs: Product.SubscriptionPeriod.Unit, rhs: Product.SubscriptionPeriod.Unit) -> Bool

##  Parameters

`lhs`

    

A value to compare.

`rhs`

    

Another value to compare.

## Discussion

This is the default implementation of the greater-than operator (`>`) for any
type that conforms to `Comparable`.

## See Also

### Inherited operators

`static func ... (Product.SubscriptionPeriod.Unit) ->
PartialRangeFrom<Product.SubscriptionPeriod.Unit>`

Returns a partial range extending upward from a lower bound.

`static func ... (Product.SubscriptionPeriod.Unit) ->
PartialRangeThrough<Product.SubscriptionPeriod.Unit>`

Returns a partial range up to, and including, its upper bound.

`static func ... (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) ->
ClosedRange<Product.SubscriptionPeriod.Unit>`

Returns a closed range that contains both of its bounds.

`static func ..< (Product.SubscriptionPeriod.Unit) ->
PartialRangeUpTo<Product.SubscriptionPeriod.Unit>`

Returns a partial range up to, but not including, its upper bound.

`static func ..< (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Range<Product.SubscriptionPeriod.Unit>`

Returns a half-open range that contains its lower bound but not its upper
bound.

`static func < (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

`static func <= (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether the value of the first argument is
less than or equal to that of the second argument.

`static func >= (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether the value of the first argument is
greater than or equal to that of the second argument.

Operator

# >=(_:_:)

Returns a Boolean value indicating whether the value of the first argument is
greater than or equal to that of the second argument.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    static func >= (lhs: Product.SubscriptionPeriod.Unit, rhs: Product.SubscriptionPeriod.Unit) -> Bool

##  Parameters

`lhs`

    

A value to compare.

`rhs`

    

Another value to compare.

## Return Value

`true` if `lhs` is greater than or equal to `rhs`; otherwise, `false`.

## Discussion

This is the default implementation of the greater-than-or-equal-to operator
(`>=`) for any type that conforms to `Comparable`.

## See Also

### Inherited operators

`static func ... (Product.SubscriptionPeriod.Unit) ->
PartialRangeFrom<Product.SubscriptionPeriod.Unit>`

Returns a partial range extending upward from a lower bound.

`static func ... (Product.SubscriptionPeriod.Unit) ->
PartialRangeThrough<Product.SubscriptionPeriod.Unit>`

Returns a partial range up to, and including, its upper bound.

`static func ... (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) ->
ClosedRange<Product.SubscriptionPeriod.Unit>`

Returns a closed range that contains both of its bounds.

`static func ..< (Product.SubscriptionPeriod.Unit) ->
PartialRangeUpTo<Product.SubscriptionPeriod.Unit>`

Returns a partial range up to, but not including, its upper bound.

`static func ..< (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Range<Product.SubscriptionPeriod.Unit>`

Returns a half-open range that contains its lower bound but not its upper
bound.

`static func < (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

`static func <= (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether the value of the first argument is
less than or equal to that of the second argument.

`static func > (Product.SubscriptionPeriod.Unit,
Product.SubscriptionPeriod.Unit) -> Bool`

Returns a Boolean value indicating whether the value of the first argument is
greater than that of the second argument.

