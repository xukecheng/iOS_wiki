Instance Method

# brightness(_:)

Brightens the view by the specified amount.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func brightness(_ amount: Double) -> some VisualEffect
    

##  Parameters

`amount`

    

A value between 0 (no effect) and 1 (full white brightening) that represents
the intensity of the brightness effect.

## Return Value

An effect that brightens the view by the specified amount.

## See Also

### Adjusting Color

`func colorEffect(Shader, isEnabled: Bool) -> some VisualEffect`

Returns a new visual effect that applies `shader` to `self` as a filter effect
on the color of each pixel.

`func contrast(Double) -> some VisualEffect`

Sets the contrast and separation between similar colors in the view.

`func grayscale(Double) -> some VisualEffect`

Adds a grayscale effect to the view.

`func hueRotation(Angle) -> some VisualEffect`

Applies a hue rotation effect to the view.

`func saturation(Double) -> some VisualEffect`

Adjusts the color saturation of the view.

`func opacity(Double) -> some VisualEffect`

Sets the transparency of the view.

Instance Method

# colorEffect(_:isEnabled:)

Returns a new visual effect that applies `shader` to `self` as a filter effect
on the color of each pixel.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    func colorEffect(
        _ shader: Shader,
        isEnabled: Bool = true
    ) -> some VisualEffect
    

##  Parameters

`shader`

    

The shader to apply to `self` as a color filter.

`isEnabled`

    

Whether the effect is enabled or not.

## Return Value

A new view that renders `self` with the shader applied as a color filter.

## Discussion

For a shader function to act as a color filter it must have a function
signature matching:

where `position` is the user-space coordinates of the pixel applied to the
shader and `color` its source color, as a pre-multiplied color in the
destination color space. `args...` should be compatible with the uniform
arguments bound to `shader`. The function should return the modified color
value.

Important

Views backed by AppKit or UIKit views may not render into the filtered layer.
Instead, they log a warning and display a placeholder image to highlight the
error.

## See Also

### Adjusting Color

`func brightness(Double) -> some VisualEffect`

Brightens the view by the specified amount.

`func contrast(Double) -> some VisualEffect`

Sets the contrast and separation between similar colors in the view.

`func grayscale(Double) -> some VisualEffect`

Adds a grayscale effect to the view.

`func hueRotation(Angle) -> some VisualEffect`

Applies a hue rotation effect to the view.

`func saturation(Double) -> some VisualEffect`

Adjusts the color saturation of the view.

`func opacity(Double) -> some VisualEffect`

Sets the transparency of the view.

Instance Method

# contrast(_:)

Sets the contrast and separation between similar colors in the view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func contrast(_ amount: Double) -> some VisualEffect
    

##  Parameters

`amount`

    

The intensity of color contrast to apply. negative values invert colors in
addition to applying contrast.

## Return Value

An effect that applies color contrast to the view.

## Discussion

Apply contrast to a view to increase or decrease the separation between
similar colors in the view.

## See Also

### Adjusting Color

`func brightness(Double) -> some VisualEffect`

Brightens the view by the specified amount.

`func colorEffect(Shader, isEnabled: Bool) -> some VisualEffect`

Returns a new visual effect that applies `shader` to `self` as a filter effect
on the color of each pixel.

`func grayscale(Double) -> some VisualEffect`

Adds a grayscale effect to the view.

`func hueRotation(Angle) -> some VisualEffect`

Applies a hue rotation effect to the view.

`func saturation(Double) -> some VisualEffect`

Adjusts the color saturation of the view.

`func opacity(Double) -> some VisualEffect`

Sets the transparency of the view.

Instance Method

# grayscale(_:)

Adds a grayscale effect to the view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func grayscale(_ amount: Double) -> some VisualEffect
    

##  Parameters

`amount`

    

The intensity of grayscale to apply from 0.0 to less than 1.0. Values closer
to 0.0 are more colorful, and values closer to 1.0 are less colorful.

## Return Value

An effect that reduces the intensity of colors in the view.

## Discussion

A grayscale effect reduces the intensity of colors in the view.

## See Also

### Adjusting Color

`func brightness(Double) -> some VisualEffect`

Brightens the view by the specified amount.

`func colorEffect(Shader, isEnabled: Bool) -> some VisualEffect`

Returns a new visual effect that applies `shader` to `self` as a filter effect
on the color of each pixel.

`func contrast(Double) -> some VisualEffect`

Sets the contrast and separation between similar colors in the view.

`func hueRotation(Angle) -> some VisualEffect`

Applies a hue rotation effect to the view.

`func saturation(Double) -> some VisualEffect`

Adjusts the color saturation of the view.

`func opacity(Double) -> some VisualEffect`

Sets the transparency of the view.

Instance Method

# hueRotation(_:)

Applies a hue rotation effect to the view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func hueRotation(_ angle: Angle) -> some VisualEffect
    

##  Parameters

`angle`

    

The hue rotation angle to apply to the colors in the view.

## Return Value

An effect that shifts all of the colors in the view.

## Discussion

Use hue rotation effect to shift all of the colors in a view according to the
angle you specify.

## See Also

### Adjusting Color

`func brightness(Double) -> some VisualEffect`

Brightens the view by the specified amount.

`func colorEffect(Shader, isEnabled: Bool) -> some VisualEffect`

Returns a new visual effect that applies `shader` to `self` as a filter effect
on the color of each pixel.

`func contrast(Double) -> some VisualEffect`

Sets the contrast and separation between similar colors in the view.

`func grayscale(Double) -> some VisualEffect`

Adds a grayscale effect to the view.

`func saturation(Double) -> some VisualEffect`

Adjusts the color saturation of the view.

`func opacity(Double) -> some VisualEffect`

Sets the transparency of the view.

Instance Method

# saturation(_:)

Adjusts the color saturation of the view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func saturation(_ amount: Double) -> some VisualEffect
    

##  Parameters

`amount`

    

The amount of saturation to apply to the view.

## Return Value

An effect that adjusts the saturation of the view.

## Discussion

Use color saturation to increase or decrease the intensity of colors in a
view.

See Also

`contrast(_:)`

## See Also

### Adjusting Color

`func brightness(Double) -> some VisualEffect`

Brightens the view by the specified amount.

`func colorEffect(Shader, isEnabled: Bool) -> some VisualEffect`

Returns a new visual effect that applies `shader` to `self` as a filter effect
on the color of each pixel.

`func contrast(Double) -> some VisualEffect`

Sets the contrast and separation between similar colors in the view.

`func grayscale(Double) -> some VisualEffect`

Adds a grayscale effect to the view.

`func hueRotation(Angle) -> some VisualEffect`

Applies a hue rotation effect to the view.

`func opacity(Double) -> some VisualEffect`

Sets the transparency of the view.

Instance Method

# opacity(_:)

Sets the transparency of the view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func opacity(_ opacity: Double) -> some VisualEffect
    

##  Parameters

`opacity`

    

A value between 0 (fully transparent) and 1 (fully opaque).

## Return Value

An effect that sets the transparency of the view.

## Discussion

When applying the `opacity(_:)` effect to a view that has already had its
opacity transformed, the effect of the underlying opacity transformation is
multiplied.

## See Also

### Adjusting Color

`func brightness(Double) -> some VisualEffect`

Brightens the view by the specified amount.

`func colorEffect(Shader, isEnabled: Bool) -> some VisualEffect`

Returns a new visual effect that applies `shader` to `self` as a filter effect
on the color of each pixel.

`func contrast(Double) -> some VisualEffect`

Sets the contrast and separation between similar colors in the view.

`func grayscale(Double) -> some VisualEffect`

Adds a grayscale effect to the view.

`func hueRotation(Angle) -> some VisualEffect`

Applies a hue rotation effect to the view.

`func saturation(Double) -> some VisualEffect`

Adjusts the color saturation of the view.

Instance Method

# scaleEffect(_:anchor:)

Scales the view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func scaleEffect(
        _ scale: CGFloat,
        anchor: UnitPoint = .center
    ) -> some VisualEffect
    

##  Parameters

`s`

    

The amount to scale the view in the view in both the horizontal and vertical
directions.

`anchor`

    

The point with a default of `center` that defines the location within the view
from which to apply the transformation.

## Return Value

An effect that scales the view’s rendered output.

## See Also

### Scaling

`func scaleEffect(CGSize, anchor: UnitPoint) -> some VisualEffect`

Scales the view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some
VisualEffect`

Scales the view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> some VisualEffect`

Scales this view uniformly by the specified size in each dimension.

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> some VisualEffect`

Scales this view uniformly by the specified factor.

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
some VisualEffect`

Scales this view by the specified horizontal, vertical, and depth factors.

Instance Method

# scaleEffect(_:anchor:)

Scales the view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func scaleEffect(
        _ scale: CGSize,
        anchor: UnitPoint = .center
    ) -> some VisualEffect
    

##  Parameters

`scale`

    

A `CGSize` that represents the horizontal and vertical amount to scale the
view.

`anchor`

    

The point with a default of `center` that defines the location within the view
from which to apply the transformation.

## Return Value

An effect that scales the view’s rendered output.

## See Also

### Scaling

`func scaleEffect(CGFloat, anchor: UnitPoint) -> some VisualEffect`

Scales the view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some
VisualEffect`

Scales the view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> some VisualEffect`

Scales this view uniformly by the specified size in each dimension.

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> some VisualEffect`

Scales this view uniformly by the specified factor.

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
some VisualEffect`

Scales this view by the specified horizontal, vertical, and depth factors.

Instance Method

# scaleEffect(x:y:anchor:)

Scales the view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func scaleEffect(
        x: CGFloat = 1.0,
        y: CGFloat = 1.0,
        anchor: UnitPoint = .center
    ) -> some VisualEffect
    

##  Parameters

`x`

    

An amount that represents the horizontal amount to scale the view. The default
value is `1.0`.

`y`

    

An amount that represents the vertical amount to scale the view. The default
value is `1.0`.

`anchor`

    

The point with a default of `center` that defines the location within the view
from which to apply the transformation.

## Return Value

An effect that scales the view’s rendered output.

## See Also

### Scaling

`func scaleEffect(CGFloat, anchor: UnitPoint) -> some VisualEffect`

Scales the view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(CGSize, anchor: UnitPoint) -> some VisualEffect`

Scales the view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> some VisualEffect`

Scales this view uniformly by the specified size in each dimension.

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> some VisualEffect`

Scales this view uniformly by the specified factor.

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
some VisualEffect`

Scales this view by the specified horizontal, vertical, and depth factors.

Instance Method

# scaleEffect(_:anchor:)

Scales this view uniformly by the specified size in each dimension.

visionOS 1.0+

    
    
    func scaleEffect(
        _ scale: Size3D,
        anchor: UnitPoint3D = .center
    ) -> some VisualEffect
    

##  Parameters

`scale`

    

The scale factor for this view in each dimension.

`anchor`

    

The anchor point about which to scale the view. Defaults to center.

## Return Value

An effect that scales this view by `scale`.

## Discussion

The original dimensions of the view are considered to be unchanged by scaling
the contents. To change the dimensions of the view, use a modifier like
`frame()` instead.

## See Also

### Scaling

`func scaleEffect(CGFloat, anchor: UnitPoint) -> some VisualEffect`

Scales the view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(CGSize, anchor: UnitPoint) -> some VisualEffect`

Scales the view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some
VisualEffect`

Scales the view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> some VisualEffect`

Scales this view uniformly by the specified factor.

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
some VisualEffect`

Scales this view by the specified horizontal, vertical, and depth factors.

Instance Method

# scaleEffect(_:anchor:)

Scales this view uniformly by the specified factor.

visionOS 1.0+

    
    
    func scaleEffect(
        _ s: CGFloat,
        anchor: UnitPoint3D = .center
    ) -> some VisualEffect
    

##  Parameters

`s`

    

The scale factor for this view.

`anchor`

    

The anchor point about which to scale the view. Defaults to center.

## Return Value

An effect that scales this view by `s` in all dimensions.

## Discussion

The original dimensions of the view are considered to be unchanged by scaling
the contents. To change the dimensions of the view, use a modifier like
`frame()` instead.

## See Also

### Scaling

`func scaleEffect(CGFloat, anchor: UnitPoint) -> some VisualEffect`

Scales the view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(CGSize, anchor: UnitPoint) -> some VisualEffect`

Scales the view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some
VisualEffect`

Scales the view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> some VisualEffect`

Scales this view uniformly by the specified size in each dimension.

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
some VisualEffect`

Scales this view by the specified horizontal, vertical, and depth factors.

Instance Method

# scaleEffect(x:y:z:anchor:)

Scales this view by the specified horizontal, vertical, and depth factors.

visionOS 1.0+

    
    
    func scaleEffect(
        x: CGFloat = 1.0,
        y: CGFloat = 1.0,
        z: CGFloat = 1.0,
        anchor: UnitPoint3D = .center
    ) -> some VisualEffect
    

##  Parameters

`x`

    

The horizontal scale factor for this view.

`y`

    

The vertical scale factor for this view.

`z`

    

The depth scale factor for this view.

`anchor`

    

The anchor point about which to scale the view. Defaults to center.

## Return Value

An effect that scales this view by `x`,`y`, and `z`.

## Discussion

The original dimensions of the view are considered to be unchanged by scaling
the contents. To change the dimensions of the view, use a modifier like
`frame()` instead.

## See Also

### Scaling

`func scaleEffect(CGFloat, anchor: UnitPoint) -> some VisualEffect`

Scales the view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(CGSize, anchor: UnitPoint) -> some VisualEffect`

Scales the view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some
VisualEffect`

Scales the view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> some VisualEffect`

Scales this view uniformly by the specified size in each dimension.

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> some VisualEffect`

Scales this view uniformly by the specified factor.

Instance Method

# rotationEffect(_:anchor:)

Rotates content in two dimensions around the specified point.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func rotationEffect(
        _ angle: Angle,
        anchor: UnitPoint = .center
    ) -> some VisualEffect
    

##  Parameters

`angle`

    

The angle by which to rotate the content.

`anchor`

    

A unit point within the content about which to perform the rotation. The
default value is `center`.

## Return Value

A rotation effect.

## Discussion

This effect rotates the content around the axis that points out of the xy-
plane. It has no effect on the content’s frame. The following code rotates
text by 22˚ and then draws a border around the modified view to show that the
frame remains unchanged by the rotation:

## See Also

### Rotating

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some
VisualEffect`

Renders content as if it’s rotated in three dimensions around the specified
axis.

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint3D, perspective: CGFloat) -> some VisualEffect`

Renders content as if it’s rotated in three dimensions around the specified
axis.

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some VisualEffect`

Rotates content by the specified 3D rotation value.

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
some VisualEffect`

Rotates content by an angle about an axis that you specify as a rotation axis
value.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> some VisualEffect`

Rotates content by an angle about an axis that you specify as a tuple of
elements.

Instance Method

# rotation3DEffect(_:axis:anchor:anchorZ:perspective:)

Renders content as if it’s rotated in three dimensions around the specified
axis.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func rotation3DEffect(
        _ angle: Angle,
        axis: (x: CGFloat, y: CGFloat, z: CGFloat),
        anchor: UnitPoint = .center,
        anchorZ: CGFloat = 0,
        perspective: CGFloat = 1
    ) -> some VisualEffect
    

##  Parameters

`angle`

    

The angle by which to rotate the content.

`axis`

    

The axis of rotation, specified as a tuple with named elements for each of the
three spatial dimensions.

`anchor`

    

A two dimensional unit point within the content about which to perform the
rotation. The default value is `center`.

`anchorZ`

    

The location on the z-axis around which to rotate the content. The default is
`0`.

`perspective`

    

The relative vanishing point for the rotation. The default is `1`.

## Return Value

A rotation effect.

## Discussion

Use this method to create the effect of rotating a two dimensional view in
three dimensions around a specified axis of rotation. The effect projects the
rotated content onto the original content’s plane. Use the `perspective` input
to control the renderer’s vanishing point. The following example creates the
appearance of rotating text 45˚ about the y-axis:

Important

In visionOS, create this effect with
`perspectiveRotationEffect(_:axis:anchor:perspective:)` instead. To truly
rotate a view in three dimensions, use a 3D rotation effect without a
perspective input like `rotation3DEffect(_:axis:anchor:)`.

## See Also

### Rotating

`func rotationEffect(Angle, anchor: UnitPoint) -> some VisualEffect`

Rotates content in two dimensions around the specified point.

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint3D, perspective: CGFloat) -> some VisualEffect`

Renders content as if it’s rotated in three dimensions around the specified
axis.

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some VisualEffect`

Rotates content by the specified 3D rotation value.

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
some VisualEffect`

Rotates content by an angle about an axis that you specify as a rotation axis
value.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> some VisualEffect`

Rotates content by an angle about an axis that you specify as a tuple of
elements.

Instance Method

# perspectiveRotationEffect(_:axis:anchor:perspective:)

Renders content as if it’s rotated in three dimensions around the specified
axis.

visionOS 1.0+

    
    
    func perspectiveRotationEffect(
        _ angle: Angle,
        axis: (x: CGFloat, y: CGFloat, z: CGFloat),
        anchor: UnitPoint3D = .back,
        perspective: CGFloat = 1
    ) -> some VisualEffect
    

##  Parameters

`angle`

    

The angle by which to rotate the content.

`axis`

    

The axis of rotation, specified as a tuple with named elements for each of the
three spatial dimensions.

`anchor`

    

A unit point within the content about which to perform the rotation. The
default value is `center`.

`perspective`

    

The relative vanishing point for the rotation. The default is `1`.

## Return Value

A rotation effect.

## Discussion

Use this method to create the effect of rotating content in three dimensions
around a specified axis of rotation. The modifier projects two dimensional
content onto the original content’s plane. Use the `perspective` input to
control the renderer’s vanishing point. The following example creates the
appearance of rotating text 45˚ about the y-axis:

Important

To truly rotate content in three dimensions, use a 3D rotation effect without
a perspective input like `rotation3DEffect(_:axis:anchor:)`.

## See Also

### Rotating

`func rotationEffect(Angle, anchor: UnitPoint) -> some VisualEffect`

Rotates content in two dimensions around the specified point.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some
VisualEffect`

Renders content as if it’s rotated in three dimensions around the specified
axis.

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some VisualEffect`

Rotates content by the specified 3D rotation value.

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
some VisualEffect`

Rotates content by an angle about an axis that you specify as a rotation axis
value.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> some VisualEffect`

Rotates content by an angle about an axis that you specify as a tuple of
elements.

Instance Method

# rotation3DEffect(_:anchor:)

Rotates content by the specified 3D rotation value.

visionOS 1.0+

    
    
    func rotation3DEffect(
        _ rotation: Rotation3D,
        anchor: UnitPoint3D = .center
    ) -> some VisualEffect
    

##  Parameters

`rotation`

    

A rotation to apply to the content.

`anchor`

    

The unit point within the content about which to perform the rotation. The
default value is `center`.

## Return Value

A rotation effect.

## Discussion

This effect causes the content to appear rotated, but doesn’t change the
content’s frame. The following code applies a rotation of 45° about the
y-axis, using the default anchor point at the center of the content:

## See Also

### Rotating

`func rotationEffect(Angle, anchor: UnitPoint) -> some VisualEffect`

Rotates content in two dimensions around the specified point.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some
VisualEffect`

Renders content as if it’s rotated in three dimensions around the specified
axis.

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint3D, perspective: CGFloat) -> some VisualEffect`

Renders content as if it’s rotated in three dimensions around the specified
axis.

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
some VisualEffect`

Rotates content by an angle about an axis that you specify as a rotation axis
value.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> some VisualEffect`

Rotates content by an angle about an axis that you specify as a tuple of
elements.

Instance Method

# rotation3DEffect(_:axis:anchor:)

Rotates content by an angle about an axis that you specify as a rotation axis
value.

visionOS 1.0+

    
    
    func rotation3DEffect(
        _ angle: Angle,
        axis: RotationAxis3D,
        anchor: UnitPoint3D = .center
    ) -> some VisualEffect
    

##  Parameters

`angle`

    

The angle by which to rotate the view’s content.

`axis`

    

The axis of rotation.

`anchor`

    

The unit point within the content about which to perform the rotation. The
default value is `center`.

## Return Value

A rotation effect.

## Discussion

This effect causes the content to appear rotated, but doesn’t change the
content’s frame. The following code applies a rotation of 45° about the
y-axis, using the default anchor point at the center of the content:

## See Also

### Rotating

`func rotationEffect(Angle, anchor: UnitPoint) -> some VisualEffect`

Rotates content in two dimensions around the specified point.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some
VisualEffect`

Renders content as if it’s rotated in three dimensions around the specified
axis.

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint3D, perspective: CGFloat) -> some VisualEffect`

Renders content as if it’s rotated in three dimensions around the specified
axis.

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some VisualEffect`

Rotates content by the specified 3D rotation value.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> some VisualEffect`

Rotates content by an angle about an axis that you specify as a tuple of
elements.

Instance Method

# rotation3DEffect(_:axis:anchor:)

Rotates content by an angle about an axis that you specify as a tuple of
elements.

visionOS 1.0+

    
    
    func rotation3DEffect(
        _ angle: Angle,
        axis: (x: CGFloat, y: CGFloat, z: CGFloat),
        anchor: UnitPoint3D = .center
    ) -> some VisualEffect
    

##  Parameters

`angle`

    

The angle by which to rotate the content.

`axis`

    

The axis of rotation, specified as a tuple with named elements for each of the
three spatial dimensions.

`anchor`

    

The unit point within the content about which to perform the rotation. The
default value is `center`.

## Return Value

A rotation effect.

## Discussion

This effect causes the content to appear rotated, but doesn’t change the
content’s frame. The following code applies a rotation of 45° about the
y-axis, using the default anchor point at the center of the content:

## See Also

### Rotating

`func rotationEffect(Angle, anchor: UnitPoint) -> some VisualEffect`

Rotates content in two dimensions around the specified point.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some
VisualEffect`

Renders content as if it’s rotated in three dimensions around the specified
axis.

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint3D, perspective: CGFloat) -> some VisualEffect`

Renders content as if it’s rotated in three dimensions around the specified
axis.

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some VisualEffect`

Rotates content by the specified 3D rotation value.

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
some VisualEffect`

Rotates content by an angle about an axis that you specify as a rotation axis
value.

Instance Method

# offset(_:)

Offsets the view by the horizontal and vertical amount specified in the offset
parameter.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func offset(_ offset: CGSize) -> some VisualEffect
    

##  Parameters

`offset`

    

The distance to offset the view.

## Return Value

An effect that offsets the view by `offset`.

## See Also

### Translating

`func offset(x: CGFloat, y: CGFloat) -> some VisualEffect`

Offsets the view by the specified horizontal and vertical distances.

`func offset(z: CGFloat) -> some VisualEffect`

Brings a view forward in Z by the provided distance in points.

Instance Method

# offset(x:y:)

Offsets the view by the specified horizontal and vertical distances.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func offset(
        x: CGFloat = 0,
        y: CGFloat = 0
    ) -> some VisualEffect
    

##  Parameters

`x`

    

The horizontal distance to offset the view.

`y`

    

The vertical distance to offset the view.

## Return Value

An effect that offsets the view by `x` and `y`.

## See Also

### Translating

`func offset(CGSize) -> some VisualEffect`

Offsets the view by the horizontal and vertical amount specified in the offset
parameter.

`func offset(z: CGFloat) -> some VisualEffect`

Brings a view forward in Z by the provided distance in points.

Instance Method

# offset(z:)

Brings a view forward in Z by the provided distance in points.

visionOS 1.0+

    
    
    func offset(z: CGFloat) -> some VisualEffect
    

##  Parameters

`distance`

    

The distance to extrude the view forward in Z, in points.

## Return Value

An effect that is extruded forward in Z by `distance`.

## See Also

### Translating

`func offset(CGSize) -> some VisualEffect`

Offsets the view by the horizontal and vertical amount specified in the offset
parameter.

`func offset(x: CGFloat, y: CGFloat) -> some VisualEffect`

Offsets the view by the specified horizontal and vertical distances.

Instance Method

# transform3DEffect(_:)

Applies a 3D transformation to the receiver.

visionOS 1.0+

    
    
    func transform3DEffect(_ transform: AffineTransform3D) -> some VisualEffect
    

##  Parameters

`transform`

    

The 3D transformation to apply to the view, interpreting it as a 3D plane in
space.

## Return Value

An effect that renders transformed according to the provided `transform`

## See Also

### Applying a transform

`func transformEffect(CGAffineTransform) -> some VisualEffect`

Applies an affine transformation to the view’s rendered output.

`func transformEffect(ProjectionTransform) -> some VisualEffect`

Applies a projection transformation to the view’s rendered output.

Instance Method

# transformEffect(_:)

Applies an affine transformation to the view’s rendered output.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func transformEffect(_ transform: CGAffineTransform) -> some VisualEffect
    

##  Parameters

`transform`

    

A `CGAffineTransform` to apply to the view.

## Return Value

An effect that applies an affine transformation to the view’s rendered output.

## Discussion

Use `transformEffect(_:)` to rotate, scale, translate, or skew the output of
the view according to the provided `CGAffineTransform`.

## See Also

### Applying a transform

`func transform3DEffect(AffineTransform3D) -> some VisualEffect`

Applies a 3D transformation to the receiver.

`func transformEffect(ProjectionTransform) -> some VisualEffect`

Applies a projection transformation to the view’s rendered output.

Instance Method

# transformEffect(_:)

Applies a projection transformation to the view’s rendered output.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func transformEffect(_ transform: ProjectionTransform) -> some VisualEffect
    

##  Parameters

`transform`

    

A `ProjectionTransform` to apply to the view.

## Return Value

An effect that applies a projection transformation to the view’s rendered
output.

## Discussion

Use `transformEffect(_:)` to rotate, scale, translate, or skew the output of
the view according to the provided `ProjectionTransform`.

## See Also

### Applying a transform

`func transform3DEffect(AffineTransform3D) -> some VisualEffect`

Applies a 3D transformation to the receiver.

`func transformEffect(CGAffineTransform) -> some VisualEffect`

Applies an affine transformation to the view’s rendered output.

Instance Method

# blur(radius:opaque:)

Applies a Gaussian blur to the view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func blur(
        radius: CGFloat,
        opaque: Bool = false
    ) -> some VisualEffect
    

##  Parameters

`radius`

    

The radial size of the blur. A blur is more diffuse when its radius is large.

`opaque`

    

A Boolean value that indicates whether the blur renderer permits transparency
in the blur output. Set to `true` to create an opaque blur, or set to `false`
to permit transparency.

## Return Value

An effect that blurs the view.

## Discussion

Use `blur(radius:opaque:)` to apply a gaussian blur effect to the rendering of
the view.

## See Also

### Applying other effects

`func distortionEffect(Shader, maxSampleOffset: CGSize, isEnabled: Bool) ->
some VisualEffect`

Returns a new visual effect that applies `shader` to `self` as a geometric
distortion effect on the location of each pixel.

`func layerEffect(Shader, maxSampleOffset: CGSize, isEnabled: Bool) -> some
VisualEffect`

Returns a new visual effect that applies `shader` to `self` as a filter on the
raster layer created from `self`.

Instance Method

# distortionEffect(_:maxSampleOffset:isEnabled:)

Returns a new visual effect that applies `shader` to `self` as a geometric
distortion effect on the location of each pixel.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    func distortionEffect(
        _ shader: Shader,
        maxSampleOffset: CGSize,
        isEnabled: Bool = true
    ) -> some VisualEffect
    

##  Parameters

`shader`

    

The shader to apply as a distortion effect.

`maxSampleOffset`

    

The maximum distance in each axis between the returned source pixel position
and the destination pixel position, for all source pixels.

`isEnabled`

    

Whether the effect is enabled or not.

## Return Value

A new view that renders `self` with the shader applied as a distortion effect.

## Discussion

For a shader function to act as a distortion effect it must have a function
signature matching:

where `position` is the user-space coordinates of the destination pixel
applied to the shader. `args...` should be compatible with the uniform
arguments bound to `shader`. The function should return the user-space
coordinates of the corresponding source pixel.

Important

Views backed by AppKit or UIKit views may not render into the filtered layer.
Instead, they log a warning and display a placeholder image to highlight the
error.

## See Also

### Applying other effects

`func blur(radius: CGFloat, opaque: Bool) -> some VisualEffect`

Applies a Gaussian blur to the view.

`func layerEffect(Shader, maxSampleOffset: CGSize, isEnabled: Bool) -> some
VisualEffect`

Returns a new visual effect that applies `shader` to `self` as a filter on the
raster layer created from `self`.

Instance Method

# layerEffect(_:maxSampleOffset:isEnabled:)

Returns a new visual effect that applies `shader` to `self` as a filter on the
raster layer created from `self`.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    func layerEffect(
        _ shader: Shader,
        maxSampleOffset: CGSize,
        isEnabled: Bool = true
    ) -> some VisualEffect
    

##  Parameters

`shader`

    

The shader to apply as a layer effect.

`maxSampleOffset`

    

If the shader function samples from the layer at locations not equal to the
destination position, this value must specify the maximum sampling distance in
each axis, for all source pixels.

`isEnabled`

    

Whether the effect is enabled or not.

## Return Value

A new view that renders `self` with the shader applied as a distortion effect.

## Discussion

For a shader function to act as a layer effect it must have a function
signature matching:

where `position` is the user-space coordinates of the destination pixel
applied to the shader, and `layer` is a subregion of the rasterized contents
of `self`. `args...` should be compatible with the uniform arguments bound to
`shader`.

The `SwiftUI::Layer` type is defined in the `<SwiftUI/SwiftUI.h>` header file.
It exports a single `sample()` function that returns a linearly-filtered pixel
value from a position in the source content, as a premultiplied RGBA pixel
value:

The function should return the color mapping to the destination pixel,
typically by sampling one or more pixels from `layer` at location(s) derived
from `position` and them applying some kind of transformation to produce a new
color.

Important

Views backed by AppKit or UIKit views may not render into the filtered layer.
Instead, they log a warning and display a placeholder image to highlight the
error.

## See Also

### Applying other effects

`func blur(radius: CGFloat, opaque: Bool) -> some VisualEffect`

Applies a Gaussian blur to the view.

`func distortionEffect(Shader, maxSampleOffset: CGSize, isEnabled: Bool) ->
some VisualEffect`

Returns a new visual effect that applies `shader` to `self` as a geometric
distortion effect on the location of each pixel.

