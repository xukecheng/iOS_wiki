Function

# withAnimation(_:_:)

Returns the result of recomputing the view’s body with the provided animation.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func withAnimation<Result>(
        _ animation: Animation? = .default,
        _ body: () throws -> Result
    ) rethrows -> Result

## Discussion

This function sets the given `Animation` as the `animation` property of the
thread’s current `Transaction`.

## See Also

### Adding state-based animation to an action

`func withAnimation<Result>(Animation?, completionCriteria:
AnimationCompletionCriteria, () throws -> Result, completion: () -> Void)
rethrows -> Result`

Returns the result of recomputing the view’s body with the provided animation,
and runs the completion when all animations are complete.

`struct AnimationCompletionCriteria`

The criteria that determines when an animation is considered finished.

`struct Animation`

The way a view changes over time to create a smooth visual transition from one
state to another.

Function

# withAnimation(_:completionCriteria:_:completion:)

Returns the result of recomputing the view’s body with the provided animation,
and runs the completion when all animations are complete.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func withAnimation<Result>(
        _ animation: Animation? = .default,
        completionCriteria: AnimationCompletionCriteria = .logicallyComplete,
        _ body: () throws -> Result,
        completion: @escaping () -> Void
    ) rethrows -> Result

## Discussion

This function sets the given `Animation` as the `animation` property of the
thread’s current `Transaction` as well as calling
`Transaction/addAnimationCompletion` with the specified completion.

The completion callback will always be fired exactly one time. If no
animations are created by the changes in `body`, then the callback will be
called immediately after `body`.

## See Also

### Adding state-based animation to an action

`func withAnimation<Result>(Animation?, () throws -> Result) rethrows ->
Result`

Returns the result of recomputing the view’s body with the provided animation.

`struct AnimationCompletionCriteria`

The criteria that determines when an animation is considered finished.

`struct Animation`

The way a view changes over time to create a smooth visual transition from one
state to another.

Structure

# AnimationCompletionCriteria

The criteria that determines when an animation is considered finished.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct AnimationCompletionCriteria

## Topics

### Getting the completion criteria

`static let logicallyComplete: AnimationCompletionCriteria`

The animation has logically completed, but may still be in its long tail.

`static let removed: AnimationCompletionCriteria`

The entire animation is finished and will now be removed.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Adding state-based animation to an action

`func withAnimation<Result>(Animation?, () throws -> Result) rethrows ->
Result`

Returns the result of recomputing the view’s body with the provided animation.

`func withAnimation<Result>(Animation?, completionCriteria:
AnimationCompletionCriteria, () throws -> Result, completion: () -> Void)
rethrows -> Result`

Returns the result of recomputing the view’s body with the provided animation,
and runs the completion when all animations are complete.

`struct Animation`

The way a view changes over time to create a smooth visual transition from one
state to another.

Structure

# Animation

The way a view changes over time to create a smooth visual transition from one
state to another.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct Animation

## Overview

An `Animation` provides a visual transition of a view when a state value
changes from one value to another. The characteristics of this transition vary
according to the animation type. For instance, a `linear` animation provides a
mechanical feel to the animation because its speed is consistent from start to
finish. In contrast, an animation that uses easing, like `easeOut`, offers a
more natural feel by varying the acceleration of the animation.

To apply an animation to a view, add the `animation(_:value:)` modifier, and
specify both an animation type and the value to animate. For instance, the
`Circle` view in the following code performs an `easeIn` animation each time
the state variable `scale` changes:

Play

When the value of `scale` changes, the modifier `scaleEffect(_:anchor:)`
resizes `Circle` according to the new value. SwiftUI can animate the
transition between sizes because `Circle` conforms to the `Shape` protocol.
Shapes in SwiftUI conform to the `Animatable` protocol, which describes how to
animate a property of a view.

In addition to adding an animation to a view, you can also configure the
animation by applying animation modifiers to the animation type. For example,
you can:

  * Delay the start of the animation by using the `delay(_:)` modifier.

  * Repeat the animation by using the `repeatCount(_:autoreverses:)` or `repeatForever(autoreverses:)` modifiers.

  * Change the speed of the animation by using the `speed(_:)` modifier.

For example, the `Circle` view in the following code repeats the `easeIn`
animation three times by using the `repeatCount(_:autoreverses:)` modifier:

Play

A view can also perform an animation when a binding value changes. To specify
the animation type on a binding, call its `animation(_:)` method. For example,
the view in the following code performs a `linear` animation, moving the box
truck between the leading and trailing edges of the view. The truck moves each
time a person clicks the `Toggle` control, which changes the value of the
`$isTrailing` binding.

Play

## Topics

### Getting the default animation

`static let `default`: Animation`

A default animation instance.

### Getting linear animations

`static var linear: Animation`

An animation that moves at a constant speed.

`static func linear(duration: TimeInterval) -> Animation`

An animation that moves at a constant speed during a specified duration.

### Getting eased animations

`static var easeIn: Animation`

An animation that starts slowly and then increases speed towards the end of
the movement.

`static func easeIn(duration: TimeInterval) -> Animation`

An animation with a specified duration that starts slowly and then increases
speed towards the end of the movement.

`static var easeOut: Animation`

An animation that starts quickly and then slows towards the end of the
movement.

`static func easeOut(duration: TimeInterval) -> Animation`

An animation with a specified duration that starts quickly and then slows
towards the end of the movement.

`static var easeInOut: Animation`

An animation that combines the behaviors of in and out easing animations.

`static func easeInOut(duration: TimeInterval) -> Animation`

An animation with a specified duration that combines the behaviors of in and
out easing animations.

### Getting built-in spring animations

`static var bouncy: Animation`

A spring animation with a predefined duration and higher amount of bounce.

`static func bouncy(duration: TimeInterval, extraBounce: Double) -> Animation`

A spring animation with a predefined duration and higher amount of bounce that
can be tuned.

`static var smooth: Animation`

A smooth spring animation with a predefined duration and no bounce.

`static func smooth(duration: TimeInterval, extraBounce: Double) -> Animation`

A smooth spring animation with a predefined duration and no bounce that can be
tuned.

`static var snappy: Animation`

A spring animation with a predefined duration and small amount of bounce that
feels more snappy.

`static func snappy(duration: TimeInterval, extraBounce: Double) -> Animation`

A spring animation with a predefined duration and small amount of bounce that
feels more snappy and can be tuned.

### Customizing spring animations

`static var spring: Animation`

A persistent spring animation. When mixed with other `spring()` or
`interactiveSpring()` animations on the same property, each animation will be
replaced by their successor, preserving velocity from one animation to the
next. Optionally blends the response values between springs over a time
period.

`static func spring(Spring, blendDuration: TimeInterval) -> Animation`

A persistent spring animation.

`static func spring(duration: TimeInterval, bounce: Double, blendDuration:
Double) -> Animation`

A persistent spring animation. When mixed with other `spring()` or
`interactiveSpring()` animations on the same property, each animation will be
replaced by their successor, preserving velocity from one animation to the
next. Optionally blends the duration values between springs over a time
period.

`static func spring(response: Double, dampingFraction: Double, blendDuration:
TimeInterval) -> Animation`

A persistent spring animation. When mixed with other `spring()` or
`interactiveSpring()` animations on the same property, each animation will be
replaced by their successor, preserving velocity from one animation to the
next. Optionally blends the response values between springs over a time
period.

`static var interactiveSpring: Animation`

A convenience for a `spring` animation with a lower `duration` value, intended
for driving interactive animations.

`static func interactiveSpring(response: Double, dampingFraction: Double,
blendDuration: TimeInterval) -> Animation`

A convenience for a `spring` animation with a lower `response` value, intended
for driving interactive animations.

`static var interpolatingSpring: Animation`

An interpolating spring animation that uses a damped spring model to produce
values in the range [0, 1] that are then used to interpolate within the [from,
to] range of the animated property. Preserves velocity across overlapping
animations by adding the effects of each animation.

`static func interpolatingSpring(Spring, initialVelocity: Double) ->
Animation`

An interpolating spring animation that uses a damped spring model to produce
values in the range of one to zero.

`static func interpolatingSpring(duration: TimeInterval, bounce: Double,
initialVelocity: Double) -> Animation`

An interpolating spring animation that uses a damped spring model to produce
values in the range [0, 1] that are then used to interpolate within the [from,
to] range of the animated property. Preserves velocity across overlapping
animations by adding the effects of each animation.

`static func interpolatingSpring(mass: Double, stiffness: Double, damping:
Double, initialVelocity: Double) -> Animation`

An interpolating spring animation that uses a damped spring model to produce
values in the range [0, 1] that are then used to interpolate within the [from,
to] range of the animated property. Preserves velocity across overlapping
animations by adding the effects of each animation.

### Creating custom animations

`init<A>(A)`

Create an `Animation` that contains the specified custom animation.

`static func timingCurve(UnitCurve, duration: TimeInterval) -> Animation`

Creates a new animation with speed controlled by the given curve.

`static func timingCurve(Double, Double, Double, Double, duration:
TimeInterval) -> Animation`

An animation created from a cubic Bézier timing curve.

### Configuring an animation

`func delay(TimeInterval) -> Animation`

Delays the start of the animation by the specified number of seconds.

`func repeatCount(Int, autoreverses: Bool) -> Animation`

Repeats the animation for a specific number of times.

`func repeatForever(autoreverses: Bool) -> Animation`

Repeats the animation for the lifespan of the view containing the animation.

`func speed(Double) -> Animation`

Changes the duration of an animation by adjusting its speed.

### Instance Properties

`var base: any CustomAnimation`

### Instance Methods

`func animate<V>(value: V, time: TimeInterval, context: inout
AnimationContext<V>) -> V?`

Calculates the current value of the animation.

`func logicallyComplete(after: TimeInterval) -> Animation`

Causes the animation to report logical completion after the specified
duration, if it has not already logically completed.

`func shouldMerge<V>(previous: Animation, value: V, time: TimeInterval,
context: inout AnimationContext<V>) -> Bool`

Returns a Boolean value that indicates whether the current animation should
merge with a previous animation.

`func velocity<V>(value: V, time: TimeInterval, context: AnimationContext<V>)
-> V?`

Calculates the current velocity of the animation.

### Type Methods

`static func interactiveSpring(duration: TimeInterval, extraBounce: Double,
blendDuration: TimeInterval) -> Animation`

A convenience for a `spring` animation with a lower `response` value, intended
for driving interactive animations.

## Relationships

### Conforms To

  * `CustomDebugStringConvertible`
  * `CustomReflectable`
  * `CustomStringConvertible`
  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Adding state-based animation to an action

`func withAnimation<Result>(Animation?, () throws -> Result) rethrows ->
Result`

Returns the result of recomputing the view’s body with the provided animation.

`func withAnimation<Result>(Animation?, completionCriteria:
AnimationCompletionCriteria, () throws -> Result, completion: () -> Void)
rethrows -> Result`

Returns the result of recomputing the view’s body with the provided animation,
and runs the completion when all animations are complete.

`struct AnimationCompletionCriteria`

The criteria that determines when an animation is considered finished.

Instance Method

# animation(_:)

Applies the given animation to this view when this view changes.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func animation(_ animation: Animation?) -> some View
    

Available when `Self` conforms to `Equatable`.

##  Parameters

`animation`

    

The animation to apply. If `animation` is `nil`, the view doesn’t animate.

## Return Value

A view that applies `animation` to this view whenever it changes.

## See Also

### Adding state-based animation to a view

`func animation<V>(Animation?, value: V) -> some View`

Applies the given animation to this view when the specified value changes.

`func animation<V>(Animation?, body: (PlaceholderContentView<Self>) -> V) ->
some View`

Applies the given animation to all animatable values within the `body`
closure.

Instance Method

# animation(_:value:)

Applies the given animation to this view when the specified value changes.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func animation<V>(
        _ animation: Animation?,
        value: V
    ) -> some View where V : Equatable
    

##  Parameters

`animation`

    

The animation to apply. If `animation` is `nil`, the view doesn’t animate.

`value`

    

A value to monitor for changes.

## Return Value

A view that applies `animation` to this view whenever `value` changes.

## See Also

### Adding state-based animation to a view

`func animation(Animation?) -> some View`

Applies the given animation to this view when this view changes.

Available when `Self` conforms to `Equatable`.

`func animation<V>(Animation?, body: (PlaceholderContentView<Self>) -> V) ->
some View`

Applies the given animation to all animatable values within the `body`
closure.

Instance Method

# animation(_:body:)

Applies the given animation to all animatable values within the `body`
closure.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func animation<V>(
        _ animation: Animation?,
        @ViewBuilder body: (PlaceholderContentView<Self>) -> V
    ) -> some View where V : View
    

## Discussion

Any modifiers applied to the content of `body` will be applied to this view,
and the `animation` will only be used on the modifiers defined in the `body`.

The following code animates the opacity changing with an easeInOut animation,
while the contents of MyView are animated with the implicit transaction’s
animation:

## See Also

### Adding state-based animation to a view

`func animation(Animation?) -> some View`

Applies the given animation to this view when this view changes.

Available when `Self` conforms to `Equatable`.

`func animation<V>(Animation?, value: V) -> some View`

Applies the given animation to this view when the specified value changes.

Instance Method

# phaseAnimator(_:content:animation:)

Animates effects that you apply to a view over a sequence of phases that
change continuously.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func phaseAnimator<Phase>(
        _ phases: some Sequence,
        @ViewBuilder content: @escaping (PlaceholderContentView<Self>, Phase) -> some View,
        animation: @escaping (Phase) -> Animation? = { _ in .default }
    ) -> some View where Phase : Equatable
    

##  Parameters

`phases`

    

The sequence of phases to cycle through. Ensure that the sequence isn’t empty.
If it is, SwiftUI logs a runtime warning and also returns a visual warning as
the output view.

`content`

    

A view builder closure that takes two parameters: a proxy value representing
the modified view and the current phase. You can apply effects to the proxy
based on the current phase.

`animation`

    

A closure that takes the current phase as input. Return the animation to use
when transitioning to the next phase. If you return `nil`, the transition
doesn’t animate. If you don’t set this parameter, SwiftUI uses a default
animation.

## Discussion

When the modified view first appears, this modifier renders its `content`
closure using the first phase as input to the closure, along with a proxy for
the modified view. Apply effects to the proxy — and thus to the modified view
— in a way that’s appropriate for the first phase value.

Right away, the modifier provides its `content` closure with the value of the
second phase. Update the effects that you apply to the proxy view accordingly,
and the modifier animates the change for you. As soon as the animation
completes, the procedure repeats using successive phases until reaching the
last phase, at which point the modifier loops back to the first phase.

## See Also

### Creating phase-based animation

Controlling the timing and movements of your animations

Build sophisticated animations that you control using phase and keyframe
animators.

`func phaseAnimator<Phase>(some Sequence, trigger: some Equatable, content:
(PlaceholderContentView<Self>, Phase) -> some View, animation: (Phase) ->
Animation?) -> some View`

Animates effects that you apply to a view over a sequence of phases that
change based on a trigger.

`struct PhaseAnimator`

A container that animates its content by automatically cycling through a
collection of phases that you provide, each defining a discrete step within an
animation.

Instance Method

# phaseAnimator(_:trigger:content:animation:)

Animates effects that you apply to a view over a sequence of phases that
change based on a trigger.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func phaseAnimator<Phase>(
        _ phases: some Sequence,
        trigger: some Equatable,
        @ViewBuilder content: @escaping (PlaceholderContentView<Self>, Phase) -> some View,
        animation: @escaping (Phase) -> Animation? = { _ in .default }
    ) -> some View where Phase : Equatable
    

##  Parameters

`phases`

    

The sequence of phases to cycle through. Ensure that the sequence isn’t empty.
If it is, SwiftUI logs a runtime warning and also returns a visual warning as
the output view.

`trigger`

    

A value whose changes cause the animator to use the next phase.

`content`

    

A view builder closure that takes two parameters: a proxy value representing
the modified view and the current phase. You can apply effects to the proxy
based on the current phase.

`animation`

    

A closure that takes the current phase as input. Return the animation to use
when transitioning to the next phase. If you return `nil`, the transition
doesn’t animate. If you don’t set this parameter, SwiftUI uses a default
animation.

## Discussion

When the modified view first appears, this modifier renders its `content`
closure using the first phase as input to the closure, along with a proxy for
the modified view. Apply effects to the proxy — and thus to the modified view
— in a way that’s appropriate for the first phase value.

Later, when the value of the `trigger` input changes, the modifier provides
its `content` closure with the value of the second phase. Update the effects
that you apply to the proxy view accordingly, and the modifier animates the
change for you. The next time the `trigger` input changes, this procedure
repeats using successive phases until reaching the last phase, at which point
the modifier loops back to the first phase.

## See Also

### Creating phase-based animation

Controlling the timing and movements of your animations

Build sophisticated animations that you control using phase and keyframe
animators.

`func phaseAnimator<Phase>(some Sequence, content:
(PlaceholderContentView<Self>, Phase) -> some View, animation: (Phase) ->
Animation?) -> some View`

Animates effects that you apply to a view over a sequence of phases that
change continuously.

`struct PhaseAnimator`

A container that animates its content by automatically cycling through a
collection of phases that you provide, each defining a discrete step within an
animation.

Structure

# PhaseAnimator

A container that animates its content by automatically cycling through a
collection of phases that you provide, each defining a discrete step within an
animation.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct PhaseAnimator<Phase, Content> where Phase : Equatable, Content : View

## Overview

Use one of the phase animator view modifiers like
`phaseAnimator(_:content:animation:)` to create a phased animation in your
app.

## Topics

### Creating a phase animator

`init(some Sequence<Phase>, content: (Phase) -> Content, animation: (Phase) ->
Animation?)`

Cycles through a sequence of phases continuously, animating updates to a view
on each phase change.

`init(some Sequence<Phase>, trigger: some Equatable, content: (Phase) ->
Content, animation: (Phase) -> Animation?)`

Cycles through a sequence of phases in response to changes in a specified
value, animating updates to a view on each phase change.

## Relationships

### Conforms To

  * `View`

## See Also

### Creating phase-based animation

Controlling the timing and movements of your animations

Build sophisticated animations that you control using phase and keyframe
animators.

`func phaseAnimator<Phase>(some Sequence, content:
(PlaceholderContentView<Self>, Phase) -> some View, animation: (Phase) ->
Animation?) -> some View`

Animates effects that you apply to a view over a sequence of phases that
change continuously.

`func phaseAnimator<Phase>(some Sequence, trigger: some Equatable, content:
(PlaceholderContentView<Self>, Phase) -> some View, animation: (Phase) ->
Animation?) -> some View`

Animates effects that you apply to a view over a sequence of phases that
change based on a trigger.

Instance Method

# keyframeAnimator(initialValue:repeating:content:keyframes:)

Loops the given keyframes continuously, updating the view using the modifiers
you apply in `body`.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func keyframeAnimator<Value>(
        initialValue: Value,
        repeating: Bool = true,
        @ViewBuilder content: @escaping (PlaceholderContentView<Self>, Value) -> some View,
        @KeyframesBuilder<Value> keyframes: @escaping (Value) -> some Keyframes
    ) -> some View
    

##  Parameters

`initialValue`

    

The initial value that the keyframes will animate from.

`repeating`

    

Whether the keyframes are currently repeating. If false, the value at the
beginning of the keyframe timeline will be provided to the content closure.

`content`

    

A view builder closure that takes two parameters. The first parameter is a
proxy value representing the modified view. The second parameter is the
interpolated value generated by the keyframes.

`keyframes`

    

Keyframes defining how the value changes over time. The current value of the
animator is the single argument, which is equal to `initialValue` when the
view first appears, then is equal to the end value of the previous keyframe
animation on subsequent calls.

## Discussion

Note that the `content` closure will be updated on every frame while
animating, so avoid performing any expensive operations directly within
`content`.

## See Also

### Creating keyframe-based animation

`func keyframeAnimator<Value>(initialValue: Value, trigger: some Equatable,
content: (PlaceholderContentView<Self>, Value) -> some View, keyframes:
(Value) -> some Keyframes) -> some View`

Plays the given keyframes when the given trigger value changes, updating the
view using the modifiers you apply in `body`.

`struct KeyframeAnimator`

A container that animates its content with keyframes.

`protocol Keyframes`

A type that defines changes to a value over time.

`struct KeyframeTimeline`

A description of how a value changes over time, modeled using keyframes.

`struct KeyframeTrack`

A sequence of keyframes animating a single property of a root type.

`struct KeyframeTrackContentBuilder`

The builder that creates keyframe track content from the keyframes that you
define within a closure.

`struct KeyframesBuilder`

A builder that combines keyframe content values into a single value.

`protocol KeyframeTrackContent`

A group of keyframes that define an interpolation curve of an animatable
value.

`struct CubicKeyframe`

A keyframe that uses a cubic curve to smoothly interpolate between values.

`struct LinearKeyframe`

A keyframe that uses simple linear interpolation.

`struct MoveKeyframe`

A keyframe that immediately moves to the given value without interpolating.

`struct SpringKeyframe`

A keyframe that uses a spring function to interpolate to the given value.

Instance Method

# keyframeAnimator(initialValue:trigger:content:keyframes:)

Plays the given keyframes when the given trigger value changes, updating the
view using the modifiers you apply in `body`.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func keyframeAnimator<Value>(
        initialValue: Value,
        trigger: some Equatable,
        @ViewBuilder content: @escaping (PlaceholderContentView<Self>, Value) -> some View,
        @KeyframesBuilder<Value> keyframes: @escaping (Value) -> some Keyframes
    ) -> some View
    

##  Parameters

`initialValue`

    

The initial value that the keyframes will animate from.

`trigger`

    

A value to observe for changes.

`content`

    

A view builder closure that takes two parameters. The first parameter is a
proxy value representing the modified view. The second parameter is the
interpolated value generated by the keyframes.

`keyframes`

    

Keyframes defining how the value changes over time. The current value of the
animator is the single argument, which is equal to `initialValue` when the
view first appears, then is equal to the end value of the previous keyframe
animation on subsequent calls.

## Discussion

Note that the `content` closure will be updated on every frame while
animating, so avoid performing any expensive operations directly within
`content`.

If the trigger value changes while animating, the `keyframes` closure will be
called with the current interpolated value, and the keyframes that you return
define a new animation that replaces the old one. The previous velocity will
be preserved, so cubic or spring keyframes will maintain continuity from the
previous animation if they do not specify a custom initial velocity.

When a keyframe animation finishes, the animator will remain at the end value,
which becomes the initial value for the next animation.

## See Also

### Creating keyframe-based animation

`func keyframeAnimator<Value>(initialValue: Value, repeating: Bool, content:
(PlaceholderContentView<Self>, Value) -> some View, keyframes: (Value) -> some
Keyframes) -> some View`

Loops the given keyframes continuously, updating the view using the modifiers
you apply in `body`.

`struct KeyframeAnimator`

A container that animates its content with keyframes.

`protocol Keyframes`

A type that defines changes to a value over time.

`struct KeyframeTimeline`

A description of how a value changes over time, modeled using keyframes.

`struct KeyframeTrack`

A sequence of keyframes animating a single property of a root type.

`struct KeyframeTrackContentBuilder`

The builder that creates keyframe track content from the keyframes that you
define within a closure.

`struct KeyframesBuilder`

A builder that combines keyframe content values into a single value.

`protocol KeyframeTrackContent`

A group of keyframes that define an interpolation curve of an animatable
value.

`struct CubicKeyframe`

A keyframe that uses a cubic curve to smoothly interpolate between values.

`struct LinearKeyframe`

A keyframe that uses simple linear interpolation.

`struct MoveKeyframe`

A keyframe that immediately moves to the given value without interpolating.

`struct SpringKeyframe`

A keyframe that uses a spring function to interpolate to the given value.

Structure

# KeyframeAnimator

A container that animates its content with keyframes.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct KeyframeAnimator<Value, KeyframePath, Content> where Value == KeyframePath.Value, KeyframePath : Keyframes, Content : View

## Overview

The `content` closure updates every frame while animating, so avoid performing
any expensive operations directly within `content`.

## Topics

### Creating a phase animator

`init(initialValue: Value, repeating: Bool, content: (Value) -> Content,
keyframes: (Value) -> KeyframePath)`

Loops the given keyframes continuously, updating the view using the modifiers
you apply in `body`.

`init(initialValue: Value, trigger: some Equatable, content: (Value) ->
Content, keyframes: (Value) -> KeyframePath)`

Plays the given keyframes when the given trigger value changes, updating the
view using the modifiers you apply in `body`.

## Relationships

### Conforms To

  * `View`

## See Also

### Creating keyframe-based animation

`func keyframeAnimator<Value>(initialValue: Value, repeating: Bool, content:
(PlaceholderContentView<Self>, Value) -> some View, keyframes: (Value) -> some
Keyframes) -> some View`

Loops the given keyframes continuously, updating the view using the modifiers
you apply in `body`.

`func keyframeAnimator<Value>(initialValue: Value, trigger: some Equatable,
content: (PlaceholderContentView<Self>, Value) -> some View, keyframes:
(Value) -> some Keyframes) -> some View`

Plays the given keyframes when the given trigger value changes, updating the
view using the modifiers you apply in `body`.

`protocol Keyframes`

A type that defines changes to a value over time.

`struct KeyframeTimeline`

A description of how a value changes over time, modeled using keyframes.

`struct KeyframeTrack`

A sequence of keyframes animating a single property of a root type.

`struct KeyframeTrackContentBuilder`

The builder that creates keyframe track content from the keyframes that you
define within a closure.

`struct KeyframesBuilder`

A builder that combines keyframe content values into a single value.

`protocol KeyframeTrackContent`

A group of keyframes that define an interpolation curve of an animatable
value.

`struct CubicKeyframe`

A keyframe that uses a cubic curve to smoothly interpolate between values.

`struct LinearKeyframe`

A keyframe that uses simple linear interpolation.

`struct MoveKeyframe`

A keyframe that immediately moves to the given value without interpolating.

`struct SpringKeyframe`

A keyframe that uses a spring function to interpolate to the given value.

Protocol

# Keyframes

A type that defines changes to a value over time.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    protocol Keyframes<Value>

## Topics

### Creating a keyframe

`var body: Self.Body`

The composition of content that comprise the keyframes.

**Required**

` associatedtype Body : Keyframes`

The type of keyframes representing the body of this type.

**Required**

` associatedtype Value = Self.Body.Value`

The type of value animated by this keyframes type

**Required**

## Relationships

### Conforming Types

  * `KeyframeTrack`

## See Also

### Creating keyframe-based animation

`func keyframeAnimator<Value>(initialValue: Value, repeating: Bool, content:
(PlaceholderContentView<Self>, Value) -> some View, keyframes: (Value) -> some
Keyframes) -> some View`

Loops the given keyframes continuously, updating the view using the modifiers
you apply in `body`.

`func keyframeAnimator<Value>(initialValue: Value, trigger: some Equatable,
content: (PlaceholderContentView<Self>, Value) -> some View, keyframes:
(Value) -> some Keyframes) -> some View`

Plays the given keyframes when the given trigger value changes, updating the
view using the modifiers you apply in `body`.

`struct KeyframeAnimator`

A container that animates its content with keyframes.

`struct KeyframeTimeline`

A description of how a value changes over time, modeled using keyframes.

`struct KeyframeTrack`

A sequence of keyframes animating a single property of a root type.

`struct KeyframeTrackContentBuilder`

The builder that creates keyframe track content from the keyframes that you
define within a closure.

`struct KeyframesBuilder`

A builder that combines keyframe content values into a single value.

`protocol KeyframeTrackContent`

A group of keyframes that define an interpolation curve of an animatable
value.

`struct CubicKeyframe`

A keyframe that uses a cubic curve to smoothly interpolate between values.

`struct LinearKeyframe`

A keyframe that uses simple linear interpolation.

`struct MoveKeyframe`

A keyframe that immediately moves to the given value without interpolating.

`struct SpringKeyframe`

A keyframe that uses a spring function to interpolate to the given value.

Structure

# KeyframeTimeline

A description of how a value changes over time, modeled using keyframes.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct KeyframeTimeline<Value>

## Overview

Unlike other animations in SwiftUI (using `Animation`), keyframes don’t
interpolate between from and to values that SwiftUI provides as state changes.
Instead, keyframes fully define the path that a value takes over time using
the tracks that make up their body.

`Keyframes` values are roughly analogous to video clips; they have a set
duration, and you can scrub and evaluate them for any time within the
duration.

The `Keyframes` structure also allows you to compute an interpolated value at
a specific time, which you can use when integrating keyframes into custom use
cases.

For example, you can use a `Keyframes` instance to define animations for a
type conforming to `Animatable:`

For animations that involve multiple coordinated changes, you can include
multiple nested tracks:

Multiple nested tracks update the initial value in the order that they are
declared. This means that if multiple nested plans change the same property of
the root value, the value from the last competing track will be used.

## Topics

### Creating a keyframe timeline

`init(initialValue: Value, content: () -> some Keyframes<Value>)`

Creates a new instance using the initial value and content that you provide.

### Getting the duration

`var duration: TimeInterval`

The duration of the content in seconds.

### Getting an interpolated value

`func value(time: Double) -> Value`

Returns the interpolated value at the given time.

`func value(progress: Double) -> Value`

Returns the interpolated value at the given progress in the range zero to one.

## See Also

### Creating keyframe-based animation

`func keyframeAnimator<Value>(initialValue: Value, repeating: Bool, content:
(PlaceholderContentView<Self>, Value) -> some View, keyframes: (Value) -> some
Keyframes) -> some View`

Loops the given keyframes continuously, updating the view using the modifiers
you apply in `body`.

`func keyframeAnimator<Value>(initialValue: Value, trigger: some Equatable,
content: (PlaceholderContentView<Self>, Value) -> some View, keyframes:
(Value) -> some Keyframes) -> some View`

Plays the given keyframes when the given trigger value changes, updating the
view using the modifiers you apply in `body`.

`struct KeyframeAnimator`

A container that animates its content with keyframes.

`protocol Keyframes`

A type that defines changes to a value over time.

`struct KeyframeTrack`

A sequence of keyframes animating a single property of a root type.

`struct KeyframeTrackContentBuilder`

The builder that creates keyframe track content from the keyframes that you
define within a closure.

`struct KeyframesBuilder`

A builder that combines keyframe content values into a single value.

`protocol KeyframeTrackContent`

A group of keyframes that define an interpolation curve of an animatable
value.

`struct CubicKeyframe`

A keyframe that uses a cubic curve to smoothly interpolate between values.

`struct LinearKeyframe`

A keyframe that uses simple linear interpolation.

`struct MoveKeyframe`

A keyframe that immediately moves to the given value without interpolating.

`struct SpringKeyframe`

A keyframe that uses a spring function to interpolate to the given value.

Structure

# KeyframeTrack

A sequence of keyframes animating a single property of a root type.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct KeyframeTrack<Root, Value, Content> where Value == Content.Value, Content : KeyframeTrackContent

## Topics

### Creating a keyframe track

`init(content: () -> Content)`

Creates an instance that animates the entire value from the root of the key
path.

`init(WritableKeyPath<Root, Value>, content: () -> Content)`

Creates an instance that animates the property of the root value at the given
key path.

## Relationships

### Conforms To

  * `Keyframes`

## See Also

### Creating keyframe-based animation

`func keyframeAnimator<Value>(initialValue: Value, repeating: Bool, content:
(PlaceholderContentView<Self>, Value) -> some View, keyframes: (Value) -> some
Keyframes) -> some View`

Loops the given keyframes continuously, updating the view using the modifiers
you apply in `body`.

`func keyframeAnimator<Value>(initialValue: Value, trigger: some Equatable,
content: (PlaceholderContentView<Self>, Value) -> some View, keyframes:
(Value) -> some Keyframes) -> some View`

Plays the given keyframes when the given trigger value changes, updating the
view using the modifiers you apply in `body`.

`struct KeyframeAnimator`

A container that animates its content with keyframes.

`protocol Keyframes`

A type that defines changes to a value over time.

`struct KeyframeTimeline`

A description of how a value changes over time, modeled using keyframes.

`struct KeyframeTrackContentBuilder`

The builder that creates keyframe track content from the keyframes that you
define within a closure.

`struct KeyframesBuilder`

A builder that combines keyframe content values into a single value.

`protocol KeyframeTrackContent`

A group of keyframes that define an interpolation curve of an animatable
value.

`struct CubicKeyframe`

A keyframe that uses a cubic curve to smoothly interpolate between values.

`struct LinearKeyframe`

A keyframe that uses simple linear interpolation.

`struct MoveKeyframe`

A keyframe that immediately moves to the given value without interpolating.

`struct SpringKeyframe`

A keyframe that uses a spring function to interpolate to the given value.

Structure

# KeyframeTrackContentBuilder

The builder that creates keyframe track content from the keyframes that you
define within a closure.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    @resultBuilder
    struct KeyframeTrackContentBuilder<Value> where Value : Animatable

## Topics

### Building keyframe track content

`static func buildArray([some KeyframeTrackContent<Value>]) -> some
KeyframeTrackContent<Value> `

`static func buildBlock() -> some KeyframeTrackContent<Value> `

`static func buildEither<First, Second>(first: First) ->
KeyframeTrackContentBuilder<Value>.Conditional<Value, First, Second>`

`static func buildEither<First, Second>(second: Second) ->
KeyframeTrackContentBuilder<Value>.Conditional<Value, First, Second>`

`static func buildExpression<K>(K) -> K`

`static func buildPartialBlock(accumulated: some KeyframeTrackContent<Value>,
next: some KeyframeTrackContent<Value>) -> some KeyframeTrackContent<Value> `

`static func buildPartialBlock<K>(first: K) -> K`

`struct Conditional`

A conditional result from the result builder.

Available when `Value` conforms to `Animatable`.

## See Also

### Creating keyframe-based animation

`func keyframeAnimator<Value>(initialValue: Value, repeating: Bool, content:
(PlaceholderContentView<Self>, Value) -> some View, keyframes: (Value) -> some
Keyframes) -> some View`

Loops the given keyframes continuously, updating the view using the modifiers
you apply in `body`.

`func keyframeAnimator<Value>(initialValue: Value, trigger: some Equatable,
content: (PlaceholderContentView<Self>, Value) -> some View, keyframes:
(Value) -> some Keyframes) -> some View`

Plays the given keyframes when the given trigger value changes, updating the
view using the modifiers you apply in `body`.

`struct KeyframeAnimator`

A container that animates its content with keyframes.

`protocol Keyframes`

A type that defines changes to a value over time.

`struct KeyframeTimeline`

A description of how a value changes over time, modeled using keyframes.

`struct KeyframeTrack`

A sequence of keyframes animating a single property of a root type.

`struct KeyframesBuilder`

A builder that combines keyframe content values into a single value.

`protocol KeyframeTrackContent`

A group of keyframes that define an interpolation curve of an animatable
value.

`struct CubicKeyframe`

A keyframe that uses a cubic curve to smoothly interpolate between values.

`struct LinearKeyframe`

A keyframe that uses simple linear interpolation.

`struct MoveKeyframe`

A keyframe that immediately moves to the given value without interpolating.

`struct SpringKeyframe`

A keyframe that uses a spring function to interpolate to the given value.

Structure

# KeyframesBuilder

A builder that combines keyframe content values into a single value.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    @resultBuilder
    struct KeyframesBuilder<Value>

## Topics

### Building keyframes

`static func buildArray([some KeyframeTrackContent<Value>]) -> some
KeyframeTrackContent<Value> `

`static func buildBlock() -> some Keyframes<Value> `

`static func buildBlock() -> some KeyframeTrackContent<Value> `

`static func buildEither<First, Second>(first: First) ->
KeyframeTrackContentBuilder<Value>.Conditional<Value, First, Second>`

`static func buildEither<First, Second>(second: Second) ->
KeyframeTrackContentBuilder<Value>.Conditional<Value, First, Second>`

`static func buildExpression<K>(K) -> K`

`static func buildExpression<Content>(Content) -> Content`

Keyframes

`static func buildFinalResult<Content>(Content) -> KeyframeTrack<Value, Value,
Content>`

`static func buildFinalResult<Content>(Content) -> Content`

`static func buildPartialBlock(accumulated: some KeyframeTrackContent<Value>,
next: some KeyframeTrackContent<Value>) -> some KeyframeTrackContent<Value> `

`static func buildPartialBlock(accumulated: some Keyframes<Value>, next: some
Keyframes<Value>) -> some Keyframes<Value> `

`static func buildPartialBlock<Content>(first: Content) -> Content`

`static func buildPartialBlock<K>(first: K) -> K`

## See Also

### Creating keyframe-based animation

`func keyframeAnimator<Value>(initialValue: Value, repeating: Bool, content:
(PlaceholderContentView<Self>, Value) -> some View, keyframes: (Value) -> some
Keyframes) -> some View`

Loops the given keyframes continuously, updating the view using the modifiers
you apply in `body`.

`func keyframeAnimator<Value>(initialValue: Value, trigger: some Equatable,
content: (PlaceholderContentView<Self>, Value) -> some View, keyframes:
(Value) -> some Keyframes) -> some View`

Plays the given keyframes when the given trigger value changes, updating the
view using the modifiers you apply in `body`.

`struct KeyframeAnimator`

A container that animates its content with keyframes.

`protocol Keyframes`

A type that defines changes to a value over time.

`struct KeyframeTimeline`

A description of how a value changes over time, modeled using keyframes.

`struct KeyframeTrack`

A sequence of keyframes animating a single property of a root type.

`struct KeyframeTrackContentBuilder`

The builder that creates keyframe track content from the keyframes that you
define within a closure.

`protocol KeyframeTrackContent`

A group of keyframes that define an interpolation curve of an animatable
value.

`struct CubicKeyframe`

A keyframe that uses a cubic curve to smoothly interpolate between values.

`struct LinearKeyframe`

A keyframe that uses simple linear interpolation.

`struct MoveKeyframe`

A keyframe that immediately moves to the given value without interpolating.

`struct SpringKeyframe`

A keyframe that uses a spring function to interpolate to the given value.

Protocol

# KeyframeTrackContent

A group of keyframes that define an interpolation curve of an animatable
value.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    protocol KeyframeTrackContent<Value>

## Topics

### Creating a keyframe

`var body: Self.Body`

The composition of content that comprise the keyframe track.

**Required**

` associatedtype Body : KeyframeTrackContent`

**Required**

` associatedtype Value : Animatable = Self.Body.Value`

**Required**

## Relationships

### Conforming Types

  * `CubicKeyframe`
  * `KeyframeTrackContentBuilder.Conditional`

Conforms when `Value` conforms to `Animatable`.

  * `LinearKeyframe`
  * `MoveKeyframe`
  * `SpringKeyframe`

## See Also

### Creating keyframe-based animation

`func keyframeAnimator<Value>(initialValue: Value, repeating: Bool, content:
(PlaceholderContentView<Self>, Value) -> some View, keyframes: (Value) -> some
Keyframes) -> some View`

Loops the given keyframes continuously, updating the view using the modifiers
you apply in `body`.

`func keyframeAnimator<Value>(initialValue: Value, trigger: some Equatable,
content: (PlaceholderContentView<Self>, Value) -> some View, keyframes:
(Value) -> some Keyframes) -> some View`

Plays the given keyframes when the given trigger value changes, updating the
view using the modifiers you apply in `body`.

`struct KeyframeAnimator`

A container that animates its content with keyframes.

`protocol Keyframes`

A type that defines changes to a value over time.

`struct KeyframeTimeline`

A description of how a value changes over time, modeled using keyframes.

`struct KeyframeTrack`

A sequence of keyframes animating a single property of a root type.

`struct KeyframeTrackContentBuilder`

The builder that creates keyframe track content from the keyframes that you
define within a closure.

`struct KeyframesBuilder`

A builder that combines keyframe content values into a single value.

`struct CubicKeyframe`

A keyframe that uses a cubic curve to smoothly interpolate between values.

`struct LinearKeyframe`

A keyframe that uses simple linear interpolation.

`struct MoveKeyframe`

A keyframe that immediately moves to the given value without interpolating.

`struct SpringKeyframe`

A keyframe that uses a spring function to interpolate to the given value.

Structure

# CubicKeyframe

A keyframe that uses a cubic curve to smoothly interpolate between values.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct CubicKeyframe<Value> where Value : Animatable

## Overview

If you don’t specify a start or end velocity, SwiftUI automatically computes a
curve that maintains smooth motion between keyframes.

Adjacent cubic keyframes result in a Catmull-Rom spline.

If a cubic keyframe follows a different type of keyframe, such as a linear
keyframe, the end velocity of the segment defined by the previous keyframe
will be used as the starting velocity.

Likewise, if a cubic keyframe is followed by a different type of keyframe, the
initial velocity of the next segment is used as the end velocity of the
segment defined by this keyframe.

## Topics

### Creating the keyframe

`init(Value, duration: TimeInterval, startVelocity: Value?, endVelocity:
Value?)`

Creates a new keyframe using the given value and timestamp.

## Relationships

### Conforms To

  * `KeyframeTrackContent`

## See Also

### Creating keyframe-based animation

`func keyframeAnimator<Value>(initialValue: Value, repeating: Bool, content:
(PlaceholderContentView<Self>, Value) -> some View, keyframes: (Value) -> some
Keyframes) -> some View`

Loops the given keyframes continuously, updating the view using the modifiers
you apply in `body`.

`func keyframeAnimator<Value>(initialValue: Value, trigger: some Equatable,
content: (PlaceholderContentView<Self>, Value) -> some View, keyframes:
(Value) -> some Keyframes) -> some View`

Plays the given keyframes when the given trigger value changes, updating the
view using the modifiers you apply in `body`.

`struct KeyframeAnimator`

A container that animates its content with keyframes.

`protocol Keyframes`

A type that defines changes to a value over time.

`struct KeyframeTimeline`

A description of how a value changes over time, modeled using keyframes.

`struct KeyframeTrack`

A sequence of keyframes animating a single property of a root type.

`struct KeyframeTrackContentBuilder`

The builder that creates keyframe track content from the keyframes that you
define within a closure.

`struct KeyframesBuilder`

A builder that combines keyframe content values into a single value.

`protocol KeyframeTrackContent`

A group of keyframes that define an interpolation curve of an animatable
value.

`struct LinearKeyframe`

A keyframe that uses simple linear interpolation.

`struct MoveKeyframe`

A keyframe that immediately moves to the given value without interpolating.

`struct SpringKeyframe`

A keyframe that uses a spring function to interpolate to the given value.

Structure

# LinearKeyframe

A keyframe that uses simple linear interpolation.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct LinearKeyframe<Value> where Value : Animatable

## Topics

### Creating the keyframe

`init(Value, duration: TimeInterval, timingCurve: UnitCurve)`

Creates a new keyframe using the given value and timestamp.

## Relationships

### Conforms To

  * `KeyframeTrackContent`

## See Also

### Creating keyframe-based animation

`func keyframeAnimator<Value>(initialValue: Value, repeating: Bool, content:
(PlaceholderContentView<Self>, Value) -> some View, keyframes: (Value) -> some
Keyframes) -> some View`

Loops the given keyframes continuously, updating the view using the modifiers
you apply in `body`.

`func keyframeAnimator<Value>(initialValue: Value, trigger: some Equatable,
content: (PlaceholderContentView<Self>, Value) -> some View, keyframes:
(Value) -> some Keyframes) -> some View`

Plays the given keyframes when the given trigger value changes, updating the
view using the modifiers you apply in `body`.

`struct KeyframeAnimator`

A container that animates its content with keyframes.

`protocol Keyframes`

A type that defines changes to a value over time.

`struct KeyframeTimeline`

A description of how a value changes over time, modeled using keyframes.

`struct KeyframeTrack`

A sequence of keyframes animating a single property of a root type.

`struct KeyframeTrackContentBuilder`

The builder that creates keyframe track content from the keyframes that you
define within a closure.

`struct KeyframesBuilder`

A builder that combines keyframe content values into a single value.

`protocol KeyframeTrackContent`

A group of keyframes that define an interpolation curve of an animatable
value.

`struct CubicKeyframe`

A keyframe that uses a cubic curve to smoothly interpolate between values.

`struct MoveKeyframe`

A keyframe that immediately moves to the given value without interpolating.

`struct SpringKeyframe`

A keyframe that uses a spring function to interpolate to the given value.

Structure

# MoveKeyframe

A keyframe that immediately moves to the given value without interpolating.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct MoveKeyframe<Value> where Value : Animatable

## Topics

### Creating the keyframe

`init(Value)`

Creates a new keyframe using the given value.

## Relationships

### Conforms To

  * `KeyframeTrackContent`

## See Also

### Creating keyframe-based animation

`func keyframeAnimator<Value>(initialValue: Value, repeating: Bool, content:
(PlaceholderContentView<Self>, Value) -> some View, keyframes: (Value) -> some
Keyframes) -> some View`

Loops the given keyframes continuously, updating the view using the modifiers
you apply in `body`.

`func keyframeAnimator<Value>(initialValue: Value, trigger: some Equatable,
content: (PlaceholderContentView<Self>, Value) -> some View, keyframes:
(Value) -> some Keyframes) -> some View`

Plays the given keyframes when the given trigger value changes, updating the
view using the modifiers you apply in `body`.

`struct KeyframeAnimator`

A container that animates its content with keyframes.

`protocol Keyframes`

A type that defines changes to a value over time.

`struct KeyframeTimeline`

A description of how a value changes over time, modeled using keyframes.

`struct KeyframeTrack`

A sequence of keyframes animating a single property of a root type.

`struct KeyframeTrackContentBuilder`

The builder that creates keyframe track content from the keyframes that you
define within a closure.

`struct KeyframesBuilder`

A builder that combines keyframe content values into a single value.

`protocol KeyframeTrackContent`

A group of keyframes that define an interpolation curve of an animatable
value.

`struct CubicKeyframe`

A keyframe that uses a cubic curve to smoothly interpolate between values.

`struct LinearKeyframe`

A keyframe that uses simple linear interpolation.

`struct SpringKeyframe`

A keyframe that uses a spring function to interpolate to the given value.

Structure

# SpringKeyframe

A keyframe that uses a spring function to interpolate to the given value.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct SpringKeyframe<Value> where Value : Animatable

## Topics

### Creating the keyframe

`init(Value, duration: TimeInterval?, spring: Spring, startVelocity: Value?)`

Creates a new keyframe using the given value and timestamp.

## Relationships

### Conforms To

  * `KeyframeTrackContent`

## See Also

### Creating keyframe-based animation

`func keyframeAnimator<Value>(initialValue: Value, repeating: Bool, content:
(PlaceholderContentView<Self>, Value) -> some View, keyframes: (Value) -> some
Keyframes) -> some View`

Loops the given keyframes continuously, updating the view using the modifiers
you apply in `body`.

`func keyframeAnimator<Value>(initialValue: Value, trigger: some Equatable,
content: (PlaceholderContentView<Self>, Value) -> some View, keyframes:
(Value) -> some Keyframes) -> some View`

Plays the given keyframes when the given trigger value changes, updating the
view using the modifiers you apply in `body`.

`struct KeyframeAnimator`

A container that animates its content with keyframes.

`protocol Keyframes`

A type that defines changes to a value over time.

`struct KeyframeTimeline`

A description of how a value changes over time, modeled using keyframes.

`struct KeyframeTrack`

A sequence of keyframes animating a single property of a root type.

`struct KeyframeTrackContentBuilder`

The builder that creates keyframe track content from the keyframes that you
define within a closure.

`struct KeyframesBuilder`

A builder that combines keyframe content values into a single value.

`protocol KeyframeTrackContent`

A group of keyframes that define an interpolation curve of an animatable
value.

`struct CubicKeyframe`

A keyframe that uses a cubic curve to smoothly interpolate between values.

`struct LinearKeyframe`

A keyframe that uses simple linear interpolation.

`struct MoveKeyframe`

A keyframe that immediately moves to the given value without interpolating.

Protocol

# CustomAnimation

A type that defines how an animatable value changes over time.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    protocol CustomAnimation : Hashable

## Overview

Use this protocol to create a type that changes an animatable value over time,
which produces a custom visual transition of a view. For example, the follow
code changes an animatable value using an elastic ease-in ease-out function:

Note

To maintain state during the life span of a custom animation, use the `state`
property available on the `context` parameter value. You can also use
context’s `environment` property to retrieve environment values from the view
that created the custom animation. For more information, see
`AnimationContext`.

To create an `Animation` instance of a custom animation, use the `init(_:)`
initializer, passing in an instance of a custom animation; for example:

To help make view code more readable, extend `Animation` and add a static
property and function that returns an `Animation` instance of a custom
animation. For example, the following code adds the static property
`elasticEaseInEaseOut` that returns the elastic ease-in ease-out animation
with a default duration of `0.35` seconds. Next, the code adds a method that
returns the animation with a specified duration.

To animate a view with the elastic ease-in ease-out animation, a view calls
either `.elasticEaseInEaseOut` or `.elasticEaseInEaseOut(duration:)`. For
example, the follow code includes an Animate button that, when clicked,
animates a circle as it moves from one edge of the view to the other, using
the elastic ease-in ease-out animation with a duration of `5` seconds:

Play

## Topics

### Animating a value

`func animate<V>(value: V, time: TimeInterval, context: inout
AnimationContext<V>) -> V?`

Calculates the value of the animation at the specified time.

**Required**

### Getting the velocity

`func velocity<V>(value: V, time: TimeInterval, context: AnimationContext<V>)
-> V?`

Calculates the velocity of the animation at a specified time.

**Required** Default implementation provided.

### Determining whether to merge

`func shouldMerge<V>(previous: Animation, value: V, time: TimeInterval,
context: inout AnimationContext<V>) -> Bool`

Determines whether an instance of the animation can merge with other instance
of the same type.

**Required** Default implementation provided.

## Relationships

### Inherits From

  * `Equatable`
  * `Hashable`

## See Also

### Creating custom animations

`struct AnimationContext`

Contextual values that a custom animation can use to manage state and access a
view’s environment.

`struct AnimationState`

A container that stores the state for a custom animation.

`protocol AnimationStateKey`

A key for accessing animation state values.

`struct UnitCurve`

A function defined by a two-dimensional curve that maps an input progress in
the range [0,1] to an output progress that is also in the range [0,1]. By
changing the shape of the curve, the effective speed of an animation or other
interpolation can be changed.

`struct Spring`

A representation of a spring’s motion.

Structure

# AnimationContext

Contextual values that a custom animation can use to manage state and access a
view’s environment.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct AnimationContext<Value> where Value : VectorArithmetic

## Overview

The system provides an `AnimationContext` to a `CustomAnimation` instance so
that the animation can store and retrieve values in an instance of
`AnimationState`. To access these values, use the context’s `state` property.

For more convenient access to state, create an `AnimationStateKey` and extend
`AnimationContext` to include a computed property that gets and sets the
`AnimationState` value. Then use this property instead of `state` to retrieve
the state of a custom animation. For example, the following code creates an
animation state key named `PausableState`. Then the code extends
`AnimationContext` to include the `pausableState` property:

To access the pausable state, the custom animation `PausableAnimation` uses
the `pausableState` property instead of the `state` property:

The animation can also retrieve environment values of the view that created
the animation. To retrieve a view’s environment value, use the context’s
`environment` property. For instance, the following code creates a custom
`EnvironmentKey` named `AnimationPausedKey`, and the view
`PausableAnimationView` uses the key to store the paused state:

Then the custom animation `PausableAnimation` retrieves the paused state from
the view’s environment using the `environment` property:

## Topics

### Managing state

`var state: AnimationState<Value>`

The current state of a custom animation.

### Retrieving view environment values

`var environment: EnvironmentValues`

The current environment of the view that created the custom animation.

### Creating context

`func withState<T>(AnimationState<T>) -> AnimationContext<T>`

Creates a new context from another one with a state that you provide.

### Instance Properties

`var isLogicallyComplete: Bool`

Set this to `true` to indicate that an animation is logically complete.

## See Also

### Creating custom animations

`protocol CustomAnimation`

A type that defines how an animatable value changes over time.

`struct AnimationState`

A container that stores the state for a custom animation.

`protocol AnimationStateKey`

A key for accessing animation state values.

`struct UnitCurve`

A function defined by a two-dimensional curve that maps an input progress in
the range [0,1] to an output progress that is also in the range [0,1]. By
changing the shape of the curve, the effective speed of an animation or other
interpolation can be changed.

`struct Spring`

A representation of a spring’s motion.

Structure

# AnimationState

A container that stores the state for a custom animation.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct AnimationState<Value> where Value : VectorArithmetic

## Overview

An `AnimationContext` uses this type to store state for a `CustomAnimation`.
To retrieve the stored state of a context, you can use the `state` property.
However, a more convenient way to access the animation state is to define an
`AnimationStateKey` and extend `AnimationContext` with a computed property
that gets and sets the animation state, as shown in the following code:

When creating an `AnimationStateKey`, it’s convenient to define the state
values that your custom animation needs. For example, the following code adds
the properties `paused` and `pauseTime` to the `PausableState` animation state
key:

To access the pausable state in a `PausableAnimation`, the follow code calls
`pausableState` instead of using the context’s `state` property. And because
the animation state key `PausableState` defines properties for state values,
the custom animation can read and write those values.

### Storing state for secondary animations

A custom animation can also use `AnimationState` to store the state of a
secondary animation. For example, the following code creates an
`AnimationStateKey` that includes the property `secondaryState`, which a
custom animation can use to store other state:

The custom animation `TargetAnimation` uses `TargetState` to store state data
in `secondaryState` for another animation that runs as part of the target
animation.

## Topics

### Creating animation state

`init()`

Create an empty state container.

### Accessing custom keys

`subscript<K>(K.Type) -> K.Value`

Accesses the state for a custom key.

## See Also

### Creating custom animations

`protocol CustomAnimation`

A type that defines how an animatable value changes over time.

`struct AnimationContext`

Contextual values that a custom animation can use to manage state and access a
view’s environment.

`protocol AnimationStateKey`

A key for accessing animation state values.

`struct UnitCurve`

A function defined by a two-dimensional curve that maps an input progress in
the range [0,1] to an output progress that is also in the range [0,1]. By
changing the shape of the curve, the effective speed of an animation or other
interpolation can be changed.

`struct Spring`

A representation of a spring’s motion.

Protocol

# AnimationStateKey

A key for accessing animation state values.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    protocol AnimationStateKey

## Overview

To access animation state from an `AnimationContext` in a custom animation,
create an `AnimationStateKey`. For example, the following code creates an
animation state key named `PausableState` and sets the value for the required
`defaultValue` property. The code also defines properties for state values
that the custom animation needs when calculating animation values. Keeping the
state values in the animation state key makes it more convenient to read and
write those values in the implementation of a `CustomAnimation`.

To make accessing the value of the animation state key more convenient, define
a property for it by extending `AnimationContext`:

Then, you can read and write your state in an instance of `CustomAnimation`
using the `AnimationContext`:

## Topics

### Setting the default value

`static var defaultValue: Self.Value`

The default value for the animation state key.

**Required**

` associatedtype Value`

The associated type representing the type of the animation state key’s value.

**Required**

## See Also

### Creating custom animations

`protocol CustomAnimation`

A type that defines how an animatable value changes over time.

`struct AnimationContext`

Contextual values that a custom animation can use to manage state and access a
view’s environment.

`struct AnimationState`

A container that stores the state for a custom animation.

`struct UnitCurve`

A function defined by a two-dimensional curve that maps an input progress in
the range [0,1] to an output progress that is also in the range [0,1]. By
changing the shape of the curve, the effective speed of an animation or other
interpolation can be changed.

`struct Spring`

A representation of a spring’s motion.

Structure

# UnitCurve

A function defined by a two-dimensional curve that maps an input progress in
the range [0,1] to an output progress that is also in the range [0,1]. By
changing the shape of the curve, the effective speed of an animation or other
interpolation can be changed.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct UnitCurve

## Overview

The horizontal (x) axis defines the input progress: a single input progress
value in the range [0,1] must be provided when evaluating a curve.

The vertical (y) axis maps to the output progress: when a curve is evaluated,
the y component of the point that intersects the input progress is returned.

## Topics

### Getting a linear curve

`static let linear: UnitCurve`

A linear curve.

### Getting easing curves

`static let easeIn: UnitCurve`

A bezier curve that starts out slowly, then speeds up as it finishes.

`static let easeOut: UnitCurve`

A bezier curve that starts out quickly, then slows down as it approaches the
end.

`static let easeInOut: UnitCurve`

A bezier curve that starts out slowly, speeds up over the middle, then slows
down again as it approaches the end.

`static let circularEaseIn: UnitCurve`

A curve that starts out slowly, then speeds up as it finishes.

`static let circularEaseOut: UnitCurve`

A circular curve that starts out quickly, then slows down as it approaches the
end.

`static let circularEaseInOut: UnitCurve`

A circular curve that starts out slowly, speeds up over the middle, then slows
down again as it approaches the end.

### Creating a general Bezier curve

`static func bezier(startControlPoint: UnitPoint, endControlPoint: UnitPoint)
-> UnitCurve`

Creates a new curve using bezier control points.

### Inverting a curve

`var inverse: UnitCurve`

Returns a copy of the curve with its x and y components swapped.

### Getting curve characteristics

`func value(at: Double) -> Double`

Returns the output value (y component) of the curve at the given time.

`func velocity(at: Double) -> Double`

Returns the rate of change (first derivative) of the output value of the curve
at the given time.

### Deprecated symbols

`static let easeInEaseOut: UnitCurve`

A bezier curve that starts out slowly, speeds up over the middle, then slows
down again as it approaches the end.

Deprecated

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Creating custom animations

`protocol CustomAnimation`

A type that defines how an animatable value changes over time.

`struct AnimationContext`

Contextual values that a custom animation can use to manage state and access a
view’s environment.

`struct AnimationState`

A container that stores the state for a custom animation.

`protocol AnimationStateKey`

A key for accessing animation state values.

`struct Spring`

A representation of a spring’s motion.

Structure

# Spring

A representation of a spring’s motion.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct Spring

## Overview

Use this type to convert between different representations of spring
parameters:

You can also use it to query for a spring’s position and its other properties
for a given set of inputs:

## Topics

### Creating a spring

`init(duration: TimeInterval, bounce: Double)`

Creates a spring with the specified duration and bounce.

`init(mass: Double, stiffness: Double, damping: Double, allowOverDamping:
Bool)`

Creates a spring with the specified mass, stiffness, and damping.

`init(response: Double, dampingRatio: Double)`

Creates a spring with the specified response and damping ratio.

`init(settlingDuration: TimeInterval, dampingRatio: Double, epsilon: Double)`

Creates a spring with the specified duration and damping ratio.

### Getting built-in springs

`static var bouncy: Spring`

A spring with a predefined duration and higher amount of bounce.

`static func bouncy(duration: TimeInterval, extraBounce: Double) -> Spring`

A spring with a predefined duration and higher amount of bounce that can be
tuned.

`static var smooth: Spring`

A smooth spring with a predefined duration and no bounce.

`static func smooth(duration: TimeInterval, extraBounce: Double) -> Spring`

A smooth spring with a predefined duration and no bounce that can be tuned.

`static var snappy: Spring`

A spring with a predefined duration and small amount of bounce that feels more
snappy.

`static func snappy(duration: TimeInterval, extraBounce: Double) -> Spring`

A spring with a predefined duration and small amount of bounce that feels more
snappy and can be tuned.

### Getting spring characteristics

`var bounce: Double`

How bouncy the spring is.

`var damping: Double`

Defines how the spring’s motion should be damped due to the forces of
friction.

`var dampingRatio: Double`

The amount of drag applied, as a fraction of the amount needed to produce
critical damping.

`var duration: TimeInterval`

The perceptual duration, which defines the pace of the spring.

`var mass: Double`

The mass of the object attached to the end of the spring.

`var response: Double`

The stiffness of the spring, defined as an approximate duration in seconds.

`var settlingDuration: TimeInterval`

The estimated duration required for the spring system to be considered at
rest.

`var stiffness: Double`

The spring stiffness coefficient.

### Getting spring state

`func value<V>(target: V, initialVelocity: V, time: TimeInterval) -> V`

Calculates the value of the spring at a given time given a target amount of
change.

`func value<V>(fromValue: V, toValue: V, initialVelocity: V, time:
TimeInterval) -> V`

Calculates the value of the spring at a given time for a starting and ending
value for the spring to travel.

`func velocity<V>(target: V, initialVelocity: V, time: TimeInterval) -> V`

Calculates the velocity of the spring at a given time given a target amount of
change.

`func velocity<V>(fromValue: V, toValue: V, initialVelocity: V, time:
TimeInterval) -> V`

Calculates the velocity of the spring at a given time given a starting and
ending value for the spring to travel.

### Setting spring state

`func update<V>(value: inout V, velocity: inout V, target: V, deltaTime:
TimeInterval)`

Updates the current value and velocity of a spring.

### Calculating forces and durations

`func force<V>(target: V, position: V, velocity: V) -> V`

Calculates the force upon the spring given a current position, target, and
velocity amount of change.

`func force<V>(fromValue: V, toValue: V, position: V, velocity: V) -> V`

Calculates the force upon the spring given a current position, velocity, and
divisor from the starting and end values for the spring to travel.

`func settlingDuration<V>(target: V, initialVelocity: V, epsilon: Double) ->
TimeInterval`

The estimated duration required for the spring system to be considered at
rest.

`func settlingDuration<V>(fromValue: V, toValue: V, initialVelocity: V,
epsilon: Double) -> TimeInterval`

The estimated duration required for the spring system to be considered at
rest.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Creating custom animations

`protocol CustomAnimation`

A type that defines how an animatable value changes over time.

`struct AnimationContext`

Contextual values that a custom animation can use to manage state and access a
view’s environment.

`struct AnimationState`

A container that stores the state for a custom animation.

`protocol AnimationStateKey`

A key for accessing animation state values.

`struct UnitCurve`

A function defined by a two-dimensional curve that maps an input progress in
the range [0,1] to an output progress that is also in the range [0,1]. By
changing the shape of the curve, the effective speed of an animation or other
interpolation can be changed.

Protocol

# Animatable

A type that describes how to animate a property of a view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    protocol Animatable

## Topics

### Animating data

`var animatableData: Self.AnimatableData`

The data to animate.

**Required** Default implementations provided.

`associatedtype AnimatableData : VectorArithmetic`

The type defining the data to animate.

**Required**

## Relationships

### Inherited By

  * `AnimatableModifier`
  * `GeometryEffect`
  * `InsettableShape`
  * `Layout`
  * `Shape`
  * `VisualEffect`

### Conforming Types

  * `Angle`
  * `AnyLayout`
  * `AnyShape`
  * `ButtonBorderShape`
  * `Capsule`
  * `Circle`
  * `Color.Resolved`
  * `ContainerRelativeShape`
  * `EdgeInsets`
  * `EdgeInsets3D`
  * `Ellipse`
  * `EmptyVisualEffect`
  * `GridLayout`
  * `HStackLayout`
  * `OffsetShape`
  * `Path`
  * `Rectangle`
  * `RectangleCornerRadii`
  * `RotatedShape`
  * `RoundedRectangle`
  * `ScaledShape`
  * `StrokeStyle`
  * `TransformedShape`
  * `UnevenRoundedRectangle`
  * `UnitPoint`
  * `UnitPoint3D`
  * `VStackLayout`
  * `ZStackLayout`

## See Also

### Making data animatable

`struct AnimatablePair`

A pair of animatable values, which is itself animatable.

`protocol VectorArithmetic`

A type that can serve as the animatable data of an animatable type.

`struct EmptyAnimatableData`

An empty type for animatable data.

Structure

# AnimatablePair

A pair of animatable values, which is itself animatable.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct AnimatablePair<First, Second> where First : VectorArithmetic, Second : VectorArithmetic

## Topics

### Creating an animatable pair

`init(First, Second)`

Creates an animated pair with the provided values.

### Getting the constituent animations

`var first: First`

The first value.

`var second: Second`

The second value.

### Manipulating values

`var magnitudeSquared: Double`

The dot-product of this animated pair with itself.

## Relationships

### Conforms To

  * `AdditiveArithmetic`
  * `Equatable`
  * `Sendable`
  * `VectorArithmetic`

## See Also

### Making data animatable

`protocol Animatable`

A type that describes how to animate a property of a view.

`protocol VectorArithmetic`

A type that can serve as the animatable data of an animatable type.

`struct EmptyAnimatableData`

An empty type for animatable data.

Protocol

# VectorArithmetic

A type that can serve as the animatable data of an animatable type.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    protocol VectorArithmetic : AdditiveArithmetic

## Overview

`VectorArithmetic` extends the `AdditiveArithmetic` protocol with scalar
multiplication and a way to query the vector magnitude of the value. Use this
type as the `animatableData` associated type of a type that conforms to the
`Animatable` protocol.

## Topics

### Manipulating values

`var magnitudeSquared: Double`

Returns the dot-product of this vector arithmetic instance with itself.

**Required**

` func scale(by: Double)`

Multiplies each component of this value by the given value.

**Required** Default implementation provided.

`func scaled(by: Double) -> Self`

Returns a value with each component of this value multiplied by the given
value.

`func interpolate(towards: Self, amount: Double)`

Interpolates this value with `other` by the specified `amount`.

`func interpolated(towards: Self, amount: Double) -> Self`

Returns this value interpolated with `other` by the specified `amount`.

## Relationships

### Inherits From

  * `AdditiveArithmetic`
  * `Equatable`

### Conforming Types

  * `AnimatablePair`
  * `EmptyAnimatableData`

## See Also

### Making data animatable

`protocol Animatable`

A type that describes how to animate a property of a view.

`struct AnimatablePair`

A pair of animatable values, which is itself animatable.

`struct EmptyAnimatableData`

An empty type for animatable data.

Structure

# EmptyAnimatableData

An empty type for animatable data.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct EmptyAnimatableData

## Overview

This type is suitable for use as the `animatableData` property of types that
do not have any animatable properties.

## Topics

### Creating the data

`init()`

### Manipulating the data

`var magnitudeSquared: Double`

The dot-product of this animatable data instance with itself.

## Relationships

### Conforms To

  * `AdditiveArithmetic`
  * `Equatable`
  * `Sendable`
  * `VectorArithmetic`

## See Also

### Making data animatable

`protocol Animatable`

A type that describes how to animate a property of a view.

`struct AnimatablePair`

A pair of animatable values, which is itself animatable.

`protocol VectorArithmetic`

A type that can serve as the animatable data of an animatable type.

Article

# Updating watchOS apps with timelines

Seamlessly schedule updates to your user interface, even while it’s inactive.

## Overview

When you schedule periodic updates to your user interface with `TimelineView`,
updates continue to run even when your app is in the `ScenePhase.background`
or `ScenePhase.inactive` state, making this an ideal choice for keeping a
watchOS app up-to-date while in the Always On state. Additionally, you can use
a `TimelineView` to drive other changes — such as animation — when your app is
running in the foreground.

### Set up the timeline

Specify the part of your user interface that receives periodic updates using a
`TimelineView`.

The `TimelineView` structure takes a schedule that determines when the system
makes updates. It also takes a `ViewBuilder` that defines the updatable
content. The system then calls the view builder, passing the context for each
update.

The `TimelineView.Context` instance contains both the time and the current
`TimelineView.Context.Cadence` for the updates. When creating the updatable
content for the `TimelineView`, use the time from the context, not the current
system time. When in Always On, the system may request views up to 5 minutes
in the future.

The cadence also indicates the current maximum rate for updates that the
`TimelineView` receives:

`TimelineView.Context.Cadence.live`

    

Receives high-frequency updates that are suitable for driving animation.

`TimelineView.Context.Cadence.seconds`

    

Receives up to one update per second.

`TimelineView.Context.Cadence.minutes`

    

Receives up to one update per minute.

The cadence can change from update to update. Always check the current value
and hide information that isn’t relevant. For example, a timer app may show
the time remaining in minutes, seconds, and hundredths of a second when it
receives updates at the `TimelineView.Context.Cadence.live` frequency. It can
also play animation at that frequency.

When the updates drop to the `TimelineView.Context.Cadence.seconds` frequency,
the app hides the hundredths of seconds and swaps the animation for a static
image. The countdown only shows minutes and seconds.

If the frequency drops to `TimelineView.Context.Cadence.minutes`, the app also
hides the seconds and only shows the time remaining to the nearest minute.

### Specify the schedule

When you create a `TimelineView`, you must specify the update schedule, which
is an instance that adopts the `TimelineSchedule` protocol. While you can
create your own custom schedules, SwiftUI provides schedules for many common
use cases.

The system attempts to trigger updates based on the schedule, but it can delay
or defer an update based on the system’s current state. Additionally, if the
schedule is more frequent than the current cadence, the system throttles the
updates to the cadence.

Common schedules include:

`EveryMinuteTimelineSchedule`

    

A schedule to update the `TimelineView` every minute. These updates align with
the system clock. For example, if the schedule starts at 1:00 pm, you’d get
updates at 1:01, 1:02, 1:03, and so on.

`PeriodicTimelineSchedule`

    

A schedule to update your interface at a regular, repeating interval. When you
create this schedule, you specify the starting time and the interval between
updates.

`AnimationTimelineSchedule`

    

A schedule to create a `TimelineView` instance with high-frequency updates for
animated content. When you create the schedule, you can set both the minimum
interval and a Boolean value that indicates whether the animation is currently
paused. If you don’t set a minimum interval, the system picks an appropriate
update interval. Additionally, it only updates the view when the paused
parameter is `false`.

`ExplicitTimelineSchedule`

    

A schedule to specify a list of update times. For example, an app that plays
audiobooks might schedule updates for the beginning of each chapter. When you
create an explicit timeline, you pass a `Sequence`, such as an `Array` of
`Date` instances. The system updates the `TimelineView` at the time specified
by each date in the sequence.

### Update during always on

You can use timeline views to update your watchOS app while it’s in the Always
On state; however, you must be able to specify the view’s contents given a
`Date` instance for a time in the future. To improve performance, the system
may ask for views up to 5 minutes in the future. For example, an egg timer
could use a `TimelineView` to display the time remaining during Always On
because it can calculate the amount of time remaining given any arbitrary time
in the future.

When your app is active and in the foreground, the timeline schedule runs in
the `TimelineScheduleMode.normal` mode, and your `TimelineView` can receive
updates at the `TimelineView.Context.Cadence.live` cadence. When your app
transitions into Always On, the timeline schedule also transitions into the
`TimelineScheduleMode.lowFrequency` mode, the cadence generally drops, and the
system may batch-load future updates.

Note

In the Always On state, apps running a background session may not need to use
a `TimelineView` to update their user interface. Any changes the app makes
while running in the background continue to update its interface; however, to
preserve battery life, the system only refreshes the user interface about once
per second. For more information, see Designing your app for the Always On
state.

While the actual cadence can vary depending on the requested schedule and the
current state of the system, apps generally receive an update frequency based
on whether they have background runtime or are inactive, frontmost apps.

Apps with background runtime receive updates at the
`TimelineView.Context.Cadence.seconds` frequency. This would include apps with
an active background session (like workout or background audio apps) or apps
executing a background refresh task.

Inactive apps receive updates as long as they remain in the frontmost state,
generally at the `TimelineView.Context.Cadence.minutes` frequency. However, if
you request a short burst of updates at the
`TimelineView.Context.Cadence.seconds` frequency, the system provides that
cadence if possible.

For example, an egg timer could use an `ExplicitTimelineSchedule` to set up
per-minute updates for most of the countdown, and switch to per-second updates
for the last minute. If conditions permit, the system provides
`TimelineView.Context.Cadence.seconds` updates for the last minute.

## See Also

### App experience

API Reference

Setting up a watchOS project

Create a new watchOS project or add a watch target to an existing iOS project.

Creating independent watchOS apps

Set up a watchOS app that installs and runs without a companion iOS app.

Keeping your watchOS content up to date

Ensure that your app’s content is relevant and up to date.

Authenticating users on Apple Watch

Create an account sign-up and sign-in strategy for your app.

Responding to the Action button on Apple Watch Ultra

Use App Intents to register actions for your app.

Structure

# TimelineView

A view that updates according to a schedule that you provide.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    struct TimelineView<Schedule, Content> where Schedule : TimelineSchedule

## Overview

A timeline view acts as a container with no appearance of its own. Instead, it
redraws the content it contains at scheduled points in time. For example, you
can update the face of an analog timer once per second:

The closure that creates the content receives an input of type
`TimelineView.Context` that you can use to customize the content’s appearance.
The context includes the `date` that triggered the update. In the example
above, the timeline view sends that date to an analog timer that you create so
the timer view knows how to draw the hands on its face.

The context also includes a `cadence` property that you can use to hide
unnecessary detail. For example, you can use the cadence to decide when it’s
appropriate to display the timer’s second hand:

The system might use a cadence that’s slower than the schedule’s update rate.
For example, a view on watchOS might remain visible when the user lowers their
wrist, but update less frequently, and thus require less detail.

You can define a custom schedule by creating a type that conforms to the
`TimelineSchedule` protocol, or use one of the built-in schedule types:

  * Use an `everyMinute` schedule to update at the beginning of each minute.

  * Use a `periodic(from:by:)` schedule to update periodically with a custom start time and interval between updates.

  * Use an `explicit(_:)` schedule when you need a finite number, or irregular set of updates.

For a schedule containing only dates in the past, the timeline view shows the
last date in the schedule. For a schedule containing only dates in the future,
the timeline draws its content using the current date until the first
scheduled date arrives.

## Topics

### Creating a timeline

`init(Schedule, content: (TimelineViewDefaultContext) -> Content)`

Creates a new timeline view that uses the given schedule.

Available when `Schedule` conforms to `TimelineSchedule` and `Content`
conforms to `View`.

`struct Context`

Information passed to a timeline view’s content callback.

### Deprecated symbols

`init(Schedule, content: (TimelineView<Schedule, Content>.Context) ->
Content)`

Creates a new timeline view that uses the given schedule.

Available when `Schedule` conforms to `TimelineSchedule` and `Content`
conforms to `View`.

Deprecated

## Relationships

### Conforms To

  * `View`

Conforms when `Schedule` conforms to `TimelineSchedule` and `Content` conforms
to `View`.

## See Also

### Updating a view on a schedule

Updating watchOS apps with timelines

Seamlessly schedule updates to your user interface, even while it’s inactive.

`protocol TimelineSchedule`

A type that provides a sequence of dates for use as a schedule.

`typealias TimelineViewDefaultContext`

Information passed to a timeline view’s content callback.

Protocol

# TimelineSchedule

A type that provides a sequence of dates for use as a schedule.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    protocol TimelineSchedule

## Overview

Types that conform to this protocol implement a particular kind of schedule by
defining an `entries(from:mode:)` method that returns a sequence of dates. Use
a timeline schedule type when you initialize a `TimelineView`. For example,
you can create a timeline view that updates every second, starting from some
`startDate`, using a periodic schedule returned by `periodic(from:by:)`:

You can also create custom timeline schedules. The timeline view updates its
content according to the sequence of dates produced by the schedule.

## Topics

### Getting built-in schedules

`static var animation: AnimationTimelineSchedule`

A pausable schedule of dates updating at a frequency no more quickly than the
provided interval.

Available when `Self` is `AnimationTimelineSchedule`.

`static func animation(minimumInterval: Double?, paused: Bool) ->
AnimationTimelineSchedule`

A pausable schedule of dates updating at a frequency no more quickly than the
provided interval.

Available when `Self` is `AnimationTimelineSchedule`.

`static var everyMinute: EveryMinuteTimelineSchedule`

A schedule for updating a timeline view at the start of every minute.

Available when `Self` is `EveryMinuteTimelineSchedule`.

`static func explicit<S>(S) -> ExplicitTimelineSchedule<S>`

A schedule for updating a timeline view at explicit points in time.

`static func periodic(from: Date, by: TimeInterval) ->
PeriodicTimelineSchedule`

A schedule for updating a timeline view at regular intervals.

Available when `Self` is `PeriodicTimelineSchedule`.

### Getting a sequence of dates

`func entries(from: Date, mode: Self.Mode) -> Self.Entries`

Provides a sequence of dates starting around a given date.

**Required**

` associatedtype Entries : Sequence`

The sequence of dates within a schedule.

**Required**

### Specifying a mode

`typealias Mode`

An alias for the timeline schedule update mode.

`enum TimelineScheduleMode`

A mode of operation for timeline schedule updates.

### Supporting types

`struct AnimationTimelineSchedule`

A pausable schedule of dates updating at a frequency no more quickly than the
provided interval.

`struct EveryMinuteTimelineSchedule`

A schedule for updating a timeline view at the start of every minute.

`struct ExplicitTimelineSchedule`

A schedule for updating a timeline view at explicit points in time.

`struct PeriodicTimelineSchedule`

A schedule for updating a timeline view at regular intervals.

## Relationships

### Conforming Types

  * `AnimationTimelineSchedule`
  * `EveryMinuteTimelineSchedule`
  * `ExplicitTimelineSchedule`
  * `PeriodicTimelineSchedule`

## See Also

### Updating a view on a schedule

Updating watchOS apps with timelines

Seamlessly schedule updates to your user interface, even while it’s inactive.

`struct TimelineView`

A view that updates according to a schedule that you provide.

`typealias TimelineViewDefaultContext`

Information passed to a timeline view’s content callback.

Type Alias

# TimelineViewDefaultContext

Information passed to a timeline view’s content callback.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    typealias TimelineViewDefaultContext = TimelineView<EveryMinuteTimelineSchedule, Never>.Context

## Discussion

The context includes both the date from the schedule that triggered the
callback, and a cadence that you can use to customize the appearance of your
view. For example, you might choose to display the second hand of an analog
clock only when the cadence is `TimelineView.Context.Cadence.seconds` or
faster.

Note

This type alias uses a specific concrete instance of `TimelineView.Context`
that all timeline views can use. It does this to prevent introducing an
unnecessary generic parameter dependency on the context type.

## See Also

### Updating a view on a schedule

Updating watchOS apps with timelines

Seamlessly schedule updates to your user interface, even while it’s inactive.

`struct TimelineView`

A view that updates according to a schedule that you provide.

`protocol TimelineSchedule`

A type that provides a sequence of dates for use as a schedule.

Instance Method

# matchedGeometryEffect(id:in:properties:anchor:isSource:)

Defines a group of views with synchronized geometry using an identifier and
namespace that you provide.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func matchedGeometryEffect<ID>(
        id: ID,
        in namespace: Namespace.ID,
        properties: MatchedGeometryProperties = .frame,
        anchor: UnitPoint = .center,
        isSource: Bool = true
    ) -> some View where ID : Hashable
    

##  Parameters

`id`

    

The identifier, often derived from the identifier of the data being displayed
by the view.

`namespace`

    

The namespace in which defines the `id`. New namespaces are created by adding
an `@Namespace` variable to a `View` type and reading its value in the view’s
body method.

`properties`

    

The properties to copy from the source view.

`anchor`

    

The relative location in the view used to produce its shared position value.

`isSource`

    

True if the view should be used as the source of geometry for other views in
the group.

## Return Value

A new view that defines an entry in the global database of views synchronizing
their geometry.

## Discussion

This method sets the geometry of each view in the group from the inserted view
with `isSource = true` (known as the “source” view), updating the values
marked by `properties`.

If inserting a view in the same transaction that another view with the same
key is removed, the system will interpolate their frame rectangles in window
space to make it appear that there is a single view moving from its old
position to its new position. The usual transition mechanisms define how each
of the two views is rendered during the transition (e.g. fade in/out, scale,
etc), the `matchedGeometryEffect()` modifier only arranges for the geometry of
the views to be linked, not their rendering.

If the number of currently-inserted views in the group with `isSource = true`
is not exactly one results are undefined, due to it not being clear which is
the source view.

## See Also

### Synchronizing geometries

`struct MatchedGeometryProperties`

A set of view properties that may be synchronized between views using the
`View.matchedGeometryEffect()` function.

`protocol GeometryEffect`

An effect that changes the visual appearance of a view, largely without
changing its ancestors or descendants.

`struct Namespace`

A dynamic property type that allows access to a namespace defined by the
persistent identity of the object containing the property (e.g. a view).

`func geometryGroup() -> some View`

Isolates the geometry (e.g. position and size) of the view from its parent
view.

Structure

# MatchedGeometryProperties

A set of view properties that may be synchronized between views using the
`View.matchedGeometryEffect()` function.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    @frozen
    struct MatchedGeometryProperties

## Topics

### Matching properties

`static let frame: MatchedGeometryProperties`

Both the `position` and `size` properties.

`static let position: MatchedGeometryProperties`

The view’s position, in window coordinates.

`static let size: MatchedGeometryProperties`

The view’s size, in local coordinates.

## Relationships

### Conforms To

  * `Equatable`
  * `ExpressibleByArrayLiteral`
  * `OptionSet`
  * `RawRepresentable`
  * `Sendable`
  * `SetAlgebra`

## See Also

### Synchronizing geometries

`func matchedGeometryEffect<ID>(id: ID, in: Namespace.ID, properties:
MatchedGeometryProperties, anchor: UnitPoint, isSource: Bool) -> some View`

Defines a group of views with synchronized geometry using an identifier and
namespace that you provide.

`protocol GeometryEffect`

An effect that changes the visual appearance of a view, largely without
changing its ancestors or descendants.

`struct Namespace`

A dynamic property type that allows access to a namespace defined by the
persistent identity of the object containing the property (e.g. a view).

`func geometryGroup() -> some View`

Isolates the geometry (e.g. position and size) of the view from its parent
view.

Protocol

# GeometryEffect

An effect that changes the visual appearance of a view, largely without
changing its ancestors or descendants.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    protocol GeometryEffect : Animatable, ViewModifier where Self.Body == Never

## Overview

The only change the effect makes to the view’s ancestors and descendants is to
change the coordinate transform to and from them.

## Topics

### Applying effects

`func effectValue(size: CGSize) -> ProjectionTransform`

Returns the current value of the effect.

**Required**

` func ignoredByLayout() -> _IgnoredByLayoutEffect<Self>`

Returns an effect that produces the same geometry transform as this effect,
but only applies the transform while rendering its view.

## Relationships

### Inherits From

  * `Animatable`
  * `ViewModifier`

## See Also

### Synchronizing geometries

`func matchedGeometryEffect<ID>(id: ID, in: Namespace.ID, properties:
MatchedGeometryProperties, anchor: UnitPoint, isSource: Bool) -> some View`

Defines a group of views with synchronized geometry using an identifier and
namespace that you provide.

`struct MatchedGeometryProperties`

A set of view properties that may be synchronized between views using the
`View.matchedGeometryEffect()` function.

`struct Namespace`

A dynamic property type that allows access to a namespace defined by the
persistent identity of the object containing the property (e.g. a view).

`func geometryGroup() -> some View`

Isolates the geometry (e.g. position and size) of the view from its parent
view.

Structure

# Namespace

A dynamic property type that allows access to a namespace defined by the
persistent identity of the object containing the property (e.g. a view).

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    @frozen @propertyWrapper
    struct Namespace

## Topics

### Creating a namespace

`init()`

### Getting the namespace

`var wrappedValue: Namespace.ID`

`struct ID`

A namespace defined by the persistent identity of an `@Namespace` dynamic
property.

## Relationships

### Conforms To

  * `DynamicProperty`
  * `Sendable`

## See Also

### Synchronizing geometries

`func matchedGeometryEffect<ID>(id: ID, in: Namespace.ID, properties:
MatchedGeometryProperties, anchor: UnitPoint, isSource: Bool) -> some View`

Defines a group of views with synchronized geometry using an identifier and
namespace that you provide.

`struct MatchedGeometryProperties`

A set of view properties that may be synchronized between views using the
`View.matchedGeometryEffect()` function.

`protocol GeometryEffect`

An effect that changes the visual appearance of a view, largely without
changing its ancestors or descendants.

`func geometryGroup() -> some View`

Isolates the geometry (e.g. position and size) of the view from its parent
view.

Instance Method

# geometryGroup()

Isolates the geometry (e.g. position and size) of the view from its parent
view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func geometryGroup() -> some View
    

## Discussion

By default SwiftUI views push position and size changes down through the view
hierarchy, so that only views that draw something (known as leaf views) apply
the current animation to their frame rectangle. However in some cases this
coalescing behavior can give undesirable results; inserting a geometry group
can correct that. A group acts as a barrier between the parent view and its
subviews, forcing the position and size values to be resolved and animated by
the parent, before being passed down to each subview.

The example below shows one use of this function: ensuring that the member
views of each row in the stack apply (and animate as) a single geometric
transform from their ancestor view, rather than letting the effects of the
ancestor views be applied separately to each leaf view. If the members of
`ItemView` may be added and removed at different times the group ensures that
they stay locked together as animations are applied.

Returns: a new view whose geometry is isolated from that of its parent view.

## See Also

### Synchronizing geometries

`func matchedGeometryEffect<ID>(id: ID, in: Namespace.ID, properties:
MatchedGeometryProperties, anchor: UnitPoint, isSource: Bool) -> some View`

Defines a group of views with synchronized geometry using an identifier and
namespace that you provide.

`struct MatchedGeometryProperties`

A set of view properties that may be synchronized between views using the
`View.matchedGeometryEffect()` function.

`protocol GeometryEffect`

An effect that changes the visual appearance of a view, largely without
changing its ancestors or descendants.

`struct Namespace`

A dynamic property type that allows access to a namespace defined by the
persistent identity of the object containing the property (e.g. a view).

Instance Method

# transition(_:)

Associates a transition with the view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func transition<T>(_ transition: T) -> some View where T : Transition
    

## Discussion

When this view appears or disappears, the transition will be applied to it,
allowing for animating it in and out.

The following code will conditionally show MyView, and when it appears or
disappears, will use a custom RotatingFadeTransition transition to show it.

## See Also

### Defining transitions

`func transition(AnyTransition) -> some View`

Associates a transition with the view.

`protocol Transition`

A description of view changes to apply when a view is added to and removed
from the view hierarchy.

`struct TransitionProperties`

The properties a `Transition` can have.

`enum TransitionPhase`

An indication of which the current stage of a transition.

`struct AsymmetricTransition`

A composite `Transition` that uses a different transition for insertion versus
removal.

`struct AnyTransition`

A type-erased transition.

`func contentTransition(ContentTransition) -> some View`

Modifies the view to use a given transition as its method of animating changes
to the contents of its views.

`var contentTransition: ContentTransition`

The current method of animating the contents of views.

`var contentTransitionAddsDrawingGroup: Bool`

A Boolean value that controls whether views that render content transitions
use GPU-accelerated rendering.

`struct ContentTransition`

A kind of transition that applies to the content within a single view, rather
than to the insertion or removal of a view.

`struct PlaceholderContentView`

A placeholder used to construct an inline modifier, transition, or other
helper type.

Instance Method

# transition(_:)

Associates a transition with the view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func transition(_ t: AnyTransition) -> some View
    

## Discussion

When this view appears or disappears, the transition will be applied to it,
allowing for animating it in and out.

The following code will conditionally show MyView, and when it appears or
disappears, will use a slide transition to show it.

## See Also

### Defining transitions

`func transition<T>(T) -> some View`

Associates a transition with the view.

`protocol Transition`

A description of view changes to apply when a view is added to and removed
from the view hierarchy.

`struct TransitionProperties`

The properties a `Transition` can have.

`enum TransitionPhase`

An indication of which the current stage of a transition.

`struct AsymmetricTransition`

A composite `Transition` that uses a different transition for insertion versus
removal.

`struct AnyTransition`

A type-erased transition.

`func contentTransition(ContentTransition) -> some View`

Modifies the view to use a given transition as its method of animating changes
to the contents of its views.

`var contentTransition: ContentTransition`

The current method of animating the contents of views.

`var contentTransitionAddsDrawingGroup: Bool`

A Boolean value that controls whether views that render content transitions
use GPU-accelerated rendering.

`struct ContentTransition`

A kind of transition that applies to the content within a single view, rather
than to the insertion or removal of a view.

`struct PlaceholderContentView`

A placeholder used to construct an inline modifier, transition, or other
helper type.

Protocol

# Transition

A description of view changes to apply when a view is added to and removed
from the view hierarchy.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    protocol Transition

## Overview

A transition should generally be made by applying one or more modifiers to the
`content`. For symmetric transitions, the `isIdentity` property on `phase` can
be used to change the properties of modifiers. For asymmetric transitions, the
phase itself can be used to change those properties. Transitions should not
use any identity-affecting changes like `.id`, `if`, and `switch` on the
`content`, since doing so would reset the state of the view they’re applied
to, causing wasted work and potentially surprising behavior when it appears
and disappears.

The following code defines a transition that can be used to change the opacity
and rotation when a view appears and disappears.

  * See Also: `TransitionPhase`

  * See Also: `AnyTransition`

## Topics

### Getting built-in transitions

`static var blurReplace: BlurReplaceTransition`

A transition that animates the insertion or removal of a view by combining
blurring and scaling effects.

Available when `Self` is `BlurReplaceTransition`.

`static func blurReplace(BlurReplaceTransition.Configuration) -> Self`

A transition that animates the insertion or removal of a view by combining
blurring and scaling effects.

Available when `Self` is `BlurReplaceTransition`.

`static var identity: IdentityTransition`

A transition that returns the input view, unmodified, as the output view.

Available when `Self` is `IdentityTransition`.

`static func move(edge: Edge) -> Self`

Returns a transition that moves the view away, towards the specified edge of
the view.

Available when `Self` is `MoveTransition`.

`static func offset(CGSize) -> Self`

Returns a transition that offset the view by the specified amount.

Available when `Self` is `OffsetTransition`.

`static func offset(x: CGFloat, y: CGFloat) -> Self`

Returns a transition that offset the view by the specified x and y values.

Available when `Self` is `OffsetTransition`.

`static var opacity: OpacityTransition`

A transition from transparent to opaque on insertion, and from opaque to
transparent on removal.

Available when `Self` is `OpacityTransition`.

`static func push(from: Edge) -> Self`

Creates a transition that when added to a view will animate the view’s
insertion by moving it in from the specified edge while fading it in, and
animate its removal by moving it out towards the opposite edge and fading it
out.

Available when `Self` is `PushTransition`.

`static var scale: ScaleTransition`

Returns a transition that scales the view.

Available when `Self` is `ScaleTransition`.

`static func scale(Double, anchor: UnitPoint) -> Self`

Returns a transition that scales the view by the specified amount.

Available when `Self` is `ScaleTransition`.

`static var slide: SlideTransition`

A transition that inserts by moving in from the leading edge, and removes by
moving out towards the trailing edge.

Available when `Self` is `SlideTransition`.

`static var symbolEffect: SymbolEffectTransition`

A transition that applies the default symbol effect transition to symbol
images within the inserted or removed view hierarchy. Other views are
unaffected by this transition.

Available when `Self` is `SymbolEffectTransition`.

`static func symbolEffect<T>(T, options: SymbolEffectOptions) ->
SymbolEffectTransition`

Creates a transition that applies the provided effect to symbol images within
the inserted or removed view hierarchy. Other views are unaffected by this
transition.

Available when `Self` is `SymbolEffectTransition`.

### Configuring a transition

`func animation(Animation?) -> some Transition`

Attaches an animation to this transition.

`static var properties: TransitionProperties`

Returns the properties this transition type has.

**Required** Default implementation provided.

### Using a transition

`func apply<V>(content: V, phase: TransitionPhase) -> some View`

`func combined<T>(with: T) -> some Transition`

### Creating a custom transition

`func body(content: Self.Content, phase: TransitionPhase) -> Self.Body`

Gets the current body of the caller.

**Required**

` associatedtype Body : View`

The type of view representing the body.

**Required**

` typealias Content`

The content view type passed to `body()`.

### Supporting types

`struct BlurReplaceTransition`

A transition that animates the insertion or removal of a view by combining
blurring and scaling effects.

`struct IdentityTransition`

A transition that returns the input view, unmodified, as the output view.

`struct MoveTransition`

Returns a transition that moves the view away, towards the specified edge of
the view.

`struct OffsetTransition`

Returns a transition that offset the view by the specified amount.

`struct OpacityTransition`

A transition from transparent to opaque on insertion, and from opaque to
transparent on removal.

`struct PushTransition`

A transition that when added to a view will animate the view’s insertion by
moving it in from the specified edge while fading it in, and animate its
removal by moving it out towards the opposite edge and fading it out.

`struct ScaleTransition`

Returns a transition that scales the view.

`struct SlideTransition`

A transition that inserts by moving in from the leading edge, and removes by
moving out towards the trailing edge.

## Relationships

### Conforming Types

  * `AsymmetricTransition`
  * `BlurReplaceTransition`
  * `IdentityTransition`
  * `MoveTransition`
  * `OffsetTransition`
  * `OpacityTransition`
  * `PushTransition`
  * `ScaleTransition`
  * `SlideTransition`
  * `SymbolEffectTransition`

## See Also

### Defining transitions

`func transition<T>(T) -> some View`

Associates a transition with the view.

`func transition(AnyTransition) -> some View`

Associates a transition with the view.

`struct TransitionProperties`

The properties a `Transition` can have.

`enum TransitionPhase`

An indication of which the current stage of a transition.

`struct AsymmetricTransition`

A composite `Transition` that uses a different transition for insertion versus
removal.

`struct AnyTransition`

A type-erased transition.

`func contentTransition(ContentTransition) -> some View`

Modifies the view to use a given transition as its method of animating changes
to the contents of its views.

`var contentTransition: ContentTransition`

The current method of animating the contents of views.

`var contentTransitionAddsDrawingGroup: Bool`

A Boolean value that controls whether views that render content transitions
use GPU-accelerated rendering.

`struct ContentTransition`

A kind of transition that applies to the content within a single view, rather
than to the insertion or removal of a view.

`struct PlaceholderContentView`

A placeholder used to construct an inline modifier, transition, or other
helper type.

Structure

# TransitionProperties

The properties a `Transition` can have.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct TransitionProperties

## Overview

A transition can have properties that specify high level information about it.
This can determine how a transition interacts with other features like
Accessibility settings.

  * See Also: `Transition`

## Topics

### Creating the transition properties

`init(hasMotion: Bool)`

`var hasMotion: Bool`

Whether the transition includes motion.

## Relationships

### Conforms To

  * `Sendable`

## See Also

### Defining transitions

`func transition<T>(T) -> some View`

Associates a transition with the view.

`func transition(AnyTransition) -> some View`

Associates a transition with the view.

`protocol Transition`

A description of view changes to apply when a view is added to and removed
from the view hierarchy.

`enum TransitionPhase`

An indication of which the current stage of a transition.

`struct AsymmetricTransition`

A composite `Transition` that uses a different transition for insertion versus
removal.

`struct AnyTransition`

A type-erased transition.

`func contentTransition(ContentTransition) -> some View`

Modifies the view to use a given transition as its method of animating changes
to the contents of its views.

`var contentTransition: ContentTransition`

The current method of animating the contents of views.

`var contentTransitionAddsDrawingGroup: Bool`

A Boolean value that controls whether views that render content transitions
use GPU-accelerated rendering.

`struct ContentTransition`

A kind of transition that applies to the content within a single view, rather
than to the insertion or removal of a view.

`struct PlaceholderContentView`

A placeholder used to construct an inline modifier, transition, or other
helper type.

Enumeration

# TransitionPhase

An indication of which the current stage of a transition.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    @frozen
    enum TransitionPhase

## Overview

When a view is appearing with a transition, the transition will first be shown
with the `willAppear` phase, then will be immediately moved to the `identity`
phase. When a view is being removed, its transition is changed from the
`identity` phase to the `didDisappear` phase. If a view is removed while it is
still transitioning in, then its phase will change to `didDisappear`. If a
view is re-added while it is transitioning out, its phase will change back to
`identity`.

In the `identity` phase, transitions should generally not make any visual
change to the view they are applied to, since the transition’s view
modifications in the `identity` phase will be applied to the view as long as
it is visible. In the `willAppear` and `didDisappear` phases, transitions
should apply a change that will be animated to create the transition. If no
animatable change is applied, then the transition will be a no-op.

  * See Also: `Transition`

  * See Also: `AnyTransition`

## Topics

### Getting the phase

`case identity`

The transition is being applied to a view that is in the view hierarchy.

`case willAppear`

The transition is being applied to a view that is about to be inserted into
the view hierarchy.

`case didDisappear`

The transition is being applied to a view that has been requested to be
removed from the view hierarchy.

### Getting phase characteristics

`var isIdentity: Bool`

A Boolean that indicates whether the transition should have an identity
effect, i.e. not change the appearance of its view.

`var value: Double`

A value that can be used to multiply effects that are applied differently
depending on the phase.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Defining transitions

`func transition<T>(T) -> some View`

Associates a transition with the view.

`func transition(AnyTransition) -> some View`

Associates a transition with the view.

`protocol Transition`

A description of view changes to apply when a view is added to and removed
from the view hierarchy.

`struct TransitionProperties`

The properties a `Transition` can have.

`struct AsymmetricTransition`

A composite `Transition` that uses a different transition for insertion versus
removal.

`struct AnyTransition`

A type-erased transition.

`func contentTransition(ContentTransition) -> some View`

Modifies the view to use a given transition as its method of animating changes
to the contents of its views.

`var contentTransition: ContentTransition`

The current method of animating the contents of views.

`var contentTransitionAddsDrawingGroup: Bool`

A Boolean value that controls whether views that render content transitions
use GPU-accelerated rendering.

`struct ContentTransition`

A kind of transition that applies to the content within a single view, rather
than to the insertion or removal of a view.

`struct PlaceholderContentView`

A placeholder used to construct an inline modifier, transition, or other
helper type.

Structure

# AsymmetricTransition

A composite `Transition` that uses a different transition for insertion versus
removal.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct AsymmetricTransition<Insertion, Removal> where Insertion : Transition, Removal : Transition

## Topics

### Creating the transition

`init(insertion: Insertion, removal: Removal)`

Creates a composite `Transition` that uses a different transition for
insertion versus removal.

### Getting transition properties

`var insertion: Insertion`

The `Transition` defining the insertion phase of `self`.

`var removal: Removal`

The `Transition` defining the removal phase of `self`.

## Relationships

### Conforms To

  * `Transition`

## See Also

### Defining transitions

`func transition<T>(T) -> some View`

Associates a transition with the view.

`func transition(AnyTransition) -> some View`

Associates a transition with the view.

`protocol Transition`

A description of view changes to apply when a view is added to and removed
from the view hierarchy.

`struct TransitionProperties`

The properties a `Transition` can have.

`enum TransitionPhase`

An indication of which the current stage of a transition.

`struct AnyTransition`

A type-erased transition.

`func contentTransition(ContentTransition) -> some View`

Modifies the view to use a given transition as its method of animating changes
to the contents of its views.

`var contentTransition: ContentTransition`

The current method of animating the contents of views.

`var contentTransitionAddsDrawingGroup: Bool`

A Boolean value that controls whether views that render content transitions
use GPU-accelerated rendering.

`struct ContentTransition`

A kind of transition that applies to the content within a single view, rather
than to the insertion or removal of a view.

`struct PlaceholderContentView`

A placeholder used to construct an inline modifier, transition, or other
helper type.

Structure

# AnyTransition

A type-erased transition.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct AnyTransition

## Overview

  * See Also: `Transition`

## Topics

### Getting built-in transitions

`static let identity: AnyTransition`

A transition that returns the input view, unmodified, as the output view.

`static func move(edge: Edge) -> AnyTransition`

Returns a transition that moves the view away, towards the specified edge of
the view.

`static func offset(CGSize) -> AnyTransition`

`static func offset(x: CGFloat, y: CGFloat) -> AnyTransition`

`static let opacity: AnyTransition`

A transition from transparent to opaque on insertion, and from opaque to
transparent on removal.

`static func push(from: Edge) -> AnyTransition`

Creates a transition that when added to a view will animate the view’s
insertion by moving it in from the specified edge while fading it in, and
animate its removal by moving it out towards the opposite edge and fading it
out.

`static var scale: AnyTransition`

Returns a transition that scales the view.

`static func scale(scale: CGFloat, anchor: UnitPoint) -> AnyTransition`

Returns a transition that scales the view by the specified amount.

`static var slide: AnyTransition`

A transition that inserts by moving in from the leading edge, and removes by
moving out towards the trailing edge.

### Combining and configuring transitions

`func animation(Animation?) -> AnyTransition`

Attaches an animation to this transition.

`static func asymmetric(insertion: AnyTransition, removal: AnyTransition) ->
AnyTransition`

Provides a composite transition that uses a different transition for insertion
versus removal.

`func combined(with: AnyTransition) -> AnyTransition`

Combines this transition with another, returning a new transition that is the
result of both transitions being applied.

### Creating a custom transition

`init<T>(T)`

Create an instance that type-erases `transition`.

`static func modifier<E>(active: E, identity: E) -> AnyTransition`

Returns a transition defined between an active modifier and an identity
modifier.

## See Also

### Defining transitions

`func transition<T>(T) -> some View`

Associates a transition with the view.

`func transition(AnyTransition) -> some View`

Associates a transition with the view.

`protocol Transition`

A description of view changes to apply when a view is added to and removed
from the view hierarchy.

`struct TransitionProperties`

The properties a `Transition` can have.

`enum TransitionPhase`

An indication of which the current stage of a transition.

`struct AsymmetricTransition`

A composite `Transition` that uses a different transition for insertion versus
removal.

`func contentTransition(ContentTransition) -> some View`

Modifies the view to use a given transition as its method of animating changes
to the contents of its views.

`var contentTransition: ContentTransition`

The current method of animating the contents of views.

`var contentTransitionAddsDrawingGroup: Bool`

A Boolean value that controls whether views that render content transitions
use GPU-accelerated rendering.

`struct ContentTransition`

A kind of transition that applies to the content within a single view, rather
than to the insertion or removal of a view.

`struct PlaceholderContentView`

A placeholder used to construct an inline modifier, transition, or other
helper type.

Instance Method

# contentTransition(_:)

Modifies the view to use a given transition as its method of animating changes
to the contents of its views.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func contentTransition(_ transition: ContentTransition) -> some View
    

##  Parameters

`transition`

    

The transition to apply when animating the content change.

## Discussion

This modifier allows you to perform a transition that animates a change within
a single view. The provided `ContentTransition` can present an opacity
animation for content changes, an interpolated animation of the content’s
paths as they change, or perform no animation at all.

Tip

The `contentTransition(_:)` modifier only has an effect within the context of
an `Animation`.

In the following example, a `Button` changes the color and font size of a
`Text` view. Since both of these properties apply to the paths of the text,
the `interpolate` transition can animate a gradual change to these properties
through the entire transition. By contrast, the `opacity` transition would
simply fade between the start and end states.

This example uses an ease-in–ease-out animation with a five-second duration to
make it easier to see the effect of the interpolation. The figure below shows
the `Text` at the beginning of the animation, halfway through, and at the end.

Time| Display  
---|---  
Start|  
Middle|  
End|  
  
To control whether content transitions use GPU-accelerated rendering, set the
value of the `contentTransitionAddsDrawingGroup` environment variable.

## See Also

### Defining transitions

`func transition<T>(T) -> some View`

Associates a transition with the view.

`func transition(AnyTransition) -> some View`

Associates a transition with the view.

`protocol Transition`

A description of view changes to apply when a view is added to and removed
from the view hierarchy.

`struct TransitionProperties`

The properties a `Transition` can have.

`enum TransitionPhase`

An indication of which the current stage of a transition.

`struct AsymmetricTransition`

A composite `Transition` that uses a different transition for insertion versus
removal.

`struct AnyTransition`

A type-erased transition.

`var contentTransition: ContentTransition`

The current method of animating the contents of views.

`var contentTransitionAddsDrawingGroup: Bool`

A Boolean value that controls whether views that render content transitions
use GPU-accelerated rendering.

`struct ContentTransition`

A kind of transition that applies to the content within a single view, rather
than to the insertion or removal of a view.

`struct PlaceholderContentView`

A placeholder used to construct an inline modifier, transition, or other
helper type.

Instance Property

# contentTransition

The current method of animating the contents of views.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var contentTransition: ContentTransition { get set }

## See Also

### Defining transitions

`func transition<T>(T) -> some View`

Associates a transition with the view.

`func transition(AnyTransition) -> some View`

Associates a transition with the view.

`protocol Transition`

A description of view changes to apply when a view is added to and removed
from the view hierarchy.

`struct TransitionProperties`

The properties a `Transition` can have.

`enum TransitionPhase`

An indication of which the current stage of a transition.

`struct AsymmetricTransition`

A composite `Transition` that uses a different transition for insertion versus
removal.

`struct AnyTransition`

A type-erased transition.

`func contentTransition(ContentTransition) -> some View`

Modifies the view to use a given transition as its method of animating changes
to the contents of its views.

`var contentTransitionAddsDrawingGroup: Bool`

A Boolean value that controls whether views that render content transitions
use GPU-accelerated rendering.

`struct ContentTransition`

A kind of transition that applies to the content within a single view, rather
than to the insertion or removal of a view.

`struct PlaceholderContentView`

A placeholder used to construct an inline modifier, transition, or other
helper type.

Instance Property

# contentTransitionAddsDrawingGroup

A Boolean value that controls whether views that render content transitions
use GPU-accelerated rendering.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var contentTransitionAddsDrawingGroup: Bool { get set }

## Discussion

Setting this value to `true` causes SwiftUI to wrap content transitions with a
`drawingGroup(opaque:colorMode:)` modifier.

## See Also

### Defining transitions

`func transition<T>(T) -> some View`

Associates a transition with the view.

`func transition(AnyTransition) -> some View`

Associates a transition with the view.

`protocol Transition`

A description of view changes to apply when a view is added to and removed
from the view hierarchy.

`struct TransitionProperties`

The properties a `Transition` can have.

`enum TransitionPhase`

An indication of which the current stage of a transition.

`struct AsymmetricTransition`

A composite `Transition` that uses a different transition for insertion versus
removal.

`struct AnyTransition`

A type-erased transition.

`func contentTransition(ContentTransition) -> some View`

Modifies the view to use a given transition as its method of animating changes
to the contents of its views.

`var contentTransition: ContentTransition`

The current method of animating the contents of views.

`struct ContentTransition`

A kind of transition that applies to the content within a single view, rather
than to the insertion or removal of a view.

`struct PlaceholderContentView`

A placeholder used to construct an inline modifier, transition, or other
helper type.

Structure

# ContentTransition

A kind of transition that applies to the content within a single view, rather
than to the insertion or removal of a view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    struct ContentTransition

## Overview

Set the behavior of content transitions within a view with the
`contentTransition(_:)` modifier, passing in one of the defined transitions,
such as `opacity` or `interpolate` as the parameter.

Tip

Content transitions only take effect within transactions that apply an
`Animation` to the views inside the `contentTransition(_:)` modifier.

Content transitions only take effect within the context of an `Animation`
block.

## Topics

### Getting content transitions

`static let identity: ContentTransition`

The identity content transition, which indicates that content changes
shouldn’t animate.

`static let interpolate: ContentTransition`

A content transition that indicates the views attempt to interpolate their
contents during transitions, where appropriate.

`static func numericText(countsDown: Bool) -> ContentTransition`

Creates a content transition intended to be used with `Text` views displaying
numeric text. In certain environments changes to the text will enable a
nonstandard transition tailored to numeric characters that count up or down.

`static func numericText(value: Double) -> ContentTransition`

Creates a content transition intended to be used with `Text` views displaying
numbers.

`static let opacity: ContentTransition`

A content transition that indicates content fades from transparent to opaque
on insertion, and from opaque to transparent on removal.

`static var symbolEffect: ContentTransition`

A content transition that applies the default symbol effect transition to
symbol images within the inserted or removed view hierarchy. Other views are
unaffected by this transition.

`static func symbolEffect<T>(T, options: SymbolEffectOptions) ->
ContentTransition`

Creates a content transition that applies the symbol Replace animation to
symbol images that it is applied to.

## Relationships

### Conforms To

  * `Equatable`
  * `Sendable`

## See Also

### Defining transitions

`func transition<T>(T) -> some View`

Associates a transition with the view.

`func transition(AnyTransition) -> some View`

Associates a transition with the view.

`protocol Transition`

A description of view changes to apply when a view is added to and removed
from the view hierarchy.

`struct TransitionProperties`

The properties a `Transition` can have.

`enum TransitionPhase`

An indication of which the current stage of a transition.

`struct AsymmetricTransition`

A composite `Transition` that uses a different transition for insertion versus
removal.

`struct AnyTransition`

A type-erased transition.

`func contentTransition(ContentTransition) -> some View`

Modifies the view to use a given transition as its method of animating changes
to the contents of its views.

`var contentTransition: ContentTransition`

The current method of animating the contents of views.

`var contentTransitionAddsDrawingGroup: Bool`

A Boolean value that controls whether views that render content transitions
use GPU-accelerated rendering.

`struct PlaceholderContentView`

A placeholder used to construct an inline modifier, transition, or other
helper type.

Structure

# PlaceholderContentView

A placeholder used to construct an inline modifier, transition, or other
helper type.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct PlaceholderContentView<Value>

## Overview

You don’t use this type directly. Instead SwiftUI creates this type on your
behalf.

## Relationships

### Conforms To

  * `View`

## See Also

### Defining transitions

`func transition<T>(T) -> some View`

Associates a transition with the view.

`func transition(AnyTransition) -> some View`

Associates a transition with the view.

`protocol Transition`

A description of view changes to apply when a view is added to and removed
from the view hierarchy.

`struct TransitionProperties`

The properties a `Transition` can have.

`enum TransitionPhase`

An indication of which the current stage of a transition.

`struct AsymmetricTransition`

A composite `Transition` that uses a different transition for insertion versus
removal.

`struct AnyTransition`

A type-erased transition.

`func contentTransition(ContentTransition) -> some View`

Modifies the view to use a given transition as its method of animating changes
to the contents of its views.

`var contentTransition: ContentTransition`

The current method of animating the contents of views.

`var contentTransitionAddsDrawingGroup: Bool`

A Boolean value that controls whether views that render content transitions
use GPU-accelerated rendering.

`struct ContentTransition`

A kind of transition that applies to the content within a single view, rather
than to the insertion or removal of a view.

Function

# withTransaction(_:_:)

Executes a closure with the specified transaction and returns the result.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func withTransaction<Result>(
        _ transaction: Transaction,
        _ body: () throws -> Result
    ) rethrows -> Result

##  Parameters

`transaction `

    

An instance of a transaction, set as the thread’s current transaction.

`body`

    

A closure to execute.

## Return Value

The result of executing the closure with the specified transaction.

## See Also

### Moving an animation to another view

`func withTransaction<R, V>(WritableKeyPath<Transaction, V>, V, () throws ->
R) rethrows -> R`

Executes a closure with the specified transaction key path and value and
returns the result.

`func transaction((inout Transaction) -> Void) -> some View`

Applies the given transaction mutation function to all animations used within
the view.

`func transaction(value: some Equatable, (inout Transaction) -> Void) -> some
View`

Applies the given transaction mutation function to all animations used within
the view.

`func transaction<V>((inout Transaction) -> Void, body:
(PlaceholderContentView<Self>) -> V) -> some View`

Applies the given transaction mutation function to all animations used within
the `body` closure.

`struct Transaction`

The context of the current state-processing update.

`protocol TransactionKey`

A key for accessing values in a transaction.

Function

# withTransaction(_:_:_:)

Executes a closure with the specified transaction key path and value and
returns the result.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func withTransaction<R, V>(
        _ keyPath: WritableKeyPath<Transaction, V>,
        _ value: V,
        _ body: () throws -> R
    ) rethrows -> R

##  Parameters

`keyPath`

    

A key path that indicates the property of the `Transaction` structure to
update.

`value`

    

The new value to set for the item specified by `keyPath`.

`body`

    

A closure to execute.

## Return Value

The result of executing the closure with the specified transaction value.

## See Also

### Moving an animation to another view

`func withTransaction<Result>(Transaction, () throws -> Result) rethrows ->
Result`

Executes a closure with the specified transaction and returns the result.

`func transaction((inout Transaction) -> Void) -> some View`

Applies the given transaction mutation function to all animations used within
the view.

`func transaction(value: some Equatable, (inout Transaction) -> Void) -> some
View`

Applies the given transaction mutation function to all animations used within
the view.

`func transaction<V>((inout Transaction) -> Void, body:
(PlaceholderContentView<Self>) -> V) -> some View`

Applies the given transaction mutation function to all animations used within
the `body` closure.

`struct Transaction`

The context of the current state-processing update.

`protocol TransactionKey`

A key for accessing values in a transaction.

Instance Method

# transaction(_:)

Applies the given transaction mutation function to all animations used within
the view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func transaction(_ transform: @escaping (inout Transaction) -> Void) -> some View
    

##  Parameters

`transform`

    

The transformation to apply to transactions within this view.

## Return Value

A view that wraps this view and applies a transformation to all transactions
used within the view.

## Discussion

Use this modifier to change or replace the animation used in a view. Consider
three identical animations controlled by a button that executes all three
animations simultaneously:

  * The first animation rotates the “Rotation” `Text` view by 360 degrees.

  * The second uses the `transaction(_:)` modifier to change the animation by adding a delay to the start of the animation by two seconds and then increases the rotational speed of the “Rotation\nModified” `Text` view animation by a factor of 2.

  * The third animation uses the `transaction(_:)` modifier to replace the rotation animation affecting the “Animation\nReplaced” `Text` view with a spring animation.

The following code implements these animations:

Use this modifier on leaf views such as `Image` or `Button` rather than
container views such as `VStack` or `HStack`. The transformation applies to
all child views within this view; calling `transaction(_:)` on a container
view can lead to unbounded scope of execution depending on the depth of the
view hierarchy.

## See Also

### Moving an animation to another view

`func withTransaction<Result>(Transaction, () throws -> Result) rethrows ->
Result`

Executes a closure with the specified transaction and returns the result.

`func withTransaction<R, V>(WritableKeyPath<Transaction, V>, V, () throws ->
R) rethrows -> R`

Executes a closure with the specified transaction key path and value and
returns the result.

`func transaction(value: some Equatable, (inout Transaction) -> Void) -> some
View`

Applies the given transaction mutation function to all animations used within
the view.

`func transaction<V>((inout Transaction) -> Void, body:
(PlaceholderContentView<Self>) -> V) -> some View`

Applies the given transaction mutation function to all animations used within
the `body` closure.

`struct Transaction`

The context of the current state-processing update.

`protocol TransactionKey`

A key for accessing values in a transaction.

Instance Method

# transaction(value:_:)

Applies the given transaction mutation function to all animations used within
the view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func transaction(
        value: some Equatable,
        _ transform: @escaping (inout Transaction) -> Void
    ) -> some View
    

##  Parameters

`value`

    

A value to monitor for changes.

`transform`

    

The transformation to apply to transactions within this view.

## Return Value

A view that wraps this view and applies a transformation to all transactions
used within the view whenever `value` changes.

## Discussion

Use this modifier to change or replace the animation used in a view. Consider
three identical views controlled by a button that changes all three
simultaneously:

  * The first view animates rotating the “Rotation” `Text` view by 360 degrees.

  * The second uses the `transaction(_:)` modifier to change the animation by adding a delay to the start of the animation by two seconds and then increases the rotational speed of the “Rotation\nModified” `Text` view animation by a factor of 2.

  * The third uses the `transaction(_:)` modifier to disable animations affecting the “Animation\nReplaced” `Text` view.

The following code implements these animations:

## See Also

### Moving an animation to another view

`func withTransaction<Result>(Transaction, () throws -> Result) rethrows ->
Result`

Executes a closure with the specified transaction and returns the result.

`func withTransaction<R, V>(WritableKeyPath<Transaction, V>, V, () throws ->
R) rethrows -> R`

Executes a closure with the specified transaction key path and value and
returns the result.

`func transaction((inout Transaction) -> Void) -> some View`

Applies the given transaction mutation function to all animations used within
the view.

`func transaction<V>((inout Transaction) -> Void, body:
(PlaceholderContentView<Self>) -> V) -> some View`

Applies the given transaction mutation function to all animations used within
the `body` closure.

`struct Transaction`

The context of the current state-processing update.

`protocol TransactionKey`

A key for accessing values in a transaction.

Instance Method

# transaction(_:body:)

Applies the given transaction mutation function to all animations used within
the `body` closure.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func transaction<V>(
        _ transform: @escaping (inout Transaction) -> Void,
        @ViewBuilder body: (PlaceholderContentView<Self>) -> V
    ) -> some View where V : View
    

## Discussion

Any modifiers applied to the content of `body` will be applied to this view,
and the changes to the transaction performed in the `transform` will only
affect the modifiers defined in the `body`.

The following code animates the opacity changing with a faster animation,
while the contents of MyView are animated with the implicit transaction:

  * See Also: `Transaction.disablesAnimations`

## See Also

### Moving an animation to another view

`func withTransaction<Result>(Transaction, () throws -> Result) rethrows ->
Result`

Executes a closure with the specified transaction and returns the result.

`func withTransaction<R, V>(WritableKeyPath<Transaction, V>, V, () throws ->
R) rethrows -> R`

Executes a closure with the specified transaction key path and value and
returns the result.

`func transaction((inout Transaction) -> Void) -> some View`

Applies the given transaction mutation function to all animations used within
the view.

`func transaction(value: some Equatable, (inout Transaction) -> Void) -> some
View`

Applies the given transaction mutation function to all animations used within
the view.

`struct Transaction`

The context of the current state-processing update.

`protocol TransactionKey`

A key for accessing values in a transaction.

Structure

# Transaction

The context of the current state-processing update.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct Transaction

## Overview

Use a transaction to pass an animation between views in a view hierarchy.

The root transaction for a state change comes from the binding that changed,
plus any global values set by calling `withTransaction(_:_:)` or
`withAnimation(_:_:)`.

## Topics

### Creating a transaction

`init()`

Creates a transaction.

`init(animation: Animation?)`

Creates a transaction and assigns its animation property.

### Managing animations

`var animation: Animation?`

The animation, if any, associated with the current state change.

`var disablesAnimations: Bool`

A Boolean value that indicates whether views should disable animations.

`func addAnimationCompletion(criteria: AnimationCompletionCriteria, () ->
Void)`

Adds a completion to run when the animations created with this transaction are
all complete.

### Managing window dismissal

`var dismissBehavior: DismissBehavior`

The behavior for how windows will dismiss programmatically when used in
conjunction with `DismissWindowAction`.

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

`subscript<K>(K.Type) -> K.Value`

Accesses the transaction value associated with a custom key.

## See Also

### Moving an animation to another view

`func withTransaction<Result>(Transaction, () throws -> Result) rethrows ->
Result`

Executes a closure with the specified transaction and returns the result.

`func withTransaction<R, V>(WritableKeyPath<Transaction, V>, V, () throws ->
R) rethrows -> R`

Executes a closure with the specified transaction key path and value and
returns the result.

`func transaction((inout Transaction) -> Void) -> some View`

Applies the given transaction mutation function to all animations used within
the view.

`func transaction(value: some Equatable, (inout Transaction) -> Void) -> some
View`

Applies the given transaction mutation function to all animations used within
the view.

`func transaction<V>((inout Transaction) -> Void, body:
(PlaceholderContentView<Self>) -> V) -> some View`

Applies the given transaction mutation function to all animations used within
the `body` closure.

`protocol TransactionKey`

A key for accessing values in a transaction.

Protocol

# TransactionKey

A key for accessing values in a transaction.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    protocol TransactionKey

## Overview

You can create custom transaction values by extending the `Transaction`
structure with new properties. First declare a new transaction key type and
specify a value for the required `defaultValue` property:

The Swift compiler automatically infers the associated `Value` type as the
type you specify for the default value. Then use the key to define a new
transaction value property:

Clients of your transaction value never use the key directly. Instead, they
use the key path of your custom transaction value property. To set the
transaction value for a change, wrap that change in a call to
`withTransaction`:

To set it for a view and all its subviews, add the `transaction(value:_:)`
view modifier to that view:

To use the value from inside `MyView` or one of its descendants, use the
`transaction(_:)` view modifier:

## Topics

### Setting a default value

`static var defaultValue: Self.Value`

The default value for the transaction key.

**Required**

` associatedtype Value`

The associated type representing the type of the transaction key’s value.

**Required**

## See Also

### Moving an animation to another view

`func withTransaction<Result>(Transaction, () throws -> Result) rethrows ->
Result`

Executes a closure with the specified transaction and returns the result.

`func withTransaction<R, V>(WritableKeyPath<Transaction, V>, V, () throws ->
R) rethrows -> R`

Executes a closure with the specified transaction key path and value and
returns the result.

`func transaction((inout Transaction) -> Void) -> some View`

Applies the given transaction mutation function to all animations used within
the view.

`func transaction(value: some Equatable, (inout Transaction) -> Void) -> some
View`

Applies the given transaction mutation function to all animations used within
the view.

`func transaction<V>((inout Transaction) -> Void, body:
(PlaceholderContentView<Self>) -> V) -> some View`

Applies the given transaction mutation function to all animations used within
the `body` closure.

`struct Transaction`

The context of the current state-processing update.

Protocol

# AnimatableModifier

A modifier that can create another modifier with animation.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    protocol AnimatableModifier : Animatable, ViewModifier

Deprecated

Use `Animatable` instead.

## Relationships

### Inherits From

  * `Animatable`
  * `ViewModifier`

