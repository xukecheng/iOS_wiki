Case

# Color.RGBColorSpace.sRGB

The extended red, green, blue (sRGB) color space.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case sRGB

## Discussion

For information about the sRGB colorimetry and nonlinear transform function,
see the IEC 61966-2-1 specification.

Standard sRGB color spaces clamp the red, green, and blue components of a
color to a range of `0` to `1`, but SwiftUI colors use an extended sRGB color
space, so you can use component values outside that range.

## See Also

### Getting color spaces

`case sRGBLinear`

The extended sRGB color space with a linear transfer function.

`case displayP3`

The Display P3 color space.

Case

# Color.RGBColorSpace.sRGBLinear

The extended sRGB color space with a linear transfer function.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case sRGBLinear

## Discussion

This color space has the same colorimetry as `Color.RGBColorSpace.sRGB`, but
uses a linear transfer function.

Standard sRGB color spaces clamp the red, green, and blue components of a
color to a range of `0` to `1`, but SwiftUI colors use an extended sRGB color
space, so you can use component values outside that range.

## See Also

### Getting color spaces

`case sRGB`

The extended red, green, blue (sRGB) color space.

`case displayP3`

The Display P3 color space.

Case

# Color.RGBColorSpace.displayP3

The Display P3 color space.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case displayP3

## Discussion

This color space uses the Digital Cinema Initiatives - Protocol 3 (DCI-P3)
primary colors, a D65 white point, and the `Color.RGBColorSpace.sRGB` transfer
function.

## See Also

### Getting color spaces

`case sRGB`

The extended red, green, blue (sRGB) color space.

`case sRGBLinear`

The extended sRGB color space with a linear transfer function.

