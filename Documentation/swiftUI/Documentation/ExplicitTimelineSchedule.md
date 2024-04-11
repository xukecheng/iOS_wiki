Initializer

# init(_:)

Creates a schedule composed of an explicit sequence of dates.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init(_ dates: Entries)

##  Parameters

`dates`

    

The sequence of dates at which a timeline view updates. Use a monotonically
increasing sequence of dates, and ensure that at least one is in the future.

## Discussion

Use the `entries(from:mode:)` method to get the sequence of dates.

Instance Method

# entries(from:mode:)

Provides the sequence of dates with which you initialized the schedule.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func entries(
        from startDate: Date,
        mode: TimelineScheduleMode
    ) -> Entries

##  Parameters

`startDate`

    

The date from which the sequence begins. This particular implementation of the
protocol method ignores the start date.

`mode`

    

The mode for the update schedule. This particular implementation of the
protocol method ignores the mode.

## Return Value

The sequence of dates that you provided at initialization.

## Discussion

A `TimelineView` that you create with a schedule calls this `TimelineSchedule`
method to ask the schedule when to update its content. The explicit timeline
schedule implementation of this method returns the unmodified sequence of
dates that you provided when you created the schedule with `explicit(_:)`. As
a result, this particular implementation ignores the `startDate` and `mode`
parameters.

