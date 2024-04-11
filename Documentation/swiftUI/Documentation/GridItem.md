Initializer

# init(_:spacing:alignment:)

Creates a grid item with the specified size, spacing, and alignment.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(
        _ size: GridItem.Size = .flexible(),
        spacing: CGFloat? = nil,
        alignment: Alignment? = nil
    )

##  Parameters

`size`

    

The size of the grid item.

`spacing`

    

The spacing to use between this and the next item.

`alignment`

    

The alignment to use for this grid item.

Instance Property

# alignment

The alignment to use when placing each view.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    var alignment: Alignment?

## Discussion

Use this property to anchor the view’s relative position to the same relative
position in the view’s assigned grid space.

## See Also

### Inspecting grid item properties

`var spacing: CGFloat?`

The spacing to the next item.

`var size: GridItem.Size`

The size of the item, which is the width of a column item or the height of a
row item.

`enum Size`

The size in the minor axis of one or more rows or columns in a grid layout.

Instance Property

# spacing

The spacing to the next item.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    var spacing: CGFloat?

## Discussion

If this value is `nil`, the item uses a reasonable default for the current
platform.

## See Also

### Inspecting grid item properties

`var alignment: Alignment?`

The alignment to use when placing each view.

`var size: GridItem.Size`

The size of the item, which is the width of a column item or the height of a
row item.

`enum Size`

The size in the minor axis of one or more rows or columns in a grid layout.

Instance Property

# size

The size of the item, which is the width of a column item or the height of a
row item.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    var size: GridItem.Size

## See Also

### Inspecting grid item properties

`var alignment: Alignment?`

The alignment to use when placing each view.

`var spacing: CGFloat?`

The spacing to the next item.

`enum Size`

The size in the minor axis of one or more rows or columns in a grid layout.

Enumeration

# GridItem.Size

The size in the minor axis of one or more rows or columns in a grid layout.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    enum Size

## Overview

Use a `Size` instance when you create a `GridItem`. The value tells a
`LazyHGrid` how to size its rows, or a `LazyVGrid` how to size its columns.

## Topics

### Getting the sizes

`case adaptive(minimum: CGFloat, maximum: CGFloat)`

Multiple items in the space of a single flexible item.

`case fixed(CGFloat)`

A single item with the specified fixed size.

`case flexible(minimum: CGFloat, maximum: CGFloat)`

A single flexible item.

## Relationships

### Conforms To

  * `Sendable`

## See Also

### Inspecting grid item properties

`var alignment: Alignment?`

The alignment to use when placing each view.

`var spacing: CGFloat?`

The spacing to the next item.

`var size: GridItem.Size`

The size of the item, which is the width of a column item or the height of a
row item.

