Type Property

# animation

A pausable schedule of dates updating at a frequency no more quickly than the
provided interval.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var animation: AnimationTimelineSchedule { get }

Available when `Self` is `AnimationTimelineSchedule`.

## See Also

### Getting built-in schedules

`static func animation(minimumInterval: Double?, paused: Bool) ->
AnimationTimelineSchedule`

A pausable schedule of dates updating at a frequency no more quickly than the
provided interval.

Available when `Self` is `AnimationTimelineSchedule`.

`static var everyMinute: EveryMinuteTimelineSchedule`

A schedule for updating a timeline view at the start of every minute.

Available when `Self` is `EveryMinuteTimelineSchedule`.

`static func explicit<S>(S) -> ExplicitTimelineSchedule<S>`

A schedule for updating a timeline view at explicit points in time.

`static func periodic(from: Date, by: TimeInterval) ->
PeriodicTimelineSchedule`

A schedule for updating a timeline view at regular intervals.

Available when `Self` is `PeriodicTimelineSchedule`.

Type Method

# animation(minimumInterval:paused:)

A pausable schedule of dates updating at a frequency no more quickly than the
provided interval.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static func animation(
        minimumInterval: Double? = nil,
        paused: Bool = false
    ) -> AnimationTimelineSchedule

Available when `Self` is `AnimationTimelineSchedule`.

##  Parameters

`minimumInterval`

    

The minimum interval to update the schedule at. Pass nil to let the system
pick an appropriate update interval.

`paused`

    

If the schedule should stop generating updates.

## See Also

### Getting built-in schedules

`static var animation: AnimationTimelineSchedule`

A pausable schedule of dates updating at a frequency no more quickly than the
provided interval.

Available when `Self` is `AnimationTimelineSchedule`.

`static var everyMinute: EveryMinuteTimelineSchedule`

A schedule for updating a timeline view at the start of every minute.

Available when `Self` is `EveryMinuteTimelineSchedule`.

`static func explicit<S>(S) -> ExplicitTimelineSchedule<S>`

A schedule for updating a timeline view at explicit points in time.

`static func periodic(from: Date, by: TimeInterval) ->
PeriodicTimelineSchedule`

A schedule for updating a timeline view at regular intervals.

Available when `Self` is `PeriodicTimelineSchedule`.

Type Property

# everyMinute

A schedule for updating a timeline view at the start of every minute.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static var everyMinute: EveryMinuteTimelineSchedule { get }

Available when `Self` is `EveryMinuteTimelineSchedule`.

## Discussion

Initialize a `TimelineView` with an every minute timeline schedule when you
want to schedule timeline view updates at the start of every minute:

The schedule provides the first date as the beginning of the minute in which
you use it to initialize the timeline view. For example, if you create the
timeline view at `10:09:38`, the schedule’s first entry is `10:09:00`. In
response, the timeline view performs its first update immediately, providing
the beginning of the current minute, namely `10:09:00`, as context to its
content. Subsequent updates happen at the beginning of each minute that
follows.

The schedule defines the `EveryMinuteTimelineSchedule.Entries` structure to
return the sequence of dates when the timeline view calls the
`entries(from:mode:)` method.

## See Also

### Getting built-in schedules

`static var animation: AnimationTimelineSchedule`

A pausable schedule of dates updating at a frequency no more quickly than the
provided interval.

Available when `Self` is `AnimationTimelineSchedule`.

`static func animation(minimumInterval: Double?, paused: Bool) ->
AnimationTimelineSchedule`

A pausable schedule of dates updating at a frequency no more quickly than the
provided interval.

Available when `Self` is `AnimationTimelineSchedule`.

`static func explicit<S>(S) -> ExplicitTimelineSchedule<S>`

A schedule for updating a timeline view at explicit points in time.

`static func periodic(from: Date, by: TimeInterval) ->
PeriodicTimelineSchedule`

A schedule for updating a timeline view at regular intervals.

Available when `Self` is `PeriodicTimelineSchedule`.

Type Method

# explicit(_:)

A schedule for updating a timeline view at explicit points in time.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static func explicit<S>(_ dates: S) -> ExplicitTimelineSchedule<S> where Self == ExplicitTimelineSchedule<S>, S : Sequence, S.Element == Date

##  Parameters

`dates`

    

The sequence of dates at which a timeline view updates. Use a monotonically
increasing sequence of dates, and ensure that at least one is in the future.

## Discussion

Initialize a `TimelineView` with an explicit timeline schedule when you want
to schedule view updates at particular points in time:

The timeline view updates its content on exactly the dates that you specify,
until it runs out of dates, after which it stops changing. If the dates you
provide are in the past, the timeline view updates exactly once with the last
entry. If you only provide dates in the future, the timeline view renders with
the current date until the first date arrives. If you provide one or more
dates in the past and one or more in the future, the view renders the most
recent past date, refreshing normally on all subsequent dates.

## See Also

### Getting built-in schedules

`static var animation: AnimationTimelineSchedule`

A pausable schedule of dates updating at a frequency no more quickly than the
provided interval.

Available when `Self` is `AnimationTimelineSchedule`.

`static func animation(minimumInterval: Double?, paused: Bool) ->
AnimationTimelineSchedule`

A pausable schedule of dates updating at a frequency no more quickly than the
provided interval.

Available when `Self` is `AnimationTimelineSchedule`.

`static var everyMinute: EveryMinuteTimelineSchedule`

A schedule for updating a timeline view at the start of every minute.

Available when `Self` is `EveryMinuteTimelineSchedule`.

`static func periodic(from: Date, by: TimeInterval) ->
PeriodicTimelineSchedule`

A schedule for updating a timeline view at regular intervals.

Available when `Self` is `PeriodicTimelineSchedule`.

Type Method

# periodic(from:by:)

A schedule for updating a timeline view at regular intervals.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static func periodic(
        from startDate: Date,
        by interval: TimeInterval
    ) -> PeriodicTimelineSchedule

Available when `Self` is `PeriodicTimelineSchedule`.

##  Parameters

`startDate`

    

The date on which to start the sequence.

`interval`

    

The time interval between successive sequence entries.

## Discussion

Initialize a `TimelineView` with a periodic timeline schedule when you want to
schedule timeline view updates periodically with a custom interval:

The timeline view updates its content at the start date, and then again at
dates separated in time by the interval amount, which is every three seconds
in the example above. For a start date in the past, the view updates
immediately, providing as context the date corresponding to the most recent
interval boundary. The view then refreshes normally at subsequent interval
boundaries. For a start date in the future, the view updates once with the
current date, and then begins regular updates at the start date.

The schedule defines the `PeriodicTimelineSchedule.Entries` structure to
return the sequence of dates when the timeline view calls the
`entries(from:mode:)` method.

## See Also

### Getting built-in schedules

`static var animation: AnimationTimelineSchedule`

A pausable schedule of dates updating at a frequency no more quickly than the
provided interval.

Available when `Self` is `AnimationTimelineSchedule`.

`static func animation(minimumInterval: Double?, paused: Bool) ->
AnimationTimelineSchedule`

A pausable schedule of dates updating at a frequency no more quickly than the
provided interval.

Available when `Self` is `AnimationTimelineSchedule`.

`static var everyMinute: EveryMinuteTimelineSchedule`

A schedule for updating a timeline view at the start of every minute.

Available when `Self` is `EveryMinuteTimelineSchedule`.

`static func explicit<S>(S) -> ExplicitTimelineSchedule<S>`

A schedule for updating a timeline view at explicit points in time.

Instance Method

# entries(from:mode:)

Provides a sequence of dates starting around a given date.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func entries(
        from startDate: Date,
        mode: Self.Mode
    ) -> Self.Entries

**Required**

##  Parameters

`startDate`

    

The date by which the sequence begins.

`mode`

    

An indication of whether the schedule updates normally, or with some other
cadence.

## Return Value

A sequence of dates in ascending order.

## Discussion

A `TimelineView` that you create calls this method to figure out when to
update its content. The method returns a sequence of dates in increasing order
that represent points in time when the timeline view should update. Types that
conform to the `TimelineSchedule` protocol, like the one returned by
`periodic(from:by:)`, or a custom schedule that you define, implement a custom
version of this method to implement a particular kind of schedule.

One or more dates in the sequence might be before the given `startDate`, in
which case the timeline view performs its first update at `startDate` using
the entry that most closely precedes that date. For example, if in response to
a `startDate` of `10:09:55`, the method returns a sequence with the values
`10:09:00`, `10:10:00`, `10:11:00`, and so on, the timeline view performs an
initial update at `10:09:55` (using the `10:09:00` entry), followed by another
update at the beginning of every minute, starting at `10:10:00`.

A type that conforms should adjust its behavior based on the `mode` when
possible. For example, a periodic schedule providing updates for a timer could
restrict updates to once per minute while in the
`TimelineScheduleMode.lowFrequency` mode:

## See Also

### Getting a sequence of dates

`associatedtype Entries : Sequence`

The sequence of dates within a schedule.

**Required**

Associated Type

# Entries

The sequence of dates within a schedule.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    associatedtype Entries : Sequence where Self.Entries.Element == Date

**Required**

## Discussion

The `entries(from:mode:)` method returns a value of this type, which is a
`Sequence` of dates in ascending order. A `TimelineView` that you create with
a schedule updates its content at the moments in time corresponding to the
dates included in the sequence.

## See Also

### Getting a sequence of dates

`func entries(from: Date, mode: Self.Mode) -> Self.Entries`

Provides a sequence of dates starting around a given date.

**Required**

Type Alias

# TimelineSchedule.Mode

An alias for the timeline schedule update mode.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    typealias Mode = TimelineScheduleMode

## See Also

### Specifying a mode

`enum TimelineScheduleMode`

A mode of operation for timeline schedule updates.

Enumeration

# TimelineScheduleMode

A mode of operation for timeline schedule updates.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    enum TimelineScheduleMode

## Overview

A `TimelineView` provides a mode when calling its schedule’s
`entries(from:mode:)` method. The view chooses a mode based on the state of
the system. For example, a watchOS view might request a lower frequency of
updates, using the `TimelineScheduleMode.lowFrequency` mode, when the user
lowers their wrist.

## Topics

### Getting timeline schedule modes

`case normal`

A mode that produces schedule updates at the schedule’s natural cadence.

`case lowFrequency`

A mode that produces schedule updates at a reduced rate.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Specifying a mode

`typealias Mode`

An alias for the timeline schedule update mode.

Structure

# AnimationTimelineSchedule

A pausable schedule of dates updating at a frequency no more quickly than the
provided interval.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    struct AnimationTimelineSchedule

## Overview

You can also use `animation(minimumInterval:paused:)` to construct this
schedule.

## Topics

### Creating a schedule

`init(minimumInterval: Double?, paused: Bool)`

Create a pausable schedule of dates updating at a frequency no more quickly
than the provided interval.

### Getting the sequence of dates

`func entries(from: Date, mode: TimelineScheduleMode) ->
AnimationTimelineSchedule.Entries`

Returns entries at the frequency of the animation schedule.

## Relationships

### Conforms To

  * `Sendable`
  * `TimelineSchedule`

## See Also

### Supporting types

`struct EveryMinuteTimelineSchedule`

A schedule for updating a timeline view at the start of every minute.

`struct ExplicitTimelineSchedule`

A schedule for updating a timeline view at explicit points in time.

`struct PeriodicTimelineSchedule`

A schedule for updating a timeline view at regular intervals.

Structure

# EveryMinuteTimelineSchedule

A schedule for updating a timeline view at the start of every minute.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    struct EveryMinuteTimelineSchedule

## Overview

You can also use `everyMinute` to construct this schedule.

## Topics

### Creating a schedule

`init()`

Creates a per-minute update schedule.

### Getting the sequence of dates

`func entries(from: Date, mode: TimelineScheduleMode) ->
EveryMinuteTimelineSchedule.Entries`

Provides a sequence of per-minute dates starting from a given date.

`struct Entries`

The sequence of dates in an every minute schedule.

## Relationships

### Conforms To

  * `Sendable`
  * `TimelineSchedule`

## See Also

### Supporting types

`struct AnimationTimelineSchedule`

A pausable schedule of dates updating at a frequency no more quickly than the
provided interval.

`struct ExplicitTimelineSchedule`

A schedule for updating a timeline view at explicit points in time.

`struct PeriodicTimelineSchedule`

A schedule for updating a timeline view at regular intervals.

Structure

# ExplicitTimelineSchedule

A schedule for updating a timeline view at explicit points in time.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    struct ExplicitTimelineSchedule<Entries> where Entries : Sequence, Entries.Element == Date

## Overview

You can also use `explicit(_:)` to construct this schedule.

## Topics

### Creating a schedule

`init(Entries)`

Creates a schedule composed of an explicit sequence of dates.

### Getting the sequence of dates

`func entries(from: Date, mode: TimelineScheduleMode) -> Entries`

Provides the sequence of dates with which you initialized the schedule.

## Relationships

### Conforms To

  * `TimelineSchedule`

## See Also

### Supporting types

`struct AnimationTimelineSchedule`

A pausable schedule of dates updating at a frequency no more quickly than the
provided interval.

`struct EveryMinuteTimelineSchedule`

A schedule for updating a timeline view at the start of every minute.

`struct PeriodicTimelineSchedule`

A schedule for updating a timeline view at regular intervals.

Structure

# PeriodicTimelineSchedule

A schedule for updating a timeline view at regular intervals.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    struct PeriodicTimelineSchedule

## Overview

You can also use `periodic(from:by:)` to construct this schedule.

## Topics

### Creating a schedule

`init(from: Date, by: TimeInterval)`

Creates a periodic update schedule.

### Getting the sequence of dates

`func entries(from: Date, mode: TimelineScheduleMode) ->
PeriodicTimelineSchedule.Entries`

Provides a sequence of periodic dates starting from around a given date.

`struct Entries`

The sequence of dates in periodic schedule.

## Relationships

### Conforms To

  * `Sendable`
  * `TimelineSchedule`

## See Also

### Supporting types

`struct AnimationTimelineSchedule`

A pausable schedule of dates updating at a frequency no more quickly than the
provided interval.

`struct EveryMinuteTimelineSchedule`

A schedule for updating a timeline view at the start of every minute.

`struct ExplicitTimelineSchedule`

A schedule for updating a timeline view at explicit points in time.

