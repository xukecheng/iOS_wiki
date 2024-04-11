Case

# Edge3D.top

visionOS 1.0+

    
    
    case top

## See Also

### Getting the edges

`case bottom`

`case leading`

`case trailing`

`case front`

`case back`

Case

# Edge3D.bottom

visionOS 1.0+

    
    
    case bottom

## See Also

### Getting the edges

`case top`

`case leading`

`case trailing`

`case front`

`case back`

Case

# Edge3D.leading

visionOS 1.0+

    
    
    case leading

## See Also

### Getting the edges

`case top`

`case bottom`

`case trailing`

`case front`

`case back`

Case

# Edge3D.trailing

visionOS 1.0+

    
    
    case trailing

## See Also

### Getting the edges

`case top`

`case bottom`

`case leading`

`case front`

`case back`

Case

# Edge3D.front

visionOS 1.0+

    
    
    case front

## See Also

### Getting the edges

`case top`

`case bottom`

`case leading`

`case trailing`

`case back`

Case

# Edge3D.back

visionOS 1.0+

    
    
    case back

## See Also

### Getting the edges

`case top`

`case bottom`

`case leading`

`case trailing`

`case front`

Initializer

# init(_:)

visionOS 1.0+

    
    
    init(_ edge: Edge)

Structure

# Edge3D.Set

An efficient set of 3D edges.

visionOS 1.0+

    
    
    @frozen
    struct Set

## Topics

### Getting edge sets

`static let all: Edge3D.Set`

`static let top: Edge3D.Set`

`static let bottom: Edge3D.Set`

`static let leading: Edge3D.Set`

`static let front: Edge3D.Set`

`static let back: Edge3D.Set`

`static let trailing: Edge3D.Set`

`static let horizontal: Edge3D.Set`

`static let vertical: Edge3D.Set`

`static let depth: Edge3D.Set`

### Creating an edge set

`init(Edge)`

`init(Edge3D)`

Creates a set of edges containing only the specified edge.

## Relationships

### Conforms To

  * `Equatable`
  * `ExpressibleByArrayLiteral`
  * `OptionSet`
  * `RawRepresentable`
  * `Sendable`
  * `SetAlgebra`

