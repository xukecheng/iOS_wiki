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

