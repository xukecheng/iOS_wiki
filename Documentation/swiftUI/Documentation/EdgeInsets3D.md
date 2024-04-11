Instance Property

# top

The inset distance along the top face of a 3D volume.

visionOS 1.0+

    
    
    var top: CGFloat

## See Also

### Getting edge insets

`var bottom: CGFloat`

The inset distance along the bottom face of a 3D volume.

`var leading: CGFloat`

The inset distance along the leading face of a 3D volume.

`var trailing: CGFloat`

The inset distance along the top trailing of a 3D volume.

`var front: CGFloat`

The inset distance along the top front of a 3D volume.

`var back: CGFloat`

The inset distance along the top back of a 3D volume.

Instance Property

# bottom

The inset distance along the bottom face of a 3D volume.

visionOS 1.0+

    
    
    var bottom: CGFloat

## See Also

### Getting edge insets

`var top: CGFloat`

The inset distance along the top face of a 3D volume.

`var leading: CGFloat`

The inset distance along the leading face of a 3D volume.

`var trailing: CGFloat`

The inset distance along the top trailing of a 3D volume.

`var front: CGFloat`

The inset distance along the top front of a 3D volume.

`var back: CGFloat`

The inset distance along the top back of a 3D volume.

Instance Property

# leading

The inset distance along the leading face of a 3D volume.

visionOS 1.0+

    
    
    var leading: CGFloat

## See Also

### Getting edge insets

`var top: CGFloat`

The inset distance along the top face of a 3D volume.

`var bottom: CGFloat`

The inset distance along the bottom face of a 3D volume.

`var trailing: CGFloat`

The inset distance along the top trailing of a 3D volume.

`var front: CGFloat`

The inset distance along the top front of a 3D volume.

`var back: CGFloat`

The inset distance along the top back of a 3D volume.

Instance Property

# trailing

The inset distance along the top trailing of a 3D volume.

visionOS 1.0+

    
    
    var trailing: CGFloat

## See Also

### Getting edge insets

`var top: CGFloat`

The inset distance along the top face of a 3D volume.

`var bottom: CGFloat`

The inset distance along the bottom face of a 3D volume.

`var leading: CGFloat`

The inset distance along the leading face of a 3D volume.

`var front: CGFloat`

The inset distance along the top front of a 3D volume.

`var back: CGFloat`

The inset distance along the top back of a 3D volume.

Instance Property

# front

The inset distance along the top front of a 3D volume.

visionOS 1.0+

    
    
    var front: CGFloat

## See Also

### Getting edge insets

`var top: CGFloat`

The inset distance along the top face of a 3D volume.

`var bottom: CGFloat`

The inset distance along the bottom face of a 3D volume.

`var leading: CGFloat`

The inset distance along the leading face of a 3D volume.

`var trailing: CGFloat`

The inset distance along the top trailing of a 3D volume.

`var back: CGFloat`

The inset distance along the top back of a 3D volume.

Instance Property

# back

The inset distance along the top back of a 3D volume.

visionOS 1.0+

    
    
    var back: CGFloat

## See Also

### Getting edge insets

`var top: CGFloat`

The inset distance along the top face of a 3D volume.

`var bottom: CGFloat`

The inset distance along the bottom face of a 3D volume.

`var leading: CGFloat`

The inset distance along the leading face of a 3D volume.

`var trailing: CGFloat`

The inset distance along the top trailing of a 3D volume.

`var front: CGFloat`

The inset distance along the top front of a 3D volume.

Initializer

# init(horizontal:vertical:depth:)

Creates an `EdgeInsets3D` value with values provided for each axis.

visionOS 1.0+

    
    
    init(
        horizontal: CGFloat = 0,
        vertical: CGFloat = 0,
        depth: CGFloat = 0
    )

##  Parameters

`horizontal`

    

The insets to apply along the horizontal axis.

`vertical`

    

The insets to apply along the vertical axis.

`depth`

    

The insets to apply along the depth axis.

## See Also

### Creating an edge inset

`init(top: CGFloat, leading: CGFloat, bottom: CGFloat, trailing: CGFloat,
front: CGFloat, back: CGFloat)`

Creates an `EdgeInsets3D` value with values provided for each face.

Initializer

# init(top:leading:bottom:trailing:front:back:)

Creates an `EdgeInsets3D` value with values provided for each face.

visionOS 1.0+

    
    
    init(
        top: CGFloat = 0,
        leading: CGFloat = 0,
        bottom: CGFloat = 0,
        trailing: CGFloat = 0,
        front: CGFloat = 0,
        back: CGFloat = 0
    )

## See Also

### Creating an edge inset

`init(horizontal: CGFloat, vertical: CGFloat, depth: CGFloat)`

Creates an `EdgeInsets3D` value with values provided for each axis.

