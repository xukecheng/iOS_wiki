Initializer

# init(fetchRequest:managedObjectContext:sectionNameKeyPath:cacheName:)

Returns a fetch request controller initialized using the given arguments.

iOS 3.0+  iPadOS 3.0+  macOS 10.12+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    init(
        fetchRequest: NSFetchRequest<ResultType>,
        managedObjectContext context: NSManagedObjectContext,
        sectionNameKeyPath: String?,
        cacheName name: String?
    )

##  Parameters

`fetchRequest`

    

The fetch request used to get the objects.

The fetch request must have at least one sort descriptor. If the controller
generates sections, the first sort descriptor in the array is used to group
the objects into sections; its key must either be the same as
`sectionNameKeyPath` or the relative ordering using its key must match that
using `sectionNameKeyPath`.

Important

You must not modify `fetchRequest` after invoking this method. For example,
you must not change its predicate or the sort orderings.

`context`

    

The managed object against which `fetchRequest` is executed.

`sectionNameKeyPath`

    

A key path on result objects that returns the section name. Pass `nil` to
indicate that the controller should generate a single section.

The section name is used to pre-compute the section information.

If this key path is not the same as that specified by the first sort
descriptor in `fetchRequest`, they must generate the same relative orderings.
For example, the first sort descriptor in `fetchRequest` might specify the key
for a persistent property; `sectionNameKeyPath` might specify a key for a
transient property derived from the persistent property.

`name`

    

The name of the cache file the receiver should use. Pass `nil` to prevent
caching.

Pre-computed section info is cached to a private directory under this name. If
Core Data finds a cache stored with this name, it is checked to see if it
matches the `fetchRequest`. If it does, the cache is loaded directly—this
avoids the overhead of computing the section and index information. If the
cached information doesn’t match the request, the cache is deleted and
recomputed when the fetch happens.

## Return Value

The receiver initialized with the specified fetch request, context, key path,
and cache name.

## See Also

### Initializing a Fetched Results Controller

`func performFetch()`

Executes the controller’s fetch request.

### Related Documentation

Core Data Programming Guide

Instance Method

# performFetch()

Executes the controller’s fetch request.

iOS 3.0+  iPadOS 3.0+  macOS 10.12+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func performFetch() throws

## Discussion

After you execute this method, access the controller’s fetched objects using
the `fetchedObjects` property.

Important

If you specify a value for the `sectionNameKeyPath` parameter when you
initialize the fetched results controller, the fetch request must include a
sort descriptor for the corresponding key path; otherwise, the fetch fails.

## See Also

### Initializing a Fetched Results Controller

`init(fetchRequest: NSFetchRequest<ResultType>, managedObjectContext:
NSManagedObjectContext, sectionNameKeyPath: String?, cacheName: String?)`

Returns a fetch request controller initialized using the given arguments.

Instance Property

# fetchRequest

The fetch request used to do the fetching.

iOS 3.0+  iPadOS 3.0+  macOS 10.12+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var fetchRequest: NSFetchRequest<ResultType> { get }

## Discussion

If you want to modify the fetch request, you must follow the steps described
in Modifying the fetch request.

## See Also

### Getting Configuration Information

`var managedObjectContext: NSManagedObjectContext`

The managed object context used to fetch objects.

`var sectionNameKeyPath: String?`

The key path of the attribute that determines which section the fetched entity
belongs to.

`var cacheName: String?`

The name of the file used to cache section information.

`var delegate: (any NSFetchedResultsControllerDelegate)?`

The object that is notified when the fetched results changed.

`class func deleteCache(withName: String?)`

Deletes the cached section information with the given name.

### Related Documentation

`init(fetchRequest: NSFetchRequest<ResultType>, managedObjectContext:
NSManagedObjectContext, sectionNameKeyPath: String?, cacheName: String?)`

Returns a fetch request controller initialized using the given arguments.

Instance Property

# managedObjectContext

The managed object context used to fetch objects.

iOS 3.0+  iPadOS 3.0+  macOS 10.12+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var managedObjectContext: NSManagedObjectContext { get }

## Discussion

The controller registers to listen to change notifications on this context and
properly update its result set and section information.

## See Also

### Getting Configuration Information

`var fetchRequest: NSFetchRequest<ResultType>`

The fetch request used to do the fetching.

`var sectionNameKeyPath: String?`

The key path of the attribute that determines which section the fetched entity
belongs to.

`var cacheName: String?`

The name of the file used to cache section information.

`var delegate: (any NSFetchedResultsControllerDelegate)?`

The object that is notified when the fetched results changed.

`class func deleteCache(withName: String?)`

Deletes the cached section information with the given name.

Instance Property

# sectionNameKeyPath

The key path of the attribute that determines which section the fetched entity
belongs to.

iOS 3.0+  iPadOS 3.0+  macOS 10.12+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var sectionNameKeyPath: String? { get }

## Discussion

This property returns the value you specify for the `sectionNameKeyPath`
parameter when you initialize the fetched results controller.

If the controller generates sections, typically this property’s value matches
the specified key path of the first sort descriptor in the controller’s fetch
request. If the two key paths don’t match, then they must generate the same
relative ordering. For example, the fetch request’s first sort descriptor
might specify the key path of a persistent attribute, but `sectionNameKeyPath`
might specify the key path of a transient attribute that derives its value
from the persistent one.

## See Also

### Getting Configuration Information

`var fetchRequest: NSFetchRequest<ResultType>`

The fetch request used to do the fetching.

`var managedObjectContext: NSManagedObjectContext`

The managed object context used to fetch objects.

`var cacheName: String?`

The name of the file used to cache section information.

`var delegate: (any NSFetchedResultsControllerDelegate)?`

The object that is notified when the fetched results changed.

`class func deleteCache(withName: String?)`

Deletes the cached section information with the given name.

Instance Property

# cacheName

The name of the file used to cache section information.

iOS 3.0+  iPadOS 3.0+  macOS 10.12+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var cacheName: String? { get }

## Discussion

The file itself is stored in a private directory; you can only access it by
name using `deleteCache(withName:)`

## See Also

### Getting Configuration Information

`var fetchRequest: NSFetchRequest<ResultType>`

The fetch request used to do the fetching.

`var managedObjectContext: NSManagedObjectContext`

The managed object context used to fetch objects.

`var sectionNameKeyPath: String?`

The key path of the attribute that determines which section the fetched entity
belongs to.

`var delegate: (any NSFetchedResultsControllerDelegate)?`

The object that is notified when the fetched results changed.

`class func deleteCache(withName: String?)`

Deletes the cached section information with the given name.

### Related Documentation

`init(fetchRequest: NSFetchRequest<ResultType>, managedObjectContext:
NSManagedObjectContext, sectionNameKeyPath: String?, cacheName: String?)`

Returns a fetch request controller initialized using the given arguments.

Instance Property

# delegate

The object that is notified when the fetched results changed.

iOS 3.0+  iPadOS 3.0+  macOS 10.12+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    unowned(unsafe) var delegate: (any NSFetchedResultsControllerDelegate)? { get set }

## Discussion

If you do not specify a delegate, the controller does not track changes to
managed objects associated with its managed object context.

## See Also

### Getting Configuration Information

`var fetchRequest: NSFetchRequest<ResultType>`

The fetch request used to do the fetching.

`var managedObjectContext: NSManagedObjectContext`

The managed object context used to fetch objects.

`var sectionNameKeyPath: String?`

The key path of the attribute that determines which section the fetched entity
belongs to.

`var cacheName: String?`

The name of the file used to cache section information.

`class func deleteCache(withName: String?)`

Deletes the cached section information with the given name.

Type Method

# deleteCache(withName:)

Deletes the cached section information with the given name.

iOS 3.0+  iPadOS 3.0+  macOS 10.12+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    class func deleteCache(withName name: String?)

##  Parameters

`name`

    

The name of the cache file to delete.

If `name` is `nil`, deletes all cache files.

## See Also

### Getting Configuration Information

`var fetchRequest: NSFetchRequest<ResultType>`

The fetch request used to do the fetching.

`var managedObjectContext: NSManagedObjectContext`

The managed object context used to fetch objects.

`var sectionNameKeyPath: String?`

The key path of the attribute that determines which section the fetched entity
belongs to.

`var cacheName: String?`

The name of the file used to cache section information.

`var delegate: (any NSFetchedResultsControllerDelegate)?`

The object that is notified when the fetched results changed.

Instance Property

# fetchedObjects

The results of the fetch.

iOS 3.0+  iPadOS 3.0+  macOS 10.12+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var fetchedObjects: [ResultType]? { get }

## Discussion

The value of the property is `nil` if `performFetch()` hasn’t been called.

The results array only includes instances of the entity specified by the fetch
request (`fetchRequest`) and that match its predicate. (If the fetch request
has no predicate, then the results array includes all instances of the entity
specified by the fetch request.)

The results array reflects the in-memory state of managed objects in the
controller’s managed object context, not their state in the persistent store.
The returned array does not, however, update as managed objects are inserted,
modified, or deleted.

## See Also

### Accessing Results

`func object(at: IndexPath) -> ResultType`

Returns the object at the given index path in the fetch results.

`func indexPath(forObject: ResultType) -> IndexPath?`

Returns the index path of a given object.

### Related Documentation

`func fetch(NSFetchRequest<any NSFetchRequestResult>) -> [Any]`

Returns an array of objects that meet the criteria of the specified fetch
request.

Instance Method

# object(at:)

Returns the object at the given index path in the fetch results.

iOS 3.0+  iPadOS 3.0+  macOS 10.12+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func object(at indexPath: IndexPath) -> ResultType

##  Parameters

`indexPath`

    

An index path in the fetch results.

If `indexPath` does not describe a valid index path in the fetch results, an
exception is raised.

## Return Value

The object at a given index path in the fetch results.

## See Also

### Accessing Results

`var fetchedObjects: [ResultType]?`

The results of the fetch.

`func indexPath(forObject: ResultType) -> IndexPath?`

Returns the index path of a given object.

Instance Method

# indexPath(forObject:)

Returns the index path of a given object.

iOS 3.0+  iPadOS 3.0+  macOS 10.12+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func indexPath(forObject object: ResultType) -> IndexPath?

##  Parameters

`object`

    

An object in the receiver’s fetch results.

## Return Value

The index path of `object` in the receiver’s fetch results, or `nil` if
`object` could not be found.

## Discussion

In versions of iOS before 3.2, this method raises an exception if `object` is
not contained in the receiver’s fetch results.

## See Also

### Accessing Results

`var fetchedObjects: [ResultType]?`

The results of the fetch.

`func object(at: IndexPath) -> ResultType`

Returns the object at the given index path in the fetch results.

Instance Property

# sections

The sections for the fetch results.

iOS 3.0+  iPadOS 3.0+  macOS 10.12+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var sections: [any NSFetchedResultsSectionInfo]? { get }

## Discussion

The objects in the sections array implement the `NSFetchedResultsSectionInfo`
protocol.

You typically use the sections array when implementing `UITableViewDataSource`
methods, such as `numberOfSections(in:)` and
`tableView(_:titleForHeaderInSection:)`.

## See Also

### Querying Section Information

`func section(forSectionIndexTitle: String, at: Int) -> Int`

Returns the section number for a given section title and index in the section
index.

Instance Method

# section(forSectionIndexTitle:at:)

Returns the section number for a given section title and index in the section
index.

iOS 3.0+  iPadOS 3.0+  macOS 10.12+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func section(
        forSectionIndexTitle title: String,
        at sectionIndex: Int
    ) -> Int

##  Parameters

`title`

    

The title of a section

`sectionIndex`

    

The index of a section.

## Return Value

The section number for the given section title and index in the section index

## Discussion

You would typically call this method when executing `UITableViewDataSource`’s
`tableView(_:sectionForSectionIndexTitle:at:)` method.

## See Also

### Querying Section Information

`var sections: [any NSFetchedResultsSectionInfo]?`

The sections for the fetch results.

Instance Method

# sectionIndexTitle(forSectionName:)

Returns the corresponding section index entry for a given section name.

iOS 3.0+  iPadOS 3.0+  macOS 10.12+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func sectionIndexTitle(forSectionName sectionName: String) -> String?

##  Parameters

`sectionName`

    

The name of a section.

## Return Value

The section index entry corresponding to the section with name `sectionName`.

## Discussion

The default implementation returns the capitalized first letter of the section
name.

You should override this method if you need a different way to convert from a
section name to its name in the section index.

### Special Considerations

You only need this method if you use a section index.

## See Also

### Configuring Section Information

`var sectionIndexTitles: [String]`

The array of section index titles.

Instance Property

# sectionIndexTitles

The array of section index titles.

iOS 3.0+  iPadOS 3.0+  macOS 10.12+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var sectionIndexTitles: [String] { get }

## Discussion

The default implementation returns the array created by calling
`sectionIndexTitle(forSectionName:)` on all the known sections. You should
override this method if you want to return a different array for the section
index.

### Special Considerations

You only need this method if you use a section index.

## See Also

### Configuring Section Information

`func sectionIndexTitle(forSectionName: String) -> String?`

Returns the corresponding section index entry for a given section name.

