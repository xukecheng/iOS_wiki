Instance Property

# magnitudeSquared

Returns the dot-product of this vector arithmetic instance with itself.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var magnitudeSquared: Double { get }

**Required**

## See Also

### Manipulating values

`func scale(by: Double)`

Multiplies each component of this value by the given value.

**Required** Default implementation provided.

`func scaled(by: Double) -> Self`

Returns a value with each component of this value multiplied by the given
value.

`func interpolate(towards: Self, amount: Double)`

Interpolates this value with `other` by the specified `amount`.

`func interpolated(towards: Self, amount: Double) -> Self`

Returns this value interpolated with `other` by the specified `amount`.

Instance Method

# scale(by:)

Multiplies each component of this value by the given value.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    mutating func scale(by rhs: Double)

**Required** Default implementation provided.

## Default Implementations

### VectorArithmetic Implementations

`func scale(by: Double)`

Multiplies each component of this value by the given value.

Available when `Self` conforms to `Scalable3D`.

## See Also

### Manipulating values

`var magnitudeSquared: Double`

Returns the dot-product of this vector arithmetic instance with itself.

**Required**

` func scaled(by: Double) -> Self`

Returns a value with each component of this value multiplied by the given
value.

`func interpolate(towards: Self, amount: Double)`

Interpolates this value with `other` by the specified `amount`.

`func interpolated(towards: Self, amount: Double) -> Self`

Returns this value interpolated with `other` by the specified `amount`.

Instance Method

# scaled(by:)

Returns a value with each component of this value multiplied by the given
value.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func scaled(by rhs: Double) -> Self

## See Also

### Manipulating values

`var magnitudeSquared: Double`

Returns the dot-product of this vector arithmetic instance with itself.

**Required**

` func scale(by: Double)`

Multiplies each component of this value by the given value.

**Required** Default implementation provided.

`func interpolate(towards: Self, amount: Double)`

Interpolates this value with `other` by the specified `amount`.

`func interpolated(towards: Self, amount: Double) -> Self`

Returns this value interpolated with `other` by the specified `amount`.

Instance Method

# interpolate(towards:amount:)

Interpolates this value with `other` by the specified `amount`.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    mutating func interpolate(
        towards other: Self,
        amount: Double
    )

## Discussion

This is equivalent to `self = self + (other - self) * amount`.

## See Also

### Manipulating values

`var magnitudeSquared: Double`

Returns the dot-product of this vector arithmetic instance with itself.

**Required**

` func scale(by: Double)`

Multiplies each component of this value by the given value.

**Required** Default implementation provided.

`func scaled(by: Double) -> Self`

Returns a value with each component of this value multiplied by the given
value.

`func interpolated(towards: Self, amount: Double) -> Self`

Returns this value interpolated with `other` by the specified `amount`.

Instance Method

# interpolated(towards:amount:)

Returns this value interpolated with `other` by the specified `amount`.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func interpolated(
        towards other: Self,
        amount: Double
    ) -> Self

## Discussion

This result is equivalent to `self + (other - self) * amount`.

## See Also

### Manipulating values

`var magnitudeSquared: Double`

Returns the dot-product of this vector arithmetic instance with itself.

**Required**

` func scale(by: Double)`

Multiplies each component of this value by the given value.

**Required** Default implementation provided.

`func scaled(by: Double) -> Self`

Returns a value with each component of this value multiplied by the given
value.

`func interpolate(towards: Self, amount: Double)`

Interpolates this value with `other` by the specified `amount`.

