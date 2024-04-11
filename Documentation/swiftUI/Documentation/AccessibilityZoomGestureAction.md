Instance Property

# direction

The zoom gesture’s direction.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    let direction: AccessibilityZoomGestureAction.Direction

## See Also

### Getting the action’s direction

`enum Direction`

A direction that matches the movement of a zoom gesture performed by an
assistive technology, such as a swipe up and down in Voiceover’s zoom rotor.

Enumeration

# AccessibilityZoomGestureAction.Direction

A direction that matches the movement of a zoom gesture performed by an
assistive technology, such as a swipe up and down in Voiceover’s zoom rotor.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    @frozen
    enum Direction

## Topics

### Getting the direction

`case zoomIn`

The gesture direction that represents zooming in.

`case zoomOut`

The gesture direction that represents zooming out.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Getting the action’s direction

`let direction: AccessibilityZoomGestureAction.Direction`

The zoom gesture’s direction.

Instance Property

# location

The zoom gesture’s activation point, normalized to the accessibility element’s
frame.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    let location: UnitPoint

## See Also

### Getting location information

`let point: CGPoint`

The zoom gesture’s activation point within the window’s coordinate space.

Instance Property

# point

The zoom gesture’s activation point within the window’s coordinate space.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    let point: CGPoint

## See Also

### Getting location information

`let location: UnitPoint`

The zoom gesture’s activation point, normalized to the accessibility element’s
frame.

