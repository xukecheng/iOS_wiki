Initializer

# init(eoFill:antialiased:)

Creates a new fill style with the specified settings.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        eoFill: Bool = false,
        antialiased: Bool = true
    )

##  Parameters

`eoFill`

    

A Boolean value that indicates whether to use the even-odd rule for rendering
a shape. Pass `false` to use the non-zero winding number rule instead.

`antialiased`

    

A Boolean value that indicates whether to use antialiasing when rendering the
edges of a shape.

Instance Property

# isEOFilled

A Boolean value that indicates whether to use the even-odd rule when rendering
a shape.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var isEOFilled: Bool

## Discussion

When `isOEFilled` is `false`, the style uses the non-zero winding number rule.

## See Also

### Setting fill style properties

`var isAntialiased: Bool`

A Boolean value that indicates whether to apply antialiasing to the edges of a
shape.

Instance Property

# isAntialiased

A Boolean value that indicates whether to apply antialiasing to the edges of a
shape.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var isAntialiased: Bool

## See Also

### Setting fill style properties

`var isEOFilled: Bool`

A Boolean value that indicates whether to use the even-odd rule when rendering
a shape.

