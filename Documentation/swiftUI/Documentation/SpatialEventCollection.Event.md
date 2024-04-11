Instance Property

# timestamp

The time the event was processed.

visionOS 1.0+

    
    
    var timestamp: TimeInterval

## See Also

### Identifying the event

`var id: SpatialEventCollection.Event.ID`

An identifier that uniquely identifies the event over its lifetime.

`struct ID`

A value that uniquely identifies an event over the course of its lifetime.

`var kind: SpatialEventCollection.Event.Kind`

The event’s input source.

`enum Kind`

The possible input sources or modes of an event.

`var modifierKeys: EventModifiers`

The set of active modifier keys at the time of this event.

Instance Property

# id

An identifier that uniquely identifies the event over its lifetime.

visionOS 1.0+

    
    
    var id: SpatialEventCollection.Event.ID

## See Also

### Identifying the event

`var timestamp: TimeInterval`

The time the event was processed.

`struct ID`

A value that uniquely identifies an event over the course of its lifetime.

`var kind: SpatialEventCollection.Event.Kind`

The event’s input source.

`enum Kind`

The possible input sources or modes of an event.

`var modifierKeys: EventModifiers`

The set of active modifier keys at the time of this event.

Structure

# SpatialEventCollection.Event.ID

A value that uniquely identifies an event over the course of its lifetime.

visionOS 1.0+

    
    
    struct ID

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`

## See Also

### Identifying the event

`var timestamp: TimeInterval`

The time the event was processed.

`var id: SpatialEventCollection.Event.ID`

An identifier that uniquely identifies the event over its lifetime.

`var kind: SpatialEventCollection.Event.Kind`

The event’s input source.

`enum Kind`

The possible input sources or modes of an event.

`var modifierKeys: EventModifiers`

The set of active modifier keys at the time of this event.

Instance Property

# kind

The event’s input source.

visionOS 1.0+

    
    
    var kind: SpatialEventCollection.Event.Kind

## See Also

### Identifying the event

`var timestamp: TimeInterval`

The time the event was processed.

`var id: SpatialEventCollection.Event.ID`

An identifier that uniquely identifies the event over its lifetime.

`struct ID`

A value that uniquely identifies an event over the course of its lifetime.

`enum Kind`

The possible input sources or modes of an event.

`var modifierKeys: EventModifiers`

The set of active modifier keys at the time of this event.

Enumeration

# SpatialEventCollection.Event.Kind

The possible input sources or modes of an event.

visionOS 1.0+

    
    
    enum Kind

## Topics

### Getting the event type

`case directPinch`

An event generated from a pinching hand in close proximity to content.

`case indirectPinch`

An event generated from an indirectly targeted pinching hand.

`case pointer`

An event representing a click-based, indirect input device describing the
input sequence from click to click release.

`case touch`

An event generated from a touch directly targeting content.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`

## See Also

### Identifying the event

`var timestamp: TimeInterval`

The time the event was processed.

`var id: SpatialEventCollection.Event.ID`

An identifier that uniquely identifies the event over its lifetime.

`struct ID`

A value that uniquely identifies an event over the course of its lifetime.

`var kind: SpatialEventCollection.Event.Kind`

The event’s input source.

`var modifierKeys: EventModifiers`

The set of active modifier keys at the time of this event.

Instance Property

# modifierKeys

The set of active modifier keys at the time of this event.

visionOS 1.0+

    
    
    var modifierKeys: EventModifiers

## See Also

### Identifying the event

`var timestamp: TimeInterval`

The time the event was processed.

`var id: SpatialEventCollection.Event.ID`

An identifier that uniquely identifies the event over its lifetime.

`struct ID`

A value that uniquely identifies an event over the course of its lifetime.

`var kind: SpatialEventCollection.Event.Kind`

The event’s input source.

`enum Kind`

The possible input sources or modes of an event.

Instance Property

# location

The 2D location of the event.

visionOS 1.0+

    
    
    var location: CGPoint

## See Also

### Locating the event

`var location3D: Point3D`

The 3D location of the touch.

`var selectionRay: Ray3D?`

The 3D ray used to target the touch.

`var inputDevicePose: SpatialEventCollection.Event.InputDevicePose?`

The 3D position and orientation of the device controlling the touch, if one
exists.

`struct InputDevicePose`

A pose describing the input device like a hand controlling the event.

`var targetedEntity: Entity?`

The entity target for this touch, if one exists.

Instance Property

# location3D

The 3D location of the touch.

visionOS 1.0+

    
    
    var location3D: Point3D

## See Also

### Locating the event

`var location: CGPoint`

The 2D location of the event.

`var selectionRay: Ray3D?`

The 3D ray used to target the touch.

`var inputDevicePose: SpatialEventCollection.Event.InputDevicePose?`

The 3D position and orientation of the device controlling the touch, if one
exists.

`struct InputDevicePose`

A pose describing the input device like a hand controlling the event.

`var targetedEntity: Entity?`

The entity target for this touch, if one exists.

Instance Property

# selectionRay

The 3D ray used to target the touch.

visionOS 1.0+

    
    
    var selectionRay: Ray3D?

## See Also

### Locating the event

`var location: CGPoint`

The 2D location of the event.

`var location3D: Point3D`

The 3D location of the touch.

`var inputDevicePose: SpatialEventCollection.Event.InputDevicePose?`

The 3D position and orientation of the device controlling the touch, if one
exists.

`struct InputDevicePose`

A pose describing the input device like a hand controlling the event.

`var targetedEntity: Entity?`

The entity target for this touch, if one exists.

Instance Property

# inputDevicePose

The 3D position and orientation of the device controlling the touch, if one
exists.

visionOS 1.0+

    
    
    var inputDevicePose: SpatialEventCollection.Event.InputDevicePose? { get set }

## See Also

### Locating the event

`var location: CGPoint`

The 2D location of the event.

`var location3D: Point3D`

The 3D location of the touch.

`var selectionRay: Ray3D?`

The 3D ray used to target the touch.

`struct InputDevicePose`

A pose describing the input device like a hand controlling the event.

`var targetedEntity: Entity?`

The entity target for this touch, if one exists.

Structure

# SpatialEventCollection.Event.InputDevicePose

A pose describing the input device like a hand controlling the event.

visionOS 1.0+

    
    
    struct InputDevicePose

## Topics

### Getting the event type

`var altitude: Angle`

The altitude angle.

`var azimuth: Angle`

The azimuth angle.

`var pose3D: Pose3D`

The 3D pose of the input device.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`

## See Also

### Locating the event

`var location: CGPoint`

The 2D location of the event.

`var location3D: Point3D`

The 3D location of the touch.

`var selectionRay: Ray3D?`

The 3D ray used to target the touch.

`var inputDevicePose: SpatialEventCollection.Event.InputDevicePose?`

The 3D position and orientation of the device controlling the touch, if one
exists.

`var targetedEntity: Entity?`

The entity target for this touch, if one exists.

Instance Property

# targetedEntity

The entity target for this touch, if one exists.

visionOS 1.0+

    
    
    var targetedEntity: Entity?

## See Also

### Locating the event

`var location: CGPoint`

The 2D location of the event.

`var location3D: Point3D`

The 3D location of the touch.

`var selectionRay: Ray3D?`

The 3D ray used to target the touch.

`var inputDevicePose: SpatialEventCollection.Event.InputDevicePose?`

The 3D position and orientation of the device controlling the touch, if one
exists.

`struct InputDevicePose`

A pose describing the input device like a hand controlling the event.

Instance Property

# phase

The phase of the event.

visionOS 1.0+

    
    
    var phase: SpatialEventCollection.Event.Phase

## See Also

### Getting the event’s current phase

`enum Phase`

The states that an event can have.

Enumeration

# SpatialEventCollection.Event.Phase

The states that an event can have.

visionOS 1.0+

    
    
    enum Phase

## Topics

### Getting the phase

`case active`

The phase is active and the state associated with it is guaranteed to produce
at least one more update.

`case cancelled`

The state associated with this phase was canceled and won’t produce any more
updates.

`case ended`

The state associated with this phase ended normally and won’t produce any more
updates.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`

## See Also

### Getting the event’s current phase

`var phase: SpatialEventCollection.Event.Phase`

The phase of the event.

