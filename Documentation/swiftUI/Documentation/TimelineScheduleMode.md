Case

# TimelineScheduleMode.normal

A mode that produces schedule updates at the schedule’s natural cadence.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    case normal

## See Also

### Getting timeline schedule modes

`case lowFrequency`

A mode that produces schedule updates at a reduced rate.

Case

# TimelineScheduleMode.lowFrequency

A mode that produces schedule updates at a reduced rate.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    case lowFrequency

## Discussion

In this mode, the schedule should generate only “major” updates, if possible.
For example, a timeline providing updates to a timer might restrict updates to
once a minute while in this mode.

## See Also

### Getting timeline schedule modes

`case normal`

A mode that produces schedule updates at the schedule’s natural cadence.

