Initializer

# init(alignment:horizontalSpacing:verticalSpacing:)

Creates a grid with the specified spacing and alignment.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init(
        alignment: Alignment = .center,
        horizontalSpacing: CGFloat? = nil,
        verticalSpacing: CGFloat? = nil
    )

##  Parameters

`alignment`

    

The guide for aligning subviews within the space allocated for a given cell.
The default is `center`.

`horizontalSpacing`

    

The horizontal distance between each cell, given in points. The value is `nil`
by default, which results in a default distance between cells that’s
appropriate for the platform.

`verticalSpacing`

    

The vertical distance between each cell, given in points. The value is `nil`
by default, which results in a default distance between cells that’s
appropriate for the platform.

Instance Property

# alignment

The alignment of subviews.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var alignment: Alignment

## See Also

### Getting the grid’s properties

`var horizontalSpacing: CGFloat?`

The horizontal distance between adjacent subviews.

`var verticalSpacing: CGFloat?`

The vertical distance between adjacent subviews.

Instance Property

# horizontalSpacing

The horizontal distance between adjacent subviews.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var horizontalSpacing: CGFloat?

## Discussion

Set this value to `nil` to use default horizonal distances between subviews.

## See Also

### Getting the grid’s properties

`var alignment: Alignment`

The alignment of subviews.

`var verticalSpacing: CGFloat?`

The vertical distance between adjacent subviews.

Instance Property

# verticalSpacing

The vertical distance between adjacent subviews.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var verticalSpacing: CGFloat?

## Discussion

Set this value to `nil` to use default vertical distances between subviews.

## See Also

### Getting the grid’s properties

`var alignment: Alignment`

The alignment of subviews.

`var horizontalSpacing: CGFloat?`

The horizontal distance between adjacent subviews.

Collection

API Collection

# Layout Implementations

## Topics

### Structures

`struct Cache`

A stateful grid layout algorithm.

