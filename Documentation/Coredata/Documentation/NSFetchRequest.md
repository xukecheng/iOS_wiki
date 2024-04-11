Initializer

# init()

Creates a new fetch request.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    init()

## See Also

### Managing the Fetch Request’s Entity

`init(entityName: String)`

Initializes a fetch request configured with a given entity name.

`var entityName: String?`

The name of the entity the request is configured to fetch.

`var entity: NSEntityDescription?`

The entity specified for the fetch request.

`var includesSubentities: Bool`

A Boolean value that indicates whether the fetch request includes subentities
in the results.

`struct NSFetchRequestResultType`

Constants that specify the possible result types a fetch request can return.

Initializer

# init(entityName:)

Initializes a fetch request configured with a given entity name.

iOS 4.0+  iPadOS 4.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    convenience init(entityName: String)

##  Parameters

`entityName`

    

The name of the entity to fetch.

## Return Value

A fetch request configured to fetch using the entity named `entityName`.

## Discussion

This method provides a convenient way to configure the entity for a fetch
request without having to retrieve an `NSEntityDescription` object. When the
fetch is executed, the request uses the managed object context to find the
entity with the given name. The model associated with the context’s persistent
store coordinator must contain an entity named `entityName`.

## See Also

### Managing the Fetch Request’s Entity

`init()`

Creates a new fetch request.

`var entityName: String?`

The name of the entity the request is configured to fetch.

`var entity: NSEntityDescription?`

The entity specified for the fetch request.

`var includesSubentities: Bool`

A Boolean value that indicates whether the fetch request includes subentities
in the results.

`struct NSFetchRequestResultType`

Constants that specify the possible result types a fetch request can return.

### Related Documentation

`+ fetchRequestWithEntityName:`

Returns a fetch request configured with a given entity name.

Instance Property

# entityName

The name of the entity the request is configured to fetch.

iOS 4.0+  iPadOS 4.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var entityName: String? { get }

## Discussion

The entity name property is populated whenever the NSFetchRequest is created
with `init(entityName:)` or `fetchRequestWithEntityName:`.

## See Also

### Managing the Fetch Request’s Entity

`init()`

Creates a new fetch request.

`init(entityName: String)`

Initializes a fetch request configured with a given entity name.

`var entity: NSEntityDescription?`

The entity specified for the fetch request.

`var includesSubentities: Bool`

A Boolean value that indicates whether the fetch request includes subentities
in the results.

`struct NSFetchRequestResultType`

Constants that specify the possible result types a fetch request can return.

### Related Documentation

`+ fetchRequestWithEntityName:`

Returns a fetch request configured with a given entity name.

Instance Property

# entity

The entity specified for the fetch request.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var entity: NSEntityDescription? { get set }

## Discussion

When an `NSFetchRequest` instance is created with `init()`, it is expected
that the `entity` property will be set. If this property is not set, the fetch
request fails upon execution.

## See Also

### Managing the Fetch Request’s Entity

`init()`

Creates a new fetch request.

`init(entityName: String)`

Initializes a fetch request configured with a given entity name.

`var entityName: String?`

The name of the entity the request is configured to fetch.

`var includesSubentities: Bool`

A Boolean value that indicates whether the fetch request includes subentities
in the results.

`struct NSFetchRequestResultType`

Constants that specify the possible result types a fetch request can return.

### Related Documentation

`+ fetchRequestWithEntityName:`

Returns a fetch request configured with a given entity name.

Instance Property

# includesSubentities

A Boolean value that indicates whether the fetch request includes subentities
in the results.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var includesSubentities: Bool { get set }

## Discussion

The value is `true` if the request will include all subentities of the entity
for the request; otherwise it is `false`. The default is `true`.

## See Also

### Managing the Fetch Request’s Entity

`init()`

Creates a new fetch request.

`init(entityName: String)`

Initializes a fetch request configured with a given entity name.

`var entityName: String?`

The name of the entity the request is configured to fetch.

`var entity: NSEntityDescription?`

The entity specified for the fetch request.

`struct NSFetchRequestResultType`

Constants that specify the possible result types a fetch request can return.

Instance Property

# predicate

The predicate of the fetch request.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var predicate: NSPredicate? { get set }

## Discussion

The predicate instance constrains the selection of objects the
`NSFetchRequest` instance is to fetch.

If the predicate is empty—for example, if it is an `AND` predicate whose array
of elements contains no predicates—the request has its predicate set to `nil`.
For more about predicates, see Predicate Programming Guide.

## See Also

### Specifying Fetch Constraints

`var fetchLimit: Int`

The fetch limit of the fetch request.

`var fetchOffset: Int`

The fetch offset of the fetch request.

`var fetchBatchSize: Int`

The batch size of the objects specified in the fetch request.

`var affectedStores: [NSPersistentStore]?`

An array of persistent stores specified for the fetch request.

`class NSFetchRequestExpression`

An expression that evaluates the result of a fetch request on a managed object
context.

`class NSExpressionDescription`

An object that describes an expression to include with a fetch request.

`class NSFetchedPropertyDescription`

A description object used to define which properties are fetched from Core
Data.

Instance Property

# fetchLimit

The fetch limit of the fetch request.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var fetchLimit: Int { get set }

## Discussion

The fetch limit specifies the maximum number of objects that a request should
return when executed.

If you set a fetch limit, the framework makes a best effort to improve
efficiency, but does not guarantee it. For every object store except the SQL
store, a fetch request executed with a fetch limit in effect simply performs
an unlimited fetch and throws away the unasked for rows.

## See Also

### Specifying Fetch Constraints

`var predicate: NSPredicate?`

The predicate of the fetch request.

`var fetchOffset: Int`

The fetch offset of the fetch request.

`var fetchBatchSize: Int`

The batch size of the objects specified in the fetch request.

`var affectedStores: [NSPersistentStore]?`

An array of persistent stores specified for the fetch request.

`class NSFetchRequestExpression`

An expression that evaluates the result of a fetch request on a managed object
context.

`class NSExpressionDescription`

An object that describes an expression to include with a fetch request.

`class NSFetchedPropertyDescription`

A description object used to define which properties are fetched from Core
Data.

Instance Property

# fetchOffset

The fetch offset of the fetch request.

iOS 3.0+  iPadOS 3.0+  macOS 10.6+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var fetchOffset: Int { get set }

## Discussion

The default value is `0`.

This setting allows you to specify an offset at which rows will begin being
returned. Effectively, the request skips the specified number of matching
entries. For example, given a fetch that typically returns `a, b, c, d`,
specifying an offset of 1 will return `b, c, d`, and an offset of 4 will
return an empty array. Offsets are ignored in nested requests such as
subqueries.

This property can be used to restrict the working set of data. In combination
with `fetchLimit`, you can create a subrange of an arbitrary result set.

## See Also

### Specifying Fetch Constraints

`var predicate: NSPredicate?`

The predicate of the fetch request.

`var fetchLimit: Int`

The fetch limit of the fetch request.

`var fetchBatchSize: Int`

The batch size of the objects specified in the fetch request.

`var affectedStores: [NSPersistentStore]?`

An array of persistent stores specified for the fetch request.

`class NSFetchRequestExpression`

An expression that evaluates the result of a fetch request on a managed object
context.

`class NSExpressionDescription`

An object that describes an expression to include with a fetch request.

`class NSFetchedPropertyDescription`

A description object used to define which properties are fetched from Core
Data.

Instance Property

# fetchBatchSize

The batch size of the objects specified in the fetch request.

iOS 3.0+  iPadOS 3.0+  macOS 10.6+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var fetchBatchSize: Int { get set }

## Discussion

The default value is `0`. A batch size of `0` is treated as infinite, which
disables the batch fetching behavior.

If you set a nonzero batch size, the collection of objects returned when an
instance of `NSFetchRequest` is executed is broken into batches. When the
fetch is executed, the entire request is evaluated and the identities of all
matching objects recorded, but only data for objects up to the `batchSize`
will be fetched from the persistent store at a time. The array returned from
executing the request is a proxy object that transparently fetches subsequent
batches on demand. (In database terms, this is an in-memory cursor.)

You can use this feature to restrict the working set of data in your
application. In combination with `fetchLimit`, you can create a subrange of an
arbitrary result set.

### Special Considerations

For purposes of thread safety, when the fetch is executed, consider the array
proxy returned as being owned by the managed object context the request is
executed against. Treat the array proxy as if it were a managed object
registered with that context.

## See Also

### Specifying Fetch Constraints

`var predicate: NSPredicate?`

The predicate of the fetch request.

`var fetchLimit: Int`

The fetch limit of the fetch request.

`var fetchOffset: Int`

The fetch offset of the fetch request.

`var affectedStores: [NSPersistentStore]?`

An array of persistent stores specified for the fetch request.

`class NSFetchRequestExpression`

An expression that evaluates the result of a fetch request on a managed object
context.

`class NSExpressionDescription`

An object that describes an expression to include with a fetch request.

`class NSFetchedPropertyDescription`

A description object used to define which properties are fetched from Core
Data.

Instance Property

# affectedStores

An array of persistent stores specified for the fetch request.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var affectedStores: [NSPersistentStore]? { get set }

## Discussion

The contents of the array are the identifiers for the stores to be searched
when the fetch request is executed.

## See Also

### Specifying Fetch Constraints

`var predicate: NSPredicate?`

The predicate of the fetch request.

`var fetchLimit: Int`

The fetch limit of the fetch request.

`var fetchOffset: Int`

The fetch offset of the fetch request.

`var fetchBatchSize: Int`

The batch size of the objects specified in the fetch request.

`class NSFetchRequestExpression`

An expression that evaluates the result of a fetch request on a managed object
context.

`class NSExpressionDescription`

An object that describes an expression to include with a fetch request.

`class NSFetchedPropertyDescription`

A description object used to define which properties are fetched from Core
Data.

Instance Property

# sortDescriptors

The sort descriptors of the fetch request.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var sortDescriptors: [NSSortDescriptor]? { get set }

## Discussion

The sort descriptors specify how the objects returned when the
`NSFetchRequest` is issued should be ordered—for example, by last name and
then by first name. The sort descriptors are applied in the order in which
they appear in the `sortDescriptors` array (serially in lowest-array-index-
first order).

A value of `nil` is treated as no sort descriptors.

Instance Property

# relationshipKeyPathsForPrefetching

The relationship key paths to prefetch along with the entity for the request.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var relationshipKeyPathsForPrefetching: [String]? { get set }

## Discussion

This property is an array of relationship key-path strings in NSKeyValueCoding
notation (as you typically use with `value(forKeyPath:)`). The default value
is an empty array (no prefetching).

Prefetching allows Core Data to obtain related objects in a single fetch (per
entity), rather than incurring subsequent access to the store for each
individual record as their faults are tripped. For example, given an Employee
entity with a relationship to a Department entity, suppose you fetch all the
employees, and then for each print out their name and the name of the
department to which they belong. In this case, a fault might be fired for each
individual Department object. This can represent a significant overhead. You
can avoid this by prefetching the department relationship in the Employee
fetch, as illustrated in Listing 1.

(For more details, see Core Data Performance in Core Data Programming Guide)

Instance Property

# resultType

The result type of the fetch request.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var resultType: NSFetchRequestResultType { get set }

## Discussion

The default value is `managedObjectResultType`.

If you set the value to `managedObjectIDResultType`, and do not include
property values in the request, sort orderings are demoted to “best efforts”
hints.

`includesPendingChanges` discusses with whether pending changes are taken into
account when the `resultType` is set to `managedObjectResultType`.

`includesPropertyValues` discusses whether property values are included or not
by default when the `resultType` is set to `managedObjectResultType`.

## See Also

### Managing How Results Are Returned

`var includesPendingChanges: Bool`

A Boolean value that indicates whether, when the fetch is executed, it matches
against currently unsaved changes in the managed object context.

`var propertiesToFetch: [Any]?`

A collection of either property descriptions or string property names that
specify which properties should be returned by the fetch.

`var returnsDistinctResults: Bool`

A Boolean value that indicates whether the fetch request returns only distinct
values for the fields specified by `propertiesToFetch`.

`var includesPropertyValues: Bool`

A Boolean value that indicates whether, when the fetch is executed, property
data is obtained from the persistent store.

`var shouldRefreshRefetchedObjects: Bool`

A Boolean value that indicates whether the property values of fetched objects
will be updated with the current values in the persistent store.

`var returnsObjectsAsFaults: Bool`

A Boolean value that indicates whether the objects resulting from a fetch
request are faults.

`struct NSFetchRequestResultType`

Constants that specify the possible result types a fetch request can return.

`protocol NSFetchRequestResult`

An abstract protocol used with parameterized fetch requests.

Instance Property

# includesPendingChanges

A Boolean value that indicates whether, when the fetch is executed, it matches
against currently unsaved changes in the managed object context.

iOS 3.0+  iPadOS 3.0+  macOS 10.6+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var includesPendingChanges: Bool { get set }

## Discussion

This value is `true` if when the fetch is executed, the fetch will match
against currently unsaved changes in the managed object context; otherwise the
value is `false`. The default value is `true`.

If the value is `false`, the fetch request doesn't check unsaved changes and
only returns objects that matched the predicate in the persistent store.

### Special Considerations

A value of `true` is not supported in conjunction with the result type
`dictionaryResultType`, including calculation of aggregate results (such as
`max` and `min`). For dictionaries, the array returned from the fetch reflects
the current state in the persistent store, and does not take into account any
pending changes, insertions, or deletions in the context.

If you need to take pending changes into account for some simple aggregations
like `max` and `min`, you can instead use a normal fetch request, sorted on
the attribute you want, with a fetch limit of 1.

## See Also

### Managing How Results Are Returned

`var resultType: NSFetchRequestResultType`

The result type of the fetch request.

`var propertiesToFetch: [Any]?`

A collection of either property descriptions or string property names that
specify which properties should be returned by the fetch.

`var returnsDistinctResults: Bool`

A Boolean value that indicates whether the fetch request returns only distinct
values for the fields specified by `propertiesToFetch`.

`var includesPropertyValues: Bool`

A Boolean value that indicates whether, when the fetch is executed, property
data is obtained from the persistent store.

`var shouldRefreshRefetchedObjects: Bool`

A Boolean value that indicates whether the property values of fetched objects
will be updated with the current values in the persistent store.

`var returnsObjectsAsFaults: Bool`

A Boolean value that indicates whether the objects resulting from a fetch
request are faults.

`struct NSFetchRequestResultType`

Constants that specify the possible result types a fetch request can return.

`protocol NSFetchRequestResult`

An abstract protocol used with parameterized fetch requests.

Instance Property

# propertiesToFetch

A collection of either property descriptions or string property names that
specify which properties should be returned by the fetch.

iOS 3.0+  iPadOS 3.0+  macOS 10.6+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var propertiesToFetch: [Any]? { get set }

## Discussion

Property descriptions can either be instances of `NSPropertyDescription` or
`NSString`. The property descriptions may represent attributes, to-one
relationships, or expressions. The name of an attribute or relationship
description must match the name of a description on the fetch request’s
entity.

### Special Considerations

You must set the entity for the fetch request before setting this value;
otherwise, `NSFetchRequest` throws an `invalidArgumentException` exception.

This property can be set with `managedObjectResultType` and thereby implement
a partial faulting (whereby only some of the properties are populated) of the
returned objects, as well as the `dictionaryResultType` to define what
properties are included in the resulting `NSDictionary`.

## See Also

### Managing How Results Are Returned

`var resultType: NSFetchRequestResultType`

The result type of the fetch request.

`var includesPendingChanges: Bool`

A Boolean value that indicates whether, when the fetch is executed, it matches
against currently unsaved changes in the managed object context.

`var returnsDistinctResults: Bool`

A Boolean value that indicates whether the fetch request returns only distinct
values for the fields specified by `propertiesToFetch`.

`var includesPropertyValues: Bool`

A Boolean value that indicates whether, when the fetch is executed, property
data is obtained from the persistent store.

`var shouldRefreshRefetchedObjects: Bool`

A Boolean value that indicates whether the property values of fetched objects
will be updated with the current values in the persistent store.

`var returnsObjectsAsFaults: Bool`

A Boolean value that indicates whether the objects resulting from a fetch
request are faults.

`struct NSFetchRequestResultType`

Constants that specify the possible result types a fetch request can return.

`protocol NSFetchRequestResult`

An abstract protocol used with parameterized fetch requests.

Instance Property

# returnsDistinctResults

A Boolean value that indicates whether the fetch request returns only distinct
values for the fields specified by `propertiesToFetch`.

iOS 3.0+  iPadOS 3.0+  macOS 10.6+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var returnsDistinctResults: Bool { get set }

## Discussion

This value is used only if a value has been set for `propertiesToFetch`.

This value is `true` if when the fetch is executed, it returns only distinct
values for the fields specified by `propertiesToFetch`; otherwise, the value
is `false`. The default value is `false`.

## See Also

### Managing How Results Are Returned

`var resultType: NSFetchRequestResultType`

The result type of the fetch request.

`var includesPendingChanges: Bool`

A Boolean value that indicates whether, when the fetch is executed, it matches
against currently unsaved changes in the managed object context.

`var propertiesToFetch: [Any]?`

A collection of either property descriptions or string property names that
specify which properties should be returned by the fetch.

`var includesPropertyValues: Bool`

A Boolean value that indicates whether, when the fetch is executed, property
data is obtained from the persistent store.

`var shouldRefreshRefetchedObjects: Bool`

A Boolean value that indicates whether the property values of fetched objects
will be updated with the current values in the persistent store.

`var returnsObjectsAsFaults: Bool`

A Boolean value that indicates whether the objects resulting from a fetch
request are faults.

`struct NSFetchRequestResultType`

Constants that specify the possible result types a fetch request can return.

`protocol NSFetchRequestResult`

An abstract protocol used with parameterized fetch requests.

Instance Property

# includesPropertyValues

A Boolean value that indicates whether, when the fetch is executed, property
data is obtained from the persistent store.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var includesPropertyValues: Bool { get set }

## Discussion

This value is `true` if when the fetch is executed, property data is obtained
from the persistent store; otherwise it is `false`. The default value is
`true`.

You can set `includesPropertyValues` to `false` to avoid creating objects to
represent property values and thereby reduce memory overhead. You typically
should only do so, however, if you are sure that you will not need the actual
property data, or you already have the information in the row cache.
Otherwise, you will incur multiple trips to the database.

During a normal fetch (`includesPropertyValues` is `true`), Core Data fetches
the object ID _and_ property data for the matching records, fills the row
cache with the information, and returns managed objects as faults (see
`returnsObjectsAsFaults`). Although these faults are managed objects, all of
their property data still resides in the row cache until the fault is fired.
When the fault is fired, Core Data retrieves the data from the row cache—there
is no need to go back to the database.

If `includesPropertyValues` is `false`, then Core Data fetches _only_ the
object ID information for the matching records—it does not populate the row
cache. Core Data still returns managed objects because it only needs managed
object IDs to create faults. However, if you subsequently fire the fault, Core
Data looks in the (empty) row cache, doesn't find any data, and then goes back
to the store a second time for the data.

If `includesPropertyValues` is `true` and `resultType` is set to
`managedObjectIDResultType`, the properties are fetched even though they are
not being presented to the application and can result in a significant
performance penalty.

## See Also

### Managing How Results Are Returned

`var resultType: NSFetchRequestResultType`

The result type of the fetch request.

`var includesPendingChanges: Bool`

A Boolean value that indicates whether, when the fetch is executed, it matches
against currently unsaved changes in the managed object context.

`var propertiesToFetch: [Any]?`

A collection of either property descriptions or string property names that
specify which properties should be returned by the fetch.

`var returnsDistinctResults: Bool`

A Boolean value that indicates whether the fetch request returns only distinct
values for the fields specified by `propertiesToFetch`.

`var shouldRefreshRefetchedObjects: Bool`

A Boolean value that indicates whether the property values of fetched objects
will be updated with the current values in the persistent store.

`var returnsObjectsAsFaults: Bool`

A Boolean value that indicates whether the objects resulting from a fetch
request are faults.

`struct NSFetchRequestResultType`

Constants that specify the possible result types a fetch request can return.

`protocol NSFetchRequestResult`

An abstract protocol used with parameterized fetch requests.

Instance Property

# shouldRefreshRefetchedObjects

A Boolean value that indicates whether the property values of fetched objects
will be updated with the current values in the persistent store.

iOS 5.0+  iPadOS 5.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var shouldRefreshRefetchedObjects: Bool { get set }

## Discussion

This value is `true` if the property values of fetched objects will be updated
with the current values in the persistent store; otherwise, it is `false`.

By default when you fetch objects, they maintain their current property
values, even if the values in the persistent store have changed. Invoking this
method with the parameter `true` means that when the fetch is executed, the
property values of fetched objects are updated with the current values in the
persistent store. This is a more convenient way to ensure that managed object
property values are consistent with the store than by using
`refresh(_:mergeChanges:)` (`NSManagedObjetContext`) for multiple objects in
turn.

## See Also

### Managing How Results Are Returned

`var resultType: NSFetchRequestResultType`

The result type of the fetch request.

`var includesPendingChanges: Bool`

A Boolean value that indicates whether, when the fetch is executed, it matches
against currently unsaved changes in the managed object context.

`var propertiesToFetch: [Any]?`

A collection of either property descriptions or string property names that
specify which properties should be returned by the fetch.

`var returnsDistinctResults: Bool`

A Boolean value that indicates whether the fetch request returns only distinct
values for the fields specified by `propertiesToFetch`.

`var includesPropertyValues: Bool`

A Boolean value that indicates whether, when the fetch is executed, property
data is obtained from the persistent store.

`var returnsObjectsAsFaults: Bool`

A Boolean value that indicates whether the objects resulting from a fetch
request are faults.

`struct NSFetchRequestResultType`

Constants that specify the possible result types a fetch request can return.

`protocol NSFetchRequestResult`

An abstract protocol used with parameterized fetch requests.

Instance Property

# returnsObjectsAsFaults

A Boolean value that indicates whether the objects resulting from a fetch
request are faults.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var returnsObjectsAsFaults: Bool { get set }

## Discussion

This value is `true` if the objects resulting from a fetch using the
`NSFetchRequest` are faults; otherwise, it is `false`. The default value is
`true`. This setting is not used if the result type (see `resultType`) is
`NSManagedObjectIDResultType`, as object IDs do not have property values. You
can set `returnsObjectsAsFaults` to `false` to gain a performance benefit if
you know you will need to access the property values from the returned
objects.

When you execute a fetch, by default `returnsObjectsAsFaults` is `true`; Core
Data fetches the object data for the matching records, fills the row cache
with the information, and returns managed object as faults. These faults are
managed objects, but all of their property data resides in the row cache until
the fault is fired. When the fault is fired, Core Data retrieves the data from
the row cache. Although the overhead for this operation is small, for large
datasets it may not be trivial. If you _need_ to access the property values
from the returned objects (for example, if you iterate over all the objects to
calculate the average value of a particular attribute), then it is more
efficient to set `returnsObjectsAsFaults` to `false` to avoid the additional
overhead.

## See Also

### Managing How Results Are Returned

`var resultType: NSFetchRequestResultType`

The result type of the fetch request.

`var includesPendingChanges: Bool`

A Boolean value that indicates whether, when the fetch is executed, it matches
against currently unsaved changes in the managed object context.

`var propertiesToFetch: [Any]?`

A collection of either property descriptions or string property names that
specify which properties should be returned by the fetch.

`var returnsDistinctResults: Bool`

A Boolean value that indicates whether the fetch request returns only distinct
values for the fields specified by `propertiesToFetch`.

`var includesPropertyValues: Bool`

A Boolean value that indicates whether, when the fetch is executed, property
data is obtained from the persistent store.

`var shouldRefreshRefetchedObjects: Bool`

A Boolean value that indicates whether the property values of fetched objects
will be updated with the current values in the persistent store.

`struct NSFetchRequestResultType`

Constants that specify the possible result types a fetch request can return.

`protocol NSFetchRequestResult`

An abstract protocol used with parameterized fetch requests.

Protocol

# NSFetchRequestResult

An abstract protocol used with parameterized fetch requests.

iOS 10.0+  iPadOS 10.0+  macOS 10.12+  Mac Catalyst 13.0+  tvOS 10.0+  watchOS
3.0+  visionOS 1.0+

    
    
    protocol NSFetchRequestResult

## Relationships

### Inherits From

  * `NSObjectProtocol`

### Conforming Types

  * `NSDictionary`
  * `NSManagedObject`
  * `NSManagedObjectID`
  * `NSNumber`

## See Also

### Managing How Results Are Returned

`var resultType: NSFetchRequestResultType`

The result type of the fetch request.

`var includesPendingChanges: Bool`

A Boolean value that indicates whether, when the fetch is executed, it matches
against currently unsaved changes in the managed object context.

`var propertiesToFetch: [Any]?`

A collection of either property descriptions or string property names that
specify which properties should be returned by the fetch.

`var returnsDistinctResults: Bool`

A Boolean value that indicates whether the fetch request returns only distinct
values for the fields specified by `propertiesToFetch`.

`var includesPropertyValues: Bool`

A Boolean value that indicates whether, when the fetch is executed, property
data is obtained from the persistent store.

`var shouldRefreshRefetchedObjects: Bool`

A Boolean value that indicates whether the property values of fetched objects
will be updated with the current values in the persistent store.

`var returnsObjectsAsFaults: Bool`

A Boolean value that indicates whether the objects resulting from a fetch
request are faults.

`struct NSFetchRequestResultType`

Constants that specify the possible result types a fetch request can return.

Instance Property

# propertiesToGroupBy

An array of objects that indicates how data should be grouped before a select
statement is run in a SQL database.

iOS 5.0+  iPadOS 5.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var propertiesToGroupBy: [Any]? { get set }

## Discussion

An array of `NSPropertyDescription` or `NSExpressionDescription` objects or
key-path strings that indicate how data should be grouped before a select
statement is run in an SQL database.

If you use this setting, you must set the `resultType` to
`dictionaryResultType`, and the SELECT values must be literals, aggregates, or
columns specified in `propertiesToGroupBy`.

Aggregates will operate on the groups specified in `propertiesToGroupBy `

rather than the whole table. If you set `propertiesToGroupBy`, you can also
set a predicate to filter rows that are returned by `propertiesToGroupBy`.

See `havingPredicate`.

## See Also

### Grouping and Filtering Dictionary Results

`var havingPredicate: NSPredicate?`

The predicate used to filter rows being returned by a query containing a GROUP
BY directive.

Instance Property

# havingPredicate

The predicate used to filter rows being returned by a query containing a GROUP
BY directive.

iOS 5.0+  iPadOS 5.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var havingPredicate: NSPredicate? { get set }

## Discussion

If a `havingPredicate` value is supplied, the predicate will be run after
``.Specifying a `havingPredicate` requires that `propertiesToGroupBy` also be
specified.

## See Also

### Grouping and Filtering Dictionary Results

`var propertiesToGroupBy: [Any]?`

An array of objects that indicates how data should be grouped before a select
statement is run in a SQL database.

### Related Documentation

`class NSFetchRequest`

A description of search criteria used to retrieve data from a persistent
store.

Instance Method

# execute()

Executes the fetch request against the managed object context that is
associated with the current queue.

iOS 10.0+  iPadOS 10.0+  macOS 10.12+  Mac Catalyst 13.1+  tvOS 10.0+  watchOS
3.0+  visionOS 1.0+

    
    
    func execute() throws -> [ResultType]

## Discussion

Calling `execute` on an `NSFetchRequest` will cause the `NSFetchRequest` to
run against the managed object context (`NSManagedObjectContext`) that is
associated with the queue on which the `execute` is called.

