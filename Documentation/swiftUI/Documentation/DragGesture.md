Initializer

# init(minimumDistance:coordinateSpace:)

Creates a dragging gesture with the minimum dragging distance before the
gesture succeeds and the coordinate space of the gesture’s location.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  watchOS 10.0+
visionOS 1.0+

    
    
    init(
        minimumDistance: CGFloat = 10,
        coordinateSpace: some CoordinateSpaceProtocol = .local
    )

##  Parameters

`minimumDistance`

    

The minimum dragging distance for the gesture to succeed.

`coordinateSpace`

    

The coordinate space of the dragging gesture’s location.

## See Also

### Creating a drag gesture

`var minimumDistance: CGFloat`

The minimum dragging distance before the gesture succeeds.

`var coordinateSpace: CoordinateSpace`

The coordinate space in which to receive location values.

Instance Property

# minimumDistance

The minimum dragging distance before the gesture succeeds.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    var minimumDistance: CGFloat

## See Also

### Creating a drag gesture

`init(minimumDistance: CGFloat, coordinateSpace: some
CoordinateSpaceProtocol)`

Creates a dragging gesture with the minimum dragging distance before the
gesture succeeds and the coordinate space of the gesture’s location.

`var coordinateSpace: CoordinateSpace`

The coordinate space in which to receive location values.

Instance Property

# coordinateSpace

The coordinate space in which to receive location values.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    var coordinateSpace: CoordinateSpace

## See Also

### Creating a drag gesture

`init(minimumDistance: CGFloat, coordinateSpace: some
CoordinateSpaceProtocol)`

Creates a dragging gesture with the minimum dragging distance before the
gesture succeeds and the coordinate space of the gesture’s location.

`var minimumDistance: CGFloat`

The minimum dragging distance before the gesture succeeds.

Initializer

# init(minimumDistance:coordinateSpace:)

Creates a dragging gesture with the minimum dragging distance before the
gesture succeeds and the coordinate space of the gesture’s location.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  watchOS 6.0–10.4  Deprecated
visionOS 1.0+

    
    
    init(
        minimumDistance: CGFloat = 10,
        coordinateSpace: CoordinateSpace = .local
    )

Deprecated

Use `init(minimumDistance:coordinateSpace:)` instead.

##  Parameters

`minimumDistance`

    

The minimum dragging distance for the gesture to succeed.

`coordinateSpace`

    

The coordinate space of the dragging gesture’s location.

Structure

# DragGesture.Value

The attributes of a drag gesture.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    struct Value

## Topics

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

`var predictedEndTranslation: CGSize`

A prediction, based on the current drag velocity, of what the final
translation will be if dragging stopped now.

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

`var inputDevicePose3D: Pose3D?`

The 3D pose of the device driving the drag, if one exists.

### Handling changes over time

`var time: Date`

The time associated with the drag gesture’s current event.

`var velocity: CGSize`

The current drag velocity.

## Relationships

### Conforms To

  * `Equatable`
  * `Sendable`

