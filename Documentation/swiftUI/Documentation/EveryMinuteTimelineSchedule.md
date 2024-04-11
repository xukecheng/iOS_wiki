Initializer

# init()

Creates a per-minute update schedule.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init()

## Discussion

Use the `entries(from:mode:)` method to get the sequence of dates.

Instance Method

# entries(from:mode:)

Provides a sequence of per-minute dates starting from a given date.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func entries(
        from startDate: Date,
        mode: TimelineScheduleMode
    ) -> EveryMinuteTimelineSchedule.Entries

##  Parameters

`startDate`

    

The date from which the sequence begins.

`mode`

    

The mode for the update schedule.

## Return Value

A sequence of per-minute dates in ascending order.

## Discussion

A `TimelineView` that you create with an every minute schedule calls this
method to ask the schedule when to update its content. The method returns a
sequence of per-minute dates in increasing order, from earliest to latest,
that represents when the timeline view updates.

For a `startDate` that’s exactly minute-aligned, the schedule’s sequence of
dates starts at that time. Otherwise, it starts at the beginning of the
specified minute. For example, for start dates of both `10:09:32` and
`10:09:00`, the first entry in the sequence is `10:09:00`.

## See Also

### Getting the sequence of dates

`struct Entries`

The sequence of dates in an every minute schedule.

Structure

# EveryMinuteTimelineSchedule.Entries

The sequence of dates in an every minute schedule.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    struct Entries

## Overview

The `entries(from:mode:)` method returns a value of this type, which is a
`Sequence` of dates, one per minute, in ascending order. A `TimelineView` that
you create updates its content at the moments in time corresponding to the
dates included in the sequence.

## Relationships

### Conforms To

  * `IteratorProtocol`
  * `Sendable`
  * `Sequence`

## See Also

### Getting the sequence of dates

`func entries(from: Date, mode: TimelineScheduleMode) ->
EveryMinuteTimelineSchedule.Entries`

Provides a sequence of per-minute dates starting from a given date.

