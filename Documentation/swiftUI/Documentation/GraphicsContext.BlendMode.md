Type Property

# normal

A mode that paints source image samples over the background image samples.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var normal: GraphicsContext.BlendMode { get }

## Discussion

This is the default blend mode.

Type Property

# darken

A mode that creates composite image samples by choosing the darker samples
from either the source image or the background.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var darken: GraphicsContext.BlendMode { get }

## Discussion

When you draw in this mode, source image samples that are darker than the
background replace the background. Otherwise, the background image samples
remain unchanged.

## See Also

### Darkening

`static var multiply: GraphicsContext.BlendMode`

A mode that multiplies the source image samples with the background image
samples.

`static var colorBurn: GraphicsContext.BlendMode`

A mode that darkens background image samples to reflect the source image
samples.

`static var plusDarker: GraphicsContext.BlendMode`

A mode that adds the inverse of the color components of the source and
background images, and then inverts the result, producing a darkened
composite.

Type Property

# multiply

A mode that multiplies the source image samples with the background image
samples.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var multiply: GraphicsContext.BlendMode { get }

## Discussion

Drawing in this mode results in colors that are at least as dark as either of
the two contributing sample colors.

## See Also

### Darkening

`static var darken: GraphicsContext.BlendMode`

A mode that creates composite image samples by choosing the darker samples
from either the source image or the background.

`static var colorBurn: GraphicsContext.BlendMode`

A mode that darkens background image samples to reflect the source image
samples.

`static var plusDarker: GraphicsContext.BlendMode`

A mode that adds the inverse of the color components of the source and
background images, and then inverts the result, producing a darkened
composite.

Type Property

# colorBurn

A mode that darkens background image samples to reflect the source image
samples.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var colorBurn: GraphicsContext.BlendMode { get }

## Discussion

Source image sample values that specify white do not produce a change.

## See Also

### Darkening

`static var darken: GraphicsContext.BlendMode`

A mode that creates composite image samples by choosing the darker samples
from either the source image or the background.

`static var multiply: GraphicsContext.BlendMode`

A mode that multiplies the source image samples with the background image
samples.

`static var plusDarker: GraphicsContext.BlendMode`

A mode that adds the inverse of the color components of the source and
background images, and then inverts the result, producing a darkened
composite.

Type Property

# plusDarker

A mode that adds the inverse of the color components of the source and
background images, and then inverts the result, producing a darkened
composite.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var plusDarker: GraphicsContext.BlendMode { get }

## Discussion

This mode implements the equation `R = MAX(0, 1 - ((1 - D) + (1 - S)))` where

  * `R` is the composite image.

  * `S` is the source image.

  * `D` is the background.

## See Also

### Darkening

`static var darken: GraphicsContext.BlendMode`

A mode that creates composite image samples by choosing the darker samples
from either the source image or the background.

`static var multiply: GraphicsContext.BlendMode`

A mode that multiplies the source image samples with the background image
samples.

`static var colorBurn: GraphicsContext.BlendMode`

A mode that darkens background image samples to reflect the source image
samples.

Type Property

# lighten

A mode that creates composite image samples by choosing the lighter samples
from either the source image or the background.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var lighten: GraphicsContext.BlendMode { get }

## Discussion

When you draw in this mode, source image samples that are lighter than the
background replace the background. Otherwise, the background image samples
remain unchanged.

## See Also

### Lightening

`static var screen: GraphicsContext.BlendMode`

A mode that multiplies the inverse of the source image samples with the
inverse of the background image samples.

`static var colorDodge: GraphicsContext.BlendMode`

A mode that brightens the background image samples to reflect the source image
samples.

`static var plusLighter: GraphicsContext.BlendMode`

A mode that adds the components of the source and background images, resulting
in a lightened composite.

Type Property

# screen

A mode that multiplies the inverse of the source image samples with the
inverse of the background image samples.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var screen: GraphicsContext.BlendMode { get }

## Discussion

Drawing in this mode results in colors that are at least as light as either of
the two contributing sample colors.

## See Also

### Lightening

`static var lighten: GraphicsContext.BlendMode`

A mode that creates composite image samples by choosing the lighter samples
from either the source image or the background.

`static var colorDodge: GraphicsContext.BlendMode`

A mode that brightens the background image samples to reflect the source image
samples.

`static var plusLighter: GraphicsContext.BlendMode`

A mode that adds the components of the source and background images, resulting
in a lightened composite.

Type Property

# colorDodge

A mode that brightens the background image samples to reflect the source image
samples.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var colorDodge: GraphicsContext.BlendMode { get }

## Discussion

Source image sample values that specify black do not produce a change.

## See Also

### Lightening

`static var lighten: GraphicsContext.BlendMode`

A mode that creates composite image samples by choosing the lighter samples
from either the source image or the background.

`static var screen: GraphicsContext.BlendMode`

A mode that multiplies the inverse of the source image samples with the
inverse of the background image samples.

`static var plusLighter: GraphicsContext.BlendMode`

A mode that adds the components of the source and background images, resulting
in a lightened composite.

Type Property

# plusLighter

A mode that adds the components of the source and background images, resulting
in a lightened composite.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var plusLighter: GraphicsContext.BlendMode { get }

## Discussion

This mode implements the equation `R = MIN(1, S + D)` where

  * `R` is the composite image.

  * `S` is the source image.

  * `D` is the background.

## See Also

### Lightening

`static var lighten: GraphicsContext.BlendMode`

A mode that creates composite image samples by choosing the lighter samples
from either the source image or the background.

`static var screen: GraphicsContext.BlendMode`

A mode that multiplies the inverse of the source image samples with the
inverse of the background image samples.

`static var colorDodge: GraphicsContext.BlendMode`

A mode that brightens the background image samples to reflect the source image
samples.

Type Property

# overlay

A mode that either multiplies or screens the source image samples with the
background image samples, depending on the background color.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var overlay: GraphicsContext.BlendMode { get }

## Discussion

Drawing in this mode overlays the existing image samples while preserving the
highlights and shadows of the background. The background color mixes with the
source image to reflect the lightness or darkness of the background.

## See Also

### Adding contrast

`static var softLight: GraphicsContext.BlendMode`

A mode that either darkens or lightens colors, depending on the source image
sample color.

`static var hardLight: GraphicsContext.BlendMode`

A mode that either multiplies or screens colors, depending on the source image
sample color.

Type Property

# softLight

A mode that either darkens or lightens colors, depending on the source image
sample color.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var softLight: GraphicsContext.BlendMode { get }

## Discussion

If the source image sample color is lighter than 50% gray, the background is
lightened, similar to dodging. If the source image sample color is darker than
50% gray, the background is darkened, similar to burning. If the source image
sample color is equal to 50% gray, the background is not changed. Image
samples that are equal to pure black or pure white produce darker or lighter
areas, but do not result in pure black or white. The overall effect is similar
to what you’d achieve by shining a diffuse spotlight on the source image. Use
this to add highlights to a scene.

## See Also

### Adding contrast

`static var overlay: GraphicsContext.BlendMode`

A mode that either multiplies or screens the source image samples with the
background image samples, depending on the background color.

`static var hardLight: GraphicsContext.BlendMode`

A mode that either multiplies or screens colors, depending on the source image
sample color.

Type Property

# hardLight

A mode that either multiplies or screens colors, depending on the source image
sample color.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var hardLight: GraphicsContext.BlendMode { get }

## Discussion

If the source image sample color is lighter than 50% gray, the background is
lightened, similar to screening. If the source image sample color is darker
than 50% gray, the background is darkened, similar to multiplying. If the
source image sample color is equal to 50% gray, the source image is not
changed. Image samples that are equal to pure black or pure white result in
pure black or white. The overall effect is similar to what you’d achieve by
shining a harsh spotlight on the source image. Use this to add highlights to a
scene.

## See Also

### Adding contrast

`static var overlay: GraphicsContext.BlendMode`

A mode that either multiplies or screens the source image samples with the
background image samples, depending on the background color.

`static var softLight: GraphicsContext.BlendMode`

A mode that either darkens or lightens colors, depending on the source image
sample color.

Type Property

# difference

A mode that subtracts the brighter of the source image sample color or the
background image sample color from the other.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var difference: GraphicsContext.BlendMode { get }

## Discussion

Source image sample values that are black produce no change; white inverts the
background color values.

## See Also

### Inverting

`static var exclusion: GraphicsContext.BlendMode`

A mode that produces an effect similar to that produced by the difference
blend mode, but with lower contrast.

Type Property

# exclusion

A mode that produces an effect similar to that produced by the difference
blend mode, but with lower contrast.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var exclusion: GraphicsContext.BlendMode { get }

## Discussion

Source image sample values that are black don’t produce a change; white
inverts the background color values.

## See Also

### Inverting

`static var difference: GraphicsContext.BlendMode`

A mode that subtracts the brighter of the source image sample color or the
background image sample color from the other.

Type Property

# hue

A mode that uses the luminance and saturation values of the background with
the hue of the source image.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var hue: GraphicsContext.BlendMode { get }

## See Also

### Mixing color components

`static var saturation: GraphicsContext.BlendMode`

A mode that uses the luminance and hue values of the background with the
saturation of the source image.

`static var color: GraphicsContext.BlendMode`

A mode that uses the luminance values of the background with the hue and
saturation values of the source image.

`static var luminosity: GraphicsContext.BlendMode`

A mode that uses the hue and saturation of the background with the luminance
of the source image.

Type Property

# saturation

A mode that uses the luminance and hue values of the background with the
saturation of the source image.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var saturation: GraphicsContext.BlendMode { get }

## Discussion

Areas of the background that have no saturation — namely, pure gray areas —
don’t produce a change.

## See Also

### Mixing color components

`static var hue: GraphicsContext.BlendMode`

A mode that uses the luminance and saturation values of the background with
the hue of the source image.

`static var color: GraphicsContext.BlendMode`

A mode that uses the luminance values of the background with the hue and
saturation values of the source image.

`static var luminosity: GraphicsContext.BlendMode`

A mode that uses the hue and saturation of the background with the luminance
of the source image.

Type Property

# color

A mode that uses the luminance values of the background with the hue and
saturation values of the source image.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var color: GraphicsContext.BlendMode { get }

## Discussion

This mode preserves the gray levels in the image. You can use this mode to
color monochrome images or to tint color images.

## See Also

### Mixing color components

`static var hue: GraphicsContext.BlendMode`

A mode that uses the luminance and saturation values of the background with
the hue of the source image.

`static var saturation: GraphicsContext.BlendMode`

A mode that uses the luminance and hue values of the background with the
saturation of the source image.

`static var luminosity: GraphicsContext.BlendMode`

A mode that uses the hue and saturation of the background with the luminance
of the source image.

Type Property

# luminosity

A mode that uses the hue and saturation of the background with the luminance
of the source image.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var luminosity: GraphicsContext.BlendMode { get }

## Discussion

This mode creates an effect that is inverse to the effect created by the
`color` mode.

## See Also

### Mixing color components

`static var hue: GraphicsContext.BlendMode`

A mode that uses the luminance and saturation values of the background with
the hue of the source image.

`static var saturation: GraphicsContext.BlendMode`

A mode that uses the luminance and hue values of the background with the
saturation of the source image.

`static var color: GraphicsContext.BlendMode`

A mode that uses the luminance values of the background with the hue and
saturation values of the source image.

Type Property

# clear

A mode that clears any pixels that the source image overwrites.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var clear: GraphicsContext.BlendMode { get }

## Discussion

With this mode, you can use the source image like an eraser.

This mode implements the equation `R = 0` where `R` is the composite image.

## See Also

### Accessing porter-duff modes

`static var copy: GraphicsContext.BlendMode`

A mode that replaces background image samples with source image samples.

`static var sourceIn: GraphicsContext.BlendMode`

A mode that you use to paint the source image, including its transparency,
onto the opaque parts of the background.

`static var sourceOut: GraphicsContext.BlendMode`

A mode that you use to paint the source image onto the transparent parts of
the background, while erasing the background.

`static var sourceAtop: GraphicsContext.BlendMode`

A mode that you use to paint the opaque parts of the source image onto the
opaque parts of the background.

`static var destinationOver: GraphicsContext.BlendMode`

A mode that you use to paint the source image under the background.

`static var destinationIn: GraphicsContext.BlendMode`

A mode that you use to erase any of the background that isn’t covered by
opaque source pixels.

`static var destinationOut: GraphicsContext.BlendMode`

A mode that you use to erase any of the background that is covered by opaque
source pixels.

`static var destinationAtop: GraphicsContext.BlendMode`

A mode that you use to paint the source image under the background, while
erasing any of the background not matched by opaque pixels from the source
image.

`static var xor: GraphicsContext.BlendMode`

A mode that you use to clear pixels where both the source and background
images are opaque.

Type Property

# copy

A mode that replaces background image samples with source image samples.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var copy: GraphicsContext.BlendMode { get }

## Discussion

Unlike the `normal` mode, the source image completely replaces the background,
so that even transparent pixels in the source image replace opaque pixels in
the background, rather than letting the background show through.

This mode implements the equation `R = S` where

  * `R` is the composite image.

  * `S` is the source image.

## See Also

### Accessing porter-duff modes

`static var clear: GraphicsContext.BlendMode`

A mode that clears any pixels that the source image overwrites.

`static var sourceIn: GraphicsContext.BlendMode`

A mode that you use to paint the source image, including its transparency,
onto the opaque parts of the background.

`static var sourceOut: GraphicsContext.BlendMode`

A mode that you use to paint the source image onto the transparent parts of
the background, while erasing the background.

`static var sourceAtop: GraphicsContext.BlendMode`

A mode that you use to paint the opaque parts of the source image onto the
opaque parts of the background.

`static var destinationOver: GraphicsContext.BlendMode`

A mode that you use to paint the source image under the background.

`static var destinationIn: GraphicsContext.BlendMode`

A mode that you use to erase any of the background that isn’t covered by
opaque source pixels.

`static var destinationOut: GraphicsContext.BlendMode`

A mode that you use to erase any of the background that is covered by opaque
source pixels.

`static var destinationAtop: GraphicsContext.BlendMode`

A mode that you use to paint the source image under the background, while
erasing any of the background not matched by opaque pixels from the source
image.

`static var xor: GraphicsContext.BlendMode`

A mode that you use to clear pixels where both the source and background
images are opaque.

Type Property

# sourceIn

A mode that you use to paint the source image, including its transparency,
onto the opaque parts of the background.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var sourceIn: GraphicsContext.BlendMode { get }

## Discussion

This mode implements the equation `R = S*Da` where

  * `R` is the composite image.

  * `S` is the source image.

  * `Da` is the source background’s alpha value.

## See Also

### Accessing porter-duff modes

`static var clear: GraphicsContext.BlendMode`

A mode that clears any pixels that the source image overwrites.

`static var copy: GraphicsContext.BlendMode`

A mode that replaces background image samples with source image samples.

`static var sourceOut: GraphicsContext.BlendMode`

A mode that you use to paint the source image onto the transparent parts of
the background, while erasing the background.

`static var sourceAtop: GraphicsContext.BlendMode`

A mode that you use to paint the opaque parts of the source image onto the
opaque parts of the background.

`static var destinationOver: GraphicsContext.BlendMode`

A mode that you use to paint the source image under the background.

`static var destinationIn: GraphicsContext.BlendMode`

A mode that you use to erase any of the background that isn’t covered by
opaque source pixels.

`static var destinationOut: GraphicsContext.BlendMode`

A mode that you use to erase any of the background that is covered by opaque
source pixels.

`static var destinationAtop: GraphicsContext.BlendMode`

A mode that you use to paint the source image under the background, while
erasing any of the background not matched by opaque pixels from the source
image.

`static var xor: GraphicsContext.BlendMode`

A mode that you use to clear pixels where both the source and background
images are opaque.

Type Property

# sourceOut

A mode that you use to paint the source image onto the transparent parts of
the background, while erasing the background.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var sourceOut: GraphicsContext.BlendMode { get }

## Discussion

This mode implements the equation `R = S*(1 - Da)` where

  * `R` is the composite image.

  * `S` is the source image.

  * `Da` is the source background’s alpha value.

## See Also

### Accessing porter-duff modes

`static var clear: GraphicsContext.BlendMode`

A mode that clears any pixels that the source image overwrites.

`static var copy: GraphicsContext.BlendMode`

A mode that replaces background image samples with source image samples.

`static var sourceIn: GraphicsContext.BlendMode`

A mode that you use to paint the source image, including its transparency,
onto the opaque parts of the background.

`static var sourceAtop: GraphicsContext.BlendMode`

A mode that you use to paint the opaque parts of the source image onto the
opaque parts of the background.

`static var destinationOver: GraphicsContext.BlendMode`

A mode that you use to paint the source image under the background.

`static var destinationIn: GraphicsContext.BlendMode`

A mode that you use to erase any of the background that isn’t covered by
opaque source pixels.

`static var destinationOut: GraphicsContext.BlendMode`

A mode that you use to erase any of the background that is covered by opaque
source pixels.

`static var destinationAtop: GraphicsContext.BlendMode`

A mode that you use to paint the source image under the background, while
erasing any of the background not matched by opaque pixels from the source
image.

`static var xor: GraphicsContext.BlendMode`

A mode that you use to clear pixels where both the source and background
images are opaque.

Type Property

# sourceAtop

A mode that you use to paint the opaque parts of the source image onto the
opaque parts of the background.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var sourceAtop: GraphicsContext.BlendMode { get }

## Discussion

This mode implements the equation `R = S*Da + D*(1 - Sa)` where

  * `R` is the composite image.

  * `S` is the source image.

  * `D` is the background.

  * `Sa` is the source image’s alpha value.

  * `Da` is the source background’s alpha value.

## See Also

### Accessing porter-duff modes

`static var clear: GraphicsContext.BlendMode`

A mode that clears any pixels that the source image overwrites.

`static var copy: GraphicsContext.BlendMode`

A mode that replaces background image samples with source image samples.

`static var sourceIn: GraphicsContext.BlendMode`

A mode that you use to paint the source image, including its transparency,
onto the opaque parts of the background.

`static var sourceOut: GraphicsContext.BlendMode`

A mode that you use to paint the source image onto the transparent parts of
the background, while erasing the background.

`static var destinationOver: GraphicsContext.BlendMode`

A mode that you use to paint the source image under the background.

`static var destinationIn: GraphicsContext.BlendMode`

A mode that you use to erase any of the background that isn’t covered by
opaque source pixels.

`static var destinationOut: GraphicsContext.BlendMode`

A mode that you use to erase any of the background that is covered by opaque
source pixels.

`static var destinationAtop: GraphicsContext.BlendMode`

A mode that you use to paint the source image under the background, while
erasing any of the background not matched by opaque pixels from the source
image.

`static var xor: GraphicsContext.BlendMode`

A mode that you use to clear pixels where both the source and background
images are opaque.

Type Property

# destinationOver

A mode that you use to paint the source image under the background.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var destinationOver: GraphicsContext.BlendMode { get }

## Discussion

This mode implements the equation `R = S*(1 - Da) + D` where

  * `R` is the composite image.

  * `S` is the source image.

  * `D` is the background.

  * `Da` is the source background’s alpha value.

## See Also

### Accessing porter-duff modes

`static var clear: GraphicsContext.BlendMode`

A mode that clears any pixels that the source image overwrites.

`static var copy: GraphicsContext.BlendMode`

A mode that replaces background image samples with source image samples.

`static var sourceIn: GraphicsContext.BlendMode`

A mode that you use to paint the source image, including its transparency,
onto the opaque parts of the background.

`static var sourceOut: GraphicsContext.BlendMode`

A mode that you use to paint the source image onto the transparent parts of
the background, while erasing the background.

`static var sourceAtop: GraphicsContext.BlendMode`

A mode that you use to paint the opaque parts of the source image onto the
opaque parts of the background.

`static var destinationIn: GraphicsContext.BlendMode`

A mode that you use to erase any of the background that isn’t covered by
opaque source pixels.

`static var destinationOut: GraphicsContext.BlendMode`

A mode that you use to erase any of the background that is covered by opaque
source pixels.

`static var destinationAtop: GraphicsContext.BlendMode`

A mode that you use to paint the source image under the background, while
erasing any of the background not matched by opaque pixels from the source
image.

`static var xor: GraphicsContext.BlendMode`

A mode that you use to clear pixels where both the source and background
images are opaque.

Type Property

# destinationIn

A mode that you use to erase any of the background that isn’t covered by
opaque source pixels.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var destinationIn: GraphicsContext.BlendMode { get }

## Discussion

This mode implements the equation `R = D*Sa` where

  * `R` is the composite image.

  * `S` is the source image.

  * `Da` is the source background’s alpha value.

## See Also

### Accessing porter-duff modes

`static var clear: GraphicsContext.BlendMode`

A mode that clears any pixels that the source image overwrites.

`static var copy: GraphicsContext.BlendMode`

A mode that replaces background image samples with source image samples.

`static var sourceIn: GraphicsContext.BlendMode`

A mode that you use to paint the source image, including its transparency,
onto the opaque parts of the background.

`static var sourceOut: GraphicsContext.BlendMode`

A mode that you use to paint the source image onto the transparent parts of
the background, while erasing the background.

`static var sourceAtop: GraphicsContext.BlendMode`

A mode that you use to paint the opaque parts of the source image onto the
opaque parts of the background.

`static var destinationOver: GraphicsContext.BlendMode`

A mode that you use to paint the source image under the background.

`static var destinationOut: GraphicsContext.BlendMode`

A mode that you use to erase any of the background that is covered by opaque
source pixels.

`static var destinationAtop: GraphicsContext.BlendMode`

A mode that you use to paint the source image under the background, while
erasing any of the background not matched by opaque pixels from the source
image.

`static var xor: GraphicsContext.BlendMode`

A mode that you use to clear pixels where both the source and background
images are opaque.

Type Property

# destinationOut

A mode that you use to erase any of the background that is covered by opaque
source pixels.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var destinationOut: GraphicsContext.BlendMode { get }

## Discussion

This mode implements the equation `R = D*(1 - Sa)` where

  * `R` is the composite image.

  * `D` is the background.

  * `Sa` is the source image’s alpha value.

## See Also

### Accessing porter-duff modes

`static var clear: GraphicsContext.BlendMode`

A mode that clears any pixels that the source image overwrites.

`static var copy: GraphicsContext.BlendMode`

A mode that replaces background image samples with source image samples.

`static var sourceIn: GraphicsContext.BlendMode`

A mode that you use to paint the source image, including its transparency,
onto the opaque parts of the background.

`static var sourceOut: GraphicsContext.BlendMode`

A mode that you use to paint the source image onto the transparent parts of
the background, while erasing the background.

`static var sourceAtop: GraphicsContext.BlendMode`

A mode that you use to paint the opaque parts of the source image onto the
opaque parts of the background.

`static var destinationOver: GraphicsContext.BlendMode`

A mode that you use to paint the source image under the background.

`static var destinationIn: GraphicsContext.BlendMode`

A mode that you use to erase any of the background that isn’t covered by
opaque source pixels.

`static var destinationAtop: GraphicsContext.BlendMode`

A mode that you use to paint the source image under the background, while
erasing any of the background not matched by opaque pixels from the source
image.

`static var xor: GraphicsContext.BlendMode`

A mode that you use to clear pixels where both the source and background
images are opaque.

Type Property

# destinationAtop

A mode that you use to paint the source image under the background, while
erasing any of the background not matched by opaque pixels from the source
image.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var destinationAtop: GraphicsContext.BlendMode { get }

## Discussion

This mode implements the equation `R = S*(1 - Da) + D*Sa` where

  * `R` is the composite image.

  * `S` is the source image.

  * `D` is the background.

  * `Sa` is the source image’s alpha value.

  * `Da` is the source background’s alpha value.

## See Also

### Accessing porter-duff modes

`static var clear: GraphicsContext.BlendMode`

A mode that clears any pixels that the source image overwrites.

`static var copy: GraphicsContext.BlendMode`

A mode that replaces background image samples with source image samples.

`static var sourceIn: GraphicsContext.BlendMode`

A mode that you use to paint the source image, including its transparency,
onto the opaque parts of the background.

`static var sourceOut: GraphicsContext.BlendMode`

A mode that you use to paint the source image onto the transparent parts of
the background, while erasing the background.

`static var sourceAtop: GraphicsContext.BlendMode`

A mode that you use to paint the opaque parts of the source image onto the
opaque parts of the background.

`static var destinationOver: GraphicsContext.BlendMode`

A mode that you use to paint the source image under the background.

`static var destinationIn: GraphicsContext.BlendMode`

A mode that you use to erase any of the background that isn’t covered by
opaque source pixels.

`static var destinationOut: GraphicsContext.BlendMode`

A mode that you use to erase any of the background that is covered by opaque
source pixels.

`static var xor: GraphicsContext.BlendMode`

A mode that you use to clear pixels where both the source and background
images are opaque.

Type Property

# xor

A mode that you use to clear pixels where both the source and background
images are opaque.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var xor: GraphicsContext.BlendMode { get }

## Discussion

This mode implements the equation `R = S*(1 - Da) + D*(1 - Sa)` where

  * `R` is the composite image.

  * `S` is the source image.

  * `D` is the background.

  * `Sa` is the source image’s alpha value.

  * `Da` is the source background’s alpha value.

This XOR mode is only nominally related to the classical bitmap XOR operation,
which SwiftUI doesn’t support.

## See Also

### Accessing porter-duff modes

`static var clear: GraphicsContext.BlendMode`

A mode that clears any pixels that the source image overwrites.

`static var copy: GraphicsContext.BlendMode`

A mode that replaces background image samples with source image samples.

`static var sourceIn: GraphicsContext.BlendMode`

A mode that you use to paint the source image, including its transparency,
onto the opaque parts of the background.

`static var sourceOut: GraphicsContext.BlendMode`

A mode that you use to paint the source image onto the transparent parts of
the background, while erasing the background.

`static var sourceAtop: GraphicsContext.BlendMode`

A mode that you use to paint the opaque parts of the source image onto the
opaque parts of the background.

`static var destinationOver: GraphicsContext.BlendMode`

A mode that you use to paint the source image under the background.

`static var destinationIn: GraphicsContext.BlendMode`

A mode that you use to erase any of the background that isn’t covered by
opaque source pixels.

`static var destinationOut: GraphicsContext.BlendMode`

A mode that you use to erase any of the background that is covered by opaque
source pixels.

`static var destinationAtop: GraphicsContext.BlendMode`

A mode that you use to paint the source image under the background, while
erasing any of the background not matched by opaque pixels from the source
image.

