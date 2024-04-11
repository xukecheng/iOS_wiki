Type Property

# start

Indicates that an activity started.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+

    
    
    static let start: SensoryFeedback

## Discussion

Use this haptic when starting a timer or any other activity that can be
explicitly started and stopped.

Only plays feedback on watchOS.

## See Also

### Indicating start and stop

`static let stop: SensoryFeedback`

Indicates that an activity stopped.

Type Property

# stop

Indicates that an activity stopped.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+

    
    
    static let stop: SensoryFeedback

## Discussion

Use this haptic when stopping a timer or other activity that was previously
started.

Only plays feedback on watchOS.

## See Also

### Indicating start and stop

`static let start: SensoryFeedback`

Indicates that an activity started.

Type Property

# alignment

Indicates the alignment of a dragged item.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+

    
    
    static let alignment: SensoryFeedback

## Discussion

For example, use this pattern in a drawing app when the user drags a shape
into alignment with another shape.

Only plays feedback on macOS.

## See Also

### Indicating changes and selections

`static let decrease: SensoryFeedback`

Indicates that an important value decreased below a significant threshold.

`static let increase: SensoryFeedback`

Indicates that an important value increased above a significant threshold.

`static let levelChange: SensoryFeedback`

Indicates movement between discrete levels of pressure.

`static let selection: SensoryFeedback`

Indicates that a UI element’s values are changing.

Type Property

# decrease

Indicates that an important value decreased below a significant threshold.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+

    
    
    static let decrease: SensoryFeedback

## Discussion

Only plays feedback on watchOS.

## See Also

### Indicating changes and selections

`static let alignment: SensoryFeedback`

Indicates the alignment of a dragged item.

`static let increase: SensoryFeedback`

Indicates that an important value increased above a significant threshold.

`static let levelChange: SensoryFeedback`

Indicates movement between discrete levels of pressure.

`static let selection: SensoryFeedback`

Indicates that a UI element’s values are changing.

Type Property

# increase

Indicates that an important value increased above a significant threshold.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+

    
    
    static let increase: SensoryFeedback

## Discussion

Only plays feedback on watchOS.

## See Also

### Indicating changes and selections

`static let alignment: SensoryFeedback`

Indicates the alignment of a dragged item.

`static let decrease: SensoryFeedback`

Indicates that an important value decreased below a significant threshold.

`static let levelChange: SensoryFeedback`

Indicates movement between discrete levels of pressure.

`static let selection: SensoryFeedback`

Indicates that a UI element’s values are changing.

Type Property

# levelChange

Indicates movement between discrete levels of pressure.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+

    
    
    static let levelChange: SensoryFeedback

## Discussion

For example, as the user presses a fast-forward button on a video player,
playback could increase or decrease and haptic feedback could be provided as
different levels of pressure are reached.

Only plays feedback on macOS.

## See Also

### Indicating changes and selections

`static let alignment: SensoryFeedback`

Indicates the alignment of a dragged item.

`static let decrease: SensoryFeedback`

Indicates that an important value decreased below a significant threshold.

`static let increase: SensoryFeedback`

Indicates that an important value increased above a significant threshold.

`static let selection: SensoryFeedback`

Indicates that a UI element’s values are changing.

Type Property

# selection

Indicates that a UI element’s values are changing.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+

    
    
    static let selection: SensoryFeedback

## Discussion

Only plays feedback on iOS and watchOS.

## See Also

### Indicating changes and selections

`static let alignment: SensoryFeedback`

Indicates the alignment of a dragged item.

`static let decrease: SensoryFeedback`

Indicates that an important value decreased below a significant threshold.

`static let increase: SensoryFeedback`

Indicates that an important value increased above a significant threshold.

`static let levelChange: SensoryFeedback`

Indicates movement between discrete levels of pressure.

Type Property

# success

Indicates that a task or action has completed.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+

    
    
    static let success: SensoryFeedback

## Discussion

Only plays feedback on iOS and watchOS.

## See Also

### Indicating the outcome of an operation

`static let warning: SensoryFeedback`

Indicates that a task or action has produced a warning of some kind.

`static let error: SensoryFeedback`

Indicates that an error has occurred.

Type Property

# warning

Indicates that a task or action has produced a warning of some kind.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+

    
    
    static let warning: SensoryFeedback

## Discussion

Only plays feedback on iOS and watchOS.

## See Also

### Indicating the outcome of an operation

`static let success: SensoryFeedback`

Indicates that a task or action has completed.

`static let error: SensoryFeedback`

Indicates that an error has occurred.

Type Property

# error

Indicates that an error has occurred.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+

    
    
    static let error: SensoryFeedback

## Discussion

Only plays feedback on iOS and watchOS.

## See Also

### Indicating the outcome of an operation

`static let success: SensoryFeedback`

Indicates that a task or action has completed.

`static let warning: SensoryFeedback`

Indicates that a task or action has produced a warning of some kind.

Type Property

# impact

Provides a physical metaphor you can use to complement a visual experience.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+

    
    
    static let impact: SensoryFeedback

## Discussion

Use this to provide feedback for UI elements colliding. It should supplement
the user experience, since only some platforms will play feedback in response
to it.

Only plays feedback on iOS and watchOS.

## See Also

### Producing a physical impact

`static func impact(weight: SensoryFeedback.Weight, intensity: Double) ->
SensoryFeedback`

Provides a physical metaphor you can use to complement a visual experience.

`static func impact(flexibility: SensoryFeedback.Flexibility, intensity:
Double) -> SensoryFeedback`

Provides a physical metaphor you can use to complement a visual experience.

`struct Flexibility`

The flexibility to be represented by a type of feedback.

`struct Weight`

The weight to be represented by a type of feedback.

Type Method

# impact(weight:intensity:)

Provides a physical metaphor you can use to complement a visual experience.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+

    
    
    static func impact(
        weight: SensoryFeedback.Weight = .medium,
        intensity: Double = 1.0
    ) -> SensoryFeedback

## Discussion

Use this to provide feedback for UI elements colliding. It should supplement
the user experience, since only some platforms will play feedback in response
to it.

Not all platforms will play different feedback for different weights and
intensities of impact.

Only plays feedback on iOS and watchOS.

## See Also

### Producing a physical impact

`static let impact: SensoryFeedback`

Provides a physical metaphor you can use to complement a visual experience.

`static func impact(flexibility: SensoryFeedback.Flexibility, intensity:
Double) -> SensoryFeedback`

Provides a physical metaphor you can use to complement a visual experience.

`struct Flexibility`

The flexibility to be represented by a type of feedback.

`struct Weight`

The weight to be represented by a type of feedback.

Type Method

# impact(flexibility:intensity:)

Provides a physical metaphor you can use to complement a visual experience.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+

    
    
    static func impact(
        flexibility: SensoryFeedback.Flexibility,
        intensity: Double = 1.0
    ) -> SensoryFeedback

## Discussion

Use this to provide feedback for UI elements colliding. It should supplement
the user experience, since only some platforms will play feedback in response
to it.

Not all platforms will play different feedback for different flexibilities and
intensities of impact.

Only plays feedback on iOS and watchOS.

## See Also

### Producing a physical impact

`static let impact: SensoryFeedback`

Provides a physical metaphor you can use to complement a visual experience.

`static func impact(weight: SensoryFeedback.Weight, intensity: Double) ->
SensoryFeedback`

Provides a physical metaphor you can use to complement a visual experience.

`struct Flexibility`

The flexibility to be represented by a type of feedback.

`struct Weight`

The weight to be represented by a type of feedback.

Structure

# SensoryFeedback.Flexibility

The flexibility to be represented by a type of feedback.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+

    
    
    struct Flexibility

## Overview

`Flexibility` values can be passed to
`SensoryFeedback.impact(flexibility:intensity:)`.

## Topics

### Getting flexibility values

`static let rigid: SensoryFeedback.Flexibility`

Indicates a collision between hard or inflexible UI objects.

`static let soft: SensoryFeedback.Flexibility`

Indicates a collision between soft or flexible UI objects.

`static let solid: SensoryFeedback.Flexibility`

Indicates a collision between solid UI objects of medium flexibility.

## Relationships

### Conforms To

  * `Equatable`
  * `Sendable`

## See Also

### Producing a physical impact

`static let impact: SensoryFeedback`

Provides a physical metaphor you can use to complement a visual experience.

`static func impact(weight: SensoryFeedback.Weight, intensity: Double) ->
SensoryFeedback`

Provides a physical metaphor you can use to complement a visual experience.

`static func impact(flexibility: SensoryFeedback.Flexibility, intensity:
Double) -> SensoryFeedback`

Provides a physical metaphor you can use to complement a visual experience.

`struct Weight`

The weight to be represented by a type of feedback.

Structure

# SensoryFeedback.Weight

The weight to be represented by a type of feedback.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+

    
    
    struct Weight

## Overview

`Weight` values can be passed to `SensoryFeedback.impact(weight:intensity:)`.

## Topics

### Getting flexibility values

`static let light: SensoryFeedback.Weight`

Indicates a collision between small or lightweight UI objects.

`static let medium: SensoryFeedback.Weight`

Indicates a collision between medium-sized or medium-weight UI objects.

`static let heavy: SensoryFeedback.Weight`

Indicates a collision between large or heavyweight UI objects.

## Relationships

### Conforms To

  * `Equatable`
  * `Sendable`

## See Also

### Producing a physical impact

`static let impact: SensoryFeedback`

Provides a physical metaphor you can use to complement a visual experience.

`static func impact(weight: SensoryFeedback.Weight, intensity: Double) ->
SensoryFeedback`

Provides a physical metaphor you can use to complement a visual experience.

`static func impact(flexibility: SensoryFeedback.Flexibility, intensity:
Double) -> SensoryFeedback`

Provides a physical metaphor you can use to complement a visual experience.

`struct Flexibility`

The flexibility to be represented by a type of feedback.

