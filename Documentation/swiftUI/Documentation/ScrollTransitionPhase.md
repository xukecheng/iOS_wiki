Case

# ScrollTransitionPhase.identity

The scroll transition is being applied to a view that is in the visible area.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    case identity

## Discussion

In this phase, a transition should show its steady state appearance, which
will generally not make any visual change to the view.

## See Also

### Getting the phase

`case topLeading`

The scroll transition is being applied to a view that is about to move into
the visible area at the top edge of a vertical scroll view, or the leading
edge of a horizont scroll view.

`case bottomTrailing`

The scroll transition is being applied to a view that is about to move into
the visible area at the bottom edge of a vertical scroll view, or the trailing
edge of a horizontal scroll view.

Case

# ScrollTransitionPhase.topLeading

The scroll transition is being applied to a view that is about to move into
the visible area at the top edge of a vertical scroll view, or the leading
edge of a horizont scroll view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    case topLeading

## See Also

### Getting the phase

`case identity`

The scroll transition is being applied to a view that is in the visible area.

`case bottomTrailing`

The scroll transition is being applied to a view that is about to move into
the visible area at the bottom edge of a vertical scroll view, or the trailing
edge of a horizontal scroll view.

Case

# ScrollTransitionPhase.bottomTrailing

The scroll transition is being applied to a view that is about to move into
the visible area at the bottom edge of a vertical scroll view, or the trailing
edge of a horizontal scroll view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    case bottomTrailing

## See Also

### Getting the phase

`case identity`

The scroll transition is being applied to a view that is in the visible area.

`case topLeading`

The scroll transition is being applied to a view that is about to move into
the visible area at the top edge of a vertical scroll view, or the leading
edge of a horizont scroll view.

Instance Property

# isIdentity

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var isIdentity: Bool { get }

## See Also

### Accessing the phase state

`var value: Double`

A phase-derived value that can be used to scale or otherwise modify effects.

Instance Property

# value

A phase-derived value that can be used to scale or otherwise modify effects.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var value: Double { get }

## Discussion

Returns -1.0 when in the topLeading phase, zero when in the identity phase,
and 1.0 when in the bottomTrailing phase.

## See Also

### Accessing the phase state

`var isIdentity: Bool`

