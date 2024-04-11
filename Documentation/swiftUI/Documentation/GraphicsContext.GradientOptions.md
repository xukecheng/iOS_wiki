Type Property

# linearColor

An option that interpolates between colors in a linear color space.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var linearColor: GraphicsContext.GradientOptions { get }

## See Also

### Getting gradient options

`static var mirror: GraphicsContext.GradientOptions`

An option that repeats the gradient outside its nominal range, reflecting
every other instance.

`static var `repeat`: GraphicsContext.GradientOptions`

An option that repeats the gradient outside its nominal range.

Type Property

# mirror

An option that repeats the gradient outside its nominal range, reflecting
every other instance.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var mirror: GraphicsContext.GradientOptions { get }

## Discussion

Use this option to cause the gradient to repeat its pattern in areas that
exceed the bounds of its start and end points. The repetitions alternately
reverse the start and end points, producing a pattern like `0 -> 1`, `1 -> 0`,
`0 -> 1`, and so on.

Without either this option or `repeat`, the gradient stops at the end of its
range. This option takes precendence if you set both this one and `repeat`.

## See Also

### Getting gradient options

`static var linearColor: GraphicsContext.GradientOptions`

An option that interpolates between colors in a linear color space.

`static var `repeat`: GraphicsContext.GradientOptions`

An option that repeats the gradient outside its nominal range.

Type Property

# repeat

An option that repeats the gradient outside its nominal range.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var `repeat`: GraphicsContext.GradientOptions { get }

## Discussion

Use this option to cause the gradient to repeat its pattern in areas that
exceed the bounds of its start and end points. The repetitions use the same
start and end value for each repetition.

Without this option or `mirror`, the gradient stops at the end of its range.
The `mirror` option takes precendence if you set both this one and that one.

## See Also

### Getting gradient options

`static var linearColor: GraphicsContext.GradientOptions`

An option that interpolates between colors in a linear color space.

`static var mirror: GraphicsContext.GradientOptions`

An option that repeats the gradient outside its nominal range, reflecting
every other instance.

