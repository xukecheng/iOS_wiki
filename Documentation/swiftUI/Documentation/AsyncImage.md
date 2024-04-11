Initializer

# init(url:scale:)

Loads and displays an image from the specified URL.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init(
        url: URL?,
        scale: CGFloat = 1
    ) where Content == Image

##  Parameters

`url`

    

The URL of the image to display.

`scale`

    

The scale to use for the image. The default is `1`. Set a different value when
loading images designed for higher resolution displays. For example, set a
value of `2` for an image that you would name with the `@2x` suffix if stored
in a file on disk.

## Discussion

Until the image loads, SwiftUI displays a default placeholder. When the load
operation completes successfully, SwiftUI updates the view to show the loaded
image. If the operation fails, SwiftUI continues to display the placeholder.
The following example loads and displays an icon from an example server:

If you want to customize the placeholder or apply image-specific modifiers —
like `resizable(capInsets:resizingMode:)` — to the loaded image, use the
`init(url:scale:content:placeholder:)` initializer instead.

## See Also

### Loading an image

`init<I, P>(url: URL?, scale: CGFloat, content: (Image) -> I, placeholder: ()
-> P)`

Loads and displays a modifiable image from the specified URL using a custom
placeholder until the image loads.

Initializer

# init(url:scale:content:placeholder:)

Loads and displays a modifiable image from the specified URL using a custom
placeholder until the image loads.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init<I, P>(
        url: URL?,
        scale: CGFloat = 1,
        @ViewBuilder content: @escaping (Image) -> I,
        @ViewBuilder placeholder: @escaping () -> P
    ) where Content == _ConditionalContent<I, P>, I : View, P : View

##  Parameters

`url`

    

The URL of the image to display.

`scale`

    

The scale to use for the image. The default is `1`. Set a different value when
loading images designed for higher resolution displays. For example, set a
value of `2` for an image that you would name with the `@2x` suffix if stored
in a file on disk.

`content`

    

A closure that takes the loaded image as an input, and returns the view to
show. You can return the image directly, or modify it as needed before
returning it.

`placeholder`

    

A closure that returns the view to show until the load operation completes
successfully.

## Discussion

Until the image loads, SwiftUI displays the placeholder view that you specify.
When the load operation completes successfully, SwiftUI updates the view to
show content that you specify, which you create using the loaded image. For
example, you can show a green placeholder, followed by a tiled version of the
loaded image:

If the load operation fails, SwiftUI continues to display the placeholder. To
be able to display a different view on a load error, use the
`init(url:scale:transaction:content:)` initializer instead.

## See Also

### Loading an image

`init(url: URL?, scale: CGFloat)`

Loads and displays an image from the specified URL.

Initializer

# init(url:scale:transaction:content:)

Loads and displays a modifiable image from the specified URL in phases.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init(
        url: URL?,
        scale: CGFloat = 1,
        transaction: Transaction = Transaction(),
        @ViewBuilder content: @escaping (AsyncImagePhase) -> Content
    )

##  Parameters

`url`

    

The URL of the image to display.

`scale`

    

The scale to use for the image. The default is `1`. Set a different value when
loading images designed for higher resolution displays. For example, set a
value of `2` for an image that you would name with the `@2x` suffix if stored
in a file on disk.

`transaction`

    

The transaction to use when the phase changes.

`content`

    

A closure that takes the load phase as an input, and returns the view to
display for the specified phase.

## Discussion

If you set the asynchronous image’s URL to `nil`, or after you set the URL to
a value but before the load operation completes, the phase is
`AsyncImagePhase.empty`. After the operation completes, the phase becomes
either `AsyncImagePhase.failure(_:)` or `AsyncImagePhase.success(_:)`. In the
first case, the phase’s `error` value indicates the reason for failure. In the
second case, the phase’s `image` property contains the loaded image. Use the
phase to drive the output of the `content` closure, which defines the view’s
appearance:

To add transitions when you change the URL, apply an identifier to the
`AsyncImage`.

