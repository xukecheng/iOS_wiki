Initializer

# init(property:collationType:)

Creates an index element description using the specified property description
and collation type.

iOS 11.0+  iPadOS 11.0+  macOS 10.13+  Mac Catalyst 13.1+  tvOS 11.0+  watchOS
4.0+  visionOS 1.0+

    
    
    init(
        property: NSPropertyDescription,
        collationType: NSFetchIndexElementType
    )

Instance Property

# collationType

The type of collation that the index element uses, either binary or R-tree.

iOS 11.0+  iPadOS 11.0+  macOS 10.13+  Mac Catalyst 13.1+  tvOS 11.0+  watchOS
4.0+  visionOS 1.0+

    
    
    var collationType: NSFetchIndexElementType { get set }

## See Also

### Inspecting an Index Element Description

`var indexDescription: NSFetchIndexDescription?`

`var isAscending: Bool`

A Boolean value that controls whether an index that supports direction is an
ascending or descending index.

`var property: NSPropertyDescription?`

A property description.

`var propertyName: String?`

The specified name in the property description.

Instance Property

# indexDescription

iOS 11.0+  iPadOS 11.0+  macOS 10.13+  Mac Catalyst 13.1+  tvOS 11.0+  watchOS
4.0+  visionOS 1.0+

    
    
    unowned(unsafe) var indexDescription: NSFetchIndexDescription? { get }

## See Also

### Inspecting an Index Element Description

`var collationType: NSFetchIndexElementType`

The type of collation that the index element uses, either binary or R-tree.

`var isAscending: Bool`

A Boolean value that controls whether an index that supports direction is an
ascending or descending index.

`var property: NSPropertyDescription?`

A property description.

`var propertyName: String?`

The specified name in the property description.

Instance Property

# isAscending

A Boolean value that controls whether an index that supports direction is an
ascending or descending index.

iOS 11.0+  iPadOS 11.0+  macOS 10.13+  Mac Catalyst 13.1+  tvOS 11.0+  watchOS
4.0+  visionOS 1.0+

    
    
    var isAscending: Bool { get set }

## See Also

### Inspecting an Index Element Description

`var collationType: NSFetchIndexElementType`

The type of collation that the index element uses, either binary or R-tree.

`var indexDescription: NSFetchIndexDescription?`

`var property: NSPropertyDescription?`

A property description.

`var propertyName: String?`

The specified name in the property description.

Instance Property

# property

A property description.

iOS 11.0+  iPadOS 11.0+  macOS 10.13+  Mac Catalyst 13.1+  tvOS 11.0+  watchOS
4.0+  visionOS 1.0+

    
    
    var property: NSPropertyDescription? { get }

## Discussion

This property may also be an `NSExpressionDescription` that expresses a
function.

## See Also

### Inspecting an Index Element Description

`var collationType: NSFetchIndexElementType`

The type of collation that the index element uses, either binary or R-tree.

`var indexDescription: NSFetchIndexDescription?`

`var isAscending: Bool`

A Boolean value that controls whether an index that supports direction is an
ascending or descending index.

`var propertyName: String?`

The specified name in the property description.

Instance Property

# propertyName

The specified name in the property description.

iOS 11.0+  iPadOS 11.0+  macOS 10.13+  Mac Catalyst 13.1+  tvOS 11.0+  watchOS
4.0+  visionOS 1.0+

    
    
    var propertyName: String? { get }

## See Also

### Inspecting an Index Element Description

`var collationType: NSFetchIndexElementType`

The type of collation that the index element uses, either binary or R-tree.

`var indexDescription: NSFetchIndexDescription?`

`var isAscending: Bool`

A Boolean value that controls whether an index that supports direction is an
ascending or descending index.

`var property: NSPropertyDescription?`

A property description.

