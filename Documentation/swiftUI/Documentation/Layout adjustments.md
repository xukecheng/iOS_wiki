Article

# Laying out a simple view

Create a view layout by adjusting the size of views.

## Overview

To create a layout for a view, start by composing a hierarchy of child views.
Then, refine the size and spacing of the child views with configuration
parameters, and by adding view modifiers, like those that affect a view’s
frame and padding. To review how to compose layouts, see Building layouts with
stack views.

### Establish a view hierarchy

The following example creates a view to display an incoming message from a
messaging service. The view uses an `HStack` to collect a view that identifies
the sender and another that provides the content of the message:

The following screenshot of a `MessageRow` view includes a border that shows
its bounds. Note the large size of the circle, which fills the space available
to it:

When SwiftUI renders a view hierarchy, it recursively evaluates each child
view: The parent view proposes a size to the child views it contains, and the
child views respond with a computed size.

The `MessageRow` view proposes a size to its only child, the `HStack`, which
is the full size proposed to it by its own parent. The stack proportionally
divides this space between its child views, with system-default spacing
between each child. This continues recursively:

  * The `ZStack` proposes a size to its child views, the `Circle` and `Text` views.

  * The `Circle` expands up to the size offered, while the `Text` takes just enough space for the string it contains.

  * The `ZStack` returns the size of its largest child view, in this case the `Circle`.

When all child views have reported their size, the parent view renders them.
For a hands-on approach to learning how the SwiftUI view hierarchy works, see
the Building lists and navigation section in the Introducing SwiftUI tutorial.

### Limit the view size

In the example above, SwiftUI has built-in views that manage size in different
ways, including views that:

  * Expand to fill the space offered by their parent, like `Color`, `LinearGradient`, and `Circle`.

  * Have an ideal size that varies according to their contents, like `Text` and the container views.

  * Have an ideal size that never varies, like `Toggle` or `DatePicker`.

You can constrain a view to a fixed size by adding a frame modifier. For
example, use the `frame(width:height:alignment:)` modifier to limit the width
the circle to `40` points:

When you add a frame modifier, SwiftUI wraps the affected view, effectively
adding a new view to the view hierarchy.

When SwiftUI evaluates this new hierarchy, the frame modifier fixes the width
of the `ZStack` that it wraps by passing along the value you specified as its
parameter. The remainder of the size evaluation proceeds as before, where the
`Circle` now expands to fill a smaller space, constrained by the frame’s 40
point width. This enables the `HStack` to provide more space to its other
child, which displays the message text.

### Position content with alignment

If you want the top of the circle aligned with the top of the message content
text, you can refine the view by applying an alignment to the `HStack`. To
position the content vertically within the stack, specify the `alignment`
parameter to `top`:

With the alignment applied, you get an unexpected result. The tops of the
views don’t appear to align:

However, if you select the circle in Xcode, or temporarily add a border to the
circle, you can see the tops of the views do in fact align. For more
information on inspecting the size of a view, see Inspecting view layout.

In the previous section, you applied a frame with only a width constraint.
SwiftUI drew a circle limited by that width. But because the height was left
unspecified, the circle’s frame separately expanded to fill the available
height, even though that extra space had no visible impact on the rendered
circle. You can resolve this problem by adding an explicit `height` parameter:

The contents of the `HStack` are now top aligned, although the stack itself is
centered in the `MessageRow` view as shown by the border displaying the row’s
boundaries.

### Add padding to the view

To avoid visually crowding the outer edges of a view, add padding. This
introduces a fixed amount of space along the specified edges, reducing the
space available for the contents of the view by a corresponding amount. For
example, you can use `padding(_:_:)` to add extra space along the `horizontal`
edges of the `HStack`:

The padding modifier defaults to system-standard spacing, although you can
alternatively choose different values for the padding modifier.

## See Also

### Finetuning a layout

Inspecting view layout

Determine the position and extent of a view using Xcode previews or by adding
temporary borders.

Article

# Inspecting view layout

Determine the position and extent of a view using Xcode previews or by adding
temporary borders.

## Overview

To learn how SwiftUI sizes and positions views, take advantage of Xcode
previews to inspect a single view’s boundaries. You can also add temporary
borders to see how SwiftUI positions and sizes multiple views together.

### Highlight views with Xcode previews

Using Xcode previews, you can quickly see the size of a specific view element
by selecting the view or child view in the editor. To illustrate this, the
following example uses a `VStack` to vertically group an image, provided by SF
Symbols, above a name:

With the `VStack` selected, you’ll see a blue border around the view in the
Xcode preview:

### Use temporary borders to explore complex layouts

To see the border of more than one view, or to see a border when the view
isn’t selected, temporarily add a border with the view modifier
`border(_:width:)`. Set the border’s color to something other than `blue` to
easily distinguish it from a border added by Xcode:

## See Also

### Finetuning a layout

Laying out a simple view

Create a view layout by adjusting the size of views.

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

Structure

# ScenePadding

The padding used to space a view from its containing scene.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    struct ScenePadding

## Overview

Add scene padding to a view using the `scenePadding(_:edges:)` modifier.

## Topics

### Getting padding values

`static let minimum: ScenePadding`

The minimum scene padding value.

`static let navigationBar: ScenePadding`

The navigation bar content scene padding.

## Relationships

### Conforms To

  * `Equatable`
  * `Sendable`

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

`func scenePadding(ScenePadding, edges: Edge.Set) -> some View`

Adds a specified kind of padding to the specified edges of this view using an
amount that’s appropriate for the current scene.

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

Article

# Making fine adjustments to a view’s position

Shift the position of a view by applying the offset or position modifier.

## Overview

Use SwiftUI to adaptively lay out and position your views. If you can’t
achieve your design with composition alone, fine tune the layout with view
modifiers. Add an offset modifier to shift the rendered content of a view from
its current position, or a position modifier to set an explicit position
within its parent.

### Create a view layout

The following example provides a view to illustrate how to position views,
providing a rough layout of views composed within a `ZStack`. The stack
contains a quadrant with an overlaid circle image:

For more detail on composing views with stacks, see Building layouts with
stack views.

### Shift the location of a view’s content

Fine-tune the position of the circle within the quadrant by using an offset
modifier to shift where the parent view places the circle. An offset modifier
shifts the image from its default center position. For example, the
`offset(x:y:)` modifier uses the parameters of `x` and `y` to represent a
relative location within the view’s coordinate space.

In SwiftUI, the view’s coordinate space uses `x` to represent a horizontal
direction and `y` to represent a vertical direction. The value of `x` starts
at `0` at the leading edge of a view, and increases as the location moves
toward the trailing edge of a view. The value of `y` starts at `0` at the top
edge of a view, and increases as the location moves toward the bottom edge of
a view. Don’t assume the leading edge is always on the left, because it
changes with the layout direction. When the layout direction is set to right-
to-left, the `0` horizontal value is on the right side of the view.

The following diagram shows the coordinates in the left-to-right layout
direction against a rectangle, with the origin at the top, leading corner:

The following example shifts the circle `40` points from the center, up and
toward the trailing edge:

### Position view content explicitly

To explicitly position elements within a view, use the `position(x:y:)` view
modifier. A position modifier overrides where the parent view places its
content. The modifier renders the view at a location offset from the origin of
the parent view, unlike an offset modifier that shifts the view from the
location chosen by the parent view. The position modifier uses the same `x`,
`y` coordinate system as the offset modifier, and similarly doesn’t influence
the size of the view. In this example, the position of the circle is set
halfway down on the right side of the quadrant with explicit values:

## See Also

### Adjusting a view’s position

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

`func offset(z: CGFloat) -> some View`

Brings a view forward in Z by the provided distance in points.

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

Article

# Aligning views within a stack

Position views inside a stack using alignment guides.

## Overview

Stacks place their child views to match their alignment, which defaults to
center alignment. When you initialize the stack, you can specify an alignment
for the stack to use that also applies to a stack’s child views. If you want
to modify the placement of individual child views, use the alignment guide
modifier to make adjustments that offset the view from the alignment the stack
provides.

To align views across multiple stacks, see Aligning views across stacks.

### Use defaults for basic alignment

For an example of how SwiftUI applies default alignment to the views in an
`HStack`, examine the following code used to provide a status view for a
recording app. The `HStack` contains an image view for the icon and two text
views with labels that use the `font(_:)` modifier to adjust the font size of
the text.

The orange reference line in the following figure shows the default alignment
position of the views within the stack. The line functions as a visual
reference for the purposes of this article.

### Customize stack alignment

You can align content within a stack based on guides provided by the
alignments that the stack supports. The various kinds of stacks support the
following alignments:

  * `HStack` uses the guides defined in `VerticalAlignment`.

  * `VStack` uses the guides defined in `HorizontalAlignment`.

  * `ZStack` uses the guides defined in `Alignment`, and a combination of `HorizontalAlignment` and `VerticalAlignment`.

Use the `alignment` parameter when initializing a stack to define the
alignment guide for the stack. The following example sets the alignment of the
`HStack` to `firstTextBaseline`, which aligns its child views to the baseline
of the first text view (which contains the string “Connecting”):

### Adjust the alignment of individual views within a stack

Custom images don’t provide a text baseline guide, so the bottom of the image
aligns to the text view’s baseline. Adjust the alignment of the image using
`alignmentGuide(_:computeValue:)` to get the visual alignment you desire. The
alignment guide’s closure provides an instance of `ViewDimensions`, the
parameter `context` in this example — which you can use to return an offset
value. The value looked up from `context` with `bottom`, provides an offset
that aligns the bottom of the image adjusted by an offset to the baseline
guide defined on the stack:

When you use an alignment guide modifier, make sure to specify an active
alignment of the stack. Otherwise, SwiftUI doesn’t invoke the closure to
offset the view. In the example above, the `firstTextBaseline` input to the
alignment guide matches the stack’s alignment, so the adjustment affects the
placement of the image:

### Use SF Symbols to simplify views when aligning with text

You can replace the microphone image with a similar icon from SF Symbols to
simplify the view. The icons from SF Symbols use text baseline guides, which
means they support whatever font styling you apply to the view.

## See Also

### Aligning views

Aligning views across stacks

Create a custom alignment and use it to align views across multiple stacks.

`func alignmentGuide(HorizontalAlignment, computeValue: (ViewDimensions) ->
CGFloat) -> some View`

Sets the view’s horizontal alignment.

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

Article

# Aligning views across stacks

Create a custom alignment and use it to align views across multiple stacks.

## Overview

As you nest stacks together, you may want specific items within those stacks
to align with each other. By default, the alignment you specify for a stack
applies only to that stack’s child views. To align child views that reside in
the nested stacks, define a custom alignment, assign it to the enclosing view,
and use the alignment guide modifier to identify specific views to align.

### Begin with the default center alignment

To illustrate aligning items across stacks, the following view shows a
horizontal stack wrapping around two nested vertical stacks that have a
different number of child views. The enclosing `HStack` doesn’t define an
alignment, so it defaults to `center`.

The image below shows the contents of a nested vertical stack aligning at the
center of the stack. The child elements within the vertical stacks, such as
the titles beneath each image, don’t align with each other.

### Define a custom alignment

To create a new vertical alignment guide, extend `VerticalAlignment` with a
new static property for your guide. Name the guide according to what it aligns
to make it easier to use. The following example uses bottom positioning as the
default value for this guide:

### Assign and apply the custom alignment

To use the alignment guide, assign it to a parent view that encloses the views
you want to align. The following example specifies `imageTitleAlignmentGuide`
as the alignment for the horizontal stack:

The two vertical stacks now align on the bottoms of the stacks, using the
default from your specification for the custom guide.

When you define an alignment on a stack, it projects through enclosed child
views. Within the nested `VStack` instances, apply
`alignmentGuide(_:computeValue:)` to the views to align, using your custom
guide for the `HStack`.

The closure from the alignment guide modifier returns `firstTextBaseline`,
which aligns the baselines of the titles with the alignment guide
`imageTitleAlignmentGuide`.

## See Also

### Aligning views

Aligning views within a stack

Position views inside a stack using alignment guides.

`func alignmentGuide(HorizontalAlignment, computeValue: (ViewDimensions) ->
CGFloat) -> some View`

Sets the view’s horizontal alignment.

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

Structure

# Alignment

An alignment in both axes.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct Alignment

## Overview

An `Alignment` contains a `HorizontalAlignment` guide and a
`VerticalAlignment` guide. Specify an alignment to direct the behavior of
certain layout containers and modifiers, like when you place views in a
`ZStack`, or layer a view in front of or behind another view using
`overlay(alignment:content:)` or `background(alignment:content:)`,
respectively. During layout, SwiftUI brings the specified guides of the
affected views together, aligning the views.

SwiftUI provides a set of built-in alignments that represent common
combinations of the built-in horizontal and vertical alignment guides. The
blue boxes in the following diagram demonstrate the alignment named by each
box’s label, relative to the background view:

The following code generates the diagram above, where each blue box appears in
an overlay that’s configured with a different alignment:

To avoid crowding, the alignment diagram shows only two of the available text
baseline alignments. The others align as their names imply. Notice that the
first text baseline alignment aligns with the top-most line of text in the
background view, while the last text baseline aligns with the bottom-most
line. For more information about text baseline alignment, see
`VerticalAlignment`.

In a left-to-right language like English, the leading and trailing alignments
appear on the left and right edges, respectively. SwiftUI reverses these in
right-to-left language environments. For more information, see
`HorizontalAlignment`.

### Custom alignment

You can create custom alignments — which you typically do to make use of
custom horizontal or vertical guides — by using the
`init(horizontal:vertical:)` initializer. For example, you can combine a
custom vertical guide called `firstThird` with the built-in horizontal
`center` guide, and use it to configure a `ZStack`:

For more information about creating custom guides, including the code that
creates the custom `firstThird` alignment in the example above, see
`AlignmentID`.

## Topics

### Getting top guides

`static let topLeading: Alignment`

A guide that marks the top and leading edges of the view.

`static let top: Alignment`

A guide that marks the top edge of the view.

`static let topTrailing: Alignment`

A guide that marks the top and trailing edges of the view.

### Getting middle guides

`static let leading: Alignment`

A guide that marks the leading edge of the view.

`static let center: Alignment`

A guide that marks the center of the view.

`static let trailing: Alignment`

A guide that marks the trailing edge of the view.

### Getting bottom guides

`static let bottomLeading: Alignment`

A guide that marks the bottom and leading edges of the view.

`static let bottom: Alignment`

A guide that marks the bottom edge of the view.

`static let bottomTrailing: Alignment`

A guide that marks the bottom and trailing edges of the view.

### Getting text baseline guides

`static var leadingFirstTextBaseline: Alignment`

A guide that marks the leading edge and top-most text baseline in a view.

`static var centerFirstTextBaseline: Alignment`

A guide that marks the top-most text baseline in a view.

`static var trailingFirstTextBaseline: Alignment`

A guide that marks the trailing edge and top-most text baseline in a view.

`static var leadingLastTextBaseline: Alignment`

A guide that marks the leading edge and bottom-most text baseline in a view.

`static var centerLastTextBaseline: Alignment`

A guide that marks the bottom-most text baseline in a view.

`static var trailingLastTextBaseline: Alignment`

A guide that marks the trailing edge and bottom-most text baseline in a view.

### Creating a custom alignment

`init(horizontal: HorizontalAlignment, vertical: VerticalAlignment)`

Creates a custom alignment value with the specified horizontal and vertical
alignment guides.

`var horizontal: HorizontalAlignment`

The alignment on the horizontal axis.

`var vertical: VerticalAlignment`

The alignment on the vertical axis.

## Relationships

### Conforms To

  * `Equatable`
  * `Sendable`

## See Also

### Aligning views

Aligning views within a stack

Position views inside a stack using alignment guides.

Aligning views across stacks

Create a custom alignment and use it to align views across multiple stacks.

`func alignmentGuide(HorizontalAlignment, computeValue: (ViewDimensions) ->
CGFloat) -> some View`

Sets the view’s horizontal alignment.

`func alignmentGuide(VerticalAlignment, computeValue: (ViewDimensions) ->
CGFloat) -> some View`

Sets the view’s vertical alignment.

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

Structure

# HorizontalAlignment

An alignment position along the horizontal axis.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct HorizontalAlignment

## Overview

Use horizontal alignment guides to tell SwiftUI how to position views relative
to one another horizontally, like when you place views vertically in an
`VStack`. The following example demonstrates common built-in horizontal
alignments:

You can generate the example above by creating a series of columns implemented
as vertical stacks, where you configure each stack with a different alignment
guide:

During layout, SwiftUI aligns the views inside each stack by bringing together
the specified guides of the affected views. SwiftUI calculates the position of
a guide for a particular view based on the characteristics of the view. For
example, the `center` guide appears at half the width of the view. You can
override the guide calculation for a particular view using the
`alignmentGuide(_:computeValue:)` view modifier.

### Layout direction

When a user configures their device to use a left-to-right language like
English, the system places the leading alignment on the left and the trailing
alignment on the right, as the example from the previous section demonstrates.
However, in a right-to-left language, the system reverses these. You can see
this by using the `environment(_:_:)` view modifier to explicitly override the
`layoutDirection` environment value for the view defined above:

This automatic layout adjustment makes it easier to localize your app, but
it’s still important to test your app for the different locales that you ship
into. For more information about the localization process, see Localization.

### Custom alignment guides

You can create a custom horizontal alignment by creating a type that conforms
to the `AlignmentID` protocol, and then using that type to initalize a new
static property on `HorizontalAlignment`:

You implement the `defaultValue(in:)` method to calculate a default value for
the custom alignment guide. The method receives a `ViewDimensions` instance
that you can use to calculate an appropriate value based on characteristics of
the view. The example above places the guide at one quarter of the width of
the view, as measured from the view’s origin.

You can then use the custom alignment guide like any built-in guide. For
example, you can use it as the `alignment` parameter to a `VStack`, or you can
change it for a specific view using the `alignmentGuide(_:computeValue:)` view
modifier. Custom alignment guides also automatically reverse in a right-to-
left environment, just like built-in guides.

### Composite alignment

Combine a `VerticalAlignment` with a `HorizontalAlignment` to create a
composite `Alignment` that indicates both vertical and horizontal positioning
in one value. For example, you could combine your custom `oneQuarter`
horizontal alignment from the previous section with a built-in `center`
vertical alignment to use in a `ZStack`:

The example above uses widths and heights that generate two mismatched sets of
four vertical stripes. The `ZStack` centers the two sets vertically and aligns
them horizontally one quarter of the way from the leading edge of each set. In
a left-to-right locale, this aligns the right edges of the left-most stripes
of each set:

## Topics

### Getting guides

`static let leading: HorizontalAlignment`

A guide that marks the leading edge of the view.

`static let center: HorizontalAlignment`

A guide that marks the horizontal center of the view.

`static let trailing: HorizontalAlignment`

A guide that marks the trailing edge of the view.

`static let listRowSeparatorLeading: HorizontalAlignment`

A guide marking the leading edge of a `List` row separator.

`static let listRowSeparatorTrailing: HorizontalAlignment`

A guide marking the trailing edge of a `List` row separator.

### Creating a custom alignment

`init(any AlignmentID.Type)`

Creates a custom horizontal alignment of the specified type.

`func combineExplicit<S>(S) -> CGFloat?`

Merges a sequence of explicit alignment values produced by this instance.

## Relationships

### Conforms To

  * `Equatable`
  * `Sendable`

## See Also

### Aligning views

Aligning views within a stack

Position views inside a stack using alignment guides.

Aligning views across stacks

Create a custom alignment and use it to align views across multiple stacks.

`func alignmentGuide(HorizontalAlignment, computeValue: (ViewDimensions) ->
CGFloat) -> some View`

Sets the view’s horizontal alignment.

`func alignmentGuide(VerticalAlignment, computeValue: (ViewDimensions) ->
CGFloat) -> some View`

Sets the view’s vertical alignment.

`struct Alignment`

An alignment in both axes.

`struct VerticalAlignment`

An alignment position along the vertical axis.

`struct DepthAlignment`

An alignment position along the depth axis.

`protocol AlignmentID`

A type that you use to create custom alignment guides.

`struct ViewDimensions`

A view’s size and alignment guides in its own coordinate space.

Structure

# VerticalAlignment

An alignment position along the vertical axis.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct VerticalAlignment

## Overview

Use vertical alignment guides to position views relative to one another
vertically, like when you place views side-by-side in an `HStack` or when you
create a row of views in a `Grid` using `GridRow`. The following example
demonstrates common built-in vertical alignments:

You can generate the example above by creating a series of rows implemented as
horizontal stacks, where you configure each stack with a different alignment
guide:

During layout, SwiftUI aligns the views inside each stack by bringing together
the specified guides of the affected views. SwiftUI calculates the position of
a guide for a particular view based on the characteristics of the view. For
example, the `center` guide appears at half the height of the view. You can
override the guide calculation for a particular view using the
`alignmentGuide(_:computeValue:)` view modifier.

### Text baseline alignment

Use the `firstTextBaseline` or `lastTextBaseline` guide to match the bottom of
either the top- or bottom-most line of text that a view contains,
respectively. Text baseline alignment excludes the parts of characters that
descend below the baseline, like the tail on lower case g and j:

If you use a text baseline alignment on a view that contains no text, SwiftUI
applies the equivalent of `bottom` alignment instead. For the row in the
example above, SwiftUI matches the bottom of the horizontal lines with the
baseline of the text:

Aligning a text view to its baseline rather than to the bottom of its frame
produces the best layout effect in many cases, like when creating forms. For
example, you can align the baseline of descriptive text in one `GridRow` cell
with the baseline of a text field, or the label of a checkbox, in another cell
in the same row.

### Custom alignment guides

You can create a custom vertical alignment guide by first creating a type that
conforms to the `AlignmentID` protocol, and then using that type to initalize
a new static property on `VerticalAlignment`:

You implement the `defaultValue(in:)` method to calculate a default value for
the custom alignment guide. The method receives a `ViewDimensions` instance
that you can use to calculate a value based on characteristics of the view.
The example above places the guide at one-third of the height of the view as
measured from the view’s origin.

You can then use the custom alignment guide like any built-in guide. For
example, you can use it as the `alignment` parameter to an `HStack`, or to
alter the guide calculation for a specific view using the
`alignmentGuide(_:computeValue:)` view modifier.

### Composite alignment

Combine a `VerticalAlignment` with a `HorizontalAlignment` to create a
composite `Alignment` that indicates both vertical and horizontal positioning
in one value. For example, you could combine your custom `firstThird` vertical
alignment from the previous section with a built-in `center` horizontal
alignment to use in a `ZStack`:

The example above uses widths and heights that generate two mismatched sets of
three vertical stripes. The `ZStack` centers the two sets horizontally and
aligns them vertically one-third from the top of each set. This aligns the
bottom edges of the top stripe from each set:

## Topics

### Getting guides

`static let top: VerticalAlignment`

A guide that marks the top edge of the view.

`static let center: VerticalAlignment`

A guide that marks the vertical center of the view.

`static let bottom: VerticalAlignment`

A guide that marks the bottom edge of the view.

`static let firstTextBaseline: VerticalAlignment`

A guide that marks the top-most text baseline in a view.

`static let lastTextBaseline: VerticalAlignment`

A guide that marks the bottom-most text baseline in a view.

### Creating a custom alignment

`init(any AlignmentID.Type)`

Creates a custom vertical alignment of the specified type.

`func combineExplicit<S>(S) -> CGFloat?`

Merges a sequence of explicit alignment values produced by this instance.

## Relationships

### Conforms To

  * `Equatable`
  * `Sendable`

## See Also

### Aligning views

Aligning views within a stack

Position views inside a stack using alignment guides.

Aligning views across stacks

Create a custom alignment and use it to align views across multiple stacks.

`func alignmentGuide(HorizontalAlignment, computeValue: (ViewDimensions) ->
CGFloat) -> some View`

Sets the view’s horizontal alignment.

`func alignmentGuide(VerticalAlignment, computeValue: (ViewDimensions) ->
CGFloat) -> some View`

Sets the view’s vertical alignment.

`struct Alignment`

An alignment in both axes.

`struct HorizontalAlignment`

An alignment position along the horizontal axis.

`struct DepthAlignment`

An alignment position along the depth axis.

`protocol AlignmentID`

A type that you use to create custom alignment guides.

`struct ViewDimensions`

A view’s size and alignment guides in its own coordinate space.

Structure

# DepthAlignment

An alignment position along the depth axis.

visionOS 1.0+

    
    
    @frozen
    struct DepthAlignment

## Topics

### Getting guides

`static let back: DepthAlignment`

A guide marking the bottom edge of the view.

`static let center: DepthAlignment`

A guide marking the vertical center of the view.

`static let front: DepthAlignment`

A guide marking the top edge of the view.

## Relationships

### Conforms To

  * `Equatable`

## See Also

### Aligning views

Aligning views within a stack

Position views inside a stack using alignment guides.

Aligning views across stacks

Create a custom alignment and use it to align views across multiple stacks.

`func alignmentGuide(HorizontalAlignment, computeValue: (ViewDimensions) ->
CGFloat) -> some View`

Sets the view’s horizontal alignment.

`func alignmentGuide(VerticalAlignment, computeValue: (ViewDimensions) ->
CGFloat) -> some View`

Sets the view’s vertical alignment.

`struct Alignment`

An alignment in both axes.

`struct HorizontalAlignment`

An alignment position along the horizontal axis.

`struct VerticalAlignment`

An alignment position along the vertical axis.

`protocol AlignmentID`

A type that you use to create custom alignment guides.

`struct ViewDimensions`

A view’s size and alignment guides in its own coordinate space.

Protocol

# AlignmentID

A type that you use to create custom alignment guides.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    protocol AlignmentID

## Overview

Every built-in alignment guide that `VerticalAlignment` or
`HorizontalAlignment` defines as a static property, like `top` or `leading`,
has a unique alignment identifier type that produces the default offset for
that guide. To create a custom alignment guide, define your own alignment
identifier as a type that conforms to the `AlignmentID` protocol, and
implement the required `defaultValue(in:)` method:

When implementing the method, calculate the guide’s default offset from the
view’s origin. If it’s helpful, you can use information from the
`ViewDimensions` input in the calculation. This parameter provides context
about the specific view that’s using the guide. The above example creates an
identifier called `FirstThirdAlignment` and calculates a default value that’s
one-third of the height of the aligned view.

Use the identifier’s type to create a static property in an extension of one
of the alignment guide types, like `VerticalAlignment`:

You can apply your custom guide like any of the built-in guides. For example,
you can use an `HStack` to align its views at one-third of their height using
the guide defined above:

Because each set of stripes has three equal, vertically stacked rectangles,
they align at the bottom edge of the top rectangle. This corresponds in each
case to a third of the overall height, as measured from the origin at the top
of each set of stripes:

You can also use the `alignmentGuide(_:computeValue:)` view modifier to alter
the behavior of your custom guide for a view, as you might alter a built-in
guide. For example, you can change one of the stacks of stripes from the
previous example to align its `firstThird` guide at two thirds of the height
instead:

The modified guide calculation causes the affected view to place the bottom
edge of its middle rectangle on the `firstThird` guide, which aligns with the
bottom edge of the top rectangle in the other two groups:

## Topics

### Getting the default value

`static func defaultValue(in: ViewDimensions) -> CGFloat`

Calculates a default value for the corresponding guide in the specified
context.

**Required**

## See Also

### Aligning views

Aligning views within a stack

Position views inside a stack using alignment guides.

Aligning views across stacks

Create a custom alignment and use it to align views across multiple stacks.

`func alignmentGuide(HorizontalAlignment, computeValue: (ViewDimensions) ->
CGFloat) -> some View`

Sets the view’s horizontal alignment.

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

`struct ViewDimensions`

A view’s size and alignment guides in its own coordinate space.

Structure

# ViewDimensions

A view’s size and alignment guides in its own coordinate space.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    struct ViewDimensions

## Overview

This structure contains the size and alignment guides of a view. You receive
an instance of this structure to use in a variety of layout calculations, like
when you:

  * Define a default value for a custom alignment guide; see `defaultValue(in:)`.

  * Modify an alignment guide on a view; see `alignmentGuide(_:computeValue:)`.

  * Ask for the dimensions of a subview of a custom view layout; see `dimensions(in:)`.

### Custom alignment guides

You receive an instance of this structure as the `context` parameter to the
`defaultValue(in:)` method that you implement to produce the default offset
for an alignment guide, or as the first argument to the closure you provide to
the `alignmentGuide(_:computeValue:)` view modifier to override the default
calculation for an alignment guide. In both cases you can use the instance, if
helpful, to calculate the offset for the guide. For example, you could compute
a default offset for a custom `VerticalAlignment` as a fraction of the view’s
`height`:

As another example, you could use the view dimensions instance to look up the
offset of an existing guide and modify it:

The example above indents the second text view because the subtraction moves
the second text view’s leading guide in the negative x direction, which is to
the left in the view’s coordinate space. As a result, SwiftUI moves the second
text view to the right, relative to the first text view, to keep their leading
guides aligned:

### Layout direction

The discussion above describes a left-to-right language environment, but you
don’t change your guide calculation to operate in a right-to-left environment.
SwiftUI moves the view’s origin from the left to the right side of the view
and inverts the positive x direction. As a result, the existing calculation
produces the same effect, but in the opposite direction.

You can see this if you use the `environment(_:_:)` modifier to set the
`layoutDirection` property for the view that you defined above:

With no change in your guide, this produces the desired effect — it indents
the second text view’s right side, relative to the first text view’s right
side. The leading edge is now on the right, and the direction of the offset is
reversed:

## Topics

### Getting dimensions

`var height: CGFloat`

The view’s height.

`var width: CGFloat`

The view’s width.

### Accessing guide values

`subscript(VerticalAlignment) -> CGFloat`

Gets the value of the given vertical guide.

`subscript(HorizontalAlignment) -> CGFloat`

Gets the value of the given horizontal guide.

`subscript(explicit _: VerticalAlignment) -> CGFloat?`

Gets the explicit value of the given vertical alignment guide

`subscript(explicit _: HorizontalAlignment) -> CGFloat?`

Gets the explicit value of the given horizontal alignment guide.

## Relationships

### Conforms To

  * `Equatable`

## See Also

### Aligning views

Aligning views within a stack

Position views inside a stack using alignment guides.

Aligning views across stacks

Create a custom alignment and use it to align views across multiple stacks.

`func alignmentGuide(HorizontalAlignment, computeValue: (ViewDimensions) ->
CGFloat) -> some View`

Sets the view’s horizontal alignment.

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

Structure

# ContentMarginPlacement

The placement of margins.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct ContentMarginPlacement

## Overview

Different views can support customizating margins that appear in different
parts of that view. Use values of this type to customize those margins of a
particular placement.

For example, use a `scrollIndicators` placement to customize the margins of
scrollable view’s scroll indicators separately from the margins of a
scrollable view’s content.

Use this type with the `contentMargins(_:for:)` modifier.

## Topics

### Getting the placement

`static var automatic: ContentMarginPlacement`

The automatic placement.

`static var scrollContent: ContentMarginPlacement`

The scroll content placement.

`static var scrollIndicators: ContentMarginPlacement`

The scroll indicators placement.

## See Also

### Setting margins

`func contentMargins(CGFloat, for: ContentMarginPlacement) -> some View`

Configures the content margin for a provided placement.

`func contentMargins(Edge.Set, CGFloat?, for: ContentMarginPlacement) -> some
View`

Configures the content margin for a provided placement.

`func contentMargins(Edge.Set, EdgeInsets, for: ContentMarginPlacement) ->
some View`

Configures the content margin for a provided placement.

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

Structure

# SafeAreaRegions

A set of symbolic safe area regions.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    @frozen
    struct SafeAreaRegions

## Topics

### Getting safe area regions

`static let all: SafeAreaRegions`

All safe area regions.

`static let container: SafeAreaRegions`

The safe area defined by the device and containers within the user interface,
including elements such as top and bottom bars.

`static let keyboard: SafeAreaRegions`

The safe area matching the current extent of any software keyboard displayed
over the view content.

## Relationships

### Conforms To

  * `Equatable`
  * `ExpressibleByArrayLiteral`
  * `OptionSet`
  * `RawRepresentable`
  * `Sendable`
  * `SetAlgebra`

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

`func safeAreaPadding(Edge.Set, CGFloat?) -> some View`

Adds the provided insets into the safe area of this view.

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

Enumeration

# LayoutDirectionBehavior

A description of what should happen when the layout direction changes.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    enum LayoutDirectionBehavior

## Overview

A `LayoutDirectionBehavior` can be used with the `layoutDirectionBehavior`
view modifier or the `layoutDirectionBehavior` property of `Shape`.

## Topics

### Getting behaviors

`case fixed`

A behavior that doesn’t mirror when the layout direction changes.

`static var mirrors: LayoutDirectionBehavior`

A behavior that mirrors when the layout direction is right-to-left.

`case mirrors(in: LayoutDirection)`

A behavior that mirrors when the layout direction has the specified value.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Setting a layout direction

`func layoutDirectionBehavior(LayoutDirectionBehavior) -> some View`

Sets the behavior of this view for different layout directions.

`var layoutDirection: LayoutDirection`

The layout direction associated with the current environment.

`enum LayoutDirection`

A direction in which SwiftUI can lay out content.

Instance Property

# layoutDirection

The layout direction associated with the current environment.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var layoutDirection: LayoutDirection { get set }

## Discussion

Use this value to determine or set whether the environment uses a left-to-
right or right-to-left direction.

## See Also

### Setting a layout direction

`func layoutDirectionBehavior(LayoutDirectionBehavior) -> some View`

Sets the behavior of this view for different layout directions.

`enum LayoutDirectionBehavior`

A description of what should happen when the layout direction changes.

`enum LayoutDirection`

A direction in which SwiftUI can lay out content.

Enumeration

# LayoutDirection

A direction in which SwiftUI can lay out content.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    enum LayoutDirection

## Overview

SwiftUI supports both left-to-right and right-to-left directions for laying
out content to support different languages and locales. The system sets the
value based on the user’s locale, but you can also use the `environment(_:_:)`
modifier to override the direction for a view and its child views:

You can also read the `layoutDirection` environment value to find out which
direction applies to a particular environment. However, in many cases, you
don’t need to take any action based on this value. SwiftUI horizontally flips
the x position of each view within its parent, so layout calculations
automatically produce the desired effect for both modes without any changes.

## Topics

### Getting layout directions

`case leftToRight`

A left-to-right layout direction.

`case rightToLeft`

A right-to-left layout direction.

### Creating a layout direction

`init?(UITraitEnvironmentLayoutDirection)`

Create a direction from its UITraitEnvironmentLayoutDirection equivalent.

## Relationships

### Conforms To

  * `CaseIterable`
  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Setting a layout direction

`func layoutDirectionBehavior(LayoutDirectionBehavior) -> some View`

Sets the behavior of this view for different layout directions.

`enum LayoutDirectionBehavior`

A description of what should happen when the layout direction changes.

`var layoutDirection: LayoutDirection`

The layout direction associated with the current environment.

Instance Property

# isLuminanceReduced

A Boolean value that indicates whether the display or environment currently
requires reduced luminance.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var isLuminanceReduced: Bool { get set }

## Discussion

When you detect this condition, lower the overall brightness of your view. For
example, you can change large, filled shapes to be stroked, and choose less
bright colors:

In addition to the changes that you make, the system could also dim the
display to achieve a suitable brightness. By reacting to `isLuminanceReduced`,
you can preserve contrast and readability while helping to satisfy the reduced
brightness requirement.

Note

On watchOS, the system typically sets this value to `true` when the user
lowers their wrist, but the display remains on. Starting in watchOS 8, the
system keeps your view visible on wrist down by default. If you want the
system to blur the screen instead, as it did in earlier versions of watchOS,
set the value for the `WKSupportsAlwaysOnDisplay` key in your app’s
Information Property List file to `false`.

## See Also

### Reacting to interface characteristics

`var displayScale: CGFloat`

The display scale of this environment.

`var pixelLength: CGFloat`

The size of a pixel on the screen.

`var horizontalSizeClass: UserInterfaceSizeClass?`

The horizontal size class of this environment.

`var verticalSizeClass: UserInterfaceSizeClass?`

The vertical size class of this environment.

`enum UserInterfaceSizeClass`

A set of values that indicate the visual size available to the view.

Instance Property

# displayScale

The display scale of this environment.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var displayScale: CGFloat { get set }

## See Also

### Reacting to interface characteristics

`var isLuminanceReduced: Bool`

A Boolean value that indicates whether the display or environment currently
requires reduced luminance.

`var pixelLength: CGFloat`

The size of a pixel on the screen.

`var horizontalSizeClass: UserInterfaceSizeClass?`

The horizontal size class of this environment.

`var verticalSizeClass: UserInterfaceSizeClass?`

The vertical size class of this environment.

`enum UserInterfaceSizeClass`

A set of values that indicate the visual size available to the view.

Instance Property

# pixelLength

The size of a pixel on the screen.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var pixelLength: CGFloat { get }

## Discussion

This value is usually equal to `1` divided by `displayScale`.

## See Also

### Reacting to interface characteristics

`var isLuminanceReduced: Bool`

A Boolean value that indicates whether the display or environment currently
requires reduced luminance.

`var displayScale: CGFloat`

The display scale of this environment.

`var horizontalSizeClass: UserInterfaceSizeClass?`

The horizontal size class of this environment.

`var verticalSizeClass: UserInterfaceSizeClass?`

The vertical size class of this environment.

`enum UserInterfaceSizeClass`

A set of values that indicate the visual size available to the view.

Instance Property

# horizontalSizeClass

The horizontal size class of this environment.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @backDeployed(before: macOS 14.0, tvOS 17.0, watchOS 10.0)
    var horizontalSizeClass: UserInterfaceSizeClass? { get set }

## Discussion

You receive a `UserInterfaceSizeClass` value when you read this environment
value. The value tells you about the amount of horizontal space available to
the view that reads it. You can read this size class like any other of the
`EnvironmentValues`, by creating a property with the `Environment` property
wrapper:

SwiftUI sets this size class based on several factors, including:

  * The current device type.

  * The orientation of the device.

  * The appearance of Slide Over and Split View on iPad.

Several built-in views change their behavior based on this size class. For
example, a `NavigationView` presents a multicolumn view when the horizontal
size class is `UserInterfaceSizeClass.regular`, but a single column otherwise.
You can also adjust the appearance of custom views by reading the size class
and conditioning your views. If you do, be prepared to handle size class
changes while your app runs, because factors like device orientation can
change at runtime.

In watchOS, the horizontal size class is always
`UserInterfaceSizeClass.compact`. In macOS, and tvOS, it’s always
`UserInterfaceSizeClass.regular`.

Writing to the horizontal size class in the environment before macOS 14.0,
tvOS 17.0, and watchOS 10.0 is not supported.

## See Also

### Reacting to interface characteristics

`var isLuminanceReduced: Bool`

A Boolean value that indicates whether the display or environment currently
requires reduced luminance.

`var displayScale: CGFloat`

The display scale of this environment.

`var pixelLength: CGFloat`

The size of a pixel on the screen.

`var verticalSizeClass: UserInterfaceSizeClass?`

The vertical size class of this environment.

`enum UserInterfaceSizeClass`

A set of values that indicate the visual size available to the view.

Instance Property

# verticalSizeClass

The vertical size class of this environment.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @backDeployed(before: macOS 14.0, tvOS 17.0, watchOS 10.0)
    var verticalSizeClass: UserInterfaceSizeClass? { get set }

## Discussion

You receive a `UserInterfaceSizeClass` value when you read this environment
value. The value tells you about the amount of vertical space available to the
view that reads it. You can read this size class like any other of the
`EnvironmentValues`, by creating a property with the `Environment` property
wrapper:

SwiftUI sets this size class based on several factors, including:

  * The current device type.

  * The orientation of the device.

You can adjust the appearance of custom views by reading this size class and
conditioning your views. If you do, be prepared to handle size class changes
while your app runs, because factors like device orientation can change at
runtime.

In watchOS, the vertical size class is always
`UserInterfaceSizeClass.compact`. In macOS, and tvOS, it’s always
`UserInterfaceSizeClass.regular`.

Writing to the vertical size class in the environment before macOS 14.0, tvOS
17.0, and watchOS 10.0 is not supported.

## See Also

### Reacting to interface characteristics

`var isLuminanceReduced: Bool`

A Boolean value that indicates whether the display or environment currently
requires reduced luminance.

`var displayScale: CGFloat`

The display scale of this environment.

`var pixelLength: CGFloat`

The size of a pixel on the screen.

`var horizontalSizeClass: UserInterfaceSizeClass?`

The horizontal size class of this environment.

`enum UserInterfaceSizeClass`

A set of values that indicate the visual size available to the view.

Enumeration

# UserInterfaceSizeClass

A set of values that indicate the visual size available to the view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    enum UserInterfaceSizeClass

## Overview

You receive a size class value when you read either the `horizontalSizeClass`
or `verticalSizeClass` environment value. The value tells you about the amount
of space available to your views in a given direction. You can read the size
class like any other of the `EnvironmentValues`, by creating a property with
the `Environment` property wrapper:

SwiftUI sets the size class based on several factors, including:

  * The current device type.

  * The orientation of the device.

  * The appearance of Slide Over and Split View on iPad.

Several built-in views change their behavior based on the size class. For
example, a `NavigationView` presents a multicolumn view when the horizontal
size class is `UserInterfaceSizeClass.regular`, but a single column otherwise.
You can also adjust the appearance of custom views by reading the size class
and conditioning your views. If you do, be prepared to handle size class
changes while your app runs, because factors like device orientation can
change at runtime.

## Topics

### Getting size classes

`case compact`

The compact size class.

`case regular`

The regular size class.

### Creating a size class

`init?(UIUserInterfaceSizeClass)`

Creates a SwiftUI size class from the specified UIKit size class.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Reacting to interface characteristics

`var isLuminanceReduced: Bool`

A Boolean value that indicates whether the display or environment currently
requires reduced luminance.

`var displayScale: CGFloat`

The display scale of this environment.

`var pixelLength: CGFloat`

The size of a pixel on the screen.

`var horizontalSizeClass: UserInterfaceSizeClass?`

The horizontal size class of this environment.

`var verticalSizeClass: UserInterfaceSizeClass?`

The vertical size class of this environment.

Enumeration

# Edge

An enumeration to indicate one edge of a rectangle.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    enum Edge

## Topics

### Getting the edges

`case top`

`case bottom`

`case leading`

`case trailing`

### Creating an edge

`init?(Edge3D)`

Converts a 3D edge to a 2D edge, if possible.

### Accessing sets of edges

`struct Set`

An efficient set of edges.

## Relationships

### Conforms To

  * `CaseIterable`
  * `Equatable`
  * `Hashable`
  * `RawRepresentable`
  * `Sendable`

## See Also

### Accessing edges and regions

`enum Edge3D`

An edge or face of a 3D volume.

`enum HorizontalEdge`

An edge on the horizontal axis.

`enum VerticalEdge`

An edge on the vertical axis.

`struct EdgeInsets`

The inset distances for the sides of a rectangle.

`struct EdgeInsets3D`

The inset distances for the faces of a 3D volume.

Enumeration

# Edge3D

An edge or face of a 3D volume.

visionOS 1.0+

    
    
    @frozen
    enum Edge3D

## Topics

### Getting the edges

`case top`

`case bottom`

`case leading`

`case trailing`

`case front`

`case back`

### Creating an edge

`init(Edge)`

### Accessing sets of edges

`struct Set`

An efficient set of 3D edges.

## Relationships

### Conforms To

  * `CaseIterable`
  * `Equatable`
  * `Hashable`
  * `RawRepresentable`
  * `Sendable`

## See Also

### Accessing edges and regions

`enum Edge`

An enumeration to indicate one edge of a rectangle.

`enum HorizontalEdge`

An edge on the horizontal axis.

`enum VerticalEdge`

An edge on the vertical axis.

`struct EdgeInsets`

The inset distances for the sides of a rectangle.

`struct EdgeInsets3D`

The inset distances for the faces of a 3D volume.

Enumeration

# HorizontalEdge

An edge on the horizontal axis.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    @frozen
    enum HorizontalEdge

## Overview

Use a horizontal edge for tasks like setting a swipe action with the
`swipeActions(edge:allowsFullSwipe:content:)` view modifier. The positions of
the leading and trailing edges depend on the locale chosen by the user.

## Topics

### Getting the edges

`case leading`

The leading edge.

`case trailing`

The trailing edge.

### Accessing sets of edges

`struct Set`

An efficient set of horizontal edges.

## Relationships

### Conforms To

  * `CaseIterable`
  * `Decodable`
  * `Encodable`
  * `Equatable`
  * `Hashable`
  * `RawRepresentable`
  * `Sendable`

## See Also

### Accessing edges and regions

`enum Edge`

An enumeration to indicate one edge of a rectangle.

`enum Edge3D`

An edge or face of a 3D volume.

`enum VerticalEdge`

An edge on the vertical axis.

`struct EdgeInsets`

The inset distances for the sides of a rectangle.

`struct EdgeInsets3D`

The inset distances for the faces of a 3D volume.

Enumeration

# VerticalEdge

An edge on the vertical axis.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    @frozen
    enum VerticalEdge

## Topics

### Getting the edges

`case top`

The top edge.

`case bottom`

The bottom edge.

### Accessing sets of edges

`struct Set`

An efficient set of vertical edges.

## Relationships

### Conforms To

  * `CaseIterable`
  * `Decodable`
  * `Encodable`
  * `Equatable`
  * `Hashable`
  * `RawRepresentable`
  * `Sendable`

## See Also

### Accessing edges and regions

`enum Edge`

An enumeration to indicate one edge of a rectangle.

`enum Edge3D`

An edge or face of a 3D volume.

`enum HorizontalEdge`

An edge on the horizontal axis.

`struct EdgeInsets`

The inset distances for the sides of a rectangle.

`struct EdgeInsets3D`

The inset distances for the faces of a 3D volume.

Structure

# EdgeInsets

The inset distances for the sides of a rectangle.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct EdgeInsets

## Topics

### Getting edge insets

`var top: CGFloat`

`var bottom: CGFloat`

`var leading: CGFloat`

`var trailing: CGFloat`

### Creating an edge inset

`init()`

`init(top: CGFloat, leading: CGFloat, bottom: CGFloat, trailing: CGFloat)`

`init(EdgeInsets3D)`

Creates a 2D `EdgeInsets` from an `EdgeInsets3D`, dropping its `front` and
`back` values.

`init(NSDirectionalEdgeInsets)`

Create edge insets from the equivalent NSDirectionalEdgeInsets.

## Relationships

### Conforms To

  * `Animatable`
  * `Equatable`
  * `Sendable`

## See Also

### Accessing edges and regions

`enum Edge`

An enumeration to indicate one edge of a rectangle.

`enum Edge3D`

An edge or face of a 3D volume.

`enum HorizontalEdge`

An edge on the horizontal axis.

`enum VerticalEdge`

An edge on the vertical axis.

`struct EdgeInsets3D`

The inset distances for the faces of a 3D volume.

Structure

# EdgeInsets3D

The inset distances for the faces of a 3D volume.

visionOS 1.0+

    
    
    @frozen
    struct EdgeInsets3D

## Topics

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

`var back: CGFloat`

The inset distance along the top back of a 3D volume.

### Creating an edge inset

`init(horizontal: CGFloat, vertical: CGFloat, depth: CGFloat)`

Creates an `EdgeInsets3D` value with values provided for each axis.

`init(top: CGFloat, leading: CGFloat, bottom: CGFloat, trailing: CGFloat,
front: CGFloat, back: CGFloat)`

Creates an `EdgeInsets3D` value with values provided for each face.

## Relationships

### Conforms To

  * `Animatable`
  * `Equatable`
  * `Sendable`

## See Also

### Accessing edges and regions

`enum Edge`

An enumeration to indicate one edge of a rectangle.

`enum Edge3D`

An edge or face of a 3D volume.

`enum HorizontalEdge`

An edge on the horizontal axis.

`enum VerticalEdge`

An edge on the vertical axis.

`struct EdgeInsets`

The inset distances for the sides of a rectangle.

