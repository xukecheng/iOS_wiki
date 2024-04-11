Initializer

# init(image:sourceRect:scale:)

Creates a shape-filling shape style.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        image: Image,
        sourceRect: CGRect = CGRect(x: 0, y: 0, width: 1, height: 1),
        scale: CGFloat = 1
    )

##  Parameters

`image`

    

The image to be drawn.

`sourceRect`

    

A unit-space rectangle defining how much of the source image to draw. The
results are undefined if `sourceRect` selects areas outside the `[0, 1]` range
in either axis.

`scale`

    

A scale factor applied to the image during rendering.

Instance Property

# image

The image to be drawn.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var image: Image

## See Also

### Configuring the image paint style

`var scale: CGFloat`

A scale factor applied to the image while being drawn.

`var sourceRect: CGRect`

A unit-space rectangle defining how much of the source image to draw.

Instance Property

# scale

A scale factor applied to the image while being drawn.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var scale: CGFloat

## See Also

### Configuring the image paint style

`var image: Image`

The image to be drawn.

`var sourceRect: CGRect`

A unit-space rectangle defining how much of the source image to draw.

Instance Property

# sourceRect

A unit-space rectangle defining how much of the source image to draw.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var sourceRect: CGRect

## Discussion

The results are undefined if this rectangle selects areas outside the `[0, 1]`
range in either axis.

## See Also

### Configuring the image paint style

`var image: Image`

The image to be drawn.

`var scale: CGFloat`

A scale factor applied to the image while being drawn.

