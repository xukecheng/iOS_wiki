Type Property

# hierarchical

A mode that renders symbols as multiple layers, with different opacities
applied to the foreground style.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static let hierarchical: SymbolRenderingMode

## Discussion

SwiftUI fills the first layer with the foreground style, and the others the
secondary, and tertiary variants of the foreground style. You can specify
these styles explicitly using the `foregroundStyle(_:_:)` and
`foregroundStyle(_:_:_:)` modifiers. If you only specify a primary foreground
style, SwiftUI automatically derives the others from that style. For example,
you can render a filled exclamation mark triangle with purple as the tint
color for the exclamation mark, and lower opacity purple for the triangle:

## See Also

### Getting symbol rendering modes

`static let monochrome: SymbolRenderingMode`

A mode that renders symbols as a single layer filled with the foreground
style.

`static let multicolor: SymbolRenderingMode`

A mode that renders symbols as multiple layers with their inherit styles.

`static let palette: SymbolRenderingMode`

A mode that renders symbols as multiple layers, with different styles applied
to the layers.

Type Property

# monochrome

A mode that renders symbols as a single layer filled with the foreground
style.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static let monochrome: SymbolRenderingMode

## Discussion

For example, you can render a filled exclamation mark triangle in purple:

## See Also

### Getting symbol rendering modes

`static let hierarchical: SymbolRenderingMode`

A mode that renders symbols as multiple layers, with different opacities
applied to the foreground style.

`static let multicolor: SymbolRenderingMode`

A mode that renders symbols as multiple layers with their inherit styles.

`static let palette: SymbolRenderingMode`

A mode that renders symbols as multiple layers, with different styles applied
to the layers.

Type Property

# multicolor

A mode that renders symbols as multiple layers with their inherit styles.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static let multicolor: SymbolRenderingMode

## Discussion

The layers may be filled with their own inherent styles, or the foreground
style. For example, you can render a filled exclamation mark triangle in its
inherent colors, with yellow for the triangle and white for the exclamation
mark:

## See Also

### Getting symbol rendering modes

`static let hierarchical: SymbolRenderingMode`

A mode that renders symbols as multiple layers, with different opacities
applied to the foreground style.

`static let monochrome: SymbolRenderingMode`

A mode that renders symbols as a single layer filled with the foreground
style.

`static let palette: SymbolRenderingMode`

A mode that renders symbols as multiple layers, with different styles applied
to the layers.

Type Property

# palette

A mode that renders symbols as multiple layers, with different styles applied
to the layers.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static let palette: SymbolRenderingMode

## Discussion

In this mode SwiftUI maps each successively defined layer in the image to the
next of the primary, secondary, and tertiary variants of the foreground style.
You can specify these styles explicitly using the `foregroundStyle(_:_:)` and
`foregroundStyle(_:_:_:)` modifiers. If you only specify a primary foreground
style, SwiftUI automatically derives the others from that style. For example,
you can render a filled exclamation mark triangle with yellow as the tint
color for the exclamation mark, and fill the triangle with cyan:

You can also omit the symbol rendering mode, as specifying multiple foreground
styles implies switching to palette rendering mode:

## See Also

### Getting symbol rendering modes

`static let hierarchical: SymbolRenderingMode`

A mode that renders symbols as multiple layers, with different opacities
applied to the foreground style.

`static let monochrome: SymbolRenderingMode`

A mode that renders symbols as a single layer filled with the foreground
style.

`static let multicolor: SymbolRenderingMode`

A mode that renders symbols as multiple layers with their inherit styles.

