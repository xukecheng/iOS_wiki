Initializer

# init(_:bundle:)

Creates a color from a color set that you indicate by name.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        _ name: String,
        bundle: Bundle? = nil
    )

##  Parameters

`name`

    

The name of the color resource to look up.

`bundle`

    

The bundle in which to search for the color resource. If you don’t indicate a
bundle, the initializer looks in your app’s main bundle by default.

## Discussion

Use this initializer to load a color from a color set stored in an Asset
Catalog. The system determines which color within the set to use based on the
environment at render time. For example, you can provide light and dark
versions for background and foreground colors:

You can then instantiate colors by referencing the names of the assets:

SwiftUI renders the appropriate colors for each appearance:

Initializer

# init(hue:saturation:brightness:opacity:)

Creates a constant color from hue, saturation, and brightness values.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        hue: Double,
        saturation: Double,
        brightness: Double,
        opacity: Double = 1
    )

##  Parameters

`hue`

    

A value in the range `0` to `1` that maps to an angle from 0° to 360° to
represent a shade on the color wheel.

`saturation`

    

A value in the range `0` to `1` that indicates how strongly the hue affects
the color. A value of `0` removes the effect of the hue, resulting in gray. As
the value increases, the hue becomes more prominent.

`brightness`

    

A value in the range `0` to `1` that indicates how bright a color is. A value
of `0` results in black, regardless of the other components. The color
lightens as you increase this component.

`opacity`

    

An optional degree of opacity, given in the range `0` to `1`. A value of `0`
means 100% transparency, while a value of `1` means 100% opacity. The default
is `1`.

## Discussion

This initializer creates a constant color that doesn’t change based on
context. For example, it doesn’t have distinct light and dark appearances,
unlike various system-defined colors, or a color that you load from an Asset
Catalog with `init(_:bundle:)`.

## See Also

### Creating a color from component values

`init(Color.RGBColorSpace, white: Double, opacity: Double)`

Creates a constant grayscale color.

`init(Color.RGBColorSpace, red: Double, green: Double, blue: Double, opacity:
Double)`

Creates a constant color from red, green, and blue component values.

`enum RGBColorSpace`

A profile that specifies how to interpret a color value for display.

Initializer

# init(_:white:opacity:)

Creates a constant grayscale color.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        _ colorSpace: Color.RGBColorSpace = .sRGB,
        white: Double,
        opacity: Double = 1
    )

##  Parameters

`colorSpace`

    

The profile that specifies how to interpret the color for display. The default
is `Color.RGBColorSpace.sRGB`.

`white`

    

A value that indicates how white the color is, with higher values closer to
100% white, and lower values closer to 100% black.

`opacity`

    

An optional degree of opacity, given in the range `0` to `1`. A value of `0`
means 100% transparency, while a value of `1` means 100% opacity. The default
is `1`.

## Discussion

This initializer creates a constant color that doesn’t change based on
context. For example, it doesn’t have distinct light and dark appearances,
unlike various system-defined colors, or a color that you load from an Asset
Catalog with `init(_:bundle:)`.

A standard sRGB color space clamps the `white` component to a range of `0` to
`1`, but SwiftUI colors use an extended sRGB color space, so you can use
component values outside that range. This makes it possible to create colors
using the `Color.RGBColorSpace.sRGB` or `Color.RGBColorSpace.sRGBLinear` color
space that make full use of the wider gamut of a diplay that supports
`Color.RGBColorSpace.displayP3`.

## See Also

### Creating a color from component values

`init(hue: Double, saturation: Double, brightness: Double, opacity: Double)`

Creates a constant color from hue, saturation, and brightness values.

`init(Color.RGBColorSpace, red: Double, green: Double, blue: Double, opacity:
Double)`

Creates a constant color from red, green, and blue component values.

`enum RGBColorSpace`

A profile that specifies how to interpret a color value for display.

Initializer

# init(_:red:green:blue:opacity:)

Creates a constant color from red, green, and blue component values.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        _ colorSpace: Color.RGBColorSpace = .sRGB,
        red: Double,
        green: Double,
        blue: Double,
        opacity: Double = 1
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

This initializer creates a constant color that doesn’t change based on
context. For example, it doesn’t have distinct light and dark appearances,
unlike various system-defined colors, or a color that you load from an Asset
Catalog with `init(_:bundle:)`.

A standard sRGB color space clamps each color component — `red`, `green`, and
`blue` — to a range of `0` to `1`, but SwiftUI colors use an extended sRGB
color space, so you can use component values outside that range. This makes it
possible to create colors using the `Color.RGBColorSpace.sRGB` or
`Color.RGBColorSpace.sRGBLinear` color space that make full use of the wider
gamut of a diplay that supports `Color.RGBColorSpace.displayP3`.

## See Also

### Creating a color from component values

`init(hue: Double, saturation: Double, brightness: Double, opacity: Double)`

Creates a constant color from hue, saturation, and brightness values.

`init(Color.RGBColorSpace, white: Double, opacity: Double)`

Creates a constant grayscale color.

`enum RGBColorSpace`

A profile that specifies how to interpret a color value for display.

Enumeration

# Color.RGBColorSpace

A profile that specifies how to interpret a color value for display.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    enum RGBColorSpace

## Topics

### Getting color spaces

`case sRGB`

The extended red, green, blue (sRGB) color space.

`case sRGBLinear`

The extended sRGB color space with a linear transfer function.

`case displayP3`

The Display P3 color space.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Creating a color from component values

`init(hue: Double, saturation: Double, brightness: Double, opacity: Double)`

Creates a constant color from hue, saturation, and brightness values.

`init(Color.RGBColorSpace, white: Double, opacity: Double)`

Creates a constant grayscale color.

`init(Color.RGBColorSpace, red: Double, green: Double, blue: Double, opacity:
Double)`

Creates a constant color from red, green, and blue component values.

Initializer

# init(uiColor:)

Creates a color from a UIKit color.

iOS 15.0+  iPadOS 15.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS 8.0+
visionOS 1.0+

    
    
    init(uiColor: UIColor)

##  Parameters

`color`

    

A `UIColor` instance from which to create a color.

## Discussion

Use this method to create a SwiftUI color from a `UIColor` instance. The new
color preserves the adaptability of the original. For example, you can create
a rectangle using `link` to see how the shade adjusts to match the user’s
system settings:

The `Box` view defined above automatically changes its appearance when the
user turns on Dark Mode. With the light and dark appearances placed side by
side, you can see the subtle difference in shades:

Note

Use this initializer only if you need to convert an existing `UIColor` to a
SwiftUI color. Otherwise, create a SwiftUI `Color` using an initializer like
`init(_:red:green:blue:opacity:)`, or use a system color like `blue`.

## See Also

### Creating a color from another color

`init(nsColor: NSColor)`

Creates a color from an AppKit color.

`init(cgColor: CGColor)`

Creates a color from a Core Graphics color.

Initializer

# init(nsColor:)

Creates a color from an AppKit color.

macOS 12.0+

    
    
    init(nsColor: NSColor)

##  Parameters

`color`

    

An `NSColor` instance from which to create a color.

## Discussion

Use this method to create a SwiftUI color from an `NSColor` instance. The new
color preserves the adaptability of the original. For example, you can create
a rectangle using `linkColor` to see how the shade adjusts to match the user’s
system settings:

The `Box` view defined above automatically changes its appearance when the
user turns on Dark Mode. With the light and dark appearances placed side by
side, you can see the subtle difference in shades:

Note

Use this initializer only if you need to convert an existing `NSColor` to a
SwiftUI color. Otherwise, create a SwiftUI `Color` using an initializer like
`init(_:red:green:blue:opacity:)`, or use a system color like `blue`.

## See Also

### Creating a color from another color

`init(uiColor: UIColor)`

Creates a color from a UIKit color.

`init(cgColor: CGColor)`

Creates a color from a Core Graphics color.

Initializer

# init(cgColor:)

Creates a color from a Core Graphics color.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init(cgColor: CGColor)

##  Parameters

`color`

    

A `CGColor` instance from which to create a color.

## See Also

### Creating a color from another color

`init(uiColor: UIColor)`

Creates a color from a UIKit color.

`init(nsColor: NSColor)`

Creates a color from an AppKit color.

Initializer

# init(_:)

Initialize a `Color` with a color resource.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init(_ resource: ColorResource)

Initializer

# init(_:)

Creates a color that represents the specified custom color.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init<T>(_ color: T) where T : Hashable, T : ShapeStyle, T.Resolved == Color.Resolved

## See Also

### Creating a custom color

`init(Color.Resolved)`

Creates a constant color with the values specified by the resolved color.

`func resolve(in: EnvironmentValues) -> Color.Resolved`

Evaluates this color to a resolved color given the current `context`.

Initializer

# init(_:)

Creates a constant color with the values specified by the resolved color.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init(_ resolved: Color.Resolved)

## See Also

### Creating a custom color

`init<T>(T)`

Creates a color that represents the specified custom color.

`func resolve(in: EnvironmentValues) -> Color.Resolved`

Evaluates this color to a resolved color given the current `context`.

Instance Method

# resolve(in:)

Evaluates this color to a resolved color given the current `context`.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func resolve(in environment: EnvironmentValues) -> Color.Resolved

## See Also

### Creating a custom color

`init<T>(T)`

Creates a color that represents the specified custom color.

`init(Color.Resolved)`

Creates a constant color with the values specified by the resolved color.

Type Property

# black

A black color suitable for use in UI elements.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let black: Color

## See Also

### Getting standard colors

`static let blue: Color`

A context-dependent blue color suitable for use in UI elements.

`static let brown: Color`

A context-dependent brown color suitable for use in UI elements.

`static let clear: Color`

A clear color suitable for use in UI elements.

`static let cyan: Color`

A context-dependent cyan color suitable for use in UI elements.

`static let gray: Color`

A context-dependent gray color suitable for use in UI elements.

`static let green: Color`

A context-dependent green color suitable for use in UI elements.

`static let indigo: Color`

A context-dependent indigo color suitable for use in UI elements.

`static let mint: Color`

A context-dependent mint color suitable for use in UI elements.

`static let orange: Color`

A context-dependent orange color suitable for use in UI elements.

`static let pink: Color`

A context-dependent pink color suitable for use in UI elements.

`static let purple: Color`

A context-dependent purple color suitable for use in UI elements.

`static let red: Color`

A context-dependent red color suitable for use in UI elements.

`static let teal: Color`

A context-dependent teal color suitable for use in UI elements.

`static let white: Color`

A white color suitable for use in UI elements.

`static let yellow: Color`

A context-dependent yellow color suitable for use in UI elements.

Type Property

# blue

A context-dependent blue color suitable for use in UI elements.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let blue: Color

## See Also

### Getting standard colors

`static let black: Color`

A black color suitable for use in UI elements.

`static let brown: Color`

A context-dependent brown color suitable for use in UI elements.

`static let clear: Color`

A clear color suitable for use in UI elements.

`static let cyan: Color`

A context-dependent cyan color suitable for use in UI elements.

`static let gray: Color`

A context-dependent gray color suitable for use in UI elements.

`static let green: Color`

A context-dependent green color suitable for use in UI elements.

`static let indigo: Color`

A context-dependent indigo color suitable for use in UI elements.

`static let mint: Color`

A context-dependent mint color suitable for use in UI elements.

`static let orange: Color`

A context-dependent orange color suitable for use in UI elements.

`static let pink: Color`

A context-dependent pink color suitable for use in UI elements.

`static let purple: Color`

A context-dependent purple color suitable for use in UI elements.

`static let red: Color`

A context-dependent red color suitable for use in UI elements.

`static let teal: Color`

A context-dependent teal color suitable for use in UI elements.

`static let white: Color`

A white color suitable for use in UI elements.

`static let yellow: Color`

A context-dependent yellow color suitable for use in UI elements.

Type Property

# brown

A context-dependent brown color suitable for use in UI elements.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static let brown: Color

## See Also

### Getting standard colors

`static let black: Color`

A black color suitable for use in UI elements.

`static let blue: Color`

A context-dependent blue color suitable for use in UI elements.

`static let clear: Color`

A clear color suitable for use in UI elements.

`static let cyan: Color`

A context-dependent cyan color suitable for use in UI elements.

`static let gray: Color`

A context-dependent gray color suitable for use in UI elements.

`static let green: Color`

A context-dependent green color suitable for use in UI elements.

`static let indigo: Color`

A context-dependent indigo color suitable for use in UI elements.

`static let mint: Color`

A context-dependent mint color suitable for use in UI elements.

`static let orange: Color`

A context-dependent orange color suitable for use in UI elements.

`static let pink: Color`

A context-dependent pink color suitable for use in UI elements.

`static let purple: Color`

A context-dependent purple color suitable for use in UI elements.

`static let red: Color`

A context-dependent red color suitable for use in UI elements.

`static let teal: Color`

A context-dependent teal color suitable for use in UI elements.

`static let white: Color`

A white color suitable for use in UI elements.

`static let yellow: Color`

A context-dependent yellow color suitable for use in UI elements.

Type Property

# clear

A clear color suitable for use in UI elements.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let clear: Color

## See Also

### Getting standard colors

`static let black: Color`

A black color suitable for use in UI elements.

`static let blue: Color`

A context-dependent blue color suitable for use in UI elements.

`static let brown: Color`

A context-dependent brown color suitable for use in UI elements.

`static let cyan: Color`

A context-dependent cyan color suitable for use in UI elements.

`static let gray: Color`

A context-dependent gray color suitable for use in UI elements.

`static let green: Color`

A context-dependent green color suitable for use in UI elements.

`static let indigo: Color`

A context-dependent indigo color suitable for use in UI elements.

`static let mint: Color`

A context-dependent mint color suitable for use in UI elements.

`static let orange: Color`

A context-dependent orange color suitable for use in UI elements.

`static let pink: Color`

A context-dependent pink color suitable for use in UI elements.

`static let purple: Color`

A context-dependent purple color suitable for use in UI elements.

`static let red: Color`

A context-dependent red color suitable for use in UI elements.

`static let teal: Color`

A context-dependent teal color suitable for use in UI elements.

`static let white: Color`

A white color suitable for use in UI elements.

`static let yellow: Color`

A context-dependent yellow color suitable for use in UI elements.

Type Property

# cyan

A context-dependent cyan color suitable for use in UI elements.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static let cyan: Color

## See Also

### Getting standard colors

`static let black: Color`

A black color suitable for use in UI elements.

`static let blue: Color`

A context-dependent blue color suitable for use in UI elements.

`static let brown: Color`

A context-dependent brown color suitable for use in UI elements.

`static let clear: Color`

A clear color suitable for use in UI elements.

`static let gray: Color`

A context-dependent gray color suitable for use in UI elements.

`static let green: Color`

A context-dependent green color suitable for use in UI elements.

`static let indigo: Color`

A context-dependent indigo color suitable for use in UI elements.

`static let mint: Color`

A context-dependent mint color suitable for use in UI elements.

`static let orange: Color`

A context-dependent orange color suitable for use in UI elements.

`static let pink: Color`

A context-dependent pink color suitable for use in UI elements.

`static let purple: Color`

A context-dependent purple color suitable for use in UI elements.

`static let red: Color`

A context-dependent red color suitable for use in UI elements.

`static let teal: Color`

A context-dependent teal color suitable for use in UI elements.

`static let white: Color`

A white color suitable for use in UI elements.

`static let yellow: Color`

A context-dependent yellow color suitable for use in UI elements.

Type Property

# gray

A context-dependent gray color suitable for use in UI elements.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let gray: Color

## See Also

### Getting standard colors

`static let black: Color`

A black color suitable for use in UI elements.

`static let blue: Color`

A context-dependent blue color suitable for use in UI elements.

`static let brown: Color`

A context-dependent brown color suitable for use in UI elements.

`static let clear: Color`

A clear color suitable for use in UI elements.

`static let cyan: Color`

A context-dependent cyan color suitable for use in UI elements.

`static let green: Color`

A context-dependent green color suitable for use in UI elements.

`static let indigo: Color`

A context-dependent indigo color suitable for use in UI elements.

`static let mint: Color`

A context-dependent mint color suitable for use in UI elements.

`static let orange: Color`

A context-dependent orange color suitable for use in UI elements.

`static let pink: Color`

A context-dependent pink color suitable for use in UI elements.

`static let purple: Color`

A context-dependent purple color suitable for use in UI elements.

`static let red: Color`

A context-dependent red color suitable for use in UI elements.

`static let teal: Color`

A context-dependent teal color suitable for use in UI elements.

`static let white: Color`

A white color suitable for use in UI elements.

`static let yellow: Color`

A context-dependent yellow color suitable for use in UI elements.

Type Property

# green

A context-dependent green color suitable for use in UI elements.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let green: Color

## See Also

### Getting standard colors

`static let black: Color`

A black color suitable for use in UI elements.

`static let blue: Color`

A context-dependent blue color suitable for use in UI elements.

`static let brown: Color`

A context-dependent brown color suitable for use in UI elements.

`static let clear: Color`

A clear color suitable for use in UI elements.

`static let cyan: Color`

A context-dependent cyan color suitable for use in UI elements.

`static let gray: Color`

A context-dependent gray color suitable for use in UI elements.

`static let indigo: Color`

A context-dependent indigo color suitable for use in UI elements.

`static let mint: Color`

A context-dependent mint color suitable for use in UI elements.

`static let orange: Color`

A context-dependent orange color suitable for use in UI elements.

`static let pink: Color`

A context-dependent pink color suitable for use in UI elements.

`static let purple: Color`

A context-dependent purple color suitable for use in UI elements.

`static let red: Color`

A context-dependent red color suitable for use in UI elements.

`static let teal: Color`

A context-dependent teal color suitable for use in UI elements.

`static let white: Color`

A white color suitable for use in UI elements.

`static let yellow: Color`

A context-dependent yellow color suitable for use in UI elements.

Type Property

# indigo

A context-dependent indigo color suitable for use in UI elements.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static let indigo: Color

## See Also

### Getting standard colors

`static let black: Color`

A black color suitable for use in UI elements.

`static let blue: Color`

A context-dependent blue color suitable for use in UI elements.

`static let brown: Color`

A context-dependent brown color suitable for use in UI elements.

`static let clear: Color`

A clear color suitable for use in UI elements.

`static let cyan: Color`

A context-dependent cyan color suitable for use in UI elements.

`static let gray: Color`

A context-dependent gray color suitable for use in UI elements.

`static let green: Color`

A context-dependent green color suitable for use in UI elements.

`static let mint: Color`

A context-dependent mint color suitable for use in UI elements.

`static let orange: Color`

A context-dependent orange color suitable for use in UI elements.

`static let pink: Color`

A context-dependent pink color suitable for use in UI elements.

`static let purple: Color`

A context-dependent purple color suitable for use in UI elements.

`static let red: Color`

A context-dependent red color suitable for use in UI elements.

`static let teal: Color`

A context-dependent teal color suitable for use in UI elements.

`static let white: Color`

A white color suitable for use in UI elements.

`static let yellow: Color`

A context-dependent yellow color suitable for use in UI elements.

Type Property

# mint

A context-dependent mint color suitable for use in UI elements.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static let mint: Color

## See Also

### Getting standard colors

`static let black: Color`

A black color suitable for use in UI elements.

`static let blue: Color`

A context-dependent blue color suitable for use in UI elements.

`static let brown: Color`

A context-dependent brown color suitable for use in UI elements.

`static let clear: Color`

A clear color suitable for use in UI elements.

`static let cyan: Color`

A context-dependent cyan color suitable for use in UI elements.

`static let gray: Color`

A context-dependent gray color suitable for use in UI elements.

`static let green: Color`

A context-dependent green color suitable for use in UI elements.

`static let indigo: Color`

A context-dependent indigo color suitable for use in UI elements.

`static let orange: Color`

A context-dependent orange color suitable for use in UI elements.

`static let pink: Color`

A context-dependent pink color suitable for use in UI elements.

`static let purple: Color`

A context-dependent purple color suitable for use in UI elements.

`static let red: Color`

A context-dependent red color suitable for use in UI elements.

`static let teal: Color`

A context-dependent teal color suitable for use in UI elements.

`static let white: Color`

A white color suitable for use in UI elements.

`static let yellow: Color`

A context-dependent yellow color suitable for use in UI elements.

Type Property

# orange

A context-dependent orange color suitable for use in UI elements.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let orange: Color

## See Also

### Getting standard colors

`static let black: Color`

A black color suitable for use in UI elements.

`static let blue: Color`

A context-dependent blue color suitable for use in UI elements.

`static let brown: Color`

A context-dependent brown color suitable for use in UI elements.

`static let clear: Color`

A clear color suitable for use in UI elements.

`static let cyan: Color`

A context-dependent cyan color suitable for use in UI elements.

`static let gray: Color`

A context-dependent gray color suitable for use in UI elements.

`static let green: Color`

A context-dependent green color suitable for use in UI elements.

`static let indigo: Color`

A context-dependent indigo color suitable for use in UI elements.

`static let mint: Color`

A context-dependent mint color suitable for use in UI elements.

`static let pink: Color`

A context-dependent pink color suitable for use in UI elements.

`static let purple: Color`

A context-dependent purple color suitable for use in UI elements.

`static let red: Color`

A context-dependent red color suitable for use in UI elements.

`static let teal: Color`

A context-dependent teal color suitable for use in UI elements.

`static let white: Color`

A white color suitable for use in UI elements.

`static let yellow: Color`

A context-dependent yellow color suitable for use in UI elements.

Type Property

# pink

A context-dependent pink color suitable for use in UI elements.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let pink: Color

## See Also

### Getting standard colors

`static let black: Color`

A black color suitable for use in UI elements.

`static let blue: Color`

A context-dependent blue color suitable for use in UI elements.

`static let brown: Color`

A context-dependent brown color suitable for use in UI elements.

`static let clear: Color`

A clear color suitable for use in UI elements.

`static let cyan: Color`

A context-dependent cyan color suitable for use in UI elements.

`static let gray: Color`

A context-dependent gray color suitable for use in UI elements.

`static let green: Color`

A context-dependent green color suitable for use in UI elements.

`static let indigo: Color`

A context-dependent indigo color suitable for use in UI elements.

`static let mint: Color`

A context-dependent mint color suitable for use in UI elements.

`static let orange: Color`

A context-dependent orange color suitable for use in UI elements.

`static let purple: Color`

A context-dependent purple color suitable for use in UI elements.

`static let red: Color`

A context-dependent red color suitable for use in UI elements.

`static let teal: Color`

A context-dependent teal color suitable for use in UI elements.

`static let white: Color`

A white color suitable for use in UI elements.

`static let yellow: Color`

A context-dependent yellow color suitable for use in UI elements.

Type Property

# purple

A context-dependent purple color suitable for use in UI elements.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let purple: Color

## See Also

### Getting standard colors

`static let black: Color`

A black color suitable for use in UI elements.

`static let blue: Color`

A context-dependent blue color suitable for use in UI elements.

`static let brown: Color`

A context-dependent brown color suitable for use in UI elements.

`static let clear: Color`

A clear color suitable for use in UI elements.

`static let cyan: Color`

A context-dependent cyan color suitable for use in UI elements.

`static let gray: Color`

A context-dependent gray color suitable for use in UI elements.

`static let green: Color`

A context-dependent green color suitable for use in UI elements.

`static let indigo: Color`

A context-dependent indigo color suitable for use in UI elements.

`static let mint: Color`

A context-dependent mint color suitable for use in UI elements.

`static let orange: Color`

A context-dependent orange color suitable for use in UI elements.

`static let pink: Color`

A context-dependent pink color suitable for use in UI elements.

`static let red: Color`

A context-dependent red color suitable for use in UI elements.

`static let teal: Color`

A context-dependent teal color suitable for use in UI elements.

`static let white: Color`

A white color suitable for use in UI elements.

`static let yellow: Color`

A context-dependent yellow color suitable for use in UI elements.

Type Property

# red

A context-dependent red color suitable for use in UI elements.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let red: Color

## See Also

### Getting standard colors

`static let black: Color`

A black color suitable for use in UI elements.

`static let blue: Color`

A context-dependent blue color suitable for use in UI elements.

`static let brown: Color`

A context-dependent brown color suitable for use in UI elements.

`static let clear: Color`

A clear color suitable for use in UI elements.

`static let cyan: Color`

A context-dependent cyan color suitable for use in UI elements.

`static let gray: Color`

A context-dependent gray color suitable for use in UI elements.

`static let green: Color`

A context-dependent green color suitable for use in UI elements.

`static let indigo: Color`

A context-dependent indigo color suitable for use in UI elements.

`static let mint: Color`

A context-dependent mint color suitable for use in UI elements.

`static let orange: Color`

A context-dependent orange color suitable for use in UI elements.

`static let pink: Color`

A context-dependent pink color suitable for use in UI elements.

`static let purple: Color`

A context-dependent purple color suitable for use in UI elements.

`static let teal: Color`

A context-dependent teal color suitable for use in UI elements.

`static let white: Color`

A white color suitable for use in UI elements.

`static let yellow: Color`

A context-dependent yellow color suitable for use in UI elements.

Type Property

# teal

A context-dependent teal color suitable for use in UI elements.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static let teal: Color

## See Also

### Getting standard colors

`static let black: Color`

A black color suitable for use in UI elements.

`static let blue: Color`

A context-dependent blue color suitable for use in UI elements.

`static let brown: Color`

A context-dependent brown color suitable for use in UI elements.

`static let clear: Color`

A clear color suitable for use in UI elements.

`static let cyan: Color`

A context-dependent cyan color suitable for use in UI elements.

`static let gray: Color`

A context-dependent gray color suitable for use in UI elements.

`static let green: Color`

A context-dependent green color suitable for use in UI elements.

`static let indigo: Color`

A context-dependent indigo color suitable for use in UI elements.

`static let mint: Color`

A context-dependent mint color suitable for use in UI elements.

`static let orange: Color`

A context-dependent orange color suitable for use in UI elements.

`static let pink: Color`

A context-dependent pink color suitable for use in UI elements.

`static let purple: Color`

A context-dependent purple color suitable for use in UI elements.

`static let red: Color`

A context-dependent red color suitable for use in UI elements.

`static let white: Color`

A white color suitable for use in UI elements.

`static let yellow: Color`

A context-dependent yellow color suitable for use in UI elements.

Type Property

# white

A white color suitable for use in UI elements.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let white: Color

## See Also

### Getting standard colors

`static let black: Color`

A black color suitable for use in UI elements.

`static let blue: Color`

A context-dependent blue color suitable for use in UI elements.

`static let brown: Color`

A context-dependent brown color suitable for use in UI elements.

`static let clear: Color`

A clear color suitable for use in UI elements.

`static let cyan: Color`

A context-dependent cyan color suitable for use in UI elements.

`static let gray: Color`

A context-dependent gray color suitable for use in UI elements.

`static let green: Color`

A context-dependent green color suitable for use in UI elements.

`static let indigo: Color`

A context-dependent indigo color suitable for use in UI elements.

`static let mint: Color`

A context-dependent mint color suitable for use in UI elements.

`static let orange: Color`

A context-dependent orange color suitable for use in UI elements.

`static let pink: Color`

A context-dependent pink color suitable for use in UI elements.

`static let purple: Color`

A context-dependent purple color suitable for use in UI elements.

`static let red: Color`

A context-dependent red color suitable for use in UI elements.

`static let teal: Color`

A context-dependent teal color suitable for use in UI elements.

`static let yellow: Color`

A context-dependent yellow color suitable for use in UI elements.

Type Property

# yellow

A context-dependent yellow color suitable for use in UI elements.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let yellow: Color

## See Also

### Getting standard colors

`static let black: Color`

A black color suitable for use in UI elements.

`static let blue: Color`

A context-dependent blue color suitable for use in UI elements.

`static let brown: Color`

A context-dependent brown color suitable for use in UI elements.

`static let clear: Color`

A clear color suitable for use in UI elements.

`static let cyan: Color`

A context-dependent cyan color suitable for use in UI elements.

`static let gray: Color`

A context-dependent gray color suitable for use in UI elements.

`static let green: Color`

A context-dependent green color suitable for use in UI elements.

`static let indigo: Color`

A context-dependent indigo color suitable for use in UI elements.

`static let mint: Color`

A context-dependent mint color suitable for use in UI elements.

`static let orange: Color`

A context-dependent orange color suitable for use in UI elements.

`static let pink: Color`

A context-dependent pink color suitable for use in UI elements.

`static let purple: Color`

A context-dependent purple color suitable for use in UI elements.

`static let red: Color`

A context-dependent red color suitable for use in UI elements.

`static let teal: Color`

A context-dependent teal color suitable for use in UI elements.

`static let white: Color`

A white color suitable for use in UI elements.

Type Property

# accentColor

A color that reflects the accent color of the system or app.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static var accentColor: Color { get }

## Discussion

The accent color is a broad theme color applied to views and controls. You can
set it at the application level by specifying an accent color in your app’s
asset catalog.

Note

In macOS, SwiftUI applies customization of the accent color only if the user
chooses Multicolor under General > Accent color in System Preferences.

The following code renders a `Text` view using the app’s accent color:

## See Also

### Getting semantic colors

`static let primary: Color`

The color to use for primary content.

`static let secondary: Color`

The color to use for secondary content.

Type Property

# primary

The color to use for primary content.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let primary: Color

## See Also

### Getting semantic colors

`static var accentColor: Color`

A color that reflects the accent color of the system or app.

`static let secondary: Color`

The color to use for secondary content.

Type Property

# secondary

The color to use for secondary content.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let secondary: Color

## See Also

### Getting semantic colors

`static var accentColor: Color`

A color that reflects the accent color of the system or app.

`static let primary: Color`

The color to use for primary content.

Instance Method

# opacity(_:)

Multiplies the opacity of the color by the given amount.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func opacity(_ opacity: Double) -> Color

##  Parameters

`opacity`

    

The amount by which to multiply the opacity of the color.

## Return Value

A view with modified opacity.

## See Also

### Modifying a color

`var gradient: AnyGradient`

Returns the standard gradient for the color `self`.

Instance Property

# gradient

Returns the standard gradient for the color `self`.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var gradient: AnyGradient { get }

## Discussion

For example, filling a rectangle with a gradient derived from the standard
blue color:

## See Also

### Modifying a color

`func opacity(Double) -> Color`

Multiplies the opacity of the color by the given amount.

Instance Property

# description

A textual representation of the color.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var description: String { get }

## Discussion

Use this method to get a string that represents the color. The
`print(_:separator:terminator:)` function uses this property to get a string
representing an instance:

Operator

# ==(_:_:)

Indicates whether two colors are equal.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static func == (lhs: Color, rhs: Color) -> Bool

##  Parameters

`lhs`

    

The first color to compare.

`rhs`

    

The second color to compare.

## Return Value

A Boolean that’s set to `true` if the two colors are equal.

## See Also

### Comparing colors

`func hash(into: inout Hasher)`

Hashes the essential components of the color by feeding them into the given
hash function.

Instance Method

# hash(into:)

Hashes the essential components of the color by feeding them into the given
hash function.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func hash(into hasher: inout Hasher)

##  Parameters

`hasher`

    

The hash function to use when combining the components of the color.

## See Also

### Comparing colors

`static func == (Color, Color) -> Bool`

Indicates whether two colors are equal.

Initializer

# init(_:)

Creates a color from a UIKit color.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  Mac Catalyst
13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated  watchOS 6.0–10.4
Deprecated  visionOS 1.0+

    
    
    init(_ color: UIColor)

Deprecated

Use `init(uiColor:)` instead.

##  Parameters

`color`

    

A `UIColor` instance from which to create a color.

## Discussion

Use this method to create a SwiftUI color from a `UIColor` instance. The new
color preserves the adaptability of the original. For example, you can create
a rectangle using `link` to see how the shade adjusts to match the user’s
system settings:

The `Box` view defined above automatically changes its appearance when the
user turns on Dark Mode. With the light and dark appearances placed side by
side, you can see the subtle difference in shades:

Note

Use this initializer only if you need to convert an existing `UIColor` to a
SwiftUI color. Otherwise, create a SwiftUI `Color` using an initializer like
`init(_:red:green:blue:opacity:)`, or use a system color like `blue`.

## See Also

### Deprecated symbols

`init(NSColor)`

Creates a color from an AppKit color.

Deprecated

`init(CGColor)`

Creates a color from a Core Graphics color.

Deprecated

`var cgColor: CGColor?`

A Core Graphics representation of the color, if available.

Initializer

# init(_:)

Creates a color from an AppKit color.

macOS 10.15–14.4  Deprecated

    
    
    init(_ color: NSColor)

Deprecated

Use `init(nsColor:)` instead.

##  Parameters

`color`

    

An `NSColor` instance from which to create a color.

## Discussion

Use this method to create a SwiftUI color from an `NSColor` instance. The new
color preserves the adaptability of the original. For example, you can create
a rectangle using `linkColor` to see how the shade adjusts to match the user’s
system settings:

The `Box` view defined above automatically changes its appearance when the
user turns on Dark Mode. With the light and dark appearances placed side by
side, you can see the subtle difference in shades:

Note

Use this initializer only if you need to convert an existing `NSColor` to a
SwiftUI color. Otherwise, create a SwiftUI `Color` using an initializer like
`init(_:red:green:blue:opacity:)`, or use a system color like `blue`.

## See Also

### Deprecated symbols

`init(UIColor)`

Creates a color from a UIKit color.

Deprecated

`init(CGColor)`

Creates a color from a Core Graphics color.

Deprecated

`var cgColor: CGColor?`

A Core Graphics representation of the color, if available.

Initializer

# init(_:)

Creates a color from a Core Graphics color.

iOS 14.0–17.4  Deprecated  iPadOS 14.0–17.4  Deprecated  macOS 11.0–14.4
Deprecated  Mac Catalyst 14.0–17.4  Deprecated  tvOS 14.0–17.4  Deprecated
watchOS 7.0–10.4  Deprecated  visionOS 1.0+

    
    
    init(_ cgColor: CGColor)

Deprecated

Use `init(cgColor:)` instead.

##  Parameters

`color`

    

A `CGColor` instance from which to create a color.

## See Also

### Deprecated symbols

`init(UIColor)`

Creates a color from a UIKit color.

Deprecated

`init(NSColor)`

Creates a color from an AppKit color.

Deprecated

`var cgColor: CGColor?`

A Core Graphics representation of the color, if available.

Instance Property

# cgColor

A Core Graphics representation of the color, if available.

iOS 14.0–17.4  Deprecated  iPadOS 14.0–17.4  Deprecated  macOS 11.0–14.4
Deprecated  Mac Catalyst 14.0–17.4  Deprecated  tvOS 14.0–17.4  Deprecated
watchOS 7.0–10.4  Deprecated  visionOS 1.0+

    
    
    var cgColor: CGColor? { get }

## Discussion

You can get a `CGColor` instance from a constant SwiftUI color. This includes
colors you create from a Core Graphics color, from RGB or HSB components, or
from constant UIKit and AppKit colors.

For a dynamic color, like one you load from an Asset Catalog using
`init(_:bundle:)`, or one you create from a dynamic UIKit or AppKit color,
this property is `nil`. To evaluate all types of colors, use the
`resolve(in:)` method.

## See Also

### Deprecated symbols

`init(UIColor)`

Creates a color from a UIKit color.

Deprecated

`init(NSColor)`

Creates a color from an AppKit color.

Deprecated

`init(CGColor)`

Creates a color from a Core Graphics color.

Deprecated

Collection

API Collection

# ShapeStyle Implementations

## Topics

### Structures

`struct Resolved`

A concrete color value.

Collection

API Collection

# Transferable Implementations

## Topics

### Type Properties

`static var transferRepresentation: some TransferRepresentation`

One group of colors–constant colors–created with explicitly specified
component values are transferred as is.

