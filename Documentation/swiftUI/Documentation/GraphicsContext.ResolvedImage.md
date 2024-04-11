Instance Property

# size

The size of the image.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var size: CGSize { get }

## See Also

### Getting the image properties

`let baseline: CGFloat`

The distance from the top of the image to its baseline.

`var shading: GraphicsContext.Shading?`

An optional shading to fill the image with.

Instance Property

# baseline

The distance from the top of the image to its baseline.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    let baseline: CGFloat

## Discussion

If the image has no baseline, this value is equivalent to the image’s height.

## See Also

### Getting the image properties

`var size: CGSize`

The size of the image.

`var shading: GraphicsContext.Shading?`

An optional shading to fill the image with.

Instance Property

# shading

An optional shading to fill the image with.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var shading: GraphicsContext.Shading?

## Discussion

The value of this property defaults to `foreground` for template images, and
to `nil` otherwise.

## See Also

### Getting the image properties

`var size: CGSize`

The size of the image.

`let baseline: CGFloat`

The distance from the top of the image to its baseline.

