Case

# Font.Leading.standard

The font’s default line spacing.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    case standard

## Discussion

If you modify a font to use a nonstandard line spacing like
`Font.Leading.tight` or `Font.Leading.loose`, you can use this value to return
to the font’s default line spacing.

## See Also

### Getting leading line spacing options

`case loose`

Increased line spacing.

`case tight`

Reduced line spacing.

Case

# Font.Leading.loose

Increased line spacing.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    case loose

## Discussion

This value typically increases line spacing by 1 point for watchOS and 2
points on other platforms.

## See Also

### Getting leading line spacing options

`case standard`

The font’s default line spacing.

`case tight`

Reduced line spacing.

Case

# Font.Leading.tight

Reduced line spacing.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    case tight

## Discussion

This value typically reduces line spacing by 1 point for watchOS and 2 points
on other platforms.

## See Also

### Getting leading line spacing options

`case standard`

The font’s default line spacing.

`case loose`

Increased line spacing.

