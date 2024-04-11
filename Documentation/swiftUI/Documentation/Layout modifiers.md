Instance Method

# frame(width:height:alignment:)

Positions this view within an invisible frame with the specified size.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func frame(
        width: CGFloat? = nil,
        height: CGFloat? = nil,
        alignment: Alignment = .center
    ) -> some View
    

##  Parameters

`width`

    

A fixed width for the resulting view. If `width` is `nil`, the resulting view
assumes this view’s sizing behavior.

`height`

    

A fixed height for the resulting view. If `height` is `nil`, the resulting
view assumes this view’s sizing behavior.

`alignment`

    

The alignment of this view inside the resulting frame. Note that most
alignment values have no apparent effect when the size of the frame happens to
match that of this view.

## Return Value

A view with fixed dimensions of `width` and `height`, for the parameters that
are non-`nil`.

## Discussion

Use this method to specify a fixed size for a view’s width, height, or both.
If you only specify one of the dimensions, the resulting view assumes this
view’s sizing behavior in the other dimension.

For example, the following code lays out an ellipse in a fixed 200 by 100
frame. Because a shape always occupies the space offered to it by the layout
system, the first ellipse is 200x100 points. The second ellipse is laid out in
a frame with only a fixed height, so it occupies that height, and whatever
width the layout system offers to its parent.

`The alignment` parameter specifies this view’s alignment within the frame.

In the example above, the text is positioned at the top, leading corner of the
frame. If the text is taller than the frame, its bounds may extend beyond the
bottom of the frame’s bounds.

## See Also

### Influencing a view’s size

`func frame(depth: CGFloat?, alignment: DepthAlignment) -> some View`

Positions this view within an invisible frame with the specified depth.

`func frame(minWidth: CGFloat?, idealWidth: CGFloat?, maxWidth: CGFloat?,
minHeight: CGFloat?, idealHeight: CGFloat?, maxHeight: CGFloat?, alignment:
Alignment) -> some View`

Positions this view within an invisible frame having the specified size
constraints.

`func frame(minDepth: CGFloat?, idealDepth: CGFloat?, maxDepth: CGFloat?,
alignment: DepthAlignment) -> some View`

Positions this view within an invisible frame having the specified depth
constraints.

`func containerRelativeFrame(Axis.Set, alignment: Alignment) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func containerRelativeFrame(Axis.Set, alignment: Alignment, (CGFloat, Axis)
-> CGFloat) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func containerRelativeFrame(Axis.Set, count: Int, span: Int, spacing:
CGFloat, alignment: Alignment) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func fixedSize() -> some View`

Fixes this view at its ideal size.

`func fixedSize(horizontal: Bool, vertical: Bool) -> some View`

Fixes this view at its ideal size in the specified dimensions.

`func layoutPriority(Double) -> some View`

Sets the priority by which a parent layout should apportion space to this
child.

Instance Method

# frame(depth:alignment:)

Positions this view within an invisible frame with the specified depth.

visionOS 1.0+

    
    
    func frame(
        depth: CGFloat?,
        alignment: DepthAlignment = .center
    ) -> some View
    

##  Parameters

`depth`

    

A fixed depth for the resulting view. If `depth` is `nil`, the resulting view
assumes this view’s sizing behavior.

`alignment`

    

The alignment of this view inside the resulting view. `alignment` applies if
this view is smaller than the size given by the resulting frame.

## Return Value

A view with a fixed dimension of `depth` if non-`nil`.

## Discussion

Use this method to specify a fixed size for a view’s depth. If you don’t
specify a dimension, the resulting view assumes this view’s sizing behavior in
depth.

## See Also

### Influencing a view’s size

`func frame(width: CGFloat?, height: CGFloat?, alignment: Alignment) -> some
View`

Positions this view within an invisible frame with the specified size.

`func frame(minWidth: CGFloat?, idealWidth: CGFloat?, maxWidth: CGFloat?,
minHeight: CGFloat?, idealHeight: CGFloat?, maxHeight: CGFloat?, alignment:
Alignment) -> some View`

Positions this view within an invisible frame having the specified size
constraints.

`func frame(minDepth: CGFloat?, idealDepth: CGFloat?, maxDepth: CGFloat?,
alignment: DepthAlignment) -> some View`

Positions this view within an invisible frame having the specified depth
constraints.

`func containerRelativeFrame(Axis.Set, alignment: Alignment) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func containerRelativeFrame(Axis.Set, alignment: Alignment, (CGFloat, Axis)
-> CGFloat) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func containerRelativeFrame(Axis.Set, count: Int, span: Int, spacing:
CGFloat, alignment: Alignment) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func fixedSize() -> some View`

Fixes this view at its ideal size.

`func fixedSize(horizontal: Bool, vertical: Bool) -> some View`

Fixes this view at its ideal size in the specified dimensions.

`func layoutPriority(Double) -> some View`

Sets the priority by which a parent layout should apportion space to this
child.

Instance Method

#
frame(minWidth:idealWidth:maxWidth:minHeight:idealHeight:maxHeight:alignment:)

Positions this view within an invisible frame having the specified size
constraints.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func frame(
        minWidth: CGFloat? = nil,
        idealWidth: CGFloat? = nil,
        maxWidth: CGFloat? = nil,
        minHeight: CGFloat? = nil,
        idealHeight: CGFloat? = nil,
        maxHeight: CGFloat? = nil,
        alignment: Alignment = .center
    ) -> some View
    

##  Parameters

`minWidth`

    

The minimum width of the resulting frame.

`idealWidth`

    

The ideal width of the resulting frame.

`maxWidth`

    

The maximum width of the resulting frame.

`minHeight`

    

The minimum height of the resulting frame.

`idealHeight`

    

The ideal height of the resulting frame.

`maxHeight`

    

The maximum height of the resulting frame.

`alignment`

    

The alignment of this view inside the resulting frame. Note that most
alignment values have no apparent effect when the size of the frame happens to
match that of this view.

## Return Value

A view with flexible dimensions given by the call’s non-`nil` parameters.

## Discussion

Always specify at least one size characteristic when calling this method. Pass
`nil` or leave out a characteristic to indicate that the frame should adopt
this view’s sizing behavior, constrained by the other non-`nil` arguments.

The size proposed to this view is the size proposed to the frame, limited by
any constraints specified, and with any ideal dimensions specified replacing
any corresponding unspecified dimensions in the proposal.

If no minimum or maximum constraint is specified in a given dimension, the
frame adopts the sizing behavior of its child in that dimension. If both
constraints are specified in a dimension, the frame unconditionally adopts the
size proposed for it, clamped to the constraints. Otherwise, the size of the
frame in either dimension is:

  * If a minimum constraint is specified and the size proposed for the frame by the parent is less than the size of this view, the proposed size, clamped to that minimum.

  * If a maximum constraint is specified and the size proposed for the frame by the parent is greater than the size of this view, the proposed size, clamped to that maximum.

  * Otherwise, the size of this view.

## See Also

### Influencing a view’s size

`func frame(width: CGFloat?, height: CGFloat?, alignment: Alignment) -> some
View`

Positions this view within an invisible frame with the specified size.

`func frame(depth: CGFloat?, alignment: DepthAlignment) -> some View`

Positions this view within an invisible frame with the specified depth.

`func frame(minDepth: CGFloat?, idealDepth: CGFloat?, maxDepth: CGFloat?,
alignment: DepthAlignment) -> some View`

Positions this view within an invisible frame having the specified depth
constraints.

`func containerRelativeFrame(Axis.Set, alignment: Alignment) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func containerRelativeFrame(Axis.Set, alignment: Alignment, (CGFloat, Axis)
-> CGFloat) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func containerRelativeFrame(Axis.Set, count: Int, span: Int, spacing:
CGFloat, alignment: Alignment) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func fixedSize() -> some View`

Fixes this view at its ideal size.

`func fixedSize(horizontal: Bool, vertical: Bool) -> some View`

Fixes this view at its ideal size in the specified dimensions.

`func layoutPriority(Double) -> some View`

Sets the priority by which a parent layout should apportion space to this
child.

Instance Method

# frame(minDepth:idealDepth:maxDepth:alignment:)

Positions this view within an invisible frame having the specified depth
constraints.

visionOS 1.0+

    
    
    func frame(
        minDepth: CGFloat? = nil,
        idealDepth: CGFloat? = nil,
        maxDepth: CGFloat? = nil,
        alignment: DepthAlignment = .center
    ) -> some View
    

##  Parameters

`minDepth`

    

The minimum depth of the resulting frame.

`idealDepth`

    

The ideal depth of the resulting frame.

`maxDepth`

    

The maximum depth of the resulting frame.

`alignment`

    

The alignment of this view inside the resulting frame. Note that most
alignment values have no apparent effect when the size of the frame happens to
match that of this view.

## Return Value

A view with flexible dimensions given by the call’s non-`nil` parameters.

## Discussion

Always specify at least one size characteristic when calling this method. Pass
`nil` or leave out a characteristic to indicate that the frame should adopt
this view’s sizing behavior, constrained by the other non-`nil` arguments.

The size proposed to this view is the size proposed to the frame, limited by
any constraints specified, and with an ideal dimension specified replacing any
corresponding unspecified dimensions in the proposal.

If no minimum or maximum constraint is specified in a given dimension, the
frame adopts the sizing behavior of its child in that dimension. If both
constraints are specified in a dimension, the frame unconditionally adopts the
size proposed for it, clamped to the constraints. Otherwise, the size of the
frame in either dimension is:

  * If a minimum constraint is specified and the size proposed for the frame by the parent is less than the size of this view, the proposed size, clamped to that minimum.

  * If a maximum constraint is specified and the size proposed for the frame by the parent is greater than the size of this view, the proposed size, clamped to that maximum.

  * Otherwise, the size of this view.

## See Also

### Influencing a view’s size

`func frame(width: CGFloat?, height: CGFloat?, alignment: Alignment) -> some
View`

Positions this view within an invisible frame with the specified size.

`func frame(depth: CGFloat?, alignment: DepthAlignment) -> some View`

Positions this view within an invisible frame with the specified depth.

`func frame(minWidth: CGFloat?, idealWidth: CGFloat?, maxWidth: CGFloat?,
minHeight: CGFloat?, idealHeight: CGFloat?, maxHeight: CGFloat?, alignment:
Alignment) -> some View`

Positions this view within an invisible frame having the specified size
constraints.

`func containerRelativeFrame(Axis.Set, alignment: Alignment) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func containerRelativeFrame(Axis.Set, alignment: Alignment, (CGFloat, Axis)
-> CGFloat) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func containerRelativeFrame(Axis.Set, count: Int, span: Int, spacing:
CGFloat, alignment: Alignment) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func fixedSize() -> some View`

Fixes this view at its ideal size.

`func fixedSize(horizontal: Bool, vertical: Bool) -> some View`

Fixes this view at its ideal size in the specified dimensions.

`func layoutPriority(Double) -> some View`

Sets the priority by which a parent layout should apportion space to this
child.

Instance Method

# containerRelativeFrame(_:alignment:)

Positions this view within an invisible frame with a size relative to the
nearest container.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func containerRelativeFrame(
        _ axes: Axis.Set,
        alignment: Alignment = .center
    ) -> some View
    

## Discussion

Use this modifier to specify a size for a view’s width, height, or both that
is dependent on the size of the nearest container. Different things can
represent a “container” including:

  * The window presenting a view on iPadOS or macOS, or the screen of a device on iOS.

  * A column of a NavigationSplitView

  * A NavigationStack

  * A tab of a TabView

  * A scrollable view like ScrollView or List

The size provided to this modifier is the size of a container like the ones
listed above subtracting any safe area insets that might be applied to that
container.

The following example will have each purple rectangle occupy the full size of
the screen on iOS:

Use the `containerRelativeFrame(_:count:span:spacing:alignment:)` modifier to
size a view such that multiple views will be visible in the container. When
using this modifier, the count refers to the total number of rows or columns
that the length of the container size in a particular axis should be divided
into. The span refers to the number of rows or columns that the modified view
should actually occupy. Thus the size of the element can be described like so:

The following example only uses the nearest container size in the horizontal
axis, allowing the vertical axis to be determined using the
`aspectRatio(_:contentMode:)` modifier.

Use the `containerRelativeFrame(_:alignment:_:)` modifier to apply your own
custom logic to adjust the size of the nearest container for your view. The
following example will result in the container frame’s width being divided by
3 and using that value as the width of the purple rectangle.

## See Also

### Influencing a view’s size

`func frame(width: CGFloat?, height: CGFloat?, alignment: Alignment) -> some
View`

Positions this view within an invisible frame with the specified size.

`func frame(depth: CGFloat?, alignment: DepthAlignment) -> some View`

Positions this view within an invisible frame with the specified depth.

`func frame(minWidth: CGFloat?, idealWidth: CGFloat?, maxWidth: CGFloat?,
minHeight: CGFloat?, idealHeight: CGFloat?, maxHeight: CGFloat?, alignment:
Alignment) -> some View`

Positions this view within an invisible frame having the specified size
constraints.

`func frame(minDepth: CGFloat?, idealDepth: CGFloat?, maxDepth: CGFloat?,
alignment: DepthAlignment) -> some View`

Positions this view within an invisible frame having the specified depth
constraints.

`func containerRelativeFrame(Axis.Set, alignment: Alignment, (CGFloat, Axis)
-> CGFloat) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func containerRelativeFrame(Axis.Set, count: Int, span: Int, spacing:
CGFloat, alignment: Alignment) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func fixedSize() -> some View`

Fixes this view at its ideal size.

`func fixedSize(horizontal: Bool, vertical: Bool) -> some View`

Fixes this view at its ideal size in the specified dimensions.

`func layoutPriority(Double) -> some View`

Sets the priority by which a parent layout should apportion space to this
child.

Instance Method

# containerRelativeFrame(_:alignment:_:)

Positions this view within an invisible frame with a size relative to the
nearest container.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func containerRelativeFrame(
        _ axes: Axis.Set,
        alignment: Alignment = .center,
        _ length: @escaping (CGFloat, Axis) -> CGFloat
    ) -> some View
    

## Discussion

Use the `containerRelativeFrame(_:alignment:)` modifier to specify a size for
a view’s width, height, or both that is dependent on the size of the nearest
container. Different things can represent a “container” including:

  * The window presenting a view on iPadOS or macOS, or the screen of a device on iOS.

  * A column of a NavigationSplitView

  * A NavigationStack

  * A tab of a TabView

  * A scrollable view like ScrollView or List

The size provided to this modifier is the size of a container like the ones
listed above subtracting any safe area insets that might be applied to that
container.

The following example will have each purple rectangle occupy the full size of
the screen on iOS:

Use the `View/containerRelativeFrame(_:count:spacing:alignment:)` modifier to
size a view such that multiple views will be visible in the container. When
using this modifier, the count refers to the total number of rows or columns
that the length of the container size in a particular axis should be divided
into. The span refers to the number of rows or columns that the modified view
should actually occupy. Thus the size of the element can be described like so:

The following example only uses the nearest container size in the horizontal
axis, allowing the vertical axis to be determined using the
`aspectRatio(_:contentMode:)` modifier.

Use this modifier to apply your own custom logic to adjust the size of the
nearest container for your view. The following example will result in the
container frame’s width being divided by 3 and using that value as the width
of the purple rectangle.

## See Also

### Influencing a view’s size

`func frame(width: CGFloat?, height: CGFloat?, alignment: Alignment) -> some
View`

Positions this view within an invisible frame with the specified size.

`func frame(depth: CGFloat?, alignment: DepthAlignment) -> some View`

Positions this view within an invisible frame with the specified depth.

`func frame(minWidth: CGFloat?, idealWidth: CGFloat?, maxWidth: CGFloat?,
minHeight: CGFloat?, idealHeight: CGFloat?, maxHeight: CGFloat?, alignment:
Alignment) -> some View`

Positions this view within an invisible frame having the specified size
constraints.

`func frame(minDepth: CGFloat?, idealDepth: CGFloat?, maxDepth: CGFloat?,
alignment: DepthAlignment) -> some View`

Positions this view within an invisible frame having the specified depth
constraints.

`func containerRelativeFrame(Axis.Set, alignment: Alignment) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func containerRelativeFrame(Axis.Set, count: Int, span: Int, spacing:
CGFloat, alignment: Alignment) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func fixedSize() -> some View`

Fixes this view at its ideal size.

`func fixedSize(horizontal: Bool, vertical: Bool) -> some View`

Fixes this view at its ideal size in the specified dimensions.

`func layoutPriority(Double) -> some View`

Sets the priority by which a parent layout should apportion space to this
child.

Instance Method

# containerRelativeFrame(_:count:span:spacing:alignment:)

Positions this view within an invisible frame with a size relative to the
nearest container.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func containerRelativeFrame(
        _ axes: Axis.Set,
        count: Int,
        span: Int = 1,
        spacing: CGFloat,
        alignment: Alignment = .center
    ) -> some View
    

## Discussion

Use the `containerRelativeFrame(_:alignment:)` modifier to specify a size for
a view’s width, height, or both that is dependent on the size of the nearest
container. Different things can represent a “container” including:

  * The window presenting a view on iPadOS or macOS, or the screen of a device on iOS.

  * A column of a NavigationSplitView

  * A NavigationStack

  * A tab of a TabView

  * A scrollable view like ScrollView or List

The size provided to this modifier is the size of a container like the ones
listed above subtracting any safe area insets that might be applied to that
container.

The following example will have each purple rectangle occupy the full size of
the screen on iOS:

Use this modifier to size a view such that multiple views will be visible in
the container. When using this modifier, the count refers to the total number
of rows or columns that the length of the container size in a particular axis
should be divided into. The span refers to the number of rows or columns that
the modified view should actually occupy. Thus the size of the element can be
described like so:

The following example only uses the nearest container size in the horizontal
axis, allowing the vertical axis to be determined using the
`aspectRatio(_:contentMode:)` modifier.

Use the `containerRelativeFrame(_:alignment:_:)` modifier to apply your own
custom logic to adjust the size of the nearest container for your view. The
following example will result in the container frame’s width being divided by
3 and using that value as the width of the purple rectangle.

## See Also

### Influencing a view’s size

`func frame(width: CGFloat?, height: CGFloat?, alignment: Alignment) -> some
View`

Positions this view within an invisible frame with the specified size.

`func frame(depth: CGFloat?, alignment: DepthAlignment) -> some View`

Positions this view within an invisible frame with the specified depth.

`func frame(minWidth: CGFloat?, idealWidth: CGFloat?, maxWidth: CGFloat?,
minHeight: CGFloat?, idealHeight: CGFloat?, maxHeight: CGFloat?, alignment:
Alignment) -> some View`

Positions this view within an invisible frame having the specified size
constraints.

`func frame(minDepth: CGFloat?, idealDepth: CGFloat?, maxDepth: CGFloat?,
alignment: DepthAlignment) -> some View`

Positions this view within an invisible frame having the specified depth
constraints.

`func containerRelativeFrame(Axis.Set, alignment: Alignment) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func containerRelativeFrame(Axis.Set, alignment: Alignment, (CGFloat, Axis)
-> CGFloat) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func fixedSize() -> some View`

Fixes this view at its ideal size.

`func fixedSize(horizontal: Bool, vertical: Bool) -> some View`

Fixes this view at its ideal size in the specified dimensions.

`func layoutPriority(Double) -> some View`

Sets the priority by which a parent layout should apportion space to this
child.

Instance Method

# fixedSize()

Fixes this view at its ideal size.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func fixedSize() -> some View
    

## Return Value

A view that fixes this view at its ideal size.

## Discussion

During the layout of the view hierarchy, each view proposes a size to each
child view it contains. If the child view doesn’t need a fixed size it can
accept and conform to the size offered by the parent.

For example, a `Text` view placed in an explicitly sized frame wraps and
truncates its string to remain within its parent’s bounds:

The `fixedSize()` modifier can be used to create a view that maintains the
_ideal size_ of its children both dimensions:

This can result in the view exceeding the parent’s bounds, which may or may
not be the effect you want.

You can think of `fixedSize()` as the creation of a _counter proposal_ to the
view size proposed to a view by its parent. The ideal size of a view, and the
specific effects of `fixedSize()` depends on the particular view and how you
have configured it.

To create a view that fixes the view’s size in either the horizontal or
vertical dimensions, see `fixedSize(horizontal:vertical:)`.

## See Also

### Influencing a view’s size

`func frame(width: CGFloat?, height: CGFloat?, alignment: Alignment) -> some
View`

Positions this view within an invisible frame with the specified size.

`func frame(depth: CGFloat?, alignment: DepthAlignment) -> some View`

Positions this view within an invisible frame with the specified depth.

`func frame(minWidth: CGFloat?, idealWidth: CGFloat?, maxWidth: CGFloat?,
minHeight: CGFloat?, idealHeight: CGFloat?, maxHeight: CGFloat?, alignment:
Alignment) -> some View`

Positions this view within an invisible frame having the specified size
constraints.

`func frame(minDepth: CGFloat?, idealDepth: CGFloat?, maxDepth: CGFloat?,
alignment: DepthAlignment) -> some View`

Positions this view within an invisible frame having the specified depth
constraints.

`func containerRelativeFrame(Axis.Set, alignment: Alignment) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func containerRelativeFrame(Axis.Set, alignment: Alignment, (CGFloat, Axis)
-> CGFloat) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func containerRelativeFrame(Axis.Set, count: Int, span: Int, spacing:
CGFloat, alignment: Alignment) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func fixedSize(horizontal: Bool, vertical: Bool) -> some View`

Fixes this view at its ideal size in the specified dimensions.

`func layoutPriority(Double) -> some View`

Sets the priority by which a parent layout should apportion space to this
child.

Instance Method

# fixedSize(horizontal:vertical:)

Fixes this view at its ideal size in the specified dimensions.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func fixedSize(
        horizontal: Bool,
        vertical: Bool
    ) -> some View
    

##  Parameters

`horizontal`

    

A Boolean value that indicates whether to fix the width of the view.

`vertical`

    

A Boolean value that indicates whether to fix the height of the view.

## Return Value

A view that fixes this view at its ideal size in the dimensions specified by
`horizontal` and `vertical`.

## Discussion

This function behaves like `fixedSize()`, except with
`fixedSize(horizontal:vertical:)` the fixing of the axes can be optionally
specified in one or both dimensions. For example, if you horizontally fix a
text view before wrapping it in the frame view, you’re telling the text view
to maintain its ideal _width_. The view calculates this to be the space needed
to represent the entire string.

This can result in the view exceeding the parent’s bounds, which may or may
not be the effect you want.

## See Also

### Influencing a view’s size

`func frame(width: CGFloat?, height: CGFloat?, alignment: Alignment) -> some
View`

Positions this view within an invisible frame with the specified size.

`func frame(depth: CGFloat?, alignment: DepthAlignment) -> some View`

Positions this view within an invisible frame with the specified depth.

`func frame(minWidth: CGFloat?, idealWidth: CGFloat?, maxWidth: CGFloat?,
minHeight: CGFloat?, idealHeight: CGFloat?, maxHeight: CGFloat?, alignment:
Alignment) -> some View`

Positions this view within an invisible frame having the specified size
constraints.

`func frame(minDepth: CGFloat?, idealDepth: CGFloat?, maxDepth: CGFloat?,
alignment: DepthAlignment) -> some View`

Positions this view within an invisible frame having the specified depth
constraints.

`func containerRelativeFrame(Axis.Set, alignment: Alignment) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func containerRelativeFrame(Axis.Set, alignment: Alignment, (CGFloat, Axis)
-> CGFloat) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func containerRelativeFrame(Axis.Set, count: Int, span: Int, spacing:
CGFloat, alignment: Alignment) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func fixedSize() -> some View`

Fixes this view at its ideal size.

`func layoutPriority(Double) -> some View`

Sets the priority by which a parent layout should apportion space to this
child.

Instance Method

# layoutPriority(_:)

Sets the priority by which a parent layout should apportion space to this
child.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func layoutPriority(_ value: Double) -> some View
    

##  Parameters

`value`

    

The priority by which a parent layout apportions space to the child.

## Discussion

Views typically have a default priority of `0` which causes space to be
apportioned evenly to all sibling views. Raising a view’s layout priority
encourages the higher priority view to shrink later when the group is shrunk
and stretch sooner when the group is stretched.

In the example above, the first `Text` element has the default priority `0`
which causes its view to shrink dramatically due to the higher priority of the
second `Text` element, even though all of their other attributes (font, font
size and character count) are the same.

A parent layout offers the child views with the highest layout priority all
the space offered to the parent minus the minimum space required for all its
lower-priority children.

## See Also

### Influencing a view’s size

`func frame(width: CGFloat?, height: CGFloat?, alignment: Alignment) -> some
View`

Positions this view within an invisible frame with the specified size.

`func frame(depth: CGFloat?, alignment: DepthAlignment) -> some View`

Positions this view within an invisible frame with the specified depth.

`func frame(minWidth: CGFloat?, idealWidth: CGFloat?, maxWidth: CGFloat?,
minHeight: CGFloat?, idealHeight: CGFloat?, maxHeight: CGFloat?, alignment:
Alignment) -> some View`

Positions this view within an invisible frame having the specified size
constraints.

`func frame(minDepth: CGFloat?, idealDepth: CGFloat?, maxDepth: CGFloat?,
alignment: DepthAlignment) -> some View`

Positions this view within an invisible frame having the specified depth
constraints.

`func containerRelativeFrame(Axis.Set, alignment: Alignment) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func containerRelativeFrame(Axis.Set, alignment: Alignment, (CGFloat, Axis)
-> CGFloat) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func containerRelativeFrame(Axis.Set, count: Int, span: Int, spacing:
CGFloat, alignment: Alignment) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func fixedSize() -> some View`

Fixes this view at its ideal size.

`func fixedSize(horizontal: Bool, vertical: Bool) -> some View`

Fixes this view at its ideal size in the specified dimensions.

Instance Method

# position(_:)

Positions the center of this view at the specified point in its parent’s
coordinate space.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func position(_ position: CGPoint) -> some View
    

##  Parameters

`position`

    

The point at which to place the center of this view.

## Return Value

A view that fixes the center of this view at `position`.

## Discussion

Use the `position(_:)` modifier to place the center of a view at a specific
coordinate in the parent view using a `CGPoint` to specify the `x` and `y`
offset.

## See Also

### Adjusting a view’s position

Making fine adjustments to a view’s position

Shift the position of a view by applying the offset or position modifier.

`func position(x: CGFloat, y: CGFloat) -> some View`

Positions the center of this view at the specified coordinates in its parent’s
coordinate space.

`func offset(CGSize) -> some View`

Offset this view by the horizontal and vertical amount specified in the offset
parameter.

`func offset(x: CGFloat, y: CGFloat) -> some View`

Offset this view by the specified horizontal and vertical distances.

`func offset(z: CGFloat) -> some View`

Brings a view forward in Z by the provided distance in points.

Instance Method

# position(x:y:)

Positions the center of this view at the specified coordinates in its parent’s
coordinate space.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func position(
        x: CGFloat = 0,
        y: CGFloat = 0
    ) -> some View
    

##  Parameters

`x`

    

The x-coordinate at which to place the center of this view.

`y`

    

The y-coordinate at which to place the center of this view.

## Return Value

A view that fixes the center of this view at `x` and `y`.

## Discussion

Use the `position(x:y:)` modifier to place the center of a view at a specific
coordinate in the parent view using an `x` and `y` offset.

## See Also

### Adjusting a view’s position

Making fine adjustments to a view’s position

Shift the position of a view by applying the offset or position modifier.

`func position(CGPoint) -> some View`

Positions the center of this view at the specified point in its parent’s
coordinate space.

`func offset(CGSize) -> some View`

Offset this view by the horizontal and vertical amount specified in the offset
parameter.

`func offset(x: CGFloat, y: CGFloat) -> some View`

Offset this view by the specified horizontal and vertical distances.

`func offset(z: CGFloat) -> some View`

Brings a view forward in Z by the provided distance in points.

Instance Method

# offset(_:)

Offset this view by the horizontal and vertical amount specified in the offset
parameter.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func offset(_ offset: CGSize) -> some View
    

##  Parameters

`offset`

    

The distance to offset this view.

## Return Value

A view that offsets this view by `offset`.

## Discussion

Use `offset(_:)` to shift the displayed contents by the amount specified in
the `offset` parameter.

The original dimensions of the view aren’t changed by offsetting the contents;
in the example below the gray border drawn by this view surrounds the original
position of the text:

## See Also

### Adjusting a view’s position

Making fine adjustments to a view’s position

Shift the position of a view by applying the offset or position modifier.

`func position(CGPoint) -> some View`

Positions the center of this view at the specified point in its parent’s
coordinate space.

`func position(x: CGFloat, y: CGFloat) -> some View`

Positions the center of this view at the specified coordinates in its parent’s
coordinate space.

`func offset(x: CGFloat, y: CGFloat) -> some View`

Offset this view by the specified horizontal and vertical distances.

`func offset(z: CGFloat) -> some View`

Brings a view forward in Z by the provided distance in points.

Instance Method

# offset(x:y:)

Offset this view by the specified horizontal and vertical distances.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func offset(
        x: CGFloat = 0,
        y: CGFloat = 0
    ) -> some View
    

##  Parameters

`x`

    

The horizontal distance to offset this view.

`y`

    

The vertical distance to offset this view.

## Return Value

A view that offsets this view by `x` and `y`.

## Discussion

Use `offset(x:y:)` to shift the displayed contents by the amount specified in
the `x` and `y` parameters.

The original dimensions of the view aren’t changed by offsetting the contents;
in the example below the gray border drawn by this view surrounds the original
position of the text:

## See Also

### Adjusting a view’s position

Making fine adjustments to a view’s position

Shift the position of a view by applying the offset or position modifier.

`func position(CGPoint) -> some View`

Positions the center of this view at the specified point in its parent’s
coordinate space.

`func position(x: CGFloat, y: CGFloat) -> some View`

Positions the center of this view at the specified coordinates in its parent’s
coordinate space.

`func offset(CGSize) -> some View`

Offset this view by the horizontal and vertical amount specified in the offset
parameter.

`func offset(z: CGFloat) -> some View`

Brings a view forward in Z by the provided distance in points.

Instance Method

# offset(z:)

Brings a view forward in Z by the provided distance in points.

visionOS 1.0+

    
    
    func offset(z: CGFloat) -> some View
    

##  Parameters

`distance`

    

The distance to extrude the view forward in Z, in points.

## Return Value

A view that is extruded forward in Z by `distance`.

## See Also

### Adjusting a view’s position

Making fine adjustments to a view’s position

Shift the position of a view by applying the offset or position modifier.

`func position(CGPoint) -> some View`

Positions the center of this view at the specified point in its parent’s
coordinate space.

`func position(x: CGFloat, y: CGFloat) -> some View`

Positions the center of this view at the specified coordinates in its parent’s
coordinate space.

`func offset(CGSize) -> some View`

Offset this view by the horizontal and vertical amount specified in the offset
parameter.

`func offset(x: CGFloat, y: CGFloat) -> some View`

Offset this view by the specified horizontal and vertical distances.

Instance Method

# coordinateSpace(_:)

Assigns a name to the view’s coordinate space, so other code can operate on
dimensions like points and sizes relative to the named space.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func coordinateSpace(_ name: NamedCoordinateSpace) -> some View
    

##  Parameters

`name`

    

A name used to identify this coordinate space.

## Discussion

Use `coordinateSpace(_:)` to allow another function to find and operate on a
view and operate on dimensions relative to that view.

The example below demonstrates how a nested view can find and operate on its
enclosing view’s coordinate space:

Here, the `VStack` in the `ContentView` named “stack” is composed of a red
frame with a custom `Circle` view `overlay(_:alignment:)` at its center.

The `circle` view has an attached `DragGesture` that targets the enclosing
VStack’s coordinate space. As the gesture recognizer’s closure registers
events inside `circle` it stores them in the shared `location` state variable
and the `VStack` displays the coordinates in a `Text` view.

## See Also

### Measuring a view

`struct GeometryReader`

A container view that defines its content as a function of its own size and
coordinate space.

`struct GeometryReader3D`

A container view that defines its content as a function of its own size and
coordinate space.

`struct GeometryProxy`

A proxy for access to the size and coordinate space (for anchor resolution) of
the container view.

`struct GeometryProxy3D`

A proxy for access to the size and coordinate space of the container view.

`enum CoordinateSpace`

A resolved coordinate space created by the coordinate space protocol.

`protocol CoordinateSpaceProtocol`

A frame of reference within the layout system.

`struct PhysicalMetric`

Provides access to a value in points that corresponds to the specified
physical measurement.

`struct PhysicalMetricsConverter`

A physical metrics converter provides conversion between point values and
their extent in 3D space, in the form of physical length measurements.

Instance Method

# alignmentGuide(_:computeValue:)

Sets the view’s horizontal alignment.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func alignmentGuide(
        _ g: HorizontalAlignment,
        computeValue: @escaping (ViewDimensions) -> CGFloat
    ) -> some View
    

##  Parameters

`g`

    

A `HorizontalAlignment` value at which to base the offset.

`computeValue`

    

A closure that returns the offset value to apply to this view.

## Return Value

A view modified with respect to its horizontal alignment according to the
computation performed in the method’s closure.

## Discussion

Use `alignmentGuide(_:computeValue:)` to calculate specific offsets to
reposition views in relationship to one another. You can return a constant or
can use the `ViewDimensions` argument to the closure to calculate a return
value.

In the example below, the `HStack` is offset by a constant of 50 points to the
right of center:

Changing the alignment of one view may have effects on surrounding views. Here
the offset values inside a stack and its contained views is the difference of
their absolute offsets.

## See Also

### Aligning views

Aligning views within a stack

Position views inside a stack using alignment guides.

Aligning views across stacks

Create a custom alignment and use it to align views across multiple stacks.

`func alignmentGuide(VerticalAlignment, computeValue: (ViewDimensions) ->
CGFloat) -> some View`

Sets the view’s vertical alignment.

`struct Alignment`

An alignment in both axes.

`struct HorizontalAlignment`

An alignment position along the horizontal axis.

`struct VerticalAlignment`

An alignment position along the vertical axis.

`struct DepthAlignment`

An alignment position along the depth axis.

`protocol AlignmentID`

A type that you use to create custom alignment guides.

`struct ViewDimensions`

A view’s size and alignment guides in its own coordinate space.

Instance Method

# alignmentGuide(_:computeValue:)

Sets the view’s vertical alignment.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func alignmentGuide(
        _ g: VerticalAlignment,
        computeValue: @escaping (ViewDimensions) -> CGFloat
    ) -> some View
    

##  Parameters

`g`

    

A `VerticalAlignment` value at which to base the offset.

`computeValue`

    

A closure that returns the offset value to apply to this view.

## Return Value

A view modified with respect to its vertical alignment according to the
computation performed in the method’s closure.

## Discussion

Use `alignmentGuide(_:computeValue:)` to calculate specific offsets to
reposition views in relationship to one another. You can return a constant or
can use the `ViewDimensions` argument to the closure to calculate a return
value.

In the example below, the weather emoji are offset 20 points from the vertical
center of the `HStack`.

Changing the alignment of one view may have effects on surrounding views. Here
the offset values inside a stack and its contained views is the difference of
their absolute offsets.

## See Also

### Aligning views

Aligning views within a stack

Position views inside a stack using alignment guides.

Aligning views across stacks

Create a custom alignment and use it to align views across multiple stacks.

`func alignmentGuide(HorizontalAlignment, computeValue: (ViewDimensions) ->
CGFloat) -> some View`

Sets the view’s horizontal alignment.

`struct Alignment`

An alignment in both axes.

`struct HorizontalAlignment`

An alignment position along the horizontal axis.

`struct VerticalAlignment`

An alignment position along the vertical axis.

`struct DepthAlignment`

An alignment position along the depth axis.

`protocol AlignmentID`

A type that you use to create custom alignment guides.

`struct ViewDimensions`

A view’s size and alignment guides in its own coordinate space.

Instance Method

# padding(_:)

Adds a specific padding amount to each edge of this view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func padding(_ length: CGFloat) -> some View
    

##  Parameters

`length`

    

The amount, given in points, to pad this view on all edges.

## Return Value

A view that’s padded by the amount you specify.

## Discussion

Use this modifier to add padding all the way around a view.

The order in which you apply modifiers matters. The example above applies the
padding before applying the border to ensure that the border encompasses the
padded region:

To independently control the amount of padding for each edge, use
`padding(_:)`. To pad a select set of edges by the same amount, use
`padding(_:_:)`.

## See Also

### Adding padding around a view

`func padding(Edge.Set, CGFloat?) -> some View`

Adds an equal padding amount to specific edges of this view.

`func padding(EdgeInsets) -> some View`

Adds a different padding amount to each edge of this view.

`func padding3D(CGFloat) -> some View`

Pads this view along all edge insets by the amount you specify.

`func padding3D(EdgeInsets3D) -> some View`

Pads this view using the edge insets you specify.

`func padding3D(Edge3D.Set, CGFloat?) -> some View`

Pads this view using the edge insets you specify.

`func scenePadding(Edge.Set) -> some View`

Adds padding to the specified edges of this view using an amount that’s
appropriate for the current scene.

`func scenePadding(ScenePadding, edges: Edge.Set) -> some View`

Adds a specified kind of padding to the specified edges of this view using an
amount that’s appropriate for the current scene.

`struct ScenePadding`

The padding used to space a view from its containing scene.

Instance Method

# padding(_:_:)

Adds an equal padding amount to specific edges of this view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func padding(
        _ edges: Edge.Set = .all,
        _ length: CGFloat? = nil
    ) -> some View
    

##  Parameters

`edges`

    

The set of edges to pad for this view. The default is `all`.

`length`

    

An amount, given in points, to pad this view on the specified edges. If you
set the value to `nil`, SwiftUI uses a platform-specific default amount. The
default value of this parameter is `nil`.

## Return Value

A view that’s padded by the specified amount on the specified edges.

## Discussion

Use this modifier to add a specified amount of padding to one or more edges of
the view. Indicate the edges to pad by naming either a single value from
`Edge.Set`, or by specifying an `OptionSet` that contains edge values:

The order in which you apply modifiers matters. The example above applies the
padding before applying the border to ensure that the border encompasses the
padded region:

You can omit either or both of the parameters. If you omit the `length`,
SwiftUI uses a default amount of padding. If you omit the `edges`, SwiftUI
applies the padding to all edges. Omit both to add a default padding all the
way around a view. SwiftUI chooses a default amount of padding that’s
appropriate for the platform and the presentation context.

The example above looks like this in iOS under typical conditions:

To control the amount of padding independently for each edge, use
`padding(_:)`. To pad all outside edges of a view by a specified amount, use
`padding(_:)`.

## See Also

### Adding padding around a view

`func padding(CGFloat) -> some View`

Adds a specific padding amount to each edge of this view.

`func padding(EdgeInsets) -> some View`

Adds a different padding amount to each edge of this view.

`func padding3D(CGFloat) -> some View`

Pads this view along all edge insets by the amount you specify.

`func padding3D(EdgeInsets3D) -> some View`

Pads this view using the edge insets you specify.

`func padding3D(Edge3D.Set, CGFloat?) -> some View`

Pads this view using the edge insets you specify.

`func scenePadding(Edge.Set) -> some View`

Adds padding to the specified edges of this view using an amount that’s
appropriate for the current scene.

`func scenePadding(ScenePadding, edges: Edge.Set) -> some View`

Adds a specified kind of padding to the specified edges of this view using an
amount that’s appropriate for the current scene.

`struct ScenePadding`

The padding used to space a view from its containing scene.

Instance Method

# padding(_:)

Adds a different padding amount to each edge of this view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func padding(_ insets: EdgeInsets) -> some View
    

##  Parameters

`insets`

    

An `EdgeInsets` instance that contains padding amounts for each edge.

## Return Value

A view that’s padded by different amounts on each edge.

## Discussion

Use this modifier to add a different amount of padding on each edge of a view:

The order in which you apply modifiers matters. The example above applies the
padding before applying the border to ensure that the border encompasses the
padded region:

To pad a view on specific edges with equal padding for all padded edges, use
`padding(_:_:)`. To pad all edges of a view equally, use `padding(_:)`.

## See Also

### Adding padding around a view

`func padding(CGFloat) -> some View`

Adds a specific padding amount to each edge of this view.

`func padding(Edge.Set, CGFloat?) -> some View`

Adds an equal padding amount to specific edges of this view.

`func padding3D(CGFloat) -> some View`

Pads this view along all edge insets by the amount you specify.

`func padding3D(EdgeInsets3D) -> some View`

Pads this view using the edge insets you specify.

`func padding3D(Edge3D.Set, CGFloat?) -> some View`

Pads this view using the edge insets you specify.

`func scenePadding(Edge.Set) -> some View`

Adds padding to the specified edges of this view using an amount that’s
appropriate for the current scene.

`func scenePadding(ScenePadding, edges: Edge.Set) -> some View`

Adds a specified kind of padding to the specified edges of this view using an
amount that’s appropriate for the current scene.

`struct ScenePadding`

The padding used to space a view from its containing scene.

Instance Method

# padding3D(_:)

Pads this view along all edge insets by the amount you specify.

visionOS 1.0+

    
    
    func padding3D(_ length: CGFloat) -> some View
    

##  Parameters

`length`

    

The amount to inset this view on each edge.

## Return Value

A view that pads this view by the amount you specify.

## See Also

### Adding padding around a view

`func padding(CGFloat) -> some View`

Adds a specific padding amount to each edge of this view.

`func padding(Edge.Set, CGFloat?) -> some View`

Adds an equal padding amount to specific edges of this view.

`func padding(EdgeInsets) -> some View`

Adds a different padding amount to each edge of this view.

`func padding3D(EdgeInsets3D) -> some View`

Pads this view using the edge insets you specify.

`func padding3D(Edge3D.Set, CGFloat?) -> some View`

Pads this view using the edge insets you specify.

`func scenePadding(Edge.Set) -> some View`

Adds padding to the specified edges of this view using an amount that’s
appropriate for the current scene.

`func scenePadding(ScenePadding, edges: Edge.Set) -> some View`

Adds a specified kind of padding to the specified edges of this view using an
amount that’s appropriate for the current scene.

`struct ScenePadding`

The padding used to space a view from its containing scene.

Instance Method

# padding3D(_:)

Pads this view using the edge insets you specify.

visionOS 1.0+

    
    
    func padding3D(_ insets: EdgeInsets3D) -> some View
    

##  Parameters

`insets`

    

The edges to inset.

## Return Value

A view that pads this view using edge the insets you specify.

## See Also

### Adding padding around a view

`func padding(CGFloat) -> some View`

Adds a specific padding amount to each edge of this view.

`func padding(Edge.Set, CGFloat?) -> some View`

Adds an equal padding amount to specific edges of this view.

`func padding(EdgeInsets) -> some View`

Adds a different padding amount to each edge of this view.

`func padding3D(CGFloat) -> some View`

Pads this view along all edge insets by the amount you specify.

`func padding3D(Edge3D.Set, CGFloat?) -> some View`

Pads this view using the edge insets you specify.

`func scenePadding(Edge.Set) -> some View`

Adds padding to the specified edges of this view using an amount that’s
appropriate for the current scene.

`func scenePadding(ScenePadding, edges: Edge.Set) -> some View`

Adds a specified kind of padding to the specified edges of this view using an
amount that’s appropriate for the current scene.

`struct ScenePadding`

The padding used to space a view from its containing scene.

Instance Method

# padding3D(_:_:)

Pads this view using the edge insets you specify.

visionOS 1.0+

    
    
    func padding3D(
        _ edges: Edge3D.Set = .all,
        _ length: CGFloat? = nil
    ) -> some View
    

##  Parameters

`edges`

    

The set of edges along which to inset this view.

`length`

    

The amount to inset this view on each edge. If `nil`, the amount is the system
default amount.

## Return Value

A view that pads this view using edge the insets you specify.

## See Also

### Adding padding around a view

`func padding(CGFloat) -> some View`

Adds a specific padding amount to each edge of this view.

`func padding(Edge.Set, CGFloat?) -> some View`

Adds an equal padding amount to specific edges of this view.

`func padding(EdgeInsets) -> some View`

Adds a different padding amount to each edge of this view.

`func padding3D(CGFloat) -> some View`

Pads this view along all edge insets by the amount you specify.

`func padding3D(EdgeInsets3D) -> some View`

Pads this view using the edge insets you specify.

`func scenePadding(Edge.Set) -> some View`

Adds padding to the specified edges of this view using an amount that’s
appropriate for the current scene.

`func scenePadding(ScenePadding, edges: Edge.Set) -> some View`

Adds a specified kind of padding to the specified edges of this view using an
amount that’s appropriate for the current scene.

`struct ScenePadding`

The padding used to space a view from its containing scene.

Instance Method

# listRowInsets(_:)

Applies an inset to the rows in a list.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func listRowInsets(_ insets: EdgeInsets?) -> some View
    

##  Parameters

`insets`

    

The `EdgeInsets` to apply to the edges of the view.

## Return Value

A view that uses the given edge insets when used as a list cell.

## Discussion

Use `listRowInsets(_:)` to change the default padding of the content of list
items.

In the example below, the `Flavor` enumeration provides content for list
items. The SwiftUI `ForEach` structure computes views for each element of the
`Flavor` enumeration and extracts the raw value of each of its elements using
the resulting text to create each list row item. The `listRowInsets(_:)`
modifier then changes the edge insets of each row of the list according to the
`EdgeInsets` provided:

## See Also

### Configuring rows

`func listRowHoverEffect(HoverEffect?) -> some View`

Requests that the containing list row use the provided hover effect.

`func listRowHoverEffectDisabled(Bool) -> some View`

Requests that the containing list row have its hover effect disabled.

`func listItemTint(Color?) -> some View`

Sets a fixed tint color for content in a list.

`func listItemTint(ListItemTint?) -> some View`

Sets the tint effect for content in a list.

`struct ListItemTint`

A tint effect configuration that you can apply to content in a list.

`var defaultMinListRowHeight: CGFloat`

The default minimum height of a row in a `List`. The default minimum height of
a row in a list.

Instance Method

# scenePadding(_:)

Adds padding to the specified edges of this view using an amount that’s
appropriate for the current scene.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func scenePadding(_ edges: Edge.Set = .all) -> some View
    

##  Parameters

`edges`

    

The set of edges along which to pad this view.

## Return Value

A view that’s padded on specified edges by a scene-appropriate amount.

## Discussion

Use this modifier to add a scene-appropriate amount of padding to a view.
Specify either a single edge value from `Edge.Set`, or an `OptionSet` that
describes the edges to pad.

In macOS, use scene padding to produce the recommended spacing around the root
view of a window. In watchOS, use scene padding to align elements of your user
interface with top level elements, like the title of a navigation view. For
example, compare the effects of different kinds of padding on text views
presented inside a `NavigationView` in watchOS:

The text with scene padding automatically aligns with the title, unlike the
text that uses the default padding or the text without padding:

Scene padding in watchOS also ensures that your content avoids the curved
edges of a device like Apple Watch Series 7. In other platforms, scene padding
produces the same default padding that you get from the `padding(_:_:)`
modifier.

Important

Scene padding doesn’t pad the top and bottom edges of a view in watchOS, even
if you specify those edges as part of the input. For example, if you specify
`vertical` instead of `horizontal` in the example above, the modifier would
have no effect in watchOS. It does, however, apply to all the edges that you
specify in other platforms.

## See Also

### Adding padding around a view

`func padding(CGFloat) -> some View`

Adds a specific padding amount to each edge of this view.

`func padding(Edge.Set, CGFloat?) -> some View`

Adds an equal padding amount to specific edges of this view.

`func padding(EdgeInsets) -> some View`

Adds a different padding amount to each edge of this view.

`func padding3D(CGFloat) -> some View`

Pads this view along all edge insets by the amount you specify.

`func padding3D(EdgeInsets3D) -> some View`

Pads this view using the edge insets you specify.

`func padding3D(Edge3D.Set, CGFloat?) -> some View`

Pads this view using the edge insets you specify.

`func scenePadding(ScenePadding, edges: Edge.Set) -> some View`

Adds a specified kind of padding to the specified edges of this view using an
amount that’s appropriate for the current scene.

`struct ScenePadding`

The padding used to space a view from its containing scene.

Instance Method

# scenePadding(_:edges:)

Adds a specified kind of padding to the specified edges of this view using an
amount that’s appropriate for the current scene.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func scenePadding(
        _ padding: ScenePadding,
        edges: Edge.Set = .all
    ) -> some View
    

##  Parameters

`padding`

    

The kind of padding to add.

`edges`

    

The set of edges along which to pad this view.

## Return Value

A view that’s padded on specified edges by a scene-appropriate amount.

## Discussion

Use this modifier to add a scene-appropriate amount of padding to a view.
Specify either a single edge value from `Edge.Set`, or an `OptionSet` that
describes the edges to pad.

In macOS, use scene padding to produce the recommended spacing around the root
view of a window. In watchOS, use scene padding to align elements of your user
interface with top level elements, like the title of a navigation view. For
example, compare the effects of different kinds of padding on text views
presented inside a `NavigationView` in watchOS:

The text with minimum scene padding uses the system minimum padding and the
text with navigation bar scene padding automatically aligns with the
navigation bar content. In contrast, the text that uses the default padding
and the text without padding do not align with scene elements.

Scene padding in watchOS also ensures that your content avoids the curved
edges of a device like Apple Watch Series 7. In other platforms, scene padding
produces the same default padding that you get from the `padding(_:_:)`
modifier.

Important

Scene padding doesn’t pad the top and bottom edges of a view in watchOS, even
if you specify those edges as part of the input. For example, if you specify
`vertical` instead of `horizontal` in the example above, the modifier would
have no effect in watchOS. It does, however, apply to all the edges that you
specify in other platforms.

## See Also

### Adding padding around a view

`func padding(CGFloat) -> some View`

Adds a specific padding amount to each edge of this view.

`func padding(Edge.Set, CGFloat?) -> some View`

Adds an equal padding amount to specific edges of this view.

`func padding(EdgeInsets) -> some View`

Adds a different padding amount to each edge of this view.

`func padding3D(CGFloat) -> some View`

Pads this view along all edge insets by the amount you specify.

`func padding3D(EdgeInsets3D) -> some View`

Pads this view using the edge insets you specify.

`func padding3D(Edge3D.Set, CGFloat?) -> some View`

Pads this view using the edge insets you specify.

`func scenePadding(Edge.Set) -> some View`

Adds padding to the specified edges of this view using an amount that’s
appropriate for the current scene.

`struct ScenePadding`

The padding used to space a view from its containing scene.

Instance Method

# listRowSpacing(_:)

Sets the vertical spacing between two adjacent rows in a List.

iOS 15.0+  iPadOS 15.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    func listRowSpacing(_ spacing: CGFloat?) -> some View
    

##  Parameters

`spacing`

    

The spacing value to use. A value of `nil` uses the default spacing.

## Discussion

The following example creates a List with 10 pts of spacing between each row:

## See Also

### Configuring spacing

`func listSectionSpacing(CGFloat) -> some View`

Sets the spacing to a custom value between adjacent sections in a List.

`func listSectionSpacing(ListSectionSpacing) -> some View`

Sets the spacing between adjacent sections in a List.

`struct ListSectionSpacing`

The spacing options between two adjacent sections in a list.

Instance Method

# listSectionSpacing(_:)

Sets the spacing to a custom value between adjacent sections in a List.

iOS 17.0+  iPadOS 17.0+  Mac Catalyst 17.0+  watchOS 10.0+  visionOS 1.0+

    
    
    func listSectionSpacing(_ spacing: CGFloat) -> some View
    

##  Parameters

`spacing`

    

the amount of spacing to apply.

## Discussion

The following example creates a List with 5 pts of spacing between sections:

Spacing can also be specified on a per-section basis. The following example
creates a List with compact spacing for its second section:

If adjacent sections have different spacing value, the smaller value on the
shared edge is used. Spacing specified inside the List is preferred over any
List-wide value.

## See Also

### Configuring spacing

`func listRowSpacing(CGFloat?) -> some View`

Sets the vertical spacing between two adjacent rows in a List.

`func listSectionSpacing(ListSectionSpacing) -> some View`

Sets the spacing between adjacent sections in a List.

`struct ListSectionSpacing`

The spacing options between two adjacent sections in a list.

Instance Method

# listSectionSpacing(_:)

Sets the spacing between adjacent sections in a List.

iOS 17.0+  iPadOS 17.0+  Mac Catalyst 17.0+  watchOS 10.0+  visionOS 1.0+

    
    
    func listSectionSpacing(_ spacing: ListSectionSpacing) -> some View
    

## Discussion

Pass `.default` for the default spacing, or use `.compact` for a compact
appearance between sections.

The following example creates a List with compact spacing between sections:

## See Also

### Configuring spacing

`func listRowSpacing(CGFloat?) -> some View`

Sets the vertical spacing between two adjacent rows in a List.

`func listSectionSpacing(CGFloat) -> some View`

Sets the spacing to a custom value between adjacent sections in a List.

`struct ListSectionSpacing`

The spacing options between two adjacent sections in a list.

Instance Method

# gridCellColumns(_:)

Tells a view that acts as a cell in a grid to span the specified number of
columns.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func gridCellColumns(_ count: Int) -> some View
    

##  Parameters

`count`

    

The number of columns that the view should consume when placed in a grid row.

## Return Value

A view that occupies the specified number of columns in a grid row.

## Discussion

By default, each view that you put into the content closure of a `GridRow`
corresponds to exactly one column of the grid. Apply the `gridCellColumns(_:)`
modifier to a view that you want to span more than one column, as in the
following example of a typical macOS configuration view:

The `Toggle` in the example above spans the column that contains the font
names and the column that contains the buttons:

Important

When you tell a cell to span multiple columns, the grid changes the merged
cell to use anchor alignment, rather than the usual alignment guides. For
information about the behavior of anchor alignment, see `gridCellAnchor(_:)`.

As a convenience you can cause a view to span all of the `Grid` columns by
placing the view directly in the content closure of the `Grid`, outside of a
`GridRow`, and omitting the modifier. To do the opposite and include more than
one view in a cell, group the views using an appropriate layout container,
like an `HStack`, so that they act as a single view.

## See Also

### Statically arranging views in two dimensions

`struct Grid`

A container view that arranges other views in a two dimensional layout.

`struct GridRow`

A horizontal row in a two dimensional grid container.

`func gridCellAnchor(UnitPoint) -> some View`

Specifies a custom alignment anchor for a view that acts as a grid cell.

`func gridCellUnsizedAxes(Axis.Set) -> some View`

Asks grid layouts not to offer the view extra size in the specified axes.

`func gridColumnAlignment(HorizontalAlignment) -> some View`

Overrides the default horizontal alignment of the grid column that the view
appears in.

Instance Method

# gridCellAnchor(_:)

Specifies a custom alignment anchor for a view that acts as a grid cell.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func gridCellAnchor(_ anchor: UnitPoint) -> some View
    

##  Parameters

`anchor`

    

The unit point that defines how to align the view within the bounds of its
grid cell.

## Return Value

A view that uses the specified anchor point to align its content.

## Discussion

Grids, like stacks and other layout containers, perform most alignment
operations using alignment guides. The grid moves the contents of each cell in
a row in the y direction until the specified `VerticalAlignment` guide of each
view in the row aligns with the same guide of all the other views in the row.
Similarly, the grid aligns the `HorizontalAlignment` guides of views in a
column by adjusting views in the x direction. See the guide types for more
information about typical SwiftUI alignment operations.

When you use the `gridCellAnchor(_:)` modifier on a view in a grid, the grid
changes to an anchor-based alignment strategy for the associated cell. With
anchor alignment, the grid projects a `UnitPoint` that you specify onto both
the view and the cell, and aligns the two projections. For example, consider
the following grid:

The grid creates red reference squares in the first row and column to
establish row and column sizes. Without the anchor modifier, the blue marker
in the remaining cell would appear at the center of its cell, because of the
grid’s default `center` alignment. With the anchor modifier shown in the code
above, the grid aligns the one quarter point of the marker with the one
quarter point of its cell in the x direction, as measured from the origin at
the top left of the cell. The grid also aligns the three quarters point of the
marker with the three quarters point of the cell in the y direction:

`UnitPoint` defines many convenience points that correspond to the typical
alignment guides, which you can use as well. For example, you can use
`topTrailing` to align the top and trailing edges of a view in a cell with the
top and trailing edges of the cell:

Applying the anchor-based alignment strategy to a single cell doesn’t affect
the alignment strategy that the grid uses on other cells.

### Anchor alignment for merged cells

If you use the `gridCellColumns(_:)` modifier to cause a cell to span more
than one column, or if you place a view in a grid outside of a row so that the
view spans the entire grid, the grid automatically converts its vertical and
horizontal alignment guides to the unit point equivalent for the merged cell,
and uses an anchor-based approach for that cell. For example, the following
grid places the marker at the center of the merged cell by converting the
grid’s default `center` alignment guide to a `center` anchor for the blue
marker in the merged cell:

The grid makes this conversion in part to avoid ambiguity. Each column has its
own horizontal guide, and it isn’t clear which of these a cell that spans
multiple columns should align with. Further, in the example above, neither of
the center alignment guides for the second or third column would provide the
expected behavior, which is to center the marker in the merged cell. Anchor
alignment provides this behavior:

## See Also

### Statically arranging views in two dimensions

`struct Grid`

A container view that arranges other views in a two dimensional layout.

`struct GridRow`

A horizontal row in a two dimensional grid container.

`func gridCellColumns(Int) -> some View`

Tells a view that acts as a cell in a grid to span the specified number of
columns.

`func gridCellUnsizedAxes(Axis.Set) -> some View`

Asks grid layouts not to offer the view extra size in the specified axes.

`func gridColumnAlignment(HorizontalAlignment) -> some View`

Overrides the default horizontal alignment of the grid column that the view
appears in.

Instance Method

# gridCellUnsizedAxes(_:)

Asks grid layouts not to offer the view extra size in the specified axes.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func gridCellUnsizedAxes(_ axes: Axis.Set) -> some View
    

##  Parameters

`axes`

    

The dimensions in which the grid shouldn’t offer the view a share of any
available space. This prevents a flexible view like a `Spacer`, `Divider`, or
`Color` from defining the size of a row or column.

## Return Value

A view that doesn’t ask an enclosing grid for extra size in one or more axes.

## Discussion

Use this modifier to prevent a flexible view from taking more space on the
specified axes than the other cells in a row or column require. For example,
consider the following `Grid` that places a `Divider` between two rows of
content:

The text and images all have ideal widths for their content. However, because
a divider takes as much space as its parent offers, the grid fills the width
of the display, expanding all the other cells to match:

You can prevent the grid from giving the divider more width than the other
cells require by adding the modifier with the `Axis.horizontal` parameter:

This restores the grid to the width that it would have without the divider:

## See Also

### Statically arranging views in two dimensions

`struct Grid`

A container view that arranges other views in a two dimensional layout.

`struct GridRow`

A horizontal row in a two dimensional grid container.

`func gridCellColumns(Int) -> some View`

Tells a view that acts as a cell in a grid to span the specified number of
columns.

`func gridCellAnchor(UnitPoint) -> some View`

Specifies a custom alignment anchor for a view that acts as a grid cell.

`func gridColumnAlignment(HorizontalAlignment) -> some View`

Overrides the default horizontal alignment of the grid column that the view
appears in.

Instance Method

# gridColumnAlignment(_:)

Overrides the default horizontal alignment of the grid column that the view
appears in.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func gridColumnAlignment(_ guide: HorizontalAlignment) -> some View
    

##  Parameters

`guide`

    

The `HorizontalAlignment` guide to use for the grid column that the view
appears in.

## Return Value

A view that uses the specified horizontal alignment, and that causes all cells
in the same column of a grid to use the same alignment.

## Discussion

You set a default alignment for the cells in a grid in both vertical and
horizontal dimensions when you create the grid with the
`init(alignment:horizontalSpacing:verticalSpacing:content:)` initializer.
However, you can use the `gridColumnAlignment(_:)` modifier to override the
horizontal alignment of a column within the grid. The following example sets a
grid’s alignment to `leadingFirstTextBaseline`, and then sets the first column
to use `trailing` alignment:

This creates the layout of a typical macOS configuration view, with the
trailing edge of the first column flush with the leading edge of the second
column:

Add the modifier to only one cell in a column. The grid automatically aligns
all cells in that column the same way. You get undefined behavior if you apply
different alignments to different cells in the same column.

To override row alignment, see `init(alignment:content:)`. To override
alignment for a single cell, see `gridCellAnchor(_:)`.

## See Also

### Statically arranging views in two dimensions

`struct Grid`

A container view that arranges other views in a two dimensional layout.

`struct GridRow`

A horizontal row in a two dimensional grid container.

`func gridCellColumns(Int) -> some View`

Tells a view that acts as a cell in a grid to span the specified number of
columns.

`func gridCellAnchor(UnitPoint) -> some View`

Specifies a custom alignment anchor for a view that acts as a grid cell.

`func gridCellUnsizedAxes(Axis.Set) -> some View`

Asks grid layouts not to offer the view extra size in the specified axes.

Instance Method

# ignoresSafeArea(_:edges:)

Expands the safe area of a view.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func ignoresSafeArea(
        _ regions: SafeAreaRegions = .all,
        edges: Edge.Set = .all
    ) -> some View
    

##  Parameters

`regions`

    

The regions to expand the view’s safe area into. The modifier expands into all
safe area region types by default.

`edges`

    

The set of edges to expand. Any edges that you don’t include in this set
remain unchanged. The set includes all edges by default.

## Return Value

A view with an expanded safe area.

## Discussion

By default, the SwiftUI layout system sizes and positions views to avoid
certain safe areas. This ensures that system content like the software
keyboard or edges of the device don’t obstruct your views. To extend your
content into these regions, you can ignore safe areas on specific edges by
applying this modifier.

For examples of how to use this modifier, see Adding a background to your
view.

## See Also

### Staying in the safe areas

`func safeAreaInset<V>(edge: HorizontalEdge, alignment: VerticalAlignment,
spacing: CGFloat?, content: () -> V) -> some View`

Shows the specified content beside the modified view.

`func safeAreaInset<V>(edge: VerticalEdge, alignment: HorizontalAlignment,
spacing: CGFloat?, content: () -> V) -> some View`

Shows the specified content above or below the modified view.

`func safeAreaPadding(EdgeInsets) -> some View`

Adds the provided insets into the safe area of this view.

`func safeAreaPadding(CGFloat) -> some View`

Adds the provided insets into the safe area of this view.

`func safeAreaPadding(Edge.Set, CGFloat?) -> some View`

Adds the provided insets into the safe area of this view.

`struct SafeAreaRegions`

A set of symbolic safe area regions.

Instance Method

# safeAreaInset(edge:alignment:spacing:content:)

Shows the specified content beside the modified view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func safeAreaInset<V>(
        edge: HorizontalEdge,
        alignment: VerticalAlignment = .center,
        spacing: CGFloat? = nil,
        @ViewBuilder content: () -> V
    ) -> some View where V : View
    

##  Parameters

`edge`

    

The horizontal edge of the view to inset by the width of `content`, to make
space for `content`.

`spacing`

    

Extra distance placed between the two views, or nil to use the default amount
of spacing.

`alignment`

    

The alignment guide used to position `content` vertically.

`content`

    

A view builder function providing the view to display in the inset space of
the modified view.

## Return Value

A new view that displays `content` beside the modified view, making space for
the `content` view by horizontally insetting the modified view.

## Discussion

The `content` view is anchored to the specified horizontal edge in the parent
view, aligning its vertical axis to the specified alignment guide. The
modified view is inset by the width of `content`, from `edge`, with its safe
area increased by the same amount.

## See Also

### Staying in the safe areas

`func ignoresSafeArea(SafeAreaRegions, edges: Edge.Set) -> some View`

Expands the safe area of a view.

`func safeAreaInset<V>(edge: VerticalEdge, alignment: HorizontalAlignment,
spacing: CGFloat?, content: () -> V) -> some View`

Shows the specified content above or below the modified view.

`func safeAreaPadding(EdgeInsets) -> some View`

Adds the provided insets into the safe area of this view.

`func safeAreaPadding(CGFloat) -> some View`

Adds the provided insets into the safe area of this view.

`func safeAreaPadding(Edge.Set, CGFloat?) -> some View`

Adds the provided insets into the safe area of this view.

`struct SafeAreaRegions`

A set of symbolic safe area regions.

Instance Method

# safeAreaInset(edge:alignment:spacing:content:)

Shows the specified content above or below the modified view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func safeAreaInset<V>(
        edge: VerticalEdge,
        alignment: HorizontalAlignment = .center,
        spacing: CGFloat? = nil,
        @ViewBuilder content: () -> V
    ) -> some View where V : View
    

##  Parameters

`edge`

    

The vertical edge of the view to inset by the height of `content`, to make
space for `content`.

`spacing`

    

Extra distance placed between the two views, or nil to use the default amount
of spacing.

`alignment`

    

The alignment guide used to position `content` horizontally.

`content`

    

A view builder function providing the view to display in the inset space of
the modified view.

## Return Value

A new view that displays both `content` above or below the modified view,
making space for the `content` view by vertically insetting the modified view,
adjusting the safe area of the result to match.

## Discussion

The `content` view is anchored to the specified vertical edge in the parent
view, aligning its horizontal axis to the specified alignment guide. The
modified view is inset by the height of `content`, from `edge`, with its safe
area increased by the same amount.

## See Also

### Staying in the safe areas

`func ignoresSafeArea(SafeAreaRegions, edges: Edge.Set) -> some View`

Expands the safe area of a view.

`func safeAreaInset<V>(edge: HorizontalEdge, alignment: VerticalAlignment,
spacing: CGFloat?, content: () -> V) -> some View`

Shows the specified content beside the modified view.

`func safeAreaPadding(EdgeInsets) -> some View`

Adds the provided insets into the safe area of this view.

`func safeAreaPadding(CGFloat) -> some View`

Adds the provided insets into the safe area of this view.

`func safeAreaPadding(Edge.Set, CGFloat?) -> some View`

Adds the provided insets into the safe area of this view.

`struct SafeAreaRegions`

A set of symbolic safe area regions.

Instance Method

# safeAreaPadding(_:)

Adds the provided insets into the safe area of this view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func safeAreaPadding(_ insets: EdgeInsets) -> some View
    

## Discussion

Use this modifier when you would like to add a fixed amount of space to the
safe area a view sees.

See the `View/safeAreaInset(edge:alignment:spacing:content)` modifier for
adding to the safe area based on the size of a view.

## See Also

### Staying in the safe areas

`func ignoresSafeArea(SafeAreaRegions, edges: Edge.Set) -> some View`

Expands the safe area of a view.

`func safeAreaInset<V>(edge: HorizontalEdge, alignment: VerticalAlignment,
spacing: CGFloat?, content: () -> V) -> some View`

Shows the specified content beside the modified view.

`func safeAreaInset<V>(edge: VerticalEdge, alignment: HorizontalAlignment,
spacing: CGFloat?, content: () -> V) -> some View`

Shows the specified content above or below the modified view.

`func safeAreaPadding(CGFloat) -> some View`

Adds the provided insets into the safe area of this view.

`func safeAreaPadding(Edge.Set, CGFloat?) -> some View`

Adds the provided insets into the safe area of this view.

`struct SafeAreaRegions`

A set of symbolic safe area regions.

Instance Method

# safeAreaPadding(_:)

Adds the provided insets into the safe area of this view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func safeAreaPadding(_ length: CGFloat) -> some View
    

## Discussion

Use this modifier when you would like to add a fixed amount of space to the
safe area a view sees.

See the `View/safeAreaInset(edge:alignment:spacing:content)` modifier for
adding to the safe area based on the size of a view.

## See Also

### Staying in the safe areas

`func ignoresSafeArea(SafeAreaRegions, edges: Edge.Set) -> some View`

Expands the safe area of a view.

`func safeAreaInset<V>(edge: HorizontalEdge, alignment: VerticalAlignment,
spacing: CGFloat?, content: () -> V) -> some View`

Shows the specified content beside the modified view.

`func safeAreaInset<V>(edge: VerticalEdge, alignment: HorizontalAlignment,
spacing: CGFloat?, content: () -> V) -> some View`

Shows the specified content above or below the modified view.

`func safeAreaPadding(EdgeInsets) -> some View`

Adds the provided insets into the safe area of this view.

`func safeAreaPadding(Edge.Set, CGFloat?) -> some View`

Adds the provided insets into the safe area of this view.

`struct SafeAreaRegions`

A set of symbolic safe area regions.

Instance Method

# safeAreaPadding(_:_:)

Adds the provided insets into the safe area of this view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func safeAreaPadding(
        _ edges: Edge.Set = .all,
        _ length: CGFloat? = nil
    ) -> some View
    

## Discussion

Use this modifier when you would like to add a fixed amount of space to the
safe area a view sees.

See the `View/safeAreaInset(edge:alignment:spacing:content)` modifier for
adding to the safe area based on the size of a view.

## See Also

### Staying in the safe areas

`func ignoresSafeArea(SafeAreaRegions, edges: Edge.Set) -> some View`

Expands the safe area of a view.

`func safeAreaInset<V>(edge: HorizontalEdge, alignment: VerticalAlignment,
spacing: CGFloat?, content: () -> V) -> some View`

Shows the specified content beside the modified view.

`func safeAreaInset<V>(edge: VerticalEdge, alignment: HorizontalAlignment,
spacing: CGFloat?, content: () -> V) -> some View`

Shows the specified content above or below the modified view.

`func safeAreaPadding(EdgeInsets) -> some View`

Adds the provided insets into the safe area of this view.

`func safeAreaPadding(CGFloat) -> some View`

Adds the provided insets into the safe area of this view.

`struct SafeAreaRegions`

A set of symbolic safe area regions.

Instance Method

# contentMargins(_:for:)

Configures the content margin for a provided placement.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func contentMargins(
        _ length: CGFloat,
        for placement: ContentMarginPlacement = .automatic
    ) -> some View
    

##  Parameters

`length`

    

The amount of margins to add on all edges.

`placement`

    

Where the margins should be added.

## Discussion

Use this modifier to customize the content margins of different kinds of
views. For example, you can use this modifier to customize the margins of
scrollable views like `ScrollView`. In the following example, the scroll view
will automatically inset its content by the safe area plus an additional 20
points on the leading and trailing edge.

You can provide a `ContentMarginPlacement` to target specific parts of a view
to customize. For example, provide a `ContentMargingPlacement/scrollContent`
placement to inset the content of a `TextEditor` without affecting the insets
of its scroll indicators.

Similarly, you can customize the insets of scroll indicators separately from
scroll content. Consider doing this when applying a custom clip shape that may
clip the indicators.

When applying multiple contentMargins modifiers, modifiers with the same
placement will override modifiers higher up in the view hierarchy.

## See Also

### Setting margins

`func contentMargins(Edge.Set, CGFloat?, for: ContentMarginPlacement) -> some
View`

Configures the content margin for a provided placement.

`func contentMargins(Edge.Set, EdgeInsets, for: ContentMarginPlacement) ->
some View`

Configures the content margin for a provided placement.

`struct ContentMarginPlacement`

The placement of margins.

Instance Method

# contentMargins(_:_:for:)

Configures the content margin for a provided placement.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func contentMargins(
        _ edges: Edge.Set = .all,
        _ length: CGFloat?,
        for placement: ContentMarginPlacement = .automatic
    ) -> some View
    

##  Parameters

`edges`

    

The edges to add the margins to.

`length`

    

The amount of margins to add.

`placement`

    

Where the margins should be added.

## Discussion

Use this modifier to customize the content margins of different kinds of
views. For example, you can use this modifier to customize the margins of
scrollable views like `ScrollView`. In the following example, the scroll view
will automatically inset its content by the safe area plus an additional 20
points on the leading and trailing edge.

You can provide a `ContentMarginPlacement` to target specific parts of a view
to customize. For example, provide a `ContentMargingPlacement/scrollContent`
placement to inset the content of a `TextEditor` without affecting the insets
of its scroll indicators.

Similarly, you can customize the insets of scroll indicators separately from
scroll content. Consider doing this when applying a custom clip shape that may
clip the indicators.

When applying multiple contentMargins modifiers, modifiers with the same
placement will override modifiers higher up in the view hierarchy.

## See Also

### Setting margins

`func contentMargins(CGFloat, for: ContentMarginPlacement) -> some View`

Configures the content margin for a provided placement.

`func contentMargins(Edge.Set, EdgeInsets, for: ContentMarginPlacement) ->
some View`

Configures the content margin for a provided placement.

`struct ContentMarginPlacement`

The placement of margins.

Instance Method

# contentMargins(_:_:for:)

Configures the content margin for a provided placement.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func contentMargins(
        _ edges: Edge.Set = .all,
        _ insets: EdgeInsets,
        for placement: ContentMarginPlacement = .automatic
    ) -> some View
    

##  Parameters

`edges`

    

The edges to add the margins to.

`insets`

    

The amount of margins to add.

`placement`

    

Where the margins should be added.

## Discussion

Use this modifier to customize the content margins of different kinds of
views. For example, you can use this modifier to customize the margins of
scrollable views like `ScrollView`. In the following example, the scroll view
will automatically inset its content by the safe area plus an additional 20
points on the leading and trailing edge.

You can provide a `ContentMarginPlacement` to target specific parts of a view
to customize. For example, provide a `ContentMargingPlacement/scrollContent`
placement to inset the content of a `TextEditor` without affecting the insets
of its scroll indicators.

Similarly, you can customize the insets of scroll indicators separately from
scroll content. Consider doing this when applying a custom clip shape that may
clip the indicators.

When applying multiple contentMargins modifiers, modifiers with the same
placement will override modifiers higher up in the view hierarchy.

## See Also

### Setting margins

`func contentMargins(CGFloat, for: ContentMarginPlacement) -> some View`

Configures the content margin for a provided placement.

`func contentMargins(Edge.Set, CGFloat?, for: ContentMarginPlacement) -> some
View`

Configures the content margin for a provided placement.

`struct ContentMarginPlacement`

The placement of margins.

Instance Method

# zIndex(_:)

Controls the display order of overlapping views.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func zIndex(_ value: Double) -> some View
    

##  Parameters

`value`

    

A relative front-to-back ordering for this view; the default is `0`.

## Discussion

Use `zIndex(_:)` when you want to control the front-to-back ordering of views.

In this example there are two overlapping rotated rectangles. The frontmost is
represented by the larger index value.

## See Also

### Layering views

Adding a background to your view

Compose a background behind your view and extend it beyond the safe area
insets.

`struct ZStack`

A view that overlays its subviews, aligning them in both axes.

`func background<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify behind this view.

`func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to a style.

`func background(ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to the default background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with the default
background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with the default background
style.

`func overlay<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify in front of this view.

`func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Layers the specified style in front of this view.

`func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Layers a shape that you specify in front of this view.

`var backgroundMaterial: Material?`

The material underneath the current view.

`func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some
View`

Sets the container background of the enclosing container using a view.

`func containerBackground<V>(for: ContainerBackgroundPlacement, alignment:
Alignment, content: () -> V) -> some View`

Sets the container background of the enclosing container using a view.

`struct ContainerBackgroundPlacement`

The placement of a container background.

Instance Method

# layoutDirectionBehavior(_:)

Sets the behavior of this view for different layout directions.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func layoutDirectionBehavior(_ behavior: LayoutDirectionBehavior) -> some View
    

##  Parameters

`behavior`

    

A LayoutDirectionBehavior value that indicates whether this view should mirror
in a particular layout direction. By default, views will adjust their layouts
automatically in a right-to-left context and do not need to be mirrored.

## Return Value

A view that conditionally mirrors its contents horizontally in a given layout
direction.

## Discussion

Use `layoutDirectionBehavior(_:)` when you need the system to horizontally
mirror the contents of the view when presented in a layout direction.

To override the layout direction for a specific view, use the
`environment(_:_:)` view modifier to explicitly override the `layoutDirection`
environment value for the view.

## See Also

### Setting a layout direction

`enum LayoutDirectionBehavior`

A description of what should happen when the layout direction changes.

`var layoutDirection: LayoutDirection`

The layout direction associated with the current environment.

`enum LayoutDirection`

A direction in which SwiftUI can lay out content.

Instance Method

# layoutValue(key:value:)

Associates a value with a custom layout property.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func layoutValue<K>(
        key: K.Type,
        value: K.Value
    ) -> some View where K : LayoutValueKey
    

##  Parameters

`key`

    

The type of the key that you want to set a value for. Create the key as a type
that conforms to the `LayoutValueKey` protocol.

`value`

    

The value to assign to the key for this view. The value must be of the type
that you establish for the key’s associated value when you implement the key’s
`defaultValue` property.

## Return Value

A view that has the specified value for the specified key.

## Discussion

Use this method to set a value for a custom property that you define with
`LayoutValueKey`. For example, if you define a `Flexibility` key, you can set
the key on a `Text` view using the key’s type and a value:

For convenience, you might define a method that does this in an extension to
`View`:

This method makes the call site easier to read:

If you perform layout operations in a type that conforms to the `Layout`
protocol, you can read the key’s associated value for each subview of your
custom layout type. Do this by indexing the subview’s proxy with the key. For
more information, see `LayoutValueKey`.

## See Also

### Associating values with views in a custom layout

`protocol LayoutValueKey`

A key for accessing a layout value of a layout container’s subviews.

