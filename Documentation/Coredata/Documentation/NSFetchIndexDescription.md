Initializer

# init(name:elements:)

Creates a fetch index description using the specified name and element
descriptions.

iOS 11.0+  iPadOS 11.0+  macOS 10.13+  Mac Catalyst 13.1+  tvOS 11.0+  watchOS
4.0+  visionOS 1.0+

    
    
    init(
        name: String,
        elements: [NSFetchIndexElementDescription]?
    )

##  Parameters

`name`

    

The name of the fetch index description.

`elements`

    

An array of fetch index element descriptions.

Instance Property

# elements

An array of fetch index element descriptions.

iOS 11.0+  iPadOS 11.0+  macOS 10.13+  Mac Catalyst 13.1+  tvOS 11.0+  watchOS
4.0+  visionOS 1.0+

    
    
    var elements: [NSFetchIndexElementDescription] { get set }

## Discussion

Setting this property to an invalid value throws an exception, such as when
the new value includes both R-tree and non-R-tree elements.

## See Also

### Inspecting an Index Description

`var entity: NSEntityDescription?`

The entity description for the fetch index description.

`var name: String`

The name of the fetch index description.

`var partialIndexPredicate: NSPredicate?`

A predicate that selects rows for indexing, if the index is a partial index.

Instance Property

# entity

The entity description for the fetch index description.

iOS 11.0+  iPadOS 11.0+  macOS 10.13+  Mac Catalyst 13.1+  tvOS 11.0+  watchOS
4.0+  visionOS 1.0+

    
    
    unowned(unsafe) var entity: NSEntityDescription? { get }

## See Also

### Inspecting an Index Description

`var elements: [NSFetchIndexElementDescription]`

An array of fetch index element descriptions.

`var name: String`

The name of the fetch index description.

`var partialIndexPredicate: NSPredicate?`

A predicate that selects rows for indexing, if the index is a partial index.

Instance Property

# name

The name of the fetch index description.

iOS 11.0+  iPadOS 11.0+  macOS 10.13+  Mac Catalyst 13.1+  tvOS 11.0+  watchOS
4.0+  visionOS 1.0+

    
    
    var name: String { get set }

## See Also

### Inspecting an Index Description

`var elements: [NSFetchIndexElementDescription]`

An array of fetch index element descriptions.

`var entity: NSEntityDescription?`

The entity description for the fetch index description.

`var partialIndexPredicate: NSPredicate?`

A predicate that selects rows for indexing, if the index is a partial index.

Instance Property

# partialIndexPredicate

A predicate that selects rows for indexing, if the index is a partial index.

iOS 11.0+  iPadOS 11.0+  macOS 10.13+  Mac Catalyst 13.1+  tvOS 11.0+  watchOS
4.0+  visionOS 1.0+

    
    
    @NSCopying
    var partialIndexPredicate: NSPredicate? { get set }

## See Also

### Inspecting an Index Description

`var elements: [NSFetchIndexElementDescription]`

An array of fetch index element descriptions.

`var entity: NSEntityDescription?`

The entity description for the fetch index description.

`var name: String`

The name of the fetch index description.

