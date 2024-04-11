Type Property

# identity

Creates a new configuration that does not change the appearance of the view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static let identity: ScrollTransitionConfiguration

## See Also

### Getting the configuration

`static let animated: ScrollTransitionConfiguration`

Creates a new configuration that discretely animates the transition when the
view becomes visible.

`static func animated(Animation) -> ScrollTransitionConfiguration`

Creates a new configuration that discretely animates the transition when the
view becomes visible.

`static let interactive: ScrollTransitionConfiguration`

Creates a new configuration that interactively interpolates the transition’s
effect as the view is scrolled into the visible region of the container.

`static func interactive(timingCurve: UnitCurve) ->
ScrollTransitionConfiguration`

Creates a new configuration that interactively interpolates the transition’s
effect as the view is scrolled into the visible region of the container.

Type Property

# animated

Creates a new configuration that discretely animates the transition when the
view becomes visible.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static let animated: ScrollTransitionConfiguration

## See Also

### Getting the configuration

`static let identity: ScrollTransitionConfiguration`

Creates a new configuration that does not change the appearance of the view.

`static func animated(Animation) -> ScrollTransitionConfiguration`

Creates a new configuration that discretely animates the transition when the
view becomes visible.

`static let interactive: ScrollTransitionConfiguration`

Creates a new configuration that interactively interpolates the transition’s
effect as the view is scrolled into the visible region of the container.

`static func interactive(timingCurve: UnitCurve) ->
ScrollTransitionConfiguration`

Creates a new configuration that interactively interpolates the transition’s
effect as the view is scrolled into the visible region of the container.

Type Method

# animated(_:)

Creates a new configuration that discretely animates the transition when the
view becomes visible.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static func animated(_ animation: Animation = .default) -> ScrollTransitionConfiguration

##  Parameters

`animation`

    

The animation to use when transitioning between states.

## Return Value

A configuration that discretely animates between transition phases.

## Discussion

Unlike the interactive configuration, the transition isn’t interpolated as the
scroll view is scrolled. Instead, the transition phase only changes once the
threshold has been reached, at which time the given animation is used to
animate to the new phase.

## See Also

### Getting the configuration

`static let identity: ScrollTransitionConfiguration`

Creates a new configuration that does not change the appearance of the view.

`static let animated: ScrollTransitionConfiguration`

Creates a new configuration that discretely animates the transition when the
view becomes visible.

`static let interactive: ScrollTransitionConfiguration`

Creates a new configuration that interactively interpolates the transition’s
effect as the view is scrolled into the visible region of the container.

`static func interactive(timingCurve: UnitCurve) ->
ScrollTransitionConfiguration`

Creates a new configuration that interactively interpolates the transition’s
effect as the view is scrolled into the visible region of the container.

Type Property

# interactive

Creates a new configuration that interactively interpolates the transition’s
effect as the view is scrolled into the visible region of the container.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static let interactive: ScrollTransitionConfiguration

## See Also

### Getting the configuration

`static let identity: ScrollTransitionConfiguration`

Creates a new configuration that does not change the appearance of the view.

`static let animated: ScrollTransitionConfiguration`

Creates a new configuration that discretely animates the transition when the
view becomes visible.

`static func animated(Animation) -> ScrollTransitionConfiguration`

Creates a new configuration that discretely animates the transition when the
view becomes visible.

`static func interactive(timingCurve: UnitCurve) ->
ScrollTransitionConfiguration`

Creates a new configuration that interactively interpolates the transition’s
effect as the view is scrolled into the visible region of the container.

Type Method

# interactive(timingCurve:)

Creates a new configuration that interactively interpolates the transition’s
effect as the view is scrolled into the visible region of the container.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static func interactive(timingCurve: UnitCurve = .easeInOut) -> ScrollTransitionConfiguration

##  Parameters

`timingCurve`

    

The curve that adjusts the pace at which the effect is interpolated between
phases of the transition. For example, an `.easeIn` curve causes interpolation
to begin slowly as the view reaches the edge of the scroll view, then speed up
as it reaches the visible threshold. The curve is applied ‘forward’ while the
view is appearing, meaning that time zero corresponds to the view being just
hidden, and time 1.0 corresponds to the pont at which the view reaches the
configuration threshold. This also means that the timing curve is applied in
reversed while the view is moving away from the center of the scroll view.

## Return Value

A configuration that interactively interpolates between transition phases
based on the current scroll position.

## See Also

### Getting the configuration

`static let identity: ScrollTransitionConfiguration`

Creates a new configuration that does not change the appearance of the view.

`static let animated: ScrollTransitionConfiguration`

Creates a new configuration that discretely animates the transition when the
view becomes visible.

`static func animated(Animation) -> ScrollTransitionConfiguration`

Creates a new configuration that discretely animates the transition when the
view becomes visible.

`static let interactive: ScrollTransitionConfiguration`

Creates a new configuration that interactively interpolates the transition’s
effect as the view is scrolled into the visible region of the container.

Instance Method

# animation(_:)

Sets the animation with which the transition will be applied.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func animation(_ animation: Animation) -> ScrollTransitionConfiguration

##  Parameters

`animation`

    

An animation that will be used to apply the transition to the view.

## Return Value

A copy of this configuration with the animation set to the given value.

## Discussion

If the transition is interactive, the given animation will be used to animate
the effect toward the current interpolated value, causing the effect to lag
behind the current scroll position.

## See Also

### Accessing the configuration

`func threshold(ScrollTransitionConfiguration.Threshold) ->
ScrollTransitionConfiguration`

Sets the threshold at which the view will be considered fully visible.

`struct Threshold`

Describes a specific point in the progression of a target view within a
container from hidden (fully outside the container) to visible.

Instance Method

# threshold(_:)

Sets the threshold at which the view will be considered fully visible.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func threshold(_ threshold: ScrollTransitionConfiguration.Threshold) -> ScrollTransitionConfiguration

##  Parameters

`threshold`

    

The threshold specifying how much of the view must intersect with the
container before it is treated as visible.

## Return Value

A copy of this configuration with the threshold set to the given value.

## See Also

### Accessing the configuration

`func animation(Animation) -> ScrollTransitionConfiguration`

Sets the animation with which the transition will be applied.

`struct Threshold`

Describes a specific point in the progression of a target view within a
container from hidden (fully outside the container) to visible.

Structure

# ScrollTransitionConfiguration.Threshold

Describes a specific point in the progression of a target view within a
container from hidden (fully outside the container) to visible.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct Threshold

## Topics

### Getting the threshold

`static var centered: ScrollTransitionConfiguration.Threshold`

The target view is centered within the container

`static let hidden: ScrollTransitionConfiguration.Threshold`

`static let visible: ScrollTransitionConfiguration.Threshold`

`static func visible(Double) -> ScrollTransitionConfiguration.Threshold`

The target view is visible by the given amount, where zero is fully hidden,
and one is fully visible.

### Modifying the threshold

`func inset(by: Double) -> ScrollTransitionConfiguration.Threshold`

Returns a threshold that is met when the target view is closer to the center
of the container by `distance`. Use negative values to move the threshold away
from the center.

`func interpolated(towards: ScrollTransitionConfiguration.Threshold, amount:
Double) -> ScrollTransitionConfiguration.Threshold`

Creates a new threshold that combines this threshold value with another
threshold, interpolated by the given amount.

## See Also

### Accessing the configuration

`func animation(Animation) -> ScrollTransitionConfiguration`

Sets the animation with which the transition will be applied.

`func threshold(ScrollTransitionConfiguration.Threshold) ->
ScrollTransitionConfiguration`

Sets the threshold at which the view will be considered fully visible.

