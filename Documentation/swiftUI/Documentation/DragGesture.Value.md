Instance Property

# startLocation

The location of the drag gesture’s first event.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    var startLocation: CGPoint

## See Also

### Getting 2D position

`var location: CGPoint`

The location of the drag gesture’s current event.

`var predictedEndLocation: CGPoint`

A prediction, based on the current drag velocity, of where the final location
will be if dragging stopped now.

`var translation: CGSize`

The total translation from the start of the drag gesture to the current event
of the drag gesture.

`var predictedEndTranslation: CGSize`

A prediction, based on the current drag velocity, of what the final
translation will be if dragging stopped now.

Instance Property

# location

The location of the drag gesture’s current event.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    var location: CGPoint

## See Also

### Getting 2D position

`var startLocation: CGPoint`

The location of the drag gesture’s first event.

`var predictedEndLocation: CGPoint`

A prediction, based on the current drag velocity, of where the final location
will be if dragging stopped now.

`var translation: CGSize`

The total translation from the start of the drag gesture to the current event
of the drag gesture.

`var predictedEndTranslation: CGSize`

A prediction, based on the current drag velocity, of what the final
translation will be if dragging stopped now.

Instance Property

# predictedEndLocation

A prediction, based on the current drag velocity, of where the final location
will be if dragging stopped now.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    var predictedEndLocation: CGPoint { get }

## See Also

### Getting 2D position

`var startLocation: CGPoint`

The location of the drag gesture’s first event.

`var location: CGPoint`

The location of the drag gesture’s current event.

`var translation: CGSize`

The total translation from the start of the drag gesture to the current event
of the drag gesture.

`var predictedEndTranslation: CGSize`

A prediction, based on the current drag velocity, of what the final
translation will be if dragging stopped now.

Instance Property

# translation

The total translation from the start of the drag gesture to the current event
of the drag gesture.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    var translation: CGSize { get }

## Discussion

This is equivalent to `location.{x,y} - startLocation.{x,y}`.

## See Also

### Getting 2D position

`var startLocation: CGPoint`

The location of the drag gesture’s first event.

`var location: CGPoint`

The location of the drag gesture’s current event.

`var predictedEndLocation: CGPoint`

A prediction, based on the current drag velocity, of where the final location
will be if dragging stopped now.

`var predictedEndTranslation: CGSize`

A prediction, based on the current drag velocity, of what the final
translation will be if dragging stopped now.

Instance Property

# predictedEndTranslation

A prediction, based on the current drag velocity, of what the final
translation will be if dragging stopped now.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    var predictedEndTranslation: CGSize { get }

## See Also

### Getting 2D position

`var startLocation: CGPoint`

The location of the drag gesture’s first event.

`var location: CGPoint`

The location of the drag gesture’s current event.

`var predictedEndLocation: CGPoint`

A prediction, based on the current drag velocity, of where the final location
will be if dragging stopped now.

`var translation: CGSize`

The total translation from the start of the drag gesture to the current event
of the drag gesture.

Instance Property

# startLocation3D

The 3D start location of the drag gesture.

visionOS 1.0+

    
    
    var startLocation3D: Point3D { get }

## See Also

### Getting 3D position

`var location3D: Point3D`

The 3D location of the drag gesture.

`var predictedEndLocation3D: Point3D`

A prediction of where the final location would be if dragging stopped now,
based on the current drag velocity.

`var translation3D: Vector3D`

The translation of the drag gesture from `startLocation3D` to `location3D`.

`var predictedEndTranslation3D: Vector3D`

A prediction of what the final translation would be if dragging stopped now,
based on the current drag velocity.

`var startInputDevicePose3D: Pose3D?`

The starting 3D pose of the device driving the drag, if one exists.

`var inputDevicePose3D: Pose3D?`

The 3D pose of the device driving the drag, if one exists.

Instance Property

# location3D

The 3D location of the drag gesture.

visionOS 1.0+

    
    
    var location3D: Point3D { get }

## See Also

### Getting 3D position

`var startLocation3D: Point3D`

The 3D start location of the drag gesture.

`var predictedEndLocation3D: Point3D`

A prediction of where the final location would be if dragging stopped now,
based on the current drag velocity.

`var translation3D: Vector3D`

The translation of the drag gesture from `startLocation3D` to `location3D`.

`var predictedEndTranslation3D: Vector3D`

A prediction of what the final translation would be if dragging stopped now,
based on the current drag velocity.

`var startInputDevicePose3D: Pose3D?`

The starting 3D pose of the device driving the drag, if one exists.

`var inputDevicePose3D: Pose3D?`

The 3D pose of the device driving the drag, if one exists.

Instance Property

# predictedEndLocation3D

A prediction of where the final location would be if dragging stopped now,
based on the current drag velocity.

visionOS 1.0+

    
    
    var predictedEndLocation3D: Point3D { get }

## See Also

### Getting 3D position

`var startLocation3D: Point3D`

The 3D start location of the drag gesture.

`var location3D: Point3D`

The 3D location of the drag gesture.

`var translation3D: Vector3D`

The translation of the drag gesture from `startLocation3D` to `location3D`.

`var predictedEndTranslation3D: Vector3D`

A prediction of what the final translation would be if dragging stopped now,
based on the current drag velocity.

`var startInputDevicePose3D: Pose3D?`

The starting 3D pose of the device driving the drag, if one exists.

`var inputDevicePose3D: Pose3D?`

The 3D pose of the device driving the drag, if one exists.

Instance Property

# translation3D

The translation of the drag gesture from `startLocation3D` to `location3D`.

visionOS 1.0+

    
    
    var translation3D: Vector3D { get }

## See Also

### Getting 3D position

`var startLocation3D: Point3D`

The 3D start location of the drag gesture.

`var location3D: Point3D`

The 3D location of the drag gesture.

`var predictedEndLocation3D: Point3D`

A prediction of where the final location would be if dragging stopped now,
based on the current drag velocity.

`var predictedEndTranslation3D: Vector3D`

A prediction of what the final translation would be if dragging stopped now,
based on the current drag velocity.

`var startInputDevicePose3D: Pose3D?`

The starting 3D pose of the device driving the drag, if one exists.

`var inputDevicePose3D: Pose3D?`

The 3D pose of the device driving the drag, if one exists.

Instance Property

# predictedEndTranslation3D

A prediction of what the final translation would be if dragging stopped now,
based on the current drag velocity.

visionOS 1.0+

    
    
    var predictedEndTranslation3D: Vector3D { get }

## See Also

### Getting 3D position

`var startLocation3D: Point3D`

The 3D start location of the drag gesture.

`var location3D: Point3D`

The 3D location of the drag gesture.

`var predictedEndLocation3D: Point3D`

A prediction of where the final location would be if dragging stopped now,
based on the current drag velocity.

`var translation3D: Vector3D`

The translation of the drag gesture from `startLocation3D` to `location3D`.

`var startInputDevicePose3D: Pose3D?`

The starting 3D pose of the device driving the drag, if one exists.

`var inputDevicePose3D: Pose3D?`

The 3D pose of the device driving the drag, if one exists.

Instance Property

# startInputDevicePose3D

The starting 3D pose of the device driving the drag, if one exists.

visionOS 1.0+

    
    
    var startInputDevicePose3D: Pose3D? { get }

## See Also

### Getting 3D position

`var startLocation3D: Point3D`

The 3D start location of the drag gesture.

`var location3D: Point3D`

The 3D location of the drag gesture.

`var predictedEndLocation3D: Point3D`

A prediction of where the final location would be if dragging stopped now,
based on the current drag velocity.

`var translation3D: Vector3D`

The translation of the drag gesture from `startLocation3D` to `location3D`.

`var predictedEndTranslation3D: Vector3D`

A prediction of what the final translation would be if dragging stopped now,
based on the current drag velocity.

`var inputDevicePose3D: Pose3D?`

The 3D pose of the device driving the drag, if one exists.

Instance Property

# inputDevicePose3D

The 3D pose of the device driving the drag, if one exists.

visionOS 1.0+

    
    
    var inputDevicePose3D: Pose3D? { get }

## See Also

### Getting 3D position

`var startLocation3D: Point3D`

The 3D start location of the drag gesture.

`var location3D: Point3D`

The 3D location of the drag gesture.

`var predictedEndLocation3D: Point3D`

A prediction of where the final location would be if dragging stopped now,
based on the current drag velocity.

`var translation3D: Vector3D`

The translation of the drag gesture from `startLocation3D` to `location3D`.

`var predictedEndTranslation3D: Vector3D`

A prediction of what the final translation would be if dragging stopped now,
based on the current drag velocity.

`var startInputDevicePose3D: Pose3D?`

The starting 3D pose of the device driving the drag, if one exists.

Instance Property

# time

The time associated with the drag gesture’s current event.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    var time: Date

## See Also

### Handling changes over time

`var velocity: CGSize`

The current drag velocity.

Instance Property

# velocity

The current drag velocity.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    var velocity: CGSize { get }

## See Also

### Handling changes over time

`var time: Date`

The time associated with the drag gesture’s current event.

