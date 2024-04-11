Initializer

# init(cornerRadius:style:)

Creates a new rounded rectangle shape.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        cornerRadius: CGFloat,
        style: RoundedCornerStyle = .continuous
    )

##  Parameters

`cornerRadius`

    

the radius of the rounded corners.

`style`

    

the style of corners drawn by the shape.

## See Also

### Creating a rounded rectangle

`init(cornerSize: CGSize, style: RoundedCornerStyle)`

Creates a new rounded rectangle shape.

Initializer

# init(cornerSize:style:)

Creates a new rounded rectangle shape.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        cornerSize: CGSize,
        style: RoundedCornerStyle = .continuous
    )

##  Parameters

`cornerSize`

    

the width and height of the rounded corners.

`style`

    

the style of corners drawn by the shape.

## See Also

### Creating a rounded rectangle

`init(cornerRadius: CGFloat, style: RoundedCornerStyle)`

Creates a new rounded rectangle shape.

Instance Property

# cornerSize

The width and height of the rounded rectangle’s corners.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var cornerSize: CGSize

## See Also

### Getting the shape’s characteristics

`var style: RoundedCornerStyle`

The style of corners drawn by the rounded rectangle.

Instance Property

# style

The style of corners drawn by the rounded rectangle.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var style: RoundedCornerStyle

## See Also

### Getting the shape’s characteristics

`var cornerSize: CGSize`

The width and height of the rounded rectangle’s corners.

Instance Property

# animatableData

The data to animate.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var animatableData: CGSize.AnimatableData { get set }

