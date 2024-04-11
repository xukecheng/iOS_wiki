Instance Property

# animatableData

The data to animate.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var animatableData: Self.AnimatableData { get set }

**Required** Default implementations provided.

## Default Implementations

### Animatable Implementations

`var animatableData: Self`

The data to animate.

Available when `Self` conforms to `VectorArithmetic`.

`var animatableData: EmptyAnimatableData`

The data to animate.

Available when `AnimatableData` is `EmptyAnimatableData`.

## See Also

### Animating data

`associatedtype AnimatableData : VectorArithmetic`

The type defining the data to animate.

**Required**

Associated Type

# AnimatableData

The type defining the data to animate.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    associatedtype AnimatableData : VectorArithmetic

**Required**

## See Also

### Animating data

`var animatableData: Self.AnimatableData`

The data to animate.

**Required** Default implementations provided.

