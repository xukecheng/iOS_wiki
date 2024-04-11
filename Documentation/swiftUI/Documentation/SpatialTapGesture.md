Initializer

# init(count:coordinateSpace:)

Creates a tap gesture with the number of required taps and the coordinate
space of the gesture’s location.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  watchOS 10.0+
visionOS 1.0+

    
    
    init(
        count: Int = 1,
        coordinateSpace: some CoordinateSpaceProtocol = .local
    )

##  Parameters

`count`

    

The required number of taps to complete the tap gesture.

`coordinateSpace`

    

The coordinate space of the tap gesture’s location.

## See Also

### Creating a spatial tap gesture

`var coordinateSpace: CoordinateSpace`

The coordinate space in which to receive location values.

`var count: Int`

The required number of tap events.

Instance Property

# coordinateSpace

The coordinate space in which to receive location values.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    var coordinateSpace: CoordinateSpace

## See Also

### Creating a spatial tap gesture

`init(count: Int, coordinateSpace: some CoordinateSpaceProtocol)`

Creates a tap gesture with the number of required taps and the coordinate
space of the gesture’s location.

`var count: Int`

The required number of tap events.

Instance Property

# count

The required number of tap events.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    var count: Int

## See Also

### Creating a spatial tap gesture

`init(count: Int, coordinateSpace: some CoordinateSpaceProtocol)`

Creates a tap gesture with the number of required taps and the coordinate
space of the gesture’s location.

`var coordinateSpace: CoordinateSpace`

The coordinate space in which to receive location values.

Structure

# SpatialTapGesture.Value

The attributes of a tap gesture.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    struct Value

## Topics

### Getting the tap location

`var location: CGPoint`

The location of the tap gesture’s current event.

`var location3D: Point3D`

The 3D location of the tap.

## Relationships

### Conforms To

  * `Equatable`
  * `Sendable`

Initializer

# init(count:coordinateSpace:)

Creates a tap gesture with the number of required taps and the coordinate
space of the gesture’s location.

iOS 16.0–17.4  Deprecated  iPadOS 16.0–17.4  Deprecated  macOS 13.0–14.4
Deprecated  Mac Catalyst 16.0–17.4  Deprecated  watchOS 9.0–10.4  Deprecated
visionOS 1.0+

    
    
    init(
        count: Int = 1,
        coordinateSpace: CoordinateSpace = .local
    )

Deprecated

Use `init(count:coordinateSpace:)` instead.

##  Parameters

`count`

    

The required number of taps to complete the tap gesture.

`coordinateSpace`

    

The coordinate space of the tap gesture’s location.

