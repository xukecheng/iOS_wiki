Type Property

# dithersResult

An option that causes the filter to dither the result, to reduce banding.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var dithersResult: GraphicsContext.BlurOptions { get }

## See Also

### Getting blur options

`static var opaque: GraphicsContext.BlurOptions`

An option that causes the filter to ensure the result is completely opaque.

Type Property

# opaque

An option that causes the filter to ensure the result is completely opaque.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var opaque: GraphicsContext.BlurOptions { get }

## Discussion

The filter ensure opacity by dividing each pixel by its alpha value. The
result may be undefined if the input to the filter isn’t also completely
opaque.

## See Also

### Getting blur options

`static var dithersResult: GraphicsContext.BlurOptions`

An option that causes the filter to dither the result, to reduce banding.

