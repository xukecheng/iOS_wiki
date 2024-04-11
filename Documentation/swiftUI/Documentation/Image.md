Initializer

# init(_:bundle:)

Creates a labeled image that you can use as content for controls.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        _ name: String,
        bundle: Bundle? = nil
    )

##  Parameters

`name`

    

The name of the image resource to lookup, as well as the localization key with
which to label the image.

`bundle`

    

The bundle to search for the image resource and localization content. If
`nil`, SwiftUI uses the main `Bundle`. Defaults to `nil`.

## See Also

### Creating an image

`init(String, variableValue: Double?, bundle: Bundle?)`

Creates a labeled image that you can use as content for controls, with a
variable value.

`init(ImageResource)`

Initialize an `Image` with an image resource.

Initializer

# init(_:variableValue:bundle:)

Creates a labeled image that you can use as content for controls, with a
variable value.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init(
        _ name: String,
        variableValue: Double?,
        bundle: Bundle? = nil
    )

##  Parameters

`name`

    

The name of the image resource to lookup, as well as the localization key with
which to label the image.

`variableValue`

    

An optional value between `0.0` and `1.0` that the rendered image can use to
customize its appearance, if specified. If the symbol doesn’t support variable
values, this parameter has no effect.

`bundle`

    

The bundle to search for the image resource and localization content. If
`nil`, SwiftUI uses the main `Bundle`. Defaults to `nil`.

## Discussion

This initializer creates an image using a using a symbol in the specified
bundle. The rendered symbol may alter its appearance to represent the value
provided in `variableValue`.

Note

See WWDC22 session 10158: Adopt variable color in SF Symbols for details on
how to create symbols that support variable values.

## See Also

### Creating an image

`init(String, bundle: Bundle?)`

Creates a labeled image that you can use as content for controls.

`init(ImageResource)`

Initialize an `Image` with an image resource.

Initializer

# init(_:)

Initialize an `Image` with an image resource.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init(_ resource: ImageResource)

## See Also

### Creating an image

`init(String, bundle: Bundle?)`

Creates a labeled image that you can use as content for controls.

`init(String, variableValue: Double?, bundle: Bundle?)`

Creates a labeled image that you can use as content for controls, with a
variable value.

Initializer

# init(_:bundle:label:)

Creates a labeled image that you can use as content for controls, with the
specified label.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        _ name: String,
        bundle: Bundle? = nil,
        label: Text
    )

##  Parameters

`name`

    

The name of the image resource to lookup

`bundle`

    

The bundle to search for the image resource. If `nil`, SwiftUI uses the main
`Bundle`. Defaults to `nil`.

`label`

    

The label associated with the image. SwiftUI uses the label for accessibility.

## See Also

### Creating an image for use as a control

`init(String, variableValue: Double?, bundle: Bundle?, label: Text)`

Creates a labeled image that you can use as content for controls, with the
specified label and variable value.

`init(CGImage, scale: CGFloat, orientation: Image.Orientation, label: Text)`

Creates a labeled image based on a Core Graphics image instance, usable as
content for controls.

Initializer

# init(_:variableValue:bundle:label:)

Creates a labeled image that you can use as content for controls, with the
specified label and variable value.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init(
        _ name: String,
        variableValue: Double?,
        bundle: Bundle? = nil,
        label: Text
    )

##  Parameters

`name`

    

The name of the image resource to lookup.

`variableValue`

    

An optional value between `0.0` and `1.0` that the rendered image can use to
customize its appearance, if specified. If the symbol doesn’t support variable
values, this parameter has no effect.

`bundle`

    

The bundle to search for the image resource. If `nil`, SwiftUI uses the main
`Bundle`. Defaults to `nil`.

`label`

    

The label associated with the image. SwiftUI uses the label for accessibility.

## Discussion

This initializer creates an image using a using a symbol in the specified
bundle. The rendered symbol may alter its appearance to represent the value
provided in `variableValue`.

Note

See WWDC22 session 10158: Adopt variable color in SF Symbols for details on
how to create symbols that support variable values.

## See Also

### Creating an image for use as a control

`init(String, bundle: Bundle?, label: Text)`

Creates a labeled image that you can use as content for controls, with the
specified label.

`init(CGImage, scale: CGFloat, orientation: Image.Orientation, label: Text)`

Creates a labeled image based on a Core Graphics image instance, usable as
content for controls.

Initializer

# init(_:scale:orientation:label:)

Creates a labeled image based on a Core Graphics image instance, usable as
content for controls.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        _ cgImage: CGImage,
        scale: CGFloat,
        orientation: Image.Orientation = .up,
        label: Text
    )

##  Parameters

`cgImage`

    

The base graphical image.

`scale`

    

The scale factor for the image, with a value like `1.0`, `2.0`, or `3.0`.

`orientation`

    

The orientation of the image. The default is `Image.Orientation.up`.

`label`

    

The label associated with the image. SwiftUI uses the label for accessibility.

## See Also

### Creating an image for use as a control

`init(String, bundle: Bundle?, label: Text)`

Creates a labeled image that you can use as content for controls, with the
specified label.

`init(String, variableValue: Double?, bundle: Bundle?, label: Text)`

Creates a labeled image that you can use as content for controls, with the
specified label and variable value.

Initializer

# init(decorative:bundle:)

Creates an unlabeled, decorative image.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        decorative name: String,
        bundle: Bundle? = nil
    )

##  Parameters

`name`

    

The name of the image resource to lookup

`bundle`

    

The bundle to search for the image resource. If `nil`, SwiftUI uses the main
`Bundle`. Defaults to `nil`.

## Discussion

SwiftUI ignores this image for accessibility purposes.

## See Also

### Creating an image for decorative use

`init(decorative: String, variableValue: Double?, bundle: Bundle?)`

Creates an unlabeled, decorative image, with a variable value.

`init(decorative: CGImage, scale: CGFloat, orientation: Image.Orientation)`

Creates an unlabeled, decorative image based on a Core Graphics image
instance.

Initializer

# init(decorative:variableValue:bundle:)

Creates an unlabeled, decorative image, with a variable value.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init(
        decorative name: String,
        variableValue: Double?,
        bundle: Bundle? = nil
    )

##  Parameters

`name`

    

The name of the image resource to lookup.

`variableValue`

    

An optional value between `0.0` and `1.0` that the rendered image can use to
customize its appearance, if specified. If the symbol doesn’t support variable
values, this parameter has no effect.

`bundle`

    

The bundle to search for the image resource. If `nil`, SwiftUI uses the main
`Bundle`. Defaults to `nil`.

## Discussion

This initializer creates an image using a using a symbol in the specified
bundle. The rendered symbol may alter its appearance to represent the value
provided in `variableValue`.

Note

See WWDC22 session 10158: Adopt variable color in SF Symbols for details on
how to create symbols that support variable values.

SwiftUI ignores this image for accessibility purposes.

## See Also

### Creating an image for decorative use

`init(decorative: String, bundle: Bundle?)`

Creates an unlabeled, decorative image.

`init(decorative: CGImage, scale: CGFloat, orientation: Image.Orientation)`

Creates an unlabeled, decorative image based on a Core Graphics image
instance.

Initializer

# init(decorative:scale:orientation:)

Creates an unlabeled, decorative image based on a Core Graphics image
instance.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        decorative cgImage: CGImage,
        scale: CGFloat,
        orientation: Image.Orientation = .up
    )

##  Parameters

`cgImage`

    

The base graphical image.

`scale`

    

The scale factor for the image, with a value like `1.0`, `2.0`, or `3.0`.

`orientation`

    

The orientation of the image. The default is `Image.Orientation.up`.

## Discussion

SwiftUI ignores this image for accessibility purposes.

## See Also

### Creating an image for decorative use

`init(decorative: String, bundle: Bundle?)`

Creates an unlabeled, decorative image.

`init(decorative: String, variableValue: Double?, bundle: Bundle?)`

Creates an unlabeled, decorative image, with a variable value.

Initializer

# init(systemName:)

Creates a system symbol image.

iOS 13.0+  iPadOS 13.0+  macOS 11.0+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(systemName: String)

##  Parameters

`systemName`

    

The name of the system symbol image. Use the SF Symbols app to look up the
names of system symbol images.

## Discussion

This initializer creates an image using a system-provided symbol. Use SF
Symbols to find symbols and their corresponding names.

To create a custom symbol image from your app’s asset catalog, use
`init(_:bundle:)` instead.

## See Also

### Creating a system symbol image

`init(systemName: String, variableValue: Double?)`

Creates a system symbol image with a variable value.

Initializer

# init(systemName:variableValue:)

Creates a system symbol image with a variable value.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init(
        systemName: String,
        variableValue: Double?
    )

##  Parameters

`systemName`

    

The name of the system symbol image. Use the SF Symbols app to look up the
names of system symbol images.

`variableValue`

    

An optional value between `0.0` and `1.0` that the rendered image can use to
customize its appearance, if specified. If the symbol doesn’t support variable
values, this parameter has no effect. Use the SF Symbols app to look up which
symbols support variable values.

## Discussion

This initializer creates an image using a system-provided symbol. The rendered
symbol may alter its appearance to represent the value provided in
`variableValue`. Use SF Symbols (version 4.0 or later) to find system symbols
that support variable values and their corresponding names.

The following example shows the effect of creating the `"chart.bar.fill"`
symbol with different values.

To create a custom symbol image from your app’s asset catalog, use
`init(_:variableValue:bundle:)` instead.

## See Also

### Creating a system symbol image

`init(systemName: String)`

Creates a system symbol image.

Initializer

# init(uiImage:)

Creates a SwiftUI image from a UIKit image instance.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    init(uiImage: UIImage)

##  Parameters

`uiImage`

    

The UIKit image to wrap with a SwiftUI `Image` instance.

## See Also

### Creating an image from another image

`init(nsImage: NSImage)`

Creates a SwiftUI image from an AppKit image instance.

Initializer

# init(nsImage:)

Creates a SwiftUI image from an AppKit image instance.

macOS 10.15+

    
    
    init(nsImage: NSImage)

##  Parameters

`nsImage`

    

The AppKit image to wrap with a SwiftUI `Image`. instance.

## See Also

### Creating an image from another image

`init(uiImage: UIImage)`

Creates a SwiftUI image from a UIKit image instance.

Initializer

# init(size:label:opaque:colorMode:renderer:)

Initializes an image of the given size, with contents provided by a custom
rendering closure.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init(
        size: CGSize,
        label: Text? = nil,
        opaque: Bool = false,
        colorMode: ColorRenderingMode = .nonLinear,
        renderer: @escaping (inout GraphicsContext) -> Void
    )

##  Parameters

`size`

    

The size of the newly-created image.

`label`

    

The label associated with the image. SwiftUI uses the label for accessibility.

`opaque`

    

A Boolean value that indicates whether the image is fully opaque. This may
improve performance when `true`. Don’t render non-opaque pixels to an image
declared as opaque. Defaults to `false`.

`colorMode`

    

The working color space and storage format of the image. Defaults to
`ColorRenderingMode.nonLinear`.

`renderer`

    

A closure to draw the contents of the image. The closure receives a
`GraphicsContext` as its parameter.

## Discussion

Use this initializer to create an image by calling drawing commands on a
`GraphicsContext` provided to the `renderer` closure.

The following example shows a custom image created by passing a
`GraphicContext` to draw an ellipse and fill it with a gradient:

Instance Method

# resizable(capInsets:resizingMode:)

Sets the mode by which SwiftUI resizes an image to fit its space.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func resizable(
        capInsets: EdgeInsets = EdgeInsets(),
        resizingMode: Image.ResizingMode = .stretch
    ) -> Image

##  Parameters

`capInsets`

    

Inset values that indicate a portion of the image that SwiftUI doesn’t resize.

`resizingMode`

    

The mode by which SwiftUI resizes the image.

## Return Value

An image, with the new resizing behavior set.

Instance Method

# antialiased(_:)

Specifies whether SwiftUI applies antialiasing when rendering the image.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func antialiased(_ isAntialiased: Bool) -> Image

##  Parameters

`isAntialiased`

    

A Boolean value that specifies whether to allow antialiasing. Pass `true` to
allow antialising, `false` otherwise.

## Return Value

An image with the antialiasing behavior set.

## See Also

### Specifying rendering behavior

`func symbolRenderingMode(SymbolRenderingMode?) -> Image`

Sets the rendering mode for symbol images within this view.

`func renderingMode(Image.TemplateRenderingMode?) -> Image`

Indicates whether SwiftUI renders an image as-is, or by using a different
mode.

`func interpolation(Image.Interpolation) -> Image`

Specifies the current level of quality for rendering an image that requires
interpolation.

`enum TemplateRenderingMode`

A type that indicates how SwiftUI renders images.

`enum Interpolation`

The level of quality for rendering an image that requires interpolation, such
as a scaled image.

Instance Method

# symbolRenderingMode(_:)

Sets the rendering mode for symbol images within this view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func symbolRenderingMode(_ mode: SymbolRenderingMode?) -> Image

##  Parameters

`mode`

    

The symbol rendering mode to use.

## Return Value

A view that uses the rendering mode you supply.

## See Also

### Specifying rendering behavior

`func antialiased(Bool) -> Image`

Specifies whether SwiftUI applies antialiasing when rendering the image.

`func renderingMode(Image.TemplateRenderingMode?) -> Image`

Indicates whether SwiftUI renders an image as-is, or by using a different
mode.

`func interpolation(Image.Interpolation) -> Image`

Specifies the current level of quality for rendering an image that requires
interpolation.

`enum TemplateRenderingMode`

A type that indicates how SwiftUI renders images.

`enum Interpolation`

The level of quality for rendering an image that requires interpolation, such
as a scaled image.

Instance Method

# renderingMode(_:)

Indicates whether SwiftUI renders an image as-is, or by using a different
mode.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func renderingMode(_ renderingMode: Image.TemplateRenderingMode?) -> Image

##  Parameters

`renderingMode`

    

The mode SwiftUI uses to render images.

## Return Value

A modified `Image`.

## Discussion

The `Image.TemplateRenderingMode` enumeration has two cases:
`Image.TemplateRenderingMode.original` and
`Image.TemplateRenderingMode.template`. The original mode renders pixels as
they appear in the original source image. Template mode renders all
nontransparent pixels as the foreground color, which you can use for purposes
like creating image masks.

The following example shows both rendering modes, as applied to an icon image
of a green circle with darker green border:

You also use `renderingMode` to produce multicolored system graphics from the
SF Symbols set. Use the `Image.TemplateRenderingMode.original` mode to apply a
foreground color to all parts of the symbol except those that have a distinct
color in the graphic. The following example shows three uses of the
`person.crop.circle.badge.plus` symbol to achieve different effects:

  * A default appearance with no foreground color or template rendering mode specified. The symbol appears all black in light mode, and all white in Dark Mode.

  * The multicolor behavior achieved by using `original` template rendering mode, along with a blue foreground color. This mode causes the graphic to override the foreground color for distinctive parts of the image, in this case the plus icon.

  * A single-color template behavior achieved by using `template` rendering mode with a blue foreground color. This mode applies the foreground color to the entire image, regardless of the user’s Appearance preferences.

Use the SF Symbols app to find system images that offer the multicolor
feature. Keep in mind that some multicolor symbols use both the foreground and
accent colors.

## See Also

### Specifying rendering behavior

`func antialiased(Bool) -> Image`

Specifies whether SwiftUI applies antialiasing when rendering the image.

`func symbolRenderingMode(SymbolRenderingMode?) -> Image`

Sets the rendering mode for symbol images within this view.

`func interpolation(Image.Interpolation) -> Image`

Specifies the current level of quality for rendering an image that requires
interpolation.

`enum TemplateRenderingMode`

A type that indicates how SwiftUI renders images.

`enum Interpolation`

The level of quality for rendering an image that requires interpolation, such
as a scaled image.

Instance Method

# interpolation(_:)

Specifies the current level of quality for rendering an image that requires
interpolation.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func interpolation(_ interpolation: Image.Interpolation) -> Image

##  Parameters

`interpolation`

    

The quality level, expressed as a value of the `Interpolation` type, that
SwiftUI applies when interpolating an image.

## Return Value

An image with the given interpolation value set.

## Discussion

See the article Fitting images into available space for examples of using
`interpolation(_:)` when scaling an `Image`.

## See Also

### Specifying rendering behavior

`func antialiased(Bool) -> Image`

Specifies whether SwiftUI applies antialiasing when rendering the image.

`func symbolRenderingMode(SymbolRenderingMode?) -> Image`

Sets the rendering mode for symbol images within this view.

`func renderingMode(Image.TemplateRenderingMode?) -> Image`

Indicates whether SwiftUI renders an image as-is, or by using a different
mode.

`enum TemplateRenderingMode`

A type that indicates how SwiftUI renders images.

`enum Interpolation`

The level of quality for rendering an image that requires interpolation, such
as a scaled image.

Enumeration

# Image.TemplateRenderingMode

A type that indicates how SwiftUI renders images.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    enum TemplateRenderingMode

## Topics

### Getting rendering modes

`case original`

A mode that renders pixels of bitmap images as-is.

`case template`

A mode that renders all non-transparent pixels as the foreground color.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Specifying rendering behavior

`func antialiased(Bool) -> Image`

Specifies whether SwiftUI applies antialiasing when rendering the image.

`func symbolRenderingMode(SymbolRenderingMode?) -> Image`

Sets the rendering mode for symbol images within this view.

`func renderingMode(Image.TemplateRenderingMode?) -> Image`

Indicates whether SwiftUI renders an image as-is, or by using a different
mode.

`func interpolation(Image.Interpolation) -> Image`

Specifies the current level of quality for rendering an image that requires
interpolation.

`enum Interpolation`

The level of quality for rendering an image that requires interpolation, such
as a scaled image.

Enumeration

# Image.Interpolation

The level of quality for rendering an image that requires interpolation, such
as a scaled image.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    enum Interpolation

## Overview

The `interpolation(_:)` modifier specifies the interpolation behavior when
using the `resizable(capInsets:resizingMode:)` modifier on an `Image`. Use
this behavior to prioritize rendering performance or image quality.

## Topics

### Getting interpolation options

`case high`

A value that indicates a high level of interpolation quality, which may slow
down image rendering.

`case low`

A value that indicates a low level of interpolation quality, which may speed
up image rendering.

`case medium`

A value that indicates a medium level of interpolation quality, between the
low- and high-quality values.

`case none`

A value that indicates SwiftUI doesn’t interpolate image data.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Specifying rendering behavior

`func antialiased(Bool) -> Image`

Specifies whether SwiftUI applies antialiasing when rendering the image.

`func symbolRenderingMode(SymbolRenderingMode?) -> Image`

Sets the rendering mode for symbol images within this view.

`func renderingMode(Image.TemplateRenderingMode?) -> Image`

Indicates whether SwiftUI renders an image as-is, or by using a different
mode.

`func interpolation(Image.Interpolation) -> Image`

Specifies the current level of quality for rendering an image that requires
interpolation.

`enum TemplateRenderingMode`

A type that indicates how SwiftUI renders images.

Instance Method

# allowedDynamicRange(_:)

Returns a new image configured with the specified allowed dynamic range.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    func allowedDynamicRange(_ range: Image.DynamicRange?) -> Image

##  Parameters

`range`

    

the requested dynamic range, or nil to restore the default allowed range.

## Return Value

a new image.

## Discussion

The following example enables HDR rendering for a specific image view,
assuming that the image has an HDR (ITU-R 2100) color space and the output
device supports it:

## See Also

### Specifying dynamic range

`var allowedDynamicRange: Image.DynamicRange?`

The allowed dynamic range for the view, or nil.

`struct DynamicRange`

Instance Property

# allowedDynamicRange

The allowed dynamic range for the view, or nil.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    var allowedDynamicRange: Image.DynamicRange? { get set }

## See Also

### View attributes

`var backgroundMaterial: Material?`

The material underneath the current view.

`var backgroundProminence: BackgroundProminence`

The prominence of the background underneath views associated with this
environment.

`var backgroundStyle: AnyShapeStyle?`

An optional style that overrides the default system background style when set.

`var badgeProminence: BadgeProminence`

The prominence to apply to badges associated with this environment.

`var contentTransition: ContentTransition`

The current method of animating the contents of views.

`var contentTransitionAddsDrawingGroup: Bool`

A Boolean value that controls whether views that render content transitions
use GPU-accelerated rendering.

`var defaultMinListHeaderHeight: CGFloat?`

The default minimum height of a header in a list.

`var defaultMinListRowHeight: CGFloat`

The default minimum height of a row in a `List`. The default minimum height of
a row in a list.

`var isFocusEffectEnabled: Bool`

A Boolean value that indicates whether the view associated with this
environment allows focus effects to be displayed.

`var headerProminence: Prominence`

The prominence to apply to section headers within a view.

`var physicalMetrics: PhysicalMetricsConverter`

The physical metrics associated with a scene.

`var realityKitScene: Scene?`

`var redactionReasons: RedactionReasons`

The current redaction reasons applied to the view hierarchy.

`var springLoadingBehavior: SpringLoadingBehavior`

The behavior of spring loaded interactions for the views associated with this
environment.

`var symbolRenderingMode: SymbolRenderingMode?`

The current symbol rendering mode, or `nil` denoting that the mode is picked
automatically using the current image and foreground style as parameters.

`var symbolVariants: SymbolVariants`

The symbol variant to use in this environment.

Structure

# Image.DynamicRange

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    struct DynamicRange

## Topics

### Getting dynamic range values

`static let standard: Image.DynamicRange`

Restrict the image content dynamic range to the standard range.

`static let high: Image.DynamicRange`

Allow image content to use an unrestricted extended range.

`static let constrainedHigh: Image.DynamicRange`

Allow image content to use some extended range. This is appropriate for
placing HDR content next to SDR content.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Specifying dynamic range

`func allowedDynamicRange(Image.DynamicRange?) -> Image`

Returns a new image configured with the specified allowed dynamic range.

`var allowedDynamicRange: Image.DynamicRange?`

The allowed dynamic range for the view, or nil.

