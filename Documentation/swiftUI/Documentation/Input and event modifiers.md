Instance Method

# disabled(_:)

Adds a condition that controls whether users can interact with this view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func disabled(_ disabled: Bool) -> some View
    

##  Parameters

`disabled`

    

A Boolean value that determines whether users can interact with this view.

## Return Value

A view that controls whether users can interact with this view.

## Discussion

The higher views in a view hierarchy can override the value you set on this
view. In the following example, the button isn’t interactive because the outer
`disabled(_:)` modifier overrides the inner one:

## See Also

### Managing view interaction

`var isEnabled: Bool`

A Boolean value that indicates whether the view associated with this
environment allows user interaction.

`func interactionActivityTrackingTag(String) -> some View`

Sets a tag that you use for tracking interactivity.

`func invalidatableContent(Bool) -> some View`

Mark the receiver as their content might be invalidated.

Instance Method

# interactionActivityTrackingTag(_:)

Sets a tag that you use for tracking interactivity.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func interactionActivityTrackingTag(_ tag: String) -> some View
    

##  Parameters

`tag`

    

The tag used to track user interactions hosted by this view as activities.

## Return Value

A view that uses a tracking tag.

## Discussion

The following example tracks the scrolling activity of a `List`:

The resolved activity tracking tag is additive, so using the modifier across
the view hierarchy builds the tag from top to bottom. The example below shows
a hierarchical usage of this modifier with the resulting tag `Home-Feed`:

## See Also

### Managing view interaction

`func disabled(Bool) -> some View`

Adds a condition that controls whether users can interact with this view.

`var isEnabled: Bool`

A Boolean value that indicates whether the view associated with this
environment allows user interaction.

`func invalidatableContent(Bool) -> some View`

Mark the receiver as their content might be invalidated.

Instance Method

# swipeActions(edge:allowsFullSwipe:content:)

Adds custom swipe actions to a row in a list.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  watchOS 8.0+
visionOS 1.0+

    
    
    func swipeActions<T>(
        edge: HorizontalEdge = .trailing,
        allowsFullSwipe: Bool = true,
        @ViewBuilder content: () -> T
    ) -> some View where T : View
    

##  Parameters

`edge`

    

The edge of the view to associate the swipe actions with. The default is
`HorizontalEdge.trailing`.

`allowsFullSwipe`

    

A Boolean value that indicates whether a full swipe automatically performs the
first action. The default is `true`.

`content`

    

The content of the swipe actions.

## Discussion

Use this method to add swipe actions to a view that acts as a row in a list.
Indicate the `HorizontalEdge` where the swipe action originates, and define
individual actions with `Button` instances. For example, if you have a list of
messages, you can add an action to toggle a message as unread on a swipe from
the leading edge, and actions to delete or flag messages on a trailing edge
swipe:

Actions appear in the order you list them, starting from the swipe’s
originating edge. In the example above, the Delete action appears closest to
the screen’s trailing edge:

For labels or images that appear in swipe actions, SwiftUI automatically
applies the `fill` symbol variant, as shown above.

By default, the user can perform the first action for a given swipe direction
with a full swipe. For the example above, the user can perform both the toggle
unread and delete actions with full swipes. You can opt out of this behavior
for an edge by setting the `allowsFullSwipe` parameter to `false`. For
example, you can disable the full swipe on the leading edge:

When you set a role for a button using one of the values from the `ButtonRole`
enumeration, SwiftUI styles the button according to its role. In the example
above, the delete action appears in `red` because it has the `destructive`
role. If you want to set a different color — for example, to match the overall
theme of your app’s UI — add the `View/tint(_:)` modifier to the button:

The modifications in the code above make the toggle unread action `blue` and
the flag action `orange`:

When you add swipe actions, SwiftUI no longer synthesizes the Delete actions
that otherwise appear when using the `ForEach/onDelete(perform:)` method on a
`ForEach` instance. You become responsible for creating a Delete action, if
appropriate, among your swipe actions.

Actions accumulate for a given edge if you call the modifier multiple times on
the same list row view.

## See Also

### Configuring interaction

`func selectionDisabled(Bool) -> some View`

Adds a condition that controls whether users can select this view.

Instance Method

# refreshable(action:)

Marks this view as refreshable.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func refreshable(action: @escaping () async -> Void) -> some View
    

##  Parameters

`action`

    

An asynchronous handler that SwiftUI executes when the user requests a
refresh. Use this handler to initiate an update of model data displayed in the
modified view. Use `await` in front of any asynchronous calls inside the
handler.

## Return Value

A view with a new refresh action in its environment.

## Discussion

Apply this modifier to a view to set the `refresh` value in the view’s
environment to a `RefreshAction` instance that uses the specified `action` as
its handler. Views that detect the presence of the instance can change their
appearance to provide a way for the user to execute the handler.

For example, when you apply this modifier on iOS and iPadOS to a `List`, the
list enables a standard pull-to-refresh gesture that refreshes the list
contents. When the user drags the top of the scrollable area downward, the
view reveals a progress indicator and executes the specified handler. The
indicator remains visible for the duration of the refresh, which runs
asynchronously:

You can add refresh capability to your own views as well. For information on
how to do that, see `RefreshAction`.

## See Also

### Refreshing a list’s content

`var refresh: RefreshAction?`

A refresh action stored in a view’s environment.

`struct RefreshAction`

An action that initiates a refresh operation.

Instance Method

# selectionDisabled(_:)

Adds a condition that controls whether users can select this view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func selectionDisabled(_ isDisabled: Bool = true) -> some View
    

##  Parameters

`isDisabled`

    

A Boolean value that determines whether users can select this view.

## Discussion

Use this modifier to control the selectability of views in selectable
containers like `List` or `Table`. In the example, below, the user can’t
select the first item in the list.

You can also use this modifier to specify the selectability of views within a
`Picker`. The following example represents a flavor picker that disables
selection on flavors that are unavailable.

## See Also

### Configuring interaction

`func swipeActions<T>(edge: HorizontalEdge, allowsFullSwipe: Bool, content: ()
-> T) -> some View`

Adds custom swipe actions to a row in a list.

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

    
    
    ScrollView([.horizontal, .vertical]) {
        // initially centered content
    }
    .defaultScrollAnchor(.center)
    

Provide a value of `UnitPoint/bottom` to have the scroll view start at the
bottom of its content when scrollable in the vertical axis.

    
    
    @Binding var items: [Item]
    @Binding var scrolledID: Item.ID?
    
    
    ScrollView {
        LazyVStack {
            ForEach(items) { item in
                ItemView(item)
            }
        }
    }
    .defaultScrollAnchor(.bottom)
    

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

    
    
    ScrollView {
        LazyVStack(spacing: 0.0) {
            ForEach(items) { item in
                FullScreenItem(item)
            }
        }
    }
    .scrollTargetBehavior(.paging)
    

### View Aligned Behavior

SwiftUI offers a `ViewAlignedScrollTargetBehavior` scroll behavior that will
always settle on the geometry of individual views.

    
    
    ScrollView(.horizontal) {
        LazyHStack(spacing: 10.0) {
            ForEach(items) { item in
                ItemView(item)
            }
        }
        .scrollTargetLayout()
    }
    .scrollTargetBehavior(.viewAligned)
    .safeAreaPadding(.horizontal, 20.0)
    

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

Instance Method

# onTapGesture(count:perform:)

Adds an action to perform when this view recognizes a tap gesture.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 16.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func onTapGesture(
        count: Int = 1,
        perform action: @escaping () -> Void
    ) -> some View
    

##  Parameters

`count`

    

The number of taps or clicks required to trigger the action closure provided
in `action`. Defaults to `1`.

`action`

    

The action to perform.

## Discussion

Use this method to perform the specified `action` when the user clicks or taps
on the view or container `count` times.

Note

If you create a control that’s functionally equivalent to a `Button`, use
`ButtonStyle` to create a customized button instead.

In the example below, the color of the heart images changes to a random color
from the `colors` array whenever the user clicks or taps on the view twice:

    
    
    struct TapGestureExample: View {
        let colors: [Color] = [.gray, .red, .orange, .yellow,
                               .green, .blue, .purple, .pink]
        @State private var fgColor: Color = .gray
    
    
        var body: some View {
            Image(systemName: "heart.fill")
                .resizable()
                .frame(width: 200, height: 200)
                .foregroundColor(fgColor)
                .onTapGesture(count: 2) {
                    fgColor = colors.randomElement()!
                }
        }
    }
    

## See Also

### Recognizing tap gestures

`func onTapGesture(count: Int, coordinateSpace: some CoordinateSpaceProtocol,
perform: (CGPoint) -> Void) -> some View`

Adds an action to perform when this view recognizes a tap gesture, and
provides the action with the location of the interaction.

`struct TapGesture`

A gesture that recognizes one or more taps.

`struct SpatialTapGesture`

A gesture that recognizes one or more taps and reports their location.

Instance Method

# onTapGesture(count:coordinateSpace:perform:)

Adds an action to perform when this view recognizes a tap gesture, and
provides the action with the location of the interaction.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  watchOS 10.0+
visionOS 1.0+

    
    
    func onTapGesture(
        count: Int = 1,
        coordinateSpace: some CoordinateSpaceProtocol = .local,
        perform action: @escaping (CGPoint) -> Void
    ) -> some View
    

##  Parameters

`count`

    

The number of taps or clicks required to trigger the action closure provided
in `action`. Defaults to `1`.

`coordinateSpace`

    

The coordinate space in which to receive location values. Defaults to
`CoordinateSpace.local`.

`action`

    

The action to perform. This closure receives an input that indicates where the
interaction occurred.

## Discussion

Use this method to perform the specified `action` when the user clicks or taps
on the modified view `count` times. The action closure receives the location
of the interaction.

Note

If you create a control that’s functionally equivalent to a `Button`, use
`ButtonStyle` to create a customized button instead.

The following code adds a tap gesture to a `Circle` that toggles the color of
the circle based on the tap location.

## See Also

### Recognizing tap gestures

`func onTapGesture(count: Int, perform: () -> Void) -> some View`

Adds an action to perform when this view recognizes a tap gesture.

`struct TapGesture`

A gesture that recognizes one or more taps.

`struct SpatialTapGesture`

A gesture that recognizes one or more taps and reports their location.

Instance Method

#
onLongPressGesture(minimumDuration:maximumDistance:perform:onPressingChanged:)

Adds an action to perform when this view recognizes a long press gesture.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    func onLongPressGesture(
        minimumDuration: Double = 0.5,
        maximumDistance: CGFloat = 10,
        perform action: @escaping () -> Void,
        onPressingChanged: ((Bool) -> Void)? = nil
    ) -> some View
    

##  Parameters

`minimumDuration`

    

The minimum duration of the long press that must elapse before the gesture
succeeds.

`maximumDistance`

    

The maximum distance that the fingers or cursor performing the long press can
move before the gesture fails.

`action`

    

The action to perform when a long press is recognized.

`onPressingChanged`

    

A closure to run when the pressing state of the gesture changes, passing the
current state as a parameter.

## See Also

### Recognizing long press gestures

`func onLongPressGesture(minimumDuration: Double, perform: () -> Void,
onPressingChanged: ((Bool) -> Void)?) -> some View`

Adds an action to perform when this view recognizes a long press gesture.

`func onLongTouchGesture(minimumDuration: Double, perform: () -> Void,
onTouchingChanged: ((Bool) -> Void)?) -> some View`

Adds an action to perform when this view recognizes a remote long touch
gesture. A long touch gesture is when the finger is on the remote touch
surface without actually pressing.

`struct LongPressGesture`

A gesture that succeeds when the user performs a long press.

Instance Method

# onLongPressGesture(minimumDuration:perform:onPressingChanged:)

Adds an action to perform when this view recognizes a long press gesture.

tvOS 14.0+

    
    
    func onLongPressGesture(
        minimumDuration: Double = 0.5,
        perform action: @escaping () -> Void,
        onPressingChanged: ((Bool) -> Void)? = nil
    ) -> some View
    

##  Parameters

`minimumDuration`

    

The minimum duration of the long press that must elapse before the gesture
succeeds.

`action`

    

The action to perform when a long press is recognized.

`onPressingChanged`

    

A closure to run when the pressing state of the gesture changes, passing the
current state as a parameter.

## See Also

### Recognizing long press gestures

`func onLongPressGesture(minimumDuration: Double, maximumDistance: CGFloat,
perform: () -> Void, onPressingChanged: ((Bool) -> Void)?) -> some View`

Adds an action to perform when this view recognizes a long press gesture.

`func onLongTouchGesture(minimumDuration: Double, perform: () -> Void,
onTouchingChanged: ((Bool) -> Void)?) -> some View`

Adds an action to perform when this view recognizes a remote long touch
gesture. A long touch gesture is when the finger is on the remote touch
surface without actually pressing.

`struct LongPressGesture`

A gesture that succeeds when the user performs a long press.

Instance Method

# onLongTouchGesture(minimumDuration:perform:onTouchingChanged:)

Adds an action to perform when this view recognizes a remote long touch
gesture. A long touch gesture is when the finger is on the remote touch
surface without actually pressing.

tvOS 16.0+

    
    
    func onLongTouchGesture(
        minimumDuration: Double = 0.5,
        perform action: @escaping () -> Void,
        onTouchingChanged: ((Bool) -> Void)? = nil
    ) -> some View
    

##  Parameters

`minimumDuration`

    

The minimum duration of the long touch that must elapse before the gesture
succeeds.

`action`

    

The action to perform when a long touch is recognized

`onTouchingChanged`

    

A closure to run when the touching state of the gesture changes, passing the
current state as a parameter.

## See Also

### Recognizing long press gestures

`func onLongPressGesture(minimumDuration: Double, maximumDistance: CGFloat,
perform: () -> Void, onPressingChanged: ((Bool) -> Void)?) -> some View`

Adds an action to perform when this view recognizes a long press gesture.

`func onLongPressGesture(minimumDuration: Double, perform: () -> Void,
onPressingChanged: ((Bool) -> Void)?) -> some View`

Adds an action to perform when this view recognizes a long press gesture.

`struct LongPressGesture`

A gesture that succeeds when the user performs a long press.

Instance Method

# gesture(_:including:)

Attaches a gesture to the view with a lower precedence than gestures defined
by the view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func gesture<T>(
        _ gesture: T,
        including mask: GestureMask = .all
    ) -> some View where T : Gesture
    

##  Parameters

`gesture`

    

A gesture to attach to the view.

`mask`

    

A value that controls how adding this gesture to the view affects other
gestures recognized by the view and its subviews. Defaults to `all`.

## Discussion

Use this method when you need to attach a gesture to a view. The example below
defines a custom gesture that prints a message to the console and attaches it
to the view’s `VStack`. Inside the `VStack` a red heart `Image` defines its
own `TapGesture` handler that also prints a message to the console, and blue
rectangle with no custom gesture handlers. Tapping or clicking the image
prints a message to the console from the tap gesture handler on the image,
while tapping or clicking the rectangle inside the `VStack` prints a message
in the console from the enclosing vertical stack gesture handler.

    
    
    struct GestureExample: View {
        @State private var message = "Message"
        let newGesture = TapGesture().onEnded {
            print("Tap on VStack.")
        }
    
    
        var body: some View {
            VStack(spacing:25) {
                Image(systemName: "heart.fill")
                    .resizable()
                    .frame(width: 75, height: 75)
                    .padding()
                    .foregroundColor(.red)
                    .onTapGesture {
                        print("Tap on image.")
                    }
                Rectangle()
                    .fill(Color.blue)
            }
            .gesture(newGesture)
            .frame(width: 200, height: 200)
            .border(Color.purple)
        }
    }
    

## See Also

### Recognizing gestures that change over time

`struct DragGesture`

A dragging motion that invokes an action as the drag-event sequence changes.

`struct MagnifyGesture`

A gesture that recognizes a magnification motion and tracks the amount of
magnification.

`struct RotateGesture`

A gesture that recognizes a rotation motion and tracks the angle of the
rotation.

`struct RotateGesture3D`

A gesture that recognizes 3D rotation motion and tracks the angle and axis of
the rotation.

`struct GestureMask`

Options that control how adding a gesture to a view affects other gestures
recognized by the view and its subviews.

Instance Method

# highPriorityGesture(_:including:)

Attaches a gesture to the view with a higher precedence than gestures defined
by the view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func highPriorityGesture<T>(
        _ gesture: T,
        including mask: GestureMask = .all
    ) -> some View where T : Gesture
    

##  Parameters

`gesture`

    

A gesture to attach to the view.

`mask`

    

A value that controls how adding this gesture to the view affects other
gestures recognized by the view and its subviews. Defaults to `all`.

## Discussion

Use this method when you need to define a high priority gesture to take
precedence over the view’s existing gestures. The example below defines a
custom gesture that prints a message to the console and attaches it to the
view’s `VStack`. Inside the `VStack` a red heart `Image` defines its own
`TapGesture` handler that also prints a message to the console, and a blue
rectangle with no custom gesture handlers. Tapping or clicking any of the
views results in a console message from the high priority gesture attached to
the enclosing `VStack`.

## See Also

### Defining custom gestures

`func defersSystemGestures(on: Edge.Set) -> some View`

Sets the screen edge from which you want your gesture to take precedence over
the system gesture.

`protocol Gesture`

An instance that matches a sequence of events to a gesture, and returns a
stream of values for each of its states.

`struct AnyGesture`

A type-erased gesture.

`struct HandActivationBehavior`

An activation behavior specific to hand-driven input.

Instance Method

# simultaneousGesture(_:including:)

Attaches a gesture to the view to process simultaneously with gestures defined
by the view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func simultaneousGesture<T>(
        _ gesture: T,
        including mask: GestureMask = .all
    ) -> some View where T : Gesture
    

##  Parameters

`gesture`

    

A gesture to attach to the view.

`mask`

    

A value that controls how adding this gesture to the view affects other
gestures recognized by the view and its subviews. Defaults to `all`.

## Discussion

Use this method when you need to define and process a view specific gesture
simultaneously with the same priority as the view’s existing gestures. The
example below defines a custom gesture that prints a message to the console
and attaches it to the view’s `VStack`. Inside the `VStack` is a red heart
`Image` defines its own `TapGesture` handler that also prints a message to the
console and a blue rectangle with no custom gesture handlers.

Tapping or clicking the “heart” image sends two messages to the console: one
for the image’s tap gesture handler, and the other from a custom gesture
handler attached to the enclosing vertical stack. Tapping or clicking on the
blue rectangle results only in the single message to the console from the tap
recognizer attached to the `VStack`:

## See Also

### Combining gestures

Composing SwiftUI gestures

Combine gestures to create complex interactions.

`struct SequenceGesture`

A gesture that’s a sequence of two gestures.

`struct SimultaneousGesture`

A gesture containing two gestures that can happen at the same time with
neither of them preceding the other.

`struct ExclusiveGesture`

A gesture that consists of two gestures where only one of them can succeed.

Instance Method

# defersSystemGestures(on:)

Sets the screen edge from which you want your gesture to take precedence over
the system gesture.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+

    
    
    func defersSystemGestures(on edges: Edge.Set) -> some View
    

##  Parameters

`edges`

    

A value that indicates the screen edge from which you want your gesture to
take precedence over the system gesture.

## Discussion

The following code defers the vertical screen edges system gestures of a given
canvas.

## See Also

### Defining custom gestures

`func highPriorityGesture<T>(T, including: GestureMask) -> some View`

Attaches a gesture to the view with a higher precedence than gestures defined
by the view.

`protocol Gesture`

An instance that matches a sequence of events to a gesture, and returns a
stream of values for each of its states.

`struct AnyGesture`

A type-erased gesture.

`struct HandActivationBehavior`

An activation behavior specific to hand-driven input.

Instance Method

# onKeyPress(_:action:)

Performs an action if the user presses a key on a hardware keyboard while the
view has focus.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    func onKeyPress(
        _ key: KeyEquivalent,
        action: @escaping () -> KeyPress.Result
    ) -> some View
    

##  Parameters

`key`

    

The key to match against incoming hardware keyboard events.

`action`

    

The action to perform. Return `.handled` to consume the event and prevent
further dispatch, or `.ignored` to allow dispatch to continue.

## Return Value

A modified view that binds hardware keyboard input when focused.

## Discussion

SwiftUI performs the action for key-down and key-repeat events.

## See Also

### Responding to keyboard input

`func onKeyPress(phases: KeyPress.Phases, action: (KeyPress) ->
KeyPress.Result) -> some View`

Performs an action if the user presses any key on a hardware keyboard while
the view has focus.

`func onKeyPress(KeyEquivalent, phases: KeyPress.Phases, action: (KeyPress) ->
KeyPress.Result) -> some View`

Performs an action if the user presses a key on a hardware keyboard while the
view has focus.

`func onKeyPress(characters: CharacterSet, phases: KeyPress.Phases, action:
(KeyPress) -> KeyPress.Result) -> some View`

Performs an action if the user presses one or more keys on a hardware keyboard
while the view has focus.

`func onKeyPress(keys: Set<KeyEquivalent>, phases: KeyPress.Phases, action:
(KeyPress) -> KeyPress.Result) -> some View`

Performs an action if the user presses one or more keys on a hardware keyboard
while the view has focus.

`struct KeyPress`

Instance Method

# onKeyPress(phases:action:)

Performs an action if the user presses any key on a hardware keyboard while
the view has focus.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    func onKeyPress(
        phases: KeyPress.Phases = [.down, .repeat],
        action: @escaping (KeyPress) -> KeyPress.Result
    ) -> some View
    

##  Parameters

`phases`

    

The key-press phases to match (`.down`, `.repeat`, and `.up`). The default
value is `[.down, .repeat]`.

`action`

    

The action to perform. The action receives a value describing the matched key
event. Return `.handled` to consume the event and prevent further dispatch, or
`.ignored` to allow dispatch to continue.

## Return Value

A modified view that binds hardware keyboard input when focused.

## See Also

### Responding to keyboard input

`func onKeyPress(KeyEquivalent, action: () -> KeyPress.Result) -> some View`

Performs an action if the user presses a key on a hardware keyboard while the
view has focus.

`func onKeyPress(KeyEquivalent, phases: KeyPress.Phases, action: (KeyPress) ->
KeyPress.Result) -> some View`

Performs an action if the user presses a key on a hardware keyboard while the
view has focus.

`func onKeyPress(characters: CharacterSet, phases: KeyPress.Phases, action:
(KeyPress) -> KeyPress.Result) -> some View`

Performs an action if the user presses one or more keys on a hardware keyboard
while the view has focus.

`func onKeyPress(keys: Set<KeyEquivalent>, phases: KeyPress.Phases, action:
(KeyPress) -> KeyPress.Result) -> some View`

Performs an action if the user presses one or more keys on a hardware keyboard
while the view has focus.

`struct KeyPress`

Instance Method

# onKeyPress(_:phases:action:)

Performs an action if the user presses a key on a hardware keyboard while the
view has focus.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    func onKeyPress(
        _ key: KeyEquivalent,
        phases: KeyPress.Phases,
        action: @escaping (KeyPress) -> KeyPress.Result
    ) -> some View
    

##  Parameters

`key`

    

The key to match against incoming hardware keyboard events.

`phases`

    

The key-press phases to match (`.down`, `.up`, and `.repeat`).

`action`

    

The action to perform. The action receives a value describing the matched key
event. Return `.handled` to consume the event and prevent further dispatch, or
`.ignored` to allow dispatch to continue.

## Return Value

A modified view that binds hardware keyboard input when focused.

## Discussion

SwiftUI performs the action for the specified event phases.

## See Also

### Responding to keyboard input

`func onKeyPress(KeyEquivalent, action: () -> KeyPress.Result) -> some View`

Performs an action if the user presses a key on a hardware keyboard while the
view has focus.

`func onKeyPress(phases: KeyPress.Phases, action: (KeyPress) ->
KeyPress.Result) -> some View`

Performs an action if the user presses any key on a hardware keyboard while
the view has focus.

`func onKeyPress(characters: CharacterSet, phases: KeyPress.Phases, action:
(KeyPress) -> KeyPress.Result) -> some View`

Performs an action if the user presses one or more keys on a hardware keyboard
while the view has focus.

`func onKeyPress(keys: Set<KeyEquivalent>, phases: KeyPress.Phases, action:
(KeyPress) -> KeyPress.Result) -> some View`

Performs an action if the user presses one or more keys on a hardware keyboard
while the view has focus.

`struct KeyPress`

Instance Method

# onKeyPress(characters:phases:action:)

Performs an action if the user presses one or more keys on a hardware keyboard
while the view has focus.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    func onKeyPress(
        characters: CharacterSet,
        phases: KeyPress.Phases = [.down, .repeat],
        action: @escaping (KeyPress) -> KeyPress.Result
    ) -> some View
    

##  Parameters

`characters`

    

The set of characters to match against incoming hardware keyboard events.

`phases`

    

The key-press phases to match (`.down`, `.repeat`, and `.up`). The default
value is `[.down, .repeat]`.

`action`

    

The action to perform. The action receives a value describing the matched key
event. Return `.handled` to consume the event and prevent further dispatch, or
`.ignored` to allow dispatch to continue.

## Return Value

A modified view that binds hardware keyboard input when focused.

## See Also

### Responding to keyboard input

`func onKeyPress(KeyEquivalent, action: () -> KeyPress.Result) -> some View`

Performs an action if the user presses a key on a hardware keyboard while the
view has focus.

`func onKeyPress(phases: KeyPress.Phases, action: (KeyPress) ->
KeyPress.Result) -> some View`

Performs an action if the user presses any key on a hardware keyboard while
the view has focus.

`func onKeyPress(KeyEquivalent, phases: KeyPress.Phases, action: (KeyPress) ->
KeyPress.Result) -> some View`

Performs an action if the user presses a key on a hardware keyboard while the
view has focus.

`func onKeyPress(keys: Set<KeyEquivalent>, phases: KeyPress.Phases, action:
(KeyPress) -> KeyPress.Result) -> some View`

Performs an action if the user presses one or more keys on a hardware keyboard
while the view has focus.

`struct KeyPress`

Instance Method

# onKeyPress(keys:phases:action:)

Performs an action if the user presses one or more keys on a hardware keyboard
while the view has focus.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    func onKeyPress(
        keys: Set<KeyEquivalent>,
        phases: KeyPress.Phases = [.down, .repeat],
        action: @escaping (KeyPress) -> KeyPress.Result
    ) -> some View
    

##  Parameters

`keys`

    

A set of keys to match against incoming hardware keyboard events.

`phases`

    

The key-press phases to match (`.down`, `.repeat`, and `.up`). The default
value is `[.down, .repeat]`.

`action`

    

The action to perform. The action receives a value describing the matched key
event. Return `.handled` to consume the event and prevent further dispatch, or
`.ignored` to allow dispatch to continue.

## Return Value

A modified view that binds keyboard input when focused.

## See Also

### Responding to keyboard input

`func onKeyPress(KeyEquivalent, action: () -> KeyPress.Result) -> some View`

Performs an action if the user presses a key on a hardware keyboard while the
view has focus.

`func onKeyPress(phases: KeyPress.Phases, action: (KeyPress) ->
KeyPress.Result) -> some View`

Performs an action if the user presses any key on a hardware keyboard while
the view has focus.

`func onKeyPress(KeyEquivalent, phases: KeyPress.Phases, action: (KeyPress) ->
KeyPress.Result) -> some View`

Performs an action if the user presses a key on a hardware keyboard while the
view has focus.

`func onKeyPress(characters: CharacterSet, phases: KeyPress.Phases, action:
(KeyPress) -> KeyPress.Result) -> some View`

Performs an action if the user presses one or more keys on a hardware keyboard
while the view has focus.

`struct KeyPress`

Instance Method

# keyboardShortcut(_:)

Assigns a keyboard shortcut to the modified control.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    func keyboardShortcut(_ shortcut: KeyboardShortcut) -> some View
    

## Discussion

Pressing the control’s shortcut while the control is anywhere in the frontmost
window or scene, or anywhere in the macOS main menu, is equivalent to direct
interaction with the control to perform its primary action.

The target of a keyboard shortcut is resolved in a leading-to-trailing
traversal of one or more view hierarchies. On macOS, the system looks in the
key window first, then the main window, and then the command groups; on other
platforms, the system looks in the active scene, and then the command groups.

If multiple controls are associated with the same shortcut, the first one
found is used.

## See Also

### Creating keyboard shortcuts

`func keyboardShortcut(KeyboardShortcut?) -> some View`

Assigns an optional keyboard shortcut to the modified control.

`func keyboardShortcut(KeyEquivalent, modifiers: EventModifiers) -> some View`

Defines a keyboard shortcut and assigns it to the modified control.

`func keyboardShortcut(KeyEquivalent, modifiers: EventModifiers, localization:
KeyboardShortcut.Localization) -> some View`

Defines a keyboard shortcut and assigns it to the modified control.

`var keyboardShortcut: KeyboardShortcut?`

The keyboard shortcut that buttons in this environment will be triggered with.

`struct KeyboardShortcut`

Keyboard shortcuts describe combinations of keys on a keyboard that the user
can press in order to activate a button or toggle.

`struct KeyEquivalent`

Key equivalents consist of a letter, punctuation, or function key that can be
combined with an optional set of modifier keys to specify a keyboard shortcut.

`struct EventModifiers`

A set of key modifiers that you can add to a gesture.

Instance Method

# keyboardShortcut(_:)

Assigns an optional keyboard shortcut to the modified control.

iOS 15.4+  iPadOS 15.4+  macOS 12.3+  Mac Catalyst 15.4+  visionOS 1.0+

    
    
    func keyboardShortcut(_ shortcut: KeyboardShortcut?) -> some View
    

## Discussion

Pressing the control’s shortcut while the control is anywhere in the frontmost
window or scene, or anywhere in the macOS main menu, is equivalent to direct
interaction with the control to perform its primary action.

The target of a keyboard shortcut is resolved in a leading-to-trailing
traversal of one or more view hierarchies. On macOS, the system looks in the
key window first, then the main window, and then the command groups; on other
platforms, the system looks in the active scene, and then the command groups.

If multiple controls are associated with the same shortcut, the first one
found is used. If the provided shortcut is `nil`, the modifier will have no
effect.

## See Also

### Creating keyboard shortcuts

`func keyboardShortcut(KeyboardShortcut) -> some View`

Assigns a keyboard shortcut to the modified control.

`func keyboardShortcut(KeyEquivalent, modifiers: EventModifiers) -> some View`

Defines a keyboard shortcut and assigns it to the modified control.

`func keyboardShortcut(KeyEquivalent, modifiers: EventModifiers, localization:
KeyboardShortcut.Localization) -> some View`

Defines a keyboard shortcut and assigns it to the modified control.

`var keyboardShortcut: KeyboardShortcut?`

The keyboard shortcut that buttons in this environment will be triggered with.

`struct KeyboardShortcut`

Keyboard shortcuts describe combinations of keys on a keyboard that the user
can press in order to activate a button or toggle.

`struct KeyEquivalent`

Key equivalents consist of a letter, punctuation, or function key that can be
combined with an optional set of modifier keys to specify a keyboard shortcut.

`struct EventModifiers`

A set of key modifiers that you can add to a gesture.

Instance Method

# keyboardShortcut(_:modifiers:)

Defines a keyboard shortcut and assigns it to the modified control.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    func keyboardShortcut(
        _ key: KeyEquivalent,
        modifiers: EventModifiers = .command
    ) -> some View
    

## Discussion

Pressing the control’s shortcut while the control is anywhere in the frontmost
window or scene, or anywhere in the macOS main menu, is equivalent to direct
interaction with the control to perform its primary action.

The target of a keyboard shortcut is resolved in a leading-to-trailing, depth-
first traversal of one or more view hierarchies. On macOS, the system looks in
the key window first, then the main window, and then the command groups; on
other platforms, the system looks in the active scene, and then the command
groups.

If multiple controls are associated with the same shortcut, the first one
found is used.

The default localization configuration is set to `automatic`.

## See Also

### Creating keyboard shortcuts

`func keyboardShortcut(KeyboardShortcut) -> some View`

Assigns a keyboard shortcut to the modified control.

`func keyboardShortcut(KeyboardShortcut?) -> some View`

Assigns an optional keyboard shortcut to the modified control.

`func keyboardShortcut(KeyEquivalent, modifiers: EventModifiers, localization:
KeyboardShortcut.Localization) -> some View`

Defines a keyboard shortcut and assigns it to the modified control.

`var keyboardShortcut: KeyboardShortcut?`

The keyboard shortcut that buttons in this environment will be triggered with.

`struct KeyboardShortcut`

Keyboard shortcuts describe combinations of keys on a keyboard that the user
can press in order to activate a button or toggle.

`struct KeyEquivalent`

Key equivalents consist of a letter, punctuation, or function key that can be
combined with an optional set of modifier keys to specify a keyboard shortcut.

`struct EventModifiers`

A set of key modifiers that you can add to a gesture.

Instance Method

# keyboardShortcut(_:modifiers:localization:)

Defines a keyboard shortcut and assigns it to the modified control.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    func keyboardShortcut(
        _ key: KeyEquivalent,
        modifiers: EventModifiers = .command,
        localization: KeyboardShortcut.Localization
    ) -> some View
    

## Discussion

Pressing the control’s shortcut while the control is anywhere in the frontmost
window or scene, or anywhere in the macOS main menu, is equivalent to direct
interaction with the control to perform its primary action.

The target of a keyboard shortcut is resolved in a leading-to-trailing, depth-
first traversal of one or more view hierarchies. On macOS, the system looks in
the key window first, then the main window, and then the command groups; on
other platforms, the system looks in the active scene, and then the command
groups.

If multiple controls are associated with the same shortcut, the first one
found is used.

### Localization

Provide a `localization` value to specify how this shortcut should be
localized. Given that `key` is always defined in relation to the US-English
keyboard layout, it might be hard to reach on different international layouts.
For example the shortcut `⌘[` works well for the US layout but is hard to
reach for German users, where `[` is available by pressing `⌥5`, making users
type `⌥⌘5`. The automatic keyboard shortcut remapping re-assigns the shortcut
to an appropriate replacement, `⌘Ö` in this case.

Certain shortcuts carry information about directionality. For instance, `⌘[`
can reveal a previous view. Following the layout direction of the UI, this
shortcut will be automatically mirrored to `⌘]`. However, this does not apply
to items such as “Align Left `⌘{`”, which will be “left” independently of the
layout direction. When the shortcut shouldn’t follow the directionality of the
UI, but rather be the same in both right-to-left and left-to-right directions,
using `withoutMirroring` will prevent the system from flipping it.

    
    
    var body: some Commands {
        CommandMenu("Card") {
            Button("Align Left") { ... }
                .keyboardShortcut("{",
                     modifiers: .option,
                     localization: .withoutMirroring)
            Button("Align Right") { ... }
                .keyboardShortcut("}",
                     modifiers: .option,
                     localization: .withoutMirroring)
        }
    }
    

Lastly, providing the option `custom` disables the automatic localization for
this shortcut to tell the system that internationalization is taken care of in
a different way.

## See Also

### Creating keyboard shortcuts

`func keyboardShortcut(KeyboardShortcut) -> some View`

Assigns a keyboard shortcut to the modified control.

`func keyboardShortcut(KeyboardShortcut?) -> some View`

Assigns an optional keyboard shortcut to the modified control.

`func keyboardShortcut(KeyEquivalent, modifiers: EventModifiers) -> some View`

Defines a keyboard shortcut and assigns it to the modified control.

`var keyboardShortcut: KeyboardShortcut?`

The keyboard shortcut that buttons in this environment will be triggered with.

`struct KeyboardShortcut`

Keyboard shortcuts describe combinations of keys on a keyboard that the user
can press in order to activate a button or toggle.

`struct KeyEquivalent`

Key equivalents consist of a letter, punctuation, or function key that can be
combined with an optional set of modifier keys to specify a keyboard shortcut.

`struct EventModifiers`

A set of key modifiers that you can add to a gesture.

Instance Method

# onHover(perform:)

Adds an action to perform when the user moves the pointer over or away from
the view’s frame.

iOS 13.4+  iPadOS 13.4+  macOS 10.15+  Mac Catalyst 13.4+  visionOS 1.0+

    
    
    func onHover(perform action: @escaping (Bool) -> Void) -> some View
    

##  Parameters

`action`

    

The action to perform whenever the pointer enters or exits this view’s frame.
If the pointer is in the view’s frame, the `action` closure passes `true` as a
parameter; otherwise, `false`.

## Return Value

A view that triggers `action` when the pointer enters or exits this view’s
frame.

## Discussion

Calling this method defines a region for detecting pointer movement with the
size and position of this view.

## See Also

### Responding to hover events

`func onContinuousHover(coordinateSpace: some CoordinateSpaceProtocol,
perform: (HoverPhase) -> Void) -> some View`

Adds an action to perform when the pointer enters, moves within, and exits the
view’s bounds.

`func hoverEffect(HoverEffect, isEnabled: Bool) -> some View`

Applies a hover effect to this view.

`func hoverEffectDisabled(Bool) -> some View`

Adds a condition that controls whether this view can display hover effects.

`func defaultHoverEffect(HoverEffect?) -> some View`

Sets the default hover effect to use for views within this view.

`var isHoverEffectEnabled: Bool`

A Boolean value that indicates whether the view associated with this
environment allows hover effects to be displayed.

`enum HoverPhase`

The current hovering state and value of the pointer.

Instance Method

# onContinuousHover(coordinateSpace:perform:)

Adds an action to perform when the pointer enters, moves within, and exits the
view’s bounds.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    func onContinuousHover(
        coordinateSpace: some CoordinateSpaceProtocol = .local,
        perform action: @escaping (HoverPhase) -> Void
    ) -> some View
    

##  Parameters

`coordinateSpace`

    

The coordinate space for the location values. The default value is
`CoordinateSpace.local`.

`action`

    

The action to perform whenever the pointer enters, moves within, or exits the
view’s bounds. The closure takes a `phase` input that has the value
`HoverPhase.active(_:)` and contains the pointer’s coordinates if the pointer
is within the view’s bounds. The closure receives the `HoverPhase.ended` phase
when the pointer leaves the view’s bounds.

## Return Value

A view that calls `action` when the pointer enters, moves within, or exits the
view’s bounds.

## Discussion

Use this modifier to define a region for detecting pointer movement with a
view. The following example updates a small rectangle’s position and style by
modifying `hoverLocation` and `isHovering` as the pointer moves within the
larger, red rectangle:

## See Also

### Responding to hover events

`func onHover(perform: (Bool) -> Void) -> some View`

Adds an action to perform when the user moves the pointer over or away from
the view’s frame.

`func hoverEffect(HoverEffect, isEnabled: Bool) -> some View`

Applies a hover effect to this view.

`func hoverEffectDisabled(Bool) -> some View`

Adds a condition that controls whether this view can display hover effects.

`func defaultHoverEffect(HoverEffect?) -> some View`

Sets the default hover effect to use for views within this view.

`var isHoverEffectEnabled: Bool`

A Boolean value that indicates whether the view associated with this
environment allows hover effects to be displayed.

`enum HoverPhase`

The current hovering state and value of the pointer.

Instance Method

# hoverEffect(_:)

Applies a hover effect to this view.

iOS 13.4+  iPadOS 13.4+  Mac Catalyst 13.4+  tvOS 16.0+  visionOS 1.0+

    
    
    func hoverEffect(_ effect: HoverEffect = .automatic) -> some View
    

##  Parameters

`effect`

    

The effect to apply to this view.

`isEnabled`

    

Whether the effect is enabled or not.

## Return Value

A new view that applies a hover effect to `self`.

## Discussion

By default, `automatic` is used. You can control the behavior of the automatic
effect with the `defaultHoverEffect(_:)` modifier.

## See Also

### Changing view appearance for hover events

`struct HoverEffect`

An effect applied when the pointer hovers over a view.

Instance Method

# hoverEffect(_:isEnabled:)

Applies a hover effect to this view.

iOS 17.0+  iPadOS 17.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS 1.0+

    
    
    func hoverEffect(
        _ effect: HoverEffect = .automatic,
        isEnabled: Bool = true
    ) -> some View
    

##  Parameters

`effect`

    

The effect to apply to this view.

`isEnabled`

    

Whether the effect is enabled or not.

## Return Value

A new view that applies a hover effect to `self`.

## Discussion

By default, `automatic` is used. You can control the behavior of the automatic
effect with the `defaultHoverEffect(_:)` modifier.

## See Also

### Responding to hover events

`func onHover(perform: (Bool) -> Void) -> some View`

Adds an action to perform when the user moves the pointer over or away from
the view’s frame.

`func onContinuousHover(coordinateSpace: some CoordinateSpaceProtocol,
perform: (HoverPhase) -> Void) -> some View`

Adds an action to perform when the pointer enters, moves within, and exits the
view’s bounds.

`func hoverEffectDisabled(Bool) -> some View`

Adds a condition that controls whether this view can display hover effects.

`func defaultHoverEffect(HoverEffect?) -> some View`

Sets the default hover effect to use for views within this view.

`var isHoverEffectEnabled: Bool`

A Boolean value that indicates whether the view associated with this
environment allows hover effects to be displayed.

`enum HoverPhase`

The current hovering state and value of the pointer.

Instance Method

# hoverEffectDisabled(_:)

Adds a condition that controls whether this view can display hover effects.

iOS 17.0+  iPadOS 17.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS 1.0+

    
    
    func hoverEffectDisabled(_ disabled: Bool = true) -> some View
    

##  Parameters

`disabled`

    

A Boolean value that determines whether this view can display hover effects.

## Return Value

A view that controls whether hover effects can be displayed in this view.

## Discussion

The higher views in a view hierarchy can override the value you set on this
view. In the following example, the button does not display a hover effect
because the outer `hoverEffectDisabled(_:)` modifier overrides the inner one:

## See Also

### Responding to hover events

`func onHover(perform: (Bool) -> Void) -> some View`

Adds an action to perform when the user moves the pointer over or away from
the view’s frame.

`func onContinuousHover(coordinateSpace: some CoordinateSpaceProtocol,
perform: (HoverPhase) -> Void) -> some View`

Adds an action to perform when the pointer enters, moves within, and exits the
view’s bounds.

`func hoverEffect(HoverEffect, isEnabled: Bool) -> some View`

Applies a hover effect to this view.

`func defaultHoverEffect(HoverEffect?) -> some View`

Sets the default hover effect to use for views within this view.

`var isHoverEffectEnabled: Bool`

A Boolean value that indicates whether the view associated with this
environment allows hover effects to be displayed.

`enum HoverPhase`

The current hovering state and value of the pointer.

Instance Method

# defaultHoverEffect(_:)

Sets the default hover effect to use for views within this view.

iOS 17.0+  iPadOS 17.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS 1.0+

    
    
    func defaultHoverEffect(_ effect: HoverEffect?) -> some View
    

##  Parameters

`effect`

    

The default hover effect to use for views within this view.

## Return Value

A view that uses this effect as the default hover effect.

## Discussion

Use this modifier to set a specific hover effect for all views with the
`hoverEffect(_:)` modifier applied within a view. The default effect is
typically used when no `HoverEffect` was provided or if `automatic` is
specified.

For example, this view uses `highlight` for both the red and green Color
views:

This also works for customizing the default hover effect in views like
`Button`s when using a SwiftUI-defined style like `ButtonStyle/bordered`,
which can provide a hover effect by default. For example, this view replaces
the hover effect for a `Button` with `highlight`:

Use a `nil` effect to indicate that the default hover effect should not be
modified.

## See Also

### Responding to hover events

`func onHover(perform: (Bool) -> Void) -> some View`

Adds an action to perform when the user moves the pointer over or away from
the view’s frame.

`func onContinuousHover(coordinateSpace: some CoordinateSpaceProtocol,
perform: (HoverPhase) -> Void) -> some View`

Adds an action to perform when the pointer enters, moves within, and exits the
view’s bounds.

`func hoverEffect(HoverEffect, isEnabled: Bool) -> some View`

Applies a hover effect to this view.

`func hoverEffectDisabled(Bool) -> some View`

Adds a condition that controls whether this view can display hover effects.

`var isHoverEffectEnabled: Bool`

A Boolean value that indicates whether the view associated with this
environment allows hover effects to be displayed.

`enum HoverPhase`

The current hovering state and value of the pointer.

Instance Method

# listRowHoverEffect(_:)

Requests that the containing list row use the provided hover effect.

visionOS 1.0+

    
    
    func listRowHoverEffect(_ effect: HoverEffect?) -> some View
    

##  Parameters

`effect`

    

The hover effect applied to the entire list row.

## Return Value

A view that requests a hover effect for a containing list row

## Discussion

By default, `List` rows have built-in hover effects in visionOS. In some
cases, it is useful to change the default hover effect.

This modifier can be applied to a list row’s content to request that the list
row’s default effect be replaced by the provided effect. If the view is not
contained within a `List` or if the view does not support hover effects in
this context, the modifier has no effect.

Use a `nil` effect to indicate that the list row’s default hover effect should
not be modified.

## See Also

### Configuring rows

`func listRowInsets(EdgeInsets?) -> some View`

Applies an inset to the rows in a list.

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

# listRowHoverEffectDisabled(_:)

Requests that the containing list row have its hover effect disabled.

visionOS 1.0+

    
    
    func listRowHoverEffectDisabled(_ disabled: Bool = true) -> some View
    

##  Parameters

`disabled`

    

A Boolean value that determines whether the containing list row should display
its default hover effect.

## Return Value

A view that requests the default hover effect on its containing list row to
conditionally be disabled.

## Discussion

By default, `List` rows have built-in hover effects in visionOS. In some
cases, it is useful to disable the default hover effect.

## See Also

### Configuring rows

`func listRowInsets(EdgeInsets?) -> some View`

Applies an inset to the rows in a list.

`func listRowHoverEffect(HoverEffect?) -> some View`

Requests that the containing list row use the provided hover effect.

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

# focused(_:equals:)

Modifies this view by binding its focus state to the given state value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func focused<Value>(
        _ binding: FocusState<Value>.Binding,
        equals value: Value
    ) -> some View where Value : Hashable
    

##  Parameters

`binding`

    

The state binding to register. When focus moves to the modified view, the
binding sets the bound value to the corresponding match value. If a caller
sets the state value programmatically to the matching value, then focus moves
to the modified view. When focus leaves the modified view, the binding sets
the bound value to `nil`. If a caller sets the value to `nil`, SwiftUI
automatically dismisses focus.

`value`

    

The value to match against when determining whether the binding should change.

## Return Value

The modified view.

## Discussion

Use this modifier to cause the view to receive focus whenever the the
`binding` equals the `value`. Typically, you create an enumeration of fields
that may receive focus, bind an instance of this enumeration, and assign its
cases to focusable views.

The following example uses the cases of a `LoginForm` enumeration to bind the
focus state of two `TextField` views. A sign-in button validates the fields
and sets the bound `focusedField` value to any field that requires the user to
correct a problem.

    
    
    struct LoginForm {
        enum Field: Hashable {
            case usernameField
            case passwordField
        }
    
    
        @State private var username = ""
        @State private var password = ""
        @FocusState private var focusedField: Field?
    
    
        var body: some View {
            Form {
                TextField("Username", text: $username)
                    .focused($focusedField, equals: .usernameField)
    
    
                SecureField("Password", text: $password)
                    .focused($focusedField, equals: .passwordField)
    
    
                Button("Sign In") {
                    if username.isEmpty {
                        focusedField = .usernameField
                    } else if password.isEmpty {
                        focusedField = .passwordField
                    } else {
                        handleLogin(username, password)
                    }
                }
            }
        }
    }
    

To control focus using a Boolean, use the `focused(_:)` method instead.

## See Also

### Managing focus state

`func focused(FocusState<Bool>.Binding) -> some View`

Modifies this view by binding its focus state to the given Boolean state
value.

`var isFocused: Bool`

Returns whether the nearest focusable ancestor has focus.

`struct FocusState`

A property wrapper type that can read and write a value that SwiftUI updates
as the placement of focus within the scene changes.

`struct FocusedValue`

A property wrapper for observing values from the focused view or one of its
ancestors.

`protocol FocusedValueKey`

A protocol for identifier types used when publishing and observing focused
values.

`struct FocusedBinding`

A convenience property wrapper for observing and automatically unwrapping
state bindings from the focused view or one of its ancestors.

Instance Method

# focused(_:)

Modifies this view by binding its focus state to the given Boolean state
value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func focused(_ condition: FocusState<Bool>.Binding) -> some View
    

##  Parameters

`condition`

    

The focus state to bind. When focus moves to the view, the binding sets the
bound value to `true`. If a caller sets the value to `true` programmatically,
then focus moves to the modified view. When focus leaves the modified view,
the binding sets the value to `false`. If a caller sets the value to `false`,
SwiftUI automatically dismisses focus.

## Return Value

The modified view.

## Discussion

Use this modifier to cause the view to receive focus whenever the the
`condition` value is `true`. You can use this modifier to observe the focus
state of a single view, or programmatically set and remove focus from the
view.

In the following example, a single `TextField` accepts a user’s desired
`username`. The text field binds its focus state to the Boolean value
`usernameFieldIsFocused`. A “Submit” button’s action verifies whether the name
is available. If the name is unavailable, the button sets
`usernameFieldIsFocused` to `true`, which causes focus to return to the text
field, so the user can enter a different name.

    
    
    @State private var username: String = ""
    @FocusState private var usernameFieldIsFocused: Bool
    @State private var showUsernameTaken = false
    
    
    var body: some View {
        VStack {
            TextField("Choose a username.", text: $username)
                .focused($usernameFieldIsFocused)
            if showUsernameTaken {
                Text("That username is taken. Please choose another.")
            }
            Button("Submit") {
                showUsernameTaken = false
                if !isUserNameAvailable(username: username) {
                    usernameFieldIsFocused = true
                    showUsernameTaken = true
                }
            }
        }
    }
    

To control focus by matching a value, use the `focused(_:equals:)` method
instead.

## See Also

### Managing focus state

`func focused<Value>(FocusState<Value>.Binding, equals: Value) -> some View`

Modifies this view by binding its focus state to the given state value.

`var isFocused: Bool`

Returns whether the nearest focusable ancestor has focus.

`struct FocusState`

A property wrapper type that can read and write a value that SwiftUI updates
as the placement of focus within the scene changes.

`struct FocusedValue`

A property wrapper for observing values from the focused view or one of its
ancestors.

`protocol FocusedValueKey`

A protocol for identifier types used when publishing and observing focused
values.

`struct FocusedBinding`

A convenience property wrapper for observing and automatically unwrapping
state bindings from the focused view or one of its ancestors.

Instance Method

# focusedValue(_:)

Sets the focused value for the given object type.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func focusedValue<T>(_ object: T?) -> some View where T : AnyObject, T : Observable
    

## Discussion

Important

This initializer only accepts objects conforming to the `Observable` protocol.
For reading environment objects that conform to `ObservableObject`, use
`focusedObject(_:)`, instead.

To read this value, use the `FocusedValue` property wrapper.

## See Also

### Exposing value types to focused views

`func focusedValue<Value>(WritableKeyPath<FocusedValues, Value?>, Value) ->
some View`

Modifies this view by injecting a value that you provide for use by other
views whose state depends on the focused view hierarchy.

`func focusedValue<Value>(WritableKeyPath<FocusedValues, Value?>, Value?) ->
some View`

Creates a new view that exposes the provided value to other views whose state
depends on the focused view hierarchy.

`func focusedSceneValue<T>(WritableKeyPath<FocusedValues, T?>, T?) -> some
View`

Creates a new view that exposes the provided value to other views whose state
depends on the active scene.

`func focusedSceneValue<T>(WritableKeyPath<FocusedValues, T?>, T) -> some
View`

Modifies this view by injecting a value that you provide for use by other
views whose state depends on the focused scene.

`struct FocusedValues`

A collection of state exported by the focused view and its ancestors.

Instance Method

# focusedValue(_:_:)

Modifies this view by injecting a value that you provide for use by other
views whose state depends on the focused view hierarchy.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func focusedValue<Value>(
        _ keyPath: WritableKeyPath<FocusedValues, Value?>,
        _ value: Value
    ) -> some View
    

##  Parameters

`keyPath`

    

The key path to associate `value` with when adding it to the existing table of
exported focus values.

`value`

    

The focus value to export.

## Return Value

A modified representation of this view.

## See Also

### Exposing value types to focused views

`func focusedValue<T>(T?) -> some View`

Sets the focused value for the given object type.

`func focusedValue<Value>(WritableKeyPath<FocusedValues, Value?>, Value?) ->
some View`

Creates a new view that exposes the provided value to other views whose state
depends on the focused view hierarchy.

`func focusedSceneValue<T>(WritableKeyPath<FocusedValues, T?>, T?) -> some
View`

Creates a new view that exposes the provided value to other views whose state
depends on the active scene.

`func focusedSceneValue<T>(WritableKeyPath<FocusedValues, T?>, T) -> some
View`

Modifies this view by injecting a value that you provide for use by other
views whose state depends on the focused scene.

`struct FocusedValues`

A collection of state exported by the focused view and its ancestors.

Instance Method

# focusedValue(_:_:)

Creates a new view that exposes the provided value to other views whose state
depends on the focused view hierarchy.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func focusedValue<Value>(
        _ keyPath: WritableKeyPath<FocusedValues, Value?>,
        _ value: Value?
    ) -> some View
    

##  Parameters

`keyPath`

    

The key path to associate `value` with when adding it to the existing table of
exported focus values.

`value`

    

The focus value to export, or `nil` if no value is currently available.

## Return Value

A modified representation of this view.

## Discussion

Use this method instead of `View/focusedSceneValue(_:_:)` when your scene
includes multiple focusable views with their own associated values, and you
need an app- or scene-scoped element like a command or toolbar item that
operates on the value associated with whichever view currently has focus. Each
focusable view can supply its own value:

## See Also

### Exposing value types to focused views

`func focusedValue<T>(T?) -> some View`

Sets the focused value for the given object type.

`func focusedValue<Value>(WritableKeyPath<FocusedValues, Value?>, Value) ->
some View`

Modifies this view by injecting a value that you provide for use by other
views whose state depends on the focused view hierarchy.

`func focusedSceneValue<T>(WritableKeyPath<FocusedValues, T?>, T?) -> some
View`

Creates a new view that exposes the provided value to other views whose state
depends on the active scene.

`func focusedSceneValue<T>(WritableKeyPath<FocusedValues, T?>, T) -> some
View`

Modifies this view by injecting a value that you provide for use by other
views whose state depends on the focused scene.

`struct FocusedValues`

A collection of state exported by the focused view and its ancestors.

Instance Method

# focusedSceneValue(_:_:)

Creates a new view that exposes the provided value to other views whose state
depends on the active scene.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func focusedSceneValue<T>(
        _ keyPath: WritableKeyPath<FocusedValues, T?>,
        _ value: T?
    ) -> some View
    

##  Parameters

`keyPath`

    

The key path to associate `value` with when adding it to the existing table of
published focus values.

`value`

    

The focus value to publish, or `nil` if no value is currently available.

## Return Value

A modified representation of this view.

## Discussion

Use this method instead of `View/focusedValue(_:_:)` for values that must be
visible regardless of where focus is located in the active scene. For example,
if an app needs a command for moving focus to a particular text field in the
sidebar, it could use this modifier to publish a button action that’s visible
to command views as long as the scene is active, and regardless of where focus
happens to be in it.

## See Also

### Exposing value types to focused views

`func focusedValue<T>(T?) -> some View`

Sets the focused value for the given object type.

`func focusedValue<Value>(WritableKeyPath<FocusedValues, Value?>, Value) ->
some View`

Modifies this view by injecting a value that you provide for use by other
views whose state depends on the focused view hierarchy.

`func focusedValue<Value>(WritableKeyPath<FocusedValues, Value?>, Value?) ->
some View`

Creates a new view that exposes the provided value to other views whose state
depends on the focused view hierarchy.

`func focusedSceneValue<T>(WritableKeyPath<FocusedValues, T?>, T) -> some
View`

Modifies this view by injecting a value that you provide for use by other
views whose state depends on the focused scene.

`struct FocusedValues`

A collection of state exported by the focused view and its ancestors.

Instance Method

# focusedSceneValue(_:_:)

Modifies this view by injecting a value that you provide for use by other
views whose state depends on the focused scene.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func focusedSceneValue<T>(
        _ keyPath: WritableKeyPath<FocusedValues, T?>,
        _ value: T
    ) -> some View
    

##  Parameters

`keyPath`

    

The key path to associate `value` with when adding it to the existing table of
published focus values.

`value`

    

The focus value to publish.

## Return Value

A modified representation of this view.

## Discussion

Use this method instead of `View/focusedValue(_:_:)` for values that must be
visible regardless of where focus is located in the active scene. For example,
if an app needs a command for moving focus to a particular text field in the
sidebar, it could use this modifier to publish a button action that’s visible
to command views as long as the scene is active, and regardless of where focus
happens to be in it.

    
    
    struct Sidebar: View {
        @FocusState var isFiltering: Bool
    
    
        var body: some View {
            VStack {
                TextField(...)
                    .focused(when: $isFiltering)
                    .focusedSceneValue(\.filterAction) {
                        isFiltering = true
                    }
            }
        }
    }
    
    
    struct NavigationCommands: Commands {
        @FocusedValue(\.filterAction) var filterAction
    
    
        var body: some Commands {
            CommandMenu("Navigate") {
                Button("Filter in Sidebar") {
                    filterAction?()
                }
            }
            .disabled(filterAction == nil)
        }
    }
    
    
    struct FilterActionKey: FocusedValuesKey {
        typealias Value = () -> Void
    }
    
    
    extension FocusedValues {
        var filterAction: (() -> Void)? {
            get { self[FilterActionKey.self] }
            set { self[FilterActionKey.self] = newValue }
        }
    }
    

## See Also

### Exposing value types to focused views

`func focusedValue<T>(T?) -> some View`

Sets the focused value for the given object type.

`func focusedValue<Value>(WritableKeyPath<FocusedValues, Value?>, Value) ->
some View`

Modifies this view by injecting a value that you provide for use by other
views whose state depends on the focused view hierarchy.

`func focusedValue<Value>(WritableKeyPath<FocusedValues, Value?>, Value?) ->
some View`

Creates a new view that exposes the provided value to other views whose state
depends on the focused view hierarchy.

`func focusedSceneValue<T>(WritableKeyPath<FocusedValues, T?>, T?) -> some
View`

Creates a new view that exposes the provided value to other views whose state
depends on the active scene.

`struct FocusedValues`

A collection of state exported by the focused view and its ancestors.

Instance Method

# focusedObject(_:)

Creates a new view that exposes the provided object to other views whose state
depends on the focused view hierarchy.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func focusedObject<T>(_ object: T?) -> some View where T : ObservableObject
    

##  Parameters

`object`

    

The observable object to associate with focus, or `nil` if no object is
currently available.

## Return Value

A view that supplies an observable object when in focus.

## Discussion

Use this method instead of `View/focusedSceneObject(_:)` when your scene
includes multiple focusable views with their own associated data, and you need
an app- or scene-scoped element like a command or toolbar item that operates
on the data associated with whichever view currently has focus. Each focusable
view can supply its own object:

Interested views can then use the `FocusedObject` property wrapper to observe
and update the focused view’s object. In this example, an app command updates
the focused view’s data, and is automatically disabled when focus is in an
unrelated part of the scene:

## See Also

### Exposing reference types to focused views

`func focusedObject<T>(T) -> some View`

Creates a new view that exposes the provided object to other views whose whose
state depends on the focused view hierarchy.

`func focusedSceneObject<T>(T?) -> some View`

Creates a new view that exposes the provided object to other views whose whose
state depends on the active scene.

`func focusedSceneObject<T>(T) -> some View`

Creates a new view that exposes the provided object to other views whose whose
state depends on the active scene.

`struct FocusedObject`

A property wrapper type for an observable object supplied by the focused view
or one of its ancestors.

Instance Method

# focusedObject(_:)

Creates a new view that exposes the provided object to other views whose whose
state depends on the focused view hierarchy.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func focusedObject<T>(_ object: T) -> some View where T : ObservableObject
    

##  Parameters

`object`

    

The observable object to associate with focus.

## Return Value

A view that supplies an observable object when in focus.

## Discussion

Use this method instead of `View/focusedSceneObject(_:)` when your scene
includes multiple focusable views with their own associated data, and you need
an app- or scene-scoped element like a command or toolbar item that operates
on the data associated with whichever view currently has focus. Each focusable
view can supply its own object:

Interested views can then use the `FocusedObject` property wrapper to observe
and update the focused view’s object. In this example, an app command updates
the focused view’s data, and is automatically disabled when focus is in an
unrelated part of the scene:

## See Also

### Exposing reference types to focused views

`func focusedObject<T>(T?) -> some View`

Creates a new view that exposes the provided object to other views whose state
depends on the focused view hierarchy.

`func focusedSceneObject<T>(T?) -> some View`

Creates a new view that exposes the provided object to other views whose whose
state depends on the active scene.

`func focusedSceneObject<T>(T) -> some View`

Creates a new view that exposes the provided object to other views whose whose
state depends on the active scene.

`struct FocusedObject`

A property wrapper type for an observable object supplied by the focused view
or one of its ancestors.

Instance Method

# focusedSceneObject(_:)

Creates a new view that exposes the provided object to other views whose whose
state depends on the active scene.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func focusedSceneObject<T>(_ object: T?) -> some View where T : ObservableObject
    

##  Parameters

`object`

    

The observable object to associate with the scene, or `nil` if no object is
currently available.

## Return Value

A view that supplies an observable object while the scene is active.

## Discussion

Use this method instead of `View/focusedObject(_:)` for observable objects
that must be visible regardless of where focus is located in the active scene.
This is sometimes needed for things like main menu and discoverability HUD
commands that observe and update data from the active scene but aren’t
concerned with what the user is actually focused on. The scene’s root view can
supply the scene’s state object:

Interested views can then use the `FocusedObject` property wrapper to observe
and update the active scene’s state object. In this example, an app command
updates the active scene’s data, and is enabled as long as any scene is
active.

## See Also

### Exposing reference types to focused views

`func focusedObject<T>(T?) -> some View`

Creates a new view that exposes the provided object to other views whose state
depends on the focused view hierarchy.

`func focusedObject<T>(T) -> some View`

Creates a new view that exposes the provided object to other views whose whose
state depends on the focused view hierarchy.

`func focusedSceneObject<T>(T) -> some View`

Creates a new view that exposes the provided object to other views whose whose
state depends on the active scene.

`struct FocusedObject`

A property wrapper type for an observable object supplied by the focused view
or one of its ancestors.

Instance Method

# focusedSceneObject(_:)

Creates a new view that exposes the provided object to other views whose whose
state depends on the active scene.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func focusedSceneObject<T>(_ object: T) -> some View where T : ObservableObject
    

##  Parameters

`object`

    

The observable object to associate with the scene.

## Return Value

A view that supplies an observable object while the scene is active.

## Discussion

Use this method instead of `View/focusedObject(_:)` for observable objects
that must be visible regardless of where focus is located in the active scene.
This is sometimes needed for things like main menu and discoverability HUD
commands that observe and update data from the active scene but aren’t
concerned with what the user is actually focused on. The scene’s root view can
supply the scene’s state object:

Interested views can then use the `FocusedObject` property wrapper to observe
and update the active scene’s state object. In this example, an app command
updates the active scene’s data, and is enabled as long as any scene is
active.

## See Also

### Exposing reference types to focused views

`func focusedObject<T>(T?) -> some View`

Creates a new view that exposes the provided object to other views whose state
depends on the focused view hierarchy.

`func focusedObject<T>(T) -> some View`

Creates a new view that exposes the provided object to other views whose whose
state depends on the focused view hierarchy.

`func focusedSceneObject<T>(T?) -> some View`

Creates a new view that exposes the provided object to other views whose whose
state depends on the active scene.

`struct FocusedObject`

A property wrapper type for an observable object supplied by the focused view
or one of its ancestors.

Instance Method

# prefersDefaultFocus(_:in:)

Indicates that the view should receive focus by default for a given namespace.

macOS 12.0+  tvOS 14.0+  watchOS 7.0+

    
    
    func prefersDefaultFocus(
        _ prefersDefaultFocus: Bool = true,
        in namespace: Namespace.ID
    ) -> some View
    

##  Parameters

`prefersDefaultFocus`

    

A Boolean value that indicates whether this view prefers to receive focus by
default. The default value, `true`, causes the view to receive focus by
default.

`namespace`

    

The namespace associated with the focus scope within which this view prefers
default focus.

## Return Value

A modified view that sets whether it prefers to be focused by default.

## Discussion

This modifier sets the initial focus preference when no other view has focus.
Use the environment value `resetFocus` to force a reevaluation of default
focus at any time.

The following tvOS example shows three buttons, labeled “1”, “2”, and “3”, in
a `VStack`. By default, the “1” button would receive focus, because it is the
first child in the stack. However, the `prefersDefaultFocus(_:in:)` modifier
allows button “3” to receive default focus instead. Once the buttons are
visible, the user can move down to and focus the “Reset to default focus”
button. When the user activates this button, it uses the `ResetFocusAction` to
reevaluate default focus in the `mainNamespace`, which returns the focus to
button “3”.

The default focus preference is limited to the focusable ancestor that matches
the provided namespace. If multiple views express this preference, then
SwiftUI applies the current platform rules to determine which view receives
focus.

## See Also

### Controlling default focus

`func defaultFocus<V>(FocusState<V>.Binding, V, priority:
DefaultFocusEvaluationPriority) -> some View`

Defines a region of the window in which default focus is evaluated by
assigning a value to a given focus state binding.

`struct DefaultFocusEvaluationPriority`

Prioritizations for default focus preferences when evaluating where to move
focus in different circumstances.

Instance Method

# focusScope(_:)

Creates a focus scope that SwiftUI uses to limit default focus preferences.

macOS 12.0+  tvOS 14.0+  watchOS 7.0+

    
    
    func focusScope(_ namespace: Namespace.ID) -> some View
    

##  Parameters

`namespace`

    

A namespace identifier that SwiftUI can use to scope default focus
preferences.

## Return Value

A view that sets the namespace of descendants for default focus.

## Discussion

The returned view gets associated with the provided namespace. Pass this
namespace to `prefersDefaultFocus(_:in:)` and the `resetFocus` function.

## See Also

### Setting focus scope

`func focusSection() -> some View`

Indicates that the view’s frame and cohort of focusable descendants should be
used to guide focus movement.

Instance Method

# focusSection()

Indicates that the view’s frame and cohort of focusable descendants should be
used to guide focus movement.

macOS 13.0+  tvOS 15.0+

    
    
    func focusSection() -> some View
    

## Return Value

A view that can guide focus to its focusable descendents.

## Discussion

Use focus sections to customize SwiftUI’s behavior when the user moves focus
between views.

The following tvOS example places three buttons (“1”, “2”, and “3”) at the
upper left of the screen and three buttons (“A”, “B”, and “C”) at the bottom
right. By default, swiping right on the Siri Remote on any of the buttons in
the “1” - “3” group would do nothing, since the focus system finds no
focusable views directly to their right. But by declaring the `VStack` that
encloses buttons “A” - “C” as a focus section, the `VStack` can receive focus,
and deliver that focus to its first focusable child (button “A”). The example
puts a border on the `VStack` to illustrate this spatial arrangement.

Note that because the `VStack` containing buttons “1” - “3” does not declare
itself as a focus section, it is impossible to direct focus back to the left
from buttons “A” - “C”. None of those buttons has a focusable view — in this
case either a button or a `VStack` with the `focusSection()` modifier —
directly to its left.

Applying this modifier to a view affects focus behavior based on the style of
movement:

  * **Directional movement** : Navigating with Siri Remote gestures, arrow keys on a keyboard, or any other type of input that works in terms of cardinal directions (up, down, left, right) produces directional movement. When modified with `focusSection()`, the view’s frame becomes capable of accepting focus in order to direct it at its nearest focusable descendant in the direction of travel. In the earlier example, declaring the right-side `VStack` as a focus section allowed it to receive right-directed focus from the buttons on the left.

  * **Sequential movement** : Navigating with a Digital Crown, the Tab key on a keyboard, or any other type of input that works in terms of the next or previous item in a sequence, produces sequential movement. When you use the `focusSection()` modifier, SwiftUI deviates from its default layout-based sequence to visit each of the modified view’s focusable descendants before resuming the default sequence. Within the set of focusable descendants, SwiftUI continues to visit views in layout order (leading-to-trailing, top-to-bottom).

`focusSection()` does not affect the focusability of the modified view. If the
modified view has no focusable descendants, then the modifier does nothing.

## See Also

### Setting focus scope

`func focusScope(Namespace.ID) -> some View`

Creates a focus scope that SwiftUI uses to limit default focus preferences.

Instance Method

# focusable(_:)

Specifies if the view is focusable.

iOS 17.0+  iPadOS 17.0+  macOS 12.0+  Mac Catalyst 17.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func focusable(_ isFocusable: Bool = true) -> some View
    

##  Parameters

`isFocusable`

    

A Boolean value that indicates whether this view is focusable.

## Return Value

A view that sets whether a view is focusable.

## See Also

### Indicating that a view can receive focus

`func focusable(Bool, interactions: FocusInteractions) -> some View`

Specifies if the view is focusable, and if so, what focus-driven interactions
it supports.

`struct FocusInteractions`

Values describe different focus interactions that a view can support.

Instance Method

# focusable(_:interactions:)

Specifies if the view is focusable, and if so, what focus-driven interactions
it supports.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func focusable(
        _ isFocusable: Bool = true,
        interactions: FocusInteractions
    ) -> some View
    

##  Parameters

`isFocusable`

    

`true` if the view should participate in focus; `false` otherwise. The default
value is `true`.

`interactions`

    

The types of focus interactions supported by the view. The default value is
`.automatic`.

## Return Value

A view that sets whether its child is focusable.

## Discussion

By default, SwiftUI enables all possible focus interactions. However, on macOS
and iOS it is conventional for button-like views to only accept focus when the
user has enabled keyboard navigation system-wide in the Settings app. Clients
can reproduce this behavior with custom views by only supporting `.activate`
interactions.

Note

The focus interactions allowed for custom views changed in macOS
14—previously, custom views could only become focused with keyboard navigation
enabled system-wide. Clients built using older SDKs will continue to see the
older focus behavior, while custom views in clients built using macOS 14 or
later will always be focusable unless the client requests otherwise by
specifying a restricted set of focus interactions.

## See Also

### Indicating that a view can receive focus

`func focusable(Bool) -> some View`

Specifies if the view is focusable.

`struct FocusInteractions`

Values describe different focus interactions that a view can support.

Instance Method

# focusEffectDisabled(_:)

Adds a condition that controls whether this view can display focus effects,
such as a default focus ring or hover effect.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func focusEffectDisabled(_ disabled: Bool = true) -> some View
    

##  Parameters

`disabled`

    

A Boolean value that determines whether this view can display focus effects.

## Return Value

A view that controls whether focus effects can be displayed in this view.

## Discussion

The higher views in a view hierarchy can override the value you set on this
view. In the following example, the button does not display a focus effect
because the outer `focusEffectDisabled(_:)` modifier overrides the inner one:

## See Also

### Configuring effects

`var isFocusEffectEnabled: Bool`

A Boolean value that indicates whether the view associated with this
environment allows focus effects to be displayed.

Instance Method

# defaultFocus(_:_:priority:)

Defines a region of the window in which default focus is evaluated by
assigning a value to a given focus state binding.

iOS 17.0+  iPadOS 17.0+  macOS 13.0+  Mac Catalyst 17.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func defaultFocus<V>(
        _ binding: FocusState<V>.Binding,
        _ value: V,
        priority: DefaultFocusEvaluationPriority = .automatic
    ) -> some View where V : Hashable
    

##  Parameters

`binding`

    

A focus state binding to update when evaluating default focus in the modified
view hierarchy.

`value`

    

The value to set the binding to during evaluation.

`priority`

    

An indication of how to prioritize the preferred default focus target when
focus moves into the modified view hierarchy. The default value is
`automatic`, which means the preference will be given priority when focus is
being initialized or relocated programmatically, but not when responding to
user-directed navigation commands.

## Return Value

The modified view.

## Discussion

By default, SwiftUI evaluates default focus when the window first appears, and
when a focus state binding update moves focus automatically, but not when
responding to user-driven navigation commands.

Clients can override the default behavior by specifying an evaluation priority
of `userInitiated`, which causes SwiftUI to use the client’s preferred default
focus in response to user-driven focus navigation as well as automatic
changes.

In the following example, focus automatically goes to the second of the two
text fields when the view is first presented in the window.

## See Also

### Controlling default focus

`func prefersDefaultFocus(Bool, in: Namespace.ID) -> some View`

Indicates that the view should receive focus by default for a given namespace.

`struct DefaultFocusEvaluationPriority`

Prioritizations for default focus preferences when evaluating where to move
focus in different circumstances.

Instance Method

# copyable(_:)

Specifies a list of items to copy in response to the system’s Copy command.

macOS 13.0+

    
    
    func copyable<T>(_ payload: @autoclosure @escaping () -> [T]) -> some View where T : Transferable
    

##  Parameters

`payload`

    

A closure that returns an array of items to copy to the Clipboard when someone
issues a Copy command. The items in the array must conform to the
`Transferable` protocol.

## Return Value

A view that adds one or more items to the Clipboard in response to a Copy
command.

## Discussion

Use this modifier to specify one or more items that the system copies to the
Clipboard when someone issues a Copy command while the modified view has
focus. People issue a Copy command by choosing Edit > Copy from the app’s
menu, or by using the Command-C keyboard shortcut. The system enables the Copy
command for your app when it detects copyable content.

For example, the following code enables people to copy all of the strings that
they select in a `List`:

The command copies each item’s representation as specified by the item’s
conformance to the `Transferable` protocol. The above example records
selection using each list item’s corresponding string, and strings conform to
the `Transferable` protocol by default. For more complex cases, you might need
to take additional steps.

For example, the following code displays colors composed from a list of `Item`
instances that contain both a color and its name, as well as an identifier.
The list manages selection using item identifiers:

This example does two things that the previous example didn’t have to:

  * It converts the list of selected item identifiers into a list of selected items for use with the copyable modifier.

  * It ensures that the copyable items conform to the `Transferable` protocol, using the item’s `name` property as the representation.

When someone copies the first item in the list, which appears in the interface
as a red rectangle, and then pastes into a text editor, they get the string
“red”.

Note

To enable people to copy using a custom action — like from a context menu item
— rather than using the system Copy command, update the Clipboard directly
using an `NSPasteboard` or a `UIPasteboard` instance.

## See Also

### Copying transferable items

`func cuttable<T>(for: T.Type, action: () -> [T]) -> some View`

Specifies an action that moves items to the Clipboard in response to the
system’s Cut command.

`func pasteDestination<T>(for: T.Type, action: ([T]) -> Void, validator: ([T])
-> [T]) -> some View`

Specifies an action that adds validated items to a view in response to the
system’s Paste command.

Instance Method

# cuttable(for:action:)

Specifies an action that moves items to the Clipboard in response to the
system’s Cut command.

macOS 13.0+

    
    
    func cuttable<T>(
        for payloadType: T.Type = T.self,
        action: @escaping () -> [T]
    ) -> some View where T : Transferable
    

##  Parameters

`payloadType`

    

The type of items to cut.

`action`

    

A closure that you implement to delete the selected items from the collection,
and return them for addition to the Clipboard. The items must conform to the
`Transferable` protocol.

## Return Value

A view that sends one or more items to the Clipboard in response to a Cut
command.

## Discussion

Use this modifier to remove one or more items from a collection of items and
then move the items to the Clipboard when someone issues a Cut command. People
issue a Cut command by choosing Edit > Cut from the app’s menu, or by using
the Command-X keyboard shortcut. The system enables the Cut command for your
app when it detects cuttable content.

For example, the following code enables people to remove bird names from a
list of birds:

When someone selects “owl” and issues a Cut command, the `action` closure
removes the selected item from the list and returns it. In response, SwiftUI
moves it to the Clipboard. If you want to copy the item without removing it,
use the `copyable(_:)` modifier instead.

Note

To enable people to cut using a custom action — like from a context menu item
— rather than using the system Cut command, update the Clipboard directly
using an `NSPasteboard` or a `UIPasteboard` instance.

## See Also

### Copying transferable items

`func copyable<T>(() -> [T]) -> some View`

Specifies a list of items to copy in response to the system’s Copy command.

`func pasteDestination<T>(for: T.Type, action: ([T]) -> Void, validator: ([T])
-> [T]) -> some View`

Specifies an action that adds validated items to a view in response to the
system’s Paste command.

Instance Method

# pasteDestination(for:action:validator:)

Specifies an action that adds validated items to a view in response to the
system’s Paste command.

macOS 13.0+

    
    
    func pasteDestination<T>(
        for payloadType: T.Type = T.self,
        action: @escaping ([T]) -> Void,
        validator: @escaping ([T]) -> [T] = { $0 }
    ) -> some View where T : Transferable
    

##  Parameters

`payloadType`

    

The type of data that the paste destination accepts. The type must conform to
the `Transferable` protocol.

`action`

    

The action to perform when someone uses the system’s Paste command to paste
one or more items of the payload type. The closure takes one parameter, which
is the array of items to paste.

`validator`

    

A closure that you implement to validate the data to paste. SwiftUI calls this
before it calls the `action` closure, and passes in an array of items to
validate. Inspect the items, and return an array that includes only those from
the input array that you consider valid. The array that you return from this
closure becomes the input to the `action` closure. If you return an empty
array, SwiftUI doesn’t call the `action` closure.

## Return Value

A view that people can paste into using the system Paste command.

## Discussion

Use this modifier to paste one or more items into a view from the Clipboard
when someone issues a Paste command. People issue a Paste command by choosing
Edit > Paste from the app’s menu, or by using the Command-V keyboard shortcut.
The system enables the Paste command for your app when the view in focus
provides a paste destination.

For example, the following code enables people to paste bird names into a
list:

The paste destination handles only pasted content with a type that matches the
`payloadType` that you specify. The list in the above example only accepts
strings.

Use the `validator` closure to restrict the pasted content to items that make
sense in the context of the view. The above example allows people to paste
only strings that match one of a known list of bird names because the list is
meant to contain only birds. You can omit the final closure if you don’t need
to perform any validation.

Note

To enable people to paste using a custom action — like from a context menu
item — rather than using the system Paste command, access the Clipboard
directly using an `NSPasteboard` or a `UIPasteboard` instance.

## See Also

### Copying transferable items

`func copyable<T>(() -> [T]) -> some View`

Specifies a list of items to copy in response to the system’s Copy command.

`func cuttable<T>(for: T.Type, action: () -> [T]) -> some View`

Specifies an action that moves items to the Clipboard in response to the
system’s Cut command.

Instance Method

# onCopyCommand(perform:)

Adds an action to perform in response to the system’s Copy command.

macOS 10.15+

    
    
    func onCopyCommand(perform payloadAction: (() -> [NSItemProvider])?) -> some View
    

##  Parameters

`payloadAction`

    

An action closure returning the `NSItemProvider` items that should be copied
to the Clipboard when the Copy command is triggered. If `action` is `nil`, the
Copy command is considered disabled.

## Return Value

A view that triggers `action` when a system Copy command occurs.

## See Also

### Copying items using item providers

`func onCutCommand(perform: (() -> [NSItemProvider])?) -> some View`

Adds an action to perform in response to the system’s Cut command.

`func onPasteCommand(of: [UTType], perform: ([NSItemProvider]) -> Void) ->
some View`

Adds an action to perform in response to the system’s Paste command.

`func onPasteCommand<Payload>(of: [UTType], validator: ([NSItemProvider]) ->
Payload?, perform: (Payload) -> Void) -> some View`

Adds an action to perform in response to the system’s Paste command with items
that you validate.

Instance Method

# onCutCommand(perform:)

Adds an action to perform in response to the system’s Cut command.

macOS 10.15+

    
    
    func onCutCommand(perform payloadAction: (() -> [NSItemProvider])?) -> some View
    

##  Parameters

`payloadAction`

    

An action closure that should delete the selected data and return
`NSItemProvider` items corresponding to that data, which should be written to
the Clipboard. If `action` is `nil`, the Cut command is considered disabled.

## Return Value

A view that triggers `action` when a system Cut command occurs.

## See Also

### Copying items using item providers

`func onCopyCommand(perform: (() -> [NSItemProvider])?) -> some View`

Adds an action to perform in response to the system’s Copy command.

`func onPasteCommand(of: [UTType], perform: ([NSItemProvider]) -> Void) ->
some View`

Adds an action to perform in response to the system’s Paste command.

`func onPasteCommand<Payload>(of: [UTType], validator: ([NSItemProvider]) ->
Payload?, perform: (Payload) -> Void) -> some View`

Adds an action to perform in response to the system’s Paste command with items
that you validate.

Instance Method

# onPasteCommand(of:perform:)

Adds an action to perform in response to the system’s Paste command.

macOS 11.0+

    
    
    func onPasteCommand(
        of supportedContentTypes: [UTType],
        perform payloadAction: @escaping ([NSItemProvider]) -> Void
    ) -> some View
    

##  Parameters

`supportedContentTypes`

    

The uniform type identifiers that describe the types of content this view can
accept through a paste action. If the Clipboard doesn’t contain any of the
supported types, the Paste command doesn’t trigger.

`payloadAction`

    

The action to perform when the Paste command triggers. The action closure’s
parameter contains items from the Clipboard with the types you specify in the
`supportedContentTypes` parameter.

## Return Value

A view that triggers `action` when a system Paste command occurs.

## Discussion

Pass an array of uniform type identifiers to the `supportedContentTypes`
parameter. Place the higher priority types closer to the beginning of the
array. The Clipboard items that the `action` closure receives have the most
preferred type out of all the types the source supports.

For example, if your app can handle plain text and rich text, but you prefer
rich text, place the rich text type first in the array. If rich text is
available when the paste action occurs, the `action` closure passes that rich
text along.

## See Also

### Copying items using item providers

`func onCopyCommand(perform: (() -> [NSItemProvider])?) -> some View`

Adds an action to perform in response to the system’s Copy command.

`func onCutCommand(perform: (() -> [NSItemProvider])?) -> some View`

Adds an action to perform in response to the system’s Cut command.

`func onPasteCommand<Payload>(of: [UTType], validator: ([NSItemProvider]) ->
Payload?, perform: (Payload) -> Void) -> some View`

Adds an action to perform in response to the system’s Paste command with items
that you validate.

Instance Method

# onPasteCommand(of:validator:perform:)

Adds an action to perform in response to the system’s Paste command with items
that you validate.

macOS 11.0+

    
    
    func onPasteCommand<Payload>(
        of supportedContentTypes: [UTType],
        validator: @escaping ([NSItemProvider]) -> Payload?,
        perform payloadAction: @escaping (Payload) -> Void
    ) -> some View
    

##  Parameters

`supportedContentTypes`

    

The uniform type identifiers that describe the types of content this view can
accept through a paste action. If the Clipboard doesn’t contain any of the
supported types, the Paste command doesn’t trigger.

`validator`

    

A handler that validates the command. This handler receives items from the
Clipboard with the types you specify in the `supportedContentTypes`. Use this
handler to decide whether the items are valid and preprocess them for the
`action` closure. If you return `nil` instead, the Paste command doesn’t
trigger.

`payloadAction`

    

The action to perform when the Paste command triggers.

## Return Value

A view that triggers `action` when the system Paste command is invoked,
validating the Paste command with `validator`.

## Discussion

Pass an array of uniform type identifiers to the `supportedContentTypes`
parameter. Place the higher priority types closer to the beginning of the
array. The Clipboard items that the `validator` closure receives have the most
preferred type out of all the types the source supports.

For example, if your app can handle plain text and rich text, but you prefer
rich text, place the rich text type first in the array. If rich text is
available when the paste action occurs, the `validator` closure passes that
rich text along.

## See Also

### Copying items using item providers

`func onCopyCommand(perform: (() -> [NSItemProvider])?) -> some View`

Adds an action to perform in response to the system’s Copy command.

`func onCutCommand(perform: (() -> [NSItemProvider])?) -> some View`

Adds an action to perform in response to the system’s Cut command.

`func onPasteCommand(of: [UTType], perform: ([NSItemProvider]) -> Void) ->
some View`

Adds an action to perform in response to the system’s Paste command.

Instance Method

# onDrag(_:preview:)

Activates this view as the source of a drag and drop operation.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    func onDrag<V>(
        _ data: @escaping () -> NSItemProvider,
        @ViewBuilder preview: () -> V
    ) -> some View where V : View
    

##  Parameters

`data`

    

A closure that returns a single `NSItemProvider` that represents the draggable
data from this view.

`preview`

    

A `View` to use as the source for the dragging preview, once the drag
operation has begun. The preview is centered over the source view.

## Return Value

A view that activates this view as the source of a drag-and- drop operation,
beginning with user gesture input.

## Discussion

Applying the `onDrag(_:preview:)` modifier adds the appropriate gestures for
drag and drop to this view. When a drag operation begins, a rendering of
`preview` is generated and used as the preview image.

## See Also

### Moving items using item providers

`func itemProvider(Optional<() -> NSItemProvider?>) -> some View`

Provides a closure that vends the drag representation to be used for a
particular data element.

`func onDrag(() -> NSItemProvider) -> some View`

Activates this view as the source of a drag and drop operation.

`func onDrop(of: [UTType], isTargeted: Binding<Bool>?, perform:
([NSItemProvider]) -> Bool) -> some View`

Defines the destination of a drag-and-drop operation that handles the dropped
content with a closure that you specify.

`func onDrop(of: [UTType], isTargeted: Binding<Bool>?, perform:
([NSItemProvider], CGPoint) -> Bool) -> some View`

Defines the destination of a drag and drop operation that handles the dropped
content with a closure that you specify.

`func onDrop(of: [UTType], delegate: any DropDelegate) -> some View`

Defines the destination of a drag and drop operation using behavior controlled
by the delegate that you provide.

`protocol DropDelegate`

An interface that you implement to interact with a drop operation in a view
modified to accept drops.

`struct DropProposal`

The behavior of a drop.

`enum DropOperation`

Operation types that determine how a drag and drop session resolves when the
user drops a drag item.

`struct DropInfo`

The current state of a drop.

Instance Method

# onDrag(_:)

Activates this view as the source of a drag and drop operation.

iOS 13.4+  iPadOS 13.4+  macOS 10.15+  Mac Catalyst 13.4+  visionOS 1.0+

    
    
    func onDrag(_ data: @escaping () -> NSItemProvider) -> some View
    

##  Parameters

`data`

    

A closure that returns a single `NSItemProvider` that represents the draggable
data from this view.

## Return Value

A view that activates this view as the source of a drag and drop operation,
beginning with user gesture input.

## Discussion

Applying the `onDrag(_:)` modifier adds the appropriate gestures for drag and
drop to this view. When a drag operation begins, a rendering of this view is
generated and used as the preview image.

## See Also

### Moving items using item providers

`func itemProvider(Optional<() -> NSItemProvider?>) -> some View`

Provides a closure that vends the drag representation to be used for a
particular data element.

`func onDrag<V>(() -> NSItemProvider, preview: () -> V) -> some View`

Activates this view as the source of a drag and drop operation.

`func onDrop(of: [UTType], isTargeted: Binding<Bool>?, perform:
([NSItemProvider]) -> Bool) -> some View`

Defines the destination of a drag-and-drop operation that handles the dropped
content with a closure that you specify.

`func onDrop(of: [UTType], isTargeted: Binding<Bool>?, perform:
([NSItemProvider], CGPoint) -> Bool) -> some View`

Defines the destination of a drag and drop operation that handles the dropped
content with a closure that you specify.

`func onDrop(of: [UTType], delegate: any DropDelegate) -> some View`

Defines the destination of a drag and drop operation using behavior controlled
by the delegate that you provide.

`protocol DropDelegate`

An interface that you implement to interact with a drop operation in a view
modified to accept drops.

`struct DropProposal`

The behavior of a drop.

`enum DropOperation`

Operation types that determine how a drag and drop session resolves when the
user drops a drag item.

`struct DropInfo`

The current state of a drop.

Instance Method

# itemProvider(_:)

Provides a closure that vends the drag representation to be used for a
particular data element.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func itemProvider(_ action: Optional<() -> NSItemProvider?>) -> some View
    

## See Also

### Moving items using item providers

`func onDrag<V>(() -> NSItemProvider, preview: () -> V) -> some View`

Activates this view as the source of a drag and drop operation.

`func onDrag(() -> NSItemProvider) -> some View`

Activates this view as the source of a drag and drop operation.

`func onDrop(of: [UTType], isTargeted: Binding<Bool>?, perform:
([NSItemProvider]) -> Bool) -> some View`

Defines the destination of a drag-and-drop operation that handles the dropped
content with a closure that you specify.

`func onDrop(of: [UTType], isTargeted: Binding<Bool>?, perform:
([NSItemProvider], CGPoint) -> Bool) -> some View`

Defines the destination of a drag and drop operation that handles the dropped
content with a closure that you specify.

`func onDrop(of: [UTType], delegate: any DropDelegate) -> some View`

Defines the destination of a drag and drop operation using behavior controlled
by the delegate that you provide.

`protocol DropDelegate`

An interface that you implement to interact with a drop operation in a view
modified to accept drops.

`struct DropProposal`

The behavior of a drop.

`enum DropOperation`

Operation types that determine how a drag and drop session resolves when the
user drops a drag item.

`struct DropInfo`

The current state of a drop.

Instance Method

# onDrop(of:isTargeted:perform:)

Defines the destination of a drag-and-drop operation that handles the dropped
content with a closure that you specify.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    func onDrop(
        of supportedContentTypes: [UTType],
        isTargeted: Binding<Bool>?,
        perform action: @escaping ([NSItemProvider]) -> Bool
    ) -> some View
    

##  Parameters

`supportedContentTypes`

    

The uniform type identifiers that describe the types of content this view can
accept through drag and drop. If the drag-and-drop operation doesn’t contain
any of the supported types, then this drop destination doesn’t activate and
`isTargeted` doesn’t update.

`isTargeted`

    

A binding that updates when a drag and drop operation enters or exits the drop
target area. The binding’s value is `true` when the cursor is inside the area,
and `false` when the cursor is outside.

`action`

    

A closure that takes the dropped content and responds appropriately. The
parameter to `action` contains the dropped items, with types specified by
`supportedContentTypes`. Return `true` if the drop operation was successful;
otherwise, return `false`.

## Return Value

A view that provides a drop destination for a drag operation of the specified
types.

## Discussion

The drop destination is the same size and position as this view.

## See Also

### Moving items using item providers

`func itemProvider(Optional<() -> NSItemProvider?>) -> some View`

Provides a closure that vends the drag representation to be used for a
particular data element.

`func onDrag<V>(() -> NSItemProvider, preview: () -> V) -> some View`

Activates this view as the source of a drag and drop operation.

`func onDrag(() -> NSItemProvider) -> some View`

Activates this view as the source of a drag and drop operation.

`func onDrop(of: [UTType], isTargeted: Binding<Bool>?, perform:
([NSItemProvider], CGPoint) -> Bool) -> some View`

Defines the destination of a drag and drop operation that handles the dropped
content with a closure that you specify.

`func onDrop(of: [UTType], delegate: any DropDelegate) -> some View`

Defines the destination of a drag and drop operation using behavior controlled
by the delegate that you provide.

`protocol DropDelegate`

An interface that you implement to interact with a drop operation in a view
modified to accept drops.

`struct DropProposal`

The behavior of a drop.

`enum DropOperation`

Operation types that determine how a drag and drop session resolves when the
user drops a drag item.

`struct DropInfo`

The current state of a drop.

Instance Method

# onDrop(of:isTargeted:perform:)

Defines the destination of a drag and drop operation that handles the dropped
content with a closure that you specify.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    func onDrop(
        of supportedContentTypes: [UTType],
        isTargeted: Binding<Bool>?,
        perform action: @escaping ([NSItemProvider], CGPoint) -> Bool
    ) -> some View
    

##  Parameters

`supportedContentTypes`

    

The uniform type identifiers that describe the types of content this view can
accept through drag and drop. If the drag and drop operation doesn’t contain
any of the supported types, then this drop destination doesn’t activate and
`isTargeted` doesn’t update.

`isTargeted`

    

A binding that updates when a drag and drop operation enters or exits the drop
target area. The binding’s value is `true` when the cursor is inside the area,
and `false` when the cursor is outside.

`action`

    

A closure that takes the dropped content and responds appropriately. The first
parameter to `action` contains the dropped items, with types specified by
`supportedContentTypes`. The second parameter contains the drop location in
this view’s coordinate space. Return `true` if the drop operation was
successful; otherwise, return `false`.

## Return Value

A view that provides a drop destination for a drag operation of the specified
types.

## Discussion

The drop destination is the same size and position as this view.

## See Also

### Moving items using item providers

`func itemProvider(Optional<() -> NSItemProvider?>) -> some View`

Provides a closure that vends the drag representation to be used for a
particular data element.

`func onDrag<V>(() -> NSItemProvider, preview: () -> V) -> some View`

Activates this view as the source of a drag and drop operation.

`func onDrag(() -> NSItemProvider) -> some View`

Activates this view as the source of a drag and drop operation.

`func onDrop(of: [UTType], isTargeted: Binding<Bool>?, perform:
([NSItemProvider]) -> Bool) -> some View`

Defines the destination of a drag-and-drop operation that handles the dropped
content with a closure that you specify.

`func onDrop(of: [UTType], delegate: any DropDelegate) -> some View`

Defines the destination of a drag and drop operation using behavior controlled
by the delegate that you provide.

`protocol DropDelegate`

An interface that you implement to interact with a drop operation in a view
modified to accept drops.

`struct DropProposal`

The behavior of a drop.

`enum DropOperation`

Operation types that determine how a drag and drop session resolves when the
user drops a drag item.

`struct DropInfo`

The current state of a drop.

Instance Method

# onDrop(of:delegate:)

Defines the destination of a drag and drop operation using behavior controlled
by the delegate that you provide.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    func onDrop(
        of supportedContentTypes: [UTType],
        delegate: any DropDelegate
    ) -> some View
    

##  Parameters

`supportedContentTypes`

    

The uniform type identifiers that describe the types of content this view can
accept through drag and drop. If the drag and drop operation doesn’t contain
any of the supported types, then this drop destination doesn’t activate and
`isTargeted` doesn’t update.

`delegate`

    

A type that conforms to the `DropDelegate` protocol. You have comprehensive
control over drop behavior when you use a delegate.

## Return Value

A view that provides a drop destination for a drag operation of the specified
types.

## Discussion

The drop destination is the same size and position as this view.

## See Also

### Moving items using item providers

`func itemProvider(Optional<() -> NSItemProvider?>) -> some View`

Provides a closure that vends the drag representation to be used for a
particular data element.

`func onDrag<V>(() -> NSItemProvider, preview: () -> V) -> some View`

Activates this view as the source of a drag and drop operation.

`func onDrag(() -> NSItemProvider) -> some View`

Activates this view as the source of a drag and drop operation.

`func onDrop(of: [UTType], isTargeted: Binding<Bool>?, perform:
([NSItemProvider]) -> Bool) -> some View`

Defines the destination of a drag-and-drop operation that handles the dropped
content with a closure that you specify.

`func onDrop(of: [UTType], isTargeted: Binding<Bool>?, perform:
([NSItemProvider], CGPoint) -> Bool) -> some View`

Defines the destination of a drag and drop operation that handles the dropped
content with a closure that you specify.

`protocol DropDelegate`

An interface that you implement to interact with a drop operation in a view
modified to accept drops.

`struct DropProposal`

The behavior of a drop.

`enum DropOperation`

Operation types that determine how a drag and drop session resolves when the
user drops a drag item.

`struct DropInfo`

The current state of a drop.

Instance Method

# dropDestination(for:action:isTargeted:)

Defines the destination of a drag and drop operation that handles the dropped
content with a closure that you specify.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    func dropDestination<T>(
        for payloadType: T.Type = T.self,
        action: @escaping ([T], CGPoint) -> Bool,
        isTargeted: @escaping (Bool) -> Void = { _ in }
    ) -> some View where T : Transferable
    

##  Parameters

`payloadType`

    

The expected type of the dropped models.

`action`

    

A closure that takes the dropped content and responds appropriately. The first
parameter to `action` contains the dropped items. The second parameter
contains the drop location in this view’s coordinate space. Return `true` if
the drop operation was successful; otherwise, return `false`.

`isTargeted`

    

A closure that is called when a drag and drop operation enters or exits the
drop target area. The received value is `true` when the cursor is inside the
area, and `false` when the cursor is outside.

## Return Value

A view that provides a drop destination for a drag operation of the specified
type.

## Discussion

The dropped content can be provided as binary data, file URLs, or file
promises.

The drop destination is the same size and position as this view.

## See Also

### Moving transferable items

`func draggable<T>(() -> T) -> some View`

Activates this view as the source of a drag and drop operation.

`func draggable<V, T>(() -> T, preview: () -> V) -> some View`

Activates this view as the source of a drag and drop operation.

Instance Method

# draggable(_:)

Activates this view as the source of a drag and drop operation.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    func draggable<T>(_ payload: @autoclosure @escaping () -> T) -> some View where T : Transferable
    

##  Parameters

`payload`

    

A closure that returns a single instance or a value conforming to
`Transferable` that represents the draggable data from this view.

## Return Value

A view that activates this view as the source of a drag and drop operation,
beginning with user gesture input.

## Discussion

Applying the `draggable(_:)` modifier adds the appropriate gestures for drag
and drop to this view. When a drag operation begins, a rendering of this view
is generated and used as the preview image.

## See Also

### Moving transferable items

`func draggable<V, T>(() -> T, preview: () -> V) -> some View`

Activates this view as the source of a drag and drop operation.

`func dropDestination<T>(for: T.Type, action: ([T], CGPoint) -> Bool,
isTargeted: (Bool) -> Void) -> some View`

Defines the destination of a drag and drop operation that handles the dropped
content with a closure that you specify.

Instance Method

# draggable(_:preview:)

Activates this view as the source of a drag and drop operation.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    func draggable<V, T>(
        _ payload: @autoclosure @escaping () -> T,
        @ViewBuilder preview: () -> V
    ) -> some View where V : View, T : Transferable
    

##  Parameters

`payload`

    

A closure that returns a single class instance or a value conforming to
`Transferable` that represents the draggable data from this view.

`preview`

    

A `View` to use as the source for the dragging preview, once the drag
operation has begun. The preview is centered over the source view.

## Return Value

A view that activates this view as the source of a drag and drop operation,
beginning with user gesture input.

## Discussion

Applying the `draggable(_:preview:)` modifier adds the appropriate gestures
for drag and drop to this view. When a drag operation begins, a rendering of
`preview` is generated and used as the preview image.

## See Also

### Moving transferable items

`func draggable<T>(() -> T) -> some View`

Activates this view as the source of a drag and drop operation.

`func dropDestination<T>(for: T.Type, action: ([T], CGPoint) -> Bool,
isTargeted: (Bool) -> Void) -> some View`

Defines the destination of a drag and drop operation that handles the dropped
content with a closure that you specify.

Instance Method

# springLoadingBehavior(_:)

Sets the spring loading behavior this view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func springLoadingBehavior(_ behavior: SpringLoadingBehavior) -> some View
    

##  Parameters

`behavior`

    

Whether spring loading is enabled or not. If unspecified, the default behavior
is `.automatic.`

## Discussion

Spring loading refers to a view being activated during a drag and drop
interaction. On iOS this can occur when pausing briefly on top of a view with
dragged content. On macOS this can occur with similar brief pauses or on
pressure-sensitive systems by “force clicking” during the drag. This has no
effect on tvOS or watchOS.

This is commonly used with views that have a navigation or presentation
effect, allowing the destination to be revealed without pausing the drag
interaction. For example, a button that reveals a list of folders that a
dragged item can be dropped onto.

Unlike `disabled(_:)`, this modifier overrides the value set by an ancestor
view rather than being unioned with it. For example, the below button would
allow spring loading:

## See Also

### Configuring spring loading

`var springLoadingBehavior: SpringLoadingBehavior`

The behavior of spring loaded interactions for the views associated with this
environment.

`struct SpringLoadingBehavior`

The options for controlling the spring loading behavior of views.

Instance Method

# onSubmit(of:_:)

Adds an action to perform when the user submits a value to this view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func onSubmit(
        of triggers: SubmitTriggers = .text,
        _ action: @escaping (() -> Void)
    ) -> some View
    

##  Parameters

`triggers`

    

The triggers that should invoke the provided action.

`action`

    

The action to perform on submission of a value.

## Discussion

Different views may have different triggers for the provided action. A
`TextField`, or `SecureField` will trigger this action when the user hits the
hardware or software return key. This modifier may also bind this action to a
default action keyboard shortcut. You may set this action on an individual
view or an entire view hierarchy.

You can use the `submitScope(_:)` modifier to stop a submit trigger from a
control from propagating higher up in the view hierarchy to higher
`View.onSubmit(of:_:)` modifiers.

You can use different submit triggers to filter the types of triggers that
should invoke the provided submission action. For example, you may provide a
value of `search` to only hear submission triggers that originate from search
fields vended by searchable modifiers.

## See Also

### Responding to submission events

`func submitScope(Bool) -> some View`

Prevents submission triggers originating from this view to invoke a submission
action configured by a submission modifier higher up in the view hierarchy.

`struct SubmitTriggers`

A type that defines various triggers that result in the firing of a submission
action.

Instance Method

# submitScope(_:)

Prevents submission triggers originating from this view to invoke a submission
action configured by a submission modifier higher up in the view hierarchy.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func submitScope(_ isBlocking: Bool = true) -> some View
    

##  Parameters

`isBlocking`

    

A Boolean that indicates whether this scope is actively blocking submission
triggers from reaching higher submission actions.

## Discussion

Use this modifier when you want to avoid specific views from initiating a
submission action configured by the `onSubmit(of:_:)` modifier. In the example
below, the tag field doesn’t trigger the submission of the form:

## See Also

### Responding to submission events

`func onSubmit(of: SubmitTriggers, (() -> Void)) -> some View`

Adds an action to perform when the user submits a value to this view.

`struct SubmitTriggers`

A type that defines various triggers that result in the firing of a submission
action.

Instance Method

# submitLabel(_:)

Sets the submit label for this view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func submitLabel(_ submitLabel: SubmitLabel) -> some View
    

##  Parameters

`submitLabel`

    

One of the cases specified in `SubmitLabel`.

## Discussion

## See Also

### Labeling a submission event

`struct SubmitLabel`

A semantic label describing the label of submission within a view hierarchy.

Instance Method

# onMoveCommand(perform:)

Adds an action to perform in response to a move command, like when the user
presses an arrow key on a Mac keyboard, or taps the edge of the Siri Remote
when controlling an Apple TV.

macOS 10.15+  tvOS 13.0+

    
    
    func onMoveCommand(perform action: ((MoveCommandDirection) -> Void)?) -> some View
    

## See Also

### Responding to commands

`func onDeleteCommand(perform: (() -> Void)?) -> some View`

Adds an action to perform in response to the system’s Delete command, or
pressing either the ⌫ (backspace) or ⌦ (forward delete) keys while the view
has focus.

`func pageCommand<V>(value: Binding<V>, in: ClosedRange<V>, step: V) -> some
View`

Steps a value through a range in response to page up or page down commands.

`func onExitCommand(perform: (() -> Void)?) -> some View`

Sets up an action that triggers in response to receiving the exit command
while the view has focus.

`func onPlayPauseCommand(perform: (() -> Void)?) -> some View`

Adds an action to perform in response to the system’s Play/Pause command.

`func onCommand(Selector, perform: (() -> Void)?) -> some View`

Adds an action to perform in response to the given selector.

`enum MoveCommandDirection`

Specifies the direction of an arrow key movement.

Instance Method

# moveDisabled(_:)

Adds a condition for whether the view’s view hierarchy is movable.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func moveDisabled(_ isDisabled: Bool) -> some View
    

## See Also

### Editing a list

`func deleteDisabled(Bool) -> some View`

Adds a condition for whether the view’s view hierarchy is deletable.

`var editMode: Binding<EditMode>?`

An indication of whether the user can edit the contents of a view associated
with this environment.

`enum EditMode`

A mode that indicates whether the user can edit a view’s content.

`struct EditActions`

A set of edit actions on a collection of data that a view can offer to a user.

`struct EditableCollectionContent`

An opaque wrapper view that adds editing capabilities to a row in a list.

`struct IndexedIdentifierCollection`

A collection wrapper that iterates over the indices and identifiers of a
collection together.

Instance Method

# onDeleteCommand(perform:)

Adds an action to perform in response to the system’s Delete command, or
pressing either the ⌫ (backspace) or ⌦ (forward delete) keys while the view
has focus.

macOS 10.15+

    
    
    func onDeleteCommand(perform action: (() -> Void)?) -> some View
    

## See Also

### Responding to commands

`func onMoveCommand(perform: ((MoveCommandDirection) -> Void)?) -> some View`

Adds an action to perform in response to a move command, like when the user
presses an arrow key on a Mac keyboard, or taps the edge of the Siri Remote
when controlling an Apple TV.

`func pageCommand<V>(value: Binding<V>, in: ClosedRange<V>, step: V) -> some
View`

Steps a value through a range in response to page up or page down commands.

`func onExitCommand(perform: (() -> Void)?) -> some View`

Sets up an action that triggers in response to receiving the exit command
while the view has focus.

`func onPlayPauseCommand(perform: (() -> Void)?) -> some View`

Adds an action to perform in response to the system’s Play/Pause command.

`func onCommand(Selector, perform: (() -> Void)?) -> some View`

Adds an action to perform in response to the given selector.

`enum MoveCommandDirection`

Specifies the direction of an arrow key movement.

Instance Method

# deleteDisabled(_:)

Adds a condition for whether the view’s view hierarchy is deletable.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func deleteDisabled(_ isDisabled: Bool) -> some View
    

## See Also

### Editing a list

`func moveDisabled(Bool) -> some View`

Adds a condition for whether the view’s view hierarchy is movable.

`var editMode: Binding<EditMode>?`

An indication of whether the user can edit the contents of a view associated
with this environment.

`enum EditMode`

A mode that indicates whether the user can edit a view’s content.

`struct EditActions`

A set of edit actions on a collection of data that a view can offer to a user.

`struct EditableCollectionContent`

An opaque wrapper view that adds editing capabilities to a row in a list.

`struct IndexedIdentifierCollection`

A collection wrapper that iterates over the indices and identifiers of a
collection together.

Instance Method

# pageCommand(value:in:step:)

Steps a value through a range in response to page up or page down commands.

tvOS 14.3+

    
    
    func pageCommand<V>(
        value: Binding<V>,
        in bounds: ClosedRange<V>,
        step: V = 1
    ) -> some View where V : BinaryInteger
    

##  Parameters

`value`

    

A `Binding` to the value to modify when the user pages up or down.

`bounds`

    

A closed range that specifies the upper and lower bounds of `value`.

`step`

    

The amount by which to increment or decrement `value`. Defaults to 1.

## Discussion

Use this command to step through sections of a data model associated with a
view by providing a binding to a value, a range, and step. If taking another
step would cause the value to exceed the bounds, then the value remains
unchanged.

On tvOS, the user triggers ‘pageUp’ and ‘pageDown’ commands by pressing a
dedicated button on a connected remote. For example, you can let a user page
through a TV programming guide using the channel buttons:

## See Also

### Responding to commands

`func onMoveCommand(perform: ((MoveCommandDirection) -> Void)?) -> some View`

Adds an action to perform in response to a move command, like when the user
presses an arrow key on a Mac keyboard, or taps the edge of the Siri Remote
when controlling an Apple TV.

`func onDeleteCommand(perform: (() -> Void)?) -> some View`

Adds an action to perform in response to the system’s Delete command, or
pressing either the ⌫ (backspace) or ⌦ (forward delete) keys while the view
has focus.

`func onExitCommand(perform: (() -> Void)?) -> some View`

Sets up an action that triggers in response to receiving the exit command
while the view has focus.

`func onPlayPauseCommand(perform: (() -> Void)?) -> some View`

Adds an action to perform in response to the system’s Play/Pause command.

`func onCommand(Selector, perform: (() -> Void)?) -> some View`

Adds an action to perform in response to the given selector.

`enum MoveCommandDirection`

Specifies the direction of an arrow key movement.

Instance Method

# onExitCommand(perform:)

Sets up an action that triggers in response to receiving the exit command
while the view has focus.

macOS 10.15+  tvOS 13.0+

    
    
    func onExitCommand(perform action: (() -> Void)?) -> some View
    

## Discussion

The user generates an exit command by pressing the Menu button on tvOS, or the
escape key on macOS.

## See Also

### Responding to commands

`func onMoveCommand(perform: ((MoveCommandDirection) -> Void)?) -> some View`

Adds an action to perform in response to a move command, like when the user
presses an arrow key on a Mac keyboard, or taps the edge of the Siri Remote
when controlling an Apple TV.

`func onDeleteCommand(perform: (() -> Void)?) -> some View`

Adds an action to perform in response to the system’s Delete command, or
pressing either the ⌫ (backspace) or ⌦ (forward delete) keys while the view
has focus.

`func pageCommand<V>(value: Binding<V>, in: ClosedRange<V>, step: V) -> some
View`

Steps a value through a range in response to page up or page down commands.

`func onPlayPauseCommand(perform: (() -> Void)?) -> some View`

Adds an action to perform in response to the system’s Play/Pause command.

`func onCommand(Selector, perform: (() -> Void)?) -> some View`

Adds an action to perform in response to the given selector.

`enum MoveCommandDirection`

Specifies the direction of an arrow key movement.

Instance Method

# onPlayPauseCommand(perform:)

Adds an action to perform in response to the system’s Play/Pause command.

tvOS 13.0+

    
    
    func onPlayPauseCommand(perform action: (() -> Void)?) -> some View
    

## See Also

### Responding to commands

`func onMoveCommand(perform: ((MoveCommandDirection) -> Void)?) -> some View`

Adds an action to perform in response to a move command, like when the user
presses an arrow key on a Mac keyboard, or taps the edge of the Siri Remote
when controlling an Apple TV.

`func onDeleteCommand(perform: (() -> Void)?) -> some View`

Adds an action to perform in response to the system’s Delete command, or
pressing either the ⌫ (backspace) or ⌦ (forward delete) keys while the view
has focus.

`func pageCommand<V>(value: Binding<V>, in: ClosedRange<V>, step: V) -> some
View`

Steps a value through a range in response to page up or page down commands.

`func onExitCommand(perform: (() -> Void)?) -> some View`

Sets up an action that triggers in response to receiving the exit command
while the view has focus.

`func onCommand(Selector, perform: (() -> Void)?) -> some View`

Adds an action to perform in response to the given selector.

`enum MoveCommandDirection`

Specifies the direction of an arrow key movement.

Instance Method

# onCommand(_:perform:)

Adds an action to perform in response to the given selector.

macOS 10.15+

    
    
    func onCommand(
        _ selector: Selector,
        perform action: (() -> Void)?
    ) -> some View
    

##  Parameters

`selector`

    

The selector to register for `action`.

`action`

    

The action to perform. If `action` is `nil`, `command` keeps its association
with this view but doesn’t trigger.

## Return Value

A view that triggers `action` when the `command` occurs.

## Discussion

This view or one of the views it contains must be in focus in order for the
action to trigger. Other actions for the same command on views _closer_ to the
view in focus take priority, potentially overriding this action.

## See Also

### Responding to commands

`func onMoveCommand(perform: ((MoveCommandDirection) -> Void)?) -> some View`

Adds an action to perform in response to a move command, like when the user
presses an arrow key on a Mac keyboard, or taps the edge of the Siri Remote
when controlling an Apple TV.

`func onDeleteCommand(perform: (() -> Void)?) -> some View`

Adds an action to perform in response to the system’s Delete command, or
pressing either the ⌫ (backspace) or ⌦ (forward delete) keys while the view
has focus.

`func pageCommand<V>(value: Binding<V>, in: ClosedRange<V>, step: V) -> some
View`

Steps a value through a range in response to page up or page down commands.

`func onExitCommand(perform: (() -> Void)?) -> some View`

Sets up an action that triggers in response to receiving the exit command
while the view has focus.

`func onPlayPauseCommand(perform: (() -> Void)?) -> some View`

Adds an action to perform in response to the system’s Play/Pause command.

`enum MoveCommandDirection`

Specifies the direction of an arrow key movement.

Instance Method

# digitalCrownAccessory(_:)

Specifies the visibility of Digital Crown accessory Views on Apple Watch.

watchOS 9.0+

    
    
    func digitalCrownAccessory(_ visibility: Visibility) -> some View
    

##  Parameters

`visibility`

    

The visibility of the digital crown accessory.

## Discussion

Use this method to customize the visibility of a Digital Crown accessory
`View` created with the `View/digitalCrownAccessory(_ content:)` modifier. You
may want to keep an accessory visible even when the Digital Crown Indicator is
not visible to indicate what scrolling the crown will do.

## See Also

### Interacting with the Digital Crown

`func digitalCrownAccessory<Content>(content: () -> Content) -> some View`

Places an accessory View next to the Digital Crown on Apple Watch.

`func digitalCrownRotation<V>(Binding<V>, from: V, through: V, sensitivity:
DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>, onChange: (DigitalCrownEvent) ->
Void, onIdle: () -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(detent: Binding<V>, from: V, through: V, by:
V.Stride, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(detent: Binding<V>, from: V, through: V, by:
V.Stride, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>, from: V, through: V, by: V.Stride?,
sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`struct DigitalCrownEvent`

An event emitted when the user rotates the Digital Crown.

`enum DigitalCrownRotationalSensitivity`

The amount of Digital Crown rotation needed to move between two integer
numbers.

Instance Method

# digitalCrownAccessory(content:)

Places an accessory View next to the Digital Crown on Apple Watch.

watchOS 9.0+

    
    
    func digitalCrownAccessory<Content>(@ViewBuilder content: @escaping () -> Content) -> some View where Content : View
    

##  Parameters

`content`

    

The view to be used as a Digital Crown Accessory.

## Discussion

Use this method to place a custom `View` next to the Digital Crown on Apple
Watch. Use `digitalCrownAccessory(_:)` to specify the visibility of your
custom view.

## See Also

### Interacting with the Digital Crown

`func digitalCrownAccessory(Visibility) -> some View`

Specifies the visibility of Digital Crown accessory Views on Apple Watch.

`func digitalCrownRotation<V>(Binding<V>, from: V, through: V, sensitivity:
DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>, onChange: (DigitalCrownEvent) ->
Void, onIdle: () -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(detent: Binding<V>, from: V, through: V, by:
V.Stride, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(detent: Binding<V>, from: V, through: V, by:
V.Stride, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>, from: V, through: V, by: V.Stride?,
sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`struct DigitalCrownEvent`

An event emitted when the user rotates the Digital Crown.

`enum DigitalCrownRotationalSensitivity`

The amount of Digital Crown rotation needed to move between two integer
numbers.

Instance Method

#
digitalCrownRotation(_:from:through:sensitivity:isContinuous:isHapticFeedbackEnabled:onChange:onIdle:)

Tracks Digital Crown rotations by updating the specified binding.

watchOS 9.0+

    
    
    func digitalCrownRotation<V>(
        _ binding: Binding<V>,
        from minValue: V,
        through maxValue: V,
        sensitivity: DigitalCrownRotationalSensitivity = .high,
        isContinuous: Bool = false,
        isHapticFeedbackEnabled: Bool = true,
        onChange: @escaping (DigitalCrownEvent) -> Void = { _ in },
        onIdle: @escaping () -> Void = { }
    ) -> some View where V : BinaryFloatingPoint
    

##  Parameters

`binding`

    

A binding to a value that updates when the user rotates the Digital Crown.

`minValue`

    

Lower end of the range reported.

`maxValue`

    

Upper end of the range reported.

`sensitivity`

    

How much the user needs to rotate the Digital Crown to move between two
integer numbers.

`isContinuous`

    

Controls if the value reported stops at `minValue` and `maxValue`, or if it
should wrap around. Default is `false`.

`isHapticFeedbackEnabled`

    

Controls the generation of haptic feedback when turning the Digital Crown.
Default is `true`.

`onChange`

    

A block that is called as the Digital Crown is rotated.

`onIdle`

    

A block that is called when the Digital Crown has settled to an idle state.

## Discussion

Use this method to receive continuous values on a binding you provides as the
user turns the Digital Crown on Apple Watch. The example below receives
changes to the binding value, starting at the `minValue` of `0.0` up to the
`maxValue` of `10.0` settling in to multiples of `0.1` increasing or
decreasing depending on the direction that the user turns the Digital Crown,
rolling over if the user exceeds the specified boundary values:

## See Also

### Interacting with the Digital Crown

`func digitalCrownAccessory(Visibility) -> some View`

Specifies the visibility of Digital Crown accessory Views on Apple Watch.

`func digitalCrownAccessory<Content>(content: () -> Content) -> some View`

Places an accessory View next to the Digital Crown on Apple Watch.

`func digitalCrownRotation<V>(Binding<V>, onChange: (DigitalCrownEvent) ->
Void, onIdle: () -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(detent: Binding<V>, from: V, through: V, by:
V.Stride, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(detent: Binding<V>, from: V, through: V, by:
V.Stride, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>, from: V, through: V, by: V.Stride?,
sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`struct DigitalCrownEvent`

An event emitted when the user rotates the Digital Crown.

`enum DigitalCrownRotationalSensitivity`

The amount of Digital Crown rotation needed to move between two integer
numbers.

Instance Method

# digitalCrownRotation(_:onChange:onIdle:)

Tracks Digital Crown rotations by updating the specified binding.

watchOS 9.0+

    
    
    func digitalCrownRotation<V>(
        _ binding: Binding<V>,
        onChange: @escaping (DigitalCrownEvent) -> Void = { _ in },
        onIdle: @escaping () -> Void = { }
    ) -> some View where V : BinaryFloatingPoint
    

##  Parameters

`binding`

    

A binding to a value that updates as the user rotates the Digital Crown. The
implicit range is `(-infinity, +infinity)`.

`onChange`

    

A block that is called as the Digital Crown is rotated.

`onIdle`

    

A block that is called when the Digital Crown has settled to an idle state.

## Discussion

Use this method to receive values on a binding you provide as the user turns
the Digital Crown on Apple Watch. The example below receives changes to the
binding value, starting at `0.0` and incrementing or decrementing depending on
the direction that the user turns the Digital Crown:

## See Also

### Interacting with the Digital Crown

`func digitalCrownAccessory(Visibility) -> some View`

Specifies the visibility of Digital Crown accessory Views on Apple Watch.

`func digitalCrownAccessory<Content>(content: () -> Content) -> some View`

Places an accessory View next to the Digital Crown on Apple Watch.

`func digitalCrownRotation<V>(Binding<V>, from: V, through: V, sensitivity:
DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(detent: Binding<V>, from: V, through: V, by:
V.Stride, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(detent: Binding<V>, from: V, through: V, by:
V.Stride, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>, from: V, through: V, by: V.Stride?,
sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`struct DigitalCrownEvent`

An event emitted when the user rotates the Digital Crown.

`enum DigitalCrownRotationalSensitivity`

The amount of Digital Crown rotation needed to move between two integer
numbers.

Instance Method

#
digitalCrownRotation(detent:from:through:by:sensitivity:isContinuous:isHapticFeedbackEnabled:onChange:onIdle:)

Tracks Digital Crown rotations by updating the specified binding.

watchOS 9.0+

    
    
    func digitalCrownRotation<V>(
        detent: Binding<V>,
        from minValue: V,
        through maxValue: V,
        by stride: V.Stride,
        sensitivity: DigitalCrownRotationalSensitivity = .high,
        isContinuous: Bool = false,
        isHapticFeedbackEnabled: Bool = true,
        onChange: @escaping (DigitalCrownEvent) -> Void = { _ in },
        onIdle: @escaping () -> Void = { }
    ) -> some View where V : BinaryFloatingPoint, V.Stride : BinaryFloatingPoint
    

##  Parameters

`detent`

    

A binding to a value that updates when the user rotates the Digital Crown.

`minValue`

    

Lower end of the range reported.

`maxValue`

    

Upper end of the range reported.

`stride`

    

The value settles on multiples of `stride`.

`sensitivity`

    

How much the user needs to rotate the Digital Crown to move between two
detents.

`isContinuous`

    

Controls if the value reported stops at `minValue` and `maxValue`, or if it
should wrap around. Default is `false`.

`isHapticFeedbackEnabled`

    

Controls the generation of haptic feedback when turning the Digital Crown.
Default is `true`.

`onChange`

    

A block that is called as the Digital Crown is rotated.

`onIdle`

    

A block that is called when the Digital Crown has settled to an idle state.

## Discussion

Use this method to receive values on a binding you provide as the user turns
the Digital Crown on Apple Watch. The example below receives changes to the
binding value, starting at the `minValue` of `0.0` up to the `maxValue` of
`10.0` in steps of `0.1` incrementing or decrementing depending on the
direction that the user turns the Digital Crown, rolling over if the user
exceeds the specified boundary values. The binding will always be updated to a
value that is a multiple of the stride that is provided:

## See Also

### Interacting with the Digital Crown

`func digitalCrownAccessory(Visibility) -> some View`

Specifies the visibility of Digital Crown accessory Views on Apple Watch.

`func digitalCrownAccessory<Content>(content: () -> Content) -> some View`

Places an accessory View next to the Digital Crown on Apple Watch.

`func digitalCrownRotation<V>(Binding<V>, from: V, through: V, sensitivity:
DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>, onChange: (DigitalCrownEvent) ->
Void, onIdle: () -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(detent: Binding<V>, from: V, through: V, by:
V.Stride, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>, from: V, through: V, by: V.Stride?,
sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`struct DigitalCrownEvent`

An event emitted when the user rotates the Digital Crown.

`enum DigitalCrownRotationalSensitivity`

The amount of Digital Crown rotation needed to move between two integer
numbers.

Instance Method

#
digitalCrownRotation(detent:from:through:by:sensitivity:isContinuous:isHapticFeedbackEnabled:onChange:onIdle:)

Tracks Digital Crown rotations by updating the specified binding.

watchOS 9.0+

    
    
    func digitalCrownRotation<V>(
        detent: Binding<V>,
        from minValue: V,
        through maxValue: V,
        by stride: V.Stride,
        sensitivity: DigitalCrownRotationalSensitivity = .high,
        isContinuous: Bool = false,
        isHapticFeedbackEnabled: Bool = true,
        onChange: @escaping (DigitalCrownEvent) -> Void = { _ in },
        onIdle: @escaping () -> Void = { }
    ) -> some View where V : BinaryInteger, V.Stride : BinaryInteger
    

##  Parameters

`binding`

    

A binding to a value that updates when the user rotates the Digital Crown.

`minValue`

    

Lower end of the range reported.

`maxValue`

    

Upper end of the range reported.

`stride`

    

The value settles on multiples of `stride`.

`sensitivity`

    

How much the user needs to rotate the Digital Crown to move between two
integer numbers.

`isContinuous`

    

Controls if the value reported stops at `minValue` and `maxValue`, or if it
should wrap around. Default is `false`.

`isHapticFeedbackEnabled`

    

Controls the generation of haptic feedback when turning the Digital Crown.
Default is `true`.

`onChange`

    

A block that is called as the Digital Crown is rotated.

`onIdle`

    

A block that is called when the Digital Crown has settled to an idle state.

## Discussion

Use this method to receive values on a binding you provides as the user turns
the Digital Crown on Apple Watch. The example below receives changes to the
binding value, starting at the `minValue` of `0` up to the `maxValue` of `100`
in steps of `1` incrementing or decrementing depending on the direction that
the user turns the Digital Crown, rolling over if the user exceeds the
specified boundary values. The binding will always be updated to a value that
is a multiple of the stride that is provided:

## See Also

### Interacting with the Digital Crown

`func digitalCrownAccessory(Visibility) -> some View`

Specifies the visibility of Digital Crown accessory Views on Apple Watch.

`func digitalCrownAccessory<Content>(content: () -> Content) -> some View`

Places an accessory View next to the Digital Crown on Apple Watch.

`func digitalCrownRotation<V>(Binding<V>, from: V, through: V, sensitivity:
DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>, onChange: (DigitalCrownEvent) ->
Void, onIdle: () -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(detent: Binding<V>, from: V, through: V, by:
V.Stride, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>, from: V, through: V, by: V.Stride?,
sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`struct DigitalCrownEvent`

An event emitted when the user rotates the Digital Crown.

`enum DigitalCrownRotationalSensitivity`

The amount of Digital Crown rotation needed to move between two integer
numbers.

Instance Method

# digitalCrownRotation(_:)

Tracks Digital Crown rotations by updating the specified binding.

watchOS 6.0+

    
    
    func digitalCrownRotation<V>(_ binding: Binding<V>) -> some View where V : BinaryFloatingPoint
    

##  Parameters

`binding`

    

A binding to a value that updates as the user rotates the Digital Crown. The
implicit range is `(-infinity, +infinity)`.

## Discussion

Use this method to receive values on a binding you provide as the user turns
the Digital Crown on Apple Watch. The example below receives changes to the
binding value, starting at `0.0` and incrementing or decrementing depending on
the direction that the user turns the Digital Crown:

## See Also

### Interacting with the Digital Crown

`func digitalCrownAccessory(Visibility) -> some View`

Specifies the visibility of Digital Crown accessory Views on Apple Watch.

`func digitalCrownAccessory<Content>(content: () -> Content) -> some View`

Places an accessory View next to the Digital Crown on Apple Watch.

`func digitalCrownRotation<V>(Binding<V>, from: V, through: V, sensitivity:
DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>, onChange: (DigitalCrownEvent) ->
Void, onIdle: () -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(detent: Binding<V>, from: V, through: V, by:
V.Stride, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(detent: Binding<V>, from: V, through: V, by:
V.Stride, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>, from: V, through: V, by: V.Stride?,
sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`struct DigitalCrownEvent`

An event emitted when the user rotates the Digital Crown.

`enum DigitalCrownRotationalSensitivity`

The amount of Digital Crown rotation needed to move between two integer
numbers.

Instance Method

#
digitalCrownRotation(_:from:through:by:sensitivity:isContinuous:isHapticFeedbackEnabled:)

Tracks Digital Crown rotations by updating the specified binding.

watchOS 6.0+

    
    
    func digitalCrownRotation<V>(
        _ binding: Binding<V>,
        from minValue: V,
        through maxValue: V,
        by stride: V.Stride? = nil,
        sensitivity: DigitalCrownRotationalSensitivity = .high,
        isContinuous: Bool = false,
        isHapticFeedbackEnabled: Bool = true
    ) -> some View where V : BinaryFloatingPoint, V.Stride : BinaryFloatingPoint
    

##  Parameters

`binding`

    

A binding to a value that updates when the user rotates the Digital Crown.

`minValue`

    

Lower end of the range reported.

`maxValue`

    

Upper end of the range reported.

`stride`

    

The value settles on multiples of `stride`.

`sensitivity`

    

How much the user needs to rotate the Digital Crown to move between two
integer numbers.

`isContinuous`

    

Controls if the value reported stops at `minValue` and `maxValue`, or if it
should wrap around. Default is `false`.

`isHapticFeedbackEnabled`

    

Controls the generation of haptic feedback when turning the Digital Crown.
Default is `true`.

## Discussion

Use this method to receive values on a binding you provides as the user turns
the Digital Crown on Apple Watch. The example below receives changes to the
binding value, starting at the `minValue` of `0.0` up to the `maxValue` of
`10.0` in steps of `0.1` incrementing or decrementing depending on the
direction that the user turns the Digital Crown, rolling over if the user
exceeds the specified boundary values:

## See Also

### Interacting with the Digital Crown

`func digitalCrownAccessory(Visibility) -> some View`

Specifies the visibility of Digital Crown accessory Views on Apple Watch.

`func digitalCrownAccessory<Content>(content: () -> Content) -> some View`

Places an accessory View next to the Digital Crown on Apple Watch.

`func digitalCrownRotation<V>(Binding<V>, from: V, through: V, sensitivity:
DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>, onChange: (DigitalCrownEvent) ->
Void, onIdle: () -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(detent: Binding<V>, from: V, through: V, by:
V.Stride, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(detent: Binding<V>, from: V, through: V, by:
V.Stride, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool,
isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle:
() -> Void) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`func digitalCrownRotation<V>(Binding<V>) -> some View`

Tracks Digital Crown rotations by updating the specified binding.

`struct DigitalCrownEvent`

An event emitted when the user rotates the Digital Crown.

`enum DigitalCrownRotationalSensitivity`

The amount of Digital Crown rotation needed to move between two integer
numbers.

Instance Method

# userActivity(_:element:_:)

Advertises a user activity type.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func userActivity<P>(
        _ activityType: String,
        element: P?,
        _ update: @escaping (P, NSUserActivity) -> ()
    ) -> some View
    

##  Parameters

`activityType`

    

The type of activity to advertise.

`element`

    

If the element is `nil`, the handler will not be associated with the activity
(and if there are no handlers, no activity is advertised). The method passes
the non-`nil` element to the handler as a convenience so the handlers don’t
all need to implement an early exit with `guard element = element else {
return }`.

`update`

    

A function that modifies the passed-in activity for advertisement.

## Discussion

The scope of the activity applies only to the scene or window the view is in.

## See Also

### Sending and receiving user activities

Restoring Your App’s State with SwiftUI

Provide app continuity for users by preserving their current activities.

`func userActivity(String, isActive: Bool, (NSUserActivity) -> ()) -> some
View`

Advertises a user activity type.

`func onContinueUserActivity(String, perform: (NSUserActivity) -> ()) -> some
View`

Registers a handler to invoke in response to a user activity that your app
receives.

Instance Method

# userActivity(_:isActive:_:)

Advertises a user activity type.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func userActivity(
        _ activityType: String,
        isActive: Bool = true,
        _ update: @escaping (NSUserActivity) -> ()
    ) -> some View
    

##  Parameters

`activityType`

    

The type of activity to advertise.

`isActive`

    

When `false`, avoids advertising the activity. Defaults to `true`.

`update`

    

A function that modifies the passed-in activity for advertisement.

## Discussion

You can use `userActivity(_:isActive:_:)` to start, stop, or modify the
advertisement of a specific type of user activity.

The scope of the activity applies only to the scene or window the view is in.

## See Also

### Sending and receiving user activities

Restoring Your App’s State with SwiftUI

Provide app continuity for users by preserving their current activities.

`func userActivity<P>(String, element: P?, (P, NSUserActivity) -> ()) -> some
View`

Advertises a user activity type.

`func onContinueUserActivity(String, perform: (NSUserActivity) -> ()) -> some
View`

Registers a handler to invoke in response to a user activity that your app
receives.

Instance Method

# onContinueUserActivity(_:perform:)

Registers a handler to invoke in response to a user activity that your app
receives.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func onContinueUserActivity(
        _ activityType: String,
        perform action: @escaping (NSUserActivity) -> ()
    ) -> some View
    

##  Parameters

`activityType`

    

The type of activity that the `action` closure handles. Be sure that this
string matches one of the values that you list in the `NSUserActivityTypes`
array in your app’s Information Property List.

`action`

    

A closure that SwiftUI calls when your app receives a user activity of the
specified type. The closure takes the activity as an input parameter.

## Return Value

A view that handles incoming user activities.

## Discussion

Use this view modifier to receive `NSUserActivity` instances in a particular
scene within your app. The scene that SwiftUI routes the incoming user
activity to depends on the structure of your app, what scenes are active, and
other configuration. For more information, see
`handlesExternalEvents(matching:)`.

UI frameworks traditionally pass Universal Links to your app using a user
activity. However, SwiftUI passes a Universal Link to your app directly as a
URL. To receive a Universal Link, use the `onOpenURL(perform:)` modifier
instead.

## See Also

### Sending and receiving user activities

Restoring Your App’s State with SwiftUI

Provide app continuity for users by preserving their current activities.

`func userActivity<P>(String, element: P?, (P, NSUserActivity) -> ()) -> some
View`

Advertises a user activity type.

`func userActivity(String, isActive: Bool, (NSUserActivity) -> ()) -> some
View`

Advertises a user activity type.

Instance Method

# handlesExternalEvents(preferring:allowing:)

Specifies the external events that the view’s scene handles if the scene is
already open.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    func handlesExternalEvents(
        preferring: Set<String>,
        allowing: Set<String>
    ) -> some View
    

##  Parameters

`preferring`

    

A set of strings that SwiftUI compares against the incoming user activity or
URL to see if the view’s scene prefers to handle the external event.

`allowing`

    

A set of strings that SwiftUI compares against the incoming user activity or
URL to see if the view’s scene can handle the exernal event.

## Return Value

A view whose enclosing scene — if already open — handles incoming external
events.

## Discussion

Apply this modifier to a view to indicate whether an open scene that contains
the view handles specified user activities or URLs that your app receives.
Specify two sets of string identifiers to distinguish between the kinds of
events that the scene _prefers_ to handle and those that it _can_ handle. You
can dynamically update the identifiers in each set to reflect changing app
state.

When your app receives an event on a platform that supports multiple
simultaneous scenes, SwiftUI sends the event to the first open scene it finds
that prefers to handle the event. Otherwise, it sends the event to the first
open scene it finds that can handle the event. If it finds neither — including
when you don’t add this view modifier — SwiftUI creates a new scene for the
event.

Important

Don’t confuse this view modifier with the `handlesExternalEvents(matching:)`
_scene_ modifier. You use the view modifier to indicate that an open scene
handles certain events, whereas you use the scene modifier to help SwiftUI
choose a new scene to open when no open scene handles the event.

On platforms that support only a single scene, SwiftUI ignores this modifier
and sends all external events to the one open scene.

### Matching an event

To find an open scene that handles a particular external event, SwiftUI
compares a property of the event against the strings that you specify in the
`preferring` and `allowing` sets. SwiftUI examines the following event
properties to perform the comparison:

  * For an `NSUserActivity`, like when your app handles Handoff, SwiftUI uses the activity’s `targetContentIdentifier` property, or if that’s `nil`, its `webpageURL` property rendered as an `absoluteString`.

  * For a `URL`, like when another process opens a URL that your app handles, SwiftUI uses the URL’s `absoluteString`.

For both parameter sets, an empty set of strings never matches. Similarly,
empty strings never match. Conversely, as a special case, the string that
contains only an asterisk (`*`) matches anything. The modifier performs string
comparisons that are case and diacritic insensitive.

If you specify multiple instances of this view modifier inside a single scene,
the scene uses the union of the respective `preferring` and `allowing` sets
from all the modifiers.

### Handling a user activity in an open scene

As an example, the following view — which participates in Handoff through the
`userActivity(_:isActive:_:)` and `onContinueUserActivity(_:perform:)` methods
— updates its `preferring` set according to the current selection. The
enclosing scene prefers to handle an event for a contact that’s already
selected, but doesn’t volunteer itself as a preferred scene when no contact is
selected:

The above code also updates the `allowing` set to indicate that the scene can
handle any incoming event when there’s no current selection, but that it can’t
handle any event if the view already displays a contact. The `preferring` set
takes precedence in the special case where the incoming event exactly matches
the currently selected contact.

## See Also

### Handling external events

`func handlesExternalEvents(matching: Set<String>) -> some Scene`

Specifies the external events for which SwiftUI opens a new instance of the
modified scene.

Instance Method

# onAppear(perform:)

Adds an action to perform before this view appears.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func onAppear(perform action: (() -> Void)? = nil) -> some View
    

##  Parameters

`action`

    

The action to perform. If `action` is `nil`, the call has no effect.

## Return Value

A view that triggers `action` before it appears.

## Discussion

The exact moment that SwiftUI calls this method depends on the specific view
type that you apply it to, but the `action` closure completes before the first
rendered frame appears.

## See Also

### Responding to view life cycle updates

`func onDisappear(perform: (() -> Void)?) -> some View`

Adds an action to perform after this view disappears.

`func task(priority: TaskPriority, () async -> Void) -> some View`

Adds an asynchronous task to perform before this view appears.

`func task<T>(id: T, priority: TaskPriority, () async -> Void) -> some View`

Adds a task to perform before this view appears or when a specified value
changes.

Instance Method

# onDisappear(perform:)

Adds an action to perform after this view disappears.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func onDisappear(perform action: (() -> Void)? = nil) -> some View
    

##  Parameters

`action`

    

The action to perform. If `action` is `nil`, the call has no effect.

## Return Value

A view that triggers `action` after it disappears.

## Discussion

The exact moment that SwiftUI calls this method depends on the specific view
type that you apply it to, but the `action` closure doesn’t execute until the
view disappears from the interface.

## See Also

### Responding to view life cycle updates

`func onAppear(perform: (() -> Void)?) -> some View`

Adds an action to perform before this view appears.

`func task(priority: TaskPriority, () async -> Void) -> some View`

Adds an asynchronous task to perform before this view appears.

`func task<T>(id: T, priority: TaskPriority, () async -> Void) -> some View`

Adds a task to perform before this view appears or when a specified value
changes.

Instance Method

# onChange(of:initial:_:)

Adds a modifier for this view that fires an action when a specific value
changes.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func onChange<V>(
        of value: V,
        initial: Bool = false,
        _ action: @escaping () -> Void
    ) -> some View where V : Equatable
    

##  Parameters

`value`

    

The value to check against when determining whether to run the closure.

`initial`

    

Whether the action should be run when this view initially appears.

`action`

    

A closure to run when the value changes.

## Return Value

A view that fires an action when the specified value changes.

## Discussion

You can use `onChange` to trigger a side effect as the result of a value
changing, such as an `Environment` key or a `Binding`.

The system may call the action closure on the main actor, so avoid long-
running tasks in the closure. If you need to perform such tasks, detach an
asynchronous background task.

When the value changes, the new version of the closure will be called, so any
captured values will have their values from the time that the observed value
has its new value. In the following code example, `PlayerView` calls into its
model when `playState` changes model.

## See Also

### Responding to data changes

`func onChange<V>(of: V, initial: Bool, (V, V) -> Void) -> some View`

Adds a modifier for this view that fires an action when a specific value
changes.

`func onReceive<P>(P, perform: (P.Output) -> Void) -> some View`

Adds an action to perform when this view detects data emitted by the given
publisher.

Instance Method

# onChange(of:initial:_:)

Adds a modifier for this view that fires an action when a specific value
changes.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func onChange<V>(
        of value: V,
        initial: Bool = false,
        _ action: @escaping (V, V) -> Void
    ) -> some View where V : Equatable
    

##  Parameters

`value`

    

The value to check against when determining whether to run the closure.

`initial`

    

Whether the action should be run when this view initially appears.

`action`

    

A closure to run when the value changes.

`oldValue`

    

The old value that failed the comparison check (or the initial value when
requested).

`newValue`

    

The new value that failed the comparison check.

## Return Value

A view that fires an action when the specified value changes.

## Discussion

You can use `onChange` to trigger a side effect as the result of a value
changing, such as an `Environment` key or a `Binding`.

The system may call the action closure on the main actor, so avoid long-
running tasks in the closure. If you need to perform such tasks, detach an
asynchronous background task.

When the value changes, the new version of the closure will be called, so any
captured values will have their values from the time that the observed value
has its new value. The old and new observed values are passed into the
closure. In the following code example, `PlayerView` passes both the old and
new values to the model.

## See Also

### Responding to data changes

`func onChange<V>(of: V, initial: Bool, () -> Void) -> some View`

Adds a modifier for this view that fires an action when a specific value
changes.

`func onReceive<P>(P, perform: (P.Output) -> Void) -> some View`

Adds an action to perform when this view detects data emitted by the given
publisher.

Instance Method

# task(priority:_:)

Adds an asynchronous task to perform before this view appears.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func task(
        priority: TaskPriority = .userInitiated,
        _ action: @escaping () async -> Void
    ) -> some View
    

##  Parameters

`priority`

    

The task priority to use when creating the asynchronous task. The default
priority is `userInitiated`.

`action`

    

A closure that SwiftUI calls as an asynchronous task before the view appears.
SwiftUI will automatically cancel the task at some point after the view
disappears before the action completes.

## Return Value

A view that runs the specified action asynchronously before the view appears.

## Discussion

Use this modifier to perform an asynchronous task with a lifetime that matches
that of the modified view. If the task doesn’t finish before SwiftUI removes
the view or the view changes identity, SwiftUI cancels the task.

Use the `await` keyword inside the task to wait for an asynchronous call to
complete, or to wait on the values of an `AsyncSequence` instance. For
example, you can modify a `Text` view to start a task that loads content from
a remote resource:

This example uses the `lines` method to get the content stored at the
specified `URL` as an asynchronous sequence of strings. When each new line
arrives, the body of the `for`-`await`-`in` loop stores the line in an array
of strings and updates the content of the text view to report the latest line
count.

## See Also

### Responding to view life cycle updates

`func onAppear(perform: (() -> Void)?) -> some View`

Adds an action to perform before this view appears.

`func onDisappear(perform: (() -> Void)?) -> some View`

Adds an action to perform after this view disappears.

`func task<T>(id: T, priority: TaskPriority, () async -> Void) -> some View`

Adds a task to perform before this view appears or when a specified value
changes.

Instance Method

# task(id:priority:_:)

Adds a task to perform before this view appears or when a specified value
changes.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func task<T>(
        id value: T,
        priority: TaskPriority = .userInitiated,
        _ action: @escaping () async -> Void
    ) -> some View where T : Equatable
    

##  Parameters

`id`

    

The value to observe for changes. The value must conform to the `Equatable`
protocol.

`priority`

    

The task priority to use when creating the asynchronous task. The default
priority is `userInitiated`.

`action`

    

A closure that SwiftUI calls as an asynchronous task before the view appears.
SwiftUI can automatically cancel the task after the view disappears before the
action completes. If the `id` value changes, SwiftUI cancels and restarts the
task.

## Return Value

A view that runs the specified action asynchronously before the view appears,
or restarts the task when the `id` value changes.

## Discussion

This method behaves like `task(priority:_:)`, except that it also cancels and
recreates the task when a specified value changes. To detect a change, the
modifier tests whether a new value for the `id` parameter equals the previous
value. For this to work, the value’s type must conform to the `Equatable`
protocol.

For example, if you define an equatable `Server` type that posts custom
notifications whenever its state changes — for example, from _signed out_ to
_signed in_ — you can use the task modifier to update the contents of a `Text`
view to reflect the state of the currently selected server:

This example uses the `notifications(named:object:)` method to create an
asynchronous sequence of notifications, given by an `AsyncSequence` instance.
The example then maps the notification sequence to a sequence of strings that
correspond to values stored with each notification.

Elsewhere, the server defines a custom `didUpdateStatus` notification:

Whenever the server status changes, like after the user signs in, the server
posts a notification of this custom type:

The task attached to the `Text` view gets and displays the status value from
the notification’s user information dictionary. When the user chooses a
different server, SwiftUI cancels the task and creates a new one, which then
waits for notifications from the new server.

## See Also

### Responding to view life cycle updates

`func onAppear(perform: (() -> Void)?) -> some View`

Adds an action to perform before this view appears.

`func onDisappear(perform: (() -> Void)?) -> some View`

Adds an action to perform after this view disappears.

`func task(priority: TaskPriority, () async -> Void) -> some View`

Adds an asynchronous task to perform before this view appears.

Instance Method

# renameAction(_:)

Sets a closure to run for the rename action.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func renameAction(_ action: @escaping () -> Void) -> some View
    

##  Parameters

`action`

    

A closure to run when renaming.

## Return Value

A view that has the specified rename action.

## Discussion

Use this modifier in conjunction with the `RenameButton` to implement standard
rename interactions. A rename button receives its action from the environment.
Use this modifier to customize the action provided to the rename button.

When the user taps the rename button in the context menu, the rename action
focuses the text field by setting the `isFocused` property to true.

## See Also

### Renaming a document

`struct RenameButton`

A button that triggers a standard rename action.

`func renameAction(FocusState<Bool>.Binding) -> some View`

Sets the rename action in the environment to update focus state.

`var rename: RenameAction?`

An action that activates the standard rename interaction.

`struct RenameAction`

An action that activates a standard rename interaction.

Instance Method

# renameAction(_:)

Sets the rename action in the environment to update focus state.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func renameAction(_ isFocused: FocusState<Bool>.Binding) -> some View
    

##  Parameters

`isFocused`

    

The focus binding to update when activating the rename action.

## Return Value

A view that has the specified rename action.

## Discussion

Use this modifier in conjunction with the `RenameButton` to implement standard
rename interactions. A rename button receives its action from the environment.
Use this modifier to customize the action provided to the rename button.

When someone taps the rename button in the context menu, the rename action
focuses the text field by setting the `isFocused` property to true.

## See Also

### Renaming a document

`struct RenameButton`

A button that triggers a standard rename action.

`func renameAction(() -> Void) -> some View`

Sets a closure to run for the rename action.

`var rename: RenameAction?`

An action that activates the standard rename interaction.

`struct RenameAction`

An action that activates a standard rename interaction.

Instance Method

# onOpenURL(perform:)

Registers a handler to invoke in response to a URL that your app receives.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func onOpenURL(perform action: @escaping (URL) -> ()) -> some View
    

##  Parameters

`action`

    

A closure that SwiftUI calls when your app receives a Universal Link or a
custom `URL`. The closure takes the URL as an input parameter.

## Return Value

A view that handles incoming URLs.

## Discussion

Use this view modifier to receive URLs in a particular scene within your app.
The scene that SwiftUI routes the incoming URL to depends on the structure of
your app, what scenes are active, and other configuration. For more
information, see `handlesExternalEvents(matching:)`.

UI frameworks traditionally pass Universal Links to your app using an
`NSUserActivity`. However, SwiftUI passes a Universal Link to your app
directly as a URL, which you receive using this modifier. To receive other
user activities, like when your app participates in Handoff, use the
`onContinueUserActivity(_:perform:)` modifier instead.

For more information about linking into your app, see Allowing apps and
websites to link to your content.

## See Also

### Sending and receiving URLs

`var openURL: OpenURLAction`

An action that opens a URL.

`struct OpenURLAction`

An action that opens a URL.

Instance Method

# widgetURL(_:)

Sets the URL to open in the containing app when the user clicks the widget.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    func widgetURL(_ url: URL?) -> some View
    

##  Parameters

`url`

    

The URL to open in the containing app.

## Return Value

A view that opens the specified URL when the user clicks the widget.

## Overview

Widgets support one `widgetURL` modifier in their view hierarchy. If multiple
views have `widgetURL` modifiers, the behavior is undefined.

## See Also

### URLs

`func onOpenURL(perform: (URL) -> ()) -> some View`

Registers a handler to invoke in response to a URL that your app receives.

Instance Method

# onReceive(_:perform:)

Adds an action to perform when this view detects data emitted by the given
publisher.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func onReceive<P>(
        _ publisher: P,
        perform action: @escaping (P.Output) -> Void
    ) -> some View where P : Publisher, P.Failure == Never
    

##  Parameters

`publisher`

    

The publisher to subscribe to.

`action`

    

The action to perform when an event is emitted by `publisher`. The event
emitted by publisher is passed as a parameter to `action`.

## Return Value

A view that triggers `action` when `publisher` emits an event.

## See Also

### Responding to data changes

`func onChange<V>(of: V, initial: Bool, () -> Void) -> some View`

Adds a modifier for this view that fires an action when a specific value
changes.

`func onChange<V>(of: V, initial: Bool, (V, V) -> Void) -> some View`

Adds a modifier for this view that fires an action when a specific value
changes.

Instance Method

# allowsHitTesting(_:)

Configures whether this view participates in hit test operations.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func allowsHitTesting(_ enabled: Bool) -> some View
    

Instance Method

# contentShape(_:eoFill:)

Defines the content shape for hit testing.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func contentShape<S>(
        _ shape: S,
        eoFill: Bool = false
    ) -> some View where S : Shape
    

##  Parameters

`shape`

    

The hit testing shape for the view.

`eoFill`

    

A Boolean that indicates whether the shape is interpreted with the even-odd
winding number rule.

## Return Value

A view that uses the given shape for hit testing.

## See Also

### Controlling hit testing

`func allowsTightening(Bool) -> some View`

Sets whether text in this view can compress the space between characters when
necessary to fit text in a line.

`func contentShape<S>(ContentShapeKinds, S, eoFill: Bool) -> some View`

Sets the content shape for this view.

`struct ContentShapeKinds`

A kind for the content shape of a view.

Instance Method

# contentShape(_:_:eoFill:)

Sets the content shape for this view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func contentShape<S>(
        _ kind: ContentShapeKinds,
        _ shape: S,
        eoFill: Bool = false
    ) -> some View where S : Shape
    

##  Parameters

`kind`

    

The kinds to apply to this content shape.

`shape`

    

The shape to use.

`eoFill`

    

A Boolean that indicates whether the shape is interpreted with the even-odd
winding number rule.

## Return Value

A view that uses the given shape for the specified kind.

## Discussion

The content shape has a variety of uses. You can control the kind of the
content shape by specifying one in `kind`. For example, the following example
only sets the focus ring shape of the view, without affecting its shape for
hit-testing:

## See Also

### Controlling hit testing

`func allowsTightening(Bool) -> some View`

Sets whether text in this view can compress the space between characters when
necessary to fit text in a line.

`func contentShape<S>(S, eoFill: Bool) -> some View`

Defines the content shape for hit testing.

`struct ContentShapeKinds`

A kind for the content shape of a view.

Instance Method

# exportsItemProviders(_:onExport:)

Exports a read-only item provider for consumption by shortcuts, quick actions,
and services.

macOS 12.0+

    
    
    func exportsItemProviders(
        _ contentTypes: [UTType],
        onExport: @escaping () -> [NSItemProvider]
    ) -> some View
    

##  Parameters

`contentTypes`

    

The types of content that the view supports exporting. An empty array means
the view does not currently support exporting.

`onExport`

    

A closure that will be called on request of the items by the shortcut or
service.

## Discussion

If the associated view supports selection, the exported item should reflect
that selected subpart.

## See Also

### Importing and exporting using item providers

`func importsItemProviders([UTType], onImport: ([NSItemProvider]) -> Bool) ->
some View`

Enables importing item providers from services, such as Continuity Camera on
macOS.

`func exportsItemProviders([UTType], onExport: () -> [NSItemProvider], onEdit:
([NSItemProvider]) -> Bool) -> some View`

Exports a read-write item provider for consumption by shortcuts, quick
actions, and services.

Instance Method

# exportsItemProviders(_:onExport:onEdit:)

Exports a read-write item provider for consumption by shortcuts, quick
actions, and services.

macOS 12.0+

    
    
    func exportsItemProviders(
        _ contentTypes: [UTType],
        onExport: @escaping () -> [NSItemProvider],
        onEdit: @escaping ([NSItemProvider]) -> Bool
    ) -> some View
    

##  Parameters

`contentTypes`

    

The types of content that the view supports exporting and importing. An empty
array means the view does not currently support exporting.

`onExport`

    

A closure that will be called on request of the items by the shortcut or
service.

`onEdit`

    

A closure that will be called after the shortcut or service completes with its
output data. This should replace the selected subpart that was exported with
`onExport`. Return `false` to indicate that there was a failure to receive the
items.

## Discussion

If the associated view supports selection, the exported item should reflect
that selected subpart.

## See Also

### Importing and exporting using item providers

`func importsItemProviders([UTType], onImport: ([NSItemProvider]) -> Bool) ->
some View`

Enables importing item providers from services, such as Continuity Camera on
macOS.

`func exportsItemProviders([UTType], onExport: () -> [NSItemProvider]) -> some
View`

Exports a read-only item provider for consumption by shortcuts, quick actions,
and services.

Instance Method

# importsItemProviders(_:onImport:)

Enables importing item providers from services, such as Continuity Camera on
macOS.

macOS 12.0+

    
    
    func importsItemProviders(
        _ contentTypes: [UTType],
        onImport: @escaping ([NSItemProvider]) -> Bool
    ) -> some View
    

##  Parameters

`contentTypes`

    

The types of content that the view supports importing. An empty array means
the view does not currently support importing.

`onImport`

    

A closure that will be called with the imported service item. Return `false`
to indicate that there was a failure to receive the items.

## See Also

### Importing and exporting using item providers

`func exportsItemProviders([UTType], onExport: () -> [NSItemProvider]) -> some
View`

Exports a read-only item provider for consumption by shortcuts, quick actions,
and services.

`func exportsItemProviders([UTType], onExport: () -> [NSItemProvider], onEdit:
([NSItemProvider]) -> Bool) -> some View`

Exports a read-write item provider for consumption by shortcuts, quick
actions, and services.

Instance Method

# exportableToServices(_:)

Exports items for consumption by shortcuts, quick actions, and services.

macOS 13.0+

    
    
    func exportableToServices<T>(_ payload: @autoclosure @escaping () -> [T]) -> some View where T : Transferable
    

##  Parameters

`payload`

    

A closure that will be called on request of the items by the shortcut or
service.

## Discussion

If the associated view supports selection, the exported item should reflect
that selected subpart.

## See Also

### Importing and exporting transferable items

`func importableFromServices<T>(for: T.Type, action: ([T]) -> Bool) -> some
View`

Enables importing items from services, such as Continuity Camera on macOS.

`func exportableToServices<T>(() -> [T], onEdit: ([T]) -> Bool) -> some View`

Exports read-write items for consumption by shortcuts, quick actions, and
services.

Instance Method

# exportableToServices(_:onEdit:)

Exports read-write items for consumption by shortcuts, quick actions, and
services.

macOS 13.0+

    
    
    func exportableToServices<T>(
        _ payload: @autoclosure @escaping () -> [T],
        onEdit: @escaping ([T]) -> Bool
    ) -> some View where T : Transferable
    

##  Parameters

`payload`

    

A closure that will be called on request of the items by the shortcut or
service.

`onEdit`

    

A closure that will be called after the shortcut or service completes with its
output data. This should replace the selected subpart that was exported with
`onExport`. Return `false` to indicate that there was a failure to receive the
items.

## Discussion

If the associated view supports selection, the exported item should reflect
that selected subpart.

## See Also

### Importing and exporting transferable items

`func importableFromServices<T>(for: T.Type, action: ([T]) -> Bool) -> some
View`

Enables importing items from services, such as Continuity Camera on macOS.

`func exportableToServices<T>(() -> [T]) -> some View`

Exports items for consumption by shortcuts, quick actions, and services.

Instance Method

# importableFromServices(for:action:)

Enables importing items from services, such as Continuity Camera on macOS.

macOS 13.0+

    
    
    func importableFromServices<T>(
        for payloadType: T.Type = T.self,
        action: @escaping ([T]) -> Bool
    ) -> some View where T : Transferable
    

##  Parameters

`payloadType`

    

The expected type of the imported models.

`action`

    

A closure that will be called with the imported service item. Return `false`
to indicate that there was a failure to receive the items.

## Discussion

## See Also

### Importing and exporting transferable items

`func exportableToServices<T>(() -> [T]) -> some View`

Exports items for consumption by shortcuts, quick actions, and services.

`func exportableToServices<T>(() -> [T], onEdit: ([T]) -> Bool) -> some View`

Exports read-write items for consumption by shortcuts, quick actions, and
services.

Instance Method

# shortcutsLinkStyle(_:)

Sets the given style for ShortcutsLinks within the view hierarchy

AppIntents  SwiftUI  iOS 16.0+  iPadOS 16.0+

    
    
    func shortcutsLinkStyle(_ style: ShortcutsLinkStyle) -> some View
    

##  Parameters

`style`

    

The style to set.

## Return Value

A view that uses the specified shortcuts button style on its child views.

## See Also

### App intents

`func siriTipViewStyle(SiriTipViewStyle) -> some View`

Sets the given style for SiriTipView within the view hierarchy

Instance Method

# siriTipViewStyle(_:)

Sets the given style for SiriTipView within the view hierarchy

AppIntents  SwiftUI  iOS 16.0+  iPadOS 16.0+

    
    
    func siriTipViewStyle(_ style: SiriTipViewStyle) -> some View
    

##  Parameters

`style`

    

The style to set.

## Return Value

A view that uses the specified style on its child views.

## See Also

### App intents

`func shortcutsLinkStyle(ShortcutsLinkStyle) -> some View`

Sets the given style for ShortcutsLinks within the view hierarchy

