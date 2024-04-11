Initializer

# init(_:content:)

Creates a new timeline view that uses the given schedule.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init(
        _ schedule: Schedule,
        @ViewBuilder content: @escaping (TimelineViewDefaultContext) -> Content
    )

Available when `Schedule` conforms to `TimelineSchedule` and `Content`
conforms to `View`.

##  Parameters

`schedule`

    

A schedule that produces a sequence of dates that indicate the instances when
the view should update. Use a type that conforms to `TimelineSchedule`, like
`everyMinute`, or a custom timeline schedule that you define.

`content`

    

A closure that generates view content at the moments indicated by the
schedule. The closure takes an input of type `TimelineViewDefaultContext` that
includes the date from the schedule that prompted the update, as well as a
`TimelineView.Context.Cadence` value that the view can use to customize its
appearance.

## See Also

### Creating a timeline

`struct Context`

Information passed to a timeline view’s content callback.

Structure

# TimelineView.Context

Information passed to a timeline view’s content callback.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    struct Context

## Overview

The context includes both the `date` from the schedule that triggered the
callback, and a `cadence` that you can use to customize the appearance of your
view. For example, you might choose to display the second hand of an analog
clock only when the cadence is `TimelineView.Context.Cadence.seconds` or
faster.

## Topics

### Getting the date

`let date: Date`

The date from the schedule that triggered the current view update.

### Getting the cadence

`let cadence: TimelineView<Schedule, Content>.Context.Cadence`

The rate at which the timeline updates the view.

`enum Cadence`

A rate at which timeline views can receive updates.

### Invalidating the context

`func invalidateTimelineContent()`

Resets any pre-rendered views the system has from the timeline.

Available when `Schedule` conforms to `TimelineSchedule`.

## See Also

### Creating a timeline

`init(Schedule, content: (TimelineViewDefaultContext) -> Content)`

Creates a new timeline view that uses the given schedule.

Available when `Schedule` conforms to `TimelineSchedule` and `Content`
conforms to `View`.

Initializer

# init(_:content:)

Creates a new timeline view that uses the given schedule.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init(
        _ schedule: Schedule,
        @ViewBuilder content: @escaping (TimelineView<Schedule, Content>.Context) -> Content
    )

Available when `Schedule` conforms to `TimelineSchedule` and `Content`
conforms to `View`.

Deprecated

Use `init(_:content:)` instead. The replacement initializer’s `context`
closure takes a `TimelineViewDefaultContext` as its input rather than a
`TimelineView.Context` to prevent introducing an unnecessary generic parameter
dependency on the context type.

##  Parameters

`schedule`

    

A schedule that produces a sequence of dates that indicate the instances when
the view should update. Use a type that conforms to `TimelineSchedule`, like
`everyMinute`, or a custom timeline schedule that you define.

`content`

    

A closure that generates view content at the moments indicated by the
schedule. The closure takes an input of type `TimelineView.Context` that
includes the date from the schedule that prompted the update, as well as a
`TimelineView.Context.Cadence` value that the view can use to customize its
appearance.

