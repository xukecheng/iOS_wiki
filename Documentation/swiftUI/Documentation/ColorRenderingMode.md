Case

# ColorRenderingMode.extendedLinear

The extended linear sRGB working color space.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case extendedLinear

## Discussion

Color component values outside the range `[0, 1]` are preserved. This color
space isn’t gamma corrected.

## See Also

### Getting rendering modes

`case linear`

The linear sRGB working color space.

`case nonLinear`

The non-linear sRGB working color space.

Case

# ColorRenderingMode.linear

The linear sRGB working color space.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case linear

## Discussion

Color component values outside the range `[0, 1]` produce undefined results.
This color space isn’t gamma corrected.

## See Also

### Getting rendering modes

`case extendedLinear`

The extended linear sRGB working color space.

`case nonLinear`

The non-linear sRGB working color space.

Case

# ColorRenderingMode.nonLinear

The non-linear sRGB working color space.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case nonLinear

## Discussion

Color component values outside the range `[0, 1]` produce undefined results.
This color space is gamma corrected.

## See Also

### Getting rendering modes

`case extendedLinear`

The extended linear sRGB working color space.

`case linear`

The linear sRGB working color space.

