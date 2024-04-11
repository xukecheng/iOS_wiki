Case

# HorizontalEdge.leading

The leading edge.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    case leading

## See Also

### Getting the edges

`case trailing`

The trailing edge.

Case

# HorizontalEdge.trailing

The trailing edge.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    case trailing

## See Also

### Getting the edges

`case leading`

The leading edge.

Structure

# HorizontalEdge.Set

An efficient set of horizontal edges.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    @frozen
    struct Set

## Topics

### Getting edge sets

`static let all: HorizontalEdge.Set`

A set containing the leading and trailing horizontal edges.

`static let leading: HorizontalEdge.Set`

A set containing only the leading horizontal edge.

`static let trailing: HorizontalEdge.Set`

A set containing only the trailing horizontal edge.

### Creating an edge set

`init(HorizontalEdge)`

Creates a set of edges containing only the specified horizontal edge.

## Relationships

### Conforms To

  * `Equatable`
  * `ExpressibleByArrayLiteral`
  * `OptionSet`
  * `RawRepresentable`
  * `Sendable`
  * `SetAlgebra`

