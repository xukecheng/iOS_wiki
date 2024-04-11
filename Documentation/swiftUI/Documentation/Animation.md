Type Property

# default

A default animation instance.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let `default`: Animation

## Discussion

The `default` animation is `spring(response:dampingFraction:blendDuration:)`
with:

  * `response` equal to `0.55`

  * `dampingFraction` equal to `1.0`

  * `blendDuration` equal to `0.0`

Prior to iOS 17, macOS 14, tvOS 17, and watchOS 10, the `default` animation is
`easeInOut`.

The global function `withAnimation(_:_:)` uses the default animation if you
don’t provide one. For instance, the following code listing shows an example
of using the `default` animation to flip the text “Hello” each time someone
clicks the Animate button.

Play

To use the `default` animation when adding the `animation(_:value:)` view
modifier, specify it explicitly as the animation type. For instance, the
following code shows an example of the `default` animation to spin the text
“Hello” each time someone clicks the Animate button.

Play

A `default` animation instance is only equal to other `default` animation
instances (using `==`), and not equal to other animation instances even when
the animations are identical. For example, if you create an animation using
the `spring(response:dampingFraction:blendDuration:)` modifier with the same
parameter values that `default` uses, the animation isn’t equal to `default`.
This behavior lets you differentiate between animations that you intentionally
choose and those that use the `default` animation.

Type Property

# linear

An animation that moves at a constant speed.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static var linear: Animation { get }

## Return Value

A linear animation with the default duration.

## Discussion

A linear animation provides a mechanical feel to the motion because its speed
is consistent from start to finish of the animation. This constant speed makes
a linear animation ideal for animating the movement of objects where changes
in the speed might feel awkward, such as with an activity indicator.

The following code shows an example of using linear animation to animate the
movement of a circle as it moves between the leading and trailing edges of the
view. The circle also animates its color change as it moves across the view.

Play

The `linear` animation has a default duration of 0.35 seconds. To specify a
different duration, use `linear(duration:)`.

## See Also

### Getting linear animations

`static func linear(duration: TimeInterval) -> Animation`

An animation that moves at a constant speed during a specified duration.

Type Method

# linear(duration:)

An animation that moves at a constant speed during a specified duration.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static func linear(duration: TimeInterval) -> Animation

##  Parameters

`duration`

    

The length of time, expressed in seconds, that the animation takes to
complete.

## Return Value

A linear animation with a specified duration.

## Discussion

A linear animation provides a mechanical feel to the motion because its speed
is consistent from start to finish of the animation. This constant speed makes
a linear animation ideal for animating the movement of objects where changes
in the speed might feel awkward, such as with an activity indicator.

Use `linear(duration:)` when you want to specify the time it takes for the
animation to complete. Otherwise, use `linear` to perform the animation for a
default length of time.

The following code shows an example of using linear animation with a duration
of two seconds to animate the movement of a circle as it moves between the
leading and trailing edges of the view. The color of the circle also animates
from red to blue as it moves across the view.

Play

## See Also

### Getting linear animations

`static var linear: Animation`

An animation that moves at a constant speed.

Type Property

# easeIn

An animation that starts slowly and then increases speed towards the end of
the movement.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static var easeIn: Animation { get }

## Return Value

An ease-in animation with the default duration.

## Discussion

An easing animation provides motion with a natural feel by varying the
acceleration and deceleration of the animation, which matches how things tend
to move in reality. With an ease in animation, the motion starts slowly and
increases its speed towards the end.

The `easeIn` animation has a default duration of 0.35 seconds. To specify a
different duration, use `easeIn(duration:)`.

The following code shows an example of animating the size changes of a
`Circle` using the ease in animation.

Play

## See Also

### Getting eased animations

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

Type Method

# easeIn(duration:)

An animation with a specified duration that starts slowly and then increases
speed towards the end of the movement.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static func easeIn(duration: TimeInterval) -> Animation

##  Parameters

`duration`

    

The length of time, expressed in seconds, that the animation takes to
complete.

## Return Value

An ease-in animation with a specified duration.

## Discussion

An easing animation provides motion with a natural feel by varying the
acceleration and deceleration of the animation, which matches how things tend
to move in reality. With an ease in animation, the motion starts slowly and
increases its speed towards the end.

Use `easeIn(duration:)` when you want to specify the time it takes for the
animation to complete. Otherwise, use `easeIn` to perform the animation for a
default length of time.

The following code shows an example of animating the size changes of a
`Circle` using an ease in animation with a duration of one second.

Play

## See Also

### Getting eased animations

`static var easeIn: Animation`

An animation that starts slowly and then increases speed towards the end of
the movement.

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

Type Property

# easeOut

An animation that starts quickly and then slows towards the end of the
movement.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static var easeOut: Animation { get }

## Return Value

An ease-out animation with the default duration.

## Discussion

An easing animation provides motion with a natural feel by varying the
acceleration and deceleration of the animation, which matches how things tend
to move in reality. With an ease out animation, the motion starts quickly and
decreases its speed towards the end.

The `easeOut` animation has a default duration of 0.35 seconds. To specify a
different duration, use `easeOut(duration:)`.

The following code shows an example of animating the size changes of a
`Circle` using an ease out animation.

Play

## See Also

### Getting eased animations

`static var easeIn: Animation`

An animation that starts slowly and then increases speed towards the end of
the movement.

`static func easeIn(duration: TimeInterval) -> Animation`

An animation with a specified duration that starts slowly and then increases
speed towards the end of the movement.

`static func easeOut(duration: TimeInterval) -> Animation`

An animation with a specified duration that starts quickly and then slows
towards the end of the movement.

`static var easeInOut: Animation`

An animation that combines the behaviors of in and out easing animations.

`static func easeInOut(duration: TimeInterval) -> Animation`

An animation with a specified duration that combines the behaviors of in and
out easing animations.

Type Method

# easeOut(duration:)

An animation with a specified duration that starts quickly and then slows
towards the end of the movement.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static func easeOut(duration: TimeInterval) -> Animation

##  Parameters

`duration`

    

The length of time, expressed in seconds, that the animation takes to
complete.

## Return Value

An ease-out animation with a specified duration.

## Discussion

An easing animation provides motion with a natural feel by varying the
acceleration and deceleration of the animation, which matches how things tend
to move in reality. With an ease out animation, the motion starts quickly and
decreases its speed towards the end.

Use `easeOut(duration:)` when you want to specify the time it takes for the
animation to complete. Otherwise, use `easeOut` to perform the animation for a
default length of time.

The following code shows an example of animating the size changes of a
`Circle` using an ease out animation with a duration of one second.

Play

## See Also

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

`static var easeInOut: Animation`

An animation that combines the behaviors of in and out easing animations.

`static func easeInOut(duration: TimeInterval) -> Animation`

An animation with a specified duration that combines the behaviors of in and
out easing animations.

Type Property

# easeInOut

An animation that combines the behaviors of in and out easing animations.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static var easeInOut: Animation { get }

## Return Value

An ease-in ease-out animation with the default duration.

## Discussion

An easing animation provides motion with a natural feel by varying the
acceleration and deceleration of the animation, which matches how things tend
to move in reality. An ease in and out animation starts slowly, increasing its
speed towards the halfway point, and finally decreasing the speed towards the
end of the animation.

The `easeInOut` animation has a default duration of 0.35 seconds. To specify
the duration, use the `easeInOut(duration:)` method.

The following code shows an example of animating the size changes of a
`Circle` using an ease in and out animation.

Play

## See Also

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

`static func easeInOut(duration: TimeInterval) -> Animation`

An animation with a specified duration that combines the behaviors of in and
out easing animations.

Type Method

# easeInOut(duration:)

An animation with a specified duration that combines the behaviors of in and
out easing animations.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static func easeInOut(duration: TimeInterval) -> Animation

##  Parameters

`duration`

    

The length of time, expressed in seconds, that the animation takes to
complete.

## Return Value

An ease-in ease-out animation with a specified duration.

## Discussion

An easing animation provides motion with a natural feel by varying the
acceleration and deceleration of the animation, which matches how things tend
to move in reality. An ease in and out animation starts slowly, increasing its
speed towards the halfway point, and finally decreasing the speed towards the
end of the animation.

Use `easeInOut(duration:)` when you want to specify the time it takes for the
animation to complete. Otherwise, use `easeInOut` to perform the animation for
a default length of time.

The following code shows an example of animating the size changes of a
`Circle` using an ease in and out animation with a duration of one second.

Play

## See Also

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

Type Property

# bouncy

A spring animation with a predefined duration and higher amount of bounce.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static var bouncy: Animation { get }

## See Also

### Getting built-in spring animations

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

Type Method

# bouncy(duration:extraBounce:)

A spring animation with a predefined duration and higher amount of bounce that
can be tuned.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static func bouncy(
        duration: TimeInterval = 0.5,
        extraBounce: Double = 0.0
    ) -> Animation

##  Parameters

`duration`

    

The perceptual duration, which defines the pace of the spring. This is
approximately equal to the settling duration, but for very bouncy springs,
will be the duration of the period of oscillation for the spring.

`extraBounce`

    

How much additional bounce should be added to the base bounce of 0.3.

`blendDuration`

    

The duration in seconds over which to interpolate changes to the duration.

## See Also

### Getting built-in spring animations

`static var bouncy: Animation`

A spring animation with a predefined duration and higher amount of bounce.

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

Type Property

# smooth

A smooth spring animation with a predefined duration and no bounce.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static var smooth: Animation { get }

## See Also

### Getting built-in spring animations

`static var bouncy: Animation`

A spring animation with a predefined duration and higher amount of bounce.

`static func bouncy(duration: TimeInterval, extraBounce: Double) -> Animation`

A spring animation with a predefined duration and higher amount of bounce that
can be tuned.

`static func smooth(duration: TimeInterval, extraBounce: Double) -> Animation`

A smooth spring animation with a predefined duration and no bounce that can be
tuned.

`static var snappy: Animation`

A spring animation with a predefined duration and small amount of bounce that
feels more snappy.

`static func snappy(duration: TimeInterval, extraBounce: Double) -> Animation`

A spring animation with a predefined duration and small amount of bounce that
feels more snappy and can be tuned.

Type Method

# smooth(duration:extraBounce:)

A smooth spring animation with a predefined duration and no bounce that can be
tuned.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static func smooth(
        duration: TimeInterval = 0.5,
        extraBounce: Double = 0.0
    ) -> Animation

##  Parameters

`duration`

    

The perceptual duration, which defines the pace of the spring. This is
approximately equal to the settling duration, but for very bouncy springs,
will be the duration of the period of oscillation for the spring.

`extraBounce`

    

How much additional bounce should be added to the base bounce of 0.

`blendDuration`

    

The duration in seconds over which to interpolate changes to the duration.

## See Also

### Getting built-in spring animations

`static var bouncy: Animation`

A spring animation with a predefined duration and higher amount of bounce.

`static func bouncy(duration: TimeInterval, extraBounce: Double) -> Animation`

A spring animation with a predefined duration and higher amount of bounce that
can be tuned.

`static var smooth: Animation`

A smooth spring animation with a predefined duration and no bounce.

`static var snappy: Animation`

A spring animation with a predefined duration and small amount of bounce that
feels more snappy.

`static func snappy(duration: TimeInterval, extraBounce: Double) -> Animation`

A spring animation with a predefined duration and small amount of bounce that
feels more snappy and can be tuned.

Type Property

# snappy

A spring animation with a predefined duration and small amount of bounce that
feels more snappy.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static var snappy: Animation { get }

## See Also

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

`static func snappy(duration: TimeInterval, extraBounce: Double) -> Animation`

A spring animation with a predefined duration and small amount of bounce that
feels more snappy and can be tuned.

Type Method

# snappy(duration:extraBounce:)

A spring animation with a predefined duration and small amount of bounce that
feels more snappy and can be tuned.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static func snappy(
        duration: TimeInterval = 0.5,
        extraBounce: Double = 0.0
    ) -> Animation

##  Parameters

`duration`

    

The perceptual duration, which defines the pace of the spring. This is
approximately equal to the settling duration, but for very bouncy springs,
will be the duration of the period of oscillation for the spring.

`extraBounce`

    

How much additional bounce should be added to the base bounce of 0.15.

`blendDuration`

    

The duration in seconds over which to interpolate changes to the duration.

## See Also

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

Type Property

# spring

A persistent spring animation. When mixed with other `spring()` or
`interactiveSpring()` animations on the same property, each animation will be
replaced by their successor, preserving velocity from one animation to the
next. Optionally blends the response values between springs over a time
period.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static var spring: Animation { get }

## Discussion

This uses the default parameter values.

## See Also

### Customizing spring animations

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

Type Method

# spring(_:blendDuration:)

A persistent spring animation.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static func spring(
        _ spring: Spring,
        blendDuration: TimeInterval = 0.0
    ) -> Animation

## Discussion

When mixed with other `spring()` or `interactiveSpring()` animations on the
same property, each animation will be replaced by their successor, preserving
velocity from one animation to the next. Optionally blends the duration values
between springs over a time period.

## See Also

### Customizing spring animations

`static var spring: Animation`

A persistent spring animation. When mixed with other `spring()` or
`interactiveSpring()` animations on the same property, each animation will be
replaced by their successor, preserving velocity from one animation to the
next. Optionally blends the response values between springs over a time
period.

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

Type Method

# spring(duration:bounce:blendDuration:)

A persistent spring animation. When mixed with other `spring()` or
`interactiveSpring()` animations on the same property, each animation will be
replaced by their successor, preserving velocity from one animation to the
next. Optionally blends the duration values between springs over a time
period.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static func spring(
        duration: TimeInterval = 0.5,
        bounce: Double = 0.0,
        blendDuration: Double = 0
    ) -> Animation

##  Parameters

`duration`

    

The perceptual duration, which defines the pace of the spring. This is
approximately equal to the settling duration, but for very bouncy springs,
will be the duration of the period of oscillation for the spring.

`bounce`

    

How bouncy the spring should be. A value of 0 indicates no bounces (a
critically damped spring), positive values indicate increasing amounts of
bounciness up to a maximum of 1.0 (corresponding to undamped oscillation), and
negative values indicate overdamped springs with a minimum value of -1.0.

`blendDuration`

    

The duration in seconds over which to interpolate changes to the duration.

## Return Value

a spring animation.

## See Also

### Customizing spring animations

`static var spring: Animation`

A persistent spring animation. When mixed with other `spring()` or
`interactiveSpring()` animations on the same property, each animation will be
replaced by their successor, preserving velocity from one animation to the
next. Optionally blends the response values between springs over a time
period.

`static func spring(Spring, blendDuration: TimeInterval) -> Animation`

A persistent spring animation.

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

Type Method

# spring(response:dampingFraction:blendDuration:)

A persistent spring animation. When mixed with other `spring()` or
`interactiveSpring()` animations on the same property, each animation will be
replaced by their successor, preserving velocity from one animation to the
next. Optionally blends the response values between springs over a time
period.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static func spring(
        response: Double = 0.5,
        dampingFraction: Double = 0.825,
        blendDuration: TimeInterval = 0
    ) -> Animation

##  Parameters

`response`

    

The stiffness of the spring, defined as an approximate duration in seconds. A
value of zero requests an infinitely-stiff spring, suitable for driving
interactive animations.

`dampingFraction`

    

The amount of drag applied to the value being animated, as a fraction of an
estimate of amount needed to produce critical damping.

`blendDuration`

    

The duration in seconds over which to interpolate changes to the response
value of the spring.

## Return Value

a spring animation.

## See Also

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

Type Property

# interactiveSpring

A convenience for a `spring` animation with a lower `duration` value, intended
for driving interactive animations.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static var interactiveSpring: Animation { get }

## Discussion

This uses the default parameter values.

## See Also

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

Type Method

# interactiveSpring(response:dampingFraction:blendDuration:)

A convenience for a `spring` animation with a lower `response` value, intended
for driving interactive animations.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static func interactiveSpring(
        response: Double = 0.15,
        dampingFraction: Double = 0.86,
        blendDuration: TimeInterval = 0.25
    ) -> Animation

## See Also

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

Type Property

# interpolatingSpring

An interpolating spring animation that uses a damped spring model to produce
values in the range [0, 1] that are then used to interpolate within the [from,
to] range of the animated property. Preserves velocity across overlapping
animations by adding the effects of each animation.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static var interpolatingSpring: Animation { get }

## Discussion

This uses the default parameter values.

## See Also

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

Type Method

# interpolatingSpring(_:initialVelocity:)

An interpolating spring animation that uses a damped spring model to produce
values in the range of one to zero.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static func interpolatingSpring(
        _ spring: Spring,
        initialVelocity: Double = 0.0
    ) -> Animation

## Discussion

These vales are used to interpolate within the `[from, to]` range of the
animated property. Preserves velocity across overlapping animations by adding
the effects of each animation.

## See Also

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

Type Method

# interpolatingSpring(duration:bounce:initialVelocity:)

An interpolating spring animation that uses a damped spring model to produce
values in the range [0, 1] that are then used to interpolate within the [from,
to] range of the animated property. Preserves velocity across overlapping
animations by adding the effects of each animation.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static func interpolatingSpring(
        duration: TimeInterval = 0.5,
        bounce: Double = 0.0,
        initialVelocity: Double = 0.0
    ) -> Animation

##  Parameters

`duration`

    

The perceptual duration, which defines the pace of the spring. This is
approximately equal to the settling duration, but for very bouncy springs,
will be the duration of the period of oscillation for the spring.

`bounce`

    

How bouncy the spring should be. A value of 0 indicates no bounces (a
critically damped spring), positive values indicate increasing amounts of
bounciness up to a maximum of 1.0 (corresponding to undamped oscillation), and
negative values indicate overdamped springs with a minimum value of -1.0.

`initialVelocity`

    

the initial velocity of the spring, as a value in the range [0, 1]
representing the magnitude of the value being animated.

## Return Value

a spring animation.

## See Also

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

`static func interpolatingSpring(mass: Double, stiffness: Double, damping:
Double, initialVelocity: Double) -> Animation`

An interpolating spring animation that uses a damped spring model to produce
values in the range [0, 1] that are then used to interpolate within the [from,
to] range of the animated property. Preserves velocity across overlapping
animations by adding the effects of each animation.

Type Method

# interpolatingSpring(mass:stiffness:damping:initialVelocity:)

An interpolating spring animation that uses a damped spring model to produce
values in the range [0, 1] that are then used to interpolate within the [from,
to] range of the animated property. Preserves velocity across overlapping
animations by adding the effects of each animation.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static func interpolatingSpring(
        mass: Double = 1.0,
        stiffness: Double,
        damping: Double,
        initialVelocity: Double = 0.0
    ) -> Animation

##  Parameters

`mass`

    

The mass of the object attached to the spring.

`stiffness`

    

The stiffness of the spring.

`damping`

    

The spring damping value.

`initialVelocity`

    

the initial velocity of the spring, as a value in the range [0, 1]
representing the magnitude of the value being animated.

## Return Value

a spring animation.

## See Also

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

Initializer

# init(_:)

Create an `Animation` that contains the specified custom animation.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init<A>(_ base: A) where A : CustomAnimation

## See Also

### Creating custom animations

`static func timingCurve(UnitCurve, duration: TimeInterval) -> Animation`

Creates a new animation with speed controlled by the given curve.

`static func timingCurve(Double, Double, Double, Double, duration:
TimeInterval) -> Animation`

An animation created from a cubic Bézier timing curve.

Type Method

# timingCurve(_:duration:)

Creates a new animation with speed controlled by the given curve.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static func timingCurve(
        _ curve: UnitCurve,
        duration: TimeInterval
    ) -> Animation

##  Parameters

`timingCurve`

    

A curve that describes the speed of the animation over its duration.

`duration`

    

The duration of the animation, in seconds.

## See Also

### Creating custom animations

`init<A>(A)`

Create an `Animation` that contains the specified custom animation.

`static func timingCurve(Double, Double, Double, Double, duration:
TimeInterval) -> Animation`

An animation created from a cubic Bézier timing curve.

Type Method

# timingCurve(_:_:_:_:duration:)

An animation created from a cubic Bézier timing curve.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static func timingCurve(
        _ p1x: Double,
        _ p1y: Double,
        _ p2x: Double,
        _ p2y: Double,
        duration: TimeInterval = 0.35
    ) -> Animation

##  Parameters

`p1x`

    

The x-coordinate of the first control point of the cubic Bézier curve.

`p1y`

    

The y-coordinate of the first control point of the cubic Bézier curve.

`p2x`

    

The x-coordinate of the second control point of the cubic Bézier curve.

`p2y`

    

The y-coordinate of the second control point of the cubic Bézier curve.

`duration`

    

The length of time, expressed in seconds, the animation takes to complete.

## Return Value

A cubic Bézier timing curve animation.

## Discussion

Use this method to create a timing curve based on the control points of a
cubic Bézier curve. A cubic Bézier timing curve consists of a line whose
starting point is `(0, 0)` and whose end point is `(1, 1)`. Two additional
control points, `(p1x, p1y)` and `(p2x, p2y)`, define the shape of the curve.

The slope of the line defines the speed of the animation at that point in
time. A steep slopes causes the animation to appear to run faster, while a
shallower slope appears to run slower. The following illustration shows a
timing curve where the animation starts and finishes fast, but appears slower
through the middle section of the animation.

The following code uses the timing curve from the previous illustration to
animate a `Circle` as its size changes.

Play

## See Also

### Creating custom animations

`init<A>(A)`

Create an `Animation` that contains the specified custom animation.

`static func timingCurve(UnitCurve, duration: TimeInterval) -> Animation`

Creates a new animation with speed controlled by the given curve.

Instance Method

# delay(_:)

Delays the start of the animation by the specified number of seconds.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func delay(_ delay: TimeInterval) -> Animation

##  Parameters

`delay`

    

The number of seconds to delay the start of the animation.

## Return Value

An animation with a delayed start.

## Discussion

Use this method to delay the start of an animation. For example, the following
code animates the height change of two capsules. Animation of the first
`Capsule` begins immediately. However, animation of the second one doesn’t
begin until a half second later.

Play

## See Also

### Configuring an animation

`func repeatCount(Int, autoreverses: Bool) -> Animation`

Repeats the animation for a specific number of times.

`func repeatForever(autoreverses: Bool) -> Animation`

Repeats the animation for the lifespan of the view containing the animation.

`func speed(Double) -> Animation`

Changes the duration of an animation by adjusting its speed.

Instance Method

# repeatCount(_:autoreverses:)

Repeats the animation for a specific number of times.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func repeatCount(
        _ repeatCount: Int,
        autoreverses: Bool = true
    ) -> Animation

##  Parameters

`repeatCount`

    

The number of times that the animation repeats. Each repeated sequence starts
at the beginning when `autoreverse` is `false`.

`autoreverses`

    

A Boolean value that indicates whether the animation sequence plays in reverse
after playing forward. Autoreverse counts towards the `repeatCount`. For
instance, a `repeatCount` of one plays the animation forward once, but it
doesn’t play in reverse even if `autoreverse` is `true`. When `autoreverse` is
`true` and `repeatCount` is `2`, the animation moves forward, then reverses,
then stops.

## Return Value

An animation that repeats for specific number of times.

## Discussion

Use this method to repeat the animation a specific number of times. For
example, in the following code, the animation moves a truck from one edge of
the view to the other edge. It repeats this animation three times.

Play

The first time the animation runs, the truck moves from the leading edge to
the trailing edge of the view. The second time the animation runs, the truck
moves from the trailing edge to the leading edge because `autoreverse` is
`true`. If `autoreverse` were `false`, the truck would jump back to leading
edge before moving to the trailing edge. The third time the animation runs,
the truck moves from the leading to the trailing edge of the view.

## See Also

### Configuring an animation

`func delay(TimeInterval) -> Animation`

Delays the start of the animation by the specified number of seconds.

`func repeatForever(autoreverses: Bool) -> Animation`

Repeats the animation for the lifespan of the view containing the animation.

`func speed(Double) -> Animation`

Changes the duration of an animation by adjusting its speed.

Instance Method

# repeatForever(autoreverses:)

Repeats the animation for the lifespan of the view containing the animation.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func repeatForever(autoreverses: Bool = true) -> Animation

##  Parameters

`autoreverses`

    

A Boolean value that indicates whether the animation sequence plays in reverse
after playing forward.

## Return Value

An animation that continuously repeats.

## Discussion

Use this method to repeat the animation until the instance of the view no
longer exists, or the view’s explicit or structural identity changes. For
example, the following code continuously rotates a gear symbol for the
lifespan of the view.

Play

## See Also

### Configuring an animation

`func delay(TimeInterval) -> Animation`

Delays the start of the animation by the specified number of seconds.

`func repeatCount(Int, autoreverses: Bool) -> Animation`

Repeats the animation for a specific number of times.

`func speed(Double) -> Animation`

Changes the duration of an animation by adjusting its speed.

Instance Method

# speed(_:)

Changes the duration of an animation by adjusting its speed.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func speed(_ speed: Double) -> Animation

##  Parameters

`speed`

    

The speed at which SwiftUI performs the animation.

## Return Value

An animation with the adjusted speed.

## Discussion

Setting the speed of an animation changes the duration of the animation by a
factor of `speed`. A higher speed value causes a faster animation sequence due
to a shorter duration. For example, a one-second animation with a speed of
`2.0` completes in half the time (half a second).

Play

Setting `speed` to a lower number slows the animation, extending its duration.
For example, a one-second animation with a speed of `0.25` takes four seconds
to complete.

Play

## See Also

### Configuring an animation

`func delay(TimeInterval) -> Animation`

Delays the start of the animation by the specified number of seconds.

`func repeatCount(Int, autoreverses: Bool) -> Animation`

Repeats the animation for a specific number of times.

`func repeatForever(autoreverses: Bool) -> Animation`

Repeats the animation for the lifespan of the view containing the animation.

Instance Property

# base

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var base: any CustomAnimation { get }

Instance Method

# animate(value:time:context:)

Calculates the current value of the animation.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func animate<V>(
        value: V,
        time: TimeInterval,
        context: inout AnimationContext<V>
    ) -> V? where V : VectorArithmetic

## Return Value

The current value of the animation, or `nil` if the animation has finished.

Instance Method

# logicallyComplete(after:)

Causes the animation to report logical completion after the specified
duration, if it has not already logically completed.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func logicallyComplete(after duration: TimeInterval) -> Animation

##  Parameters

`duration`

    

The duration after which the animation should report that it is logically
complete.

## Return Value

An animation that reports logical completion after the given duration.

## Discussion

Note that the indicated duration will not cause the animation to continue
running after the base animation has fully completed.

If the animation is removed before the given duration is reached, logical
completion will be reported immediately.

Instance Method

# shouldMerge(previous:value:time:context:)

Returns a Boolean value that indicates whether the current animation should
merge with a previous animation.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func shouldMerge<V>(
        previous: Animation,
        value: V,
        time: TimeInterval,
        context: inout AnimationContext<V>
    ) -> Bool where V : VectorArithmetic

Instance Method

# velocity(value:time:context:)

Calculates the current velocity of the animation.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func velocity<V>(
        value: V,
        time: TimeInterval,
        context: AnimationContext<V>
    ) -> V? where V : VectorArithmetic

## Return Value

The current velocity of the animation, or `nil` if the the velocity isn’t
available.

Type Method

# interactiveSpring(duration:extraBounce:blendDuration:)

A convenience for a `spring` animation with a lower `response` value, intended
for driving interactive animations.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static func interactiveSpring(
        duration: TimeInterval = 0.15,
        extraBounce: Double = 0.0,
        blendDuration: TimeInterval = 0.25
    ) -> Animation

