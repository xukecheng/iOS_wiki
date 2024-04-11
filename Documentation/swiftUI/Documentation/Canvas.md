Initializer

# init(opaque:colorMode:rendersAsynchronously:renderer:)

Creates and configures a canvas.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init(
        opaque: Bool = false,
        colorMode: ColorRenderingMode = .nonLinear,
        rendersAsynchronously: Bool = false,
        renderer: @escaping (inout GraphicsContext, CGSize) -> Void
    )

Available when `Symbols` is `EmptyView`.

##  Parameters

`opaque`

    

A Boolean that indicates whether the canvas is fully opaque. You might be able
to improve performance by setting this value to `true`, but then drawing a
non-opaque image into the context produces undefined results. The default is
`false`.

`colorMode`

    

A working color space and storage format of the canvas. The default is
`ColorRenderingMode.nonLinear`.

`rendersAsynchronously`

    

A Boolean that indicates whether the canvas can present its contents to its
parent view asynchronously. The default is `false`.

`renderer`

    

A closure in which you conduct immediate mode drawing. The closure takes two
inputs: a context that you use to issue drawing commands and a size —
representing the current size of the canvas — that you can use to customize
the content. The canvas calls the renderer any time it needs to redraw the
content.

## Discussion

Use this initializer to create a new canvas that you can draw into. For
example, you can draw a path:

The example above draws the outline of an ellipse that exactly inscribes a
canvas with a blue border:

For information about using a context to draw into a canvas, see
`GraphicsContext`. If you want to provide SwiftUI views for the renderer to
use as drawing elements, use
`init(opaque:colorMode:rendersAsynchronously:renderer:symbols:)` instead.

## See Also

### Creating a canvas

`init(opaque: Bool, colorMode: ColorRenderingMode, rendersAsynchronously:
Bool, renderer: (inout GraphicsContext, CGSize) -> Void, symbols: () ->
Symbols)`

Creates and configures a canvas that you supply with renderable child views.

Initializer

# init(opaque:colorMode:rendersAsynchronously:renderer:symbols:)

Creates and configures a canvas that you supply with renderable child views.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init(
        opaque: Bool = false,
        colorMode: ColorRenderingMode = .nonLinear,
        rendersAsynchronously: Bool = false,
        renderer: @escaping (inout GraphicsContext, CGSize) -> Void,
        @ViewBuilder symbols: () -> Symbols
    )

##  Parameters

`opaque`

    

A Boolean that indicates whether the canvas is fully opaque. You might be able
to improve performance by setting this value to `true`, but then drawing a
non-opaque image into the context produces undefined results. The default is
`false`.

`colorMode`

    

A working color space and storage format of the canvas. The default is
`ColorRenderingMode.nonLinear`.

`rendersAsynchronously`

    

A Boolean that indicates whether the canvas can present its contents to its
parent view asynchronously. The default is `false`.

`renderer`

    

A closure in which you conduct immediate mode drawing. The closure takes two
inputs: a context that you use to issue drawing commands and a size —
representing the current size of the canvas — that you can use to customize
the content. The canvas calls the renderer any time it needs to redraw the
content.

`symbols`

    

A `ViewBuilder` that you use to supply SwiftUI views to the canvas for use
during drawing. Uniquely tag each view using the `tag(_:)` modifier, so that
you can find them from within your renderer using the `resolveSymbol(id:)`
method.

## Discussion

This initializer behaves like the
`init(opaque:colorMode:rendersAsynchronously:renderer:)` initializer, except
that you also provide a collection of SwiftUI views for the renderer to use as
drawing elements.

SwiftUI stores a rendered version of each child view that you specify in the
`symbols` view builder and makes these available to the canvas. Tag each child
view so that you can retrieve it from within the renderer using the
`resolveSymbol(id:)` method. For example, you can create a scatter plot using
a passed-in child view as the mark for each data point:

You can use any SwiftUI view for the `mark` input:

If the `rects` input contains 50 randomly arranged `CGRect` instances, SwiftUI
draws a plot like this:

The symbol inputs, like all other elements that you draw to the canvas, lack
individual accessibility and interactivity, even if the original SwiftUI view
has these attributes. However, you can add accessibility and interactivity
modifers to the canvas as a whole.

## See Also

### Creating a canvas

`init(opaque: Bool, colorMode: ColorRenderingMode, rendersAsynchronously:
Bool, renderer: (inout GraphicsContext, CGSize) -> Void)`

Creates and configures a canvas.

Available when `Symbols` is `EmptyView`.

Instance Property

# isOpaque

A Boolean that indicates whether the canvas is fully opaque.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var isOpaque: Bool { get set }

## Discussion

You might be able to improve performance by setting this value to `true`,
making the canvas is fully opaque. However, in that case, the result of
drawing a non-opaque image into the canvas is undefined.

## See Also

### Managing opacity and color

`var colorMode: ColorRenderingMode`

The working color space and storage format of the canvas.

Instance Property

# colorMode

The working color space and storage format of the canvas.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var colorMode: ColorRenderingMode { get set }

## See Also

### Managing opacity and color

`var isOpaque: Bool`

A Boolean that indicates whether the canvas is fully opaque.

Instance Property

# symbols

A view that provides child views that you can use in the drawing callback.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var symbols: Symbols

## Discussion

Uniquely tag each child view using the `tag(_:)` modifier, so that you can
find them from within your renderer using the `resolveSymbol(id:)` method.

Instance Property

# rendersAsynchronously

A Boolean that indicates whether the canvas can present its contents to its
parent view asynchronously.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var rendersAsynchronously: Bool { get set }

## See Also

### Rendering

`var renderer: (inout GraphicsContext, CGSize) -> Void`

The drawing callback that you use to draw into the canvas.

Instance Property

# renderer

The drawing callback that you use to draw into the canvas.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var renderer: (inout GraphicsContext, CGSize) -> Void

##  Parameters

`context`

    

The graphics context to draw into.

`size`

    

The current size of the view.

## See Also

### Rendering

`var rendersAsynchronously: Bool`

A Boolean that indicates whether the canvas can present its contents to its
parent view asynchronously.

