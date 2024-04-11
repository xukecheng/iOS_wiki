Initializer

# init(duration:bounce:)

Creates a spring with the specified duration and bounce.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init(
        duration: TimeInterval = 0.5,
        bounce: Double = 0.0
    )

##  Parameters

`duration`

    

Defines the pace of the spring. This is approximately equal to the settling
duration, but for springs with very large bounce values, will be the duration
of the period of oscillation for the spring.

`bounce`

    

How bouncy the spring should be. A value of 0 indicates no bounces (a
critically damped spring), positive values indicate increasing amounts of
bounciness up to a maximum of 1.0 (corresponding to undamped oscillation), and
negative values indicate overdamped springs with a minimum value of -1.0.

## See Also

### Creating a spring

`init(mass: Double, stiffness: Double, damping: Double, allowOverDamping:
Bool)`

Creates a spring with the specified mass, stiffness, and damping.

`init(response: Double, dampingRatio: Double)`

Creates a spring with the specified response and damping ratio.

`init(settlingDuration: TimeInterval, dampingRatio: Double, epsilon: Double)`

Creates a spring with the specified duration and damping ratio.

Initializer

# init(mass:stiffness:damping:allowOverDamping:)

Creates a spring with the specified mass, stiffness, and damping.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init(
        mass: Double = 1.0,
        stiffness: Double,
        damping: Double,
        allowOverDamping: Bool = false
    )

##  Parameters

`mass`

    

Specifies that property of the object attached to the end of the spring.

`stiffness`

    

The corresponding spring coefficient.

`damping`

    

Defines how the spring’s motion should be damped due to the forces of
friction.

`allowOverdamping`

    

A value of true specifies that over-damping should be allowed when appropriate
based on the other inputs, and a value of false specifies that such cases
should instead be treated as critically damped.

## See Also

### Creating a spring

`init(duration: TimeInterval, bounce: Double)`

Creates a spring with the specified duration and bounce.

`init(response: Double, dampingRatio: Double)`

Creates a spring with the specified response and damping ratio.

`init(settlingDuration: TimeInterval, dampingRatio: Double, epsilon: Double)`

Creates a spring with the specified duration and damping ratio.

Initializer

# init(response:dampingRatio:)

Creates a spring with the specified response and damping ratio.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init(
        response: Double,
        dampingRatio: Double
    )

##  Parameters

`response`

    

Defines the stiffness of the spring as an approximate duration in seconds.

`dampingRatio`

    

Defines the amount of drag applied as a fraction the amount needed to produce
critical damping.

## See Also

### Creating a spring

`init(duration: TimeInterval, bounce: Double)`

Creates a spring with the specified duration and bounce.

`init(mass: Double, stiffness: Double, damping: Double, allowOverDamping:
Bool)`

Creates a spring with the specified mass, stiffness, and damping.

`init(settlingDuration: TimeInterval, dampingRatio: Double, epsilon: Double)`

Creates a spring with the specified duration and damping ratio.

Initializer

# init(settlingDuration:dampingRatio:epsilon:)

Creates a spring with the specified duration and damping ratio.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init(
        settlingDuration: TimeInterval,
        dampingRatio: Double,
        epsilon: Double = 0.001
    )

##  Parameters

`settlingDuration`

    

The approximate time it will take for the spring to come to rest.

`dampingRatio`

    

The amount of drag applied as a fraction of the amount needed to produce
critical damping.

`epsilon`

    

The threshhold for how small all subsequent values need to be before the
spring is considered to have settled.

## See Also

### Creating a spring

`init(duration: TimeInterval, bounce: Double)`

Creates a spring with the specified duration and bounce.

`init(mass: Double, stiffness: Double, damping: Double, allowOverDamping:
Bool)`

Creates a spring with the specified mass, stiffness, and damping.

`init(response: Double, dampingRatio: Double)`

Creates a spring with the specified response and damping ratio.

Type Property

# bouncy

A spring with a predefined duration and higher amount of bounce.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static var bouncy: Spring { get }

## See Also

### Getting built-in springs

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

Type Method

# bouncy(duration:extraBounce:)

A spring with a predefined duration and higher amount of bounce that can be
tuned.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static func bouncy(
        duration: TimeInterval = 0.5,
        extraBounce: Double = 0.0
    ) -> Spring

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

### Getting built-in springs

`static var bouncy: Spring`

A spring with a predefined duration and higher amount of bounce.

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

Type Property

# smooth

A smooth spring with a predefined duration and no bounce.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static var smooth: Spring { get }

## See Also

### Getting built-in springs

`static var bouncy: Spring`

A spring with a predefined duration and higher amount of bounce.

`static func bouncy(duration: TimeInterval, extraBounce: Double) -> Spring`

A spring with a predefined duration and higher amount of bounce that can be
tuned.

`static func smooth(duration: TimeInterval, extraBounce: Double) -> Spring`

A smooth spring with a predefined duration and no bounce that can be tuned.

`static var snappy: Spring`

A spring with a predefined duration and small amount of bounce that feels more
snappy.

`static func snappy(duration: TimeInterval, extraBounce: Double) -> Spring`

A spring with a predefined duration and small amount of bounce that feels more
snappy and can be tuned.

Type Method

# smooth(duration:extraBounce:)

A smooth spring with a predefined duration and no bounce that can be tuned.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static func smooth(
        duration: TimeInterval = 0.5,
        extraBounce: Double = 0.0
    ) -> Spring

##  Parameters

`duration`

    

The perceptual duration, which defines the pace of the spring. This is
approximately equal to the settling duration, but for very bouncy springs,
will be the duration of the period of oscillation for the spring.

`extraBounce`

    

How much additional bounce should be added to the base bounce of 0.

## See Also

### Getting built-in springs

`static var bouncy: Spring`

A spring with a predefined duration and higher amount of bounce.

`static func bouncy(duration: TimeInterval, extraBounce: Double) -> Spring`

A spring with a predefined duration and higher amount of bounce that can be
tuned.

`static var smooth: Spring`

A smooth spring with a predefined duration and no bounce.

`static var snappy: Spring`

A spring with a predefined duration and small amount of bounce that feels more
snappy.

`static func snappy(duration: TimeInterval, extraBounce: Double) -> Spring`

A spring with a predefined duration and small amount of bounce that feels more
snappy and can be tuned.

Type Property

# snappy

A spring with a predefined duration and small amount of bounce that feels more
snappy.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static var snappy: Spring { get }

## See Also

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

`static func snappy(duration: TimeInterval, extraBounce: Double) -> Spring`

A spring with a predefined duration and small amount of bounce that feels more
snappy and can be tuned.

Type Method

# snappy(duration:extraBounce:)

A spring with a predefined duration and small amount of bounce that feels more
snappy and can be tuned.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static func snappy(
        duration: TimeInterval = 0.5,
        extraBounce: Double = 0.0
    ) -> Spring

##  Parameters

`duration`

    

The perceptual duration, which defines the pace of the spring. This is
approximately equal to the settling duration, but for very bouncy springs,
will be the duration of the period of oscillation for the spring.

`extraBounce`

    

How much additional bounciness should be added to the base bounce of 0.15.

## See Also

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

Instance Property

# bounce

How bouncy the spring is.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var bounce: Double { get }

## Discussion

A value of 0 indicates no bounces (a critically damped spring), positive
values indicate increasing amounts of bounciness up to a maximum of 1.0
(corresponding to undamped oscillation), and negative values indicate
overdamped springs with a minimum value of -1.0.

## See Also

### Getting spring characteristics

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

Instance Property

# damping

Defines how the spring’s motion should be damped due to the forces of
friction.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var damping: Double { get }

## Discussion

Reducing this value reduces the energy loss with each oscillation: the spring
will overshoot its destination. Increasing the value increases the energy loss
with each duration: there will be fewer and smaller oscillations.

## See Also

### Getting spring characteristics

`var bounce: Double`

How bouncy the spring is.

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

Instance Property

# dampingRatio

The amount of drag applied, as a fraction of the amount needed to produce
critical damping.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var dampingRatio: Double { get }

## Discussion

When `dampingRatio` is 1, the spring will smoothly decelerate to its final
position without oscillating. Damping ratios less than 1 will oscillate more
and more before coming to a complete stop.

## See Also

### Getting spring characteristics

`var bounce: Double`

How bouncy the spring is.

`var damping: Double`

Defines how the spring’s motion should be damped due to the forces of
friction.

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

Instance Property

# duration

The perceptual duration, which defines the pace of the spring.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var duration: TimeInterval { get }

## See Also

### Getting spring characteristics

`var bounce: Double`

How bouncy the spring is.

`var damping: Double`

Defines how the spring’s motion should be damped due to the forces of
friction.

`var dampingRatio: Double`

The amount of drag applied, as a fraction of the amount needed to produce
critical damping.

`var mass: Double`

The mass of the object attached to the end of the spring.

`var response: Double`

The stiffness of the spring, defined as an approximate duration in seconds.

`var settlingDuration: TimeInterval`

The estimated duration required for the spring system to be considered at
rest.

`var stiffness: Double`

The spring stiffness coefficient.

Instance Property

# mass

The mass of the object attached to the end of the spring.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var mass: Double { get }

## Discussion

The default mass is 1. Increasing this value will increase the spring’s
effect: the attached object will be subject to more oscillations and greater
overshoot, resulting in an increased settling duration. Decreasing the mass
will reduce the spring effect: there will be fewer oscillations and a reduced
overshoot, resulting in a decreased settling duration.

## See Also

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

`var response: Double`

The stiffness of the spring, defined as an approximate duration in seconds.

`var settlingDuration: TimeInterval`

The estimated duration required for the spring system to be considered at
rest.

`var stiffness: Double`

The spring stiffness coefficient.

Instance Property

# response

The stiffness of the spring, defined as an approximate duration in seconds.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var response: Double { get }

## See Also

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

`var settlingDuration: TimeInterval`

The estimated duration required for the spring system to be considered at
rest.

`var stiffness: Double`

The spring stiffness coefficient.

Instance Property

# settlingDuration

The estimated duration required for the spring system to be considered at
rest.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var settlingDuration: TimeInterval { get }

## Discussion

This uses a `target` of 1.0, an `initialVelocity` of 0, and an `epsilon` of
0.001.

## See Also

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

`var stiffness: Double`

The spring stiffness coefficient.

Instance Property

# stiffness

The spring stiffness coefficient.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var stiffness: Double { get }

## Discussion

Increasing the stiffness reduces the number of oscillations and will reduce
the settling duration. Decreasing the stiffness increases the the number of
oscillations and will increase the settling duration.

## See Also

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

Instance Method

# value(target:initialVelocity:time:)

Calculates the value of the spring at a given time given a target amount of
change.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func value<V>(
        target: V,
        initialVelocity: V = .zero,
        time: TimeInterval
    ) -> V where V : VectorArithmetic

## See Also

### Getting spring state

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

Instance Method

# value(fromValue:toValue:initialVelocity:time:)

Calculates the value of the spring at a given time for a starting and ending
value for the spring to travel.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func value<V>(
        fromValue: V,
        toValue: V,
        initialVelocity: V,
        time: TimeInterval
    ) -> V where V : Animatable

## See Also

### Getting spring state

`func value<V>(target: V, initialVelocity: V, time: TimeInterval) -> V`

Calculates the value of the spring at a given time given a target amount of
change.

`func velocity<V>(target: V, initialVelocity: V, time: TimeInterval) -> V`

Calculates the velocity of the spring at a given time given a target amount of
change.

`func velocity<V>(fromValue: V, toValue: V, initialVelocity: V, time:
TimeInterval) -> V`

Calculates the velocity of the spring at a given time given a starting and
ending value for the spring to travel.

Instance Method

# velocity(target:initialVelocity:time:)

Calculates the velocity of the spring at a given time given a target amount of
change.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func velocity<V>(
        target: V,
        initialVelocity: V = .zero,
        time: TimeInterval
    ) -> V where V : VectorArithmetic

## See Also

### Getting spring state

`func value<V>(target: V, initialVelocity: V, time: TimeInterval) -> V`

Calculates the value of the spring at a given time given a target amount of
change.

`func value<V>(fromValue: V, toValue: V, initialVelocity: V, time:
TimeInterval) -> V`

Calculates the value of the spring at a given time for a starting and ending
value for the spring to travel.

`func velocity<V>(fromValue: V, toValue: V, initialVelocity: V, time:
TimeInterval) -> V`

Calculates the velocity of the spring at a given time given a starting and
ending value for the spring to travel.

Instance Method

# velocity(fromValue:toValue:initialVelocity:time:)

Calculates the velocity of the spring at a given time given a starting and
ending value for the spring to travel.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func velocity<V>(
        fromValue: V,
        toValue: V,
        initialVelocity: V,
        time: TimeInterval
    ) -> V where V : Animatable

## See Also

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

Instance Method

# update(value:velocity:target:deltaTime:)

Updates the current value and velocity of a spring.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func update<V>(
        value: inout V,
        velocity: inout V,
        target: V,
        deltaTime: TimeInterval
    ) where V : VectorArithmetic

##  Parameters

`value`

    

The current value of the spring.

`velocity`

    

The current velocity of the spring.

`target`

    

The target that `value` is moving towards.

`deltaTime`

    

The amount of time that has passed since the spring was at the position
specified by `value`.

Instance Method

# force(target:position:velocity:)

Calculates the force upon the spring given a current position, target, and
velocity amount of change.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func force<V>(
        target: V,
        position: V,
        velocity: V
    ) -> V where V : VectorArithmetic

## Discussion

This value is in units of the vector type per second squared.

## See Also

### Calculating forces and durations

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

Instance Method

# force(fromValue:toValue:position:velocity:)

Calculates the force upon the spring given a current position, velocity, and
divisor from the starting and end values for the spring to travel.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func force<V>(
        fromValue: V,
        toValue: V,
        position: V,
        velocity: V
    ) -> V where V : Animatable

## Discussion

This value is in units of the vector type per second squared.

## See Also

### Calculating forces and durations

`func force<V>(target: V, position: V, velocity: V) -> V`

Calculates the force upon the spring given a current position, target, and
velocity amount of change.

`func settlingDuration<V>(target: V, initialVelocity: V, epsilon: Double) ->
TimeInterval`

The estimated duration required for the spring system to be considered at
rest.

`func settlingDuration<V>(fromValue: V, toValue: V, initialVelocity: V,
epsilon: Double) -> TimeInterval`

The estimated duration required for the spring system to be considered at
rest.

Instance Method

# settlingDuration(target:initialVelocity:epsilon:)

The estimated duration required for the spring system to be considered at
rest.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func settlingDuration<V>(
        target: V,
        initialVelocity: V = .zero,
        epsilon: Double
    ) -> TimeInterval where V : VectorArithmetic

## Discussion

The epsilon value specifies the threshhold for how small all subsequent values
need to be before the spring is considered to have settled.

## See Also

### Calculating forces and durations

`func force<V>(target: V, position: V, velocity: V) -> V`

Calculates the force upon the spring given a current position, target, and
velocity amount of change.

`func force<V>(fromValue: V, toValue: V, position: V, velocity: V) -> V`

Calculates the force upon the spring given a current position, velocity, and
divisor from the starting and end values for the spring to travel.

`func settlingDuration<V>(fromValue: V, toValue: V, initialVelocity: V,
epsilon: Double) -> TimeInterval`

The estimated duration required for the spring system to be considered at
rest.

Instance Method

# settlingDuration(fromValue:toValue:initialVelocity:epsilon:)

The estimated duration required for the spring system to be considered at
rest.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func settlingDuration<V>(
        fromValue: V,
        toValue: V,
        initialVelocity: V,
        epsilon: Double
    ) -> TimeInterval where V : Animatable

## Discussion

The epsilon value specifies the threshhold for how small all subsequent values
need to be before the spring is considered to have settled.

## See Also

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

