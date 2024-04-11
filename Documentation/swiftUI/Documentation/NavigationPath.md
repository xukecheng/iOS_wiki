Initializer

# init()

Creates a new, empty navigation path.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init()

## See Also

### Creating a navigation path

`init(NavigationPath.CodableRepresentation)`

Creates a new navigation path from a serializable version.

`init<S>(S)`

Creates a new navigation path from the contents of a sequence that contains
codable elements.

`init<S>(S)`

Creates a new navigation path from the contents of a sequence.

Initializer

# init(_:)

Creates a new navigation path from a serializable version.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init(_ codable: NavigationPath.CodableRepresentation)

##  Parameters

`codable`

    

A value describing the contents of the new path in a serializable format.

## See Also

### Creating a navigation path

`init()`

Creates a new, empty navigation path.

`init<S>(S)`

Creates a new navigation path from the contents of a sequence that contains
codable elements.

`init<S>(S)`

Creates a new navigation path from the contents of a sequence.

Initializer

# init(_:)

Creates a new navigation path from the contents of a sequence that contains
codable elements.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init<S>(_ elements: S) where S : Sequence, S.Element : Decodable, S.Element : Encodable, S.Element : Hashable

##  Parameters

`elements`

    

A sequence used to create the navigation path.

## See Also

### Creating a navigation path

`init()`

Creates a new, empty navigation path.

`init(NavigationPath.CodableRepresentation)`

Creates a new navigation path from a serializable version.

`init<S>(S)`

Creates a new navigation path from the contents of a sequence.

Initializer

# init(_:)

Creates a new navigation path from the contents of a sequence.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init<S>(_ elements: S) where S : Sequence, S.Element : Hashable

##  Parameters

`elements`

    

A sequence used to create the navigation path.

## See Also

### Creating a navigation path

`init()`

Creates a new, empty navigation path.

`init(NavigationPath.CodableRepresentation)`

Creates a new navigation path from a serializable version.

`init<S>(S)`

Creates a new navigation path from the contents of a sequence that contains
codable elements.

Instance Property

# isEmpty

A Boolean that indicates whether this path is empty.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var isEmpty: Bool { get }

## See Also

### Managing path contents

`var count: Int`

The number of elements in this path.

`func append<V>(V)`

Appends a new codable value to the end of this path.

`func append<V>(V)`

Appends a new value to the end of this path.

`func removeLast(Int)`

Removes values from the end of this path.

Instance Property

# count

The number of elements in this path.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var count: Int { get }

## See Also

### Managing path contents

`var isEmpty: Bool`

A Boolean that indicates whether this path is empty.

`func append<V>(V)`

Appends a new codable value to the end of this path.

`func append<V>(V)`

Appends a new value to the end of this path.

`func removeLast(Int)`

Removes values from the end of this path.

Instance Method

# append(_:)

Appends a new codable value to the end of this path.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    mutating func append<V>(_ value: V) where V : Decodable, V : Encodable, V : Hashable

## See Also

### Managing path contents

`var isEmpty: Bool`

A Boolean that indicates whether this path is empty.

`var count: Int`

The number of elements in this path.

`func append<V>(V)`

Appends a new value to the end of this path.

`func removeLast(Int)`

Removes values from the end of this path.

Instance Method

# append(_:)

Appends a new value to the end of this path.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    mutating func append<V>(_ value: V) where V : Hashable

## See Also

### Managing path contents

`var isEmpty: Bool`

A Boolean that indicates whether this path is empty.

`var count: Int`

The number of elements in this path.

`func append<V>(V)`

Appends a new codable value to the end of this path.

`func removeLast(Int)`

Removes values from the end of this path.

Instance Method

# removeLast(_:)

Removes values from the end of this path.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    mutating func removeLast(_ k: Int = 1)

##  Parameters

`k`

    

The number of values to remove. The default value is `1`.

## Discussion

Precondition

The input parameter `k` must be greater than or equal to zero, and must be
less than or equal to the number of elements in the path.

## See Also

### Managing path contents

`var isEmpty: Bool`

A Boolean that indicates whether this path is empty.

`var count: Int`

The number of elements in this path.

`func append<V>(V)`

Appends a new codable value to the end of this path.

`func append<V>(V)`

Appends a new value to the end of this path.

Instance Property

# codable

A value that describes the contents of this path in a serializable format.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var codable: NavigationPath.CodableRepresentation? { get }

## Discussion

This value is `nil` if any of the type-erased elements of the path don’t
conform to the `Codable` protocol.

## See Also

### Encoding a path

`struct CodableRepresentation`

A serializable representation of a navigation path.

Structure

# NavigationPath.CodableRepresentation

A serializable representation of a navigation path.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    struct CodableRepresentation

## Overview

When a navigation path contains elements the conform to the `Codable`
protocol, you can use the path’s `CodableRepresentation` to convert the path
to an external representation and to convert an external representation back
into a navigation path.

## Relationships

### Conforms To

  * `Decodable`
  * `Encodable`
  * `Equatable`

## See Also

### Encoding a path

`var codable: NavigationPath.CodableRepresentation?`

A value that describes the contents of this path in a serializable format.

