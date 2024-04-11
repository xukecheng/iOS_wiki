Instance Method

# mask(alignment:_:)

Masks this view using the alpha channel of the given view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func mask<Mask>(
        alignment: Alignment = .center,
        @ViewBuilder _ mask: () -> Mask
    ) -> some View where Mask : View
    

##  Parameters

`alignment`

    

The alignment for `mask` in relation to this view.

`mask`

    

The view whose alpha the rendering system applies to the specified view.

## Discussion

Use `mask(_:)` when you want to apply the alpha (opacity) value of another
view to the current view.

This example shows an image masked by rectangle with a 10% opacity:

## See Also

### Masking and clipping

`func clipped(antialiased: Bool) -> some View`

Clips this view to its bounding rectangular frame.

`func clipShape<S>(S, style: FillStyle) -> some View`

Sets a clipping shape for this view.

Instance Method

# clipped(antialiased:)

Clips this view to its bounding rectangular frame.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func clipped(antialiased: Bool = false) -> some View
    

##  Parameters

`antialiased`

    

A Boolean value that indicates whether the rendering system applies smoothing
to the edges of the clipping rectangle.

## Return Value

A view that clips this view to its bounding frame.

## Discussion

Use the `clipped(antialiased:)` modifier to hide any content that extends
beyond the layout bounds of the shape.

By default, a view’s bounding frame is used only for layout, so any content
that extends beyond the edges of the frame is still visible.

## See Also

### Masking and clipping

`func mask<Mask>(alignment: Alignment, () -> Mask) -> some View`

Masks this view using the alpha channel of the given view.

`func clipShape<S>(S, style: FillStyle) -> some View`

Sets a clipping shape for this view.

Instance Method

# clipShape(_:style:)

Sets a clipping shape for this view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func clipShape<S>(
        _ shape: S,
        style: FillStyle = FillStyle()
    ) -> some View where S : Shape
    

##  Parameters

`shape`

    

The clipping shape to use for this view. The `shape` fills the view’s frame,
while maintaining its aspect ratio.

`style`

    

The fill style to use when rasterizing `shape`.

## Return Value

A view that clips this view to `shape`, using `style` to define the shape’s
rasterization.

## Discussion

Use `clipShape(_:style:)` to clip the view to the provided shape. By applying
a clipping shape to a view, you preserve the parts of the view covered by the
shape, while eliminating other parts of the view. The clipping shape itself
isn’t visible.

For example, this code applies a circular clipping shape to a `Text` view:

The resulting view shows only the portion of the text that lies within the
bounds of the circle.

## See Also

### Masking and clipping

`func mask<Mask>(alignment: Alignment, () -> Mask) -> some View`

Masks this view using the alpha channel of the given view.

`func clipped(antialiased: Bool) -> some View`

Clips this view to its bounding rectangular frame.

Instance Method

# containerShape(_:)

Sets the container shape to use for any container relative shape within this
view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func containerShape<T>(_ shape: T) -> some View where T : InsettableShape
    

## Discussion

The example below defines a view that shows its content with a rounded
rectangle background and the same container shape. Any
`ContainerRelativeShape` within the `content` matches the rounded rectangle
shape from this container inset as appropriate.

## See Also

### Setting a container shape

`protocol InsettableShape`

A shape type that is able to inset itself to produce another shape.

`struct ContainerRelativeShape`

A shape that is replaced by an inset version of the current container shape.
If no container shape was defined, is replaced by a rectangle.

Instance Method

# scaledToFill()

Scales this view to fill its parent.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func scaledToFill() -> some View
    

## Return Value

A view that scales this view to fill its parent, maintaining this view’s
aspect ratio.

## Discussion

Use `scaledToFill()` to scale this view to fill its parent, while maintaining
the view’s aspect ratio as the view scales:

This method is equivalent to calling `aspectRatio(_:contentMode:)` with a
`nil` aspectRatio and a content mode of `ContentMode.fill`.

## See Also

### Scaling, rotating, or transforming a view

`func scaledToFit() -> some View`

Scales this view to fit its parent.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(CGSize, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified factor.

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified size in each dimension.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> ModifiedContent<Self,
_UniformScaleEffect>`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
some View`

Scales this view by the specified horizontal, vertical, and depth factors.

`func aspectRatio(CGFloat?, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the specified aspect ratio.

`func aspectRatio(CGSize, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the aspect ratio of the given size.

`func rotationEffect(Angle, anchor: UnitPoint) -> some View`

Rotates a view’s rendered output in two dimensions around the specified point.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some
View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some View`

Rotates the view’s content by the specified 3D rotation value.

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
some View`

Rotates the view’s content by an angle about an axis that you specify as a
rotation axis value.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> some View`

Rotates the view’s content by an angle about an axis that you specify as a
tuple of elements.

`func transformEffect(CGAffineTransform) -> some View`

Applies an affine transformation to this view’s rendered output.

`func transform3DEffect(AffineTransform3D) -> some View`

Applies a 3D transformation to the receiver.

`func projectionEffect(ProjectionTransform) -> some View`

Applies a projection transformation to this view’s rendered output.

`struct ProjectionTransform`

`enum ContentMode`

Constants that define how a view’s content fills the available space.

Instance Method

# scaledToFit()

Scales this view to fit its parent.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func scaledToFit() -> some View
    

## Return Value

A view that scales this view to fit its parent, maintaining this view’s aspect
ratio.

## Discussion

Use `scaledToFit()` to scale this view to fit its parent, while maintaining
the view’s aspect ratio as the view scales.

This method is equivalent to calling `aspectRatio(_:contentMode:)` with a
`nil` aspectRatio and a content mode of `ContentMode.fit`.

## See Also

### Scaling, rotating, or transforming a view

`func scaledToFill() -> some View`

Scales this view to fill its parent.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(CGSize, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified factor.

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified size in each dimension.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> ModifiedContent<Self,
_UniformScaleEffect>`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
some View`

Scales this view by the specified horizontal, vertical, and depth factors.

`func aspectRatio(CGFloat?, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the specified aspect ratio.

`func aspectRatio(CGSize, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the aspect ratio of the given size.

`func rotationEffect(Angle, anchor: UnitPoint) -> some View`

Rotates a view’s rendered output in two dimensions around the specified point.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some
View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some View`

Rotates the view’s content by the specified 3D rotation value.

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
some View`

Rotates the view’s content by an angle about an axis that you specify as a
rotation axis value.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> some View`

Rotates the view’s content by an angle about an axis that you specify as a
tuple of elements.

`func transformEffect(CGAffineTransform) -> some View`

Applies an affine transformation to this view’s rendered output.

`func transform3DEffect(AffineTransform3D) -> some View`

Applies a 3D transformation to the receiver.

`func projectionEffect(ProjectionTransform) -> some View`

Applies a projection transformation to this view’s rendered output.

`struct ProjectionTransform`

`enum ContentMode`

Constants that define how a view’s content fills the available space.

Instance Method

# scaleEffect(_:anchor:)

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func scaleEffect(
        _ s: CGFloat,
        anchor: UnitPoint = .center
    ) -> some View
    

##  Parameters

`s`

    

The amount to scale the view in the view in both the horizontal and vertical
directions.

`anchor`

    

The anchor point with a default of `center` that indicates the starting
position for the scale operation.

## Discussion

Use `scaleEffect(_:anchor:)` to apply a horizontally and vertically scaling
transform to a view.

## See Also

### Scaling, rotating, or transforming a view

`func scaledToFill() -> some View`

Scales this view to fill its parent.

`func scaledToFit() -> some View`

Scales this view to fit its parent.

`func scaleEffect(CGSize, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified factor.

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified size in each dimension.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> ModifiedContent<Self,
_UniformScaleEffect>`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
some View`

Scales this view by the specified horizontal, vertical, and depth factors.

`func aspectRatio(CGFloat?, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the specified aspect ratio.

`func aspectRatio(CGSize, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the aspect ratio of the given size.

`func rotationEffect(Angle, anchor: UnitPoint) -> some View`

Rotates a view’s rendered output in two dimensions around the specified point.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some
View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some View`

Rotates the view’s content by the specified 3D rotation value.

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
some View`

Rotates the view’s content by an angle about an axis that you specify as a
rotation axis value.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> some View`

Rotates the view’s content by an angle about an axis that you specify as a
tuple of elements.

`func transformEffect(CGAffineTransform) -> some View`

Applies an affine transformation to this view’s rendered output.

`func transform3DEffect(AffineTransform3D) -> some View`

Applies a 3D transformation to the receiver.

`func projectionEffect(ProjectionTransform) -> some View`

Applies a projection transformation to this view’s rendered output.

`struct ProjectionTransform`

`enum ContentMode`

Constants that define how a view’s content fills the available space.

Instance Method

# scaleEffect(_:anchor:)

Scales this view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func scaleEffect(
        _ scale: CGSize,
        anchor: UnitPoint = .center
    ) -> some View
    

##  Parameters

`scale`

    

A `CGSize` that represents the horizontal and vertical amount to scale the
view.

`anchor`

    

The point with a default of `center` that defines the location within the view
from which to apply the transformation.

## Discussion

Use `scaleEffect(_:anchor:)` to scale a view by applying a scaling transform
of a specific size, specified by `scale`.

## See Also

### Scaling, rotating, or transforming a view

`func scaledToFill() -> some View`

Scales this view to fill its parent.

`func scaledToFit() -> some View`

Scales this view to fit its parent.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified factor.

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified size in each dimension.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> ModifiedContent<Self,
_UniformScaleEffect>`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
some View`

Scales this view by the specified horizontal, vertical, and depth factors.

`func aspectRatio(CGFloat?, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the specified aspect ratio.

`func aspectRatio(CGSize, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the aspect ratio of the given size.

`func rotationEffect(Angle, anchor: UnitPoint) -> some View`

Rotates a view’s rendered output in two dimensions around the specified point.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some
View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some View`

Rotates the view’s content by the specified 3D rotation value.

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
some View`

Rotates the view’s content by an angle about an axis that you specify as a
rotation axis value.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> some View`

Rotates the view’s content by an angle about an axis that you specify as a
tuple of elements.

`func transformEffect(CGAffineTransform) -> some View`

Applies an affine transformation to this view’s rendered output.

`func transform3DEffect(AffineTransform3D) -> some View`

Applies a 3D transformation to the receiver.

`func projectionEffect(ProjectionTransform) -> some View`

Applies a projection transformation to this view’s rendered output.

`struct ProjectionTransform`

`enum ContentMode`

Constants that define how a view’s content fills the available space.

Instance Method

# scaleEffect(_:anchor:)

Scales this view uniformly by the specified factor.

visionOS 1.0+

    
    
    func scaleEffect(
        _ s: CGFloat,
        anchor: UnitPoint3D = .center
    ) -> some View
    

##  Parameters

`s`

    

The scale factor for this view.

`anchor`

    

The anchor point about which to scale the view. Defaults to center.

## Return Value

A view that scales this view by `s` in all dimensions.

## Discussion

The original dimensions of the view are considered to be unchanged by scaling
the contents. To change the dimensions of the view, use a modifier like
`frame()` instead.

## See Also

### Scaling, rotating, or transforming a view

`func scaledToFill() -> some View`

Scales this view to fill its parent.

`func scaledToFit() -> some View`

Scales this view to fit its parent.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(CGSize, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified size in each dimension.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> ModifiedContent<Self,
_UniformScaleEffect>`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
some View`

Scales this view by the specified horizontal, vertical, and depth factors.

`func aspectRatio(CGFloat?, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the specified aspect ratio.

`func aspectRatio(CGSize, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the aspect ratio of the given size.

`func rotationEffect(Angle, anchor: UnitPoint) -> some View`

Rotates a view’s rendered output in two dimensions around the specified point.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some
View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some View`

Rotates the view’s content by the specified 3D rotation value.

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
some View`

Rotates the view’s content by an angle about an axis that you specify as a
rotation axis value.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> some View`

Rotates the view’s content by an angle about an axis that you specify as a
tuple of elements.

`func transformEffect(CGAffineTransform) -> some View`

Applies an affine transformation to this view’s rendered output.

`func transform3DEffect(AffineTransform3D) -> some View`

Applies a 3D transformation to the receiver.

`func projectionEffect(ProjectionTransform) -> some View`

Applies a projection transformation to this view’s rendered output.

`struct ProjectionTransform`

`enum ContentMode`

Constants that define how a view’s content fills the available space.

Instance Method

# scaleEffect(_:anchor:)

Scales this view uniformly by the specified size in each dimension.

visionOS 1.0+

    
    
    func scaleEffect(
        _ scale: Size3D,
        anchor: UnitPoint3D = .center
    ) -> some View
    

##  Parameters

`scale`

    

The scale factor for this view in each dimension.

`anchor`

    

The anchor point about which to scale the view. Defaults to center.

## Return Value

A view that scales this view by `scale`.

## Discussion

The original dimensions of the view are considered to be unchanged by scaling
the contents. To change the dimensions of the view, use a modifier like
`frame()` instead.

## See Also

### Scaling, rotating, or transforming a view

`func scaledToFill() -> some View`

Scales this view to fill its parent.

`func scaledToFit() -> some View`

Scales this view to fit its parent.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(CGSize, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified factor.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> ModifiedContent<Self,
_UniformScaleEffect>`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
some View`

Scales this view by the specified horizontal, vertical, and depth factors.

`func aspectRatio(CGFloat?, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the specified aspect ratio.

`func aspectRatio(CGSize, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the aspect ratio of the given size.

`func rotationEffect(Angle, anchor: UnitPoint) -> some View`

Rotates a view’s rendered output in two dimensions around the specified point.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some
View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some View`

Rotates the view’s content by the specified 3D rotation value.

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
some View`

Rotates the view’s content by an angle about an axis that you specify as a
rotation axis value.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> some View`

Rotates the view’s content by an angle about an axis that you specify as a
tuple of elements.

`func transformEffect(CGAffineTransform) -> some View`

Applies an affine transformation to this view’s rendered output.

`func transform3DEffect(AffineTransform3D) -> some View`

Applies a 3D transformation to the receiver.

`func projectionEffect(ProjectionTransform) -> some View`

Applies a projection transformation to this view’s rendered output.

`struct ProjectionTransform`

`enum ContentMode`

Constants that define how a view’s content fills the available space.

Instance Method

# scaleEffect(_:anchor:)

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func scaleEffect(
        _ s: CGFloat,
        anchor: UnitPoint = .center
    ) -> ModifiedContent<Self, _UniformScaleEffect>

##  Parameters

`s`

    

The amount to scale the view in the view in both the horizontal and vertical
directions.

`anchor`

    

The anchor point with a default of `center` that indicates the starting
position for the scale operation.

## Discussion

Use `scaleEffect(_:anchor:)` to apply a horizontally and vertically scaling
transform to a view.

## See Also

### Scaling, rotating, or transforming a view

`func scaledToFill() -> some View`

Scales this view to fill its parent.

`func scaledToFit() -> some View`

Scales this view to fit its parent.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(CGSize, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified factor.

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified size in each dimension.

`func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
some View`

Scales this view by the specified horizontal, vertical, and depth factors.

`func aspectRatio(CGFloat?, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the specified aspect ratio.

`func aspectRatio(CGSize, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the aspect ratio of the given size.

`func rotationEffect(Angle, anchor: UnitPoint) -> some View`

Rotates a view’s rendered output in two dimensions around the specified point.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some
View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some View`

Rotates the view’s content by the specified 3D rotation value.

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
some View`

Rotates the view’s content by an angle about an axis that you specify as a
rotation axis value.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> some View`

Rotates the view’s content by an angle about an axis that you specify as a
tuple of elements.

`func transformEffect(CGAffineTransform) -> some View`

Applies an affine transformation to this view’s rendered output.

`func transform3DEffect(AffineTransform3D) -> some View`

Applies a 3D transformation to the receiver.

`func projectionEffect(ProjectionTransform) -> some View`

Applies a projection transformation to this view’s rendered output.

`struct ProjectionTransform`

`enum ContentMode`

Constants that define how a view’s content fills the available space.

Instance Method

# scaleEffect(x:y:anchor:)

Scales this view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func scaleEffect(
        x: CGFloat = 1.0,
        y: CGFloat = 1.0,
        anchor: UnitPoint = .center
    ) -> some View
    

##  Parameters

`x`

    

An amount that represents the horizontal amount to scale the view. The default
value is `1.0`.

`y`

    

An amount that represents the vertical amount to scale the view. The default
value is `1.0`.

`anchor`

    

The anchor point that indicates the starting position for the scale operation.

## Discussion

Use `scaleEffect(x:y:anchor:)` to apply a scaling transform to a view by a
specific horizontal and vertical amount.

## See Also

### Scaling, rotating, or transforming a view

`func scaledToFill() -> some View`

Scales this view to fill its parent.

`func scaledToFit() -> some View`

Scales this view to fit its parent.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(CGSize, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified factor.

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified size in each dimension.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> ModifiedContent<Self,
_UniformScaleEffect>`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
some View`

Scales this view by the specified horizontal, vertical, and depth factors.

`func aspectRatio(CGFloat?, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the specified aspect ratio.

`func aspectRatio(CGSize, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the aspect ratio of the given size.

`func rotationEffect(Angle, anchor: UnitPoint) -> some View`

Rotates a view’s rendered output in two dimensions around the specified point.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some
View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some View`

Rotates the view’s content by the specified 3D rotation value.

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
some View`

Rotates the view’s content by an angle about an axis that you specify as a
rotation axis value.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> some View`

Rotates the view’s content by an angle about an axis that you specify as a
tuple of elements.

`func transformEffect(CGAffineTransform) -> some View`

Applies an affine transformation to this view’s rendered output.

`func transform3DEffect(AffineTransform3D) -> some View`

Applies a 3D transformation to the receiver.

`func projectionEffect(ProjectionTransform) -> some View`

Applies a projection transformation to this view’s rendered output.

`struct ProjectionTransform`

`enum ContentMode`

Constants that define how a view’s content fills the available space.

Instance Method

# scaleEffect(x:y:z:anchor:)

Scales this view by the specified horizontal, vertical, and depth factors.

visionOS 1.0+

    
    
    func scaleEffect(
        x: CGFloat = 1.0,
        y: CGFloat = 1.0,
        z: CGFloat = 1.0,
        anchor: UnitPoint3D = .center
    ) -> some View
    

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

A view that scales this view by `x`,`y`, and `z`.

## Discussion

The original dimensions of the view are considered to be unchanged by scaling
the contents. To change the dimensions of the view, use a modifier like
`frame()` instead.

## See Also

### Scaling, rotating, or transforming a view

`func scaledToFill() -> some View`

Scales this view to fill its parent.

`func scaledToFit() -> some View`

Scales this view to fit its parent.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(CGSize, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified factor.

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified size in each dimension.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> ModifiedContent<Self,
_UniformScaleEffect>`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

`func aspectRatio(CGFloat?, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the specified aspect ratio.

`func aspectRatio(CGSize, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the aspect ratio of the given size.

`func rotationEffect(Angle, anchor: UnitPoint) -> some View`

Rotates a view’s rendered output in two dimensions around the specified point.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some
View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some View`

Rotates the view’s content by the specified 3D rotation value.

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
some View`

Rotates the view’s content by an angle about an axis that you specify as a
rotation axis value.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> some View`

Rotates the view’s content by an angle about an axis that you specify as a
tuple of elements.

`func transformEffect(CGAffineTransform) -> some View`

Applies an affine transformation to this view’s rendered output.

`func transform3DEffect(AffineTransform3D) -> some View`

Applies a 3D transformation to the receiver.

`func projectionEffect(ProjectionTransform) -> some View`

Applies a projection transformation to this view’s rendered output.

`struct ProjectionTransform`

`enum ContentMode`

Constants that define how a view’s content fills the available space.

Instance Method

# imageScale(_:)

Scales images within the view according to one of the relative sizes available
including small, medium, and large images sizes.

iOS 13.0+  iPadOS 13.0+  macOS 11.0+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func imageScale(_ scale: Image.Scale) -> some View
    

##  Parameters

`scale`

    

One of the relative sizes provided by the image scale enumeration.

## Discussion

The example below shows the relative scaling effect. The system renders the
image at a relative size based on the available space and configuration
options of the image it is scaling.

## See Also

### Configuring an image

Fitting images into available space

Adjust the size and shape of images in your app’s user interface by applying
view modifiers.

`var imageScale: Image.Scale`

The image scale for this environment.

`enum Scale`

A scale to apply to vector images relative to text.

`enum Orientation`

The orientation of an image.

`enum ResizingMode`

The modes that SwiftUI uses to resize an image to fit within its containing
view.

Instance Method

# aspectRatio(_:contentMode:)

Constrains this view’s dimensions to the specified aspect ratio.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func aspectRatio(
        _ aspectRatio: CGFloat? = nil,
        contentMode: ContentMode
    ) -> some View
    

##  Parameters

`aspectRatio`

    

The ratio of width to height to use for the resulting view. Use `nil` to
maintain the current aspect ratio in the resulting view.

`contentMode`

    

A flag that indicates whether this view fits or fills the parent context.

## Return Value

A view that constrains this view’s dimensions to the aspect ratio of the given
size using `contentMode` as its scaling algorithm.

## Discussion

Use `aspectRatio(_:contentMode:)` to constrain a view’s dimensions to an
aspect ratio specified by a `CGFloat` using the specified content mode.

If this view is resizable, the resulting view will have `aspectRatio` as its
aspect ratio. In this example, the purple ellipse has a 3:4 width-to-height
ratio, and scales to fit its frame:

## See Also

### Scaling, rotating, or transforming a view

`func scaledToFill() -> some View`

Scales this view to fill its parent.

`func scaledToFit() -> some View`

Scales this view to fit its parent.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(CGSize, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified factor.

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified size in each dimension.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> ModifiedContent<Self,
_UniformScaleEffect>`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
some View`

Scales this view by the specified horizontal, vertical, and depth factors.

`func aspectRatio(CGSize, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the aspect ratio of the given size.

`func rotationEffect(Angle, anchor: UnitPoint) -> some View`

Rotates a view’s rendered output in two dimensions around the specified point.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some
View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some View`

Rotates the view’s content by the specified 3D rotation value.

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
some View`

Rotates the view’s content by an angle about an axis that you specify as a
rotation axis value.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> some View`

Rotates the view’s content by an angle about an axis that you specify as a
tuple of elements.

`func transformEffect(CGAffineTransform) -> some View`

Applies an affine transformation to this view’s rendered output.

`func transform3DEffect(AffineTransform3D) -> some View`

Applies a 3D transformation to the receiver.

`func projectionEffect(ProjectionTransform) -> some View`

Applies a projection transformation to this view’s rendered output.

`struct ProjectionTransform`

`enum ContentMode`

Constants that define how a view’s content fills the available space.

Instance Method

# aspectRatio(_:contentMode:)

Constrains this view’s dimensions to the aspect ratio of the given size.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func aspectRatio(
        _ aspectRatio: CGSize,
        contentMode: ContentMode
    ) -> some View
    

##  Parameters

`aspectRatio`

    

A size that specifies the ratio of width to height to use for the resulting
view.

`contentMode`

    

A flag indicating whether this view should fit or fill the parent context.

## Return Value

A view that constrains this view’s dimensions to `aspectRatio`, using
`contentMode` as its scaling algorithm.

## Discussion

Use `aspectRatio(_:contentMode:)` to constrain a view’s dimensions to an
aspect ratio specified by a `CGSize`.

If this view is resizable, the resulting view uses `aspectRatio` as its own
aspect ratio. In this example, the purple ellipse has a 3:4 width-to-height
ratio, and scales to fill its frame:

## See Also

### Scaling, rotating, or transforming a view

`func scaledToFill() -> some View`

Scales this view to fill its parent.

`func scaledToFit() -> some View`

Scales this view to fit its parent.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(CGSize, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified factor.

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified size in each dimension.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> ModifiedContent<Self,
_UniformScaleEffect>`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
some View`

Scales this view by the specified horizontal, vertical, and depth factors.

`func aspectRatio(CGFloat?, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the specified aspect ratio.

`func rotationEffect(Angle, anchor: UnitPoint) -> some View`

Rotates a view’s rendered output in two dimensions around the specified point.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some
View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some View`

Rotates the view’s content by the specified 3D rotation value.

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
some View`

Rotates the view’s content by an angle about an axis that you specify as a
rotation axis value.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> some View`

Rotates the view’s content by an angle about an axis that you specify as a
tuple of elements.

`func transformEffect(CGAffineTransform) -> some View`

Applies an affine transformation to this view’s rendered output.

`func transform3DEffect(AffineTransform3D) -> some View`

Applies a 3D transformation to the receiver.

`func projectionEffect(ProjectionTransform) -> some View`

Applies a projection transformation to this view’s rendered output.

`struct ProjectionTransform`

`enum ContentMode`

Constants that define how a view’s content fills the available space.

Instance Method

# rotationEffect(_:anchor:)

Rotates a view’s rendered output in two dimensions around the specified point.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func rotationEffect(
        _ angle: Angle,
        anchor: UnitPoint = .center
    ) -> some View
    

##  Parameters

`angle`

    

The angle by which to rotate the view.

`anchor`

    

A unit point within the view about which to perform the rotation. The default
value is `center`.

## Return Value

A view with rotated content.

## Discussion

This modifier rotates the view’s content around the axis that points out of
the xy-plane. It has no effect on the view’s frame. The following code rotates
text by 22˚ and then draws a border around the modified view to show that the
frame remains unchanged by the rotation modifier:

## See Also

### Scaling, rotating, or transforming a view

`func scaledToFill() -> some View`

Scales this view to fill its parent.

`func scaledToFit() -> some View`

Scales this view to fit its parent.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(CGSize, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified factor.

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified size in each dimension.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> ModifiedContent<Self,
_UniformScaleEffect>`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
some View`

Scales this view by the specified horizontal, vertical, and depth factors.

`func aspectRatio(CGFloat?, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the specified aspect ratio.

`func aspectRatio(CGSize, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the aspect ratio of the given size.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some
View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some View`

Rotates the view’s content by the specified 3D rotation value.

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
some View`

Rotates the view’s content by an angle about an axis that you specify as a
rotation axis value.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> some View`

Rotates the view’s content by an angle about an axis that you specify as a
tuple of elements.

`func transformEffect(CGAffineTransform) -> some View`

Applies an affine transformation to this view’s rendered output.

`func transform3DEffect(AffineTransform3D) -> some View`

Applies a 3D transformation to the receiver.

`func projectionEffect(ProjectionTransform) -> some View`

Applies a projection transformation to this view’s rendered output.

`struct ProjectionTransform`

`enum ContentMode`

Constants that define how a view’s content fills the available space.

Instance Method

# rotation3DEffect(_:anchor:)

Rotates the view’s content by the specified 3D rotation value.

visionOS 1.0+

    
    
    func rotation3DEffect(
        _ rotation: Rotation3D,
        anchor: UnitPoint3D = .center
    ) -> some View
    

##  Parameters

`rotation`

    

A rotation to apply to the view’s content.

`anchor`

    

The unit point within the view about which to perform the rotation. The
default value is `center`.

## Return Value

A view with rotated content.

## Discussion

This modifier rotates the view’s content without changing the view’s frame.
The following code displays a 3D model with a rotation of 45° about the y-axis
using the default anchor point at the center of the view:

## See Also

### Scaling, rotating, or transforming a view

`func scaledToFill() -> some View`

Scales this view to fill its parent.

`func scaledToFit() -> some View`

Scales this view to fit its parent.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(CGSize, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified factor.

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified size in each dimension.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> ModifiedContent<Self,
_UniformScaleEffect>`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
some View`

Scales this view by the specified horizontal, vertical, and depth factors.

`func aspectRatio(CGFloat?, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the specified aspect ratio.

`func aspectRatio(CGSize, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the aspect ratio of the given size.

`func rotationEffect(Angle, anchor: UnitPoint) -> some View`

Rotates a view’s rendered output in two dimensions around the specified point.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some
View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
some View`

Rotates the view’s content by an angle about an axis that you specify as a
rotation axis value.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> some View`

Rotates the view’s content by an angle about an axis that you specify as a
tuple of elements.

`func transformEffect(CGAffineTransform) -> some View`

Applies an affine transformation to this view’s rendered output.

`func transform3DEffect(AffineTransform3D) -> some View`

Applies a 3D transformation to the receiver.

`func projectionEffect(ProjectionTransform) -> some View`

Applies a projection transformation to this view’s rendered output.

`struct ProjectionTransform`

`enum ContentMode`

Constants that define how a view’s content fills the available space.

Instance Method

# rotation3DEffect(_:axis:anchor:anchorZ:perspective:)

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func rotation3DEffect(
        _ angle: Angle,
        axis: (x: CGFloat, y: CGFloat, z: CGFloat),
        anchor: UnitPoint = .center,
        anchorZ: CGFloat = 0,
        perspective: CGFloat = 1
    ) -> some View
    

##  Parameters

`angle`

    

The angle by which to rotate the view’s content.

`axis`

    

The axis of rotation, specified as a tuple with named elements for each of the
three spatial dimensions.

`anchor`

    

A two dimensional unit point within the view about which to perform the
rotation. The default value is `center`.

`anchorZ`

    

The location on the z-axis around which to rotate the content. The default is
`0`.

`perspective`

    

The relative vanishing point for the rotation. The default is `1`.

## Return Value

A view with rotated content.

## Discussion

Use this method to create the effect of rotating a view in three dimensions
around a specified axis of rotation. The modifier projects the rotated content
onto the original view’s plane. Use the `perspective` value to control the
renderer’s vanishing point. The following example creates the appearance of
rotating text 45˚ about the y-axis:

Important

In visionOS, create this effect with
`perspectiveRotationEffect(_:axis:anchor:anchorZ:perspective:)` instead. To
truly rotate a view in three dimensions, use a 3D rotation modifier without a
perspective input like `rotation3DEffect(_:axis:anchor:)`.

## See Also

### Scaling, rotating, or transforming a view

`func scaledToFill() -> some View`

Scales this view to fill its parent.

`func scaledToFit() -> some View`

Scales this view to fit its parent.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(CGSize, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified factor.

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified size in each dimension.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> ModifiedContent<Self,
_UniformScaleEffect>`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
some View`

Scales this view by the specified horizontal, vertical, and depth factors.

`func aspectRatio(CGFloat?, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the specified aspect ratio.

`func aspectRatio(CGSize, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the aspect ratio of the given size.

`func rotationEffect(Angle, anchor: UnitPoint) -> some View`

Rotates a view’s rendered output in two dimensions around the specified point.

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some
View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some View`

Rotates the view’s content by the specified 3D rotation value.

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
some View`

Rotates the view’s content by an angle about an axis that you specify as a
rotation axis value.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> some View`

Rotates the view’s content by an angle about an axis that you specify as a
tuple of elements.

`func transformEffect(CGAffineTransform) -> some View`

Applies an affine transformation to this view’s rendered output.

`func transform3DEffect(AffineTransform3D) -> some View`

Applies a 3D transformation to the receiver.

`func projectionEffect(ProjectionTransform) -> some View`

Applies a projection transformation to this view’s rendered output.

`struct ProjectionTransform`

`enum ContentMode`

Constants that define how a view’s content fills the available space.

Instance Method

# rotation3DEffect(_:axis:anchor:)

Rotates the view’s content by an angle about an axis that you specify as a
tuple of elements.

visionOS 1.0+

    
    
    func rotation3DEffect(
        _ angle: Angle,
        axis: (x: CGFloat, y: CGFloat, z: CGFloat),
        anchor: UnitPoint3D = .center
    ) -> some View
    

##  Parameters

`angle`

    

The angle by which to rotate the view’s content.

`axis`

    

The axis of rotation, specified as a tuple with named elements for each of the
three spatial dimensions.

`anchor`

    

The unit point within the view about which to perform the rotation. The
default value is `center`.

## Return Value

A view with rotated content.

## Discussion

This modifier rotates the view’s content without changing the view’s frame.
The following code displays a 3D model with a rotation of 45° about the y-axis
using the default anchor point at the center of the view:

## See Also

### Scaling, rotating, or transforming a view

`func scaledToFill() -> some View`

Scales this view to fill its parent.

`func scaledToFit() -> some View`

Scales this view to fit its parent.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(CGSize, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified factor.

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified size in each dimension.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> ModifiedContent<Self,
_UniformScaleEffect>`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
some View`

Scales this view by the specified horizontal, vertical, and depth factors.

`func aspectRatio(CGFloat?, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the specified aspect ratio.

`func aspectRatio(CGSize, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the aspect ratio of the given size.

`func rotationEffect(Angle, anchor: UnitPoint) -> some View`

Rotates a view’s rendered output in two dimensions around the specified point.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some
View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some View`

Rotates the view’s content by the specified 3D rotation value.

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
some View`

Rotates the view’s content by an angle about an axis that you specify as a
rotation axis value.

`func transformEffect(CGAffineTransform) -> some View`

Applies an affine transformation to this view’s rendered output.

`func transform3DEffect(AffineTransform3D) -> some View`

Applies a 3D transformation to the receiver.

`func projectionEffect(ProjectionTransform) -> some View`

Applies a projection transformation to this view’s rendered output.

`struct ProjectionTransform`

`enum ContentMode`

Constants that define how a view’s content fills the available space.

Instance Method

# rotation3DEffect(_:axis:anchor:)

Rotates the view’s content by an angle about an axis that you specify as a
rotation axis value.

visionOS 1.0+

    
    
    func rotation3DEffect(
        _ angle: Angle,
        axis: RotationAxis3D,
        anchor: UnitPoint3D = .center
    ) -> some View
    

##  Parameters

`angle`

    

The angle by which to rotate the view’s content.

`axis`

    

The axis of rotation.

`anchor`

    

The unit point within the view about which to perform the rotation. The
default value is `center`.

## Return Value

A view with rotated content.

## Discussion

This modifier rotates the view’s content without changing the view’s frame.
The following code displays a 3D model with a rotation of 45° about the y-axis
using the default anchor point at the center of the view:

## See Also

### Scaling, rotating, or transforming a view

`func scaledToFill() -> some View`

Scales this view to fill its parent.

`func scaledToFit() -> some View`

Scales this view to fit its parent.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(CGSize, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified factor.

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified size in each dimension.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> ModifiedContent<Self,
_UniformScaleEffect>`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
some View`

Scales this view by the specified horizontal, vertical, and depth factors.

`func aspectRatio(CGFloat?, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the specified aspect ratio.

`func aspectRatio(CGSize, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the aspect ratio of the given size.

`func rotationEffect(Angle, anchor: UnitPoint) -> some View`

Rotates a view’s rendered output in two dimensions around the specified point.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some
View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some View`

Rotates the view’s content by the specified 3D rotation value.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> some View`

Rotates the view’s content by an angle about an axis that you specify as a
tuple of elements.

`func transformEffect(CGAffineTransform) -> some View`

Applies an affine transformation to this view’s rendered output.

`func transform3DEffect(AffineTransform3D) -> some View`

Applies a 3D transformation to the receiver.

`func projectionEffect(ProjectionTransform) -> some View`

Applies a projection transformation to this view’s rendered output.

`struct ProjectionTransform`

`enum ContentMode`

Constants that define how a view’s content fills the available space.

Instance Method

# perspectiveRotationEffect(_:axis:anchor:anchorZ:perspective:)

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

visionOS 1.0+

    
    
    func perspectiveRotationEffect(
        _ angle: Angle,
        axis: (x: CGFloat, y: CGFloat, z: CGFloat),
        anchor: UnitPoint = .center,
        anchorZ: CGFloat = 0,
        perspective: CGFloat = 1
    ) -> some View
    

##  Parameters

`angle`

    

The angle by which to rotate the view’s content.

`axis`

    

The axis of rotation, specified as a tuple with named elements for each of the
three spatial dimensions.

`anchor`

    

A two dimensional unit point within the view about which to perform the
rotation. The default value is `center`.

`anchorZ`

    

The location on the z-axis around which to rotate the content. The default is
`0`.

`perspective`

    

The relative vanishing point for the rotation. The default is `1`.

## Return Value

A view with rotated content.

## Discussion

Use this method to create the effect of rotating a view in three dimensions
around a specified axis of rotation. The modifier projects the rotated, two-
dimensional content onto the original view’s plane. Use the `perspective`
input to control the renderer’s vanishing point. The following example creates
the appearance of rotating text 45˚ about the y-axis:

Important

To truly rotate a view in three dimensions, use a 3D rotation modifier without
a perspective input like `rotation3DEffect(_:axis:anchor:)`.

## See Also

### Scaling, rotating, or transforming a view

`func scaledToFill() -> some View`

Scales this view to fill its parent.

`func scaledToFit() -> some View`

Scales this view to fit its parent.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(CGSize, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified factor.

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified size in each dimension.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> ModifiedContent<Self,
_UniformScaleEffect>`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
some View`

Scales this view by the specified horizontal, vertical, and depth factors.

`func aspectRatio(CGFloat?, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the specified aspect ratio.

`func aspectRatio(CGSize, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the aspect ratio of the given size.

`func rotationEffect(Angle, anchor: UnitPoint) -> some View`

Rotates a view’s rendered output in two dimensions around the specified point.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some View`

Rotates the view’s content by the specified 3D rotation value.

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
some View`

Rotates the view’s content by an angle about an axis that you specify as a
rotation axis value.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> some View`

Rotates the view’s content by an angle about an axis that you specify as a
tuple of elements.

`func transformEffect(CGAffineTransform) -> some View`

Applies an affine transformation to this view’s rendered output.

`func transform3DEffect(AffineTransform3D) -> some View`

Applies a 3D transformation to the receiver.

`func projectionEffect(ProjectionTransform) -> some View`

Applies a projection transformation to this view’s rendered output.

`struct ProjectionTransform`

`enum ContentMode`

Constants that define how a view’s content fills the available space.

Instance Method

# projectionEffect(_:)

Applies a projection transformation to this view’s rendered output.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func projectionEffect(_ transform: ProjectionTransform) -> some View
    

##  Parameters

`transform`

    

A `ProjectionTransform` to apply to the view.

## Discussion

Use `projectionEffect(_:)` to apply a 3D transformation to the view.

The example below rotates the text 30˚ around the `z` axis, which is the axis
pointing out of the screen:

## See Also

### Scaling, rotating, or transforming a view

`func scaledToFill() -> some View`

Scales this view to fill its parent.

`func scaledToFit() -> some View`

Scales this view to fit its parent.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(CGSize, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified factor.

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified size in each dimension.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> ModifiedContent<Self,
_UniformScaleEffect>`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
some View`

Scales this view by the specified horizontal, vertical, and depth factors.

`func aspectRatio(CGFloat?, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the specified aspect ratio.

`func aspectRatio(CGSize, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the aspect ratio of the given size.

`func rotationEffect(Angle, anchor: UnitPoint) -> some View`

Rotates a view’s rendered output in two dimensions around the specified point.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some
View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some View`

Rotates the view’s content by the specified 3D rotation value.

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
some View`

Rotates the view’s content by an angle about an axis that you specify as a
rotation axis value.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> some View`

Rotates the view’s content by an angle about an axis that you specify as a
tuple of elements.

`func transformEffect(CGAffineTransform) -> some View`

Applies an affine transformation to this view’s rendered output.

`func transform3DEffect(AffineTransform3D) -> some View`

Applies a 3D transformation to the receiver.

`struct ProjectionTransform`

`enum ContentMode`

Constants that define how a view’s content fills the available space.

Instance Method

# transformEffect(_:)

Applies an affine transformation to this view’s rendered output.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func transformEffect(_ transform: CGAffineTransform) -> some View
    

##  Parameters

`transform`

    

A `CGAffineTransform` to apply to the view.

## Discussion

Use `transformEffect(_:)` to rotate, scale, translate, or skew the output of
the view according to the provided `CGAffineTransform`.

In the example below, the text is rotated at -30˚ on the `y` axis.

## See Also

### Scaling, rotating, or transforming a view

`func scaledToFill() -> some View`

Scales this view to fill its parent.

`func scaledToFit() -> some View`

Scales this view to fit its parent.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(CGSize, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified factor.

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified size in each dimension.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> ModifiedContent<Self,
_UniformScaleEffect>`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
some View`

Scales this view by the specified horizontal, vertical, and depth factors.

`func aspectRatio(CGFloat?, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the specified aspect ratio.

`func aspectRatio(CGSize, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the aspect ratio of the given size.

`func rotationEffect(Angle, anchor: UnitPoint) -> some View`

Rotates a view’s rendered output in two dimensions around the specified point.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some
View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some View`

Rotates the view’s content by the specified 3D rotation value.

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
some View`

Rotates the view’s content by an angle about an axis that you specify as a
rotation axis value.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> some View`

Rotates the view’s content by an angle about an axis that you specify as a
tuple of elements.

`func transform3DEffect(AffineTransform3D) -> some View`

Applies a 3D transformation to the receiver.

`func projectionEffect(ProjectionTransform) -> some View`

Applies a projection transformation to this view’s rendered output.

`struct ProjectionTransform`

`enum ContentMode`

Constants that define how a view’s content fills the available space.

Instance Method

# transform3DEffect(_:)

Applies a 3D transformation to the receiver.

visionOS 1.0+

    
    
    func transform3DEffect(_ transform: AffineTransform3D) -> some View
    

##  Parameters

`transform`

    

The 3D transformation to apply to the view, interpreting it as a 3D plane in
space.

## Return Value

A view that renders transformed according to the provided `transform`

## See Also

### Scaling, rotating, or transforming a view

`func scaledToFill() -> some View`

Scales this view to fill its parent.

`func scaledToFit() -> some View`

Scales this view to fit its parent.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(CGSize, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given vertical and horizontal size
amounts, relative to an anchor point.

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified factor.

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> some View`

Scales this view uniformly by the specified size in each dimension.

`func scaleEffect(CGFloat, anchor: UnitPoint) -> ModifiedContent<Self,
_UniformScaleEffect>`

Scales this view’s rendered output by the given amount in both the horizontal
and vertical directions, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View`

Scales this view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
some View`

Scales this view by the specified horizontal, vertical, and depth factors.

`func aspectRatio(CGFloat?, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the specified aspect ratio.

`func aspectRatio(CGSize, contentMode: ContentMode) -> some View`

Constrains this view’s dimensions to the aspect ratio of the given size.

`func rotationEffect(Angle, anchor: UnitPoint) -> some View`

Rotates a view’s rendered output in two dimensions around the specified point.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some
View`

Renders a view’s content as if it’s rotated in three dimensions around the
specified axis.

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some View`

Rotates the view’s content by the specified 3D rotation value.

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
some View`

Rotates the view’s content by an angle about an axis that you specify as a
rotation axis value.

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> some View`

Rotates the view’s content by an angle about an axis that you specify as a
tuple of elements.

`func transformEffect(CGAffineTransform) -> some View`

Applies an affine transformation to this view’s rendered output.

`func projectionEffect(ProjectionTransform) -> some View`

Applies a projection transformation to this view’s rendered output.

`struct ProjectionTransform`

`enum ContentMode`

Constants that define how a view’s content fills the available space.

Instance Method

# blur(radius:opaque:)

Applies a Gaussian blur to this view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func blur(
        radius: CGFloat,
        opaque: Bool = false
    ) -> some View
    

##  Parameters

`radius`

    

The radial size of the blur. A blur is more diffuse when its radius is large.

`opaque`

    

A Boolean value that indicates whether the blur renderer permits transparency
in the blur output. Set to `true` to create an opaque blur, or set to `false`
to permit transparency.

## Discussion

Use `blur(radius:opaque:)` to apply a gaussian blur effect to the rendering of
this view.

The example below shows two `Text` views, the first with no blur effects, the
second with `blur(radius:opaque:)` applied with the `radius` set to `2`. The
larger the radius, the more diffuse the effect.

## See Also

### Applying blur and shadows

`func shadow(color: Color, radius: CGFloat, x: CGFloat, y: CGFloat) -> some
View`

Adds a shadow to this view.

`struct ColorMatrix`

A matrix to use in an RGBA color transformation.

Instance Method

# opacity(_:)

Sets the transparency of this view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func opacity(_ opacity: Double) -> some View
    

##  Parameters

`opacity`

    

A value between 0 (fully transparent) and 1 (fully opaque).

## Return Value

A view that sets the transparency of this view.

## Discussion

Apply opacity to reveal views that are behind another view or to de-emphasize
a view.

When applying the `opacity(_:)` modifier to a view that has already had its
opacity transformed, the modifier multiplies the effect of the underlying
opacity transformation.

The example below shows yellow and red rectangles configured to overlap. The
top yellow rectangle has its opacity set to 50%, allowing the occluded portion
of the bottom rectangle to be visible:

## See Also

### Hiding views

`func hidden() -> some View`

Hides this view unconditionally.

Instance Method

# brightness(_:)

Brightens this view by the specified amount.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func brightness(_ amount: Double) -> some View
    

##  Parameters

`amount`

    

A value between 0 (no effect) and 1 (full white brightening) that represents
the intensity of the brightness effect.

## Return Value

A view that brightens this view by the specified amount.

## Discussion

Use `brightness(_:)` to brighten the intensity of the colors in a view. The
example below shows a series of red squares, with their brightness increasing
from 0 (fully red) to 100% (white) in 20% increments.

## See Also

### Transforming colors

`func contrast(Double) -> some View`

Sets the contrast and separation between similar colors in this view.

`func colorInvert() -> some View`

Inverts the colors in this view.

`func colorMultiply(Color) -> some View`

Adds a color multiplication effect to this view.

`func saturation(Double) -> some View`

Adjusts the color saturation of this view.

`func grayscale(Double) -> some View`

Adds a grayscale effect to this view.

`func hueRotation(Angle) -> some View`

Applies a hue rotation effect to this view.

`func luminanceToAlpha() -> some View`

Adds a luminance to alpha effect to this view.

Instance Method

# contrast(_:)

Sets the contrast and separation between similar colors in this view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func contrast(_ amount: Double) -> some View
    

##  Parameters

`amount`

    

The intensity of color contrast to apply. negative values invert colors in
addition to applying contrast.

## Return Value

A view that applies color contrast to this view.

## Discussion

Apply contrast to a view to increase or decrease the separation between
similar colors in the view.

In the example below, the `contrast(_:)` modifier is applied to a set of red
squares each containing a contrasting green inner circle. At each step in the
loop, the `contrast(_:)` modifier changes the contrast of the circle/square
view in 20% increments. This ranges from -20% contrast (yielding inverted
colors — turning the red square to pale-green and the green circle to mauve),
to neutral-gray at 0%, to 100% contrast (bright-red square / bright-green
circle). Applying negative contrast values, as shown in the -20% square, will
apply contrast in addition to inverting colors.

## See Also

### Transforming colors

`func brightness(Double) -> some View`

Brightens this view by the specified amount.

`func colorInvert() -> some View`

Inverts the colors in this view.

`func colorMultiply(Color) -> some View`

Adds a color multiplication effect to this view.

`func saturation(Double) -> some View`

Adjusts the color saturation of this view.

`func grayscale(Double) -> some View`

Adds a grayscale effect to this view.

`func hueRotation(Angle) -> some View`

Applies a hue rotation effect to this view.

`func luminanceToAlpha() -> some View`

Adds a luminance to alpha effect to this view.

Instance Method

# colorInvert()

Inverts the colors in this view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func colorInvert() -> some View
    

## Return Value

A view that inverts its colors.

## Discussion

The `colorInvert()` modifier inverts all of the colors in a view so that each
color displays as its complementary color. For example, blue converts to
yellow, and white converts to black.

In the example below, two red squares each have an interior green circle. The
inverted square shows the effect of the square’s colors: complimentary colors
for red and green — teal and purple.

## See Also

### Transforming colors

`func brightness(Double) -> some View`

Brightens this view by the specified amount.

`func contrast(Double) -> some View`

Sets the contrast and separation between similar colors in this view.

`func colorMultiply(Color) -> some View`

Adds a color multiplication effect to this view.

`func saturation(Double) -> some View`

Adjusts the color saturation of this view.

`func grayscale(Double) -> some View`

Adds a grayscale effect to this view.

`func hueRotation(Angle) -> some View`

Applies a hue rotation effect to this view.

`func luminanceToAlpha() -> some View`

Adds a luminance to alpha effect to this view.

Instance Method

# colorMultiply(_:)

Adds a color multiplication effect to this view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func colorMultiply(_ color: Color) -> some View
    

##  Parameters

`color`

    

The color to bias this view toward.

## Return Value

A view with a color multiplication effect.

## Discussion

The following example shows two versions of the same image side by side; at
left is the original, and at right is a duplicate with the `colorMultiply(_:)`
modifier applied with `purple`.

## See Also

### Transforming colors

`func brightness(Double) -> some View`

Brightens this view by the specified amount.

`func contrast(Double) -> some View`

Sets the contrast and separation between similar colors in this view.

`func colorInvert() -> some View`

Inverts the colors in this view.

`func saturation(Double) -> some View`

Adjusts the color saturation of this view.

`func grayscale(Double) -> some View`

Adds a grayscale effect to this view.

`func hueRotation(Angle) -> some View`

Applies a hue rotation effect to this view.

`func luminanceToAlpha() -> some View`

Adds a luminance to alpha effect to this view.

Instance Method

# saturation(_:)

Adjusts the color saturation of this view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func saturation(_ amount: Double) -> some View
    

##  Parameters

`amount`

    

The amount of saturation to apply to this view.

## Return Value

A view that adjusts the saturation of this view.

## Discussion

Use color saturation to increase or decrease the intensity of colors in a
view.

The example below shows a series of red squares with their saturation
increasing from 0 (gray) to 100% (fully-red) in 20% increments:

See Also

`contrast(_:)`

## See Also

### Transforming colors

`func brightness(Double) -> some View`

Brightens this view by the specified amount.

`func contrast(Double) -> some View`

Sets the contrast and separation between similar colors in this view.

`func colorInvert() -> some View`

Inverts the colors in this view.

`func colorMultiply(Color) -> some View`

Adds a color multiplication effect to this view.

`func grayscale(Double) -> some View`

Adds a grayscale effect to this view.

`func hueRotation(Angle) -> some View`

Applies a hue rotation effect to this view.

`func luminanceToAlpha() -> some View`

Adds a luminance to alpha effect to this view.

Instance Method

# grayscale(_:)

Adds a grayscale effect to this view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func grayscale(_ amount: Double) -> some View
    

##  Parameters

`amount`

    

The intensity of grayscale to apply from 0.0 to less than 1.0. Values closer
to 0.0 are more colorful, and values closer to 1.0 are less colorful.

## Return Value

A view that adds a grayscale effect to this view.

## Discussion

A grayscale effect reduces the intensity of colors in this view.

The example below shows a series of red squares with their grayscale effect
increasing from 0 (reddest) to 99% (fully desaturated) in approximate 20%
increments:

## See Also

### Transforming colors

`func brightness(Double) -> some View`

Brightens this view by the specified amount.

`func contrast(Double) -> some View`

Sets the contrast and separation between similar colors in this view.

`func colorInvert() -> some View`

Inverts the colors in this view.

`func colorMultiply(Color) -> some View`

Adds a color multiplication effect to this view.

`func saturation(Double) -> some View`

Adjusts the color saturation of this view.

`func hueRotation(Angle) -> some View`

Applies a hue rotation effect to this view.

`func luminanceToAlpha() -> some View`

Adds a luminance to alpha effect to this view.

Instance Method

# hueRotation(_:)

Applies a hue rotation effect to this view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func hueRotation(_ angle: Angle) -> some View
    

##  Parameters

`angle`

    

The hue rotation angle to apply to the colors in this view.

## Return Value

A view that applies a hue rotation effect to this view.

## Discussion

Use hue rotation effect to shift all of the colors in a view according to the
angle you specify.

The example below shows a series of squares filled with a linear gradient.
Each square shows the effect of a 36˚ hueRotation (a total of 180˚ across the
5 squares) on the gradient:

## See Also

### Transforming colors

`func brightness(Double) -> some View`

Brightens this view by the specified amount.

`func contrast(Double) -> some View`

Sets the contrast and separation between similar colors in this view.

`func colorInvert() -> some View`

Inverts the colors in this view.

`func colorMultiply(Color) -> some View`

Adds a color multiplication effect to this view.

`func saturation(Double) -> some View`

Adjusts the color saturation of this view.

`func grayscale(Double) -> some View`

Adds a grayscale effect to this view.

`func luminanceToAlpha() -> some View`

Adds a luminance to alpha effect to this view.

Instance Method

# luminanceToAlpha()

Adds a luminance to alpha effect to this view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func luminanceToAlpha() -> some View
    

## Return Value

A view with the luminance to alpha effect applied.

## Discussion

Use this modifier to create a semitransparent mask, with the opacity of each
part of the modified view controlled by the luminance of the corresponding
part of the original view. Regions of lower luminance become more transparent,
while higher luminance yields greater opacity.

In particular, the modifier maps the red, green, and blue components of each
input pixel’s color to a grayscale value, and that value becomes the alpha
component of a black pixel in the output. This modifier produces an effect
that’s equivalent to using the `feColorMatrix` filter primitive with the
`luminanceToAlpha` type attribute, as defined by the Scalable Vector Graphics
(SVG) 2 specification.

The example below defines a `Palette` view as a series of rectangles, each
composed as a `Color` with a particular white value, and then displays two
versions of the palette over a blue background:

The unmodified version of the palette contains rectangles that range from
solid black to solid white, thus with increasing luminance. The second version
of the palette, which has the `luminanceToAlpha()` modifier applied, allows
the background to show through in an amount that corresponds inversely to the
luminance of the input.

## See Also

### Transforming colors

`func brightness(Double) -> some View`

Brightens this view by the specified amount.

`func contrast(Double) -> some View`

Sets the contrast and separation between similar colors in this view.

`func colorInvert() -> some View`

Inverts the colors in this view.

`func colorMultiply(Color) -> some View`

Adds a color multiplication effect to this view.

`func saturation(Double) -> some View`

Adjusts the color saturation of this view.

`func grayscale(Double) -> some View`

Adds a grayscale effect to this view.

`func hueRotation(Angle) -> some View`

Applies a hue rotation effect to this view.

Instance Method

# shadow(color:radius:x:y:)

Adds a shadow to this view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func shadow(
        color: Color = Color(.sRGBLinear, white: 0, opacity: 0.33),
        radius: CGFloat,
        x: CGFloat = 0,
        y: CGFloat = 0
    ) -> some View
    

##  Parameters

`color`

    

The shadow’s color.

`radius`

    

A measure of how much to blur the shadow. Larger values result in more blur.

`x`

    

An amount to offset the shadow horizontally from the view.

`y`

    

An amount to offset the shadow vertically from the view.

## Return Value

A view that adds a shadow to this view.

## Discussion

Use this modifier to add a shadow of a specified color behind a view. You can
offset the shadow from its view independently in the horizontal and vertical
dimensions using the `x` and `y` parameters. You can also blur the edges of
the shadow using the `radius` parameter. Use a radius of zero to create a
sharp shadow. Larger radius values produce softer shadows.

The example below creates a grid of boxes with varying offsets and blur. Each
box displays its radius and offset values for reference.

The example above uses `primary` as the color to make the shadow easy to see
for the purpose of illustration. In practice, you might prefer something more
subtle, like `gray`. If you don’t specify a color, the method uses a semi-
transparent black.

## See Also

### Applying blur and shadows

`func blur(radius: CGFloat, opaque: Bool) -> some View`

Applies a Gaussian blur to this view.

`struct ColorMatrix`

A matrix to use in an RGBA color transformation.

Instance Method

# visualEffect(_:)

Applies effects to this view, while providing access to layout information
through a geometry proxy.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func visualEffect(_ effect: @escaping (EmptyVisualEffect, GeometryProxy) -> some VisualEffect) -> some View
    

##  Parameters

`effect`

    

A closure that returns the effect to be applied. The first argument provided
to the closure is a placeholder representing this view. The second argument is
a `GeometryProxy`.

## Return Value

A view with the effect applied.

## Discussion

You return new effects by calling functions on the first argument provided to
the `effect` closure. In this example, `ContentView` is offset by its own
size, causing its top left corner to appear where the bottom right corner was
originally located:

## See Also

### Applying effects based on geometry

`func visualEffect3D((EmptyVisualEffect, GeometryProxy3D) -> some
VisualEffect) -> some View`

Applies effects to this view, while providing access to layout information
through a 3D geometry proxy.

`protocol VisualEffect`

Visual Effects change the visual appearance of a view without changing its
ancestors or descendents.

`struct EmptyVisualEffect`

The base visual effect that you apply additional effect to.

Instance Method

# visualEffect3D(_:)

Applies effects to this view, while providing access to layout information
through a 3D geometry proxy.

visionOS 1.0+

    
    
    func visualEffect3D(_ effect: @escaping (EmptyVisualEffect, GeometryProxy3D) -> some VisualEffect) -> some View
    

##  Parameters

`effect`

    

A closure that returns the effect to be applied. The first argument provided
to the closure is a placeholder representing this view. The second argument is
a `GeometryProxy3D`.

## Return Value

A view with the effect applied.

## Discussion

You return new effects by calling functions on the first argument provided to
the `effect` closure. In this example, `ContentView` is offset in Z by its own
depth, causing its back face to appear where the front face of the view was
originally located:

## See Also

### Applying effects based on geometry

`func visualEffect((EmptyVisualEffect, GeometryProxy) -> some VisualEffect) ->
some View`

Applies effects to this view, while providing access to layout information
through a geometry proxy.

`protocol VisualEffect`

Visual Effects change the visual appearance of a view without changing its
ancestors or descendents.

`struct EmptyVisualEffect`

The base visual effect that you apply additional effect to.

Instance Method

# colorEffect(_:isEnabled:)

Returns a new view that applies `shader` to `self` as a filter effect on the
color of each pixel.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    func colorEffect(
        _ shader: Shader,
        isEnabled: Bool = true
    ) -> some View
    

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

### Accessing Metal shaders

`func distortionEffect(Shader, maxSampleOffset: CGSize, isEnabled: Bool) ->
some View`

Returns a new view that applies `shader` to `self` as a geometric distortion
effect on the location of each pixel.

`func layerEffect(Shader, maxSampleOffset: CGSize, isEnabled: Bool) -> some
View`

Returns a new view that applies `shader` to `self` as a filter on the raster
layer created from `self`.

`struct Shader`

A reference to a function in a Metal shader library, along with its bound
uniform argument values.

`struct ShaderFunction`

A reference to a function in a Metal shader library.

`struct ShaderLibrary`

A Metal shader library.

Instance Method

# distortionEffect(_:maxSampleOffset:isEnabled:)

Returns a new view that applies `shader` to `self` as a geometric distortion
effect on the location of each pixel.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    func distortionEffect(
        _ shader: Shader,
        maxSampleOffset: CGSize,
        isEnabled: Bool = true
    ) -> some View
    

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

### Accessing Metal shaders

`func colorEffect(Shader, isEnabled: Bool) -> some View`

Returns a new view that applies `shader` to `self` as a filter effect on the
color of each pixel.

`func layerEffect(Shader, maxSampleOffset: CGSize, isEnabled: Bool) -> some
View`

Returns a new view that applies `shader` to `self` as a filter on the raster
layer created from `self`.

`struct Shader`

A reference to a function in a Metal shader library, along with its bound
uniform argument values.

`struct ShaderFunction`

A reference to a function in a Metal shader library.

`struct ShaderLibrary`

A Metal shader library.

Instance Method

# layerEffect(_:maxSampleOffset:isEnabled:)

Returns a new view that applies `shader` to `self` as a filter on the raster
layer created from `self`.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    func layerEffect(
        _ shader: Shader,
        maxSampleOffset: CGSize,
        isEnabled: Bool = true
    ) -> some View
    

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

### Accessing Metal shaders

`func colorEffect(Shader, isEnabled: Bool) -> some View`

Returns a new view that applies `shader` to `self` as a filter effect on the
color of each pixel.

`func distortionEffect(Shader, maxSampleOffset: CGSize, isEnabled: Bool) ->
some View`

Returns a new view that applies `shader` to `self` as a geometric distortion
effect on the location of each pixel.

`struct Shader`

A reference to a function in a Metal shader library, along with its bound
uniform argument values.

`struct ShaderFunction`

A reference to a function in a Metal shader library.

`struct ShaderLibrary`

A Metal shader library.

Instance Method

# blendMode(_:)

Sets the blend mode for compositing this view with overlapping views.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func blendMode(_ blendMode: BlendMode) -> some View
    

##  Parameters

`blendMode`

    

The `BlendMode` for compositing this view.

## Return Value

A view that applies `blendMode` to this view.

## Discussion

Use `blendMode(_:)` to combine overlapping views and use a different visual
effect to produce the result. The `BlendMode` enumeration defines many
possible effects.

In the example below, the two overlapping rectangles have a
`BlendMode.colorBurn` effect applied, which effectively removes the non-
overlapping portion of the second image:

## See Also

### Compositing views

`func compositingGroup() -> some View`

Wraps this view in a compositing group.

`func drawingGroup(opaque: Bool, colorMode: ColorRenderingMode) -> some View`

Composites this view’s contents into an offscreen image before final display.

`enum BlendMode`

Modes for compositing a view with overlapping content.

`enum ColorRenderingMode`

The set of possible working color spaces for color-compositing operations.

Instance Method

# compositingGroup()

Wraps this view in a compositing group.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func compositingGroup() -> some View
    

## Return Value

A view that wraps this view in a compositing group.

## Discussion

A compositing group makes compositing effects in this view’s ancestor views,
such as opacity and the blend mode, take effect before this view is rendered.

Use `compositingGroup()` to apply effects to a parent view before applying
effects to this view.

In the example below the `compositingGroup()` modifier separates the
application of effects into stages. It applies the `opacity(_:)` effect to the
VStack before the `blur(radius:)` effect is applied to the views inside the
enclosed `ZStack`. This limits the scope of the opacity change to the
outermost view.

## See Also

### Compositing views

`func blendMode(BlendMode) -> some View`

Sets the blend mode for compositing this view with overlapping views.

`func drawingGroup(opaque: Bool, colorMode: ColorRenderingMode) -> some View`

Composites this view’s contents into an offscreen image before final display.

`enum BlendMode`

Modes for compositing a view with overlapping content.

`enum ColorRenderingMode`

The set of possible working color spaces for color-compositing operations.

Instance Method

# drawingGroup(opaque:colorMode:)

Composites this view’s contents into an offscreen image before final display.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func drawingGroup(
        opaque: Bool = false,
        colorMode: ColorRenderingMode = .nonLinear
    ) -> some View
    

##  Parameters

`opaque`

    

A Boolean value that indicates whether the image is opaque. The default is
`false`; if set to `true`, the alpha channel of the image must be `1`.

`colorMode`

    

One of the working color space and storage formats defined in
`ColorRenderingMode`. The default is `ColorRenderingMode.nonLinear`.

## Return Value

A view that composites this view’s contents into an offscreen image before
display.

## Discussion

The `drawingGroup(opaque:colorMode:)` modifier flattens a subtree of views
into a single view before rendering it.

In the example below, the contents of the view are composited to a single
bitmap; the bitmap is then displayed in place of the view:

Note

Views backed by native platform views may not render into the image. Instead,
they log a warning and display a placeholder image to highlight the error.

## See Also

### Compositing views

`func blendMode(BlendMode) -> some View`

Sets the blend mode for compositing this view with overlapping views.

`func compositingGroup() -> some View`

Wraps this view in a compositing group.

`enum BlendMode`

Modes for compositing a view with overlapping content.

`enum ColorRenderingMode`

The set of possible working color spaces for color-compositing operations.

Instance Method

# animation(_:)

Applies the given animation to this view when this view changes.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func animation(_ animation: Animation?) -> some View
    

Available when `Self` conforms to `Equatable`.

##  Parameters

`animation`

    

The animation to apply. If `animation` is `nil`, the view doesn’t animate.

## Return Value

A view that applies `animation` to this view whenever it changes.

## See Also

### Adding state-based animation to a view

`func animation<V>(Animation?, value: V) -> some View`

Applies the given animation to this view when the specified value changes.

`func animation<V>(Animation?, body: (PlaceholderContentView<Self>) -> V) ->
some View`

Applies the given animation to all animatable values within the `body`
closure.

Instance Method

# animation(_:value:)

Applies the given animation to this view when the specified value changes.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func animation<V>(
        _ animation: Animation?,
        value: V
    ) -> some View where V : Equatable
    

##  Parameters

`animation`

    

The animation to apply. If `animation` is `nil`, the view doesn’t animate.

`value`

    

A value to monitor for changes.

## Return Value

A view that applies `animation` to this view whenever `value` changes.

## See Also

### Adding state-based animation to a view

`func animation(Animation?) -> some View`

Applies the given animation to this view when this view changes.

Available when `Self` conforms to `Equatable`.

`func animation<V>(Animation?, body: (PlaceholderContentView<Self>) -> V) ->
some View`

Applies the given animation to all animatable values within the `body`
closure.

Instance Method

# animation(_:body:)

Applies the given animation to all animatable values within the `body`
closure.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func animation<V>(
        _ animation: Animation?,
        @ViewBuilder body: (PlaceholderContentView<Self>) -> V
    ) -> some View where V : View
    

## Discussion

Any modifiers applied to the content of `body` will be applied to this view,
and the `animation` will only be used on the modifiers defined in the `body`.

The following code animates the opacity changing with an easeInOut animation,
while the contents of MyView are animated with the implicit transaction’s
animation:

## See Also

### Adding state-based animation to a view

`func animation(Animation?) -> some View`

Applies the given animation to this view when this view changes.

Available when `Self` conforms to `Equatable`.

`func animation<V>(Animation?, value: V) -> some View`

Applies the given animation to this view when the specified value changes.

Instance Method

# keyframeAnimator(initialValue:repeating:content:keyframes:)

Loops the given keyframes continuously, updating the view using the modifiers
you apply in `body`.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func keyframeAnimator<Value>(
        initialValue: Value,
        repeating: Bool = true,
        @ViewBuilder content: @escaping (PlaceholderContentView<Self>, Value) -> some View,
        @KeyframesBuilder<Value> keyframes: @escaping (Value) -> some Keyframes
    ) -> some View
    

##  Parameters

`initialValue`

    

The initial value that the keyframes will animate from.

`repeating`

    

Whether the keyframes are currently repeating. If false, the value at the
beginning of the keyframe timeline will be provided to the content closure.

`content`

    

A view builder closure that takes two parameters. The first parameter is a
proxy value representing the modified view. The second parameter is the
interpolated value generated by the keyframes.

`keyframes`

    

Keyframes defining how the value changes over time. The current value of the
animator is the single argument, which is equal to `initialValue` when the
view first appears, then is equal to the end value of the previous keyframe
animation on subsequent calls.

## Discussion

Note that the `content` closure will be updated on every frame while
animating, so avoid performing any expensive operations directly within
`content`.

## See Also

### Creating keyframe-based animation

`func keyframeAnimator<Value>(initialValue: Value, trigger: some Equatable,
content: (PlaceholderContentView<Self>, Value) -> some View, keyframes:
(Value) -> some Keyframes) -> some View`

Plays the given keyframes when the given trigger value changes, updating the
view using the modifiers you apply in `body`.

`struct KeyframeAnimator`

A container that animates its content with keyframes.

`protocol Keyframes`

A type that defines changes to a value over time.

`struct KeyframeTimeline`

A description of how a value changes over time, modeled using keyframes.

`struct KeyframeTrack`

A sequence of keyframes animating a single property of a root type.

`struct KeyframeTrackContentBuilder`

The builder that creates keyframe track content from the keyframes that you
define within a closure.

`struct KeyframesBuilder`

A builder that combines keyframe content values into a single value.

`protocol KeyframeTrackContent`

A group of keyframes that define an interpolation curve of an animatable
value.

`struct CubicKeyframe`

A keyframe that uses a cubic curve to smoothly interpolate between values.

`struct LinearKeyframe`

A keyframe that uses simple linear interpolation.

`struct MoveKeyframe`

A keyframe that immediately moves to the given value without interpolating.

`struct SpringKeyframe`

A keyframe that uses a spring function to interpolate to the given value.

Instance Method

# keyframeAnimator(initialValue:trigger:content:keyframes:)

Plays the given keyframes when the given trigger value changes, updating the
view using the modifiers you apply in `body`.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func keyframeAnimator<Value>(
        initialValue: Value,
        trigger: some Equatable,
        @ViewBuilder content: @escaping (PlaceholderContentView<Self>, Value) -> some View,
        @KeyframesBuilder<Value> keyframes: @escaping (Value) -> some Keyframes
    ) -> some View
    

##  Parameters

`initialValue`

    

The initial value that the keyframes will animate from.

`trigger`

    

A value to observe for changes.

`content`

    

A view builder closure that takes two parameters. The first parameter is a
proxy value representing the modified view. The second parameter is the
interpolated value generated by the keyframes.

`keyframes`

    

Keyframes defining how the value changes over time. The current value of the
animator is the single argument, which is equal to `initialValue` when the
view first appears, then is equal to the end value of the previous keyframe
animation on subsequent calls.

## Discussion

Note that the `content` closure will be updated on every frame while
animating, so avoid performing any expensive operations directly within
`content`.

If the trigger value changes while animating, the `keyframes` closure will be
called with the current interpolated value, and the keyframes that you return
define a new animation that replaces the old one. The previous velocity will
be preserved, so cubic or spring keyframes will maintain continuity from the
previous animation if they do not specify a custom initial velocity.

When a keyframe animation finishes, the animator will remain at the end value,
which becomes the initial value for the next animation.

## See Also

### Creating keyframe-based animation

`func keyframeAnimator<Value>(initialValue: Value, repeating: Bool, content:
(PlaceholderContentView<Self>, Value) -> some View, keyframes: (Value) -> some
Keyframes) -> some View`

Loops the given keyframes continuously, updating the view using the modifiers
you apply in `body`.

`struct KeyframeAnimator`

A container that animates its content with keyframes.

`protocol Keyframes`

A type that defines changes to a value over time.

`struct KeyframeTimeline`

A description of how a value changes over time, modeled using keyframes.

`struct KeyframeTrack`

A sequence of keyframes animating a single property of a root type.

`struct KeyframeTrackContentBuilder`

The builder that creates keyframe track content from the keyframes that you
define within a closure.

`struct KeyframesBuilder`

A builder that combines keyframe content values into a single value.

`protocol KeyframeTrackContent`

A group of keyframes that define an interpolation curve of an animatable
value.

`struct CubicKeyframe`

A keyframe that uses a cubic curve to smoothly interpolate between values.

`struct LinearKeyframe`

A keyframe that uses simple linear interpolation.

`struct MoveKeyframe`

A keyframe that immediately moves to the given value without interpolating.

`struct SpringKeyframe`

A keyframe that uses a spring function to interpolate to the given value.

Instance Method

# phaseAnimator(_:content:animation:)

Animates effects that you apply to a view over a sequence of phases that
change continuously.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func phaseAnimator<Phase>(
        _ phases: some Sequence,
        @ViewBuilder content: @escaping (PlaceholderContentView<Self>, Phase) -> some View,
        animation: @escaping (Phase) -> Animation? = { _ in .default }
    ) -> some View where Phase : Equatable
    

##  Parameters

`phases`

    

The sequence of phases to cycle through. Ensure that the sequence isn’t empty.
If it is, SwiftUI logs a runtime warning and also returns a visual warning as
the output view.

`content`

    

A view builder closure that takes two parameters: a proxy value representing
the modified view and the current phase. You can apply effects to the proxy
based on the current phase.

`animation`

    

A closure that takes the current phase as input. Return the animation to use
when transitioning to the next phase. If you return `nil`, the transition
doesn’t animate. If you don’t set this parameter, SwiftUI uses a default
animation.

## Discussion

When the modified view first appears, this modifier renders its `content`
closure using the first phase as input to the closure, along with a proxy for
the modified view. Apply effects to the proxy — and thus to the modified view
— in a way that’s appropriate for the first phase value.

Right away, the modifier provides its `content` closure with the value of the
second phase. Update the effects that you apply to the proxy view accordingly,
and the modifier animates the change for you. As soon as the animation
completes, the procedure repeats using successive phases until reaching the
last phase, at which point the modifier loops back to the first phase.

## See Also

### Creating phase-based animation

Controlling the timing and movements of your animations

Build sophisticated animations that you control using phase and keyframe
animators.

`func phaseAnimator<Phase>(some Sequence, trigger: some Equatable, content:
(PlaceholderContentView<Self>, Phase) -> some View, animation: (Phase) ->
Animation?) -> some View`

Animates effects that you apply to a view over a sequence of phases that
change based on a trigger.

`struct PhaseAnimator`

A container that animates its content by automatically cycling through a
collection of phases that you provide, each defining a discrete step within an
animation.

Instance Method

# phaseAnimator(_:trigger:content:animation:)

Animates effects that you apply to a view over a sequence of phases that
change based on a trigger.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func phaseAnimator<Phase>(
        _ phases: some Sequence,
        trigger: some Equatable,
        @ViewBuilder content: @escaping (PlaceholderContentView<Self>, Phase) -> some View,
        animation: @escaping (Phase) -> Animation? = { _ in .default }
    ) -> some View where Phase : Equatable
    

##  Parameters

`phases`

    

The sequence of phases to cycle through. Ensure that the sequence isn’t empty.
If it is, SwiftUI logs a runtime warning and also returns a visual warning as
the output view.

`trigger`

    

A value whose changes cause the animator to use the next phase.

`content`

    

A view builder closure that takes two parameters: a proxy value representing
the modified view and the current phase. You can apply effects to the proxy
based on the current phase.

`animation`

    

A closure that takes the current phase as input. Return the animation to use
when transitioning to the next phase. If you return `nil`, the transition
doesn’t animate. If you don’t set this parameter, SwiftUI uses a default
animation.

## Discussion

When the modified view first appears, this modifier renders its `content`
closure using the first phase as input to the closure, along with a proxy for
the modified view. Apply effects to the proxy — and thus to the modified view
— in a way that’s appropriate for the first phase value.

Later, when the value of the `trigger` input changes, the modifier provides
its `content` closure with the value of the second phase. Update the effects
that you apply to the proxy view accordingly, and the modifier animates the
change for you. The next time the `trigger` input changes, this procedure
repeats using successive phases until reaching the last phase, at which point
the modifier loops back to the first phase.

## See Also

### Creating phase-based animation

Controlling the timing and movements of your animations

Build sophisticated animations that you control using phase and keyframe
animators.

`func phaseAnimator<Phase>(some Sequence, content:
(PlaceholderContentView<Self>, Phase) -> some View, animation: (Phase) ->
Animation?) -> some View`

Animates effects that you apply to a view over a sequence of phases that
change continuously.

`struct PhaseAnimator`

A container that animates its content by automatically cycling through a
collection of phases that you provide, each defining a discrete step within an
animation.

Instance Method

# contentTransition(_:)

Modifies the view to use a given transition as its method of animating changes
to the contents of its views.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func contentTransition(_ transition: ContentTransition) -> some View
    

##  Parameters

`transition`

    

The transition to apply when animating the content change.

## Discussion

This modifier allows you to perform a transition that animates a change within
a single view. The provided `ContentTransition` can present an opacity
animation for content changes, an interpolated animation of the content’s
paths as they change, or perform no animation at all.

Tip

The `contentTransition(_:)` modifier only has an effect within the context of
an `Animation`.

In the following example, a `Button` changes the color and font size of a
`Text` view. Since both of these properties apply to the paths of the text,
the `interpolate` transition can animate a gradual change to these properties
through the entire transition. By contrast, the `opacity` transition would
simply fade between the start and end states.

This example uses an ease-in–ease-out animation with a five-second duration to
make it easier to see the effect of the interpolation. The figure below shows
the `Text` at the beginning of the animation, halfway through, and at the end.

Time| Display  
---|---  
Start|  
Middle|  
End|  
  
To control whether content transitions use GPU-accelerated rendering, set the
value of the `contentTransitionAddsDrawingGroup` environment variable.

## See Also

### Defining transitions

`func transition<T>(T) -> some View`

Associates a transition with the view.

`func transition(AnyTransition) -> some View`

Associates a transition with the view.

`protocol Transition`

A description of view changes to apply when a view is added to and removed
from the view hierarchy.

`struct TransitionProperties`

The properties a `Transition` can have.

`enum TransitionPhase`

An indication of which the current stage of a transition.

`struct AsymmetricTransition`

A composite `Transition` that uses a different transition for insertion versus
removal.

`struct AnyTransition`

A type-erased transition.

`var contentTransition: ContentTransition`

The current method of animating the contents of views.

`var contentTransitionAddsDrawingGroup: Bool`

A Boolean value that controls whether views that render content transitions
use GPU-accelerated rendering.

`struct ContentTransition`

A kind of transition that applies to the content within a single view, rather
than to the insertion or removal of a view.

`struct PlaceholderContentView`

A placeholder used to construct an inline modifier, transition, or other
helper type.

Instance Method

# transition(_:)

Associates a transition with the view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func transition<T>(_ transition: T) -> some View where T : Transition
    

## Discussion

When this view appears or disappears, the transition will be applied to it,
allowing for animating it in and out.

The following code will conditionally show MyView, and when it appears or
disappears, will use a custom RotatingFadeTransition transition to show it.

## See Also

### Defining transitions

`func transition(AnyTransition) -> some View`

Associates a transition with the view.

`protocol Transition`

A description of view changes to apply when a view is added to and removed
from the view hierarchy.

`struct TransitionProperties`

The properties a `Transition` can have.

`enum TransitionPhase`

An indication of which the current stage of a transition.

`struct AsymmetricTransition`

A composite `Transition` that uses a different transition for insertion versus
removal.

`struct AnyTransition`

A type-erased transition.

`func contentTransition(ContentTransition) -> some View`

Modifies the view to use a given transition as its method of animating changes
to the contents of its views.

`var contentTransition: ContentTransition`

The current method of animating the contents of views.

`var contentTransitionAddsDrawingGroup: Bool`

A Boolean value that controls whether views that render content transitions
use GPU-accelerated rendering.

`struct ContentTransition`

A kind of transition that applies to the content within a single view, rather
than to the insertion or removal of a view.

`struct PlaceholderContentView`

A placeholder used to construct an inline modifier, transition, or other
helper type.

Instance Method

# transition(_:)

Associates a transition with the view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func transition(_ t: AnyTransition) -> some View
    

## Discussion

When this view appears or disappears, the transition will be applied to it,
allowing for animating it in and out.

The following code will conditionally show MyView, and when it appears or
disappears, will use a slide transition to show it.

## See Also

### Defining transitions

`func transition<T>(T) -> some View`

Associates a transition with the view.

`protocol Transition`

A description of view changes to apply when a view is added to and removed
from the view hierarchy.

`struct TransitionProperties`

The properties a `Transition` can have.

`enum TransitionPhase`

An indication of which the current stage of a transition.

`struct AsymmetricTransition`

A composite `Transition` that uses a different transition for insertion versus
removal.

`struct AnyTransition`

A type-erased transition.

`func contentTransition(ContentTransition) -> some View`

Modifies the view to use a given transition as its method of animating changes
to the contents of its views.

`var contentTransition: ContentTransition`

The current method of animating the contents of views.

`var contentTransitionAddsDrawingGroup: Bool`

A Boolean value that controls whether views that render content transitions
use GPU-accelerated rendering.

`struct ContentTransition`

A kind of transition that applies to the content within a single view, rather
than to the insertion or removal of a view.

`struct PlaceholderContentView`

A placeholder used to construct an inline modifier, transition, or other
helper type.

Instance Method

# transaction(_:)

Applies the given transaction mutation function to all animations used within
the view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func transaction(_ transform: @escaping (inout Transaction) -> Void) -> some View
    

##  Parameters

`transform`

    

The transformation to apply to transactions within this view.

## Return Value

A view that wraps this view and applies a transformation to all transactions
used within the view.

## Discussion

Use this modifier to change or replace the animation used in a view. Consider
three identical animations controlled by a button that executes all three
animations simultaneously:

  * The first animation rotates the “Rotation” `Text` view by 360 degrees.

  * The second uses the `transaction(_:)` modifier to change the animation by adding a delay to the start of the animation by two seconds and then increases the rotational speed of the “Rotation\nModified” `Text` view animation by a factor of 2.

  * The third animation uses the `transaction(_:)` modifier to replace the rotation animation affecting the “Animation\nReplaced” `Text` view with a spring animation.

The following code implements these animations:

Use this modifier on leaf views such as `Image` or `Button` rather than
container views such as `VStack` or `HStack`. The transformation applies to
all child views within this view; calling `transaction(_:)` on a container
view can lead to unbounded scope of execution depending on the depth of the
view hierarchy.

## See Also

### Moving an animation to another view

`func withTransaction<Result>(Transaction, () throws -> Result) rethrows ->
Result`

Executes a closure with the specified transaction and returns the result.

`func withTransaction<R, V>(WritableKeyPath<Transaction, V>, V, () throws ->
R) rethrows -> R`

Executes a closure with the specified transaction key path and value and
returns the result.

`func transaction(value: some Equatable, (inout Transaction) -> Void) -> some
View`

Applies the given transaction mutation function to all animations used within
the view.

`func transaction<V>((inout Transaction) -> Void, body:
(PlaceholderContentView<Self>) -> V) -> some View`

Applies the given transaction mutation function to all animations used within
the `body` closure.

`struct Transaction`

The context of the current state-processing update.

`protocol TransactionKey`

A key for accessing values in a transaction.

Instance Method

# transaction(value:_:)

Applies the given transaction mutation function to all animations used within
the view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func transaction(
        value: some Equatable,
        _ transform: @escaping (inout Transaction) -> Void
    ) -> some View
    

##  Parameters

`value`

    

A value to monitor for changes.

`transform`

    

The transformation to apply to transactions within this view.

## Return Value

A view that wraps this view and applies a transformation to all transactions
used within the view whenever `value` changes.

## Discussion

Use this modifier to change or replace the animation used in a view. Consider
three identical views controlled by a button that changes all three
simultaneously:

  * The first view animates rotating the “Rotation” `Text` view by 360 degrees.

  * The second uses the `transaction(_:)` modifier to change the animation by adding a delay to the start of the animation by two seconds and then increases the rotational speed of the “Rotation\nModified” `Text` view animation by a factor of 2.

  * The third uses the `transaction(_:)` modifier to disable animations affecting the “Animation\nReplaced” `Text` view.

The following code implements these animations:

## See Also

### Moving an animation to another view

`func withTransaction<Result>(Transaction, () throws -> Result) rethrows ->
Result`

Executes a closure with the specified transaction and returns the result.

`func withTransaction<R, V>(WritableKeyPath<Transaction, V>, V, () throws ->
R) rethrows -> R`

Executes a closure with the specified transaction key path and value and
returns the result.

`func transaction((inout Transaction) -> Void) -> some View`

Applies the given transaction mutation function to all animations used within
the view.

`func transaction<V>((inout Transaction) -> Void, body:
(PlaceholderContentView<Self>) -> V) -> some View`

Applies the given transaction mutation function to all animations used within
the `body` closure.

`struct Transaction`

The context of the current state-processing update.

`protocol TransactionKey`

A key for accessing values in a transaction.

Instance Method

# transaction(_:body:)

Applies the given transaction mutation function to all animations used within
the `body` closure.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func transaction<V>(
        _ transform: @escaping (inout Transaction) -> Void,
        @ViewBuilder body: (PlaceholderContentView<Self>) -> V
    ) -> some View where V : View
    

## Discussion

Any modifiers applied to the content of `body` will be applied to this view,
and the changes to the transaction performed in the `transform` will only
affect the modifiers defined in the `body`.

The following code animates the opacity changing with a faster animation,
while the contents of MyView are animated with the implicit transaction:

  * See Also: `Transaction.disablesAnimations`

## See Also

### Moving an animation to another view

`func withTransaction<Result>(Transaction, () throws -> Result) rethrows ->
Result`

Executes a closure with the specified transaction and returns the result.

`func withTransaction<R, V>(WritableKeyPath<Transaction, V>, V, () throws ->
R) rethrows -> R`

Executes a closure with the specified transaction key path and value and
returns the result.

`func transaction((inout Transaction) -> Void) -> some View`

Applies the given transaction mutation function to all animations used within
the view.

`func transaction(value: some Equatable, (inout Transaction) -> Void) -> some
View`

Applies the given transaction mutation function to all animations used within
the view.

`struct Transaction`

The context of the current state-processing update.

`protocol TransactionKey`

A key for accessing values in a transaction.

Instance Method

# contentTransition(_:)

Modifies the view to use a given transition as its method of animating changes
to the contents of its views.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func contentTransition(_ transition: ContentTransition) -> some View
    

##  Parameters

`transition`

    

The transition to apply when animating the content change.

## Discussion

This modifier allows you to perform a transition that animates a change within
a single view. The provided `ContentTransition` can present an opacity
animation for content changes, an interpolated animation of the content’s
paths as they change, or perform no animation at all.

Tip

The `contentTransition(_:)` modifier only has an effect within the context of
an `Animation`.

In the following example, a `Button` changes the color and font size of a
`Text` view. Since both of these properties apply to the paths of the text,
the `interpolate` transition can animate a gradual change to these properties
through the entire transition. By contrast, the `opacity` transition would
simply fade between the start and end states.

This example uses an ease-in–ease-out animation with a five-second duration to
make it easier to see the effect of the interpolation. The figure below shows
the `Text` at the beginning of the animation, halfway through, and at the end.

Time| Display  
---|---  
Start|  
Middle|  
End|  
  
To control whether content transitions use GPU-accelerated rendering, set the
value of the `contentTransitionAddsDrawingGroup` environment variable.

## See Also

### Defining transitions

`func transition<T>(T) -> some View`

Associates a transition with the view.

`func transition(AnyTransition) -> some View`

Associates a transition with the view.

`protocol Transition`

A description of view changes to apply when a view is added to and removed
from the view hierarchy.

`struct TransitionProperties`

The properties a `Transition` can have.

`enum TransitionPhase`

An indication of which the current stage of a transition.

`struct AsymmetricTransition`

A composite `Transition` that uses a different transition for insertion versus
removal.

`struct AnyTransition`

A type-erased transition.

`var contentTransition: ContentTransition`

The current method of animating the contents of views.

`var contentTransitionAddsDrawingGroup: Bool`

A Boolean value that controls whether views that render content transitions
use GPU-accelerated rendering.

`struct ContentTransition`

A kind of transition that applies to the content within a single view, rather
than to the insertion or removal of a view.

`struct PlaceholderContentView`

A placeholder used to construct an inline modifier, transition, or other
helper type.

Instance Method

# matchedGeometryEffect(id:in:properties:anchor:isSource:)

Defines a group of views with synchronized geometry using an identifier and
namespace that you provide.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func matchedGeometryEffect<ID>(
        id: ID,
        in namespace: Namespace.ID,
        properties: MatchedGeometryProperties = .frame,
        anchor: UnitPoint = .center,
        isSource: Bool = true
    ) -> some View where ID : Hashable
    

##  Parameters

`id`

    

The identifier, often derived from the identifier of the data being displayed
by the view.

`namespace`

    

The namespace in which defines the `id`. New namespaces are created by adding
an `@Namespace` variable to a `View` type and reading its value in the view’s
body method.

`properties`

    

The properties to copy from the source view.

`anchor`

    

The relative location in the view used to produce its shared position value.

`isSource`

    

True if the view should be used as the source of geometry for other views in
the group.

## Return Value

A new view that defines an entry in the global database of views synchronizing
their geometry.

## Discussion

This method sets the geometry of each view in the group from the inserted view
with `isSource = true` (known as the “source” view), updating the values
marked by `properties`.

If inserting a view in the same transaction that another view with the same
key is removed, the system will interpolate their frame rectangles in window
space to make it appear that there is a single view moving from its old
position to its new position. The usual transition mechanisms define how each
of the two views is rendered during the transition (e.g. fade in/out, scale,
etc), the `matchedGeometryEffect()` modifier only arranges for the geometry of
the views to be linked, not their rendering.

If the number of currently-inserted views in the group with `isSource = true`
is not exactly one results are undefined, due to it not being clear which is
the source view.

## See Also

### Synchronizing geometries

`struct MatchedGeometryProperties`

A set of view properties that may be synchronized between views using the
`View.matchedGeometryEffect()` function.

`protocol GeometryEffect`

An effect that changes the visual appearance of a view, largely without
changing its ancestors or descendants.

`struct Namespace`

A dynamic property type that allows access to a namespace defined by the
persistent identity of the object containing the property (e.g. a view).

`func geometryGroup() -> some View`

Isolates the geometry (e.g. position and size) of the view from its parent
view.

Instance Method

# geometryGroup()

Isolates the geometry (e.g. position and size) of the view from its parent
view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func geometryGroup() -> some View
    

## Discussion

By default SwiftUI views push position and size changes down through the view
hierarchy, so that only views that draw something (known as leaf views) apply
the current animation to their frame rectangle. However in some cases this
coalescing behavior can give undesirable results; inserting a geometry group
can correct that. A group acts as a barrier between the parent view and its
subviews, forcing the position and size values to be resolved and animated by
the parent, before being passed down to each subview.

The example below shows one use of this function: ensuring that the member
views of each row in the stack apply (and animate as) a single geometric
transform from their ancestor view, rather than letting the effects of the
ancestor views be applied separately to each leaf view. If the members of
`ItemView` may be added and removed at different times the group ensures that
they stay locked together as animations are applied.

Returns: a new view whose geometry is isolated from that of its parent view.

## See Also

### Synchronizing geometries

`func matchedGeometryEffect<ID>(id: ID, in: Namespace.ID, properties:
MatchedGeometryProperties, anchor: UnitPoint, isSource: Bool) -> some View`

Defines a group of views with synchronized geometry using an identifier and
namespace that you provide.

`struct MatchedGeometryProperties`

A set of view properties that may be synchronized between views using the
`View.matchedGeometryEffect()` function.

`protocol GeometryEffect`

An effect that changes the visual appearance of a view, largely without
changing its ancestors or descendants.

`struct Namespace`

A dynamic property type that allows access to a namespace defined by the
persistent identity of the object containing the property (e.g. a view).

