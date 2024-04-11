Initializer

# init(alignment:spacing:)

Creates a horizontal stack with the specified spacing and vertical alignment.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init(
        alignment: VerticalAlignment = .center,
        spacing: CGFloat? = nil
    )

##  Parameters

`alignment`

    

The guide for aligning the subviews in this stack. It has the same vertical
screen coordinate for all subviews.

`spacing`

    

The distance between adjacent subviews. Set this value to `nil` to use default
distances between subviews.

Instance Property

# alignment

The vertical alignment of subviews.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var alignment: VerticalAlignment

## See Also

### Getting the stack’s properties

`var spacing: CGFloat?`

The distance between adjacent subviews.

Instance Property

# spacing

The distance between adjacent subviews.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var spacing: CGFloat?

## Discussion

Set this value to `nil` to use default distances between subviews.

## See Also

### Getting the stack’s properties

`var alignment: VerticalAlignment`

The vertical alignment of subviews.

