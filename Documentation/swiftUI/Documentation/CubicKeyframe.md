Initializer

# init(_:duration:startVelocity:endVelocity:)

Creates a new keyframe using the given value and timestamp.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init(
        _ to: Value,
        duration: TimeInterval,
        startVelocity: Value? = nil,
        endVelocity: Value? = nil
    )

##  Parameters

`to`

    

The value of the keyframe.

`startVelocity`

    

The velocity of the value at the beginning of the segment, or `nil` to
automatically compute the velocity to maintain smooth motion.

`endVelocity`

    

The velocity of the value at the end of the segment, or `nil` to automatically
compute the velocity to maintain smooth motion.

`duration`

    

The duration of the segment defined by this keyframe.

