Type Property

# single

Draw a single solid line.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static let single: Text.LineStyle

Initializer

# init(nsUnderlineStyle:)

Creates a `Text.LineStyle` from `NSUnderlineStyle`.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init?(nsUnderlineStyle: NSUnderlineStyle)

##  Parameters

`nsUnderlineStyle`

    

A value of `NSUnderlineStyle` to wrap with `Text.LineStyle`.

## Return Value

A new `Text.LineStyle` or `nil` when `nsUnderlineStyle` contains styles not
supported by `Text.LineStyle`.

## Discussion

Note

Use this initializer only if you need to convert an existing
`NSUnderlineStyle` to a SwiftUI `Text.LineStyle`. Otherwise, create a
`Text.LineStyle` using an initializer like `init(pattern:color:)`.

## See Also

### Creating a text line style

`init(pattern: Text.LineStyle.Pattern, color: Color?)`

Creates a line style.

`struct Pattern`

The pattern, that the line has.

Initializer

# init(pattern:color:)

Creates a line style.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init(
        pattern: Text.LineStyle.Pattern = .solid,
        color: Color? = nil
    )

##  Parameters

`pattern`

    

The pattern of the line.

`color`

    

The color of the line. If not provided, the foreground color of text is used.

## See Also

### Creating a text line style

`init?(nsUnderlineStyle: NSUnderlineStyle)`

Creates a `Text.LineStyle` from `NSUnderlineStyle`.

`struct Pattern`

The pattern, that the line has.

Structure

# Text.LineStyle.Pattern

The pattern, that the line has.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    struct Pattern

## Topics

### Getting line style patterns

`static let solid: Text.LineStyle.Pattern`

Draw a solid line.

`static let dot: Text.LineStyle.Pattern`

Draw a line of dots.

`static let dash: Text.LineStyle.Pattern`

Draw a line of dashes.

`static let dashDot: Text.LineStyle.Pattern`

`static let dashDotDot: Text.LineStyle.Pattern`

Draw a line of alternating dashes and two dots.

## Relationships

### Conforms To

  * `Sendable`

## See Also

### Creating a text line style

`init?(nsUnderlineStyle: NSUnderlineStyle)`

Creates a `Text.LineStyle` from `NSUnderlineStyle`.

`init(pattern: Text.LineStyle.Pattern, color: Color?)`

Creates a line style.

