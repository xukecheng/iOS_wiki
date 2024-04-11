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

