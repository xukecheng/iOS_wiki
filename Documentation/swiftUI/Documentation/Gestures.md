Article

# Adding interactivity with gestures

Use gesture modifiers to add interactivity to your app.

## Overview

Gesture modifiers handle all of the logic needed to process user-input events
such as touches, and recognize when those events match a known gesture
pattern, such as a long press or rotation. When recognizing a pattern, SwiftUI
runs a callback you use to update the state of a view or perform an action.

### Add gesture modifiers to a view

Each gesture you add applies to a specific view in the view hierarchy. To
recognize a gesture event on a particular view, create and configure the
gesture, and then use the `gesture(_:including:)` modifier:

### Respond to gesture callbacks

Depending on the callbacks you add to a gesture modifier, SwiftUI reports back
to your code whenever the state of the gesture changes. Gesture modifiers
offer three ways to receive updates: `updating(_:body:)`, `onChanged(_:)`, and
`onEnded(_:)`.

#### Update transient UI state

To update a view as a gesture changes, add a `GestureState` property to your
view and update it in the `updating(_:body:)` callback. SwiftUI invokes the
updating callback as soon as it recognizes the gesture and whenever the value
of the gesture changes. For example, SwiftUI invokes the updating callback as
soon as a magnification gesture begins and then again whenever the
magnification value changes. SwiftUI doesn’t invoke the updating callback when
the user ends or cancels a gesture. Instead, the gesture state property
automatically resets its state back to its initial value.

For example, to make a view that changes color while the user performs a long
press, add a gesture state property and update it in the updating callback.

#### Update permanent state during a gesture

To track changes to a gesture that shouldn’t reset once the gesture ends, use
the `onChanged(_:)` callback. For example, to count the number of times your
app recognizes a long press, add an `onChanged(_:)` callback and increment a
counter.

#### Update permanent state when a gesture ends

To recognize when a gesture successfully completes and to retrieve the
gesture’s final value, use the `onEnded(_:)` function to update your app’s
state in the callback. SwiftUI only invokes the `onEnded(_:)` callback when
the gesture succeeds. For example, during a `LongPressGesture` if the user
stops touching the view before `minimumDuration` seconds have elapsed or moves
their finger more than `maximumDistance` points SwiftUI does not invoke the
`onEnded(_:)` callback.

For example, to stop counting long press attempts after the user completes a
long press, add an `onEnded(_:)` callback and conditionally apply the gesture
modifier.

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

Structure

# TapGesture

A gesture that recognizes one or more taps.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 16.0+  watchOS
6.0+  visionOS 1.0+

    
    
    struct TapGesture

## Overview

To recognize a tap gesture on a view, create and configure the gesture, and
then add it to the view using the `gesture(_:including:)` modifier. The
following code adds a tap gesture to a `Circle` that toggles the color of the
circle:

## Topics

### Creating a tap gesture

`init(count: Int)`

Creates a tap gesture with the number of required taps.

`var count: Int`

The required number of tap events.

## Relationships

### Conforms To

  * `Gesture`

## See Also

### Recognizing tap gestures

`func onTapGesture(count: Int, perform: () -> Void) -> some View`

Adds an action to perform when this view recognizes a tap gesture.

`func onTapGesture(count: Int, coordinateSpace: some CoordinateSpaceProtocol,
perform: (CGPoint) -> Void) -> some View`

Adds an action to perform when this view recognizes a tap gesture, and
provides the action with the location of the interaction.

`struct SpatialTapGesture`

A gesture that recognizes one or more taps and reports their location.

Structure

# SpatialTapGesture

A gesture that recognizes one or more taps and reports their location.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    struct SpatialTapGesture

## Overview

To recognize a tap gesture on a view, create and configure the gesture, and
then add it to the view using the `gesture(_:including:)` modifier. The
following code adds a tap gesture to a `Circle` that toggles the color of the
circle based on the tap location:

## Topics

### Creating a spatial tap gesture

`init(count: Int, coordinateSpace: some CoordinateSpaceProtocol)`

Creates a tap gesture with the number of required taps and the coordinate
space of the gesture’s location.

`var coordinateSpace: CoordinateSpace`

The coordinate space in which to receive location values.

`var count: Int`

The required number of tap events.

### Getting the gesture’s value

`struct Value`

The attributes of a tap gesture.

### Deprecated initializers

`init(count: Int, coordinateSpace: CoordinateSpace)`

Creates a tap gesture with the number of required taps and the coordinate
space of the gesture’s location.

Deprecated

## Relationships

### Conforms To

  * `Gesture`

## See Also

### Recognizing tap gestures

`func onTapGesture(count: Int, perform: () -> Void) -> some View`

Adds an action to perform when this view recognizes a tap gesture.

`func onTapGesture(count: Int, coordinateSpace: some CoordinateSpaceProtocol,
perform: (CGPoint) -> Void) -> some View`

Adds an action to perform when this view recognizes a tap gesture, and
provides the action with the location of the interaction.

`struct TapGesture`

A gesture that recognizes one or more taps.

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

Structure

# LongPressGesture

A gesture that succeeds when the user performs a long press.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 14.0+  watchOS
6.0+  visionOS 1.0+

    
    
    struct LongPressGesture

## Overview

To recognize a long-press gesture on a view, create and configure the gesture,
then add it to the view using the `gesture(_:including:)` modifier.

Add a long-press gesture to a `Circle` to animate its color from blue to red,
and then change it to green when the gesture ends:

## Topics

### Creating a long press gesture

`init(minimumDuration: Double)`

Creates a long-press gesture with a minimum duration

`init(minimumDuration: Double, maximumDistance: CGFloat)`

Creates a long-press gesture with a minimum duration and a maximum distance
that the interaction can move before the gesture fails.

`var minimumDuration: Double`

The minimum duration of the long press that must elapse before the gesture
succeeds.

`var maximumDistance: CGFloat`

The maximum distance that the long press can move before the gesture fails.

## Relationships

### Conforms To

  * `Gesture`

## See Also

### Recognizing long press gestures

`func onLongPressGesture(minimumDuration: Double, maximumDistance: CGFloat,
perform: () -> Void, onPressingChanged: ((Bool) -> Void)?) -> some View`

Adds an action to perform when this view recognizes a long press gesture.

`func onLongPressGesture(minimumDuration: Double, perform: () -> Void,
onPressingChanged: ((Bool) -> Void)?) -> some View`

Adds an action to perform when this view recognizes a long press gesture.

`func onLongTouchGesture(minimumDuration: Double, perform: () -> Void,
onTouchingChanged: ((Bool) -> Void)?) -> some View`

Adds an action to perform when this view recognizes a remote long touch
gesture. A long touch gesture is when the finger is on the remote touch
surface without actually pressing.

Structure

# SpatialEventGesture

A gesture that provides information about ongoing spatial events like clicks
and touches.

visionOS 1.0+

    
    
    struct SpatialEventGesture

## Overview

Use a gesture of this type to track multiple simultaneous spatial events and
gain access to detailed information about each. For example, you can place a
particle emitter at every location in a `Canvas` that has an ongoing spatial
event:

The gesture provides a `SpatialEventCollection` structure when it detects
changes. The collection contains `SpatialEventCollection.Event` values that
represent ongoing spatial events. Each event contains a stable, unique
identifier so that you can track how the event changes over time. The event
also indicates its current location, a timestamp, the pose of the input device
that creates it, and other useful information.

The phase of events in the collection can change to
`SpatialEventCollection.Event.Phase.ended` or
`SpatialEventCollection.Event.Phase.cancelled` while the gesture itself
remains active. Individually track state for each event inside `onChanged(_:)`
or `updating(_:body:)` and clean up all state in `onEnded(_:)`.

Tip

Only use a spatial event gesture if you need to access low-level event
information, like when you create a complex multi-touch experience. For most
use cases, it’s better to rely on gestures that recognize targeted
interactions, like a `SpatialTapGesture`, `MagnifyGesture`, or `DragGesture`.

## Topics

### Creating a spatial event gesture

`init(coordinateSpace: any CoordinateSpaceProtocol)`

Creates the gesture with a desired coordinate space.

### Getting gesture properties

`let coordinateSpace: CoordinateSpace`

The coordinate space of the gesture.

## Relationships

### Conforms To

  * `Gesture`

## See Also

### Recognizing spatial events

`struct SpatialEventCollection`

A collection of spatial input events that target a specific view.

Structure

# SpatialEventCollection

A collection of spatial input events that target a specific view.

visionOS 1.0+

    
    
    struct SpatialEventCollection

## Overview

You receive a structure of this type as an input to the `onChanged(_:)` or
`onEnded(_:)` method of a `SpatialEventGesture`. The structure contains a
collection of `SpatialEventCollection.Event` values that correspond to ongoing
input events. You can look up a specific event in the collection by its `id`
value or iterate over all events in the collection to apply logic depending on
the event’s state.

## Topics

### Accessing the collection’s events

`struct Event`

A spatial event generated from an input like a touch or click that can drive
gestures in the system.

`subscript(SpatialEventCollection.Event.ID) -> SpatialEventCollection.Event?`

Retrieves an event using its unique identifier.

### Iterating over events in the collection

`func makeIterator() -> SpatialEventCollection.Iterator`

Makes an iterator over all events in the collection.

`struct Iterator`

An iterator over all events in the collection.

## Relationships

### Conforms To

  * `Collection`
  * `Equatable`
  * `Sequence`

## See Also

### Recognizing spatial events

`struct SpatialEventGesture`

A gesture that provides information about ongoing spatial events like clicks
and touches.

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

Structure

# DragGesture

A dragging motion that invokes an action as the drag-event sequence changes.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    struct DragGesture

## Overview

To recognize a drag gesture on a view, create and configure the gesture, and
then add it to the view using the `gesture(_:including:)` modifier.

Add a drag gesture to a `Circle` and change its color while the user performs
the drag gesture:

## Topics

### Creating a drag gesture

`init(minimumDistance: CGFloat, coordinateSpace: some
CoordinateSpaceProtocol)`

Creates a dragging gesture with the minimum dragging distance before the
gesture succeeds and the coordinate space of the gesture’s location.

`var minimumDistance: CGFloat`

The minimum dragging distance before the gesture succeeds.

`var coordinateSpace: CoordinateSpace`

The coordinate space in which to receive location values.

### Deprecated initializers

`init(minimumDistance: CGFloat, coordinateSpace: CoordinateSpace)`

Creates a dragging gesture with the minimum dragging distance before the
gesture succeeds and the coordinate space of the gesture’s location.

Deprecated

### Structures

`struct Value`

The attributes of a drag gesture.

## Relationships

### Conforms To

  * `Gesture`

## See Also

### Recognizing gestures that change over time

`func gesture<T>(T, including: GestureMask) -> some View`

Attaches a gesture to the view with a lower precedence than gestures defined
by the view.

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

Structure

# MagnifyGesture

A gesture that recognizes a magnification motion and tracks the amount of
magnification.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    struct MagnifyGesture

## Overview

A magnify gesture tracks how a magnification event sequence changes. To
recognize a magnify gesture on a view, create and configure the gesture, and
then add it to the view using the `gesture(_:including:)` modifier.

Add a magnify gesture to a `Circle` that changes its size while the user
performs the gesture:

## Topics

### Creating the gesture

`init(minimumScaleDelta: CGFloat)`

Creates a magnify gesture with a given minimum delta for the gesture to start.

`var minimumScaleDelta: CGFloat`

The minimum required delta before the gesture starts.

## Relationships

### Conforms To

  * `Gesture`

## See Also

### Recognizing gestures that change over time

`func gesture<T>(T, including: GestureMask) -> some View`

Attaches a gesture to the view with a lower precedence than gestures defined
by the view.

`struct DragGesture`

A dragging motion that invokes an action as the drag-event sequence changes.

`struct RotateGesture`

A gesture that recognizes a rotation motion and tracks the angle of the
rotation.

`struct RotateGesture3D`

A gesture that recognizes 3D rotation motion and tracks the angle and axis of
the rotation.

`struct GestureMask`

Options that control how adding a gesture to a view affects other gestures
recognized by the view and its subviews.

Structure

# RotateGesture

A gesture that recognizes a rotation motion and tracks the angle of the
rotation.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    struct RotateGesture

## Overview

A rotate gesture tracks how a rotation event sequence changes. To recognize a
rotate gesture on a view, create and configure the gesture, and then add it to
the view using the `gesture(_:including:)` modifier.

Add a rotate gesture to a `Rectangle` and apply a rotation effect:

## Topics

### Creating the gesture

`init(minimumAngleDelta: Angle)`

Creates a rotation gesture with a minimum delta for the gesture to start.

`var minimumAngleDelta: Angle`

The minimum delta required before the gesture succeeds.

## Relationships

### Conforms To

  * `Gesture`

## See Also

### Recognizing gestures that change over time

`func gesture<T>(T, including: GestureMask) -> some View`

Attaches a gesture to the view with a lower precedence than gestures defined
by the view.

`struct DragGesture`

A dragging motion that invokes an action as the drag-event sequence changes.

`struct MagnifyGesture`

A gesture that recognizes a magnification motion and tracks the amount of
magnification.

`struct RotateGesture3D`

A gesture that recognizes 3D rotation motion and tracks the angle and axis of
the rotation.

`struct GestureMask`

Options that control how adding a gesture to a view affects other gestures
recognized by the view and its subviews.

Structure

# RotateGesture3D

A gesture that recognizes 3D rotation motion and tracks the angle and axis of
the rotation.

visionOS 1.0+

    
    
    struct RotateGesture3D

## Overview

You can constrain this gesture to recognize rotation about a specific 3D axis.
For example, `RotateGesture3D(constrainedToAxis: .x)` creates a gesture that
recognizes rotation only around the global X axis. The axis you provide will
be normalized.

A rotation gesture tracks how a rotation event sequence changes. To recognize
a rotation gesture on a view, create and configure the gesture, and then add
it to the view using the `gesture(_:including:)` modifier.

## Topics

### Creating the gesture

`init(constrainedToAxis: RotationAxis3D?, minimumAngleDelta: Angle)`

Creates a rotation gesture with a minimum delta for the gesture to start and
axis to constrain measurement of rotation.

`var minimumAngleDelta: Angle`

The minimum angle delta before the gesture becomes active.

`var constrainedAxis: RotationAxis3D?`

An axis around which the rotation is constrained.

## Relationships

### Conforms To

  * `Gesture`

## See Also

### Recognizing gestures that change over time

`func gesture<T>(T, including: GestureMask) -> some View`

Attaches a gesture to the view with a lower precedence than gestures defined
by the view.

`struct DragGesture`

A dragging motion that invokes an action as the drag-event sequence changes.

`struct MagnifyGesture`

A gesture that recognizes a magnification motion and tracks the amount of
magnification.

`struct RotateGesture`

A gesture that recognizes a rotation motion and tracks the angle of the
rotation.

`struct GestureMask`

Options that control how adding a gesture to a view affects other gestures
recognized by the view and its subviews.

Structure

# GestureMask

Options that control how adding a gesture to a view affects other gestures
recognized by the view and its subviews.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct GestureMask

## Topics

### Getting gesture options

`static let all: GestureMask`

Enable both the added gesture as well as all other gestures on the view and
its subviews.

`static let gesture: GestureMask`

Enable the added gesture but disable all gestures in the subview hierarchy.

`static let subviews: GestureMask`

Enable all gestures in the subview hierarchy but disable the added gesture.

`static let none: GestureMask`

Disable all gestures in the subview hierarchy, including the added gesture.

## Relationships

### Conforms To

  * `Equatable`
  * `ExpressibleByArrayLiteral`
  * `OptionSet`
  * `RawRepresentable`
  * `Sendable`
  * `SetAlgebra`

## See Also

### Recognizing gestures that change over time

`func gesture<T>(T, including: GestureMask) -> some View`

Attaches a gesture to the view with a lower precedence than gestures defined
by the view.

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

Article

# Composing SwiftUI gestures

Combine gestures to create complex interactions.

## Overview

When you add multiple gestures to your app’s view hierarchy, you need to
decide how the gestures interact with each other. You use gesture composition
to define the order SwiftUI recognizes gestures. There are three gesture
composition types:

  * Simultaneous

  * Sequenced

  * Exclusive

When you combine gesture modifiers simultaneously, SwiftUI must recognize all
subgesture patterns at the same time for it to recognize the combining
gesture. When you sequence gesture modifiers one after the other, SwiftUI must
recognize each subgesture in order. Finally, when you combine gestures
exclusively, SwiftUI recognizes the entire gesture pattern when SwiftUI only
recognizes one subgesture but not the others.

### Sequence one gesture after another

When you sequence one gesture after another, SwiftUI recognizes the first
gesture before it recognizes the second. For example, to require a long press
before the user can drag a view, you sequence a `DragGesture` after a
`LongPressGesture`.

#### Model sequenced gesture states

To make it easier to track complicated states, use an enumeration that
captures all of the states you need to configure your views. In the following
example, there are three important states: no interaction (`inactive`), long
press in progress (`pressing`), and dragging (`dragging`).

#### Create gestures and update the UI state

When you sequence two gestures, the callbacks capture the state of both
gestures. In the update callback, the new `value` uses an enumeration to
represent the combination of the possible gesture states. The code below
converts the underlying gesture states into the high-level `DragState`
enumeration defined above.

When the user begins pressing the view, the drag state changes to `pressing`
and a shadow animates under the shape. After the user finishes the long press
and the drag state changes to `dragging`, a border appears around the shape to
indicate that the user may begin moving the view.

## See Also

### Combining gestures

`func simultaneousGesture<T>(T, including: GestureMask) -> some View`

Attaches a gesture to the view to process simultaneously with gestures defined
by the view.

`struct SequenceGesture`

A gesture that’s a sequence of two gestures.

`struct SimultaneousGesture`

A gesture containing two gestures that can happen at the same time with
neither of them preceding the other.

`struct ExclusiveGesture`

A gesture that consists of two gestures where only one of them can succeed.

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

Structure

# SequenceGesture

A gesture that’s a sequence of two gestures.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct SequenceGesture<First, Second> where First : Gesture, Second : Gesture

## Overview

Read Composing SwiftUI gestures to learn how you can create a sequence of two
gestures.

## Topics

### Creating the gesture

`init(First, Second)`

Creates a sequence gesture with two gestures.

`var first: First`

The first gesture in a sequence of two gestures.

`var second: Second`

The second gesture in a sequence of two gestures.

### Getting the gesture’s values

`enum Value`

The value of a sequence gesture that helps to detect whether the first gesture
succeeded, so the second gesture can start.

## Relationships

### Conforms To

  * `Gesture`

## See Also

### Combining gestures

Composing SwiftUI gestures

Combine gestures to create complex interactions.

`func simultaneousGesture<T>(T, including: GestureMask) -> some View`

Attaches a gesture to the view to process simultaneously with gestures defined
by the view.

`struct SimultaneousGesture`

A gesture containing two gestures that can happen at the same time with
neither of them preceding the other.

`struct ExclusiveGesture`

A gesture that consists of two gestures where only one of them can succeed.

Structure

# SimultaneousGesture

A gesture containing two gestures that can happen at the same time with
neither of them preceding the other.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct SimultaneousGesture<First, Second> where First : Gesture, Second : Gesture

## Overview

A simultaneous gesture is a container-event handler that evaluates its two
child gestures at the same time. Its value is a struct with two optional
values, each representing the phases of one of the two gestures.

## Topics

### Creating the gesture

`init(First, Second)`

Creates a gesture with two gestures that can receive updates or succeed
independently of each other.

`var first: First`

The first of two gestures that can happen simultaneously.

`var second: Second`

The second of two gestures that can happen simultaneously.

### Getting the gesture’s values

`struct Value`

The value of a simultaneous gesture that indicates which of its two gestures
receives events.

## Relationships

### Conforms To

  * `Gesture`

## See Also

### Combining gestures

Composing SwiftUI gestures

Combine gestures to create complex interactions.

`func simultaneousGesture<T>(T, including: GestureMask) -> some View`

Attaches a gesture to the view to process simultaneously with gestures defined
by the view.

`struct SequenceGesture`

A gesture that’s a sequence of two gestures.

`struct ExclusiveGesture`

A gesture that consists of two gestures where only one of them can succeed.

Structure

# ExclusiveGesture

A gesture that consists of two gestures where only one of them can succeed.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct ExclusiveGesture<First, Second> where First : Gesture, Second : Gesture

## Overview

The `ExclusiveGesture` gives precedence to its first gesture.

## Topics

### Creating the gesture

`init(First, Second)`

Creates a gesture from two gestures where only one of them succeeds.

`var first: First`

The first of two gestures.

`var second: Second`

The second of two gestures.

### Supporting types

`enum Value`

The value of an exclusive gesture that indicates which of two gestures
succeeded.

## Relationships

### Conforms To

  * `Gesture`

## See Also

### Combining gestures

Composing SwiftUI gestures

Combine gestures to create complex interactions.

`func simultaneousGesture<T>(T, including: GestureMask) -> some View`

Attaches a gesture to the view to process simultaneously with gestures defined
by the view.

`struct SequenceGesture`

A gesture that’s a sequence of two gestures.

`struct SimultaneousGesture`

A gesture containing two gestures that can happen at the same time with
neither of them preceding the other.

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

Protocol

# Gesture

An instance that matches a sequence of events to a gesture, and returns a
stream of values for each of its states.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    protocol Gesture<Value>

## Overview

Create custom gestures by declaring types that conform to the `Gesture`
protocol.

## Topics

### Implementing a custom gesture

`var body: Self.Body`

The content and behavior of the gesture.

**Required**

` associatedtype Body : Gesture`

The type of gesture representing the body of `Self`.

**Required**

### Performing the gesture

`func updating<State>(GestureState<State>, body: (Self.Value, inout State,
inout Transaction) -> Void) -> GestureStateGesture<Self, State>`

Updates the provided gesture state property as the gesture’s value changes.

`func onChanged((Self.Value) -> Void) -> _ChangedGesture<Self>`

Adds an action to perform when the gesture’s value changes.

Available when `Value` conforms to `Equatable`.

`func onEnded((Self.Value) -> Void) -> _EndedGesture<Self>`

Adds an action to perform when the gesture ends.

`associatedtype Value`

The type representing the gesture’s value.

**Required**

### Composing gestures

`func simultaneously<Other>(with: Other) -> SimultaneousGesture<Self, Other>`

Combines a gesture with another gesture to create a new gesture that
recognizes both gestures at the same time.

`func sequenced<Other>(before: Other) -> SequenceGesture<Self, Other>`

Sequences a gesture with another one to create a new gesture, which results in
the second gesture only receiving events after the first gesture succeeds.

`func exclusively<Other>(before: Other) -> ExclusiveGesture<Self, Other>`

Combines two gestures exclusively to create a new gesture where only one
gesture succeeds, giving precedence to the first gesture.

### Adding modifier keys to a gesture

`func modifiers(EventModifiers) -> _ModifiersGesture<Self>`

Combines a gesture with keyboard modifiers.

### Transforming a gesture

`func map<T>((Self.Value) -> T) -> _MapGesture<Self, T>`

Returns a gesture that’s the result of mapping the given closure over the
gesture.

### Customizing gesture activation

`func handActivationBehavior(HandActivationBehavior) -> some
Gesture<Self.Value> `

Customizes the activation behavior for a gesture when driven by hand or hand-
like input.

### Using a gesture with a RealityKit entity

`func targetedToAnyEntity() -> some Gesture<EntityTargetValue<Self.Value>> `

Require this gesture to target an entity.

`func targetedToEntity(Entity) -> some Gesture<EntityTargetValue<Self.Value>>
`

Require this gesture to target `entity` or a descendant of `entity`. This is
equivalent to `targetedToEntity(.descendingFrom(entity))`.

`func targetedToEntity(where: QueryPredicate<Entity>) -> some
Gesture<EntityTargetValue<Self.Value>> `

Require this gesture to target an entity that can be found in the results of
the specified QueryPredicate

## Relationships

### Conforming Types

  * `AnyGesture`
  * `DragGesture`
  * `ExclusiveGesture`
  * `GestureStateGesture`
  * `LongPressGesture`
  * `MagnificationGesture`
  * `MagnifyGesture`
  * `RotateGesture`
  * `RotateGesture3D`
  * `RotationGesture`
  * `SequenceGesture`
  * `SimultaneousGesture`
  * `SpatialEventGesture`
  * `SpatialTapGesture`
  * `TapGesture`

## See Also

### Defining custom gestures

`func highPriorityGesture<T>(T, including: GestureMask) -> some View`

Attaches a gesture to the view with a higher precedence than gestures defined
by the view.

`func defersSystemGestures(on: Edge.Set) -> some View`

Sets the screen edge from which you want your gesture to take precedence over
the system gesture.

`struct AnyGesture`

A type-erased gesture.

`struct HandActivationBehavior`

An activation behavior specific to hand-driven input.

Structure

# AnyGesture

A type-erased gesture.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct AnyGesture<Value>

## Topics

### Implementing a custom gesture

`init<T>(T)`

Creates an instance from another gesture.

## Relationships

### Conforms To

  * `Gesture`

## See Also

### Defining custom gestures

`func highPriorityGesture<T>(T, including: GestureMask) -> some View`

Attaches a gesture to the view with a higher precedence than gestures defined
by the view.

`func defersSystemGestures(on: Edge.Set) -> some View`

Sets the screen edge from which you want your gesture to take precedence over
the system gesture.

`protocol Gesture`

An instance that matches a sequence of events to a gesture, and returns a
stream of values for each of its states.

`struct HandActivationBehavior`

An activation behavior specific to hand-driven input.

Structure

# HandActivationBehavior

An activation behavior specific to hand-driven input.

visionOS 1.0+

    
    
    struct HandActivationBehavior

## Overview

Hand activation behavior determines what hand input modes activate a gesture.

## Topics

### Getting the behaviors

`static let automatic: HandActivationBehavior`

The default activation behavior, including direct touch, direct pinch, and
indirect pinch.

`static let pinch: HandActivationBehavior`

Activation that requires a pinched hand.

## Relationships

### Conforms To

  * `Equatable`

## See Also

### Defining custom gestures

`func highPriorityGesture<T>(T, including: GestureMask) -> some View`

Attaches a gesture to the view with a higher precedence than gestures defined
by the view.

`func defersSystemGestures(on: Edge.Set) -> some View`

Sets the screen edge from which you want your gesture to take precedence over
the system gesture.

`protocol Gesture`

An instance that matches a sequence of events to a gesture, and returns a
stream of values for each of its states.

`struct AnyGesture`

A type-erased gesture.

Structure

# GestureState

A property wrapper type that updates a property while the user performs a
gesture and resets the property back to its initial state when the gesture
ends.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @propertyWrapper @frozen
    struct GestureState<Value>

## Overview

Declare a property as `@GestureState`, pass as a binding to it as a parameter
to a gesture’s `updating(_:body:)` callback, and receive updates to it. A
property that’s declared as `@GestureState` implicitly resets when the gesture
becomes inactive, making it suitable for tracking transient state.

Add a long-press gesture to a `Circle`, and update the interface during the
gesture by declaring a property as `@GestureState`:

## Topics

### Creating a gesture state

`init(initialValue: Value)`

Creates a view state that’s derived from a gesture with an initial value.

`init(initialValue: Value, reset: (Value, inout Transaction) -> Void)`

Creates a view state that’s derived from a gesture with an initial state value
and a closure that provides a transaction to reset it.

`init(initialValue: Value, resetTransaction: Transaction)`

Creates a view state that’s derived from a gesture with an initial state value
and a transaction to reset it.

`init(reset: (Value, inout Transaction) -> Void)`

Creates a view state that’s derived from a gesture with a closure that
provides a transaction to reset it.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(resetTransaction: Transaction)`

Creates a view state that’s derived from a gesture with a transaction to reset
it.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(wrappedValue: Value)`

Creates a view state that’s derived from a gesture.

`init(wrappedValue: Value, reset: (Value, inout Transaction) -> Void)`

Creates a view state that’s derived from a gesture with a wrapped state value
and a closure that provides a transaction to reset it.

`init(wrappedValue: Value, resetTransaction: Transaction)`

Creates a view state that’s derived from a gesture with a wrapped state value
and a transaction to reset it.

### Getting the state

`var wrappedValue: Value`

The wrapped value referenced by the gesture state property.

`var projectedValue: GestureState<Value>`

A binding to the gesture state property.

## Relationships

### Conforms To

  * `DynamicProperty`

## See Also

### Managing gesture state

`struct GestureStateGesture`

A gesture that updates the state provided by a gesture’s updating callback.

Structure

# GestureStateGesture

A gesture that updates the state provided by a gesture’s updating callback.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct GestureStateGesture<Base, State> where Base : Gesture

## Overview

A gesture’s `updating(_:body:)` callback returns a `GestureStateGesture`
instance for updating a transient state property that’s annotated with the
`GestureState` property wrapper.

## Topics

### Creating an in-progress gesture

`init(base: Base, state: GestureState<State>, body: (GestureStateGesture<Base,
State>.Value, inout State, inout Transaction) -> Void)`

Creates a new gesture that’s the result of an ongoing gesture.

`var base: Base`

The originating gesture.

`var state: GestureState<State>`

A value that changes as the user performs the gesture.

### Supporting types

`var body: (GestureStateGesture<Base, State>.Value, inout State, inout
Transaction) -> Void`

The updating gesture containing the originating gesture’s value, the updated
state of the gesture, and a transaction.

## Relationships

### Conforms To

  * `Gesture`

## See Also

### Managing gesture state

`struct GestureState`

A property wrapper type that updates a property while the user performs a
gesture and resets the property back to its initial state when the gesture
ends.

Structure

# MagnificationGesture

A gesture that recognizes a magnification motion and tracks the amount of
magnification.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  visionOS 1.0+

    
    
    struct MagnificationGesture

Deprecated

Use `MagnifyGesture` instead.

## Topics

### Creating the gesture

`init(minimumScaleDelta: CGFloat)`

Creates a magnification gesture with a given minimum delta for the gesture to
start.

`var minimumScaleDelta: CGFloat`

The minimum required delta before the gesture starts.

## Relationships

### Conforms To

  * `Gesture`

## See Also

### Deprecated gestures

`struct RotationGesture`

A gesture that recognizes a rotation motion and tracks the angle of the
rotation.

Deprecated

Structure

# RotationGesture

A gesture that recognizes a rotation motion and tracks the angle of the
rotation.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  visionOS 1.0+

    
    
    struct RotationGesture

Deprecated

Use `RotateGesture` instead.

## Topics

### Creating the gesture

`init(minimumAngleDelta: Angle)`

Creates a rotation gesture with a minimum delta for the gesture to start.

`var minimumAngleDelta: Angle`

The minimum delta required before the gesture succeeds.

## Relationships

### Conforms To

  * `Gesture`

## See Also

### Deprecated gestures

`struct MagnificationGesture`

A gesture that recognizes a magnification motion and tracks the amount of
magnification.

Deprecated

