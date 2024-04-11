Case

# TransitionPhase.identity

The transition is being applied to a view that is in the view hierarchy.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    case identity

## Discussion

In this phase, a transition should show its steady state appearance, which
will generally not make any visual change to the view.

## See Also

### Getting the phase

`case willAppear`

The transition is being applied to a view that is about to be inserted into
the view hierarchy.

`case didDisappear`

The transition is being applied to a view that has been requested to be
removed from the view hierarchy.

Case

# TransitionPhase.willAppear

The transition is being applied to a view that is about to be inserted into
the view hierarchy.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    case willAppear

## Discussion

In this phase, a transition should show the appearance that will be animated
from to make the appearance transition.

## See Also

### Getting the phase

`case identity`

The transition is being applied to a view that is in the view hierarchy.

`case didDisappear`

The transition is being applied to a view that has been requested to be
removed from the view hierarchy.

Case

# TransitionPhase.didDisappear

The transition is being applied to a view that has been requested to be
removed from the view hierarchy.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    case didDisappear

## Discussion

In this phase, a transition should show the appearance that will be animated
to to make the disappearance transition.

## See Also

### Getting the phase

`case identity`

The transition is being applied to a view that is in the view hierarchy.

`case willAppear`

The transition is being applied to a view that is about to be inserted into
the view hierarchy.

Instance Property

# isIdentity

A Boolean that indicates whether the transition should have an identity
effect, i.e. not change the appearance of its view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var isIdentity: Bool { get }

## Discussion

This is true in the `identity` phase.

## See Also

### Getting phase characteristics

`var value: Double`

A value that can be used to multiply effects that are applied differently
depending on the phase.

Instance Property

# value

A value that can be used to multiply effects that are applied differently
depending on the phase.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var value: Double { get }

## Return Value

Zero when in the `identity` case, -1.0 for `willAppear`, and 1.0 for
`didDisappear`.

## See Also

### Getting phase characteristics

`var isIdentity: Bool`

A Boolean that indicates whether the transition should have an identity
effect, i.e. not change the appearance of its view.

