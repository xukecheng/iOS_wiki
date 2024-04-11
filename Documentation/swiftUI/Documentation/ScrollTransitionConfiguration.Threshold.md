Type Property

# centered

The target view is centered within the container

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static var centered: ScrollTransitionConfiguration.Threshold { get }

## See Also

### Getting the threshold

`static let hidden: ScrollTransitionConfiguration.Threshold`

`static let visible: ScrollTransitionConfiguration.Threshold`

`static func visible(Double) -> ScrollTransitionConfiguration.Threshold`

The target view is visible by the given amount, where zero is fully hidden,
and one is fully visible.

Type Property

# hidden

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static let hidden: ScrollTransitionConfiguration.Threshold

## See Also

### Getting the threshold

`static var centered: ScrollTransitionConfiguration.Threshold`

The target view is centered within the container

`static let visible: ScrollTransitionConfiguration.Threshold`

`static func visible(Double) -> ScrollTransitionConfiguration.Threshold`

The target view is visible by the given amount, where zero is fully hidden,
and one is fully visible.

Type Property

# visible

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static let visible: ScrollTransitionConfiguration.Threshold

## See Also

### Getting the threshold

`static var centered: ScrollTransitionConfiguration.Threshold`

The target view is centered within the container

`static let hidden: ScrollTransitionConfiguration.Threshold`

`static func visible(Double) -> ScrollTransitionConfiguration.Threshold`

The target view is visible by the given amount, where zero is fully hidden,
and one is fully visible.

Type Method

# visible(_:)

The target view is visible by the given amount, where zero is fully hidden,
and one is fully visible.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static func visible(_ amount: Double) -> ScrollTransitionConfiguration.Threshold

## Discussion

Values less than zero or greater than one are clamped.

## See Also

### Getting the threshold

`static var centered: ScrollTransitionConfiguration.Threshold`

The target view is centered within the container

`static let hidden: ScrollTransitionConfiguration.Threshold`

`static let visible: ScrollTransitionConfiguration.Threshold`

Instance Method

# inset(by:)

Returns a threshold that is met when the target view is closer to the center
of the container by `distance`. Use negative values to move the threshold away
from the center.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func inset(by distance: Double) -> ScrollTransitionConfiguration.Threshold

## See Also

### Modifying the threshold

`func interpolated(towards: ScrollTransitionConfiguration.Threshold, amount:
Double) -> ScrollTransitionConfiguration.Threshold`

Creates a new threshold that combines this threshold value with another
threshold, interpolated by the given amount.

Instance Method

# interpolated(towards:amount:)

Creates a new threshold that combines this threshold value with another
threshold, interpolated by the given amount.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func interpolated(
        towards other: ScrollTransitionConfiguration.Threshold,
        amount: Double
    ) -> ScrollTransitionConfiguration.Threshold

##  Parameters

`other`

    

The second threshold value.

`amount`

    

The ratio with which this threshold is combined with the given threshold,
where zero is equal to this threshold, 1.0 is equal to `other`, and values in
between combine the two thresholds.

## See Also

### Modifying the threshold

`func inset(by: Double) -> ScrollTransitionConfiguration.Threshold`

Returns a threshold that is met when the target view is closer to the center
of the container by `distance`. Use negative values to move the threshold away
from the center.

