Initializer

# init(sortDescriptors:predicate:animation:)

Creates a fetch request based on a predicate and value type sort parameters.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    @MainActor
    init(
        sortDescriptors: [SortDescriptor<Result>],
        predicate: NSPredicate? = nil,
        animation: Animation? = nil
    )

Available when `Result` inherits `NSManagedObject`.

##  Parameters

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
type explicitly, use the `init(entity:sortDescriptors:predicate:animation:)`
initializer instead. If you need more control over the fetch request
configuration, use `init(fetchRequest:animation:)`. For reference type sort
descriptors, use `init(sortDescriptors:predicate:animation:)`.

## See Also

### Creating a fetch request

`init(sortDescriptors: [NSSortDescriptor], predicate: NSPredicate?, animation:
Animation?)`

Creates a fetch request based on a predicate and reference type sort
parameters.

Available when `Result` inherits `NSManagedObject`.

`init(entity: NSEntityDescription, sortDescriptors: [NSSortDescriptor],
predicate: NSPredicate?, animation: Animation?)`

Creates a fetch request for a specified entity description, based on a
predicate and sort parameters.

Available when `Result` conforms to `NSFetchRequestResult`.

Initializer

# init(sortDescriptors:predicate:animation:)

Creates a fetch request based on a predicate and reference type sort
parameters.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @MainActor
    init(
        sortDescriptors: [NSSortDescriptor],
        predicate: NSPredicate? = nil,
        animation: Animation? = nil
    )

Available when `Result` inherits `NSManagedObject`.

##  Parameters

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
type explicitly, use the `init(entity:sortDescriptors:predicate:animation:)`
initializer instead. If you need more control over the fetch request
configuration, use `init(fetchRequest:animation:)`. For value type sort
descriptors, use `init(sortDescriptors:predicate:animation:)`.

## See Also

### Creating a fetch request

`init(sortDescriptors: [SortDescriptor<Result>], predicate: NSPredicate?,
animation: Animation?)`

Creates a fetch request based on a predicate and value type sort parameters.

Available when `Result` inherits `NSManagedObject`.

`init(entity: NSEntityDescription, sortDescriptors: [NSSortDescriptor],
predicate: NSPredicate?, animation: Animation?)`

Creates a fetch request for a specified entity description, based on a
predicate and sort parameters.

Available when `Result` conforms to `NSFetchRequestResult`.

Initializer

# init(entity:sortDescriptors:predicate:animation:)

Creates a fetch request for a specified entity description, based on a
predicate and sort parameters.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @MainActor
    init(
        entity: NSEntityDescription,
        sortDescriptors: [NSSortDescriptor],
        predicate: NSPredicate? = nil,
        animation: Animation? = nil
    )

Available when `Result` conforms to `NSFetchRequestResult`.

##  Parameters

`entity`

    

The description of the Core Data entity to fetch.

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
declaration, use the `init(sortDescriptors:predicate:animation:)` initializer
to let the request infer the entity type. If you need more control over the
fetch request configuration, use `init(fetchRequest:animation:)`.

## See Also

### Creating a fetch request

`init(sortDescriptors: [SortDescriptor<Result>], predicate: NSPredicate?,
animation: Animation?)`

Creates a fetch request based on a predicate and value type sort parameters.

Available when `Result` inherits `NSManagedObject`.

`init(sortDescriptors: [NSSortDescriptor], predicate: NSPredicate?, animation:
Animation?)`

Creates a fetch request based on a predicate and reference type sort
parameters.

Available when `Result` inherits `NSManagedObject`.

Initializer

# init(fetchRequest:animation:)

Creates a fully configured fetch request that uses the specified animation
when updating results.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @MainActor
    init(
        fetchRequest: NSFetchRequest<Result>,
        animation: Animation? = nil
    )

Available when `Result` conforms to `NSFetchRequestResult`.

##  Parameters

`fetchRequest`

    

An `NSFetchRequest` instance that describes the search criteria for retrieving
data from the persistent store.

`animation`

    

The animation to use for user interface changes that result from changes to
the fetched results.

## Discussion

Use this initializer when you want to configure a fetch request with more than
a predicate and sort descriptors. For example, you can vend a request from a
`Quake` managed object that the Loading and Displaying a Large Data Feed
sample code project defines to store earthquake data. Limit the number of
results to `1000` by setting a `fetchLimit` for the request:

Use the request to define a `FetchedResults` property:

If you only need to configure the request’s predicate and sort descriptors,
use `init(sortDescriptors:predicate:animation:)` instead. If you need to
specify a `Transaction` rather than an optional `Animation`, use
`init(fetchRequest:transaction:)`.

## See Also

### Creating a fully configured fetch request

`init(fetchRequest: NSFetchRequest<Result>, transaction: Transaction)`

Creates a fully configured fetch request that uses the specified transaction
when updating results.

Available when `Result` conforms to `NSFetchRequestResult`.

Initializer

# init(fetchRequest:transaction:)

Creates a fully configured fetch request that uses the specified transaction
when updating results.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @MainActor
    init(
        fetchRequest: NSFetchRequest<Result>,
        transaction: Transaction
    )

Available when `Result` conforms to `NSFetchRequestResult`.

##  Parameters

`fetchRequest`

    

An `NSFetchRequest` instance that describes the search criteria for retrieving
data from the persistent store.

`transaction`

    

A transaction to use for user interface changes that result from changes to
the fetched results.

## Discussion

Use this initializer if you need a fetch request with updates that affect the
user interface based on a `Transaction`. Otherwise, use
`init(fetchRequest:animation:)`.

## See Also

### Creating a fully configured fetch request

`init(fetchRequest: NSFetchRequest<Result>, animation: Animation?)`

Creates a fully configured fetch request that uses the specified animation
when updating results.

Available when `Result` conforms to `NSFetchRequestResult`.

Structure

# FetchRequest.Configuration

The request’s configurable properties.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    struct Configuration

## Overview

You initialize a `FetchRequest` with an optional predicate and sort
descriptors, either explicitly or using a configured `NSFetchRequest`. Later,
you can dynamically update the predicate and sort parameters using the
request’s configuration structure.

You access or bind to a request’s configuration components through properties
on the associated `FetchedResults` instance.

### Configure using a binding

Get a `Binding` to a fetch request’s configuration structure by accessing the
request’s `projectedValue`, which you do by using the dollar sign (`$`) prefix
on the associated results property. For example, you can create a request for
`Quake` entities — a managed object type that the Loading and Displaying a
Large Data Feed sample code project defines — that initially sorts the results
by time:

Then you can bind the request’s sort descriptors, which you access through the
`quakes` result, to those of a `Table` instance:

A user who clicks on a table column header initiates the following sequence of
events:

  1. The table updates the sort descriptors through the binding.

  2. The modified sort descriptors reconfigure the request.

  3. The reconfigured request fetches new results.

  4. SwiftUI redraws the table in response to new results.

### Set configuration directly

If you need to access the fetch request’s configuration elements directly, use
the `nsPredicate` and `sortDescriptors` or `nsSortDescriptors` properties of
the `FetchedResults` instance. Continuing the example above, to enable the
user to dynamically update the predicate, declare a `State` property to hold a
query string:

Then add an `onChange(of:initial:_:)` modifier to the `Table` that sets a new
predicate any time the query changes:

To give the user control over the string, add a `TextField` in your user
interface that’s bound to the `query` state:

When the user types into the text field, the predicate updates, the request
fetches new results, and SwiftUI redraws the table.

## Topics

### Setting a predicate

`var nsPredicate: NSPredicate?`

The request’s predicate.

### Setting sort descriptors

`var sortDescriptors: [SortDescriptor<Result>]`

The request’s sort descriptors, accessed as value types.

Available when `Result` inherits `NSManagedObject`.

`var nsSortDescriptors: [NSSortDescriptor]`

The request’s sort descriptors, accessed as reference types.

## See Also

### Configuring a request dynamically

`var projectedValue: Binding<FetchRequest<Result>.Configuration>`

A binding to the request’s mutable configuration properties.

Instance Property

# projectedValue

A binding to the request’s mutable configuration properties.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    @MainActor
    var projectedValue: Binding<FetchRequest<Result>.Configuration> { get }

## Discussion

SwiftUI returns the value associated with this property when you use
`FetchRequest` as a property wrapper on a `FetchedResults` instance, and then
access the results with a dollar sign (`$`) prefix. The value that SwiftUI
returns is a `Binding` to the request’s `FetchRequest.Configuration`
structure, which dynamically configures the request.

For example, consider the following fetch request for a type that the Loading
and Displaying a Large Data Feed sample code project defines to store
earthquake data, sorted based on the `time` property:

You can use the projected value to enable a `Table` instance to make updates:

Because you initialize the table using a binding to the descriptors, the table
can modify the sort in response to actions that the user takes, like clicking
a column header.

## See Also

### Configuring a request dynamically

`struct Configuration`

The request’s configurable properties.

Instance Method

# update()

Updates the fetched results.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @MainActor
    mutating func update()

Available when `Result` conforms to `NSFetchRequestResult`.

## Discussion

SwiftUI calls this function before rendering a view’s `body` to ensure the
view has the most recent fetched results.

## See Also

### Getting the fetched results

`var wrappedValue: FetchedResults<Result>`

The fetched results of the fetch request.

Instance Property

# wrappedValue

The fetched results of the fetch request.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @MainActor
    var wrappedValue: FetchedResults<Result> { get }

## Discussion

SwiftUI returns the value associated with this property when you use
`FetchRequest` as a property wrapper, and then access the wrapped property by
name. For example, consider the following `quakes` property declaration that
fetches a `Quake` type that the Loading and Displaying a Large Data Feed
sample code project defines:

You access the request’s `wrappedValue`, which contains a `FetchedResults`
instance, by referring to the `quakes` property by name:

If you need to separate the request and the result entities, you can declare
`quakes` in two steps by using the request’s `wrappedValue` to obtain the
results:

The `wrappedValue` property returns an empty array when there are no fetched
results — for example, because no entities satisfy the predicate, or because
the data store is empty.

## See Also

### Getting the fetched results

`func update()`

Updates the fetched results.

Available when `Result` conforms to `NSFetchRequestResult`.

Collection

API Collection

# DynamicProperty Implementations

## Topics

### Instance Methods

`func update()`

Updates the fetched results.

Available when `Result` conforms to `NSFetchRequestResult`.

