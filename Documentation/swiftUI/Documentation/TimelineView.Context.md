Instance Property

# date

The date from the schedule that triggered the current view update.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    let date: Date

## Discussion

The first time a `TimelineView` closure receives this date, it might be in the
past. For example, if you create an `everyMinute` schedule at `10:09:55`, the
schedule creates entries `10:09:00`, `10:10:00`, `10:11:00`, and so on. In
response, the timeline view performs an initial update immediately, at
`10:09:55`, but the context contains the `10:09:00` date entry. Subsequent
entries arrive at their corresponding times.

Instance Property

# cadence

The rate at which the timeline updates the view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    let cadence: TimelineView<Schedule, Content>.Context.Cadence

## Discussion

Use this value to hide information that updates faster than the view’s current
update rate. For example, you could hide the millisecond component of a
digital timer when the cadence is anything slower than
`TimelineView.Context.Cadence.live`.

Because the `TimelineView.Context.Cadence` enumeration conforms to the
`Comparable` protocol, you can compare cadences with relational operators.
Slower cadences have higher values, so you could perform the check described
above with the following comparison:

## See Also

### Getting the cadence

`enum Cadence`

A rate at which timeline views can receive updates.

Enumeration

# TimelineView.Context.Cadence

A rate at which timeline views can receive updates.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    enum Cadence

## Overview

Use the cadence presented to content in a `TimelineView` to hide information
that updates faster than the view’s current update rate. For example, you
could hide the millisecond component of a digital timer when the cadence is
`TimelineView.Context.Cadence.seconds` or
`TimelineView.Context.Cadence.minutes`.

Because this enumeration conforms to the `Comparable` protocol, you can
compare cadences with relational operators. Slower cadences have higher
values, so you could perform the check described above with the following
comparison:

## Topics

### Getting cadences

`case live`

Updates the view continuously.

`case seconds`

Updates the view approximately once per second.

`case minutes`

Updates the view approximately once per minute.

## Relationships

### Conforms To

  * `Comparable`
  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Getting the cadence

`let cadence: TimelineView<Schedule, Content>.Context.Cadence`

The rate at which the timeline updates the view.

Instance Method

# invalidateTimelineContent()

Resets any pre-rendered views the system has from the timeline.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  watchOS 8.0+  visionOS 1.0+

    
    
    func invalidateTimelineContent()

Available when `Schedule` conforms to `TimelineSchedule`.

## Discussion

When entering Always On Display, the system might pre-render frames. If the
content of these frames must change in a way that isn’t reflected by the
schedule or the timeline view’s current bindings — for example, because the
user changes the title of a future calendar event — call this method to
request that the frames be regenerated.

