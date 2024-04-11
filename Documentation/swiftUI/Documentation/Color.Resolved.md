Initializer

# init(colorSpace:red:green:blue:opacity:)

Creates a resolved color from red, green, and blue component values.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init(
        colorSpace: Color.RGBColorSpace = .sRGB,
        red: Float,
        green: Float,
        blue: Float,
        opacity: Float = 1
    )

##  Parameters

`colorSpace`

    

The profile that specifies how to interpret the color for display. The default
is `Color.RGBColorSpace.sRGB`.

`red`

    

The amount of red in the color.

`green`

    

The amount of green in the color.

`blue`

    

The amount of blue in the color.

`opacity`

    

An optional degree of opacity, given in the range `0` to `1`. A value of `0`
means 100% transparency, while a value of `1` means 100% opacity. The default
is `1`.

## Discussion

A standard sRGB color space clamps each color component — `red`, `green`, and
`blue` — to a range of `0` to `1`, but SwiftUI colors use an extended sRGB
color space, so you can use component values outside that range. This makes it
possible to create colors using the `Color.RGBColorSpace.sRGB` or
`Color.RGBColorSpace.sRGBLinear` color space that make full use of the wider
gamut of a diplay that supports `Color.RGBColorSpace.displayP3`.

Instance Property

# blue

The amount of blue in the color in the sRGB color space.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var blue: Float { get set }

Instance Property

# cgColor

A Core Graphics representation of the color.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var cgColor: CGColor { get }

## Discussion

You can get a `CGColor` instance from a resolved color.

Instance Property

# green

The amount of green in the color in the sRGB color space.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var green: Float { get set }

Instance Property

# linearBlue

The amount of blue in the color in the sRGB linear color space.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var linearBlue: Float

Instance Property

# linearGreen

The amount of green in the color in the sRGB linear color space.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var linearGreen: Float

Instance Property

# linearRed

The amount of red in the color in the sRGB linear color space.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var linearRed: Float

Instance Property

# opacity

The degree of opacity in the color, given in the range `0` to `1`.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var opacity: Float

## Discussion

A value of `0` means 100% transparency, while a value of `1` means 100%
opacity.

Instance Property

# red

The amount of red in the color in the sRGB color space.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var red: Float { get set }

