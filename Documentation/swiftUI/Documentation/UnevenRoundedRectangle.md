Initializer

# init(cornerRadii:style:)

Creates a new rounded rectangle shape with uneven corners.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init(
        cornerRadii: RectangleCornerRadii,
        style: RoundedCornerStyle = .continuous
    )

##  Parameters

`cornerRadii`

    

the radii of each corner.

`style`

    

the style of corners drawn by the shape.

## See Also

### Creating an uneven rounded rectangle

`init(topLeadingRadius: CGFloat, bottomLeadingRadius: CGFloat,
bottomTrailingRadius: CGFloat, topTrailingRadius: CGFloat, style:
RoundedCornerStyle)`

Creates a new rounded rectangle shape with uneven corners.

Initializer

#
init(topLeadingRadius:bottomLeadingRadius:bottomTrailingRadius:topTrailingRadius:style:)

Creates a new rounded rectangle shape with uneven corners.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init(
        topLeadingRadius: CGFloat = 0,
        bottomLeadingRadius: CGFloat = 0,
        bottomTrailingRadius: CGFloat = 0,
        topTrailingRadius: CGFloat = 0,
        style: RoundedCornerStyle = .continuous
    )

## See Also

### Creating an uneven rounded rectangle

`init(cornerRadii: RectangleCornerRadii, style: RoundedCornerStyle)`

Creates a new rounded rectangle shape with uneven corners.

Instance Property

# cornerRadii

The radii of each corner of the rounded rectangle.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var cornerRadii: RectangleCornerRadii

## See Also

### Getting the shape’s characteristics

`var style: RoundedCornerStyle`

The style of corners drawn by the rounded rectangle.

Instance Property

# style

The style of corners drawn by the rounded rectangle.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var style: RoundedCornerStyle

## See Also

### Getting the shape’s characteristics

`var cornerRadii: RectangleCornerRadii`

The radii of each corner of the rounded rectangle.

Instance Property

# animatableData

The data to animate.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var animatableData: RectangleCornerRadii.AnimatableData { get set }

