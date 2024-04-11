Case

# CoordinateSpace.global

The global coordinate space at the root of the view hierarchy.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case global

## See Also

### Getting coordinate spaces

`case local`

The local coordinate space of the current view.

`case named(AnyHashable)`

A named reference to a view’s local coordinate space.

Case

# CoordinateSpace.local

The local coordinate space of the current view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case local

## See Also

### Getting coordinate spaces

`case global`

The global coordinate space at the root of the view hierarchy.

`case named(AnyHashable)`

A named reference to a view’s local coordinate space.

Case

# CoordinateSpace.named(_:)

A named reference to a view’s local coordinate space.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case named(AnyHashable)

## See Also

### Getting coordinate spaces

`case global`

The global coordinate space at the root of the view hierarchy.

`case local`

The local coordinate space of the current view.

Instance Property

# isGlobal

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var isGlobal: Bool { get }

## See Also

### Testing a space

`var isLocal: Bool`

Instance Property

# isLocal

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var isLocal: Bool { get }

## See Also

### Testing a space

`var isGlobal: Bool`

