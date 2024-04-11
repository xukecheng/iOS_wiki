Instance Property

# nsPredicate

The request’s predicate.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var nsPredicate: NSPredicate? { get nonmutating set }

## Discussion

Set this value to cause the associated `SectionedFetchRequest` to execute a
fetch with a new predicate, producing an updated collection of results.

## See Also

### Configuring the associated sectioned fetch request

`var sortDescriptors: [SortDescriptor<Result>]`

The request’s sort descriptors, accessed as value types.

Available when `SectionIdentifier` conforms to `Hashable` and `Result`
inherits `NSManagedObject`.

`var nsSortDescriptors: [NSSortDescriptor]`

The request’s sort descriptors, accessed as reference types.

`var sectionIdentifier: KeyPath<Result, SectionIdentifier>`

The key path that the system uses to group fetched results into sections.

`struct Section`

A collection of fetched results that share a specified identifier.

Instance Property

# sortDescriptors

The request’s sort descriptors, accessed as value types.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var sortDescriptors: [SortDescriptor<Result>] { get nonmutating set }

Available when `SectionIdentifier` conforms to `Hashable` and `Result`
inherits `NSManagedObject`.

## Discussion

Set this value to cause the associated `SectionedFetchRequest` to execute a
fetch with a new collection of `SortDescriptor` instances. The order of
entities stored in the results collection may change as a result. Use care to
coordinate section and sort updates, as described in
`SectionedFetchRequest.Configuration`.

If you want to use `NSSortDescriptor` instances, set `nsSortDescriptors`
instead.

## See Also

### Configuring the associated sectioned fetch request

`var nsPredicate: NSPredicate?`

The request’s predicate.

`var nsSortDescriptors: [NSSortDescriptor]`

The request’s sort descriptors, accessed as reference types.

`var sectionIdentifier: KeyPath<Result, SectionIdentifier>`

The key path that the system uses to group fetched results into sections.

`struct Section`

A collection of fetched results that share a specified identifier.

Instance Property

# nsSortDescriptors

The request’s sort descriptors, accessed as reference types.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var nsSortDescriptors: [NSSortDescriptor] { get nonmutating set }

## Discussion

Set this value to cause the associated `SectionedFetchRequest` to execute a
fetch with a new collection of `NSSortDescriptor` instances. The order of
managed objects stored in the results collection may change as a result. Use
care to coordinate section and sort updates, as described in
`SectionedFetchRequest.Configuration`.

If you want to use `SortDescriptor` instances, set `sortDescriptors` instead.

## See Also

### Configuring the associated sectioned fetch request

`var nsPredicate: NSPredicate?`

The request’s predicate.

`var sortDescriptors: [SortDescriptor<Result>]`

The request’s sort descriptors, accessed as value types.

Available when `SectionIdentifier` conforms to `Hashable` and `Result`
inherits `NSManagedObject`.

`var sectionIdentifier: KeyPath<Result, SectionIdentifier>`

The key path that the system uses to group fetched results into sections.

`struct Section`

A collection of fetched results that share a specified identifier.

Instance Property

# sectionIdentifier

The key path that the system uses to group fetched results into sections.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var sectionIdentifier: KeyPath<Result, SectionIdentifier> { get nonmutating set }

## Discussion

Set this value to cause the associated `SectionedFetchRequest` to execute a
fetch with a new section identifier, producing an updated collection of
results. Changing this value produces a new set of sections. Use care to
coordinate section and sort updates, as described in
`SectionedFetchRequest.Configuration`.

## See Also

### Configuring the associated sectioned fetch request

`var nsPredicate: NSPredicate?`

The request’s predicate.

`var sortDescriptors: [SortDescriptor<Result>]`

The request’s sort descriptors, accessed as value types.

Available when `SectionIdentifier` conforms to `Hashable` and `Result`
inherits `NSManagedObject`.

`var nsSortDescriptors: [NSSortDescriptor]`

The request’s sort descriptors, accessed as reference types.

`struct Section`

A collection of fetched results that share a specified identifier.

Structure

# SectionedFetchResults.Section

A collection of fetched results that share a specified identifier.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    struct Section

## Overview

Examine a `Section` instance to find the entities that satisfy a
`SectionedFetchRequest` predicate, and that have a particular property with
the value stored in the section’s `id` parameter. You specify which property
by setting the fetch request’s `sectionIdentifier` parameter during
initialization, or by modifying the corresponding `SectionedFetchResults`
instance’s `sectionIdentifier` property.

Obtain specific sections by treating the fetch results as a collection. For
example, consider the following property declaration that fetches `Quake`
managed objects that the Loading and Displaying a Large Data Feed sample code
project defines to store earthquake data:

Get the first section using a subscript:

Alternatively, you can loop over the sections to create a list of sections.

The sections also act as collections, which means you can use elements like
the `count` property in the example above.

## Topics

### Identifying the section

`let id: SectionIdentifier`

The value that all entities in the section share for a specified key path.

### Getting indices

`var startIndex: Int`

The index of the first entity in the section.

`var endIndex: Int`

The index that’s one greater than that of the last entity in the section.

### Getting results

`subscript(Int) -> Result`

Gets the entity at the specified index within the section.

## Relationships

### Conforms To

  * `BidirectionalCollection`
  * `Collection`
  * `Identifiable`
  * `RandomAccessCollection`
  * `Sequence`

## See Also

### Configuring the associated sectioned fetch request

`var nsPredicate: NSPredicate?`

The request’s predicate.

`var sortDescriptors: [SortDescriptor<Result>]`

The request’s sort descriptors, accessed as value types.

Available when `SectionIdentifier` conforms to `Hashable` and `Result`
inherits `NSManagedObject`.

`var nsSortDescriptors: [NSSortDescriptor]`

The request’s sort descriptors, accessed as reference types.

`var sectionIdentifier: KeyPath<Result, SectionIdentifier>`

The key path that the system uses to group fetched results into sections.

Instance Property

# startIndex

The index of the first section in the results collection.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var startIndex: Int { get }

## See Also

### Getting indices

`var endIndex: Int`

The index that’s one greater than that of the last section.

Instance Property

# endIndex

The index that’s one greater than that of the last section.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var endIndex: Int { get }

## See Also

### Getting indices

`var startIndex: Int`

The index of the first section in the results collection.

Instance Subscript

# subscript(_:)

Gets the section at the specified index.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    subscript(position: Int) -> SectionedFetchResults<SectionIdentifier, Result>.Section { get }

