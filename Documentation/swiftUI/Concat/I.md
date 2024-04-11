# Images

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



# ImmersiveSpace

Initializer

# init(for:content:)

Creates the immersive space for a specified type of presented data.

visionOS 1.0+

    
    
    init(
        for type: Data.Type,
        @ImmersiveSpaceContentBuilder content: @escaping (Binding<Data?>) -> Content
    )

##  Parameters

`type`

    

The type of presented data this immersive space accepts.

`content`

    

An immersive space content builder that defines the content for each instance
of the immersive space. The closure receives a binding to the value that you
pass to the `openImmersiveSpace` action when you call that action to open an
immersive space. The system automatically persists and restores the value of
this binding during state restoration.

## Discussion

The space uses the specified content builder to form the content. Your app
invokes this initializer when it presents a value of the specified `type`
using the `openImmersiveSpace` action.

## See Also

### Creating a data-driven immersive space

`init<V>(for: Data.Type, content: (Binding<Data?>) -> V)`

Creates the immersive space for a specified type of presented data using view-
based content.

Available when `Content` conforms to `ImmersiveSpaceContent`, `Data` conforms
to `Decodable`, `Data` conforms to `Encodable`, and `Data` conforms to
`Hashable`.

`init(id: String, for: Data.Type, content: (Binding<Data?>) -> Content)`

Creates the immersive space associated with an identifier for a specified type
of presented data.

`init<V>(id: String, for: Data.Type, content: (Binding<Data?>) -> V)`

Creates the immersive space associated with an identifier for a specified type
of presented data using view-based content.

Available when `Content` conforms to `ImmersiveSpaceContent`, `Data` conforms
to `Decodable`, `Data` conforms to `Encodable`, and `Data` conforms to
`Hashable`.

Initializer

# init(for:content:)

Creates the immersive space for a specified type of presented data using view-
based content.

visionOS 1.0+

    
    
    init<V>(
        for type: Data.Type,
        @ViewBuilder content: @escaping (Binding<Data?>) -> V
    ) where Content == ImmersiveSpaceViewContent<V>, V : View

Available when `Content` conforms to `ImmersiveSpaceContent`, `Data` conforms
to `Decodable`, `Data` conforms to `Encodable`, and `Data` conforms to
`Hashable`.

##  Parameters

`type`

    

The type of presented data this immersive space accepts.

`content`

    

A view builder that defines the content for each instance of the immersive
space. The closure receives a binding to the value that you pass to the
`openImmersiveSpace` action when you use it to open an immersive space. The
system automatically persists and restores the value of this binding during
state restoration.

## Discussion

The immersive space uses the specified view as a template to form the content
of the space. Your app invokes this initializer when it presents a value of
the specified `type` using the `openImmersiveSpace` action.

## See Also

### Creating a data-driven immersive space

`init(for: Data.Type, content: (Binding<Data?>) -> Content)`

Creates the immersive space for a specified type of presented data.

`init(id: String, for: Data.Type, content: (Binding<Data?>) -> Content)`

Creates the immersive space associated with an identifier for a specified type
of presented data.

`init<V>(id: String, for: Data.Type, content: (Binding<Data?>) -> V)`

Creates the immersive space associated with an identifier for a specified type
of presented data using view-based content.

Available when `Content` conforms to `ImmersiveSpaceContent`, `Data` conforms
to `Decodable`, `Data` conforms to `Encodable`, and `Data` conforms to
`Hashable`.

Initializer

# init(id:for:content:)

Creates the immersive space associated with an identifier for a specified type
of presented data.

visionOS 1.0+

    
    
    init(
        id: String,
        for type: Data.Type,
        @ImmersiveSpaceContentBuilder content: @escaping (Binding<Data?>) -> Content
    )

##  Parameters

`id`

    

A string that uniquely identifies the immersive space. Ensure that identifiers
are unique among the immersive spaces in your app.

`type`

    

The type of presented data this immersive space accepts.

`content`

    

An immersive space content builder that defines the content for each instance
of the immersive space. The closure receives a binding to the value that you
pass to the `openImmersiveSpace` action when you call that action to open an
immersive space. The system automatically persists and restores the value of
this binding during state restoration.

## Discussion

The space uses the specified content builder to form the content. Your app
invokes this initializer when it presents a value of the specified `type`
using the `openImmersiveSpace` action.

## See Also

### Creating a data-driven immersive space

`init(for: Data.Type, content: (Binding<Data?>) -> Content)`

Creates the immersive space for a specified type of presented data.

`init<V>(for: Data.Type, content: (Binding<Data?>) -> V)`

Creates the immersive space for a specified type of presented data using view-
based content.

Available when `Content` conforms to `ImmersiveSpaceContent`, `Data` conforms
to `Decodable`, `Data` conforms to `Encodable`, and `Data` conforms to
`Hashable`.

`init<V>(id: String, for: Data.Type, content: (Binding<Data?>) -> V)`

Creates the immersive space associated with an identifier for a specified type
of presented data using view-based content.

Available when `Content` conforms to `ImmersiveSpaceContent`, `Data` conforms
to `Decodable`, `Data` conforms to `Encodable`, and `Data` conforms to
`Hashable`.

Initializer

# init(id:for:content:)

Creates the immersive space associated with an identifier for a specified type
of presented data using view-based content.

visionOS 1.0+

    
    
    init<V>(
        id: String,
        for type: Data.Type,
        @ViewBuilder content: @escaping (Binding<Data?>) -> V
    ) where Content == ImmersiveSpaceViewContent<V>, V : View

Available when `Content` conforms to `ImmersiveSpaceContent`, `Data` conforms
to `Decodable`, `Data` conforms to `Encodable`, and `Data` conforms to
`Hashable`.

##  Parameters

`id`

    

A string that uniquely identifies the immersive space. Ensure that identifiers
are unique among the immersive spaces in your app.

`type`

    

The type of presented data this immersive space accepts.

`content`

    

A view builder that defines the content for each instance of the immersive
space. The closure receives a binding to the value that you pass to the
`openImmersiveSpace` action when you use it to open an immersive space. The
system automatically persists and restores the value of this binding during
state restoration.

## Discussion

The immersive space uses the specified view as a template to form the content
of the space. Your app invokes this initializer when it presents a value of
the specified `type` using the `openImmersiveSpace` action.

## See Also

### Creating a data-driven immersive space

`init(for: Data.Type, content: (Binding<Data?>) -> Content)`

Creates the immersive space for a specified type of presented data.

`init<V>(for: Data.Type, content: (Binding<Data?>) -> V)`

Creates the immersive space for a specified type of presented data using view-
based content.

Available when `Content` conforms to `ImmersiveSpaceContent`, `Data` conforms
to `Decodable`, `Data` conforms to `Encodable`, and `Data` conforms to
`Hashable`.

`init(id: String, for: Data.Type, content: (Binding<Data?>) -> Content)`

Creates the immersive space associated with an identifier for a specified type
of presented data.

Initializer

# init(for:content:defaultValue:)

Creates an immersive space.

visionOS 1.0+

    
    
    init(
        for type: Data.Type = Data.self,
        @ImmersiveSpaceContentBuilder content: @escaping (Binding<Data>) -> Content,
        defaultValue: @escaping () -> Data
    )

##  Parameters

`type`

    

The type of presented data this immersive space accepts.

`content`

    

An immersive space content builder that defines the content for each instance
of the immersive space. The closure receives a binding to the value that you
pass to the `openImmersiveSpace` action when you call that action to open an
immersive space. The system automatically persists and restores the value of
this binding during state restoration.

`defaultValue`

    

A closure that returns a value that SwiftUI presents when it doesn’t receive
one from you, like when you call the `openImmersiveSpace` action without
providing a value.

## Discussion

The immersive space uses the specified content builder as a template to form
the content of the space. Your app invokes this initializer when it presents a
value of the specified `type` using the `openImmersiveSpace` action.

## See Also

### Providing default data to an immersive space

`init<V>(for: Data.Type, content: (Binding<Data>) -> V, defaultValue: () ->
Data)`

Creates an immersive space for a specified type of presented data and a
default value if the data is not set.

Available when `Content` conforms to `ImmersiveSpaceContent`, `Data` conforms
to `Decodable`, `Data` conforms to `Encodable`, and `Data` conforms to
`Hashable`.

`init<V>(id: String, for: Data.Type, content: (Binding<Data>) -> V,
defaultValue: () -> Data)`

Creates the immersive space associated with an identifier for a specified type
of presented data and a default value if the data is not set.

Available when `Content` conforms to `ImmersiveSpaceContent`, `Data` conforms
to `Decodable`, `Data` conforms to `Encodable`, and `Data` conforms to
`Hashable`.

`init(id: String, for: Data.Type, content: (Binding<Data>) -> Content,
defaultValue: () -> Data)`

Creates the immersive space associated with an identifier for a specified type
of presented data, and a default value, if the data is not set.

Initializer

# init(for:content:defaultValue:)

Creates an immersive space for a specified type of presented data and a
default value if the data is not set.

visionOS 1.0+

    
    
    init<V>(
        for type: Data.Type = Data.self,
        @ViewBuilder content: @escaping (Binding<Data>) -> V,
        defaultValue: @escaping () -> Data
    ) where Content == ImmersiveSpaceViewContent<V>, V : View

Available when `Content` conforms to `ImmersiveSpaceContent`, `Data` conforms
to `Decodable`, `Data` conforms to `Encodable`, and `Data` conforms to
`Hashable`.

##  Parameters

`type`

    

The type of presented data this immersive space accepts.

`content`

    

A view builder that defines the content for each instance of the immersive
space. The closure receives a binding to the value that you pass to the
`openImmersiveSpace` action when you use it to open an immersive space. The
system automatically persists and restores the value of this binding during
state restoration.

`defaultValue`

    

A closure that returns a value that SwiftUI presents when it doesn’t receive
one from you, like when you call the `openImmersiveSpace` action without
providing a value.

## Discussion

The immersive space uses the specified view as a template to form the content
of the space. Your app invokes this initializer when it presents a value of
the specified `type` using the `openImmersiveSpace` action.

## See Also

### Providing default data to an immersive space

`init(for: Data.Type, content: (Binding<Data>) -> Content, defaultValue: () ->
Data)`

Creates an immersive space.

`init<V>(id: String, for: Data.Type, content: (Binding<Data>) -> V,
defaultValue: () -> Data)`

Creates the immersive space associated with an identifier for a specified type
of presented data and a default value if the data is not set.

Available when `Content` conforms to `ImmersiveSpaceContent`, `Data` conforms
to `Decodable`, `Data` conforms to `Encodable`, and `Data` conforms to
`Hashable`.

`init(id: String, for: Data.Type, content: (Binding<Data>) -> Content,
defaultValue: () -> Data)`

Creates the immersive space associated with an identifier for a specified type
of presented data, and a default value, if the data is not set.

Initializer

# init(id:for:content:defaultValue:)

Creates the immersive space associated with an identifier for a specified type
of presented data and a default value if the data is not set.

visionOS 1.0+

    
    
    init<V>(
        id: String,
        for type: Data.Type = Data.self,
        @ViewBuilder content: @escaping (Binding<Data>) -> V,
        defaultValue: @escaping () -> Data
    ) where Content == ImmersiveSpaceViewContent<V>, V : View

Available when `Content` conforms to `ImmersiveSpaceContent`, `Data` conforms
to `Decodable`, `Data` conforms to `Encodable`, and `Data` conforms to
`Hashable`.

##  Parameters

`id`

    

A string that uniquely identifies the immersive space. Ensure that identifiers
are unique among the immersive spaces in your app.

`type`

    

The type of presented data this immersive space accepts.

`content`

    

A view builder that defines the content for each instance of the immersive
space. The closure receives a binding to the value that you pass to the
`openImmersiveSpace` action when you use it to open an immersive space. The
system automatically persists and restores the value of this binding during
state restoration.

`defaultValue`

    

A closure that returns a value that SwiftUI presents when it doesn’t receive
one from you, like when you call the `openImmersiveSpace` action without
providing a value.

## Discussion

The immersive space uses the specified view as a template to form the content
of the space. Your app invokes this initializer when it presents a value of
the specified `type` using the `openImmersiveSpace` action.

## See Also

### Providing default data to an immersive space

`init(for: Data.Type, content: (Binding<Data>) -> Content, defaultValue: () ->
Data)`

Creates an immersive space.

`init<V>(for: Data.Type, content: (Binding<Data>) -> V, defaultValue: () ->
Data)`

Creates an immersive space for a specified type of presented data and a
default value if the data is not set.

Available when `Content` conforms to `ImmersiveSpaceContent`, `Data` conforms
to `Decodable`, `Data` conforms to `Encodable`, and `Data` conforms to
`Hashable`.

`init(id: String, for: Data.Type, content: (Binding<Data>) -> Content,
defaultValue: () -> Data)`

Creates the immersive space associated with an identifier for a specified type
of presented data, and a default value, if the data is not set.

Initializer

# init(id:for:content:defaultValue:)

Creates the immersive space associated with an identifier for a specified type
of presented data, and a default value, if the data is not set.

visionOS 1.0+

    
    
    init(
        id: String,
        for type: Data.Type = Data.self,
        @ImmersiveSpaceContentBuilder content: @escaping (Binding<Data>) -> Content,
        defaultValue: @escaping () -> Data
    )

##  Parameters

`id`

    

A string that uniquely identifies the immersive space. Ensure that identifiers
are unique among the immersive spaces in your app.

`type`

    

The type of presented data this immersive space accepts.

`content`

    

An immersive space content builder that defines the content for each instance
of the immersive space. The closure receives a binding to the value that you
pass to the `openImmersiveSpace` action when you call that action to open an
immersive space. The system automatically persists and restores the value of
this binding during state restoration.

`defaultValue`

    

A closure that returns a value that SwiftUI presents when it doesn’t receive
one from you, like when you call the `openImmersiveSpace` action without
providing a value.

## Discussion

The space uses the specified content builder to form the content. Your app
invokes this initializer when it presents a value of the specified `type`
using the `openImmersiveSpace` action.

## See Also

### Providing default data to an immersive space

`init(for: Data.Type, content: (Binding<Data>) -> Content, defaultValue: () ->
Data)`

Creates an immersive space.

`init<V>(for: Data.Type, content: (Binding<Data>) -> V, defaultValue: () ->
Data)`

Creates an immersive space for a specified type of presented data and a
default value if the data is not set.

Available when `Content` conforms to `ImmersiveSpaceContent`, `Data` conforms
to `Decodable`, `Data` conforms to `Encodable`, and `Data` conforms to
`Hashable`.

`init<V>(id: String, for: Data.Type, content: (Binding<Data>) -> V,
defaultValue: () -> Data)`

Creates the immersive space associated with an identifier for a specified type
of presented data and a default value if the data is not set.

Available when `Content` conforms to `ImmersiveSpaceContent`, `Data` conforms
to `Decodable`, `Data` conforms to `Encodable`, and `Data` conforms to
`Hashable`.

Structure

# ImmersiveSpaceViewContent

Immersive space content that uses a SwiftUI view hierarchy as the content.

visionOS 1.0+

    
    
    struct ImmersiveSpaceViewContent<Content> where Content : View

## Overview

You don’t create this type directly. SwiftUI creates it when you construct an
`ImmersiveSpace` with view-based content.

## Relationships

### Conforms To

  * `ImmersiveSpaceContent`

## See Also

### Supporting types

`protocol ImmersiveSpaceContent`

A type that you can use as the content of an immersive space.

Protocol

# ImmersiveSpaceContent

A type that you can use as the content of an immersive space.

visionOS 1.0+

    
    
    protocol ImmersiveSpaceContent

## Topics

### Creating immersive space content

`var body: Self.Body`

**Required**

` associatedtype Body : ImmersiveSpaceContent`

**Required**

## Relationships

### Conforming Types

  * `ImmersiveSpaceViewContent`

## See Also

### Supporting types

`struct ImmersiveSpaceViewContent`

Immersive space content that uses a SwiftUI view hierarchy as the content.

Initializer

# init(content:)

Creates an immersive space.

visionOS 1.0+

    
    
    init(@ImmersiveSpaceContentBuilder content: @escaping () -> Content) where Data == Never

##  Parameters

`content`

    

An immersive space content builder that defines the content of the space.

## Discussion

The space uses the specified content builder to form the content.

Initializer

# init(content:)

Creates an immersive space using view-based content.

visionOS 1.0+

    
    
    init<V>(@ViewBuilder content: @escaping () -> V) where Content == ImmersiveSpaceViewContent<V>, Data == Never, V : View

Available when `Content` conforms to `ImmersiveSpaceContent`, `Data` conforms
to `Decodable`, `Data` conforms to `Encodable`, and `Data` conforms to
`Hashable`.

##  Parameters

`content`

    

A view builder that defines the content for each instance of the immersive
space.

## Discussion

The immersive space uses the specified view as a template to form the content
of the space.

Initializer

# init(id:content:)

Creates the immersive space associated with the specified identifier using
view-based content.

visionOS 1.0+

    
    
    init<V>(
        id: String,
        @ViewBuilder content: () -> V
    ) where Content == ImmersiveSpaceViewContent<V>, Data == Never, V : View

Available when `Content` conforms to `ImmersiveSpaceContent`, `Data` conforms
to `Decodable`, `Data` conforms to `Encodable`, and `Data` conforms to
`Hashable`.

##  Parameters

`id`

    

A string that uniquely identifies the immersive space. Ensure that identifiers
are unique among the immersive spaces in your app.

`content`

    

A view builder that defines the content for each instance of the immersive
space.

## Discussion

The immersive space uses the specified view as a template to form the content
of the space.

Initializer

# init(id:content:)

Creates the immersive space associated with the specified identifier.

visionOS 1.0+

    
    
    init(
        id: String,
        @ImmersiveSpaceContentBuilder content: () -> Content
    ) where Data == Never

##  Parameters

`id`

    

A string that uniquely identifies the immersive space. Ensure that identifiers
are unique among the immersive spaces in your app.

`content`

    

An immersive space content builder that defines the content of the space.

## Discussion

The space uses the specified content builder to form the content.



# Image.Scale

Case

# Image.Scale.small

A scale that produces small images.

iOS 13.0+  iPadOS 13.0+  macOS 11.0+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case small

## See Also

### Getting image scales

`case medium`

A scale that produces medium-sized images.

`case large`

A scale that produces large images.

Case

# Image.Scale.medium

A scale that produces medium-sized images.

iOS 13.0+  iPadOS 13.0+  macOS 11.0+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case medium

## See Also

### Getting image scales

`case small`

A scale that produces small images.

`case large`

A scale that produces large images.

Case

# Image.Scale.large

A scale that produces large images.

iOS 13.0+  iPadOS 13.0+  macOS 11.0+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case large

## See Also

### Getting image scales

`case small`

A scale that produces small images.

`case medium`

A scale that produces medium-sized images.



# InsetTableStyle

Initializer

# init()

Creates a default inset table style, with alternating row backgrounds.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init()

## See Also

### Creating the table style

`init(alternatesRowBackgrounds: Bool)`

Creates an inset table style with optional alternating row backgrounds.

Deprecated

Initializer

# init(alternatesRowBackgrounds:)

Creates an inset table style with optional alternating row backgrounds.

macOS 12.0–14.4  Deprecated

    
    
    init(alternatesRowBackgrounds: Bool)

Deprecated

Use the `inset` style and add the `alternatingRowBackgrounds(_:)` view
modifier instead.

## See Also

### Creating the table style

`init()`

Creates a default inset table style, with alternating row backgrounds.



# Image.TemplateRenderingMode

Case

# Image.TemplateRenderingMode.original

A mode that renders pixels of bitmap images as-is.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case original

## Discussion

For system images created from the SF Symbol set, multicolor symbols respect
the current foreground and accent colors.

## See Also

### Getting rendering modes

`case template`

A mode that renders all non-transparent pixels as the foreground color.

Case

# Image.TemplateRenderingMode.template

A mode that renders all non-transparent pixels as the foreground color.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case template

## See Also

### Getting rendering modes

`case original`

A mode that renders pixels of bitmap images as-is.



# ImageRenderer

Initializer

# init(content:)

Creates a renderer object with a source content view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    @MainActor
    init(content view: Content)

##  Parameters

`view`

    

A `View` to render.

Instance Property

# content

The root view rendered by this image renderer.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    @MainActor
    final var content: Content { get set }

Instance Property

# proposedSize

The size proposed to the root view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    @MainActor
    final var proposedSize: ProposedViewSize { get set }

## Discussion

The default value of this property, `unspecified`, produces an image that
matches the original view size. You can provide a custom `ProposedViewSize` to
override the view’s size in one or both dimensions.

## See Also

### Accessing renderer properties

`var scale: CGFloat`

The scale at which to render the image.

`var isOpaque: Bool`

A Boolean value that indicates whether the alpha channel of the image is fully
opaque.

`var colorMode: ColorRenderingMode`

The working color space and storage format of the image.

Instance Property

# scale

The scale at which to render the image.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    @MainActor
    final var scale: CGFloat { get set }

## Discussion

This value is a ratio of view points to image pixels. This relationship means
that values greater than `1.0` create an image larger than the original
content view, and less than `1.0` creates a smaller image. The following
example shows a 100 x 50 rectangle view and an image rendered from it with a
`scale` of `2.0`, resulting in an image size of 200 x 100.

The default value of this property is `1.0`.

## See Also

### Accessing renderer properties

`var proposedSize: ProposedViewSize`

The size proposed to the root view.

`var isOpaque: Bool`

A Boolean value that indicates whether the alpha channel of the image is fully
opaque.

`var colorMode: ColorRenderingMode`

The working color space and storage format of the image.

Instance Property

# isOpaque

A Boolean value that indicates whether the alpha channel of the image is fully
opaque.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    @MainActor
    final var isOpaque: Bool { get set }

## Discussion

Setting this value to `true`, meaning the alpha channel is opaque, may improve
performance. Don’t render non-opaque pixels to a renderer declared as opaque.
This property defaults to `false`.

## See Also

### Accessing renderer properties

`var proposedSize: ProposedViewSize`

The size proposed to the root view.

`var scale: CGFloat`

The scale at which to render the image.

`var colorMode: ColorRenderingMode`

The working color space and storage format of the image.

Instance Property

# colorMode

The working color space and storage format of the image.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    @MainActor
    final var colorMode: ColorRenderingMode { get set }

## See Also

### Accessing renderer properties

`var proposedSize: ProposedViewSize`

The size proposed to the root view.

`var scale: CGFloat`

The scale at which to render the image.

`var isOpaque: Bool`

A Boolean value that indicates whether the alpha channel of the image is fully
opaque.

Instance Method

# render(rasterizationScale:renderer:)

Draws the renderer’s current contents to an arbitrary Core Graphics context.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    @MainActor
    final func render(
        rasterizationScale: CGFloat = 1,
        renderer: (CGSize, (CGContext) -> Void) -> Void
    )

##  Parameters

`rasterizationScale`

    

The scale factor for converting user interface points to pixels when
rasterizing parts of the view that can’t be represented as native Core
Graphics drawing commands.

`renderer`

    

The closure that sets up the Core Graphics context and renders the view. This
closure receives two parameters: the size of the view and a function that you
invoke in the closure to render the view at the reported size. This function
takes a `CGContext` parameter, and assumes a bottom-left coordinate space
origin.

## Discussion

Use this method to rasterize the renderer’s content to a `CGContext` you
provide. The `renderer` closure receives two parameters: the current size of
the view, and a function that renders the view to your `CGContext`. Implement
the closure to provide a suitable `CGContext`, then invoke the function to
render the content to that context.

## See Also

### Rendering images

`var cgImage: CGImage?`

The current contents of the view, rasterized as a Core Graphics image.

`var nsImage: NSImage?`

The current contents of the view, rasterized as an AppKit image.

`var uiImage: UIImage?`

The current contents of the view, rasterized as a UIKit image.

Instance Property

# cgImage

The current contents of the view, rasterized as a Core Graphics image.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    @MainActor
    final var cgImage: CGImage? { get }

## Discussion

The renderer notifies its `objectWillChange` publisher when the contents of
the image may have changed.

## See Also

### Rendering images

`func render(rasterizationScale: CGFloat, renderer: (CGSize, (CGContext) ->
Void) -> Void)`

Draws the renderer’s current contents to an arbitrary Core Graphics context.

`var nsImage: NSImage?`

The current contents of the view, rasterized as an AppKit image.

`var uiImage: UIImage?`

The current contents of the view, rasterized as a UIKit image.

Instance Property

# nsImage

The current contents of the view, rasterized as an AppKit image.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    @MainActor
    final var nsImage: NSImage? { get }

## Discussion

The renderer notifies its `objectWillChange` publisher when the contents of
the image may have changed.

## See Also

### Rendering images

`func render(rasterizationScale: CGFloat, renderer: (CGSize, (CGContext) ->
Void) -> Void)`

Draws the renderer’s current contents to an arbitrary Core Graphics context.

`var cgImage: CGImage?`

The current contents of the view, rasterized as a Core Graphics image.

`var uiImage: UIImage?`

The current contents of the view, rasterized as a UIKit image.

Instance Property

# uiImage

The current contents of the view, rasterized as a UIKit image.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    @MainActor
    final var uiImage: UIImage? { get }

## Discussion

The renderer notifies its `objectWillChange` publisher when the contents of
the image may have changed.

## See Also

### Rendering images

`func render(rasterizationScale: CGFloat, renderer: (CGSize, (CGContext) ->
Void) -> Void)`

Draws the renderer’s current contents to an arbitrary Core Graphics context.

`var cgImage: CGImage?`

The current contents of the view, rasterized as a Core Graphics image.

`var nsImage: NSImage?`

The current contents of the view, rasterized as an AppKit image.

Instance Property

# objectWillChange

A publisher that informs subscribers of changes to the image.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    final let objectWillChange: PassthroughSubject<Void, Never>

## Discussion

The renderer’s `ObjectWillChangePublisher` publishes `Void` elements.
Subscribers should interpret any event as indicating that the contents of the
image may have changed.



# Image

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



# ImportFromDevicesCommands

Initializer

# init()

Creates a new set of device import commands.

macOS 12.0+

    
    
    init()



# InspectorCommands

Initializer

# init()

A new value describing the built-in inspector-related commands.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    init()



# Input and event modifiers

Instance Method

# disabled(_:)

Adds a condition that controls whether users can interact with this view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func disabled(_ disabled: Bool) -> some View
    

##  Parameters

`disabled`

    

A Boolean value that determines whether users can interact with this view.

## Return Value

A view that controls whether users can interact with this view.

## Discussion

The higher views in a view hierarchy can override the value you set on this
view. In the following example, the button isn’t interactive because the outer
`disabled(_:)` modifier overrides the inner one:

## See Also

### Managing view interaction

`var isEnabled: Bool`

A Boolean value that indicates whether the view associated with this
environment allows user interaction.

`func interactionActivityTrackingTag(String) -> some View`

Sets a tag that you use for tracking interactivity.

`func invalidatableContent(Bool) -> some View`

Mark the receiver as their content might be invalidated.

Instance Method

# interactionActivityTrackingTag(_:)

Sets a tag that you use for tracking interactivity.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func interactionActivityTrackingTag(_ tag: String) -> some View
    

##  Parameters

`tag`

    

The tag used to track user interactions hosted by this view as activities.

## Return Value

A view that uses a tracking tag.

## Discussion

The following example tracks the scrolling activity of a `List`:

The resolved activity tracking tag is additive, so using the modifier across
the view hierarchy builds the tag from top to bottom. The example below shows
a hierarchical usage of this modifier with the resulting tag `Home-Feed`:

## See Also

### Managing view interaction

`func disabled(Bool) -> some View`

Adds a condition that controls whether users can interact with this view.

`var isEnabled: Bool`

A Boolean value that indicates whether the view associated with this
environment allows user interaction.

`func invalidatableContent(Bool) -> some View`

Mark the receiver as their content might be invalidated.

Instance Method

# swipeActions(edge:allowsFullSwipe:content:)

Adds custom swipe actions to a row in a list.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  watchOS 8.0+
visionOS 1.0+

    
    
    func swipeActions<T>(
        edge: HorizontalEdge = .trailing,
        allowsFullSwipe: Bool = true,
        @ViewBuilder content: () -> T
    ) -> some View where T : View
    

##  Parameters

`edge`

    

The edge of the view to associate the swipe actions with. The default is
`HorizontalEdge.trailing`.

`allowsFullSwipe`

    

A Boolean value that indicates whether a full swipe automatically performs the
first action. The default is `true`.

`content`

    

The content of the swipe actions.

## Discussion

Use this method to add swipe actions to a view that acts as a row in a list.
Indicate the `HorizontalEdge` where the swipe action originates, and define
individual actions with `Button` instances. For example, if you have a list of
messages, you can add an action to toggle a message as unread on a swipe from
the leading edge, and actions to delete or flag messages on a trailing edge
swipe:

Actions appear in the order you list them, starting from the swipe’s
originating edge. In the example above, the Delete action appears closest to
the screen’s trailing edge:

For labels or images that appear in swipe actions, SwiftUI automatically
applies the `fill` symbol variant, as shown above.

By default, the user can perform the first action for a given swipe direction
with a full swipe. For the example above, the user can perform both the toggle
unread and delete actions with full swipes. You can opt out of this behavior
for an edge by setting the `allowsFullSwipe` parameter to `false`. For
example, you can disable the full swipe on the leading edge:

When you set a role for a button using one of the values from the `ButtonRole`
enumeration, SwiftUI styles the button according to its role. In the example
above, the delete action appears in `red` because it has the `destructive`
role. If you want to set a different color — for example, to match the overall
theme of your app’s UI — add the `View/tint(_:)` modifier to the button:

The modifications in the code above make the toggle unread action `blue` and
the flag action `orange`:

When you add swipe actions, SwiftUI no longer synthesizes the Delete actions
that otherwise appear when using the `ForEach/onDelete(perform:)` method on a
`ForEach` instance. You become responsible for creating a Delete action, if
appropriate, among your swipe actions.

Actions accumulate for a given edge if you call the modifier multiple times on
the same list row view.

## See Also

### Configuring interaction

`func selectionDisabled(Bool) -> some View`

Adds a condition that controls whether users can select this view.

Instance Method

# refreshable(action:)

Marks this view as refreshable.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func refreshable(action: @escaping () async -> Void) -> some View
    

##  Parameters

`action`

    

An asynchronous handler that SwiftUI executes when the user requests a
refresh. Use this handler to initiate an update of model data displayed in the
modified view. Use `await` in front of any asynchronous calls inside the
handler.

## Return Value

A view with a new refresh action in its environment.

## Discussion

Apply this modifier to a view to set the `refresh` value in the view’s
environment to a `RefreshAction` instance that uses the specified `action` as
its handler. Views that detect the presence of the instance can change their
appearance to provide a way for the user to execute the handler.

For example, when you apply this modifier on iOS and iPadOS to a `List`, the
list enables a standard pull-to-refresh gesture that refreshes the list
contents. When the user drags the top of the scrollable area downward, the
view reveals a progress indicator and executes the specified handler. The
indicator remains visible for the duration of the refresh, which runs
asynchronously:

You can add refresh capability to your own views as well. For information on
how to do that, see `RefreshAction`.

## See Also

### Refreshing a list’s content

`var refresh: RefreshAction?`

A refresh action stored in a view’s environment.

`struct RefreshAction`

An action that initiates a refresh operation.

Instance Method

# selectionDisabled(_:)

Adds a condition that controls whether users can select this view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func selectionDisabled(_ isDisabled: Bool = true) -> some View
    

##  Parameters

`isDisabled`

    

A Boolean value that determines whether users can select this view.

## Discussion

Use this modifier to control the selectability of views in selectable
containers like `List` or `Table`. In the example, below, the user can’t
select the first item in the list.

You can also use this modifier to specify the selectability of views within a
`Picker`. The following example represents a flavor picker that disables
selection on flavors that are unavailable.

## See Also

### Configuring interaction

`func swipeActions<T>(edge: HorizontalEdge, allowsFullSwipe: Bool, content: ()
-> T) -> some View`

Adds custom swipe actions to a row in a list.

Instance Method

# scrollPosition(id:anchor:)

Associates a binding to be updated when a scroll view within this view
scrolls.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func scrollPosition(
        id: Binding<(some Hashable)?>,
        anchor: UnitPoint? = nil
    ) -> some View
    

## Discussion

Use this modifier along with the `View/scrollTargetLayout()` modifier to know
the identity of the view that is actively scrolled. As the scroll view
scrolls, the binding will be updated with the identity of the leading-most /
top-most view.

Use the `View/scrollTargetLayout()` modifier to configure which the layout
that contains your scroll targets. In the following example, the top-most
ItemView will update with the scrolledID binding as the scroll view scrolls.

You can write to the binding to scroll to the view with the provided identity.

SwiftUI will attempt to keep the view with the identity specified in the
provided binding when events occur that might cause it to be scrolled out of
view by the system. Some examples of these include:

  * The data backing the content of a scroll view is re-ordered.

  * The size of the scroll view changes, like when a window is resized on macOS or during a rotation on iOS.

  * The scroll view initially lays out it content defaulting to the top most view, but the binding has a different view’s identity.

You can provide an anchor to this modifier to both:

  * Influence which view the system chooses as the view whose identity value will update the providing binding as the scroll view scrolls.

  * Control the alignment of the view when scrolling to a view when writing a new binding value.

For example, providing a value of `bottom` will prefer to have the bottom-most
view chosen and prefer to scroll to views aligned to the bottom.

## See Also

### Managing scroll position

`func defaultScrollAnchor(UnitPoint?) -> some View`

Associates an anchor to control which part of the scroll view’s content should
be rendered by default.

Instance Method

# defaultScrollAnchor(_:)

Associates an anchor to control which part of the scroll view’s content should
be rendered by default.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func defaultScrollAnchor(_ anchor: UnitPoint?) -> some View
    

## Discussion

Use this modifier to specify an anchor to control both which part of the
scroll view’s content should be visible initially and how the scroll view
handles content size changes.

Provide a value of `UnitPoint/center`` to have the scroll view start in the
center of its content when a scroll view is scrollable in both axes.

    
    
    ScrollView([.horizontal, .vertical]) {
        // initially centered content
    }
    .defaultScrollAnchor(.center)
    

Provide a value of `UnitPoint/bottom` to have the scroll view start at the
bottom of its content when scrollable in the vertical axis.

    
    
    @Binding var items: [Item]
    @Binding var scrolledID: Item.ID?
    
    
    ScrollView {
        LazyVStack {
            ForEach(items) { item in
                ItemView(item)
            }
        }
    }
    .defaultScrollAnchor(.bottom)
    

The user may scroll away from the initial defined scroll position. When the
content size of the scroll view changes, it may consult the anchor to know how
to reposition the content.

## See Also

### Managing scroll position

`func scrollPosition(id: Binding<(some Hashable)?>, anchor: UnitPoint?) ->
some View`

Associates a binding to be updated when a scroll view within this view
scrolls.

Instance Method

# scrollTargetBehavior(_:)

Sets the scroll behavior of views scrollable in the provided axes.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func scrollTargetBehavior(_ behavior: some ScrollTargetBehavior) -> some View
    

## Discussion

A scrollable view calculates where scroll gestures should end using its
deceleration rate and the state of its scroll gesture by default. A scroll
behavior allows for customizing this logic. You can provide your own
`ScrollTargetBehavior` or use one of the built in behaviors provided by
SwiftUI.

### Paging Behavior

SwiftUI offers a `PagingScrollTargetBehavior` behavior which uses the geometry
of the scroll view to decide where to allow scrolls to end.

In the following example, every view in the lazy stack is flexible in both
directions and the scroll view will settle to container aligned boundaries.

    
    
    ScrollView {
        LazyVStack(spacing: 0.0) {
            ForEach(items) { item in
                FullScreenItem(item)
            }
        }
    }
    .scrollTargetBehavior(.paging)
    

### View Aligned Behavior

SwiftUI offers a `ViewAlignedScrollTargetBehavior` scroll behavior that will
always settle on the geometry of individual views.

    
    
    ScrollView(.horizontal) {
        LazyHStack(spacing: 10.0) {
            ForEach(items) { item in
                ItemView(item)
            }
        }
        .scrollTargetLayout()
    }
    .scrollTargetBehavior(.viewAligned)
    .safeAreaPadding(.horizontal, 20.0)
    

You configure which views should be used for settling using the
`scrollTargetLayout(isEnabled:)` modifier. Apply this modifier to a layout
container like `LazyVStack` or `HStack` and each individual view in that
layout will be considered for alignment.

## See Also

### Defining scroll targets

`func scrollTargetLayout(isEnabled: Bool) -> some View`

Configures the outermost layout as a scroll target layout.

`struct ScrollTarget`

A type defining the target in which a scroll view should try and scroll to.

`protocol ScrollTargetBehavior`

A type that defines the scroll behavior of a scrollable view.

`struct ScrollTargetBehaviorContext`

The context in which a scroll target behavior updates its scroll target.

`struct PagingScrollTargetBehavior`

The scroll behavior that aligns scroll targets to container-based geometry.

`struct ViewAlignedScrollTargetBehavior`

The scroll behavior that aligns scroll targets to view-based geometry.

Instance Method

# scrollTargetLayout(isEnabled:)

Configures the outermost layout as a scroll target layout.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func scrollTargetLayout(isEnabled: Bool = true) -> some View
    

## Discussion

This modifier works together with the `ViewAlignedScrollTargetBehavior` to
ensure that scroll views align to view based content.

Apply this modifier to layout containers like `LazyHStack` or `VStack` within
a `ScrollView` that contain the main repeating content of your `ScrollView`.

Scroll target layouts act as a convenience for applying a
`View/scrollTarget(isEnabled:)` modifier to each views in the layout.

A scroll target layout will ensure that any target layout nested within the
primary one will not also become a scroll target layout.

## See Also

### Defining scroll targets

`func scrollTargetBehavior(some ScrollTargetBehavior) -> some View`

Sets the scroll behavior of views scrollable in the provided axes.

`struct ScrollTarget`

A type defining the target in which a scroll view should try and scroll to.

`protocol ScrollTargetBehavior`

A type that defines the scroll behavior of a scrollable view.

`struct ScrollTargetBehaviorContext`

The context in which a scroll target behavior updates its scroll target.

`struct PagingScrollTargetBehavior`

The scroll behavior that aligns scroll targets to container-based geometry.

`struct ViewAlignedScrollTargetBehavior`

The scroll behavior that aligns scroll targets to view-based geometry.

Instance Method

# scrollTransition(_:axis:transition:)

Applies the given transition, animating between the phases of the transition
as this view appears and disappears within the visible region of the
containing scroll view, or other container specified using the
`coordinateSpace` parameter.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func scrollTransition(
        _ configuration: ScrollTransitionConfiguration = .interactive,
        axis: Axis? = nil,
        transition: @escaping (EmptyVisualEffect, ScrollTransitionPhase) -> some VisualEffect
    ) -> some View
    

##  Parameters

`configuration`

    

The configuration controlling how the transition will be applied. The
configuration will be applied both while the view is coming into view and
while it is disappearing (the transition is symmetrical).

`axis`

    

The axis of the containing scroll view over which the transition will be
applied. The default value of `nil` uses the axis of the innermost containing
scroll view, or `.vertical` if the innermost scroll view is scrollable along
both axes.

`coordinateSpace`

    

The coordinate space of the container that visibility is evaluated within.
Defaults to `.scrollView`.

`transition`

    

A closure that applies visual effects as a function of the provided phase.

## See Also

### Animating scroll transitions

`func scrollTransition(topLeading: ScrollTransitionConfiguration,
bottomTrailing: ScrollTransitionConfiguration, axis: Axis?, transition:
(EmptyVisualEffect, ScrollTransitionPhase) -> some VisualEffect) -> some View`

Applies the given transition, animating between the phases of the transition
as this view appears and disappears within the visible region of the
containing scroll view, or other container specified using the
`coordinateSpace` parameter.

`enum ScrollTransitionPhase`

The phases that a view transitions between when it scrolls among other views.

`struct ScrollTransitionConfiguration`

The configuration of a scroll transition that controls how a transition is
applied as a view is scrolled through the visible region of a containing
scroll view or other container.

Instance Method

# scrollTransition(topLeading:bottomTrailing:axis:transition:)

Applies the given transition, animating between the phases of the transition
as this view appears and disappears within the visible region of the
containing scroll view, or other container specified using the
`coordinateSpace` parameter.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func scrollTransition(
        topLeading: ScrollTransitionConfiguration,
        bottomTrailing: ScrollTransitionConfiguration,
        axis: Axis? = nil,
        transition: @escaping (EmptyVisualEffect, ScrollTransitionPhase) -> some VisualEffect
    ) -> some View
    

##  Parameters

`transition`

    

the transition to apply.

`topLeading`

    

The configuration that drives the transition when the view is about to appear
at the top edge of a vertical scroll view, or the leading edge of a horizont
scroll view.

`bottomTrailing`

    

The configuration that drives the transition when the view is about to appear
at the bottom edge of a vertical scroll view, or the trailing edge of a
horizont scroll view.

`axis`

    

The axis of the containing scroll view over which the transition will be
applied. The default value of `nil` uses the axis of the innermost containing
scroll view, or `.vertical` if the innermost scroll view is scrollable along
both axes.

`transition`

    

A closure that applies visual effects as a function of the provided phase.

## See Also

### Animating scroll transitions

`func scrollTransition(ScrollTransitionConfiguration, axis: Axis?, transition:
(EmptyVisualEffect, ScrollTransitionPhase) -> some VisualEffect) -> some View`

Applies the given transition, animating between the phases of the transition
as this view appears and disappears within the visible region of the
containing scroll view, or other container specified using the
`coordinateSpace` parameter.

`enum ScrollTransitionPhase`

The phases that a view transitions between when it scrolls among other views.

`struct ScrollTransitionConfiguration`

The configuration of a scroll transition that controls how a transition is
applied as a view is scrolled through the visible region of a containing
scroll view or other container.

Instance Method

# onTapGesture(count:perform:)

Adds an action to perform when this view recognizes a tap gesture.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 16.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func onTapGesture(
        count: Int = 1,
        perform action: @escaping () -> Void
    ) -> some View
    

##  Parameters

`count`

    

The number of taps or clicks required to trigger the action closure provided
in `action`. Defaults to `1`.

`action`

    

The action to perform.

## Discussion

Use this method to perform the specified `action` when the user clicks or taps
on the view or container `count` times.

Note

If you create a control that’s functionally equivalent to a `Button`, use
`ButtonStyle` to create a customized button instead.

In the example below, the color of the heart images changes to a random color
from the `colors` array whenever the user clicks or taps on the view twice:

    
    
    struct TapGestureExample: View {
        let colors: [Color] = [.gray, .red, .orange, .yellow,
                               .green, .blue, .purple, .pink]
        @State private var fgColor: Color = .gray
    
    
        var body: some View {
            Image(systemName: "heart.fill")
                .resizable()
                .frame(width: 200, height: 200)
                .foregroundColor(fgColor)
                .onTapGesture(count: 2) {
                    fgColor = colors.randomElement()!
                }
        }
    }
    

## See Also

### Recognizing tap gestures

`func onTapGesture(count: Int, coordinateSpace: some CoordinateSpaceProtocol,
perform: (CGPoint) -> Void) -> some View`

Adds an action to perform when this view recognizes a tap gesture, and
provides the action with the location of the interaction.

`struct TapGesture`

A gesture that recognizes one or more taps.

`struct SpatialTapGesture`

A gesture that recognizes one or more taps and reports their location.

Instance Method

# onTapGesture(count:coordinateSpace:perform:)

Adds an action to perform when this view recognizes a tap gesture, and
provides the action with the location of the interaction.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  watchOS 10.0+
visionOS 1.0+

    
    
    func onTapGesture(
        count: Int = 1,
        coordinateSpace: some CoordinateSpaceProtocol = .local,
        perform action: @escaping (CGPoint) -> Void
    ) -> some View
    

##  Parameters

`count`

    

The number of taps or clicks required to trigger the action closure provided
in `action`. Defaults to `1`.

`coordinateSpace`

    

The coordinate space in which to receive location values. Defaults to
`CoordinateSpace.local`.

`action`

    

The action to perform. This closure receives an input that indicates where the
interaction occurred.

## Discussion

Use this method to perform the specified `action` when the user clicks or taps
on the modified view `count` times. The action closure receives the location
of the interaction.

Note

If you create a control that’s functionally equivalent to a `Button`, use
`ButtonStyle` to create a customized button instead.

The following code adds a tap gesture to a `Circle` that toggles the color of
the circle based on the tap location.

## See Also

### Recognizing tap gestures

`func onTapGesture(count: Int, perform: () -> Void) -> some View`

Adds an action to perform when this view recognizes a tap gesture.

`struct TapGesture`

A gesture that recognizes one or more taps.

`struct SpatialTapGesture`

A gesture that recognizes one or more taps and reports their location.

Instance Method

#
onLongPressGesture(minimumDuration:maximumDistance:perform:onPressingChanged:)

Adds an action to perform when this view recognizes a long press gesture.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    func onLongPressGesture(
        minimumDuration: Double = 0.5,
        maximumDistance: CGFloat = 10,
        perform action: @escaping () -> Void,
        onPressingChanged: ((Bool) -> Void)? = nil
    ) -> some View
    

##  Parameters

`minimumDuration`

    

The minimum duration of the long press that must elapse before the gesture
succeeds.

`maximumDistance`

    

The maximum distance that the fingers or cursor performing the long press can
move before the gesture fails.

`action`

    

The action to perform when a long press is recognized.

`onPressingChanged`

    

A closure to run when the pressing state of the gesture changes, passing the
current state as a parameter.

## See Also

### Recognizing long press gestures

`func onLongPressGesture(minimumDuration: Double, perform: () -> Void,
onPressingChanged: ((Bool) -> Void)?) -> some View`

Adds an action to perform when this view recognizes a long press gesture.

`func onLongTouchGesture(minimumDuration: Double, perform: () -> Void,
onTouchingChanged: ((Bool) -> Void)?) -> some View`

Adds an action to perform when this view recognizes a remote long touch
gesture. A long touch gesture is when the finger is on the remote touch
surface without actually pressing.

`struct LongPressGesture`

A gesture that succeeds when the user performs a long press.

Instance Method

# onLongPressGesture(minimumDuration:perform:onPressingChanged:)

Adds an action to perform when this view recognizes a long press gesture.

tvOS 14.0+

    
    
    func onLongPressGesture(
        minimumDuration: Double = 0.5,
        perform action: @escaping () -> Void,
        onPressingChanged: ((Bool) -> Void)? = nil
    ) -> some View
    

##  Parameters

`minimumDuration`

    

The minimum duration of the long press that must elapse before the gesture
succeeds.

`action`

    

The action to perform when a long press is recognized.

`onPressingChanged`

    

A closure to run when the pressing state of the gesture changes, passing the
current state as a parameter.

## See Also

### Recognizing long press gestures

`func onLongPressGesture(minimumDuration: Double, maximumDistance: CGFloat,
perform: () -> Void, onPressingChanged: ((Bool) -> Void)?) -> some View`

Adds an action to perform when this view recognizes a long press gesture.

`func onLongTouchGesture(minimumDuration: Double, perform: () -> Void,
onTouchingChanged: ((Bool) -> Void)?) -> some View`

Adds an action to perform when this view recognizes a remote long touch
gesture. A long touch gesture is when the finger is on the remote touch
surface without actually pressing.

`struct LongPressGesture`

A gesture that succeeds when the user performs a long press.

Instance Method

# onLongTouchGesture(minimumDuration:perform:onTouchingChanged:)

Adds an action to perform when this view recognizes a remote long touch
gesture. A long touch gesture is when the finger is on the remote touch
surface without actually pressing.

tvOS 16.0+

    
    
    func onLongTouchGesture(
        minimumDuration: Double = 0.5,
        perform action: @escaping () -> Void,
        onTouchingChanged: ((Bool) -> Void)? = nil
    ) -> some View
    

##  Parameters

`minimumDuration`

    

The minimum duration of the long touch that must elapse before the gesture
succeeds.

`action`

    

The action to perform when a long touch is recognized

`onTouchingChanged`

    

A closure to run when the touching state of the gesture changes, passing the
current state as a parameter.

## See Also

### Recognizing long press gestures

`func onLongPressGesture(minimumDuration: Double, maximumDistance: CGFloat,
perform: () -> Void, onPressingChanged: ((Bool) -> Void)?) -> some View`

Adds an action to perform when this view recognizes a long press gesture.

`func onLongPressGesture(minimumDuration: Double, perform: () -> Void,
onPressingChanged: ((Bool) -> Void)?) -> some View`

Adds an action to perform when this view recognizes a long press gesture.

`struct LongPressGesture`

A gesture that succeeds when the user performs a long press.

Instance Method

# gesture(_:including:)

Attaches a gesture to the view with a lower precedence than gestures defined
by the view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func gesture<T>(
        _ gesture: T,
        including mask: GestureMask = .all
    ) -> some View where T : Gesture
    

##  Parameters

`gesture`

    

A gesture to attach to the view.

`mask`

    

A value that controls how adding this gesture to the view affects other
gestures recognized by the view and its subviews. Defaults to `all`.

## Discussion

Use this method when you need to attach a gesture to a view. The example below
defines a custom gesture that prints a message to the console and attaches it
to the view’s `VStack`. Inside the `VStack` a red heart `Image` defines its
own `TapGesture` handler that also prints a message to the console, and blue
rectangle with no custom gesture handlers. Tapping or clicking the image
prints a message to the console from the tap gesture handler on the image,
while tapping or clicking the rectangle inside the `VStack` prints a message
in the console from the enclosing vertical stack gesture handler.

    
    
    struct GestureExample: View {
        @State private var message = "Message"
        let newGesture = TapGesture().onEnded {
            print("Tap on VStack.")
        }
    
    
        var body: some View {
            VStack(spacing:25) {
                Image(systemName: "heart.fill")
                    .resizable()
                    .frame(width: 75, height: 75)
                    .padding()
                    .foregroundColor(.red)
                    .onTapGesture {
                        print("Tap on image.")
                    }
                Rectangle()
                    .fill(Color.blue)
            }
            .gesture(newGesture)
            .frame(width: 200, height: 200)
            .border(Color.purple)
        }
    }
    

## See Also

### Recognizing gestures that change over time

`struct DragGesture`

A dragging motion that invokes an action as the drag-event sequence changes.

`struct MagnifyGesture`

A gesture that recognizes a magnification motion and tracks the amount of
magnification.

`struct RotateGesture`

A gesture that recognizes a rotation motion and tracks the angle of the
rotation.

`struct RotateGesture3D`

A gesture that recognizes 3D rotation motion and tracks the angle and axis of
the rotation.

`struct GestureMask`

Options that control how adding a gesture to a view affects other gestures
recognized by the view and its subviews.

Instance Method

# highPriorityGesture(_:including:)

Attaches a gesture to the view with a higher precedence than gestures defined
by the view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func highPriorityGesture<T>(
        _ gesture: T,
        including mask: GestureMask = .all
    ) -> some View where T : Gesture
    

##  Parameters

`gesture`

    

A gesture to attach to the view.

`mask`

    

A value that controls how adding this gesture to the view affects other
gestures recognized by the view and its subviews. Defaults to `all`.

## Discussion

Use this method when you need to define a high priority gesture to take
precedence over the view’s existing gestures. The example below defines a
custom gesture that prints a message to the console and attaches it to the
view’s `VStack`. Inside the `VStack` a red heart `Image` defines its own
`TapGesture` handler that also prints a message to the console, and a blue
rectangle with no custom gesture handlers. Tapping or clicking any of the
views results in a console message from the high priority gesture attached to
the enclosing `VStack`.

## See Also

### Defining custom gestures

`func defersSystemGestures(on: Edge.Set) -> some View`

Sets the screen edge from which you want your gesture to take precedence over
the system gesture.

`protocol Gesture`

An instance that matches a sequence of events to a gesture, and returns a
stream of values for each of its states.

`struct AnyGesture`

A type-erased gesture.

`struct HandActivationBehavior`

An activation behavior specific to hand-driven input.

Instance Method

# simultaneousGesture(_:including:)

Attaches a gesture to the view to process simultaneously with gestures defined
by the view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func simultaneousGesture<T>(
        _ gesture: T,
        including mask: GestureMask = .all
    ) -> some View where T : Gesture
    

##  Parameters

`gesture`

    

A gesture to attach to the view.

`mask`

    

A value that controls how adding this gesture to the view affects other
gestures recognized by the view and its subviews. Defaults to `all`.

## Discussion

Use this method when you need to define and process a view specific gesture
simultaneously with the same priority as the view’s existing gestures. The
example below defines a custom gesture that prints a message to the console
and attaches it to the view’s `VStack`. Inside the `VStack` is a red heart
`Image` defines its own `TapGesture` handler that also prints a message to the
console and a blue rectangle with no custom gesture handlers.

Tapping or clicking the “heart” image sends two messages to the console: one
for the image’s tap gesture handler, and the other from a custom gesture
handler attached to the enclosing vertical stack. Tapping or clicking on the
blue rectangle results only in the single message to the console from the tap
recognizer attached to the `VStack`:

## See Also

### Combining gestures

Composing SwiftUI gestures

Combine gestures to create complex interactions.

`struct SequenceGesture`

A gesture that’s a sequence of two gestures.

`struct SimultaneousGesture`

A gesture containing two gestures that can happen at the same time with
neither of them preceding the other.

`struct ExclusiveGesture`

A gesture that consists of two gestures where only one of them can succeed.

Instance Method

# defersSystemGestures(on:)

Sets the screen edge from which you want your gesture to take precedence over
the system gesture.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+

    
    
    func defersSystemGestures(on edges: Edge.Set) -> some View
    

##  Parameters

`edges`

    

A value that indicates the screen edge from which you want your gesture to
take precedence over the system gesture.

## Discussion

The following code defers the vertical screen edges system gestures of a given
canvas.

## See Also

### Defining custom gestures

`func highPriorityGesture<T>(T, including: GestureMask) -> some View`

Attaches a gesture to the view with a higher precedence than gestures defined
by the view.

`protocol Gesture`

An instance that matches a sequence of events to a gesture, and returns a
stream of values for each of its states.

`struct AnyGesture`

A type-erased gesture.

`struct HandActivationBehavior`

An activation behavior specific to hand-driven input.

Instance Method

# onKeyPress(_:action:)

Performs an action if the user presses a key on a hardware keyboard while the
view has focus.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    func onKeyPress(
        _ key: KeyEquivalent,
        action: @escaping () -> KeyPress.Result
    ) -> some View
    

##  Parameters

`key`

    

The key to match against incoming hardware keyboard events.

`action`

    

The action to perform. Return `.handled` to consume the event and prevent
further dispatch, or `.ignored` to allow dispatch to continue.

## Return Value

A modified view that binds hardware keyboard input when focused.

## Discussion

SwiftUI performs the action for key-down and key-repeat events.

## See Also

### Responding to keyboard input

`func onKeyPress(phases: KeyPress.Phases, action: (KeyPress) ->
KeyPress.Result) -> some View`

Performs an action if the user presses any key on a hardware keyboard while
the view has focus.

`func onKeyPress(KeyEquivalent, phases: KeyPress.Phases, action: (KeyPress) ->
KeyPress.Result) -> some View`

Performs an action if the user presses a key on a hardware keyboard while the
view has focus.

`func onKeyPress(characters: CharacterSet, phases: KeyPress.Phases, action:
(KeyPress) -> KeyPress.Result) -> some View`

Performs an action if the user presses one or more keys on a hardware keyboard
while the view has focus.

`func onKeyPress(keys: Set<KeyEquivalent>, phases: KeyPress.Phases, action:
(KeyPress) -> KeyPress.Result) -> some View`

Performs an action if the user presses one or more keys on a hardware keyboard
while the view has focus.

`struct KeyPress`

Instance Method

# onKeyPress(phases:action:)

Performs an action if the user presses any key on a hardware keyboard while
the view has focus.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    func onKeyPress(
        phases: KeyPress.Phases = [.down, .repeat],
        action: @escaping (KeyPress) -> KeyPress.Result
    ) -> some View
    

##  Parameters

`phases`

    

The key-press phases to match (`.down`, `.repeat`, and `.up`). The default
value is `[.down, .repeat]`.

`action`

    

The action to perform. The action receives a value describing the matched key
event. Return `.handled` to consume the event and prevent further dispatch, or
`.ignored` to allow dispatch to continue.

## Return Value

A modified view that binds hardware keyboard input when focused.

## See Also

### Responding to keyboard input

`func onKeyPress(KeyEquivalent, action: () -> KeyPress.Result) -> some View`

Performs an action if the user presses a key on a hardware keyboard while the
view has focus.

`func onKeyPress(KeyEquivalent, phases: KeyPress.Phases, action: (KeyPress) ->
KeyPress.Result) -> some View`

Performs an action if the user presses a key on a hardware keyboard while the
view has focus.

`func onKeyPress(characters: CharacterSet, phases: KeyPress.Phases, action:
(KeyPress) -> KeyPress.Result) -> some View`

Performs an action if the user presses one or more keys on a hardware keyboard
while the view has focus.

`func onKeyPress(keys: Set<KeyEquivalent>, phases: KeyPress.Phases, action:
(KeyPress) -> KeyPress.Result) -> some View`

Performs an action if the user presses one or more keys on a hardware keyboard
while the view has focus.

`struct KeyPress`

Instance Method

# onKeyPress(_:phases:action:)

Performs an action if the user presses a key on a hardware keyboard while the
view has focus.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    func onKeyPress(
        _ key: KeyEquivalent,
        phases: KeyPress.Phases,
        action: @escaping (KeyPress) -> KeyPress.Result
    ) -> some View
    

##  Parameters

`key`

    

The key to match against incoming hardware keyboard events.

`phases`

    

The key-press phases to match (`.down`, `.up`, and `.repeat`).

`action`

    

The action to perform. The action receives a value describing the matched key
event. Return `.handled` to consume the event and prevent further dispatch, or
`.ignored` to allow dispatch to continue.

## Return Value

A modified view that binds hardware keyboard input when focused.

## Discussion

SwiftUI performs the action for the specified event phases.

## See Also

### Responding to keyboard input

`func onKeyPress(KeyEquivalent, action: () -> KeyPress.Result) -> some View`

Performs an action if the user presses a key on a hardware keyboard while the
view has focus.

`func onKeyPress(phases: KeyPress.Phases, action: (KeyPress) ->
KeyPress.Result) -> some View`

Performs an action if the user presses any key on a hardware keyboard while
the view has focus.

`func onKeyPress(characters: CharacterSet, phases: KeyPress.Phases, action:
(KeyPress) -> KeyPress.Result) -> some View`

Performs an action if the user presses one or more keys on a hardware keyboard
while the view has focus.

`func onKeyPress(keys: Set<KeyEquivalent>, phases: KeyPress.Phases, action:
(KeyPress) -> KeyPress.Result) -> some View`

Performs an action if the user presses one or more keys on a hardware keyboard
while the view has focus.

`struct KeyPress`

Instance Method

# onKeyPress(characters:phases:action:)

Performs an action if the user presses one or more keys on a hardware keyboard
while the view has focus.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    func onKeyPress(
        characters: CharacterSet,
        phases: KeyPress.Phases = [.down, .repeat],
        action: @escaping (KeyPress) -> KeyPress.Result
    ) -> some View
    

##  Parameters

`characters`

    

The set of characters to match against incoming hardware keyboard events.

`phases`

    

The key-press phases to match (`.down`, `.repeat`, and `.up`). The default
value is `[.down, .repeat]`.

`action`

    

The action to perform. The action receives a value describing the matched key
event. Return `.handled` to consume the event and prevent further dispatch, or
`.ignored` to allow dispatch to continue.

## Return Value

A modified view that binds hardware keyboard input when focused.

## See Also

### Responding to keyboard input

`func onKeyPress(KeyEquivalent, action: () -> KeyPress.Result) -> some View`

Performs an action if the user presses a key on a hardware keyboard while the
view has focus.

`func onKeyPress(phases: KeyPress.Phases, action: (KeyPress) ->
KeyPress.Result) -> some View`

Performs an action if the user presses any key on a hardware keyboard while
the view has focus.

`func onKeyPress(KeyEquivalent, phases: KeyPress.Phases, action: (KeyPress) ->
KeyPress.Result) -> some View`

Performs an action if the user presses a key on a hardware keyboard while the
view has focus.

`func onKeyPress(keys: Set<KeyEquivalent>, phases: KeyPress.Phases, action:
(KeyPress) -> KeyPress.Result) -> some View`

Performs an action if the user presses one or more keys on a hardware keyboard
while the view has focus.

`struct KeyPress`

Instance Method

# onKeyPress(keys:phases:action:)

Performs an action if the user presses one or more keys on a hardware keyboard
while the view has focus.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    func onKeyPress(
        keys: Set<KeyEquivalent>,
        phases: KeyPress.Phases = [.down, .repeat],
        action: @escaping (KeyPress) -> KeyPress.Result
    ) -> some View
    

##  Parameters

`keys`

    

A set of keys to match against incoming hardware keyboard events.

`phases`

    

The key-press phases to match (`.down`, `.repeat`, and `.up`). The default
value is `[.down, .repeat]`.

`action`

    

The action to perform. The action receives a value describing the matched key
event. Return `.handled` to consume the event and prevent further dispatch, or
`.ignored` to allow dispatch to continue.

## Return Value

A modified view that binds keyboard input when focused.

## See Also

### Responding to keyboard input

`func onKeyPress(KeyEquivalent, action: () -> KeyPress.Result) -> some View`

Performs an action if the user presses a key on a hardware keyboard while the
view has focus.

`func onKeyPress(phases: KeyPress.Phases, action: (KeyPress) ->
KeyPress.Result) -> some View`

Performs an action if the user presses any key on a hardware keyboard while
the view has focus.

`func onKeyPress(KeyEquivalent, phases: KeyPress.Phases, action: (KeyPress) ->
KeyPress.Result) -> some View`

Performs an action if the user presses a key on a hardware keyboard while the
view has focus.

`func onKeyPress(characters: CharacterSet, phases: KeyPress.Phases, action:
(KeyPress) -> KeyPress.Result) -> some View`

Performs an action if the user presses one or more keys on a hardware keyboard
while the view has focus.

`struct KeyPress`

Instance Method

# keyboardShortcut(_:)

Assigns a keyboard shortcut to the modified control.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    func keyboardShortcut(_ shortcut: KeyboardShortcut) -> some View
    

## Discussion

Pressing the control’s shortcut while the control is anywhere in the frontmost
window or scene, or anywhere in the macOS main menu, is equivalent to direct
interaction with the control to perform its primary action.

The target of a keyboard shortcut is resolved in a leading-to-trailing
traversal of one or more view hierarchies. On macOS, the system looks in the
key window first, then the main window, and then the command groups; on other
platforms, the system looks in the active scene, and then the command groups.

If multiple controls are associated with the same shortcut, the first one
found is used.

## See Also

### Creating keyboard shortcuts

`func keyboardShortcut(KeyboardShortcut?) -> some View`

Assigns an optional keyboard shortcut to the modified control.

`func keyboardShortcut(KeyEquivalent, modifiers: EventModifiers) -> some View`

Defines a keyboard shortcut and assigns it to the modified control.

`func keyboardShortcut(KeyEquivalent, modifiers: EventModifiers, localization:
KeyboardShortcut.Localization) -> some View`

Defines a keyboard shortcut and assigns it to the modified control.

`var keyboardShortcut: KeyboardShortcut?`

The keyboard shortcut that buttons in this environment will be triggered with.

`struct KeyboardShortcut`

Keyboard shortcuts describe combinations of keys on a keyboard that the user
can press in order to activate a button or toggle.

`struct KeyEquivalent`

Key equivalents consist of a letter, punctuation, or function key that can be
combined with an optional set of modifier keys to specify a keyboard shortcut.

`struct EventModifiers`

A set of key modifiers that you can add to a gesture.

Instance Method

# keyboardShortcut(_:)

Assigns an optional keyboard shortcut to the modified control.

iOS 15.4+  iPadOS 15.4+  macOS 12.3+  Mac Catalyst 15.4+  visionOS 1.0+

    
    
    func keyboardShortcut(_ shortcut: KeyboardShortcut?) -> some View
    

## Discussion

Pressing the control’s shortcut while the control is anywhere in the frontmost
window or scene, or anywhere in the macOS main menu, is equivalent to direct
interaction with the control to perform its primary action.

The target of a keyboard shortcut is resolved in a leading-to-trailing
traversal of one or more view hierarchies. On macOS, the system looks in the
key window first, then the main window, and then the command groups; on other
platforms, the system looks in the active scene, and then the command groups.

If multiple controls are associated with the same shortcut, the first one
found is used. If the provided shortcut is `nil`, the modifier will have no
effect.

## See Also

### Creating keyboard shortcuts

`func keyboardShortcut(KeyboardShortcut) -> some View`

Assigns a keyboard shortcut to the modified control.

`func keyboardShortcut(KeyEquivalent, modifiers: EventModifiers) -> some View`

Defines a keyboard shortcut and assigns it to the modified control.

`func keyboardShortcut(KeyEquivalent, modifiers: EventModifiers, localization:
KeyboardShortcut.Localization) -> some View`

Defines a keyboard shortcut and assigns it to the modified control.

`var keyboardShortcut: KeyboardShortcut?`

The keyboard shortcut that buttons in this environment will be triggered with.

`struct KeyboardShortcut`

Keyboard shortcuts describe combinations of keys on a keyboard that the user
can press in order to activate a button or toggle.

`struct KeyEquivalent`

Key equivalents consist of a letter, punctuation, or function key that can be
combined with an optional set of modifier keys to specify a keyboard shortcut.

`struct EventModifiers`

A set of key modifiers that you can add to a gesture.

Instance Method

# keyboardShortcut(_:modifiers:)

Defines a keyboard shortcut and assigns it to the modified control.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    func keyboardShortcut(
        _ key: KeyEquivalent,
        modifiers: EventModifiers = .command
    ) -> some View
    

## Discussion

Pressing the control’s shortcut while the control is anywhere in the frontmost
window or scene, or anywhere in the macOS main menu, is equivalent to direct
interaction with the control to perform its primary action.

The target of a keyboard shortcut is resolved in a leading-to-trailing, depth-
first traversal of one or more view hierarchies. On macOS, the system looks in
the key window first, then the main window, and then the command groups; on
other platforms, the system looks in the active scene, and then the command
groups.

If multiple controls are associated with the same shortcut, the first one
found is used.

The default localization configuration is set to `automatic`.

## See Also

### Creating keyboard shortcuts

`func keyboardShortcut(KeyboardShortcut) -> some View`

Assigns a keyboard shortcut to the modified control.

`func keyboardShortcut(KeyboardShortcut?) -> some View`

Assigns an optional keyboard shortcut to the modified control.

`func keyboardShortcut(KeyEquivalent, modifiers: EventModifiers, localization:
KeyboardShortcut.Localization) -> some View`

Defines a keyboard shortcut and assigns it to the modified control.

`var keyboardShortcut: KeyboardShortcut?`

The keyboard shortcut that buttons in this environment will be triggered with.

`struct KeyboardShortcut`

Keyboard shortcuts describe combinations of keys on a keyboard that the user
can press in order to activate a button or toggle.

`struct KeyEquivalent`

Key equivalents consist of a letter, punctuation, or function key that can be
combined with an optional set of modifier keys to specify a keyboard shortcut.

`struct EventModifiers`

A set of key modifiers that you can add to a gesture.

Instance Method

# keyboardShortcut(_:modifiers:localization:)

Defines a keyboard shortcut and assigns it to the modified control.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    func keyboardShortcut(
        _ key: KeyEquivalent,
        modifiers: EventModifiers = .command,
        localization: KeyboardShortcut.Localization
    ) -> some View
    

## Discussion

Pressing the control’s shortcut while the control is anywhere in the frontmost
window or scene, or anywhere in the macOS main menu, is equivalent to direct
interaction with the control to perform its primary action.

The target of a keyboard shortcut is resolved in a leading-to-trailing, depth-
first traversal of one or more view hierarchies. On macOS, the system looks in
the key window first, then the main window, and then the command groups; on
other platforms, the system looks in the active scene, and then the command
groups.

If multiple controls are associated with the same shortcut, the first one
found is used.

### Localization

Provide a `localization` value to specify how this shortcut should be
localized. Given that `key` is always defined in relation to the US-English
keyboard layout, it might be hard to reach on different international layouts.
For example the shortcut `⌘[` works well for the US layout but is hard to
reach for German users, where `[` is available by pressing `⌥5`, making users
type `⌥⌘5`. The automatic keyboard shortcut remapping re-assigns the shortcut
to an appropriate replacement, `⌘Ö` in this case.

Certain shortcuts carry information about directionality. For instance, `⌘[`
can reveal a previous view. Following the layout direction of the UI, this
shortcut will be automatically mirrored to `⌘]`. However, this does not apply
to items such as “Align Left `⌘{`”, which will be “left” independently of the
layout direction. When the shortcut shouldn’t follow the directionality of the
UI, but rather be the same in both right-to-left and left-to-right directions,
using `withoutMirroring` will prevent the system from flipping it.

    
    
    var body: some Commands {
        CommandMenu("Card") {
            Button("Align Left") { ... }
                .keyboardShortcut("{",
                     modifiers: .option,
                     localization: .withoutMirroring)
            Button("Align Right") { ... }
                .keyboardShortcut("}",
                     modifiers: .option,
                     localization: .withoutMirroring)
        }
    }
    

Lastly, providing the option `custom` disables the automatic localization for
this shortcut to tell the system that internationalization is taken care of in
a different way.

## See Also

### Creating keyboard shortcuts

`func keyboardShortcut(KeyboardShortcut) -> some View`

Assigns a keyboard shortcut to the modified control.

`func keyboardShortcut(KeyboardShortcut?) -> some View`

Assigns an optional keyboard shortcut to the modified control.

`func keyboardShortcut(KeyEquivalent, modifiers: EventModifiers) -> some View`

Defines a keyboard shortcut and assigns it to the modified control.

`var keyboardShortcut: KeyboardShortcut?`

The keyboard shortcut that buttons in this environment will be triggered with.

`struct KeyboardShortcut`

Keyboard shortcuts describe combinations of keys on a keyboard that the user
can press in order to activate a button or toggle.

`struct KeyEquivalent`

Key equivalents consist of a letter, punctuation, or function key that can be
combined with an optional set of modifier keys to specify a keyboard shortcut.

`struct EventModifiers`

A set of key modifiers that you can add to a gesture.

Instance Method

# onHover(perform:)

Adds an action to perform when the user moves the pointer over or away from
the view’s frame.

iOS 13.4+  iPadOS 13.4+  macOS 10.15+  Mac Catalyst 13.4+  visionOS 1.0+

    
    
    func onHover(perform action: @escaping (Bool) -> Void) -> some View
    

##  Parameters

`action`

    

The action to perform whenever the pointer enters or exits this view’s frame.
If the pointer is in the view’s frame, the `action` closure passes `true` as a
parameter; otherwise, `false`.

## Return Value

A view that triggers `action` when the pointer enters or exits this view’s
frame.

## Discussion

Calling this method defines a region for detecting pointer movement with the
size and position of this view.

## See Also

### Responding to hover events

`func onContinuousHover(coordinateSpace: some CoordinateSpaceProtocol,
perform: (HoverPhase) -> Void) -> some View`

Adds an action to perform when the pointer enters, moves within, and exits the
view’s bounds.

`func hoverEffect(HoverEffect, isEnabled: Bool) -> some View`

Applies a hover effect to this view.

`func hoverEffectDisabled(Bool) -> some View`

Adds a condition that controls whether this view can display hover effects.

`func defaultHoverEffect(HoverEffect?) -> some View`

Sets the default hover effect to use for views within this view.

`var isHoverEffectEnabled: Bool`

A Boolean value that indicates whether the view associated with this
environment allows hover effects to be displayed.

`enum HoverPhase`

The current hovering state and value of the pointer.

Instance Method

# onContinuousHover(coordinateSpace:perform:)

Adds an action to perform when the pointer enters, moves within, and exits the
view’s bounds.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    func onContinuousHover(
        coordinateSpace: some CoordinateSpaceProtocol = .local,
        perform action: @escaping (HoverPhase) -> Void
    ) -> some View
    

##  Parameters

`coordinateSpace`

    

The coordinate space for the location values. The default value is
`CoordinateSpace.local`.

`action`

    

The action to perform whenever the pointer enters, moves within, or exits the
view’s bounds. The closure takes a `phase` input that has the value
`HoverPhase.active(_:)` and contains the pointer’s coordinates if the pointer
is within the view’s bounds. The closure receives the `HoverPhase.ended` phase
when the pointer leaves the view’s bounds.

## Return Value

A view that calls `action` when the pointer enters, moves within, or exits the
view’s bounds.

## Discussion

Use this modifier to define a region for detecting pointer movement with a
view. The following example updates a small rectangle’s position and style by
modifying `hoverLocation` and `isHovering` as the pointer moves within the
larger, red rectangle:

## See Also

### Responding to hover events

`func onHover(perform: (Bool) -> Void) -> some View`

Adds an action to perform when the user moves the pointer over or away from
the view’s frame.

`func hoverEffect(HoverEffect, isEnabled: Bool) -> some View`

Applies a hover effect to this view.

`func hoverEffectDisabled(Bool) -> some View`

Adds a condition that controls whether this view can display hover effects.

`func defaultHoverEffect(HoverEffect?) -> some View`

Sets the default hover effect to use for views within this view.

`var isHoverEffectEnabled: Bool`

A Boolean value that indicates whether the view associated with this
environment allows hover effects to be displayed.

`enum HoverPhase`

The current hovering state and value of the pointer.

Instance Method

# hoverEffect(_:)

Applies a hover effect to this view.

iOS 13.4+  iPadOS 13.4+  Mac Catalyst 13.4+  tvOS 16.0+  visionOS 1.0+

    
    
    func hoverEffect(_ effect: HoverEffect = .automatic) -> some View
    

##  Parameters

`effect`

    

The effect to apply to this view.

`isEnabled`

    

Whether the effect is enabled or not.

## Return Value

A new view that applies a hover effect to `self`.

## Discussion

By default, `automatic` is used. You can control the behavior of the automatic
effect with the `defaultHoverEffect(_:)` modifier.

## See Also

### Changing view appearance for hover events

`struct HoverEffect`

An effect applied when the pointer hovers over a view.

Instance Method

# hoverEffect(_:isEnabled:)

Applies a hover effect to this view.

iOS 17.0+  iPadOS 17.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS 1.0+

    
    
    func hoverEffect(
        _ effect: HoverEffect = .automatic,
        isEnabled: Bool = true
    ) -> some View
    

##  Parameters

`effect`

    

The effect to apply to this view.

`isEnabled`

    

Whether the effect is enabled or not.

## Return Value

A new view that applies a hover effect to `self`.

## Discussion

By default, `automatic` is used. You can control the behavior of the automatic
effect with the `defaultHoverEffect(_:)` modifier.

## See Also

### Responding to hover events

`func onHover(perform: (Bool) -> Void) -> some View`

Adds an action to perform when the user moves the pointer over or away from
the view’s frame.

`func onContinuousHover(coordinateSpace: some CoordinateSpaceProtocol,
perform: (HoverPhase) -> Void) -> some View`

Adds an action to perform when the pointer enters, moves within, and exits the
view’s bounds.

`func hoverEffectDisabled(Bool) -> some View`

Adds a condition that controls whether this view can display hover effects.

`func defaultHoverEffect(HoverEffect?) -> some View`

Sets the default hover effect to use for views within this view.

`var isHoverEffectEnabled: Bool`

A Boolean value that indicates whether the view associated with this
environment allows hover effects to be displayed.

`enum HoverPhase`

The current hovering state and value of the pointer.

Instance Method

# hoverEffectDisabled(_:)

Adds a condition that controls whether this view can display hover effects.

iOS 17.0+  iPadOS 17.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS 1.0+

    
    
    func hoverEffectDisabled(_ disabled: Bool = true) -> some View
    

##  Parameters

`disabled`

    

A Boolean value that determines whether this view can display hover effects.

## Return Value

A view that controls whether hover effects can be displayed in this view.

## Discussion

The higher views in a view hierarchy can override the value you set on this
view. In the following example, the button does not display a hover effect
because the outer `hoverEffectDisabled(_:)` modifier overrides the inner one:

## See Also

### Responding to hover events

`func onHover(perform: (Bool) -> Void) -> some View`

Adds an action to perform when the user moves the pointer over or away from
the view’s frame.

`func onContinuousHover(coordinateSpace: some CoordinateSpaceProtocol,
perform: (HoverPhase) -> Void) -> some View`

Adds an action to perform when the pointer enters, moves within, and exits the
view’s bounds.

`func hoverEffect(HoverEffect, isEnabled: Bool) -> some View`

Applies a hover effect to this view.

`func defaultHoverEffect(HoverEffect?) -> some View`

Sets the default hover effect to use for views within this view.

`var isHoverEffectEnabled: Bool`

A Boolean value that indicates whether the view associated with this
environment allows hover effects to be displayed.

`enum HoverPhase`

The current hovering state and value of the pointer.

Instance Method

# defaultHoverEffect(_:)

Sets the default hover effect to use for views within this view.

iOS 17.0+  iPadOS 17.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS 1.0+

    
    
    func defaultHoverEffect(_ effect: HoverEffect?) -> some View
    

##  Parameters

`effect`

    

The default hover effect to use for views within this view.

## Return Value

A view that uses this effect as the default hover effect.

## Discussion

Use this modifier to set a specific hover effect for all views with the
`hoverEffect(_:)` modifier applied within a view. The default effect is
typically used when no `HoverEffect` was provided or if `automatic` is
specified.

For example, this view uses `highlight` for both the red and green Color
views:

This also works for customizing the default hover effect in views like
`Button`s when using a SwiftUI-defined style like `ButtonStyle/bordered`,
which can provide a hover effect by default. For example, this view replaces
the hover effect for a `Button` with `highlight`:

Use a `nil` effect to indicate that the default hover effect should not be
modified.

## See Also

### Responding to hover events

`func onHover(perform: (Bool) -> Void) -> some View`

Adds an action to perform when the user moves the pointer over or away from
the view’s frame.

`func onContinuousHover(coordinateSpace: some CoordinateSpaceProtocol,
perform: (HoverPhase) -> Void) -> some View`

Adds an action to perform when the pointer enters, moves within, and exits the
view’s bounds.

`func hoverEffect(HoverEffect, isEnabled: Bool) -> some View`

Applies a hover effect to this view.

`func hoverEffectDisabled(Bool) -> some View`

Adds a condition that controls whether this view can display hover effects.

`var isHoverEffectEnabled: Bool`

A Boolean value that indicates whether the view associated with this
environment allows hover effects to be displayed.

`enum HoverPhase`

The current hovering state and value of the pointer.

Instance Method

# listRowHoverEffect(_:)

Requests that the containing list row use the provided hover effect.

visionOS 1.0+

    
    
    func listRowHoverEffect(_ effect: HoverEffect?) -> some View
    

##  Parameters

`effect`

    

The hover effect applied to the entire list row.

## Return Value

A view that requests a hover effect for a containing list row

## Discussion

By default, `List` rows have built-in hover effects in visionOS. In some
cases, it is useful to change the default hover effect.

This modifier can be applied to a list row’s content to request that the list
row’s default effect be replaced by the provided effect. If the view is not
contained within a `List` or if the view does not support hover effects in
this context, the modifier has no effect.

Use a `nil` effect to indicate that the list row’s default hover effect should
not be modified.

## See Also

### Configuring rows

`func listRowInsets(EdgeInsets?) -> some View`

Applies an inset to the rows in a list.

`func listRowHoverEffectDisabled(Bool) -> some View`

Requests that the containing list row have its hover effect disabled.

`func listItemTint(Color?) -> some View`

Sets a fixed tint color for content in a list.

`func listItemTint(ListItemTint?) -> some View`

Sets the tint effect for content in a list.

`struct ListItemTint`

A tint effect configuration that you can apply to content in a list.

`var defaultMinListRowHeight: CGFloat`

The default minimum height of a row in a `List`. The default minimum height of
a row in a list.

Instance Method

# listRowHoverEffectDisabled(_:)

Requests that the containing list row have its hover effect disabled.

visionOS 1.0+

    
    
    func listRowHoverEffectDisabled(_ disabled: Bool = true) -> some View
    

##  Parameters

`disabled`

    

A Boolean value that determines whether the containing list row should display
its default hover effect.

## Return Value

A view that requests the default hover effect on its containing list row to
conditionally be disabled.

## Discussion

By default, `List` rows have built-in hover effects in visionOS. In some
cases, it is useful to disable the default hover effect.

## See Also

### Configuring rows

`func listRowInsets(EdgeInsets?) -> some View`

Applies an inset to the rows in a list.

`func listRowHoverEffect(HoverEffect?) -> some View`

Requests that the containing list row use the provided hover effect.

`func listItemTint(Color?) -> some View`

Sets a fixed tint color for content in a list.

`func listItemTint(ListItemTint?) -> some View`

Sets the tint effect for content in a list.

`struct ListItemTint`

A tint effect configuration that you can apply to content in a list.

`var defaultMinListRowHeight: CGFloat`

The default minimum height of a row in a `List`. The default minimum height of
a row in a list.

Instance Method

# focused(_:equals:)

Modifies this view by binding its focus state to the given state value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func focused<Value>(
        _ binding: FocusState<Value>.Binding,
        equals value: Value
    ) -> some View where Value : Hashable
    

##  Parameters

`binding`

    

The state binding to register. When focus moves to the modified view, the
binding sets the bound value to the corresponding match value. If a caller
sets the state value programmatically to the matching value, then focus moves
to the modified view. When focus leaves the modified view, the binding sets
the bound value to `nil`. If a caller sets the value to `nil`, SwiftUI
automatically dismisses focus.

`value`

    

The value to match against when determining whether the binding should change.

## Return Value

The modified view.

## Discussion

Use this modifier to cause the view to receive focus whenever the the
`binding` equals the `value`. Typically, you create an enumeration of fields
that may receive focus, bind an instance of this enumeration, and assign its
cases to focusable views.

The following example uses the cases of a `LoginForm` enumeration to bind the
focus state of two `TextField` views. A sign-in button validates the fields
and sets the bound `focusedField` value to any field that requires the user to
correct a problem.

    
    
    struct LoginForm {
        enum Field: Hashable {
            case usernameField
            case passwordField
        }
    
    
        @State private var username = ""
        @State private var password = ""
        @FocusState private var focusedField: Field?
    
    
        var body: some View {
            Form {
                TextField("Username", text: $username)
                    .focused($focusedField, equals: .usernameField)
    
    
                SecureField("Password", text: $password)
                    .focused($focusedField, equals: .passwordField)
    
    
                Button("Sign In") {
                    if username.isEmpty {
                        focusedField = .usernameField
                    } else if password.isEmpty {
                        focusedField = .passwordField
                    } else {
                        handleLogin(username, password)
                    }
                }
            }
        }
    }
    

To control focus using a Boolean, use the `focused(_:)` method instead.

## See Also

### Managing focus state

`func focused(FocusState<Bool>.Binding) -> some View`

Modifies this view by binding its focus state to the given Boolean state
value.

`var isFocused: Bool`

Returns whether the nearest focusable ancestor has focus.

`struct FocusState`

A property wrapper type that can read and write a value that SwiftUI updates
as the placement of focus within the scene changes.

`struct FocusedValue`

A property wrapper for observing values from the focused view or one of its
ancestors.

`protocol FocusedValueKey`

A protocol for identifier types used when publishing and observing focused
values.

`struct FocusedBinding`

A convenience property wrapper for observing and automatically unwrapping
state bindings from the focused view or one of its ancestors.

Instance Method

# focused(_:)

Modifies this view by binding its focus state to the given Boolean state
value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func focused(_ condition: FocusState<Bool>.Binding) -> some View
    

##  Parameters

`condition`

    

The focus state to bind. When focus moves to the view, the binding sets the
bound value to `true`. If a caller sets the value to `true` programmatically,
then focus moves to the modified view. When focus leaves the modified view,
the binding sets the value to `false`. If a caller sets the value to `false`,
SwiftUI automatically dismisses focus.

## Return Value

The modified view.

## Discussion

Use this modifier to cause the view to receive focus whenever the the
`condition` value is `true`. You can use this modifier to observe the focus
state of a single view, or programmatically set and remove focus from the
view.

In the following example, a single `TextField` accepts a user’s desired
`username`. The text field binds its focus state to the Boolean value
`usernameFieldIsFocused`. A “Submit” button’s action verifies whether the name
is available. If the name is unavailable, the button sets
`usernameFieldIsFocused` to `true`, which causes focus to return to the text
field, so the user can enter a different name.

    
    
    @State private var username: String = ""
    @FocusState private var usernameFieldIsFocused: Bool
    @State private var showUsernameTaken = false
    
    
    var body: some View {
        VStack {
            TextField("Choose a username.", text: $username)
                .focused($usernameFieldIsFocused)
            if showUsernameTaken {
                Text("That username is taken. Please choose another.")
            }
            Button("Submit") {
                showUsernameTaken = false
                if !isUserNameAvailable(username: username) {
                    usernameFieldIsFocused = true
                    showUsernameTaken = true
                }
            }
        }
    }
    

To control focus by matching a value, use the `focused(_:equals:)` method
instead.

## See Also

### Managing focus state

`func focused<Value>(FocusState<Value>.Binding, equals: Value) -> some View`

Modifies this view by binding its focus state to the given state value.

`var isFocused: Bool`

Returns whether the nearest focusable ancestor has focus.

`struct FocusState`

A property wrapper type that can read and write a value that SwiftUI updates
as the placement of focus within the scene changes.

`struct FocusedValue`

A property wrapper for observing values from the focused view or one of its
ancestors.

`protocol FocusedValueKey`

A protocol for identifier types used when publishing and observing focused
values.

`struct FocusedBinding`

A convenience property wrapper for observing and automatically unwrapping
state bindings from the focused view or one of its ancestors.

Instance Method

# focusedValue(_:)

Sets the focused value for the given object type.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func focusedValue<T>(_ object: T?) -> some View where T : AnyObject, T : Observable
    

## Discussion

Important

This initializer only accepts objects conforming to the `Observable` protocol.
For reading environment objects that conform to `ObservableObject`, use
`focusedObject(_:)`, instead.

To read this value, use the `FocusedValue` property wrapper.

## See Also

### Exposing value types to focused views

`func focusedValue<Value>(WritableKeyPath<FocusedValues, Value?>, Value) ->
some View`

Modifies this view by injecting a value that you provide for use by other
views whose state depends on the focused view hierarchy.

`func focusedValue<Value>(WritableKeyPath<FocusedValues, Value?>, Value?) ->
some View`

Creates a new view that exposes the provided value to other views whose state
depends on the focused view hierarchy.

`func focusedSceneValue<T>(WritableKeyPath<FocusedValues, T?>, T?) -> some
View`

Creates a new view that exposes the provided value to other views whose state
depends on the active scene.

`func focusedSceneValue<T>(WritableKeyPath<FocusedValues, T?>, T) -> some
View`

Modifies this view by injecting a value that you provide for use by other
views whose state depends on the focused scene.

`struct FocusedValues`

A collection of state exported by the focused view and its ancestors.

Instance Method

# focusedValue(_:_:)

Modifies this view by injecting a value that you provide for use by other
views whose state depends on the focused view hierarchy.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func focusedValue<Value>(
        _ keyPath: WritableKeyPath<FocusedValues, Value?>,
        _ value: Value
    ) -> some View
    

##  Parameters

`keyPath`

    

The key path to associate `value` with when adding it to the existing table of
exported focus values.

`value`

    

The focus value to export.

## Return Value

A modified representation of this view.

## See Also

### Exposing value types to focused views

`func focusedValue<T>(T?) -> some View`

Sets the focused value for the given object type.

`func focusedValue<Value>(WritableKeyPath<FocusedValues, Value?>, Value?) ->
some View`

Creates a new view that exposes the provided value to other views whose state
depends on the focused view hierarchy.

`func focusedSceneValue<T>(WritableKeyPath<FocusedValues, T?>, T?) -> some
View`

Creates a new view that exposes the provided value to other views whose state
depends on the active scene.

`func focusedSceneValue<T>(WritableKeyPath<FocusedValues, T?>, T) -> some
View`

Modifies this view by injecting a value that you provide for use by other
views whose state depends on the focused scene.

`struct FocusedValues`

A collection of state exported by the focused view and its ancestors.

Instance Method

# focusedValue(_:_:)

Creates a new view that exposes the provided value to other views whose state
depends on the focused view hierarchy.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func focusedValue<Value>(
        _ keyPath: WritableKeyPath<FocusedValues, Value?>,
        _ value: Value?
    ) -> some View
    

##  Parameters

`keyPath`

    

The key path to associate `value` with when adding it to the existing table of
exported focus values.

`value`

    

The focus value to export, or `nil` if no value is currently available.

## Return Value

A modified representation of this view.

## Discussion

Use this method instead of `View/focusedSceneValue(_:_:)` when your scene
includes multiple focusable views with their own associated values, and you
need an app- or scene-scoped element like a command or toolbar item that
operates on the value associated with whichever view currently has focus. Each
focusable view can supply its own value:

## See Also

### Exposing value types to focused views

`func focusedValue<T>(T?) -> some View`

Sets the focused value for the given object type.

`func focusedValue<Value>(WritableKeyPath<FocusedValues, Value?>, Value) ->
some View`

Modifies this view by injecting a value that you provide for use by other
views whose state depends on the focused view hierarchy.

`func focusedSceneValue<T>(WritableKeyPath<FocusedValues, T?>, T?) -> some
View`

Creates a new view that exposes the provided value to other views whose state
depends on the active scene.

`func focusedSceneValue<T>(WritableKeyPath<FocusedValues, T?>, T) -> some
View`

Modifies this view by injecting a value that you provide for use by other
views whose state depends on the focused scene.

`struct FocusedValues`

A collection of state exported by the focused view and its ancestors.

Instance Method

# focusedSceneValue(_:_:)

Creates a new view that exposes the provided value to other views whose state
depends on the active scene.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func focusedSceneValue<T>(
        _ keyPath: WritableKeyPath<FocusedValues, T?>,
        _ value: T?
    ) -> some View
    

##  Parameters

`keyPath`

    

The key path to associate `value` with when adding it to the existing table of
published focus values.

`value`

    

The focus value to publish, or `nil` if no value is currently available.

## Return Value

A modified representation of this view.

## Discussion

Use this method instead of `View/focusedValue(_:_:)` for values that must be
visible regardless of where focus is located in the active scene. For example,
if an app needs a command for moving focus to a particular text field in the
sidebar, it could use this modifier to publish a button action that’s visible
to command views as long as the scene is active, and regardless of where focus
happens to be in it.

## See Also

### Exposing value types to focused views

`func focusedValue<T>(T?) -> some View`

Sets the focused value for the given object type.

`func focusedValue<Value>(WritableKeyPath<FocusedValues, Value?>, Value) ->
some View`

Modifies this view by injecting a value that you provide for use by other
views whose state depends on the focused view hierarchy.

`func focusedValue<Value>(WritableKeyPath<FocusedValues, Value?>, Value?) ->
some View`

Creates a new view that exposes the provided value to other views whose state
depends on the focused view hierarchy.

`func focusedSceneValue<T>(WritableKeyPath<FocusedValues, T?>, T) -> some
View`

Modifies this view by injecting a value that you provide for use by other
views whose state depends on the focused scene.

`struct FocusedValues`

A collection of state exported by the focused view and its ancestors.

Instance Method

# focusedSceneValue(_:_:)

Modifies this view by injecting a value that you provide for use by other
views whose state depends on the focused scene.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func focusedSceneValue<T>(
        _ keyPath: WritableKeyPath<FocusedValues, T?>,
        _ value: T
    ) -> some View
    

##  Parameters

`keyPath`

    

The key path to associate `value` with when adding it to the existing table of
published focus values.

`value`

    

The focus value to publish.

## Return Value

A modified representation of this view.

## Discussion

Use this method instead of `View/focusedValue(_:_:)` for values that must be
visible regardless of where focus is located in the active scene. For example,
if an app needs a command for moving focus to a particular text field in the
sidebar, it could use this modifier to publish a button action that’s visible
to command views as long as the scene is active, and regardless of where focus
happens to be in it.

    
    
    struct Sidebar: View {
        @FocusState var isFiltering: Bool
    
    
        var body: some View {
            VStack {
                TextField(...)
                    .focused(when: $isFiltering)
                    .focusedSceneValue(\.filterAction) {
                        isFiltering = true
                    }
            }
        }
    }
    
    
    struct NavigationCommands: Commands {
        @FocusedValue(\.filterAction) var filterAction
    
    
        var body: some Commands {
            CommandMenu("Navigate") {
                Button("Filter in Sidebar") {
                    filterAction?()
                }
            }
            .disabled(filterAction == nil)
        }
    }
    
    
    struct FilterActionKey: FocusedValuesKey {
        typealias Value = () -> Void
    }
    
    
    extension FocusedValues {
        var filterAction: (() -> Void)? {
            get { self[FilterActionKey.self] }
            set { self[FilterActionKey.self] = newValue }
        }
    }
    

## See Also

### Exposing value types to focused views

`func focusedValue<T>(T?) -> some View`

Sets the focused value for the given object type.

`func focusedValue<Value>(WritableKeyPath<FocusedValues, Value?>, Value) ->
some View`

Modifies this view by injecting a value that you provide for use by other
views whose state depends on the focused view hierarchy.

`func focusedValue<Value>(WritableKeyPath<FocusedValues, Value?>, Value?) ->
some View`

Creates a new view that exposes the provided value to other views whose state
depends on the focused view hierarchy.

`func focusedSceneValue<T>(WritableKeyPath<FocusedValues, T?>, T?) -> some
View`

Creates a new view that exposes the provided value to other views whose state
depends on the active scene.

`struct FocusedValues`

A collection of state exported by the focused view and its ancestors.

Instance Method

# focusedObject(_:)

Creates a new view that exposes the provided object to other views whose state
depends on the focused view hierarchy.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func focusedObject<T>(_ object: T?) -> some View where T : ObservableObject
    

##  Parameters

`object`

    

The observable object to associate with focus, or `nil` if no object is
currently available.

## Return Value

A view that supplies an observable object when in focus.

## Discussion

Use this method instead of `View/focusedSceneObject(_:)` when your scene
includes multiple focusable views with their own associated data, and you need
an app- or scene-scoped element like a command or toolbar item that operates
on the data associated with whichever view currently has focus. Each focusable
view can supply its own object:

Interested views can then use the `FocusedObject` property wrapper to observe
and update the focused view’s object. In this example, an app command updates
the focused view’s data, and is automatically disabled when focus is in an
unrelated part of the scene:

## See Also

### Exposing reference types to focused views

`func focusedObject<T>(T) -> some View`

Creates a new view that exposes the provided object to other views whose whose
state depends on the focused view hierarchy.

`func focusedSceneObject<T>(T?) -> some View`

Creates a new view that exposes the provided object to other views whose whose
state depends on the active scene.

`func focusedSceneObject<T>(T) -> some View`

Creates a new view that exposes the provided object to other views whose whose
state depends on the active scene.

`struct FocusedObject`

A property wrapper type for an observable object supplied by the focused view
or one of its ancestors.

Instance Method

# focusedObject(_:)

Creates a new view that exposes the provided object to other views whose whose
state depends on the focused view hierarchy.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func focusedObject<T>(_ object: T) -> some View where T : ObservableObject
    

##  Parameters

`object`

    

The observable object to associate with focus.

## Return Value

A view that supplies an observable object when in focus.

## Discussion

Use this method instead of `View/focusedSceneObject(_:)` when your scene
includes multiple focusable views with their own associated data, and you need
an app- or scene-scoped element like a command or toolbar item that operates
on the data associated with whichever view currently has focus. Each focusable
view can supply its own object:

Interested views can then use the `FocusedObject` property wrapper to observe
and update the focused view’s object. In this example, an app command updates
the focused view’s data, and is automatically disabled when focus is in an
unrelated part of the scene:

## See Also

### Exposing reference types to focused views

`func focusedObject<T>(T?) -> some View`

Creates a new view that exposes the provided object to other views whose state
depends on the focused view hierarchy.

`func focusedSceneObject<T>(T?) -> some View`

Creates a new view that exposes the provided object to other views whose whose
state depends on the active scene.

`func focusedSceneObject<T>(T) -> some View`

Creates a new view that exposes the provided object to other views whose whose
state depends on the active scene.

`struct FocusedObject`

A property wrapper type for an observable object supplied by the focused view
or one of its ancestors.

Instance Method

# focusedSceneObject(_:)

Creates a new view that exposes the provided object to other views whose whose
state depends on the active scene.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func focusedSceneObject<T>(_ object: T?) -> some View where T : ObservableObject
    

##  Parameters

`object`

    

The observable object to associate with the scene, or `nil` if no object is
currently available.

## Return Value

A view that supplies an observable object while the scene is active.

## Discussion

Use this method instead of `View/focusedObject(_:)` for observable objects
that must be visible regardless of where focus is located in the active scene.
This is sometimes needed for things like main menu and discoverability HUD
commands that observe and update data from the active scene but aren’t
concerned with what the user is actually focused on. The scene’s root view can
supply the scene’s state object:

Interested views can then use the `FocusedObject` property wrapper to observe
and update the active scene’s state object. In this example, an app command
updates the active scene’s data, and is enabled as long as any scene is
active.

## See Also

### Exposing reference types to focused views

`func focusedObject<T>(T?) -> some View`

Creates a new view that exposes the provided object to other views whose state
depends on the focused view hierarchy.

`func focusedObject<T>(T) -> some View`

Creates a new view that exposes the provided object to other views whose whose
state depends on the focused view hierarchy.

`func focusedSceneObject<T>(T) -> some View`

Creates a new view that exposes the provided object to other views whose whose
state depends on the active scene.

`struct FocusedObject`

A property wrapper type for an observable object supplied by the focused view
or one of its ancestors.

Instance Method

# focusedSceneObject(_:)

Creates a new view that exposes the provided object to other views whose whose
state depends on the active scene.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func focusedSceneObject<T>(_ object: T) -> some View where T : ObservableObject
    

##  Parameters

`object`

    

The observable object to associate with the scene.

## Return Value

A view that supplies an observable object while the scene is active.

## Discussion

Use this method instead of `View/focusedObject(_:)` for observable objects
that must be visible regardless of where focus is located in the active scene.
This is sometimes needed for things like main menu and discoverability HUD
commands that observe and update data from the active scene but aren’t
concerned with what the user is actually focused on. The scene’s root view can
supply the scene’s state object:

Interested views can then use the `FocusedObject` property wrapper to observe
and update the active scene’s state object. In this example, an app command
updates the active scene’s data, and is enabled as long as any scene is
active.

## See Also

### Exposing reference types to focused views

`func focusedObject<T>(T?) -> some View`

Creates a new view that exposes the provided object to other views whose state
depends on the focused view hierarchy.

`func focusedObject<T>(T) -> some View`

Creates a new view that exposes the provided object to other views whose whose
state depends on the focused view hierarchy.

`func focusedSceneObject<T>(T?) -> some View`

Creates a new view that exposes the provided object to other views whose whose
state depends on the active scene.

`struct FocusedObject`

A property wrapper type for an observable object supplied by the focused view
or one of its ancestors.

Instance Method

# prefersDefaultFocus(_:in:)

Indicates that the view should receive focus by default for a given namespace.

macOS 12.0+  tvOS 14.0+  watchOS 7.0+

    
    
    func prefersDefaultFocus(
        _ prefersDefaultFocus: Bool = true,
        in namespace: Namespace.ID
    ) -> some View
    

##  Parameters

`prefersDefaultFocus`

    

A Boolean value that indicates whether this view prefers to receive focus by
default. The default value, `true`, causes the view to receive focus by
default.

`namespace`

    

The namespace associated with the focus scope within which this view prefers
default focus.

## Return Value

A modified view that sets whether it prefers to be focused by default.

## Discussion

This modifier sets the initial focus preference when no other view has focus.
Use the environment value `resetFocus` to force a reevaluation of default
focus at any time.

The following tvOS example shows three buttons, labeled “1”, “2”, and “3”, in
a `VStack`. By default, the “1” button would receive focus, because it is the
first child in the stack. However, the `prefersDefaultFocus(_:in:)` modifier
allows button “3” to receive default focus instead. Once the buttons are
visible, the user can move down to and focus the “Reset to default focus”
button. When the user activates this button, it uses the `ResetFocusAction` to
reevaluate default focus in the `mainNamespace`, which returns the focus to
button “3”.

The default focus preference is limited to the focusable ancestor that matches
the provided namespace. If multiple views express this preference, then
SwiftUI applies the current platform rules to determine which view receives
focus.

## See Also

### Controlling default focus

`func defaultFocus<V>(FocusState<V>.Binding, V, priority:
DefaultFocusEvaluationPriority) -> some View`

Defines a region of the window in which default focus is evaluated by
assigning a value to a given focus state binding.

`struct DefaultFocusEvaluationPriority`

Prioritizations for default focus preferences when evaluating where to move
focus in different circumstances.

Instance Method

# focusScope(_:)

Creates a focus scope that SwiftUI uses to limit default focus preferences.

macOS 12.0+  tvOS 14.0+  watchOS 7.0+

    
    
    func focusScope(_ namespace: Namespace.ID) -> some View
    

##  Parameters

`namespace`

    

A namespace identifier that SwiftUI can use to scope default focus
preferences.

## Return Value

A view that sets the namespace of descendants for default focus.

## Discussion

The returned view gets associated with the provided namespace. Pass this
namespace to `prefersDefaultFocus(_:in:)` and the `resetFocus` function.

## See Also

### Setting focus scope

`func focusSection() -> some View`

Indicates that the view’s frame and cohort of focusable descendants should be
used to guide focus movement.

Instance Method

# focusSection()

Indicates that the view’s frame and cohort of focusable descendants should be
used to guide focus movement.

macOS 13.0+  tvOS 15.0+

    
    
    func focusSection() -> some View
    

## Return Value

A view that can guide focus to its focusable descendents.

## Discussion

Use focus sections to customize SwiftUI’s behavior when the user moves focus
between views.

The following tvOS example places three buttons (“1”, “2”, and “3”) at the
upper left of the screen and three buttons (“A”, “B”, and “C”) at the bottom
right. By default, swiping right on the Siri Remote on any of the buttons in
the “1” - “3” group would do nothing, since the focus system finds no
focusable views directly to their right. But by declaring the `VStack` that
encloses buttons “A” - “C” as a focus section, the `VStack` can receive focus,
and deliver that focus to its first focusable child (button “A”). The example
puts a border on the `VStack` to illustrate this spatial arrangement.

Note that because the `VStack` containing buttons “1” - “3” does not declare
itself as a focus section, it is impossible to direct focus back to the left
from buttons “A” - “C”. None of those buttons has a focusable view — in this
case either a button or a `VStack` with the `focusSection()` modifier —
directly to its left.

Applying this modifier to a view affects focus behavior based on the style of
movement:

  * **Directional movement** : Navigating with Siri Remote gestures, arrow keys on a keyboard, or any other type of input that works in terms of cardinal directions (up, down, left, right) produces directional movement. When modified with `focusSection()`, the view’s frame becomes capable of accepting focus in order to direct it at its nearest focusable descendant in the direction of travel. In the earlier example, declaring the right-side `VStack` as a focus section allowed it to receive right-directed focus from the buttons on the left.

  * **Sequential movement** : Navigating with a Digital Crown, the Tab key on a keyboard, or any other type of input that works in terms of the next or previous item in a sequence, produces sequential movement. When you use the `focusSection()` modifier, SwiftUI deviates from its default layout-based sequence to visit each of the modified view’s focusable descendants before resuming the default sequence. Within the set of focusable descendants, SwiftUI continues to visit views in layout order (leading-to-trailing, top-to-bottom).

`focusSection()` does not affect the focusability of the modified view. If the
modified view has no focusable descendants, then the modifier does nothing.

## See Also

### Setting focus scope

`func focusScope(Namespace.ID) -> some View`

Creates a focus scope that SwiftUI uses to limit default focus preferences.

Instance Method

# focusable(_:)

Specifies if the view is focusable.

iOS 17.0+  iPadOS 17.0+  macOS 12.0+  Mac Catalyst 17.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func focusable(_ isFocusable: Bool = true) -> some View
    

##  Parameters

`isFocusable`

    

A Boolean value that indicates whether this view is focusable.

## Return Value

A view that sets whether a view is focusable.

## See Also

### Indicating that a view can receive focus

`func focusable(Bool, interactions: FocusInteractions) -> some View`

Specifies if the view is focusable, and if so, what focus-driven interactions
it supports.

`struct FocusInteractions`

Values describe different focus interactions that a view can support.

Instance Method

# focusable(_:interactions:)

Specifies if the view is focusable, and if so, what focus-driven interactions
it supports.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func focusable(
        _ isFocusable: Bool = true,
        interactions: FocusInteractions
    ) -> some View
    

##  Parameters

`isFocusable`

    

`true` if the view should participate in focus; `false` otherwise. The default
value is `true`.

`interactions`

    

The types of focus interactions supported by the view. The default value is
`.automatic`.

## Return Value

A view that sets whether its child is focusable.

## Discussion

By default, SwiftUI enables all possible focus interactions. However, on macOS
and iOS it is conventional for button-like views to only accept focus when the
user has enabled keyboard navigation system-wide in the Settings app. Clients
can reproduce this behavior with custom views by only supporting `.activate`
interactions.

Note

The focus interactions allowed for custom views changed in macOS
14—previously, custom views could only become focused with keyboard navigation
enabled system-wide. Clients built using older SDKs will continue to see the
older focus behavior, while custom views in clients built using macOS 14 or
later will always be focusable unless the client requests otherwise by
specifying a restricted set of focus interactions.

## See Also

### Indicating that a view can receive focus

`func focusable(Bool) -> some View`

Specifies if the view is focusable.

`struct FocusInteractions`

Values describe different focus interactions that a view can support.

Instance Method

# focusEffectDisabled(_:)

Adds a condition that controls whether this view can display focus effects,
such as a default focus ring or hover effect.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func focusEffectDisabled(_ disabled: Bool = true) -> some View
    

##  Parameters

`disabled`

    

A Boolean value that determines whether this view can display focus effects.

## Return Value

A view that controls whether focus effects can be displayed in this view.

## Discussion

The higher views in a view hierarchy can override the value you set on this
view. In the following example, the button does not display a focus effect
because the outer `focusEffectDisabled(_:)` modifier overrides the inner one:

## See Also

### Configuring effects

`var isFocusEffectEnabled: Bool`

A Boolean value that indicates whether the view associated with this
environment allows focus effects to be displayed.

Instance Method

# defaultFocus(_:_:priority:)

Defines a region of the window in which default focus is evaluated by
assigning a value to a given focus state binding.

iOS 17.0+  iPadOS 17.0+  macOS 13.0+  Mac Catalyst 17.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func defaultFocus<V>(
        _ binding: FocusState<V>.Binding,
        _ value: V,
        priority: DefaultFocusEvaluationPriority = .automatic
    ) -> some View where V : Hashable
    

##  Parameters

`binding`

    

A focus state binding to update when evaluating default focus in the modified
view hierarchy.

`value`

    

The value to set the binding to during evaluation.

`priority`

    

An indication of how to prioritize the preferred default focus target when
focus moves into the modified view hierarchy. The default value is
`automatic`, which means the preference will be given priority when focus is
being initialized or relocated programmatically, but not when responding to
user-directed navigation commands.

## Return Value

The modified view.

## Discussion

By default, SwiftUI evaluates default focus when the window first appears, and
when a focus state binding update moves focus automatically, but not when
responding to user-driven navigation commands.

Clients can override the default behavior by specifying an evaluation priority
of `userInitiated`, which causes SwiftUI to use the client’s preferred default
focus in response to user-driven focus navigation as well as automatic
changes.

In the following example, focus automatically goes to the second of the two
text fields when the view is first presented in the window.

## See Also

### Controlling default focus

`func prefersDefaultFocus(Bool, in: Namespace.ID) -> some View`

Indicates that the view should receive focus by default for a given namespace.

`struct DefaultFocusEvaluationPriority`

Prioritizations for default focus preferences when evaluating where to move
focus in different circumstances.

Instance Method

# copyable(_:)

Specifies a list of items to copy in response to the system’s Copy command.

macOS 13.0+

    
    
    func copyable<T>(_ payload: @autoclosure @escaping () -> [T]) -> some View where T : Transferable
    

##  Parameters

`payload`

    

A closure that returns an array of items to copy to the Clipboard when someone
issues a Copy command. The items in the array must conform to the
`Transferable` protocol.

## Return Value

A view that adds one or more items to the Clipboard in response to a Copy
command.

## Discussion

Use this modifier to specify one or more items that the system copies to the
Clipboard when someone issues a Copy command while the modified view has
focus. People issue a Copy command by choosing Edit > Copy from the app’s
menu, or by using the Command-C keyboard shortcut. The system enables the Copy
command for your app when it detects copyable content.

For example, the following code enables people to copy all of the strings that
they select in a `List`:

The command copies each item’s representation as specified by the item’s
conformance to the `Transferable` protocol. The above example records
selection using each list item’s corresponding string, and strings conform to
the `Transferable` protocol by default. For more complex cases, you might need
to take additional steps.

For example, the following code displays colors composed from a list of `Item`
instances that contain both a color and its name, as well as an identifier.
The list manages selection using item identifiers:

This example does two things that the previous example didn’t have to:

  * It converts the list of selected item identifiers into a list of selected items for use with the copyable modifier.

  * It ensures that the copyable items conform to the `Transferable` protocol, using the item’s `name` property as the representation.

When someone copies the first item in the list, which appears in the interface
as a red rectangle, and then pastes into a text editor, they get the string
“red”.

Note

To enable people to copy using a custom action — like from a context menu item
— rather than using the system Copy command, update the Clipboard directly
using an `NSPasteboard` or a `UIPasteboard` instance.

## See Also

### Copying transferable items

`func cuttable<T>(for: T.Type, action: () -> [T]) -> some View`

Specifies an action that moves items to the Clipboard in response to the
system’s Cut command.

`func pasteDestination<T>(for: T.Type, action: ([T]) -> Void, validator: ([T])
-> [T]) -> some View`

Specifies an action that adds validated items to a view in response to the
system’s Paste command.

Instance Method

# cuttable(for:action:)

Specifies an action that moves items to the Clipboard in response to the
system’s Cut command.

macOS 13.0+

    
    
    func cuttable<T>(
        for payloadType: T.Type = T.self,
        action: @escaping () -> [T]
    ) -> some View where T : Transferable
    

##  Parameters

`payloadType`

    

The type of items to cut.

`action`

    

A closure that you implement to delete the selected items from the collection,
and return them for addition to the Clipboard. The items must conform to the
`Transferable` protocol.

## Return Value

A view that sends one or more items to the Clipboard in response to a Cut
command.

## Discussion

Use this modifier to remove one or more items from a collection of items and
then move the items to the Clipboard when someone issues a Cut command. People
issue a Cut command by choosing Edit > Cut from the app’s menu, or by using
the Command-X keyboard shortcut. The system enables the Cut command for your
app when it detects cuttable content.

For example, the following code enables people to remove bird names from a
list of birds:

When someone selects “owl” and issues a Cut command, the `action` closure
removes the selected item from the list and returns it. In response, SwiftUI
moves it to the Clipboard. If you want to copy the item without removing it,
use the `copyable(_:)` modifier instead.

Note

To enable people to cut using a custom action — like from a context menu item
— rather than using the system Cut command, update the Clipboard directly
using an `NSPasteboard` or a `UIPasteboard` instance.

## See Also

### Copying transferable items

`func copyable<T>(() -> [T]) -> some View`

Specifies a list of items to copy in response to the system’s Copy command.

`func pasteDestination<T>(for: T.Type, action: ([T]) -> Void, validator: ([T])
-> [T]) -> some View`

Specifies an action that adds validated items to a view in response to the
system’s Paste command.

Instance Method

# pasteDestination(for:action:validator:)

Specifies an action that adds validated items to a view in response to the
system’s Paste command.

macOS 13.0+

    
    
    func pasteDestination<T>(
        for payloadType: T.Type = T.self,
        action: @escaping ([T]) -> Void,
        validator: @escaping ([T]) -> [T] = { $0 }
    ) -> some View where T : Transferable
    

##  Parameters

`payloadType`

    

The type of data that the paste destination accepts. The type must conform to
the `Transferable` protocol.

`action`

    

The action to perform when someone uses the system’s Paste command to paste
one or more items of the payload type. The closure takes one parameter, which
is the array of items to paste.

`validator`

    

A closure that you implement to validate the data to paste. SwiftUI calls this
before it calls the `action` closure, and passes in an array of items to
validate. Inspect the items, and return an array that includes only those from
the input array that you consider valid. The array that you return from this
closure becomes the input to the `action` closure. If you return an empty
array, SwiftUI doesn’t call the `action` closure.

## Return Value

A view that people can paste into using the system Paste command.

## Discussion

Use this modifier to paste one or more items into a view from the Clipboard
when someone issues a Paste command. People issue a Paste command by choosing
Edit > Paste from the app’s menu, or by using the Command-V keyboard shortcut.
The system enables the Paste command for your app when the view in focus
provides a paste destination.

For example, the following code enables people to paste bird names into a
list:

The paste destination handles only pasted content with a type that matches the
`payloadType` that you specify. The list in the above example only accepts
strings.

Use the `validator` closure to restrict the pasted content to items that make
sense in the context of the view. The above example allows people to paste
only strings that match one of a known list of bird names because the list is
meant to contain only birds. You can omit the final closure if you don’t need
to perform any validation.

Note

To enable people to paste using a custom action — like from a context menu
item — rather than using the system Paste command, access the Clipboard
directly using an `NSPasteboard` or a `UIPasteboard` instance.

## See Also

### Copying transferable items

`func copyable<T>(() -> [T]) -> some View`

Specifies a list of items to copy in response to the system’s Copy command.

`func cuttable<T>(for: T.Type, action: () -> [T]) -> some View`

Specifies an action that moves items to the Clipboard in response to the
system’s Cut command.

Instance Method

# onCopyCommand(perform:)

Adds an action to perform in response to the system’s Copy command.

macOS 10.15+

    
    
    func onCopyCommand(perform payloadAction: (() -> [NSItemProvider])?) -> some View
    

##  Parameters

`payloadAction`

    

An action closure returning the `NSItemProvider` items that should be copied
to the Clipboard when the Copy command is triggered. If `action` is `nil`, the
Copy command is considered disabled.

## Return Value

A view that triggers `action` when a system Copy command occurs.

## See Also

### Copying items using item providers

`func onCutCommand(perform: (() -> [NSItemProvider])?) -> some View`

Adds an action to perform in response to the system’s Cut command.

`func onPasteCommand(of: [UTType], perform: ([NSItemProvider]) -> Void) ->
some View`

Adds an action to perform in response to the system’s Paste command.

`func onPasteCommand<Payload>(of: [UTType], validator: ([NSItemProvider]) ->
Payload?, perform: (Payload) -> Void) -> some View`

Adds an action to perform in response to the system’s Paste command with items
that you validate.

Instance Method

# onCutCommand(perform:)

Adds an action to perform in response to the system’s Cut command.

macOS 10.15+

    
    
    func onCutCommand(perform payloadAction: (() -> [NSItemProvider])?) -> some View
    

##  Parameters

`payloadAction`

    

An action closure that should delete the selected data and return
`NSItemProvider` items corresponding to that data, which should be written to
the Clipboard. If `action` is `nil`, the Cut command is considered disabled.

## Return Value

A view that triggers `action` when a system Cut command occurs.

## See Also

### Copying items using item providers

`func onCopyCommand(perform: (() -> [NSItemProvider])?) -> some View`

Adds an action to perform in response to the system’s Copy command.

`func onPasteCommand(of: [UTType], perform: ([NSItemProvider]) -> Void) ->
some View`

Adds an action to perform in response to the system’s Paste command.

`func onPasteCommand<Payload>(of: [UTType], validator: ([NSItemProvider]) ->
Payload?, perform: (Payload) -> Void) -> some View`

Adds an action to perform in response to the system’s Paste command with items
that you validate.

Instance Method

# onPasteCommand(of:perform:)

Adds an action to perform in response to the system’s Paste command.

macOS 11.0+

    
    
    func onPasteCommand(
        of supportedContentTypes: [UTType],
        perform payloadAction: @escaping ([NSItemProvider]) -> Void
    ) -> some View
    

##  Parameters

`supportedContentTypes`

    

The uniform type identifiers that describe the types of content this view can
accept through a paste action. If the Clipboard doesn’t contain any of the
supported types, the Paste command doesn’t trigger.

`payloadAction`

    

The action to perform when the Paste command triggers. The action closure’s
parameter contains items from the Clipboard with the types you specify in the
`supportedContentTypes` parameter.

## Return Value

A view that triggers `action` when a system Paste command occurs.

## Discussion

Pass an array of uniform type identifiers to the `supportedContentTypes`
parameter. Place the higher priority types closer to the beginning of the
array. The Clipboard items that the `action` closure receives have the most
preferred type out of all the types the source supports.

For example, if your app can handle plain text and rich text, but you prefer
rich text, place the rich text type first in the array. If rich text is
available when the paste action occurs, the `action` closure passes that rich
text along.

## See Also

### Copying items using item providers

`func onCopyCommand(perform: (() -> [NSItemProvider])?) -> some View`

Adds an action to perform in response to the system’s Copy command.

`func onCutCommand(perform: (() -> [NSItemProvider])?) -> some View`

Adds an action to perform in response to the system’s Cut command.

`func onPasteCommand<Payload>(of: [UTType], validator: ([NSItemProvider]) ->
Payload?, perform: (Payload) -> Void) -> some View`

Adds an action to perform in response to the system’s Paste command with items
that you validate.

Instance Method

# onPasteCommand(of:validator:perform:)

Adds an action to perform in response to the system’s Paste command with items
that you validate.

macOS 11.0+

    
    
    func onPasteCommand<Payload>(
        of supportedContentTypes: [UTType],
        validator: @escaping ([NSItemProvider]) -> Payload?,
        perform payloadAction: @escaping (Payload) -> Void
    ) -> some View
    

##  Parameters

`supportedContentTypes`

    

The uniform type identifiers that describe the types of content this view can
accept through a paste action. If the Clipboard doesn’t contain any of the
supported types, the Paste command doesn’t trigger.

`validator`

    

A handler that validates the command. This handler receives items from the
Clipboard with the types you specify in the `supportedContentTypes`. Use this
handler to decide whether the items are valid and preprocess them for the
`action` closure. If you return `nil` instead, the Paste command doesn’t
trigger.

`payloadAction`

    

The action to perform when the Paste command triggers.

## Return Value

A view that triggers `action` when the system Paste command is invoked,
validating the Paste command with `validator`.

## Discussion

Pass an array of uniform type identifiers to the `supportedContentTypes`
parameter. Place the higher priority types closer to the beginning of the
array. The Clipboard items that the `validator` closure receives have the most
preferred type out of all the types the source supports.

For example, if your app can handle plain text and rich text, but you prefer
rich text, place the rich text type first in the array. If rich text is
available when the paste action occurs, the `validator` closure passes that
rich text along.

## See Also

### Copying items using item providers

`func onCopyCommand(perform: (() -> [NSItemProvider])?) -> some View`

Adds an action to perform in response to the system’s Copy command.

`func onCutCommand(perform: (() -> [NSItemProvider])?) -> some View`

Adds an action to perform in response to the system’s Cut command.

`func onPasteCommand(of: [UTType], perform: ([NSItemProvider]) -> Void) ->
some View`

Adds an action to perform in response to the system’s Paste command.

Instance Method

# onDrag(_:preview:)

Activates this view as the source of a drag and drop operation.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    func onDrag<V>(
        _ data: @escaping () -> NSItemProvider,
        @ViewBuilder preview: () -> V
    ) -> some View where V : View
    

##  Parameters

`data`

    

A closure that returns a single `NSItemProvider` that represents the draggable
data from this view.

`preview`

    

A `View` to use as the source for the dragging preview, once the drag
operation has begun. The preview is centered over the source view.

## Return Value

A view that activates this view as the source of a drag-and- drop operation,
beginning with user gesture input.

## Discussion

Applying the `onDrag(_:preview:)` modifier adds the appropriate gestures for
drag and drop to this view. When a drag operation begins, a rendering of
`preview` is generated and used as the preview image.

## See Also

### Moving items using item providers

`func itemProvider(Optional<() -> NSItemProvider?>) -> some View`

Provides a closure that vends the drag representation to be used for a
particular data element.

`func onDrag(() -> NSItemProvider) -> some View`

Activates this view as the source of a drag and drop operation.

`func onDrop(of: [UTType], isTargeted: Binding<Bool>?, perform:
([NSItemProvider]) -> Bool) -> some View`

Defines the destination of a drag-and-drop operation that handles the dropped
content with a closure that you specify.

`func onDrop(of: [UTType], isTargeted: Binding<Bool>?, perform:
([NSItemProvider], CGPoint) -> Bool) -> some View`

Defines the destination of a drag and drop operation that handles the dropped
content with a closure that you specify.

`func onDrop(of: [UTType], delegate: any DropDelegate) -> some View`

Defines the destination of a drag and drop operation using behavior controlled
by the delegate that you provide.

`protocol DropDelegate`

An interface that you implement to interact with a drop operation in a view
modified to accept drops.

`struct DropProposal`

The behavior of a drop.

`enum DropOperation`

Operation types that determine how a drag and drop session resolves when the
user drops a drag item.

`struct DropInfo`

The current state of a drop.

Instance Method

# onDrag(_:)

Activates this view as the source of a drag and drop operation.

iOS 13.4+  iPadOS 13.4+  macOS 10.15+  Mac Catalyst 13.4+  visionOS 1.0+

    
    
    func onDrag(_ data: @escaping () -> NSItemProvider) -> some View
    

##  Parameters

`data`

    

A closure that returns a single `NSItemProvider` that represents the draggable
data from this view.

## Return Value

A view that activates this view as the source of a drag and drop operation,
beginning with user gesture input.

## Discussion

Applying the `onDrag(_:)` modifier adds the appropriate gestures for drag and
drop to this view. When a drag operation begins, a rendering of this view is
generated and used as the preview image.

## See Also

### Moving items using item providers

`func itemProvider(Optional<() -> NSItemProvider?>) -> some View`

Provides a closure that vends the drag representation to be used for a
particular data element.

`func onDrag<V>(() -> NSItemProvider, preview: () -> V) -> some View`

Activates this view as the source of a drag and drop operation.

`func onDrop(of: [UTType], isTargeted: Binding<Bool>?, perform:
([NSItemProvider]) -> Bool) -> some View`

Defines the destination of a drag-and-drop operation that handles the dropped
content with a closure that you specify.

`func onDrop(of: [UTType], isTargeted: Binding<Bool>?, perform:
([NSItemProvider], CGPoint) -> Bool) -> some View`

Defines the destination of a drag and drop operation that handles the dropped
content with a closure that you specify.

`func onDrop(of: [UTType], delegate: any DropDelegate) -> some View`

Defines the destination of a drag and drop operation using behavior controlled
by the delegate that you provide.

`protocol DropDelegate`

An interface that you implement to interact with a drop operation in a view
modified to accept drops.

`struct DropProposal`

The behavior of a drop.

`enum DropOperation`

Operation types that determine how a drag and drop session resolves when the
user drops a drag item.

`struct DropInfo`

The current state of a drop.

Instance Method

# itemProvider(_:)

Provides a closure that vends the drag representation to be used for a
particular data element.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func itemProvider(_ action: Optional<() -> NSItemProvider?>) -> some View
    

## See Also

### Moving items using item providers

`func onDrag<V>(() -> NSItemProvider, preview: () -> V) -> some View`

Activates this view as the source of a drag and drop operation.

`func onDrag(() -> NSItemProvider) -> some View`

Activates this view as the source of a drag and drop operation.

`func onDrop(of: [UTType], isTargeted: Binding<Bool>?, perform:
([NSItemProvider]) -> Bool) -> some View`

Defines the destination of a drag-and-drop operation that handles the dropped
content with a closure that you specify.

`func onDrop(of: [UTType], isTargeted: Binding<Bool>?, perform:
([NSItemProvider], CGPoint) -> Bool) -> some View`

Defines the destination of a drag and drop operation that handles the dropped
content with a closure that you specify.

`func onDrop(of: [UTType], delegate: any DropDelegate) -> some View`

Defines the destination of a drag and drop operation using behavior controlled
by the delegate that you provide.

`protocol DropDelegate`

An interface that you implement to interact with a drop operation in a view
modified to accept drops.

`struct DropProposal`

The behavior of a drop.

`enum DropOperation`

Operation types that determine how a drag and drop session resolves when the
user drops a drag item.

`struct DropInfo`

The current state of a drop.

Instance Method

# onDrop(of:isTargeted:perform:)

Defines the destination of a drag-and-drop operation that handles the dropped
content with a closure that you specify.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    func onDrop(
        of supportedContentTypes: [UTType],
        isTargeted: Binding<Bool>?,
        perform action: @escaping ([NSItemProvider]) -> Bool
    ) -> some View
    

##  Parameters

`supportedContentTypes`

    

The uniform type identifiers that describe the types of content this view can
accept through drag and drop. If the drag-and-drop operation doesn’t contain
any of the supported types, then this drop destination doesn’t activate and
`isTargeted` doesn’t update.

`isTargeted`

    

A binding that updates when a drag and drop operation enters or exits the drop
target area. The binding’s value is `true` when the cursor is inside the area,
and `false` when the cursor is outside.

`action`

    

A closure that takes the dropped content and responds appropriately. The
parameter to `action` contains the dropped items, with types specified by
`supportedContentTypes`. Return `true` if the drop operation was successful;
otherwise, return `false`.

## Return Value

A view that provides a drop destination for a drag operation of the specified
types.

## Discussion

The drop destination is the same size and position as this view.

## See Also

### Moving items using item providers

`func itemProvider(Optional<() -> NSItemProvider?>) -> some View`

Provides a closure that vends the drag representation to be used for a
particular data element.

`func onDrag<V>(() -> NSItemProvider, preview: () -> V) -> some View`

Activates this view as the source of a drag and drop operation.

`func onDrag(() -> NSItemProvider) -> some View`

Activates this view as the source of a drag and drop operation.

`func onDrop(of: [UTType], isTargeted: Binding<Bool>?, perform:
([NSItemProvider], CGPoint) -> Bool) -> some View`

Defines the destination of a drag and drop operation that handles the dropped
content with a closure that you specify.

`func onDrop(of: [UTType], delegate: any DropDelegate) -> some View`

Defines the destination of a drag and drop operation using behavior controlled
by the delegate that you provide.

`protocol DropDelegate`

An interface that you implement to interact with a drop operation in a view
modified to accept drops.

`struct DropProposal`

The behavior of a drop.

`enum DropOperation`

Operation types that determine how a drag and drop session resolves when the
user drops a drag item.

`struct DropInfo`

The current state of a drop.

Instance Method

# onDrop(of:isTargeted:perform:)

Defines the destination of a drag and drop operation that handles the dropped
content with a closure that you specify.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    func onDrop(
        of supportedContentTypes: [UTType],
        isTargeted: Binding<Bool>?,
        perform action: @escaping ([NSItemProvider], CGPoint) -> Bool
    ) -> some View
    

##  Parameters

`supportedContentTypes`

    

The uniform type identifiers that describe the types of content this view can
accept through drag and drop. If the drag and drop operation doesn’t contain
any of the supported types, then this drop destination doesn’t activate and
`isTargeted` doesn’t update.

`isTargeted`

    

A binding that updates when a drag and drop operation enters or exits the drop
target area. The binding’s value is `true` when the cursor is inside the area,
and `false` when the cursor is outside.

`action`

    

A closure that takes the dropped content and responds appropriately. The first
parameter to `action` contains the dropped items, with types specified by
`supportedContentTypes`. The second parameter contains the drop location in
this view’s coordinate space. Return `true` if the drop operation was
successful; otherwise, return `false`.

## Return Value

A view that provides a drop destination for a drag operation of the specified
types.

## Discussion

The drop destination is the same size and position as this view.

## See Also

### Moving items using item providers

`func itemProvider(Optional<() -> NSItemProvider?>) -> some View`

Provides a closure that vends the drag representation to be used for a
particular data element.

`func onDrag<V>(() -> NSItemProvider, preview: () -> V) -> some View`

Activates this view as the source of a drag and drop operation.

`func onDrag(() -> NSItemProvider) -> some View`

Activates this view as the source of a drag and drop operation.

`func onDrop(of: [UTType], isTargeted: Binding<Bool>?, perform:
([NSItemProvider]) -> Bool) -> some View`

Defines the destination of a drag-and-drop operation that handles the dropped
content with a closure that you specify.

`func onDrop(of: [UTType], delegate: any DropDelegate) -> some View`

Defines the destination of a drag and drop operation using behavior controlled
by the delegate that you provide.

`protocol DropDelegate`

An interface that you implement to interact with a drop operation in a view
modified to accept drops.

`struct DropProposal`

The behavior of a drop.

`enum DropOperation`

Operation types that determine how a drag and drop session resolves when the
user drops a drag item.

`struct DropInfo`

The current state of a drop.

Instance Method

# onDrop(of:delegate:)

Defines the destination of a drag and drop operation using behavior controlled
by the delegate that you provide.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    func onDrop(
        of supportedContentTypes: [UTType],
        delegate: any DropDelegate
    ) -> some View
    

##  Parameters

`supportedContentTypes`

    

The uniform type identifiers that describe the types of content this view can
accept through drag and drop. If the drag and drop operation doesn’t contain
any of the supported types, then this drop destination doesn’t activate and
`isTargeted` doesn’t update.

`delegate`

    

A type that conforms to the `DropDelegate` protocol. You have comprehensive
control over drop behavior when you use a delegate.

## Return Value

A view that provides a drop destination for a drag operation of the specified
types.

## Discussion

The drop destination is the same size and position as this view.

## See Also

### Moving items using item providers

`func itemProvider(Optional<() -> NSItemProvider?>) -> some View`

Provides a closure that vends the drag representation to be used for a
particular data element.

`func onDrag<V>(() -> NSItemProvider, preview: () -> V) -> some View`

Activates this view as the source of a drag and drop operation.

`func onDrag(() -> NSItemProvider) -> some View`

Activates this view as the source of a drag and drop operation.

`func onDrop(of: [UTType], isTargeted: Binding<Bool>?, perform:
([NSItemProvider]) -> Bool) -> some View`

Defines the destination of a drag-and-drop operation that handles the dropped
content with a closure that you specify.

`func onDrop(of: [UTType], isTargeted: Binding<Bool>?, perform:
([NSItemProvider], CGPoint) -> Bool) -> some View`

Defines the destination of a drag and drop operation that handles the dropped
content with a closure that you specify.

`protocol DropDelegate`

An interface that you implement to interact with a drop operation in a view
modified to accept drops.

`struct DropProposal`

The behavior of a drop.

`enum DropOperation`

Operation types that determine how a drag and drop session resolves when the
user drops a drag item.

`struct DropInfo`

The current state of a drop.

Instance Method

# dropDestination(for:action:isTargeted:)

Defines the destination of a drag and drop operation that handles the dropped
content with a closure that you specify.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    func dropDestination<T>(
        for payloadType: T.Type = T.self,
        action: @escaping ([T], CGPoint) -> Bool,
        isTargeted: @escaping (Bool) -> Void = { _ in }
    ) -> some View where T : Transferable
    

##  Parameters

`payloadType`

    

The expected type of the dropped models.

`action`

    

A closure that takes the dropped content and responds appropriately. The first
parameter to `action` contains the dropped items. The second parameter
contains the drop location in this view’s coordinate space. Return `true` if
the drop operation was successful; otherwise, return `false`.

`isTargeted`

    

A closure that is called when a drag and drop operation enters or exits the
drop target area. The received value is `true` when the cursor is inside the
area, and `false` when the cursor is outside.

## Return Value

A view that provides a drop destination for a drag operation of the specified
type.

## Discussion

The dropped content can be provided as binary data, file URLs, or file
promises.

The drop destination is the same size and position as this view.

## See Also

### Moving transferable items

`func draggable<T>(() -> T) -> some View`

Activates this view as the source of a drag and drop operation.

`func draggable<V, T>(() -> T, preview: () -> V) -> some View`

Activates this view as the source of a drag and drop operation.

Instance Method

# draggable(_:)

Activates this view as the source of a drag and drop operation.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    func draggable<T>(_ payload: @autoclosure @escaping () -> T) -> some View where T : Transferable
    

##  Parameters

`payload`

    

A closure that returns a single instance or a value conforming to
`Transferable` that represents the draggable data from this view.

## Return Value

A view that activates this view as the source of a drag and drop operation,
beginning with user gesture input.

## Discussion

Applying the `draggable(_:)` modifier adds the appropriate gestures for drag
and drop to this view. When a drag operation begins, a rendering of this view
is generated and used as the preview image.

## See Also

### Moving transferable items

`func draggable<V, T>(() -> T, preview: () -> V) -> some View`

Activates this view as the source of a drag and drop operation.

`func dropDestination<T>(for: T.Type, action: ([T], CGPoint) -> Bool,
isTargeted: (Bool) -> Void) -> some View`

Defines the destination of a drag and drop operation that handles the dropped
content with a closure that you specify.

Instance Method

# draggable(_:preview:)

Activates this view as the source of a drag and drop operation.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    func draggable<V, T>(
        _ payload: @autoclosure @escaping () -> T,
        @ViewBuilder preview: () -> V
    ) -> some View where V : View, T : Transferable
    

##  Parameters

`payload`

    

A closure that returns a single class instance or a value conforming to
`Transferable` that represents the draggable data from this view.

`preview`

    

A `View` to use as the source for the dragging preview, once the drag
operation has begun. The preview is centered over the source view.

## Return Value

A view that activates this view as the source of a drag and drop operation,
beginning with user gesture input.

## Discussion

Applying the `draggable(_:preview:)` modifier adds the appropriate gestures
for drag and drop to this view. When a drag operation begins, a rendering of
`preview` is generated and used as the preview image.

## See Also

### Moving transferable items

`func draggable<T>(() -> T) -> some View`

Activates this view as the source of a drag and drop operation.

`func dropDestination<T>(for: T.Type, action: ([T], CGPoint) -> Bool,
isTargeted: (Bool) -> Void) -> some View`

Defines the destination of a drag and drop operation that handles the dropped
content with a closure that you specify.

Instance Method

# springLoadingBehavior(_:)

Sets the spring loading behavior this view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func springLoadingBehavior(_ behavior: SpringLoadingBehavior) -> some View
    

##  Parameters

`behavior`

    

Whether spring loading is enabled or not. If unspecified, the default behavior
is `.automatic.`

## Discussion

Spring loading refers to a view being activated during a drag and drop
interaction. On iOS this can occur when pausing briefly on top of a view with
dragged content. On macOS this can occur with similar brief pauses or on
pressure-sensitive systems by “force clicking” during the drag. This has no
effect on tvOS or watchOS.

This is commonly used with views that have a navigation or presentation
effect, allowing the destination to be revealed without pausing the drag
interaction. For example, a button that reveals a list of folders that a
dragged item can be dropped onto.

Unlike `disabled(_:)`, this modifier overrides the value set by an ancestor
view rather than being unioned with it. For example, the below button would
allow spring loading:

## See Also

### Configuring spring loading

`var springLoadingBehavior: SpringLoadingBehavior`

The behavior of spring loaded interactions for the views associated with this
environment.

`struct SpringLoadingBehavior`

The options for controlling the spring loading behavior of views.

Instance Method

# onSubmit(of:_:)

Adds an action to perform when the user submits a value to this view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func onSubmit(
        of triggers: SubmitTriggers = .text,
        _ action: @escaping (() -> Void)
    ) -> some View
    

##  Parameters

`triggers`

    

The triggers that should invoke the provided action.

`action`

    

The action to perform on submission of a value.

## Discussion

Different views may have different triggers for the provided action. A
`TextField`, or `SecureField` will trigger this action when the user hits the
hardware or software return key. This modifier may also bind this action to a
default action keyboard shortcut. You may set this action on an individual
view or an entire view hierarchy.

You can use the `submitScope(_:)` modifier to stop a submit trigger from a
control from propagating higher up in the view hierarchy to higher
`View.onSubmit(of:_:)` modifiers.

You can use different submit triggers to filter the types of triggers that
should invoke the provided submission action. For example, you may provide a
value of `search` to only hear submission triggers that originate from search
fields vended by searchable modifiers.

## See Also

### Responding to submission events

`func submitScope(Bool) -> some View`

Prevents submission triggers originating from this view to invoke a submission
action configured by a submission modifier higher up in the view hierarchy.

`struct SubmitTriggers`

A type that defines various triggers that result in the firing of a submission
action.

Instance Method

# submitScope(_:)

Prevents submission triggers originating from this view to invoke a submission
action configured by a submission modifier higher up in the view hierarchy.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func submitScope(_ isBlocking: Bool = true) -> some View
    

##  Parameters

`isBlocking`

    

A Boolean that indicates whether this scope is actively blocking submission
triggers from reaching higher submission actions.

## Discussion

Use this modifier when you want to avoid specific views from initiating a
submission action configured by the `onSubmit(of:_:)` modifier. In the example
below, the tag field doesn’t trigger the submission of the form:

## See Also

### Responding to submission events

`func onSubmit(of: SubmitTriggers, (() -> Void)) -> some View`

Adds an action to perform when the user submits a value to this view.

`struct SubmitTriggers`

A type that defines various triggers that result in the firing of a submission
action.

Instance Method

# submitLabel(_:)

Sets the submit label for this view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func submitLabel(_ submitLabel: SubmitLabel) -> some View
    

##  Parameters

`submitLabel`

    

One of the cases specified in `SubmitLabel`.

## Discussion

## See Also

### Labeling a submission event

`struct SubmitLabel`

A semantic label describing the label of submission within a view hierarchy.

Instance Method

# onMoveCommand(perform:)

Adds an action to perform in response to a move command, like when the user
presses an arrow key on a Mac keyboard, or taps the edge of the Siri Remote
when controlling an Apple TV.

macOS 10.15+  tvOS 13.0+

    
    
    func onMoveCommand(perform action: ((MoveCommandDirection) -> Void)?) -> some View
    

## See Also

### Responding to commands

`func onDeleteCommand(perform: (() -> Void)?) -> some View`

Adds an action to perform in response to the system’s Delete command, or
pressing either the ⌫ (backspace) or ⌦ (forward delete) keys while the view
has focus.

`func pageCommand<V>(value: Binding<V>, in: ClosedRange<V>, step: V) -> some
View`

Steps a value through a range in response to page up or page down commands.

`func onExitCommand(perform: (() -> Void)?) -> some View`

Sets up an action that triggers in response to receiving the exit command
while the view has focus.

`func onPlayPauseCommand(perform: (() -> Void)?) -> some View`

Adds an action to perform in response to the system’s Play/Pause command.

`func onCommand(Selector, perform: (() -> Void)?) -> some View`

Adds an action to perform in response to the given selector.

`enum MoveCommandDirection`

Specifies the direction of an arrow key movement.

Instance Method

# moveDisabled(_:)

Adds a condition for whether the view’s view hierarchy is movable.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func moveDisabled(_ isDisabled: Bool) -> some View
    

## See Also

### Editing a list

`func deleteDisabled(Bool) -> some View`

Adds a condition for whether the view’s view hierarchy is deletable.

`var editMode: Binding<EditMode>?`

An indication of whether the user can edit the contents of a view associated
with this environment.

`enum EditMode`

A mode that indicates whether the user can edit a view’s content.

`struct EditActions`

A set of edit actions on a collection of data that a view can offer to a user.

`struct EditableCollectionContent`

An opaque wrapper view that adds editing capabilities to a row in a list.

`struct IndexedIdentifierCollection`

A collection wrapper that iterates over the indices and identifiers of a
collection together.

Instance Method

# onDeleteCommand(perform:)

Adds an action to perform in response to the system’s Delete command, or
pressing either the ⌫ (backspace) or ⌦ (forward delete) keys while the view
has focus.

macOS 10.15+

    
    
    func onDeleteCommand(perform action: (() -> Void)?) -> some View
    

## See Also

### Responding to commands

`func onMoveCommand(perform: ((MoveCommandDirection) -> Void)?) -> some View`

Adds an action to perform in response to a move command, like when the user
presses an arrow key on a Mac keyboard, or taps the edge of the Siri Remote
when controlling an Apple TV.

`func pageCommand<V>(value: Binding<V>, in: ClosedRange<V>, step: V) -> some
View`

Steps a value through a range in response to page up or page down commands.

`func onExitCommand(perform: (() -> Void)?) -> some View`

Sets up an action that triggers in response to receiving the exit command
while the view has focus.

`func onPlayPauseCommand(perform: (() -> Void)?) -> some View`

Adds an action to perform in response to the system’s Play/Pause command.

`func onCommand(Selector, perform: (() -> Void)?) -> some View`

Adds an action to perform in response to the given selector.

`enum MoveCommandDirection`

Specifies the direction of an arrow key movement.

Instance Method

# deleteDisabled(_:)

Adds a condition for whether the view’s view hierarchy is deletable.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func deleteDisabled(_ isDisabled: Bool) -> some View
    

## See Also

### Editing a list

`func moveDisabled(Bool) -> some View`

Adds a condition for whether the view’s view hierarchy is movable.

`var editMode: Binding<EditMode>?`

An indication of whether the user can edit the contents of a view associated
with this environment.

`enum EditMode`

A mode that indicates whether the user can edit a view’s content.

`struct EditActions`

A set of edit actions on a collection of data that a view can offer to a user.

`struct EditableCollectionContent`

An opaque wrapper view that adds editing capabilities to a row in a list.

`struct IndexedIdentifierCollection`

A collection wrapper that iterates over the indices and identifiers of a
collection together.

Instance Method

# pageCommand(value:in:step:)

Steps a value through a range in response to page up or page down commands.

tvOS 14.3+

    
    
    func pageCommand<V>(
        value: Binding<V>,
        in bounds: ClosedRange<V>,
        step: V = 1
    ) -> some View where V : BinaryInteger
    

##  Parameters

`value`

    

A `Binding` to the value to modify when the user pages up or down.

`bounds`

    

A closed range that specifies the upper and lower bounds of `value`.

`step`

    

The amount by which to increment or decrement `value`. Defaults to 1.

## Discussion

Use this command to step through sections of a data model associated with a
view by providing a binding to a value, a range, and step. If taking another
step would cause the value to exceed the bounds, then the value remains
unchanged.

On tvOS, the user triggers ‘pageUp’ and ‘pageDown’ commands by pressing a
dedicated button on a connected remote. For example, you can let a user page
through a TV programming guide using the channel buttons:

## See Also

### Responding to commands

`func onMoveCommand(perform: ((MoveCommandDirection) -> Void)?) -> some View`

Adds an action to perform in response to a move command, like when the user
presses an arrow key on a Mac keyboard, or taps the edge of the Siri Remote
when controlling an Apple TV.

`func onDeleteCommand(perform: (() -> Void)?) -> some View`

Adds an action to perform in response to the system’s Delete command, or
pressing either the ⌫ (backspace) or ⌦ (forward delete) keys while the view
has focus.

`func onExitCommand(perform: (() -> Void)?) -> some View`

Sets up an action that triggers in response to receiving the exit command
while the view has focus.

`func onPlayPauseCommand(perform: (() -> Void)?) -> some View`

Adds an action to perform in response to the system’s Play/Pause command.

`func onCommand(Selector, perform: (() -> Void)?) -> some View`

Adds an action to perform in response to the given selector.

`enum MoveCommandDirection`

Specifies the direction of an arrow key movement.

Instance Method

# onExitCommand(perform:)

Sets up an action that triggers in response to receiving the exit command
while the view has focus.

macOS 10.15+  tvOS 13.0+

    
    
    func onExitCommand(perform action: (() -> Void)?) -> some View
    

## Discussion

The user generates an exit command by pressing the Menu button on tvOS, or the
escape key on macOS.

## See Also

### Responding to commands

`func onMoveCommand(perform: ((MoveCommandDirection) -> Void)?) -> some View`

Adds an action to perform in response to a move command, like when the user
presses an arrow key on a Mac keyboard, or taps the edge of the Siri Remote
when controlling an Apple TV.

`func onDeleteCommand(perform: (() -> Void)?) -> some View`

Adds an action to perform in response to the system’s Delete command, or
pressing either the ⌫ (backspace) or ⌦ (forward delete) keys while the view
has focus.

`func pageCommand<V>(value: Binding<V>, in: ClosedRange<V>, step: V) -> some
View`

Steps a value through a range in response to page up or page down commands.

`func onPlayPauseCommand(perform: (() -> Void)?) -> some View`

Adds an action to perform in response to the system’s Play/Pause command.

`func onCommand(Selector, perform: (() -> Void)?) -> some View`

Adds an action to perform in response to the given selector.

`enum MoveCommandDirection`

Specifies the direction of an arrow key movement.

Instance Method

# onPlayPauseCommand(perform:)

Adds an action to perform in response to the system’s Play/Pause command.

tvOS 13.0+

    
    
    func onPlayPauseCommand(perform action: (() -> Void)?) -> some View
    

## See Also

### Responding to commands

`func onMoveCommand(perform: ((MoveCommandDirection) -> Void)?) -> some View`

Adds an action to perform in response to a move command, like when the user
presses an arrow key on a Mac keyboard, or taps the edge of the Siri Remote
when controlling an Apple TV.

`func onDeleteCommand(perform: (() -> Void)?) -> some View`

Adds an action to perform in response to the system’s Delete command, or
pressing either the ⌫ (backspace) or ⌦ (forward delete) keys while the view
has focus.

`func pageCommand<V>(value: Binding<V>, in: ClosedRange<V>, step: V) -> some
View`

Steps a value through a range in response to page up or page down commands.

`func onExitCommand(perform: (() -> Void)?) -> some View`

Sets up an action that triggers in response to receiving the exit command
while the view has focus.

`func onCommand(Selector, perform: (() -> Void)?) -> some View`

Adds an action to perform in response to the given selector.

`enum MoveCommandDirection`

Specifies the direction of an arrow key movement.

Instance Method

# onCommand(_:perform:)

Adds an action to perform in response to the given selector.

macOS 10.15+

    
    
    func onCommand(
        _ selector: Selector,
        perform action: (() -> Void)?
    ) -> some View
    

##  Parameters

`selector`

    

The selector to register for `action`.

`action`

    

The action to perform. If `action` is `nil`, `command` keeps its association
with this view but doesn’t trigger.

## Return Value

A view that triggers `action` when the `command` occurs.

## Discussion

This view or one of the views it contains must be in focus in order for the
action to trigger. Other actions for the same command on views _closer_ to the
view in focus take priority, potentially overriding this action.

## See Also

### Responding to commands

`func onMoveCommand(perform: ((MoveCommandDirection) -> Void)?) -> some View`

Adds an action to perform in response to a move command, like when the user
presses an arrow key on a Mac keyboard, or taps the edge of the Siri Remote
when controlling an Apple TV.

`func onDeleteCommand(perform: (() -> Void)?) -> some View`

Adds an action to perform in response to the system’s Delete command, or
pressing either the ⌫ (backspace) or ⌦ (forward delete) keys while the view
has focus.

`func pageCommand<V>(value: Binding<V>, in: ClosedRange<V>, step: V) -> some
View`

Steps a value through a range in response to page up or page down commands.

`func onExitCommand(perform: (() -> Void)?) -> some View`

Sets up an action that triggers in response to receiving the exit command
while the view has focus.

`func onPlayPauseCommand(perform: (() -> Void)?) -> some View`

Adds an action to perform in response to the system’s Play/Pause command.

`enum MoveCommandDirection`

Specifies the direction of an arrow key movement.

Instance Method

# digitalCrownAccessory(_:)

Specifies the visibility of Digital Crown accessory Views on Apple Watch.

watchOS 9.0+

    
    
    func digitalCrownAccessory(_ visibility: Visibility) -> some View
    

##  Parameters

`visibility`

    

The visibility of the digital crown accessory.

## Discussion

Use this method to customize the visibility of a Digital Crown accessory
`View` created with the `View/digitalCrownAccessory(_ content:)` modifier. You
may want to keep an accessory visible even when the Digital Crown Indicator is
not visible to indicate what scrolling the crown will do.

## See Also

### Interacting with the Digital Crown

`func digitalCrownAccessory<Content>(content: () -> Content) -> some View`

Places an accessory View next to the Digital Crown on Apple Watch.

`func digitalCrownRotation<V>(Binding<V>, from: V, through: V, sensitivity:
DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>, onChange: (DigitalCrownEvent) ->
Void, onIdle: () -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(detent: Binding<V>, from: V, through: V, by:
V.Stride, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(detent: Binding<V>, from: V, through: V, by:
V.Stride, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>, from: V, through: V, by: V.Stride?,
sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`struct DigitalCrownEvent`

An event emitted when the user rotates the Digital Crown.

`enum DigitalCrownRotationalSensitivity`

The amount of Digital Crown rotation needed to move between two integer
numbers.

Instance Method

# digitalCrownAccessory(content:)

Places an accessory View next to the Digital Crown on Apple Watch.

watchOS 9.0+

    
    
    func digitalCrownAccessory<Content>(@ViewBuilder content: @escaping () -> Content) -> some View where Content : View
    

##  Parameters

`content`

    

The view to be used as a Digital Crown Accessory.

## Discussion

Use this method to place a custom `View` next to the Digital Crown on Apple
Watch. Use `digitalCrownAccessory(_:)` to specify the visibility of your
custom view.

## See Also

### Interacting with the Digital Crown

`func digitalCrownAccessory(Visibility) -> some View`

Specifies the visibility of Digital Crown accessory Views on Apple Watch.

`func digitalCrownRotation<V>(Binding<V>, from: V, through: V, sensitivity:
DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>, onChange: (DigitalCrownEvent) ->
Void, onIdle: () -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(detent: Binding<V>, from: V, through: V, by:
V.Stride, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(detent: Binding<V>, from: V, through: V, by:
V.Stride, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>, from: V, through: V, by: V.Stride?,
sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`struct DigitalCrownEvent`

An event emitted when the user rotates the Digital Crown.

`enum DigitalCrownRotationalSensitivity`

The amount of Digital Crown rotation needed to move between two integer
numbers.

Instance Method

#
digitalCrownRotation(_:from:through:sensitivity:isContinuous:isHapticFeedbackEnabled:onChange:onIdle:)

Tracks Digital Crown rotations by updating the specified binding.

watchOS 9.0+

    
    
    func digitalCrownRotation<V>(
        _ binding: Binding<V>,
        from minValue: V,
        through maxValue: V,
        sensitivity: DigitalCrownRotationalSensitivity = .high,
        isContinuous: Bool = false,
        isHapticFeedbackEnabled: Bool = true,
        onChange: @escaping (DigitalCrownEvent) -> Void = { _ in },
        onIdle: @escaping () -> Void = { }
    ) -> some View where V : BinaryFloatingPoint
    

##  Parameters

`binding`

    

A binding to a value that updates when the user rotates the Digital Crown.

`minValue`

    

Lower end of the range reported.

`maxValue`

    

Upper end of the range reported.

`sensitivity`

    

How much the user needs to rotate the Digital Crown to move between two
integer numbers.

`isContinuous`

    

Controls if the value reported stops at `minValue` and `maxValue`, or if it
should wrap around. Default is `false`.

`isHapticFeedbackEnabled`

    

Controls the generation of haptic feedback when turning the Digital Crown.
Default is `true`.

`onChange`

    

A block that is called as the Digital Crown is rotated.

`onIdle`

    

A block that is called when the Digital Crown has settled to an idle state.

## Discussion

Use this method to receive continuous values on a binding you provides as the
user turns the Digital Crown on Apple Watch. The example below receives
changes to the binding value, starting at the `minValue` of `0.0` up to the
`maxValue` of `10.0` settling in to multiples of `0.1` increasing or
decreasing depending on the direction that the user turns the Digital Crown,
rolling over if the user exceeds the specified boundary values:

## See Also

### Interacting with the Digital Crown

`func digitalCrownAccessory(Visibility) -> some View`

Specifies the visibility of Digital Crown accessory Views on Apple Watch.

`func digitalCrownAccessory<Content>(content: () -> Content) -> some View`

Places an accessory View next to the Digital Crown on Apple Watch.

`func digitalCrownRotation<V>(Binding<V>, onChange: (DigitalCrownEvent) ->
Void, onIdle: () -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(detent: Binding<V>, from: V, through: V, by:
V.Stride, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(detent: Binding<V>, from: V, through: V, by:
V.Stride, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>, from: V, through: V, by: V.Stride?,
sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`struct DigitalCrownEvent`

An event emitted when the user rotates the Digital Crown.

`enum DigitalCrownRotationalSensitivity`

The amount of Digital Crown rotation needed to move between two integer
numbers.

Instance Method

# digitalCrownRotation(_:onChange:onIdle:)

Tracks Digital Crown rotations by updating the specified binding.

watchOS 9.0+

    
    
    func digitalCrownRotation<V>(
        _ binding: Binding<V>,
        onChange: @escaping (DigitalCrownEvent) -> Void = { _ in },
        onIdle: @escaping () -> Void = { }
    ) -> some View where V : BinaryFloatingPoint
    

##  Parameters

`binding`

    

A binding to a value that updates as the user rotates the Digital Crown. The
implicit range is `(-infinity, +infinity)`.

`onChange`

    

A block that is called as the Digital Crown is rotated.

`onIdle`

    

A block that is called when the Digital Crown has settled to an idle state.

## Discussion

Use this method to receive values on a binding you provide as the user turns
the Digital Crown on Apple Watch. The example below receives changes to the
binding value, starting at `0.0` and incrementing or decrementing depending on
the direction that the user turns the Digital Crown:

## See Also

### Interacting with the Digital Crown

`func digitalCrownAccessory(Visibility) -> some View`

Specifies the visibility of Digital Crown accessory Views on Apple Watch.

`func digitalCrownAccessory<Content>(content: () -> Content) -> some View`

Places an accessory View next to the Digital Crown on Apple Watch.

`func digitalCrownRotation<V>(Binding<V>, from: V, through: V, sensitivity:
DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(detent: Binding<V>, from: V, through: V, by:
V.Stride, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(detent: Binding<V>, from: V, through: V, by:
V.Stride, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>, from: V, through: V, by: V.Stride?,
sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`struct DigitalCrownEvent`

An event emitted when the user rotates the Digital Crown.

`enum DigitalCrownRotationalSensitivity`

The amount of Digital Crown rotation needed to move between two integer
numbers.

Instance Method

#
digitalCrownRotation(detent:from:through:by:sensitivity:isContinuous:isHapticFeedbackEnabled:onChange:onIdle:)

Tracks Digital Crown rotations by updating the specified binding.

watchOS 9.0+

    
    
    func digitalCrownRotation<V>(
        detent: Binding<V>,
        from minValue: V,
        through maxValue: V,
        by stride: V.Stride,
        sensitivity: DigitalCrownRotationalSensitivity = .high,
        isContinuous: Bool = false,
        isHapticFeedbackEnabled: Bool = true,
        onChange: @escaping (DigitalCrownEvent) -> Void = { _ in },
        onIdle: @escaping () -> Void = { }
    ) -> some View where V : BinaryFloatingPoint, V.Stride : BinaryFloatingPoint
    

##  Parameters

`detent`

    

A binding to a value that updates when the user rotates the Digital Crown.

`minValue`

    

Lower end of the range reported.

`maxValue`

    

Upper end of the range reported.

`stride`

    

The value settles on multiples of `stride`.

`sensitivity`

    

How much the user needs to rotate the Digital Crown to move between two
detents.

`isContinuous`

    

Controls if the value reported stops at `minValue` and `maxValue`, or if it
should wrap around. Default is `false`.

`isHapticFeedbackEnabled`

    

Controls the generation of haptic feedback when turning the Digital Crown.
Default is `true`.

`onChange`

    

A block that is called as the Digital Crown is rotated.

`onIdle`

    

A block that is called when the Digital Crown has settled to an idle state.

## Discussion

Use this method to receive values on a binding you provide as the user turns
the Digital Crown on Apple Watch. The example below receives changes to the
binding value, starting at the `minValue` of `0.0` up to the `maxValue` of
`10.0` in steps of `0.1` incrementing or decrementing depending on the
direction that the user turns the Digital Crown, rolling over if the user
exceeds the specified boundary values. The binding will always be updated to a
value that is a multiple of the stride that is provided:

## See Also

### Interacting with the Digital Crown

`func digitalCrownAccessory(Visibility) -> some View`

Specifies the visibility of Digital Crown accessory Views on Apple Watch.

`func digitalCrownAccessory<Content>(content: () -> Content) -> some View`

Places an accessory View next to the Digital Crown on Apple Watch.

`func digitalCrownRotation<V>(Binding<V>, from: V, through: V, sensitivity:
DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>, onChange: (DigitalCrownEvent) ->
Void, onIdle: () -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(detent: Binding<V>, from: V, through: V, by:
V.Stride, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>, from: V, through: V, by: V.Stride?,
sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`struct DigitalCrownEvent`

An event emitted when the user rotates the Digital Crown.

`enum DigitalCrownRotationalSensitivity`

The amount of Digital Crown rotation needed to move between two integer
numbers.

Instance Method

#
digitalCrownRotation(detent:from:through:by:sensitivity:isContinuous:isHapticFeedbackEnabled:onChange:onIdle:)

Tracks Digital Crown rotations by updating the specified binding.

watchOS 9.0+

    
    
    func digitalCrownRotation<V>(
        detent: Binding<V>,
        from minValue: V,
        through maxValue: V,
        by stride: V.Stride,
        sensitivity: DigitalCrownRotationalSensitivity = .high,
        isContinuous: Bool = false,
        isHapticFeedbackEnabled: Bool = true,
        onChange: @escaping (DigitalCrownEvent) -> Void = { _ in },
        onIdle: @escaping () -> Void = { }
    ) -> some View where V : BinaryInteger, V.Stride : BinaryInteger
    

##  Parameters

`binding`

    

A binding to a value that updates when the user rotates the Digital Crown.

`minValue`

    

Lower end of the range reported.

`maxValue`

    

Upper end of the range reported.

`stride`

    

The value settles on multiples of `stride`.

`sensitivity`

    

How much the user needs to rotate the Digital Crown to move between two
integer numbers.

`isContinuous`

    

Controls if the value reported stops at `minValue` and `maxValue`, or if it
should wrap around. Default is `false`.

`isHapticFeedbackEnabled`

    

Controls the generation of haptic feedback when turning the Digital Crown.
Default is `true`.

`onChange`

    

A block that is called as the Digital Crown is rotated.

`onIdle`

    

A block that is called when the Digital Crown has settled to an idle state.

## Discussion

Use this method to receive values on a binding you provides as the user turns
the Digital Crown on Apple Watch. The example below receives changes to the
binding value, starting at the `minValue` of `0` up to the `maxValue` of `100`
in steps of `1` incrementing or decrementing depending on the direction that
the user turns the Digital Crown, rolling over if the user exceeds the
specified boundary values. The binding will always be updated to a value that
is a multiple of the stride that is provided:

## See Also

### Interacting with the Digital Crown

`func digitalCrownAccessory(Visibility) -> some View`

Specifies the visibility of Digital Crown accessory Views on Apple Watch.

`func digitalCrownAccessory<Content>(content: () -> Content) -> some View`

Places an accessory View next to the Digital Crown on Apple Watch.

`func digitalCrownRotation<V>(Binding<V>, from: V, through: V, sensitivity:
DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>, onChange: (DigitalCrownEvent) ->
Void, onIdle: () -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(detent: Binding<V>, from: V, through: V, by:
V.Stride, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>, from: V, through: V, by: V.Stride?,
sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`struct DigitalCrownEvent`

An event emitted when the user rotates the Digital Crown.

`enum DigitalCrownRotationalSensitivity`

The amount of Digital Crown rotation needed to move between two integer
numbers.

Instance Method

# digitalCrownRotation(_:)

Tracks Digital Crown rotations by updating the specified binding.

watchOS 6.0+

    
    
    func digitalCrownRotation<V>(_ binding: Binding<V>) -> some View where V : BinaryFloatingPoint
    

##  Parameters

`binding`

    

A binding to a value that updates as the user rotates the Digital Crown. The
implicit range is `(-infinity, +infinity)`.

## Discussion

Use this method to receive values on a binding you provide as the user turns
the Digital Crown on Apple Watch. The example below receives changes to the
binding value, starting at `0.0` and incrementing or decrementing depending on
the direction that the user turns the Digital Crown:

## See Also

### Interacting with the Digital Crown

`func digitalCrownAccessory(Visibility) -> some View`

Specifies the visibility of Digital Crown accessory Views on Apple Watch.

`func digitalCrownAccessory<Content>(content: () -> Content) -> some View`

Places an accessory View next to the Digital Crown on Apple Watch.

`func digitalCrownRotation<V>(Binding<V>, from: V, through: V, sensitivity:
DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>, onChange: (DigitalCrownEvent) ->
Void, onIdle: () -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(detent: Binding<V>, from: V, through: V, by:
V.Stride, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(detent: Binding<V>, from: V, through: V, by:
V.Stride, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>, from: V, through: V, by: V.Stride?,
sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`struct DigitalCrownEvent`

An event emitted when the user rotates the Digital Crown.

`enum DigitalCrownRotationalSensitivity`

The amount of Digital Crown rotation needed to move between two integer
numbers.

Instance Method

#
digitalCrownRotation(_:from:through:by:sensitivity:isContinuous:isHapticFeedbackEnabled:)

Tracks Digital Crown rotations by updating the specified binding.

watchOS 6.0+

    
    
    func digitalCrownRotation<V>(
        _ binding: Binding<V>,
        from minValue: V,
        through maxValue: V,
        by stride: V.Stride? = nil,
        sensitivity: DigitalCrownRotationalSensitivity = .high,
        isContinuous: Bool = false,
        isHapticFeedbackEnabled: Bool = true
    ) -> some View where V : BinaryFloatingPoint, V.Stride : BinaryFloatingPoint
    

##  Parameters

`binding`

    

A binding to a value that updates when the user rotates the Digital Crown.

`minValue`

    

Lower end of the range reported.

`maxValue`

    

Upper end of the range reported.

`stride`

    

The value settles on multiples of `stride`.

`sensitivity`

    

How much the user needs to rotate the Digital Crown to move between two
integer numbers.

`isContinuous`

    

Controls if the value reported stops at `minValue` and `maxValue`, or if it
should wrap around. Default is `false`.

`isHapticFeedbackEnabled`

    

Controls the generation of haptic feedback when turning the Digital Crown.
Default is `true`.

## Discussion

Use this method to receive values on a binding you provides as the user turns
the Digital Crown on Apple Watch. The example below receives changes to the
binding value, starting at the `minValue` of `0.0` up to the `maxValue` of
`10.0` in steps of `0.1` incrementing or decrementing depending on the
direction that the user turns the Digital Crown, rolling over if the user
exceeds the specified boundary values:

## See Also

### Interacting with the Digital Crown

`func digitalCrownAccessory(Visibility) -> some View`

Specifies the visibility of Digital Crown accessory Views on Apple Watch.

`func digitalCrownAccessory<Content>(content: () -> Content) -> some View`

Places an accessory View next to the Digital Crown on Apple Watch.

`func digitalCrownRotation<V>(Binding<V>, from: V, through: V, sensitivity:
DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>, onChange: (DigitalCrownEvent) ->
Void, onIdle: () -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(detent: Binding<V>, from: V, through: V, by:
V.Stride, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(detent: Binding<V>, from: V, through: V, by:
V.Stride, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`struct DigitalCrownEvent`

An event emitted when the user rotates the Digital Crown.

`enum DigitalCrownRotationalSensitivity`

The amount of Digital Crown rotation needed to move between two integer
numbers.

Instance Method

# userActivity(_:element:_:)

Advertises a user activity type.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func userActivity<P>(
        _ activityType: String,
        element: P?,
        _ update: @escaping (P, NSUserActivity) -> ()
    ) -> some View
    

##  Parameters

`activityType`

    

The type of activity to advertise.

`element`

    

If the element is `nil`, the handler will not be associated with the activity
(and if there are no handlers, no activity is advertised). The method passes
the non-`nil` element to the handler as a convenience so the handlers don’t
all need to implement an early exit with `guard element = element else {
return }`.

`update`

    

A function that modifies the passed-in activity for advertisement.

## Discussion

The scope of the activity applies only to the scene or window the view is in.

## See Also

### Sending and receiving user activities

Restoring Your App’s State with SwiftUI

Provide app continuity for users by preserving their current activities.

`func userActivity(String, isActive: Bool, (NSUserActivity) -> ()) -> some
View`

Advertises a user activity type.

`func onContinueUserActivity(String, perform: (NSUserActivity) -> ()) -> some
View`

Registers a handler to invoke in response to a user activity that your app
receives.

Instance Method

# userActivity(_:isActive:_:)

Advertises a user activity type.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func userActivity(
        _ activityType: String,
        isActive: Bool = true,
        _ update: @escaping (NSUserActivity) -> ()
    ) -> some View
    

##  Parameters

`activityType`

    

The type of activity to advertise.

`isActive`

    

When `false`, avoids advertising the activity. Defaults to `true`.

`update`

    

A function that modifies the passed-in activity for advertisement.

## Discussion

You can use `userActivity(_:isActive:_:)` to start, stop, or modify the
advertisement of a specific type of user activity.

The scope of the activity applies only to the scene or window the view is in.

## See Also

### Sending and receiving user activities

Restoring Your App’s State with SwiftUI

Provide app continuity for users by preserving their current activities.

`func userActivity<P>(String, element: P?, (P, NSUserActivity) -> ()) -> some
View`

Advertises a user activity type.

`func onContinueUserActivity(String, perform: (NSUserActivity) -> ()) -> some
View`

Registers a handler to invoke in response to a user activity that your app
receives.

Instance Method

# onContinueUserActivity(_:perform:)

Registers a handler to invoke in response to a user activity that your app
receives.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func onContinueUserActivity(
        _ activityType: String,
        perform action: @escaping (NSUserActivity) -> ()
    ) -> some View
    

##  Parameters

`activityType`

    

The type of activity that the `action` closure handles. Be sure that this
string matches one of the values that you list in the `NSUserActivityTypes`
array in your app’s Information Property List.

`action`

    

A closure that SwiftUI calls when your app receives a user activity of the
specified type. The closure takes the activity as an input parameter.

## Return Value

A view that handles incoming user activities.

## Discussion

Use this view modifier to receive `NSUserActivity` instances in a particular
scene within your app. The scene that SwiftUI routes the incoming user
activity to depends on the structure of your app, what scenes are active, and
other configuration. For more information, see
`handlesExternalEvents(matching:)`.

UI frameworks traditionally pass Universal Links to your app using a user
activity. However, SwiftUI passes a Universal Link to your app directly as a
URL. To receive a Universal Link, use the `onOpenURL(perform:)` modifier
instead.

## See Also

### Sending and receiving user activities

Restoring Your App’s State with SwiftUI

Provide app continuity for users by preserving their current activities.

`func userActivity<P>(String, element: P?, (P, NSUserActivity) -> ()) -> some
View`

Advertises a user activity type.

`func userActivity(String, isActive: Bool, (NSUserActivity) -> ()) -> some
View`

Advertises a user activity type.

Instance Method

# handlesExternalEvents(preferring:allowing:)

Specifies the external events that the view’s scene handles if the scene is
already open.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    func handlesExternalEvents(
        preferring: Set<String>,
        allowing: Set<String>
    ) -> some View
    

##  Parameters

`preferring`

    

A set of strings that SwiftUI compares against the incoming user activity or
URL to see if the view’s scene prefers to handle the external event.

`allowing`

    

A set of strings that SwiftUI compares against the incoming user activity or
URL to see if the view’s scene can handle the exernal event.

## Return Value

A view whose enclosing scene — if already open — handles incoming external
events.

## Discussion

Apply this modifier to a view to indicate whether an open scene that contains
the view handles specified user activities or URLs that your app receives.
Specify two sets of string identifiers to distinguish between the kinds of
events that the scene _prefers_ to handle and those that it _can_ handle. You
can dynamically update the identifiers in each set to reflect changing app
state.

When your app receives an event on a platform that supports multiple
simultaneous scenes, SwiftUI sends the event to the first open scene it finds
that prefers to handle the event. Otherwise, it sends the event to the first
open scene it finds that can handle the event. If it finds neither — including
when you don’t add this view modifier — SwiftUI creates a new scene for the
event.

Important

Don’t confuse this view modifier with the `handlesExternalEvents(matching:)`
_scene_ modifier. You use the view modifier to indicate that an open scene
handles certain events, whereas you use the scene modifier to help SwiftUI
choose a new scene to open when no open scene handles the event.

On platforms that support only a single scene, SwiftUI ignores this modifier
and sends all external events to the one open scene.

### Matching an event

To find an open scene that handles a particular external event, SwiftUI
compares a property of the event against the strings that you specify in the
`preferring` and `allowing` sets. SwiftUI examines the following event
properties to perform the comparison:

  * For an `NSUserActivity`, like when your app handles Handoff, SwiftUI uses the activity’s `targetContentIdentifier` property, or if that’s `nil`, its `webpageURL` property rendered as an `absoluteString`.

  * For a `URL`, like when another process opens a URL that your app handles, SwiftUI uses the URL’s `absoluteString`.

For both parameter sets, an empty set of strings never matches. Similarly,
empty strings never match. Conversely, as a special case, the string that
contains only an asterisk (`*`) matches anything. The modifier performs string
comparisons that are case and diacritic insensitive.

If you specify multiple instances of this view modifier inside a single scene,
the scene uses the union of the respective `preferring` and `allowing` sets
from all the modifiers.

### Handling a user activity in an open scene

As an example, the following view — which participates in Handoff through the
`userActivity(_:isActive:_:)` and `onContinueUserActivity(_:perform:)` methods
— updates its `preferring` set according to the current selection. The
enclosing scene prefers to handle an event for a contact that’s already
selected, but doesn’t volunteer itself as a preferred scene when no contact is
selected:

The above code also updates the `allowing` set to indicate that the scene can
handle any incoming event when there’s no current selection, but that it can’t
handle any event if the view already displays a contact. The `preferring` set
takes precedence in the special case where the incoming event exactly matches
the currently selected contact.

## See Also

### Handling external events

`func handlesExternalEvents(matching: Set<String>) -> some Scene`

Specifies the external events for which SwiftUI opens a new instance of the
modified scene.

Instance Method

# onAppear(perform:)

Adds an action to perform before this view appears.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func onAppear(perform action: (() -> Void)? = nil) -> some View
    

##  Parameters

`action`

    

The action to perform. If `action` is `nil`, the call has no effect.

## Return Value

A view that triggers `action` before it appears.

## Discussion

The exact moment that SwiftUI calls this method depends on the specific view
type that you apply it to, but the `action` closure completes before the first
rendered frame appears.

## See Also

### Responding to view life cycle updates

`func onDisappear(perform: (() -> Void)?) -> some View`

Adds an action to perform after this view disappears.

`func task(priority: TaskPriority, () async -> Void) -> some View`

Adds an asynchronous task to perform before this view appears.

`func task<T>(id: T, priority: TaskPriority, () async -> Void) -> some View`

Adds a task to perform before this view appears or when a specified value
changes.

Instance Method

# onDisappear(perform:)

Adds an action to perform after this view disappears.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func onDisappear(perform action: (() -> Void)? = nil) -> some View
    

##  Parameters

`action`

    

The action to perform. If `action` is `nil`, the call has no effect.

## Return Value

A view that triggers `action` after it disappears.

## Discussion

The exact moment that SwiftUI calls this method depends on the specific view
type that you apply it to, but the `action` closure doesn’t execute until the
view disappears from the interface.

## See Also

### Responding to view life cycle updates

`func onAppear(perform: (() -> Void)?) -> some View`

Adds an action to perform before this view appears.

`func task(priority: TaskPriority, () async -> Void) -> some View`

Adds an asynchronous task to perform before this view appears.

`func task<T>(id: T, priority: TaskPriority, () async -> Void) -> some View`

Adds a task to perform before this view appears or when a specified value
changes.

Instance Method

# onChange(of:initial:_:)

Adds a modifier for this view that fires an action when a specific value
changes.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func onChange<V>(
        of value: V,
        initial: Bool = false,
        _ action: @escaping () -> Void
    ) -> some View where V : Equatable
    

##  Parameters

`value`

    

The value to check against when determining whether to run the closure.

`initial`

    

Whether the action should be run when this view initially appears.

`action`

    

A closure to run when the value changes.

## Return Value

A view that fires an action when the specified value changes.

## Discussion

You can use `onChange` to trigger a side effect as the result of a value
changing, such as an `Environment` key or a `Binding`.

The system may call the action closure on the main actor, so avoid long-
running tasks in the closure. If you need to perform such tasks, detach an
asynchronous background task.

When the value changes, the new version of the closure will be called, so any
captured values will have their values from the time that the observed value
has its new value. In the following code example, `PlayerView` calls into its
model when `playState` changes model.

## See Also

### Responding to data changes

`func onChange<V>(of: V, initial: Bool, (V, V) -> Void) -> some View`

Adds a modifier for this view that fires an action when a specific value
changes.

`func onReceive<P>(P, perform: (P.Output) -> Void) -> some View`

Adds an action to perform when this view detects data emitted by the given
publisher.

Instance Method

# onChange(of:initial:_:)

Adds a modifier for this view that fires an action when a specific value
changes.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func onChange<V>(
        of value: V,
        initial: Bool = false,
        _ action: @escaping (V, V) -> Void
    ) -> some View where V : Equatable
    

##  Parameters

`value`

    

The value to check against when determining whether to run the closure.

`initial`

    

Whether the action should be run when this view initially appears.

`action`

    

A closure to run when the value changes.

`oldValue`

    

The old value that failed the comparison check (or the initial value when
requested).

`newValue`

    

The new value that failed the comparison check.

## Return Value

A view that fires an action when the specified value changes.

## Discussion

You can use `onChange` to trigger a side effect as the result of a value
changing, such as an `Environment` key or a `Binding`.

The system may call the action closure on the main actor, so avoid long-
running tasks in the closure. If you need to perform such tasks, detach an
asynchronous background task.

When the value changes, the new version of the closure will be called, so any
captured values will have their values from the time that the observed value
has its new value. The old and new observed values are passed into the
closure. In the following code example, `PlayerView` passes both the old and
new values to the model.

## See Also

### Responding to data changes

`func onChange<V>(of: V, initial: Bool, () -> Void) -> some View`

Adds a modifier for this view that fires an action when a specific value
changes.

`func onReceive<P>(P, perform: (P.Output) -> Void) -> some View`

Adds an action to perform when this view detects data emitted by the given
publisher.

Instance Method

# task(priority:_:)

Adds an asynchronous task to perform before this view appears.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func task(
        priority: TaskPriority = .userInitiated,
        _ action: @escaping () async -> Void
    ) -> some View
    

##  Parameters

`priority`

    

The task priority to use when creating the asynchronous task. The default
priority is `userInitiated`.

`action`

    

A closure that SwiftUI calls as an asynchronous task before the view appears.
SwiftUI will automatically cancel the task at some point after the view
disappears before the action completes.

## Return Value

A view that runs the specified action asynchronously before the view appears.

## Discussion

Use this modifier to perform an asynchronous task with a lifetime that matches
that of the modified view. If the task doesn’t finish before SwiftUI removes
the view or the view changes identity, SwiftUI cancels the task.

Use the `await` keyword inside the task to wait for an asynchronous call to
complete, or to wait on the values of an `AsyncSequence` instance. For
example, you can modify a `Text` view to start a task that loads content from
a remote resource:

This example uses the `lines` method to get the content stored at the
specified `URL` as an asynchronous sequence of strings. When each new line
arrives, the body of the `for`-`await`-`in` loop stores the line in an array
of strings and updates the content of the text view to report the latest line
count.

## See Also

### Responding to view life cycle updates

`func onAppear(perform: (() -> Void)?) -> some View`

Adds an action to perform before this view appears.

`func onDisappear(perform: (() -> Void)?) -> some View`

Adds an action to perform after this view disappears.

`func task<T>(id: T, priority: TaskPriority, () async -> Void) -> some View`

Adds a task to perform before this view appears or when a specified value
changes.

Instance Method

# task(id:priority:_:)

Adds a task to perform before this view appears or when a specified value
changes.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func task<T>(
        id value: T,
        priority: TaskPriority = .userInitiated,
        _ action: @escaping () async -> Void
    ) -> some View where T : Equatable
    

##  Parameters

`id`

    

The value to observe for changes. The value must conform to the `Equatable`
protocol.

`priority`

    

The task priority to use when creating the asynchronous task. The default
priority is `userInitiated`.

`action`

    

A closure that SwiftUI calls as an asynchronous task before the view appears.
SwiftUI can automatically cancel the task after the view disappears before the
action completes. If the `id` value changes, SwiftUI cancels and restarts the
task.

## Return Value

A view that runs the specified action asynchronously before the view appears,
or restarts the task when the `id` value changes.

## Discussion

This method behaves like `task(priority:_:)`, except that it also cancels and
recreates the task when a specified value changes. To detect a change, the
modifier tests whether a new value for the `id` parameter equals the previous
value. For this to work, the value’s type must conform to the `Equatable`
protocol.

For example, if you define an equatable `Server` type that posts custom
notifications whenever its state changes — for example, from _signed out_ to
_signed in_ — you can use the task modifier to update the contents of a `Text`
view to reflect the state of the currently selected server:

This example uses the `notifications(named:object:)` method to create an
asynchronous sequence of notifications, given by an `AsyncSequence` instance.
The example then maps the notification sequence to a sequence of strings that
correspond to values stored with each notification.

Elsewhere, the server defines a custom `didUpdateStatus` notification:

Whenever the server status changes, like after the user signs in, the server
posts a notification of this custom type:

The task attached to the `Text` view gets and displays the status value from
the notification’s user information dictionary. When the user chooses a
different server, SwiftUI cancels the task and creates a new one, which then
waits for notifications from the new server.

## See Also

### Responding to view life cycle updates

`func onAppear(perform: (() -> Void)?) -> some View`

Adds an action to perform before this view appears.

`func onDisappear(perform: (() -> Void)?) -> some View`

Adds an action to perform after this view disappears.

`func task(priority: TaskPriority, () async -> Void) -> some View`

Adds an asynchronous task to perform before this view appears.

Instance Method

# renameAction(_:)

Sets a closure to run for the rename action.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func renameAction(_ action: @escaping () -> Void) -> some View
    

##  Parameters

`action`

    

A closure to run when renaming.

## Return Value

A view that has the specified rename action.

## Discussion

Use this modifier in conjunction with the `RenameButton` to implement standard
rename interactions. A rename button receives its action from the environment.
Use this modifier to customize the action provided to the rename button.

When the user taps the rename button in the context menu, the rename action
focuses the text field by setting the `isFocused` property to true.

## See Also

### Renaming a document

`struct RenameButton`

A button that triggers a standard rename action.

`func renameAction(FocusState<Bool>.Binding) -> some View`

Sets the rename action in the environment to update focus state.

`var rename: RenameAction?`

An action that activates the standard rename interaction.

`struct RenameAction`

An action that activates a standard rename interaction.

Instance Method

# renameAction(_:)

Sets the rename action in the environment to update focus state.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func renameAction(_ isFocused: FocusState<Bool>.Binding) -> some View
    

##  Parameters

`isFocused`

    

The focus binding to update when activating the rename action.

## Return Value

A view that has the specified rename action.

## Discussion

Use this modifier in conjunction with the `RenameButton` to implement standard
rename interactions. A rename button receives its action from the environment.
Use this modifier to customize the action provided to the rename button.

When someone taps the rename button in the context menu, the rename action
focuses the text field by setting the `isFocused` property to true.

## See Also

### Renaming a document

`struct RenameButton`

A button that triggers a standard rename action.

`func renameAction(() -> Void) -> some View`

Sets a closure to run for the rename action.

`var rename: RenameAction?`

An action that activates the standard rename interaction.

`struct RenameAction`

An action that activates a standard rename interaction.

Instance Method

# onOpenURL(perform:)

Registers a handler to invoke in response to a URL that your app receives.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func onOpenURL(perform action: @escaping (URL) -> ()) -> some View
    

##  Parameters

`action`

    

A closure that SwiftUI calls when your app receives a Universal Link or a
custom `URL`. The closure takes the URL as an input parameter.

## Return Value

A view that handles incoming URLs.

## Discussion

Use this view modifier to receive URLs in a particular scene within your app.
The scene that SwiftUI routes the incoming URL to depends on the structure of
your app, what scenes are active, and other configuration. For more
information, see `handlesExternalEvents(matching:)`.

UI frameworks traditionally pass Universal Links to your app using an
`NSUserActivity`. However, SwiftUI passes a Universal Link to your app
directly as a URL, which you receive using this modifier. To receive other
user activities, like when your app participates in Handoff, use the
`onContinueUserActivity(_:perform:)` modifier instead.

For more information about linking into your app, see Allowing apps and
websites to link to your content.

## See Also

### Sending and receiving URLs

`var openURL: OpenURLAction`

An action that opens a URL.

`struct OpenURLAction`

An action that opens a URL.

Instance Method

# widgetURL(_:)

Sets the URL to open in the containing app when the user clicks the widget.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    func widgetURL(_ url: URL?) -> some View
    

##  Parameters

`url`

    

The URL to open in the containing app.

## Return Value

A view that opens the specified URL when the user clicks the widget.

## Overview

Widgets support one `widgetURL` modifier in their view hierarchy. If multiple
views have `widgetURL` modifiers, the behavior is undefined.

## See Also

### URLs

`func onOpenURL(perform: (URL) -> ()) -> some View`

Registers a handler to invoke in response to a URL that your app receives.

Instance Method

# onReceive(_:perform:)

Adds an action to perform when this view detects data emitted by the given
publisher.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func onReceive<P>(
        _ publisher: P,
        perform action: @escaping (P.Output) -> Void
    ) -> some View where P : Publisher, P.Failure == Never
    

##  Parameters

`publisher`

    

The publisher to subscribe to.

`action`

    

The action to perform when an event is emitted by `publisher`. The event
emitted by publisher is passed as a parameter to `action`.

## Return Value

A view that triggers `action` when `publisher` emits an event.

## See Also

### Responding to data changes

`func onChange<V>(of: V, initial: Bool, () -> Void) -> some View`

Adds a modifier for this view that fires an action when a specific value
changes.

`func onChange<V>(of: V, initial: Bool, (V, V) -> Void) -> some View`

Adds a modifier for this view that fires an action when a specific value
changes.

Instance Method

# allowsHitTesting(_:)

Configures whether this view participates in hit test operations.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func allowsHitTesting(_ enabled: Bool) -> some View
    

Instance Method

# contentShape(_:eoFill:)

Defines the content shape for hit testing.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func contentShape<S>(
        _ shape: S,
        eoFill: Bool = false
    ) -> some View where S : Shape
    

##  Parameters

`shape`

    

The hit testing shape for the view.

`eoFill`

    

A Boolean that indicates whether the shape is interpreted with the even-odd
winding number rule.

## Return Value

A view that uses the given shape for hit testing.

## See Also

### Controlling hit testing

`func allowsTightening(Bool) -> some View`

Sets whether text in this view can compress the space between characters when
necessary to fit text in a line.

`func contentShape<S>(ContentShapeKinds, S, eoFill: Bool) -> some View`

Sets the content shape for this view.

`struct ContentShapeKinds`

A kind for the content shape of a view.

Instance Method

# contentShape(_:_:eoFill:)

Sets the content shape for this view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func contentShape<S>(
        _ kind: ContentShapeKinds,
        _ shape: S,
        eoFill: Bool = false
    ) -> some View where S : Shape
    

##  Parameters

`kind`

    

The kinds to apply to this content shape.

`shape`

    

The shape to use.

`eoFill`

    

A Boolean that indicates whether the shape is interpreted with the even-odd
winding number rule.

## Return Value

A view that uses the given shape for the specified kind.

## Discussion

The content shape has a variety of uses. You can control the kind of the
content shape by specifying one in `kind`. For example, the following example
only sets the focus ring shape of the view, without affecting its shape for
hit-testing:

## See Also

### Controlling hit testing

`func allowsTightening(Bool) -> some View`

Sets whether text in this view can compress the space between characters when
necessary to fit text in a line.

`func contentShape<S>(S, eoFill: Bool) -> some View`

Defines the content shape for hit testing.

`struct ContentShapeKinds`

A kind for the content shape of a view.

Instance Method

# exportsItemProviders(_:onExport:)

Exports a read-only item provider for consumption by shortcuts, quick actions,
and services.

macOS 12.0+

    
    
    func exportsItemProviders(
        _ contentTypes: [UTType],
        onExport: @escaping () -> [NSItemProvider]
    ) -> some View
    

##  Parameters

`contentTypes`

    

The types of content that the view supports exporting. An empty array means
the view does not currently support exporting.

`onExport`

    

A closure that will be called on request of the items by the shortcut or
service.

## Discussion

If the associated view supports selection, the exported item should reflect
that selected subpart.

## See Also

### Importing and exporting using item providers

`func importsItemProviders([UTType], onImport: ([NSItemProvider]) -> Bool) ->
some View`

Enables importing item providers from services, such as Continuity Camera on
macOS.

`func exportsItemProviders([UTType], onExport: () -> [NSItemProvider], onEdit:
([NSItemProvider]) -> Bool) -> some View`

Exports a read-write item provider for consumption by shortcuts, quick
actions, and services.

Instance Method

# exportsItemProviders(_:onExport:onEdit:)

Exports a read-write item provider for consumption by shortcuts, quick
actions, and services.

macOS 12.0+

    
    
    func exportsItemProviders(
        _ contentTypes: [UTType],
        onExport: @escaping () -> [NSItemProvider],
        onEdit: @escaping ([NSItemProvider]) -> Bool
    ) -> some View
    

##  Parameters

`contentTypes`

    

The types of content that the view supports exporting and importing. An empty
array means the view does not currently support exporting.

`onExport`

    

A closure that will be called on request of the items by the shortcut or
service.

`onEdit`

    

A closure that will be called after the shortcut or service completes with its
output data. This should replace the selected subpart that was exported with
`onExport`. Return `false` to indicate that there was a failure to receive the
items.

## Discussion

If the associated view supports selection, the exported item should reflect
that selected subpart.

## See Also

### Importing and exporting using item providers

`func importsItemProviders([UTType], onImport: ([NSItemProvider]) -> Bool) ->
some View`

Enables importing item providers from services, such as Continuity Camera on
macOS.

`func exportsItemProviders([UTType], onExport: () -> [NSItemProvider]) -> some
View`

Exports a read-only item provider for consumption by shortcuts, quick actions,
and services.

Instance Method

# importsItemProviders(_:onImport:)

Enables importing item providers from services, such as Continuity Camera on
macOS.

macOS 12.0+

    
    
    func importsItemProviders(
        _ contentTypes: [UTType],
        onImport: @escaping ([NSItemProvider]) -> Bool
    ) -> some View
    

##  Parameters

`contentTypes`

    

The types of content that the view supports importing. An empty array means
the view does not currently support importing.

`onImport`

    

A closure that will be called with the imported service item. Return `false`
to indicate that there was a failure to receive the items.

## See Also

### Importing and exporting using item providers

`func exportsItemProviders([UTType], onExport: () -> [NSItemProvider]) -> some
View`

Exports a read-only item provider for consumption by shortcuts, quick actions,
and services.

`func exportsItemProviders([UTType], onExport: () -> [NSItemProvider], onEdit:
([NSItemProvider]) -> Bool) -> some View`

Exports a read-write item provider for consumption by shortcuts, quick
actions, and services.

Instance Method

# exportableToServices(_:)

Exports items for consumption by shortcuts, quick actions, and services.

macOS 13.0+

    
    
    func exportableToServices<T>(_ payload: @autoclosure @escaping () -> [T]) -> some View where T : Transferable
    

##  Parameters

`payload`

    

A closure that will be called on request of the items by the shortcut or
service.

## Discussion

If the associated view supports selection, the exported item should reflect
that selected subpart.

## See Also

### Importing and exporting transferable items

`func importableFromServices<T>(for: T.Type, action: ([T]) -> Bool) -> some
View`

Enables importing items from services, such as Continuity Camera on macOS.

`func exportableToServices<T>(() -> [T], onEdit: ([T]) -> Bool) -> some View`

Exports read-write items for consumption by shortcuts, quick actions, and
services.

Instance Method

# exportableToServices(_:onEdit:)

Exports read-write items for consumption by shortcuts, quick actions, and
services.

macOS 13.0+

    
    
    func exportableToServices<T>(
        _ payload: @autoclosure @escaping () -> [T],
        onEdit: @escaping ([T]) -> Bool
    ) -> some View where T : Transferable
    

##  Parameters

`payload`

    

A closure that will be called on request of the items by the shortcut or
service.

`onEdit`

    

A closure that will be called after the shortcut or service completes with its
output data. This should replace the selected subpart that was exported with
`onExport`. Return `false` to indicate that there was a failure to receive the
items.

## Discussion

If the associated view supports selection, the exported item should reflect
that selected subpart.

## See Also

### Importing and exporting transferable items

`func importableFromServices<T>(for: T.Type, action: ([T]) -> Bool) -> some
View`

Enables importing items from services, such as Continuity Camera on macOS.

`func exportableToServices<T>(() -> [T]) -> some View`

Exports items for consumption by shortcuts, quick actions, and services.

Instance Method

# importableFromServices(for:action:)

Enables importing items from services, such as Continuity Camera on macOS.

macOS 13.0+

    
    
    func importableFromServices<T>(
        for payloadType: T.Type = T.self,
        action: @escaping ([T]) -> Bool
    ) -> some View where T : Transferable
    

##  Parameters

`payloadType`

    

The expected type of the imported models.

`action`

    

A closure that will be called with the imported service item. Return `false`
to indicate that there was a failure to receive the items.

## Discussion

## See Also

### Importing and exporting transferable items

`func exportableToServices<T>(() -> [T]) -> some View`

Exports items for consumption by shortcuts, quick actions, and services.

`func exportableToServices<T>(() -> [T], onEdit: ([T]) -> Bool) -> some View`

Exports read-write items for consumption by shortcuts, quick actions, and
services.

Instance Method

# shortcutsLinkStyle(_:)

Sets the given style for ShortcutsLinks within the view hierarchy

AppIntents  SwiftUI  iOS 16.0+  iPadOS 16.0+

    
    
    func shortcutsLinkStyle(_ style: ShortcutsLinkStyle) -> some View
    

##  Parameters

`style`

    

The style to set.

## Return Value

A view that uses the specified shortcuts button style on its child views.

## See Also

### App intents

`func siriTipViewStyle(SiriTipViewStyle) -> some View`

Sets the given style for SiriTipView within the view hierarchy

Instance Method

# siriTipViewStyle(_:)

Sets the given style for SiriTipView within the view hierarchy

AppIntents  SwiftUI  iOS 16.0+  iPadOS 16.0+

    
    
    func siriTipViewStyle(_ style: SiriTipViewStyle) -> some View
    

##  Parameters

`style`

    

The style to set.

## Return Value

A view that uses the specified style on its child views.

## See Also

### App intents

`func shortcutsLinkStyle(ShortcutsLinkStyle) -> some View`

Sets the given style for ShortcutsLinks within the view hierarchy



# InterfaceOrientation

Type Property

# portrait

The device is in portrait mode, with the top of the device on top.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static let portrait: InterfaceOrientation

## See Also

### Getting an orientation

`static let portraitUpsideDown: InterfaceOrientation`

The device is in portrait mode, but is upside down.

`static let landscapeLeft: InterfaceOrientation`

The device is in landscape mode, with the top of the device on the left.

`static let landscapeRight: InterfaceOrientation`

The device is in landscape mode, with the top of the device on the right.

Type Property

# portraitUpsideDown

The device is in portrait mode, but is upside down.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static let portraitUpsideDown: InterfaceOrientation

## See Also

### Getting an orientation

`static let portrait: InterfaceOrientation`

The device is in portrait mode, with the top of the device on top.

`static let landscapeLeft: InterfaceOrientation`

The device is in landscape mode, with the top of the device on the left.

`static let landscapeRight: InterfaceOrientation`

The device is in landscape mode, with the top of the device on the right.

Type Property

# landscapeLeft

The device is in landscape mode, with the top of the device on the left.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static let landscapeLeft: InterfaceOrientation

## See Also

### Getting an orientation

`static let portrait: InterfaceOrientation`

The device is in portrait mode, with the top of the device on top.

`static let portraitUpsideDown: InterfaceOrientation`

The device is in portrait mode, but is upside down.

`static let landscapeRight: InterfaceOrientation`

The device is in landscape mode, with the top of the device on the right.

Type Property

# landscapeRight

The device is in landscape mode, with the top of the device on the right.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static let landscapeRight: InterfaceOrientation

## See Also

### Getting an orientation

`static let portrait: InterfaceOrientation`

The device is in portrait mode, with the top of the device on top.

`static let portraitUpsideDown: InterfaceOrientation`

The device is in portrait mode, but is upside down.

`static let landscapeLeft: InterfaceOrientation`

The device is in landscape mode, with the top of the device on the left.

Type Property

# portrait

The device is in portrait mode, with the top of the device on top.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static let portrait: InterfaceOrientation

## See Also

### Getting an orientation

`static let portraitUpsideDown: InterfaceOrientation`

The device is in portrait mode, but is upside down.

`static let landscapeLeft: InterfaceOrientation`

The device is in landscape mode, with the top of the device on the left.

`static let landscapeRight: InterfaceOrientation`

The device is in landscape mode, with the top of the device on the right.

Type Property

# portraitUpsideDown

The device is in portrait mode, but is upside down.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static let portraitUpsideDown: InterfaceOrientation

## See Also

### Getting an orientation

`static let portrait: InterfaceOrientation`

The device is in portrait mode, with the top of the device on top.

`static let landscapeLeft: InterfaceOrientation`

The device is in landscape mode, with the top of the device on the left.

`static let landscapeRight: InterfaceOrientation`

The device is in landscape mode, with the top of the device on the right.

Type Property

# landscapeLeft

The device is in landscape mode, with the top of the device on the left.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static let landscapeLeft: InterfaceOrientation

## See Also

### Getting an orientation

`static let portrait: InterfaceOrientation`

The device is in portrait mode, with the top of the device on top.

`static let portraitUpsideDown: InterfaceOrientation`

The device is in portrait mode, but is upside down.

`static let landscapeRight: InterfaceOrientation`

The device is in landscape mode, with the top of the device on the right.

Type Property

# landscapeRight

The device is in landscape mode, with the top of the device on the right.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static let landscapeRight: InterfaceOrientation

## See Also

### Getting an orientation

`static let portrait: InterfaceOrientation`

The device is in portrait mode, with the top of the device on top.

`static let portraitUpsideDown: InterfaceOrientation`

The device is in portrait mode, but is upside down.

`static let landscapeLeft: InterfaceOrientation`

The device is in landscape mode, with the top of the device on the left.



# ImmersiveSpaceContent

Instance Property

# body

visionOS 1.0+

    
    
    @ImmersiveSpaceContentBuilder
    var body: Self.Body { get }

**Required**

## See Also

### Creating immersive space content

`associatedtype Body : ImmersiveSpaceContent`

**Required**

Associated Type

# Body

visionOS 1.0+

    
    
    associatedtype Body : ImmersiveSpaceContent

**Required**

## See Also

### Creating immersive space content

`var body: Self.Body`

**Required**



# IconOnlyLabelStyle

Initializer

# init()

Creates an icon-only label style.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init()



# IndexViewStyle

Type Property

# page

An index view style that places a page index view over its content.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS 8.0+
visionOS 1.0+

    
    
    static var page: PageIndexViewStyle { get }

Available when `Self` is `PageIndexViewStyle`.

## See Also

### Getting built-in index view styles

`static func page(backgroundDisplayMode:
PageIndexViewStyle.BackgroundDisplayMode) -> PageIndexViewStyle`

An index view style that places a page index view over its content.

Available when `Self` is `PageIndexViewStyle`.

Type Method

# page(backgroundDisplayMode:)

An index view style that places a page index view over its content.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS 8.0+
visionOS 1.0+

    
    
    static func page(backgroundDisplayMode: PageIndexViewStyle.BackgroundDisplayMode) -> PageIndexViewStyle

Available when `Self` is `PageIndexViewStyle`.

##  Parameters

`backgroundDisplayMode`

    

The display mode of the background of any page index views receiving this
style

## See Also

### Getting built-in index view styles

`static var page: PageIndexViewStyle`

An index view style that places a page index view over its content.

Available when `Self` is `PageIndexViewStyle`.

Structure

# PageIndexViewStyle

An index view style that places a page index view over its content.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS 8.0+
visionOS 1.0+

    
    
    struct PageIndexViewStyle

## Overview

You can also use `page` to construct this style.

## Topics

### Creating the control group style

`init(backgroundDisplayMode: PageIndexViewStyle.BackgroundDisplayMode)`

Creates a page index view style.

`struct BackgroundDisplayMode`

The background style for the page index view.

## Relationships

### Conforms To

  * `IndexViewStyle`



# InsettableShape

Instance Method

# strokeBorder(_:lineWidth:antialiased:)

Returns a view that is the result of filling the `lineWidth`-sized border (aka
inner stroke) of `self` with `content`. This is equivalent to insetting `self`
by `lineWidth / 2` and stroking the resulting shape with `lineWidth` as the
line-width.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func strokeBorder<S>(
        _ content: S = .foreground,
        lineWidth: CGFloat = 1,
        antialiased: Bool = true
    ) -> StrokeBorderShapeView<Self, S, EmptyView> where S : ShapeStyle

## See Also

### Setting the stroke border characteristics

`func strokeBorder<S>(S, lineWidth: CGFloat, antialiased: Bool) -> some View`

Returns a view that is the result of filling the `lineWidth`-sized border (aka
inner stroke) of `self` with `content`. This is equivalent to insetting `self`
by `lineWidth / 2` and stroking the resulting shape with `lineWidth` as the
line-width.

`func strokeBorder(lineWidth: CGFloat, antialiased: Bool) -> some View`

Returns a view that is the result of filling the `lineWidth`-sized border (aka
inner stroke) of `self` with the foreground color. This is equivalent to
insetting `self` by `lineWidth / 2` and stroking the resulting shape with
`lineWidth` as the line-width.

`func strokeBorder<S>(S, style: StrokeStyle, antialiased: Bool) ->
StrokeBorderShapeView<Self, S, EmptyView>`

Returns a view that is the result of insetting `self` by `style.lineWidth /
2`, stroking the resulting shape with `style`, and then filling with
`content`.

`func strokeBorder<S>(S, style: StrokeStyle, antialiased: Bool) -> some View`

Returns a view that is the result of insetting `self` by `style.lineWidth /
2`, stroking the resulting shape with `style`, and then filling with
`content`.

`func strokeBorder(style: StrokeStyle, antialiased: Bool) -> some View`

Returns a view that is the result of insetting `self` by `style.lineWidth /
2`, stroking the resulting shape with `style`, and then filling with the
foreground color.

Instance Method

# strokeBorder(_:lineWidth:antialiased:)

Returns a view that is the result of filling the `lineWidth`-sized border (aka
inner stroke) of `self` with `content`. This is equivalent to insetting `self`
by `lineWidth / 2` and stroking the resulting shape with `lineWidth` as the
line-width.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func strokeBorder<S>(
        _ content: S,
        lineWidth: CGFloat = 1,
        antialiased: Bool = true
    ) -> some View where S : ShapeStyle
    

## See Also

### Setting the stroke border characteristics

`func strokeBorder<S>(S, lineWidth: CGFloat, antialiased: Bool) ->
StrokeBorderShapeView<Self, S, EmptyView>`

Returns a view that is the result of filling the `lineWidth`-sized border (aka
inner stroke) of `self` with `content`. This is equivalent to insetting `self`
by `lineWidth / 2` and stroking the resulting shape with `lineWidth` as the
line-width.

`func strokeBorder(lineWidth: CGFloat, antialiased: Bool) -> some View`

Returns a view that is the result of filling the `lineWidth`-sized border (aka
inner stroke) of `self` with the foreground color. This is equivalent to
insetting `self` by `lineWidth / 2` and stroking the resulting shape with
`lineWidth` as the line-width.

`func strokeBorder<S>(S, style: StrokeStyle, antialiased: Bool) ->
StrokeBorderShapeView<Self, S, EmptyView>`

Returns a view that is the result of insetting `self` by `style.lineWidth /
2`, stroking the resulting shape with `style`, and then filling with
`content`.

`func strokeBorder<S>(S, style: StrokeStyle, antialiased: Bool) -> some View`

Returns a view that is the result of insetting `self` by `style.lineWidth /
2`, stroking the resulting shape with `style`, and then filling with
`content`.

`func strokeBorder(style: StrokeStyle, antialiased: Bool) -> some View`

Returns a view that is the result of insetting `self` by `style.lineWidth /
2`, stroking the resulting shape with `style`, and then filling with the
foreground color.

Instance Method

# strokeBorder(lineWidth:antialiased:)

Returns a view that is the result of filling the `lineWidth`-sized border (aka
inner stroke) of `self` with the foreground color. This is equivalent to
insetting `self` by `lineWidth / 2` and stroking the resulting shape with
`lineWidth` as the line-width.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func strokeBorder(
        lineWidth: CGFloat = 1,
        antialiased: Bool = true
    ) -> some View
    

## See Also

### Setting the stroke border characteristics

`func strokeBorder<S>(S, lineWidth: CGFloat, antialiased: Bool) ->
StrokeBorderShapeView<Self, S, EmptyView>`

Returns a view that is the result of filling the `lineWidth`-sized border (aka
inner stroke) of `self` with `content`. This is equivalent to insetting `self`
by `lineWidth / 2` and stroking the resulting shape with `lineWidth` as the
line-width.

`func strokeBorder<S>(S, lineWidth: CGFloat, antialiased: Bool) -> some View`

Returns a view that is the result of filling the `lineWidth`-sized border (aka
inner stroke) of `self` with `content`. This is equivalent to insetting `self`
by `lineWidth / 2` and stroking the resulting shape with `lineWidth` as the
line-width.

`func strokeBorder<S>(S, style: StrokeStyle, antialiased: Bool) ->
StrokeBorderShapeView<Self, S, EmptyView>`

Returns a view that is the result of insetting `self` by `style.lineWidth /
2`, stroking the resulting shape with `style`, and then filling with
`content`.

`func strokeBorder<S>(S, style: StrokeStyle, antialiased: Bool) -> some View`

Returns a view that is the result of insetting `self` by `style.lineWidth /
2`, stroking the resulting shape with `style`, and then filling with
`content`.

`func strokeBorder(style: StrokeStyle, antialiased: Bool) -> some View`

Returns a view that is the result of insetting `self` by `style.lineWidth /
2`, stroking the resulting shape with `style`, and then filling with the
foreground color.

Instance Method

# strokeBorder(_:style:antialiased:)

Returns a view that is the result of insetting `self` by `style.lineWidth /
2`, stroking the resulting shape with `style`, and then filling with
`content`.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func strokeBorder<S>(
        _ content: S = .foreground,
        style: StrokeStyle,
        antialiased: Bool = true
    ) -> StrokeBorderShapeView<Self, S, EmptyView> where S : ShapeStyle

## See Also

### Setting the stroke border characteristics

`func strokeBorder<S>(S, lineWidth: CGFloat, antialiased: Bool) ->
StrokeBorderShapeView<Self, S, EmptyView>`

Returns a view that is the result of filling the `lineWidth`-sized border (aka
inner stroke) of `self` with `content`. This is equivalent to insetting `self`
by `lineWidth / 2` and stroking the resulting shape with `lineWidth` as the
line-width.

`func strokeBorder<S>(S, lineWidth: CGFloat, antialiased: Bool) -> some View`

Returns a view that is the result of filling the `lineWidth`-sized border (aka
inner stroke) of `self` with `content`. This is equivalent to insetting `self`
by `lineWidth / 2` and stroking the resulting shape with `lineWidth` as the
line-width.

`func strokeBorder(lineWidth: CGFloat, antialiased: Bool) -> some View`

Returns a view that is the result of filling the `lineWidth`-sized border (aka
inner stroke) of `self` with the foreground color. This is equivalent to
insetting `self` by `lineWidth / 2` and stroking the resulting shape with
`lineWidth` as the line-width.

`func strokeBorder<S>(S, style: StrokeStyle, antialiased: Bool) -> some View`

Returns a view that is the result of insetting `self` by `style.lineWidth /
2`, stroking the resulting shape with `style`, and then filling with
`content`.

`func strokeBorder(style: StrokeStyle, antialiased: Bool) -> some View`

Returns a view that is the result of insetting `self` by `style.lineWidth /
2`, stroking the resulting shape with `style`, and then filling with the
foreground color.

Instance Method

# strokeBorder(_:style:antialiased:)

Returns a view that is the result of insetting `self` by `style.lineWidth /
2`, stroking the resulting shape with `style`, and then filling with
`content`.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func strokeBorder<S>(
        _ content: S,
        style: StrokeStyle,
        antialiased: Bool = true
    ) -> some View where S : ShapeStyle
    

## See Also

### Setting the stroke border characteristics

`func strokeBorder<S>(S, lineWidth: CGFloat, antialiased: Bool) ->
StrokeBorderShapeView<Self, S, EmptyView>`

Returns a view that is the result of filling the `lineWidth`-sized border (aka
inner stroke) of `self` with `content`. This is equivalent to insetting `self`
by `lineWidth / 2` and stroking the resulting shape with `lineWidth` as the
line-width.

`func strokeBorder<S>(S, lineWidth: CGFloat, antialiased: Bool) -> some View`

Returns a view that is the result of filling the `lineWidth`-sized border (aka
inner stroke) of `self` with `content`. This is equivalent to insetting `self`
by `lineWidth / 2` and stroking the resulting shape with `lineWidth` as the
line-width.

`func strokeBorder(lineWidth: CGFloat, antialiased: Bool) -> some View`

Returns a view that is the result of filling the `lineWidth`-sized border (aka
inner stroke) of `self` with the foreground color. This is equivalent to
insetting `self` by `lineWidth / 2` and stroking the resulting shape with
`lineWidth` as the line-width.

`func strokeBorder<S>(S, style: StrokeStyle, antialiased: Bool) ->
StrokeBorderShapeView<Self, S, EmptyView>`

Returns a view that is the result of insetting `self` by `style.lineWidth /
2`, stroking the resulting shape with `style`, and then filling with
`content`.

`func strokeBorder(style: StrokeStyle, antialiased: Bool) -> some View`

Returns a view that is the result of insetting `self` by `style.lineWidth /
2`, stroking the resulting shape with `style`, and then filling with the
foreground color.

Instance Method

# strokeBorder(style:antialiased:)

Returns a view that is the result of insetting `self` by `style.lineWidth /
2`, stroking the resulting shape with `style`, and then filling with the
foreground color.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func strokeBorder(
        style: StrokeStyle,
        antialiased: Bool = true
    ) -> some View
    

## See Also

### Setting the stroke border characteristics

`func strokeBorder<S>(S, lineWidth: CGFloat, antialiased: Bool) ->
StrokeBorderShapeView<Self, S, EmptyView>`

Returns a view that is the result of filling the `lineWidth`-sized border (aka
inner stroke) of `self` with `content`. This is equivalent to insetting `self`
by `lineWidth / 2` and stroking the resulting shape with `lineWidth` as the
line-width.

`func strokeBorder<S>(S, lineWidth: CGFloat, antialiased: Bool) -> some View`

Returns a view that is the result of filling the `lineWidth`-sized border (aka
inner stroke) of `self` with `content`. This is equivalent to insetting `self`
by `lineWidth / 2` and stroking the resulting shape with `lineWidth` as the
line-width.

`func strokeBorder(lineWidth: CGFloat, antialiased: Bool) -> some View`

Returns a view that is the result of filling the `lineWidth`-sized border (aka
inner stroke) of `self` with the foreground color. This is equivalent to
insetting `self` by `lineWidth / 2` and stroking the resulting shape with
`lineWidth` as the line-width.

`func strokeBorder<S>(S, style: StrokeStyle, antialiased: Bool) ->
StrokeBorderShapeView<Self, S, EmptyView>`

Returns a view that is the result of insetting `self` by `style.lineWidth /
2`, stroking the resulting shape with `style`, and then filling with
`content`.

`func strokeBorder<S>(S, style: StrokeStyle, antialiased: Bool) -> some View`

Returns a view that is the result of insetting `self` by `style.lineWidth /
2`, stroking the resulting shape with `style`, and then filling with
`content`.

Instance Method

# inset(by:)

Returns `self` inset by `amount`.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func inset(by amount: CGFloat) -> Self.InsetShape

**Required**

## See Also

### Setting the inset

`associatedtype InsetShape : InsettableShape`

The type of the inset shape.

**Required**

Associated Type

# InsetShape

The type of the inset shape.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    associatedtype InsetShape : InsettableShape

**Required**

## See Also

### Setting the inset

`func inset(by: CGFloat) -> Self.InsetShape`

Returns `self` inset by `amount`.

**Required**



# Identifiable Implementations

Instance Property

# id

The stable identity of the entity associated with this instance, corresponding
to the `id` of the binding’s wrapped value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var id: Value.ID { get }

Available when `Value` conforms to `Identifiable`.

## See Also

### Managing changes

`func animation(Animation?) -> Binding<Value>`

Specifies an animation to perform when the binding value changes.

`func transaction(Transaction) -> Binding<Value>`

Specifies a transaction for the binding.

`var transaction: Transaction`

The binding’s transaction.



# Input events

Instance Method

# onKeyPress(_:action:)

Performs an action if the user presses a key on a hardware keyboard while the
view has focus.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    func onKeyPress(
        _ key: KeyEquivalent,
        action: @escaping () -> KeyPress.Result
    ) -> some View
    

##  Parameters

`key`

    

The key to match against incoming hardware keyboard events.

`action`

    

The action to perform. Return `.handled` to consume the event and prevent
further dispatch, or `.ignored` to allow dispatch to continue.

## Return Value

A modified view that binds hardware keyboard input when focused.

## Discussion

SwiftUI performs the action for key-down and key-repeat events.

## See Also

### Responding to keyboard input

`func onKeyPress(phases: KeyPress.Phases, action: (KeyPress) ->
KeyPress.Result) -> some View`

Performs an action if the user presses any key on a hardware keyboard while
the view has focus.

`func onKeyPress(KeyEquivalent, phases: KeyPress.Phases, action: (KeyPress) ->
KeyPress.Result) -> some View`

Performs an action if the user presses a key on a hardware keyboard while the
view has focus.

`func onKeyPress(characters: CharacterSet, phases: KeyPress.Phases, action:
(KeyPress) -> KeyPress.Result) -> some View`

Performs an action if the user presses one or more keys on a hardware keyboard
while the view has focus.

`func onKeyPress(keys: Set<KeyEquivalent>, phases: KeyPress.Phases, action:
(KeyPress) -> KeyPress.Result) -> some View`

Performs an action if the user presses one or more keys on a hardware keyboard
while the view has focus.

`struct KeyPress`

Instance Method

# onKeyPress(phases:action:)

Performs an action if the user presses any key on a hardware keyboard while
the view has focus.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    func onKeyPress(
        phases: KeyPress.Phases = [.down, .repeat],
        action: @escaping (KeyPress) -> KeyPress.Result
    ) -> some View
    

##  Parameters

`phases`

    

The key-press phases to match (`.down`, `.repeat`, and `.up`). The default
value is `[.down, .repeat]`.

`action`

    

The action to perform. The action receives a value describing the matched key
event. Return `.handled` to consume the event and prevent further dispatch, or
`.ignored` to allow dispatch to continue.

## Return Value

A modified view that binds hardware keyboard input when focused.

## See Also

### Responding to keyboard input

`func onKeyPress(KeyEquivalent, action: () -> KeyPress.Result) -> some View`

Performs an action if the user presses a key on a hardware keyboard while the
view has focus.

`func onKeyPress(KeyEquivalent, phases: KeyPress.Phases, action: (KeyPress) ->
KeyPress.Result) -> some View`

Performs an action if the user presses a key on a hardware keyboard while the
view has focus.

`func onKeyPress(characters: CharacterSet, phases: KeyPress.Phases, action:
(KeyPress) -> KeyPress.Result) -> some View`

Performs an action if the user presses one or more keys on a hardware keyboard
while the view has focus.

`func onKeyPress(keys: Set<KeyEquivalent>, phases: KeyPress.Phases, action:
(KeyPress) -> KeyPress.Result) -> some View`

Performs an action if the user presses one or more keys on a hardware keyboard
while the view has focus.

`struct KeyPress`

Instance Method

# onKeyPress(_:phases:action:)

Performs an action if the user presses a key on a hardware keyboard while the
view has focus.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    func onKeyPress(
        _ key: KeyEquivalent,
        phases: KeyPress.Phases,
        action: @escaping (KeyPress) -> KeyPress.Result
    ) -> some View
    

##  Parameters

`key`

    

The key to match against incoming hardware keyboard events.

`phases`

    

The key-press phases to match (`.down`, `.up`, and `.repeat`).

`action`

    

The action to perform. The action receives a value describing the matched key
event. Return `.handled` to consume the event and prevent further dispatch, or
`.ignored` to allow dispatch to continue.

## Return Value

A modified view that binds hardware keyboard input when focused.

## Discussion

SwiftUI performs the action for the specified event phases.

## See Also

### Responding to keyboard input

`func onKeyPress(KeyEquivalent, action: () -> KeyPress.Result) -> some View`

Performs an action if the user presses a key on a hardware keyboard while the
view has focus.

`func onKeyPress(phases: KeyPress.Phases, action: (KeyPress) ->
KeyPress.Result) -> some View`

Performs an action if the user presses any key on a hardware keyboard while
the view has focus.

`func onKeyPress(characters: CharacterSet, phases: KeyPress.Phases, action:
(KeyPress) -> KeyPress.Result) -> some View`

Performs an action if the user presses one or more keys on a hardware keyboard
while the view has focus.

`func onKeyPress(keys: Set<KeyEquivalent>, phases: KeyPress.Phases, action:
(KeyPress) -> KeyPress.Result) -> some View`

Performs an action if the user presses one or more keys on a hardware keyboard
while the view has focus.

`struct KeyPress`

Instance Method

# onKeyPress(characters:phases:action:)

Performs an action if the user presses one or more keys on a hardware keyboard
while the view has focus.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    func onKeyPress(
        characters: CharacterSet,
        phases: KeyPress.Phases = [.down, .repeat],
        action: @escaping (KeyPress) -> KeyPress.Result
    ) -> some View
    

##  Parameters

`characters`

    

The set of characters to match against incoming hardware keyboard events.

`phases`

    

The key-press phases to match (`.down`, `.repeat`, and `.up`). The default
value is `[.down, .repeat]`.

`action`

    

The action to perform. The action receives a value describing the matched key
event. Return `.handled` to consume the event and prevent further dispatch, or
`.ignored` to allow dispatch to continue.

## Return Value

A modified view that binds hardware keyboard input when focused.

## See Also

### Responding to keyboard input

`func onKeyPress(KeyEquivalent, action: () -> KeyPress.Result) -> some View`

Performs an action if the user presses a key on a hardware keyboard while the
view has focus.

`func onKeyPress(phases: KeyPress.Phases, action: (KeyPress) ->
KeyPress.Result) -> some View`

Performs an action if the user presses any key on a hardware keyboard while
the view has focus.

`func onKeyPress(KeyEquivalent, phases: KeyPress.Phases, action: (KeyPress) ->
KeyPress.Result) -> some View`

Performs an action if the user presses a key on a hardware keyboard while the
view has focus.

`func onKeyPress(keys: Set<KeyEquivalent>, phases: KeyPress.Phases, action:
(KeyPress) -> KeyPress.Result) -> some View`

Performs an action if the user presses one or more keys on a hardware keyboard
while the view has focus.

`struct KeyPress`

Instance Method

# onKeyPress(keys:phases:action:)

Performs an action if the user presses one or more keys on a hardware keyboard
while the view has focus.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    func onKeyPress(
        keys: Set<KeyEquivalent>,
        phases: KeyPress.Phases = [.down, .repeat],
        action: @escaping (KeyPress) -> KeyPress.Result
    ) -> some View
    

##  Parameters

`keys`

    

A set of keys to match against incoming hardware keyboard events.

`phases`

    

The key-press phases to match (`.down`, `.repeat`, and `.up`). The default
value is `[.down, .repeat]`.

`action`

    

The action to perform. The action receives a value describing the matched key
event. Return `.handled` to consume the event and prevent further dispatch, or
`.ignored` to allow dispatch to continue.

## Return Value

A modified view that binds keyboard input when focused.

## See Also

### Responding to keyboard input

`func onKeyPress(KeyEquivalent, action: () -> KeyPress.Result) -> some View`

Performs an action if the user presses a key on a hardware keyboard while the
view has focus.

`func onKeyPress(phases: KeyPress.Phases, action: (KeyPress) ->
KeyPress.Result) -> some View`

Performs an action if the user presses any key on a hardware keyboard while
the view has focus.

`func onKeyPress(KeyEquivalent, phases: KeyPress.Phases, action: (KeyPress) ->
KeyPress.Result) -> some View`

Performs an action if the user presses a key on a hardware keyboard while the
view has focus.

`func onKeyPress(characters: CharacterSet, phases: KeyPress.Phases, action:
(KeyPress) -> KeyPress.Result) -> some View`

Performs an action if the user presses one or more keys on a hardware keyboard
while the view has focus.

`struct KeyPress`

Structure

# KeyPress

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    struct KeyPress

## Topics

### Getting the keypress

`let key: KeyEquivalent`

The key equivalent value for the pressed key.

`let characters: String`

The characters generated by the pressed key as if no modifier key applies.

`let modifiers: EventModifiers`

The set of modifier keys the user held in addition to the pressed key.

### Getting the phase of the keypress

`let phase: KeyPress.Phases`

The phase of the key-press event (`.down`, `.repeat`, or `.up`).

`struct Phases`

Options for matching different phases of a key-press event.

### Getting the result

`enum Result`

A result value returned from a key-press action that indicates whether the
action consumed the event.

## Relationships

### Conforms To

  * `CustomDebugStringConvertible`
  * `Sendable`

## See Also

### Responding to keyboard input

`func onKeyPress(KeyEquivalent, action: () -> KeyPress.Result) -> some View`

Performs an action if the user presses a key on a hardware keyboard while the
view has focus.

`func onKeyPress(phases: KeyPress.Phases, action: (KeyPress) ->
KeyPress.Result) -> some View`

Performs an action if the user presses any key on a hardware keyboard while
the view has focus.

`func onKeyPress(KeyEquivalent, phases: KeyPress.Phases, action: (KeyPress) ->
KeyPress.Result) -> some View`

Performs an action if the user presses a key on a hardware keyboard while the
view has focus.

`func onKeyPress(characters: CharacterSet, phases: KeyPress.Phases, action:
(KeyPress) -> KeyPress.Result) -> some View`

Performs an action if the user presses one or more keys on a hardware keyboard
while the view has focus.

`func onKeyPress(keys: Set<KeyEquivalent>, phases: KeyPress.Phases, action:
(KeyPress) -> KeyPress.Result) -> some View`

Performs an action if the user presses one or more keys on a hardware keyboard
while the view has focus.

Instance Method

# keyboardShortcut(_:)

Assigns a keyboard shortcut to the modified control.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    func keyboardShortcut(_ shortcut: KeyboardShortcut) -> some View
    

## Discussion

Pressing the control’s shortcut while the control is anywhere in the frontmost
window or scene, or anywhere in the macOS main menu, is equivalent to direct
interaction with the control to perform its primary action.

The target of a keyboard shortcut is resolved in a leading-to-trailing
traversal of one or more view hierarchies. On macOS, the system looks in the
key window first, then the main window, and then the command groups; on other
platforms, the system looks in the active scene, and then the command groups.

If multiple controls are associated with the same shortcut, the first one
found is used.

## See Also

### Creating keyboard shortcuts

`func keyboardShortcut(KeyboardShortcut?) -> some View`

Assigns an optional keyboard shortcut to the modified control.

`func keyboardShortcut(KeyEquivalent, modifiers: EventModifiers) -> some View`

Defines a keyboard shortcut and assigns it to the modified control.

`func keyboardShortcut(KeyEquivalent, modifiers: EventModifiers, localization:
KeyboardShortcut.Localization) -> some View`

Defines a keyboard shortcut and assigns it to the modified control.

`var keyboardShortcut: KeyboardShortcut?`

The keyboard shortcut that buttons in this environment will be triggered with.

`struct KeyboardShortcut`

Keyboard shortcuts describe combinations of keys on a keyboard that the user
can press in order to activate a button or toggle.

`struct KeyEquivalent`

Key equivalents consist of a letter, punctuation, or function key that can be
combined with an optional set of modifier keys to specify a keyboard shortcut.

`struct EventModifiers`

A set of key modifiers that you can add to a gesture.

Instance Method

# keyboardShortcut(_:)

Assigns an optional keyboard shortcut to the modified control.

iOS 15.4+  iPadOS 15.4+  macOS 12.3+  Mac Catalyst 15.4+  visionOS 1.0+

    
    
    func keyboardShortcut(_ shortcut: KeyboardShortcut?) -> some View
    

## Discussion

Pressing the control’s shortcut while the control is anywhere in the frontmost
window or scene, or anywhere in the macOS main menu, is equivalent to direct
interaction with the control to perform its primary action.

The target of a keyboard shortcut is resolved in a leading-to-trailing
traversal of one or more view hierarchies. On macOS, the system looks in the
key window first, then the main window, and then the command groups; on other
platforms, the system looks in the active scene, and then the command groups.

If multiple controls are associated with the same shortcut, the first one
found is used. If the provided shortcut is `nil`, the modifier will have no
effect.

## See Also

### Creating keyboard shortcuts

`func keyboardShortcut(KeyboardShortcut) -> some View`

Assigns a keyboard shortcut to the modified control.

`func keyboardShortcut(KeyEquivalent, modifiers: EventModifiers) -> some View`

Defines a keyboard shortcut and assigns it to the modified control.

`func keyboardShortcut(KeyEquivalent, modifiers: EventModifiers, localization:
KeyboardShortcut.Localization) -> some View`

Defines a keyboard shortcut and assigns it to the modified control.

`var keyboardShortcut: KeyboardShortcut?`

The keyboard shortcut that buttons in this environment will be triggered with.

`struct KeyboardShortcut`

Keyboard shortcuts describe combinations of keys on a keyboard that the user
can press in order to activate a button or toggle.

`struct KeyEquivalent`

Key equivalents consist of a letter, punctuation, or function key that can be
combined with an optional set of modifier keys to specify a keyboard shortcut.

`struct EventModifiers`

A set of key modifiers that you can add to a gesture.

Instance Method

# keyboardShortcut(_:modifiers:)

Defines a keyboard shortcut and assigns it to the modified control.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    func keyboardShortcut(
        _ key: KeyEquivalent,
        modifiers: EventModifiers = .command
    ) -> some View
    

## Discussion

Pressing the control’s shortcut while the control is anywhere in the frontmost
window or scene, or anywhere in the macOS main menu, is equivalent to direct
interaction with the control to perform its primary action.

The target of a keyboard shortcut is resolved in a leading-to-trailing, depth-
first traversal of one or more view hierarchies. On macOS, the system looks in
the key window first, then the main window, and then the command groups; on
other platforms, the system looks in the active scene, and then the command
groups.

If multiple controls are associated with the same shortcut, the first one
found is used.

The default localization configuration is set to `automatic`.

## See Also

### Creating keyboard shortcuts

`func keyboardShortcut(KeyboardShortcut) -> some View`

Assigns a keyboard shortcut to the modified control.

`func keyboardShortcut(KeyboardShortcut?) -> some View`

Assigns an optional keyboard shortcut to the modified control.

`func keyboardShortcut(KeyEquivalent, modifiers: EventModifiers, localization:
KeyboardShortcut.Localization) -> some View`

Defines a keyboard shortcut and assigns it to the modified control.

`var keyboardShortcut: KeyboardShortcut?`

The keyboard shortcut that buttons in this environment will be triggered with.

`struct KeyboardShortcut`

Keyboard shortcuts describe combinations of keys on a keyboard that the user
can press in order to activate a button or toggle.

`struct KeyEquivalent`

Key equivalents consist of a letter, punctuation, or function key that can be
combined with an optional set of modifier keys to specify a keyboard shortcut.

`struct EventModifiers`

A set of key modifiers that you can add to a gesture.

Instance Method

# keyboardShortcut(_:modifiers:localization:)

Defines a keyboard shortcut and assigns it to the modified control.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    func keyboardShortcut(
        _ key: KeyEquivalent,
        modifiers: EventModifiers = .command,
        localization: KeyboardShortcut.Localization
    ) -> some View
    

## Discussion

Pressing the control’s shortcut while the control is anywhere in the frontmost
window or scene, or anywhere in the macOS main menu, is equivalent to direct
interaction with the control to perform its primary action.

The target of a keyboard shortcut is resolved in a leading-to-trailing, depth-
first traversal of one or more view hierarchies. On macOS, the system looks in
the key window first, then the main window, and then the command groups; on
other platforms, the system looks in the active scene, and then the command
groups.

If multiple controls are associated with the same shortcut, the first one
found is used.

### Localization

Provide a `localization` value to specify how this shortcut should be
localized. Given that `key` is always defined in relation to the US-English
keyboard layout, it might be hard to reach on different international layouts.
For example the shortcut `⌘[` works well for the US layout but is hard to
reach for German users, where `[` is available by pressing `⌥5`, making users
type `⌥⌘5`. The automatic keyboard shortcut remapping re-assigns the shortcut
to an appropriate replacement, `⌘Ö` in this case.

Certain shortcuts carry information about directionality. For instance, `⌘[`
can reveal a previous view. Following the layout direction of the UI, this
shortcut will be automatically mirrored to `⌘]`. However, this does not apply
to items such as “Align Left `⌘{`”, which will be “left” independently of the
layout direction. When the shortcut shouldn’t follow the directionality of the
UI, but rather be the same in both right-to-left and left-to-right directions,
using `withoutMirroring` will prevent the system from flipping it.

Lastly, providing the option `custom` disables the automatic localization for
this shortcut to tell the system that internationalization is taken care of in
a different way.

## See Also

### Creating keyboard shortcuts

`func keyboardShortcut(KeyboardShortcut) -> some View`

Assigns a keyboard shortcut to the modified control.

`func keyboardShortcut(KeyboardShortcut?) -> some View`

Assigns an optional keyboard shortcut to the modified control.

`func keyboardShortcut(KeyEquivalent, modifiers: EventModifiers) -> some View`

Defines a keyboard shortcut and assigns it to the modified control.

`var keyboardShortcut: KeyboardShortcut?`

The keyboard shortcut that buttons in this environment will be triggered with.

`struct KeyboardShortcut`

Keyboard shortcuts describe combinations of keys on a keyboard that the user
can press in order to activate a button or toggle.

`struct KeyEquivalent`

Key equivalents consist of a letter, punctuation, or function key that can be
combined with an optional set of modifier keys to specify a keyboard shortcut.

`struct EventModifiers`

A set of key modifiers that you can add to a gesture.

Instance Property

# keyboardShortcut

The keyboard shortcut that buttons in this environment will be triggered with.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    var keyboardShortcut: KeyboardShortcut? { get }

## Discussion

This is particularly useful in button styles when a button’s appearance
depends on the shortcut associated with it. On macOS, for example, when a
button is bound to the Return key, it is typically drawn with a special
emphasis. This happens automatically when using the built-in button styles,
and can be implemented manually in custom styles using this environment key:

If no keyboard shortcut has been applied to the view or its ancestor, then the
environment value will be `nil`.

## See Also

### Creating keyboard shortcuts

`func keyboardShortcut(KeyboardShortcut) -> some View`

Assigns a keyboard shortcut to the modified control.

`func keyboardShortcut(KeyboardShortcut?) -> some View`

Assigns an optional keyboard shortcut to the modified control.

`func keyboardShortcut(KeyEquivalent, modifiers: EventModifiers) -> some View`

Defines a keyboard shortcut and assigns it to the modified control.

`func keyboardShortcut(KeyEquivalent, modifiers: EventModifiers, localization:
KeyboardShortcut.Localization) -> some View`

Defines a keyboard shortcut and assigns it to the modified control.

`struct KeyboardShortcut`

Keyboard shortcuts describe combinations of keys on a keyboard that the user
can press in order to activate a button or toggle.

`struct KeyEquivalent`

Key equivalents consist of a letter, punctuation, or function key that can be
combined with an optional set of modifier keys to specify a keyboard shortcut.

`struct EventModifiers`

A set of key modifiers that you can add to a gesture.

Structure

# KeyboardShortcut

Keyboard shortcuts describe combinations of keys on a keyboard that the user
can press in order to activate a button or toggle.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    struct KeyboardShortcut

## Topics

### Getting standard shortcuts

`static let cancelAction: KeyboardShortcut`

The standard keyboard shortcut for cancelling the in-progress action or
dismissing a prompt, consisting of the Escape (⎋) key and no modifiers.

`static let defaultAction: KeyboardShortcut`

The standard keyboard shortcut for the default button, consisting of the
Return (↩) key and no modifiers.

### Creating a shortcut

`init(KeyEquivalent, modifiers: EventModifiers)`

Creates a new keyboard shortcut with the given key equivalent and set of
modifier keys.

`var key: KeyEquivalent`

The key equivalent that the user presses in conjunction with any specified
modifier keys to activate the shortcut.

`var modifiers: EventModifiers`

The modifier keys that the user presses in conjunction with a key equivalent
to activate the shortcut.

### Creating a localized shortcut

`init(KeyEquivalent, modifiers: EventModifiers, localization:
KeyboardShortcut.Localization)`

Creates a new keyboard shortcut with the given key equivalent and set of
modifier keys.

`var localization: KeyboardShortcut.Localization`

The localization strategy to apply to this shortcut.

`struct Localization`

Options for how a keyboard shortcut participates in automatic localization.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Creating keyboard shortcuts

`func keyboardShortcut(KeyboardShortcut) -> some View`

Assigns a keyboard shortcut to the modified control.

`func keyboardShortcut(KeyboardShortcut?) -> some View`

Assigns an optional keyboard shortcut to the modified control.

`func keyboardShortcut(KeyEquivalent, modifiers: EventModifiers) -> some View`

Defines a keyboard shortcut and assigns it to the modified control.

`func keyboardShortcut(KeyEquivalent, modifiers: EventModifiers, localization:
KeyboardShortcut.Localization) -> some View`

Defines a keyboard shortcut and assigns it to the modified control.

`var keyboardShortcut: KeyboardShortcut?`

The keyboard shortcut that buttons in this environment will be triggered with.

`struct KeyEquivalent`

Key equivalents consist of a letter, punctuation, or function key that can be
combined with an optional set of modifier keys to specify a keyboard shortcut.

`struct EventModifiers`

A set of key modifiers that you can add to a gesture.

Structure

# KeyEquivalent

Key equivalents consist of a letter, punctuation, or function key that can be
combined with an optional set of modifier keys to specify a keyboard shortcut.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 17.0+  visionOS
1.0+

    
    
    struct KeyEquivalent

## Overview

Key equivalents are used to establish keyboard shortcuts to app functionality.
Any key can be used as a key equivalent as long as pressing it produces a
single character value. Key equivalents are typically initialized using a
single-character string literal, with constants for unprintable or hard-to-
type values.

The modifier keys necessary to type a key equivalent are factored in to the
resulting keyboard shortcut. That is, a key equivalent whose raw value is the
capitalized string “A” corresponds with the keyboard shortcut Command-Shift-A.
The exact mapping may depend on the keyboard layout—for example, a key
equivalent with the character value “}” produces a shortcut equivalent to
Command-Shift-] on ANSI keyboards, but would produce a different shortcut for
keyboard layouts where punctuation characters are in different locations.

## Topics

### Getting arrow keys

`static let upArrow: KeyEquivalent`

Up Arrow (U+F700)

`static let downArrow: KeyEquivalent`

Down Arrow (U+F701)

`static let leftArrow: KeyEquivalent`

Left Arrow (U+F702)

`static let rightArrow: KeyEquivalent`

Right Arrow (U+F703)

### Getting other special keys

`static let clear: KeyEquivalent`

Clear (U+F739)

`static let delete: KeyEquivalent`

Delete (U+0008)

`static let deleteForward: KeyEquivalent`

Delete Forward (U+F728)

`static let end: KeyEquivalent`

End (U+F72B)

`static let escape: KeyEquivalent`

Escape (U+001B)

`static let home: KeyEquivalent`

Home (U+F729)

`static let pageDown: KeyEquivalent`

Page Down (U+F72D)

`static let pageUp: KeyEquivalent`

Page Up (U+F72C)

`static let `return`: KeyEquivalent`

Return (U+000D)

`static let space: KeyEquivalent`

Space (U+0020)

`static let tab: KeyEquivalent`

Tab (U+0009)

### Creating a key equivalent

`init(Character)`

Creates a new key equivalent from the given character value.

`var character: Character`

The character value that the key equivalent represents.

## Relationships

### Conforms To

  * `Equatable`
  * `ExpressibleByExtendedGraphemeClusterLiteral`
  * `ExpressibleByUnicodeScalarLiteral`
  * `Hashable`
  * `Sendable`

## See Also

### Creating keyboard shortcuts

`func keyboardShortcut(KeyboardShortcut) -> some View`

Assigns a keyboard shortcut to the modified control.

`func keyboardShortcut(KeyboardShortcut?) -> some View`

Assigns an optional keyboard shortcut to the modified control.

`func keyboardShortcut(KeyEquivalent, modifiers: EventModifiers) -> some View`

Defines a keyboard shortcut and assigns it to the modified control.

`func keyboardShortcut(KeyEquivalent, modifiers: EventModifiers, localization:
KeyboardShortcut.Localization) -> some View`

Defines a keyboard shortcut and assigns it to the modified control.

`var keyboardShortcut: KeyboardShortcut?`

The keyboard shortcut that buttons in this environment will be triggered with.

`struct KeyboardShortcut`

Keyboard shortcuts describe combinations of keys on a keyboard that the user
can press in order to activate a button or toggle.

`struct EventModifiers`

A set of key modifiers that you can add to a gesture.

Structure

# EventModifiers

A set of key modifiers that you can add to a gesture.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct EventModifiers

## Topics

### Getting modifier keys

`static let all: EventModifiers`

All possible modifier keys.

`static let capsLock: EventModifiers`

The Caps Lock key.

`static let command: EventModifiers`

The Command key.

`static let control: EventModifiers`

The Control key.

`static let numericPad: EventModifiers`

Any key on the numeric keypad.

`static let option: EventModifiers`

The Option key.

`static let shift: EventModifiers`

The Shift key.

### Creating a set of options

`init(rawValue: Int)`

Creates a new set from a raw value.

`let rawValue: Int`

The raw value.

### Deprecated modifiers

`static let function: EventModifiers`

The Function key.

Deprecated

## Relationships

### Conforms To

  * `Equatable`
  * `ExpressibleByArrayLiteral`
  * `OptionSet`
  * `RawRepresentable`
  * `Sendable`
  * `SetAlgebra`

## See Also

### Creating keyboard shortcuts

`func keyboardShortcut(KeyboardShortcut) -> some View`

Assigns a keyboard shortcut to the modified control.

`func keyboardShortcut(KeyboardShortcut?) -> some View`

Assigns an optional keyboard shortcut to the modified control.

`func keyboardShortcut(KeyEquivalent, modifiers: EventModifiers) -> some View`

Defines a keyboard shortcut and assigns it to the modified control.

`func keyboardShortcut(KeyEquivalent, modifiers: EventModifiers, localization:
KeyboardShortcut.Localization) -> some View`

Defines a keyboard shortcut and assigns it to the modified control.

`var keyboardShortcut: KeyboardShortcut?`

The keyboard shortcut that buttons in this environment will be triggered with.

`struct KeyboardShortcut`

Keyboard shortcuts describe combinations of keys on a keyboard that the user
can press in order to activate a button or toggle.

`struct KeyEquivalent`

Key equivalents consist of a letter, punctuation, or function key that can be
combined with an optional set of modifier keys to specify a keyboard shortcut.

Instance Method

# onHover(perform:)

Adds an action to perform when the user moves the pointer over or away from
the view’s frame.

iOS 13.4+  iPadOS 13.4+  macOS 10.15+  Mac Catalyst 13.4+  visionOS 1.0+

    
    
    func onHover(perform action: @escaping (Bool) -> Void) -> some View
    

##  Parameters

`action`

    

The action to perform whenever the pointer enters or exits this view’s frame.
If the pointer is in the view’s frame, the `action` closure passes `true` as a
parameter; otherwise, `false`.

## Return Value

A view that triggers `action` when the pointer enters or exits this view’s
frame.

## Discussion

Calling this method defines a region for detecting pointer movement with the
size and position of this view.

## See Also

### Responding to hover events

`func onContinuousHover(coordinateSpace: some CoordinateSpaceProtocol,
perform: (HoverPhase) -> Void) -> some View`

Adds an action to perform when the pointer enters, moves within, and exits the
view’s bounds.

`func hoverEffect(HoverEffect, isEnabled: Bool) -> some View`

Applies a hover effect to this view.

`func hoverEffectDisabled(Bool) -> some View`

Adds a condition that controls whether this view can display hover effects.

`func defaultHoverEffect(HoverEffect?) -> some View`

Sets the default hover effect to use for views within this view.

`var isHoverEffectEnabled: Bool`

A Boolean value that indicates whether the view associated with this
environment allows hover effects to be displayed.

`enum HoverPhase`

The current hovering state and value of the pointer.

Instance Method

# onContinuousHover(coordinateSpace:perform:)

Adds an action to perform when the pointer enters, moves within, and exits the
view’s bounds.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    func onContinuousHover(
        coordinateSpace: some CoordinateSpaceProtocol = .local,
        perform action: @escaping (HoverPhase) -> Void
    ) -> some View
    

##  Parameters

`coordinateSpace`

    

The coordinate space for the location values. The default value is
`CoordinateSpace.local`.

`action`

    

The action to perform whenever the pointer enters, moves within, or exits the
view’s bounds. The closure takes a `phase` input that has the value
`HoverPhase.active(_:)` and contains the pointer’s coordinates if the pointer
is within the view’s bounds. The closure receives the `HoverPhase.ended` phase
when the pointer leaves the view’s bounds.

## Return Value

A view that calls `action` when the pointer enters, moves within, or exits the
view’s bounds.

## Discussion

Use this modifier to define a region for detecting pointer movement with a
view. The following example updates a small rectangle’s position and style by
modifying `hoverLocation` and `isHovering` as the pointer moves within the
larger, red rectangle:

## See Also

### Responding to hover events

`func onHover(perform: (Bool) -> Void) -> some View`

Adds an action to perform when the user moves the pointer over or away from
the view’s frame.

`func hoverEffect(HoverEffect, isEnabled: Bool) -> some View`

Applies a hover effect to this view.

`func hoverEffectDisabled(Bool) -> some View`

Adds a condition that controls whether this view can display hover effects.

`func defaultHoverEffect(HoverEffect?) -> some View`

Sets the default hover effect to use for views within this view.

`var isHoverEffectEnabled: Bool`

A Boolean value that indicates whether the view associated with this
environment allows hover effects to be displayed.

`enum HoverPhase`

The current hovering state and value of the pointer.

Instance Method

# hoverEffect(_:isEnabled:)

Applies a hover effect to this view.

iOS 17.0+  iPadOS 17.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS 1.0+

    
    
    func hoverEffect(
        _ effect: HoverEffect = .automatic,
        isEnabled: Bool = true
    ) -> some View
    

##  Parameters

`effect`

    

The effect to apply to this view.

`isEnabled`

    

Whether the effect is enabled or not.

## Return Value

A new view that applies a hover effect to `self`.

## Discussion

By default, `automatic` is used. You can control the behavior of the automatic
effect with the `defaultHoverEffect(_:)` modifier.

## See Also

### Responding to hover events

`func onHover(perform: (Bool) -> Void) -> some View`

Adds an action to perform when the user moves the pointer over or away from
the view’s frame.

`func onContinuousHover(coordinateSpace: some CoordinateSpaceProtocol,
perform: (HoverPhase) -> Void) -> some View`

Adds an action to perform when the pointer enters, moves within, and exits the
view’s bounds.

`func hoverEffectDisabled(Bool) -> some View`

Adds a condition that controls whether this view can display hover effects.

`func defaultHoverEffect(HoverEffect?) -> some View`

Sets the default hover effect to use for views within this view.

`var isHoverEffectEnabled: Bool`

A Boolean value that indicates whether the view associated with this
environment allows hover effects to be displayed.

`enum HoverPhase`

The current hovering state and value of the pointer.

Instance Method

# hoverEffectDisabled(_:)

Adds a condition that controls whether this view can display hover effects.

iOS 17.0+  iPadOS 17.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS 1.0+

    
    
    func hoverEffectDisabled(_ disabled: Bool = true) -> some View
    

##  Parameters

`disabled`

    

A Boolean value that determines whether this view can display hover effects.

## Return Value

A view that controls whether hover effects can be displayed in this view.

## Discussion

The higher views in a view hierarchy can override the value you set on this
view. In the following example, the button does not display a hover effect
because the outer `hoverEffectDisabled(_:)` modifier overrides the inner one:

## See Also

### Responding to hover events

`func onHover(perform: (Bool) -> Void) -> some View`

Adds an action to perform when the user moves the pointer over or away from
the view’s frame.

`func onContinuousHover(coordinateSpace: some CoordinateSpaceProtocol,
perform: (HoverPhase) -> Void) -> some View`

Adds an action to perform when the pointer enters, moves within, and exits the
view’s bounds.

`func hoverEffect(HoverEffect, isEnabled: Bool) -> some View`

Applies a hover effect to this view.

`func defaultHoverEffect(HoverEffect?) -> some View`

Sets the default hover effect to use for views within this view.

`var isHoverEffectEnabled: Bool`

A Boolean value that indicates whether the view associated with this
environment allows hover effects to be displayed.

`enum HoverPhase`

The current hovering state and value of the pointer.

Instance Method

# defaultHoverEffect(_:)

Sets the default hover effect to use for views within this view.

iOS 17.0+  iPadOS 17.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS 1.0+

    
    
    func defaultHoverEffect(_ effect: HoverEffect?) -> some View
    

##  Parameters

`effect`

    

The default hover effect to use for views within this view.

## Return Value

A view that uses this effect as the default hover effect.

## Discussion

Use this modifier to set a specific hover effect for all views with the
`hoverEffect(_:)` modifier applied within a view. The default effect is
typically used when no `HoverEffect` was provided or if `automatic` is
specified.

For example, this view uses `highlight` for both the red and green Color
views:

This also works for customizing the default hover effect in views like
`Button`s when using a SwiftUI-defined style like `ButtonStyle/bordered`,
which can provide a hover effect by default. For example, this view replaces
the hover effect for a `Button` with `highlight`:

Use a `nil` effect to indicate that the default hover effect should not be
modified.

## See Also

### Responding to hover events

`func onHover(perform: (Bool) -> Void) -> some View`

Adds an action to perform when the user moves the pointer over or away from
the view’s frame.

`func onContinuousHover(coordinateSpace: some CoordinateSpaceProtocol,
perform: (HoverPhase) -> Void) -> some View`

Adds an action to perform when the pointer enters, moves within, and exits the
view’s bounds.

`func hoverEffect(HoverEffect, isEnabled: Bool) -> some View`

Applies a hover effect to this view.

`func hoverEffectDisabled(Bool) -> some View`

Adds a condition that controls whether this view can display hover effects.

`var isHoverEffectEnabled: Bool`

A Boolean value that indicates whether the view associated with this
environment allows hover effects to be displayed.

`enum HoverPhase`

The current hovering state and value of the pointer.

Instance Property

# isHoverEffectEnabled

A Boolean value that indicates whether the view associated with this
environment allows hover effects to be displayed.

iOS 17.0+  iPadOS 17.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS 1.0+

    
    
    var isHoverEffectEnabled: Bool { get set }

## Discussion

The default value is `true`.

## See Also

### Responding to hover events

`func onHover(perform: (Bool) -> Void) -> some View`

Adds an action to perform when the user moves the pointer over or away from
the view’s frame.

`func onContinuousHover(coordinateSpace: some CoordinateSpaceProtocol,
perform: (HoverPhase) -> Void) -> some View`

Adds an action to perform when the pointer enters, moves within, and exits the
view’s bounds.

`func hoverEffect(HoverEffect, isEnabled: Bool) -> some View`

Applies a hover effect to this view.

`func hoverEffectDisabled(Bool) -> some View`

Adds a condition that controls whether this view can display hover effects.

`func defaultHoverEffect(HoverEffect?) -> some View`

Sets the default hover effect to use for views within this view.

`enum HoverPhase`

The current hovering state and value of the pointer.

Enumeration

# HoverPhase

The current hovering state and value of the pointer.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  visionOS
1.0+

    
    
    @frozen
    enum HoverPhase

## Overview

When you use the `onContinuousHover(coordinateSpace:perform:)` modifier, you
can handle the hovering state using the `action` closure. SwiftUI calls the
closure with a phase value to indicate the current hovering state. The
following example updates `hoverLocation` and `isHovering` based on the phase
provided to the closure:

## Topics

### Getting hover phases

`case active(CGPoint)`

The pointer’s location moved to the specified point within the view.

`case ended`

The pointer exited the view.

## Relationships

### Conforms To

  * `Equatable`
  * `Sendable`

## See Also

### Responding to hover events

`func onHover(perform: (Bool) -> Void) -> some View`

Adds an action to perform when the user moves the pointer over or away from
the view’s frame.

`func onContinuousHover(coordinateSpace: some CoordinateSpaceProtocol,
perform: (HoverPhase) -> Void) -> some View`

Adds an action to perform when the pointer enters, moves within, and exits the
view’s bounds.

`func hoverEffect(HoverEffect, isEnabled: Bool) -> some View`

Applies a hover effect to this view.

`func hoverEffectDisabled(Bool) -> some View`

Adds a condition that controls whether this view can display hover effects.

`func defaultHoverEffect(HoverEffect?) -> some View`

Sets the default hover effect to use for views within this view.

`var isHoverEffectEnabled: Bool`

A Boolean value that indicates whether the view associated with this
environment allows hover effects to be displayed.

Instance Method

# hoverEffect(_:)

Applies a hover effect to this view.

iOS 13.4+  iPadOS 13.4+  Mac Catalyst 13.4+  tvOS 16.0+  visionOS 1.0+

    
    
    func hoverEffect(_ effect: HoverEffect = .automatic) -> some View
    

##  Parameters

`effect`

    

The effect to apply to this view.

`isEnabled`

    

Whether the effect is enabled or not.

## Return Value

A new view that applies a hover effect to `self`.

## Discussion

By default, `automatic` is used. You can control the behavior of the automatic
effect with the `defaultHoverEffect(_:)` modifier.

## See Also

### Changing view appearance for hover events

`struct HoverEffect`

An effect applied when the pointer hovers over a view.

Structure

# HoverEffect

An effect applied when the pointer hovers over a view.

iOS 13.4+  iPadOS 13.4+  Mac Catalyst 13.4+  tvOS 16.0+  visionOS 1.0+

    
    
    struct HoverEffect

## Topics

### Getting hover effects

`static let automatic: HoverEffect`

An effect that attempts to determine the effect automatically. This is the
default effect.

`static let highlight: HoverEffect`

An effect that morphs the pointer into a platter behind the view and shows a
light source indicating position.

`static let lift: HoverEffect`

An effect that slides the pointer under the view and disappears as the view
scales up and gains a shadow.

## See Also

### Changing view appearance for hover events

`func hoverEffect(HoverEffect) -> some View`

Applies a hover effect to this view.

Instance Method

# onSubmit(of:_:)

Adds an action to perform when the user submits a value to this view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func onSubmit(
        of triggers: SubmitTriggers = .text,
        _ action: @escaping (() -> Void)
    ) -> some View
    

##  Parameters

`triggers`

    

The triggers that should invoke the provided action.

`action`

    

The action to perform on submission of a value.

## Discussion

Different views may have different triggers for the provided action. A
`TextField`, or `SecureField` will trigger this action when the user hits the
hardware or software return key. This modifier may also bind this action to a
default action keyboard shortcut. You may set this action on an individual
view or an entire view hierarchy.

You can use the `submitScope(_:)` modifier to stop a submit trigger from a
control from propagating higher up in the view hierarchy to higher
`View.onSubmit(of:_:)` modifiers.

You can use different submit triggers to filter the types of triggers that
should invoke the provided submission action. For example, you may provide a
value of `search` to only hear submission triggers that originate from search
fields vended by searchable modifiers.

## See Also

### Responding to submission events

`func submitScope(Bool) -> some View`

Prevents submission triggers originating from this view to invoke a submission
action configured by a submission modifier higher up in the view hierarchy.

`struct SubmitTriggers`

A type that defines various triggers that result in the firing of a submission
action.

Instance Method

# submitScope(_:)

Prevents submission triggers originating from this view to invoke a submission
action configured by a submission modifier higher up in the view hierarchy.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func submitScope(_ isBlocking: Bool = true) -> some View
    

##  Parameters

`isBlocking`

    

A Boolean that indicates whether this scope is actively blocking submission
triggers from reaching higher submission actions.

## Discussion

Use this modifier when you want to avoid specific views from initiating a
submission action configured by the `onSubmit(of:_:)` modifier. In the example
below, the tag field doesn’t trigger the submission of the form:

## See Also

### Responding to submission events

`func onSubmit(of: SubmitTriggers, (() -> Void)) -> some View`

Adds an action to perform when the user submits a value to this view.

`struct SubmitTriggers`

A type that defines various triggers that result in the firing of a submission
action.

Structure

# SubmitTriggers

A type that defines various triggers that result in the firing of a submission
action.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    struct SubmitTriggers

## Overview

These triggers may be provided to the `onSubmit(of:_:)` modifier to alter
which types of user behaviors trigger a provided submission action.

## Topics

### Getting submit triggers

`static let search: SubmitTriggers`

Defines triggers originating from search fields constructed from searchable
modifiers.

`static let text: SubmitTriggers`

Defines triggers originating from text input controls like `TextField` and
`SecureField`.

### Creating a set of options

`init(rawValue: SubmitTriggers.RawValue)`

Creates a set of submit triggers.

## Relationships

### Conforms To

  * `Equatable`
  * `ExpressibleByArrayLiteral`
  * `OptionSet`
  * `RawRepresentable`
  * `Sendable`
  * `SetAlgebra`

## See Also

### Responding to submission events

`func onSubmit(of: SubmitTriggers, (() -> Void)) -> some View`

Adds an action to perform when the user submits a value to this view.

`func submitScope(Bool) -> some View`

Prevents submission triggers originating from this view to invoke a submission
action configured by a submission modifier higher up in the view hierarchy.

Instance Method

# submitLabel(_:)

Sets the submit label for this view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func submitLabel(_ submitLabel: SubmitLabel) -> some View
    

##  Parameters

`submitLabel`

    

One of the cases specified in `SubmitLabel`.

## Discussion

## See Also

### Labeling a submission event

`struct SubmitLabel`

A semantic label describing the label of submission within a view hierarchy.

Structure

# SubmitLabel

A semantic label describing the label of submission within a view hierarchy.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    struct SubmitLabel

## Overview

A submit label is a description of a submission action provided to a view
hierarchy using the `onSubmit(of:_:)` modifier.

## Topics

### Getting submission labels

`static var `continue`: SubmitLabel`

Defines a submit label with text of “Continue”.

`static var done: SubmitLabel`

Defines a submit label with text of “Done”.

`static var go: SubmitLabel`

Defines a submit label with text of “Go”.

`static var join: SubmitLabel`

Defines a submit label with text of “Join”.

`static var next: SubmitLabel`

Defines a submit label with text of “Next”.

`static var `return`: SubmitLabel`

Defines a submit label with text of “Return”.

`static var route: SubmitLabel`

Defines a submit label with text of “Route”.

`static var search: SubmitLabel`

Defines a submit label with text of “Search”.

`static var send: SubmitLabel`

Defines a submit label with text of “Send”.

## Relationships

### Conforms To

  * `Sendable`

## See Also

### Labeling a submission event

`func submitLabel(SubmitLabel) -> some View`

Sets the submit label for this view.

Instance Method

# onMoveCommand(perform:)

Adds an action to perform in response to a move command, like when the user
presses an arrow key on a Mac keyboard, or taps the edge of the Siri Remote
when controlling an Apple TV.

macOS 10.15+  tvOS 13.0+

    
    
    func onMoveCommand(perform action: ((MoveCommandDirection) -> Void)?) -> some View
    

## See Also

### Responding to commands

`func onDeleteCommand(perform: (() -> Void)?) -> some View`

Adds an action to perform in response to the system’s Delete command, or
pressing either the ⌫ (backspace) or ⌦ (forward delete) keys while the view
has focus.

`func pageCommand<V>(value: Binding<V>, in: ClosedRange<V>, step: V) -> some
View`

Steps a value through a range in response to page up or page down commands.

`func onExitCommand(perform: (() -> Void)?) -> some View`

Sets up an action that triggers in response to receiving the exit command
while the view has focus.

`func onPlayPauseCommand(perform: (() -> Void)?) -> some View`

Adds an action to perform in response to the system’s Play/Pause command.

`func onCommand(Selector, perform: (() -> Void)?) -> some View`

Adds an action to perform in response to the given selector.

`enum MoveCommandDirection`

Specifies the direction of an arrow key movement.

Instance Method

# onDeleteCommand(perform:)

Adds an action to perform in response to the system’s Delete command, or
pressing either the ⌫ (backspace) or ⌦ (forward delete) keys while the view
has focus.

macOS 10.15+

    
    
    func onDeleteCommand(perform action: (() -> Void)?) -> some View
    

## See Also

### Responding to commands

`func onMoveCommand(perform: ((MoveCommandDirection) -> Void)?) -> some View`

Adds an action to perform in response to a move command, like when the user
presses an arrow key on a Mac keyboard, or taps the edge of the Siri Remote
when controlling an Apple TV.

`func pageCommand<V>(value: Binding<V>, in: ClosedRange<V>, step: V) -> some
View`

Steps a value through a range in response to page up or page down commands.

`func onExitCommand(perform: (() -> Void)?) -> some View`

Sets up an action that triggers in response to receiving the exit command
while the view has focus.

`func onPlayPauseCommand(perform: (() -> Void)?) -> some View`

Adds an action to perform in response to the system’s Play/Pause command.

`func onCommand(Selector, perform: (() -> Void)?) -> some View`

Adds an action to perform in response to the given selector.

`enum MoveCommandDirection`

Specifies the direction of an arrow key movement.

Instance Method

# pageCommand(value:in:step:)

Steps a value through a range in response to page up or page down commands.

tvOS 14.3+

    
    
    func pageCommand<V>(
        value: Binding<V>,
        in bounds: ClosedRange<V>,
        step: V = 1
    ) -> some View where V : BinaryInteger
    

##  Parameters

`value`

    

A `Binding` to the value to modify when the user pages up or down.

`bounds`

    

A closed range that specifies the upper and lower bounds of `value`.

`step`

    

The amount by which to increment or decrement `value`. Defaults to 1.

## Discussion

Use this command to step through sections of a data model associated with a
view by providing a binding to a value, a range, and step. If taking another
step would cause the value to exceed the bounds, then the value remains
unchanged.

On tvOS, the user triggers ‘pageUp’ and ‘pageDown’ commands by pressing a
dedicated button on a connected remote. For example, you can let a user page
through a TV programming guide using the channel buttons:

## See Also

### Responding to commands

`func onMoveCommand(perform: ((MoveCommandDirection) -> Void)?) -> some View`

Adds an action to perform in response to a move command, like when the user
presses an arrow key on a Mac keyboard, or taps the edge of the Siri Remote
when controlling an Apple TV.

`func onDeleteCommand(perform: (() -> Void)?) -> some View`

Adds an action to perform in response to the system’s Delete command, or
pressing either the ⌫ (backspace) or ⌦ (forward delete) keys while the view
has focus.

`func onExitCommand(perform: (() -> Void)?) -> some View`

Sets up an action that triggers in response to receiving the exit command
while the view has focus.

`func onPlayPauseCommand(perform: (() -> Void)?) -> some View`

Adds an action to perform in response to the system’s Play/Pause command.

`func onCommand(Selector, perform: (() -> Void)?) -> some View`

Adds an action to perform in response to the given selector.

`enum MoveCommandDirection`

Specifies the direction of an arrow key movement.

Instance Method

# onExitCommand(perform:)

Sets up an action that triggers in response to receiving the exit command
while the view has focus.

macOS 10.15+  tvOS 13.0+

    
    
    func onExitCommand(perform action: (() -> Void)?) -> some View
    

## Discussion

The user generates an exit command by pressing the Menu button on tvOS, or the
escape key on macOS.

## See Also

### Responding to commands

`func onMoveCommand(perform: ((MoveCommandDirection) -> Void)?) -> some View`

Adds an action to perform in response to a move command, like when the user
presses an arrow key on a Mac keyboard, or taps the edge of the Siri Remote
when controlling an Apple TV.

`func onDeleteCommand(perform: (() -> Void)?) -> some View`

Adds an action to perform in response to the system’s Delete command, or
pressing either the ⌫ (backspace) or ⌦ (forward delete) keys while the view
has focus.

`func pageCommand<V>(value: Binding<V>, in: ClosedRange<V>, step: V) -> some
View`

Steps a value through a range in response to page up or page down commands.

`func onPlayPauseCommand(perform: (() -> Void)?) -> some View`

Adds an action to perform in response to the system’s Play/Pause command.

`func onCommand(Selector, perform: (() -> Void)?) -> some View`

Adds an action to perform in response to the given selector.

`enum MoveCommandDirection`

Specifies the direction of an arrow key movement.

Instance Method

# onPlayPauseCommand(perform:)

Adds an action to perform in response to the system’s Play/Pause command.

tvOS 13.0+

    
    
    func onPlayPauseCommand(perform action: (() -> Void)?) -> some View
    

## See Also

### Responding to commands

`func onMoveCommand(perform: ((MoveCommandDirection) -> Void)?) -> some View`

Adds an action to perform in response to a move command, like when the user
presses an arrow key on a Mac keyboard, or taps the edge of the Siri Remote
when controlling an Apple TV.

`func onDeleteCommand(perform: (() -> Void)?) -> some View`

Adds an action to perform in response to the system’s Delete command, or
pressing either the ⌫ (backspace) or ⌦ (forward delete) keys while the view
has focus.

`func pageCommand<V>(value: Binding<V>, in: ClosedRange<V>, step: V) -> some
View`

Steps a value through a range in response to page up or page down commands.

`func onExitCommand(perform: (() -> Void)?) -> some View`

Sets up an action that triggers in response to receiving the exit command
while the view has focus.

`func onCommand(Selector, perform: (() -> Void)?) -> some View`

Adds an action to perform in response to the given selector.

`enum MoveCommandDirection`

Specifies the direction of an arrow key movement.

Instance Method

# onCommand(_:perform:)

Adds an action to perform in response to the given selector.

macOS 10.15+

    
    
    func onCommand(
        _ selector: Selector,
        perform action: (() -> Void)?
    ) -> some View
    

##  Parameters

`selector`

    

The selector to register for `action`.

`action`

    

The action to perform. If `action` is `nil`, `command` keeps its association
with this view but doesn’t trigger.

## Return Value

A view that triggers `action` when the `command` occurs.

## Discussion

This view or one of the views it contains must be in focus in order for the
action to trigger. Other actions for the same command on views _closer_ to the
view in focus take priority, potentially overriding this action.

## See Also

### Responding to commands

`func onMoveCommand(perform: ((MoveCommandDirection) -> Void)?) -> some View`

Adds an action to perform in response to a move command, like when the user
presses an arrow key on a Mac keyboard, or taps the edge of the Siri Remote
when controlling an Apple TV.

`func onDeleteCommand(perform: (() -> Void)?) -> some View`

Adds an action to perform in response to the system’s Delete command, or
pressing either the ⌫ (backspace) or ⌦ (forward delete) keys while the view
has focus.

`func pageCommand<V>(value: Binding<V>, in: ClosedRange<V>, step: V) -> some
View`

Steps a value through a range in response to page up or page down commands.

`func onExitCommand(perform: (() -> Void)?) -> some View`

Sets up an action that triggers in response to receiving the exit command
while the view has focus.

`func onPlayPauseCommand(perform: (() -> Void)?) -> some View`

Adds an action to perform in response to the system’s Play/Pause command.

`enum MoveCommandDirection`

Specifies the direction of an arrow key movement.

Enumeration

# MoveCommandDirection

Specifies the direction of an arrow key movement.

macOS 10.15+  tvOS 13.0+

    
    
    enum MoveCommandDirection

## Topics

### Getting move command directions

`case up`

`case down`

`case left`

`case right`

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Responding to commands

`func onMoveCommand(perform: ((MoveCommandDirection) -> Void)?) -> some View`

Adds an action to perform in response to a move command, like when the user
presses an arrow key on a Mac keyboard, or taps the edge of the Siri Remote
when controlling an Apple TV.

`func onDeleteCommand(perform: (() -> Void)?) -> some View`

Adds an action to perform in response to the system’s Delete command, or
pressing either the ⌫ (backspace) or ⌦ (forward delete) keys while the view
has focus.

`func pageCommand<V>(value: Binding<V>, in: ClosedRange<V>, step: V) -> some
View`

Steps a value through a range in response to page up or page down commands.

`func onExitCommand(perform: (() -> Void)?) -> some View`

Sets up an action that triggers in response to receiving the exit command
while the view has focus.

`func onPlayPauseCommand(perform: (() -> Void)?) -> some View`

Adds an action to perform in response to the system’s Play/Pause command.

`func onCommand(Selector, perform: (() -> Void)?) -> some View`

Adds an action to perform in response to the given selector.

Instance Method

# allowsTightening(_:)

Sets whether text in this view can compress the space between characters when
necessary to fit text in a line.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func allowsTightening(_ flag: Bool) -> some View
    

##  Parameters

`flag`

    

A Boolean value that indicates whether the space between characters compresses
when necessary.

## Return Value

A view that can compress the space between characters when necessary to fit
text in a line.

## Discussion

Use `allowsTightening(_:)` to enable the compression of inter-character
spacing of text in a view to try to fit the text in the view’s bounds.

In the example below, two identically configured text views show the effects
of `allowsTightening(_:)` on the compression of the spacing between
characters:

## See Also

### Controlling hit testing

`func contentShape<S>(S, eoFill: Bool) -> some View`

Defines the content shape for hit testing.

`func contentShape<S>(ContentShapeKinds, S, eoFill: Bool) -> some View`

Sets the content shape for this view.

`struct ContentShapeKinds`

A kind for the content shape of a view.

Instance Method

# contentShape(_:eoFill:)

Defines the content shape for hit testing.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func contentShape<S>(
        _ shape: S,
        eoFill: Bool = false
    ) -> some View where S : Shape
    

##  Parameters

`shape`

    

The hit testing shape for the view.

`eoFill`

    

A Boolean that indicates whether the shape is interpreted with the even-odd
winding number rule.

## Return Value

A view that uses the given shape for hit testing.

## See Also

### Controlling hit testing

`func allowsTightening(Bool) -> some View`

Sets whether text in this view can compress the space between characters when
necessary to fit text in a line.

`func contentShape<S>(ContentShapeKinds, S, eoFill: Bool) -> some View`

Sets the content shape for this view.

`struct ContentShapeKinds`

A kind for the content shape of a view.

Instance Method

# contentShape(_:_:eoFill:)

Sets the content shape for this view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func contentShape<S>(
        _ kind: ContentShapeKinds,
        _ shape: S,
        eoFill: Bool = false
    ) -> some View where S : Shape
    

##  Parameters

`kind`

    

The kinds to apply to this content shape.

`shape`

    

The shape to use.

`eoFill`

    

A Boolean that indicates whether the shape is interpreted with the even-odd
winding number rule.

## Return Value

A view that uses the given shape for the specified kind.

## Discussion

The content shape has a variety of uses. You can control the kind of the
content shape by specifying one in `kind`. For example, the following example
only sets the focus ring shape of the view, without affecting its shape for
hit-testing:

## See Also

### Controlling hit testing

`func allowsTightening(Bool) -> some View`

Sets whether text in this view can compress the space between characters when
necessary to fit text in a line.

`func contentShape<S>(S, eoFill: Bool) -> some View`

Defines the content shape for hit testing.

`struct ContentShapeKinds`

A kind for the content shape of a view.

Structure

# ContentShapeKinds

A kind for the content shape of a view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    struct ContentShapeKinds

## Overview

The kind is used by the system to influence various effects, hit-testing, and
more.

## Topics

### Getting shape kinds

`static let interaction: ContentShapeKinds`

The kind for hit-testing and accessibility.

`static let dragPreview: ContentShapeKinds`

The kind for drag and drop previews.

`static let contextMenuPreview: ContentShapeKinds`

The kind for context menu previews.

`static let focusEffect: ContentShapeKinds`

The kind for the focus effect.

`static let hoverEffect: ContentShapeKinds`

The kind for hover effects.

`static let accessibility: ContentShapeKinds`

The kind for accessibility visuals and sorting.

### Creating a set of options

`init(rawValue: Int)`

Creates a content shape kind.

## Relationships

### Conforms To

  * `Equatable`
  * `ExpressibleByArrayLiteral`
  * `OptionSet`
  * `RawRepresentable`
  * `Sendable`
  * `SetAlgebra`

## See Also

### Controlling hit testing

`func allowsTightening(Bool) -> some View`

Sets whether text in this view can compress the space between characters when
necessary to fit text in a line.

`func contentShape<S>(S, eoFill: Bool) -> some View`

Defines the content shape for hit testing.

`func contentShape<S>(ContentShapeKinds, S, eoFill: Bool) -> some View`

Sets the content shape for this view.

Instance Method

# digitalCrownAccessory(_:)

Specifies the visibility of Digital Crown accessory Views on Apple Watch.

watchOS 9.0+

    
    
    func digitalCrownAccessory(_ visibility: Visibility) -> some View
    

##  Parameters

`visibility`

    

The visibility of the digital crown accessory.

## Discussion

Use this method to customize the visibility of a Digital Crown accessory
`View` created with the `View/digitalCrownAccessory(_ content:)` modifier. You
may want to keep an accessory visible even when the Digital Crown Indicator is
not visible to indicate what scrolling the crown will do.

## See Also

### Interacting with the Digital Crown

`func digitalCrownAccessory<Content>(content: () -> Content) -> some View`

Places an accessory View next to the Digital Crown on Apple Watch.

`func digitalCrownRotation<V>(Binding<V>, from: V, through: V, sensitivity:
DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>, onChange: (DigitalCrownEvent) ->
Void, onIdle: () -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(detent: Binding<V>, from: V, through: V, by:
V.Stride, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(detent: Binding<V>, from: V, through: V, by:
V.Stride, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>, from: V, through: V, by: V.Stride?,
sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`struct DigitalCrownEvent`

An event emitted when the user rotates the Digital Crown.

`enum DigitalCrownRotationalSensitivity`

The amount of Digital Crown rotation needed to move between two integer
numbers.

Instance Method

# digitalCrownAccessory(content:)

Places an accessory View next to the Digital Crown on Apple Watch.

watchOS 9.0+

    
    
    func digitalCrownAccessory<Content>(@ViewBuilder content: @escaping () -> Content) -> some View where Content : View
    

##  Parameters

`content`

    

The view to be used as a Digital Crown Accessory.

## Discussion

Use this method to place a custom `View` next to the Digital Crown on Apple
Watch. Use `digitalCrownAccessory(_:)` to specify the visibility of your
custom view.

## See Also

### Interacting with the Digital Crown

`func digitalCrownAccessory(Visibility) -> some View`

Specifies the visibility of Digital Crown accessory Views on Apple Watch.

`func digitalCrownRotation<V>(Binding<V>, from: V, through: V, sensitivity:
DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>, onChange: (DigitalCrownEvent) ->
Void, onIdle: () -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(detent: Binding<V>, from: V, through: V, by:
V.Stride, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(detent: Binding<V>, from: V, through: V, by:
V.Stride, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>, from: V, through: V, by: V.Stride?,
sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`struct DigitalCrownEvent`

An event emitted when the user rotates the Digital Crown.

`enum DigitalCrownRotationalSensitivity`

The amount of Digital Crown rotation needed to move between two integer
numbers.

Instance Method

#
digitalCrownRotation(_:from:through:sensitivity:isContinuous:isHapticFeedbackEnabled:onChange:onIdle:)

Tracks Digital Crown rotations by updating the specified binding.

watchOS 9.0+

    
    
    func digitalCrownRotation<V>(
        _ binding: Binding<V>,
        from minValue: V,
        through maxValue: V,
        sensitivity: DigitalCrownRotationalSensitivity = .high,
        isContinuous: Bool = false,
        isHapticFeedbackEnabled: Bool = true,
        onChange: @escaping (DigitalCrownEvent) -> Void = { _ in },
        onIdle: @escaping () -> Void = { }
    ) -> some View where V : BinaryFloatingPoint
    

##  Parameters

`binding`

    

A binding to a value that updates when the user rotates the Digital Crown.

`minValue`

    

Lower end of the range reported.

`maxValue`

    

Upper end of the range reported.

`sensitivity`

    

How much the user needs to rotate the Digital Crown to move between two
integer numbers.

`isContinuous`

    

Controls if the value reported stops at `minValue` and `maxValue`, or if it
should wrap around. Default is `false`.

`isHapticFeedbackEnabled`

    

Controls the generation of haptic feedback when turning the Digital Crown.
Default is `true`.

`onChange`

    

A block that is called as the Digital Crown is rotated.

`onIdle`

    

A block that is called when the Digital Crown has settled to an idle state.

## Discussion

Use this method to receive continuous values on a binding you provides as the
user turns the Digital Crown on Apple Watch. The example below receives
changes to the binding value, starting at the `minValue` of `0.0` up to the
`maxValue` of `10.0` settling in to multiples of `0.1` increasing or
decreasing depending on the direction that the user turns the Digital Crown,
rolling over if the user exceeds the specified boundary values:

## See Also

### Interacting with the Digital Crown

`func digitalCrownAccessory(Visibility) -> some View`

Specifies the visibility of Digital Crown accessory Views on Apple Watch.

`func digitalCrownAccessory<Content>(content: () -> Content) -> some View`

Places an accessory View next to the Digital Crown on Apple Watch.

`func digitalCrownRotation<V>(Binding<V>, onChange: (DigitalCrownEvent) ->
Void, onIdle: () -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(detent: Binding<V>, from: V, through: V, by:
V.Stride, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(detent: Binding<V>, from: V, through: V, by:
V.Stride, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>, from: V, through: V, by: V.Stride?,
sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`struct DigitalCrownEvent`

An event emitted when the user rotates the Digital Crown.

`enum DigitalCrownRotationalSensitivity`

The amount of Digital Crown rotation needed to move between two integer
numbers.

Instance Method

# digitalCrownRotation(_:onChange:onIdle:)

Tracks Digital Crown rotations by updating the specified binding.

watchOS 9.0+

    
    
    func digitalCrownRotation<V>(
        _ binding: Binding<V>,
        onChange: @escaping (DigitalCrownEvent) -> Void = { _ in },
        onIdle: @escaping () -> Void = { }
    ) -> some View where V : BinaryFloatingPoint
    

##  Parameters

`binding`

    

A binding to a value that updates as the user rotates the Digital Crown. The
implicit range is `(-infinity, +infinity)`.

`onChange`

    

A block that is called as the Digital Crown is rotated.

`onIdle`

    

A block that is called when the Digital Crown has settled to an idle state.

## Discussion

Use this method to receive values on a binding you provide as the user turns
the Digital Crown on Apple Watch. The example below receives changes to the
binding value, starting at `0.0` and incrementing or decrementing depending on
the direction that the user turns the Digital Crown:

## See Also

### Interacting with the Digital Crown

`func digitalCrownAccessory(Visibility) -> some View`

Specifies the visibility of Digital Crown accessory Views on Apple Watch.

`func digitalCrownAccessory<Content>(content: () -> Content) -> some View`

Places an accessory View next to the Digital Crown on Apple Watch.

`func digitalCrownRotation<V>(Binding<V>, from: V, through: V, sensitivity:
DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(detent: Binding<V>, from: V, through: V, by:
V.Stride, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(detent: Binding<V>, from: V, through: V, by:
V.Stride, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>, from: V, through: V, by: V.Stride?,
sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`struct DigitalCrownEvent`

An event emitted when the user rotates the Digital Crown.

`enum DigitalCrownRotationalSensitivity`

The amount of Digital Crown rotation needed to move between two integer
numbers.

Instance Method

#
digitalCrownRotation(detent:from:through:by:sensitivity:isContinuous:isHapticFeedbackEnabled:onChange:onIdle:)

Tracks Digital Crown rotations by updating the specified binding.

watchOS 9.0+

    
    
    func digitalCrownRotation<V>(
        detent: Binding<V>,
        from minValue: V,
        through maxValue: V,
        by stride: V.Stride,
        sensitivity: DigitalCrownRotationalSensitivity = .high,
        isContinuous: Bool = false,
        isHapticFeedbackEnabled: Bool = true,
        onChange: @escaping (DigitalCrownEvent) -> Void = { _ in },
        onIdle: @escaping () -> Void = { }
    ) -> some View where V : BinaryFloatingPoint, V.Stride : BinaryFloatingPoint
    

##  Parameters

`detent`

    

A binding to a value that updates when the user rotates the Digital Crown.

`minValue`

    

Lower end of the range reported.

`maxValue`

    

Upper end of the range reported.

`stride`

    

The value settles on multiples of `stride`.

`sensitivity`

    

How much the user needs to rotate the Digital Crown to move between two
detents.

`isContinuous`

    

Controls if the value reported stops at `minValue` and `maxValue`, or if it
should wrap around. Default is `false`.

`isHapticFeedbackEnabled`

    

Controls the generation of haptic feedback when turning the Digital Crown.
Default is `true`.

`onChange`

    

A block that is called as the Digital Crown is rotated.

`onIdle`

    

A block that is called when the Digital Crown has settled to an idle state.

## Discussion

Use this method to receive values on a binding you provide as the user turns
the Digital Crown on Apple Watch. The example below receives changes to the
binding value, starting at the `minValue` of `0.0` up to the `maxValue` of
`10.0` in steps of `0.1` incrementing or decrementing depending on the
direction that the user turns the Digital Crown, rolling over if the user
exceeds the specified boundary values. The binding will always be updated to a
value that is a multiple of the stride that is provided:

## See Also

### Interacting with the Digital Crown

`func digitalCrownAccessory(Visibility) -> some View`

Specifies the visibility of Digital Crown accessory Views on Apple Watch.

`func digitalCrownAccessory<Content>(content: () -> Content) -> some View`

Places an accessory View next to the Digital Crown on Apple Watch.

`func digitalCrownRotation<V>(Binding<V>, from: V, through: V, sensitivity:
DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>, onChange: (DigitalCrownEvent) ->
Void, onIdle: () -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(detent: Binding<V>, from: V, through: V, by:
V.Stride, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>, from: V, through: V, by: V.Stride?,
sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`struct DigitalCrownEvent`

An event emitted when the user rotates the Digital Crown.

`enum DigitalCrownRotationalSensitivity`

The amount of Digital Crown rotation needed to move between two integer
numbers.

Instance Method

#
digitalCrownRotation(detent:from:through:by:sensitivity:isContinuous:isHapticFeedbackEnabled:onChange:onIdle:)

Tracks Digital Crown rotations by updating the specified binding.

watchOS 9.0+

    
    
    func digitalCrownRotation<V>(
        detent: Binding<V>,
        from minValue: V,
        through maxValue: V,
        by stride: V.Stride,
        sensitivity: DigitalCrownRotationalSensitivity = .high,
        isContinuous: Bool = false,
        isHapticFeedbackEnabled: Bool = true,
        onChange: @escaping (DigitalCrownEvent) -> Void = { _ in },
        onIdle: @escaping () -> Void = { }
    ) -> some View where V : BinaryInteger, V.Stride : BinaryInteger
    

##  Parameters

`binding`

    

A binding to a value that updates when the user rotates the Digital Crown.

`minValue`

    

Lower end of the range reported.

`maxValue`

    

Upper end of the range reported.

`stride`

    

The value settles on multiples of `stride`.

`sensitivity`

    

How much the user needs to rotate the Digital Crown to move between two
integer numbers.

`isContinuous`

    

Controls if the value reported stops at `minValue` and `maxValue`, or if it
should wrap around. Default is `false`.

`isHapticFeedbackEnabled`

    

Controls the generation of haptic feedback when turning the Digital Crown.
Default is `true`.

`onChange`

    

A block that is called as the Digital Crown is rotated.

`onIdle`

    

A block that is called when the Digital Crown has settled to an idle state.

## Discussion

Use this method to receive values on a binding you provides as the user turns
the Digital Crown on Apple Watch. The example below receives changes to the
binding value, starting at the `minValue` of `0` up to the `maxValue` of `100`
in steps of `1` incrementing or decrementing depending on the direction that
the user turns the Digital Crown, rolling over if the user exceeds the
specified boundary values. The binding will always be updated to a value that
is a multiple of the stride that is provided:

## See Also

### Interacting with the Digital Crown

`func digitalCrownAccessory(Visibility) -> some View`

Specifies the visibility of Digital Crown accessory Views on Apple Watch.

`func digitalCrownAccessory<Content>(content: () -> Content) -> some View`

Places an accessory View next to the Digital Crown on Apple Watch.

`func digitalCrownRotation<V>(Binding<V>, from: V, through: V, sensitivity:
DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>, onChange: (DigitalCrownEvent) ->
Void, onIdle: () -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(detent: Binding<V>, from: V, through: V, by:
V.Stride, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>, from: V, through: V, by: V.Stride?,
sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`struct DigitalCrownEvent`

An event emitted when the user rotates the Digital Crown.

`enum DigitalCrownRotationalSensitivity`

The amount of Digital Crown rotation needed to move between two integer
numbers.

Instance Method

# digitalCrownRotation(_:)

Tracks Digital Crown rotations by updating the specified binding.

watchOS 6.0+

    
    
    func digitalCrownRotation<V>(_ binding: Binding<V>) -> some View where V : BinaryFloatingPoint
    

##  Parameters

`binding`

    

A binding to a value that updates as the user rotates the Digital Crown. The
implicit range is `(-infinity, +infinity)`.

## Discussion

Use this method to receive values on a binding you provide as the user turns
the Digital Crown on Apple Watch. The example below receives changes to the
binding value, starting at `0.0` and incrementing or decrementing depending on
the direction that the user turns the Digital Crown:

## See Also

### Interacting with the Digital Crown

`func digitalCrownAccessory(Visibility) -> some View`

Specifies the visibility of Digital Crown accessory Views on Apple Watch.

`func digitalCrownAccessory<Content>(content: () -> Content) -> some View`

Places an accessory View next to the Digital Crown on Apple Watch.

`func digitalCrownRotation<V>(Binding<V>, from: V, through: V, sensitivity:
DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>, onChange: (DigitalCrownEvent) ->
Void, onIdle: () -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(detent: Binding<V>, from: V, through: V, by:
V.Stride, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(detent: Binding<V>, from: V, through: V, by:
V.Stride, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>, from: V, through: V, by: V.Stride?,
sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`struct DigitalCrownEvent`

An event emitted when the user rotates the Digital Crown.

`enum DigitalCrownRotationalSensitivity`

The amount of Digital Crown rotation needed to move between two integer
numbers.

Instance Method

#
digitalCrownRotation(_:from:through:by:sensitivity:isContinuous:isHapticFeedbackEnabled:)

Tracks Digital Crown rotations by updating the specified binding.

watchOS 6.0+

    
    
    func digitalCrownRotation<V>(
        _ binding: Binding<V>,
        from minValue: V,
        through maxValue: V,
        by stride: V.Stride? = nil,
        sensitivity: DigitalCrownRotationalSensitivity = .high,
        isContinuous: Bool = false,
        isHapticFeedbackEnabled: Bool = true
    ) -> some View where V : BinaryFloatingPoint, V.Stride : BinaryFloatingPoint
    

##  Parameters

`binding`

    

A binding to a value that updates when the user rotates the Digital Crown.

`minValue`

    

Lower end of the range reported.

`maxValue`

    

Upper end of the range reported.

`stride`

    

The value settles on multiples of `stride`.

`sensitivity`

    

How much the user needs to rotate the Digital Crown to move between two
integer numbers.

`isContinuous`

    

Controls if the value reported stops at `minValue` and `maxValue`, or if it
should wrap around. Default is `false`.

`isHapticFeedbackEnabled`

    

Controls the generation of haptic feedback when turning the Digital Crown.
Default is `true`.

## Discussion

Use this method to receive values on a binding you provides as the user turns
the Digital Crown on Apple Watch. The example below receives changes to the
binding value, starting at the `minValue` of `0.0` up to the `maxValue` of
`10.0` in steps of `0.1` incrementing or decrementing depending on the
direction that the user turns the Digital Crown, rolling over if the user
exceeds the specified boundary values:

## See Also

### Interacting with the Digital Crown

`func digitalCrownAccessory(Visibility) -> some View`

Specifies the visibility of Digital Crown accessory Views on Apple Watch.

`func digitalCrownAccessory<Content>(content: () -> Content) -> some View`

Places an accessory View next to the Digital Crown on Apple Watch.

`func digitalCrownRotation<V>(Binding<V>, from: V, through: V, sensitivity:
DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>, onChange: (DigitalCrownEvent) ->
Void, onIdle: () -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(detent: Binding<V>, from: V, through: V, by:
V.Stride, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(detent: Binding<V>, from: V, through: V, by:
V.Stride, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`struct DigitalCrownEvent`

An event emitted when the user rotates the Digital Crown.

`enum DigitalCrownRotationalSensitivity`

The amount of Digital Crown rotation needed to move between two integer
numbers.

Structure

# DigitalCrownEvent

An event emitted when the user rotates the Digital Crown.

watchOS 9.0+

    
    
    struct DigitalCrownEvent

## Overview

Use the `digitalCrownRotation(_:)` modifier to receive these events.

## Topics

### Getting events

`var offset: Double`

The offset of the digital crown when this event was sent.

`var velocity: Double`

The velocity at which the offset was changing when this event was sent.

## Relationships

### Conforms To

  * `Sendable`

## See Also

### Interacting with the Digital Crown

`func digitalCrownAccessory(Visibility) -> some View`

Specifies the visibility of Digital Crown accessory Views on Apple Watch.

`func digitalCrownAccessory<Content>(content: () -> Content) -> some View`

Places an accessory View next to the Digital Crown on Apple Watch.

`func digitalCrownRotation<V>(Binding<V>, from: V, through: V, sensitivity:
DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>, onChange: (DigitalCrownEvent) ->
Void, onIdle: () -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(detent: Binding<V>, from: V, through: V, by:
V.Stride, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(detent: Binding<V>, from: V, through: V, by:
V.Stride, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>, from: V, through: V, by: V.Stride?,
sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`enum DigitalCrownRotationalSensitivity`

The amount of Digital Crown rotation needed to move between two integer
numbers.

Enumeration

# DigitalCrownRotationalSensitivity

The amount of Digital Crown rotation needed to move between two integer
numbers.

watchOS 6.0+

    
    
    enum DigitalCrownRotationalSensitivity

## Overview

You may need to experiment to find the level of sensitivity that works for
your use case.

## Topics

### Getting sensitivity options

`case low`

Low sensitivity.

`case medium`

Medium sensitivity.

`case high`

High sensitivity.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Interacting with the Digital Crown

`func digitalCrownAccessory(Visibility) -> some View`

Specifies the visibility of Digital Crown accessory Views on Apple Watch.

`func digitalCrownAccessory<Content>(content: () -> Content) -> some View`

Places an accessory View next to the Digital Crown on Apple Watch.

`func digitalCrownRotation<V>(Binding<V>, from: V, through: V, sensitivity:
DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>, onChange: (DigitalCrownEvent) ->
Void, onIdle: () -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(detent: Binding<V>, from: V, through: V, by:
V.Stride, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(detent: Binding<V>, from: V, through: V, by:
V.Stride, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>, from: V, through: V, by: V.Stride?,
sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`struct DigitalCrownEvent`

An event emitted when the user rotates the Digital Crown.

Instance Method

# touchBar(content:)

Sets the content that the Touch Bar displays.

macOS 10.15+

    
    
    func touchBar<Content>(@ViewBuilder content: () -> Content) -> some View where Content : View
    

##  Parameters

`content`

    

A collection of views to be displayed by the Touch Bar.

## Return Value

A view that contains the Touch Bar content.

## Discussion

Use `touchBar(_:)` when you need to dynamically construct items to show in the
Touch Bar. The content is displayed by the Touch Bar when appropriate,
depending on focus.

In the example below, four buttons are added to a Touch Bar content struct and
then added to the Touch Bar:

## See Also

### Managing Touch Bar input

`func touchBar<Content>(TouchBar<Content>) -> some View`

Sets the Touch Bar content to be shown in the Touch Bar when applicable.

`func touchBarItemPrincipal(Bool) -> some View`

Sets principal views that have special significance to this Touch Bar.

`func touchBarCustomizationLabel(Text) -> some View`

Sets a user-visible string that identifies the view’s functionality.

`func touchBarItemPresence(TouchBarItemPresence) -> some View`

Sets the behavior of the user-customized view.

`struct TouchBar`

A container for a view that you can show in the Touch Bar.

`enum TouchBarItemPresence`

Options that affect user customization of the Touch Bar.

Instance Method

# touchBar(_:)

Sets the Touch Bar content to be shown in the Touch Bar when applicable.

macOS 10.15+

    
    
    func touchBar<Content>(_ touchBar: TouchBar<Content>) -> some View where Content : View
    

##  Parameters

`touchBar`

    

A collection of views that the Touch Bar displays.

## Return Value

A view that contains the Touch Bar content.

## Discussion

Use `touchBar(_:)` to provide a static set of views that are displayed by the
Touch Bar when appropriate, depending on whether the view has focus.

The example below provides Touch Bar content in-line, that creates the content
the Touch Bar displays:

## See Also

### Managing Touch Bar input

`func touchBar<Content>(content: () -> Content) -> some View`

Sets the content that the Touch Bar displays.

`func touchBarItemPrincipal(Bool) -> some View`

Sets principal views that have special significance to this Touch Bar.

`func touchBarCustomizationLabel(Text) -> some View`

Sets a user-visible string that identifies the view’s functionality.

`func touchBarItemPresence(TouchBarItemPresence) -> some View`

Sets the behavior of the user-customized view.

`struct TouchBar`

A container for a view that you can show in the Touch Bar.

`enum TouchBarItemPresence`

Options that affect user customization of the Touch Bar.

Instance Method

# touchBarItemPrincipal(_:)

Sets principal views that have special significance to this Touch Bar.

macOS 10.15+

    
    
    func touchBarItemPrincipal(_ principal: Bool = true) -> some View
    

##  Parameters

`principal`

    

A Boolean value that indicates whether to display this view prominently in the
Touch Bar compared to other views.

## Return Value

A Touch Bar view with one element centered in the Touch Bar row.

## Discussion

Use `touchBarItemPrincipal(_:)` to designate a view as a significant view in
the Touch Bar. Currently, that view will be placed in the center of the row.

The example below sets the last button as the principal button for the Touch
Bar view.

Note

Multiple visible bars may each specify a principal view, but the system only
honors one of them.

## See Also

### Managing Touch Bar input

`func touchBar<Content>(content: () -> Content) -> some View`

Sets the content that the Touch Bar displays.

`func touchBar<Content>(TouchBar<Content>) -> some View`

Sets the Touch Bar content to be shown in the Touch Bar when applicable.

`func touchBarCustomizationLabel(Text) -> some View`

Sets a user-visible string that identifies the view’s functionality.

`func touchBarItemPresence(TouchBarItemPresence) -> some View`

Sets the behavior of the user-customized view.

`struct TouchBar`

A container for a view that you can show in the Touch Bar.

`enum TouchBarItemPresence`

Options that affect user customization of the Touch Bar.

Instance Method

# touchBarCustomizationLabel(_:)

Sets a user-visible string that identifies the view’s functionality.

macOS 10.15+

    
    
    func touchBarCustomizationLabel(_ label: Text) -> some View
    

##  Parameters

`label`

    

A `Text` view containing the customization label.

## Return Value

A Touch Bar element with a set customization label.

## Discussion

This string is visible during user customization.

## See Also

### Managing Touch Bar input

`func touchBar<Content>(content: () -> Content) -> some View`

Sets the content that the Touch Bar displays.

`func touchBar<Content>(TouchBar<Content>) -> some View`

Sets the Touch Bar content to be shown in the Touch Bar when applicable.

`func touchBarItemPrincipal(Bool) -> some View`

Sets principal views that have special significance to this Touch Bar.

`func touchBarItemPresence(TouchBarItemPresence) -> some View`

Sets the behavior of the user-customized view.

`struct TouchBar`

A container for a view that you can show in the Touch Bar.

`enum TouchBarItemPresence`

Options that affect user customization of the Touch Bar.

Instance Method

# touchBarItemPresence(_:)

Sets the behavior of the user-customized view.

macOS 10.15+

    
    
    func touchBarItemPresence(_ presence: TouchBarItemPresence) -> some View
    

##  Parameters

`presence`

    

One of the allowed `TouchBarItemPresence` descriptions.

## Return Value

A trait that describes the behavior for this Touch Bar view.

## Discussion

Use `touchBarItemPresence(_:)` to define the visibility requirements of a
particular Touch Bar view during customization by the user.

Touch Bar views may be:

  * `.required`: not allowed to be removed by the user.

  * `.default`: shown by default prior to user customization, but removable.

  * `.optional`: not visible by default, but can be added through the customization palette.

Each `TouchBarItemPresence` must be initialized with a string that is a
globally unique identifier for this item.

In the example below, all of the Touch Bar items are visible in the Touch Bar
by default, except for the “Clubs” item. It’s set to `.optional` but is
configurable by the user:

## See Also

### Managing Touch Bar input

`func touchBar<Content>(content: () -> Content) -> some View`

Sets the content that the Touch Bar displays.

`func touchBar<Content>(TouchBar<Content>) -> some View`

Sets the Touch Bar content to be shown in the Touch Bar when applicable.

`func touchBarItemPrincipal(Bool) -> some View`

Sets principal views that have special significance to this Touch Bar.

`func touchBarCustomizationLabel(Text) -> some View`

Sets a user-visible string that identifies the view’s functionality.

`struct TouchBar`

A container for a view that you can show in the Touch Bar.

`enum TouchBarItemPresence`

Options that affect user customization of the Touch Bar.

Structure

# TouchBar

A container for a view that you can show in the Touch Bar.

macOS 10.15+

    
    
    struct TouchBar<Content> where Content : View

## Topics

### Creating a Touch Bar view

`init(content: () -> Content)`

Creates a non-customizable Touch Bar view container.

`init(id: String, content: () -> Content)`

Creates a customizable Touch Bar view container with a globally unique
identifier.

## See Also

### Managing Touch Bar input

`func touchBar<Content>(content: () -> Content) -> some View`

Sets the content that the Touch Bar displays.

`func touchBar<Content>(TouchBar<Content>) -> some View`

Sets the Touch Bar content to be shown in the Touch Bar when applicable.

`func touchBarItemPrincipal(Bool) -> some View`

Sets principal views that have special significance to this Touch Bar.

`func touchBarCustomizationLabel(Text) -> some View`

Sets a user-visible string that identifies the view’s functionality.

`func touchBarItemPresence(TouchBarItemPresence) -> some View`

Sets the behavior of the user-customized view.

`enum TouchBarItemPresence`

Options that affect user customization of the Touch Bar.

Enumeration

# TouchBarItemPresence

Options that affect user customization of the Touch Bar.

macOS 10.15+

    
    
    enum TouchBarItemPresence

## Topics

### Getting presence options

`case `default`(String)`

The Touch Bar view is visible by default, but can be removed during
customization.

`case optional(String)`

The Touch Bar view isn’t visible by default, but appears in the customization
palette.

`case required(String)`

The Touch Bar view is visible by default and cannot be removed during
customization.

## Relationships

### Conforms To

  * `Sendable`

## See Also

### Managing Touch Bar input

`func touchBar<Content>(content: () -> Content) -> some View`

Sets the content that the Touch Bar displays.

`func touchBar<Content>(TouchBar<Content>) -> some View`

Sets the Touch Bar content to be shown in the Touch Bar when applicable.

`func touchBarItemPrincipal(Bool) -> some View`

Sets principal views that have special significance to this Touch Bar.

`func touchBarCustomizationLabel(Text) -> some View`

Sets a user-visible string that identifies the view’s functionality.

`func touchBarItemPresence(TouchBarItemPresence) -> some View`

Sets the behavior of the user-customized view.

`struct TouchBar`

A container for a view that you can show in the Touch Bar.



# ImagePaint

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



# Image.ResizingMode

Case

# Image.ResizingMode.stretch

A mode to enlarge or reduce the size of an image so that it fills the
available space.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case stretch

## See Also

### Getting resizing modes

`case tile`

A mode to repeat the image at its original size, as many times as necessary to
fill the available space.

Case

# Image.ResizingMode.tile

A mode to repeat the image at its original size, as many times as necessary to
fill the available space.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case tile

## See Also

### Getting resizing modes

`case stretch`

A mode to enlarge or reduce the size of an image so that it fills the
available space.



# InsetListStyle

Initializer

# init()

Creates an inset list style.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    init()

## See Also

### Creating the list style

`init(alternatesRowBackgrounds: Bool)`

Creates an inset list style with optional alternating row backgrounds.

Deprecated

Initializer

# init(alternatesRowBackgrounds:)

Creates an inset list style with optional alternating row backgrounds.

macOS 12.0–14.4  Deprecated

    
    
    init(alternatesRowBackgrounds: Bool)

Deprecated

Use the `inset` style and add the `alternatingRowBackgrounds(_:)` view
modifier instead.

## See Also

### Creating the list style

`init()`

Creates an inset list style.



# Image.DynamicRange

Type Property

# standard

Restrict the image content dynamic range to the standard range.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    static let standard: Image.DynamicRange

## See Also

### Getting dynamic range values

`static let high: Image.DynamicRange`

Allow image content to use an unrestricted extended range.

`static let constrainedHigh: Image.DynamicRange`

Allow image content to use some extended range. This is appropriate for
placing HDR content next to SDR content.

Type Property

# high

Allow image content to use an unrestricted extended range.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    static let high: Image.DynamicRange

## See Also

### Getting dynamic range values

`static let standard: Image.DynamicRange`

Restrict the image content dynamic range to the standard range.

`static let constrainedHigh: Image.DynamicRange`

Allow image content to use some extended range. This is appropriate for
placing HDR content next to SDR content.

Type Property

# constrainedHigh

Allow image content to use some extended range. This is appropriate for
placing HDR content next to SDR content.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    static let constrainedHigh: Image.DynamicRange

## See Also

### Getting dynamic range values

`static let standard: Image.DynamicRange`

Restrict the image content dynamic range to the standard range.

`static let high: Image.DynamicRange`

Allow image content to use an unrestricted extended range.



# Image.Orientation

Case

# Image.Orientation.up

A value that indicates the original pixel data matches the image’s intended
display orientation.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case up

## See Also

### Getting image orientations

`case down`

A value that indicates a 180° rotation of the image from the orientation of
its original pixel data.

`case left`

A value that indicates a 90° counterclockwise rotation from the orientation of
its original pixel data.

`case right`

A value that indicates a 90° clockwise rotation of the image from the
orientation of its original pixel data.

Case

# Image.Orientation.down

A value that indicates a 180° rotation of the image from the orientation of
its original pixel data.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case down

## See Also

### Getting image orientations

`case up`

A value that indicates the original pixel data matches the image’s intended
display orientation.

`case left`

A value that indicates a 90° counterclockwise rotation from the orientation of
its original pixel data.

`case right`

A value that indicates a 90° clockwise rotation of the image from the
orientation of its original pixel data.

Case

# Image.Orientation.left

A value that indicates a 90° counterclockwise rotation from the orientation of
its original pixel data.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case left

## See Also

### Getting image orientations

`case up`

A value that indicates the original pixel data matches the image’s intended
display orientation.

`case down`

A value that indicates a 180° rotation of the image from the orientation of
its original pixel data.

`case right`

A value that indicates a 90° clockwise rotation of the image from the
orientation of its original pixel data.

Case

# Image.Orientation.right

A value that indicates a 90° clockwise rotation of the image from the
orientation of its original pixel data.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case right

## See Also

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

Case

# Image.Orientation.upMirrored

A value that indicates a horizontal flip of the image from the orientation of
its original pixel data.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case upMirrored

## See Also

### Getting mirrored image orientation

`case downMirrored`

A value that indicates a vertical flip of the image from the orientation of
its original pixel data.

`case leftMirrored`

A value that indicates a 90° clockwise rotation and horizontal flip of the
image from the orientation of its original pixel data.

`case rightMirrored`

A value that indicates a 90° counterclockwise rotation and horizontal flip
from the orientation of its original pixel data.

Case

# Image.Orientation.downMirrored

A value that indicates a vertical flip of the image from the orientation of
its original pixel data.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case downMirrored

## See Also

### Getting mirrored image orientation

`case upMirrored`

A value that indicates a horizontal flip of the image from the orientation of
its original pixel data.

`case leftMirrored`

A value that indicates a 90° clockwise rotation and horizontal flip of the
image from the orientation of its original pixel data.

`case rightMirrored`

A value that indicates a 90° counterclockwise rotation and horizontal flip
from the orientation of its original pixel data.

Case

# Image.Orientation.leftMirrored

A value that indicates a 90° clockwise rotation and horizontal flip of the
image from the orientation of its original pixel data.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case leftMirrored

## See Also

### Getting mirrored image orientation

`case upMirrored`

A value that indicates a horizontal flip of the image from the orientation of
its original pixel data.

`case downMirrored`

A value that indicates a vertical flip of the image from the orientation of
its original pixel data.

`case rightMirrored`

A value that indicates a 90° counterclockwise rotation and horizontal flip
from the orientation of its original pixel data.

Case

# Image.Orientation.rightMirrored

A value that indicates a 90° counterclockwise rotation and horizontal flip
from the orientation of its original pixel data.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case rightMirrored

## See Also

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



# ImmersionStyle

Type Property

# automatic

The default immersion style.

visionOS 1.0+

    
    
    static var automatic: AutomaticImmersionStyle { get }

Available when `Self` is `AutomaticImmersionStyle`.

## Discussion

The system uses this style for an `ImmersiveSpace` if you don’t provide an
`immersionStyle(selection:in:)` scene modifier. You don’t typically specify
the `automatic` style explicitly.

By default, the system uses the `mixed` immersion style as the `automatic`
style.

## See Also

### Getting built-in styles

`static var full: FullImmersionStyle`

An immersion style that displays unbounded content that completely replaces
passthrough video.

Available when `Self` is `FullImmersionStyle`.

`static var mixed: MixedImmersionStyle`

An immersion style that displays unbounded content intermixed with other app
content, along with passthrough video.

Available when `Self` is `MixedImmersionStyle`.

`static var progressive: ProgressiveImmersionStyle`

An immersion style that displays unbounded content that partially replaces
passthrough video.

Available when `Self` is `ProgressiveImmersionStyle`.

Type Property

# full

An immersion style that displays unbounded content that completely replaces
passthrough video.

visionOS 1.0+

    
    
    static var full: FullImmersionStyle { get }

Available when `Self` is `FullImmersionStyle`.

## Discussion

Use the `immersionStyle(selection:in:)` scene modifier to specify this style
for an `ImmersiveSpace`.

When using this style, the space’s content fully obscures passthrough except
for the user’s upper limbs. You can manage limb visibility separately by
applying the `upperLimbVisibility(_:)` scene modifier to the space, or the
view modifier equivalent to a view inside the scene.

The immersion style affects how windows interact with virtual objects in the
environment. In `full` immersion, windows always render in front of virtual
content, no matter how someone positions the window or the content. This helps
people to avoid losing track of windows behind virtual content when
passthrough is off.

## See Also

### Getting built-in styles

`static var automatic: AutomaticImmersionStyle`

The default immersion style.

Available when `Self` is `AutomaticImmersionStyle`.

`static var mixed: MixedImmersionStyle`

An immersion style that displays unbounded content intermixed with other app
content, along with passthrough video.

Available when `Self` is `MixedImmersionStyle`.

`static var progressive: ProgressiveImmersionStyle`

An immersion style that displays unbounded content that partially replaces
passthrough video.

Available when `Self` is `ProgressiveImmersionStyle`.

Type Property

# mixed

An immersion style that displays unbounded content intermixed with other app
content, along with passthrough video.

visionOS 1.0+

    
    
    static var mixed: MixedImmersionStyle { get }

Available when `Self` is `MixedImmersionStyle`.

## Discussion

Use the `immersionStyle(selection:in:)` scene modifier to specify this style
for an `ImmersiveSpace`. However, this is the default immersion style if you
don’t specify one.

The immersion style affects how windows interact with virtual objects in the
environment. In `mixed` immersion, a virtual object obscures part or all of a
window that’s behind the object. Similarly, a window obscures a virtual object
that’s behind the window.

## See Also

### Getting built-in styles

`static var automatic: AutomaticImmersionStyle`

The default immersion style.

Available when `Self` is `AutomaticImmersionStyle`.

`static var full: FullImmersionStyle`

An immersion style that displays unbounded content that completely replaces
passthrough video.

Available when `Self` is `FullImmersionStyle`.

`static var progressive: ProgressiveImmersionStyle`

An immersion style that displays unbounded content that partially replaces
passthrough video.

Available when `Self` is `ProgressiveImmersionStyle`.

Type Property

# progressive

An immersion style that displays unbounded content that partially replaces
passthrough video.

visionOS 1.0+

    
    
    static var progressive: ProgressiveImmersionStyle { get }

Available when `Self` is `ProgressiveImmersionStyle`.

## Discussion

Use the `immersionStyle(selection:in:)` scene modifier to specify this style
for an `ImmersiveSpace`.

The system initially uses a radial portal effect that replaces passthrough in
a portion of the field of view. People can interactively adjust the size of
the portal by rotating the Digital Crown, including down to the point where
the portal disappears and up to the point where the portal fully replaces
passthrough. The latter matches the behavior of the `full` immersion style,
including the configurable visibility of the viewer’s upper limbs.

The immersion style affects how windows interact with virtual objects in the
environment. In `progressive` immersion, windows always render in front of
virtual content, no matter how someone positions the window or the content.
This helps people to avoid losing track of windows behind virtual content when
passthrough is off.

## See Also

### Getting built-in styles

`static var automatic: AutomaticImmersionStyle`

The default immersion style.

Available when `Self` is `AutomaticImmersionStyle`.

`static var full: FullImmersionStyle`

An immersion style that displays unbounded content that completely replaces
passthrough video.

Available when `Self` is `FullImmersionStyle`.

`static var mixed: MixedImmersionStyle`

An immersion style that displays unbounded content intermixed with other app
content, along with passthrough video.

Available when `Self` is `MixedImmersionStyle`.

Structure

# AutomaticImmersionStyle

The default style of immersive spaces.

visionOS 1.0+

    
    
    struct AutomaticImmersionStyle

## Overview

You don’t typically use this style explicitly, but if you need to, use
`automatic` with the `immersionStyle(selection:in:)`modifier to specify this
style.

## Topics

### Creating the immersion style

`init()`

## Relationships

### Conforms To

  * `ImmersionStyle`

## See Also

### Supporting types

`struct FullImmersionStyle`

An immersion style that displays unbounded content that completely replaces
passthrough video.

`struct MixedImmersionStyle`

An immersion style that displays unbounded content intermixed with other app
content, along with passthrough video.

`struct ProgressiveImmersionStyle`

An immersion style that displays unbounded content that partially replaces
passthrough video.

Structure

# FullImmersionStyle

An immersion style that displays unbounded content that completely replaces
passthrough video.

visionOS 1.0+

    
    
    struct FullImmersionStyle

## Overview

Use `full` with the `immersionStyle(selection:in:)`modifier to specify this
style.

## Topics

### Creating the immersion style

`init()`

## Relationships

### Conforms To

  * `ImmersionStyle`

## See Also

### Supporting types

`struct AutomaticImmersionStyle`

The default style of immersive spaces.

`struct MixedImmersionStyle`

An immersion style that displays unbounded content intermixed with other app
content, along with passthrough video.

`struct ProgressiveImmersionStyle`

An immersion style that displays unbounded content that partially replaces
passthrough video.

Structure

# MixedImmersionStyle

An immersion style that displays unbounded content intermixed with other app
content, along with passthrough video.

visionOS 1.0+

    
    
    struct MixedImmersionStyle

## Overview

Use `mixed` with the `immersionStyle(selection:in:)`modifier to specify this
style.

## Topics

### Creating the immersion style

`init()`

## Relationships

### Conforms To

  * `ImmersionStyle`

## See Also

### Supporting types

`struct AutomaticImmersionStyle`

The default style of immersive spaces.

`struct FullImmersionStyle`

An immersion style that displays unbounded content that completely replaces
passthrough video.

`struct ProgressiveImmersionStyle`

An immersion style that displays unbounded content that partially replaces
passthrough video.

Structure

# ProgressiveImmersionStyle

An immersion style that displays unbounded content that partially replaces
passthrough video.

visionOS 1.0+

    
    
    struct ProgressiveImmersionStyle

## Overview

Use `progressive` with the `immersionStyle(selection:in:)`modifier to specify
this style.

## Topics

### Creating the immersion style

`init()`

## Relationships

### Conforms To

  * `ImmersionStyle`

## See Also

### Supporting types

`struct AutomaticImmersionStyle`

The default style of immersive spaces.

`struct FullImmersionStyle`

An immersion style that displays unbounded content that completely replaces
passthrough video.

`struct MixedImmersionStyle`

An immersion style that displays unbounded content intermixed with other app
content, along with passthrough video.



# InsetGroupedListStyle

Initializer

# init()

Creates an inset grouped list style.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    init()



# Image.Interpolation

Case

# Image.Interpolation.high

A value that indicates a high level of interpolation quality, which may slow
down image rendering.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case high

## See Also

### Getting interpolation options

`case low`

A value that indicates a low level of interpolation quality, which may speed
up image rendering.

`case medium`

A value that indicates a medium level of interpolation quality, between the
low- and high-quality values.

`case none`

A value that indicates SwiftUI doesn’t interpolate image data.

Case

# Image.Interpolation.low

A value that indicates a low level of interpolation quality, which may speed
up image rendering.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case low

## See Also

### Getting interpolation options

`case high`

A value that indicates a high level of interpolation quality, which may slow
down image rendering.

`case medium`

A value that indicates a medium level of interpolation quality, between the
low- and high-quality values.

`case none`

A value that indicates SwiftUI doesn’t interpolate image data.

Case

# Image.Interpolation.medium

A value that indicates a medium level of interpolation quality, between the
low- and high-quality values.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case medium

## See Also

### Getting interpolation options

`case high`

A value that indicates a high level of interpolation quality, which may slow
down image rendering.

`case low`

A value that indicates a low level of interpolation quality, which may speed
up image rendering.

`case none`

A value that indicates SwiftUI doesn’t interpolate image data.

Case

# Image.Interpolation.none

A value that indicates SwiftUI doesn’t interpolate image data.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case none

## See Also

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



# IdentityTransition

Initializer

# init()

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init()



# InlinePickerStyle

Initializer

# init()

Creates an inline picker style.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init()



# Immersive spaces

Structure

# ImmersiveSpace

A scene that presents its content in an unbounded space.

visionOS 1.0+

    
    
    struct ImmersiveSpace<Content, Data> where Content : ImmersiveSpaceContent, Data : Decodable, Data : Encodable, Data : Hashable

## Overview

Use an immersive space as a container for a view hierarchy that your app
presents. The hierarchy that you declare as the immersive space’s content
serves as a template for it:

If you want to create a bounded scene instead, use one of the types that
creates a window or a volume, like `WindowGroup` or `DocumentGroup`.

### Style the immersive space

By default, immersive spaces use the `mixed` style which places virtual
content in a person’s surroundings. You can select a different style for the
immersive space by adding the `immersionStyle(selection:in:)` scene modifier
to the scene. For example, you can completely control the visual experience
using the `full` immersion style:

You can change the immersion style after presenting the immersive space by
changing the modifier’s `selection` input, although you can only use one of
the values that you specify in the modifier’s second parameter. For any style
of immersion, the other parts of your app’s interface — namely its windows —
remain visible. However, the immersion style affects how windows interact with
virtual objects in the environment:

  * For the `mixed` style, a virtual object obscures part or all of a window that’s behind the object. Similarly, a window obscures a virtual object that’s behind the window.

  * For other styles, windows always render in front of virtual content, no matter how someone positions the window or the content. This helps people to avoid losing track of windows behind virtual content when passthrough is partially or completely off.

### Open an immersive space

You can programmatically open an immersive space by giving it an identifier.
For example, you can label the solar system view from the previous example:

Elsewhere in your code, you use the `openImmersiveSpace` environment value to
get the instance of the `OpenImmersiveSpaceAction` structure for a given
`Environment`. You call the instance directly — for example, from a button’s
closure, like in the following code — using the identifier:

Mark the call to the action with `await` because it executes asynchronously.
When your app opens an immersive space, the system hides all other visible
apps. The system allows only one immersive space to be open at a time. Be sure
to close the open immersive space before opening another one.

### Dismiss an immersive space

You can dismiss an immersive space by calling the `dismissImmersiveSpace`
action from the environment. For example, you can define a button that
dismisses an immersive space:

The dismiss action runs asynchronously, like the open action. You don’t need
to specify an identifier when dismissing an immersive space because there can
only be one immersive space open at a time.

### Present an immersive space at launch

When an app launches, it opens an instance of the first scene that’s listed in
the app’s body. However, to open an immersive space at launch, you need to
provide additional configuration information in your app’s `Info.plist` file.
In particular, set the `UIApplicationPreferredDefaultSceneSessionRole` key in
the scene manifest to the value UISceneSessionRoleImmersiveSpaceApplication.

To configure the style of the immersive space that opens at launch, add a
scene configuration to the scene session role. Use the
`UISceneInitialImmersionStyle` key together with a value that indicates one of
the mixed, full, or progressive styles. See the initial immersion style key
for more information.

## Topics

### Creating a data-driven immersive space

`init(for: Data.Type, content: (Binding<Data?>) -> Content)`

Creates the immersive space for a specified type of presented data.

`init<V>(for: Data.Type, content: (Binding<Data?>) -> V)`

Creates the immersive space for a specified type of presented data using view-
based content.

Available when `Content` conforms to `ImmersiveSpaceContent`, `Data` conforms
to `Decodable`, `Data` conforms to `Encodable`, and `Data` conforms to
`Hashable`.

`init(id: String, for: Data.Type, content: (Binding<Data?>) -> Content)`

Creates the immersive space associated with an identifier for a specified type
of presented data.

`init<V>(id: String, for: Data.Type, content: (Binding<Data?>) -> V)`

Creates the immersive space associated with an identifier for a specified type
of presented data using view-based content.

Available when `Content` conforms to `ImmersiveSpaceContent`, `Data` conforms
to `Decodable`, `Data` conforms to `Encodable`, and `Data` conforms to
`Hashable`.

### Providing default data to an immersive space

`init(for: Data.Type, content: (Binding<Data>) -> Content, defaultValue: () ->
Data)`

Creates an immersive space.

`init<V>(for: Data.Type, content: (Binding<Data>) -> V, defaultValue: () ->
Data)`

Creates an immersive space for a specified type of presented data and a
default value if the data is not set.

Available when `Content` conforms to `ImmersiveSpaceContent`, `Data` conforms
to `Decodable`, `Data` conforms to `Encodable`, and `Data` conforms to
`Hashable`.

`init<V>(id: String, for: Data.Type, content: (Binding<Data>) -> V,
defaultValue: () -> Data)`

Creates the immersive space associated with an identifier for a specified type
of presented data and a default value if the data is not set.

Available when `Content` conforms to `ImmersiveSpaceContent`, `Data` conforms
to `Decodable`, `Data` conforms to `Encodable`, and `Data` conforms to
`Hashable`.

`init(id: String, for: Data.Type, content: (Binding<Data>) -> Content,
defaultValue: () -> Data)`

Creates the immersive space associated with an identifier for a specified type
of presented data, and a default value, if the data is not set.

### Supporting types

`struct ImmersiveSpaceViewContent`

Immersive space content that uses a SwiftUI view hierarchy as the content.

`protocol ImmersiveSpaceContent`

A type that you can use as the content of an immersive space.

### Initializers

`init(content: () -> Content)`

Creates an immersive space.

`init<V>(content: () -> V)`

Creates an immersive space using view-based content.

Available when `Content` conforms to `ImmersiveSpaceContent`, `Data` conforms
to `Decodable`, `Data` conforms to `Encodable`, and `Data` conforms to
`Hashable`.

`init<V>(id: String, content: () -> V)`

Creates the immersive space associated with the specified identifier using
view-based content.

Available when `Content` conforms to `ImmersiveSpaceContent`, `Data` conforms
to `Decodable`, `Data` conforms to `Encodable`, and `Data` conforms to
`Hashable`.

`init(id: String, content: () -> Content)`

Creates the immersive space associated with the specified identifier.

## Relationships

### Conforms To

  * `Scene`

## See Also

### Creating an immersive space

`struct ImmersiveSpaceContentBuilder`

A result builder for composing a collection of immersive space elements.

`func immersionStyle(selection: Binding<any ImmersionStyle>, in: any
ImmersionStyle...) -> some Scene`

Sets the style for an immersive space.

`protocol ImmersionStyle`

The styles that an immersive space can have.

Structure

# ImmersiveSpaceContentBuilder

A result builder for composing a collection of immersive space elements.

visionOS 1.0+

    
    
    @resultBuilder
    struct ImmersiveSpaceContentBuilder

## Topics

### Building content

`static func buildBlock<Content>(Content) -> Content`

## See Also

### Creating an immersive space

`struct ImmersiveSpace`

A scene that presents its content in an unbounded space.

`func immersionStyle(selection: Binding<any ImmersionStyle>, in: any
ImmersionStyle...) -> some Scene`

Sets the style for an immersive space.

`protocol ImmersionStyle`

The styles that an immersive space can have.

Instance Method

# immersionStyle(selection:in:)

Sets the style for an immersive space.

visionOS 1.0+

    
    
    func immersionStyle(
        selection: Binding<any ImmersionStyle>,
        in styles: any ImmersionStyle...
    ) -> some Scene
    

##  Parameters

`selection`

    

A `Binding` to the style that the space uses. You can change this value to
change the scene’s style even after you present the immersive space. Even
though you provide a binding, the value changes only if you change it.

`styles`

    

The list of styles that the `selection` input can have. Include any styles
that you plan to use during the lifetime of the scene.

## Return Value

A scene that uses one of the specified `styles`.

## Discussion

Use this modifier to configure the appearance and behavior of an
`ImmersiveSpace`. Specify a style that conforms to the `ImmersionStyle`
protocol, like `mixed` or `full`. For example, the following app defines a
solar system scene that uses full immersion:

## See Also

### Creating an immersive space

`struct ImmersiveSpace`

A scene that presents its content in an unbounded space.

`struct ImmersiveSpaceContentBuilder`

A result builder for composing a collection of immersive space elements.

`protocol ImmersionStyle`

The styles that an immersive space can have.

Protocol

# ImmersionStyle

The styles that an immersive space can have.

visionOS 1.0+

    
    
    protocol ImmersionStyle

## Overview

Configure the appearance and behavior of an `ImmersiveSpace` by adding the
`immersionStyle(selection:in:)` scene modifier to the space and specifying a
style that conforms to this protocol, like `mixed` or `full`. For example, the
following app defines a solar system scene that uses full immersion:

## Topics

### Getting built-in styles

`static var automatic: AutomaticImmersionStyle`

The default immersion style.

Available when `Self` is `AutomaticImmersionStyle`.

`static var full: FullImmersionStyle`

An immersion style that displays unbounded content that completely replaces
passthrough video.

Available when `Self` is `FullImmersionStyle`.

`static var mixed: MixedImmersionStyle`

An immersion style that displays unbounded content intermixed with other app
content, along with passthrough video.

Available when `Self` is `MixedImmersionStyle`.

`static var progressive: ProgressiveImmersionStyle`

An immersion style that displays unbounded content that partially replaces
passthrough video.

Available when `Self` is `ProgressiveImmersionStyle`.

### Supporting types

`struct AutomaticImmersionStyle`

The default style of immersive spaces.

`struct FullImmersionStyle`

An immersion style that displays unbounded content that completely replaces
passthrough video.

`struct MixedImmersionStyle`

An immersion style that displays unbounded content intermixed with other app
content, along with passthrough video.

`struct ProgressiveImmersionStyle`

An immersion style that displays unbounded content that partially replaces
passthrough video.

## Relationships

### Conforming Types

  * `AutomaticImmersionStyle`
  * `FullImmersionStyle`
  * `MixedImmersionStyle`
  * `ProgressiveImmersionStyle`

## See Also

### Creating an immersive space

`struct ImmersiveSpace`

A scene that presents its content in an unbounded space.

`struct ImmersiveSpaceContentBuilder`

A result builder for composing a collection of immersive space elements.

`func immersionStyle(selection: Binding<any ImmersionStyle>, in: any
ImmersionStyle...) -> some Scene`

Sets the style for an immersive space.

Instance Property

# openImmersiveSpace

An action that presents an immersive space.

visionOS 1.0+

    
    
    var openImmersiveSpace: OpenImmersiveSpaceAction { get }

## Discussion

Use this environment value to get the instance of the
`OpenImmersiveSpaceAction` structure for a given `Environment`. Then call the
instance to present a space. You call the instance directly because it defines
`callAsFunction()` methods that Swift calls when you call the instance.

For example, you can define a button that opens a specified planet in an
immersive space:

You indicate which immersive space to open by providing one of the following:

  * A string identifier that you pass through the `id` parameter.

  * A `value` parameter that has a type that matches the type that you specify in the space’s initializer, as in the above example.

  * Both an identifier and a value. This enables you to define multiple spaces that take input values of the same type and distinguish them by their string identifiers.

The call is asynchronous and returns after presenting the space or if an error
occurs. You can check for errors by inspecting the call’s return value, which
is of type `OpenImmersiveSpaceAction.Result`. For example, the call returns an
error if you already have an immersive space open, because the system enables
only one space to be open at a time.

If you provide a value when you open the space, the scene’s trailing closure
receives a binding to the value that you provide. For best performance, use
lightweight data for the presentation value. For structured model values that
conform to `Identifiable`, the value’s identifier makes a good presentation
value, like the `planet.ID` value in the above code.

## See Also

### Opening an immersive space

`struct OpenImmersiveSpaceAction`

An action that presents an immersive space.

Structure

# OpenImmersiveSpaceAction

An action that presents an immersive space.

visionOS 1.0+

    
    
    struct OpenImmersiveSpaceAction

## Overview

Use the `openImmersiveSpace` environment value to get the instance of this
structure for a given `Environment`. Then call the instance to present a
space. You call the instance directly because it defines `callAsFunction()`
methods that Swift calls when you call the instance.

For example, you can define a button that opens a specified planet in an
immersive space:

You indicate which immersive space to open by providing one of the following:

  * A string identifier that you pass through the `id` parameter.

  * A `value` parameter that has a type that matches the type that you specify in the space’s initializer, as in the above example.

  * Both an identifier and a value. This enables you to define multiple spaces that take input values of the same type and distinguish them by their string identifiers.

The call is asynchronous and returns after presenting the space or if an error
occurs. You can check for errors by inspecting the call’s return value, which
is of type `OpenImmersiveSpaceAction.Result`. For example, the call returns an
error if you already have an immersive space open, because the system enables
only one space to be open at a time.

If you provide a value when you open the space, the scene’s trailing closure
receives a binding to the value that you provide. For best performance, use
lightweight data for the presentation value. For structured model values that
conform to `Identifiable`, the value’s identifier makes a good presentation
value, like the `planet.ID` value in the above code.

## Topics

### Calling the action

`func callAsFunction(id: String) async -> OpenImmersiveSpaceAction.Result`

Presents an immersive space for the scene with the specified identifier.

`func callAsFunction<D>(id: String, value: D) async ->
OpenImmersiveSpaceAction.Result`

Presents the immersive space that your app defines for the specified
identifier and that handles the type of the presented value.

`func callAsFunction<D>(value: D) async -> OpenImmersiveSpaceAction.Result`

Presents the immersive space that handles the type of the presented value.

### Getting the result

`enum Result`

The outcome of an attempt to open an immersive space.

## Relationships

### Conforms To

  * `Sendable`

## See Also

### Opening an immersive space

`var openImmersiveSpace: OpenImmersiveSpaceAction`

An action that presents an immersive space.

Instance Property

# dismissImmersiveSpace

An immersive space dismissal action stored in a view’s environment.

visionOS 1.0+

    
    
    var dismissImmersiveSpace: DismissImmersiveSpaceAction { get }

## Discussion

Use this environment value to get a `DismissImmersiveSpaceAction` instance for
a given `Environment`. Then call the instance to dismiss a space. You call the
instance directly because it defines a `callAsFunction()` method that Swift
calls when you call the instance.

For example, you can define a button that dismisses an immersive space:

The asynchronous call returns after the system finishes dismissing the space.
Unlike the call to `openImmersiveSpace` that you use to open the space — which
requires an identifier, a value, or both to specify which space to open — the
dismiss action requires no parameters because there can be only one immersive
space open at a time. The call closes the space that is currently open, if
any.

## See Also

### Closing the immersive space

`struct DismissImmersiveSpaceAction`

An action that dismisses an immersive space.

Structure

# DismissImmersiveSpaceAction

An action that dismisses an immersive space.

visionOS 1.0+

    
    
    struct DismissImmersiveSpaceAction

## Overview

Use the `dismissImmersiveSpace` environment value to get an instance of this
type for a given `Environment`. Then call the instance to dismiss a space. You
call the instance directly because it defines a `callAsFunction()` method that
Swift calls when you call the instance.

For example, you can define a button that dismisses an immersive space:

The asynchronous call returns after the system finishes dismissing the space.
Unlike the call to `openImmersiveSpace` that you use to open the space — which
requires an identifier, a value, or both to specify which space to open — the
dismiss action requires no parameters because there can be only one immersive
space open at a time. The call closes the space that is currently open, if
any.

## Topics

### Calling the action

`func callAsFunction() async`

Dismisses the currently opened immersive space.

## See Also

### Closing the immersive space

`var dismissImmersiveSpace: DismissImmersiveSpaceAction`

An immersive space dismissal action stored in a view’s environment.

Instance Method

# upperLimbVisibility(_:)

Sets the preferred visibility of the user’s upper limbs, while an
`ImmersiveSpace` scene is presented.

visionOS 1.0+

    
    
    func upperLimbVisibility(_ preferredVisibility: Visibility) -> some Scene
    

## Discussion

The system can show the user’s upper limbs during fully immersive experiences,
but you can also hide them, for example, in order to display virtual hands
instead.

Note that this modifier only sets a preference and ultimately the system will
decide if it will honor it or not. The system may by unable to honor the
preference if the immersive space is currently not visible.

## See Also

### Hiding upper limbs during immersion

`func upperLimbVisibility(Visibility) -> some View`

Sets the preferred visibility of the user’s upper limbs, while an
`ImmersiveSpace` scene is presented.

Instance Method

# upperLimbVisibility(_:)

Sets the preferred visibility of the user’s upper limbs, while an
`ImmersiveSpace` scene is presented.

visionOS 1.0+

    
    
    func upperLimbVisibility(_ preferredVisibility: Visibility) -> some View
    

## Discussion

The system can show the user’s upper limbs during fully immersive experiences,
but you can also hide them, for example, in order to display virtual hands
instead.

Note that this modifier only sets a preference and ultimately the system will
decide if it will honor it or not. The system may by unable to honor the
preference if the immersive space is currently not visible.

## See Also

### Hiding upper limbs during immersion

`func upperLimbVisibility(Visibility) -> some Scene`

Sets the preferred visibility of the user’s upper limbs, while an
`ImmersiveSpace` scene is presented.

Instance Method

# immersiveContentBrightness(_:)

Sets the content brightness of an immersive space.

visionOS 1.0+

    
    
    func immersiveContentBrightness(_ brightness: ImmersiveContentBrightness) -> some Scene
    

##  Parameters

`brightness`

    

The level of content brightness that you prefer.

## Return Value

A scene that has the specified content brightness.

## Discussion

Pass one of the standard brightness levels defined in
`ImmersiveContentBrightness` or a custom one that you create with the
`custom(_:)` method to this scene modifier to set a preference for the content
brightness in an `ImmersiveSpace`. The system takes the value that you set
into account, but might not be able to honor a specific preference.

When you do this to create an environment that’s suitable for video playback,
the standard brightness values provide good results for most use cases. To
optimize further, you can create a custom brightness using a normalized value
that expresses the linear brightness ratio between a standard dynamic range
white video frame and the background that surrounds the player window.

Important

This modifier doesn’t affect scenes other than immersive spaces.

## See Also

### Adjusting content brightness

`struct ImmersiveContentBrightness`

The content brightness of an immersive space.

Structure

# ImmersiveContentBrightness

The content brightness of an immersive space.

visionOS 1.0+

    
    
    struct ImmersiveContentBrightness

## Overview

Use a value of this type as an input to the `immersiveContentBrightness(_:)`
scene modifier to indicate the ambient content brightness of an
`ImmersiveSpace`.

When you do this to create an environment that’s suitable for video playback,
use one of the standard brightness values like `bright`, `dim`, or `dark` to
provide good results for most use cases. To optimize further, you can create a
custom brightness using a normalized value that expresses the linear
brightness ratio between a standard dynamic range white video frame and the
background that surrounds the player window.

## Topics

### Type Properties

`static let automatic: ImmersiveContentBrightness`

The default content brightness.

`static let bright: ImmersiveContentBrightness`

A bright content brightness.

`static let dark: ImmersiveContentBrightness`

A dark content brightness.

`static let dim: ImmersiveContentBrightness`

A dimmed content brightness.

### Type Methods

`static func custom(Double) -> ImmersiveContentBrightness`

Creates a content brightness with a custom value.

## Relationships

### Conforms To

  * `Equatable`

## See Also

### Adjusting content brightness

`func immersiveContentBrightness(ImmersiveContentBrightness) -> some Scene`

Sets the content brightness of an immersive space.



# ImmersiveSpaceContentBuilder

Type Method

# buildBlock(_:)

visionOS 1.0+

    
    
    static func buildBlock<Content>(_ content: Content) -> Content where Content : ImmersiveSpaceContent



# ImmersiveContentBrightness

Type Property

# automatic

The default content brightness.

visionOS 1.0+

    
    
    static let automatic: ImmersiveContentBrightness

Type Property

# bright

A bright content brightness.

visionOS 1.0+

    
    
    static let bright: ImmersiveContentBrightness

Type Property

# dark

A dark content brightness.

visionOS 1.0+

    
    
    static let dark: ImmersiveContentBrightness

Type Property

# dim

A dimmed content brightness.

visionOS 1.0+

    
    
    static let dim: ImmersiveContentBrightness

Type Method

# custom(_:)

Creates a content brightness with a custom value.

visionOS 1.0+

    
    
    static func custom(_ value: Double) -> ImmersiveContentBrightness

##  Parameters

`value`

    

The value of the brightness. Provide a value between 0 and 1. Larger values
correspond to a brighter environment.



