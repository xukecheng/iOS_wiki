Initializer

# init(minimumInterval:paused:)

Create a pausable schedule of dates updating at a frequency no more quickly
than the provided interval.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init(
        minimumInterval: Double? = nil,
        paused: Bool = false
    )

##  Parameters

`minimumInterval`

    

The minimum interval to update the schedule at. Pass nil to let the system
pick an appropriate update interval.

`paused`

    

If the schedule should stop generating updates.

Instance Method

# entries(from:mode:)

Returns entries at the frequency of the animation schedule.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func entries(
        from start: Date,
        mode: TimelineScheduleMode
    ) -> AnimationTimelineSchedule.Entries

## Discussion

When in `.lowFrequency` mode, return no entries, effectively pausing the
animation.

