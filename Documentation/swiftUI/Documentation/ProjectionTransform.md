Initializer

# init()

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init()

## See Also

### Creating a transform

`init(CGAffineTransform)`

`init(CATransform3D)`

Initializer

# init(_:)

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(_ m: CGAffineTransform)

## See Also

### Creating a transform

`init()`

`init(CATransform3D)`

Initializer

# init(_:)

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(_ m: CATransform3D)

## See Also

### Creating a transform

`init()`

`init(CGAffineTransform)`

Instance Property

# isAffine

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var isAffine: Bool { get }

## See Also

### Getting transform characteristics

`var isIdentity: Bool`

Instance Property

# isIdentity

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var isIdentity: Bool { get }

## See Also

### Getting transform characteristics

`var isAffine: Bool`

Instance Method

# invert()

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    mutating func invert() -> Bool

## See Also

### Manipulating transforms

`func inverted() -> ProjectionTransform`

`func concatenating(ProjectionTransform) -> ProjectionTransform`

Instance Method

# inverted()

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func inverted() -> ProjectionTransform

## See Also

### Manipulating transforms

`func invert() -> Bool`

`func concatenating(ProjectionTransform) -> ProjectionTransform`

Instance Method

# concatenating(_:)

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func concatenating(_ rhs: ProjectionTransform) -> ProjectionTransform

## See Also

### Manipulating transforms

`func invert() -> Bool`

`func inverted() -> ProjectionTransform`

Instance Property

# m11

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var m11: CGFloat

## See Also

### Accessing the transform’s coefficients

`var m12: CGFloat`

`var m13: CGFloat`

`var m21: CGFloat`

`var m22: CGFloat`

`var m23: CGFloat`

`var m31: CGFloat`

`var m32: CGFloat`

`var m33: CGFloat`

Instance Property

# m12

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var m12: CGFloat

## See Also

### Accessing the transform’s coefficients

`var m11: CGFloat`

`var m13: CGFloat`

`var m21: CGFloat`

`var m22: CGFloat`

`var m23: CGFloat`

`var m31: CGFloat`

`var m32: CGFloat`

`var m33: CGFloat`

Instance Property

# m13

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var m13: CGFloat

## See Also

### Accessing the transform’s coefficients

`var m11: CGFloat`

`var m12: CGFloat`

`var m21: CGFloat`

`var m22: CGFloat`

`var m23: CGFloat`

`var m31: CGFloat`

`var m32: CGFloat`

`var m33: CGFloat`

Instance Property

# m21

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var m21: CGFloat

## See Also

### Accessing the transform’s coefficients

`var m11: CGFloat`

`var m12: CGFloat`

`var m13: CGFloat`

`var m22: CGFloat`

`var m23: CGFloat`

`var m31: CGFloat`

`var m32: CGFloat`

`var m33: CGFloat`

Instance Property

# m22

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var m22: CGFloat

## See Also

### Accessing the transform’s coefficients

`var m11: CGFloat`

`var m12: CGFloat`

`var m13: CGFloat`

`var m21: CGFloat`

`var m23: CGFloat`

`var m31: CGFloat`

`var m32: CGFloat`

`var m33: CGFloat`

Instance Property

# m23

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var m23: CGFloat

## See Also

### Accessing the transform’s coefficients

`var m11: CGFloat`

`var m12: CGFloat`

`var m13: CGFloat`

`var m21: CGFloat`

`var m22: CGFloat`

`var m31: CGFloat`

`var m32: CGFloat`

`var m33: CGFloat`

Instance Property

# m31

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var m31: CGFloat

## See Also

### Accessing the transform’s coefficients

`var m11: CGFloat`

`var m12: CGFloat`

`var m13: CGFloat`

`var m21: CGFloat`

`var m22: CGFloat`

`var m23: CGFloat`

`var m32: CGFloat`

`var m33: CGFloat`

Instance Property

# m32

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var m32: CGFloat

## See Also

### Accessing the transform’s coefficients

`var m11: CGFloat`

`var m12: CGFloat`

`var m13: CGFloat`

`var m21: CGFloat`

`var m22: CGFloat`

`var m23: CGFloat`

`var m31: CGFloat`

`var m33: CGFloat`

Instance Property

# m33

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var m33: CGFloat

## See Also

### Accessing the transform’s coefficients

`var m11: CGFloat`

`var m12: CGFloat`

`var m13: CGFloat`

`var m21: CGFloat`

`var m22: CGFloat`

`var m23: CGFloat`

`var m31: CGFloat`

`var m32: CGFloat`

