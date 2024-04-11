Initializer

# init(shape:scale:anchor:)

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        shape: Content,
        scale: CGSize,
        anchor: UnitPoint = .center
    )

Instance Property

# anchor

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var anchor: UnitPoint

## See Also

### Getting the shape’s characteristics

`var scale: CGSize`

`var shape: Content`

Instance Property

# scale

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var scale: CGSize

## See Also

### Getting the shape’s characteristics

`var anchor: UnitPoint`

`var shape: Content`

Instance Property

# shape

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var shape: Content

## See Also

### Getting the shape’s characteristics

`var anchor: UnitPoint`

`var scale: CGSize`

Instance Property

# animatableData

The data to animate.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var animatableData: ScaledShape<Content>.AnimatableData { get set }

