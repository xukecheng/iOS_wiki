Structure

# ScrollView

A scrollable view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    struct ScrollView<Content> where Content : View

## Overview

The scroll view displays its content within the scrollable content region. As
the user performs platform-appropriate scroll gestures, the scroll view
adjusts what portion of the underlying content is visible. `ScrollView` can
scroll horizontally, vertically, or both, but does not provide zooming
functionality.

In the following example, a `ScrollView` allows the user to scroll through a
`VStack` containing 100 `Text` views. The image after the listing shows the
scroll view’s temporarily visible scrollbar at the right; you can disable it
with the `showsIndicators` parameter of the `ScrollView` initializer.

### Controlling Scroll Position

You can influence where a scroll view is initially scrolled by using the
`defaultScrollAnchor(_:)` view modifier.

Provide a value of `UnitPoint/center`` to have the scroll view start in the
center of its content when a scroll view is scrollable in both axes.

Or provide an alignment of `UnitPoint/bottom`` to have the scroll view start
at the bottom of its content when a scroll view is scrollable in its vertical
axes.

After the scroll view initially renders, the user may scroll the content of
the scroll view.

To perform programmatic scrolling, wrap one or more scroll views with a
`ScrollViewReader`.

## Topics

### Creating a scroll view

`init(Axis.Set, showsIndicators: Bool, content: () -> Content)`

Creates a new instance that’s scrollable in the direction of the given axis
and can show indicators while scrolling.

`init(Axis.Set, content: () -> Content)`

Creates a new instance that’s scrollable in the direction of the given axis
and can show indicators while scrolling.

Available when `Content` conforms to `View`.

### Configuring a scroll view

`var content: Content`

The scroll view’s content.

`var axes: Axis.Set`

The scrollable axes of the scroll view.

`var showsIndicators: Bool`

A value that indicates whether the scroll view displays the scrollable
component of the content offset, in a way that’s suitable for the platform.

### Supporting types

`var body: some View`

The content and behavior of the scroll view.

## Relationships

### Conforms To

  * `View`

## See Also

### Creating a scroll view

`struct ScrollViewReader`

A view that provides programmatic scrolling, by working with a proxy to scroll
to known child views.

`struct ScrollViewProxy`

A proxy value that supports programmatic scrolling of the scrollable views
within a view hierarchy.

Structure

# ScrollViewReader

A view that provides programmatic scrolling, by working with a proxy to scroll
to known child views.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    @frozen
    struct ScrollViewReader<Content> where Content : View

## Overview

The scroll view reader’s content view builder receives a `ScrollViewProxy`
instance; you use the proxy’s `scrollTo(_:anchor:)` to perform scrolling.

The following example creates a `ScrollView` containing 100 views that
together display a color gradient. It also contains two buttons, one each at
the top and bottom. The top button tells the `ScrollViewProxy` to scroll to
the bottom button, and vice versa.

Important

You may not use the `ScrollViewProxy` during execution of the `content` view
builder; doing so results in a runtime error. Instead, only actions created
within `content` can call the proxy, such as gesture handlers or a view’s
`onChange(of:perform:)` method.

## Topics

### Creating a scroll view reader

`init(content: (ScrollViewProxy) -> Content)`

Creates an instance that can perform programmatic scrolling of its child
scroll views.

### Configuring a scroll view reader

`var content: (ScrollViewProxy) -> Content`

The view builder that creates the reader’s content.

## Relationships

### Conforms To

  * `View`

## See Also

### Creating a scroll view

`struct ScrollView`

A scrollable view.

`struct ScrollViewProxy`

A proxy value that supports programmatic scrolling of the scrollable views
within a view hierarchy.

Structure

# ScrollViewProxy

A proxy value that supports programmatic scrolling of the scrollable views
within a view hierarchy.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    struct ScrollViewProxy

## Overview

You don’t create instances of `ScrollViewProxy` directly. Instead, your
`ScrollViewReader` receives an instance of `ScrollViewProxy` in its `content`
view builder. You use actions within this view builder, such as button and
gesture handlers or the `onChange(of:perform:)` method, to call the proxy’s
`scrollTo(_:anchor:)` method.

## Topics

### Performing scrolling

`func scrollTo<ID>(ID, anchor: UnitPoint?)`

Scans all scroll views contained by the proxy for the first with a child view
with identifier `id`, and then scrolls to that view.

## See Also

### Creating a scroll view

`struct ScrollView`

A scrollable view.

`struct ScrollViewReader`

A view that provides programmatic scrolling, by working with a proxy to scroll
to known child views.

Instance Method

# scrollPosition(id:anchor:)

Associates a binding to be updated when a scroll view within this view
scrolls.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func scrollPosition(
        id: Binding<(some Hashable)?>,
        anchor: UnitPoint? = nil
    ) -> some View
    

## Discussion

Use this modifier along with the `View/scrollTargetLayout()` modifier to know
the identity of the view that is actively scrolled. As the scroll view
scrolls, the binding will be updated with the identity of the leading-most /
top-most view.

Use the `View/scrollTargetLayout()` modifier to configure which the layout
that contains your scroll targets. In the following example, the top-most
ItemView will update with the scrolledID binding as the scroll view scrolls.

You can write to the binding to scroll to the view with the provided identity.

SwiftUI will attempt to keep the view with the identity specified in the
provided binding when events occur that might cause it to be scrolled out of
view by the system. Some examples of these include:

  * The data backing the content of a scroll view is re-ordered.

  * The size of the scroll view changes, like when a window is resized on macOS or during a rotation on iOS.

  * The scroll view initially lays out it content defaulting to the top most view, but the binding has a different view’s identity.

You can provide an anchor to this modifier to both:

  * Influence which view the system chooses as the view whose identity value will update the providing binding as the scroll view scrolls.

  * Control the alignment of the view when scrolling to a view when writing a new binding value.

For example, providing a value of `bottom` will prefer to have the bottom-most
view chosen and prefer to scroll to views aligned to the bottom.

## See Also

### Managing scroll position

`func defaultScrollAnchor(UnitPoint?) -> some View`

Associates an anchor to control which part of the scroll view’s content should
be rendered by default.

Instance Method

# defaultScrollAnchor(_:)

Associates an anchor to control which part of the scroll view’s content should
be rendered by default.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func defaultScrollAnchor(_ anchor: UnitPoint?) -> some View
    

## Discussion

Use this modifier to specify an anchor to control both which part of the
scroll view’s content should be visible initially and how the scroll view
handles content size changes.

Provide a value of `UnitPoint/center`` to have the scroll view start in the
center of its content when a scroll view is scrollable in both axes.

Provide a value of `UnitPoint/bottom` to have the scroll view start at the
bottom of its content when scrollable in the vertical axis.

The user may scroll away from the initial defined scroll position. When the
content size of the scroll view changes, it may consult the anchor to know how
to reposition the content.

## See Also

### Managing scroll position

`func scrollPosition(id: Binding<(some Hashable)?>, anchor: UnitPoint?) ->
some View`

Associates a binding to be updated when a scroll view within this view
scrolls.

Instance Method

# scrollTargetBehavior(_:)

Sets the scroll behavior of views scrollable in the provided axes.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func scrollTargetBehavior(_ behavior: some ScrollTargetBehavior) -> some View
    

## Discussion

A scrollable view calculates where scroll gestures should end using its
deceleration rate and the state of its scroll gesture by default. A scroll
behavior allows for customizing this logic. You can provide your own
`ScrollTargetBehavior` or use one of the built in behaviors provided by
SwiftUI.

### Paging Behavior

SwiftUI offers a `PagingScrollTargetBehavior` behavior which uses the geometry
of the scroll view to decide where to allow scrolls to end.

In the following example, every view in the lazy stack is flexible in both
directions and the scroll view will settle to container aligned boundaries.

### View Aligned Behavior

SwiftUI offers a `ViewAlignedScrollTargetBehavior` scroll behavior that will
always settle on the geometry of individual views.

You configure which views should be used for settling using the
`scrollTargetLayout(isEnabled:)` modifier. Apply this modifier to a layout
container like `LazyVStack` or `HStack` and each individual view in that
layout will be considered for alignment.

## See Also

### Defining scroll targets

`func scrollTargetLayout(isEnabled: Bool) -> some View`

Configures the outermost layout as a scroll target layout.

`struct ScrollTarget`

A type defining the target in which a scroll view should try and scroll to.

`protocol ScrollTargetBehavior`

A type that defines the scroll behavior of a scrollable view.

`struct ScrollTargetBehaviorContext`

The context in which a scroll target behavior updates its scroll target.

`struct PagingScrollTargetBehavior`

The scroll behavior that aligns scroll targets to container-based geometry.

`struct ViewAlignedScrollTargetBehavior`

The scroll behavior that aligns scroll targets to view-based geometry.

Instance Method

# scrollTargetLayout(isEnabled:)

Configures the outermost layout as a scroll target layout.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func scrollTargetLayout(isEnabled: Bool = true) -> some View
    

## Discussion

This modifier works together with the `ViewAlignedScrollTargetBehavior` to
ensure that scroll views align to view based content.

Apply this modifier to layout containers like `LazyHStack` or `VStack` within
a `ScrollView` that contain the main repeating content of your `ScrollView`.

Scroll target layouts act as a convenience for applying a
`View/scrollTarget(isEnabled:)` modifier to each views in the layout.

A scroll target layout will ensure that any target layout nested within the
primary one will not also become a scroll target layout.

## See Also

### Defining scroll targets

`func scrollTargetBehavior(some ScrollTargetBehavior) -> some View`

Sets the scroll behavior of views scrollable in the provided axes.

`struct ScrollTarget`

A type defining the target in which a scroll view should try and scroll to.

`protocol ScrollTargetBehavior`

A type that defines the scroll behavior of a scrollable view.

`struct ScrollTargetBehaviorContext`

The context in which a scroll target behavior updates its scroll target.

`struct PagingScrollTargetBehavior`

The scroll behavior that aligns scroll targets to container-based geometry.

`struct ViewAlignedScrollTargetBehavior`

The scroll behavior that aligns scroll targets to view-based geometry.

Structure

# ScrollTarget

A type defining the target in which a scroll view should try and scroll to.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct ScrollTarget

## Topics

### Getting the scroll target

`var anchor: UnitPoint?`

The anchor to which the rect should be aligned within the visible region of
the scrollable view.

`var rect: CGRect`

The rect that a scrollable view should try and have contained.

## See Also

### Defining scroll targets

`func scrollTargetBehavior(some ScrollTargetBehavior) -> some View`

Sets the scroll behavior of views scrollable in the provided axes.

`func scrollTargetLayout(isEnabled: Bool) -> some View`

Configures the outermost layout as a scroll target layout.

`protocol ScrollTargetBehavior`

A type that defines the scroll behavior of a scrollable view.

`struct ScrollTargetBehaviorContext`

The context in which a scroll target behavior updates its scroll target.

`struct PagingScrollTargetBehavior`

The scroll behavior that aligns scroll targets to container-based geometry.

`struct ViewAlignedScrollTargetBehavior`

The scroll behavior that aligns scroll targets to view-based geometry.

Protocol

# ScrollTargetBehavior

A type that defines the scroll behavior of a scrollable view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    protocol ScrollTargetBehavior

## Overview

A scrollable view calculates where scroll gestures should end using its
deceleration rate and the state of its scroll gesture by default. A scroll
behavior allows for customizing this logic.

You define a scroll behavior using the `updateTarget(_:context:)` method.

Using this method, you can control where someone can scroll in a scrollable
view. For example, you can create a custom scroll behavior that aligns to
every 10 points by doing the following:

### Paging Behavior

SwiftUI offers built in scroll behaviors. One such behavior is the
`PagingScrollTargetBehavior` which uses the geometry of the scroll view to
decide where to allow scrolls to end.

In the following example, every view in the lazy stack is flexible in both
directions and the scroll view will settle to container aligned boundaries.

### View Aligned Behavior

SwiftUI also offers a `ViewAlignedScrollTargetBehavior` scroll behavior that
will always settle on the geometry of individual views.

You configure which views should be used for settling using the
`scrollTargetLayout(isEnabled:)` modifier. Apply this modifier to a layout
container like `LazyVStack` or `HStack` and each individual view in that
layout will be considered for alignment.

Use types conforming to this protocol with the `scrollTargetBehavior(_:)`
modifier.

## Topics

### Getting the scroll target behavior

`static var paging: PagingScrollTargetBehavior`

The scroll behavior that aligns scroll targets to container-based geometry.

Available when `Self` is `PagingScrollTargetBehavior`.

`static var viewAligned: ViewAlignedScrollTargetBehavior`

The scroll behavior that aligns scroll targets to view-based geometry.

Available when `Self` is `ViewAlignedScrollTargetBehavior`.

`static func viewAligned(limitBehavior:
ViewAlignedScrollTargetBehavior.LimitBehavior) -> Self`

The scroll behavior that aligns scroll targets to view-based geometry.

Available when `Self` is `ViewAlignedScrollTargetBehavior`.

### Updating the proposed target

`func updateTarget(inout ScrollTarget, context: Self.TargetContext)`

Updates the proposed target that a scrollable view should scroll to.

**Required**

` typealias TargetContext`

The context in which a scroll behavior updates the scroll target.

## Relationships

### Conforming Types

  * `PagingScrollTargetBehavior`
  * `ViewAlignedScrollTargetBehavior`

## See Also

### Defining scroll targets

`func scrollTargetBehavior(some ScrollTargetBehavior) -> some View`

Sets the scroll behavior of views scrollable in the provided axes.

`func scrollTargetLayout(isEnabled: Bool) -> some View`

Configures the outermost layout as a scroll target layout.

`struct ScrollTarget`

A type defining the target in which a scroll view should try and scroll to.

`struct ScrollTargetBehaviorContext`

The context in which a scroll target behavior updates its scroll target.

`struct PagingScrollTargetBehavior`

The scroll behavior that aligns scroll targets to container-based geometry.

`struct ViewAlignedScrollTargetBehavior`

The scroll behavior that aligns scroll targets to view-based geometry.

Structure

# ScrollTargetBehaviorContext

The context in which a scroll target behavior updates its scroll target.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    @dynamicMemberLookup
    struct ScrollTargetBehaviorContext

## Topics

### Getting the scroll target behavior context

`var axes: Axis.Set`

The axes in which the scrollable view is scrollable.

`var containerSize: CGSize`

The size of the container of the scrollable view.

`var contentSize: CGSize`

The size of the content of the scrollable view.

`var originalTarget: ScrollTarget`

The original target when the scroll gesture began.

`var velocity: CGVector`

The current velocity of the scrollable view’s scroll gesture.

### Accessing the context

`subscript<T>(dynamicMember _: KeyPath<EnvironmentValues, T>) -> T`

## See Also

### Defining scroll targets

`func scrollTargetBehavior(some ScrollTargetBehavior) -> some View`

Sets the scroll behavior of views scrollable in the provided axes.

`func scrollTargetLayout(isEnabled: Bool) -> some View`

Configures the outermost layout as a scroll target layout.

`struct ScrollTarget`

A type defining the target in which a scroll view should try and scroll to.

`protocol ScrollTargetBehavior`

A type that defines the scroll behavior of a scrollable view.

`struct PagingScrollTargetBehavior`

The scroll behavior that aligns scroll targets to container-based geometry.

`struct ViewAlignedScrollTargetBehavior`

The scroll behavior that aligns scroll targets to view-based geometry.

Structure

# PagingScrollTargetBehavior

The scroll behavior that aligns scroll targets to container-based geometry.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct PagingScrollTargetBehavior

## Overview

In the following example, every view in the lazy stack is flexible in both
directions and the scroll view settles to container-aligned boundaries.

## Topics

### Creating the target behavior

`init()`

Creates a paging scroll behavior.

## Relationships

### Conforms To

  * `ChartScrollTargetBehavior`
  * `ScrollTargetBehavior`

## See Also

### Defining scroll targets

`func scrollTargetBehavior(some ScrollTargetBehavior) -> some View`

Sets the scroll behavior of views scrollable in the provided axes.

`func scrollTargetLayout(isEnabled: Bool) -> some View`

Configures the outermost layout as a scroll target layout.

`struct ScrollTarget`

A type defining the target in which a scroll view should try and scroll to.

`protocol ScrollTargetBehavior`

A type that defines the scroll behavior of a scrollable view.

`struct ScrollTargetBehaviorContext`

The context in which a scroll target behavior updates its scroll target.

`struct ViewAlignedScrollTargetBehavior`

The scroll behavior that aligns scroll targets to view-based geometry.

Structure

# ViewAlignedScrollTargetBehavior

The scroll behavior that aligns scroll targets to view-based geometry.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct ViewAlignedScrollTargetBehavior

## Overview

You use this behavior when a scroll view should always align its scroll
targets to a rectangle that’s aligned to the geometry of a view. In the
following example, the scroll view always picks an item view to settle on.

You configure which views should be used for settling using the
`scrollTargetLayout(isEnabled:)` modifier. Apply this modifier to a layout
container like `LazyVStack` or `HStack` and each individual view in that
layout will be considered for alignment.

You can customize whether the view aligned behavior limits the number of views
that can be scrolled at a time by using the
`ViewAlignedScrollTargetBehavior.LimitBehavior` type. Provide a value of
`always` to always have the behavior only allow a few views to be scrolled at
a time.

By default, the view aligned behavior will limit the number of views it
scrolls when in a compact horizontal size class when scrollable in the
horizontal axis, when in a compact vertical size class when scrollable in the
vertical axis, and otherwise does not impose any limit on the number of views
that can be scrolled.

## Topics

### Creating the target behavior

`init(limitBehavior: ViewAlignedScrollTargetBehavior.LimitBehavior)`

Creates a view aligned scroll behavior.

`struct LimitBehavior`

A type that defines the amount of views that can be scrolled at a time.

## Relationships

### Conforms To

  * `ScrollTargetBehavior`

## See Also

### Defining scroll targets

`func scrollTargetBehavior(some ScrollTargetBehavior) -> some View`

Sets the scroll behavior of views scrollable in the provided axes.

`func scrollTargetLayout(isEnabled: Bool) -> some View`

Configures the outermost layout as a scroll target layout.

`struct ScrollTarget`

A type defining the target in which a scroll view should try and scroll to.

`protocol ScrollTargetBehavior`

A type that defines the scroll behavior of a scrollable view.

`struct ScrollTargetBehaviorContext`

The context in which a scroll target behavior updates its scroll target.

`struct PagingScrollTargetBehavior`

The scroll behavior that aligns scroll targets to container-based geometry.

Instance Method

# scrollTransition(_:axis:transition:)

Applies the given transition, animating between the phases of the transition
as this view appears and disappears within the visible region of the
containing scroll view, or other container specified using the
`coordinateSpace` parameter.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func scrollTransition(
        _ configuration: ScrollTransitionConfiguration = .interactive,
        axis: Axis? = nil,
        transition: @escaping (EmptyVisualEffect, ScrollTransitionPhase) -> some VisualEffect
    ) -> some View
    

##  Parameters

`configuration`

    

The configuration controlling how the transition will be applied. The
configuration will be applied both while the view is coming into view and
while it is disappearing (the transition is symmetrical).

`axis`

    

The axis of the containing scroll view over which the transition will be
applied. The default value of `nil` uses the axis of the innermost containing
scroll view, or `.vertical` if the innermost scroll view is scrollable along
both axes.

`coordinateSpace`

    

The coordinate space of the container that visibility is evaluated within.
Defaults to `.scrollView`.

`transition`

    

A closure that applies visual effects as a function of the provided phase.

## See Also

### Animating scroll transitions

`func scrollTransition(topLeading: ScrollTransitionConfiguration,
bottomTrailing: ScrollTransitionConfiguration, axis: Axis?, transition:
(EmptyVisualEffect, ScrollTransitionPhase) -> some VisualEffect) -> some View`

Applies the given transition, animating between the phases of the transition
as this view appears and disappears within the visible region of the
containing scroll view, or other container specified using the
`coordinateSpace` parameter.

`enum ScrollTransitionPhase`

The phases that a view transitions between when it scrolls among other views.

`struct ScrollTransitionConfiguration`

The configuration of a scroll transition that controls how a transition is
applied as a view is scrolled through the visible region of a containing
scroll view or other container.

Instance Method

# scrollTransition(topLeading:bottomTrailing:axis:transition:)

Applies the given transition, animating between the phases of the transition
as this view appears and disappears within the visible region of the
containing scroll view, or other container specified using the
`coordinateSpace` parameter.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func scrollTransition(
        topLeading: ScrollTransitionConfiguration,
        bottomTrailing: ScrollTransitionConfiguration,
        axis: Axis? = nil,
        transition: @escaping (EmptyVisualEffect, ScrollTransitionPhase) -> some VisualEffect
    ) -> some View
    

##  Parameters

`transition`

    

the transition to apply.

`topLeading`

    

The configuration that drives the transition when the view is about to appear
at the top edge of a vertical scroll view, or the leading edge of a horizont
scroll view.

`bottomTrailing`

    

The configuration that drives the transition when the view is about to appear
at the bottom edge of a vertical scroll view, or the trailing edge of a
horizont scroll view.

`axis`

    

The axis of the containing scroll view over which the transition will be
applied. The default value of `nil` uses the axis of the innermost containing
scroll view, or `.vertical` if the innermost scroll view is scrollable along
both axes.

`transition`

    

A closure that applies visual effects as a function of the provided phase.

## See Also

### Animating scroll transitions

`func scrollTransition(ScrollTransitionConfiguration, axis: Axis?, transition:
(EmptyVisualEffect, ScrollTransitionPhase) -> some VisualEffect) -> some View`

Applies the given transition, animating between the phases of the transition
as this view appears and disappears within the visible region of the
containing scroll view, or other container specified using the
`coordinateSpace` parameter.

`enum ScrollTransitionPhase`

The phases that a view transitions between when it scrolls among other views.

`struct ScrollTransitionConfiguration`

The configuration of a scroll transition that controls how a transition is
applied as a view is scrolled through the visible region of a containing
scroll view or other container.

Enumeration

# ScrollTransitionPhase

The phases that a view transitions between when it scrolls among other views.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    @frozen
    enum ScrollTransitionPhase

## Overview

When a view with a scroll transition modifier applied is approaching the
visible region of the containing scroll view or other container, the effect
will first be applied with the `topLeading` or `bottomTrailing` phase
(depending on which edge the view is approaching), then will be moved to the
`identity` phase as the view moves into the visible area. The timing and
behavior that determines when a view is visible within the container is
controlled by the configuration that is provided to the `scrollTransition`
modifier.

In the `identity` phase, scroll transitions should generally not make any
visual change to the view they are applied to, since the transition’s view
modifications in the `identity` phase will be applied to the view as long as
it is visible. In the `topLeading` and `bottomTrailing` phases, transitions
should apply a change that will be animated to create the transition.

## Topics

### Getting the phase

`case identity`

The scroll transition is being applied to a view that is in the visible area.

`case topLeading`

The scroll transition is being applied to a view that is about to move into
the visible area at the top edge of a vertical scroll view, or the leading
edge of a horizont scroll view.

`case bottomTrailing`

The scroll transition is being applied to a view that is about to move into
the visible area at the bottom edge of a vertical scroll view, or the trailing
edge of a horizontal scroll view.

### Accessing the phase state

`var isIdentity: Bool`

`var value: Double`

A phase-derived value that can be used to scale or otherwise modify effects.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`

## See Also

### Animating scroll transitions

`func scrollTransition(ScrollTransitionConfiguration, axis: Axis?, transition:
(EmptyVisualEffect, ScrollTransitionPhase) -> some VisualEffect) -> some View`

Applies the given transition, animating between the phases of the transition
as this view appears and disappears within the visible region of the
containing scroll view, or other container specified using the
`coordinateSpace` parameter.

`func scrollTransition(topLeading: ScrollTransitionConfiguration,
bottomTrailing: ScrollTransitionConfiguration, axis: Axis?, transition:
(EmptyVisualEffect, ScrollTransitionPhase) -> some VisualEffect) -> some View`

Applies the given transition, animating between the phases of the transition
as this view appears and disappears within the visible region of the
containing scroll view, or other container specified using the
`coordinateSpace` parameter.

`struct ScrollTransitionConfiguration`

The configuration of a scroll transition that controls how a transition is
applied as a view is scrolled through the visible region of a containing
scroll view or other container.

Structure

# ScrollTransitionConfiguration

The configuration of a scroll transition that controls how a transition is
applied as a view is scrolled through the visible region of a containing
scroll view or other container.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct ScrollTransitionConfiguration

## Topics

### Getting the configuration

`static let identity: ScrollTransitionConfiguration`

Creates a new configuration that does not change the appearance of the view.

`static let animated: ScrollTransitionConfiguration`

Creates a new configuration that discretely animates the transition when the
view becomes visible.

`static func animated(Animation) -> ScrollTransitionConfiguration`

Creates a new configuration that discretely animates the transition when the
view becomes visible.

`static let interactive: ScrollTransitionConfiguration`

Creates a new configuration that interactively interpolates the transition’s
effect as the view is scrolled into the visible region of the container.

`static func interactive(timingCurve: UnitCurve) ->
ScrollTransitionConfiguration`

Creates a new configuration that interactively interpolates the transition’s
effect as the view is scrolled into the visible region of the container.

### Accessing the configuration

`func animation(Animation) -> ScrollTransitionConfiguration`

Sets the animation with which the transition will be applied.

`func threshold(ScrollTransitionConfiguration.Threshold) ->
ScrollTransitionConfiguration`

Sets the threshold at which the view will be considered fully visible.

`struct Threshold`

Describes a specific point in the progression of a target view within a
container from hidden (fully outside the container) to visible.

## See Also

### Animating scroll transitions

`func scrollTransition(ScrollTransitionConfiguration, axis: Axis?, transition:
(EmptyVisualEffect, ScrollTransitionPhase) -> some VisualEffect) -> some View`

Applies the given transition, animating between the phases of the transition
as this view appears and disappears within the visible region of the
containing scroll view, or other container specified using the
`coordinateSpace` parameter.

`func scrollTransition(topLeading: ScrollTransitionConfiguration,
bottomTrailing: ScrollTransitionConfiguration, axis: Axis?, transition:
(EmptyVisualEffect, ScrollTransitionPhase) -> some VisualEffect) -> some View`

Applies the given transition, animating between the phases of the transition
as this view appears and disappears within the visible region of the
containing scroll view, or other container specified using the
`coordinateSpace` parameter.

`enum ScrollTransitionPhase`

The phases that a view transitions between when it scrolls among other views.

Instance Method

# scrollIndicatorsFlash(onAppear:)

Flashes the scroll indicators of a scrollable view when it appears.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func scrollIndicatorsFlash(onAppear: Bool) -> some View
    

##  Parameters

`onAppear`

    

A Boolean value that indicates whether the scroll indicators flash when the
scroll view appears.

## Return Value

A view that flashes any visible scroll indicators when it first appears.

## Discussion

Use this modifier to control whether the scroll indicators of a scroll view
briefly flash when the view first appears. For example, you can make the
indicators flash by setting the `onAppear` parameter to `true`:

Only scroll indicators that you configure to be visible flash. To flash scroll
indicators when a value changes, use `scrollIndicatorsFlash(trigger:)`
instead.

## See Also

### Showing scroll indicators

`func scrollIndicatorsFlash(trigger: some Equatable) -> some View`

Flashes the scroll indicators of scrollable views when a value changes.

`func scrollIndicators(ScrollIndicatorVisibility, axes: Axis.Set) -> some
View`

Sets the visibility of scroll indicators within this view.

`var horizontalScrollIndicatorVisibility: ScrollIndicatorVisibility`

The visibility to apply to scroll indicators of any horizontally scrollable
content.

`var verticalScrollIndicatorVisibility: ScrollIndicatorVisibility`

The visiblity to apply to scroll indicators of any vertically scrollable
content.

`struct ScrollIndicatorVisibility`

The visibility of scroll indicators of a UI element.

Instance Method

# scrollIndicatorsFlash(trigger:)

Flashes the scroll indicators of scrollable views when a value changes.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func scrollIndicatorsFlash(trigger value: some Equatable) -> some View
    

##  Parameters

`value`

    

The value that causes scroll indicators to flash. The value must conform to
the `Equatable` protocol.

## Return Value

A view that flashes any visible scroll indicators when a value changes.

## Discussion

When the value that you provide to this modifier changes, the scroll
indicators of any scrollable views within the modified view hierarchy briefly
flash. The following example configures the scroll indicators to flash any
time `flashCount` changes:

Only scroll indicators that you configure to be visible flash. To flash scroll
indicators when a scroll view initially appears, use
`scrollIndicatorsFlash(onAppear:)` instead.

## See Also

### Showing scroll indicators

`func scrollIndicatorsFlash(onAppear: Bool) -> some View`

Flashes the scroll indicators of a scrollable view when it appears.

`func scrollIndicators(ScrollIndicatorVisibility, axes: Axis.Set) -> some
View`

Sets the visibility of scroll indicators within this view.

`var horizontalScrollIndicatorVisibility: ScrollIndicatorVisibility`

The visibility to apply to scroll indicators of any horizontally scrollable
content.

`var verticalScrollIndicatorVisibility: ScrollIndicatorVisibility`

The visiblity to apply to scroll indicators of any vertically scrollable
content.

`struct ScrollIndicatorVisibility`

The visibility of scroll indicators of a UI element.

Instance Method

# scrollIndicators(_:axes:)

Sets the visibility of scroll indicators within this view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func scrollIndicators(
        _ visibility: ScrollIndicatorVisibility,
        axes: Axis.Set = [.vertical, .horizontal]
    ) -> some View
    

##  Parameters

`visibility`

    

The visibility to apply to scrollable views.

`axes`

    

The axes of scrollable views that the visibility applies to.

## Return Value

A view with the specified scroll indicator visibility.

## Discussion

Use this modifier to hide or show scroll indicators on scrollable content in
views like a `ScrollView`, `List`, or `TextEditor`. This modifier applies the
prefered visibility to any scrollable content within a view hierarchy.

Use the `hidden` value to indicate that you prefer that views never show
scroll indicators along a given axis. Use `visible` when you prefer that views
show scroll indicators. Depending on platform conventions, visible scroll
indicators might only appear while scrolling. Pass `automatic` to allow views
to decide whether or not to show their indicators.

## See Also

### Showing scroll indicators

`func scrollIndicatorsFlash(onAppear: Bool) -> some View`

Flashes the scroll indicators of a scrollable view when it appears.

`func scrollIndicatorsFlash(trigger: some Equatable) -> some View`

Flashes the scroll indicators of scrollable views when a value changes.

`var horizontalScrollIndicatorVisibility: ScrollIndicatorVisibility`

The visibility to apply to scroll indicators of any horizontally scrollable
content.

`var verticalScrollIndicatorVisibility: ScrollIndicatorVisibility`

The visiblity to apply to scroll indicators of any vertically scrollable
content.

`struct ScrollIndicatorVisibility`

The visibility of scroll indicators of a UI element.

Instance Property

# horizontalScrollIndicatorVisibility

The visibility to apply to scroll indicators of any horizontally scrollable
content.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var horizontalScrollIndicatorVisibility: ScrollIndicatorVisibility { get set }

## See Also

### Showing scroll indicators

`func scrollIndicatorsFlash(onAppear: Bool) -> some View`

Flashes the scroll indicators of a scrollable view when it appears.

`func scrollIndicatorsFlash(trigger: some Equatable) -> some View`

Flashes the scroll indicators of scrollable views when a value changes.

`func scrollIndicators(ScrollIndicatorVisibility, axes: Axis.Set) -> some
View`

Sets the visibility of scroll indicators within this view.

`var verticalScrollIndicatorVisibility: ScrollIndicatorVisibility`

The visiblity to apply to scroll indicators of any vertically scrollable
content.

`struct ScrollIndicatorVisibility`

The visibility of scroll indicators of a UI element.

Instance Property

# verticalScrollIndicatorVisibility

The visiblity to apply to scroll indicators of any vertically scrollable
content.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var verticalScrollIndicatorVisibility: ScrollIndicatorVisibility { get set }

## See Also

### Showing scroll indicators

`func scrollIndicatorsFlash(onAppear: Bool) -> some View`

Flashes the scroll indicators of a scrollable view when it appears.

`func scrollIndicatorsFlash(trigger: some Equatable) -> some View`

Flashes the scroll indicators of scrollable views when a value changes.

`func scrollIndicators(ScrollIndicatorVisibility, axes: Axis.Set) -> some
View`

Sets the visibility of scroll indicators within this view.

`var horizontalScrollIndicatorVisibility: ScrollIndicatorVisibility`

The visibility to apply to scroll indicators of any horizontally scrollable
content.

`struct ScrollIndicatorVisibility`

The visibility of scroll indicators of a UI element.

Structure

# ScrollIndicatorVisibility

The visibility of scroll indicators of a UI element.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    struct ScrollIndicatorVisibility

## Overview

Pass a value of this type to the `scrollIndicators(_:axes:)` method to specify
the preferred scroll indicator visibility of a view hierarchy.

## Topics

### Getting visibilties

`static var automatic: ScrollIndicatorVisibility`

Scroll indicator visibility depends on the policies of the component accepting
the visibility configuration.

`static var hidden: ScrollIndicatorVisibility`

Hide the scroll indicators.

`static var never: ScrollIndicatorVisibility`

Scroll indicators should never be visible.

`static var visible: ScrollIndicatorVisibility`

Show the scroll indicators.

## Relationships

### Conforms To

  * `Equatable`

## See Also

### Showing scroll indicators

`func scrollIndicatorsFlash(onAppear: Bool) -> some View`

Flashes the scroll indicators of a scrollable view when it appears.

`func scrollIndicatorsFlash(trigger: some Equatable) -> some View`

Flashes the scroll indicators of scrollable views when a value changes.

`func scrollIndicators(ScrollIndicatorVisibility, axes: Axis.Set) -> some
View`

Sets the visibility of scroll indicators within this view.

`var horizontalScrollIndicatorVisibility: ScrollIndicatorVisibility`

The visibility to apply to scroll indicators of any horizontally scrollable
content.

`var verticalScrollIndicatorVisibility: ScrollIndicatorVisibility`

The visiblity to apply to scroll indicators of any vertically scrollable
content.

Instance Method

# scrollContentBackground(_:)

Specifies the visibility of the background for scrollable views within this
view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    func scrollContentBackground(_ visibility: Visibility) -> some View
    

##  Parameters

`visibility`

    

the visibility to use for the background.

## Discussion

The following example hides the standard system background of the List.

## See Also

### Managing content visibility

`func scrollClipDisabled(Bool) -> some View`

Sets whether a scroll view clips its content to its bounds.

Instance Method

# scrollClipDisabled(_:)

Sets whether a scroll view clips its content to its bounds.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func scrollClipDisabled(_ disabled: Bool = true) -> some View
    

##  Parameters

`disabled`

    

A Boolean value that specifies whether to disable scroll view clipping.

## Return Value

A view that disables or enables scroll view clipping.

## Discussion

By default, a scroll view clips its content to its bounds, but you can disable
that behavior by using this modifier. For example, if the views inside the
scroll view have shadows that extend beyond the bounds of the scroll view, you
can use this modifier to avoid clipping the shadows:

The scroll view in the above example clips when the content view’s `disabled`
input is `false`, as it does if you omit the modifier, but not when the input
is `true`:

  * True 
  * False 

While you might want to avoid clipping parts of views that exceed the bounds
of the scroll view, like the shadows in the above example, you typically still
want the scroll view to clip at some point. Create custom clipping by using
the `clipShape(_:style:)` modifier to add a different clip shape. The
following code disables the default clipping and then adds rectangular
clipping that exceeds the bounds of the scroll view by the default padding
amount:

## See Also

### Managing content visibility

`func scrollContentBackground(Visibility) -> some View`

Specifies the visibility of the background for scrollable views within this
view.

Instance Method

# scrollDisabled(_:)

Disables or enables scrolling in scrollable views.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func scrollDisabled(_ disabled: Bool) -> some View
    

##  Parameters

`disabled`

    

A Boolean that indicates whether scrolling is disabled.

## Discussion

Use this modifier to control whether a `ScrollView` can scroll:

SwiftUI passes the disabled property through the environment, which means you
can use this modifier to disable scrolling for all scroll views within a view
hierarchy. In the following example, the modifier affects both scroll views:

You can also use this modifier to disable scrolling for other kinds of
scrollable views, like a `List` or a `TextEditor`.

## See Also

### Disabling scrolling

`var isScrollEnabled: Bool`

A Boolean value that indicates whether any scroll views associated with this
environment allow scrolling to occur.

Instance Property

# isScrollEnabled

A Boolean value that indicates whether any scroll views associated with this
environment allow scrolling to occur.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var isScrollEnabled: Bool { get set }

## Discussion

The default value is `true`. Use the `scrollDisabled(_:)` modifier to
configure this property.

## See Also

### Disabling scrolling

`func scrollDisabled(Bool) -> some View`

Disables or enables scrolling in scrollable views.

Instance Method

# scrollBounceBehavior(_:axes:)

Configures the bounce behavior of scrollable views along the specified axis.

iOS 16.4+  iPadOS 16.4+  macOS 13.3+  Mac Catalyst 16.4+  tvOS 16.4+  watchOS
9.4+  visionOS 1.0+

    
    
    func scrollBounceBehavior(
        _ behavior: ScrollBounceBehavior,
        axes: Axis.Set = [.vertical]
    ) -> some View
    

##  Parameters

`behavior`

    

The bounce behavior to apply to any scrollable views within the configured
view. Use one of the `ScrollBounceBehavior` values.

`axes`

    

The set of axes to apply `behavior` to. The default is `Axis.vertical`.

## Return Value

A view that’s configured with the specified scroll bounce behavior.

## Discussion

Use this modifier to indicate whether scrollable views bounce when people
scroll to the end of the view’s content, taking into account the relative
sizes of the view and its content. For example, the following `ScrollView`
only enables bounce behavior if its content is large enough to require
scrolling:

The modifier passes the scroll bounce mode through the `Environment`, which
means that the mode affects any scrollable views in the modified view
hierarchy. Provide an axis to the modifier to constrain the kinds of
scrollable views that the mode affects. For example, all the scroll views in
the following example can access the mode value, but only the two nested
scroll views are affected, because only they use horizontal scrolling:

You can use this modifier to configure any kind of scrollable view, including
`ScrollView`, `List`, `Table`, and `TextEditor`:

## See Also

### Configuring scroll bounce behavior

`var horizontalScrollBounceBehavior: ScrollBounceBehavior`

The scroll bounce mode for the horizontal axis of scrollable views.

`var verticalScrollBounceBehavior: ScrollBounceBehavior`

The scroll bounce mode for the vertical axis of scrollable views.

`struct ScrollBounceBehavior`

The ways that a scrollable view can bounce when it reaches the end of its
content.

Instance Property

# horizontalScrollBounceBehavior

The scroll bounce mode for the horizontal axis of scrollable views.

iOS 16.4+  iPadOS 16.4+  macOS 13.3+  Mac Catalyst 16.4+  tvOS 16.4+  watchOS
9.4+  visionOS 1.0+

    
    
    var horizontalScrollBounceBehavior: ScrollBounceBehavior { get set }

## Discussion

Use the `scrollBounceBehavior(_:axes:)` view modifier to set this value in the
`Environment`.

## See Also

### Configuring scroll bounce behavior

`func scrollBounceBehavior(ScrollBounceBehavior, axes: Axis.Set) -> some View`

Configures the bounce behavior of scrollable views along the specified axis.

`var verticalScrollBounceBehavior: ScrollBounceBehavior`

The scroll bounce mode for the vertical axis of scrollable views.

`struct ScrollBounceBehavior`

The ways that a scrollable view can bounce when it reaches the end of its
content.

Instance Property

# verticalScrollBounceBehavior

The scroll bounce mode for the vertical axis of scrollable views.

iOS 16.4+  iPadOS 16.4+  macOS 13.3+  Mac Catalyst 16.4+  tvOS 16.4+  watchOS
9.4+  visionOS 1.0+

    
    
    var verticalScrollBounceBehavior: ScrollBounceBehavior { get set }

## Discussion

Use the `scrollBounceBehavior(_:axes:)` view modifier to set this value in the
`Environment`.

## See Also

### Configuring scroll bounce behavior

`func scrollBounceBehavior(ScrollBounceBehavior, axes: Axis.Set) -> some View`

Configures the bounce behavior of scrollable views along the specified axis.

`var horizontalScrollBounceBehavior: ScrollBounceBehavior`

The scroll bounce mode for the horizontal axis of scrollable views.

`struct ScrollBounceBehavior`

The ways that a scrollable view can bounce when it reaches the end of its
content.

Structure

# ScrollBounceBehavior

The ways that a scrollable view can bounce when it reaches the end of its
content.

iOS 16.4+  iPadOS 16.4+  macOS 13.3+  Mac Catalyst 16.4+  tvOS 16.4+  watchOS
9.4+  visionOS 1.0+

    
    
    struct ScrollBounceBehavior

## Overview

Use the `scrollBounceBehavior(_:axes:)` view modifier to set a value of this
type for a scrollable view, like a `ScrollView` or a `List`. The value
configures the bounce behavior when people scroll to the end of the view’s
content.

You can configure each scrollable axis to use a different bounce mode.

## Topics

### Bounce behaviors

`static var automatic: ScrollBounceBehavior`

The automatic behavior.

`static var always: ScrollBounceBehavior`

The scrollable view always bounces.

`static var basedOnSize: ScrollBounceBehavior`

The scrollable view bounces when its content is large enough to require
scrolling.

## Relationships

### Conforms To

  * `Sendable`

## See Also

### Configuring scroll bounce behavior

`func scrollBounceBehavior(ScrollBounceBehavior, axes: Axis.Set) -> some View`

Configures the bounce behavior of scrollable views along the specified axis.

`var horizontalScrollBounceBehavior: ScrollBounceBehavior`

The scroll bounce mode for the horizontal axis of scrollable views.

`var verticalScrollBounceBehavior: ScrollBounceBehavior`

The scroll bounce mode for the vertical axis of scrollable views.

Instance Method

# scrollDismissesKeyboard(_:)

Configures the behavior in which scrollable content interacts with the
software keyboard.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+

    
    
    func scrollDismissesKeyboard(_ mode: ScrollDismissesKeyboardMode) -> some View
    

##  Parameters

`mode`

    

The keyboard dismissal mode that scrollable content uses.

## Return Value

A view that uses the specified keyboard dismissal mode.

## Discussion

You use this modifier to customize how scrollable content interacts with the
software keyboard. For example, you can specify a value of `immediately` to
indicate that you would like scrollable content to immediately dismiss the
keyboard if present when a scroll drag gesture begins.

You can also use this modifier to customize the keyboard dismissal behavior
for other kinds of scrollable views, like a `List` or a `TextEditor`.

By default, a `TextEditor` is interactive while other kinds of scrollable
content always dismiss the keyboard on a scroll when linked against iOS 16 or
later. Pass a value of `never` to indicate that scrollable content should
never automatically dismiss the keyboard.

## See Also

### Interacting with a software keyboard

`var scrollDismissesKeyboardMode: ScrollDismissesKeyboardMode`

The way that scrollable content interacts with the software keyboard.

`struct ScrollDismissesKeyboardMode`

The ways that scrollable content can interact with the software keyboard.

Instance Property

# scrollDismissesKeyboardMode

The way that scrollable content interacts with the software keyboard.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+

    
    
    var scrollDismissesKeyboardMode: ScrollDismissesKeyboardMode { get set }

## Discussion

The default value is `automatic`. Use the `scrollDismissesKeyboard(_:)`
modifier to configure this property.

## See Also

### Interacting with a software keyboard

`func scrollDismissesKeyboard(ScrollDismissesKeyboardMode) -> some View`

Configures the behavior in which scrollable content interacts with the
software keyboard.

`struct ScrollDismissesKeyboardMode`

The ways that scrollable content can interact with the software keyboard.

Structure

# ScrollDismissesKeyboardMode

The ways that scrollable content can interact with the software keyboard.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+

    
    
    struct ScrollDismissesKeyboardMode

## Overview

Use this type in a call to the `scrollDismissesKeyboard(_:)` modifier to
specify the dismissal behavior of scrollable views.

## Topics

### Getting modes

`static var automatic: ScrollDismissesKeyboardMode`

Determine the mode automatically based on the surrounding context.

`static var immediately: ScrollDismissesKeyboardMode`

Dismiss the keyboard as soon as scrolling starts.

`static var interactively: ScrollDismissesKeyboardMode`

Enable people to interactively dismiss the keyboard as part of the scroll
operation.

`static var never: ScrollDismissesKeyboardMode`

Never dismiss the keyboard automatically as a result of scrolling.

## Relationships

### Conforms To

  * `Sendable`

## See Also

### Interacting with a software keyboard

`func scrollDismissesKeyboard(ScrollDismissesKeyboardMode) -> some View`

Configures the behavior in which scrollable content interacts with the
software keyboard.

`var scrollDismissesKeyboardMode: ScrollDismissesKeyboardMode`

The way that scrollable content interacts with the software keyboard.

