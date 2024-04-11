Instance Method

# firstBaseline(in:)

Gets the distance from the first line’s ascender to its baseline.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func firstBaseline(in size: CGSize) -> CGFloat

## See Also

### Getting the text properties

`func lastBaseline(in: CGSize) -> CGFloat`

Gets the distance from the first line’s ascender to the last line’s baseline.

`func measure(in: CGSize) -> CGSize`

Measures the size of the resolved text for a given area into which the text
should be placed.

`var shading: GraphicsContext.Shading`

The shading to fill uncolored text regions with.

Instance Method

# lastBaseline(in:)

Gets the distance from the first line’s ascender to the last line’s baseline.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func lastBaseline(in size: CGSize) -> CGFloat

## See Also

### Getting the text properties

`func firstBaseline(in: CGSize) -> CGFloat`

Gets the distance from the first line’s ascender to its baseline.

`func measure(in: CGSize) -> CGSize`

Measures the size of the resolved text for a given area into which the text
should be placed.

`var shading: GraphicsContext.Shading`

The shading to fill uncolored text regions with.

Instance Method

# measure(in:)

Measures the size of the resolved text for a given area into which the text
should be placed.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func measure(in size: CGSize) -> CGSize

##  Parameters

`size`

    

The area to place the `Text` view in.

## See Also

### Getting the text properties

`func firstBaseline(in: CGSize) -> CGFloat`

Gets the distance from the first line’s ascender to its baseline.

`func lastBaseline(in: CGSize) -> CGFloat`

Gets the distance from the first line’s ascender to the last line’s baseline.

`var shading: GraphicsContext.Shading`

The shading to fill uncolored text regions with.

Instance Property

# shading

The shading to fill uncolored text regions with.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var shading: GraphicsContext.Shading

## Discussion

This value defaults to the `foreground` shading.

## See Also

### Getting the text properties

`func firstBaseline(in: CGSize) -> CGFloat`

Gets the distance from the first line’s ascender to its baseline.

`func lastBaseline(in: CGSize) -> CGFloat`

Gets the distance from the first line’s ascender to the last line’s baseline.

`func measure(in: CGSize) -> CGSize`

Measures the size of the resolved text for a given area into which the text
should be placed.

