Case

# Edge.top

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case top

## See Also

### Getting the edges

`case bottom`

`case leading`

`case trailing`

Case

# Edge.bottom

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case bottom

## See Also

### Getting the edges

`case top`

`case leading`

`case trailing`

Case

# Edge.leading

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case leading

## See Also

### Getting the edges

`case top`

`case bottom`

`case trailing`

Case

# Edge.trailing

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case trailing

## See Also

### Getting the edges

`case top`

`case bottom`

`case leading`

Initializer

# init(_:)

Converts a 3D edge to a 2D edge, if possible.

visionOS 1.0+

    
    
    init?(_ edge: Edge3D)

Structure

# Edge.Set

An efficient set of edges.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct Set

## Topics

### Getting edge sets

`static let all: Edge.Set`

`static let top: Edge.Set`

`static let bottom: Edge.Set`

`static let leading: Edge.Set`

`static let trailing: Edge.Set`

`static let horizontal: Edge.Set`

`static let vertical: Edge.Set`

### Creating an edge set

`init(Edge)`

Creates set of edges containing only the specified edge.

## Relationships

### Conforms To

  * `Equatable`
  * `ExpressibleByArrayLiteral`
  * `OptionSet`
  * `RawRepresentable`
  * `Sendable`
  * `SetAlgebra`

