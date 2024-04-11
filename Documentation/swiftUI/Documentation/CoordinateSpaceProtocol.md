Type Property

# immersiveSpace

The named coordinate space that represents the currently opened
`ImmersiveSpace` scene. If no immersive space is currently opened, this
CoordinateSpace provides the same behavior as the `.global` coordinate space.

visionOS 1.1+

    
    
    static var immersiveSpace: NamedCoordinateSpace { get }

Available when `Self` is `NamedCoordinateSpace`.

## See Also

### Getting built-in coordinate spaces

`static var global: GlobalCoordinateSpace`

The global coordinate space at the root of the view hierarchy.

Available when `Self` is `GlobalCoordinateSpace`.

`static var local: LocalCoordinateSpace`

The local coordinate space of the current view.

Available when `Self` is `LocalCoordinateSpace`.

`static func named(some Hashable) -> NamedCoordinateSpace`

Creates a named coordinate space using the given value.

Available when `Self` is `NamedCoordinateSpace`.

`static var scrollView: NamedCoordinateSpace`

The named coordinate space that is added by the system for the innermost
containing scroll view.

Available when `Self` is `NamedCoordinateSpace`.

`static func scrollView(axis: Axis) -> Self`

The named coordinate space that is added by the system for the innermost
containing scroll view that allows scrolling along the provided axis.

Available when `Self` is `NamedCoordinateSpace`.

Type Property

# global

The global coordinate space at the root of the view hierarchy.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static var global: GlobalCoordinateSpace { get }

Available when `Self` is `GlobalCoordinateSpace`.

## See Also

### Getting built-in coordinate spaces

`static var immersiveSpace: NamedCoordinateSpace`

The named coordinate space that represents the currently opened
`ImmersiveSpace` scene. If no immersive space is currently opened, this
CoordinateSpace provides the same behavior as the `.global` coordinate space.

Available when `Self` is `NamedCoordinateSpace`.

`static var local: LocalCoordinateSpace`

The local coordinate space of the current view.

Available when `Self` is `LocalCoordinateSpace`.

`static func named(some Hashable) -> NamedCoordinateSpace`

Creates a named coordinate space using the given value.

Available when `Self` is `NamedCoordinateSpace`.

`static var scrollView: NamedCoordinateSpace`

The named coordinate space that is added by the system for the innermost
containing scroll view.

Available when `Self` is `NamedCoordinateSpace`.

`static func scrollView(axis: Axis) -> Self`

The named coordinate space that is added by the system for the innermost
containing scroll view that allows scrolling along the provided axis.

Available when `Self` is `NamedCoordinateSpace`.

Type Property

# local

The local coordinate space of the current view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static var local: LocalCoordinateSpace { get }

Available when `Self` is `LocalCoordinateSpace`.

## See Also

### Getting built-in coordinate spaces

`static var immersiveSpace: NamedCoordinateSpace`

The named coordinate space that represents the currently opened
`ImmersiveSpace` scene. If no immersive space is currently opened, this
CoordinateSpace provides the same behavior as the `.global` coordinate space.

Available when `Self` is `NamedCoordinateSpace`.

`static var global: GlobalCoordinateSpace`

The global coordinate space at the root of the view hierarchy.

Available when `Self` is `GlobalCoordinateSpace`.

`static func named(some Hashable) -> NamedCoordinateSpace`

Creates a named coordinate space using the given value.

Available when `Self` is `NamedCoordinateSpace`.

`static var scrollView: NamedCoordinateSpace`

The named coordinate space that is added by the system for the innermost
containing scroll view.

Available when `Self` is `NamedCoordinateSpace`.

`static func scrollView(axis: Axis) -> Self`

The named coordinate space that is added by the system for the innermost
containing scroll view that allows scrolling along the provided axis.

Available when `Self` is `NamedCoordinateSpace`.

Type Method

# named(_:)

Creates a named coordinate space using the given value.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static func named(_ name: some Hashable) -> NamedCoordinateSpace

Available when `Self` is `NamedCoordinateSpace`.

##  Parameters

`name`

    

A unique value that identifies the coordinate space.

## Return Value

A named coordinate space identified by the given value.

## Discussion

Use the `coordinateSpace(_:)` modifier to assign a name to the local
coordinate space of a parent view. Child views can then refer to that
coordinate space using `.named(_:)`.

## See Also

### Getting built-in coordinate spaces

`static var immersiveSpace: NamedCoordinateSpace`

The named coordinate space that represents the currently opened
`ImmersiveSpace` scene. If no immersive space is currently opened, this
CoordinateSpace provides the same behavior as the `.global` coordinate space.

Available when `Self` is `NamedCoordinateSpace`.

`static var global: GlobalCoordinateSpace`

The global coordinate space at the root of the view hierarchy.

Available when `Self` is `GlobalCoordinateSpace`.

`static var local: LocalCoordinateSpace`

The local coordinate space of the current view.

Available when `Self` is `LocalCoordinateSpace`.

`static var scrollView: NamedCoordinateSpace`

The named coordinate space that is added by the system for the innermost
containing scroll view.

Available when `Self` is `NamedCoordinateSpace`.

`static func scrollView(axis: Axis) -> Self`

The named coordinate space that is added by the system for the innermost
containing scroll view that allows scrolling along the provided axis.

Available when `Self` is `NamedCoordinateSpace`.

Type Property

# scrollView

The named coordinate space that is added by the system for the innermost
containing scroll view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static var scrollView: NamedCoordinateSpace { get }

Available when `Self` is `NamedCoordinateSpace`.

## See Also

### Getting built-in coordinate spaces

`static var immersiveSpace: NamedCoordinateSpace`

The named coordinate space that represents the currently opened
`ImmersiveSpace` scene. If no immersive space is currently opened, this
CoordinateSpace provides the same behavior as the `.global` coordinate space.

Available when `Self` is `NamedCoordinateSpace`.

`static var global: GlobalCoordinateSpace`

The global coordinate space at the root of the view hierarchy.

Available when `Self` is `GlobalCoordinateSpace`.

`static var local: LocalCoordinateSpace`

The local coordinate space of the current view.

Available when `Self` is `LocalCoordinateSpace`.

`static func named(some Hashable) -> NamedCoordinateSpace`

Creates a named coordinate space using the given value.

Available when `Self` is `NamedCoordinateSpace`.

`static func scrollView(axis: Axis) -> Self`

The named coordinate space that is added by the system for the innermost
containing scroll view that allows scrolling along the provided axis.

Available when `Self` is `NamedCoordinateSpace`.

Type Method

# scrollView(axis:)

The named coordinate space that is added by the system for the innermost
containing scroll view that allows scrolling along the provided axis.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static func scrollView(axis: Axis) -> Self

Available when `Self` is `NamedCoordinateSpace`.

## See Also

### Getting built-in coordinate spaces

`static var immersiveSpace: NamedCoordinateSpace`

The named coordinate space that represents the currently opened
`ImmersiveSpace` scene. If no immersive space is currently opened, this
CoordinateSpace provides the same behavior as the `.global` coordinate space.

Available when `Self` is `NamedCoordinateSpace`.

`static var global: GlobalCoordinateSpace`

The global coordinate space at the root of the view hierarchy.

Available when `Self` is `GlobalCoordinateSpace`.

`static var local: LocalCoordinateSpace`

The local coordinate space of the current view.

Available when `Self` is `LocalCoordinateSpace`.

`static func named(some Hashable) -> NamedCoordinateSpace`

Creates a named coordinate space using the given value.

Available when `Self` is `NamedCoordinateSpace`.

`static var scrollView: NamedCoordinateSpace`

The named coordinate space that is added by the system for the innermost
containing scroll view.

Available when `Self` is `NamedCoordinateSpace`.

Instance Property

# coordinateSpace

The resolved coordinate space.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var coordinateSpace: CoordinateSpace { get }

**Required**

Structure

# GlobalCoordinateSpace

The global coordinate space at the root of the view hierarchy.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct GlobalCoordinateSpace

## Topics

### Creating the coordinate space

`init()`

## Relationships

### Conforms To

  * `CoordinateSpaceProtocol`

## See Also

### Supporting types

`struct LocalCoordinateSpace`

The local coordinate space of the current view.

`struct NamedCoordinateSpace`

A named coordinate space.

Structure

# LocalCoordinateSpace

The local coordinate space of the current view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct LocalCoordinateSpace

## Topics

### Creating the coordinate space

`init()`

## Relationships

### Conforms To

  * `CoordinateSpaceProtocol`

## See Also

### Supporting types

`struct GlobalCoordinateSpace`

The global coordinate space at the root of the view hierarchy.

`struct NamedCoordinateSpace`

A named coordinate space.

Structure

# NamedCoordinateSpace

A named coordinate space.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct NamedCoordinateSpace

## Overview

Use the `coordinateSpace(_:)` modifier to assign a name to the local
coordinate space of a parent view. Child views can then refer to that
coordinate space using `.named(_:)`.

## Relationships

### Conforms To

  * `CoordinateSpaceProtocol`
  * `Equatable`

## See Also

### Supporting types

`struct GlobalCoordinateSpace`

The global coordinate space at the root of the view hierarchy.

`struct LocalCoordinateSpace`

The local coordinate space of the current view.

