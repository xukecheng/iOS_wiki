Structure

# Image

A view that displays an image.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct Image

## Overview

Use an `Image` instance when you want to add images to your SwiftUI app. You
can create images from many sources:

  * Image files in your app’s asset library or bundle. Supported types include PNG, JPEG, HEIC, and more.

  * Instances of platform-specific image types, like `UIImage` and `NSImage`.

  * A bitmap stored in a Core Graphics `CGImage` instance.

  * System graphics from the SF Symbols set.

The following example shows how to load an image from the app’s asset library
or bundle and scale it to fit within its container:

You can use methods on the `Image` type as well as standard view modifiers to
adjust the size of the image to fit your app’s interface. Here, the `Image`
type’s `resizable(capInsets:resizingMode:)` method scales the image to fit the
current view. Then, the `aspectRatio(_:contentMode:)` view modifier adjusts
this resizing behavior to maintain the image’s original aspect ratio, rather
than scaling the x- and y-axes independently to fill all four sides of the
view. The article Fitting images into available space shows how to apply
scaling, clipping, and tiling to `Image` instances of different sizes.

An `Image` is a late-binding token; the system resolves its actual value only
when it’s about to use the image in an environment.

### Making images accessible

To use an image as a control, use one of the initializers that takes a `label`
parameter. This allows the system’s accessibility frameworks to use the label
as the name of the control for users who use features like VoiceOver. For
images that are only present for aesthetic reasons, use an initializer with
the `decorative` parameter; the accessibility systems ignore these images.

## Topics

### Creating an image

`init(String, bundle: Bundle?)`

Creates a labeled image that you can use as content for controls.

`init(String, variableValue: Double?, bundle: Bundle?)`

Creates a labeled image that you can use as content for controls, with a
variable value.

`init(ImageResource)`

Initialize an `Image` with an image resource.

### Creating an image for use as a control

`init(String, bundle: Bundle?, label: Text)`

Creates a labeled image that you can use as content for controls, with the
specified label.

`init(String, variableValue: Double?, bundle: Bundle?, label: Text)`

Creates a labeled image that you can use as content for controls, with the
specified label and variable value.

`init(CGImage, scale: CGFloat, orientation: Image.Orientation, label: Text)`

Creates a labeled image based on a Core Graphics image instance, usable as
content for controls.

### Creating an image for decorative use

`init(decorative: String, bundle: Bundle?)`

Creates an unlabeled, decorative image.

`init(decorative: String, variableValue: Double?, bundle: Bundle?)`

Creates an unlabeled, decorative image, with a variable value.

`init(decorative: CGImage, scale: CGFloat, orientation: Image.Orientation)`

Creates an unlabeled, decorative image based on a Core Graphics image
instance.

### Creating a system symbol image

`init(systemName: String)`

Creates a system symbol image.

`init(systemName: String, variableValue: Double?)`

Creates a system symbol image with a variable value.

### Creating an image from another image

`init(uiImage: UIImage)`

Creates a SwiftUI image from a UIKit image instance.

`init(nsImage: NSImage)`

Creates a SwiftUI image from an AppKit image instance.

### Creating an image from drawing instructions

`init(size: CGSize, label: Text?, opaque: Bool, colorMode: ColorRenderingMode,
renderer: (inout GraphicsContext) -> Void)`

Initializes an image of the given size, with contents provided by a custom
rendering closure.

### Resizing images

`func resizable(capInsets: EdgeInsets, resizingMode: Image.ResizingMode) ->
Image`

Sets the mode by which SwiftUI resizes an image to fit its space.

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

`enum Interpolation`

The level of quality for rendering an image that requires interpolation, such
as a scaled image.

### Specifying dynamic range

`func allowedDynamicRange(Image.DynamicRange?) -> Image`

Returns a new image configured with the specified allowed dynamic range.

`var allowedDynamicRange: Image.DynamicRange?`

The allowed dynamic range for the view, or nil.

`struct DynamicRange`

## Relationships

### Conforms To

  * `Equatable`
  * `Sendable`
  * `Transferable`
  * `View`

Article

# Fitting images into available space

Adjust the size and shape of images in your app’s user interface by applying
view modifiers.

## Overview

Image sizes vary widely, from single-pixel PNG files to digital photography
images with millions of pixels. Because device sizes also vary, apps commonly
need to make runtime adjustments to image sizes so they fit within the visible
user interface. SwiftUI provides modifiers to scale, clip, and transform
images to fit your interface perfectly.

### Scale a large image to fit its container using resizing

Consider the image `Landscape_4.jpg`, a photograph with the dimensions 4032 x
3024, showing a water wheel, the surrounding building, and the sky above.

The following example loads the image directly into an `Image` view, and then
places it in a 300 x 400 point frame, with a blue border:

As seen in the following screenshot, the image data loads at full size into
the view, so only the clouds from the upper left of the original image are
visible. Because the image renders at full size, and the blue frame is smaller
than the original image, the image displays beyond the area bounded by the
frame.

To fix this, you need to apply two modifiers to the `Image`:

  * `resizable(capInsets:resizingMode:)` tells the image view to adjust the image representation to match the size of the view. By default, this modifier scales the image by reducing the size of larger images and enlarges images smaller than the view. By itself, this modifier scales each axis of the image independently.

  * `aspectRatio(_:contentMode:)` corrects the behavior where the image scaling is different for each axis. This preserves the image’s original aspect ratio, using one of two strategies defined by the `ContentMode` enumeration. `ContentMode.fit` scales the image to fit the view size along one axis, possibly leaving empty space along the other axis. `ContentMode.fill` scales the image to fill the entire view.

### Keep image data inside the view’s bounds using clipping

If you use `ContentMode.fill` when scaling an image, a portion of an image may
extend beyond the view’s bounds, unless the view matches the image’s aspect
ratio exactly. The following example illustrates this problem:

To prevent this problem, add the `clipped(antialiased:)` modifier. This
modifier simply cuts off excess image rendering at the bounding frame of the
view. Optionally, you can add an antialiasing behavior to apply smoothing to
the edges of the clipping rectangle; this parameter defaults to `false`. The
following example shows the effect of adding clipping to the previous fill-
mode example:

### Use interpolation flags to adjust rendered image quality

Rendering an image at anything other than its original size requires
_interpolation_ : using the existing image data to approximate a
representation at a different size. Different approaches to performing
interpolation have different trade-offs between computational complexity and
visual quality of the rendered image. You can use the `interpolation(_:)`
modifier to provide a hint for SwiftUI rendering behavior.

It’s easier to see the effect of interpolation when scaling a smaller image
into a larger space, because the rendered image requires more image data than
is available. Consider the following example, which renders a 34 x 34 image
named `dot_green` into the same 300 x 400 container frame as before:

Passing the `Image.Interpolation.none` value to `interpolation(_:)` produces a
highly pixelated image when rendered.

If you change the interpolation value to `Image.Interpolation.medium`, SwiftUI
smoothes out the pixel data to produce an image that isn’t as pixelated:

Tip

You can also specify interpolation behavior when scaling images down, to
ensure the highest quality image possible, fastest rendering time, or a
behavior in between.

### Fill a space with a repeating image using tiling

When you have an image that’s much smaller than the space you want to render
it into, another option to fill the space is _tiling_ : repeating the same
image over and over again. To tile an image, pass the
`Image.ResizingMode.tile` parameter to the
`resizable(capInsets:resizingMode:)` modifier:

Tiling can be particuarly useful when using an image that, when placed end-to-
end with copies of itself, creates a larger pattern with no visual
discontinuities.

## See Also

### Configuring an image

`func imageScale(Image.Scale) -> some View`

Scales images within the view according to one of the relative sizes available
including small, medium, and large images sizes.

`var imageScale: Image.Scale`

The image scale for this environment.

`enum Scale`

A scale to apply to vector images relative to text.

`enum Orientation`

The orientation of an image.

`enum ResizingMode`

The modes that SwiftUI uses to resize an image to fit within its containing
view.

Instance Method

# imageScale(_:)

Scales images within the view according to one of the relative sizes available
including small, medium, and large images sizes.

iOS 13.0+  iPadOS 13.0+  macOS 11.0+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func imageScale(_ scale: Image.Scale) -> some View
    

##  Parameters

`scale`

    

One of the relative sizes provided by the image scale enumeration.

## Discussion

The example below shows the relative scaling effect. The system renders the
image at a relative size based on the available space and configuration
options of the image it is scaling.

## See Also

### Configuring an image

Fitting images into available space

Adjust the size and shape of images in your app’s user interface by applying
view modifiers.

`var imageScale: Image.Scale`

The image scale for this environment.

`enum Scale`

A scale to apply to vector images relative to text.

`enum Orientation`

The orientation of an image.

`enum ResizingMode`

The modes that SwiftUI uses to resize an image to fit within its containing
view.

Instance Property

# imageScale

The image scale for this environment.

iOS 13.0+  iPadOS 13.0+  macOS 11.0+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var imageScale: Image.Scale { get set }

## See Also

### Configuring an image

Fitting images into available space

Adjust the size and shape of images in your app’s user interface by applying
view modifiers.

`func imageScale(Image.Scale) -> some View`

Scales images within the view according to one of the relative sizes available
including small, medium, and large images sizes.

`enum Scale`

A scale to apply to vector images relative to text.

`enum Orientation`

The orientation of an image.

`enum ResizingMode`

The modes that SwiftUI uses to resize an image to fit within its containing
view.

Enumeration

# Image.Scale

A scale to apply to vector images relative to text.

iOS 13.0+  iPadOS 13.0+  macOS 11.0+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    enum Scale

## Overview

Use this type with the `imageScale(_:)` modifier, or the `imageScale`
environment key, to set the image scale.

The following example shows the three `Scale` values as applied to a system
symbol image, each set against a text view:

## Topics

### Getting image scales

`case small`

A scale that produces small images.

`case medium`

A scale that produces medium-sized images.

`case large`

A scale that produces large images.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Configuring an image

Fitting images into available space

Adjust the size and shape of images in your app’s user interface by applying
view modifiers.

`func imageScale(Image.Scale) -> some View`

Scales images within the view according to one of the relative sizes available
including small, medium, and large images sizes.

`var imageScale: Image.Scale`

The image scale for this environment.

`enum Orientation`

The orientation of an image.

`enum ResizingMode`

The modes that SwiftUI uses to resize an image to fit within its containing
view.

Enumeration

# Image.Orientation

The orientation of an image.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    enum Orientation

## Overview

Many image formats such as JPEG include orientation metadata in the image
data. In other cases, you can specify image orientation in code. Properly
specifying orientation is often important both for displaying the image and
for certain kinds of image processing.

In SwiftUI, you provide an orientation value when initializing an `Image` from
an existing `CGImage`.

## Topics

### Getting image orientations

`case up`

A value that indicates the original pixel data matches the image’s intended
display orientation.

`case down`

A value that indicates a 180° rotation of the image from the orientation of
its original pixel data.

`case left`

A value that indicates a 90° counterclockwise rotation from the orientation of
its original pixel data.

`case right`

A value that indicates a 90° clockwise rotation of the image from the
orientation of its original pixel data.

### Getting mirrored image orientation

`case upMirrored`

A value that indicates a horizontal flip of the image from the orientation of
its original pixel data.

`case downMirrored`

A value that indicates a vertical flip of the image from the orientation of
its original pixel data.

`case leftMirrored`

A value that indicates a 90° clockwise rotation and horizontal flip of the
image from the orientation of its original pixel data.

`case rightMirrored`

A value that indicates a 90° counterclockwise rotation and horizontal flip
from the orientation of its original pixel data.

## Relationships

### Conforms To

  * `CaseIterable`
  * `Equatable`
  * `Hashable`
  * `RawRepresentable`
  * `Sendable`

## See Also

### Configuring an image

Fitting images into available space

Adjust the size and shape of images in your app’s user interface by applying
view modifiers.

`func imageScale(Image.Scale) -> some View`

Scales images within the view according to one of the relative sizes available
including small, medium, and large images sizes.

`var imageScale: Image.Scale`

The image scale for this environment.

`enum Scale`

A scale to apply to vector images relative to text.

`enum ResizingMode`

The modes that SwiftUI uses to resize an image to fit within its containing
view.

Enumeration

# Image.ResizingMode

The modes that SwiftUI uses to resize an image to fit within its containing
view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    enum ResizingMode

## Topics

### Getting resizing modes

`case stretch`

A mode to enlarge or reduce the size of an image so that it fills the
available space.

`case tile`

A mode to repeat the image at its original size, as many times as necessary to
fill the available space.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Configuring an image

Fitting images into available space

Adjust the size and shape of images in your app’s user interface by applying
view modifiers.

`func imageScale(Image.Scale) -> some View`

Scales images within the view according to one of the relative sizes available
including small, medium, and large images sizes.

`var imageScale: Image.Scale`

The image scale for this environment.

`enum Scale`

A scale to apply to vector images relative to text.

`enum Orientation`

The orientation of an image.

Structure

# AsyncImage

A view that asynchronously loads and displays an image.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    struct AsyncImage<Content> where Content : View

## Overview

This view uses the shared `URLSession` instance to load an image from the
specified URL, and then display it. For example, you can display an icon
that’s stored on a server:

Until the image loads, the view displays a standard placeholder that fills the
available space. After the load completes successfully, the view updates to
display the image. In the example above, the icon is smaller than the frame,
and so appears smaller than the placeholder.

You can specify a custom placeholder using
`init(url:scale:content:placeholder:)`. With this initializer, you can also
use the `content` parameter to manipulate the loaded image. For example, you
can add a modifier to make the loaded image resizable:

For this example, SwiftUI shows a `ProgressView` first, and then the image
scaled to fit in the specified frame:

Important

You can’t apply image-specific modifiers, like
`resizable(capInsets:resizingMode:)`, directly to an `AsyncImage`. Instead,
apply them to the `Image` instance that your `content` closure gets when
defining the view’s appearance.

To gain more control over the loading process, use the
`init(url:scale:transaction:content:)` initializer, which takes a `content`
closure that receives an `AsyncImagePhase` to indicate the state of the
loading operation. Return a view that’s appropriate for the current phase:

## Topics

### Loading an image

`init(url: URL?, scale: CGFloat)`

Loads and displays an image from the specified URL.

`init<I, P>(url: URL?, scale: CGFloat, content: (Image) -> I, placeholder: ()
-> P)`

Loads and displays a modifiable image from the specified URL using a custom
placeholder until the image loads.

### Loading an image in phases

`init(url: URL?, scale: CGFloat, transaction: Transaction, content:
(AsyncImagePhase) -> Content)`

Loads and displays a modifiable image from the specified URL in phases.

## Relationships

### Conforms To

  * `View`

## See Also

### Loading images asynchronously

`enum AsyncImagePhase`

The current phase of the asynchronous image loading operation.

Enumeration

# AsyncImagePhase

The current phase of the asynchronous image loading operation.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    enum AsyncImagePhase

## Overview

When you create an `AsyncImage` instance with the
`init(url:scale:transaction:content:)` initializer, you define the appearance
of the view using a `content` closure. SwiftUI calls the closure with a phase
value at different points during the load operation to indicate the current
state. Use the phase to decide what to draw. For example, you can draw the
loaded image if it exists, a view that indicates an error, or a placeholder:

## Topics

### Getting load phases

`case empty`

No image is loaded.

`case success(Image)`

An image succesfully loaded.

`case failure(any Error)`

An image failed to load with an error.

### Getting the image

`var image: Image?`

The loaded image, if any.

### Getting the error

`var error: (any Error)?`

The error that occurred when attempting to load an image, if any.

## Relationships

### Conforms To

  * `Sendable`

## See Also

### Loading images asynchronously

`struct AsyncImage`

A view that asynchronously loads and displays an image.

Instance Method

# symbolVariant(_:)

Makes symbols within the view show a particular variant.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func symbolVariant(_ variant: SymbolVariants) -> some View
    

##  Parameters

`variant`

    

The variant to use for symbols. Use the values in `SymbolVariants`.

## Return Value

A view that applies the specified symbol variant or variants to itself and its
child views.

## Discussion

When you want all the SF Symbols in a part of your app’s user interface to use
the same variant, use the `symbolVariant(_:)` modifier with a `SymbolVariants`
value, like `fill`:

A symbol that doesn’t have the specified variant remains unaffected. In the
example above, the `list.bullet` symbol doesn’t have a filled variant, so the
`symbolVariant(_:)` modifer has no effect.

If you apply the modifier more than once, its effects accumulate.
Alternatively, you can apply multiple variants in one call:

All of the labels in the code above produce the same output:

You can apply all these variants in any order, but if you apply more than one
shape variant, the one closest to the symbol takes precedence. For example,
the following image uses the `square` shape:

To cause a symbol to ignore the variants currently in the environment,
directly set the `symbolVariants` environment value to `none` using the
`environment(_:_:)` modifer.

## See Also

### Setting a symbol variant

`var symbolVariants: SymbolVariants`

The symbol variant to use in this environment.

`struct SymbolVariants`

A variant of a symbol.

Instance Property

# symbolVariants

The symbol variant to use in this environment.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var symbolVariants: SymbolVariants { get set }

## Discussion

You set this environment value indirectly by using the `symbolVariant(_:)`
view modifier. However, you access the environment variable directly using the
`environment(_:_:)` modifier. Do this when you want to use the `none` variant
to ignore the value that’s already in the environment:

## See Also

### Setting a symbol variant

`func symbolVariant(SymbolVariants) -> some View`

Makes symbols within the view show a particular variant.

`struct SymbolVariants`

A variant of a symbol.

Structure

# SymbolVariants

A variant of a symbol.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    struct SymbolVariants

## Overview

Many of the SF Symbols that you can add to your app using an `Image` or a
`Label` instance have common variants, like a filled version or a version
that’s contained within a circle. The symbol’s name indicates the variant:

You can configure a part of your view hierarchy to use a particular variant
for all symbols in that view and its child views using `SymbolVariants`. Add
the `symbolVariant(_:)` modifier to a view to set a variant for that view’s
environment. For example, you can use the modifier to create the same set of
labels as in the example above, using only the base name of the symbol in the
label declarations:

Alternatively, you can set the variant in the environment directly by passing
the `symbolVariants` environment value to the `environment(_:_:)` modifier:

SwiftUI sets a variant for you in some environments. For example, SwiftUI
automatically applies the `fill` symbol variant for items that appear in the
`content` closure of the `swipeActions(edge:allowsFullSwipe:content:)` method,
or as the tab bar items of a `TabView`.

## Topics

### Getting symbol variants

`static let none: SymbolVariants`

No variant for a symbol.

`static let circle: SymbolVariants`

A variant that encapsulates the symbol in a circle.

`static let square: SymbolVariants`

A variant that encapsulates the symbol in a square.

`static let rectangle: SymbolVariants`

A variant that encapsulates the symbol in a rectangle.

`static let fill: SymbolVariants`

A variant that fills the symbol.

`static let slash: SymbolVariants`

A variant that draws a slash through the symbol.

### Modifying a variant

`var circle: SymbolVariants`

A version of the variant that’s encapsulated in a circle.

`var square: SymbolVariants`

A version of the variant that’s encapsulated in a square.

`var rectangle: SymbolVariants`

A version of the variant that’s encapsulated in a rectangle.

`var fill: SymbolVariants`

A filled version of the variant.

`var slash: SymbolVariants`

A slashed version of the variant.

### Comparing variants

`func contains(SymbolVariants) -> Bool`

Returns a Boolean value that indicates whether the current variant contains
the specified variant.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Setting a symbol variant

`func symbolVariant(SymbolVariants) -> some View`

Makes symbols within the view show a particular variant.

`var symbolVariants: SymbolVariants`

The symbol variant to use in this environment.

Instance Method

# symbolEffect(_:options:isActive:)

Returns a new view with a symbol effect added to it.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func symbolEffect<T>(
        _ effect: T,
        options: SymbolEffectOptions = .default,
        isActive: Bool = true
    ) -> some View where T : IndefiniteSymbolEffect, T : SymbolEffect
    

##  Parameters

`effect`

    

A symbol effect to add to the view. Existing effects added by ancestors of the
view are preserved, but may be overridden by the new effect. Added effects
will be applied to the ``SwiftUI/Image` views contained by the child view.

`isActive`

    

whether the effect is active or inactive.

## Return Value

a copy of the view with a symbol effect added.

## Discussion

The following example adds a repeating pulse effect to two symbol images:

## See Also

### Managing symbol effects

`func symbolEffect<T, U>(T, options: SymbolEffectOptions, value: U) -> some
View`

Returns a new view with a symbol effect added to it.

`func symbolEffectsRemoved(Bool) -> some View`

Returns a new view with its inherited symbol image effects either removed or
left unchanged.

`struct SymbolEffectTransition`

Creates a transition that applies the Appear or Disappear symbol animation to
symbol images within the inserted or removed view hierarchy.

Instance Method

# symbolEffect(_:options:value:)

Returns a new view with a symbol effect added to it.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func symbolEffect<T, U>(
        _ effect: T,
        options: SymbolEffectOptions = .default,
        value: U
    ) -> some View where T : DiscreteSymbolEffect, T : SymbolEffect, U : Equatable
    

##  Parameters

`effect`

    

A symbol effect to add to the view. Existing effects added by ancestors of the
view are preserved, but may be overridden by the new effect. Added effects
will be applied to the ``SwiftUI/Image` views contained by the child view.

`value`

    

the value to monitor for changes, the animation is triggered each time the
value changes.

## Return Value

a copy of the view with a symbol effect added.

## Discussion

The following example adds a bounce effect to two symbol images, the animation
will play each time `counter` changes:

## See Also

### Managing symbol effects

`func symbolEffect<T>(T, options: SymbolEffectOptions, isActive: Bool) -> some
View`

Returns a new view with a symbol effect added to it.

`func symbolEffectsRemoved(Bool) -> some View`

Returns a new view with its inherited symbol image effects either removed or
left unchanged.

`struct SymbolEffectTransition`

Creates a transition that applies the Appear or Disappear symbol animation to
symbol images within the inserted or removed view hierarchy.

Instance Method

# symbolEffectsRemoved(_:)

Returns a new view with its inherited symbol image effects either removed or
left unchanged.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func symbolEffectsRemoved(_ isEnabled: Bool = true) -> some View
    

##  Parameters

`isEnabled`

    

Whether to remove inherited symbol effects or not.

## Return Value

a copy of the view with its symbol effects either removed or left unchanged.

## Discussion

The following example adds a repeating pulse effect to two symbol images, but
then disables the effect on one of them:

## See Also

### Managing symbol effects

`func symbolEffect<T>(T, options: SymbolEffectOptions, isActive: Bool) -> some
View`

Returns a new view with a symbol effect added to it.

`func symbolEffect<T, U>(T, options: SymbolEffectOptions, value: U) -> some
View`

Returns a new view with a symbol effect added to it.

`struct SymbolEffectTransition`

Creates a transition that applies the Appear or Disappear symbol animation to
symbol images within the inserted or removed view hierarchy.

Structure

# SymbolEffectTransition

Creates a transition that applies the Appear or Disappear symbol animation to
symbol images within the inserted or removed view hierarchy.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    @frozen
    struct SymbolEffectTransition

## Overview

Other views are unaffected by this transition.

## Topics

### Creating a transition

`init<T>(effect: T, options: SymbolEffectOptions)`

## Relationships

### Conforms To

  * `Transition`

## See Also

### Managing symbol effects

`func symbolEffect<T>(T, options: SymbolEffectOptions, isActive: Bool) -> some
View`

Returns a new view with a symbol effect added to it.

`func symbolEffect<T, U>(T, options: SymbolEffectOptions, value: U) -> some
View`

Returns a new view with a symbol effect added to it.

`func symbolEffectsRemoved(Bool) -> some View`

Returns a new view with its inherited symbol image effects either removed or
left unchanged.

Instance Method

# symbolRenderingMode(_:)

Sets the rendering mode for symbol images within this view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func symbolRenderingMode(_ mode: SymbolRenderingMode?) -> some View
    

##  Parameters

`mode`

    

The symbol rendering mode to use.

## Return Value

A view that uses the rendering mode you supply.

## See Also

### Setting symbol rendering modes

`var symbolRenderingMode: SymbolRenderingMode?`

The current symbol rendering mode, or `nil` denoting that the mode is picked
automatically using the current image and foreground style as parameters.

`struct SymbolRenderingMode`

A symbol rendering mode.

Instance Property

# symbolRenderingMode

The current symbol rendering mode, or `nil` denoting that the mode is picked
automatically using the current image and foreground style as parameters.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var symbolRenderingMode: SymbolRenderingMode? { get set }

## See Also

### Setting symbol rendering modes

`func symbolRenderingMode(SymbolRenderingMode?) -> some View`

Sets the rendering mode for symbol images within this view.

`struct SymbolRenderingMode`

A symbol rendering mode.

Structure

# SymbolRenderingMode

A symbol rendering mode.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    struct SymbolRenderingMode

## Topics

### Getting symbol rendering modes

`static let hierarchical: SymbolRenderingMode`

A mode that renders symbols as multiple layers, with different opacities
applied to the foreground style.

`static let monochrome: SymbolRenderingMode`

A mode that renders symbols as a single layer filled with the foreground
style.

`static let multicolor: SymbolRenderingMode`

A mode that renders symbols as multiple layers with their inherit styles.

`static let palette: SymbolRenderingMode`

A mode that renders symbols as multiple layers, with different styles applied
to the layers.

## Relationships

### Conforms To

  * `Sendable`

## See Also

### Setting symbol rendering modes

`func symbolRenderingMode(SymbolRenderingMode?) -> some View`

Sets the rendering mode for symbol images within this view.

`var symbolRenderingMode: SymbolRenderingMode?`

The current symbol rendering mode, or `nil` denoting that the mode is picked
automatically using the current image and foreground style as parameters.

Class

# ImageRenderer

An object that creates images from SwiftUI views.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    final class ImageRenderer<Content> where Content : View

## Overview

Use `ImageRenderer` to export bitmap image data from a SwiftUI view. You
initialize the renderer with a view, then render images on demand, either by
calling the `render(rasterizationScale:renderer:)` method, or by using the
renderer’s properties to create a `CGImage`, `NSImage`, or `UIImage`.

By drawing to a `Canvas` and exporting with an `ImageRenderer`, you can
generate images from any progammatically-rendered content, like paths, shapes,
gradients, and more. You can also render standard SwiftUI views like `Text`
views, or containers of multiple view types.

The following example uses a private `createAwardView(forUser:date:)` method
to create a game app’s view of a trophy symbol with a user name and date. This
view combines a `Canvas` that applies a shadow filter with two `Text` views
into a `VStack`. A `Button` allows the person to save this view. The button’s
action uses an `ImageRenderer` to rasterize a `CGImage` and then calls a
private `uploadAchievementImage(_:)` method to encode and upload the image.

Because `ImageRenderer` conforms to `ObservableObject`, you can use it to
produce a stream of images as its properties change. Subscribe to the
renderer’s `objectWillChange` publisher, then use the renderer to rasterize a
new image each time the subscriber receives an update.

Important

`ImageRenderer` output only includes views that SwiftUI renders, such as text,
images, shapes, and composite views of these types. It does not render views
provided by native platform frameworks (AppKit and UIKit) such as web views,
media players, and some controls. For these views, `ImageRenderer` displays a
placeholder image, similar to the behavior of
`drawingGroup(opaque:colorMode:)`.

### Rendering to a PDF context

The `render(rasterizationScale:renderer:)` method renders the specified view
to any `CGContext`. That means you aren’t limited to creating a rasterized
`CGImage`. For example, you can generate PDF data by rendering to a PDF
context. The resulting PDF maintains resolution-independence for supported
members of the view hierarchy, such as text, symbol images, lines, shapes, and
fills.

The following example uses the `createAwardView(forUser:date:)` method from
the previous example, and exports its contents as an 800-by-600 point PDF to
the file URL `renderURL`. It uses the `size` parameter sent to the rendering
closure to center the `trophyAndDate` view vertically and horizontally on the
page.

### Creating an image from drawing instructions

`ImageRenderer` makes it possible to create a custom image by drawing into a
`Canvas`, rendering a `CGImage` from it, and using that to initialize an
`Image`. To simplify this process, use the `Image` initializer
`init(size:label:opaque:colorMode:renderer:)`, which takes a closure whose
argument is a `GraphicsContext` that you can directly draw into.

## Topics

### Creating an image renderer

`init(content: Content)`

Creates a renderer object with a source content view.

### Providing the source view

`var content: Content`

The root view rendered by this image renderer.

### Accessing renderer properties

`var proposedSize: ProposedViewSize`

The size proposed to the root view.

`var scale: CGFloat`

The scale at which to render the image.

`var isOpaque: Bool`

A Boolean value that indicates whether the alpha channel of the image is fully
opaque.

`var colorMode: ColorRenderingMode`

The working color space and storage format of the image.

### Rendering images

`func render(rasterizationScale: CGFloat, renderer: (CGSize, (CGContext) ->
Void) -> Void)`

Draws the renderer’s current contents to an arbitrary Core Graphics context.

`var cgImage: CGImage?`

The current contents of the view, rasterized as a Core Graphics image.

`var nsImage: NSImage?`

The current contents of the view, rasterized as an AppKit image.

`var uiImage: UIImage?`

The current contents of the view, rasterized as a UIKit image.

### Producing a stream of images

`let objectWillChange: PassthroughSubject<Void, Never>`

A publisher that informs subscribers of changes to the image.

## Relationships

### Conforms To

  * `Observable`
  * `ObservableObject`

