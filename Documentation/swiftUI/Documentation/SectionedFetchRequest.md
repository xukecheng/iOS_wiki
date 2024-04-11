Initializer

# init(sectionIdentifier:sortDescriptors:predicate:animation:)

Creates a sectioned fetch request based on a section identifier, a predicate,
and value type sort parameters.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    @MainActor
    init(
        sectionIdentifier: KeyPath<Result, SectionIdentifier>,
        sortDescriptors: [SortDescriptor<Result>],
        predicate: NSPredicate? = nil,
        animation: Animation? = nil
    )

Available when `SectionIdentifier` conforms to `Hashable` and `Result`
inherits `NSManagedObject`.

##  Parameters

`sectionIdentifier`

    

A key path that SwiftUI applies to the `Result` type to get an object’s
section identifier.

`sortDescriptors`

    

An array of sort descriptors that define the sort order of the fetched
results.

`predicate`

    

An `NSPredicate` instance that defines logical conditions used to filter the
fetched results.

`animation`

    

The animation to use for user interface changes that result from changes to
the fetched results.

## Discussion

The request gets the entity type from the `Result` instance by calling that
managed object’s `entity()` type method. If you need to specify the entity
type explicitly, use the
`init(entity:sectionIdentifier:sortDescriptors:predicate:animation:)`
initializer instead. If you need more control over the fetch request
configuration, use `init(fetchRequest:sectionIdentifier:animation:)`. For
reference type sort descriptors, use
`init(sectionIdentifier:sortDescriptors:predicate:animation:)`.

## See Also

### Creating a fetch request

`init(sectionIdentifier: KeyPath<Result, SectionIdentifier>, sortDescriptors:
[NSSortDescriptor], predicate: NSPredicate?, animation: Animation?)`

Creates a sectioned fetch request based on a section identifier, a predicate,
and reference type sort parameters.

Available when `SectionIdentifier` conforms to `Hashable` and `Result`
inherits `NSManagedObject`.

`init(entity: NSEntityDescription, sectionIdentifier: KeyPath<Result,
SectionIdentifier>, sortDescriptors: [NSSortDescriptor], predicate:
NSPredicate?, animation: Animation?)`

Creates a sectioned fetch request for a specified entity description, based on
a section identifier, a predicate, and sort parameters.

Available when `SectionIdentifier` conforms to `Hashable` and `Result`
conforms to `NSFetchRequestResult`.

Initializer

# init(sectionIdentifier:sortDescriptors:predicate:animation:)

Creates a sectioned fetch request based on a section identifier, a predicate,
and reference type sort parameters.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    @MainActor
    init(
        sectionIdentifier: KeyPath<Result, SectionIdentifier>,
        sortDescriptors: [NSSortDescriptor],
        predicate: NSPredicate? = nil,
        animation: Animation? = nil
    )

Available when `SectionIdentifier` conforms to `Hashable` and `Result`
inherits `NSManagedObject`.

##  Parameters

`sectionIdentifier`

    

A key path that SwiftUI applies to the `Result` type to get an object’s
section identifier.

`sortDescriptors`

    

An array of sort descriptors that define the sort order of the fetched
results.

`predicate`

    

An `NSPredicate` instance that defines logical conditions used to filter the
fetched results.

`animation`

    

The animation to use for user interface changes that result from changes to
the fetched results.

## Discussion

The request gets the entity type from the `Result` instance by calling that
managed object’s `entity()` type method. If you need to specify the entity
type explicitly, use the
`init(entity:sectionIdentifier:sortDescriptors:predicate:animation:)`
initializer instead. If you need more control over the fetch request
configuration, use `init(fetchRequest:sectionIdentifier:animation:)`. For
value type sort descriptors, use
`init(sectionIdentifier:sortDescriptors:predicate:animation:)`.

## See Also

### Creating a fetch request

`init(sectionIdentifier: KeyPath<Result, SectionIdentifier>, sortDescriptors:
[SortDescriptor<Result>], predicate: NSPredicate?, animation: Animation?)`

Creates a sectioned fetch request based on a section identifier, a predicate,
and value type sort parameters.

Available when `SectionIdentifier` conforms to `Hashable` and `Result`
inherits `NSManagedObject`.

`init(entity: NSEntityDescription, sectionIdentifier: KeyPath<Result,
SectionIdentifier>, sortDescriptors: [NSSortDescriptor], predicate:
NSPredicate?, animation: Animation?)`

Creates a sectioned fetch request for a specified entity description, based on
a section identifier, a predicate, and sort parameters.

Available when `SectionIdentifier` conforms to `Hashable` and `Result`
conforms to `NSFetchRequestResult`.

Initializer

# init(entity:sectionIdentifier:sortDescriptors:predicate:animation:)

Creates a sectioned fetch request for a specified entity description, based on
a section identifier, a predicate, and sort parameters.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    @MainActor
    init(
        entity: NSEntityDescription,
        sectionIdentifier: KeyPath<Result, SectionIdentifier>,
        sortDescriptors: [NSSortDescriptor],
        predicate: NSPredicate? = nil,
        animation: Animation? = nil
    )

Available when `SectionIdentifier` conforms to `Hashable` and `Result`
conforms to `NSFetchRequestResult`.

##  Parameters

`entity`

    

The description of the Core Data entity to fetch.

`sectionIdentifier`

    

A key path that SwiftUI applies to the `Result` type to get an object’s
section identifier.

`sortDescriptors`

    

An array of sort descriptors that define the sort order of the fetched
results.

`predicate`

    

An `NSPredicate` instance that defines logical conditions used to filter the
fetched results.

`animation`

    

The animation to use for user interface changes that result from changes to
the fetched results.

## Discussion

Use this initializer if you need to explicitly specify the entity type for the
request. If you specify a placeholder `Result` type in the request
declaration, use the
`init(sectionIdentifier:sortDescriptors:predicate:animation:)` initializer to
let the request infer the entity type. If you need more control over the fetch
request configuration, use `init(fetchRequest:sectionIdentifier:animation:)`.

## See Also

### Creating a fetch request

`init(sectionIdentifier: KeyPath<Result, SectionIdentifier>, sortDescriptors:
[SortDescriptor<Result>], predicate: NSPredicate?, animation: Animation?)`

Creates a sectioned fetch request based on a section identifier, a predicate,
and value type sort parameters.

Available when `SectionIdentifier` conforms to `Hashable` and `Result`
inherits `NSManagedObject`.

`init(sectionIdentifier: KeyPath<Result, SectionIdentifier>, sortDescriptors:
[NSSortDescriptor], predicate: NSPredicate?, animation: Animation?)`

Creates a sectioned fetch request based on a section identifier, a predicate,
and reference type sort parameters.

Available when `SectionIdentifier` conforms to `Hashable` and `Result`
inherits `NSManagedObject`.

Initializer

# init(fetchRequest:sectionIdentifier:animation:)

Creates a fully configured sectioned fetch request that uses the specified
animation when updating results.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    @MainActor
    init(
        fetchRequest: NSFetchRequest<Result>,
        sectionIdentifier: KeyPath<Result, SectionIdentifier>,
        animation: Animation? = nil
    )

Available when `SectionIdentifier` conforms to `Hashable` and `Result`
conforms to `NSFetchRequestResult`.

##  Parameters

`fetchRequest`

    

An `NSFetchRequest` instance that describes the search criteria for retrieving
data from the persistent store.

`sectionIdentifier`

    

A key path that SwiftUI applies to the `Result` type to get an object’s
section identifier.

`animation`

    

The animation to use for user interface changes that result from changes to
the fetched results.

## Discussion

Use this initializer when you want to configure a fetch request with more than
a predicate and sort descriptors. For example, you can vend a request from a
`Quake` managed object that the Loading and Displaying a Large Data Feed
sample code project defines to store earthquake data. Limit the number of
results to `1000` by setting a `fetchLimit` for the request:

Use the request to define a `SectionedFetchedResults` property:

If you only need to configure the request’s section identifier, predicate, and
sort descriptors, use
`init(sectionIdentifier:sortDescriptors:predicate:animation:)` instead. If you
need to specify a `Transaction` rather than an optional `Animation`, use
`init(fetchRequest:sectionIdentifier:transaction:)`.

## See Also

### Creating a fully configured fetch request

`init(fetchRequest: NSFetchRequest<Result>, sectionIdentifier: KeyPath<Result,
SectionIdentifier>, transaction: Transaction)`

Creates a fully configured sectioned fetch request that uses the specified
transaction when updating results.

Available when `SectionIdentifier` conforms to `Hashable` and `Result`
conforms to `NSFetchRequestResult`.

Initializer

# init(fetchRequest:sectionIdentifier:transaction:)

Creates a fully configured sectioned fetch request that uses the specified
transaction when updating results.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    @MainActor
    init(
        fetchRequest: NSFetchRequest<Result>,
        sectionIdentifier: KeyPath<Result, SectionIdentifier>,
        transaction: Transaction
    )

Available when `SectionIdentifier` conforms to `Hashable` and `Result`
conforms to `NSFetchRequestResult`.

##  Parameters

`fetchRequest`

    

An `NSFetchRequest` instance that describes the search criteria for retrieving
data from the persistent store.

`sectionIdentifier`

    

A key path that SwiftUI applies to the `Result` type to get an object’s
section identifier.

`transaction`

    

A transaction to use for user interface changes that result from changes to
the fetched results.

## Discussion

Use this initializer if you need a fetch request with updates that affect the
user interface based on a `Transaction`. Otherwise, use
`init(fetchRequest:sectionIdentifier:animation:)`.

## See Also

### Creating a fully configured fetch request

`init(fetchRequest: NSFetchRequest<Result>, sectionIdentifier: KeyPath<Result,
SectionIdentifier>, animation: Animation?)`

Creates a fully configured sectioned fetch request that uses the specified
animation when updating results.

Available when `SectionIdentifier` conforms to `Hashable` and `Result`
conforms to `NSFetchRequestResult`.

Structure

# SectionedFetchRequest.Configuration

The request’s configurable properties.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    struct Configuration

## Overview

You initialize a `SectionedFetchRequest` with a section identifier, an
optional predicate, and sort descriptors, either explicitly or with a
configured `NSFetchRequest`. Later, you can dynamically update the identifier,
predicate, and sort parameters using the request’s configuration structure.

You access or bind to a request’s configuration components through properties
on the associated `SectionedFetchResults` instance, just like you do for a
`FetchRequest` using `FetchRequest.Configuration`.

When configuring a sectioned fetch request, ensure that the combination of the
section identifier and the primary sort descriptor doesn’t create
discontiguous sections.

## Topics

### Setting the section identifier

`var sectionIdentifier: KeyPath<Result, SectionIdentifier>`

The request’s section identifier key path.

### Setting a predicate

`var nsPredicate: NSPredicate?`

The request’s predicate.

### Setting sort descriptors

`var sortDescriptors: [SortDescriptor<Result>]`

The request’s sort descriptors, accessed as value types.

Available when `SectionIdentifier` conforms to `Hashable` and `Result`
inherits `NSManagedObject`.

`var nsSortDescriptors: [NSSortDescriptor]`

The request’s sort descriptors, accessed as reference types.

## See Also

### Configuring a request dynamically

`var projectedValue: Binding<SectionedFetchRequest<SectionIdentifier,
Result>.Configuration>`

A binding to the request’s mutable configuration properties.

Instance Property

# projectedValue

A binding to the request’s mutable configuration properties.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    @MainActor
    var projectedValue: Binding<SectionedFetchRequest<SectionIdentifier, Result>.Configuration> { get }

## Discussion

This property behaves like the `projectedValue` of a `FetchRequest`. In
particular, SwiftUI returns the value associated with this property when you
use `SectionedFetchRequest` as a property wrapper on a `SectionedFetchResults`
instance and then access the results with a dollar sign (`$`) prefix. The
value that SwiftUI returns is a `Binding` to the request’s
`SectionedFetchRequest.Configuration` structure, which dynamically configures
the request.

## See Also

### Configuring a request dynamically

`struct Configuration`

The request’s configurable properties.

Instance Method

# update()

Updates the fetched results.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    @MainActor
    func update()

Available when `SectionIdentifier` conforms to `Hashable` and `Result`
conforms to `NSFetchRequestResult`.

## Discussion

SwiftUI calls this function before rendering a view’s `body` to ensure the
view has the most recent fetched results.

## See Also

### Getting the fetched results

`var wrappedValue: SectionedFetchResults<SectionIdentifier, Result>`

The fetched results of the fetch request.

Instance Property

# wrappedValue

The fetched results of the fetch request.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    @MainActor
    var wrappedValue: SectionedFetchResults<SectionIdentifier, Result> { get }

## Discussion

This property behaves like the `wrappedValue` of a `FetchRequest`. In
particular, SwiftUI returns the value associated with this property when you
use `SectionedFetchRequest` as a property wrapper and then access the wrapped
property by name. For example, consider the following `quakes` property
declaration that fetches a `Quake` type that the Loading and Displaying a
Large Data Feed sample code project defines:

You access the request’s `wrappedValue`, which contains a
`SectionedFetchResults` instance, by referring to the `quakes` property by
name. That value is a collection of sections, each of which contains a group
of managed objects:

If you need to separate the request and the result entities, you can declare
`quakes` in two steps by using the request’s `wrappedValue` to obtain the
results:

The `wrappedValue` property returns an empty array when there are no fetched
results; for example, because no entities satisfy the predicate, or because
the data store is empty.

## See Also

### Getting the fetched results

`func update()`

Updates the fetched results.

Available when `SectionIdentifier` conforms to `Hashable` and `Result`
conforms to `NSFetchRequestResult`.

Collection

API Collection

# DynamicProperty Implementations

## Topics

### Instance Methods

`func update()`

Updates the fetched results.

Available when `SectionIdentifier` conforms to `Hashable` and `Result`
conforms to `NSFetchRequestResult`.

