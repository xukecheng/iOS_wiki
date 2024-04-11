Initializer

# init()

Creates a transaction.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init()

## See Also

### Creating a transaction

`init(animation: Animation?)`

Creates a transaction and assigns its animation property.

Initializer

# init(animation:)

Creates a transaction and assigns its animation property.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(animation: Animation?)

##  Parameters

`animation`

    

The animation to perform when the current state changes.

## See Also

### Creating a transaction

`init()`

Creates a transaction.

Instance Property

# animation

The animation, if any, associated with the current state change.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var animation: Animation? { get set }

## See Also

### Managing animations

`var disablesAnimations: Bool`

A Boolean value that indicates whether views should disable animations.

`func addAnimationCompletion(criteria: AnimationCompletionCriteria, () ->
Void)`

Adds a completion to run when the animations created with this transaction are
all complete.

Instance Property

# disablesAnimations

A Boolean value that indicates whether views should disable animations.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var disablesAnimations: Bool { get set }

## Discussion

This value is `true` during the initial phase of a two-part transition update,
to prevent `View/animation(_:)` from inserting new animations into the
transaction.

## See Also

### Managing animations

`var animation: Animation?`

The animation, if any, associated with the current state change.

`func addAnimationCompletion(criteria: AnimationCompletionCriteria, () ->
Void)`

Adds a completion to run when the animations created with this transaction are
all complete.

Instance Method

# addAnimationCompletion(criteria:_:)

Adds a completion to run when the animations created with this transaction are
all complete.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    mutating func addAnimationCompletion(
        criteria: AnimationCompletionCriteria = .logicallyComplete,
        _ completion: @escaping () -> Void
    )

## Discussion

The completion callback will always be fired exactly one time. If no
animations are created by the changes in `body`, then the callback will be
called immediately after `body`.

## See Also

### Managing animations

`var animation: Animation?`

The animation, if any, associated with the current state change.

`var disablesAnimations: Bool`

A Boolean value that indicates whether views should disable animations.

Instance Property

# dismissBehavior

The behavior for how windows will dismiss programmatically when used in
conjunction with `DismissWindowAction`.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    var dismissBehavior: DismissBehavior { get set }

## Discussion

The default value is `.interactive`.

You can use this property to dismiss windows which may be showing a modal
presentation by using the `.destructive` value:

Instance Property

# isContinuous

A Boolean value that indicates whether the transaction originated from an
action that produces a sequence of values.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var isContinuous: Bool { get set }

## Discussion

This value is `true` if a continuous action created the transaction, and is
`false` otherwise. Continuous actions include things like dragging a slider or
pressing and holding a stepper, as opposed to tapping a button.

## See Also

### Getting information about a transaction

`var scrollTargetAnchor: UnitPoint?`

The preferred alignment of the view within a scroll view’s visible region when
scrolling to a view.

`var tracksVelocity: Bool`

Whether this transaction will track the velocity of any animatable properties
that change.

`subscript<K>(K.Type) -> K.Value`

Accesses the transaction value associated with a custom key.

Instance Property

# scrollTargetAnchor

The preferred alignment of the view within a scroll view’s visible region when
scrolling to a view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var scrollTargetAnchor: UnitPoint? { get set }

## Discussion

Use this API in conjunction with a `ScrollViewProxy/scrollTo(_:anchor)` or
when updating the binding provided to a `scrollPosition(id:anchor:)`.

When used with the `scrollPosition(id:anchor:)` modifier, this value will be
preferred over the anchor specified in the modifier for the current
transaction.

## See Also

### Getting information about a transaction

`var isContinuous: Bool`

A Boolean value that indicates whether the transaction originated from an
action that produces a sequence of values.

`var tracksVelocity: Bool`

Whether this transaction will track the velocity of any animatable properties
that change.

`subscript<K>(K.Type) -> K.Value`

Accesses the transaction value associated with a custom key.

Instance Property

# tracksVelocity

Whether this transaction will track the velocity of any animatable properties
that change.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var tracksVelocity: Bool { get set }

## Discussion

This property can be enabled in an interactive context to track velocity
during a user interaction so that when the interaction ends, an animation can
use the accumulated velocities to create animations that preserve them. This
tracking is mutually exclusive with an animation being used during a view
change, since if there is an animation, it is responsible for managing its own
velocity.

Gesture onChanged and updating callbacks automatically set this property to
true.

This example shows an interaction which applies changes, tracking velocity
until the final change, which applies an animation (which will start with the
velocity that was tracked during the previous changes). These changes could
come from a server or from an interactive control like a slider.

## See Also

### Getting information about a transaction

`var isContinuous: Bool`

A Boolean value that indicates whether the transaction originated from an
action that produces a sequence of values.

`var scrollTargetAnchor: UnitPoint?`

The preferred alignment of the view within a scroll view’s visible region when
scrolling to a view.

`subscript<K>(K.Type) -> K.Value`

Accesses the transaction value associated with a custom key.

Instance Subscript

# subscript(_:)

Accesses the transaction value associated with a custom key.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    subscript<K>(key: K.Type) -> K.Value where K : TransactionKey { get set }

## Overview

Create custom transaction values by defining a key that conforms to the
`TransactionKey` protocol, and then using that key with the subscript operator
of the `Transaction` structure to get and set a value for that key:

## See Also

### Getting information about a transaction

`var isContinuous: Bool`

A Boolean value that indicates whether the transaction originated from an
action that produces a sequence of values.

`var scrollTargetAnchor: UnitPoint?`

The preferred alignment of the view within a scroll view’s visible region when
scrolling to a view.

`var tracksVelocity: Bool`

Whether this transaction will track the velocity of any animatable properties
that change.

