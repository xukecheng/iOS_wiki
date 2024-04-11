Instance Method

# place(at:anchor:proposal:)

Assigns a position and proposed size to the subview.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func place(
        at position: CGPoint,
        anchor: UnitPoint = .topLeading,
        proposal: ProposedViewSize
    )

##  Parameters

`position`

    

The place where the anchor of the subview should appear in its container view,
relative to container’s bounds.

`anchor`

    

The unit point on the subview that appears at `position`. You can use a built-
in point, like `center`, or you can create a custom `UnitPoint`.

`proposal`

    

A proposed size for the subview. In SwiftUI, views choose their own size, but
can take a size proposal from their parent view into account when doing so.

## Discussion

Call this method from your implementation of the `Layout` protocol’s
`placeSubviews(in:proposal:subviews:cache:)` method for each subview arranged
by the layout. Provide a position within the container’s bounds where the
subview should appear, and an anchor that indicates which part of the subview
appears at that point.

Include a proposed size that the subview can take into account when sizing
itself. To learn the subview’s size for a given proposal before calling this
method, you can call the `dimensions(in:)` or `sizeThatFits(_:)` method on the
subview with the same proposal. That enables you to know subview sizes before
committing to subview positions.

Important

Call this method only from within your `Layout` type’s implementation of the
`placeSubviews(in:proposal:subviews:cache:)` method.

If you call this method more than once for a subview, the last call takes
precedence. If you don’t call this method for a subview, the subview appears
at the center of its layout container and uses the layout container’s size
proposal.

Instance Method

# dimensions(in:)

Asks the subview for its dimensions and alignment guides.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func dimensions(in proposal: ProposedViewSize) -> ViewDimensions

##  Parameters

`proposal`

    

A proposed size for the subview. In SwiftUI, views choose their own size, but
can take a size proposal from their parent view into account when doing so.

## Return Value

A `ViewDimensions` instance that includes a height and width, as well as a set
of alignment guides.

## Discussion

Call this method to ask a subview of a custom `Layout` type about its size and
alignment properties. You can call it from your implementation of any of that
protocol’s methods, like `placeSubviews(in:proposal:subviews:cache:)` or
`sizeThatFits(proposal:subviews:cache:)`, to get information for your layout
calculations.

When you call this method, you propose a size using the `proposal` parameter.
The subview can choose its own size, but might take the proposal into account.
You can call this method more than once with different proposals to find out
if the view is flexible. For example, you can propose:

  * `zero` to get the subview’s minimum size.

  * `infinity` to get the subview’s maximum size.

  * `unspecified` to get the subview’s ideal size.

If you need only the view’s height and width, you can use the
`sizeThatFits(_:)` method instead.

## See Also

### Getting subview characteristics

`func sizeThatFits(ProposedViewSize) -> CGSize`

Asks the subview for its size.

`var spacing: ViewSpacing`

The subviews’s preferred spacing values.

`var priority: Double`

The layout priority of the subview.

Instance Method

# sizeThatFits(_:)

Asks the subview for its size.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func sizeThatFits(_ proposal: ProposedViewSize) -> CGSize

##  Parameters

`proposal`

    

A proposed size for the subview. In SwiftUI, views choose their own size, but
can take a size proposal from their parent view into account when doing so.

## Return Value

The size that the subview chooses for itself, given the proposal from its
container view.

## Discussion

Use this method as a convenience to get the `width` and `height` properties of
the `ViewDimensions` instance returned by the `dimensions(in:)` method,
reported as a `CGSize` instance.

## See Also

### Getting subview characteristics

`func dimensions(in: ProposedViewSize) -> ViewDimensions`

Asks the subview for its dimensions and alignment guides.

`var spacing: ViewSpacing`

The subviews’s preferred spacing values.

`var priority: Double`

The layout priority of the subview.

Instance Property

# spacing

The subviews’s preferred spacing values.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var spacing: ViewSpacing { get }

## Discussion

This `ViewSpacing` instance indicates how much space a subview in a custom
layout prefers to have between it and the next view. It contains preferences
for all edges, and might take into account the type of both this and the
adjacent view. If your `Layout` type places subviews based on spacing
preferences, use this instance to compute a distance between this subview and
the next. See `placeSubviews(in:proposal:subviews:cache:)` for an example.

You can also merge this instance with instances from other subviews to
construct a new instance that’s suitable for the subviews’ container. See
`spacing(subviews:cache:)`.

## See Also

### Getting subview characteristics

`func dimensions(in: ProposedViewSize) -> ViewDimensions`

Asks the subview for its dimensions and alignment guides.

`func sizeThatFits(ProposedViewSize) -> CGSize`

Asks the subview for its size.

`var priority: Double`

The layout priority of the subview.

Instance Property

# priority

The layout priority of the subview.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var priority: Double { get }

## Discussion

If you define a custom layout type using the `Layout` protocol, you can read
this value from subviews and use the value when deciding how to assign space
to subviews. For example, you can read all of the subview priorities into an
array before placing the subviews in a custom layout type called
`BasicVStack`:

Set the layout priority for a view that appears in your layout by applying the
`layoutPriority(_:)` view modifier. For example, you can assign two different
priorities to views that you arrange with `BasicVStack`:

## See Also

### Getting subview characteristics

`func dimensions(in: ProposedViewSize) -> ViewDimensions`

Asks the subview for its dimensions and alignment guides.

`func sizeThatFits(ProposedViewSize) -> CGSize`

Asks the subview for its size.

`var spacing: ViewSpacing`

The subviews’s preferred spacing values.

Instance Subscript

# subscript(_:)

Gets the value for the subview that’s associated with the specified key.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    subscript<K>(key: K.Type) -> K.Value where K : LayoutValueKey { get }

## Overview

If you define a custom layout value using `LayoutValueKey`, you can read the
key’s associated value for a given subview in a layout container by indexing
the container’s subviews with the key type. For example, if you define a
`Flexibility` key type, you can put the associated values of all the layout’s
subviews into an array:

For more information about creating a custom layout, see `Layout`.

