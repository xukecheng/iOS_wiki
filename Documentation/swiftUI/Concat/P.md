# PageTabViewStyle.IndexDisplayMode

Type Property

# always

Always display an index view regardless of page count

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS 8.0+
visionOS 1.0+

    
    
    static let always: PageTabViewStyle.IndexDisplayMode

## See Also

### Getting the modes

`static let automatic: PageTabViewStyle.IndexDisplayMode`

Displays an index view when there are more than one page

`static let never: PageTabViewStyle.IndexDisplayMode`

Never display an index view

Type Property

# automatic

Displays an index view when there are more than one page

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS 7.0+
visionOS 1.0+

    
    
    static let automatic: PageTabViewStyle.IndexDisplayMode

## See Also

### Getting the modes

`static let always: PageTabViewStyle.IndexDisplayMode`

Always display an index view regardless of page count

`static let never: PageTabViewStyle.IndexDisplayMode`

Never display an index view

Type Property

# never

Never display an index view

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS 8.0+
visionOS 1.0+

    
    
    static let never: PageTabViewStyle.IndexDisplayMode

## See Also

### Getting the modes

`static let always: PageTabViewStyle.IndexDisplayMode`

Always display an index view regardless of page count

`static let automatic: PageTabViewStyle.IndexDisplayMode`

Displays an index view when there are more than one page



# PopoverAttachmentAnchor

Case

# PopoverAttachmentAnchor.point(_:)

The anchor point for the popover expressed as a unit point that describes
possible alignments relative to a SwiftUI view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case point(UnitPoint)

## See Also

### Getting attachment anchors

`case rect(Anchor<CGRect>.Source)`

The anchor point for the popover relative to the source’s frame.

Case

# PopoverAttachmentAnchor.rect(_:)

The anchor point for the popover relative to the source’s frame.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case rect(Anchor<CGRect>.Source)

## See Also

### Getting attachment anchors

`case point(UnitPoint)`

The anchor point for the popover expressed as a unit point that describes
possible alignments relative to a SwiftUI view.



# PhaseAnimator

Initializer

# init(_:content:animation:)

Cycles through a sequence of phases continuously, animating updates to a view
on each phase change.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init(
        _ phases: some Sequence<Phase>,
        @ViewBuilder content: @escaping (Phase) -> Content,
        animation: @escaping (Phase) -> Animation? = { _ in .default }
    )

##  Parameters

`phases`

    

The sequence of phases to cycle through. Ensure that the sequence isn’t empty.
If it is, SwiftUI logs a runtime warning and also returns a visual warning as
the output view.

`content`

    

A view builder closure that takes the current phase as an input. Return a view
that’s based on the current phase.

`animation`

    

A closure that takes the current phase as input. Return the animation to use
when transitioning to the next phase. If you return `nil`, the transition
doesn’t animate. If you don’t set this parameter, SwiftUI uses a default
animation.

## Discussion

When the phase animator first appears, this initializer renders the `content`
closure using the first phase as input to the closure. The animator then
begins immediately animating to the view produced by sending the second phase
to the `content` closure using the animation returned from the `animation`
closure. This procedure repeats for successive phases until reaching the last
phase, after which the animator loops back to the first phase again.

## See Also

### Creating a phase animator

`init(some Sequence<Phase>, trigger: some Equatable, content: (Phase) ->
Content, animation: (Phase) -> Animation?)`

Cycles through a sequence of phases in response to changes in a specified
value, animating updates to a view on each phase change.

Initializer

# init(_:trigger:content:animation:)

Cycles through a sequence of phases in response to changes in a specified
value, animating updates to a view on each phase change.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init(
        _ phases: some Sequence<Phase>,
        trigger: some Equatable,
        @ViewBuilder content: @escaping (Phase) -> Content,
        animation: @escaping (Phase) -> Animation? = { _ in .default }
    )

##  Parameters

`phases`

    

The sequence of phases to cycle through. Ensure that the sequence isn’t empty.
If it is, SwiftUI logs a runtime warning and also returns a visual warning as
the output view.

`trigger`

    

A value whose changes cause the animator to use the next phase.

`content`

    

A view builder closure that takes the current phase as an input. Return a view
that’s based on the phase input.

`animation`

    

A closure that takes the current phase as input. Return the animation to use
when transitioning to the next phase. If you return `nil`, the transition
doesn’t animate. If you don’t set this parameter, SwiftUI uses a default
animation.

## Discussion

When the phase animator first appears, this initializer renders the `content`
closure using the first phase as input to the closure. When the value of the
`trigger` input changes, the animator reevaluates the `content` closure using
the value from the second phase and animates the change. This procedure
repeats with each successive phase until reaching the last phase, at which
point the animator loops back to the first phase.

## See Also

### Creating a phase animator

`init(some Sequence<Phase>, content: (Phase) -> Content, animation: (Phase) ->
Animation?)`

Cycles through a sequence of phases continuously, animating updates to a view
on each phase change.



# PeriodicTimelineSchedule

Initializer

# init(from:by:)

Creates a periodic update schedule.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init(
        from startDate: Date,
        by interval: TimeInterval
    )

##  Parameters

`startDate`

    

The date on which to start the sequence.

`interval`

    

The time interval between successive sequence entries.

## Discussion

Use the `entries(from:mode:)` method to get the sequence of dates.

Instance Method

# entries(from:mode:)

Provides a sequence of periodic dates starting from around a given date.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func entries(
        from startDate: Date,
        mode: TimelineScheduleMode
    ) -> PeriodicTimelineSchedule.Entries

## Discussion

A `TimelineView` that you create with a schedule calls this method to ask the
schedule when to update its content. The method returns a sequence of equally
spaced dates in increasing order that represent points in time when the
timeline view should update.

The schedule defines its periodicity and phase aligment based on the
parameters you pass to its `init(from:by:)` initializer. For example, for a
`startDate` and `interval` of `10:09:30` and `60` seconds, the schedule
prepares to issue dates half past each minute. The `startDate` that you pass
to the `entries(from:mode:)` method then dictates the first date of the
sequence as the beginning of the interval that the start date overlaps.
Continuing the example above, a start date of `10:34:45` causes the first
sequence entry to be `10:34:30`, because that’s the start of the interval in
which the start date appears.

## See Also

### Getting the sequence of dates

`struct Entries`

The sequence of dates in periodic schedule.

Structure

# PeriodicTimelineSchedule.Entries

The sequence of dates in periodic schedule.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    struct Entries

## Overview

The `entries(from:mode:)` method returns a value of this type, which is a
`Sequence` of periodic dates in ascending order. A `TimelineView` that you
create updates its content at the moments in time corresponding to the dates
included in the sequence.

## Relationships

### Conforms To

  * `IteratorProtocol`
  * `Sendable`
  * `Sequence`

## See Also

### Getting the sequence of dates

`func entries(from: Date, mode: TimelineScheduleMode) ->
PeriodicTimelineSchedule.Entries`

Provides a sequence of periodic dates starting from around a given date.



# ProminentDetailNavigationSplitViewStyle

Initializer

# init()

Creates an instance of `ProminentDetailNavigationSplitViewStyle`.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init()

## Discussion

You can also use `prominentDetail` to construct this style.



# PreviewContext

Instance Subscript

# subscript(_:)

Returns the context’s value for a key, or a the key’s default value if the
context doesn’t define a value for the key.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    subscript<Key>(key: Key.Type) -> Key.Value where Key : PreviewContextKey { get }

**Required**

Instance Subscript

# subscript(_:)

Returns the context’s value for a key, or a the key’s default value if the
context doesn’t define a value for the key.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    subscript<Key>(key: Key.Type) -> Key.Value where Key : PreviewContextKey { get }

**Required**



# PlainWindowStyle

Initializer

# init()

visionOS 1.0+

    
    
    init()



# PlaceholderTextShapeStyle

Initializer

# init()

Creates a new placeholder text shape style.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init()



# PhysicalMetricsConverter

Instance Method

# convert(_:from:)

Converts a point, whose coordinates are in the specified unit, to a point
suitable for use in the environment this converter is associated with.

visionOS 1.0+

    
    
    func convert(
        _ point: CGPoint,
        from unit: UnitLength
    ) -> CGPoint

## Return Value

A value in points. Use this value only in the scene this converter was
associated with.

## See Also

### Converting from a unit length

`func convert(Rect3D, from: UnitLength) -> Rect3D`

Converts a `Rect3D`, whose coordinates are in the specified unit, to a
`Rect3D` with coordinates specified in points, suitable for use in the
environment this converter is associated with.

`func convert(Size3D, from: UnitLength) -> Size3D`

Converts a size, given in the specified unit, to a size in points suitable for
use in the environment this converter is associated with.

`func convert(CGFloat, from: UnitLength) -> CGFloat`

Converts a length in the specified unit to a length in points suitable for use
in the environment this converter is associated with.

`func convert(Point3D, from: UnitLength) -> Point3D`

Converts a point, whose coordinates are in the specified unit, to a point
value suitable for use in the environment this converter is associated with.

`func convert(CGSize, from: UnitLength) -> CGSize`

Converts a size, given in the specified unit, to a size in points suitable for
use in the environment this converter is associated with.

`func convert<V>(V, from: UnitLength) -> V`

Converts a vector of physical length measurements, in the specified unit, to a
vector of values in points suitable for use in the environment this converter
is associated with.

`func convert(CGRect, from: UnitLength) -> CGRect`

Converts a rectangle, whose coordinates are in the specified unit, to a
rectangle with coordinates specified in points, suitable for use in the
environment this converter is associated with.

Instance Method

# convert(_:from:)

Converts a `Rect3D`, whose coordinates are in the specified unit, to a
`Rect3D` with coordinates specified in points, suitable for use in the
environment this converter is associated with.

visionOS 1.0+

    
    
    func convert(
        _ rect: Rect3D,
        from unit: UnitLength
    ) -> Rect3D

## Return Value

A value in points. Use this value only in the scene this converter was
associated with.

## See Also

### Converting from a unit length

`func convert(CGPoint, from: UnitLength) -> CGPoint`

Converts a point, whose coordinates are in the specified unit, to a point
suitable for use in the environment this converter is associated with.

`func convert(Size3D, from: UnitLength) -> Size3D`

Converts a size, given in the specified unit, to a size in points suitable for
use in the environment this converter is associated with.

`func convert(CGFloat, from: UnitLength) -> CGFloat`

Converts a length in the specified unit to a length in points suitable for use
in the environment this converter is associated with.

`func convert(Point3D, from: UnitLength) -> Point3D`

Converts a point, whose coordinates are in the specified unit, to a point
value suitable for use in the environment this converter is associated with.

`func convert(CGSize, from: UnitLength) -> CGSize`

Converts a size, given in the specified unit, to a size in points suitable for
use in the environment this converter is associated with.

`func convert<V>(V, from: UnitLength) -> V`

Converts a vector of physical length measurements, in the specified unit, to a
vector of values in points suitable for use in the environment this converter
is associated with.

`func convert(CGRect, from: UnitLength) -> CGRect`

Converts a rectangle, whose coordinates are in the specified unit, to a
rectangle with coordinates specified in points, suitable for use in the
environment this converter is associated with.

Instance Method

# convert(_:from:)

Converts a size, given in the specified unit, to a size in points suitable for
use in the environment this converter is associated with.

visionOS 1.0+

    
    
    func convert(
        _ size: Size3D,
        from unit: UnitLength
    ) -> Size3D

## Return Value

A value in points. Use this value only in the scene this converter was
associated with.

## See Also

### Converting from a unit length

`func convert(CGPoint, from: UnitLength) -> CGPoint`

Converts a point, whose coordinates are in the specified unit, to a point
suitable for use in the environment this converter is associated with.

`func convert(Rect3D, from: UnitLength) -> Rect3D`

Converts a `Rect3D`, whose coordinates are in the specified unit, to a
`Rect3D` with coordinates specified in points, suitable for use in the
environment this converter is associated with.

`func convert(CGFloat, from: UnitLength) -> CGFloat`

Converts a length in the specified unit to a length in points suitable for use
in the environment this converter is associated with.

`func convert(Point3D, from: UnitLength) -> Point3D`

Converts a point, whose coordinates are in the specified unit, to a point
value suitable for use in the environment this converter is associated with.

`func convert(CGSize, from: UnitLength) -> CGSize`

Converts a size, given in the specified unit, to a size in points suitable for
use in the environment this converter is associated with.

`func convert<V>(V, from: UnitLength) -> V`

Converts a vector of physical length measurements, in the specified unit, to a
vector of values in points suitable for use in the environment this converter
is associated with.

`func convert(CGRect, from: UnitLength) -> CGRect`

Converts a rectangle, whose coordinates are in the specified unit, to a
rectangle with coordinates specified in points, suitable for use in the
environment this converter is associated with.

Instance Method

# convert(_:from:)

Converts a length in the specified unit to a length in points suitable for use
in the environment this converter is associated with.

visionOS 1.0+

    
    
    func convert(
        _ lengthValue: CGFloat,
        from unit: UnitLength
    ) -> CGFloat

## Return Value

A value in points. Use this value only in the scene this converter was
associated with.

## See Also

### Converting from a unit length

`func convert(CGPoint, from: UnitLength) -> CGPoint`

Converts a point, whose coordinates are in the specified unit, to a point
suitable for use in the environment this converter is associated with.

`func convert(Rect3D, from: UnitLength) -> Rect3D`

Converts a `Rect3D`, whose coordinates are in the specified unit, to a
`Rect3D` with coordinates specified in points, suitable for use in the
environment this converter is associated with.

`func convert(Size3D, from: UnitLength) -> Size3D`

Converts a size, given in the specified unit, to a size in points suitable for
use in the environment this converter is associated with.

`func convert(Point3D, from: UnitLength) -> Point3D`

Converts a point, whose coordinates are in the specified unit, to a point
value suitable for use in the environment this converter is associated with.

`func convert(CGSize, from: UnitLength) -> CGSize`

Converts a size, given in the specified unit, to a size in points suitable for
use in the environment this converter is associated with.

`func convert<V>(V, from: UnitLength) -> V`

Converts a vector of physical length measurements, in the specified unit, to a
vector of values in points suitable for use in the environment this converter
is associated with.

`func convert(CGRect, from: UnitLength) -> CGRect`

Converts a rectangle, whose coordinates are in the specified unit, to a
rectangle with coordinates specified in points, suitable for use in the
environment this converter is associated with.

Instance Method

# convert(_:from:)

Converts a point, whose coordinates are in the specified unit, to a point
value suitable for use in the environment this converter is associated with.

visionOS 1.0+

    
    
    func convert(
        _ point: Point3D,
        from unit: UnitLength
    ) -> Point3D

## Return Value

A value in points. Use this value only in the scene this converter was
associated with.

## See Also

### Converting from a unit length

`func convert(CGPoint, from: UnitLength) -> CGPoint`

Converts a point, whose coordinates are in the specified unit, to a point
suitable for use in the environment this converter is associated with.

`func convert(Rect3D, from: UnitLength) -> Rect3D`

Converts a `Rect3D`, whose coordinates are in the specified unit, to a
`Rect3D` with coordinates specified in points, suitable for use in the
environment this converter is associated with.

`func convert(Size3D, from: UnitLength) -> Size3D`

Converts a size, given in the specified unit, to a size in points suitable for
use in the environment this converter is associated with.

`func convert(CGFloat, from: UnitLength) -> CGFloat`

Converts a length in the specified unit to a length in points suitable for use
in the environment this converter is associated with.

`func convert(CGSize, from: UnitLength) -> CGSize`

Converts a size, given in the specified unit, to a size in points suitable for
use in the environment this converter is associated with.

`func convert<V>(V, from: UnitLength) -> V`

Converts a vector of physical length measurements, in the specified unit, to a
vector of values in points suitable for use in the environment this converter
is associated with.

`func convert(CGRect, from: UnitLength) -> CGRect`

Converts a rectangle, whose coordinates are in the specified unit, to a
rectangle with coordinates specified in points, suitable for use in the
environment this converter is associated with.

Instance Method

# convert(_:from:)

Converts a size, given in the specified unit, to a size in points suitable for
use in the environment this converter is associated with.

visionOS 1.0+

    
    
    func convert(
        _ size: CGSize,
        from unit: UnitLength
    ) -> CGSize

## Return Value

A value in points. Use this value only in the scene this converter was
associated with.

## See Also

### Converting from a unit length

`func convert(CGPoint, from: UnitLength) -> CGPoint`

Converts a point, whose coordinates are in the specified unit, to a point
suitable for use in the environment this converter is associated with.

`func convert(Rect3D, from: UnitLength) -> Rect3D`

Converts a `Rect3D`, whose coordinates are in the specified unit, to a
`Rect3D` with coordinates specified in points, suitable for use in the
environment this converter is associated with.

`func convert(Size3D, from: UnitLength) -> Size3D`

Converts a size, given in the specified unit, to a size in points suitable for
use in the environment this converter is associated with.

`func convert(CGFloat, from: UnitLength) -> CGFloat`

Converts a length in the specified unit to a length in points suitable for use
in the environment this converter is associated with.

`func convert(Point3D, from: UnitLength) -> Point3D`

Converts a point, whose coordinates are in the specified unit, to a point
value suitable for use in the environment this converter is associated with.

`func convert<V>(V, from: UnitLength) -> V`

Converts a vector of physical length measurements, in the specified unit, to a
vector of values in points suitable for use in the environment this converter
is associated with.

`func convert(CGRect, from: UnitLength) -> CGRect`

Converts a rectangle, whose coordinates are in the specified unit, to a
rectangle with coordinates specified in points, suitable for use in the
environment this converter is associated with.

Instance Method

# convert(_:from:)

Converts a vector of physical length measurements, in the specified unit, to a
vector of values in points suitable for use in the environment this converter
is associated with.

visionOS 1.0+

    
    
    func convert<V>(
        _ lengthValues: V,
        from unit: UnitLength
    ) -> V where V : VectorArithmetic

## Return Value

A value in points. Use this value only in the scene this converter was
associated with.

## See Also

### Converting from a unit length

`func convert(CGPoint, from: UnitLength) -> CGPoint`

Converts a point, whose coordinates are in the specified unit, to a point
suitable for use in the environment this converter is associated with.

`func convert(Rect3D, from: UnitLength) -> Rect3D`

Converts a `Rect3D`, whose coordinates are in the specified unit, to a
`Rect3D` with coordinates specified in points, suitable for use in the
environment this converter is associated with.

`func convert(Size3D, from: UnitLength) -> Size3D`

Converts a size, given in the specified unit, to a size in points suitable for
use in the environment this converter is associated with.

`func convert(CGFloat, from: UnitLength) -> CGFloat`

Converts a length in the specified unit to a length in points suitable for use
in the environment this converter is associated with.

`func convert(Point3D, from: UnitLength) -> Point3D`

Converts a point, whose coordinates are in the specified unit, to a point
value suitable for use in the environment this converter is associated with.

`func convert(CGSize, from: UnitLength) -> CGSize`

Converts a size, given in the specified unit, to a size in points suitable for
use in the environment this converter is associated with.

`func convert(CGRect, from: UnitLength) -> CGRect`

Converts a rectangle, whose coordinates are in the specified unit, to a
rectangle with coordinates specified in points, suitable for use in the
environment this converter is associated with.

Instance Method

# convert(_:from:)

Converts a rectangle, whose coordinates are in the specified unit, to a
rectangle with coordinates specified in points, suitable for use in the
environment this converter is associated with.

visionOS 1.0+

    
    
    func convert(
        _ rect: CGRect,
        from unit: UnitLength
    ) -> CGRect

## Return Value

A value in points. Use this value only in the scene this converter was
associated with.

## See Also

### Converting from a unit length

`func convert(CGPoint, from: UnitLength) -> CGPoint`

Converts a point, whose coordinates are in the specified unit, to a point
suitable for use in the environment this converter is associated with.

`func convert(Rect3D, from: UnitLength) -> Rect3D`

Converts a `Rect3D`, whose coordinates are in the specified unit, to a
`Rect3D` with coordinates specified in points, suitable for use in the
environment this converter is associated with.

`func convert(Size3D, from: UnitLength) -> Size3D`

Converts a size, given in the specified unit, to a size in points suitable for
use in the environment this converter is associated with.

`func convert(CGFloat, from: UnitLength) -> CGFloat`

Converts a length in the specified unit to a length in points suitable for use
in the environment this converter is associated with.

`func convert(Point3D, from: UnitLength) -> Point3D`

Converts a point, whose coordinates are in the specified unit, to a point
value suitable for use in the environment this converter is associated with.

`func convert(CGSize, from: UnitLength) -> CGSize`

Converts a size, given in the specified unit, to a size in points suitable for
use in the environment this converter is associated with.

`func convert<V>(V, from: UnitLength) -> V`

Converts a vector of physical length measurements, in the specified unit, to a
vector of values in points suitable for use in the environment this converter
is associated with.

Instance Method

# convert(_:to:)

Converts a `Rect3D`’s coordinates to physical length measurements in the
specified unit.

visionOS 1.0+

    
    
    func convert(
        _ rect: Rect3D,
        to unit: UnitLength
    ) -> Rect3D

## Return Value

A `Rect3D` value with physical length measurements, in the given unit

## Discussion

The `Rect3D` is assumed to be in the coordinate system of the scene that this
converter is associated with. If the scene is scaled, the physical measurement
will take this scale into account.

## See Also

### Converting to a unit length

`func convert(CGRect, to: UnitLength) -> CGRect`

Converts a rectangle’s coordinates to physical length measurements in the
specified unit.

`func convert(CGPoint, to: UnitLength) -> CGPoint`

Converts a point’s coordinates to physical length measurements in the
specified unit.

`func convert<V>(V, to: UnitLength) -> V`

Converts a vector of values in points to corresponding physical length
measurements in the specified unit.

`func convert(Point3D, to: UnitLength) -> Point3D`

Converts a point’s coordinates to physical length measurements in the
specified unit.

`func convert(CGSize, to: UnitLength) -> CGSize`

Converts a size, specified in points, to physical length measurements in the
specified unit.

`func convert(Size3D, to: UnitLength) -> Size3D`

Converts a size, specified in points, to physical length measurements in the
specified unit.

`func convert(CGFloat, to: UnitLength) -> CGFloat`

Converts a length in points to a physical length measurement in the specified
unit.

Instance Method

# convert(_:to:)

Converts a rectangle’s coordinates to physical length measurements in the
specified unit.

visionOS 1.0+

    
    
    func convert(
        _ rect: CGRect,
        to unit: UnitLength
    ) -> CGRect

## Return Value

A rectangle with physical length measurements, in the given unit

## Discussion

The rectangle is assumed to be in the coordinate system of the scene that this
converter is associated with. If the scene is scaled, the physical measurement
will take this scale into account.

## See Also

### Converting to a unit length

`func convert(Rect3D, to: UnitLength) -> Rect3D`

Converts a `Rect3D`’s coordinates to physical length measurements in the
specified unit.

`func convert(CGPoint, to: UnitLength) -> CGPoint`

Converts a point’s coordinates to physical length measurements in the
specified unit.

`func convert<V>(V, to: UnitLength) -> V`

Converts a vector of values in points to corresponding physical length
measurements in the specified unit.

`func convert(Point3D, to: UnitLength) -> Point3D`

Converts a point’s coordinates to physical length measurements in the
specified unit.

`func convert(CGSize, to: UnitLength) -> CGSize`

Converts a size, specified in points, to physical length measurements in the
specified unit.

`func convert(Size3D, to: UnitLength) -> Size3D`

Converts a size, specified in points, to physical length measurements in the
specified unit.

`func convert(CGFloat, to: UnitLength) -> CGFloat`

Converts a length in points to a physical length measurement in the specified
unit.

Instance Method

# convert(_:to:)

Converts a point’s coordinates to physical length measurements in the
specified unit.

visionOS 1.0+

    
    
    func convert(
        _ point: CGPoint,
        to unit: UnitLength
    ) -> CGPoint

## Return Value

A point value with physical length measurements, in the given unit

## Discussion

The point is assumed to be in the coordinate system of the scene that this
converter is associated with. If the scene is scaled, the physical measurement
will take this scale into account.

## See Also

### Converting to a unit length

`func convert(Rect3D, to: UnitLength) -> Rect3D`

Converts a `Rect3D`’s coordinates to physical length measurements in the
specified unit.

`func convert(CGRect, to: UnitLength) -> CGRect`

Converts a rectangle’s coordinates to physical length measurements in the
specified unit.

`func convert<V>(V, to: UnitLength) -> V`

Converts a vector of values in points to corresponding physical length
measurements in the specified unit.

`func convert(Point3D, to: UnitLength) -> Point3D`

Converts a point’s coordinates to physical length measurements in the
specified unit.

`func convert(CGSize, to: UnitLength) -> CGSize`

Converts a size, specified in points, to physical length measurements in the
specified unit.

`func convert(Size3D, to: UnitLength) -> Size3D`

Converts a size, specified in points, to physical length measurements in the
specified unit.

`func convert(CGFloat, to: UnitLength) -> CGFloat`

Converts a length in points to a physical length measurement in the specified
unit.

Instance Method

# convert(_:to:)

Converts a vector of values in points to corresponding physical length
measurements in the specified unit.

visionOS 1.0+

    
    
    func convert<V>(
        _ pointValues: V,
        to unit: UnitLength
    ) -> V where V : VectorArithmetic

## Return Value

A vector of physical length measurements, each converted from the points value
in the input vector at the same position. converter was associated with.

## Discussion

The point values are assumed to be in the coordinate system of the scene that
this converter is associated with. If the scene was scaled by user action, the
physical measurement will take this scale into account.

## See Also

### Converting to a unit length

`func convert(Rect3D, to: UnitLength) -> Rect3D`

Converts a `Rect3D`’s coordinates to physical length measurements in the
specified unit.

`func convert(CGRect, to: UnitLength) -> CGRect`

Converts a rectangle’s coordinates to physical length measurements in the
specified unit.

`func convert(CGPoint, to: UnitLength) -> CGPoint`

Converts a point’s coordinates to physical length measurements in the
specified unit.

`func convert(Point3D, to: UnitLength) -> Point3D`

Converts a point’s coordinates to physical length measurements in the
specified unit.

`func convert(CGSize, to: UnitLength) -> CGSize`

Converts a size, specified in points, to physical length measurements in the
specified unit.

`func convert(Size3D, to: UnitLength) -> Size3D`

Converts a size, specified in points, to physical length measurements in the
specified unit.

`func convert(CGFloat, to: UnitLength) -> CGFloat`

Converts a length in points to a physical length measurement in the specified
unit.

Instance Method

# convert(_:to:)

Converts a point’s coordinates to physical length measurements in the
specified unit.

visionOS 1.0+

    
    
    func convert(
        _ point: Point3D,
        to unit: UnitLength
    ) -> Point3D

## Return Value

A point value with physical length measurements, in the given unit

## Discussion

The point is assumed to be in the coordinate system of the scene that this
converter is associated with. If the scene is scaled, the physical measurement
will take this scale into account.

## See Also

### Converting to a unit length

`func convert(Rect3D, to: UnitLength) -> Rect3D`

Converts a `Rect3D`’s coordinates to physical length measurements in the
specified unit.

`func convert(CGRect, to: UnitLength) -> CGRect`

Converts a rectangle’s coordinates to physical length measurements in the
specified unit.

`func convert(CGPoint, to: UnitLength) -> CGPoint`

Converts a point’s coordinates to physical length measurements in the
specified unit.

`func convert<V>(V, to: UnitLength) -> V`

Converts a vector of values in points to corresponding physical length
measurements in the specified unit.

`func convert(CGSize, to: UnitLength) -> CGSize`

Converts a size, specified in points, to physical length measurements in the
specified unit.

`func convert(Size3D, to: UnitLength) -> Size3D`

Converts a size, specified in points, to physical length measurements in the
specified unit.

`func convert(CGFloat, to: UnitLength) -> CGFloat`

Converts a length in points to a physical length measurement in the specified
unit.

Instance Method

# convert(_:to:)

Converts a size, specified in points, to physical length measurements in the
specified unit.

visionOS 1.0+

    
    
    func convert(
        _ size: CGSize,
        to unit: UnitLength
    ) -> CGSize

## Return Value

A size in the given unit

## Discussion

The size is assumed to be in the coordinate system of the scene that this
converter is associated with. If the scene is scaled, the physical measurement
will take this scale into account.

## See Also

### Converting to a unit length

`func convert(Rect3D, to: UnitLength) -> Rect3D`

Converts a `Rect3D`’s coordinates to physical length measurements in the
specified unit.

`func convert(CGRect, to: UnitLength) -> CGRect`

Converts a rectangle’s coordinates to physical length measurements in the
specified unit.

`func convert(CGPoint, to: UnitLength) -> CGPoint`

Converts a point’s coordinates to physical length measurements in the
specified unit.

`func convert<V>(V, to: UnitLength) -> V`

Converts a vector of values in points to corresponding physical length
measurements in the specified unit.

`func convert(Point3D, to: UnitLength) -> Point3D`

Converts a point’s coordinates to physical length measurements in the
specified unit.

`func convert(Size3D, to: UnitLength) -> Size3D`

Converts a size, specified in points, to physical length measurements in the
specified unit.

`func convert(CGFloat, to: UnitLength) -> CGFloat`

Converts a length in points to a physical length measurement in the specified
unit.

Instance Method

# convert(_:to:)

Converts a size, specified in points, to physical length measurements in the
specified unit.

visionOS 1.0+

    
    
    func convert(
        _ size: Size3D,
        to unit: UnitLength
    ) -> Size3D

## Return Value

A size in the given unit

## Discussion

The size is assumed to be in the coordinate system of the scene that this
converter is associated with. If the scene is scaled, the physical measurement
will take this scale into account.

## See Also

### Converting to a unit length

`func convert(Rect3D, to: UnitLength) -> Rect3D`

Converts a `Rect3D`’s coordinates to physical length measurements in the
specified unit.

`func convert(CGRect, to: UnitLength) -> CGRect`

Converts a rectangle’s coordinates to physical length measurements in the
specified unit.

`func convert(CGPoint, to: UnitLength) -> CGPoint`

Converts a point’s coordinates to physical length measurements in the
specified unit.

`func convert<V>(V, to: UnitLength) -> V`

Converts a vector of values in points to corresponding physical length
measurements in the specified unit.

`func convert(Point3D, to: UnitLength) -> Point3D`

Converts a point’s coordinates to physical length measurements in the
specified unit.

`func convert(CGSize, to: UnitLength) -> CGSize`

Converts a size, specified in points, to physical length measurements in the
specified unit.

`func convert(CGFloat, to: UnitLength) -> CGFloat`

Converts a length in points to a physical length measurement in the specified
unit.

Instance Method

# convert(_:to:)

Converts a length in points to a physical length measurement in the specified
unit.

visionOS 1.0+

    
    
    func convert(
        _ pointsValue: CGFloat,
        to unit: UnitLength
    ) -> CGFloat

## Return Value

A physical length in the given unit

## Discussion

The length is assumed to be in the coordinate system of the scene that this
converter is associated with. If the scene is scaled, the physical measurement
will take this scale into account.

## See Also

### Converting to a unit length

`func convert(Rect3D, to: UnitLength) -> Rect3D`

Converts a `Rect3D`’s coordinates to physical length measurements in the
specified unit.

`func convert(CGRect, to: UnitLength) -> CGRect`

Converts a rectangle’s coordinates to physical length measurements in the
specified unit.

`func convert(CGPoint, to: UnitLength) -> CGPoint`

Converts a point’s coordinates to physical length measurements in the
specified unit.

`func convert<V>(V, to: UnitLength) -> V`

Converts a vector of values in points to corresponding physical length
measurements in the specified unit.

`func convert(Point3D, to: UnitLength) -> Point3D`

Converts a point’s coordinates to physical length measurements in the
specified unit.

`func convert(CGSize, to: UnitLength) -> CGSize`

Converts a size, specified in points, to physical length measurements in the
specified unit.

`func convert(Size3D, to: UnitLength) -> Size3D`

Converts a size, specified in points, to physical length measurements in the
specified unit.



# PreviewContextKey

Type Property

# defaultValue

The default value of the key.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    static var defaultValue: Self.Value { get }

**Required**

## See Also

### Setting a default

`associatedtype Value`

The type of the value returned by the key.

**Required**

Associated Type

# Value

The type of the value returned by the key.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    associatedtype Value

**Required**

## See Also

### Setting a default

`static var defaultValue: Self.Value`

The default value of the key.

**Required**

Type Property

# defaultValue

The default value of the key.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    static var defaultValue: Self.Value { get }

**Required**

## See Also

### Setting a default

`associatedtype Value`

The type of the value returned by the key.

**Required**

Associated Type

# Value

The type of the value returned by the key.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    associatedtype Value

**Required**

## See Also

### Setting a default

`static var defaultValue: Self.Value`

The default value of the key.

**Required**



# PresentationDetent

Type Property

# large

The system detent for a sheet at full height.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static let large: PresentationDetent

## See Also

### Getting built-in detents

`static let medium: PresentationDetent`

The system detent for a sheet that’s approximately half the height of the
screen, and is inactive in compact height.

Type Property

# medium

The system detent for a sheet that’s approximately half the height of the
screen, and is inactive in compact height.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static let medium: PresentationDetent

## See Also

### Getting built-in detents

`static let large: PresentationDetent`

The system detent for a sheet at full height.

Type Method

# custom(_:)

A custom detent with a calculated height.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static func custom<D>(_ type: D.Type) -> PresentationDetent where D : CustomPresentationDetent

## See Also

### Creating custom detents

`static func fraction(CGFloat) -> PresentationDetent`

A custom detent with the specified fractional height.

`static func height(CGFloat) -> PresentationDetent`

A custom detent with the specified height.

`struct Context`

Information that you use to calculate the presentation’s height.

Type Method

# fraction(_:)

A custom detent with the specified fractional height.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static func fraction(_ fraction: CGFloat) -> PresentationDetent

## See Also

### Creating custom detents

`static func custom<D>(D.Type) -> PresentationDetent`

A custom detent with a calculated height.

`static func height(CGFloat) -> PresentationDetent`

A custom detent with the specified height.

`struct Context`

Information that you use to calculate the presentation’s height.

Type Method

# height(_:)

A custom detent with the specified height.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static func height(_ height: CGFloat) -> PresentationDetent

## See Also

### Creating custom detents

`static func custom<D>(D.Type) -> PresentationDetent`

A custom detent with a calculated height.

`static func fraction(CGFloat) -> PresentationDetent`

A custom detent with the specified fractional height.

`struct Context`

Information that you use to calculate the presentation’s height.

Structure

# PresentationDetent.Context

Information that you use to calculate the presentation’s height.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    @dynamicMemberLookup
    struct Context

## Topics

### Getting the height

`var maxDetentValue: CGFloat`

The height that the presentation appears in.

### Supporting types

`subscript<T>(dynamicMember _: KeyPath<EnvironmentValues, T>) -> T`

Returns the value specified by the keyPath from the environment.

## See Also

### Creating custom detents

`static func custom<D>(D.Type) -> PresentationDetent`

A custom detent with a calculated height.

`static func fraction(CGFloat) -> PresentationDetent`

A custom detent with the specified fractional height.

`static func height(CGFloat) -> PresentationDetent`

A custom detent with the specified height.



# PlainListStyle

Initializer

# init()

Creates a plain list style.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init()



# Path.Element

Case

# Path.Element.closeSubpath

A line from the start point of the current subpath (if any) to the current
point, which terminates the subpath.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case closeSubpath

## Discussion

After closing the subpath, the current point becomes undefined.

## See Also

### Getting path elements

`case curve(to: CGPoint, control1: CGPoint, control2: CGPoint)`

A cubic Bézier curve from the previous current point to the given end-point,
using the two control points to define the curve.

`case line(to: CGPoint)`

A line from the previous current point to the given point, which becomes the
new current point.

`case move(to: CGPoint)`

A path element that terminates the current subpath (without closing it) and
defines a new current point.

`case quadCurve(to: CGPoint, control: CGPoint)`

A quadratic Bézier curve from the previous current point to the given end-
point, using the single control point to define the curve.

Case

# Path.Element.curve(to:control1:control2:)

A cubic Bézier curve from the previous current point to the given end-point,
using the two control points to define the curve.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case curve(
        to: CGPoint,
        control1: CGPoint,
        control2: CGPoint
    )

## Discussion

The end-point of the curve becomes the new current point.

## See Also

### Getting path elements

`case closeSubpath`

A line from the start point of the current subpath (if any) to the current
point, which terminates the subpath.

`case line(to: CGPoint)`

A line from the previous current point to the given point, which becomes the
new current point.

`case move(to: CGPoint)`

A path element that terminates the current subpath (without closing it) and
defines a new current point.

`case quadCurve(to: CGPoint, control: CGPoint)`

A quadratic Bézier curve from the previous current point to the given end-
point, using the single control point to define the curve.

Case

# Path.Element.line(to:)

A line from the previous current point to the given point, which becomes the
new current point.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case line(to: CGPoint)

## See Also

### Getting path elements

`case closeSubpath`

A line from the start point of the current subpath (if any) to the current
point, which terminates the subpath.

`case curve(to: CGPoint, control1: CGPoint, control2: CGPoint)`

A cubic Bézier curve from the previous current point to the given end-point,
using the two control points to define the curve.

`case move(to: CGPoint)`

A path element that terminates the current subpath (without closing it) and
defines a new current point.

`case quadCurve(to: CGPoint, control: CGPoint)`

A quadratic Bézier curve from the previous current point to the given end-
point, using the single control point to define the curve.

Case

# Path.Element.move(to:)

A path element that terminates the current subpath (without closing it) and
defines a new current point.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case move(to: CGPoint)

## See Also

### Getting path elements

`case closeSubpath`

A line from the start point of the current subpath (if any) to the current
point, which terminates the subpath.

`case curve(to: CGPoint, control1: CGPoint, control2: CGPoint)`

A cubic Bézier curve from the previous current point to the given end-point,
using the two control points to define the curve.

`case line(to: CGPoint)`

A line from the previous current point to the given point, which becomes the
new current point.

`case quadCurve(to: CGPoint, control: CGPoint)`

A quadratic Bézier curve from the previous current point to the given end-
point, using the single control point to define the curve.

Case

# Path.Element.quadCurve(to:control:)

A quadratic Bézier curve from the previous current point to the given end-
point, using the single control point to define the curve.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case quadCurve(
        to: CGPoint,
        control: CGPoint
    )

## Discussion

The end-point of the curve becomes the new current point.

## See Also

### Getting path elements

`case closeSubpath`

A line from the start point of the current subpath (if any) to the current
point, which terminates the subpath.

`case curve(to: CGPoint, control1: CGPoint, control2: CGPoint)`

A cubic Bézier curve from the previous current point to the given end-point,
using the two control points to define the curve.

`case line(to: CGPoint)`

A line from the previous current point to the given point, which becomes the
new current point.

`case move(to: CGPoint)`

A path element that terminates the current subpath (without closing it) and
defines a new current point.



# Path

Initializer

# init()

Creates an empty path.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init()

## See Also

### Creating a path

`init((inout Path) -> ())`

Creates an empty path, then executes a closure to add its initial elements.

`init(CGMutablePath)`

Creates a path from a copy of a mutable shape path.

`init(CGPath)`

Creates a path from an immutable shape path.

`init?(String)`

Initializes from the result of a previous call to `Path.stringRepresentation`.
Fails if the `string` does not describe a valid path.

`init(CGRect)`

Creates a path containing a rectangle.

`init(ellipseIn: CGRect)`

Creates a path as an ellipse within the given rectangle.

`init(roundedRect: CGRect, cornerRadius: CGFloat, style: RoundedCornerStyle)`

Creates a path containing a rounded rectangle.

`init(roundedRect: CGRect, cornerSize: CGSize, style: RoundedCornerStyle)`

Creates a path containing a rounded rectangle.

`init(roundedRect: CGRect, cornerRadii: RectangleCornerRadii, style:
RoundedCornerStyle)`

Creates a path as the given rounded rectangle, which may have uneven corner
radii.

Initializer

# init(_:)

Creates an empty path, then executes a closure to add its initial elements.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(_ callback: (inout Path) -> ())

##  Parameters

`callback`

    

The Swift function that will be called to initialize the new path.

## See Also

### Creating a path

`init()`

Creates an empty path.

`init(CGMutablePath)`

Creates a path from a copy of a mutable shape path.

`init(CGPath)`

Creates a path from an immutable shape path.

`init?(String)`

Initializes from the result of a previous call to `Path.stringRepresentation`.
Fails if the `string` does not describe a valid path.

`init(CGRect)`

Creates a path containing a rectangle.

`init(ellipseIn: CGRect)`

Creates a path as an ellipse within the given rectangle.

`init(roundedRect: CGRect, cornerRadius: CGFloat, style: RoundedCornerStyle)`

Creates a path containing a rounded rectangle.

`init(roundedRect: CGRect, cornerSize: CGSize, style: RoundedCornerStyle)`

Creates a path containing a rounded rectangle.

`init(roundedRect: CGRect, cornerRadii: RectangleCornerRadii, style:
RoundedCornerStyle)`

Creates a path as the given rounded rectangle, which may have uneven corner
radii.

Initializer

# init(_:)

Creates a path from a copy of a mutable shape path.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(_ path: CGMutablePath)

##  Parameters

`path`

    

The CoreGraphics path to initialize the new path from.

## See Also

### Creating a path

`init()`

Creates an empty path.

`init((inout Path) -> ())`

Creates an empty path, then executes a closure to add its initial elements.

`init(CGPath)`

Creates a path from an immutable shape path.

`init?(String)`

Initializes from the result of a previous call to `Path.stringRepresentation`.
Fails if the `string` does not describe a valid path.

`init(CGRect)`

Creates a path containing a rectangle.

`init(ellipseIn: CGRect)`

Creates a path as an ellipse within the given rectangle.

`init(roundedRect: CGRect, cornerRadius: CGFloat, style: RoundedCornerStyle)`

Creates a path containing a rounded rectangle.

`init(roundedRect: CGRect, cornerSize: CGSize, style: RoundedCornerStyle)`

Creates a path containing a rounded rectangle.

`init(roundedRect: CGRect, cornerRadii: RectangleCornerRadii, style:
RoundedCornerStyle)`

Creates a path as the given rounded rectangle, which may have uneven corner
radii.

Initializer

# init(_:)

Creates a path from an immutable shape path.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(_ path: CGPath)

##  Parameters

`path`

    

The immutable CoreGraphics path to initialize the new path from.

## See Also

### Creating a path

`init()`

Creates an empty path.

`init((inout Path) -> ())`

Creates an empty path, then executes a closure to add its initial elements.

`init(CGMutablePath)`

Creates a path from a copy of a mutable shape path.

`init?(String)`

Initializes from the result of a previous call to `Path.stringRepresentation`.
Fails if the `string` does not describe a valid path.

`init(CGRect)`

Creates a path containing a rectangle.

`init(ellipseIn: CGRect)`

Creates a path as an ellipse within the given rectangle.

`init(roundedRect: CGRect, cornerRadius: CGFloat, style: RoundedCornerStyle)`

Creates a path containing a rounded rectangle.

`init(roundedRect: CGRect, cornerSize: CGSize, style: RoundedCornerStyle)`

Creates a path containing a rounded rectangle.

`init(roundedRect: CGRect, cornerRadii: RectangleCornerRadii, style:
RoundedCornerStyle)`

Creates a path as the given rounded rectangle, which may have uneven corner
radii.

Initializer

# init(_:)

Initializes from the result of a previous call to `Path.stringRepresentation`.
Fails if the `string` does not describe a valid path.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init?(_ string: String)

## See Also

### Creating a path

`init()`

Creates an empty path.

`init((inout Path) -> ())`

Creates an empty path, then executes a closure to add its initial elements.

`init(CGMutablePath)`

Creates a path from a copy of a mutable shape path.

`init(CGPath)`

Creates a path from an immutable shape path.

`init(CGRect)`

Creates a path containing a rectangle.

`init(ellipseIn: CGRect)`

Creates a path as an ellipse within the given rectangle.

`init(roundedRect: CGRect, cornerRadius: CGFloat, style: RoundedCornerStyle)`

Creates a path containing a rounded rectangle.

`init(roundedRect: CGRect, cornerSize: CGSize, style: RoundedCornerStyle)`

Creates a path containing a rounded rectangle.

`init(roundedRect: CGRect, cornerRadii: RectangleCornerRadii, style:
RoundedCornerStyle)`

Creates a path as the given rounded rectangle, which may have uneven corner
radii.

Initializer

# init(_:)

Creates a path containing a rectangle.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(_ rect: CGRect)

##  Parameters

`rect`

    

The rectangle to add.

## Discussion

This is a convenience function that creates a path of a rectangle. Using this
convenience function is more efficient than creating a path and adding a
rectangle to it.

Calling this function is equivalent to using `minX` and related properties to
find the corners of the rectangle, then using the `move(to:)`, `addLine(to:)`,
and `closeSubpath()` functions to add the rectangle.

## See Also

### Creating a path

`init()`

Creates an empty path.

`init((inout Path) -> ())`

Creates an empty path, then executes a closure to add its initial elements.

`init(CGMutablePath)`

Creates a path from a copy of a mutable shape path.

`init(CGPath)`

Creates a path from an immutable shape path.

`init?(String)`

Initializes from the result of a previous call to `Path.stringRepresentation`.
Fails if the `string` does not describe a valid path.

`init(ellipseIn: CGRect)`

Creates a path as an ellipse within the given rectangle.

`init(roundedRect: CGRect, cornerRadius: CGFloat, style: RoundedCornerStyle)`

Creates a path containing a rounded rectangle.

`init(roundedRect: CGRect, cornerSize: CGSize, style: RoundedCornerStyle)`

Creates a path containing a rounded rectangle.

`init(roundedRect: CGRect, cornerRadii: RectangleCornerRadii, style:
RoundedCornerStyle)`

Creates a path as the given rounded rectangle, which may have uneven corner
radii.

Initializer

# init(ellipseIn:)

Creates a path as an ellipse within the given rectangle.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(ellipseIn rect: CGRect)

##  Parameters

`rect`

    

The rectangle that bounds the ellipse.

## Discussion

This is a convenience function that creates a path of an ellipse. Using this
convenience function is more efficient than creating a path and adding an
ellipse to it.

The ellipse is approximated by a sequence of Bézier curves. Its center is the
midpoint of the rectangle defined by the rect parameter. If the rectangle is
square, then the ellipse is circular with a radius equal to one-half the width
(or height) of the rectangle. If the rect parameter specifies a rectangular
shape, then the major and minor axes of the ellipse are defined by the width
and height of the rectangle.

The ellipse forms a complete subpath of the path—that is, the ellipse drawing
starts with a move-to operation and ends with a close-subpath operation, with
all moves oriented in the clockwise direction. If you supply an affine
transform, then the constructed Bézier curves that define the ellipse are
transformed before they are added to the path.

## See Also

### Creating a path

`init()`

Creates an empty path.

`init((inout Path) -> ())`

Creates an empty path, then executes a closure to add its initial elements.

`init(CGMutablePath)`

Creates a path from a copy of a mutable shape path.

`init(CGPath)`

Creates a path from an immutable shape path.

`init?(String)`

Initializes from the result of a previous call to `Path.stringRepresentation`.
Fails if the `string` does not describe a valid path.

`init(CGRect)`

Creates a path containing a rectangle.

`init(roundedRect: CGRect, cornerRadius: CGFloat, style: RoundedCornerStyle)`

Creates a path containing a rounded rectangle.

`init(roundedRect: CGRect, cornerSize: CGSize, style: RoundedCornerStyle)`

Creates a path containing a rounded rectangle.

`init(roundedRect: CGRect, cornerRadii: RectangleCornerRadii, style:
RoundedCornerStyle)`

Creates a path as the given rounded rectangle, which may have uneven corner
radii.

Initializer

# init(roundedRect:cornerRadius:style:)

Creates a path containing a rounded rectangle.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        roundedRect rect: CGRect,
        cornerRadius: CGFloat,
        style: RoundedCornerStyle = .continuous
    )

##  Parameters

`rect`

    

A rectangle, specified in user space coordinates.

`cornerRadius`

    

The radius of all corners of the rectangle, specified in user space
coordinates.

`style`

    

The corner style. Defaults to the `continous` style if not specified.

## Discussion

This is a convenience function that creates a path of a rounded rectangle.
Using this convenience function is more efficient than creating a path and
adding a rounded rectangle to it.

## See Also

### Creating a path

`init()`

Creates an empty path.

`init((inout Path) -> ())`

Creates an empty path, then executes a closure to add its initial elements.

`init(CGMutablePath)`

Creates a path from a copy of a mutable shape path.

`init(CGPath)`

Creates a path from an immutable shape path.

`init?(String)`

Initializes from the result of a previous call to `Path.stringRepresentation`.
Fails if the `string` does not describe a valid path.

`init(CGRect)`

Creates a path containing a rectangle.

`init(ellipseIn: CGRect)`

Creates a path as an ellipse within the given rectangle.

`init(roundedRect: CGRect, cornerSize: CGSize, style: RoundedCornerStyle)`

Creates a path containing a rounded rectangle.

`init(roundedRect: CGRect, cornerRadii: RectangleCornerRadii, style:
RoundedCornerStyle)`

Creates a path as the given rounded rectangle, which may have uneven corner
radii.

Initializer

# init(roundedRect:cornerSize:style:)

Creates a path containing a rounded rectangle.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        roundedRect rect: CGRect,
        cornerSize: CGSize,
        style: RoundedCornerStyle = .continuous
    )

##  Parameters

`rect`

    

A rectangle, specified in user space coordinates.

`cornerSize`

    

The size of the corners, specified in user space coordinates.

`style`

    

The corner style. Defaults to the `continous` style if not specified.

## Discussion

This is a convenience function that creates a path of a rounded rectangle.
Using this convenience function is more efficient than creating a path and
adding a rounded rectangle to it.

## See Also

### Creating a path

`init()`

Creates an empty path.

`init((inout Path) -> ())`

Creates an empty path, then executes a closure to add its initial elements.

`init(CGMutablePath)`

Creates a path from a copy of a mutable shape path.

`init(CGPath)`

Creates a path from an immutable shape path.

`init?(String)`

Initializes from the result of a previous call to `Path.stringRepresentation`.
Fails if the `string` does not describe a valid path.

`init(CGRect)`

Creates a path containing a rectangle.

`init(ellipseIn: CGRect)`

Creates a path as an ellipse within the given rectangle.

`init(roundedRect: CGRect, cornerRadius: CGFloat, style: RoundedCornerStyle)`

Creates a path containing a rounded rectangle.

`init(roundedRect: CGRect, cornerRadii: RectangleCornerRadii, style:
RoundedCornerStyle)`

Creates a path as the given rounded rectangle, which may have uneven corner
radii.

Initializer

# init(roundedRect:cornerRadii:style:)

Creates a path as the given rounded rectangle, which may have uneven corner
radii.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init(
        roundedRect rect: CGRect,
        cornerRadii: RectangleCornerRadii,
        style: RoundedCornerStyle = .continuous
    )

##  Parameters

`rect`

    

A rectangle, specified in user space coordinates.

`cornerRadii`

    

The radius of each corner of the rectangle, specified in user space
coordinates.

`style`

    

The corner style. Defaults to the `continous` style if not specified.

## Discussion

This is a convenience function that creates a path of a rounded rectangle.
Using this function is more efficient than creating a path and adding a
rounded rectangle to it.

## See Also

### Creating a path

`init()`

Creates an empty path.

`init((inout Path) -> ())`

Creates an empty path, then executes a closure to add its initial elements.

`init(CGMutablePath)`

Creates a path from a copy of a mutable shape path.

`init(CGPath)`

Creates a path from an immutable shape path.

`init?(String)`

Initializes from the result of a previous call to `Path.stringRepresentation`.
Fails if the `string` does not describe a valid path.

`init(CGRect)`

Creates a path containing a rectangle.

`init(ellipseIn: CGRect)`

Creates a path as an ellipse within the given rectangle.

`init(roundedRect: CGRect, cornerRadius: CGFloat, style: RoundedCornerStyle)`

Creates a path containing a rounded rectangle.

`init(roundedRect: CGRect, cornerSize: CGSize, style: RoundedCornerStyle)`

Creates a path containing a rounded rectangle.

Instance Property

# boundingRect

A rectangle containing all path segments.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var boundingRect: CGRect { get }

## Discussion

This is the smallest rectangle completely enclosing all points in the path but
not including control points for Bézier curves.

## See Also

### Getting the path’s characteristics

`var cgPath: CGPath`

An immutable path representing the elements in the path.

`func contains(CGPoint, eoFill: Bool) -> Bool`

Returns true if the path contains a specified point.

`var currentPoint: CGPoint?`

Returns the last point in the path, or nil if the path contains no points.

`var description: String`

A description of the path that may be used to recreate the path via
`init?(_:)`.

`var isEmpty: Bool`

A Boolean value indicating whether the path contains zero elements.

Instance Property

# cgPath

An immutable path representing the elements in the path.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var cgPath: CGPath { get }

## See Also

### Getting the path’s characteristics

`var boundingRect: CGRect`

A rectangle containing all path segments.

`func contains(CGPoint, eoFill: Bool) -> Bool`

Returns true if the path contains a specified point.

`var currentPoint: CGPoint?`

Returns the last point in the path, or nil if the path contains no points.

`var description: String`

A description of the path that may be used to recreate the path via
`init?(_:)`.

`var isEmpty: Bool`

A Boolean value indicating whether the path contains zero elements.

Instance Method

# contains(_:eoFill:)

Returns true if the path contains a specified point.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func contains(
        _ p: CGPoint,
        eoFill: Bool = false
    ) -> Bool

## Discussion

If `eoFill` is true, this method uses the even-odd rule to define which points
are inside the path. Otherwise, it uses the non-zero rule.

## See Also

### Getting the path’s characteristics

`var boundingRect: CGRect`

A rectangle containing all path segments.

`var cgPath: CGPath`

An immutable path representing the elements in the path.

`var currentPoint: CGPoint?`

Returns the last point in the path, or nil if the path contains no points.

`var description: String`

A description of the path that may be used to recreate the path via
`init?(_:)`.

`var isEmpty: Bool`

A Boolean value indicating whether the path contains zero elements.

Instance Property

# currentPoint

Returns the last point in the path, or nil if the path contains no points.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var currentPoint: CGPoint? { get }

## See Also

### Getting the path’s characteristics

`var boundingRect: CGRect`

A rectangle containing all path segments.

`var cgPath: CGPath`

An immutable path representing the elements in the path.

`func contains(CGPoint, eoFill: Bool) -> Bool`

Returns true if the path contains a specified point.

`var description: String`

A description of the path that may be used to recreate the path via
`init?(_:)`.

`var isEmpty: Bool`

A Boolean value indicating whether the path contains zero elements.

Instance Property

# description

A description of the path that may be used to recreate the path via
`init?(_:)`.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var description: String { get }

## See Also

### Getting the path’s characteristics

`var boundingRect: CGRect`

A rectangle containing all path segments.

`var cgPath: CGPath`

An immutable path representing the elements in the path.

`func contains(CGPoint, eoFill: Bool) -> Bool`

Returns true if the path contains a specified point.

`var currentPoint: CGPoint?`

Returns the last point in the path, or nil if the path contains no points.

`var isEmpty: Bool`

A Boolean value indicating whether the path contains zero elements.

Instance Property

# isEmpty

A Boolean value indicating whether the path contains zero elements.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var isEmpty: Bool { get }

## See Also

### Getting the path’s characteristics

`var boundingRect: CGRect`

A rectangle containing all path segments.

`var cgPath: CGPath`

An immutable path representing the elements in the path.

`func contains(CGPoint, eoFill: Bool) -> Bool`

Returns true if the path contains a specified point.

`var currentPoint: CGPoint?`

Returns the last point in the path, or nil if the path contains no points.

`var description: String`

A description of the path that may be used to recreate the path via
`init?(_:)`.

Instance Method

# move(to:)

Begins a new subpath at the specified point.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    mutating func move(to end: CGPoint)

##  Parameters

`end`

    

The point, in user space coordinates, at which to start a new subpath.

## Discussion

The specified point becomes the start point of a new subpath. The current
point is set to this start point.

## See Also

### Drawing a path

`func addArc(center: CGPoint, radius: CGFloat, startAngle: Angle, endAngle:
Angle, clockwise: Bool, transform: CGAffineTransform)`

Adds an arc of a circle to the path, specified with a radius and angles.

`func addArc(tangent1End: CGPoint, tangent2End: CGPoint, radius: CGFloat,
transform: CGAffineTransform)`

Adds an arc of a circle to the path, specified with a radius and two tangent
lines.

`func addCurve(to: CGPoint, control1: CGPoint, control2: CGPoint)`

Adds a cubic Bézier curve to the path, with the specified end point and
control points.

`func addEllipse(in: CGRect, transform: CGAffineTransform)`

Adds an ellipse that fits inside the specified rectangle to the path.

`func addLine(to: CGPoint)`

Appends a straight line segment from the current point to the specified point.

`func addLines([CGPoint])`

Adds a sequence of connected straight-line segments to the path.

`func addPath(Path, transform: CGAffineTransform)`

Appends another path value to this path.

`func addQuadCurve(to: CGPoint, control: CGPoint)`

Adds a quadratic Bézier curve to the path, with the specified end point and
control point.

`func addRect(CGRect, transform: CGAffineTransform)`

Adds a rectangular subpath to the path.

`func addRects([CGRect], transform: CGAffineTransform)`

Adds a set of rectangular subpaths to the path.

`func addRelativeArc(center: CGPoint, radius: CGFloat, startAngle: Angle,
delta: Angle, transform: CGAffineTransform)`

Adds an arc of a circle to the path, specified with a radius and a difference
in angle.

`func addRoundedRect(in: CGRect, cornerSize: CGSize, style:
RoundedCornerStyle, transform: CGAffineTransform)`

Adds a rounded rectangle to the path.

`func closeSubpath()`

Closes and completes the current subpath.

Instance Method

# addArc(center:radius:startAngle:endAngle:clockwise:transform:)

Adds an arc of a circle to the path, specified with a radius and angles.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    mutating func addArc(
        center: CGPoint,
        radius: CGFloat,
        startAngle: Angle,
        endAngle: Angle,
        clockwise: Bool,
        transform: CGAffineTransform = .identity
    )

##  Parameters

`center`

    

The center of the arc, in user space coordinates.

`radius`

    

The radius of the arc, in user space coordinates.

`startAngle`

    

The angle to the starting point of the arc, measured from the positive x-axis.

`endAngle`

    

The angle to the end point of the arc, measured from the positive x-axis.

`clockwise`

    

true to make a clockwise arc; false to make a counterclockwise arc.

`transform`

    

An affine transform to apply to the arc before adding to the path. Defaults to
the identity transform if not specified.

## Discussion

This method calculates starting and ending points using the radius and angles
you specify, uses a sequence of cubic Bézier curves to approximate a segment
of a circle between those points, and then appends those curves to the path.

The `clockwise` parameter determines the direction in which the arc is
created; the actual direction of the final path is dependent on the
`transform` parameter and the current transform of a context where the path is
drawn. However, because SwiftUI by default uses a vertically-flipped
coordinate system (with the origin in the top-left of the view), specifying a
clockwise arc results in a counterclockwise arc after the transformation is
applied.

If the path ends with an unclosed subpath, this method adds a line connecting
the current point to the starting point of the arc. If there is no unclosed
subpath, this method creates a new subpath whose starting point is the
starting point of the arc. The ending point of the arc becomes the new current
point of the path.

## See Also

### Drawing a path

`func move(to: CGPoint)`

Begins a new subpath at the specified point.

`func addArc(tangent1End: CGPoint, tangent2End: CGPoint, radius: CGFloat,
transform: CGAffineTransform)`

Adds an arc of a circle to the path, specified with a radius and two tangent
lines.

`func addCurve(to: CGPoint, control1: CGPoint, control2: CGPoint)`

Adds a cubic Bézier curve to the path, with the specified end point and
control points.

`func addEllipse(in: CGRect, transform: CGAffineTransform)`

Adds an ellipse that fits inside the specified rectangle to the path.

`func addLine(to: CGPoint)`

Appends a straight line segment from the current point to the specified point.

`func addLines([CGPoint])`

Adds a sequence of connected straight-line segments to the path.

`func addPath(Path, transform: CGAffineTransform)`

Appends another path value to this path.

`func addQuadCurve(to: CGPoint, control: CGPoint)`

Adds a quadratic Bézier curve to the path, with the specified end point and
control point.

`func addRect(CGRect, transform: CGAffineTransform)`

Adds a rectangular subpath to the path.

`func addRects([CGRect], transform: CGAffineTransform)`

Adds a set of rectangular subpaths to the path.

`func addRelativeArc(center: CGPoint, radius: CGFloat, startAngle: Angle,
delta: Angle, transform: CGAffineTransform)`

Adds an arc of a circle to the path, specified with a radius and a difference
in angle.

`func addRoundedRect(in: CGRect, cornerSize: CGSize, style:
RoundedCornerStyle, transform: CGAffineTransform)`

Adds a rounded rectangle to the path.

`func closeSubpath()`

Closes and completes the current subpath.

Instance Method

# addArc(tangent1End:tangent2End:radius:transform:)

Adds an arc of a circle to the path, specified with a radius and two tangent
lines.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    mutating func addArc(
        tangent1End: CGPoint,
        tangent2End: CGPoint,
        radius: CGFloat,
        transform: CGAffineTransform = .identity
    )

##  Parameters

`tangent1End`

    

The end point, in user space coordinates, for the first tangent line to be
used in constructing the arc. (The start point for this tangent line is the
path’s current point.)

`tangent2End`

    

The end point, in user space coordinates, for the second tangent line to be
used in constructing the arc. (The start point for this tangent line is the
tangent1End point.)

`radius`

    

The radius of the arc, in user space coordinates.

`transform`

    

An affine transform to apply to the arc before adding to the path. Defaults to
the identity transform if not specified.

## Discussion

This method calculates two tangent lines—the first from the current point to
the tangent1End point, and the second from the `tangent1End` point to the
`tangent2End` point—then calculates the start and end points for a circular
arc of the specified radius such that the arc is tangent to both lines.
Finally, this method approximates that arc with a sequence of cubic Bézier
curves and appends those curves to the path.

If the starting point of the arc (that is, the point where a circle of the
specified radius must meet the first tangent line in order to also be tangent
to the second line) is not the current point, this method appends a straight
line segment from the current point to the starting point of the arc.

The ending point of the arc (that is, the point where a circle of the
specified radius must meet the second tangent line in order to also be tangent
to the first line) becomes the new current point of the path.

## See Also

### Drawing a path

`func move(to: CGPoint)`

Begins a new subpath at the specified point.

`func addArc(center: CGPoint, radius: CGFloat, startAngle: Angle, endAngle:
Angle, clockwise: Bool, transform: CGAffineTransform)`

Adds an arc of a circle to the path, specified with a radius and angles.

`func addCurve(to: CGPoint, control1: CGPoint, control2: CGPoint)`

Adds a cubic Bézier curve to the path, with the specified end point and
control points.

`func addEllipse(in: CGRect, transform: CGAffineTransform)`

Adds an ellipse that fits inside the specified rectangle to the path.

`func addLine(to: CGPoint)`

Appends a straight line segment from the current point to the specified point.

`func addLines([CGPoint])`

Adds a sequence of connected straight-line segments to the path.

`func addPath(Path, transform: CGAffineTransform)`

Appends another path value to this path.

`func addQuadCurve(to: CGPoint, control: CGPoint)`

Adds a quadratic Bézier curve to the path, with the specified end point and
control point.

`func addRect(CGRect, transform: CGAffineTransform)`

Adds a rectangular subpath to the path.

`func addRects([CGRect], transform: CGAffineTransform)`

Adds a set of rectangular subpaths to the path.

`func addRelativeArc(center: CGPoint, radius: CGFloat, startAngle: Angle,
delta: Angle, transform: CGAffineTransform)`

Adds an arc of a circle to the path, specified with a radius and a difference
in angle.

`func addRoundedRect(in: CGRect, cornerSize: CGSize, style:
RoundedCornerStyle, transform: CGAffineTransform)`

Adds a rounded rectangle to the path.

`func closeSubpath()`

Closes and completes the current subpath.

Instance Method

# addCurve(to:control1:control2:)

Adds a cubic Bézier curve to the path, with the specified end point and
control points.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    mutating func addCurve(
        to end: CGPoint,
        control1: CGPoint,
        control2: CGPoint
    )

##  Parameters

`control1`

    

The first control point of the curve, in user space coordinates.

`control2`

    

The second control point of the curve, in user space coordinates.

## Discussion

This method constructs a curve starting from the path’s current point and
ending at the specified end point, with curvature defined by the two control
points. After this method appends that curve to the current path, the end
point of the curve becomes the path’s current point.

## See Also

### Drawing a path

`func move(to: CGPoint)`

Begins a new subpath at the specified point.

`func addArc(center: CGPoint, radius: CGFloat, startAngle: Angle, endAngle:
Angle, clockwise: Bool, transform: CGAffineTransform)`

Adds an arc of a circle to the path, specified with a radius and angles.

`func addArc(tangent1End: CGPoint, tangent2End: CGPoint, radius: CGFloat,
transform: CGAffineTransform)`

Adds an arc of a circle to the path, specified with a radius and two tangent
lines.

`func addEllipse(in: CGRect, transform: CGAffineTransform)`

Adds an ellipse that fits inside the specified rectangle to the path.

`func addLine(to: CGPoint)`

Appends a straight line segment from the current point to the specified point.

`func addLines([CGPoint])`

Adds a sequence of connected straight-line segments to the path.

`func addPath(Path, transform: CGAffineTransform)`

Appends another path value to this path.

`func addQuadCurve(to: CGPoint, control: CGPoint)`

Adds a quadratic Bézier curve to the path, with the specified end point and
control point.

`func addRect(CGRect, transform: CGAffineTransform)`

Adds a rectangular subpath to the path.

`func addRects([CGRect], transform: CGAffineTransform)`

Adds a set of rectangular subpaths to the path.

`func addRelativeArc(center: CGPoint, radius: CGFloat, startAngle: Angle,
delta: Angle, transform: CGAffineTransform)`

Adds an arc of a circle to the path, specified with a radius and a difference
in angle.

`func addRoundedRect(in: CGRect, cornerSize: CGSize, style:
RoundedCornerStyle, transform: CGAffineTransform)`

Adds a rounded rectangle to the path.

`func closeSubpath()`

Closes and completes the current subpath.

Instance Method

# addEllipse(in:transform:)

Adds an ellipse that fits inside the specified rectangle to the path.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    mutating func addEllipse(
        in rect: CGRect,
        transform: CGAffineTransform = .identity
    )

## Discussion

The ellipse is approximated by a sequence of Bézier curves. Its center is the
midpoint of the rectangle defined by the `rect` parameter. If the rectangle is
square, then the ellipse is circular with a radius equal to one-half the width
(or height) of the rectangle. If the `rect` parameter specifies a rectangular
shape, then the major and minor axes of the ellipse are defined by the width
and height of the rectangle.

The ellipse forms a complete subpath of the path— that is, the ellipse drawing
starts with a move-to operation and ends with a close-subpath operation, with
all moves oriented in the clockwise direction.

  * Parameter:

    * rect: A rectangle that defines the area for the ellipse to fit in.

    * transform: An affine transform to apply to the ellipse before adding to the path. Defaults to the identity transform if not specified.

## See Also

### Drawing a path

`func move(to: CGPoint)`

Begins a new subpath at the specified point.

`func addArc(center: CGPoint, radius: CGFloat, startAngle: Angle, endAngle:
Angle, clockwise: Bool, transform: CGAffineTransform)`

Adds an arc of a circle to the path, specified with a radius and angles.

`func addArc(tangent1End: CGPoint, tangent2End: CGPoint, radius: CGFloat,
transform: CGAffineTransform)`

Adds an arc of a circle to the path, specified with a radius and two tangent
lines.

`func addCurve(to: CGPoint, control1: CGPoint, control2: CGPoint)`

Adds a cubic Bézier curve to the path, with the specified end point and
control points.

`func addLine(to: CGPoint)`

Appends a straight line segment from the current point to the specified point.

`func addLines([CGPoint])`

Adds a sequence of connected straight-line segments to the path.

`func addPath(Path, transform: CGAffineTransform)`

Appends another path value to this path.

`func addQuadCurve(to: CGPoint, control: CGPoint)`

Adds a quadratic Bézier curve to the path, with the specified end point and
control point.

`func addRect(CGRect, transform: CGAffineTransform)`

Adds a rectangular subpath to the path.

`func addRects([CGRect], transform: CGAffineTransform)`

Adds a set of rectangular subpaths to the path.

`func addRelativeArc(center: CGPoint, radius: CGFloat, startAngle: Angle,
delta: Angle, transform: CGAffineTransform)`

Adds an arc of a circle to the path, specified with a radius and a difference
in angle.

`func addRoundedRect(in: CGRect, cornerSize: CGSize, style:
RoundedCornerStyle, transform: CGAffineTransform)`

Adds a rounded rectangle to the path.

`func closeSubpath()`

Closes and completes the current subpath.

Instance Method

# addLine(to:)

Appends a straight line segment from the current point to the specified point.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    mutating func addLine(to end: CGPoint)

##  Parameters

`end`

    

The location, in user space coordinates, for the end of the new line segment.

## Discussion

After adding the line segment, the current point is set to the endpoint of the
line segment.

## See Also

### Drawing a path

`func move(to: CGPoint)`

Begins a new subpath at the specified point.

`func addArc(center: CGPoint, radius: CGFloat, startAngle: Angle, endAngle:
Angle, clockwise: Bool, transform: CGAffineTransform)`

Adds an arc of a circle to the path, specified with a radius and angles.

`func addArc(tangent1End: CGPoint, tangent2End: CGPoint, radius: CGFloat,
transform: CGAffineTransform)`

Adds an arc of a circle to the path, specified with a radius and two tangent
lines.

`func addCurve(to: CGPoint, control1: CGPoint, control2: CGPoint)`

Adds a cubic Bézier curve to the path, with the specified end point and
control points.

`func addEllipse(in: CGRect, transform: CGAffineTransform)`

Adds an ellipse that fits inside the specified rectangle to the path.

`func addLines([CGPoint])`

Adds a sequence of connected straight-line segments to the path.

`func addPath(Path, transform: CGAffineTransform)`

Appends another path value to this path.

`func addQuadCurve(to: CGPoint, control: CGPoint)`

Adds a quadratic Bézier curve to the path, with the specified end point and
control point.

`func addRect(CGRect, transform: CGAffineTransform)`

Adds a rectangular subpath to the path.

`func addRects([CGRect], transform: CGAffineTransform)`

Adds a set of rectangular subpaths to the path.

`func addRelativeArc(center: CGPoint, radius: CGFloat, startAngle: Angle,
delta: Angle, transform: CGAffineTransform)`

Adds an arc of a circle to the path, specified with a radius and a difference
in angle.

`func addRoundedRect(in: CGRect, cornerSize: CGSize, style:
RoundedCornerStyle, transform: CGAffineTransform)`

Adds a rounded rectangle to the path.

`func closeSubpath()`

Closes and completes the current subpath.

Instance Method

# addLines(_:)

Adds a sequence of connected straight-line segments to the path.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    mutating func addLines(_ lines: [CGPoint])

## Discussion

Calling this convenience method is equivalent to applying the transform to all
points in the array, then calling the `move(to:)` method with the first value
in the `points` array, then calling the `addLine(to:)` method for each
subsequent point until the array is exhausted. After calling this method, the
path’s current point is the last point in the array.

  * Parameter:

    * lines: An array of values that specify the start and end points of the line segments to draw. Each point in the array specifies a position in user space. The first point in the array specifies the initial starting point.

    * transform: An affine transform to apply to the points before adding to the path. Defaults to the identity transform if not specified.

## See Also

### Drawing a path

`func move(to: CGPoint)`

Begins a new subpath at the specified point.

`func addArc(center: CGPoint, radius: CGFloat, startAngle: Angle, endAngle:
Angle, clockwise: Bool, transform: CGAffineTransform)`

Adds an arc of a circle to the path, specified with a radius and angles.

`func addArc(tangent1End: CGPoint, tangent2End: CGPoint, radius: CGFloat,
transform: CGAffineTransform)`

Adds an arc of a circle to the path, specified with a radius and two tangent
lines.

`func addCurve(to: CGPoint, control1: CGPoint, control2: CGPoint)`

Adds a cubic Bézier curve to the path, with the specified end point and
control points.

`func addEllipse(in: CGRect, transform: CGAffineTransform)`

Adds an ellipse that fits inside the specified rectangle to the path.

`func addLine(to: CGPoint)`

Appends a straight line segment from the current point to the specified point.

`func addPath(Path, transform: CGAffineTransform)`

Appends another path value to this path.

`func addQuadCurve(to: CGPoint, control: CGPoint)`

Adds a quadratic Bézier curve to the path, with the specified end point and
control point.

`func addRect(CGRect, transform: CGAffineTransform)`

Adds a rectangular subpath to the path.

`func addRects([CGRect], transform: CGAffineTransform)`

Adds a set of rectangular subpaths to the path.

`func addRelativeArc(center: CGPoint, radius: CGFloat, startAngle: Angle,
delta: Angle, transform: CGAffineTransform)`

Adds an arc of a circle to the path, specified with a radius and a difference
in angle.

`func addRoundedRect(in: CGRect, cornerSize: CGSize, style:
RoundedCornerStyle, transform: CGAffineTransform)`

Adds a rounded rectangle to the path.

`func closeSubpath()`

Closes and completes the current subpath.

Instance Method

# addPath(_:transform:)

Appends another path value to this path.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    mutating func addPath(
        _ path: Path,
        transform: CGAffineTransform = .identity
    )

##  Parameters

`path`

    

The path to add.

`transform`

    

An affine transform to apply to the path parameter before adding to this path.
Defaults to the identity transform if not specified.

## Discussion

If the `path` parameter is a non-empty empty path, its elements are appended
in order to this path. Afterward, the start point and current point of this
path are those of the last subpath in the `path` parameter.

## See Also

### Drawing a path

`func move(to: CGPoint)`

Begins a new subpath at the specified point.

`func addArc(center: CGPoint, radius: CGFloat, startAngle: Angle, endAngle:
Angle, clockwise: Bool, transform: CGAffineTransform)`

Adds an arc of a circle to the path, specified with a radius and angles.

`func addArc(tangent1End: CGPoint, tangent2End: CGPoint, radius: CGFloat,
transform: CGAffineTransform)`

Adds an arc of a circle to the path, specified with a radius and two tangent
lines.

`func addCurve(to: CGPoint, control1: CGPoint, control2: CGPoint)`

Adds a cubic Bézier curve to the path, with the specified end point and
control points.

`func addEllipse(in: CGRect, transform: CGAffineTransform)`

Adds an ellipse that fits inside the specified rectangle to the path.

`func addLine(to: CGPoint)`

Appends a straight line segment from the current point to the specified point.

`func addLines([CGPoint])`

Adds a sequence of connected straight-line segments to the path.

`func addQuadCurve(to: CGPoint, control: CGPoint)`

Adds a quadratic Bézier curve to the path, with the specified end point and
control point.

`func addRect(CGRect, transform: CGAffineTransform)`

Adds a rectangular subpath to the path.

`func addRects([CGRect], transform: CGAffineTransform)`

Adds a set of rectangular subpaths to the path.

`func addRelativeArc(center: CGPoint, radius: CGFloat, startAngle: Angle,
delta: Angle, transform: CGAffineTransform)`

Adds an arc of a circle to the path, specified with a radius and a difference
in angle.

`func addRoundedRect(in: CGRect, cornerSize: CGSize, style:
RoundedCornerStyle, transform: CGAffineTransform)`

Adds a rounded rectangle to the path.

`func closeSubpath()`

Closes and completes the current subpath.

Instance Method

# addQuadCurve(to:control:)

Adds a quadratic Bézier curve to the path, with the specified end point and
control point.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    mutating func addQuadCurve(
        to end: CGPoint,
        control: CGPoint
    )

##  Parameters

`control`

    

The control point of the curve, in user space coordinates.

## Discussion

This method constructs a curve starting from the path’s current point and
ending at the specified end point, with curvature defined by the control
point. After this method appends that curve to the current path, the end point
of the curve becomes the path’s current point.

## See Also

### Drawing a path

`func move(to: CGPoint)`

Begins a new subpath at the specified point.

`func addArc(center: CGPoint, radius: CGFloat, startAngle: Angle, endAngle:
Angle, clockwise: Bool, transform: CGAffineTransform)`

Adds an arc of a circle to the path, specified with a radius and angles.

`func addArc(tangent1End: CGPoint, tangent2End: CGPoint, radius: CGFloat,
transform: CGAffineTransform)`

Adds an arc of a circle to the path, specified with a radius and two tangent
lines.

`func addCurve(to: CGPoint, control1: CGPoint, control2: CGPoint)`

Adds a cubic Bézier curve to the path, with the specified end point and
control points.

`func addEllipse(in: CGRect, transform: CGAffineTransform)`

Adds an ellipse that fits inside the specified rectangle to the path.

`func addLine(to: CGPoint)`

Appends a straight line segment from the current point to the specified point.

`func addLines([CGPoint])`

Adds a sequence of connected straight-line segments to the path.

`func addPath(Path, transform: CGAffineTransform)`

Appends another path value to this path.

`func addRect(CGRect, transform: CGAffineTransform)`

Adds a rectangular subpath to the path.

`func addRects([CGRect], transform: CGAffineTransform)`

Adds a set of rectangular subpaths to the path.

`func addRelativeArc(center: CGPoint, radius: CGFloat, startAngle: Angle,
delta: Angle, transform: CGAffineTransform)`

Adds an arc of a circle to the path, specified with a radius and a difference
in angle.

`func addRoundedRect(in: CGRect, cornerSize: CGSize, style:
RoundedCornerStyle, transform: CGAffineTransform)`

Adds a rounded rectangle to the path.

`func closeSubpath()`

Closes and completes the current subpath.

Instance Method

# addRect(_:transform:)

Adds a rectangular subpath to the path.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    mutating func addRect(
        _ rect: CGRect,
        transform: CGAffineTransform = .identity
    )

##  Parameters

`rect`

    

A rectangle, specified in user space coordinates.

`transform`

    

An affine transform to apply to the rectangle before adding to the path.
Defaults to the identity transform if not specified.

## Discussion

This is a convenience function that adds a rectangle to a path, starting by
moving to the bottom-left corner and then adding lines counter-clockwise to
create a rectangle, closing the subpath.

## See Also

### Drawing a path

`func move(to: CGPoint)`

Begins a new subpath at the specified point.

`func addArc(center: CGPoint, radius: CGFloat, startAngle: Angle, endAngle:
Angle, clockwise: Bool, transform: CGAffineTransform)`

Adds an arc of a circle to the path, specified with a radius and angles.

`func addArc(tangent1End: CGPoint, tangent2End: CGPoint, radius: CGFloat,
transform: CGAffineTransform)`

Adds an arc of a circle to the path, specified with a radius and two tangent
lines.

`func addCurve(to: CGPoint, control1: CGPoint, control2: CGPoint)`

Adds a cubic Bézier curve to the path, with the specified end point and
control points.

`func addEllipse(in: CGRect, transform: CGAffineTransform)`

Adds an ellipse that fits inside the specified rectangle to the path.

`func addLine(to: CGPoint)`

Appends a straight line segment from the current point to the specified point.

`func addLines([CGPoint])`

Adds a sequence of connected straight-line segments to the path.

`func addPath(Path, transform: CGAffineTransform)`

Appends another path value to this path.

`func addQuadCurve(to: CGPoint, control: CGPoint)`

Adds a quadratic Bézier curve to the path, with the specified end point and
control point.

`func addRects([CGRect], transform: CGAffineTransform)`

Adds a set of rectangular subpaths to the path.

`func addRelativeArc(center: CGPoint, radius: CGFloat, startAngle: Angle,
delta: Angle, transform: CGAffineTransform)`

Adds an arc of a circle to the path, specified with a radius and a difference
in angle.

`func addRoundedRect(in: CGRect, cornerSize: CGSize, style:
RoundedCornerStyle, transform: CGAffineTransform)`

Adds a rounded rectangle to the path.

`func closeSubpath()`

Closes and completes the current subpath.

Instance Method

# addRects(_:transform:)

Adds a set of rectangular subpaths to the path.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    mutating func addRects(
        _ rects: [CGRect],
        transform: CGAffineTransform = .identity
    )

## Discussion

Calling this convenience method is equivalent to repeatedly calling the
`addRect(_:transform:)` method for each rectangle in the array.

  * Parameter:

    * rects: An array of rectangles, specified in user space coordinates.

    * transform: An affine transform to apply to the ellipse before adding to the path. Defaults to the identity transform if not specified.

## See Also

### Drawing a path

`func move(to: CGPoint)`

Begins a new subpath at the specified point.

`func addArc(center: CGPoint, radius: CGFloat, startAngle: Angle, endAngle:
Angle, clockwise: Bool, transform: CGAffineTransform)`

Adds an arc of a circle to the path, specified with a radius and angles.

`func addArc(tangent1End: CGPoint, tangent2End: CGPoint, radius: CGFloat,
transform: CGAffineTransform)`

Adds an arc of a circle to the path, specified with a radius and two tangent
lines.

`func addCurve(to: CGPoint, control1: CGPoint, control2: CGPoint)`

Adds a cubic Bézier curve to the path, with the specified end point and
control points.

`func addEllipse(in: CGRect, transform: CGAffineTransform)`

Adds an ellipse that fits inside the specified rectangle to the path.

`func addLine(to: CGPoint)`

Appends a straight line segment from the current point to the specified point.

`func addLines([CGPoint])`

Adds a sequence of connected straight-line segments to the path.

`func addPath(Path, transform: CGAffineTransform)`

Appends another path value to this path.

`func addQuadCurve(to: CGPoint, control: CGPoint)`

Adds a quadratic Bézier curve to the path, with the specified end point and
control point.

`func addRect(CGRect, transform: CGAffineTransform)`

Adds a rectangular subpath to the path.

`func addRelativeArc(center: CGPoint, radius: CGFloat, startAngle: Angle,
delta: Angle, transform: CGAffineTransform)`

Adds an arc of a circle to the path, specified with a radius and a difference
in angle.

`func addRoundedRect(in: CGRect, cornerSize: CGSize, style:
RoundedCornerStyle, transform: CGAffineTransform)`

Adds a rounded rectangle to the path.

`func closeSubpath()`

Closes and completes the current subpath.

Instance Method

# addRelativeArc(center:radius:startAngle:delta:transform:)

Adds an arc of a circle to the path, specified with a radius and a difference
in angle.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    mutating func addRelativeArc(
        center: CGPoint,
        radius: CGFloat,
        startAngle: Angle,
        delta: Angle,
        transform: CGAffineTransform = .identity
    )

##  Parameters

`center`

    

The center of the arc, in user space coordinates.

`radius`

    

The radius of the arc, in user space coordinates.

`startAngle`

    

The angle to the starting point of the arc, measured from the positive x-axis.

`delta`

    

The difference between the starting angle and ending angle of the arc. A
positive value creates a counter- clockwise arc (in user space coordinates),
and vice versa.

`transform`

    

An affine transform to apply to the arc before adding to the path. Defaults to
the identity transform if not specified. /

## Discussion

This method calculates starting and ending points using the radius and angles
you specify, uses a sequence of cubic Bézier curves to approximate a segment
of a circle between those points, and then appends those curves to the path.

The `delta` parameter determines both the length of the arc the direction in
which the arc is created; the actual direction of the final path is dependent
on the `transform` parameter and the current transform of a context where the
path is drawn. However, because SwiftUI by default uses a vertically-flipped
coordinate system (with the origin in the top-left of the view), specifying a
clockwise arc results in a counterclockwise arc after the transformation is
applied.

If the path ends with an unclosed subpath, this method adds a line connecting
the current point to the starting point of the arc. If there is no unclosed
subpath, this method creates a new subpath whose starting point is the
starting point of the arc. The ending point of the arc becomes the new current
point of the path.

## See Also

### Drawing a path

`func move(to: CGPoint)`

Begins a new subpath at the specified point.

`func addArc(center: CGPoint, radius: CGFloat, startAngle: Angle, endAngle:
Angle, clockwise: Bool, transform: CGAffineTransform)`

Adds an arc of a circle to the path, specified with a radius and angles.

`func addArc(tangent1End: CGPoint, tangent2End: CGPoint, radius: CGFloat,
transform: CGAffineTransform)`

Adds an arc of a circle to the path, specified with a radius and two tangent
lines.

`func addCurve(to: CGPoint, control1: CGPoint, control2: CGPoint)`

Adds a cubic Bézier curve to the path, with the specified end point and
control points.

`func addEllipse(in: CGRect, transform: CGAffineTransform)`

Adds an ellipse that fits inside the specified rectangle to the path.

`func addLine(to: CGPoint)`

Appends a straight line segment from the current point to the specified point.

`func addLines([CGPoint])`

Adds a sequence of connected straight-line segments to the path.

`func addPath(Path, transform: CGAffineTransform)`

Appends another path value to this path.

`func addQuadCurve(to: CGPoint, control: CGPoint)`

Adds a quadratic Bézier curve to the path, with the specified end point and
control point.

`func addRect(CGRect, transform: CGAffineTransform)`

Adds a rectangular subpath to the path.

`func addRects([CGRect], transform: CGAffineTransform)`

Adds a set of rectangular subpaths to the path.

`func addRoundedRect(in: CGRect, cornerSize: CGSize, style:
RoundedCornerStyle, transform: CGAffineTransform)`

Adds a rounded rectangle to the path.

`func closeSubpath()`

Closes and completes the current subpath.

Instance Method

# addRoundedRect(in:cornerSize:style:transform:)

Adds a rounded rectangle to the path.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    mutating func addRoundedRect(
        in rect: CGRect,
        cornerSize: CGSize,
        style: RoundedCornerStyle = .continuous,
        transform: CGAffineTransform = .identity
    )

##  Parameters

`rect`

    

A rectangle, specified in user space coordinates.

`cornerSize`

    

The size of the corners, specified in user space coordinates.

`style`

    

The corner style. Defaults to the `continous` style if not specified.

`transform`

    

An affine transform to apply to the rectangle before adding to the path.
Defaults to the identity transform if not specified.

## Discussion

This is a convenience function that adds a rounded rectangle to a path,
starting by moving to the center of the right edge and then adding lines and
curves counter-clockwise to create a rounded rectangle, closing the subpath.

## See Also

### Drawing a path

`func move(to: CGPoint)`

Begins a new subpath at the specified point.

`func addArc(center: CGPoint, radius: CGFloat, startAngle: Angle, endAngle:
Angle, clockwise: Bool, transform: CGAffineTransform)`

Adds an arc of a circle to the path, specified with a radius and angles.

`func addArc(tangent1End: CGPoint, tangent2End: CGPoint, radius: CGFloat,
transform: CGAffineTransform)`

Adds an arc of a circle to the path, specified with a radius and two tangent
lines.

`func addCurve(to: CGPoint, control1: CGPoint, control2: CGPoint)`

Adds a cubic Bézier curve to the path, with the specified end point and
control points.

`func addEllipse(in: CGRect, transform: CGAffineTransform)`

Adds an ellipse that fits inside the specified rectangle to the path.

`func addLine(to: CGPoint)`

Appends a straight line segment from the current point to the specified point.

`func addLines([CGPoint])`

Adds a sequence of connected straight-line segments to the path.

`func addPath(Path, transform: CGAffineTransform)`

Appends another path value to this path.

`func addQuadCurve(to: CGPoint, control: CGPoint)`

Adds a quadratic Bézier curve to the path, with the specified end point and
control point.

`func addRect(CGRect, transform: CGAffineTransform)`

Adds a rectangular subpath to the path.

`func addRects([CGRect], transform: CGAffineTransform)`

Adds a set of rectangular subpaths to the path.

`func addRelativeArc(center: CGPoint, radius: CGFloat, startAngle: Angle,
delta: Angle, transform: CGAffineTransform)`

Adds an arc of a circle to the path, specified with a radius and a difference
in angle.

`func closeSubpath()`

Closes and completes the current subpath.

Instance Method

# closeSubpath()

Closes and completes the current subpath.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    mutating func closeSubpath()

## Discussion

Appends a line from the current point to the starting point of the current
subpath and ends the subpath.

After closing the subpath, your application can begin a new subpath without
first calling `move(to:)`. In this case, a new subpath is implicitly created
with a starting and current point equal to the previous subpath’s starting
point.

## See Also

### Drawing a path

`func move(to: CGPoint)`

Begins a new subpath at the specified point.

`func addArc(center: CGPoint, radius: CGFloat, startAngle: Angle, endAngle:
Angle, clockwise: Bool, transform: CGAffineTransform)`

Adds an arc of a circle to the path, specified with a radius and angles.

`func addArc(tangent1End: CGPoint, tangent2End: CGPoint, radius: CGFloat,
transform: CGAffineTransform)`

Adds an arc of a circle to the path, specified with a radius and two tangent
lines.

`func addCurve(to: CGPoint, control1: CGPoint, control2: CGPoint)`

Adds a cubic Bézier curve to the path, with the specified end point and
control points.

`func addEllipse(in: CGRect, transform: CGAffineTransform)`

Adds an ellipse that fits inside the specified rectangle to the path.

`func addLine(to: CGPoint)`

Appends a straight line segment from the current point to the specified point.

`func addLines([CGPoint])`

Adds a sequence of connected straight-line segments to the path.

`func addPath(Path, transform: CGAffineTransform)`

Appends another path value to this path.

`func addQuadCurve(to: CGPoint, control: CGPoint)`

Adds a quadratic Bézier curve to the path, with the specified end point and
control point.

`func addRect(CGRect, transform: CGAffineTransform)`

Adds a rectangular subpath to the path.

`func addRects([CGRect], transform: CGAffineTransform)`

Adds a set of rectangular subpaths to the path.

`func addRelativeArc(center: CGPoint, radius: CGFloat, startAngle: Angle,
delta: Angle, transform: CGAffineTransform)`

Adds an arc of a circle to the path, specified with a radius and a difference
in angle.

`func addRoundedRect(in: CGRect, cornerSize: CGSize, style:
RoundedCornerStyle, transform: CGAffineTransform)`

Adds a rounded rectangle to the path.

Instance Method

# applying(_:)

Returns a path constructed by applying the transform to all points of the
path.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func applying(_ transform: CGAffineTransform) -> Path

##  Parameters

`transform`

    

An affine transform to apply to the path.

## Return Value

a new copy of the path with the transform applied to all points.

## See Also

### Transforming the path

`func offsetBy(dx: CGFloat, dy: CGFloat) -> Path`

Returns a path constructed by translating all its points.

`func trimmedPath(from: CGFloat, to: CGFloat) -> Path`

Returns a partial copy of the path.

Instance Method

# offsetBy(dx:dy:)

Returns a path constructed by translating all its points.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func offsetBy(
        dx: CGFloat,
        dy: CGFloat
    ) -> Path

##  Parameters

`dx`

    

The offset to apply in the horizontal axis.

`dy`

    

The offset to apply in the vertical axis.

## Return Value

a new copy of the path with the offset applied to all points.

## See Also

### Transforming the path

`func applying(CGAffineTransform) -> Path`

Returns a path constructed by applying the transform to all points of the
path.

`func trimmedPath(from: CGFloat, to: CGFloat) -> Path`

Returns a partial copy of the path.

Instance Method

# trimmedPath(from:to:)

Returns a partial copy of the path.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func trimmedPath(
        from: CGFloat,
        to: CGFloat
    ) -> Path

## Discussion

The returned path contains the region between `from` and `to`, both of which
must be fractions between zero and one defining points linearly-interpolated
along the path.

## See Also

### Transforming the path

`func applying(CGAffineTransform) -> Path`

Returns a path constructed by applying the transform to all points of the
path.

`func offsetBy(dx: CGFloat, dy: CGFloat) -> Path`

Returns a path constructed by translating all its points.

Instance Method

# addRoundedRect(in:cornerSize:style:transform:)

Adds a rounded rectangle to the path.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    mutating func addRoundedRect(
        in rect: CGRect,
        cornerSize: CGSize,
        style: RoundedCornerStyle = .continuous,
        transform: CGAffineTransform = .identity
    )

##  Parameters

`rect`

    

A rectangle, specified in user space coordinates.

`cornerSize`

    

The size of the corners, specified in user space coordinates.

`style`

    

The corner style. Defaults to the `continous` style if not specified.

`transform`

    

An affine transform to apply to the rectangle before adding to the path.
Defaults to the identity transform if not specified.

## Discussion

This is a convenience function that adds a rounded rectangle to a path,
starting by moving to the center of the right edge and then adding lines and
curves counter-clockwise to create a rounded rectangle, closing the subpath.

## See Also

### Drawing a path

`func move(to: CGPoint)`

Begins a new subpath at the specified point.

`func addArc(center: CGPoint, radius: CGFloat, startAngle: Angle, endAngle:
Angle, clockwise: Bool, transform: CGAffineTransform)`

Adds an arc of a circle to the path, specified with a radius and angles.

`func addArc(tangent1End: CGPoint, tangent2End: CGPoint, radius: CGFloat,
transform: CGAffineTransform)`

Adds an arc of a circle to the path, specified with a radius and two tangent
lines.

`func addCurve(to: CGPoint, control1: CGPoint, control2: CGPoint)`

Adds a cubic Bézier curve to the path, with the specified end point and
control points.

`func addEllipse(in: CGRect, transform: CGAffineTransform)`

Adds an ellipse that fits inside the specified rectangle to the path.

`func addLine(to: CGPoint)`

Appends a straight line segment from the current point to the specified point.

`func addLines([CGPoint])`

Adds a sequence of connected straight-line segments to the path.

`func addPath(Path, transform: CGAffineTransform)`

Appends another path value to this path.

`func addQuadCurve(to: CGPoint, control: CGPoint)`

Adds a quadratic Bézier curve to the path, with the specified end point and
control point.

`func addRect(CGRect, transform: CGAffineTransform)`

Adds a rectangular subpath to the path.

`func addRects([CGRect], transform: CGAffineTransform)`

Adds a set of rectangular subpaths to the path.

`func addRelativeArc(center: CGPoint, radius: CGFloat, startAngle: Angle,
delta: Angle, transform: CGAffineTransform)`

Adds an arc of a circle to the path, specified with a radius and a difference
in angle.

`func closeSubpath()`

Closes and completes the current subpath.

Instance Method

# intersection(_:eoFill:)

Returns a new path with filled regions common to both paths.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func intersection(
        _ other: Path,
        eoFill: Bool = false
    ) -> Path

##  Parameters

`other`

    

The path to intersect.

`eoFill`

    

Whether to use the even-odd rule for determining which areas to treat as the
interior of the paths (if true), or the non-zero rule (if false).

## Return Value

A new path.

## Discussion

The filled region of the resulting path is the overlapping area of the filled
region of both paths. This can be used to clip the fill of a path to a mask.

Any unclosed subpaths in either path are assumed to be closed. The result of
filling this path using either even-odd or non-zero fill rules is identical.

## See Also

### Performing operations on the path

`func addRoundedRect(in: CGRect, cornerSize: CGSize, style:
RoundedCornerStyle, transform: CGAffineTransform)`

Adds a rounded rectangle to the path.

`func lineIntersection(Path, eoFill: Bool) -> Path`

Returns a new path with a line from this path that overlaps the filled regions
of the given path.

`func lineSubtraction(Path, eoFill: Bool) -> Path`

Returns a new path with a line from this path that does not overlap the filled
region of the given path.

`func normalized(eoFill: Bool) -> Path`

Returns a new weakly-simple copy of this path.

`func subtracting(Path, eoFill: Bool) -> Path`

Returns a new path with filled regions from this path that are not in the
given path.

`func symmetricDifference(Path, eoFill: Bool) -> Path`

Returns a new path with filled regions either from this path or the given
path, but not in both.

`func union(Path, eoFill: Bool) -> Path`

Returns a new path with filled regions in either this path or the given path.

Instance Method

# lineIntersection(_:eoFill:)

Returns a new path with a line from this path that overlaps the filled regions
of the given path.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func lineIntersection(
        _ other: Path,
        eoFill: Bool = false
    ) -> Path

##  Parameters

`other`

    

The path to intersect.

`eoFill`

    

Whether to use the even-odd rule for determining which areas to treat as the
interior of the paths (if true), or the non-zero rule (if false).

## Return Value

A new path.

## Discussion

The line of the resulting path is the line of this path that overlaps the
filled region of `other`.

Intersected subpaths that are clipped create open subpaths. Closed subpaths
that do not intersect `other` remain closed.

## See Also

### Performing operations on the path

`func addRoundedRect(in: CGRect, cornerSize: CGSize, style:
RoundedCornerStyle, transform: CGAffineTransform)`

Adds a rounded rectangle to the path.

`func intersection(Path, eoFill: Bool) -> Path`

Returns a new path with filled regions common to both paths.

`func lineSubtraction(Path, eoFill: Bool) -> Path`

Returns a new path with a line from this path that does not overlap the filled
region of the given path.

`func normalized(eoFill: Bool) -> Path`

Returns a new weakly-simple copy of this path.

`func subtracting(Path, eoFill: Bool) -> Path`

Returns a new path with filled regions from this path that are not in the
given path.

`func symmetricDifference(Path, eoFill: Bool) -> Path`

Returns a new path with filled regions either from this path or the given
path, but not in both.

`func union(Path, eoFill: Bool) -> Path`

Returns a new path with filled regions in either this path or the given path.

Instance Method

# lineSubtraction(_:eoFill:)

Returns a new path with a line from this path that does not overlap the filled
region of the given path.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func lineSubtraction(
        _ other: Path,
        eoFill: Bool = false
    ) -> Path

##  Parameters

`other`

    

The path to subtract.

`eoFill`

    

Whether to use the even-odd rule for determining which areas to treat as the
interior of the paths (if true), or the non-zero rule (if false).

## Return Value

A new path.

## Discussion

The line of the resulting path is the line of this path that does not overlap
the filled region of `other`.

Intersected subpaths that are clipped create open subpaths. Closed subpaths
that do not intersect `other` remain closed.

## See Also

### Performing operations on the path

`func addRoundedRect(in: CGRect, cornerSize: CGSize, style:
RoundedCornerStyle, transform: CGAffineTransform)`

Adds a rounded rectangle to the path.

`func intersection(Path, eoFill: Bool) -> Path`

Returns a new path with filled regions common to both paths.

`func lineIntersection(Path, eoFill: Bool) -> Path`

Returns a new path with a line from this path that overlaps the filled regions
of the given path.

`func normalized(eoFill: Bool) -> Path`

Returns a new weakly-simple copy of this path.

`func subtracting(Path, eoFill: Bool) -> Path`

Returns a new path with filled regions from this path that are not in the
given path.

`func symmetricDifference(Path, eoFill: Bool) -> Path`

Returns a new path with filled regions either from this path or the given
path, but not in both.

`func union(Path, eoFill: Bool) -> Path`

Returns a new path with filled regions in either this path or the given path.

Instance Method

# normalized(eoFill:)

Returns a new weakly-simple copy of this path.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func normalized(eoFill: Bool = true) -> Path

##  Parameters

`eoFill`

    

Whether to use the even-odd rule for determining which areas to treat as the
interior of the paths (if true), or the non-zero rule (if false).

## Return Value

A new path.

## Discussion

The returned path is a weakly-simple path, has no self-intersections, and has
a normalized orientation. The result of filling this path using either even-
odd or non-zero fill rules is identical.

## See Also

### Performing operations on the path

`func addRoundedRect(in: CGRect, cornerSize: CGSize, style:
RoundedCornerStyle, transform: CGAffineTransform)`

Adds a rounded rectangle to the path.

`func intersection(Path, eoFill: Bool) -> Path`

Returns a new path with filled regions common to both paths.

`func lineIntersection(Path, eoFill: Bool) -> Path`

Returns a new path with a line from this path that overlaps the filled regions
of the given path.

`func lineSubtraction(Path, eoFill: Bool) -> Path`

Returns a new path with a line from this path that does not overlap the filled
region of the given path.

`func subtracting(Path, eoFill: Bool) -> Path`

Returns a new path with filled regions from this path that are not in the
given path.

`func symmetricDifference(Path, eoFill: Bool) -> Path`

Returns a new path with filled regions either from this path or the given
path, but not in both.

`func union(Path, eoFill: Bool) -> Path`

Returns a new path with filled regions in either this path or the given path.

Instance Method

# subtracting(_:eoFill:)

Returns a new path with filled regions from this path that are not in the
given path.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func subtracting(
        _ other: Path,
        eoFill: Bool = false
    ) -> Path

##  Parameters

`other`

    

The path to subtract.

`eoFill`

    

Whether to use the even-odd rule for determining which areas to treat as the
interior of the paths (if true), or the non-zero rule (if false).

## Return Value

A new path.

## Discussion

The filled region of the resulting path is the filled region of this path with
the filled region `other` removed from it.

Any unclosed subpaths in either path are assumed to be closed. The result of
filling this path using either even-odd or non-zero fill rules is identical.

## See Also

### Performing operations on the path

`func addRoundedRect(in: CGRect, cornerSize: CGSize, style:
RoundedCornerStyle, transform: CGAffineTransform)`

Adds a rounded rectangle to the path.

`func intersection(Path, eoFill: Bool) -> Path`

Returns a new path with filled regions common to both paths.

`func lineIntersection(Path, eoFill: Bool) -> Path`

Returns a new path with a line from this path that overlaps the filled regions
of the given path.

`func lineSubtraction(Path, eoFill: Bool) -> Path`

Returns a new path with a line from this path that does not overlap the filled
region of the given path.

`func normalized(eoFill: Bool) -> Path`

Returns a new weakly-simple copy of this path.

`func symmetricDifference(Path, eoFill: Bool) -> Path`

Returns a new path with filled regions either from this path or the given
path, but not in both.

`func union(Path, eoFill: Bool) -> Path`

Returns a new path with filled regions in either this path or the given path.

Instance Method

# symmetricDifference(_:eoFill:)

Returns a new path with filled regions either from this path or the given
path, but not in both.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func symmetricDifference(
        _ other: Path,
        eoFill: Bool = false
    ) -> Path

##  Parameters

`other`

    

The path to difference.

`eoFill`

    

Whether to use the even-odd rule for determining which areas to treat as the
interior of the paths (if true), or the non-zero rule (if false).

## Return Value

A new path.

## Discussion

The filled region of the resulting path is the filled region contained in
either this path or `other`, but not both.

Any unclosed subpaths in either path are assumed to be closed. The result of
filling this path using either even-odd or non-zero fill rules is identical.

## See Also

### Performing operations on the path

`func addRoundedRect(in: CGRect, cornerSize: CGSize, style:
RoundedCornerStyle, transform: CGAffineTransform)`

Adds a rounded rectangle to the path.

`func intersection(Path, eoFill: Bool) -> Path`

Returns a new path with filled regions common to both paths.

`func lineIntersection(Path, eoFill: Bool) -> Path`

Returns a new path with a line from this path that overlaps the filled regions
of the given path.

`func lineSubtraction(Path, eoFill: Bool) -> Path`

Returns a new path with a line from this path that does not overlap the filled
region of the given path.

`func normalized(eoFill: Bool) -> Path`

Returns a new weakly-simple copy of this path.

`func subtracting(Path, eoFill: Bool) -> Path`

Returns a new path with filled regions from this path that are not in the
given path.

`func union(Path, eoFill: Bool) -> Path`

Returns a new path with filled regions in either this path or the given path.

Instance Method

# union(_:eoFill:)

Returns a new path with filled regions in either this path or the given path.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func union(
        _ other: Path,
        eoFill: Bool = false
    ) -> Path

##  Parameters

`other`

    

The path to union.

`eoFill`

    

Whether to use the even-odd rule for determining which areas to treat as the
interior of the paths (if true), or the non-zero rule (if false).

## Return Value

A new path.

## Discussion

The filled region of resulting path is the combination of the filled region of
both paths added together.

Any unclosed subpaths in either path are assumed to be closed. The result of
filling this path using either even-odd or non-zero fill rules is identical.

## See Also

### Performing operations on the path

`func addRoundedRect(in: CGRect, cornerSize: CGSize, style:
RoundedCornerStyle, transform: CGAffineTransform)`

Adds a rounded rectangle to the path.

`func intersection(Path, eoFill: Bool) -> Path`

Returns a new path with filled regions common to both paths.

`func lineIntersection(Path, eoFill: Bool) -> Path`

Returns a new path with a line from this path that overlaps the filled regions
of the given path.

`func lineSubtraction(Path, eoFill: Bool) -> Path`

Returns a new path with a line from this path that does not overlap the filled
region of the given path.

`func normalized(eoFill: Bool) -> Path`

Returns a new weakly-simple copy of this path.

`func subtracting(Path, eoFill: Bool) -> Path`

Returns a new path with filled regions from this path that are not in the
given path.

`func symmetricDifference(Path, eoFill: Bool) -> Path`

Returns a new path with filled regions either from this path or the given
path, but not in both.

Instance Method

# forEach(_:)

Calls `body` with each element in the path.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func forEach(_ body: (Path.Element) -> Void)

## See Also

### Operating over path elements

`enum Element`

An element of a path.

Enumeration

# Path.Element

An element of a path.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    enum Element

## Topics

### Getting path elements

`case closeSubpath`

A line from the start point of the current subpath (if any) to the current
point, which terminates the subpath.

`case curve(to: CGPoint, control1: CGPoint, control2: CGPoint)`

A cubic Bézier curve from the previous current point to the given end-point,
using the two control points to define the curve.

`case line(to: CGPoint)`

A line from the previous current point to the given point, which becomes the
new current point.

`case move(to: CGPoint)`

A path element that terminates the current subpath (without closing it) and
defines a new current point.

`case quadCurve(to: CGPoint, control: CGPoint)`

A quadratic Bézier curve from the previous current point to the given end-
point, using the single control point to define the curve.

## Relationships

### Conforms To

  * `Equatable`
  * `Sendable`

## See Also

### Operating over path elements

`func forEach((Path.Element) -> Void)`

Calls `body` with each element in the path.

Instance Method

# strokedPath(_:)

Returns a stroked copy of the path using `style` to define how the stroked
outline is created.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func strokedPath(_ style: StrokeStyle) -> Path

Instance Method

# addRoundedRect(in:cornerRadii:style:transform:)

Adds a rounded rectangle with uneven corners to the path.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    mutating func addRoundedRect(
        in rect: CGRect,
        cornerRadii: RectangleCornerRadii,
        style: RoundedCornerStyle = .continuous,
        transform: CGAffineTransform = .identity
    )

##  Parameters

`rect`

    

A rectangle, specified in user space coordinates.

`cornerRadii`

    

The radius of each corner of the rectangle, specified in user space
coordinates.

`style`

    

The corner style. Defaults to the `continous` style if not specified.

`transform`

    

An affine transform to apply to the rectangle before adding to the path.
Defaults to the identity transform if not specified.

## Discussion

This is a convenience function that adds a rounded rectangle to a path,
starting by moving to the center of the right edge and then adding lines and
curves counter-clockwise to create a rounded rectangle, closing the subpath.



# Prominence

Case

# Prominence.standard

The standard prominence.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    case standard

## See Also

### Getting prominence options

`case increased`

An increased prominence.

Case

# Prominence.increased

An increased prominence.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    case increased

## Discussion

Note

Not all views will react to increased prominence.

## See Also

### Getting prominence options

`case standard`

The standard prominence.



# PasteButton

Initializer

# init(supportedContentTypes:payloadAction:)

Creates a Paste button that accepts specific types of data from the
pasteboard.

iOS 16.0+  iPadOS 16.0+  macOS 11.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    @MainActor
    init(
        supportedContentTypes: [UTType],
        payloadAction: @escaping ([NSItemProvider]) -> Void
    )

##  Parameters

`supportedContentTypes`

    

The exact uniform type identifiers supported by the button. If the pasteboard
doesn’t contain any of the supported types, the button becomes disabled.

`payloadAction`

    

The handler to call when the user clicks the Paste button and the pasteboard
has items that conform to `supportedContentTypes`. This closure receives an
array of item providers that you use to inspect and load the pasteboard data.

## Discussion

Set the contents of `supportedContentTypes` in order of your app’s preference
for its supported types. The Paste button takes the most-preferred type that
the pasteboard source supports and delivers this to the `payloadAction`
closure.

## See Also

### Creating a paste button

`init<T>(payloadType: T.Type, onPaste: ([T]) -> Void)`

Creates an instance that accepts values of the specified type.

Initializer

# init(payloadType:onPaste:)

Creates an instance that accepts values of the specified type.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    @MainActor
    init<T>(
        payloadType: T.Type,
        onPaste: @escaping ([T]) -> Void
    ) where T : Transferable

##  Parameters

`type`

    

The type that you want to paste via the `PasteButton`.

`onPaste`

    

The handler to call on trigger of the button with at least one item of the
specified `Transferable` type from the pasteboard.

## See Also

### Creating a paste button

`init(supportedContentTypes: [UTType], payloadAction: ([NSItemProvider]) ->
Void)`

Creates a Paste button that accepts specific types of data from the
pasteboard.

Initializer

# init(supportedTypes:payloadAction:)

Creates a Paste button that accepts specific types of data from the
pasteboard.

macOS 10.15–14.4  Deprecated

    
    
    @MainActor
    init(
        supportedTypes: [String],
        payloadAction: @escaping ([NSItemProvider]) -> Void
    )

Deprecated

Use the `init(supportedContentTypes:payloadAction:)` initializer instead.

##  Parameters

`supportedTypes`

    

The exact uniform type identifiers supported by the button. If the pasteboard
doesn’t contain any of the supported types, the button becomes disabled.

`payloadAction`

    

The handler to call when the user clicks the Paste button, and the pasteboard
has items that conform to `supportedTypes`. This closure receives an array of
item providers that you use to inspect and load the pasteboard data.

## Discussion

Set the contents of `supportedTypes` in order of your app’s preference for its
supported types. The Paste button takes the most-preferred type that the
pasteboard source supports and delivers this to the `payloadAction` closure.

## See Also

### Deprecated initializers

`init<Payload>(supportedTypes: [String], validator: ([NSItemProvider]) ->
Payload?, payloadAction: (Payload) -> Void)`

Creates a Paste button that accepts specific types of data from the
pasteboard, performing a custom validation of the data before sending it to
your app.

Deprecated

`init<Payload>(supportedContentTypes: [UTType], validator: ([NSItemProvider])
-> Payload?, payloadAction: (Payload) -> Void)`

Creates a Paste button that accepts specific types of data from the
pasteboard, performing a custom validation of the data before sending it to
your app.

Deprecated

Initializer

# init(supportedTypes:validator:payloadAction:)

Creates a Paste button that accepts specific types of data from the
pasteboard, performing a custom validation of the data before sending it to
your app.

macOS 10.15–14.4  Deprecated

    
    
    @MainActor
    init<Payload>(
        supportedTypes: [String],
        validator: @escaping ([NSItemProvider]) -> Payload?,
        payloadAction: @escaping (Payload) -> Void
    )

Deprecated

Use the `init(supportedContentTypes:validator:payloadAction:)` initializer
instead.

##  Parameters

`supportedTypes`

    

The exact uniform type identifiers supported by the button. If the pasteboard
doesn’t contain any of the supported types, the button becomes disabled.

`validator`

    

A handler that receives those contents of the pasteboard that conform to
`payloadAction`. Load and inspect these items to determine whether to validate
the button. If you load a valid item, return it from this closure. If the
pasteboard doesn’t contain any valid items, return `nil` to invalidate the
button.

`payloadAction`

    

The handler called when the user clicks the button. This closure receives the
preprocessed result of `validator`.

## Discussion

Set the contents of `supportedTypes` in order of your app’s preference for its
supported types. The Paste button takes the most-preferred type that the
pasteboard source supports and delivers this to the `validator` closure.

## See Also

### Deprecated initializers

`init(supportedTypes: [String], payloadAction: ([NSItemProvider]) -> Void)`

Creates a Paste button that accepts specific types of data from the
pasteboard.

Deprecated

`init<Payload>(supportedContentTypes: [UTType], validator: ([NSItemProvider])
-> Payload?, payloadAction: (Payload) -> Void)`

Creates a Paste button that accepts specific types of data from the
pasteboard, performing a custom validation of the data before sending it to
your app.

Deprecated

Initializer

# init(supportedContentTypes:validator:payloadAction:)

Creates a Paste button that accepts specific types of data from the
pasteboard, performing a custom validation of the data before sending it to
your app.

macOS 11.0–14.4  Deprecated

    
    
    @MainActor
    init<Payload>(
        supportedContentTypes: [UTType],
        validator: @escaping ([NSItemProvider]) -> Payload?,
        payloadAction: @escaping (Payload) -> Void
    )

Deprecated

Use `init(payloadType:onPaste:)` instead.

##  Parameters

`supportedContentTypes`

    

The exact uniform type identifiers supported by the button. If the pasteboard
doesn’t contain any of the supported types, the button becomes disabled.

`validator`

    

A handler that receives those contents of the pasteboard that conform to
`supportedContentTypes`. Load and inspect these items to determine whether to
validate the button. If you load a valid item, return it from this closure. If
the pasteboard doesn’t contain any valid items, return `nil` to invalidate the
button.

`payloadAction`

    

The handler called when the user clicks the button. This closure receives the
preprocessed result of `validator`.

## Discussion

Set the contents of `supportedContentTypes` in order of your app’s preference
for its supported types. The Paste button takes the most-preferred type that
the pasteboard source supports and delivers this to the `validator` closure.

## See Also

### Deprecated initializers

`init(supportedTypes: [String], payloadAction: ([NSItemProvider]) -> Void)`

Creates a Paste button that accepts specific types of data from the
pasteboard.

Deprecated

`init<Payload>(supportedTypes: [String], validator: ([NSItemProvider]) ->
Payload?, payloadAction: (Payload) -> Void)`

Creates a Paste button that accepts specific types of data from the
pasteboard, performing a custom validation of the data before sending it to
your app.

Deprecated



# PlainTextEditorStyle

Initializer

# init()

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    init()



# PreferenceKey

Type Property

# defaultValue

The default value of the preference.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static var defaultValue: Self.Value { get }

**Required** Default implementation provided.

## Discussion

Views that have no explicit value for the key produce this default value.
Combining child views may remove an implicit value produced by using the
default. This means that `reduce(value: &x, nextValue: {defaultValue})`
shouldn’t change the meaning of `x`.

## Default Implementations

### PreferenceKey Implementations

`static var defaultValue: Self.Value`

Let nil-expressible values default-initialize to nil.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

## See Also

### Getting the default value

`associatedtype Value`

The type of value produced by this preference.

**Required**

Associated Type

# Value

The type of value produced by this preference.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    associatedtype Value

**Required**

## See Also

### Getting the default value

`static var defaultValue: Self.Value`

The default value of the preference.

**Required** Default implementation provided.

Type Method

# reduce(value:nextValue:)

Combines a sequence of values by modifying the previously-accumulated value
with the result of a closure that provides the next value.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static func reduce(
        value: inout Self.Value,
        nextValue: () -> Self.Value
    )

**Required**

##  Parameters

`value`

    

The value accumulated through previous calls to this method. The
implementation should modify this value.

`nextValue`

    

A closure that returns the next value in the sequence.

## Discussion

This method receives its values in view-tree order. Conceptually, this
combines the preference value from one tree with that of its next sibling.



# PageIndexViewStyle.BackgroundDisplayMode

Type Property

# automatic

Background will use the default for the platform.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS 8.0+
visionOS 1.0+

    
    
    static let automatic: PageIndexViewStyle.BackgroundDisplayMode

## See Also

### Getting the display modes

`static let always: PageIndexViewStyle.BackgroundDisplayMode`

Background is always displayed behind the page index view.

`static let interactive: PageIndexViewStyle.BackgroundDisplayMode`

Background is only shown while the index view is interacted with.

`static let never: PageIndexViewStyle.BackgroundDisplayMode`

Background is never displayed behind the page index view.

Type Property

# always

Background is always displayed behind the page index view.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  tvOS 14.0+  visionOS 1.0+

    
    
    static let always: PageIndexViewStyle.BackgroundDisplayMode

## See Also

### Getting the display modes

`static let automatic: PageIndexViewStyle.BackgroundDisplayMode`

Background will use the default for the platform.

`static let interactive: PageIndexViewStyle.BackgroundDisplayMode`

Background is only shown while the index view is interacted with.

`static let never: PageIndexViewStyle.BackgroundDisplayMode`

Background is never displayed behind the page index view.

Type Property

# interactive

Background is only shown while the index view is interacted with.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  tvOS 14.0+  visionOS 1.0+

    
    
    static let interactive: PageIndexViewStyle.BackgroundDisplayMode

## See Also

### Getting the display modes

`static let automatic: PageIndexViewStyle.BackgroundDisplayMode`

Background will use the default for the platform.

`static let always: PageIndexViewStyle.BackgroundDisplayMode`

Background is always displayed behind the page index view.

`static let never: PageIndexViewStyle.BackgroundDisplayMode`

Background is never displayed behind the page index view.

Type Property

# never

Background is never displayed behind the page index view.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS 8.0+
visionOS 1.0+

    
    
    static let never: PageIndexViewStyle.BackgroundDisplayMode

## See Also

### Getting the display modes

`static let automatic: PageIndexViewStyle.BackgroundDisplayMode`

Background will use the default for the platform.

`static let always: PageIndexViewStyle.BackgroundDisplayMode`

Background is always displayed behind the page index view.

`static let interactive: PageIndexViewStyle.BackgroundDisplayMode`

Background is only shown while the index view is interacted with.



# PrimitiveButtonStyle

Type Property

# automatic

The default button style, based on the button’s context.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static var automatic: DefaultButtonStyle { get }

Available when `Self` is `DefaultButtonStyle`.

## Discussion

If you create a button directly on a blank canvas, the style varies by
platform. iOS uses the borderless button style by default, whereas macOS,
tvOS, and watchOS use the bordered button style.

If you create a button inside a container, like a `List`, the style resolves
to the recommended style for buttons inside that container for that specific
platform.

You can override a button’s style. To apply the default style to a button, or
to a view that contains buttons, use the `buttonStyle(_:)` modifier.

## See Also

### Getting built-in button styles

`static var accessoryBar: AccessoryBarButtonStyle`

A button style that is typically used in the context of an accessory toolbar
(sometimes refererred to as a “scope bar”), for buttons that narrow the focus
of a search or other operation.

Available when `Self` is `AccessoryBarButtonStyle`.

`static var accessoryBarAction: AccessoryBarActionButtonStyle`

A button style that you use for extra actions in an accessory toolbar.

Available when `Self` is `AccessoryBarActionButtonStyle`.

`static var bordered: BorderedButtonStyle`

A button style that applies standard border artwork based on the button’s
context.

Available when `Self` is `BorderedButtonStyle`.

`static var borderedProminent: BorderedProminentButtonStyle`

A button style that applies standard border prominent artwork based on the
button’s context.

Available when `Self` is `BorderedProminentButtonStyle`.

`static var borderless: BorderlessButtonStyle`

A button style that doesn’t apply a border.

Available when `Self` is `BorderlessButtonStyle`.

`static var card: CardButtonStyle`

A button style that doesn’t pad the content, and applies a motion effect when
a button has focus.

Available when `Self` is `CardButtonStyle`.

`static var link: LinkButtonStyle`

A button style for buttons that emulate links.

Available when `Self` is `LinkButtonStyle`.

`static var plain: PlainButtonStyle`

A button style that doesn’t style or decorate its content while idle, but may
apply a visual effect to indicate the pressed, focused, or enabled state of
the button.

Available when `Self` is `PlainButtonStyle`.

Type Property

# accessoryBar

A button style that is typically used in the context of an accessory toolbar
(sometimes refererred to as a “scope bar”), for buttons that narrow the focus
of a search or other operation.

macOS 14.0+  visionOS 1.0+

    
    
    static var accessoryBar: AccessoryBarButtonStyle { get }

Available when `Self` is `AccessoryBarButtonStyle`.

## Discussion

This is the default button style for views in accessory toolbars, created with
`ToolbarItemPlacement.init(id:_)`, and for searchable scopes.

This style will also affect button style `Toggle`s, as well as button style
`Picker`s and `Menu`s.

## See Also

### Getting built-in button styles

`static var automatic: DefaultButtonStyle`

The default button style, based on the button’s context.

Available when `Self` is `DefaultButtonStyle`.

`static var accessoryBarAction: AccessoryBarActionButtonStyle`

A button style that you use for extra actions in an accessory toolbar.

Available when `Self` is `AccessoryBarActionButtonStyle`.

`static var bordered: BorderedButtonStyle`

A button style that applies standard border artwork based on the button’s
context.

Available when `Self` is `BorderedButtonStyle`.

`static var borderedProminent: BorderedProminentButtonStyle`

A button style that applies standard border prominent artwork based on the
button’s context.

Available when `Self` is `BorderedProminentButtonStyle`.

`static var borderless: BorderlessButtonStyle`

A button style that doesn’t apply a border.

Available when `Self` is `BorderlessButtonStyle`.

`static var card: CardButtonStyle`

A button style that doesn’t pad the content, and applies a motion effect when
a button has focus.

Available when `Self` is `CardButtonStyle`.

`static var link: LinkButtonStyle`

A button style for buttons that emulate links.

Available when `Self` is `LinkButtonStyle`.

`static var plain: PlainButtonStyle`

A button style that doesn’t style or decorate its content while idle, but may
apply a visual effect to indicate the pressed, focused, or enabled state of
the button.

Available when `Self` is `PlainButtonStyle`.

Type Property

# accessoryBarAction

A button style that you use for extra actions in an accessory toolbar.

macOS 14.0+  visionOS 1.0+

    
    
    static var accessoryBarAction: AccessoryBarActionButtonStyle { get }

Available when `Self` is `AccessoryBarActionButtonStyle`.

## Discussion

Use this style for buttons that perform extra actions relative to the
accessory toolbar’s main functions, like adding or editing filters. This style
also affects other view types that you apply a button style to, like `Toggle`,
`Picker`, and `Menu` instances.

## See Also

### Getting built-in button styles

`static var automatic: DefaultButtonStyle`

The default button style, based on the button’s context.

Available when `Self` is `DefaultButtonStyle`.

`static var accessoryBar: AccessoryBarButtonStyle`

A button style that is typically used in the context of an accessory toolbar
(sometimes refererred to as a “scope bar”), for buttons that narrow the focus
of a search or other operation.

Available when `Self` is `AccessoryBarButtonStyle`.

`static var bordered: BorderedButtonStyle`

A button style that applies standard border artwork based on the button’s
context.

Available when `Self` is `BorderedButtonStyle`.

`static var borderedProminent: BorderedProminentButtonStyle`

A button style that applies standard border prominent artwork based on the
button’s context.

Available when `Self` is `BorderedProminentButtonStyle`.

`static var borderless: BorderlessButtonStyle`

A button style that doesn’t apply a border.

Available when `Self` is `BorderlessButtonStyle`.

`static var card: CardButtonStyle`

A button style that doesn’t pad the content, and applies a motion effect when
a button has focus.

Available when `Self` is `CardButtonStyle`.

`static var link: LinkButtonStyle`

A button style for buttons that emulate links.

Available when `Self` is `LinkButtonStyle`.

`static var plain: PlainButtonStyle`

A button style that doesn’t style or decorate its content while idle, but may
apply a visual effect to indicate the pressed, focused, or enabled state of
the button.

Available when `Self` is `PlainButtonStyle`.

Type Property

# bordered

A button style that applies standard border artwork based on the button’s
context.

iOS 15.0+  iPadOS 15.0+  macOS 10.15+  Mac Catalyst 15.0+  tvOS 13.0+  watchOS
7.0+  visionOS 1.0+

    
    
    static var bordered: BorderedButtonStyle { get }

Available when `Self` is `BorderedButtonStyle`.

## Discussion

To apply this style to a button, or to a view that contains buttons, use the
`buttonStyle(_:)` modifier.

## See Also

### Getting built-in button styles

`static var automatic: DefaultButtonStyle`

The default button style, based on the button’s context.

Available when `Self` is `DefaultButtonStyle`.

`static var accessoryBar: AccessoryBarButtonStyle`

A button style that is typically used in the context of an accessory toolbar
(sometimes refererred to as a “scope bar”), for buttons that narrow the focus
of a search or other operation.

Available when `Self` is `AccessoryBarButtonStyle`.

`static var accessoryBarAction: AccessoryBarActionButtonStyle`

A button style that you use for extra actions in an accessory toolbar.

Available when `Self` is `AccessoryBarActionButtonStyle`.

`static var borderedProminent: BorderedProminentButtonStyle`

A button style that applies standard border prominent artwork based on the
button’s context.

Available when `Self` is `BorderedProminentButtonStyle`.

`static var borderless: BorderlessButtonStyle`

A button style that doesn’t apply a border.

Available when `Self` is `BorderlessButtonStyle`.

`static var card: CardButtonStyle`

A button style that doesn’t pad the content, and applies a motion effect when
a button has focus.

Available when `Self` is `CardButtonStyle`.

`static var link: LinkButtonStyle`

A button style for buttons that emulate links.

Available when `Self` is `LinkButtonStyle`.

`static var plain: PlainButtonStyle`

A button style that doesn’t style or decorate its content while idle, but may
apply a visual effect to indicate the pressed, focused, or enabled state of
the button.

Available when `Self` is `PlainButtonStyle`.

Type Property

# borderedProminent

A button style that applies standard border prominent artwork based on the
button’s context.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var borderedProminent: BorderedProminentButtonStyle { get }

Available when `Self` is `BorderedProminentButtonStyle`.

## Discussion

To apply this style to a button, or to a view that contains buttons, use the
`buttonStyle(_:)` modifier.

## See Also

### Getting built-in button styles

`static var automatic: DefaultButtonStyle`

The default button style, based on the button’s context.

Available when `Self` is `DefaultButtonStyle`.

`static var accessoryBar: AccessoryBarButtonStyle`

A button style that is typically used in the context of an accessory toolbar
(sometimes refererred to as a “scope bar”), for buttons that narrow the focus
of a search or other operation.

Available when `Self` is `AccessoryBarButtonStyle`.

`static var accessoryBarAction: AccessoryBarActionButtonStyle`

A button style that you use for extra actions in an accessory toolbar.

Available when `Self` is `AccessoryBarActionButtonStyle`.

`static var bordered: BorderedButtonStyle`

A button style that applies standard border artwork based on the button’s
context.

Available when `Self` is `BorderedButtonStyle`.

`static var borderless: BorderlessButtonStyle`

A button style that doesn’t apply a border.

Available when `Self` is `BorderlessButtonStyle`.

`static var card: CardButtonStyle`

A button style that doesn’t pad the content, and applies a motion effect when
a button has focus.

Available when `Self` is `CardButtonStyle`.

`static var link: LinkButtonStyle`

A button style for buttons that emulate links.

Available when `Self` is `LinkButtonStyle`.

`static var plain: PlainButtonStyle`

A button style that doesn’t style or decorate its content while idle, but may
apply a visual effect to indicate the pressed, focused, or enabled state of
the button.

Available when `Self` is `PlainButtonStyle`.

Type Property

# borderless

A button style that doesn’t apply a border.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 17.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var borderless: BorderlessButtonStyle { get }

Available when `Self` is `BorderlessButtonStyle`.

## Discussion

To apply this style to a button, or to a view that contains buttons, use the
`buttonStyle(_:)` modifier.

On tvOS, this button style adds a default hover effect to the first image of
the button’s content, if one exists. You can supply a different hover effect
by using the `hoverEffect(_:)` modifier in the button’s label.

## See Also

### Getting built-in button styles

`static var automatic: DefaultButtonStyle`

The default button style, based on the button’s context.

Available when `Self` is `DefaultButtonStyle`.

`static var accessoryBar: AccessoryBarButtonStyle`

A button style that is typically used in the context of an accessory toolbar
(sometimes refererred to as a “scope bar”), for buttons that narrow the focus
of a search or other operation.

Available when `Self` is `AccessoryBarButtonStyle`.

`static var accessoryBarAction: AccessoryBarActionButtonStyle`

A button style that you use for extra actions in an accessory toolbar.

Available when `Self` is `AccessoryBarActionButtonStyle`.

`static var bordered: BorderedButtonStyle`

A button style that applies standard border artwork based on the button’s
context.

Available when `Self` is `BorderedButtonStyle`.

`static var borderedProminent: BorderedProminentButtonStyle`

A button style that applies standard border prominent artwork based on the
button’s context.

Available when `Self` is `BorderedProminentButtonStyle`.

`static var card: CardButtonStyle`

A button style that doesn’t pad the content, and applies a motion effect when
a button has focus.

Available when `Self` is `CardButtonStyle`.

`static var link: LinkButtonStyle`

A button style for buttons that emulate links.

Available when `Self` is `LinkButtonStyle`.

`static var plain: PlainButtonStyle`

A button style that doesn’t style or decorate its content while idle, but may
apply a visual effect to indicate the pressed, focused, or enabled state of
the button.

Available when `Self` is `PlainButtonStyle`.

Type Property

# card

A button style that doesn’t pad the content, and applies a motion effect when
a button has focus.

tvOS 14.0+

    
    
    static var card: CardButtonStyle { get }

Available when `Self` is `CardButtonStyle`.

## Discussion

This style doesn’t apply padding to its contents, so images, text, and other
content display edge-to-edge. A button with this style appears partially
translucent. When the user focuses on a card button, the button animates up to
a raised position with more opacity. This style also applies the standard
background colors for unfocused and focused states in both light and dark
mode.

To apply this style to a button, or to a view that contains buttons, use the
`buttonStyle(_:)` modifier.

## See Also

### Getting built-in button styles

`static var automatic: DefaultButtonStyle`

The default button style, based on the button’s context.

Available when `Self` is `DefaultButtonStyle`.

`static var accessoryBar: AccessoryBarButtonStyle`

A button style that is typically used in the context of an accessory toolbar
(sometimes refererred to as a “scope bar”), for buttons that narrow the focus
of a search or other operation.

Available when `Self` is `AccessoryBarButtonStyle`.

`static var accessoryBarAction: AccessoryBarActionButtonStyle`

A button style that you use for extra actions in an accessory toolbar.

Available when `Self` is `AccessoryBarActionButtonStyle`.

`static var bordered: BorderedButtonStyle`

A button style that applies standard border artwork based on the button’s
context.

Available when `Self` is `BorderedButtonStyle`.

`static var borderedProminent: BorderedProminentButtonStyle`

A button style that applies standard border prominent artwork based on the
button’s context.

Available when `Self` is `BorderedProminentButtonStyle`.

`static var borderless: BorderlessButtonStyle`

A button style that doesn’t apply a border.

Available when `Self` is `BorderlessButtonStyle`.

`static var link: LinkButtonStyle`

A button style for buttons that emulate links.

Available when `Self` is `LinkButtonStyle`.

`static var plain: PlainButtonStyle`

A button style that doesn’t style or decorate its content while idle, but may
apply a visual effect to indicate the pressed, focused, or enabled state of
the button.

Available when `Self` is `PlainButtonStyle`.

Type Property

# link

A button style for buttons that emulate links.

macOS 10.15+

    
    
    static var link: LinkButtonStyle { get }

Available when `Self` is `LinkButtonStyle`.

## Discussion

To apply this style to a button, or to a view that contains buttons, use the
`buttonStyle(_:)` modifier.

## See Also

### Getting built-in button styles

`static var automatic: DefaultButtonStyle`

The default button style, based on the button’s context.

Available when `Self` is `DefaultButtonStyle`.

`static var accessoryBar: AccessoryBarButtonStyle`

A button style that is typically used in the context of an accessory toolbar
(sometimes refererred to as a “scope bar”), for buttons that narrow the focus
of a search or other operation.

Available when `Self` is `AccessoryBarButtonStyle`.

`static var accessoryBarAction: AccessoryBarActionButtonStyle`

A button style that you use for extra actions in an accessory toolbar.

Available when `Self` is `AccessoryBarActionButtonStyle`.

`static var bordered: BorderedButtonStyle`

A button style that applies standard border artwork based on the button’s
context.

Available when `Self` is `BorderedButtonStyle`.

`static var borderedProminent: BorderedProminentButtonStyle`

A button style that applies standard border prominent artwork based on the
button’s context.

Available when `Self` is `BorderedProminentButtonStyle`.

`static var borderless: BorderlessButtonStyle`

A button style that doesn’t apply a border.

Available when `Self` is `BorderlessButtonStyle`.

`static var card: CardButtonStyle`

A button style that doesn’t pad the content, and applies a motion effect when
a button has focus.

Available when `Self` is `CardButtonStyle`.

`static var plain: PlainButtonStyle`

A button style that doesn’t style or decorate its content while idle, but may
apply a visual effect to indicate the pressed, focused, or enabled state of
the button.

Available when `Self` is `PlainButtonStyle`.

Type Property

# plain

A button style that doesn’t style or decorate its content while idle, but may
apply a visual effect to indicate the pressed, focused, or enabled state of
the button.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static var plain: PlainButtonStyle { get }

Available when `Self` is `PlainButtonStyle`.

## Discussion

To apply this style to a button, or to a view that contains buttons, use the
`buttonStyle(_:)` modifier.

## See Also

### Getting built-in button styles

`static var automatic: DefaultButtonStyle`

The default button style, based on the button’s context.

Available when `Self` is `DefaultButtonStyle`.

`static var accessoryBar: AccessoryBarButtonStyle`

A button style that is typically used in the context of an accessory toolbar
(sometimes refererred to as a “scope bar”), for buttons that narrow the focus
of a search or other operation.

Available when `Self` is `AccessoryBarButtonStyle`.

`static var accessoryBarAction: AccessoryBarActionButtonStyle`

A button style that you use for extra actions in an accessory toolbar.

Available when `Self` is `AccessoryBarActionButtonStyle`.

`static var bordered: BorderedButtonStyle`

A button style that applies standard border artwork based on the button’s
context.

Available when `Self` is `BorderedButtonStyle`.

`static var borderedProminent: BorderedProminentButtonStyle`

A button style that applies standard border prominent artwork based on the
button’s context.

Available when `Self` is `BorderedProminentButtonStyle`.

`static var borderless: BorderlessButtonStyle`

A button style that doesn’t apply a border.

Available when `Self` is `BorderlessButtonStyle`.

`static var card: CardButtonStyle`

A button style that doesn’t pad the content, and applies a motion effect when
a button has focus.

Available when `Self` is `CardButtonStyle`.

`static var link: LinkButtonStyle`

A button style for buttons that emulate links.

Available when `Self` is `LinkButtonStyle`.

Instance Method

# makeBody(configuration:)

Creates a view that represents the body of a button.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @ViewBuilder
    func makeBody(configuration: Self.Configuration) -> Self.Body

**Required**

##  Parameters

`configuration `

    

The properties of the button.

## Discussion

The system calls this method for each `Button` instance in a view hierarchy
where this style is the current button style.

## See Also

### Creating custom button styles

`typealias Configuration`

The properties of a button.

`associatedtype Body : View`

A view that represents the body of a button.

**Required**

Type Alias

# PrimitiveButtonStyle.Configuration

The properties of a button.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    typealias Configuration = PrimitiveButtonStyleConfiguration

## See Also

### Creating custom button styles

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Creates a view that represents the body of a button.

**Required**

` associatedtype Body : View`

A view that represents the body of a button.

**Required**

Associated Type

# Body

A view that represents the body of a button.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    associatedtype Body : View

**Required**

## See Also

### Creating custom button styles

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Creates a view that represents the body of a button.

**Required**

` typealias Configuration`

The properties of a button.

Structure

# DefaultButtonStyle

The default button style, based on the button’s context.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    struct DefaultButtonStyle

## Overview

You can also use `automatic` to construct this style.

## Topics

### Creating the button style

`init()`

Creates a default button style.

### Supporting types

`func makeBody(configuration: DefaultButtonStyle.Configuration) -> some View`

Creates a view that represents the body of a button.

## Relationships

### Conforms To

  * `PrimitiveButtonStyle`

## See Also

### Supporting types

`struct AccessoryBarButtonStyle`

A button style that you use for actions in an accessory toolbar that narrow
the focus of a search or other operation.

`struct AccessoryBarActionButtonStyle`

A button style that you use for extra actions in an accessory toolbar.

`struct BorderedButtonStyle`

A button style that applies standard border artwork based on the button’s
context.

`struct BorderedProminentButtonStyle`

A button style that applies standard border prominent artwork based on the
button’s context.

`struct BorderlessButtonStyle`

A button style that doesn’t apply a border.

`struct CardButtonStyle`

A button style that doesn’t pad the content, and applies a motion effect when
a button has focus.

`struct LinkButtonStyle`

A button style for buttons that emulate links.

`struct PlainButtonStyle`

A button style that doesn’t style or decorate its content while idle, but may
apply a visual effect to indicate the pressed, focused, or enabled state of
the button.

Structure

# AccessoryBarButtonStyle

A button style that you use for actions in an accessory toolbar that narrow
the focus of a search or other operation.

macOS 14.0+  visionOS 1.0+

    
    
    struct AccessoryBarButtonStyle

## Overview

This is the default button style for views in accessory toolbars, which you
create with `init(id:)`, and for searchable scopes. This style also affects
other view types that you apply a button style to, like `Toggle`, `Picker`,
and `Menu` instances.

Use `accessoryBar` to construct this style.

## Topics

### Creating the button style

`init()`

Creates an accessory toolbar style

### Supporting types

`func makeBody(configuration: AccessoryBarButtonStyle.Configuration) -> some
View`

Creates a view that represents the body of a button.

## Relationships

### Conforms To

  * `PrimitiveButtonStyle`

## See Also

### Supporting types

`struct DefaultButtonStyle`

The default button style, based on the button’s context.

`struct AccessoryBarActionButtonStyle`

A button style that you use for extra actions in an accessory toolbar.

`struct BorderedButtonStyle`

A button style that applies standard border artwork based on the button’s
context.

`struct BorderedProminentButtonStyle`

A button style that applies standard border prominent artwork based on the
button’s context.

`struct BorderlessButtonStyle`

A button style that doesn’t apply a border.

`struct CardButtonStyle`

A button style that doesn’t pad the content, and applies a motion effect when
a button has focus.

`struct LinkButtonStyle`

A button style for buttons that emulate links.

`struct PlainButtonStyle`

A button style that doesn’t style or decorate its content while idle, but may
apply a visual effect to indicate the pressed, focused, or enabled state of
the button.

Structure

# AccessoryBarActionButtonStyle

A button style that you use for extra actions in an accessory toolbar.

macOS 14.0+  visionOS 1.0+

    
    
    struct AccessoryBarActionButtonStyle

## Overview

Use this style for buttons that perform extra actions relative to the
accessory toolbar’s main functions, like adding or editing filters. This style
also affects other view types that you apply a button style to, like `Toggle`,
`Picker`, and `Menu` instances.

Use `accessoryBarAction` to construct this style.

## Topics

### Creating the button style

`init()`

Creates an accessory toolbar action button style

### Supporting types

`func makeBody(configuration: AccessoryBarActionButtonStyle.Configuration) ->
some View`

Creates a view that represents the body of a button.

## Relationships

### Conforms To

  * `PrimitiveButtonStyle`

## See Also

### Supporting types

`struct DefaultButtonStyle`

The default button style, based on the button’s context.

`struct AccessoryBarButtonStyle`

A button style that you use for actions in an accessory toolbar that narrow
the focus of a search or other operation.

`struct BorderedButtonStyle`

A button style that applies standard border artwork based on the button’s
context.

`struct BorderedProminentButtonStyle`

A button style that applies standard border prominent artwork based on the
button’s context.

`struct BorderlessButtonStyle`

A button style that doesn’t apply a border.

`struct CardButtonStyle`

A button style that doesn’t pad the content, and applies a motion effect when
a button has focus.

`struct LinkButtonStyle`

A button style for buttons that emulate links.

`struct PlainButtonStyle`

A button style that doesn’t style or decorate its content while idle, but may
apply a visual effect to indicate the pressed, focused, or enabled state of
the button.

Structure

# BorderedButtonStyle

A button style that applies standard border artwork based on the button’s
context.

iOS 15.0+  iPadOS 15.0+  macOS 10.15+  Mac Catalyst 15.0+  tvOS 13.0+  watchOS
7.0+  visionOS 1.0+

    
    
    struct BorderedButtonStyle

## Overview

You can also use `bordered` to construct this style.

## Topics

### Creating the button style

`init()`

Creates a bordered button style.

### Supporting types

`func makeBody(configuration: BorderedButtonStyle.Configuration) -> some View`

Creates a view that represents the body of a button.

### Deprecated symbols

`init(tint: Color)`

Creates a bordered button style with a tint color.

Deprecated

## Relationships

### Conforms To

  * `PrimitiveButtonStyle`

## See Also

### Supporting types

`struct DefaultButtonStyle`

The default button style, based on the button’s context.

`struct AccessoryBarButtonStyle`

A button style that you use for actions in an accessory toolbar that narrow
the focus of a search or other operation.

`struct AccessoryBarActionButtonStyle`

A button style that you use for extra actions in an accessory toolbar.

`struct BorderedProminentButtonStyle`

A button style that applies standard border prominent artwork based on the
button’s context.

`struct BorderlessButtonStyle`

A button style that doesn’t apply a border.

`struct CardButtonStyle`

A button style that doesn’t pad the content, and applies a motion effect when
a button has focus.

`struct LinkButtonStyle`

A button style for buttons that emulate links.

`struct PlainButtonStyle`

A button style that doesn’t style or decorate its content while idle, but may
apply a visual effect to indicate the pressed, focused, or enabled state of
the button.

Structure

# BorderedProminentButtonStyle

A button style that applies standard border prominent artwork based on the
button’s context.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    struct BorderedProminentButtonStyle

## Overview

Use `borderedProminent` to construct this style.

## Topics

### Creating the button style

`init()`

Creates a bordered prominent button style.

## Relationships

### Conforms To

  * `PrimitiveButtonStyle`

## See Also

### Supporting types

`struct DefaultButtonStyle`

The default button style, based on the button’s context.

`struct AccessoryBarButtonStyle`

A button style that you use for actions in an accessory toolbar that narrow
the focus of a search or other operation.

`struct AccessoryBarActionButtonStyle`

A button style that you use for extra actions in an accessory toolbar.

`struct BorderedButtonStyle`

A button style that applies standard border artwork based on the button’s
context.

`struct BorderlessButtonStyle`

A button style that doesn’t apply a border.

`struct CardButtonStyle`

A button style that doesn’t pad the content, and applies a motion effect when
a button has focus.

`struct LinkButtonStyle`

A button style for buttons that emulate links.

`struct PlainButtonStyle`

A button style that doesn’t style or decorate its content while idle, but may
apply a visual effect to indicate the pressed, focused, or enabled state of
the button.

Structure

# BorderlessButtonStyle

A button style that doesn’t apply a border.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 17.0+  watchOS
8.0+  visionOS 1.0+

    
    
    struct BorderlessButtonStyle

## Overview

You can also use `borderless` to construct this style.

## Topics

### Creating the button style

`init()`

Creates a borderless button style.

### Supporting types

`func makeBody(configuration: BorderlessButtonStyle.Configuration) -> some
View`

Creates a view that represents the body of a button.

## Relationships

### Conforms To

  * `PrimitiveButtonStyle`

## See Also

### Supporting types

`struct DefaultButtonStyle`

The default button style, based on the button’s context.

`struct AccessoryBarButtonStyle`

A button style that you use for actions in an accessory toolbar that narrow
the focus of a search or other operation.

`struct AccessoryBarActionButtonStyle`

A button style that you use for extra actions in an accessory toolbar.

`struct BorderedButtonStyle`

A button style that applies standard border artwork based on the button’s
context.

`struct BorderedProminentButtonStyle`

A button style that applies standard border prominent artwork based on the
button’s context.

`struct CardButtonStyle`

A button style that doesn’t pad the content, and applies a motion effect when
a button has focus.

`struct LinkButtonStyle`

A button style for buttons that emulate links.

`struct PlainButtonStyle`

A button style that doesn’t style or decorate its content while idle, but may
apply a visual effect to indicate the pressed, focused, or enabled state of
the button.

Structure

# CardButtonStyle

A button style that doesn’t pad the content, and applies a motion effect when
a button has focus.

tvOS 14.0+

    
    
    struct CardButtonStyle

## Overview

You can also use `card` to construct this style.

## Topics

### Creating the button style

`init()`

Creates a style that doesn’t pad a button’s content and applies a motion
effect to a focused button.

### Supporting types

`func makeBody(configuration: CardButtonStyle.Configuration) -> some View`

Creates a view that represents the body of a button.

## Relationships

### Conforms To

  * `PrimitiveButtonStyle`

## See Also

### Related Documentation

`class TVCardView`

A view that responds to focus interaction with a motion effect it applies to
all of its subviews.

### Supporting types

`struct DefaultButtonStyle`

The default button style, based on the button’s context.

`struct AccessoryBarButtonStyle`

A button style that you use for actions in an accessory toolbar that narrow
the focus of a search or other operation.

`struct AccessoryBarActionButtonStyle`

A button style that you use for extra actions in an accessory toolbar.

`struct BorderedButtonStyle`

A button style that applies standard border artwork based on the button’s
context.

`struct BorderedProminentButtonStyle`

A button style that applies standard border prominent artwork based on the
button’s context.

`struct BorderlessButtonStyle`

A button style that doesn’t apply a border.

`struct LinkButtonStyle`

A button style for buttons that emulate links.

`struct PlainButtonStyle`

A button style that doesn’t style or decorate its content while idle, but may
apply a visual effect to indicate the pressed, focused, or enabled state of
the button.

Structure

# LinkButtonStyle

A button style for buttons that emulate links.

macOS 10.15+

    
    
    struct LinkButtonStyle

## Overview

You can also use `link` to construct this style.

## Topics

### Creating the button style

`init()`

Creates a link button style.

### Supporting types

`func makeBody(configuration: LinkButtonStyle.Configuration) -> some View`

Creates a view that represents the body of a button.

## Relationships

### Conforms To

  * `PrimitiveButtonStyle`

## See Also

### Supporting types

`struct DefaultButtonStyle`

The default button style, based on the button’s context.

`struct AccessoryBarButtonStyle`

A button style that you use for actions in an accessory toolbar that narrow
the focus of a search or other operation.

`struct AccessoryBarActionButtonStyle`

A button style that you use for extra actions in an accessory toolbar.

`struct BorderedButtonStyle`

A button style that applies standard border artwork based on the button’s
context.

`struct BorderedProminentButtonStyle`

A button style that applies standard border prominent artwork based on the
button’s context.

`struct BorderlessButtonStyle`

A button style that doesn’t apply a border.

`struct CardButtonStyle`

A button style that doesn’t pad the content, and applies a motion effect when
a button has focus.

`struct PlainButtonStyle`

A button style that doesn’t style or decorate its content while idle, but may
apply a visual effect to indicate the pressed, focused, or enabled state of
the button.

Structure

# PlainButtonStyle

A button style that doesn’t style or decorate its content while idle, but may
apply a visual effect to indicate the pressed, focused, or enabled state of
the button.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    struct PlainButtonStyle

## Overview

You can also use `plain` to construct this style.

## Topics

### Creating the button style

`init()`

Creates a plain button style.

### Supporting types

`func makeBody(configuration: PlainButtonStyle.Configuration) -> some View`

Creates a view that represents the body of a button.

## Relationships

### Conforms To

  * `PrimitiveButtonStyle`

## See Also

### Supporting types

`struct DefaultButtonStyle`

The default button style, based on the button’s context.

`struct AccessoryBarButtonStyle`

A button style that you use for actions in an accessory toolbar that narrow
the focus of a search or other operation.

`struct AccessoryBarActionButtonStyle`

A button style that you use for extra actions in an accessory toolbar.

`struct BorderedButtonStyle`

A button style that applies standard border artwork based on the button’s
context.

`struct BorderedProminentButtonStyle`

A button style that applies standard border prominent artwork based on the
button’s context.

`struct BorderlessButtonStyle`

A button style that doesn’t apply a border.

`struct CardButtonStyle`

A button style that doesn’t pad the content, and applies a motion effect when
a button has focus.

`struct LinkButtonStyle`

A button style for buttons that emulate links.



# PullDownMenuBarExtraStyle

Initializer

# init()

Creates a pull down menu bar extra style.

macOS 13.0+

    
    
    init()



# PreviewProvider

Type Property

# previews

A collection of views to preview.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @ViewBuilder @MainActor
    static var previews: Self.Previews { get }

**Required**

## Discussion

Implement a computed `previews` property to indicate the content to preview.
Xcode generates a preview for each view that you list. You can apply `View`
modifiers to the views, like you do when creating a custom view. For a
preview, you can also use various preview-specific modifiers that customize
the preview. For example, you can choose a specific device for the preview by
adding the `previewDevice(_:)` modifier:

For the full list of preview-specific modifiers, see Previews in Xcode.

## See Also

### Creating a preview

`associatedtype Previews : View`

The type to preview.

**Required**

Associated Type

# Previews

The type to preview.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    associatedtype Previews : View

**Required**

## Discussion

When you create a preview, Swift infers this type from your implementation of
the required `previews` property.

## See Also

### Creating a preview

`static var previews: Self.Previews`

A collection of views to preview.

**Required**

Type Property

# platform

The platform on which to run the provider.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @MainActor
    static var platform: PreviewPlatform? { get }

**Required** Default implementation provided.

## Discussion

Xcode infers the platform for a preview based on the currently selected
target. If you have a multiplatform target and want to suggest a particular
target for a preview, implement the `platform` computed property to provide a
hint, and specify one of the `PreviewPlatform` values:

Xcode ignores this value unless you have a multiplatform target.

## Default Implementations

### PreviewProvider Implementations

`static var platform: PreviewPlatform?`

The platform to run the provider on.

Type Property

# previews

A collection of views to preview.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @ViewBuilder @MainActor
    static var previews: Self.Previews { get }

**Required**

## Discussion

Implement a computed `previews` property to indicate the content to preview.
Xcode generates a preview for each view that you list. You can apply `View`
modifiers to the views, like you do when creating a custom view. For a
preview, you can also use various preview-specific modifiers that customize
the preview. For example, you can choose a specific device for the preview by
adding the `previewDevice(_:)` modifier:

For the full list of preview-specific modifiers, see Previews in Xcode.

## See Also

### Creating a preview

`associatedtype Previews : View`

The type to preview.

**Required**

Associated Type

# Previews

The type to preview.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    associatedtype Previews : View

**Required**

## Discussion

When you create a preview, Swift infers this type from your implementation of
the required `previews` property.

## See Also

### Creating a preview

`static var previews: Self.Previews`

A collection of views to preview.

**Required**

Type Property

# platform

The platform on which to run the provider.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @MainActor
    static var platform: PreviewPlatform? { get }

**Required** Default implementation provided.

## Discussion

Xcode infers the platform for a preview based on the currently selected
target. If you have a multiplatform target and want to suggest a particular
target for a preview, implement the `platform` computed property to provide a
hint, and specify one of the `PreviewPlatform` values:

Xcode ignores this value unless you have a multiplatform target.

## Default Implementations

### PreviewProvider Implementations

`static var platform: PreviewPlatform?`

The platform to run the provider on.



# ProgressViewStyleConfiguration

Instance Property

# label

A view that describes the task represented by the progress view.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    var label: ProgressViewStyleConfiguration.Label?

## Discussion

If `nil`, then the task is self-evident from the surrounding context, and the
style does not need to provide any additional description.

If the progress view is defined using a `Progress` instance, then this label
is equivalent to its `localizedDescription`.

## See Also

### Configuring the label

`struct Label`

A type-erased label describing the task represented by the progress view.

Structure

# ProgressViewStyleConfiguration.Label

A type-erased label describing the task represented by the progress view.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    struct Label

## Relationships

### Conforms To

  * `View`

## See Also

### Configuring the label

`var label: ProgressViewStyleConfiguration.Label?`

A view that describes the task represented by the progress view.

Instance Property

# currentValueLabel

A view that describes the current value of a progress view.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    var currentValueLabel: ProgressViewStyleConfiguration.CurrentValueLabel?

## Discussion

If `nil`, then the value of the progress view is either self-evident from the
surrounding context or unknown, and the style does not need to provide any
additional description.

If the progress view is defined using a `Progress` instance, then this label
is equivalent to its `localizedAdditionalDescription`.

## See Also

### Configuring the current value label

`struct CurrentValueLabel`

A type-erased label that describes the current value of a progress view.

Structure

# ProgressViewStyleConfiguration.CurrentValueLabel

A type-erased label that describes the current value of a progress view.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    struct CurrentValueLabel

## Relationships

### Conforms To

  * `View`

## See Also

### Configuring the current value label

`var currentValueLabel: ProgressViewStyleConfiguration.CurrentValueLabel?`

A view that describes the current value of a progress view.

Instance Property

# fractionCompleted

The completed fraction of the task represented by the progress view, from
`0.0` (not yet started) to `1.0` (fully complete), or `nil` if the progress is
indeterminate or relative to a date interval.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    let fractionCompleted: Double?



# PalettePickerStyle

Initializer

# init()

Creates a palette picker style.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    init()



# PopUpButtonPickerStyle

Initializer

# init()

Creates a pop-up button picker style.

macOS 10.15–14.4  Deprecated

    
    
    init()

Deprecated

Use `MenuPickerStyle` instead.



# Persistent storage

Instance Method

# defaultAppStorage(_:)

The default store used by `AppStorage` contained within the view.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func defaultAppStorage(_ store: UserDefaults) -> some View
    

##  Parameters

`store`

    

The user defaults to use as the default store for `AppStorage`.

## Discussion

If unspecified, the default store for a view hierarchy is
`UserDefaults.standard`, but can be set a to a custom one. For example,
sharing defaults between an app and an extension can override the default
store to one created with `UserDefaults.init(suiteName:_)`.

## See Also

### Saving state across app launches

Restoring Your App’s State with SwiftUI

Provide app continuity for users by preserving their current activities.

`struct AppStorage`

A property wrapper type that reflects a value from `UserDefaults` and
invalidates a view on a change in value in that user default.

`struct SceneStorage`

A property wrapper type that reads and writes to persisted, per-scene storage.

Structure

# AppStorage

A property wrapper type that reflects a value from `UserDefaults` and
invalidates a view on a change in value in that user default.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    @frozen @propertyWrapper
    struct AppStorage<Value>

## Topics

### Storing a value

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a string user default.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to an integer user default,
transforming that to `RawRepresentable` data type.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a user default as data.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to an integer user default.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a string user default,
transforming that to `RawRepresentable` data type.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a url user default.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a double user default.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a boolean user default.

`init<RowValue>(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can save and restore table column state.

`init(wrappedValue: Value, String, store: UserDefaults?)`

Creates a property that can read and write to a user default as data via
`PersistentIdentifier`.

### Storing an optional value

`init(String, store: UserDefaults?)`

Creates a property that can read and write an Optional integer user default.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(String, store: UserDefaults?)`

Creates a property that can read and write an Optional string user default.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(String, store: UserDefaults?)`

Creates a property that can read and write an Optional double user default.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init<R>(String, store: UserDefaults?)`

Creates a property that can save and restore an Optional integer, transforming
it to an Optional `RawRepresentable` data type.

`init<R>(String, store: UserDefaults?)`

Creates a property that can save and restore an Optional string, transforming
it to an Optional `RawRepresentable` data type.

`init(String, store: UserDefaults?)`

Creates a property that can read and write an Optional data user default.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(String, store: UserDefaults?)`

Creates a property that can read and write an Optional boolean user default.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(String, store: UserDefaults?)`

Creates a property that can read and write an Optional URL user default.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(String, store: UserDefaults?)`

Creates a property that can read and write an Optional data user default via
`PersistentIdentifier`.

### Getting the value

`var wrappedValue: Value`

`var projectedValue: Binding<Value>`

## Relationships

### Conforms To

  * `DynamicProperty`

## See Also

### Saving state across app launches

Restoring Your App’s State with SwiftUI

Provide app continuity for users by preserving their current activities.

`func defaultAppStorage(UserDefaults) -> some View`

The default store used by `AppStorage` contained within the view.

`struct SceneStorage`

A property wrapper type that reads and writes to persisted, per-scene storage.

Structure

# SceneStorage

A property wrapper type that reads and writes to persisted, per-scene storage.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    @frozen @propertyWrapper
    struct SceneStorage<Value>

## Overview

You use `SceneStorage` when you need automatic state restoration of the value.
`SceneStorage` works very similar to `State`, except its initial value is
restored by the system if it was previously saved, and the value is shared
with other `SceneStorage` variables in the same scene.

The system manages the saving and restoring of `SceneStorage` on your behalf.
The underlying data that backs `SceneStorage` is not available to you, so you
must access it via the `SceneStorage` property wrapper. The system makes no
guarantees as to when and how often the data will be persisted.

Each `Scene` has its own notion of `SceneStorage`, so data is not shared
between scenes.

Ensure that the data you use with `SceneStorage` is lightweight. Data of a
large size, such as model data, should not be stored in `SceneStorage`, as
poor performance may result.

If the `Scene` is explicitly destroyed (e.g. the switcher snapshot is
destroyed on iPadOS or the window is closed on macOS), the data is also
destroyed. Do not use `SceneStorage` with sensitive data.

## Topics

### Storing a value

`init(wrappedValue: Value, String)`

Creates a property that can save and restore a URL.

`init(wrappedValue: Value, String)`

Creates a property that can save and restore an integer.

`init(wrappedValue: Value, String)`

Creates a property that can save and restore a double.

`init(wrappedValue: Value, String)`

Creates a property that can save and restore a string.

`init(wrappedValue: Value, String)`

Creates a property that can save and restore a boolean.

`init(wrappedValue: Value, String)`

Creates a property that can save and restore a string, transforming it to a
`RawRepresentable` data type.

`init(wrappedValue: Value, String)`

Creates a property that can save and restore data.

`init(wrappedValue: Value, String)`

Creates a property that can save and restore an integer, transforming it to a
`RawRepresentable` data type.

`init<RowValue>(wrappedValue: Value, String)`

Creates a property that can save and restore table column state.

`init(wrappedValue: Value, String)`

Creates a property that can save and restore a `PersistentIdentifier`.

### Storing an optional value

`init(String)`

Creates a property that can save and restore an Optional string.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init<R>(String)`

Creates a property that can save and restore an Optional integer, transforming
it to an Optional `RawRepresentable` data type.

`init(String)`

Creates a property that can save and restore an Optional double.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(String)`

Creates a property that can save and restore an Optional boolean.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(String)`

Creates a property that can save and restore an Optional data.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(String)`

Creates a property that can save and restore an Optional URL.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init(String)`

Creates a property that can save and restore an Optional integer.

Available when `Value` conforms to `ExpressibleByNilLiteral`.

`init<R>(String)`

Creates a property that can save and restore an Optional string, transforming
it to an Optional `RawRepresentable` data type.

`init(String)`

Creates a property that can read and write an Optional data user default via
`PersistentIdentifier`.

### Getting the value

`var wrappedValue: Value`

The underlying value referenced by the state variable.

`var projectedValue: Binding<Value>`

A binding to the state value.

## Relationships

### Conforms To

  * `DynamicProperty`

## See Also

### Saving state across app launches

Restoring Your App’s State with SwiftUI

Provide app continuity for users by preserving their current activities.

`func defaultAppStorage(UserDefaults) -> some View`

The default store used by `AppStorage` contained within the view.

`struct AppStorage`

A property wrapper type that reflects a value from `UserDefaults` and
invalidates a view on a change in value in that user default.

Instance Property

# managedObjectContext

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var managedObjectContext: NSManagedObjectContext { get set }

## See Also

### Accessing Core Data

Loading and Displaying a Large Data Feed

Consume data in the background, and lower memory use by batching imports and
preventing duplicate records.

`struct FetchRequest`

A property wrapper type that retrieves entities from a Core Data persistent
store.

`struct FetchedResults`

A collection of results retrieved from a Core Data store.

`struct SectionedFetchRequest`

A property wrapper type that retrieves entities, grouped into sections, from a
Core Data persistent store.

`struct SectionedFetchResults`

A collection of results retrieved from a Core Data persistent store, grouped
into sections.

Structure

# FetchRequest

A property wrapper type that retrieves entities from a Core Data persistent
store.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @MainActor @propertyWrapper
    struct FetchRequest<Result> where Result : NSFetchRequestResult

## Overview

Use a `FetchRequest` property wrapper to declare a `FetchedResults` property
that provides a collection of Core Data managed objects to a SwiftUI view. The
request infers the entity type from the `Result` placeholder type that you
specify. Condition the request with an optional predicate and sort
descriptors. For example, you can create a request to list all `Quake` managed
objects that the Loading and Displaying a Large Data Feed sample code project
defines to store earthquake data, sorted by their `time` property:

Alternatively, when you need more flexibility, you can initialize the request
with a configured `NSFetchRequest` instance:

Always declare properties that have a fetch request wrapper as private. This
lets the compiler help you avoid accidentally setting the property from the
memberwise initializer of the enclosing view.

The fetch request and its results use the managed object context stored in the
environment, which you can access using the `managedObjectContext` environment
value. To support user interface activity, you typically rely on the
`viewContext` property of a shared `NSPersistentContainer` instance. For
example, you can set a context on your top level content view using a shared
container that you define as part of your model:

When you need to dynamically change the predicate or sort descriptors, access
the request’s `FetchRequest.Configuration` structure. To create a request that
groups the fetched results according to a characteristic that they share, use
`SectionedFetchRequest` instead.

## Topics

### Creating a fetch request

`init(sortDescriptors: [SortDescriptor<Result>], predicate: NSPredicate?,
animation: Animation?)`

Creates a fetch request based on a predicate and value type sort parameters.

Available when `Result` inherits `NSManagedObject`.

`init(sortDescriptors: [NSSortDescriptor], predicate: NSPredicate?, animation:
Animation?)`

Creates a fetch request based on a predicate and reference type sort
parameters.

Available when `Result` inherits `NSManagedObject`.

`init(entity: NSEntityDescription, sortDescriptors: [NSSortDescriptor],
predicate: NSPredicate?, animation: Animation?)`

Creates a fetch request for a specified entity description, based on a
predicate and sort parameters.

Available when `Result` conforms to `NSFetchRequestResult`.

### Creating a fully configured fetch request

`init(fetchRequest: NSFetchRequest<Result>, animation: Animation?)`

Creates a fully configured fetch request that uses the specified animation
when updating results.

Available when `Result` conforms to `NSFetchRequestResult`.

`init(fetchRequest: NSFetchRequest<Result>, transaction: Transaction)`

Creates a fully configured fetch request that uses the specified transaction
when updating results.

Available when `Result` conforms to `NSFetchRequestResult`.

### Configuring a request dynamically

`struct Configuration`

The request’s configurable properties.

`var projectedValue: Binding<FetchRequest<Result>.Configuration>`

A binding to the request’s mutable configuration properties.

### Getting the fetched results

`func update()`

Updates the fetched results.

Available when `Result` conforms to `NSFetchRequestResult`.

`var wrappedValue: FetchedResults<Result>`

The fetched results of the fetch request.

### Default Implementations

API Reference

DynamicProperty Implementations

## Relationships

### Conforms To

  * `DynamicProperty`

Conforms when `Result` conforms to `NSFetchRequestResult`.

## See Also

### Accessing Core Data

Loading and Displaying a Large Data Feed

Consume data in the background, and lower memory use by batching imports and
preventing duplicate records.

`var managedObjectContext: NSManagedObjectContext`

`struct FetchedResults`

A collection of results retrieved from a Core Data store.

`struct SectionedFetchRequest`

A property wrapper type that retrieves entities, grouped into sections, from a
Core Data persistent store.

`struct SectionedFetchResults`

A collection of results retrieved from a Core Data persistent store, grouped
into sections.

Structure

# FetchedResults

A collection of results retrieved from a Core Data store.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    struct FetchedResults<Result> where Result : NSFetchRequestResult

## Overview

Use a `FetchedResults` instance to show or edit Core Data managed objects in
your app’s user interface. You request a particular set of results by
specifying a `Result` type as the entity type, and annotating the fetched
results property declaration with a `FetchRequest` property wrapper. For
example, you can create a request to list all `Quake` managed objects that the
Loading and Displaying a Large Data Feed sample code project defines to store
earthquake data, sorted by their `time` property:

The results instance conforms to `RandomAccessCollection`, so you access it
like any other collection. For example, you can create a `List` that iterates
over all the results:

When you need to dynamically change the request’s predicate or sort
descriptors, set the result instance’s `nsPredicate` and `sortDescriptors` or
`nsSortDescriptors` properties, respectively.

The fetch request and its results use the managed object context stored in the
environment, which you can access using the `managedObjectContext` environment
value. To support user interface activity, you typically rely on the
`viewContext` property of a shared `NSPersistentContainer` instance. For
example, you can set a context on your top level content view using a
container that you define as part of your model:

## Topics

### Configuring the associated fetch request

`var nsPredicate: NSPredicate?`

The request’s predicate.

`var sortDescriptors: [SortDescriptor<Result>]`

The request’s sort descriptors, accessed as value types.

Available when `Result` inherits `NSManagedObject`.

`var nsSortDescriptors: [NSSortDescriptor]`

The request’s sort descriptors, accessed as reference types.

### Getting indices

`var startIndex: Int`

The index of the first entity in the results collection.

`var endIndex: Int`

The index that’s one greater than the last valid subscript argument.

### Getting results

`subscript(Int) -> Result`

Gets the entity at the specified index.

## Relationships

### Conforms To

  * `BidirectionalCollection`
  * `Collection`
  * `RandomAccessCollection`
  * `Sequence`

## See Also

### Accessing Core Data

Loading and Displaying a Large Data Feed

Consume data in the background, and lower memory use by batching imports and
preventing duplicate records.

`var managedObjectContext: NSManagedObjectContext`

`struct FetchRequest`

A property wrapper type that retrieves entities from a Core Data persistent
store.

`struct SectionedFetchRequest`

A property wrapper type that retrieves entities, grouped into sections, from a
Core Data persistent store.

`struct SectionedFetchResults`

A collection of results retrieved from a Core Data persistent store, grouped
into sections.

Structure

# SectionedFetchRequest

A property wrapper type that retrieves entities, grouped into sections, from a
Core Data persistent store.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    @MainActor @propertyWrapper
    struct SectionedFetchRequest<SectionIdentifier, Result> where SectionIdentifier : Hashable, Result : NSFetchRequestResult

## Overview

Use a `SectionedFetchRequest` property wrapper to declare a
`SectionedFetchResults` property that provides a grouped collection of Core
Data managed objects to a SwiftUI view. If you don’t need sectioning, use
`FetchRequest` instead.

Configure a sectioned fetch request with an optional predicate and sort
descriptors, and include a `sectionIdentifier` parameter to indicate how to
group the fetched results. Be sure that you choose sorting and sectioning that
work together to avoid discontiguous sections. For example, you can request a
list of earthquakes, composed of `Quake` managed objects that the Loading and
Displaying a Large Data Feed sample code project defines to store earthquake
data, sorted by time and grouped by date:

Always declare properties that have a sectioned fetch request wrapper as
private. This lets the compiler help you avoid accidentally setting the
property from the memberwise initializer of the enclosing view.

The request infers the entity type from the `Result` type that you specify,
which is `Quake` in the example above. Indicate a `SectionIdentifier` type to
declare the type found at the fetched object’s `sectionIdentifier` key path.
The section identifier type must conform to the `Hashable` protocol.

The example above depends on the `Quake` type having a `day` property that’s
either a stored or computed string. Be sure to mark any computed property with
the `@objc` attribute for it to function as a section identifier. For best
performance with large data sets, use stored properties.

The sectioned fetch request and its results use the managed object context
stored in the environment, which you can access using the
`managedObjectContext` environment value. To support user interface activity,
you typically rely on the `viewContext` property of a shared
`NSPersistentContainer` instance. For example, you can set a context on your
top-level content view using a shared container that you define as part of
your model:

When you need to dynamically change the section identifier, predicate, or sort
descriptors, access the request’s `SectionedFetchRequest.Configuration`
structure, either directly or with a binding.

## Topics

### Creating a fetch request

`init(sectionIdentifier: KeyPath<Result, SectionIdentifier>, sortDescriptors:
[SortDescriptor<Result>], predicate: NSPredicate?, animation: Animation?)`

Creates a sectioned fetch request based on a section identifier, a predicate,
and value type sort parameters.

Available when `SectionIdentifier` conforms to `Hashable` and `Result`
inherits `NSManagedObject`.

`init(sectionIdentifier: KeyPath<Result, SectionIdentifier>, sortDescriptors:
[NSSortDescriptor], predicate: NSPredicate?, animation: Animation?)`

Creates a sectioned fetch request based on a section identifier, a predicate,
and reference type sort parameters.

Available when `SectionIdentifier` conforms to `Hashable` and `Result`
inherits `NSManagedObject`.

`init(entity: NSEntityDescription, sectionIdentifier: KeyPath<Result,
SectionIdentifier>, sortDescriptors: [NSSortDescriptor], predicate:
NSPredicate?, animation: Animation?)`

Creates a sectioned fetch request for a specified entity description, based on
a section identifier, a predicate, and sort parameters.

Available when `SectionIdentifier` conforms to `Hashable` and `Result`
conforms to `NSFetchRequestResult`.

### Creating a fully configured fetch request

`init(fetchRequest: NSFetchRequest<Result>, sectionIdentifier: KeyPath<Result,
SectionIdentifier>, animation: Animation?)`

Creates a fully configured sectioned fetch request that uses the specified
animation when updating results.

Available when `SectionIdentifier` conforms to `Hashable` and `Result`
conforms to `NSFetchRequestResult`.

`init(fetchRequest: NSFetchRequest<Result>, sectionIdentifier: KeyPath<Result,
SectionIdentifier>, transaction: Transaction)`

Creates a fully configured sectioned fetch request that uses the specified
transaction when updating results.

Available when `SectionIdentifier` conforms to `Hashable` and `Result`
conforms to `NSFetchRequestResult`.

### Configuring a request dynamically

`struct Configuration`

The request’s configurable properties.

`var projectedValue: Binding<SectionedFetchRequest<SectionIdentifier,
Result>.Configuration>`

A binding to the request’s mutable configuration properties.

### Getting the fetched results

`func update()`

Updates the fetched results.

Available when `SectionIdentifier` conforms to `Hashable` and `Result`
conforms to `NSFetchRequestResult`.

`var wrappedValue: SectionedFetchResults<SectionIdentifier, Result>`

The fetched results of the fetch request.

### Default Implementations

API Reference

DynamicProperty Implementations

## Relationships

### Conforms To

  * `DynamicProperty`

Conforms when `SectionIdentifier` conforms to `Hashable` and `Result` conforms
to `NSFetchRequestResult`.

## See Also

### Accessing Core Data

Loading and Displaying a Large Data Feed

Consume data in the background, and lower memory use by batching imports and
preventing duplicate records.

`var managedObjectContext: NSManagedObjectContext`

`struct FetchRequest`

A property wrapper type that retrieves entities from a Core Data persistent
store.

`struct FetchedResults`

A collection of results retrieved from a Core Data store.

`struct SectionedFetchResults`

A collection of results retrieved from a Core Data persistent store, grouped
into sections.

Structure

# SectionedFetchResults

A collection of results retrieved from a Core Data persistent store, grouped
into sections.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    struct SectionedFetchResults<SectionIdentifier, Result> where SectionIdentifier : Hashable, Result : NSFetchRequestResult

## Overview

Use a `SectionedFetchResults` instance to show or edit Core Data managed
objects, grouped into sections, in your app’s user interface. If you don’t
need sectioning, use `FetchedResults` instead.

You request a particular set of results by annotating the fetched results
property declaration with a `SectionedFetchRequest` property wrapper. Indicate
the type of the fetched entities with a `Results` type, and the type of the
identifier that distinguishes the sections with a `SectionIdentifier` type.
For example, you can create a request to list all `Quake` managed objects that
the Loading and Displaying a Large Data Feed sample code project defines to
store earthquake data, sorted by their `time` property and grouped by a string
that represents the days when earthquakes occurred:

The `quakes` property acts as a collection of `SectionedFetchResults.Section`
instances, each containing a collection of `Quake` instances. The example
above depends on the `Quake` model object declaring both `time` and `day`
properties, either stored or computed. For best performance with large data
sets, use stored properties.

The collection of sections, as well as the collection of managed objects in
each section, conforms to the `RandomAccessCollection` protocol, so you can
access them as you would any other collection. For example, you can create
nested `ForEach` loops inside a `List` to iterate over the results:

Don’t confuse the `Section` view that you use to create a hierarchical display
with the `SectionedFetchResults.Section` instances that hold the fetched
results.

When you need to dynamically change the request’s section identifier,
predicate, or sort descriptors, set the result instance’s `sectionIdentifier`,
`nsPredicate`, and `sortDescriptors` or `nsSortDescriptors` properties,
respectively. Be sure that the sorting and sectioning work together to avoid
discontinguous sections.

The fetch request and its results use the managed object context stored in the
environment, which you can access using the `managedObjectContext` environment
value. To support user interface activity, you typically rely on the
`viewContext` property of a shared `NSPersistentContainer` instance. For
example, you can set a context on your top-level content view using a
container that you define as part of your model:

## Topics

### Configuring the associated sectioned fetch request

`var nsPredicate: NSPredicate?`

The request’s predicate.

`var sortDescriptors: [SortDescriptor<Result>]`

The request’s sort descriptors, accessed as value types.

Available when `SectionIdentifier` conforms to `Hashable` and `Result`
inherits `NSManagedObject`.

`var nsSortDescriptors: [NSSortDescriptor]`

The request’s sort descriptors, accessed as reference types.

`var sectionIdentifier: KeyPath<Result, SectionIdentifier>`

The key path that the system uses to group fetched results into sections.

`struct Section`

A collection of fetched results that share a specified identifier.

### Getting indices

`var startIndex: Int`

The index of the first section in the results collection.

`var endIndex: Int`

The index that’s one greater than that of the last section.

### Getting results

`subscript(Int) -> SectionedFetchResults<SectionIdentifier, Result>.Section`

Gets the section at the specified index.

## Relationships

### Conforms To

  * `BidirectionalCollection`
  * `Collection`
  * `RandomAccessCollection`
  * `Sequence`

## See Also

### Accessing Core Data

Loading and Displaying a Large Data Feed

Consume data in the background, and lower memory use by batching imports and
preventing duplicate records.

`var managedObjectContext: NSManagedObjectContext`

`struct FetchRequest`

A property wrapper type that retrieves entities from a Core Data persistent
store.

`struct FetchedResults`

A collection of results retrieved from a Core Data store.

`struct SectionedFetchRequest`

A property wrapper type that retrieves entities, grouped into sections, from a
Core Data persistent store.



# PresentationDetent.Context

Instance Property

# maxDetentValue

The height that the presentation appears in.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var maxDetentValue: CGFloat { get }

Instance Subscript

# subscript(dynamicMember:)

Returns the value specified by the keyPath from the environment.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    subscript<T>(dynamicMember keyPath: KeyPath<EnvironmentValues, T>) -> T { get }

## Overview

This uses the environment from where the sheet is shown, not the environment
where the presentation modifier is applied.



# ProgressView

Initializer

# init()

Creates a progress view for showing indeterminate progress, without a label.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init() where Label == EmptyView

Available when `Label` conforms to `View` and `CurrentValueLabel` is
`EmptyView`.

## See Also

### Creating an indeterminate progress view

`init(label: () -> Label)`

Creates a progress view for showing indeterminate progress that displays a
custom label.

Available when `Label` conforms to `View` and `CurrentValueLabel` is
`EmptyView`.

`init(LocalizedStringKey)`

Creates a progress view for showing indeterminate progress that generates its
label from a localized string.

Available when `Label` conforms to `View` and `CurrentValueLabel` is
`EmptyView`.

`init<S>(S)`

Creates a progress view for showing indeterminate progress that generates its
label from a string.

Available when `Label` conforms to `View` and `CurrentValueLabel` is
`EmptyView`.

Initializer

# init(label:)

Creates a progress view for showing indeterminate progress that displays a
custom label.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(@ViewBuilder label: () -> Label)

Available when `Label` conforms to `View` and `CurrentValueLabel` is
`EmptyView`.

##  Parameters

`label`

    

A view builder that creates a view that describes the task in progress.

## See Also

### Creating an indeterminate progress view

`init()`

Creates a progress view for showing indeterminate progress, without a label.

Available when `Label` conforms to `View` and `CurrentValueLabel` is
`EmptyView`.

`init(LocalizedStringKey)`

Creates a progress view for showing indeterminate progress that generates its
label from a localized string.

Available when `Label` conforms to `View` and `CurrentValueLabel` is
`EmptyView`.

`init<S>(S)`

Creates a progress view for showing indeterminate progress that generates its
label from a string.

Available when `Label` conforms to `View` and `CurrentValueLabel` is
`EmptyView`.

Initializer

# init(_:)

Creates a progress view for showing indeterminate progress that generates its
label from a localized string.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(_ titleKey: LocalizedStringKey) where Label == Text

Available when `Label` conforms to `View` and `CurrentValueLabel` is
`EmptyView`.

##  Parameters

`titleKey`

    

The key for the progress view’s localized title that describes the task in
progress.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings. To initialize a indeterminate
progress view with a string variable, use the corresponding initializer that
takes a `StringProtocol` instance.

## See Also

### Creating an indeterminate progress view

`init()`

Creates a progress view for showing indeterminate progress, without a label.

Available when `Label` conforms to `View` and `CurrentValueLabel` is
`EmptyView`.

`init(label: () -> Label)`

Creates a progress view for showing indeterminate progress that displays a
custom label.

Available when `Label` conforms to `View` and `CurrentValueLabel` is
`EmptyView`.

`init<S>(S)`

Creates a progress view for showing indeterminate progress that generates its
label from a string.

Available when `Label` conforms to `View` and `CurrentValueLabel` is
`EmptyView`.

Initializer

# init(_:)

Creates a progress view for showing indeterminate progress that generates its
label from a string.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init<S>(_ title: S) where Label == Text, S : StringProtocol

Available when `Label` conforms to `View` and `CurrentValueLabel` is
`EmptyView`.

##  Parameters

`title`

    

A string that describes the task in progress.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the title
similar to `init(verbatim:)`. See `Text` for more information about localizing
strings. To initialize a progress view with a localized string key, use the
corresponding initializer that takes a `LocalizedStringKey` instance.

## See Also

### Creating an indeterminate progress view

`init()`

Creates a progress view for showing indeterminate progress, without a label.

Available when `Label` conforms to `View` and `CurrentValueLabel` is
`EmptyView`.

`init(label: () -> Label)`

Creates a progress view for showing indeterminate progress that displays a
custom label.

Available when `Label` conforms to `View` and `CurrentValueLabel` is
`EmptyView`.

`init(LocalizedStringKey)`

Creates a progress view for showing indeterminate progress that generates its
label from a localized string.

Available when `Label` conforms to `View` and `CurrentValueLabel` is
`EmptyView`.

Initializer

# init(_:)

Creates a progress view for visualizing the given progress instance.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(_ progress: Progress) where Label == EmptyView, CurrentValueLabel == EmptyView

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

## Discussion

The progress view synthesizes a default label using the `localizedDescription`
of the given progress instance.

## See Also

### Creating a determinate progress view

`init<V>(value: V?, total: V)`

Creates a progress view for showing determinate progress.

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

`init<V>(LocalizedStringKey, value: V?, total: V)`

Creates a progress view for showing determinate progress that generates its
label from a localized string.

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

`init<S, V>(S, value: V?, total: V)`

Creates a progress view for showing determinate progress that generates its
label from a string.

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

`init<V>(value: V?, total: V, label: () -> Label)`

Creates a progress view for showing determinate progress, with a custom label.

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

`init<V>(value: V?, total: V, label: () -> Label, currentValueLabel: () ->
CurrentValueLabel)`

Creates a progress view for showing determinate progress, with a custom label.

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

Initializer

# init(value:total:)

Creates a progress view for showing determinate progress.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init<V>(
        value: V?,
        total: V = 1.0
    ) where Label == EmptyView, CurrentValueLabel == EmptyView, V : BinaryFloatingPoint

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

##  Parameters

`value`

    

The completed amount of the task to this point, in a range of `0.0` to
`total`, or `nil` if the progress is indeterminate.

`total`

    

The full amount representing the complete scope of the task, meaning the task
is complete if `value` equals `total`. The default value is `1.0`.

## Discussion

If the value is non-`nil`, but outside the range of `0.0` through `total`, the
progress view pins the value to those limits, rounding to the nearest possible
bound. A value of `nil` represents indeterminate progress, in which case the
progress view ignores `total`.

## See Also

### Creating a determinate progress view

`init(Progress)`

Creates a progress view for visualizing the given progress instance.

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

`init<V>(LocalizedStringKey, value: V?, total: V)`

Creates a progress view for showing determinate progress that generates its
label from a localized string.

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

`init<S, V>(S, value: V?, total: V)`

Creates a progress view for showing determinate progress that generates its
label from a string.

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

`init<V>(value: V?, total: V, label: () -> Label)`

Creates a progress view for showing determinate progress, with a custom label.

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

`init<V>(value: V?, total: V, label: () -> Label, currentValueLabel: () ->
CurrentValueLabel)`

Creates a progress view for showing determinate progress, with a custom label.

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

Initializer

# init(_:value:total:)

Creates a progress view for showing determinate progress that generates its
label from a localized string.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init<V>(
        _ titleKey: LocalizedStringKey,
        value: V?,
        total: V = 1.0
    ) where Label == Text, CurrentValueLabel == EmptyView, V : BinaryFloatingPoint

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

##  Parameters

`titleKey`

    

The key for the progress view’s localized title that describes the task in
progress.

`value`

    

The completed amount of the task to this point, in a range of `0.0` to
`total`, or `nil` if the progress is indeterminate.

`total`

    

The full amount representing the complete scope of the task, meaning the task
is complete if `value` equals `total`. The default value is `1.0`.

## Discussion

If the value is non-`nil`, but outside the range of `0.0` through `total`, the
progress view pins the value to those limits, rounding to the nearest possible
bound. A value of `nil` represents indeterminate progress, in which case the
progress view ignores `total`.

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings. To initialize a determinate
progress view with a string variable, use the corresponding initializer that
takes a `StringProtocol` instance.

## See Also

### Creating a determinate progress view

`init(Progress)`

Creates a progress view for visualizing the given progress instance.

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

`init<V>(value: V?, total: V)`

Creates a progress view for showing determinate progress.

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

`init<S, V>(S, value: V?, total: V)`

Creates a progress view for showing determinate progress that generates its
label from a string.

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

`init<V>(value: V?, total: V, label: () -> Label)`

Creates a progress view for showing determinate progress, with a custom label.

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

`init<V>(value: V?, total: V, label: () -> Label, currentValueLabel: () ->
CurrentValueLabel)`

Creates a progress view for showing determinate progress, with a custom label.

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

Initializer

# init(_:value:total:)

Creates a progress view for showing determinate progress that generates its
label from a string.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init<S, V>(
        _ title: S,
        value: V?,
        total: V = 1.0
    ) where Label == Text, CurrentValueLabel == EmptyView, S : StringProtocol, V : BinaryFloatingPoint

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

##  Parameters

`title`

    

The string that describes the task in progress.

`value`

    

The completed amount of the task to this point, in a range of `0.0` to
`total`, or `nil` if the progress is indeterminate.

`total`

    

The full amount representing the complete scope of the task, meaning the task
is complete if `value` equals `total`. The default value is `1.0`.

## Discussion

If the value is non-`nil`, but outside the range of `0.0` through `total`, the
progress view pins the value to those limits, rounding to the nearest possible
bound. A value of `nil` represents indeterminate progress, in which case the
progress view ignores `total`.

This initializer creates a `Text` view on your behalf, and treats the title
similar to `init(verbatim:)`. See `Text` for more information about localizing
strings. To initialize a determinate progress view with a localized string
key, use the corresponding initializer that takes a `LocalizedStringKey`
instance.

## See Also

### Creating a determinate progress view

`init(Progress)`

Creates a progress view for visualizing the given progress instance.

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

`init<V>(value: V?, total: V)`

Creates a progress view for showing determinate progress.

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

`init<V>(LocalizedStringKey, value: V?, total: V)`

Creates a progress view for showing determinate progress that generates its
label from a localized string.

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

`init<V>(value: V?, total: V, label: () -> Label)`

Creates a progress view for showing determinate progress, with a custom label.

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

`init<V>(value: V?, total: V, label: () -> Label, currentValueLabel: () ->
CurrentValueLabel)`

Creates a progress view for showing determinate progress, with a custom label.

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

Initializer

# init(value:total:label:)

Creates a progress view for showing determinate progress, with a custom label.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init<V>(
        value: V?,
        total: V = 1.0,
        @ViewBuilder label: () -> Label
    ) where CurrentValueLabel == EmptyView, V : BinaryFloatingPoint

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

##  Parameters

`value`

    

The completed amount of the task to this point, in a range of `0.0` to
`total`, or `nil` if the progress is indeterminate.

`total`

    

The full amount representing the complete scope of the task, meaning the task
is complete if `value` equals `total`. The default value is `1.0`.

`label`

    

A view builder that creates a view that describes the task in progress.

## Discussion

If the value is non-`nil`, but outside the range of `0.0` through `total`, the
progress view pins the value to those limits, rounding to the nearest possible
bound. A value of `nil` represents indeterminate progress, in which case the
progress view ignores `total`.

## See Also

### Creating a determinate progress view

`init(Progress)`

Creates a progress view for visualizing the given progress instance.

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

`init<V>(value: V?, total: V)`

Creates a progress view for showing determinate progress.

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

`init<V>(LocalizedStringKey, value: V?, total: V)`

Creates a progress view for showing determinate progress that generates its
label from a localized string.

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

`init<S, V>(S, value: V?, total: V)`

Creates a progress view for showing determinate progress that generates its
label from a string.

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

`init<V>(value: V?, total: V, label: () -> Label, currentValueLabel: () ->
CurrentValueLabel)`

Creates a progress view for showing determinate progress, with a custom label.

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

Initializer

# init(value:total:label:currentValueLabel:)

Creates a progress view for showing determinate progress, with a custom label.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init<V>(
        value: V?,
        total: V = 1.0,
        @ViewBuilder label: () -> Label,
        @ViewBuilder currentValueLabel: () -> CurrentValueLabel
    ) where V : BinaryFloatingPoint

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

##  Parameters

`value`

    

The completed amount of the task to this point, in a range of `0.0` to
`total`, or `nil` if the progress is indeterminate.

`total`

    

The full amount representing the complete scope of the task, meaning the task
is complete if `value` equals `total`. The default value is `1.0`.

`label`

    

A view builder that creates a view that describes the task in progress.

`currentValueLabel`

    

A view builder that creates a view that describes the level of completed
progress of the task.

## Discussion

If the value is non-`nil`, but outside the range of `0.0` through `total`, the
progress view pins the value to those limits, rounding to the nearest possible
bound. A value of `nil` represents indeterminate progress, in which case the
progress view ignores `total`.

## See Also

### Creating a determinate progress view

`init(Progress)`

Creates a progress view for visualizing the given progress instance.

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

`init<V>(value: V?, total: V)`

Creates a progress view for showing determinate progress.

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

`init<V>(LocalizedStringKey, value: V?, total: V)`

Creates a progress view for showing determinate progress that generates its
label from a localized string.

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

`init<S, V>(S, value: V?, total: V)`

Creates a progress view for showing determinate progress that generates its
label from a string.

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

`init<V>(value: V?, total: V, label: () -> Label)`

Creates a progress view for showing determinate progress, with a custom label.

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

Initializer

# init(timerInterval:countsDown:)

Creates a progress view for showing continuous progress as time passes.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init(
        timerInterval: ClosedRange<Date>,
        countsDown: Bool = true
    )

Available when `Label` is `EmptyView` and `CurrentValueLabel` is
`DefaultDateProgressLabel`.

##  Parameters

`timerInterval`

    

The date range over which the view progresses.

`countsDown`

    

If `true` (the default), the view empties as time passes.

## Discussion

Use this initializer to create a view that shows continuous progress within a
date range. The following example initializes a progress view with a range of
`start...end`, where `start` is 30 seconds in the past and `end` is 90 seconds
in the future. As a result, the progress view begins at 25 percent complete.

By default, the progress view empties as time passes from the start of the
date range to the end, but you can use the `countsDown` parameter to create a
progress view that fills as time passes, as the above example demonstrates.

The progress view provided by this initializer omits a descriptive label and
provides a text label that automatically updates to describe the current time
remaining. To provide custom views for these labels, use
`init(value:total:label:currentValueLabel:)` instead.

Note

Date-relative progress views, such as those created with this initializer,
don’t support custom styles.

## See Also

### Create a progress view spanning a date range

`init(timerInterval: ClosedRange<Date>, countsDown: Bool, label: () -> Label)`

Creates a progress view for showing continuous progress as time passes, with a
descriptive label.

Available when `Label` conforms to `View` and `CurrentValueLabel` is
`DefaultDateProgressLabel`.

`init(timerInterval: ClosedRange<Date>, countsDown: Bool, label: () -> Label,
currentValueLabel: () -> CurrentValueLabel)`

Creates a progress view for showing continuous progress as time passes, with
descriptive and current progress labels.

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

Initializer

# init(timerInterval:countsDown:label:)

Creates a progress view for showing continuous progress as time passes, with a
descriptive label.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init(
        timerInterval: ClosedRange<Date>,
        countsDown: Bool = true,
        @ViewBuilder label: () -> Label
    )

Available when `Label` conforms to `View` and `CurrentValueLabel` is
`DefaultDateProgressLabel`.

##  Parameters

`timerInterval`

    

The date range over which the view progresses.

`countsDown`

    

A Boolean value that determines whether the view empties or fills as time
passes. If `true` (the default), the view empties.

`label`

    

An optional view that describes the purpose of the progress view.

## Discussion

Use this initializer to create a view that shows continuous progress within a
date range. The following example initializes a progress view with a range of
`start...end`, where `start` is 30 seconds in the past and `end` is 90 seconds
in the future. As a result, the progress view begins at 25 percent complete.
This example also provides a custom descriptive label.

By default, the progress view empties as time passes from the start of the
date range to the end, but you can use the `countsDown` parameter to create a
progress view that fills as time passes, as the above example demonstrates.

The progress view provided by this initializer uses a text label that
automatically updates to describe the current time remaining. To provide a
custom label to show the current value, use
`init(value:total:label:currentValueLabel:)` instead.

Note

Date-relative progress views, such as those created with this initializer,
don’t support custom styles.

## See Also

### Create a progress view spanning a date range

`init(timerInterval: ClosedRange<Date>, countsDown: Bool)`

Creates a progress view for showing continuous progress as time passes.

Available when `Label` is `EmptyView` and `CurrentValueLabel` is
`DefaultDateProgressLabel`.

`init(timerInterval: ClosedRange<Date>, countsDown: Bool, label: () -> Label,
currentValueLabel: () -> CurrentValueLabel)`

Creates a progress view for showing continuous progress as time passes, with
descriptive and current progress labels.

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

Initializer

# init(timerInterval:countsDown:label:currentValueLabel:)

Creates a progress view for showing continuous progress as time passes, with
descriptive and current progress labels.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init(
        timerInterval: ClosedRange<Date>,
        countsDown: Bool = true,
        @ViewBuilder label: () -> Label,
        @ViewBuilder currentValueLabel: () -> CurrentValueLabel
    )

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

##  Parameters

`timerInterval`

    

The date range over which the view should progress.

`countsDown`

    

A Boolean value that determines whether the view empties or fills as time
passes. If `true` (the default), the view empties.

`label`

    

An optional view that describes the purpose of the progress view.

`currentValueLabel`

    

A view that displays the current value of the timer.

## Discussion

Use this initializer to create a view that shows continuous progress within a
date range. The following example initializes a progress view with a range of
`start...end`, where `start` is 30 seconds in the past and `end` is 90 seconds
in the future. As a result, the progress view begins at 25 percent complete.
This example also provides custom views for a descriptive label (Progress) and
a current value label that shows the date range.

By default, the progress view empties as time passes from the start of the
date range to the end, but you can use the `countsDown` parameter to create a
progress view that fills as time passes, as the above example demonstrates.

Note

Date-relative progress views, such as those created with this initializer,
don’t support custom styles.

## See Also

### Create a progress view spanning a date range

`init(timerInterval: ClosedRange<Date>, countsDown: Bool)`

Creates a progress view for showing continuous progress as time passes.

Available when `Label` is `EmptyView` and `CurrentValueLabel` is
`DefaultDateProgressLabel`.

`init(timerInterval: ClosedRange<Date>, countsDown: Bool, label: () -> Label)`

Creates a progress view for showing continuous progress as time passes, with a
descriptive label.

Available when `Label` conforms to `View` and `CurrentValueLabel` is
`DefaultDateProgressLabel`.

Initializer

# init(_:)

Creates a progress view based on a style configuration.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(_ configuration: ProgressViewStyleConfiguration) where Label == ProgressViewStyleConfiguration.Label, CurrentValueLabel == ProgressViewStyleConfiguration.CurrentValueLabel

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

## Discussion

You can use this initializer within the `makeBody(configuration:)` method of a
`ProgressViewStyle` to create an instance of the styled progress view. This is
useful for custom progress view styles that only modify the current progress
view style, as opposed to implementing a brand new style. Because this
modifier style can’t know how the current style represents progress, avoid
making assumptions about the view’s contents, such as whether it uses bars or
other shapes.

The following example shows a style that adds a rounded pink border to a
progress view, but otherwise preserves the progress view’s current style:

Note

Progress views in widgets don’t apply custom styles.



# PrimitiveButtonStyleConfiguration

Instance Property

# label

A view that describes the effect of calling the button’s action.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    let label: PrimitiveButtonStyleConfiguration.Label

## See Also

### Configuring a button’s label

`struct Label`

A type-erased label of a button.

Structure

# PrimitiveButtonStyleConfiguration.Label

A type-erased label of a button.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    struct Label

## Relationships

### Conforms To

  * `View`

## See Also

### Configuring a button’s label

`let label: PrimitiveButtonStyleConfiguration.Label`

A view that describes the effect of calling the button’s action.

Instance Method

# trigger()

Performs the button’s action.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func trigger()

Instance Property

# role

An optional semantic role describing the button’s purpose.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    let role: ButtonRole?

## Discussion

A value of `nil` means that the Button has no assigned role. If the button
does have a role, use it to make adjustments to the button’s appearance. The
following example shows a custom style that uses bold text when the role is
`cancel`, `red` text when the role is `destructive`, and adds no special
styling otherwise:

You can create one of each button using this style to see the effect:



# PagingScrollTargetBehavior

Initializer

# init()

Creates a paging scroll behavior.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init()



# ProgressiveImmersionStyle

Initializer

# init()

visionOS 1.0+

    
    
    init()



# PageTabViewStyle

Initializer

# init(indexDisplayMode:)

Creates a new `PageTabViewStyle` with an index display mode

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS 7.0+
visionOS 1.0+

    
    
    init(indexDisplayMode: PageTabViewStyle.IndexDisplayMode = .automatic)

## See Also

### Creating a page tab view style

`struct IndexDisplayMode`

A style for displaying the page index view

Structure

# PageTabViewStyle.IndexDisplayMode

A style for displaying the page index view

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS 7.0+
visionOS 1.0+

    
    
    struct IndexDisplayMode

## Topics

### Getting the modes

`static let always: PageTabViewStyle.IndexDisplayMode`

Always display an index view regardless of page count

`static let automatic: PageTabViewStyle.IndexDisplayMode`

Displays an index view when there are more than one page

`static let never: PageTabViewStyle.IndexDisplayMode`

Never display an index view

## Relationships

### Conforms To

  * `Sendable`

## See Also

### Creating a page tab view style

`init(indexDisplayMode: PageTabViewStyle.IndexDisplayMode)`

Creates a new `PageTabViewStyle` with an index display mode



# PinnedScrollableViews

Type Property

# sectionHeaders

The header view of each `Section` will be pinned.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    static let sectionHeaders: PinnedScrollableViews

## See Also

### Getting scrollable view types

`static let sectionFooters: PinnedScrollableViews`

The footer view of each `Section` will be pinned.

Type Property

# sectionFooters

The footer view of each `Section` will be pinned.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    static let sectionFooters: PinnedScrollableViews

## See Also

### Getting scrollable view types

`static let sectionHeaders: PinnedScrollableViews`

The header view of each `Section` will be pinned.



# PhysicalMetric

Initializer

# init(wrappedValue:from:)

Creates a value that maps the specified set of physical length measurements,
in the specified unit, to a corresponding set of values measured in points in
the associated scene.

visionOS 1.0+

    
    
    init(
        wrappedValue value: Value,
        from unit: UnitLength
    ) where Value : VectorArithmetic

## See Also

### Creating a metric

`init(wrappedValue: CGPoint, from: UnitLength)`

Creates a value that maps the specified point, whose dimensions are specified
in physical length measurements in the given unit, to the corresponding value
in points in the associated scene.

`init(wrappedValue: CGSize, from: UnitLength)`

Creates a value that maps the specified size, in the specified unit to the
corresponding value in points in the associated scene.

`init(wrappedValue: Size3D, from: UnitLength)`

Creates a value that maps the specified size, in the specified unit to the
corresponding value in points in the associated scene.

`init(wrappedValue: Point3D, from: UnitLength)`

Creates a value that maps the specified point, whose dimensions are specified
in physical length measurements in the given unit, to the corresponding value
in points in the associated scene.

`init(wrappedValue: Value, from: UnitLength)`

Creates a value that maps the specified single physical length measurement, in
the specified unit, to the corresponding value in points in the associated
scene.

`init(wrappedValue: CGRect, from: UnitLength)`

Creates a value that maps the specified rectangle, whose dimensions are
specified in physical length measurements in the given unit, to the
corresponding value in points in the associated scene.

`init(wrappedValue: Rect3D, from: UnitLength)`

Creates a value that maps the specified `Rect3D`, whose dimensions are
specified in physical length measurements in the given unit, to the
corresponding value in points in the associated scene.

Initializer

# init(wrappedValue:from:)

Creates a value that maps the specified point, whose dimensions are specified
in physical length measurements in the given unit, to the corresponding value
in points in the associated scene.

visionOS 1.0+

    
    
    init(
        wrappedValue point: CGPoint,
        from unit: UnitLength
    ) where Value == CGPoint

## See Also

### Creating a metric

`init(wrappedValue: Value, from: UnitLength)`

Creates a value that maps the specified set of physical length measurements,
in the specified unit, to a corresponding set of values measured in points in
the associated scene.

`init(wrappedValue: CGSize, from: UnitLength)`

Creates a value that maps the specified size, in the specified unit to the
corresponding value in points in the associated scene.

`init(wrappedValue: Size3D, from: UnitLength)`

Creates a value that maps the specified size, in the specified unit to the
corresponding value in points in the associated scene.

`init(wrappedValue: Point3D, from: UnitLength)`

Creates a value that maps the specified point, whose dimensions are specified
in physical length measurements in the given unit, to the corresponding value
in points in the associated scene.

`init(wrappedValue: Value, from: UnitLength)`

Creates a value that maps the specified single physical length measurement, in
the specified unit, to the corresponding value in points in the associated
scene.

`init(wrappedValue: CGRect, from: UnitLength)`

Creates a value that maps the specified rectangle, whose dimensions are
specified in physical length measurements in the given unit, to the
corresponding value in points in the associated scene.

`init(wrappedValue: Rect3D, from: UnitLength)`

Creates a value that maps the specified `Rect3D`, whose dimensions are
specified in physical length measurements in the given unit, to the
corresponding value in points in the associated scene.

Initializer

# init(wrappedValue:from:)

Creates a value that maps the specified size, in the specified unit to the
corresponding value in points in the associated scene.

visionOS 1.0+

    
    
    init(
        wrappedValue size: CGSize,
        from unit: UnitLength
    ) where Value == CGSize

## See Also

### Creating a metric

`init(wrappedValue: Value, from: UnitLength)`

Creates a value that maps the specified set of physical length measurements,
in the specified unit, to a corresponding set of values measured in points in
the associated scene.

`init(wrappedValue: CGPoint, from: UnitLength)`

Creates a value that maps the specified point, whose dimensions are specified
in physical length measurements in the given unit, to the corresponding value
in points in the associated scene.

`init(wrappedValue: Size3D, from: UnitLength)`

Creates a value that maps the specified size, in the specified unit to the
corresponding value in points in the associated scene.

`init(wrappedValue: Point3D, from: UnitLength)`

Creates a value that maps the specified point, whose dimensions are specified
in physical length measurements in the given unit, to the corresponding value
in points in the associated scene.

`init(wrappedValue: Value, from: UnitLength)`

Creates a value that maps the specified single physical length measurement, in
the specified unit, to the corresponding value in points in the associated
scene.

`init(wrappedValue: CGRect, from: UnitLength)`

Creates a value that maps the specified rectangle, whose dimensions are
specified in physical length measurements in the given unit, to the
corresponding value in points in the associated scene.

`init(wrappedValue: Rect3D, from: UnitLength)`

Creates a value that maps the specified `Rect3D`, whose dimensions are
specified in physical length measurements in the given unit, to the
corresponding value in points in the associated scene.

Initializer

# init(wrappedValue:from:)

Creates a value that maps the specified size, in the specified unit to the
corresponding value in points in the associated scene.

visionOS 1.0+

    
    
    init(
        wrappedValue size: Size3D,
        from unit: UnitLength
    ) where Value == Size3D

## See Also

### Creating a metric

`init(wrappedValue: Value, from: UnitLength)`

Creates a value that maps the specified set of physical length measurements,
in the specified unit, to a corresponding set of values measured in points in
the associated scene.

`init(wrappedValue: CGPoint, from: UnitLength)`

Creates a value that maps the specified point, whose dimensions are specified
in physical length measurements in the given unit, to the corresponding value
in points in the associated scene.

`init(wrappedValue: CGSize, from: UnitLength)`

Creates a value that maps the specified size, in the specified unit to the
corresponding value in points in the associated scene.

`init(wrappedValue: Point3D, from: UnitLength)`

Creates a value that maps the specified point, whose dimensions are specified
in physical length measurements in the given unit, to the corresponding value
in points in the associated scene.

`init(wrappedValue: Value, from: UnitLength)`

Creates a value that maps the specified single physical length measurement, in
the specified unit, to the corresponding value in points in the associated
scene.

`init(wrappedValue: CGRect, from: UnitLength)`

Creates a value that maps the specified rectangle, whose dimensions are
specified in physical length measurements in the given unit, to the
corresponding value in points in the associated scene.

`init(wrappedValue: Rect3D, from: UnitLength)`

Creates a value that maps the specified `Rect3D`, whose dimensions are
specified in physical length measurements in the given unit, to the
corresponding value in points in the associated scene.

Initializer

# init(wrappedValue:from:)

Creates a value that maps the specified point, whose dimensions are specified
in physical length measurements in the given unit, to the corresponding value
in points in the associated scene.

visionOS 1.0+

    
    
    init(
        wrappedValue point: Point3D,
        from unit: UnitLength
    ) where Value == Point3D

## See Also

### Creating a metric

`init(wrappedValue: Value, from: UnitLength)`

Creates a value that maps the specified set of physical length measurements,
in the specified unit, to a corresponding set of values measured in points in
the associated scene.

`init(wrappedValue: CGPoint, from: UnitLength)`

Creates a value that maps the specified point, whose dimensions are specified
in physical length measurements in the given unit, to the corresponding value
in points in the associated scene.

`init(wrappedValue: CGSize, from: UnitLength)`

Creates a value that maps the specified size, in the specified unit to the
corresponding value in points in the associated scene.

`init(wrappedValue: Size3D, from: UnitLength)`

Creates a value that maps the specified size, in the specified unit to the
corresponding value in points in the associated scene.

`init(wrappedValue: Value, from: UnitLength)`

Creates a value that maps the specified single physical length measurement, in
the specified unit, to the corresponding value in points in the associated
scene.

`init(wrappedValue: CGRect, from: UnitLength)`

Creates a value that maps the specified rectangle, whose dimensions are
specified in physical length measurements in the given unit, to the
corresponding value in points in the associated scene.

`init(wrappedValue: Rect3D, from: UnitLength)`

Creates a value that maps the specified `Rect3D`, whose dimensions are
specified in physical length measurements in the given unit, to the
corresponding value in points in the associated scene.

Initializer

# init(wrappedValue:from:)

Creates a value that maps the specified single physical length measurement, in
the specified unit, to the corresponding value in points in the associated
scene.

visionOS 1.0+

    
    
    init(
        wrappedValue value: Value,
        from unit: UnitLength
    ) where Value == CGFloat

## See Also

### Creating a metric

`init(wrappedValue: Value, from: UnitLength)`

Creates a value that maps the specified set of physical length measurements,
in the specified unit, to a corresponding set of values measured in points in
the associated scene.

`init(wrappedValue: CGPoint, from: UnitLength)`

Creates a value that maps the specified point, whose dimensions are specified
in physical length measurements in the given unit, to the corresponding value
in points in the associated scene.

`init(wrappedValue: CGSize, from: UnitLength)`

Creates a value that maps the specified size, in the specified unit to the
corresponding value in points in the associated scene.

`init(wrappedValue: Size3D, from: UnitLength)`

Creates a value that maps the specified size, in the specified unit to the
corresponding value in points in the associated scene.

`init(wrappedValue: Point3D, from: UnitLength)`

Creates a value that maps the specified point, whose dimensions are specified
in physical length measurements in the given unit, to the corresponding value
in points in the associated scene.

`init(wrappedValue: CGRect, from: UnitLength)`

Creates a value that maps the specified rectangle, whose dimensions are
specified in physical length measurements in the given unit, to the
corresponding value in points in the associated scene.

`init(wrappedValue: Rect3D, from: UnitLength)`

Creates a value that maps the specified `Rect3D`, whose dimensions are
specified in physical length measurements in the given unit, to the
corresponding value in points in the associated scene.

Initializer

# init(wrappedValue:from:)

Creates a value that maps the specified rectangle, whose dimensions are
specified in physical length measurements in the given unit, to the
corresponding value in points in the associated scene.

visionOS 1.0+

    
    
    init(
        wrappedValue rect: CGRect,
        from unit: UnitLength
    ) where Value == CGRect

## See Also

### Creating a metric

`init(wrappedValue: Value, from: UnitLength)`

Creates a value that maps the specified set of physical length measurements,
in the specified unit, to a corresponding set of values measured in points in
the associated scene.

`init(wrappedValue: CGPoint, from: UnitLength)`

Creates a value that maps the specified point, whose dimensions are specified
in physical length measurements in the given unit, to the corresponding value
in points in the associated scene.

`init(wrappedValue: CGSize, from: UnitLength)`

Creates a value that maps the specified size, in the specified unit to the
corresponding value in points in the associated scene.

`init(wrappedValue: Size3D, from: UnitLength)`

Creates a value that maps the specified size, in the specified unit to the
corresponding value in points in the associated scene.

`init(wrappedValue: Point3D, from: UnitLength)`

Creates a value that maps the specified point, whose dimensions are specified
in physical length measurements in the given unit, to the corresponding value
in points in the associated scene.

`init(wrappedValue: Value, from: UnitLength)`

Creates a value that maps the specified single physical length measurement, in
the specified unit, to the corresponding value in points in the associated
scene.

`init(wrappedValue: Rect3D, from: UnitLength)`

Creates a value that maps the specified `Rect3D`, whose dimensions are
specified in physical length measurements in the given unit, to the
corresponding value in points in the associated scene.

Initializer

# init(wrappedValue:from:)

Creates a value that maps the specified `Rect3D`, whose dimensions are
specified in physical length measurements in the given unit, to the
corresponding value in points in the associated scene.

visionOS 1.0+

    
    
    init(
        wrappedValue rect: Rect3D,
        from unit: UnitLength
    ) where Value == Rect3D

## See Also

### Creating a metric

`init(wrappedValue: Value, from: UnitLength)`

Creates a value that maps the specified set of physical length measurements,
in the specified unit, to a corresponding set of values measured in points in
the associated scene.

`init(wrappedValue: CGPoint, from: UnitLength)`

Creates a value that maps the specified point, whose dimensions are specified
in physical length measurements in the given unit, to the corresponding value
in points in the associated scene.

`init(wrappedValue: CGSize, from: UnitLength)`

Creates a value that maps the specified size, in the specified unit to the
corresponding value in points in the associated scene.

`init(wrappedValue: Size3D, from: UnitLength)`

Creates a value that maps the specified size, in the specified unit to the
corresponding value in points in the associated scene.

`init(wrappedValue: Point3D, from: UnitLength)`

Creates a value that maps the specified point, whose dimensions are specified
in physical length measurements in the given unit, to the corresponding value
in points in the associated scene.

`init(wrappedValue: Value, from: UnitLength)`

Creates a value that maps the specified single physical length measurement, in
the specified unit, to the corresponding value in points in the associated
scene.

`init(wrappedValue: CGRect, from: UnitLength)`

Creates a value that maps the specified rectangle, whose dimensions are
specified in physical length measurements in the given unit, to the
corresponding value in points in the associated scene.

Instance Property

# wrappedValue

A value in points in the coordinate system of the associated scene.

visionOS 1.0+

    
    
    var wrappedValue: Value { get }



# ProgressViewStyle

Type Property

# automatic

The default progress view style in the current context of the view being
styled.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    static var automatic: DefaultProgressViewStyle { get }

Available when `Self` is `DefaultProgressViewStyle`.

## Discussion

The default style represents the recommended style based on the original
initialization parameters of the progress view, and the progress view’s
context within the view hierarchy.

## See Also

### Getting built-in progress view styles

`static var circular: CircularProgressViewStyle`

The style of a progress view that uses a circular gauge to indicate the
partial completion of an activity.

Available when `Self` is `CircularProgressViewStyle`.

`static var linear: LinearProgressViewStyle`

A progress view that visually indicates its progress using a horizontal bar.

Available when `Self` is `LinearProgressViewStyle`.

Type Property

# circular

The style of a progress view that uses a circular gauge to indicate the
partial completion of an activity.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    static var circular: CircularProgressViewStyle { get }

Available when `Self` is `CircularProgressViewStyle`.

## Discussion

On watchOS, and in widgets and complications, a circular progress view appears
as a gauge with the `accessoryCircularCapacity` style. If the progress view is
indeterminate, the gauge is empty.

In cases where no determinate circular progress view style is available,
circular progress views use an indeterminate style.

## See Also

### Getting built-in progress view styles

`static var automatic: DefaultProgressViewStyle`

The default progress view style in the current context of the view being
styled.

Available when `Self` is `DefaultProgressViewStyle`.

`static var linear: LinearProgressViewStyle`

A progress view that visually indicates its progress using a horizontal bar.

Available when `Self` is `LinearProgressViewStyle`.

Type Property

# linear

A progress view that visually indicates its progress using a horizontal bar.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    static var linear: LinearProgressViewStyle { get }

Available when `Self` is `LinearProgressViewStyle`.

## See Also

### Getting built-in progress view styles

`static var automatic: DefaultProgressViewStyle`

The default progress view style in the current context of the view being
styled.

Available when `Self` is `DefaultProgressViewStyle`.

`static var circular: CircularProgressViewStyle`

The style of a progress view that uses a circular gauge to indicate the
partial completion of an activity.

Available when `Self` is `CircularProgressViewStyle`.

Instance Method

# makeBody(configuration:)

Creates a view representing the body of a progress view.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    @ViewBuilder
    func makeBody(configuration: Self.Configuration) -> Self.Body

**Required**

##  Parameters

`configuration`

    

The properties of the progress view being created.

`configuration`

    

The properties of the progress view, such as its preferred progress type.

## Discussion

The view hierarchy calls this method for each progress view where this style
is the current progress view style.

## See Also

### Creating custom progress view styles

`typealias Configuration`

A type alias for the properties of a progress view instance.

`associatedtype Body : View`

A view representing the body of a progress view.

**Required**

Type Alias

# ProgressViewStyle.Configuration

A type alias for the properties of a progress view instance.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    typealias Configuration = ProgressViewStyleConfiguration

## See Also

### Creating custom progress view styles

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Creates a view representing the body of a progress view.

**Required**

` associatedtype Body : View`

A view representing the body of a progress view.

**Required**

Associated Type

# Body

A view representing the body of a progress view.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    associatedtype Body : View

**Required**

## See Also

### Creating custom progress view styles

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Creates a view representing the body of a progress view.

**Required**

` typealias Configuration`

A type alias for the properties of a progress view instance.

Structure

# DefaultProgressViewStyle

The default progress view style in the current context of the view being
styled.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    struct DefaultProgressViewStyle

## Overview

Use `automatic` to construct this style.

## Topics

### Creating the progress view style

`init()`

Creates a default progress view style.

## Relationships

### Conforms To

  * `ProgressViewStyle`

## See Also

### Supporting types

`struct CircularProgressViewStyle`

A progress view that uses a circular gauge to indicate the partial completion
of an activity.

`struct LinearProgressViewStyle`

A progress view that visually indicates its progress using a horizontal bar.

Structure

# CircularProgressViewStyle

A progress view that uses a circular gauge to indicate the partial completion
of an activity.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    struct CircularProgressViewStyle

## Overview

On watchOS, and in widgets and complications, a circular progress view appears
as a gauge with the `accessoryCircularCapacity` style. If the progress view is
indeterminate, the gauge is empty.

In cases where no determinate circular progress view style is available,
circular progress views use an indeterminate style.

Use `circular` to construct the circular progress view style.

## Topics

### Creating the progress view style

`init()`

Creates a circular progress view style.

### Deprecated initializers

`init(tint: Color)`

Creates a circular progress view style with a tint color.

Deprecated

## Relationships

### Conforms To

  * `ProgressViewStyle`

## See Also

### Supporting types

`struct DefaultProgressViewStyle`

The default progress view style in the current context of the view being
styled.

`struct LinearProgressViewStyle`

A progress view that visually indicates its progress using a horizontal bar.

Structure

# LinearProgressViewStyle

A progress view that visually indicates its progress using a horizontal bar.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    struct LinearProgressViewStyle

## Overview

Use `linear` to construct this style.

## Topics

### Creating the progress view style

`init()`

Creates a linear progress view style.

### Deprecated initializers

`init(tint: Color)`

Creates a linear progress view style with a tint color.

Deprecated

## Relationships

### Conforms To

  * `ProgressViewStyle`

## See Also

### Supporting types

`struct DefaultProgressViewStyle`

The default progress view style in the current context of the view being
styled.

`struct CircularProgressViewStyle`

A progress view that uses a circular gauge to indicate the partial completion
of an activity.



# ProjectionTransform

Initializer

# init()

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init()

## See Also

### Creating a transform

`init(CGAffineTransform)`

`init(CATransform3D)`

Initializer

# init(_:)

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(_ m: CGAffineTransform)

## See Also

### Creating a transform

`init()`

`init(CATransform3D)`

Initializer

# init(_:)

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(_ m: CATransform3D)

## See Also

### Creating a transform

`init()`

`init(CGAffineTransform)`

Instance Property

# isAffine

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var isAffine: Bool { get }

## See Also

### Getting transform characteristics

`var isIdentity: Bool`

Instance Property

# isIdentity

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var isIdentity: Bool { get }

## See Also

### Getting transform characteristics

`var isAffine: Bool`

Instance Method

# invert()

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    mutating func invert() -> Bool

## See Also

### Manipulating transforms

`func inverted() -> ProjectionTransform`

`func concatenating(ProjectionTransform) -> ProjectionTransform`

Instance Method

# inverted()

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func inverted() -> ProjectionTransform

## See Also

### Manipulating transforms

`func invert() -> Bool`

`func concatenating(ProjectionTransform) -> ProjectionTransform`

Instance Method

# concatenating(_:)

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func concatenating(_ rhs: ProjectionTransform) -> ProjectionTransform

## See Also

### Manipulating transforms

`func invert() -> Bool`

`func inverted() -> ProjectionTransform`

Instance Property

# m11

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var m11: CGFloat

## See Also

### Accessing the transform’s coefficients

`var m12: CGFloat`

`var m13: CGFloat`

`var m21: CGFloat`

`var m22: CGFloat`

`var m23: CGFloat`

`var m31: CGFloat`

`var m32: CGFloat`

`var m33: CGFloat`

Instance Property

# m12

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var m12: CGFloat

## See Also

### Accessing the transform’s coefficients

`var m11: CGFloat`

`var m13: CGFloat`

`var m21: CGFloat`

`var m22: CGFloat`

`var m23: CGFloat`

`var m31: CGFloat`

`var m32: CGFloat`

`var m33: CGFloat`

Instance Property

# m13

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var m13: CGFloat

## See Also

### Accessing the transform’s coefficients

`var m11: CGFloat`

`var m12: CGFloat`

`var m21: CGFloat`

`var m22: CGFloat`

`var m23: CGFloat`

`var m31: CGFloat`

`var m32: CGFloat`

`var m33: CGFloat`

Instance Property

# m21

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var m21: CGFloat

## See Also

### Accessing the transform’s coefficients

`var m11: CGFloat`

`var m12: CGFloat`

`var m13: CGFloat`

`var m22: CGFloat`

`var m23: CGFloat`

`var m31: CGFloat`

`var m32: CGFloat`

`var m33: CGFloat`

Instance Property

# m22

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var m22: CGFloat

## See Also

### Accessing the transform’s coefficients

`var m11: CGFloat`

`var m12: CGFloat`

`var m13: CGFloat`

`var m21: CGFloat`

`var m23: CGFloat`

`var m31: CGFloat`

`var m32: CGFloat`

`var m33: CGFloat`

Instance Property

# m23

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var m23: CGFloat

## See Also

### Accessing the transform’s coefficients

`var m11: CGFloat`

`var m12: CGFloat`

`var m13: CGFloat`

`var m21: CGFloat`

`var m22: CGFloat`

`var m31: CGFloat`

`var m32: CGFloat`

`var m33: CGFloat`

Instance Property

# m31

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var m31: CGFloat

## See Also

### Accessing the transform’s coefficients

`var m11: CGFloat`

`var m12: CGFloat`

`var m13: CGFloat`

`var m21: CGFloat`

`var m22: CGFloat`

`var m23: CGFloat`

`var m32: CGFloat`

`var m33: CGFloat`

Instance Property

# m32

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var m32: CGFloat

## See Also

### Accessing the transform’s coefficients

`var m11: CGFloat`

`var m12: CGFloat`

`var m13: CGFloat`

`var m21: CGFloat`

`var m22: CGFloat`

`var m23: CGFloat`

`var m31: CGFloat`

`var m33: CGFloat`

Instance Property

# m33

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var m33: CGFloat

## See Also

### Accessing the transform’s coefficients

`var m11: CGFloat`

`var m12: CGFloat`

`var m13: CGFloat`

`var m21: CGFloat`

`var m22: CGFloat`

`var m23: CGFloat`

`var m31: CGFloat`

`var m32: CGFloat`



# PlainButtonStyle

Initializer

# init()

Creates a plain button style.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init()

Instance Method

# makeBody(configuration:)

Creates a view that represents the body of a button.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func makeBody(configuration: PlainButtonStyle.Configuration) -> some View
    

##  Parameters

`configuration `

    

The properties of the button.

## Discussion

The system calls this method for each `Button` instance in a view hierarchy
where this style is the current button style.



# PickerStyle

Type Property

# automatic

The default picker style, based on the picker’s context.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static var automatic: DefaultPickerStyle { get }

Available when `Self` is `DefaultPickerStyle`.

## Discussion

How a picker using the default picker style appears largely depends on the
platform and the view type in which it appears. For example, in a standard
view, the default picker styles by platform are:

  * On iOS and watchOS the default is a wheel.

  * On macOS, the default is a pop-up button.

  * On tvOS, the default is a segmented control.

The default picker style may also take into account other factors — like
whether the picker appears in a container view — when setting the appearance
of a picker.

You can override a picker’s style. To apply the default style to a picker, or
to a view that contains pickers, use the `pickerStyle(_:)` modifier.

## See Also

### Getting built-in picker styles

`static var inline: InlinePickerStyle`

A `PickerStyle` where each option is displayed inline with other views in the
current container.

Available when `Self` is `InlinePickerStyle`.

`static var menu: MenuPickerStyle`

A picker style that presents the options as a menu when the user presses a
button, or as a submenu when nested within a larger menu.

Available when `Self` is `MenuPickerStyle`.

`static var navigationLink: NavigationLinkPickerStyle`

A picker style represented by a navigation link that presents the options by
pushing a List-style picker view.

Available when `Self` is `NavigationLinkPickerStyle`.

`static var palette: PalettePickerStyle`

A picker style that presents the options as a row of compact elements.

Available when `Self` is `PalettePickerStyle`.

`static var radioGroup: RadioGroupPickerStyle`

A picker style that presents the options as a group of radio buttons.

Available when `Self` is `RadioGroupPickerStyle`.

`static var segmented: SegmentedPickerStyle`

A picker style that presents the options in a segmented control.

Available when `Self` is `SegmentedPickerStyle`.

`static var wheel: WheelPickerStyle`

A picker style that presents the options in a scrollable wheel that shows the
selected option and a few neighboring options.

Available when `Self` is `WheelPickerStyle`.

Type Property

# inline

A `PickerStyle` where each option is displayed inline with other views in the
current container.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    static var inline: InlinePickerStyle { get }

Available when `Self` is `InlinePickerStyle`.

## See Also

### Getting built-in picker styles

`static var automatic: DefaultPickerStyle`

The default picker style, based on the picker’s context.

Available when `Self` is `DefaultPickerStyle`.

`static var menu: MenuPickerStyle`

A picker style that presents the options as a menu when the user presses a
button, or as a submenu when nested within a larger menu.

Available when `Self` is `MenuPickerStyle`.

`static var navigationLink: NavigationLinkPickerStyle`

A picker style represented by a navigation link that presents the options by
pushing a List-style picker view.

Available when `Self` is `NavigationLinkPickerStyle`.

`static var palette: PalettePickerStyle`

A picker style that presents the options as a row of compact elements.

Available when `Self` is `PalettePickerStyle`.

`static var radioGroup: RadioGroupPickerStyle`

A picker style that presents the options as a group of radio buttons.

Available when `Self` is `RadioGroupPickerStyle`.

`static var segmented: SegmentedPickerStyle`

A picker style that presents the options in a segmented control.

Available when `Self` is `SegmentedPickerStyle`.

`static var wheel: WheelPickerStyle`

A picker style that presents the options in a scrollable wheel that shows the
selected option and a few neighboring options.

Available when `Self` is `WheelPickerStyle`.

Type Property

# menu

A picker style that presents the options as a menu when the user presses a
button, or as a submenu when nested within a larger menu.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 17.0+  visionOS
1.0+

    
    
    static var menu: MenuPickerStyle { get }

Available when `Self` is `MenuPickerStyle`.

## Discussion

Use this style when there are more than five options. Consider using `inline`
when there are fewer than five options.

The button itself indicates the selected option. You can include additional
controls in the set of options, such as a button to customize the list of
options.

To apply this style to a picker, or to a view that contains pickers, use the
`pickerStyle(_:)` modifier.

## See Also

### Getting built-in picker styles

`static var automatic: DefaultPickerStyle`

The default picker style, based on the picker’s context.

Available when `Self` is `DefaultPickerStyle`.

`static var inline: InlinePickerStyle`

A `PickerStyle` where each option is displayed inline with other views in the
current container.

Available when `Self` is `InlinePickerStyle`.

`static var navigationLink: NavigationLinkPickerStyle`

A picker style represented by a navigation link that presents the options by
pushing a List-style picker view.

Available when `Self` is `NavigationLinkPickerStyle`.

`static var palette: PalettePickerStyle`

A picker style that presents the options as a row of compact elements.

Available when `Self` is `PalettePickerStyle`.

`static var radioGroup: RadioGroupPickerStyle`

A picker style that presents the options as a group of radio buttons.

Available when `Self` is `RadioGroupPickerStyle`.

`static var segmented: SegmentedPickerStyle`

A picker style that presents the options in a segmented control.

Available when `Self` is `SegmentedPickerStyle`.

`static var wheel: WheelPickerStyle`

A picker style that presents the options in a scrollable wheel that shows the
selected option and a few neighboring options.

Available when `Self` is `WheelPickerStyle`.

Type Property

# navigationLink

A picker style represented by a navigation link that presents the options by
pushing a List-style picker view.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    static var navigationLink: NavigationLinkPickerStyle { get }

Available when `Self` is `NavigationLinkPickerStyle`.

## Discussion

In navigation stacks, prefer the default `menu` style. Consider the navigation
link style when you have a large number of options or your design is better
expressed by pushing onto a stack.

To apply this style to a picker, or to a view that contains pickers, use the
`pickerStyle(_:)` modifier.

## See Also

### Getting built-in picker styles

`static var automatic: DefaultPickerStyle`

The default picker style, based on the picker’s context.

Available when `Self` is `DefaultPickerStyle`.

`static var inline: InlinePickerStyle`

A `PickerStyle` where each option is displayed inline with other views in the
current container.

Available when `Self` is `InlinePickerStyle`.

`static var menu: MenuPickerStyle`

A picker style that presents the options as a menu when the user presses a
button, or as a submenu when nested within a larger menu.

Available when `Self` is `MenuPickerStyle`.

`static var palette: PalettePickerStyle`

A picker style that presents the options as a row of compact elements.

Available when `Self` is `PalettePickerStyle`.

`static var radioGroup: RadioGroupPickerStyle`

A picker style that presents the options as a group of radio buttons.

Available when `Self` is `RadioGroupPickerStyle`.

`static var segmented: SegmentedPickerStyle`

A picker style that presents the options in a segmented control.

Available when `Self` is `SegmentedPickerStyle`.

`static var wheel: WheelPickerStyle`

A picker style that presents the options in a scrollable wheel that shows the
selected option and a few neighboring options.

Available when `Self` is `WheelPickerStyle`.

Type Property

# palette

A picker style that presents the options as a row of compact elements.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    static var palette: PalettePickerStyle { get }

Available when `Self` is `PalettePickerStyle`.

## Discussion

Note

When used outside of menus, this style is rendered as a segmented picker. If
that is the intended usage, consider `segmented` instead.

For each option’s label, use one symbol per item, if you add more than 6
options, the picker scrolls horizontally on iOS.

The following example creates a palette picker:

Palette pickers will display the selection of untinted SF Symbols or template
images by applying the system tint. For tinted SF Symbols, a stroke is
outlined around the symbol upon selection. If you would like to supply a
particular image (or SF Symbol) to signify selection, we suggest using
`custom`. This deactivates any system selection behavior, allowing the
provided image to solely indicate selection instead.

The following example creates a palette picker that disables the system
selection behaviour:

If a specific SF Symbol variant is preferable instead, use
`symbolVariant(_:)`:

To apply this style to a picker, or to a view that contains pickers, use the
`pickerStyle(_:)` modifier.

## See Also

### Getting built-in picker styles

`static var automatic: DefaultPickerStyle`

The default picker style, based on the picker’s context.

Available when `Self` is `DefaultPickerStyle`.

`static var inline: InlinePickerStyle`

A `PickerStyle` where each option is displayed inline with other views in the
current container.

Available when `Self` is `InlinePickerStyle`.

`static var menu: MenuPickerStyle`

A picker style that presents the options as a menu when the user presses a
button, or as a submenu when nested within a larger menu.

Available when `Self` is `MenuPickerStyle`.

`static var navigationLink: NavigationLinkPickerStyle`

A picker style represented by a navigation link that presents the options by
pushing a List-style picker view.

Available when `Self` is `NavigationLinkPickerStyle`.

`static var radioGroup: RadioGroupPickerStyle`

A picker style that presents the options as a group of radio buttons.

Available when `Self` is `RadioGroupPickerStyle`.

`static var segmented: SegmentedPickerStyle`

A picker style that presents the options in a segmented control.

Available when `Self` is `SegmentedPickerStyle`.

`static var wheel: WheelPickerStyle`

A picker style that presents the options in a scrollable wheel that shows the
selected option and a few neighboring options.

Available when `Self` is `WheelPickerStyle`.

Type Property

# radioGroup

A picker style that presents the options as a group of radio buttons.

macOS 10.15+

    
    
    static var radioGroup: RadioGroupPickerStyle { get }

Available when `Self` is `RadioGroupPickerStyle`.

## Discussion

Use this style when there are two to five options. Consider using `menu` when
there are more than five options.

For each option’s label, use sentence-style capitalization without ending
punctuation, like a period or colon.

To apply this style to a picker, or to a view that contains pickers, use the
`pickerStyle(_:)` modifier.

## See Also

### Getting built-in picker styles

`static var automatic: DefaultPickerStyle`

The default picker style, based on the picker’s context.

Available when `Self` is `DefaultPickerStyle`.

`static var inline: InlinePickerStyle`

A `PickerStyle` where each option is displayed inline with other views in the
current container.

Available when `Self` is `InlinePickerStyle`.

`static var menu: MenuPickerStyle`

A picker style that presents the options as a menu when the user presses a
button, or as a submenu when nested within a larger menu.

Available when `Self` is `MenuPickerStyle`.

`static var navigationLink: NavigationLinkPickerStyle`

A picker style represented by a navigation link that presents the options by
pushing a List-style picker view.

Available when `Self` is `NavigationLinkPickerStyle`.

`static var palette: PalettePickerStyle`

A picker style that presents the options as a row of compact elements.

Available when `Self` is `PalettePickerStyle`.

`static var segmented: SegmentedPickerStyle`

A picker style that presents the options in a segmented control.

Available when `Self` is `SegmentedPickerStyle`.

`static var wheel: WheelPickerStyle`

A picker style that presents the options in a scrollable wheel that shows the
selected option and a few neighboring options.

Available when `Self` is `WheelPickerStyle`.

Type Property

# segmented

A picker style that presents the options in a segmented control.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+
visionOS 1.0+

    
    
    static var segmented: SegmentedPickerStyle { get }

Available when `Self` is `SegmentedPickerStyle`.

## Discussion

Use this style when there are two to five options. Consider using `menu` when
there are more than five options.

For each option’s label, use sentence-style capitalization without ending
punctuation, like a period or colon.

To apply this style to a picker, or to a view that contains pickers, use the
`pickerStyle(_:)` modifier.

## See Also

### Getting built-in picker styles

`static var automatic: DefaultPickerStyle`

The default picker style, based on the picker’s context.

Available when `Self` is `DefaultPickerStyle`.

`static var inline: InlinePickerStyle`

A `PickerStyle` where each option is displayed inline with other views in the
current container.

Available when `Self` is `InlinePickerStyle`.

`static var menu: MenuPickerStyle`

A picker style that presents the options as a menu when the user presses a
button, or as a submenu when nested within a larger menu.

Available when `Self` is `MenuPickerStyle`.

`static var navigationLink: NavigationLinkPickerStyle`

A picker style represented by a navigation link that presents the options by
pushing a List-style picker view.

Available when `Self` is `NavigationLinkPickerStyle`.

`static var palette: PalettePickerStyle`

A picker style that presents the options as a row of compact elements.

Available when `Self` is `PalettePickerStyle`.

`static var radioGroup: RadioGroupPickerStyle`

A picker style that presents the options as a group of radio buttons.

Available when `Self` is `RadioGroupPickerStyle`.

`static var wheel: WheelPickerStyle`

A picker style that presents the options in a scrollable wheel that shows the
selected option and a few neighboring options.

Available when `Self` is `WheelPickerStyle`.

Type Property

# wheel

A picker style that presents the options in a scrollable wheel that shows the
selected option and a few neighboring options.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  watchOS 6.0+  visionOS 1.0+

    
    
    static var wheel: WheelPickerStyle { get }

Available when `Self` is `WheelPickerStyle`.

## Discussion

Because most options aren’t visible, organize them in a predictable order,
such as alphabetically.

To apply this style to a picker, or to a view that contains pickers, use the
`pickerStyle(_:)` modifier.

## See Also

### Getting built-in picker styles

`static var automatic: DefaultPickerStyle`

The default picker style, based on the picker’s context.

Available when `Self` is `DefaultPickerStyle`.

`static var inline: InlinePickerStyle`

A `PickerStyle` where each option is displayed inline with other views in the
current container.

Available when `Self` is `InlinePickerStyle`.

`static var menu: MenuPickerStyle`

A picker style that presents the options as a menu when the user presses a
button, or as a submenu when nested within a larger menu.

Available when `Self` is `MenuPickerStyle`.

`static var navigationLink: NavigationLinkPickerStyle`

A picker style represented by a navigation link that presents the options by
pushing a List-style picker view.

Available when `Self` is `NavigationLinkPickerStyle`.

`static var palette: PalettePickerStyle`

A picker style that presents the options as a row of compact elements.

Available when `Self` is `PalettePickerStyle`.

`static var radioGroup: RadioGroupPickerStyle`

A picker style that presents the options as a group of radio buttons.

Available when `Self` is `RadioGroupPickerStyle`.

`static var segmented: SegmentedPickerStyle`

A picker style that presents the options in a segmented control.

Available when `Self` is `SegmentedPickerStyle`.

Structure

# DefaultPickerStyle

The default picker style, based on the picker’s context.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    struct DefaultPickerStyle

## Overview

You can also use `automatic` to construct this style.

## Topics

### Creating the picker style

`init()`

Creates a default picker style.

## Relationships

### Conforms To

  * `PickerStyle`

## See Also

### Supporting types

`struct InlinePickerStyle`

A `PickerStyle` where each option is displayed inline with other views in the
current container.

`struct MenuPickerStyle`

A picker style that presents the options as a menu when the user presses a
button, or as a submenu when nested within a larger menu.

`struct NavigationLinkPickerStyle`

A picker style represented by a navigation link that presents the options by
pushing a List-style picker view.

`struct PalettePickerStyle`

A picker style that presents the options as a row of compact elements.

`struct RadioGroupPickerStyle`

A picker style that presents the options as a group of radio buttons.

`struct SegmentedPickerStyle`

A picker style that presents the options in a segmented control.

`struct WheelPickerStyle`

A picker style that presents the options in a scrollable wheel that shows the
selected option and a few neighboring options.

Structure

# InlinePickerStyle

A `PickerStyle` where each option is displayed inline with other views in the
current container.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    struct InlinePickerStyle

## Overview

You can also use `inline` to construct this style.

## Topics

### Creating the picker style

`init()`

Creates an inline picker style.

## Relationships

### Conforms To

  * `PickerStyle`

## See Also

### Supporting types

`struct DefaultPickerStyle`

The default picker style, based on the picker’s context.

`struct MenuPickerStyle`

A picker style that presents the options as a menu when the user presses a
button, or as a submenu when nested within a larger menu.

`struct NavigationLinkPickerStyle`

A picker style represented by a navigation link that presents the options by
pushing a List-style picker view.

`struct PalettePickerStyle`

A picker style that presents the options as a row of compact elements.

`struct RadioGroupPickerStyle`

A picker style that presents the options as a group of radio buttons.

`struct SegmentedPickerStyle`

A picker style that presents the options in a segmented control.

`struct WheelPickerStyle`

A picker style that presents the options in a scrollable wheel that shows the
selected option and a few neighboring options.

Structure

# MenuPickerStyle

A picker style that presents the options as a menu when the user presses a
button, or as a submenu when nested within a larger menu.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 17.0+  visionOS
1.0+

    
    
    struct MenuPickerStyle

## Overview

You can also use `menu` to construct this style.

## Topics

### Creating the picker style

`init()`

Creates a menu picker style.

## Relationships

### Conforms To

  * `PickerStyle`

## See Also

### Supporting types

`struct DefaultPickerStyle`

The default picker style, based on the picker’s context.

`struct InlinePickerStyle`

A `PickerStyle` where each option is displayed inline with other views in the
current container.

`struct NavigationLinkPickerStyle`

A picker style represented by a navigation link that presents the options by
pushing a List-style picker view.

`struct PalettePickerStyle`

A picker style that presents the options as a row of compact elements.

`struct RadioGroupPickerStyle`

A picker style that presents the options as a group of radio buttons.

`struct SegmentedPickerStyle`

A picker style that presents the options in a segmented control.

`struct WheelPickerStyle`

A picker style that presents the options in a scrollable wheel that shows the
selected option and a few neighboring options.

Structure

# NavigationLinkPickerStyle

A picker style represented by a navigation link that presents the options by
pushing a List-style picker view.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    struct NavigationLinkPickerStyle

## Overview

In navigation stacks, prefer the default `menu` style. Consider the navigation
link style when you have a large number of options or your design is better
expressed by pushing onto a stack.

You can also use `navigationLink` to construct this style.

## Topics

### Creating the picker style

`init()`

Creates a navigation link picker style.

## Relationships

### Conforms To

  * `PickerStyle`

## See Also

### Supporting types

`struct DefaultPickerStyle`

The default picker style, based on the picker’s context.

`struct InlinePickerStyle`

A `PickerStyle` where each option is displayed inline with other views in the
current container.

`struct MenuPickerStyle`

A picker style that presents the options as a menu when the user presses a
button, or as a submenu when nested within a larger menu.

`struct PalettePickerStyle`

A picker style that presents the options as a row of compact elements.

`struct RadioGroupPickerStyle`

A picker style that presents the options as a group of radio buttons.

`struct SegmentedPickerStyle`

A picker style that presents the options in a segmented control.

`struct WheelPickerStyle`

A picker style that presents the options in a scrollable wheel that shows the
selected option and a few neighboring options.

Structure

# PalettePickerStyle

A picker style that presents the options as a row of compact elements.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    struct PalettePickerStyle

## Overview

You can also use `palette` to construct this style.

## Topics

### Creating the picker style

`init()`

Creates a palette picker style.

## Relationships

### Conforms To

  * `PickerStyle`

## See Also

### Supporting types

`struct DefaultPickerStyle`

The default picker style, based on the picker’s context.

`struct InlinePickerStyle`

A `PickerStyle` where each option is displayed inline with other views in the
current container.

`struct MenuPickerStyle`

A picker style that presents the options as a menu when the user presses a
button, or as a submenu when nested within a larger menu.

`struct NavigationLinkPickerStyle`

A picker style represented by a navigation link that presents the options by
pushing a List-style picker view.

`struct RadioGroupPickerStyle`

A picker style that presents the options as a group of radio buttons.

`struct SegmentedPickerStyle`

A picker style that presents the options in a segmented control.

`struct WheelPickerStyle`

A picker style that presents the options in a scrollable wheel that shows the
selected option and a few neighboring options.

Structure

# RadioGroupPickerStyle

A picker style that presents the options as a group of radio buttons.

macOS 10.15+

    
    
    struct RadioGroupPickerStyle

## Overview

You can also use `radioGroup` to construct this style.

## Topics

### Creating the picker style

`init()`

Creates a radio group picker style.

## Relationships

### Conforms To

  * `PickerStyle`

## See Also

### Supporting types

`struct DefaultPickerStyle`

The default picker style, based on the picker’s context.

`struct InlinePickerStyle`

A `PickerStyle` where each option is displayed inline with other views in the
current container.

`struct MenuPickerStyle`

A picker style that presents the options as a menu when the user presses a
button, or as a submenu when nested within a larger menu.

`struct NavigationLinkPickerStyle`

A picker style represented by a navigation link that presents the options by
pushing a List-style picker view.

`struct PalettePickerStyle`

A picker style that presents the options as a row of compact elements.

`struct SegmentedPickerStyle`

A picker style that presents the options in a segmented control.

`struct WheelPickerStyle`

A picker style that presents the options in a scrollable wheel that shows the
selected option and a few neighboring options.

Structure

# SegmentedPickerStyle

A picker style that presents the options in a segmented control.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+
visionOS 1.0+

    
    
    struct SegmentedPickerStyle

## Overview

You can also use `segmented` to construct this style.

## Topics

### Creating the picker style

`init()`

Creates a segmented picker style.

## Relationships

### Conforms To

  * `PickerStyle`

## See Also

### Supporting types

`struct DefaultPickerStyle`

The default picker style, based on the picker’s context.

`struct InlinePickerStyle`

A `PickerStyle` where each option is displayed inline with other views in the
current container.

`struct MenuPickerStyle`

A picker style that presents the options as a menu when the user presses a
button, or as a submenu when nested within a larger menu.

`struct NavigationLinkPickerStyle`

A picker style represented by a navigation link that presents the options by
pushing a List-style picker view.

`struct PalettePickerStyle`

A picker style that presents the options as a row of compact elements.

`struct RadioGroupPickerStyle`

A picker style that presents the options as a group of radio buttons.

`struct WheelPickerStyle`

A picker style that presents the options in a scrollable wheel that shows the
selected option and a few neighboring options.

Structure

# WheelPickerStyle

A picker style that presents the options in a scrollable wheel that shows the
selected option and a few neighboring options.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  watchOS 6.0+  visionOS 1.0+

    
    
    struct WheelPickerStyle

## Overview

You can also use `wheel` to construct this style.

## Topics

### Creating the picker style

`init()`

Sets the picker style to display an item wheel from which the user makes a
selection.

## Relationships

### Conforms To

  * `PickerStyle`

## See Also

### Supporting types

`struct DefaultPickerStyle`

The default picker style, based on the picker’s context.

`struct InlinePickerStyle`

A `PickerStyle` where each option is displayed inline with other views in the
current container.

`struct MenuPickerStyle`

A picker style that presents the options as a menu when the user presses a
button, or as a submenu when nested within a larger menu.

`struct NavigationLinkPickerStyle`

A picker style represented by a navigation link that presents the options by
pushing a List-style picker view.

`struct PalettePickerStyle`

A picker style that presents the options as a row of compact elements.

`struct RadioGroupPickerStyle`

A picker style that presents the options as a group of radio buttons.

`struct SegmentedPickerStyle`

A picker style that presents the options in a segmented control.

Structure

# PopUpButtonPickerStyle

A picker style that presents the options as a menu when the user presses a
button.

macOS 10.15–14.4  Deprecated

    
    
    struct PopUpButtonPickerStyle

Deprecated

Use `MenuPickerStyle` instead.

## Overview

Use this style when there are more than five options. Consider using
`RadioGroupPickerStyle` when there are fewer than five options.

The button itself indicates the selected option. You can include additional
controls in the set of options, such as a button to customize the list of
options.

To apply this style to a picker, or to a view that contains pickers, use the
`pickerStyle(_:)` modifier.

### Creating the picker style

  * `init()`

## Topics

### Initializers

`init()`

Creates a pop-up button picker style.

## Relationships

### Conforms To

  * `PickerStyle`



# PresentationBackgroundInteraction

Type Property

# automatic

The default background interaction for the presentation.

iOS 16.4+  iPadOS 16.4+  macOS 13.3+  Mac Catalyst 16.4+  tvOS 16.4+  watchOS
9.4+  visionOS 1.0+

    
    
    static var automatic: PresentationBackgroundInteraction { get }

## See Also

### Getting interaction types

`static var disabled: PresentationBackgroundInteraction`

People can’t interact with the view behind a presentation.

`static var enabled: PresentationBackgroundInteraction`

People can interact with the view behind a presentation.

`static func enabled(upThrough: PresentationDetent) ->
PresentationBackgroundInteraction`

People can interact with the view behind a presentation up through a specified
detent.

Type Property

# disabled

People can’t interact with the view behind a presentation.

iOS 16.4+  iPadOS 16.4+  macOS 13.3+  Mac Catalyst 16.4+  tvOS 16.4+  watchOS
9.4+  visionOS 1.0+

    
    
    static var disabled: PresentationBackgroundInteraction { get }

## See Also

### Getting interaction types

`static var automatic: PresentationBackgroundInteraction`

The default background interaction for the presentation.

`static var enabled: PresentationBackgroundInteraction`

People can interact with the view behind a presentation.

`static func enabled(upThrough: PresentationDetent) ->
PresentationBackgroundInteraction`

People can interact with the view behind a presentation up through a specified
detent.

Type Property

# enabled

People can interact with the view behind a presentation.

iOS 16.4+  iPadOS 16.4+  macOS 13.3+  Mac Catalyst 16.4+  tvOS 16.4+  watchOS
9.4+  visionOS 1.0+

    
    
    static var enabled: PresentationBackgroundInteraction { get }

## See Also

### Getting interaction types

`static var automatic: PresentationBackgroundInteraction`

The default background interaction for the presentation.

`static var disabled: PresentationBackgroundInteraction`

People can’t interact with the view behind a presentation.

`static func enabled(upThrough: PresentationDetent) ->
PresentationBackgroundInteraction`

People can interact with the view behind a presentation up through a specified
detent.

Type Method

# enabled(upThrough:)

People can interact with the view behind a presentation up through a specified
detent.

iOS 16.4+  iPadOS 16.4+  macOS 13.3+  Mac Catalyst 16.4+  tvOS 16.4+  watchOS
9.4+  visionOS 1.0+

    
    
    static func enabled(upThrough detent: PresentationDetent) -> PresentationBackgroundInteraction

##  Parameters

`detent`

    

The largest detent at which people can interact with the view behind the
presentation.

## Discussion

At detents larger than the one you specify, SwiftUI disables interaction.

## See Also

### Getting interaction types

`static var automatic: PresentationBackgroundInteraction`

The default background interaction for the presentation.

`static var disabled: PresentationBackgroundInteraction`

People can’t interact with the view behind a presentation.

`static var enabled: PresentationBackgroundInteraction`

People can interact with the view behind a presentation.



# Presentation modifiers

Instance Method

# alert(_:isPresented:actions:)

Presents an alert when a given condition is true, using a string variable as a
title.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func alert<S, A>(
        _ title: S,
        isPresented: Binding<Bool>,
        @ViewBuilder actions: () -> A
    ) -> some View where S : StringProtocol, A : View
    

##  Parameters

`title`

    

A text string used as the title of the alert.

`isPresented`

    

A binding to a Boolean value that determines whether to present the alert.
When the user presses or taps one of the alert’s actions, the system sets this
value to `false` and dismisses.

`actions`

    

A `ViewBuilder` returning the alert’s actions.

## Discussion

In the example below, a login form conditionally presents an alert by setting
the `didFail` state variable. When the form sets the value to to `true`, the
system displays an alert with an “OK” action.

All actions in an alert dismiss the alert after the action runs. The default
button is shown with greater prominence. You can influence the default button
by assigning it the `defaultAction` keyboard shortcut.

The system may reorder the buttons based on their role and prominence.

If no actions are present, the system includes a standard “OK” action. No
default cancel action is provided. If you want to show a cancel action, use a
button with a role of `cancel`.

On iOS, tvOS, and watchOS, alerts only support controls with labels that are
`Text`. Passing any other type of view results in the content being omitted.

## See Also

### Presenting an alert

`func alert<A>(Text, isPresented: Binding<Bool>, actions: () -> A) -> some
View`

Presents an alert when a given condition is true, using a text view for the
title.

`func alert<A>(LocalizedStringKey, isPresented: Binding<Bool>, actions: () ->
A) -> some View`

Presents an alert when a given condition is true, using a localized string key
for the title.

`func alert<A, T>(Text, isPresented: Binding<Bool>, presenting: T?, actions:
(T) -> A) -> some View`

Presents an alert using the given data to produce the alert’s content and a
text view as a title.

`func alert<A, T>(LocalizedStringKey, isPresented: Binding<Bool>, presenting:
T?, actions: (T) -> A) -> some View`

Presents an alert using the given data to produce the alert’s content and a
localized string key for a title.

`func alert<S, A, T>(S, isPresented: Binding<Bool>, presenting: T?, actions:
(T) -> A) -> some View`

Presents an alert using the given data to produce the alert’s content and a
string variable as a title.

`func alert<E, A>(isPresented: Binding<Bool>, error: E?, actions: () -> A) ->
some View`

Presents an alert when an error is present.

Instance Method

# alert(_:isPresented:actions:)

Presents an alert when a given condition is true, using a text view for the
title.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func alert<A>(
        _ title: Text,
        isPresented: Binding<Bool>,
        @ViewBuilder actions: () -> A
    ) -> some View where A : View
    

##  Parameters

`title`

    

The title of the alert.

`isPresented`

    

A binding to a Boolean value that determines whether to present the alert.
When the user presses or taps one of the alert’s actions, the system sets this
value to `false` and dismisses.

`actions`

    

A `ViewBuilder` returning the alert’s actions.

## Discussion

In the example below, a login form conditionally presents an alert by setting
the `didFail` state variable. When the form sets the value to to `true`, the
system displays an alert with an “OK” action.

All actions in an alert dismiss the alert after the action runs. The default
button is shown with greater prominence. You can influence the default button
by assigning it the `defaultAction` keyboard shortcut.

The system may reorder the buttons based on their role and prominence.

If no actions are present, the system includes a standard “OK” action. No
default cancel action is provided. If you want to show a cancel action, use a
button with a role of `cancel`.

On iOS, tvOS, and watchOS, alerts only support controls with labels that are
`Text`. Passing any other type of view results in the content being omitted.

## See Also

### Presenting an alert

`func alert<S, A>(S, isPresented: Binding<Bool>, actions: () -> A) -> some
View`

Presents an alert when a given condition is true, using a string variable as a
title.

`func alert<A>(LocalizedStringKey, isPresented: Binding<Bool>, actions: () ->
A) -> some View`

Presents an alert when a given condition is true, using a localized string key
for the title.

`func alert<A, T>(Text, isPresented: Binding<Bool>, presenting: T?, actions:
(T) -> A) -> some View`

Presents an alert using the given data to produce the alert’s content and a
text view as a title.

`func alert<A, T>(LocalizedStringKey, isPresented: Binding<Bool>, presenting:
T?, actions: (T) -> A) -> some View`

Presents an alert using the given data to produce the alert’s content and a
localized string key for a title.

`func alert<S, A, T>(S, isPresented: Binding<Bool>, presenting: T?, actions:
(T) -> A) -> some View`

Presents an alert using the given data to produce the alert’s content and a
string variable as a title.

`func alert<E, A>(isPresented: Binding<Bool>, error: E?, actions: () -> A) ->
some View`

Presents an alert when an error is present.

Instance Method

# alert(_:isPresented:actions:)

Presents an alert when a given condition is true, using a localized string key
for the title.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func alert<A>(
        _ titleKey: LocalizedStringKey,
        isPresented: Binding<Bool>,
        @ViewBuilder actions: () -> A
    ) -> some View where A : View
    

##  Parameters

`titleKey`

    

The key for the localized string that describes the title of the alert.

`isPresented`

    

A binding to a Boolean value that determines whether to present the alert.
When the user presses or taps one of the alert’s actions, the system sets this
value to `false` and dismisses.

`actions`

    

A `ViewBuilder` returning the alert’s actions.

## Discussion

In the example below, a login form conditionally presents an alert by setting
the `didFail` state variable. When the form sets the value to to `true`, the
system displays an alert with an “OK” action.

All actions in an alert dismiss the alert after the action runs. The default
button is shown with greater prominence. You can influence the default button
by assigning it the `defaultAction` keyboard shortcut.

The system may reorder the buttons based on their role and prominence.

If no actions are present, the system includes a standard “OK” action. No
default cancel action is provided. If you want to show a cancel action, use a
button with a role of `cancel`.

On iOS, tvOS, and watchOS, alerts only support controls with labels that are
`Text`. Passing any other type of view results in the content being omitted.

This modifier creates a `Text` view for the title on your behalf, and treats
the localized key similar to `init(_:tableName:bundle:comment:)`. See `Text`
for more information about localizing strings.

## See Also

### Presenting an alert

`func alert<S, A>(S, isPresented: Binding<Bool>, actions: () -> A) -> some
View`

Presents an alert when a given condition is true, using a string variable as a
title.

`func alert<A>(Text, isPresented: Binding<Bool>, actions: () -> A) -> some
View`

Presents an alert when a given condition is true, using a text view for the
title.

`func alert<A, T>(Text, isPresented: Binding<Bool>, presenting: T?, actions:
(T) -> A) -> some View`

Presents an alert using the given data to produce the alert’s content and a
text view as a title.

`func alert<A, T>(LocalizedStringKey, isPresented: Binding<Bool>, presenting:
T?, actions: (T) -> A) -> some View`

Presents an alert using the given data to produce the alert’s content and a
localized string key for a title.

`func alert<S, A, T>(S, isPresented: Binding<Bool>, presenting: T?, actions:
(T) -> A) -> some View`

Presents an alert using the given data to produce the alert’s content and a
string variable as a title.

`func alert<E, A>(isPresented: Binding<Bool>, error: E?, actions: () -> A) ->
some View`

Presents an alert when an error is present.

Instance Method

# alert(_:isPresented:presenting:actions:)

Presents an alert using the given data to produce the alert’s content and a
text view as a title.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func alert<A, T>(
        _ title: Text,
        isPresented: Binding<Bool>,
        presenting data: T?,
        @ViewBuilder actions: (T) -> A
    ) -> some View where A : View
    

##  Parameters

`title`

    

the title of the alert.

`isPresented`

    

A binding to a Boolean value that determines whether to present the alert.
When the user presses or taps one of the alert’s actions, the system sets this
value to `false` and dismisses.

`data`

    

An optional source of truth for the alert. The system passes the contents to
the modifier’s closures. You use this data to populate the fields of an alert
that you create that the system displays to the user.

`actions`

    

A `ViewBuilder` returning the alert’s actions given the currently available
data.

## Discussion

For the alert to appear, both `isPresented` must be `true` and `data` must not
be `nil`. The data should not change after the presentation occurs. Any
changes that you make after the presentation occurs are ignored.

Use this method when you need to populate the fields of an alert with content
from a data source. The example below shows a custom data source,
`SaveDetails`, that provides data to populate the alert:

All actions in an alert dismiss the alert after the action runs. The default
button is shown with greater prominence. You can influence the default button
by assigning it the `defaultAction` keyboard shortcut.

The system may reorder the buttons based on their role and prominence.

If no actions are present, the system includes a standard “OK” action. No
default cancel action is provided. If you want to show a cancel action, use a
button with a role of `cancel`.

On iOS, tvOS, and watchOS, alerts only support controls with labels that are
`Text`. Passing any other type of view results in the content being omitted.

## See Also

### Presenting an alert

`func alert<S, A>(S, isPresented: Binding<Bool>, actions: () -> A) -> some
View`

Presents an alert when a given condition is true, using a string variable as a
title.

`func alert<A>(Text, isPresented: Binding<Bool>, actions: () -> A) -> some
View`

Presents an alert when a given condition is true, using a text view for the
title.

`func alert<A>(LocalizedStringKey, isPresented: Binding<Bool>, actions: () ->
A) -> some View`

Presents an alert when a given condition is true, using a localized string key
for the title.

`func alert<A, T>(LocalizedStringKey, isPresented: Binding<Bool>, presenting:
T?, actions: (T) -> A) -> some View`

Presents an alert using the given data to produce the alert’s content and a
localized string key for a title.

`func alert<S, A, T>(S, isPresented: Binding<Bool>, presenting: T?, actions:
(T) -> A) -> some View`

Presents an alert using the given data to produce the alert’s content and a
string variable as a title.

`func alert<E, A>(isPresented: Binding<Bool>, error: E?, actions: () -> A) ->
some View`

Presents an alert when an error is present.

Instance Method

# alert(_:isPresented:presenting:actions:)

Presents an alert using the given data to produce the alert’s content and a
localized string key for a title.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func alert<A, T>(
        _ titleKey: LocalizedStringKey,
        isPresented: Binding<Bool>,
        presenting data: T?,
        @ViewBuilder actions: (T) -> A
    ) -> some View where A : View
    

##  Parameters

`titleKey`

    

The key for the localized string that describes the title of the alert.

`isPresented`

    

A binding to a Boolean value that determines whether to present the alert.
When the user presses or taps one of the alert’s actions, the system sets this
value to `false` and dismisses.

`data`

    

An optional source of truth for the alert. The system passes the contents to
the modifier’s closures. You use this data to populate the fields of an alert
that you create that the system displays to the user.

`actions`

    

A `ViewBuilder` returning the alert’s actions given the currently available
data.

## Discussion

For the alert to appear, both `isPresented` must be `true` and `data` must not
be `nil`. The data should not change after the presentation occurs. Any
changes that you make after the presentation occurs are ignored.

Use this method when you need to populate the fields of an alert with content
from a data source. The example below shows a custom data source,
`SaveDetails`, that provides data to populate the alert:

This modifier creates a `Text` view for the title on your behalf, and treats
the localized key similar to `init(_:tableName:bundle:comment:)`. See `Text`
for more information about localizing strings.

All actions in an alert dismiss the alert after the action runs. The default
button is shown with greater prominence. You can influence the default button
by assigning it the `defaultAction` keyboard shortcut.

The system may reorder the buttons based on their role and prominence.

If no actions are present, the system includes a standard “OK” action. No
default cancel action is provided. If you want to show a cancel action, use a
button with a role of `cancel`.

On iOS, tvOS, and watchOS, alerts only support controls with labels that are
`Text`. Passing any other type of view results in the content being omitted.

## See Also

### Presenting an alert

`func alert<S, A>(S, isPresented: Binding<Bool>, actions: () -> A) -> some
View`

Presents an alert when a given condition is true, using a string variable as a
title.

`func alert<A>(Text, isPresented: Binding<Bool>, actions: () -> A) -> some
View`

Presents an alert when a given condition is true, using a text view for the
title.

`func alert<A>(LocalizedStringKey, isPresented: Binding<Bool>, actions: () ->
A) -> some View`

Presents an alert when a given condition is true, using a localized string key
for the title.

`func alert<A, T>(Text, isPresented: Binding<Bool>, presenting: T?, actions:
(T) -> A) -> some View`

Presents an alert using the given data to produce the alert’s content and a
text view as a title.

`func alert<S, A, T>(S, isPresented: Binding<Bool>, presenting: T?, actions:
(T) -> A) -> some View`

Presents an alert using the given data to produce the alert’s content and a
string variable as a title.

`func alert<E, A>(isPresented: Binding<Bool>, error: E?, actions: () -> A) ->
some View`

Presents an alert when an error is present.

Instance Method

# alert(_:isPresented:presenting:actions:)

Presents an alert using the given data to produce the alert’s content and a
string variable as a title.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func alert<S, A, T>(
        _ title: S,
        isPresented: Binding<Bool>,
        presenting data: T?,
        @ViewBuilder actions: (T) -> A
    ) -> some View where S : StringProtocol, A : View
    

##  Parameters

`title`

    

A text string used as the title of the alert.

`isPresented`

    

A binding to a Boolean value that determines whether to present the alert.
When the user presses or taps one of the alert’s actions, the system sets this
value to `false` and dismisses.

`data`

    

An optional source of truth for the alert. The system passes the contents to
the modifier’s closures. You use this data to populate the fields of an alert
that you create that the system displays to the user.

`actions`

    

A `ViewBuilder` returning the alert’s actions given the currently available
data.

## Discussion

For the alert to appear, both `isPresented` must be `true` and `data` must not
be `nil`. The data should not change after the presentation occurs. Any
changes that you make after the presentation occurs are ignored.

Use this method when you need to populate the fields of an alert with content
from a data source. The example below shows a custom data source,
`SaveDetails`, that provides data to populate the alert:

All actions in an alert dismiss the alert after the action runs. The default
button is shown with greater prominence. You can influence the default button
by assigning it the `defaultAction` keyboard shortcut.

The system may reorder the buttons based on their role and prominence.

If no actions are present, the system includes a standard “OK” action. No
default cancel action is provided. If you want to show a cancel action, use a
button with a role of `cancel`.

On iOS, tvOS, and watchOS, alerts only support controls with labels that are
`Text`. Passing any other type of view results in the content being omitted.

## See Also

### Presenting an alert

`func alert<S, A>(S, isPresented: Binding<Bool>, actions: () -> A) -> some
View`

Presents an alert when a given condition is true, using a string variable as a
title.

`func alert<A>(Text, isPresented: Binding<Bool>, actions: () -> A) -> some
View`

Presents an alert when a given condition is true, using a text view for the
title.

`func alert<A>(LocalizedStringKey, isPresented: Binding<Bool>, actions: () ->
A) -> some View`

Presents an alert when a given condition is true, using a localized string key
for the title.

`func alert<A, T>(Text, isPresented: Binding<Bool>, presenting: T?, actions:
(T) -> A) -> some View`

Presents an alert using the given data to produce the alert’s content and a
text view as a title.

`func alert<A, T>(LocalizedStringKey, isPresented: Binding<Bool>, presenting:
T?, actions: (T) -> A) -> some View`

Presents an alert using the given data to produce the alert’s content and a
localized string key for a title.

`func alert<E, A>(isPresented: Binding<Bool>, error: E?, actions: () -> A) ->
some View`

Presents an alert when an error is present.

Instance Method

# alert(isPresented:error:actions:)

Presents an alert when an error is present.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func alert<E, A>(
        isPresented: Binding<Bool>,
        error: E?,
        @ViewBuilder actions: () -> A
    ) -> some View where E : LocalizedError, A : View
    

##  Parameters

`isPresented`

    

A binding to a Boolean value that determines whether to present the alert.
When the user presses or taps one of the alert’s actions, the system sets this
value to `false` and dismisses.

`error`

    

An optional localized Error that is used to generate the alert’s title. The
system passes the contents to the modifier’s closures. You use this data to
populate the fields of an alert that you create that the system displays to
the user.

`actions`

    

A `ViewBuilder` returning the alert’s actions.

## Discussion

In the example below, a form conditionally presents an alert depending upon
the value of an error. When the error value isn’t `nil`, the system presents
an alert with an “OK” action.

The title of the alert is inferred from the error’s `errorDescription`.

All actions in an alert dismiss the alert after the action runs. The default
button is shown with greater prominence. You can influence the default button
by assigning it the `defaultAction` keyboard shortcut.

The system may reorder the buttons based on their role and prominence.

If no actions are present, the system includes a standard “OK” action. No
default cancel action is provided. If you want to show a cancel action, use a
button with a role of `cancel`.

On iOS, tvOS, and watchOS, alerts only support controls with labels that are
`Text`. Passing any other type of view results in the content being omitted.

This modifier creates a `Text` view for the title on your behalf, and treats
the localized key similar to `init(_:tableName:bundle:comment:)`. See `Text`
for more information about localizing strings.

## See Also

### Presenting an alert

`func alert<S, A>(S, isPresented: Binding<Bool>, actions: () -> A) -> some
View`

Presents an alert when a given condition is true, using a string variable as a
title.

`func alert<A>(Text, isPresented: Binding<Bool>, actions: () -> A) -> some
View`

Presents an alert when a given condition is true, using a text view for the
title.

`func alert<A>(LocalizedStringKey, isPresented: Binding<Bool>, actions: () ->
A) -> some View`

Presents an alert when a given condition is true, using a localized string key
for the title.

`func alert<A, T>(Text, isPresented: Binding<Bool>, presenting: T?, actions:
(T) -> A) -> some View`

Presents an alert using the given data to produce the alert’s content and a
text view as a title.

`func alert<A, T>(LocalizedStringKey, isPresented: Binding<Bool>, presenting:
T?, actions: (T) -> A) -> some View`

Presents an alert using the given data to produce the alert’s content and a
localized string key for a title.

`func alert<S, A, T>(S, isPresented: Binding<Bool>, presenting: T?, actions:
(T) -> A) -> some View`

Presents an alert using the given data to produce the alert’s content and a
string variable as a title.

Instance Method

# alert(_:isPresented:actions:message:)

Presents an alert with a message when a given condition is true using a string
variable as a title.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func alert<S, A, M>(
        _ title: S,
        isPresented: Binding<Bool>,
        @ViewBuilder actions: () -> A,
        @ViewBuilder message: () -> M
    ) -> some View where S : StringProtocol, A : View, M : View
    

##  Parameters

`title`

    

A text string used as the title of the alert.

`isPresented`

    

A binding to a Boolean value that determines whether to present the alert.
When the user presses or taps one of the alert’s actions, the system sets this
value to `false` and dismisses.

`actions`

    

A `ViewBuilder` returning the alert’s actions.

`message`

    

A `ViewBuilder` returning the message for the alert.

## Discussion

In the example below, a login form conditionally presents an alert by setting
the `didFail` state variable. When the form sets the value to to `true`, the
system displays an alert with an “OK” action.

All actions in an alert dismiss the alert after the action runs. The default
button is shown with greater prominence. You can influence the default button
by assigning it the `defaultAction` keyboard shortcut.

The system may reorder the buttons based on their role and prominence.

If no actions are present, the system includes a standard “OK” action. No
default cancel action is provided. If you want to show a cancel action, use a
button with a role of `cancel`.

On iOS, tvOS, and watchOS, alerts only support controls with labels that are
`Text`. Passing any other type of view results in the content being omitted.

Only unstyled text is supported for the message.

## See Also

### Presenting an alert with a message

`func alert<A, M>(LocalizedStringKey, isPresented: Binding<Bool>, actions: ()
-> A, message: () -> M) -> some View`

Presents an alert with a message when a given condition is true, using a
localized string key for a title.

`func alert<A, M>(Text, isPresented: Binding<Bool>, actions: () -> A, message:
() -> M) -> some View`

Presents an alert with a message when a given condition is true using a text
view as a title.

`func alert<A, M, T>(LocalizedStringKey, isPresented: Binding<Bool>,
presenting: T?, actions: (T) -> A, message: (T) -> M) -> some View`

Presents an alert with a message using the given data to produce the alert’s
content and a localized string key for a title.

`func alert<A, M, T>(Text, isPresented: Binding<Bool>, presenting: T?,
actions: (T) -> A, message: (T) -> M) -> some View`

Presents an alert with a message using the given data to produce the alert’s
content and a text view for a title.

`func alert<S, A, M, T>(S, isPresented: Binding<Bool>, presenting: T?,
actions: (T) -> A, message: (T) -> M) -> some View`

Presents an alert with a message using the given data to produce the alert’s
content and a string variable as a title.

`func alert<E, A, M>(isPresented: Binding<Bool>, error: E?, actions: (E) -> A,
message: (E) -> M) -> some View`

Presents an alert with a message when an error is present.

Instance Method

# alert(_:isPresented:actions:message:)

Presents an alert with a message when a given condition is true, using a
localized string key for a title.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func alert<A, M>(
        _ titleKey: LocalizedStringKey,
        isPresented: Binding<Bool>,
        @ViewBuilder actions: () -> A,
        @ViewBuilder message: () -> M
    ) -> some View where A : View, M : View
    

##  Parameters

`titleKey`

    

The key for the localized string that describes the title of the alert.

`isPresented`

    

A binding to a Boolean value that determines whether to present the alert.
When the user presses or taps one of the alert’s actions, the system sets this
value to `false` and dismisses.

`actions`

    

A `ViewBuilder` returning the alert’s actions.

`message`

    

A `ViewBuilder` returning the message for the alert.

## Discussion

In the example below, a login form conditionally presents an alert by setting
the `didFail` state variable. When the form sets the value to to `true`, the
system displays an alert with an “OK” action.

All actions in an alert dismiss the alert after the action runs. The default
button is shown with greater prominence. You can influence the default button
by assigning it the `defaultAction` keyboard shortcut.

The system may reorder the buttons based on their role and prominence.

If no actions are present, the system includes a standard “OK” action. No
default cancel action is provided. If you want to show a cancel action, use a
button with a role of `cancel`.

On iOS, tvOS, and watchOS, alerts only support controls with labels that are
`Text`. Passing any other type of view results in the content being omitted.

Only unstyled text is supported for the message.

This modifier creates a `Text` view for the title on your behalf, and treats
the localized key similar to `init(_:tableName:bundle:comment:)`. See `Text`
for more information about localizing strings.

## See Also

### Presenting an alert with a message

`func alert<S, A, M>(S, isPresented: Binding<Bool>, actions: () -> A, message:
() -> M) -> some View`

Presents an alert with a message when a given condition is true using a string
variable as a title.

`func alert<A, M>(Text, isPresented: Binding<Bool>, actions: () -> A, message:
() -> M) -> some View`

Presents an alert with a message when a given condition is true using a text
view as a title.

`func alert<A, M, T>(LocalizedStringKey, isPresented: Binding<Bool>,
presenting: T?, actions: (T) -> A, message: (T) -> M) -> some View`

Presents an alert with a message using the given data to produce the alert’s
content and a localized string key for a title.

`func alert<A, M, T>(Text, isPresented: Binding<Bool>, presenting: T?,
actions: (T) -> A, message: (T) -> M) -> some View`

Presents an alert with a message using the given data to produce the alert’s
content and a text view for a title.

`func alert<S, A, M, T>(S, isPresented: Binding<Bool>, presenting: T?,
actions: (T) -> A, message: (T) -> M) -> some View`

Presents an alert with a message using the given data to produce the alert’s
content and a string variable as a title.

`func alert<E, A, M>(isPresented: Binding<Bool>, error: E?, actions: (E) -> A,
message: (E) -> M) -> some View`

Presents an alert with a message when an error is present.

Instance Method

# alert(_:isPresented:actions:message:)

Presents an alert with a message when a given condition is true using a text
view as a title.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func alert<A, M>(
        _ title: Text,
        isPresented: Binding<Bool>,
        @ViewBuilder actions: () -> A,
        @ViewBuilder message: () -> M
    ) -> some View where A : View, M : View
    

##  Parameters

`title`

    

The title of the alert.

`isPresented`

    

A binding to a Boolean value that determines whether to present the alert.
When the user presses or taps one of the alert’s actions, the system sets this
value to `false` and dismisses.

`actions`

    

A `ViewBuilder` returning the alert’s actions.

`message`

    

A `ViewBuilder` returning the message for the alert.

## Discussion

In the example below, a login form conditionally presents an alert by setting
the `didFail` state variable. When the form sets the value to to `true`, the
system displays an alert with an “OK” action.

All actions in an alert dismiss the alert after the action runs. The default
button is shown with greater prominence. You can influence the default button
by assigning it the `defaultAction` keyboard shortcut.

The system may reorder the buttons based on their role and prominence.

If no actions are present, the system includes a standard “OK” action. No
default cancel action is provided. If you want to show a cancel action, use a
button with a role of `cancel`.

On iOS, tvOS, and watchOS, alerts only support controls with labels that are
`Text`. Passing any other type of view results in the content being omitted.

Only unstyled text is supported for the message.

## See Also

### Presenting an alert with a message

`func alert<S, A, M>(S, isPresented: Binding<Bool>, actions: () -> A, message:
() -> M) -> some View`

Presents an alert with a message when a given condition is true using a string
variable as a title.

`func alert<A, M>(LocalizedStringKey, isPresented: Binding<Bool>, actions: ()
-> A, message: () -> M) -> some View`

Presents an alert with a message when a given condition is true, using a
localized string key for a title.

`func alert<A, M, T>(LocalizedStringKey, isPresented: Binding<Bool>,
presenting: T?, actions: (T) -> A, message: (T) -> M) -> some View`

Presents an alert with a message using the given data to produce the alert’s
content and a localized string key for a title.

`func alert<A, M, T>(Text, isPresented: Binding<Bool>, presenting: T?,
actions: (T) -> A, message: (T) -> M) -> some View`

Presents an alert with a message using the given data to produce the alert’s
content and a text view for a title.

`func alert<S, A, M, T>(S, isPresented: Binding<Bool>, presenting: T?,
actions: (T) -> A, message: (T) -> M) -> some View`

Presents an alert with a message using the given data to produce the alert’s
content and a string variable as a title.

`func alert<E, A, M>(isPresented: Binding<Bool>, error: E?, actions: (E) -> A,
message: (E) -> M) -> some View`

Presents an alert with a message when an error is present.

Instance Method

# alert(_:isPresented:presenting:actions:message:)

Presents an alert with a message using the given data to produce the alert’s
content and a localized string key for a title.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func alert<A, M, T>(
        _ titleKey: LocalizedStringKey,
        isPresented: Binding<Bool>,
        presenting data: T?,
        @ViewBuilder actions: (T) -> A,
        @ViewBuilder message: (T) -> M
    ) -> some View where A : View, M : View
    

##  Parameters

`titleKey`

    

The key for the localized string that describes the title of the alert.

`isPresented`

    

A binding to a Boolean value that determines whether to present the alert.
When the user presses or taps one of the alert’s actions, the system sets this
value to `false` and dismisses.

`data`

    

An optional source of truth for the alert. The system passes the contents to
the modifier’s closures. You use this data to populate the fields of an alert
that you create that the system displays to the user.

`actions`

    

A `ViewBuilder` returning the alert’s actions given the currently available
data.

`message`

    

A `ViewBuilder` returning the message for the alert given the currently
available data.

## Discussion

For the alert to appear, both `isPresented` must be `true` and `data` must not
be `nil`. The data should not change after the presentation occurs. Any
changes that you make after the presentation occurs are ignored.

Use this method when you need to populate the fields of an alert with content
from a data source. The example below shows a custom data source,
`SaveDetails`, that provides data to populate the alert:

This modifier creates a `Text` view for the title on your behalf, and treats
the localized key similar to `init(_:tableName:bundle:comment:)`. See `Text`
for more information about localizing strings.

All actions in an alert dismiss the alert after the action runs. The default
button is shown with greater prominence. You can influence the default button
by assigning it the `defaultAction` keyboard shortcut.

The system may reorder the buttons based on their role and prominence.

If no actions are present, the system includes a standard “OK” action. No
default cancel action is provided. If you want to show a cancel action, use a
button with a role of `cancel`.

On iOS, tvOS, and watchOS, alerts only support controls with labels that are
`Text`. Passing any other type of view results in the content being omitted.

Only unstyled text is supported for the message.

## See Also

### Presenting an alert with a message

`func alert<S, A, M>(S, isPresented: Binding<Bool>, actions: () -> A, message:
() -> M) -> some View`

Presents an alert with a message when a given condition is true using a string
variable as a title.

`func alert<A, M>(LocalizedStringKey, isPresented: Binding<Bool>, actions: ()
-> A, message: () -> M) -> some View`

Presents an alert with a message when a given condition is true, using a
localized string key for a title.

`func alert<A, M>(Text, isPresented: Binding<Bool>, actions: () -> A, message:
() -> M) -> some View`

Presents an alert with a message when a given condition is true using a text
view as a title.

`func alert<A, M, T>(Text, isPresented: Binding<Bool>, presenting: T?,
actions: (T) -> A, message: (T) -> M) -> some View`

Presents an alert with a message using the given data to produce the alert’s
content and a text view for a title.

`func alert<S, A, M, T>(S, isPresented: Binding<Bool>, presenting: T?,
actions: (T) -> A, message: (T) -> M) -> some View`

Presents an alert with a message using the given data to produce the alert’s
content and a string variable as a title.

`func alert<E, A, M>(isPresented: Binding<Bool>, error: E?, actions: (E) -> A,
message: (E) -> M) -> some View`

Presents an alert with a message when an error is present.

Instance Method

# alert(_:isPresented:presenting:actions:message:)

Presents an alert with a message using the given data to produce the alert’s
content and a text view for a title.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func alert<A, M, T>(
        _ title: Text,
        isPresented: Binding<Bool>,
        presenting data: T?,
        @ViewBuilder actions: (T) -> A,
        @ViewBuilder message: (T) -> M
    ) -> some View where A : View, M : View
    

##  Parameters

`title`

    

the title of the alert.

`isPresented`

    

A binding to a Boolean value that determines whether to present the alert.
When the user presses or taps one of the alert’s actions, the system sets this
value to `false` and dismisses.

`data`

    

An optional source of truth for the alert. The system passes the contents to
the modifier’s closures. You use this data to populate the fields of an alert
that you create that the system displays to the user.

`actions`

    

A `ViewBuilder` returning the alert’s actions given the currently available
data.

`message`

    

A `ViewBuilder` returning the message for the alert given the currently
available data.

## Discussion

For the alert to appear, both `isPresented` must be `true` and `data` must not
be `nil`. The data should not change after the presentation occurs. Any
changes that you make after the presentation occurs are ignored.

Use this method when you need to populate the fields of an alert with content
from a data source. The example below shows a custom data source,
`SaveDetails`, that provides data to populate the alert:

All actions in an alert dismiss the alert after the action runs. The default
button is shown with greater prominence. You can influence the default button
by assigning it the `defaultAction` keyboard shortcut.

The system may reorder the buttons based on their role and prominence.

If no actions are present, the system includes a standard “OK” action. No
default cancel action is provided. If you want to show a cancel action, use a
button with a role of `cancel`.

On iOS, tvOS, and watchOS, alerts only support controls with labels that are
`Text`. Passing any other type of view results in the content being omitted.

Only unstyled text is supported for the message.

## See Also

### Presenting an alert with a message

`func alert<S, A, M>(S, isPresented: Binding<Bool>, actions: () -> A, message:
() -> M) -> some View`

Presents an alert with a message when a given condition is true using a string
variable as a title.

`func alert<A, M>(LocalizedStringKey, isPresented: Binding<Bool>, actions: ()
-> A, message: () -> M) -> some View`

Presents an alert with a message when a given condition is true, using a
localized string key for a title.

`func alert<A, M>(Text, isPresented: Binding<Bool>, actions: () -> A, message:
() -> M) -> some View`

Presents an alert with a message when a given condition is true using a text
view as a title.

`func alert<A, M, T>(LocalizedStringKey, isPresented: Binding<Bool>,
presenting: T?, actions: (T) -> A, message: (T) -> M) -> some View`

Presents an alert with a message using the given data to produce the alert’s
content and a localized string key for a title.

`func alert<S, A, M, T>(S, isPresented: Binding<Bool>, presenting: T?,
actions: (T) -> A, message: (T) -> M) -> some View`

Presents an alert with a message using the given data to produce the alert’s
content and a string variable as a title.

`func alert<E, A, M>(isPresented: Binding<Bool>, error: E?, actions: (E) -> A,
message: (E) -> M) -> some View`

Presents an alert with a message when an error is present.

Instance Method

# alert(_:isPresented:presenting:actions:message:)

Presents an alert with a message using the given data to produce the alert’s
content and a string variable as a title.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func alert<S, A, M, T>(
        _ title: S,
        isPresented: Binding<Bool>,
        presenting data: T?,
        @ViewBuilder actions: (T) -> A,
        @ViewBuilder message: (T) -> M
    ) -> some View where S : StringProtocol, A : View, M : View
    

##  Parameters

`title`

    

A text string used as the title of the alert.

`isPresented`

    

A binding to a Boolean value that determines whether to present the alert.
When the user presses or taps one of the alert’s actions, the system sets this
value to `false` and dismisses.

`data`

    

An optional source of truth for the alert. The system passes the contents to
the modifier’s closures. You use this data to populate the fields of an alert
that you create that the system displays to the user.

`actions`

    

A `ViewBuilder` returning the alert’s actions given the currently available
data.

`message`

    

A `ViewBuilder` returning the message for the alert given the currently
available data.

## Discussion

For the alert to appear, both `isPresented` must be `true` and `data` must not
be `nil`. The data should not change after the presentation occurs. Any
changes that you make after the presentation occurs are ignored.

Use this method when you need to populate the fields of an alert with content
from a data source. The example below shows a custom data source,
`SaveDetails`, that provides data to populate the alert:

All actions in an alert dismiss the alert after the action runs. The default
button is shown with greater prominence. You can influence the default button
by assigning it the `defaultAction` keyboard shortcut.

The system may reorder the buttons based on their role and prominence.

If no actions are present, the system includes a standard “OK” action. No
default cancel action is provided. If you want to show a cancel action, use a
button with a role of `cancel`.

On iOS, tvOS, and watchOS, alerts only support controls with labels that are
`Text`. Passing any other type of view results in the content being omitted.

Only unstyled text is supported for the message.

## See Also

### Presenting an alert with a message

`func alert<S, A, M>(S, isPresented: Binding<Bool>, actions: () -> A, message:
() -> M) -> some View`

Presents an alert with a message when a given condition is true using a string
variable as a title.

`func alert<A, M>(LocalizedStringKey, isPresented: Binding<Bool>, actions: ()
-> A, message: () -> M) -> some View`

Presents an alert with a message when a given condition is true, using a
localized string key for a title.

`func alert<A, M>(Text, isPresented: Binding<Bool>, actions: () -> A, message:
() -> M) -> some View`

Presents an alert with a message when a given condition is true using a text
view as a title.

`func alert<A, M, T>(LocalizedStringKey, isPresented: Binding<Bool>,
presenting: T?, actions: (T) -> A, message: (T) -> M) -> some View`

Presents an alert with a message using the given data to produce the alert’s
content and a localized string key for a title.

`func alert<A, M, T>(Text, isPresented: Binding<Bool>, presenting: T?,
actions: (T) -> A, message: (T) -> M) -> some View`

Presents an alert with a message using the given data to produce the alert’s
content and a text view for a title.

`func alert<E, A, M>(isPresented: Binding<Bool>, error: E?, actions: (E) -> A,
message: (E) -> M) -> some View`

Presents an alert with a message when an error is present.

Instance Method

# alert(isPresented:error:actions:message:)

Presents an alert with a message when an error is present.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func alert<E, A, M>(
        isPresented: Binding<Bool>,
        error: E?,
        @ViewBuilder actions: (E) -> A,
        @ViewBuilder message: (E) -> M
    ) -> some View where E : LocalizedError, A : View, M : View
    

##  Parameters

`isPresented`

    

A binding to a Boolean value that determines whether to present the alert.
When the user presses or taps one of the alert’s actions, the system sets this
value to `false` and dismisses.

`error`

    

An optional localized Error that is used to generate the alert’s title. The
system passes the contents to the modifier’s closures. You use this data to
populate the fields of an alert that you create that the system displays to
the user.

`actions`

    

A `ViewBuilder` returning the alert’s actions.

`message`

    

A view builder returning the message for the alert given the current error.

## Discussion

In the example below, a form conditionally presents an alert depending upon
the value of an error. When the error value isn’t `nil`, the system presents
an alert with an “OK” action.

The title of the alert is inferred from the error’s `errorDescription`.

All actions in an alert dismiss the alert after the action runs. The default
button is shown with greater prominence. You can influence the default button
by assigning it the `defaultAction` keyboard shortcut.

The system may reorder the buttons based on their role and prominence.

If no actions are present, the system includes a standard “OK” action. No
default cancel action is provided. If you want to show a cancel action, use a
button with a role of `cancel`.

On iOS, tvOS, and watchOS, alerts only support controls with labels that are
`Text`. Passing any other type of view results in the content being omitted.

This modifier creates a `Text` view for the title on your behalf, and treats
the localized key similar to `init(_:tableName:bundle:comment:)`. See `Text`
for more information about localizing strings.

## See Also

### Presenting an alert with a message

`func alert<S, A, M>(S, isPresented: Binding<Bool>, actions: () -> A, message:
() -> M) -> some View`

Presents an alert with a message when a given condition is true using a string
variable as a title.

`func alert<A, M>(LocalizedStringKey, isPresented: Binding<Bool>, actions: ()
-> A, message: () -> M) -> some View`

Presents an alert with a message when a given condition is true, using a
localized string key for a title.

`func alert<A, M>(Text, isPresented: Binding<Bool>, actions: () -> A, message:
() -> M) -> some View`

Presents an alert with a message when a given condition is true using a text
view as a title.

`func alert<A, M, T>(LocalizedStringKey, isPresented: Binding<Bool>,
presenting: T?, actions: (T) -> A, message: (T) -> M) -> some View`

Presents an alert with a message using the given data to produce the alert’s
content and a localized string key for a title.

`func alert<A, M, T>(Text, isPresented: Binding<Bool>, presenting: T?,
actions: (T) -> A, message: (T) -> M) -> some View`

Presents an alert with a message using the given data to produce the alert’s
content and a text view for a title.

`func alert<S, A, M, T>(S, isPresented: Binding<Bool>, presenting: T?,
actions: (T) -> A, message: (T) -> M) -> some View`

Presents an alert with a message using the given data to produce the alert’s
content and a string variable as a title.

Instance Method

# confirmationDialog(_:isPresented:titleVisibility:actions:)

Presents a confirmation dialog when a given condition is true, using a string
variable as a title.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func confirmationDialog<S, A>(
        _ title: S,
        isPresented: Binding<Bool>,
        titleVisibility: Visibility = .automatic,
        @ViewBuilder actions: () -> A
    ) -> some View where S : StringProtocol, A : View
    

##  Parameters

`title`

    

A text string used as the title of the dialog.

`isPresented`

    

A binding to a Boolean value that determines whether to present the dialog.
When the user presses or taps the dialog’s default action button, the system
sets this value to `false`, dismissing the dialog.

`titleVisibility`

    

The visibility of the dialog’s title. The default value is
`Visibility.automatic`.

`actions`

    

A view builder returning the dialog’s actions.

## Discussion

In the example below, a button conditionally presents a confirmation dialog
depending upon the value of a bound Boolean variable. When the Boolean value
is set to `true`, the system displays a confirmation dialog with a cancel
action and a destructive action.

All actions in a confirmation dialog will dismiss the dialog after the action
runs. The default button will be shown with greater prominence. You can
influence the default button by assigning it the `defaultAction` keyboard
shortcut.

The system may reorder the buttons based on their role and prominence.

Dialogs include a standard dismiss action by default. If you provide a button
with a role of `cancel`, that button takes the place of the default dismiss
action. You don’t have to dismiss the presentation with the cancel button’s
action.

Note

In regular size classes in iOS, the system renders confirmation dialogs as a
popover that the user dismisses by tapping anywhere outside the popover,
rather than displaying the standard dismiss action.

## See Also

### Getting confirmation for an action

`func confirmationDialog<A>(Text, isPresented: Binding<Bool>, titleVisibility:
Visibility, actions: () -> A) -> some View`

Presents a confirmation dialog when a given condition is true, using a text
view for the title.

`func confirmationDialog<A>(LocalizedStringKey, isPresented: Binding<Bool>,
titleVisibility: Visibility, actions: () -> A) -> some View`

Presents a confirmation dialog when a given condition is true, using a
localized string key for the title.

`func confirmationDialog<A, T>(Text, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A) -> some View`

Presents a confirmation dialog using data to produce the dialog’s content and
a text view for the title.

`func confirmationDialog<A, T>(LocalizedStringKey, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A) -> some View`

Presents a confirmation dialog using data to produce the dialog’s content and
a localized string key for the title.

`func confirmationDialog<S, A, T>(S, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A) -> some View`

Presents a confirmation dialog using data to produce the dialog’s content and
a string variable for the title.

Instance Method

# confirmationDialog(_:isPresented:titleVisibility:actions:)

Presents a confirmation dialog when a given condition is true, using a text
view for the title.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func confirmationDialog<A>(
        _ title: Text,
        isPresented: Binding<Bool>,
        titleVisibility: Visibility = .automatic,
        @ViewBuilder actions: () -> A
    ) -> some View where A : View
    

##  Parameters

`title`

    

the title of the dialog.

`isPresented`

    

A binding to a Boolean value that determines whether to present the dialog.
When the user presses or taps the dialog’s default action button, the system
sets this value to `false`, dismissing the dialog.

`titleVisibility`

    

The visibility of the dialog’s title. The default value is
`Visibility.automatic`.

`actions`

    

A view builder returning the dialog’s actions.

## Discussion

In the example below, a button conditionally presents a confirmation dialog
depending upon the value of a bound Boolean variable. When the Boolean value
is set to `true`, the system displays a confirmation dialog with a cancel
action and a destructive action.

All actions in a confirmation dialog will dismiss the dialog after the action
runs. The default button will be shown with greater prominence. You can
influence the default button by assigning it the `defaultAction` keyboard
shortcut.

The system may reorder the buttons based on their role and prominence.

Dialogs include a standard dismiss action by default. If you provide a button
with a role of `cancel`, that button takes the place of the default dismiss
action. You don’t have to dismiss the presentation with the cancel button’s
action.

Note

In regular size classes in iOS, the system renders confirmation dialogs as a
popover that the user dismisses by tapping anywhere outside the popover,
rather than displaying the standard dismiss action.

## See Also

### Getting confirmation for an action

`func confirmationDialog<S, A>(S, isPresented: Binding<Bool>, titleVisibility:
Visibility, actions: () -> A) -> some View`

Presents a confirmation dialog when a given condition is true, using a string
variable as a title.

`func confirmationDialog<A>(LocalizedStringKey, isPresented: Binding<Bool>,
titleVisibility: Visibility, actions: () -> A) -> some View`

Presents a confirmation dialog when a given condition is true, using a
localized string key for the title.

`func confirmationDialog<A, T>(Text, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A) -> some View`

Presents a confirmation dialog using data to produce the dialog’s content and
a text view for the title.

`func confirmationDialog<A, T>(LocalizedStringKey, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A) -> some View`

Presents a confirmation dialog using data to produce the dialog’s content and
a localized string key for the title.

`func confirmationDialog<S, A, T>(S, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A) -> some View`

Presents a confirmation dialog using data to produce the dialog’s content and
a string variable for the title.

Instance Method

# confirmationDialog(_:isPresented:titleVisibility:actions:)

Presents a confirmation dialog when a given condition is true, using a
localized string key for the title.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func confirmationDialog<A>(
        _ titleKey: LocalizedStringKey,
        isPresented: Binding<Bool>,
        titleVisibility: Visibility = .automatic,
        @ViewBuilder actions: () -> A
    ) -> some View where A : View
    

##  Parameters

`titleKey`

    

The key for the localized string that describes the title of the dialog.

`isPresented`

    

A binding to a Boolean value that determines whether to present the dialog.
When the user presses or taps the dialog’s default action button, the system
sets this value to `false`, dismissing the dialog.

`titleVisibility`

    

The visibility of the dialog’s title. The default value is
`Visibility.automatic`.

`actions`

    

A view builder returning the dialog’s actions.

## Discussion

In the example below, a button conditionally presents a confirmation dialog
depending upon the value of a bound Boolean variable. When the Boolean value
is set to `true`, the system displays a confirmation dialog with a cancel
action and a destructive action.

All actions in a confirmation dialog will dismiss the dialog after the action
runs. The default button will be shown with greater prominence. You can
influence the default button by assigning it the `defaultAction` keyboard
shortcut.

The system may reorder the buttons based on their role and prominence.

Dialogs include a standard dismiss action by default. If you provide a button
with a role of `cancel`, that button takes the place of the default dismiss
action. You don’t have to dismiss the presentation with the cancel button’s
action.

Note

In regular size classes in iOS, the system renders confirmation dialogs as a
popover that the user dismisses by tapping anywhere outside the popover,
rather than displaying the standard dismiss action.

On iOS, tvOS, and watchOS, confirmation dialogs only support controls with
labels that are `Text`. Passing any other type of view results in the content
being omitted.

This modifier creates a `Text` view for the title on your behalf, and treats
the localized key similar to `init(_:tableName:bundle:comment:)`. See `Text`
for more information about localizing strings.

## See Also

### Getting confirmation for an action

`func confirmationDialog<S, A>(S, isPresented: Binding<Bool>, titleVisibility:
Visibility, actions: () -> A) -> some View`

Presents a confirmation dialog when a given condition is true, using a string
variable as a title.

`func confirmationDialog<A>(Text, isPresented: Binding<Bool>, titleVisibility:
Visibility, actions: () -> A) -> some View`

Presents a confirmation dialog when a given condition is true, using a text
view for the title.

`func confirmationDialog<A, T>(Text, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A) -> some View`

Presents a confirmation dialog using data to produce the dialog’s content and
a text view for the title.

`func confirmationDialog<A, T>(LocalizedStringKey, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A) -> some View`

Presents a confirmation dialog using data to produce the dialog’s content and
a localized string key for the title.

`func confirmationDialog<S, A, T>(S, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A) -> some View`

Presents a confirmation dialog using data to produce the dialog’s content and
a string variable for the title.

Instance Method

# confirmationDialog(_:isPresented:titleVisibility:presenting:actions:)

Presents a confirmation dialog using data to produce the dialog’s content and
a text view for the title.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func confirmationDialog<A, T>(
        _ title: Text,
        isPresented: Binding<Bool>,
        titleVisibility: Visibility = .automatic,
        presenting data: T?,
        @ViewBuilder actions: (T) -> A
    ) -> some View where A : View
    

##  Parameters

`title`

    

the title of the dialog.

`isPresented`

    

A binding to a Boolean value that determines whether to present the dialog.
When the user presses or taps the dialog’s default action button, the system
sets this value to `false`, dismissing the dialog.

`titleVisibility`

    

The visibility of the dialog’s title. The default value is
`Visibility.automatic`.

`data`

    

An optional source of truth for the confirmation dialog. The system passes the
contents to the modifier’s closures. You use this data to populate the fields
of a confirmation dialog that you create that the system displays to the user.

`actions`

    

A view builder returning the dialog’s actions given the currently available
data.

## Discussion

In order for the interface to appear, both `isPresented` must be `true` and
`data` must not be `nil`. `data` should not change after the presentation
occurs. Any changes which occur after the presentation occurs will be ignored.

Use this method when you need to populate the fields of a confirmation dialog
with content from a data source. The example below shows a custom data source,
`FileDetails`, that provides data to populate the dialog:

All actions in a confirmation dialog will dismiss the dialog after the action
runs. The default button will be shown with greater prominence. You can
influence the default button by assigning it the `defaultAction` keyboard
shortcut.

The system may reorder the buttons based on their role and prominence.

Dialogs include a standard dismiss action by default. If you provide a button
with a role of `cancel`, that button takes the place of the default dismiss
action. You don’t have to dismiss the presentation with the cancel button’s
action.

Note

In regular size classes in iOS, the system renders confirmation dialogs as a
popover that the user dismisses by tapping anywhere outside the popover,
rather than displaying the standard dismiss action.

On iOS, tvOS, and watchOS, confirmation dialogs only support controls with
labels that are `Text`. Passing any other type of view results in the content
being omitted.

## See Also

### Getting confirmation for an action

`func confirmationDialog<S, A>(S, isPresented: Binding<Bool>, titleVisibility:
Visibility, actions: () -> A) -> some View`

Presents a confirmation dialog when a given condition is true, using a string
variable as a title.

`func confirmationDialog<A>(Text, isPresented: Binding<Bool>, titleVisibility:
Visibility, actions: () -> A) -> some View`

Presents a confirmation dialog when a given condition is true, using a text
view for the title.

`func confirmationDialog<A>(LocalizedStringKey, isPresented: Binding<Bool>,
titleVisibility: Visibility, actions: () -> A) -> some View`

Presents a confirmation dialog when a given condition is true, using a
localized string key for the title.

`func confirmationDialog<A, T>(LocalizedStringKey, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A) -> some View`

Presents a confirmation dialog using data to produce the dialog’s content and
a localized string key for the title.

`func confirmationDialog<S, A, T>(S, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A) -> some View`

Presents a confirmation dialog using data to produce the dialog’s content and
a string variable for the title.

Instance Method

# confirmationDialog(_:isPresented:titleVisibility:presenting:actions:)

Presents a confirmation dialog using data to produce the dialog’s content and
a localized string key for the title.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func confirmationDialog<A, T>(
        _ titleKey: LocalizedStringKey,
        isPresented: Binding<Bool>,
        titleVisibility: Visibility = .automatic,
        presenting data: T?,
        @ViewBuilder actions: (T) -> A
    ) -> some View where A : View
    

##  Parameters

`titleKey`

    

The key for the localized string that describes the title of the dialog.

`isPresented`

    

A binding to a Boolean value that determines whether to present the dialog.
When the user presses or taps the dialog’s default action button, the system
sets this value to `false`, dismissing the dialog.

`titleVisibility`

    

The visibility of the dialog’s title. The default value is
`Visibility.automatic`.

`data`

    

An optional source of truth for the confirmation dialog. The system passes the
contents to the modifier’s closures. You use this data to populate the fields
of a confirmation dialog that you create that the system displays to the user.

`actions`

    

A view builder returning the dialog’s actions given the currently available
data.

## Discussion

In order for the interface to appear, both `isPresented` must be `true` and
`data` must not be `nil`. `data` should not change after the presentation
occurs. Any changes which occur after the presentation occurs will be ignored.

Use this method when you need to populate the fields of a confirmation dialog
with content from a data source. The example below shows a custom data source,
`FileDetails`, that provides data to populate the dialog:

This modifier creates a `Text` view for the title on your behalf, and treats
the localized key similar to `init(_:tableName:bundle:comment:)`. See `Text`
for more information about localizing strings.

All actions in a confirmation dialog will dismiss the dialog after the action
runs. The default button will be shown with greater prominence. You can
influence the default button by assigning it the `defaultAction` keyboard
shortcut.

The system may reorder the buttons based on their role and prominence.

Dialogs include a standard dismiss action by default. If you provide a button
with a role of `cancel`, that button takes the place of the default dismiss
action. You don’t have to dismiss the presentation with the cancel button’s
action.

Note

In regular size classes in iOS, the system renders confirmation dialogs as a
popover that the user dismisses by tapping anywhere outside the popover,
rather than displaying the standard dismiss action.

On iOS, tvOS, and watchOS, confirmation dialogs only support controls with
labels that are `Text`. Passing any other type of view results in the content
being omitted.

## See Also

### Getting confirmation for an action

`func confirmationDialog<S, A>(S, isPresented: Binding<Bool>, titleVisibility:
Visibility, actions: () -> A) -> some View`

Presents a confirmation dialog when a given condition is true, using a string
variable as a title.

`func confirmationDialog<A>(Text, isPresented: Binding<Bool>, titleVisibility:
Visibility, actions: () -> A) -> some View`

Presents a confirmation dialog when a given condition is true, using a text
view for the title.

`func confirmationDialog<A>(LocalizedStringKey, isPresented: Binding<Bool>,
titleVisibility: Visibility, actions: () -> A) -> some View`

Presents a confirmation dialog when a given condition is true, using a
localized string key for the title.

`func confirmationDialog<A, T>(Text, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A) -> some View`

Presents a confirmation dialog using data to produce the dialog’s content and
a text view for the title.

`func confirmationDialog<S, A, T>(S, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A) -> some View`

Presents a confirmation dialog using data to produce the dialog’s content and
a string variable for the title.

Instance Method

# confirmationDialog(_:isPresented:titleVisibility:presenting:actions:)

Presents a confirmation dialog using data to produce the dialog’s content and
a string variable for the title.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func confirmationDialog<S, A, T>(
        _ title: S,
        isPresented: Binding<Bool>,
        titleVisibility: Visibility = .automatic,
        presenting data: T?,
        @ViewBuilder actions: (T) -> A
    ) -> some View where S : StringProtocol, A : View
    

##  Parameters

`title`

    

A text string used as the title of the dialog.

`isPresented`

    

A binding to a Boolean value that determines whether to present the dialog.
When the user presses or taps the dialog’s default action button, the system
sets this value to `false`, dismissing the dialog.

`titleVisibility`

    

The visibility of the dialog’s title. The default value is
`Visibility.automatic`.

`data`

    

An optional source of truth for the confirmation dialog. The system passes the
contents to the modifier’s closures. You use this data to populate the fields
of a confirmation dialog that you create that the system displays to the user.

`actions`

    

A view builder returning the dialog’s actions given the currently available
data.

## Discussion

In order for the interface to appear, both `isPresented` must be `true` and
`data` must not be `nil`. `data` should not change after the presentation
occurs. Any changes which occur after the presentation occurs will be ignored.

Use this method when you need to populate the fields of a confirmation dialog
with content from a data source. The example below shows a custom data source,
`FileDetails`, that provides data to populate the dialog:

All actions in a confirmation dialog will dismiss the dialog after the action
runs. The default button will be shown with greater prominence. You can
influence the default button by assigning it the `defaultAction` keyboard
shortcut.

The system may reorder the buttons based on their role and prominence.

Dialogs include a standard dismiss action by default. If you provide a button
with a role of `cancel`, that button takes the place of the default dismiss
action. You don’t have to dismiss the presentation with the cancel button’s
action.

Note

In regular size classes in iOS, the system renders confirmation dialogs as a
popover that the user dismisses by tapping anywhere outside the popover,
rather than displaying the standard dismiss action.

On iOS, tvOS, and watchOS, confirmation dialogs only support controls with
labels that are `Text`. Passing any other type of view results in the content
being omitted.

## See Also

### Getting confirmation for an action

`func confirmationDialog<S, A>(S, isPresented: Binding<Bool>, titleVisibility:
Visibility, actions: () -> A) -> some View`

Presents a confirmation dialog when a given condition is true, using a string
variable as a title.

`func confirmationDialog<A>(Text, isPresented: Binding<Bool>, titleVisibility:
Visibility, actions: () -> A) -> some View`

Presents a confirmation dialog when a given condition is true, using a text
view for the title.

`func confirmationDialog<A>(LocalizedStringKey, isPresented: Binding<Bool>,
titleVisibility: Visibility, actions: () -> A) -> some View`

Presents a confirmation dialog when a given condition is true, using a
localized string key for the title.

`func confirmationDialog<A, T>(Text, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A) -> some View`

Presents a confirmation dialog using data to produce the dialog’s content and
a text view for the title.

`func confirmationDialog<A, T>(LocalizedStringKey, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A) -> some View`

Presents a confirmation dialog using data to produce the dialog’s content and
a localized string key for the title.

Instance Method

# confirmationDialog(_:isPresented:titleVisibility:actions:message:)

Presents a confirmation dialog with a message when a given condition is true,
using a string variable for the title.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func confirmationDialog<S, A, M>(
        _ title: S,
        isPresented: Binding<Bool>,
        titleVisibility: Visibility = .automatic,
        @ViewBuilder actions: () -> A,
        @ViewBuilder message: () -> M
    ) -> some View where S : StringProtocol, A : View, M : View
    

##  Parameters

`title`

    

A text string used as the title of the dialog.

`isPresented`

    

A binding to a Boolean value that determines whether to present the dialog.
When the user presses or taps the dialog’s default action button, the system
sets this value to `false`, dismissing the dialog.

`titleVisibility`

    

The visibility of the dialog’s title. The default value is
`Visibility.automatic`.

`actions`

    

A view builder returning the dialog’s actions.

`message`

    

A view builder returning the message for the dialog.

## Discussion

In the example below, a button conditionally presents a confirmation dialog
depending upon the value of a bound Boolean variable. When the Boolean value
is set to `true`, the system displays a confirmation dialog with a cancel
action and a destructive action.

All actions in a confirmation dialog will dismiss the dialog after the action
runs. The default button will be shown with greater prominence. You can
influence the default button by assigning it the `defaultAction` keyboard
shortcut.

The system may reorder the buttons based on their role and prominence.

Dialogs include a standard dismiss action by default. If you provide a button
with a role of `cancel`, that button takes the place of the default dismiss
action. You don’t have to dismiss the presentation with the cancel button’s
action.

Note

In regular size classes in iOS, the system renders confirmation dialogs as a
popover that the user dismisses by tapping anywhere outside the popover,
rather than displaying the standard dismiss action.

## See Also

### Showing a confirmation dialog with a message

`func confirmationDialog<A, M>(LocalizedStringKey, isPresented: Binding<Bool>,
titleVisibility: Visibility, actions: () -> A, message: () -> M) -> some View`

Presents a confirmation dialog with a message when a given condition is true,
using a localized string key for the title.

`func confirmationDialog<A, M>(Text, isPresented: Binding<Bool>,
titleVisibility: Visibility, actions: () -> A, message: () -> M) -> some View`

Presents a confirmation dialog with a message when a given condition is true,
using a text view for the title.

`func confirmationDialog<A, M, T>(Text, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A, message: (T)
-> M) -> some View`

Presents a confirmation dialog with a message using data to produce the
dialog’s content and a text view for the message.

`func confirmationDialog<S, A, M, T>(S, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A, message: (T)
-> M) -> some View`

Presents a confirmation dialog with a message using data to produce the
dialog’s content and a string variable for the title.

`func confirmationDialog<A, M, T>(LocalizedStringKey, isPresented:
Binding<Bool>, titleVisibility: Visibility, presenting: T?, actions: (T) -> A,
message: (T) -> M) -> some View`

Presents a confirmation dialog with a message using data to produce the
dialog’s content and a localized string key for the title.

Instance Method

# confirmationDialog(_:isPresented:titleVisibility:actions:message:)

Presents a confirmation dialog with a message when a given condition is true,
using a localized string key for the title.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func confirmationDialog<A, M>(
        _ titleKey: LocalizedStringKey,
        isPresented: Binding<Bool>,
        titleVisibility: Visibility = .automatic,
        @ViewBuilder actions: () -> A,
        @ViewBuilder message: () -> M
    ) -> some View where A : View, M : View
    

##  Parameters

`titleKey`

    

The key for the localized string that describes the title of the dialog.

`isPresented`

    

A binding to a Boolean value that determines whether to present the dialog.
When the user presses or taps the dialog’s default action button, the system
sets this value to `false`, dismissing the dialog.

`titleVisibility`

    

The visibility of the dialog’s title. The default value is
`Visibility.automatic`.

`actions`

    

A view builder returning the dialog’s actions.

`message`

    

A view builder returning the message for the dialog.

## Discussion

In the example below, a button conditionally presents a confirmation dialog
depending upon the value of a bound Boolean variable. When the Boolean value
is set to `true`, the system displays a confirmation dialog with a cancel
action and a destructive action.

All actions in a confirmation dialog will dismiss the dialog after the action
runs. The default button will be shown with greater prominence. You can
influence the default button by assigning it the `defaultAction` keyboard
shortcut.

The system may reorder the buttons based on their role and prominence.

Dialogs include a standard dismiss action by default. If you provide a button
with a role of `cancel`, that button takes the place of the default dismiss
action. You don’t have to dismiss the presentation with the cancel button’s
action.

Note

In regular size classes in iOS, the system renders confirmation dialogs as a
popover that the user dismisses by tapping anywhere outside the popover,
rather than displaying the standard dismiss action.

On iOS, tvOS, and watchOS, confirmation dialogs only support controls with
labels that are `Text`. Passing any other type of view results in the content
being omitted.

This modifier creates a `Text` view for the title on your behalf, and treats
the localized key similar to `init(_:tableName:bundle:comment:)`. See `Text`
for more information about localizing strings.

## See Also

### Showing a confirmation dialog with a message

`func confirmationDialog<S, A, M>(S, isPresented: Binding<Bool>,
titleVisibility: Visibility, actions: () -> A, message: () -> M) -> some View`

Presents a confirmation dialog with a message when a given condition is true,
using a string variable for the title.

`func confirmationDialog<A, M>(Text, isPresented: Binding<Bool>,
titleVisibility: Visibility, actions: () -> A, message: () -> M) -> some View`

Presents a confirmation dialog with a message when a given condition is true,
using a text view for the title.

`func confirmationDialog<A, M, T>(Text, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A, message: (T)
-> M) -> some View`

Presents a confirmation dialog with a message using data to produce the
dialog’s content and a text view for the message.

`func confirmationDialog<S, A, M, T>(S, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A, message: (T)
-> M) -> some View`

Presents a confirmation dialog with a message using data to produce the
dialog’s content and a string variable for the title.

`func confirmationDialog<A, M, T>(LocalizedStringKey, isPresented:
Binding<Bool>, titleVisibility: Visibility, presenting: T?, actions: (T) -> A,
message: (T) -> M) -> some View`

Presents a confirmation dialog with a message using data to produce the
dialog’s content and a localized string key for the title.

Instance Method

# confirmationDialog(_:isPresented:titleVisibility:actions:message:)

Presents a confirmation dialog with a message when a given condition is true,
using a text view for the title.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func confirmationDialog<A, M>(
        _ title: Text,
        isPresented: Binding<Bool>,
        titleVisibility: Visibility = .automatic,
        @ViewBuilder actions: () -> A,
        @ViewBuilder message: () -> M
    ) -> some View where A : View, M : View
    

##  Parameters

`title`

    

the title of the dialog.

`isPresented`

    

A binding to a Boolean value that determines whether to present the dialog.
When the user presses or taps the dialog’s default action button, the system
sets this value to `false`, dismissing the dialog.

`titleVisibility`

    

The visibility of the dialog’s title. The default value is
`Visibility.automatic`.

`actions`

    

A view builder returning the dialog’s actions.

`message`

    

A view builder returning the message for the dialog.

## Discussion

In the example below, a button conditionally presents a confirmation dialog
depending upon the value of a bound Boolean variable. When the Boolean value
is set to `true`, the system displays a confirmation dialog with a cancel
action and a destructive action.

All actions in a confirmation dialog will dismiss the dialog after the action
runs. The default button will be shown with greater prominence. You can
influence the default button by assigning it the `defaultAction` keyboard
shortcut.

The system may reorder the buttons based on their role and prominence.

Dialogs include a standard dismiss action by default. If you provide a button
with a role of `cancel`, that button takes the place of the default dismiss
action. You don’t have to dismiss the presentation with the cancel button’s
action.

Note

In regular size classes in iOS, the system renders confirmation dialogs as a
popover that the user dismisses by tapping anywhere outside the popover,
rather than displaying the standard dismiss action.

## See Also

### Showing a confirmation dialog with a message

`func confirmationDialog<S, A, M>(S, isPresented: Binding<Bool>,
titleVisibility: Visibility, actions: () -> A, message: () -> M) -> some View`

Presents a confirmation dialog with a message when a given condition is true,
using a string variable for the title.

`func confirmationDialog<A, M>(LocalizedStringKey, isPresented: Binding<Bool>,
titleVisibility: Visibility, actions: () -> A, message: () -> M) -> some View`

Presents a confirmation dialog with a message when a given condition is true,
using a localized string key for the title.

`func confirmationDialog<A, M, T>(Text, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A, message: (T)
-> M) -> some View`

Presents a confirmation dialog with a message using data to produce the
dialog’s content and a text view for the message.

`func confirmationDialog<S, A, M, T>(S, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A, message: (T)
-> M) -> some View`

Presents a confirmation dialog with a message using data to produce the
dialog’s content and a string variable for the title.

`func confirmationDialog<A, M, T>(LocalizedStringKey, isPresented:
Binding<Bool>, titleVisibility: Visibility, presenting: T?, actions: (T) -> A,
message: (T) -> M) -> some View`

Presents a confirmation dialog with a message using data to produce the
dialog’s content and a localized string key for the title.

Instance Method

#
confirmationDialog(_:isPresented:titleVisibility:presenting:actions:message:)

Presents a confirmation dialog with a message using data to produce the
dialog’s content and a text view for the message.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func confirmationDialog<A, M, T>(
        _ title: Text,
        isPresented: Binding<Bool>,
        titleVisibility: Visibility = .automatic,
        presenting data: T?,
        @ViewBuilder actions: (T) -> A,
        @ViewBuilder message: (T) -> M
    ) -> some View where A : View, M : View
    

##  Parameters

`title`

    

the title of the dialog.

`isPresented`

    

A binding to a Boolean value that determines whether to present the dialog.
When the user presses or taps the dialog’s default action button, the system
sets this value to `false`, dismissing the dialog.

`titleVisibility`

    

The visibility of the dialog’s title. The default value is
`Visibility.automatic`.

`data`

    

An optional source of truth for the confirmation dialog. The system passes the
contents to the modifier’s closures. You use this data to populate the fields
of a confirmation dialog that you create that the system displays to the user.

`actions`

    

A view builder returning the dialog’s actions given the currently available
data.

`message`

    

A view builder returning the message for the dialog given the currently
available data.

## Discussion

In order for the interface to appear, both `isPresented` must be `true` and
`data` must not be `nil`. `data` should not change after the presentation
occurs. Any changes which occur after the presentation occurs will be ignored.

Use this method when you need to populate the fields of a confirmation dialog
with content from a data source. The example below shows a custom data source,
`FileDetails`, that provides data to populate the dialog:

All actions in a confirmation dialog will dismiss the dialog after the action
runs. The default button will be shown with greater prominence. You can
influence the default button by assigning it the `defaultAction` keyboard
shortcut.

The system may reorder the buttons based on their role and prominence.

Dialogs include a standard dismiss action by default. If you provide a button
with a role of `cancel`, that button takes the place of the default dismiss
action. You don’t have to dismiss the presentation with the cancel button’s
action.

Note

In regular size classes in iOS, the system renders confirmation dialogs as a
popover that the user dismisses by tapping anywhere outside the popover,
rather than displaying the standard dismiss action.

On iOS, tvOS, and watchOS, confirmation dialogs only support controls with
labels that are `Text`. Passing any other type of view results in the content
being omitted.

## See Also

### Showing a confirmation dialog with a message

`func confirmationDialog<S, A, M>(S, isPresented: Binding<Bool>,
titleVisibility: Visibility, actions: () -> A, message: () -> M) -> some View`

Presents a confirmation dialog with a message when a given condition is true,
using a string variable for the title.

`func confirmationDialog<A, M>(LocalizedStringKey, isPresented: Binding<Bool>,
titleVisibility: Visibility, actions: () -> A, message: () -> M) -> some View`

Presents a confirmation dialog with a message when a given condition is true,
using a localized string key for the title.

`func confirmationDialog<A, M>(Text, isPresented: Binding<Bool>,
titleVisibility: Visibility, actions: () -> A, message: () -> M) -> some View`

Presents a confirmation dialog with a message when a given condition is true,
using a text view for the title.

`func confirmationDialog<S, A, M, T>(S, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A, message: (T)
-> M) -> some View`

Presents a confirmation dialog with a message using data to produce the
dialog’s content and a string variable for the title.

`func confirmationDialog<A, M, T>(LocalizedStringKey, isPresented:
Binding<Bool>, titleVisibility: Visibility, presenting: T?, actions: (T) -> A,
message: (T) -> M) -> some View`

Presents a confirmation dialog with a message using data to produce the
dialog’s content and a localized string key for the title.

Instance Method

#
confirmationDialog(_:isPresented:titleVisibility:presenting:actions:message:)

Presents a confirmation dialog with a message using data to produce the
dialog’s content and a string variable for the title.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func confirmationDialog<S, A, M, T>(
        _ title: S,
        isPresented: Binding<Bool>,
        titleVisibility: Visibility = .automatic,
        presenting data: T?,
        @ViewBuilder actions: (T) -> A,
        @ViewBuilder message: (T) -> M
    ) -> some View where S : StringProtocol, A : View, M : View
    

##  Parameters

`title`

    

A text string used as the title of the dialog.

`isPresented`

    

A binding to a Boolean value that determines whether to present the dialog.
When the user presses or taps the dialog’s default action button, the system
sets this value to `false`, dismissing the dialog.

`titleVisibility`

    

The visibility of the dialog’s title. The default value is
`Visibility.automatic`.

`data`

    

An optional source of truth for the confirmation dialog. The system passes the
contents to the modifier’s closures. You use this data to populate the fields
of a confirmation dialog that you create that the system displays to the user.

`actions`

    

A view builder returning the dialog’s actions given the currently available
data.

`message`

    

A view builder returning the message for the dialog given the currently
available data.

## Discussion

In order for the interface to appear, both `isPresented` must be `true` and
`data` must not be `nil`. `data` should not change after the presentation
occurs. Any changes which occur after the presentation occurs will be ignored.

Use this method when you need to populate the fields of a confirmation dialog
with content from a data source. The example below shows a custom data source,
`FileDetails`, that provides data to populate the dialog:

All actions in a confirmation dialog will dismiss the dialog after the action
runs. The default button will be shown with greater prominence. You can
influence the default button by assigning it the `defaultAction` keyboard
shortcut.

The system may reorder the buttons based on their role and prominence.

Dialogs include a standard dismiss action by default. If you provide a button
with a role of `cancel`, that button takes the place of the default dismiss
action. You don’t have to dismiss the presentation with the cancel button’s
action.

Note

In regular size classes in iOS, the system renders confirmation dialogs as a
popover that the user dismisses by tapping anywhere outside the popover,
rather than displaying the standard dismiss action.

On iOS, tvOS, and watchOS, confirmation dialogs only support controls with
labels that are `Text`. Passing any other type of view results in the content
being omitted.

## See Also

### Showing a confirmation dialog with a message

`func confirmationDialog<S, A, M>(S, isPresented: Binding<Bool>,
titleVisibility: Visibility, actions: () -> A, message: () -> M) -> some View`

Presents a confirmation dialog with a message when a given condition is true,
using a string variable for the title.

`func confirmationDialog<A, M>(LocalizedStringKey, isPresented: Binding<Bool>,
titleVisibility: Visibility, actions: () -> A, message: () -> M) -> some View`

Presents a confirmation dialog with a message when a given condition is true,
using a localized string key for the title.

`func confirmationDialog<A, M>(Text, isPresented: Binding<Bool>,
titleVisibility: Visibility, actions: () -> A, message: () -> M) -> some View`

Presents a confirmation dialog with a message when a given condition is true,
using a text view for the title.

`func confirmationDialog<A, M, T>(Text, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A, message: (T)
-> M) -> some View`

Presents a confirmation dialog with a message using data to produce the
dialog’s content and a text view for the message.

`func confirmationDialog<A, M, T>(LocalizedStringKey, isPresented:
Binding<Bool>, titleVisibility: Visibility, presenting: T?, actions: (T) -> A,
message: (T) -> M) -> some View`

Presents a confirmation dialog with a message using data to produce the
dialog’s content and a localized string key for the title.

Instance Method

#
confirmationDialog(_:isPresented:titleVisibility:presenting:actions:message:)

Presents a confirmation dialog with a message using data to produce the
dialog’s content and a localized string key for the title.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func confirmationDialog<A, M, T>(
        _ titleKey: LocalizedStringKey,
        isPresented: Binding<Bool>,
        titleVisibility: Visibility = .automatic,
        presenting data: T?,
        @ViewBuilder actions: (T) -> A,
        @ViewBuilder message: (T) -> M
    ) -> some View where A : View, M : View
    

##  Parameters

`titleKey`

    

The key for the localized string that describes the title of the dialog.

`isPresented`

    

A binding to a Boolean value that determines whether to present the dialog.
When the user presses or taps the dialog’s default action button, the system
sets this value to `false`, dismissing the dialog.

`titleVisibility`

    

The visibility of the dialog’s title. The default value is
`Visibility.automatic`.

`data`

    

An optional source of truth for the confirmation dialog. The system passes the
contents to the modifier’s closures. You use this data to populate the fields
of a confirmation dialog that you create that the system displays to the user.

`actions`

    

A view builder returning the dialog’s actions given the currently available
data.

`message`

    

A view builder returning the message for the dialog given the currently
available data.

## Discussion

In order for the interface to appear, both `isPresented` must be `true` and
`data` must not be `nil`. `data` should not change after the presentation
occurs. Any changes which occur after the presentation occurs will be ignored.

Use this method when you need to populate the fields of a confirmation dialog
with content from a data source. The example below shows a custom data source,
`FileDetails`, that provides data to populate the dialog:

This modifier creates a `Text` view for the title on your behalf, and treats
the localized key similar to `init(_:tableName:bundle:comment:)`. See `Text`
for more information about localizing strings.

All actions in a confirmation dialog will dismiss the dialog after the action
runs. The default button will be shown with greater prominence. You can
influence the default button by assigning it the `defaultAction` keyboard
shortcut.

The system may reorder the buttons based on their role and prominence.

Dialogs include a standard dismiss action by default. If you provide a button
with a role of `cancel`, that button takes the place of the default dismiss
action. You don’t have to dismiss the presentation with the cancel button’s
action.

Note

In regular size classes in iOS, the system renders confirmation dialogs as a
popover that the user dismisses by tapping anywhere outside the popover,
rather than displaying the standard dismiss action.

On iOS, tvOS, and watchOS, confirmation dialogs only support controls with
labels that are `Text`. Passing any other type of view results in the content
being omitted.

## See Also

### Showing a confirmation dialog with a message

`func confirmationDialog<S, A, M>(S, isPresented: Binding<Bool>,
titleVisibility: Visibility, actions: () -> A, message: () -> M) -> some View`

Presents a confirmation dialog with a message when a given condition is true,
using a string variable for the title.

`func confirmationDialog<A, M>(LocalizedStringKey, isPresented: Binding<Bool>,
titleVisibility: Visibility, actions: () -> A, message: () -> M) -> some View`

Presents a confirmation dialog with a message when a given condition is true,
using a localized string key for the title.

`func confirmationDialog<A, M>(Text, isPresented: Binding<Bool>,
titleVisibility: Visibility, actions: () -> A, message: () -> M) -> some View`

Presents a confirmation dialog with a message when a given condition is true,
using a text view for the title.

`func confirmationDialog<A, M, T>(Text, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A, message: (T)
-> M) -> some View`

Presents a confirmation dialog with a message using data to produce the
dialog’s content and a text view for the message.

`func confirmationDialog<S, A, M, T>(S, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A, message: (T)
-> M) -> some View`

Presents a confirmation dialog with a message using data to produce the
dialog’s content and a string variable for the title.

Instance Method

# dialogIcon(_:)

Configures the icon used by dialogs within this view.

iOS 17.0+  iPadOS 17.0+  macOS 13.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+

    
    
    func dialogIcon(_ icon: Image?) -> some View
    

##  Parameters

`icon`

    

The custom icon to use for confirmation dialogs and alerts. Passing `nil` will
use the default app icon.

## Discussion

On macOS, this icon replaces the default icon of the app.

On watchOS, this icon will be shown in any dialogs presented.

This modifier has no effect on other platforms.

The following example configures a `confirmationDialog` with a custom image.

## See Also

### Configuring a dialog

`func dialogSeverity(DialogSeverity) -> some View`

`func dialogSuppressionToggle(isSuppressed: Binding<Bool>) -> some View`

Enables user suppression of dialogs and alerts presented within `self`, with a
default suppression message on macOS. Unused on other platforms.

`func dialogSuppressionToggle<S>(S, isSuppressed: Binding<Bool>) -> some View`

Enables user suppression of dialogs and alerts presented within `self`, with a
custom suppression message on macOS. Unused on other platforms.

`func dialogSuppressionToggle(Text, isSuppressed: Binding<Bool>) -> some View`

Enables user suppression of dialogs and alerts presented within `self`, with a
custom suppression message on macOS. Unused on other platforms.

`func dialogSuppressionToggle(LocalizedStringKey, isSuppressed: Binding<Bool>)
-> some View`

Enables user suppression of dialogs and alerts presented within `self`, with a
custom suppression message on macOS. Unused on other platforms.

Instance Method

# dialogSeverity(_:)

macOS 13.0+  watchOS 10.0+  visionOS 1.0+

    
    
    func dialogSeverity(_ severity: DialogSeverity) -> some View
    

##  Parameters

`severity`

    

The severity to use for confirmation dialogs and alerts.

## See Also

### Configuring a dialog

`func dialogIcon(Image?) -> some View`

Configures the icon used by dialogs within this view.

`func dialogSuppressionToggle(isSuppressed: Binding<Bool>) -> some View`

Enables user suppression of dialogs and alerts presented within `self`, with a
default suppression message on macOS. Unused on other platforms.

`func dialogSuppressionToggle<S>(S, isSuppressed: Binding<Bool>) -> some View`

Enables user suppression of dialogs and alerts presented within `self`, with a
custom suppression message on macOS. Unused on other platforms.

`func dialogSuppressionToggle(Text, isSuppressed: Binding<Bool>) -> some View`

Enables user suppression of dialogs and alerts presented within `self`, with a
custom suppression message on macOS. Unused on other platforms.

`func dialogSuppressionToggle(LocalizedStringKey, isSuppressed: Binding<Bool>)
-> some View`

Enables user suppression of dialogs and alerts presented within `self`, with a
custom suppression message on macOS. Unused on other platforms.

Instance Method

# dialogSuppressionToggle(isSuppressed:)

Enables user suppression of dialogs and alerts presented within `self`, with a
default suppression message on macOS. Unused on other platforms.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func dialogSuppressionToggle(isSuppressed: Binding<Bool>) -> some View
    

##  Parameters

`isSuppressed`

    

Whether the suppression toggle is on or off in the dialog.

## Discussion

Applying dialog suppression adds a toggle to dialogs on macOS, which allows
the user to request the alert not be displayed again. Typically whether a
dialog is suppressed is stored in `AppStorage` and used to decide whether to
present the dialog in the future.

The following example configures a `confirmationDialog` with a suppression
toggle. The toggle’s state is stored in `AppStorage` and used to determine
whether or not to show the dialog when the “Delete Items” button is pressed.

## See Also

### Configuring a dialog

`func dialogIcon(Image?) -> some View`

Configures the icon used by dialogs within this view.

`func dialogSeverity(DialogSeverity) -> some View`

`func dialogSuppressionToggle<S>(S, isSuppressed: Binding<Bool>) -> some View`

Enables user suppression of dialogs and alerts presented within `self`, with a
custom suppression message on macOS. Unused on other platforms.

`func dialogSuppressionToggle(Text, isSuppressed: Binding<Bool>) -> some View`

Enables user suppression of dialogs and alerts presented within `self`, with a
custom suppression message on macOS. Unused on other platforms.

`func dialogSuppressionToggle(LocalizedStringKey, isSuppressed: Binding<Bool>)
-> some View`

Enables user suppression of dialogs and alerts presented within `self`, with a
custom suppression message on macOS. Unused on other platforms.

Instance Method

# dialogSuppressionToggle(_:isSuppressed:)

Enables user suppression of dialogs and alerts presented within `self`, with a
custom suppression message on macOS. Unused on other platforms.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func dialogSuppressionToggle<S>(
        _ title: S,
        isSuppressed: Binding<Bool>
    ) -> some View where S : StringProtocol
    

##  Parameters

`title`

    

The title of the suppression toggle in the dialog. This parameter can be
elided to use the default suppression title.

`isSuppressed`

    

Whether the suppression toggle is on or off in the dialog.

## Discussion

Applying dialog suppression adds a toggle to dialogs on macOS, which allows
the user to request the alert not be displayed again. Typically whether a
dialog is suppressed is stored in `AppStorage` and used to decide whether to
present the dialog in the future.

The following example configures a `confirmationDialog` with a suppression
toggle. The toggle’s state is stored in `AppStorage` and used to determine
whether or not to show the dialog when the “Delete Items” button is pressed.

## See Also

### Configuring a dialog

`func dialogIcon(Image?) -> some View`

Configures the icon used by dialogs within this view.

`func dialogSeverity(DialogSeverity) -> some View`

`func dialogSuppressionToggle(isSuppressed: Binding<Bool>) -> some View`

Enables user suppression of dialogs and alerts presented within `self`, with a
default suppression message on macOS. Unused on other platforms.

`func dialogSuppressionToggle(Text, isSuppressed: Binding<Bool>) -> some View`

Enables user suppression of dialogs and alerts presented within `self`, with a
custom suppression message on macOS. Unused on other platforms.

`func dialogSuppressionToggle(LocalizedStringKey, isSuppressed: Binding<Bool>)
-> some View`

Enables user suppression of dialogs and alerts presented within `self`, with a
custom suppression message on macOS. Unused on other platforms.

Instance Method

# dialogSuppressionToggle(_:isSuppressed:)

Enables user suppression of dialogs and alerts presented within `self`, with a
custom suppression message on macOS. Unused on other platforms.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func dialogSuppressionToggle(
        _ label: Text,
        isSuppressed: Binding<Bool>
    ) -> some View
    

##  Parameters

`label`

    

The label of the suppression toggle in the dialog. This parameter can be
elided to use the default suppression title.

`isSuppressed`

    

Whether the suppression toggle is on or off in the dialog.

## Discussion

Applying dialog suppression adds a toggle to dialogs on macOS, which allows
the user to request the alert not be displayed again. Typically whether a
dialog is suppressed is stored in `AppStorage` and used to decide whether to
present the dialog in the future.

The following example configures a `confirmationDialog` with a suppression
toggle. The toggle’s state is stored in `AppStorage` and used to determine
whether or not to show the dialog when the “Delete Items” button is pressed.

## See Also

### Configuring a dialog

`func dialogIcon(Image?) -> some View`

Configures the icon used by dialogs within this view.

`func dialogSeverity(DialogSeverity) -> some View`

`func dialogSuppressionToggle(isSuppressed: Binding<Bool>) -> some View`

Enables user suppression of dialogs and alerts presented within `self`, with a
default suppression message on macOS. Unused on other platforms.

`func dialogSuppressionToggle<S>(S, isSuppressed: Binding<Bool>) -> some View`

Enables user suppression of dialogs and alerts presented within `self`, with a
custom suppression message on macOS. Unused on other platforms.

`func dialogSuppressionToggle(LocalizedStringKey, isSuppressed: Binding<Bool>)
-> some View`

Enables user suppression of dialogs and alerts presented within `self`, with a
custom suppression message on macOS. Unused on other platforms.

Instance Method

# dialogSuppressionToggle(_:isSuppressed:)

Enables user suppression of dialogs and alerts presented within `self`, with a
custom suppression message on macOS. Unused on other platforms.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func dialogSuppressionToggle(
        _ titleKey: LocalizedStringKey,
        isSuppressed: Binding<Bool>
    ) -> some View
    

##  Parameters

`titleKey`

    

The title of the suppression toggle in the dialog. This parameter can be
elided to use the default suppression title.

`isSuppressed`

    

Whether the suppression toggle is on or off in the dialog.

## Discussion

Applying dialog suppression adds a toggle to dialogs on macOS, which allows
the user to request the alert not be displayed again. Typically whether a
dialog is suppressed is stored in `AppStorage` and used to decide whether to
present the dialog in the future.

The following example configures a `confirmationDialog` with a suppression
toggle. The toggle’s state is stored in `AppStorage` and used to determine
whether or not to show the dialog when the “Delete Items” button is pressed.

## See Also

### Configuring a dialog

`func dialogIcon(Image?) -> some View`

Configures the icon used by dialogs within this view.

`func dialogSeverity(DialogSeverity) -> some View`

`func dialogSuppressionToggle(isSuppressed: Binding<Bool>) -> some View`

Enables user suppression of dialogs and alerts presented within `self`, with a
default suppression message on macOS. Unused on other platforms.

`func dialogSuppressionToggle<S>(S, isSuppressed: Binding<Bool>) -> some View`

Enables user suppression of dialogs and alerts presented within `self`, with a
custom suppression message on macOS. Unused on other platforms.

`func dialogSuppressionToggle(Text, isSuppressed: Binding<Bool>) -> some View`

Enables user suppression of dialogs and alerts presented within `self`, with a
custom suppression message on macOS. Unused on other platforms.

Instance Method

# sheet(isPresented:onDismiss:content:)

Presents a sheet when a binding to a Boolean value that you provide is true.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func sheet<Content>(
        isPresented: Binding<Bool>,
        onDismiss: (() -> Void)? = nil,
        @ViewBuilder content: @escaping () -> Content
    ) -> some View where Content : View
    

##  Parameters

`isPresented`

    

A binding to a Boolean value that determines whether to present the sheet that
you create in the modifier’s `content` closure.

`onDismiss`

    

The closure to execute when dismissing the sheet.

`content`

    

A closure that returns the content of the sheet.

## Discussion

Use this method when you want to present a modal view to the user when a
Boolean value you provide is true. The example below displays a modal view of
the mockup for a software license agreement when the user toggles the
`isShowingSheet` variable by clicking or tapping on the “Show License
Agreement” button:

In vertically compact environments, such as iPhone in landscape orientation, a
sheet presentation automatically adapts to appear as a full-screen cover. Use
the `presentationCompactAdaptation(_:)` or
`presentationCompactAdaptation(horizontal:vertical:)` modifier to override
this behavior.

## See Also

### Showing a sheet, cover, or popover

`func sheet<Item, Content>(item: Binding<Item?>, onDismiss: (() -> Void)?,
content: (Item) -> Content) -> some View`

Presents a sheet using the given item as a data source for the sheet’s
content.

`func fullScreenCover<Content>(isPresented: Binding<Bool>, onDismiss: (() ->
Void)?, content: () -> Content) -> some View`

Presents a modal view that covers as much of the screen as possible when
binding to a Boolean value you provide is true.

`func fullScreenCover<Item, Content>(item: Binding<Item?>, onDismiss: (() ->
Void)?, content: (Item) -> Content) -> some View`

Presents a modal view that covers as much of the screen as possible using the
binding you provide as a data source for the sheet’s content.

`func popover<Content>(isPresented: Binding<Bool>, attachmentAnchor:
PopoverAttachmentAnchor, arrowEdge: Edge, content: () -> Content) -> some
View`

Presents a popover when a given condition is true.

`func popover<Item, Content>(item: Binding<Item?>, attachmentAnchor:
PopoverAttachmentAnchor, arrowEdge: Edge, content: (Item) -> Content) -> some
View`

Presents a popover using the given item as a data source for the popover’s
content.

`enum PopoverAttachmentAnchor`

An attachment anchor for a popover.

Instance Method

# sheet(item:onDismiss:content:)

Presents a sheet using the given item as a data source for the sheet’s
content.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func sheet<Item, Content>(
        item: Binding<Item?>,
        onDismiss: (() -> Void)? = nil,
        @ViewBuilder content: @escaping (Item) -> Content
    ) -> some View where Item : Identifiable, Content : View
    

##  Parameters

`item`

    

A binding to an optional source of truth for the sheet. When `item` is
non-`nil`, the system passes the item’s content to the modifier’s closure. You
display this content in a sheet that you create that the system displays to
the user. If `item` changes, the system dismisses the sheet and replaces it
with a new one using the same process.

`onDismiss`

    

The closure to execute when dismissing the sheet.

`content`

    

A closure returning the content of the sheet.

## Discussion

Use this method when you need to present a modal view with content from a
custom data source. The example below shows a custom data source
`InventoryItem` that the `content` closure uses to populate the display the
action sheet shows to the user:

In vertically compact environments, such as iPhone in landscape orientation, a
sheet presentation automatically adapts to appear as a full-screen cover. Use
the `presentationCompactAdaptation(_:)` or
`presentationCompactAdaptation(horizontal:vertical:)` modifier to override
this behavior.

## See Also

### Showing a sheet, cover, or popover

`func sheet<Content>(isPresented: Binding<Bool>, onDismiss: (() -> Void)?,
content: () -> Content) -> some View`

Presents a sheet when a binding to a Boolean value that you provide is true.

`func fullScreenCover<Content>(isPresented: Binding<Bool>, onDismiss: (() ->
Void)?, content: () -> Content) -> some View`

Presents a modal view that covers as much of the screen as possible when
binding to a Boolean value you provide is true.

`func fullScreenCover<Item, Content>(item: Binding<Item?>, onDismiss: (() ->
Void)?, content: (Item) -> Content) -> some View`

Presents a modal view that covers as much of the screen as possible using the
binding you provide as a data source for the sheet’s content.

`func popover<Content>(isPresented: Binding<Bool>, attachmentAnchor:
PopoverAttachmentAnchor, arrowEdge: Edge, content: () -> Content) -> some
View`

Presents a popover when a given condition is true.

`func popover<Item, Content>(item: Binding<Item?>, attachmentAnchor:
PopoverAttachmentAnchor, arrowEdge: Edge, content: (Item) -> Content) -> some
View`

Presents a popover using the given item as a data source for the popover’s
content.

`enum PopoverAttachmentAnchor`

An attachment anchor for a popover.

Instance Method

# fullScreenCover(isPresented:onDismiss:content:)

Presents a modal view that covers as much of the screen as possible when
binding to a Boolean value you provide is true.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS 7.0+
visionOS 1.0+

    
    
    func fullScreenCover<Content>(
        isPresented: Binding<Bool>,
        onDismiss: (() -> Void)? = nil,
        @ViewBuilder content: @escaping () -> Content
    ) -> some View where Content : View
    

##  Parameters

`isPresented`

    

A binding to a Boolean value that determines whether to present the sheet.

`onDismiss`

    

The closure to execute when dismissing the modal view.

`content`

    

A closure that returns the content of the modal view.

## Discussion

Use this method to show a modal view that covers as much of the screen as
possible. The example below displays a custom view when the user toggles the
value of the `isPresenting` binding:

## See Also

### Showing a sheet, cover, or popover

`func sheet<Content>(isPresented: Binding<Bool>, onDismiss: (() -> Void)?,
content: () -> Content) -> some View`

Presents a sheet when a binding to a Boolean value that you provide is true.

`func sheet<Item, Content>(item: Binding<Item?>, onDismiss: (() -> Void)?,
content: (Item) -> Content) -> some View`

Presents a sheet using the given item as a data source for the sheet’s
content.

`func fullScreenCover<Item, Content>(item: Binding<Item?>, onDismiss: (() ->
Void)?, content: (Item) -> Content) -> some View`

Presents a modal view that covers as much of the screen as possible using the
binding you provide as a data source for the sheet’s content.

`func popover<Content>(isPresented: Binding<Bool>, attachmentAnchor:
PopoverAttachmentAnchor, arrowEdge: Edge, content: () -> Content) -> some
View`

Presents a popover when a given condition is true.

`func popover<Item, Content>(item: Binding<Item?>, attachmentAnchor:
PopoverAttachmentAnchor, arrowEdge: Edge, content: (Item) -> Content) -> some
View`

Presents a popover using the given item as a data source for the popover’s
content.

`enum PopoverAttachmentAnchor`

An attachment anchor for a popover.

Instance Method

# fullScreenCover(item:onDismiss:content:)

Presents a modal view that covers as much of the screen as possible using the
binding you provide as a data source for the sheet’s content.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS 7.0+
visionOS 1.0+

    
    
    func fullScreenCover<Item, Content>(
        item: Binding<Item?>,
        onDismiss: (() -> Void)? = nil,
        @ViewBuilder content: @escaping (Item) -> Content
    ) -> some View where Item : Identifiable, Content : View
    

##  Parameters

`item`

    

A binding to an optional source of truth for the sheet. When `item` is
non-`nil`, the system passes the contents to the modifier’s closure. You
display this content in a sheet that you create that the system displays to
the user. If `item` changes, the system dismisses the currently displayed
sheet and replaces it with a new one using the same process.

`onDismiss`

    

The closure to execute when dismissing the modal view.

`content`

    

A closure returning the content of the modal view.

## Discussion

Use this method to display a modal view that covers as much of the screen as
possible. In the example below a custom structure — `CoverData` — provides
data for the full-screen view to display in the `content` closure when the
user clicks or taps the “Present Full-Screen Cover With Data” button:

## See Also

### Showing a sheet, cover, or popover

`func sheet<Content>(isPresented: Binding<Bool>, onDismiss: (() -> Void)?,
content: () -> Content) -> some View`

Presents a sheet when a binding to a Boolean value that you provide is true.

`func sheet<Item, Content>(item: Binding<Item?>, onDismiss: (() -> Void)?,
content: (Item) -> Content) -> some View`

Presents a sheet using the given item as a data source for the sheet’s
content.

`func fullScreenCover<Content>(isPresented: Binding<Bool>, onDismiss: (() ->
Void)?, content: () -> Content) -> some View`

Presents a modal view that covers as much of the screen as possible when
binding to a Boolean value you provide is true.

`func popover<Content>(isPresented: Binding<Bool>, attachmentAnchor:
PopoverAttachmentAnchor, arrowEdge: Edge, content: () -> Content) -> some
View`

Presents a popover when a given condition is true.

`func popover<Item, Content>(item: Binding<Item?>, attachmentAnchor:
PopoverAttachmentAnchor, arrowEdge: Edge, content: (Item) -> Content) -> some
View`

Presents a popover using the given item as a data source for the popover’s
content.

`enum PopoverAttachmentAnchor`

An attachment anchor for a popover.

Instance Method

# popover(isPresented:attachmentAnchor:arrowEdge:content:)

Presents a popover when a given condition is true.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  visionOS 1.0+

    
    
    func popover<Content>(
        isPresented: Binding<Bool>,
        attachmentAnchor: PopoverAttachmentAnchor = .rect(.bounds),
        arrowEdge: Edge = .top,
        @ViewBuilder content: @escaping () -> Content
    ) -> some View where Content : View
    

##  Parameters

`isPresented`

    

A binding to a Boolean value that determines whether to present the popover
content that you return from the modifier’s `content` closure.

`attachmentAnchor`

    

The positioning anchor that defines the attachment point of the popover. The
default is `bounds`.

`arrowEdge`

    

The edge of the `attachmentAnchor` that defines the location of the popover’s
arrow in macOS. The default is `Edge.top`. iOS ignores this parameter.

`content`

    

A closure returning the content of the popover.

## Discussion

Use this method to show a popover whose contents are a SwiftUI view that you
provide when a bound Boolean variable is `true`. In the example below, a
popover displays whenever the user toggles the `isShowingPopover` state
variable by pressing the “Show Popover” button:

## See Also

### Showing a sheet, cover, or popover

`func sheet<Content>(isPresented: Binding<Bool>, onDismiss: (() -> Void)?,
content: () -> Content) -> some View`

Presents a sheet when a binding to a Boolean value that you provide is true.

`func sheet<Item, Content>(item: Binding<Item?>, onDismiss: (() -> Void)?,
content: (Item) -> Content) -> some View`

Presents a sheet using the given item as a data source for the sheet’s
content.

`func fullScreenCover<Content>(isPresented: Binding<Bool>, onDismiss: (() ->
Void)?, content: () -> Content) -> some View`

Presents a modal view that covers as much of the screen as possible when
binding to a Boolean value you provide is true.

`func fullScreenCover<Item, Content>(item: Binding<Item?>, onDismiss: (() ->
Void)?, content: (Item) -> Content) -> some View`

Presents a modal view that covers as much of the screen as possible using the
binding you provide as a data source for the sheet’s content.

`func popover<Item, Content>(item: Binding<Item?>, attachmentAnchor:
PopoverAttachmentAnchor, arrowEdge: Edge, content: (Item) -> Content) -> some
View`

Presents a popover using the given item as a data source for the popover’s
content.

`enum PopoverAttachmentAnchor`

An attachment anchor for a popover.

Instance Method

# popover(item:attachmentAnchor:arrowEdge:content:)

Presents a popover using the given item as a data source for the popover’s
content.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  visionOS 1.0+

    
    
    func popover<Item, Content>(
        item: Binding<Item?>,
        attachmentAnchor: PopoverAttachmentAnchor = .rect(.bounds),
        arrowEdge: Edge = .top,
        @ViewBuilder content: @escaping (Item) -> Content
    ) -> some View where Item : Identifiable, Content : View
    

##  Parameters

`item`

    

A binding to an optional source of truth for the popover. When `item` is
non-`nil`, the system passes the contents to the modifier’s closure. You use
this content to populate the fields of a popover that you create that the
system displays to the user. If `item` changes, the system dismisses the
currently presented popover and replaces it with a new popover using the same
process.

`attachmentAnchor`

    

The positioning anchor that defines the attachment point of the popover. The
default is `bounds`.

`arrowEdge`

    

The edge of the `attachmentAnchor` that defines the location of the popover’s
arrow in macOS. The default is `Edge.top`. iOS ignores this parameter.

`content`

    

A closure returning the content of the popover.

## Discussion

Use this method when you need to present a popover with content from a custom
data source. The example below uses data in the `PopoverModel` structure to
populate the view in the `content` closure that the popover displays to the
user:

## See Also

### Showing a sheet, cover, or popover

`func sheet<Content>(isPresented: Binding<Bool>, onDismiss: (() -> Void)?,
content: () -> Content) -> some View`

Presents a sheet when a binding to a Boolean value that you provide is true.

`func sheet<Item, Content>(item: Binding<Item?>, onDismiss: (() -> Void)?,
content: (Item) -> Content) -> some View`

Presents a sheet using the given item as a data source for the sheet’s
content.

`func fullScreenCover<Content>(isPresented: Binding<Bool>, onDismiss: (() ->
Void)?, content: () -> Content) -> some View`

Presents a modal view that covers as much of the screen as possible when
binding to a Boolean value you provide is true.

`func fullScreenCover<Item, Content>(item: Binding<Item?>, onDismiss: (() ->
Void)?, content: (Item) -> Content) -> some View`

Presents a modal view that covers as much of the screen as possible using the
binding you provide as a data source for the sheet’s content.

`func popover<Content>(isPresented: Binding<Bool>, attachmentAnchor:
PopoverAttachmentAnchor, arrowEdge: Edge, content: () -> Content) -> some
View`

Presents a popover when a given condition is true.

`enum PopoverAttachmentAnchor`

An attachment anchor for a popover.

Instance Method

# interactiveDismissDisabled(_:)

Conditionally prevents interactive dismissal of presentations like popovers,
sheets, and inspectors.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func interactiveDismissDisabled(_ isDisabled: Bool = true) -> some View
    

##  Parameters

`isDisabled`

    

A Boolean value that indicates whether to prevent nonprogrammatic dismissal of
the containing view hierarchy when presented in a sheet or popover.

## Discussion

Users can dismiss certain kinds of presentations using built-in gestures. In
particular, a user can dismiss a sheet by dragging it down, or a popover by
clicking or tapping outside of the presented view. Use the
`interactiveDismissDisabled(_:)` modifier to conditionally prevent this kind
of dismissal. You typically do this to prevent the user from dismissing a
presentation before providing needed data or completing a required action.

For instance, suppose you have a view that displays a licensing agreement that
the user must acknowledge before continuing:

If you present this view in a sheet, the user can dismiss it by either tapping
the button — which calls `dismiss` from its `action` closure — or by dragging
the sheet down. To ensure that the user accepts the terms by tapping the
button, disable interactive dismissal, conditioned on the `areTermsAccepted`
property:

You can apply the modifier to any view in the sheet’s view hierarchy,
including to the sheet’s top level view, as the example demonstrates, or to
any child view, like the `Form` or the Accept `Button`.

The modifier has no effect on programmatic dismissal, which you can invoke by
updating the `Binding` that controls the presentation, or by calling the
environment’s `dismiss` action. On macOS, disabling interactive dismissal in a
popover makes the popover nontransient.

## See Also

### Dismissing a presentation

`var isPresented: Bool`

A Boolean value that indicates whether the view associated with this
environment is currently presented.

`var dismiss: DismissAction`

An action that dismisses the current presentation.

`struct DismissAction`

An action that dismisses a presentation.

Instance Method

# presentationDetents(_:)

Sets the available detents for the enclosing sheet.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func presentationDetents(_ detents: Set<PresentationDetent>) -> some View
    

##  Parameters

`detents`

    

A set of supported detents for the sheet. If you provide more that one detent,
people can drag the sheet to resize it.

## Discussion

By default, sheets support the `large` detent.

## See Also

### Configuring a sheet’s height

`func presentationDetents(Set<PresentationDetent>, selection:
Binding<PresentationDetent>) -> some View`

Sets the available detents for the enclosing sheet, giving you programmatic
control of the currently selected detent.

`func presentationContentInteraction(PresentationContentInteraction) -> some
View`

Configures the behavior of swipe gestures on a presentation.

`func presentationDragIndicator(Visibility) -> some View`

Sets the visibility of the drag indicator on top of a sheet.

`struct PresentationDetent`

A type that represents a height where a sheet naturally rests.

`protocol CustomPresentationDetent`

The definition of a custom detent with a calculated height.

`struct PresentationContentInteraction`

A behavior that you can use to influence how a presentation responds to swipe
gestures.

Instance Method

# presentationDetents(_:selection:)

Sets the available detents for the enclosing sheet, giving you programmatic
control of the currently selected detent.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func presentationDetents(
        _ detents: Set<PresentationDetent>,
        selection: Binding<PresentationDetent>
    ) -> some View
    

##  Parameters

`detents`

    

A set of supported detents for the sheet. If you provide more that one detent,
people can drag the sheet to resize it.

`selection`

    

A `Binding` to the currently selected detent. Ensure that the value matches
one of the detents that you provide for the `detents` parameter.

## Discussion

By default, sheets support the `large` detent.

## See Also

### Configuring a sheet’s height

`func presentationDetents(Set<PresentationDetent>) -> some View`

Sets the available detents for the enclosing sheet.

`func presentationContentInteraction(PresentationContentInteraction) -> some
View`

Configures the behavior of swipe gestures on a presentation.

`func presentationDragIndicator(Visibility) -> some View`

Sets the visibility of the drag indicator on top of a sheet.

`struct PresentationDetent`

A type that represents a height where a sheet naturally rests.

`protocol CustomPresentationDetent`

The definition of a custom detent with a calculated height.

`struct PresentationContentInteraction`

A behavior that you can use to influence how a presentation responds to swipe
gestures.

Instance Method

# presentationDragIndicator(_:)

Sets the visibility of the drag indicator on top of a sheet.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func presentationDragIndicator(_ visibility: Visibility) -> some View
    

##  Parameters

`visibility`

    

The preferred visibility of the drag indicator.

## Discussion

You can show a drag indicator when it isn’t apparent that a sheet can resize
or when the sheet can’t dismiss interactively.

## See Also

### Configuring a sheet’s height

`func presentationDetents(Set<PresentationDetent>) -> some View`

Sets the available detents for the enclosing sheet.

`func presentationDetents(Set<PresentationDetent>, selection:
Binding<PresentationDetent>) -> some View`

Sets the available detents for the enclosing sheet, giving you programmatic
control of the currently selected detent.

`func presentationContentInteraction(PresentationContentInteraction) -> some
View`

Configures the behavior of swipe gestures on a presentation.

`struct PresentationDetent`

A type that represents a height where a sheet naturally rests.

`protocol CustomPresentationDetent`

The definition of a custom detent with a calculated height.

`struct PresentationContentInteraction`

A behavior that you can use to influence how a presentation responds to swipe
gestures.

Instance Method

# presentationBackground(_:)

Sets the presentation background of the enclosing sheet using a shape style.

iOS 16.4+  iPadOS 16.4+  macOS 13.3+  Mac Catalyst 16.4+  tvOS 16.4+  watchOS
9.4+  visionOS 1.0+

    
    
    func presentationBackground<S>(_ style: S) -> some View where S : ShapeStyle
    

##  Parameters

`style`

    

The shape style to use as the presentation background.

## Discussion

The following example uses the `thick` material as the sheet background:

The `presentationBackground(_:)` modifier differs from the
`background(_:ignoresSafeAreaEdges:)` modifier in several key ways. A
presentation background:

  * Automatically fills the entire presentation.

  * Allows views behind the presentation to show through translucent styles.

## See Also

### Styling a sheet and its background

`func presentationCornerRadius(CGFloat?) -> some View`

Requests that the presentation have a specific corner radius.

`func presentationBackground<V>(alignment: Alignment, content: () -> V) ->
some View`

Sets the presentation background of the enclosing sheet to a custom view.

`func presentationBackgroundInteraction(PresentationBackgroundInteraction) ->
some View`

Controls whether people can interact with the view behind a presentation.

`struct PresentationBackgroundInteraction`

The kinds of interaction available to views behind a presentation.

Instance Method

# presentationBackground(alignment:content:)

Sets the presentation background of the enclosing sheet to a custom view.

iOS 16.4+  iPadOS 16.4+  macOS 13.3+  Mac Catalyst 16.4+  tvOS 16.4+  watchOS
9.4+  visionOS 1.0+

    
    
    func presentationBackground<V>(
        alignment: Alignment = .center,
        @ViewBuilder content: () -> V
    ) -> some View where V : View
    

##  Parameters

`alignment`

    

The alignment that the modifier uses to position the implicit `ZStack` that
groups the background views. The default is `center`.

`content`

    

The view to use as the background of the presentation.

## Discussion

The following example uses a yellow view as the sheet background:

The `presentationBackground(alignment:content:)` modifier differs from the
`background(alignment:content:)` modifier in several key ways. A presentation
background:

  * Automatically fills the entire presentation.

  * Allows views behind the presentation to show through translucent areas of the `content`.

## See Also

### Styling a sheet and its background

`func presentationCornerRadius(CGFloat?) -> some View`

Requests that the presentation have a specific corner radius.

`func presentationBackground<S>(S) -> some View`

Sets the presentation background of the enclosing sheet using a shape style.

`func presentationBackgroundInteraction(PresentationBackgroundInteraction) ->
some View`

Controls whether people can interact with the view behind a presentation.

`struct PresentationBackgroundInteraction`

The kinds of interaction available to views behind a presentation.

Instance Method

# presentationBackgroundInteraction(_:)

Controls whether people can interact with the view behind a presentation.

iOS 16.4+  iPadOS 16.4+  macOS 13.3+  Mac Catalyst 16.4+  tvOS 16.4+  watchOS
9.4+  visionOS 1.0+

    
    
    func presentationBackgroundInteraction(_ interaction: PresentationBackgroundInteraction) -> some View
    

##  Parameters

`interaction`

    

A specification of how people can interact with the view behind a
presentation.

## Discussion

On many platforms, SwiftUI automatically disables the view behind a sheet that
you present, so that people can’t interact with the backing view until they
dismiss the sheet. Use this modifier if you want to enable interaction.

The following example enables people to interact with the view behind the
sheet when the sheet is at the smallest detent, but not at the other detents:

## See Also

### Styling a sheet and its background

`func presentationCornerRadius(CGFloat?) -> some View`

Requests that the presentation have a specific corner radius.

`func presentationBackground<S>(S) -> some View`

Sets the presentation background of the enclosing sheet using a shape style.

`func presentationBackground<V>(alignment: Alignment, content: () -> V) ->
some View`

Sets the presentation background of the enclosing sheet to a custom view.

`struct PresentationBackgroundInteraction`

The kinds of interaction available to views behind a presentation.

Instance Method

# presentationCompactAdaptation(horizontal:vertical:)

Specifies how to adapt a presentation to horizontally and vertically compact
size classes.

iOS 16.4+  iPadOS 16.4+  macOS 13.3+  Mac Catalyst 16.4+  tvOS 16.4+  watchOS
9.4+  visionOS 1.0+

    
    
    func presentationCompactAdaptation(
        horizontal horizontalAdaptation: PresentationAdaptation,
        vertical verticalAdaptation: PresentationAdaptation
    ) -> some View
    

##  Parameters

`horizontalAdaptation`

    

The adaptation to use in a horizontally compact size class.

`verticalAdaptation`

    

The adaptation to use in a vertically compact size class. In a size class that
is both horizontally and vertically compact, SwiftUI uses the
`verticalAdaptation` value.

## Discussion

Some presentations adapt their appearance depending on the context. For
example, a popover presentation over a horizontally-compact view uses a sheet
appearance by default. Use this modifier to indicate a custom adaptation
preference.

If you want to specify the same adaptation for both dimensions, use the
`presentationCompactAdaptation(_:)` method instead.

## See Also

### Adapting a presentation to size classes

`func presentationCompactAdaptation(PresentationAdaptation) -> some View`

Specifies how to adapt a presentation to compact size classes.

`struct PresentationAdaptation`

Strategies for adapting a presentation to a different size class.

Instance Method

# presentationCompactAdaptation(_:)

Specifies how to adapt a presentation to compact size classes.

iOS 16.4+  iPadOS 16.4+  macOS 13.3+  Mac Catalyst 16.4+  tvOS 16.4+  watchOS
9.4+  visionOS 1.0+

    
    
    func presentationCompactAdaptation(_ adaptation: PresentationAdaptation) -> some View
    

##  Parameters

`adaptation`

    

The adaptation to use in either a horizontally or vertically compact size
class.

## Discussion

Some presentations adapt their appearance depending on the context. For
example, a sheet presentation over a vertically-compact view uses a full-
screen-cover appearance by default. Use this modifier to indicate a custom
adaptation preference. For example, the following code uses a presentation
adaptation value of `none` to request that the system not adapt the sheet in
compact size classes:

If you want to specify different adaptations for each dimension, use the
`presentationCompactAdaptation(horizontal:vertical:)` method instead.

## See Also

### Adapting a presentation to size classes

`func presentationCompactAdaptation(horizontal: PresentationAdaptation,
vertical: PresentationAdaptation) -> some View`

Specifies how to adapt a presentation to horizontally and vertically compact
size classes.

`struct PresentationAdaptation`

Strategies for adapting a presentation to a different size class.

Instance Method

# presentationContentInteraction(_:)

Configures the behavior of swipe gestures on a presentation.

iOS 16.4+  iPadOS 16.4+  macOS 13.3+  Mac Catalyst 16.4+  tvOS 16.4+  watchOS
9.4+  visionOS 1.0+

    
    
    func presentationContentInteraction(_ behavior: PresentationContentInteraction) -> some View
    

##  Parameters

`behavior`

    

The requested behavior.

## Discussion

By default, when a person swipes up on a scroll view in a resizable
presentation, the presentation grows to the next detent. A scroll view
embedded in the presentation only scrolls after the presentation reaches its
largest size. Use this modifier to control which action takes precedence.

For example, you can request that swipe gestures scroll content first,
resizing the sheet only after hitting the end of the scroll view, by passing
the `scrolls` value to this modifier:

People can always resize your presentation using the drag indicator.

## See Also

### Configuring a sheet’s height

`func presentationDetents(Set<PresentationDetent>) -> some View`

Sets the available detents for the enclosing sheet.

`func presentationDetents(Set<PresentationDetent>, selection:
Binding<PresentationDetent>) -> some View`

Sets the available detents for the enclosing sheet, giving you programmatic
control of the currently selected detent.

`func presentationDragIndicator(Visibility) -> some View`

Sets the visibility of the drag indicator on top of a sheet.

`struct PresentationDetent`

A type that represents a height where a sheet naturally rests.

`protocol CustomPresentationDetent`

The definition of a custom detent with a calculated height.

`struct PresentationContentInteraction`

A behavior that you can use to influence how a presentation responds to swipe
gestures.

Instance Method

# presentationCornerRadius(_:)

Requests that the presentation have a specific corner radius.

iOS 16.4+  iPadOS 16.4+  macOS 13.3+  Mac Catalyst 16.4+  tvOS 16.4+  watchOS
9.4+  visionOS 1.0+

    
    
    func presentationCornerRadius(_ cornerRadius: CGFloat?) -> some View
    

##  Parameters

`cornerRadius`

    

The corner radius, or `nil` to use the system default.

## Discussion

Use this modifier to change the corner radius of a presentation.

## See Also

### Styling a sheet and its background

`func presentationBackground<S>(S) -> some View`

Sets the presentation background of the enclosing sheet using a shape style.

`func presentationBackground<V>(alignment: Alignment, content: () -> V) ->
some View`

Sets the presentation background of the enclosing sheet to a custom view.

`func presentationBackgroundInteraction(PresentationBackgroundInteraction) ->
some View`

Controls whether people can interact with the view behind a presentation.

`struct PresentationBackgroundInteraction`

The kinds of interaction available to views behind a presentation.

Instance Method

# fileExporter(isPresented:document:contentType:defaultFilename:onCompletion:)

Presents a system interface for exporting a document that’s stored in a value
type, like a structure, to a file on disk.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    func fileExporter<D>(
        isPresented: Binding<Bool>,
        document: D?,
        contentType: UTType,
        defaultFilename: String? = nil,
        onCompletion: @escaping (Result<URL, any Error>) -> Void
    ) -> some View where D : FileDocument
    

##  Parameters

`isPresented`

    

A binding to whether the interface should be shown.

`document`

    

The in-memory document to export.

`contentType`

    

The content type to use for the exported file.

`defaultFilename`

    

If provided, the default name to use for the exported file, which will the
user will have an opportunity to edit prior to the export.

`onCompletion`

    

A callback that will be invoked when the operation has has succeeded or
failed.

`result`

    

A `Result` indicating whether the operation succeeded or failed.

## Discussion

In order for the interface to appear, both `isPresented` must be `true` and
`document` must not be `nil`. When the operation is finished, `isPresented`
will be set to `false` before `onCompletion` is called. If the user cancels
the operation, `isPresented` will be set to `false` and `onCompletion` will
not be called.

The `contentType` provided must be included within the document type’s
`writableContentTypes`, otherwise the first valid writable content type will
be used instead.

## See Also

### Exporting to file

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType:
UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void) -> some View`

Presents a system interface for exporting a document that’s stored in a
reference type, like a class, to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType:
UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for exporting a collection of value type documents
to files on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType:
UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for exporting a collection of reference type
documents to files on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system interface for allowing the user to export a `FileDocument`
to a file on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system dialog for allowing the user to export a
`ReferenceFileDocument` to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system dialog for allowing the user to export a collection of
documents that conform to `ReferenceFileDocument` to files on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system dialog for allowing the user to export a collection of
documents that conform to `FileDocument` to files on disk.

`func fileExporter<T>(isPresented: Binding<Bool>, item: T?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system interface allowing the user to export a `Transferable` item
to file on disk.

`func fileExporter<C, T>(isPresented: Binding<Bool>, items: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system interface allowing the user to export a collection of items
to files on disk.

`func fileExporterFilenameLabel(LocalizedStringKey) -> some View`

On macOS, configures the `fileExporter` with a label for the file name field.

`func fileExporterFilenameLabel(Text?) -> some View`

On macOS, configures the `fileExporter` with a text to use as a label for the
file name field.

`func fileExporterFilenameLabel<S>(S) -> some View`

On macOS, configures the `fileExporter` with a label for the file name field.

Instance Method

# fileExporter(isPresented:document:contentType:defaultFilename:onCompletion:)

Presents a system interface for exporting a document that’s stored in a
reference type, like a class, to a file on disk.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    func fileExporter<D>(
        isPresented: Binding<Bool>,
        document: D?,
        contentType: UTType,
        defaultFilename: String? = nil,
        onCompletion: @escaping (Result<URL, any Error>) -> Void
    ) -> some View where D : ReferenceFileDocument
    

##  Parameters

`isPresented`

    

A binding to whether the interface should be shown.

`document`

    

The in-memory document to export.

`contentType`

    

The content type to use for the exported file.

`defaultFilename`

    

If provided, the default name to use for the exported file, which will the
user will have an opportunity to edit prior to the export.

`onCompletion`

    

A callback that will be invoked when the operation has has succeeded or
failed.

`result`

    

A `Result` indicating whether the operation succeeded or failed.

## Discussion

In order for the interface to appear, both `isPresented` must be `true` and
`document` must not be `nil`. When the operation is finished, `isPresented`
will be set to `false` before `onCompletion` is called. If the user cancels
the operation, `isPresented` will be set to `false` and `onCompletion` will
not be called.

The `contentType` provided must be included within the document type’s
`writableContentTypes`, otherwise the first valid writable content type will
be used instead.

## See Also

### Exporting to file

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType:
UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void) -> some View`

Presents a system interface for exporting a document that’s stored in a value
type, like a structure, to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType:
UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for exporting a collection of value type documents
to files on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType:
UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for exporting a collection of reference type
documents to files on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system interface for allowing the user to export a `FileDocument`
to a file on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system dialog for allowing the user to export a
`ReferenceFileDocument` to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system dialog for allowing the user to export a collection of
documents that conform to `ReferenceFileDocument` to files on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system dialog for allowing the user to export a collection of
documents that conform to `FileDocument` to files on disk.

`func fileExporter<T>(isPresented: Binding<Bool>, item: T?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system interface allowing the user to export a `Transferable` item
to file on disk.

`func fileExporter<C, T>(isPresented: Binding<Bool>, items: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system interface allowing the user to export a collection of items
to files on disk.

`func fileExporterFilenameLabel(LocalizedStringKey) -> some View`

On macOS, configures the `fileExporter` with a label for the file name field.

`func fileExporterFilenameLabel(Text?) -> some View`

On macOS, configures the `fileExporter` with a text to use as a label for the
file name field.

`func fileExporterFilenameLabel<S>(S) -> some View`

On macOS, configures the `fileExporter` with a label for the file name field.

Instance Method

# fileExporter(isPresented:documents:contentType:onCompletion:)

Presents a system interface for exporting a collection of reference type
documents to files on disk.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    func fileExporter<C>(
        isPresented: Binding<Bool>,
        documents: C,
        contentType: UTType,
        onCompletion: @escaping (Result<[URL], any Error>) -> Void
    ) -> some View where C : Collection, C.Element : ReferenceFileDocument
    

##  Parameters

`isPresented`

    

A binding to whether the interface should be shown.

`documents`

    

The collection of in-memory documents to export.

`contentType`

    

The content type to use for the exported file.

`onCompletion`

    

A callback that will be invoked when the operation has has succeeded or
failed.

`result`

    

A `Result` indicating whether the operation succeeded or failed.

## Discussion

In order for the interface to appear, both `isPresented` must be `true` and
`documents` must not be empty. When the operation is finished, `isPresented`
will be set to `false` before `onCompletion` is called. If the user cancels
the operation, `isPresented` will be set to `false` and `onCompletion` will
not be called.

The `contentType` provided must be included within the document type’s
`writableContentTypes`, otherwise the first valid writable content type will
be used instead.

## See Also

### Exporting to file

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType:
UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void) -> some View`

Presents a system interface for exporting a document that’s stored in a value
type, like a structure, to a file on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType:
UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void) -> some View`

Presents a system interface for exporting a document that’s stored in a
reference type, like a class, to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType:
UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for exporting a collection of value type documents
to files on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system interface for allowing the user to export a `FileDocument`
to a file on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system dialog for allowing the user to export a
`ReferenceFileDocument` to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system dialog for allowing the user to export a collection of
documents that conform to `ReferenceFileDocument` to files on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system dialog for allowing the user to export a collection of
documents that conform to `FileDocument` to files on disk.

`func fileExporter<T>(isPresented: Binding<Bool>, item: T?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system interface allowing the user to export a `Transferable` item
to file on disk.

`func fileExporter<C, T>(isPresented: Binding<Bool>, items: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system interface allowing the user to export a collection of items
to files on disk.

`func fileExporterFilenameLabel(LocalizedStringKey) -> some View`

On macOS, configures the `fileExporter` with a label for the file name field.

`func fileExporterFilenameLabel(Text?) -> some View`

On macOS, configures the `fileExporter` with a text to use as a label for the
file name field.

`func fileExporterFilenameLabel<S>(S) -> some View`

On macOS, configures the `fileExporter` with a label for the file name field.

Instance Method

# fileExporter(isPresented:documents:contentType:onCompletion:)

Presents a system interface for exporting a collection of value type documents
to files on disk.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    func fileExporter<C>(
        isPresented: Binding<Bool>,
        documents: C,
        contentType: UTType,
        onCompletion: @escaping (Result<[URL], any Error>) -> Void
    ) -> some View where C : Collection, C.Element : FileDocument
    

##  Parameters

`isPresented`

    

A binding to whether the interface should be shown.

`documents`

    

The collection of in-memory documents to export.

`contentType`

    

The content type to use for the exported file.

`onCompletion`

    

A callback that will be invoked when the operation has has succeeded or
failed.

`result`

    

A `Result` indicating whether the operation succeeded or failed.

## Discussion

In order for the interface to appear, both `isPresented` must be `true` and
`documents` must not be empty. When the operation is finished, `isPresented`
will be set to `false` before `onCompletion` is called. If the user cancels
the operation, `isPresented` will be set to `false` and `onCompletion` will
not be called.

The `contentType` provided must be included within the document type’s
`writableContentTypes`, otherwise the first valid writable content type will
be used instead.

## See Also

### Exporting to file

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType:
UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void) -> some View`

Presents a system interface for exporting a document that’s stored in a value
type, like a structure, to a file on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType:
UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void) -> some View`

Presents a system interface for exporting a document that’s stored in a
reference type, like a class, to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType:
UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for exporting a collection of reference type
documents to files on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system interface for allowing the user to export a `FileDocument`
to a file on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system dialog for allowing the user to export a
`ReferenceFileDocument` to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system dialog for allowing the user to export a collection of
documents that conform to `ReferenceFileDocument` to files on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system dialog for allowing the user to export a collection of
documents that conform to `FileDocument` to files on disk.

`func fileExporter<T>(isPresented: Binding<Bool>, item: T?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system interface allowing the user to export a `Transferable` item
to file on disk.

`func fileExporter<C, T>(isPresented: Binding<Bool>, items: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system interface allowing the user to export a collection of items
to files on disk.

`func fileExporterFilenameLabel(LocalizedStringKey) -> some View`

On macOS, configures the `fileExporter` with a label for the file name field.

`func fileExporterFilenameLabel(Text?) -> some View`

On macOS, configures the `fileExporter` with a text to use as a label for the
file name field.

`func fileExporterFilenameLabel<S>(S) -> some View`

On macOS, configures the `fileExporter` with a label for the file name field.

Instance Method

#
fileExporter(isPresented:document:contentTypes:defaultFilename:onCompletion:onCancellation:)

Presents a system interface for allowing the user to export a `FileDocument`
to a file on disk.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func fileExporter<D>(
        isPresented: Binding<Bool>,
        document: D?,
        contentTypes: [UTType] = [],
        defaultFilename: String? = nil,
        onCompletion: @escaping (Result<URL, any Error>) -> Void,
        onCancellation: @escaping () -> Void = {}
    ) -> some View where D : FileDocument
    

##  Parameters

`isPresented`

    

A binding to whether the interface should be shown.

`document`

    

The in-memory document to export.

`contentTypes`

    

The list of supported content types which can be exported. If not provided,
`FileDocument.writableContentTypes` are used.

`defaultFilename`

    

If provided, the default name to use for the exported file, which will the
user will have an opportunity to edit prior to the export.

`onCompletion`

    

A callback that will be invoked when the operation has succeeded or failed.
The `result` indicates whether the operation succeeded or failed.

`onCancellation`

    

A callback that will be invoked if the user cancels the operation.

## Discussion

In order for the interface to appear, `isPresented` must be `true`. When the
operation is finished, `isPresented` will be set to `false` before
`onCompletion` is called. If the user cancels the operation, `isPresented`
will be set to `false` and `onCancellation` will be called.

## See Also

### Exporting to file

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType:
UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void) -> some View`

Presents a system interface for exporting a document that’s stored in a value
type, like a structure, to a file on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType:
UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void) -> some View`

Presents a system interface for exporting a document that’s stored in a
reference type, like a class, to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType:
UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for exporting a collection of value type documents
to files on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType:
UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for exporting a collection of reference type
documents to files on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system dialog for allowing the user to export a
`ReferenceFileDocument` to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system dialog for allowing the user to export a collection of
documents that conform to `ReferenceFileDocument` to files on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system dialog for allowing the user to export a collection of
documents that conform to `FileDocument` to files on disk.

`func fileExporter<T>(isPresented: Binding<Bool>, item: T?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system interface allowing the user to export a `Transferable` item
to file on disk.

`func fileExporter<C, T>(isPresented: Binding<Bool>, items: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system interface allowing the user to export a collection of items
to files on disk.

`func fileExporterFilenameLabel(LocalizedStringKey) -> some View`

On macOS, configures the `fileExporter` with a label for the file name field.

`func fileExporterFilenameLabel(Text?) -> some View`

On macOS, configures the `fileExporter` with a text to use as a label for the
file name field.

`func fileExporterFilenameLabel<S>(S) -> some View`

On macOS, configures the `fileExporter` with a label for the file name field.

Instance Method

#
fileExporter(isPresented:document:contentTypes:defaultFilename:onCompletion:onCancellation:)

Presents a system dialog for allowing the user to export a
`ReferenceFileDocument` to a file on disk.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func fileExporter<D>(
        isPresented: Binding<Bool>,
        document: D?,
        contentTypes: [UTType] = [],
        defaultFilename: String? = nil,
        onCompletion: @escaping (Result<URL, any Error>) -> Void,
        onCancellation: @escaping () -> Void = {}
    ) -> some View where D : ReferenceFileDocument
    

##  Parameters

`isPresented`

    

A binding to whether the dialog should be shown.

`document`

    

The in-memory document to export.

`contentTypes`

    

The list of supported content types which can be exported. If not provided,
`ReferenceFileDocument.writableContentTypes` are used.

`defaultFilename`

    

If provided, the default name to use for the exported file, which will the
user will have an opportunity to edit prior to the export.

`onCompletion`

    

A callback that will be invoked when the operation has succeeded or failed.
The `result` indicates whether the operation succeeded or failed.

`onCancellation`

    

A callback that will be invoked if the user cancels the operation.

## Discussion

In order for the dialog to appear, `isPresented` must be `true`. When the
operation is finished, `isPresented` will be set to `false` before
`onCompletion` is called. If the user cancels the operation, `isPresented`
will be set to `false` and `onCancellation` will be called.

## See Also

### Exporting to file

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType:
UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void) -> some View`

Presents a system interface for exporting a document that’s stored in a value
type, like a structure, to a file on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType:
UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void) -> some View`

Presents a system interface for exporting a document that’s stored in a
reference type, like a class, to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType:
UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for exporting a collection of value type documents
to files on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType:
UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for exporting a collection of reference type
documents to files on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system interface for allowing the user to export a `FileDocument`
to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system dialog for allowing the user to export a collection of
documents that conform to `ReferenceFileDocument` to files on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system dialog for allowing the user to export a collection of
documents that conform to `FileDocument` to files on disk.

`func fileExporter<T>(isPresented: Binding<Bool>, item: T?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system interface allowing the user to export a `Transferable` item
to file on disk.

`func fileExporter<C, T>(isPresented: Binding<Bool>, items: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system interface allowing the user to export a collection of items
to files on disk.

`func fileExporterFilenameLabel(LocalizedStringKey) -> some View`

On macOS, configures the `fileExporter` with a label for the file name field.

`func fileExporterFilenameLabel(Text?) -> some View`

On macOS, configures the `fileExporter` with a text to use as a label for the
file name field.

`func fileExporterFilenameLabel<S>(S) -> some View`

On macOS, configures the `fileExporter` with a label for the file name field.

Instance Method

#
fileExporter(isPresented:documents:contentTypes:onCompletion:onCancellation:)

Presents a system dialog for allowing the user to export a collection of
documents that conform to `ReferenceFileDocument` to files on disk.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func fileExporter<C>(
        isPresented: Binding<Bool>,
        documents: C,
        contentTypes: [UTType] = [],
        onCompletion: @escaping (Result<[URL], any Error>) -> Void,
        onCancellation: @escaping () -> Void = {}
    ) -> some View where C : Collection, C.Element : ReferenceFileDocument
    

##  Parameters

`isPresented`

    

A binding to whether the dialog should be shown.

`documents`

    

The in-memory documents to export.

`contentTypes`

    

The list of supported content types which can be exported. If not provided,
`ReferenceFileDocument.writableContentTypes` are used.

`onCompletion`

    

A callback that will be invoked when the operation has succeeded or failed.
The `result` indicates whether the operation succeeded or failed.

`onCancellation`

    

A callback that will be invoked if the user cancels the operation.

## Discussion

In order for the dialog to appear, `isPresented` must be `true`. When the
operation is finished, `isPresented` will be set to `false` before
`onCompletion` is called. If the user cancels the operation, `isPresented`
will be set to `false` and `onCancellation` will be called.

## See Also

### Exporting to file

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType:
UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void) -> some View`

Presents a system interface for exporting a document that’s stored in a value
type, like a structure, to a file on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType:
UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void) -> some View`

Presents a system interface for exporting a document that’s stored in a
reference type, like a class, to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType:
UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for exporting a collection of value type documents
to files on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType:
UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for exporting a collection of reference type
documents to files on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system interface for allowing the user to export a `FileDocument`
to a file on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system dialog for allowing the user to export a
`ReferenceFileDocument` to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system dialog for allowing the user to export a collection of
documents that conform to `FileDocument` to files on disk.

`func fileExporter<T>(isPresented: Binding<Bool>, item: T?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system interface allowing the user to export a `Transferable` item
to file on disk.

`func fileExporter<C, T>(isPresented: Binding<Bool>, items: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system interface allowing the user to export a collection of items
to files on disk.

`func fileExporterFilenameLabel(LocalizedStringKey) -> some View`

On macOS, configures the `fileExporter` with a label for the file name field.

`func fileExporterFilenameLabel(Text?) -> some View`

On macOS, configures the `fileExporter` with a text to use as a label for the
file name field.

`func fileExporterFilenameLabel<S>(S) -> some View`

On macOS, configures the `fileExporter` with a label for the file name field.

Instance Method

#
fileExporter(isPresented:documents:contentTypes:onCompletion:onCancellation:)

Presents a system dialog for allowing the user to export a collection of
documents that conform to `FileDocument` to files on disk.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func fileExporter<C>(
        isPresented: Binding<Bool>,
        documents: C,
        contentTypes: [UTType] = [],
        onCompletion: @escaping (Result<[URL], any Error>) -> Void,
        onCancellation: @escaping () -> Void = {}
    ) -> some View where C : Collection, C.Element : FileDocument
    

##  Parameters

`isPresented`

    

A binding to whether the dialog should be shown.

`documents`

    

The in-memory documents to export.

`contentTypes`

    

The list of supported content types which can be exported. If not provided,
`FileDocument.writableContentTypes` are used.

`onCompletion`

    

A callback that will be invoked when the operation has succeeded or failed.
The `result` indicates whether the operation succeeded or failed.

`onCancellation`

    

A callback that will be invoked if the user cancels the operation.

## Discussion

In order for the dialog to appear, `isPresented` must be `true`. When the
operation is finished, `isPresented` will be set to `false` before
`onCompletion` is called. If the user cancels the operation, `isPresented`
will be set to `false` and `onCancellation` will be called.

## See Also

### Exporting to file

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType:
UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void) -> some View`

Presents a system interface for exporting a document that’s stored in a value
type, like a structure, to a file on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType:
UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void) -> some View`

Presents a system interface for exporting a document that’s stored in a
reference type, like a class, to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType:
UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for exporting a collection of value type documents
to files on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType:
UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for exporting a collection of reference type
documents to files on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system interface for allowing the user to export a `FileDocument`
to a file on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system dialog for allowing the user to export a
`ReferenceFileDocument` to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system dialog for allowing the user to export a collection of
documents that conform to `ReferenceFileDocument` to files on disk.

`func fileExporter<T>(isPresented: Binding<Bool>, item: T?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system interface allowing the user to export a `Transferable` item
to file on disk.

`func fileExporter<C, T>(isPresented: Binding<Bool>, items: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system interface allowing the user to export a collection of items
to files on disk.

`func fileExporterFilenameLabel(LocalizedStringKey) -> some View`

On macOS, configures the `fileExporter` with a label for the file name field.

`func fileExporterFilenameLabel(Text?) -> some View`

On macOS, configures the `fileExporter` with a text to use as a label for the
file name field.

`func fileExporterFilenameLabel<S>(S) -> some View`

On macOS, configures the `fileExporter` with a label for the file name field.

Instance Method

#
fileExporter(isPresented:item:contentTypes:defaultFilename:onCompletion:onCancellation:)

Presents a system interface allowing the user to export a `Transferable` item
to file on disk.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func fileExporter<T>(
        isPresented: Binding<Bool>,
        item: T?,
        contentTypes: [UTType] = [],
        defaultFilename: String? = nil,
        onCompletion: @escaping (Result<URL, any Error>) -> Void,
        onCancellation: @escaping () -> Void = { }
    ) -> some View where T : Transferable
    

##  Parameters

`isPresented`

    

A binding to whether the interface should be shown.

`item`

    

The item to be saved on disk.

`contentTypes`

    

The optional content types to use for the exported file. If empty, SwiftUI
uses the content types from the `transferRepresentation` property provided for
`Transferable` conformance.

`onCompletion`

    

A callback that will be invoked when the operation has succeeded or failed.

`onCancellation`

    

A callback that will be invoked if the operation was cancelled.

## Discussion

In order for the interface to appear `isPresented` must be set to `true`. When
the operation is finished, `isPresented` will be set to `false` before
`onCompletion` is called. If the user cancels the operation, `isPresented`
will be set to `false` and `onCompletion` will not be called.

## See Also

### Exporting to file

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType:
UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void) -> some View`

Presents a system interface for exporting a document that’s stored in a value
type, like a structure, to a file on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType:
UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void) -> some View`

Presents a system interface for exporting a document that’s stored in a
reference type, like a class, to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType:
UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for exporting a collection of value type documents
to files on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType:
UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for exporting a collection of reference type
documents to files on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system interface for allowing the user to export a `FileDocument`
to a file on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system dialog for allowing the user to export a
`ReferenceFileDocument` to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system dialog for allowing the user to export a collection of
documents that conform to `ReferenceFileDocument` to files on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system dialog for allowing the user to export a collection of
documents that conform to `FileDocument` to files on disk.

`func fileExporter<C, T>(isPresented: Binding<Bool>, items: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system interface allowing the user to export a collection of items
to files on disk.

`func fileExporterFilenameLabel(LocalizedStringKey) -> some View`

On macOS, configures the `fileExporter` with a label for the file name field.

`func fileExporterFilenameLabel(Text?) -> some View`

On macOS, configures the `fileExporter` with a text to use as a label for the
file name field.

`func fileExporterFilenameLabel<S>(S) -> some View`

On macOS, configures the `fileExporter` with a label for the file name field.

Instance Method

# fileExporter(isPresented:items:contentTypes:onCompletion:onCancellation:)

Presents a system interface allowing the user to export a collection of items
to files on disk.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func fileExporter<C, T>(
        isPresented: Binding<Bool>,
        items: C,
        contentTypes: [UTType] = [],
        onCompletion: @escaping (Result<[URL], any Error>) -> Void,
        onCancellation: @escaping () -> Void = { }
    ) -> some View where C : Collection, T : Transferable, T == C.Element
    

##  Parameters

`isPresented`

    

A binding to whether the interface should be shown.

`items`

    

Collection of values to be saved on disk.

`contentTypes`

    

The content types to use for the exported file. If empty, SwiftUI uses the
content types from the `transferRepresentation` property provided for
`Transferable` conformance.

`allowsOtherContentTypes`

    

A Boolean value that indicates if the users are allowed to save the files with
a different file extension than specified by the `contentType` property.

`onCompletion`

    

A callback that will be invoked when the operation has has succeeded or
failed.

`onCancellation`

    

A callback that will be invoked if the operation was cancelled.

## Discussion

In order for the interface to appear `isPresented` must be set to `true`. When
the operation is finished, `isPresented` will be set to `false` before
`onCompletion` is called. If the user cancels the operation, `isPresented`
will be set to `false` and `onCompletion` will not be called.

## See Also

### Exporting to file

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType:
UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void) -> some View`

Presents a system interface for exporting a document that’s stored in a value
type, like a structure, to a file on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType:
UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void) -> some View`

Presents a system interface for exporting a document that’s stored in a
reference type, like a class, to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType:
UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for exporting a collection of value type documents
to files on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType:
UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for exporting a collection of reference type
documents to files on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system interface for allowing the user to export a `FileDocument`
to a file on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system dialog for allowing the user to export a
`ReferenceFileDocument` to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system dialog for allowing the user to export a collection of
documents that conform to `ReferenceFileDocument` to files on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system dialog for allowing the user to export a collection of
documents that conform to `FileDocument` to files on disk.

`func fileExporter<T>(isPresented: Binding<Bool>, item: T?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system interface allowing the user to export a `Transferable` item
to file on disk.

`func fileExporterFilenameLabel(LocalizedStringKey) -> some View`

On macOS, configures the `fileExporter` with a label for the file name field.

`func fileExporterFilenameLabel(Text?) -> some View`

On macOS, configures the `fileExporter` with a text to use as a label for the
file name field.

`func fileExporterFilenameLabel<S>(S) -> some View`

On macOS, configures the `fileExporter` with a label for the file name field.

Instance Method

# fileExporterFilenameLabel(_:)

On macOS, configures the `fileExporter` with a label for the file name field.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func fileExporterFilenameLabel(_ labelKey: LocalizedStringKey) -> some View
    

##  Parameters

`labelKey`

    

The key to a localized string to display.

## See Also

### Exporting to file

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType:
UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void) -> some View`

Presents a system interface for exporting a document that’s stored in a value
type, like a structure, to a file on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType:
UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void) -> some View`

Presents a system interface for exporting a document that’s stored in a
reference type, like a class, to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType:
UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for exporting a collection of value type documents
to files on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType:
UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for exporting a collection of reference type
documents to files on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system interface for allowing the user to export a `FileDocument`
to a file on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system dialog for allowing the user to export a
`ReferenceFileDocument` to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system dialog for allowing the user to export a collection of
documents that conform to `ReferenceFileDocument` to files on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system dialog for allowing the user to export a collection of
documents that conform to `FileDocument` to files on disk.

`func fileExporter<T>(isPresented: Binding<Bool>, item: T?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system interface allowing the user to export a `Transferable` item
to file on disk.

`func fileExporter<C, T>(isPresented: Binding<Bool>, items: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system interface allowing the user to export a collection of items
to files on disk.

`func fileExporterFilenameLabel(Text?) -> some View`

On macOS, configures the `fileExporter` with a text to use as a label for the
file name field.

`func fileExporterFilenameLabel<S>(S) -> some View`

On macOS, configures the `fileExporter` with a label for the file name field.

Instance Method

# fileExporterFilenameLabel(_:)

On macOS, configures the `fileExporter` with a text to use as a label for the
file name field.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func fileExporterFilenameLabel(_ label: Text?) -> some View
    

##  Parameters

`label`

    

The optional text to use as the label for the file name field.

## See Also

### Exporting to file

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType:
UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void) -> some View`

Presents a system interface for exporting a document that’s stored in a value
type, like a structure, to a file on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType:
UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void) -> some View`

Presents a system interface for exporting a document that’s stored in a
reference type, like a class, to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType:
UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for exporting a collection of value type documents
to files on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType:
UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for exporting a collection of reference type
documents to files on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system interface for allowing the user to export a `FileDocument`
to a file on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system dialog for allowing the user to export a
`ReferenceFileDocument` to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system dialog for allowing the user to export a collection of
documents that conform to `ReferenceFileDocument` to files on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system dialog for allowing the user to export a collection of
documents that conform to `FileDocument` to files on disk.

`func fileExporter<T>(isPresented: Binding<Bool>, item: T?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system interface allowing the user to export a `Transferable` item
to file on disk.

`func fileExporter<C, T>(isPresented: Binding<Bool>, items: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system interface allowing the user to export a collection of items
to files on disk.

`func fileExporterFilenameLabel(LocalizedStringKey) -> some View`

On macOS, configures the `fileExporter` with a label for the file name field.

`func fileExporterFilenameLabel<S>(S) -> some View`

On macOS, configures the `fileExporter` with a label for the file name field.

Instance Method

# fileExporterFilenameLabel(_:)

On macOS, configures the `fileExporter` with a label for the file name field.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func fileExporterFilenameLabel<S>(_ label: S) -> some View where S : StringProtocol
    

##  Parameters

`label`

    

The string to use as the label for the file name field.

## See Also

### Exporting to file

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType:
UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void) -> some View`

Presents a system interface for exporting a document that’s stored in a value
type, like a structure, to a file on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType:
UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void) -> some View`

Presents a system interface for exporting a document that’s stored in a
reference type, like a class, to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType:
UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for exporting a collection of value type documents
to files on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType:
UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for exporting a collection of reference type
documents to files on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system interface for allowing the user to export a `FileDocument`
to a file on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system dialog for allowing the user to export a
`ReferenceFileDocument` to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system dialog for allowing the user to export a collection of
documents that conform to `ReferenceFileDocument` to files on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system dialog for allowing the user to export a collection of
documents that conform to `FileDocument` to files on disk.

`func fileExporter<T>(isPresented: Binding<Bool>, item: T?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system interface allowing the user to export a `Transferable` item
to file on disk.

`func fileExporter<C, T>(isPresented: Binding<Bool>, items: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system interface allowing the user to export a collection of items
to files on disk.

`func fileExporterFilenameLabel(LocalizedStringKey) -> some View`

On macOS, configures the `fileExporter` with a label for the file name field.

`func fileExporterFilenameLabel(Text?) -> some View`

On macOS, configures the `fileExporter` with a text to use as a label for the
file name field.

Instance Method

#
fileImporter(isPresented:allowedContentTypes:allowsMultipleSelection:onCompletion:)

Presents a system interface for allowing the user to import multiple files.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    func fileImporter(
        isPresented: Binding<Bool>,
        allowedContentTypes: [UTType],
        allowsMultipleSelection: Bool,
        onCompletion: @escaping (Result<[URL], any Error>) -> Void
    ) -> some View
    

##  Parameters

`isPresented`

    

A binding to whether the interface should be shown.

`allowedContentTypes`

    

The list of supported content types which can be imported.

`allowsMultipleSelection`

    

Whether the importer allows the user to select more than one file to import.

`onCompletion`

    

A callback that will be invoked when the operation has succeeded or failed. To
access the received URLs, call `startAccessingSecurityScopedResource`. When
the access is no longer required, call `stopAccessingSecurityScopedResource`.

`result`

    

A `Result` indicating whether the operation succeeded or failed.

## Discussion

In order for the interface to appear, `isPresented` must be `true`. When the
operation is finished, `isPresented` will be set to `false` before
`onCompletion` is called. If the user cancels the operation, `isPresented`
will be set to `false` and `onCompletion` will not be called.

Note

This dialog provides security-scoped URLs. Call the
`startAccessingSecurityScopedResource` method to access or bookmark the URLs,
and the `stopAccessingSecurityScopedResource` method to release the access.

For example, a button that allows the user to choose multiple PDF files for
the application to combine them later, might look like this:

Note

Changing `allowedContentTypes` or `allowsMultipleSelection` while the file
importer is presented will have no immediate effect, however will apply the
next time it is presented.

## See Also

### Importing from file

`func fileImporter(isPresented: Binding<Bool>, allowedContentTypes: [UTType],
onCompletion: (Result<URL, any Error>) -> Void) -> some View`

Presents a system interface for allowing the user to import an existing file.

`func fileImporter(isPresented: Binding<Bool>, allowedContentTypes: [UTType],
allowsMultipleSelection: Bool, onCompletion: (Result<[URL], any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system dialog for allowing the user to import multiple files.

Instance Method

# fileImporter(isPresented:allowedContentTypes:onCompletion:)

Presents a system interface for allowing the user to import an existing file.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    func fileImporter(
        isPresented: Binding<Bool>,
        allowedContentTypes: [UTType],
        onCompletion: @escaping (Result<URL, any Error>) -> Void
    ) -> some View
    

##  Parameters

`isPresented`

    

A binding to whether the interface should be shown.

`allowedContentTypes`

    

The list of supported content types which can be imported.

`onCompletion`

    

A callback that will be invoked when the operation has succeeded or failed. To
access the received URLs, call `startAccessingSecurityScopedResource`. When
the access is no longer required, call `stopAccessingSecurityScopedResource`.

`result`

    

A `Result` indicating whether the operation succeeded or failed.

## Discussion

In order for the interface to appear, `isPresented` must be `true`. When the
operation is finished, `isPresented` will be set to `false` before
`onCompletion` is called. If the user cancels the operation, `isPresented`
will be set to `false` and `onCompletion` will not be called.

Note

This dialog provides security-scoped URLs. Call the
`startAccessingSecurityScopedResource` method to access or bookmark the URLs,
and the `stopAccessingSecurityScopedResource` method to release the access.

For example, an application can have a button that allows the user to choose
the default directory with document templates loaded on every launch. Such a
button might look like this:

Note

Changing `allowedContentTypes` while the file importer is presented will have
no immediate effect, however will apply the next time it is presented.

## See Also

### Importing from file

`func fileImporter(isPresented: Binding<Bool>, allowedContentTypes: [UTType],
allowsMultipleSelection: Bool, onCompletion: (Result<[URL], any Error>) ->
Void) -> some View`

Presents a system interface for allowing the user to import multiple files.

`func fileImporter(isPresented: Binding<Bool>, allowedContentTypes: [UTType],
allowsMultipleSelection: Bool, onCompletion: (Result<[URL], any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system dialog for allowing the user to import multiple files.

Instance Method

#
fileImporter(isPresented:allowedContentTypes:allowsMultipleSelection:onCompletion:onCancellation:)

Presents a system dialog for allowing the user to import multiple files.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func fileImporter(
        isPresented: Binding<Bool>,
        allowedContentTypes: [UTType],
        allowsMultipleSelection: Bool,
        onCompletion: @escaping (Result<[URL], any Error>) -> Void,
        onCancellation: @escaping () -> Void
    ) -> some View
    

##  Parameters

`isPresented`

    

A binding to whether the dialog should be shown.

`allowedContentTypes`

    

The list of supported content types which can be imported.

`allowsMultipleSelection`

    

Whether the importer allows the user to select more than one file to import.

`onCompletion`

    

A callback that will be invoked when the operation has succeeded or failed.
The `result` indicates whether the operation succeeded or failed. To access
the received URLs, call `startAccessingSecurityScopedResource`. When the
access is no longer required, call `stopAccessingSecurityScopedResource`.

`onCancellation`

    

A callback that will be invoked if the user cancels the operation.

## Discussion

In order for the dialog to appear, `isPresented` must be `true`. When the
operation is finished, `isPresented` will be set to `false` before
`onCompletion` is called. If the user cancels the operation, `isPresented`
will be set to `false` and `onCompletion` will not be called.

Note

This dialog provides security-scoped URLs. Call the
`startAccessingSecurityScopedResource` method to access or bookmark the URLs,
and the `stopAccessingSecurityScopedResource` method to release the access.

For example, a button that allows the user to choose multiple PDF files for
the application to combine them later, might look like this:

Note

Changing `allowedContentTypes` or `allowsMultipleSelection` while the file
importer is presented will have no immediate effect, however will apply the
next time it is presented.

## See Also

### Importing from file

`func fileImporter(isPresented: Binding<Bool>, allowedContentTypes: [UTType],
allowsMultipleSelection: Bool, onCompletion: (Result<[URL], any Error>) ->
Void) -> some View`

Presents a system interface for allowing the user to import multiple files.

`func fileImporter(isPresented: Binding<Bool>, allowedContentTypes: [UTType],
onCompletion: (Result<URL, any Error>) -> Void) -> some View`

Presents a system interface for allowing the user to import an existing file.

Instance Method

# fileMover(isPresented:file:onCompletion:)

Presents a system interface for allowing the user to move an existing file to
a new location.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    func fileMover(
        isPresented: Binding<Bool>,
        file: URL?,
        onCompletion: @escaping (Result<URL, any Error>) -> Void
    ) -> some View
    

##  Parameters

`isPresented`

    

A binding to whether the interface should be shown.

`file`

    

The `URL` of the file to be moved.

`onCompletion`

    

A callback that will be invoked when the operation has has succeeded or
failed. To access the received URLs, call
`startAccessingSecurityScopedResource`. When the access is no longer required,
call `stopAccessingSecurityScopedResource`.

`result`

    

A `Result` indicating whether the operation succeeded or failed.

## Discussion

Note

This interface provides security-scoped URLs. Call the
`startAccessingSecurityScopedResource` method to access or bookmark the URLs,
and the `stopAccessingSecurityScopedResource` method to release the access.

In order for the interface to appear, both `isPresented` must be `true` and
`file` must not be `nil`. When the operation is finished, `isPresented` will
be set to `false` before `onCompletion` is called. If the user cancels the
operation, `isPresented` will be set to `false` and `onCompletion` will not be
called.

## See Also

### Moving a file

`func fileMover<C>(isPresented: Binding<Bool>, files: C, onCompletion:
(Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for allowing the user to move a collection of
existing files to a new location.

`func fileMover(isPresented: Binding<Bool>, file: URL?, onCompletion:
(Result<URL, any Error>) -> Void, onCancellation: () -> Void) -> some View`

Presents a system dialog for allowing the user to move an existing file to a
new location.

`func fileMover<C>(isPresented: Binding<Bool>, files: C, onCompletion:
(Result<[URL], any Error>) -> Void, onCancellation: () -> Void) -> some View`

Presents a system dialog for allowing the user to move a collection of
existing files to a new location.

Instance Method

# fileMover(isPresented:files:onCompletion:)

Presents a system interface for allowing the user to move a collection of
existing files to a new location.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    func fileMover<C>(
        isPresented: Binding<Bool>,
        files: C,
        onCompletion: @escaping (Result<[URL], any Error>) -> Void
    ) -> some View where C : Collection, C.Element == URL
    

##  Parameters

`isPresented`

    

A binding to whether the interface should be shown.

`files`

    

A collection of `URL`s for the files to be moved.

`onCompletion`

    

A callback that will be invoked when the operation has has succeeded or
failed. To access the received URLs, call
`startAccessingSecurityScopedResource`. When the access is no longer required,
call `stopAccessingSecurityScopedResource`.

`result`

    

A `Result` indicating whether the operation succeeded or failed.

## Discussion

Note

This interface provides security-scoped URLs. Call the
`startAccessingSecurityScopedResource` method to access or bookmark the URLs,
and the `stopAccessingSecurityScopedResource` method to release the access.

In order for the interface to appear, both `isPresented` must be `true` and
`files` must not be empty. When the operation is finished, `isPresented` will
be set to `false` before `onCompletion` is called. If the user cancels the
operation, `isPresented` will be set to `false` and `onCompletion` will not be
called.

## See Also

### Moving a file

`func fileMover(isPresented: Binding<Bool>, file: URL?, onCompletion:
(Result<URL, any Error>) -> Void) -> some View`

Presents a system interface for allowing the user to move an existing file to
a new location.

`func fileMover(isPresented: Binding<Bool>, file: URL?, onCompletion:
(Result<URL, any Error>) -> Void, onCancellation: () -> Void) -> some View`

Presents a system dialog for allowing the user to move an existing file to a
new location.

`func fileMover<C>(isPresented: Binding<Bool>, files: C, onCompletion:
(Result<[URL], any Error>) -> Void, onCancellation: () -> Void) -> some View`

Presents a system dialog for allowing the user to move a collection of
existing files to a new location.

Instance Method

# fileMover(isPresented:file:onCompletion:onCancellation:)

Presents a system dialog for allowing the user to move an existing file to a
new location.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func fileMover(
        isPresented: Binding<Bool>,
        file: URL?,
        onCompletion: @escaping (Result<URL, any Error>) -> Void,
        onCancellation: @escaping () -> Void
    ) -> some View
    

##  Parameters

`isPresented`

    

A binding to whether the dialog should be shown.

`file`

    

The URL of the file to be moved.

`onCompletion`

    

A callback that will be invoked when the operation has succeeded or failed.
The `result` indicates whether the operation succeeded or failed. To access
the received URLs, call `startAccessingSecurityScopedResource`. When the
access is no longer required, call `stopAccessingSecurityScopedResource`.

`onCancellation`

    

A callback that will be invoked if the user cancels the operation.

## Discussion

Note

This dialog provides security-scoped URLs. Call the
`startAccessingSecurityScopedResource` method to access or bookmark the URLs,
and the `stopAccessingSecurityScopedResource` method to release the access.

For example, a button that allows the user to move a file might look like
this:

## See Also

### Moving a file

`func fileMover(isPresented: Binding<Bool>, file: URL?, onCompletion:
(Result<URL, any Error>) -> Void) -> some View`

Presents a system interface for allowing the user to move an existing file to
a new location.

`func fileMover<C>(isPresented: Binding<Bool>, files: C, onCompletion:
(Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for allowing the user to move a collection of
existing files to a new location.

`func fileMover<C>(isPresented: Binding<Bool>, files: C, onCompletion:
(Result<[URL], any Error>) -> Void, onCancellation: () -> Void) -> some View`

Presents a system dialog for allowing the user to move a collection of
existing files to a new location.

Instance Method

# fileMover(isPresented:files:onCompletion:onCancellation:)

Presents a system dialog for allowing the user to move a collection of
existing files to a new location.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func fileMover<C>(
        isPresented: Binding<Bool>,
        files: C,
        onCompletion: @escaping (Result<[URL], any Error>) -> Void,
        onCancellation: @escaping () -> Void
    ) -> some View where C : Collection, C.Element == URL
    

##  Parameters

`isPresented`

    

A binding to whether the dialog should be shown.

`files`

    

A collection of URLs for the files to be moved.

`onCompletion`

    

A callback that will be invoked when the operation has succeeded or failed.
The `result` indicates whether the operation succeeded or failed. To access
the received URLs, call `startAccessingSecurityScopedResource`. When the
access is no longer required, call `stopAccessingSecurityScopedResource`.

`onCancellation`

    

A callback that will be invoked if the user cancels the operation.

## Discussion

Note

This dialog provides security-scoped URLs. Call the
`startAccessingSecurityScopedResource` method to access or bookmark the URLs,
and the `stopAccessingSecurityScopedResource` method to release the access.

For example, a button that allows the user to move files might look like this:

## See Also

### Moving a file

`func fileMover(isPresented: Binding<Bool>, file: URL?, onCompletion:
(Result<URL, any Error>) -> Void) -> some View`

Presents a system interface for allowing the user to move an existing file to
a new location.

`func fileMover<C>(isPresented: Binding<Bool>, files: C, onCompletion:
(Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for allowing the user to move a collection of
existing files to a new location.

`func fileMover(isPresented: Binding<Bool>, file: URL?, onCompletion:
(Result<URL, any Error>) -> Void, onCancellation: () -> Void) -> some View`

Presents a system dialog for allowing the user to move an existing file to a
new location.

Instance Method

# fileDialogBrowserOptions(_:)

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to
provide a refined URL search experience: include or exclude hidden files,
allow searching by tag, etc.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func fileDialogBrowserOptions(_ options: FileDialogBrowserOptions) -> some View
    

##  Parameters

`options`

    

The search options to apply to a given file dialog.

## See Also

### Configuring a file dialog

`func fileDialogConfirmationLabel<S>(S) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom confirmation button label.

`func fileDialogConfirmationLabel(Text?) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with custom text as a confirmation button label.

`func fileDialogConfirmationLabel(LocalizedStringKey) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom confirmation button label.

`func fileDialogCustomizationID(String) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to
persist and restore the file dialog configuration.

`func fileDialogDefaultDirectory(URL?) -> some View`

Configures the `fileExporter`, `fileImporter`, or `fileMover` to open with the
specified default directory.

`func fileDialogImportsUnresolvedAliases(Bool) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover`
behavior when a user chooses an alias.

`func fileDialogMessage<S>(S) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom message that is presented to the user, similar to a title.

`func fileDialogMessage(Text?) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom text that is presented to the user, similar to a title.

`func fileDialogMessage(LocalizedStringKey) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom message that is presented to the user, similar to a title.

`func fileDialogURLEnabled(Predicate<URL>) -> some View`

On macOS, configures the the `fileImporter` or `fileMover` to conditionally
disable presented URLs.

`struct FileDialogBrowserOptions`

The way that file dialogs present the file system.

Instance Method

# fileDialogConfirmationLabel(_:)

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom confirmation button label.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func fileDialogConfirmationLabel<S>(_ label: S) -> some View where S : StringProtocol
    

##  Parameters

`label`

    

The string to use as the label for the confirmation button.

## See Also

### Configuring a file dialog

`func fileDialogBrowserOptions(FileDialogBrowserOptions) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to
provide a refined URL search experience: include or exclude hidden files,
allow searching by tag, etc.

`func fileDialogConfirmationLabel(Text?) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with custom text as a confirmation button label.

`func fileDialogConfirmationLabel(LocalizedStringKey) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom confirmation button label.

`func fileDialogCustomizationID(String) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to
persist and restore the file dialog configuration.

`func fileDialogDefaultDirectory(URL?) -> some View`

Configures the `fileExporter`, `fileImporter`, or `fileMover` to open with the
specified default directory.

`func fileDialogImportsUnresolvedAliases(Bool) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover`
behavior when a user chooses an alias.

`func fileDialogMessage<S>(S) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom message that is presented to the user, similar to a title.

`func fileDialogMessage(Text?) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom text that is presented to the user, similar to a title.

`func fileDialogMessage(LocalizedStringKey) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom message that is presented to the user, similar to a title.

`func fileDialogURLEnabled(Predicate<URL>) -> some View`

On macOS, configures the the `fileImporter` or `fileMover` to conditionally
disable presented URLs.

`struct FileDialogBrowserOptions`

The way that file dialogs present the file system.

Instance Method

# fileDialogConfirmationLabel(_:)

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with custom text as a confirmation button label.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func fileDialogConfirmationLabel(_ label: Text?) -> some View
    

##  Parameters

`label`

    

The optional text to use as the label for the confirmation button.

## See Also

### Configuring a file dialog

`func fileDialogBrowserOptions(FileDialogBrowserOptions) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to
provide a refined URL search experience: include or exclude hidden files,
allow searching by tag, etc.

`func fileDialogConfirmationLabel<S>(S) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom confirmation button label.

`func fileDialogConfirmationLabel(LocalizedStringKey) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom confirmation button label.

`func fileDialogCustomizationID(String) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to
persist and restore the file dialog configuration.

`func fileDialogDefaultDirectory(URL?) -> some View`

Configures the `fileExporter`, `fileImporter`, or `fileMover` to open with the
specified default directory.

`func fileDialogImportsUnresolvedAliases(Bool) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover`
behavior when a user chooses an alias.

`func fileDialogMessage<S>(S) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom message that is presented to the user, similar to a title.

`func fileDialogMessage(Text?) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom text that is presented to the user, similar to a title.

`func fileDialogMessage(LocalizedStringKey) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom message that is presented to the user, similar to a title.

`func fileDialogURLEnabled(Predicate<URL>) -> some View`

On macOS, configures the the `fileImporter` or `fileMover` to conditionally
disable presented URLs.

`struct FileDialogBrowserOptions`

The way that file dialogs present the file system.

Instance Method

# fileDialogConfirmationLabel(_:)

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom confirmation button label.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func fileDialogConfirmationLabel(_ labelKey: LocalizedStringKey) -> some View
    

##  Parameters

`labelKey`

    

The key to a localized string to display.

## See Also

### Configuring a file dialog

`func fileDialogBrowserOptions(FileDialogBrowserOptions) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to
provide a refined URL search experience: include or exclude hidden files,
allow searching by tag, etc.

`func fileDialogConfirmationLabel<S>(S) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom confirmation button label.

`func fileDialogConfirmationLabel(Text?) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with custom text as a confirmation button label.

`func fileDialogCustomizationID(String) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to
persist and restore the file dialog configuration.

`func fileDialogDefaultDirectory(URL?) -> some View`

Configures the `fileExporter`, `fileImporter`, or `fileMover` to open with the
specified default directory.

`func fileDialogImportsUnresolvedAliases(Bool) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover`
behavior when a user chooses an alias.

`func fileDialogMessage<S>(S) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom message that is presented to the user, similar to a title.

`func fileDialogMessage(Text?) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom text that is presented to the user, similar to a title.

`func fileDialogMessage(LocalizedStringKey) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom message that is presented to the user, similar to a title.

`func fileDialogURLEnabled(Predicate<URL>) -> some View`

On macOS, configures the the `fileImporter` or `fileMover` to conditionally
disable presented URLs.

`struct FileDialogBrowserOptions`

The way that file dialogs present the file system.

Instance Method

# fileDialogCustomizationID(_:)

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to
persist and restore the file dialog configuration.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func fileDialogCustomizationID(_ id: String) -> some View
    

##  Parameters

`id`

    

An identifier of the configuration.

## Discussion

Among other parameters, it stores the current directory, view style (e.g.,
Icons, List, Columns), recent places, and expanded window size. It enables a
refined user experience; for example, when importing an image, the user might
switch to the Icons view, but the List view could be more convenient in
another context. The file dialog stores these settings and applies them every
time before presenting the panel. If not provided, on every launch, the file
dialog uses the default configuration.

## See Also

### Configuring a file dialog

`func fileDialogBrowserOptions(FileDialogBrowserOptions) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to
provide a refined URL search experience: include or exclude hidden files,
allow searching by tag, etc.

`func fileDialogConfirmationLabel<S>(S) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom confirmation button label.

`func fileDialogConfirmationLabel(Text?) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with custom text as a confirmation button label.

`func fileDialogConfirmationLabel(LocalizedStringKey) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom confirmation button label.

`func fileDialogDefaultDirectory(URL?) -> some View`

Configures the `fileExporter`, `fileImporter`, or `fileMover` to open with the
specified default directory.

`func fileDialogImportsUnresolvedAliases(Bool) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover`
behavior when a user chooses an alias.

`func fileDialogMessage<S>(S) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom message that is presented to the user, similar to a title.

`func fileDialogMessage(Text?) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom text that is presented to the user, similar to a title.

`func fileDialogMessage(LocalizedStringKey) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom message that is presented to the user, similar to a title.

`func fileDialogURLEnabled(Predicate<URL>) -> some View`

On macOS, configures the the `fileImporter` or `fileMover` to conditionally
disable presented URLs.

`struct FileDialogBrowserOptions`

The way that file dialogs present the file system.

Instance Method

# fileDialogDefaultDirectory(_:)

Configures the `fileExporter`, `fileImporter`, or `fileMover` to open with the
specified default directory.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func fileDialogDefaultDirectory(_ defaultDirectory: URL?) -> some View
    

##  Parameters

`defaultDirectory`

    

The directory to show when the system file dialog launches. If the given file
dialog has a `fileDialogCustomizationID` if stores the user-chosen directory
and subsequently opens with it, ignoring the default value provided in this
modifier.

## See Also

### Configuring a file dialog

`func fileDialogBrowserOptions(FileDialogBrowserOptions) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to
provide a refined URL search experience: include or exclude hidden files,
allow searching by tag, etc.

`func fileDialogConfirmationLabel<S>(S) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom confirmation button label.

`func fileDialogConfirmationLabel(Text?) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with custom text as a confirmation button label.

`func fileDialogConfirmationLabel(LocalizedStringKey) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom confirmation button label.

`func fileDialogCustomizationID(String) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to
persist and restore the file dialog configuration.

`func fileDialogImportsUnresolvedAliases(Bool) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover`
behavior when a user chooses an alias.

`func fileDialogMessage<S>(S) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom message that is presented to the user, similar to a title.

`func fileDialogMessage(Text?) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom text that is presented to the user, similar to a title.

`func fileDialogMessage(LocalizedStringKey) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom message that is presented to the user, similar to a title.

`func fileDialogURLEnabled(Predicate<URL>) -> some View`

On macOS, configures the the `fileImporter` or `fileMover` to conditionally
disable presented URLs.

`struct FileDialogBrowserOptions`

The way that file dialogs present the file system.

Instance Method

# fileDialogImportsUnresolvedAliases(_:)

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover`
behavior when a user chooses an alias.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func fileDialogImportsUnresolvedAliases(_ imports: Bool) -> some View
    

##  Parameters

`imports`

    

A Boolean value that indicates if the application receives unresolved or
resolved URLs when a user chooses aliases.

## Discussion

By default, file dialogs resolve aliases and provide the URL of the item
referred to by the chosen alias. This modifier allows control of this
behavior: pass `true` if the application doesn’t want file dialog to resolve
aliases.

## See Also

### Configuring a file dialog

`func fileDialogBrowserOptions(FileDialogBrowserOptions) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to
provide a refined URL search experience: include or exclude hidden files,
allow searching by tag, etc.

`func fileDialogConfirmationLabel<S>(S) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom confirmation button label.

`func fileDialogConfirmationLabel(Text?) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with custom text as a confirmation button label.

`func fileDialogConfirmationLabel(LocalizedStringKey) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom confirmation button label.

`func fileDialogCustomizationID(String) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to
persist and restore the file dialog configuration.

`func fileDialogDefaultDirectory(URL?) -> some View`

Configures the `fileExporter`, `fileImporter`, or `fileMover` to open with the
specified default directory.

`func fileDialogMessage<S>(S) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom message that is presented to the user, similar to a title.

`func fileDialogMessage(Text?) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom text that is presented to the user, similar to a title.

`func fileDialogMessage(LocalizedStringKey) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom message that is presented to the user, similar to a title.

`func fileDialogURLEnabled(Predicate<URL>) -> some View`

On macOS, configures the the `fileImporter` or `fileMover` to conditionally
disable presented URLs.

`struct FileDialogBrowserOptions`

The way that file dialogs present the file system.

Instance Method

# fileDialogMessage(_:)

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom message that is presented to the user, similar to a title.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func fileDialogMessage<S>(_ message: S) -> some View where S : StringProtocol
    

##  Parameters

`message`

    

The string to use as the file dialog message.

## See Also

### Configuring a file dialog

`func fileDialogBrowserOptions(FileDialogBrowserOptions) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to
provide a refined URL search experience: include or exclude hidden files,
allow searching by tag, etc.

`func fileDialogConfirmationLabel<S>(S) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom confirmation button label.

`func fileDialogConfirmationLabel(Text?) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with custom text as a confirmation button label.

`func fileDialogConfirmationLabel(LocalizedStringKey) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom confirmation button label.

`func fileDialogCustomizationID(String) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to
persist and restore the file dialog configuration.

`func fileDialogDefaultDirectory(URL?) -> some View`

Configures the `fileExporter`, `fileImporter`, or `fileMover` to open with the
specified default directory.

`func fileDialogImportsUnresolvedAliases(Bool) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover`
behavior when a user chooses an alias.

`func fileDialogMessage(Text?) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom text that is presented to the user, similar to a title.

`func fileDialogMessage(LocalizedStringKey) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom message that is presented to the user, similar to a title.

`func fileDialogURLEnabled(Predicate<URL>) -> some View`

On macOS, configures the the `fileImporter` or `fileMover` to conditionally
disable presented URLs.

`struct FileDialogBrowserOptions`

The way that file dialogs present the file system.

Instance Method

# fileDialogMessage(_:)

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom text that is presented to the user, similar to a title.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func fileDialogMessage(_ message: Text?) -> some View
    

##  Parameters

`message`

    

The optional text to use as the file dialog message.

## See Also

### Configuring a file dialog

`func fileDialogBrowserOptions(FileDialogBrowserOptions) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to
provide a refined URL search experience: include or exclude hidden files,
allow searching by tag, etc.

`func fileDialogConfirmationLabel<S>(S) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom confirmation button label.

`func fileDialogConfirmationLabel(Text?) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with custom text as a confirmation button label.

`func fileDialogConfirmationLabel(LocalizedStringKey) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom confirmation button label.

`func fileDialogCustomizationID(String) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to
persist and restore the file dialog configuration.

`func fileDialogDefaultDirectory(URL?) -> some View`

Configures the `fileExporter`, `fileImporter`, or `fileMover` to open with the
specified default directory.

`func fileDialogImportsUnresolvedAliases(Bool) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover`
behavior when a user chooses an alias.

`func fileDialogMessage<S>(S) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom message that is presented to the user, similar to a title.

`func fileDialogMessage(LocalizedStringKey) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom message that is presented to the user, similar to a title.

`func fileDialogURLEnabled(Predicate<URL>) -> some View`

On macOS, configures the the `fileImporter` or `fileMover` to conditionally
disable presented URLs.

`struct FileDialogBrowserOptions`

The way that file dialogs present the file system.

Instance Method

# fileDialogMessage(_:)

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom message that is presented to the user, similar to a title.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func fileDialogMessage(_ messageKey: LocalizedStringKey) -> some View
    

##  Parameters

`messageKey`

    

The key to a localized string to display.

## See Also

### Configuring a file dialog

`func fileDialogBrowserOptions(FileDialogBrowserOptions) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to
provide a refined URL search experience: include or exclude hidden files,
allow searching by tag, etc.

`func fileDialogConfirmationLabel<S>(S) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom confirmation button label.

`func fileDialogConfirmationLabel(Text?) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with custom text as a confirmation button label.

`func fileDialogConfirmationLabel(LocalizedStringKey) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom confirmation button label.

`func fileDialogCustomizationID(String) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to
persist and restore the file dialog configuration.

`func fileDialogDefaultDirectory(URL?) -> some View`

Configures the `fileExporter`, `fileImporter`, or `fileMover` to open with the
specified default directory.

`func fileDialogImportsUnresolvedAliases(Bool) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover`
behavior when a user chooses an alias.

`func fileDialogMessage<S>(S) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom message that is presented to the user, similar to a title.

`func fileDialogMessage(Text?) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom text that is presented to the user, similar to a title.

`func fileDialogURLEnabled(Predicate<URL>) -> some View`

On macOS, configures the the `fileImporter` or `fileMover` to conditionally
disable presented URLs.

`struct FileDialogBrowserOptions`

The way that file dialogs present the file system.

Instance Method

# fileDialogURLEnabled(_:)

On macOS, configures the the `fileImporter` or `fileMover` to conditionally
disable presented URLs.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func fileDialogURLEnabled(_ predicate: Predicate<URL>) -> some View
    

##  Parameters

`predicate`

    

The predicate that evaluates the URLs presented to the user to conditionally
disable them. The implementation is expected to have constant complexity and
should not access the files contents or metadata. A common use case is
inspecting the path or the file name.

## See Also

### Configuring a file dialog

`func fileDialogBrowserOptions(FileDialogBrowserOptions) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to
provide a refined URL search experience: include or exclude hidden files,
allow searching by tag, etc.

`func fileDialogConfirmationLabel<S>(S) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom confirmation button label.

`func fileDialogConfirmationLabel(Text?) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with custom text as a confirmation button label.

`func fileDialogConfirmationLabel(LocalizedStringKey) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom confirmation button label.

`func fileDialogCustomizationID(String) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to
persist and restore the file dialog configuration.

`func fileDialogDefaultDirectory(URL?) -> some View`

Configures the `fileExporter`, `fileImporter`, or `fileMover` to open with the
specified default directory.

`func fileDialogImportsUnresolvedAliases(Bool) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover`
behavior when a user chooses an alias.

`func fileDialogMessage<S>(S) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom message that is presented to the user, similar to a title.

`func fileDialogMessage(Text?) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom text that is presented to the user, similar to a title.

`func fileDialogMessage(LocalizedStringKey) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom message that is presented to the user, similar to a title.

`struct FileDialogBrowserOptions`

The way that file dialogs present the file system.

Instance Method

# inspector(isPresented:content:)

Inserts an inspector at the applied position in the view hierarchy.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+

    
    
    func inspector<V>(
        isPresented: Binding<Bool>,
        @ViewBuilder content: () -> V
    ) -> some View where V : View
    

##  Parameters

`isPresented`

    

A binding to `Bool` controlling the presented state.

`content`

    

The inspector content.

## Discussion

Apply this modifier to declare an inspector with a context-dependent
presentation. For example, an inspector can present as a trailing column in a
horizontally regular size class, but adapt to a sheet in a horizontally
compact size class.

Note

Trailing column inspectors have their presentation state restored by the
framework.

See Also

`InspectorCommands` for including the default inspector commands and keyboard
shortcuts.

## See Also

### Presenting an inspector

`func inspectorColumnWidth(CGFloat) -> some View`

Sets a fixed, preferred width for the inspector containing this view when
presented as a trailing column.

`func inspectorColumnWidth(min: CGFloat?, ideal: CGFloat, max: CGFloat?) ->
some View`

Sets a flexible, preferred width for the inspector in a trailing-column
presentation.

Instance Method

# inspectorColumnWidth(_:)

Sets a fixed, preferred width for the inspector containing this view when
presented as a trailing column.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+

    
    
    func inspectorColumnWidth(_ width: CGFloat) -> some View
    

##  Parameters

`width`

    

The preferred fixed width for the inspector if presented as a trailing column.

## Discussion

Apply this modifier on the content of a `inspector(isPresented:content:)` to
specify a fixed preferred width for the trailing column. Use
`inspectorColumnWidth(min:ideal:max:)` if you need to specify a flexible
width.

The following example shows an editor interface with an inspector, which when
presented as a trailing-column, has a fixed width of 225 points. The example
also uses `interactiveDismissDisabled(_:)` to prevent the inspector from being
collapsed by user action like dragging a divider.

Note

A fixed width does not prevent the user collapsing the inspector on macOS. See
`interactiveDismissDisabled(_:)`.

## See Also

### Presenting an inspector

`func inspector<V>(isPresented: Binding<Bool>, content: () -> V) -> some View`

Inserts an inspector at the applied position in the view hierarchy.

`func inspectorColumnWidth(min: CGFloat?, ideal: CGFloat, max: CGFloat?) ->
some View`

Sets a flexible, preferred width for the inspector in a trailing-column
presentation.

Instance Method

# inspectorColumnWidth(min:ideal:max:)

Sets a flexible, preferred width for the inspector in a trailing-column
presentation.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+

    
    
    func inspectorColumnWidth(
        min: CGFloat? = nil,
        ideal: CGFloat,
        max: CGFloat? = nil
    ) -> some View
    

##  Parameters

`min`

    

The minimum allowed width for the trailing column inspector

`ideal`

    

The initial width of the inspector in the absence of state restoration.
`ideal` influences the resulting width on macOS when a user double-clicks the
divider on the leading edge of the inspector. clicks a divider to readjust

`max`

    

The maximum allowed width for the trailing column inspector

## Discussion

Apply this modifier on the content of a `inspector(isPresented:content:)` to
specify a preferred flexible width for the column. Use
`inspectorColumnWidth(_:)` if you need to specify a fixed width.

The following example shows an editor interface with an inspector, which when
presented as a trailing-column, has a preferred width of 225 points, maximum
of 400, and a minimum of 150 at which point it will collapse, if allowed.

Only some platforms enable flexible inspector columns. If you specify a width
that the current presentation environment doesn’t support, SwiftUI may use a
different width for your column.

## See Also

### Presenting an inspector

`func inspector<V>(isPresented: Binding<Bool>, content: () -> V) -> some View`

Inserts an inspector at the applied position in the view hierarchy.

`func inspectorColumnWidth(CGFloat) -> some View`

Sets a fixed, preferred width for the inspector containing this view when
presented as a trailing column.

Instance Method

# quickLookPreview(_:)

Presents a Quick Look preview of the contents of a single URL.

QuickLook  SwiftUI  iOS 14.0+  iPadOS 14.0+  macOS 11.0+

    
    
    func quickLookPreview(_ item: Binding<URL?>) -> some View
    

##  Parameters

`item`

    

A `Binding` to a URL that should be previewed.

## Return Value

A view that presents the preview of the contents of the URL.

## Discussion

The Quick Look preview appears when you set the binding to a non-`nil` item.
When you set the item back to `nil`, Quick Look dismisses the preview.

Upon dismissal by the user, Quick Look automatically sets the item binding to
`nil`. Quick Look displays the preview when a non-`nil` item is set. Set
`item` to `nil` to dismiss the preview.

## See Also

### Previewing content

`func quickLookPreview<Items>(Binding<Items.Element?>, in: Items) -> some
View`

Presents a Quick Look preview of the URLs you provide.

Instance Method

# quickLookPreview(_:in:)

Presents a Quick Look preview of the URLs you provide.

QuickLook  SwiftUI  iOS 14.0+  iPadOS 14.0+  macOS 11.0+

    
    
    func quickLookPreview<Items>(
        _ selection: Binding<Items.Element?>,
        in items: Items
    ) -> some View where Items : RandomAccessCollection, Items.Element == URL
    

##  Parameters

`selection`

    

A `Binding` to an element that’s part of the items collection. This is the URL
that you currently want to preview.

`items`

    

A collection of URLs to preview.

## Return Value

A view that presents the preview of the contents of the URL.

## Discussion

The Quick Look preview appears when you set the binding to a non-`nil` item.
When you set the item back to `nil`, Quick Look dismisses the preview. If the
value of the selection binding isn’t contained in the items collection, Quick
Look treats it the same as a `nil` selection.

Quick Look updates the value of the selection binding to match the URL of the
file the user is previewing. Upon dismissal by the user, Quick Look
automatically sets the item binding to `nil`.

## See Also

### Previewing content

`func quickLookPreview(Binding<URL?>) -> some View`

Presents a Quick Look preview of the contents of a single URL.

Instance Method

# familyActivityPicker(isPresented:selection:)

Presents an activity picker view as a sheet.

iOS 15.0+  iPadOS 15.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    func familyActivityPicker(
        isPresented: Binding<Bool>,
        selection: Binding<FamilyActivitySelection>
    ) -> some View
    

##  Parameters

`isPresented`

    

A binding that indicates whether the app presents the picker view.

`selection`

    

A binding that manages the user-selected categories, apps, and web domains.

## Discussion

Use this view modifier to present a `FamilyControls/FamilyActivityPicker`.

## See Also

### Configuring Family Sharing

`struct FamilyActivityPicker`

A view in which users specify applications, web domains, and categories
without revealing their choices to the app.

`func familyActivityPicker(headerText: String?, footerText: String?,
isPresented: Binding<Bool>, selection: Binding<FamilyActivitySelection>) ->
some View`

Presents an activity picker view as a sheet.

Instance Method

# familyActivityPicker(headerText:footerText:isPresented:selection:)

Presents an activity picker view as a sheet.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    func familyActivityPicker(
        headerText: String? = nil,
        footerText: String? = nil,
        isPresented: Binding<Bool>,
        selection: Binding<FamilyActivitySelection>
    ) -> some View
    

##  Parameters

`headerText`

    

An optional string that provides text for the header of the picker view.

`footerText`

    

An optional string that provides text for the footer of the picker view.

`isPresented`

    

A binding that indicates whether the app presents the picker view.

`selection`

    

A binding that manages the user-selected categories, apps, and web domains.

## Discussion

Use this view modifier to present a `FamilyControls/FamilyActivityPicker`.

## See Also

### Configuring Family Sharing

`struct FamilyActivityPicker`

A view in which users specify applications, web domains, and categories
without revealing their choices to the app.

`func familyActivityPicker(isPresented: Binding<Bool>, selection:
Binding<FamilyActivitySelection>) -> some View`

Presents an activity picker view as a sheet.

Instance Method

# activitySystemActionForegroundColor(_:)

The text color for the auxiliary action button that the system shows next to a
Live Activity on the Lock Screen.

iOS 16.1+  iPadOS 16.1+  Mac Catalyst 16.1+  visionOS 1.0+

    
    
    func activitySystemActionForegroundColor(_ color: Color?) -> some View
    

##  Parameters

`color`

    

The text color to use. Pass `nil` to use the system’s default color.

## See Also

### Configuring a Live Activity

`func activityBackgroundTint(Color?) -> some View`

Sets the tint color for the background of a Live Activity that appears on the
Lock Screen.

`var isActivityFullscreen: Bool`

A Boolean value that indicates whether the Live Activity appears in a full-
screen presentation.

Instance Method

# activityBackgroundTint(_:)

Sets the tint color for the background of a Live Activity that appears on the
Lock Screen.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    func activityBackgroundTint(_ color: Color?) -> some View
    

##  Parameters

`color`

    

The background tint color to apply. To use the system’s default background
material, pass `nil`.

## Discussion

When you set a custom background tint color, consider setting a custom text
color for the auxiliary button people use to end a Live Activity on the Lock
Screen. To set a custom text color, use the
`activitySystemActionForegroundColor(_:)` view modifier.

## See Also

### Configuring a Live Activity

`func activitySystemActionForegroundColor(Color?) -> some View`

The text color for the auxiliary action button that the system shows next to a
Live Activity on the Lock Screen.

`var isActivityFullscreen: Bool`

A Boolean value that indicates whether the Live Activity appears in a full-
screen presentation.

Instance Method

# musicSubscriptionOffer(isPresented:options:onLoadCompletion:)

Initiates the process of presenting a sheet with subscription offers for Apple
Music when the `isPresented` binding is `true`.

MusicKit  SwiftUI  iOS 15.0+  iPadOS 15.0+  macOS 12.0+

    
    
    func musicSubscriptionOffer(
        isPresented: Binding<Bool>,
        options: MusicSubscriptionOffer.Options = .default,
        onLoadCompletion: @escaping ((any Error)?) -> Void = { _ in }
    ) -> some View
    

##  Parameters

`isPresented`

    

A binding to a Boolean value that you can set to `true` to show a sheet with
subscription offers for Apple Music.

`options`

    

Options to use for loading the subscription offer for Apple Music.

`onLoadCompletion`

    

The function to call upon completing the initial loading process for this
subscription offer. The subscription offer UI becomes visible when it calls
this function with the error argument as `nil`. If there is an error in the
loading process, the subscription offer calls this function with a non-`nil`
error, and it resets the `isPresented` binding to `false`.

## Discussion

The example below displays a simple button that the user can activate to begin
presenting subscription offers for Apple Music. The action handler of this
button initiates the presentation of those offers by setting the
`isShowingOffer` variable to `true`.

You can also configure the Apple Music subscription offer by creating an
instance of `MusicSubscriptionOffer.Options`, setting relevant properties on
it, and passing it to `.musicSubscriptionOffer(…)`. For example, to present
contextual offers that highlight a specific album, you can configure the
subscription offer like the following:

The initial value of `offerOptions` includes relevant tokens (affiliate and
campaign tokens) that allow you to receive compensation for referring new
Apple Music subscribers. For more information, see this presentation of the
Apple Services Performance Partners Program.

You may also set `isShowingOffer` to `false` to programmatically dismiss the
subscription offer (or to abort its loading process).

## See Also

### Interacting with the App Store and Apple Music

`func appStoreOverlay(isPresented: Binding<Bool>, configuration: () ->
SKOverlay.Configuration) -> some View`

Presents a StoreKit overlay when a given condition is true.

`func manageSubscriptionsSheet(isPresented: Binding<Bool>) -> some View`

`func refundRequestSheet(for: Transaction.ID, isPresented: Binding<Bool>,
onDismiss: ((Result<Transaction.RefundRequestStatus,
Transaction.RefundRequestError>) -> ())?) -> some View`

Display the refund request sheet for the given transaction.

`func offerCodeRedemption(isPresented: Binding<Bool>, onCompletion:
(Result<Void, any Error>) -> Void) -> some View`

Presents a sheet that enables users to redeem subscription offer codes that
you configure in App Store Connect.

`func currentEntitlementTask(for: String, priority: TaskPriority, action:
(EntitlementTaskState<VerificationResult<Transaction>?>) async -> ()) -> some
View`

Declares the view as dependent on the entitlement of an in-app purchase
product for `productID` and returns a modified view.

`func inAppPurchaseOptions(((Product) async -> Set<Product.PurchaseOption>)?)
-> some View`

Add a function to call before initiating a purchase from an in-app store
within view, providing a set of options for the purchase.

`func manageSubscriptionsSheet(isPresented: Binding<Bool>,
subscriptionGroupID: String) -> some View`

`func onInAppPurchaseCompletion(perform: ((Product,
Result<Product.PurchaseResult, any Error>) async -> ())?) -> some View`

Add an action to perform when a purchase initiated from an in-app store within
this view completes.

`func onInAppPurchaseStart(perform: ((Product) async -> ())?) -> some View`

Add an action to perform when a user triggers the purchase button on an in-app
store within this view.

`func productIconBorder() -> some View`

Adds a standard border to an icon used by an `ProductView` .

`func productViewStyle(some ProductViewStyle) -> some View`

Sets the style for in-app store products within a view.

`func productDescription(Visibility) -> some View`

`func storeButton(Visibility, for: StoreButtonKind...) -> some View`

Specifies the visibility of certain kinds of auxiliary buttons used by
`StoreView` or `SubscriptionStoreView` instances within the view.

`func storeProductTask(for: Product.ID, priority: TaskPriority, action:
(Product.TaskState) async -> ()) -> some View`

Declares the view as dependent on the in-app purchase product for `id` and
returns a modified view.

`func storeProductsTask(for: some Collection<String> & Equatable & Sendable,
priority: TaskPriority, action: (Product.CollectionTaskState) async -> ()) ->
some View`

Declares the view as dependent on a collection of in-app purchase products and
returns a modified view.

`func subscriptionStatusTask(for: String, priority: TaskPriority, action:
(EntitlementTaskState<[Product.SubscriptionInfo.Status]>) async -> ()) -> some
View`

Declares the view as dependent on the status of an auto-renewable subscription
group for `groupID` and returns a modified view.

`func subscriptionStoreButtonLabel(SubscriptionStoreButtonLabel) -> some View`

Configures in-app subscription store instances within a view to use a certain
button label.

`func subscriptionStoreControlIcon(icon: (Product, Product.SubscriptionInfo)
-> some View) -> some View`

Set a view to use to decorate individual subscription options within a
`SubscriptionStoreView`.

`func subscriptionStoreControlStyle(some SubscriptionStoreControlStyle) ->
some View`

Sets the control style for in-app subscription stores within a view.

`func subscriptionStorePickerItemBackground(some ShapeStyle) -> some View`

Sets the background style for picker items of `SubscriptionStoreView`
instances within this view.

`func subscriptionStorePolicyDestination(for: SubscriptionStorePolicyKind,
destination: () -> some View) -> some View`

Configures a view as the destination when someone chooses to view the
corresponding policy in a `SubscriptionStoreView` within this view.

`func subscriptionStorePolicyDestination(url: URL, for:
SubscriptionStorePolicyKind) -> some View`

Configures a URL as the destination when someone chooses to view the
corresponding policy in a `SubscriptionStoreView` within this view.

`func subscriptionStorePolicyForegroundStyle(some ShapeStyle) -> some View`

Sets the style for terms of service or privacy policy buttons created by
`SubscriptionStoreView` within a view.

`func subscriptionStorePolicyForegroundStyle(some ShapeStyle, some ShapeStyle)
-> some View`

Sets the style for terms of service and privacy policy buttons created by
`SubscriptionStoreView` within a view.

`func subscriptionStoreSignInAction((() -> ())?) -> some View`

Add an action to perform when someone triggers the sign in button on a
`SubscriptionStoreView` within this view.

`func subscriptionStoreControlBackground(SubscriptionStoreControlBackground)
-> some View`

Set the control background style for `SubscriptionStoreView` instances within
the view.

`func subscriptionStoreControlBackground(some ShapeStyle) -> some View`

Set the control background style for `SubscriptionStoreView` instances within
the view.

`func subscriptionPromotionalOffer(offer: (Product, Product.SubscriptionInfo)
-> Product.SubscriptionOffer?, signature: (Product, Product.SubscriptionInfo,
Product.SubscriptionOffer) async throws ->
Product.SubscriptionOffer.Signature) -> some View`

Select a promotional offer to apply to a purchase made from a subscription
store view.

Instance Method

# appStoreOverlay(isPresented:configuration:)

Presents a StoreKit overlay when a given condition is true.

StoreKit  SwiftUI  iOS 14.0+  iPadOS 14.0+  visionOS 1.0+

    
    
    func appStoreOverlay(
        isPresented: Binding<Bool>,
        configuration: @escaping () -> SKOverlay.Configuration
    ) -> some View
    

##  Parameters

`isPresented`

    

A Binding to a boolean value indicating whether the overlay should be
presented.

`configuration`

    

A closure providing the configuration of the overlay.

## Discussion

You use `appStoreOverlay` to display an overlay that recommends another app.
The overlay enables users to instantly view the other app’s page on the App
Store.

When `isPresented` is true, the system will run `configuration` to determine
how to configure the overlay. The overlay will automatically be presented over
the current scene.

See Also

SKOverlay.Configuration.

## See Also

### Interacting with the App Store and Apple Music

`func manageSubscriptionsSheet(isPresented: Binding<Bool>) -> some View`

`func refundRequestSheet(for: Transaction.ID, isPresented: Binding<Bool>,
onDismiss: ((Result<Transaction.RefundRequestStatus,
Transaction.RefundRequestError>) -> ())?) -> some View`

Display the refund request sheet for the given transaction.

`func offerCodeRedemption(isPresented: Binding<Bool>, onCompletion:
(Result<Void, any Error>) -> Void) -> some View`

Presents a sheet that enables users to redeem subscription offer codes that
you configure in App Store Connect.

`func musicSubscriptionOffer(isPresented: Binding<Bool>, options:
MusicSubscriptionOffer.Options, onLoadCompletion: ((any Error)?) -> Void) ->
some View`

Initiates the process of presenting a sheet with subscription offers for Apple
Music when the `isPresented` binding is `true`.

`func currentEntitlementTask(for: String, priority: TaskPriority, action:
(EntitlementTaskState<VerificationResult<Transaction>?>) async -> ()) -> some
View`

Declares the view as dependent on the entitlement of an in-app purchase
product for `productID` and returns a modified view.

`func inAppPurchaseOptions(((Product) async -> Set<Product.PurchaseOption>)?)
-> some View`

Add a function to call before initiating a purchase from an in-app store
within view, providing a set of options for the purchase.

`func manageSubscriptionsSheet(isPresented: Binding<Bool>,
subscriptionGroupID: String) -> some View`

`func onInAppPurchaseCompletion(perform: ((Product,
Result<Product.PurchaseResult, any Error>) async -> ())?) -> some View`

Add an action to perform when a purchase initiated from an in-app store within
this view completes.

`func onInAppPurchaseStart(perform: ((Product) async -> ())?) -> some View`

Add an action to perform when a user triggers the purchase button on an in-app
store within this view.

`func productIconBorder() -> some View`

Adds a standard border to an icon used by an `ProductView` .

`func productViewStyle(some ProductViewStyle) -> some View`

Sets the style for in-app store products within a view.

`func productDescription(Visibility) -> some View`

`func storeButton(Visibility, for: StoreButtonKind...) -> some View`

Specifies the visibility of certain kinds of auxiliary buttons used by
`StoreView` or `SubscriptionStoreView` instances within the view.

`func storeProductTask(for: Product.ID, priority: TaskPriority, action:
(Product.TaskState) async -> ()) -> some View`

Declares the view as dependent on the in-app purchase product for `id` and
returns a modified view.

`func storeProductsTask(for: some Collection<String> & Equatable & Sendable,
priority: TaskPriority, action: (Product.CollectionTaskState) async -> ()) ->
some View`

Declares the view as dependent on a collection of in-app purchase products and
returns a modified view.

`func subscriptionStatusTask(for: String, priority: TaskPriority, action:
(EntitlementTaskState<[Product.SubscriptionInfo.Status]>) async -> ()) -> some
View`

Declares the view as dependent on the status of an auto-renewable subscription
group for `groupID` and returns a modified view.

`func subscriptionStoreButtonLabel(SubscriptionStoreButtonLabel) -> some View`

Configures in-app subscription store instances within a view to use a certain
button label.

`func subscriptionStoreControlIcon(icon: (Product, Product.SubscriptionInfo)
-> some View) -> some View`

Set a view to use to decorate individual subscription options within a
`SubscriptionStoreView`.

`func subscriptionStoreControlStyle(some SubscriptionStoreControlStyle) ->
some View`

Sets the control style for in-app subscription stores within a view.

`func subscriptionStorePickerItemBackground(some ShapeStyle) -> some View`

Sets the background style for picker items of `SubscriptionStoreView`
instances within this view.

`func subscriptionStorePolicyDestination(for: SubscriptionStorePolicyKind,
destination: () -> some View) -> some View`

Configures a view as the destination when someone chooses to view the
corresponding policy in a `SubscriptionStoreView` within this view.

`func subscriptionStorePolicyDestination(url: URL, for:
SubscriptionStorePolicyKind) -> some View`

Configures a URL as the destination when someone chooses to view the
corresponding policy in a `SubscriptionStoreView` within this view.

`func subscriptionStorePolicyForegroundStyle(some ShapeStyle) -> some View`

Sets the style for terms of service or privacy policy buttons created by
`SubscriptionStoreView` within a view.

`func subscriptionStorePolicyForegroundStyle(some ShapeStyle, some ShapeStyle)
-> some View`

Sets the style for terms of service and privacy policy buttons created by
`SubscriptionStoreView` within a view.

`func subscriptionStoreSignInAction((() -> ())?) -> some View`

Add an action to perform when someone triggers the sign in button on a
`SubscriptionStoreView` within this view.

`func subscriptionStoreControlBackground(SubscriptionStoreControlBackground)
-> some View`

Set the control background style for `SubscriptionStoreView` instances within
the view.

`func subscriptionStoreControlBackground(some ShapeStyle) -> some View`

Set the control background style for `SubscriptionStoreView` instances within
the view.

`func subscriptionPromotionalOffer(offer: (Product, Product.SubscriptionInfo)
-> Product.SubscriptionOffer?, signature: (Product, Product.SubscriptionInfo,
Product.SubscriptionOffer) async throws ->
Product.SubscriptionOffer.Signature) -> some View`

Select a promotional offer to apply to a purchase made from a subscription
store view.

Instance Method

# manageSubscriptionsSheet(isPresented:)

StoreKit  SwiftUI  iOS 15.0+  iPadOS 15.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    func manageSubscriptionsSheet(isPresented: Binding<Bool>) -> some View
    

## See Also

### Interacting with the App Store and Apple Music

`func appStoreOverlay(isPresented: Binding<Bool>, configuration: () ->
SKOverlay.Configuration) -> some View`

Presents a StoreKit overlay when a given condition is true.

`func refundRequestSheet(for: Transaction.ID, isPresented: Binding<Bool>,
onDismiss: ((Result<Transaction.RefundRequestStatus,
Transaction.RefundRequestError>) -> ())?) -> some View`

Display the refund request sheet for the given transaction.

`func offerCodeRedemption(isPresented: Binding<Bool>, onCompletion:
(Result<Void, any Error>) -> Void) -> some View`

Presents a sheet that enables users to redeem subscription offer codes that
you configure in App Store Connect.

`func musicSubscriptionOffer(isPresented: Binding<Bool>, options:
MusicSubscriptionOffer.Options, onLoadCompletion: ((any Error)?) -> Void) ->
some View`

Initiates the process of presenting a sheet with subscription offers for Apple
Music when the `isPresented` binding is `true`.

`func currentEntitlementTask(for: String, priority: TaskPriority, action:
(EntitlementTaskState<VerificationResult<Transaction>?>) async -> ()) -> some
View`

Declares the view as dependent on the entitlement of an in-app purchase
product for `productID` and returns a modified view.

`func inAppPurchaseOptions(((Product) async -> Set<Product.PurchaseOption>)?)
-> some View`

Add a function to call before initiating a purchase from an in-app store
within view, providing a set of options for the purchase.

`func manageSubscriptionsSheet(isPresented: Binding<Bool>,
subscriptionGroupID: String) -> some View`

`func onInAppPurchaseCompletion(perform: ((Product,
Result<Product.PurchaseResult, any Error>) async -> ())?) -> some View`

Add an action to perform when a purchase initiated from an in-app store within
this view completes.

`func onInAppPurchaseStart(perform: ((Product) async -> ())?) -> some View`

Add an action to perform when a user triggers the purchase button on an in-app
store within this view.

`func productIconBorder() -> some View`

Adds a standard border to an icon used by an `ProductView` .

`func productViewStyle(some ProductViewStyle) -> some View`

Sets the style for in-app store products within a view.

`func productDescription(Visibility) -> some View`

`func storeButton(Visibility, for: StoreButtonKind...) -> some View`

Specifies the visibility of certain kinds of auxiliary buttons used by
`StoreView` or `SubscriptionStoreView` instances within the view.

`func storeProductTask(for: Product.ID, priority: TaskPriority, action:
(Product.TaskState) async -> ()) -> some View`

Declares the view as dependent on the in-app purchase product for `id` and
returns a modified view.

`func storeProductsTask(for: some Collection<String> & Equatable & Sendable,
priority: TaskPriority, action: (Product.CollectionTaskState) async -> ()) ->
some View`

Declares the view as dependent on a collection of in-app purchase products and
returns a modified view.

`func subscriptionStatusTask(for: String, priority: TaskPriority, action:
(EntitlementTaskState<[Product.SubscriptionInfo.Status]>) async -> ()) -> some
View`

Declares the view as dependent on the status of an auto-renewable subscription
group for `groupID` and returns a modified view.

`func subscriptionStoreButtonLabel(SubscriptionStoreButtonLabel) -> some View`

Configures in-app subscription store instances within a view to use a certain
button label.

`func subscriptionStoreControlIcon(icon: (Product, Product.SubscriptionInfo)
-> some View) -> some View`

Set a view to use to decorate individual subscription options within a
`SubscriptionStoreView`.

`func subscriptionStoreControlStyle(some SubscriptionStoreControlStyle) ->
some View`

Sets the control style for in-app subscription stores within a view.

`func subscriptionStorePickerItemBackground(some ShapeStyle) -> some View`

Sets the background style for picker items of `SubscriptionStoreView`
instances within this view.

`func subscriptionStorePolicyDestination(for: SubscriptionStorePolicyKind,
destination: () -> some View) -> some View`

Configures a view as the destination when someone chooses to view the
corresponding policy in a `SubscriptionStoreView` within this view.

`func subscriptionStorePolicyDestination(url: URL, for:
SubscriptionStorePolicyKind) -> some View`

Configures a URL as the destination when someone chooses to view the
corresponding policy in a `SubscriptionStoreView` within this view.

`func subscriptionStorePolicyForegroundStyle(some ShapeStyle) -> some View`

Sets the style for terms of service or privacy policy buttons created by
`SubscriptionStoreView` within a view.

`func subscriptionStorePolicyForegroundStyle(some ShapeStyle, some ShapeStyle)
-> some View`

Sets the style for terms of service and privacy policy buttons created by
`SubscriptionStoreView` within a view.

`func subscriptionStoreSignInAction((() -> ())?) -> some View`

Add an action to perform when someone triggers the sign in button on a
`SubscriptionStoreView` within this view.

`func subscriptionStoreControlBackground(SubscriptionStoreControlBackground)
-> some View`

Set the control background style for `SubscriptionStoreView` instances within
the view.

`func subscriptionStoreControlBackground(some ShapeStyle) -> some View`

Set the control background style for `SubscriptionStoreView` instances within
the view.

`func subscriptionPromotionalOffer(offer: (Product, Product.SubscriptionInfo)
-> Product.SubscriptionOffer?, signature: (Product, Product.SubscriptionInfo,
Product.SubscriptionOffer) async throws ->
Product.SubscriptionOffer.Signature) -> some View`

Select a promotional offer to apply to a purchase made from a subscription
store view.

Instance Method

# refundRequestSheet(for:isPresented:onDismiss:)

Display the refund request sheet for the given transaction.

StoreKit  SwiftUI  iOS 15.0+  iPadOS 15.0+  macOS 14.0+  Mac Catalyst 15.0+
visionOS 1.0+

    
    
    @preconcurrency
    func refundRequestSheet(
        for transactionID: Transaction.ID,
        isPresented: Binding<Bool>,
        onDismiss: (@MainActor (Result<Transaction.RefundRequestStatus, Transaction.RefundRequestError>) -> ())? = nil
    ) -> some View
    

##  Parameters

`transactionID`

    

The transaction ID to request a refund for.

`isPresented`

    

A binding to a Boolean value that determines whether the refund request sheet
is presented.

`onDismiss`

    

The closure to execute when dismissing the sheet, with the result of the
refund request provided as a parameter.

## See Also

### Interacting with the App Store and Apple Music

`func appStoreOverlay(isPresented: Binding<Bool>, configuration: () ->
SKOverlay.Configuration) -> some View`

Presents a StoreKit overlay when a given condition is true.

`func manageSubscriptionsSheet(isPresented: Binding<Bool>) -> some View`

`func offerCodeRedemption(isPresented: Binding<Bool>, onCompletion:
(Result<Void, any Error>) -> Void) -> some View`

Presents a sheet that enables users to redeem subscription offer codes that
you configure in App Store Connect.

`func musicSubscriptionOffer(isPresented: Binding<Bool>, options:
MusicSubscriptionOffer.Options, onLoadCompletion: ((any Error)?) -> Void) ->
some View`

Initiates the process of presenting a sheet with subscription offers for Apple
Music when the `isPresented` binding is `true`.

`func currentEntitlementTask(for: String, priority: TaskPriority, action:
(EntitlementTaskState<VerificationResult<Transaction>?>) async -> ()) -> some
View`

Declares the view as dependent on the entitlement of an in-app purchase
product for `productID` and returns a modified view.

`func inAppPurchaseOptions(((Product) async -> Set<Product.PurchaseOption>)?)
-> some View`

Add a function to call before initiating a purchase from an in-app store
within view, providing a set of options for the purchase.

`func manageSubscriptionsSheet(isPresented: Binding<Bool>,
subscriptionGroupID: String) -> some View`

`func onInAppPurchaseCompletion(perform: ((Product,
Result<Product.PurchaseResult, any Error>) async -> ())?) -> some View`

Add an action to perform when a purchase initiated from an in-app store within
this view completes.

`func onInAppPurchaseStart(perform: ((Product) async -> ())?) -> some View`

Add an action to perform when a user triggers the purchase button on an in-app
store within this view.

`func productIconBorder() -> some View`

Adds a standard border to an icon used by an `ProductView` .

`func productViewStyle(some ProductViewStyle) -> some View`

Sets the style for in-app store products within a view.

`func productDescription(Visibility) -> some View`

`func storeButton(Visibility, for: StoreButtonKind...) -> some View`

Specifies the visibility of certain kinds of auxiliary buttons used by
`StoreView` or `SubscriptionStoreView` instances within the view.

`func storeProductTask(for: Product.ID, priority: TaskPriority, action:
(Product.TaskState) async -> ()) -> some View`

Declares the view as dependent on the in-app purchase product for `id` and
returns a modified view.

`func storeProductsTask(for: some Collection<String> & Equatable & Sendable,
priority: TaskPriority, action: (Product.CollectionTaskState) async -> ()) ->
some View`

Declares the view as dependent on a collection of in-app purchase products and
returns a modified view.

`func subscriptionStatusTask(for: String, priority: TaskPriority, action:
(EntitlementTaskState<[Product.SubscriptionInfo.Status]>) async -> ()) -> some
View`

Declares the view as dependent on the status of an auto-renewable subscription
group for `groupID` and returns a modified view.

`func subscriptionStoreButtonLabel(SubscriptionStoreButtonLabel) -> some View`

Configures in-app subscription store instances within a view to use a certain
button label.

`func subscriptionStoreControlIcon(icon: (Product, Product.SubscriptionInfo)
-> some View) -> some View`

Set a view to use to decorate individual subscription options within a
`SubscriptionStoreView`.

`func subscriptionStoreControlStyle(some SubscriptionStoreControlStyle) ->
some View`

Sets the control style for in-app subscription stores within a view.

`func subscriptionStorePickerItemBackground(some ShapeStyle) -> some View`

Sets the background style for picker items of `SubscriptionStoreView`
instances within this view.

`func subscriptionStorePolicyDestination(for: SubscriptionStorePolicyKind,
destination: () -> some View) -> some View`

Configures a view as the destination when someone chooses to view the
corresponding policy in a `SubscriptionStoreView` within this view.

`func subscriptionStorePolicyDestination(url: URL, for:
SubscriptionStorePolicyKind) -> some View`

Configures a URL as the destination when someone chooses to view the
corresponding policy in a `SubscriptionStoreView` within this view.

`func subscriptionStorePolicyForegroundStyle(some ShapeStyle) -> some View`

Sets the style for terms of service or privacy policy buttons created by
`SubscriptionStoreView` within a view.

`func subscriptionStorePolicyForegroundStyle(some ShapeStyle, some ShapeStyle)
-> some View`

Sets the style for terms of service and privacy policy buttons created by
`SubscriptionStoreView` within a view.

`func subscriptionStoreSignInAction((() -> ())?) -> some View`

Add an action to perform when someone triggers the sign in button on a
`SubscriptionStoreView` within this view.

`func subscriptionStoreControlBackground(SubscriptionStoreControlBackground)
-> some View`

Set the control background style for `SubscriptionStoreView` instances within
the view.

`func subscriptionStoreControlBackground(some ShapeStyle) -> some View`

Set the control background style for `SubscriptionStoreView` instances within
the view.

`func subscriptionPromotionalOffer(offer: (Product, Product.SubscriptionInfo)
-> Product.SubscriptionOffer?, signature: (Product, Product.SubscriptionInfo,
Product.SubscriptionOffer) async throws ->
Product.SubscriptionOffer.Signature) -> some View`

Select a promotional offer to apply to a purchase made from a subscription
store view.

Instance Method

# offerCodeRedemption(isPresented:onCompletion:)

Presents a sheet that enables users to redeem subscription offer codes that
you configure in App Store Connect.

StoreKit  SwiftUI  iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    func offerCodeRedemption(
        isPresented: Binding<Bool>,
        onCompletion: @escaping @MainActor (Result<Void, any Error>) -> Void = { _ in }
    ) -> some View
    

##  Parameters

`isPresented`

    

A Binding to a boolean value indicating whether the sheet should be presented.

`onCompletion`

    

A closure that returns the result of the presentation.

## Discussion

Important

The resulting transaction from redeeming an offer code is emitted in
`Transaction.updates`. Set up a transaction listener as soon as your app
launches to receive new transactions while the app is running.

## See Also

### Interacting with the App Store and Apple Music

`func appStoreOverlay(isPresented: Binding<Bool>, configuration: () ->
SKOverlay.Configuration) -> some View`

Presents a StoreKit overlay when a given condition is true.

`func manageSubscriptionsSheet(isPresented: Binding<Bool>) -> some View`

`func refundRequestSheet(for: Transaction.ID, isPresented: Binding<Bool>,
onDismiss: ((Result<Transaction.RefundRequestStatus,
Transaction.RefundRequestError>) -> ())?) -> some View`

Display the refund request sheet for the given transaction.

`func musicSubscriptionOffer(isPresented: Binding<Bool>, options:
MusicSubscriptionOffer.Options, onLoadCompletion: ((any Error)?) -> Void) ->
some View`

Initiates the process of presenting a sheet with subscription offers for Apple
Music when the `isPresented` binding is `true`.

`func currentEntitlementTask(for: String, priority: TaskPriority, action:
(EntitlementTaskState<VerificationResult<Transaction>?>) async -> ()) -> some
View`

Declares the view as dependent on the entitlement of an in-app purchase
product for `productID` and returns a modified view.

`func inAppPurchaseOptions(((Product) async -> Set<Product.PurchaseOption>)?)
-> some View`

Add a function to call before initiating a purchase from an in-app store
within view, providing a set of options for the purchase.

`func manageSubscriptionsSheet(isPresented: Binding<Bool>,
subscriptionGroupID: String) -> some View`

`func onInAppPurchaseCompletion(perform: ((Product,
Result<Product.PurchaseResult, any Error>) async -> ())?) -> some View`

Add an action to perform when a purchase initiated from an in-app store within
this view completes.

`func onInAppPurchaseStart(perform: ((Product) async -> ())?) -> some View`

Add an action to perform when a user triggers the purchase button on an in-app
store within this view.

`func productIconBorder() -> some View`

Adds a standard border to an icon used by an `ProductView` .

`func productViewStyle(some ProductViewStyle) -> some View`

Sets the style for in-app store products within a view.

`func productDescription(Visibility) -> some View`

`func storeButton(Visibility, for: StoreButtonKind...) -> some View`

Specifies the visibility of certain kinds of auxiliary buttons used by
`StoreView` or `SubscriptionStoreView` instances within the view.

`func storeProductTask(for: Product.ID, priority: TaskPriority, action:
(Product.TaskState) async -> ()) -> some View`

Declares the view as dependent on the in-app purchase product for `id` and
returns a modified view.

`func storeProductsTask(for: some Collection<String> & Equatable & Sendable,
priority: TaskPriority, action: (Product.CollectionTaskState) async -> ()) ->
some View`

Declares the view as dependent on a collection of in-app purchase products and
returns a modified view.

`func subscriptionStatusTask(for: String, priority: TaskPriority, action:
(EntitlementTaskState<[Product.SubscriptionInfo.Status]>) async -> ()) -> some
View`

Declares the view as dependent on the status of an auto-renewable subscription
group for `groupID` and returns a modified view.

`func subscriptionStoreButtonLabel(SubscriptionStoreButtonLabel) -> some View`

Configures in-app subscription store instances within a view to use a certain
button label.

`func subscriptionStoreControlIcon(icon: (Product, Product.SubscriptionInfo)
-> some View) -> some View`

Set a view to use to decorate individual subscription options within a
`SubscriptionStoreView`.

`func subscriptionStoreControlStyle(some SubscriptionStoreControlStyle) ->
some View`

Sets the control style for in-app subscription stores within a view.

`func subscriptionStorePickerItemBackground(some ShapeStyle) -> some View`

Sets the background style for picker items of `SubscriptionStoreView`
instances within this view.

`func subscriptionStorePolicyDestination(for: SubscriptionStorePolicyKind,
destination: () -> some View) -> some View`

Configures a view as the destination when someone chooses to view the
corresponding policy in a `SubscriptionStoreView` within this view.

`func subscriptionStorePolicyDestination(url: URL, for:
SubscriptionStorePolicyKind) -> some View`

Configures a URL as the destination when someone chooses to view the
corresponding policy in a `SubscriptionStoreView` within this view.

`func subscriptionStorePolicyForegroundStyle(some ShapeStyle) -> some View`

Sets the style for terms of service or privacy policy buttons created by
`SubscriptionStoreView` within a view.

`func subscriptionStorePolicyForegroundStyle(some ShapeStyle, some ShapeStyle)
-> some View`

Sets the style for terms of service and privacy policy buttons created by
`SubscriptionStoreView` within a view.

`func subscriptionStoreSignInAction((() -> ())?) -> some View`

Add an action to perform when someone triggers the sign in button on a
`SubscriptionStoreView` within this view.

`func subscriptionStoreControlBackground(SubscriptionStoreControlBackground)
-> some View`

Set the control background style for `SubscriptionStoreView` instances within
the view.

`func subscriptionStoreControlBackground(some ShapeStyle) -> some View`

Set the control background style for `SubscriptionStoreView` instances within
the view.

`func subscriptionPromotionalOffer(offer: (Product, Product.SubscriptionInfo)
-> Product.SubscriptionOffer?, signature: (Product, Product.SubscriptionInfo,
Product.SubscriptionOffer) async throws ->
Product.SubscriptionOffer.Signature) -> some View`

Select a promotional offer to apply to a purchase made from a subscription
store view.

Instance Method

# photosPicker(isPresented:selection:matching:preferredItemEncoding:)

Presents a Photos picker that selects a `PhotosPickerItem`.

PhotosUI  SwiftUI  iOS 16.0+  iPadOS 16.0+  macOS 13.0+  watchOS 9.0+

    
    
    func photosPicker(
        isPresented: Binding<Bool>,
        selection: Binding<PhotosPickerItem?>,
        matching filter: PHPickerFilter? = nil,
        preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy = .automatic
    ) -> some View
    

##  Parameters

`isPresented`

    

The binding to whether the Photos picker should be shown.

`selection`

    

The item being shown and selected in the Photos picker.

`filter`

    

Types of items that can be shown. Default is `nil`. Setting it to `nil` means
all supported types can be shown.

`preferredItemEncoding`

    

The encoding disambiguation policy of the selected item. Default is
`.automatic`. Setting it to `.automatic` means the best encoding determined by
the system will be used.

## Discussion

The user explicitly grants access only to items they choose, so photo library
access authorization is not needed.

## See Also

### Selecting photos

`struct PhotosPicker`

A view that displays a Photos picker for choosing assets from the photo
library.

`func photosPicker(isPresented: Binding<Bool>, selection:
Binding<PhotosPickerItem?>, matching: PHPickerFilter?, preferredItemEncoding:
PhotosPickerItem.EncodingDisambiguationPolicy, photoLibrary: PHPhotoLibrary)
-> some View`

Presents a Photos picker that selects a `PhotosPickerItem` from a given photo
library.

`func photosPicker(isPresented: Binding<Bool>, selection:
Binding<[PhotosPickerItem]>, maxSelectionCount: Int?, selectionBehavior:
PhotosPickerSelectionBehavior, matching: PHPickerFilter?,
preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy) -> some
View`

Presents a Photos picker that selects a collection of `PhotosPickerItem`.

`func photosPicker(isPresented: Binding<Bool>, selection:
Binding<[PhotosPickerItem]>, maxSelectionCount: Int?, selectionBehavior:
PhotosPickerSelectionBehavior, matching: PHPickerFilter?,
preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy,
photoLibrary: PHPhotoLibrary) -> some View`

Presents a Photos picker that selects a collection of `PhotosPickerItem` from
a given photo library.

`func photosPickerAccessoryVisibility(Visibility, edges: Edge.Set) -> some
View`

Sets the accessory visibility of the Photos picker. Accessories include
anything between the content and the edge, like the navigation bar or the
sidebar.

`func photosPickerDisabledCapabilities(PHPickerCapabilities) -> some View`

Disables capabilities of the Photos picker.

`func photosPickerStyle(PhotosPickerStyle) -> some View`

Sets the mode of the Photos picker.

Instance Method

#
photosPicker(isPresented:selection:matching:preferredItemEncoding:photoLibrary:)

Presents a Photos picker that selects a `PhotosPickerItem` from a given photo
library.

PhotosUI  SwiftUI  iOS 16.0+  iPadOS 16.0+  macOS 13.0+

    
    
    func photosPicker(
        isPresented: Binding<Bool>,
        selection: Binding<PhotosPickerItem?>,
        matching filter: PHPickerFilter? = nil,
        preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy = .automatic,
        photoLibrary: PHPhotoLibrary
    ) -> some View
    

##  Parameters

`isPresented`

    

The binding to whether the Photos picker should be shown.

`selection`

    

The item being shown and selected in the Photos picker.

`filter`

    

Types of items that can be shown. Default is `nil`. Setting it to `nil` means
all supported types can be shown.

`preferredItemEncoding`

    

The encoding disambiguation policy of the selected item. Default is
`.automatic`. Setting it to `.automatic` means the best encoding determined by
the system will be used.

`photoLibrary`

    

The photo library to choose from.

## Discussion

The user explicitly grants access only to items they choose, so photo library
access authorization is not needed.

## See Also

### Selecting photos

`struct PhotosPicker`

A view that displays a Photos picker for choosing assets from the photo
library.

`func photosPicker(isPresented: Binding<Bool>, selection:
Binding<PhotosPickerItem?>, matching: PHPickerFilter?, preferredItemEncoding:
PhotosPickerItem.EncodingDisambiguationPolicy) -> some View`

Presents a Photos picker that selects a `PhotosPickerItem`.

`func photosPicker(isPresented: Binding<Bool>, selection:
Binding<[PhotosPickerItem]>, maxSelectionCount: Int?, selectionBehavior:
PhotosPickerSelectionBehavior, matching: PHPickerFilter?,
preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy) -> some
View`

Presents a Photos picker that selects a collection of `PhotosPickerItem`.

`func photosPicker(isPresented: Binding<Bool>, selection:
Binding<[PhotosPickerItem]>, maxSelectionCount: Int?, selectionBehavior:
PhotosPickerSelectionBehavior, matching: PHPickerFilter?,
preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy,
photoLibrary: PHPhotoLibrary) -> some View`

Presents a Photos picker that selects a collection of `PhotosPickerItem` from
a given photo library.

`func photosPickerAccessoryVisibility(Visibility, edges: Edge.Set) -> some
View`

Sets the accessory visibility of the Photos picker. Accessories include
anything between the content and the edge, like the navigation bar or the
sidebar.

`func photosPickerDisabledCapabilities(PHPickerCapabilities) -> some View`

Disables capabilities of the Photos picker.

`func photosPickerStyle(PhotosPickerStyle) -> some View`

Sets the mode of the Photos picker.

Instance Method

#
photosPicker(isPresented:selection:maxSelectionCount:selectionBehavior:matching:preferredItemEncoding:)

Presents a Photos picker that selects a collection of `PhotosPickerItem`.

PhotosUI  SwiftUI  iOS 16.0+  iPadOS 16.0+  macOS 13.0+  watchOS 9.0+

    
    
    func photosPicker(
        isPresented: Binding<Bool>,
        selection: Binding<[PhotosPickerItem]>,
        maxSelectionCount: Int? = nil,
        selectionBehavior: PhotosPickerSelectionBehavior = .default,
        matching filter: PHPickerFilter? = nil,
        preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy = .automatic
    ) -> some View
    

##  Parameters

`isPresented`

    

The binding to whether the Photos picker should be shown.

`selection`

    

All items being shown and selected in the Photos picker.

`maxSelectionCount`

    

The maximum number of items that can be selected. Default is `nil`. Setting it
to `nil` means maximum supported by the system.

`selectionBehavior`

    

The selection behavior of the Photos picker. Default is `.default`.

`filter`

    

Types of items that can be shown. Default is `nil`. Setting it to `nil` means
all supported types can be shown.

`preferredItemEncoding`

    

The encoding disambiguation policy of selected items. Default is `.automatic`.
Setting it to `.automatic` means the best encoding determined by the system
will be used.

## Discussion

The user explicitly grants access only to items they choose, so photo library
access authorization is not needed.

## See Also

### Selecting photos

`struct PhotosPicker`

A view that displays a Photos picker for choosing assets from the photo
library.

`func photosPicker(isPresented: Binding<Bool>, selection:
Binding<PhotosPickerItem?>, matching: PHPickerFilter?, preferredItemEncoding:
PhotosPickerItem.EncodingDisambiguationPolicy) -> some View`

Presents a Photos picker that selects a `PhotosPickerItem`.

`func photosPicker(isPresented: Binding<Bool>, selection:
Binding<PhotosPickerItem?>, matching: PHPickerFilter?, preferredItemEncoding:
PhotosPickerItem.EncodingDisambiguationPolicy, photoLibrary: PHPhotoLibrary)
-> some View`

Presents a Photos picker that selects a `PhotosPickerItem` from a given photo
library.

`func photosPicker(isPresented: Binding<Bool>, selection:
Binding<[PhotosPickerItem]>, maxSelectionCount: Int?, selectionBehavior:
PhotosPickerSelectionBehavior, matching: PHPickerFilter?,
preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy,
photoLibrary: PHPhotoLibrary) -> some View`

Presents a Photos picker that selects a collection of `PhotosPickerItem` from
a given photo library.

`func photosPickerAccessoryVisibility(Visibility, edges: Edge.Set) -> some
View`

Sets the accessory visibility of the Photos picker. Accessories include
anything between the content and the edge, like the navigation bar or the
sidebar.

`func photosPickerDisabledCapabilities(PHPickerCapabilities) -> some View`

Disables capabilities of the Photos picker.

`func photosPickerStyle(PhotosPickerStyle) -> some View`

Sets the mode of the Photos picker.

Instance Method

#
photosPicker(isPresented:selection:maxSelectionCount:selectionBehavior:matching:preferredItemEncoding:photoLibrary:)

Presents a Photos picker that selects a collection of `PhotosPickerItem` from
a given photo library.

PhotosUI  SwiftUI  iOS 16.0+  iPadOS 16.0+  macOS 13.0+

    
    
    func photosPicker(
        isPresented: Binding<Bool>,
        selection: Binding<[PhotosPickerItem]>,
        maxSelectionCount: Int? = nil,
        selectionBehavior: PhotosPickerSelectionBehavior = .default,
        matching filter: PHPickerFilter? = nil,
        preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy = .automatic,
        photoLibrary: PHPhotoLibrary
    ) -> some View
    

##  Parameters

`isPresented`

    

The binding to whether the Photos picker should be shown.

`selection`

    

All items being shown and selected in the Photos picker.

`maxSelectionCount`

    

The maximum number of items that can be selected. Default is `nil`. Setting it
to `nil` means maximum supported by the system.

`selectionBehavior`

    

The selection behavior of the Photos picker. Default is `.default`.

`filter`

    

Types of items that can be shown. Default is `nil`. Setting it to `nil` means
all supported types can be shown.

`preferredItemEncoding`

    

The encoding disambiguation policy of selected items. Default is `.automatic`.
Setting it to `.automatic` means the best encoding determined by the system
will be used.

`photoLibrary`

    

The photo library to choose from.

## Discussion

The user explicitly grants access only to items they choose, so photo library
access authorization is not needed.

## See Also

### Selecting photos

`struct PhotosPicker`

A view that displays a Photos picker for choosing assets from the photo
library.

`func photosPicker(isPresented: Binding<Bool>, selection:
Binding<PhotosPickerItem?>, matching: PHPickerFilter?, preferredItemEncoding:
PhotosPickerItem.EncodingDisambiguationPolicy) -> some View`

Presents a Photos picker that selects a `PhotosPickerItem`.

`func photosPicker(isPresented: Binding<Bool>, selection:
Binding<PhotosPickerItem?>, matching: PHPickerFilter?, preferredItemEncoding:
PhotosPickerItem.EncodingDisambiguationPolicy, photoLibrary: PHPhotoLibrary)
-> some View`

Presents a Photos picker that selects a `PhotosPickerItem` from a given photo
library.

`func photosPicker(isPresented: Binding<Bool>, selection:
Binding<[PhotosPickerItem]>, maxSelectionCount: Int?, selectionBehavior:
PhotosPickerSelectionBehavior, matching: PHPickerFilter?,
preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy) -> some
View`

Presents a Photos picker that selects a collection of `PhotosPickerItem`.

`func photosPickerAccessoryVisibility(Visibility, edges: Edge.Set) -> some
View`

Sets the accessory visibility of the Photos picker. Accessories include
anything between the content and the edge, like the navigation bar or the
sidebar.

`func photosPickerDisabledCapabilities(PHPickerCapabilities) -> some View`

Disables capabilities of the Photos picker.

`func photosPickerStyle(PhotosPickerStyle) -> some View`

Sets the mode of the Photos picker.

Instance Method

# photosPickerAccessoryVisibility(_:edges:)

Sets the accessory visibility of the Photos picker. Accessories include
anything between the content and the edge, like the navigation bar or the
sidebar.

PhotosUI  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+

    
    
    func photosPickerAccessoryVisibility(
        _ visibility: Visibility,
        edges: Edge.Set = .all
    ) -> some View
    

##  Parameters

`edges`

    

The accessory visibility to apply.

`edges`

    

One or more of the available edges.

## Return Value

A Photos picker with the specified accessory visibility.

## See Also

### Selecting photos

`struct PhotosPicker`

A view that displays a Photos picker for choosing assets from the photo
library.

`func photosPicker(isPresented: Binding<Bool>, selection:
Binding<PhotosPickerItem?>, matching: PHPickerFilter?, preferredItemEncoding:
PhotosPickerItem.EncodingDisambiguationPolicy) -> some View`

Presents a Photos picker that selects a `PhotosPickerItem`.

`func photosPicker(isPresented: Binding<Bool>, selection:
Binding<PhotosPickerItem?>, matching: PHPickerFilter?, preferredItemEncoding:
PhotosPickerItem.EncodingDisambiguationPolicy, photoLibrary: PHPhotoLibrary)
-> some View`

Presents a Photos picker that selects a `PhotosPickerItem` from a given photo
library.

`func photosPicker(isPresented: Binding<Bool>, selection:
Binding<[PhotosPickerItem]>, maxSelectionCount: Int?, selectionBehavior:
PhotosPickerSelectionBehavior, matching: PHPickerFilter?,
preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy) -> some
View`

Presents a Photos picker that selects a collection of `PhotosPickerItem`.

`func photosPicker(isPresented: Binding<Bool>, selection:
Binding<[PhotosPickerItem]>, maxSelectionCount: Int?, selectionBehavior:
PhotosPickerSelectionBehavior, matching: PHPickerFilter?,
preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy,
photoLibrary: PHPhotoLibrary) -> some View`

Presents a Photos picker that selects a collection of `PhotosPickerItem` from
a given photo library.

`func photosPickerDisabledCapabilities(PHPickerCapabilities) -> some View`

Disables capabilities of the Photos picker.

`func photosPickerStyle(PhotosPickerStyle) -> some View`

Sets the mode of the Photos picker.

Instance Method

# photosPickerDisabledCapabilities(_:)

Disables capabilities of the Photos picker.

PhotosUI  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+

    
    
    func photosPickerDisabledCapabilities(_ disabledCapabilities: PHPickerCapabilities) -> some View
    

##  Parameters

`disabledCapabilities`

    

One or more of the available capabilities.

## Return Value

A Photos picker with specified capabilities that are disabled.

## See Also

### Selecting photos

`struct PhotosPicker`

A view that displays a Photos picker for choosing assets from the photo
library.

`func photosPicker(isPresented: Binding<Bool>, selection:
Binding<PhotosPickerItem?>, matching: PHPickerFilter?, preferredItemEncoding:
PhotosPickerItem.EncodingDisambiguationPolicy) -> some View`

Presents a Photos picker that selects a `PhotosPickerItem`.

`func photosPicker(isPresented: Binding<Bool>, selection:
Binding<PhotosPickerItem?>, matching: PHPickerFilter?, preferredItemEncoding:
PhotosPickerItem.EncodingDisambiguationPolicy, photoLibrary: PHPhotoLibrary)
-> some View`

Presents a Photos picker that selects a `PhotosPickerItem` from a given photo
library.

`func photosPicker(isPresented: Binding<Bool>, selection:
Binding<[PhotosPickerItem]>, maxSelectionCount: Int?, selectionBehavior:
PhotosPickerSelectionBehavior, matching: PHPickerFilter?,
preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy) -> some
View`

Presents a Photos picker that selects a collection of `PhotosPickerItem`.

`func photosPicker(isPresented: Binding<Bool>, selection:
Binding<[PhotosPickerItem]>, maxSelectionCount: Int?, selectionBehavior:
PhotosPickerSelectionBehavior, matching: PHPickerFilter?,
preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy,
photoLibrary: PHPhotoLibrary) -> some View`

Presents a Photos picker that selects a collection of `PhotosPickerItem` from
a given photo library.

`func photosPickerAccessoryVisibility(Visibility, edges: Edge.Set) -> some
View`

Sets the accessory visibility of the Photos picker. Accessories include
anything between the content and the edge, like the navigation bar or the
sidebar.

`func photosPickerStyle(PhotosPickerStyle) -> some View`

Sets the mode of the Photos picker.

Instance Method

# photosPickerStyle(_:)

Sets the mode of the Photos picker.

PhotosUI  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+

    
    
    func photosPickerStyle(_ style: PhotosPickerStyle) -> some View
    

##  Parameters

`mode`

    

One of the available modes.

## Return Value

A Photos picker that uses the specified mode.

## See Also

### Selecting photos

`struct PhotosPicker`

A view that displays a Photos picker for choosing assets from the photo
library.

`func photosPicker(isPresented: Binding<Bool>, selection:
Binding<PhotosPickerItem?>, matching: PHPickerFilter?, preferredItemEncoding:
PhotosPickerItem.EncodingDisambiguationPolicy) -> some View`

Presents a Photos picker that selects a `PhotosPickerItem`.

`func photosPicker(isPresented: Binding<Bool>, selection:
Binding<PhotosPickerItem?>, matching: PHPickerFilter?, preferredItemEncoding:
PhotosPickerItem.EncodingDisambiguationPolicy, photoLibrary: PHPhotoLibrary)
-> some View`

Presents a Photos picker that selects a `PhotosPickerItem` from a given photo
library.

`func photosPicker(isPresented: Binding<Bool>, selection:
Binding<[PhotosPickerItem]>, maxSelectionCount: Int?, selectionBehavior:
PhotosPickerSelectionBehavior, matching: PHPickerFilter?,
preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy) -> some
View`

Presents a Photos picker that selects a collection of `PhotosPickerItem`.

`func photosPicker(isPresented: Binding<Bool>, selection:
Binding<[PhotosPickerItem]>, maxSelectionCount: Int?, selectionBehavior:
PhotosPickerSelectionBehavior, matching: PHPickerFilter?,
preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy,
photoLibrary: PHPhotoLibrary) -> some View`

Presents a Photos picker that selects a collection of `PhotosPickerItem` from
a given photo library.

`func photosPickerAccessoryVisibility(Visibility, edges: Edge.Set) -> some
View`

Sets the accessory visibility of the Photos picker. Accessories include
anything between the content and the edge, like the navigation bar or the
sidebar.

`func photosPickerDisabledCapabilities(PHPickerCapabilities) -> some View`

Disables capabilities of the Photos picker.



# PresentationAdaptation

Type Property

# automatic

Use the default presentation adaptation.

iOS 16.4+  iPadOS 16.4+  macOS 13.3+  Mac Catalyst 16.4+  tvOS 16.4+  watchOS
9.4+  visionOS 1.0+

    
    
    static var automatic: PresentationAdaptation { get }

## See Also

### Getting adaptation strategies

`static var none: PresentationAdaptation`

Don’t adapt for the size class, if possible.

`static var fullScreenCover: PresentationAdaptation`

Prefer a full-screen-cover appearance when adapting for size classes.

`static var popover: PresentationAdaptation`

Prefer a popover appearance when adapting for size classes.

`static var sheet: PresentationAdaptation`

Prefer a sheet appearance when adapting for size classes.

Type Property

# none

Don’t adapt for the size class, if possible.

iOS 16.4+  iPadOS 16.4+  macOS 13.3+  Mac Catalyst 16.4+  tvOS 16.4+  watchOS
9.4+  visionOS 1.0+

    
    
    static var none: PresentationAdaptation { get }

## See Also

### Getting adaptation strategies

`static var automatic: PresentationAdaptation`

Use the default presentation adaptation.

`static var fullScreenCover: PresentationAdaptation`

Prefer a full-screen-cover appearance when adapting for size classes.

`static var popover: PresentationAdaptation`

Prefer a popover appearance when adapting for size classes.

`static var sheet: PresentationAdaptation`

Prefer a sheet appearance when adapting for size classes.

Type Property

# fullScreenCover

Prefer a full-screen-cover appearance when adapting for size classes.

iOS 16.4+  iPadOS 16.4+  macOS 13.3+  Mac Catalyst 16.4+  tvOS 16.4+  watchOS
9.4+  visionOS 1.0+

    
    
    static var fullScreenCover: PresentationAdaptation { get }

## See Also

### Getting adaptation strategies

`static var automatic: PresentationAdaptation`

Use the default presentation adaptation.

`static var none: PresentationAdaptation`

Don’t adapt for the size class, if possible.

`static var popover: PresentationAdaptation`

Prefer a popover appearance when adapting for size classes.

`static var sheet: PresentationAdaptation`

Prefer a sheet appearance when adapting for size classes.

Type Property

# popover

Prefer a popover appearance when adapting for size classes.

iOS 16.4+  iPadOS 16.4+  macOS 13.3+  Mac Catalyst 16.4+  tvOS 16.4+  watchOS
9.4+  visionOS 1.0+

    
    
    static var popover: PresentationAdaptation { get }

## See Also

### Getting adaptation strategies

`static var automatic: PresentationAdaptation`

Use the default presentation adaptation.

`static var none: PresentationAdaptation`

Don’t adapt for the size class, if possible.

`static var fullScreenCover: PresentationAdaptation`

Prefer a full-screen-cover appearance when adapting for size classes.

`static var sheet: PresentationAdaptation`

Prefer a sheet appearance when adapting for size classes.

Type Property

# sheet

Prefer a sheet appearance when adapting for size classes.

iOS 16.4+  iPadOS 16.4+  macOS 13.3+  Mac Catalyst 16.4+  tvOS 16.4+  watchOS
9.4+  visionOS 1.0+

    
    
    static var sheet: PresentationAdaptation { get }

## See Also

### Getting adaptation strategies

`static var automatic: PresentationAdaptation`

Use the default presentation adaptation.

`static var none: PresentationAdaptation`

Don’t adapt for the size class, if possible.

`static var fullScreenCover: PresentationAdaptation`

Prefer a full-screen-cover appearance when adapting for size classes.

`static var popover: PresentationAdaptation`

Prefer a popover appearance when adapting for size classes.



# Picker

Initializer

# init(selection:content:label:)

Creates a picker that displays a custom label.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        selection: Binding<SelectionValue>,
        @ViewBuilder content: () -> Content,
        @ViewBuilder label: () -> Label
    )

Available when `Label` conforms to `View`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

##  Parameters

`selection`

    

A binding to a property that determines the currently-selected option.

`content`

    

A view that contains the set of options.

`label`

    

A view that describes the purpose of selecting an option.

## See Also

### Creating a picker

`init(LocalizedStringKey, selection: Binding<SelectionValue>, content: () ->
Content)`

Creates a picker that generates its label from a localized string key.

Available when `Label` is `Text`, `SelectionValue` conforms to `Hashable`, and
`Content` conforms to `View`.

`init<S>(S, selection: Binding<SelectionValue>, content: () -> Content)`

Creates a picker that generates its label from a string.

Available when `Label` is `Text`, `SelectionValue` conforms to `Hashable`, and
`Content` conforms to `View`.

Initializer

# init(_:selection:content:)

Creates a picker that generates its label from a localized string key.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        selection: Binding<SelectionValue>,
        @ViewBuilder content: () -> Content
    )

Available when `Label` is `Text`, `SelectionValue` conforms to `Hashable`, and
`Content` conforms to `View`.

##  Parameters

`titleKey`

    

A localized string key that describes the purpose of selecting an option.

`selection`

    

A binding to a property that determines the currently-selected option.

`content`

    

A view that contains the set of options.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

To initialize a picker with a string variable, use
`init(_:selection:content:)` instead.

## See Also

### Creating a picker

`init(selection: Binding<SelectionValue>, content: () -> Content, label: () ->
Label)`

Creates a picker that displays a custom label.

Available when `Label` conforms to `View`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

`init<S>(S, selection: Binding<SelectionValue>, content: () -> Content)`

Creates a picker that generates its label from a string.

Available when `Label` is `Text`, `SelectionValue` conforms to `Hashable`, and
`Content` conforms to `View`.

Initializer

# init(_:selection:content:)

Creates a picker that generates its label from a string.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        selection: Binding<SelectionValue>,
        @ViewBuilder content: () -> Content
    ) where S : StringProtocol

Available when `Label` is `Text`, `SelectionValue` conforms to `Hashable`, and
`Content` conforms to `View`.

##  Parameters

`title`

    

A string that describes the purpose of selecting an option.

`selection`

    

A binding to a property that determines the currently-selected option.

`content`

    

A view that contains the set of options.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the title
similar to `init(_:)`. See `Text` for more information about localizing
strings.

To initialize a picker with a localized string key, use
`init(_:selection:content:)` instead.

## See Also

### Creating a picker

`init(selection: Binding<SelectionValue>, content: () -> Content, label: () ->
Label)`

Creates a picker that displays a custom label.

Available when `Label` conforms to `View`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

`init(LocalizedStringKey, selection: Binding<SelectionValue>, content: () ->
Content)`

Creates a picker that generates its label from a localized string key.

Available when `Label` is `Text`, `SelectionValue` conforms to `Hashable`, and
`Content` conforms to `View`.

Initializer

# init(_:sources:selection:content:)

Creates a picker that generates its label from a localized string key.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init<C>(
        _ titleKey: LocalizedStringKey,
        sources: C,
        selection: KeyPath<C.Element, Binding<SelectionValue>>,
        @ViewBuilder content: () -> Content
    ) where C : RandomAccessCollection

Available when `Label` is `Text`, `SelectionValue` conforms to `Hashable`, and
`Content` conforms to `View`.

##  Parameters

`titleKey`

    

A localized string key that describes the purpose of selecting an option.

`sources`

    

A collection of values used as the source for displaying the Picker’s
selection.

`selection`

    

The key path of the values that determines the currently-selected options.
When a user selects an option from the picker, the values at the key path of
all items in the `sources` collection are updated with the selected option.

`content`

    

A view that contains the set of options.

## Discussion

If the wrapped values of the collection passed to `sources` are not all the
same, some styles render the selection in a mixed state. The specific
presentation depends on the style. For example, a Picker with a menu style
uses dashes instead of checkmarks to indicate the selected values.

In the following example, a picker in a document inspector controls the
thickness of borders for the currently-selected shapes, which can be of any
number.

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

### Creating a picker for a collection

`init<C, S>(S, sources: C, selection: KeyPath<C.Element,
Binding<SelectionValue>>, content: () -> Content)`

Creates a picker bound to a collection of bindings that generates its label
from a string.

Available when `Label` is `Text`, `SelectionValue` conforms to `Hashable`, and
`Content` conforms to `View`.

`init<C>(sources: C, selection: KeyPath<C.Element, Binding<SelectionValue>>,
content: () -> Content, label: () -> Label)`

Creates a picker that displays a custom label.

Available when `Label` conforms to `View`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

Initializer

# init(_:sources:selection:content:)

Creates a picker bound to a collection of bindings that generates its label
from a string.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init<C, S>(
        _ title: S,
        sources: C,
        selection: KeyPath<C.Element, Binding<SelectionValue>>,
        @ViewBuilder content: () -> Content
    ) where C : RandomAccessCollection, S : StringProtocol

Available when `Label` is `Text`, `SelectionValue` conforms to `Hashable`, and
`Content` conforms to `View`.

##  Parameters

`title`

    

A string that describes the purpose of selecting an option.

`sources`

    

A collection of values used as the source for displaying the Picker’s
selection.

`selection`

    

The key path of the values that determines the currently-selected options.
When a user selects an option from the picker, the values at the key path of
all items in the `sources` collection are updated with the selected option.

`content`

    

A view that contains the set of options.

## Discussion

If the wrapped values of the collection passed to `sources` are not all the
same, some styles render the selection in a mixed state. The specific
presentation depends on the style. For example, a Picker with a menu style
uses dashes instead of checkmarks to indicate the selected values.

In the following example, a picker in a document inspector controls the
thickness of borders for the currently-selected shapes, which can be of any
number.

This initializer creates a `Text` view on your behalf, and treats the title
similar to `init(_:)`. See `Text` for more information about localizing
strings.

To initialize a picker with a localized string key, use
`init(_:sources:selection:content:)` instead.

## See Also

### Creating a picker for a collection

`init<C>(LocalizedStringKey, sources: C, selection: KeyPath<C.Element,
Binding<SelectionValue>>, content: () -> Content)`

Creates a picker that generates its label from a localized string key.

Available when `Label` is `Text`, `SelectionValue` conforms to `Hashable`, and
`Content` conforms to `View`.

`init<C>(sources: C, selection: KeyPath<C.Element, Binding<SelectionValue>>,
content: () -> Content, label: () -> Label)`

Creates a picker that displays a custom label.

Available when `Label` conforms to `View`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

Initializer

# init(sources:selection:content:label:)

Creates a picker that displays a custom label.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init<C>(
        sources: C,
        selection: KeyPath<C.Element, Binding<SelectionValue>>,
        @ViewBuilder content: () -> Content,
        @ViewBuilder label: () -> Label
    ) where C : RandomAccessCollection

Available when `Label` conforms to `View`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

##  Parameters

`sources`

    

A collection of values used as the source for displaying the Picker’s
selection.

`selection`

    

The key path of the values that determines the currently-selected options.
When a user selects an option from the picker, the values at the key path of
all items in the `sources` collection are updated with the selected option.

`content`

    

A view that contains the set of options.

`label`

    

A view that describes the purpose of selecting an option.

## Discussion

If the wrapped values of the collection passed to `sources` are not all the
same, some styles render the selection in a mixed state. The specific
presentation depends on the style. For example, a Picker with a menu style
uses dashes instead of checkmarks to indicate the selected values.

In the following example, a picker in a document inspector controls the
thickness of borders for the currently-selected shapes, which can be of any
number.

## See Also

### Creating a picker for a collection

`init<C>(LocalizedStringKey, sources: C, selection: KeyPath<C.Element,
Binding<SelectionValue>>, content: () -> Content)`

Creates a picker that generates its label from a localized string key.

Available when `Label` is `Text`, `SelectionValue` conforms to `Hashable`, and
`Content` conforms to `View`.

`init<C, S>(S, sources: C, selection: KeyPath<C.Element,
Binding<SelectionValue>>, content: () -> Content)`

Creates a picker bound to a collection of bindings that generates its label
from a string.

Available when `Label` is `Text`, `SelectionValue` conforms to `Hashable`, and
`Content` conforms to `View`.

Initializer

# init(_:image:selection:content:)

Creates a picker that generates its label from a string and image resource.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        image: ImageResource,
        selection: Binding<SelectionValue>,
        @ViewBuilder content: () -> Content
    ) where S : StringProtocol

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

##  Parameters

`title`

    

A string that describes the purpose of selecting an option.

`systemImage`

    

The name of the image resource to lookup.

`selection`

    

A binding to a property that determines the currently-selected option.

`content`

    

A view that contains the set of options.

## See Also

### Creating a picker with an image resource label

`init(LocalizedStringKey, image: ImageResource, selection:
Binding<SelectionValue>, content: () -> Content)`

Creates a picker that generates its label from a localized string key and
image resource

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

`init<C, S>(S, image: ImageResource, sources: C, selection: KeyPath<C.Element,
Binding<SelectionValue>>, content: () -> Content)`

Creates a picker bound to a collection of bindings that generates its label
from a string and image resource.

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

`init<C>(LocalizedStringKey, image: ImageResource, sources: C, selection:
KeyPath<C.Element, Binding<SelectionValue>>, content: () -> Content)`

Creates a picker that generates its label from a localized string key and
image resource.

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

Initializer

# init(_:image:selection:content:)

Creates a picker that generates its label from a localized string key and
image resource

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        image: ImageResource,
        selection: Binding<SelectionValue>,
        @ViewBuilder content: () -> Content
    )

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

##  Parameters

`titleKey`

    

A localized string key that describes the purpose of selecting an option.

`image`

    

The name of the image resource to lookup.

`selection`

    

A binding to a property that determines the currently-selected option.

`content`

    

A view that contains the set of options.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

To initialize a picker with a string variable, use
`init(_:selection:content:)` instead.

## See Also

### Creating a picker with an image resource label

`init<S>(S, image: ImageResource, selection: Binding<SelectionValue>, content:
() -> Content)`

Creates a picker that generates its label from a string and image resource.

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

`init<C, S>(S, image: ImageResource, sources: C, selection: KeyPath<C.Element,
Binding<SelectionValue>>, content: () -> Content)`

Creates a picker bound to a collection of bindings that generates its label
from a string and image resource.

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

`init<C>(LocalizedStringKey, image: ImageResource, sources: C, selection:
KeyPath<C.Element, Binding<SelectionValue>>, content: () -> Content)`

Creates a picker that generates its label from a localized string key and
image resource.

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

Initializer

# init(_:image:sources:selection:content:)

Creates a picker bound to a collection of bindings that generates its label
from a string and image resource.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init<C, S>(
        _ title: S,
        image: ImageResource,
        sources: C,
        selection: KeyPath<C.Element, Binding<SelectionValue>>,
        @ViewBuilder content: () -> Content
    ) where C : RandomAccessCollection, S : StringProtocol, C.Element == Binding<SelectionValue>

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

##  Parameters

`title`

    

A string that describes the purpose of selecting an option.

`image`

    

The name of the image resource to lookup.

`sources`

    

A collection of values used as the source for displaying the Picker’s
selection.

`selection`

    

The key path of the values that determines the currently-selected options.
When a user selects an option from the picker, the values at the key path of
all items in the `sources` collection are updated with the selected option.

`content`

    

A view that contains the set of options.

## Discussion

If the wrapped values of the collection passed to `sources` are not all the
same, some styles render the selection in a mixed state. The specific
presentation depends on the style. For example, a Picker with a menu style
uses dashes instead of checkmarks to indicate the selected values.

In the following example, a picker in a document inspector controls the
thickness of borders for the currently-selected shapes, which can be of any
number.

## See Also

### Creating a picker with an image resource label

`init<S>(S, image: ImageResource, selection: Binding<SelectionValue>, content:
() -> Content)`

Creates a picker that generates its label from a string and image resource.

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

`init(LocalizedStringKey, image: ImageResource, selection:
Binding<SelectionValue>, content: () -> Content)`

Creates a picker that generates its label from a localized string key and
image resource

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

`init<C>(LocalizedStringKey, image: ImageResource, sources: C, selection:
KeyPath<C.Element, Binding<SelectionValue>>, content: () -> Content)`

Creates a picker that generates its label from a localized string key and
image resource.

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

Initializer

# init(_:image:sources:selection:content:)

Creates a picker that generates its label from a localized string key and
image resource.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init<C>(
        _ titleKey: LocalizedStringKey,
        image: ImageResource,
        sources: C,
        selection: KeyPath<C.Element, Binding<SelectionValue>>,
        @ViewBuilder content: () -> Content
    ) where C : RandomAccessCollection, C.Element == Binding<SelectionValue>

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

##  Parameters

`titleKey`

    

A localized string key that describes the purpose of selecting an option.

`image`

    

The name of the image resource to lookup.

`sources`

    

A collection of values used as the source for displaying he Picker’s
selection.

`selection`

    

The key path of the values that determines the currently-selected options.
When a user selects an option from the picker, the values at the key path of
all items in the `sources` collection are updated with the selected option.

`content`

    

A view that contains the set of options.

## Discussion

If the wrapped values of the collection passed to `sources` are not all the
same, some styles render the selection in a mixed state. The specific
presentation depends on the style. For example, a Picker with a menu style
uses dashes instead of checkmarks to indicate the selected values.

In the following example, a picker in a document inspector controls the
thickness of borders for the currently-selected shapes, which can be of any
number.

## See Also

### Creating a picker with an image resource label

`init<S>(S, image: ImageResource, selection: Binding<SelectionValue>, content:
() -> Content)`

Creates a picker that generates its label from a string and image resource.

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

`init(LocalizedStringKey, image: ImageResource, selection:
Binding<SelectionValue>, content: () -> Content)`

Creates a picker that generates its label from a localized string key and
image resource

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

`init<C, S>(S, image: ImageResource, sources: C, selection: KeyPath<C.Element,
Binding<SelectionValue>>, content: () -> Content)`

Creates a picker bound to a collection of bindings that generates its label
from a string and image resource.

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

Initializer

# init(_:systemImage:selection:content:)

Creates a picker that generates its label from a string and system image.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        systemImage: String,
        selection: Binding<SelectionValue>,
        @ViewBuilder content: () -> Content
    ) where S : StringProtocol

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

##  Parameters

`title`

    

A string that describes the purpose of selecting an option.

`systemImage`

    

The name of the image resource to lookup.

`selection`

    

A binding to a property that determines the currently-selected option.

`content`

    

A view that contains the set of options.

## See Also

### Creating a picker with an system image label

`init(LocalizedStringKey, systemImage: String, selection:
Binding<SelectionValue>, content: () -> Content)`

Creates a picker that generates its label from a localized string key and
system image.

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

`init<C>(LocalizedStringKey, systemImage: String, sources: C, selection:
KeyPath<C.Element, Binding<SelectionValue>>, content: () -> Content)`

Creates a picker that generates its label from a localized string key.

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

`init<C, S>(S, systemImage: String, sources: C, selection: KeyPath<C.Element,
Binding<SelectionValue>>, content: () -> Content)`

Creates a picker bound to a collection of bindings that generates its label
from a string.

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

Initializer

# init(_:systemImage:selection:content:)

Creates a picker that generates its label from a localized string key and
system image.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        systemImage: String,
        selection: Binding<SelectionValue>,
        @ViewBuilder content: () -> Content
    )

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

##  Parameters

`titleKey`

    

A localized string key that describes the purpose of selecting an option.

`systemImage`

    

The name of the image resource to lookup.

`selection`

    

A binding to a property that determines the currently-selected option.

`content`

    

A view that contains the set of options.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

To initialize a picker with a string variable, use
`init(_:selection:content:)` instead.

## See Also

### Creating a picker with an system image label

`init<S>(S, systemImage: String, selection: Binding<SelectionValue>, content:
() -> Content)`

Creates a picker that generates its label from a string and system image.

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

`init<C>(LocalizedStringKey, systemImage: String, sources: C, selection:
KeyPath<C.Element, Binding<SelectionValue>>, content: () -> Content)`

Creates a picker that generates its label from a localized string key.

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

`init<C, S>(S, systemImage: String, sources: C, selection: KeyPath<C.Element,
Binding<SelectionValue>>, content: () -> Content)`

Creates a picker bound to a collection of bindings that generates its label
from a string.

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

Initializer

# init(_:systemImage:sources:selection:content:)

Creates a picker that generates its label from a localized string key.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init<C>(
        _ titleKey: LocalizedStringKey,
        systemImage: String,
        sources: C,
        selection: KeyPath<C.Element, Binding<SelectionValue>>,
        @ViewBuilder content: () -> Content
    ) where C : RandomAccessCollection, C.Element == Binding<SelectionValue>

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

##  Parameters

`titleKey`

    

A localized string key that describes the purpose of selecting an option.

`systemImage`

    

The name of the image resource to lookup.

`sources`

    

A collection of values used as the source for displaying the Picker’s
selection.

`selection`

    

The key path of the values that determines the currently-selected options.
When a user selects an option from the picker, the values at the key path of
all items in the `sources` collection are updated with the selected option.

`content`

    

A view that contains the set of options.

## Discussion

If the wrapped values of the collection passed to `sources` are not all the
same, some styles render the selection in a mixed state. The specific
presentation depends on the style. For example, a Picker with a menu style
uses dashes instead of checkmarks to indicate the selected values.

In the following example, a picker in a document inspector controls the
thickness of borders for the currently-selected shapes, which can be of any
number.

## See Also

### Creating a picker with an system image label

`init<S>(S, systemImage: String, selection: Binding<SelectionValue>, content:
() -> Content)`

Creates a picker that generates its label from a string and system image.

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

`init(LocalizedStringKey, systemImage: String, selection:
Binding<SelectionValue>, content: () -> Content)`

Creates a picker that generates its label from a localized string key and
system image.

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

`init<C, S>(S, systemImage: String, sources: C, selection: KeyPath<C.Element,
Binding<SelectionValue>>, content: () -> Content)`

Creates a picker bound to a collection of bindings that generates its label
from a string.

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

Initializer

# init(_:systemImage:sources:selection:content:)

Creates a picker bound to a collection of bindings that generates its label
from a string.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init<C, S>(
        _ title: S,
        systemImage: String,
        sources: C,
        selection: KeyPath<C.Element, Binding<SelectionValue>>,
        @ViewBuilder content: () -> Content
    ) where C : RandomAccessCollection, S : StringProtocol, C.Element == Binding<SelectionValue>

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

##  Parameters

`title`

    

A string that describes the purpose of selecting an option.

`systemImage`

    

The name of the image resource to lookup.

`sources`

    

A collection of values used as the source for displaying the Picker’s
selection.

`selection`

    

The key path of the values that determines the currently-selected options.
When a user selects an option from the picker, the values at the key path of
all items in the `sources` collection are updated with the selected option.

`content`

    

A view that contains the set of options.

## Discussion

If the wrapped values of the collection passed to `sources` are not all the
same, some styles render the selection in a mixed state. The specific
presentation depends on the style. For example, a Picker with a menu style
uses dashes instead of checkmarks to indicate the selected values.

In the following example, a picker in a document inspector controls the
thickness of borders for the currently-selected shapes, which can be of any
number.

## See Also

### Creating a picker with an system image label

`init<S>(S, systemImage: String, selection: Binding<SelectionValue>, content:
() -> Content)`

Creates a picker that generates its label from a string and system image.

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

`init(LocalizedStringKey, systemImage: String, selection:
Binding<SelectionValue>, content: () -> Content)`

Creates a picker that generates its label from a localized string key and
system image.

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

`init<C>(LocalizedStringKey, systemImage: String, sources: C, selection:
KeyPath<C.Element, Binding<SelectionValue>>, content: () -> Content)`

Creates a picker that generates its label from a localized string key.

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

Initializer

# init(selection:label:content:)

Creates a picker that displays a custom label.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    init(
        selection: Binding<SelectionValue>,
        label: Label,
        @ViewBuilder content: () -> Content
    )

Available when `Label` conforms to `View`, `SelectionValue` conforms to
`Hashable`, and `Content` conforms to `View`.

Deprecated

Use `init(selection:content:label:)` instead.

##  Parameters

`selection`

    

A binding to a property that determines the currently-selected option.

`label`

    

A view that describes the purpose of selecting an option.

`content`

    

A view that contains the set of options.



# PaletteControlGroupStyle

Initializer

# init()

Creates a palette control group style.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    init()



# PresentationMode

Instance Property

# isPresented

Indicates whether a view is currently presented.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    var isPresented: Bool { get }

Deprecated

Use `isPresented` instead.

Instance Method

# dismiss()

Dismisses the view if it is currently presented.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    mutating func dismiss()

Deprecated

Use `dismiss` instead.



# PullDownMenuButtonStyle

Initializer

# init()

macOS 10.15–14.4  Deprecated

    
    
    init()

Deprecated

Use `BorderedButtonMenuStyle` instead.



# Preferences

Instance Method

# preference(key:value:)

Sets a value for the given preference.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func preference<K>(
        key: K.Type = K.self,
        value: K.Value
    ) -> some View where K : PreferenceKey
    

## See Also

### Setting preferences

`func transformPreference<K>(K.Type, (inout K.Value) -> Void) -> some View`

Applies a transformation to a preference value.

Instance Method

# transformPreference(_:_:)

Applies a transformation to a preference value.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func transformPreference<K>(
        _ key: K.Type = K.self,
        _ callback: @escaping (inout K.Value) -> Void
    ) -> some View where K : PreferenceKey
    

## See Also

### Setting preferences

`func preference<K>(key: K.Type, value: K.Value) -> some View`

Sets a value for the given preference.

Protocol

# PreferenceKey

A named value produced by a view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    protocol PreferenceKey

## Overview

A view with multiple children automatically combines its values for a given
preference into a single value visible to its ancestors.

## Topics

### Getting the default value

`static var defaultValue: Self.Value`

The default value of the preference.

**Required** Default implementation provided.

`associatedtype Value`

The type of value produced by this preference.

**Required**

### Combining preferences

`static func reduce(value: inout Self.Value, nextValue: () -> Self.Value)`

Combines a sequence of values by modifying the previously-accumulated value
with the result of a closure that provides the next value.

**Required**

## Relationships

### Conforming Types

  * `PreferredColorSchemeKey`

Instance Method

# anchorPreference(key:value:transform:)

Sets a value for the specified preference key, the value is a function of a
geometry value tied to the current coordinate space, allowing readers of the
value to convert the geometry to their local coordinates.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func anchorPreference<A, K>(
        key _: K.Type = K.self,
        value: Anchor<A>.Source,
        transform: @escaping (Anchor<A>) -> K.Value
    ) -> some View where K : PreferenceKey
    

##  Parameters

`key`

    

the preference key type.

`value`

    

the geometry value in the current coordinate space.

`transform`

    

the function to produce the preference value.

## Return Value

a new version of the view that writes the preference.

## See Also

### Setting preferences based on geometry

`func transformAnchorPreference<A, K>(key: K.Type, value: Anchor<A>.Source,
transform: (inout K.Value, Anchor<A>) -> Void) -> some View`

Sets a value for the specified preference key, the value is a function of the
key’s current value and a geometry value tied to the current coordinate space,
allowing readers of the value to convert the geometry to their local
coordinates.

Instance Method

# transformAnchorPreference(key:value:transform:)

Sets a value for the specified preference key, the value is a function of the
key’s current value and a geometry value tied to the current coordinate space,
allowing readers of the value to convert the geometry to their local
coordinates.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func transformAnchorPreference<A, K>(
        key _: K.Type = K.self,
        value: Anchor<A>.Source,
        transform: @escaping (inout K.Value, Anchor<A>) -> Void
    ) -> some View where K : PreferenceKey
    

##  Parameters

`key`

    

the preference key type.

`value`

    

the geometry value in the current coordinate space.

`transform`

    

the function to produce the preference value.

## Return Value

a new version of the view that writes the preference.

## See Also

### Setting preferences based on geometry

`func anchorPreference<A, K>(key: K.Type, value: Anchor<A>.Source, transform:
(Anchor<A>) -> K.Value) -> some View`

Sets a value for the specified preference key, the value is a function of a
geometry value tied to the current coordinate space, allowing readers of the
value to convert the geometry to their local coordinates.

Instance Method

# onPreferenceChange(_:perform:)

Adds an action to perform when the specified preference key’s value changes.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func onPreferenceChange<K>(
        _ key: K.Type = K.self,
        perform action: @escaping (K.Value) -> Void
    ) -> some View where K : PreferenceKey, K.Value : Equatable
    

##  Parameters

`key`

    

The key to monitor for value changes.

`action`

    

The action to perform when the value for `key` changes. The `action` closure
passes the new value as its parameter.

## Return Value

A view that triggers `action` when the value for `key` changes.

Instance Method

# backgroundPreferenceValue(_:_:)

Reads the specified preference value from the view, using it to produce a
second view that is applied as the background of the original view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func backgroundPreferenceValue<Key, T>(
        _ key: Key.Type = Key.self,
        @ViewBuilder _ transform: @escaping (Key.Value) -> T
    ) -> some View where Key : PreferenceKey, T : View
    

##  Parameters

`key`

    

The preference key type whose value is to be read.

`transform`

    

A function that produces the background view from the preference value read
from the original view.

## Return Value

A view that layers a second view behind the view.

## See Also

### Generating backgrounds and overlays from preferences

`func backgroundPreferenceValue<K, V>(K.Type, alignment: Alignment, (K.Value)
-> V) -> some View`

Reads the specified preference value from the view, using it to produce a
second view that is applied as the background of the original view.

`func overlayPreferenceValue<Key, T>(Key.Type, (Key.Value) -> T) -> some View`

Reads the specified preference value from the view, using it to produce a
second view that is applied as an overlay to the original view.

`func overlayPreferenceValue<K, V>(K.Type, alignment: Alignment, (K.Value) ->
V) -> some View`

Reads the specified preference value from the view, using it to produce a
second view that is applied as an overlay to the original view.

Instance Method

# backgroundPreferenceValue(_:alignment:_:)

Reads the specified preference value from the view, using it to produce a
second view that is applied as the background of the original view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func backgroundPreferenceValue<K, V>(
        _ key: K.Type,
        alignment: Alignment = .center,
        @ViewBuilder _ transform: @escaping (K.Value) -> V
    ) -> some View where K : PreferenceKey, V : View
    

##  Parameters

`key`

    

The preference key type whose value is to be read.

`alignment`

    

An optional alignment to use when positioning the background view relative to
the original view.

`transform`

    

A function that produces the background view from the preference value read
from the original view.

## Return Value

A view that layers a second view behind the view.

## Discussion

The values of the preference key from both views are combined and made visible
to the parent view.

## See Also

### Generating backgrounds and overlays from preferences

`func backgroundPreferenceValue<Key, T>(Key.Type, (Key.Value) -> T) -> some
View`

Reads the specified preference value from the view, using it to produce a
second view that is applied as the background of the original view.

`func overlayPreferenceValue<Key, T>(Key.Type, (Key.Value) -> T) -> some View`

Reads the specified preference value from the view, using it to produce a
second view that is applied as an overlay to the original view.

`func overlayPreferenceValue<K, V>(K.Type, alignment: Alignment, (K.Value) ->
V) -> some View`

Reads the specified preference value from the view, using it to produce a
second view that is applied as an overlay to the original view.

Instance Method

# overlayPreferenceValue(_:_:)

Reads the specified preference value from the view, using it to produce a
second view that is applied as an overlay to the original view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func overlayPreferenceValue<Key, T>(
        _ key: Key.Type = Key.self,
        @ViewBuilder _ transform: @escaping (Key.Value) -> T
    ) -> some View where Key : PreferenceKey, T : View
    

##  Parameters

`key`

    

The preference key type whose value is to be read.

`transform`

    

A function that produces the overlay view from the preference value read from
the original view.

## Return Value

A view that layers a second view in front of the view.

## See Also

### Generating backgrounds and overlays from preferences

`func backgroundPreferenceValue<Key, T>(Key.Type, (Key.Value) -> T) -> some
View`

Reads the specified preference value from the view, using it to produce a
second view that is applied as the background of the original view.

`func backgroundPreferenceValue<K, V>(K.Type, alignment: Alignment, (K.Value)
-> V) -> some View`

Reads the specified preference value from the view, using it to produce a
second view that is applied as the background of the original view.

`func overlayPreferenceValue<K, V>(K.Type, alignment: Alignment, (K.Value) ->
V) -> some View`

Reads the specified preference value from the view, using it to produce a
second view that is applied as an overlay to the original view.

Instance Method

# overlayPreferenceValue(_:alignment:_:)

Reads the specified preference value from the view, using it to produce a
second view that is applied as an overlay to the original view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func overlayPreferenceValue<K, V>(
        _ key: K.Type,
        alignment: Alignment = .center,
        @ViewBuilder _ transform: @escaping (K.Value) -> V
    ) -> some View where K : PreferenceKey, V : View
    

##  Parameters

`key`

    

The preference key type whose value is to be read.

`alignment`

    

An optional alignment to use when positioning the overlay view relative to the
original view.

`transform`

    

A function that produces the overlay view from the preference value read from
the original view.

## Return Value

A view that layers a second view in front of the view.

## Discussion

The values of the preference key from both views are combined and made visible
to the parent view.

## See Also

### Generating backgrounds and overlays from preferences

`func backgroundPreferenceValue<Key, T>(Key.Type, (Key.Value) -> T) -> some
View`

Reads the specified preference value from the view, using it to produce a
second view that is applied as the background of the original view.

`func backgroundPreferenceValue<K, V>(K.Type, alignment: Alignment, (K.Value)
-> V) -> some View`

Reads the specified preference value from the view, using it to produce a
second view that is applied as the background of the original view.

`func overlayPreferenceValue<Key, T>(Key.Type, (Key.Value) -> T) -> some View`

Reads the specified preference value from the view, using it to produce a
second view that is applied as an overlay to the original view.



# PreviewPlatform

Case

# PreviewPlatform.iOS

Specifies iOS as the preview platform.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case iOS

## See Also

### Getting an operating system

`case macOS`

Specifies macOS as the preview platform.

`case tvOS`

Specifies tvOS as the preview platform.

`case watchOS`

Specifies watchOS as the preview platform.

Case

# PreviewPlatform.macOS

Specifies macOS as the preview platform.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case macOS

## See Also

### Getting an operating system

`case iOS`

Specifies iOS as the preview platform.

`case tvOS`

Specifies tvOS as the preview platform.

`case watchOS`

Specifies watchOS as the preview platform.

Case

# PreviewPlatform.tvOS

Specifies tvOS as the preview platform.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case tvOS

## See Also

### Getting an operating system

`case iOS`

Specifies iOS as the preview platform.

`case macOS`

Specifies macOS as the preview platform.

`case watchOS`

Specifies watchOS as the preview platform.

Case

# PreviewPlatform.watchOS

Specifies watchOS as the preview platform.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case watchOS

## See Also

### Getting an operating system

`case iOS`

Specifies iOS as the preview platform.

`case macOS`

Specifies macOS as the preview platform.

`case tvOS`

Specifies tvOS as the preview platform.

Case

# PreviewPlatform.iOS

Specifies iOS as the preview platform.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case iOS

## See Also

### Getting an operating system

`case macOS`

Specifies macOS as the preview platform.

`case tvOS`

Specifies tvOS as the preview platform.

`case watchOS`

Specifies watchOS as the preview platform.

Case

# PreviewPlatform.macOS

Specifies macOS as the preview platform.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case macOS

## See Also

### Getting an operating system

`case iOS`

Specifies iOS as the preview platform.

`case tvOS`

Specifies tvOS as the preview platform.

`case watchOS`

Specifies watchOS as the preview platform.

Case

# PreviewPlatform.tvOS

Specifies tvOS as the preview platform.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case tvOS

## See Also

### Getting an operating system

`case iOS`

Specifies iOS as the preview platform.

`case macOS`

Specifies macOS as the preview platform.

`case watchOS`

Specifies watchOS as the preview platform.

Case

# PreviewPlatform.watchOS

Specifies watchOS as the preview platform.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case watchOS

## See Also

### Getting an operating system

`case iOS`

Specifies iOS as the preview platform.

`case macOS`

Specifies macOS as the preview platform.

`case tvOS`

Specifies tvOS as the preview platform.



# Previews in Xcode

Macro

# Preview(_:body:)

Creates a preview of a SwiftUI view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @freestanding(declaration)
    macro Preview(
        _ name: String? = nil,
        body: @escaping @MainActor () -> any View
    )

##  Parameters

`name`

    

An optional display name for the preview. If you don’t specify a name, the
canvas labels the preview using the line number where the preview appears in
source.

`body`

    

A `ViewBuilder` that produces a SwiftUI view to preview. You typically specify
one of your app’s custom views and optionally any inputs, model data,
modifiers, and enclosing views that the custom view needs for normal
operation.

## Overview

Use this macro to display a SwiftUI preview in the canvas. You typically
specify at least one preview macro for every `View` that your app defines to
help you develop, test, and debug the view:

If you include more than one preview in a source file, the canvas provides
controls that enable you to select which to display when that source file is
active. The canvas labels the different previews with the line number where
the preview appears in source. To better identify the previews in the canvas,
you can give them names. For example if your `ContentView` takes a Boolean
input, you can create named previews for each input state:

Inside the preview, you can provide different inputs, model data, and other
infrastructure that the view needs for normal operation. For example, you can
present a custom view as the sidebar inside a `NavigationSplitView` if that’s
how your app uses the view.

Other preview macros provide different customization options. For example, if
you need to modify the appearance of a preview using one or more
`PreviewTrait`, instances, use the `Preview(_:traits:_:body:)` macro.

## See Also

### Creating a preview

`macro Preview(String?, traits: PreviewTrait<Preview.ViewTraits>,
PreviewTrait<Preview.ViewTraits>..., body: () -> any View)`

Creates a preview of a SwiftUI view using the specified traits.

`macro Preview(String?, traits: PreviewTrait<Preview.ViewTraits>..., body: ()
-> any View, cameras: () -> [PreviewCamera])`

Creates a preview of a SwiftUI view using the specified traits and custom
viewpoints.

Macro

# Preview(_:traits:_:body:)

Creates a preview of a SwiftUI view using the specified traits.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    @freestanding(declaration)
    macro Preview(
        _ name: String? = nil,
        traits: PreviewTrait<Preview.ViewTraits>,
        _ additionalTraits: PreviewTrait<Preview.ViewTraits>...,
        body: @escaping @MainActor () -> any View
    )

##  Parameters

`name`

    

An optional display name for the preview. If you don’t specify a name, the
canvas labels the preview using the line number where the preview appears in
source.

`traits`

    

A `PreviewTrait` instance that customizes the appearance of the preview.

`additionalTraits`

    

Optional additional traits that further customize the preview.

`body`

    

A `ViewBuilder` that produces a SwiftUI view to preview. You typically specify
one of your app’s custom views and optionally any inputs, model data,
modifiers, and enclosing views that the custom view needs for normal
operation.

## Overview

This macro behaves like `Preview(_:body:)` except that it also enables you to
customize the appearance of the preview by adding one or more traits, which
are instances of `PreviewTrait`. For example, you can display a preview at a
fixed size using the `fixedLayout(width:height:)` trait:

The macro ignores traits that don’t apply to the current context. For example,
the `portrait` trait has no impact on a visionOS preview.

Other preview macros provide different customization options. For example, if
you want to specify a custom viewpoint for the preview, use
`Preview(_:traits:body:cameras:)`.

## See Also

### Creating a preview

`macro Preview(String?, body: () -> any View)`

Creates a preview of a SwiftUI view.

`macro Preview(String?, traits: PreviewTrait<Preview.ViewTraits>..., body: ()
-> any View, cameras: () -> [PreviewCamera])`

Creates a preview of a SwiftUI view using the specified traits and custom
viewpoints.

Macro

# Preview(_:traits:body:cameras:)

Creates a preview of a SwiftUI view using the specified traits and custom
viewpoints.

visionOS 1.0+

    
    
    @freestanding(declaration)
    macro Preview(
        _ name: String? = nil,
        traits: PreviewTrait<Preview.ViewTraits>...,
        @ViewBuilder body: @escaping @MainActor () -> any View,
        @PreviewCameraBuilder cameras: () -> [PreviewCamera]
    )

##  Parameters

`name`

    

An optional display name for the preview. If you don’t specify a name, the
canvas labels the preview using the line number where the preview appears in
source.

`traits`

    

An optional list of `PreviewTrait` instances that customize the appearance of
the preview.

`body`

    

A `ViewBuilder` that produces a SwiftUI view to preview. You typically specify
one of your app’s custom views and optionally any inputs, model data,
modifiers, and enclosing views that the custom view needs for normal
operation.

`cameras`

    

One or more preview cameras that indicate the custom, fixed viewpoints that
you want to be able to view the preview from. The first of these replaces the
front viewpoint as the default.

## Overview

This macro behaves like `Preview(_:traits:_:body:)` except that it also
enables you to specify one or more `PreviewCamera` instances that define
custom, fixed viewpoints from which to view the preview:

If you use one of the preview macros that doesn’t include a `cameras` closure,
the canvas displays the preview from the front by default. It also provides a
camera picker to choose other standard, fixed viewpoints — like the top or the
back. When you do specify one or more preview cameras, the canvas adds a
submenu to the camera picker that lists the viewpoints that you define, like
Corner 1 and Corner 2 in the above example. The canvas also displays the
preview from the first of these custom viewpoints by default when it loads the
preview.

Note

In addition to using fixed camera perspectives, you can also interactively
alter the viewpoint of a preview in the canvas using controls like those that
Simulator provides. For more information, see Interacting with your app in the
visionOS simulator.

Other preview macros provide different customization options. For example, if
you want to preview the view as it would appear in a particular kind of scene,
you can use `Preview(_:immersionStyle:traits:body:cameras:)` or
`Preview(_:windowStyle:traits:body:cameras:)`.

## See Also

### Creating a preview

`macro Preview(String?, body: () -> any View)`

Creates a preview of a SwiftUI view.

`macro Preview(String?, traits: PreviewTrait<Preview.ViewTraits>,
PreviewTrait<Preview.ViewTraits>..., body: () -> any View)`

Creates a preview of a SwiftUI view using the specified traits.

Macro

# Preview(_:immersionStyle:traits:body:)

Creates a preview of a SwiftUI view in an immersive space.

visionOS 1.0+

    
    
    @freestanding(declaration)
    macro Preview<Style>(
        _ name: String? = nil,
        immersionStyle: Style,
        traits: PreviewTrait<Preview.ViewTraits>...,
        @ViewBuilder body: @escaping @MainActor () -> any View
    ) where Style : ImmersionStyle

##  Parameters

`name`

    

An optional display name for the preview. If you don’t specify a name, the
canvas labels the preview using the line number where the preview appears in
source.

`immersionStyle`

    

The `ImmersionStyle` to use for the preview. Use this input to display the
view as if it appears in an immersive space that has the specified style.

`traits`

    

An optional list of `PreviewTrait` instances that customize the appearance of
the preview.

`body`

    

A `ViewBuilder` that produces a SwiftUI view to preview. You typically specify
one of your app’s custom views and optionally any inputs, model data,
modifiers, and enclosing views that the custom view needs for normal
operation.

## Overview

This preview macro behaves like `Preview(_:traits:_:body:)`, except that it
also enables you to define a scene context for the view. Specifically, it
places the view in an immersive space with the specified immersion style, like
the `mixed` style:

Use this preview macro when the view needs scene context to behave as it would
during normal operation of your app.

Other preview macros provide different customization options. For example, if
you want to see how the view appears in a window rather than an immersive
space, you can use `Preview(_:windowStyle:traits:body:)`. If you want to add
custom, fixed viewpoints to an immersive space preview, use
`Preview(_:immersionStyle:traits:body:cameras:)`.

## See Also

### Creating a preview in the context of a scene

`macro Preview<Style>(String?, immersionStyle: Style, traits:
PreviewTrait<Preview.ViewTraits>..., body: () -> any View, cameras: () ->
[PreviewCamera])`

Creates a preview of a SwiftUI view in an immersive space with custom
viewpoints.

`macro Preview<Style>(String?, windowStyle: Style, traits:
PreviewTrait<Preview.ViewTraits>..., body: () -> any View)`

Creates a preview of a SwiftUI view in a window.

`macro Preview<Style>(String?, windowStyle: Style, traits:
PreviewTrait<Preview.ViewTraits>..., body: () -> any View, cameras: () ->
[PreviewCamera])`

Creates a preview of a SwiftUI view in a window with custom viewpoints.

Macro

# Preview(_:immersionStyle:traits:body:cameras:)

Creates a preview of a SwiftUI view in an immersive space with custom
viewpoints.

visionOS 1.0+

    
    
    @freestanding(declaration)
    macro Preview<Style>(
        _ name: String? = nil,
        immersionStyle: Style,
        traits: PreviewTrait<Preview.ViewTraits>...,
        @ViewBuilder body: @escaping @MainActor () -> any View,
        @PreviewCameraBuilder cameras: () -> [PreviewCamera]
    ) where Style : ImmersionStyle

##  Parameters

`name`

    

An optional display name for the preview. If you don’t specify a name, the
canvas labels the preview using the line number where the preview appears in
source.

`immersionStyle`

    

The `ImmersionStyle` to use for the preview. Use this input to display the
view as if it appears in an immersive space that has the specified style.

`traits`

    

An optional list of `PreviewTrait` instances that customize the appearance of
the preview.

`body`

    

A `ViewBuilder` that produces a SwiftUI view to preview. You typically specify
one of your app’s custom views and optionally any inputs, model data,
modifiers, and enclosing views that the custom view needs for normal
operation.

`cameras`

    

One or more preview cameras that indicate the custom, fixed viewpoints that
you want to be able to view the preview from. The first of these replaces the
front viewpoint as the default.

## Overview

This preview macro behaves like `Preview(_:immersionStyle:traits:body:)`
combined with `Preview(_:traits:body:cameras:)`: it enables you to define an
immersive space scene context for the view, and also to define custom, fixed
viewpoints for the preview:

See those other preview macros for more information about using scenes and
cameras in your preview. If you want to preview in a window rather than an
immersive space, use `Preview(_:windowStyle:traits:body:cameras:)`.

## See Also

### Creating a preview in the context of a scene

`macro Preview<Style>(String?, immersionStyle: Style, traits:
PreviewTrait<Preview.ViewTraits>..., body: () -> any View)`

Creates a preview of a SwiftUI view in an immersive space.

`macro Preview<Style>(String?, windowStyle: Style, traits:
PreviewTrait<Preview.ViewTraits>..., body: () -> any View)`

Creates a preview of a SwiftUI view in a window.

`macro Preview<Style>(String?, windowStyle: Style, traits:
PreviewTrait<Preview.ViewTraits>..., body: () -> any View, cameras: () ->
[PreviewCamera])`

Creates a preview of a SwiftUI view in a window with custom viewpoints.

Macro

# Preview(_:windowStyle:traits:body:)

Creates a preview of a SwiftUI view in a window.

visionOS 1.0+

    
    
    @freestanding(declaration)
    macro Preview<Style>(
        _ name: String? = nil,
        windowStyle: Style,
        traits: PreviewTrait<Preview.ViewTraits>...,
        @ViewBuilder body: @escaping @MainActor () -> any View
    ) where Style : WindowStyle

##  Parameters

`name`

    

An optional display name for the preview. If you don’t specify a name, the
canvas labels the preview using the line number where the preview appears in
source.

`windowStyle`

    

The `WindowStyle` to use for the preview. Use this input to display the view
as if it appears in a window that has the specified style.

`traits`

    

An optional list of `PreviewTrait` instances that customize the appearance of
the preview.

`body`

    

A `ViewBuilder` that produces a SwiftUI view to preview. You typically specify
one of your app’s custom views and optionally any inputs, model data,
modifiers, and enclosing views that the custom view needs for normal
operation.

## Overview

This preview macro behaves like `Preview(_:traits:_:body:)`, except that it
also enables you to define a scene context for the view. Specifically, it
places the view in a window with the specified window style, like the
`volumetric` style:

Use this preview macro when the view needs scene context to behave as it would
during normal operation of your app.

Other preview macros provide different customization options. For example, if
you want to see how the view appears in an immersive space rather than a
window, you can use `Preview(_:immersionStyle:traits:body:)`. If you want to
add custom, fixed viewpoints to a window-based preview, use
`Preview(_:windowStyle:traits:body:cameras:)`.

## See Also

### Creating a preview in the context of a scene

`macro Preview<Style>(String?, immersionStyle: Style, traits:
PreviewTrait<Preview.ViewTraits>..., body: () -> any View)`

Creates a preview of a SwiftUI view in an immersive space.

`macro Preview<Style>(String?, immersionStyle: Style, traits:
PreviewTrait<Preview.ViewTraits>..., body: () -> any View, cameras: () ->
[PreviewCamera])`

Creates a preview of a SwiftUI view in an immersive space with custom
viewpoints.

`macro Preview<Style>(String?, windowStyle: Style, traits:
PreviewTrait<Preview.ViewTraits>..., body: () -> any View, cameras: () ->
[PreviewCamera])`

Creates a preview of a SwiftUI view in a window with custom viewpoints.

Macro

# Preview(_:windowStyle:traits:body:cameras:)

Creates a preview of a SwiftUI view in a window with custom viewpoints.

visionOS 1.0+

    
    
    @freestanding(declaration)
    macro Preview<Style>(
        _ name: String? = nil,
        windowStyle: Style,
        traits: PreviewTrait<Preview.ViewTraits>...,
        @ViewBuilder body: @escaping @MainActor () -> any View,
        @PreviewCameraBuilder cameras: () -> [PreviewCamera]
    ) where Style : WindowStyle

##  Parameters

`name`

    

An optional display name for the preview. If you don’t specify a name, the
canvas labels the preview using the line number where the preview appears in
source.

`windowStyle`

    

The `WindowStyle` to use for the preview. Use this input to display the view
as if it appears in a window that has the specified style.

`traits`

    

An optional list of `PreviewTrait` instances that customize the appearance of
the preview.

`body`

    

A `ViewBuilder` that produces a SwiftUI view to preview. You typically specify
one of your app’s custom views and optionally any inputs, model data,
modifiers, and enclosing views that the custom view needs for normal
operation.

`cameras`

    

One or more preview cameras that indicate the custom, fixed viewpoints that
you want to be able to view the preview from. The first of these replaces the
front viewpoint as the default.

## Overview

This preview macro behaves like `Preview(_:windowStyle:traits:body:)` combined
with `Preview(_:traits:body:cameras:)`: it enables you to define a window
scene context for the view, and also to define custom, fixed viewpoints for
the preview:

See those other preview macros for more information about using scenes and
cameras in your preview. If you want to preview in an immersive space rather
than a window, use `Preview(_:immersionStyle:traits:body:cameras:)`.

## See Also

### Creating a preview in the context of a scene

`macro Preview<Style>(String?, immersionStyle: Style, traits:
PreviewTrait<Preview.ViewTraits>..., body: () -> any View)`

Creates a preview of a SwiftUI view in an immersive space.

`macro Preview<Style>(String?, immersionStyle: Style, traits:
PreviewTrait<Preview.ViewTraits>..., body: () -> any View, cameras: () ->
[PreviewCamera])`

Creates a preview of a SwiftUI view in an immersive space with custom
viewpoints.

`macro Preview<Style>(String?, windowStyle: Style, traits:
PreviewTrait<Preview.ViewTraits>..., body: () -> any View)`

Creates a preview of a SwiftUI view in a window.

Protocol

# PreviewProvider

A type that produces view previews in Xcode.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @MainActor
    protocol PreviewProvider : _PreviewProvider

## Overview

Important

You can use this protocol to define a preview manually, but you typically use
a preview macro like `Preview(_:body:)` instead.

You can create an Xcode preview by declaring a structure that conforms to the
`PreviewProvider` protocol. Implement the required `previews` computed
property, and return the view to display:

Xcode statically discovers preview providers in your project and generates
previews for any providers currently open in the source editor. Xcode
generates the preview using the current run destination as a hint for which
device to display. For example, Xcode shows the following preview if you’ve
selected an iOS target to run on the iPhone 12 Pro Max simulator:

When you create a new file (File > New > File) and choose the SwiftUI view
template, Xcode automatically inserts a preview structure at the bottom of the
file that you can configure. You can also create new preview structures in an
existing SwiftUI view file by choosing Editor > Create Preview.

Customize the preview’s appearance by adding view modifiers, just like you do
when building a custom `View`. This includes preview-specific modifiers that
let you control aspects of the preview, like the device orientation:

For the complete list of preview customizations, see Previews in Xcode.

Xcode creates different previews for each view in your preview, so you can see
variations side by side. For example, you might want to see a view’s light and
dark appearances simultaneously:

Use a `Group` when you want to maintain different previews, but apply a single
modifier to all of them:

## Topics

### Creating a preview

`static var previews: Self.Previews`

A collection of views to preview.

**Required**

` associatedtype Previews : View`

The type to preview.

**Required**

### Specifying the platform

`static var platform: PreviewPlatform?`

The platform on which to run the provider.

**Required** Default implementation provided.

## See Also

### Defining a preview

`enum PreviewPlatform`

Platforms that can run the preview.

`func previewDisplayName(String?) -> some View`

Sets a user visible name to show in the canvas for a preview.

Enumeration

# PreviewPlatform

Platforms that can run the preview.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    enum PreviewPlatform

## Overview

Xcode infers the platform for a preview based on the currently selected
target. If you have a multiplatform target and want to suggest a particular
target for a preview, implement the `platform` computed property as a hint,
and specify one of the preview platforms:

## Topics

### Getting an operating system

`case iOS`

Specifies iOS as the preview platform.

`case macOS`

Specifies macOS as the preview platform.

`case tvOS`

Specifies tvOS as the preview platform.

`case watchOS`

Specifies watchOS as the preview platform.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Defining a preview

`protocol PreviewProvider`

A type that produces view previews in Xcode.

`func previewDisplayName(String?) -> some View`

Sets a user visible name to show in the canvas for a preview.

Instance Method

# previewDisplayName(_:)

Sets a user visible name to show in the canvas for a preview.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func previewDisplayName(_ value: String?) -> some View
    

##  Parameters

`value`

    

A name for the preview.

## Return Value

A preview that uses the given name.

## Discussion

Apply this modifier to a view inside your `PreviewProvider` implementation to
associate a display name with that view’s preview:

Add a name when you have multiple previews together in the canvas that you
need to tell apart. The default value is `nil`, in which case Xcode displays a
default string.

## See Also

### Defining a preview

`protocol PreviewProvider`

A type that produces view previews in Xcode.

`enum PreviewPlatform`

Platforms that can run the preview.

Instance Method

# previewDevice(_:)

Overrides the device for a preview.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func previewDevice(_ value: PreviewDevice?) -> some View
    

##  Parameters

`value`

    

A device to use for preview, or `nil` to let Xcode automatically choose a
device based on the run destination.

## Return Value

A preview that uses the given device.

## Discussion

By default, Xcode automatically chooses a preview device based on your
currently selected run destination. If you want to choose a device that
doesn’t change based on Xcode settings, provide a `PreviewDevice` instance
that you initialize with the name or model of a specific device:

You can get a list of supported preview device names, like “iPhone 11”, “iPad
Pro (11-inch)”, and “Apple Watch Series 5 - 44mm”, by using the `xcrun`
command in the Terminal app:

Additionally, you can use the following values for macOS platform development:

  * “Mac”

  * “Mac Catalyst”

## See Also

### Customizing a preview

`struct PreviewDevice`

A simulator device that runs a preview.

`func previewLayout(PreviewLayout) -> some View`

Overrides the size of the container for the preview.

`func previewInterfaceOrientation(InterfaceOrientation) -> some View`

Overrides the orientation of the preview.

`struct InterfaceOrientation`

The orientation of the interface from the user’s perspective.

Structure

# PreviewDevice

A simulator device that runs a preview.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    struct PreviewDevice

## Overview

Create a preview device by name, like “iPhone X”, or by model number, like
“iPad8,1”. Use the device in a call to the `previewDevice(_:)` modifier to set
a preview device that doesn’t change when you change the run destination in
Xcode:

You can get a list of supported preview device names by using the `xcrun`
command in the Terminal app:

Additionally, you can use the following values for macOS platform development:

  * “Mac”

  * “Mac Catalyst”

## Relationships

### Conforms To

  * `ExpressibleByExtendedGraphemeClusterLiteral`
  * `ExpressibleByStringLiteral`
  * `ExpressibleByUnicodeScalarLiteral`
  * `RawRepresentable`
  * `Sendable`

## See Also

### Customizing a preview

`func previewDevice(PreviewDevice?) -> some View`

Overrides the device for a preview.

`func previewLayout(PreviewLayout) -> some View`

Overrides the size of the container for the preview.

`func previewInterfaceOrientation(InterfaceOrientation) -> some View`

Overrides the orientation of the preview.

`struct InterfaceOrientation`

The orientation of the interface from the user’s perspective.

Instance Method

# previewLayout(_:)

Overrides the size of the container for the preview.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func previewLayout(_ value: PreviewLayout) -> some View
    

##  Parameters

`value`

    

A layout to use for preview.

## Return Value

A preview that uses the given layout.

## Discussion

By default, previews use the `PreviewLayout/device` layout, which places the
view inside a visual representation of the chosen device. You can instead tell
a preview to use a different layout by choosing one of the `PreviewLayout`
values, like `PreviewLayout/sizeThatFits`:

## See Also

### Customizing a preview

`func previewDevice(PreviewDevice?) -> some View`

Overrides the device for a preview.

`struct PreviewDevice`

A simulator device that runs a preview.

`func previewInterfaceOrientation(InterfaceOrientation) -> some View`

Overrides the orientation of the preview.

`struct InterfaceOrientation`

The orientation of the interface from the user’s perspective.

Instance Method

# previewInterfaceOrientation(_:)

Overrides the orientation of the preview.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func previewInterfaceOrientation(_ value: InterfaceOrientation) -> some View
    

##  Parameters

`value`

    

An orientation to use for preview.

## Return Value

A preview that uses the given orientation.

## Discussion

By default, device previews appear right side up, using orientation
`portrait`. You can change the orientation of a preview using one of the
values in the `InterfaceOrientation` structure:

## See Also

### Customizing a preview

`func previewDevice(PreviewDevice?) -> some View`

Overrides the device for a preview.

`struct PreviewDevice`

A simulator device that runs a preview.

`func previewLayout(PreviewLayout) -> some View`

Overrides the size of the container for the preview.

`struct InterfaceOrientation`

The orientation of the interface from the user’s perspective.

Structure

# InterfaceOrientation

The orientation of the interface from the user’s perspective.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    struct InterfaceOrientation

## Overview

By default, device previews appear right side up, using orientation
`portrait`. You can change the orientation with a call to the
`previewInterfaceOrientation(_:)` modifier:

## Topics

### Getting an orientation

`static let portrait: InterfaceOrientation`

The device is in portrait mode, with the top of the device on top.

`static let portraitUpsideDown: InterfaceOrientation`

The device is in portrait mode, but is upside down.

`static let landscapeLeft: InterfaceOrientation`

The device is in landscape mode, with the top of the device on the left.

`static let landscapeRight: InterfaceOrientation`

The device is in landscape mode, with the top of the device on the right.

## Relationships

### Conforms To

  * `CaseIterable`
  * `Equatable`
  * `Identifiable`
  * `Sendable`

## See Also

### Customizing a preview

`func previewDevice(PreviewDevice?) -> some View`

Overrides the device for a preview.

`struct PreviewDevice`

A simulator device that runs a preview.

`func previewLayout(PreviewLayout) -> some View`

Overrides the size of the container for the preview.

`func previewInterfaceOrientation(InterfaceOrientation) -> some View`

Overrides the orientation of the preview.

Instance Method

# previewContext(_:)

Declares a context for the preview.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func previewContext<C>(_ value: C) -> some View where C : PreviewContext
    

##  Parameters

`value`

    

The context for the preview; the default is `nil`.

## See Also

### Setting a context

`protocol PreviewContext`

A context type for use with a preview.

`protocol PreviewContextKey`

A key type for a preview context.

Protocol

# PreviewContext

A context type for use with a preview.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    protocol PreviewContext

## Topics

### Accessing a preview context

`subscript<Key>(Key.Type) -> Key.Value`

Returns the context’s value for a key, or a the key’s default value if the
context doesn’t define a value for the key.

**Required**

## See Also

### Setting a context

`func previewContext<C>(C) -> some View`

Declares a context for the preview.

`protocol PreviewContextKey`

A key type for a preview context.

Protocol

# PreviewContextKey

A key type for a preview context.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    protocol PreviewContextKey

## Overview

The default value is `nil`.

## Topics

### Setting a default

`static var defaultValue: Self.Value`

The default value of the key.

**Required**

` associatedtype Value`

The type of the value returned by the key.

**Required**

## See Also

### Setting a context

`func previewContext<C>(C) -> some View`

Declares a context for the preview.

`protocol PreviewContext`

A context type for use with a preview.

Macro

# Preview(_:body:)

Creates a preview of a SwiftUI view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @freestanding(declaration)
    macro Preview(
        _ name: String? = nil,
        body: @escaping @MainActor () -> any View
    )

##  Parameters

`name`

    

An optional display name for the preview. If you don’t specify a name, the
canvas labels the preview using the line number where the preview appears in
source.

`body`

    

A `ViewBuilder` that produces a SwiftUI view to preview. You typically specify
one of your app’s custom views and optionally any inputs, model data,
modifiers, and enclosing views that the custom view needs for normal
operation.

## Overview

Use this macro to display a SwiftUI preview in the canvas. You typically
specify at least one preview macro for every `View` that your app defines to
help you develop, test, and debug the view:

If you include more than one preview in a source file, the canvas provides
controls that enable you to select which to display when that source file is
active. The canvas labels the different previews with the line number where
the preview appears in source. To better identify the previews in the canvas,
you can give them names. For example if your `ContentView` takes a Boolean
input, you can create named previews for each input state:

Inside the preview, you can provide different inputs, model data, and other
infrastructure that the view needs for normal operation. For example, you can
present a custom view as the sidebar inside a `NavigationSplitView` if that’s
how your app uses the view.

Other preview macros provide different customization options. For example, if
you need to modify the appearance of a preview using one or more
`PreviewTrait`, instances, use the `Preview(_:traits:_:body:)` macro.

## See Also

### Creating a preview

`macro Preview(String?, traits: PreviewTrait<Preview.ViewTraits>,
PreviewTrait<Preview.ViewTraits>..., body: () -> any View)`

Creates a preview of a SwiftUI view using the specified traits.

`macro Preview(String?, traits: PreviewTrait<Preview.ViewTraits>..., body: ()
-> any View, cameras: () -> [PreviewCamera])`

Creates a preview of a SwiftUI view using the specified traits and custom
viewpoints.

Macro

# Preview(_:traits:_:body:)

Creates a preview of a SwiftUI view using the specified traits.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    @freestanding(declaration)
    macro Preview(
        _ name: String? = nil,
        traits: PreviewTrait<Preview.ViewTraits>,
        _ additionalTraits: PreviewTrait<Preview.ViewTraits>...,
        body: @escaping @MainActor () -> any View
    )

##  Parameters

`name`

    

An optional display name for the preview. If you don’t specify a name, the
canvas labels the preview using the line number where the preview appears in
source.

`traits`

    

A `PreviewTrait` instance that customizes the appearance of the preview.

`additionalTraits`

    

Optional additional traits that further customize the preview.

`body`

    

A `ViewBuilder` that produces a SwiftUI view to preview. You typically specify
one of your app’s custom views and optionally any inputs, model data,
modifiers, and enclosing views that the custom view needs for normal
operation.

## Overview

This macro behaves like `Preview(_:body:)` except that it also enables you to
customize the appearance of the preview by adding one or more traits, which
are instances of `PreviewTrait`. For example, you can display a preview at a
fixed size using the `fixedLayout(width:height:)` trait:

The macro ignores traits that don’t apply to the current context. For example,
the `portrait` trait has no impact on a visionOS preview.

Other preview macros provide different customization options. For example, if
you want to specify a custom viewpoint for the preview, use
`Preview(_:traits:body:cameras:)`.

## See Also

### Creating a preview

`macro Preview(String?, body: () -> any View)`

Creates a preview of a SwiftUI view.

`macro Preview(String?, traits: PreviewTrait<Preview.ViewTraits>..., body: ()
-> any View, cameras: () -> [PreviewCamera])`

Creates a preview of a SwiftUI view using the specified traits and custom
viewpoints.

Macro

# Preview(_:traits:body:cameras:)

Creates a preview of a SwiftUI view using the specified traits and custom
viewpoints.

visionOS 1.0+

    
    
    @freestanding(declaration)
    macro Preview(
        _ name: String? = nil,
        traits: PreviewTrait<Preview.ViewTraits>...,
        @ViewBuilder body: @escaping @MainActor () -> any View,
        @PreviewCameraBuilder cameras: () -> [PreviewCamera]
    )

##  Parameters

`name`

    

An optional display name for the preview. If you don’t specify a name, the
canvas labels the preview using the line number where the preview appears in
source.

`traits`

    

An optional list of `PreviewTrait` instances that customize the appearance of
the preview.

`body`

    

A `ViewBuilder` that produces a SwiftUI view to preview. You typically specify
one of your app’s custom views and optionally any inputs, model data,
modifiers, and enclosing views that the custom view needs for normal
operation.

`cameras`

    

One or more preview cameras that indicate the custom, fixed viewpoints that
you want to be able to view the preview from. The first of these replaces the
front viewpoint as the default.

## Overview

This macro behaves like `Preview(_:traits:_:body:)` except that it also
enables you to specify one or more `PreviewCamera` instances that define
custom, fixed viewpoints from which to view the preview:

If you use one of the preview macros that doesn’t include a `cameras` closure,
the canvas displays the preview from the front by default. It also provides a
camera picker to choose other standard, fixed viewpoints — like the top or the
back. When you do specify one or more preview cameras, the canvas adds a
submenu to the camera picker that lists the viewpoints that you define, like
Corner 1 and Corner 2 in the above example. The canvas also displays the
preview from the first of these custom viewpoints by default when it loads the
preview.

Note

In addition to using fixed camera perspectives, you can also interactively
alter the viewpoint of a preview in the canvas using controls like those that
Simulator provides. For more information, see Interacting with your app in the
visionOS simulator.

Other preview macros provide different customization options. For example, if
you want to preview the view as it would appear in a particular kind of scene,
you can use `Preview(_:immersionStyle:traits:body:cameras:)` or
`Preview(_:windowStyle:traits:body:cameras:)`.

## See Also

### Creating a preview

`macro Preview(String?, body: () -> any View)`

Creates a preview of a SwiftUI view.

`macro Preview(String?, traits: PreviewTrait<Preview.ViewTraits>,
PreviewTrait<Preview.ViewTraits>..., body: () -> any View)`

Creates a preview of a SwiftUI view using the specified traits.

Macro

# Preview(_:immersionStyle:traits:body:)

Creates a preview of a SwiftUI view in an immersive space.

visionOS 1.0+

    
    
    @freestanding(declaration)
    macro Preview<Style>(
        _ name: String? = nil,
        immersionStyle: Style,
        traits: PreviewTrait<Preview.ViewTraits>...,
        @ViewBuilder body: @escaping @MainActor () -> any View
    ) where Style : ImmersionStyle

##  Parameters

`name`

    

An optional display name for the preview. If you don’t specify a name, the
canvas labels the preview using the line number where the preview appears in
source.

`immersionStyle`

    

The `ImmersionStyle` to use for the preview. Use this input to display the
view as if it appears in an immersive space that has the specified style.

`traits`

    

An optional list of `PreviewTrait` instances that customize the appearance of
the preview.

`body`

    

A `ViewBuilder` that produces a SwiftUI view to preview. You typically specify
one of your app’s custom views and optionally any inputs, model data,
modifiers, and enclosing views that the custom view needs for normal
operation.

## Overview

This preview macro behaves like `Preview(_:traits:_:body:)`, except that it
also enables you to define a scene context for the view. Specifically, it
places the view in an immersive space with the specified immersion style, like
the `mixed` style:

Use this preview macro when the view needs scene context to behave as it would
during normal operation of your app.

Other preview macros provide different customization options. For example, if
you want to see how the view appears in a window rather than an immersive
space, you can use `Preview(_:windowStyle:traits:body:)`. If you want to add
custom, fixed viewpoints to an immersive space preview, use
`Preview(_:immersionStyle:traits:body:cameras:)`.

## See Also

### Creating a preview in the context of a scene

`macro Preview<Style>(String?, immersionStyle: Style, traits:
PreviewTrait<Preview.ViewTraits>..., body: () -> any View, cameras: () ->
[PreviewCamera])`

Creates a preview of a SwiftUI view in an immersive space with custom
viewpoints.

`macro Preview<Style>(String?, windowStyle: Style, traits:
PreviewTrait<Preview.ViewTraits>..., body: () -> any View)`

Creates a preview of a SwiftUI view in a window.

`macro Preview<Style>(String?, windowStyle: Style, traits:
PreviewTrait<Preview.ViewTraits>..., body: () -> any View, cameras: () ->
[PreviewCamera])`

Creates a preview of a SwiftUI view in a window with custom viewpoints.

Macro

# Preview(_:immersionStyle:traits:body:cameras:)

Creates a preview of a SwiftUI view in an immersive space with custom
viewpoints.

visionOS 1.0+

    
    
    @freestanding(declaration)
    macro Preview<Style>(
        _ name: String? = nil,
        immersionStyle: Style,
        traits: PreviewTrait<Preview.ViewTraits>...,
        @ViewBuilder body: @escaping @MainActor () -> any View,
        @PreviewCameraBuilder cameras: () -> [PreviewCamera]
    ) where Style : ImmersionStyle

##  Parameters

`name`

    

An optional display name for the preview. If you don’t specify a name, the
canvas labels the preview using the line number where the preview appears in
source.

`immersionStyle`

    

The `ImmersionStyle` to use for the preview. Use this input to display the
view as if it appears in an immersive space that has the specified style.

`traits`

    

An optional list of `PreviewTrait` instances that customize the appearance of
the preview.

`body`

    

A `ViewBuilder` that produces a SwiftUI view to preview. You typically specify
one of your app’s custom views and optionally any inputs, model data,
modifiers, and enclosing views that the custom view needs for normal
operation.

`cameras`

    

One or more preview cameras that indicate the custom, fixed viewpoints that
you want to be able to view the preview from. The first of these replaces the
front viewpoint as the default.

## Overview

This preview macro behaves like `Preview(_:immersionStyle:traits:body:)`
combined with `Preview(_:traits:body:cameras:)`: it enables you to define an
immersive space scene context for the view, and also to define custom, fixed
viewpoints for the preview:

See those other preview macros for more information about using scenes and
cameras in your preview. If you want to preview in a window rather than an
immersive space, use `Preview(_:windowStyle:traits:body:cameras:)`.

## See Also

### Creating a preview in the context of a scene

`macro Preview<Style>(String?, immersionStyle: Style, traits:
PreviewTrait<Preview.ViewTraits>..., body: () -> any View)`

Creates a preview of a SwiftUI view in an immersive space.

`macro Preview<Style>(String?, windowStyle: Style, traits:
PreviewTrait<Preview.ViewTraits>..., body: () -> any View)`

Creates a preview of a SwiftUI view in a window.

`macro Preview<Style>(String?, windowStyle: Style, traits:
PreviewTrait<Preview.ViewTraits>..., body: () -> any View, cameras: () ->
[PreviewCamera])`

Creates a preview of a SwiftUI view in a window with custom viewpoints.

Macro

# Preview(_:windowStyle:traits:body:)

Creates a preview of a SwiftUI view in a window.

visionOS 1.0+

    
    
    @freestanding(declaration)
    macro Preview<Style>(
        _ name: String? = nil,
        windowStyle: Style,
        traits: PreviewTrait<Preview.ViewTraits>...,
        @ViewBuilder body: @escaping @MainActor () -> any View
    ) where Style : WindowStyle

##  Parameters

`name`

    

An optional display name for the preview. If you don’t specify a name, the
canvas labels the preview using the line number where the preview appears in
source.

`windowStyle`

    

The `WindowStyle` to use for the preview. Use this input to display the view
as if it appears in a window that has the specified style.

`traits`

    

An optional list of `PreviewTrait` instances that customize the appearance of
the preview.

`body`

    

A `ViewBuilder` that produces a SwiftUI view to preview. You typically specify
one of your app’s custom views and optionally any inputs, model data,
modifiers, and enclosing views that the custom view needs for normal
operation.

## Overview

This preview macro behaves like `Preview(_:traits:_:body:)`, except that it
also enables you to define a scene context for the view. Specifically, it
places the view in a window with the specified window style, like the
`volumetric` style:

Use this preview macro when the view needs scene context to behave as it would
during normal operation of your app.

Other preview macros provide different customization options. For example, if
you want to see how the view appears in an immersive space rather than a
window, you can use `Preview(_:immersionStyle:traits:body:)`. If you want to
add custom, fixed viewpoints to a window-based preview, use
`Preview(_:windowStyle:traits:body:cameras:)`.

## See Also

### Creating a preview in the context of a scene

`macro Preview<Style>(String?, immersionStyle: Style, traits:
PreviewTrait<Preview.ViewTraits>..., body: () -> any View)`

Creates a preview of a SwiftUI view in an immersive space.

`macro Preview<Style>(String?, immersionStyle: Style, traits:
PreviewTrait<Preview.ViewTraits>..., body: () -> any View, cameras: () ->
[PreviewCamera])`

Creates a preview of a SwiftUI view in an immersive space with custom
viewpoints.

`macro Preview<Style>(String?, windowStyle: Style, traits:
PreviewTrait<Preview.ViewTraits>..., body: () -> any View, cameras: () ->
[PreviewCamera])`

Creates a preview of a SwiftUI view in a window with custom viewpoints.

Macro

# Preview(_:windowStyle:traits:body:cameras:)

Creates a preview of a SwiftUI view in a window with custom viewpoints.

visionOS 1.0+

    
    
    @freestanding(declaration)
    macro Preview<Style>(
        _ name: String? = nil,
        windowStyle: Style,
        traits: PreviewTrait<Preview.ViewTraits>...,
        @ViewBuilder body: @escaping @MainActor () -> any View,
        @PreviewCameraBuilder cameras: () -> [PreviewCamera]
    ) where Style : WindowStyle

##  Parameters

`name`

    

An optional display name for the preview. If you don’t specify a name, the
canvas labels the preview using the line number where the preview appears in
source.

`windowStyle`

    

The `WindowStyle` to use for the preview. Use this input to display the view
as if it appears in a window that has the specified style.

`traits`

    

An optional list of `PreviewTrait` instances that customize the appearance of
the preview.

`body`

    

A `ViewBuilder` that produces a SwiftUI view to preview. You typically specify
one of your app’s custom views and optionally any inputs, model data,
modifiers, and enclosing views that the custom view needs for normal
operation.

`cameras`

    

One or more preview cameras that indicate the custom, fixed viewpoints that
you want to be able to view the preview from. The first of these replaces the
front viewpoint as the default.

## Overview

This preview macro behaves like `Preview(_:windowStyle:traits:body:)` combined
with `Preview(_:traits:body:cameras:)`: it enables you to define a window
scene context for the view, and also to define custom, fixed viewpoints for
the preview:

    
    
    #Preview("Volume", windowStyle: .volumetric) {
       ContentView()
    } cameras: {
       PreviewCamera(from: .front)
       PreviewCamera(from: .top, zoom: 2)
       PreviewCamera(from: .leading, zoom: 0.5, name: "close up")
    }
    

See those other preview macros for more information about using scenes and
cameras in your preview. If you want to preview in an immersive space rather
than a window, use `Preview(_:immersionStyle:traits:body:cameras:)`.

## See Also

### Creating a preview in the context of a scene

`macro Preview<Style>(String?, immersionStyle: Style, traits:
PreviewTrait<Preview.ViewTraits>..., body: () -> any View)`

Creates a preview of a SwiftUI view in an immersive space.

`macro Preview<Style>(String?, immersionStyle: Style, traits:
PreviewTrait<Preview.ViewTraits>..., body: () -> any View, cameras: () ->
[PreviewCamera])`

Creates a preview of a SwiftUI view in an immersive space with custom
viewpoints.

`macro Preview<Style>(String?, windowStyle: Style, traits:
PreviewTrait<Preview.ViewTraits>..., body: () -> any View)`

Creates a preview of a SwiftUI view in a window.

Protocol

# PreviewProvider

A type that produces view previews in Xcode.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @MainActor
    protocol PreviewProvider : _PreviewProvider

## Overview

Important

You can use this protocol to define a preview manually, but you typically use
a preview macro like `Preview(_:body:)` instead.

You can create an Xcode preview by declaring a structure that conforms to the
`PreviewProvider` protocol. Implement the required `previews` computed
property, and return the view to display:

    
    
    struct CircleImage_Previews: PreviewProvider {
        static var previews: some View {
            CircleImage()
        }
    }
    

Xcode statically discovers preview providers in your project and generates
previews for any providers currently open in the source editor. Xcode
generates the preview using the current run destination as a hint for which
device to display. For example, Xcode shows the following preview if you’ve
selected an iOS target to run on the iPhone 12 Pro Max simulator:

When you create a new file (File > New > File) and choose the SwiftUI view
template, Xcode automatically inserts a preview structure at the bottom of the
file that you can configure. You can also create new preview structures in an
existing SwiftUI view file by choosing Editor > Create Preview.

Customize the preview’s appearance by adding view modifiers, just like you do
when building a custom `View`. This includes preview-specific modifiers that
let you control aspects of the preview, like the device orientation:

    
    
    struct CircleImage_Previews: PreviewProvider {
        static var previews: some View {
            CircleImage()
                .previewInterfaceOrientation(.landscapeLeft)
        }
    }
    

For the complete list of preview customizations, see Previews in Xcode.

Xcode creates different previews for each view in your preview, so you can see
variations side by side. For example, you might want to see a view’s light and
dark appearances simultaneously:

    
    
    struct CircleImage_Previews: PreviewProvider {
        static var previews: some View {
            CircleImage()
            CircleImage()
                .preferredColorScheme(.dark)
        }
    }
    

Use a `Group` when you want to maintain different previews, but apply a single
modifier to all of them:

    
    
    struct CircleImage_Previews: PreviewProvider {
        static var previews: some View {
            Group {
                CircleImage()
                CircleImage()
                    .preferredColorScheme(.dark)
            }
            .previewLayout(.sizeThatFits)
        }
    }
    

## Topics

### Creating a preview

`static var previews: Self.Previews`

A collection of views to preview.

**Required**

` associatedtype Previews : View`

The type to preview.

**Required**

### Specifying the platform

`static var platform: PreviewPlatform?`

The platform on which to run the provider.

**Required** Default implementation provided.

## See Also

### Defining a preview

`enum PreviewPlatform`

Platforms that can run the preview.

`func previewDisplayName(String?) -> some View`

Sets a user visible name to show in the canvas for a preview.

Enumeration

# PreviewPlatform

Platforms that can run the preview.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    enum PreviewPlatform

## Overview

Xcode infers the platform for a preview based on the currently selected
target. If you have a multiplatform target and want to suggest a particular
target for a preview, implement the `platform` computed property as a hint,
and specify one of the preview platforms:

    
    
    struct CircleImage_Previews: PreviewProvider {
        static var previews: some View {
            CircleImage()
        }
    
    
        static var platform: PreviewPlatform? {
            PreviewPlatform.tvOS
        }
    }
    

## Topics

### Getting an operating system

`case iOS`

Specifies iOS as the preview platform.

`case macOS`

Specifies macOS as the preview platform.

`case tvOS`

Specifies tvOS as the preview platform.

`case watchOS`

Specifies watchOS as the preview platform.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Defining a preview

`protocol PreviewProvider`

A type that produces view previews in Xcode.

`func previewDisplayName(String?) -> some View`

Sets a user visible name to show in the canvas for a preview.

Instance Method

# previewDisplayName(_:)

Sets a user visible name to show in the canvas for a preview.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func previewDisplayName(_ value: String?) -> some View
    

##  Parameters

`value`

    

A name for the preview.

## Return Value

A preview that uses the given name.

## Discussion

Apply this modifier to a view inside your `PreviewProvider` implementation to
associate a display name with that view’s preview:

Add a name when you have multiple previews together in the canvas that you
need to tell apart. The default value is `nil`, in which case Xcode displays a
default string.

## See Also

### Defining a preview

`protocol PreviewProvider`

A type that produces view previews in Xcode.

`enum PreviewPlatform`

Platforms that can run the preview.

Instance Method

# previewDevice(_:)

Overrides the device for a preview.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func previewDevice(_ value: PreviewDevice?) -> some View
    

##  Parameters

`value`

    

A device to use for preview, or `nil` to let Xcode automatically choose a
device based on the run destination.

## Return Value

A preview that uses the given device.

## Discussion

By default, Xcode automatically chooses a preview device based on your
currently selected run destination. If you want to choose a device that
doesn’t change based on Xcode settings, provide a `PreviewDevice` instance
that you initialize with the name or model of a specific device:

You can get a list of supported preview device names, like “iPhone 11”, “iPad
Pro (11-inch)”, and “Apple Watch Series 5 - 44mm”, by using the `xcrun`
command in the Terminal app:

Additionally, you can use the following values for macOS platform development:

  * “Mac”

  * “Mac Catalyst”

## See Also

### Customizing a preview

`struct PreviewDevice`

A simulator device that runs a preview.

`func previewLayout(PreviewLayout) -> some View`

Overrides the size of the container for the preview.

`func previewInterfaceOrientation(InterfaceOrientation) -> some View`

Overrides the orientation of the preview.

`struct InterfaceOrientation`

The orientation of the interface from the user’s perspective.

Structure

# PreviewDevice

A simulator device that runs a preview.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    struct PreviewDevice

## Overview

Create a preview device by name, like “iPhone X”, or by model number, like
“iPad8,1”. Use the device in a call to the `previewDevice(_:)` modifier to set
a preview device that doesn’t change when you change the run destination in
Xcode:

    
    
    struct CircleImage_Previews: PreviewProvider {
        static var previews: some View {
            CircleImage()
                .previewDevice(PreviewDevice(rawValue: "iPad Pro (11-inch)"))
        }
    }
    

You can get a list of supported preview device names by using the `xcrun`
command in the Terminal app:

    
    
    % xcrun simctl list devicetypes
    

Additionally, you can use the following values for macOS platform development:

  * “Mac”

  * “Mac Catalyst”

## Relationships

### Conforms To

  * `ExpressibleByExtendedGraphemeClusterLiteral`
  * `ExpressibleByStringLiteral`
  * `ExpressibleByUnicodeScalarLiteral`
  * `RawRepresentable`
  * `Sendable`

## See Also

### Customizing a preview

`func previewDevice(PreviewDevice?) -> some View`

Overrides the device for a preview.

`func previewLayout(PreviewLayout) -> some View`

Overrides the size of the container for the preview.

`func previewInterfaceOrientation(InterfaceOrientation) -> some View`

Overrides the orientation of the preview.

`struct InterfaceOrientation`

The orientation of the interface from the user’s perspective.

Instance Method

# previewLayout(_:)

Overrides the size of the container for the preview.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func previewLayout(_ value: PreviewLayout) -> some View
    

##  Parameters

`value`

    

A layout to use for preview.

## Return Value

A preview that uses the given layout.

## Discussion

By default, previews use the `PreviewLayout/device` layout, which places the
view inside a visual representation of the chosen device. You can instead tell
a preview to use a different layout by choosing one of the `PreviewLayout`
values, like `PreviewLayout/sizeThatFits`:

    
    
    struct CircleImage_Previews: PreviewProvider {
        static var previews: some View {
            CircleImage()
                .previewLayout(.sizeThatFits)
        }
    }
    

## See Also

### Customizing a preview

`func previewDevice(PreviewDevice?) -> some View`

Overrides the device for a preview.

`struct PreviewDevice`

A simulator device that runs a preview.

`func previewInterfaceOrientation(InterfaceOrientation) -> some View`

Overrides the orientation of the preview.

`struct InterfaceOrientation`

The orientation of the interface from the user’s perspective.

Instance Method

# previewInterfaceOrientation(_:)

Overrides the orientation of the preview.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func previewInterfaceOrientation(_ value: InterfaceOrientation) -> some View
    

##  Parameters

`value`

    

An orientation to use for preview.

## Return Value

A preview that uses the given orientation.

## Discussion

By default, device previews appear right side up, using orientation
`portrait`. You can change the orientation of a preview using one of the
values in the `InterfaceOrientation` structure:

    
    
    struct CircleImage_Previews: PreviewProvider {
        static var previews: some View {
            CircleImage()
                .previewInterfaceOrientation(.landscapeRight)
        }
    }
    

## See Also

### Customizing a preview

`func previewDevice(PreviewDevice?) -> some View`

Overrides the device for a preview.

`struct PreviewDevice`

A simulator device that runs a preview.

`func previewLayout(PreviewLayout) -> some View`

Overrides the size of the container for the preview.

`struct InterfaceOrientation`

The orientation of the interface from the user’s perspective.

Structure

# InterfaceOrientation

The orientation of the interface from the user’s perspective.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    struct InterfaceOrientation

## Overview

By default, device previews appear right side up, using orientation
`portrait`. You can change the orientation with a call to the
`previewInterfaceOrientation(_:)` modifier:

    
    
    struct CircleImage_Previews: PreviewProvider {
        static var previews: some View {
            CircleImage()
                .previewInterfaceOrientation(.landscapeRight)
        }
    }
    

## Topics

### Getting an orientation

`static let portrait: InterfaceOrientation`

The device is in portrait mode, with the top of the device on top.

`static let portraitUpsideDown: InterfaceOrientation`

The device is in portrait mode, but is upside down.

`static let landscapeLeft: InterfaceOrientation`

The device is in landscape mode, with the top of the device on the left.

`static let landscapeRight: InterfaceOrientation`

The device is in landscape mode, with the top of the device on the right.

## Relationships

### Conforms To

  * `CaseIterable`
  * `Equatable`
  * `Identifiable`
  * `Sendable`

## See Also

### Customizing a preview

`func previewDevice(PreviewDevice?) -> some View`

Overrides the device for a preview.

`struct PreviewDevice`

A simulator device that runs a preview.

`func previewLayout(PreviewLayout) -> some View`

Overrides the size of the container for the preview.

`func previewInterfaceOrientation(InterfaceOrientation) -> some View`

Overrides the orientation of the preview.

Instance Method

# previewContext(_:)

Declares a context for the preview.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func previewContext<C>(_ value: C) -> some View where C : PreviewContext
    

##  Parameters

`value`

    

The context for the preview; the default is `nil`.

## See Also

### Setting a context

`protocol PreviewContext`

A context type for use with a preview.

`protocol PreviewContextKey`

A key type for a preview context.

Protocol

# PreviewContext

A context type for use with a preview.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    protocol PreviewContext

## Topics

### Accessing a preview context

`subscript<Key>(Key.Type) -> Key.Value`

Returns the context’s value for a key, or a the key’s default value if the
context doesn’t define a value for the key.

**Required**

## See Also

### Setting a context

`func previewContext<C>(C) -> some View`

Declares a context for the preview.

`protocol PreviewContextKey`

A key type for a preview context.

Protocol

# PreviewContextKey

A key type for a preview context.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    protocol PreviewContextKey

## Overview

The default value is `nil`.

## Topics

### Setting a default

`static var defaultValue: Self.Value`

The default value of the key.

**Required**

` associatedtype Value`

The type of the value returned by the key.

**Required**

## See Also

### Setting a context

`func previewContext<C>(C) -> some View`

Declares a context for the preview.

`protocol PreviewContext`

A context type for use with a preview.



# PageIndexViewStyle

Initializer

# init(backgroundDisplayMode:)

Creates a page index view style.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS 8.0+
visionOS 1.0+

    
    
    init(backgroundDisplayMode: PageIndexViewStyle.BackgroundDisplayMode = .automatic)

##  Parameters

`backgroundDisplayMode`

    

The display mode of the background of any page index views receiving this
style

## See Also

### Creating the control group style

`struct BackgroundDisplayMode`

The background style for the page index view.

Structure

# PageIndexViewStyle.BackgroundDisplayMode

The background style for the page index view.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS 8.0+
visionOS 1.0+

    
    
    struct BackgroundDisplayMode

## Topics

### Getting the display modes

`static let automatic: PageIndexViewStyle.BackgroundDisplayMode`

Background will use the default for the platform.

`static let always: PageIndexViewStyle.BackgroundDisplayMode`

Background is always displayed behind the page index view.

`static let interactive: PageIndexViewStyle.BackgroundDisplayMode`

Background is only shown while the index view is interacted with.

`static let never: PageIndexViewStyle.BackgroundDisplayMode`

Background is never displayed behind the page index view.

## Relationships

### Conforms To

  * `Sendable`

## See Also

### Creating the control group style

`init(backgroundDisplayMode: PageIndexViewStyle.BackgroundDisplayMode)`

Creates a page index view style.



# ProposedViewSize

Type Property

# zero

A size proposal that contains zero in both dimensions.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static let zero: ProposedViewSize

## Discussion

Subviews of a custom layout return their minimum size when you propose this
value using the `dimensions(in:)` method. A custom layout should also return
its minimum size from the `sizeThatFits(proposal:subviews:cache:)` method for
this value.

## See Also

### Getting standard proposals

`static let infinity: ProposedViewSize`

A size proposal that contains infinity in both dimensions.

`static let unspecified: ProposedViewSize`

The proposed size with both dimensions left unspecified.

Type Property

# infinity

A size proposal that contains infinity in both dimensions.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static let infinity: ProposedViewSize

## Discussion

Both dimensions contain `infinity` in this size proposal. Subviews of a custom
layout return their maximum size when you propose this value using the
`dimensions(in:)` method. A custom layout should also return its maximum size
from the `sizeThatFits(proposal:subviews:cache:)` method for this value.

## See Also

### Getting standard proposals

`static let zero: ProposedViewSize`

A size proposal that contains zero in both dimensions.

`static let unspecified: ProposedViewSize`

The proposed size with both dimensions left unspecified.

Type Property

# unspecified

The proposed size with both dimensions left unspecified.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static let unspecified: ProposedViewSize

## Discussion

Both dimensions contain `nil` in this size proposal. Subviews of a custom
layout return their ideal size when you propose this value using the
`dimensions(in:)` method. A custom layout should also return its ideal size
from the `sizeThatFits(proposal:subviews:cache:)` method for this value.

## See Also

### Getting standard proposals

`static let zero: ProposedViewSize`

A size proposal that contains zero in both dimensions.

`static let infinity: ProposedViewSize`

A size proposal that contains infinity in both dimensions.

Initializer

# init(_:)

Creates a new proposed size from a specified size.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init(_ size: CGSize)

##  Parameters

`size`

    

A proposed size with dimensions measured in points.

## See Also

### Creating a custom size proposal

`init(width: CGFloat?, height: CGFloat?)`

Creates a new proposed size using the specified width and height.

Initializer

# init(width:height:)

Creates a new proposed size using the specified width and height.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init(
        width: CGFloat?,
        height: CGFloat?
    )

##  Parameters

`width`

    

A proposed width in points. Use a value of `nil` to indicate that the width is
unspecified for this proposal.

`height`

    

A proposed height in points. Use a value of `nil` to indicate that the height
is unspecified for this proposal.

## See Also

### Creating a custom size proposal

`init(CGSize)`

Creates a new proposed size from a specified size.

Instance Property

# height

The proposed vertical size measured in points.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var height: CGFloat?

## Discussion

A value of `nil` represents an unspecified height proposal, which a view
interprets to mean that it should use its ideal height.

## See Also

### Getting the proposal’s dimensions

`var width: CGFloat?`

The proposed horizontal size measured in points.

Instance Property

# width

The proposed horizontal size measured in points.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var width: CGFloat?

## Discussion

A value of `nil` represents an unspecified width proposal, which a view
interprets to mean that it should use its ideal width.

## See Also

### Getting the proposal’s dimensions

`var height: CGFloat?`

The proposed vertical size measured in points.

Instance Method

# replacingUnspecifiedDimensions(by:)

Creates a new proposal that replaces unspecified dimensions in this proposal
with the corresponding dimension of the specified size.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func replacingUnspecifiedDimensions(by size: CGSize = CGSize(width: 10, height: 10)) -> CGSize

##  Parameters

`size`

    

A set of concrete values to use for the size proposal in place of any
unspecified dimensions. The default value is `10` for both dimensions.

## Return Value

A new, fully specified size proposal.

## Discussion

Use the default value to prevent a flexible view from disappearing into a
zero-sized frame, and ensure the unspecified value remains visible during
debugging.



# PlainTextFieldStyle

Initializer

# init()

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init()



# PaletteSelectionEffect

Type Property

# automatic

Applies the system’s default effect when selected.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    static var automatic: PaletteSelectionEffect

## Discussion

When using un-tinted SF Symbols or template images, the current tint color is
applied to the selected items’ image. If the provided SF Symbols have custom
tints, a stroke is drawn around selected items.

## See Also

### Getting palette selection effects

`static var custom: PaletteSelectionEffect`

Does not apply any system effect when selected.

`static func symbolVariant(SymbolVariants) -> PaletteSelectionEffect`

Applies the specified symbol variant when selected.

Type Property

# custom

Does not apply any system effect when selected.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    static var custom: PaletteSelectionEffect

## Discussion

Note

Make sure to manually implement a way to indicate selection when using this
case. For example, you could dynamically resolve the item’s image based on the
selection state.

## See Also

### Getting palette selection effects

`static var automatic: PaletteSelectionEffect`

Applies the system’s default effect when selected.

`static func symbolVariant(SymbolVariants) -> PaletteSelectionEffect`

Applies the specified symbol variant when selected.

Type Method

# symbolVariant(_:)

Applies the specified symbol variant when selected.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    static func symbolVariant(_ variant: SymbolVariants) -> PaletteSelectionEffect

## Discussion

Note

This effect only applies to SF Symbols.

## See Also

### Getting palette selection effects

`static var automatic: PaletteSelectionEffect`

Applies the system’s default effect when selected.

`static var custom: PaletteSelectionEffect`

Does not apply any system effect when selected.



# PushTransition

Initializer

# init(edge:)

Creates a transition that animates a view by moving and fading it.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init(edge: Edge)

## See Also

### Creating the transition

`var edge: Edge`

The edge from which the view will be animated in.

Instance Property

# edge

The edge from which the view will be animated in.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var edge: Edge

## See Also

### Creating the transition

`init(edge: Edge)`

Creates a transition that animates a view by moving and fading it.



